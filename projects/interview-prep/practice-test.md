# Practice Test — SpaceX Build Reliability Engineer (Starship)

> **Instructions:** Answer each question as you would in a live technical interview — out loud or written. Then check your answer against the answer key at the bottom. Aim for ≥80% before your interview.
>
> Time yourself: SpaceX technical interviews are fast-paced. Target 2–3 minutes per technical question, 3–4 minutes per behavioral question.

---

## SECTION A — NDT / NDE (10 Questions)

**A1.** You need to inspect a 304L stainless steel weld on a Starship propellant tank ring for internal porosity. The weld is 3 days old, the surface is rough from grinding, and the line is running at production speed. Which NDT method do you choose and why? What are the limitations of your choice?

---

**A2.** Walk me through the complete Liquid Penetrant Testing process sequence, in order. What happens if you under-wash the excess penetrant? What happens if you over-wash it?

---

**A3.** A radiographic test of a weld shows no indication of cracking. A junior engineer concludes the weld is crack-free. Is this conclusion valid? Explain.

---

**A4.** What is the minimum illumination requirement for visual inspection per most aerospace specifications, and why does it matter?

---

**A5.** Explain how EMAT generates ultrasonic waves without touching the part. Why is this physically possible only with conductive materials?

---

**A6.** A titanium bracket needs weld inspection. You have liquid penetrant, conventional UT, and EMAT available. Which do you use, when, and why?

---

**A7.** Your PT inspection reveals a linear indication 3mm long on a weld toe. Before writing the NCMR, what additional information do you need to determine if this is rejectable?

---

**A8.** What is the difference between PAUT (Phased Array UT) and conventional single-element UT? In what production scenario would PAUT justify its higher cost?

---

**A9.** A new NDT inspector consistently finds 40% fewer defects than the rest of the team on the same hardware. How do you investigate and resolve this?

---

**A10.** EMAT is described as superior for austenitic stainless steel weld inspection. Explain the metallurgical reason why conventional UT struggles with these welds.

---

## SECTION B — Welding (8 Questions)

**B1.** During TIG welding of a 304L stainless tank section, you notice the weld bead has turned gray-black. What does this indicate, and what corrective action do you take?

---

**B2.** A new welding procedure is producing welds with consistent undercut at the toes. Name three possible causes and how you would adjust the process to eliminate each.

---

**B3.** Why is back purging with argon required when TIG welding stainless steel? What happens if it is omitted?

---

**B4.** Calculate the heat input for a TIG weld with: Voltage = 12V, Current = 150A, Travel speed = 300 mm/min. Is this a high or low heat input for thin-wall stainless? What does this imply for distortion risk?

---

**B5.** A welding procedure qualification record (PQR) was completed on 6mm 304L plate. A production engineer wants to use this PQR to qualify a procedure for 2mm 304L. Is this acceptable under AWS D17.1? What are the limits on essential variables?

---

**B6.** Describe the failure modes unique to laser keyhole mode welding that do not occur in conduction mode welding. What process parameters control the transition between modes?

---

**B7.** You are reviewing a weld traveler and see that the interpass temperature was measured at 180°C before a pass was added. The spec limits it to 150°C. What do you do?

---

**B8.** Robotic TIG welding of a production ring is producing inconsistent penetration — some welds look good, others have cold laps. The weld program has not changed. What are the most likely root causes?

---

## SECTION C — Materials (6 Questions)

**C1.** A design engineer proposes switching Starship tank material from 304L to 7075-T6 aluminum to save mass. Make the strongest case for and against this change from first principles.

---

**C2.** What is sensitization in austenitic stainless steel? How does the "L" designation (304L vs 304) address it? What temperature range is dangerous?

---

**C3.** An Inconel 718 turbopump bracket has been machined and is awaiting heat treatment. An operations engineer proposes skipping the aging step to save 18 hours of furnace time. What is the risk, quantitatively if possible?

---

**C4.** A titanium weld comes out of the weld cell with a blue-purple discoloration. What does this mean, what is the likely cause, and is the part acceptable?

---

**C5.** Why are aluminum alloys generally not used for cryogenic propellant tanks on Starship? What specific material behavior at cryogenic temperatures is the concern?

---

**C6.** LOX compatibility. A technician applies a standard petroleum-based grease to a threaded fitting that will be exposed to liquid oxygen. What is the risk? What should they have used instead?

---

## SECTION D — GD&T (7 Questions)

**D1.** A drawing calls out a hole position of ∅0.5 at MMC. The hole MMC is ∅20.00 mm and the actual measured diameter is ∅20.40 mm. The hole center measured 0.22 mm from the true position in X and 0.15 mm in Y. Does this hole pass or fail? Show your work.

---

**D2.** Explain the difference between Profile of a Surface and Flatness. For a LOX inlet flange on a Starship propellant tank, which control is appropriate and why?

---

**D3.** A feature control frame reads: [Position | ∅0.3 | Ⓜ | A | B | C]. Interpret this statement completely.

---

**D4.** Why is concentricity rarely used in modern aerospace drawings despite being in the GD&T standard? What is typically used instead?

---

**D5.** A CMM report shows a cylinder's measured axis is 0.08mm from the datum axis. The drawing calls for ∅0.1 cylindricity. Does the part pass? What additional information do you need?

---

**D6.** Explain the 3-2-1 datum setup principle for a rectangular machined bracket. How many degrees of freedom does each datum constrain, and in which directions?

---

**D7.** A drawing has a basic dimension of 100mm and a position tolerance of ∅0.2. What does "basic" mean? Can the 100mm dimension be toleranced separately?

---

## SECTION E — Reliability Engineering (8 Questions)

**E1.** You are conducting a PFMEA for the robotic TIG welding process of Starship tank rings. List five distinct failure modes, assign estimated S/O/D ratings (justify each), calculate RPNs, and rank by priority. Then propose a corrective action for the top item.

---

**E2.** A pressure sensor fleet of 200 units shows the following failures in the first 500 hours of operation: 8 failures at hours 50, 80, 110, 145, 200, 260, 340, 430. What Weibull shape parameter (β) does this suggest, and what does it tell you about the failure mechanism? What do you do next?

---

**E3.** Your weld bead width measurement process has: mean = 4.2mm, std dev = 0.18mm, USL = 5.0mm, LSL = 3.5mm. Calculate Cp and Cpk. Is the process capable for a flight-critical feature?

---

**E4.** A control chart for weld penetration depth shows 9 consecutive points above the centerline but within control limits. Is the process in statistical control? What is the appropriate action?

---

**E5.** Explain the difference between MTBF and B10 life. For a flight-critical fastener with β = 4.5 and η = 50,000 cycles, calculate the B10 life. Is it safe to use MTBF as the replacement interval for this fastener?

---

**E6.** A weld inspection process has Cpk = 1.1 and Ppk = 0.75. A manufacturing engineer says "Cpk is above 1.0, we're fine." What do you tell them?

---

**E7.** Construct a simple fault tree for the top event: "Propellant leak at tank weld joint." Include at least two levels with AND and OR gates and identify single-point failures.

---

**E8.** Your FPY on a critical subassembly is 78%. The line manager wants to add a rework station to fix the 22% failures rather than find root cause. What is the problem with this approach? How do you calculate the process's true cost?

---

## SECTION F — Quality Systems and Manufacturing (6 Questions)

**F1.** You are the quality engineer on shift and an inspector brings you a Starship tank ring weld that failed radiographic inspection — it shows a 12mm linear indication near the root. Production is 6 hours behind schedule and the launch window is in 3 weeks. Walk me through every step you take.

---

**F2.** A supplier delivers 50 titanium brackets. Upon incoming inspection, 8 of them show incorrect alloy designation on the certs — the certs say Ti-3Al-2.5V but the PO specifies Ti-6Al-4V. What do you do?

---

**F3.** An engineer proposes a "Use As Is" disposition on a Starship LOX tank fitting that has a thread engagement depth 15% below the minimum specified in the drawing. Write the engineering rationale you would require before approving this UAI.

---

**F4.** What is First Article Inspection (FAI) per AS9102? When is it required? What happens if a design change is made to a part that previously passed FAI?

---

**F5.** Write the SQL query to find all part numbers where the NCMR rate (NCMRs per 100 parts inspected) exceeded 5% in the last 90 days. Use these tables: `parts(part_id, part_number)`, `inspections(inspection_id, part_id, inspection_date)`, `ncmrs(ncmr_id, part_id, date_opened)`.

---

**F6.** A root cause analysis using 5-Why on a recurring weld porosity issue identifies "operator did not follow pre-weld cleaning procedure." Stop here — is this a valid root cause? If not, what is the next question to ask?

---

## SECTION G — Behavioral / Situational (5 Questions)

**G1.** Tell me about the most technically difficult manufacturing problem you have solved. Be specific about what you did personally.

---

**G2.** Describe a time you disagreed with a design engineer's decision about a manufacturing process. What did you do, and what was the outcome?

---

**G3.** You are a new BRE at Starbase and on your third week you notice that the pre-weld cleaning procedure hasn't been followed correctly for the last two shifts. No NCMRs have been written. The parts are already further along in the assembly. What do you do?

---

**G4.** SpaceX moves fast and sometimes ships hardware that isn't perfect. How do you personally decide when something is "good enough to fly" versus when you would stop production?

---

**G5.** Give me an example where you used data to change someone's mind. What was the data, what was the decision, and what happened?

---

---

# ANSWER KEY

> **How to score yourself:** Give yourself full credit if your answer hits all the bold-marked key points. Partial credit if you get the core concept but miss specifics.

---

## Section A Answers

**A1.** → **EMAT** is the correct primary choice for production-speed inspection of stainless weld with rough surface. **Key points:** No couplant required (rough surface doesn't matter), SH waves aren't scattered by austenitic grain structure, can run at production speed. **Add:** Combine with RT to catch volumetric porosity that UT might miss. **Limitations:** EMAT has lower sensitivity than contact UT; heavier probes; requires conductive material; won't work on non-metallic coatings.

**A2.** → Sequence: **Pre-clean → Apply penetrant → Dwell → Remove excess → Apply developer → Inspect → Post-clean**. Under-wash = residual penetrant remains on surface → false positive indications everywhere. Over-wash = real penetrant drawn out of tight defects → false negatives; actual defects are missed.

**A3.** → **Not valid.** RT is orientation-dependent. A crack parallel to the X-ray beam will be essentially invisible — the radiation passes through both sides of the crack with negligible contrast difference. The correct statement is: "No indication was found at the tested beam angles." Must specify that it is not a comprehensive crack-free certification unless multiple angles were used or supplemented with UT.

**A4.** → **100 foot-candles (approximately 1075 lux)**. Matters because defects that are visually detectable at correct illumination become invisible in dim conditions — insufficient light causes missed indications, which are far more dangerous than false positives.

**A5.** → A **static magnetic field** is applied. An **RF coil** passes alternating current, inducing **eddy currents** in the conductive surface layer. The Lorentz force interaction (F = qv × B) between moving charges (eddy currents) and the static magnetic field creates mechanical stress waves (ultrasound) inside the material. Requires electrical conductivity because eddy currents cannot be induced in non-conductive materials.

**A6.** → **PT first** (surface cracks, surface-open porosity — quick, cheap). **Conventional UT or EMAT second** for subsurface flaws in the weld body. **Note:** Titanium is not austenitic stainless, so conventional UT is less problematic than for 304L. However, titanium's fine grain structure means UT works well. **Key point:** PT is always done before UT/EMAT; visual inspection before all.

**A7.** → Need: (1) **AWS D17.1 weld class** (A, B, or C) — acceptance criteria differ. (2) **Weld type** (groove, fillet, partial penetration) — different limits. (3) **Orientation** — linear indications are more severe than rounded. (4) **Is the indication confirmed real or a false indication** (PT artifact, scratch). A 3mm linear indication may be rejectable under Class A but acceptable under Class C.

**A8.** → PAUT uses an array of elements electronically steered to produce **multiple beam angles simultaneously**, generating a cross-sectional image (B-scan or S-scan) in a single pass. Conventional UT requires manual repositioning for each angle. **Justify cost** when: large volume of welds to inspect on a production schedule, complex joint geometries requiring multiple angles, or where flaw characterization (size/depth) is required rather than just detection.

**A9.** → **Structured approach:** (1) Have the low-detector perform a **blind re-inspection** of hardware that another inspector already documented defects on — to see if they find those known defects. (2) Observe the inspector's technique directly. (3) Check if equipment calibration is different. (4) Review lighting conditions at their station. **Root cause options:** inadequate training, technique deviation, different interpretation of acceptance criteria, equipment issue. Resolve: side-by-side demonstration, calibration verification, training, possibly re-inspection of all hardware inspected by that individual.

**A10.** → Austenitic stainless steel (304L) welds solidify with a **coarse, columnar dendritic grain structure** with strong **crystallographic anisotropy**. Conventional UT uses longitudinal (compressional) waves which are highly scattered at grain boundaries in this anisotropic structure, causing **beam skewing, mode conversion, and high noise**. This makes real defect signals hard to distinguish from grain noise, and can deflect the beam around actual defects. EMAT's **shear horizontal (SH) waves** have particle motion parallel to the surface and transverse to the propagation direction — this wave mode interacts differently with grain boundaries and experiences far less scattering, making defect detection reliable.

---

## Section B Answers

**B1.** → Gray-black color = **severe oxidation** of the weld metal, indicating **inadequate shielding gas coverage** (too little post-flow, contaminated gas, nozzle distance too great, or draft in the environment). **Actions:** (1) Stop welding. (2) Write NCMR — weld is rejectable per AWS D17.1. (3) Check gas flow rate (typically 15–25 CFH for TIG), post-flow timer, nozzle condition, and area for air drafts. (4) Inspect the weld by PT and UT/RT before dispositioning. (5) Do not attempt to brush off oxidation and continue — the base metal underneath may be sensitized.

**B2.** → Causes of undercut: (1) **Current too high** — reduce amperage 5–10%. (2) **Arc length too long (excessive voltage)** — bring torch closer to maintain shorter arc. (3) **Travel speed too fast at toes** — slow travel and weave slightly to fill toes. (4) **Torch angle** — adjust angle so heat distribution is more symmetric at toes.

**B3.** → When stainless is heated by the arc, the **back side of the weld root** is also hot and exposed to atmosphere. Oxygen reacts with chromium to form chromium oxide — the critical element for corrosion resistance — depleting it from the weld root. The back purge excludes oxygen from the root and ID surface during welding. Without it: black oxidized roots, loss of corrosion resistance, potential sensitization, and reduced mechanical properties at the root. For Starship LOX tanks this is especially critical — oxidized particles can become FOD in oxygen-wetted systems.

**B4.** → H = (12 × 150 × 60) / 300 = **360 J/mm**. For thin-wall stainless (2–4mm Starship sections), 360 J/mm is **moderate to high**. High heat input on thin wall = significant distortion risk and wider HAZ → increased sensitization concern. **Implication:** Consider reducing to <250 J/mm by reducing current, increasing travel speed, or using pulsed TIG to reduce average heat input.

**B5.** → **Not automatically acceptable.** AWS D17.1 defines essential variables for the WPS — changes in base metal thickness beyond a certain ratio require re-qualification. Specifically, going from 6mm to 2mm is outside typical thickness qualification range (usually the PQR qualifies thicknesses from 50% to 200% of the test plate thickness, so 3mm–12mm range). **Need a new PQR** on representative thickness to properly qualify the procedure.

**B6.** → **Keyhole mode unique failure:** Keyhole collapse — the vapor capillary suddenly closes, trapping gas → **subsurface porosity**. This does not occur in conduction mode (no keyhole). **Controlling parameters:** Power density (W/mm²) is the primary parameter — determined by laser power ÷ focal spot area. Speed, focal position (above/at/below surface), and shielding gas composition also affect mode. The transition is not abrupt — there is a regime where the mode is unstable.

**B7.** → **(1) Stop and quarantine** — do not allow additional weld passes until the issue is resolved. **(2) Write a hold** — the heat-affected zone of that pass already experienced >150°C interpass temp. **(3) Evaluate** — contact Quality Engineering. Depending on how much above 150°C (180°C is marginal, not extreme), the disposition options are: (a) Scrap the weld and re-prep, (b) Request engineering review for Use As Is with justification, (c) Require additional NDE (PT + RT + UT) to verify no HAZ damage. **(4) Root cause** — investigate: Is the interpass thermometer calibrated? Was the 150°C limit in the WPS clearly communicated? Add a mandatory cool-down step and verification checkpoint to the work instructions.

**B8.** → Most likely root causes for variable penetration with unchanged program: **(1) Joint fit-up variation** — gap between panels not consistent; wider gap = less penetration, deeper penetration on other areas. (2) **Fixture wear** — parts not held consistently in position relative to welding head. (3) **Wire feed issues** — for MIG; incorrect filler contact or contamination for TIG. (4) **Base metal surface condition** — varying oxide layer, oil contamination. (5) **Seam tracking failure** — robotic seam tracker losing the joint. Investigate with weld data logging (current, voltage, speed), review fixture inspection records, and check material certifications for batch variation.

---

## Section C Answers

**C1.** → **Against aluminum:** (1) Melts at 660°C — reentry peak skin temps can exceed this at some locations. (2) At cryogenic temps (LOX = -183°C), Al becomes more brittle and ductility decreases — risk of crack propagation at stress concentrations. (3) Al is difficult to weld in thick sections without distortion. (4) 7075 specifically is not weldable — prone to hot cracking. **For aluminum:** Mass savings could be significant (density 2.81 vs 7.93 g/cm³). But the mass penalty of SS is traded against: higher strength at cryo (less material needed), no need for thermal protection system at some locations, weldability, cost, and iteration speed. **Bottom line:** The tradeoff does not favor aluminum for Starship — the specific locations where aluminum fails (cryo embrittlement, reentry temps) are the exact locations Starship operates.

**C2.** → Sensitization = **chromium carbide (Cr₂₃C₆) precipitation at grain boundaries** when austenitic SS is held in the 450–850°C "sensitization range." The precipitation depletes the zone adjacent to grain boundaries of chromium below the ~12% needed for passivation → intergranular corrosion susceptibility. **"L" grade** (304L): max 0.03% carbon vs 0.08% in standard 304. Lower C means less chromium carbide can form, drastically reducing sensitization tendency. **Dangerous range:** 450–850°C (approximately 840–1560°F). Normal TIG interpass temperature limit of 150°C keeps parts below the sensitization range.

**C3.** → Inconel 718's strength comes from **gamma-prime and gamma-double-prime precipitates** — these form only during the aging heat treatment. Without aging: yield strength drops from ~1030 MPa (aged) to **~550–700 MPa (annealed)** — a >30% loss. **Risk:** The bracket would be significantly understrength. At turbopump operational loads and temperatures, fatigue life would be dramatically reduced. **Never skip aging on Inconel 718.** The corrective action if this happened is to re-run the full heat treatment (solution anneal + double age) — the cycle can be repeated.

**C4.** → Blue-purple discoloration on titanium weld = **oxygen contamination** of the weld at elevated temperature. Titanium is highly reactive with O₂ above ~400°C. Contamination above ~0.3% by weight causes embrittlement — the titanium becomes brittle and can fracture at low strain. **Likely cause:** Trailing gas shield inadequate, shielding gas contaminated, or gas ran out. **Acceptability:** Per most aerospace specs and AWS D17.1, blue-purple is **rejectable** — the part must be scrapped or repaired if structurally possible. Do not grind and attempt to re-weld without resolving the shielding issue.

**C5.** → At cryogenic temperatures, aluminum alloys experience **reduced fracture toughness** (lower KIc) compared to room temperature. While yield strength may increase slightly, the material becomes more susceptible to crack initiation and propagation at stress concentrations (holes, weld toes, surface defects). Austenitic stainless steel, by contrast, does not undergo a ductile-to-brittle transition at low temperatures — its FCC crystal structure maintains ductility. For LOX tanks at -183°C, a brittle fracture mode in aluminum would be catastrophic with no warning.

**C6.** → **Catastrophic fire/explosion risk.** Liquid oxygen is a powerful oxidizer — hydrocarbon lubricants (petroleum-based greases) are fuels. The combination can detonate with minimal ignition energy. A threaded joint with petroleum grease wetted by LOX is a potential explosive system. **Should have used:** Krytox (PTFE-based fluorinated lubricant), Braycote, Fluorolube, or other oxygen-compatible lubricants that are non-flammable and non-reactive with LOX. This is a safety stop — work should have been halted before LOX exposure and proper material substituted.

---

## Section D Answers

**D1.** → **Step 1:** Calculate actual positional deviation.
Δx = 0.22mm, Δy = 0.15mm
Deviation = 2 × √(0.22² + 0.15²) = 2 × √(0.0484 + 0.0225) = 2 × √0.0709 = 2 × 0.2663 = **0.533mm**

**Step 2:** Calculate effective tolerance.
Actual hole = 20.40mm; MMC = 20.00mm; Bonus = 20.40 − 20.00 = 0.40mm
Effective tolerance = 0.50 + 0.40 = **0.90mm**

**Step 3:** Compare. 0.533mm ≤ 0.90mm → **PASS** ✓

**D2.** → Flatness: Form only. No datum. The surface is within two parallel planes. Does not tell you *where* those planes are in space. Profile of a Surface: Controls form + orientation + location relative to the datum reference frame. **For a LOX inlet flange:** Profile of a Surface is correct — the flange must be flat AND in the right location relative to the bolt pattern and pipe centerline to seal properly. Flatness alone could let the flange be flat but tilted or offset, causing leaks.

**D3.** → The hole's axis must be located within a **cylindrical tolerance zone of diameter 0.3mm** positioned at the **theoretically exact (basic) location** defined by datums A, B, and C. The Ⓜ indicates **MMC modifier** — so the stated 0.3mm tolerance applies at MMC; bonus tolerance is available as the hole departs from MMC. The cylindrical zone is oriented and located by the datum reference frame: A (primary), B (secondary), C (tertiary), applied in that order.

**D4.** → Concentricity is measured using the **median points** of diametrically opposed surface elements — a statistical concept that is extremely difficult to measure with standard CMM or hand tools. It is also hypersensitive to surface form errors. **Runout** (Total Runout or Circular Runout) is used instead — it controls the same functional requirement (coaxiality) and is directly measurable with a dial indicator and V-blocks or spindle. Total Runout is a more conservative and practical control.

**D5.** → **Cannot determine pass/fail from this information alone.** The drawing specifies **cylindricity** (∅0.1), not position. Cylindricity controls the entire cylinder surface simultaneously — it requires that all surface points lie within two concentric cylinders separated by 0.1mm. The 0.08mm offset described is a **location** measurement (distance from datum axis) — this would be relevant for **concentricity or total runout**, not cylindricity. Need a full cylindricity measurement: sweep the entire surface, compare to least-squares best-fit cylinder.

**D6.** → Primary datum (large flat surface): **3 points of contact → removes 3 DOF** (translation in Z, rotation around X axis, rotation around Y axis). Secondary datum (long edge): **2 points of contact → removes 2 DOF** (translation in Y, rotation around Z axis). Tertiary datum (short edge or end): **1 point of contact → removes 1 DOF** (translation in X). Total: all 6 DOF constrained. The part is fully located without being over-constrained.

**D7.** → A **basic dimension** (shown in a rectangular box) is a theoretically exact value — it defines the perfect, nominal location, size, or angle from which tolerances are measured by GD&T controls (feature control frames). **Basic dimensions have no tolerance of their own.** No, the 100mm cannot have a separately applied ±tolerance — that would conflict with the GD&T intent. The tolerance is entirely captured by the position tolerance callout in the feature control frame (e.g., ∅0.2 at MMC).

---

## Section E Answers

**E1.** → Sample PFMEA (acceptable answers will vary — key is the reasoning):

| Failure Mode | Effect | S | O | D | RPN | Priority |
|---|---|---|---|---|---|---|
| Porosity in weld | Structural weakness, potential fracture | 9 | 3 | 4 | 108 | 1 |
| Incorrect filler wire alloy | Wrong chemistry, reduced strength | 8 | 2 | 6 | 96 | 2 |
| Wrong interpass temp | Sensitization, corrosion susceptibility | 7 | 3 | 5 | 105 | 3 |
| Incomplete fusion at root | Crack initiation site | 9 | 2 | 5 | 90 | 4 |
| Tungsten inclusion | Stress concentration, reduced fatigue life | 7 | 2 | 4 | 56 | 5 |

**Top item corrective action (Porosity):** Add automated real-time gas purity monitor with interlock (cannot weld if purity below spec → O from 3 to 1). Add RT to all flight-critical welds (D from 4 to 2). New RPN = 9×1×2 = 18.

**E2.** → Failures early in life (8 failures in first 500 hours, with failure times spreading out) suggest **β < 1 — infant mortality region**. The decreasing rate (gap between early failures is small; gap later is large) is characteristic of early-life failures from manufacturing or assembly defects. **Action:** (1) Perform Weibull analysis — plot median ranks vs. failure times, fit β. (2) If β < 1 confirmed, implement **burn-in testing** — run sensors for 200–300 hours before deployment to weed out infant mortality failures. (3) Root cause analysis: what manufacturing defect is causing early failure? (solder quality, contamination, mechanical stress during assembly).

**E3.** →
σ = 0.18mm, μ = 4.2mm, USL = 5.0mm, LSL = 3.5mm

Cp = (5.0 − 3.5) / (6 × 0.18) = 1.5 / 1.08 = **1.39**

Cpk = min[(5.0 − 4.2)/(3 × 0.18), (4.2 − 3.5)/(3 × 0.18)]
     = min[0.8/0.54, 0.7/0.54]
     = min[1.48, 1.30]
     = **1.30**

**Assessment:** Cp = 1.39 shows adequate spread. Cpk = 1.30 shows slight off-centering toward LSL. For a **flight-critical feature** requiring Cpk ≥ 1.67, this process is **NOT capable** — action required. For a non-flight-critical feature (Cpk ≥ 1.33 acceptable), it is marginally capable. Recommendation: shift process mean toward USL side (target ~4.25mm) to improve Cpk.

**E4.** → **No, the process is NOT in statistical control.** Eight consecutive points on one side of the centerline is one of the standard Western Electric run rules indicating a **special-cause variation** (non-random pattern). Even though all points are within ±3σ control limits, the run rule detects a shift in process mean. **Action:** Immediately investigate what changed when the run started: new material batch, shift change, fixture adjustment, tool wear, environmental condition. Do not simply wait to see if it corrects itself.

**E5.** → **MTBF** is the mean time between failures for an exponential distribution (β=1, constant failure rate). It equals η when β=1. **B10** is the time at which 10% of the population has failed — a design life metric.

B10 = η × [−ln(0.90)]^(1/β) = 50,000 × [−ln(0.90)]^(1/4.5) = 50,000 × [0.10536]^(0.2222)
    = 50,000 × 0.632^0.222 ≈ 50,000 × 0.908 ≈ **45,400 cycles** (approximately)

**MTBF is NOT a safe replacement interval** for β > 1. MTBF for a Weibull distribution is η × Γ(1 + 1/β) — for β=4.5, Γ(1.22) ≈ 0.91, so MTBF ≈ 45,500 cycles. But at t = MTBF, **~63.2% of the population has failed** (that's the definition of η). Setting replacement at MTBF would tolerate an unacceptable failure rate. Use B1 or B5 for flight-critical fasteners.

**E6.** → **They're wrong — the Ppk gap is a critical finding.** Cpk = 1.1 (short-term): the process is marginally capable within a subgroup — spread is acceptable in the short term. **But Ppk = 0.75 (long-term): the process is NOT capable over time.** The large Cpk-Ppk gap means the process is **shifting significantly** between subgroups — operator-to-operator, shift-to-shift, batch-to-batch, or machine state changes. A Ppk of 0.75 means the process produces non-conformances at a significant rate when viewed over the full production run. **Action needed:** Identify sources of between-subgroup variation (MSA/Gauge R&R study, operator comparisons, fixture re-qualification).

**E7.** → Sample fault tree:

```
TOP EVENT: Propellant leak at tank weld joint
                          |
                      [OR GATE]
            ________________|________________
           |                                 |
    Weld Failure                    Seal/Joint Failure
    (structural)                    (non-weld)
           |                                 |
       [OR GATE]                         [OR GATE]
      ______|______              _____________|___________
     |             |            |                         |
  Crack        Porosity    O-ring failure         Fitting overtorque
  in weld      in weld     (single-point)         (single-point)
     |
  [OR GATE]
  ____|____
 |         |
Weld     Fatigue     
defect   crack
(mfg)    (operational)
```

**Single-point failures:** O-ring failure (OR gate — no redundancy), Fitting overtorque (single cause path). **Corrective actions:** Add redundant seal, add torque verification step.

**E8.** → **Problem with rework station approach:** It treats the symptom (22% failures) without addressing root cause. The rework station adds cost (labor, space, cycle time) but the root cause continues producing failures. This is "burning money to clean up instead of stopping the fire." **True cost calculation:**

Direct cost = rework labor cost × 22% of units
Hidden costs: delayed throughput, inspector time, yield loss on units damaged during rework, risk of rework-induced defects, overtime costs, late deliveries
Rolled Throughput Yield with rework loop: RTY drops further if rework has its own failure rate

**Right approach:** Pareto the 22% failures by defect type, identify top 1–2 causes (usually 80% of failures), apply corrective action at the source. Even a partial fix that drops failures to 8% is far cheaper than a permanent rework station.

---

## Section F Answers

**F1.** → **(1) Stop the part — do not process further.** Red tag and quarantine. (2) Write the NCMR immediately — document all findings (indication length, location, weld seam ID, inspection method, radiograph image number). (3) **Contain** — check if any other parts on the same weld program, same welder, same shift have similar indications (run RT on adjacent parts). (4) Notify Manufacturing Engineering and Design Engineering — convene MRB. (5) **Do not let schedule pressure dictate the disposition.** The disposition (UAI, rework, repair, scrap) must be based on engineering analysis: Can the 12mm linear indication be characterized? Is it a crack or porosity? What is the load path through this joint? What is the safety factor? (6) If the indication is a crack → likely scrap or repair. Cracks are almost universally rejectable on flight hardware. (7) Root cause on the welding process — this cannot happen again. (8) Corrective action: 8D, get to true root cause.

**F2.** → **(1) Reject and quarantine all 50 brackets immediately** — do not allow into production. (2) Write a supplier nonconformance/supplier CAR. (3) Notify Procurement and Engineering. (4) **Do not attempt material testing alone to verify alloy** — if certs are wrong, you have a chain-of-custody break; even if independent testing says the material is Ti-6Al-4V, the formal documentation trail is broken and the parts may not be usable for flight hardware. (5) Disposition options: Return to Supplier (preferred — their error), or if extremely time-critical, work with engineering and quality management to determine if independent certified lab testing + full traceability documentation allows any path forward. (6) Counterfeit materials notification per AS9100 requirements.

**F3.** → Required engineering rationale for UAI: (1) Calculation showing actual thread engagement still achieves required load capacity with documented safety factor (typically ≥1.4 for aerospace). Reference: Shigley's or NASA thread design guidelines. (2) Analysis of worst-case loading on this fitting (pull-out load, vibration, pressure load). (3) Confirmation that the 15% reduction does not affect form/fit/function for adjacent components. (4) Review of similar hardware data — has this condition been seen before? (5) Documented by a licensed engineer with authority over this hardware, reviewed by a second engineer, and retained permanently in the part's history file. If the fitting is LOX-wetted and structural: extremely high bar — likely requires engineering director approval.

**F4.** → FAI per AS9102 is a formal **first article inspection** process that verifies the first production part (first article) conforms to ALL engineering drawing and specification requirements before series production begins. Required when: first production run of a new part, when a manufacturing process change is made that could affect part characteristics, when production is interrupted for >2 years, or when there is a design change. **Design change:** If the change affects a characteristic that was verified during original FAI, a **partial or full FAI** is required on the changed characteristic(s). The scope is determined by the nature of the change — a minor drawing tolerance change may require only a dimensional re-inspection of affected features; a material change may require complete re-inspection.

**F5.** →
```sql
SELECT
    p.part_number,
    COUNT(DISTINCT i.inspection_id)                              AS total_inspections,
    COUNT(DISTINCT n.ncmr_id)                                    AS total_ncmrs,
    ROUND(COUNT(DISTINCT n.ncmr_id) * 100.0 /
          NULLIF(COUNT(DISTINCT i.inspection_id), 0), 2)         AS ncmr_rate_pct
FROM parts p
JOIN inspections i
    ON p.part_id = i.part_id
    AND i.inspection_date >= DATEADD(day, -90, GETDATE())
LEFT JOIN ncmrs n
    ON p.part_id = n.part_id
    AND n.date_opened >= DATEADD(day, -90, GETDATE())
GROUP BY p.part_number
HAVING COUNT(DISTINCT n.ncmr_id) * 100.0 /
       NULLIF(COUNT(DISTINCT i.inspection_id), 0) > 5
ORDER BY ncmr_rate_pct DESC;
```

**F6.** → **Not a valid root cause.** "Operator did not follow the procedure" describes *what happened*, not *why it happened*. This stops at the symptom level and leads to ineffective corrective actions (retrain the operator, which rarely prevents recurrence). **Next question:** "Why didn't the operator follow the procedure?" Answers might be: procedure was unclear or not accessible at the workstation, procedure wasn't part of formal training, procedure was in conflict with verbal instruction from supervisor, the step took too long so operators skip it under schedule pressure, the procedure has never been enforced. Each of these leads to a systemic corrective action (rewrite procedure, add mandatory sign-off, supervisor coaching, poka-yoke to force compliance) rather than blaming an individual.

---

## Section G — Scoring Guide

These are evaluated on structure, specificity, and SpaceX cultural fit.

**Strong answer characteristics:**
- Uses "I" not "we" when describing your actions
- Specific: names the part, the process, the measurement, the improvement achieved
- Shows quantified results: "reduced defect rate from 8% to 1.5%", "saved 12 hours of rework per vehicle"
- For G3/G4: Shows you would escalate, document, and stand firm on quality — not look the other way under schedule pressure
- For G4 specifically: Shows you understand that "good enough to fly" requires engineering analysis and documentation, not a gut call

**Red flags:**
- "We as a team..." without describing your specific role
- Vague results: "the quality improved"
- For G3: "I would let it go since no parts failed yet"
- For G4: "If the schedule says ship it, I'd ship it"

---

## Your Score

**Total questions:** 50 (some multi-part)

**Minimum before interview:** 80% hit rate on key points

**Focus areas if you struggled:**
- Sections A/B: Review EMAT physics and TIG welding defect causes
- Section D: Practice true position calculations until they're automatic
- Section E: Work through Weibull and Cpk calculations by hand
- Section F/G: Practice answering out loud — timing and structure matter

Good luck. You've got this.
