# Grit removal package datasheet guidance

## What to decide up front

**1) Technology class**
- **Aerated grit chamber** (rectangular, air-induced spiral roll)
- **Vortex / forced vortex** (hydraulic or mechanical)
- **Horizontal grit chamber / detritor**
- If you don’t know yet, leave “technology preference” as “Vendor to propose”.

**2) What is “grit” for this project**
Municipal headworks grit behaves differently from industrial sand/scale.
If you have any grit study or gradation data, include it.

**3) Package boundaries**
Confirm whether you want:
- grit separation only, or
- separation + washing/classification + dewatering + conveying to dumpster,
- plus odor control, washwater recycle, or HVAC/enclosure.

## Process data that drives the quote

### Flow basis (must be explicit)
At minimum:
- Average flow
- Peak hour flow
- Peak day / wet weather flow
- Minimum / overnight flow (turndown)

Also define:
- number of duty trains and redundancy (N, N+1)
- whether peak flow is **per train** or **total**.

### Influent characteristics
Include:
- upstream screening: bar spacing / perforated plate size
- TSS / VSS (or at least qualitative: “stringy”, “high rags”, “FOG present”)
- temperature range
- septicity / H2S potential (materials + odor)

### Grit characteristics (if known)
Even approximate values improve quotes:
- grit loading rate (e.g., volume per day) or qualitative (“heavy grit in wet weather”)
- target cut size and specific gravity basis (example: ≥ 0.2 mm, SG 2.65)
- organics content target in removed grit (if you care about landfill acceptance)

## Mechanical / design interface items that routinely cause change orders

- **Hydraulics**
  - inlet/outlet elevations and available headloss
  - bypass requirements and channel geometry constraints

- **Grit removal method**
  - pump, airlift, screw conveyor, bucket elevator
  - washwater source and discharge destination

- **Materials**
  - stainless grade, coatings, fasteners, concrete interfaces
  - abrasion considerations for grit pumps and piping

- **Controls**
  - vendor PLC included or plant PLC only?
  - comms protocol (Modbus TCP, EtherNet/IP, etc.)
  - desired operating modes (flow-paced? timer-based? wet weather mode?)

## What to attach in addition to the datasheet

- Site plan / headworks layout (even a sketch with dimensions)
- Hydraulic profile (if gravity system)
- Any existing O&M pain points (ragging, pump wear, odor, grit carryover)

