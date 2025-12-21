---
schema_version: 1
template_id: V-ASME
title: ASME PRESSURE VESSEL
service: PROCESS VESSEL
has_motor: false
category: vessels
---

# ASME PRESSURE VESSEL DATASHEET

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
| 1 | service_type | Service Type | | | dropdown | ["Flash Drum","Separator","Accumulator","Receiver","Reactor","Surge Vessel","Knockout Drum"] |
| 2 | fluid | Process Fluid | | | text | |
| 3 | phase | Fluid Phase | | | dropdown | ["Liquid","Vapor","Two-Phase","Three-Phase"] |
| 4 | volume_total | Total Volume | | m³ | number | |
| 5 | volume_working | Working Volume | | m³ | number | |
| 6 | sg_liquid | Liquid Specific Gravity | | | number | |
| 7 | mw_vapor | Vapor Molecular Weight | | | number | |
| 8 | pressure_operating | Operating Pressure | | bar(g) | number | |
| 9 | pressure_design | Design Pressure | | bar(g) | number | |
| 10 | mawp | MAWP | | bar(g) | number | |
| 11 | vacuum | Full Vacuum | | | dropdown | ["Yes","No"] |
| 12 | pressure_test | Hydro Test Pressure | | bar(g) | number | |
| 13 | temp_operating | Operating Temperature | | °C | number | |
| 14 | temp_design_max | Maximum Design Temperature | | °C | number | |
| 15 | temp_design_min | Minimum Design Temperature | | °C | number | |
| 16 | mdmt | MDMT | | °C | number | |
| 17 | diameter | Inside Diameter | | mm | number | |
| 18 | tan_tan | Tan-to-Tan Length | | mm | number | |
| 19 | orientation | Orientation | | | dropdown | ["Vertical","Horizontal"] |
| 20 | head_top | Top Head Type | | | dropdown | ["Elliptical 2:1","Hemispherical","Torispherical","Flat"] |
| 21 | head_bottom | Bottom Head Type | | | dropdown | ["Elliptical 2:1","Hemispherical","Torispherical","Conical","Flat"] |
| 22 | shell_thickness | Shell Thickness | | mm | number | |
| 23 | head_thickness | Head Thickness | | mm | number | |
| 24 | corrosion_allowance | Corrosion Allowance | | mm | number | |
| 25 | design_code | Design Code | | | dropdown | ["ASME VIII Div 1","ASME VIII Div 2"] |
| 26 | joint_efficiency | Joint Efficiency | | | dropdown | ["0.70","0.85","1.00"] |
| 27 | radiography | Radiography | | | dropdown | ["Full (RT-1)","Spot (RT-2)","Partial (RT-3)","None (RT-4)"] |
| 28 | pwht | PWHT Required | | | dropdown | ["Yes","No"] |
| 29 | impact_test | Impact Testing | | | dropdown | ["Required","Not Required","Exempted per UCS-66"] |
| 30 | nameplate | ASME U Stamp | | | dropdown | ["Yes"] |
| 31 | internals | Internals | | | dropdown | ["None","Demister Pad","Vortex Breaker","Baffles","Trays"] |
| 32 | insulation | Insulation | | | dropdown | ["None","Mineral Wool","Calcium Silicate","Foam Glass","Cold Insulation"] |

## Fittings / Nozzles

| Mark | Service | Size | Rating | Facing | Projection | Location |
|------|---------|------|--------|--------|------------|----------|
| N1 | Inlet | | | | | |
| N2 | Outlet (Liquid) | | | | | |
| N3 | Outlet (Vapor) | | | | | |
| N4 | Drain | | | | | |
| N5 | Vent | | | | | |
| N6 | Level | | | | | |
| N7 | Pressure | | | | | |
| N8 | Temperature | | | | | |
| N9 | Safety Valve | | | | | |
| MH | Manhole | | | | | |

## Materials

| # | field_id | Component | Material | Specification |
|---|----------|-----------|----------|---------------|
| 1 | shell | Shell | | |
| 2 | heads | Heads | | |
| 3 | nozzles | Nozzle Necks | | |
| 4 | flanges | Flanges | | |
| 5 | rf_pads | Reinforcing Pads | | |
| 6 | mat_internals | Internals | | |
| 7 | supports | Supports/Saddles | | |
| 8 | gaskets | Gaskets | | |
| 9 | bolts | Bolts | | |

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
