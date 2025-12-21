---
schema_version: 1
template_id: TEST-01
title: TEST EQUIPMENT
service: TEST SERVICE
has_motor: true
category: test
---

# TEST EQUIPMENT DATASHEET

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
| Service | TEST SERVICE |
| Location | |
| Manufacturer | |
| Model | |
| P&ID No | |

## Operating / Design Data

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | qavg | Design Average Flow | | m3/h | number | |
| 2 | qph | Design Peak Flow | | m3/h | number | |
| 3 | redundancy | Redundancy | | | dropdown | ["N+1","2x50%"] |
| 4 | bypass | Bypass Required | | | dropdown | ["Yes","No"] |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | tank | Tank | 316 SS |
| 2 | wetted | Wetted Parts | 316 SS |

## Driver / Motor Data

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | motor_power | Rated Power | | kW | number | |
| 2 | motor_voltage | Voltage | | V | text | |

## Remarks

| # | Remark |
|---|--------|
| 1 | |

## Revision History

| Rev | Date | Description | By |
|-----|------|-------------|-----|
| 0 | | Initial release | |
