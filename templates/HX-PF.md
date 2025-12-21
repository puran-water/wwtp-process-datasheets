---
schema_version: 1
template_id: HX-PF
title: PLATE & FRAME HEAT EXCHANGER
service: HEAT TRANSFER
has_motor: false
category: heat_exchangers
---

# PLATE & FRAME HEAT EXCHANGER DATASHEET

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

## Operating / Design Data - Hot Side

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | hot_fluid | Fluid | | | text | |
| 2 | hot_flow | Flow Rate | | m³/h | number | |
| 3 | hot_temp_in | Inlet Temperature | | °C | number | |
| 4 | hot_temp_out | Outlet Temperature | | °C | number | |
| 5 | hot_pressure_operating | Operating Pressure | | bar(g) | number | |
| 6 | hot_pressure_design | Design Pressure | | bar(g) | number | |
| 7 | hot_pressure_drop | Allowable Pressure Drop | | bar | number | |
| 8 | hot_fouling | Fouling Factor | | m²·K/W | number | |
| 9 | hot_sg | Specific Gravity | | | number | |
| 10 | hot_viscosity | Viscosity | | cP | number | |

## Operating / Design Data - Cold Side

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | cold_fluid | Fluid | | | text | |
| 2 | cold_flow | Flow Rate | | m³/h | number | |
| 3 | cold_temp_in | Inlet Temperature | | °C | number | |
| 4 | cold_temp_out | Outlet Temperature | | °C | number | |
| 5 | cold_pressure_operating | Operating Pressure | | bar(g) | number | |
| 6 | cold_pressure_design | Design Pressure | | bar(g) | number | |
| 7 | cold_pressure_drop | Allowable Pressure Drop | | bar | number | |
| 8 | cold_fouling | Fouling Factor | | m²·K/W | number | |
| 9 | cold_sg | Specific Gravity | | | number | |
| 10 | cold_viscosity | Viscosity | | cP | number | |

## Thermal Design

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | duty | Heat Duty | | kW | number | |
| 2 | lmtd | LMTD | | °C | number | |
| 3 | u_overall | Overall Heat Transfer Coeff | | W/m²·K | number | |
| 4 | area | Heat Transfer Area | | m² | number | |
| 5 | overdesign | Overdesign | | % | number | |
| 6 | phe_type | PHE Type | | | dropdown | ["Gasketed","Semi-Welded","Fully Welded","Brazed"] |
| 7 | flow_arrangement | Flow Arrangement | | | dropdown | ["1-Pass/1-Pass","2-Pass/2-Pass","Multi-Pass"] |
| 8 | approach_temp | Approach Temperature | | °C | number | |

## Mechanical Design

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | frame_type | Frame Type | | | dropdown | ["Standard","Hygienic","High Pressure"] |
| 2 | plate_count | Number of Plates | | | number | |
| 3 | plate_size | Plate Size (W x H) | | mm | text | |
| 4 | plate_thickness | Plate Thickness | | mm | number | |
| 5 | plate_pattern | Plate Pattern | | | dropdown | ["Chevron","Herringbone","Mixed"] |
| 6 | channel_gap | Channel Gap | | mm | number | |
| 7 | port_size | Port Size | | mm | number | |
| 8 | connection_type | Connection Type | | | dropdown | ["Flanged","Threaded","Tri-Clamp"] |
| 9 | flange_rating | Flange Rating | | | dropdown | ["PN10","PN16","PN25","150#","300#"] |
| 10 | frame_length | Frame Length (A) | | mm | number | |
| 11 | frame_height | Frame Height (B) | | mm | number | |
| 12 | frame_width | Frame Width (closed) | | mm | number | |
| 13 | max_plates | Maximum Plate Capacity | | | number | |
| 14 | weight_empty | Weight (empty) | | kg | number | |
| 15 | weight_operating | Weight (operating) | | kg | number | |

## Nozzles

| Mark | Service | Size | Rating | Location |
|------|---------|------|--------|----------|
| H1 | Hot Inlet | | | |
| H2 | Hot Outlet | | | |
| C1 | Cold Inlet | | | |
| C2 | Cold Outlet | | | |
| D | Drain | | | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | plates | Plates | |
| 2 | gaskets | Gaskets | |
| 3 | frame | Frame | |
| 4 | pressure_plate | Pressure Plate | |
| 5 | tie_bolts | Tie Bolts | |
| 6 | connections | Connections | |

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
