---
title: Post-Test-Print Revenue Maximization Framework
project: mfg-farm
created: 2026-05-13
status: active — awaiting test print result (May 13–14 window)
scope: Decision framework for both PASS and FAIL scenarios; Batch 1 + Batch 2 execution; 12-month product roadmap
related: production-workflow-v1.md, headphone-hooks-execution-checklist.md, revenue-ramp-metrics.md, batch-3-candidate-research.md, batch-3-4-launch-sequencing.md, scaling-cost-levers.md, etsy-seo-strategy.md
confidence: high — all unit economics sourced from verified cost-model-spreadsheet.csv and previously completed research
---

# Post-Test-Print Revenue Maximization Framework

**Lead finding:** The test print outcome is a fork in the road with very different 30-day consequences, but the 90-day destination is the same either way. If the snap arm passes, the revenue clock starts immediately — first Etsy order within 2–3 weeks is achievable. If it fails, the 2–3 week design iteration delay pushes the revenue start but does not threaten the 6-month target. In both cases, Batch 2 (headphone hooks) proceeds on its own timeline: the hook design has no dependency on ModRun's snap arm geometry, and it can launch 3–4 weeks after test print completion regardless of outcome. The most important decision in the first 72 hours after the test print is not the design decision — it is whether you start the headphone hook print queue while the ModRun result is still being evaluated.

---

## Part 1: Batch 1 Post-Test-Print Decision Framework

### 1.1 The Four Gates (Read Before Evaluating Your Test Print)

Do not treat the test print as pass/fail on overall aesthetics. Evaluate each gate independently:

| Gate | Pass Criterion | Fail Criterion |
|---|---|---|
| Snap arm function | Click-fit engages smoothly, holds cable under lateral pull, releases cleanly with one hand | Arm cracks under light load, does not click, rattles under cable, or requires two-hand release |
| Dimensional accuracy | Snap arm 1.35–1.45mm; bore within ±0.5mm of nominal | Any dimension outside the acceptance band |
| Support removal | Clean release; no surface damage at support interfaces | Torn surface or visible scar >1mm on snap arm functional face |
| Finish quality | Layer lines visible but uniform; no stringing across bore | Stringing inside bore, base warping, blobs on exterior near snap arm |

A "near-pass" (3 of 4 gates green, one marginal) is not a fail — it is a 1-day fix. See section 1.3 below.

---

### 1.2 Scenario A: Test Print PASSES (4/4 or Near-Pass Resolved)

#### Immediate Actions (Days 0–2)

1. Lock FDM_TOLERANCE in the CadQuery source. Record the confirmed value in a git commit tagged `v1.0`. From this point, `/stl/v1.0/` is write-protected.
2. Create and save the Bambu Studio production slicer profile: `ModRun-PLA-Production-v1`. Parameters are in `production-workflow-v1.md` Section 1.2.
3. Start the first 12-clip production plate that evening. Target: overnight print, harvest Day 1 morning.
4. Place Day 0 materials order: 2× eSUN PLA+ 1kg black, 1× white (Amazon Prime, 1–2 day delivery). 100× kraft mailer boxes, 100× poly mailers.
5. Pull up the Etsy listing draft from `post-test-print-doc-2-etsy-listing-design-templates.md`. Do not publish yet — photos first.

#### Photography Window (Days 3–7)

You need a minimum of 5 photos before listing. Shoot over one session — this is a 60–90 minute exercise with the existing desk setup:

- Hero lifestyle (clips on rail, cables routed, desk clean)
- Snap arm close-up showing the click mechanism
- Multi-bore comparison (6mm / 8mm / 12mm side by side)
- Bundle layout (clips + rail arranged on white background)
- In-situ use-case: cable entering and exiting the clip

Ship nothing before photographs are done. The first photos establish the listing's click-through rate and that rate determines 90-day revenue more than any other single decision.

#### Etsy Listing and First Orders (Days 7–14)

- Publish listing Thursday 10 AM–2 PM (peak Etsy search traffic window per `etsy-seo-strategy.md`).
- Enable Etsy Ads at $1.00/day immediately on publish.
- Set processing time to 3–5 business days. Do not understate this.
- First-week target: 50+ views, 1+ order. If views are under 30 after 7 days with Ads running, the hero photo needs to change — swap to the in-situ use-case shot.

#### 90-Day Revenue Projection (Pass Scenario)

[ASSUMPTION: Pricing follows `revenue-ramp-metrics.md` blended AOV of $24.99 at 70% bundle / 30% rail mix.]

| Period | ModRun Units | Gross Revenue | Net After Fees |
|---|---|---|---|
| Month 1 (Weeks 1–4) | 30–50 | $750–1,250 | $600–1,000 |
| Month 2 (Weeks 5–8) | 60–90 | $1,500–2,250 | $1,200–1,800 |
| Month 3 (Weeks 9–12) | 80–110 | $2,000–2,750 | $1,600–2,200 |
| **90-day cumulative** | **170–250** | **$4,250–6,250** | **$3,400–5,000** |

Headphone hooks add $788–$933/month (20 units/week at $12.99–$14.99) starting Week 4. Combined 90-day gross with hooks live: **$6,700–$9,900**.

#### Unit Economics Reminder (Pass Scenario)

Per the established cost model:

| Product | COGS/Unit (all-in incl. Etsy fees) | Net/Unit | Net Margin |
|---|---|---|---|
| ModRun clip (single, $12.99) | ~$4.85 | ~$8.14 | 62.7% |
| ModRun blended bundle AOV ($24.99) | ~$7.50 | ~$17.49 | 69.9% |
| Headphone hook ($12.99) | $3.13 | $9.86 | 75.9% |
| Headphone hook ($14.99, post-50 reviews) | $3.32 | $11.67 | 77.9% |

**The most important unit economics lever is not supplier negotiation or filament tier — it is AOV.** Moving even 30% of orders from single clips to 3-clip bundles improves blended margin from ~62% to ~69%. Review `scaling-cost-levers.md` for the full analysis. Prioritize bundle listing creation in Week 1.

---

### 1.3 Scenario B: Test Print FAILS

Failure is defined as: snap arm cracks under test load, or 2+ dimensional gates fail simultaneously, or surface finish on the snap face is too degraded to function.

#### Diagnosis First — Most Failures Are Category-Specific

| Failure Mode | Root Cause | Resolution | Time to Re-Test |
|---|---|---|---|
| Snap arm cracks at root | Layer line orientation wrong (horizontal instead of vertical Z-axis), or nozzle temp too low | Change print orientation to vertical Z (snap arm layers stack parallel to arm length); increase nozzle to 225C; reprint | 1–2 days |
| Snap arm doesn't click (too stiff) | Tolerance too tight | Increase `FDM_TOLERANCE` from 0.15mm → 0.20mm; regenerate STL; reprint | 1 day |
| Snap arm clicks but cable falls out | Tolerance too loose | Decrease `FDM_TOLERANCE` from 0.15mm → 0.10mm; regenerate STL; reprint | 1 day |
| No click, arm must be forced | Wall count issue | Verify wall count is exactly 4 (not 3); reprint | 1 day |
| Bore diameter off >0.5mm | Slicer horizontal expansion setting | Set horizontal expansion to −0.05mm in Bambu Studio; reprint | 1 day |
| Full geometry iteration needed | Design error, not tolerance/settings | Redesign in CadQuery; test individual snap arm component first; full reprint | 2–3 weeks |

The most likely failure modes are the first three — all resolvable in 1 day without design work. Do not assume "full geometry iteration" until you have ruled out settings and tolerance issues.

#### Design Iteration Roadmap (If Full Iteration Required)

1. **Week 1:** Identify the exact failure mode through systematic elimination (orientation, temp, tolerance in sequence). Run each test as a single-component print — print only the snap arm subcomponent to save filament and time.
2. **Week 2:** If settings alone cannot fix it, iterate the CadQuery geometry: increase snap arm cross-section at root by 10–15%, reduce arm length by 2mm to decrease leverage stress, regenerate STL.
3. **Week 3:** Full-geometry reprint and re-test all 4 gates. If 3/4 gates pass, proceed to near-pass protocol. If all 4 fail again, consult `scaling-production-research.md` Section 4 (snap arm orientation risk analysis).

[ASSUMPTION: Design iteration scope is unknown until failure mode is diagnosed. The 2–3 week estimate assumes a non-trivial geometry change, not just tolerance tweaking.]

#### Revenue Impact of Fail Scenario

| Metric | Pass | Fail (1-day fix) | Fail (2–3 week iteration) |
|---|---|---|---|
| First Etsy listing live | Day 7–10 | Day 8–11 | Day 28–35 |
| First ModRun revenue | Week 2 | Week 2–3 | Week 5–6 |
| 90-day ModRun gross | $4,250–6,250 | $3,900–5,800 | $2,800–4,200 |
| Headphone hook impact | None — launches Week 4 regardless | None — unaffected | None — unaffected |

**Critical point:** Headphone hooks are independent of ModRun snap arm outcome. Even in the worst-case 3-week delay, headphone hook revenue starts Week 4–5 and partially compensates. The fail scenario does not collapse the business; it delays the revenue start by 2–5 weeks.

---

## Part 2: Batch 1 + Batch 2 Parallel Execution Strategy

### 2.1 Production Capacity — Single Bambu P1S

[ASSUMPTION: Bambu P1S, 256×256mm build plate, 0.20mm layer height, 200mm/s outer wall speed.]

**ModRun clips:**
- 12-clip plate print time: ~45–60 min on P1S at production settings
- Daily capacity (16-hour operating window): 16–21 plates → 192–252 clips
- Practical weekly production at 20 units/week order rate: 2–3 plate runs (24–36 clips produced, ~20 shipped)
- Weekly printer utilization: ~2.5–3.5 hours printing (not a constraint)

**Headphone hooks:**
- 4-hook plate print time: ~95–110 min on P1S (25g per hook, 4 hooks per 256mm plate)
- Daily capacity (16-hour window): 8–10 plates → 32–40 hooks
- Weekly target (20 hooks/week): ~5 plate runs → 5.5–7 hours total print time
- Weekly printer utilization for hooks: ~6 hours

**Combined utilization at 20 ModRun + 20 hooks/week:**
- ModRun: ~3 hours/week
- Hooks: ~6 hours/week
- **Total: ~9 hours/week on a 112-hour available window (16 hr/day × 7 days)**
- Single-printer utilization: ~8%. The printer is massively underutilized at 20-unit targets for either product.

**Conclusion:** There is no production constraint from running both products simultaneously. Queue clips overnight (90-min plate, harvest in morning) and hooks in parallel daytime slots. The constraint through Month 3 is Etsy demand, not printer time.

### 2.2 Parallel Launch Decision: Simultaneous vs. Staggered

**Recommendation: Staggered by 3–4 weeks, with hook design work starting immediately.**

Rationale:
- Simultaneous launch splits your photography, listing-copy, and first-week optimization attention across two products. Reviews from ModRun build cross-sell credibility for hooks. The ecosystem framing ("complete your desk setup") is stronger if ModRun has 5–10 reviews before the hook listing appears.
- A 3-week stagger is not a delay — hook production can begin in Week 1 to build launch inventory while you optimize the ModRun listing.
- The hooks' Etsy launch window should target Thursday of Week 3–4 to catch the same peak traffic window used for ModRun.

**Operational checklist for parallel running:**

| Week | ModRun Activity | Hook Activity |
|---|---|---|
| 1 | First production plate → photography → listing live | Test print 3 hook variants; order silicone bumper pads |
| 2 | Process first orders; optimize listing based on CTR | Print 25mm production batch (4 units); fit-test; finalize tolerance |
| 3 | Build 20-unit inventory; watch reviews | Print 30-unit launch inventory; photograph; draft Etsy listing |
| 4 | Price test data from first week in | Publish hook listing Thursday; enable Etsy Ads at $1/day |
| 5+ | Both products running in parallel steady-state | — |

### 2.3 Cash Flow Simulation: Does Batch 1 Fund Batch 2?

Headphone hook startup cost: **$5** (silicone bumper pads). This is the entire incremental capital outlay.

Headphone hooks use PLA+ filament already in stock for ModRun production. No new material purchasing is required. No new packaging required (existing poly mailers, thank-you cards). No new tools.

**Batch 1 revenue is not needed to fund Batch 2 production.** This is the correct answer and it changes the decision calculus: you should order the silicone bumper pads today (before the test print is even evaluated) and begin hook test printing immediately, regardless of ModRun outcome.

**Cash flow at 20 units/week for each product (steady-state):**

| Product | Weekly Material + Packaging COGS | Weekly Net Profit |
|---|---|---|
| ModRun clips (20 units, blended $24.99 AOV) | ~$8–12 | ~$383 |
| Headphone hooks (20 units, $12.99) | ~$11 | ~$197 |
| **Combined** | **~$20** | **~$580/week** |

At this combined rate, 90-day net profit from production costs and operations alone (excluding Etsy fees): **~$6,700–7,500** — consistent with the `revenue-ramp-metrics.md` Month 6 target.

### 2.4 Supply Chain Simultaneity

Both products draw from the same filament stock. No conflict.

- **ModRun clips:** PLA+, primary colors black/white/grey. eSUN 10kg bundles.
- **Headphone hooks:** Same PLA+ stock. Silicone bumper pads ($5 per 100-pack, one-time order).
- **Packaging:** Shared poly mailers and thank-you cards. No SKU-specific packaging until Month 3+.

Simultaneous supply ordering (Day 0 after test print): order 2× black PLA+ 1kg, 1× white, 1× grey, 100-pack silicone bumpers, 100× poly mailers, 50× kraft boxes. Total outlay: ~$85–95. This funds both products through first 4 weeks at projected sell-through rates.

---

## Part 3: Revenue Maximization Levers

### 3.1 Pricing Strategy and Price Elasticity

**Current pricing:** ModRun clips $12.99 single / $24.99 blended bundle AOV. Hooks $12.99 launch.

**Competitive context per Etsy research (May 2026):**
- ModRun dominant competitor (Robbosales): $10.99. PETG premium tier: $18.50–$22.50.
- Hooks dominant competitor (3DdesignBros): $14.99 with 1,254 reviews.
- ModRun is positioned as a premium original-design product, not competing on price with $10.99 generics.

**Price elasticity assumptions to test:**

| Product | Current Price | Test Price | When to Test | Expected Outcome |
|---|---|---|---|---|
| ModRun single clip | $12.99 | $14.99 | After 25 reviews | If conversion rate stays within 20% of current, keep. Revenue impact: +$2/unit. |
| ModRun 3-clip bundle | $28.99 | $32.99 | After 50 reviews | Bundle buyers are less price-sensitive. +$4/order at 30% of orders = +$28/week. |
| Headphone hook single | $12.99 | $14.99 | After 50 reviews | Matches dominant competitor. +$1.81/unit, +$36/week at 20 units/week. |
| Headphone hook 3-pack | $32.99 | $36.99 | Simultaneously with single test | Bundle anchor effect; few buyers will order 3-pack at launch anyway. |

**The AOV lever is more powerful than the price lever.** Moving 30% of single-clip orders to 3-clip bundles at $28.99 increases weekly revenue by ~$120 at 20 clips/week with no price increase. Priority: get the bundle listing live in Week 1.

**Shipping pricing:** Current model is buyer-pays. Free shipping listings rank slightly higher on Etsy search. Test the free-shipping format at Month 2 by rolling shipping cost into product price ($12.99 → $15.99 with free shipping). Monitor conversion rate delta over 4 weeks. If conversion rate holds, the 2.1 percentage point margin cost is worth the search rank improvement.

### 3.2 Etsy SEO and Marketing

Per `etsy-seo-strategy.md` (validated May 2026):

**ModRun title (140 char limit):** Use: `ModRun Cable Clip System | Parametric Desk Cable Management | 3D Printed | Custom Bore Size`

**High-signal tags for ModRun (all 13, priority order):**
`cable management desk`, `cable clip 3d print`, `desk organizer cord`, `standing desk accessory`, `cable management system`, `cord organizer desk`, `monitor setup accessory`, `3d printed home office`, `custom cable clip`, `desk cable holder`, `minimalist desk setup`, `cable organizer custom`, `gamer desk cable`

**The standing-desk-specific positioning is the primary whitespace opportunity.** Per `etsy-seo-strategy.md` finding: "standing-desk-specific cable management" returns under 200 listings on Etsy with very high buyer intent. Angle the listing description toward standing desk buyers — they buy more organizational products and have higher AOV history.

**Post-purchase marketing sequence (weeks 1–8):**
1. Every shipped order includes a cross-sell card: "Complete your desk setup — add a headphone hook." Include the Etsy listing URL.
2. Update ModRun listing description in Week 4 to add: "Pairs with our parametric headphone hook — link below." Add the hook listing URL as a "You may also like" entry.
3. At 10 reviews, quote the best review in the listing's opening paragraph.
4. r/battlestations post in Week 2 (not Week 1 — build a few reviews first). The post format: photo of real desk with ModRun installed, honest product story, Etsy link in comments when asked.

**Photo video upgrade at Month 2:** The `etsy-seo-strategy.md` finding is clear — in-situ use-case videos outperform lifestyle photos 2.5–3x in click-through. A 15-second loop video showing cable insertion into a clip and rail installation is the highest-ROI marketing investment of Month 2. Film with a smartphone, edit in CapCut (free), upload as the listing's first media slot.

### 3.3 Operational Efficiency

**Print speed:** The current settings (200mm/s outer wall, 300mm/s inner wall) are already optimized per `production-workflow-v1.md`. Do not increase outer wall speed above 200mm/s — dimensional accuracy at the snap arm degrades.

**Batch size discipline:** Always print 12-clip plates. Never print partial plates for individual orders. Pre-print to build 5–10 unit inventory per SKU. The 12-clip plate is the atomic unit of production.

**Scrap rate target:** 2–4% at steady state (post first 50 units). First 10–20 units will run 5–8% scrap as the profile matures. A 5% scrap rate adds ~$0.05/unit material cost — not significant, but track it. Gate 1 (visual), Gate 2 (dimensional), Gate 3 (functional) as specified in `production-workflow-v1.md` Section 3.

**Packaging cost reduction:** At 20 units/week across 2 products (~40 orders), stay with current poly mailer + thank-you card. The kraft box upgrade ($0.63/box vs. $0.08 poly mailer) is justified only for bundle orders (3+ clips) where the perceived value premium supports it. Single-clip orders: poly mailer. Bundle orders: kraft box.

**Labor time target:** 40 minutes active operator time per 12-clip harvest + 5-order batch packaging. The workflow in `production-workflow-v1.md` achieves this. Do not deviate from the sequence — it is optimized for parallel printer operation during post-processing.

### 3.4 Product Bundling and Cross-Sell

**ModRun + Headphone Hook ecosystem bundle:**

| Bundle | Contents | Price | Net Margin | Notes |
|---|---|---|---|---|
| "Desk Starter Kit" | 3 clips + 1 rail + 1 hook | $39.99 | ~71% | Highest AOV single-order option; positions as complete desk solution |
| "Cable Pro Bundle" | 6 clips + 1 rail + 2 hooks | $64.99 | ~73% | Targets gaming desk setups with multiple cable runs |
| Standalone hook 3-pack | 3 hooks (custom thickness/color) | $32.99 | ~77% | Same margin as single but drives review velocity on hook listing |

Create the "Desk Starter Kit" listing in Week 3 (after both ModRun and hooks are live). The cross-sell insert in every order should reference this bundle explicitly by name and price.

**Bundle listing title:** `ModRun Desk Starter Kit | 3D Printed Cable Clips + Headphone Hook | Complete Desk Setup`

The ecosystem positioning — the fact that you sell both cable management and headphone management in an original parametric design system — is a defensible moat no competitor can copy quickly. Every listing should reference the other.

### 3.5 Upsell Sequence After First Purchase

**Customer journey post-first-purchase:**

1. **Day of purchase:** Order confirmation email (Etsy auto-sends). No action needed.
2. **Day of ship:** Include thank-you card with cross-sell hook listing URL and 30-day satisfaction guarantee language.
3. **Day +14 (if no review):** Etsy's auto-review request fires. Do not supplement with additional pressure.
4. **Month 2 (if customer favorites other listings):** Etsy sends a price-drop notification automatically when you run a sale — this is the upsell trigger for existing favoriting customers. Run a 10% sale for 48 hours to fire these notifications.
5. **Month 3:** If customer has ordered hooks, cross-sell Batch 3 (magnetic bin labels). Cross-sell insert reads: "Organizing cables and headphones. Next: magnetic workshop labels. [URL]"

The upsell sequence is passive — Etsy's notification system handles the retargeting automatically once a customer has favorited a listing. Your job is to ensure every listing links to at least one other listing in the shop.

---

## Part 4: Production Capacity Analysis — 20-Unit-Per-Week Plan

### 4.1 ModRun Clip Capacity

| Scenario | Print Time/Plate | Plates/Week | Clips/Week | Weekly Hours |
|---|---|---|---|---|
| Conservative (1 plate/day, 5 days) | 55 min | 5 | 60 | 4.5 hr |
| Target (20 units/week) | 55 min | 2 | 24 | 1.8 hr |
| Near-capacity (daily plates, 7 days) | 55 min | 7 | 84 | 6.5 hr |

**At 20 clips/week, the printer runs under 2 hours for ModRun production.** This is deliberately conservative — demand growth, not capacity, governs ramp speed. At 22–28 min/unit for single-clip estimates, batch printing (12 per plate) compresses effective per-unit time to ~5 min.

### 4.2 Headphone Hook Capacity

| Scenario | Print Time/Plate | Plates/Week | Hooks/Week | Weekly Hours |
|---|---|---|---|---|
| Target (20 hooks/week) | 100 min | 5 | 20 | 8.3 hr |
| Aggressive (3 plates/day, 5 days) | 100 min | 15 | 60 | 25 hr |
| Maximum single-printer (12 hr/day, 7 days) | 100 min | ~50 | ~200 | 83 hr |

**The 20-hook/week target uses 8.3 hours of printer time.** Combined with ModRun's 1.8 hours, total weekly printer utilization for both targets is **~10 hours on a 112-hour available window** — under 9% utilization.

### 4.3 Production Priority Decision

**Question from task brief: Focus production on Batch 2 only until Batch 1 reaches profitability, then ramp both?**

**Answer: No. Run both from Day 1.** Here is why:

The printer utilization numbers make this obvious — there is no competition for machine time. Running 20 clips/week takes 1.8 hours. Running 20 hooks/week takes 8.3 hours. Running both takes 10 hours. The printer has 102 hours of idle capacity per week at this volume.

The real constraint is Etsy ranking velocity. Each listing needs reviews to climb in search. Running both listings simultaneously from Week 4 (when hooks launch) gives both products a faster review ramp than a sequential approach. The cross-sell traffic between listings also accelerates each product's ranking independently.

**Production queue management:**
- Morning slot: ModRun plate (overnight print, harvest AM)
- Afternoon slot: Headphone hook plates (3–4 per afternoon session)
- No scheduling conflict at 20 units/week for each product

### 4.4 Scaling Past 20 Units/Week

The second printer trigger activates when:
1. Single printer running >28 hours/week for 2 consecutive weeks, AND
2. Etsy order processing time is slipping beyond stated 3–5 day window

At 20 units/week for each product, weekly printer hours = ~10. The trigger activates around 55–60 combined units/week (estimated Month 4–5 based on `revenue-ramp-metrics.md` scaling targets). Second printer cost: $699. Payback at incremental 40 units/week at $24.99 AOV: ~3 weeks.

---

## Part 5: Batch 3 Product Selection Readiness

### 5.1 Current State: Batch 3 Is Already Researched

Per `batch-3-candidate-research.md` (completed May 2026):

**Rank 1 — Magnetic Workshop Bin Labels (Batch 3, Month 2)**
- 50mm × 40mm PLA+ tiles with N52 disc magnet press-fit pocket
- Parametric CadQuery design complete: `cadquery/sku_batch_2_magnetic_labels.py`
- Validated demand: 300–500+ active Etsy listings, dominant competitor (ColKy Designs) at $30.99/10-pack with 69 reviews
- Margin: 72–76% net at $22–27 per 10-pack
- Print time: 8–12 min/tile, 30+ tiles per plate → extremely high throughput
- New BOM: N52 8mm × 2mm disc magnets (Amazon domestic, 200× for ~$38, 1–2 day delivery)
- Design status: Complete. Only remaining step is magnet press-fit tolerance calibration (one test plate)

**Rank 2 — Monitor Riser Legs (Batch 3, Month 2–3)**
- Parametric leg sets (8cm / 12cm / 16cm height), 3 variants, sold as 4-leg sets
- Price range: $28–$38 per set depending on height
- Margin: 67–69% net (slightly lower due to larger print volume per unit)
- Cross-sell: Direct ModRun desk buyer cross-sell — anyone organizing cables also needs a riser
- Design: `cadquery/sku_batch_2_plant_markers.py` analogue (needs 3–4 hours of design work)

**Batch 4 candidates:** Pegboard hooks (same peg tolerance validation risk as ModRun snap arm — sequence after Batch 3 reviews), plant markers in ASA (requires ASA print profile calibration).

### 5.2 Can Batch 3 Research Start Now?

**Yes, and it already has.** The research, margin validation, and design are complete for the two leading candidates. The only remaining gates before launch:

| Product | Gate Remaining | Time to Clear | Action |
|---|---|---|---|
| Magnetic bin labels | N52 magnet press-fit calibration | 1 day (one test plate) | Order magnets this week |
| Monitor riser legs | CadQuery design (not yet built) | 3–4 hours | Execute in Month 1 Week 2 |

**Batch 3 launch target: Month 2 (Weeks 5–8).** This is not ambitious — the bin label design is done and the magnet is the only physical calibration gate. Order the magnets at the same time as the bumper pads. The combined order is $43 total for the startup materials of both Batch 2 and Batch 3.

### 5.3 Parallel Product Testing Strategy

You can design 2–3 Batch 3 candidates simultaneously while Batch 1/2 run. The design work is non-blocking (CadQuery sessions, 2–4 hours each) and the test prints are single-component prints that use < 50g filament each. Timeline:

- **Month 1 Week 2:** Design monitor riser legs in CadQuery (3–4 hours)
- **Month 1 Week 3:** Test print riser legs + bin label magnet calibration (parallel, same day)
- **Month 2 Week 5:** Both Batch 3 listings live
- **Month 3 Week 9:** Begin Batch 4 (pegboard hooks) test print + ASA profile calibration

Running all four product lines by Month 3 is achievable without stressing single-printer capacity.

---

## Part 6: 12-Month Product Roadmap and Farm Scaling

### 6.1 Product Portfolio Roadmap

| Month | Active Products | New Launch | Weekly Units (all products) | Gross Revenue/Month |
|---|---|---|---|---|
| 1 | ModRun | Headphone hooks (Week 4) | 25–40 | $750–1,500 |
| 2 | ModRun + Hooks | Magnetic bin labels (Week 6) | 40–65 | $2,000–3,500 |
| 3 | ModRun + Hooks + Bin Labels | Monitor riser legs (Week 10) | 60–90 | $3,500–5,500 |
| 4 | 4 products running | Pegboard hooks (Batch 4) | 80–110 | $5,000–7,500 |
| 5 | 5 products running | Plant markers (ASA, Batch 4-B) | 90–120 | $6,000–8,500 |
| 6 | Full 5-product portfolio | 2nd printer evaluation | 100–140 | $6,900–9,500 |
| 7–8 | Full portfolio + 2nd printer | Multi-color SKUs (AMS 2 Pro) | 140–200 | $8,000–12,000 |
| 9–10 | Multi-printer farm | Laser engraving evaluation | 180–250 | $10,000–16,000 |
| 11–12 | Multi-printer farm | 3rd printer if 80% utilization | 250–350+ | $14,000–22,000 |

[ASSUMPTION: Revenue per unit stays at current pricing through Month 6. Price tests may lift revenue 10–15% from Month 3 onward if conversion holds.]

### 6.2 Year 1 Revenue Projection

**Conservative case (demand builds slowly, 1-printer all year):**
- Months 1–3 ramp: $6,250–10,500 cumulative gross
- Months 4–6 at $5,000–7,500/month: ~$15,000–22,500
- Months 7–12 with 2nd printer at $8,000–12,000/month: ~$48,000–72,000
- **Year 1 total (conservative): ~$69,250–105,000 gross**

**At 75% net margin (blended across all products): ~$52,000–78,750 net Year 1**

[ASSUMPTION: These projections assume Etsy demand ramps as modeled in `revenue-ramp-metrics.md`. The primary uncertainty is search rank velocity, not production capacity.]

### 6.3 Printer Farm Scaling Gates

Per `printer-farm-automation-framework.md` and `revenue-ramp-metrics.md`:

| Gate | Condition | Action | Cost |
|---|---|---|---|
| 2nd printer | P1S >28 hr/week for 2 weeks + order backlog | Order P1S immediately | $699 |
| Color-per-printer strategy | 2nd printer acquired | P1=black, P2=white → eliminates filament swaps | $0 |
| AMS 2 Pro multi-color | 25+ color-coded orders/month for 2 months | Purchase AMS 2 Pro | $286 |
| Printago (free) | 2nd printer online | Connect both to Printago for queue management | $0 |
| SimplyPrint Pro | 2nd printer online | Failure detection ($9.99/month) | $10/month |
| 3rd printer | Combined >80% utilization for 2 weeks | Add 3rd P1S | $699 |

**Farm payback math:** At 40 incremental units/week from a 2nd printer at $24.99 blended AOV, additional weekly gross = $1,000. Second printer ($699) pays back in 4.9 weeks. This is a favorable ROI — but only exercise it when demand triggers it, not ahead of demand.

---

## Part 7: Risk Mitigations and Decision Gates

### 7.1 Risk Register

| Risk | Probability | Revenue Impact | Mitigation | Decision Gate |
|---|---|---|---|---|
| Batch 1 test print fails (geometry) | Low–Medium | −$2,000–3,000 gross (30-day delay) | Systematic diagnosis per Section 1.3; snap arm subcomponent-only reprints to minimize filament waste | Start Batch 2 (hooks) immediately regardless of outcome |
| Market saturation on hooks (before 20/week) | Low (May 2026 — category not saturated) | Hooks plateau at 10–15/week instead of 20 | Accelerate Batch 3 (bin labels) as primary revenue; hooks become supporting SKU | If hook weekly views plateau below 100 for 3 weeks post-launch, accelerate bin labels |
| USPS shipping cost inflation above $8/unit | Medium (USPS has 8% Jan 2027 surcharge baked in) | −5–8 margin points if cost hits $8 | Per `scaling-cost-levers.md`: pass through in price increase ($1–2 per order); test free-shipping format to recapture Etsy rank; consider USPS Ground Advantage for orders over 1 lb | Monitor monthly; price-test the $1 pass-through at Month 3 |
| Printer hardware failure (thermal, nozzle clog, bed) | Low per month, Medium per year | $833–2,400 lost revenue per 10-day outage | JLC3DP overflow contract mfg relationship (validate Month 3); maintain spare: 0.4mm nozzle, 2 flex PEI plates, extra PTFE tube, 500g each color as safety stock | Set up JLC3DP account before Month 3; ship 5-unit sample at $50–80 to validate overflow path |
| Etsy algorithm deprioritizes listing | Low (original designs protected post-June 2025 policy) | High — primary discovery channel | Git commit history documents CadQuery design provenance; maintain original-design documentation | If listing views drop >50% in 1 week with no external cause, check Etsy seller dashboard for policy flags; appeal immediately with design documentation |
| Supply chain delay (filament stock-out) | Low | $200–400 per week of outage | eSUN + Anycubic as dual sources; minimum 500g safety stock per active color (covers 1 week at 20 units) | Order backup filament when primary spool drops below 250g |
| Etsy bans account (terms violation) | Very low | Catastrophic | Always self-manufacture (Etsy handmade policy); never dropship clips; all materials accurately described | No deviation from handmade policy; clips always self-printed |

### 7.2 Decision Gates Summary

**Gates that require action within 24 hours of trigger:**

1. Test print result known → immediately execute Pass or Fail protocol (Section 1.2 or 1.3)
2. Printer running >28 hr/week for 2 consecutive weeks → order 2nd P1S within 7 days
3. Etsy listing views drop >50% in 1 week → investigate listing flags that day
4. Primary filament source (eSUN Amazon) shows stock-out → order Anycubic backup same day

**Gates that require review monthly:**

1. Gross margin below 68% → run margin investigation protocol (revenue-ramp-metrics.md)
2. Shipping cost at Pirate Ship exceeds $5.50/label average → test price pass-through
3. Hook listing weekly views plateau below 100 for 3 weeks → accelerate Batch 3 launch

### 7.3 The One Decision That Cannot Be Undone

The only irreversible mistake in the post-test-print phase is publishing Etsy listings before photographs are ready. The listing's first 7 days determine its initial Etsy search rank. A placeholder hero photo (or a render instead of a real print photo) during launch week permanently suppresses the listing's starting position. Everything else — price, description, tags — can be A/B tested and refined. The photos need to be right at launch.

**Rule:** No listing goes live without at least 5 real-product photos. No exceptions.

---

## Implementation Priority Order (First 7 Days Post-Test-Print)

Regardless of pass or fail:

| Day | Action | Time Required | Dependency |
|---|---|---|---|
| Day 0 | Order silicone bumper pads (100-pack) + N52 magnets (200×) | 10 min | None — do this now |
| Day 0 | Order Day 0 materials (filament, mailers, boxes) if test print passes | 15 min | Test print PASS only |
| Day 0–1 | Lock STL and slicer profile (if pass); or begin diagnosis (if fail) | 1–2 hr | Test print result |
| Day 1 | Start first 12-clip production plate (if pass) | 5 min setup | STL locked |
| Day 1 | Start hook test prints (25mm variant first) | 25 min | Always |
| Day 3–5 | Photography session — ModRun | 90 min | 12 clips produced |
| Day 5–7 | Photography session — Headphone hook | 60 min | 4 hooks produced |
| Day 7–10 | Publish ModRun Etsy listing (if pass) | 45 min | Photos complete |
| Week 3–4 | Publish headphone hook listing | 45 min | Photos + 30-unit inventory |

---

*Document status: EXECUTION-READY for both PASS and FAIL scenarios. Update this document's status field within 24 hours of test print completion. Pin the outcome (pass/fail, which gates, what tolerance value confirmed) as a comment at the top of this file.*

*Sources grounding this framework: production-workflow-v1.md (print times, plate capacity, slicer settings), headphone-hooks-cost-model.md (hook COGS $3.13, 76% margin, 25g weight), revenue-ramp-metrics.md (weekly projection table, scaling triggers), scaling-cost-levers.md (AOV maximization finding, Etsy fee structure), batch-3-candidate-research.md (magnetic bin labels as Batch 3 frontrunner, magnet specs), batch-3-4-launch-sequencing.md (Month 1–3 calendar), etsy-seo-strategy.md (Thursday publish window, standing-desk whitespace, video CTR finding), supply-chain-diversification-strategy.md (JLC3DP overflow path, filament safety stock), printer-farm-automation-framework.md (color-per-printer strategy, SimplyPrint, Printago), bundle-strategy.md (Desk Starter Kit at $39.99, ecosystem framing).*
