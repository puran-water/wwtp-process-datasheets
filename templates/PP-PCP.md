---
schema_version: 1
template_id: PP-PCP
title: PROGRESSIVE CAVITY PUMP
service: SLUDGE PUMPING
has_motor: true
category: pumps
---

# PROGRESSIVE CAVITY PUMP DATASHEET

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
| 2 | fluid | Pumped Fluid | | | dropdown | ["Primary Sludge","WAS","Thickened Sludge","Digested Sludge","Dewatered Cake","Polymer","Grease","Scum"] |
| 3 | qdesign | Design Flow Rate | | m³/h | number | |
| 4 | qmin | Minimum Flow | | m³/h | number | |
| 5 | qmax | Maximum Flow | | m³/h | number | |
| 6 | num_duty | Number of Duty Pumps | | | number | |
| 7 | num_standby | Number of Standby Pumps | | | number | |
| 8 | discharge_pressure | Discharge Pressure | | bar | number | |
| 9 | suction_pressure | Suction Pressure | | bar | number | |
| 10 | npsha | NPSH Available | | m | number | |
| 11 | npshr | NPSH Required | | m | number | |
| 12 | sg | Specific Gravity | | | number | |
| 13 | temp | Fluid Temperature | | °C | number | |
| 14 | solids | Solids Content | | % | number | |
| 15 | max_particle | Maximum Particle Size | | mm | number | |
| 16 | viscosity | Viscosity | | cP | number | |
| 17 | abrasive | Abrasive Content | | | dropdown | ["Low","Medium","High"] |
| 18 | stages | Number of Stages | | | dropdown | ["1","2","3","4"] |
| 19 | rotor_coating | Rotor Coating | | | dropdown | ["Chrome","Ceramic","None"] |
| 20 | stator_material | Stator Elastomer | | | dropdown | ["NBR","EPDM","FKM/Viton","Natural Rubber"] |
| 21 | hopper | Hopper/Bridge Breaker | | | dropdown | ["None","Standard Hopper","Auger Feed","Bridge Breaker"] |
| 22 | suction_nozzle | Suction Nozzle Size | | mm | number | |
| 23 | discharge_nozzle | Discharge Nozzle Size | | mm | number | |
| 24 | nozzle_rating | Nozzle Flange Rating | | | dropdown | ["PN10","PN16","PN25","150#","300#"] |
| 25 | speed | Operating Speed | | RPM | number | |
| 26 | shaft_power | Shaft Power at Design | | kW | number | |
| 27 | turndown | Turndown Ratio | | | text | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | casing | Pump Casing | |
| 2 | rotor | Rotor | |
| 3 | stator | Stator | |
| 4 | shaft | Drive Shaft | |
| 5 | coupling | Coupling Rod | |
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
