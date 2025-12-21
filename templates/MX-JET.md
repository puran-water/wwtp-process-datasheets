---
schema_version: 1
template_id: MX-JET
title: JET MIXER - EDUCTOR
service: TANK MIXING
has_motor: false
category: mixers
---

# JET MIXER / EDUCTOR DATASHEET

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
| 1 | service_type | Service Type | | | dropdown | ["Tank Mixing","Blending","Equalization","Chemical Dilution","Digester Mixing"] |
| 2 | num_units | Number of Units per Tank | | | number | |
| 3 | tank_volume | Tank Volume | | m³ | number | |
| 4 | tank_diameter | Tank Diameter | | m | number | |
| 5 | liquid_depth | Liquid Depth | | m | number | |
| 6 | fluid | Mixed Fluid | | | dropdown | ["Water","Mixed Liquor","Sludge","Chemical Solution"] |
| 7 | sg | Specific Gravity | | | number | |
| 8 | viscosity | Viscosity | | cP | number | |
| 9 | solids | Solids Content | | % | number | |
| 10 | temp | Fluid Temperature | | °C | number | |
| 11 | motive_flow | Motive Flow (per unit) | | m³/h | number | |
| 12 | motive_pressure | Motive Pressure | | bar | number | |
| 13 | entrained_flow | Entrained Flow (per unit) | | m³/h | number | |
| 14 | discharge_flow | Discharge Flow (per unit) | | m³/h | number | |
| 15 | entrainment_ratio | Entrainment Ratio | | | number | |
| 16 | nozzle_diameter | Nozzle Diameter | | mm | number | |
| 17 | throat_diameter | Throat Diameter | | mm | number | |
| 18 | diffuser_diameter | Diffuser Outlet Diameter | | mm | number | |
| 19 | inlet_connection | Motive Inlet Connection | | mm | number | |
| 20 | outlet_connection | Discharge Connection | | mm | number | |
| 21 | connection_type | Connection Type | | | dropdown | ["Flanged","Threaded","Butt Weld"] |
| 22 | mounting | Mounting Type | | | dropdown | ["Floor Mount","Tank Wall","Suspended"] |
| 23 | orientation | Orientation | | | dropdown | ["Horizontal","Vertical","Angled"] |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | body | Eductor Body | |
| 2 | nozzle | Motive Nozzle | |
| 3 | diffuser | Diffuser | |
| 4 | flange | Flanges | |
| 5 | fasteners | Fasteners | 316 SS |

## Motive Pump Data

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | pump_tag | Motive Pump Tag | | | text | |
| 2 | pump_type | Pump Type | | | dropdown | ["Centrifugal","Progressive Cavity","Submersible"] |
| 3 | pump_flow | Pump Flow | | m³/h | number | |
| 4 | pump_head | Pump Head | | m | number | |
| 5 | pump_power | Pump Motor Power | | kW | number | |
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
