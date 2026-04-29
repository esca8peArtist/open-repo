---
title: "12-Month Adjacent Technology Rollout — Capital Plan and Decision Trees"
project: mfg-farm
created: 2026-04-29
status: production-ready
session: Item18
depends_on: ITEM18_ADJACENT_MANUFACTURING_ECONOMICS.md, technology-comparison-matrix.csv
---

# 12-Month Adjacent Technology Rollout — Capital Plan and Decision Trees

**For the ModRun mfg-farm operator — Phase 3-4 capital allocation and milestone gates.**

---

## Overview

This plan operates on a conditional capital model: each wave requires a demand validation gate before committing capital to the next level. Total capital exposure if all gates trigger is approximately $6,000–10,000 over 12 months. Conservative path (only laser engraving validated, no resin or injection molding) requires $2,100 in equipment capital.

**Core principle**: Validate demand with contract shops and low-cost experiments before buying equipment. The contract-shop test for laser engraving costs $50–150 and takes 2 weeks. That $50–150 replaces a speculative $1,899 equipment purchase.

---

## Wave 1: Laser Engraving Validation (Months 1–3)

### Month 1: Contract-Shop Test

**Action**: Send 15–20 cable clips to a local makerspace, laser engraving service, or Ponoko for outsourced engraving. Designs: a 2-line text engrave ("audio / USB-C") and a simple line-art logo example.

**Cost**: $50–150 (outsourced engraving at $3–8/piece)

**Simultaneously**: Create an Etsy listing for "Custom Engraved Cable Clip — Personalized Name or Label." List at $16–18 (vs. $12 standard). Photograph the engraved prototypes with lifestyle staging against the desk setup they serve.

**Success metric**: Orders begin appearing. Even 5–10 orders in Month 1 at the elevated price point validates that the personalization premium exists.

### Month 2: Scale Outsourcing if Demand Appears

**Action**: If Month 1 generated 10+ orders for engraved clips: continue outsourcing at $5–8/piece while tracking:
- Net margin per engraved order (revenue minus outsourced engraving cost, Etsy fees, shipping)
- Repeat customer rate and review quality
- Order velocity trend (is it growing week-over-week?)

**Cost**: Variable — outsourced engraving only. Budget $150–400 depending on order volume.

**If Month 1 generated <5 orders**: Do not scale outsourcing. Evaluate whether the listing photography, pricing, or description needs revision. Run one A/B test (different photography or title) in Month 2 before drawing conclusions.

### Month 3: Equipment Purchase Gate

**Decision trigger**: Buy xTool S1 40W if **both** of these are true:
1. Outsourced engraved units exceed 50/month by end of Month 2
2. Net margin on engraved orders exceeds $3.50/unit after outsourcing cost (confirming the premium captures more than the outsourcing overhead)

**If YES**: Purchase xTool S1 40W ($1,899 + $60 LightBurn license + $90 ventilation duct kit + bench fixtures = $2,049 total). Setup and calibration: 1 full day. First production run of engraved clips: within 3 days of receipt.

**If NO — demand below threshold**: Do not purchase. Continue outsourcing at low volumes. Re-evaluate at Month 6.

**Decision tree:**

```
Month 2 engraved units > 50/month?
├── YES → Net margin per unit > $3.50?
│         ├── YES → BUY xTool S1 ($2,049) in Month 3
│         └── NO  → Diagnose: is outsourcing cost too high, or is the premium too low?
│                   → Negotiate lower outsourcing rate first; re-evaluate Month 4
└── NO  → Continue outsourcing; revisit Month 6 with 90-day demand data
```

**Wave 1 capital summary:**

| Item | Cost | Trigger |
|---|---|---|
| Contract-shop prototype engraving | $50–150 | Month 1 — always |
| Outsourced production during validation | $150–400/month | Month 2 — if demand appears |
| xTool S1 40W + LightBurn + duct | $2,049 | Month 3 — if gate passes |
| **Wave 1 total (equipment gate triggers)** | **$2,249–$2,599** | |
| **Wave 1 total (equipment gate does not trigger)** | **$200–550** | |

**Expected outcome if gate triggers**: By Month 5 (2 months of in-house laser production), the xTool investment is generating $400–800/month in incremental net profit from engraved products. Payback in 4–5 months. Annual run rate from laser engraving alone: $5,000–10,000 net.

---

## Wave 2: Resin Printing Evaluation (Months 4–6)

### Month 4: Entry Equipment Purchase (Low Capital, Independent of Laser Gate)

The resin printing entry decision is lower-stakes than laser engraving because the equipment cost is $574 all-in — comparable to 2–3 months of outsourced laser engraving. This makes it viable to test resin printing even if the laser gate did not trigger, as a parallel bet on a different product category.

**Action**: Purchase Elegoo Saturn 4 Ultra 16K ($499) + Elegoo Mercury Plus V3 Wash and Cure Station ($75) = $574 total. Acquire test resins: 1L clear standard ($30), 1L gray standard ($28), 1L ABS-like ($30). Total Month 4 capital: $662.

**Product development sprint**: Design and test 2–3 resin-specific product concepts over 3–4 weeks:
1. Transparent cable channel cover (snap-on PLA clip accessory in clear resin; showcases cable routing)
2. Precision desk cable anchor with 0.1mm tolerance fit for monitor stand VESA mount
3. Miniature cable label set in bright-colored resin (snap-on, readable from across desk)

**Listing**: Create Etsy listings for each concept once 10+ quality samples are produced and photographed.

### Month 5: Market Signal Assessment

**Track for Month 4–5 listings:**
- Favorites and click-through rate (leading indicator for orders)
- First orders and review content (are customers noting surface quality as the value?)
- Return rate on precision-fit parts (indicates whether resin tolerance is meeting customer expectations)

**Outsource alternative**: If you do not want to invest $574 in resin equipment, you can order resin prints from a service (Shapeways, i.materialise, Craftcloud) for $5–25/piece for prototypes. Use this path for the first 5–10 pieces to get product photography before equipment purchase.

### Month 6: Form 4 Gate vs. Continue with Saturn 4

**Decision trigger for Form 4 upgrade ($3,499)**:

The Form 4 is justified if **all three** of these are true:
1. Resin product revenue exceeds $800/month net (after Etsy fees and material costs)
2. Post-processing labor on the Saturn 4 is exceeding 6 hours/week (the Form 4's workflow reduces this materially)
3. At least one resin product has 20+ reviews with consistent 5-star quality feedback

If these conditions are met, the Form 4 upgrade pays back in 4–5 months on the incremental reliability and workflow improvement alone.

If conditions are not met: continue with the Saturn 4. It is sufficient for volumes below 150–200 parts/month and remains the right tool for the current scale.

**Formlabs rental/lease note**: Formlabs does not operate a public rental program. Resellers may offer 12–36 month lease financing at approximately $80–150/month. At $120/month lease vs. $3,499 purchase: over 36 months, total cost is $4,320 (lease) vs. $3,499 (purchase). Purchase is financially better if you have the capital; lease is appropriate if capital is constrained and resin revenue is already $400+/month.

**Decision tree:**

```
Month 5 resin product revenue > $400/month?
├── YES → Tracking toward $800/month goal?
│         ├── YES → Prepare for Form 4 upgrade at Month 6 if revenue sustained
│         └── NO  → Identify constraint: product-market fit, pricing, or photos?
└── NO  → Revenue <$400/month: continue Saturn 4; no Form 4 upgrade
           → If <$100/month by Month 6: resin printing is not a current opportunity
              → Keep Saturn 4 for prototyping; revisit resin market in Q4
```

**Wave 2 capital summary:**

| Item | Cost | Trigger |
|---|---|---|
| Elegoo Saturn 4 Ultra 16K + Mercury Plus | $574 | Month 4 — low-risk always |
| Test resin supply (3 liters) | $88 | Month 4 — always |
| Formlabs Form 4 upgrade | $3,499 | Month 6 — only if resin revenue >$800/month |
| **Wave 2 total (Form 4 gate triggers)** | **$4,161** | |
| **Wave 2 total (Form 4 gate does not trigger)** | **$662** | |

---

## Wave 3: Injection Molding Decision Gate (Months 7–12)

### Month 7: Volume Check — The Hard Gate

**This gate cannot be forced.** Injection molding only makes financial sense when the monthly production volume of a single SKU is consistently above 500 units per month. Below this threshold, FDM is strictly lower COGS with no tooling risk.

**Month 7 check**: What is the trailing 60-day average monthly unit volume of ModRun's highest-volume single SKU?

| Volume | Action |
|---|---|
| > 500 units/month (single SKU) | Proceed to injection molding process |
| 300–500 units/month | Wait — check again at Month 10 |
| < 300 units/month | Do not pursue injection molding in this 12-month window |

**Design preparation (Month 7–8, if volume gate passes):**

Converting the CadQuery FDM cable clip design for injection molding requires 5–10 hours of CAD work:
1. Add 1–2° draft angles to all vertical walls
2. Design gate location (typically at thickest wall section)
3. Add ejector pin clearances (1mm minimum from features)
4. Verify uniform wall thickness (maximum 3–4mm to prevent sink marks)
5. Remove any features that create undercuts unless side-action slides are designed into the mold

Budget $200–400 for this design revision (either your own time at 8–10 hours, or a freelance design engineer at $30–50/hour on Upwork).

### Months 8–9: Quoting and Mold Construction

**Quoting process:**

Submit CAD (STEP format) to Fictiv for injection molding quote: https://www.fictiv.com/injection-molding-service

Also submit to one Chinese alternative (PCBWay, JLCCNC) for price benchmarking. The gap between domestic and overseas quotes for aluminum molds has narrowed in 2026 due to tariffs; expect 20–40% differential rather than the 50–60% of pre-2024.

**Target mold specs for cable clip:**
- Material: P20 steel or 7075 aluminum (aluminum for <10,000 unit production target)
- Cavities: 1 (single-cavity; do not invest in multi-cavity until design is fully validated)
- Surface finish: SPI A-1 (glossy) or SPI C-1 (matte texture) depending on desired aesthetics
- Shot life (aluminum): 10,000–50,000 shots
- Expected quote: $2,000–4,000 for Fictiv aluminum single-cavity; $800–2,000 overseas

**Timeline from order to T1 samples:**
- Fictiv domestic network: 10–15 business days
- Overseas: 15–25 business days

**T1 sample review (Month 9):**

Receive 5–10 T1 parts. Inspect against drawing:
- Dimensional check on all critical tolerances (snap-fit gap, clip width, mounting point diameter)
- Surface finish check
- Functional test: does the clip install and remove correctly on target cable sizes?
- Gate mark location: is the gate scar in an acceptable position (hidden face)?

If T1 parts require revision: submit correction request to mold shop (expect $200–600 for minor corrections, 5–10 additional business days). This is normal — T1 samples almost always require at least minor corrections.

### Month 10: First Production Run

**Specifications for first injection molding run:**

| Volume | Per-Unit Cost (post-mold) | Total Run Cost | Notes |
|---|---|---|---|
| 500 units | $1.50–2.50 | $750–1,250 | First validation run; use to fill backlog |
| 1,000 units | $0.90–1.50 | $900–1,500 | Better unit economics; recommended minimum |
| 2,000 units | $0.60–1.00 | $1,200–2,000 | Stronger economics but requires 2-month backlog |

Recommended first run: 1,000 units. This provides 1–2 months of inventory at 500 units/month, enough to validate that injection-molded parts meet customer expectations before committing to a larger run.

**Quality control on first run:**

Sample 10% of the run (100 units) for dimensional inspection. Spot-check snap-fit function on 20 units. Inspect gate mark on all 100 sampled units for unacceptable flash or surface defects.

### Months 11–12: Evaluate ROI and Ongoing Strategy

**After first production run:**

Calculate actual COGS per injection-molded unit including:
- Mold amortization (mold cost ÷ total units planned for mold life; assume 10,000 shot mold life for planning)
- Per-unit material and machine cost from job shop invoice
- Incoming QC time (1 minute/unit sample)
- Storage cost (injection-molded parts require less active management than FDM — they stack efficiently)

Compare to FDM COGS: if injection molding COGS including mold amortization is below $1.15 (FDM COGS), the transition is justified at current volume. If above $1.15, FDM remains superior and injection molding is only a future option when volume increases.

**12-month review decision points:**

1. Is the injection-molded product delivering consistent quality (< 3% defect rate)?
2. Has the customer perception shifted positively (review language, return rate)?
3. Is the mold amortizing on schedule (are monthly volumes sustaining the original threshold)?
4. Is the freed FDM capacity being redeployed to higher-margin products (laser engraved, resin specialty, new SKUs)?

If answers are YES: commit to multi-cavity mold for the next tooling investment at Month 15 (outside this plan's scope).

If answers are NO on quality or volume: return to FDM for the affected SKU. The aluminum mold remains available for future use; the loss is the tooling capital, not the ongoing production cost.

---

## Capital Allocation Summary

### Budget Scenarios

**Scenario A: Laser Only (Conservative Validation)**

Wave 1 contract test → laser demand validates → xTool S1 purchased

| Month | Action | Capital |
|---|---|---|
| 1 | Contract-shop prototype engraving | $150 |
| 2 | Outsourced production during validation | $300 |
| 3 | xTool S1 40W + LightBurn + duct | $2,049 |
| **Total** | | **$2,499** |

Expected return by Month 12: $5,000–10,000 net from laser engraving product line.

---

**Scenario B: Laser + Resin Entry (Recommended)**

Wave 1 laser validation + Wave 2 resin entry regardless of laser outcome

| Month | Action | Capital |
|---|---|---|
| 1 | Contract-shop prototype engraving | $150 |
| 2 | Outsourced production | $300 |
| 3 | xTool S1 (if laser gate passes) | $2,049 |
| 4 | Elegoo Saturn 4 + Mercury Plus + resin supply | $662 |
| **Total** | | **$3,161** |

Expected return by Month 12: $6,000–15,000 net from laser + specialty resin products.

---

**Scenario C: Full Path (All Gates Trigger)**

All three waves execute: laser buy → Form 4 upgrade → injection molding tooling

| Month | Action | Capital |
|---|---|---|
| 1 | Contract-shop prototype engraving | $150 |
| 2 | Outsourced production | $300 |
| 3 | xTool S1 purchase | $2,049 |
| 4 | Elegoo Saturn 4 + Mercury Plus + resin | $662 |
| 6 | Formlabs Form 4 (if resin >$800/month) | $3,499 |
| 7–8 | IM design revision CAD work | $300 |
| 9 | Fictiv mold construction (aluminum, single-cavity) | $3,000 |
| 10 | First injection molding production run (1,000 units) | $1,200 |
| **Total** | | **$11,160** |

Expected return by Month 12 (all gates): $15,000–30,000 net (ModRun FDM + laser + resin + IM combined). Note: this scenario requires ModRun to be running at 500+ units/month by Month 7, which itself implies $8,000–15,000/month revenue — making the capital investment proportional.

---

## Risk Mitigations Built Into This Plan

**Capital gating**: No equipment purchase is made until demand is validated. The laser engraving contract test costs $150 and takes 2 weeks — this is the cheapest possible validation mechanism.

**Sequential commitment**: Each wave is independent. If laser engraving does not validate in Month 2, the plan pivots to evaluating resin printing as an independent experiment (Month 4 $662 investment is still justified on its own merits given the low entry cost).

**Reversibility**: xTool S1 and Elegoo Saturn 4 equipment retain 50–70% resale value if products fail to gain traction. The injection mold is the least reversible investment — it is worthless if the product is discontinued, which is why it sits behind the strictest volume gate.

**FDM as the fallback**: At every decision point, FDM remains the default. If no adjacent technology validates demand at adequate margin, the ModRun operation continues scaling FDM capacity (5-printer farm roadmap from multi-printer-architecture.md) without any of the capital commitments in this plan.

---

## Quick-Reference Decision Trees

### Laser Engraving Gate (Month 3)

```
Outsourced engraved units > 50/month AND net margin > $3.50/unit?
├── YES → Buy xTool S1 40W ($2,049)
└── NO  → Continue outsourcing; check again at Month 6
```

### Resin Printing Gate (Month 6 — Form 4 upgrade)

```
Resin product revenue > $800/month sustained?
├── YES → Buy Formlabs Form 4 ($3,499) OR explore lease at $120/month
└── NO  → Continue with Elegoo Saturn 4; no upgrade needed
```

### Injection Molding Gate (Month 7)

```
Single-SKU monthly volume > 500 units sustained for 60+ days?
├── YES → Product design frozen (no anticipated revisions)?
│         ├── YES → Begin Fictiv quote; design revision ($300); mold order ($2,000–4,000)
│         └── NO  → Freeze design first; revisit Month 9
└── NO  → Do not pursue injection molding this window
           → Check again at Month 10 or 12
```

---

## One-Page Summary

**Month 1**: Spend $150 on outsourced laser engraving of 20 cable clips. List on Etsy at $16–18. Track orders.

**Month 3**: If 50+ engraved units/month → buy xTool S1 ($2,049). If not → continue outsourcing.

**Month 4**: Buy Elegoo Saturn 4 + wash/cure ($662) regardless of laser outcome. Test 2–3 resin product concepts. This is a low-risk bet on a different market segment.

**Month 6**: Form 4 upgrade ($3,499) only if resin revenue >$800/month. Otherwise keep the Saturn 4.

**Month 7**: If ModRun volume >500 units/month of a single SKU → begin injection molding process. If not → stay on FDM.

**Capital floor**: $812 (resin entry + contract test, no equipment gates trigger).
**Capital ceiling**: ~$11,000 (all gates trigger, all capital deployed).
**Expected path (realistic)**: Scenario B — laser + resin entry — at approximately $3,200 over 12 months.
