---
title: Test Print Failure Investigation Runbook
subtitle: Structured measurement, analysis, and decision procedures for failure scenarios
project: mfg-farm
created: 2026-06-06
status: production-ready
purpose: "For OUTCOME C and D failures, provide step-by-step investigation procedures, measurement templates, photo documentation checklist, and decision triggers"
related: TEST_PRINT_OUTCOME_DECISION_MATRIX.md, FAILURE_SCENARIO_DECISION_TREE.md
---

# Test Print Failure Investigation Runbook

**Document Purpose**: When ModRun cable clip test print reveals failure (OUTCOME C: FAIL or OUTCOME D: PARTIAL-FAIL), this runbook provides:
1. Structured investigation procedures to identify root cause
2. Measurement templates for documenting findings
3. Photo documentation checklist for evidence capture
4. Decision triggers for go/no-go on redesign vs. fallback pivot
5. Material reference data for diagnosis

**Scope**: Failures only (Outcome C and Outcome D multi-issue scenarios). For Outcome A/B successes, skip to TEST_PRINT_OUTCOME_DECISION_MATRIX.md.

**Time Required**: 60-90 minutes for full investigation (30 min measurement + 30 min photo documentation + 15 min analysis)

---

## Part 1: Structured Failure Inspection Protocol (30 Minutes)

**Start with this systematic inspection before jumping to diagnosis.**

### Step 1: Visual Inspection (5 minutes)

**Setup**: Clean workspace, good lighting (natural light or LED lamp at 45° angle), magnifier or macro phone camera

| Inspection Point | Check This | Record Here |
|---|---|---|
| **Snap-arm overall** | Visually compare to design reference: is it shorter, thinner, thicker than expected? Any discoloration? | ☐ Shorter ☐ Thinner ☐ Thicker ☐ Discolored |
| **Snap-arm cracks** | Look for visible cracks anywhere on snap-arm (base, mid-arm, tip). Take close-up photo. | ☐ No cracks visible ☐ Cracks at [BASE/MID/TIP] — PHOTO: [filename] |
| **Stress marks** | Look for white stress lines or layer separation lines along snap-arm length. | ☐ No stress marks ☐ Stress marks visible at [describe location] — PHOTO: [filename] |
| **Material color** | Check if filament color is consistent across part. Dark spots or burnt areas? | ☐ Consistent color ☐ Dark spots at [location] ☐ Burnt smell? YES/NO |
| **Mating surface** | Look at where snap-arm connects to main clip body. Is junction smooth or jagged? Sharp corner or rounded? | ☐ Smooth junction ☐ Jagged/rough ☐ Sharp corner (risk of stress concentration) ☐ Well-rounded |
| **Rail bore diameter** | Visually, does the bore look right-sized for 3mm cable? Too large, too small, or right? | ☐ Right-sized ☐ Too large ☐ Too small |
| **Post diameter** | Check cable post (if present): does it look like 8mm? | ☐ Right-sized ☐ Too thin ☐ Too thick |
| **Surface finish** | Run fingernail gently across snap-arm. Is it smooth or rough? | ☐ Smooth ☐ Rough/striated ☐ Layer separation visible |
| **Overall print quality** | Are layer lines visible? Uniform or uneven? Any missing infill visible (holes in side walls)? | ☐ Clean layers ☐ Uneven layers ☐ Visible gaps (under-extrusion sign) |

**Analysis**: If you see any of these RED FLAGS, note them:
- ⚠️ Cracks or stress marks → Design stress concentration or material brittleness
- ⚠️ Dark spots or burnt smell → Over-heating (nozzle temp too high)
- ⚠️ Visible layer separation → Layer adhesion issue (too cold? humidity? speed too fast?)
- ⚠️ Rough surface or missing infill → Under-extrusion (flow rate too low)
- ⚠️ Sharp corner at snap-arm base → Likely stress concentration point

---

### Step 2: Dimensional Measurement (20 minutes)

**Tools Needed**: Digital calipers (±0.1mm accuracy), ruler, spreadsheet or paper

**Snap-Arm Thickness** (Critical — do this first):

1. Place clip on flat surface with snap-arm pointing upward
2. Position calipers perpendicular to snap-arm, measure at middle of arm length (not at base or tip)
3. Take 3 measurements at different points along snap-arm (measure at 1/4 length, 1/2 length, 3/4 length)
4. Record all three measurements

| Measurement Point | Reading | Target | Status |
|---|---|---|---|
| Snap-arm at 1/4 length (from base) | _____ mm | 1.4 ±0.15 | ☐ PASS ☐ FAIL |
| Snap-arm at 1/2 length | _____ mm | 1.4 ±0.15 | ☐ PASS ☐ FAIL |
| Snap-arm at 3/4 length | _____ mm | 1.4 ±0.15 | ☐ PASS ☐ FAIL |
| **Average** | _____ mm | 1.4 ±0.15 | ☐ PASS ☐ FAIL |

**Interpretation**:
- **All three within 1.25–1.55mm** → Tolerance is OK. If snap still failed, issue is geometry (stress concentration) not thickness.
- **All three <1.10mm** → Under-extrusion (flow too low). Fix: increase flow +3%.
- **All three >1.70mm** → Over-extrusion (flow too high) or CAD thickness wrong. Fix: reduce flow -2% or edit CAD.
- **Varies by ±0.3mm across length** → Inconsistent extrusion (likely uneven temperature or filament diameter). Fix: check nozzle temp, filament path.

---

**Bore Diameter** (Cable hole in rail):

1. Use calipers to measure bore from inside edge to inside edge (internal diameter)
2. Take measurement from 2-3 points across bore length
3. Expected: 3.0 ±0.2mm (bore should accept 2.9–3.2mm bare cable)

| Measurement Location | Reading | Target | Status |
|---|---|---|---|
| Bore at entrance | _____ mm | 3.0 ±0.2 | ☐ PASS ☐ FAIL |
| Bore at middle | _____ mm | 3.0 ±0.2 | ☐ PASS ☐ FAIL |
| Bore at exit | _____ mm | 3.0 ±0.2 | ☐ PASS ☐ FAIL |

**Interpretation**:
- **All within 2.8–3.2mm** → Bore is acceptable. Cable should fit smoothly.
- **All <2.8mm** → Bore too tight. Fix: increase bore diameter +0.2mm in CAD.
- **All >3.2mm** → Bore too loose. Fix: decrease bore diameter -0.2mm in CAD, or accept as cosmetic variance.
- **Varies significantly (>0.3mm variance)** → Tapering issue (likely print angle or bed tilt). Fix: verify printer bed leveling, check print orientation.

---

**Mating Surface (Snap-arm junction)**:

1. Place clip on flat surface (like a table)
2. Check if mating surface (where snap-arm connects to body) sits flush or is raised/recessed
3. If raised/recessed, measure gap with calipers

| Check | Measurement | Status |
|---|---|---|
| Is mating surface flush with table? | ☐ YES ☐ NO | — |
| If not flush, how much gap? | _____ mm | ☐ <0.1mm (acceptable) ☐ >0.1mm (fix needed) |
| Is junction smooth or rough? | ☐ Smooth ☐ Rough | — |

**Interpretation**:
- **Flush, smooth** → Good. No stress concentration risk.
- **Recessed <0.1mm** → Acceptable (normal print tolerance). No design issue.
- **Raised >0.1mm or rough** → Possible layer adhesion issue. Fix: check bed temperature (too low?), clean nozzle.

---

**Post Diameter** (if cable management post is present):

1. Measure post diameter with calipers at 2-3 points along its height
2. Expected: 8 ±0.5mm

| Measurement Location | Reading | Target | Status |
|---|---|---|---|
| Post at base (where it connects) | _____ mm | 8 ±0.5 | ☐ PASS ☐ FAIL |
| Post at middle | _____ mm | 8 ±0.5 | ☐ PASS ☐ FAIL |
| Post at tip | _____ mm | 8 ±0.5 | ☐ PASS ☐ FAIL |

**Interpretation**:
- **All 7.5–8.5mm** → Post is good. Cable should wrap smoothly.
- **<7.5mm** → Post too thin. Fix: increase post diameter +0.3mm in CAD.
- **>8.5mm** → Post too thick. Fix: decrease post diameter -0.3mm in CAD.

---

### Step 3: Functional Testing (5 minutes)

**Snap-Arm Flex Test**:
1. Hold clip in one hand
2. Gently flex snap-arm up and down 5-10 times with other hand
3. Record observation

| Test | Result | Interpretation |
|---|---|---|
| Can you flex snap-arm up without breaking? | ☐ YES (5+ cycles) ☐ NO (breaks immediately) | YES = functional; NO = material too brittle or geometry too weak |
| Does snap-arm make snapping sound when flexed? | ☐ YES ☐ NO | YES = good material compliance; NO = material stiff |
| After 10 flex cycles, are there visible cracks? | ☐ NO ☐ YES | NO = good; YES = fatigue issue (design needs reinforcement) |
| Does snap-arm return to original shape or stay bent? | ☐ Returns ☐ Stays bent | Returns = good elastic recovery; Stays = material overworked or too soft |

**Go/No-Go**:
- ✅ **PASS flex test**: Can flex 10+ times without cracks, returns to shape, no brittleness
- 🔴 **FAIL flex test**: Breaks on first flex, or visible cracks after 3 cycles, or material feels brittle

---

**Grip Test** (if clip mounts on rail or cable):
1. Place clip on test cable or rail with intended mounting load
2. Pull cable/rail horizontally with medium force (equivalent to 500g hanging weight)
3. Record observation

| Test | Result | Interpretation |
|---|---|---|
| Does clip hold cable without slipping? | ☐ YES ☐ NO | YES = good grip; NO = snap-arm too loose or bore too large |
| Is grip force reasonable (not requiring extreme force)? | ☐ YES (light grip) ☐ NO (very tight or very loose) | YES = good; NO = tolerance needs adjustment |
| Can you manually release clip without breaking it? | ☐ YES ☐ NO | YES = good design; NO = snap-arm too tight (design issue) |

**Go/No-Go**:
- ✅ **PASS grip test**: Holds cable securely without excessive force, can be manually released
- 🔴 **FAIL grip test**: Slips under light load, or requires excessive force to engage/release

---

**Post Stability Test** (if post is present):
1. Hold clip with post pointing upward
2. Wrap cable around post and apply downward pull (equivalent to 500g cable weight)
3. Measure post wobble with ruler (how far does post move laterally?)

| Test | Result | Interpretation |
|---|---|---|
| Post wobble under cable load | _____ mm | <0.5mm = stable; 0.5–2mm = marginal; >2mm = unstable |
| Is post smooth or does cable catch? | ☐ Smooth ☐ Catches | Smooth = good; Catches = surface finish issue |

**Go/No-Go**:
- ✅ **PASS post test**: Wobble <0.5mm, post is rigid, cable wraps smoothly
- 🔴 **FAIL post test**: Wobble >2mm, post flexes excessively, cable catches

---

### Step 4: Material Inspection (5 minutes)

| Check | Observation | Possible Cause |
|---|---|---|
| **Filament condition** | Is spool dusty/wet/discolored? | Wet filament → poor print quality. Dry before next print: 60°C for 4-6 hours. |
| **Print smell** | Does print smell burnt, plasticky, or neutral? | Burnt smell → nozzle temp too high. Reduce 5°C. |
| **Material flexibility** | Can you bend a small scraps piece without it snapping? | Snaps easily = material too brittle (too cold to print or wrong material). Flexes = OK. |
| **Material color** | Consistent color or spots/streaks? | Spots/streaks = inconsistent extrusion or filament contamination. |
| **Weight check** | Weigh entire print. Expected weight? | Significantly lighter than expected = under-extrusion. Heavier = over-extrusion. |

---

## Part 2: Photo Documentation Checklist (30 Minutes)

**Capture evidence photos for diagnosis and archive. Use phone camera or macro lens.**

### Photo Requirements

| Photo | Purpose | Angles | Notes |
|---|---|---|---|
| **Close-up: Snap-arm** | Show snap-arm thickness, cracks, stress marks | Top view, side view, angled view showing thickness | Use macro mode, good lighting from above |
| **Close-up: Snap-arm base** | Show junction quality, stress concentration risk | Side view of base where arm connects | Check for sharp corners, layer separation |
| **Close-up: Crack or failure** | Document any visible cracks or breaks | Multiple angles of crack, showing depth | Use macro + good lighting |
| **Overall clip** | Show print quality, layer finish, warping | Top, bottom, side views | Check for uniformity |
| **Bore/hole detail** | Show internal bore size and finish | Looking into bore (use phone light to illuminate) | Check for roughness, under-extrusion |
| **Post (if present)** | Show post diameter, surface finish | Side view of post, top view | Check for wobble, surface quality |
| **Mating surface** | Show snap-arm junction area | Close-up of junction, flat-surface check | Check for gaps, layer separation |
| **Scale reference** | Show size relative to known object | Clip next to ruler, coin, or finger | For dimension verification |

### How to Photograph

**Setup**:
1. Place clip on white poster board or mat
2. Position phone at 45° angle with good lighting (natural window light is best)
3. Use macro mode (phone camera "macro" or dedicated macro lens)
4. Take 2-3 shots per angle (one may be blurry; redundancy helps)

**Filename convention**:
- `failure-analysis-snap-arm-close-up-[DATE].jpg`
- `failure-analysis-crack-at-base-[DATE].jpg`
- `failure-analysis-overall-view-[DATE].jpg`

**Storage**:
- Save all photos to: `/projects/mfg-farm/failure-analysis/[DATE]/`
- Backup to external drive or cloud (Google Drive, GitHub, AWS S3)

---

## Part 3: Root Cause Analysis Decision Tree (15 Minutes)

**Use measurements and observations from Parts 1-2 to diagnose root cause.**

### Snap-Arm Failure Diagnosis

```
SNAP-ARM FAILED (cracks on flex test OR breaks on load)
│
├─ Check: Is snap-arm thickness within spec (1.25–1.55mm)?
│  │
│  ├─ NO, thickness <1.10mm (too thin)
│  │  │ Likely cause: UNDER-EXTRUSION
│  │  │ Symptoms: Snap-arm is thinner than spec, may break cleanly
│  │  │ Confidence: 85%
│  │  │ Evidence to look for: Thin walls across print, missing infill visible at sides
│  │  │ Fix: Increase flow +3% in slicer OR check nozzle for blockage
│  │  │ Retest: Print v2 with +3% flow, measure snap-arm (should be 1.4mm)
│  │  │
│  │  └─ Decision: If <1.20mm measured, UNDER-EXTRUSION is confirmed → Fix flow, retest
│  │
│  ├─ NO, thickness >1.70mm (too thick)
│  │  │ Likely cause: OVER-EXTRUSION or CAD error
│  │  │ Symptoms: Snap-arm is thicker than expected, may be stiff/brittle
│  │  │ Confidence: 75% (could also be material brittleness if thick but snaps)
│  │  │ Evidence to look for: Thick walls, elephant foot (base is wider), rough finish
│  │  │ Fix: Reduce flow -2% in slicer OR check CAD thickness value
│  │  │ Retest: Print v2 with -2% flow, measure snap-arm (should be 1.4mm)
│  │  │
│  │  └─ Decision: If >1.70mm measured, OVER-EXTRUSION likely → Fix flow, retest
│  │
│  └─ YES, thickness is OK (1.25–1.55mm)
│     │ But snap-arm still failed → Problem is NOT thickness, but GEOMETRY or MATERIAL
│     │
│     ├─ Sub-check: Are stress marks visible on snap-arm?
│     │  │
│     │  ├─ YES, stress marks at base or mid-arm
│     │  │  │ Likely cause: GEOMETRY STRESS CONCENTRATION
│     │  │  │ Symptoms: Cracks at base where arm connects to body (sharp corner?), or cracks at mid-arm (thin point?)
│     │  │  │ Confidence: 80%
│     │  │  │ Evidence: Sharp corner at snap-arm base, thin section at mid-arm, layer separation at junction
│     │  │  │ Fix: Add 0.3–0.5mm radius fillet at snap-arm base, OR increase arm thickness by 0.1mm
│     │  │  │ Retest: CAD edit, v2 print, retest flexing
│     │  │  │
│     │  │  └─ Decision: Edit CAD to add fillet or reinforce base, retest
│     │  │
│     │  └─ NO, no visible stress marks but still breaks on flex
│     │     │ Likely cause: MATERIAL BRITTLENESS (filament property issue)
│     │     │ Symptoms: Print material is brittle, snaps without bending, may be discolored or smell burnt
│     │     │ Confidence: 70%
│     │     │ Evidence: Burnt smell, discoloration, material snaps when hand-flexed
│     │     │ Fix: Dry filament (wet PLA+ absorbs humidity, prints brittle), reduce nozzle temp 5°C, or try new filament batch
│     │     │ Retest: Dry filament 4-6 hours at 60°C, reduce temp to 215°C, print v2, test flexibility
│     │     │
│     │     └─ Decision: Dry filament or reduce nozzle temp, retest
│
└─ Final diagnosis: [Pick one] → Proceed with fix → Retest Day 2
```

### Bore or Post Failure Diagnosis

```
BORE OR POST DIAMETER OUT OF SPEC (too large, too small, or unstable)
│
├─ If bore <2.8mm (too tight):
│  │ Likely cause: CAD bore too small OR under-extrusion (walls thickened bore)
│  │ Fix: Increase bore diameter +0.2mm in CAD, regenerate STL, retest
│  │ Confidence: 85%
│  │
│  └─ Decision: Edit CAD bore constant (BORE_DIAMETER = 3.0 → 3.2mm), retest
│
├─ If bore >3.2mm (too loose):
│  │ Likely cause: Over-extrusion (walls ate into bore) OR CAD bore too large
│  │ Fix: Reduce bore diameter -0.2mm in CAD, OR reduce flow -2% in slicer
│  │ Confidence: 75%
│  │
│  └─ Decision: Reduce bore diameter in CAD (3.0 → 2.8mm) or reduce slicer flow -2%, retest
│
└─ If post wobbles >2mm (unstable):
   │ Likely cause: Infill too sparse (post is hollow) OR post diameter too thin
   │ Fix: Increase infill from 25% → 30%, OR increase post diameter from 8mm → 8.5mm
   │ Confidence: 80%
   │
   └─ Decision: Edit CAD post diameter (8.0 → 8.5mm) OR increase slicer infill (25% → 30%), retest
```

---

## Part 4: Decision Triggers for Go/No-Go on Redesign

**Use these objective thresholds to decide whether to iterate (v2 redesign) or pivot to fallback.**

### Confidence Assessment Worksheet

For each diagnosis, fill in confidence level (0-100%):

| Root Cause Identified | Confidence in Fix | Notes | Next Action |
|---|---|---|---|
| **Under-extrusion** (snap-arm measured <1.10mm) | _____% | Typically 85%+ confident; flow adjustment is straightforward | If ≥70%: Do v2 redesign (adjust flow +3%). If <70%: Escalate |
| **Over-extrusion** (snap-arm measured >1.70mm) | _____% | Typically 75%+ confident; could also be material | If ≥70%: v2 redesign (reduce flow -2%). If <70%: Escalate |
| **Slicer layer height** (stress marks at layer boundaries) | _____% | Typically 70%+ confident; layer height 0.15mm reduces issue | If ≥70%: v2 redesign (0.15mm layer height). If <70%: Escalate |
| **Geometry stress concentration** (cracks at snap-arm base, sharp corner visible) | _____% | Typically 75%+ confident; add fillet or reinforce base | If ≥70%: v2 redesign (add fillet). If <70%: Escalate |
| **Material brittleness** (print snaps without bending, burnt smell) | _____% | Typically 70%+ confident; filament may be wet or overheated | If ≥70%: v2 redesign (dry filament, reduce temp). If <70%: Escalate |
| **Print settings misalignment** (STL scale wrong, units error) | _____% | Typically 90%+ confident; very quick fix (re-export STL) | If ≥70%: v2 redesign (fix scale). If <70%: Escalate |
| **Unknown / multiple hypotheses equally likely** | _____% | If you can't narrow down to one cause, confidence is <60% | If <70%: Escalate to expert OR pivot to fallback |

### Decision Gate: Redesign (v2) vs. Fallback Pivot

**After filling in confidence levels above:**

- **All diagnoses ≥70% confidence in fix** → ✅ **Proceed with v2 redesign** (you have clear path forward)
  - Implement highest-priority fix (usually under/over-extrusion is fastest)
  - Print v2 test Day 1 evening, measure Day 2 morning
  - If v2 passes: lock design, production batch Days 3-4
  - If v2 fails: reassess and escalate to fallback

- **Most diagnoses 60-70% confidence** → ⚠️ **Consider escalation to expert first** (wait 2-4 hours for expert advice before committing to 2-3 day iteration)
  - Post photos + measurements to r/3Dprinting or Bambu Discord
  - Get expert feedback, update confidence level
  - If expert confirms diagnosis (confidence now ≥75%): proceed with v2
  - If expert says unclear: pivot to fallback

- **Most diagnoses <60% confidence** → 🔴 **Pivot to fallback product** (iteration risk is too high)
  - Select fallback (magnetic clips, adhesive-only, or screw-mount)
  - Begin fallback CAD work Days 2-3
  - Fallback test print Day 3-4
  - Launch fallback June 2-5

---

## Part 5: Material Reference Data & Troubleshooting

### PLA+ Print Parameter Reference

| Parameter | Optimal Range | Too Low | Too High | Symptom |
|---|---|---|---|---|
| **Nozzle Temp** | 215–225°C | <210°C: under-extrusion, brittle | >230°C: burnt smell, discolored, weak | Measure actual temp on printer display |
| **Bed Temp** | 60–65°C | <55°C: poor adhesion, warping | >70°C: elephant foot, over-sized first layer | Check printer bed temp display |
| **Flow Rate** | 100% (baseline) | <95%: under-extrusion, thin walls | >105%: over-extrusion, blobs, rough surface | Adjust in Bambu Studio: Nozzle Profile → Flow |
| **Layer Height** | 0.20mm (standard) | <0.15mm: very fine but slow | >0.25mm: coarse surface, snap-arms too blocky | Best for features <2mm: use 0.15mm |
| **Print Speed** | 200mm/s outer, 300mm/s infill | <100mm/s: very slow but cleaner | >300mm/s outer: layer separation, artifacts | Bambu P1S can handle 200 outer comfortably |
| **Infill** | 25% (gyroid) | <20%: weak structure | >30%: heavier, wastes material | Gyroid gives isotropic strength |

### Under-Extrusion Red Flags

**Visual**: Thin walls, missing infill visible, parts feel lightweight
**Measurement**: Snap-arm <1.10mm, bore walls thin/rough, lines visible through sides
**Solutions** (in order of likelihood):
1. **Increase flow +3%** (in Bambu Studio nozzle profile)
2. **Check nozzle for blockage** (remove filament, heat to 230°C, try pushing through or use cleaning wire)
3. **Verify filament path** (is filament jammed between extruder and nozzle?)
4. **Check filament diameter** (should be 1.75 ±0.03mm on spool label)
5. **Reduce print speed by 20%** (slower = more time for extrusion)

### Over-Extrusion Red Flags

**Visual**: Thick walls, blobs at corners, rough surface, elephant foot at base
**Measurement**: Snap-arm >1.70mm, bore looks thick/clogged
**Solutions** (in order of likelihood):
1. **Reduce flow -2%** (in Bambu Studio nozzle profile)
2. **Reduce nozzle temp 5°C** (225°C → 220°C; material less viscous = flows less)
3. **Verify filament diameter** (oversized filament = more material flows than expected)
4. **Check bed leveling** (if nozzle too close to bed, material gets squeezed sideways = over-extrusion appearance)

### Brittleness Red Flags

**Visual**: Material cracks easily under flex, snaps without bending, discolored
**Likely causes**:
1. **Filament is wet** (PLA+ absorbs humidity). Solution: Dry 4-6 hours at 60°C in oven or desiccant box
2. **Nozzle temp too high** (material overheated). Solution: Reduce to 215°C
3. **Wrong material type** (printed PETG-style settings on PLA+). Solution: Verify slicer profile is "PLA+" not generic PLA
4. **Old filament** (PLA+ degrades over 2-3 years). Solution: Try newer batch

---

## Part 6: Quick Diagnosis Templates (Copy & Fill In)

### Template A: Under-Extrusion Suspected

```
UNDER-EXTRUSION DIAGNOSIS

Snap-arm measurement: _____ mm (expected 1.4mm)
Delta: _____ mm too thin

Visual evidence:
  [ ] Thin walls visible across print
  [ ] Missing infill visible on sides
  [ ] Overall print feels lightweight
  [ ] Surface is rough/striated

Confidence assessment: _____% 
(If ≥70%, proceed with flow +3% fix)

Fix to implement:
  [ ] Open Bambu Studio
  [ ] Go to: Nozzle Profile → Flow
  [ ] Change from 100% to 103%
  [ ] Regenerate G-code for v2 test print
  [ ] Queue print Day 1 evening

v2 test print specs:
  - Expected snap-arm: 1.4–1.5mm
  - Retest scheduled: Day 2, 10:00 AM
  - Decision gate: If v2 within spec, approve design + production
  
Escalation trigger: If v2 still <1.25mm, escalate to expert
```

### Template B: Geometry Stress Concentration Suspected

```
GEOMETRY STRESS CONCENTRATION DIAGNOSIS

Visible cracks at: [ ] Base of snap-arm [ ] Mid-arm [ ] Snap-arm tip
Stress marks visible: [ ] YES [ ] NO
Sharp corner at snap-arm base: [ ] YES [ ] NO

Snap-arm thickness: _____ mm (within spec? [ ] YES [ ] NO)

Visual evidence:
  [ ] Cracks originate at sharp junction (snap-arm to body)
  [ ] Stress marks form pattern (horizontal / vertical / radial)
  [ ] Break point is consistent location across flex tests

Confidence assessment: _____% (typically 75–80% for sharp corner)

Fix to implement:
  [ ] Open cadquery/modrun_clip_b123d.py
  [ ] Find SNAP_ARM_BASE_RADIUS constant (current value: _____)
  [ ] Increase radius by 0.3–0.5mm: NEW_VALUE = current + 0.3
  [ ] Regenerate STL: uv run python modrun_clip_b123d.py --output-dir stl/
  [ ] Queue print Day 1 evening

v2 test print specs:
  - Expected improvement: Cracks should disappear
  - Retest scheduled: Day 2, flex test 10+ cycles
  - Decision gate: If no cracks after 10 flex cycles, approve design
  
Escalation trigger: If v2 still has cracks, escalate to expert (may need structural redesign)
```

### Template C: Material Brittleness Suspected

```
MATERIAL BRITTLENESS DIAGNOSIS

Print smell: [ ] Burnt [ ] Plasticky [ ] Neutral
Discoloration visible: [ ] YES [ ] NO (location: _____)
Hand-flex test of scrap: [ ] Snaps [ ] Flexes [ ] Bends without breaking

Filament spool condition:
  [ ] Dusty / humid appearance
  [ ] Color consistent or streaked
  [ ] Spool sealed or open

Confidence assessment: _____% (typically 70% for brittleness)

Fix to implement (pick one):
  [ ] Option A: Dry filament
      - Place spool in oven at 60°C for 4–6 hours
      - Store in airtight container with desiccant
      - Retest print Day 2
  
  [ ] Option B: Reduce nozzle temp
      - Current temp: 220°C → New temp: 215°C
      - Regenerate G-code with new temp profile
      - Retest print Day 1 evening
  
  [ ] Option C: Try new filament batch
      - Open new spool of PLA+ (same brand)
      - Verify expiration date and storage condition
      - Retest print Day 1 evening

v2 test print specs:
  - Expected improvement: Print should flex without snapping
  - Retest scheduled: Day 2, hand-flex test of snap-arm
  - Decision gate: If snap-arm flexes 10+ cycles without cracks, approve design
  
Escalation trigger: If v2 still brittle after drying/temp reduction, escalate to expert (may indicate material defect)
```

---

## Part 7: Escalation Procedure for Expert Consultation

**Use when confidence is <70% or you have multiple competing diagnoses.**

### How to Escalate

1. **Prepare evidence package** (15 min):
   - All photos from Part 2 (snap-arm close-ups, cracks, overall)
   - All measurements from Part 1 (snap-arm thickness, bore, material notes)
   - Failure description (what happened when it broke?)
   - Slicer settings (copy from Bambu Studio profile)
   - CAD model (optional but helpful)

2. **Choose escalation channel** (fastest first):
   - **Bambu Lab Discord** (fastest: 30-60 min response)
     - Channel: #support or tag @support
     - Include: Photos + "PLA+ test print snap-arm failed, measured 0.95mm vs. 1.4mm spec"
   - **r/3Dprinting** (1-2 hour response)
     - Post with [HELP] tag, photos, measurements
   - **Local maker community** (2-4 hours)
     - Post to local Slack/Discord

3. **Post format**:
   ```
   HELP: Test print failed. Snap-arm issue.
   
   Project: 3D-printed cable clip (PLA+)
   Snap-arm design spec: 1.4mm thickness, 20mm length
   
   Print settings:
   - Nozzle: 220°C
   - Bed: 60°C
   - Layer height: 0.20mm
   - Flow: 100% (default)
   - Material: PLA+ (eSUN, recently purchased)
   
   Failure details:
   - Snap-arm broke on flex test
   - Measured thickness: [X]mm
   - Visible cracks: [YES/NO, location]
   - Stress marks: [YES/NO, pattern]
   
   Possible causes I'm considering:
   1. Under-extrusion (snap-arm too thin?)
   2. Geometry stress concentration (sharp corner at base?)
   3. Material issue (filament was damp?)
   
   Question: What does this failure pattern suggest?
   Recommended fix?
   
   [Attach photos of snap-arm close-up, cracks, overall print]
   ```

4. **Timeline**:
   - Post to Discord: Day 1 afternoon (~14:00)
   - Wait for expert response: Day 1 evening (16:00-18:00) or Day 2 morning
   - Implement recommendation: Days 2-3
   - Retest: Day 3-4
   - Decision on proceed (v2) or pivot (fallback): Day 4

---

## Part 8: Final Diagnosis Summary & Decision (5 Minutes)

**Complete this form when investigation is done:**

```
TEST PRINT FAILURE INVESTIGATION SUMMARY
Date: [DATE]
Time: [START TIME] — [END TIME] (_____ minutes elapsed)

═══════════════════════════════════════════════════════════════

FINDINGS

Primary root cause (most likely): [description]
Confidence level: _____% 

Supporting evidence:
  □ Measurement data: [snap-arm thickness, bore diameter, etc.]
  □ Visual inspection: [cracks, stress marks, discoloration, etc.]
  □ Functional tests: [flex test, grip test, post stability result]
  □ Material inspection: [filament condition, brittleness, smell, etc.]

Secondary hypotheses (if applicable):
  1. [description] - Confidence _____% 
  2. [description] - Confidence _____%

═══════════════════════════════════════════════════════════════

DECISION

✅ Confidence ≥70%: PROCEED WITH V2 REDESIGN
   Fix to implement: [description]
   Timeline: v2 print Day 1 evening, retest Day 2 morning
   Expected snap-arm measurement after fix: _____ mm

⚠️  Confidence 60-70%: ESCALATE TO EXPERT FIRST
   Questions for expert: [list 2-3 specific questions]
   Escalation channel: [Bambu Discord / r/3Dprinting / other]
   Timeline: Post evidence today, wait for response, implement recommendation

🔴 Confidence <60%: PIVOT TO FALLBACK PRODUCT
   Fallback product selected: [Magnetic / Adhesive / Screw-mount]
   Fallback confidence: _____% (typically 90%+ for fallback)
   Timeline: Fallback CAD Days 2-3, test Day 3-4, launch June 2-5

═══════════════════════════════════════════════════════════════

NEXT IMMEDIATE ACTION

Start: [specific action] (CAD edit / slicer change / expert post / fallback CAD)
Estimated completion: [date/time]
Decision gate: [measurement target / expert response / fallback test result]

Signed: [your name]
Timestamp: [date and time]
```

---

## Document Status & Sign-Off

**Version**: 1.0  
**Created**: 2026-06-06  
**Status**: Production-ready  
**Purpose**: Structured investigation procedures for test print failure diagnosis  

**When to Use**: OUTCOME C (FAIL) or OUTCOME D (PARTIAL-FAIL) only. For OUTCOME A/B successes, skip to TEST_PRINT_OUTCOME_DECISION_MATRIX.md and proceed to launch.

**Related Documents**:
- TEST_PRINT_OUTCOME_DECISION_MATRIX.md (main decision routing document)
- FAILURE_SCENARIO_DECISION_TREE.md (visual flowchart)
- post-test-print-launch-timeline.md (detailed T+0 to T+7 timeline)

**How to Use**:
1. Perform test print inspection (Part 1: 30 min)
2. Capture evidence photos (Part 2: 30 min)
3. Work through diagnosis decision tree (Part 3: 15 min)
4. Fill in decision triggers (Part 4: 5 min)
5. Complete final summary (Part 8: 5 min)
6. Reference material guide (Part 5) as needed for troubleshooting

**Total time**: 60-90 minutes for full investigation

---

*Last updated: 2026-06-06*  
*Status: READY FOR EXECUTION*
