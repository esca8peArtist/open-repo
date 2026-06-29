---
title: Pricing Calculator — ModRun Cable Clip (Worked Model)
project: mfg-farm
created: 2026-06-28
status: production-ready
scope: >
  Worked pricing model with fill-in fields for any product. Pre-filled baseline for
  ModRun cable clip C-01 at current production costs. Includes Etsy vs Amazon FBA
  comparison, volume scenario table (10–500 units), and printer break-even analysis.
related:
  - COMMODITY_PRODUCT_LIBRARY_Q3_2026.md
  - cost-model-spreadsheet.csv
  - MULTI_CHANNEL_SALES_ARCHITECTURE.md
  - PHASE_2_TRACK_3_MARKET_EXPANSION_RESEARCH.md
---

# Pricing Calculator — ModRun Cable Clip

---

## Part 1: Input Variables

Fill in these values for any product. Values pre-filled below are for the ModRun cable clip 3-pack (C-01 SKU) at current single-printer, 20 units/week production level.

### Section A: Material Inputs

| Variable | Unit | C-01 Baseline | [FILL IN for new product] | Notes |
|---|---|---|---|---|
| Filament cost per gram | $/g | $0.022 | [FILL IN] | PLA+ at $18.99/kg + 15% scrap buffer. PETG: use $0.030/g. Bulk rate (10kg+): $0.019/g PLA+ |
| Print weight | grams | 14g | [FILL IN] | Weigh the test print on a postal scale. Use the actual print, not the slicer estimate (slicer is ±5%) |
| Scrap rate | % | 8% (first 100 units); 5% thereafter | [FILL IN] | Apply during calibration. Reduce to 5% once settings dialed |
| **Material cost** | $ | **$0.31** | **= weight × $/g × (1 + scrap rate)** | 14g × $0.022 × 1.08 = $0.332 → rounds to $0.31 at steady state |

### Section B: Machine Time Inputs

| Variable | Unit | C-01 Baseline | [FILL IN for new product] | Notes |
|---|---|---|---|---|
| Print time | hours | 0.55 hrs | [FILL IN] | From slicer estimate (Bambu Studio). Add 5 min for bed removal and print start. |
| Machine cost per hour | $/hr | $0.28 | Same for all products using P1S | Breakdown: $0.08 depreciation (P1S $399, 5,000-hr life) + $0.17 electricity (150W avg × $0.12/kWh) + $0.03 wear parts (nozzle, build plate). Total: $0.28/hr |
| **Machine cost** | $ | **$0.15** | **= print time × $0.28** | 0.55 hrs × $0.28 = $0.154 |

### Section C: Labor

| Variable | Unit | C-01 Baseline | Notes |
|---|---|---|---|
| Post-processing time | minutes | 2 min | Bed removal, inspection, any support removal |
| Packaging time | minutes | 3 min | Insert into mailer, card, tape, label |
| Total labor per unit | minutes | 5 min | |
| Labor rate | $/hour | $0 currently (opportunity cost baseline) | Apply $15/hr only when comparing to hiring a contractor. At solo operation, this is your time — track it to know when a contractor becomes worth it. |
| **Labor cost (solo)** | $ | **$0** (time cost only) | At 100+ units/week: switch to $15/hr to model contractor cost |

### Section D: Packaging

| Item | C-01 Cost | Notes |
|---|---|---|
| Poly mailer (6×9", 2.5mil) | $0.08 | Purchase in 200-packs (~$0.08–$0.10 each) |
| Tissue paper | $0.05 | One sheet per order |
| Thank-you / business card insert | $0.08 | VistaPrint 500-pack ~$40; amortized |
| Tape | $0.07 | Packaging tape, prorated per unit |
| Label (Pirate Ship or Etsy label) | $0.07 | Pre-paid label fee included in shipping cost paid by seller |
| **Packaging subtotal** | **$0.35** | |

### Section E: Shipping (If Seller-Absorbed)

| Scenario | USPS Cost | Notes |
|---|---|---|
| Cable clip 3-pack (fully packaged ~44g, 1.6 oz) | $4.00–$4.50 | USPS First Class Package via Pirate Ship (discounted rate) |
| Bundle with rail section (4–6 oz) | $5.00–$5.50 | USPS First Class or Priority Mail Small Flat Rate |
| Large bundle (8+ oz) | $5.50–$7.00 | Priority Mail; verify if flat rate box is cheaper |
| **C-01 assumed shipping (built into price)** | **$4.25** | Midpoint; use $4.25 as the absorbed shipping cost when computing true floor price |

---

## Part 2: Pre-Filled Baseline — ModRun Cable Clip 3-Pack (C-01)

### Cost Stack at Single-Unit Level

| Component | Cost | % of $12.99 Price |
|---|---|---|
| Filament (14g × $0.022 × 1.05 scrap) | $0.32 | 2.5% |
| Machine time (0.55 hrs × $0.28) | $0.15 | 1.2% |
| Packaging | $0.35 | 2.7% |
| Shipping (absorbed, USPS First Class) | $4.25 | 32.7% |
| **Total COGS (material + machine + packaging + shipping)** | **$5.07** | **39.1%** |
| Etsy transaction fee (6.5%) | $0.84 | 6.5% |
| Etsy payment processing (3% + $0.25) | $0.64 | 4.9% |
| Etsy listing fee (amortized) | $0.20 | 1.5% |
| **Total Etsy fees** | **$1.68** | **12.9%** |
| **Total all-in cost** | **$6.75** | **52.0%** |
| **Net margin per unit** | **$6.24** | **48.0%** |

Note: The COMMODITY_PRODUCT_LIBRARY_Q3_2026.md reports 82.8% net margin ($10.75 net) at $12.99. That calculation excludes absorbed shipping as a COGS item (treats it as buyer-paid). When the seller absorbs shipping (which free-shipping Etsy listings must do), the true margin at $12.99 is closer to 48%. At $16.99 with free shipping, the true margin is 58%.

**This is why the launch price should be at least $14.99** — the shipping absorption at $12.99 erodes margin significantly. The $12.99 launch price is justified only by the review-accumulation velocity it enables during the 14–21 day recency window.

---

## Part 3: Output — Floor Price, Etsy Target, Amazon FBA Target

### Floor Price (0% Net Margin, Including Shipping)

```
Floor price = (Material cost + Machine cost + Packaging + Shipping) ÷ (1 - Etsy fee rate)
Floor price = ($0.32 + $0.15 + $0.35 + $4.25) ÷ (1 - 0.129)
Floor price = $5.07 ÷ 0.871
Floor price = $5.82
```

Do not sell below $5.82. Everything above this is margin. The launch price of $12.99 is 2.2× the floor.

**For future products**: Replace the numerator with the actual COGS for that product (materials + machine + packaging + shipping) and divide by (1 - 0.129) for Etsy. The floor price scales directly with COGS.

### Etsy Target Price (30% Net Margin After All Costs Including Shipping)

```
Target price = Floor price ÷ (1 - target margin)
At 30% net margin: Target price = $5.07 ÷ (1 - 0.30) = $7.24

But this doesn't account for Etsy fees (which are % of price, not a fixed cost):
True formula: Target price = COGS ÷ (1 - Etsy fee rate - target margin rate)
= $5.07 ÷ (1 - 0.129 - 0.30)
= $5.07 ÷ 0.571
= $8.88
```

At $8.88, the net margin (after all costs including shipping) is exactly 30%. At $12.99, the margin is 48%. At $14.99, the margin is 55%. These are the real numbers including shipping.

**Practical pricing guidance**: The 30% margin floor sets the minimum viable price. The actual launch price should be set by the market (competitor pricing) and the review velocity strategy (lower price = faster reviews = faster ranking). For C-01, $12.99–$14.99 is the correct range. Higher than $16.99 before 15 reviews is algorithmically punishing.

### Amazon FBA Target Price

Amazon FBA fees on the same product are higher. The same COGS but with a different fee structure:

```
Amazon FBA fees on a $15.99 sale (C-01 individual pricing):
- Referral fee (15%): $2.40
- FBA fulfillment (1.6 oz, <2 oz tier): $3.22
- Total fees: $5.62 (35.1%)

Remaining for COGS and profit: $15.99 - $5.62 = $10.37
COGS (without shipping — FBA handles shipping): $0.32 + $0.15 + $0.45 (FBA packaging) = $0.92
Net margin per unit: $10.37 - $0.92 = $9.45 (59.1%)
```

The FBA shipping is handled by Amazon — this is the counterintuitive offset. FBA's higher platform fee is partially compensated by eliminating the $4.25 seller-absorbed shipping cost. The net margin at $15.99 on FBA (~$9.45) is comparable to Etsy at $14.99 (~$8.08 net). Price the Amazon listing $1–2 above the Etsy listing to account for the higher fee rate while maintaining comparable net yield.

**Amazon FBA price recommendation for C-01**: $15.99 (individual 3-pack) vs. Etsy's $12.99–$14.99. This $1–3 premium is defensible given Prime delivery and the distinct buyer persona.

---

## Part 4: Volume Scenario Table

How margin and revenue change at different production volumes. Economies of scale come primarily from two sources: (1) bulk filament pricing reduces material cost/gram, and (2) batch packaging reduces time per unit.

| Volume | Units/Week | Units/Year | Filament Cost/g | COGS/Unit | Etsy Fees/Unit | Net/Unit | Monthly Net | Key Change |
|---|---|---|---|---|---|---|---|---|
| **Baseline (current)** | 20/week | 1,040 | $0.022 | $5.07 | $1.68 | $6.24 | **$541** | Single spool purchases |
| **Growth tier 1** | 50/week | 2,600 | $0.019 | $4.91 | $1.68 | $6.40 | **$1,386** | 10kg bulk rate ($19/kg); batch packaging |
| **Growth tier 2** | 100/week | 5,200 | $0.017 | $4.78 | $1.68 | $6.53 | **$2,831** | 25kg+ rate; FBA handling reduces packaging time |
| **Scale tier** | 250/week | 13,000 | $0.015 | $4.65 | $1.68 | $6.66 | **$7,218** | 50kg bulk deal ($15/kg); case packaging; mixed Etsy + Amazon |
| **Farm tier** | 500/week | 26,000 | $0.012 | $4.48 | $1.68 | $6.83 | **$14,793** | 100kg+ deal ($12/kg); contractor packaging; FBA dominant |

Notes on the table:
- Etsy fees are constant as a % of price — they don't scale with volume
- The net per unit improvement from 20 to 500 units/week is only $6.24 → $6.83 (9.5%) — cable clips have very low COGS already, so volume leverage on cost is limited
- The margin improvement comes primarily from reducing packaging and labor overhead per unit, not filament price
- The large monthly net jump from 20 to 500/week ($541 → $14,793) is purely volume, not margin expansion — the same 48% net margin on more units

**Where volume actually helps**: Higher-COGS products (bundles, topo maps, headphone hooks) see more meaningful margin improvement with volume because the filament cost component is larger. Cable clips are already near the COGS floor.

### Economies of Scale on Filament Bulk Buys

| Purchase Size | Typical Rate | Annual Savings vs. $0.022/g (at 5,200 units/year) | Minimum Units to Justify |
|---|---|---|---|
| 1 kg spool (individual) | $0.022/g | Baseline | Any |
| 3–5 kg bundle | $0.021/g | $7.28/year | 20/week |
| 10 kg bulk | $0.019/g | $40.56/year | 50/week |
| 25 kg purchase | $0.017/g | $65.00/year | 100/week |
| 50 kg deal (e.g., Anycubic bulk) | $0.015/g | $91.00/year | 200/week |

**Decision rule**: Buy the largest quantity you can sell through in 6 weeks without moisture degradation. PLA+ absorbs moisture and prints worse after 8–12 weeks in a humid environment if unsealed. Seal unused spools in a vacuum bag with desiccant if storing longer than 2 weeks.

---

## Part 5: Break-Even Analysis — Printer Cost Recovery

How many cable clip units must you sell to recover the cost of the Bambu P1S printer?

**Assumption**: P1S costs $399 after promotional pricing (current 2026 price). At net margin of $6.24/unit (at $12.99 launch price including absorbed shipping):

```
Units to break even = Printer cost ÷ Net margin per unit
= $399 ÷ $6.24
= 64 units
```

At 20 units/week, the printer pays for itself in **3.2 weeks** from cable clip sales alone.

### Break-Even by Price Point

| Sale Price | Net/Unit (after all costs incl. shipping) | Units to Break Even (P1S $399) | Weeks at 20/wk |
|---|---|---|---|
| $9.99 | $2.79 | 143 units | 7.2 weeks |
| $12.99 | $6.24 | 64 units | 3.2 weeks |
| $14.99 | $8.24 | 48 units | 2.4 weeks |
| $16.99 | $10.24 | 39 units | 2.0 weeks |
| $19.99 | $13.24 | 30 units | 1.5 weeks |

**Key takeaway**: At any viable price point, the printer breaks even in under 8 weeks of cable clip production alone. The printer cost is not the financial risk — the real risk is producing before validating demand. Print the test batch first, list, and generate sales before ordering bulk filament.

### Break-Even Including Startup Capital (Filament + Packaging)

| Item | Cost |
|---|---|
| Bambu P1S | $399 |
| Initial filament (2 kg, 3 colors) | $38 |
| Packaging supplies (200-pack poly mailers, tissue, cards) | $35 |
| Etsy shop setup | $0 |
| First 5 listings at $0.20 each | $1 |
| **Total startup capital** | **$473** |

At $6.24 net/unit and 20 units/week: **$473 ÷ $6.24 = 76 units = 3.8 weeks to recover all startup capital.**

If pricing at $14.99 (post-review price): **$473 ÷ $8.24 = 57 units = 2.9 weeks.**

---

## Part 6: Fill-In Template for New Products

Use this template when pricing any new product from the Q3 library or beyond.

```
PRODUCT NAME: _______________
SKU ID: _______________

--- INPUT VARIABLES ---
Filament type: PLA+ / PETG / ASA / Other: ___________
Filament cost per gram: $_____ (see Part 1 Section A for rates by quantity)
Print weight: ____g (from test print, postal scale)
Print time: ____hrs (from Bambu Studio slicer)
Machine cost per hour: $0.28 (fixed for P1S)

Any hardware BOM items:
  Item 1: _________ × qty ___ @ $___ each = $____
  Item 2: _________ × qty ___ @ $___ each = $____
  Item 3: _________ × qty ___ @ $___ each = $____
Hardware subtotal: $____

--- COST CALCULATIONS ---
Material cost: ___g × $___/g = $_____
Machine cost: ___hrs × $0.28 = $_____
Hardware cost: $_____
Packaging: $0.35 (standard; adjust if product requires rigid box)
Shipping (absorbed): $_____ (weigh fully packaged unit, look up USPS First Class rate)
Total COGS: $_____

--- PRICING OUTPUTS ---
Floor price (0% margin, Etsy): COGS ÷ (1 - 0.129) = $_____
30% margin target price: COGS ÷ (1 - 0.129 - 0.30) = $_____
Etsy launch price (based on competitor range + recency strategy): $_____
Post-review price (after 15 reviews): $_____
Amazon FBA price (Etsy price + $1-$3 to offset higher fees): $_____

--- BREAK-EVEN ---
Net per unit at launch price: Launch price - COGS - Etsy fees = $_____
Units to break even on P1S ($399): $399 ÷ net per unit = _____ units
Weeks to break even at ___ units/week: _____ weeks

--- MARGIN SANITY CHECK ---
Launch price: $_____
Total costs (COGS + fees): $_____
Net per unit: $_____
Gross margin %: net ÷ launch price = _____%
Minimum acceptable gross margin (before Offsite Ads): 35%
Minimum acceptable gross margin (after Offsite Ads at 12%): 40%
Pass/Fail: _____
```

---

## Sources

- [COMMODITY_PRODUCT_LIBRARY_Q3_2026.md](COMMODITY_PRODUCT_LIBRARY_Q3_2026.md) — C-01 unit economics baseline; cost assumption table
- [cost-model-spreadsheet.csv](cost-model-spreadsheet.csv) — volume scenario data (5/week through 100/week)
- [MULTI_CHANNEL_SALES_ARCHITECTURE.md](MULTI_CHANNEL_SALES_ARCHITECTURE.md) — Etsy vs Amazon fee structure, $25.79 vs $21.23 per-unit comparison
- [amazon-fba-analysis.md](amazon-fba-analysis.md) — FBA fee schedule, volume scenario economics at 10/50/100 units/month
- [etsy-seo-strategy-q2-q3-2026.md](etsy-seo-strategy-q2-q3-2026.md) — pricing elasticity analysis, $12.99/$16.99/$19.99 tier conversion benchmarks
- [PHASE_2_TRACK_3_MARKET_EXPANSION_RESEARCH.md](PHASE_2_TRACK_3_MARKET_EXPANSION_RESEARCH.md) — net revenue comparison across channels
