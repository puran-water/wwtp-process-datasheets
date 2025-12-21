---
schema_version: 1
template_id: V-SS
title: STAINLESS STEEL PRESSURE VESSEL
service: PROCESS VESSEL
has_motor: false
category: vessels
---

# STAINLESS STEEL PRESSURE VESSEL DATASHEET

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
| 1 | service_type | Service Type | | | dropdown | ["Filter Vessel","Reactor","Accumulator","Flash Drum","Separator","Receiver"] |
| 2 | fluid | Process Fluid | | | text | |
| 3 | volume_total | Total Volume | | m³ | number | |
| 4 | volume_working | Working Volume | | m³ | number | |
| 5 | sg | Specific Gravity | | | number | |
| 6 | pressure_operating | Operating Pressure | | bar(g) | number | |
| 7 | pressure_design | Design Pressure | | bar(g) | number | |
| 8 | vacuum | Full Vacuum | | | dropdown | ["Yes","No"] |
| 9 | pressure_test | Hydro Test Pressure | | bar(g) | number | |
| 10 | temp_operating | Operating Temperature | | °C | number | |
| 11 | temp_design_max | Maximum Design Temperature | | °C | number | |
| 12 | temp_design_min | Minimum Design Temperature | | °C | number | |
| 13 | ss_grade | Stainless Steel Grade | | | dropdown | ["304","304L","316","316L","Duplex 2205","Super Duplex 2507"] |
| 14 | diameter | Inside Diameter | | mm | number | |
| 15 | tan_tan | Tan-to-Tan Length | | mm | number | |
| 16 | orientation | Orientation | | | dropdown | ["Vertical","Horizontal"] |
| 17 | head_top | Top Head Type | | | dropdown | ["Elliptical 2:1","Hemispherical","Torispherical","Flat"] |
| 18 | head_bottom | Bottom Head Type | | | dropdown | ["Elliptical 2:1","Hemispherical","Torispherical","Conical","Flat"] |
| 19 | shell_thickness | Shell Thickness | | mm | number | |
| 20 | head_thickness | Head Thickness | | mm | number | |
| 21 | corrosion_allowance | Corrosion Allowance | | mm | number | |
| 22 | design_code | Design Code | | | dropdown | ["ASME VIII Div 1","ASME VIII Div 2","EN 13445","PD 5500"] |
| 23 | radiography | Radiography | | | dropdown | ["Full","Spot","None"] |
| 24 | pwht | PWHT Required | | | dropdown | ["Yes","No"] |
| 25 | finish_internal | Internal Surface Finish | | | dropdown | ["2B Mill","#4 Brushed","Electropolished","Ra ≤ 0.8µm"] |
| 26 | insulation | Insulation | | | dropdown | ["None","Mineral Wool","Calcium Silicate","Foam Glass"] |
| 27 | insulation_thickness | Insulation Thickness | | mm | number | |

## Fittings / Nozzles

| Mark | Service | Size | Rating | Facing | Location |
|------|---------|------|--------|--------|----------|
| N1 | Inlet | | | | |
| N2 | Outlet | | | | |
| N3 | Drain | | | | |
| N4 | Vent | | | | |
| N5 | Level | | | | |
| N6 | Pressure | | | | |
| N7 | Temperature | | | | |
| MH | Manhole | | | | |

## Materials

| # | field_id | Component | Material | Specification |
|---|----------|-----------|----------|---------------|
| 1 | shell | Shell | | |
| 2 | heads | Heads | | |
| 3 | nozzles | Nozzle Necks | | |
| 4 | flanges | Flanges | | |
| 5 | internals | Internals | | |
| 6 | gaskets | Gaskets | | |
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
