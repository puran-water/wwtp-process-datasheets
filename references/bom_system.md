# BOM System

Bill of Materials generation for package → component expansion.

## Table of Contents

- [Overview](#overview)
- [BOM Definition Files](#bom-definition-files)
- [Quantity Rules](#quantity-rules)
- [Package Templates](#package-templates)
- [Usage](#usage)

---

## Overview

Package templates (like `101-SC`, `230-AT`) define complete systems that include multiple component items. The BOM system allows expanding a filled package template into a list of individual component datasheets to prepare.

**Workflow:**
1. Fill package template with project values
2. Run `generate_bom.py` to list components
3. Fill each component template with service-specific parameters
4. Issue complete datasheet package with RFQ

---

## BOM Definition Files

BOM definitions are YAML files in `components/` directory. Create BOM files as needed for package templates.

### Existing BOM Files

| File | Package |
|------|---------|
| `bom_101-SC.yaml` | Screening Package |
| `bom_101-GR.yaml` | Grit Removal Package |
| `bom_130-CL.yaml` | Primary Clarifier |
| `bom_230-AT.yaml` | Aeration Tank |
| `bom_310-DMF.yaml` | Pressure Filter |
| `bom_420-UV.yaml` | UV Disinfection |
| `bom_601-GT.yaml` | Gravity Thickener |

### Package → Component Relationships

Reference for creating additional BOM files (from `process_units_hierarchy.json`):

| Package | Typical Components |
|---------|-------------------|
| `101-SC` | 101-SCR, 101-WC, 101-CV |
| `101-GR` | 101-GSP, 101-GW, 101-CV, PP-CEN |
| `101-FSC` | 101-WC, 101-CV |
| `130-CL` | 130-CM, PP-CEN |
| `130-DAF` | 130-SAT, PP-CEN |
| `230-AT` | 230-BL, 230-DF, PP-CEN |
| `240-SC` | 240-CM, PP-CEN |
| `250-MBR` | BL-REGEN, PP-CEN |
| `250-XMBR` | PP-CEN, PP-HP |
| `260-TF` | 260-TFD, PP-CEN |
| `280-SBR` | 280-DEC, 230-BL, 230-DF, MX-SUB |
| `310-DMF` | 310-FV, PP-CEN |
| `310-GSF` | PP-CEN |
| `320-UF` | BL-REGEN, PP-CEN, PP-CIP |
| `320-PUF` | PP-CEN, PP-CIP |
| `330-GAC` | V-FRP, PP-CEN |
| `330-IX` | V-FRP, PP-CEN |
| `340-DEG` | BL-REGEN, PP-CEN |
| `350-ROS` | 350-ROM, 350-ROV, PP-HP, PP-CIP |
| `401-CL` | PP-DIAP, MX-STATIC, TK-POLY |
| `401-O3` | 401-O3D |
| `420-UV` | 420-UVR |
| `501-MEE` | HX-ST, PP-CEN |
| `501-MVR` | 730-CMP, HX-ST, PP-CEN |
| `510-FC` | HX-ST, PP-CEN |
| `601-GT` | 601-TM, PP-PCP |
| `610-BFP` | PP-PCP |
| `610-CFG` | PP-PCP |
| `640-DIG` | 640-GH, MX-TOPENTRY, HX-ST, PP-PCP |
| `710-BIO` | PP-CEN, BL-REGEN |
| `740-MEM` | 730-CMP |

### File Structure

```yaml
package_template: 101-SC
package_name: Screening Package
components:
  - template_id: 101-SCR
    name: Screen
    service: PRELIMINARY SCREENING
    qty_rule: num_screens

  - template_id: 101-WC
    name: Washer-Compactor
    service: SCREENINGS PROCESSING
    qty_rule: conditional
    condition_field: washer_included
    condition_value: "Yes"

  - template_id: 101-CV
    name: Screw Conveyor
    service: SCREENINGS TRANSPORT
    qty_rule: fixed
    qty: 1
```

### Component Fields

| Field | Required | Description |
|-------|----------|-------------|
| `template_id` | Yes | Component template to use |
| `name` | Yes | Human-readable component name |
| `service` | Yes | Service description for component datasheet |
| `qty_rule` | Yes | Quantity calculation rule |
| `condition_field` | If conditional | Field to check for inclusion |
| `condition_value` | If conditional | Value that triggers inclusion |
| `qty` | If fixed | Fixed quantity value |

---

## Quantity Rules

### Single Field Reference

Reference a field_id directly from the package template:

```yaml
qty_rule: num_screens    # Value of 'num_screens' field in template
qty_rule: num_trains     # Value of 'num_trains' field
qty_rule: num_vessels    # Value of 'num_vessels' field
```

### Arithmetic Expressions

Simple arithmetic with field values:

```yaml
qty_rule: num_trains + 1           # Add 1 spare
qty_rule: num_vessels * 2          # Two per vessel
qty_rule: num_basins - 1           # One less than basins
```

### Combined Expressions

Multiple fields with arithmetic:

```yaml
qty_rule: num_basins * units_per_basin        # Multiply two fields
qty_rule: num_trains * pumps_per_train + 1    # Complex expression
qty_rule: (num_screens + 1) * 2               # Parentheses supported
```

### Fixed Quantity

Always include a fixed number:

```yaml
qty_rule: fixed
qty: 1                    # Always 1
qty: 2                    # Always 2
```

### Conditional Inclusion

Include only if condition is met:

```yaml
qty_rule: conditional
condition_field: washer_included    # field_id to check
condition_value: "Yes"              # Value that triggers inclusion

# Component included if template has washer_included = "Yes"
```

### Conditional with Quantity

Combine conditional with quantity:

```yaml
qty_rule: conditional
condition_field: conveyor_type
condition_value: "Screw"
qty: 2                              # If included, qty = 2
```

---

## Package Templates

Package templates define complete systems with multiple components. See [Package → Component Relationships](#package--component-relationships) for the full list.

**Key packages with existing BOM files:**

| Package | Description | Components |
|---------|-------------|------------|
| `101-SC` | Screening Package | Screens, washer-compactor, conveyors |
| `101-GR` | Grit Removal | Grit separator, grit washer, pumps |
| `130-CL` | Primary Clarifier | Mechanism, sludge pumps |
| `230-AT` | Aeration Tank | Blowers, diffusers, RAS pumps |
| `310-DMF` | Pressure Filter | Filter vessels, backwash pumps |
| `420-UV` | UV Disinfection | Reactor modules, cleaning system |
| `601-GT` | Gravity Thickener | Mechanism, underflow pumps |

**Additional packages (BOM files to be created as needed):**

| Package | Description | Components |
|---------|-------------|------------|
| `250-MBR` | Submerged MBR | Air scour blowers, permeate pumps |
| `280-SBR` | Sequencing Batch Reactor | Decanter, blowers, diffusers, mixers |
| `350-ROS` | RO Skid Package | Membranes, pressure vessels, HP pumps |
| `401-CL` | Chlorination System | Dosing pumps, static mixers, storage tank |
| `401-O3` | Ozone System | Generator, destruct unit |
| `501-MEE` | Multi-Effect Evaporator | Heat exchangers, circulation pumps |
| `640-DIG` | Anaerobic Digester | Gas holder, mixers, heat exchangers, feed pumps |

---

## Usage

### Generate BOM

```bash
# Console output
python scripts/generate_bom.py templates/101-SC.md

# CSV output
python scripts/generate_bom.py templates/101-SC.md --output bom.csv

# Verbose (show rule evaluation)
python scripts/generate_bom.py templates/101-SC.md --verbose
```

### Example Session

```bash
$ python scripts/generate_bom.py templates/101-SC.md

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

### Workflow Integration

1. **Fill package template** with design values:
   - `num_screens: 2`
   - `washer_included: Yes`

2. **Generate BOM** to see required components:
   ```bash
   python scripts/generate_bom.py templates/101-SC.md
   ```

3. **Create component datasheets** for each line item:
   - Copy `templates/101-SCR.md` for each screen
   - Fill with service-specific parameters
   - Generate Excel for each

4. **Issue complete package**:
   - Package datasheet (101-SC)
   - All component datasheets (101-SCR × 2, 101-WC × 1, 101-CV × 1)
