---
title: Snap-Arm CAD Modification Procedures — Parameter-Based Edits
project: mfg-farm
date: 2026-06-28
status: pre-staged for post-test-print execution
cad_file: projects/mfg-farm/cadquery/modrun_clip_b123d.py
related:
  - TEST_PRINT_CONTINGENCY_DECISION_TREE.md
  - MATERIAL_SUBSTITUTION_PROTOCOL.md
confidence: 90%
---

# Snap-Arm CAD Modification Procedures

**Purpose**: Pre-staged parameter edits for the three most likely snap-arm failure modes.
Each procedure is a single-number change to `modrun_clip_b123d.py`. No redesign required.
Estimated edit time: 30 seconds. STL regeneration: ~10-20 seconds. Total to re-slice: under
2 minutes. Print time: 6-8 hours (unchanged).

**CAD file location**: `projects/mfg-farm/cadquery/modrun_clip_b123d.py`

**Parameter block location**: Lines 26-45 of `modrun_clip_b123d.py` — the
`# Geometry constants` block at the top of the file. All snap-arm parameters are defined
here. No function-body edits are needed.

**Entry point**: Use `TEST_PRINT_CONTINGENCY_DECISION_TREE.md` to determine which section
to execute. Do not guess — measure first, then come here.

---

## Section A: Snap-Arm Too Tight

**Trigger**: `T_mid < 1.25 mm` from decision tree measurement.

**Root cause in print**: The arm printed thinner than designed. This is most often a slicer
issue (fewer than 3 walls, layer height > 0.20 mm, or under-extrusion flow rate <95%).
Before editing the CAD parameter, verify slicer settings are correct — a slicer fix alone
may resolve this without any CAD change.

**Slicer check first (5 minutes)**:
1. Open Bambu Studio, load the existing STL
2. Confirm: Layer height = 0.20 mm, Walls = 3, Flow rate = 100%, Nozzle = 0.4 mm
3. Slice preview: does the snap-arm show 3 perimeter rings? If not, increase wall count
4. If slicer was already correct: proceed to parameter edit below

**Parameter edit**:

File: `projects/mfg-farm/cadquery/modrun_clip_b123d.py`
Line: 41
Current: `SNAP_ARM_THICKNESS = 1.4    # mm — arm thickness; thinner = more flexible`
Change to: `SNAP_ARM_THICKNESS = 1.5    # mm — arm thickness; thinner = more flexible`

This is the only change. Do not modify any other parameter.

**Effect of this change**:
- Arm increases from 1.4 → 1.5 mm (7% thicker)
- Flexural stiffness increases approximately 15% (stiffness scales with thickness cubed: (1.5/1.4)^3 = 1.23)
- Grip force on cable increases proportionally — this is desirable if the arm was under-built
- No change to SNAP_NUB_HEIGHT, SNAP_ARM_LENGTH, or any slot/bore parameter
- Rail slot compatibility: unchanged (arm width `SLOT_WIDTH - 0.4` is unaffected by thickness)
- Thermal impact: none — same print temp, same material

**STL regeneration command**:

```bash
cd projects/mfg-farm
uv run python cadquery/modrun_clip_b123d.py --bore 6 --output-dir stl/
```

Run for all bore sizes if producing the full set:

```bash
uv run python cadquery/modrun_clip_b123d.py --output-dir stl/
```

This overwrites `stl/modrun_clip_3mm.stl`, `stl/modrun_clip_6mm.stl`, `stl/modrun_clip_12mm.stl`.

**Re-slice and print**:
1. Open Bambu Studio
2. File → Import → select the updated STL (e.g., `modrun_clip_6mm.stl`)
3. Confirm print settings: 0.20 mm layer height, PLA+, 3 walls, 220-225°C, 50 mm/s
4. Start print
5. Print time: 6-8 hours (same as original)

**Functional validation after reprint**:
- Measure `T_mid` again — should be 1.45-1.60 mm (target 1.5 mm ± print tolerance ~0.05 mm)
- Flex test: arm bends smoothly without cracking under 2N force
- Seat test: insert clip into 6 mm deep rail slot mockup — audible click at full seating
- If still too tight (T_mid still below 1.35 mm): increase to `SNAP_ARM_THICKNESS = 1.6` and repeat

**Note on arm cracking during Section A**: If the arm cracked in the original print, increasing
thickness is not the only fix. Cracking at 1.4 mm may indicate PLA+ is too brittle at this
geometry — see `MATERIAL_SUBSTITUTION_PROTOCOL.md` before assuming more thickness solves it.

---

## Section B: Snap-Arm Too Loose

**Trigger**: `T_mid > 1.55 mm` from decision tree measurement, AND cable slips from clip under
lateral pull, OR snap-arm seats without audible click.

**Root cause in print**: Over-extrusion or elephant foot artifact caused the arm to print thicker
than designed. The extra thickness reduces flexibility — the arm cannot deflect far enough to
let the nub engage the slot edge properly, so the clip does not lock.

**Slicer check first (5 minutes)**:
1. Confirm flow rate = 100% (not 105% or higher — a common "improve adhesion" tweak)
2. Confirm first-layer height = 0.20 mm (not 0.25 mm "initial layer" setting)
3. Confirm live-adjust Z-offset was not set too negative (over-squish causes elephant foot)
4. If any of the above were non-standard: correct slicer settings and reprint before CAD change

**Parameter edit**:

File: `projects/mfg-farm/cadquery/modrun_clip_b123d.py`
Line: 41
Current: `SNAP_ARM_THICKNESS = 1.4    # mm — arm thickness; thinner = more flexible`
Change to: `SNAP_ARM_THICKNESS = 1.3    # mm — arm thickness; thinner = more flexible`

This is the only change. Do not modify any other parameter.

**Effect of this change**:
- Arm reduces from 1.4 → 1.3 mm (7% thinner)
- Flexural stiffness decreases approximately 19% — arm becomes more flexible
- Snap engagement improves: arm can deflect to let nub seat, then spring back to lock
- Grip force on cable: slightly reduced. Run cable pull test after reprint (see validation)
- No change to SNAP_NUB_HEIGHT, SNAP_ARM_LENGTH, or any slot/bore parameter
- Thermal impact: none

**STL regeneration command**: identical to Section A above.

```bash
cd projects/mfg-farm
uv run python cadquery/modrun_clip_b123d.py --output-dir stl/
```

**Re-slice and print**: identical to Section A above. Same settings.

**Functional validation after reprint**:
- Measure `T_mid` — should be 1.25-1.40 mm (target 1.3 mm ± print tolerance ~0.05 mm)
- Seat test: insert clip into slot — audible click confirms nub engagement
- Cable pull test: route a USB-C cable through 6 mm bore clip. Tug laterally with ~2N force.
  Cable should not slip free. If it does, nub height is insufficient.
- If cable slips after Section B reprint: increase `SNAP_NUB_HEIGHT` from 1.2 → 1.4 mm (see
  Note below), do NOT reduce arm thickness further

**Section B Note — SNAP_NUB_HEIGHT adjustment**:
If arm deflects and seats (click heard) but cable still slips, the nub is too small to retain.

File: `projects/mfg-farm/cadquery/modrun_clip_b123d.py`
Line: 43
Current: `SNAP_NUB_HEIGHT = 1.2       # mm — locking nub protrusion`
Change to: `SNAP_NUB_HEIGHT = 1.4       # mm — locking nub protrusion`

This can be combined with the Section B thickness change or applied independently on a third
iteration. Regenerate STL and reprint after any parameter change.

---

## Section C: Material Failure — No Parameter Edit; Route to Material Substitution

**Trigger**: Arm cracks, delaminates, or shows brittleness under functional test, regardless
of dimensional measurement being within spec.

**No CAD parameter changes for material failure.** The geometry is correct; the material
or print temperature is the issue.

**Primary route**: Correct print temperature first.
- PLA+: must print at 220-225°C. Printing at 215°C or below causes inter-layer brittleness.
  Printing at 230°C or above causes slight sagging in thin features.
- If temperature was non-standard: correct and reprint with same CAD parameters

**If temperature correction does not resolve brittleness**: execute
`MATERIAL_SUBSTITUTION_PROTOCOL.md`. Do not change SNAP_ARM_THICKNESS or any other
parameter simultaneously with a material change — you will lose the ability to determine
which variable resolved the failure.

---

## Parameter Reference Table

All snap-arm parameters in `modrun_clip_b123d.py`, with their lines and the full set of
pre-approved adjustment values:

| Parameter | Line | Default | Too Tight | Too Loose | Notes |
|---|---|---|---|---|---|
| `SNAP_ARM_THICKNESS` | 41 | 1.4 mm | 1.5 mm | 1.3 mm | Primary tolerance control |
| `SNAP_ARM_LENGTH` | 40 | 8.0 mm | do not change | do not change | Changes slot engagement depth |
| `SNAP_ARM_WIDTH` | 42 | `SLOT_WIDTH - 0.4` | do not change | do not change | Controls slot side clearance |
| `SNAP_NUB_HEIGHT` | 43 | 1.2 mm | 1.0 mm | 1.4 mm | Adjust only if grip fails after arm fix |
| `SNAP_NUB_LEAD_ANGLE` | 44 | 35 deg | do not change | do not change | Chamfer for insertion ease |
| `SNAP_NUB_LOCK_ANGLE` | 45 | 80 deg | do not change | do not change | Near-vertical retention face |
| `FDM_TOLERANCE` | 29 | 0.15 mm | do not change | do not change | Rail-slot interface only |

**Parameters not to touch in iteration 1-2**: `SNAP_ARM_LENGTH`, `SNAP_ARM_WIDTH`,
`SNAP_NUB_LEAD_ANGLE`, `SNAP_NUB_LOCK_ANGLE`. These control rail interface geometry and
insertion physics — changing them without a new rail test print adds uncontrolled variables.

---

## Iteration Tracking

Record each iteration to avoid re-solving the same problem:

| Iteration | SNAP_ARM_THICKNESS | SNAP_NUB_HEIGHT | Print temp | Result | Next action |
|---|---|---|---|---|---|
| 1 (test print) | 1.4 mm | 1.2 mm | ___°C | __________ | __________ |
| 2 | | | | | |
| 3 | | | | | |

**Convergence expectation**: Most printers reach a stable snap-arm geometry within 2 iterations.
If 3 iterations have not produced a passing print, route to `MATERIAL_SUBSTITUTION_PROTOCOL.md`
before continuing CAD iteration — the issue is likely material, not geometry.

---

**Cross-references**:
- Decision tree (which section to execute): `TEST_PRINT_CONTINGENCY_DECISION_TREE.md`
- Material swap procedure: `MATERIAL_SUBSTITUTION_PROTOCOL.md`
- Mechanical property comparison (PLA+ vs PETG stiffness): `FDM_MATERIAL_CAPABILITY_MATRIX.md`
