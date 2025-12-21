---
schema_version: 1
template_id: 520-ATFD
title: AGITATED THIN FILM DRYER
service: SOLIDS DRYING
has_motor: true
category: brine_management
---

# AGITATED THIN FILM DRYER DATASHEET

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
| Service | Agitated Thin Film Drying |
| Location | |
| Manufacturer | |
| Model | |
| P&ID No | |

## Operating / Design Data

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | application | Application | | | dropdown | ["ZLD Final Drying", "Salt Drying", "Concentrate Drying", "Hazardous Waste"] |
| 2 | dryer_type | Dryer Type | | | dropdown | ["Horizontal ATFD", "Vertical ATFD", "Paddle Dryer"] |
| 3 | feed_type | Feed Type | | | dropdown | ["Slurry", "Filter Cake", "Concentrated Liquor", "Crystals"] |
| 4 | feed_rate | Feed Rate | | kg/h | number | |
| 5 | feed_moisture | Feed Moisture Content | | % wt | number | |
| 6 | feed_solids | Feed Solids Content | | % wt | number | |
| 7 | product_rate | Product Rate | | kg/h | number | |
| 8 | product_moisture | Product Moisture Content | | % wt | number | |
| 9 | evaporation_rate | Evaporation Rate | | kg/h | number | |
| 10 | operating_temp | Operating Temperature | | °C | number | |
| 11 | jacket_temp | Jacket Temperature | | °C | number | |
| 12 | operating_pressure | Operating Pressure | | kPa(abs) | number | |
| 13 | residence_time | Residence Time | | min | number | |
| 14 | heat_duty | Heat Duty | | kW | number | |
| 15 | specific_energy | Specific Energy | | kWh/kg evaporated | number | |
| 16 | heating_medium | Heating Medium | | | dropdown | ["Steam", "Hot Oil", "Hot Water", "Electric"] |
| 17 | steam_pressure | Steam Pressure (if applicable) | | kPa(g) | number | |
| 18 | steam_consumption | Steam Consumption | | kg/h | number | |

## Mechanical Design

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | body_diameter | Body Diameter | | mm | number | |
| 2 | body_length | Body Length | | mm | number | |
| 3 | heat_transfer_area | Heat Transfer Area | | m² | number | |
| 4 | rotor_type | Rotor Type | | | dropdown | ["Fixed Blade", "Hinged Blade", "Adjustable Blade"] |
| 5 | rotor_speed | Rotor Speed | | RPM | number | |
| 6 | tip_speed | Blade Tip Speed | | m/s | number | |
| 7 | blade_clearance | Blade-Wall Clearance | | mm | number | |
| 8 | num_blades | Number of Blades | | | number | |
| 9 | film_thickness | Nominal Film Thickness | | mm | number | |
| 10 | design_pressure | Design Pressure (jacket) | | kPa(g) | number | |
| 11 | design_temp | Design Temperature | | °C | number | |

## Vapor Handling

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | vapor_flow | Vapor Flow Rate | | kg/h | number | |
| 2 | vapor_outlet_size | Vapor Outlet Size | | mm | number | |
| 3 | demister | Demister Type | | | dropdown | ["Mesh Pad", "Cyclone", "Vane", "None"] |
| 4 | condenser | Condenser Type | | | dropdown | ["Shell & Tube", "Plate", "Air Cooled", "Direct Contact"] |
| 5 | vacuum_system | Vacuum System | | | dropdown | ["Steam Ejector", "Liquid Ring", "Dry Pump", "N/A"] |

## Product Discharge

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | discharge_type | Discharge Type | | | dropdown | ["Screw", "Rotary Valve", "Double Dump Valve", "Gravity"] |
| 2 | cooling | Product Cooling | | | dropdown | ["Integral", "Separate Cooler", "None"] |
| 3 | packaging | Product Packaging | | | dropdown | ["Bulk Bag", "Drum", "Conveyor", "Silo"] |

## Materials

| # | field_id | Component | Material |
|---|----------|-----------|----------|
| 1 | body | Dryer Body | |
| 2 | jacket | Heating Jacket | |
| 3 | rotor | Rotor/Shaft | |
| 4 | blades | Blades | |
| 5 | seals | Shaft Seals | |
| 6 | discharge | Discharge System | |
| 7 | fasteners | Fasteners | 316 SS |

## Driver / Motor Data

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | main_drive | Main Drive Motor Power | | kW | number | |
| 2 | discharge_drive | Discharge Drive Motor Power | | kW | number | |
| 3 | vacuum_pump_power | Vacuum Pump Motor Power | | kW | number | |
| 4 | total_power | Total Connected Power | | kW | number | |
| 5 | mtr_voltage | Motor Voltage / Phase / Hz | | V/Ph/Hz | text | |
| 6 | mtr_enclosure | Motor Enclosure Type | | | dropdown | ["TEFC", "TENV", "Explosion Proof"] |
| 7 | mtr_eff | Motor Efficiency Class | | | dropdown | ["IE1", "IE2", "IE3", "IE4"] |
| 8 | vfd | VFD on Main Drive | | | dropdown | ["Yes", "No"] |
| 9 | gear_type | Gear Reducer Type | | | dropdown | ["Helical", "Planetary", "Cycloidal"] |

## Safety

| # | field_id | Field | Value | Units | Type | Options |
|---|----------|-------|-------|-------|------|---------|
| 1 | atex | ATEX Zone | | | dropdown | ["Zone 0", "Zone 1", "Zone 2", "Non-Hazardous"] |
| 2 | inerting | Inert Gas Blanketing | | | dropdown | ["Nitrogen", "None"] |
| 3 | rupture_disc | Rupture Disc | | | dropdown | ["Yes", "No"] |

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
