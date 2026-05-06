---
title: ModRun Cost Optimization Lever Analysis — 100 to 500 Units/Month
date: 2026-05-06
status: pre-negotiation-ready
tags: [mfg-farm, modrun, cost-model, scaling, 3pl, filament, printer-roi, unit-economics]
confidence: high
related: cost-model-spreadsheet.csv, scaling-cost-model.csv, supplier-economics.md, phase-2-supplier-research.md, production-scaling-research.md, production-workflow-v1.md
scope: analysis only — no supplier contact until post-test-print
---

# ModRun Cost Optimization Lever Analysis: 100–500 Units/Month

**Lead finding:** The dominant cost lever at every scale tier examined is not filament, not printer capex, and not labor — it is shipping, which runs $4.50–$5.50 per order and consumes 59% of a single-clip order's COGS. Supplier negotiation and filament bulk purchasing deliver real but secondary savings (3–5 margin points at best). The most powerful financial move at any volume is average order value (AOV) maximization: moving a customer from a single clip at $8.99 to a 3-clip bundle at $28.99 improves gross margin from ~38% to ~69% with zero change to filament cost, printer fleet, or logistics infrastructure. All other decisions in this document should be read against that baseline.

**Current state:** Cost model baseline is $0.08–$0.13 COGS per clip (manufacturing only) at 20 units/week, 72–73% gross margin when blended orders include rails. The analysis below extends this to 100, 200, 300, and 500 units/month, identifies the precise volume thresholds where each optimization unlocks, and builds a Go/No-Go decision tree for each capital deployment.

---

## Section 1: Unit Economics at 100 / 200 / 300 / 500 Units per Month

All figures use the blended revenue model: 70% 3-clip bundle orders at $24.99, 30% rail orders at $34.99, yielding a $27.50 blended AOV. PLA+ at $12/kg (10kg bulk), USPS Ground Advantage via Pirate Ship at $4.50 blended average, Etsy fees 9.5% of revenue (6.5% transaction + 3.0% payment processing). Labor is imputed at $15/hour opportunity cost.

### 100 Units/Month (25 Units/Week — Single Printer, Solo)

This tier sits just above the single-printer inflection point. One Bambu P1S running 12–14 hours/week delivers this output comfortably without approaching capacity limits.

| Component | $/Unit | % of Total Cost |
|---|---|---|
| Filament (PLA+ at $12/kg, 70g blended weight) | $0.84 | 10.1% |
| Printer depreciation ($699, 5,000-hr life, ~8 hr/week) | $0.10 | 1.2% |
| Electricity ($0.12/kWh, 200W avg) | $0.01 | 0.1% |
| Scrap allowance (5% mature rate) | $0.04 | 0.5% |
| Packaging (poly mailer + zipper bag) | $0.22 | 2.6% |
| Etsy fees (9.5% of $27.50) | $2.61 | 31.4% |
| Shipping (USPS Ground Advantage blended) | $4.50 | 54.1% |
| **Total cost per order** | **$8.32** | **100%** |
| Revenue per order | $27.50 | |
| **Gross profit per order** | **$19.18** | |
| **Gross margin** | **69.7%** | |
| **Monthly gross profit** | **$1,918** | |

Labor burden at this volume: 2–2.5 active hours/day covering print monitoring, harvest, QC, packaging, and shipping. Fully manageable solo. No contractor needed.

Key observation: Etsy fees (31.4%) and shipping (54.1%) together consume 85.5% of all costs. Filament is 10.1%. The implication is that supplier negotiations — the most commonly discussed optimization lever — affect less than 11 cents of every dollar of cost at this volume.

### 200 Units/Month (50 Units/Week — Single Printer Near Ceiling)

At 50 units/week, one printer is running 35+ hours/week. This is near-full utilization for a 16-hour operating day. Printer depreciation per unit collapses as utilization rises; filament consumption now justifies a first bulk tier upgrade if not already in place.

| Component | $/Unit | % of Total Cost | Change vs. 100/mo |
|---|---|---|---|
| Filament (PLA+ at $11.50/kg, 10kg bundle) | $0.81 | 9.8% | −$0.03 |
| Printer depreciation (high utilization) | $0.04 | 0.5% | −$0.06 |
| Electricity | $0.01 | 0.1% | — |
| Scrap allowance (4% as profile matures) | $0.03 | 0.4% | −$0.01 |
| Packaging (poly mailer, case quantity) | $0.20 | 2.4% | −$0.02 |
| Etsy fees | $2.61 | 31.6% | — |
| Shipping | $4.50 | 54.5% | — |
| **Total cost per order** | **$8.20** | **100%** | **−$0.12** |
| **Gross margin** | **70.2%** | | **+0.5 pts** |
| **Monthly gross profit** | **$3,860** | | |

The $0.12 improvement from 100 to 200 units is entirely from depreciation collapse at high printer utilization. Filament saves $0.03/unit. The throughput doubled but the margin improvement is trivial (0.5 points). This is structurally important: doubling output from 100 to 200 units/month doubles gross profit dollars ($1,918 → $3,860) while barely moving percentage margin. The leverage is volume, not cost reduction.

Labor note: 50 units/week pushes active daily labor to 3.5–4 hours. The operator is still solo-viable but begins approaching the threshold where batching discipline and print queue optimization become non-optional.

### 300 Units/Month (75 Units/Week — Two Printers Required)

At 75 units/week, one printer cannot reliably deliver output without running 24 hours/day. A second Bambu P1S ($699) should be acquired when demand consistently exceeds 50 units/week for two consecutive weeks. The second printer adds depreciation cost per unit but unlocks throughput redundancy — if one printer fails, production continues.

| Component | $/Unit | % of Total Cost | Change vs. 200/mo |
|---|---|---|---|
| Filament (PLA+ at $11.00/kg, approaching 25kg/mo consumption) | $0.77 | 9.3% | −$0.04 |
| Printer depreciation (2 printers, blended utilization) | $0.07 | 0.8% | +$0.03 |
| Electricity (2 printers) | $0.02 | 0.2% | +$0.01 |
| Scrap allowance (4%) | $0.03 | 0.4% | — |
| Packaging | $0.19 | 2.3% | −$0.01 |
| Etsy fees | $2.61 | 31.5% | — |
| Shipping | $4.50 | 54.4% | — |
| **Total cost per order** | **$8.19** | **100%** | **−$0.01** |
| **Gross margin** | **70.2%** | | flat |
| **Monthly gross profit** | **$5,793** | | |

Key tension: the second printer adds $0.03/unit in depreciation, which nearly offsets the filament savings from higher volume. Net COGS improvement from 200 to 300 units is only $0.01/unit. But the business case for the second printer is not margin improvement — it is throughput multiplication and production continuity insurance.

Labor: 75 units/week pushes daily active labor above 4 hours at solo operation. This is the first point where a part-time post-processing contractor (10 hours/week at $15/hour = $600/month) meaningfully improves operator quality of life. The contractor cost of $0.16/unit (at 300 units/month) reduces gross margin by 0.6 points but frees the operator for higher-value tasks (Etsy optimization, product expansion, customer communication).

### 500 Units/Month (125 Units/Week — Two-Printer Fleet, Contractor Required)

At 500 units/month, the operation is generating ~$13,750/month in gross revenue and ~$9,000/month in gross profit before labor. Two printers each running approximately 22 hours/week handles this output. Monthly filament consumption reaches 35–40 kg, which triggers the transition from 10kg Amazon bundles to a direct pallet order.

| Component | $/Unit | % of Total Cost | Change vs. 300/mo |
|---|---|---|---|
| Filament (PLA+ at $10.49/kg, Anycubic 50kg pallet) | $0.73 | 8.7% | −$0.04 |
| Printer depreciation (2 printers, near full utilization) | $0.06 | 0.7% | −$0.01 |
| Electricity | $0.02 | 0.2% | — |
| Scrap allowance (3.5% with mature dual-printer profile) | $0.03 | 0.4% | — |
| Packaging (case quantity, branded mailers beginning) | $0.18 | 2.1% | −$0.01 |
| Contractor labor (post-processing, 15 hrs/week) | $0.17 | 2.0% | new |
| Etsy fees | $2.61 | 31.1% | — |
| Shipping | $4.50 | 53.6% | — |
| **Total cost per order** | **$8.30** | **100%** | +$0.11 |
| **Gross margin** | **69.8%** | | −0.4 pts |
| **Monthly gross profit** | **$9,700** (before contractor cash cost) | | |

Apparent paradox: COGS per unit is slightly higher at 500 units/month than at 300. The contractor labor addition ($0.17/unit) outweighs all material savings. This is the correct trade-off — the operator's freed time is more valuable than the $0.17/unit margin compression, and without the contractor, the operator cannot sustain 125 units/week while also managing listings, customer service, and product development.

**Volume tier summary:**

| Volume | Gross Margin | Monthly Gross Profit | Key New Cost | Key Savings |
|---|---|---|---|---|
| 100 units/mo | 69.7% | $1,918 | — | Depreciation per unit improving |
| 200 units/mo | 70.2% | $3,860 | — | Depreciation collapse at high utilization |
| 300 units/mo | 70.2% | $5,793 | 2nd printer depreciation | Filament volume savings |
| 500 units/mo | 69.8% | $9,700 | Contractor labor | Pallet filament pricing |

The key insight from this table: gross margin is remarkably stable across the 100–500 unit range, staying within a 0.5-point band (69.7–70.2%). This stability is not accidental — it reflects a cost structure where the dominant costs (Etsy fees and shipping) are fixed percentages of revenue that do not improve with volume. The implication: margin optimization through cost reduction has limited upside in this business. Volume is the lever, and AOV discipline is the margin protector.

---

## Section 2: Filament Bulk Purchasing Tiers

### The Pricing Landscape (PLA+, US Market, May 2026)

All primary suppliers are Chinese-origin but US-warehoused in part. Current pricing already embeds the 2025–2026 tariff environment. Further escalation would raise all tiers proportionally.

| Tier | Volume | Best Available Price | Supplier | Format | Notes |
|---|---|---|---|---|---|
| Retail spool | 1 kg | $15–18/kg | eSUN (Amazon) | 1-kg spool | No bulk savings; launch default |
| Small bundle | 5 kg | $13–15/kg | eSUN or Overture (Amazon) | 5-spool pack | Available Prime; minor savings |
| Case bundle | 10 kg | $11–13/kg | eSUN 10kg Amazon bundle | Case | Primary Phase 1 target |
| Mid-bulk | 25 kg | $9–12/kg | eSUN eBay wholesale | Multiple cases | Requires monitoring; availability variable |
| Pallet deal | 50 kg | $10.49/kg | Anycubic direct store | Pallet | Listed price, no account needed |
| Wholesale direct | 50–100 kg | $8.50–10/kg | eSUN direct (esun3dstore.com) | Quote | Requires direct inquiry and commitment |
| Polymaker wholesale | 10 kg+ (case) | $14.99/kg | Polymaker (us-wholesale.polymaker.com) | Case | $1,000 minimum order; quality-tier only |

### Tier Transition Timing

**Retail → 10kg Amazon bundle:** The right move is the first time you order more than 3 kg of a single color in one purchase, which typically happens by Week 3 of production. The savings are $3–5/kg with zero friction (still Amazon Prime). The only reason to stay on retail spools past Month 1 is that you have not yet confirmed color velocity — once you know black is your dominant color, buy 10 kg at once.

**10kg bundle → 50kg Anycubic pallet:** The Anycubic 50 kg pallet at $10.49/kg is the first genuine bulk tier. The trigger is monthly filament consumption exceeding 25 kg/month, which corresponds to approximately 300–350 units/month of the blended clip/rail mix. At $12/kg (current 10kg rate) versus $10.49/kg (Anycubic 50 kg), the savings per order are $75.50 on a 50 kg pallet. At 30 kg/month consumption, the annualized saving is approximately $542/year — meaningful but not transformative.

Critical constraint: 50 kg of PLA+ occupies approximately 6–8 cubic feet of dry storage. At typical home-based operations, this requires a designated sealed cabinet or rack with active desiccant humidity control. Storage below 30% relative humidity is necessary to prevent moisture absorption that causes AMS feed errors. The logistics overhead (storage setup, ~$80–150 one-time investment in dry storage containers and desiccant) must be counted against the pallet savings.

**Pre-qualification requirement:** Place one 5–10 kg test order from Anycubic before committing to the 50 kg pallet. Community AMS compatibility reports are mixed for Anycubic; some batches have winding issues that cause feed interruptions on long jobs. Validate your specific printer and profile against Anycubic filament before it becomes your primary supplier.

**50kg pallet → eSUN direct wholesale:** At 100 kg/month consumption (corresponding to approximately 1,000+ units/month, well beyond the scope of this analysis), direct wholesale at $8.50–9.50/kg becomes available through eSUN's direct channel. This tier is not relevant for the 100–500 unit range.

**Polymaker exception:** For white and light grey filament specifically, where color consistency and batch-to-batch uniformity are visible to customers in product photography, Polymaker wholesale at $14.99/kg (versus eSUN $12/kg) is worth the $3/kg premium. The extra $0.21/unit cost on a 70g clip order is absorbed within the rounding error of the blended COGS model. Polymaker's vacuum-sealed packaging also reduces moisture-related quality variation, which matters more as the filament inventory grows from one spool to 10+ kg stored. Activate Polymaker wholesale at Month 3–4 with a $1,000 opening order (approximately 67 kg), triggered by confirmed production at 50+ units/week.

### Shelf Space vs. Savings: The Practical Trade-Off

The case for buying in pallet quantities is straightforward in a spreadsheet but requires physical discipline in a home or small-commercial operation. Practical guidance by tier:

- **10 kg (one case):** Two sealed bins on a shelf. Zero overhead. Correct for Month 1–3.
- **25 kg:** Three to four bins; fits on one dedicated shelf section. Storage cost negligible. Correct for Month 3–6 once color velocity is confirmed.
- **50 kg:** Requires a dedicated rack section or a single shelving unit (approximately 24" wide × 18" deep × 48" tall holds 50 kg comfortably). One-time rack cost: $40–80. Requires active humidity monitoring. Correct at 300+ units/month.
- **100 kg+:** Dedicated storage room or climate-controlled closet. Not warranted below 1,000 units/month.

---

## Section 3: Consolidation Leverage — When 3PL Becomes Viable

### The 3PL Break-Even Calculation

Third-party logistics (3PL) providers replace the operator's daily packing and shipping labor with a fee-per-order. The fundamental trade-off: you pay per-order fees in exchange for your time back. 3PL only wins when the fee is less than the opportunity cost of the labor you are replacing.

**Self-fulfillment cost at 300 units/month:**
- Packing labor: 90 seconds/order × 300 orders × $15/hr = $112.50/month
- Shipping (Pirate Ship, current rates): $4.50/order × 300 = $1,350/month
- Label printing supplies: ~$5/month
- Total self-fulfillment cost: $1,467.50/month

**3PL cost at 300 units/month (ShipMonk or Simpl Fulfillment as benchmark):**
- Pick-and-pack fee: $2.50–3.50/order × 300 = $750–1,050/month
- Storage: $15–25/month for small ModRun inventory footprint
- Postage: 3PLs typically add $0.50–1.50/order markup over commercial USPS rates = $150–450/month additional vs. self-shipping
- Total 3PL cost: $915–1,525/month

At 300 units/month, 3PL is cost-neutral to slightly worse than self-fulfillment, and you lose control over packaging quality, inserts, and presentation. The math does not support a 3PL at this volume.

**3PL break-even volume (where 3PL saves money):**

3PL saves money when the daily packing labor exceeds the 3PL pick-and-pack premium. At 500 units/month (roughly 17 orders/day), packing takes approximately 25 minutes/day — a manageable daily task that does not warrant 3PL delegation. The break-even on operator time savings (where the freed 25 minutes/day has value exceeding the 3PL premium) comes when:

1. The operator's time is constrained by other revenue-generating activities (new products, Amazon listing optimization, supplier negotiations), AND
2. Volume exceeds approximately 750–1,000 orders/month (25–33 orders/day, roughly 45–60 minutes of daily packing), AND
3. The operation has sufficient cash flow to absorb the 3PL's minimum monthly fee (ShipBob's $275/month minimum kicks in here)

**Hard break-even numbers:**

| Volume | Self-Fulfillment Labor | 3PL Fee Premium | 3PL Viable? |
|---|---|---|---|
| 100 units/mo | $37.50/mo | ~$200/mo | No — 3PL is 5× more expensive |
| 300 units/mo | $112/mo | ~$200/mo | No — 3PL adds $88/mo overhead |
| 500 units/mo | $187/mo | ~$350/mo | No — still adds $163/mo overhead |
| 750 units/mo | $281/mo | ~$500/mo | Break-even approaching if time is constrained |
| 1,000+ units/mo | $375/mo | ~$650/mo | Yes, if multi-channel or operator time is the ceiling |

**Conclusion for the 100–500 unit range:** 3PL is not the right move. The correct approach is a part-time 1099 packing contractor at $15–18/hour for 10 hours/week, hired when order volume exceeds 75 units/week (300 units/month). This costs $600–720/month but keeps postage at Pirate Ship commercial rates (no 3PL markup) and maintains packaging quality control.

### Multi-Product Bundling as a Consolidation Play

The stronger consolidation argument is not 3PL — it is multi-product bundling that increases order AOV without adding per-order shipping cost. ModRun's natural expansion products (Desk Headphone Hook, Cable Spine, Monitor Riser per product-line-strategy.md) all ship in the same poly mailer or small box as a cable clip bundle.

When a customer orders a 3-clip bundle + a headphone hook in one transaction, the $4.50 shipping cost is amortized across a $35–40 order instead of a $24.99 order. Gross margin on the combined order rises to 72–74% even though each product's individual margin is unchanged. This is free consolidation leverage that requires no 3PL, no new infrastructure, and no new suppliers — only a second SKU in the Etsy shop.

At 300 units/month, achieving a 15% multi-product order rate (45 orders where a customer buys two products) improves blended gross margin by approximately 0.8 points and generates an additional $250–300/month in gross profit. This is a larger business improvement than transitioning from 10 kg to 50 kg filament bulk pricing.

---

## Section 4: Printer ROI Analysis

### Printer Economics Baseline

**Bambu P1S (recommended production printer):**
- Purchase price: $699–$799 (AMS Lite included)
- Depreciation life: 5,000 operational hours at $0.14/hour
- Real-world production speed: 12-clip plate in 45 minutes = 16 plates/day at 12-hour operation = 192 clips/day theoretical ceiling, ~130–160 clips/day at 85% utilization
- Per-unit depreciation at full utilization (16 hr/day): $0.04/unit
- Per-unit depreciation at moderate utilization (8 hr/day): $0.10/unit
- Per-unit depreciation at low utilization (2 hr/day): $0.42/unit

The printer's cost contribution is not fixed — it is entirely a function of how hard you run it. This creates a powerful incentive to maximize utilization before buying the next printer.

### First Printer Break-Even (already established)

From the existing cost model, the first printer's $699–$950 startup investment is recovered in Month 1 at 20 units/week. This analysis focuses on the second and third printer decisions.

### Second Printer Break-Even

**Scenario:** Adding a second Bambu P1S ($699–799) at the point when the first printer is running at 80%+ utilization and demand consistently exceeds 50 units/week for two consecutive weeks.

**Investment:** $699–799 (printer only; filament and packaging inventory are operating costs)

**Capacity unlocked:** Doubles clip throughput from ~50 to ~100 units/week at moderate utilization on both printers, or ~80–100 units/week at high utilization with realistic failure rates.

**Incremental revenue unlocked:** Moving from 50 to 100 units/week at $27.50 AOV = $1,375/week additional gross revenue = $5,917/month additional.

**Incremental gross profit at 70% margin:** $5,917 × 0.70 = $4,142/month.

**Second printer payback period:** $749 ÷ ($4,142/month) = **2.2 weeks**. Even at a conservative estimate accounting for demand ramp-up time, the payback is 3–5 weeks.

**The non-obvious value:** The second printer is also production insurance. If one printer jams, fails a calibration, or requires a nozzle replacement (a 20–30 minute event), the other printer continues running. At 50+ units/week, a day of downtime without backup is a $200–275 revenue event. The second printer eliminates single-point-of-failure risk and pays for itself in lost-production insurance alone within a quarter, independent of its capacity contribution.

**Decision rule:** Order the second Bambu P1S when two conditions are met simultaneously: (1) sustained demand above 50 units/week for two consecutive weeks, and (2) the first printer is running more than 10 hours/day. Do not buy speculatively — the printer has near-zero resale loss if bought slightly early, but the capital deployed has better uses (filament inventory, FBA onboarding) if demand signals are unclear.

### Third Printer Break-Even

**Trigger:** The two-printer fleet is consistently running 80%+ utilization (combined 16+ hours/day) and demand exceeds 100 units/week sustained. Expected timeline: Month 8–12 on a strong growth trajectory.

**Investment:** $699–799 (same unit)

**Capacity unlocked:** Adds ~50 units/week at moderate utilization. Moving from ~100 to ~150 units/week.

**Incremental gross profit:** 50 units/week × 4.3 weeks × $27.50 × 0.699 margin = $4,146/month.

**Third printer payback:** $749 ÷ $4,146/month = **2.2 weeks**. Payback math is identical to the second printer because marginal revenue and margin are constant.

**Key difference from second printer:** The third printer forces a process upgrade. At 150+ units/week, daily packing and post-processing exceeds the practical solo capacity. Hiring a part-time contractor ($600–800/month) is a prerequisite for the third printer to actually deliver its capacity. Model the true cost of the third printer as $699 + $7,200/year contractor = $8,600 total-year commitment.

**Adjusted payback with contractor:** Incremental gross profit at 50 additional units/week = $4,146/month. Contractor cost = $700/month. Net incremental profit = $3,446/month. Payback on printer capex alone: 2.6 weeks. The contractor cost is recovered within its first operating month by the additional revenue enabled.

### Printer Fleet Scaling Thresholds (Summary)

| Decision | Trigger Volume | Capital | Payback | Key Dependency |
|---|---|---|---|---|
| Launch (Printer 1) | Demand exists | $699–799 | Month 1 | Test print passing |
| 2nd Printer | 50+ units/week for 2 weeks | $699–799 | 3–5 weeks | Demand evidence, not speculation |
| 3rd Printer | 100+ units/week sustained | $699–799 + $700/mo contractor | 3 weeks (printer alone) | Contractor hired simultaneously |
| 4th+ Printer | 150+ units/week, 3-printer fleet saturated | $699–799 per unit | 2–3 weeks | Print farm management software (SimplyPrint); dedicated space |

---

## Section 5: Geographic Arbitrage — Should Any Operations Move?

### The Core Question

At 100–500 units/month, the operation is home-based FDM manufacturing with self-fulfillment. The geographic arbitrage question has two distinct sub-questions: (A) should production move to a lower-cost region, and (B) should fulfillment move to a Midwest warehouse for shipping savings?

### Sub-Question A: Production Location

**The answer is no, at this scale.** In-house FDM production is not labor-intensive enough to justify geographic relocation. The labor content of producing 500 units/month is approximately 80–100 active operator hours — under 25 hours/week. At $15/hour, the total monthly labor value is $1,200–1,500.

Moving production to a lower-labor-cost region (rural Midwest, Mexico, Southeast Asia) would reduce the $15/hour rate — but the offset costs are prohibitive:
- Equipment relocation: $500–1,500 (shipping printers, filament inventory)
- New facility setup: $0 (home-based) vs. $200–500/month (rented space)
- Operational complexity: Remote print farm monitoring, contractor management, quality control at distance
- Shipping cost from non-prime location to US customers: no improvement over current

The arithmetic does not support relocation at any volume tier examined here. Production should stay co-located with the operator throughout the 100–500 unit range.

**When this calculus changes:** If the operation reaches 2,000+ units/month and requires 3–4 full-time employees, a dedicated manufacturing space becomes viable, and labor costs in a lower-cost metropolitan area (Detroit, Cincinnati, Tulsa) versus a high-cost area (San Francisco, New York) could produce meaningful savings. This is a Year 2+ decision.

### Sub-Question B: Fulfillment Geography

Shipping cost is the dominant variable cost in this business. USPS Ground Advantage pricing is zone-based — an order shipping from San Jose to Boston (Zone 8) costs $1.50–2.00 more than the same order shipping from Chicago to Boston (Zone 4). The US population centroid is roughly in the St. Louis area; a fulfillment location near that centroid would reduce average blended zone by 1–2 zones.

**Estimated shipping savings from Midwest location:**

| Current Location | Blended Average Zone | Blended Average Rate | Midwest Location Rate | Per-Order Savings | Annual Savings at 300 units/mo |
|---|---|---|---|---|---|
| East Coast (NYC) | Zone 4.5 avg | $4.75 | $4.25 | $0.50 | $1,800 |
| West Coast (LA/SF) | Zone 5.5 avg | $5.25 | $4.25 | $1.00 | $3,600 |
| Midwest (Chicago) | Zone 3.5 avg | $4.25 | already optimal | $0 | $0 |

For a West Coast operator, Midwest fulfillment could save $1.00/order — meaningful at 500 units/month ($6,000/year savings). However, this saving requires either (A) operating a second location, which creates complexity far exceeding the saving, or (B) using a 3PL or FBA in the Midwest — which, as Section 3 establishes, is not cost-effective until 750–1,000 units/month.

**Practical recommendation:** If the operator is currently on the West Coast and approaches 500 units/month, Amazon FBA (where Amazon's fulfillment centers are distributed nationally) is the correct vehicle for geographic arbitrage. FBA automatically routes orders from the nearest fulfillment center, averaging Zone 2–3 for most US customers. The FBA fee premium (~$3.22–3.83/unit fulfillment fee + 15% referral) must be offset against the shipping savings: at $5.25 current shipping and $3.50 FBA fulfillment with 15% referral, the net fee load on a $24.99 order is approximately $7.24 via FBA versus $5.25 + $2.37 Etsy fees = $7.62 self-fulfilled. FBA is actually slightly cheaper per-order for West Coast operators at $24.99 ASP — a finding that inverts the conventional wisdom that FBA is more expensive.

East Coast operators have no geographic arbitrage available from location change. Current blended rates are already near optimal.

---

## Section 6: Decision Tree and Go/No-Go Thresholds

### Master Decision Framework

This section consolidates all scaling decisions into a sequence of Go/No-Go gates based on quantified triggers. Each decision is stated as a testable condition with a specific threshold.

---

**Gate 1: Launch (already triggered post-test-print)**

- Condition: Test print passes 4/4 criteria
- Action: Begin production at whatever demand exists
- Capital: $950 startup (already deployed)
- No numerical threshold required — if test print passes, launch

---

**Gate 2: Transition to 10 kg Filament Bundles**

- Trigger: Monthly filament consumption exceeds 8 kg (any single color)
- Equivalent volume: ~100 units/month of clip mix
- Capital: $115–130 (one 10 kg Amazon bundle)
- Savings: $3–5/kg vs. retail spools = $24–40/month at this consumption rate
- Payback: Immediate (one order cycle)
- **Go/No-Go: GO at first month where any color consumes >8 kg. This is the easiest decision in the model.**

---

**Gate 3: Add Second Bambu P1S**

- Primary trigger: Demand exceeds 50 units/week for two consecutive weeks AND first printer runs >10 hours/day
- Secondary trigger: Backlog orders exist (customers waiting >5 days for in-stock items)
- Capital: $699–799 (printer only)
- Payback: 3–5 weeks at full utilization
- Revenue unlocked: +$4,142/month gross profit at 50 additional units/week
- Risk: Buying speculatively when demand is not yet confirmed. The printer can be sold for $500–600 on the secondary market if demand does not materialize — maximum downside is $150–200 loss.
- **Go/No-Go: GO when 50 units/week demand is confirmed for 2 consecutive weeks. WAIT if demand is inconsistent or seasonal.**

---

**Gate 4: Hire Part-Time Contractor (1099 Post-Processor)**

- Trigger: Post-processing + packaging + shipping prep exceeds 2 hours/day consistently (approximately 75+ units/week or 300+ units/month)
- Cost: $600–800/month (10–15 hours/week at $15–18/hour)
- Value: Frees operator for high-value tasks (new listings, Amazon expansion, supplier negotiations)
- Net impact: −$0.17/unit gross margin; +approximately $500–1,000/month in incremental revenue enabled by freed operator capacity
- Form: 1099 independent contractor only. Avoid W-2 — payroll overhead (FICA, workers' comp) adds 15–20% to labor cost.
- **Go/No-Go: GO at 300+ units/month when daily packing exceeds 2 hours. OPTIONAL at 200 units/month if operator has other income-generating activities competing for time.**

---

**Gate 5: Transition to Anycubic 50 kg Filament Pallet**

- Trigger: Monthly filament consumption exceeds 25 kg (approximately 300+ units/month blended mix)
- Capital: $524.73 (50 kg at $10.49/kg)
- Savings vs. 10 kg Amazon bundles: $1.00–1.50/kg = $25–37.50/month at 25 kg consumption
- Annualized savings: $300–450/year
- Prerequisites: (1) Anycubic AMS compatibility validated via test order, (2) dry storage infrastructure in place (sealed rack with desiccant, approximately $80–120 one-time investment), (3) cash position supports $524 outlay
- Payback: 14–20 months (savings-based) or immediately if treated as working capital (inventory has resale value)
- **Go/No-Go: GO at 300+ units/month IF Anycubic has been pre-qualified AND dry storage is available. WAIT if either prerequisite is unmet — a bad 50 kg pallet of filament that causes AMS feed errors is a $524 loss plus production downtime.**

---

**Gate 6: Amazon FBA Onboarding**

- Trigger: Etsy volume reliably at 50+ units/week for 4 consecutive weeks AND operator has $400–500 in discretionary capital AND Etsy review base exceeds 20 with 4.8+ average
- Capital: $300–500 (FBA preparation labels, initial inventory batch of 50–75 units)
- Revenue impact: FBA channel adds 20–40% incremental units above Etsy ceiling; does not cannibalize Etsy
- Fee structure: 15% Amazon referral + $3.22–3.83 FBA fulfillment = 27–35% total fees vs. Etsy 9.5%. Lower margin per unit but higher volume potential. For West Coast operators, net per-unit economics may favor FBA slightly (see Section 5).
- Product fit: Top 2–3 Etsy SKUs only. Do not send every variant to FBA — focus on 3-clip bundle and 1-rail SKUs.
- **Go/No-Go: GO at 50+ units/week Etsy with $400 available capital. WAIT if Etsy is still growing organically (organic growth means Etsy ceiling has not been reached).**

---

**Gate 7: Polymaker Wholesale Activation (Quality Tier)**

- Trigger: Production confirmed at 50+ units/week AND white/grey SKUs are among top 3 sellers
- Capital: $1,000 minimum order (~67 kg PolyLite PLA at $14.99/kg)
- Incremental cost vs. eSUN: +$2.99/kg = +$0.21/unit at 70g. Costs $157 more per month at 500 units/month.
- Benefit: Batch-to-batch color consistency, vacuum packaging preventing moisture-induced print failures, documented certificates of analysis. For white filament specifically, eSUN's batch variation can produce visible color shift between orders. Polymaker eliminates this.
- **Go/No-Go: GO for white and light grey only when at 50+ units/week. STAY on eSUN for black (color consistency irrelevant for black; cost matters more).**

---

**Gate 8: Add Third Printer**

- Trigger: Two-printer fleet at 80%+ combined utilization (>16 hours/day total) for 2+ consecutive weeks AND demand evidence above 100 units/week
- Capital: $699–799 (printer) + $700/month (contractor, if not already hired)
- Payback on printer capex: 2.6 weeks net of contractor cost
- Process prerequisite: Bambu Farm Manager or SimplyPrint running for queue coordination before third printer arrives. Adding a third printer without queue management software creates coordination overhead that erodes the throughput gain.
- Expected timeline: Month 8–14 on a strong growth trajectory.
- **Go/No-Go: GO when 100 units/week is sustained for 2+ weeks. DO NOT pre-buy in anticipation.**

---

**Gate 9: Dedicated 3PL Engagement**

- Trigger: Order volume exceeds 750 orders/month AND daily packing exceeds 45 minutes even with a contractor AND operator's strategic time is fully committed to growth activities
- Best-fit providers at this volume: Simpl Fulfillment (no minimum, flat-rate), ShipMonk (50+ order minimum)
- **Go/No-Go: NOT triggered within the 100–500 unit/month range of this analysis. Revisit at 750+ units/month.**

---

### Quantified Decision Summary Table

| Decision | Hard Threshold | Capital | Monthly Profit Impact | Risk If Wrong |
|---|---|---|---|---|
| 10 kg filament bundle | 8 kg/month consumption | $130 | +$30–40/mo | Near zero — still useful inventory |
| 2nd Printer | 50 units/week × 2 weeks | $699–799 | +$4,100/mo (at capacity) | $150–200 resale loss if wrong |
| 1099 Contractor | 300 units/month | $700/mo | +net positive via freed capacity | None — month-to-month arrangement |
| Anycubic 50 kg pallet | 300 units/month + AMS pre-qual | $525 | +$25–38/mo | $500+ loss if AMS incompatible |
| Amazon FBA | 50 units/week + $400 capital | $400–500 | +20–40% revenue additive | FBA fee load if volume doesn't materialize |
| Polymaker wholesale | 50 units/week, white/grey | $1,000 | −$157/mo (cost), +quality | Overinventory if color sales shift |
| 3rd Printer | 100 units/week × 2 weeks | $699–799 | +$3,400/mo net of contractor | $150–200 resale loss if wrong |
| 3PL | 750+ orders/month | Variable | Net neutral initially | Packaging quality risk |

---

## Confidence Notes and Model Limitations

**High confidence (derived from verified pricing and existing cost models):**
- All filament pricing tiers: verified against live Amazon, Anycubic store, and Polymaker wholesale page data (May 2026)
- Etsy fee structure (9.5%): documented Etsy fee schedule
- Printer capex ($699 P1S): current US Bambu store price
- Depreciation rate ($0.14/hr): derived from $699 ÷ 5,000 hr
- USPS rates: confirmed post-8% surcharge (Pirate Ship documentation, April 2026)
- Shipping cost structure: derived from production-scaling-research.md Section 3.3 and supplier-economics.md

**Medium confidence:**
- Blended filament weight (70g/order): derived from modeled 70/30 clip/rail mix; actual weight depends on order mix that emerges from Etsy data
- Contractor cost trigger ($600–800/month at 300 units): based on production-scaling-research.md labor model benchmarks; actual threshold depends on the specific operator's post-processing speed
- Anycubic AMS compatibility: mixed community reports; validation test order is the only way to confirm for a specific printer

**Gaps:**
- Exact USPS zone distribution from operator's specific zip code: use Pirate Ship's rate calculator with 10 actual past-order addresses to calibrate the blended shipping cost
- eSUN direct wholesale pricing at 20+ kg/month commitment: requires direct inquiry to esun3dstore.com; could unlock $9.50–10.50/kg vs. current $11–12/kg on Amazon bundles
- Anycubic 100 kg pallet pricing: not publicly listed; quoted on request only

---

## Sources

- [Anycubic Bulk PLA 50–100kg Deals](https://store.anycubic.com/products/pla-basic-50-100kg-deals)
- [eSUN PLA+ 10kg Bundle — Amazon B0G2KWC5XL](https://www.amazon.com/eSUN-Pro-Grade-Toughness-Clog-Free-Dimensional/dp/B0G2KWC5XL)
- [Polymaker US Wholesale Program](https://us-wholesale.polymaker.com/)
- [Pirate Ship: April 2026 USPS Time-Limited Price Change](https://support.pirateship.com/en/articles/14491291-april-2026-usps-time-limited-price-change)
- [ShipMonk Pricing — Small Business 3PL](https://www.shipmonk.com/)
- [Simpl Fulfillment — Flat-Rate 3PL](https://www.simplfulfillment.com/)
- [Amazon FBA Fees 2026 — AMZ Prep](https://amzprep.com/amazon-fba-fees/)
- Internal: cost-model-spreadsheet.csv (Session throughput model, all tiers)
- Internal: scaling-cost-model.csv (Session 717, May 2026)
- Internal: supplier-economics.md (filament tier pricing, tariff analysis)
- Internal: phase-2-supplier-research.md (bulk purchasing breakpoints, 3PL comparison)
- Internal: production-scaling-research.md (printer throughput, bottleneck analysis)
- Internal: production-workflow-v1.md (labor times, per-unit economics)
- Internal: multi-printer-architecture.md (printer capex, fleet ROI)
- Internal: amazon-fba-analysis.md (FBA fee schedule, channel strategy)
- Internal: 100-unit-operations-blueprint.md (operational thresholds)
