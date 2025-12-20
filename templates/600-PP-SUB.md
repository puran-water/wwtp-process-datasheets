---
schema_version: 1
template_id: 600-PP-SUB
title: SUBMERSIBLE PUMP
service: WET WELL PUMPING
has_motor: true
category: pumps
---

# SUBMERSIBLE PUMP DATASHEET

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
| 2 | fluid | Pumped Fluid | | | dropdown | ["Raw Sewage","Stormwater","Combined Sewage","Sludge","Scum","Industrial Wastewater"] |
| 3 | qdesign | Design Flow Rate | | m³/h | number | |
| 4 | qmin | Minimum Flow | | m³/h | number | |
| 5 | qmax | Maximum Flow | | m³/h | number | |
| 6 | num_duty | Number of Duty Pumps | | | number | |
| 7 | num_standby | Number of Standby Pumps | | | number | |
| 8 | tdh | Total Dynamic Head | | m | number | |
| 9 | static_head | Static Discharge Head | | m | number | |
| 10 | friction_head | Friction Head Loss | | m | number | |
| 11 | submergence | Minimum Submergence | | m | number | |
| 12 | sg | Specific Gravity | | | number | |
| 13 | temp | Fluid Temperature | | °C | number | |
| 14 | solids | Solids Content | | % | number | |
| 15 | free_passage | Free Passage (sphere) | | mm | number | |
| 16 | impeller_type | Impeller Type | | | dropdown | ["Vortex","Channel","Semi-Open","Grinder"] |
| 17 | discharge_nozzle | Discharge Nozzle Size | | mm | number | |
| 18 | nozzle_rating | Discharge Flange Rating | | | dropdown | ["PN10","PN16","PN25","150#","300#"] |
| 19 | shaft_power | Shaft Power at Design | | kW | number | |
| 20 | efficiency | Pump Efficiency (at BEP) | | % | number | |
| 21 | cooling | Motor Cooling | | | dropdown | ["Fluid Cooled","Oil Filled","Air Filled"] |
| 22 | cable_length | Cable Length | | m | number | |
| 23 | guide_rail | Guide Rail System | | | dropdown | ["Yes","No"] |
| 24 | auto_coupling | Automatic Coupling | | | dropdown | ["Yes","No"] |
| 25 | lifting | Lifting Chain/Cable | | | dropdown | ["Stainless Chain","Galvanized Cable","Stainless Cable"] |
| 26 | level_control | Level Control | | | dropdown | ["Float Switches","Ultrasonic","Pressure Transducer"] |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | casing | Pump Casing | |
| 2 | impeller | Impeller | |
| 3 | motor_housing | Motor Housing | |
| 4 | shaft | Shaft | |
| 5 | seals | Mechanical Seals | |
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
