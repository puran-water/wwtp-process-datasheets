---
schema_version: 1
template_id: FL-BASKET
title: BASKET STRAINER
service: STRAINING
has_motor: false
category: filtration
---

# BASKET STRAINER DATASHEET

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
| 1 | strainer_type | Strainer Type | | | dropdown | ["Simplex","Duplex","Y-Strainer"] |
| 2 | orientation | Orientation | | | dropdown | ["Horizontal","Vertical","Angled"] |
| 3 | fluid | Process Fluid | | | text | |
| 4 | flow | Design Flow Rate | | m³/h | number | |
| 5 | flow_max | Maximum Flow Rate | | m³/h | number | |
| 6 | temp_operating | Operating Temperature | | °C | number | |
| 7 | temp_design | Design Temperature | | °C | number | |
| 8 | pressure_operating | Operating Pressure | | bar(g) | number | |
| 9 | pressure_design | Design Pressure | | bar(g) | number | |
| 10 | viscosity | Fluid Viscosity | | cP | number | |
| 11 | sg | Specific Gravity | | | number | |
| 12 | solids_conc | Solids Concentration | | mg/L | number | |
| 13 | solids_type | Solids Type | | | text | |
| 14 | mesh_size | Screen Mesh Size | | mesh | number | |
| 15 | perf_size | Perforation Size | | mm | number | |
| 16 | open_area | Screen Open Area | | % | number | |
| 17 | dp_clean | Pressure Drop (Clean) | | bar | number | |
| 18 | dp_dirty | Pressure Drop (Dirty/Alarm) | | bar | number | |
| 19 | basket_volume | Basket Volume | | L | number | |
| 20 | connection_in | Inlet Connection Size | | mm | text | |
| 21 | connection_out | Outlet Connection Size | | mm | text | |
| 22 | connection_type | Connection Type | | | dropdown | ["Flanged","Threaded","Buttweld"] |
| 23 | flange_rating | Flange Rating | | | dropdown | ["PN10","PN16","PN25","PN40","150#","300#"] |

## Mechanical Design

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | body_size | Body Size | | DN | number | |
| 2 | basket_type | Basket Type | | | dropdown | ["Perforated","Mesh","Wedge Wire"] |
| 3 | basket_support | Basket Support | | | dropdown | ["Bottom","Side","Suspended"] |
| 4 | cover_type | Cover Type | | | dropdown | ["Bolted","Quick-Open","Hinged"] |
| 5 | cover_seal | Cover Seal Type | | | dropdown | ["O-Ring","Gasket","Metal-to-Metal"] |
| 6 | drain | Drain Connection | | | dropdown | ["Yes","No"] |
| 7 | vent | Vent Connection | | | dropdown | ["Yes","No"] |
| 8 | dp_gauge | DP Gauge Connection | | | dropdown | ["Yes","No"] |
| 9 | design_code | Design Code | | | dropdown | ["ASME VIII","EN 13445","PD 5500"] |
| 10 | weight_empty | Weight (Empty) | | kg | number | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | body | Body | |
| 2 | cover | Cover | |
| 3 | basket | Basket | |
| 4 | screen | Screen/Mesh | |
| 5 | gaskets | Gaskets | |
| 6 | fasteners | Fasteners | 316 SS |

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
