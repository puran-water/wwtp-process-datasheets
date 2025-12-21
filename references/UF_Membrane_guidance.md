# UF (Ultrafiltration) Membrane datasheet guidance

Covers: 320-UF (submerged), 320-PUF (pressurized)

## What to decide up front

**1) Configuration**
- **Submerged/immersed**: membranes in tank, vacuum-driven, lower pressure
- **Pressurized/enclosed**: membranes in housing, pump-driven, higher flux

**2) Membrane geometry**
- **Hollow fiber (outside-in)**: most common for submerged
- **Hollow fiber (inside-out)**: for pressurized systems
- **Tubular**: high-solids applications

**3) Application**
- **Tertiary filtration**: polishing secondary effluent for reuse
- **Pretreatment to RO**: SDI reduction
- **Direct filtration**: surface water treatment
- **MBR**: see MBR_guidance.md

**4) Membrane material**
- **PVDF**: chemical resistant, standard choice
- **PES**: lower cost, less chemical resistance
- **Ceramic**: extreme durability, highest cost

## Process data that drives the quote

### Hydraulic design
- Design average flow (m³/h)
- Design peak flow (m³/h)
- Recovery rate: typically 90-95%
- Backwash/CEB water volume

### Membrane sizing
- Net flux: 40-80 LMH typical for tertiary (higher than MBR)
- Instantaneous flux: including backwash periods
- Membrane area required (m²)
- Number of modules/racks

### Feed water quality
- TSS (mg/L): typically <50 for pressurized, <200 for submerged
- Turbidity (NTU)
- SDI (for RO pretreatment applications)
- Iron, manganese (fouling potential)
- Organics (DOC, UV254)

### Operating parameters
- TMP: 10-50 kPa (submerged), 50-200 kPa (pressurized)
- Backwash frequency: every 15-60 minutes
- Backwash duration: 30-60 seconds
- Air scour (submerged): 0.3-1.0 Nm³/h per m²

## Mechanical / design interface items

- **Feed pumps**: sized for peak flow plus recirculation
- **Permeate/filtrate pumps**: for submerged systems
- **Air scour blowers**: for submerged systems
- **Backwash system**: clean water source, pumps
- **CIP system**: chemical storage, dosing, heating
- **Pretreatment**: strainer (100-500 μm) upstream

## Cleaning requirements

- **Maintenance clean (CEB)**: daily, NaOCl or acid
- **Recovery clean (CIP)**: monthly, intensive chemical soak
- **Chemicals**: NaOCl, citric acid, NaOH, specialty cleaners

## What to attach with the datasheet

- Feed water analysis
- Effluent quality requirements (TSS, turbidity, SDI)
- Site layout and footprint constraints
- Chemical availability and storage constraints
