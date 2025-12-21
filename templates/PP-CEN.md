---
schema_version: 1
template_id: PP-CEN
title: CENTRIFUGAL PUMP
service: PUMPING
has_motor: true
category: pumps
---

# CENTRIFUGAL PUMP DATASHEET

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
| 2 | fluid | Pumped Fluid | | | dropdown | ["Raw Sewage","Primary Effluent","Secondary Effluent","RAS","WAS","Thickened Sludge","Digested Sludge","Filtrate","Washwater","Chemical"] |
| 3 | qdesign | Design Flow Rate | | m³/h | number | |
| 4 | qmin | Minimum Flow | | m³/h | number | |
| 5 | qmax | Maximum Flow | | m³/h | number | |
| 6 | num_duty | Number of Duty Pumps | | | number | |
| 7 | num_standby | Number of Standby Pumps | | | number | |
| 8 | tdh | Total Dynamic Head | | m | number | |
| 9 | suction_head | Suction Head (static) | | m | number | |
| 10 | discharge_head | Discharge Head (static) | | m | number | |
| 11 | npsha | NPSH Available | | m | number | |
| 12 | npshr | NPSH Required | | m | number | |
| 13 | sg | Specific Gravity | | | number | |
| 14 | temp | Fluid Temperature | | °C | number | |
| 15 | solids | Solids Content | | % | number | |
| 16 | max_particle | Maximum Particle Size | | mm | number | |
| 17 | viscosity | Viscosity (if non-Newtonian) | | cP | number | |
| 18 | pump_type | Pump Type | | | dropdown | ["End Suction","Vertical Inline","Split Case","Vertical Turbine","Self-Priming"] |
| 19 | mounting | Mounting | | | dropdown | ["Horizontal","Vertical","Submersible"] |
| 20 | op.impeller | Impeller Type | | | dropdown | ["Closed","Semi-Open","Recessed","Vortex","Non-Clog"] |
| 21 | seal_type | Seal Type | | | dropdown | ["Mechanical Single","Mechanical Double","Packing","Magnetic Drive"] |
| 22 | suction_nozzle | Suction Nozzle Size | | mm | number | |
| 23 | discharge_nozzle | Discharge Nozzle Size | | mm | number | |
| 24 | nozzle_rating | Nozzle Flange Rating | | | dropdown | ["PN10","PN16","PN25","150#","300#"] |
| 25 | speed | Operating Speed | | RPM | number | |
| 26 | shaft_power | Shaft Power at Design | | kW | number | |
| 27 | efficiency | Pump Efficiency (at BEP) | | % | number | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | casing | Pump Casing | |
| 2 | mat.impeller | Impeller | |
| 3 | shaft | Shaft | |
| 4 | wear_rings | Wear Rings | |
| 5 | seal | Mechanical Seal Faces | |
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
