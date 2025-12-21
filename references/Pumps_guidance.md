# Pumps datasheet guidance

Covers: PP-CEN (Centrifugal), PP-PCP (Progressive Cavity), PP-SUB (Submersible), PP-HP (High Pressure), PP-DIAP (Diaphragm), PP-LOBE (Rotary Lobe), PP-VERT (Vertical Turbine), PP-SCREW (Screw), PP-PERI (Peristaltic), PP-GEAR, PP-CIP, PP-AIRLIFT

## What to decide up front

**1) Pump type selection**

| Application | Recommended Type |
|-------------|------------------|
| Clean water transfer | Centrifugal (PP-CEN) |
| RAS/WAS/sludge | Progressive cavity (PP-PCP), Rotary lobe (PP-LOBE) |
| Wet well | Submersible (PP-SUB), Vertical turbine (PP-VERT) |
| High pressure (RO, filter) | Multistage centrifugal (PP-HP) |
| Chemical dosing | Diaphragm metering (PP-DIAP), Peristaltic (PP-PERI) |
| Scum, thick sludge | Rotary lobe (PP-LOBE), Progressive cavity (PP-PCP) |
| Grit slurry | Recessed impeller, vortex |

**2) Drive configuration**
- **Direct coupled**: compact, alignment critical
- **Belt driven**: speed adjustment, vibration isolation
- **VFD**: variable speed, most flexible
- **Close-coupled**: motor-pump integral (vertical inline)

**3) Seal type (for centrifugal)**
- **Packed gland**: simple, requires adjustment
- **Mechanical seal**: standard, various arrangements
- **Double mechanical**: hazardous/expensive fluids
- **Sealless (mag-drive)**: zero leakage

## Process data that drives the quote

### Hydraulic requirements
- Design flow rate (m³/h or L/s)
- Total dynamic head (m or kPa)
- Suction conditions (flooded or lift)
- NPSHa (Net Positive Suction Head available)

### Fluid characteristics
- Liquid type (water, sludge, chemical)
- Temperature range
- Specific gravity
- Solids content (% TS for sludge)
- Particle size (for solids-handling)
- Viscosity
- Corrosivity / pH

### Operating conditions
- Continuous or intermittent duty
- Starts per hour
- Turndown requirements
- Parallel operation requirements

### For positive displacement pumps
- Viscosity at operating temperature
- Shear sensitivity
- Pulsation requirements
- Relief valve settings

### For metering pumps
- Dose rate range (mL/min to L/h)
- Accuracy requirement (typically ±1-2%)
- Turndown ratio
- Chemical compatibility

## Mechanical / design interface items

- **Materials**: impeller, casing, shaft, wear rings
- **Mounting**: baseplate, grout, vibration isolation
- **Piping**: suction, discharge, bypass, drain
- **Instrumentation**: pressure, flow, vibration, seal leak
- **Controls**: level, flow pacing, interlock with process
- **VFD**: enclosure, bypass, harmonics

## Standard selections by application

| Service | Type | Typical Materials |
|---------|------|-------------------|
| Raw sewage | Submersible, solids-handling | Cast iron, 316 SS |
| RAS | Progressive cavity | 316 SS stator, chrome rotor |
| WAS | Rotary lobe | 316 SS, hard-coated lobes |
| Chemical (NaOH) | Centrifugal | 316 SS, Alloy 20 |
| Chemical (acid) | Centrifugal | Hastelloy, PVDF-lined |
| Polymer | Peristaltic, progressive cavity | Rubber hose/stator |
| RO feed | Multistage horizontal | Duplex SS |

## What to attach with the datasheet

- System curve or head calculation
- P&ID showing pump context
- Process design basis (flows, solids)
- Electrical supply available
- Existing equipment (for replacement/matching)
