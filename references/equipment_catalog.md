# Equipment Catalog

Complete template inventory for WWTP process datasheets.

## Table of Contents

- [Process Areas](#process-areas)
- [Universal Components](#universal-components)
- [Template → Asset Mapping](#template--asset-mapping)
- [Package vs Component](#package-vs-component)

---

## Process Areas

### Headworks (Area 101)

| Template | Equipment | Description |
|----------|-----------|-------------|
| `101-SC` | Screening Package | Complete screening system (screens + handling) |
| `101-GR` | Grit Removal Package | Complete grit system (removal + handling) |
| `101-SCR` | Screen | Standalone bar/fine screen unit |
| `101-WC` | Washer-Compactor | Screenings washing and compaction |
| `101-CV` | Screw Conveyor | Screenings/grit transport |
| `101-GW` | Grit Washer | Grit cleaning and classification |

### Primary Treatment (Area 130)

| Template | Equipment | Description |
|----------|-----------|-------------|
| `130-CL` | Primary Clarifier | Circular/rectangular sedimentation tank |
| `130-LC` | Lamella Clarifier | Inclined plate settler (distinct from conventional) |
| `130-CM` | Clarifier Mechanism | Primary scraper/rake drive |

### Secondary Treatment (Areas 230, 240)

| Template | Equipment | Description |
|----------|-----------|-------------|
| `230-AT` | Aeration Tank | Basin + diffuser + blower system |
| `230-BL` | Blower Package | Aeration air supply |
| `230-DF` | Diffuser Grid | Fine bubble diffuser assembly |
| `240-SC` | Secondary Clarifier | Final clarifier for activated sludge |
| `240-CM` | Clarifier Mechanism | Secondary scraper/rake drive |

### Tertiary Treatment (Areas 310, 420)

| Template | Equipment | Description |
|----------|-----------|-------------|
| `310-DMF` | Pressure Filter | Dual media / pressure filtration system |
| `310-FV` | Filter Vessel | Individual filter vessel internals |
| `420-UV` | UV Disinfection | Open channel or closed vessel UV system |
| `420-UVR` | UV Reactor Module | Individual lamp bank + cleaning |

### Solids Handling (Area 601)

| Template | Equipment | Description |
|----------|-----------|-------------|
| `601-GT` | Gravity Thickener | Sludge thickening tank |
| `601-TM` | Thickener Mechanism | Thickener rake drive |

---

## Universal Components

These components are used across multiple process areas and are procured separately from package equipment:

| Component | Template | Typical Services |
|-----------|----------|------------------|
| Centrifugal Pump | `600-PP-CEN` | RAS/WAS, transfer, chemical feed |
| Progressive Cavity Pump | `600-PP-PCP` | Sludge transfer, polymer, high-solids |
| Submersible Pump | `600-PP-SUB` | Wet wells, sumps, lift stations |
| Blower Package | `230-BL` | Aeration air supply |
| Diffuser Grid | `230-DF` | Fine bubble aeration |
| Clarifier Mechanism | `130-CM`, `240-CM` | Scraper/rake drives |
| Thickener Mechanism | `601-TM` | Rake drives for thickeners |
| UV Reactor Module | `420-UVR` | Lamp banks + cleaning |
| Filter Vessel | `310-FV` | Tertiary filter internals |
| Screen | `101-SCR` | Standalone screening units |
| Washer-Compactor | `101-WC` | Screenings processing |
| Screw Conveyor | `101-CV` | Screenings/grit transport |
| Grit Washer | `101-GW` | Grit cleaning/classification |

---

## Template → Asset Mapping

| Template | Generated Excel |
|----------|-----------------|
| `templates/000-PROJECT-DATA.md` | `assets/000-PROJECT-DATA-01 PROJECT DATA.xlsx` |
| `templates/101-SC.md` | `assets/101-SC-01 SCREENING PACKAGE.xlsx` |
| `templates/101-GR.md` | `assets/101-GR-01 GRIT REMOVAL PACKAGE.xlsx` |
| `templates/101-SCR.md` | `assets/101-SCR-01 SCREEN.xlsx` |
| `templates/101-WC.md` | `assets/101-WC-01 WASHER-COMPACTOR.xlsx` |
| `templates/101-CV.md` | `assets/101-CV-01 SCREW CONVEYOR.xlsx` |
| `templates/101-GW.md` | `assets/101-GW-01 GRIT WASHER.xlsx` |
| `templates/130-CL.md` | `assets/130-CL-01 PRIMARY CLARIFIER.xlsx` |
| `templates/130-LC.md` | `assets/130-LC-01 LAMELLA CLARIFIER.xlsx` |
| `templates/130-CM.md` | `assets/130-CM-01 CLARIFIER MECHANISM.xlsx` |
| `templates/230-AT.md` | `assets/230-AT-01 AERATION TANK.xlsx` |
| `templates/230-BL.md` | `assets/230-BL-01 BLOWER PACKAGE.xlsx` |
| `templates/230-DF.md` | `assets/230-DF-01 DIFFUSER GRID.xlsx` |
| `templates/240-SC.md` | `assets/240-SC-01 SECONDARY CLARIFIER.xlsx` |
| `templates/240-CM.md` | `assets/240-CM-01 CLARIFIER MECHANISM.xlsx` |
| `templates/310-DMF.md` | `assets/310-DMF-01 PRESSURE FILTER.xlsx` |
| `templates/310-FV.md` | `assets/310-FV-01 FILTER VESSEL.xlsx` |
| `templates/420-UV.md` | `assets/420-UV-01 UV DISINFECTION.xlsx` |
| `templates/420-UVR.md` | `assets/420-UVR-01 UV REACTOR MODULE.xlsx` |
| `templates/601-GT.md` | `assets/601-GT-01 GRAVITY THICKENER.xlsx` |
| `templates/601-TM.md` | `assets/601-TM-01 THICKENER MECHANISM.xlsx` |
| `templates/600-PP-CEN.md` | `assets/600-PP-CEN-01 CENTRIFUGAL PUMP.xlsx` |
| `templates/600-PP-PCP.md` | `assets/600-PP-PCP-01 PROGRESSIVE CAVITY PUMP.xlsx` |
| `templates/600-PP-SUB.md` | `assets/600-PP-SUB-01 SUBMERSIBLE PUMP.xlsx` |

---

## Package vs Component

**Package templates** define complete systems that include multiple components:
- `101-SC` (Screening Package) → screens + washer-compactor + conveyors
- `101-GR` (Grit Removal Package) → grit chamber + washer + pumps
- `230-AT` (Aeration Tank) → basin + blowers + diffusers
- `310-DMF` (Pressure Filter) → vessels + media + controls
- `420-UV` (UV Disinfection) → reactors + lamps + controls
- `601-GT` (Gravity Thickener) → tank + mechanism

**Component templates** define individual equipment items:
- `101-SCR`, `101-WC`, `101-CV`, `101-GW` (headworks components)
- `230-BL`, `230-DF` (aeration components)
- `130-CM`, `240-CM`, `601-TM` (mechanism components)
- `310-FV`, `420-UVR` (tertiary components)
- `600-PP-*` (pumps)

Use `scripts/generate_bom.py` to expand a package template into its component datasheets.
