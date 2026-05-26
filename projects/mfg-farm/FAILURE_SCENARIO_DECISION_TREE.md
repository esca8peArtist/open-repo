---
title: Failure Scenario Decision Tree
subtitle: ASCII flowchart + prose for rapid test print failure routing
project: mfg-farm
date: 2026-05-26
status: production-ready
version: 1.0
purpose: "Real-time routing from test print outcome to contingency execution without decision lag"
---

# Failure Scenario Decision Tree

**Document Purpose**: When test print outcome is known (May 25-27), user needs an immediate routing decision. This document provides a visual flowchart + prose decision matrix to route to correct contingency path in <15 minutes, with no discovery overhead.

**How to use**: 
1. Evaluate test print using test-print-failure-recovery-plan.md Section 1
2. Record outcome on the decision tree below (PASS, PASS-WITH-ADJUSTMENTS, FAIL, PARTIAL-FAIL)
3. Follow the routing path → detailed execution plan in POST_TEST_PRINT_FAILURE_EXECUTION_PLAN.md

---

## Master Decision Tree (ASCII Flowchart)

```
TEST PRINT OUTCOME EVALUATION (Day 1 AM, ~15 minutes)
|
├─ RUN FULL INSPECTION PROTOCOL (test-print-failure-recovery-plan.md Section 1)
│  ├─ Visual inspection (crack/stress marks visible?)
│  ├─ Dimensional check (snap-arm 1.4mm ±0.15mm? Within spec?)
│  ├─ Functional tests (snap-arm flex test, rail grip test, cable post wobble test)
│  └─ Document findings → Next decision point
│
└─ ROUTE TO OUTCOME BASED ON INSPECTION RESULTS
   │
   ├─ OUTCOME A: ✅ PASS
   │  │ Snap-arm thickness 1.4–1.55 mm
   │  │ No cracks or stress marks
   │  │ All functional tests pass
   │  │ All dimensions within tolerance
   │  │
   │  └─→ DECISION: Proceed to Launch Path (no contingency needed)
   │     └─ Proceed to ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md Part 1
   │     └─ Target launch: May 30 (4-day prep, standard sequence)
   │     └─ No redesign needed; move forward at speed
   │
   ├─ OUTCOME B: ⚠️ PASS WITH MINOR ADJUSTMENTS
   │  │ Snap-arm thickness 1.25–1.4mm OR 1.55–1.70mm (slightly off spec)
   │  │ No visible cracks, but close to edge
   │  │ Functional tests pass with some tightness/looseness
   │  │
   │  └─→ DECISION: Quick CAD tolerance tweak + retest (1-day path)
   │     ├─ Step 1: Adjust snap-arm tolerance ±0.1mm in CAD (5 min)
   │     ├─ Step 2: Regenerate STL, reprint test sample (2-3 hours print + 1 hour cool)
   │     ├─ Step 3: Re-test (15 min)
   │     ├─ Step 4: If passes: Proceed to launch May 31 (1-day delay)
   │     └─ Step 5: If fails: Route to SCENARIO A (FAIL path)
   │     └─ Total timeline: +1 day vs. Outcome A (May 30 → May 31 launch)
   │
   ├─ OUTCOME C: 🔴 FAIL
   │  │ Snap-arm snaps on flex test
   │  │ Visible cracks or stress marks
   │  │ Thickness <1.25mm OR >1.70mm
   │  │ Post wobbles >2mm or feels brittle
   │  │ Design fundamentally unfeasible in current form
   │  │
   │  └─→ ROUTE TO SCENARIO A: FAIL → Design Pivot Decision (Day 1 afternoon)
   │     │
   │     ├─ OPTION A1: v2 Redesign Path (Snap-Arm Iteration)
   │     │  ├─ Decision criteria: Root cause identified? Confidence ≥70% in fix?
   │     │  │  YES → Proceed with v2 redesign (see Scenario A section below)
   │     │  │  Timeline: Days 1-3 CAD + test, Days 4-7 production batch + evaluation
   │     │  │  Launch target: May 30-31 (if v2 passes by Day 7)
   │     │  │
   │     │  └─ NO → Escalate to Option A2 (Fallback Pivot)
   │     │
   │     └─ OPTION A2: Fallback Product Pivot
   │        ├─ Decision criteria: Snap-arm v2 confidence <70%? OR v2 test fails on Day 3-4?
   │        │  YES → Commit to fallback product (magnetic/adhesive/screw-mount)
   │        │  Timeline: Days 3-5 CAD + test fallback, Days 6-7 Etsy prep, Day 8 launch
   │        │  Launch target: June 2-5
   │        │
   │        └─ Fallback product choice (pick one):
   │           ├─ Magnetic clips (recommended: fastest, differentiated, $200-300/mo potential)
   │           ├─ Adhesive-only clips (semi-permanent, slightly faster CAD)
   │           └─ Screw-mount clips (proven, least differentiated)
   │
   ├─ OUTCOME D: 🟡 PARTIAL-FAIL
   │  │ Some sizes work, some don't
   │  │ Examples:
   │  │  - 0.5" SKU: PASS ✓
   │  │  - 0.75" SKU: FAIL (snap too tight) ✗
   │  │  - 1.0" SKU: MARGINAL (loose snap, functional but borderline) ◐
   │  │ OR: Snap-arm borderline functional (tight tolerance, not cracked but risky)
   │  │
   │  └─→ ROUTE TO SCENARIO B: PARTIAL-FAIL → Launch Strategy Decision
   │     │
   │     ├─ OPTION B1: Launch Passing SKU(s) Immediately + Parallel Iterate Failing SKU(s)
   │     │  ├─ Decision criteria: Passing SKU revenue >$100/month? Failing SKU fix is clear?
   │     │  │  YES → Launch passing SKU May 30 (standard timeline)
   │     │  │  Parallel: Iterate failing SKU Days 1-7, add to catalog June 2-5
   │     │  │  Timeline: Staggered release (May 30 + June 2-5)
   │     │  │
   │     │  └─ Advantage: Immediate revenue + early reviews on passing SKU
   │     │     Risk: Single-SKU launch is weaker than full portfolio (lower algorithm signal)
   │     │     Mitigation: Add "More sizes coming soon" to listing
   │     │
   │     └─ OPTION B2: Hold All SKUs for Full Redesign + Coordinated Launch
   │        ├─ Decision criteria: Passing SKU revenue <$50/month? Failing SKU is core product?
   │        │  YES → Delay launch, redesign all sizes, launch full portfolio June 1-2
   │        │  Timeline: Coordinated (all sizes evaluated by Day 7, launch June 1-2)
   │        │
   │        └─ Advantage: Single cohesive brand message, stronger portfolio positioning
   │           Risk: 2-3 day delay (May 30 → June 1-2); missed early-adopter window
   │           Mitigation: June 1-2 launch is still within strong market window
   │
   └─ END: Route to appropriate execution plan (POST_TEST_PRINT_FAILURE_EXECUTION_PLAN.md)

```

---

## Decision Matrix: Outcome → Route

**Use this table to quickly route to correct contingency path based on test print results:**

| Test Print Outcome | Visual Inspection | Dimensions | Functional Tests | Route Decision | Next Action |
|---|---|---|---|---|---|
| **PASS** | No defects | Within spec (1.4 mm ±0.15) | All pass (flex, grip, post stable) | ✅ Proceed to Launch | ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md Part 1, launch May 30 |
| **PASS-MINOR-ADJ** | Clean, no cracks | Near spec but tight/loose (1.25-1.70mm range) | Pass with slight tightness/looseness | ⚠️ Quick tweak + retest | CAD tolerance ±0.1mm, retest Day 2, launch May 31 |
| **FAIL-SNAP-ARM** | Cracks visible, stress marks | Snap-arm too thin (<1.25mm) | Snap-arm breaks on flex test | 🔴 Scenario A: Redesign or Pivot | Diagnose root cause (under-extrusion? tolerance? geometry?). If confidence <70%: pivot to fallback product. If confidence ≥70%: v2 redesign (Days 1-7). |
| **FAIL-GRIP-SURFACE** | Rough/separated layers | OK | Clip slips on rail or doesn't grip | 🔴 Scenario A (reduced severity) | Likely print speed or layer height issue. Quick fix: reduce speed, retest Day 2. If persists: fallback pivot. |
| **FAIL-POST-WOBBLE** | No visible defects | Post diameter OK | Post wobbles >2mm under cable pull | 🔴 Scenario A (medium severity) | Likely infill or wall thickness issue. Increase infill to 30% or post diameter to 8.5mm, retest Day 2. If persists: fallback pivot. |
| **FAIL-SCALE-OFF** | Looks noticeably wrong size | Off by >1mm | Can't fit on rail or looks tiny | 🔴 Scenario A (likely slicer error) | Check: slicer scale 1.0x? File export correct units? Reexport STL, retest Day 2. Usually quick fix. |
| **FAIL-BRITTLE** | Discolored, cracks easily | OK | Snaps with no flex, material feels weak | 🔴 Scenario A (material issue) | Likely nozzle temp too high. Reduce to 215°C, retest Day 2. OR filament is wet (dry 4-6 hrs). Usually quick fix. |
| **PARTIAL-PASS-1-of-3** | 0.5" size OK, 0.75" & 1.0" have snap issues | 0.5" in spec, others tight | 0.5" passes all, 0.75"/1.0" fail snap tests | 🟡 Scenario B (Option B1 recommended) | Launch 0.5" May 30, parallel iterate 0.75" & 1.0" (likely size-dependent scaling issue), add to catalog June 2-5. |
| **PARTIAL-PASS-2-of-3** | 2 sizes OK, 1 has snap issue | 2/3 in spec, 1 tight | 2/3 pass, 1 borderline snap | 🟡 Scenario B (Option B1 recommended) | Launch 2 passing SKUs May 30, iterate 1 failing SKU Days 1-7, add June 2-5. Strong option: get early revenue + reviews on proven SKUs. |
| **PARTIAL-PASS-BORDERLINE** | Clean, no visible defects | At edge of spec (1.4-1.55mm, very tight) | All pass but snap is very tight, risky | 🟡 Scenario B (Option B2 safer) | v2 redesign all sizes (relax snap-arm tolerance), retest Day 3-4. All-or-nothing: if v2 passes all, launch June 1-2 (cleaner). If v2 partially passes: Option B1. |

---

## Routing Decision: A1 (v2 Redesign) vs. A2 (Fallback Pivot) for SCENARIO A

**When test print FAILS, the biggest decision is: redesign snap-arm (v2) or pivot to fallback product?**

**Decision framework** (pick the row that matches your situation):

| Situation | Confidence Assessment | Recommendation | Rationale |
|---|---|---|---|
| **Root cause is clear** (e.g., "snap-arm measured 1.0mm, too thin. Increase to 1.5mm.") | ≥90% confident fix will work | **A1: v2 Redesign** | Clear root cause + high confidence = proceed with iteration. Time cost is minimal (3-4 days), upside is large ($500+/month snap-arm vs. $200-300/month fallback). |
| **Root cause is likely** (e.g., "probably under-extrusion. Increase flow +3%, retest.") | 70-89% confident | **A1: v2 Redesign** | Medium-high confidence is acceptable threshold. Proceed with v2. If v2 fails on Day 3-4, escalate to fallback. |
| **Root cause is unclear** (e.g., "snap-arm failed but I'm not sure why: tolerance? geometry? material?") | <70% confident | **A2: Fallback Pivot** | Low confidence on root cause = high risk of iterating on wrong fix. Better to pivot to fallback (guaranteed to work, simpler design) and get revenue by June 2-5 than spend 5-7 days debugging snap-arm with <50% success rate. |
| **You've already spent 1 design iteration (Outcome B→retest failed)** | — | **A1: v2 (max 1 more iteration)** | If Outcome B retest fails, you have 1 more v2 attempt. If v2 fails on Day 3-4, **escalate to A2 immediately**. Do not attempt v3; opportunity cost is too high. |
| **Snap-arm is core product positioning** (key differentiator for your brand) | — | **A1: v2 Redesign (commit max 10 days)** | If snap-arm is critical to your brand story, iterate up to Day 10 (June 5 launch). But set hard deadline: if v3 still fails on Day 6-7, pivot to fallback. Do not delay past June 5 waiting for perfect snap-arm. |
| **You have no time for iteration** (market window closes June 15) | — | **A2: Fallback Pivot (immediate)** | Speed is critical. Fallback is 5 days faster (June 2-5 vs. May 30-31). Fallback guarantees you capture June 2-15 market window. Snap-arm v2 is risky on timeline. |
| **You're frustrated or fatigued** (spent 4+ hours on test print already) | — | **A2: Fallback Pivot** | Mental state matters. If you're burnt out, pivoting to simpler product is better than grinding through v2-v3 iterations. Fallback is low-stress path: simple design, fast validation, solid revenue. |

---

## Specific Routing Examples (Real Scenarios)

### Example 1: OUTCOME C (FAIL) → Snap-Arm Measured 0.9mm (Too Thin)

**Inspection results**:
- Visual: Snap-arm clearly thinner than expected, no visible cracks but material is stressed
- Dimensional: Snap-arm measured 0.9mm vs. spec 1.4mm (CRITICAL misspec)
- Functional: Snap-arm breaks immediately on flex test

**Diagnosis**:
- Root cause: Under-extrusion (nozzle jammed? Flow rate too low? Layer thickness wrong?)
- Hypothesis: "Increase flow +3% or reduce layer height 0.20→0.15mm, retest"
- Confidence: 85% (this is a textbook under-extrusion symptom)

**Routing**:
```
Root cause: CLEAR (under-extrusion)
Confidence: ≥70% (85%)
├─ YES → A1: v2 Redesign
├─ Timeline: Days 2-4 (fix flow + retest Day 2, evaluate Day 2 evening, lock design, produce batch Days 3-4)
├─ Launch target: May 30-31 (on schedule if v2 passes Day 2)
└─ If v2 fails Day 2: Escalate to A2 (fallback pivot) immediately
```

**Execution**:
- Day 1 afternoon: Adjust slicer flow +3%, regenerate G-code, print v2 test (90 min print + 1 hour cool)
- Day 2 morning: Measure snap-arm on v2 (should be 1.4mm if fix worked)
- Day 2 noon: If v2 passes → lock design, order production batch. If v2 fails → pivot to fallback (Day 2 decision)
- Day 3-4: Production batch printing/delivery
- May 30-31: Launch

---

### Example 2: OUTCOME D (PARTIAL-FAIL) → Two Sizes Pass, One Size Fails Snap Test

**Inspection results**:
- Visual: 0.5" looks good, 0.75" has tight snap-arm, 1.0" snap-arm is loose
- Dimensional: 0.5" = 1.4mm (PASS), 0.75" = 1.3mm (TIGHT), 1.0" = 1.5mm (LOOSE)
- Functional: 0.5" and 1.0" pass flex test, 0.75" snap-arm is too tight to flex

**Diagnosis**:
- Root cause: Size-dependent scaling issue in parametric design (larger sizes get looser, medium size gets tighter, unclear why)
- Hypothesis: "Design tolerance scales with size? Adjust parametric multiplier for 0.75" size."
- Confidence: 70% (I think it's a parametric design bug, but not 100% sure)

**Routing**:
```
Two sizes pass (0.5", 1.0"), one fails (0.75")
Revenue upside of launching passing SKUs: ~$300+/month
├─ Option B1 (Launch 2, iterate 1): RECOMMENDED
├─ Timeline: Launch 0.5" & 1.0" May 30 (standard), iterate 0.75" Days 1-7, add June 2-5
├─ Parallel: Re-examine 0.75" size parametric scaling while 0.5"/1.0" are live
└─ If 0.75" v2 passes by Day 7: add to catalog June 2-5
   If 0.75" v2 fails: decide accept borderline performance OR delay to June 6+ for deeper debugging
```

**Execution**:
- Day 1 afternoon: Launch prep for 0.5" & 1.0" (photography, listing copy)
- Days 1-3: Photography, Etsy prep (passing SKUs only)
- Day 4: Publish 0.5" & 1.0" to Etsy (standard launch)
- Days 2-3 parallel: CAD analysis of 0.75" scaling issue, edit parametric multiplier, regenerate STL
- Day 3-4: Order 0.75" v2 test print (1-2 units)
- Day 5-6: Evaluate 0.75" v2
- Day 7: Decision: add to catalog OR delay further
- May 30 +: Full 3-size portfolio by June 2-5

---

### Example 3: OUTCOME C (FAIL) → Snap-Arm Cracked, Root Cause Unclear

**Inspection results**:
- Visual: Snap-arm has horizontal crack (stress fracture)
- Dimensional: Snap-arm measures 1.4mm (IN SPEC!)
- Functional: Snap breaks immediately on flex test

**Diagnosis**:
- Root cause: Unknown (tolerance is correct, so why did it break? Geometry issue? Material defect? Temperature?)
- Hypothesis: "Could be stress concentration at snap-arm root, or material was brittle from over-heating, or infill is too low"
- Confidence: 40% (three possible causes, no clear winner)

**Routing**:
```
Root cause: UNCLEAR
Confidence: <70% (40%, three competing hypotheses)
├─ Option A1.5 (Expert escalation): Ask 3D printing forum / Discord experts
│  └─ Timeline: +1-2 days (wait for feedback, implement fix, retest)
│  └─ If expert suggests clear fix: proceed to A1 v2 redesign
│  └─ If expert says "might be design-level issue": escalate to A2 (fallback pivot)
│
└─ Option A2 (Fallback pivot): Skip debug, pivot to fallback immediately
   └─ Timeline: Days 3-5 (fallback CAD + test + production prep), launch June 2-5
   └─ Rationale: Low confidence on root cause + time cost of debugging = not worth it
```

**Execution**:
- Day 1 afternoon: Post to r/3Dprinting or Bambu Discord with photos + measurements (ask for help diagnosing crack)
- Day 2 morning: Read expert feedback
  - If expert says "almost certainly stress concentration at root, add 0.3mm fillet": → A1 v2 redesign (Day 2 CAD edit + Day 3 test)
  - If expert says "unclear, could be multiple issues": → A2 fallback pivot (Day 2 decision, begin fallback CAD)
- Day 3+: Proceed based on expert input

---

### Example 4: OUTCOME B (MINOR ADJ) → Snap-Arm Very Tight, 1.5mm Measured vs. 1.4mm Target

**Inspection results**:
- Visual: No cracks, looks solid, but snap-arm is clearly thicker/stiffer than expected
- Dimensional: Snap-arm = 1.5mm (ABOVE spec 1.4±0.15, in the 1.55mm ceiling range)
- Functional: Snap-arm flexes but with high force required; snap is very stiff

**Diagnosis**:
- Root cause: Over-extrusion (nozzle flow too high? Filament diameter expanded?)
- Hypothesis: "Reduce flow -2% or nozzle temp -5°C to shrink snap-arm to 1.4mm"
- Confidence: 85% (textbook over-extrusion symptom)

**Routing**:
```
Snap-arm is functional but stiff
Confidence in fix: ≥70% (85%, classic over-extrusion)
├─ Proceed: Quick CAD tolerance tweak OR print setting fix
├─ Option 1 (Faster): Reduce flow -2% in slicer, retest Day 2 (no CAD change)
├─ Option 2 (Designer control): Edit CAD to reduce snap-arm thickness 1.4 → 1.35mm (tighter target), retest Day 2
├─ Timeline: Either option = +1 day (May 30 → May 31 launch)
└─ If retest passes: Proceed to May 31 launch
   If retest fails: Route to Scenario A (redesign or pivot)
```

**Execution**:
- Day 1 evening: Edit slicer (reduce flow -2%) OR edit CAD (reduce snap-arm 1.4 → 1.35mm)
- Day 2 morning: Print retest sample (90 min print + 1 hour cool)
- Day 2 noon: Measure snap-arm (target 1.3-1.4mm)
  - If PASS: lock design, order production batch, launch May 31 ✓
  - If FAIL: escalate to Scenario A, decide A1 (v2 redesign) vs. A2 (fallback pivot)

---

## Quick Reference: Outcome → Timeframe Table

**Use this table to estimate launch date based on test print outcome:**

| Outcome | Severity | Days to Launch Decision | Days to Production Ready | Estimated Launch Date |
|---|---|---|---|---|
| **PASS** | None | Same day (Day 1) | 4 days (Days 2-5 prep) | **May 30** (4 days after test print) |
| **PASS-MINOR-ADJ** | Low | 1 day (retest Day 2) | 4-5 days (Days 3-6 prep) | **May 31** (5 days after test print) |
| **FAIL-quick-fix** (under-extrusion, temp, speed) | Medium | 1 day (v2 test Day 2, evaluate Day 2 evening) | 2-3 days (Days 3-4 production) | **May 30-31** (3-4 days after test print) |
| **FAIL-v2-design** (snap-arm redesign needed) | Medium-High | 3-4 days (CAD Days 1-2, test Days 3-4) | 2-3 days (Days 5-6 production) | **May 30-31** (if v2 passes) OR **June 2-5** (if v2 fails, pivot) |
| **FAIL-escalate-pivot** (root cause unclear, <70% confidence) | High | 1 day (Day 1 escalation decision) | 3-5 days (fallback CAD + test + production) | **June 2-5** (7-10 days after test print) |
| **PARTIAL-B1** (launch passing, iterate failing) | Medium | Same day (Day 1 decision) | 4 days (Days 2-5 prep passing) | **May 30** (passing) + **June 2-5** (failing) |
| **PARTIAL-B2** (full redesign, coordinated launch) | Medium | 3-4 days (all 3 sizes v2 testing Days 1-4) | 2-3 days (Days 5-6 production) | **June 1-2** (4-5 days after test print) |

---

## Decision Gate Checklist (Use Day 1 Morning)

**After test print inspection, answer these questions to route to correct path:**

- [ ] **Test print outcome recorded**: PASS / MINOR-ADJ / FAIL / PARTIAL-FAIL *(circle one)*
- [ ] **If FAIL**: Root cause identified? YES / NO *(circle one)*
  - If NO: Confidence <70%. Route to **A2 (Fallback Pivot)** or escalate to expert
  - If YES: Confidence ≥70%. Route to **A1 (v2 Redesign)**
- [ ] **If PARTIAL-FAIL**: Pick B1 or B2
  - [ ] Option B1 (Launch passing + iterate): Passing SKU revenue >$100/month? YES / NO
  - [ ] Option B2 (Full redesign): Failing SKU is core product? YES / NO
- [ ] **Timeline criticality**: Must launch by June 15 (market window)? YES / NO
  - If NO: Can afford 2-week delay (June 6+ replan). More flexibility on iterations.
  - If YES: Prioritize speed. Pick A2/fallback if v2 confidence is <80%.
- [ ] **Decision locked**: Write your chosen path in project log (A1 / A2 / B1 / B2 / expert escalation)
  - Time to decision: <15 minutes
  - Confidence in decision: 80%+ (if <80%, escalate to expert before Day 1 afternoon)

---

## Escalation Path: When to Ask for Expert Help

**If test print fails and root cause is unclear, consider escalating to expert (3D printing community or consultant) before spending 5-7 days on v2 iteration.**

**When to escalate** (any of these conditions):
- Root cause is unclear after inspection (≤3 competing hypotheses)
- Confidence in fix is <60%
- You've already iterated once (Outcome B retest failed) and facing another iteration
- You're unsure whether to proceed with v2 redesign vs. pivot to fallback

**Escalation channels** (ranked by speed + expertise):
1. **Bambu Lab Discord community** (fastest: 30-60 min response) — tag @support or moderators with photos
2. **r/3Dprinting subreddit** (1-2 hour response) — post with [HELP] tag + photos + measurements
3. **Local maker community** (2-4 hours) — check local Slack/Discord
4. **Paid consulting** ($50-200/hour) — Fiverr 3D printing experts, professional FDM consultants
5. **Printer manufacturer support** (24-48 hours) — Bambu Lab support email (slower but authoritative)

**Escalation format** (what to share):
```
HELP NEEDED: Test print failed. Snap-arm [description of failure].

Test print specs:
- Material: PLA+ (eSUN brand)
- Nozzle temp: 220°C
- Layer height: 0.20mm
- Print speed: 60 mm/s
- Snap-arm dimensions: [measured values]

Photos:
- [Snap-arm close-up]
- [Side view of crack/issue]

Possible causes I'm considering:
1. Under-extrusion (measured too thin?)
2. Stress concentration (design geometry issue?)
3. [Other hypothesis]

Question: What does this failure pattern suggest? Any recommendations?
```

**Decision timeline**:
- Post to Discord/Reddit: Day 1 afternoon (~2 PM)
- Wait for expert response: Day 1 evening (4-6 PM) or Day 2 morning
- Implement recommendation: Days 2-3
- Test: Day 3-4
- Decision on A1 vs. A2: Day 4 (based on expert input)

**Cost-benefit**: Spending 4-6 hours waiting for expert feedback can save 3-5 days of iterating on wrong hypothesis. Worth it if confidence is <70%.

---

## Final Routing Summary Table

**Print this table and fill in your outcome. One-stop routing guide:**

| Your Test Print Outcome | Immediate Route (Day 1) | CAD Action | Timeline to Launch | Expected Revenue |
|---|---|---|---|---|
| ✅ PASS | Launch path (standard sequence) | None | May 30 | $180-400/month |
| ⚠️ MINOR-ADJ | Quick tolerance tweak (1-day iteration) | Edit snap-arm ±0.1mm | May 31 | $180-400/month |
| 🔴 FAIL (clear root cause) | Scenario A1: v2 redesign | Fix identified issue (flow, temp, tolerance) | May 30-31 (if v2 passes) | $180-400/month |
| 🔴 FAIL (unclear cause) | Scenario A2: Fallback pivot OR escalate expert | Simplify design, abandon snap-arm | June 2-5 | $60-240/month (fallback) |
| 🟡 PARTIAL (1 of 3 passes) | Scenario B1: Launch 1, iterate 2 in parallel | Redesign failing size only | May 30 + June 2-5 | $300-400/month |
| 🟡 PARTIAL (2 of 3 pass) | Scenario B1 preferred | Redesign 1 failing size | May 30 + June 2-5 | $300-400/month |
| 🟡 PARTIAL (borderline all) | Scenario B2: Coordinated redesign all 3 | Redesign all 3 sizes relaxed tolerance | June 1-2 | $400-500/month |

---

## Decision Commitment Format

**On Day 1, after test print evaluation, document your decision using this format (copy to project log):**

```
TEST PRINT DECISION LOG — [DATE]

Outcome: [PASS / MINOR-ADJ / FAIL / PARTIAL-FAIL]
Severity: [None / Low / Medium / High]
Root cause (if failure): [description or "unclear"]
Confidence in fix: [%]

Routing decision: [A1 / A2 / B1 / B2 / Expert escalation]

Rationale: [1-2 sentences on why this route]

Timeline commitment:
- Days 1-3: [specific CAD or prep action]
- Days 4-7: [test or production action]
- Launch target: [date]

Capital budget: $[amount]

Next action: [specific task to start today]
Next review: [date/time for Day 3 or Day 7 gate]

Signed: [user name] on [timestamp]
```

**Example filled-in:**
```
TEST PRINT DECISION LOG — May 26, 2026, 2:00 PM

Outcome: FAIL
Severity: High (snap-arm cracked)
Root cause (if failure): Likely under-extrusion (snap-arm measured 0.9mm vs. 1.4mm spec)
Confidence in fix: 85%

Routing decision: A1 (v2 Redesign)

Rationale: Clear root cause (under-extrusion symptom). High confidence fix is straightforward (increase flow +3%). Quick retest on Day 2 will confirm. Risk is low.

Timeline commitment:
- Days 1-2: Adjust slicer flow, retest Day 2 evening
- Days 3-4: Production batch printing
- Launch target: May 30-31

Capital budget: $80-150 (local print service + materials)

Next action: Open Bambu Studio, adjust flow +3%, regenerate G-code for v2 test print tonight

Next review: Day 2 evening (after v2 retest), evaluate if v2 passes or escalate to A2

Signed: user on May 26, 2026, 14:00 UTC
```

---

---

## Commitment & Sign-Off

This decision tree is real-time routing. Use it immediately upon receiving test print result (Day 1, ~15 minutes after evaluation).

**Required actions**:
1. Complete test print inspection (test-print-failure-recovery-plan.md Section 1)
2. Record outcome on this decision tree
3. Follow routing path to correct scenario (A1, A2, B1, B2, or escalation)
4. Begin Day 1 execution per POST_TEST_PRINT_FAILURE_EXECUTION_PLAN.md

**No further planning needed.** All contingencies are pre-staged. Decision tree simply routes to the right plan.

---

**Document Status**: Production-ready  
**Version**: 1.0  
**Created**: 2026-05-26  
**Last Review**: 2026-05-26  
**Author**: SuperClaude Orchestrator  

**Related Documents**:
- POST_TEST_PRINT_FAILURE_EXECUTION_PLAN.md (detailed execution for each scenario)
- FAILURE_SCENARIO_RESOURCE_ALLOCATION_MATRIX.md (capital and timeline tradeoffs)
- test-print-failure-recovery-plan.md (diagnostic procedures)
- ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md (standard launch sequence if PASS)
