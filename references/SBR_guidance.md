# SBR (Sequencing Batch Reactor) datasheet guidance

Covers: 280-SBR, 280-DEC

## What to decide up front

**1) Number of basins**
- Minimum 2 basins for continuous flow acceptance
- 3+ basins for operational flexibility
- Basin sizing for batch volume

**2) Cycle configuration**
- **Fill**: static, mixed, or aerated fill
- **React**: aerated (aerobic), mixed (anoxic), or static (anaerobic)
- **Settle**: quiescent settling
- **Decant**: effluent withdrawal
- **Idle**: optional, for sludge wasting

**3) Decanter type**
- **Floating weir**: follows water surface, most common
- **Fixed weir with adjustable level**: simpler mechanism
- **Submerged trough**: less scum carryover

**4) Nutrient removal configuration**
- **BOD only**: aerobic react only
- **Nitrification**: extended aerobic react
- **Denitrification**: anoxic react period
- **Enhanced P removal**: anaerobic fill + aerobic react

## Process data that drives the quote

### Hydraulic design
- Design average flow (m³/d)
- Design peak flow (m³/h)
- Number of cycles per day: typically 4-6
- Batch volume and decant volume

### Biological design
- Influent BOD/COD (mg/L)
- TKN, ammonia, TP if nutrient removal required
- MLSS target: 2,000-4,000 mg/L
- SRT: 10-30 days depending on process goals
- F/M ratio

### Tank sizing
- Total volume per basin (m³)
- Operating depth range (min/max)
- Length × width dimensions
- Freeboard requirements

### Aeration requirements
- Oxygen demand (kg O₂/d)
- Aeration type: fine bubble diffusers or mechanical
- Blower sizing: air flow and pressure

## Mechanical / design interface items

- **Decanter mechanism**: travel distance, rate, motor/actuator
- **Mixers**: submersible or top-entry, for anoxic periods
- **Diffuser grid**: retractable or fixed, drain-down capability
- **Blowers**: sized for peak demand, variable speed
- **WAS pumps**: intermittent operation, solids handling
- **Controls**: PLC with cycle programming, DO control

## Operations considerations

- Cycle time optimization
- Settleability monitoring (SVI)
- Decant rate vs TSS carryover
- Scum management
- Cold weather operation

## What to attach with the datasheet

- Process design basis with nutrient limits
- Basin layout and dimensions
- Cycle time programming requirements
- Effluent permit limits
