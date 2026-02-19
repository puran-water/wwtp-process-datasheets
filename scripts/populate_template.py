#!/usr/bin/env python3
"""
Populate Datasheet Template with Equipment Data

Maps equipment-list fields to template field_ids and fills Value columns.
Can be used standalone or imported by md_to_excel.py.

Usage:
    python populate_template.py \
        --template templates/PP-LOBE.md \
        --equipment-data equipment-list.qmd \
        --tag 200-P-01 \
        --output populated/PP-LOBE-200-P-01.md

    python populate_template.py \
        --template templates/640-DIG.md \
        --equipment-data equipment-list.yaml \
        --tag 200-DIG-01 \
        --project-id CH2O-2022-CBG-005
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Any, Optional

import yaml


SCRIPT_DIR = Path(__file__).parent
CATALOG_DIR = SCRIPT_DIR.parent / "catalogs"
TEMPLATES_DIR = SCRIPT_DIR.parent / "templates"

# Equipment type code -> default template ID mapping
EQUIPMENT_TEMPLATE_MAP = {
    "P": "PP-CEN", "PU": "PP-CEN",
    "B": "BL-PD", "BL": "BL-PD",
    "AG": "MX-TOPENTRY", "MX": "MX-TOPENTRY",
    "EHX": "HX-PF", "HX": "HX-PF", "HE": "HX-ST",
    "SC": "101-SCR", "SCR": "101-SCR",
    "G": "101-GR", "GR": "101-GR",
    "TK": "TK-SS", "CN": "101-CV", "CV": "101-CV",
    "FL": "FL-AUTO", "CT": "120-CT",
}


def _extract_type_code(tag: str) -> str:
    """Extract type code from tag, handling paired tags like 200-B-03/04."""
    # Strip /NN suffix for paired tags
    base_tag = re.sub(r'/\d+$', '', tag)
    m = re.match(r"[A-Z]?\d{3,4}-([A-Z]{1,5})-\d+", base_tag)
    return m.group(1) if m else ""


def resolve_template(tag: str, equipment: dict, templates_dir: Path) -> Optional[Path]:
    """Auto-resolve equipment tag to best matching template.

    Priority:
    1. Explicit template_id in equipment data
    2. Type code from tag mapped via EQUIPMENT_TEMPLATE_MAP
    """
    # 1. Explicit template_id in equipment data
    explicit = equipment.get("template_id", "")
    if explicit:
        path = templates_dir / f"{explicit}.md"
        if path.exists():
            return path
    # 2. Type code from tag
    type_code = _extract_type_code(tag)
    template_id = EQUIPMENT_TEMPLATE_MAP.get(type_code)
    if template_id:
        path = templates_dir / f"{template_id}.md"
        if path.exists():
            return path
    return None


# =============================================================================
# Data Loading
# =============================================================================

def load_field_mappings(catalog_path: Optional[Path] = None) -> dict:
    """Load field mapping catalog."""
    if catalog_path is None:
        catalog_path = CATALOG_DIR / "field_mappings.yaml"
    if not catalog_path.exists():
        print(f"Warning: Field mappings not found: {catalog_path}")
        return {}
    with open(catalog_path) as f:
        return yaml.safe_load(f) or {}


def load_equipment_data(path) -> tuple[dict, list[dict]]:
    """Load equipment list from QMD or YAML file."""
    path = Path(path)
    with open(path) as f:
        content = f.read()

    if path.suffix in [".qmd", ".md"]:
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm = yaml.safe_load(parts[1]) or {}
            return fm, fm.get("equipment", [])

    data = yaml.safe_load(content)
    if isinstance(data, list):
        return {}, data
    return data, data.get("equipment", data.get("loads", []))


def find_equipment(equipment_list: list[dict], tag: str) -> Optional[dict]:
    """Find equipment entry by tag."""
    for eq in equipment_list:
        if eq.get("tag", eq.get("equipment_tag", "")) == tag:
            return eq
    return None


# =============================================================================
# Capacity / Description Parsing
# =============================================================================

def parse_capacity_string(text: str) -> dict:
    """Parse capacity from free-text string or description.

    Patterns recognised:
      "500 m3/h @ 30m w.c."  → flow_m3h + head_m
      "50 m3/h @ 2.5 bar"    → flow_m3h + pressure_bar
      "2500 Nm3/h"           → flow_nm3h
      "1200 m3/day"          → flow_m3h (converted)
      "500 m3/h"             → flow_m3h
      "1500 m3"              → volume_m3
    """
    if not text:
        return {}
    text = str(text).strip()

    # flow @ head in m w.c.
    m = re.search(r"([\d.]+)\s*m3/hr?\s*@\s*([\d.]+)\s*m\s*w\.?c\.?", text, re.I)
    if m:
        return {"flow_m3h": float(m.group(1)), "head_m": float(m.group(2))}

    # flow @ head in m (plain)
    m = re.search(r"([\d.]+)\s*m3/hr?\s*@\s*([\d.]+)\s*m\b", text, re.I)
    if m:
        return {"flow_m3h": float(m.group(1)), "head_m": float(m.group(2))}

    # flow @ pressure in bar
    m = re.search(r"([\d.]+)\s*m3/hr?\s*@\s*([\d.]+)\s*bar\s*g?", text, re.I)
    if m:
        return {"flow_m3h": float(m.group(1)), "pressure_bar": float(m.group(2))}

    # Nm3/h
    m = re.search(r"([\d.]+)\s*[Nn]m3/hr?", text)
    if m:
        return {"flow_nm3h": float(m.group(1))}

    # m3/day
    m = re.search(r"([\d.]+)\s*m3/[Dd]ay?", text, re.I)
    if m:
        return {"flow_m3h": float(m.group(1)) / 24}

    # m3/h (plain)
    m = re.search(r"([\d.]+)\s*m3/hr?", text, re.I)
    if m:
        return {"flow_m3h": float(m.group(1))}

    # volume m3 (not followed by /)
    m = re.search(r"([\d.]+)\s*m3(?!\s*/)", text, re.I)
    if m:
        return {"volume_m3": float(m.group(1))}

    return {}


def parse_quantity_note(note: str) -> tuple[int, int]:
    """Parse 'NW + MS' into (working, standby)."""
    if not note:
        return 1, 0
    n = note.upper().replace(" ", "")
    m = re.match(r"(\d+)W(?:\+(\d+)S)?", n)
    if m:
        return int(m.group(1)), int(m.group(2) or 0)
    if n.isdigit():
        return int(n), 0
    return 1, 0


def build_capacity_data(equipment: dict) -> dict:
    """Build capacity data from all available sources.

    Priority order:
    1. Structured capacity_value + capacity_unit
    2. Free-text capacity field
    3. Description field parsing
    4. Direct head_m / pressure_bar_g fields
    """
    result = {}

    # 1. Structured fields
    cv = equipment.get("capacity_value")
    cu = equipment.get("capacity_unit", "")
    if cv is not None and cu:
        u = str(cu).lower()
        val = float(cv)
        if "m3/h" in u or "m\u00b3/h" in u:
            result["flow_m3h"] = val
        elif "nm3/h" in u or "nm\u00b3/h" in u:
            result["flow_nm3h"] = val
        elif "m3/d" in u or "m\u00b3/d" in u:
            result["flow_m3h"] = val / 24
        elif "m3" in u or "m\u00b3" in u:
            result["volume_m3"] = val
        elif "l/s" in u:
            result["flow_m3h"] = val * 3.6

    # 2. Free-text capacity
    if not result:
        cap = equipment.get("capacity", "")
        if cap:
            result = parse_capacity_string(str(cap))

    # 3. Description fallback
    if not result:
        desc = equipment.get("description", "")
        if desc:
            result = parse_capacity_string(str(desc))

    # 4. Direct fields (additive, don't overwrite)
    if equipment.get("head_m"):
        result.setdefault("head_m", float(equipment["head_m"]))
    if equipment.get("pressure_bar_g"):
        result.setdefault("pressure_bar", float(equipment["pressure_bar_g"]))

    return result


# =============================================================================
# Value Resolution
# =============================================================================

def resolve_value(
    mapping_key: str,
    equipment: dict,
    capacity_data: dict,
    metadata: dict,
    voltage: int = 415,
    frequency: int = 50,
) -> Any:
    """Resolve a mapping key to a concrete value.

    Supports direct attribute names (e.g. 'power_kw') and computed
    fields prefixed with '_' (e.g. '_capacity.flow_m3h').
    """
    if mapping_key.startswith("_"):
        # --- Capacity fields ---
        if mapping_key == "_capacity.flow_m3h":
            return capacity_data.get("flow_m3h")
        if mapping_key == "_capacity.flow_nm3h":
            return capacity_data.get("flow_nm3h")
        if mapping_key == "_capacity.volume_m3":
            return capacity_data.get("volume_m3")
        if mapping_key == "_capacity.head_m":
            return capacity_data.get("head_m")
        if mapping_key == "_capacity.pressure_bar":
            return capacity_data.get("pressure_bar")

        # --- Quantity fields ---
        if mapping_key == "_quantity.working":
            w, _ = parse_quantity_note(equipment.get("quantity_note", ""))
            return w
        if mapping_key == "_quantity.standby":
            _, s = parse_quantity_note(equipment.get("quantity_note", ""))
            return s

        # --- Feeder fields ---
        if mapping_key == "_feeder.vfd_flag":
            ft = (equipment.get("feeder_type") or "").upper()
            return "Yes" if "VFD" in ft else "No"
        if mapping_key == "_feeder.starting":
            ft = (equipment.get("feeder_type") or "").upper()
            if "VFD" in ft:
                return "VFD"
            if "SOFT" in ft:
                return "Soft Start"
            return "DOL"

        # --- Project / electrical fields ---
        if mapping_key == "_voltage_string":
            return f"{voltage}V / 3Ph / {frequency}Hz"
        if mapping_key == "_project_id":
            return metadata.get("project_id", "")

        return None

    # Direct attribute lookup
    return equipment.get(mapping_key)


# =============================================================================
# Template Population (operates on parsed template dict)
# =============================================================================

def populate_parsed_template(
    template: dict,
    equipment: dict,
    mappings: dict,
    metadata: dict = None,
    voltage: int = 415,
    frequency: int = 50,
) -> dict:
    """Populate a parsed template dict with equipment values.

    Modifies the template dict in-place and returns it.
    Works with the dict returned by md_to_excel.parse_template().

    Args:
        template: Parsed template with 'metadata' and 'sections' keys
        equipment: Equipment dict with tag, power_kw, capacity, etc.
        mappings: Field mappings catalog (from field_mappings.yaml)
        metadata: Project metadata (project_id, etc.)
        voltage: System voltage
        frequency: System frequency

    Returns:
        Modified template dict with Value fields populated
    """
    if metadata is None:
        metadata = {}

    template_id = template["metadata"].get("template_id", "")
    has_motor = template["metadata"].get("has_motor", False)

    # Build field mapping for this template
    field_map = {}
    if has_motor:
        field_map.update(mappings.get("_common_motor", {}))
    field_map.update(mappings.get(template_id, {}))

    if not field_map:
        return template  # No mappings for this template

    # Pre-compute capacity data once
    capacity_data = build_capacity_data(equipment)

    tag = equipment.get("tag", equipment.get("equipment_tag", ""))
    project_id = metadata.get("project_id", "")

    for section_name, rows in template["sections"].items():
        if section_name == "Document Control":
            for row in rows:
                field = row.get("Field", "")
                if "Tag" in field and tag:
                    row["Value"] = tag
                elif field == "Project" and project_id:
                    row["Value"] = project_id

        elif section_name == "Service Information":
            for row in rows:
                field = row.get("Field", "")
                if field == "Service":
                    desc = equipment.get("description", "")
                    if desc:
                        row["Value"] = desc

        else:
            # Data tables with field_id column
            for row in rows:
                field_id = row.get("field_id", "")
                if field_id and field_id in field_map:
                    mapping_key = field_map[field_id]
                    value = resolve_value(
                        mapping_key, equipment, capacity_data,
                        metadata, voltage, frequency
                    )
                    if value is not None:
                        row["Value"] = str(value)

    return template


# =============================================================================
# Standalone CLI
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Populate datasheet template with equipment data"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--template", "-t",
                       help="Template .md file path")
    group.add_argument("--auto", action="store_true",
                       help="Auto-resolve templates from equipment type codes")
    parser.add_argument("--equipment-data", "-e", required=True,
                        help="Equipment list (QMD or YAML)")
    parser.add_argument("--tag",
                        help="Equipment tag to populate (required with --template)")
    parser.add_argument("--output", "-o",
                        help="Output populated .md file (default: stdout)")
    parser.add_argument("--output-dir",
                        help="Output directory for --auto mode")
    parser.add_argument("--project-id",
                        help="Project identifier")
    parser.add_argument("--voltage", type=int, default=415)
    parser.add_argument("--frequency", type=int, default=50)
    parser.add_argument("--mappings",
                        help="Path to field_mappings.yaml (default: catalogs/)")
    parser.add_argument("--templates-dir",
                        help="Path to templates directory (default: templates/)")

    args = parser.parse_args()

    equipment_path = Path(args.equipment_data)
    if not equipment_path.exists():
        print(f"Error: Equipment data not found: {equipment_path}")
        sys.exit(1)

    # Load data
    mappings_path = Path(args.mappings) if args.mappings else None
    mappings = load_field_mappings(mappings_path)
    metadata_dict, equip_list = load_equipment_data(equipment_path)
    meta = {"project_id": args.project_id or metadata_dict.get("project_id", "")}
    templates_dir = Path(args.templates_dir) if args.templates_dir else TEMPLATES_DIR

    if args.auto:
        # Auto mode: iterate all equipment and resolve templates
        output_dir = Path(args.output_dir) if args.output_dir else Path(".")
        output_dir.mkdir(parents=True, exist_ok=True)
        processed = 0
        skipped = 0
        for eq in equip_list:
            tag = eq.get("tag", eq.get("equipment_tag", ""))
            if not tag:
                continue
            template_path = resolve_template(tag, eq, templates_dir)
            if template_path is None:
                type_code = _extract_type_code(tag)
                print(f"Skip: {tag} (type '{type_code}' — no template match)")
                skipped += 1
                continue
            populated = _populate_single(
                template_path, eq, mappings, meta,
                args.voltage, args.frequency,
            )
            out_file = output_dir / f"{template_path.stem}-{tag}.md"
            out_file.write_text(populated, encoding="utf-8")
            print(f"Populated: {out_file}")
            processed += 1
        print(f"\nDone: {processed} populated, {skipped} skipped")
    else:
        # Single template mode
        if not args.tag:
            print("Error: --tag is required when using --template")
            sys.exit(1)
        template_path = Path(args.template)
        if not template_path.exists():
            print(f"Error: Template not found: {template_path}")
            sys.exit(1)
        equipment = find_equipment(equip_list, args.tag)
        if equipment is None:
            print(f"Error: Tag '{args.tag}' not found in equipment list")
            sys.exit(1)
        populated = _populate_single(
            template_path, equipment, mappings, meta,
            args.voltage, args.frequency,
        )
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(populated, encoding="utf-8")
            print(f"Populated: {output_path}")
        else:
            print(populated)


def _populate_single(
    template_path: Path,
    equipment: dict,
    mappings: dict,
    metadata: dict,
    voltage: int,
    frequency: int,
) -> str:
    """Populate a single template for one equipment item."""
    try:
        from md_to_excel import parse_template
        template = parse_template(template_path)
        populate_parsed_template(
            template, equipment, mappings, metadata,
            voltage, frequency
        )
        return _serialize_template(template_path, template)
    except ImportError:
        return _populate_markdown_raw(
            template_path, equipment, mappings, metadata,
            voltage, frequency
        )


def _serialize_template(template_path: Path, template: dict) -> str:
    """Re-serialize a parsed+populated template back to markdown.

    Reads the original file and replaces Value cells with populated values.
    """
    content = template_path.read_text(encoding="utf-8")
    lines = content.split("\n")
    result = []
    current_section = ""
    header_cols = []

    # Build lookup: section_name → {field_id → value, ...}
    section_values = {}
    for sec_name, rows in template["sections"].items():
        vals = {}
        for row in rows:
            fid = row.get("field_id", "")
            val = row.get("Value", "")
            field = row.get("Field", "")
            if fid:
                vals[fid] = val
            elif field:
                vals[field] = val
        section_values[sec_name] = vals

    for line in lines:
        sec_match = re.match(r"^##\s+(.+)", line)
        if sec_match:
            current_section = sec_match.group(1).strip()
            header_cols = []
            result.append(line)
            continue

        if line.strip().startswith("|"):
            raw = line.split("|")
            if raw and raw[0].strip() == "":
                raw = raw[1:]
            if raw and raw[-1].strip() == "":
                raw = raw[:-1]
            cells = [c.strip() for c in raw]

            # Skip separators
            if all(c.replace("-", "").replace(":", "").strip() == "" for c in cells):
                result.append(line)
                continue

            # Detect header
            if "field_id" in cells:
                header_cols = cells
                result.append(line)
                continue
            if not header_cols and len(cells) >= 2 and cells[0] == "Field":
                header_cols = ["Field", "Value"]
                result.append(line)
                continue

            sec_vals = section_values.get(current_section, {})
            modified = False

            if header_cols and "field_id" in header_cols:
                try:
                    fid_idx = header_cols.index("field_id")
                    val_idx = header_cols.index("Value")
                except ValueError:
                    result.append(line)
                    continue
                if fid_idx < len(cells):
                    fid = cells[fid_idx]
                    new_val = sec_vals.get(fid)
                    if new_val and val_idx < len(cells):
                        cells[val_idx] = new_val
                        modified = True
            elif header_cols == ["Field", "Value"] and len(cells) >= 2:
                field_name = cells[0]
                new_val = sec_vals.get(field_name)
                if new_val:
                    cells[1] = new_val
                    modified = True

            if modified:
                line = "| " + " | ".join(cells) + " |"

        result.append(line)

    return "\n".join(result)


def _populate_markdown_raw(
    template_path: Path,
    equipment: dict,
    mappings: dict,
    metadata: dict,
    voltage: int,
    frequency: int,
) -> str:
    """Fallback: populate raw markdown without md_to_excel parser."""
    content = template_path.read_text(encoding="utf-8")

    # Parse frontmatter for template_id
    fm = {}
    if content.startswith("---"):
        end = content.find("\n---\n", 3)
        if end > 0:
            try:
                fm = yaml.safe_load(content[3:end]) or {}
            except yaml.YAMLError:
                pass

    template_id = fm.get("template_id", "")
    has_motor = fm.get("has_motor", False)

    field_map = {}
    if has_motor:
        field_map.update(mappings.get("_common_motor", {}))
    field_map.update(mappings.get(template_id, {}))

    if not field_map:
        return content

    capacity_data = build_capacity_data(equipment)
    tag = equipment.get("tag", equipment.get("equipment_tag", ""))
    project_id = metadata.get("project_id", "")

    doc_map = {}
    if tag:
        doc_map["Equipment Tag"] = tag
    if project_id:
        doc_map["Project"] = project_id

    service_map = {}
    desc = equipment.get("description", "")
    if desc:
        service_map["Service"] = desc

    lines = content.split("\n")
    result = []
    current_section = ""
    header_cols = []

    for line in lines:
        sec_match = re.match(r"^##\s+(.+)", line)
        if sec_match:
            current_section = sec_match.group(1).strip()
            header_cols = []
            result.append(line)
            continue

        if line.strip().startswith("|"):
            raw = line.split("|")
            if raw and raw[0].strip() == "":
                raw = raw[1:]
            if raw and raw[-1].strip() == "":
                raw = raw[:-1]
            cells = [c.strip() for c in raw]

            if all(c.replace("-", "").replace(":", "").strip() == "" for c in cells):
                result.append(line)
                continue

            if "field_id" in cells:
                header_cols = cells
                result.append(line)
                continue
            if not header_cols and len(cells) >= 2 and cells[0] == "Field":
                header_cols = ["Field", "Value"]
                result.append(line)
                continue

            modified = False

            if current_section == "Document Control" and len(cells) >= 2:
                if cells[0] in doc_map:
                    cells[1] = doc_map[cells[0]]
                    modified = True

            elif current_section == "Service Information" and len(cells) >= 2:
                if cells[0] in service_map:
                    cells[1] = service_map[cells[0]]
                    modified = True

            elif header_cols and "field_id" in header_cols:
                try:
                    fid_idx = header_cols.index("field_id")
                    val_idx = header_cols.index("Value")
                except ValueError:
                    result.append(line)
                    continue
                if fid_idx < len(cells):
                    fid = cells[fid_idx]
                    if fid in field_map:
                        value = resolve_value(
                            field_map[fid], equipment, capacity_data,
                            metadata, voltage, frequency
                        )
                        if value is not None and val_idx < len(cells):
                            cells[val_idx] = str(value)
                            modified = True

            if modified:
                line = "| " + " | ".join(cells) + " |"

        result.append(line)

    return "\n".join(result)


if __name__ == "__main__":
    main()
