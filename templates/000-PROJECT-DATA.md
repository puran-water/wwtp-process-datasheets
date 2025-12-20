---
schema_version: 1
template_id: 000-PROJECT-DATA
title: PROJECT DATA
service: MASTER PROJECT INFORMATION
has_motor: false
category: project
---

# PROJECT DATA DATASHEET

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
| Service | MASTER PROJECT INFORMATION |
| Location | |
| Manufacturer | |
| Model | |
| P&ID No | |

## Operating / Design Data

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | project_name | Project Name | | | text | |
| 2 | project_number | Project Number | | | text | |
| 3 | client | Client Name | | | text | |
| 4 | location | Site Location | | | text | |
| 5 | design_pop | Design Population | | PE | number | |
| 6 | qavg | Design Average Flow (Qavg) | | m³/d | number | |
| 7 | qpeak_day | Design Peak Day Flow | | m³/d | number | |
| 8 | qpeak_hour | Design Peak Hour Flow | | m³/h | number | |
| 9 | pf_daily | Daily Peaking Factor | | | number | |
| 10 | pf_hourly | Hourly Peaking Factor | | | number | |
| 11 | temp_min | Minimum Wastewater Temperature | | °C | number | |
| 12 | temp_max | Maximum Wastewater Temperature | | °C | number | |
| 13 | ambient_min | Minimum Ambient Temperature | | °C | number | |
| 14 | ambient_max | Maximum Ambient Temperature | | °C | number | |
| 15 | elevation | Site Elevation | | m | number | |
| 16 | seismic | Seismic Zone | | | text | |
| 17 | voltage | Electrical Service Voltage | | V | text | |
| 18 | phases | Electrical Phases | | | dropdown | ["1","3"] |
| 19 | frequency | Electrical Frequency | | Hz | dropdown | ["50","60"] |
| 20 | controls | Controls Protocol | | | dropdown | ["Modbus","Ethernet/IP","Profinet","Hardwired"] |
| 21 | design_code | Design Code / Standard | | | text | |
| 22 | permit_ref | Permit Reference | | | text | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | default_wetted | Default Wetted Metal | 316 SS |
| 2 | default_structural | Default Structural Metal | Carbon Steel |
| 3 | default_fasteners | Default Fasteners | 316 SS |
| 4 | concrete | Concrete Protection | |
| 5 | coatings | Coating System | |

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
