---
title: Post-Test-Print Etsy Launch Sequence
project: mfg-farm
created: 2026-05-19
scope: Decision framework and execution timelines based on test print outcomes
version: 1.0
---

# Post-Test-Print Etsy Launch Sequence

**Purpose**: Maps test print outcomes to specific Etsy launch actions, timelines, and decision points. Enables rapid execution of the May 29-Jun 2 launch window once test print results are available.

**Test Print Baseline** (user will execute):
- Layer height: 0.20 mm
- Material: PLA+
- Wall count: 3
- Nozzle temp: 220–225°C
- Print time: ~90 min per unit

---

## Part 1: Test Print Success Criteria

The test print passes if ALL of the following are true:

### 1.1 Visual Inspection (Critical Path)
- ✅ Snap-arm shows no cracks, splits, or stress marks (white discoloration)
- ✅ Rail grip surfaces are smooth with no layer separation
- ✅ Cable post is straight with no visible wobble or cracks
- ✅ Overall dimensions appear consistent with CAD preview

### 1.2 Dimensional Verification (Critical Path)
| Dimension | CAD Spec | Tolerance | Result Required |
|-----------|----------|-----------|-----------------|
| Snap-arm thickness | 1.4 mm | ±0.15 | **1.25–1.55 mm** (HIGHEST RISK) |
| Snap-arm length | 16.2 mm | ±0.2 | 16.0–16.4 mm |
| Rail jaw opening | 7.8–8.2 mm | var | Within range |
| Cable post diameter | 8.0 mm | ±0.3 | 7.7–8.3 mm |
| Cable post height | 12.0 mm | ±0.2 | 11.8–12.2 mm |
| Overall width | 14.0 mm | ±0.3 | 13.7–14.3 mm |

**CRITICAL THRESHOLD**: Snap-arm thickness <1.25 mm or >1.55 mm = design iteration required.

### 1.3 Functional Tests (Critical Path)
- ✅ **Snap-arm flex**: Flexes smoothly under thumb pressure; returns to original position without cracking
- ✅ **Rail grip (dry test)**: Grips ModRun rail securely; no slipping when pulled horizontally
- ✅ **Cable post stability**: Post stays straight under moderate cable tension; <2 mm deflection

**PASS THRESHOLD**: All three functional tests pass = ready for immediate Etsy launch.

---

## Part 2: Decision Tree & Outcome Branches

```
TEST PRINT INSPECTION
│
├─ BRANCH A: ALL TESTS PASS (Snap-arm 1.25–1.55 mm, functional tests green)
│  └─ OUTCOME: PROCEED TO IMMEDIATE ETSY LAUNCH (May 25-29)
│
├─ BRANCH B: SNAP-ARM TOLERANCE OUT OF RANGE (1.25–1.55 mm threshold violated)
│  ├─ Sub-branch B1: <1.25 mm (under-thick)
│  │  └─ ACTION: Minor design iteration (5-7 days), reschedule launch to June 2-5
│  │
│  └─ Sub-branch B2: >1.55 mm (over-thick)
│     └─ ACTION: Minor design iteration (5-7 days), reschedule launch to June 2-5
│
├─ BRANCH C: SNAP-ARM FAILURE (cracks, stress marks, fails flex test)
│  └─ ACTION: Significant design rework (10-14 days), reschedule launch to June 10-15
│
├─ BRANCH D: FUNCTIONAL FAILURE (grip or post failure)
│  ├─ Sub-branch D1: Grip surface too smooth
│  │  └─ ACTION: Material iteration or texture redesign (7-10 days), launch June 2-5
│  │
│  └─ Sub-branch D2: Post wobble/deflection
│     └─ ACTION: Post diameter adjustment (5-7 days), launch June 2-5
│
└─ BRANCH E: SCALE/SHRINKAGE ISSUE (dimensions noticeably off)
   └─ ACTION: Process parameter adjustment (temperature/speed, 5 days), launch May 29-June 2
```

---

## Part 3: Branch A Execution — IMMEDIATE ETSY LAUNCH (Test Print Passes)

**Timeline**: May 23-29 (6 days to launch)

### 3.1 Approval Decision (May 23 — same day as test print completion)
- [ ] User confirms test print passes ALL success criteria from Part 1
- [ ] User approves proceeding with Etsy launch
- **Go/No-Go Decision**: If yes, proceed to 3.2. If no or uncertain, escalate to Branch B-E.

### 3.2 Pre-Launch Validation (May 24, 4 hours)
- [ ] **Cross-check**: Read `test-print-failure-recovery-plan.md` Section 1 (Post-Print Inspection Checklist) against user's test print results
- [ ] **Dimensional mapping**: Confirm all measured dimensions fall within CAD tolerance bands from Part 1 above
- [ ] **Functional validation**: User's three functional tests (snap-arm flex, rail grip, post stability) all pass
- [ ] **Design freeze**: Confirm `modrun_clip.py` and `modrun_rail.py` are FINAL designs (no further iterations)
- [ ] **Status update**: Mark designs as "TEST-PRINT-VALIDATED" in PROJECTS.md

### 3.3 Integration with Existing Launch Artifacts (May 24-25, 6 hours)
- [ ] **Integrate with `etsy-listing-launch-checklist.md`**: Add test print validation results as Pre-Launch Step 0 completion proof
- [ ] **Integrate with `8-printer-farm-cost-model.md`**: Confirm per-unit cost assumptions remain valid post-test-print
- [ ] **Integrate with `supplier-negotiation-playbook-consolidated.md`**: Confirm supplier scorecard and vendor selection remain valid
- [ ] **Etsy copy validation**: Re-read all listing descriptions in `etsy-listing-launch-checklist.md` — verify they match test-print-validated design
- [ ] **SKU/Product spec verification**: Ensure product descriptions, photos, and pricing align with validated design

### 3.4 Etsy Store Launch Readiness (May 25-26, 8 hours)
- [ ] **Etsy account setup**: (User action) Create Etsy shop, configure payment, shipping, policies
- [ ] **Product listing upload**: (User action) Upload 21 Phase 1 products using checklists from `etsy-listing-launch-checklist.md`
- [ ] **Photography**: (User action) Take mockup photos of ModRun cable clips using test print as reference
- [ ] **Promotional setup**: (User action) Configure search ads, email signup, review request templates
- [ ] **Final pre-launch audit**: Verify all 21 listings are live, pricing correct, shipping configured

### 3.5 Day 1 Launch Operations (May 27-29, ongoing)
Reference: `DAY1_LAUNCH_OPERATIONS_PLAYBOOK.md`
- [ ] **Monitoring setup**: GA4 tracking, Etsy dashboard, order notification system
- [ ] **Social media announcement**: (User action) Post to social channels with launch day messaging
- [ ] **Press/influencer outreach**: (User action) Send launch notifications to targets
- [ ] **Support readiness**: Set up email/message templates for customer support
- [ ] **Daily operations**: Monitor orders, ship same-day, track metrics per `revenue-ramp-metrics.md`

### 3.6 Launch Confidence Checkpoints
- ✅ **May 26 (2 days pre-launch)**: All 21 listings live, pricing correct, shipping zone configured, payment processing tested
- ✅ **May 28 (1 day pre-launch)**: Social announcements scheduled, email templates ready, order fulfillment system tested
- ✅ **May 29 (Launch day)**: Monitor live sales, first orders shipped same-day, team available for urgent issues

**Branch A Expected Outcome**: Etsy store live May 29-30. Phase 1 first orders incoming. June 1-15 window for analytics collection.

---

## Part 4: Branch B Execution — SNAP-ARM TOLERANCE ITERATION (May 24-June 5)

**Timeline**: May 24-June 5 (12 days, reschedule launch to June 2-5)

### 4.1 Diagnosis (May 24, 2 hours)
- [ ] **Measure snap-arm thickness**: Confirm value is <1.25 mm or >1.55 mm
- [ ] **Determine direction**: 
  - If <1.25 mm → snap-arm is too thin, likely fails under cable tension
  - If >1.55 mm → snap-arm is too thick, may not flex properly
- [ ] **Document cause**: Review `modrun_clip.py` extrusion parameters. Likely cause: nozzle temp deviation, layer height setting, or CAD wall thickness spec.

### 4.2 Design Iteration (May 25-27, 3-5 hours)
- [ ] **Adjust `modrun_clip.py`**:
  - If too thin: increase extrusion width or wall count in relevant sections
  - If too thick: decrease extrusion width or adjust profile offset
- [ ] **Test CAD**: Update, slice with Cura, check wall thickness at critical point
- [ ] **Nozzle temp tuning**: Consider 220°C (test was 220-225°C) if temperature is a variable
- [ ] **Updated design file**: Save new version, tag as `modrun_clip_v2_[date]`

### 4.3 Second Test Print (May 28-29, 2 hours execution + inspection)
- [ ] **Execute second test print** with updated design parameters
- [ ] **Inspect using Part 1 criteria** — snap-arm thickness must now be 1.25-1.55 mm
- [ ] **Functional tests**: Snap-arm flex, rail grip, post stability (same as Branch A)

### 4.4 Decision Gate (May 29)
- ✅ **If second test print passes**: Proceed to 4.5 (Launch readiness)
- ❌ **If second test print fails**: Escalate to Branch C (Significant redesign) — reschedule launch to June 10-15

### 4.5 Pre-Launch Validation & Launch (May 30-June 5)
- [ ] Repeat steps 3.2-3.6 from Branch A, compressed into May 30-June 5 timeline
- [ ] **Etsy store launch**: June 2-5 (3-4 days after design iteration)
- [ ] **Updated timeline**: June analytics collection window shorter (10-12 days instead of 15)

**Branch B Expected Outcome**: Etsy store live June 2-5. Slightly compressed analytics window but Phase 1 still on track.

---

## Part 5: Branch C Execution — SNAP-ARM STRUCTURAL FAILURE (May 24-June 15)

**Timeline**: May 24-June 15 (22 days, significant redesign required)

### 5.1 Diagnosis (May 24, 3 hours)
- [ ] **Failure analysis**: Review cracking pattern, stress mark locations, flex test failure
- [ ] **Root cause**: Determine if failure is:
  - Material issue (PLA+ brittleness, too cold?)
  - Design issue (snap-arm geometry too aggressive)
  - Process issue (nozzle temp too low, cooling too fast)
- [ ] **Consult references**: Review `test-print-failure-recovery-plan.md` Section 2 (Snap-Arm Failure) for detailed diagnostics

### 5.2 Structural Redesign (May 25-June 5, 8-12 hours)
- [ ] **Modify `modrun_clip.py`**:
  - Increase snap-arm thickness beyond 1.4 mm (try 1.6-1.8 mm)
  - Increase snap-arm length for better leverage
  - Add fillet radius at snap-arm base to reduce stress concentration
  - Consider reducing overall clamp force requirement
- [ ] **Material trial**: Consider testing with different material (PETG instead of PLA+ for higher flex tolerance)
- [ ] **CAD validation**: Run stress simulation if possible (FEA or manual calculations)
- [ ] **Vendor consultation**: Email supplier contacts (see `supplier-negotiation-playbook-consolidated.md`) for manufacturing advice on similar snap features

### 5.3 Third Test Print (June 6-7, 2 hours execution + inspection)
- [ ] **Execute test print** with redesigned snap-arm geometry
- [ ] **Inspect snap-arm flex**: Must flex smoothly under thumb pressure, no cracks
- [ ] **Functional test**: Cable post stability and rail grip also confirmed

### 5.4 Launch Timeline (June 8-15)
- [ ] Repeat Branch A validation (3.2-3.5) in compressed 5-day window
- [ ] **Etsy store launch**: June 10-15
- [ ] **Shortened analytics window**: Only ~15 days before Phase 2 decisions needed

**Branch C Expected Outcome**: Etsy store live June 10-15. Phase 1 data collection compressed. Phase 2 launch decision may shift to mid-June.

---

## Part 6: Branch D Execution — FUNCTIONAL FAILURE (May 24-June 5)

**Timeline**: May 24-June 5 (12 days, targeted redesign)

### 6.1 Sub-Branch D1: Grip Surface Failure
**Symptoms**: Clip slides on ModRun rail; no friction/grip
**Root cause**: Rail jaw surfaces too smooth from FDM printing

**5-day recovery**:
- [ ] **Option A**: Add micro-texture to `modrun_clip.py` rail grip surfaces (indent pattern, ~0.1 mm deep)
- [ ] **Option B**: Increase jaw pressure by reducing jaw opening slightly (7.6–7.8 mm instead of 7.8–8.2 mm)
- [ ] **Test iteration**: Second test print with textured surface (May 27-28)
- [ ] **Launch readiness**: June 2-5 if test passes

### 6.2 Sub-Branch D2: Cable Post Wobble
**Symptoms**: Post deflects >2 mm under cable tension; post may shear off under load
**Root cause**: Post diameter too small (8.0 mm tolerance may be at lower bound) or insufficient wall thickness

**5-7 day recovery**:
- [ ] **Increase post diameter**: Try 8.5 mm or 9.0 mm
- [ ] **Increase post height wall thickness**: Add extra perimeter walls in post section
- [ ] **Test iteration**: Second test print with thicker post (May 27-29)
- [ ] **Launch readiness**: June 2-5 if test passes

### 6.3 Decision Gate (May 30)
- ✅ **If functional test passes on redesigned component**: Proceed to launch (3.2-3.5 steps, June 2-5)
- ❌ **If functional test fails again**: Escalate to Branch C (full structural rework)

**Branch D Expected Outcome**: Etsy store live June 2-5 (targeted single-component redesign). Phase 1 timeline mostly on track.

---

## Part 7: Branch E Execution — SCALE/SHRINKAGE ISSUE (May 24-June 2)

**Timeline**: May 24-June 2 (9 days, process adjustment)

### 7.1 Diagnosis (May 24, 2 hours)
- [ ] **Measure overall dimensions**: Are printed parts noticeably larger or smaller than CAD?
- [ ] **Likely cause**: 
  - Oversized (typically 0.3-0.5% expansion): Nozzle temp too high, or material brand variation
  - Undersized (typically 0.2-0.4% shrinkage): Nozzle temp too low, or cooling too fast
- [ ] **Review Cura slicing parameters**: Compare against original test print settings

### 7.2 Process Adjustment (May 25-26, 2-3 hours)
- [ ] **Adjust nozzle temperature**: 
  - If oversized: Try 215°C or 218°C (lower than 220-225°C range)
  - If undersized: Try 223°C or 225°C (higher in range)
- [ ] **Adjust layer height or print speed**: Minor tweaks to cooling rates
- [ ] **Document new parameters**: Update test print spec sheet

### 7.3 Fourth Test Print (May 27-28, 2 hours execution + inspection)
- [ ] **Execute test print** with adjusted temperature
- [ ] **Measure dimensions**: Confirm all dimensions now fall within CAD tolerance bands
- [ ] **Functional tests**: Snap-arm flex, rail grip, post stability

### 7.4 Launch Readiness (May 29-June 2)
- [ ] Repeat Branch A validation (3.2-3.5) in compressed 3-day window
- [ ] **Etsy store launch**: May 29-June 2 (on original timeline)
- [ ] **Full analytics window**: June 1-July 15 (45 days for Phase 2 decision gate)

**Branch E Expected Outcome**: Etsy store live May 29-June 2 (minimal schedule slip). Phase 1 analytics window intact.

---

## Part 8: Integration Checklist — All Branches

Once test print branch completes and Etsy launch readiness confirmed, integrate these existing deliverables:

### 8.1 Existing Documents to Integrate
- [ ] **`etsy-listing-launch-checklist.md`** — Add test print result as Pre-Launch Step 0 proof
- [ ] **`DAY1_LAUNCH_OPERATIONS_PLAYBOOK.md`** — Activate Phase 1 operational procedures
- [ ] **`8-printer-farm-cost-model.md`** — Validate per-unit costs post-design-validation
- [ ] **`supplier-negotiation-playbook-consolidated.md`** — Confirm vendor selection for post-launch manufacturing scale
- [ ] **`revenue-ramp-metrics.md`** — Activate daily/weekly monitoring upon launch

### 8.2 Key Validation Points
- ✅ Design is test-print-validated and finalized
- ✅ Etsy shop is created with all 21 Phase 1 products live
- ✅ Pricing, shipping, and policies configured
- ✅ Payment processing tested with first order
- ✅ Support templates ready for customer inquiries
- ✅ Analytics dashboard live (GA4, Etsy API, Kit email)

### 8.3 Post-Launch Monitoring (Daily, Weeks 1-6)
- [ ] **Order volume**: Track daily orders; target = 5-15 orders by Day 7
- [ ] **Customer feedback**: Respond to all reviews and questions same-day
- [ ] **Operational metrics**: Fulfillment time, return rate, support ticket volume
- [ ] **Conversion tracking**: Understand which products and marketing channels drive traffic
- [ ] **Cash flow**: Monitor revenue accrual, payment processing delays

### 8.4 Decision Point — Phase 2 Authorization (June 15, ~45 days post-launch)
Based on Phase 1 analytics:
- [ ] **Cohort analysis**: What % of purchasers are in target demographic (foragers, homesteaders, Midwest Zone 5)?
- [ ] **Conversion rate**: What % of traffic converts to purchase? Target >2%
- [ ] **Margin validation**: Are actual unit costs matching cost model? Margins healthy?
- [ ] **Repeat purchase rate**: Are customers buying multiple products or one-time?
- **Go/No-Go decision**: Proceed to Phase 2 (lifestyle photography) or iterate Phase 1?

---

## Part 9: Timeline Summary Table

| Branch | Test Print Outcome | Design Iteration | 2nd Test Print | Etsy Launch Date | Phase 1 Analytics Window | Phase 2 Gate Decision |
|--------|-------------------|------------------|-----------------|------------------|-------------------------|----------------------|
| **A** | All tests pass | None | N/A | May 29-30 | June 1-July 15 | ~July 15 |
| **B** | Snap-arm tolerance off | 3-5 days | May 28 | June 2-5 | June 2-July 17 | ~July 17 |
| **C** | Snap-arm structural | 8-12 days | June 6-7 | June 10-15 | June 10-July 25 | ~July 25 |
| **D** | Functional failure | 5-7 days | May 28-29 | June 2-5 | June 2-July 17 | ~July 17 |
| **E** | Scale/shrinkage | 2-3 days | May 27-28 | May 29-June 2 | June 1-July 15 | ~July 15 |

---

## Part 10: Success Criteria & Risk Mitigation

### 10.1 Success Criteria (All Branches)
✅ Test print completed and documented by May 23
✅ Design validated or iteration completed by May 30
✅ Etsy store live and accepting orders by June 5 at latest
✅ 21 Phase 1 products active on Etsy
✅ Analytics collection system operational
✅ Phase 1 revenue >$500 by June 30
✅ Cohort data sufficient for Phase 2 decision by July 15

### 10.2 Risk Mitigation
- **Risk**: Multiple design iterations delay launch beyond June 5
- **Mitigation**: If Branch C extends past June 5, user can launch with Branch E (process-adjusted) version as interim while developing Branch C
- **Risk**: Test print materials unavailable
- **Mitigation**: Pre-order 2-3 kg PLA+ spools in advance; order placed May 20
- **Risk**: Etsy shop setup delays
- **Mitigation**: User creates Etsy shop immediately upon test print approval (May 23); product uploads happen in parallel with design validation

### 10.3 Escalation Path
- **Day 1 blocker**: Test print not completed by May 23 → Reschedule to May 25-26, launch to June 5-10
- **Multiple iteration failures**: Design fails 3rd test print → Escalate to user for fundamental design review (June 15+)
- **Unexpected manufacturing issue**: Supplier unavailable post-validation → Sourcing partner identification (backup in `supplier-negotiation-playbook-consolidated.md`)

---

## Part 11: User Action Summary

**Test Print Execution** (User to do May 22-23):
1. Print ModRun cable clip with baseline specs
2. Inspect using Part 1 checklist (visual, dimensional, functional)
3. Document results with photos and measurements
4. Report outcome to orchestrator

**Based on Outcome** (User to do per branch, May 24+):
- Branch A: Approve design, proceed with Etsy launch (May 25-29)
- Branch B/D: Approve design iteration, execute 2nd test print (May 27-29)
- Branch C: Approve structural redesign, execute 3rd test print (June 6-7)
- Branch E: Approve process adjustment, execute 4th test print (May 27-28)

**Launch Window** (User to do June 1-7 depending on branch):
1. Create Etsy shop
2. Upload 21 Phase 1 product listings
3. Configure payments, shipping, policies
4. Announce launch on social media
5. Monitor orders and customer feedback daily

---

## Part 12: Document References

**Cross-references** (integration points):
- `test-print-failure-recovery-plan.md` — Detailed inspection procedures for test print outcomes
- `etsy-listing-launch-checklist.md` — 21 Phase 1 product pre-launch checklist
- `DAY1_LAUNCH_OPERATIONS_PLAYBOOK.md` — Operational procedures upon launch
- `8-printer-farm-cost-model.md` — Per-unit cost validation post-design confirmation
- `supplier-negotiation-playbook-consolidated.md` — Vendor selection and scale logistics
- `revenue-ramp-metrics.md` — Phase 1 KPI monitoring framework
- `modrun_clip.py` & `modrun_rail.py` — Design source files (CAD parameters)

---

**Status**: READY FOR USER EXECUTION
**Next action**: User executes test print (May 22-23) → Reports outcome → Orchestrator activates appropriate branch
