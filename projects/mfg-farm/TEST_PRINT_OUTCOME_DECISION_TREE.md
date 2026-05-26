---
title: Test Print Outcome Decision Tree — Launch Contingency Planning
project: mfg-farm
date: 2026-05-26
status: production-ready
related: ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md, post-test-print-quick-reference.md, supplier-economics.md
scope: executable immediately upon test print completion; routes all four outcome paths (PASS/PASS-WITH-ADJUSTMENTS/FAIL/PARTIAL-FAIL) to launch or recovery with zero planning lag
---

# Test Print Outcome Decision Tree — Launch Contingency Planning

**Purpose**: User executes test print (0.20mm layer height, PLA+, 3 walls, 220–225°C) and reports a simple result. This document provides instant routing to execution roadmap—no planning lag, no discovery phase.

**Owner**: User (physical print execution + result reporting) → Agent (route to appropriate playbook)

**Target**: All 4 outcome paths pre-staged with diagnostic procedures, action sequences, timeline contingencies, and financial impacts quantified.

**Print Specification** (for reference):
- **Material**: PLA+ (matte black or color variant)
- **Layer height**: 0.20mm (crisp detail for snap-arm tolerance visibility)
- **Walls**: 3 walls minimum (structural margin for brittle failures)
- **Nozzle temp**: 220–225°C (within PLA+ spec; affects surface finish & layer adhesion)
- **Focus tolerance**: Snap-arm clearance in rail slot (1.4mm ±0.15mm target)
- **Critical inspection**: Cable bore snap test, jaw pressure, layer adhesion, no cracks

---

## Part 0: Pre-Test-Print Checklist

**Before you print**, ensure:

- [ ] Bambu P1S heated bed cleaned & leveled
- [ ] Nozzle cleaned (AMS load/unload cycle once to purge residue)
- [ ] PLA+ loaded in AMS slot 1 (confirm color)
- [ ] Bambu Studio profile: 0.20mm layer height, 3 walls, standard fill
- [ ] Test print file: `modrun_clip_6mm.stl` (middle bore size; snap-arm most visible)
- [ ] Print bed has 10"×4" clear space (clip is ~3"×1.5"×1.4" with margins)
- [ ] Cooling time: 30 min post-print minimum before handling
- [ ] Inspection tools ready: calipers, light source, tweezers

**Once you hit print, this document becomes your guide.**

---

## Part 1: OUTCOME A — PASS ✓

**Definition**: Snap-arm tolerance acceptable; clip functions correctly; no structural defects; ready for production.

### 1.1 Diagnostic Checklist (10 minutes)

Use this table to validate the test print. Check each item; if ALL pass, confirm **OUTCOME A: PASS**.

| Inspection Item | Spec | Pass ✓ | Marginal ⚠ | Fail ✗ | Notes |
|---|---|---|---|---|---|
| **Snap-arm thickness** | 1.4mm ±0.15mm; arm should bend <2mm under thumb pressure | ✓ | ⚠ | ✗ | Measure with calipers at 3 points; record avg |
| **Snap-arm in slot** | Arm fits in rail slot (8.0mm width) with 0.2mm clearance ea side; no binding | ✓ | ⚠ | ✗ | Slide arm left-right in slot; should move freely |
| **Cable bore diameter** | 6mm ±0.05mm (for 6mm bore variant); no wobble when cable post inserted | ✓ | ⚠ | ✗ | Measure with bore gauge or calipers |
| **Snap-arm locking nub** | Nub engages rail slot cleanly; cable does NOT fall out; click is audible | ✓ | ⚠ | ✗ | Insert cable; snap arm closed; tug cable gently |
| **Jaw pressure** | Firm snap when arm closes; no rattle or click after closure | ✓ | ⚠ | ✗ | Snap arm closed by hand; no wobble in arm |
| **Layer adhesion** | No layer separation, cracks, or bed adhesion defects; print is solid | ✓ | ⚠ | ✗ | Inspect under light; flex arm gently—no snapping |
| **Surface finish** | Smooth surfaces on snap arm & bore edges; no rough stringing or zits | ✓ | ⚠ | ✗ | Visual inspection; rough texture OK if functional |
| **Overall function** | Clip holds cable securely; arm does not crack under normal use; design validated | ✓ | ⚠ | ✗ | Final user assessment—does it work? |

**DECISION GATE**: All 8 items marked ✓? → Proceed to **Action Sequence A: Launch Immediately**.
Any ⚠ (marginal)? → Proceed to **OUTCOME B: PASS-WITH-ADJUSTMENTS**.
Any ✗ (fail)? → Proceed to **OUTCOME C: FAIL** or **OUTCOME D: PARTIAL-FAIL** (route based on failure mode below).

### 1.2 Action Sequence A: Launch Immediately (May 25–29)

**Timeline**: 4 days. Pre-stage execution in parallel per ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST Part 1.

| Day | Phase | Actions | Owner | Duration | Blocker? |
|---|---|---|---|---|---|
| **Today** | Tolerance Lock | ✅ All 8 diagnostics pass | You | 10 min | NO |
| **Today** | Photos (May 25) | 8 hero shots: clip on rail, close-up snap-arm, cable inserted, 3× angles, color variant, ecosystem | You + Agent | 30 min | NO |
| **Today** | Dry Run QA | Print 3 additional units at same settings; test all 3 for consistency; log any variance | You | 90 min | NO |
| **May 26** | Listing Final | Review Etsy listing (draft from pre-work); add photos; verify all fields complete; no placeholders | You | 30 min | NO |
| **May 26** | Supplier Lock | Confirm ≥3 of 5 suppliers responded; finalize pricing; log in tracker | You | 30 min | NO |
| **May 27** | Inventory Batch | Print 20–25 clips + 4 rails at production settings; QA all units; sort by color; pack for launch | You | 120 min | NO |
| **May 28** | Pre-launch Check | Test Etsy listing URL from incognito; verify listing indexed; final inventory count | You | 30 min | NO |
| **May 29** | **GO LIVE** | Publish Etsy listing 10 AM; post Reddit/Instagram/TikTok; ship first orders same-day if arrive before 2 PM | You | 30 min | NO |

**Success Criteria for Launch**:
- ✅ Listing live with ≥5 photos
- ✅ Shipping profile configured (USPS Priority, flat $3.99)
- ✅ Shop policies complete (no placeholders)
- ✅ 20+ clips in inventory, QA'd
- ✅ ≥3 suppliers confirmed with pricing locked
- ✅ Social media posts scheduled or pre-written

**Financial Impact (OUTCOME A: PASS)**:
- No design iteration cost (zero extra filament, zero time)
- Inventory ready May 29 (on-schedule launch window)
- Expected revenue June 1–7: $400–600 (20 clips @ $12.99–$18.99, assuming 60–70% margin)
- No supplier financing needed (use existing cash flow for filament)
- Margin: 65–72% (validated in post-test-print-quick-reference.md)

---

## Part 2: OUTCOME B — PASS-WITH-ADJUSTMENTS ⚠

**Definition**: Snap-arm is tight but functional; minor sanding/adjustment acceptable; design works but may benefit from tolerance refinement.

**Common symptoms**:
- Snap arm takes significant pressure to close (>2kg force, but arm does not crack)
- Arm sits in slot slightly tight; binding under 10% of insertion depth
- Cable bore snap is hard but repeatable (>500 cycles, no failure risk)
- Surface finish rougher than expected but functionally sound

### 2.1 Diagnostic Checklist (5 minutes)

| Inspection Item | Assessment | Action |
|---|---|---|
| **Arm bends but hard to close** | Pressure needed to engage snap >2kg, but arm returns cleanly | Document pressure; proceed to 2.2 |
| **Slot binding (slight)** | Arm binds <5mm on insertion; 90% of travel free | Document bind point; proceed to 2.2 |
| **Cable bore snap works** | Snap engages/disengages after 10+ test cycles, no fatigue cracks | Continue testing; monitor for cracks |
| **Layer adhesion OK** | No separation visible; arm does not snap under normal pressure | Proceed to 2.2 |
| **Surface finish rough** | Texture on arm is visible but not sharp; does not affect function | Document; proceed if function solid |

**DECISION GATE**: Functionality is confirmed but adjustment would improve UX? → **Action Sequence B: Test 2–3 Adjustments, Then Validate**.

### 2.2 Action Sequence B: Adjust + Validate (May 24–25, 1 day)

**Option 1: Hardware Adjustment (No CAD change)**
- **Layer height**: -0.05mm (try 0.15mm, increases arm flexibility slightly)
- **Nozzle temp**: -5°C (try 215°C, reduces resin viscosity, tighter tolerances)
- **Retraction tuning**: Increase by 0.5mm, reduce stringing on arm edge

**Option 2: Filament Swap (Material change)**
- **Try**: PLA+ from different supplier (e.g., eSUN → Anycubic Overture)
- **Rationale**: Different suppliers have ±0.5% diameter variation; may ease snap arm fit
- **Cost**: ~$1.50 per test unit (low risk)

**Option 3: CAD Micro-Adjustment (Parametric tolerance)**
- **Change**: Reduce snap-arm thickness by 0.1mm (1.4mm → 1.3mm)
- **Effect**: Arm becomes 7% more flexible; easier snap
- **Risk**: Low (arm still 1.3mm, well above snap failure point ~0.8mm)
- **Regenerate STL**: Run `modrun_clip_b123d.py --snap-arm-thickness 1.3` (script parameterized)

**Execution Order** (Pick one path, commit to it):

| Path | Time | Cost | Risk | Best For |
|---|---|---|---|---|
| **1. Hardware only** (layer + temp) | 2 hours | $0 | Lowest | "Arm works but tight — tweak settings" |
| **2. Filament swap** | 1 hour | $1.50 | Low | "Want to avoid CAD iteration" |
| **3. CAD micro-adjust** | 3 hours | $1.50 | Low | "Confident in design; want perfect fit" |

### 2.3 Validation Sequence (May 25)

**After adjustment, print 2–3 test units**:

| Test # | Action | Result | Decision |
|---|---|---|---|
| Unit 1 | Print with adjusted setting; cool 30 min; test snap arm | Pass? ✓ / Fail? ✗ | If ✓ → Test Unit 2 |
| Unit 2 | Print with adjusted setting; test snap arm 20+ cycles | Pass? / Fail? | If ✓ → Confirm adjustment |
| Unit 3 | (Optional) Stress test: snap arm 100+ cycles or extreme pressure | Pass? / Fail? | If ✓ → Proceed to launch |

**Success Criteria**:
- ✅ Unit 1 passes snap test
- ✅ Unit 2 passes 20+ cycles with no fatigue crack
- ✅ Unit 3 (if run) passes stress test
- ✅ Arm pressure <1.5kg (comfortable to close)
- ✅ No layer separation observed

**If all 3 pass**: Proceed to **Action Sequence A: Launch Immediately** (adjusted settings locked).
**If any fail**: Escalate to **OUTCOME C: FAIL** (design fundamentally undersized; larger arm required).

### 2.4 Financial Impact (OUTCOME B: PASS-WITH-ADJUSTMENTS)

**Timeline**: 1-day validation (May 24–25) → Launch May 26–30 (1 day slip).

| Cost Item | Amount | Notes |
|---|---|---|
| Filament (test units, 3× 75g) | $0.33 | At $0.013/g PLA+ |
| Nozzle cleaning/setup | $0 | Incidental |
| **Total iteration cost** | **$0.33** | Negligible |

**Revenue impact**:
- Launch delayed 1 day (May 29 → May 30)
- First week revenue: $380–500 (vs. $400–600 if on-schedule)
- Margin: 65–72% (unchanged)
- Supplier: No change (filament still from existing stock)

**Decision point**: Is 1-day launch slip acceptable? → YES (minor impact, confidence gain high).

---

## Part 3: OUTCOME C — FAIL ✗

**Definition**: Snap-arm broken/non-functional; design must be revised before production.

**Failure modes**:
- Arm snaps during first insertion or snap test (brittle failure)
- Arm cracks visibly; layers separate
- Bore diameter out-of-spec (>6.3mm or <5.7mm) → cannot hold cable securely
- Locking nub fails to engage rail slot; cable falls out

### 3.1 Diagnostic Checklist (10 minutes)

| Failure Mode | Root Cause | Next Action |
|---|---|---|
| **Arm snaps under light pressure** | Brittle failure (PLA+ too stiff or arm thickness insufficient) | → Path 1: Switch to TPU 95A flexible filament |
| **Arm cracks; layer separation visible** | Layer adhesion problem (nozzle temp too low or bed not level) OR design too thin | → Path 1 (filament) or Path 2 (CAD) |
| **Bore diameter wrong** (>6.3mm or <5.7mm) | Printer calibration drift or slicer error | → Path 2: CAD + re-tune printer |
| **Locking nub does not engage** | Nub height insufficient or rail slot width wrong | → Path 2: CAD revision (increase nub height by 0.3mm) |
| **Cable falls out after snap** | Nub angle wrong or engagement shallower than expected | → Path 2: CAD revision (increase nub protrusion by 0.2mm) |

**Decision Tree**:
- **Brittle failure + arm cracks?** → **Path 1: Material Pivot (TPU 95A)**
- **Bore or nub issue + clean print?** → **Path 2: CAD Revision**
- **Both issues?** → **Path 2 + Path 1 sequence** (fix design, then test in flexible material)

### 3.2 Path 1: Material Pivot to TPU 95A (1–2 day delay)

**Rationale**: If failure is brittle (arm snaps cleanly), the issue is material stiffness, not design. TPU 95A (thermoplastic polyurethane, 95 Shore A hardness) provides flexibility that prevents snap failure while retaining structural integrity.

**Procurement**:

| Supplier | Product | Cost | Lead Time | Notes |
|---|---|---|---|---|
| Overture (Amazon Prime) | TPU 95A, 500g | $18–22 | 2 days | Reliable AMS compatibility |
| eSUN (Amazon Prime) | TPU95A, 500g | $16–20 | 2 days | Warehouse stock; slightly cheaper |
| Anycubic (direct) | TPU-M95, 500g | $12–15 | 5–7 days | China ship; too slow for contingency |

**Recommended path**: **Order Overture TPU 95A from Amazon Prime, arrive May 27 afternoon**. Cost: ~$20.

**Print Settings for TPU** (different from PLA+):

| Setting | PLA+ Standard | TPU 95A Adjustment | Reason |
|---|---|---|---|
| Nozzle temp | 220–225°C | 215–220°C | TPU sensitive to heat; lower temp prevents oozing |
| Bed temp | 60°C | 45–50°C | Reduced adhesion to prevent warping |
| Layer height | 0.20mm | 0.25–0.30mm | TPU prints cleaner at thicker layers |
| Print speed | 80–100 mm/s | 30–50 mm/s | TPU must print slower to avoid stringing |
| Retraction | 6mm | 0mm or minimal | TPU clogs easily; disable retraction first, enable only if stringing severe |

**Test Print Sequence**:

| Step | Action | Time | Result |
|---|---|---|---|
| 1 | Filament arrives May 27 afternoon | — | Unbox, dry 2+ hours at room temp |
| 2 | Load TPU into AMS; run purge cycle | 10 min | Confirm color & extrusion |
| 3 | Slice `modrun_clip_6mm.stl` with TPU profile | 10 min | Use Bambu Studio TPU preset (or manual settings above) |
| 4 | Print 1 test unit (TPU, 0.25mm layer, 220°C) | 60 min | Monitor for stringing; adjust retraction if needed |
| 5 | Cool 30 min minimum | — | TPU takes longer to set than PLA |
| 6 | Test snap arm: pressure, cycles, durability | 15 min | Snap arm should flex without breaking; engage/disengage 20+ times |
| 7 | Cable bore test: insert cable, hold, tug | 10 min | Nub must lock cleanly; cable cannot fall out |

**Success Criteria**:
- ✅ Snap arm flexes under thumb pressure (2–3mm deflection)
- ✅ Arm engages/disengages ≥20 cycles without cracking
- ✅ No visible cracks, stringing, or layer separation
- ✅ Cable locks securely; does not fall out

**If TPU test passes**: Proceed to **Action Sequence C1: TPU Launch Roadmap** (below).
**If TPU test fails**: Escalate to **Path 2: CAD Revision** (design issue confirmed).

### 3.3 Path 2: CAD Revision (2–3 day delay)

**Rationale**: If failure is NOT brittle (e.g., bore out-of-spec, nub engagement issue), the design requires adjustment.

**Common revisions**:

| Issue | Fix | Change |
|---|---|---|
| Snap-arm too thin (cracks in PLA) | Increase thickness | 1.4mm → 1.6mm (+14%) |
| Bore diameter off | Adjust bore offset | Run calibration print; adjust by ±0.1mm |
| Nub height insufficient | Increase protrusion | 1.2mm → 1.5mm nub height |
| Slot binding (design too large) | Reduce clip width | 7.6mm → 7.4mm (minor tolerance) |

**Execution**:

1. **Edit CAD** (parametric design in `modrun_clip_b123d.py`):
   ```python
   SNAP_ARM_THICKNESS = 1.6  # Changed from 1.4
   SNAP_NUB_HEIGHT = 1.5      # Changed from 1.2
   ```

2. **Regenerate STL**:
   ```bash
   uv run python cadquery/modrun_clip_b123d.py --bore 6 --output-dir stl/
   ```

3. **Test print** (1 unit, PLA+ at original settings):
   - Confirm fix without introducing new issues
   - Run full diagnostic checklist from Part 1

4. **If revised design passes**: Proceed to **Action Sequence C2: CAD Launch Roadmap** (below).
5. **If revised design fails**: Root-cause analysis required (escalate to agent).

### 3.4 Action Sequence C1: TPU Launch Roadmap (May 27–30, 2 days)

**Assumption**: TPU test print passed; material change is confirmed solution.

| Day | Phase | Actions | Duration | Blocker? |
|---|---|---|---|---|
| May 27 | TPU Batch 1 | Print 15 clips in TPU (45-unit batch split 3×5 to manage slow print speed) | 180 min | NO |
| May 27 | QA All | Test all 15 units for snap arm durability, cable lock, no cracks | 45 min | NO |
| May 28 | TPU Batch 2 | Print 10 more clips (safety stock); QA | 120 min | NO |
| May 28 | Materials List | Document: "ModRun clips, Standard Line: PLA+ (stock). Premium Line: TPU 95A (new, $0.40 material premium per unit)" | 15 min | NO |
| May 29 | Etsy Launch | Update listing: add TPU color option if ordered (or note "Premium flexible variant available—message for quote"); publish | 20 min | NO |
| May 29 | Social Post | "Tested TPU variant—even more durable. Standard PLA+ or flexible TPU 95A. Etsy link in bio." | 10 min | NO |

**Success Criteria**:
- ✅ 25 TPU clips printed & QA'd
- ✅ Etsy listing updated (TPU option documented)
- ✅ Launch May 29 (1 day slip from original May 28)
- ✅ Margin adjusted: TPU adds $0.40 material cost per unit (margin: 60–68% vs. 65–72% for PLA)

### 3.5 Action Sequence C2: CAD Launch Roadmap (May 26–30, 2–3 days)

**Assumption**: CAD revision is committed; revised design passes validation test print.

| Day | Phase | Actions | Duration | Blocker? |
|---|---|---|---|---|
| May 26 | CAD Edit | Modify parametric design; regenerate STL; commit to git | 30 min | NO |
| May 26 | Test Print 1 | Print 1 unit revised design; full diagnostic checklist | 60 min | NO |
| May 27 | Validate | If test passes → print 10-unit batch (45 min); QA all 10 | 75 min | YES if test fails |
| May 27 | Supplier Re-confirm | Email suppliers: "Updated design ready for production batch; no pricing change expected" | 10 min | NO |
| May 28 | Production Batch | Print 20 clips at final settings; QA; pack for launch | 120 min | NO |
| May 29 | Etsy Launch | Update listing: "Production design finalized; now shipping with improved tolerances"; publish | 20 min | NO |

**Success Criteria**:
- ✅ Revised design passes validation test
- ✅ 20+ production units printed & QA'd
- ✅ Etsy launch May 29 (1 day slip)
- ✅ Margin: 65–72% (no material cost change)
- ✅ Git commit: `fix: modrun-snap-arm-tolerance-adjustment-[description]`

### 3.6 Financial Impact (OUTCOME C: FAIL)

| Cost | Path 1 (TPU) | Path 2 (CAD) | Notes |
|---|---|---|---|
| Material iteration | $20 (TPU 95A spool) | $0.75 (test print filament) | TPU is one-time; CAD iteration uses existing filament |
| Filament per unit (ongoing) | +$0.40 (vs. PLA) | No change ($0.79) | TPU material cost higher; not passed to customer yet |
| Design revision labor | $0 | 30 min (CAD + regenerate) | Minimal if parametric |
| Timeline slip | 1 day (May 28 → 29) | 2–3 days (May 28 → 30–31) | CAD iteration slower than material swap |
| **Revenue impact** | $380–500 (1-day slip) | $350–450 (2–3 day slip) | Delayed first-week revenue vs. OUTCOME A |
| **Total contingency cost** | **$20** | **$0.75** | Path 1 higher upfront; Path 2 lower risk |

**Go/No-Go Decision**:
- **Path 1 (TPU)**: Proceed if failure is clearly brittle (arm snaps, no structural issues). Timeline: +1 day.
- **Path 2 (CAD)**: Proceed if failure is design-related (bore, nub, slot fit). Timeline: +2–3 days.
- **Both paths fail**: De-risk with service bureau (Craftcloud instant quote for 10–25 units @ $10–15/unit) while design is revisited. Cost: $100–375 for emergency inventory; buys 5–10 days.

---

## Part 4: OUTCOME D — PARTIAL-FAIL (Cosmetic)

**Definition**: Clip functional but cosmetic issues present (surface roughness, stringing, layer splits, visible zits).

**Common symptoms**:
- Snap arm works but has rough texture or visible stringing
- Layer splits visible on outer edge (non-structural)
- Surface finish poor (bumpy, not smooth)
- Color inconsistent or filament looked old
- First-layer finish uneven or slightly raised edges

### 4.1 Risk Assessment (5 minutes)

| Cosmetic Issue | Functional Impact | Customer Return Risk | Action |
|---|---|---|---|
| **Stringing on arm** | None (arm works fine) | Low (<2% return rate) | Proceed to launch as-is OR tune settings |
| **Surface roughness (all over)** | None (texture, not structural) | Low (<2%) | Proceed as-is; market as "industrial finish" |
| **Layer splits on edge** | None (interior solid) | Low (<1%) if not visible in use | Proceed as-is; not visible to customer |
| **Visible zits or blobs** | None (cosmetic only) | Medium (5–10% if customer-facing) | Tune nozzle wipe OR retest with PLA (not PLA+) |
| **First-layer unevenness** | None (fits rail fine) | Low (<1%) | Proceed; imperceptible in final product |

**Decision Gate**: 
- Functional defect observed? → **OUTCOME C: FAIL** (escalate).
- Only cosmetic issues? → **OUTCOME D: DECISION TREE BELOW**.

### 4.2 Decision Path D: Assess Risk + Proceed or Retune

**Step 1: Evaluate customer impact** (2 minutes)

Ask yourself: *Will a customer see this cosmetic issue in the final product?*

- Cable clip mounted in rail on desk: Customer sees the top/side (depends on angle)
- Snap arm: Mostly hidden inside rail slot; stringing NOT visible
- Cable bore: Partially visible but customer focus on cable management, not finish
- Outer edges: Might be visible depending on color & installation

**Step 2: Decide**: Proceed with tuning or proceed without.

| Issue | Customer Visibility | Recommendation |
|---|---|---|
| **Stringing on snap arm** | Hidden (inside slot) | Proceed to launch; stringing invisible |
| **Rough texture on bore** | Partially visible | Proceed if texture does not affect cable fit; cosmetic risk low |
| **Layer splits on edge** | Depends on color (black less visible) | Proceed if edge not customer-facing; risk <2% |
| **Blobs on side wall** | Visible if customer looks close | **Tune nozzle or retint**; medium risk |
| **First-layer uneven** | Not visible (bottom face) | Proceed; no risk |

### 4.3 Action Sequence D1: Proceed Without Tuning (FAST PATH, May 25–29)

**Decision**: Cosmetic issue is acceptable; customer return risk <3%; launch on-schedule.

**Execution**: Same as **Action Sequence A: Launch Immediately** (Part 1). No iteration needed.

**Risk Acknowledgment**:
- Expected return rate: 2–3% due to cosmetic issues
- Refund cost: ~$1–2 per unit (low impact at $12.99 price point)
- Margin still 65–72% after accounting for 3% return rate

**Proceed to launch May 29.**

### 4.4 Action Sequence D2: Tune + Validate (SAFE PATH, May 24–25, 1 day)

**Decision**: Cosmetic issue is visible; mitigate with print setting tweak before launch.

**Common tuning options**:

| Cosmetic Issue | Setting Change | Effect | Confidence |
|---|---|---|---|
| **Stringing on arm** | Increase retraction 0.5mm OR lower temp 2°C | Reduces oozing | 80% (minor tweak) |
| **Rough surface finish** | Reduce nozzle wipe time OR increase print speed 5% | Cleaner extrusion | 60% (empirical; may backfire) |
| **Layer splits** | Increase wall thickness (CAD: 2.0mm → 2.2mm walls) | Adds margin | 90% (design change) |
| **Blobs (nozzle zits)** | Enable nozzle wipe in Bambu Studio OR increase Z-hop | Lifts nozzle cleanly | 75% (medium confidence) |

**Recommended tuning** (lowest risk):

```
Original settings:
  - Nozzle: 223°C
  - Retraction: 6mm
  - Layer height: 0.20mm

Tuned settings:
  - Nozzle: 220°C (down 3°C)
  - Retraction: 6.5mm (up 0.5mm)
  - Z-hop: 0.4mm (enable if disabled)
  - Print speed: 85 mm/s (down from 95 mm/s)
```

**Test print sequence**:

| Step | Action | Time | Result |
|---|---|---|---|
| 1 | Slice with tuned settings | 10 min | Save as "modrun_clip_6mm_v2_tuned" |
| 2 | Print 1 test unit | 60 min | Monitor for stringing; observe surface quality |
| 3 | Cool 30 min | — | Full cool before inspection |
| 4 | Inspect cosmetics | 5 min | Is stringing reduced? Surface smoother? |
| 5 | Test functionality | 10 min | Run full diagnostic checklist (Part 1) |

**Success Criteria**:
- ✅ Stringing/blobs visibly reduced (50%+ improvement)
- ✅ Functionality unchanged (snap arm works, cable bore clear)
- ✅ No new issues introduced (no worse surface finish)

**If tuned unit improves cosmetics**: Print 20-unit production batch at tuned settings; proceed to **Action Sequence A: Launch May 29** (same timeline as OUTCOME A).

**If tuned unit same/worse**: Revert to original settings; proceed with **Action Sequence D1: Proceed Without Tuning** (accept risk, launch May 29).

### 4.5 Financial Impact (OUTCOME D: PARTIAL-FAIL)

**Path D1 (Proceed without tuning)**:
- Extra cost: $0 (no iteration)
- Timeline: On-schedule (May 29)
- Return risk: 2–3% (~$2–4 per 10 units)
- Net revenue impact: Minimal (acceptable loss from returns)

**Path D2 (Tune + validate)**:
- Extra cost: $0.50–1.00 (1 test print filament)
- Timeline: 1-day delay (May 30), but lower return risk
- Return risk: 0.5–1% (significant improvement)
- Net revenue impact: Positive (reduced refund costs offset 1-day delay revenue loss)

**Recommendation**: 
- If cosmetic issue is barely visible (stringing on hidden snap arm) → **Path D1** (launch May 29)
- If cosmetic issue is very visible (blobs on customer-facing side) → **Path D2** (launch May 30, lower return risk)

---

## Part 5: Launch Timeline Contingency Matrix

**Summary table for all four outcomes** — use this to track where you are and what comes next.

| Outcome | Result | Day 0 Decision | Days 1–3 Work | Launch Day | First-Week Revenue | Margin | Notes |
|---|---|---|---|---|---|---|---|
| **A: PASS** | ✅ All specs pass | Proceed immediately | Photos, supplier, inventory | **May 29** | $400–600 | 65–72% | On-schedule; maximum revenue |
| **B: PASS-WITH-ADJ** | ⚠ Works but tight | Test adjustment (1 day) | Validate 2–3 units, retest | **May 30** | $380–500 | 65–72% | 1-day slip; confidence gain |
| **C: FAIL (Path 1)** | ✗ Brittle; material issue | Order TPU 95A | Test TPU, print batch | **May 29** | $350–450 | 60–68% | 1-day slip; material cost +$0.40 |
| **C: FAIL (Path 2)** | ✗ Design issue | Edit CAD, regen STL | Validate, print batch | **May 30–31** | $300–400 | 65–72% | 2–3 day slip; design locked |
| **D: PATH 1** | Cosmetic (accept) | Accept risk | Photos, supplier, inventory | **May 29** | $390–580 | 63–70% | On-schedule; 2–3% return risk |
| **D: PATH 2** | Cosmetic (tune) | Tune settings | Test tuned print, validate | **May 30** | $370–480 | 65–71% | 1-day slip; <1% return risk |

---

## Part 6: Fallback Supplier Contingency

**If test print delays launch AND inventory depletes faster than expected, these suppliers provide emergency material:**

### 6.1 Standard Filament Suppliers (PLA+)

| Supplier | Product | Cost | Lead Time | Minimum | Best For |
|---|---|---|---|---|
| **Overture (Amazon Prime)** | PLA+ 1kg or 10kg bundle | $11–15/kg | 2 days | 1 spool | Emergency replenishment; AMS-reliable |
| **eSUN (Amazon Prime)** | PLA+ 10kg bundle | $11–13/kg | 2 days | 10kg case | Bulk emergency; cheaper per kg |
| **Anycubic (Amazon)** | PLA+ 1kg | $13–16/kg | 2 days | 1 spool | Backup if primary out of stock |
| **Craftcloud (web)** | Service bureau FDM | $10–15/part | Next day | 5 units | If in-house production fails entirely |

### 6.2 Flexible Material Suppliers (TPU 95A)

| Supplier | Product | Cost | Lead Time | Minimum | Best For |
|---|---|---|---|---|
| **Overture (Amazon Prime)** | TPU 95A 500g | $18–22 | 2 days | 500g | Preferred if Path 1 chosen |
| **eSUN (Amazon Prime)** | TPU95A 500g | $16–20 | 2 days | 500g | Budget option if Overture unavailable |
| **Anycubic (direct)** | TPU-M95 500g | $12–15 | 5–7 days | 500g | Cheap but slow; not for emergencies |

### 6.3 Emergency Service Bureau (If In-House Fails)

**Craftcloud (craftcloud.com)**: Instant quote FDM service.

- **Turnaround**: 1–2 business days
- **Cost per unit**: $10–15 for small clip (100–200 part estimate)
- **Minimum**: 1 unit (no MOQ)
- **Best for**: Equipment failure, supply disruption, emergency backlog

**Process**:
1. Upload STL file to Craftcloud
2. Get instant quote (<2 min)
3. Review 1–2 material options
4. Order (ship within 24h)
5. Receive 2–3 business days

**Margin impact**: Adds $10–15 per unit cost (margin drops to 15–25% on that unit). Use only for order fulfillment backlog, not production baseline.

---

## Part 7: Financial Scenario Modeling

**All four outcomes quantified** for capital planning.

### 7.1 Scenario 1: OUTCOME A (PASS) — On-Schedule Launch May 29

**Unit economics**:
| Cost Item | Per Unit | Notes |
|---|---|---|
| Material (PLA+, 75g) | $0.98 | @$13/kg filament |
| Electricity/depreciation | $0.13 | Bambu P1S amortized |
| Packaging (mailer, bubble, label) | $0.45 | USPS First Class included |
| Etsy fees (6.5%) | $0.81 | @$12.99 price |
| Shipping label (Pirate Ship) | $0.35 | USPS First Class |
| Labor (4 min pick/pack) | $1.00 | @$15/hr |
| **COGS Total** | **$3.72** | — |
| **Selling Price** | **$12.99** | — |
| **Margin** | **71.3%** | Gross margin before supplier/supplier commitments |

**First-week revenue forecast** (May 29 – June 4):

| Day | Est. Orders | Revenue | Cumulative |
|---|---|---|---|
| May 29 (launch) | 2–3 | $26–39 | $26–39 |
| May 30 | 4–6 | $52–78 | $78–117 |
| May 31 | 5–7 | $65–91 | $143–208 |
| June 1–2 | 3–4 | $39–52 | $182–260 |
| June 3–4 | 2–3 | $26–39 | $208–299 |
| **Total Week 1** | **16–23 units** | **$208–299** | — |

**Cumulative revenue May 29–June 15** (3 weeks):
- Week 1: $200–300 (low; launch momentum)
- Week 2: $300–450 (builds from reviews, SEO)
- Week 3: $400–600 (peak; word-of-mouth)
- **Month 1 revenue**: $900–1,350 (target: $1,000+ with good ops)

**Capital required**:
- Filament (safety stock): $60 (50kg @ $12/kg)
- Packaging supplies: $30 (mailers, bubble wrap, labels)
- Bumper pads (if added): $20 (100-pack AliExpress)
- **Total**: $110–150 for May operations

### 7.2 Scenario 2: OUTCOME B (PASS-WITH-ADJUSTMENTS) — 1-Day Slip to May 30

**Delay cost**:
- Iteration filament: $0.33 (3 test prints)
- Timeline slip: 1 day → Lost ~$20–30 first-day revenue

**Unit economics**: Identical to OUTCOME A (same settings, no material change).

**Cumulative revenue May 30–June 15** (3 weeks, shifted 1 day):
- Week 1: $180–270 (1-day shorter window)
- Week 2: $300–450 (same ramp as A)
- Week 3: $400–600 (same ramp as A)
- **Month 1 revenue**: $880–1,320 (vs. $900–1,350 for OUTCOME A; negligible difference)

**Capital required**: Identical to OUTCOME A ($110–150).

**Verdict**: 1-day slip has minimal revenue impact; proceed if confidence improves.

### 7.3 Scenario 3: OUTCOME C (FAIL, Path 1 — TPU Material) — 1-Day Slip to May 29

**Extra costs**:
- TPU filament (500g @ $20): $20
- Test print (125g @ $0.013/g): $1.60
- **Total iteration cost**: $21.60

**Unit economics**:
| Cost Item | PLA+ | TPU 95A | Change |
|---|---|---|---|
| Material | $0.98 | $1.38 | +$0.40 |
| Electricity | $0.13 | $0.13 | No change |
| Packaging | $0.45 | $0.45 | No change |
| Etsy fees (6.5%) | $0.81 | $0.81 | No change (price unchanged) |
| Shipping | $0.35 | $0.35 | No change |
| Labor | $1.00 | $1.00 | No change |
| **COGS** | **$3.72** | **$4.12** | **+$0.40** |
| **Margin** | **71.3%** | **68.3%** | **-3%** |

**Selling price question**: Do you charge customer extra for TPU? 
- Option A: Same price ($12.99) → margin drops to 68.3%
- Option B: Premium price ($15.99) → margin jumps to 73.2%, but order volume may drop
- **Recommended**: Option A (maintain $12.99; marketing "upgrade"); absorb margin hit

**Cumulative revenue May 29–June 15** (if TPU is premium line, not primary):
- **Primary line (PLA+)**: $900–1,350 (same as OUTCOME A)
- **Premium line (TPU)**: $200–400 (estimated 20–30% TPU adoption)
- **Total blended revenue**: $1,100–1,750
- **Blended margin**: 70.2% (weighted average)

**Capital required**:
- TPU filament spool: $20 (upfront, but reusable for future batches)
- PLA+ safety stock: $60
- Packaging: $30
- **Total**: $110–150 (same as OUTCOME A; TPU spool is investment, not operational expense)

### 7.4 Scenario 4: OUTCOME C (FAIL, Path 2 — CAD Revision) — 2–3 Day Slip to May 31

**Extra costs**:
- CAD iteration filament: $0.75 (1–2 test prints)
- CAD revision labor: 0.5 hour (git commit, regenerate STL)
- **Total iteration cost**: <$5 (negligible)

**Unit economics**: Identical to OUTCOME A (same PLA+ filament, same price).

**Timeline impact**:
- **Revised design locked by May 27**
- **Production batch printed May 28–29**
- **Launch May 31** (2–3 day slip vs. May 29 original)

**Cumulative revenue May 31–June 15** (2.5 weeks, shifted 2 days):
- Week 1: $150–230 (2-day shorter window)
- Week 2: $300–450 (same ramp as A)
- Week 3: $400–600 (same ramp as A)
- **Month 1 revenue**: $850–1,280 (vs. $900–1,350; ~$50–70 revenue loss)

**Capital required**: Identical to OUTCOME A ($110–150).

**Verdict**: 2–3 day slip costs ~$50–70 revenue but removes design risk long-term.

### 7.5 Scenario 5: OUTCOME D (PARTIAL-FAIL, Path 1 — Accept Risk) — On-Schedule May 29

**Return cost**:
- Expected return rate: 2–3% of units shipped
- Refund per unit: ~$2 (credit to customer, cost to you)
- **First month return cost**: ~0.025 × 200–300 units × $2 = $10–15

**Unit economics**:
| Cost Item | Per Unit |
|---|---|
| COGS | $3.72 |
| Etsy fees | $0.81 |
| Expected return cost | $0.05 |
| **Effective COGS** | **$3.77** |
| **Margin** | **70.4%** (vs. 71.3% if 0% returns) |

**Cumulative revenue**: Same as OUTCOME A ($900–1,350) minus $10–15 refunds.

**Capital required**: Identical to OUTCOME A ($110–150).

**Verdict**: Accept cosmetic risk; 2–3% return rate manageable at this price point.

### 7.6 Scenario 6: OUTCOME D (PARTIAL-FAIL, Path 2 — Tune + Validate) — 1-Day Slip to May 30

**Extra cost**:
- Tuning filament: $0.50 (1 test print)

**Unit economics**: Identical to OUTCOME A.

**Timeline**: 1-day slip (same as OUTCOME B).

**Return rate**: <1% (vs. 2–3% for Path 1).

**Cumulative revenue**: $880–1,320 (same as OUTCOME B).

**Capital required**: Identical to OUTCOME A ($110–150).

**Verdict**: Low-cost insurance; pay $0.50 to cut return rate from 2–3% to <1% (saves ~$5–10).

---

## Part 8: Decision Summary & Quick-Start

**You received test print result. Start here:**

### Quick-Start Decision Tree (30 seconds)

1. **Did snap arm break or crack?** 
   - YES → **OUTCOME C: FAIL** (go to Part 3)
   - NO → Continue

2. **Can you snap the cable in and out 10+ times without the arm failing?**
   - NO → **OUTCOME C: FAIL**
   - YES → Continue

3. **Does the arm feel too tight to close comfortably (>2kg pressure)?**
   - YES → **OUTCOME B: PASS-WITH-ADJUSTMENTS** (go to Part 2)
   - NO → Continue

4. **Is the print surface rough, or do you see stringing/blobs?**
   - YES → **OUTCOME D: PARTIAL-FAIL** (go to Part 4)
   - NO → **OUTCOME A: PASS** (go to Part 1)

### Next Steps (Execute Immediately)

**OUTCOME A: PASS** → Execute Part 1, Section 1.2 (Action Sequence A).
**OUTCOME B: PASS-WITH-ADJUSTMENTS** → Execute Part 2, Section 2.2 (Action Sequence B).
**OUTCOME C: FAIL** → Execute Part 3, Section 3.2 (Path 1) or 3.3 (Path 2).
**OUTCOME D: PARTIAL-FAIL** → Execute Part 4, Section 4.3 (D1) or 4.4 (D2).

---

## Appendix A: Tolerance Reference & Diagnostic Tools

**Snap-arm specifications** (for measurement):

```
Snap-arm length:        8.0 mm
Snap-arm thickness:     1.4 mm (target ±0.15mm)
Snap-arm width:         7.6 mm (fits rail slot 8.0mm with 0.2mm clearance each side)
Snap-nub height:        1.2 mm
Snap-nub lead angle:    35° (insertion face)
Snap-nub lock angle:    80° (retention face)

Cable bore (6mm variant): 6.0 mm diameter ±0.05mm
Cable bore gap:          3.9 mm (65% of 6mm bore diameter)
```

**Measurement procedure**:

| Tool | What to Measure | How | Target |
|---|---|---|---|
| **Calipers (digital)** | Snap-arm thickness at 3 points (base, mid, tip) | Place caliper perpendicular to arm; record each | 1.4 ±0.15 mm |
| **Calipers** | Snap-arm width (side-to-side) | Measure arm at mid-length; should fit slot | 7.6 ±0.2 mm |
| **Bore gauge OR caliper** | Cable bore diameter | Insert bore gauge; slide in/out; record smallest gap | 6.0 ±0.05 mm |
| **Ruler (plastic, 0.5mm marks)** | Snap-arm bend under light pressure | Apply 1kg pressure; measure gap between arm and rail | <2 mm deflection |
| **Ruler** | Nub protrusion on arm | Measure nub height above arm surface | 1.2 ±0.2 mm |

**Pass criteria**: All measurements within tolerance; arm does not crack under normal pressure.

---

## Appendix B: Supplier Contact Checklist

**After test print passes (OUTCOME A or B), send these emails immediately:**

### Email 1: eSUN Direct (Primary supplier)

```
Subject: ModRun Cable Clip Production Batch — 20–50 kg/month potential

Hi eSUN,

I'm preparing a production batch for ModRun cable management clips launching on Etsy May 29. Test print is complete and validated.

Immediate need:
- 20 kg PLA+ (Matte Black, 1.75mm) — delivery by May 27
- Pricing quote for 20 kg bundle (vs. 10kg bundle rate)

Longer-term (June onwards):
- Potential 30–50 kg/month at consistent quality
- Interest in bulk pricing tier if volume confirmed

Can you provide a quote and lead time for May 27 delivery?

Best regards,
[Your name]
```

### Email 2: Anycubic Store (Secondary supplier)

```
Subject: PLA+ Supplier Inquiry — 30–50 kg/month potential

Hi Anycubic,

I'm scaling 3D printing production for ModRun cable management clips. Looking for reliable bulk supply partner.

Questions:
- Current PLA+ pricing for 20 kg batch (US warehouse vs. direct ship)?
- Can you deliver 20 kg by May 28?
- Volume pricing for 30–50 kg/month?

Test print is complete; ready to validate supplier quality.

Best regards,
[Your name]
```

### Email 3: Overture (Backup supplier)

```
Subject: PLA+ Bulk Order — Potential ongoing partnership

Hi Overture,

I'm launching a product line on Etsy using PLA+ and may need reliable bulk supply for 30–50 kg/month starting June.

Test: Can you deliver 20 kg (Matte Black, 1.75mm) by May 27–28?
Price: What is your 20 kg bundle rate?

Looking for a reliable domestic supplier. Interested in discussing ongoing partnership if pricing and quality align.

Best regards,
[Your name]
```

---

## Appendix C: Git Commit Template (Test Print Validation)

**After test print passes and design is locked**, commit to git:

```bash
git add cadquery/modrun_clip_b123d.py projects/mfg-farm/TEST_PRINT_OUTCOME_DECISION_TREE.md

git commit -m "feat: modrun-snap-arm-tolerance-validated-outcome-A

Test print completed [DATE]. All tolerance parameters pass:
- Snap-arm thickness: 1.4mm ±0.15mm ✓
- Snap-arm in slot: free movement, no binding ✓
- Cable bore: 6.0mm ±0.05mm ✓
- Snap-nub engagement: click audible, no slip ✓
- Layer adhesion: solid, no separation ✓
- Function: cable insert/remove ≥20 cycles, no fatigue ✓

Design locked for production. Ready for Etsy launch May 29.

Outcome: PASS (Decision Tree routing complete)
Next: Execute Action Sequence A (ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST Part 1)"
```

---

## Appendix D: Post-Launch Metrics Tracking

**After launch, track these metrics daily** (5 min/day):

| Metric | Where | Daily Check | Target |
|---|---|---|---|
| **Orders placed** | Etsy Shop Manager | Check 7 PM daily | 2–4 per day Week 1 |
| **Views** | Etsy Stats | Check 7 PM daily | 50+ per day |
| **Click-through rate** | Etsy Stats | Check 7 PM daily | >1% |
| **Favorites** | Etsy Stats | Check 7 PM daily | 5+ per day |
| **Customer questions** | Etsy Q&A | Check 8 AM + 3 PM | Reply <4 hours |
| **Margin check** | Spreadsheet | Weekly on Sunday | ≥65% |
| **Return rate** | Etsy + manual log | Weekly on Sunday | <3% |

**If metrics are below target by Day 4 (June 2)**, execute:
- [ ] Replace hero photo with under-desk angle shot
- OR [ ] Increase Etsy Ads to $2–3/day
- OR [ ] Post Reddit/TikTok content (free marketing)

---

**This decision tree is now live. Print it, post it, reference daily until launch.**

**When test print is done, pick your outcome. Execute the action sequence. Ship with confidence.**

---

*Contingency Planning Document v1.0*  
*Created: 2026-05-26*  
*Status: Production-ready*  
*Next review: 2026-06-01 (post-launch assessment)*
