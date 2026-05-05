---
title: Scaling Transition Roadmap — ModRun 20→100+ Units/Week
date: 2026-05-05
status: active
tags: [mfg-farm, modrun, roadmap, scaling, decision-gates, capital, risk, milestones]
confidence: high
related: 100-unit-operations-blueprint.md, multi-printer-architecture.md, workforce-scaling-research.md, manufacturing-automation-architecture.md
---

# Scaling Transition Roadmap: 20 → 100+ Units/Week

**Lead finding:** The 20→100 unit/week transition requires two capital investments (second printer, basic automation tooling) and one operational shift (overnight batch production discipline) — not a facility upgrade, not a contractor, not a 3PL. The investor-grade version of this business is built on process maturity at each stage, not hardware accumulation. Operators who reach 100 units/week consistently and profitably are universally those who systematized one printer before adding a second.

**Timeline:** The milestones below assume a post-test-print start. The test print is a prerequisite — all production-scale investment is contingent on the test print validating the snap arm function, dimensional tolerance, and clip-to-rail fit. Run the test print first.

---

## Month-by-Month Milestones

### Months 1–2: Single Printer Optimization (Target: 20 units/week)

**Objective:** Establish a proven, repeatable production process on one printer before adding any complexity.

**Week 1 (post-test-print):**
- Lock production slicer profile: save as `ModRun-PLA-Production-v1` in Bambu Studio. Record all parameters explicitly (layer height: 0.20mm, infill: 20% gyroid, walls: 3, nozzle: 222°C, minimum layer time: 8 seconds). Version-control this file — any change requires a new version and a validation print.
- Establish file directory structure: `/modrun-production/cadquery/`, `/stl/v1.0/`, `/sliced/production/`
- First 12-clip production plate: run 3 plates to establish actual (not estimated) print time, scrap rate, and harvest cadence. Record to QC log.
- Set up Pirate Ship account and postal scale. Print first batch shipping labels.

**Weeks 2–4:**
- Begin online sales (Etsy listings go live). Do not wait for inventory; list with 3–5 day processing time.
- Run the **overnight clip protocol**: queue 6–8 plate jobs before bed; harvest in the morning. This single habit multiplies weekly output without adding active time.
- Target: 2–3 plates per day, 5 operating days = 10–15 plates/week = 120–180 clips/week capacity. Actual sell-through at this stage will be 5–20 units/week (demand is the constraint, not production).
- Enable Bambu P1S AI failure detection notifications. Test push notification routing to phone. Confirm you receive a test alert before trusting it for overnight production.

**Months 1–2 KPIs to track weekly:**
- Printer utilization hours/day (target: reach 12+ hours/day by end of Month 2)
- Weekly orders fulfilled vs. available inventory
- Scrap rate per printer per week (target: <5% by Week 3, <3% by Week 6)
- Owner active hours per day on operations (target: <2 hours at 20 units/week)

**Month 2 decision checkpoint:** If Etsy views are adequate (200+/week) but conversion is below 2%, the problem is product presentation — photography, listing copy, pricing — not manufacturing. Do not add printer capacity to solve a marketing problem.

**Exit condition for this phase:** Any two of: (a) printer running 12+ hours/day for 2 consecutive weeks, (b) backlogged orders causing extended processing times, (c) weekly sell-through consistently above 25 units.

---

### Months 2–3: Second Printer Addition (Target: 40–50 units/week)

**Objective:** Double physical capacity with zero increase in active daily labor through automation.

**Printer 2 purchase trigger (the rule):** The second printer is justified when the first printer has run at 80%+ utilization (approximately 13+ hours/day) for two consecutive weeks AND unfulfilled orders or inventory stockouts have occurred. Purchasing ahead of this trigger is speculative hardware investment. At $699/unit, the second printer pays back in under 3 weeks when it enables incremental sales — but only if demand exists to fill it.

**Setup sequence:**
1. Purchase Bambu P1S #2. Unbox and run Bambu Studio calibration sequence before loading any production filament.
2. Install Bambu Farm Manager on the primary computer. Add both printers. Confirm both appear in the fleet dashboard.
3. Install Printago free tier. Configure material tags for each printer (P1: black PLA+, P2: white PLA+ initially).
4. Run one validation plate on P2 with the locked production profile. Compare output to P1 baseline. If dimensional variation exceeds 0.3mm on any critical feature, run full auto-calibration on P2 before production use.
5. Label printers P1 and P2 physically on the machine housing. Every maintenance log and failure report references the printer number — this becomes critical at 3+ printers.

**Load distribution strategy:**
- P1: primary production color (black) — the highest-velocity SKU runs continuously
- P2: second production color (white) + overflow black when P1 queue is ahead

**Overnight protocol with 2 printers:** Queue both printers for 8-hour overnight runs (10pm–6am). Each printer completes 8–10 plates overnight. Morning harvest: 20 plates × 12 clips = 240 clips in inventory before the business day begins. At 50 units/week sell-through, this is 3.5 weeks of finished goods production in a single overnight session.

**Month 3 milestone check:**
- If revenue is above $4,000/month and both printers run 12+ hours/day, the operation is healthy. Plan for P3 in Month 5–6.
- If revenue is below $2,000/month at 2 printers, the constraint is demand not supply. Hold at 2 printers and invest in Etsy SEO, photography, and bundle listings.

---

### Months 3–4: Multi-Printer Workflows (Target: 60–80 units/week)

**Objective:** Establish the operational routines that scale to 5 printers without linear labor increase.

**Key operational additions:**
- **Batch-by-color discipline:** Assign each printer a primary color and only switch colors for overflow. Color switching wastes 3–5g of filament per purge cycle and adds 5 minutes of AMS management. At 2 printers, this saves 15–30 minutes/week. At 5 printers, it saves 60–90 minutes/week.
- **Priority queue logic:** Implement in SimplyPrint (add the farm plan subscription if not already running): Priority 1 = committed orders within 48 hours, Priority 2 = top-SKU restock below 20 units, Priority 3 = standard production, Priority 4 = new variants. This formalizes what was previously informal judgment and prevents the most common scaling mistake: printing new colorway experiments while customer orders wait.
- **Inventory buffer targets:** Maintain 2 weeks of finished goods for the top-3 SKUs (by velocity). At 60 units/week, a 2-week buffer = 120 units in finished goods — manageable storage footprint (2–3 small bins), significant buffer against demand spikes and printer downtime.

**Parallel scheduling mechanics:** With 2 printers, the scheduling problem is simple: P1 runs clips, P2 runs clips or rails. With 3 printers, introduce explicit job queue management:
- P1 dedicated to highest-velocity SKU (black 6mm clips)
- P2 dedicated to second-highest velocity (white 6mm clips)
- P3 on rails during the day; overnight runs clips of any color from the backlog

**Failure recovery practice:** Every printer failure is a protocol practice opportunity. When P2 has a bed adhesion failure at 2am:
1. SimplyPrint push notification wakes you (or alerts at 7am if configured for normal priority)
2. Remotely cancel the job via SimplyPrint mobile app
3. Re-queue the job to P1 or P2 after the morning harvest
4. Log the failure: printer, failure mode, time elapsed, filament lot

After 3–4 failure events, the failure recovery workflow becomes automatic. This matters enormously when you have 5 printers and failures are a daily statistical certainty.

---

### Months 4–6: Scaling to 5 Printers (Target: 100–150 units/week)

**Objective:** Reach full-scale print farm operation with systematic labor and quality management.

**Third printer trigger:** Same rule as the second — 80%+ utilization on both P1 and P2 sustained for 2 consecutive weeks. With 2 printers at 85% utilization and 12-clip plates running 16 hours/day, daily capacity is ~360 clips. At 100 units/week, that's ~85% of capacity — the trigger condition.

**Contractor introduction:** When packaging + shipping exceeds 90 minutes/day consistently (approximately 100 units/week), source a 1099 post-processing contractor:
- Source: local maker space community board, Nextdoor, or neighborhood Facebook group
- Role: visual QC inspection, bundling, packaging, label application, outbound staging
- Hours: 10 hours/week at $15–16/hour = $600–640/month
- Training: 1–2 days using the one-page visual QC checklist (laminated, posted at the QC station)
- Contract: written agreement covering scope, NDA, IP assignment. Do not share design files or production data beyond what is necessary for packaging tasks.

**Printer 4 and 5:** Add in sequence as printers 1–3 reach sustained 80%+ utilization. At 5 printers, you reach the natural ceiling for a solo operator plus one contractor. Beyond this, consider a second contractor or a part-time W-2 employee before adding more printers.

**Facility check at Month 5–6:** Five printers running simultaneously produce approximately 1,000W of sustained heat output. Verify:
- Room temperature stays below 26°C with all 5 printers running. If not, deploy portable AC unit ($280).
- Power distribution: 5 P1S printers on two dedicated 20A circuits (3 on one, 2 on the other). Do not run more than 3 on a single 20A circuit.
- Ventilation: bathroom exhaust fan (110 CFM) running continuously during operating hours.

---

### Month 6+: 3PL Transition Evaluation

**The 3PL decision is triggered by operational pain, not volume milestones alone.** Evaluate when any of these conditions persist for 3+ consecutive weeks:
- Packing and shipping exceeds 4 hours/day AND a second contractor is impractical
- Order error rate (wrong item, wrong quantity, delayed shipment) exceeds 1% despite process controls
- Desire to operate the business remotely without a physical inventory location

**3PL evaluation framework:**
1. Calculate current self-fulfillment cost per order: shipping + packaging materials + labor time (at opportunity cost). At 100 units/week with $4.50 average Pirate Ship rate + $0.20 packaging + $0.20 labor = $4.90 per order self-fulfillment cost.
2. Get quotes from Simpl Fulfillment and ShipMonk. Compare their per-order all-in cost to your current $4.90.
3. Add the 3PL's monthly minimum ($750 for Simpl) to the comparison. At 100 orders/month, Simpl's $750 minimum is $7.50/order in fixed cost alone — above your self-fulfillment cost. The math flips when you reach 400+ orders/month.

**Amazon FBA transition (independent of 3PL decision):** FBA is a channel-specific logistics decision, not a whole-business fulfillment decision. Activate Amazon FBA for your top 2–3 Amazon SKUs when Amazon channel orders reach 30+ units/week. Self-fulfill Etsy orders in parallel. FBA removes all fulfillment labor for the Amazon channel at the cost of ~28–32% total Amazon fees (referral + FBA fulfillment) vs. Etsy's ~15% plus self-shipping.

---

## Capital Requirements

### Full Scaling Path — Investment Summary

| Phase | Item | Unit Cost | Quantity | Phase Capital |
|---|---|---|---|---|
| **Phase 1** (Month 1) | Bambu P1S | $699 | 1 | $699 |
| | Starter filament (PLA+, 3 spools) | $20 | 3 | $60 |
| | Packaging supplies | — | — | $40 |
| | Postal scale | $30 | 1 | $30 |
| | **Phase 1 total** | | | **$829** |
| **Phase 2** (Month 2–3) | Bambu P1S #2 | $699 | 1 | $699 |
| | Thermal label printer (Rollo X1038) | $180 | 1 | $180 |
| | Filament stock expansion (10kg) | $130 | 1 | $130 |
| | **Phase 2 total** | | | **$1,009** |
| **Phase 3** (Month 4–5) | Bambu P1S #3 | $699 | 1 | $699 |
| | Portable AC unit | $300 | 1 | $300 |
| | Anti-vibration pads | $20 | 3 | $60 |
| | Additional shelving + bins | $80 | 1 | $80 |
| | **Phase 3 total** | | | **$1,139** |
| **Phase 4** (Month 5–6) | Bambu P1S #4 and #5 | $699 | 2 | $1,398 |
| | AutoFarm3D Door Opener (3 units) | $129 | 3 | $387 |
| | Spare PEI plates (2 per printer) | $20 | 10 | $200 |
| | Spare nozzle kits (0.4mm brass, 5-pack) | $25 | 2 | $50 |
| | **Phase 4 total** | | | **$2,035** |
| **Ongoing monthly (5 printers)** | Electricity | — | — | $150 |
| | SimplyPrint farm plan | $30 | 1 | $30 |
| | AutoFarm3D software | $20 | 1 | $20 |
| | Craftybase Indie | $45 | 1 | $45 |
| | Contractor (10 hr/week at $16/hr) | $640 | 1 | $640 |
| | **Total ongoing monthly overhead** | | | **$885/month** |

**Total capital to reach 100+ units/week capacity (5 printers):** approximately $5,012 across 6 months, plus $885/month in ongoing operational overhead.

**Working capital:** At 5 printers consuming ~50 kg/month of filament, the working capital requirement for filament inventory (3-week safety stock) is approximately $1,800 at bulk pricing ($12/kg × 150 kg). This capital is not consumed — it rotates as filament is used and replenished.

**Payback timeline:** Phase 1 printer ($829) recovers in the first month of 20-unit/week production. Phase 2 printer ($699) recovers in 2–3 weeks at 40-unit/week demand. Phase 3–4 printers recover similarly, with payback periods of 2–4 weeks per printer at sustained demand.

---

## Risk Mitigation

### Printer Reliability

**Mean time between failures:** Bambu P1S community data indicates approximately 300–500 hours between significant failures (bed adhesion degradation, nozzle clog, AMS feed issue) for a well-maintained printer running PLA. At 16 hours/day operation, this is approximately 20–31 days between maintenance events. Most failures are minor (10–30 minute resolution); full printer downtime events (hotend replacement, belt failure) occur roughly every 1,000–2,000 hours.

**Spare parts strategy:** Maintain on-hand at all times:
- 2 spare 0.4mm brass nozzles per printer (full fleet: 10 nozzles, ~$25 for a 10-pack)
- 2 spare PEI spring steel plates per printer (full fleet: 10 plates, $15–20 each from Bambu)
- 1 spare AMS PTFE tube kit per 2 printers
- 1 spare hotend assembly (the most common significant failure) — stock 1 per 3 printers, ~$30 each

At 5 printers, total spare parts investment: ~$400–500. A single averted 2-hour production downtime event recovers this cost.

**Single printer contingency:** With 2+ printers, a single printer failure is a 50% (or 33%, or 20%) capacity reduction — painful but not a business halt. Communicate affected Etsy processing times proactively; extend by 1–2 days during repair. The Star Seller threshold (>95% on-time shipments) can tolerate a 2–3 day repair window if you have finished goods buffer stock.

**Printer failure at 1 printer:** This is the highest-risk scenario. At 1 printer, a 3-day failure halts production completely. Mitigation:
- Maintain 2 weeks of finished goods inventory for top SKUs
- Know your nearest Bambu service partner or have Bambu warranty claim process documented
- Consider purchasing a second printer at Month 2 as redundancy, not just capacity

### Demand Volatility

**Queue depth management when demand drops:** If weekly orders drop below 50% of production capacity for 2+ consecutive weeks:
- Reduce print runs to match demand + 1-week buffer (do not overproduce and tie up capital in excess inventory)
- Idle a printer rather than running it at 30% utilization — idle printers do not consume filament or wear out components
- Evaluate whether the demand drop is seasonal (holiday lull, summer slowdown) or structural (listing de-indexed, competitor entry)

**Seasonal demand patterns:** Etsy cable management accessory searches typically spike in September–November (back-to-school, new office setups, pre-holiday organization). Plan inventory buildup in August–September. Expect a January–February lull; use that period for design iteration and new SKU development.

**Exit criteria:** If weekly orders drop below 30 units/week sustained for 4+ consecutive weeks despite SEO and listing optimization efforts, revert to single-printer operation. Moth-ball printers 3–5 (they retain value; resale market for Bambu P1S is active). Maintain P1 and P2 for resilience. Do not carry operational costs (contractor, SimplyPrint farm plan, AutoFarm3D) for idle capacity.

### Quality Consistency at Scale

**The central risk:** Three printers printing from the same file produce three slightly different outputs as calibration drifts. A clip from P1 (well-calibrated, nozzle fresh) that snap-fits perfectly may be incompatible with a clip from P3 (nozzle 2,000 hours old, slight Z-offset drift) that is dimensionally off by 0.3mm.

**Mitigation protocol:**
- Monthly calibration cycle: never let more than 30 days pass on any printer without a full auto-calibration run
- Cross-printer dimensional comparison: once per month, print one 12-clip plate on each printer with the same filament lot, then measure 3 clips from each batch with calipers. If any printer's mean measurement is more than 0.3mm from the others, investigate and calibrate before next production run
- Nozzle swap cadence: replace nozzles every 2 kg of filament printed per printer (every ~1,000 clips at 2g/clip). At 5 printers running PLA+ at 50 kg/month, this means 25 nozzle changes/month — establish a rotation schedule

**Process standardization document:** Write a 2-page Production SOP covering: plate preparation, job dispatch, first-layer confirmation, harvest protocol, QC checkpoints, failure response, and calibration schedule. Laminate it. Post it on the print room wall. This document is the quality system. When a contractor is introduced, this SOP is their training material.

### Supply Chain

**Filament concentration risk:** At 5 printers consuming 50 kg/month, a primary supplier stockout halts production. Mitigate with two qualified suppliers:
- Primary: eSUN PLA+ (Amazon, 10kg bundles, 1–2 day delivery, $11–13/kg)
- Backup: Overture PLA+ or SUNLU PLA+ (Amazon, same Prime shipping, validated as compatible with P1S and existing production profile)

Test the backup supplier: run one 10-plate production run with the backup filament before committing to it as a validated source. Verify that scrap rate, snap arm function, and dimensional accuracy match the primary supplier's output. Do not discover a backup supplier is incompatible during a stockout emergency.

**Tariff risk (2026):** All major FDM filament suppliers (eSUN, Overture, SUNLU, Anycubic) are Chinese-manufactured. 2025–2026 tariff escalations have created pricing pressure on Chinese goods. Monitor pricing quarterly. At $11–13/kg for PLA+, a 25% tariff increase would push prices to $14–16/kg — still significantly below retail single-spool pricing, and still economically sound for this operation. Push Plastic (US-manufactured, $20–26/kg retail) is a domestic fallback option if tariff pressure becomes untenable.

**3-week safety stock:** Maintain 3 weeks of filament in the top production colors at all times. At 50 kg/month = 12.5 kg/week, safety stock is approximately 37 kg. This represents $444–481 in working capital (at $12–13/kg) and approximately 5–6 full shelf bins of storage.

---

## Decision Gates

### Gate 1: 1 → 2 Printers

**Trigger condition:** P1 at 80%+ utilization (13+ hours/day printing) for 2 consecutive weeks AND any of: (a) unfulfilled orders backing up, (b) processing time extended beyond 5 days, (c) weekly revenue above $3,000/month.

**Decision options:**
- Add P2 at $699: proceed if trigger condition is met AND demand appears demand-constrained, not marketing-constrained (i.e., you have traffic and conversions but can't keep up, not low traffic)
- Reduce product scope instead: if one SKU (e.g., desk clamp rails) accounts for 80% of revenue and is backlogged while other SKUs have inventory sitting, reduce SKU count to focus capacity rather than add printers

**Gate 1 pass criteria:** Trigger condition met for 2 consecutive weeks with documented evidence (QC log utilization tracking).

### Gate 2: 2 → 3 Printers

**Trigger condition:** Both P1 and P2 at 80%+ utilization for 2 consecutive weeks AND monthly revenue above $5,000.

**Decision:** Same framework as Gate 1. Add P3 if supply-constrained; optimize listings and channel strategy if demand-constrained.

**Gate 2 additional consideration:** By Month 5–6, evaluate whether adding a third printer or opening a second sales channel (Amazon Handmade) better addresses growth. Amazon Handmade requires no additional printer capacity — it is a distribution expansion that multiplies revenue per unit of production.

### Gate 3: 3 → 5 Printers (Full Farm)

**Trigger condition:** P1, P2, and P3 all at 80%+ utilization for 2 consecutive weeks AND monthly net profit above $6,000/month (indicating sufficient cash flow to absorb two additional $699 investments simultaneously).

**This gate should only be reached at Month 5–8 at the earliest under realistic demand growth assumptions.** Do not front-run this gate.

### Gate 4: Reversion — Scaling Down

**Trigger condition:** Weekly orders drop below 30 units/week sustained for 4 consecutive weeks despite active marketing.

**Reversion actions:**
1. Halt production on P3–P5 immediately. Running printers at 20% utilization costs electricity, wear, and consumables without generating revenue.
2. Cancel SimplyPrint farm plan (revert to Bambu Farm Manager free tier for P1–P2).
3. Release or suspend 1099 contractor relationship.
4. Maintain P1 and P2 operational with 2-week finished goods buffer.
5. Evaluate demand root cause: Etsy algorithm change, seasonal, competitive. Act accordingly.

Reselling printers: Bambu P1S holds 60–70% of purchase value in the used market (per community resale data). A purchased-at-$699 printer with 500 hours of use sells for $400–450 on Facebook Marketplace or eBay. Capital recovery on reversion is meaningful.

---

## Critical Path Summary

The critical path to 100 units/week is not the printers — it is the first 200–300 Etsy reviews and the SEO ranking that comes from them. A 5-printer farm with a de-indexed Etsy shop produces nothing. A 1-printer operation with a top-3 search placement in its niche runs at capacity.

| Sequence | Action | Blocking dependency |
|---|---|---|
| 1 | Test print → validate design | No dependency |
| 2 | Lock production profile, set up Pirate Ship | Test print passed |
| 3 | List on Etsy; start sales | Production profile locked |
| 4 | Build to 20 units/week sell-through | 30+ reviews, SEO traction |
| 5 | Add P2 at 80% utilization of P1 | Gate 1 trigger met |
| 6 | Grow Etsy to 50 units/week | Reviews, SEO, photography quality |
| 7 | Add P3, introduce contractor | Gate 2 trigger met |
| 8 | Reach 100 units/week | Gate 3 trigger met |

The time axis on this path is 4–8 months under realistic Etsy growth assumptions — not because production scaling is hard, but because organic Etsy search ranking takes time. The manufacturing infrastructure is the easy part.

---

## Sources

- [3DCentral: How to Start and Scale a 3D Print Farm Business](https://3dcentral.ca/how-to-start-and-scale-a-3d-print-farm-business-the-complete-guide/) — scaling thresholds, daily operations benchmarks
- [ADP Industries: How to Set Up a Bambu Lab Print Farm](https://www.adpindustries.com/blog/bambu-lab-print-farm-setup-guide/) — printer addition timing, fleet management benchmarks
- [ADP Industries: Bambu Lab vs Creality vs Prusa — 2026](https://adpindustries.com/blog/bambu-lab-vs-creality-vs-prusa-2026/) — reliability data, farm suitability
- [3DQue AutoFarm3D Door Opener](https://shop.3dque.com/products/autofarm3d-door-opener-for-bambu-lab-p1p-x1c-x1e-pre-sale) — auto-eject hardware pricing
- [Bambu Lab Wiki: P1S Maintenance Checklist for Print Farms](https://jcsfy.com/blogs/3d-printing-tech/bambu-p1s-maintenance-checklist-for-print-farms) — MTBF data, spare parts cadence
- [Bambu Lab Community Forum: Printers Per Circuit](https://forum.bambulab.com/t/how-many-printers-can-you-safely-run-simultaneously-on-one-circuit/21063) — electrical capacity data
- [SimplyPrint: FarmLoop Auto-Queuing](https://simplyprint.io/blog/autoprint-update-farmloop-ai-bed-check/) — overnight automation capability
- [SigmaFilament: Filament for Print Farms Failure Reduction Guide](https://sigmafilament.com/filament-for-print-farms-guide/) — dual-supplier strategy, quality consistency
- [Financial Models Lab: Second Printer ROI Analysis](https://financialmodelslab.com/blogs/how-much-makes/3d-printing-business) — printer payback calculations
- [Simpl Fulfillment Pricing](https://www.simplfulfillment.com/pricing) — $750/month minimum, flat-rate 3PL model
- [ShipMonk Pricing — Research.com 2026](https://research.com/software/reviews/shipmonk-review) — per-pick fee structure
- [Pirate Ship: April 2026 USPS Rate Change](https://support.pirateship.com/en/articles/14491291-april-2026-usps-time-limited-price-change) — current shipping cost baseline
- [Etsy Star Seller Requirements](https://help.etsy.com/hc/en-us/articles/4403054980503-Etsy-Star-Seller-Program-Policy) — shipping compliance thresholds for ranking
- [NextGenModeling Case Study — eRank](https://help.erank.com/blog/nextgenmodeling-etsy-seo-success-story/) — single-operator scale evidence
