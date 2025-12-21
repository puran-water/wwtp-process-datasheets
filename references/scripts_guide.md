# Scripts Guide

Detailed usage for automation scripts.

## Table of Contents

- [md_to_excel.py](#md_to_excelpy)
- [validate_template.py](#validate_templatepy)
- [validate_datasheet.py](#validate_datasheetpy)
- [generate_bom.py](#generate_bompy)
- [Git Workflow](#git-workflow)

---

## md_to_excel.py

Convert markdown templates to professionally-styled Excel datasheets.

### Usage

```bash
# Convert single template
python scripts/md_to_excel.py templates/101-GR.md

# Convert all templates
python scripts/md_to_excel.py --all

# Specify output directory
python scripts/md_to_excel.py --all --output-dir assets/

# Dry run (show what would be generated)
python scripts/md_to_excel.py --all --dry-run
```

### Options

| Flag | Description |
|------|-------------|
| `--all` | Process all templates in `templates/` |
| `--output-dir DIR` | Output directory (default: `assets/`) |
| `--dry-run` | Show what would be generated without writing |

### Output

Creates Excel files with naming convention: `{template_id}-01 {TITLE}.xlsx`

Example: `templates/101-GR.md` → `assets/101-GR-01 GRIT REMOVAL PACKAGE.xlsx`

---

## validate_template.py

Validate markdown template syntax, structure, and BOM references.

### Usage

```bash
# Validate single template
python scripts/validate_template.py templates/101-GR.md

# Validate all templates
python scripts/validate_template.py --all

# Verbose output
python scripts/validate_template.py templates/101-GR.md --verbose
```

### Validation Checks

| Check | Description |
|-------|-------------|
| YAML frontmatter | Valid YAML, required fields present |
| Required sections | Document Control, Service Info, Operating Data, Materials, Remarks, Revision History |
| Table structure | Correct column count for each table type |
| Field types | Valid type values (number, text, dropdown, date, readonly) |
| Dropdown options | Valid JSON array in Options column |
| field_id uniqueness | No duplicate field_ids within template |
| BOM references | Referenced component templates exist |

### Example Output

```
Validating 10 template(s)...
============================================================

File: 101-GR.md
  STATUS: VALID

File: 101-SC.md
  STATUS: VALID
  [2 fields need attention]
    - Row 5: Consider adding units for 'screen_spacing'
    - Row 12: Dropdown has only 1 option

File: 130-CL.md
  STATUS: INVALID
  [1 error]
    - Missing required section: Materials

============================================================
Results: 9 passed, 1 failed
```

---

## validate_datasheet.py

Check Excel datasheet completeness before RFQ issuance.

### Usage

```bash
# Validate single datasheet
python scripts/validate_datasheet.py "assets/101-GR-01 GRIT REMOVAL PACKAGE.xlsx"

# Validate all datasheets
python scripts/validate_datasheet.py --all

# Output as JSON
python scripts/validate_datasheet.py --all --format json

# Quiet mode (exit code only)
python scripts/validate_datasheet.py --all --quiet
```

### Options

| Flag | Description |
|------|-------------|
| `--all` | Validate all Excel files in `assets/` |
| `--format json` | Output results as JSON |
| `--quiet` | Suppress output, use exit code only |

### Exit Codes

| Code | Meaning |
|------|---------|
| `0` | Ready — all required fields populated |
| `1` | Not ready — missing required fields |
| `2` | Error — file not found or parse error |

### Validation Checks

| Check | Description |
|-------|-------------|
| Required fields | Fields marked REQ in config must have values |
| Dropdown validity | Selected value must be in dropdown list |
| Unit consistency | Values should have corresponding units |
| Completeness % | Percentage of all fields populated |

### Example Output

```
Validating: 101-GR-01 GRIT REMOVAL PACKAGE.xlsx
============================================================
Status: NOT READY
Completeness: 72%

Missing required fields:
  - qpeak (Design Peak Flow)
  - grit_concentration (Grit Concentration)
  - material_wetted (Wetted Parts Material)

Warnings:
  - Row 8: Value without units
============================================================
```

### JSON Output

```json
{
  "file": "101-GR-01 GRIT REMOVAL PACKAGE.xlsx",
  "status": "NOT_READY",
  "completeness_pct": 72,
  "missing_required": ["qpeak", "grit_concentration", "material_wetted"],
  "warnings": ["Row 8: Value without units"]
}
```

---

## generate_bom.py

Generate Bill of Materials from package templates.

### Usage

```bash
# Generate BOM (console output)
python scripts/generate_bom.py templates/101-SC.md

# Output to CSV file
python scripts/generate_bom.py templates/101-SC.md --output bom_101-SC.csv

# Verbose (show qty_rule evaluation)
python scripts/generate_bom.py templates/101-SC.md --verbose
```

### Options

| Flag | Description |
|------|-------------|
| `--output FILE` | Write BOM to CSV file |
| `--verbose` | Show qty_rule evaluation details |

### Example Output

```
================================================================================
BILL OF MATERIALS
================================================================================
Package: 101-SC (Screening Package)
Source:  templates/101-SC.md
================================================================================

Template        Component                  Qty Service
--------------------------------------------------------------------------------
101-SCR         Screen                       2 PRELIMINARY SCREENING
101-WC          Washer-Compactor             1 SCREENINGS PROCESSING
101-CV          Screw Conveyor               1 SCREENINGS TRANSPORT

================================================================================
Total component datasheets required: 3
================================================================================
```

### CSV Output

```csv
template_id,component,qty,service
101-SCR,Screen,2,PRELIMINARY SCREENING
101-WC,Washer-Compactor,1,SCREENINGS PROCESSING
101-CV,Screw Conveyor,1,SCREENINGS TRANSPORT
```

---

## Git Workflow

Recommended workflow for tracking template changes:

### Basic Edit Cycle

```bash
# 1. Edit markdown source
vim templates/101-GR.md

# 2. See what changed
git diff templates/101-GR.md

# 3. Validate syntax
python scripts/validate_template.py templates/101-GR.md

# 4. Regenerate Excel
python scripts/md_to_excel.py templates/101-GR.md

# 5. Validate completeness
python scripts/validate_datasheet.py "assets/101-GR-01 GRIT REMOVAL PACKAGE.xlsx"

# 6. Commit both source and artifact
git add templates/101-GR.md "assets/101-GR-01 GRIT REMOVAL PACKAGE.xlsx"
git commit -m "Update grit removal flow requirements"
```

### Batch Operations

```bash
# Regenerate all Excel files
python scripts/md_to_excel.py --all

# Validate all templates
python scripts/validate_template.py --all

# Check all datasheets ready for RFQ
python scripts/validate_datasheet.py --all

# Commit all changes
git add templates/ assets/
git commit -m "Regenerate all datasheets"
```

### Pre-RFQ Checklist

```bash
# 1. Validate all templates
python scripts/validate_template.py --all
# Should show: Results: N passed, 0 failed

# 2. Regenerate all Excel
python scripts/md_to_excel.py --all

# 3. Check completeness
python scripts/validate_datasheet.py --all
# Should show: Status: READY for all files

# 4. Generate BOMs for packages
python scripts/generate_bom.py templates/101-SC.md
python scripts/generate_bom.py templates/230-AT.md
# etc.
```
