---
schema_version: 1
template_id: PP-LOBE
title: ROTARY LOBE PUMP
service: SLUDGE PUMPING
has_motor: true
category: pumps
---

# ROTARY LOBE PUMP DATASHEET

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
| 2 | fluid | Pumped Fluid | | | dropdown | ["Primary Sludge","WAS","Thickened Sludge","Digested Sludge","Dewatered Cake","Polymer","Grease","Scum","Chemical Slurry"] |
| 3 | qdesign | Design Flow Rate | | m³/h | number | |
| 4 | qmin | Minimum Flow | | m³/h | number | |
| 5 | qmax | Maximum Flow | | m³/h | number | |
| 6 | num_duty | Number of Duty Pumps | | | number | |
| 7 | num_standby | Number of Standby Pumps | | | number | |
| 8 | discharge_pressure | Discharge Pressure | | bar | number | |
| 9 | suction_pressure | Suction Pressure | | bar | number | |
| 10 | diff_pressure | Differential Pressure | | bar | number | |
| 11 | npsha | NPSH Available | | m | number | |
| 12 | npshr | NPSH Required | | m | number | |
| 13 | sg | Specific Gravity | | | number | |
| 14 | temp | Fluid Temperature | | °C | number | |
| 15 | solids | Solids Content | | % | number | |
| 16 | max_particle | Maximum Particle Size | | mm | number | |
| 17 | viscosity | Viscosity | | cP | number | |
| 18 | abrasive | Abrasive Content | | | dropdown | ["Low","Medium","High"] |
| 19 | lobe_config | Lobe Configuration | | | dropdown | ["Bi-Lobe","Tri-Lobe","Multi-Lobe"] |
| 20 | lobe_coating | Lobe Coating | | | dropdown | ["Rubber Covered","Metal","Polyurethane"] |
| 21 | timing | Timing Gears | | | dropdown | ["External","Internal"] |
| 22 | cip_capable | CIP Capable | | | dropdown | ["Yes","No"] |
| 23 | suction_nozzle | Suction Nozzle Size | | mm | number | |
| 24 | discharge_nozzle | Discharge Nozzle Size | | mm | number | |
| 25 | nozzle_rating | Nozzle Flange Rating | | | dropdown | ["PN10","PN16","PN25","150#","300#"] |
| 26 | speed | Operating Speed | | RPM | number | |
| 27 | shaft_power | Shaft Power at Design | | kW | number | |
| 28 | turndown | Turndown Ratio | | | text | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | casing | Pump Casing | |
| 2 | lobes | Lobes/Rotors | |
| 3 | cover | End Cover | |
| 4 | shaft | Shafts | |
| 5 | seals | Mechanical Seals | |
| 6 | timing_gears | Timing Gears | |
| 7 | fasteners | Fasteners | 316 SS |

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
