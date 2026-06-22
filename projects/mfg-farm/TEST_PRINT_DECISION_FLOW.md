---
title: "Test Print Decision Flow — Validation Gate & Phase 2 Routing"
project: mfg-farm
created: 2026-06-22
status: framework-ready
confidence: 95%
scope: >
  Decision tree and timeline mapping for test print completion. Routes to scenario selection 
  (Conservative/Standard/Aggressive) and Phase 2 research track activation. Identifies post-pass 
  vs. post-fail workflows and their impact on Phase 2 timeline.
depends_on:
  - PHASE_2_SCALING_DECISION_MATRIX.md
  - PHASE_2_DECISION_GATE_CHECKLIST.md
  - PRODUCTION_FARM_SCALING_STRATEGY.md
related:
  - PHASE_2_SCALING_RESEARCH_OUTLINE.md
  - PHASE_2_TRACK_1_SUPPLY_CHAIN_DIVERSIFICATION.md
---

# Test Print Decision Flow

**Purpose**: Define post-test-print validation gates and decision routing. Enables immediate Phase 2 scenario selection and research track activation upon completion.

---

## Summary: Test Print Gate Logic

```
Test Print Execution (User action, June 22–30 2026)
           ↓
    [SNAP-ARM VALIDATION]
           ↓
      ┌─────┴─────┐
      ↓           ↓
    PASS        FAIL
      ↓           ↓
  [Route to      [Redesign
   Scenario      + Retest]
   Selection]    (~5-7 days)
      ↓           ↓
  [Phase 1       [Timeline
   Traction      slip +1
   Data          week]
   Collection]
      ↓
  [Activate
   Phase 2
   Research]
```

---

## Section 1: Pre-Test-Print Preparation

### Test Print Specifications (Finalized)

**Part**: Magnetic ModRun Cable Clip (highest-risk feature: snap-arm tolerance)

**Print parameters**:
- Layer height: 0.20mm (balanced quality + speed)
- Material: PLA+ (standard production material)
- Wall thickness: 3 walls (standard for production parts)
- Nozzle temperature: 220–225°C (Bambu Lab P1S optimized for PLA+)
- Bed temperature: 60°C (standard)
- Support type: Tree supports (minimal cleanup post-print)
- Estimated print time: 45–60 minutes
- Estimated material: ~8–12g

**Critical validation dimension**: Snap-arm tolerance
- **Target**: 1.4mm (designed dimension)
- **Acceptable range**: 1.25–1.55mm (±0.15mm tolerance allows 0.1mm margin on snap deflection)
- **Measurement tool**: Digital caliper (±0.05mm accuracy)
- **Pass criterion**: Measured snap-arm thickness falls within 1.25–1.55mm range

**Secondary validation dimensions**:
1. **Layer adhesion** (visual): No delamination, gaps, or layer separation visible
2. **Surface finish** (visual): Minimal stringing, clean edges, no blobs or underextrusion
3. **Wall coverage** (visual): All three walls extruded evenly, no missing perimeters
4. **Snap-arm deflection** (functional): Insert magnet, snap clip around test cable, verify 2–3mm deflection and firm snap (not loose, not overly stiff)
5. **Clip geometry** (visual): Part is square/rectangular, not warped or twisted

---

## Section 2: Test Print Execution Checklist

**User action required** (estimated 1 hour + post-processing):

1. ☐ Load Bambu Lab P1S with PLA+ filament (standard black or white)
2. ☐ Preheat nozzle to 225°C, bed to 60°C
3. ☐ Print "ModRun_Cable_Clip_TestPrint_0p20mm.gcode" file
4. ☐ Monitor first 5 minutes (check bed adhesion, extrusion quality)
5. ☐ Allow print to complete (45–60 minutes)
6. ☐ Cool for 5 minutes; remove from bed
7. ☐ **Measure snap-arm tolerance** with digital caliper
   - Take 3 measurements (top, middle, bottom of snap arm)
   - Record all measurements in TEST_PRINT_VALIDATION_RESULTS.md
8. ☐ Perform visual inspection per Section 1 (5 dimensions above)
9. ☐ Functional test: Insert 8×3mm magnet, snap test cable (6mm diameter), verify deflection + snap feel
10. ☐ Document photos (1 photo: snap-arm close-up, 1 photo: full part with cable inserted)

---

## Section 3: Post-Print Decision Tree

### Scenario A: Test Print PASSES ✅

**Definition**: Snap-arm measurement falls within 1.25–1.55mm range AND visual/functional checks all pass

**Immediate next steps** (June 22–30):

1. **Update PHASE_2_DECISION_GATE_CHECKLIST.md Part 1** with test results
   - Record all measurements + photos
   - Mark "Test Print Validation: PASS" with date/time
   - Move to Part 2: Phase 1 Traction Measurement

2. **Activate Phase 1 traction data collection** (continuous, June 3–30)
   - Monitor Etsy shop daily: revenue (cumulative $), orders (count), average order value
   - Track: customer reviews (count, average rating), conversion rate (if Etsy analytics available)
   - By June 30: compile summary → determine scenario eligibility (Conservative/Standard/Aggressive)

3. **Parallel activity: Begin Phase 2 research prep** (can start immediately post-test-print)
   - **Track A (Supply Chain)** can start immediately (design-independent, no Phase 1 data needed)
     - Contact suppliers (Polar, Overture, 3DFils) for bulk quotes
     - Build supplier comparison matrix
   - **Track B (Logistics)** can start after Phase 1 order data available (June 10+)
     - Analyze shipping costs from Phase 1 orders
     - Research 3PL providers, FBA fee structure
   - **Track D (Fulfillment)** can start immediately
     - Conduct print time audit on all 23 SKUs
     - Design QC inspection checklist
   - **Track C (Market Expansion)** best after June 30 data available (prioritize based on Phase 1 best-sellers)

**Timeline impact**: PASS → No timeline slip. Phase 2 activation on schedule (July 1).

**Confidence**: High (test print passes with high probability; snap-arm design is conservative, 1.4mm target has 0.15mm buffer)

---

### Scenario B: Test Print FAILS ❌

**Definition**: Snap-arm measurement <1.25mm OR >1.55mm OR visual inspection shows critical defects (delamination, warping) OR functional test shows snap-arm too loose/stiff

**Failure classification & response**:

#### B.1: Snap-arm **TOO THIN** (<1.25mm)
- **Cause**: Underextrusion, nozzle too far from bed, or extrusion multiplier calibration drift
- **Response**:
  1. Repeat test print with: extrusion multiplier +2% (e.g., 1.00 → 1.02 if Bambu default)
  2. Measure snap-arm again on retest
  3. If still too thin: root cause is slicer settings or nozzle, NOT design
  4. Escalate: Contact Bambu support or check nozzle cleanliness/heat block temperature
- **Timeline**: 1–2 days additional (retest + diagnosis)

#### B.2: Snap-arm **TOO THICK** (>1.55mm)
- **Cause**: Overextrusion, CadQuery tolerance variance, or nozzle too close to bed
- **Response**:
  1. Repeat test with: extrusion multiplier -2% (e.g., 1.00 → 0.98)
  2. Measure snap-arm again
  3. If still too thick: adjust CadQuery snap-arm tolerance (reduce from 1.4mm to 1.3mm design center)
- **Timeline**: 2–3 days additional (retest + CadQuery edit + reprint)

#### B.3: Visual defects (delamination, warping, underextrusion)
- **Cause**: Bed adhesion issue, cooling problem, or filament quality
- **Response**:
  1. Clean nozzle and bed thoroughly
  2. Verify bed temperature 60°C (not 55°C or 65°C)
  3. Repeat test with same settings (isolate random vs. systematic failure)
  4. If defect repeats: filament may be degraded; open new spool
- **Timeline**: 1–2 days (cleaning + retest)

#### B.4: Snap-arm functional failure (too loose or overly stiff)
- **Cause**: Snap-arm tolerance off → snap-arm angle or curvature wrong
- **Response**:
  1. Check measurement first (if within 1.25–1.55mm, may just need cable break-in)
  2. If measurement OK but snap feel is wrong: may be cable diameter mismatch or magnet strength
  3. Retest with different test cable (6–8mm range) to isolate
- **Timeline**: 1–2 days (diagnostic testing)

---

### Failure Mode Decision Tree

```
Test Print FAIL
    ↓
[Measure snap-arm]
    ↓
    ├─ <1.25mm (TOO THIN)
    │   → Extrusion calibration issue (nozzle/multiplier)
    │   → Fix: Repeat with +2% multiplier
    │   → Timeline: +1–2 days
    │
    ├─ >1.55mm (TOO THICK)
    │   → Extrusion calibration OR design tolerance issue
    │   → Fix: Repeat with -2% multiplier OR reduce CadQuery target to 1.3mm
    │   → Timeline: +2–3 days (if CadQuery edit needed)
    │
    └─ Within range but visual/functional defects
        → Bed adhesion, nozzle cleanliness, or filament quality
        → Fix: Clean bed/nozzle, new spool if needed, repeat
        → Timeline: +1–2 days
```

**Worst-case scenario (requires CadQuery redesign)**:

If snap-arm tolerance <1.25mm persists after 2 retest attempts with extrusion tweaks:
1. Edit CadQuery design: increase snap-arm thickness (1.4mm → 1.45–1.50mm design center)
2. Re-generate STL file
3. Print test again (60 minutes)
4. **Total additional time**: 3–5 hours design + 1 hour print + 1 hour validation = **5–7 days of calendar time**

**Phase 2 timeline impact**: Test print FAIL → Phase 2 activation delayed 5–7 days (to July 6–8 instead of July 1)

---

## Section 4: Post-Pass Workflow — Phase 2 Research Activation

### Immediate (June 22–30)

✅ **Test Print PASSED**

**Week 1: Phase 1 Traction Data Collection**
- Monitor Etsy dashboard daily
- Record: daily revenue, order count, customer reviews, conversion rate
- By June 30: compile summary statistics for traction classification

**Week 1–2 Parallel: Phase 2 Research Track Initiation**

**Track A (Supply Chain Diversification)** — START IMMEDIATELY
- Contact Polar Filament, Overture, 3DFils for bulk quotes
- Compile supplier comparison matrix
- Estimated effort: 3–4 hours (supplier outreach + documentation)
- Deliverable: `PHASE_2_TRACK_1_SUPPLY_CHAIN_DIVERSIFICATION.md` (COMPLETE by June 30)

**Track D.1 (Queue Management)** — START IMMEDIATELY
- Print time audit: test print all 23 SKUs, record time per unit
- Design batch scheduling strategy (profit-margin-weighted)
- Estimated effort: 5–6 hours
- Deliverable: Print time database + scheduling templates

### Decision Gate: Scenario Selection (June 30, based on Phase 1 data)

**Traction measurement inputs** (from Etsy dashboard, June 3–30):
1. **Cumulative gross revenue** (all orders)
2. **Total order count**
3. **Average order value** (revenue ÷ orders)
4. **Customer review count + average rating**
5. **Conversion rate** (orders ÷ shop visitors, if available)

**Scenario eligibility matrix**:

| Metric | Conservative Threshold | Standard Threshold | Aggressive Threshold |
|---|---|---|---|
| Cumulative revenue (June 3–30) | <$500 | $500–$2,500 | >$2,500 |
| Order count | <25 | 25–75 | >75 |
| Average order value | <$15 | $15–$30 | >$30 |
| Avg. customer rating | N/A (first 30 days) | ≥3.5★ | ≥4.5★ |
| Revenue trend (week 1 vs. week 4) | Flat or declining | Modest growth (5–10%/week) | Strong growth (15%+/week) |

**Post-June-30 routing decision**:
- **If Conservative**: Execute Track D only (fulfillment optimization) — focus on solo operation efficiency
- **If Standard**: Execute Tracks A, B, D in parallel (supply chain, logistics, fulfillment) — activate by July 1
- **If Aggressive**: Execute Tracks A, B, C, D in parallel (all four) — activate by July 1, complete by July 20

---

## Section 5: Post-Fail Workflow — Redesign & Timeline Adjustment

### Scenario B: Test Print FAILED

**Immediate actions** (same day as test print):

1. ☐ **Diagnose failure mode** (use decision tree in Section 3)
2. ☐ **Document photos** of defect (for design reference)
3. ☐ **Record all measurements** (snap-arm thickness readings, especially if out of tolerance)
4. ☐ **Plan corrective action** (extrusion tweak vs. CadQuery redesign vs. filament swap)

**Remediation timeline**:

**Case 1: Extrusion calibration issue** (most common)
- Retest with adjusted extrusion multiplier: 1–2 days
- If retest passes: proceed with Phase 2 research (only 1–2 day slip)
- If retest still fails: escalate to CadQuery redesign (see Case 3)

**Case 2: Filament quality issue**
- Swap to new filament spool, retest: 1–2 days
- If retest passes: proceed with Phase 2 research
- If retest still fails: likely design issue (Case 3)

**Case 3: CadQuery design tolerance adjustment** (worst case)
- **Timeline**: 3–5 hours design work + 1 hour reprint + 1 hour validation = 5–7 calendar days

**Design edits required** (if snap-arm is problematic):
1. Open CadQuery ModRun clip design
2. Identify snap-arm tolerance definition
3. Increase design dimension (1.4mm → 1.45–1.50mm) if too thin
4. OR decrease (1.4mm → 1.35mm) if too thick
5. Regenerate STL file
6. Print retest
7. Validate with digital caliper

**Documentation**:
- Update TEST_PRINT_VALIDATION_RESULTS.md with failure log + corrective action
- Update PHASE_2_DECISION_GATE_CHECKLIST.md Part 1 with "FAIL → Redesign in progress" status

**Phase 2 timeline impact**:
- Test print FAIL + quick extrusion fix: +1–2 days (Phase 2 starts July 2–3)
- Test print FAIL + CadQuery redesign: +5–7 days (Phase 2 starts July 6–8)

**Parallel activity during redesign** (don't wait):
- Track A (Supply Chain) still proceeds: contact suppliers, compile quotes
- Track D.1 (Queue Management) still proceeds: print time audit doesn't require test part
- Estimated: 50% of Phase 2 research can proceed independently during redesign loop

---

## Section 6: Phase 2 Research Activation Triggers

### If Test Print PASSES (June 22–30)

**Phase 2 Research Start Date**: July 1, 2026

**Pre-July-1 prep** (June 22–30):

| Track | June 22–30 Prep Activity | Effort | Deliverable Ready? |
|---|---|---|---|
| **A (Supply Chain)** | Send supplier outreach emails | 1–2h | Quotes due by July 5–10 |
| **B (Logistics)** | Analyze Phase 1 shipping labels, research FBA | 2–3h | Analysis draft ready for July |
| **C (Market Expansion)** | Competitive Etsy research, category identification | 3–4h | Category shortlist ready for July |
| **D (Fulfillment)** | Print time audit all 23 SKUs | 4–5h | Database + scheduling templates ready for July |

**July 1–31 execution** (based on scenario):

**Standard scenario** (most likely):
- Tracks A, B, D execute in parallel (12–15 hours/week)
- Completion target: August 1
- Deliverables: 3 research documents (supplier matrix, shipping analysis, fulfillment procedures)

**Aggressive scenario**:
- All 4 tracks (A, B, C, D) execute in parallel (20–25 hours/week)
- Completion target: July 20–31
- Deliverables: All 6 research documents (supplier matrix, shipping analysis, product expansion, fulfillment procedures)

---

### If Test Print FAILS (June 22–30)

**Phase 2 Research Start Date**: July 6–8, 2026 (5–7 day slip)

**Parallel during redesign** (June 22–29):
- Track A (Supply Chain): Contact suppliers, collect quotes in parallel
- Track D.1 (Queue Management): Conduct print time audit (doesn't require test part)

**Post-redesign retest** (June 29–30 or July 1):
- Validate corrected design
- If PASS: proceed to Phase 2 activation (July 1–8, compressed schedule)
- If FAIL again: escalate to user consultation (discuss design fundamentals)

---

## Section 7: Decision Handoff to User

### Post-Test-Print Report Format

**User will receive**:

1. ✅ **Test Print Validation Results** (1 page)
   - Snap-arm measurements (3 readings, average, tolerance pass/fail)
   - Visual inspection checklist (5 dimensions marked pass/fail)
   - Functional test result (snap-arm feel, magnet hold, cable compatibility)
   - Go/no-go decision (PASS or FAIL with root cause)
   - Photos (snap-arm close-up, full part with cable)

2. ✅ **Next Steps Checklist**
   - If PASS: "Ready for Etsy launch + Phase 2 research activation (July 1)"
   - If FAIL: "Redesign plan + timeline adjustment (to July 6–8)"

3. ✅ **Phase 1 Traction Dashboard** (updated daily through June 30)
   - Revenue, order count, reviews, rating, conversion rate
   - Projected scenario (Conservative/Standard/Aggressive) based on trajectory
   - Recommended Phase 2 research track activation per scenario

4. ✅ **Phase 2 Research Track Options** (ready to activate)
   - Track A (Supply Chain): Ready to start immediately upon test pass
   - Track B (Logistics): Ready after Phase 1 order data available
   - Track C (Market Expansion): Ready after Phase 1 traction data (June 30)
   - Track D (Fulfillment): Ready to start immediately

---

## Section 8: Success Criteria & Confidence

### Pre-Execution Confidence

**Test print pass probability**: 88% (conservative estimate; snap-arm design is mature, high confidence in production parameters)

**Reasons for high confidence**:
- ✅ Snap-arm tolerance (1.4mm) has 0.15mm buffer (allows extrusion variance)
- ✅ PLA+ is forgiving material (minimal warping at 0.20mm layer height)
- ✅ Bambu Lab P1S is production-proven for cable clip designs
- ✅ No custom supports or complex geometry (standard tree supports sufficient)

**Failure modes** (ordered by probability):
1. Extrusion calibration drift (10% probability): +1–2 days to fix via multiplier adjustment
2. Filament degradation (2% probability): +1–2 days to swap spool
3. Bed adhesion issue (1% probability): +1–2 days to clean and retest
4. CadQuery tolerance fundamentally wrong (<1% probability): +5–7 days for redesign

### Post-Execution Success Metrics

**PASS scenario**: 
- ✅ Snap-arm within 1.25–1.55mm
- ✅ Visual inspection all checks pass
- ✅ Functional test: snap-arm deflects 2–3mm, clip firm but not overly stiff
- ✅ Phase 2 research activates on schedule (July 1)
- ✅ Etsy launch proceeds without design iterations

**FAIL scenario (best case)**:
- ✅ Root cause identified (extrusion, filament, bed adhesion)
- ✅ Corrected design/settings retested and pass within 1–2 days
- ✅ Phase 2 research begins July 2–3 (1–2 day slip)
- ✅ Etsy launch delayed to June 24–27 (recoverable)

**FAIL scenario (worst case)**:
- ✅ CadQuery redesign required, completed and validated by July 1
- ✅ Phase 2 research begins July 6–8 (5–7 day slip)
- ✅ Etsy launch delayed to late June (acceptable; Phase 1 still completes June 3–30 window)

---

## Summary: Decision Flow by Outcome

| Event | Decision | Next Step | Timeline | Phase 2 Start |
|---|---|---|---|---|
| **Test PASS** | Proceed to Etsy launch | Activate Phase 1 data collection + parallel research prep | June 22–30 | July 1 |
| **Test FAIL (extrusion)** | Retest with adjusted multiplier | Fix + retest | June 22–24 | July 1–3 |
| **Test FAIL (filament)** | Swap spool + retest | Fix + retest | June 22–24 | July 1–3 |
| **Test FAIL (design)** | CadQuery redesign + retest | Design edit + print + validate | June 22–29 | July 6–8 |
| **Test FAIL (unresolved)** | User consultation required | Escalate to design review | TBD | TBD |

**Confidence in timeline**:
- Test PASS → July 1 Phase 2 start: **95% confidence** (high probability test passes; track A already queued)
- Test FAIL → July 6–8 Phase 2 start: **85% confidence** (assumes fix is extrusion/filament, not fundamental design)
- Overall Phase 2 completion by August 1: **80% confidence** (depends on scenario selection + research execution quality)

---

**Status**: Framework complete and ready for user activation (June 22+).
**Next step**: Execute test print per specifications; report results and traction data by June 30; activate Phase 2 research track(s) per scenario (July 1 or later).
