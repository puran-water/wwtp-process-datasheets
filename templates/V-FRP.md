---
schema_version: 1
template_id: V-FRP
title: FRP PRESSURE VESSEL
service: FILTRATION/ION EXCHANGE
has_motor: false
category: vessels
---

# FRP PRESSURE VESSEL DATASHEET

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
| 1 | service_type | Service Type | | | dropdown | ["Pressure Sand Filter","Carbon Filter","Multi-Media Filter","Softener","IX Cation","IX Anion","IX Mixed Bed","Cartridge Housing"] |
| 2 | num_vessels | Number of Vessels | | | number | |
| 3 | configuration | Configuration | | | dropdown | ["Single","Duplex Alternating","Triplex","Parallel"] |
| 4 | flow_design | Design Flow Rate | | m³/h | number | |
| 5 | flow_service | Service Flow Rate | | m³/h | number | |
| 6 | flow_backwash | Backwash Flow Rate | | m³/h | number | |
| 7 | pressure_operating | Operating Pressure | | bar | number | |
| 8 | pressure_design | Design Pressure | | bar | number | |
| 9 | pressure_test | Test Pressure | | bar | number | |
| 10 | pressure_drop | Pressure Drop (clean bed) | | bar | number | |
| 11 | temp_operating | Operating Temperature | | °C | number | |
| 12 | temp_design | Design Temperature | | °C | number | |
| 13 | diameter | Vessel Diameter | | mm | number | |
| 14 | shell_height | Straight Shell Height | | mm | number | |
| 15 | head_type | Head Type | | | dropdown | ["Elliptical","Hemispherical","Dished"] |
| 16 | resin_type | Resin/Laminate Type | | | dropdown | ["Isophthalic Polyester","Vinyl Ester","Epoxy"] |
| 17 | liner | Corrosion Barrier | | | dropdown | ["C-Glass Veil","Nexus Veil","Synthetic Veil"] |
| 18 | liner_thickness | Liner Thickness | | mm | number | |
| 19 | design_standard | Design Standard | | | dropdown | ["ASME RTP-1","ASME Section X","BS 4994","EN 13121"] |
| 20 | media_type | Media Type | | | dropdown | ["Sand","Anthracite","GAC","Resin","Multi-Media"] |
| 21 | media_volume | Media Volume | | L | number | |
| 22 | media_depth | Media Bed Depth | | mm | number | |
| 23 | underdrain | Underdrain Type | | | dropdown | ["Hub-Lateral","Screen Plate","Nozzle Plate"] |
| 24 | distributor | Top Distributor | | | dropdown | ["Radial","Hub-Lateral","Spray"] |

## Fittings / Nozzles

| # | field_id | Service | Size | Rating | Location |
|---|----------|---------|------|--------|----------|
| 1 | inlet | Inlet | | | |
| 2 | outlet | Outlet | | | |
| 3 | backwash_inlet | Backwash Inlet | | | |
| 4 | backwash_outlet | Backwash Outlet | | | |
| 5 | drain | Drain | | | |
| 6 | vent | Vent | | | |
| 7 | manhole | Manhole | | | |
| 8 | sample | Sample | | | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | shell | Shell/Body | |
| 2 | heads | Heads | |
| 3 | nozzles | Nozzles | |
| 4 | internals | Internals | |
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
