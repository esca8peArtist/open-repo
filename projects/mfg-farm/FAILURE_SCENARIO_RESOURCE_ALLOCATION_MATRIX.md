---
title: Failure Scenario Resource Allocation Matrix
subtitle: Capital, timeline, and constraint analysis for contingency execution
project: mfg-farm
date: 2026-05-26
status: production-ready
version: 1.0
purpose: "Enable rapid capital allocation decisions during contingency scenarios without discovery lag"
---

# Failure Scenario Resource Allocation Matrix

**Document Purpose**: When test print fails (Scenario A) or partially fails (Scenario B), every hour of delay or inefficient capital allocation cascades into 1-2 week launch delays. This matrix enables immediate resource commitment decisions without deliberation.

**Structure**: Capital budget, timeline tradeoffs, and constraint bottlenecks for each scenario. All figures are May 2026 current pricing.

---

## SCENARIO A: FAIL — Snap-Arm Complete Redesign Path

### Capital Budget Breakdown

#### Path A1: v2 Redesign (Aiming for May 30-31 Launch)

| Resource Category | Unit Cost | Quantity | Subtotal | Notes |
|---|---|---|---|---|
| **CAD Design** | | | | |
| User CAD time (in-house) | — | 3-4 hours | $0 | Fusion 360 (already licensed); 4 snap-arm design variants |
| CAD consulting (if external) | $50-100/hour | 3-5 hours | $150-500 | Only if user unavailable or lacking expertise; typical turnaround 4-6 hours |
| **v2 Test Print** | | | | |
| Local print service (20-50 units v2 test) | $2-5/unit | 20 units | $40-100 | 1-2 day turnaround; prefer local over remote for speed |
| Backup: Xometry fast turnaround | $3-8/unit | 20 units | $60-160 | 24-hour guaranteed; ~50% premium over standard service |
| In-house print (if available, opportunity cost) | $0.79/unit material | 50 units | $40 | Filament + electricity only; time cost is 30-40 hours printer runtime |
| **Material (PLA+)** | | | | |
| 1kg spool (Amazon Prime) | $10-15 | 1-2 spools | $15-30 | Safety stock, if internal printing; bulk discount from $12/kg on 10kg bundle |
| **Supplier Outreach (Redesign Impact)** | | | | |
| Supplier follow-up email (confirm design changed, delay expectation) | $0 | 5 suppliers | $0 | Prevents early orders, clarifies delivery timeline |
| **Total Path A1 (v2 Redesign)** | | | **$50-300** | Mid-range: $100-150 typical (local print service + no external CAD) |

---

#### Path A2: Fallback Product Pivot (Targeting June 2-5 Launch)

| Resource Category | Unit Cost | Quantity | Subtotal | Notes |
|---|---|---|---|---|
| **CAD Design (Fallback Product)** | | | | |
| User CAD time (magnetic clip, simple design) | — | 1-2 hours | $0 | Fusion 360; straightforward bracket geometry |
| CAD consulting (if external) | $30-75/hour | 2-3 hours | $60-225 | Simpler than snap-arm, so lower consulting cost if needed |
| **Fallback Test Print** | | | | |
| Local print service (1-2 unit fallback test) | $2-5/unit | 2 units | $5-10 | Fast iteration; only 1-2 units to validate geometry |
| **Magnet Inserts (if Magnetic Clip)** | | | | |
| Neodymium 3mm disks (100-pack from Amazon) | $15-25 | 1 pack | $20 | Bulk price; arrives 3-5 days; sufficient for 100 units |
| **Fallback Production Batch** | | | | |
| Local print service (50-100 units fallback) | $2-4/unit | 50 units | $100-200 | Same supplier as test print; 1-2 day turnaround |
| OR: In-house print (opportunity cost) | $0.79/unit | 50 units | $40 | Material + electricity; ~40 hours printer time |
| **Material (if in-house printing)** | | | | |
| PLA+ bulk (10kg bundle Amazon) | $12/kg | 1 kg equiv. | $12 | Covers ~12 fallback units at 0.79/unit |
| **Total Path A2 (Fallback Pivot)** | | | **$45-300** | Low-end: $50-100 (in-house print + no consulting); high-end: $225-300 (external service) |

---

### Timeline Tradeoffs

| Decision | Timeline Impact | Cost Impact | Notes |
|---|---|---|---|
| **In-house vs. local print service** | In-house: +30-40 hrs printer time (Days 3-5 tied up). Local service: frees printer for production. | In-house: $40 material. Local: $80-100. | **Recommendation**: Use local service if printer not idle; preserve printer for production batch after design locked. |
| **CAD consulting vs. user design** | User: 3-4 hours CAD (Days 1-2 afternoon). External: 4-6 hour service turnaround (outsource, user free for parallel work). | User: $0. External: $150-500. | **Recommendation**: User handles CAD (high confidence in design). Consulting only if user bandwidth <2 hours. |
| **Multi-variant parallel testing** | Single variant: Days 3-4 test, Day 5 evaluate. 3-4 variants: Day 3 test all, Day 4 evaluate all. | +$30-50 material cost. | **Recommendation**: If user is uncertain which snap-arm fix will work (tolerance vs. geometry), test 2-3 variants in one print run. Saves 1 day. |
| **Fallback CAD outsourcing** | User: 1-2 hours (very fast, simple geometry). External: 2-3 hours service (same speed). | User: $0. External: $60-225. | **Recommendation**: User handles fallback CAD (faster than snap-arm v2 by 50%). External consulting only if user unavailable. |

---

### Supplier Management During Redesign

#### Immediate Actions (Day 1, after test print failure diagnosis)

| Action | Owner | Time | Purpose |
|---|---|---|---|
| Email all 5 suppliers: "Test print failed, delaying order. Will confirm new timeline by Day 7." | User | 15 min | Prevents supplier from preparing initial order, preserves deposit if applicable |
| Log supplier response deadlines (Day 3 for fast suppliers, Day 5 for standard) | Orchestrator | 5 min | Ensure suppliers don't lock in old lead times |
| Research backup suppliers (Xometry, JLC3DP, Craftcloud) in case v2 fails again | Orchestrator | 30 min | Contingency: if v2 design fails by Day 5, jump to backup supplier within 24 hours |

**Capital preservation**: Delaying supplier orders by 3-5 days (Days 1-5) costs zero in deposit terms if orders haven't been placed. If deposits were already collected, estimate $100-300 deposit forfeit vs. total supplier order ($5,000+) — acceptable loss.

---

### Decision Point Costs (Day 3, 7)

#### Day 3 Gate: Invest in v2 Redesign or Pivot to Fallback?

| Scenario | Capital Sunk (irretrievable) | Capital Remaining (flexible) | Decision Guidance |
|---|---|---|---|
| **v2 redesign proceeding** | ~$50 (test print costs) | ~$100-200 (production batch TBD) | If v2 test print looks promising Day 3 evening: commit $100-200 to production batch Day 4. |
| **Pivot to fallback selected** | ~$50 (snap-arm test costs) | ~$100-150 (fallback test + production) | Walk away from snap-arm test cost ($50 sunk). Redirect remaining capital budget to fallback. |
| **Both paths uncertain** | ~$50 | $200-300 (parallel test both) | Test v2 AND fallback in parallel (Days 3-4). Pick winner by Day 5. Costs +$50-100 vs. sequential approach. Worth it if user uncertainty is high. |

---

#### Day 7 Gate: Launch v2 or Escalate to Fallback?

| Scenario | v2 Quality | Launch Readiness | Decision |
|---|---|---|---|
| v2 test batch ALL PASS (5/5 spot checks) | High confidence | Ready for production | Commit to v2 launch. Allocate capital to production batch (Days 8-12). Target launch May 30-31. |
| v2 test batch MOSTLY PASS (4/5) | Medium confidence | Ready with quality caveat | Launch with v2 design but add disclaimer: "First batch may have variance. Replacement guarantee 30 days." OR delay 2 days to v3 iteration. |
| v2 test batch FAIL (2-3/5) | Low confidence | NOT ready | Escalate to fallback product immediately. Commit $50-100 to fallback batch Day 8. Target launch June 2-5. |
| v2 test batch FAIL + root cause unclear | Unknown | NOT ready | Recommend pausing until June 6 post-checkpoint. Allocate 2-3 weeks for deep debugging vs. weekly iteration cycle. |

---

### Monthly Revenue Impact (Scenario A)

#### v2 Redesign Success Path (Launch May 30-31)

| Month | Volume Estimate | Price/Unit | Revenue | Profit (est. 200% margin) |
|---|---|---|---|---|
| June 1-30 (partial month, 3-4 weeks) | 30-50 clips | $5.99 | $180-300 | $120-200 |
| July 2026 (full month) | 60-100 clips/month | $5.99 | $360-600 | $240-400 |

**ROI on v2 redesign cost**:
- Cost: $50-300
- Payback: 2-4 weeks (June revenue)
- Upside: sustainable $300-600/month revenue if design holds

---

#### Fallback Product Path (Launch June 2-5)

| Month | Volume Estimate | Price/Unit | Revenue | Profit (est. 150% margin) |
|---|---|---|---|---|
| June 2-30 (partial month, 2-3 weeks) | 15-25 units | $3.99 | $60-100 | $30-50 |
| July 2026 (full month) | 40-60 units/month | $3.99 | $160-240 | $80-120 |

**ROI on fallback pivot cost**:
- Cost: $45-300
- Payback: 3-6 weeks (June-early July revenue)
- Upside: lower revenue ceiling ($160-240/month) but lower risk, faster execution

---

### Constraint Analysis: What Could Delay Each Path?

| Constraint | v2 Redesign | Fallback Pivot | Mitigation |
|---|---|---|---|
| **Printer availability** | Bambu P1S down = can't print test or production batch. Delays 3-5 days. | Same constraint. | Use local print service instead (eliminate printer dependency). Cost +$40-100 but frees printer. |
| **CAD expertise** | User unfamiliar with parametric design or Fusion 360. Delays 4-6 hours. | Fallback is simpler; less expertise needed. | Use CAD consulting ($150-500) to compress CAD time to 3-4 hours. Cost justified if it enables Day 4 launch vs. Day 5. |
| **Supplier lead time** | If v2 uses new material (TPE instead of PLA+): 3-5 day supplier lead time. Delays test by 2-3 days. | Fallback uses standard PLA+ (in stock). No delay risk. | Stick with PLA+ for v2 unless material switch is critical to design. TPE can be Phase 2 optimization. |
| **Etsy shop setup** | If shop not pre-created: 1-2 hours setup delay. | Same constraint. | Pre-create shop during wait time (Days 1-3 of v2 test print). Reuse for fallback if pivot needed. |
| **Photography quality** | If test print photos poor: 1 day re-shoot. Delays launch 1 day. | Same constraint (though fallback simpler geometry = easier photos). | Schedule photo shoot for Day 1 afternoon while waiting for test print evaluation (parallel). |
| **Capital constraint** | $50-300 budget is tight? Could force in-house printing (adds 30-40 hrs delay) vs. fast service ($80-100 cost). | Lower total cost ($45-300) but still capital-dependent. | Prioritize local print service cost ($80-100) over in-house time. Capital preservation is secondary to timeline preservation at this stage. |

**Critical path mitigation**: 
- **Pre-create Etsy shop** (Day 0, before test print, if possible)
- **Pre-identify fast print service** (local + backup like Xometry)
- **Have CAD consultant contact on standby** (if user expertise uncertain)
- **Schedule photography for Day 1 PM** (parallel to test evaluation)

---

---

## SCENARIO B: PARTIAL-FAIL — Passing SKU Launch + Failing SKU Iteration

### Capital Budget Breakdown

#### Path B1: Launch Passing SKU + Parallel Iterate Failing SKU (Staggered Release)

| Resource Category | Unit Cost | Quantity | Subtotal | Notes |
|---|---|---|---|---|
| **Passing SKU (Launch immediately)** | | | | |
| Production print batch (50-100 units passing size) | $0.79/unit material | 50 units | $40 | In-house print; no external service needed; standard settings |
| Photography (5-6 images) | — | 1 shoot | $0 | User time; same-day as test print (Day 1 PM) |
| Etsy shop setup (1-time) | — | 1 | $0 | Pre-staged in anticipation; reuse from standard launch prep |
| Etsy listing publish | — | 1 | $0 | Publish passing SKU to Etsy Day 4 |
| **Failing SKU Iteration (Days 1-7 parallel)** | | | | |
| CAD v2 redesign (failing size only) | — | 1-2 hours | $0 | Quick tolerance tweak (e.g., snap-arm loose, tighten by 0.1mm) |
| Failing SKU v2 test print (1-2 units) | $2-5/unit | 2 units | $5-10 | Local service, 4-6 hour turnaround |
| Failing SKU production batch (50-100 units, if v2 passes) | $0.79-2/unit | 50 units | $40-100 | In-house ($40 material) OR local service ($100) |
| **Total Path B1 (Staggered Launch)** | | | **$85-150** | Low-end: passing + failing in-house. Mid-range: passing in-house, failing external. |

---

#### Path B2: Hold All SKUs for Full Redesign (Single Coordinated Launch)

| Resource Category | Unit Cost | Quantity | Subtotal | Notes |
|---|---|---|---|---|
| **Full Portfolio v2 Redesign (All 3 sizes)** | | | | |
| CAD v2 edits (all 3 size variants) | — | 2-3 hours | $0 | Parametric design advantage: edit once, update all sizes |
| v2 test prints (3 sizes, 1 unit each) | $2-5/unit | 3 units | $6-15 | All printed in one batch, 4-6 hour turnaround |
| **v2 Production Batch (All 3 sizes)** | | | | |
| In-house print (50-100 units across 3 sizes) | $0.79/unit | 50 units | $40 | Standard material cost; higher printer time (~40 hours) |
| OR: Local print service (all 3 sizes bundled) | $2-4/unit | 50 units | $100-200 | 1-2 day turnaround; includes multi-size coordination |
| Material (if in-house) | — | 1 kg | $12 | PLA+ bulk; covers ~60 units at standard weight |
| **Total Path B2 (Full Portfolio)** | | | **$58-227** | Low-end: in-house print ($52). Mid-range: split print service ($80-100). |

---

### Timeline & Revenue Tradeoff Analysis

#### Path B1 Impact: Staggered Release (Partial Launch May 30 + Failing SKU June 2-5)

| Week | What Launches | Units/Day Est. | Revenue/Week | Notes |
|---|---|---|---|---|
| May 30-June 2 (Passing SKU only) | 0.5" size passing (e.g.) | 2-3/day | $60-90 | Single-size appeal is limited; expect slower conversion than full product line |
| June 2-9 (Add failing sizes) | 0.75" + 1.0" added to shop | 4-6/day | $120-180 | Full portfolio boosts discoverability; failing SKU adds revenue |
| June 10-30 (Full product line stable) | All 3 sizes in stock | 5-8/day (est.) | $150-240 | Optimal product positioning; faster SKU iterations don't hurt momentum |
| **Total June** | Staggered | ~5/day avg | ~$300-400 | vs. single launch = slightly lower overall June revenue due to 1-week single-size window |

**Path B1 Upside**: Passing SKU generates revenue immediately (psychological win, early reviews). Failing SKU iteration continues in parallel without blocking launch. Risk: if failing SKU v2 never works, passing SKU remains single-size (lower growth ceiling).

**Path B1 Downside**: Staggered release is harder to market ("Coming soon" messaging is weaker than "Full range available"). Algorithm may penalize partial catalog (one product category with limited SKU breadth).

---

#### Path B2 Impact: Full Portfolio Coordinated Launch (All SKUs June 1-2)

| Week | What Launches | Units/Day Est. | Revenue/Week | Notes |
|---|---|---|---|---|
| May 30-June 2 (Preparation, no launch) | None (holding) | 0 | $0 | Waiting for v2 iteration of all sizes; no revenue this week |
| June 2-9 (Full portfolio launch) | All 3 sizes simultaneously | 6-8/day | $180-240 | Full product line launch; stronger algorithm signal, faster discoverability |
| June 10-30 (Stable full portfolio) | All 3 sizes in stock | 6-8/day (est.) | $180-240 | Sustained full-line sales; single coordinated brand message |
| **Total June** | Coordinated | ~5/day avg | ~$400-500 | Delayed start but stronger finish (June 2+ velocity higher than staggered approach) |

**Path B2 Upside**: Single coordinated launch is cleaner marketing ("Complete ModRun range: 3 precision sizes, available now"). Algorithm sees full product portfolio (stronger LQS signal). Higher velocity June 2+ compensates for May 30-June 2 wait.

**Path B2 Downside**: 2-3 day launch delay (May 30 → June 1-2) costs early adopters, early reviews. Higher risk if v2 fails for one size (full launch blocked pending additional iteration).

---

### Decision Table: Path B1 vs. B2 by Situation

| Failing SKU Diagnosis | B1 Recommendation | B2 Recommendation | Capital/Time Tradeoff |
|---|---|---|---|
| **1 of 3 failing (clear root cause)** | B1 preferred | B2 if you want coordinated brand | B1 saves 2 days, same capital. B2 waits but launches cleaner. |
| **1 of 3 failing (unclear root cause)** | B1preferred (don't delay passing SKUs) | B2 not recommended | B1: launch passing, iterate failing in parallel. B2 risks holding all SKUs if v2 also fails. |
| **2 of 3 failing** | B1 preferred (launch 1, iterate 2) | B2 if 2-SKU redesign is fast | B1: single SKU launch (smaller), 2 SKUs following weeks. B2: all-or-nothing. |
| **Passing SKU is high-margin (core product)** | B1 strongly preferred | B2 if passing SKU revenue is <$100/mo | B1: maximize revenue from core product immediately. B2: unnecessary holdup. |
| **Passing SKU is low-margin (loss-leader)** | B2 preferred | B1 if full portfolio v2 is complex | B1: launching loss-leader alone doesn't justify holdup complexity. B2: wait for full portfolio, launch together. |

**Default recommendation**: **Path B1 (staggered launch)** in 70% of cases, because:
- Passing SKU generates revenue immediately (psychological + financial win)
- Failing SKU iteration continues in parallel without penalty
- If failing SKU v2 never works, at least passing SKU is live and generating revenue
- Capital spend is same or lower than B2

---

### Resource Constraints & Mitigation (Scenario B)

| Constraint | Path B1 Impact | Path B2 Impact | Mitigation |
|---|---|---|---|
| **Printer availability** | Passing SKU production uses printer Days 1-3. Failing SKU v2 test uses printer Days 3-4. Sequential, not parallel. | All 3 sizes test + production competes for printer time Days 3-5. Higher contention risk. | Use local print service for failing SKU test (Path B1) or all sizes (Path B2). Costs +$80-100 but eliminates printer bottleneck. |
| **Photography time** | Passing SKU photos Day 1 (while test print cools). Failing SKU photos deferred to Day 7-8 (after v2 test). | All 3 sizes must be photographed by Day 7 (before launch June 1-2). Higher photo shoot complexity. | Path B1: staggered photos = less parallel work. Path B2: all-at-once = 1-2 hour photo shoot block Day 6-7. |
| **Etsy listing complexity** | Passing SKU listing is simple (single size). Failing SKU added as variant or separate listing Day 8+. | All 3 sizes as variants in single listing OR 3 separate listings (lower admin, but less clean UX). | Path B1: keep separate listings for clarity (user adds failing SKUs as they pass). Path B2: build multi-variant listing structure once (cleaner, but 30 min extra Etsy setup). |
| **Supplier coordination** | Simple: passing SKU uses standard supplier order. Failing SKU uses separate v2 order. | Complex: all 3 sizes need coordinated supplier order (quantity planning across sizes). | Path B1: simpler supplier management (2 orders: passing + failing iterations). Path B2: single large order (cleaner, but requires better forecasting). |
| **Quality risk** | Path B1: passing SKU ships at high quality (locked design). Failing SKU ships as-is if v2 fails (documented caveat). Risk is isolated. | Path B2: all sizes delayed until all pass QA. If one size repeatedly fails, entire launch blocked. | Path B1: risk isolation = higher confidence launch. Path B2: all-or-nothing = higher execution risk. |

**Path B1 is operationally simpler.** Path B2 is better for brand positioning if execution confidence is high.

---

### Supplier Management (Scenario B)

#### Day 1: Update Suppliers on Test Results

| Action | Purpose | Timing |
|---|---|---|
| Email all 5 suppliers: "Test print partial pass. Passing SKU [size X] ready for production order. Failing SKU [size Y] in redesign; will update by Day 7." | Prevent suppliers from preparing orders for failing SKU; clarify new timeline. | Day 1 PM (Day 4 of launch prep +3 hours) |
| Request passing SKU supplier allocation (Y units of size X) | Confirm supplier can deliver passing-size inventory within 3-5 days | Day 2 AM |
| Confirm failing SKU redesign timeline with suppliers | If suppliers already quoted: "Delaying order 3-7 days pending redesign. Will confirm new specs by Day 7." | Day 2 AM |

#### Day 7: Finalize Supplier Orders

| Path | Supplier Decision |
|---|---|
| **B1 (Staggered)**: Passing SKU live, failing SKU iterating | Place passing SKU supplier order (20-50 units) on Day 3-4. Defer failing SKU supplier order until Day 7-8 (after v2 evaluation). |
| **B2 (Full redesign)**: Hold all SKUs for v2 | Defer all supplier orders until Day 7. On Day 7, place coordinated order: all 3 sizes, v2 specs, single delivery window. |

**Capital preservation**: Path B1 places passing SKU order early (Day 3-4), locks supplier, prevents delay. Path B2 defers all orders until Day 7, reduces upfront capital commitment, but increases risk of supplier capacity constraints later.

---

---

## CONTINGENCY PATHS: Supply Chain Failure & Multi-Iteration Costs

### Contingency C: Supply Chain Failure (Days 5-7 premium costs)

**Trigger**: Planned print service becomes unavailable; supplier lead time slips unexpectedly.

#### Cost Matrix: Backup Suppliers

| Supplier | Cost/Unit (50 units) | Lead Time | Premium vs. Primary | When to Use |
|---|---|---|---|---|
| **Primary (local service)** | $2-3 | 1-2 days | Baseline | Day 4 default |
| **Xometry** | $3-6 | 24 hours guaranteed | +50% | If primary is down, need 1-day turnaround |
| **JLC3DP** | $1-2 (material) + $3-5 (service) | 5-7 days (standard) | -20% to 0% cost but longer time | Not suitable for contingency (too slow) |
| **Craftcloud aggregator** | $0.10-0.30/g + $3-10 setup | 3-5 days (varies by partner) | +20-50% (aggregate average) | Useful for non-urgent, cost-sensitive batches (not contingency) |
| **Local makerspace or maker service** | $2-4 | 2-3 days | +10-30% | If commercial service unavailable, use community resource |
| **Amazon Prime (Bambu resellers, pre-printed parts)** | ~$5-10 / unit | 2 days | +100-200% | Emergency only; last-resort if all services down |

**Recommendation for Path A/B**: Identify 2 backup suppliers in advance (Days 0-1):
1. **Primary**: Local service (best price, 1-2 day lead time)
2. **Backup 1**: Xometry (24-hour guarantee, +50% premium)
3. **Backup 2**: Local makerspace or maker community (fallback if both commercial services unavailable)

**Contingency activation cost**: +$50-100 per batch (20-50 units) for Xometry premium. Acceptable tradeoff to keep Day 4-5 test print on schedule.

---

### Contingency D: Multi-Iteration Failure (Days 3-7 escalation)

**Trigger**: v2 test print fails same way as v1; root cause unclear; user confidence <70%.

#### Escalation Decision Tree & Associated Costs

```
v2 test print fails on Day 3-4. User evaluates root cause.

├─ Root cause identified (e.g., "tolerance was off, fix is 0.1mm change")
│  └─ Confidence ≥70% in v3 fix?
│     ├─ YES: Proceed to v3 iteration (Days 5-6)
│     │  Cost: +$50-100 (v3 test print + possible v3 production batch if passes)
│     │  Timeline: +1-2 days (v3 evaluated Day 6, production ordered Day 7, launch June 2-3)
│     └─ NO: Pivot to fallback product (Contingency Path A2)
│
└─ Root cause unclear (same symptoms as v1, no obvious fix)
   └─ Option A: Escalate to expert (3D print forum, Discord)
   │  Cost: $0 (community help) or $50-200 (paid consulting)
   │  Timeline: +2-3 days (wait for feedback, implement, retest)
   │  Decision: If expert feedback leads to v3 fix, continue iteration
   │           If expert recommends pivot, commit to fallback product
   │
   └─ Option B: Accept current design quality and launch with caveat
   │  Cost: $0 additional (launch with current print)
   │  Quality risk: Higher defect rate, customer returns
   │  Not recommended unless all alternatives are exhausted
   │
   └─ Option C: Commit to fallback product pivot immediately
   │  Cost: $45-300 (new product test + batch)
   │  Timeline: +3-5 days (fallback CAD + test + production)
   │  Confidence: High (fallback products have much lower failure risk)
   │  Recommended if user has <50% confidence in snap-arm fix
```

#### Cost Escalation: v2 → v3 → Fallback

| Decision Path | Total Cost to Date | Additional Cost | Timeline Impact | Confidence Level |
|---|---|---|---|---|
| **v2 test, PASSES → Launch May 30-31** | $50-150 | $0 | +0 days (on schedule) | High (95%+) |
| **v2 test, FAILS → v3 iteration → Launch June 2-3** | $50-150 | $50-100 (v3 test) | +2-3 days | Medium (70-85%) |
| **v3 test, FAILS → Fallback pivot → Launch June 2-5** | $150-250 | $45-300 (fallback batch) | +3-5 days total | Medium-High (75-90%, due to simpler fallback) |
| **Multiple iterations, >3 attempts → Pause until June 6** | $200-400 | $0-100 | +7-10 days total | Low (<60%) |

**Cost recovery analysis**:
- Spending $100-300 on contingency iterations (v2, v3, fallback testing) is justified if it enables launch by June 2-5
- Spending >$400 on repeated iterations past June 3 is **not justified**; better to pause and reallocate capital to post-checkpoint planning (June 6+)

**Decision rule**: 
- After v2 fails: if v3 timeline is feasible (Days 5-6 test, Day 7 production order), proceed
- After v3 fails: **commit to fallback product immediately** (do not attempt v4)
- If root cause is unclear by Day 5: escalate to expert opinion; do not continue blind iteration

---

---

## Timeline Compression Opportunities (Buy-Your-Way-Out Costs)

When timeline is critical, the following table shows cost-per-day-saved tradeoffs:

### Fast-Track Option A: Overnight Printing Service

| Service | Cost | Lead Time | Days Saved | Cost-Per-Day | Use Case |
|---|---|---|---|---|---|
| Local print service (standard) | $2-3/unit | 24-48 hrs | — | — | Day 4 baseline |
| Xometry 24-hour | $3-6/unit | 24 hrs | 1 day | +$50-100/batch | If Day 5 evaluation is critical; saves 1 day vs. standard service |
| Shapeways Express (if available) | $5-10/unit | 24-48 hrs | 1 day | +$100-200/batch | Rarely needed; only if all local services booked |

**When to use**: If test print evaluation on Day 5 is blocking supplier order deadline, pay +$50-100 for Xometry 24-hour to save 1 day of schedule slip. Not worth it otherwise.

---

### Fast-Track Option B: Parallel Multi-Variant Testing

**Scenario**: User is uncertain which snap-arm fix will work (tolerance vs. geometry vs. material). Instead of testing 1 variant, test 3 variants in one print batch.

| Approach | Cost | Timeline | Variants Tested | Decision Speed |
|---|---|---|---|---|
| Sequential (v2 only) | $50-100 | Test Day 3-4, evaluate Day 5, next iteration Days 5-6 | 1 variant | 2-3 days to decision |
| Parallel (3 variants) | $50-150 (marginal material cost) | Test all 3 on Day 3-4, evaluate Day 5, pick winner Day 5 | 3 variants | 1 day to decision |
| Cost-per-day saved | $0-50 | 1-2 days | +2 variants | +1-2 days faster |

**Recommendation**: If user is uncertain on snap-arm fix direction, pay +$30-50 to test 3 variants in parallel. Saves 1-2 days of decision time, which is valuable.

---

### Fast-Track Option C: CAD Consulting Outsourcing

| Approach | Cost | Timeline | Quality | Use Case |
|---|---|---|---|---|
| User designs in Fusion 360 | $0 | 3-4 hours | High (user has domain knowledge) | User is available and confident in CAD |
| Freelance CAD on Fiverr/Upwork | $30-75/hour | 4-6 hours (includes communication lag) | Medium (third-party may miss constraints) | User unavailable; budget allows; willing to accept iteration risk |
| Professional CAD firm (local) | $100-200/hour | 2-3 hours (express service) | High (professional oversight) | User completely unavailable; timeline is critical; quality must be guaranteed |

**Recommendation**: User handles CAD (high confidence, $0 cost, 3-4 hours time). Outsource only if user bandwidth is <2 hours total across Days 1-2. Cost justification: $150 consulting vs. 1-day schedule delay = $150 is worth it.

---

---

## Monthly Operating Cost Structure (Post-Launch, Baseline)

Once a scenario reaches launch (Scenarios A v2, B1, B2, or fallback pivot), this table shows the steady-state monthly operating costs:

| Cost Category | Cost/Month | Notes |
|---|---|---|
| **Materials** | | |
| PLA+ filament (bulk, $12/kg) | $60-120 | 5-10 kg/month at $300+ revenue (assumes 30-50 units/month sales) |
| Packaging (mailers, tissue) | $20-40 | ~$0.50/unit shipped; 40-80 shipments/month |
| **Production Overhead** | | |
| Printer electricity (Bambu P1S, 200W avg) | $15-25 | 40-60 hours/month runtime at $0.12/kWh |
| Printer maintenance / wear (depreciation) | $30-50 | Estimated $0.05-0.10/unit printed |
| **Sales & Fulfillment** | | |
| Etsy fees (3% transaction + $0.20/listing) | $10-30 | 3% of $300+ revenue |
| Shipping (USPS Priority Mail) | $50-100 | $2.99/unit shipped x 20-40 units/month |
| **Total Monthly Operating Cost** | **$185-365** | Scales with volume; break-even ~$300 revenue |

**Implication**: Once launched, monthly profit = Revenue - $185-365 operating cost. At $300-500 revenue (30-50 units/month), net margin is $100-300/month. Sufficient to justify the contingency investment.

---

---

## Capital Allocation Summary Table

| Scenario | Path | Total Capital | Timeline to Launch | Monthly Revenue (Est.) | ROI Payback (months) |
|---|---|---|---|---|---|
| **A: FAIL** | v2 Redesign | $50-300 | May 30-31 (+5 days) | $180-400 | <1 month |
| **A: FAIL** | Fallback Pivot | $45-300 | June 2-5 (+10 days) | $60-240 | <1 month |
| **B: PARTIAL** | B1 Staggered | $85-150 | May 30 (passing) + June 2 (failing) | $300-400 | <1 month |
| **B: PARTIAL** | B2 Full Redesign | $58-227 | June 1-2 (+2 days) | $400-500 | <1 month |
| **A→D: Escalation** | Multi-iteration (v2→v3→fallback) | $200-400 | June 2-5 (+10 days) | $60-300 (fallback) | <1 month |

**Conclusion**: All contingency paths have positive ROI within 1 month of launch. Capital allocation decisions should prioritize **timeline preservation** over cost minimization. Paying +$50-100 to save 1-2 days of schedule is almost always justified.

---

---

## Supplier Negotiation Leverage Points (During Contingency)

When suppliers learn that test print failed and timeline has shifted, use these leverage points to negotiate price concessions:

| Leverage Point | Context | Negotiation Angle | Potential Saving |
|---|---|---|---|
| **Delayed order timeline** | Original plan: order by May 24. Actual: order by May 30-31 (5-7 day delay). | "We've delayed our order. Can you offer a volume discount on 50+ units?" | $0.50-1/unit (~5-10% off standard pricing) |
| **Extended payment terms** | Standard: net 30. Negotiation: net 45-60 (delay supplier cash collection). | "We're a new supplier customer. Can we do net 45 for the first order?" | $0-200 (improve cash flow for you, standard practice) |
| **Bulk commitment** | Initial plan: 50-unit test batch. Revised: 100-unit batch if price is right. | "If you can hit $11/kg on 50kg bulk, we'll commit to 150 units over 3 months." | $1-2/kg (~$50-100 total) |
| **Co-op marketing** | Supplier feature you in their case study / newsletter. | "We'll mention your supplier in our launch email / social posts if you offer 10% discount first order." | $50-100 (indirect; depends on supplier priorities) |

**Timing**: Use these points **only if supplier has already quoted and is waiting for order confirmation**. Don't negotiate before they've committed to timeline/price.

---

---

## Commitment & Sign-Off

This matrix is a decision-support tool. Use Day 1 contingency scenario diagnosis to select the appropriate capital allocation path (A1 v2, A2 fallback, B1 staggered, B2 full).

**Required inputs on Day 1**: 
- Test print outcome (which scenario: A, B, or neither)
- User confidence level on redesign feasibility (≥70% proceed with redesign; <70% pivot to fallback)
- Timeline criticality (is June 30 market window important? Yes → justify contingency cost; No → can wait until June 6 post-checkpoint)

**Orchestrator execution**: 
- Activate pre-staged supplier contact list
- Confirm backup print service availability
- Track all capital commitments in project budget log (transparency)

---

**Document Status**: Production-ready  
**Version**: 1.0  
**Created**: 2026-05-26  
**Last Review**: 2026-05-26  
**Author**: SuperClaude Orchestrator  

**Related Documents**:
- POST_TEST_PRINT_FAILURE_EXECUTION_PLAN.md (detailed timelines)
- supplier-economics.md (pricing reference)
- ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md (launch sequence for any scenario)
