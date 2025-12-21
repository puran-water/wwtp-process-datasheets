---
schema_version: 1
template_id: TK-BOLT
title: BOLTED STEEL TANK
service: WATER/PROCESS STORAGE
has_motor: false
category: tanks
---

# BOLTED STEEL TANK DATASHEET

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
| 1 | fluid | Fluid Stored | | | dropdown | ["Potable Water","Process Water","Fire Water","Effluent","Leachate","Sludge"] |
| 2 | volume_nominal | Nominal Volume | | m³ | number | |
| 3 | volume_working | Working Volume | | m³ | number | |
| 4 | sg | Specific Gravity | | | number | |
| 5 | temp_operating | Operating Temperature | | °C | number | |
| 6 | temp_design | Design Temperature | | °C | number | |
| 7 | diameter | Tank Diameter | | m | number | |
| 8 | height | Tank Height | | m | number | |
| 9 | shell_material | Shell Material | | | dropdown | ["Galvanized Steel","Epoxy Coated Steel","Glass-Fused-to-Steel","Stainless Steel"] |
| 10 | liner | Internal Liner | | | dropdown | ["None","Epoxy","Polyurea","PVC","HDPE"] |
| 11 | coating_external | External Coating | | | dropdown | ["Galvanized","Painted","None"] |
| 12 | roof_type | Roof Type | | | dropdown | ["Aluminum Geodesic","Steel Cone","Aluminum Flat","Membrane","Open Top"] |
| 13 | floor_type | Floor Type | | | dropdown | ["Concrete Ringwall","Concrete Pad","Steel with Liner"] |
| 14 | panel_profile | Panel Profile | | | dropdown | ["Corrugated","Trough Deck","Flat"] |
| 15 | panel_width | Panel Width | | mm | number | |
| 16 | panel_thickness | Panel Thickness | | mm | number | |
| 17 | wind_load | Design Wind Speed | | m/s | number | |
| 18 | seismic_zone | Seismic Zone | | | dropdown | ["Zone 0","Zone 1","Zone 2A","Zone 2B","Zone 3","Zone 4"] |
| 19 | snow_load | Snow Load | | kN/m² | number | |
| 20 | design_standard | Design Standard | | | dropdown | ["AWWA D103","FM Approved","NSF 61","EN 14015"] |
| 21 | level_indicator | Level Indicator | | | dropdown | ["Ultrasonic","Radar","Pressure Transmitter","Float"] |
| 22 | access | Access | | | dropdown | ["External Ladder","Spiral Staircase","Both"] |

## Fittings / Nozzles

| # | field_id | Service | Size | Type | Location |
|---|----------|---------|------|------|----------|
| 1 | inlet | Inlet | | | |
| 2 | outlet | Outlet | | | |
| 3 | drain | Drain | | | |
| 4 | overflow | Overflow | | | |
| 5 | vent | Vent | | | |
| 6 | manhole | Manhole | | | |
| 7 | roof_access | Roof Access Hatch | | | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | shell | Shell Panels | |
| 2 | roof | Roof | |
| 3 | floor | Floor | |
| 4 | hardware | Hardware/Bolts | |
| 5 | sealant | Joint Sealant | |
| 6 | gaskets | Gaskets | |

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
