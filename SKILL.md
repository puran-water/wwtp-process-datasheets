---
name: wwtp-process-datasheets
description: |
  Tier 2 skill for generating vendor-ready RFQ process datasheets (Excel) from equipment
  list artifacts. Covers 102 templates across the full treatment train including preliminary
  treatment (screening, grit), primary clarification, secondary biological treatment
  (activated sludge, MBR, SBR, trickling filters, RBC), tertiary treatment (filtration, UF,
  GAC, IX, RO), disinfection (chlorine, ozone, UV), brine management (evaporators,
  crystallizers), sludge handling (thickening, dewatering, digestion), and biogas treatment
  (conditioning, H2S removal, upgrading, flaring). Also includes universal equipment
  templates for pumps, blowers, mixers, tanks, vessels, heat exchangers, and filters.
  Use when: (1) Equipment list artifact is complete, (2) Preparing procurement packages
  for WWTP equipment quotes, (3) Generating RFQ packages for FEED/BEP deliverables.
---

# WWTP Process Datasheets

Tier 2 skill: Markdown-native templates with automated Excel generation for **pricing-ready** WWTP equipment RFQs.

## Integration with Skill Hierarchy

This skill consumes equipment list artifacts and produces RFQ datasheets that feed into:
- **rfq-package-skill** (Tier 3) - Complete vendor RFQ packages
- **feed-bep-skill** (Tier 3) - Front-End Engineering deliverables

### Source Format Exception

**This skill uses Markdown (not QMD) as source of truth.** This is a documented exception
to the Tier 2 "QMD as source of truth" pattern for the following reasons:

1. **102 pre-existing templates** - Templates were developed before the QMD standardization
2. **Table-heavy format** - Process datasheets are 90%+ tabular data, where Markdown tables
   are more readable and editable than QMD embedded YAML
3. **Direct Excel mapping** - Markdown table structure maps 1:1 to Excel cells, making
   conversion straightforward without Quarto rendering
4. **RFQ workflow** - Datasheets are often edited by non-engineers (procurement), so
   simpler Markdown format reduces friction

The `md_to_excel.py` script handles conversion directly, bypassing Quarto.

### Input Artifacts

Query from `artifact-registry.yaml`:
- `equipment-list` artifact (eq-001) with equipment array
- `project.yaml` for client/project metadata

### Output Artifacts

| Artifact | Path | Description |
|----------|------|-------------|
| Datasheet MD | `datasheets/{TAG}.md` | Markdown source of truth |
| Datasheet Excel | `datasheets/{TAG}.xlsx` | Vendor-ready RFQ datasheet |

### Artifact Registration

After generating datasheets, register with:
```bash
python scripts/register_datasheets.py --project-dir /path/to/project
```

## Skill Pattern

```
INPUT:
  - artifact-registry.yaml (equipment-list artifact)
  - project.yaml (client, project metadata)

PROCESSING:
  - Query equipment list from registry
  - For each equipment item:
    - Select appropriate template by equipment type
    - Populate template with equipment data
    - Generate Excel datasheet
  - Register all datasheets as artifacts

OUTPUT:
  - datasheets/*.md (markdown sources)
  - datasheets/*.xlsx (Excel files)
  - Updates artifact-registry.yaml
```

## Architecture

```
templates/           <- Source of truth (102 markdown templates)
scripts/             <- Automation (Python)
  ├── md_to_excel.py           <- Convert MD → Excel
  ├── validate_template.py     <- Validate MD syntax
  ├── validate_datasheet.py    <- Check Excel completeness
  ├── generate_bom.py          <- Expand package → components
  └── register_datasheets.py   <- Register artifacts (NEW)
assets/              <- Generated artifacts (Excel)
references/          <- Guidance documents
components/          <- BOM definitions
```

**Markdown is source of truth** — Edit templates, generate Excel for distribution.

## Equipment Type to Template Mapping

Map equipment from equipment-list artifact to datasheet templates:

| Equipment Type Code | Template | Description |
|---------------------|----------|-------------|
| SC | 101-SC | Coarse/Fine Screen |
| GR | 101-GR | Grit Removal |
| EQ | TK-* | Equalization Tank |
| PC | 130-CL | Primary Clarifier |
| AT | 230-AT | Aeration Tank |
| MB | 250-MBR | MBR Membrane |
| BL | BL-* | Blower (by type) |
| PU | PP-* | Pump (by type) |
| MX | MX-* | Mixer (by type) |
| DF | 230-DF | Diffusers |
| UV | 420-UV | UV Disinfection |
| CL | 401-CL | Chlorination |
| AD | 640-DIG | Anaerobic Digester |
| TK | TK-* | Tank (by material) |
| HE | HX-* | Heat Exchanger |
| FT | 310-* | Filter (by type) |

### Template Selection Logic

```python
def select_template(equipment: dict) -> str:
    """Select appropriate template based on equipment type and details."""
    tag = equipment.get('tag', '')
    eq_type = tag.split('-')[1] if '-' in tag else ''
    description = equipment.get('description', '').lower()

    # Blowers - select by type
    if eq_type == 'BL':
        if 'positive displacement' in description or 'pd' in description:
            return 'BL-PD'
        elif 'turbo' in description:
            return 'BL-TURBO'
        elif 'centrifugal' in description:
            return 'BL-CENT'
        else:
            return 'BL-PD'  # Default

    # Pumps - select by type
    if eq_type == 'PU':
        if 'centrifugal' in description:
            return 'PP-CEN'
        elif 'progressive' in description or 'cavity' in description:
            return 'PP-PCP'
        elif 'submersible' in description:
            return 'PP-SUB'
        else:
            return 'PP-CEN'  # Default

    # ... additional logic
```

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
| `equipment_catalog.md` | Complete 102-template inventory with typical applications |
| `template_format.md` | Creating/editing templates, YAML frontmatter, field types, naming conventions |
| `scripts_guide.md` | CLI options, batch processing, CI/CD integration |
| `bom_system.md` | Expand package templates into component BOMs for detailed RFQs |
| `RFQ_workflow.md` | End-to-end procurement workflow, validation checklists |
| `project-info.md` | Python requirements, markdown philosophy, license |

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

**Template naming conventions**: See `references/template_format.md`
