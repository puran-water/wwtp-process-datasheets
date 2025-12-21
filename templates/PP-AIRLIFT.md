---
schema_version: 1
template_id: PP-AIRLIFT
title: AIR LIFT PUMP
service: SLUDGE/GRIT TRANSFER
has_motor: false
category: pumps
---

# AIR LIFT PUMP DATASHEET

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
| 2 | fluid | Pumped Fluid | | | dropdown | ["RAS","Grit Slurry","Scum","Mixed Liquor","Clarifier Sludge"] |
| 3 | qdesign | Design Flow Rate | | m³/h | number | |
| 4 | qmin | Minimum Flow | | m³/h | number | |
| 5 | qmax | Maximum Flow | | m³/h | number | |
| 6 | num_units | Number of Air Lift Units | | | number | |
| 7 | lift | Static Lift | | m | number | |
| 8 | submergence | Submergence Depth | | m | number | |
| 9 | submergence_ratio | Submergence Ratio | | % | number | |
| 10 | sg | Specific Gravity | | | number | |
| 11 | temp | Fluid Temperature | | °C | number | |
| 12 | solids | Solids Content | | % | number | |
| 13 | air_flow | Air Flow Required | | Nm³/h | number | |
| 14 | air_pressure | Air Pressure Required | | bar | number | |
| 15 | riser_dia | Riser Pipe Diameter | | mm | number | |
| 16 | riser_length | Riser Pipe Length | | m | number | |
| 17 | discharge_dia | Discharge Pipe Diameter | | mm | number | |
| 18 | air_injection | Air Injection Type | | | dropdown | ["Orifice Plate","Diffuser","Venturi","Open Pipe"] |
| 19 | air_injection_depth | Air Injection Depth | | m | number | |
| 20 | efficiency | Air Lift Efficiency | | % | number | |
| 21 | control | Flow Control | | | dropdown | ["Manual Valve","Modulating Valve","Blower Speed"] |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | riser | Riser Pipe | |
| 2 | discharge | Discharge Pipe | |
| 3 | air_line | Air Supply Piping | |
| 4 | injector | Air Injector | |
| 5 | supports | Pipe Supports | |
| 6 | fasteners | Fasteners | 316 SS |

## Air Supply Data

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | blower_tag | Air Supply Blower Tag | | | text | |
| 2 | blower_type | Blower Type | | | dropdown | ["Positive Displacement","Regenerative","Centrifugal"] |
| 3 | air_capacity | Blower Capacity | | Nm³/h | number | |
| 4 | discharge_pressure | Blower Discharge Pressure | | bar | number | |
| 5 | motor_power | Blower Motor Power | | kW | number | |
| 6 | electrical | Voltage / Phase / Hz | | V/Ph/Hz | text | |

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
