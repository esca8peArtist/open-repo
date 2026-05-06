---
title: Revenue Ramp Dashboard & Scaling Triggers
project: mfg-farm
created: 2026-05-06
status: live-tracking-template
audience: Anya — update weekly every Sunday; review scaling triggers monthly
scope: Week-by-week revenue projections, unit volume tracking, gross margin monitoring, supplier cost reduction, scaling triggers
related: cost-model-spreadsheet.csv, product-line-strategy.md, post-test-print-execution.md
confidence: high
---

# Revenue Ramp Dashboard & Scaling Triggers

**Lead finding:** The 4-week ramp from first listing to $2,500/month target is achievable but not automatic. The model is accurate; the demand variable is what creates uncertainty. This document gives you the numbers to track, the thresholds that trigger action, and the decisions that convert a launch into a business. Update it every Sunday.

---

## Target Revenue Model: Weeks 1–10

### Week-by-Week Gross Revenue Projections

These projections assume:
- ModRun clips: $24.99 blended average order value (3-clip bundles + single units)
- Headphone hook launches Week 4 at $15/unit average
- No Product 3 until Week 7 at earliest
- USPS 8% surcharge embedded in COGS through January 2027
- Etsy Ads at $1/day ($7/week) ongoing

| Week | ModRun Units | Hook Units | Total Units | Gross Revenue | Etsy Fees (~9.5%) | Ads Spend | Net Revenue |
|---|---|---|---|---|---|---|---|
| 1 | 5–8 | 0 | 5–8 | $125–200 | $12–19 | $7 | $106–174 |
| 2 | 8–12 | 0 | 8–12 | $200–300 | $19–29 | $7 | $174–264 |
| 3 | 12–18 | 0 | 12–18 | $300–450 | $29–43 | $7 | $264–400 |
| 4 | 15–20 | 5–8 | 20–28 | $450–575 | $43–55 | $7 | $400–513 |
| 5 | 18–22 | 8–12 | 26–34 | $600–700 | $57–67 | $7 | $536–626 |
| 6 | 20–25 | 10–15 | 30–40 | $700–875 | $67–83 | $7 | $626–785 |
| 7 | 20–25 | 12–18 | 32–43 | $750–975 | $71–93 | $7 | $672–875 |
| 8 | 22–28 | 15–20 | 37–48 | $875–1,100 | $83–105 | $7 | $785–988 |
| 9 | 25–30 | 18–22 | 43–52 | $1,000–1,200 | $95–114 | $7 | $898–1,079 |
| 10 | 25–32 | 20–25 | 45–57 | $1,100–1,350 | $105–128 | $7 | $988–1,215 |

**4-week cumulative target:** $600–$800 gross
**8-week cumulative target:** $3,500–$5,000 gross
**Monthly run rate by Week 10:** $2,200–$2,800/month gross (~$1,800–$2,300 net after fees and ads)

**Monthly milestone targets:**
- Month 1 (Weeks 1–4): $600–$800 gross
- Month 2 (Weeks 5–8): $1,500–$2,000 gross
- Month 3 (Weeks 9–12): $2,200–$2,800 gross
- Month 6 (steady state, multi-product): $6,900–$7,500 gross

*Note: Month 6 target requires all 5 product lines from product-line-strategy.md to be live. Magnetic bin labels (Product 3) launch Week 7–8; plant markers (Product 4) at Month 2; pegboard hooks (Product 5) at Month 3.*

---

## Weekly Tracking Template

Copy this to a new row in your Google Sheet every Sunday. Fill in actuals.

```
Week: [NUMBER]
Date: [YYYY-MM-DD]

UNITS
  ModRun shipped this week: ___
  Headphone hook shipped this week: ___
  Other products shipped: ___
  Total units shipped: ___

REVENUE
  Gross revenue this week: $___
  Etsy fees paid: $___
  Ads spend: $___
  Net revenue (gross - fees - ads): $___

COGS THIS WEEK
  Filament consumed: ___ grams (estimated)
  Filament cost: $___
  Packaging cost: $___
  Shipping labels cost: $___
  Total COGS: $___
  
MARGIN
  Gross margin this week: ___% (= (gross - COGS) / gross)
  Is margin above 70%? [ ] Yes  [ ] No — investigate

ETSY METRICS (from Stats dashboard)
  Total views: ___
  Total favorites: ___
  Conversion rate: ___% (sales / views)
  Best-performing listing (most views): ___
  
INVENTORY STATUS
  ModRun clips on hand (finished goods): ___
  Headphone hooks on hand: ___
  Filament on hand — black: ___ kg
  Filament on hand — white: ___ kg
  Filament on hand — grey: ___ kg
  Reorder needed? [ ] No  [ ] Yes — color: ___ qty: ___

OPEN ISSUES
  Customer complaints / cases open: ___
  Defective units this week (scrap rate): ___% 
  Late shipments (beyond stated processing time): ___

THIS WEEK'S TOP PRIORITY:
___________________________________________
```

---

## Unit Volume Tracking: ModRun Baseline

### ModRun Sales Velocity Targets

| Phase | Units/Week | Monthly Gross | Notes |
|---|---|---|---|
| Launch (Weeks 1–2) | 5–12 | — | Building reviews; demand developing |
| Early traction (Weeks 3–5) | 12–20 | $600–$1,200 | Targeting 10+ reviews |
| Steady state (Month 2) | 20–25 | $1,200–$1,400 | Solo operation sweet spot |
| Growth (Month 3) | 30–40 | $1,800–$2,400 | Near single-printer capacity |
| Near-capacity (Month 4) | 40–55 | $2,400–$3,300 | Second printer decision trigger approaching |
| Two-printer scale (Month 5–6) | 55–80 | $3,300–$4,800 | Second printer installed |

**Tracking note:** "Units" here means units shipped to customers, not units printed. Print batch size varies; shipped units is the only revenue-correlated metric.

---

## Gross Margin Monitoring

### Target: 72–73% at 20 units/week

This is the steady-state target from `cost-model-spreadsheet.csv`. The margin at launch will be lower (Week 1–2 scrap rates are higher; initial filament is from 1kg retail spools at slightly higher cost). Do not be alarmed by 65–68% margins in Week 1–2. The floor at 70% should be reached by Week 4.

**Alert thresholds:**

| Margin | Status | Action |
|---|---|---|
| >72% | On target | No action |
| 70–72% | Acceptable | Monitor; check which cost component increased |
| 68–70% | Watch | Identify cause (shipping rate change? higher scrap? discount pricing?) |
| Below 68% | Alert — investigate | See investigation protocol below |
| Below 65% | Critical | Stop discounting immediately; audit every COGS component |

### Margin Alert Investigation Protocol

If weekly margin drops below 68%, run through this checklist in order:

**Step 1 — Identify the driver:**
- Calculate: (gross revenue - filament - packaging - shipping - Etsy fees) / gross revenue
- If margin has dropped, which component increased? Filament? Shipping? Etsy fees?

**Step 2 — Filament cost increase:**
- Compare this week's $/unit material cost to the baseline ($0.42/unit at 20/week)
- If higher: check if you bought a 1kg retail spool at $15–20/kg instead of the 10kg bundle at $12/kg
- Fix: order the 10kg bundle before stock runs out; never buy retail spools for production

**Step 3 — Shipping cost increase:**
- Compare this week's average label cost to the $4.10 baseline
- If higher: check if any orders used Priority Mail instead of Ground Advantage unnecessarily
- Fix: confirm Pirate Ship is defaulting to Ground Advantage on all standard orders

**Step 4 — Scrap rate:**
- If this week's print scrap rate is above 6%, material waste is compressing margin
- See the quality gate failure protocol in `post-test-print-stl-refinement.md`
- A 10% scrap rate effectively adds ~$0.05/unit to material cost — not large, but cumulative

**Step 5 — Discount pricing:**
- Did you discount any orders this week? (Promotional codes, custom orders with reduced price)
- Discounts are fine for reviews, not for sustained volume
- If more than 20% of this week's orders used a discount code, you are training buyers to wait for discounts

---

## Supplier Cost Reduction Opportunities

Track these as monthly review items. Every month, check whether any of these levers can now be pulled.

### Monthly Supplier Cost Review Table

| Lever | Current State | Activation Condition | Potential Saving/Month |
|---|---|---|---|
| eSUN direct wholesale | Amazon bundles at $11–13/kg | 20+ kg/month for 2 consecutive months; email contact@esun3dstore.com | $30–90/month at 30 kg/month |
| Anycubic 50kg pallet | Not yet purchased | AMS validation passed; monthly consumption >12 kg (need >25 kg storage capacity) | $15–45/month vs. Amazon bundles at same volume |
| Polymaker wholesale (white/grey) | Not yet active | Month 3–4; $1,000 minimum order; ~67 kg per order | Quality upgrade, not cost reduction — premium tier only |
| Shop4Mailers bulk | Amazon basics poly mailers at $0.10/unit | Already available — order 1,000-pack on Day 0 | $50/1,000 units ($0.05/unit savings) |
| Pirate Ship vs. retail postage | Already using Pirate Ship | N/A — activate Day 0 | $80–120/month at 20 orders/week |
| SUNLU for color sampling | Not yet purchased | Any time you need a new color in quantities less than 6 kg | Avoids buying 10kg of a color before velocity is confirmed |

**Monthly review question for each lever:** "Has the activation condition been met this month? If yes, activate. If no, record why not and when you expect to meet the condition."

---

## Scaling Triggers

These are binary decision gates — not gradients. When the trigger condition is met, execute the corresponding action within 7 days.

### Trigger 1: Add Second Printer ($699–799)

**Condition (AND logic — both must be true):**
- Single printer running >28 hours/week for 2 consecutive weeks
- Etsy order processing time slipping beyond stated timeline (orders backing up)

**Why 2-week confirmation:** One busy week might be a demand spike, not sustained demand. Two consecutive weeks indicates the constraint is structural.

**Action:** Order second Bambu P1S from BambuLab.com or Amazon. Expected lead time: 3–7 days. While waiting, reduce order acceptance by extending processing time to 7–10 business days — do not continue accepting orders you cannot fulfill within the stated timeline.

**Payback:** At 40 units/week on two printers at $24.99 AOV, the second printer ($750) pays back in approximately 3 weeks of incremental revenue.

### Trigger 2: Anycubic 50kg Pallet ($524)

**Condition:**
- Monthly filament consumption has exceeded 25 kg for 1 month
- Anycubic AMS validation test has passed (zero feed errors on full 12-clip plate)

**Action:** Order the 50kg pallet from store.anycubic.com. Confirm storage capacity before ordering — 50 spools require approximately 10 cubic feet of dry storage.

**Why not before 25 kg/month:** At lower volumes, the cash and storage commitment of a 50kg pallet outweighs the per-kg savings. The break-even on the pallet vs. continuing 10kg Amazon bundles is approximately 250 kg of total consumption at the $1.50/kg savings rate.

### Trigger 3: Post-Processing Help (1099 Contractor)

**Condition:**
- Packaging + shipping + QC is taking more than 3 hours per day for 2 consecutive weeks
- This typically occurs at 100+ units/week but can occur earlier if you have other demands on your time

**Action:** Post a local part-time gig (Facebook Marketplace, Craigslist, Nextdoor) for "part-time order fulfillment assistant, 10–15 hours/week, $15–18/hour." Hire on 1099; no payroll overhead.

**Training investment:** Budget one full day to train a new contractor. The workflow in `post-test-print-doc-4-first-week-operations-sop.md` is the training manual.

### Trigger 4: Add Second Product (if ModRun momentum stalls)

**Condition (EITHER):**
- ModRun weekly views have plateaued below 100/week for 3 consecutive weeks with no obvious optimization path remaining
- Conversion rate is above 1% but order volume is capped by search impressions (algorithm plateau)

**Action:** Accelerate Product Line 2 launch. Do not add a product as a substitute for fixing ModRun — add it as a parallel revenue stream that also drives cross-sell back to ModRun.

**Note:** If ModRun is growing steadily, do not rush Product 2. The product-line-strategy.md sequencing is a guide, not a deadline. A growing ModRun at 20/week is more valuable than splitting focus between two products at 10/week each.

### Trigger 5: Second Supplier (if eSUN Amazon stock-out)

**Condition:**
- eSUN 10kg case (black or white) goes out of stock on Amazon AND estimated restock date is >7 days away

**Action:** Immediately order from Anycubic direct store (if AMS validation has passed) or Overture Amazon listing (ASIN B0FS1XSDQ4 for 10kg bundle). Do not wait until you run out of filament — order the backup the day you notice the stock issue.

**Prevention:** Set up Amazon price and availability alerts for the eSUN 10kg ASIN. The AWS price alert feature (via camelcamelcamel.com) or a manual weekly check is sufficient.

### Trigger 6: 3PL Evaluation (ShipMonk or Simpl Fulfillment)

**Condition (AND logic):**
- Shipping volume exceeds 80–90 orders/week
- Fulfillment time costs more than $6/order in labor (if your time is worth >$15/hour, 3 hours/day ÷ 80 orders = 2.25 minutes/order × $15/hour ≈ $0.56/order — well under $6; but at 80 orders that's 6 hours/day, which at $15/hour = $1.13/order still under $6 3PL cost... BUT)
- Fulfillment is blocking other business-building activities (product design, marketing, supplier negotiations)

**Reality check:** At 80 units/week, self-fulfillment is probably still more profitable than 3PL on a pure cost basis. The 3PL decision is a time-allocation decision, not a cost optimization. If you would rather spend 3 hours/day on product design instead of packaging, pay the 3PL margin to reclaim that time.

**3PL evaluation order:**
1. Simpl Fulfillment (simplfulfillment.com) — no minimum volume, flat-rate per order
2. ShipMonk — 50 orders/month minimum; better rates at scale
3. ShipBob — only after 500+ orders/month, due to $275/month minimum

### Trigger 7: Amazon FBA Onboarding

**Condition:**
- Etsy sales at 50+ units/week for ModRun (baseline proven)
- Specific SKUs (black 3-clip bundle, starter kit) are selling at 20+ units/week each independently

**Action:** Create an Amazon Seller Central account. List the top 2 SKUs as FBA (Fulfilled by Amazon). Ship 50-unit inventory batch to nearest FBA warehouse.

**Math check before activating:**
- FBA fees: 15% referral + $3.06–4.25 fulfillment = $6.81–7.71 per $24.99 order (27–31% take rate)
- Etsy fees: 9.5% + shipping = ~18–20% all-in
- FBA adds ~10–12 percentage points of cost vs. Etsy
- Justified when: Amazon's search volume is large enough to compensate (cable management is a high-volume Amazon category; yes it is)
- Break-even: FBA generates incremental volume that would not have come from Etsy; not volume stolen from Etsy

---

## Ramp Projection: ModRun + Product 2 Launch (Weeks 1–8)

Staggered launch model matching the coordinated timeline:

| Week | ModRun (units) | Hook (units) | Weekly Gross | Monthly Run Rate |
|---|---|---|---|---|
| 1 | 5–8 | 0 | $125–200 | — |
| 2 | 8–12 | 0 | $200–300 | $600 (annualized) |
| 3 | 12–18 | 0 | $300–450 | $1,200 |
| 4 | 15–20 | 5–8 | $450–575 | $1,800 |
| 5 | 18–22 | 8–12 | $600–700 | $2,400 |
| 6 | 20–25 | 10–15 | $700–875 | $2,800–$3,500 |
| 7 | 20–25 | 12–18 | $750–975 | — |
| 8 | 22–28 | 15–20 | $875–1,100 | **$3,500+/month run rate** |

**Month 1 minimum threshold: $600 gross.** If the first month ends below $600 gross, the listing optimization has a problem — not the product or the manufacturing. Review photo, tags, price, and get a second opinion from the r/EtsySellers Reddit community.

---

## Confidence Notes

**High confidence:** All COGS components and margin percentages in this document are grounded in cost-model-spreadsheet.csv (verified figures). Scaling triggers are directly from post-test-print-execution.md Section 5 (printer trigger), Section 3.2 (fulfillment contractor trigger), and phase-2-supplier-research.md (pallet trigger).

**Medium confidence:** Week-by-week unit projections (5–8 units in Week 1 growing to 25–32 in Week 10) are informed estimates based on typical Etsy launch trajectories for niche physical product listings. Actual velocity depends heavily on Etsy algorithm traction, photo quality, and whether any social post drives a traffic spike. The projections represent a realistic (not optimistic) scenario.

**Lower confidence:** Amazon FBA onboarding trigger economics are based on current FBA fee schedules (May 2026). FBA fees have historically increased annually; verify current rates before activating this trigger.

**Gap:** The revenue ramp model does not include a scenario where Etsy removes or deprioritizes listings (rare but possible under the June 2025 original-design enforcement). If a listing is ever flagged, the mitigation is your git commit history showing original CadQuery design provenance. Maintain this as a standing practice.
