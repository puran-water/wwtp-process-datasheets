# WWTP Process Datasheets

Markdown-native datasheet templates with automated Excel generation for wastewater treatment equipment procurement (RFQ).

## Overview

This skill provides **vendor-ready process datasheets** for common wastewater treatment package equipment. Templates are maintained in markdown for easy editing and version control, with automated conversion to professionally-styled Excel files.

## Equipment Types Covered

| Area | Equipment |
|------|-----------|
| **Headworks (101)** | Screening packages, Grit removal |
| **Primary (130)** | Primary clarifiers, Lamella clarifiers |
| **Secondary (230/240)** | Aeration tanks, Secondary clarifiers |
| **Tertiary (310/420)** | Pressure filters, UV disinfection |
| **Solids (510)** | Gravity thickeners |

## Quick Start

```bash
# Generate all Excel datasheets from markdown templates
python3 scripts/md_to_excel.py --all

# Generate a single datasheet
python3 scripts/md_to_excel.py templates/101-GR.md

# Validate markdown templates
python3 scripts/validate_template.py --all

# Check Excel completeness before issuing RFQ
python3 scripts/validate_datasheet.py --all
```

## Project Structure

```
templates/               <- Source of truth (markdown)
├── 000-PROJECT-DATA.md
├── 101-SC.md           (Screening Package)
├── 101-GR.md           (Grit Removal)
├── 130-CL.md           (Primary Clarifier)
├── 130-LC.md           (Lamella Clarifier)
├── 230-AT.md           (Aeration Tank)
├── 240-SC.md           (Secondary Clarifier)
├── 310-DMF.md          (Pressure Filter)
├── 420-UV.md           (UV Disinfection)
└── 510-GT.md           (Gravity Thickener)

scripts/
├── md_to_excel.py       <- Generates Excel from markdown
├── excel_styles.py      <- Centralized styling definitions
├── validate_template.py <- Markdown syntax validation
└── validate_datasheet.py <- Excel completeness check

assets/                  <- Generated artifacts (Excel)
├── 101-GR-01 GRIT REMOVAL PACKAGE.xlsx
├── ...

references/              <- Guidance documents
├── RFQ_workflow.md
├── Grit_Removal_Package_guidance.md
├── ...
```

## Workflow

1. **Edit markdown source** - Modify `templates/<equipment>.md`
2. **Validate template** - `python3 scripts/validate_template.py templates/<equipment>.md`
3. **Generate Excel** - `python3 scripts/md_to_excel.py templates/<equipment>.md`
4. **Fill project data** - Complete values in generated Excel
5. **Run completeness check** - `python3 scripts/validate_datasheet.py assets/<equipment>.xlsx`
6. **Issue with RFQ** - Include P&ID, site plan, hydraulic profile

## Template Format

Templates use markdown with YAML frontmatter:

```markdown
---
schema_version: 1
template_id: 101-GR
title: GRIT REMOVAL PACKAGE
service: GRIT REMOVAL
has_motor: true
category: headworks
---

## Operating / Design Data
| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | qavg | Design Average Flow | | m³/h | number | |
| 2 | redundancy | Redundancy | | | dropdown | ["N+1","2x50%"] |
```

### Field Types

| Type | Excel Behavior |
|------|----------------|
| `number` | Numeric input cell |
| `text` | Free text input |
| `dropdown` | Data validation list |
| `date` | Date formatted cell |
| `readonly` | Protected cell |

## Excel Output Features

- Professional monochrome styling (no color fills)
- Document control block with approval fields (DES BY, CHK BY, APP BY)
- Numbered rows for easy reference
- Data validation dropdowns
- Single-page print layout (portrait, letter size)
- Revision history tracking

## Requirements

- Python 3.8+
- openpyxl
- PyYAML

```bash
pip install openpyxl pyyaml
```

## License

Proprietary - Puran Water
