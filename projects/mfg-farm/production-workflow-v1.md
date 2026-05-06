---
title: ModRun Production Workflow v1.0 — Post-Test-Print Operational Guide
date: 2026-05-06
status: production-ready
version: 1.1
scope: STL approval through 6-month scale-up — all post-test-print operations
related: manufacturing-automation-architecture.md, pricing-strategy.md, post-test-print-workflow.md, etsy-shop-launch-kit.md
confidence: high
---

# ModRun Production Workflow v1.0

**Purpose:** Eliminate post-test-print planning paralysis. This document activates immediately when the test print passes. Every decision below is pre-made so Month 1 supplier ordering, Etsy listing creation, and fulfillment setup begin within 24 hours of test-print approval.

**Lead finding:** Printer capacity on a single Bambu X1 Carbon running overnight batches far exceeds expected Month 1–3 demand. The binding constraint through Month 4 is labor-intensive post-processing and packaging, not printing time. The correct operational strategy is batch consolidation (10-unit plates where geometry allows) and parallelizing post-processing with active print jobs — not adding printers until sustained demand exceeds 50 units/week.

---

## Part 1: Post-Approval Workflow

### 1.1 Test Print Outcomes (May 6–15 Window)

The test print answers four questions:

| Gate | Pass Criterion | Fail Criterion |
|------|----------------|----------------|
| Snap arm function | Click-fit engages smoothly, no rattle, no play | Arm cracks, doesn't click, or rattles under cable load |
| Dimensional tolerance | Snap arm 1.35–1.45mm; bore within ±0.5mm nominal | Any measurement outside the acceptance band in Section 3.1 |
| Support removal | Clean release, no surface damage at support interfaces | Torn surface, visible scar >1mm on functional face |
| Finish quality | Layer lines visible but uniform; no stringing across bore | Stringing inside bore, warping on base, blobs on exterior |

**Decision tree:**

- PASS (4/4): Proceed immediately — lock STL, lock slicer profile, begin production
- NEAR-PASS (3/4): Adjust tolerance parameter in CadQuery, reprint targeted component (1 week)
- FAIL (<3/4): Geometry iteration required (2–3 weeks); do not order bulk filament until re-test passes

**This document assumes the test print PASSES.**

---

### 1.2 STL Lock and Slicer Calibration (Day 0 — 45 minutes)

**After test print approval, do these steps in sequence:**

1. Record the confirmed FDM_TOLERANCE value from the passing print (expected: 0.10–0.20mm)
2. Regenerate final production STLs from CadQuery source with confirmed tolerance:
   ```
   modrun_clip_b123d.py --bore 6 --tolerance [confirmed] --output-dir stl/v1.0/
   modrun_clip_b123d.py --bore 8 --tolerance [confirmed] --output-dir stl/v1.0/
   modrun_rail_b123d.py --tolerance [confirmed] --output-dir stl/v1.0/
   ```
3. Import STLs into Bambu Studio and create production slicer profile: `ModRun-PLA-Production-v1`

**Production slicer parameters (lock these — no ad-hoc changes):**

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Layer height | 0.20mm | Speed/strength balance for functional clips |
| Wall loops | 4 | Adequate strength for flex-to-install clips |
| Infill | 20% gyroid | Omnidirectional load distribution for snap-fit |
| Outer wall speed | 200 mm/s | X1 Carbon production sweet spot |
| Inner wall speed | 300 mm/s | |
| Supports | None | Design self-supporting; supports add 30–60 sec/unit post-processing |
| Brim | 3mm removable | Bed adhesion on flexible PEI; peels cleanly |
| Seam position | Back-aligned | Seam artifact on non-visible inside face |
| Nozzle temp | 223°C | PLA+ 215–230°C range; mid-point for adhesion |
| Bed temp | 60°C | Standard PLA+ adhesion on PEI |

4. Save 10-clip production plate as: `modrun-plate-10x-production-v1.3mf`
5. Save 5-clip plate for small runs: `modrun-plate-5x-production-v1.3mf`
6. Verify print time estimates per plate (expected: 55–70 min for 10-clip plate, 35–45 min for 5-clip plate)

**Time: 45 minutes. Done once. Profile is frozen until design version bump.**

---

### 1.3 Per-Unit Production Timeline (Step-by-Step)

**Calendar span:** Monday start → Wednesday ship-ready = ~36 hours elapsed
**Active labor per unit:** 28 minutes (at 5-unit batch) or 25 minutes (at 10-unit batch)

| Step | Who | Time per Unit | Time per 5-Unit Batch | Notes |
|------|-----|---------------|----------------------|-------|
| Design review & STL confirm | Operator | 5 min | 5 min (once per batch) | Verify correct file version loaded |
| Slicing & plate setup | Operator | 3 min | 3 min (once per batch) | Load production 3MF, queue job |
| Print monitoring | Operator | 2 min | 2 min (check-in at 50%, 90%) | X1 Carbon Bambu Cloud alerts |
| Post-processing: cool-down | Unattended | 0 min | 3–4 hours | Printer handles; operator doing other things |
| Post-processing: support/brim removal | Operator | 9 min | 45 min | Flex PEI plate, sweep clips into bin |
| Post-processing: cleaning | Operator | 6 min | 30 min | Hot water + soft brush; dry |
| Quality control inspection | Operator | 4 min | 20 min | Per checklist in Part 3 |
| Packaging: boxing | Operator | 3 min | 15 min | Kraft 6×4×2" box, padding |
| Fulfillment: label gen + ship | Operator | 2 min | 10 min | Pirate Ship batch label print |
| **Total active labor** | | **34 min** | **~130 min** | **26 min/unit at 5-batch** |

**Batch size efficiency:**

| Batch Size | Per-Unit Labor | Notes |
|------------|---------------|-------|
| 1 unit | ~45 min | Setup overhead dominates; avoid |
| 5 units | ~26 min | Practical minimum for efficient operation |
| 10 units | ~23 min | Optimal for Month 1–2 output |
| 20 units (two plates) | ~21 min | Month 3+ target; parallelized post-processing |

---

### 1.4 Post-Processing Detail

**Cool-down (unattended, 3–4 hours):**
PLA on the X1 Carbon's flexible PEI plate releases cleanly once the bed cools below 40°C. Do not harvest early — warm PLA deforms under pressure from the flex maneuver.

**Harvest sequence (30 seconds per plate):**
1. Flex PEI plate slightly to the left, then right — clips pop free
2. Sweep into harvest bin with single hand motion
3. Visual scan: look for obvious stringing across bore, layer separation at rim, warping on base (3 seconds per clip)
4. Reload plate to printer; confirm next job queues in Bambu Cloud
5. Move harvest bin to QC station

**Brim removal:**
With flexible PEI, brims peel at the plate edge before harvest. Budget 2 seconds per clip. If brims are not releasing cleanly, the plate is too warm — extend cool-down by 30 minutes.

**Cleaning (only if needed — Month 1 assess):**
Hot water + soft brush removes any stringing or debris. Dry fully before packaging — damp PLA in a sealed box causes surface cloudiness within 48 hours. If self-supporting design eliminates all support scars, this step may be skippable for most units.

---

## Part 2: Batch Queueing Strategy

### 2.1 Single-Printer Weekly Schedule (Month 1–3, 5–20 units/week)

**Bambu X1 Carbon print time estimates:**
- 10-clip plate: ~65 minutes
- 5-clip plate: ~40 minutes
- Cool-down + harvest + reload: 20 minutes

**Operating cycle (stagger prints to overlap with post-processing):**

| Day | Morning | Afternoon/Evening | Notes |
|-----|---------|-------------------|-------|
| Monday | Batch 1 starts (5 clips, 40 min print) | Harvest B1 → post-process → QC | Week kickoff; calibrate first |
| Tuesday | Batch 2 starts (10 clips) | B1 packaged → B2 cool-down + harvest | Parallel: B2 printing while B1 ships |
| Wednesday | Batch 3 starts (10 clips) | B2 post-process + pack → B3 harvest | Rhythm established |
| Thursday | Batch 4 (if demand) | B3 post-process + pack → label run | Pirate Ship batch labels for week |
| Friday | Buffer/reprint slot | Weekly QC review, reorder filament | Check inventory levels |

**Output ceiling (single printer, 4 days active):** ~25–30 units/week at sustainable pace.

**Thermal recovery:** The X1 Carbon's active cooling means there is no meaningful inter-batch thermal recovery needed at PLA temperatures. The 20-minute cool-down between print completion and next job start is driven by plate cooling for part release, not printer thermal management. Consecutive plate prints are fine.

---

### 2.2 Daily Operations Checklist (Printable)

**USE THIS EVERY OPERATING DAY.**

```
ModRun Daily Ops Checklist — Date: ___________

MORNING (15 min)
[ ] Check Bambu Cloud for overnight print status / alerts
[ ] Harvest any completed overnight batch (flex plate, sweep to bin)
[ ] Visual QC sweep: stringing? warping? obvious rejects? → reject bin
[ ] Reload plate for next batch; confirm correct 3MF file loaded
[ ] Check filament remaining on active spool (reorder if <200g)
[ ] Review Etsy orders received overnight — note any priority (ship today) orders

PRODUCTION (ongoing)
[ ] Post-process previous batch while current batch prints
[ ] Cool-down: wait until bed reads <40°C before harvesting
[ ] Support/brim removal: flex plate, sweep, inspect
[ ] Cleaning: hot water + brush if needed; dry fully
[ ] QC: pass/fail each unit per checklist (Part 3.2)
[ ] Reject bin: log defect type + unit ID in spreadsheet

PACKAGING
[ ] Pick units from finished-goods bin
[ ] Box each order: clip + rail in Kraft 6×4×2", tissue padding
[ ] Verify contents match Etsy order (SKU, quantity, color)
[ ] Stage for label printing

FULFILLMENT (once daily, batch)
[ ] Open Pirate Ship → import Etsy orders (auto-sync)
[ ] Batch print all labels — select all pending, click print (Rollo X1040)
[ ] Affix labels, seal boxes
[ ] Stage outbound pile for USPS pickup / drop-off
[ ] Confirm Etsy auto-uploads tracking (verify 1–2 orders)

END OF DAY
[ ] Queue next print batch before leaving (overnight or next-morning start)
[ ] Top up filament spool if <300g remaining (swap now to avoid midnight runout)
[ ] Log units produced today: _____ | Rejects: _____ | Shipped: _____
[ ] Check low-inventory SKUs — add to print queue if below 5-unit buffer
```

---

### 2.3 Parallel Post-Processing Workflow

**What can run simultaneously vs. sequentially:**

| Activity | Runs While Printer Is... | Notes |
|----------|--------------------------|-------|
| Current batch printing | Printing | Do post-processing on previous batch while printer runs |
| Cool-down | Idle (waiting for bed to cool) | Use this 20 min: check Etsy, print labels, pack orders |
| Harvest + brim removal | Idle (reloading) | 30 sec per plate, then start next job immediately |
| QC inspection | Previous batch post-processing | Inspect while next print runs |
| Label printing + packing | Printing | Fully parallel; entirely separate workflow |
| Filament spool swap | Brief pause (2 min) | Pre-stage spare spool to minimize idle time |

**The key insight:** At any given moment during operating hours, the printer should be printing AND the operator should be doing post-processing or fulfillment on a previous batch. A printer idle while the operator is not actively using it is wasted throughput.

---

## Part 3: Quality Gates and Failure Recovery

### 3.1 Acceptance Criteria

**Dimensional tolerances (from manufacturing-automation-architecture.md):**

| Dimension | Nominal | Acceptable Range | Reject Trigger |
|-----------|---------|-----------------|----------------|
| Clip width (cable channel) | Design spec | ±0.5mm | >0.5mm deviation |
| Clip depth (mount face) | Design spec | ±0.3mm | >0.3mm deviation |
| Snap-arm thickness | Design spec | ±0.4mm | >0.4mm or visible under-extrusion |
| Rail bore | 6.0mm / 8.0mm / 12.0mm | ±0.5mm | >0.5mm from nominal |
| Overall length | Design spec | ±0.5mm | >0.5mm deviation |

**FDM reality check:** A calibrated X1 Carbon achieves ±0.1–0.2mm repeatability. The ±0.3–0.5mm acceptance bands are deliberately wider than the printer's capability — they account for filament diameter batch variation and ambient temperature swings without creating excessive reject rates. At these bands, expected reject rate is 1–2%.

**Functional tests:**

| Test | Method | Pass | Fail |
|------|--------|------|------|
| Snap-arm engagement | Insert and remove a reference cable 5× | Smooth click, no grinding, no rattle | Binding, cracking, or play |
| Load retention | Mount clip, hang 300g weight for 30 seconds | Clip stays mounted | Clip releases or deforms |
| Bore clearance | Pass target cable diameter through bore | Slides freely | Tight binding or rattling loose |

**Surface finish:**

- Accept: visible layer lines (inherent to FDM), uniform color, seam on inside face, minor brim removal marks on underside
- Reject: stringing across bore interior (functional interference), visible delamination (layer gaps), burn marks, color contamination, warping detectable by eye

---

### 3.2 Quality Gate Decision Tree

```
Unit harvested from plate
          |
          v
VISUAL SWEEP (3 seconds per unit)
          |
    ┌─────┴─────┐
  OBVIOUS    NO OBVIOUS
  DEFECT      DEFECT
    |            |
    v            v
Stringing    To finished-
across bore? goods bin
    |            |
   YES    Every 50th unit?
    |        YES    NO
    v         v     v
→ REJECT  FUNCTIONAL  → Pack
  BIN      SNAP TEST
           |
      ┌────┴────┐
    PASS      FAIL
      |          |
      v          v
   → Pack    100% BATCH
             INSPECT
                |
        ┌───────┴────────┐
     ISOLATED         PATTERN
     FAILURE          FAILURE
        |                |
        v                v
  → Reject 1       Root cause
    Add to        investigation
   next batch     (see 3.3)
```

**Dimensional check (sampled, not 100%):** Caliper-measure snap-arm thickness on every 20th unit. If any measurement is outside the acceptance band, measure the next 10 units. If 2+ are outside the band, halt and investigate slicer or calibration.

---

### 3.3 Failure Recovery Protocols

**Print failure during job:**

| Failure | Auto-detect? | Recovery |
|---------|-------------|---------|
| Nozzle jam | Yes (X1 Carbon detects, pauses) | Clear jam manually (15 min); resume if <50% complete |
| First-layer adhesion failure | Yes (camera, spaghetti detection) | Cancel job; run auto bed-leveling; restart |
| Filament runout | Yes (AMS sensor) | Auto-pause; load new spool; resume |
| Power loss | No | Print lost; restart job from beginning |
| Color contamination | No | Cancel job; run AMS purge cycle (3g purge); reprint |

**Post-production defects:**

| Defect Pattern | Diagnosis | Action |
|----------------|-----------|--------|
| Single unit reject (<2% rate) | Normal FDM variance | Add to reject bin; reprint 1 unit in next batch |
| Batch reject rate 3–5% | Filament moisture, temperature drift | Dry active spool 6 hours; recheck nozzle temp |
| Batch reject rate >5% | Slicer profile issue or printer calibration | Halt production; run full X1 Carbon calibration suite; reprint 5-unit test plate before resuming |
| Systematic dimensional error (all units same dimension off) | FDM_TOLERANCE drift between filament brands | Rerun CadQuery with adjusted tolerance; new test print required |
| Stringing on all units | Retraction settings; temperature too high | Adjust retraction +0.5mm in slicer profile (version bump); retest 1 plate |

**Customer replacement protocols:**

| Situation | Response | Free Replacement? |
|-----------|----------|------------------|
| Customer reports clip doesn't fit cable | Ask for cable diameter; ship correct bore size | Yes, 1× |
| Customer reports snap-arm broke within 30 days | Standard use failure; design or QC issue | Yes, 1× (+ investigate batch) |
| Customer reports snap-arm broke after 90 days | Normal wear; politely explain FDM limitations | Discount code for repurchase, not free |
| Customer reports broke immediately on first install | Likely bad unit passed QC | Yes, 1× + apology note |
| Customer requests refund without return | Evaluate review risk; replace if <$15 at stake | Yes — losing $15 to protect reviews is correct |

**Acceptable replacement rate:** Under 1% of shipped units. At 5/week volume, this is less than 1 replacement per 20 weeks. Budget $15/month for replacement COGS in Month 1–2.

**When a single customer complaint triggers a production review:**
- If the complaint describes a specific failure mode (e.g., "snap arm cracked on second install"), pull the last 20 units from the same batch and run functional snap test on 5 of them
- If 2+ fail: that batch has a latent QC issue; proactively reach out to anyone from that batch with a discount or replacement offer before they leave a review

---

## Part 4: Monthly Volume Projections

### 4.1 Six-Month Scaling Roadmap

**Demand is the constraint, not printer capacity.** A single X1 Carbon running 5 days/week can produce 25–30 units/week. Demand in Month 1 is unlikely to exceed 5–10 units/week organically. The operational goal in Month 1–2 is to build review velocity (10+ reviews) and Etsy ranking, which unlocks organic demand in Month 3+.

| Month | Units/Week | Units/Month | Weekly Labor Hours | Per-Unit Labor | COGS/Unit | Revenue/Month | Gross Profit/Month |
|-------|-----------|-------------|-------------------|----------------|-----------|---------------|-------------------|
| 1 | 5 | 20 | 2.5 hrs | 35 min | $1.03 | $500 | $420 |
| 2 | 10 | 40 | 4.5 hrs | 28 min | $1.03 | $1,000 | $840 |
| 3 | 15 | 65 | 7 hrs | 26 min | $1.03 | $1,625 | $1,365 |
| 4 | 20 | 80 | 8 hrs | 25 min | $1.03 | $2,000 | $1,680 |
| 5 | 30 | 120 | 12 hrs | 24 min | $0.94* | $3,000 | $2,575 |
| 6 | 50 | 200 | 18 hrs | 23 min | $0.94* | $5,000 | $4,313 |

*Month 5+ assumes bulk filament pricing at eSUN 10kg bundle ($11.50/kg vs. retail $15/kg). COGS drops from $1.03 → $0.94/unit.

**Revenue assumes $25/unit blended average** (mix of single clips at $14.99 and rail+clip bundles at $38.99). This is conservative relative to the pricing-strategy.md tiered model.

**Labor cost note:** Per-unit labor times are active operator time. At $15/hr self-labor imputed cost, Month 1 labor cost adds $8.75/unit to landed cost. This is not a real cash expense in Month 1 — it becomes relevant when labor must be hired (Month 5+).

---

### 4.2 Per-Unit Economics Detail

**At $25 blended sale price (rail + clip bundle primary):**

| Cost Component | Per Unit | Source |
|----------------|---------|--------|
| Filament (12g clip + 15g rail, 27g total) | $0.40 | $15/kg retail; drops to $0.31 at bulk |
| Electricity | $0.02 | X1 Carbon 250W × 1.1 hr × $0.17/kWh |
| Printer depreciation | $0.09 | $1,199 / 5-year life / usage hours |
| Consumables (nozzle wear, PEI) | $0.01 | |
| Packaging (box + padding + tape) | $0.20 | Kraft box $0.15 + tissue/padding $0.05 |
| Etsy fees (6.5% listing + 3% transaction + $0.20) | $2.00 | On $25 sale |
| Shipping (USPS Ground Advantage via Pirate Ship) | $5.50 | Blended zones 1–5, 8 oz |
| **Total variable cost** | **$8.22** | |
| **Gross margin per unit** | **$16.78 (67%)** | |

**COGS (manufacturing only, $1.03) is materially different from total landed cost ($8.22) because shipping and Etsy fees are the dominant variable costs, not materials.**

---

### 4.3 Breakeven Analysis

From manufacturing-automation-architecture.md: **breakeven is 122 units/month** on fixed overhead (~$570/month: depreciation, electricity, software, packaging materials).

- Month 1 (20 units): Below breakeven on fixed overhead — absorb as startup cost
- Month 2 (40 units): Still below breakeven
- Month 3 (65 units): Approaching breakeven
- Month 4 (80 units): Above breakeven — every unit contributes pure margin
- Month 5+ (120+ units): Solidly profitable; automation ROI calculations become relevant

**Cumulative COGS, labor, and revenue by month:**

| Month | Cumul. Units | Cumul. Revenue | Cumul. COGS | Cumul. Labor Cost | Cumul. Gross Profit |
|-------|-------------|----------------|-------------|-------------------|---------------------|
| 1 | 20 | $500 | $21 | $23 | $456 |
| 2 | 60 | $1,500 | $62 | $90 | $1,348 |
| 3 | 125 | $3,125 | $129 | $216 | $2,780 |
| 4 | 205 | $5,125 | $212 | $336 | $4,577 |
| 5 | 325 | $8,125 | $307 | $516 | $7,302 |
| 6 | 525 | $13,125 | $496 | $786 | $11,843 |

*Labor cost is imputed at $15/hr self-labor. Gross profit is revenue minus COGS and imputed labor — actual cash retained is higher if owner-operated.*

---

## Part 5: Supply Chain Integration

### 5.1 Filament Replenishment

| Volume Stage | Supplier | Format | Price/kg | Lead Time | Min Order |
|-------------|----------|--------|----------|-----------|-----------|
| Launch (M1–2) | eSUN via Amazon | 1kg spool | $15.00 | 1–3 days | 1 spool |
| Growth (M3–4) | eSUN via Amazon | 10kg bundle | $11.50 | 2–5 days | 1 bundle |
| Scale (M5–6) | Anycubic direct | 50kg pallet | $10.49 | 7–14 days | 50kg |

**Reorder trigger:** Reorder when active spool reaches 200g remaining. At 27g/unit, 200g is roughly 7 more units — enough for one more plate while the order arrives.

**Colors to stock:** Black (primary, ~60% of demand), white (~25%), one accent color (grey or blue, ~15%). Never stock more than 2 spool rolls of any color until you have verified demand velocity for that color.

**Emergency backup:** Keep 1 retail-price spool of black PLA+ on hand at all times. If the 10kg bulk order is delayed, you can continue production without interrupting orders.

---

### 5.2 Etsy Upload Workflow

**Listing cadence:**
- Week 1 post-test-print: Create and publish 3 core listings (single clip, rail+clip bundle, 3-pack)
- Week 2: Add color variants as additional photos / listing variations (not separate listings)
- Week 3+: Optimize based on Etsy Stats traffic data; update titles/tags for high-impression, low-click keywords

**Daily routine:**
- 5 minutes: Check Etsy Stats (impressions, clicks, conversion rate) — look for trends
- 2 minutes: Respond to any messages within 24 hours (critical for Star Seller status)
- Weekly: Review search terms in Etsy Stats → adjust 2–3 tags in lowest-performing listing

**Listing optimization cycle (every 2 weeks):**
1. Identify lowest click-through listing from Etsy Stats
2. Test one title/tag change
3. Wait 2 weeks for data
4. Keep change if impressions or sales improved; revert if not

---

### 5.3 Pirate Ship Fulfillment Integration

**Setup (one-time, 30 minutes):**
1. Create Pirate Ship account (free)
2. Connect Etsy shop under Integrations
3. Create saved package presets:
   - "Single Clip": poly mailer 6×4×2", 4 oz, USPS Ground Advantage
   - "Rail + Clip Bundle": Kraft 6×4×2" box, 8 oz, USPS Ground Advantage
   - "3-Pack Bundle": Kraft 8×6×3" box, 12 oz, USPS Ground Advantage

**Daily label batch (5 minutes):**
1. Open Pirate Ship → Orders → Import Etsy orders (auto-syncs every 15 min)
2. Select all pending orders
3. Match each to saved package preset by SKU
4. Click "Print All Labels" — Rollo X1040 prints in 90 seconds
5. Affix labels; stage for USPS pickup

**USPS free scheduled pickup:** Schedule via USPS.com. Carrier picks up from your door. No post office trip needed until volume exceeds 30 packages/day.

---

### 5.4 Inventory Buffer

**Pre-fulfillment storage:** Keep finished units in labeled bins (one per SKU, one per color). Do not mix SKUs in the same bin.

**Buffer targets:**
- Month 1–2: 5-unit buffer per active SKU (ship same-day from stock on most orders)
- Month 3+: 10-unit buffer per active SKU (2-week demand coverage)
- Never hold more than 30 units total until demand velocity is confirmed — unsold inventory is frozen working capital

**Storage space:** A 2-foot shelf (standard 72" shelving unit, one shelf) holds approximately 200 clips in labeled bins. This is sufficient through Month 4.

---

## Part 6: Automation ROI Analysis

### 6.1 AutoFarm3D Door Opener — ROI Table

**Product:** AutoFarm3D Door Opener for Bambu X1 Carbon (3DQue)
**Hardware cost:** $129/printer
**Software cost:** $9.99–$40/month (QuinlyVision AI detection)
**What it does:** Opens printer door post-job, uses toolhead to clear parts from VAAPR release bed, closes door, starts next job — unattended overnight

**Labor savings calculation:**
- Without AutoFarm3D: Operator must harvest each plate, reload, restart (20 min/cycle during day; overnight run stops at end of last queued job)
- With AutoFarm3D: Printer runs continuously overnight without intervention; morning harvest one accumulated bin
- Estimated labor savings: 1.5–2 hours/week at current 5-unit/week scale; 3–4 hours/week at 20-unit/week scale

| Units/Week | Labor Hours Saved/Week | Annual Labor Saved (at $15/hr) | Hardware ROI Weeks | Running Breakeven (hardware + 12mo software) |
|-----------|----------------------|-------------------------------|-------------------|---------------------------------------------|
| 5 | 1.5 hrs | $1,170 | 5.5 weeks | ~1 month |
| 10 | 2.5 hrs | $1,950 | 3.3 weeks | 3 weeks |
| 20 | 4 hrs | $3,120 | 2.1 weeks | 2 weeks |
| 50 | 6 hrs | $4,680 | 1.4 weeks | 1.5 weeks |

**Decision rule: Buy at ≥15 units/week sustained for 2 consecutive weeks.** Below that threshold, overnight runs are short enough that manual plate-clearing the next morning is not a meaningful labor cost. Above that threshold, the overnight throughput gain (an extra 10–15 units per night) pays for the hardware in weeks.

**Confidence note:** AutoFarm3D Door Opener was announced June 2025 at $129/unit. Shipping status as of May 2026 should be confirmed at shop.3dque.com before including in capital budget. Community reports on maker forums suggest units are shipping but with some lead time variability.

---

### 6.2 Other Automation Decision Points

| Tool | Cost | Trigger | ROI Logic |
|------|------|---------|-----------|
| SimplyPrint (farm management) | $0–$20/mo | Month 2 (add 2nd printer) | Reduces job queueing errors; not cost-positive until 2+ printers |
| Craftybase (inventory tracking) | $20/mo | Month 2 (~40 orders/month) | Automates COGS tracking for Schedule C; saves ~2 hrs/mo |
| Rollo X1040 label printer | $100 one-time | Month 1 (any Etsy sales) | Eliminates thermal label sheet waste; pays back in ~50 labels |
| Bulk filament (10kg bundle) | $115 vs. $150 retail | Month 2 (>3kg/month usage) | $35 savings per 10kg = ~50 units' worth of free COGS |
| Second printer (Bambu X1 Carbon) | $1,199 | Month 4–5 (sustained >25 units/week) | Single printer ceiling at 30 units/week; second printer doubles throughput |
| Part-time post-processor | $18/hr × 15 hrs/week | Month 5 (>40 units/week demand) | Frees operator from post-processing; ~$1,080/month labor cost |

---

## Part 7: Failure Recovery Quick Reference

### 7.1 Printer Failure Protocols

**Nozzle jam (most common, ~2% of print jobs):**
1. X1 Carbon auto-pauses and alerts
2. Cancel job in Bambu Studio if jam is mid-print
3. Cold pull: heat nozzle to 200°C, push filament through, pull at 90°C — removes debris
4. If jam repeats: replace nozzle (0.4mm brass, ~$5, stock 3 spares)
5. Reprint affected units; add to same batch

**Bed adhesion failure (rare, ~0.5% of jobs):**
1. Job likely fails in first 10 minutes — visually or via camera
2. Cancel immediately if spaghetti detected
3. Run X1 Carbon auto-bed-leveling (5 minutes)
4. Check PEI plate for contamination — wipe with 91% IPA
5. Restart job

**Filament runout:**
1. X1 Carbon AMS auto-pauses, alerts
2. Load new spool
3. Resume print — seam may be slightly visible at resumption point; acceptable for functional parts

**Printer offline / network issue:**
1. Check local Wi-Fi connection
2. Power cycle printer
3. If Bambu Cloud unavailable: jobs can be sent locally via USB or Bambu Studio LAN mode

---

### 7.2 Supply Chain Disruption Protocols

| Disruption | Impact | Response |
|-----------|--------|---------|
| Primary filament spool delayed | Print production pauses after emergency reserve exhausted | Always maintain 1 emergency retail-price spool; reorder at 200g remaining |
| Bambu X1 Carbon service issue | Production fully stopped | Contact Bambu support (1-year warranty); prepare 2-week pause comms for Etsy; update listings to "extended processing time" |
| USPS rate increase or service disruption | Shipping costs spike | Pirate Ship automatically applies new commercial rates; review pricing immediately; adjust listings if margin drops below 50% |
| Etsy policy change | Platform risk | Maintain direct email list from Day 1 (post-purchase follow-up); direct channel reduces Etsy dependency |

---

### 7.3 Six-Month Risk Register

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| Test print fails — design rework needed | 15% | 2–4 week delay | Already baked into task brief; use delay for Etsy copy and photo prep |
| Demand lower than forecast in Month 1–2 | 40% | Revenue below projection | Single printer handles 5–30 units/week with no fixed cost change; no downside exposure |
| Demand higher than forecast (good problem) | 20% | Backlog, negative reviews if ship time slips | Update Etsy processing time to 5–7 days; queue batches; order AutoFarm3D immediately |
| Key component (X1 Carbon) hardware failure | 5%/year | Full production stop | In-warranty for 12 months from purchase; expedite Bambu service; consider renter's insurance on equipment |
| Etsy delists listing for policy issue | 8% | Revenue disruption | Original-design CadQuery provenance is timestamped in git — this is the strongest defense; respond to any notice within 24 hours with documentation |

---

## Part 8: Implementation Sequence

**Day 0 (test print approval day):**
- [ ] Lock confirmed FDM_TOLERANCE value; regenerate STLs
- [ ] Create and save `ModRun-PLA-Production-v1` slicer profile in Bambu Studio
- [ ] Save 10-clip and 5-clip production plate 3MF files
- [ ] Order 2× eSUN PLA+ 1kg spools in black (retail; bulk order follows in Month 2)
- [ ] Order 100× Kraft 6×4×2" boxes and 100× poly mailers

**Week 1 (first production run):**
- [ ] Run 1 batch (5 units) — document actual print time, post-processing time, and QC findings
- [ ] Set up Pirate Ship account; create package presets; print first test label
- [ ] Photograph products (follow post-test-print-doc-3-lifestyle-photography-brief.md)
- [ ] Create Etsy listings in draft mode (use post-test-print-doc-2-etsy-listing-design-templates.md)
- [ ] Publish listings (Thursday 10am–2pm optimal window)

**Week 2–4 (operations establishment):**
- [ ] Run 2–3 batches/week; refine daily ops checklist timings from actuals
- [ ] Set up Craftybase (Studio plan); sync Etsy shop
- [ ] Build 5-unit buffer stock before promoting listings
- [ ] Enable Etsy ads at $1/day budget; monitor CTR

**Month 2 (scaling up):**
- [ ] Order eSUN 10kg bundle when first spool (1kg) is 80% consumed
- [ ] Evaluate AutoFarm3D if producing 15+ units/week
- [ ] Add 3-pack bundle listing to Etsy
- [ ] Review and update slicer profile version if any systematic QC issue discovered

**Month 3–6 (growth mode):**
- [ ] Assess second printer at sustained >25 units/week for 2 weeks
- [ ] Evaluate part-time help at >40 units/week (post-processing + packing)
- [ ] Launch secondary product (Desk Headphone Hook per product-line-strategy.md) using same production workflow
- [ ] Monthly: review COGS model against actual; adjust pricing if filament costs change

---

## Confidence and Open Items

**High confidence (verified against existing mfg-farm docs):**
- COGS figures ($1.03/clip, $0.94 at bulk pricing) from manufacturing-automation-architecture.md Section 5
- Breakeven 122 units/month from manufacturing-automation-architecture.md Section 5.6
- Bambu X1 Carbon print parameters from manufacturing-automation-architecture.md Section 1.2
- Pirate Ship rate estimates from manufacturing-automation-architecture.md Section 3.4
- AutoFarm3D $129 hardware cost from manufacturing-automation-architecture.md Section 1.3

**Medium confidence:**
- Post-processing time estimates (9 min/unit support removal, 6 min cleaning) are reasonable for self-supporting PLA+ on flexible PEI, but actual time will depend on design geometry. Confirm from first production run.
- 35-minute per-unit baseline assumes supports are present. If test print confirms zero-support design (which is the target per manufacturing-automation-architecture.md Section 1.3), actual post-processing time is closer to 5–8 min/unit — better than the estimates above.
- AutoFarm3D shipping status and exact pricing: verify at shop.3dque.com before ordering

**Open items requiring test print data:**
- Exact clips per plate (estimated 10–12 based on X1 Carbon 256×256mm build area and estimated clip footprint)
- Actual print time per 10-clip plate (estimated 55–70 minutes; varies with geometry)
- Whether support removal is needed at all (depends on geometry angles in final design)
- Confirmed FDM_TOLERANCE value (expected 0.10–0.20mm; determines production STL parameters)

---

*Version 1.1 — Updated 2026-05-06*
*Next review: Post-test-print (May 15–20, 2026)*
*Related: manufacturing-automation-architecture.md, post-test-print-workflow.md, etsy-shop-launch-kit.md*
