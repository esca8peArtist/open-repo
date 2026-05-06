---
title: Headphone Hooks — Bill of Materials & Cost Model
project: mfg-farm
created: 2026-05-06
status: active
confidence: high — derived from established mfg-farm cost-model-spreadsheet.csv basis, PLA+ $0.013/g confirmed
related: cost-model-spreadsheet.csv, headphone-hooks-design-spec.md, headphone-hooks-sku-strategy.md
---

# Headphone Hooks — Bill of Materials & Cost Model

**Lead finding:** At 20 units/week, total COGS is $0.33–$0.36 filament + $0.16 packaging + $0.10 equipment depreciation = $0.59–$0.62 per hook before Etsy fees. At a $12.99 sell price, Etsy-fee-adjusted net per unit is approximately $9.87–$9.90 (76% net margin). This is a stronger per-print-hour return than ModRun clips at equivalent volume because the headphone hook is a single, uncomplicated print with no hardware BOM.

---

## 1. Bill of Materials — Per Unit

### Standard single hook (25mm desk variant, with cable post)

| Component | Quantity | Unit Cost | Total Cost | Source |
|---|---|---|---|---|
| PLA+ filament | 25g | $0.013/g | $0.33 | eSUN/Overture 10kg spool at $12/kg |
| Self-adhesive silicone bumper pads (2 per hook) | 2 pads | $0.025/pad | $0.05 | AliExpress 3M Bumpon SJ5302 100-pack ≈ $5 |
| Poly mailer (9"×12") | 1 | $0.08 | $0.08 | Existing supply |
| Zip lock bag (4"×6") | 1 | $0.03 | $0.03 | Existing supply |
| Thank-you card / business card insert | 1 | $0.05 | $0.05 | Existing supply |
| **Total material + packaging** | | | **$0.54** | |

### Hardware notes
- Rubber/silicone bumper pads are the only BOM addition vs. ModRun. A 100-pack at ~$5 yields 50 hooks (2 pads/hook). Reorder at 40 hooks sold.
- No screws, magnets, or inserts required. This is the simplest BOM of any expansion product.

---

## 2. Labor Cost — Per Unit

**Labor basis:** $15/hr opportunity cost (consistent with cost-model-spreadsheet.csv)

| Activity | Time per Unit | Cost per Unit |
|---|---|---|
| Print monitoring (passive) | Not counted | $0.00 |
| Post-print harvest + inspect | 1.5 min | $0.38 |
| Rubber pad installation | 1.0 min | $0.25 |
| Packaging + shipping label | 1.5 min | $0.38 |
| **Total labor** | **4.0 min** | **$1.00** |

**Note:** At 20 units/week, packaging is batched — 4–5 orders processed together reduces per-unit time to the figures above. At 5 units/week (early phase), labor per unit rises to $1.50–$2.00 due to lower batching efficiency.

---

## 3. Equipment Depreciation — Per Unit

| Equipment | Cost | Depreciation Life | Hours/Week (20 units) | Per-Unit Depreciation |
|---|---|---|---|---|
| Bambu P1S printer | $699 | 5,000 hr | ~8 hr (5 plate runs × 1.6 hr avg) | $0.11 |

At 20 units/week, the printer runs approximately 8 print-hours/week on headphone hooks. Per-unit depreciation is negligible at this throughput.

---

## 4. Etsy Fees — Per Unit

| Fee Type | Rate | On $12.99 Sell Price | On $14.99 Sell Price |
|---|---|---|---|
| Transaction fee | 6.5% | $0.84 | $0.97 |
| Payment processing | 3% + $0.25 | $0.64 | $0.70 |
| Listing fee (amortized) | $0.20/120 days | $0.005 | $0.005 |
| **Total Etsy fees** | ~9.5% + $0.25 | **$1.48** | **$1.67** |

---

## 5. Total COGS Summary — Per Unit

### At $12.99 sell price

| Cost Component | Per Unit |
|---|---|
| Material (filament + pads) | $0.38 |
| Packaging | $0.16 |
| Labor | $1.00 |
| Equipment depreciation | $0.11 |
| Etsy fees | $1.48 |
| **Total COGS** | **$3.13** |
| **Net per unit** | **$9.86** |
| **Net margin** | **75.9%** |

### At $14.99 sell price

| Cost Component | Per Unit |
|---|---|
| Material (filament + pads) | $0.38 |
| Packaging | $0.16 |
| Labor | $1.00 |
| Equipment depreciation | $0.11 |
| Etsy fees | $1.67 |
| **Total COGS** | **$3.32** |
| **Net per unit** | **$11.67** |
| **Net margin** | **77.9%** |

**Pricing recommendation:** Launch at $12.99 to undercut the dominant competitor ($14.99 with 1,254 reviews). Once 50+ reviews are accumulated, test a price increase to $14.99. Net margin impact is +$1.81/unit at the higher price — meaningful at 20 units/week (+$36/week, +$1,872/year).

---

## 6. Weekly Revenue Projection — 20 Units/Week

| Metric | $12.99 Price | $14.99 Price |
|---|---|---|
| Weekly gross revenue | $259.80 | $299.80 |
| Weekly Etsy fees | $29.60 | $33.40 |
| Weekly net revenue | $230.20 | $266.40 |
| Weekly COGS (excl. fees) | $33.00 | $33.00 |
| **Weekly net profit** | **$197.20** | **$233.40** |
| **Monthly net profit** | **~$788** | **~$933** |

---

## 7. Comparison to ModRun Clips

| Metric | ModRun Clip | Headphone Hook | Notes |
|---|---|---|---|
| COGS per unit | $0.08–$0.13 (clip only) | $0.54 (material+packaging) | Hook has rubber pad hardware; clip has none |
| Sell price | $12–$25 (blended $24.99) | $12.99–$14.99 | Hook priced lower per unit |
| Net margin | 72.9% | 75.9–77.9% | Hook margin is slightly higher |
| Print time | 6–8 min (clip) | 22–28 min (hook) | Hook is 3–4× longer print per unit |
| Net per print-hour | ~$18–22/hr | ~$21–25/hr | Hook is competitive on net/hr basis |
| Design complexity | Medium (snap-fit) | Low (no hardware) | Hook simpler to QA |

**Key finding:** The headphone hook delivers better net margin percentage than ModRun clips, nearly equivalent net per print-hour, and requires no snap-fit hardware. The primary trade-off is longer individual print time (28 min vs. 8 min for a clip). Batch printing compensates: 4 hooks per plate plate run at 95 min = ~24 min per hook effective, close to individual estimate.

---

## 8. Volume Scaling Economics

| Weekly Volume | Weekly Net Profit ($12.99) | Monthly Net Profit | Notes |
|---|---|---|---|
| 5/week | ~$42 | ~$168 | Early phase, lower batch efficiency |
| 10/week | ~$95 | ~$380 | Batching improves, break-even on rubber pad inventory |
| 20/week | ~$197 | ~$788 | Target steady-state |
| 40/week | ~$390 | ~$1,560 | Near single-printer capacity for hooks alone; plan around ModRun plate coscheduling |

---

## 9. Shipping Cost Notes

Shipping is treated as pass-through to buyer (buyer pays shipping at checkout) or baked into price with "free shipping" listing. The hook weighs 25–28g printed + rubber pads + packaging.

| Shipping scenario | Weight | USPS First Class (via Pirate Ship) |
|---|---|---|
| Single hook in poly mailer | ~60g total | $3.50–$4.00 |
| Bundle of 3 hooks | ~150g total | $4.00–$4.50 |

If offering free shipping: add $3.75 to sell price for single hook ($12.99 + $3.75 = $16.74 net-neutral point). Alternatively, charge shipping separately. Etsy search ranking slightly favors "free shipping" listings — test both formats in first 60 days.

---

## 10. Startup Cost for This Product

| Item | Cost | Notes |
|---|---|---|
| Filament (already in stock) | $0 | Existing PLA+ inventory from ModRun production |
| Silicone bumper pads (100-pack) | $5 | One-time initial order; covers first 50 hooks |
| Additional tooling | $0 | None required |
| **Total new startup cost** | **$5** | Lowest startup cost of all five expansion products |

This product has zero new capital requirements beyond a $5 bag of rubber bumpers. It is the fastest-to-revenue expansion product in the lineup.

---

## Sources

- mfg-farm/cost-model-spreadsheet.csv — ModRun COGS baseline, filament cost ($0.013/g), labor rate ($15/hr), Etsy fee structure
- mfg-farm/product-line-strategy.md — 76% margin baseline, 25g weight estimate for headphone hook
- [3D Filament Price Per Gram Guide](https://www.3dfilamentprice.com/blog/3d-filament-price-per-gram-guide) — PLA+ bulk pricing validation
- [Pirate Ship USPS First Class rates](https://www.pirateship.com) — shipping cost basis
- [Etsy fee structure](https://www.etsy.com/seller-handbook/article/understanding-fees-on-etsy) — 6.5% transaction, 3% payment processing
