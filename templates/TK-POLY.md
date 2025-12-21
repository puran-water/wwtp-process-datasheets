---
schema_version: 1
template_id: TK-POLY
title: POLYETHYLENE STORAGE TANK
service: CHEMICAL STORAGE
has_motor: false
category: tanks
---

# POLYETHYLENE STORAGE TANK DATASHEET

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
| 1 | fluid | Fluid Stored | | | dropdown | ["Sodium Hypochlorite","Sodium Hydroxide","Sulfuric Acid","Ferric Chloride","Alum","Polymer","Sodium Bisulfite","PAC","Citric Acid","Other"] |
| 2 | concentration | Concentration | | % | number | |
| 3 | volume_nominal | Nominal Volume | | L | number | |
| 4 | volume_working | Working Volume | | L | number | |
| 5 | sg | Specific Gravity | | | number | |
| 6 | temp_operating | Operating Temperature | | °C | number | |
| 7 | temp_max | Maximum Temperature | | °C | number | |
| 8 | pressure | Tank Pressure | | | dropdown | ["Atmospheric","Vented"] |
| 9 | pe_type | Polyethylene Type | | | dropdown | ["HDPE","XLPE","LLDPE"] |
| 10 | uv_stabilized | UV Stabilized | | | dropdown | ["Yes","No"] |
| 11 | color | Tank Color | | | dropdown | ["Natural","Black","Yellow","Blue","White"] |
| 12 | diameter | Tank Diameter | | mm | number | |
| 13 | height | Tank Height | | mm | number | |
| 14 | orientation | Orientation | | | dropdown | ["Vertical","Horizontal"] |
| 15 | mounting | Mounting | | | dropdown | ["Flat Bottom","Dished Bottom","Conical Bottom","Legs"] |
| 16 | wall_thickness | Wall Thickness | | mm | number | |
| 17 | containment | Secondary Containment | | | dropdown | ["Bund","Double Wall","None"] |
| 18 | top_opening | Top Opening Size | | mm | number | |
| 19 | level_indicator | Level Indicator | | | dropdown | ["Visual Scale","Ultrasonic","Float","None"] |
| 20 | vent | Tank Vent | | | dropdown | ["Open Vent","PV Valve","Desiccant Breather"] |

## Fittings / Nozzles

| # | field_id | Service | Size | Type | Location |
|---|----------|---------|------|------|----------|
| 1 | inlet | Inlet | | | |
| 2 | outlet | Outlet | | | |
| 3 | drain | Drain | | | |
| 4 | overflow | Overflow | | | |
| 5 | vent | Vent | | | |
| 6 | level | Level Connection | | | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | tank | Tank Body | |
| 2 | fittings | Fittings | |
| 3 | gaskets | Gaskets | |
| 4 | bolts | Bolts | |

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
