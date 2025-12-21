---
schema_version: 1
template_id: PP-DIAP
title: DIAPHRAGM METERING PUMP
service: CHEMICAL DOSING
has_motor: true
category: pumps
---

# DIAPHRAGM METERING PUMP DATASHEET

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
| 1 | service | Service Description | | | text | |
| 2 | chemical | Chemical Dosed | | | dropdown | ["Sodium Hypochlorite","Ferric Chloride","Alum","Polymer","Caustic Soda","Sulfuric Acid","Lime Slurry","Sodium Bisulfite","PAC","Other"] |
| 3 | concentration | Chemical Concentration | | % | number | |
| 4 | qdesign | Design Flow Rate | | L/h | number | |
| 5 | qmin | Minimum Flow | | L/h | number | |
| 6 | qmax | Maximum Flow | | L/h | number | |
| 7 | num_duty | Number of Duty Pumps | | | number | |
| 8 | num_standby | Number of Standby Pumps | | | number | |
| 9 | discharge_pressure | Maximum Discharge Pressure | | bar | number | |
| 10 | suction_lift | Suction Lift | | m | number | |
| 11 | sg | Specific Gravity | | | number | |
| 12 | temp | Fluid Temperature | | °C | number | |
| 13 | viscosity | Viscosity | | cP | number | |
| 14 | pump_type | Pump Type | | | dropdown | ["Mechanical Diaphragm","Hydraulic Diaphragm","Solenoid","Motor-Driven"] |
| 15 | diaphragm_type | Diaphragm Type | | | dropdown | ["PTFE","PTFE-Backed","Hypalon","EPDM","FKM/Viton"] |
| 16 | stroke_length | Stroke Length Adjustment | | | dropdown | ["Manual 0-100%","Auto 4-20mA","Pulse Input","Profibus"] |
| 17 | stroke_freq | Stroke Frequency Adjustment | | | dropdown | ["Fixed","Manual","VFD","Digital"] |
| 18 | turndown | Turndown Ratio | | | text | |
| 19 | accuracy | Dosing Accuracy | | % | number | |
| 20 | repeatability | Repeatability | | % | number | |
| 21 | suction_valve | Suction Check Valve | | | dropdown | ["Ball","Spring Disc","Cartridge"] |
| 22 | discharge_valve | Discharge Check Valve | | | dropdown | ["Ball","Spring Disc","Cartridge"] |
| 23 | suction_port | Suction Port Size | | mm | number | |
| 24 | discharge_port | Discharge Port Size | | mm | number | |
| 25 | connection_type | Connection Type | | | dropdown | ["Threaded NPT","Threaded BSP","Hose Barb","Tube Fitting"] |
| 26 | pulsation_dampener | Pulsation Dampener | | | dropdown | ["Yes","No"] |
| 27 | relief_valve | Back Pressure/Relief Valve | | | dropdown | ["Yes","No"] |
| 28 | calibration_column | Calibration Column | | | dropdown | ["Yes","No"] |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | head | Pump Head | |
| 2 | diaphragm | Diaphragm | |
| 3 | valves | Check Valves | |
| 4 | valve_balls | Valve Balls | |
| 5 | seals | O-Rings/Seals | |
| 6 | fasteners | Fasteners | 316 SS |

## Driver / Motor Data

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | driver_type | Driver Type | | | dropdown | ["Electric Motor","Solenoid","Pneumatic"] |
| 2 | vfd | VFD Required | | | dropdown | ["Yes","No","N/A"] |
| 3 | mfr | Manufacturer | | | text | |
| 4 | model | Model | | | text | |
| 5 | power | Rated Power | | W | number | |
| 6 | electrical | Voltage / Phase / Hz | | V/Ph/Hz | text | |
| 7 | enclosure | Enclosure Type | | | dropdown | ["TEFC","IP65","IP66","Explosion Proof"] |
| 8 | control_input | Control Input | | | dropdown | ["Manual","4-20mA","Pulse","Modbus","Profibus"] |

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
