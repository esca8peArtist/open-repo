---
title: ModRun 3PL Readiness Assessment & Cost-Benefit Analysis
date: 2026-05-06
status: decision-ready
confidence: medium-high
scope: Fulfillment scaling strategy — Month 3+ post-launch decision framework
related: production-workflow-v1.md, fulfillment-workflow.md, scaling-production-research.md
---

# ModRun 3PL Readiness Assessment & Cost-Benefit Analysis

**Lead finding:** No 3PL is ready to handle ModRun's workflow today without a process redesign on ModRun's side. The core problem is inbound: every mainstream 3PL (ShipMonk, ShipBob, Simpl, Fulfillrite) assumes pre-packaged, pre-labeled, individually scannable units arriving on pallets. Shipping loose printed clips in bulk boxes is non-standard and will trigger hourly inbound labor fees or outright rejection. Before any 3PL becomes viable, ModRun must either (a) pre-package every unit before shipping inbound, or (b) negotiate a custom receiving arrangement. Neither option is free.

At ModRun's likely Month 3 volume (35 units/week = ~140/month), the economics also do not support 3PL. The earliest plausible 3PL break-even is approximately 250-300 orders per month — roughly 60-70 units per week at a 1-unit-per-order average, or around Month 5-6 at the current scaling trajectory. Below that threshold, DIY with a part-time post-processor is cheaper and more flexible.

---

## Section 1: 3PL Landscape for 3D Printed Products (May 2026)

### Which 3PLs Explicitly Support 3D Printed Products?

No major 3PL explicitly specializes in FDM 3D printed product fulfillment as of May 2026. The four providers named in the brief (Simpl, ShipMonk, Printful, Blendable) break down as follows:

**Printful** is a print-on-demand (POD) service, not a general 3PL. They print and ship their own products (apparel, mugs, wall art). They cannot accept inbound FDM prints from an external manufacturer. Printful is the wrong category entirely — it would only apply if ModRun licensed its designs to Printful's production pipeline, which does not exist for FDM parts.

**ShipMonk** is a general D2C 3PL with over 100 platform integrations, including Etsy. They support custom kitting and product bundling. They can, in principle, handle 3D printed clips — but only if inbound inventory arrives in a format they can process. Minimum monthly fee: approximately $250/month calculated as (monthly order volume × first-item pick fee) × 0.80. Per-order pick fee: $2.50 for the first item, $0.50 per additional item. Storage: $1/month for a small bin, up to $25/month for a pallet position. ShipMonk does not publicly disclose receiving fees — these are negotiated and typically run $0.20-$0.50/unit for individual item receiving.

**Simpl Fulfillment** is purpose-built for D2C brands shipping 1-500 orders per month. All-inclusive flat rate starting at approximately $7/order (pick, pack, standard packaging, and postage included). No setup fees, no receiving fees for standard inbound. Monthly minimum: $750 (roughly 100 orders). Etsy is listed as a supported integration among 80+ channels. The $750 minimum is the critical constraint: at 100 orders/month it is exactly at threshold; below 100 orders the gap between actual fees and the minimum is a sunk cost.

**Blendable** does not appear in any 2026 3PL directory, review site, or industry publication at research time. The company name does not return results as a 3PL provider. This may be a regional provider, a company that rebranded, or a reference to a service that does not operate at commercial scale. Do not plan around Blendable until confirmed through direct contact.

**Fulfillrite** (East Coast, near Baltimore) is the most promising regional option for ModRun's Maryland location. They serve small ecommerce brands including Etsy sellers, have a 4.9-star Shopify App Store rating, and explicitly accommodate beginner sellers. Monthly minimum approximately $399 (roughly 140 orders). Etsy integration confirmed. No public per-order pricing — quotes required.

**ShipBob** is a large enterprise-oriented 3PL. Setup fee starts at $975. Monthly minimum $275 (fulfillment only; storage and receiving are separate). Order minimum ~400/month with a 90-day grace period. Their inbound receiving is time-based: $35/hour for the first two hours per Warehouse Receiving Order, $45/hour thereafter. Their Etsy integration status is inconsistent in public documentation — some sources say supported, others say not natively integrated. At ModRun's volume, ShipBob's setup cost and order minimum make it a poor fit until Month 8-10 at the earliest.

### The Inbound Problem: Bulk Raw Print Output

This is the single largest operational barrier to 3PL viability for ModRun.

Standard 3PL inbound assumes: labeled cartons, each with a scannable barcode, consistent SKU, accurate packing slips, shipped on standard pallets. A 3PL receives hundreds of inbound shipments daily and cannot manually sort, count, and assign loose items to bins without incurring labor charges.

If ModRun ships a box of 120 loose printed clips (all the same SKU, but loose in a box with no individual packaging), the 3PL will either:

1. Charge hourly labor to count, inspect, and bin each unit individually ($35-65/hour — a box of 120 clips could cost $40-80 to receive), or
2. Require pre-packaging before inbound (each clip in a poly bag with a label/barcode), which pushes the packaging labor back to ModRun.

Option 2 is the correct path: ModRun pre-packages every unit before shipping to the 3PL. This means every clip gets placed in a labeled poly bag or small box with a barcode scannable by the 3PL's WMS. The per-unit packaging labor that currently happens at order time would shift to happen at production time. This changes the workflow but does not eliminate it.

**What this means practically:** Pre-packaging adds approximately 60-90 seconds per unit before shipping inbound to the 3PL. At 100 units/week, that is 100-150 minutes of additional weekly labor. This labor cost must be included in any 3PL cost comparison.

### Storage Capacity at 100-500 Units/Month Scale

ModRun's clip dimensions (approximately 2"×1"×1" per unit) mean very low cubic footage. 500 clips occupy less than 1 cubic foot of storage volume. At $0.30-$0.75/cubic foot/month or $5-$15/month per shelf bin, ModRun's storage cost at any realistic volume is minimal — likely $5-$15/month total regardless of 3PL choice. Storage fees are not a meaningful cost driver at this scale.

The real monthly cost driver is the minimum fee structure, not actual usage.

---

## Section 2: Feature and Integration Matrix

| Feature | ShipMonk | Simpl Fulfillment | Fulfillrite | ShipBob |
|---|---|---|---|---|
| Etsy native integration | Yes (real-time sync) | Yes (80+ channels) | Yes | Inconsistent |
| Per-order fee | $2.50 + $0.50/item | ~$7 all-in | Quote only | $0.30/unit pick |
| Monthly minimum | ~$250 | $750 | ~$399 | $275 (+ storage/receiving separate) |
| Setup fee | $0 | $0 | $0 | $975 |
| Receiving fee | $0.20-0.50/unit | Included (standard inbound) | First 2 hrs flat, then hourly | $35/hr (first 2 hrs), $45/hr after |
| Storage fee | $1-25/bin/month | Included in flat rate | Quoted | $5/bin, $10/shelf, $40/pallet/month |
| Returns handling | Yes | Yes | Yes | Yes |
| Quality inspection | No — seller's responsibility at inbound | No | No | No |
| USPS, UPS, FedEx | All three | All three | All three | All three |
| Minimum volume | None stated | None stated | ~140/mo at minimum fee | 400/mo (90-day grace) |
| Setup timeline | 1-2 weeks | 1 week | ~1 week | 2-4 weeks |
| Exit notice | 30-90 days typical | Negotiated | Negotiated | 30-60 days |

**Quality control:** No 3PL will visually inspect 3D prints for print defects, stringing, or functional issues. This is categorically ModRun's responsibility before inbound. Any unit shipped to the 3PL that fails must be recalled or discarded at ModRun's cost, since the 3PL will pick and ship it exactly as received. The QC gates in production-workflow-v1.md (Gate 1 visual, Gate 2 dimensional, Gate 3 functional snap test) must all be completed before any unit leaves ModRun's possession.

**Returns workflow:** All four 3PLs can handle return shipping and re-stocking. Standard return handling runs $2-5/return for inspection plus restocking. For ModRun's PLA clips, a returned clip is effectively unsaleable (customer-handled, unknown hygiene, unknown snap-arm stress). The correct return policy is refund without return request for orders under $25 — do not have the 3PL restock returns. Budget $3-5/return as a pure disposal cost when using a 3PL.

**Shipping carrier integration:** All four 3PLs support USPS, UPS, and FedEx. ModRun's current Pirate Ship/USPS Ground Advantage workflow would be replaced by the 3PL's carrier selection — they will typically route to the cheapest carrier for each zone. This can be beneficial (3PLs negotiate 20-40% below retail carrier rates) but removes ModRun's direct control over which carrier is used. For USPS Intelligent Mail tracking that feeds into Etsy's tracking upload, any 3PL shipping via USPS will generate compatible tracking numbers.

**Inventory sync:** ShipMonk and Simpl both advertise real-time inventory sync with Etsy. In practice, "real-time" means sync within minutes of order placement, not true live bidirectional sync in all cases. For ModRun's volume, this is sufficient — the scenario where two customers simultaneously buy the last unit in stock (inventory collision) is unlikely below 50 orders/day.

---

## Section 3: Cost Comparison at ModRun Scaling Scenarios

### DIY Cost Baseline (from production-workflow-v1.md)

Current monthly fixed costs (DIY):
- Rollo label printer: $100 amortized over 36 months = $2.78/month
- Poly mailers (100-pack): $7/month at current volume
- Kraft boxes: variable, ~$0.63/unit
- USPS postage via Pirate Ship (commercial rates, no monthly fee): $3.50-5.00/order
- Pirate Ship: $0/month (pay per label)
- Craftybase Studio: $20/month (optional but needed at scale)
- Total fixed overhead: approximately $30/month excluding postage

Per-order variable DIY cost breakdown:
- Packaging (poly mailer, Month 1-2): $0.12/order
- Packaging (kraft box, rail orders): $0.97/order
- USPS Ground Advantage (blended zones): $4.50/order
- Etsy fees: $3.55/order at $24.99 ASP
- Labor (packaging only at $15/hr, 4 min/order): $1.00/order
- **Total DIY per-order variable cost: $9.17-$10.02 (clips), $10.02-$11.54 (rails)**

### 50 Units/Week Scenario (Approximately 200 Orders/Month)

This is Month 4 in the scaling roadmap.

**DIY total monthly cost at 200 orders:**
- Variable costs: 200 × $9.50 avg = $1,900
- Fixed overhead: $30
- Total DIY: **$1,930/month** ($9.65/order)
- Labor: 200 orders × 4 min = 800 min = 13.3 hours = $200/month (imputed at $15/hr)
- DIY with labor: **$2,130/month** ($10.65/order)

**3PL total monthly cost at 200 orders (using Simpl at $7/order all-in excl. Etsy fees):**
- Simpl fulfillment fees: 200 × $7 = $1,400
- Etsy fees (ModRun still owns): 200 × $3.55 = $710
- Pre-packaging labor at 90 sec/unit (ModRun pre-bags before inbound): 200 × 1.5 min = 300 min = 5 hours = $75/month
- Inbound shipping to Simpl (ModRun sends ~50-100 units at a time): estimated $15-25/shipment × 2-3 shipments/month = $50-75
- Total 3PL (Simpl): **$2,235-$2,260/month** ($11.18-$11.30/order)
- Monthly minimum check: $1,400 > $750 — no minimum penalty

At 200 orders/month, DIY with labor ($2,130) is approximately 5% cheaper than Simpl ($2,260). The gap is within the margin of estimation error. The 3PL does not yet offer clear savings.

**3PL total monthly cost at 200 orders (using ShipMonk):**
- ShipMonk pick fee: 200 orders × $2.50 = $500
- Plus 1 additional item on ~50% of orders: 100 × $0.50 = $50
- Storage: $10/month (negligible at this volume)
- Shipping (ShipMonk commercial rates, approximately same as Pirate Ship): $3.50-4.50/order = $700-$900
- Etsy fees: $710
- Pre-packaging labor: $75
- Inbound shipping: $60
- ShipMonk monthly minimum: $250 (met at 200 orders)
- Total 3PL (ShipMonk): **$2,105-$2,305/month** ($10.53-$11.53/order)

ShipMonk at 200 orders is roughly cost-equivalent to DIY when labor is included in both comparisons.

### 100 Units/Week Scenario (Approximately 400 Orders/Month)

This is Month 6-7 in the scaling roadmap, requiring a second printer.

**DIY total at 400 orders:**
- Variable costs: 400 × $9.50 = $3,800
- Fixed overhead: $30
- Labor (400 orders × 4 min = 26.7 hours at $15/hr): $400
- Part-time post-processor already justified at this volume (see production-workflow-v1.md Section 6.2): $600-720/month
- Total DIY with contractor: **$4,830-$4,950/month** ($12.08-$12.38/order)

**3PL total at 400 orders (Simpl):**
- Fulfillment: 400 × $7 = $2,800
- Etsy fees: 400 × $3.55 = $1,420
- Pre-packaging labor (5 hrs/month at $15): $75
- Inbound shipping: $100-150
- Total 3PL (Simpl): **$4,395-$4,445/month** ($10.99-$11.11/order)

At 400 orders/month, Simpl saves approximately $400-$500/month versus DIY with a contractor. 3PL is now measurably cheaper.

**3PL total at 400 orders (ShipMonk):**
- Pick fees: 400 × $2.50 + 200 × $0.50 = $1,100
- Shipping (commercial rates): ~$1,600
- Storage: $10-20
- Etsy fees: $1,420
- Pre-packaging labor: $75
- Inbound shipping: $120
- Total (ShipMonk): **$4,325-$4,345/month** ($10.81-$10.86/order)

ShipMonk and Simpl are roughly equivalent at this volume. ShipMonk's per-item pick model slightly favors multi-item orders; Simpl's flat rate favors consistent single-item orders.

### 200 Units/Week Scenario (Approximately 800 Orders/Month)

This is approximately Month 9-10, well beyond current planning horizon.

**DIY total at 800 orders:**
- Two printers running, dedicated contractor: variable COGS ($9.00 × 800 = $7,200) + labor ($800 contractor) + fixed ($100) = **$8,100/month**

**3PL total at 800 orders (Simpl):**
- Fulfillment: 800 × $7 = $5,600
- Etsy fees: 800 × $3.55 = $2,840
- Pre-packaging: $150
- Inbound: $200
- Total: **$8,790/month** — 3PL is actually slightly more expensive again due to Simpl's all-in postage being priced to average, not optimized per zone

At 800 orders, ShipMonk's model (where you benefit from their negotiated carrier rates at scale) becomes more attractive than Simpl's flat rate. The crossover depends on actual zone mix for ModRun's customer base.

---

## Section 4: Break-Even Analysis and Decision Framework

### Break-Even Model

The crossover point where 3PL becomes cheaper than DIY (with contractor labor) is approximately **300-350 orders per month**, which corresponds to approximately **70-80 units per week** at a 1-unit-per-order conversion rate.

| Monthly Orders | DIY + Labor | Simpl 3PL | ShipMonk 3PL | Delta (DIY vs Simpl) |
|---|---|---|---|---|
| 100 | $1,155 | $1,475 | $1,250 | DIY cheaper by $295-320 |
| 150 | $1,635 | $1,800 | $1,660 | DIY cheaper by $25-165 |
| 200 | $2,130 | $2,260 | $2,200 | Near parity (±$70-130) |
| 300 | $3,100 | $3,160 | $3,100 | Approximate parity |
| 400 | $4,830 | $4,445 | $4,345 | 3PL cheaper by $385-485 |
| 600 | $6,900 | $6,130 | $5,950 | 3PL cheaper by $770-950 |

Notes on model assumptions:
- DIY labor imputed at $15/hour including pre-packaging, pick/pack, label print, USPS staging
- 3PL costs include Etsy fees (ModRun pays these regardless), pre-packaging labor, inbound shipping to 3PL
- Simpl flat rate ~$7/order includes postage; ShipMonk pick + estimated commercial postage ~$6.00-6.50/order total
- Model does not include seasonal surcharges (Q4: +15-30% at most 3PLs)

### Decision Tree by Volume Stage

**Month 1-2 (10-20 units/week, ~40-80 orders/month):** Stay DIY. No 3PL reaches its monthly minimum. The Simpl $750 minimum would add $350-500 of wasted spend at 40-60 orders/month. Continue with Pirate Ship + Rollo printer + USPS pickup.

**Month 3 (35 units/week, ~140 orders/month):** Stay DIY. 3PL is $300-500/month more expensive when monthly minimums and inbound costs are counted. This is the wrong time to switch. The correct action is evaluating 3PL options, getting quotes, and deciding on a target provider so the transition is pre-planned.

**Month 4 (45-50 units/week, ~180-200 orders/month):** Near the cost parity zone. If packaging labor is consistently exceeding 2 hours/day, evaluate initiating a 3PL pilot with 1-2 months of inventory. The economics are close enough that time savings may justify the slight cost premium.

**Month 5-6 (55-70 units/week, ~220-280 orders/month):** 3PL is likely cost-justified if combined with reducing contractor hours. Begin transition at the lower end of this range (220 orders/month).

**Month 7+ (80+ units/week, ~320+ orders/month):** 3PL is clearly cheaper. Remaining DIY at this stage means losing $300-600/month in excess labor cost.

### Risk Factors That Shift the Crossover Point

**3PL damage rate above 2%:** If the 3PL's pick-and-pack process damages more than 2% of PLA clips (snapped arms, scuffed surfaces from rough handling), the replacement COGS absorb the savings. At $1.50/clip COGS and $24.99 list price, a 2% damage rate on 400 orders equals 8 damaged units = $12 in COGS + $24.99 in refunds/replacements = $37 net loss per month, partially but not fully offsetting savings. At 5% damage, the economics flip against 3PL.

The damage rate for small, rigid FDM parts in a well-run 3PL environment is not publicly documented. PLA clips at ModRun's geometry (compact, low-profile, no thin protrusions) are less fragile than resin prints or prints with antenna-style extensions. Estimated damage rate in padded poly mailers at a competent 3PL: 1-3%. Custom foam inserts reduce this to near-zero but cost more per unit. If pre-packaging includes proper bubble-wrap pouches per the current packaging BOM ($0.04/unit), the 3PL only needs to insert the pre-packaged unit into a shipping box — handling damage during pick/pack should be minimal.

**Monthly minimum exceeds actual usage:** If sales dip below 100 orders/month for any reason (seasonal demand, Etsy algorithm change, listing suspension), Simpl's $750 minimum becomes a pure fixed cost on top of DIY backup costs. ShipMonk's $250 minimum is lower-risk.

**Inbound shipping delays build excess inventory:** If ModRun sends 200 units to the 3PL and demand slows, those units sit in storage. At $5-15/bin/month, the cost is minor. The real cost is capital tied up in pre-packaged inventory that cannot be redirected.

**Exit risk:** ShipMonk has a documented problematic exit process (Trustpilot reviews note continued billing during a 6+ month exit). Negotiate exit terms explicitly: 30-day termination notice, inventory returned within 30 days of termination, data exportable at no charge. Get this in the initial contract.

---

## Section 5: Integration Effort and Operational Complexity

### Setup Timeline

**Simpl Fulfillment:** 1 week to configure. Etsy integration is direct — authorize via OAuth, products sync automatically. Ship an initial inbound batch (ModRun pre-packages 50-100 units). Simpl receives, counts, and bins. First 3PL-fulfilled orders can ship within 10-14 days of starting onboarding.

**ShipMonk:** 1-2 weeks to configure. 75+ platform integrations; Etsy is directly supported. Order sync is real-time. ShipMonk's onboarding team will request SKU catalog, weights, dimensions, and packaging instructions before receiving inbound.

**Fulfillrite (local Maryland option):** 1 week. Smaller team means more direct contact with your account manager. Baltimore-area location means potential for in-person problem resolution, which is valuable when 3D printed product handling needs to be explained. Etsy integration supported. No public pricing — a call or email would establish current rates.

### Operational Overhead After Setup

At steady-state, 3PL reduces ModRun's daily fulfillment burden to:
- Sending inbound batches as inventory depletes (once or twice per week, 15-20 minutes to box, label, and hand to USPS)
- Monitoring 3PL dashboard for order status (5 minutes/day)
- Responding to 3PL alerts for stockouts or discrepancies

The operator's daily fulfillment time drops from ~40 minutes/day (current DIY) to approximately 20-25 minutes/day (pre-packaging inbound + monitoring). The savings are real but modest at low volumes — this is where the scaling benefit manifests at higher order counts.

### Quality Control After 3PL Onboarding

**Non-negotiable:** ModRun must complete all three QC gates before any unit enters the inbound batch destined for the 3PL. The 3PL will not inspect for snap-arm function, bore stringing, or dimensional accuracy. A defective unit shipped to the 3PL will eventually be shipped to a customer.

The QC workflow does not change. What changes is timing: QC happens at production → units go into labeled poly bags → bags accumulate in a staging bin → when staging bin hits 50-100 units, box it and ship to 3PL. The production-time QC rate must stay at 100% visual (Gate 1), 1:20 dimensional (Gate 2), and 1:plate functional (Gate 3) regardless of 3PL use.

### Industry-Standard Damage Rate for 3D Prints in 3PL Environments

No published industry benchmark exists specifically for FDM prints in 3PL pick-and-pack operations. General 3PL damage rates for small consumer goods are typically cited at 0.5-2% for properly packaged items. PLA clips pre-packaged in bubble-wrap pouches and picked by hand (not conveyor belts, which is common in smaller 3PLs) should fall within the 0.5-1.5% range. Resin prints and thin-walled geometries would be higher. ModRun's clips — compact, solid wall geometry, shipped inside a pouch — are near the low end of this range.

If ModRun experiences damage rates above 1.5% after 30 days with a 3PL, the immediate diagnosis is inadequate pre-packaging (insufficient padding) or incorrect handling instructions. The fix is a thicker bubble-wrap pouch or a small rigid box rather than a poly bag. Budget for a packaging trial: test 20 units through the 3PL's pick-pack cycle before committing to a large inbound.

### Failure Mode and Recovery Process

If the 3PL damages a significant batch (e.g., mishandling drops a tray of 50 pre-packaged clips, breaking snap arms inside their bags), the recovery process is:

1. File a claim with the 3PL under their liability clause. Standard 3PL liability for damaged goods is negotiated in the contract — default is often $0.50/unit cap, which is below COGS. Negotiate replacement value liability before signing.
2. Ship emergency replacement inventory from ModRun's own stock (maintain a minimum 50-unit home buffer even after 3PL onboarding).
3. Update Etsy processing time to 7 business days during recovery.

The home inventory buffer is non-negotiable. Never send 100% of finished inventory to a 3PL.

### Exit Strategy

If ModRun needs to leave a 3PL:
- Issue 30-60 day termination notice (negotiate this in the initial contract)
- 3PL ships all remaining inventory back to ModRun within 30 days (typically at ModRun's cost — estimate $25-50 for a small return shipment of 50-200 units)
- Return to DIY operations using the home buffer stock maintained throughout 3PL engagement
- Transition time to full DIY recovery: approximately 3-5 days

The exit is not high-risk at ModRun's inventory volumes. The inventory is lightweight and compact. Retrieval costs are low. The only material risk is the 6+ month billing continuation problem documented in ShipMonk reviews — this is contractual, not operational, and must be addressed in negotiations before signing.

---

## Section 6: Provider Shortlist and Selection Framework

### Feature Parity Evaluation: Which 3PLs Can Handle Bulk Raw Prints?

The direct answer: none of them handle raw unpackaged prints natively. The capability to "handle 3D prints" depends entirely on whether ModRun does the pre-packaging work. With pre-packaging (each clip in a labeled bubble-wrap pouch), any competent 3PL becomes viable. The differentiator is not print expertise — it is contract flexibility, pricing, and Etsy integration quality.

### Recommended Provider Ranking for ModRun

**Tier 1 — Evaluate First:**

**Fulfillrite (Baltimore, Maryland)** — The geographic proximity to ModRun's Maryland location is the primary advantage. In-person visits are possible for initial setup, to demonstrate the product's fragility requirements, and for rapid problem resolution. Fulfillrite specifically serves small ecommerce brands, has Etsy integration, and their $399/month minimum is lower than Simpl's $750 threshold. Customer reviews emphasize that small sellers receive genuine attention. No public pricing requires a direct quote — this is a 30-minute call.

**Simpl Fulfillment** — Best-in-class for true flat-rate simplicity. $7/order all-in including postage eliminates shipping cost variability and simplifies margin modeling. The $750/month minimum is a real barrier below 100 orders/month, but at Month 5+ volumes it is a non-issue. The no-setup-fee and no-receiving-fee policy minimizes onboarding risk. Good choice if Fulfillrite's pricing is not competitive.

**Tier 2 — Consider at Higher Volumes:**

**ShipMonk** — Better choice at 300+ orders/month when volume discounts on pick fees matter. $250/month minimum is lower than Simpl's threshold, making it more accessible for Month 3-4 evaluation. However, the documented exit problems (continued billing, slow transition) represent meaningful downside risk that requires careful contract negotiation. Multi-item orders benefit from ShipMonk's per-item pricing versus Simpl's flat rate.

**Tier 3 — Not Recommended at Current Scale:**

**ShipBob** — $975 setup fee, 400-order minimum, and inconsistent Etsy integration documentation make this a poor fit for ModRun's current trajectory. Re-evaluate at 800+ orders/month.

**Printful** — Wrong category. Not applicable.

**Blendable** — Cannot be verified as an active provider. Do not plan around.

### Geographic Proximity Assessment

For a Maryland-based operation, a Baltimore-area 3PL (Fulfillrite) provides:
- Same-day or next-day delivery to the dense Mid-Atlantic population corridor (DC, Baltimore, Philadelphia, New York)
- In-person access for initial training on product handling requirements
- Carrier proximity to major Northeast postal hubs (faster USPS transit times to zones 1-4 relative to a Midwestern 3PL)

National 3PLs like ShipMonk and Simpl have distributed warehouse networks, which can be an advantage (stock in multiple regions) but adds complexity and minimum inventory levels per location. At ModRun's volume, a single warehouse location is appropriate.

### Integration Simplicity Ranking

1. **Simpl** — 80+ channel direct integrations, Etsy included, no API required
2. **ShipMonk** — 100+ integrations, Etsy included, real-time sync documented
3. **Fulfillrite** — Etsy integration confirmed, smaller team means more hands-on setup support
4. **ShipBob** — Etsy integration uncertain based on conflicting documentation; require written confirmation before committing

---

## Section 7: Recommended Action Plan

### Immediate Actions (Month 1-2, Pre-Launch)

None required. Do not engage a 3PL before accumulating 90 days of order data. Operating at 10-20 units/week, DIY fulfillment is both cheaper and operationally simpler.

**However, do this now:**
- Review this document and confirm understanding of the inbound pre-packaging requirement. Design the home packaging station to include a pre-packaging step (labeled poly bag per unit) that can be added at any point without workflow disruption.
- Create an account at Fulfillrite's website (free) and request pricing via their quote form. This costs nothing and establishes a contact before you need one urgently.
- Optionally, request pricing from Simpl Fulfillment as well. Both quotes will take 1-5 business days and have no commitment.

### Month 3 Checkpoint (35 units/week, ~140 orders/month)

Run the actual cost model with real data:
- Pull actual weekly labor time from the production log
- Calculate actual Pirate Ship shipping costs (blended actuals, not estimates)
- Compare to the 3PL model in this document with current actual order counts

If packaging labor exceeds 90 minutes/day consistently, accelerate the 3PL evaluation. If labor is under 60 minutes/day, extend the DIY window to Month 4.

### Month 4-5 Transition Trigger (45-60 units/week, ~180-240 orders/month)

If the Monthly 3-4 checkpoint signals 3PL is economically justified:
1. Send an initial pilot batch of 50 pre-packaged units to the preferred 3PL (Fulfillrite or Simpl)
2. Route 50% of Etsy orders through 3PL, 50% DIY for 30 days to compare accuracy and damage rates
3. If 3PL damage rate is under 1.5% and order accuracy is 98%+, complete the transition

Keep a 50-unit home buffer throughout. Never route 100% of orders to the 3PL until you have 60 days of clean performance data.

### Contingency Plans

If 3PL transition fails (damage rate too high, integration problems, billing disputes):
1. Return to full DIY immediately using home buffer stock
2. Increase packaging station capacity: add a second Rollo printer ($100), hire a part-time post-processor (10-15 hours/week at $15-18/hr)
3. If demand exceeds single-person DIY capacity, explore coworking space fulfillment (some makerspaces in Maryland offer small-business shared fulfillment areas) or hire a family member for 10 hours/week at peak
4. Re-evaluate 3PL options after a 60-day DIY recovery period with updated provider shortlist

---

## Confidence Assessment and Evidence Gaps

**High confidence:**
- 3PL pricing ranges from industry sources (multiple confirmed, consistent across sources)
- Simpl Fulfillment's $750/month minimum and ~$7/order all-in rate (confirmed from pricing page and multiple review sources)
- ShipMonk's $250/month minimum and $2.50/first-item pick fee (confirmed from multiple comparison sources)
- ShipBob's $975 setup fee and 400-order minimum (confirmed from Simpl's competitor analysis page and multiple reviews)
- The inbound pre-packaging requirement as a universal 3PL constraint (confirmed from industry documentation on receiving fees for non-standard inbound)
- DIY cost model (cross-referenced against production-workflow-v1.md actuals)

**Medium confidence:**
- Fulfillrite's $399/month minimum (sourced from third-party review, not Fulfillrite's own pricing page)
- 3PL damage rate estimate of 0.5-2% for pre-packaged small items (industry benchmark, not FDM-specific)
- Break-even at 300-350 orders/month (model-derived; actual crossover will depend on ModRun's zone mix and real per-order shipping costs)

**Low confidence / gaps:**
- Blendable as a viable 3PL (unverified)
- ShipBob's Etsy integration (conflicting sources; do not plan around it without written confirmation from ShipBob)
- Whether any 3PL will negotiate custom inbound receiving for loose bulk prints (possible but requires direct negotiation; not a documented standard offering)
- Seasonal surcharges at specific providers (Q4 +15-30% is an industry average; actual rates vary by contract)

---

## Sources

- [ShipMonk Pricing Page](https://www.shipmonk.com/pricing)
- [Simpl Fulfillment Pricing](https://www.simplfulfillment.com/pricing)
- [ShipBob vs ShipMonk Comparison — FitSmallBusiness](https://fitsmallbusiness.com/shipbob-vs-shipmonk/)
- [ShipBob Pricing 2026 — Simpl Fulfillment Competitor Analysis](https://www.simplfulfillment.com/breakdowns/shipbob-pricing)
- [3PL Fulfillment Cost Breakdown 2026 — Catalist AI](https://catalistai.com/blog/3pl-fulfillment-cost-breakdown-2026/)
- [Hidden 3PL Fees to Watch for in 2026 — Ware-Pak](https://ware-pak.com/fulfillment/hidden-3pl-fees-to-watch-for-in-2026/)
- [3PL vs In-House Fulfillment Guide 2026 — Digital Applied](https://www.digitalapplied.com/blog/ecommerce-fulfillment-3pl-vs-in-house-guide-2026)
- [3PL Contract Red Flags — ShipDudes](https://shipdudes.com/blog/3pl-contract-red-flags-12-terms-that-will-cost-you-(and-what-to-negotiate-instead))
- [3PL for Etsy Sellers — ShipHero](https://www.shiphero.com/blog/best-3pl-fulfillment-etsy)
- [Shipping 3D Printed Products — AtoShip](https://atoship.com/blog/shipping-3d-printed-products-fragile-custom)
- [Maryland Fulfillment — Badger Fulfillment Group](https://badgerfg.com/maryland-fulfillment/)
- [Fulfillrite Baltimore Review — Fulfillrite](https://www.fulfillrite.com/locations/baltimore-md/)
- [3PL Pricing 2026 — Racklify Comprehensive Guide](https://racklify.com/news/3pl-pricing-2026-most-comprehensive/)
- [Best 3PL for Etsy — ShipHype](https://shiphype.com/3pl-for-etsy/)
- [Simpl Fulfillment Review 2026 — Research.com](https://research.com/software/reviews/simpl-fulfillment-review)

---

*Version 1.0 — May 2026. Review at Month 3 post-launch (estimated August 2026) with actual order volume data.*
