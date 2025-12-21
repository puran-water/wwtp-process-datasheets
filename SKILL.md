---
name: wwtp-process-datasheets
description: Create vendor-ready RFQ process datasheets (Excel) for wastewater treatment equipment. Covers 102 templates across the full treatment train including preliminary treatment (screening, grit), primary clarification, secondary biological treatment (activated sludge, MBR, SBR, trickling filters, RBC), tertiary treatment (filtration, UF, GAC, IX, RO), disinfection (chlorine, ozone, UV), brine management (evaporators, crystallizers), sludge handling (thickening, dewatering, digestion), and biogas treatment (conditioning, H2S removal, upgrading, flaring). Also includes universal equipment templates for pumps, blowers, mixers, tanks, vessels, heat exchangers, and filters. Use when preparing procurement packages for WWTP equipment quotes.
---

# WWTP Process Datasheets

Markdown-native templates with automated Excel generation for **pricing-ready** WWTP equipment RFQs.

## Architecture

```
templates/           <- Source of truth (102 markdown templates)
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

## Equipment Coverage (102 Templates)

### Universal Equipment (36 templates)

| Category | Templates |
|----------|-----------|
| Pumps | PP-CEN, PP-PCP, PP-SUB, PP-LOBE, PP-GEAR, PP-DIAP, PP-PERI, PP-SCREW, PP-HP, PP-CIP, PP-VERT, PP-AIRLIFT |
| Blowers | BL-PD, BL-TURBO, BL-CENT, BL-REGEN |
| Mixers | MX-SUB, MX-TOPENTRY, MX-SIDEENTRY, MX-JET, MX-STATIC |
| Tanks | TK-POLY, TK-FRP, TK-SS, TK-BOLT, TK-API |
| Vessels | V-ASME, V-FRP, V-SS |
| Heat Exchangers | HX-ST, HX-PF, HX-AC |
| Filters | FL-BASKET, FL-CART, FL-BAG, FL-AUTO |

### Process Equipment (66 templates)

| Area | Templates |
|------|-----------|
| Preliminary (101-120) | 101-SC, 101-SCR, 101-FSC, 101-GR, 101-GSP, 101-GW, 101-MAC, 101-OGS, 101-WC, 101-CV, 120-CT |
| Primary (130) | 130-CL, 130-LC, 130-CM, 130-DAF, 130-SAT |
| Secondary Suspended (201-240) | 201-UASB, 201-FFR, 230-AT, 230-BL, 230-DF, 240-SC, 240-CM |
| Secondary Attached (250-280) | 250-MBR, 250-XMBR, 260-TF, 260-TFD, 270-RBC, 280-SBR, 280-DEC |
| Tertiary Filtration (310) | 310-DMF, 310-FV, 310-DSC, 310-GSF |
| Tertiary Membrane (320) | 320-UF, 320-PUF |
| Tertiary Adsorption (330) | 330-GAC, 330-IX |
| Tertiary Other (340-350) | 340-DEG, 350-ROM, 350-ROV, 350-ROS |
| Disinfection (401-420) | 401-CL, 401-O3, 401-O3D, 420-UV, 420-UVR |
| Brine (501-520) | 501-MEE, 501-MVR, 510-FC, 520-ATFD |
| Sludge (601-640) | 601-GT, 601-TM, 610-BFP, 610-CFG, 610-FP, 610-VP, 640-DIG, 640-GH |
| Biogas (701-750) | 701-CND, 710-FE, 710-BIO, 730-CMP, 740-MEM, 750-FLR |

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

## Key Principles

- **Markdown is source of truth** — All data in `templates/`, Excel for distribution only
- **Monochrome styling** — No color fills, solid black borders, typography hierarchy
- **Single-page fit** — Portrait, letter size, narrow margins
- **Peak hourly flow (m³/h)** — Process design basis (not peak day)
- **Numbered rows** — Easy reference during technical discussions
- **20+ operating fields** — Comprehensive data capture per template

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

## Template ID Convention

- **Area-prefixed**: `NNN-XXX` (e.g., `101-SC`, `640-DIG`) — Process-specific equipment
- **Universal**: `XX-YYY` (e.g., `PP-CEN`, `BL-TURBO`) — Equipment used across areas

Select universal templates based on application rather than area code.
