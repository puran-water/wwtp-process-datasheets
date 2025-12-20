#!/usr/bin/env python3
"""
Markdown to Excel Datasheet Converter

Converts markdown template files to professional Excel datasheets.

Usage:
    python scripts/md_to_excel.py templates/101-GR.md
    python scripts/md_to_excel.py --all
    python scripts/md_to_excel.py --all --output-dir assets/
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml

try:
    from openpyxl import Workbook
    from openpyxl.worksheet.datavalidation import DataValidation
except ImportError:
    print("Error: openpyxl is required. Install with: pip install openpyxl")
    sys.exit(1)

# Import centralized styles
from excel_styles import (
    FONT_TITLE, FONT_SECTION, FONT_LABEL, FONT_VALUE, FONT_SMALL,
    BORDER_ALL, NO_FILL, ALIGN_LEFT, ALIGN_CENTER, ALIGN_RIGHT,
    COLUMN_WIDTHS, ROW_HEIGHT,
    apply_print_layout, apply_column_widths, apply_row_heights,
    style_cell, apply_borders_to_range
)


# =============================================================================
# MARKDOWN PARSING
# =============================================================================

def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and remaining content."""
    if not content.startswith('---'):
        return {}, content

    # Find the closing ---
    end_match = re.search(r'\n---\s*\n', content[3:])
    if not end_match:
        return {}, content

    yaml_content = content[3:3 + end_match.start()]
    remaining = content[3 + end_match.end():]

    try:
        frontmatter = yaml.safe_load(yaml_content)
        return frontmatter or {}, remaining
    except yaml.YAMLError as e:
        print(f"Warning: Failed to parse YAML frontmatter: {e}")
        return {}, content


def parse_markdown_table(table_text: str) -> list[dict]:
    """Parse a markdown table into a list of row dictionaries."""
    lines = [line.strip() for line in table_text.strip().split('\n') if line.strip()]

    if len(lines) < 2:
        return []

    # Parse header row
    header_line = lines[0]
    headers = [h.strip() for h in header_line.split('|') if h.strip()]

    # Skip separator line (contains ---)
    rows = []
    for line in lines[2:]:
        if '---' in line:
            continue
        cells = [c.strip() for c in line.split('|') if c.strip() or line.count('|') > len(headers)]

        # Handle empty cells from split
        raw_cells = line.split('|')[1:-1] if line.startswith('|') else line.split('|')
        cells = [c.strip() for c in raw_cells]

        if len(cells) >= len(headers):
            row = {headers[i]: cells[i] if i < len(cells) else '' for i in range(len(headers))}
            rows.append(row)

    return rows


def extract_sections(content: str) -> dict[str, Any]:
    """Extract sections from markdown content."""
    sections = {}

    # Split by ## headers
    section_pattern = r'^##\s+(.+?)\s*$'
    parts = re.split(section_pattern, content, flags=re.MULTILINE)

    # parts[0] is content before first ##
    # parts[1], parts[3], parts[5]... are section names
    # parts[2], parts[4], parts[6]... are section contents

    for i in range(1, len(parts), 2):
        section_name = parts[i].strip()
        section_content = parts[i + 1] if i + 1 < len(parts) else ''
        sections[section_name] = section_content.strip()

    return sections


def parse_template(filepath: Path) -> dict:
    """Parse a markdown template file into structured data."""
    content = filepath.read_text(encoding='utf-8')

    frontmatter, body = parse_frontmatter(content)
    sections = extract_sections(body)

    template = {
        'metadata': frontmatter,
        'sections': {}
    }

    # Parse each section's table
    for section_name, section_content in sections.items():
        # Find table in section content
        table_match = re.search(r'(\|.+\|[\s\S]*?)(?=\n\n|\n##|\Z)', section_content)
        if table_match:
            table_text = table_match.group(1)
            template['sections'][section_name] = parse_markdown_table(table_text)
        else:
            template['sections'][section_name] = []

    return template


# =============================================================================
# EXCEL GENERATION
# =============================================================================

def parse_options(options_str: str) -> list[str]:
    """Parse dropdown options from JSON array or comma-separated string."""
    if not options_str:
        return []

    options_str = options_str.strip()

    # Try JSON array first
    if options_str.startswith('['):
        try:
            return json.loads(options_str)
        except json.JSONDecodeError:
            pass

    # Fall back to comma-separated
    return [opt.strip() for opt in options_str.split(',') if opt.strip()]


def build_workbook(template: dict) -> Workbook:
    """Build an Excel workbook from parsed template data."""
    wb = Workbook()
    ws = wb.active

    metadata = template['metadata']
    sections = template['sections']

    # Set sheet name
    title = metadata.get('title', 'DATASHEET')
    ws.title = title[:31]  # Excel sheet name limit

    # Apply layout
    apply_column_widths(ws)
    apply_row_heights(ws, 1, 65)

    # Track current row
    row = 1

    # Track data validations to add at end
    validations = []

    # === TITLE BLOCK (Rows 1-2) ===
    ws.merge_cells(start_row=1, start_column=1, end_row=2, end_column=10)
    title_cell = ws.cell(row=1, column=1, value=f"{title} DATASHEET")
    style_cell(title_cell, 'title')
    apply_borders_to_range(ws, 1, 2, 1, 10)
    row = 3

    # === SERVICE INFO + DOCUMENT CONTROL (Rows 3-8) ===
    service_info = sections.get('Service Information', [])
    doc_control = sections.get('Document Control', [])

    service_labels = ['Service:', 'Location:', 'Manufacturer:', 'Model:', 'P&ID No:', '']
    service_values = ['', '', '', '', '', '']

    # Extract service info values
    for item in service_info:
        field = item.get('Field', '')
        value = item.get('Value', '')
        if 'Service' in field:
            service_values[0] = value
        elif 'Location' in field:
            service_values[1] = value
        elif 'Manufacturer' in field:
            service_values[2] = value
        elif 'Model' in field:
            service_values[3] = value
        elif 'P&ID' in field:
            service_values[4] = value

    # Use service from metadata as fallback
    if not service_values[0]:
        service_values[0] = metadata.get('service', '')

    doc_labels = ['Project:', 'Client:', 'Equipment Tag:', 'Document No:', 'Revision:', 'Date:']
    doc_values = ['', '', '', '', '', '']

    # Extract document control values
    for item in doc_control:
        field = item.get('Field', '')
        value = item.get('Value', '')
        if 'Project' in field:
            doc_values[0] = value
        elif 'Client' in field:
            doc_values[1] = value
        elif 'Tag' in field:
            doc_values[2] = value
        elif 'Document' in field or 'Doc' in field:
            doc_values[3] = value
        elif 'Revision' in field or 'Rev' in field:
            doc_values[4] = value
        elif 'Date' in field:
            doc_values[5] = value

    for i in range(6):
        r = row + i

        # Left side: Service info (columns A-F)
        ws.cell(row=r, column=1).font = FONT_SMALL
        ws.cell(row=r, column=1).border = BORDER_ALL

        ws.cell(row=r, column=2, value=service_labels[i]).font = FONT_LABEL
        ws.cell(row=r, column=2).border = BORDER_ALL

        ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=6)
        ws.cell(row=r, column=3, value=service_values[i]).font = FONT_VALUE
        for col in range(3, 7):
            ws.cell(row=r, column=col).border = BORDER_ALL

        # Right side: Document control (columns G-J)
        ws.cell(row=r, column=7, value=doc_labels[i]).font = FONT_SMALL
        ws.cell(row=r, column=7).alignment = ALIGN_RIGHT
        ws.cell(row=r, column=7).border = BORDER_ALL

        ws.merge_cells(start_row=r, start_column=8, end_row=r, end_column=10)
        ws.cell(row=r, column=8, value=doc_values[i]).font = FONT_VALUE
        for col in range(8, 11):
            ws.cell(row=r, column=col).border = BORDER_ALL

    row += 6

    # === OPERATING / DESIGN DATA ===
    operating_data = sections.get('Operating / Design Data', [])
    if operating_data:
        row = write_data_section(ws, row, 'OPERATING / DESIGN DATA', operating_data, validations)

    # === MATERIALS ===
    materials = sections.get('Materials', [])
    if materials:
        row = write_materials_section(ws, row, materials)

    # === DRIVER / MOTOR DATA ===
    has_motor = metadata.get('has_motor', False)
    motor_data = sections.get('Driver / Motor Data', [])
    if has_motor and motor_data:
        row = write_data_section(ws, row, 'DRIVER / MOTOR DATA', motor_data, validations)

    # === REMARKS ===
    remarks = sections.get('Remarks', [])
    row = write_remarks_section(ws, row, remarks)

    # === REVISION HISTORY ===
    rev_history = sections.get('Revision History', [])
    row = write_revision_section(ws, row, rev_history)

    # Add data validations
    for validation in validations:
        ws.add_data_validation(validation)

    # Apply print layout
    apply_print_layout(ws)

    return wb


def write_data_section(ws, start_row: int, section_title: str, data: list[dict],
                       validations: list) -> int:
    """Write a data section (Operating Data or Motor Data)."""
    row = start_row

    # Section header
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=10)
    ws.cell(row=row, column=1, value=section_title).font = FONT_SECTION
    ws.cell(row=row, column=1).alignment = ALIGN_LEFT
    apply_borders_to_range(ws, row, row, 1, 10)
    row += 1

    # Data rows
    for item in data:
        row_num = item.get('#', '')
        field_label = item.get('Field', '')
        value = item.get('Value', '')
        units = item.get('Units', '')
        field_type = item.get('Type', 'text')
        options = item.get('Options', '')

        # Skip header-like rows
        if row_num == '#' or field_label == 'Field':
            continue

        # Row number (column A)
        ws.cell(row=row, column=1, value=row_num).font = FONT_SMALL
        ws.cell(row=row, column=1).alignment = ALIGN_CENTER
        ws.cell(row=row, column=1).border = BORDER_ALL

        # Label (columns B-D)
        ws.merge_cells(start_row=row, start_column=2, end_row=row, end_column=4)
        ws.cell(row=row, column=2, value=field_label).font = FONT_LABEL
        ws.cell(row=row, column=2).alignment = ALIGN_LEFT
        for col in range(2, 5):
            ws.cell(row=row, column=col).border = BORDER_ALL

        # Value (columns E-H)
        ws.merge_cells(start_row=row, start_column=5, end_row=row, end_column=8)
        ws.cell(row=row, column=5, value=value).font = FONT_VALUE
        ws.cell(row=row, column=5).alignment = ALIGN_LEFT
        for col in range(5, 9):
            ws.cell(row=row, column=col).border = BORDER_ALL

        # Add dropdown validation if needed
        if field_type == 'dropdown' and options:
            option_list = parse_options(options)
            if option_list:
                # Create validation formula
                formula = f'"{",".join(option_list)}"'
                if len(formula) <= 255:
                    dv = DataValidation(type='list', formula1=formula, allow_blank=True)
                    dv.add(ws.cell(row=row, column=5))
                    validations.append(dv)

        # Units (column I)
        ws.cell(row=row, column=9, value=units).font = FONT_SMALL
        ws.cell(row=row, column=9).alignment = ALIGN_LEFT
        ws.cell(row=row, column=9).border = BORDER_ALL

        # Notes (column J)
        ws.cell(row=row, column=10).font = FONT_SMALL
        ws.cell(row=row, column=10).border = BORDER_ALL

        row += 1

    return row


def write_materials_section(ws, start_row: int, materials: list[dict]) -> int:
    """Write the materials section."""
    row = start_row

    # Section header
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=10)
    ws.cell(row=row, column=1, value='MATERIALS').font = FONT_SECTION
    ws.cell(row=row, column=1).alignment = ALIGN_LEFT
    apply_borders_to_range(ws, row, row, 1, 10)
    row += 1

    # Column headers
    ws.cell(row=row, column=1).font = FONT_SMALL
    ws.cell(row=row, column=1).border = BORDER_ALL

    ws.merge_cells(start_row=row, start_column=2, end_row=row, end_column=5)
    ws.cell(row=row, column=2, value='Component').font = FONT_LABEL
    for col in range(2, 6):
        ws.cell(row=row, column=col).border = BORDER_ALL

    ws.merge_cells(start_row=row, start_column=6, end_row=row, end_column=10)
    ws.cell(row=row, column=6, value='Material').font = FONT_LABEL
    for col in range(6, 11):
        ws.cell(row=row, column=col).border = BORDER_ALL
    row += 1

    # Material rows
    for item in materials:
        row_num = item.get('#', '')
        component = item.get('Component', '')
        material = item.get('Material', '')

        # Skip header-like rows
        if row_num == '#' or component == 'Component':
            continue

        # Row number
        ws.cell(row=row, column=1, value=row_num).font = FONT_SMALL
        ws.cell(row=row, column=1).alignment = ALIGN_CENTER
        ws.cell(row=row, column=1).border = BORDER_ALL

        # Component (columns B-E)
        ws.merge_cells(start_row=row, start_column=2, end_row=row, end_column=5)
        ws.cell(row=row, column=2, value=component).font = FONT_LABEL
        for col in range(2, 6):
            ws.cell(row=row, column=col).border = BORDER_ALL

        # Material (columns F-J)
        ws.merge_cells(start_row=row, start_column=6, end_row=row, end_column=10)
        ws.cell(row=row, column=6, value=material).font = FONT_VALUE
        for col in range(6, 11):
            ws.cell(row=row, column=col).border = BORDER_ALL

        row += 1

    return row


def write_remarks_section(ws, start_row: int, remarks: list[dict]) -> int:
    """Write the remarks section."""
    row = start_row

    # Section header
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=10)
    ws.cell(row=row, column=1, value='REMARKS').font = FONT_SECTION
    ws.cell(row=row, column=1).alignment = ALIGN_LEFT
    apply_borders_to_range(ws, row, row, 1, 10)
    row += 1

    # Remarks rows (at least 3)
    num_remarks = max(len(remarks), 3)
    for i in range(num_remarks):
        remark_text = ''
        if i < len(remarks):
            item = remarks[i]
            remark_text = item.get('Remark', '')

        ws.cell(row=row, column=1, value=i + 1).font = FONT_SMALL
        ws.cell(row=row, column=1).alignment = ALIGN_CENTER
        ws.cell(row=row, column=1).border = BORDER_ALL

        ws.merge_cells(start_row=row, start_column=2, end_row=row, end_column=10)
        ws.cell(row=row, column=2, value=remark_text).font = FONT_VALUE
        for col in range(2, 11):
            ws.cell(row=row, column=col).border = BORDER_ALL

        row += 1

    return row


def write_revision_section(ws, start_row: int, revisions: list[dict]) -> int:
    """Write the revision history section."""
    row = start_row

    # Section header
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=10)
    ws.cell(row=row, column=1, value='REVISION HISTORY').font = FONT_SECTION
    ws.cell(row=row, column=1).alignment = ALIGN_LEFT
    apply_borders_to_range(ws, row, row, 1, 10)
    row += 1

    # Column headers
    ws.cell(row=row, column=1, value='Rev').font = FONT_SMALL
    ws.cell(row=row, column=1).alignment = ALIGN_CENTER
    ws.cell(row=row, column=1).border = BORDER_ALL

    ws.merge_cells(start_row=row, start_column=2, end_row=row, end_column=3)
    ws.cell(row=row, column=2, value='Date').font = FONT_SMALL
    for col in range(2, 4):
        ws.cell(row=row, column=col).border = BORDER_ALL

    ws.merge_cells(start_row=row, start_column=4, end_row=row, end_column=8)
    ws.cell(row=row, column=4, value='Description').font = FONT_SMALL
    for col in range(4, 9):
        ws.cell(row=row, column=col).border = BORDER_ALL

    ws.merge_cells(start_row=row, start_column=9, end_row=row, end_column=10)
    ws.cell(row=row, column=9, value='By').font = FONT_SMALL
    for col in range(9, 11):
        ws.cell(row=row, column=col).border = BORDER_ALL
    row += 1

    # Revision rows (at least 3)
    num_revisions = max(len(revisions), 3)
    for i in range(num_revisions):
        rev = ''
        date = ''
        description = ''
        by = ''

        if i < len(revisions):
            item = revisions[i]
            rev = item.get('Rev', '')
            date = item.get('Date', '')
            description = item.get('Description', '')
            by = item.get('By', '')

        ws.cell(row=row, column=1, value=rev).font = FONT_SMALL
        ws.cell(row=row, column=1).alignment = ALIGN_CENTER
        ws.cell(row=row, column=1).border = BORDER_ALL

        ws.merge_cells(start_row=row, start_column=2, end_row=row, end_column=3)
        ws.cell(row=row, column=2, value=date).font = FONT_SMALL
        for col in range(2, 4):
            ws.cell(row=row, column=col).border = BORDER_ALL

        ws.merge_cells(start_row=row, start_column=4, end_row=row, end_column=8)
        ws.cell(row=row, column=4, value=description).font = FONT_VALUE
        for col in range(4, 9):
            ws.cell(row=row, column=col).border = BORDER_ALL

        ws.merge_cells(start_row=row, start_column=9, end_row=row, end_column=10)
        ws.cell(row=row, column=9, value=by).font = FONT_SMALL
        for col in range(9, 11):
            ws.cell(row=row, column=col).border = BORDER_ALL

        row += 1

    return row


# =============================================================================
# OUTPUT FILENAME GENERATION
# =============================================================================

def generate_output_filename(template: dict) -> str:
    """Generate the output Excel filename based on template metadata."""
    metadata = template['metadata']
    template_id = metadata.get('template_id', 'UNKNOWN')
    title = metadata.get('title', 'DATASHEET')

    # Format: 101-GR-01 GRIT REMOVAL PACKAGE.xlsx
    return f"{template_id}-01 {title}.xlsx"


# =============================================================================
# MAIN
# =============================================================================

def convert_template(input_path: Path, output_dir: Path) -> bool:
    """Convert a single markdown template to Excel."""
    print(f"Converting: {input_path.name}")

    try:
        template = parse_template(input_path)
        workbook = build_workbook(template)

        output_filename = generate_output_filename(template)
        output_path = output_dir / output_filename

        workbook.save(output_path)
        print(f"  -> {output_path.name}")
        return True

    except Exception as e:
        print(f"  ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Convert markdown templates to Excel datasheets'
    )
    parser.add_argument('files', nargs='*', help='Markdown files to convert')
    parser.add_argument('--all', action='store_true',
                        help='Convert all templates in templates/ directory')
    parser.add_argument('--output-dir', '-o', default='assets',
                        help='Output directory for Excel files (default: assets)')

    args = parser.parse_args()

    # Determine script location for relative paths
    script_dir = Path(__file__).parent
    project_dir = script_dir.parent

    output_dir = Path(args.output_dir)
    if not output_dir.is_absolute():
        output_dir = project_dir / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    # Collect files to convert
    if args.all:
        templates_dir = project_dir / 'templates'
        files = list(templates_dir.glob('*.md'))
    elif args.files:
        files = [Path(f) for f in args.files]
    else:
        print("Usage: md_to_excel.py <files...> or --all")
        sys.exit(1)

    if not files:
        print("No template files found")
        sys.exit(1)

    print(f"Converting {len(files)} template(s)...\n")

    success_count = 0
    for filepath in sorted(files):
        if not filepath.exists():
            print(f"Warning: File not found: {filepath}")
            continue

        if convert_template(filepath, output_dir):
            success_count += 1

    print(f"\nCompleted: {success_count}/{len(files)} templates converted successfully")

    if success_count < len(files):
        sys.exit(1)


if __name__ == '__main__':
    main()
