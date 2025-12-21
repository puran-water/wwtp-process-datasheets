---
schema_version: 1
template_id: FL-CART
title: CARTRIDGE FILTER HOUSING
service: FILTRATION
has_motor: false
category: filtration
---

# CARTRIDGE FILTER HOUSING DATASHEET

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
| 1 | housing_type | Housing Type | | | dropdown | ["Single Cartridge","Multi-Cartridge","High Flow"] |
| 2 | flow_direction | Flow Direction | | | dropdown | ["Outside-In","Inside-Out"] |
| 3 | fluid | Process Fluid | | | text | |
| 4 | flow | Design Flow Rate | | m³/h | number | |
| 5 | flow_max | Maximum Flow Rate | | m³/h | number | |
| 6 | temp_operating | Operating Temperature | | °C | number | |
| 7 | temp_design | Design Temperature | | °C | number | |
| 8 | pressure_operating | Operating Pressure | | bar(g) | number | |
| 9 | pressure_design | Design Pressure | | bar(g) | number | |
| 10 | viscosity | Fluid Viscosity | | cP | number | |
| 11 | sg | Specific Gravity | | | number | |
| 12 | solids_conc | Inlet Solids Concentration | | mg/L | number | |
| 13 | micron_rating | Cartridge Micron Rating | | μm | number | |
| 14 | filter_type | Filter Type | | | dropdown | ["Absolute","Nominal"] |
| 15 | beta_ratio | Beta Ratio | | | number | |
| 16 | dp_clean | Pressure Drop (Clean) | | bar | number | |
| 17 | dp_changeout | Pressure Drop (Changeout) | | bar | number | |
| 18 | num_cartridges | Number of Cartridges | | | number | |
| 19 | cartridge_length | Cartridge Length | | mm | dropdown | ["250 (10\")","500 (20\")","750 (30\")","1000 (40\")"] |
| 20 | cartridge_od | Cartridge Outside Diameter | | mm | number | |
| 21 | adapter_type | Cartridge Adapter | | | dropdown | ["DOE","SOE 222","SOE 226","Code 7","Bayonet"] |

## Mechanical Design

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | connection_in | Inlet Connection Size | | mm | text | |
| 2 | connection_out | Outlet Connection Size | | mm | text | |
| 3 | connection_type | Connection Type | | | dropdown | ["Flanged","Threaded","Tri-Clamp"] |
| 4 | flange_rating | Flange Rating | | | dropdown | ["PN10","PN16","PN25","PN40","150#","300#"] |
| 5 | closure_type | Closure Type | | | dropdown | ["Swing Bolt","Quick-Open","V-Clamp","Threaded"] |
| 6 | drain | Drain Connection | | | dropdown | ["Yes","No"] |
| 7 | vent | Vent Connection | | | dropdown | ["Yes","No"] |
| 8 | dp_ports | DP Gauge Ports | | | dropdown | ["Yes","No"] |
| 9 | design_code | Design Code | | | dropdown | ["ASME VIII","EN 13445","PD 5500"] |
| 10 | surface_finish | Internal Surface Finish | | Ra μm | number | |
| 11 | weight_empty | Weight (Empty) | | kg | number | |

## Cartridge Specifications

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | media_type | Filter Media | | | dropdown | ["Pleated Polypropylene","Melt Blown PP","Pleated Polyester","Pleated PTFE","Pleated Glass Fiber","Activated Carbon","String Wound","Ceramic"] |
| 2 | core_material | Core Material | | | dropdown | ["Polypropylene","Stainless Steel","None"] |
| 3 | cage_material | Outer Cage Material | | | dropdown | ["Polypropylene","Stainless Steel","None"] |
| 4 | end_cap | End Cap Material | | | dropdown | ["Polypropylene","Stainless Steel","Buna-N"] |
| 5 | gasket_material | Gasket Material | | | dropdown | ["Buna-N","EPDM","Silicone","Viton","PTFE"] |
| 6 | service_life | Expected Service Life | | months | number | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | vessel | Vessel/Housing | |
| 2 | cover | Cover/Head | |
| 3 | internals | Internals/Tie Rods | |
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
