---
schema_version: 1
template_id: 250-XMBR
title: CROSSFLOW MBR SKID
service: EXTERNAL MEMBRANE BIOREACTOR
has_motor: true
category: secondary_treatment
---

# CROSSFLOW MBR SKID DATASHEET

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
| 1 | mem_config | Membrane Configuration | | | dropdown | ["Tubular","Hollow Fiber","Spiral Wound"] |
| 2 | qavg | Design Average Permeate Flow | | m³/h | number | |
| 3 | qpeak | Design Peak Permeate Flow | | m³/h | number | |
| 4 | num_skids | Number of Membrane Skids | | | number | |
| 5 | modules_per_skid | Modules per Skid | | | number | |
| 6 | redundancy | Redundancy Philosophy | | | dropdown | ["N+1","2x50%","None"] |
| 7 | material | Membrane Material | | | dropdown | ["PVDF","PES","Ceramic","PTFE"] |
| 8 | tube_diameter | Tube/Fiber Diameter | | mm | number | |
| 9 | pore_size | Nominal Pore Size | | μm | number | |
| 10 | area_per_module | Membrane Area per Module | | m² | number | |
| 11 | total_area | Total Installed Membrane Area | | m² | number | |
| 12 | design_flux | Design Net Flux | | LMH | number | |
| 13 | peak_flux | Peak Net Flux | | LMH | number | |
| 14 | crossflow_velocity | Crossflow Velocity | | m/s | number | |
| 15 | recirculation_flow | Recirculation Flow | | m³/h | number | |
| 16 | tmp_operating | Operating TMP | | bar | number | |
| 17 | tmp_max | Maximum TMP | | bar | number | |
| 18 | feed_pressure | Feed Pressure | | bar(g) | number | |
| 19 | mlss_design | Design MLSS | | mg/L | number | |
| 20 | mlss_max | Maximum MLSS | | mg/L | number | |
| 21 | temp_design | Design Temperature | | °C | number | |
| 22 | temp_range | Operating Temperature Range | | °C | text | |
| 23 | backwash | Backwash System | | | dropdown | ["Air Backwash","Permeate Backwash","None"] |
| 24 | cip_system | CIP System | | | dropdown | ["Integral","External","None"] |
| 25 | cip_tank | CIP Tank Volume | | L | number | |
| 26 | cip_chem | CIP Chemicals | | | dropdown | ["NaOCl","Citric Acid","NaOCl + Citric","NaOH","Other"] |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | membrane | Membrane | |
| 2 | housing | Module Housing | |
| 3 | skid_frame | Skid Frame | |
| 4 | piping | Piping | |
| 5 | valves | Valves | |
| 6 | instruments | Instruments | |
| 7 | fasteners | Fasteners | 316 SS |

## Driver / Motor Data

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | driver_type | Driver Type | | | dropdown | ["Electric Motor"] |
| 2 | application | Motor Application | | | dropdown | ["Recirculation Pump","Feed Pump","Both"] |
| 3 | num_pumps | Number of Pumps | | | number | |
| 4 | vfd | VFD Required | | | dropdown | ["Yes","No"] |
| 5 | mfr | Motor Manufacturer | | | text | |
| 6 | model | Motor Model | | | text | |
| 7 | power | Motor Rated Power (each) | | kW | number | |
| 8 | electrical | Voltage / Phase / Hz | | V/Ph/Hz | text | |
| 9 | enclosure | Enclosure Type | | | dropdown | ["TEFC","ODP","TENV"] |
| 10 | insulation | Insulation Class | | | dropdown | ["B","F","H"] |
| 11 | efficiency | Efficiency Class | | | dropdown | ["IE1","IE2","IE3","IE4"] |

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
