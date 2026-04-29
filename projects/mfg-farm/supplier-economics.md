---
title: ModRun Supplier Economics — Pre-Negotiation Research Package
date: 2026-04-29
status: pre-negotiation-ready
tags: [3d-printing, mfg-farm, supply-chain, filament, supplier-diversification, cogs, modrun]
confidence: high
related: material-sourcing-supplier-economics.md, phase-2-supplier-research.md, supplier-scorecard.csv, material-sourcing-scorecard.csv
scope: preparation only — do not activate supplier commitments until test print completes
---

# ModRun Supplier Economics — Pre-Negotiation Research Package

**Lead finding**: The ModRun business is not a "bureau-first" operation — in-house FDM production on the Bambu P1S delivers per-unit material costs of $0.79–$0.98 for a 75g PLA+ clip, versus $8–$25 per part from service bureaus for an identical geometry. The economic case for keeping production in-house is overwhelming at all projected volume tiers. The supplier research below focuses on three leverage points: (1) raw filament sourcing optimization, (2) domestic vs. Chinese supplier diversification under active tariff risk, and (3) supply chain design that prevents a single-supplier stock-out from halting production.

**Scope note**: `phase-2-supplier-research.md` and `material-sourcing-supplier-economics.md` already contain detailed supplier profiles for eSUN, Anycubic, Polymaker, Overture, and SUNLU, and a full COGS model. This document does not repeat that material. It provides: (1) the service bureau landscape as context for why in-house production is irreplaceable, (2) a deeper tariff and diversification analysis, (3) a safety stock and order cycle framework applied to the ModRun production parameters, and (4) a negotiation leverage map showing where price reductions are most structurally available.

---

## 1. Service Bureau Economics: Why In-House Wins at This Scale

### 1.1 The Bureau Option Exists — but at 10–25x the Cost

Shapeways (pre-bankruptcy 2024, now restructured), Craftcloud, Materialise, JLC3DP, and Slant 3D are the major US-accessible service bureaus for FDM parts. Slant 3D is the most relevant competitor because it operates a large-scale FDM farm targeting product manufacturers — effectively the closest analog to what ModRun is building in-house.

Key public pricing data points from April 2026 research:

| Service | Technology | Published Per-Part Estimate | Notes |
|---|---|---|---|
| Craftcloud (aggregator) | FDM (PLA) | $0.10–$0.30/g + $3–10 setup | 180+ global partners; no MOQ; instant quote |
| JLC3DP | FDM | ~$0.30/piece minimum (small parts) | Rising star; China-based fulfillment; import duties apply |
| Xometry | FDM, SLS, MJF | Mid-range; quote required | Fast turnaround; 12–15% undisclosed post-processing fees noted in testing |
| Slant 3D | FDM (production farm) | $100/standard prototype; quote required for production | Targets high-volume; $3.12/pick-and-pack add-on; warehousing at $0.75/cu ft |
| Materialise (i.materialise) | FDM, SLS, SLA | Material-specific quote only; no published flat rate | Industrial quality; minimum ~$10–15/part realistic for small PLA parts |

**Applied to a ModRun cable clip (75g, ~45 cm³ volume, simple geometry):**

A 75g PLA part at $0.10–$0.30/g = $7.50–$22.50 per part from a service bureau, before shipping. At Craftcloud's minimum $3–10 setup fee, the realistic per-part cost at 1–5 unit quantities is $10–$30. Even at 25-unit batch quantities where bureaus amortize setup over more parts, expect $6–$15 per clip.

In-house cost at $12/kg filament: $0.90 material + $0.13 electricity and depreciation = **$1.03/part before shipping**.

The in-house premium over bureau cost is not marginal — it is a 6x to 23x per-unit cost advantage. Service bureaus are legitimate for prototyping, rush production during equipment failures, or materials you cannot print in-house (SLS nylon, resin). They are not viable as a primary production path for a commoditized, high-volume cable clip product.

**When a bureau makes sense for ModRun:**
- Equipment failure: If the Bambu P1S is down for >3 days and there is a confirmed order backlog, a local service bureau or Craftcloud instant-quote can fulfill emergency orders at a $6–15 margin hit per unit, acceptable for one-time service recovery.
- New material prototyping: Testing SLS nylon (for extreme-heat installations) or resin (for high-detail aesthetic variants) without investing in SLS/resin hardware.
- PETG validation: Before committing to PETG in production, a $20–40 test-part run from a bureau using high-quality PETG can validate the geometry before recalibrating the in-house print profile.

### 1.2 Powder Suppliers (SLS Nylon): Not Relevant at Current Scale

SLS nylon powder printers (Formlabs Fuse 1, EOS, HP Multi Jet Fusion) begin at $18,000–$120,000 for equipment. Nylon PA12 powder runs $80–$120/kg. For cable clips at $8.99–$22.99 retail, SLS production economics require 2,000–5,000 units/month minimum to justify hardware investment. This is a Phase 4+ consideration (>12 months out). Exclude from current planning.

---

## 2. Filament Supplier Economics: Pricing Tiers and Volume Breakpoints

### 2.1 Chinese-Origin Tier (Current Primary: eSUN, Anycubic, SUNLU, Overture)

All four primary recommended suppliers are manufactured in China and US-warehoused (some) or shipped direct from China. Current tariff exposure is already embedded in April 2026 pricing — commodity PLA that was $9–11/kg in 2024 is now $10–14/kg due to accumulated tariff increases.

**Pricing breakpoints (PLA standard 1.75mm, US delivery, April 2026):**

| Volume Breakpoint | eSUN | Anycubic | Overture | SUNLU |
|---|---|---|---|---|
| 1 kg (single spool) | $15–$20 | $12–$16 | $13–$18 | $14–$16 |
| 5 kg (~5 spools) | $13–$17 | $11–$14 | $11–$14 | $12–$14 |
| 10 kg (case/bundle) | **$11–$13** | ~$10.50 | **$11–$14** | $12–$14 |
| 25 kg | ~$9–$12 (eBay wholesale) | ~$10.50 | Quote required | ~$11–$13 (reseller) |
| 50 kg | Quote via esun3dstore.com | **$10.49** (listed) | Quote required | ~$10–$12 (reseller) |
| 100 kg | Quote; est. $8.50–$10 | ~$9–$10 est. | Quote required | ~$9–$11 (reseller) |

**Lead times:**
- Amazon Prime (eSUN 10kg bundle, Overture 10kg bundle): 2–5 business days — this is the fastest path and should be the default for safety stock replenishment.
- Anycubic direct: 3–7 business days from Chinese warehouse; rises to 2–3 weeks during 618 and 11/11 sale events (June and November). Do not rely on Anycubic timing in those months without pre-ordering.
- SUNLU direct: 3–7 business days US warehouse (some inventory); 2–3 weeks China ship for non-US-stocked items.

**Rush premium**: None of these suppliers offer formal rush services. Amazon Prime is de facto rush — 2-day delivery at no filament premium. If stock runs out and Prime is not fast enough, a local FDM service bureau is the only real-time fallback.

### 2.2 US-Domestic Tier (Hedge Suppliers: Push Plastic, IC3D, 3D-Fuel, American Filament)

US-made filament is the tariff hedge — if Chinese goods tariffs increase another 20–30%, domestic suppliers' price premium narrows from the current ~100–150% premium to potentially 40–60%, which approaches justifiable at high production volumes.

**Domestic supplier pricing reality (April 2026):**

| Supplier | Location | PLA $/kg (retail) | Bulk Program | AMS Track Record | Tariff-Safe? |
|---|---|---|---|---|---|
| Push Plastic | Springdale, AR | ~$22–$28 | Yes (custom quote; 25kg spools available) | Good; used in farm context | Yes |
| IC3D | Columbus, OH | ~$24–$30 | Yes (up to 20% savings; quote required) | Adequate; less documented for Bambu | Yes |
| 3D-Fuel | Fargo, ND | ~$32–$40 | Yes (wholesale; $39.90/kg standard) | Limited farm data | Yes |
| American Filament | (US-made) | ~$31–$37 | Limited; no published bulk tier | Limited data | Yes |
| Polar Filament | (US-made) | ~$28–$32 | Limited | Positive reviews | Yes |

*Source: 3DPrint.com US Filament Review, April 2026; Push Plastic website; 3D-Fuel wholesale page.*

**Premium at current pricing**: A move to Push Plastic at $25/kg vs. eSUN at $12/kg costs $0.98 more per 75g unit — effectively doubling material cost on the clip. At the current 18% material share of COGS, this would compress margin from ~61% (bundle order) to ~55%. Survivable, but not the right move unless tariffs actually force it.

**When to activate domestic tier**: If Chinese filament tariffs increase by 15+ percentage points in a single action, recalculate the domestic break-even at that moment. The domestic premium shrinks to approximately $0.40–$0.60/unit at that threshold — still margin-positive at current pricing, and worth the supply chain security.

### 2.3 PETG Pricing Breakpoints

PETG for the Standard/Premium ModRun SKUs commands a higher per-kg price due to material complexity. Key PETG pricing data:

| Supplier | 1 kg | 10 kg | Bulk/Wholesale | AMS Reliability |
|---|---|---|---|---|
| Overture PETG (Amazon) | $17–$19 | ~$15–$17 | Quote (35% off program) | Excellent (best-in-class per ADP 2026) |
| eSUN PETG (Amazon) | $18–$22 | ~$15–$18 | Quote | Good |
| Polymaker PETG (wholesale) | ~$22 retail | ~$15.99 | From $15.99/kg wholesale | Excellent |
| SUNLU PETG | $15–$18 | ~$13–$16 | Reseller tier | Adequate |
| Hatchbox PETG (Amazon) | $16–$20 | ~$14–$17 | Limited bulk | Good |

**PETG cost per 75g unit at $16/kg: $1.20** — versus $0.90 for PLA+. The $0.30/unit premium is fully absorbed by the $2–4 retail price premium on the PETG SKU, confirming the "PETG Premium" tier justification.

---

## 3. Supply Chain Optimization: Inventory, Safety Stock, and Order Cycles

### 3.1 Safety Stock Calculation Applied to ModRun Parameters

The standard safety stock formula:

**Safety Stock = Z × σ_LT × √LT**

Where: Z = service level factor (1.65 for 95%, 1.28 for 90%), σ_LT = standard deviation of daily demand during lead time, LT = lead time in days.

**Simplified reorder-point formula for ModRun:**

Reorder Point (ROP) = (Average Daily Consumption × Lead Time) + Safety Stock

**Applied parameters (Month 2 production, 50 units/day print capacity on 1 printer):**

- Average daily filament consumption at 50 units/day × 75g = 3.75 kg/day
- Lead time (Amazon Prime): 3 days (conservative; Prime is usually 2 days)
- Lead time (Anycubic direct): 7 days
- Demand variability: assume ±30% swing (order demand fluctuates; build ahead of order volume)
- Safety stock target: 14 days of consumption buffer

**Calculated values:**

| Scenario | Daily Use | Lead Time | Safety Stock (14 days) | ROP |
|---|---|---|---|---|
| Month 1 (10 units/day) | 0.75 kg/day | 3 days (Prime) | 10.5 kg | 12.75 kg |
| Month 2 (30 units/day) | 2.25 kg/day | 3 days (Prime) | 31.5 kg | 38.25 kg |
| Month 3 (80 units/day) | 6 kg/day | 3 days (Prime) | 84 kg | 102 kg |
| Month 4 (150 units/day) | 11.25 kg/day | 7 days (Anycubic) | 157.5 kg | 236 kg |

**Practical interpretation**: At Month 2 (30 units/day), reorder when filament on-hand drops below ~38 kg. Keep ~32 kg as safety stock. For context, a 10kg eSUN case serves about 4.4 days of production at that rate — you need roughly 4 cases in safety stock at Month 2, which is manageable in 2–3 cubic feet of storage.

### 3.2 Order Cycle Optimization

**The optimal order cycle is not the shortest possible — it is the cycle that minimizes the sum of ordering costs and holding costs.**

For filament at current scale:

- Ordering cost: ~$0 incremental for Amazon Prime (no shipping, no order minimum, no account overhead). Ordering cost grows to $30–50/hour of operator time for wholesale negotiations.
- Holding cost: Filament has low spoilage risk when stored properly (1–3 year shelf life for PLA; 2–4 years for PETG under 30% RH and 15–25°C). Carrying cost is primarily capital tied up in inventory: at $12/kg, 50 kg = $600. At a 20% opportunity cost of capital, monthly holding cost on 50 kg inventory is $10. Negligible.

**Order cycle recommendation by phase:**

| Phase | Monthly Consumption | Order Frequency | Order Size | Rationale |
|---|---|---|---|---|
| Month 1 (launch) | <10 kg | As needed | 10 kg (1 case, Amazon) | Preserve cash; Prime = instant safety net |
| Month 2 | 10–25 kg | Every 2 weeks | 10–15 kg | Maintain 2-week buffer; free Prime shipping |
| Month 3 | 25–60 kg | Monthly | 30–50 kg | Switch to Anycubic 50kg pallet for primary color |
| Month 4–6 | 60–150 kg | Monthly + safety net | Primary: Anycubic/Polymaker bulk; safety: Amazon Prime 10kg reserve | Two-tier structure: bulk order + emergency reserve |

### 3.3 Storage Infrastructure by Phase

| Monthly Consumption | Filament Inventory Target | Storage Requirement | Equipment |
|---|---|---|---|
| <10 kg | 5–10 kg | <0.5 cu ft | Sealed bin + desiccant packs |
| 10–25 kg | 15–25 kg | 1–2 cu ft | Dry storage totes (airtight); RH < 30% target |
| 25–60 kg | 40–65 kg | 3–5 cu ft | Humidity-controlled dry cabinet ($80–200) or sealed storage rack |
| 60–150 kg | 80–175 kg | 6–12 cu ft | Dedicated storage room; digital hygrometer; silica gel rotation |

**Key material science parameters for storage**:
- PLA and PLA+: shelf life 1–3 years at 15–25°C, <30% RH
- PETG: shelf life 2–4 years at same conditions
- Moisture is the primary degradation vector — absorbed moisture causes extruder bubbling, diameter swelling, and layer adhesion failures
- Open spools exposed to ambient air in a typical home (40–60% RH) degrade within 2–6 weeks in humid climates
- Invest in active dry boxes (Sunlu, Creality) at the $25–50 price point for any open spool that will be on the printer for more than 48 hours

---

## 4. Cost Sensitivity Analysis: Where Supplier Negotiation Has the Highest Impact

### 4.1 COGS Waterfall — What Each Variable Controls

Full COGS model for a 3-clip bundle at $28.99 retail (the highest-volume expected SKU based on market research):

| Cost Component | Amount | % of COGS | Supplier Dependency | Negotiation Potential |
|---|---|---|---|---|
| Filament (3 × 75g at $12/kg) | $2.70 | 32.0% | eSUN, Anycubic, Polymaker | HIGH — 20–35% reduction possible |
| Electricity ($0.025/hr × 3 × 45 min) | $0.06 | 0.7% | Utility — fixed | NONE |
| Printer depreciation (3 × $0.11/hr) | $0.33 | 3.9% | Fixed amortized cost | NONE |
| Print failure waste (7% buffer) | $0.21 | 2.5% | Filament quality-dependent | MEDIUM — better quality = less waste |
| Packaging (poly mailer) | $0.05 | 0.6% | Shop4Mailers, Amazon bulk | LOW — already at floor; $0.05 is market price |
| Shipping (USPS Ground Advantage, 3-pack) | $5.00 | 59.2% | Pirate Ship / USPS | LOW-MEDIUM — commercial rate already captured |
| **Total COGS** | **$8.44** | **100%** | | |

**Critical insight**: Shipping is 59% of bundle COGS. Filament is 32%. All other factors are 9% combined. The two levers that matter are (1) filament cost optimization and (2) average order value (AOV) — which amortizes the fixed $5 shipping cost across more units.

### 4.2 Margin Impact of Filament Price Reduction

On a 3-clip bundle at $28.99 retail (net $26.10 after Etsy fees):

| Filament Scenario | $/kg | Material Cost (3 × 75g) | COGS | Gross Margin | Margin Delta |
|---|---|---|---|---|---|
| Current retail (retail spool) | $15.00 | $3.38 | $9.12 | 65.1% | baseline |
| eSUN 10kg bundle (Amazon) | $12.00 | $2.70 | $8.44 | 67.7% | +2.6 pts |
| Anycubic 50kg pallet | $10.49 | $2.36 | $8.10 | 69.0% | +3.9 pts |
| eSUN direct wholesale ($9.50/kg) | $9.50 | $2.14 | $7.88 | 69.8% | +4.7 pts |
| Polymaker wholesale ($14.99/kg) | $14.99 | $3.37 | $9.11 | 65.1% | +0 pts vs. retail |

**Takeaway**: Moving from retail spools to Anycubic pallet pricing improves bundle margin by 3.9 percentage points — worth approximately $1.02 per order at $28.99 ASP. At 500 bundles/month, that is $510/month in retained margin from filament optimization alone. At 2,000 bundles/month, it is $2,040/month. This is the highest-impact, most accessible supplier lever.

### 4.3 Negotiation Leverage Map

Where negotiation produces the most structural return, ranked by impact:

**Tier 1 — High Impact, Achievable**
1. **Anycubic 50kg pallet** ($10.49/kg, no negotiation needed — it's listed): $0.34/unit savings vs. $12/kg; available immediately without relationship. Place one test order in Month 1 to validate quality.
2. **eSUN direct wholesale at 20kg+/month**: Contact esun3dstore.com with monthly volume projection. At 20+ kg/month, $10–10.50/kg is achievable. Potential $0.12–$0.15/unit additional savings over Anycubic pallet pricing.

**Tier 2 — Medium Impact, Requires Volume Milestone**
3. **Polymaker Net-30 terms at $1,000+/order**: The per-unit savings vs. eSUN are minimal (+$2.99/kg), but Net-30 terms improve cash flow by $1,000–$3,000/month at that order size. Cash flow impact outweighs per-unit savings at Phase 3 volumes.
4. **Overture PETG wholesale (35% off program)**: Reduces PETG cost from $17–$19/kg to ~$11–$12/kg, improving PETG SKU margin by $0.38–$0.53 per unit. Only relevant once PETG SKU is confirmed at >50 units/month.

**Tier 3 — Low Impact at Current Scale**
5. **Packaging volume discounts**: Poly mailer unit cost is already at market floor ($0.05 at 1,000+). Custom-printed mailers from RUSPEPA at $0.12–$0.20/unit vs. plain at $0.05 is a margin cost, not a savings opportunity.
6. **Shipping rate negotiation**: Pirate Ship commercial rates already capture the best available USPS pricing. No further negotiation possible until volume justifies a UPS/FedEx contract (typically 50+ parcels/day).

---

## 5. Supplier Diversification Strategy

### 5.1 Single-Source vs. Multi-Source: The Risk Mathematics

A single-supplier model (eSUN only via Amazon) creates the following failure modes:

| Risk Event | Probability | Impact | Recovery Time |
|---|---|---|---|
| Amazon stock-out on 10kg bundle | Medium (2–4x/year per color) | 1–5 days lost production | 3–7 days (pivot to Anycubic or local store) |
| eSUN price increase >15% | Low-medium (tariff-driven) | Permanent margin compression | Weeks to qualify replacement |
| Shipping delay (weather, carrier disruption) | Low | 1–3 days disruption | None if safety stock held |
| Filament quality batch failure | Low | 2–5% reject rate spike | Same-day (detect via QA; swap spool) |
| Chinese tariff escalation 20%+ | Low-medium | $0.19–$0.30/unit COGS increase | 2–8 weeks to qualify domestic alternative |

The recommended multi-source structure, and when each tier activates:

**Tier A — Primary (Day 1)**: eSUN PLA+ via Amazon 10kg bundles. Best AMS compatibility, Prime availability as fallback. No wholesale account needed.

**Tier B — Secondary (Month 1)**: Anycubic direct store, 50kg pallet. Pre-qualify with one test order before depending on it. Covers the main risk: Amazon eSUN stock-out. Cost advantage of $1.50–$2.50/kg makes it financially beneficial, not just a hedge.

**Tier C — Quality-Tier Primary (Month 3–4)**: Polymaker wholesale for white and grey (visible on product; quality consistency matters). eSUN and Anycubic remain primary for black and secondary colors where per-kg cost dominates.

**Tier D — Emergency Domestic (Activate on tariff trigger)**: Push Plastic or IC3D. Contact both now with a "potential future volume interest" inquiry to establish relationships before you need them under pressure. Push Plastic's 25kg spool format is particularly useful for a farm context.

### 5.2 The Tariff Sensitivity Floor

Current tariff environment (April 2026): Chinese goods at 125–145% tariff baseline (some categories). This is already embedded in prices. The risk is further escalation.

**If Chinese filament tariffs increase by 20 additional percentage points**:
- Expected commodity PLA impact: +$2–$3/kg (from $10–$12 to $12–$15)
- Expected per-unit impact (75g clip): +$0.15–$0.23
- Impact on 3-clip bundle margin: −1.0–1.6 percentage points
- Domestic supplier (Push Plastic ~$22–$28/kg) becomes competitive only if Chinese prices reach $18+/kg

**If Chinese filament tariffs increase by 40+ additional percentage points** (escalation scenario):
- Chinese PLA could reach $16–$20/kg
- Push Plastic at $22–$28/kg is now only 10–40% more expensive
- A blended strategy (80% domestic, 20% Chinese specialty colors) becomes viable
- Activate Tier D relationships immediately if this scenario materializes

**Monitoring tripwires**: Set up Google Alerts for "filament tariff" and "Section 301 tariffs 3D printing." A tariff action typically provides 30–60 days from announcement to implementation — enough time to place a large forward-buy order at pre-increase pricing if you have the cash and storage.

### 5.3 Backup Supplier Pre-Qualification Protocol

Before you need them, you should have placed at least one test order with every Tier A and Tier B supplier. The pre-qualification checklist:

For each candidate supplier:
- [ ] Place a 1–2 kg test order (or 5kg if no smaller option) in your highest-velocity color (black)
- [ ] Print the exact ModRun clip file from the test order material on your production printer
- [ ] Run the AMS feed for a minimum 3-hour continuous job
- [ ] Measure 5 clips with calipers; record diameter, engagement width, rail fit
- [ ] Note lead time from order to doorstep (log the actual date)
- [ ] Note packaging quality (vacuum sealed vs. open bag — relevant for moisture storage planning)
- [ ] Score on the 155-point supplier evaluation framework in `material-sourcing-supplier-economics.md`

Pre-qualify Anycubic (Tier B) in Month 1, before you need it. You do not want to discover Anycubic's AMS winding issues on a 50kg pallet when you have a backlog of 200 unfulfilled orders.

### 5.4 Supplier Relationship Development Timeline

| Month | Action | Goal |
|---|---|---|
| Pre-launch | Verify eSUN Amazon ASIN pricing; verify Anycubic 50kg pallet pricing | Confirm inputs to COGS model |
| Month 1 | Place Anycubic 5–10kg test order; email Push Plastic and IC3D with interest inquiry (no commitment) | Pre-qualify Tier B; open Tier D contacts |
| Month 2 | Email eSUN direct (esun3dstore.com) with volume projection — "20+ kg/month, interested in direct wholesale pricing" | Begin Tier A negotiation |
| Month 3 | If eSUN direct pricing achieves <$11/kg, transition primary black/white orders there; if not, stay on Amazon bundles | Lock in direct pricing if available |
| Month 3–4 | Register at us-wholesale.polymaker.com; place first $1,000 order in white PLA | Activate Tier C for visible-color quality |
| Month 4 | Contact Overture wholesale team (overture3d.com/pages/wholesale) to lock in PETG pricing | Activate Tier C for PETG SKU |
| Month 6+ | Apply for Net-30 payment terms with Polymaker (after 2–3 orders); apply with eSUN direct if active | Improve cash flow; reduce per-order capital requirement |

---

## 6. Unit Economics Summary: ModRun Lead Product at Scale

### 6.1 Worked Example — 3-Clip Bundle at Production-Optimized COGS

This is the target COGS structure after Month 3 supplier optimization, for the 3-clip bundle (the highest-margin SKU):

| Component | Optimized (Month 3+) | Pre-Optimization Baseline |
|---|---|---|
| Filament (3 × 75g at $10.49/kg) | $2.36 | $3.38 (retail) |
| Electricity + depreciation | $0.39 | $0.39 |
| Failure waste (5% at optimized) | $0.14 | $0.21 |
| Packaging (poly mailer, 9x12") | $0.05 | $0.08 |
| Shipping (USPS Ground Advantage) | $5.00 | $5.50 |
| **Total COGS** | **$7.94** | **$9.56** |
| Retail price | $28.99 | $28.99 |
| Net after Etsy 6.5% + $0.20 fee | $26.10 | $26.10 |
| **Gross Margin** | **69.6%** | **63.4%** |

Optimization improves gross margin on the 3-clip bundle by 6.2 percentage points. At 1,000 bundles/month, that is $1,620/month in additional retained earnings. At 3,000 bundles/month, it is $4,860/month.

### 6.2 The AOV Lever Dwarfs All Supplier Optimization

At any volume tier, the most powerful margin improvement available is not supplier negotiation but average order value (AOV). Because the $5.00 shipping cost is fixed regardless of how many clips are in the order:

| Order Size | Units | Retail | Shipping (fixed) | Material | Gross Margin |
|---|---|---|---|---|---|
| Single clip | 1 | $8.99 | $4.50 | $0.90 | ~38% |
| 3-clip bundle | 3 | $28.99 | $5.00 | $2.70 | ~67% |
| 6-clip kit | 6 | $45.99 | $5.50 | $5.40 | ~70% |
| Deluxe system (clips + rail) | ~8 items | $69.99 | $7.00 | ~$7.20 | ~71% |

Moving a customer from a single-clip purchase to a 3-clip bundle improves gross margin from ~38% to ~67% — a 29-point improvement with zero supplier change. This is why the bundle strategy and kit SKUs in the pricing strategy documents are not just revenue tools; they are the primary margin mechanism.

---

## 7. Confidence Notes and Gaps

**High confidence (live data, April 2026)**:
- eSUN Amazon 10kg bundle pricing ($11–$13/kg)
- Anycubic 50kg pallet pricing ($10.49/kg, verified on store page)
- Service bureau FDM pricing range ($0.10–$0.30/g, $7.50–$22.50 for a 75g part)
- USPS temporary 8% surcharge (April 26, 2026 – January 17, 2027) already in Pirate Ship rates
- US domestic filament supplier pricing tiers (3DPrint.com April 2026 testing): Polar ~$32/kg, 3DxTech ~$36/kg, 3D-Fuel ~$40/kg

**Medium confidence (corroborated but not directly verified)**:
- Overture PETG at $15–$17/kg at 10kg quantity — based on Amazon pricing data; wholesale tier requires direct contact
- Polymaker PETG wholesale from $15.99/kg — public landing page listing; logged-in account required for full catalog
- Anycubic 100kg pricing (~$9–$10/kg) — extrapolated from 50kg public rate; not verified with a direct quote
- Tariff impact range on Chinese filament (prior increases already embedded; further escalation scenarios are projections)

**Gaps requiring direct verification**:
- eSUN direct wholesale pricing at 20kg+/month commitment (requires email inquiry to esun3dstore.com)
- IC3D specific bulk pricing (website cites "up to 20% savings" but no public rate card)
- Push Plastic bulk pricing matrix (requires submission of their Bulk Pricing Application Form)
- Overture wholesale tier pricing for PETG at 10kg+ volumes
- Priority Mail Cubic exact rates for ModRun's specific box dimensions — run the Pirate Ship rate calculator with test addresses

---

## Sources

- [Slant 3D Basic Pricing](https://www.slant3d.com/basic-pricing)
- [Building Your Own 3D Printer Farm vs. Using a Service — Slant 3D](https://www.slant3d.com/slant3d-blog/building-your-own-3d-printer-farm-vs-using-a-service)
- [Craftcloud — Understanding Prices](https://support.craftcloud3d.com/en/articles/24-understanding-prices-on-craftcloud)
- [Craftcloud 3D Printing Services](https://craftcloud3d.com/en/p/3d-printing-services)
- [JLC3DP Online 3D Printing Instant Quote](https://jlc3dp.com/3d-printing-quote)
- [JLC3DP How Much Does 3D Printing Cost](https://jlc3dp.com/blog/3d-printing-cost)
- [Xometry 3D Printing Cost Calculator](https://www.xometry.com/resources/3d-printing/3d-printing-cost-calculator/)
- [Materialise Online 3D Printing Service](https://www.materialise.com/en/industrial/3d-printing-services/online-3d-printing)
- [Shapeways Pricing Overview](https://www.shapeways.com/support/pricing)
- [3DPrint.com — Filaments From the USA: Solutions Amidst the Tariffs](https://3dprint.com/317466/filaments-from-the-usa-solutions-from-usa-manufacturers-amidst-the-tariffs/)
- [3DPrint.com — 2026: The Year of the Low Cost Print Farm](https://3dprint.com/322953/2026-the-year-of-the-low-cost-print-farm/)
- [3DPrint.com — Finding Solutions in an Uncertain Market: Trade Tariffs on Filament Supply](https://3dprint.com/315065/finding-solutions-in-an-uncertain-market-the-impact-of-reduced-material-providers-and-trade-tariffs-on-filament-supply/)
- [Push Plastic — Bulk Pricing](https://www.pushplastic.com/pages/bulk-pricing)
- [Push Plastic — Bulk Filament Made in USA](https://www.pushplastic.com/collections/bulk)
- [IC3D — Bulk 3D Printing Filament](https://www.ic3dprinters.com/bulk-3d-printing-filament/)
- [3D-Fuel — Wholesale 3D Printer Filament](https://www.3dfuel.com/pages/wholesale-3d-printer-filament)
- [SpoolPrices — 3D Printer Filament Price Comparison 2026](https://spoolprices.com/filament)
- [3DFilamentPrice — PETG vs PLA Ultimate 2026 Comparison](https://www.3dfilamentprice.com/blog/pla-vs-petg)
- [eufymake — How Much Do 3D Prints Cost 2026](https://www.eufymake.com/blogs/buying-guides/how-much-do-3d-prints-cost)
- [Anycubic Bulk PLA 50–100kg Deals](https://store.anycubic.com/products/pla-basic-50-100kg-deals)
- [Polymaker US Wholesale](https://us-wholesale.polymaker.com/)
- [Overture 3D Wholesale Program](https://overture3d.com/pages/wholesale)
- [Pirate Ship — April 2026 USPS Time-Limited Price Change](https://support.pirateship.com/en/articles/14491291-april-2026-usps-time-limited-price-change)
- [Craftybase — How to Calculate Reorder Point](https://craftybase.com/blog/how-to-calculate-reorder-point)
- [InfoFlow Inventory — Reorder Point Formula and Safety Stock](https://www.inflowinventory.com/blog/reorder-point-formula-safety-stock/)
- [MarketsandMarkets — Trump Tariffs Impact on 3D Printing Market](https://www.marketsandmarkets.com/ResearchInsight/trump-tariffs-impact-3d-printing-market-analysis.asp)
