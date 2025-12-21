---
schema_version: 1
template_id: PP-GEAR
title: GEAR PUMP
service: CHEMICAL/OIL TRANSFER
has_motor: true
category: pumps
---

# GEAR PUMP DATASHEET

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
| 2 | fluid | Pumped Fluid | | | dropdown | ["Polymer","Oil","Fuel","Lubricant","Chemical","Viscous Liquid"] |
| 3 | qdesign | Design Flow Rate | | L/h | number | |
| 4 | qmin | Minimum Flow | | L/h | number | |
| 5 | qmax | Maximum Flow | | L/h | number | |
| 6 | num_duty | Number of Duty Pumps | | | number | |
| 7 | num_standby | Number of Standby Pumps | | | number | |
| 8 | discharge_pressure | Discharge Pressure | | bar | number | |
| 9 | suction_pressure | Suction Pressure | | bar | number | |
| 10 | diff_pressure | Differential Pressure | | bar | number | |
| 11 | npsha | NPSH Available | | m | number | |
| 12 | npshr | NPSH Required | | m | number | |
| 13 | sg | Specific Gravity | | | number | |
| 14 | temp | Fluid Temperature | | °C | number | |
| 15 | temp_max | Maximum Temperature | | °C | number | |
| 16 | viscosity_min | Minimum Viscosity | | cP | number | |
| 17 | viscosity_max | Maximum Viscosity | | cP | number | |
| 18 | gear_type | Gear Type | | | dropdown | ["External Spur","Internal Crescent","Helical"] |
| 19 | relief_valve | Relief Valve | | | dropdown | ["Internal","External","None"] |
| 20 | seal_type | Seal Type | | | dropdown | ["Lip Seal","Mechanical Single","Mechanical Double","Magnetic Drive"] |
| 21 | suction_nozzle | Suction Port Size | | mm | number | |
| 22 | discharge_nozzle | Discharge Port Size | | mm | number | |
| 23 | connection_type | Connection Type | | | dropdown | ["Threaded NPT","Threaded BSP","Flanged","Tri-Clamp"] |
| 24 | speed | Operating Speed | | RPM | number | |
| 25 | shaft_power | Shaft Power at Design | | kW | number | |
| 26 | efficiency | Volumetric Efficiency | | % | number | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | body | Pump Body | |
| 2 | gears | Gears | |
| 3 | shaft | Shaft | |
| 4 | bearings | Bearings | |
| 5 | seals | Seals | |
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
