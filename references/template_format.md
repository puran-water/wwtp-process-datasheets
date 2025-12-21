# Template Format

Markdown template structure, field types, and frontmatter reference.

## Table of Contents

- [Template Structure](#template-structure)
- [YAML Frontmatter](#yaml-frontmatter)
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
| `template_id` | Yes | Unique ID (e.g., `101-GR`, `600-PP-CEN`) |
| `title` | Yes | Equipment title for Excel header |
| `service` | Yes | Default service description |
| `has_motor` | Yes | `true` → include Driver/Motor Data section |
| `has_electrical` | No | `true` → include Electrical Data section (non-motor power) |
| `category` | Yes | Equipment category for grouping |

**Categories**: `headworks`, `primary`, `secondary`, `tertiary`, `solids`, `pumps`

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
- Screening Package (101-SC)
- Grit Removal (101-GR)
- Primary Clarifier (130-CL)
- Aeration Tank (230-AT)
- Blower Package (230-BL)
- Secondary Clarifier (240-SC)
- Pressure Filter (310-DMF)
- Gravity Thickener (601-GT)
- All pumps (600-PP-*)
- All mechanisms (130-CM, 240-CM, 601-TM)
- Washer-Compactor (101-WC)
- Screw Conveyor (101-CV)
- Grit Washer (101-GW)

### Non-motor with power requirements (`has_electrical: true`)

Includes Electrical Data section for non-motor power:
- UV Reactor Module (420-UVR) — ballasts, control systems

### Passive equipment (neither motor nor electrical)

No power section:
- Lamella Clarifier (130-LC)
- Diffuser Grid (230-DF)
- Filter Vessel (310-FV)
- Screen (101-SCR) — unless motorized

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
