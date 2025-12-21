---
schema_version: 1
template_id: HX-AC
title: AIR-COOLED HEAT EXCHANGER
service: AIR COOLING
has_motor: true
category: heat_exchangers
---

# AIR-COOLED HEAT EXCHANGER DATASHEET

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
| 1 | fluid | Process Fluid | | | text | |
| 2 | flow | Flow Rate | | kg/h | number | |
| 3 | temp_in | Inlet Temperature | | °C | number | |
| 4 | temp_out | Outlet Temperature | | °C | number | |
| 5 | pressure_operating | Operating Pressure | | bar(g) | number | |
| 6 | pressure_design | Design Pressure | | bar(g) | number | |
| 7 | pressure_drop | Allowable Pressure Drop (Tube Side) | | bar | number | |
| 8 | fouling | Fouling Factor | | m²·K/W | number | |
| 9 | duty | Heat Duty | | kW | number | |
| 10 | air_temp_design | Design Ambient Air Temperature | | °C | number | |
| 11 | air_temp_max | Maximum Ambient Temperature | | °C | number | |
| 12 | altitude | Site Altitude | | m | number | |

## Thermal Design

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | air_flow | Air Flow Rate | | m³/s | number | |
| 2 | air_velocity | Face Velocity | | m/s | number | |
| 3 | air_temp_rise | Air Temperature Rise | | °C | number | |
| 4 | u_overall | Overall Heat Transfer Coeff | | W/m²·K | number | |
| 5 | area_bare | Bare Tube Area | | m² | number | |
| 6 | area_extended | Extended (Finned) Area | | m² | number | |
| 7 | mtd | Mean Temperature Difference | | °C | number | |
| 8 | overdesign | Overdesign | | % | number | |
| 9 | fan_control | Fan Control | | | dropdown | ["On/Off","Two-Speed","VFD","Auto-Variable Pitch"] |

## Mechanical Design

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | ache_type | ACHE Type | | | dropdown | ["Forced Draft","Induced Draft"] |
| 2 | num_bays | Number of Bays | | | number | |
| 3 | num_bundles | Bundles per Bay | | | number | |
| 4 | tube_od | Tube Outside Diameter | | mm | number | |
| 5 | tube_thickness | Tube Wall Thickness | | mm | number | |
| 6 | tube_length | Tube Length | | mm | number | |
| 7 | tube_rows | Tube Rows | | | number | |
| 8 | tubes_per_row | Tubes per Row | | | number | |
| 9 | tube_pitch | Tube Pitch (Transverse x Longitudinal) | | mm | text | |
| 10 | fin_type | Fin Type | | | dropdown | ["Extruded Aluminum","L-Footed","Wrap-On","Embedded","Welded"] |
| 11 | fin_height | Fin Height | | mm | number | |
| 12 | fin_thickness | Fin Thickness | | mm | number | |
| 13 | fin_density | Fin Density | | fins/m | number | |
| 14 | num_passes | Tube Passes | | | dropdown | ["1","2","4","6","8"] |
| 15 | header_type | Header Type | | | dropdown | ["Plug","Cover Plate","Manifold"] |
| 16 | num_fans | Number of Fans per Bay | | | number | |
| 17 | fan_diameter | Fan Diameter | | mm | number | |
| 18 | fan_blade | Fan Blade Material | | | dropdown | ["Aluminum","FRP","Composite"] |
| 19 | design_code | Design Code | | | dropdown | ["ASME VIII Div 1","API 661","EN 13445"] |

## Nozzles

| Mark | Service | Size | Rating | Location |
|------|---------|------|--------|----------|
| N1 | Process Inlet | | | |
| N2 | Process Outlet | | | |
| D | Drain | | | |
| V | Vent | | | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | tubes | Tubes | |
| 2 | fins | Fins | |
| 3 | headers | Headers | |
| 4 | tube_sheet | Tube Sheets | |
| 5 | plugs | Plugs | |
| 6 | frame | Structural Frame | |
| 7 | fasteners | Fasteners | 316 SS |

## Driver / Motor Data

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | motor_qty | Number of Motors | | | number | |
| 2 | motor_power | Motor Power (each) | | kW | number | |
| 3 | electrical | Voltage / Phase / Hz | | V/Ph/Hz | text | |
| 4 | enclosure | Enclosure Type | | | dropdown | ["TEFC","ODP","TENV","Explosion Proof"] |
| 5 | rpm | Motor RPM | | RPM | number | |
| 6 | vfd | VFD Control | | | dropdown | ["Yes","No"] |
| 7 | drive_type | Drive Type | | | dropdown | ["Direct","V-Belt","Gear"] |

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
