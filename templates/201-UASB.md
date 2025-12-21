---
schema_version: 1
template_id: 201-UASB
title: UASB REACTOR
service: ANAEROBIC TREATMENT
has_motor: false
category: secondary_treatment
---

# UASB REACTOR DATASHEET

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
| 1 | reactor_type | Reactor Type | | | dropdown | ["Conventional UASB","EGSB","IC Reactor","Hybrid UASB"] |
| 2 | qavg | Design Average Flow | | m³/h | number | |
| 3 | qpeak | Design Peak Flow | | m³/h | number | |
| 4 | num_reactors | Number of Reactors | | | number | |
| 5 | redundancy | Redundancy Philosophy | | | dropdown | ["N+1","2x50%","2x100%","None"] |
| 6 | cod_in | Inlet COD | | mg/L | number | |
| 7 | cod_out | Target Effluent COD | | mg/L | number | |
| 8 | cod_removal | COD Removal Efficiency | | % | number | |
| 9 | olr | Organic Loading Rate | | kg COD/m³/d | number | |
| 10 | hrt | Hydraulic Retention Time | | hours | number | |
| 11 | upflow_velocity | Upflow Velocity | | m/h | number | |
| 12 | temp_operating | Operating Temperature | | °C | number | |
| 13 | temp_range | Temperature Range | | °C | text | |
| 14 | ph_range | pH Range | | | text | |
| 15 | tss_in | Inlet TSS | | mg/L | number | |
| 16 | reactor_volume | Reactor Volume | | m³ | number | |
| 17 | diameter | Reactor Diameter (if circular) | | m | number | |
| 18 | length | Reactor Length (if rectangular) | | m | number | |
| 19 | width | Reactor Width (if rectangular) | | m | number | |
| 20 | height | Reactor Height | | m | number | |
| 21 | sludge_bed | Sludge Bed Height | | m | number | |
| 22 | gls_separator | GLS Separator Type | | | dropdown | ["Three-Phase","Hybrid Settler","Baffled"] |
| 23 | biogas_rate | Biogas Production Rate | | Nm³/h | number | |
| 24 | biogas_ch4 | Biogas CH4 Content | | % | number | |
| 25 | effluent_type | Effluent Collection | | | dropdown | ["Weir","Launder","Pipe"] |
| 26 | sludge_recycle | Sludge Recirculation | | | dropdown | ["Yes","No"] |
| 27 | heating | Heating Required | | | dropdown | ["Yes - External HX","Yes - Internal","No"] |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | tank | Reactor Tank | |
| 2 | gls | GLS Separator | |
| 3 | feed_dist | Feed Distribution System | |
| 4 | effluent | Effluent Launders/Weirs | |
| 5 | gas_collection | Gas Collection Hood | |
| 6 | internals | Internal Baffles | |
| 7 | piping | Internal Piping | |
| 8 | fasteners | Fasteners | 316 SS |

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
