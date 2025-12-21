---
schema_version: 1
template_id: BL-REGEN
title: REGENERATIVE BLOWER
service: LOW PRESSURE AIR SUPPLY
has_motor: true
category: blowers
---

# REGENERATIVE BLOWER DATASHEET

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
| 1 | service_type | Service Type | | | dropdown | ["Air Scour","Pneumatic Conveying","Vacuum Filtration","Aquarium/Hatchery","Small Aeration"] |
| 2 | num_duty | Number of Duty Blowers | | | number | |
| 3 | num_standby | Number of Standby Blowers | | | number | |
| 4 | mode | Operating Mode | | | dropdown | ["Pressure","Vacuum","Pressure/Vacuum"] |
| 5 | qdesign | Design Air Flow (per blower) | | m³/h | number | |
| 6 | qmin | Minimum Air Flow | | m³/h | number | |
| 7 | qmax | Maximum Air Flow | | m³/h | number | |
| 8 | pressure_rise | Pressure Rise (if pressure mode) | | mbar | number | |
| 9 | vacuum | Vacuum (if vacuum mode) | | mbar | number | |
| 10 | inlet_temp | Inlet Air Temperature | | °C | number | |
| 11 | inlet_temp_max | Maximum Inlet Temperature | | °C | number | |
| 12 | altitude | Site Altitude | | m | number | |
| 13 | humidity | Design Relative Humidity | | % | number | |
| 14 | stages | Number of Stages | | | dropdown | ["Single","Double"] |
| 15 | impeller_type | Impeller Type | | | dropdown | ["Side Channel","Radial"] |
| 16 | frequency | Drive Frequency | | | dropdown | ["50 Hz","60 Hz"] |
| 17 | inlet_filter | Inlet Filter | | | dropdown | ["Integral","External","None"] |
| 18 | silencer | Silencer | | | dropdown | ["Integral","External","None"] |
| 19 | relief_valve | Relief/Vacuum Valve | | | dropdown | ["Yes","No"] |
| 20 | noise | Maximum Noise Level | | dB(A) @ 1m | number | |
| 21 | speed | Operating Speed | | RPM | number | |
| 22 | shaft_power | Shaft Power at Design | | kW | number | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | housing | Housing | |
| 2 | impeller | Impeller | |
| 3 | cover | Cover | |
| 4 | baseplate | Baseplate | |
| 5 | fasteners | Fasteners | 316 SS |

## Driver / Motor Data

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | driver_type | Driver Type | | | dropdown | ["Integral Motor","External Motor"] |
| 2 | vfd | VFD Required | | | dropdown | ["Yes","No"] |
| 3 | mfr | Manufacturer | | | text | |
| 4 | model | Model | | | text | |
| 5 | power | Rated Power | | kW | number | |
| 6 | electrical | Voltage / Phase / Hz | | V/Ph/Hz | text | |
| 7 | enclosure | Enclosure Type | | | dropdown | ["TEFC","IP55","IP65","Explosion Proof"] |
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
