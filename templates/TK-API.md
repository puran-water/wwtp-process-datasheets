---
schema_version: 1
template_id: TK-API
title: API 650 ATMOSPHERIC TANK
service: BULK STORAGE
has_motor: false
category: tanks
---

# API 650 ATMOSPHERIC TANK DATASHEET

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
| 1 | fluid | Fluid Stored | | | dropdown | ["Process Water","Effluent","Chemical","Fuel Oil","Waste Oil","Thickened Sludge","Leachate"] |
| 2 | volume_nominal | Nominal Volume | | m³ | number | |
| 3 | volume_working | Working Volume | | m³ | number | |
| 4 | sg | Specific Gravity | | | number | |
| 5 | temp_operating | Operating Temperature | | °C | number | |
| 6 | temp_design | Design Temperature | | °C | number | |
| 7 | pressure_internal | Internal Design Pressure | | mbar(g) | number | |
| 8 | vacuum | Design Vacuum | | mbar | number | |
| 9 | diameter | Shell Diameter | | m | number | |
| 10 | height | Shell Height | | m | number | |
| 11 | num_courses | Number of Shell Courses | | | number | |
| 12 | roof_type | Roof Type | | | dropdown | ["Cone","Dome","Floating - Internal","Floating - External","Geodesic Aluminum","Open Top"] |
| 13 | roof_support | Roof Support | | | dropdown | ["Self Supporting","Rafter Supported","Column Supported"] |
| 14 | bottom_type | Bottom Type | | | dropdown | ["Flat","Cone Up","Cone Down","Single Slope"] |
| 15 | bottom_slope | Bottom Slope | | mm/m | number | |
| 16 | foundation | Foundation Type | | | dropdown | ["Ringwall Concrete","Concrete Pad","Crushed Stone"] |
| 17 | shell_material | Shell Material | | | dropdown | ["Carbon Steel","Stainless Steel 304L","Stainless Steel 316L"] |
| 18 | corrosion_allowance | Corrosion Allowance | | mm | number | |
| 19 | coating_internal | Internal Coating | | | dropdown | ["None","Epoxy","Glass Flake Epoxy","Rubber Lining"] |
| 20 | coating_external | External Coating | | | dropdown | ["Paint","Galvanized","Insulated"] |
| 21 | wind_load | Design Wind Speed | | m/s | number | |
| 22 | seismic | Seismic Design Category | | | dropdown | ["A","B","C","D","E","F"] |
| 23 | appendix | API 650 Appendices | | | dropdown | ["None","Appendix E (Seismic)","Appendix F (External Pressure)","Appendix J (Shop-Built)"] |
| 24 | annular_plate | Annular Plate Thickness | | mm | number | |
| 25 | level_indicator | Level Indicator | | | dropdown | ["Radar","Ultrasonic","Float & Tape","Servo"] |
| 26 | access | Roof Access | | | dropdown | ["Spiral Stairway","Fixed Ladder","None"] |

## Fittings / Nozzles

| Mark | Service | Qty | Size | Rating | Location |
|------|---------|-----|------|--------|----------|
| A | Roof Manway | | | | |
| B | Shell Manway | | | | |
| C | Inlet | | | | |
| D | Outlet | | | | |
| E | Drain | | | | |
| F | Overflow | | | | |
| G | Vent | | | | |
| H | Level Gauge | | | | |
| J | Mixer Nozzle | | | | |

## Materials

| # | field_id | Component | Material | Thickness |
|---|----------|-----------|----------|-----------|
| 1 | shell | Shell Plates | | |
| 2 | roof | Roof Plates | | |
| 3 | bottom | Bottom Plates | | |
| 4 | annular | Annular Plates | | |
| 5 | nozzles | Nozzle Necks | | |
| 6 | flanges | Flanges | | |
| 7 | bolts | Bolts | | |

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
