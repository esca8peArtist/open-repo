---
title: Test Print Failure Recovery Plan
project: mfg-farm
created: 2026-05-15
scope: Contingency procedures if test print fails; enables rapid design iteration
version: 1.0
---

# Test Print Failure Recovery Plan

**Purpose**: If the ModRun cable clip test print shows issues, this document provides rapid diagnostics and recovery procedures.

**Test print specifications** (baseline):
- Layer height: 0.20 mm
- Material: PLA+
- Wall count: 3
- Nozzle temp: 220–225°C
- Print time: ~90 min per unit

---

## 1. Post-Print Inspection Checklist

**Immediately after print completes (while part is still warm)**:

### 1.1 Visual Inspection (5 min)

- [ ] **Snap-arm integrity**: No cracks, splits, or white stress marks visible?
  - ✓ Clean: proceed to 1.2
  - ✗ Cracked: record location, photograph (zoom), proceed to Section 2 (Snap-Arm Failure)
  - ✗ Stress marks (white): may fail after a few cycles; photograph, proceed to Section 2

- [ ] **Rail grip surfaces**: No layer separation, no rough edges?
  - ✓ Clean: proceed to 1.2
  - ✗ Rough/separated: photograph, proceed to Section 3 (Grip Surface Failure)

- [ ] **Cable post**: Smooth, no wobble, no cracks?
  - ✓ Clean: proceed to 1.2
  - ✗ Wobbles: measure with calipers, proceed to Section 4 (Post Wobble)
  - ✗ Cracks: photograph, proceed to Section 2 (Snap-Arm Failure)

- [ ] **Overall dimensions**: Does it look roughly the same size as the CAD preview?
  - ✓ Yes: proceed to 1.2
  - ✗ Noticeably oversized/undersized: proceed to Section 5 (Scale/Shrinkage Issue)

### 1.2 Dimensional Verification (10 min)

**Required tools**: Digital calipers (±0.1 mm), ruler, computer with `modrun_clip.py` open

**Measure these dimensions**:

| Dimension | CAD Spec | Tolerance | Measured | Status |
|-----------|----------|-----------|----------|--------|
| Snap-arm length | 16.2 mm | ±0.2 | _____ | □ |
| Snap-arm thickness | 1.4 mm (CRITICAL) | ±0.15 | _____ | □ |
| Rail jaw opening | 7.8–8.2 mm | var | _____ | □ |
| Cable post diameter | 8.0 mm | ±0.3 | _____ | □ |
| Cable post height | 12.0 mm | ±0.2 | _____ | □ |
| Overall width | 14.0 mm | ±0.3 | _____ | □ |

**Snap-arm thickness is CRITICAL**: This 1.4 mm feature is the highest-risk tolerance. If measured <1.25 mm or >1.55 mm, the design needs iteration (see Section 2).

### 1.3 Functional Tests (15 min)

**Test 1: Snap-arm flex**
```
1. Hold clip in vise (or with one hand)
2. Press snap-arm tip downward gently with thumb
3. Observe: does it flex smoothly and return?
   ✓ Yes, smooth flex: snap-arm is likely viable
   ✗ No flex / cracks while testing: snap-arm failure (Section 2)
   ✗ Feels brittle: material/temperature issue (Section 6)
```

**Test 2: Rail grip (dry test)**
```
1. Slide clip onto actual ModRun rail (or test coupon)
2. Grasp firmly and pull horizontally (no cable yet)
3. Observe grip stability:
   ✓ Holds position, no slipping: grip is viable
   ✗ Slips on pull: grip surface too smooth (Section 3)
   ✗ Won't fit at all: dimensions wrong (Section 5)
```

**Test 3: Cable post stability**
```
1. Wrap 6mm cable (or rope) around post 1.5 turns
2. Pull cable with moderate force (not yanking)
3. Observe:
   ✓ Post stays straight, no wobble: viable
   ✗ Post deflects >2mm: wobble issue (Section 4)
   ✗ Cable slips: post surface too smooth (Section 3)
```

### 1.4 Documentation (5 min)

**Take photos of**:
- Part in hand (scale reference)
- Snap-arm detail (zoom, show any cracks/stress marks)
- Rail grip surface
- Cable post from side
- Cable post from top
- Any failure areas (close-up with dimension labels if possible)

**Record in file**: `projects/mfg-farm/test-print-results.md`
```
# Test Print Results — [DATE]

## Visual Inspection
[Summary: OK / Issues found]

## Dimensions
[Copy table from 1.2, fill measured values]

## Functional Tests
[Summary: All pass / Failures: snap-arm / grip / post / scale]

## Photographs
[List file paths]

## Next Action
[Proceed to Section ___ below]
```

---

## 2. Snap-Arm Failure Recovery

**Symptoms**: Cracks, stress marks, brittleness, measured thickness outside ±0.15 mm

**Root causes**:
- A: Insufficient wall count (too thin, under-extruded)
- B: Nozzle temperature too high (material degraded)
- C: Print speed too fast (insufficient layer fusion)
- D: Snap-arm tolerance too aggressive for material
- E: Design geometry has stress concentration

### Recovery Procedure

**Step 1: Diagnose (10 min)**

```
Q1: Where is the crack / stress mark?
  [ ] Across the snap-arm thickness (vertical crack)
    → Likely A or C (wall/fusion issue)
  [ ] Along the snap-arm length (horizontal crack)
    → Likely D (tolerance too tight)
  [ ] At the snap-arm root (where it connects to body)
    → Likely E (stress concentration)

Q2: Did the part feel brittle when you bent it?
  [ ] Yes (bent and cracked immediately, no flex)
    → Likely B (temperature damage) or E (design issue)
  [ ] No (flexed before cracking)
    → Likely A, C, or D (manufacturing tolerance)

Q3: Measured snap-arm thickness:
  [ ] < 1.25 mm (too thin)
    → Likely A (under-extrusion) or C (too fast)
  [ ] 1.25–1.55 mm (in spec)
    → Likely E (design geometry) or B (material)
  [ ] > 1.55 mm (too thick)
    → Material expanded; unusual but possible
```

**Step 2: Implement Fix (as applies)**

**If A (under-extrusion)**:
- [ ] Verify nozzle is clean (no jams)
- [ ] Run calibration print (20mm cube, visual check)
- [ ] If under-extruded: adjust flow rate +3% in slicer
- [ ] Re-slice and print Iteration 2 (see timeline below)

**If B (temperature damage)**:
- [ ] Reduce nozzle temperature to 215°C
- [ ] Re-slice and print Iteration 2

**If C (too fast)**:
- [ ] Reduce print speed by 10% in slicer (from ~60 mm/s to 54 mm/s)
- [ ] Re-slice and print Iteration 2

**If D (tolerance too tight)**:
- [ ] Edit `modrun_clip.py`, increase snap-arm thickness multiplier
  - Current: 1.4 mm
  - Iteration 2: 1.6 mm (optional: start at 1.5 mm for conservative test)
- [ ] Regenerate STL: `python modrun_clip.py --output modrun_clip_v2.stl`
- [ ] Re-slice and print Iteration 2

**If E (design geometry/stress concentration)**:
- [ ] Review CAD: is there a sharp corner at snap-arm root?
- [ ] If yes: edit `modrun_clip.py` to add fillet radius (0.2–0.3 mm at root)
- [ ] Regenerate STL with fillet
- [ ] Also increase snap-arm thickness to 1.6 mm as reinforcement
- [ ] Re-slice and print Iteration 2

### Iteration 2 Timeline

| Action | Owner | Time | Deadline |
|--------|-------|------|----------|
| Implement fix (from Step 2) | You | 10 min | Next morning |
| Generate new STL | You | 5 min | Next morning |
| Slice in Bambu Studio | You | 10 min | Next morning |
| Print Iteration 2 (90 min active, ~3 hr cooling) | Printer | 4 hours | Morning + afternoon |
| Inspect & test Iteration 2 (Section 1) | You | 30 min | Evening |
| Decision: PASS / iterate again | You | 5 min | Evening |

**Iteration 2 success criteria**:
- ✓ Snap-arm thickness 1.4–1.6 mm (or new tolerance)
- ✓ No visible cracks or stress marks
- ✓ Flexes smoothly without cracking (functional test)
- ✓ No brittleness

If Iteration 2 fails: escalate (see Section 7: Multi-Iteration Failure Recovery)

---

## 3. Grip Surface Failure Recovery

**Symptoms**: Layer separation, rough edges on rail-contact surfaces, filament whiskers, poor grip

**Root causes**:
- A: Print speed too fast (insufficient extrusion/layer adhesion)
- B: Surface finish design (need texture, not smooth)
- C: Layer height too high (0.20 mm is pushing it, especially on thin walls)
- D: First layer poorly squished (bed leveling off)

### Recovery Procedure

**Step 1: Diagnose (10 min)**

```
Q1: What does the grip surface look like?
  [ ] Smooth, no texture, hard to grip
    → Likely B (need texture)
  [ ] Rough/whiskers, but functional
    → Likely A (print speed) — may be acceptable as-is
  [ ] Layer separation visible (layers peeling apart)
    → Likely A or C (adhesion issue)
  [ ] Large blobs/underextrusion
    → Likely C (layer height) or D (bed level)

Q2: Does the clip slide easily on the rail?
  [ ] Yes, too easily (friction <50%)
    → Likely B (smooth surface) or A (under-extruded)
  [ ] No, grips well but rough
    → May be acceptable; decide in Step 2

Q3: Can you see layer lines on the grip surface?
  [ ] Yes, clear horizontal lines 0.2 mm apart
    → Likely C (layer height too high) or B (no texture)
  [ ] No, layers blended
    → Likely good, may just need texture
```

**Step 2: Implement Fix (as applies)**

**If A (print speed / extrusion)**:
- [ ] Increase extrusion multiplier: flow +2% in slicer
- [ ] Reduce print speed: 60 → 50 mm/s (outer walls especially)
- [ ] Re-slice and print Iteration 2

**If B (surface texture needed)**:
- [ ] Decision: Is smooth surface acceptable for now?
  - If yes: Accept as-is, proceed to next failure section
  - If no: edit `modrun_clip.py` to add surface texture
    - Option 1: Knurled pattern (0.1 mm deep, 0.3 mm pitch)
    - Option 2: Vertical fins (0.5 mm tall)
    - Option 3: Sandblast sim (roughness parameter in model)
- [ ] Generate new STL with texture
- [ ] Re-slice and print Iteration 2

**If C (layer height too high)**:
- [ ] Reduce layer height: 0.20 → 0.15 mm (conservative)
  - This will increase print time ~30%, but improves surface quality
- [ ] Re-slice with 0.15 mm layer height
- [ ] Print Iteration 2

**If D (bed leveling)**:
- [ ] Run bed-level calibration: follow printer manual
- [ ] Re-slice and print Iteration 2

### Iteration 2 Timeline

Same as Section 2 (snap-arm failure): 4 hours total, next day result

**Iteration 2 success criteria**:
- ✓ Grip surface smooth or textured (design choice)
- ✓ No layer separation
- ✓ Clip grips rail with firm friction (functional test)
- ✓ No peeling/delamination

---

## 4. Cable Post Wobble Recovery

**Symptoms**: Post deflects >2 mm when cable is pulled, bends instead of staying straight

**Root causes**:
- A: Post diameter too small (design tolerance error)
- B: Wall thickness around post too thin (insufficient lateral support)
- C: Print speed too fast (insufficient infill density / layer fusion)
- D: Infill density too low (set at 25%, may need 30%+)

### Recovery Procedure

**Step 1: Diagnose (10 min)**

```
Q1: Measure post diameter with calipers
  [ ] <7.7 mm (too small)
    → Likely A (design error)
  [ ] 7.7–8.3 mm (in spec)
    → Likely B, C, or D (printing or infill issue)
  [ ] >8.3 mm (too large)
    → Unusual; possible over-extrusion (A secondary)

Q2: How much deflection under cable tension?
  [ ] <1 mm (acceptable, slight flex normal)
    → Likely acceptable; proceed
  [ ] 1–2 mm (borderline)
    → Fix if possible; test in production anyway
  [ ] 2–5 mm (too much)
    → Must fix (Section 2 recovery)

Q3: Does the post feel hollow / weak?
  [ ] No, solid (good resistance to finger pressure)
    → Likely C or D (printing)
  [ ] Yes, squishy (fails to your thumb pressure)
    → Likely B (too thin walls) or D (low infill)
```

**Step 2: Implement Fix (as applies)**

**If A (post diameter too small)**:
- [ ] Edit `modrun_clip.py`: increase cable_post_diameter
  - Current: 8.0 mm
  - Iteration 2: 8.5 mm (conservative)
- [ ] Regenerate STL
- [ ] Re-slice and print Iteration 2

**If B (walls too thin around post)**:
- [ ] Edit `modrun_clip.py`: increase wall_thickness_post
  - Current: 1.5 mm walls
  - Iteration 2: 2.0 mm walls around post only
- [ ] Regenerate STL
- [ ] Re-slice and print Iteration 2

**If C (print speed)**:
- [ ] Reduce print speed for infill: 60 → 50 mm/s
- [ ] Also reduce perimeter speed: 50 → 40 mm/s (walls)
- [ ] Re-slice with slower speeds
- [ ] Print Iteration 2

**If D (infill density too low)**:
- [ ] Increase infill density: 25% → 30% in slicer
  - This increases material cost ~20% but adds structural support
- [ ] Re-slice and print Iteration 2

### Iteration 2 Timeline

4 hours, same as above sections

**Iteration 2 success criteria**:
- ✓ Post diameter 8.0–8.5 mm
- ✓ Deflection <1.5 mm under cable pull
- ✓ Post feels solid, not squishy
- ✓ Cable doesn't slip on post

---

## 5. Scale / Shrinkage Issue Recovery

**Symptoms**: Part is noticeably larger or smaller than expected, doesn't fit on rail

**Root causes**:
- A: Slicer scale setting wrong (accidentally exported at 2× or 0.5×)
- B: Material shrinkage (PLA+ shrinks ~0.3–0.5% on cooling)
- C: Printer bed temperature too high (over-expansion during print)
- D: STL coordinate system mismatch (exported in different units)

### Recovery Procedure

**Step 1: Quick Check (5 min)**

```
Q1: Measure overall width (should be ~14.0 mm)
  [ ] 14.0 ± 0.3 mm (correct)
    → Scale likely OK; issue is elsewhere
  [ ] <13 mm (too small)
    → Likely B or C (shrinkage/cooling)
  [ ] >15 mm (too large)
    → Likely A or D (export/file error)

Q2: Compare to a known good part
  [ ] Have ModRun clip from earlier batches? Compare side-by-side
  [ ] If Iteration 1 is 30% smaller, likely A (export error)
  [ ] If Iteration 1 is 0.5% smaller, likely B (normal shrinkage)
```

**Step 2: Implement Fix (as applies)**

**If A (slicer scale error)**:
- [ ] Open Bambu Studio
- [ ] Import modrun_clip.stl
- [ ] Right-click, select "Scale"
- [ ] Verify scale is 1.0 (100%)
- [ ] If not: set to 1.0, re-export
- [ ] Re-slice and print Iteration 2

**If B (normal shrinkage)**:
- [ ] This is normal for PLA+
- [ ] If dimensions still functional: accept as-is
- [ ] If dimensions critical: edit `modrun_clip.py` to scale model +0.5%
  - Increase all dimensions by 1.005× multiplier
- [ ] Re-generate STL and print

**If C (bed temperature over-expansion)**:
- [ ] Check printer bed temp: should be 60–65°C for PLA+
- [ ] If >70°C: reduce to 60°C
- [ ] Let bed cool fully before re-print
- [ ] Re-slice and print Iteration 2

**If D (file/export error)**:
- [ ] Regenerate STL from `modrun_clip.py` directly
  - Check: `python modrun_clip.py --check-scale` (if supported)
  - Or: inspect STL file for unit declarations (should be mm)
- [ ] Re-slice from fresh STL
- [ ] Print Iteration 2

### Iteration 2 Timeline

If A (export error): 30 min fix + 4 hours print
If B (shrinkage): decide now (accept or iterate)
If C/D: 4 hours print, next day

---

## 6. Material / Temperature Issue Recovery

**Symptoms**: Part feels brittle, snaps easily, has no flexibility, visible burn marks/discoloration

**Root causes**:
- A: Nozzle temperature too high (material degraded, burnt)
- B: Filament wet or contaminated (moisture in material)
- C: Material batch mismatch (Iteration 1 vs. different PLA+ supplier)
- D: Cooling too fast (no time for crystallization)

### Recovery Procedure

**Step 1: Quick Check (5 min)**

```
Q1: Visual inspection of the part
  [ ] Dark brown/black spots or discoloration
    → Likely A (burnt material)
  [ ] Normal color but brittle
    → Likely B (wet filament) or C (batch mismatch)
  [ ] Color mismatch vs. expected
    → Likely C (different supplier/batch)

Q2: Is filament spool showing moisture signs?
  [ ] Yes (wet filament, feels sticky)
    → Likely B (must dry filament)
  [ ] No (feels dry)
    → Likely A or C
```

**Step 2: Implement Fix (as applies)**

**If A (temperature too high)**:
- [ ] Reduce nozzle temp: 220°C → 215°C
- [ ] Re-slice and print Iteration 2

**If B (filament wet)**:
- [ ] Dry filament in oven at 50–60°C for 4–6 hours
  - Place spool in sealed container with desiccant packets
  - Or: use filament dryer if available
- [ ] After drying: print calibration cube first (test)
- [ ] Print Iteration 2

**If C (batch/supplier mismatch)**:
- [ ] Confirm filament spool label: manufacturer + batch code
- [ ] Verify temperature for this specific brand/batch
  - eSUN PLA+: 200–225°C typical
  - MatterHackers: 210–230°C typical
- [ ] Adjust nozzle temp ±5°C as needed
- [ ] Re-slice and print Iteration 2

**If D (cooling rate)**:
- [ ] Disable chamber fan (if available) for first 30 min
- [ ] Or: print in enclosure to slow cooling
- [ ] Re-slice and print Iteration 2

### Iteration 2 Timeline

If A (temperature): 4 hours print
If B (drying): 6 hours dry + 4 hours print (≈10 hours total, same day or next)
If C/D: 4 hours print

---

## 7. Multi-Iteration Failure (Escalation)

**Scenario**: You've tried Iteration 2, and it still fails with similar or different issues.

**When to escalate** (after 2 failed iterations):

This suggests either:
- Root cause misdiagnosed in Step 1 diagnosis
- Multiple issues compounding (e.g., speed + temperature + tolerance)
- Design is fundamentally incompatible with this printer/material
- Environmental issue (humidity, printer hardware degradation)

### Escalation Procedure

**Step 1: Document Everything (15 min)**

Create file: `test-print-iteration-2-analysis.md`

```markdown
# Iteration 2 Analysis — FAILED

## Original Issue
[Snap-arm / Grip / Post / Scale / Material]

## Fix Applied
[Specific changes to design, settings, or printer]

## Iteration 2 Result
[Same as Section 1.2–1.4: dimensions, functional test results, photos]

## New Issues (if different from Iteration 1)
[What changed? What's still broken?]

## Hypotheses for Escalation
1. [Most likely cause]
2. [Second hypothesis]
3. [Third hypothesis]

## Recommended Next Steps
- [ ] Call printer support (hardware issue?)
- [ ] Test with different filament batch (material issue?)
- [ ] Simplify design (remove snap-arm temporarily, test grip only)
- [ ] Revert to Iteration 1, accept limitations, proceed to production

## Images
[Link to test-print-photos folder]
```

**Step 2: Decision: Pivot or Continue?**

Call decision now (you decide):

**Option A: Simplify & Iterate (1–2 more iterations)**
- Remove snap-arm entirely (eliminate source of failures)
- Test grip + post on their own
- Add snap-arm back in final design if grip/post work

**Option B: Accept Iteration 1 + Workaround**
- Use Iteration 1 as-is (even if not perfect)
- Document workaround in operations manual
- Plan design v2 after first 50 units sold (data-driven)

**Option C: Pivot to Different Product**
- Abandon ModRun clip for now
- Test headphone hooks instead (simpler design, higher certainty)
- Return to clip v2 when you have more printer time/experience

**Option D: Escalate to Expert**
- Share design files + Iteration 2 report with 3D printing forum / discord
- Get second opinion from experienced printer user
- Continue based on their recommendation

### Recommended Decision Criteria

| Situation | Recommendation |
|-----------|-----------------|
| Iteration 2 has minor issues but functionally acceptable | Option B (accept + workaround) |
| Iteration 2 failed worse than Iteration 1 | Option A (simplify grip/post test) |
| You're frustrated after 2 iterations | Option C (pivot to hooks, lower complexity) |
| You want expert input before going further | Option D (escalate) |

---

## 8. Success Path: Iteration 1 or 2 Passes

**If test print passes** (Section 1.4 checks all ✓):

Proceed immediately to: `post-test-print-quick-reference.md`

**Timeline from test print pass**:
- Week 1: STL refinement + photography (6 hours)
- Week 2: Etsy listing + supplier outreach (2 hours)
- Week 3: Inventory production (11.5 hours)
- Week 4: Launch + first orders (4 hours ongoing)

**Target launch date**: Week of May 20–26 (if test print passes this week)

---

## 9. Quick Reference: Failure Decision Tree

```
Test print arrives. Inspect snap-arm.
├─ Cracked / stressed
│  └─ → Section 2 (Snap-Arm Failure)
├─ Snap-arm OK. Test grip.
│  ├─ Grips poorly / rough surface
│  │  └─ → Section 3 (Grip Surface Failure)
│  └─ Grip OK. Test cable post.
│     ├─ Post wobbles >2 mm
│     │  └─ → Section 4 (Post Wobble Failure)
│     └─ Post OK. Measure dimensions.
│        ├─ Off by >1 mm
│        │  └─ → Section 5 (Scale/Shrinkage)
│        └─ Dimensions OK. Check material.
│           ├─ Brittle / discolored
│           │  └─ → Section 6 (Material Issue)
│           └─ All checks pass
│              └─ → Section 8 (Success Path)

At any point, if unsure: escalate to Section 7 (Multi-Iteration Failure)
```

---

## 10. Timeline Summary

| Scenario | First Print | Iteration 1 | Iteration 2 | Total Time | Next Phase |
|----------|-------------|------------|------------|----------|-----------|
| **Passes immediately** | T+1 day | — | — | 1 day | Launch prep (Week 1 timeline) |
| **1 iteration needed** | T+1 day | Fix (15 min) + print (4 hr) = T+2 | — | 2 days | Launch prep |
| **2 iterations needed** | T+1 day | Fix + print = T+2 | Fix + print = T+3 | 3 days | Launch prep (1 day later) |
| **Escalation** | T+1 day | T+2 | T+3 | 3+ days | Decision: pivot or continue |

**Critical path**: Test print this week → Iteration 2 by May 17 → Launch prep May 18–25 → Go-live May 26+

---

## Attachment A: Tolerances Quick Reference

These are the most sensitive dimensions in the design:

| Feature | Nominal | Upper Limit | Lower Limit | Risk Level | Why |
|---------|---------|------------|------------|-----------|-----|
| **Snap-arm thickness** | 1.4 mm | 1.55 mm | 1.25 mm | CRITICAL | Determines snap durability; <1.25 mm = too flexible/failure |
| Cable post diameter | 8.0 mm | 8.3 mm | 7.7 mm | HIGH | >8.3 mm = won't fit; <7.7 mm = wobbles |
| Rail jaw opening | 8.0 mm | 8.2 mm | 7.8 mm | HIGH | Must fit rail securely; loose = slips, tight = won't install |
| Snap-arm length | 16.2 mm | 16.5 mm | 15.9 mm | MEDIUM | Affects snap force; within 0.3 mm is acceptable |
| Cable post height | 12.0 mm | 12.3 mm | 11.7 mm | MEDIUM | Affects cable loop size; within 0.3 mm OK |

---

**Status**: Ready for execution (May 16-26 window)  
**Last updated**: 2026-05-15  
**Author**: SuperClaude Orchestrator  
**Version**: 1.0 (First iteration)
