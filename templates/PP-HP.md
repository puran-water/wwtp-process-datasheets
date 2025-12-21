---
schema_version: 1
template_id: PP-HP
title: HIGH PRESSURE PUMP
service: RO/NF FEED
has_motor: true
category: pumps
---

# HIGH PRESSURE PUMP DATASHEET

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
| 1 | service | Service Description | | | text | |
| 2 | fluid | Pumped Fluid | | | dropdown | ["RO Feed","NF Feed","UF Feed","Concentrate Recycle","Booster","High Pressure Wash"] |
| 3 | qdesign | Design Flow Rate | | m³/h | number | |
| 4 | qmin | Minimum Flow | | m³/h | number | |
| 5 | qmax | Maximum Flow | | m³/h | number | |
| 6 | num_duty | Number of Duty Pumps | | | number | |
| 7 | num_standby | Number of Standby Pumps | | | number | |
| 8 | suction_pressure | Suction Pressure | | bar | number | |
| 9 | discharge_pressure | Discharge Pressure | | bar | number | |
| 10 | diff_pressure | Differential Pressure | | bar | number | |
| 11 | npsha | NPSH Available | | m | number | |
| 12 | npshr | NPSH Required | | m | number | |
| 13 | sg | Specific Gravity | | | number | |
| 14 | temp | Fluid Temperature | | °C | number | |
| 15 | tds | Total Dissolved Solids | | mg/L | number | |
| 16 | sdi | SDI (Silt Density Index) | | | number | |
| 17 | ph | pH Range | | | text | |
| 18 | pump_type | Pump Type | | | dropdown | ["Multi-Stage Centrifugal","Positive Displacement","Axial Piston","Radial Piston"] |
| 19 | stages | Number of Stages | | | number | |
| 20 | impeller_type | Impeller Type | | | dropdown | ["Closed","Semi-Open"] |
| 21 | seal_type | Seal Type | | | dropdown | ["Mechanical Single","Mechanical Double","Cartridge"] |
| 22 | seal_flush | Seal Flush | | | dropdown | ["API Plan 11","API Plan 13","API Plan 21","API Plan 32","API Plan 53"] |
| 23 | suction_nozzle | Suction Nozzle Size | | mm | number | |
| 24 | discharge_nozzle | Discharge Nozzle Size | | mm | number | |
| 25 | nozzle_rating | Nozzle Flange Rating | | | dropdown | ["PN25","PN40","PN63","300#","600#"] |
| 26 | speed | Operating Speed | | RPM | number | |
| 27 | shaft_power | Shaft Power at Design | | kW | number | |
| 28 | efficiency | Pump Efficiency (at BEP) | | % | number | |
| 29 | min_flow | Minimum Continuous Flow | | m³/h | number | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | casing | Pump Casing | |
| 2 | impellers | Impellers | |
| 3 | shaft | Shaft | |
| 4 | wear_rings | Wear Rings | |
| 5 | seals | Mechanical Seal | |
| 6 | diffusers | Diffusers | |
| 7 | fasteners | Fasteners | 316 SS |

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
