---
schema_version: 1
template_id: BL-PD
title: POSITIVE DISPLACEMENT BLOWER
service: AERATION AIR SUPPLY
has_motor: true
category: blowers
---

# POSITIVE DISPLACEMENT BLOWER DATASHEET

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
| 1 | service_type | Service Type | | | dropdown | ["Aeration","Grit Tank","Digester Mixing","Filter Air Scour","Channel Aeration"] |
| 2 | num_duty | Number of Duty Blowers | | | number | |
| 3 | num_standby | Number of Standby Blowers | | | number | |
| 4 | qdesign | Design Air Flow (per blower) | | Nm³/h | number | |
| 5 | qmin | Minimum Air Flow | | Nm³/h | number | |
| 6 | qmax | Maximum Air Flow | | Nm³/h | number | |
| 7 | turndown | Turndown Ratio | | % | number | |
| 8 | inlet_pressure | Inlet Pressure | | mbar(a) | number | |
| 9 | discharge_pressure | Discharge Pressure | | mbar(g) | number | |
| 10 | diff_pressure | Differential Pressure | | mbar | number | |
| 11 | inlet_temp | Inlet Air Temperature | | °C | number | |
| 12 | discharge_temp | Discharge Temperature | | °C | number | |
| 13 | altitude | Site Altitude | | m | number | |
| 14 | humidity | Relative Humidity | | % | number | |
| 15 | diffuser_submergence | Diffuser Submergence | | m | number | |
| 16 | piping_losses | Piping/Valve Losses | | mbar | number | |
| 17 | lobe_type | Lobe Type | | | dropdown | ["Bi-Lobe","Tri-Lobe"] |
| 18 | stages | Number of Stages | | | dropdown | ["Single","Two-Stage"] |
| 19 | cooling | Cooling System | | | dropdown | ["Air Cooled","Water Cooled"] |
| 20 | inlet_filter | Inlet Filter | | | dropdown | ["Dry Panel","Bag","HEPA","Self-Cleaning"] |
| 21 | silencer | Silencer Required | | | dropdown | ["Inlet Only","Discharge Only","Both","None"] |
| 22 | noise | Maximum Noise Level | | dB(A) @ 1m | number | |
| 23 | acoustic_enclosure | Acoustic Enclosure | | | dropdown | ["Yes","No"] |
| 24 | local_panel | Local Control Panel | | | dropdown | ["Yes","No"] |
| 25 | speed | Operating Speed | | RPM | number | |
| 26 | shaft_power | Shaft Power at Design | | kW | number | |
| 27 | efficiency | Volumetric Efficiency | | % | number | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | casing | Blower Casing | |
| 2 | rotors | Lobes/Rotors | |
| 3 | timing_gears | Timing Gears | |
| 4 | shaft | Shafts | |
| 5 | bearings | Bearings | |
| 6 | seals | Shaft Seals | |
| 7 | baseplate | Baseplate/Skid | |
| 8 | fasteners | Fasteners | 316 SS |

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
