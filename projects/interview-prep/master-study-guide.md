# SpaceX Build Reliability Engineer (Starship) — Master Study Guide

> **Role**: Build Reliability Engineer — Starship | Starbase, TX
> **Core mandate**: "Reliability by any means necessary" — you own fabrication processes, work instructions, tooling, and inspection simultaneously.

---

## PART 0 — SpaceX Engineering Culture (Read This First)

This is the lens through which every technical question is evaluated.

### The Five-Step Engineering Algorithm

SpaceX's manufacturing leadership articulates this explicitly — interviewers reference it.

1. **Challenge requirements** — Every spec is assumed dumb until proven otherwise. Find a way to make it less dumb.
2. **Delete parts or processes** — Remove anything that doesn't need to exist. Nothing should be added back without a strong reason.
3. **Simplify and optimize** — Make what remains easier to produce.
4. **Increase speed** — Add capacity and velocity once the design is right.
5. **Automate last** — "Most engineers start with Step 5 and automate a process that never should have existed."

**Interview implication**: When asked to solve a manufacturing problem, the SpaceX-right answer involves simplifying or eliminating first. Show you think about cost, cycle time, and iteration speed — not just technical correctness.

### Core Cultural Values

| Value | What It Looks Like in an Interview |
|---|---|
| Extreme ownership | "I found it, I owned the fix, I tracked it to closure" — never "the team handled it" |
| First principles | Derive from physical law, not convention — "because that's how it's always been done" is disqualifying |
| Rapid iteration | A flying prototype that fails > a perfect design that never launches |
| Reliability by any means | You reach into process, tooling, inspection, and design simultaneously |

### How to Structure Every Behavioral Answer

**Situation** → specific context, constraints, stakes
**Action** → what *you personally* did (use "I", not "we")
**Result** → quantified outcome (rate, time, cost, failure avoided)
**Learning** → what you'd do differently or what became a standard practice

### Common Behavioral Questions

- Walk me through your most technically challenging project.
- Describe a time you found and fixed a systemic quality issue on a manufacturing line.
- How do you handle a non-conforming part when production is behind schedule?
- Tell me about a time you used data to make a manufacturing decision.
- What would you do if you disagreed with a design engineer's disposition on an NCMR?

---

## PART 1 — Non-Destructive Testing / Evaluation (NDT/NDE)

Governing standards: **ASNT SNT-TC-1A** (personnel certification), **NAS 410** (aerospace NDT), **AWS D17.1** (aerospace weld inspection)

### Visual Testing (VT)

- Always performed **first**, before any other method — cheapest, fastest
- Detects: surface cracks, porosity, undercut, weld profile issues, discoloration
- Tools: borescopes, mirrors, magnifiers, digital cameras, UV lights
- Minimum illumination: **100 foot-candles** per most aerospace specs
- Limitation: surface-only; highly inspector-dependent

### Liquid Penetrant Testing (PT)

**Process sequence — must know in order:**

1. **Pre-clean** — remove oil, scale, paint (contaminants mask defects)
2. **Apply penetrant** — dwell time 10–60 min depending on material and temperature
3. **Remove excess** — careful: over-wash removes real indications; under-wash gives false positives
4. **Apply developer** — draws penetrant back to surface; creates visible indication
5. **Inspect** — UV light (fluorescent PT) or white light (visible PT)
6. **Post-clean**

**Types:**
- Type I Fluorescent — higher sensitivity, requires UV light, used in aerospace
- Type II Visible/Color-contrast — red dye, white developer, field use

**Sensitivity levels:** 1/2 (water-washable) through 4 (post-emulsifiable, highest sensitivity)

**Detects:** Surface-open cracks, porosity, seams, laps, cold shuts

**Does NOT detect:** Subsurface defects; does NOT work on porous materials

**Why not porous?** Penetrant absorbs into bulk of material → false indications everywhere on developer application.

**Common failure modes:**
- False negative: insufficient dwell time, contaminated surface, over-washing
- False positive: surface scratches, porous material, residual penetrant

### Radiographic Testing (RT / X-ray)

**Principle:** X-rays/gamma rays pass through material; density variations create image contrast

**Detects:** Internal volumetric flaws — porosity, voids, inclusions, incomplete penetration, cracks

**Critical limitation:** Crack detection depends on beam angle.
- Crack **parallel** to beam = invisible
- Crack **perpendicular** to beam = most visible
- This is why RT alone is insufficient — combine with UT for planar flaws

**Film density:** 2.0–3.0 per ASTM E1742 for aerospace work

**Digital options:** Computed Radiography (CR) uses phosphor plates; Digital Radiography (DR) uses flat-panel detectors — faster, less chemical waste

**Safety:** Radiation safety protocols, controlled area, personnel dosimetry badges required

### Electromagnetic Acoustic Transducer (EMAT)

**The SpaceX-critical NDT method** — directly relevant to 304L stainless tank weld inspection.

**Principle:** Generates ultrasonic waves inside the material via electromagnetic induction — **no physical contact, no couplant required**

**How it works:**
1. Strong static magnetic field applied (permanent magnet or electromagnet)
2. RF coil carries alternating current → eddy currents induced in material surface
3. Lorentz force interaction between eddy currents and magnetic field → acoustic waves launched into material

**Key advantages over conventional UT:**
- No couplant — works on hot, cold, rough, coated, or moving surfaces
- Generates shear horizontal (SH) waves — propagate cleanly through austenitic stainless steel's coarse grain structure

**Why EMAT for Starship tank welds?**
Austenitic stainless (304L) welds have a coarse dendritic grain structure that **scatters and skews longitudinal ultrasonic waves** (used in conventional UT), causing missed real defects and false indications. SH waves from EMAT are far less susceptible to this scattering. Plus, no couplant means production-speed inspection of large tank sections.

**Limitations:** Lower sensitivity than contact UT; requires conductive material; heavier, bulkier probes

**Wave modes EMAT can generate:** Shear horizontal (SH), Rayleigh surface waves, Lamb waves — modes impossible with conventional piezoelectric transducers

### Ultrasonic Testing (UT) — Overview

- Detects subsurface planar flaws (cracks, lack of fusion, delaminations)
- **Phased Array UT (PAUT):** Electronically steers beam, produces cross-sectional images — much faster for weld inspection
- **TOFD (Time of Flight Diffraction):** Accurately measures flaw depth and height
- **A-scan:** Single trace (amplitude vs. time); **B-scan:** Cross-section image; **C-scan:** Plan-view map

---

## PART 2 — Welding

Governing standard: **AWS D17.1** (Fusion Welding for Aerospace Applications)

### AWS D17.1 Weld Classes

| Class | Application |
|---|---|
| A | Flight hardware — most stringent |
| B | Support hardware that could affect flight safety |
| C | Non-flight support hardware |

**Key documents:** WPS (Welding Procedure Specification), PQR (Procedure Qualification Record), WPQ (Welder Performance Qualification)

### Process Comparison

| Process | Precision | Speed | Automation | Primary Use |
|---|---|---|---|---|
| TIG (GTAW) | Highest | Slow | Yes (orbital) | Aerospace, thin wall, Ti, SS |
| MIG (GMAW) | Medium | Fast | Yes | Structural, thicker SS |
| Laser | Very high | Fast | Yes | Thin sections, precision, Starship panels |
| Spot (RSW) | Medium | Very fast | Yes | Sheet metal overlap joints |
| Friction Stir (FSW) | High | Medium | Yes | Aluminum alloys (not SS) |

### TIG Welding (GTAW) — Deep Dive

**Current polarity:**
- DCEN (DC Electrode Negative): 70% heat at workpiece → deep penetration, used for most metals
- DCEP: cleaning action at surface → used for aluminum
- AC: alternating cleaning and penetration → aluminum

**Tungsten electrode:** 2% thoriated (2T) most common in aerospace; ceriated (EWCe-2) as non-radioactive alternative

**Shielding gas:**
- Pure argon for most metals
- Argon-helium mix: raises arc voltage, increases penetration and travel speed
- **Back purging with argon required for stainless and titanium** — oxygen causes oxidation and embrittlement

**Heat input** = (V × I × 60) / travel speed [mm/min] → units = J/mm
- Lower heat input = less distortion, less HAZ sensitization in stainless

**Interpass temperature:** Keep below **150°C (300°F)** for stainless — prevents carbide precipitation (sensitization → intergranular corrosion)
- 304L's low carbon (0.03% max) specifically reduces this risk

**Weld color acceptance (AWS D17.1):**
- Stainless: Silver/gold = accept | Blue = marginal | Gray/black = reject
- Titanium: Silver = accept | Light gold = usually accept | Blue-purple-gray = increasing oxidation, reject

**Common TIG defects and causes:**

| Defect | Cause | Detection | Fix |
|---|---|---|---|
| Porosity | Contaminated base/filler/gas, moisture | RT, PT | Clean everything; increase post-flow time |
| Lack of fusion | Speed too fast, current too low, poor joint prep | UT, RT | Adjust parameters; improve prep |
| Incomplete penetration | Insufficient heat, root gap too small | RT | Increase heat input; adjust joint design |
| Crater cracks | Rapid arc termination | VT, PT | Use current decay or crater fill |
| Undercut | Excessive current/arc length at toes | VT | Reduce current; adjust technique |
| Distortion | Excessive heat input | Measurement | Reduce heat; improve fixturing |
| Tungsten inclusion | Electrode contacts weld pool | RT | Replace electrode; clean joint |

### Laser Welding

**Advantages over TIG:** Narrow HAZ, fast travel speed, easily automated, minimal distortion, precise

**Modes:**
- Conduction mode: Low power density, shallow smooth welds
- Keyhole mode: High power density → deep narrow welds. Risk: keyhole collapse → porosity

**SpaceX use:** Laser welding on Starship propellant tank rings and structural panels for speed and consistency

### Robotic Welding

**Advantages:** Repeatability, speed, no human fatigue variation
**Requirements:** Requires well-controlled fixturing and joint fit-up — less forgiving of gaps than skilled human welder
**SpaceX use:** Robotic TIG and laser systems with automated seam tracking on Starship tank sections

---

## PART 3 — Materials

### 304L / 316L Stainless Steel — The Starship Choice

**Know these 5 reasons from first principles:**

1. **Cryogenic performance:** Austenitic stainless *gains* ~50% yield strength at LOX/LCH4 temperatures (~-183°C / -162°C). No ductile-to-brittle transition (unlike ferritic/martensitic steels). Aluminum has lower ductility at cryo temps.

2. **High-temperature performance:** Starship relies on the outer skin to radiate heat during reentry. 304 SS survives ~800°C. Aluminum melts at 660°C. Carbon fiber begins degrading well before this.

3. **Weldability:** 304L ("L" = low carbon, max 0.03% C) is readily weldable with robotic systems. Reduced carbide precipitation risk vs. standard 304.

4. **Cost and availability:** Orders of magnitude cheaper than CFRP. Available as sheet stock — roll and weld. No long lead time for composite layup tooling. Enables rapid iteration.

5. **Self-passivating:** Chromium oxide layer provides corrosion resistance without coatings.

**Note:** SpaceX has also developed a proprietary "30X" alloy with optimized properties beyond off-the-shelf 304L.

**304L vs 316L:**
- 316L adds 2–3% molybdenum → better pitting/crevice corrosion resistance
- Both are austenitic (non-magnetic when annealed; slightly magnetic when cold-worked)

**Sensitization:** Heating austenitic SS to 450–850°C causes chromium carbides to precipitate at grain boundaries → depletes Cr adjacent zones → susceptible to intergranular corrosion. L-grade (low C) and solution annealing prevent this. Critical in weld HAZ.

### Inconel 718 (Nickel Superalloy)

**Use:** Raptor engine turbopumps, hot sections, combustion chamber components

**Strengthening:** Precipitation hardening — gamma-prime (γ') Ni₃(Al,Ti) and gamma-double-prime (γ'') Ni₃Nb precipitates block dislocations

**Heat treatment:**
1. Solution anneal: 954–1010°C / 1 hour, air or water cool
2. Double aging: 718°C / 8h → furnace cool → 621°C / 8h total

**Properties after treatment:** UTS 1240–1400 MPa; excellent fatigue and creep resistance to ~650°C

**Machinability:** Difficult — work hardens rapidly, low thermal conductivity. Use sharp carbide tooling, high cutting fluid, slow speeds.

**Weldability:** Moderate — susceptible to strain-age cracking during PWHT. Pre-weld annealing required.

### Titanium 6Al-4V

**Use:** Structural brackets, fasteners, pressure vessels — highest strength-to-weight ratio

**Properties:** 4.43 g/cm³ density (vs 7.9 for SS). UTS ~950 MPa.

**Critical welding requirement:** Fully inert atmosphere. O₂ contamination >0.3% causes embrittlement. Use trailing gas shields, glove boxes, or vacuum chambers.

**Temperature limit:** Above ~315°C in sustained loading, creep becomes significant.

### Aluminum Alloys

| Alloy | UTS | Weldable? | Use Case |
|---|---|---|---|
| 2024-T3 | ~483 MPa | No (hot cracking) | Aircraft fuselage skin |
| 6061-T6 | ~310 MPa | Yes | General structural |
| 7075-T6 | ~570 MPa | Difficult | High-stress structures |

**Cryo concern:** Al alloys have lower ductility at cryogenic temps than stainless — key reason SpaceX chose stainless for Starship tanks.

---

## PART 4 — GD&T (Geometric Dimensioning and Tolerancing)

Standard: **ASME Y14.5-2018**

### Datum Reference Frame (DRF)

- **Primary datum (A):** 3 degrees of freedom constrained (plane contact)
- **Secondary datum (B):** 2 more DOF constrained
- **Tertiary datum (C):** Final DOF constrained
- Order matters — always establish A, then B, then C

### GD&T Symbols by Category

**Form** (no datum):
| Symbol | Control | Key Point |
|---|---|---|
| Straightness — | Line element or axis deviation | Can apply to surface elements or derived axis |
| Flatness ⬜ | Surface within two parallel planes | Form only — says nothing about where surface lives in space |
| Circularity ○ | Cross-section within concentric circles | Per cross-section only |
| Cylindricity | Combination of roundness + straightness + taper | Entire surface simultaneously |

**Orientation** (datum required): Perpendicularity ⊥, Parallelism ∥, Angularity ∠

**Location** (datum required):
- **True Position ⊕** — Most used. Cylindrical tolerance zone at exact theoretical location. 57% more tolerance volume than equivalent square zone.
- Concentricity — Median points coaxial with datum (hard to measure; often replaced by runout)
- Symmetry — Median points symmetric about datum plane

**Profile:**
- **Profile of a Surface** — Controls form + orientation + location simultaneously relative to datums. Most powerful and flexible. Heavily used in aerospace.
- Profile of a Line — 2D cross-section profile only

**Runout:**
- Circular Runout — controls wobble of each cross-section independently
- Total Runout — controls all cross-sections simultaneously

### Profile of Surface vs. Flatness — The Critical Distinction

**Flatness:** Pure form control. No datum. Says only that the surface lies within two parallel planes separated by the tolerance. Does NOT tell you where those planes are in space relative to anything else.

**Profile of a Surface:** Controls form AND orientation AND location relative to the datum reference frame. For aerospace mating structures, Profile ensures the surface is in the right place in 3D space — flatness alone cannot guarantee assembly fit.

### Material Condition Modifiers

| Modifier | Symbol | Meaning |
|---|---|---|
| MMC | Ⓜ | Max material (smallest hole, largest pin) |
| LMC | Ⓛ | Min material (largest hole, smallest pin) |
| RFS | Ⓢ | Default if no modifier — applies regardless of size |

**Bonus tolerance:** At MMC or LMC, bonus tolerance = departure from that condition
- Example: Hole with ∅0.5 position at MMC; if hole is 0.3mm larger than MMC → effective tolerance = ∅0.8

**Virtual Condition (assembly worst case):**
- External feature (pin) at MMC: VC = MMC size + position tolerance
- Internal feature (hole) at MMC: VC = MMC size − position tolerance

### True Position Formula

```
Positional deviation = 2 × √[(Δx)² + (Δy)²]
```

The factor of 2 converts radial deviation to diameter (position tolerance is a diametrical zone). Result must be ≤ position tolerance + any bonus.

---

## PART 5 — Reliability Engineering

### FMEA (Failure Mode and Effects Analysis)

**Type:** Inductive — bottom-up. Start with components, trace effects upward.

**RPN = Severity (S) × Occurrence (O) × Detection (D)** — each 1–10

**Critical RPN insight:** Never look at RPN alone. S=10 / O=1 / D=10 = RPN 100 is far more dangerous than S=5 / O=4 / D=5 = RPN 100. Always flag high-Severity failures independently.

**DFMEA vs PFMEA:** Design FMEA (product) vs Process FMEA (manufacturing). BRE role centers on PFMEA.

**PFMEA example for welding:**
- Failure mode: Porosity in weld joint
- Effect: Structural weakness, potential fracture
- Cause: Contaminated shielding gas, surface contamination
- Controls: Pre-weld cleaning procedure, gas flow check
- S: 8, O: 3, D: 4 → RPN: 96
- Action: Automated gas purity sensor, add RT to critical joints → new RPN: 32

### FTA (Fault Tree Analysis)

**Type:** Deductive — top-down. Start with an undesired event, ask how it could happen.

**Logic gates:**
- **AND gate:** All inputs must occur simultaneously. System has redundancy.
- **OR gate:** Any single input causes output. Single-point failure — highest risk.

**Probability:**
- AND: P = P(A) × P(B)
- OR: P = 1 − (1−P(A))(1−P(B)) ≈ P(A) + P(B) for small probabilities

**Cut sets:** Minimum set of basic events that cause the top event. Single-element cut sets = single-point failures — highest priority to eliminate.

**FMEA vs FTA:** Use FMEA early to identify all failure modes. Use FTA for a specific critical failure to quantify probability. Best practice: run both.

### Bathtub Curve

| Region | β (Weibull shape) | Failure Rate | Cause | Fix |
|---|---|---|---|---|
| Infant mortality | β < 1 | Decreasing | Mfg defects, latent flaws | Burn-in / proof testing |
| Useful life | β ≈ 1 | Constant (random) | Random failures | Redundancy, monitoring |
| Wear-out | β > 1 | Increasing | Fatigue, wear | Preventive replacement |

### Weibull Analysis

**Parameters:**
- **β (shape):** β<1 = infant mortality; β=1 = exponential/random; β>1 = wear-out (β≈2-3 = early wear-out, β>3 = tight wear-out clustering)
- **η (characteristic life):** Time at which **exactly 63.2%** of population has failed. (Because F(η) = 1 − e⁻¹ = 0.632)

**Reliability function:** R(t) = e^(−(t/η)^β)

**Weibull plot:** Plot median rank vs. time on log-log paper. Slope of best-fit line = β. η read at F = 63.2%.

**BX life:** B10 = time at which 10% of population fails. B50 = median life. Use for replacement interval planning.

**Median rank formula:** F_i ≈ (i − 0.3) / (n + 0.4)

### Statistical Process Control (SPC) and Capability

**Control charts:**
- X-bar/R chart: subgroup mean and range
- I-MR chart: individuals and moving range (common in low-volume aerospace)
- p-chart: proportion defective
- Control limits = ±3σ from process mean (NOT spec limits)

**Western Electric out-of-control rules:**
1. 1 point beyond ±3σ
2. 2 of 3 consecutive points beyond ±2σ (same side)
3. 4 of 5 consecutive points beyond ±1σ (same side)
4. 8 consecutive points on one side of centerline

**Process Capability:**

| Index | Formula | Meaning |
|---|---|---|
| Cp | (USL − LSL) / 6σ | Spread only (ignores centering) |
| Cpk | min[(USL−μ)/3σ, (μ−LSL)/3σ] | Actual capability with centering |
| Ppk | Same as Cpk but uses overall σ | Long-term actual capability |

**Targets:**
- Cpk ≥ 1.33 → capable (4σ process)
- Cpk ≥ 1.67 → highly capable (5σ, often required for flight-critical features)
- Cpk < 1.0 → incapable; immediate corrective action

**Cpk vs Ppk gap:** A large gap means the process shifts significantly over time — look for fixture wear, operator variation, material batch differences.

---

## PART 6 — AS9100 and Aerospace Quality Systems

### AS9100 Key Additions Over ISO 9001

- **First Article Inspection (FAI) — AS9102:** Verify first production part conforms to ALL drawing requirements before series production
- **Configuration management:** Control design changes; document revision history
- **Risk management:** Formal risk assessment required for all programs
- **Key characteristics:** Features where variation significantly affects safety or function — must have measurement and control plans
- **Critical items:** Failure = safety or mission consequence — additional scrutiny required
- **Counterfeit parts prevention:** Documented prevention process required
- **Full traceability:** Raw material lot → final assembly

### Nonconformance / MRB Process

**Flow:**
1. Inspector finds nonconformance → writes **NCMR** (Nonconformance Material Report)
2. Part tagged, physically quarantined
3. **MRB (Material Review Board)** convened: Quality Engineer + Manufacturing Engineer + Design Engineer
4. **Disposition selected:**

| Disposition | Meaning | Special Requirements |
|---|---|---|
| **Use As Is (UAI)** | Does not affect form, fit, or function | Must have documented engineering rationale |
| **Rework** | Bring back into conformance with drawing | Must re-inspect after rework |
| **Repair** | Deviates from drawing but still functional | Engineering + possibly customer approval; documented forever |
| **Scrap** | Unusable | Must be physically destroyed/marked; documented |
| **Return to Supplier** | Vendor material defect | Vendor CAR initiated |

5. Corrective action (8D/CAR) initiated if systemic

**Rework vs Repair distinction (interview favorite):**
Rework = part meets the original drawing after the work is done.
Repair = part permanently deviates from the drawing but is still functional by engineering judgment. Repair requires formal engineering approval and stays in the part's permanent record.

### 8D / Corrective Action Process

1. D1: Form team
2. D2: Describe the problem (5W2H)
3. D3: Containment — stop the bleeding
4. D4: Root cause analysis (5-Why, Fishbone/Ishikawa, FTA)
5. D5: Choose corrective actions
6. D6: Implement corrective actions
7. D7: Verify effectiveness
8. D8: Prevent recurrence; close out; recognize team

**Root cause tools:**
- **5-Why:** Iteratively ask "why" to get from symptom to root cause. Stop at the process/system level, not the person level.
- **Fishbone (Ishikawa):** Categories: Machine, Method, Material, Man, Measurement, Environment (6M).

### Key MIL-SPEC Standards

| Standard | Content |
|---|---|
| MIL-STD-1629A | FMEA procedure |
| MIL-STD-882E | System Safety — hazard analysis |
| MMPDS (formerly MIL-HDBK-5J) | Metallic materials properties database for aerospace |
| Nadcap | Third-party accreditation for special processes (welding, NDT, heat treat) |

---

## PART 7 — 3D CAD

### Siemens NX (Most Relevant to SpaceX)

**Key capabilities:**
- **Synchronous Technology:** Edit geometry directly without full feature history — critical for modifying imported models from other systems
- **PMI (Product and Manufacturing Information):** Attach GD&T, notes, surface finish symbols directly to 3D model (Model-Based Definition / MBD — eliminates separate 2D drawings)
- **Large assembly management:** Lightweight representations, reference sets, partial loading
- **NX CAM:** Generates CNC toolpaths directly from NX model — no translation errors
- **Teamcenter integration:** Native PLM — version control, BOM, change management
- **Weld assistant:** Define weld joints in assembly, generate weld features
- **Sheet metal:** Flange, bend, unbend — directly relevant to Starship panel manufacturing

**Interview-ready topics:**
- How do you manage large assembly performance in NX?
- What is Model-Based Definition and why does it matter?
- Explain synchronous vs parametric modeling and when you'd use each

### SolidWorks

- Feature-based parametric modeler; accessible, lower cost than NX
- Strong in small-to-mid assemblies
- Key features: Equations for parameter-driven design, configurations for variants, Simulation (FEA), Flow Simulation (CFD), PDM for version control

### CATIA

- Dominant in commercial aerospace (Airbus, Boeing) and automotive
- Extremely powerful surfacing (Class-A aerodynamic surfaces)
- 3DEXPERIENCE platform for cloud-based PLM integration

---

## PART 8 — SQL for Manufacturing Data

SpaceX will likely test SQL live. Practice writing these cold.

### Common Manufacturing Schema

```sql
parts(part_id, part_number, revision, material, status)
inspections(inspection_id, part_id, inspector_id, date, method, result)
defects(defect_id, inspection_id, defect_type, severity, location)
ncmrs(ncmr_id, part_id, defect_id, disposition, date_opened, date_closed)
production_runs(run_id, part_number, quantity, date, line_id, operator_id)
```

### Query 1: Defect Rate by Part Number

```sql
SELECT
    p.part_number,
    COUNT(DISTINCT i.inspection_id)         AS total_inspections,
    COUNT(DISTINCT d.defect_id)             AS total_defects,
    ROUND(COUNT(DISTINCT d.defect_id) * 100.0
          / NULLIF(COUNT(DISTINCT i.inspection_id), 0), 2) AS defect_rate_pct
FROM parts p
JOIN  inspections i ON p.part_id = i.part_id
LEFT JOIN defects d ON i.inspection_id = d.inspection_id
GROUP BY p.part_number
ORDER BY defect_rate_pct DESC;
```

### Query 2: First Pass Yield (FPY)

```sql
SELECT
    p.part_number,
    COUNT(*)                                AS total_parts,
    SUM(CASE WHEN i.result = 'pass' THEN 1 ELSE 0 END) AS first_pass,
    ROUND(SUM(CASE WHEN i.result = 'pass' THEN 1 ELSE 0 END) * 100.0
          / NULLIF(COUNT(*), 0), 2)         AS fpy_pct
FROM parts p
JOIN (
    SELECT part_id, result,
           ROW_NUMBER() OVER (PARTITION BY part_id ORDER BY date ASC) AS rn
    FROM inspections
) i ON p.part_id = i.part_id AND i.rn = 1
GROUP BY p.part_number;
```

### Query 3: NCMR Aging — Open Tickets by Disposition

```sql
SELECT
    disposition,
    COUNT(*)                                              AS open_count,
    ROUND(AVG(DATEDIFF(day, date_opened, GETDATE())), 1) AS avg_days_open,
    MAX(DATEDIFF(day, date_opened, GETDATE()))            AS max_days_open
FROM ncmrs
WHERE date_closed IS NULL
GROUP BY disposition
ORDER BY avg_days_open DESC;
```

### Query 4: Defects by Inspector (Bias Detection)

```sql
SELECT
    i.inspector_id,
    COUNT(i.inspection_id)       AS inspections_performed,
    COUNT(d.defect_id)           AS defects_found,
    ROUND(COUNT(d.defect_id) * 100.0
          / COUNT(i.inspection_id), 2) AS detection_rate_pct
FROM inspections i
LEFT JOIN defects d ON i.inspection_id = d.inspection_id
GROUP BY i.inspector_id
ORDER BY detection_rate_pct DESC;
```

### Key SQL Concepts to Know

- **ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)** — essential for first-inspection queries
- **LEFT JOIN vs INNER JOIN** — LEFT JOIN keeps all rows in left table even with no match (use for defect rate to include zero-defect parts)
- **NULLIF(denominator, 0)** — prevents divide-by-zero errors
- **DATEDIFF** — varies by SQL dialect (SQL Server, MySQL, SQLite differ)
- **Window functions:** ROW_NUMBER, RANK, LAG, LEAD, SUM OVER, AVG OVER

---

## PART 9 — Power BI for Quality Dashboards

### Key Concepts

- **Data model:** Star schema (fact tables + dimension tables). Fact = inspections/defects. Dimensions = part, date, inspector, process.
- **DAX measures (must know):**
  ```
  FPY % = DIVIDE(COUNTROWS(FILTER(Inspections, Inspections[first_result] = "pass")), COUNTROWS(Inspections))
  
  Defect Rate = DIVIDE([Total Defects], [Total Inspections], 0)
  
  Days Open = DATEDIFF(NCMR[date_opened], TODAY(), DAY)
  ```
- **Slicers:** Allow users to filter by date range, part number, process, inspector
- **Drill-through:** Click a part number to see all NCMRs for that part
- **Conditional formatting:** Red/yellow/green tiles based on Cpk thresholds
- **Refresh strategy:** DirectQuery (live, slower) vs Import (snapshot, faster) vs Composite

### Quality Dashboard Best Practices

- Leading indicators (defect rate trend, FPY by line) vs lagging indicators (escapes to next level)
- Pareto chart (80/20 rule) for defect type prioritization
- Run charts with control limits for SPC visualization
- NCMR aging heatmap by disposition and responsible team

---

## PART 10 — Tooling Design

### Principles for Aerospace Tooling

- **Locating scheme:** Use 3-2-1 locating principle. 3 points define a plane (primary datum), 2 points on a perpendicular surface (secondary), 1 point on a third surface (tertiary). Fully constrains the part.
- **Clamping:** Clamps always apply force toward locators, never away. Never clamp before all locators are contacted.
- **Tolerance stack-up:** RSS (Root Sum Square) method for independent errors: total = √(t₁² + t₂² + t₃² + ...). Worst case = sum of all. RSS is realistic for production; worst case for safety-critical.
- **Thermal expansion:** Account for CTE mismatch between tool material (often Invar for low-CTE) and part material, especially for large aerospace structures.
- **Access and ergonomics:** Design for the human — reach envelopes, sight lines for inspection, torque wrench access.
- **Mistake-proofing (poka-yoke):** Features that physically prevent incorrect assembly — keyed connectors, asymmetric features, go/no-go gauges.

### Types of Tooling Relevant to Starship

- **Assembly fixtures:** Hold structural components in precise location while joining (welding, fastening)
- **Inspection fixtures:** Precisely locate a part for CMM or manual inspection — repeatable datum establishment
- **Fluid system tooling:** Flushing, purging, and pressure testing fixtures for propellant lines
- **Jigs:** Guide cutting tools or drilling operations to maintain precise locations
- **Work access platforms:** Scaffold, man-lifts, and articulating platforms to safely access large structures like Starship rings

---

## PART 11 — Starship-Specific Knowledge

### Vehicle Architecture

- **Starship (upper stage):** Stainless steel propellant tanks (LOX forward, LCH4 aft), Raptor Vacuum engines
- **Super Heavy (booster):** Stainless steel structure, grid fins, Raptor sea-level engines (33 on Booster 9+)
- **Combined height:** ~121m — tallest rocket ever built
- **Propellants:** Liquid oxygen (LOX) + Liquid methane (LCH4) — full-flow staged combustion cycle

### 304L Stainless Construction

- Ring sections rolled from sheet and welded — laser and TIG robotic welding
- Starship's wall is ~4mm thick in some sections
- Reentry thermal management: no traditional heat shield — belly flaps with tiles, but outer skin designed to radiate heat
- The stainless skin also acts as a heat sink/radiator

### Raptor Engine

- Full-flow staged combustion (FFSC) cycle — highest efficiency thermodynamic cycle for rocket engines
- Both propellants (oxidizer-rich and fuel-rich) are fully burned in preburners before main combustion chamber
- Chamber pressure: ~300 bar (highest ever in production engine)
- Specific impulse: ~363s (sea level) / ~380s (vacuum)
- Raptor 3 targets ~280 ton-force thrust

### Common Build Challenges at Starbase

- Weld quality on large-diameter stainless rings (distortion, gap control)
- Cleanliness requirements for LOX-wetted components (oxygen-clean standards — avoid hydrocarbons)
- Large-volume integration sequencing
- Thermal gradient management during welding of thin-wall tanks
- Fit-up tolerance control on ring-to-ring interfaces

### LOX Cleanliness

**Critical for safety:** Hydrocarbons (oils, greases, organics) + liquid oxygen = detonation risk

- Parts for LOX service must be cleaned to aerospace oxygen-clean standards (typically per ASTM G93 or internal SpaceX spec)
- Cleaning process: degrease → precision clean → verify clean (UV inspection, wipe test) → protective packaging
- All tooling, gloves, and materials that contact LOX-wetted surfaces must be oxygen-compatible

---

## PART 12 — Manufacturing Process Documentation

### Work Instructions

- Step-by-step, written at technician level (not engineer level)
- Must include: required tooling/equipment, material specs, inspection points, accept/reject criteria, safety notes, reference documents
- Sign-off structure: Technician → Inspector → possibly Engineering for critical steps
- Revision-controlled — never a "living document" without formal ECO (Engineering Change Order)

### Planning Documents

- **Router / Traveler:** Accompanies the physical part through production; records each operation, materials used, inspections passed, stamps from technicians
- **Operation Card:** Detailed instruction for a single operation
- **Inspection Plan:** Which dimensions/features to inspect, method, frequency, accept/reject criteria, records required

### Test Plans

Must include:
- Test objective and success criteria
- Hardware configuration and setup
- Instrumentation requirements and calibration status
- Step-by-step procedure
- Safety considerations and emergency procedures
- Data recording requirements
- Pass/fail criteria and disposition of results

---

## Quick Reference: Interview Hot Topics

1. **Why did SpaceX choose stainless for Starship?** → Cryo strength gain, high-temp radiative capability, weldability, cost/iteration speed
2. **EMAT vs conventional UT for austenitic stainless weld inspection?** → SH waves don't scatter in coarse austenitic grains; no couplant for production speed
3. **Profile of Surface vs Flatness?** → Profile controls form + orientation + location; Flatness controls form only with no datum
4. **Rework vs Repair?** → Rework: meets drawing after. Repair: permanently deviates from drawing but acceptable per engineering.
5. **Cpk = 0.85 and Ppk = 0.60 — what does this tell you?** → Short-term incapable AND shifting over time — two separate problems
6. **What is bonus tolerance?** → At MMC/LMC, extra tolerance equal to departure from that condition
7. **MRB dispositions?** → Use As Is, Rework, Repair, Scrap, Return to Supplier
8. **Weibull β < 1 means?** → Infant mortality — decreasing failure rate — manufacturing defects
9. **Titanium welding requirements?** → Full inert atmosphere; trailing gas shield; O₂ > 0.3% causes embrittlement
10. **Stainless weld sensitization?** → 450–850°C → chromium carbides at grain boundaries → intergranular corrosion. Prevention: 304L low-carbon grade + control interpass temp
