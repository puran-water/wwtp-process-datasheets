---
name: wwtp-process-datasheets
description: Create vendor-ready RFQ process datasheets (Excel) for wastewater treatment equipment including screening packages, grit removal, primary clarifiers, lamella clarifiers, aeration systems, secondary clarifiers, pressure filters, UV disinfection, and gravity thickeners. Use when preparing procurement packages for WWTP equipment quotes.
---

# WWTP Process Datasheets

Markdown-native templates with automated Excel generation for **pricing-ready** WWTP equipment RFQs.

## Architecture

```
templates/           <- Source of truth (markdown)
scripts/             <- Automation (Python)
assets/              <- Generated artifacts (Excel)
references/          <- Guidance documents
components/          <- BOM definitions
```

**Markdown is source of truth** — Edit templates, generate Excel for distribution.

## Quick Start

1. Edit `templates/<equipment>.md` with project values
2. Validate: `python scripts/validate_template.py <template>`
3. Generate: `python scripts/md_to_excel.py <template>`
4. Check: `python scripts/validate_datasheet.py <excel>`
5. Issue with P&ID, site plan, hydraulic profile

## Equipment Coverage

| Area | Templates |
|------|-----------|
| Headworks (101) | 101-SC, 101-GR, 101-SCR, 101-WC, 101-CV, 101-GW |
| Primary (130) | 130-CL, 130-LC, 130-CM |
| Secondary (230/240) | 230-AT, 230-BL, 230-DF, 240-SC, 240-CM |
| Tertiary (310/420) | 310-DMF, 310-FV, 420-UV, 420-UVR |
| Solids (601) | 601-GT, 601-TM |
| Pumps (600) | 600-PP-CEN, 600-PP-PCP, 600-PP-SUB |

**Full catalog**: See `references/equipment_catalog.md`

## Scripts

| Script | Purpose |
|--------|---------|
| `md_to_excel.py` | Convert markdown → Excel |
| `validate_template.py` | Validate markdown syntax |
| `validate_datasheet.py` | Check Excel completeness |
| `generate_bom.py` | Expand package → components |

**Detailed usage**: See `references/scripts_guide.md`

## References

| Reference | When to Read |
|-----------|--------------|
| `equipment_catalog.md` | Selecting templates, equipment coverage |
| `template_format.md` | Creating/editing templates, field types |
| `scripts_guide.md` | CLI options, automation details |
| `bom_system.md` | Package → component relationships |
| `RFQ_workflow.md` | General procurement workflow |
| `<Equipment>_guidance.md` | Process-specific design guidance |

## Key Principles

- **Markdown is source of truth** — All data in `templates/`, Excel for distribution only
- **Monochrome styling** — No color fills, solid black borders, typography hierarchy
- **Single-page fit** — Portrait, letter size, narrow margins
- **Peak hourly flow (m³/h)** — Process design basis (not peak day)
- **Numbered rows** — Easy reference during technical discussions

## What "Pricing-Ready" Means

A vendor can produce a **priced proposal** because the datasheet captures:
- **Process duty** — flows, loadings, performance targets
- **Hydraulics** — elevations, headloss, tie-in locations
- **Mechanical scope** — materials, redundancy, ancillaries
- **Site/utilities** — power, environment, controls interface
- **Vendor response** — model, exclusions, lead time fields

## Common Commands

```bash
# Generate all Excel from markdown
python scripts/md_to_excel.py --all

# Validate all templates
python scripts/validate_template.py --all

# Check all datasheets ready for RFQ
python scripts/validate_datasheet.py --all

# Generate BOM from package
python scripts/generate_bom.py templates/101-SC.md
```
