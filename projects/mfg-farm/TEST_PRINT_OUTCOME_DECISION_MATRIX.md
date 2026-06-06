---
title: Test Print Outcome Decision Matrix
subtitle: Comprehensive contingency planning for ModRun cable clip launch routing
project: mfg-farm
created: 2026-06-06
status: production-ready
purpose: "Instant routing from test print outcome to correct contingency path without discovery overhead"
related: TEST_PRINT_FAILURE_INVESTIGATION_RUNBOOK.md, ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md, FAILURE_SCENARIO_DECISION_TREE.md
---

# Test Print Outcome Decision Matrix

**Document Purpose**: When ModRun cable clip test print outcome is known (Days 1-2 of execution), user needs immediate routing to correct next-steps sequence. This document provides comprehensive decision trees for all 4 possible outcomes (PASS, PASS-WITH-ADJUSTMENTS, FAIL, PARTIAL-FAIL), with objective go/no-go thresholds, immediate action sequences, investigation procedures, timeline options, and checklist routing to ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md branches.

**How to Use**: 
1. Perform test print inspection using TEST_PRINT_FAILURE_INVESTIGATION_RUNBOOK.md measurement procedures
2. Record outcome + measurements on the decision matrix below
3. Follow the routing path for your outcome (A, B, C, or D)
4. Execute immediate actions from the relevant branch
5. Track timeline checkpoint dates and decision gates

**Execution Timeline**: Test print results available Day 1 morning → routing decision Day 1 before noon → execution Day 1 afternoon

---

## Master Outcome Classification

```
TEST PRINT OUTCOME
│
├─ OUTCOME A: ✅ PASS
│  └─ Snap-arm thickness: 1.25–1.55mm (within spec)
│     No visual defects
│     All functional tests pass
│     → ROUTE: Launch path (no contingency)
│
├─ OUTCOME B: ⚠️ PASS-WITH-ADJUSTMENTS
│  └─ Snap-arm thickness: 1.10–1.25mm OR 1.55–1.70mm (near spec, tight/loose)
│     No visible cracks
│     Functional tests pass with slight tightness or looseness
│     → ROUTE: 1-day CAD adjustment + micro-print revalidation
│
├─ OUTCOME C: 🔴 FAIL
│  └─ Snap-arm breaks on flex test OR
│     Snap-arm thickness: <1.10mm OR >1.70mm (out of spec)
│     Visible cracks or stress marks
│     Post wobbles >2mm or feels brittle
│     → ROUTE: Root cause analysis → v2 redesign (A1) OR fallback pivot (A2)
│
└─ OUTCOME D: 🟡 PARTIAL-FAIL
   └─ Some features work, others fail
      Examples: Snap-arm functional but mating surface warped; OR
      Multiple issues (snap-arm + bore diameter both off-spec)
      → ROUTE: Prioritization matrix → launch passing features only (D1) OR
      full redesign for coordinated launch (D2)
```

---

## OUTCOME A: ✅ PASS

**Criteria Met**:
- Snap-arm thickness: 1.25–1.55mm (design spec 1.4mm ±0.15mm) ✓
- Visual inspection: No cracks, no stress marks, no discoloration ✓
- Dimensional check: All critical dimensions (bore, mating surface, post diameter) within tolerance ✓
- Functional tests: Snap-arm flexes smoothly (5-10 cycles), clip holds cable under load (500g equivalent), post stable with no wobble >0.5mm ✓
- Material quality: No brittleness, no layer separation, smooth surface finish ✓

**Decision**: ✅ **Proceed directly to Etsy launch (OUTCOME A1 preferred)**

---

### OUTCOME A1: PASS → DIRECT LAUNCH (Recommended Path)

**Decision Criteria**:
- You have high confidence in design and want maximum speed to market
- Market timing is critical (June window closing)
- No additional validation needed; print passed all checks

**Immediate Actions (First 2 Hours)**:

1. **Lock production settings** (10 min):
   - Record slicer settings on printed card and post at printer:
     - Layer height: 0.20mm
     - Nozzle temp: 220°C (PLA+)
     - Print speed: 200mm/s outer, 300mm/s infill
     - Infill: 25% gyroid
     - First layer: 0.25mm height with brim if needed
   - Document filament brand and color in project log
   - Note print queue startup time for production batch

2. **Generate production batch STLs** (5 min):
   - Export final STLs to `/projects/mfg-farm/stl/` with tolerance locked:
     ```bash
     uv run python cadquery/modrun_clip_b123d.py --output-dir stl/
     uv run python cadquery/modrun_rail_b123d.py --output-dir stl/
     ```
   - Git commit: `git commit -m "docs(mfg-farm): Lock production settings, tolerance PASS"`

3. **Photograph test print** (15 min):
   - Use photo checklist from ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md Part 1b:
     - Hero shot: clip on desk/rail setup
     - Close-up: snap-arm detail and tolerance
     - Color variants: show natural PLA+ material
     - Lifestyle context: cable management on workspace
   - Store photos in `/projects/mfg-farm/photos/test-print-approved/`
   - Backup to cloud or external drive (safety redundancy)

4. **Log decision commitment** (5 min):
   - File in project: `TEST_PRINT_DECISION_LOG_A1_[DATE].txt`
   - Content:
     ```
     OUTCOME: PASS
     Snap-arm measured: [X]mm
     All tolerances: PASS
     Confidence: 95%+
     Route: A1 (Direct Launch)
     Decision time: [timestamp]
     Launch target: May 30 (standard 4-day prep)
     Next checkpoint: May 25 (start prep checklist)
     ```

**Investigation/Analysis** (Post-decision, lower priority):
- None required for immediate launch; design is locked
- Optional: photograph cross-sections or create documentation for future design iterations

**Timeline Options**:

| Timeline | Duration | Path | Launch Date |
|---|---|---|---|
| **FAST** (Accelerated) | 3 days | Skip supplier negotiation, use existing inventory, minimal photo edits | May 28-29 |
| **STANDARD** (Recommended) | 4-5 days | Full execution per ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md Part 1-2 | **May 30** |
| **CONSERVATIVE** | 8-10 days | Extended supplier negotiation, A/B test photos, additional QA batches | June 2-5 |

**Go/No-Go Decision Point**:
- Go: Measurements within spec + no functional failures + visual inspection clean
- No-go: Any measurement outside tolerance range OR functional failure observed
  - If no-go: Escalate to OUTCOME B or C

**Checklist Routing - Execute This Sequence**:

From ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md:
1. ✅ **Part 1a** (Phase 1a): Etsy Shop Foundation — 2-3 hours
   - Create shop, complete policies, setup shipping profile
   - **Starts**: Day 1 afternoon (immediately after test print approval)
   - **Deadline**: Day 3 evening (May 25-26)

2. ✅ **Part 1b** (Phase 1b): Product Listing Preparation — 3-4 hours
   - Photography, description writing, SEO tags
   - **Starts**: Day 1 afternoon (parallel with shop setup)
   - **Deadline**: Day 4 evening (May 25-26)

3. ✅ **Part 1c** (Phase 1c): Shop Policies & Legal — 1 hour
   - Terms of service, FAQ template, contact policy
   - **Starts**: Day 2 afternoon
   - **Deadline**: Day 3 evening

4. ✅ **Part 2**: Launch-Week Execution (May 30 → June 2)
   - Deploy listings, monitor conversions, fulfill orders
   - **Launch Day**: May 30 (4 days after test print approval)

5. ✅ **Part 3**: Post-Launch Scaling (June 3+)
   - Gather reviews, optimize listings, expand product line

**Execution Checklist (Outcome A1)**:

```
Day 1 (Test Print Day):
  [ ] Inspection complete, outcome PASS recorded
  [ ] Production settings card printed and posted at printer
  [ ] STLs generated and committed to git
  [ ] Test print photos taken and archived
  [ ] Decision log filed with launch commitment
  [ ] Part 1a prep work started: shop platform choice made

Day 2-3:
  [ ] Part 1a complete: Etsy shop foundation built
  [ ] Part 1b complete: Product photos edited, listing draft created
  [ ] Part 1c complete: Policies documented

Day 4:
  [ ] Final pre-flight check (Part 1b checklist item 4)
  [ ] Confirm payment methods active
  [ ] Verify shipping template

Day 5 (May 25):
  [ ] All Part 1 items complete
  [ ] Ready to move to Part 2 execution

Day 6 (May 26-29):
  [ ] Launch prep window open
  [ ] Supplier negotiation (optional, lower priority)
  [ ] Social media posts scheduled

Day 7 (May 30):
  [ ] 🚀 LAUNCH: Listings published to Etsy
  [ ] Part 2 execution begins: monitor orders, fulfill daily
```

---

### OUTCOME A2: PASS → OPTIONAL SECOND VALIDATION TEST (Conservative Path)

**Decision Criteria**:
- You want maximum confidence before full production batch
- You have extra time (market window extends to June 15+)
- You want to build a more substantial photo portfolio before launch

**Reason to Choose A2**: When test print PASS is borderline-clean (no visible defects but snap-arm at edge of tolerance, e.g., 1.25mm or 1.55mm exactly), running a second independent validation test builds confidence in production batch consistency.

**Process (1-2 Days Additional)**:

1. **Run second independent test print** (Same day afternoon):
   - Print a new clip from the same STL with identical slicer settings
   - Goal: Verify tolerance consistency across print runs
   - Expected: Second unit should measure within 0.1mm of first unit

2. **Measure second unit** (Next morning):
   - Snap-arm dimension: should match first unit ±0.1mm
   - All critical dimensions: bore, mating surface, post diameter
   - If all pass: confidence in tolerance is 95%+ → proceed to production
   - If any fails: escalate to OUTCOME B (tolerance adjustment needed)

3. **Photograph both units** (Same afternoon):
   - Side-by-side comparison shows consistency
   - Strengthens product photography with "quality assurance" narrative

**Timeline Impact**: +1 day (May 30 launch → May 31 launch)

**When to Skip A2 and Go Direct to A1**:
- Market timing is critical and you have orders waiting
- First print measurement was clearly in center of tolerance range (1.3-1.5mm, not 1.25-1.55mm edges)
- You have previous successful prints of this design from earlier iterations

---

## OUTCOME B: ⚠️ PASS-WITH-ADJUSTMENTS

**Criteria Met (Partial)**:
- Snap-arm is functional but off-spec:
  - Too tight: 1.10–1.25mm (target 1.4mm), snap-arm requires more force to flex
  - Too loose: 1.55–1.70mm (target 1.4mm), snap-arm is very flexible, cable might slip
- No visible cracks or stress marks ✓
- Functional tests pass but with noted tightness/looseness
- Other features (mating surface, bore, post) are within spec ✓

**Decision**: ⚠️ **Proceed with quick CAD tolerance adjustment + micro-print revalidation (OUTCOME B1 recommended)**

---

### OUTCOME B1: QUICK ADJUSTMENT + 1-DAY ITERATION (Recommended)

**Decision Criteria**:
- Root cause is clear: tolerance is slightly off, but not catastrophically
- Fixing is fast: adjust snap-arm thickness ±0.05–0.1mm in CAD
- Confidence is high: v2 has 85%+ chance of passing
- Timeline is acceptable: +1 day slip (May 30 → May 31 launch)

**Immediate Actions (First 2 Hours)**:

1. **Diagnose root cause** (10 min):
   - Snap-arm measured [X]mm. Is it too tight (< 1.25mm) or too loose (> 1.55mm)?
   - **Too tight scenario**: Under-extrusion OR snap-arm CAD thickness is too large
   - **Too loose scenario**: Over-extrusion OR snap-arm CAD thickness is too small
   - Record actual measurement in project log

2. **Decide on fix method** (5 min):
   - **Option 1: CAD adjustment** (recommended if tolerance is the issue):
     - Edit parametric constant: `SNAP_ARM_THICKNESS = 1.4mm` → adjust to `1.35mm` (if too tight) or `1.45mm` (if too loose)
     - Regenerate STL
     - Time: 5-10 min
   - **Option 2: Slicer adjustment** (faster if print settings are the issue):
     - If too tight: Reduce flow -2% in nozzle profile → retest
     - If too loose: Increase flow +2%
     - Time: 2 min

3. **Choose fix method and commit** (5 min):
   - Estimated measurement error: (actual - target) = tolerance delta
   - If delta > 0.15mm: Use CAD adjustment (more reliable, documented)
   - If delta < 0.15mm: Use slicer adjustment (faster)
   - Document choice in decision log:
     ```
     OUTCOME: PASS-WITH-ADJUSTMENTS
     Original snap-arm: [X]mm
     Target: 1.4mm
     Delta: [+/- amount]mm
     Fix method: [CAD adjustment / Slicer adjustment]
     Expected v2 snap-arm: [target ± 0.05mm]
     Confidence: 85%
     ```

**Investigation/Analysis** (While waiting for v2 to print):

- **CAD model review** (if doing CAD adjustment):
  - Open `cadquery/modrun_clip_b123d.py`
  - Locate SNAP_ARM_THICKNESS constant
  - Calculate required adjustment: if measured 1.2mm and target 1.4mm, need +0.2mm → adjust constant to 1.6mm (CAD measurement will grow 0.2mm in print)
  - Note: PLA+ typically shrinks ~0.5%, so CAD offset may be needed

- **Slicer settings review** (if doing slicer adjustment):
  - Check filament diameter on spool: should be 1.75 ± 0.03mm
  - Verify nozzle is clean (no residue from previous prints)
  - Check bed temperature: PLA+ at 60-65°C optimal
  - Nozzle temperature: 215-225°C for PLA+ (current 220°C is good)

**Timeline Options**:

| Timeline | Duration | Path | Launch Date |
|---|---|---|---|
| **FAST** (Immediate iteration) | 1 day | v2 print Day 1 evening + retest Day 2 morning → approve & launch Day 2 evening | May 31 |
| **STANDARD** (Safe retest) | 1.5 days | v2 print Day 1 afternoon + retest Day 2 morning + decision Day 2 afternoon | May 31-June 1 |
| **CONSERVATIVE** (Triple-check) | 2 days | v2 print Day 1 evening, measure Day 2 morning, run Day 3 production test, approve Day 3 afternoon | June 1-2 |

**Go/No-Go Decision Point**:

**V2 Retest (Day 2 Morning)**:
- [ ] v2 snap-arm measured within 1.30–1.50mm range? (±0.1mm of target)
  - **YES** → ✅ **GO: Approve v2 design, lock tolerance, proceed to launch May 31**
  - **NO** → 🔴 **NO-GO: Escalate to OUTCOME C (redesign or fallback pivot)**

**Checklist Routing - Execute This Sequence**:

From ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md (adjusted timeline):
1. ⚠️ **Part 1a** (Phase 1a): Etsy Shop Foundation — 2-3 hours
   - **Starts**: Day 2 afternoon (after v2 retest passes)
   - **Deadline**: Day 4 evening (May 27)

2. ⚠️ **Part 1b** (Phase 1b): Product Listing Preparation — 3-4 hours
   - **Starts**: Day 2 afternoon (parallel with Part 1a)
   - **Deadline**: Day 4 evening

3. ⚠️ **Part 1c** (Phase 1c): Shop Policies & Legal — 1 hour
   - **Starts**: Day 3 afternoon
   - **Deadline**: Day 4 evening

4. ⚠️ **Part 2**: Launch-Week Execution (May 31 → June 3)
   - Deploy listings 1 day earlier than standard
   - **Launch Day**: May 31 (5 days after original test print)

**Execution Checklist (Outcome B1)**:

```
Day 1 (Original Test Print Day):
  [ ] Outcome recorded: PASS-WITH-ADJUSTMENTS
  [ ] Snap-arm measured: [X]mm, delta from target: [+/- Y]mm
  [ ] Root cause diagnosed: [CAD / Slicer issue]
  [ ] Fix method selected: [CAD adjustment / Slicer tuning]
  [ ] Decision documented in log

Day 1 Evening:
  [ ] CAD edit OR slicer adjustment completed
  [ ] v2 STL generated (if CAD edit)
  [ ] v2 print initiated (target 90 min print + 60 min cool)

Day 2 Morning:
  [ ] v2 unit cooled and measured
  [ ] Snap-arm dimension recorded: [X]mm
  [ ] Decision: PASS (→ launch May 31) OR FAIL (→ escalate to C)

Day 2 Afternoon (if v2 PASS):
  [ ] Production settings card updated and posted
  [ ] v2 STL committed to git with tolerance lock
  [ ] Test print photos taken (if not done Day 1)
  [ ] Part 1a work starts: shop foundation

Day 3-4:
  [ ] Part 1a, 1b, 1c all complete (compressed timeline)
  [ ] Etsy shop ready to publish

Day 5 (May 31):
  [ ] 🚀 LAUNCH (1 day early): Listings published May 31 instead of May 30
  [ ] Part 2 execution begins
```

---

### OUTCOME B2: ACCEPT TOLERANCE + QC HAND-ADJUSTMENT (Alternative Path)

**Decision Criteria**:
- You want to launch immediately without iteration
- Tolerance is borderline but functional (snap-arm flexes, clip holds cable)
- You're willing to add post-production QC step to manually adjust tight/loose clips

**Process**:
1. Accept current snap-arm design as-is (1.1–1.7mm range is acceptable)
2. Add QC step in fulfillment workflow:
   - **For tight clips** (< 1.25mm): Hand-sand interior mating surface with 220-grit sandpaper (1-2 min per unit)
   - **For loose clips** (> 1.55mm): Accept as cosmetic variation; still functionally sound
3. Document in listing: "Hand-finished for optimal snap fit"

**Trade-off**: Launches immediately (May 30) but requires labor per unit; margins drop ~$0.50/unit (1-2 min @ $15/hr). Only choose if market timing is critical.

**Not Recommended Unless**: Market window closes in 2-3 days OR iteration would create >5 day delay.

---

### OUTCOME B3: DEFER LAUNCH FOR FULL REDESIGN (Conservative Path)

**Decision Criteria**:
- You want perfect design before production
- Market timing is flexible (can launch June 6+)
- You want to investigate whether tolerance issue is design-level or print-setting level

**Process** (4-5 Days):
1. Run diagnostic sequence: vary print settings across 5 test prints
   - Test 1: Current settings
   - Test 2: Layer height 0.15mm (instead of 0.20mm) → finer resolution
   - Test 3: Nozzle temp 215°C (vs. 220°C) → tighter extrusion
   - Test 4: Flow -3% in nozzle profile
   - Test 5: Material swap: standard PLA instead of PLA+

2. Measure all 5 units, determine which setting eliminates tolerance variance

3. Lock optimized setting, regenerate STL, retest with optimization

4. Approve design when 3 independent prints all land within ±0.05mm of target

**Timeline**: 5-7 days (launch June 2-5 instead of May 31)

**When to Choose B3**: If you're not confident in B1 fix and want data-driven optimization before production.

---

## OUTCOME C: 🔴 FAIL

**Criteria Met (Failure Confirmed)**:
- Snap-arm breaks on flex test OR
- Snap-arm thickness < 1.10mm OR > 1.70mm (far outside spec) OR
- Visible cracks or stress marks on snap-arm or mating surface OR
- Post wobbles > 2mm under cable load OR
- Material feels brittle, not flexible

**Decision**: 🔴 **Halt standard launch sequence → Root cause analysis → Choose A1 (v2 redesign) or A2 (fallback pivot)**

---

### OUTCOME C: Failure Root Cause Analysis (Day 1 Afternoon)

**Immediate Actions (First 2 Hours)**:

1. **Document failure details** (15 min):
   - Photograph failure:
     - Snap-arm break location (at base, mid-arm, or tip?)
     - Cracks: orientation (vertical, horizontal, diagonal?)
     - Stress marks: white stress lines visible?
     - Post wobble: measure with hand (1-2mm? 5mm+?)
   - Measurements:
     - Snap-arm thickness: [X]mm vs. spec 1.4mm
     - Bore diameter: [X]mm vs. spec 3.0mm ±0.2mm
     - Mating surface: flat or warped?
   - Material inspection:
     - Is filament color consistent (no dark spots indicating heat damage)?
     - Does material crumble or flex (brittleness = over-heating)?
     - Are there layer separation lines visible?
   - File in project: `FAILURE_ANALYSIS_[DATE].txt`

2. **Diagnose root cause** (15 min):
   - **Hypothesis 1 — Under-extrusion**:
     - Symptoms: Snap-arm is thin (< 1.25mm), breaks cleanly on flex
     - Confidence: 75%
     - Likely causes: Nozzle clogged, filament jammed, flow rate too low
     - Fix: Clear nozzle, verify filament path, increase flow +3%
   - **Hypothesis 2 — Over-extrusion (opposite)**:
     - Symptoms: Snap-arm is thick (> 1.70mm) but breaks under stress (brittleness)
     - Confidence: 60%
     - Likely causes: Nozzle temp too high, filament diameter too large
     - Fix: Reduce nozzle temp 5°C, verify filament diameter on spool
   - **Hypothesis 3 — Slicer layer height too coarse**:
     - Symptoms: Snap-arm is correct thickness but has horizontal stress lines, breaks at layer boundary
     - Confidence: 70%
     - Likely causes: 0.20mm layer height is too coarse for 1.4mm feature
     - Fix: Reduce layer height to 0.15mm, retest
   - **Hypothesis 4 — CAD geometry issue**:
     - Symptoms: Snap-arm measures correct but still breaks (stress concentration at base?)
     - Confidence: 50%
     - Likely causes: Snap-arm radius too sharp, base is too thin, material flow at junction is weak
     - Fix: Add 0.3mm radius fillet at snap-arm base, increase arm thickness, retest
   - **Hypothesis 5 — Material defect**:
     - Symptoms: Material is discolored, crumbles easily, no flexibility
     - Confidence: 40%
     - Likely causes: Filament is wet (absorbed humidity), nozzle temp burned filament
     - Fix: Dry filament 4-6 hours at 60°C, reduce nozzle temp to 215°C
   - **Hypothesis 6 — Print settings misalignment**:
     - Symptoms: STL file export error (1.0x scale vs. 1.5x), CAD model has wrong units (inches vs. mm)
     - Confidence: 30% (easy to check)
     - Fix: Verify STL scale in slicer (should show dimensions matching CAD), re-export if wrong

3. **Assess confidence in fix** (5 min):
   - Which hypothesis is most likely? (pick top 2)
   - How confident are you in the fix? (estimate %)
   - Can you rule out other hypotheses by inspection?
   - Decision gate:
     - ≥70% confident in fix → Route to **A1 (v2 Redesign)**
     - <70% confident → Route to **A2 (Fallback Pivot)** OR escalate to expert

**Investigation Procedures** (Detailed):

| Hypothesis | Evidence | Test | Time |
|---|---|---|---|
| **Under-extrusion** | Snap-arm too thin, breaks cleanly | (1) Look for thin walls across print; (2) Check nozzle for blockage; (3) Verify filament path unobstructed; (4) Measure extrusion width (should be 0.4mm for 0.4 nozzle) | 15 min |
| **Over-extrusion (brittleness)** | Material is stiff, cracks under stress | (1) Smell filament (burnt smell = over-heat); (2) Check nozzle temp reading on printer display; (3) Try bending a small printed scrap piece — if it snaps vs. flexes, material is brittle | 10 min |
| **Slicer layer height too coarse** | Horizontal stress lines visible at layer boundaries | (1) Examine snap-arm under magnification (10x magnifier or macro camera); (2) Look for white stress lines or layer separation lines; (3) Re-examine slicer settings (layer height should show 0.20mm) | 10 min |
| **CAD geometry (stress concentration)** | Snap-arm thickness is correct but still breaks at base junction | (1) Examine failure point: is it at the snap-arm root (where it connects to main body) or mid-arm?; (2) Compare break location to CAD model (is there a sharp corner at failure point?); (3) Design review: add 0.3–0.5mm fillet at snap-arm base junction | 20 min |
| **Material defect (wet filament)** | Material crumbles, no flexibility, color mottled | (1) Weigh filament spool before and after print (should lose <0.3% to evaporation); (2) Check spool storage (was it sealed? exposed to humidity?); (3) Feel print — does it crumble under thumb pressure or remain flexible? | 10 min |
| **Print settings misalignment (scale/units)** | Snap-arm looks wrong size, significantly too big or too small | (1) Measure snap-arm in slicer preview before printing (should match CAD dimensions); (2) Check STL export settings (verify export units are mm, not inches or cm); (3) Re-export STL and check slicer again | 5 min |

---

### OUTCOME C1: V2 REDESIGN PATH (If Confidence ≥70%)

**When to Choose**: Root cause is clear, fix is straightforward, and you're confident it will work.

**Examples of High-Confidence Fixes**:
- Under-extrusion (symptom: snap-arm 0.9mm vs. spec 1.4mm) → increase flow +3% → 85% confidence retest will pass
- Slicer setting (symptom: stress lines at layer boundaries) → reduce layer height 0.20 → 0.15mm → 80% confidence retest will pass
- Simple CAD issue (symptom: sharp corner at snap-arm base) → add 0.3mm fillet → 75% confidence retest will pass

**Process (Days 1-4)**:

**Day 1 Afternoon (Fix Implementation)** — 30 min:
1. Implement fix in CAD or slicer:
   - **CAD fix**: Edit `cadquery/modrun_clip_b123d.py`
     - Example: Add radius fillet at snap-arm junction
     - Example: Increase snap-arm thickness from 1.4mm to 1.5mm
     - Regenerate STL: `uv run python cadquery/modrun_clip_b123d.py --output-dir stl/`
   - **Slicer fix**: Adjust Bambu Studio profile
     - Example: Layer height 0.20mm → 0.15mm
     - Example: Flow rate +3%
     - Export new G-code

2. Queue v2 print (print time: 90 min + 60 min cool)

3. Document fix in decision log:
   ```
   Root cause: [hypothesis]
   Confidence: [%]
   Fix implemented: [description]
   v2 print queued: [time]
   Expected measurement: [X]mm ±0.05mm
   Retest scheduled: [day/time]
   Escalation trigger: If v2 still fails, escalate to A2 immediately
   ```

**Day 2 Morning (Retest)** — 30 min:
1. Measure v2 snap-arm: should be 1.35–1.50mm (within ±0.1mm of target)
2. Visual inspection: no cracks, no stress marks
3. Functional test: flex 10 times, should remain strong
4. Decision gate:
   - ✅ **v2 PASSES**: Lock design, commit to git, move to production batch (Days 3-4)
   - 🔴 **v2 FAILS**: Escalate to **A2 (Fallback Pivot)** immediately (don't iterate again)

**Day 3-4 (Production Batch)** — if v2 passes:
1. Slice production batch (4-5 units per plate for 15-20 unit initial batch)
2. Print Day 3-4 (parallel printing, ~400 min total)
3. QA all units (visual + functional check)
4. Proceed to Part 1 (Etsy prep) starting Day 4-5

**Timeline to Launch** — if v2 passes:
- **May 30-31 launch** (standard timeline maintained if v2 passes by Day 2 afternoon)
- **June 2-5 launch** (if v2 retest takes longer or reveals new issue)

---

### OUTCOME C2: FALLBACK PIVOT PATH (If Confidence <70%)

**When to Choose**: Root cause is unclear, fix is risky, or you've already iterated once unsuccessfully.

**Examples of Low-Confidence Scenarios**:
- Multiple competing hypotheses (under-extrusion? geometry? material?) and can't rule out → <50% confidence in any single fix
- Snap-arm is correct thickness (1.4mm) but still breaks (indicates design-level issue, not print-setting) → 40% confidence in quick fix
- You've already done one iteration (Outcome B → v2 retest failed) and are facing second iteration → <50% confidence you'll solve on next try
- Expert feedback is mixed or inconclusive

**Process (Days 1-5)** — Parallel to exploring v2 for safety:

**Day 1 Afternoon (Pivot Design Selection)** — 30 min:
1. Decide on fallback product: Pick **one** of:
   - **Magnetic clips** (RECOMMENDED): Uses neodymium magnets for adhesion instead of snap-arm. Pros: differentiated, fast to design (1-2 days CAD), cost ~$2-3 per unit with magnets. Cons: slightly heavier, magnet sourcing required.
   - **Adhesive-only clips** (FAST): Remove snap-arm entirely, use 3M VHB tape for mounting. Pros: simplest design (design work: 30 min), semi-permanent. Cons: less versatile than snap-fit, customer perception weaker.
   - **Screw-mount clips** (PROVEN): Use #6-32 wood screws for rail attachment instead of snap-arm. Pros: proven reliable, easy to design (2 hours), no tool needed (hand-screw). Cons: most common solution, least differentiated.

2. Confidence assessment on fallback:
   - Magnetic clips: 90% confidence design will work (magnets are simple physics)
   - Adhesive clips: 95% confidence (tape is proven)
   - Screw-mount: 95% confidence (industry standard)

3. Document fallback selection in log:
   ```
   Snap-arm failure diagnosis: Confidence too low (<70%)
   Root cause: [list competing hypotheses]
   v2 attempt: Yes / No [if no, jumping straight to fallback]
   Fallback product selected: [Magnetic / Adhesive / Screw-mount]
   Fallback confidence: [%]
   Fallback CAD work: [estimated days]
   Fallback timeline to launch: June 2-5
   ```

**Day 2-3 (Fallback CAD Design)** — 3-4 hours:
1. Create fallback product parametric design:
   - **Magnetic clips**: Add magnet pockets to rail and clip, size for standard neodymium N52 5×5mm magnets (cost $0.20 each)
   - **Adhesive clips**: Remove snap-arm feature entirely, create flat mounting surface for 3M VHB tape, add landing pads on rail
   - **Screw-mount**: Add #6-32 threaded inserts to rail (if metal) or pilot holes (if printed plastic), design screw-socket on clip
2. Export v1 CAD test model
3. Generate test STL: `uv run python cadquery/modrun_clip_fallback_[type].py --output-dir stl/`

**Day 3 Afternoon (Fallback Test Print)** — 90 min print + 60 min cool:
1. Print fallback v1 test unit
2. Functional test:
   - **Magnetic**: Do magnets hold clip to rail with reasonable force? Can you remove clip with one hand?
   - **Adhesive**: Does tape stick permanently? Can you peel and re-stick multiple times without degradation?
   - **Screw-mount**: Do screws tighten smoothly? Does clip hold cable under load?

**Day 4 Morning (Fallback Decision Gate)**:
- ✅ **Fallback passes**: Lock design, proceed to production batch (Days 4-5)
- 🔴 **Fallback fails**: Escalate to expert support (this is rare; fallback designs are chosen for simplicity)

**Day 5-6 (Production Batch)** — if fallback passes:
1. Print initial batch (10-15 units)
2. Verify QA across batch
3. Proceed to Part 1 (Etsy prep)

**Timeline to Launch** — if fallback passes:
- **June 2-5 launch** (7-10 days after original test print failure)

---

### OUTCOME C3: EXPERT ESCALATION PATH (If Unsure)

**When to Choose**: You have multiple competing hypotheses and low confidence in any fix.

**Process** (Same day, 4-6 hours):
1. Post to 3D printing community with failure photos + measurements:
   - r/3Dprinting (tag with [HELP])
   - Bambu Lab Discord (@support tag)
   - Local maker community Slack

2. Include in post:
   ```
   HELP: Test print failed. Snap-arm broke on flex test.
   
   Design specs:
   - Snap-arm target: 1.4mm thickness
   - Material: PLA+ (eSUN)
   - Nozzle: 220°C
   - Layer height: 0.20mm
   - Print speed: 200mm/s
   - Infill: 25% gyroid
   
   Failure details:
   - Snap-arm measured: [X]mm
   - Break location: [base/mid-arm/tip]
   - Visible stress marks? Yes/No
   - Material brittleness? Yes/No
   
   Possible causes I'm considering:
   1. Under-extrusion (snap-arm too thin?)
   2. Stress concentration at base (geometry issue?)
   3. Material was damaged (over-heating?)
   
   Question: What does this failure pattern suggest? 
   Recommended next steps?
   ```

3. Wait for expert response (expect 1-2 hour response time on Discord)
4. Implement expert recommendation as Day 2-3 action
5. Retest Day 3-4

**Timeline Impact**: +1-2 days (expert response + implementation), May 30-31 launch becomes June 2-5

---

## OUTCOME D: 🟡 PARTIAL-FAIL

**Criteria Met (Selective Failure)**:
- Some features work, others fail
- Examples:
  - 0.5" clip size: snap-arm works, passes all tests ✓
  - 0.75" clip size: snap-arm too tight, won't flex ✗
  - 1.0" clip size: snap-arm loose, works but marginal ◐
- OR:
  - Snap-arm functional ✓ but mating surface is warped (cosmetic) ✗
  - Post diameter OK ✓ but bore diameter is 0.3mm too large ✗

**Decision**: 🟡 **Launch passing features immediately OR hold all features for coordinated redesign (choose D1 or D2)**

---

### OUTCOME D1: LAUNCH PASSING FEATURES ONLY (Recommended)

**Decision Criteria**:
- One or more SKUs pass all tests and are revenue-positive
- Failing SKUs are secondary (aesthetic, optional variant)
- Parallel iteration on failing SKUs won't slow down launch momentum
- Market timing favors immediate launch of passing products

**Example**: 0.5" clip and 1.0" clip pass; 0.75" clip has snap-arm too tight → Launch 0.5" & 1.0" on May 30, iterate 0.75" during May 30-June 2 window, add 0.75" to catalog June 2-5

**Immediate Actions (First 2 Hours)**:

1. **Document passing vs. failing SKUs** (15 min):
   ```
   PARTIAL-FAIL INVENTORY:
   
   PASSING (✓ Ready for Launch):
   - 0.5" clip: snap-arm 1.40mm ✓, bore 3.0mm ✓, post stable ✓
     → Proceed to production
   - 1.0" clip: snap-arm 1.42mm ✓, bore 3.0mm ✓, post stable ✓
     → Proceed to production
   
   FAILING (✗ Requires Iteration):
   - 0.75" clip: snap-arm 1.25mm (too tight), bore OK, post OK
     → Root cause: size-dependent tolerance scaling
     → Requires v2 redesign of parametric scaling
   ```

2. **Calculate revenue impact of passing SKUs** (10 min):
   - Passing SKU monthly revenue estimate: ≥$100-150 (for 2-3 SKUs)
   - Is this sufficient to justify launch without failing SKU?
   - **Yes** (revenue >$100/month) → Proceed with D1 (launch passing only)
   - **No** (revenue <$50/month) → Consider D2 (hold for coordinated launch)

3. **Make D1 vs. D2 decision** (5 min):
   - **Choose D1 if**: Passing SKU revenue ≥$100/month OR market timing is critical OR failing SKU is niche variant
   - **Choose D2 if**: Failing SKU is core product OR all SKUs must launch together for brand coherence

---

### OUTCOME D1: EXECUTION PLAN (Launch Passing, Iterate Failing)

**Timeline**: May 30 launch (passing) + June 2-5 launch (failing after rework)

**Part 1a-c (Etsy Prep for Passing SKUs Only)** — Days 1-3:
- Build Etsy shop, upload photos and listings for passing SKUs only
- **Note in listing**: "Additional sizes coming soon" to signal planned expansion
- Do NOT publish photos/listings for failing SKUs yet

**Part 2 (Launch Week, May 30-June 2)** — Passing SKUs only:
- **May 30**: Publish passing SKU listings, begin taking orders
- **May 30-June 2**: Fulfill orders for passing SKUs, gather initial feedback

**Parallel: Iterate Failing SKU (Days 1-5)**:
- **Day 1**: Diagnose root cause of 0.75" tight snap-arm
  - Likely cause: parametric design scales snap-arm thickness incorrectly for medium sizes
  - Hypothesis: `SNAP_ARM_THICKNESS = 1.4 * SIZE_FACTOR` where size_factor is too aggressive for 0.75"
  - Fix: Adjust scaling multiplier for 0.75" size specifically

- **Days 2-3**: CAD redesign
  - Edit parametric model to isolate 0.75" snap-arm thickness tolerance
  - Test fix on v2 test print: `uv run python cadquery/modrun_clip_b123d.py --size 0.75 --output-dir stl/`
  - Measure v2: target 1.35–1.50mm
  - If passes: lock design, regenerate production STL

- **Days 4-5**: Production batch for failing SKU
  - Print 10-15 units of reworked 0.75" clip
  - QA all units

- **June 2-5**: Add reworked SKU to catalog
  - Update Etsy shop: add photos and listing for 0.75" variant
  - Cross-sell messaging: "Now available in all three sizes"
  - Generate photos showing all 3 sizes together

**Checklist Routing (D1)**:

From ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md (MODIFIED for partial launch):
1. ✅ **Part 1a/b/c**: Build Etsy shop and listings for passing SKUs only (Days 1-3)
2. ✅ **Part 2**: Launch passing SKUs (May 30)
3. ✅ **Part 2 + Parallel iteration**: Failing SKU redesign (Days 1-5 concurrent with Part 2)
4. ✅ **Part 2 continuation**: Add failing SKU to catalog (June 2-5)

**Expected Outcome**:
- **Revenue May 30 - June 2**: ~$150-300 (2 passing SKUs, 5-10 orders)
- **Revenue June 2-5**: +$50-100 (reworked failing SKU added)
- **Total June revenue**: $400-500+ (all 3 SKUs live)
- **Advantage**: Market momentum + early reviews on proven SKUs, while iteration continues on failing SKU

---

### OUTCOME D2: HOLD ALL SKUS FOR COORDINATED LAUNCH (Conservative Path)

**Decision Criteria**:
- Failing SKU is core to product positioning (e.g., 0.75" is most popular size)
- All SKUs must launch together for brand coherence
- Timeline is flexible enough for 3-5 day delay (June 1-2 launch instead of May 30)
- You want higher confidence in full portfolio before going public

**Immediate Actions (First 2 Hours)**:

1. **Prioritize redesign**: Which failing SKU(s) are blocking launch?
   - 0.75" too-tight snap: Affects 30% of potential customers (medium-sized clips)
   - 1.0" loose snap: Affects 20% of customers, but functional (acceptable MVP)
   - Mating surface warped: Affects aesthetics only, not functionality

2. **Make time-priority decision**:
   - **Fast path** (2-3 days): Fix only the highest-priority failure (0.75" snap-arm)
   - **Full path** (4-5 days): Fix all failures, including cosmetic ones

3. **Document D2 decision**:
   ```
   Partial failure: [which SKUs/features]
   Core product SKU(s): [which are essential for launch]
   Redesign scope: [which to fix]
   Timeline: June 1-2 launch (hold all SKUs)
   Redesign strategy: Fast (fix core) or Full (fix all)
   ```

**Redesign Timeline (D2, Fast Path — 2-3 Days)**:

**Day 1 Afternoon** (1 hour):
- Diagnose failing SKU root cause
- Implement v2 CAD fix (e.g., adjust parametric tolerance for 0.75" size)
- Queue v2 test print

**Day 2 Morning** (30 min):
- Measure v2: if passes, approve design
- If fails: escalate to expert or fallback pivot

**Day 2-3** (3-4 hours):
- Print production batch for all SKUs (including reworked sizes)
- QA all units

**Days 3-4**:
- Part 1a-c: Full Etsy prep (shop, listings, photos for all 3 SKUs)

**Day 5** (June 1-2):
- 🚀 **LAUNCH**: Publish all 3 SKUs simultaneously
- Full portfolio positioning: "The complete cable clip system — 3 sizes, all optimized"

**Checklist Routing (D2)**:

From ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md (MODIFIED for delayed coordinated launch):
1. ⚠️ **Part 1a/b/c**: Delay to Day 2-4 (after all SKUs are redesigned)
2. ⚠️ **Part 2**: Launch all SKUs together (June 1-2 instead of May 30)

**Expected Outcome**:
- **Launch delay**: +1-3 days (May 30 → June 1-2)
- **Market timing**: Still within strong market window (June 1-15)
- **Revenue advantage**: Full 3-size portfolio from Day 1 (stronger positioning, more algorithm signal on Etsy)
- **Risk**: Iteration could fail, pushing launch to June 5+ (low risk if fix is straightforward)

---

## Comprehensive Routing Table (All Outcomes)

**Print this table and record your outcome + measurements:**

| Outcome | Snap-Arm Measured | Visual Inspection | Functional Tests | Route Decision | Timeline | Launch Date |
|---|---|---|---|---|---|---|
| **A: PASS** | 1.25–1.55mm | No defects, clean | All pass (flex, grip, stable) | ✅ A1 Direct Launch | 4 days | **May 30** |
| **A: PASS** | 1.25–1.55mm | Clean | All pass | ✅ A2 Optional 2nd test | 5 days | **May 31** |
| **B: MINOR-ADJ** | 1.10–1.25mm OR 1.55–1.70mm | No cracks, near-spec | Pass w/ tightness/looseness | ⚠️ B1 Quick tweak + retest | 5 days | **May 31** |
| **B: MINOR-ADJ** | 1.10–1.25mm OR 1.55–1.70mm | Clean, functional | Pass | ⚠️ B2 Accept + QC adjust | 4 days | **May 30** |
| **B: MINOR-ADJ** | 1.10–1.25mm OR 1.55–1.70mm | Clean | Pass | ⚠️ B3 Defer for data-driven optimization | 6-7 days | **June 2-5** |
| **C: FAIL** | <1.10mm OR >1.70mm | Cracks visible | Snap breaks | 🔴 C1 v2 redesign (if confidence ≥70%) | 4-5 days | **May 30-31 or June 2-5** |
| **C: FAIL** | <1.10mm OR >1.70mm | Cracks/stress | Snap breaks | 🔴 C2 Fallback pivot (if confidence <70%) | 7-10 days | **June 2-5** |
| **C: FAIL** | <1.10mm OR >1.70mm | Cracks | Snap breaks | 🔴 C3 Expert escalation (if unsure) | 8-12 days | **June 2-5** |
| **D: PARTIAL** | 0.5" pass ✓, 0.75" fail ✗ | Mixed | Mixed | 🟡 D1 Launch passing only + iterate | May 30 + June 2-5 | **May 30 (passing)** |
| **D: PARTIAL** | 2 of 3 sizes pass, 1 fails | Mixed | Mixed | 🟡 D1 Launch 2, iterate 1 | May 30 + June 2-5 | **May 30 (passing)** |
| **D: PARTIAL** | All 3 borderline/risky | All near-edge of spec | All marginal | 🟡 D2 Coordinated redesign, launch all together | 4-5 days | **June 1-2** |

---

## Decision Commitment Format (Use Day 1 After Test Print)

Copy this template to your project log and fill in immediately after test print evaluation:

```
TEST PRINT OUTCOME DECISION LOG
Date: [DATE]
Time: [TIMESTAMP]

─────────────────────────────────────────
INSPECTION RESULTS
─────────────────────────────────────────

Snap-arm measurement: [X]mm (target 1.4mm ±0.15mm)
Visual inspection: [notes on cracks, stress marks, color, surface]
Functional tests: [notes on flex, grip, post stability]
Other dimensions: bore [X]mm, mating surface [notes], post diameter [X]mm

─────────────────────────────────────────
OUTCOME CLASSIFICATION
─────────────────────────────────────────

Outcome: [A: PASS / B: MINOR-ADJ / C: FAIL / D: PARTIAL-FAIL]
Severity: [None / Low / Medium / High]

Root cause (if failure): [description or "TBD"]
Confidence in fix: [%]

─────────────────────────────────────────
ROUTING DECISION
─────────────────────────────────────────

Route chosen: [A1 / A2 / B1 / B2 / B3 / C1 / C2 / C3 / D1 / D2]
Rationale: [1-2 sentences on why this route]

Timeline commitment:
  Day 1 actions: [what you're doing today]
  Days 2-4 actions: [redesign, retest, production]
  Days 5+: [launch prep]
  Launch target date: [MAY 30 / MAY 31 / JUNE 1-2 / JUNE 2-5 / TBD]

Capital budget: $[amount for parts/materials]
Next checkpoint: [date and decision point]

─────────────────────────────────────────
NEXT IMMEDIATE ACTION
─────────────────────────────────────────

Start: [specific CAD edit / slicer adjustment / escalation / fallback CAD]
Estimated completion: [date/time]
Decision gate: [retest measurement target / expert response / etc.]

Signed: [your name]
Timestamp: [date and time]
```

**Example (Outcome B1)**:
```
TEST PRINT OUTCOME DECISION LOG
Date: May 24, 2026
Time: 14:30 UTC

─────────────────────────────────────────
INSPECTION RESULTS
─────────────────────────────────────────

Snap-arm measurement: 1.23mm (target 1.4mm ±0.15mm) — TIGHT
Visual inspection: No cracks, no stress marks, clean material color, smooth surface
Functional tests: Snap-arm flexes but with high resistance; clip holds cable under load
Other dimensions: bore 3.02mm ✓, mating surface flat ✓, post stable ✓

─────────────────────────────────────────
OUTCOME CLASSIFICATION
─────────────────────────────────────────

Outcome: B: MINOR-ADJ
Severity: Low

Root cause (if failure): Under-extrusion OR snap-arm CAD thickness too large
Confidence in fix: 85%

─────────────────────────────────────────
ROUTING DECISION
─────────────────────────────────────────

Route chosen: B1 (Quick adjustment + 1-day iteration)
Rationale: Root cause is clear (tolerance is 0.17mm too tight). Fix is simple (CAD tolerance +0.15mm or slicer flow -2%). High confidence retest will pass Day 2 morning. +1 day slip is acceptable (May 30 → May 31 launch).

Timeline commitment:
  Day 1 actions: Adjust CAD snap-arm thickness from 1.4mm to 1.50mm, regenerate STL, queue v2 test print
  Day 2: Measure v2, approve design if within spec, lock for production
  Days 3-4: Production batch printing
  Days 4-5: Part 1 Etsy prep (shop, listings, photos)
  Launch target date: MAY 31

Capital budget: $50 (filament and test materials)
Next checkpoint: Day 2 morning (v2 measurement decision)

─────────────────────────────────────────
NEXT IMMEDIATE ACTION
─────────────────────────────────────────

Start: Open cadquery/modrun_clip_b123d.py, locate SNAP_ARM_THICKNESS constant, edit from 1.4 to 1.50
Estimated completion: Today 15:00 (10 min edit + 5 min STL generation + 5 min queue print)
Decision gate: v2 snap-arm measurement tomorrow 10:00 AM, target 1.30–1.50mm. If PASS → approve + launch May 31. If FAIL → escalate to C (redesign or fallback).

Signed: user
Timestamp: May 24, 2026, 14:30 UTC
```

---

## Key Thresholds & Go/No-Go Decision Points

**Snap-Arm Dimensional Thresholds**:
- **GO** (Acceptable): 1.25–1.55mm (within target 1.4mm ±0.15mm)
- **GO-with-adjustment** (Minor tolerance issue): 1.10–1.25mm OR 1.55–1.70mm (CAD or slicer fix needed)
- **NO-GO** (Failure): <1.10mm OR >1.70mm (design review required)

**Confidence Threshold for Iteration**:
- ≥70% confidence in fix → Proceed with v2 redesign (A1, B1, C1, D2)
- <70% confidence in fix → Escalate to fallback pivot (A2, C2) or expert review (C3)

**Revenue Threshold for Partial Launch (D1)**:
- Passing SKU monthly revenue ≥$100 → Recommend D1 (launch passing, iterate failing)
- Passing SKU monthly revenue <$50 → Recommend D2 (hold all for coordinated launch)

**Timeline Thresholds**:
- Iteration adds ≤1 day → Acceptable (may slip launch by 1 day, still within window)
- Iteration adds 2-3 days → Borderline (consider fallback pivot if confidence <80%)
- Iteration adds >5 days → High risk (market window closing, consider fallback)

---

## Execution Workflows (Quick Reference)

**IF OUTCOME A** → Print & File Outcome A1 Checklist Above → Execute ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md Part 1-2 starting Day 2

**IF OUTCOME B** → Implement fix (CAD or slicer) → Queue v2 print → Wait for Day 2 measurement → If v2 PASS, execute Part 1-2 starting Day 2; if v2 FAIL, escalate to C

**IF OUTCOME C** (Confidence ≥70% in fix) → Implement v2 fix → Queue v2 print → Wait for Day 2 measurement → If v2 PASS, execute Part 1-2 starting Day 3; if v2 FAIL, escalate to C2 fallback

**IF OUTCOME C** (Confidence <70% in fix) → Escalate to expert OR select fallback product → Begin fallback CAD (Days 2-3) → Fallback test (Day 3) → Production batch (Days 4-5) → Execute Part 1-2 starting Day 5 (June 2-5 launch)

**IF OUTCOME D** → Measure revenue impact of passing SKUs → Decide D1 (launch passing only) or D2 (hold all) → Execute D1 or D2 checklist above → Part 2 launch Day 5 (May 30 or June 1-2) + parallel iteration on failing SKU

---

## Document Status & Sign-Off

**Version**: 1.0  
**Created**: 2026-06-06  
**Status**: Production-ready  
**Purpose**: Instant routing from test print outcome to contingency execution path without discovery overhead  

**Related Documents**:
- TEST_PRINT_FAILURE_INVESTIGATION_RUNBOOK.md (measurement procedures, templates, decision triggers)
- ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md (standard launch sequence if PASS or OUTCOME A)
- FAILURE_SCENARIO_DECISION_TREE.md (visual flowchart routing)
- post-test-print-launch-timeline.md (detailed T+0 to T+7 execution timeline)

**How to Use This Document**:
1. Perform test print inspection using TEST_PRINT_FAILURE_INVESTIGATION_RUNBOOK.md
2. Record measurements and outcome on this matrix
3. Find your outcome section (A, B, C, or D)
4. Follow immediate actions and timeline for your route
5. Execute checklist routing to Part 1 or contingency path
6. Use decision commitment format to log your choices

**This document is complete and self-contained.** No additional decision-making should be required once test print is evaluated.

---

*Last updated: 2026-06-06*  
*Status: READY FOR EXECUTION*
