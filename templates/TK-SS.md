---
schema_version: 1
template_id: TK-SS
title: STAINLESS STEEL TANK
service: PROCESS/CHEMICAL STORAGE
has_motor: false
category: tanks
---

# STAINLESS STEEL TANK DATASHEET

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
| 1 | fluid | Fluid Stored | | | dropdown | ["Chemical Solution","Process Water","Sludge","Food Grade Liquid","Pharmaceutical","CIP Solution"] |
| 2 | concentration | Concentration (if chemical) | | % | number | |
| 3 | volume_nominal | Nominal Volume | | m³ | number | |
| 4 | volume_working | Working Volume | | m³ | number | |
| 5 | sg | Specific Gravity | | | number | |
| 6 | temp_operating | Operating Temperature | | °C | number | |
| 7 | temp_design | Design Temperature | | °C | number | |
| 8 | pressure_operating | Operating Pressure | | mbar(g) | number | |
| 9 | pressure_design | Design Pressure | | mbar(g) | number | |
| 10 | vacuum | Design Vacuum | | mbar | number | |
| 11 | ss_grade | Stainless Steel Grade | | | dropdown | ["304","304L","316","316L","Duplex 2205","Super Duplex"] |
| 12 | diameter | Tank Diameter | | mm | number | |
| 13 | height | Straight Shell Height | | mm | number | |
| 14 | orientation | Orientation | | | dropdown | ["Vertical","Horizontal"] |
| 15 | head_type | Top Head Type | | | dropdown | ["Flat","Dished","Conical","Torispherical","Elliptical"] |
| 16 | bottom_type | Bottom Type | | | dropdown | ["Flat","Dished","Conical","Sloped"] |
| 17 | wall_thickness | Wall Thickness | | mm | number | |
| 18 | finish | Internal Surface Finish | | | dropdown | ["2B Mill","#4 Brushed","Electropolished","Ra ≤ 0.8µm"] |
| 19 | insulation | Insulation | | | dropdown | ["None","Mineral Wool","Foam","Trace Heated"] |
| 20 | jacket | Jacket | | | dropdown | ["None","Half Pipe","Dimple","Full Jacket"] |
| 21 | agitator | Agitator | | | dropdown | ["None","Top Entry","Side Entry","Magnetic"] |
| 22 | level_indicator | Level Indicator | | | dropdown | ["Sight Glass","Ultrasonic","Radar","Capacitance"] |
| 23 | design_standard | Design Standard | | | dropdown | ["EN 13445","ASME VIII","API 650","DIN 28011"] |

## Fittings / Nozzles

| # | field_id | Service | Size | Type | Location |
|---|----------|---------|------|------|----------|
| 1 | inlet | Inlet | | | |
| 2 | outlet | Outlet | | | |
| 3 | drain | Drain | | | |
| 4 | overflow | Overflow | | | |
| 5 | vent | Vent | | | |
| 6 | manhole | Manhole | | | |
| 7 | cip | CIP Spray Ball | | | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | shell | Shell | |
| 2 | heads | Heads | |
| 3 | nozzles | Nozzles | |
| 4 | supports | Supports/Legs | |
| 5 | gaskets | Gaskets | |
| 6 | bolts | Bolts | |

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
