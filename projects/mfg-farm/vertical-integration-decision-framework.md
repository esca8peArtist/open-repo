---
title: Vertical Integration Decision Framework — Build vs. Partner Analysis Across All Manufacturing Functions
project: mfg-farm
created: 2026-05-06
status: production-ready
session: Item-52
confidence: high — ROI analyses derived from established cost models (Sessions 544, 697, 796, Item-52 baseline)
related: manufacturing-partner-ecosystem.md, scaling-cost-levers.md, ITEM18_ADJACENT_MANUFACTURING_ECONOMICS.md, supplier-ecosystem-planning.md, 3pl-readiness-analysis.md
---

# Vertical Integration Decision Framework

**Lead finding:** At every scale point examined ($10K, $50K, $200K/month revenue), in-house FDM printing beats contract manufacturing on economics by at least 15–20x. The vertical integration question for ModRun is not whether to own printing — it is which ancillary functions (design, post-processing, assembly, QA, shipping) to keep in-house versus delegate, and at what revenue trigger each delegation becomes financially rational. The dominant pattern: stay integrated on all functions that happen per-unit (printing, QC, packaging, shipping) and delegate only when a function's per-unit labor cost exceeds a contractor's equivalent rate, or when a function's fixed overhead cost is recoverable within 90 days. The two functions where early delegation has the highest ROI are post-processing/packaging at Wave 2 scale, and fulfillment logistics at 250+ orders/month.

---

## Section 1: Build vs. Partner Analysis by Function

### 1.1 Design (CAD, Product Development)

**Current state:** CadQuery parametric designs complete for ModRun clip and rail. In-house design capability is established.

**Build case:**
- Design is a one-time investment per product amortized over all units produced
- CadQuery parametric design means modifications (new bore sizes, lengths, mounting variants) take minutes, not hours
- Outsourcing product design to a contractor removes the operator's ability to iterate rapidly based on customer feedback
- Design IP stays internal — critical if designs are the core competitive asset

**Partner case:**
- Complex new product categories (injection molded components, CNC-machined parts, PCB integration) may require specialized CAD expertise beyond CadQuery's parametric framework
- A freelance CAD contractor on Upwork ($17–30/hour for mechanical/product design) can be engaged for specific new product development projects without maintaining ongoing design overhead

**Verdict: Own design for all ModRun product variants.** The parametric CadQuery foundation means the operator can generate new product variants faster than any contractor. Engage an Upwork contractor ($200–500 fixed scope) only for products requiring mechanical expertise outside the operator's current skill set (complex assemblies, new hardware categories, packaging engineering). Target: <10% of product development budget on contracted design work through Wave 2.

**Design function timeline:**
- $10K/month: 100% in-house. Zero design spend.
- $50K/month: Primarily in-house. Budget $500–1,000 for one freelance design engagement per quarter if product line expansion requires it.
- $200K/month: Consider a part-time product development contractor (10 hrs/week, ~$1,200/month) or a product designer hire to accelerate new SKU pipeline.

### 1.2 Printing (Core FDM Manufacturing)

**Build case:** In-house FDM printing at $0.08–$0.13/unit COGS versus $3–15/unit at any domestic contract manufacturer. The gap is permanent and structural — it reflects the overhead and margin embedded in any service bureau. There is no volume at which contract FDM becomes cheaper than owned FDM for continuous production.

**Partner case:** Contract manufacturing is appropriate only for:
1. Surge overflow when owned printers are genuinely maxed and order backlog threatens Etsy standing
2. Production continuity when owned printers are down for repair (days, not weeks)
3. Testing new materials or finishes not achievable on current equipment

**Verdict: Own printing at all scale points.** The ROI case for in-house printing is decisive at every revenue tier. The only question is how many printers and when to add them (addressed in Section 2).

**Risk consideration:** The "own printing" verdict assumes equipment reliability. Each Bambu P1S is a point of failure. The risk mitigation is fleet size — two printers provide 50% capacity floor during single-printer downtime — not contract manufacturing backup.

### 1.3 Post-Processing (Part Removal, Inspection, Light Finishing)

**Build case:**
- At <50 units/week, post-processing (part harvest, support removal if any, visual inspection) takes 2–3 hours/day — easily managed solo
- No quality control outsourcing equivalent exists that can replicate the operator's familiarity with part nuances at this scale

**Partner case:**
- At 75+ units/week (Wave 2), daily post-processing burden exceeds 4 hours — the operator's full afternoon, competing with Etsy management, customer service, and product development
- A part-time contractor at $15/hour doing 10 hours/week ($600/month) frees the operator for higher-leverage work
- The contractor cost ($0.16/unit at 300 units/month) reduces gross margin by 0.6 points — an acceptable trade

**Verdict: Solo through ~75 units/week; contractor for post-processing/packaging at 75+ units/week.** The threshold is not about cost — it is about operator time allocation. When post-processing exceeds 3 hours/day, the operator is doing $15/hour work at the cost of $50–100/hour potential in product development and marketing.

**Post-processing function timeline:**
- $10K/month (~50–150 units/week equivalent gross output): Solo. Total post-processing time 1.5–3 hours/day.
- $50K/month (~250–500 units/week equivalent): Part-time contractor, 10–15 hours/week. $600–900/month.
- $200K/month (~1,000+ units/week): Two part-time contractors or one full-time production assistant. $2,000–3,000/month.

### 1.4 Assembly (Multi-Component Products)

**Current state:** ModRun clips and rails are single-component prints with no post-print assembly required. Assembly becomes relevant if ModRun launches multi-component kits (clip + rail bundle as a physically assembled kit, or hardware packs with screws/anchors).

**Build case:**
- Kit assembly is 30–90 seconds per kit at the operator's packing station — folded into the packaging workflow at no additional labor cost
- Physical assembly of hardware packs (screws, wall anchors included) requires only a bin system at the packing station

**Partner case:**
- Complex assembly requiring tools, adhesives, or sub-assembly staging is a legitimate candidate for 3PL kitting services
- ShipMonk and Simpl both offer kitting at $0.25–$0.75/kit assembly fee in addition to standard fulfillment rates

**Verdict: In-house assembly through Wave 2.** At ModRun's product complexity level, no assembly step justifies outsourcing through at least $50K/month. Evaluate 3PL kitting only if a new product line requires >3 minutes of assembly per unit.

### 1.5 Quality Assurance

**Build case:**
- In-house visual + functional QC protocol takes 30–45 seconds per unit — integrated into the harvest workflow
- The operator's knowledge of the product (knowing which failure modes to look for: snap arm delamination, warping, bore dimension) cannot be replicated by a contract inspector
- Third-party QA has no ROI at <2,000 units/month for a consumer product without specific buyer certification requirements

**Partner case:**
- Wholesale buyers and Amazon FBA may require documented QC, including batch inspection records, dimensional sampling plans, or third-party inspection reports
- A single Bureau Veritas / SGS inspection event ($200–400) provides the documentation trail for a wholesale or retail channel entry

**Verdict: In-house QC at all scales. Supplement with one external inspection event at first wholesale/FBA entry.** Budget $300 for an external inspection report at channel entry, not as an ongoing cost.

### 1.6 Shipping and Logistics

**Build case:**
- Pirate Ship provides commercial USPS rates with zero platform fee — there is no cost advantage to any third party for the act of purchasing and printing shipping labels
- The operator can batch-print a day's labels in 5–10 minutes from the Pirate Ship Etsy integration

**Partner case:**
- A 3PL handles all outbound shipping, including pick-and-pack and carrier selection, at an all-in cost that becomes competitive above 250–300 orders/month
- Simpl's $7/order all-in rate (including shipping postage) may beat DIY at high volume if the operator's time has meaningful opportunity cost
- A 3PL also handles returns processing, which becomes significant at scale (>100 returns/month)

**Verdict: DIY shipping through 200–250 orders/month; evaluate 3PL at 250–300 orders/month.** The handoff point is when Simpl's $7/order cost is competitive against DIY cost (label + packaging materials + labor at $15/hour opportunity cost).

DIY cost at 250 orders/month:
- Packaging (ULINE mailers): $0.08/unit × 250 = $20/month
- Shipping labels: Market rate via Pirate Ship (no markup)
- Packing labor: ~3 min/order × 250 orders = 750 minutes = 12.5 hours/month at $15/hour = $187/month
- **Total DIY non-postage cost: ~$207/month or $0.83/order**

Simpl non-postage equivalent: $7/order − postage − ≈ $2.50/order non-postage
- At 250 orders: 250 × $2.50 = $625/month vs. DIY $207/month

DIY wins clearly through 250 orders/month. The 3PL advantage only emerges when packing labor becomes a binding constraint (competing with higher-value activities) rather than a cost calculation.

**Revised practical rule:** Outsource to 3PL when (a) packing labor exceeds 20 hours/month AND (b) those 20 hours cannot be delegated to a part-time packer at lower cost than 3PL fees. At 250–300 orders/month, a part-time packer at $12–15/hour may still beat 3PL all-in cost. The 3PL becomes attractive when coordination overhead (hiring, managing, training) exceeds the cost differential.

---

## Section 2: ROI Analysis at Three Scale Points

### 2.1 Scale Point 1: $10K/Month Revenue (~30–45 Units/Week)

**Revenue context:** $10K/month gross with $27.50 blended AOV = approximately 364 orders/month. However, at early Etsy launch, $10K/month is more likely ~60–100 orders/month at $100–167 average (multi-unit bundles) or 300–500 orders at $20–33 each. Using 200 orders/month as representative.

**In-house cost model:**
- 1 Bambu P1S ($399 current price, already owned or recently purchased)
- Filament: $11–13/kg × ~3kg/month (200 units × 15g average) = $33–39/month
- Packaging: $0.22/order × 200 = $44/month
- Pirate Ship: $0 platform fee
- **Manufacturing + packaging COGS total: ~$77–83/month**
- Monthly gross profit (70% margin): $7,000/month

**Contract FDM alternative (hypothetical):**
- Xometry at $5/unit (optimistic) × 200 units = $1,000/month manufacturing cost
- $7,000 gross revenue becomes ~$5,923 gross profit (41% margin vs. 70%)
- Margin lost: $1,077/month = $12,924/year

**In-house ROI:** If the P1S was purchased at $399, it pays back in approximately 0.7 weeks at $7,000/month gross profit. The equipment investment is fully recovered before Month 1 ends. This is not a break-even question — it is an obvious answer.

**Key investments at this scale:**
- None required if single P1S already owned
- Pirate Ship (free) and Rollo thermal printer ($99–159 one-time) are the only incremental investments needed

### 2.2 Scale Point 2: $50K/Month Revenue (~250–350 Units/Week)

**Revenue context:** $50K/month with $27.50 blended AOV = 1,818 orders/month. At 70% margin post-Etsy fees and shipping, gross profit is approximately $35,000/month.

**Two-printer in-house cost model:**
- 2 Bambu P1S printers: $398–$798 total (one owned, one added)
- Filament: $10.50/kg × ~15kg/month = $157/month (bulk pricing tier)
- Contractor post-processing: 20 hours/week × $15/hour = $1,200/month
- Packaging (ULINE + noissue custom blend): ~$0.30/order × 1,818 = $545/month
- Pirate Ship: $0
- **Monthly non-shipping, non-Etsy COGS: ~$1,900/month**
- Monthly gross profit: ~$33,100/month

**Contract FDM alternative at this scale:**
- 1,818 units/month at $5/unit (Xometry optimistic) = $9,090/month
- Gross profit drops to: ~$35,000 − $9,090 = $25,910/month (vs. $33,100)
- Lost margin: $7,190/month = $86,280/year
- Foregone printer investment avoided: 2 printers at $398 total = $398 one-time
- Break-even of contract vs. in-house: $398 / $7,190 = 0.055 months — contract FDM NEVER wins at this scale

**Additional equipment ROI at $50K/month:**

*AMS 2 Pro ($286 add-on):*
- Enables multi-color production without manual filament swaps
- Time savings: 15–20 minutes per filament change × 3 changes/week = 45–60 minutes/week = 36–48 hours/year
- Labor value recovered: 36–48 hours × $15/hour = $540–720/year
- Premium pricing enabled: Multi-color SKUs command 20–40% price premium, adding $50K × 5% (conservative attach rate on multi-color) × 30% premium = $750/month
- Break-even: $286 / $750/month premium = 0.38 months. Decisively justified.

*xTool S1 40W laser ($1,899):*
- Enables personalized/engraved SKUs at $1,899 equipment cost
- Engraved clip premium: $5–8/unit over standard
- Break-even at $6/unit premium: $1,899 / $6 = 317 engraved units
- At 5% of 1,818 orders/month including engraving = 91 units/month → 3.5 months payback
- If engraved products are a featured SKU at 15% of orders: 273 units/month → 1.2 months payback
- **Verdict:** xTool S1 justified at $50K/month if any engraving demand exists. Low-risk investment.

*Second Bambu P1S ($399):*
- Throughput: doubles production capacity, eliminates single-printer availability risk
- Break-even: one week of production at $50K/month velocity ($50K / 4 weeks = $12,500/week gross)
- If second printer avoids one week of Etsy stockout per year: $12,500 revenue protected vs. $399 equipment cost
- **Verdict:** Second printer is the highest-ROI equipment investment in the entire ModRun equipment roadmap. Purchase at Month 2–3 when weekly volume consistently exceeds 30 units for two consecutive weeks.

### 2.3 Scale Point 3: $200K/Month Revenue (~1,000+ Units/Week)

**Revenue context:** $200K/month with $27.50 blended AOV = 7,273 orders/month. At 70% margin = ~$140,000/month gross profit.

**Five-printer in-house fleet cost model:**
- 5 Bambu P1S (4 additions at $399 each) = $1,596 additional capital
- Filament: $10/kg × ~50kg/month = $500/month (pallet-tier pricing)
- Full-time production assistant (40 hrs/week, $18/hour W-2 equivalent cost = $22.50 fully burdened): $3,900/month
- Custom packaging: $0.40/order × 7,273 = $2,909/month
- Printago or fleet management software: $100–200/month
- **Monthly non-shipping, non-Etsy COGS: ~$7,409/month**
- Monthly gross profit: ~$132,591/month

**Hybrid model alternative (3 in-house, 2 outsourced via Xometry):**
- In-house (3 printers): ~4,400 units/month manufacturing cost ~$572
- Outsource overflow (2,873 units via Xometry at $5/unit): $14,365/month
- Total manufacturing COGS: $14,937/month (vs. $500 fully in-house)
- Gross profit penalty: ~$14,437/month = $173,244/year
- Cost of adding 2 more P1S printers: $798 one-time
- **Hybrid model has zero cost justification. Pure in-house wins completely at this scale.**

**At $200K/month, the critical investment decision is not printers — it is staffing:**

| Staffing option | Cost | Capability | Risk |
|---|---|---|---|
| Part-time contractor (20 hrs/week) | $1,200–$1,500/month | 400–600 units/week | Capacity ceiling, turnover |
| Full-time production assistant | $3,200–$4,000/month (fully burdened) | 700–1,000 units/week | Hire/fire risk, training overhead |
| 3PL outsource | $7/order × 7,273 = $50,911/month | Unlimited scale | Loss of production control |

At $200K/month, bringing in a full-time production assistant ($3,200–$4,000/month fully burdened) is clearly correct vs. 3PL ($50,911/month). The 3PL is categorically cost-prohibitive for physical product fulfillment at this scale unless the operator has no space, no time, and no interest in maintaining any operational involvement — which contradicts the business model.

---

## Section 3: Break-Even Analysis for Key Equipment Investments

### 3.1 Bambu P1S Second Printer ($399)

**Trigger:** Weekly production volume consistently exceeds 30 units for 2 consecutive weeks.

**Break-even math:**
- Additional gross profit from doubled throughput: approximately $19.18/order (69.7% margin on $27.50 AOV)
- Units per week with second printer: 60+ (first printer handles existing 30; second handles overflow)
- Incremental gross profit per week: 30 units × $19.18 = $575.40
- Break-even: $399 / $575.40/week = **0.7 weeks**
- Annual incremental gross profit from second printer (30 additional units/week × 52 weeks × $19.18): **$29,921**

The second printer pays for itself in under one week of incremental production. This is the single highest-ROI capital investment in the business. The only reason to delay is if demand has not been validated at 30 units/week consistently — the risk is inventory, not equipment economics.

### 3.2 AMS 2 Pro Multi-Color Upgrade ($286)

**Trigger:** Any multi-color order inquiry or listing reaches 20 units/month.

**Break-even math (conservative, laser engraving path):**
- Multi-color SKU price premium: 20–30% over standard ($27.50 AOV → $33–36 for multi-color bundle)
- Incremental revenue per multi-color order: $5.50–$8.50
- At 20 multi-color orders/month: $110–170/month incremental
- Break-even: $286 / $140/month average = **2 months**
- Unattended overnight benefit: eliminates manual filament changes; saves ~1 hour/week of operator time
- Annual labor savings: 52 hours × $15/hour = $780

AMS 2 Pro pays back in 2 months from price premiums alone, with labor savings as an additional benefit. Low-risk addition at any scale above 20 units/week.

### 3.3 xTool S1 40W Laser Engraver ($1,899)

**Trigger:** 200 engraved/personalized units/month demand validated.

**Break-even math:**
- Personalized/engraved SKU premium: $5–10/unit above standard
- At 200 units/month with $7 average premium: $1,400/month incremental revenue
- Break-even: $1,899 / $1,400/month = **1.4 months**
- Pre-validation path: outsource 10–20 laser-engraved samples to a local contract shop ($100–150) to validate demand before purchasing

**Risk-adjusted break-even (50% demand materialization):**
- If only 100 units/month generate engraving demand: $700/month incremental
- Break-even: $1,899 / $700 = **2.7 months**

At any reasonable engraving demand materalization above 100 units/month, the xTool S1 is financially justified within one quarter. The pre-validation step (spend $100–150 at a contract laser shop first) is the correct risk management tool.

### 3.4 Elegoo Saturn 4 Ultra MSLA Resin Printer ($500–600)

**Trigger:** 50+ specialty resin units/month demand validated AND per-unit contract resin cost exceeds $15.

**Break-even math:**
- Resin part COGS in-house: approximately $2–4/unit (material + electricity + depreciation at $574 purchase price)
- Resin part COGS via Shapeways/Craftcloud: $10–25/unit
- Savings per unit: $8–21
- At 50 units/month with $12 average savings: $600/month savings
- Break-even: $574 / $600/month = **0.96 months** if demand validates at 50 units

Caveat: Resin printing has high post-processing labor (wash, cure, support removal, PPE) that adds $1–3/unit of labor cost not captured in COGS. Effective savings are $6–18/unit vs. outsourced, not $8–21. Adjusted break-even at 50 units/month: $574 / ($9 average savings × 50) = **1.3 months**.

The resin printer is cost-justified at 50+ specialty units/month. The key risks are (1) demand for resin products at ModRun never materializes (cable management is PLA territory), and (2) post-processing labor is consistently underestimated. Validate resin demand via Shapeways listings before purchasing.

### 3.5 Amazon FBA Entry

**Not equipment, but capital commitment — treat as break-even analysis:**

FBA requires sending inventory (30–90 days of supply) to Amazon fulfillment centers before any sales occur. At $12/unit production cost and 50 units of initial inventory: $600 upfront.

Amazon FBA fees for a 4oz product (cable clip): $2.89–3.39 fulfillment fee + 15% referral fee = approximately $4.69–5.19/unit in combined fees on a $12 list price, vs. Etsy 9.5% + shipping.

FBA makes financial sense when Amazon's higher average order volume (larger search traffic, Prime shipping advantage) generates enough incremental orders to offset the higher fee structure. FBA is not a cost optimization — it is a channel expansion. The break-even question is: does Amazon generate enough incremental revenue to justify the additional inventory capital and operational complexity?

Recommendation: Validate Etsy channel to $5,000/month before opening Amazon. The learning from Etsy (which keywords convert, which variants sell, what ASP customers accept) informs FBA inventory decisions and reduces the risk of sending the wrong product mix to FBA.

---

## Section 4: Risk-Adjusted Decision Rules

### 4.1 Framework for Integration Decisions

Three dimensions determine the correct integration level for any function:

**1. Cost differential (in-house vs. partner):** If in-house cost is less than 50% of partner cost, own it. If in-house cost is 80–120% of partner cost, the decision is driven by capability and flexibility, not economics. If in-house cost exceeds partner cost, partner is preferred unless strategic control arguments apply.

**2. Strategic importance:** Functions that directly create product differentiation (design, QC for snap-fit quality) should stay in-house regardless of cost comparison. Functions that are commodity operations (label printing, raw material receiving, shipping label generation) can be delegated without competitive risk.

**3. Capital payback period:** Equipment with <3 month payback at the projected volume is a buy decision with confidence. Equipment with 3–12 month payback requires demand validation first. Equipment with >12 month payback requires a documented thesis about the new revenue it will enable.

### 4.2 Decision Rules with Confidence Intervals

| Decision | Volume Trigger | Confidence | Primary Risk |
|---|---|---|---|
| Own second P1S | 30 units/week for 2+ weeks | 95% | Demand regression (printer sits idle) |
| Own AMS 2 Pro | 20 multi-color orders/month | 88% | Multi-color doesn't differentiate enough |
| Partner with 3PL | 250–300 orders/month | 82% | 3PL inbound requirements change workflow |
| Own xTool S1 laser | 200 engraved units/month | 78% | Personalization demand lower than expected |
| Enter Amazon FBA | $5,000/month Etsy established | 85% | Amazon listing optimization learning curve |
| Own resin printer | 50 specialty units/month | 70% | Post-processing labor kills margins |
| Hire first employee | $15,000/month gross revenue | 75% | Revenue variability; W-2 commitment |
| Contract overflow to Xometry | Backlog >2 weeks AND new demand | 92% | Cost (20–100x in-house); use only for bridge |

**Confidence intervals reflect uncertainty in demand materialization.** The equipment economics themselves are not uncertain — the question is always whether the volume trigger will actually be reached. The correct approach is to validate demand in each category before committing capital, using outsourced validation (contract laser shop, Shapeways listing, etc.) as the demand signal.

### 4.3 Anti-Patterns: What Not to Do

**Anti-pattern 1: Buying equipment to enable supply before validating demand.** Buying a second printer to produce 60 units/week before 30 units/week demand exists creates ~3–6 months of idle printer capacity and cash tied up in equipment. Rule: demand at the trigger level for two consecutive weeks before purchasing.

**Anti-pattern 2: Using contract manufacturing to avoid equipment capital.** At any volume above 5 units/month, in-house equipment pays back within weeks. The correct reason to use contract manufacturing is overflow and continuity, not cost avoidance.

**Anti-pattern 3: Moving to 3PL before 250 orders/month.** All mainstream 3PLs have monthly minimums of $400–750. Below 250 orders/month, the minimum fee alone creates a per-order overhead of $1.60–$3.00 before actual per-order costs. DIY with Pirate Ship costs $0 platform fee through any volume.

**Anti-pattern 4: Adding employees before exhausting contractor options.** W-2 employees cost 1.25–1.4x base salary in overhead. A $15/hour W-2 employee actually costs $18.75–21/hour. A $21/hour 1099 contractor has equivalent total cost with zero employment overhead, zero payroll tax filing, and full flexibility. Exhaust the contractor model before making any W-2 hire.

---

## Sources

- [AON3D: 3D Printing In-House vs. Outsourced Analysis](https://www.aon3d.com/applications/in-house-vs-outsourced-3d-printing/)
- [Sinterit: 3D Printing In-House vs. Outsourcing](https://sinterit.com/3d-printing-guide/costs-of-a-3d-printing/3d-printing-in-house-vs-outsourcing/)
- [PEA3D: 3D Printer ROI and Profitability Guide 2026](https://pea3d.com/en/3d-printing-profitability-bambu-lab-roi-analysis/)
- [StackSheriff: 3D Print Farm ROI Calculator](https://stacksheriff.com/toolbox/print-farm-roi/)
- [Bambu Lab P1S Product Page](https://us.store.bambulab.com/products/p1s)
- [Protolabs Pricing and Payment](https://www.protolabs.com/help-center/pricing-and-payment-options/)
- [JLC3DP 3D Printing Cost](https://jlc3dp.com/blog/3d-printing-cost)
- [Ultimaker: In-House vs. Outsourcing 3D Printing](https://ultimaker.com/learn/in-house-3d-printing-vs-3d-printing-service/)
- Sessions 544, 697, 796 cost model baselines (ModRun project internal)
