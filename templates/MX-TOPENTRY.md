---
schema_version: 1
template_id: MX-TOPENTRY
title: TOP-ENTRY MIXER
service: TANK MIXING
has_motor: true
category: mixers
---

# TOP-ENTRY MIXER DATASHEET

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
| 1 | service_type | Service Type | | | dropdown | ["Chemical Preparation","Flocculation","Digester","Storage Tank","Process Reactor"] |
| 2 | num_mixers | Number of Mixers per Tank | | | number | |
| 3 | tank_volume | Tank Volume | | m³ | number | |
| 4 | tank_diameter | Tank Diameter | | m | number | |
| 5 | liquid_depth | Liquid Depth | | m | number | |
| 6 | fluid | Mixed Fluid | | | dropdown | ["Sludge","Polymer","Chemical Solution","Slurry","Process Liquid"] |
| 7 | sg | Specific Gravity | | | number | |
| 8 | viscosity | Viscosity | | cP | number | |
| 9 | solids | Solids Content | | % | number | |
| 10 | temp | Fluid Temperature | | °C | number | |
| 11 | temp_max | Maximum Temperature | | °C | number | |
| 12 | impeller_type | Impeller Type | | | dropdown | ["Pitched Blade Turbine","Rushton Turbine","Hydrofoil","Anchor","Helical Ribbon"] |
| 13 | num_impellers | Number of Impellers | | | number | |
| 14 | impeller_dia | Impeller Diameter | | mm | number | |
| 15 | tip_speed | Tip Speed | | m/s | number | |
| 16 | speed | Operating Speed | | RPM | number | |
| 17 | shaft_length | Shaft Length | | mm | number | |
| 18 | shaft_seal | Shaft Seal Type | | | dropdown | ["Mechanical Seal","Stuffing Box","Magnetic Drive","Lip Seal"] |
| 19 | steady_bearing | Steady Bearing | | | dropdown | ["Yes","No"] |
| 20 | mounting | Mounting Type | | | dropdown | ["Tank Flange","Bridge Mounted","Portable"] |
| 21 | gearbox | Gearbox Type | | | dropdown | ["Helical","Planetary","Direct Drive"] |
| 22 | shaft_power | Shaft Power | | kW | number | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | shaft | Shaft | |
| 2 | impellers | Impellers | |
| 3 | tank_flange | Tank Flange | |
| 4 | seals | Seals | |
| 5 | bearings | Bearings | |
| 6 | fasteners | Fasteners | 316 SS |

## Driver / Motor Data

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | driver_type | Driver Type | | | dropdown | ["Electric Motor","Hydraulic","Pneumatic"] |
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
