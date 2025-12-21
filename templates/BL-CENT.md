---
schema_version: 1
template_id: BL-CENT
title: MULTI-STAGE CENTRIFUGAL BLOWER
service: AERATION AIR SUPPLY
has_motor: true
category: blowers
---

# MULTI-STAGE CENTRIFUGAL BLOWER DATASHEET

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
| 1 | service_type | Service Type | | | dropdown | ["Aeration","MBR Air Scour","Filter Air Scour","Biogas Compression"] |
| 2 | num_duty | Number of Duty Blowers | | | number | |
| 3 | num_standby | Number of Standby Blowers | | | number | |
| 4 | qdesign | Design Air Flow (per blower) | | Nm³/h | number | |
| 5 | qnormal | Normal Air Flow | | Nm³/h | number | |
| 6 | qmin | Minimum Air Flow | | Nm³/h | number | |
| 7 | qmax | Maximum Air Flow | | Nm³/h | number | |
| 8 | turndown | Turndown Ratio | | % | number | |
| 9 | inlet_pressure | Inlet Pressure | | mbar(a) | number | |
| 10 | discharge_pressure | Discharge Pressure | | bar(g) | number | |
| 11 | diff_pressure | Differential Pressure | | bar | number | |
| 12 | inlet_temp | Inlet Air Temperature | | °C | number | |
| 13 | inlet_temp_max | Maximum Inlet Temperature | | °C | number | |
| 14 | discharge_temp | Discharge Temperature | | °C | number | |
| 15 | altitude | Site Altitude | | m | number | |
| 16 | humidity | Design Relative Humidity | | % | number | |
| 17 | diffuser_submergence | Diffuser Submergence | | m | number | |
| 18 | piping_losses | Piping/Valve Losses | | mbar | number | |
| 19 | stages | Number of Stages | | | number | |
| 20 | impeller_type | Impeller Type | | | dropdown | ["Radial","Backward Curved"] |
| 21 | control | Capacity Control | | | dropdown | ["VFD","Inlet Guide Vanes","Discharge Throttle","Combined IGV + VFD"] |
| 22 | cooling | Interstage Cooling | | | dropdown | ["None","Air Cooled Intercooler","Water Cooled Intercooler"] |
| 23 | inlet_filter | Inlet Filter | | | dropdown | ["Dry Panel","Bag","HEPA","Self-Cleaning"] |
| 24 | silencer | Silencer Required | | | dropdown | ["Inlet Only","Discharge Only","Both","None"] |
| 25 | noise | Maximum Noise Level | | dB(A) @ 1m | number | |
| 26 | acoustic_enclosure | Acoustic Enclosure | | | dropdown | ["Yes","No"] |
| 27 | surge_protection | Surge Protection | | | dropdown | ["Blow-off Valve","Anti-Surge Control","VFD Based","None"] |
| 28 | local_panel | Local Control Panel | | | dropdown | ["Yes","No"] |
| 29 | speed | Operating Speed | | RPM | number | |
| 30 | shaft_power | Shaft Power at Design | | kW | number | |
| 31 | efficiency | Polytropic Efficiency | | % | number | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | casing | Blower Casing | |
| 2 | impellers | Impellers | |
| 3 | diffusers | Diffusers | |
| 4 | shaft | Shaft | |
| 5 | bearings | Bearings | |
| 6 | seals | Shaft Seals | |
| 7 | baseplate | Baseplate/Skid | |
| 8 | fasteners | Fasteners | 316 SS |

## Driver / Motor Data

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | driver_type | Driver Type | | | dropdown | ["Electric Motor","Steam Turbine"] |
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
