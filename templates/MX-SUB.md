---
schema_version: 1
template_id: MX-SUB
title: SUBMERSIBLE MIXER
service: TANK MIXING
has_motor: true
category: mixers
---

# SUBMERSIBLE MIXER DATASHEET

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
| 1 | service_type | Service Type | | | dropdown | ["Anoxic Zone","Anaerobic Zone","Aeration Tank","Equalization","Sludge Holding","Chemical Tank"] |
| 2 | num_mixers | Number of Mixers per Tank | | | number | |
| 3 | tank_volume | Tank Volume | | m³ | number | |
| 4 | tank_diameter | Tank Diameter (if circular) | | m | number | |
| 5 | tank_length | Tank Length (if rectangular) | | m | number | |
| 6 | tank_width | Tank Width (if rectangular) | | m | number | |
| 7 | liquid_depth | Liquid Depth | | m | number | |
| 8 | fluid | Mixed Fluid | | | dropdown | ["Mixed Liquor","RAS","Sludge","Chemical Solution","Raw Sewage"] |
| 9 | sg | Specific Gravity | | | number | |
| 10 | solids | Solids Content | | mg/L | number | |
| 11 | temp | Fluid Temperature | | °C | number | |
| 12 | thrust | Thrust Required (per mixer) | | N | number | |
| 13 | velocity | Target Velocity | | m/s | number | |
| 14 | power_density | Power Density (W/m³) | | W/m³ | number | |
| 15 | impeller_dia | Propeller Diameter | | mm | number | |
| 16 | impeller_type | Propeller Type | | | dropdown | ["Banana Blade","Hydrofoil","Marine","Turbine"] |
| 17 | speed | Operating Speed | | RPM | number | |
| 18 | mounting | Mounting Type | | | dropdown | ["Floor Stand","Guide Rail","Pedestal","Floating"] |
| 19 | tilt_angle | Tilt Angle from Vertical | | degrees | number | |
| 20 | orientation | Orientation | | | dropdown | ["Horizontal","Vertical","Angled"] |
| 21 | cable_length | Cable Length | | m | number | |
| 22 | shaft_power | Shaft Power | | kW | number | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | motor_housing | Motor Housing | |
| 2 | propeller | Propeller | |
| 3 | shaft | Shaft | |
| 4 | seals | Mechanical Seals | |
| 5 | mat_mounting | Mounting Bracket | |
| 6 | guide_rail | Guide Rail (if applicable) | |
| 7 | fasteners | Fasteners | 316 SS |

## Driver / Motor Data

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | driver_type | Driver Type | | | dropdown | ["Submersible Motor","Dry Motor"] |
| 2 | vfd | VFD Required | | | dropdown | ["Yes","No"] |
| 3 | mfr | Manufacturer | | | text | |
| 4 | model | Model | | | text | |
| 5 | power | Rated Power | | kW | number | |
| 6 | electrical | Voltage / Phase / Hz | | V/Ph/Hz | text | |
| 7 | enclosure | Motor Protection | | | dropdown | ["IP68","Submersible Rated"] |
| 8 | rpm | Full Load RPM | | RPM | number | |
| 9 | insulation | Insulation Class | | | dropdown | ["F","H"] |
| 10 | cooling | Motor Cooling | | | dropdown | ["Fluid Cooled","Oil Filled"] |

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
