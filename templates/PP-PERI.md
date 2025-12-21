---
schema_version: 1
template_id: PP-PERI
title: PERISTALTIC PUMP
service: CHEMICAL/SLUDGE DOSING
has_motor: true
category: pumps
---

# PERISTALTIC PUMP DATASHEET

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
| 2 | fluid | Pumped Fluid | | | dropdown | ["Polymer","Lime Slurry","Sludge","Abrasive Slurry","Chemical","Viscous Liquid","Shear-Sensitive"] |
| 3 | qdesign | Design Flow Rate | | L/h | number | |
| 4 | qmin | Minimum Flow | | L/h | number | |
| 5 | qmax | Maximum Flow | | L/h | number | |
| 6 | num_duty | Number of Duty Pumps | | | number | |
| 7 | num_standby | Number of Standby Pumps | | | number | |
| 8 | discharge_pressure | Maximum Discharge Pressure | | bar | number | |
| 9 | suction_lift | Maximum Suction Lift | | m | number | |
| 10 | sg | Specific Gravity | | | number | |
| 11 | temp | Fluid Temperature | | °C | number | |
| 12 | solids | Solids Content | | % | number | |
| 13 | viscosity | Viscosity | | cP | number | |
| 14 | abrasive | Abrasive Content | | | dropdown | ["Low","Medium","High"] |
| 15 | pump_size | Pump Size Class | | | dropdown | ["Tube","Industrial Hose"] |
| 16 | hose_id | Hose/Tube ID | | mm | number | |
| 17 | hose_material | Hose/Tube Material | | | dropdown | ["Natural Rubber","EPDM","NBR","Hypalon","Silicone","Norprene","Marprene"] |
| 18 | rotor_type | Rotor Type | | | dropdown | ["2-Roller","3-Roller","Shoe"] |
| 19 | occlusion | Occlusion Adjustment | | | dropdown | ["Fixed","Manual","Automatic"] |
| 20 | suction_port | Suction Port Size | | mm | number | |
| 21 | discharge_port | Discharge Port Size | | mm | number | |
| 22 | connection_type | Connection Type | | | dropdown | ["Hose Barb","Flanged","Tri-Clamp","Cam-Lock"] |
| 23 | speed | Operating Speed | | RPM | number | |
| 24 | hose_life | Expected Hose Life | | hours | number | |
| 25 | dry_run | Dry Run Capable | | | dropdown | ["Yes","No"] |
| 26 | reversible | Reversible Flow | | | dropdown | ["Yes","No"] |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | casing | Pump Casing | |
| 2 | hose | Hose/Tube | |
| 3 | rotor | Rotor | |
| 4 | rollers | Rollers | |
| 5 | connectors | End Connectors | |
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
