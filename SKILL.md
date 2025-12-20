---
name: wwtp-process-datasheets-rfq
description: Create vendor-ready RFQ process datasheets (Excel) for wastewater treatment equipment including screening packages, grit removal, primary clarifiers, lamella clarifiers, aeration systems, secondary clarifiers, pressure filters, UV disinfection, and gravity thickeners. Use when preparing procurement packages for WWTP equipment quotes.
---

# WWTP Process Datasheets for Equipment Procurement (RFQ)

This skill provides **markdown-native datasheet templates** with automated Excel generation for compiling **pricing-ready** process and mechanical requirements for common wastewater treatment package equipment.

## Architecture

```
templates/               <- Source of truth (markdown)
├── 000-PROJECT-DATA.md
├── 101-SC.md
├── 101-GR.md
├── ...

scripts/
├── md_to_excel.py       <- Generates Excel from markdown
├── excel_styles.py      <- Centralized styling definitions
├── validate_template.py <- Markdown syntax validation
├── validate_datasheet.py <- Excel completeness check

assets/                  <- Generated artifacts (Excel)
├── 000-PROJECT-DATA.xlsx
├── 101-SC-01 SCREENING PACKAGE.xlsx
├── ...
```

**Benefits of markdown-first approach:**
- **LLM-friendly** – Easy to read, edit, and manipulate programmatically
- **Git-native** – Diff, rollback, PR, merge conflicts visible in plain text
- **Consistent styling** – All Excel output uses centralized styling definitions
- **Maintainable** – Content and presentation cleanly separated

## Equipment types covered

### Headworks (Area 101)
- **Screening packages** – bar screens, fine screens, washer-compactors
- **Grit removal packages** – vortex, aerated, horizontal flow systems

### Primary Treatment (Area 130)
- **Primary clarifiers** – circular/rectangular sedimentation tanks
- **Lamella clarifiers** – inclined plate settlers (distinct from conventional clarifiers)

### Secondary Treatment (Areas 230, 240)
- **Aeration tanks / blower systems** – fine bubble diffusers, blowers, basin equipment
- **Secondary clarifiers** – final clarifiers for activated sludge separation

### Tertiary Treatment (Areas 310, 420)
- **Pressure filters / dual media filters** – tertiary filtration systems
- **UV disinfection** – open channel and closed vessel UV systems

### Solids Handling (Area 510)
- **Gravity thickeners** – sludge thickening tanks

## Templates (Markdown Sources)

All templates are markdown files with YAML frontmatter:

| Template | Description |
|----------|-------------|
| `templates/000-PROJECT-DATA.md` | Master project data (common parameters, design basis) |
| `templates/101-SC.md` | Screening Package |
| `templates/101-GR.md` | Grit Removal Package |
| `templates/130-CL.md` | Primary Clarifier |
| `templates/130-LC.md` | Lamella Clarifier |
| `templates/230-AT.md` | Aeration Tank |
| `templates/240-SC.md` | Secondary Clarifier |
| `templates/310-DMF.md` | Pressure Filter |
| `templates/420-UV.md` | UV Disinfection |
| `templates/510-GT.md` | Gravity Thickener |

### Template Structure

```markdown
---
schema_version: 1
template_id: 101-GR
title: GRIT REMOVAL PACKAGE
service: GRIT REMOVAL
has_motor: true
category: headworks
---

# GRIT REMOVAL PACKAGE DATASHEET

## Document Control
| Field | Value |
|-------|-------|
| Project | |
| Client | |
...

## Operating / Design Data
| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | qavg | Design Average Flow | | m³/h | number | |
| 2 | redundancy | Redundancy Philosophy | | | dropdown | ["N+1","2x50%","2x100%"] |
...
```

### Field Types

| Type | Excel Behavior |
|------|----------------|
| `number` | Numeric input cell |
| `text` | Free text input |
| `dropdown` | Data validation list (from JSON array in Options column) |
| `date` | Date formatted cell |
| `readonly` | Protected cell (for calculated/reference values) |

## Assets (Generated Excel)

Excel files are generated from markdown templates using `md_to_excel.py`:

| Asset | Source Template |
|-------|-----------------|
| `assets/000-PROJECT-DATA.xlsx` | `templates/000-PROJECT-DATA.md` |
| `assets/101-SC-01 SCREENING PACKAGE.xlsx` | `templates/101-SC.md` |
| `assets/101-GR-01 GRIT REMOVAL PACKAGE.xlsx` | `templates/101-GR.md` |
| `assets/130-CL-01 PRIMARY CLARIFIER.xlsx` | `templates/130-CL.md` |
| `assets/130-LC-01 LAMELLA CLARIFIER.xlsx` | `templates/130-LC.md` |
| `assets/230-AT-01 AERATION TANK.xlsx` | `templates/230-AT.md` |
| `assets/240-SC-01 SECONDARY CLARIFIER.xlsx` | `templates/240-SC.md` |
| `assets/310-DMF-01 PRESSURE FILTER.xlsx` | `templates/310-DMF.md` |
| `assets/420-UV-01 UV DISINFECTION.xlsx` | `templates/420-UV.md` |
| `assets/510-GT-01 GRAVITY THICKENER.xlsx` | `templates/510-GT.md` |

**Excel Features:**
- **Monochrome styling** – no color fills, solid black borders, typography-based hierarchy
- Document control block (Project, Client, Equipment Tag, Revision tracking)
- **DRIVER/MOTOR DATA section** – integrated motor specifications for motor-driven equipment
- Numbered rows for easy reference during technical discussions
- Print-optimized layout (single-page fit, narrow margins)
- Data validation dropdowns for standardized fields
- Revision history block

## References (guidance documents)

- `references/RFQ_workflow.md` – general RFQ workflow and completeness checks
- `references/Screening_Package_guidance.md`
- `references/Grit_Removal_Package_guidance.md`
- `references/Primary_Clarifier_guidance.md`
- `references/Lamella_Clarifier_guidance.md`
- `references/Aeration_System_guidance.md`
- `references/Secondary_Clarifier_guidance.md`
- `references/Pressure_Filter_guidance.md`
- `references/UV_Disinfection_guidance.md`
- `references/Gravity_Thickener_guidance.md`
- `references/Public_templates_found.md` – public reference sources

## Scripts (automation tools)

| Script | Purpose |
|--------|---------|
| `scripts/md_to_excel.py` | Convert markdown templates to Excel |
| `scripts/excel_styles.py` | Centralized styling definitions |
| `scripts/validate_template.py` | Validate markdown template syntax |
| `scripts/validate_datasheet.py` | Check Excel datasheet completeness |
| `scripts/config/required_fields.yaml` | Required fields configuration |

### Generate Excel from Markdown

```bash
# Convert a single template
python scripts/md_to_excel.py templates/101-GR.md

# Convert all templates
python scripts/md_to_excel.py --all

# Specify output directory
python scripts/md_to_excel.py --all --output-dir assets/
```

### Validate Markdown Templates

```bash
# Validate a single template
python scripts/validate_template.py templates/101-GR.md

# Validate all templates
python scripts/validate_template.py --all
```

**Example Output:**
```
Validating 10 template(s)...
============================================================

File: 101-GR.md
  STATUS: VALID

File: 101-SC.md
  STATUS: VALID
...

============================================================
Results: 10 passed, 0 failed
```

### Validate Excel Completeness

```bash
# Validate a single datasheet
python scripts/validate_datasheet.py "assets/101-GR-01 GRIT REMOVAL PACKAGE.xlsx"

# Validate all datasheets
python scripts/validate_datasheet.py --all

# Output as JSON
python scripts/validate_datasheet.py --all --format json
```

**Example Output:**
```
============================================================
DATASHEET VALIDATION REPORT
============================================================
File: 101-GR-01 GRIT REMOVAL PACKAGE.xlsx
Template: 101-GR
Completeness: 78% (7/9 required fields)

MISSING REQUIRED FIELDS:
  Row  21: Target Grit Cut Size - Required field is empty
  Row  23: Required Removal Efficiency - Required field is empty

WARNINGS:
  Row  22: Specific Gravity - Numeric value without units specified

STATUS: NOT READY - Fix missing fields
============================================================
```

## Recommended workflow

1. **Edit markdown source** – Open `templates/<equipment>.md` and edit content
2. **Validate markdown** – `python scripts/validate_template.py templates/<equipment>.md`
3. **Generate Excel** – `python scripts/md_to_excel.py templates/<equipment>.md`
4. **Fill project data** – Complete project-specific values in generated Excel
5. **Run completeness check** – `python scripts/validate_datasheet.py assets/<equipment>.xlsx`
6. **Issue with RFQ package** – Include P&ID, site plan, hydraulic profile

### Git Workflow

```bash
# Edit markdown source
vim templates/101-GR.md

# See what changed
git diff templates/101-GR.md

# Validate and regenerate
python scripts/validate_template.py templates/101-GR.md
python scripts/md_to_excel.py templates/101-GR.md

# Commit both source and artifact
git add templates/101-GR.md assets/101-GR-01*.xlsx
git commit -m "Update grit removal flow requirements"
```

## What "pricing-ready" means

A vendor can produce a **priced proposal** because the datasheet captures:
- **Process duty** – flows, loadings, performance targets
- **Hydraulics** – elevations, headloss, tie-in locations
- **Mechanical scope** – materials, redundancy, ancillaries
- **Site / utilities** – power, environment, controls interface
- **Vendor response fields** – model, exclusions, lead time

## Template Structure

Each template follows a consistent structure:

| Section | Description |
|---------|-------------|
| **Title** | Equipment type and datasheet label |
| **Document Control** | Project, Client, Equipment Tag, Revision info (top-right) |
| **Service Info** | Service, Location, Manufacturer, Model, P&ID No (top-left) |
| **OPERATING/DESIGN DATA** | Process parameters with numbered rows |
| **MATERIALS** | Materials of construction for key components |
| **DRIVER/MOTOR DATA** | Motor specifications (for motor-driven equipment only) |
| **REMARKS** | Special requirements or clarifications |
| **REVISION HISTORY** | Revision tracking block |

**Motor-driven equipment** (with DRIVER/MOTOR section):
- Screening Package, Grit Removal, Primary Clarifier, Aeration Tank, Secondary Clarifier, Pressure Filter, Gravity Thickener

**Non-motor equipment** (no DRIVER/MOTOR section):
- Lamella Clarifier, UV Disinfection

## Notes

- **Markdown is source of truth** – Edit templates in `templates/`, not Excel files directly
- Templates use **clean monochrome styling** – no color fills, solid black borders, typography-based hierarchy
- **Lamella clarifiers** (inclined plate settlers) are distinct from conventional **primary clarifiers** (sedimentation tanks)
- All templates include numbered rows for easy reference during technical discussions
- Templates are optimized for **single-page print** (portrait, letter size, narrow margins)
- Run `python scripts/validate_template.py --all` to validate markdown syntax
- Run `python scripts/validate_datasheet.py --all` before issuing RFQ package
