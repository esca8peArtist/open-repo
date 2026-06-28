---
title: Test Print Contingency Decision Tree — Snap-Arm Tolerance
project: mfg-farm
date: 2026-06-28
status: pre-staged (execute immediately upon test print completion)
cad_file: projects/mfg-farm/cadquery/modrun_clip_b123d.py
related:
  - SNAP_ARM_CAD_MODIFICATION_PROCEDURES.md
  - MATERIAL_SUBSTITUTION_PROTOCOL.md
  - TEST_PRINT_CONTINGENCY_PLAYBOOK.md
  - FDM_MATERIAL_CAPABILITY_MATRIX.md
target_parameter: SNAP_ARM_THICKNESS = 1.4mm (line 41 of modrun_clip_b123d.py)
confidence: 88%
---

# Test Print Contingency Decision Tree — Snap-Arm Tolerance

**Purpose**: Provide an instant routing flowchart the moment the test print completes.
Snap-arm tolerance (1.4 mm gap, line 41 of `modrun_clip_b123d.py`) is the highest-risk
feature in the ModRun cable clip. This document routes every foreseeable outcome to a
pre-staged fix procedure — no re-planning required, no 2-3 day paralysis.

**How to use**: Hold digital calipers against the completed print. Measure the snap-arm
thickness at three points (base, midpoint, free end). Cross-reference with the thresholds
below. Follow the arrow to the correct modification path.

---

## Step 0: Measurement Protocol

Before routing, take three measurements:

| Measurement point | How to measure | Record as |
|---|---|---|
| Snap-arm base thickness | Calipers perpendicular to arm, at root where arm meets body | `T_base` |
| Snap-arm midpoint thickness | Same, at center of the 8 mm cantilever length | `T_mid` |
| Snap-arm tip thickness | Same, at free end (near nub base) | `T_tip` |

Use `T_mid` as the governing value for routing. If `T_base` and `T_tip` diverge by more
than 0.15 mm from `T_mid`, flag this as a **printing artifact** (elephant foot / nozzle
over-pressure) before routing to a CAD fix.

---

## Step 1: Top-Level Route

```
Test print completed.
Measure snap-arm (calipers). Record T_mid.

         T_mid < 1.25 mm?
              │
              YES ──→ ROUTE A: Snap-Arm Too Tight (increase gap)
              │        See Section A below
              NO
              │
         T_mid > 1.55 mm?
              │
              YES ──→ ROUTE B: Snap-Arm Too Loose (reduce gap)
              │        See Section B below
              NO
              │
         1.25 ≤ T_mid ≤ 1.55 mm (within spec)?
              │
              YES → PASS CRITERIA CHECK (Section C)
              │
              Continue to functional tests:
              - Arm bends without cracking?
              - Cable doesn't slip under normal routing force?
              - Nub seats into rail slot audibly?
              │
              All YES ──→ PASS — proceed to production (no CAD changes)
              Any NO ──→ ROUTE C: Material Thermal Failure
                          See Section C below
```

---

## Section A: Snap-Arm Too Tight

**Symptom**: `T_mid < 1.25 mm`. The arm printed thinner than designed. When you press the
clip into the rail slot, the snap-arm engages before the clip is fully seated, or the arm
cracks under even light flex pressure.

**Why this happens**: FDM under-extrusion, slicer perimeter count below 3, or incorrect
layer height (e.g., 0.24 mm instead of 0.20 mm) causes thin walls to under-build.

**Functional test to confirm failure mode**:
- Press clip into a mockup of the rail slot (or a 6 mm deep gap)
- If snap-arm binds before flush seating: confirmed
- If arm cracks on first flex: severity elevated — see ROUTE C escalation flag below

**Action**: Execute `SNAP_ARM_CAD_MODIFICATION_PROCEDURES.md — Section A`.
- Parameter change: `SNAP_ARM_THICKNESS: 1.4 → 1.5` (adds 0.1 mm wall, increases stiffness by ~15%)
- Slicer check first: confirm 3 walls, 0.20 mm layer height, 0.4 mm nozzle — slicer issue
  may be the root cause; fix slicer before regenerating STL
- Re-generate STL, re-slice, re-print
- Timeline to next print: 6-8 hours

**Escalation flag**: If arm cracked during any flex test (not just binding), treat as potential
material failure. Execute ROUTE C analysis before modifying SNAP_ARM_THICKNESS.

---

## Section B: Snap-Arm Too Loose

**Symptom**: `T_mid > 1.55 mm`. The arm printed thicker than designed. The clip seats into
the rail slot but the snap-arm engages weakly or not at all — cable can be pulled free
without the nub resisting.

**Why this happens**: Over-extrusion (flow rate >100%), elephant foot from first-layer
squish, or filament that is slightly oversized (1.80 mm vs 1.75 mm nominal).

**Functional test to confirm failure mode**:
- Press clip into rail slot — does it slide in without audible snap?
- Apply lateral cable-routing force — does cable slip out of the clip?
- Check nub engagement: does the nub visibly seat below the slot edge?

**Action**: Execute `SNAP_ARM_CAD_MODIFICATION_PROCEDURES.md — Section B`.
- Parameter change: `SNAP_ARM_THICKNESS: 1.4 → 1.3` (reduces wall, increases flexibility)
- Also check: `SNAP_NUB_HEIGHT` — if nub is undersized due to over-extrusion artifact,
  may need to adjust separately (see SNAP_ARM_CAD_MODIFICATION_PROCEDURES.md — Section B Note)
- Re-generate STL, re-slice, re-print
- Timeline to next print: 6-8 hours

**Functional validation after reprint**: Cable grip test — 2N lateral force (hand-tug on a
USB-C cable should not dislodge clip). If cable still slips: increase `SNAP_NUB_HEIGHT`
from 1.2 to 1.4 mm before third iteration.

---

## Section C: Material Thermal Failure (Pass Criteria Not Met)

**Symptom**: Dimensional measurement is within spec (1.25–1.55 mm) BUT arm cracks, delaminates,
or shows visible brittleness under even light flex. Or: print shows warping at base, layer
separation visible under magnification, surface glossy instead of matte (overheated).

**Failure modes**:

| Observation | Most likely cause | Route |
|---|---|---|
| Arm snaps on first flex, clean fracture | PLA+ printed too hot (>225°C); layers fused but inter-layer bonding brittle | C1: Temperature correction |
| Arm separates along layer lines, surface rough | PLA+ printed too cold (<218°C); layers didn't bond | C2: Temperature correction |
| Base of print warped, corners lifted | Bed adhesion failure; thermal stress at base | C3: Bed and first-layer fix |
| Arm surface glossy, slightly sagged | Overheat; PLA+ at 230°C+ loses shape retention | C4: Temperature correction |
| All corrections tried, arm still brittle | PLA+ formulation incompatible with this snap geometry | C5: Material substitution |

**For C1-C4**: Correct temperature/bed settings and reprint before any CAD changes.
The geometry is correct; the print settings are not.

**For C5 (material substitution)**: Execute `MATERIAL_SUBSTITUTION_PROTOCOL.md`.
- Primary pivot: PETG at 245-250°C
- Secondary: ABS at 240-250°C (requires heated bed + enclosure)
- Do not execute CAD changes simultaneously with material change — isolate variables

---

## Pass Criteria Summary

The test print passes when ALL of the following are true:

| Criterion | Pass | Measurement method |
|---|---|---|
| Snap-arm thickness | 1.25–1.55 mm at midpoint | Digital calipers |
| Arm flexes without cracking | No cracks, no delamination under 2N flex force | Manual flex test |
| Cable doesn't slip | 2N lateral tug on USB-C cable — clip stays engaged | Hand-pull test |
| Nub seats audibly | Audible click when clip pressed into 6 mm deep slot | Seat into slot |
| No warping at base | Base is flat within ±0.5 mm (feeler gauge or visual) | Visual + caliper |
| No layer separation | Surface is uniform, no visible gaps between layers | Visual inspection |

If all 6 pass: proceed directly to production. No CAD changes needed.

If any fail: route to Section A, B, or C above. Execute the corresponding pre-staged
modification procedure before reprinting.

---

## Quick Reference (Post-Print 60-Second Route)

```
Measure T_mid with calipers.

< 1.25 mm  ──→  SNAP_ARM_CAD_MODIFICATION_PROCEDURES.md Section A (increase SNAP_ARM_THICKNESS)
1.25–1.55  ──→  Run functional tests (flex, cable pull, seat test)
                All pass?  YES → DONE, go to production
                Any fail?  NO  → MATERIAL_SUBSTITUTION_PROTOCOL.md
> 1.55 mm  ──→  SNAP_ARM_CAD_MODIFICATION_PROCEDURES.md Section B (reduce SNAP_ARM_THICKNESS)
```

---

**Cross-references**:
- CAD parameter locations: `SNAP_ARM_CAD_MODIFICATION_PROCEDURES.md`
- Material swap procedure: `MATERIAL_SUBSTITUTION_PROTOCOL.md`
- Broader failure modes (jaw gap, bore, layer separation): `TEST_PRINT_CONTINGENCY_PLAYBOOK.md`
- Material mechanical properties table: `FDM_MATERIAL_CAPABILITY_MATRIX.md`
