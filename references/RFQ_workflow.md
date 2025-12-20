# RFQ datasheet workflow

## Goal

Create a datasheet that lets a vendor quote **without guessing** and without hiding scope in assumptions.

If a vendor must assume basics (flow basis, solids loading, materials, available head, backwash disposal, etc.), you will get:

- non-comparable bids,
- exclusions and change orders,
- or a "safe" (inflated) price.

## Architecture: Markdown-First

This skill uses **markdown as the source of truth** for all datasheet templates:

```
templates/               <- Source of truth (edit these)
├── 000-PROJECT-DATA.md
├── 101-SC.md
├── 101-GR.md
├── ...

assets/                  <- Generated artifacts (don't edit directly)
├── 000-PROJECT-DATA.xlsx
├── 101-SC-01 SCREENING PACKAGE.xlsx
├── ...
```

**Benefits:**
- Markdown is easy for LLMs to read and edit
- Git diff/merge/PR works naturally on text files
- Consistent Excel styling via centralized conversion script
- Content and presentation cleanly separated

## Deliverables you should send with the datasheet

Minimum package for credible pricing:

1. **RFQ letter / instructions**
   - Pricing basis: budgetary vs firm, supply-only vs installed
   - Commercial terms: taxes, freight, incoterms, bid validity, currency
   - Schedule: required lead time, submittals, FAT/SAT expectations
2. **Process schematic**
   - PFD (at minimum); P&ID if available
3. **Hydraulic information**
   - Key elevations, tie-in locations, available headloss
4. **Site constraints**
   - Indoor/outdoor, footprint, access/rigging, environmental conditions
5. **Utilities**
   - Electrical service (V/Ph/Hz), water, air, drains
6. **Performance requirements**
   - Target cut size / effluent quality, turndown, redundancy philosophy

## Step 1: Edit Markdown Source

For new templates or modifications to existing ones, edit the markdown files directly:

```bash
# Edit a template
vim templates/101-GR.md
```

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
| 2 | redundancy | Redundancy | | | dropdown | ["N+1","2x50%"] |
```

### Field Types

| Type | Behavior |
|------|----------|
| `number` | Numeric input |
| `text` | Free text |
| `dropdown` | Data validation list (JSON array in Options column) |
| `date` | Date formatted |
| `readonly` | Protected/calculated |

## Step 2: Validate Markdown

Before generating Excel, validate the markdown syntax:

```bash
# Validate a single template
python scripts/validate_template.py templates/101-GR.md

# Validate all templates
python scripts/validate_template.py --all
```

The validator checks:
- YAML frontmatter required fields
- Required sections present
- Table structure (correct columns)
- Valid field types
- Dropdown options format (JSON arrays)

## Step 3: Generate Excel

Convert markdown to Excel:

```bash
# Convert a single template
python scripts/md_to_excel.py templates/101-GR.md

# Convert all templates
python scripts/md_to_excel.py --all
```

Excel files are generated in `assets/` with:
- Clean monochrome styling (no color fills, black borders)
- Single-page print layout
- Data validation dropdowns
- Numbered rows for reference

## Step 4: Fill Project-Specific Data

Open the generated Excel file and complete:
- Document control (Project, Client, Equipment Tag, etc.)
- Project-specific values in data tables
- Any remarks or special requirements

**Note:** For template changes (adding fields, changing options), edit the markdown source and regenerate. Only fill in project-specific values in Excel.

## Step 5: Run Completeness Check

Before issuing the RFQ, validate the filled datasheet:

```bash
# Validate a single datasheet
python scripts/validate_datasheet.py "assets/101-GR-01 GRIT REMOVAL PACKAGE.xlsx"

# Validate all datasheets
python scripts/validate_datasheet.py --all
```

The script checks for:
- **Required fields left blank** (with row numbers)
- **Unit ambiguity** (numeric values without units)
- Generates a completeness percentage

Only issue datasheets with **STATUS: READY FOR RFQ**.

## Step 6: Manual Review

Even after automated validation, scan for:

- Any obvious **physics conflicts**, e.g.:
  - lamella clarifier asked to meet an effluent turbidity with no coag/floc strategy
  - pressure filter backwash rate specified but no backwash water source
  - grit removal cut size target without defining design flow/peaking

## Git Workflow

```bash
# Edit markdown source
vim templates/101-GR.md

# See what changed (readable diff!)
git diff templates/101-GR.md

# Validate and regenerate
python scripts/validate_template.py templates/101-GR.md
python scripts/md_to_excel.py templates/101-GR.md

# Commit both source and artifact
git add templates/101-GR.md assets/101-GR-01*.xlsx
git commit -m "Update grit removal flow requirements"
```

**Diff example:**
```diff
-| 3 | redundancy | Redundancy Philosophy | | | dropdown | ["N+1","2x50%"] |
+| 3 | redundancy | Redundancy Philosophy | | | dropdown | ["N+1","2x50%","2x100%","3x50%","None"] |
```

## Common failure modes (and how to avoid them)

- **Not defining peak flow basis** (peak hour vs peak day vs wet weather)
  - Fix: state each explicitly, and give the peaking factors if that's the basis.
- **No disposal destination** for grit, sludge, or filter backwash
  - Fix: define where each waste stream goes and any constraints (solids content, flow, intermittency).
- **Material selection by habit** (e.g., "304SS everywhere") without chemistry context
  - Fix: record chlorides, temperature, H2S/odor exposure, cleaning chemicals.
- **Controls scope ambiguity**
  - Fix: specify whether vendor supplies PLC/HMI, I/O list expectations, and comms protocol.
- **Editing Excel instead of markdown**
  - Fix: Always edit templates in `templates/`, then regenerate Excel. Only fill project-specific values in Excel.

## Quick Reference

| Task | Command |
|------|---------|
| Edit template | `vim templates/<id>.md` |
| Validate markdown | `python scripts/validate_template.py templates/<id>.md` |
| Generate Excel | `python scripts/md_to_excel.py templates/<id>.md` |
| Validate all markdown | `python scripts/validate_template.py --all` |
| Generate all Excel | `python scripts/md_to_excel.py --all` |
| Check completeness | `python scripts/validate_datasheet.py assets/<file>.xlsx` |
