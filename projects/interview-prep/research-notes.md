---
title: SpaceX Build Reliability Engineer (Starship) — Interview Prep Research Notes
date: 2026-04-14
tags: [interview, spacex, manufacturing, reliability, NDT, GD&T, aerospace]
---

# SpaceX Build Reliability Engineer (Starship) — Comprehensive Interview Prep

These notes cover every technical domain listed in the job description. The goal is to prepare for both deep dives on specific topics and first-principles reasoning questions in SpaceX's engineering culture.

---

## 0. SpaceX Engineering Culture — Know This First

Before any technical content: SpaceX interviews test how you *think*, not just what you know. They want to see first-principles reasoning, ownership, and comfort with ambiguity and speed.

### SpaceX's Five-Step Engineering Algorithm

This was articulated by a former SpaceX manufacturing leader. Know it cold — interviewers reference it explicitly.

1. **Challenge requirements** — "Your requirements are definitely dumb. Find a way to make them less dumb." Every spec should be questioned before being honored.
2. **Delete parts or processes** — Remove anything that doesn't need to exist. If you can't add it back later with a good reason, it shouldn't have been there.
3. **Simplify and optimize** — Make what remains easier to manufacture and extract more performance.
4. **Increase speed** — Add capacity and velocity once the design is right.
5. **Automate** — Only the last step. "Most people start with Step 5 and automate a process that never should have existed."

**Interview implication**: When given a manufacturing problem, the SpaceX-right answer often involves simplifying or eliminating rather than adding process steps. Show you think about cost, cycle time, and iteration speed, not just technical correctness.

### Core Cultural Values
- **Extreme ownership**: You own the outcome, not the task.
- **First principles**: Derive answers from physical law, not convention.
- **Rapid iteration / build-fly-learn**: A prototype that flies and fails is more valuable than a perfect design that never launches.
- **"Reliability by any means necessary"**: The BRE role explicitly uses this phrase. You are expected to reach into fabrication methods, work instructions, tooling, and inspection simultaneously.

### Common Behavioral Questions
- Walk me through your most technically challenging project. What would you do differently?
- Describe a time you found and fixed a systemic quality issue on a manufacturing line.
- How do you handle a situation where a part is out of spec but production is behind schedule?
- Tell me about a time you used data to make a manufacturing decision.

**Strong answer pattern**: Situation → action you personally took → quantified result → what you learned / what you'd change.

---

## 1. Non-Destructive Testing / Evaluation (NDT/NDE)

### Overview
NDT allows inspection of parts without destroying them. In aerospace, the six most-used methods are: Visual (VT), Liquid Penetrant (PT), Magnetic Particle (MT), Radiographic (RT), Ultrasonic (UT), and Eddy Current (ET). SpaceX adds EMAT as a specialized tool for weld inspection.

Governing standards: ASNT SNT-TC-1A (personnel certification), NAS 410 (aerospace NDT certification), AWS D17.1 (aerospace fusion welding inspection).

---

### Visual Testing (VT)
- First and cheapest method; must be performed before any other method.
- Detects: surface cracks, porosity, undercut, overlap, incorrect weld profile, discoloration.
- Tools: borescopes, mirrors, magnifiers, digital cameras.
- Limitation: surface-only; relies on inspector skill and lighting.

**Key parameter**: Minimum illumination of 100 fc (foot-candles) per most aerospace specs.

---

### Liquid Penetrant Testing (PT)

**Process sequence** (must know order):
1. Pre-cleaning (remove oil, scale, paint — contaminants mask defects)
2. Penetrant application (dwell time: typically 10–60 min depending on material and temp)
3. Excess penetrant removal (careful — over-washing removes indication; under-washing gives false positives)
4. Developer application (draws penetrant back to surface; creates visible indication)
5. Inspection (under UV light for fluorescent PT, or white light for visible/color-contrast PT)
6. Post-cleaning

**Types**:
- Type I Fluorescent (more sensitive, requires UV light, used in aerospace)
- Type II Visible/Color-contrast (red dye, white developer, field use)

**Sensitivity levels**: Level 1/2 (water-washable) through Level 4 (post-emulsifiable, highest sensitivity).

**Detects**: Surface-open cracks, porosity, seams, laps, cold shuts. Does NOT detect subsurface defects.

**Material compatibility**: Works on non-porous metals, ceramics, plastics. Does NOT work on porous materials.

**Common failure modes in PT**:
- False negative: insufficient dwell time, contaminated surface, over-washing
- False positive: scratches in surface, porous material, residual penetrant

**Interview question**: *Why can't you use liquid penetrant on a porous material?*
Answer: The penetrant will be absorbed throughout the bulk of the material, giving false indications everywhere on developer application.

---

### Radiographic Testing (RT / X-ray)

**Principle**: X-rays or gamma rays pass through the part; variations in density create different film exposure or digital detector response.

**Detects**: Internal volumetric flaws — porosity, voids, inclusions, incomplete penetration in welds, cracks (when oriented to beam).

**Key limitation**: Crack detection depends heavily on beam angle. A crack parallel to the beam is invisible; perpendicular to the beam is most visible. This is why RT alone is not sufficient — must combine with UT for planar flaws.

**Aerospace application**: Weld inspection for root and internal porosity, casting integrity, brazed joints.

**Radiographic density**: Film density 2.0–3.0 (ASTM E1742 range for most aerospace work).

**Digital RT (DR) and Computed Radiography (CR)**: Replace film; CR uses phosphor plates, DR uses flat-panel detectors. Faster turnaround, less chemical waste.

**Safety**: Requires radiation safety protocols, area controlled, personnel dosimetry.

---

### Electromagnetic Acoustic Transducer (EMAT)

**Principle**: EMAT generates ultrasonic waves inside the material using electromagnetic induction — no physical contact with the surface and no liquid couplant required.

**How it works**:
- A strong static magnetic field is applied via a permanent magnet or electromagnet.
- An RF coil carries alternating current, inducing eddy currents in the material surface.
- Lorentz force interaction between eddy currents and the magnetic field launches acoustic waves into the material.
- Frequency range: 0.1–10 MHz.

**Key advantage over conventional UT**: No couplant. Can inspect:
- Hot surfaces (above couplant evaporation point)
- Cold surfaces (below freezing)
- Rough or coated surfaces
- Parts in motion (in-process inspection)

**Wave modes**: EMAT can generate shear horizontal (SH), Rayleigh, and Lamb waves — modes that are impossible or difficult with conventional piezoelectric transducers.

**Best application**: Austenitic stainless steel weld inspection (Starship-relevant). SH waves propagate through the coarse, anisotropic grain structure of austenitic welds without the severe beam skewing that affects longitudinal waves. This makes EMAT superior to conventional UT for Starship's 304L stainless steel tank welds.

**Limitations**: Lower sensitivity than contact UT due to energy conversion efficiency; requires conductive material; heavier probes.

**Interview question**: *Why would you choose EMAT over conventional UT for inspecting Starship's stainless steel welds?*
Answer: Austenitic stainless has a coarse dendritic grain structure that scatters and skews longitudinal ultrasonic waves, causing false indications and missed real ones. SH waves generated by EMAT are much less susceptible to this scattering. Also, the no-couplant requirement is operationally important when inspecting large structures at production speed.

---

### Ultrasonic Testing (UT) — Brief

- Detects subsurface planar flaws (cracks, lack of fusion, delaminations).
- Phased Array UT (PAUT): electronically steers beam, produces cross-sectional images — much faster for weld inspection.
- Time of Flight Diffraction (TOFD): measures flaw depth and height accurately.
- A-scan (single trace), B-scan (cross-section), C-scan (plan view map).

---

## 2. Welding — Processes, Parameters, Defects, Inspection

### Welding Processes Comparison

| Process | Heat Source | Filler | Shielding | Precision | Speed | Common Use |
|---|---|---|---|---|---|---|
| TIG (GTAW) | Tungsten arc | Optional | Inert gas (Ar, He) | Highest | Slow | Aerospace, thin wall, Ti, SS |
| MIG (GMAW) | Wire arc | Wire (continuous) | Inert/active gas | Medium | Fast | Structural, thicker SS |
| Laser | Laser beam | Optional | Inert gas | Very high | Fast | Precision, thin, automated |
| Spot (RSW) | Resistance | None (fusion) | None | Medium | Very fast | Sheet metal overlap joints |
| Friction Stir (FSW) | Mechanical | None | None needed | High | Medium | Al alloys, cannot do SS easily |

---

### TIG Welding (GTAW) — Deep Dive

Most relevant to Starship tank welding. AWS D17.1 is the governing spec.

**Key parameters**:
- **Current**: DCEN (DC Electrode Negative) for most metals — provides 70% heat at workpiece. DCEP for aluminum (cleaning action). AC for aluminum (balance of cleaning and penetration).
- **Tungsten electrode**: 2% thoriated (2T) most common in aerospace. EWCe-2 (ceriated) as non-radioactive alternative.
- **Shielding gas**: Pure argon for most. Argon-helium mix increases penetration and travel speed (He raises arc voltage). Back purging with argon is required for stainless and titanium — oxygen causes oxidation and embrittlement.
- **Heat input** (J/mm): H = (V × I × 60) / (travel speed mm/min). Lower heat input = less distortion, less HAZ sensitization in stainless.
- **Interpass temperature**: Critical for stainless — keep below 150°C (300°F) to prevent carbide precipitation (sensitization → intergranular corrosion risk). 304L's low carbon content (0.03% max) is specifically to reduce this risk.

**Weld color acceptance per AWS D17.1**:
- Stainless steel: Bright silver/gold = acceptable. Blue = marginal. Gray/black = reject (excessive oxidation, inadequate shielding).
- Titanium: Silver = acceptable. Light gold = usually acceptable. Blue-purple-gray = increasing oxidation, reject.

**Common TIG defects and causes**:
- **Porosity**: Contaminated base metal, filler, or shielding gas; moisture; inadequate gas coverage. Fix: clean everything, increase post-flow time.
- **Lack of fusion**: Travel speed too fast, current too low, joint prep inadequate. Detected by UT or RT.
- **Incomplete penetration**: Insufficient heat input, root opening too small.
- **Crater cracks**: Rapid arc termination without fill. Fix: use current decay or crater fill technique.
- **Undercut**: Excessive current or arc length at toes of weld.
- **Distortion**: Excessive heat input, insufficient fixturing.
- **Tungsten inclusion**: Contact with weld pool (contaminated electrode). RT detectable.

---

### Laser Welding

**Advantages over TIG**: Much narrower heat-affected zone, faster travel speed, easily automated, minimal distortion, can weld very thin sections.

**Key parameters**: Power (W), travel speed (mm/s), focal spot size, shielding gas flow.

**Modes**:
- Conduction mode: Low power density, shallow welds, smooth surface.
- Keyhole mode: High power density creates vapor capillary (keyhole); deep, narrow welds. Risk: keyhole collapse → porosity.

**SpaceX use**: Laser welding used on Starship propellant tank rings and structural panels for speed and consistency.

---

### Robotic Welding

Advantages: Repeatability, speed, no human fatigue variation. Disadvantage: initial setup cost, requires well-controlled fixturing and joint fit-up (less tolerance for gap variation than a skilled human welder).

SpaceX uses robotic TIG and laser systems for Starship tank section manufacturing, with automated seam tracking.

---

### AWS D17.1 — Key Points

- **Class A**: Flight hardware (stringent).
- **Class B**: Support hardware that could affect flight safety.
- **Class C**: Non-flight support hardware.
- Welding procedure qualification: WPS (Welding Procedure Specification), PQR (Procedure Qualification Record), WPQ (Welder Performance Qualification).
- Visual inspection required before any NDE.
- Acceptance criteria for porosity, undercut, cracks, lack of fusion defined per class and weld type.

---

## 3. Materials — Stainless Steel, Inconel, Titanium, Aluminum

### 304L / 316L Stainless Steel — Starship Critical

**Why SpaceX chose stainless for Starship** (know this cold):
1. **Cryogenic performance**: At liquid oxygen/methane temperatures (~-183°C / -162°C), austenitic stainless steel actually *gains* strength. Yield strength increases ~50% at cryogenic temperatures. Carbon fiber composites and aluminum are more problematic at these extremes.
2. **High-temperature performance**: Starship's heat shield-less reentry relies on the outer tank skin radiating heat. 304 SS handles ~800°C before losing structural integrity. Aluminum melts at 660°C.
3. **Weldability**: 304L ("L" = low carbon, max 0.03% C) is readily weldable, especially with robotic systems. Reduced carbide precipitation risk vs. standard 304.
4. **Cost and availability**: Stainless is orders of magnitude cheaper than carbon fiber. Available in sheet form ready to roll and weld. Enables rapid iteration without long lead times for composite layup tooling.
5. **Self-passivating**: Chromium oxide layer provides corrosion resistance without coatings.
6. **Proprietary alloy**: SpaceX has developed a 30X alloy (designation not public) with optimized properties beyond off-the-shelf 304L.

**304L vs 316L**:
- 316L adds 2-3% molybdenum → better pitting and crevice corrosion resistance, better high-temp strength.
- 316L used where chloride exposure or higher temperatures require it.
- Both are austenitic (non-magnetic in annealed condition; slightly magnetic when cold-worked).

**Sensitization**: When austenitic SS is heated to 450–850°C, chromium carbides precipitate at grain boundaries, depleting adjacent zones of Cr → susceptible to intergranular corrosion. L-grade (low C) and solution annealing prevent this. Critical for HAZ in welding.

---

### Inconel 718 (Nickel Superalloy)

**Use case**: High-temperature structural components — Raptor engine turbopumps, hot sections, combustion chamber components.

**Composition**: Ni (~54%), Cr (~19%), Fe (~18%), Nb (~5%), Mo (~3%), Ti, Al.

**Strengthening mechanism**: Precipitation hardening (age hardening) through gamma-prime (γ') Ni₃(Al,Ti) and gamma-double-prime (γ'') Ni₃Nb precipitates. These block dislocation movement.

**Heat treatment sequence**:
1. Solution anneal: 954–1010°C for 1 hour, air cool or water quench (dissolves precipitates, recrystallizes grains).
2. Aging (double): 718°C / 8h furnace cool to 621°C / 8h total → maximizes γ'' precipitation.

**Properties after treatment**: UTS 1240–1400 MPa, Yield 1030–1100 MPa, excellent fatigue and creep resistance to ~650°C.

**Machinability**: Difficult — work hardens rapidly, low thermal conductivity (heat accumulates at tool tip). Use sharp carbide tools, high cutting fluid, slow speeds.

**Weldability**: Moderate — susceptible to strain-age cracking in HAZ during PWHT. Pre-weld annealing and controlled cooling required.

---

### Titanium 6Al-4V (Ti-6Al-4V)

**Use case**: Structural brackets, fasteners, pressure vessels — high strength-to-weight ratio applications.

**Properties**: Density 4.43 g/cm³ (vs. 7.9 for SS, 8.2 for Inconel). UTS ~950 MPa, Yield ~880 MPa. Excellent corrosion resistance. Biocompatible.

**Critical welding requirement**: Must be welded in a fully inert atmosphere. Oxygen contamination above ~0.3% causes embrittlement. Use trailing gas shields, glove boxes, or vacuum chambers.

**Alpha-beta alloy**: α phase (HCP, stable at lower temps) and β phase (BCC, stable at higher temps). 6Al stabilizes α; 4V stabilizes β. Annealing and aging control the ratio.

**Not for high temperature above ~315°C** in sustained loading — creep becomes significant.

---

### Aluminum Alloys

- **2024-T3**: High strength, good fatigue resistance. Used in aircraft fuselage skins. Not weldable (prone to hot cracking).
- **6061-T6**: Good general purpose, weldable, used in structural applications.
- **7075-T6**: Highest strength Al alloy commonly used (~570 MPa UTS). Used in high-stress structural members. Difficult to weld.
- **Cryogenic concern**: Aluminum alloys have lower ductility at cryogenic temps than stainless steel, which drove SpaceX away from Al for Starship tanks.

---

## 4. GD&T — Geometric Dimensioning and Tolerancing

### Standards

- **ASME Y14.5-2018** (current US standard)
- ISO 1101 (international equivalent, some different conventions)

### Datum Reference Frame (DRF)

A datum is a theoretically perfect plane, axis, or point derived from the actual datum feature. Three datums (A, B, C) establish a coordinate system:
- **Primary datum (A)**: Constrains 3 degrees of freedom (DOF) — plane contact removes 3 translational/rotational DOF.
- **Secondary datum (B)**: Constrains 2 more DOF.
- **Tertiary datum (C)**: Constrains the final DOF.

Order matters: Always establish A, then B, then C. The datum reference frame letter order in a feature control frame is the order of precedence.

---

### GD&T Symbol Categories

**Form** (no datum required):
- Straightness (─): Limits how much a line element or axis can deviate from straight.
- Flatness (⬜): Surface must lie within two parallel planes.
- Circularity (○): Cross-section must lie within two concentric circles.
- Cylindricity (⌀ with shape): Combination of straightness, roundness, and taper for a cylinder.

**Orientation** (datum required):
- Perpendicularity (⊥): Feature axis or surface at 90° to datum.
- Parallelism (∥): Feature parallel to datum.
- Angularity (∠): Feature at specified angle to datum.

**Location** (datum required):
- **True Position (⊕)**: Most widely used. Defines cylindrical tolerance zone centered on theoretical exact location. 57% more tolerance volume than square zone of same size.
- Concentricity: Median points of cross-sections coaxial with datum axis (hard to measure; often replaced by runout).
- Symmetry: Median points of feature symmetrical about datum plane.

**Profile**:
- Profile of a Line: 2D cross-section profile control.
- **Profile of a Surface (⌒)**: Most powerful and flexible tolerance. Controls all aspects of a surface simultaneously — form, orientation, and location — relative to datums. Heavily used in aerospace (SpaceX interview question asked specifically about this).

**Why Profile of a Surface over Flatness?**
Flatness only controls form (how flat the surface is in isolation). Profile of a Surface controls the surface's form AND its location and orientation relative to the datum reference frame simultaneously. For aerospace structures where mating surfaces must align with other features in 3D space, Profile of a Surface ensures the part assembles correctly — flatness alone doesn't guarantee that.

**Runout**:
- Circular Runout: Controls wobble of each cross-section as the part rotates.
- Total Runout: Controls overall surface deviation for all cross-sections simultaneously.

---

### Material Condition Modifiers

- **MMC (Maximum Material Condition)**: Feature at maximum material (smallest hole, largest pin). Symbol: Ⓜ
- **LMC (Least Material Condition)**: Feature at minimum material (largest hole, smallest pin). Symbol: Ⓛ
- **RFS (Regardless of Feature Size)**: Default if no modifier shown; tolerance applies regardless of actual size. Symbol: Ⓢ (rarely shown explicitly in newer standards).

**Bonus tolerance**: When MMC or LMC is applied to a position tolerance, bonus tolerance equals the departure from MMC/LMC. A hole with position tolerance ∅0.5 at MMC, if it measures 0.3mm larger than MMC, gets 0.3mm bonus → effective position tolerance is ∅0.8.

**Virtual Condition**: The worst-case boundary for assembly purposes. For a pin at MMC: VC = MMC size + geometric tolerance. For a hole at MMC: VC = MMC size − geometric tolerance.

---

### True Position Formula

For a hole measured at coordinates (x, y) relative to theoretical true position (x₀, y₀):

**Positional deviation** = 2 × √[(x − x₀)² + (y − y₀)²]

The factor of 2 converts the radial deviation to a diameter (since position tolerance is a diametrical zone).

This must be ≤ stated position tolerance (plus any bonus tolerance).

---

### Basic Dimensions

Exact theoretical values defining true position — shown in a box. They have no tolerance themselves; the tolerance is applied via the GC&T feature control frame.

---

## 5. Reliability Engineering — FMEA, FTA, MTBF, Weibull, SPC

### FMEA (Failure Mode and Effects Analysis)

**Type**: Inductive (bottom-up). Starts with components, asks "what can fail?" and traces effects upward.

**Process**:
1. Define system/function.
2. List all components.
3. For each component, identify all failure modes.
4. For each failure mode: identify effect on next level and system level.
5. Assign **Severity (S)**, **Occurrence (O)**, **Detection (D)** — each on 1–10 scale.
6. Calculate **RPN = S × O × D**.
7. Prioritize highest RPNs for corrective action.
8. Implement controls, reassess.

**Key insight on RPN**: RPN alone can be misleading — a failure with S=10 (catastrophic), O=1 (rare), D=10 (undetectable) gives RPN=100, same as S=5, O=4, D=5. The first is far more critical. Always look at Severity independently.

**DFMEA vs PFMEA**: Design FMEA (product design failures) vs Process FMEA (manufacturing process failures). BRE role will focus heavily on PFMEA.

**PFMEA example for welding**:
- Failure mode: Porosity in weld
- Effect: Structural weakness, potential fracture at load-bearing joint
- Cause: Contaminated shielding gas, base metal surface contamination
- Current controls: Pre-weld cleaning procedure, gas flow verification
- S: 8, O: 3, D: 4, RPN: 96
- Recommended action: Implement automated gas purity verification, add RT inspection to critical joints

---

### FTA (Fault Tree Analysis)

**Type**: Deductive (top-down). Starts with a specific undesired event (top event), asks "how could this happen?" and works down.

**Logic gates**:
- **AND gate**: All inputs must occur simultaneously for output to occur. System has redundancy — less risky.
- **OR gate**: Any single input causes output. No redundancy — series system.

**Probability calculation**:
- AND gate: P(output) = P(A) × P(B) — (if independent)
- OR gate: P(output) = 1 − (1 − P(A)) × (1 − P(B)) ≈ P(A) + P(B) for small probabilities

**Cut sets**: Minimum sets of basic events that, if all occur, cause the top event. Single-point failures are single-element cut sets — highest priority to eliminate.

**FMEA vs FTA comparison**:
- Use FMEA early in design to identify all failure modes comprehensively.
- Use FTA for a specific critical failure to understand its causes and quantify probability.
- Best practice: Run both, use FMEA to populate FTA basic event probabilities.

---

### MTBF and Reliability Math

**MTBF (Mean Time Between Failures)**: For repairable systems.
**MTTF (Mean Time To Failure)**: For non-repairable systems.

For exponential distribution (constant failure rate, λ):
- MTBF = 1/λ
- R(t) = e^(−λt) — reliability at time t
- F(t) = 1 − e^(−λt) — probability of failure by time t

**Bathtub curve** — failure rate over product life:
1. **Infant mortality** (β < 1): Decreasing failure rate. Caused by manufacturing defects, poor assembly, latent defects. Addressed by burn-in testing.
2. **Useful life** (β ≈ 1): Constant (random) failure rate. Exponential distribution applies.
3. **Wear-out** (β > 1): Increasing failure rate. Addressed by preventive replacement before wear-out.

---

### Weibull Analysis

The most versatile reliability distribution. Handles all three bathtub curve regions.

**Two-parameter Weibull PDF**: f(t) = (β/η)(t/η)^(β−1) × e^(−(t/η)^β)

**Parameters**:
- **β (shape parameter / slope)**: Determines failure rate behavior.
  - β < 1: Infant mortality (decreasing failure rate)
  - β = 1: Random failures (exponential — constant failure rate)
  - β ≈ 2–3: Early wear-out (increasing failure rate)
  - β > 3: Steep wear-out; failures cluster tightly
- **η (scale parameter / characteristic life)**: Time at which 63.2% of population has failed. (Because e^(−1) ≈ 0.368, so F(η) = 1 − 0.368 = 0.632.)

**Reliability function**: R(t) = e^(−(t/η)^β)

**Weibull probability plot**: Plot failure data on log-log paper. Slope of resulting line = β; intercept gives η. If points fall on a straight line, Weibull is a good fit.

**BX life**: B10 = time by which 10% of population fails. B50 = median life. Critical for establishing replacement intervals.

**Interview question**: *A weld inspection dataset shows 3 of 50 Starship tank welds failed pressure testing, at intervals of 12, 18, and 23 pressure cycles. How would you begin a Weibull analysis?*
- Rank the failures, calculate median ranks (F_i ≈ (i − 0.3)/(n + 0.4)).
- Plot on Weibull paper (ln(t) vs. ln(ln(1/(1−F)))).
- Fit a line; slope = β, x-intercept at y=0 gives ln(η).
- Interpret β to understand failure mechanism.

---

### Statistical Process Control (SPC) and Process Capability

**Control charts**: Monitor process over time to detect special-cause variation (out of control) vs. common-cause variation (inherent).
- **X-bar and R chart**: Monitor process mean (X-bar) and range (R) from subgroups.
- **Individuals (I-MR) chart**: When subgroup size = 1 (common in aerospace low-volume production).
- **p-chart**: Proportion defective.
- **c-chart / u-chart**: Count of defects per unit.

**Control limits**: ±3σ from process mean (UCL/LCL). Based on *process* variation, NOT specification limits.

**Rules for out-of-control signals** (Western Electric / Nelson rules):
- 1 point beyond ±3σ
- 2 of 3 points beyond ±2σ on same side
- 4 of 5 points beyond ±1σ on same side
- 8 consecutive points on one side of centerline

---

**Process Capability Indices**:

| Index | Formula | Use |
|---|---|---|
| Cp | (USL − LSL) / 6σ | Spread capability (ignores centering) |
| Cpk | min[(USL − μ)/3σ, (μ − LSL)/3σ] | Actual capability with centering |
| Pp | (USL − LSL) / 6s (overall) | Long-term spread |
| Ppk | Uses overall std dev | Long-term actual capability |

**Target values**:
- Cpk ≥ 1.33 (4σ process) = capable
- Cpk ≥ 1.67 (5σ) = highly capable (often required for flight-critical features)
- Cpk < 1.0 = incapable; immediate action required

**Cpk vs Ppk**: Cpk uses within-subgroup (short-term) σ; Ppk uses overall σ (includes between-subgroup variation). A large gap between Cpk and Ppk indicates the process shifts over time (fixturing variation, tool wear, operator-to-operator differences).

**Interview question**: *Your weld bead width has Cpk = 0.85 and Ppk = 0.60. What does this tell you?*
- Cpk < 1.0: Even in the short term the process isn't capable — the tolerance is too tight relative to process variation.
- Gap between Cpk and Ppk: Process is also shifting significantly over time. Look for assignable causes: fixture wear, electrode degradation, material batch variation.

---

## 6. AS9100 and Aerospace Quality Systems

### AS9100 Overview

AS9100 is the international quality management standard for aviation, space, and defense organizations. It is built on ISO 9001 with aerospace-specific additions.

**Key aerospace additions over ISO 9001**:
- **First Article Inspection (FAI)**: AS9102 — must verify the first production part conforms to all drawing requirements before series production.
- **Configuration management**: Control of design changes, document revision history.
- **Risk management**: Formal risk assessment required.
- **Key characteristics**: Features where variation significantly affects safety or function — must have documented measurement and control plans.
- **Critical items**: Items where failure would have safety or mission consequences — requires additional scrutiny.
- **Counterfeit parts prevention**: Documented process required.
- **Product traceability**: Full traceability from raw material lot through final assembly.

---

### Nonconformance and MRB Process

**Flow**:
1. Inspector finds non-conforming feature (out-of-spec dimension, weld defect, wrong material, etc.).
2. **NCMR (Nonconformance Material Report)** written — documents what, where, when, who found it.
3. Part tagged and quarantined (red tag / hold area).
4. **MRB (Material Review Board)** convened: typically includes Quality Engineer, Manufacturing Engineer, Design Engineer.
5. **Disposition options** (per AS9100 §8.7):
   - **Use As Is (UAI)**: Engineering determines nonconformance does not affect form, fit, or function. Must have documented engineering rationale.
   - **Rework**: Bring part back into conformance with original drawing (must re-inspect after).
   - **Repair**: Deviation from drawing but part is still functional; requires design engineering approval and may require customer approval.
   - **Scrap**: Part is unusable; must be rendered permanently unusable (crushed, marked, etc.) and documented.
   - **Return to Supplier**: Defective material from vendor.
6. Corrective action initiated if systemic issue detected.

**8D / CAR (Corrective Action Report)**: Structured problem-solving format for systemic nonconformances.
1. Define the problem (D1-D2)
2. Containment actions (D3)
3. Root cause analysis (D4 — use 5-Why, Fishbone/Ishikawa, or FTA)
4. Corrective actions (D5-D6)
5. Verify effectiveness (D7)
6. Prevent recurrence / close out (D8)

---

### MIL-SPEC Relevant Standards

- **MIL-STD-1629A**: FMEA procedure for military systems.
- **MIL-STD-882E**: System Safety standard — hazard analysis, risk matrix.
- **MIL-STD-2219**: Fusion welding for aerospace (largely superseded by AWS D17.1).
- **MIL-HDBK-5J / MMPDS**: Metallic materials and elements for aerospace vehicle structures — material property database (now MMPDS-18).
- **Nadcap**: National Aerospace and Defense Contractors Accreditation Program — third-party auditing for special processes (welding, NDT, heat treat, plating). SpaceX suppliers typically require Nadcap approval.

---

## 7. 3D CAD — NX, SolidWorks, CATIA

### Siemens NX

Most relevant to SpaceX; widely used in aerospace manufacturing and tooling design.

**Core capabilities**:
- **Parametric and Synchronous Technology**: NX's hybrid modeling approach. Parametric respects design intent and history; Synchronous allows direct geometry editing without a feature tree — useful for modifying imported models without full redesign.
- **Large assembly management**: Can handle full aircraft/rocket digital mockups. Uses lightweight representations, partial loading, and reference sets to manage performance.
- **Sheet metal**: Flange, bend, unbend tools — directly relevant to Starship ring and panel manufacturing.
- **Surfacing**: Class-A surface modeling for aerodynamic surfaces.
- **PMI (Product and Manufacturing Information)**: Attach GD&T, notes, surface finish symbols directly to 3D model — supports Model-Based Definition (MBD), eliminating separate 2D drawings.
- **NX Inspector / FAI**: First Article Inspection workflow integrated in NX — links CMM data to design requirements.
- **NX CAM**: Generates CNC toolpaths directly from NX model — avoids translation errors.
- **Teamcenter integration**: NX is natively integrated with Teamcenter PLM for version control, BOM management, and change management.

**Key NX tools for aerospace**:
- Aerospace sheet metal: Aero rib, aero shelf, aero flange features.
- Weld assistant: Define weld joints in assembly, generate weld features.
- Assembly sequencing: Simulate assembly order and clearance.

---

### SolidWorks

- Feature-based parametric modeler. More accessible/lower cost than NX.
- Strong in small-to-mid-size parts and assemblies.
- **Key features**: Equations for parameter-driven design, configurations for variants, eDrawings for sharing, Simulation (FEA), Flow Simulation (CFD).
- **PDM (Product Data Management)**: SolidWorks PDM for version control.
- Less capable than NX for very large assemblies or advanced surface work.

---

### CATIA

- Dassault Systèmes. Dominant in commercial aerospace (Airbus, Boeing) and automotive (Ferrari).
- Extremely powerful surfacing (Class-A surfaces for aerodynamics).
- 3DEXPERIENCE platform: Cloud-based PLM integration.
- Used for complex aircraft structures where assembly feasibility simulation is critical.

---

### Interview-Ready CAD Topics

- **GD&T in CAD**: Applying feature control frames in NX, understanding semantic PMI vs cosmetic annotations.
- **Model-Based Definition (MBD)**: Eliminating 2D drawings; all manufacturing information embedded in 3D model with PMI.
- **Interference detection**: Running clearance analysis in assemblies to find where parts collide before physical assembly.
- **Digital twin**: Using the CAD model as the authoritative as-designed state to compare against CMM/scan data for as-built verification.

---

## 8. SQL for Manufacturing Data

### Core Concepts to Know

Expect to write queries on-the-spot for manufacturing quality data scenarios.

**Database schema you'll likely see**:
- `parts` table: part_id, part_number, revision, material, status
- `inspections` table: inspection_id, part_id, inspector_id, date, method, result (pass/fail/conditional)
- `defects` table: defect_id, inspection_id, defect_type, severity, location
- `ncmrs` table: ncmr_id, part_id, defect_id, disposition, date_opened, date_closed
- `production_runs` table: run_id, part_number, quantity, date, line_id, operator_id

---

### Key Query Patterns

**Defect rate by part number**:
```sql
SELECT
    p.part_number,
    COUNT(DISTINCT i.inspection_id) AS total_inspections,
    COUNT(DISTINCT d.defect_id) AS total_defects,
    ROUND(COUNT(DISTINCT d.defect_id) * 100.0 / COUNT(DISTINCT i.inspection_id), 2) AS defect_rate_pct
FROM parts p
JOIN inspections i ON p.part_id = i.part_id
LEFT JOIN defects d ON i.inspection_id = d.inspection_id
GROUP BY p.part_number
ORDER BY defect_rate_pct DESC;
```

**First Pass Yield (FPY) — parts passing first inspection**:
```sql
SELECT
    p.part_number,
    COUNT(*) AS total_parts,
    SUM(CASE WHEN i.result = 'pass' THEN 1 ELSE 0 END) AS first_pass,
    ROUND(SUM(CASE WHEN i.result = 'pass' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS fpy_pct
FROM parts p
JOIN (
    SELECT part_id, result,
           ROW_NUMBER() OVER (PARTITION BY part_id ORDER BY date ASC) AS rn
    FROM inspections
) i ON p.part_id = i.part_id AND i.rn = 1
GROUP BY p.part_number;
```

**Open NCMRs by disposition**:
```sql
SELECT
    disposition,
    COUNT(*) AS open_count,
    AVG(DATEDIFF(day, date_opened, GETDATE())) AS avg_days_open
FROM ncmrs
WHERE date_closed IS NULL
GROUP BY disposition
ORDER BY open_count DESC;
```

**Defect Pareto (top defect types)**:
```sql
SELECT
    defect_type,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS pct_of_total,
    SUM(COUNT(*)) OVER (ORDER BY COUNT(*) DESC) AS running_total,
    SUM(SUM(COUNT(*)) OVER()) AS grand_total
FROM defects
GROUP BY defect_type
ORDER BY count DESC;
```

**Trend over time — weekly defect count**:
```sql
SELECT
    DATEPART(year, i.date) AS year,
    DATEPART(week, i.date) AS week,
    COUNT(d.defect_id) AS defect_count
FROM inspections i
LEFT JOIN defects d ON i.inspection_id = d.inspection_id
GROUP BY DATEPART(year, i.date), DATEPART(week, i.date)
ORDER BY year, week;
```

**Join types — when to use which**:
- INNER JOIN: Only matching rows in both tables. Use for "show me inspections that have defects."
- LEFT JOIN: All rows from left + matching from right (NULLs where no match). Use for "all parts, including those with no defects."
- RIGHT JOIN: Inverse of LEFT (less commonly used; rewrite as LEFT JOIN by swapping tables).
- FULL OUTER JOIN: All rows from both tables. Use for reconciliation — "show me mismatches between inspection system and ERP."

**Window functions** (advanced, shows sophistication):
```sql
-- Running cumulative defect count per line
SELECT
    line_id,
    date,
    defect_count,
    SUM(defect_count) OVER (PARTITION BY line_id ORDER BY date) AS cumulative_defects
FROM daily_line_defects;
```

---

## 9. Power BI for Quality/Reliability Dashboards

### Core Competencies Expected

**Data model design**:
- Star schema: Central fact table (inspections, defects, NCMRs) surrounded by dimension tables (parts, operators, dates, machines).
- Avoid snowflaking unnecessarily — performance cost.
- Relationships: define on key columns, set correct cardinality (one-to-many most common).

**DAX (Data Analysis Expressions) — essential formulas**:

```dax
-- Defect Rate
Defect Rate % =
DIVIDE(
    COUNTROWS(Defects),
    DISTINCTCOUNT(Inspections[inspection_id]),
    0
) * 100

-- First Pass Yield
FPY % =
VAR TotalParts = DISTINCTCOUNT(Parts[part_id])
VAR PassParts = CALCULATE(DISTINCTCOUNT(Parts[part_id]),
    Inspections[result] = "pass",
    Inspections[attempt_number] = 1)
RETURN DIVIDE(PassParts, TotalParts, 0) * 100

-- MTTR (Mean Time to Resolve NCMRs)
Avg Days to Close =
AVERAGEX(
    FILTER(NCMRs, NOT ISBLANK(NCMRs[date_closed])),
    DATEDIFF(NCMRs[date_opened], NCMRs[date_closed], DAY)
)

-- OEE
OEE =
[Availability %] / 100 * [Performance %] / 100 * [Quality %] / 100 * 100
```

**Visualization best practices for quality dashboards**:
- KPI cards at the top: FPY %, Defect Rate, Open NCMRs, OEE.
- Trend line charts: Defect rate over time with control limit reference lines.
- Pareto chart: Defect type frequency + cumulative % (bar + line combo).
- Heat maps: Defect location on part (using custom background image).
- Slicers: Part number, date range, production line, inspector, defect type.
- Drill-through: Click a part number → see all inspections and NCMRs for that part.

**Key manufacturing KPIs to know**:
- **OEE** = Availability × Performance × Quality (world-class ≥ 85%)
- **First Pass Yield (FPY)**: % parts passing first inspection without rework
- **Escaped defect rate**: Defects that reached next assembly stage or customer
- **NCMR cycle time**: Days from open to disposition
- **Scrap rate**: % (by count or cost)
- **Cpk trend**: Process capability over time

---

## 10. Tooling Design — Fixtures, Jigs, Work Access

### Core Principles

**3-2-1 locating principle**: Position a part using:
- 3 points on primary datum surface (constrains 3 DOF: Z translation, and X and Y rotation)
- 2 points on secondary datum surface (constrains 2 DOF: Y translation and Z rotation)
- 1 point on tertiary datum surface (constrains final DOF: X translation)
Total: 6 DOF constrained = fully determined position. Over-constraining causes interference/binding.

**Fixture design checklist**:
1. Part must be located deterministically (3-2-1 or equivalent).
2. Clamping forces must not distort the part — clamp near supports.
3. Fixture must provide clear access for tools, welding torch, NDT equipment.
4. Material: Tool steel (hardened) for high-volume; aluminum or fabricated steel for lower volume.
5. Thermal expansion: If welding in fixture, account for part expansion and potential stress buildup.
6. Ergonomics: Operator must be able to load/unload part safely and efficiently.

**Jig vs fixture distinction**:
- **Jig**: Guides the cutting tool as well as holding the part (e.g., drill jig with bushing that guides drill). Self-contained.
- **Fixture**: Holds and locates part only — does not guide the tool.

**Weld fixture design considerations** (high relevance for Starship):
- Use copper or ceramic backing bars to support root pass and control penetration bead.
- Strong-backs prevent distortion during welding — hold panels flat until weld cools.
- Allowance for weld shrinkage: Pre-set the joint gap or pre-bend the part so it returns to spec after cooling.
- For robotic welding: Fixture must hold part within TCP (tool center point) repeatability — typically ±0.1 mm or better.

**Modular tooling**: Rather than one-off custom fixtures, use a system of base plates, support pillars, locators, and clamps that can be reconfigured. Faster to design and build for new parts; SpaceX's rapid iteration benefits from this.

**Work access platforms**: For Starship's large-scale structure, work platforms must be designed around the vehicle. Key considerations: OSHA and internal fall protection requirements, clearance from rotating/moving hardware, integration with overhead crane access, ability to retract quickly for hardware movement.

**Fluid system tooling** (for propellant and pneumatic lines):
- Proof pressure test fixtures: Must hold pressure to 1.5× MEOP (Maximum Expected Operating Pressure) minimum.
- Leak test fixtures: Must seal mating interfaces to allow helium or nitrogen leak testing.
- Flush fixtures: Route cleaning fluid through lines in defined sequence and flow rate.
- GSE (Ground Support Equipment): Fittings, hoses, pressure regulators, monitoring instrumentation — all must be documented and calibrated.

---

## 11. Starship-Specific Technical Knowledge

### Vehicle Architecture

**Starship system** = Super Heavy booster + Starship upper stage.
- Super Heavy: ~70 m tall, 33 Raptor engines (sea-level optimized), 3,400 tons liftoff thrust.
- Starship upper stage: ~50 m tall, 3 Raptor Vacuum + 3 Raptor sea-level.
- Full stack: ~120 m, ~5,000 tons propellant capacity (LOX + LCH4 — liquid methane).

**Tank construction**:
- Rings: Stainless steel sheet rolled into rings, stacked, and circumferentially welded.
- Common bulkhead design: Single bulkhead separates LOX and fuel tanks — reduces dry mass vs. separate tanks.
- Manufacturing location: Boca Chica, TX (Starbase) — built in the open air, iterating rapidly.

**Heat shield**: Hexagonal tiles (PICA-X ceramic tiles on windward side). Attachment and inspection is a significant manufacturing challenge.

**Catch mechanism**: SpaceX has demonstrated catching the Super Heavy booster with mechanical arms ("Mechazilla") at the launch tower — requires tight dimensional control of booster attachment points.

---

### Common Starship Build Challenges

1. **Ring-to-ring weld quality**: Circumferential welds on large-diameter rings (9 m diameter) are difficult to control consistently. Shrinkage and distortion accumulate over many stacked rings. Solution: Tight process control on heat input, inter-pass temperature, post-weld dimensional check with laser tracker.

2. **Tile attachment and inspection**: Each hexagonal heat shield tile must be individually attached and verified. Visual + tactile inspection for gaps, cracks, adhesion failures. High labor intensity.

3. **Header tank integration**: Small LOX and CH4 header tanks inside the main tanks provide propellant during engine relight for landing. Access for integration and weld inspection is constrained.

4. **Plumbing / valve assembly**: High-pressure fluid systems require cleanliness control (ASME B31.3 / NASA-STD-6001 for oxygen service), correct torque, leak testing, and material compatibility verification.

5. **Avionics harness routing**: Long cable runs through the vehicle require routing, strain relief, protection from structure, and continuity/isolation testing.

6. **Cryogenic insulation**: Foam insulation on cryogenic lines and common bulkhead requires controlled application and adhesion verification.

7. **Scale**: Starship is the largest rocket ever built. Conventional aerospace tooling approaches don't scale. SpaceX has developed purpose-built jacking, rotation, and transport equipment for a 9-meter-diameter vehicle.

---

### Raptor Engine — Technical Details

**Cycle**: Full-flow staged combustion (FFSC). Both propellant streams (fuel-rich and oxidizer-rich) are fully gasified before entering the main combustion chamber. Most efficient thermodynamic cycle possible for chemical rockets.

**Two pre-burners**:
- Fuel-rich pre-burner: Burns CH4 + small O2 → hot fuel-rich gas drives fuel turbopump.
- Oxidizer-rich pre-burner: Burns O2 + small CH4 → hot O2-rich gas drives oxidizer turbopump.
Both streams then combine in main combustion chamber.

**Propellants**: Liquid methane (LCH4) + liquid oxygen (LOX). Methalox chosen for:
- Higher Isp than kerosene (RP-1)
- Producible on Mars from CO₂ + H₂O (in-situ resource utilization)
- Cleaner combustion — less coking
- Better cryogenic storage density than liquid hydrogen

**Chamber pressure**: ~300 bar (Raptor 2/3) — among the highest of any production rocket engine. Higher pressure = higher efficiency but tighter manufacturing tolerances on combustion chamber, injectors, and seals.

**Materials**: SX500 proprietary alloy for parts exposed to hot oxygen-rich gas. 3D printed components (selective laser melting/SLM) for complex injector and turbopump geometries.

**Manufacturing improvements** (Raptor 3):
- Part count reduced ~30% through 3D printing consolidation.
- Integrated turbopump housing (formerly multiple welded pieces).
- Single-piece nozzle throat section.
- Target: 300+ engines/year production rate.
- Elimination of engine heat shield via internalized regenerative cooling paths.

---

## 12. Manufacturing & Assembly Processes

### Avionics Integration

**Key steps**:
1. Wire harness fabrication: Cut, strip, crimp, label per wiring diagram.
2. Harness testing: Continuity, isolation, hi-pot (high potential) dielectric testing.
3. Installation: Route per drawing, secure with clamps and tie-wraps, protect at structural pass-throughs with grommets.
4. Connector mating: Correct pin insertion, backshell torque, safety wire as required.
5. System-level functional testing: Power on, verify all signals, test each function.
6. Environmental acceptance testing: Vibration, thermal vacuum (for space hardware).

**Common defect modes**:
- Wrong pin insertion (connector keying must be verified).
- Chafing at sharp edges.
- Insufficient bend radius causing conductor fatigue.
- Moisture ingress in non-hermetic connectors.

---

### Valve and Fluid System Assembly

**Cleanliness classes** for oxygen service — critical for Starship:
- Oxygen systems require extremely clean surfaces (ASTM G93 / ASME G 4.6) to prevent ignition from contamination + high-pressure O2 impact.
- Cleaning procedure: Degrease → precision clean → clean room assembly → seal immediately.
- Verification: Particulate and NVR (non-volatile residue) analysis of flush samples.

**Torque control**: All fasteners on fluid systems torqued to specification with calibrated torque wrench; documented on assembly traveler.

**Leak testing sequence**:
1. Soap bubble test (gross leaks at low pressure).
2. Helium mass spectrometer leak test (HMSL): Leak rate in std cc/s or mbar·L/s.
3. Proof pressure test: Pressurize to 1.5× MEOP, hold, verify no permanent deformation.
4. Functional test: Cycle valve, verify actuation, flow rate, pressure drop.

---

### Thermal Systems

**Thermal protection approaches on Starship**:
- Windward side: PICA-X ablative ceramic tiles (passive).
- Leeward side: Stainless steel radiates and withstands reentry heating without tiles.
- Cryogenic lines: Foam/MLI (multi-layer insulation) reduces heat leak into propellants.

**Manufacturing considerations**:
- Tile installation requires clean, prepared surface (adhesive bond to vehicle structure).
- Tile gap control: Must accommodate thermal expansion during reentry while preventing hot gas ingestion.
- MLI blanket installation: Layer count and seam placement are quality-critical.

---

## 13. Common Interview Questions and Strong Answers

### Technical Questions

**Q: Why does aerospace rely on Profile of a Surface instead of Flatness?**
A: Flatness controls only the form of a surface in isolation — it tells you the surface is flat relative to itself, but says nothing about where it is in 3D space. Profile of a Surface simultaneously controls the form, orientation, and location of the surface relative to the datum reference frame. For aerospace structures where surfaces must interface with mating parts at specific orientations and positions, Profile of a Surface ensures the complete geometric requirement is met. Flatness alone could produce a perfectly flat surface that is tilted at the wrong angle or in the wrong location.

**Q: Walk me through how you would resolve a weld defect found on a Starship tank ring.**
A: First, physically quarantine the affected section and write an NCMR documenting the defect — type, location, extent, and how it was found. Then characterize the defect fully using the appropriate NDE methods (UT for depth/extent, PT for any surface cracks, RT if volumetric). Take the documented data to MRB with the design engineer: can this be repaired (weld repair and re-inspect), used as-is with engineering justification, or must it be scrapped? Simultaneously initiate a root cause investigation — was this a welder certification issue, a process parameter drift, a contaminated filler, a fixture problem? Implement containment on all similar parts that may have the same root cause. After disposition, close the NCMR with corrective action that prevents recurrence.

**Q: Cpk of 0.9 on a critical weld dimension. What do you do?**
A: This process is incapable (Cpk < 1.33 target, < 1.0 is immediately actionable). First, verify the measurement system is adequate — run a Gauge R&R study to ensure you're measuring real process variation, not measurement error. Then do a process study: plot control charts to distinguish common-cause (all the variation is the process) from special-cause variation (something changed). Pareto the out-of-spec occurrences by time, operator, fixture, material batch. Use the 5-Why or Fishbone diagram to get to root cause. Corrective actions might include tighter process parameter control, fixture improvement, new weld procedure, or reconsidering the design tolerance (if it's tighter than necessary for function, engaging with engineering on a tolerance relaxation is a valid path — challenge the requirement).

**Q: You have 24 hours to produce a metal prototype bracket. What process do you choose?**
A: It depends on the material and geometry. For a simple shape: laser cutting from sheet + brake forming is fastest (hours). For a machined shape: CNC from billet aluminum or steel — setup and run time likely fits in 24h for a single part. For complex internal geometry: 3D printing (SLM/DMLS for metal) can produce in 12–20h without fixturing or tooling. Casting is out — lead time for tooling is weeks. I'd lean toward machining for dimensional accuracy, or additive if geometry can't be machined conventionally. I would not compromise on inspection — the bracket still needs to be measured.

**Q: What's the difference between FMEA and FTA, and when would you use each?**
A: FMEA is inductive/bottom-up — you start with all the ways individual components can fail and trace effects upward to system level. It's broad and systematic, ideal early in design to capture all failure modes. FTA is deductive/top-down — you start with a specific catastrophic event and work backward to identify contributing causes. It quantifies probability of a specific top-level failure. I use FMEA to build a comprehensive failure mode catalog and prioritize by RPN. I use FTA when I need to analyze a specific hazard (say, LOX/fuel mixing due to valve failure) and calculate probability for safety case compliance. They complement each other well.

**Q: How does EMAT work and why is it preferable to conventional UT for austenitic stainless steel?**
A: EMAT uses electromagnetic induction — a static magnetic field and an RF coil generate eddy currents in the material surface. The Lorentz force on those currents launches ultrasonic waves directly into the part without any physical coupling medium. For austenitic stainless, the coarse dendritic grain structure created during welding is highly anisotropic — it scatters and skews longitudinal ultrasonic waves used in conventional UT, causing noise and missed indications. EMAT can generate shear horizontal (SH) waves, which propagate through austenitic grain structures with much less scattering. Additionally, the no-couplant requirement is a practical advantage for large Starship structures where applying and removing couplant on every weld would be slow and messy.

**Q: Starship is built from stainless steel. Walk me through the tradeoffs SpaceX made.**
A: The conventional choice would be carbon fiber composites (like Falcon 9's payload fairing) or aluminum alloys. Composites offer the best mass fraction but are expensive, slow to iterate, and mechanically difficult at cryogenic extremes. Aluminum has good cryogenic behavior but can't survive reentry temperatures above its melting point (~660°C). Stainless steel's key advantages for Starship: at cryogenic temperatures it gains ~50% strength (austenite doesn't undergo ductile-to-brittle transition like BCC alloys); it can radiate heat during reentry rather than needing full TPS coverage; it's orders of magnitude cheaper and has short supply lead times enabling weekly iteration; 304L's low carbon content makes it readily weldable. The tradeoff is mass — stainless is ~2.5x denser than aluminum — but Elon Musk has said the mass penalty is acceptable because of cost, iteration speed, and cryogenic/thermal performance.

---

## 14. Key Formulas Quick Reference

| Formula | Variables |
|---|---|
| RPN = S × O × D | Severity, Occurrence, Detection (each 1–10) |
| Cpk = min[(USL−μ)/3σ, (μ−LSL)/3σ] | Mean (μ), std dev (σ), spec limits |
| True Position = 2√[(Δx)²+(Δy)²] | Δx, Δy = deviations from true position |
| R(t) = e^(−(t/η)^β) | Weibull reliability; t = time, η = scale, β = shape |
| F(η) = 1 − e^(−1) = 63.2% | Characteristic life definition |
| OEE = A × P × Q | Availability, Performance, Quality (decimal) |
| MTBF = 1/λ | λ = failure rate (for exponential/constant rate) |
| Bonus tolerance = |actual size − MMC| | Applies when Ⓜ modifier used |
| Heat input (J/mm) = (V × I × 60) / speed | V = volts, I = amps, speed = mm/min |
| Positional RPN priority: always check S=10 separately | Even low RPN with max severity is critical |

---

## Sources

Research for these notes draws from:

- [SpaceX Build Reliability Engineer Interview Questions — Glassdoor](https://www.glassdoor.com/Interview/SpaceX-Build-Reliability-Engineer-Interview-Questions-EI_IE40371.0,6_KO7,33.htm)
- [SpaceX Engineering Interview Questions — Snubber (Ex-SpaceX Engineer)](https://snubber.ai/blog/spacex-interview-questions)
- [Starship Build Reliability Engineer role description — Vaia Talents](https://talents.vaia.com/companies/spacex/starship-build-reliability-engineer-27455993/)
- [SpaceX's Five-Step Engineering Algorithm — Aviation Week](https://aviationweek.com/space/commercial-space/algorithm-spacexs-five-step-process-better-engineering)
- [NDT Methods — ASNT](https://www.asnt.org/what-is-nondestructive-testing/methods)
- [EMAT Technology — Innerspec](https://www.innerspec.com/emat-technology)
- [EMAT Inspection Guide — Voliro](https://voliro.com/blog/emat-inspection/)
- [Electromagnetic Acoustic Transducer — NDE-Ed (Iowa State)](https://www.nde-ed.org/NDETechniques/Ultrasonics/EquipmentTrans/emats.xhtml)
- [Aerospace NDT — ASNT Industries](https://www.asnt.org/what-is-nondestructive-testing/industries/aerospace)
- [Aerospace NDT Methods (Nadcap) — Avior](https://www.avior.ca/blog/aerospace-ndt-methods-nadcap-approved/)
- [FMEA — Wikipedia](https://en.wikipedia.org/wiki/Failure_mode_and_effects_analysis)
- [Fault Tree Handbook — NASA](https://www.mwftr.com/CS2/Fault%20Tree%20Handbook_NASA.pdf)
- [Weibull Analysis — ReliaSoft](https://help.reliasoft.com/reference/life_data_analysis/lda/the_weibull_distribution.html)
- [Process Capability (Cp, Cpk) — 1Factory](https://www.1factory.com/quality-academy/guide-process-capability.html)
- [GD&T Symbols — GD&T Basics](https://www.gdandtbasics.com/gdt-symbols/)
- [True Position — GD&T Basics](https://www.gdandtbasics.com/true-position/)
- [AS9100 Nonconformance — Elsmar](https://elsmar.com/elsmarqualityforum/threads/as9100-control-of-nonconforming-outputs-rework-dispositions.81874/)
- [AS9100 Guide — Dickson Data](https://dicksondata.com/as9100-aerospace-quality-management)
- [AWS D17.1 Specification — AWS](https://pubs.aws.org/p/1754/d171d171m2017-amd2-specification-for-fusion-welding-for-aerospace-applications)
- [Aerospace TIG Welding — WeldingTipsAndTricks](https://www.weldingtipsandtricks.com/aerospace-tig-welding.html)
- [TIG Welding Defects — Welding and Welder](https://www.weldingandwelder.com/help-and-advice/common-tig-welding-defects-problems-and-prevention/)
- [SpaceX Raptor — Wikipedia](https://en.wikipedia.org/wiki/SpaceX_Raptor)
- [Raptor Engine — Everyday Astronaut](https://everydayastronaut.com/raptor-engine/)
- [SpaceX Materials — Jotaint International](https://jotaintl.com/about-us/academy/spacex-rocket-materials/)
- [Stainless Steel for Starship — Quora thread](https://www.quora.com/Why-is-SpaceX-switching-to-304L-stainless-steel-for-the-Starship)
- [INCONEL 718 Data Sheet — Special Metals](https://www.specialmetals.com/documents/technical-bulletins/inconel/inconel-alloy-718.pdf)
- [Siemens NX Aerospace CAD — Siemens](https://www.siemens.com/en-us/products/designcenter/nx-cad-software/workflows/aerospace-aircraft-design/)
- [Power BI Manufacturing Dashboards — ECOSIRE](https://ecosire.com/blog/power-bi-manufacturing-dashboard)
- [Aerospace Fixtures — Rayco Fixture](https://www.raycofixture.com/aerospace-jigs-fixtures-overview/)
- [Jigs and Fixtures — Xometry Pro](https://xometry.pro/en/articles/jigs-and-fixtures/)
