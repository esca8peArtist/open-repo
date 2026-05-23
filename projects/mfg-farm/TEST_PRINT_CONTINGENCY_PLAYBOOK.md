---
title: Test Print Contingency & Recovery Playbook
project: mfg-farm
date: 2026-05-23
status: pre-staged for May 23-30 execution
related: post-test-print-launch-timeline.md, headphone-hooks-design-spec.md, DAY1_LAUNCH_OPERATIONS_PLAYBOOK.md
---

# Test Print Contingency & Recovery Playbook

**Purpose**: Test print is user-blocked (overdue May 22-23). This document stages both success and failure paths so execution can proceed immediately upon print result, without delay for planning.

**Owner**: User (physical execution) + Orchestrator (research, timeline adaptation)

**Decision gate**: Is test print functionally sound (all 6 tolerance parameters pass)? → YES = execute Success Path | NO = execute Failure Path

---

## Part 1: Test Print Success Path (May 23-30)

### Trigger
Tolerance validation (from DAY1_LAUNCH_OPERATIONS_PLAYBOOK Track A-1) confirms:
- Snap arm thickness: 1.4mm ✅
- Bore diameter: Within ±0.05mm ✅
- Jaw gap: 12.4mm / 25.4mm / 40.4mm ±0.4mm ✅
- Cable post diameter: 7.5–8.5mm ✅
- Rubber pad pocket: 1.2–1.8mm depth ✅
- No visible layer separation or bed adhesion defects ✅

**Action**: Proceed immediately to T+0 afternoon (photos, Etsy draft, supplier outreach per post-test-print-launch-timeline.md).

### Phase 1B: May 23-30 Pre-Launch Optimization Roadmap

#### Day 1 (May 23): Validation + Photography + Outreach
**Duration**: 3–4 hours total
- ✅ Run tolerance validation (15 min)
- ✅ Photography shoot: 8 shots per staging guide (25 min)
- ✅ Photo editing: Lightroom/Canva batch export (10 min)
- ✅ Dry run: Pick/pack 10 units with cost tracking (90–120 min)
- ✅ Supplier outreach: Send 5 emails simultaneously (20 min)
- ✅ Etsy listing draft: Title, description, tags, price (15 min)

**Decision gate end of day**:
- [ ] All 6 tolerance parameters pass
- [ ] Photos uploaded to Etsy draft
- [ ] 5 supplier emails sent
- [ ] Margin validation (target ≥60%): ___% confirmed ✅ / ❌ flag issue

**If margin <60%**: STOP here. Do not proceed. Flag COGS problem. Options: (a) negotiate supplier pricing May 24, (b) defer launch 1 week to source better supplier, (c) adjust product price or bundle strategy. Do not go live with below-target margin.

---

#### Day 2 (May 24): Supplier Response Window + Shop Finalization
**Duration**: 2 hours (mostly waiting)

| Time | Action | Owner | Duration |
|---|---|---|---|
| Morning | Check inbox for supplier responses (eSUN, Shop4Mailers typically respond 24–48h) | User | 10 min |
| Morning | If response with above-threshold pricing: draft counter-offer using negotiation templates from supplier-outreach doc | User | 5 min per offer |
| Morning | Review Etsy listing draft — any awkward phrasing? Are all dimensions filled? | User | 10 min |
| Afternoon | Complete shop-level settings: policies, About section, icon, banner (if not done May 23) | User | 20 min |
| Afternoon | Prepare Instagram crop + caption for launch (1080×1350px in Canva) | Orchestrator | 15 min |
| Afternoon | Draft Reddit post (`r/battlestations` or `r/cablefail`) — ready to post, not published yet | Orchestrator | 10 min |

**Decision gate end of day**:
- [ ] Etsy shop is 100% complete (no placeholder fields)
- [ ] At least 1 supplier has responded
- [ ] Instagram + Reddit drafts staged and ready

---

#### Day 3 (May 25): Supplier Negotiation Checkpoint + Listing Final
**Duration**: 1.5 hours

| Time | Action | Owner | Duration |
|---|---|---|---|
| Morning | Respond to any supplier counter-offers or requests | User | 10 min |
| Morning | Follow up on any non-responsive supplier (1-sentence reminder) | User | 5 min |
| Morning | Return to Etsy listing — final review with fresh eyes. Read description aloud. Fix phrasing | User | 15 min |
| Afternoon | eRank keyword check (if subscribed): Verify all 13 tags are searchable. Any obvious swaps? | Orchestrator | 20 min |
| Afternoon | Check: Have at least 2 of 5 suppliers responded? Log in tracker | User | 5 min |

**Success criteria for Day 3**:
- Supplier negotiation is progressing (at least 2 of 5 responded)
- Etsy listing is **final** — all fields complete, no placeholders
- Tags verified as searchable (if eRank check done)

---

#### Day 4 (May 26): Pre-Launch Inventory Batch + Final Supplier Lock
**Duration**: 2 hours

| Time | Action | Owner | Duration |
|---|---|---|---|
| Morning | Print launch batch: 20 clips + 4 rails at production settings (Bambu P1S, ~90 min print time) | User | 90 min |
| While printing | Finalize supplier negotiations. Confirm at least 3 of 5. Lock in final pricing | User | 30 min |
| Afternoon | QA the batch (tolerance checks, same table as dry run) | User | 20 min |
| Afternoon | Sort launch inventory by color, count, label | User | 10 min |
| Afternoon | Final Etsy listing review in preview mode (one last read) | User | 10 min |

**Success criteria for Day 4**:
- Launch inventory ready (20+ clips, 4+ rails, all QA'd)
- At least 3 of 5 suppliers locked in with confirmed pricing
- Etsy listing reviewed and ready to publish

---

#### Day 5 (May 27): Scheduling + Social Media Final Prep
**Duration**: 1 hour

| Action | Owner | Duration | Notes |
|---|---|---|---|
| Schedule Etsy publish: Thursday (May 29) 10 AM–2 PM Central | User | 2 min | Optimal recency boost window |
| Final check: Is listing URL clean and professional? | User | 2 min | etsy.com/shop/[YOUR_SHOP_NAME] |
| TikTok filming (optional, high-return): 15-sec clip of snap engagement | User | 20 min | Can defer to T+4 if time-constrained |
| Prepare launch-day social media schedule (if using buffer or similar) | Orchestrator | 10 min | Reddit 10:05 AM, Instagram 10:30 AM, optional r/3Dprinting 11 AM |

---

#### Day 6 (May 28): Quiet Day (Buffer)
**Duration**: As needed

- Monitor supplier responses (anyone still pending can be finalized today)
- Test Etsy listing URL from incognito window (confirm it's live-ready, not draft)
- Recheck shop-level policies one more time
- Final inventory count (ensure sufficient stock for first 5–10 orders)

---

#### Day 7 (May 29): Etsy Goes Live
**Duration**: 30 minutes

| Time | Action | Owner | Notes |
|---|---|---|---|
| 10:00 AM Central | Publish Etsy listing | User | 2 min — click Publish |
| 10:05 AM | Post Reddit announcement (pre-written draft) | User | 2 min |
| 10:30 AM | Post Instagram launch content (pre-edited photo + caption) | User | 2 min |
| 11:00 AM | Optional: Post in r/3Dprinting (design post, not sales) | User | Community engagement, not direct sales |
| Afternoon | Check Etsy search visibility in Shop Manager — confirm listing indexed | User | 5 min (takes 2–4 hrs to fully index) |
| Afternoon | Check listing on mobile — thumbnail crop correctly? Price visible? | User | 5 min |
| Afternoon | Log Day 1 metrics: views, favorites, conversions | User | — |

---

#### Day 8+ (May 30 onwards): First Week Monitoring
**Duration**: 5 min/day minimum

| Action | Frequency | Owner | Notes |
|---|---|---|---|
| Check Etsy stats: Views, Favorites, Conversions | Daily (end of day) | User | 5 min |
| Respond to messages within 2 hours | As needed | User | Critical for response rate |
| Follow up on supplier outstanding items | As needed | User | Finalize any pending agreements |

**7-day success benchmarks** (from post-test-print-launch-timeline.md):
- Views: 30–100+
- Favorites: 1–5+
- Conversions: 0 (normal for new listing — do not expect Day 1 sale)
- Listing visible in search for "cable management clips": Page 1–5
- All 13 tags saved and searchable: 10–13

---

## Part 2: Test Print Failure Path (May 23-27)

### Trigger
Tolerance validation reveals **any functional failure**:
- Snap arm <1.3mm or >1.5mm (affects cable grip)
- Jaw gap out of spec by >±0.5mm (rocks on desk, won't hold tightly)
- Cable post diameter <7mm or >9mm (cables slip)
- Rubber pad pocket <1.2mm depth (silicone bumper won't fit flush)
- Visible layer separation or adhesion defects (structural weakness)
- AMS color test shows dimensional inconsistency between filament colors

**Decision**: Do NOT proceed to Etsy launch. Execute Failure Path recovery instead.

---

### Failure Mode Diagnostic Tree

#### **Failure Category A: Jaw Gap Out of Spec**

**Symptoms**: Hook rocks side-to-side when clamped, or won't slide onto test desk edge, or slides too freely (>3mm play).

**Diagnosis checklist**:
1. **Measure actual desk thickness**: Use calipers. Is it really 12mm / 25mm / 40mm as assumed?
   - If desk is non-standard (e.g., 18mm), recalibrate the tolerance script
2. **Check FDM tolerance**: Reread headphone-hooks-design-spec.md Section 2. Did you use FDM_TOLERANCE=0.20mm in the print?
   - If you modified the tolerance constant before printing, note the value used
3. **Check Bambu slicer settings**: Confirm layer height was 0.20mm, infill 25% gyroid, 3 perimeters
   - If you deviated (e.g., 0.24mm layer height), recalibrate estimate
4. **Test fit on actual desk edge**: Clamp the hook onto your desk. Does it clamp smoothly without rocking?

**Recovery Actions** (timeline varies by path):

| Root Cause | Recovery | Timeline |
|---|---|---|
| **Jaw gap too tight** | Increment `--tolerance` by 0.05mm. Reprint 1 validation clip. Measure and retest. | 30 min (if you reprint immediately) |
| **Jaw gap too loose** | Reduce FDM_TOLERANCE constant in headphone_hooks.py to 0.10mm. Regenerate STL, reprint validation clip. | 30 min |
| **Desk thickness assumption wrong** | Measure your desk with calipers. Update the tolerance script with actual desk thickness. Regenerate STL and reprint. | 30 min |
| **Slicer settings deviated** | Return to default Bambu Studio profile (0.20mm layer, 25% infill, 3 perimeters, 200mm/s outer). Reprint validation clip. | 30 min |
| **Multiple factors (tight + wrong desk)** | Test fit on **multiple desk thicknesses** (borrow a friend's desk, or test on different edges of your own desk). Isolate which dimension is the issue. Then adjust tolerance and reprint. | 1 hour |

**Decision point**: If fix is <0.05mm adjustment:
- ✅ **Proceed**: Reprint with corrected setting, confirm fit, then execute Success Path starting Day 1 (May 24 or May 25)
- Launch delay: 1 day

If fix requires >2 iterations or material change (PLA+ → PETG):
- ⏸️ **Defer**: Acknowledge structural issue, plan for Phase 2 hardware tuning, defer Etsy launch to June 3 post-Phase-1-validation
- Launch delay: 8+ days

---

#### **Failure Category B: Snap Arm Thickness Out of Spec**

**Symptoms**: Test cable wraps loosely around arm with >2cm slack, or arm is visibly thinner than 1.4mm spec.

**Diagnosis checklist**:
1. **Measure snap arm thickness**: Use calipers (measure three points along the 55mm arm length). Record all three values.
2. **Check Bambu slicer**: Confirm layer height 0.20mm, **perimeter count = 3** (critical)
   - This is the most common issue: reduced perimeter count → thinner walls
3. **Confirm nozzle size**: Is it 0.4mm? (If you swapped to 0.6mm nozzle, geometry changes)
4. **Recheck STL generation**: Did you run `modrun_cable_management_hooks.py` with default parameters?

**Recovery Actions**:

| Root Cause | Recovery | Timeline |
|---|---|---|
| **Perimeter count <3** | Set to 3 perimeters in Bambu slicer. Reprint test clip. | 30 min |
| **Layer height too high** | Confirm 0.20mm layer height. If you used 0.24mm or 0.30mm, revert. Reprint. | 30 min |
| **Nozzle diameter mismatch** | Confirm 0.4mm nozzle. If using 0.6mm, run slicer preview with correct nozzle diameter. Adjust infill if needed. | 15 min |
| **STL generation error** | Regenerate STL: `uv run python modrun_cable_management_hooks.py --output-dir ../stl/` | 10 min |

**Decision point**: 
- ✅ **Proceed with reprint**: Single setting fix, reprint validation clip, measure, confirm. Launch delay: 1 day.
- ⏸️ **Defer to Phase 2**: If arm thickness issue is systematic (multiple test prints fail), acknowledge it and defer to June 3. Use Phase 2 to source PETG (better flex fatigue).

---

#### **Failure Category C: Cable Post Diameter Out of Spec**

**Symptoms**: Test cables slip around the post without grip, or post is visibly thicker/thinner than 8mm.

**Diagnosis checklist**:
1. **Measure post diameter**: Use digital calipers on three points (top, middle, bottom of post). Record all values.
2. **Test cable fit**: Try a 4mm audio cable, 5mm USB-C, 6mm USB-A. Does each loop around post with 5–10mm clearance?
3. **Check STL generation**: Was a non-default cable post diameter specified?

**Recovery Actions**:

| Root Cause | Recovery | Timeline |
|---|---|---|
| **Filament diameter variance** | Cable post is undersized due to filament being <1.75mm. This is material-specific. Use a different filament spool. Reprint. | 30 min |
| **Dimensional drift from thermal stress** | If post printed correctly but cables don't fit, check: Is the desk clamp too tight? (clamp stress can distort adjacent features). Try fitting on a different test desk with less clamp pressure. | 20 min |
| **STL generation error** | Confirm cable post radius = 4mm in the script. Regenerate STL if needed. | 10 min |

**Decision point**:
- ✅ **Proceed**: If reprint with different filament spool resolves it, launch delay: 1 day.
- ⏸️ **Defer**: If post diameter issue is systematic, add to Phase 2 CAD refinement (post diameter +0.5mm design change).

---

#### **Failure Category D: Rubber Pad Pocket Depth Out of Spec**

**Symptoms**: Silicone bumper (1.5mm 3M Bumpon) sits proud of the pocket (protruding >0.5mm), or doesn't fit in pocket at all.

**Diagnosis checklist**:
1. **Measure pocket depth**: Use calipers or feeler gauge on both upper and lower jaw pockets.
2. **Test bumper fit**: Press a 3M SJ5302 bumper into the pocket. Does it sit flush?
3. **Check slicer top/bottom layer count**: Confirm 4 top/4 bottom layers (responsible for flat pocket surfaces).

**Recovery Actions**:

| Root Cause | Recovery | Timeline |
|---|---|---|
| **Top layers insufficient** | Set top/bottom layers = 4 in slicer. Reprint test section. | 30 min |
| **First layer height too high** | Confirm first layer = 0.25mm. If >0.25mm, reduce and reprint. | 15 min |
| **Pocket itself is filled (slicer error)** | Check STL file visually (preview in Bambu Studio mesh view). If pocket shows as filled, regenerate STL. | 10 min |

**Decision point**:
- ✅ **Proceed**: Rubber pad fit is cosmetic/comfort — not load-bearing. If pocket is <1.2mm and bumper doesn't fit, you can: (a) reprint with corrected slicer settings, OR (b) note on Etsy listing "rubber bumpers not included — customer can add" (alternative: use permanent adhesive bumpers, slightly lower comfort). Launch delay: 0 days (can launch without bumpers, add in Week 2).

---

#### **Failure Category E: Layer Separation or Adhesion Defects**

**Symptoms**: Visible gaps between layers, warping on the hook arm or clamp back, nozzle damage marks on the print surface, or any print failure (incomplete print, broken supports if any used).

**Diagnosis checklist**:
1. **Inspect for layer lines**: Are they clean and evenly spaced, or are there visible gaps/delamination?
2. **Check bed adhesion**: Is the back plate securely adhered, or is it lifting at edges?
3. **Inspect nozzle**: Is the Bambu nozzle clean, or is there filament buildup?
4. **Confirm print completed**: Did the print finish fully, or did it stop mid-print?

**Recovery Actions**:

| Root Cause | Recovery | Timeline |
|---|---|---|
| **Nozzle is dirty** | Clean nozzle with a soft brass brush while cold (or hot if filament is molten). Run Bambu nozzle cleaning cycle. Reprint. | 15 min |
| **Bed temperature too low** | Confirm bed = 60°C for PLA+. If you set it lower, Bambu will auto-adjust on next print. Reprint. | 30 min |
| **Filament quality (moisture)** | If filament was exposed to humidity, dry it in an oven (40°C, 2 hours) or use a dry box. Reprint with dry filament. | 2+ hours |
| **Print failed mid-way** | Check Bambu logs for error. Power off printer, clear build plate, reload STL, restart print. | 30 min |
| **Warping on back plate** | Increase bed temp to 65°C or add brim (4mm, already specified for tall variants). Reprint. | 30 min |

**Decision point**:
- ✅ **Proceed**: Most adhesion issues are one-time (nozzle buildup, bed temp). Reprint once with corrected setting. Launch delay: 1 day.
- ⏸️ **Defer**: If print failures are systematic or nozzle is damaged, plan Bambu nozzle replacement (cost: $3–5, lead time: 2–3 days if ordered).

---

#### **Failure Category F: AMS Color Test Inconsistency**

**Symptoms**: Second or third filament color shows dimensional drift (e.g., jaw gap is 12.4mm for black, but 13.0mm for white due to AMS spool diameter variance).

**Diagnosis checklist**:
1. **Measure prints from each AMS spool**: 
   - Print A (black) jaw gap: ___mm
   - Print B (white) jaw gap: ___mm
   - Print C (grey) jaw gap: ___mm
2. **Are differences >0.3mm between colors?** If yes, flag this.
3. **Check AMS tension**: Is the white/grey spool tension as tight as the black spool?

**Recovery Actions**:

| Root Cause | Recovery | Timeline |
|---|---|---|
| **AMS spool tension drift** | Adjust AMS tension for the non-black spools. Reprint all three colors. Verify consistency. | 45 min |
| **Filament diameter variance (vendor issue)** | Contact filament vendor (eSUN, Bambu). Note spool batch numbers. Meanwhile, proceed with single-color (black) launch. | Defer to Phase 2 |

**Decision point**:
- ✅ **Proceed with black only**: Launch listing in black only on May 29. Add note: "White and Grey available soon — message shop for timeline". This is **not** a blocker. Most buyers are indifferent to color at launch. Add variants in Week 2 once AMS consistency is confirmed.
- Launch delay: 0 days

---

### Failure Path Timeline Decision Tree

```
Test print complete?
├─ All 6 parameters PASS
│  └─→ SUCCESS PATH (May 23-30, launch May 29)
│
└─ Any 1+ parameters FAIL
   ├─ Jaw gap out of spec?
   │  ├─ Fix: rerun with ±0.05mm tolerance adjustment → 1-day delay, relaunch May 30
   │  └─ Fix: requires PETG or redesign → 8-day delay, relaunch June 3
   │
   ├─ Snap arm thickness out of spec?
   │  ├─ Fix: increase perimeter count to 3 → 1-day delay
   │  └─ Fix: systematic issue → defer to Phase 2, relaunch June 3
   │
   ├─ Cable post diameter out of spec?
   │  ├─ Fix: use different filament spool → 1-day delay
   │  └─ Fix: systematic → defer to Phase 2 (design +0.5mm)
   │
   ├─ Rubber pad pocket out of spec?
   │  ├─ Fix: adjust top layer count → 1-day delay OR relaunch without bumpers (0-day delay, add Week 2)
   │  └─ Acceptable workaround → proceed anyway, add bumpers later
   │
   ├─ Layer separation / adhesion defects?
   │  ├─ Fix: nozzle cleaning, bed temp adjustment → 1-day delay
   │  └─ Fix: nozzle damage, filament quality → 2–3-day delay
   │
   └─ AMS color variance?
       ├─ Fix: single-color (black) launch → 0-day delay, add colors Week 2
       └─ Fix: AMS tension adjustment → 1-day delay, multi-color launch May 30
```

---

### Failure Path Recovery Checklists

#### **1-Day Recovery** (May 23 test print fails → May 24 reprint ready → May 30 launch)

✅ Jaw gap adjustment (±0.05mm tolerance)
✅ Snap arm perimeter correction
✅ Cable post filament swap
✅ Rubber pad slicer correction
✅ Nozzle cleaning + bed temp fix
✅ AMS tension rebalance

| Day | Action | Duration |
|---|---|---|
| May 23 (afternoon) | Identify failure mode, determine fix | 30 min |
| May 24 (morning) | Implement fix, run slicer preview | 30 min |
| May 24 (afternoon) | Reprint, measure, validate | 90 min |
| May 25–29 | Proceed with Success Path (5-day countdown starting May 25) | — |
| May 30 | **Etsy launch** | — |

---

#### **3-Day Recovery** (May 23 test print fails → May 26 new approach ready → June 1 launch)

⚠️ Filament drying required (moisture issue)
⚠️ Nozzle replacement needed
⚠️ AMS color variance + black-only launch

| Day | Action | Duration |
|---|---|---|
| May 23 (afternoon) | Identify issue, plan dry box prep | — |
| May 24–25 | Dry filament (oven 40°C, 2–4 hrs) OR order replacement nozzle | — |
| May 26 (morning) | Reprint with corrected filament/nozzle | 90 min |
| May 26 (afternoon) | Measure, validate, begin Success Path | — |
| May 27–June 1 | Execute 5-day countdown | — |
| June 1 | **Etsy launch** | — |

**Note on June 1 launch**: The May 29 optimal recency window is lost. June 1 is a Sunday (lower traffic). Consider scheduling for Monday June 2 morning if you finish validation by June 1 afternoon.

---

#### **8-Day Deferral** (May 23 test print fails → June 3 launch after Phase 1 validation)

🔴 Jaw gap structural issue (requires redesign or PETG material)
🔴 Systematic print failures (equipment issue)
🔴 AMS completely non-functional (color variance >0.5mm)

**Action**: Acknowledge Phase 1 test print did not meet production specs. Defer Etsy launch and use May 24–June 2 to:
1. Redesign or material upgrade
2. Retest with corrected approach
3. Validate on actual customer desks
4. Launch June 3 post-Phase-1-validation with higher confidence

**Benefit**: Phase 1 validation (May 22–June 2) uncovers fundamental issues before they cause customer returns. Better to defer launch 5 days and ship a product that works than to launch May 29 with a defective hook.

---

## Part 3: Success Path vs. Failure Path Comparison

| Dimension | Success Path | 1-Day Recovery | 3-Day Recovery | 8-Day Deferral |
|---|---|---|---|---|
| **Etsy Launch Date** | May 29 (Thursday) | May 30 (Friday) | June 1 (Sunday) | June 3 (Tuesday) |
| **Days Lost** | 0 | 1 | 3 | 5 |
| **Recency Boost Window** | Optimal (Thu 10 AM) | Good (Fri 10 AM) | Fair (Sun, lower traffic) | Fair (Tue) |
| **Required Actions** | None (test print passes) | 1 slicer/tolerance fix + reprint | Filament dry/nozzle replace + reprint | Redesign or material change + full retest |
| **Confidence in Production** | High | High | High | Very high (validated on Phase 1) |
| **Launch Inventory Ready** | May 27 (4 days pre-launch) | May 28 (2 days pre-launch) | May 31 (1 day pre-launch) | June 2 (1 day pre-launch) |

---

## Appendix: Quick Reference — Decision Triggers

### When to Execute Success Path
- ✅ All 6 tolerance parameters within spec
- ✅ Photos are clear and well-lit
- ✅ Margin ≥60%
- → **Proceed immediately to May 23 afternoon execution**

### When to Execute 1-Day Recovery
- ⚠️ 1 parameter out of spec by <0.1mm
- ⚠️ Fix requires only slicer setting change or tolerance script adjustment
- ⚠️ Filament behaves normally (no adhesion, no nozzle damage)
- → **Reprint May 24 morning, launch May 30**

### When to Execute 3-Day Recovery
- ⚠️ Filament shows moisture (incomplete prints, layer gaps)
- ⚠️ Nozzle is damaged (cost: $5, lead time: 2–3 days if ordered)
- ⚠️ AMS color variance (use black-only, add colors Week 2)
- → **Plan for May 26 reprint, launch June 1 or June 2**

### When to Execute 8-Day Deferral
- 🔴 Jaw gap >0.2mm out of spec (structural, not quick fix)
- 🔴 Systematic print failures (3+ failed attempts to correct)
- 🔴 Material inadequacy discovered (PLA+ insufficient, needs PETG)
- → **Acknowledge Phase 1 validation blocker, defer to June 3 post-hardware-upgrade**

---

**Owner**: User (decision gate + physical execution) | Orchestrator (timeline planning, checklist generation)

**Next step**: Execute test print May 23 morning. By afternoon, determine success vs. failure path and proceed accordingly.
