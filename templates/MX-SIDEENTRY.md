---
schema_version: 1
template_id: MX-SIDEENTRY
title: SIDE-ENTRY MIXER
service: TANK MIXING
has_motor: true
category: mixers
---

# SIDE-ENTRY MIXER DATASHEET

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
| Service | |
| Location | |
| Manufacturer | |
| Model | |
| P&ID No | |

## Operating / Design Data

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | service_type | Service Type | | | dropdown | ["Large Storage Tank","Blending","Suspension","Chemical Preparation"] |
| 2 | num_mixers | Number of Mixers per Tank | | | number | |
| 3 | tank_volume | Tank Volume | | m³ | number | |
| 4 | tank_diameter | Tank Diameter | | m | number | |
| 5 | liquid_depth | Liquid Depth | | m | number | |
| 6 | fluid | Mixed Fluid | | | dropdown | ["Water","Sludge","Chemical Solution","Slurry","Process Liquid"] |
| 7 | sg | Specific Gravity | | | number | |
| 8 | viscosity | Viscosity | | cP | number | |
| 9 | solids | Solids Content | | % | number | |
| 10 | temp | Fluid Temperature | | °C | number | |
| 11 | impeller_type | Impeller Type | | | dropdown | ["Marine Propeller","Hydrofoil","Pitched Blade"] |
| 12 | impeller_dia | Impeller Diameter | | mm | number | |
| 13 | entry_angle | Entry Angle | | degrees | number | |
| 14 | elevation | Nozzle Elevation from Tank Bottom | | mm | number | |
| 15 | insertion_length | Insertion Length | | mm | number | |
| 16 | speed | Operating Speed | | RPM | number | |
| 17 | shaft_seal | Shaft Seal Type | | | dropdown | ["Mechanical Seal - Single","Mechanical Seal - Double","Stuffing Box"] |
| 18 | seal_flush | Seal Flush | | | dropdown | ["None","External Flush","Barrier Fluid"] |
| 19 | mounting | Mounting Nozzle Size | | mm | number | |
| 20 | nozzle_rating | Nozzle Flange Rating | | | dropdown | ["PN10","PN16","PN25","150#","300#"] |
| 21 | gearbox | Gearbox Type | | | dropdown | ["Helical","Planetary","Direct Drive"] |
| 22 | shaft_power | Shaft Power | | kW | number | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | shaft | Shaft | |
| 2 | impeller | Impeller | |
| 3 | housing | Seal Housing | |
| 4 | seals | Mechanical Seal | |
| 5 | nozzle | Tank Nozzle | |
| 6 | fasteners | Fasteners | 316 SS |

## Driver / Motor Data

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | driver_type | Driver Type | | | dropdown | ["Electric Motor","Hydraulic"] |
| 2 | vfd | VFD Required | | | dropdown | ["Yes","No"] |
| 3 | mfr | Manufacturer | | | text | |
| 4 | model | Model | | | text | |
| 5 | power | Rated Power | | kW | number | |
| 6 | electrical | Voltage / Phase / Hz | | V/Ph/Hz | text | |
| 7 | enclosure | Enclosure Type | | | dropdown | ["TEFC","ODP","TENV","Explosion Proof"] |
| 8 | rpm | Full Load RPM | | RPM | number | |
| 9 | sf | Service Factor | | | number | |
| 10 | starting | Starting Method | | | dropdown | ["DOL","Soft Start","VFD"] |
| 11 | insulation | Insulation Class | | | dropdown | ["B","F","H"] |
| 12 | efficiency_class | Efficiency Class | | | dropdown | ["IE1","IE2","IE3","IE4"] |

## Remarks

| # | Remark |
|---|--------|
| 1 | |
| 2 | |
| 3 | |

## Revision History

| Rev | Date | Description | By |
|-----|------|-------------|-----|
| 0 | | Initial release | |
| 1 | | | |
| 2 | | | |
