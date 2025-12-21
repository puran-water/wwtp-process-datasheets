---
schema_version: 1
template_id: BL-TURBO
title: HIGH-SPEED TURBO BLOWER
service: AERATION AIR SUPPLY
has_motor: true
category: blowers
---

# HIGH-SPEED TURBO BLOWER DATASHEET

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
| 1 | service_type | Service Type | | | dropdown | ["Aeration","MBR Air Scour","Grit Tank"] |
| 2 | num_duty | Number of Duty Blowers | | | number | |
| 3 | num_standby | Number of Standby Blowers | | | number | |
| 4 | qdesign | Design Air Flow (per blower) | | Nm³/h | number | |
| 5 | qmin | Minimum Air Flow | | Nm³/h | number | |
| 6 | qmax | Maximum Air Flow | | Nm³/h | number | |
| 7 | turndown | Turndown Ratio | | % | number | |
| 8 | inlet_pressure | Inlet Pressure | | mbar(a) | number | |
| 9 | discharge_pressure | Discharge Pressure | | bar(g) | number | |
| 10 | diff_pressure | Differential Pressure | | bar | number | |
| 11 | inlet_temp | Inlet Air Temperature | | °C | number | |
| 12 | discharge_temp_max | Maximum Discharge Temperature | | °C | number | |
| 13 | altitude | Site Altitude | | m | number | |
| 14 | humidity | Design Relative Humidity | | % | number | |
| 15 | diffuser_submergence | Diffuser Submergence | | m | number | |
| 16 | piping_losses | Piping/Valve Losses | | mbar | number | |
| 17 | bearing_type | Bearing Type | | | dropdown | ["Air Foil","Magnetic","Oil Film"] |
| 18 | impeller_type | Impeller Type | | | dropdown | ["Single Stage","Two Stage"] |
| 19 | impeller_material | Impeller Material | | | dropdown | ["Titanium","Aluminum Alloy","Steel"] |
| 20 | control | Capacity Control | | | dropdown | ["VFD","Inlet Guide Vanes","Combined IGV + VFD"] |
| 21 | cooling | Motor/Electronics Cooling | | | dropdown | ["Air Cooled","Water Cooled"] |
| 22 | inlet_filter | Inlet Filter | | | dropdown | ["Dry Panel","Bag","HEPA","Self-Cleaning"] |
| 23 | silencer | Silencer Required | | | dropdown | ["Inlet Only","Discharge Only","Both","None"] |
| 24 | noise | Maximum Noise Level | | dB(A) @ 1m | number | |
| 25 | acoustic_enclosure | Acoustic Enclosure | | | dropdown | ["Yes - Standard","Yes - Premium","No"] |
| 26 | surge_protection | Surge Protection | | | dropdown | ["Blow-off Valve","Anti-Surge Control","Integral VFD Logic"] |
| 27 | local_panel | Local Control Panel | | | dropdown | ["Yes","No"] |
| 28 | speed | Maximum Operating Speed | | RPM | number | |
| 29 | shaft_power | Shaft Power at Design | | kW | number | |
| 30 | efficiency | Adiabatic Efficiency | | % | number | |
| 31 | power_factor | Power Factor at Design | | | number | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | casing | Blower Casing | |
| 2 | impeller | Impeller | |
| 3 | volute | Volute/Scroll | |
| 4 | inlet | Inlet Housing | |
| 5 | baseplate | Baseplate/Skid | |
| 6 | fasteners | Fasteners | 316 SS |

## Driver / Motor Data

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | driver_type | Driver Type | | | dropdown | ["Integral High-Speed Motor","Permanent Magnet Motor"] |
| 2 | vfd | VFD Type | | | dropdown | ["Integral","Remote"] |
| 3 | mfr | Manufacturer | | | text | |
| 4 | model | Model | | | text | |
| 5 | power | Rated Power | | kW | number | |
| 6 | electrical | Voltage / Phase / Hz | | V/Ph/Hz | text | |
| 7 | enclosure | Enclosure Type | | | dropdown | ["IP55","IP65","IP66"] |
| 8 | rpm_max | Maximum Motor RPM | | RPM | number | |
| 9 | insulation | Insulation Class | | | dropdown | ["F","H"] |
| 10 | efficiency_class | Efficiency Class | | | dropdown | ["IE3","IE4","IE5"] |

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
