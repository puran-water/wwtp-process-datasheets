---
schema_version: 1
template_id: MX-STATIC
title: STATIC MIXER
service: INLINE MIXING
has_motor: false
category: mixers
---

# STATIC MIXER DATASHEET

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
| 1 | service_type | Service Type | | | dropdown | ["Chemical Injection","Coagulant Mixing","Polymer Dilution","pH Adjustment","Chlorine Mixing","Dechlorination"] |
| 2 | num_units | Number of Units | | | number | |
| 3 | main_flow | Main Flow Rate | | m³/h | number | |
| 4 | main_flow_min | Minimum Main Flow | | m³/h | number | |
| 5 | main_flow_max | Maximum Main Flow | | m³/h | number | |
| 6 | main_fluid | Main Fluid | | | dropdown | ["Raw Water","Treated Water","Effluent","Sludge"] |
| 7 | additive_fluid | Additive Fluid | | | dropdown | ["Coagulant","Polymer","Caustic","Acid","Chlorine","Sodium Bisulfite"] |
| 8 | additive_flow | Additive Flow Rate | | L/h | number | |
| 9 | dilution_ratio | Dilution Ratio | | | text | |
| 10 | sg | Main Fluid Specific Gravity | | | number | |
| 11 | viscosity | Main Fluid Viscosity | | cP | number | |
| 12 | temp | Fluid Temperature | | °C | number | |
| 13 | temp_max | Maximum Temperature | | °C | number | |
| 14 | pressure_design | Design Pressure | | bar | number | |
| 15 | pressure_drop | Pressure Drop at Design Flow | | bar | number | |
| 16 | element_type | Element Type | | | dropdown | ["Helical","Tab","Corrugated Plate","Blade","SMX"] |
| 17 | num_elements | Number of Elements | | | number | |
| 18 | mixer_diameter | Mixer Diameter | | mm | number | |
| 19 | mixer_length | Overall Length | | mm | number | |
| 20 | inlet_connection | Inlet Connection Size | | mm | number | |
| 21 | outlet_connection | Outlet Connection Size | | mm | number | |
| 22 | injection_port | Injection Port Size | | mm | number | |
| 23 | connection_type | Connection Type | | | dropdown | ["Flanged","Threaded","Butt Weld","Tri-Clamp"] |
| 24 | flange_rating | Flange Rating | | | dropdown | ["PN10","PN16","PN25","150#","300#"] |
| 25 | cov | Coefficient of Variation (CoV) | | | number | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | housing | Housing/Body | |
| 2 | elements | Mixing Elements | |
| 3 | flanges | Flanges | |
| 4 | gaskets | Gaskets | |
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
