---
schema_version: 1
template_id: PP-VERT
title: VERTICAL TURBINE PUMP
service: HIGH FLOW PUMPING
has_motor: true
category: pumps
---

# VERTICAL TURBINE PUMP DATASHEET

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
| 2 | fluid | Pumped Fluid | | | dropdown | ["Raw Water","Treated Water","Effluent","Cooling Water","Fire Water","Process Water"] |
| 3 | qdesign | Design Flow Rate | | m³/h | number | |
| 4 | qmin | Minimum Flow | | m³/h | number | |
| 5 | qmax | Maximum Flow | | m³/h | number | |
| 6 | num_duty | Number of Duty Pumps | | | number | |
| 7 | num_standby | Number of Standby Pumps | | | number | |
| 8 | tdh | Total Dynamic Head | | m | number | |
| 9 | static_suction | Static Suction Lift | | m | number | |
| 10 | static_discharge | Static Discharge Head | | m | number | |
| 11 | submergence | Minimum Submergence | | m | number | |
| 12 | setting | Bowl Setting Depth | | m | number | |
| 13 | sg | Specific Gravity | | | number | |
| 14 | temp | Fluid Temperature | | °C | number | |
| 15 | solids | Solids Content | | mg/L | number | |
| 16 | stages | Number of Stages | | | number | |
| 17 | bowl_dia | Bowl Diameter | | mm | number | |
| 18 | column_dia | Column Pipe Diameter | | mm | number | |
| 19 | column_length | Column Pipe Length | | m | number | |
| 20 | shaft_type | Line Shaft Type | | | dropdown | ["Open","Enclosed","Submersible Motor"] |
| 21 | lubrication | Shaft Lubrication | | | dropdown | ["Product Lubricated","Oil Lubricated"] |
| 22 | thrust_bearing | Thrust Bearing Location | | | dropdown | ["Above Grade","Below Grade"] |
| 23 | discharge_head | Discharge Head Type | | | dropdown | ["Above Grade","Below Grade","Can Type"] |
| 24 | discharge_nozzle | Discharge Nozzle Size | | mm | number | |
| 25 | nozzle_rating | Discharge Flange Rating | | | dropdown | ["PN10","PN16","PN25","150#","300#"] |
| 26 | shaft_power | Shaft Power at Design | | kW | number | |
| 27 | efficiency | Pump Efficiency (at BEP) | | % | number | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | bowls | Pump Bowls | |
| 2 | impellers | Impellers | |
| 3 | shaft | Line Shaft | |
| 4 | column | Column Pipe | |
| 5 | bearings | Bowl Bearings | |
| 6 | mat_discharge_head | Discharge Head | |
| 7 | fasteners | Fasteners | 316 SS |

## Driver / Motor Data

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | driver_type | Driver Type | | | dropdown | ["Hollow Shaft Motor","Solid Shaft Motor","Submersible Motor","Engine"] |
| 2 | vfd | VFD Required | | | dropdown | ["Yes","No"] |
| 3 | mfr | Manufacturer | | | text | |
| 4 | model | Model | | | text | |
| 5 | power | Rated Power | | kW | number | |
| 6 | electrical | Voltage / Phase / Hz | | V/Ph/Hz | text | |
| 7 | enclosure | Enclosure Type | | | dropdown | ["TEFC","ODP","TENV","WP-I","WP-II"] |
| 8 | rpm | Full Load RPM | | RPM | number | |
| 9 | sf | Service Factor | | | number | |
| 10 | starting | Starting Method | | | dropdown | ["DOL","Soft Start","VFD","Reduced Voltage"] |
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
