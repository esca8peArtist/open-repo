---
title: "Phase 2 Scaling Decision Matrix — Three Scenarios"
project: mfg-farm
created: 2026-06-06
status: production-ready
confidence: 85%
scope: >
  Capital needs, timeline, revenue projections, break-even analysis, and risk
  assessment for three Phase 2 scaling paths based on Phase 1 traction signals.
depends_on:
  - PRODUCTION_FARM_SCALING_STRATEGY.md
  - ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md
  - cost-model-spreadsheet.csv
  - MULTI_PRINTER_FARM_ARCHITECTURE.md
---

# Phase 2 Scaling Decision Matrix — Three Scenarios

## Executive Summary

Once test print passes (June 3) and Etsy launch executes (June 3-15), Phase 1 traction data will arrive by **late June 2026**. This document provides three mutually exclusive scaling paths — **Conservative**, **Standard**, and **Aggressive** — keyed to Phase 1 revenue signals.

**Decision Rule**: Use June 30 cumulative revenue as the primary gate. Each scenario unlocks at a different revenue threshold and carries distinct capital, timeline, and profitability profiles.

| Scenario | Phase 1 Signal (June 30) | Capital Required | Timeline to Printer 3 | 12-Month Net Profit | Upside/Risk Profile |
|---|---|---|---|---|---|
| **Conservative-1-printer-slow** | <$1,000 cumulative | $399 (Printer 2 only) | March 2027+ | $8,000–12,000 | Low capital, slow growth, viable steady state |
| **Standard-2-printer-Q3** | $1,000–$3,000 cumulative | $1,200–1,500 (P2, circuits, SM) | September 2026 | $18,000–28,000 | Balanced risk/reward, normal Etsy growth |
| **Aggressive-3-printer-Q2** | $3,000+ cumulative | $3,500–4,500 (P2, P3, laser, circuits) | July-August 2026 | $28,000–42,000 | High capital, fast execution, unproven demand |

---

## Part 1: Conservative Scenario — 1-Printer Operational Through 2026

### Scenario Definition

**Phase 1 outcome**: Etsy launch generates **$400–$1,000 in cumulative revenue by June 30** (roughly 15–40 orders, 1–2 reviews). Organic traffic is low; conversion rate near 1–2%; limited time spent on Etsy or Ads optimization.

**Strategic response**: Do not add capital until demand pulls clearly above single-printer capacity. Remain in Phase 1 solo operation through Q3 and Q4 2026, using the months to improve product photography, expand the SKU line (via CAD iteration and bureau services), and optimize Etsy SEO.

### Capital Plan

| Item | Cost | Timing | Notes |
|---|---|---|---|
| Printer 2 (optional, only if demand exceeds 20 units/week) | $399 | Q4 2026 | Hold decision until October; only order if sustained >25 units/week for 3 weeks |
| Bureau laser engraving (validation phase) | $50–150 | July-August | Send 20 clips to SendCutSend; test 3–5 personalized variants at $32–38 each |
| Acrylic label bureau cutting (validation phase) | $40–80 | August | 20 sets of 5-panel label packs via SendCutSend at ~$2/set cost |
| Etsy Ads spend (optional, low-intensity) | $0–150/month | July-December | $0–5/day if conversion rate justifies; pause if ROAS <2× |
| **Total Phase 2 capex** | **$399–$779** | **June–December** | **Spread across year; no large upfront commitment** |

### Revenue & Profitability Projections

**Monthly run-rate assumptions**:
- July 2026: $300–600 (Etsy algorithm boosts early 20–30 reviews; standard growth curve)
- August: $500–1,000
- September: $700–1,500
- October: $1,200–$2,500 (Q4 seasonal lift)
- November-December: $2,500–$5,000 (holiday peak)
- **Cumulative Jan-Dec 2026: $8,500–$15,000**

**Monthly net profit (solo operation)**:

| Month | Gross Revenue | COGS + Overhead | Net Profit | Cumulative |
|---|---|---|---|---|
| June | $600 | $250 | $350 | $350 |
| July | $450 | $200 | $250 | $600 |
| August | $750 | $320 | $430 | $1,030 |
| September | $1,200 | $500 | $700 | $1,730 |
| October | $1,800 | $700 | $1,100 | $2,830 |
| November | $3,500 | $1,400 | $2,100 | $4,930 |
| December | $4,200 | $1,700 | $2,500 | $7,430 |
| **Total 2026** | **$12,500** | **$5,070** | **$7,430** | — |

**Notes on conservative projections**:
- Assumes 18–25 units/week average (single-printer capacity floor before ordering P2)
- No Etsy Ads spend (organic only); assumes page-2/3 visibility most of the year
- Q4 seasonal lift is modest (desk accessories are not as seasonal as holiday gift items; some lift, but not dramatic)
- No Amazon FBA (organic Etsy only)
- No adjacent products (laser/resin) pursued until Q1 2027

### Break-Even Analysis

**Startup capital**: ~$550 (printer + filament kit + packaging supplies + Etsy setup)
**Payback period**: First 30 days (single-printer operation is cash-positive from the first order)
**Monthly break-even units to cover operating overhead**: 16 units (~$440 gross profit at $27.50 AOV, $8.92 COGS)

**Monthly net profit at different utilization levels**:

| Weekly Units | Monthly Units | Monthly Gross | Monthly COGS | Net Profit | Margin |
|---|---|---|---|---|---|
| 10 | 40 | $1,100 | $440 | $660 | 60% |
| 15 | 60 | $1,650 | $660 | $990 | 60% |
| 20 | 80 | $2,200 | $880 | $1,320 | 60% |
| 25 | 100 | $2,750 | $1,100 | $1,650 | 60% |

**Single-printer operation is viable indefinitely at 15–25 units/week** because monthly net profit ($990–$1,650) is sustainable for a solo operator working 8–12 hours/week.

### Risk Assessment

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Etsy growth plateaus below 10 units/week | Medium | Low (operation is still profitable, just slow) | Improve SEO, test Etsy Ads ($1/day), add new SKU (headphone hooks, rail variants) |
| Seasonal Q4 lift does not materialize | Low | Moderate (-$2,000 vs. projection) | Offset with holiday bundle listings and gift-wrapping option in September |
| Competitor enters "cable clip 3D printed" niche on Etsy | Medium | Moderate (-30% traffic, need reviews to compete) | Get to 50+ reviews by October; accelerate laser engraving SKU to differentiate |
| Filament price surge (tariff shock) | Low | Low (filament is 5% of COGS; $0.02–0.04/unit impact) | None required; margins absorb cost increase |
| Single printer failure (nozzle, bed plate) | Low-Medium | Moderate (3–7 day downtime; lost revenue ~$500–1,000) | Pre-stocked consumables kit; can run repairs on evenings/weekends without revenue loss |

### Decision Gates — When to Escalate to Standard Scenario

**If any of these conditions are met by August 31, 2026, escalate to Standard scenario**:
1. Sustained 25+ units/week for 3 consecutive weeks (indicates demand >single-printer capacity)
2. Cumulative revenue hits $2,500 by August 31 (on track for $10K+ annual run-rate)
3. Etsy shop reaches 20+ reviews with average rating >4.8 stars (strong algorithm signal)
4. Bureau laser engraving consistently generates 10+ orders/month with positive ROI (indicates premium buyer segment is real)

**If none of these gates are met by October 31, remain in Conservative scenario through end of 2026.**

---

## Part 2: Standard Scenario — 2-Printer Q3 Ramp + Laser Validation

### Scenario Definition

**Phase 1 outcome**: Etsy launch generates **$1,500–$3,500 cumulative revenue by June 30** (45–140 orders, 5–15 reviews). Organic traffic is steady; conversion rate 2–3.5%; active optimization on keyword ordering and bundle listings.

**Strategic response**: Order Printer 2 immediately (late June). Execute 2-printer cluster operation by August. Validate laser engraving via bureau route through September; if demand justifies, purchase xTool S1 in October for in-house engraving.

### Capital Plan

**Phase 2A: July–August (2-Printer ramp)**

| Item | Cost | Timing | Trigger |
|---|---|---|---|
| Bambu P1S (Printer 2) | $399 | Early July | Phase 1 hits 30+ units/week sustained |
| Bambu Farm Manager software | $0 | July | Free, once P2 arrives |
| SimplyPrint Starter | $10/month | August (optional) | Launch when printers reach 2+ |
| Filament safety stock increase (3-week buffer for 2 printers) | $75 | July | Offset against reduced per-unit material cost |
| Dedicated 20A circuit electrical (if needed) | $0–250 | August | Check existing circuit load; likely not needed for 2 P1S |
| **Subtotal: Printer 2 & logistics** | **$399–724** | **July–August** | — |

**Phase 2B: August–October (Laser validation + infrastructure)**

| Item | Cost | Timing | Trigger |
|---|---|---|---|
| Bureau laser engraving (50-unit batches) | $100–150/batch | August-September | 2+ batches at $50–75 each to validate demand |
| Acrylic label bureau cutting (10–20 sets) | $50–100 | September | Same bureau provider, consolidate shipping |
| **Optional early**: xTool S1 40W laser engraver | $1,899 | October | Only if bureau demand exceeds 100 units/month cumulative |
| **Optional**: LightBurn software | $60 | October | Required if purchasing xTool S1 |
| **Subtotal: Laser pathway (bureau only)** | **$150–250** | **Aug–Sep** | — |
| **Subtotal: Laser pathway (laser purchase)** | **$2,009–2,059** | **Oct** | **Conditional on demand validation** |

### Revenue & Profitability Projections

**Monthly run-rate assumptions**:

The inflection point is early July (Printer 2 arrival). Before that, single-printer phase applies. After:

| Month | Operating State | Capacity | Demand Est. | Gross Revenue | COGS + OH | Net Profit | Cumulative |
|---|---|---|---|---|---|---|---|
| June | 1 printer, solo | 40 units | 25 units | $688 | $310 | $378 | $378 |
| July | 1→2 printer transition | 80 units | 40 units | $1,100 | $480 | $620 | $998 |
| August | 2 printers, bureau laser | 80 units | 60 units | $1,650 | $720 | $930 | $1,928 |
| September | 2 printers, laser validation | 80 units | 75 units | $2,063 | $900 | $1,163 | $3,091 |
| October | 2 printers ± xTool S1 decision | 80 units | 80 units | $2,200 | $1,000 | $1,200 | $4,291 |
| November | 2–3 printers (if P3 ordered Sep) | 120–160 units | 120 units | $3,300 | $1,500 | $1,800 | $6,091 |
| December | 2–3 printers, Q4 peak | 120–160 units | 160 units | $4,400 | $1,900 | $2,500 | $8,591 |
| Jan–Dec 2026 Total | — | — | **~930 units** | **$25,600** | **$11,400** | **$14,200** | — |

**Sensitivity: If laser in-house by October**

If xTool S1 acquired in October and laser revenue ramps:

| Month | Gross Revenue (with laser) | Incremental Gross | Net Profit (with laser) |
|---|---|---|---|
| October | $2,600 (clips + engraved) | +$400 | $1,400 |
| November | $4,000 (2 printer + laser) | +$700 | $2,200 |
| December | $5,200 (2 printer + laser + Q4) | +$800 | $2,900 |

**Full-year estimate with laser**: $26,500–28,500 gross, $15,000–17,000 net (before tax/owner draw)

### Break-Even Analysis

**Total upfront capital (Printer 2 + electronics + optional laser)**: $399–$2,059 (depending on laser decision)

**Printer 2 payback period**:
- Hardware cost: $399
- Incremental gross profit per unit: $18.58 (same as single-printer)
- Payback at 60 units/month: **3–4 weeks**

**xTool S1 laser payback period** (if purchased October):
- Hardware cost: $1,899 + $60 (LightBurn) = $1,959
- Gross profit per engraved unit: $25–35 (depending on pricing; assume $30 conservative)
- Breakeven units: 66 units engraved
- At 100 units/month throughput: **3–4 weeks payback**

### Multi-Unit Economics

**2-printer operation at full utilization (80 units/week)**:

| Metric | Value |
|---|---|
| Monthly units (realistic demand) | 80–120 |
| Monthly gross revenue | $2,200–$3,300 |
| Monthly COGS + overhead | $1,000–$1,500 |
| Monthly net profit | $1,200–$1,800 |
| Gross margin | 69.9% |
| Cash flow post-tax (est. 25% effective) | $900–$1,350/month |

This is a **sustainable solo-operator+ part-time contractor setup**. If labor is not yet introduced (still solo), all $1,200–$1,800 net flows to the operator. At this run-rate, hiring a 10 hr/wk contractor at $15/hr ($600/month) is optional but increases throughput to 120–160 units/week.

### Risk Assessment

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Printer 2 ordered too early; demand stalls at 20 units/week | Medium | Moderate ($400 sunk, P2 sits idle 1–2 months) | Only order P2 after 2-week confirmation of 30+ units/week; use July analytics to validate gate |
| Laser bureau ROI poor (demand <50 units/month) | Low-Medium | Low ($150–250 sunk, delay in-house laser purchase) | Do not commit to xTool S1 until cumulative bureau engraved orders exceed 150 units |
| Competitor laser-engraved cable clips enter Etsy before ModRun acquires xTool | Medium | Moderate (-15% revenue impact if first-mover advantage lost) | Move laser purchase to August (instead of October) if competitive threat emerges; margins justify faster acquisition |
| Etsy algorithm downrank in September (search visibility drops) | Low-Medium | Moderate (-25% traffic, requires Ads spend to recover) | Have $10–20/day Ads budget ready in September; target ROAS >2.5× to justify continued spend |
| Q4 seasonal demand disappoints (only $2,000 instead of $4,000+) | Low | Moderate (-15–20% annual profit) | Offset with gift bundle listings, holiday packaging option, custom engraving gift cards in October |

### Decision Gates — When to Escalate to Aggressive Scenario

**If any of these conditions are met by September 15, 2026, escalate to Aggressive scenario** (add Printer 3 immediately):

1. 2-printer cluster running >80% utilization for 3 consecutive weeks in September
2. Cumulative revenue (6-month) exceeds $5,000 by September 1 (on pace for $25K+ annual)
3. Bureau laser engraving exceeds 100 units/month cumulative by early September
4. Daily order volume averages >15 units/day in September (indicates demand >>2-printer capacity)

**If none of these gates are met by October 1, remain in Standard scenario through end of 2026.**

---

## Part 3: Aggressive Scenario — 3-Printer Q2/Q3 + Laser + Amazon FBA

### Scenario Definition

**Phase 1 outcome**: Etsy launch generates **$3,000+ cumulative revenue by June 30** (120+ orders, 15+ reviews with >4.8 rating). Organic traffic is strong; conversion rate 3–5%; product-market fit signals clear; early repeating customers.

**Strategic response**: Execute rapid 3-printer deployment in July–August. Order Printer 3 by late July. Acquire xTool S1 laser in July/August (not October). Onboard Amazon FBA in September with pre-staged inventory. Plan Printer 4 acquisition in Q4 if revenue sustains.

### Capital Plan

**Phase 2A: June–July (Immediate Printer 2 + Printer 3 decision)**

| Item | Cost | Timing | Trigger |
|---|---|---|---|
| Bambu P1S (Printer 2) | $399 | Early July | Phase 1 hits 30+ units/week |
| Bambu P1S (Printer 3) | $399 | Late July | Phase 1 hits 50+ units/week by mid-July |
| Bambu Farm Manager + SimplyPrint | $10/month | July | Mandatory at 3+ printers |
| Filament safety stock (4-week buffer, 3 printers) | $150 | July | Offset cost with bulk pricing |
| Dedicated 20A circuit electrical (required at 3 printers) | $200–300 | July-August | Install before Printer 3 arrives |
| **Subtotal: Printers 2–3 & infrastructure** | **$1,348–1,448** | **July–Aug** | — |

**Phase 2B: July–August (Laser equipment acquisition)**

| Item | Cost | Timing | Trigger |
|---|---|---|---|
| xTool S1 40W laser engraver | $1,899 | July-August | Bureau validation meets 50+ units/month by early July |
| LightBurn software | $60 | July | Concurrent with xTool purchase |
| Acrylic material (3mm cast acrylic sheets, 4×8ft) | $80–120 | August | 2–3 sheets for label panel inventory |
| **Subtotal: Laser pathway** | **$2,039–2,079** | **Jul–Aug** | — |

**Phase 2C: August–September (Amazon FBA + infrastructure)**

| Item | Cost | Timing | Trigger |
|---|---|---|---|
| Amazon Seller Central account setup (free) | $0 | August | Begin registration in August for September shipment |
| FBA inventory prep (50–100 units per SKU × 3 SKU) | $750–$1,200 | August-September | FNSKU labels, packaging, box prep; cost absorbed in COGS |
| Initial FBA shipment to Amazon warehouse | $50–100 | September | Freight/labeling to bring inventory into FBA |
| Polymaker wholesale account MOQ trial | $500 | September | 25kg bulk filament order (not true MOQ; skip full $1,000 MOQ at this stage) |
| **Subtotal: FBA + supply chain** | **$1,300–$1,800** | **Aug–Sep** | — |

**Total Phase 2 Aggressive capex**: **$4,687–$5,327** over July–September

### Revenue & Profitability Projections

**Monthly run-rate assumptions**:

Aggressive scenario assumes continuous demand escalation without stalls. Actual execution requires flawless operations.

| Month | Operating State | Printers | Capacity (units) | Demand Est. | Gross Revenue | COGS + OH | Net Profit | Cumulative |
|---|---|---|---|---|---|---|---|
| June | 1 printer, solo | 1 | 40 | 25 | $688 | $310 | $378 | $378 |
| July | Printer 2 arrival; laser eval | 2 | 80 | 50 | $1,375 | $600 | $775 | $1,153 |
| August | Printer 3 arrival; laser inhouse | 3 | 120 | 85 | $2,338 | $1,050 | $1,288 | $2,441 |
| September | 3-printer cluster, FBA live | 3 | 120 | 110 | $3,025 | $1,400 | $1,625 | $4,066 |
| October | 3-printer cluster, FBA ramp | 3 | 120 | 130 | $3,575 | $1,700 | $1,875 | $5,941 |
| November | Printer 4 arrives; Q4 prep | 4 | 160 | 150 | $4,125 | $2,000 | $2,125 | $8,066 |
| December | 4-printer cluster, Q4 peak | 4 | 160 | 180 | $4,950 | $2,400 | $2,550 | $10,616 |
| Jan–Dec 2026 Total | — | 1–4 | — | **~1,135 units** | **$34,176** | **$15,140** | **$19,036** | — |

**Revenue mix (Aggressive scenario, by month 12)**:
- Etsy (FDM clips + rails): ~$3,000/month (50% of total)
- Etsy (laser engraved): ~$1,500/month (25%)
- Amazon FBA: ~$1,500/month (25%)

### Break-Even Analysis

**Total upfront capital for Phase 2**: $4,687–$5,327

**Payback timeline**:
- Printer 2 ($399): Payback in 3–4 weeks from order date (late July) → net positive by mid-August
- Printer 3 ($399): Payback in 2–3 weeks from order date (late July) → net positive by early August
- xTool S1 ($1,959): Payback at 66 units engraved (~2.5 weeks at 100+ units/month) → payback by end of August
- **Total capital recovered**: By **end of September 2026** (3 months from start of escalation)

**Monthly cash position (post-payback)**:

| Metric | August | September | October | November | December |
|---|---|---|---|---|---|
| Gross profit | $1,288 | $1,625 | $1,875 | $2,125 | $2,550 |
| Operating costs | $300 | $400 | $500 | $800 | $1,200 |
| Equipment depreciation | $120 | $120 | $120 | $160 | $160 |
| **Unencumbered cash flow** | **$868** | **$1,105** | **$1,255** | **$1,165** | **$1,190** |

After July–August equipment payback, the operation generates $868–$1,255/month in unencumbered cash flow for 7+ months.

### Multi-Unit Economics at 3-Printer Operation

**Full utilization: 120 units/week**

| Metric | Value | Notes |
|---|---|---|
| Monthly units (sustained demand) | 480 | 4 weeks × 120 units/week |
| Monthly gross revenue (blended: 60% Etsy FDM, 25% Etsy laser, 15% FBA early) | $3,300–$4,000 | At $27.50 AOV average across channels |
| Monthly COGS + overhead | $1,500–$1,800 | Labor, electricity, filament, packaging, platform fees |
| Monthly net profit (operating) | $1,500–$2,200 | Before tax |
| Gross margin | 68.6–70.9% | Consistent across scales |
| Equipment payback (all capex) | 3–4 months | See timeline above |

### Risk Assessment — Aggressive Scenario

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Demand does not materialize; Phase 1 < $3K signal was false spike | Medium-High | Critical ($4,700 capex deployed too early; 2–3 months of idle printer capacity) | Do not commit to Printer 3 or laser before **cumulative June revenue exceeds $2,500**. Execute Printer 2 first; assess in mid-July before Printer 3 order |
| Etsy algorithm downrank in July-August | Medium | Moderate (-40% organic traffic; Ads spend required to maintain demand) | Budget $200–300/month for Etsy Ads July–September if algorithm stalls organic |
| Amazon FBA requires 60+ days to activate (slower onboarding than expected) | Low-Medium | Moderate (delayed FBA revenue; must carry additional Etsy inventory capacity) | Begin FBA registration in June, not August; stage inventory by early September |
| Printer failure (or >1 nozzle issue) during Q3 ramp | Low-Medium | Moderate (3–7 day downtime; lost revenue $1,000–$2,000; Printer 3 acts as redundancy) | Stock consumables kit ($90/printer); Printer 3 provides capacity buffer |
| Laser demand falls short (only 50 units/month instead of 200+) | Low-Medium | Moderate ($1,959 ROI extends to 6+ months instead of 2–3 months) | Have fallback plan: laser operates at 50–75 units/month; still positive ROI at 4–5 month payback |
| Cannibalizing FBA revenue w/ Etsy (same customer buying from both channels) | Low | Low (net revenue same; platform fees differ) | Use FBA for different SKU mix (bundles, bulk packs); Etsy for individual/premium items |
| Operating cash strain if growth is real but Q3 cash is tied up in inventory | Low | Moderate (must pre-buy filament, acrylic, FNSKU labels; $1,000+ tied up) | Maintain $2,000 cash buffer before beginning aggressive capex; can fund from June-July profit |

### Decision Gates & Escalation Criteria

**Aggressive scenario is highest-risk path. Commit only if both conditions are met by June 30**:

1. Cumulative Phase 1 revenue **≥$3,000**
2. Etsy shop has **≥15 reviews** with **average rating ≥4.7 stars**

**If revenue is $2,000–$3,000 but reviews are <15, escalate to Standard scenario instead.**

**If either gate is not met, default to Conservative scenario.**

---

## Part 4: Comparative Risk/Return Profile

### Decision Matrix

Use this matrix to select scenario on June 30 based on Phase 1 outcomes:

```
                    PHASE 1 CUMULATIVE REVENUE (June 30)
                    <$1,000          $1,000–$3,000      $3,000+
ETSY REVIEWS
    <10 reviews     CONSERVATIVE     CONSERVATIVE       STANDARD
    10–15 reviews   CONSERVATIVE     STANDARD           STANDARD
    15+ reviews     STANDARD         STANDARD           AGGRESSIVE
```

### Scenario Comparison: Payback & ROI

| Metric | Conservative | Standard | Aggressive |
|---|---|---|---|
| **Total capex (Phase 2)** | $399–779 | $399–2,059 | $4,687–5,327 |
| **Payback period** | 8–12 weeks | 4–8 weeks | 12–16 weeks (spread) |
| **Monthly net profit (month 12)** | $1,200–$1,800 | $1,800–$2,500 | $2,000–$2,800 |
| **Annual net profit (2026, est.)** | $7,400–$9,500 | $14,200–$17,000 | $19,000–$24,000 |
| **Capital efficiency (ROI @ month 12)** | 18–24× annualized | 11–16× annualized | 5–8× annualized |
| **Risk if demand stalls** | Low (small capex sunk) | Medium ($400–2,000 sunk) | High ($4,700 sunk) |

### Upside Variance Analysis

**If all scenarios execute perfectly AND demand exceeds projections:**

| Scenario | Base Case (month 12 net) | Upside Case (20% demand beat) | Ceiling Case (40% demand beat) |
|---|---|---|---|
| Conservative | $8,500 | $10,200 | $11,900 |
| Standard | $15,600 | $18,720 | $21,840 |
| Aggressive | $21,000 | $25,200 | $29,400 |

**Upside is driven entirely by demand, not by unit economics improvement.** All scenarios converge on 68.6–70.9% gross margin regardless of scale. Printer additions and labor costs nearly offset bulk filament savings.

### Downside Risk Analysis

**If demand disappoints by 30% below projection:**

| Scenario | Base Case | Downside Case | Impact on Payback |
|---|---|---|---|
| Conservative | $8,500 | $5,950 | Still profitable; payback unchanged |
| Standard | $15,600 | $10,920 | Extends payback 6–8 weeks; still positive |
| Aggressive | $21,000 | $14,700 | Payback extends to 5–6 months; stress on cash flow |

**Conservative maintains profitability at any demand level >10 units/week.**
**Aggressive requires sustained demand >80 units/week to avoid negative cash flow in month 3–4.**

---

## Part 5: Decision Framework & Next Steps

### Phase 1 Decision Date: June 30, 2026

**Actions on June 30**:

1. **Pull Etsy analytics**: Cumulative revenue, order count, shop visits, conversion rate, average reviews
2. **Assess reviews**: Total count, average rating (target >4.7 stars)
3. **Cross-reference cost model**: Validate COGS assumptions against actual orders (print time, weight)
4. **Execute scenario selection** using the matrix in Part 4

### Implementation Timeline by Scenario

**Conservative Path**:
- July 1: Publish "Phase 2A: Optimizing Conversion" post in project notes
- July–August: Focus on SEO, photo improvements, 1–2 new SKU variants via CAD
- September: Assess for Standard scenario escalation gate
- Q4: Minor bureau services if demand supports

**Standard Path**:
- July 1–5: Order Printer 2 if not already ordered
- July 15: Farm Manager live; SimplyPrint enabled
- August 1: Begin bureau laser validation (50-unit batch to SendCutSend)
- October 1: Laser decision gate (purchase xTool S1 if >100 cumulative engraved units)
- Q4: Optional Printer 3 if revenue sustains >$5K/month

**Aggressive Path**:
- July 1–5: Order Printers 2 and 3 immediately
- July 15: Electrical upgrade (20A circuit) in-progress
- August 1: xTool S1 arrives; laser operations live
- August 15: Amazon FBA inventory prep begins
- September 1: FBA shipment to Amazon warehouse
- October 1: Printer 4 decision gate (order if 3-printer cluster >80% utilization)

### Exit Criteria & Fallback Options

**If any scenario underperforms**:

| Scenario | Underperformance Signal | Fallback Action |
|---|---|---|
| Conservative | Demand <10 units/week in Q3 | Pivot to bundle offerings; test $3 discount on Etsy |
| Standard | Printer 2 idle >50% in September | Hold Printer 3 decision; focus Ads spend on Etsy conversion |
| Aggressive | Demand <80 units/week by September 15 | Pause Printer 4; redirect capital to marketing (Etsy Ads, product photography) |

**Recovery path**: Any scenario can downgrade to the next-slower scenario without capital loss. The cost is opportunity (time) not cash.

---

## Appendix: Key Assumptions & Confidence Notes

### Core Assumptions

1. **Unit economics stable across scales** (68.6–70.9% gross margin)
2. **Phase 1 traction indicators are predictive** (revenue = demand elasticity signal)
3. **Printer acquisition timeline realistic** (5–10 day lead time from order to delivery)
4. **Payback models assume demand matches capacity utilization** (conservative; actual payback may be faster)
5. **Labor not introduced until revenue >$5K/month** (solo operation through Q3)
6. **Etsy platform remains default channel** (not overshadowed by Amazon or TikTok Shop)

### Known Unknowns

1. **Actual Etsy conversion rate** for cable management accessories (will be known June 15–20)
2. **Repeat customer rate** (impacts cumulative revenue acceleration or decay)
3. **Amazon FBA fee tier** for ModRun products (dependent on product dimensions; affects channel margin)
4. **Seasonal demand curve** for desk organization (unvalidated; could be +50% or -20% vs. baseline)
5. **Competitor response timeline** (first copy-cat "laser engraved cable clips" may enter market July–August)

### Confidence Levels

- **Conservative scenario**: 90% confidence (low capex, demand-insensitive)
- **Standard scenario**: 75% confidence (2-printer operations proven; laser demand uncertain)
- **Aggressive scenario**: 60% confidence (compounds uncertainties; high capex deployment bet)

---

## Summary Decision Rules

**Pick CONSERVATIVE if**:
- Phase 1 cumulative revenue <$1,500
- Etsy shop has <10 reviews by June 30
- Conversion rate <1.5%
- *Rationale*: Market validation incomplete; capital discipline required

**Pick STANDARD if**:
- Phase 1 cumulative revenue $1,500–$3,000
- Etsy shop has 10–15 reviews with 4.7+ rating
- Conversion rate 2–3%
- *Rationale*: Validated demand; 2-printer operation justified; measured expansion

**Pick AGGRESSIVE if**:
- Phase 1 cumulative revenue >$3,000
- Etsy shop has 15+ reviews with 4.8+ rating
- Conversion rate 3–5%
- *Rationale*: Clear product-market fit; rapid scaling justified despite capital risk

**If uncertain between two scenarios, default to the slower scenario.** The upside variance from Conservative to Standard is 2–3×; the cost of being wrong is far higher in Aggressive scenario.
