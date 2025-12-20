#!/usr/bin/env python3
"""
Markdown Template Validator

Validates markdown datasheet templates for:
- YAML frontmatter structure
- Required sections
- Table column structure
- Field type validity
- Dropdown options format (JSON arrays)
- field_id uniqueness across entire template

Usage:
    python scripts/validate_template.py templates/101-GR.md
    python scripts/validate_template.py --all
"""

import argparse
import json
import re
import sys
from pathlib import Path

import yaml


# =============================================================================
# VALIDATION SCHEMAS
# =============================================================================

REQUIRED_FRONTMATTER = {
    'schema_version': int,
    'template_id': str,
    'title': str,
    'service': str,
    'has_motor': bool,
}

OPTIONAL_FRONTMATTER = {
    'category': str,
    'has_electrical': bool,
}

REQUIRED_SECTIONS = [
    'Document Control',
    'Service Information',
    'Operating / Design Data',
    'Materials',
    'Remarks',
    'Revision History',
]

VALID_FIELD_TYPES = ['number', 'text', 'dropdown', 'date', 'readonly']

# Expected column headers for data tables
DATA_TABLE_COLUMNS = ['#', 'field_id', 'Field', 'Value', 'Units', 'Type', 'Options']
MATERIALS_TABLE_COLUMNS = ['#', 'field_id', 'Component', 'Material']


# =============================================================================
# VALIDATION FUNCTIONS
# =============================================================================

class ValidationError:
    """Represents a validation error."""
    def __init__(self, severity: str, message: str, line: int = None):
        self.severity = severity  # 'ERROR' or 'WARNING'
        self.message = message
        self.line = line

    def __str__(self):
        if self.line:
            return f"  [{self.severity}] Line {self.line}: {self.message}"
        return f"  [{self.severity}] {self.message}"


def parse_frontmatter(content: str) -> tuple[dict, int, list[ValidationError]]:
    """Parse and validate YAML frontmatter."""
    errors = []

    if not content.startswith('---'):
        errors.append(ValidationError('ERROR', 'Missing YAML frontmatter (must start with ---)'))
        return {}, 0, errors

    # Find the closing ---
    end_match = re.search(r'\n---\s*\n', content[3:])
    if not end_match:
        errors.append(ValidationError('ERROR', 'Unclosed YAML frontmatter (missing closing ---)'))
        return {}, 0, errors

    yaml_content = content[3:3 + end_match.start()]
    end_line = yaml_content.count('\n') + 2

    try:
        frontmatter = yaml.safe_load(yaml_content)
        if not isinstance(frontmatter, dict):
            errors.append(ValidationError('ERROR', 'Frontmatter must be a YAML dictionary'))
            return {}, end_line, errors
    except yaml.YAMLError as e:
        errors.append(ValidationError('ERROR', f'Invalid YAML: {e}'))
        return {}, end_line, errors

    # Check required fields
    for field, expected_type in REQUIRED_FRONTMATTER.items():
        if field not in frontmatter:
            errors.append(ValidationError('ERROR', f'Missing required frontmatter field: {field}'))
        elif not isinstance(frontmatter.get(field), expected_type):
            actual_type = type(frontmatter.get(field)).__name__
            errors.append(ValidationError('ERROR',
                f'Frontmatter field "{field}" should be {expected_type.__name__}, got {actual_type}'))

    return frontmatter, end_line, errors


def find_sections(content: str) -> dict[str, tuple[int, str]]:
    """Find all ## sections and their line numbers."""
    sections = {}
    lines = content.split('\n')

    for i, line in enumerate(lines, 1):
        match = re.match(r'^##\s+(.+?)\s*$', line)
        if match:
            section_name = match.group(1)
            # Find content until next section or end
            section_content = []
            for j in range(i, len(lines)):
                if re.match(r'^##\s+', lines[j]):
                    break
                section_content.append(lines[j])
            sections[section_name] = (i, '\n'.join(section_content))

    return sections


def validate_table_structure(table_text: str, expected_columns: list[str],
                            section_name: str, base_line: int) -> list[ValidationError]:
    """Validate markdown table structure."""
    errors = []
    lines = [line for line in table_text.strip().split('\n') if line.strip()]

    if len(lines) < 2:
        errors.append(ValidationError('WARNING', f'{section_name}: No table found', base_line))
        return errors

    # Parse header
    header_line = lines[0]
    headers = [h.strip() for h in header_line.split('|') if h.strip()]

    # Check column count
    if len(headers) < len(expected_columns):
        errors.append(ValidationError('WARNING',
            f'{section_name}: Expected {len(expected_columns)} columns, found {len(headers)}',
            base_line))

    # Check for separator line
    if len(lines) > 1 and '---' not in lines[1]:
        errors.append(ValidationError('WARNING',
            f'{section_name}: Missing table separator line (|---|---|...)',
            base_line + 1))

    return errors


def validate_field_types(table_text: str, section_name: str,
                        base_line: int) -> list[ValidationError]:
    """Validate field types in data tables."""
    errors = []
    lines = [line for line in table_text.strip().split('\n') if line.strip()]

    if len(lines) < 3:
        return errors

    # Parse data rows (skip header and separator)
    for i, line in enumerate(lines[2:], 3):
        cells = [c.strip() for c in line.split('|')[1:-1] if line.startswith('|')]
        if len(cells) < 6:
            continue

        # Check field type (column 6, index 5)
        field_type = cells[5].lower() if len(cells) > 5 else ''
        if field_type and field_type not in VALID_FIELD_TYPES:
            errors.append(ValidationError('ERROR',
                f'{section_name}: Invalid field type "{field_type}" (valid: {VALID_FIELD_TYPES})',
                base_line + i))

        # Check dropdown options format (column 7, index 6)
        if field_type == 'dropdown' and len(cells) > 6:
            options = cells[6].strip()
            if options and not options.startswith('['):
                errors.append(ValidationError('WARNING',
                    f'{section_name}: Dropdown options should be JSON array format ["a","b"]',
                    base_line + i))
            elif options.startswith('['):
                try:
                    parsed = json.loads(options)
                    if not isinstance(parsed, list):
                        errors.append(ValidationError('ERROR',
                            f'{section_name}: Dropdown options must be a JSON array',
                            base_line + i))
                except json.JSONDecodeError:
                    errors.append(ValidationError('ERROR',
                        f'{section_name}: Invalid JSON in dropdown options',
                        base_line + i))

    return errors


def extract_field_ids(table_text: str, section_name: str, base_line: int) -> list[tuple[str, str, int]]:
    """Extract field_ids from a table. Returns list of (field_id, section_name, line_number)."""
    field_ids = []
    lines = [line for line in table_text.strip().split('\n') if line.strip()]

    if len(lines) < 3:
        return field_ids

    # Parse data rows (skip header and separator)
    for i, line in enumerate(lines[2:], 3):
        cells = [c.strip() for c in line.split('|')[1:-1] if line.startswith('|')]
        if len(cells) >= 2:
            field_id = cells[1].strip()  # field_id is in column 2 (index 1)
            if field_id:
                field_ids.append((field_id, section_name, base_line + i))

    return field_ids


def validate_field_id_uniqueness(sections: dict[str, tuple[int, str]]) -> list[ValidationError]:
    """Validate that all field_ids are unique across the entire template."""
    errors = []
    all_field_ids = []  # List of (field_id, section_name, line_number)

    # Collect field_ids from all relevant sections
    for section_name, (line_num, section_content) in sections.items():
        if section_name not in ['Operating / Design Data', 'Driver / Motor Data', 'Materials', 'Electrical Data']:
            continue

        # Find table in section
        table_match = re.search(r'(\|.+\|[\s\S]*?)(?=\n\n|\n##|\Z)', section_content)
        if not table_match:
            continue

        table_text = table_match.group(1)
        all_field_ids.extend(extract_field_ids(table_text, section_name, line_num))

    # Check for duplicates
    seen = {}  # field_id -> (section_name, line_number)
    for field_id, section_name, line_num in all_field_ids:
        if field_id in seen:
            orig_section, orig_line = seen[field_id]
            errors.append(ValidationError('ERROR',
                f'Duplicate field_id "{field_id}" (first in {orig_section} line {orig_line}, '
                f'also in {section_name} line {line_num}). Use section prefix (e.g., op.{field_id} / mat.{field_id})',
                line_num))
        else:
            seen[field_id] = (section_name, line_num)

    return errors


def get_all_field_ids(sections: dict[str, tuple[int, str]]) -> set[str]:
    """Extract all field_ids from a template's sections."""
    field_ids = set()
    for section_name, (line_num, section_content) in sections.items():
        if section_name not in ['Operating / Design Data', 'Driver / Motor Data', 'Materials', 'Electrical Data']:
            continue
        table_match = re.search(r'(\|.+\|[\s\S]*?)(?=\n\n|\n##|\Z)', section_content)
        if table_match:
            for field_id, _, _ in extract_field_ids(table_match.group(1), section_name, line_num):
                field_ids.add(field_id)
    return field_ids


def extract_field_refs_from_expr(expr: str) -> list[str]:
    """Extract field name references from a qty_rule expression."""
    if not expr or expr in ('fixed', 'conditional'):
        return []
    # Tokenize expression and extract non-numeric, non-operator tokens
    tokens = re.split(r'\s*[+\-*/]\s*', expr.strip())
    refs = []
    for token in tokens:
        token = token.strip()
        if token and not token.isdigit():
            refs.append(token)
    return refs


def validate_bom_references(template_id: str, field_ids: set[str],
                           components_dir: Path) -> list[ValidationError]:
    """Validate BOM definition references against template field_ids."""
    errors = []
    bom_file = components_dir / f'bom_{template_id}.yaml'

    if not bom_file.exists():
        # No BOM file is not an error - many templates don't have components
        return errors

    try:
        with open(bom_file, 'r') as f:
            bom_data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        errors.append(ValidationError('ERROR', f'Invalid BOM YAML: {e}'))
        return errors

    if not bom_data or 'components' not in bom_data:
        return errors

    for i, component in enumerate(bom_data.get('components', []), 1):
        comp_name = component.get('name', f'component #{i}')

        # Check qty_rule field references
        qty_rule = component.get('qty_rule', 'fixed')
        for ref in extract_field_refs_from_expr(qty_rule):
            if ref not in field_ids:
                errors.append(ValidationError('ERROR',
                    f'BOM "{comp_name}": qty_rule references unknown field "{ref}"'))

        # Check condition_field for conditional rules
        if qty_rule == 'conditional':
            cond_field = component.get('condition_field', '')
            cond_value = component.get('condition_value', '')

            # Validate that conditional rules have required fields
            if not cond_field:
                errors.append(ValidationError('ERROR',
                    f'BOM "{comp_name}": conditional qty_rule requires condition_field'))
            elif cond_field not in field_ids:
                errors.append(ValidationError('ERROR',
                    f'BOM "{comp_name}": condition_field references unknown field "{cond_field}"'))

            if not cond_value:
                errors.append(ValidationError('ERROR',
                    f'BOM "{comp_name}": conditional qty_rule requires condition_value'))

            # Check qty_rule_value if present
            qty_rule_value = component.get('qty_rule_value')
            if qty_rule_value:
                for ref in extract_field_refs_from_expr(str(qty_rule_value)):
                    if ref not in field_ids:
                        errors.append(ValidationError('ERROR',
                            f'BOM "{comp_name}": qty_rule_value references unknown field "{ref}"'))

    return errors


def validate_template(filepath: Path) -> tuple[bool, list[ValidationError]]:
    """Validate a markdown template file."""
    errors = []

    if not filepath.exists():
        errors.append(ValidationError('ERROR', f'File not found: {filepath}'))
        return False, errors

    content = filepath.read_text(encoding='utf-8')

    # Validate frontmatter
    frontmatter, fm_end_line, fm_errors = parse_frontmatter(content)
    errors.extend(fm_errors)

    # Find sections
    sections = find_sections(content)

    # Check required sections
    for section in REQUIRED_SECTIONS:
        if section not in sections:
            errors.append(ValidationError('ERROR', f'Missing required section: {section}'))

    # Check for Driver / Motor Data if has_motor is true
    if frontmatter.get('has_motor', False):
        if 'Driver / Motor Data' not in sections:
            errors.append(ValidationError('ERROR',
                'has_motor is true but "Driver / Motor Data" section is missing'))

    # Validate table structures
    for section_name, (line_num, section_content) in sections.items():
        # Find table in section
        table_match = re.search(r'(\|.+\|[\s\S]*?)(?=\n\n|\n##|\Z)', section_content)
        if not table_match:
            if section_name not in ['Remarks']:  # Remarks might not have a table
                errors.append(ValidationError('WARNING',
                    f'{section_name}: No markdown table found', line_num))
            continue

        table_text = table_match.group(1)

        # Validate based on section type
        if section_name == 'Operating / Design Data':
            errors.extend(validate_table_structure(
                table_text, DATA_TABLE_COLUMNS, section_name, line_num))
            errors.extend(validate_field_types(table_text, section_name, line_num))

        elif section_name == 'Driver / Motor Data':
            errors.extend(validate_table_structure(
                table_text, DATA_TABLE_COLUMNS, section_name, line_num))
            errors.extend(validate_field_types(table_text, section_name, line_num))

        elif section_name == 'Materials':
            errors.extend(validate_table_structure(
                table_text, MATERIALS_TABLE_COLUMNS, section_name, line_num))

    # Validate field_id uniqueness across entire template
    errors.extend(validate_field_id_uniqueness(sections))

    # Validate BOM references if BOM file exists
    if frontmatter.get('template_id'):
        field_ids = get_all_field_ids(sections)
        components_dir = filepath.parent.parent / 'components'
        errors.extend(validate_bom_references(
            frontmatter['template_id'], field_ids, components_dir))

    # Determine pass/fail
    has_errors = any(e.severity == 'ERROR' for e in errors)
    return not has_errors, errors


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description='Validate markdown datasheet templates')
    parser.add_argument('files', nargs='*', help='Markdown files to validate')
    parser.add_argument('--all', action='store_true',
                        help='Validate all templates in templates/ directory')

    args = parser.parse_args()

    # Determine script location for relative paths
    script_dir = Path(__file__).parent
    project_dir = script_dir.parent

    # Collect files to validate
    if args.all:
        templates_dir = project_dir / 'templates'
        files = list(templates_dir.glob('*.md'))
    elif args.files:
        files = [Path(f) for f in args.files]
    else:
        print("Usage: validate_template.py <files...> or --all")
        sys.exit(1)

    if not files:
        print("No template files found")
        sys.exit(1)

    print(f"Validating {len(files)} template(s)...\n")
    print("=" * 60)

    pass_count = 0
    fail_count = 0

    for filepath in sorted(files):
        print(f"\nFile: {filepath.name}")

        passed, errors = validate_template(filepath)

        if passed:
            print("  STATUS: VALID")
            pass_count += 1
        else:
            print("  STATUS: INVALID")
            fail_count += 1

        # Print errors and warnings
        for error in errors:
            print(error)

    print("\n" + "=" * 60)
    print(f"Results: {pass_count} passed, {fail_count} failed")

    if fail_count > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
