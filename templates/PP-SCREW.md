---
schema_version: 1
template_id: PP-SCREW
title: SCREW PUMP
service: SLUDGE TRANSFER
has_motor: true
category: pumps
---

# SCREW PUMP DATASHEET

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
| 2 | fluid | Pumped Fluid | | | dropdown | ["Primary Sludge","WAS","Thickened Sludge","Digested Sludge","Screenings","Grit Slurry","Combined Sludge"] |
| 3 | qdesign | Design Flow Rate | | m³/h | number | |
| 4 | qmin | Minimum Flow | | m³/h | number | |
| 5 | qmax | Maximum Flow | | m³/h | number | |
| 6 | num_duty | Number of Duty Pumps | | | number | |
| 7 | num_standby | Number of Standby Pumps | | | number | |
| 8 | static_lift | Static Lift | | m | number | |
| 9 | screw_angle | Screw Angle from Horizontal | | degrees | number | |
| 10 | sg | Specific Gravity | | | number | |
| 11 | temp | Fluid Temperature | | °C | number | |
| 12 | solids | Solids Content | | % | number | |
| 13 | max_particle | Maximum Particle Size | | mm | number | |
| 14 | screw_type | Screw Type | | | dropdown | ["Open Screw","Enclosed Screw"] |
| 15 | screw_diameter | Screw Diameter | | mm | number | |
| 16 | screw_length | Screw Length | | m | number | |
| 17 | screw_pitch | Screw Pitch | | mm | number | |
| 18 | flights | Number of Flights | | | dropdown | ["1","2","3"] |
| 19 | trough_liner | Trough Liner | | | dropdown | ["Steel","UHMWPE","Stainless Steel","None"] |
| 20 | speed | Operating Speed | | RPM | number | |
| 21 | shaft_power | Shaft Power at Design | | kW | number | |
| 22 | efficiency | Pump Efficiency | | % | number | |
| 23 | lower_bearing | Lower Bearing Type | | | dropdown | ["Submerged","Above Liquid Level"] |
| 24 | upper_bearing | Upper Bearing Type | | | dropdown | ["Pillow Block","Flange Mount"] |
| 25 | drive_type | Drive Type | | | dropdown | ["Direct","Gearbox","Belt"] |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | screw | Screw/Helicoid | |
| 2 | trough | Trough | |
| 3 | shaft | Central Shaft | |
| 4 | mat_flights | Flight Edges | |
| 5 | bearings | Bearings | |
| 6 | fasteners | Fasteners | 316 SS |

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
