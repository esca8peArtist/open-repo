---
title: "Channel Pricing Calculator — ModRun Cable Clip"
project: mfg-farm
created: 2026-06-28
status: execution-ready
trigger: "Use when setting list prices; re-run if COGS inputs change (filament cost, shipping rate)"
confidence: 92%
verified-nets:
  etsy: "$25.79/sale at $28.99 list price (PHASE_2_TRACK_3_MARKET_EXPANSION_RESEARCH.md)"
  amazon-fba: "$21.23/sale at $28.99 list price (PHASE_2_TRACK_3_MARKET_EXPANSION_RESEARCH.md)"
revenue-target: "$500/month Phase 1"
related:
  - PHASE_2_TRACK_3_MARKET_EXPANSION_RESEARCH.md
  - PRICING_CALCULATOR.md
  - Cost_Model_May2026_Validation.md
  - CHANNEL_COMPARISON_MATRIX.md
---

# Channel Pricing Calculator — ModRun Cable Clip

**How to use this file**: The tables in Parts 2 and 3 are pre-filled — all you need to do is pick a price point and read off the net. Part 4 covers color variant premium modeling (for when the test print passes with multiple color options). Part 5 is the breakeven analysis for the $500/month Phase 1 revenue target.

**Verified baseline numbers** (from PHASE_2_TRACK_3_MARKET_EXPANSION_RESEARCH.md, June 28, 2026):
- Etsy net at $28.99 list price: **$25.79**
- Amazon FBA net at $28.99 list price: **$21.23**
- These are the pre-COGS nets (fees only deducted). COGS at standard PLA+ weight reduces net further — see Parts 2 and 3.

---

## Part 1: COGS Inputs

These inputs feed every calculation in this file. Update them if your actual costs differ.

### Filament

| Input | Value | Source |
|-------|-------|--------|
| PLA+ cost per kg (Phase 1) | $13.50/kg | Cost_Model_May2026_Validation.md, May 17 2026 |
| PLA+ cost per gram | $0.0135/g | $13.50 ÷ 1,000 |
| Scrap/failure allowance | 8% (first 100 units); 5% thereafter | Apply as multiplier to filament cost |
| Bulk rate (10kg+, Phase 2) | $0.019/g | Once volume justifies |

### Per-Pack Print Weight (Estimate — update from actual test print)

| Pack | Print Weight (est.) | Filament Cost |
|------|--------------------|--------------------------------------------|
| 3-pack (C-01) | 14g | 14 × $0.0135 × 1.08 (scrap) = **$0.20** |
| 4-pack | ~18g | 18 × $0.0135 × 1.08 = **$0.26** |
| 8-pack | ~36g | 36 × $0.0135 × 1.08 = **$0.52** |
| 12-pack + rail | ~200g | 200 × $0.0135 × 1.08 = **$2.92** |

**Important**: Weigh your actual test print on a postal scale. Slicer estimates are ±5% off actual. Use the real weight for every calculation.

### Machine Time

| Input | Value | Breakdown |
|-------|-------|-----------|
| Machine cost per hour (Bambu P1S) | $0.28/hr | $0.08 depreciation ($399, 5,000-hr life) + $0.17 electricity (150W × $0.12/kWh) + $0.03 wear parts |
| Print time per 3-pack (C-01) | 0.55 hrs | From Bambu Studio slicer |
| Machine cost per 3-pack | **$0.15** | 0.55 × $0.28 |
| Print time per 8-pack | ~1.1 hrs (estimate) | [Update from slicer] |
| Machine cost per 8-pack | ~$0.31 | [Update from slicer] |

### Packaging

| Item | Cost | Notes |
|------|------|-------|
| Poly mailer (6×9", 2.5mil) | $0.08 | Buy in 200-packs |
| Tissue paper | $0.05 | One sheet per order |
| Thank-you/business card insert | $0.08 | VistaPrint 500-pack ~$40 |
| Tape | $0.07 | Prorated per unit |
| **Total packaging per order** | **$0.28–$0.80** | Depends on pack size; use $0.50 as planning number |

### Shipping (Seller-Absorbed — Free Shipping Model)

| Package Weight | USPS Ground Advantage (Pirateship) | Notes |
|----------------|-----------------------------------|-------|
| Under 4 oz (3-pack or 4-pack) | $4.10–$4.55 | 8% surcharge active through Jan 2027 |
| 4–8 oz (8-pack) | $4.75–$5.00 | Most common order weight |
| 8–12 oz (12-pack) | $5.25–$5.75 | |
| 12–16 oz (12-pack + rail) | $5.75–$6.25 | Rail adds significant weight; verify on scale |

**Use $5.00 as the standard planning assumption** for the 8-pack (the anchor SKU). Free shipping is required — Etsy's 2026 algorithm actively demotes listings charging above $6 for shipping.

---

## Part 2: Etsy Net Margin Calculator

### Fee Formula

```
Etsy fees per sale:
  Transaction fee:       List price × 6.5%
  Payment processing:    List price × 3.0% + $0.25
  Listing fee:           $0.20 (per-sale auto-renewal)
  Total Etsy fees:       List price × 9.5% + $0.45

Net to seller (before COGS):
  Net = List price × (1 - 0.095) - $0.45

Net after all costs (COGS included):
  Net = List price - Etsy fees - Shipping (absorbed) - Materials - Machine cost - Packaging
```

### Pre-Filled Etsy Net Table

All prices include free shipping (absorbed by seller). COGS excludes labor — see labor note below.

| Pack | List Price | Etsy Fees | Shipping | Materials + Machine | Packaging | Net (ex-labor) | Gross Margin |
|------|------------|-----------|----------|--------------------|-----------|----|------|
| 3-pack (C-01) | $12.99 | $1.68 | $4.25 | $0.35 | $0.35 | **$6.36** | 49% |
| 3-pack (post-review) | $14.99 | $1.87 | $4.25 | $0.35 | $0.35 | **$8.17** | 54% |
| 4-pack | $16.99 | $2.06 | $4.50 | $0.50 | $0.45 | **$9.48** | 56% |
| 8-pack | $19.99 | $2.35 | $5.00 | $0.83 | $0.55 | **$11.26** | 56% |
| 8-pack (raised) | $24.99 | $2.82 | $5.00 | $0.83 | $0.55 | **$15.79** | 63% |
| 12-pack + rail (system) | **$28.99** | **$3.20** | **$6.00** | **$3.07** | **$0.70** | **$15.98** | **55%** |
| System bundle (20 clips + 2 rails) | $38.99 | $4.25 | $6.00 | $5.14 | $0.80 | **$22.80** | 58% |

**The $25.79 verified Etsy net** (from PHASE_2_TRACK_3_MARKET_EXPANSION_RESEARCH.md) is the pre-COGS net on a $28.99 sale. Post-COGS at the system bundle tier ($28.99 list), the true net excluding labor is ~$15.98 — the difference is the $9.81 in combined COGS (shipping + materials + machine + packaging).

The $25.79 figure is correct as a fees-only net. Use it for cross-channel fee comparison. Use the post-COGS figures above for actual margin decisions.

**Labor note**: The table excludes an explicit labor cost. Estimated time per order: 15 minutes (print setup, QC, packaging, label). At $20/hr opportunity cost, labor is $5.00/order. Deduct $5.00 from each "Net (ex-labor)" figure for the fully-loaded true margin.

| Pack | Net (ex-labor) | Net (at $20/hr labor) |
|------|---------------|----------------------|
| 3-pack at $12.99 | $6.36 | $1.36 |
| 3-pack at $14.99 | $8.17 | $3.17 |
| 8-pack at $19.99 | $11.26 | $6.26 |
| System bundle at $28.99 | $15.98 | $10.98 |
| System bundle at $38.99 | $22.80 | $17.80 |

**Implication**: The 3-pack at $12.99 with labor included is a review-velocity tool, not a profit center. Switch to 8-pack or system bundle as the primary SKU after 15 reviews.

---

## Part 3: Amazon FBA Pricing

### Fee Formula

```
Amazon FBA fees per sale:
  Referral fee:           List price × 15.0%
  FBA fulfillment fee:    $3.41 (small standard, under 12 oz, including 3.5% April 2026 surcharge)
  Total Amazon fees:      (List price × 0.15) + $3.41

Net to seller (before COGS, FBA handles shipping):
  Net = List price - (List price × 0.15) - $3.41

Net after all costs (COGS, no shipping — FBA handles it):
  Net = List price - Amazon fees - Materials - Machine cost - Packaging
```

### Pre-Filled Amazon FBA Net Table

FBA handles shipping — seller ships bulk inventory to Amazon warehouse, pays inbound shipping once, then FBA delivers individual orders. No per-order shipping cost for FBA.

| Pack | List Price | Amazon Fees (15%) | FBA Fee | Materials + Machine | Packaging | Net (ex-labor) | Gross Margin |
|------|------------|-------------------|---------|--------------------|-----------|----|------|
| 3-pack | $15.99 | $2.40 | $3.41 | $0.35 | $0.50 | **$9.33** | 58% |
| 4-pack | $18.99 | $2.85 | $3.41 | $0.50 | $0.50 | **$11.73** | 62% |
| 8-pack | **$22.99** | **$3.45** | **$3.41** | **$0.83** | **$0.60** | **$14.70** | **64%** |
| 12-pack + rail (system) | **$28.99** | **$4.35** | **$3.41** | **$3.07** | **$0.80** | **$17.36** | **60%** |
| System bundle (20 clips + 2 rails) | $38.99 | $5.85 | $3.56 | $5.14 | $0.90 | **$23.54** | 60% |

**The $21.23 verified Amazon FBA net** (from PHASE_2_TRACK_3_MARKET_EXPANSION_RESEARCH.md) is the pre-COGS net on a $28.99 sale. Post-COGS, the system SKU at $28.99 nets ~$17.36 (before labor). The $4.56 Etsy-vs-Amazon gap at the fees level ($25.79 vs. $21.23) narrows post-COGS because FBA eliminates the per-order shipping cost (~$5–6) that Etsy sellers absorb.

**Amazon vs. Etsy post-COGS comparison at $28.99 system SKU**:

| | Etsy | Amazon FBA | Difference |
|-|------|-----------|------------|
| Net (pre-COGS, fees only) | $25.79 | $21.23 | Etsy +$4.56 |
| Net (post-COGS, ex-labor) | $15.98 | $17.36 | Amazon FBA +$1.38 |
| Net (post-COGS, at $20/hr labor) | $10.98 | $12.36 | Amazon FBA +$1.38 |

Amazon FBA actually nets marginally more than Etsy post-COGS at the system SKU because the $3.41 FBA fee is cheaper than the $6.00 USPS shipping the Etsy seller absorbs. The frame is additive revenue, not substitution. Run both channels at comparable volumes for maximum combined yield.

### Amazon FBA Launch Capital Requirements

| Item | Cost |
|------|------|
| First FBA batch (50 units) | $40.50 (50 × $0.81 COGS ex-labor) |
| Inbound shipping to FBA warehouse | $15–25 (varies by warehouse location assigned) |
| New Selection Program exemption (first 100 units) | $0 inbound placement fee |
| Sponsored Products PPC (first 30 days) | $100–200 recommended |
| **Total Amazon FBA launch capital** | **$155–265** |

**Reorder trigger**: When FBA inventory drops to 15 units (30-day buffer at initial velocity of 0.5 units/day).

---

## Part 4: Color Variant Pricing (Multi-Variant Model)

When the test print passes with multiple colors available (black, white, gray standard; custom on request), use the following pricing structure.

### Base Price vs. Color Premium

| Color | Status | Pricing Model | Notes |
|-------|--------|---------------|-------|
| Matte Black | Standard | Base price — no premium | Default launch color |
| Matte White | Standard | Base price — no premium | Launch simultaneously with black |
| Gray | Standard | Base price — no premium | Include in color dropdown at launch |
| Custom colors (silk PLA+, wood fill, glow-in-dark) | On request | Base price + $2.00 premium | Add note in description: "Custom colors on request — message before ordering, add $2" |
| Two-color split order (e.g., 4 black + 4 white in 8-pack) | On request | Base price (no premium) | Operationally simple — just sort by color at packing |

**Color variant listing structure on Etsy**:
- Create one listing per pack size (not one per color) — Etsy's variation dropdown handles color selection
- Main listing photo: neutral gray or the most visually appealing color
- Photo slot 7: color flat-lay overhead showing all three standard colors together

**Color variant listing structure on Amazon**:
- Create a parent ASIN for each pack size with child ASINs per color
- Each child ASIN is a separate inventory unit in FBA — plan color ratios based on Etsy color preference data (collect for 30 days before sending FBA batch)
- Expected color split: 50% black, 30% white, 20% gray (desk-setup community aesthetic leans dark matte)

### Color Premium Math

At a $2 premium for custom colors:

| Base Price | Custom Color Price | Additional Net (ex-labor) |
|------------|-------------------|--------------------------|
| $19.99 (8-pack) | $21.99 | +$1.81 (after 10.5% Etsy fees) |
| $28.99 (system) | $30.99 | +$1.81 (after 10.5% Etsy fees) |

Custom color premium is a low-complexity upsell that requires only a filament spool swap and a slightly longer print queue. Implement at launch — do not wait.

---

## Part 5: Breakeven Analysis — $500/Month Revenue Target

### Units Required Per Channel

**Target**: $500/month net revenue (post-COGS, ex-labor)

| Channel | SKU | Net per Unit (ex-labor) | Units Required/Month | Units Required/Week |
|---------|-----|------------------------|---------------------|---------------------|
| Etsy | 3-pack at $14.99 | $8.17 | 62 | 15 |
| Etsy | 8-pack at $19.99 | $11.26 | 45 | 11 |
| Etsy | System at $28.99 | $15.98 | 32 | 8 |
| Amazon FBA | 8-pack at $22.99 | $14.70 | 34 | 9 |
| Amazon FBA | System at $28.99 | $17.36 | 29 | 7 |
| Combined Etsy + Amazon FBA | System at $28.99 on both | $15.98 + $17.36 avg | Split ~16/16 = 32 total | 8 |

**At 20 units/week** (current production capacity at single-printer baseline):

| SKU Mix | Monthly Units | Monthly Net (ex-labor) | Reaches $500/month? |
|---------|--------------|----------------------|---------------------|
| All 3-pack at $12.99 | 87 | $553 | Yes — barely |
| Mix: 50% 3-pack, 50% 8-pack | 87 | $844 | Yes — comfortably |
| All 8-pack at $19.99 | 87 | $980 | Yes — with margin |
| All system bundles at $28.99 | 87 | $1,390 | Well above target |

**Key insight**: At 20 units/week, the $500/month target is reachable at any price point above $12.99 for a 3-pack. The revenue lever is SKU mix — shifting from 3-packs to 8-packs or system bundles doubles monthly net without increasing production volume.

**Recommended SKU prioritization once 15 reviews are achieved**:
1. Lead SKU: 8-pack at $19.99 (best conversion/margin balance, most competitive)
2. Upsell SKU: System bundle at $28.99 (highest net per order; requires Etsy cross-sell)
3. Entry SKU: 3-pack at $14.99 (review-building and gift buyers)

### Revenue Scenarios — Etsy + Amazon Combined

| Scenario | Etsy Units/Mo | Amazon Units/Mo | Etsy Net | Amazon Net | Combined Net | vs. $500 Target |
|----------|--------------|----------------|---------|------------|-------------|----------------|
| Etsy only, 20/week | 87 | 0 | $980 (8-pack) | $0 | $980 | +$480 |
| Etsy 50/mo + Amazon 20/mo (Month 3) | 50 | 20 | $563 | $294 | $857 | +$357 |
| Etsy 50/mo + Amazon 50/mo (Month 6) | 50 | 50 | $563 | $735 | $1,298 | +$798 |
| Etsy 100/mo + Amazon 100/mo (Phase 2) | 100 | 100 | $1,126 | $1,470 | $2,596 | +$2,096 |

**Phase 1 revenue target ($500/month) is achievable on Etsy alone at 20 units/week.** Amazon adds incremental revenue on top — not a substitute for Etsy but a multiplier after Month 2–3.

### Breakeven — Printer Cost Recovery

| Sale Price | Net/Unit (ex-labor, ex-shipping) | Units to Break Even (P1S $399) | Weeks at 20/week |
|------------|----------------------------------|-------------------------------|-----------------|
| $12.99 (3-pack) | $6.36 | 63 units | 3.2 weeks |
| $14.99 (3-pack post-review) | $8.17 | 49 units | 2.5 weeks |
| $19.99 (8-pack) | $11.26 | 35 units | 1.8 weeks |
| $28.99 (system) | $15.98 | 25 units | 1.3 weeks |

At any price point above $12.99, the Bambu P1S cost is recovered within 4 weeks of production. The printer is not the financial risk — demand validation is. Print the test batch first.

### Full Startup Capital Recovery

| Item | Cost |
|------|------|
| Bambu P1S | $399 |
| Initial filament (2kg, 3 colors) | $38 |
| Packaging supplies | $35 |
| Amazon Handmade PPC seed (first 30 days) | $150 |
| **Total startup capital** | **$622** |

At $11.26 net/unit (8-pack, Etsy): $622 ÷ $11.26 = **55 units = 2.8 weeks at 20/week.**

At combined Etsy + Amazon, averaging $13 net/unit: $622 ÷ $13.00 = **48 units = 2.4 weeks.**

---

## Part 6: Price-Raise Decision Rules

Price increases should be milestone-gated, not time-gated.

| Milestone | Action |
|-----------|--------|
| 0 reviews (launch) | Launch 3-pack at $12.99 to maximize review velocity during 14–21 day recency window |
| 15 reviews, 4.8+ average | Raise 3-pack to $14.99; introduce 8-pack at $19.99 |
| 25 reviews | Launch system bundle at $28.99 (this is the $25.79 Etsy net SKU) |
| 50 reviews | Test $34.99 system listing for 14 days; keep $28.99 as primary if conversion drops |
| Star Seller badge (Day ~90) | Price at upper tier without conversion penalty; $28.99 system becomes the lead SKU |
| Amazon live with 10+ reviews | Match or price Amazon $1–3 above Etsy equivalent to account for higher fees |
| Offsite Ads mandatory ($10K+ revenue) | Build the 12% Offsite Ads fee into prices (raise by $3–4) to maintain margin |

---

## Part 7: New Product Fill-In Template

Use this template when pricing any new product beyond the cable clip.

```
PRODUCT NAME: ________________
SKU ID: ________________

--- COGS INPUTS ---
Material type: PLA+ / PETG / ASA / Other: _______
Filament cost per gram: $______ (see Part 1)
Print weight: ______g (from actual test print, postal scale)
Print time: ______hrs (from Bambu Studio slicer)
Machine cost: ______hrs × $0.28 = $______
Hardware BOM (if any):
  Item 1: _________ × ___qty @ $___each = $______
  Item 2: _________ × ___qty @ $___each = $______
Hardware total: $______
Packaging: $______ (standard $0.28–$0.80; adjust for larger items)
Shipping (absorbed): $______ (weigh fully packaged; use USPS First Class rate)
Total COGS: $______

--- ETSY PRICING ---
Floor price (0% margin): COGS ÷ (1 - 0.095) - $0.45 = $______
30% margin target: COGS ÷ (1 - 0.095 - 0.30) = $______
Etsy launch price (competitive range): $______
Post-review price: $______

--- AMAZON FBA PRICING ---
Amazon FBA launch price: Etsy price + $1–3 = $______
FBA fee (verify by weight tier): $______
Amazon net (ex-COGS): List - (List × 0.15) - FBA fee = $______
Amazon net (post-COGS): Amazon net - COGS = $______

--- BREAKEVEN ---
Net per unit at launch price (Etsy): $______
Units to break even on P1S: $399 ÷ net = ______ units
Weeks at 20/week: ______ weeks

--- MARGIN CHECK ---
Gross margin % (ex-labor): net ÷ launch price = ______%
Min acceptable (before Offsite Ads): 35%
Min acceptable (after Offsite Ads at 12%): 40%
Pass / Fail: ______
```

---

## Sources

- Fee structure verification: [PHASE_2_TRACK_3_MARKET_EXPANSION_RESEARCH.md](PHASE_2_TRACK_3_MARKET_EXPANSION_RESEARCH.md) — Part 1 fee table; $25.79 Etsy net / $21.23 Amazon FBA net at $28.99 list price
- COGS inputs: [Cost_Model_May2026_Validation.md](Cost_Model_May2026_Validation.md) — $13.50/kg PLA+ baseline, May 17 2026
- USPS rates: [PHASE_2_TRACK_2_LOGISTICS_OPTIMIZATION.md](PHASE_2_TRACK_2_LOGISTICS_OPTIMIZATION.md) — commercial rates with 8% surcharge through Jan 2027
- Machine cost breakdown: [COMMODITY_PRODUCT_LIBRARY_Q3_2026.md](COMMODITY_PRODUCT_LIBRARY_Q3_2026.md) — P1S depreciation + electricity calculation
- Amazon FBA fee schedule: [amazon-fba-analysis.md](amazon-fba-analysis.md) — small standard tier, April 2026 surcharge included
- Volume scenario data: [PRICING_CALCULATOR.md](PRICING_CALCULATOR.md) — 20–500 unit/week net and margin table
- [Amazon FBA Fees 2026 — AMZ Prep](https://amzprep.com/amazon-fba-fees/)
- [EasyPost USPS Rate Chart 2026](https://www.easypost.com/usps-rate-chart/)
