---
schema_version: 1
template_id: HX-ST
title: SHELL & TUBE HEAT EXCHANGER
service: HEAT TRANSFER
has_motor: false
category: heat_exchangers
---

# SHELL & TUBE HEAT EXCHANGER DATASHEET

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

## Operating / Design Data - Shell Side

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | shell_fluid | Fluid | | | text | |
| 2 | shell_flow | Flow Rate | | kg/h | number | |
| 3 | shell_temp_in | Inlet Temperature | | °C | number | |
| 4 | shell_temp_out | Outlet Temperature | | °C | number | |
| 5 | shell_pressure_operating | Operating Pressure | | bar(g) | number | |
| 6 | shell_pressure_design | Design Pressure | | bar(g) | number | |
| 7 | shell_pressure_drop | Allowable Pressure Drop | | bar | number | |
| 8 | shell_fouling | Fouling Factor | | m²·K/W | number | |
| 9 | shell_corrosion | Corrosion Allowance | | mm | number | |

## Operating / Design Data - Tube Side

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | tube_fluid | Fluid | | | text | |
| 2 | tube_flow | Flow Rate | | kg/h | number | |
| 3 | tube_temp_in | Inlet Temperature | | °C | number | |
| 4 | tube_temp_out | Outlet Temperature | | °C | number | |
| 5 | tube_pressure_operating | Operating Pressure | | bar(g) | number | |
| 6 | tube_pressure_design | Design Pressure | | bar(g) | number | |
| 7 | tube_pressure_drop | Allowable Pressure Drop | | bar | number | |
| 8 | tube_fouling | Fouling Factor | | m²·K/W | number | |
| 9 | tube_corrosion | Corrosion Allowance | | mm | number | |

## Thermal Design

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | duty | Heat Duty | | kW | number | |
| 2 | lmtd | LMTD (Corrected) | | °C | number | |
| 3 | u_overall | Overall Heat Transfer Coeff | | W/m²·K | number | |
| 4 | area | Heat Transfer Area | | m² | number | |
| 5 | overdesign | Overdesign | | % | number | |
| 6 | tema_type | TEMA Type | | | dropdown | ["AES","AEU","BEM","BEU","AEL","CFU","NEN","AKT"] |
| 7 | shell_passes | Shell Passes | | | dropdown | ["1","2","4"] |
| 8 | tube_passes | Tube Passes | | | dropdown | ["1","2","4","6","8"] |

## Mechanical Design

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | shell_id | Shell Inside Diameter | | mm | number | |
| 2 | shell_length | Shell Length (Tube Sheet to Tube Sheet) | | mm | number | |
| 3 | tube_od | Tube Outside Diameter | | mm | number | |
| 4 | tube_thickness | Tube Wall Thickness | | mm | number | |
| 5 | tube_length | Tube Length | | mm | number | |
| 6 | tube_count | Number of Tubes | | | number | |
| 7 | tube_pitch | Tube Pitch | | mm | number | |
| 8 | tube_pattern | Tube Pattern | | | dropdown | ["Triangular 30°","Rotated Triangular 60°","Square 90°","Rotated Square 45°"] |
| 9 | baffle_type | Baffle Type | | | dropdown | ["Single Segmental","Double Segmental","Triple Segmental","No-Tubes-in-Window","Helical","Rod"] |
| 10 | baffle_cut | Baffle Cut | | % | number | |
| 11 | baffle_spacing | Baffle Spacing (Central) | | mm | number | |
| 12 | tube_sheet | Tube-to-Tube Sheet Joint | | | dropdown | ["Rolled","Welded","Rolled + Seal Welded"] |
| 13 | expansion | Expansion Joint | | | dropdown | ["None","Bellows","Floating Head"] |
| 14 | design_code | Design Code | | | dropdown | ["ASME VIII Div 1","TEMA Class R","TEMA Class C","TEMA Class B"] |

## Nozzles

| Mark | Service | Size | Rating | Facing |
|------|---------|------|--------|--------|
| S1 | Shell Inlet | | | |
| S2 | Shell Outlet | | | |
| T1 | Tube Inlet | | | |
| T2 | Tube Outlet | | | |
| D | Shell Drain | | | |
| V | Shell Vent | | | |

## Materials

| # | field_id | Component | Shell Side | Tube Side |
|---|----------|-----------|------------|-----------|
| 1 | shell | Shell | | |
| 2 | channel | Channel/Head | | |
| 3 | tube_sheet | Tube Sheet | | |
| 4 | tubes | Tubes | | |
| 5 | baffles | Baffles | | |
| 6 | tie_rods | Tie Rods | | |
| 7 | gaskets | Gaskets | | |
| 8 | bolts | Bolts | | |

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
