---
schema_version: 1
template_id: PP-CIP
title: CIP PUMP
service: CLEAN-IN-PLACE
has_motor: true
category: pumps
---

# CIP PUMP DATASHEET

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
| 2 | fluid | CIP Fluid | | | dropdown | ["Caustic Solution","Acid Solution","Hot Water","Chlorine Solution","Peroxide Solution","Mixed"] |
| 3 | concentration | Chemical Concentration | | % | number | |
| 4 | qdesign | Design Flow Rate | | m³/h | number | |
| 5 | qmin | Minimum Flow | | m³/h | number | |
| 6 | qmax | Maximum Flow | | m³/h | number | |
| 7 | num_duty | Number of Duty Pumps | | | number | |
| 8 | num_standby | Number of Standby Pumps | | | number | |
| 9 | tdh | Total Dynamic Head | | m | number | |
| 10 | discharge_pressure | Discharge Pressure | | bar | number | |
| 11 | npsha | NPSH Available | | m | number | |
| 12 | npshr | NPSH Required | | m | number | |
| 13 | temp | Fluid Temperature | | °C | number | |
| 14 | temp_max | Maximum Temperature | | °C | number | |
| 15 | ph_range | pH Range | | | text | |
| 16 | pump_type | Pump Type | | | dropdown | ["End Suction","Self-Priming","Vertical Inline"] |
| 17 | impeller_type | Impeller Type | | | dropdown | ["Closed","Semi-Open","Open"] |
| 18 | seal_type | Seal Type | | | dropdown | ["Mechanical Single","Mechanical Double","Magnetic Drive"] |
| 19 | seal_flush | Seal Flush | | | dropdown | ["None","External Flush","Quench","Double with Barrier"] |
| 20 | sanitary | Sanitary Design | | | dropdown | ["3A","EHEDG","FDA","None"] |
| 21 | suction_nozzle | Suction Nozzle Size | | mm | number | |
| 22 | discharge_nozzle | Discharge Nozzle Size | | mm | number | |
| 23 | connection_type | Connection Type | | | dropdown | ["Tri-Clamp","DIN","SMS","Flanged"] |
| 24 | speed | Operating Speed | | RPM | number | |
| 25 | shaft_power | Shaft Power at Design | | kW | number | |
| 26 | efficiency | Pump Efficiency (at BEP) | | % | number | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | casing | Pump Casing | |
| 2 | impeller | Impeller | |
| 3 | shaft | Shaft | |
| 4 | seals | Mechanical Seal | |
| 5 | elastomers | Elastomers/O-Rings | |
| 6 | fasteners | Fasteners | 316 SS |

## Driver / Motor Data

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | driver_type | Driver Type | | | dropdown | ["Electric Motor"] |
| 2 | vfd | VFD Required | | | dropdown | ["Yes","No"] |
| 3 | mfr | Manufacturer | | | text | |
| 4 | model | Model | | | text | |
| 5 | power | Rated Power | | kW | number | |
| 6 | electrical | Voltage / Phase / Hz | | V/Ph/Hz | text | |
| 7 | enclosure | Enclosure Type | | | dropdown | ["TEFC","Washdown","IP66","IP69K"] |
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
