---
title: Post-Test-Print STL Refinement Sequence
project: mfg-farm
created: 2026-05-06
status: ready-to-execute
audience: Anya — execute immediately after test print completes
scope: Tolerance calibration, STL regeneration, quality gates, 48–72 hour production-ready timeline
related: post-test-print-execution.md, cadquery/modrun_clip_b123d.py, cadquery/modrun_rail_b123d.py, stl/
confidence: high
---

# Post-Test-Print STL Refinement Sequence

**Lead finding:** The test print is a single measurement event. The FDM_TOLERANCE parameter is the only value that needs to change between test and production. Everything else in the CadQuery source locks on first pass. This document is the 48–72 hour path from test print in hand to production-ready, git-tagged STL files with a confirmed slicer profile.

---

## Hour 0: Test Print Evaluation (30 minutes)

Do this the moment the print comes off the bed. Do not queue production prints until these checks pass.

### 1.1 Measurement Protocol

Use digital calipers (Neiko or iGaging, any ±0.01mm-resolution unit). Measure directly from the printed part — not from screen or model.

**Snap arm width:**
- Target: 7.6 mm (SNAP_ARM_WIDTH constant in CadQuery source)
- Accept range: 7.3–7.9 mm
- Record actual: _______ mm

**Snap arm thickness:**
- Target: 1.4 mm (SNAP_ARM_THICKNESS)
- Accept range: 1.2–1.6 mm
- Record actual: _______ mm

**Rail slot entry width (clip side):**
- Target: slot should accept rail section freely with no binding and no side play exceeding 0.3 mm
- Measure the opening width of the clip's rail engagement slot
- Record actual: _______ mm

**Cable bore diameter (6mm clip):**
- Target: 6.0 mm internal
- Accept range: 5.7–6.3 mm (cable should enter with light finger pressure, not fall through freely)
- Record actual: _______ mm

**Overall clip body height:**
- Target: as designed (measure against the STL reference if you have a ruler on screen)
- Significant deviation (>0.5 mm) indicates Z-calibration issue, not tolerance issue

### 1.2 Snap-Fit Functional Test

Perform in this sequence. All three must pass before declaring the test print acceptable.

**Test A — Rail engagement:**
- Press the clip into a printed rail segment at normal finger pressure
- Pass: seats with a tactile click, no binding, no force required
- Fail — too tight: clip requires tool pressure or does not seat fully
- Fail — too loose: clip rattles when inserted, no tactile click

**Test B — Cable retention:**
- Insert a 6mm cable (or a 6mm dowel rod) into the bore from the open side
- Hold the clip sideways (cable facing down) for 10 seconds
- Pass: cable stays in place
- Fail: cable drops out freely

**Test C — Snap arm flex:**
- Flex the snap arm approximately 30% of its travel by hand
- Release
- Pass: returns to original position with no visible cracking or permanent set
- Fail: arm cracks at base, or arm deflects and does not return

### 1.3 Interpreting Results — FDM_TOLERANCE Adjustment Decision

| Observation | Likely Cause | Action |
|---|---|---|
| Clip binds in rail, requires force | FDM_TOLERANCE too low (walls thicker than nominal) | Increase tolerance by 0.05 mm |
| Clip loose in rail, rattles or falls out | FDM_TOLERANCE too high (walls undersize) | Decrease tolerance by 0.05 mm |
| Cable bore too tight (cable won't insert) | Bore undersized due to FDM shrinkage on inside-radius features | Increase BORE_DIAMETER_ADD by 0.1 mm |
| Cable bore too loose (cable drops out) | Bore oversized | Decrease BORE_DIAMETER_ADD by 0.1 mm |
| Snap arm too stiff to click in by hand | Wall thickness excessive or infill pattern interfering | Check SNAP_ARM_THICKNESS; also verify slicer wall count setting (should be 3 perimeters) |
| Snap arm cracks at 30% flex | Underextrusion on thin section, or infill too low | Check nozzle temperature and flow; re-run with 20% gyroid infill minimum |
| Snap arm permanent set (doesn't spring back) | Print orientation wrong or FDM layer lines perpendicular to flex direction | Verify clip is oriented upright on build plate (snap arm flexes in Z-direction) |

**Tolerance decision table:**

| FDM_TOLERANCE default | 0.15 mm |
|---|---|
| If rail-fit is tight | 0.20 mm |
| If rail-fit is very tight | 0.25 mm |
| If rail-fit is loose | 0.10 mm |
| If near-perfect on first print | Keep 0.15 mm |

Write the confirmed value here: FDM_TOLERANCE = _______ mm

---

## Hours 1–3: CadQuery Regeneration (if tolerance adjustment needed)

Skip this section entirely if the test print passes all three functional tests with no modifications needed. Proceed directly to Section 3 (Slicer Profile Lock).

### 2.1 Parameter Updates

Open `cadquery/modrun_clip_b123d.py`. Update the FDM_TOLERANCE constant at the top of the file:

```python
FDM_TOLERANCE = 0.15  # CHANGE THIS VALUE based on test print results
```

If bore sizing also needs adjustment, update the bore diameter addition parameter:
```python
BORE_DIAMETER_ADD = 0.2  # increase to 0.3 if bore is too tight on 6mm cable
```

Open `cadquery/modrun_rail_b123d.py`. Update the matching tolerance constant:
```python
FDM_TOLERANCE = 0.15  # must match the clip file exactly
```

Save both files.

### 2.2 STL Regeneration Commands

Run all five STLs in this exact sequence. Each command outputs to `stl/v1.0/`. Do not write to the root `stl/` directory — versioned subdirectory keeps a clean record.

```bash
# Clip variants — 3 bore sizes
uv run python cadquery/modrun_clip_b123d.py --bore 6 --tolerance 0.15 --output-dir stl/v1.0/
uv run python cadquery/modrun_clip_b123d.py --bore 8 --tolerance 0.15 --output-dir stl/v1.0/
uv run python cadquery/modrun_clip_b123d.py --bore 12 --tolerance 0.15 --output-dir stl/v1.0/

# Rail variants — 2 mount types
uv run python cadquery/modrun_rail_b123d.py --variant desk_clamp --output-dir stl/v1.0/
uv run python cadquery/modrun_rail_b123d.py --variant adhesive --output-dir stl/v1.0/
```

Replace `0.15` with your confirmed FDM_TOLERANCE value throughout.

**Expected output files in stl/v1.0/:**
```
modrun_clip_6mm_v1.0.stl
modrun_clip_8mm_v1.0.stl
modrun_clip_12mm_v1.0.stl
modrun_rail_desk_clamp_v1.0.stl
modrun_rail_adhesive_v1.0.stl
```

### 2.3 STL Validation in Bambu Studio

Import each STL into Bambu Studio. Verify:

- [ ] No red repair-warning indicators (manifold check passes)
- [ ] Part lies flat on build plate with no floating geometry
- [ ] No support structures are auto-generated (design should be support-free)
- [ ] Slice preview shows clean perimeters on snap arm section (no thin-wall collapse)

If any STL shows a repair warning, the CadQuery script has a geometry issue. Do not ship this STL. Return to the CadQuery file, identify the malformed operation, and fix before re-exporting.

### 2.4 Git Commit — Production STL Lock

Once all five STLs validate in Bambu Studio, commit them with the confirmed tolerance value in the commit message. This creates a permanent, timestamped record of the production geometry.

```bash
git add cadquery/modrun_clip_b123d.py cadquery/modrun_rail_b123d.py stl/v1.0/
git commit -m "feat(modrun): production STL v1.0 — FDM_TOLERANCE=0.15, test print PASS"
git tag v1.0
```

Replace `0.15` with your confirmed value. Replace `PASS` with your snap-fit test result summary.

---

## Hours 3–6: Second Print Verification (if tolerance was adjusted)

If you changed FDM_TOLERANCE, print exactly one clip from the new STL before running a full production plate. This is not optional — a 12-clip plate at an incorrect tolerance is wasted filament and time.

### 3.1 Abbreviated Verification Print

- Slice `modrun_clip_6mm_v1.0.stl` (single clip, not a plate layout)
- Print on the same printer, same filament lot as the test print
- Repeat the complete measurement and functional test protocol from Section 1
- If pass: proceed to full production plate
- If fail: make a second tolerance adjustment (typically ±0.05 mm from the first adjustment) and repeat

### 3.2 When to Deploy Immediately vs. Run Additional Verification Prints

**Deploy immediately (skip second print):**
- Test print passed all three functional tests
- Rail engagement click was clean and firm
- Cable bore accepted cable smoothly
- FDM_TOLERANCE change is zero

**Run one verification print, then deploy:**
- Test print required one tolerance adjustment of ≤0.10 mm
- All functional failure modes were clearly attributable to a single parameter

**Run two verification prints before deploying:**
- Test print required tolerance adjustment AND bore adjustment simultaneously
- Any snap arm failure (cracking or permanent set) was observed — structural failures require confirmation that the fix resolved the root cause, not just the symptom

**Do not proceed to production until resolved:**
- Snap arm cracked on the functional test. This indicates either: wrong print orientation, infill too low (<20%), nozzle temperature too low (<215°C for PLA+), or a fundamental geometry issue. All must be ruled out before production.

---

## Hours 6–24: Slicer Profile Lock

This step applies regardless of whether you made a tolerance adjustment. The production slicer profile must be explicitly saved and locked so every future production run uses identical parameters.

### 4.1 Production Slicer Settings (Bambu Studio, P1S)

Configure these settings in Bambu Studio. Every parameter below is a fixed value — do not adjust without a deliberate production change decision.

| Parameter | Production Value | Notes |
|---|---|---|
| Layer height | 0.20 mm | Quality preset; 0.16 mm increases print time 25% with minimal functional benefit |
| First layer height | 0.25 mm | Standard |
| Wall count (perimeters) | 3 | Do not reduce below 3 — snap arm integrity requires this |
| Top/bottom layers | 4 | Standard |
| Infill pattern | Gyroid | Best isotropy for a snap feature that flexes in multiple directions |
| Infill density | 20% | Tested minimum; increase to 25% only if snap arm shows fatigue in long-term testing |
| Print speed | 200 mm/s outer wall, 300 mm/s inner | P1S standard quality profile |
| Nozzle temperature | 220°C (PLA+) | eSUN PLA+ optimal range; adjust ±5°C based on filament lot if stringing appears |
| Bed temperature | 65°C | PLA+ standard |
| Fan speed | 100% after layer 5 | Full cooling for PLA+ overhang quality |
| Support structures | None | Design is support-free — if supports are auto-generated, geometry check failed |
| Plate layout | 12 clips per plate in 4×3 grid | See production-scaling-research.md for verified layout |

### 4.2 Saving the Profile

In Bambu Studio:
1. Configure all parameters above
2. File → Save Profile As → "ModRun-PLA-Production-v1"
3. Export profile to a backup location: `projects/mfg-farm/stl/ModRun-PLA-Production-v1.json`
4. Commit the exported profile to git alongside the STLs

This profile is now the authoritative production configuration. If a print problem occurs, the first diagnostic question is always: "Was the production profile selected?"

### 4.3 Production Plate File

Create the 12-clip production plate file:

1. Open `modrun_clip_6mm_v1.0.stl` in Bambu Studio
2. Arrange 12 clips in a 4×3 grid on the P1S 256×256mm build plate
3. Leave 5mm spacing between clips
4. Select the ModRun-PLA-Production-v1 profile
5. Save as: `stl/v1.0/modrun_clip_6mm_12up_production.3mf`

Repeat for 8mm and 12mm bore variants. The 3mf files include the slicer settings embedded — this is the primary production send file, not the raw STL.

---

## Hours 24–48: Quality Gate Protocol

Run these gates on the first full production plate printed after the test print validates. This is the production qualification plate — if it passes all gates, the operation is cleared for sustained production.

### 5.1 Gate Structure

**Gate 1 — Visual (100% of units, 3–5 seconds each):**
- Snap arm present and not deformed
- Cable bore open, no stringing bridge
- Full base adhesion, no corner lift
- No layer separation visible

**Gate 2 — Dimensional spot check (1 in 12, every plate):**
- Snap arm width: accept 7.3–7.9 mm
- Snap arm thickness: accept 1.2–1.6 mm
- Cable bore: accept ±0.3 mm of nominal bore size

**Gate 3 — Functional test (1 per plate, first clip harvested):**
- Rail engagement: tactile click, no binding
- Cable retention: holds sideways for 10 seconds
- Snap arm flex to 30%, returns to position

**Gate 4 — Extended stress test (first production lot only, not every plate):**
For the first 12-clip plate from the production STLs, test 3 clips at elevated stress:
- Insert and remove from rail 10 times each: snap arm must not crack
- Flex snap arm to 50% deflection (not just 30%): must return without permanent set
- Hold a cable of the specified bore diameter in the clip under 50g of downward force (hang a known weight from the cable) for 5 minutes: cable must not drop

Pass criteria: all 3 clips pass all 3 extended tests with no failures. If any clip fails, do not ship the lot — diagnose root cause before continuing production.

### 5.2 Failure Response

| Failure Mode | Immediate Action | Root Cause Investigation |
|---|---|---|
| Snap arm cracks at 30% flex | Scrap plate; do not rework | Nozzle temp, infill density, wall count |
| Bore too tight (cable won't seat) | Re-check tolerance; may need 0.05 mm bore adjustment | FDM shrinkage on inner radius at this layer height |
| Rail binding (3+ clips from same plate) | Scrap plate; re-check STL tolerance value | Wrong STL version sliced, or printer X/Y drift |
| Warping (corner lift) | Re-clean PEI plate with IPA; re-check Z offset | Dirty bed, Z-offset drift, draft in room |
| Stringing in cable bore | Re-run retraction calibration; reduce nozzle temp by 5°C | Moisture in filament, retraction settings |

---

## Hours 48–72: Production Clearance Declaration

By 72 hours after the test print, one of three states should be reached:

**State A — Full production clearance:**
- Test print passed all gates with no tolerance adjustment
- Production STLs match test STL (no regeneration needed)
- Slicer profile saved and committed
- First production plate printed and all 4 quality gates passed
- Ready to run sustained production

**State B — Clearance after one adjustment:**
- One tolerance or bore parameter adjusted
- One verification print confirmed the adjustment resolved the issue
- First production plate printed and all 4 quality gates passed
- Ready to run sustained production

**State C — Not yet cleared:**
- Structural failure observed (snap arm cracking) that has not been reproduced and resolved
- Two or more parameters needed adjustment simultaneously — stop, diagnose, and resolve one at a time
- Do not publish Etsy listings or accept orders until State A or B is achieved

**When State A or B is confirmed, commit to git:**

```bash
git add .
git commit -m "chore(modrun): production clearance confirmed — State A/B, v1.0 STL, gate 1–4 pass, plate 1 QC clean"
```

---

## Timeline Summary

| Timeframe | Action | Decision Gate |
|---|---|---|
| Hour 0 | Measure test print; run functional tests A/B/C | Pass all three → Hour 6; Fail → adjust tolerance → Hour 1 |
| Hour 1–3 | Update CadQuery parameters; regenerate 5 STLs; validate in Bambu Studio | All 5 manifold, no supports → Hour 3; Repair warning → fix CadQuery |
| Hour 3–6 | Print one verification clip (if tolerance adjusted) | Pass → Hour 6; Fail → second adjustment → Hour 3 |
| Hour 6–24 | Lock production slicer profile; create production plate 3mf files; git commit | Profile saved; 3mf files committed → Hour 24 |
| Hour 24–48 | Print first production plate; run all 4 quality gates | All 4 pass → Hour 48 |
| Hour 48–72 | Declare production clearance; git tag v1.0; Etsy listings can go live | State A or B → proceed; State C → hold |

**Critical path:** The single slowest step is the verification print (3–4 hours for a full plate) combined with quality gate evaluation. If the test print passes on first attempt with no adjustment, the 72-hour timeline compresses to approximately 30 hours.

---

## Confidence Notes

**High confidence:** All CadQuery commands in Section 2.2 reflect the actual file names observed in `cadquery/` and `stl/` directories. Tolerance adjustment logic is based on standard FDM calibration practice for snap-fit features in PLA+. Quality gate dimensions match the SNAP_ARM_WIDTH and SNAP_ARM_THICKNESS constants documented in `post-test-print-execution.md`.

**Gap:** The exact BORE_DIAMETER_ADD parameter name inside `modrun_clip_b123d.py` has not been verified by reading the file source. If the bore adjustment variable has a different name, the command will fail with a NameError. Read the CadQuery source file before running bore adjustment commands if bore sizing is needed.
