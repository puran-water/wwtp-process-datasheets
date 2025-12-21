---
schema_version: 1
template_id: TK-FRP
title: FRP STORAGE TANK
service: CHEMICAL STORAGE
has_motor: false
category: tanks
---

# FRP STORAGE TANK DATASHEET

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
| 1 | fluid | Fluid Stored | | | dropdown | ["Sodium Hypochlorite","Caustic Soda","Sulfuric Acid","Hydrochloric Acid","Ferric Chloride","Sodium Bisulfite","Scrubber Effluent","Corrosive Process Liquid"] |
| 2 | concentration | Concentration | | % | number | |
| 3 | volume_nominal | Nominal Volume | | m³ | number | |
| 4 | volume_working | Working Volume | | m³ | number | |
| 5 | sg | Specific Gravity | | | number | |
| 6 | temp_operating | Operating Temperature | | °C | number | |
| 7 | temp_design | Design Temperature | | °C | number | |
| 8 | pressure | Design Pressure | | mbar(g) | number | |
| 9 | vacuum | Design Vacuum | | mbar | number | |
| 10 | resin_type | Resin Type | | | dropdown | ["Isophthalic Polyester","Vinyl Ester","Bisphenol A Epoxy","Phenolic"] |
| 11 | liner | Corrosion Liner | | | dropdown | ["C-Glass Veil","Nexus Veil","Synthetic Veil"] |
| 12 | liner_thickness | Liner Thickness | | mm | number | |
| 13 | structural | Structural Layer | | | dropdown | ["E-Glass Roving","E-Glass Mat"] |
| 14 | diameter | Tank Diameter | | mm | number | |
| 15 | height | Straight Shell Height | | mm | number | |
| 16 | orientation | Orientation | | | dropdown | ["Vertical","Horizontal"] |
| 17 | head_type | Head Type | | | dropdown | ["Flat","Dished","Conical","Elliptical"] |
| 18 | bottom_type | Bottom Type | | | dropdown | ["Flat","Dished","Conical","Sloped"] |
| 19 | wall_thickness | Wall Thickness | | mm | number | |
| 20 | design_standard | Design Standard | | | dropdown | ["ASTM D3299","BS 4994","EN 13121","ASME RTP-1"] |
| 21 | uv_protection | UV Protection | | | dropdown | ["Gel Coat","Paint","UV Additive"] |
| 22 | containment | Secondary Containment | | | dropdown | ["Bund","Double Wall","None"] |
| 23 | level_indicator | Level Indicator | | | dropdown | ["Visual Scale","Ultrasonic","Radar","Float"] |

## Fittings / Nozzles

| # | field_id | Service | Size | Type | Location |
|---|----------|---------|------|------|----------|
| 1 | inlet | Inlet | | | |
| 2 | outlet | Outlet | | | |
| 3 | drain | Drain | | | |
| 4 | overflow | Overflow | | | |
| 5 | vent | Vent | | | |
| 6 | manhole | Manhole | | | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | shell | Shell | |
| 2 | heads | Heads | |
| 3 | nozzles | Nozzles | |
| 4 | flanges | Flanges | |
| 5 | gaskets | Gaskets | |
| 6 | bolts | Bolts | 316 SS |

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
