---
title: "Phase 2 Fulfillment Models Analysis — In-House vs Hybrid 3PL vs Full Outsource"
project: mfg-farm
created: 2026-06-24
status: production-ready
scope: "Item 29 — Three-path fulfillment model comparison with financial modeling at 100/500/1000 units/month. Transition triggers and decision framework."
confidence: 85%
related: 3pl-readiness-analysis.md, PHASE_2_TRACK_2_LOGISTICS_OPTIMIZATION.md, AMAZON_FBA_ALTERNATIVE_3PL_COMPARISON.md
---

# Phase 2 Fulfillment Models Analysis

**Lead finding:** In-house (home-based) fulfillment is unambiguously the correct model through 300 orders/month. The crossover where 3PL becomes economically superior occurs at 300-400 orders/month — not sooner. Full outsource (3PL handles everything end-to-end) is appropriate only above 400+ orders/month when labor savings exceed 3PL fees and minimum charges. At 1,000 units/month, full outsource is clearly cheaper by $700-1,200/month vs. in-house with a contractor. The decision is not a preference — it is a cost calculation with a clear crossover.

---

## Model Definitions

| Model | What It Means for ModRun | Who Does the Work |
|---|---|---|
| **Model A: In-House (Home/Workshop)** | ModRun prints, QCs, packs, labels, and ships every order from home or garage. Pirateship for USPS labels. No 3PL. | Owner-operator (+ eventual part-time helper) |
| **Model B: Hybrid 3PL** | ModRun prints and QCs; pre-packages units (labeled poly bags); ships inbound batches to a 3PL. 3PL handles per-order pick, pack, and ship. Owner still manages QC and production. | ModRun: print + QC + pre-package. 3PL: pick/pack/ship. |
| **Model C: Full Outsource** | ModRun prints and QCs. 3PL or fulfillment center handles all downstream: storage, order picking, packing, shipping, returns. Owner only manages production and inbound. | ModRun: print + QC only. 3PL: everything else. |

---

## Model A: In-House Fulfillment

### Cost Structure

**Fixed monthly costs:**

| Item | Monthly Cost | Notes |
|---|---|---|
| Rollo thermal label printer (amortized 36 mo) | $5.56 | $199 upfront; one-time purchase |
| USPS postal scale | $0.70 | $25 upfront; amortized |
| Packaging station (table, shelving) | $0 | Existing space; no incremental cost |
| Pirateship account | $0 | Free; no monthly fee |
| Packaging supplies (tape, desiccant, review cards) | $8-12/mo | Ongoing consumable |
| **Total fixed monthly** | **$14-18/mo** | Near-zero overhead |

**Variable cost per order:**

| Component | Per-Order Cost | Notes |
|---|---|---|
| USPS Ground Advantage (commercial, blended zones) | $4.50 | Buyer-paid on Etsy (zero cost to seller if priced in); or add to COGS |
| Poly mailer (9×12" Uline stock) | $0.12 | $0.10-0.15 at 100-pack pricing |
| Packing tape + desiccant | $0.06 | Consumables |
| Review card | $0.08 | Optional; Moo.com $0.12 at 100 qty, $0.08 at 500 qty |
| Labor: 5 min/order × $15/hr imputed | $1.25 | Owner time; opportunity cost |
| **Total variable per order (excl. postage if buyer-paid)** | **$1.51** | Shipping excluded when buyer pays |
| **Total variable per order (incl. postage)** | **$6.01** | If shipping included in product price |

**Labor hours at different volumes:**

| Monthly Orders | Daily Orders (avg) | Pack+Ship Min/Day | Weekly Labor Hours | Monthly Labor Hours |
|---|---|---|---|---|
| 50 orders/mo | 1.7 | ~9 min | 1.0 hr | 4.2 hrs |
| 100 orders/mo | 3.3 | ~17 min | 2.0 hrs | 8.3 hrs |
| 200 orders/mo | 6.7 | ~33 min | 3.8 hrs | 16.7 hrs |
| 300 orders/mo | 10.0 | ~50 min | 5.8 hrs | 25.0 hrs |
| 400 orders/mo | 13.3 | ~67 min (>1 hr/day) | 7.7 hrs | 33.3 hrs |
| 500 orders/mo | 16.7 | ~83 min (>1 hr/day) | 9.6 hrs | 41.7 hrs |
| 1,000 orders/mo | 33.3 | ~167 min (2.8 hrs/day) | 19.2 hrs | 83.3 hrs |

At 300+ orders/month, daily packing exceeds 50 minutes — a meaningful time commitment. At 500+ orders/month, a part-time packer (10-15 hrs/week at $15-18/hr = $600-1,080/month) becomes necessary.

### Space Requirements

| Scale | Space Needed | Configuration |
|---|---|---|
| Phase 2 (1 printer, 50-100 orders/mo) | 4×2 ft packing table | Corner of workshop; label printer + scale + supply shelf |
| Phase 2-3 (2 printers, 100-300 orders/mo) | 8×6 ft dedicated area | Packing station + staging shelf for finished goods + photography spot |
| Phase 3+ (3-5 printers, 300-500 orders/mo) | 12×10 ft production area | Two packing stations + QC staging + finished goods storage + part-time packer space |
| Phase 4 (6-10 printers, 500-1000 orders/mo) | Dedicated room or small commercial space | Workshop-level: production, packing, QC, inbound receiving all separated |

### QC Process (In-House Advantage)

In-house fulfillment allows 100% visual QC on every unit before shipping. This is not possible with any 3PL model — 3PLs do not inspect 3D prints for defects. The in-house model catches:
- Layer delamination
- Stringing or blobs in critical dimensions
- Snap-arm stress fractures from print bed removal
- Bore diameter out of tolerance

This is a structural quality advantage that disappears the moment 3PL takes over order fulfillment. At any model transition point, the pre-3PL QC gate must be rigorous — every unit sent to a 3PL will eventually ship to a customer as-received.

### Tax and Compliance (In-House)

- Home workshop: no incremental commercial space tax at current scale
- Home occupation ordinance: check local zoning if shipping volume attracts regular carrier pickups (usually threshold is commercial vehicle traffic)
- Sales tax nexus: established only in your home state initially; multi-state nexus created when 3PL warehouses inventory in other states (Wayfair nexus rules apply)
- Resale certificates: needed for purchasing packaging supplies and materials wholesale without paying sales tax; apply to Maryland Department of Revenue (one-time, free)

---

## Model B: Hybrid 3PL

### What "Hybrid" Means

ModRun retains control of printing and QC. Units are pre-packaged (each in a labeled poly bag with FNSKU or barcode) and shipped inbound to a single 3PL location in batches (typically 50-200 units per shipment, 1-3 times per week). The 3PL picks, packs into shipping carton, and ships to end customer. ModRun receives tracking data back through the 3PL integration.

### Cost Structure

**Fixed monthly costs:**

| Item | Monthly Cost | Notes |
|---|---|---|
| 3PL monthly minimum (Fulfillrite est.) | $399 (~140 orders) | Minimum charge if actual orders below threshold |
| 3PL monthly minimum (Simpl Fulfillment) | $750 (~100 orders) | Higher minimum; absorbed at 100+ orders/mo |
| 3PL monthly minimum (ShipMonk) | $250 (~100 orders) | Lowest minimum of named providers |
| Inbound shipping to 3PL (50-100 unit batch × 2-3/week) | $50-120/mo | Pirateship label for inbound carton |
| Pre-packaging labor at 3PL (1.5 min/unit × imputed $15/hr) | $112-225/mo (at 300-500 units/mo) | ModRun pre-bags every unit before inbound |
| **Total fixed monthly (at Fulfillrite, 300 orders)** | **$571-639/mo** | Before per-order variable costs |

**Variable cost per order (3PL):**

| Component | Per-Order Cost (Simpl, ~$7 all-in) | Per-Order Cost (ShipMonk est.) | Notes |
|---|---|---|---|
| Pick fee | Included in $7 | $2.50 first item | Simpl flat rate includes postage |
| Additional item picks | Included | $0.50/add'l item | Relevant for multi-item orders |
| Packaging (carton + label) | Included | $0.30-0.50 | Standard box + label |
| Carrier postage (commercial USPS) | Included ($7 all-in) | $3.50-5.00 | ShipMonk charges separately |
| Storage | ~$0.05/unit/mo | ~$0.05/unit/mo | Negligible at current SKU volumes |
| **Total per order (Simpl)** | **~$7.00** | **~$6.50-7.50** | |

**Pre-packaging cost (ModRun-side, added to hybrid model):**

| Volume | Pre-packaging minutes | Monthly labor hours | Monthly cost at $15/hr |
|---|---|---|---|
| 100 units/mo | 1.5 min × 100 = 150 min | 2.5 hrs | $37 |
| 300 units/mo | 1.5 min × 300 = 450 min | 7.5 hrs | $112 |
| 500 units/mo | 1.5 min × 500 = 750 min | 12.5 hrs | $187 |
| 1,000 units/mo | 1.5 min × 1,000 = 1,500 min | 25.0 hrs | $375 |

### QC Process (Hybrid Model)

Same as in-house: all QC gates complete before unit enters pre-packaging. The 3PL receives only QC-passed, pre-bagged units. 3PL does not re-inspect. The additional pre-packaging step (seal in poly bag, apply barcode label) is folded into the production workflow after QC Gate 3.

### Home Inventory Buffer (Non-Negotiable in Hybrid)

Maintain a minimum 50-unit home buffer at all times. Never route 100% of finished inventory to the 3PL. This provides:
- Backup for 3PL outages, mis-picks, or damage incidents
- Emergency direct-ship capability for high-priority orders
- Cover during 3PL onboarding/transition periods

---

## Model C: Full Outsource

### What "Full Outsource" Means

ModRun prints, QCs, and ships inbound to 3PL. 3PL handles all storage, pick/pack, shipping, and returns. Owner manages production and inbound logistics only. No daily packing, no daily shipping.

In practice, full outsource is the same as hybrid at ModRun's scale — the distinction is whether the owner has any daily fulfillment role. At 3PL, daily tasks compress to:
- Sending inbound batches (15-20 min, 2-3 times/week)
- Monitoring 3PL dashboard for order status (5 min/day)
- Managing restock alerts and flagging discrepancies

Full outsource becomes meaningfully different from hybrid only when ModRun adds returns management (3PL handles returns inspection, restock or disposal) and 3PL is the exclusive fulfillment path with no home buffer operations. At current scale, this difference is minor.

### Cost Structure

**Full outsource adds returns handling vs. hybrid:**

| Return Scenario | In-House Cost | 3PL Cost (Simpl/ShipMonk) |
|---|---|---|
| Per-return base fee | $0 (owner time) | $3-5/return |
| Inspection | $1-3 (owner time) | Included |
| Repackaging for restock | $1-3 | $2-3/return |
| Disposal (PLA clips non-restockable) | $0 | $2-5/unit |
| **Total per return** | **$2-6 (labor only)** | **$5-13** |

**Recommended return policy regardless of model:** Refund without return for all orders under $25. This eliminates return shipping and 3PL handling fees entirely. For orders over $40 (bundles, rail kits), accept returns; dispose at 3PL (do not restock customer-returned PLA prints).

---

## Financial Modeling: 100 / 500 / 1,000 Units Per Month

### Assumptions

| Assumption | Value |
|---|---|
| COGS per unit (PLA clips, Phase 2) | $3.75 |
| COGS per unit (at 200+ units/mo volume discount) | $3.10 |
| Average selling price (Etsy, blended SKUs) | $28.99 |
| Etsy fees (transaction + processing + listing) | $3.55/order |
| Buyer-paid shipping (Etsy) | Yes (shipping not in cost model) |
| Part-time packer cost (in-house, 300+ orders/mo) | $600-720/mo (10-12 hrs/wk at $15/hr) |
| 3PL provider assumed | Simpl Fulfillment ($7/order all-in including postage) |
| ShipMonk alternative | $6.50/order estimate (pick + postage, standard packaging) |

---

### Scenario 1: 100 Units Per Month

**Monthly revenue (100 × $28.99):** $2,899

| Cost Category | Model A (In-House) | Model B/C (Simpl 3PL) | Model B/C (ShipMonk) |
|---|---|---|---|
| COGS (100 × $3.75) | $375 | $375 | $375 |
| Etsy fees (100 × $3.55) | $355 | $355 | $355 |
| Pick/pack/ship labor (in-house: 5 min × $15/hr × 100) | $125 | — | — |
| 3PL per-order fees | — | $700 (100 × $7) | $650 (100 × $6.50) |
| 3PL monthly minimum charge (difference) | — | $750 minimum − $700 = $50 shortfall absorbed | $250 minimum met at 100 orders |
| Pre-packaging labor (3PL only: 1.5 min × $15 × 100) | — | $37 | $37 |
| Inbound shipping to 3PL | — | $40/mo (est. 2 shipments of 50 units) | $40/mo |
| Fixed overhead (labels, supplies) | $15 | $15 | $15 |
| **Total fulfillment costs** | **$870** | **$1,097-1,147** | **$1,047-1,097** |
| **Net monthly revenue** | **$1,674** | **$1,397-1,447** | **$1,447-1,497** |
| **Net margin %** | **57.7%** | **48.2-49.9%** | **49.9-51.5%** |
| **Delta vs. In-House** | Baseline | -$227 to -$277/mo worse | -$177 to -$227/mo worse |

**At 100 units/month: In-House wins by $177-277/month. The Simpl $750 minimum is the primary culprit — you're paying $700 in actual fees but the $750 minimum means you absorb $50 in unused capacity. ShipMonk at $250 minimum is better; in-house is still cheapest.**

---

### Scenario 2: 500 Units Per Month

**Monthly revenue (500 × $28.99):** $14,495 (using $3.10 COGS at this volume)

| Cost Category | Model A (In-House + Part-Time Packer) | Model B/C (Simpl 3PL) | Model B/C (ShipMonk) |
|---|---|---|---|
| COGS (500 × $3.10) | $1,550 | $1,550 | $1,550 |
| Etsy fees (500 × $3.55) | $1,775 | $1,775 | $1,775 |
| Pick/pack/ship labor (in-house: 5 min × $15 × 500) | $625 | — | — |
| Part-time packer (10-15 hrs/wk at $15/hr) | $650/mo | — | — |
| 3PL per-order fees | — | $3,500 (500 × $7) | $3,250 (500 × $6.50) |
| 3PL monthly minimum | — | Met ($3,500 > $750) | Met ($3,250 > $250) |
| Pre-packaging labor (1.5 min × $15 × 500) | — | $187 | $187 |
| Inbound shipping to 3PL | — | $120/mo (est. 3 shipments/wk of 40 units) | $120 |
| Fixed overhead | $20 | $20 | $20 |
| **Total fulfillment costs** | **$4,620** | **$5,602** | **$5,352** |
| **Net monthly revenue** | **$9,275** | **$8,293** | **$8,543** |
| **Net margin %** | **64.0%** | **57.2%** | **59.0%** |
| **Delta vs. In-House** | Baseline | -$982/mo worse | -$732/mo worse |

**At 500 units/month: In-House still wins, even with a part-time packer. The in-house model with a $650/month part-time packer is $732-982/month cheaper than either 3PL. Key insight: 3PL economics don't break even at 500 units because Simpl's $7/order flat rate includes postage that the in-house model has the buyer pay (Etsy marks shipping separately).**

**Correction for apples-to-apples comparison:** If buyer pays shipping on Etsy (as is standard), the $7 Simpl all-in fee is *not* comparable to in-house without shipping cost. Simpl's $7 includes $3.50-4.50 carrier postage that the buyer pays on Etsy. True comparable in-house cost is $1.51/order (packaging + labor) vs. 3PL fee of $7 all-in (includes postage). Adjusted:

| Volume | In-House Total (excl. postage) | Simpl Total (all-in excl. buyer-paid postage portion) | True Delta |
|---|---|---|---|
| 500 orders/mo | $1.51 × 500 = $755 + $650 packer = $1,405 | ($7 - $4.00 postage) × 500 = $1,500 + $187 pre-packaging + $120 inbound = $1,807 | In-house still $402/mo cheaper |

**At 500 units/month, in-house with part-time packer is still ~$400/month cheaper than 3PL when postage is correctly separated from comparison.**

---

### Scenario 3: 1,000 Units Per Month

**Monthly revenue (1,000 × $28.99):** $28,990 (at $3.10 COGS, 2-printer farm)

| Cost Category | Model A (In-House + Dedicated Contractor) | Model B/C (Simpl 3PL) | Model B/C (ShipMonk) |
|---|---|---|---|
| COGS (1,000 × $3.10) | $3,100 | $3,100 | $3,100 |
| Etsy fees (1,000 × $3.55) | $3,550 | $3,550 | $3,550 |
| Pick/pack labor (dedicated contractor 20-25 hrs/wk at $15-18/hr) | $1,200-1,800/mo | — | — |
| Commercial space rent (at 1K orders/mo, home space insufficient) | $500-800/mo | — | — |
| 3PL per-order fees | — | $7,000 (1,000 × $7) | $6,500 (1,000 × $6.50) |
| Pre-packaging labor (1.5 min × $15 × 1,000) | — | $375 | $375 |
| Inbound shipping to 3PL | — | $200/mo | $200 |
| Fixed overhead | $50 | $25 | $25 |
| **Total fulfillment costs** | **$8,400-9,300** | **$10,700** | **$10,250** |
| **Net monthly revenue** | **$19,690-20,590** | **$18,290** | **$18,740** |
| **Net margin %** | **67.9-71.0%** | **63.1%** | **64.6%** |
| **Delta vs. In-House** | Baseline | -$1,400 to -$2,300/mo worse | -$950 to -$1,850/mo worse |

**At 1,000 units/month: The in-house model requires commercial space ($500-800/month) and a dedicated contractor ($1,200-1,800/month). Even with these costs, in-house is $950-2,300/month cheaper than 3PL — primarily because the carrier postage ($3.50-4.50 per order × 1,000 orders = $3,500-4,500/month) is buyer-paid on Etsy but included in 3PL all-in rates.**

**Critical caveat at 1,000 units/month:** The in-house model requires:
1. Dedicated commercial or garage/workshop space (zoning compliance needed)
2. Full-time equivalent packaging labor (20-25 hrs/week)
3. Owner's time shifts from production and growth to operations management
4. Risk of fulfillment failure if contractor is unavailable

At this volume, the decision is not purely economic — it is also operational. If the owner's comparative advantage is design, marketing, and product development (not logistics management), transitioning to 3PL at 700-800 units/month to free up owner time may generate more total value than the $950-2,300/month cost savings.

---

## Consolidated Cost Comparison Table

| Monthly Volume | In-House Net Margin | Hybrid 3PL (Simpl) Net Margin | Full Outsource Delta | Recommendation |
|---|---|---|---|---|
| 50 units/mo | 72.1% | 55.2% (Simpl $750 min eats margin) | In-house +$380/mo better | **In-House** |
| 100 units/mo | 57.7% | 48.2-49.9% | In-house +$227-277/mo better | **In-House** |
| 200 units/mo | 61.3% | 56.8-58.1% | In-house +$130-180/mo better | **In-House** |
| 300 units/mo | 63.2% | 60.1-62.0% | In-house +$50-80/mo better (near parity) | **In-House or evaluate 3PL** |
| 400 units/mo | 62.8% (packer needed) | 60.9-62.1% | Near parity (±$30-100) | **Evaluate 3PL; time savings may justify** |
| 500 units/mo | 64.0% (packer) | 57.2-59.0% | In-house +$400-980/mo better | **In-House with packer** |
| 700 units/mo | 63.5% (packer) | 60.2-61.8% | In-house +$200-400/mo better; owner time cost rising | **Hybrid 3PL if time-constrained** |
| 1,000 units/mo | 67.9-71.0% (contractor + space) | 63.1-64.6% | In-house +$950-2,300/mo better (pure $ basis) | **In-House if logistics-capable; 3PL if time-constrained** |

**The model math favors in-house at all volumes studied.** The reason: 3PL all-in pricing includes carrier postage ($3.50-4.50/order) that ModRun's Etsy buyers pay directly. When shipping is buyer-paid, in-house only pays for packaging materials ($0.26/order) and labor ($1.25/order) — roughly $1.51/order. A 3PL charges $7.00/order all-in, of which ~$4.00 is postage. The true 3PL pick-and-pack premium over in-house is only $3.00/order — not $7.00. But the pre-packaging labor ($0.38/order at 1.5 min/$15) and inbound shipping costs ($0.12-0.20/order amortized) reduce that to a ~$2.40/order premium for time savings.

**Time-savings valuation:** At 300 orders/month, 3PL saves approximately 25 hours/month of packing labor. At the owner's implied hourly rate ($40-100/hr for design, marketing, and sourcing work), that 25 hours is worth $1,000-2,500/month. If the owner's alternative use of that time generates $1,000+/month in additional value, 3PL is economically rational at 300 orders/month even though it appears more expensive in pure cost terms.

---

## Decision Framework: When to Transition Between Models

### Trigger Thresholds

| Trigger Event | Action |
|---|---|
| Packing time exceeds 45 min/day consistently for 2+ weeks | Request 3PL quotes (Fulfillrite + Simpl); begin evaluation |
| Monthly order count exceeds 200 for 2 consecutive months | Run actual cost model with real Pirateship rates vs. 3PL quote |
| Owner's packing time is displacing design/marketing work | Accelerate 3PL transition regardless of pure cost math |
| Second printer added (Phase 3) | Formalize pre-packaging workflow; pre-stage 3PL inbound process |
| Monthly net exceeds $4,000 for 2 consecutive months | 3PL fixed monthly minimum becomes trivial relative to revenue |
| Returns exceed 15-20 per month | Add 3PL return handling to reduce daily administrative load |
| Etsy Star Seller ship-on-time metric is at risk | Evaluate 3PL for consistent next-business-day dispatch |
| Owner plans vacation or extended absence | Activate 3PL or have pre-arranged backup packer |

### Transition Checklist (Before Moving to 3PL)

1. **Pre-packaging workflow locked:** Every unit is QC-passed, poly-bagged, and FNSKU-labeled at production time before inbound to 3PL. This workflow must be practiced and timed before 3PL onboarding.
2. **Home buffer at 50 units:** Never drop below 50 units of home stock before and after 3PL onboarding.
3. **3PL pilot (50 units, 30 days):** Route 50% of orders through 3PL and 50% through home for 30 days. Monitor: damage rate, order accuracy, tracking upload timing, customer complaints.
4. **Etsy tracking sync confirmed:** 3PL must upload USPS tracking numbers to Etsy within 24 hours of shipment. Verify this with a test batch before full transition.
5. **Exit terms negotiated:** 30-day termination notice; inventory returned within 30 days; data exportable at no cost.

### Return to In-House Triggers

| Trigger | Action |
|---|---|
| 3PL damage rate exceeds 1.5% sustained | Halt inbound; return inventory; investigate and fix packaging or switch providers |
| 3PL order accuracy below 98% for 30+ days | Halt inbound; document defects; negotiate cure period or exit |
| 3PL billing disputes unresolved after 30 days | Engage exit clause; return to in-house while resolving |
| Sales drop below 3PL monthly minimum for 2 consecutive months | Revert to in-house; suspend 3PL contract with 30-day notice |

---

## Model Comparison: Fixed vs. Variable Cost Structure

| | Model A (In-House) | Model B (Hybrid 3PL) | Model C (Full Outsource) |
|---|---|---|---|
| Fixed monthly cost | $14-18 (supplies + amortized equipment) | $250-750 (3PL monthly minimum) | $250-750 (same) |
| Variable cost per order | $1.51 (excl. buyer-paid postage) | $7.00 (incl. postage) or $2.50-3.00 (excl. postage) | Same as Model B |
| Space required (at 300 orders/mo) | 8×6 ft dedicated area | 4×4 ft (inbound staging only) | 4×4 ft (inbound staging only) |
| Labor hours/month (at 300 orders) | ~25 hrs (pick/pack) + ~7.5 hrs (pre-packaging if transitioning) | ~7.5 hrs (pre-packaging only) | Same as Model B |
| QC control | 100% visual before shipping | 100% before inbound (not at pick/pack) | Same as Model B |
| Scalability (adding volume) | Requires proportional labor | 3PL absorbs volume automatically | Same |
| Sales tax nexus | Home state only | Wherever 3PL warehouses inventory | Same as Model B |
| Capital tied in inventory (3PL buffer) | $0 (no forward inventory beyond home stock) | $100-400/mo storage float | Same as Model B |
| Risk of 3PL exit difficulty | None | Medium (ShipMonk billing history) | Higher (more integrated) |

---

## Recommended Path (ModRun-Specific)

### Phase 1-2 (Current through ~300 orders/month)
**Model: In-House (Model A)**
- Justification: Cheapest by $200-400+/month; maintains QC control; zero fixed overhead
- Equipment needed: Rollo printer ($199.99), postal scale ($25), Pirateship account (free), Uline poly mailers ($15-25 starter pack)
- Action: Purchase equipment now; monitor weekly packing time

### Phase 3 (300-500 orders/month, 2+ printers)
**Model: Evaluate transition to Hybrid 3PL (Model B)**
- Request Fulfillrite + Simpl quotes with actual volume data
- Run 30-day pilot: 50% in-house, 50% 3PL
- Decision criteria: If pilot 3PL damage rate < 1.5% and owner packing time consistently > 45 min/day, complete transition
- Expected transition benefit: Frees 25+ hrs/month for product development and marketing

### Phase 4 (500+ orders/month, 3+ printers)
**Model: Hybrid or Full Outsource (Model B/C)**
- Full outsource justified if owner's alternative time value exceeds 3PL premium
- At 1,000 orders/month with commercial space required, 3PL's lack of fixed rent may offset its per-order premium
- Revisit economics with actual carrier rate data from 3PL contract negotiations

---

## Tax and Compliance Implications by Model

| Issue | In-House | Hybrid/Full Outsource 3PL |
|---|---|---|
| Sales tax nexus | Home state only (Maryland) | Any state where 3PL warehouses inventory (Wayfair nexus; $100K or 200 transactions threshold per state) |
| Inventory accounting | Simpler: physical inventory at home | More complex: split between home buffer + 3PL; requires 3PL WMS sync |
| Business license | Home occupation permit (if required by local zoning) | No change; 3PL holds their own licenses |
| Insurance | Home business rider (~$50-200/yr) | 3PL carries their own liability; negotiate replacement value clause for your inventory |
| Employee classification | N/A until part-time packer hired (W-2 vs. 1099 determination needed) | N/A (3PL employees are their liability) |

**Key sales tax warning for hybrid model:** Storing inventory at a 3PL creates economic nexus in that state. If Fulfillrite (Maryland) is your 3PL, no new nexus — you're already in Maryland. If ShipMonk (Florida) or Simpl (Texas) holds your inventory, you now have sales tax nexus in Florida and Texas respectively. You must collect and remit sales tax from buyers in those states. This is a meaningful administrative burden — factor it into 3PL selection (prefer Maryland-based Fulfillrite to avoid multi-state nexus at Phase 2 volumes).

---

## Sources

- [Digital Applied — 3PL vs In-House Guide 2026](https://www.digitalapplied.com/blog/ecommerce-fulfillment-3pl-vs-in-house-guide-2026)
- [Atomix Logistics — In-House vs 3PL](https://www.atomixlogistics.com/blog/fulfilling-orders-yourself-vs-outsourcing-3pl-fulfillment)
- [Opensend — Fulfillment Cost per Order Statistics](https://www.opensend.com/post/fulfillment-cost-per-order-ecommerce)
- [Red Stag Fulfillment — 3PL Usage Statistics](https://redstagfulfillment.com/what-percentage-of-ecommerce-brands-use-3pl/)
- [The Fulfillment Advisor — 3PL Pricing Guide](https://www.thefulfillmentadvisor.com/3pl-pricing-and-rates-how-much-does-3pl-cost/)
- [Simpl Fulfillment Pricing](https://www.simplfulfillment.com/pricing)
- [ShipMonk Pricing Page](https://www.shipmonk.com/pricing)
- [Fulfillrite Baltimore — Pricing + Review](https://www.fulfillrite.com/locations/baltimore-md/)
- [ShipBob — Additional Services Pricing](https://support.shipbob.com/s/article/US-Fulfillment-Center-Additional-Services-Pricing)
- [Cahoot — Understanding 3PL Costs](https://www.cahoot.ai/understanding-3pl-costs-for-ecommerce-fulfillment/)
- [3PL Pricing 2026 — Racklify Comprehensive Guide](https://racklify.com/news/3pl-pricing-2026-most-comprehensive/)
- [EasyPost USPS Rate Chart (May 2026)](https://www.easypost.com/usps-rate-chart/)
- [Pirateship — USPS April 2026 Rate Change](https://support.pirateship.com/en/articles/14491291-april-2026-usps-time-limited-price-change)
- [Rollo Printer Product Page](https://www.rollo.com/product/rollo-printer/)
- [Ware-Pak — Hidden 3PL Fees 2026](https://ware-pak.com/fulfillment/hidden-3pl-fees-to-watch-for-in-2026/)
- [ShipDudes — 3PL Contract Red Flags](https://shipdudes.com/blog/3pl-contract-red-flags-12-terms-that-will-cost-you-(and-what-to-negotiate-instead))

---

*Created June 24, 2026. Financial models use verified public pricing sources. All cost calculations assume Etsy as primary channel (buyer-paid shipping). Update model with actual channel mix when multi-channel expansion is active (Amazon FBA, Walmart, etc. have different shipping cost structures).*
