---
title: ModRun Post-Test-Print Execution Plan
date: 2026-05-06
status: ready-to-execute
audience: Anya (day-after-test-print operations), Orchestrator (timeline sync)
scope: Supplier negotiation through 6-month fulfillment scale-up
related: supplier-economics.md, supplier-scorecard.csv, production-scaling-research.md, cost-model-spreadsheet.csv, post-test-print-EXECUTION-INDEX.md
confidence: high
---

# ModRun Post-Test-Print Execution Plan

**Lead finding:** The test print is not a quality gate — it is a calibration event. Once it completes, FDM_TOLERANCE is confirmed, the production STL files lock, and the entire downstream supply chain activates in parallel. This document is the sequenced plan for everything that happens in the 72 hours after the test print completes: which suppliers to call first, in what order, with what talking points; how to set up inventory so it does not run out at the worst moment; and how each order moves from Etsy notification to USPS handoff. Months 1 through 6 are mapped against unit thresholds so every capital decision has a pre-computed trigger.

---

## Section 1: Supplier Negotiation — Sequence and Timeline

### 1.1 The Three-Day Activation Window

Supplier lead times are 3–21 days depending on channel. The first filament order must leave within 72 hours of a passing test print so that production filament arrives before the initial Etsy listings drive demand. Do not wait for a "good price" — the difference between a retail spool ($15/kg) and a 10 kg bundle ($12/kg) on a 5 kg first order is $15 total. Place the order fast; negotiate pricing on the second order when you have leverage from a proven order history.

**Target outcome by Day 3:** One confirmed first order placed with a Tier 1 supplier, two backup suppliers pre-qualified with initial contact made.

### 1.2 Tier 1 Suppliers — Contact Order and Rationale

Contact these three in this sequence. All three can be reached in parallel on Day 0.

**1. eSUN via Amazon (first order — no negotiation required)**

The fastest path to filament on hand. The eSUN 10 kg case (ASINs B0G2KSS613 for Basic, B0G2KWC5XL for PLA+) ships Prime in 2–5 business days. No supplier account required, no negotiation needed. Rated 9/10 on the supplier scorecard for AMS compatibility — the highest of any supplier at this price tier.

- First order: 10 kg case in primary production color (black). Approximate cost $110–130.
- Order via Amazon standard checkout. No special arrangement.
- Concurrent action: After placing the Amazon order, email `contact@esun3dstore.com` to express interest in direct wholesale pricing at 20+ kg/month once you hit Month 2 production. This plants the relationship seed without delaying the first order.

**2. Anycubic direct store (pre-qualification test order — Day 1)**

Anycubic is the only publicly listed supplier with a 50 kg pallet at $10.49/kg — the best published $/kg available without a wholesale account. The risk: AMS winding issues have been reported in the community for some lots. You must validate Anycubic filament on your specific Bambu P1S before depending on it for a 50 kg pallet. Place a 5 kg test order on Day 1 (approximately $55–70 at current pricing). Run a minimum 3-hour continuous AMS job with it. If the AMS feeds without incident, Anycubic becomes your primary bulk supplier at Month 3 when you exceed 25 kg/month.

- Contact: store.anycubic.com direct purchase. No sales negotiation required for the test order.
- Validation protocol: Print one full 12-clip plate using only Anycubic filament. Measure 5 clips with calipers. Run the snap-fit functional test. Pass/fail before committing to pallet pricing.
- Lead time: 3–7 business days from Chinese warehouse. Allow 10 days as a planning assumption.

**3. Overture via Amazon (PETG pre-qualification — Day 1)**

Overture PLA+ is a credible backup for eSUN (rated 8/10 on the scorecard) and is the recommended primary supplier for PETG when the PETG SKU launches. The Overture wholesale program offers 35% off at qualifying order volumes — contact `wholesale@overture3d.com` with a brief introduction on Day 1. No commitment required; establish the relationship.

- Day 1 action: Send one introductory email (use the template in `post-test-print-doc-1-supplier-negotiation-email-templates.md`, Template 1).
- Do not place a first Overture order until the eSUN 10 kg arrives — PETG is not needed in Month 1.

### 1.3 Tier 2 Backup Suppliers — Contact by Day 7

These suppliers do not need Day 0 contact, but do need to be reached within the first week so you have pricing data before the Month 2 negotiation cycle.

| Supplier | Contact Channel | When to Contact | Purpose |
|---|---|---|---|
| Polymaker wholesale | us-wholesale.polymaker.com | Day 5–7 | Account registration for Month 3–4 white/grey quality tier |
| SUNLU direct | store.sunlu3d.com | Day 5–7 | Color-sampling backup; 6-spool minimum good for secondary colors |
| Push Plastic | pushplastic.com/pages/bulk-pricing | Day 5–7 | Domestic tariff hedge; submit bulk pricing application; no commitment |
| IC3D | ic3dprinters.com | Day 7–10 | Second domestic option; "up to 20% savings" bulk — confirm the actual price |

### 1.4 Initial Purchase Order Strategy

The 5 kg first batch logic: a ModRun clip weighs approximately 3–4 g (75 g per supplier economics doc refers to the rail + clip assembly weight — individual clip is approximately 3–4 g). A 10 kg case produces approximately 2,500–3,300 individual clips or about 200–275 three-clip bundles. At 20–30 units/week initial target, a 10 kg order provides 7–10 weeks of production buffer for clips. This is the correct first order size — more than enough to validate the full production cycle without overcommitting cash.

**First order decision table:**

| Scenario | First Order Size | Supplier | Approximate Cost | Days to Arrival |
|---|---|---|---|---|
| Default launch (PLA+, black) | 10 kg case | eSUN Amazon | $110–130 | 2–5 days |
| Secondary color (white or grey) | 1 kg test spool | eSUN Amazon | $12–18 | 2–5 days |
| Anycubic pre-qualification | 5 kg bundle | Anycubic direct | $55–70 | 7–10 days |
| PETG (do not order Month 1) | — | — | — | — |

**Bulk pricing tier to target:**

- Month 1: 10 kg bundle ($11–13/kg via Amazon). No negotiation needed; just buy it.
- Month 2–3: If eSUN direct wholesale unlocks at 20 kg/month commitment, target $10–10.50/kg. If not, stay on Amazon bundles — the convenience premium is worth it at this scale.
- Month 3+: Transition primary bulk color to Anycubic 50 kg pallet ($10.49/kg) once AMS validation passes. Keep one 10 kg eSUN case in reserve on Amazon as emergency stock.
- Month 4–6: Add Polymaker wholesale for white and grey at $14.99/kg. The $2–3/kg premium over eSUN on visible-color parts is worth the tighter tolerances and vacuum packaging for customer-facing products.

**Payment terms:** At Month 1–2 volumes, there is no leverage for Net-30 terms. Pay by credit card via Amazon or supplier direct stores. At Month 3–4, when you have 2–3 order receipts with Polymaker and your monthly spend exceeds $1,000, request Net-30 terms directly. Polymaker's wholesale program supports Net-30 for qualified accounts. eSUN direct may offer Net-15 at 20+ kg/month volume; ask in the Month 2 introduction email.

**Early pay discounts:** Not available from any of the priority suppliers at this scale. Not worth pursuing — the cash flow value of Net-30 (approximately $10–15 interest on a $500 order at 3% monthly opportunity cost) does not justify the negotiating overhead at Month 1–2 volumes.

### 1.5 Supplier Talking Points

All initial outreach should use a consistent framing that establishes credibility without overpromising. The key facts to communicate:

- You are a dedicated Etsy/Amazon seller manufacturing a specific cable management product (not a hobbyist experimenting).
- You are currently at 20–30 units/week and projecting 50 kg/month by Month 3 based on planned sales velocity.
- You are evaluating 2–3 supplier relationships and are prepared to give primary order concentration to whoever offers the best combination of pricing, lead time, and quality consistency.
- You are not price-shopping aggressively at Month 1 — you want a long-term relationship. Consistency matters more than rock-bottom pricing.

Do not mention competitors' prices in the first email. Save that for Template 2 (volume pricing negotiation) which goes out only after you have received a quote.

---

## Section 2: Inventory Management at Scale

### 2.1 Safety Stock Formula Applied to ModRun

The correct inventory target is not "as little as possible" (runs out during a demand spike) or "as much as possible" (ties up cash and storage space). It is the reorder point that keeps production running through the longest realistic lead time plus a demand variability buffer.

**Safety stock formula:**

```
Safety Stock = Z × daily_consumption_std_dev × √lead_time_days
Reorder Point = (avg_daily_consumption × lead_time_days) + safety_stock
```

For PLA+ via Amazon Prime (lead time 3 days, Z = 1.65 for 95% service level):

| Phase | Daily Consumption | Lead Time | Safety Stock | Reorder Point | On-Hand Target |
|---|---|---|---|---|---|
| Month 1 (20 units/week) | 0.10 kg/day | 3 days (Prime) | 0.5 kg | 0.8 kg | 3–5 kg |
| Month 2 (30–35 units/week) | 0.20 kg/day | 3 days (Prime) | 1.0 kg | 1.6 kg | 5–8 kg |
| Month 3 (50 units/week) | 0.35 kg/day | 7 days (Anycubic direct) | 2.5 kg | 5.0 kg | 10–15 kg |
| Month 4–6 (75–90 units/week) | 0.55 kg/day | 7 days (primary) + 3 days (Prime reserve) | 4.0 kg | 7.9 kg | 20–30 kg |

**Practical reorder rule through Month 3:** Order when on-hand filament (primary production color) drops below two full spools (2 kg). At 20 units/week, two spools is approximately 3 weeks of production — well above the 3-day Amazon Prime lead time. This is deliberately conservative for the launch period.

At Month 3 when Anycubic becomes the primary supplier, revise the reorder trigger to 5 kg on hand, given the 7–10 day lead time.

### 2.2 Storage Setup and Environmental Control

PLA+ degrades when exposed to moisture. The threshold that matters: above 30% relative humidity on an open spool accelerates hygroscopic absorption. In a typical home at 40–60% RH, an open spool in ambient air degrades within 2–6 weeks in humid climates. The symptoms are extruder bubbling, stringing, and inconsistent extrusion — all of which manifest as print failures and scrap.

**Month 1 storage (up to 10 kg inventory):**
- Sealed airtight bins or vacuum storage bags (cost $10–15)
- Silica gel desiccant packets (100g per bin; replace or recharge in oven monthly)
- Ambient temperature 18–25°C — a climate-controlled room is sufficient
- Digital hygrometer in the storage area ($8–12 on Amazon) — monitor weekly; target <30% RH in the storage bin

**Month 2–3 storage (10–25 kg inventory):**
- Dedicated dry storage totes, stackable (IRIS airtight 12-qt totes, approximately $8 each)
- Add a small rechargeable silica gel unit (Eva-Dry E-333, $25–30) inside the storage area for ambient dehumidification
- Label each bin by color and supplier lot number (see FIFO protocol below)

**Month 4+ storage (25–50 kg inventory):**
- If garage or basement storage is used, invest in a dedicated humidity-controlled dry cabinet ($80–200). The Bambu Lab AMS Dry Box or a repurposed dehumidified gun cabinet both work.
- Digital temperature/humidity data logger ($20) for continuous monitoring, not spot-checking

**Active dry box for printer-adjacent filament:** Any open spool that will be on the printer for more than 48 hours goes in a Sunlu or Creality filament dry box ($25–50). Run the dry box at 50°C for 4–6 hours before a long production print to purge residual moisture from any spool that has been exposed to ambient air.

### 2.3 FIFO Bin Labeling and Rotation System

First-in-first-out prevents age degradation and ensures the oldest filament is consumed before it degrades. The labeling protocol is simple:

**Label format (permanent marker on masking tape on each spool):**
```
[Supplier] [Color] [Lot/Batch] [Date Received]
Example: eSUN / Black / Lot 2026-05A / Rcvd 2026-05-09
```

**Bin arrangement:** New stock goes to the back or bottom of the bin. Pull from the front or top. No exceptions. This takes 30 seconds per spool to implement and eliminates the possibility of discovering a 4-month-old open spool with bubbling extrusion on a production run.

**Lot tracking rationale:** If a specific lot produces a spike in scrap rates, lot number tracking allows you to isolate the cause (supplier quality variation) versus a printer issue. Without lot tracking, you cannot distinguish the two.

### 2.4 Reorder Triggers and Supplier Monitoring

Set up a physical "kanban" reorder signal: a bright-colored card tucked inside the last two spools (the two-spool safety stock threshold). When you pull a spool and find the card, place a reorder that day. This costs nothing and works better than any app or spreadsheet alert because it is impossible to ignore.

**Supplier stock monitoring at Month 3+:** The Anycubic 50 kg pallet is a specific product with finite stock. Set a Google Alert for "Anycubic PLA" and check availability before you need it. During Anycubic's 618 sale (June) and 11/11 sale (November), lead times extend to 2–3 weeks and pallet stock can sell out. Place forward-buy orders at least 3 weeks before those sale windows.

**Tariff monitoring tripwire:** Set a Google Alert for "filament tariff" and "Section 301 3D printing." If Chinese filament tariffs increase by 15+ percentage points in a single action, run the domestic break-even calculation immediately (Push Plastic at $22–28/kg becomes viable if Chinese PLA reaches $18+/kg). A tariff announcement typically provides 30–60 days before implementation — enough time for a forward-buy at pre-increase pricing if you have cash and storage.

### 2.5 Inventory Holding Cost Model

At Month 1–2 volumes, inventory holding cost is negligible:

- 10 kg of eSUN PLA+ = $120 capital tied up
- Monthly opportunity cost at 20% annual rate = $2.00/month
- Storage materials (bins, desiccant) = $20 one-time, $2–3/month replenishment
- Total holding cost: under $5/month at launch scale

This rises to approximately $15–25/month at Month 4 (30 kg on hand at $12/kg). This is not a meaningful cost consideration until you are holding 100+ kg, which is a Month 6+ scenario. Do not optimize inventory carrying cost at this stage — optimize for never running out of filament.

---

## Section 3: Fulfillment Workflow Integration

### 3.1 Daily Fulfillment Cycle

The complete order-to-ship cycle at 20–30 units/week runs in approximately 2.5–3 hours of active time per day, with print jobs running passively overnight or while other tasks occur.

**Morning (15 minutes):**
1. Check Etsy Seller app for overnight orders (Etsy sends push notifications, but verify manually).
2. Log new orders in the fulfillment tracker (Google Sheet: `Date | Order ID | SKU | Units | Status`).
3. Verify finished goods bin: are there enough printed and QC-passed units to fill today's orders from stock? If yes, skip to packaging. If no, queue print job.

**Print queue (passive — 35 minutes to 3 hours depending on batch size):**
- Target batch: 12-clip plate (prints in 35–50 minutes for clips; 2.5–3.5 hours for a rail + clip plate).
- Batch orders: if 4 orders came in for 3-clip bundles, that is 12 clips — one full plate. Print one plate, fill four orders.
- Do not print one clip for one order. The Bambu P1S has a 256 mm × 256 mm bed. Using it for a single clip is like driving to the post office to mail one letter — do it once, but plan to batch.
- Production plate naming convention: `modrun_clip_6mm_v1.0_12up_0.20mm_20pct.3mf` (encodes product, version, units per plate, layer height, infill). Saved as a locked Bambu Studio profile. Do not re-slice per order.

**Post-processing (5–8 minutes for a 12-clip plate):**
- Flex the PEI plate when cooled to 40–45°C to release parts.
- Visual inspection at harvest: check each clip for snap arm integrity, cable bore open, no bridging stringing. This takes 3–5 seconds per clip.
- Dimensional spot check: every 20th unit gets caliper measurement on snap arm width (target 7.6 mm ±0.3 mm) and rail slot entry width.
- Per-plate functional test: press one clip from the plate into a rail segment. Confirm tactile click engagement. Confirm cable retention in the bore. This is non-negotiable — skip it and a defective batch will reach customers.
- Pass/fail bin separation: passed clips into the finished goods bin; failed clips into the scrap bin (regen is free, customer service is not).

**Packaging (90–120 seconds per order):**
- Gather clips for the order (count against the order slip).
- Insert clips into a zip-lock clear bag if bundling multiples (zip bags cost $0.01–0.03 each from Amazon).
- Optional: include a 4×6 thank-you card with review request (Vistaprint print run: $0.05–0.10/card at 500-unit minimum; hold this for Month 2).
- Seal in a 9×12 poly mailer (Shop4Mailers, $0.05/unit at 1,000-pack minimum). Self-adhesive strip. Write or print order number on the outside.

**Shipping label generation (2 minutes per day batch, not per order):**
- Log into Pirate Ship. Import orders from Etsy via CSV export or Etsy integration.
- Select USPS service: First Class Package for under 1 lb (clips + mailer = 120–250 g); Ground Advantage for heavier multi-unit orders.
- Print labels in batch to a standard inkjet or thermal printer. If printing more than 5 labels per day, the thermal printer ($150–180 for a Rollo X1038) pays back within 3–6 months in ink and time savings. At 5 or fewer labels/day, inkjet on Avery 8164 labels is sufficient.
- Affix label to mailer. Stack for USPS pickup or end-of-day drop.

**End of day (5 minutes):**
- Mark all shipped orders as "shipped" in Etsy Seller. Send tracking notification (Pirate Ship can auto-upload tracking to Etsy).
- Update daily log: units printed, units passed QC, units shipped, any failure modes noted.
- Check filament on-hand. If below two-spool threshold, order tonight.

### 3.2 USPS Drop vs. Pickup

At 1–5 orders/day (Month 1–2), USPS scheduled pickup is free via USPS.com and saves driving time. Schedule pickups for Monday/Wednesday/Friday to batch accumulate orders while maintaining 3-business-day processing target.

At 10+ orders/day (Month 4+), daily pickups or a daily drop at the nearest post office are the right cadence. Do not let orders sit longer than 24 hours after the label is printed — Etsy's "estimated dispatch date" algorithm tracks this and affects search ranking.

### 3.3 Etsy Order Management — Manual vs. API

At launch scale (under 50 orders/month), manual Etsy order management via the Seller app is sufficient. The Etsy Seller app provides push notifications, order details, and a messaging interface — everything needed for a 20-30 unit/week operation.

At 50+ orders/month, consider:
- **Vela** (free tier): Etsy listing manager that syncs inventory quantities across listings automatically. Prevents overselling when a color runs low.
- **Pirate Ship Etsy integration**: Connects your Etsy shop directly to Pirate Ship for label generation without CSV export. Worth enabling from Day 1 even at low volume — setup takes 10 minutes and the ongoing time savings compound.
- **Shopify + Etsy integration**: Only relevant at Month 5–6 when you add Amazon or a direct website channel. $29/month Shopify basic plan centralizes inventory across all channels. Do not activate before you have two sales channels.

---

## Section 4: Quality Assurance Gates

### 4.1 Gate Structure

Quality is caught at harvest, not at shipment. Every plate that completes a print job passes through four gates before any unit enters the finished goods bin. The four gates take 6–8 minutes for a 12-clip plate and are non-negotiable.

**Gate 1 — Visual inspection at harvest (100% of units, 3–5 seconds each):**

Every clip from every plate is visually checked before entering the finished goods bin. Pass criteria:
- Snap arm present, not deformed or broken
- Cable bore gap open (not bridged by stringing)
- First layer fully adhered across the full base (no corner lifting or warping visible)
- No catastrophic layer separation visible on the snap arm body

Fail action: immediately into scrap bin. Do not set aside for "later review." Scrap COGS is $0.04–0.10 per clip — not worth the mental overhead of a "maybe" pile.

**Gate 2 — Dimensional spot check (1 in every 20 units, approximately 30 seconds):**

Using digital calipers ($15–25, Neiko or iGaging both adequate):
- Snap arm width: target 7.6 mm, accept 7.3–7.9 mm (±0.3 mm from SNAP_ARM_WIDTH in CadQuery source)
- Clip slot entry width: measure the rail engagement slot opening; should accept rail slot freely with the FDM_TOLERANCE value confirmed in the test print
- Bore internal diameter (optional, relevant if customers report cable not fitting): use a go/no-go gauge made from a printed test rod at the specified bore diameter

If a dimensional check fails, pull all 20 units in that measurement window for individual re-inspection. Do not ship any unit from a batch where a dimensional failure has been found until you understand the root cause (printer calibration drift, nozzle wear, filament diameter variation, or a profile change).

**Gate 3 — Functional test (1 per plate, executed on the first clip harvested):**

Before any clip from a plate goes into the finished goods bin, one clip from that plate must pass the functional test:
- Press clip into rail slot: must seat with a tactile click and no binding
- Insert a test cable of the specified bore diameter: should retain without falling out when held sideways
- Flex snap arm by hand to approximately 30% deflection: must return to position without cracking or permanent set
- This test clip is NOT scrapped after passing — it enters the finished goods bin if it passes Gate 1 visual criteria

**Gate 4 — Stress test for new filament lots (once per new supplier lot received):**

When a new spool arrives (different lot number or supplier), before running a production plate:
- Print 3 test clips from the new filament
- Run the functional test (Gate 3) on all three
- Remove and reinsert each clip 5 times in the rail slot: snap arm must not show cracking
- Flex to 50% deflection manually: must return without permanent set
- If any of the three fail, do not use the lot for production until the failure mode is diagnosed (filament quality, temperature calibration mismatch, or moisture absorption)

### 4.2 Photo Documentation

At launch, photograph each completed batch plate before harvesting. This takes 15–20 seconds per plate with a phone camera and creates a timestamped visual record that serves three purposes:
- Etsy listing freshness: upload a new batch photo to listings monthly as a "proof of active production" signal
- Customer service: if a customer claims a defective product, you have visual documentation of the batch condition at harvest time
- QA trend analysis: reviewing plate photos over time reveals gradual print quality changes before they become failure spikes

Store plate photos in a dated folder: `/production-photos/2026-05/`. Delete nothing for the first 6 months.

### 4.3 Failure Mode Recovery Protocol

**Reprint policy:** Any order that includes a defective unit is reprinted within 24 hours of failure detection. No exceptions. Customer-facing defects are the most expensive possible outcome (chargebacks, negative reviews, Etsy case filings). The material cost of one reprint is $0.04–$0.10. The cost of one negative review is incalculable on a new shop.

**Common failure modes and immediate responses:**

| Failure Mode | Immediate Action | Root Cause to Investigate |
|---|---|---|
| Snap arm snapped at base | Scrap; do not rework | Nozzle temp too low, print speed too fast on thin section, infill below 20% |
| Cable bore stringing bridge | Remove stringing with tweezers (30 sec rework); functional test after | Retraction settings, travel speed, nozzle temp |
| Dimensional oversize (clip binds in rail) | Scrap full batch; check FDM_TOLERANCE value in STL | Wrong STL version sliced, or printer X/Y calibration drifted |
| Bed adhesion failure (spaghetti) | Scrap full plate; IPA wipe bed and re-check Z offset | Dirty PEI plate, Z-offset drift, ambient cold draft |
| Layer separation on snap arm | Scrap; do not rework | Under-extrusion, cold nozzle, moisture in filament |
| Nozzle clog (visible under-extrusion) | Pause print; cold pull nozzle; restart | Burnt material, moisture in filament, speed too high |

**Scrap rate targets by phase:**
- Weeks 1–2 (profile calibration): 8–12% — acceptable; this is profile tuning time
- Month 1 steady state: below 6%
- Month 3+ mature production: below 5%
- Any week above 10% triggers a printer inspection before the next production run

---

## Section 5: Scaling Thresholds and Timeline

### 5.1 Month-by-Month Milestones

```
MONTH 1 (Days 1–30): Single printer, 20–30 units/week
─────────────────────────────────────────────────────
Units/week:  ████████░░░░░░░░░░░░  20–30
Revenue:     ~$2,200–$2,800 gross
Key actions: eSUN 10kg order, Anycubic pre-qual test, Etsy listings live
Constraint:  Print time is non-binding; order volume is the variable
Equipment:   1× Bambu P1S at ~14 hrs/week utilization
Labor:       2–3 hrs/day (print monitoring passive; packaging active)

MONTH 2 (Days 31–60): Single printer, 30–40 units/week
─────────────────────────────────────────────────────
Units/week:  ████████████░░░░░░░░  30–40
Revenue:     ~$3,200–$4,300 gross
Key actions: eSUN direct wholesale inquiry, Anycubic pallet pre-order if AMS validated
Constraint:  Printer approaching 25 hrs/week utilization
Equipment:   1× Bambu P1S
Labor:       3–4 hrs/day; consider thermal printer at this volume

MONTH 3 (Days 61–90): Single printer at capacity
─────────────────────────────────────────────────────
Units/week:  ████████████████░░░░  40–50
Revenue:     ~$4,300–$5,400 gross
Key actions: Second printer decision if 2 consecutive weeks >35 units; Polymaker wholesale registration
Constraint:  35+ hrs/week print time approaches single-printer ceiling
Equipment:   1× P1S (2nd printer justified if demand holds)
Labor:       4–5 hrs/day; packaging becomes daily scheduling discipline

MONTH 4 (Days 91–120): Two printers, scaling to 60–75 units/week
─────────────────────────────────────────────────────
Units/week:  ████████████████████  60–75
Revenue:     ~$6,500–$8,100 gross
Key actions: Second printer acquired, thermal printer acquired, 3PL evaluation begins
Constraint:  Post-processing labor (packaging + shipping) becomes binding above 65 units/week
Equipment:   2× Bambu P1S
Labor:       5–6 hrs/day; 1099 contractor begins to make sense at 75+/week

MONTH 5–6 (Days 121–180): Two printers at capacity or 3PL threshold
─────────────────────────────────────────────────────
Units/week:  Above 80
Revenue:     ~$8,700–$10,900 gross/month
Key actions: 3PL evaluation (Simpl Fulfillment or ShipMonk); Amazon FBA onboarding for top 2 SKUs
Constraint:  3PL break-even is 80–90 units/week (at ~$5–8/order fulfilled vs. $1.50–2.00 DIY)
Decision:    In-house or 3PL? See Section 5.2.
```

### 5.2 Scaling Decision Triggers

**Add second printer ($699–799):**
- Trigger: Single printer runs at 80%+ utilization (28+ hrs/week) for 2 consecutive weeks AND Etsy order backlog is accumulating (processing time slipping past 5 business days)
- Payback: 3–5 weeks at full utilization
- Do not buy a second printer speculatively. Buy it when you have the orders that need it.

**Acquire thermal label printer ($150–180):**
- Trigger: Printing more than 30 labels per week (5+ per day)
- At 30 labels/week, an inkjet printer consuming $0.04/label in ink costs $1.20/week. The thermal printer at $0.004/label saves approximately $1.10/week — payback in 2.5 years on ink cost alone.
- The real payback is time: the thermal print-and-peel workflow saves 20–30 seconds per label versus inkjet print-cut-tape. At 30 labels/day, that is 10–15 minutes per day — the thermal printer pays for itself in 4–6 weeks on labor savings alone at $15/hr.

**Hire post-processing contractor:**
- Trigger: Packaging + post-processing exceeds 3 hours/day consistently (approximately 100+ units/week)
- Structure: 1099 contractor, $15–18/hour, 10–15 hours/week
- Monthly cost: $600–$1,080
- At 100 units/week gross revenue of ~$10,800/month, contractor labor is 5.6–10% of revenue — acceptable

**Evaluate 3PL (ShipMonk or Simpl Fulfillment):**
- Trigger: 80–90 units/week AND you want to stop spending 3+ hours/day on fulfillment
- 3PL cost: $5–8 per order fulfilled (Simpl Fulfillment, purpose-built for 1–500 orders/month)
- In-house fulfillment cost at 80 units/week: approximately $1.50–2.00 per order in labor and materials
- Break-even: 3PL adds approximately $3–6 per order versus in-house. At $28.99 average order value and 67% gross margin, an extra $6/order reduces net margin by approximately 1.7 percentage points. Evaluate against your time cost — if those 3 hours/day are worth more than $6/order to you in alternative value, 3PL makes sense.
- ShipMonk minimum: 50 orders/month (already exceeded by Month 2). Simpl has no stated minimum.

**Amazon FBA onboarding:**
- Trigger: Etsy at 50+ units/week AND you want demand diversification without proportional labor increase
- FBA fees: 15% referral + $3.06–$4.25 fulfillment = approximately $7–8 total fees on a $24.99 item (28–32% take rate vs. Etsy's 9.5%)
- Only onboard the top 2–3 SKUs by volume. FBA for long-tail SKUs is not economical.
- Timeline: Begin FBA setup preparation at Month 3, activate at Month 4 when print capacity supports simultaneous Etsy + FBA inventory

---

## Section 6: Day 0 Checklist — Immediately After Test Print

This is the master action list for the first 24 hours after the test print completes. Every item is executable the same day.

### 6.1 Test Print Evaluation (30 minutes)

- [ ] Measure snap arm thickness on printed clip with digital calipers — target 1.4 mm (SNAP_ARM_THICKNESS); record actual measurement
- [ ] Measure snap arm width — target 7.6 mm (SNAP_ARM_WIDTH); record actual
- [ ] Test snap-fit: press clip into a printed rail segment — should click with light finger pressure; if binding, FDM_TOLERANCE is too tight (decrease by 0.05 mm); if loose/rattling, too loose (increase by 0.05 mm)
- [ ] Test cable retention: insert appropriate bore cable; should hold without falling out when inverted
- [ ] Test snap arm flex: deflect 30% manually; must return to position without cracking
- [ ] Record the confirmed FDM_TOLERANCE value: ____________ mm (default 0.15; adjust based on above)
- [ ] Record any design change notes (wall thickness, snap arm dimensions, bore sizing) for CadQuery parameter adjustment

### 6.2 Design Finalization (20 minutes — only if tolerance adjustment is needed)

- [ ] Update FDM_TOLERANCE in `cadquery/modrun_clip_b123d.py` and `cadquery/modrun_rail_b123d.py`
- [ ] If other dimensions need adjustment (snap arm thickness, bore diameter, wall count), update the relevant CadQuery constants
- [ ] Regenerate all five production STLs:
  ```bash
  uv run python cadquery/modrun_clip_b123d.py --bore 6 --tolerance [CONFIRMED_VALUE] --output-dir stl/v1.0/
  uv run python cadquery/modrun_clip_b123d.py --bore 8 --tolerance [CONFIRMED_VALUE] --output-dir stl/v1.0/
  uv run python cadquery/modrun_clip_b123d.py --bore 12 --tolerance [CONFIRMED_VALUE] --output-dir stl/v1.0/
  uv run python cadquery/modrun_rail_b123d.py --variant desk_clamp --output-dir stl/v1.0/
  uv run python cadquery/modrun_rail_b123d.py --variant adhesive --output-dir stl/v1.0/
  ```
- [ ] Open each STL in Bambu Studio — confirm manifold (no red repair warnings), confirm flat on build plate with no supports
- [ ] Save production slicer profile as `ModRun-PLA-Production-v1` — settings locked (see production-scaling-research.md Section 1.4 for parameter values)
- [ ] Git commit STLs with tag `v1.0` and tolerance value in commit message

### 6.3 Supplier Actions (Day 0 — parallel with above)

- [ ] Order 10 kg eSUN PLA+ case (black) via Amazon Prime — ASIN B0G2KSS613 (Basic) or B0G2KWC5XL (PLA+)
- [ ] Order 5 kg Anycubic PLA for AMS validation test — store.anycubic.com
- [ ] Email `contact@esun3dstore.com` — brief intro, 20+ kg/month projection, ask about direct wholesale pricing (use Template 1 from `post-test-print-doc-1-supplier-negotiation-email-templates.md`)
- [ ] Email Overture wholesale intro — `wholesale@overture3d.com` (same template, adjusted for PETG focus)
- [ ] Bookmark Push Plastic bulk pricing page for domestic hedge contact (Days 5–7)
- [ ] Add "filament tariff" and "Section 301 3D printing" Google Alerts

### 6.4 Storage and Infrastructure Setup (Day 0)

- [ ] Designate filament storage area — closet, shelf, or bin that stays 18–25°C; identify current RH with hygrometer
- [ ] Source airtight storage bins and silica gel if not on hand (Amazon, 1-day delivery)
- [ ] Create FIFO labeling system: masking tape, permanent marker, lot number protocol noted above
- [ ] Write kanban reorder cards (bright color index card) — insert one into the "last 2 spools" position in storage bin
- [ ] Set up finished goods bin (a lidded box or shelf) — clearly separated from raw filament storage and from scrap

### 6.5 Fulfillment Infrastructure Setup (Day 0)

- [ ] Log into Pirate Ship (pirateship.com) — verify account is active and connected to your address
- [ ] Connect Pirate Ship Etsy integration — Settings > Stores > Connect Etsy Shop
- [ ] Test one label generation cycle with a dummy shipment to confirm thermal or inkjet output
- [ ] Verify USPS scheduled pickup is configured at your address (usps.com/pickup)
- [ ] Stock poly mailers: confirm 100+ on hand (Shop4Mailers order if not — 3–5 day lead time at $0.05/unit for 1,000-pack)
- [ ] Stock zip-lock bags for bundling: 500-count, 4×6 inch, from Amazon ($5–8)
- [ ] Acquire postal scale ($20–40, American Weigh or similar) for pre-ship weight verification
- [ ] Set up QC log: Google Sheet with columns `Date | Printer | Plate Config | Units Attempted | Pass | Fail | Failure Mode | Filament Lot | Notes`

### 6.6 Photography and Listing Verification (Day 0)

- [ ] Photograph test print on neutral background (plain white or grey card) — 5 shots: hero, detail of snap arm, detail of cable bore, installed-in-rail, scale reference
- [ ] Review test print photos against Etsy listing placeholder images — verify the actual print matches listing descriptions
- [ ] Confirm photographer is sourced or scheduled (see `post-test-print-doc-3-lifestyle-photography-brief.md`)
- [ ] Verify Etsy draft listings are complete with accurate filament specs (bore diameter, material, dimensions) — do not publish until professional photos are ready

---

## Section 7: Capital and Cost Projection

### 7.1 Launch Capital Requirement (Day 0 through Month 1)

| Item | Cost | Notes |
|---|---|---|
| eSUN 10 kg PLA+ case (black) | $110–130 | Primary production filament; Month 1 supply |
| Anycubic 5 kg test order | $55–70 | AMS validation; becomes production stock if validated |
| Poly mailers, 1,000-pack (Shop4Mailers) | $50–60 | Covers approximately 1,000 orders; ~6 months at 20 units/week |
| Zip-lock bags, 500-count | $6–8 | Clip bundle packaging |
| Silica gel desiccant (500g pack) | $10–12 | Filament storage |
| Airtight storage totes × 4 | $30–40 | IRIS 12-qt sealed bins |
| Digital hygrometer | $8–12 | Filament storage monitoring |
| Postal scale | $20–30 | Pre-ship weight verification |
| Inkjet label stock (Avery 8164, 100-sheet pack) | $15–20 | Shipping labels until thermal printer threshold |
| **Total launch capital** | **$304–382** | Excludes printer (already owned) |

### 7.2 Month-by-Month Cost and Revenue Projection

Based on `cost-model-spreadsheet.csv` data and production-scaling-research.md Section 4.4:

| Month | Units/Week | Gross Revenue | COGS + Fees | Net Profit | Cumulative Net |
|---|---|---|---|---|---|
| 1 | 20–25 | $2,200–$2,700 | $900–$1,100 | $1,200–$1,600 | $1,200–$1,600 |
| 2 | 25–35 | $2,700–$3,800 | $1,100–$1,500 | $1,600–$2,300 | $2,800–$3,900 |
| 3 | 35–50 | $3,800–$5,400 | $1,400–$2,000 | $2,400–$3,400 | $5,200–$7,300 |
| 4 | 55–70 | $5,900–$7,600 | $2,600–$3,300 | $3,300–$4,300 | $8,500–$11,600 |
| 5 | 65–80 | $7,000–$8,700 | $3,100–$3,800 | $3,900–$4,900 | $12,400–$16,500 |
| 6 | 75–90 | $8,100–$9,700 | $3,500–$4,200 | $4,600–$5,500 | $17,000–$22,000 |

*Assumptions: $24.99 blended average order value, 67–73% gross margin, eSUN 10 kg bundle pricing through Month 2 transitioning to Anycubic pallet Month 3+. Month 4 includes second printer depreciation. USPS 8% temporary surcharge through January 2027 embedded in shipping costs.*

### 7.3 Capital Investment Milestones and Payback

| Investment | Amount | Trigger | Payback Period |
|---|---|---|---|
| Launch supplies (above) | $304–382 | Day 0 | 7–10 days at 20 units/week |
| Anycubic 50 kg pallet (Month 3) | $524 | 25+ kg/month consumption confirmed | 3–5 months in filament savings vs. Amazon bundles |
| Thermal label printer (Month 2–3) | $150–180 | 30+ labels/week | 6–8 weeks on labor savings at $15/hr |
| Second Bambu P1S (Month 3–4) | $699–799 | 35+ units/week sustained 2 weeks | 3–5 weeks at full utilization |
| Polymaker wholesale account (Month 4) | ~$1,000 first order | White/grey quality tier confirmed | Ongoing: $2–3/unit quality premium on visible colors |
| 1099 contractor (Month 4–5) | $600–800/month | Post-processing >3 hrs/day | Net-positive if it enables 30+ additional units/week |

### 7.4 Cash Flow Note

The business is cash-flow positive from the first complete week of 20-unit production. Launch capital of $304–382 is recovered within 7–10 days of first sales at $24.99 average order value and 67%+ margins. There is no scenario at these volumes where the business requires external financing or carries negative cash flow beyond Day 10, assuming orders materialize. The only cash flow risk is a delay in Etsy orders — which is a marketing problem, not a supply chain or capital problem. Fund the launch capital from personal savings; do not seek a loan or credit line for an operation at this scale.

---

## Confidence Notes and Gaps

**High confidence (grounded in live pricing and CAD geometry):**
- All filament pricing (eSUN, Anycubic, Overture, Polymaker) verified in supplier-economics.md at April-May 2026 pricing
- COGS and margin figures pulled directly from cost-model-spreadsheet.csv
- USPS 8% temporary surcharge in effect through January 17, 2027 — already embedded in Pirate Ship rates
- Print time estimates based on production-scaling-research.md (medium confidence benchmark; actual requires first production run to confirm)
- Scrap rate targets (3–6% mature production) from FDM farm industry benchmarks

**Medium confidence (benchmarked but not verified on this specific operation):**
- Month 1–6 revenue projections assume market demand materializes at 20 units/week within the first 2–3 weeks of listing. This is not guaranteed — it depends on Etsy listing optimization, photos, and competitive positioning. The cost model is accurate; the demand assumption is the variable.
- Anycubic AMS compatibility — the winding concern is community-sourced, not confirmed on this printer. The Day 0 test order protocol addresses this.
- Lead time estimates for Anycubic direct (7–10 days) are planning assumptions; actual may vary by 2–3 days in either direction.

**Gaps requiring action:**
- FDM_TOLERANCE confirmed value: unknown until test print completes. Everything downstream depends on this one measurement.
- Anycubic AMS validation: unknown until the 5 kg test order runs. Do not commit to the 50 kg pallet until this test passes.
- Actual print time per plate: the 35–50 minute estimate for a 12-clip plate must be confirmed on the first production run. The first production batch is also a timing benchmark.
- Demand validation: the entire revenue projection is conditional on Etsy listing performance. No prior sales history exists on this shop. Treat Month 1 revenue as unknown and plan conservatively.

---

## Related Documents

- `post-test-print-EXECUTION-INDEX.md` — navigation guide to 5 supporting documents (email templates, Etsy listings, photography brief, operations SOP, supplier contact matrix)
- `post-test-print-doc-1-supplier-negotiation-email-templates.md` — copy-paste email templates for Tier 1 supplier outreach
- `post-test-print-doc-4-first-week-operations-sop.md` — daily step-by-step fulfillment procedures
- `post-test-print-doc-5-supplier-contact-matrix.md` — supplier contact info and negotiation tracking
- `supplier-economics.md` — full pricing matrix, tariff analysis, negotiation leverage map
- `production-scaling-research.md` — print settings, batch optimization, automation roadmap
- `cost-model-spreadsheet.csv` — full throughput-level COGS and margin projections
