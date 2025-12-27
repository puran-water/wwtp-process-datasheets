#!/usr/bin/env python3
"""
Register generated datasheets in the artifact registry.

Scans datasheets directory, validates each datasheet, and registers
them in the project's artifact-registry.yaml.

Usage:
    python scripts/register_datasheets.py --project-dir /path/to/project
    python scripts/register_datasheets.py --project-dir . --datasheets-dir datasheets
"""

import argparse
import hashlib
import sys
from datetime import datetime
from pathlib import Path

import yaml


# Shared infrastructure path
SHARED_DIR = Path(__file__).parent.parent.parent / 'shared'
sys.path.insert(0, str(SHARED_DIR / 'scripts'))

try:
    from register_artifact import register_artifact, load_registry
except ImportError:
    # Fallback if shared scripts not available
    def load_registry(project_dir: Path) -> dict:
        """Load registry from project directory (fallback implementation)."""
        registry_path = project_dir / 'mcp-outputs' / 'artifact-registry.yaml'
        if not registry_path.exists():
            registry_path = project_dir / 'artifact-registry.yaml'
        if registry_path.exists():
            return yaml.safe_load(registry_path.read_text()) or {}
        return {'artifacts': []}

    def register_artifact(registry: dict, artifact: dict) -> dict:
        if 'artifacts' not in registry:
            registry['artifacts'] = []
        # Check for existing artifact with same ID
        existing_ids = {a['id'] for a in registry['artifacts']}
        if artifact['id'] not in existing_ids:
            registry['artifacts'].append(artifact)
        return registry


def calculate_checksum(filepath: Path) -> str:
    """Calculate SHA256 checksum of a file."""
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            sha256.update(chunk)
    return sha256.hexdigest()[:16]  # Truncate for readability


def parse_datasheet_frontmatter(md_path: Path) -> dict:
    """Extract YAML frontmatter from markdown datasheet."""
    content = md_path.read_text(encoding='utf-8')

    if not content.startswith('---'):
        return {}

    # Find closing ---
    end_idx = content.find('\n---', 3)
    if end_idx == -1:
        return {}

    yaml_content = content[3:end_idx]
    try:
        return yaml.safe_load(yaml_content) or {}
    except yaml.YAMLError:
        return {}


def extract_equipment_tag(md_path: Path) -> str:
    """Extract equipment tag from datasheet content."""
    content = md_path.read_text(encoding='utf-8')

    # Look for Equipment Tag in Document Control section
    for line in content.split('\n'):
        if 'Equipment Tag' in line or 'Tag No' in line:
            parts = line.split('|')
            if len(parts) >= 3:
                tag = parts[2].strip()
                if tag:
                    return tag

    # Fallback to filename
    return md_path.stem


def find_matching_xlsx(md_path: Path, datasheets_dir: Path) -> Path | None:
    """Find the Excel file corresponding to a markdown datasheet."""
    # Look for exact match first
    xlsx_path = md_path.with_suffix('.xlsx')
    if xlsx_path.exists():
        return xlsx_path

    # Look in assets directory
    assets_dir = datasheets_dir.parent / 'assets'
    if assets_dir.exists():
        # Try pattern: {template_id}-01 {title}.xlsx
        frontmatter = parse_datasheet_frontmatter(md_path)
        template_id = frontmatter.get('template_id', md_path.stem)
        for xlsx in assets_dir.glob(f'{template_id}*.xlsx'):
            return xlsx

    return None


def create_datasheet_artifact(
    md_path: Path,
    xlsx_path: Path | None,
    project_dir: Path,
    source_artifact_id: str | None = None,
    sequence_num: int = 1
) -> dict:
    """Create artifact entry for a datasheet."""
    frontmatter = parse_datasheet_frontmatter(md_path)
    equipment_tag = extract_equipment_tag(md_path)
    template_id = frontmatter.get('template_id', md_path.stem)

    # Generate artifact ID matching schema pattern ^[a-z]+-[0-9]{3}$
    # Use 'pds' prefix (process-datasheet) with 3-digit sequence
    artifact_id = f"pds-{sequence_num:03d}"

    artifact = {
        'id': artifact_id,
        'type': 'process-datasheet',
        'equipment_tag': equipment_tag,
        'template_id': template_id,
        'title': frontmatter.get('title', ''),
        'service': frontmatter.get('service', ''),
        'category': frontmatter.get('category', ''),
        'source_md': str(md_path.relative_to(project_dir)),
        'output_xlsx': str(xlsx_path.relative_to(project_dir)) if xlsx_path else None,
        'validation': {
            'status': 'draft',
            'completeness_pct': 0,
        },
        'meta': {
            'generated_by': 'process-datasheets-skill',
            'schema_version': frontmatter.get('schema_version', 1),
            'timestamp': datetime.now().isoformat(),
            'checksum_md': calculate_checksum(md_path),
        }
    }

    if xlsx_path and xlsx_path.exists():
        artifact['meta']['checksum_xlsx'] = calculate_checksum(xlsx_path)

    if source_artifact_id:
        artifact['source_artifact'] = source_artifact_id

    return artifact


def scan_and_register(
    project_dir: Path,
    datasheets_dir: Path,
    equipment_list_artifact_id: str | None = None
) -> int:
    """Scan datasheets directory and register all datasheets."""
    registry_path = project_dir / 'mcp-outputs' / 'artifact-registry.yaml'

    if not registry_path.exists():
        # Try alternate location
        registry_path = project_dir / 'artifact-registry.yaml'

    if not registry_path.exists():
        print(f"Warning: artifact-registry.yaml not found in {project_dir}")
        print("Creating new registry...")
        registry = {
            'project_id': project_dir.name,
            'artifacts': []
        }
    else:
        # load_registry expects project_dir (Path), not registry_path (file path)
        # Pass project_dir to be compatible with shared/scripts/register_artifact.py
        registry = load_registry(project_dir)

    # Find all markdown datasheets
    md_files = list(datasheets_dir.glob('*.md'))
    if not md_files:
        print(f"No markdown datasheets found in {datasheets_dir}")
        return 0

    print(f"Found {len(md_files)} datasheets")

    # Find next available sequence number
    existing_pds_ids = [
        a['id'] for a in registry.get('artifacts', [])
        if a.get('id', '').startswith('pds-')
    ]
    next_seq = 1
    if existing_pds_ids:
        # Extract highest sequence number
        max_seq = max(int(id.split('-')[1]) for id in existing_pds_ids)
        next_seq = max_seq + 1

    registered_count = 0
    for md_path in sorted(md_files):
        # Skip project data template
        if md_path.stem == '000-PROJECT-DATA':
            continue

        xlsx_path = find_matching_xlsx(md_path, datasheets_dir)

        artifact = create_datasheet_artifact(
            md_path,
            xlsx_path,
            project_dir,
            equipment_list_artifact_id,
            next_seq + registered_count
        )

        # Check if already registered
        existing_ids = {a['id'] for a in registry.get('artifacts', [])}
        if artifact['id'] in existing_ids:
            print(f"  Updating: {artifact['id']} ({md_path.name})")
            # Update existing
            registry['artifacts'] = [
                a if a['id'] != artifact['id'] else artifact
                for a in registry['artifacts']
            ]
        else:
            print(f"  Registering: {artifact['id']} ({md_path.name})")
            registry['artifacts'].append(artifact)

        registered_count += 1

    # Save registry
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    with open(registry_path, 'w') as f:
        yaml.dump(registry, f, default_flow_style=False, sort_keys=False)

    print(f"\nRegistered {registered_count} datasheets")
    print(f"Registry updated: {registry_path}")

    return registered_count


def main():
    parser = argparse.ArgumentParser(
        description='Register datasheets in artifact registry'
    )
    parser.add_argument('--project-dir', '-p', required=True,
                        help='Project directory path')
    parser.add_argument('--datasheets-dir', '-d', default='datasheets',
                        help='Datasheets directory (default: datasheets)')
    parser.add_argument('--equipment-list-id', '-e',
                        help='ID of source equipment-list artifact')

    args = parser.parse_args()

    project_dir = Path(args.project_dir).resolve()
    if not project_dir.exists():
        print(f"Error: Project directory not found: {project_dir}")
        sys.exit(1)

    datasheets_dir = project_dir / args.datasheets_dir
    if not datasheets_dir.exists():
        # Try templates directory (skill's own templates)
        datasheets_dir = Path(__file__).parent.parent / 'templates'

    if not datasheets_dir.exists():
        print(f"Error: Datasheets directory not found: {datasheets_dir}")
        sys.exit(1)

    count = scan_and_register(
        project_dir,
        datasheets_dir,
        args.equipment_list_id
    )

    if count == 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
