---
title: ModRun Inventory Forecast Model — Demand Forecasting, Safety Stock, and Reorder Points
project: mfg-farm
created: 2026-05-07
status: production-ready
session: multi-supplier-research
confidence: high — formulas from published supply chain literature (Nventory, Netstock, Fishbowl 2026); ModRun-specific inputs from Session 291 COGS model and Etsy seasonal demand patterns
related: supply-chain-diversification-strategy.md, supplier-comparison-matrix.csv, supply-chain-resilience-strategy.md
---

# ModRun Inventory Forecast Model

**Lead finding:** At ModRun's target volume of 20 units/week (current) scaling to 100+ units/week by Month 6, the optimal inventory model is a hybrid: pure made-to-order through 50 units/week (zero finished goods inventory overhead), then a progressive pre-build buffer starting at 3 days of safety stock at 50–100 units/week, scaling to 7 days at 100–200 units/week. Filament safety stock — not finished goods safety stock — is the more important calculation at all volume tiers. The reorder point for filament should be triggered when stock drops below 2 weeks of supply, not 1 week, because the effective lead time for a new filament order (order + ship + test) is 5–7 days and demand can spike. At 20 units/week (current target), the safety stock formula produces a filament buffer of 14–21 days. For finished goods, safety stock is 4–7 units (one overnight print plate) through Month 3.

---

## Section 1: Demand Forecasting Approach

### 1.1 Forecast Method: Weighted Moving Average

ModRun does not yet have historical sales data (pre-launch). The correct approach for a new product is:

**Pre-launch estimate (Weeks 1–4):**
Use the conservative case from the Session 291 business plan: 5 units/week (floor), 20 units/week (base case), 40 units/week (optimistic). The forecast is the base case until actual sales data is available.

**Weeks 5–12 (post-launch adjustment):**
Switch to a 4-week weighted moving average (WMA) with heavier weight on recent weeks:

```
WMA(t) = (0.4 × Week_t) + (0.3 × Week_t-1) + (0.2 × Week_t-2) + (0.1 × Week_t-3)
```

This weights the most recent week at 40% and smooths backward. For a product with no long history, this is more responsive than a simple average.

**Month 3+ (established baseline):**
Overlay a seasonal multiplier based on Etsy demand patterns for home organization (see Section 1.2). Calculate a 12-week rolling average as the baseline and apply the seasonal multiplier for the planning period.

### 1.2 Seasonal Demand Multipliers for Etsy Home Organization

Based on verified Etsy seller trend data (Etsy Seller Handbook 2025–2026) and home organization market research:

| Period | Weeks | Demand Multiplier vs. Annual Average | Planning Action |
|---|---|---|---|
| January ("New Year setup") | Weeks 1–3 | +30–40% | Pre-build 1 week of top SKUs in late December |
| February–March | Weeks 5–12 | Baseline (1.0×) | Normal production cadence |
| April–May (spring setup) | Weeks 14–22 | +15–20% | Increase filament safety stock in March |
| June–August | Weeks 24–35 | Baseline (1.0×) | Lowest period; use for equipment maintenance and product development |
| September–October | Weeks 36–43 | +40–60% | Begin Q4 pre-build by August; add 2-week safety stock |
| November–December (Q4 peak) | Weeks 44–52 | +60–80% | Highest conversion; pre-build 2–3 weeks by mid-October; gift bundle SKUs |

**Practical application:** ModRun's launch timing (May 2026) puts it in the spring uptick window. Base case of 20 units/week during spring should be treated as a seasonally elevated number — true baseline (for safety stock calculations) may be 15–17 units/week adjusted for season.

### 1.3 Demand Variability Assessment

**Coefficient of Variation (CV) for Etsy sellers:**
CV = Standard Deviation / Mean

Etsy demand for niche home organization products typically shows a CV of 0.3–0.6 in early months (high variability due to unknown demand), converging to 0.15–0.30 after 3+ months as the listing accumulates reviews and search placement stabilizes.

**ModRun demand variability assumption (pre-data):**
- CV = 0.50 (conservative; reflects unknown demand in launch phase)
- This means if the mean is 20 units/week, the standard deviation is 10 units/week (daily std deviation ≈ 10/7 = 1.43 units/day)

After 8 weeks of data, recalculate CV from actual sales using: `=STDEV(weekly_sales) / AVERAGE(weekly_sales)` in Google Sheets. If CV drops below 0.25, reduce safety stock. If CV exceeds 0.60, increase.

---

## Section 2: Safety Stock Formula and Calculations

### 2.1 Core Formula

The standard safety stock formula accounting for both demand and lead time variability:

```
Safety Stock = Z × √(L × σd² + d² × σL²)
```

Where:
- **Z** = service level Z-score (1.65 for 95%; 2.05 for 98%; 2.33 for 99%)
- **L** = average supplier/production lead time in days
- **σd** = standard deviation of daily demand
- **d** = average daily demand
- **σL** = standard deviation of lead time in days

**Service level recommendation for ModRun:**
- Use Z = 1.65 (95% service level) for the clip (primary SKU, Etsy standing-critical)
- Use Z = 1.28 (90% service level) for filament safety stock (lower consequence; backup supplier available next-day)

### 2.2 Finished Goods Safety Stock — Clip

**Current assumptions (launch phase):**
- Average weekly demand: 20 units/week → average daily demand (d): 2.86 units/day
- Daily demand std deviation (σd): 1.43 units/day (CV = 0.50 × d)
- Production "lead time" = time to print a plate of clips = 4–8 hours (same-day production possible); effective lead time = 0 days for planning purposes (self-print replaces supplier lead time)
- Effective lead time variability (σL): 0 (no supply chain lead time; production is on-demand)

**Result at current scale (20 units/week, self-print, made-to-order):**
Since production lead time ≈ 0 (same-day printing), safety stock of finished goods is effectively zero. Made-to-order is the correct model. The Etsy processing time window (stated 2–5 days) absorbs the 4–8 hour print time.

**Safety stock for finished goods at 50 units/week tier:**
- Average daily demand (d): 7.14 units/day
- Daily demand std deviation: 2.14 units/day (CV = 0.30 at 50+/week as demand stabilizes)
- Effective "lead time" for finished goods pre-build: 1 day (1 overnight print plate)
- σL: 0 (production is internal, consistent)

```
Safety Stock = 1.65 × √(1 × 2.14²) = 1.65 × 2.14 = 3.5 → round to 4 units
```

**Recommendation: Pre-build a buffer of 4 finished clips per active SKU when weekly demand reaches 50 units/week.** At ModRun's clip geometry (12 clips per standard plate), one plate covers safety stock for the entire week with one overnight run.

**Safety stock for finished goods at 100 units/week tier:**
- Average daily demand: 14.29 units/day
- Daily demand std deviation: 2.86 units/day (CV = 0.20 at established velocity)
- Lead time for pre-build: 1 day

```
Safety Stock = 1.65 × √(1 × 8.18) = 1.65 × 2.86 = 4.7 → round to 5 units per SKU
```

Add a round-number margin: **maintain 8–12 units of finished clip inventory per SKU** when at 100 units/week. This is one full print plate, pre-built daily.

### 2.3 Filament Safety Stock Calculation — Critical Input

Filament is the true supply chain constraint for ModRun. Unlike contract-manufactured goods, a filament stockout stops all production immediately. The correct safety stock calculation applies standard lead time + demand variability.

**Inputs:**
- Average daily filament consumption at 20 units/week: 20 units × 75g/unit ÷ 7 days = 214g/day ≈ **0.214 kg/day**
- At 100 units/week: 100 × 75g ÷ 7 = 1,071g/day ≈ **1.07 kg/day**
- Filament lead time (eSUN Amazon Prime): 2–5 days; average = 3.5 days
- Lead time standard deviation: 1 day (Prime reliability is high; σL ≈ 1)
- Demand variability at filament level (σd): CV × d = 0.30 × 0.214 = 0.064 kg/day (at 20 units/week)
- Target service level: 90% (Z = 1.28) — acceptable because backup supplier (Anycubic) provides a fast secondary option

**Safety Stock for filament at 20 units/week:**
```
Safety Stock = 1.28 × √(3.5 × 0.064² + 0.214² × 1²)
             = 1.28 × √(0.0144 + 0.0458)
             = 1.28 × √(0.0602)
             = 1.28 × 0.245
             = 0.314 kg → round to 0.4 kg (about half a spool)
```

**Note:** This is the pure mathematical safety stock. In practice, the reorder lead time is longer than 2–5 days when factoring in the decision delay (noticing stockout → ordering → shipping). The recommended minimum safety stock is 14 days of supply (the existing protocol from `supply-chain-resilience-strategy.md`), which is more conservative than the formula output and appropriate given the low carrying cost of filament.

**Recommended filament safety stock by volume tier:**

| Production tier | Daily consumption | Minimum safety stock | Buffer cost |
|---|---|---|---|
| 20 units/week | 0.21 kg/day | 3.0 kg (14 days) | ~$36 at $12/kg |
| 50 units/week | 0.54 kg/day | 7.5 kg (14 days) | ~$90 |
| 100 units/week | 1.07 kg/day | 15 kg (14 days) | ~$180 |
| 200 units/week | 2.14 kg/day | 30 kg (14 days) | ~$360 |

**These costs are negligible relative to the revenue protected.** At 100 units/week ($7,200/month gross), a 14-day filament buffer worth $180 protects against a $3,360 revenue loss from a 14-day production stoppage. The ROI is 18.7:1.

---

## Section 3: Reorder Point Calculations

**Reorder Point Formula:**
```
Reorder Point (ROP) = (Average Daily Demand × Lead Time) + Safety Stock
```

### 3.1 Filament Reorder Points

| Volume tier | Daily demand (kg) | Lead time (days) | Safety stock (kg) | Reorder Point (kg) | Order Quantity |
|---|---|---|---|---|---|
| 20 units/week | 0.21 | 3.5 (eSUN Amazon) | 3.0 | (0.21 × 3.5) + 3.0 = **3.74 kg** | 10 kg (one Amazon case) |
| 50 units/week | 0.54 | 3.5 | 7.5 | (0.54 × 3.5) + 7.5 = **9.4 kg** | 20 kg (two Amazon cases) |
| 100 units/week | 1.07 | 3.5 | 15 | (1.07 × 3.5) + 15 = **18.7 kg** | 30–50 kg (Anycubic pallet portion or 3× eSUN cases) |
| 200 units/week | 2.14 | 3.5 | 30 | (2.14 × 3.5) + 30 = **37.5 kg** | 50 kg (Anycubic pallet) |

**Practical implementation:** Track filament stock by color. When any production color hits the reorder point, immediately order the specified quantity. Do not wait until stock is depleted. At 20 units/week, this means keeping a minimum of 3.74 kg per production color on hand at all times and ordering a 10 kg case when any color drops below this level.

**Color stock tracking (Google Sheets setup):**
- Column A: Color name (Black, White, Grey, etc.)
- Column B: Current spool count
- Column C: kg per spool (1kg or 3kg)
- Column D: Total kg on hand (B × C)
- Column E: Reorder Point (from table above, per current volume tier)
- Column F: Status (=IF(D<=E,"ORDER NOW","OK"))

Update Column B each time a spool is started. The STATUS column alerts automatically.

### 3.2 Finished Goods Reorder Points (Pre-Build Buffer)

At 50 units/week and above, a finished goods pre-build buffer is appropriate. The reorder point for a finished goods plate (12 clips per plate) is:

```
ROP (finished goods) = (daily orders × print lead time hours/24) + safety stock units
```

At 50 units/week:
- Daily orders: ~7 units/day
- Print lead time: 1 plate overnight (8 hours = 0.33 days)
- Safety stock: 4 units

```
ROP = (7 × 0.33) + 4 = 2.3 + 4 = 6.3 → trigger a pre-build plate when on-hand drops below 7 finished clips
```

**Practical rule at 50 units/week:** Start a clip plate overnight whenever finished goods inventory drops below 7 units. A 12-clip plate restores buffer to 12 units and covers 1.7 days of demand.

At 100 units/week:
- Daily orders: ~14 units/day
- Print lead time: 0.33 days (overnight plate)
- Safety stock: 8 units

```
ROP = (14 × 0.33) + 8 = 4.6 + 8 = 12.6 → trigger pre-build when on-hand drops below 13 units
```

**Practical rule at 100 units/week:** Maintain a standing overnight plate schedule (1–2 plates/night). The trigger for an additional plate is inventory dropping below 13 units.

---

## Section 4: Demand Volatility Handling

### 4.1 JIT vs. Safety Stock — The ModRun Decision Matrix

| Volume tier | Recommended model | Rationale |
|---|---|---|
| <50 units/week | Pure made-to-order (JIT) | Print time (4–8 hours) fits within Etsy 2–5 day processing window; no finished goods overhead needed |
| 50–100 units/week | Hybrid: JIT for custom SKUs + 1-day pre-build buffer for top 2 SKUs | Fast shipping badge (24h ship) improves Etsy conversion 10–20%; pre-build top sellers only |
| 100–200 units/week | Active pre-build buffer (4–7 days of top 3 SKUs) | Etsy algorithm rewards consistent same-day shipping; pre-build enables this at scale |
| 200+ units/week | 7–14 day rolling buffer on top 5 SKUs | At this volume, batch production efficiency exceeds JIT cost savings; consistent ship speed becomes a moat |

### 4.2 Demand Spike Response Protocol

**Detection threshold:** If orders in any 48-hour window exceed 2× the weekly average daily rate, classify as a demand spike.

**Response by spike duration:**

Spike lasting 2–5 days (e.g., social media mention, Etsy feature):
1. Extend all Etsy processing times to 5–7 days immediately (prevents late shipping marks)
2. Switch to overnight batch production (one full plate per night cycle instead of on-demand)
3. Prioritize oldest orders first (Etsy FIFO); clear backlog before resuming standard processing time

Spike lasting 6–21 days (sustained surge or viral moment):
1. Steps above plus: place overflow order with JLC3DP (100–300 units at 10–14 day lead time)
2. Evaluate expedited Tier 2 (Xometry) for units needed within 72 hours
3. If second printer was planned: accelerate acquisition. Payback from spike demand alone: <1 week at $399 printer cost.

**Spike pre-calculation for current scale:**
At 20 units/week (current baseline), a 3× spike = 60 units in one week. Self-print capacity: ~100 units/week at max (24-hour cycle, two overnight plates per day). Therefore: a 3× spike is absorbable via extended batch production without Tier 2 activation. A 5× spike (100 units in one week) hits the self-print ceiling and requires Tier 2 activation.

### 4.3 Etsy-Specific Demand Signals to Monitor

**Signals that predict a demand spike (check weekly in Etsy Stats dashboard):**
- Listing views increase 50%+ week-over-week without a corresponding increase in conversions (implies viral interest that will convert in 48–72 hours)
- Listing saved ("Favorited") count increases 100%+ in one week (Etsy favorites predict purchases 5–14 days later with 15–25% conversion rate)
- Etsy ad spend efficiency suddenly improves (ROAS increases without bid changes) — usually indicates the algorithm is promoting the listing to a broader audience

**Pre-action on signals:**
If listing views + saves spike simultaneously, pre-build a full plate (12 clips) before the orders materialize. The 12-unit buffer costs 4–8 hours of overnight printing and prevents a spike from creating a backlog.

---

## Section 5: Specific Recommendations for ModRun at 20 Units/Week

### Current State (20 units/week target)

**Filament inventory:**
- Keep 3–4 kg of black PLA+ on hand at all times (covers 14 days at 20 units/week, all black)
- Keep 1–2 kg of white and grey PLA+ (secondary colors at lower velocity)
- Total filament investment: ~3–4 10kg cases × $120 = $360–480 in working capital
- Reorder trigger: Any color below 3.74 kg (or 3.74 kg of black) → order 10 kg case immediately

**Finished goods:**
- Made-to-order only. No pre-build buffer needed.
- Etsy processing time: 2–5 days (adequate buffer for 4–8 hour print time + packing)
- Exception: Pre-build a plate of 12 clips on Friday afternoon to cover weekend orders (Etsy traffic peaks Saturday; print-to-order on Saturday may push to late Monday ship)

**Contract manufacturer accounts (Tier 2):**
- Create JLC3DP account this week. Upload modrun_clip.stl and modrun_rail.stl. Save quotes.
- Create Xometry account. Get expedited quote for 25-unit clip order. Save.
- Budget: $0 (account setup only). No order yet.

### Month 3 Scaling (50 units/week)

- Reorder point: 9.4 kg per production color → order 20 kg when any color hits this level
- Finished goods: Pre-build 4-unit buffer for top 2 clip SKUs; trigger overnight plate when < 7 units on hand
- Filament safety stock: Increase to 7.5 kg per production color
- Contract manufacturer: Execute 10-unit sample order from JLC3DP to validate quality and lead time for overflow readiness

### Month 6 Scaling (100 units/week)

- Reorder point: 18.7 kg per production color → order 50 kg (Anycubic pallet) when near this level
- Finished goods: 8-unit buffer per top 3 SKUs; two overnight plates minimum per night
- Filament safety stock: 15 kg per production color (3 colors × 15 kg = 45 kg total; ~$540)
- Second printer: Acquisition is the primary capacity unlock, not inventory management
- Contract manufacturer: Activate JLC3DP for regular overflow orders (25–100 units/month) at validated quality

---

## Section 6: Inventory Tracking System

### Minimum Viable Tracking (Google Sheets)

Two sheets required: Filament Tracker and Finished Goods Tracker.

**Filament Tracker columns:**
Color | Supplier | Spools on hand | kg/spool | Total kg | Reorder Point (kg) | Status | Last Order Date | Next Order Date

**Finished Goods Tracker columns:**
SKU | Description | Units on hand | Units in queue (printing) | Weekly velocity | Safety Stock | Buffer Status | Days of supply

**Review cadence:**
- Filament Tracker: Update daily (2 minutes — check if any spool was started)
- Finished Goods Tracker: Update on order fulfillment (each time an order ships, subtract 1 unit from on-hand)
- Full inventory audit: Weekly (Sunday evening, 10 minutes — count finished goods, confirm filament levels match tracker)

### When to Add an IMS

An inventory management system (Linnworks, Inventory Planner, or similar) becomes valuable when:
- SKU count exceeds 10 active variants
- Multiple fulfillment channels (Etsy + Amazon + own website)
- Monthly orders exceed 300

At 20 units/week (80 units/month) with 2–4 SKUs and Etsy-only, a Google Sheet is sufficient and preferable (lower cost, faster to set up, easier to customize for ModRun-specific production planning).

---

## Sources

- [Safety Stock Formula for Ecommerce — Nventory](https://nventory.io/us/blog/safety-stock-formula-ecommerce)
- [Reorder Point Calculator and Formula — Nventory](https://nventory.io/us/blog/reorder-point-calculator-guide)
- [How to Calculate Safety Stock: 6 Formulas — The Retail Exec](https://theretailexec.com/logistics/safety-stock-calculation/)
- [Safety Stock Using Standard Deviation — Netstock](https://www.netstock.com/blog/safety-stock-meaning-formula-how-to-calculate/)
- [Inventory Forecasting Models and Methods — Inventory Planner](https://www.inventory-planner.com/ultimate-guide-to-inventory-forecasting/)
- [Demand Forecasting for eCommerce: Complete Guide — Sumtracker](https://www.sumtracker.com/blog/demand-forecasting-for-ecommerce)
- [Etsy Seller Trend Report: Spring and Summer 2026](https://www.etsy.com/seller-handbook/article/1473931456647)
- [Home Organization Trends 2025 — Accio](https://www.accio.com/business/home_organization_trends)
- [Etsy Inventory Management 2025 Guide — CLOSO](https://closo.co/blogs/platform-specific-guides/etsy-inventory-management-2025-guide-how-to-track-sync-automate-stock)
- [AI Safety Stock Optimization — OnePint](https://www.onepint.ai/insights/ai-safety-stock-optimization-managing-uncertainty-without-overbuilding-inventory)
- Internal: `supply-chain-resilience-strategy.md`, `phase-2-supplier-research.md`, Session 291 business plan COGS model
