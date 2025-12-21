---
schema_version: 1
template_id: FL-AUTO
title: AUTOMATIC SELF-CLEANING STRAINER
service: STRAINING
has_motor: true
category: filtration
---

# AUTOMATIC SELF-CLEANING STRAINER DATASHEET

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
| 1 | strainer_type | Strainer Type | | | dropdown | ["Brush Type","Suction Scanner","Disc Type","Backwash"] |
| 2 | fluid | Process Fluid | | | text | |
| 3 | flow | Design Flow Rate | | m³/h | number | |
| 4 | flow_max | Maximum Flow Rate | | m³/h | number | |
| 5 | flow_min | Minimum Flow Rate | | m³/h | number | |
| 6 | temp_operating | Operating Temperature | | °C | number | |
| 7 | temp_design | Design Temperature | | °C | number | |
| 8 | pressure_operating | Operating Pressure | | bar(g) | number | |
| 9 | pressure_design | Design Pressure | | bar(g) | number | |
| 10 | pressure_min | Minimum Operating Pressure | | bar(g) | number | |
| 11 | viscosity | Fluid Viscosity | | cP | number | |
| 12 | sg | Specific Gravity | | | number | |
| 13 | solids_conc | Inlet Solids Concentration | | mg/L | number | |
| 14 | solids_size | Solids Particle Size Range | | μm | text | |
| 15 | solids_type | Solids Type/Nature | | | text | |
| 16 | micron_rating | Screen Micron Rating | | μm | number | |
| 17 | screen_area | Screen Filter Area | | m² | number | |
| 18 | dp_clean | Pressure Drop (Clean) | | bar | number | |
| 19 | dp_backwash | Backwash Trigger DP | | bar | number | |
| 20 | dp_max | Maximum Allowable DP | | bar | number | |

## Backwash / Cleaning Data

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | cleaning_trigger | Cleaning Trigger | | | dropdown | ["DP","Timer","Manual","DP + Timer"] |
| 2 | backwash_flow | Backwash Flow Rate | | m³/h | number | |
| 3 | backwash_duration | Backwash Duration | | seconds | number | |
| 4 | backwash_freq | Typical Backwash Frequency | | cycles/day | number | |
| 5 | water_loss | Water Loss per Backwash | | L | number | |
| 6 | flush_pressure | Minimum Flush Pressure | | bar(g) | number | |
| 7 | flush_connection | Flush Discharge Connection | | mm | text | |
| 8 | continuous_operation | Continuous Filtration During Cleaning | | | dropdown | ["Yes","No"] |

## Mechanical Design

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | screen_type | Screen Type | | | dropdown | ["Wedge Wire","Perforated","Woven Mesh","Sintered"] |
| 2 | screen_shape | Screen Shape | | | dropdown | ["Cylindrical","Disc","Conical"] |
| 3 | connection_in | Inlet Connection Size | | mm | text | |
| 4 | connection_out | Outlet Connection Size | | mm | text | |
| 5 | connection_drain | Drain Connection Size | | mm | text | |
| 6 | connection_type | Connection Type | | | dropdown | ["Flanged","Wafer","Buttweld"] |
| 7 | flange_rating | Flange Rating | | | dropdown | ["PN10","PN16","PN25","PN40","150#","300#"] |
| 8 | orientation | Installation Orientation | | | dropdown | ["Horizontal","Vertical"] |
| 9 | design_code | Design Code | | | dropdown | ["ASME VIII","EN 13445","PD 5500"] |
| 10 | weight_empty | Weight (Empty) | | kg | number | |
| 11 | weight_operating | Weight (Operating) | | kg | number | |

## Driver / Motor Data

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | drive_type | Drive Type | | | dropdown | ["Electric Motor","Hydraulic","Pneumatic"] |
| 2 | motor_power | Motor Power | | kW | number | |
| 3 | electrical | Voltage / Phase / Hz | | V/Ph/Hz | text | |
| 4 | enclosure | Motor Enclosure | | | dropdown | ["TEFC","ODP","Explosion Proof"] |
| 5 | ip_rating | IP Rating | | | dropdown | ["IP55","IP65","IP66","IP67"] |
| 6 | actuator_type | Actuator Type | | | text | |
| 7 | actuator_torque | Actuator Torque | | Nm | number | |

## Control / Instrumentation

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | control_panel | Control Panel | | | dropdown | ["Integral","Remote","Customer Supplied"] |
| 2 | dp_transmitter | DP Transmitter | | | dropdown | ["Included","Customer Supplied","Not Required"] |
| 3 | position_indicator | Cleaning Position Indicator | | | dropdown | ["Yes","No"] |
| 4 | signal_output | Signal Output | | | dropdown | ["4-20mA","Modbus","Dry Contact","Profibus"] |
| 5 | power_supply | Control Power Supply | | V | text | |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | body | Body/Housing | |
| 2 | cover | Cover | |
| 3 | screen | Screen Element | |
| 4 | cleaning_mechanism | Cleaning Mechanism | |
| 5 | seals | Seals | |
| 6 | fasteners | Fasteners | 316 SS |

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
