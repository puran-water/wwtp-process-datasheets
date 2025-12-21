# Blowers datasheet guidance

Covers: BL-PD (Positive Displacement), BL-TURBO (High-Speed Turbo), BL-CENT (Multi-Stage Centrifugal), BL-REGEN (Regenerative)

## What to decide up front

**1) Blower type selection**

| Application | Flow Range | Pressure | Recommended Type |
|-------------|------------|----------|------------------|
| Aeration (small) | <500 Nm³/h | 40-80 kPa | PD or Regenerative |
| Aeration (medium) | 500-5000 Nm³/h | 40-80 kPa | PD or Turbo |
| Aeration (large) | >5000 Nm³/h | 40-80 kPa | Multi-stage or Turbo |
| MBR air scour | Variable | 30-50 kPa | Turbo (wide turndown) |
| Low pressure | Any | <40 kPa | Regenerative |
| Pneumatic conveying | Variable | 50-100 kPa | PD |

**2) Positive displacement types**
- **Rotary lobe (Roots)**: 2 or 3 lobe, standard
- **Rotary screw (dry)**: higher efficiency, quieter
- **Rotary screw (oil-flooded)**: not for aeration (oil contamination)

**3) Turndown requirements**
- **Fixed speed PD**: limited turndown, uses inlet throttle or bypass
- **VFD PD**: 50-100% typical range
- **Turbo blowers**: 50-100% via IGV + VFD, excellent turndown
- **Multi-stage centrifugal**: inlet guide vanes, 60-100%

**4) Acoustic requirements**
- Inlet/outlet silencers
- Acoustic enclosure
- Building placement
- Noise limit at property line

## Process data that drives the quote

### Air flow requirements
- Design air flow (Nm³/h or SCFM)
- Normal operating range
- Turndown requirement (%)
- Future expansion allowance

### Pressure requirements
- System pressure loss (piping, diffusers, submergence)
- Submergence depth (m) × 9.81 = static head (kPa)
- Dynamic losses through piping and diffusers
- Design discharge pressure (kPa gauge)

### Site conditions
- Altitude above sea level
- Ambient temperature range
- Relative humidity
- Inlet filter requirements

### Power and efficiency
- Motor power (kW)
- Specific power: kW per 1000 Nm³/h
- Wire-to-air efficiency (for turbo)
- Annual energy cost impact

### Controls
- DO-based modulation
- Most-open-valve control
- Load sharing (multiple blowers)
- Common header pressure control

## Mechanical / design interface items

- **Inlet filter/silencer**: size, maintenance access
- **Discharge silencer**: noise attenuation
- **Check valve**: prevent backflow on shutdown
- **Pressure relief valve**: overpressure protection
- **Flexible connections**: vibration isolation
- **Base and vibration isolation**: concrete pad, spring mounts
- **Enclosure**: acoustic, weather protection
- **Cooling**: air-cooled (standard), water-cooled (high pressure)

## Comparison table

| Feature | PD Lobe | PD Screw | Turbo | Multi-stage |
|---------|---------|----------|-------|-------------|
| Efficiency | 60-70% | 70-80% | 75-85% | 70-80% |
| Turndown | 50-100% | 40-100% | 50-100% | 60-100% |
| Oil-free | Yes | Dry only | Yes | Yes |
| Noise | High | Medium | Low | Medium |
| Maintenance | Medium | Low | Low | Medium |
| Capital cost | Low | Medium | High | Medium |

## What to attach with the datasheet

- Aeration system design calculations
- Site layout showing blower building
- Noise survey requirements
- Electrical supply and building HVAC
- Future expansion plans
