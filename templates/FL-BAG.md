---
schema_version: 1
template_id: FL-BAG
title: BAG FILTER HOUSING
service: FILTRATION
has_motor: false
category: filtration
---

# BAG FILTER HOUSING DATASHEET

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
| 1 | housing_type | Housing Type | | | dropdown | ["Single Bag","Multi-Bag"] |
| 2 | fluid | Process Fluid | | | text | |
| 3 | flow | Design Flow Rate | | m³/h | number | |
| 4 | flow_max | Maximum Flow Rate | | m³/h | number | |
| 5 | temp_operating | Operating Temperature | | °C | number | |
| 6 | temp_design | Design Temperature | | °C | number | |
| 7 | pressure_operating | Operating Pressure | | bar(g) | number | |
| 8 | pressure_design | Design Pressure | | bar(g) | number | |
| 9 | viscosity | Fluid Viscosity | | cP | number | |
| 10 | sg | Specific Gravity | | | number | |
| 11 | solids_conc | Inlet Solids Concentration | | mg/L | number | |
| 12 | solids_type | Solids Type/Nature | | | text | |
| 13 | micron_rating | Bag Micron Rating | | μm | number | |
| 14 | filter_type | Filter Type | | | dropdown | ["Absolute","Nominal"] |
| 15 | efficiency | Removal Efficiency | | % | number | |
| 16 | dp_clean | Pressure Drop (Clean) | | bar | number | |
| 17 | dp_changeout | Pressure Drop (Changeout) | | bar | number | |
| 18 | num_bags | Number of Bags | | | number | |
| 19 | bag_size | Bag Size | | | dropdown | ["#1 (7\" x 16\")","#2 (7\" x 32\")","#3 (4\" x 8\")","#4 (4\" x 14\")","#5 (6\" x 20\")"] |

## Mechanical Design

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | inlet_location | Inlet Location | | | dropdown | ["Side","Top"] |
| 2 | outlet_location | Outlet Location | | | dropdown | ["Bottom","Side"] |
| 3 | connection_in | Inlet Connection Size | | mm | text | |
| 4 | connection_out | Outlet Connection Size | | mm | text | |
| 5 | connection_type | Connection Type | | | dropdown | ["Flanged","Threaded","Tri-Clamp"] |
| 6 | flange_rating | Flange Rating | | | dropdown | ["PN10","PN16","PN25","150#","300#"] |
| 7 | closure_type | Closure Type | | | dropdown | ["Swing Bolt","Quick-Open","Hinged","Davit Arm"] |
| 8 | basket_type | Basket Type | | | dropdown | ["Perforated","Mesh"] |
| 9 | drain | Drain Connection | | | dropdown | ["Yes","No"] |
| 10 | vent | Vent Connection | | | dropdown | ["Yes","No"] |
| 11 | dp_ports | DP Gauge Ports | | | dropdown | ["Yes","No"] |
| 12 | legs | Support Legs | | | dropdown | ["Yes","No"] |
| 13 | design_code | Design Code | | | dropdown | ["ASME VIII","EN 13445","PD 5500"] |
| 14 | surface_finish | Internal Surface Finish | | Ra μm | number | |
| 15 | weight_empty | Weight (Empty) | | kg | number | |

## Bag Specifications

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | media_type | Filter Media | | | dropdown | ["Polypropylene Felt","Polyester Felt","Nylon Mesh","PTFE Felt","Nomex","Polypropylene Mesh","Oil Absorbing"] |
| 2 | bag_construction | Bag Construction | | | dropdown | ["Sewn","Welded"] |
| 3 | ring_type | Bag Ring Type | | | dropdown | ["Plastic Snap Ring","Stainless Steel Ring","Polypropylene Flange"] |
| 4 | ring_size | Ring Size | | | dropdown | ["Standard","Oversized"] |
| 5 | service_life | Expected Service Life | | weeks | number | |
| 6 | dirt_capacity | Dirt Holding Capacity | | g | number | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | vessel | Vessel/Housing | |
| 2 | cover | Cover/Lid | |
| 3 | basket | Support Basket | |
| 4 | gaskets | Cover Gasket | |
| 5 | fasteners | Fasteners | 316 SS |

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
