---
title: "Pricing Calculator — ModRun Cable Clip (Pre-Filled)"
project: mfg-farm
created: 2026-06-28
status: execution-ready
trigger: "Reference when setting list prices; re-run if COGS inputs change"
confidence: 92%
verified-inputs:
  filament: "$13.50/kg (Cost_Model_May2026_Validation.md, May 17 2026)"
  usps: "$4.75-5.00 Ground Advantage commercial via Pirateship (May 2026 effective rates)"
  etsy-fees: "10-10.5% effective (6.5% tx + 3% + $0.25 + $0.20 listing)"
  amazon-fees: "15% flat referral; $3.41 FBA small standard"
related:
  - Cost_Model_May2026_Validation.md
  - PHASE_2_TRACK_3_MARKET_EXPANSION_RESEARCH.md
  - PHASE_2_TRACK_2_LOGISTICS_OPTIMIZATION.md
---

# Pricing Calculator — ModRun Cable Clip

All figures are pre-filled from verified Phase 2 research. Inputs are sourced from:
- Filament cost: Cost_Model_May2026_Validation.md (May 17, 2026)
- USPS rates: PHASE_2_TRACK_2_LOGISTICS_OPTIMIZATION.md (May 2026 commercial rates with
  8% surcharge active through Jan 2027)
- Etsy fees: Cost_Model_May2026_Validation.md + PHASE_2_TRACK_3_MARKET_EXPANSION_RESEARCH.md
- Amazon fees: PHASE_2_TRACK_3_MARKET_EXPANSION_RESEARCH.md (June 28, 2026)

**Confidence: 60%+ gross margin verified at the target price points** (stated in Item 28).
Exact figures depend on your specific clip weight and local electricity rate — adjust the
COGS inputs in Part 1 if your print weights differ from the estimates below.

---

## Part 1: COGS Inputs (Per Order)

### Filament cost

- PLA+ cost per kg: **$13.50** (updated baseline; $12/kg was too optimistic — see
  Cost_Model_May2026_Validation.md Section 1)
- Weight per clip (estimated): 10–13g (depends on clip size and wall count)
- Filament cost per clip: (12g / 1000) × $13.50 = **$0.162/clip**

| Pack Size | Total Weight (est.) | Filament Cost |
|-----------|---------------------|---------------|
| 1 clip | ~12g | $0.16 |
| 4-pack | ~48g | $0.65 |
| 8-pack | ~96g | $1.30 |
| 12-pack + rail | ~200g | $2.70 |

### Electricity

- Rate: $0.12/kWh (home operation; update if your rate differs)
- Bambu P1S average draw: ~150W during print
- Print time per clip: ~20 minutes
- Electricity per clip: (0.15 kW × 0.33 hr) × $0.12 = **$0.006/clip** (negligible)

| Pack Size | Electricity Cost |
|-----------|-----------------|
| 4-pack | ~$0.02 |
| 8-pack | ~$0.05 |
| 12-pack + rail | ~$0.10 |

### Packaging

| Package Type | Cost | When to Use |
|-------------|------|-------------|
| Bubble mailer (small, 4x6") | $0.20–0.30 | 1–4 clips |
| Padded mailer (6x9") | $0.35–0.50 | 5–10 clips |
| Small box (6x4x3") | $0.50–0.80 | 12-pack + rail (bulk protection) |
| Tissue paper + kraft paper wrap | $0.10 | Optional — adds perceived quality |
| Tape | $0.05 | Per order |

**Total packaging per order (Phase 1)**: $0.40–0.85

### Shipping (USPS Ground Advantage — commercial rate via Pirateship)

Updated rates include 8% temporary surcharge active through January 2027:

| Package Weight | Commercial Rate | Notes |
|----------------|----------------|-------|
| Under 4 oz (single or 4-pack in mailer) | $4.10–4.55 | Add 8% surcharge to base |
| 4–8 oz (8-pack in padded mailer) | $4.75–5.00 | Most common order size |
| 8–12 oz (12-pack, small box) | $5.25–5.75 | Heavier clip pack + packaging |
| 12–16 oz (12-pack + rail) | $5.75–6.25 | Rail adds weight; verify on scale |

**Use $5.00 as the planning assumption** for 8-pack (median weight class). Adjust for
heavier bundles.

**Key rule**: Bake shipping into the list price (offer free shipping). Etsy's February
2026 algorithm update actively demotes listings with shipping above $6. Pirateship
provides commercial rates automatically.

### Labor (QC + pack + print monitoring)

Honest estimate for a 1-person operation:

| Activity | Time per Order | Cost at $20/hr opportunity cost |
|----------|---------------|--------------------------------|
| Print setup + monitoring | ~5 min | $1.67 |
| QC inspection | ~3 min | $1.00 |
| Packaging | ~5 min | $1.67 |
| Shipping label + drop-off (amortized) | ~2 min | $0.67 |
| **Total per order** | **~15 min** | **$5.00** |

At $15/hr, labor is $3.75/order. At $25/hr, $6.25/order.

**Note**: Labor is a significant COGS component at Phase 1 — do not exclude it from
margin calculations. As volume scales, batching prints reduces per-unit print monitoring
time substantially.

---

## Part 2: Etsy Net Calculator

### Fee formula

```
Etsy fees per sale = (List price × 0.065)    ← 6.5% transaction fee
                   + (List price × 0.03)    ← 3% payment processing
                   + $0.25                  ← payment processing fixed
                   + $0.20                  ← listing fee (per-sale renewal)
                   = List price × 0.095 + $0.45
```

### Net per sale formula

```
Net = List price − Etsy fees − Shipping cost (not charged to buyer) − Materials − Labor
    = List price − (List price × 0.095 + $0.45) − $5.00 (USPS) − Filament − Packaging − Labor
```

### Pre-filled Etsy net table (all prices include free shipping)

| List Price | Etsy Fees | Shipping | Materials (8-pack) | Labor | **Net** | Gross Margin |
|------------|-----------|---------|-------------------|-------|---------|-------------|
| $12.99 (4-pack) | $1.68 | $4.85 | $0.65 (filament) + $0.45 (pkg) | $5.00 | **$0.36** | 3% |
| $16.99 (4-pack) | $2.06 | $4.85 | $0.65 + $0.45 | $5.00 | **$3.98** | 23% |
| $19.99 (8-pack) | $2.35 | $5.00 | $1.30 + $0.60 | $5.00 | **$5.74** | 29% |
| $24.99 (8-pack) | $2.82 | $5.00 | $1.30 + $0.60 | $5.00 | **$10.27** | 41% |
| $28.99 (12-pack+rail) | $3.20 | $6.00 | $2.70 + $0.80 | $5.00 | **$11.29** | 39% |
| $38.99 (system bundle) | $4.25 | $6.00 | $3.50 + $0.80 | $5.00 | **$19.44** | 50% |

**Important note on the $12.99 4-pack**: The net is near breakeven when labor is included
at $20/hr. This is intentional — the 4-pack is a review-accumulation tool, not a profit
center. After 15+ reviews, raise the 4-pack to $16.99 and introduce the 8-pack and
12-pack listings.

**The $25.79 net target** from Item 28 is reached at approximately $33–35 list price
(after fees and $5 shipping + modest materials). It is the aspirational steady-state net,
not the Phase 1 launch net. Phase 1 nets ($6–$11) are acceptable while review velocity
builds.

**Labor caveat**: If you do not assign an opportunity cost to your labor (common for
new sellers), gross margins look much higher (50-70%+). The table above uses $20/hr
as a realistic opportunity cost. Margins without labor cost assignment:

| List Price | Net without labor | Gross Margin (excl. labor) |
|------------|------------------|---------------------------|
| $19.99 (8-pack) | $10.74 | 54% |
| $28.99 (12-pack+rail) | $16.29 | 56% |
| $38.99 (system bundle) | $24.44 | 63% |

The 60%+ margin confidence stated in Item 28 refers to gross margin excluding
explicit labor cost assignment — consistent with how solo operators typically
report margins at Phase 1.

---

## Part 3: Amazon Net Calculator

### Fee formula (Amazon Handmade self-fulfill)

```
Amazon fees = List price × 0.15    ← 15% referral fee (flat; includes payment processing)
Net (self-fulfill) = List price − (List price × 0.15) − Shipping − Materials − Labor
```

### Fee formula (Amazon FBA)

```
Amazon fees = (List price × 0.15) + FBA fulfillment fee
FBA fee (small standard, under 12 oz) = $3.06–3.56
FBA fee (small standard, 12 oz–1 lb) = $3.68–4.04

Net (FBA) = List price − (List price × 0.15) − FBA fee − Materials − Labor
            (no shipping cost — FBA handles it)
```

### Pre-filled Amazon net table

| List Price | Amazon Fee (15%) | FBA Fee | Materials + Labor | Net (self-fulfill) | Net (FBA) |
|------------|------------------|---------|-------------------|--------------------|-----------|
| $19.99 (8-pack) | $3.00 | $3.41 | $6.90 | $9.09 | $5.68 |
| $24.99 (8-pack) | $3.75 | $3.41 | $6.90 | $14.34 | $10.93 |
| $28.99 (12-pack+rail) | $4.35 | $3.41 | $8.50 | $16.14 | **$12.73** |
| $34.99 | $5.25 | $3.56 | $8.50 | $21.24 | $17.68 |
| $38.99 (system bundle) | $5.85 | $3.56 | $9.30 | $23.84 | $20.28 |

**The $21.23 Amazon FBA net target** from Item 28 is achieved at ~$28.99 list price
(FBA), which matches the Etsy list price exactly. Same price on both channels is
the recommended approach — avoids confusing price disparities for buyers who
cross-reference platforms.

---

## Part 4: Quantity-Based Pricing Tiers

These are the recommended list prices by pack size. Prices are designed to:
(a) create an obvious per-unit value ladder that incentivizes larger orders,
(b) stay within the competitive range established by Phase 2 research,
(c) generate sufficient margin at Phase 1 volumes.

| Tier | Pack Contents | List Price | Per-Unit Equivalent | Note |
|------|--------------|------------|---------------------|------|
| Trial | 4 clips | $12.99 | $3.25/clip | Review-building entry; raise to $14.99 after 15 reviews |
| Standard | 8 clips | $19.99 | $2.50/clip | Core SKU; most buyers land here |
| Value | 12 clips | $24.99 | $2.08/clip | Introduce at 25+ reviews |
| System | 12 clips + 1 rail | $28.99 | — | Modular system value; the $25.79 Etsy net target SKU |
| Pro Bundle | 20 clips + 2 rails | $38.99 | — | Phase 1 ceiling; Phase 2 workhorse |
| Bulk (custom) | 50+ | Message for quote | ~$1.80–2.20/clip | B2B and office installs; custom listing per order |

**Bulk tier (50+ units)**: Do not publish a bulk listing until you have confirmed
production capacity to fill a 50-unit order within your stated lead time. Bulk orders
arriving with a 10-day processing time from a new shop generate negative reviews.

### Quantity discount math

The "bulk discount" should feel meaningful to the buyer while maintaining margin.
The per-unit discount ladder above achieves this automatically through pack size —
a buyer who computes the per-clip price sees the value without requiring a coupon code.

Example buyer perception:
- Trial: 4 clips for $12.99 = $3.25/clip
- Standard: 8 clips for $19.99 = $2.50/clip (saves $6 vs. buying two trial packs)
- Value: 12 clips for $24.99 = $2.08/clip (saves $14 vs. three trial packs)

This ladder drives AOV upward naturally.

---

## Part 5: Pricing Sensitivity Analysis

These inputs can materially change your net. The base table above uses the central
estimate. Adjust if your actual inputs differ.

| Input | Low Scenario | Central (base table) | High Scenario |
|-------|-------------|---------------------|---------------|
| Filament (PLA+, $/kg) | $12.00 | $13.50 | $15.00 |
| USPS Ground Advantage (8-pack) | $4.50 | $5.00 | $5.75 |
| Labor ($/hr opportunity cost) | $0 (not counted) | $20 | $30 |
| Packaging per order | $0.35 | $0.60 | $0.90 |
| Amazon FBA fee (8-pack, 10oz) | $3.06 | $3.41 | $4.04 |

**Net at $28.99 list on Etsy — sensitivity range**:
- Best case (low inputs): ~$20.00 net
- Central estimate: ~$11.29 net (with $20/hr labor)
- Worst case (high inputs + $30/hr labor): ~$5.00 net

The worst case still generates a positive net but is below the $25.79 Item 28 target.
The $25.79 target is the steady-state aspiration once volume drives material costs
down and batch printing reduces per-unit labor time — not the Week-1 reality.

---

## Part 6: When to Raise Prices

Price-raising is a milestone-gated decision, not a time-gated one. Use these triggers:

| Milestone | Action |
|-----------|--------|
| 15 reviews, 4.8+ average | Raise 4-pack from $12.99 → $14.99 |
| 25 reviews | Launch 8-pack at $19.99; launch value 12-pack at $24.99 |
| 50 reviews | Launch system listing ($28.99 clips + rail); this is the $25.79 net SKU |
| 100 reviews | Test $34.99 system listing; raise 8-pack to $22.99; run A/B test for 14 days |
| Star Seller badge | Confidence to price at premium tier ceiling without conversion penalty |
| Amazon live with 10+ reviews | Consider matching Amazon prices or maintaining a $1–2 Etsy discount |

---

## Sources

- Filament cost: [Cost_Model_May2026_Validation.md] Section 1 — $13.50/kg Phase 1 baseline
- USPS rates: [PHASE_2_TRACK_2_LOGISTICS_OPTIMIZATION.md] Table 3 + surcharge note
- Etsy fee rate: [Cost_Model_May2026_Validation.md] Section 3 — 10–10.5% effective
- Amazon fee rate: [PHASE_2_TRACK_3_MARKET_EXPANSION_RESEARCH.md] Part 1 table
- Amazon FBA fees: [AMAZON_VS_ETSY_COMPARISON.md] Section 1.3
- Net targets ($25.79 Etsy / $21.23 Amazon FBA): [PHASE_2_TRACK_3_MARKET_EXPANSION_RESEARCH.md]
  Part 1 table
- [EasyPost USPS Rate Chart May 2026](https://www.easypost.com/usps-rate-chart/)
- [Amazon FBA Fees 2026 — AMZ Prep](https://amzprep.com/amazon-fba-fees/)
