# Template Format

Markdown template structure, field types, and frontmatter reference.

## Table of Contents

- [Template Structure](#template-structure)
- [YAML Frontmatter](#yaml-frontmatter)
- [Template ID Convention](#template-id-convention)
- [Field Types](#field-types)
- [Section Reference](#section-reference)
- [Equipment Categories](#equipment-categories)

---

## Template Structure

Every template is a markdown file with YAML frontmatter followed by standard sections:

```markdown
---
schema_version: 1
template_id: 101-GR
title: GRIT REMOVAL PACKAGE
service: GRIT REMOVAL
has_motor: true
has_electrical: false
category: headworks
---

# GRIT REMOVAL PACKAGE DATASHEET

## Document Control
| Field | Value |
|-------|-------|
| Project | |
| Client | |
| Equipment Tag | |
| Document No | |
| Revision | |
| Date | |

## Service Information
| Field | Value |
|-------|-------|
| Service | GRIT REMOVAL |
| Location | |
| Manufacturer | |
| Model | |
| P&ID No | |

## Operating / Design Data
| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | qavg | Design Average Flow | | m³/h | number | |
| 2 | qpeak | Design Peak Flow | | m³/h | number | |
| 3 | redundancy | Redundancy Philosophy | | | dropdown | ["N+1","2x50%","2x100%"] |
| 4 | grit_type | Grit Removal Technology | | | dropdown | ["Vortex","Aerated","Horizontal"] |

## Materials
| # | Component | Specification |
|---|-----------|---------------|
| 1 | Tank/Chamber | |
| 2 | Wetted Parts | |
| 3 | Hardware | |

## Driver / Motor Data
| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | voltage | Voltage | | V | dropdown | ["380","400","415","480"] |
| 2 | phase | Phase | | | dropdown | ["3"] |
| 3 | frequency | Frequency | | Hz | dropdown | ["50","60"] |

## Remarks

## Revision History
| Rev | Date | Description | By |
|-----|------|-------------|-----|
| 0 | | Initial issue | |
```

---

## YAML Frontmatter

| Field | Required | Description |
|-------|----------|-------------|
| `schema_version` | Yes | Always `1` (for future migrations) |
| `template_id` | Yes | Unique ID (see [Template ID Convention](#template-id-convention)) |
| `title` | Yes | Equipment title for Excel header |
| `service` | Yes | Default service description |
| `has_motor` | Yes | `true` → include Driver/Motor Data section |
| `has_electrical` | No | `true` → include Electrical Data section (non-motor power) |
| `category` | Yes | Equipment category for grouping |

**Categories**: `preliminary_treatment`, `primary_treatment`, `secondary_treatment`, `tertiary_treatment`, `disinfection`, `brine`, `sludge`, `biogas`, `pumps`, `blowers`, `mixers`, `tanks`, `vessels`, `heat_exchangers`, `filters`

---

## Template ID Convention

Two ID formats based on equipment scope:

### Area-Prefixed IDs (`NNN-XXX`)

Process-specific equipment tied to a treatment area:

| Pattern | Area | Examples |
|---------|------|----------|
| `101-*` | Preliminary Treatment | `101-SC`, `101-GR`, `101-FSC` |
| `130-*` | Primary Treatment | `130-CL`, `130-DAF`, `130-CM` |
| `230-*` | Secondary - Aeration | `230-AT`, `230-BL`, `230-DF` |
| `240-*` | Secondary - Clarification | `240-SC`, `240-CM` |
| `250-*` | MBR Systems | `250-MBR`, `250-XMBR` |
| `310-*` | Tertiary Filtration | `310-DMF`, `310-GSF`, `310-DSC` |
| `350-*` | Reverse Osmosis | `350-ROS`, `350-ROM`, `350-ROV` |
| `401-*` | Chemical Disinfection | `401-CL`, `401-O3` |
| `420-*` | UV Disinfection | `420-UV`, `420-UVR` |
| `501-*` | Evaporation | `501-MEE`, `501-MVR` |
| `610-*` | Dewatering | `610-BFP`, `610-CFG` |
| `640-*` | Digestion | `640-DIG`, `640-GH` |
| `7XX-*` | Biogas Treatment | `701-CND`, `710-FE`, `740-MEM` |

### Universal IDs (`XX-YYY`)

Equipment used across multiple process areas (no area prefix):

| Pattern | Equipment Type | Examples |
|---------|---------------|----------|
| `PP-*` | Pumps | `PP-CEN`, `PP-PCP`, `PP-SUB`, `PP-HP` |
| `BL-*` | Blowers | `BL-PD`, `BL-TURBO`, `BL-CENT` |
| `MX-*` | Mixers | `MX-SUB`, `MX-TOPENTRY`, `MX-STATIC` |
| `TK-*` | Tanks | `TK-POLY`, `TK-FRP`, `TK-SS`, `TK-API` |
| `V-*` | Pressure Vessels | `V-ASME`, `V-FRP`, `V-SS` |
| `HX-*` | Heat Exchangers | `HX-ST`, `HX-PF`, `HX-AC` |
| `FL-*` | Strainers/Filters | `FL-BASKET`, `FL-CART`, `FL-AUTO` |

Select universal templates based on application requirements rather than process area.

---

## Field Types

| Type | Excel Behavior | Example |
|------|----------------|---------|
| `number` | Numeric input cell | Flows, dimensions, power |
| `text` | Free text input | Descriptions, notes, model numbers |
| `dropdown` | Data validation list from Options column | Redundancy, material grades |
| `date` | Date-formatted cell | Revision dates |
| `readonly` | Protected/calculated cell | Reference values, pre-filled defaults |

### Options Column Format

For `dropdown` type, the Options column must contain a valid JSON array:

```markdown
| 3 | redundancy | Redundancy | | | dropdown | ["N+1","2x50%","2x100%"] |
| 4 | material | Wetted Material | | | dropdown | ["304 SS","316 SS","Duplex"] |
```

---

## Section Reference

| Section | Description | Always Present |
|---------|-------------|----------------|
| **Document Control** | Project, Client, Equipment Tag, Revision | Yes |
| **Service Information** | Service, Location, Manufacturer, Model, P&ID | Yes |
| **Operating / Design Data** | Process parameters (numbered rows with field_id) | Yes |
| **Materials** | Materials of construction for key components | Yes |
| **Driver / Motor Data** | Motor specs (voltage, power, efficiency) | If `has_motor: true` |
| **Electrical Data** | Non-motor power requirements | If `has_electrical: true` |
| **Remarks** | Special requirements, notes | Yes |
| **Revision History** | Change tracking | Yes |

---

## Equipment Categories

### Motor-driven equipment (`has_motor: true`)

Includes Driver/Motor Data section for motor specifications:

| Category | Examples |
|----------|----------|
| Screening | 101-SC, 101-FSC, 101-MAC |
| Grit | 101-GR, 101-GW |
| Clarifiers | 130-CL, 240-SC |
| Mechanisms | 130-CM, 240-CM, 601-TM |
| Aeration | 230-AT |
| Blowers | BL-PD, BL-TURBO, BL-CENT, BL-REGEN |
| Pumps | PP-CEN, PP-PCP, PP-SUB, PP-HP, PP-DIAP (all PP-*) |
| Mixers | MX-SUB, MX-TOPENTRY, MX-SIDEENTRY |
| Filtration | 310-DMF, 310-DSC, 310-GSF |
| Membranes | 250-MBR, 320-UF, 320-PUF |
| Dewatering | 610-BFP, 610-CFG, 610-FP, 610-VP |
| Biogas | 701-CND, 710-BIO, 730-CMP |
| Conveyors | 101-CV, 101-WC |

### Non-motor with power requirements (`has_electrical: true`)

Includes Electrical Data section for non-motor power:
- UV Reactor Module (420-UVR) — ballasts, control systems
- Ozone Generator (401-O3) — power supply, cooling

### Passive equipment (neither motor nor electrical)

No power section:

| Category | Examples |
|----------|----------|
| Screens | 101-SCR (manual) |
| Clarifiers | 130-LC (lamella) |
| Diffusers | 230-DF |
| Filter internals | 310-FV |
| Membranes | 350-ROM, 350-ROV |
| Vessels | V-ASME, V-FRP, V-SS, TK-* |
| Heat Exchangers | HX-ST, HX-PF, HX-AC |
| Static Mixers | MX-STATIC, MX-JET |
| Strainers | FL-BASKET, FL-CART, FL-BAG |

---

## Excel Output Features

Generated Excel files include:
- **Monochrome styling** — no color fills, solid black borders
- **Typography hierarchy** — 12pt bold title, 10pt bold headers, 10pt body
- **Document control block** — top-right with Project, Client, Revision
- **Approval fields** — DES BY, CHK BY, APP BY with signature/date
- **Numbered rows** — easy reference during technical discussions
- **Data validation** — dropdown lists from Options column
- **Single-page fit** — portrait, letter size, narrow margins
- **Revision history** — bottom of sheet
