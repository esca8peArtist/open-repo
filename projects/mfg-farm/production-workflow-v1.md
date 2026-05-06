---
title: ModRun Production Workflow v2.0 — Post-Test-Print Operational Guide
date: 2026-05-06
status: production-ready
version: 2.0
scope: STL approval through 6-month scale-up — all post-test-print operations
related: manufacturing-automation-architecture.md, post-test-print-workflow.md, scaling-production-research.md, supplier-economics.md, etsy-shop-launch-kit.md, pricing-strategy.md
confidence: high
printer-model: Bambu P1S (primary reference throughout)
---

# ModRun Production Workflow v2.0

**Purpose:** Eliminate post-test-print planning paralysis. This document activates immediately when the test print passes. Every operational decision below is pre-made so Month 1 supplier ordering, Etsy listing creation, and fulfillment setup begin within 24 hours of test-print approval.

**Lead finding:** Printer capacity on a single Bambu P1S running 12-clip overnight plates far exceeds expected Month 1-3 demand — one printer can produce 120+ clips per day at full utilization. The binding constraint through Month 4 is not hardware; it is demand. The correct early-stage strategy is disciplined batch consolidation (12-clip plates, never partial plates) and parallelizing post-processing with active print jobs. Adding a second printer is justified only when the single P1S sustains above 80% utilization for two consecutive weeks. Before that threshold, a second printer adds cost, not capacity you need.

**Printer model note:** All parameters in this document reference the Bambu P1S (256x256mm build area, active cooling, AMS, $699 MSRP). Sections 6.1 and 6.2 note where the X1 Carbon ($1,199) would differ in the automation context.

---

## Part 1: Post-Test-Print Approval Workflow

### 1.1 Test Print Outcomes (May 6-15 Window)

The test print answers four questions. Answers determine the day-zero action:

| Gate | Pass Criterion | Fail Criterion |
|------|----------------|----------------|
| Snap arm function | Click-fit engages smoothly, no rattle, no play | Arm cracks, doesn't click, or rattles under cable load |
| Dimensional tolerance | Snap arm 1.35-1.45mm; bore within +/-0.5mm nominal | Any measurement outside the acceptance band in Section 3.1 |
| Support removal | Clean release, no surface damage at support interfaces | Torn surface, visible scar >1mm on functional face |
| Finish quality | Layer lines visible but uniform; no stringing across bore | Stringing inside bore, warping on base, blobs on exterior |

**Decision tree:**

- PASS (4/4): Proceed immediately — lock STL, lock slicer profile, begin production
- NEAR-PASS (3/4): Adjust FDM_TOLERANCE in CadQuery, reprint targeted component (1 day turnaround)
- FAIL snap arm only: Increase nozzle temp to 225C, verify min layer time 8 sec, reprint (same day)
- FAIL (<3/4): Geometry iteration required (2-3 weeks); do not order bulk filament until re-test passes

**This document assumes the test print PASSES.**

---

### 1.2 STL Lock and Slicer Calibration (Day 0 — 60 minutes)

**After test print approval, execute these steps in sequence. Do not skip or reorder.**

**Step 1: Record and lock FDM_TOLERANCE**

The test print was sliced at FDM_TOLERANCE = 0.15mm (default in CadQuery source). Based on snap-fit behavior:

| Observed behavior | Diagnosis | Action |
|---|---|---|
| Snaps tight with definite click, holds cable, releases cleanly | 0.15mm is correct | Lock at 0.15mm — proceed |
| Snaps tight but cable removal requires force | Slightly undersize | Adjust to 0.17mm |
| Click present but cable rattles or falls out | Slightly oversize | Adjust to 0.12mm |
| No click, arm must be forced | Material too stiff at this geometry | Check nozzle temp (must be 222+) and wall count (must be 4); reprint before adjusting tolerance |

**Step 2: Regenerate production STLs**

Run from repo root after confirming FDM_TOLERANCE value:

```bash
uv run python cadquery/modrun_clip_b123d.py --bore 6 --tolerance [confirmed] --output-dir stl/v1.0/
uv run python cadquery/modrun_clip_b123d.py --bore 8 --tolerance [confirmed] --output-dir stl/v1.0/
uv run python cadquery/modrun_clip_b123d.py --bore 12 --tolerance [confirmed] --output-dir stl/v1.0/
uv run python cadquery/modrun_rail_b123d.py --variant desk_clamp --output-dir stl/v1.0/
uv run python cadquery/modrun_rail_b123d.py --variant adhesive --output-dir stl/v1.0/
```

Commit to git immediately with tag `v1.0` and the confirmed tolerance value in the commit message. The `/stl/v1.0/` directory is write-protected from this point — any future design change goes to `/stl/v1.1/`.

**Step 3: Create and lock the production slicer profile**

In Bambu Studio, create profile named `ModRun-PLA-Production-v1`. Settings below are locked for production. Changes require an explicit version bump and a validation plate before resuming production.

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Layer height | 0.20mm | Speed/strength balance; 0.15mm adds 25% print time with no functional gain for cable clips |
| Wall loops | 4 | 3 is minimum for snap arm integrity; the 4th wall adds critical material at the arm root |
| Infill | 20% gyroid | Omnidirectional strength distribution; gyroid prevents directional weakness along snap axis |
| Outer wall speed | 200 mm/s | P1S production sweet spot; any faster degrades dimensional accuracy at snap arm |
| Inner wall speed | 300 mm/s | No quality impact at this speed |
| Infill speed | 300-500 mm/s | Negligible effect on quality; maximize |
| Minimum layer time | 8 seconds | Non-negotiable for snap arms; without this, nozzle deposits on still-molten plastic at arm tip |
| Supports | None | Both clip and rail designed support-free in default orientation |
| Brim | 3mm removable | Bed adhesion; peels cleanly on flexible PEI |
| Seam position | Back-aligned | Seam artifact on non-visible inside face |
| Nozzle temp | 222C | PLA+ optimal; 220C minimum for interlayer adhesion at 1.4mm snap arm section |
| Bed temp | 55C | Standard PLA+ adhesion on PEI |
| Cooling fan | 100% after layer 4 | PLA needs rapid cooling for feature definition; early layers need less for bed adhesion |
| Z-seam position | Back | Seam placed at rear face, away from functional snap arm surface |

**Step 4: Save production plate 3MF files**

Once the production profile is confirmed on the first plate, save the full plate configuration (not just the profile) as named 3MF files. Loading a 3MF requires zero setup decisions — plate layout, profile settings, and filament assignment are all encoded.

- `modrun-plate-12x-6mm-v1.0.3mf` — 12-clip plate, 6mm bore (primary production file)
- `modrun-plate-12x-8mm-v1.0.3mf` — 12-clip plate, 8mm bore
- `modrun-plate-12x-12mm-v1.0.3mf` — 12-clip plate, 12mm bore
- `modrun-plate-mixed-rail4clip-v1.0.3mf` — 1 rail + 4 clips, maximizes build volume
- `modrun-plate-1rail-desk-v1.0.3mf` — single desk clamp rail
- `modrun-plate-1rail-adhesive-v1.0.3mf` — single adhesive rail

**Never print from the STL directly in production. Always load the versioned 3MF.**

**Step 5: Day 0 material and packaging orders**

- Order 2x eSUN PLA+ 1kg spools in black (~$15.90/spool, Amazon Prime, 1-2 day delivery)
- Order 1x eSUN PLA+ 1kg in white
- Order 100x 6x4x2" kraft mailer boxes (MrBoxOnline: ~$0.63/box at 50-count, $31.50/bundle; or ULINE S-13913 for premium corrugated at slightly higher price — either works)
- Order 100x 6x9" poly mailers for clip-only orders (Amazon: ~$0.07/ea at 100-count)
- Order 1x roll thermal label tape for Rollo printer if not yet purchased

---

### 1.3 Per-Unit Step Timeline (Clock-Time Reference)

**This is the canonical step-by-step for a 10-unit production run. All times are active operator time unless marked [unattended].**

**Day 0 (evening, 20 minutes active):**

| Clock | Step | Active Time | Cumulative |
|-------|------|-------------|------------|
| 8:00 PM | Load production 3MF, verify correct file version, start print | 5 min | 5 min |
| 8:05 PM | [Print running — printer unattended] | — | — |
| 8:05-9:00 PM | Approx. print time for 12-clip plate on P1S | [unattended] | — |
| 9:00 PM | P1S completion chime/alert via Bambu app | — | — |
| 9:00-12:00 AM | [Cool-down — unattended. Do not harvest. Bed must reach <40C for clean PEI release] | — | — |

**Day 1 (morning, 50-70 minutes active for 12-unit harvest + post-process):**

| Clock | Step | Active Time | Cumulative |
|-------|------|-------------|------------|
| 7:00 AM | Check Bambu app: confirm print complete, no failure alerts | 2 min | 2 min |
| 7:02 AM | Flex PEI plate front-back; clips release without tools — sweep to harvest bin | 1 min | 3 min |
| 7:03 AM | Visual Gate 1: 5 seconds per clip (look for stringing across bore, lifted corners, delamination) | 1 min | 4 min |
| 7:04 AM | Reload plate for next batch; load correct 3MF; start print | 3 min | 7 min |
| 7:07 AM | [Next batch printing — printer unattended] | — | — |
| 7:07 AM | Move harvest bin to QC station | 0.5 min | 7.5 min |
| 7:08 AM | Brim removal: for any brims still attached, flex at edge (should be pre-released on PEI) | 2 min | 9.5 min |
| 7:10 AM | Stringing removal: tweezers through bore on any units with stringing | 3 min | 12.5 min |
| 7:13 AM | Cleaning: hot water + soft brush on any units with surface debris; set on drying rack | 5 min | 17.5 min |
| 7:18 AM | Gate 2 dimensional check: caliper on 1 of 12 units (snap arm thickness, bore gap) | 2 min | 19.5 min |
| 7:20 AM | Gate 3 functional snap test: 1 unit per plate — press/release cable 5x, re-seat clip 3x | 1 min | 20.5 min |
| 7:21 AM | Transfer passing units to finished-goods bin; rejected units to scrap bin with defect note | 1 min | 21.5 min |
| 7:22 AM | [Packaging runs while next batch prints — parallel workflow] | — | — |
| 7:22 AM | Pick units for current orders from finished-goods bin; match to order queue | 2 min | 23.5 min |
| 7:24 AM | Box each order: place clip(s) in zip-lock bag inside kraft box or poly mailer | 5 min/5 units | 28.5 min |
| 7:29 AM | Add rubber bumper pads to any rail orders (4x per unit, pre-attached before boxing) | 1 min | 29.5 min |
| 7:30 AM | Pirate Ship: import Etsy orders, assign presets, batch print labels | 5 min | 34.5 min |
| 7:35 AM | Affix labels; seal boxes; stage for USPS pickup | 3 min | 37.5 min |
| 7:38 AM | Mark Etsy orders as shipped (auto-uploads tracking) | 1 min | 38.5 min |
| 7:39 AM | Log in QC spreadsheet: date, batch ID, units produced, rejects, defect types | 2 min | 40.5 min |

**Active operator time for a 12-clip harvest + packaging 5 orders: approximately 40 minutes.**

The next batch is already printing during the post-processing window. At 55-65 minutes print time per 12-clip plate, the operator finishes post-processing before the next plate is even done. This is the correct parallelized flow.

**Per-unit labor at different batch sizes:**

| Batch Size | Setup (fixed, min) | Post-process (variable, min) | Total active (min) | Per-unit labor |
|------------|-------------------|-----------------------------|--------------------|----------------|
| 1 unit (never do this) | 8 | 5 | 13 | 13 min/unit |
| 5 units | 8 | 25 | 33 | 6.6 min/unit |
| 12 units (target) | 8 | 40 | 48 | 4 min/unit |
| 24 units (two plates) | 10 | 75 | 85 | 3.5 min/unit |

**Labor bottleneck reality check:** At 12-clip batches, per-unit active labor is 4 minutes. At 50 units/week (5 plates), total weekly active labor is approximately 200 minutes (3.3 hours). Printing time is the printer's job, not the operator's. The operator's constraint is fulfillment throughput, not print supervision.

---

## Part 2: Post-Processing Detail

### 2.1 Cool-Down and Harvest Protocol

**Cool-down is unattended. Do not skip it.**

PLA on the P1S flexible PEI plate releases cleanly once the bed cools below 40C. Harvesting warm parts causes two failure modes:
1. PLA deforms under the flex-peel mechanical stress when still above glass transition temperature (~60C)
2. Dimensional measurements taken on warm parts underestimate true dimensions — caliper readings shift 0.1-0.3mm as parts cool fully

Expected cool-down times by part type:
- 12-clip plate: 20-30 minutes (small parts cool quickly; P1S active cooling accelerates this)
- Single rail (desk_clamp): 40-50 minutes (larger footprint holds heat; rushing causes clamp arm lift during removal)
- Single rail (adhesive variant): 30-40 minutes

**The P1S completion chime is not the harvest signal. The bed temperature display reading <40C is the harvest signal.**

**Harvest sequence (30 seconds per plate):**
1. Flex PEI plate slightly left, then right — clips release with a soft pop
2. Sweep all units into harvest bin in one hand motion
3. Reload plate to printer; confirm next job queued in Bambu Studio or SimplyPrint; start immediately
4. Move harvest bin to QC station

**Do not waste the cool-down window.** The 20-30 minute cool-down is when you check Etsy orders, generate shipping labels, pack previous-batch orders, and respond to messages. Cool-down = free fulfillment time.

### 2.2 Brim Removal

On the P1S flexible PEI plate, 3mm brims typically pre-release at the plate edges during the flex-peel harvest step. Budget 2 seconds per unit for any residual brim tabs. If brims are not releasing cleanly:
- Primary cause: plate too warm — extend cool-down by 15-20 minutes before next harvest
- Secondary cause: IPA wipe neglected — wipe PEI surface with 91% IPA before the current plate's next use

**If brims cause surface scarring on the clip base:** This is a cosmetic issue only. The base is the least visible face of the clip in use (it mounts to the desk rail). Accept surface marks on the base; reject marks on the snap arm or cable bore faces.

### 2.3 Stringing Removal

ModRun clips are designed support-free, but bridging stringing may occur across the cable bore opening depending on retraction settings, ambient temperature, and filament moisture content. Stringing across the bore interior is a functional defect (it reduces effective bore diameter and may prevent clean cable insertion).

**Removal:** Tweezers inserted through the bore, rotated 90 degrees, pulled out cleanly. Takes 10-15 seconds per unit. Rework rate will be near zero once the slicer profile is tuned; budget for it in the first 2-3 weeks of production while dialing in retraction.

**If stringing persists across more than 20% of units in a plate:** Increase retraction distance +0.5mm in the slicer profile. Create a new version: `ModRun-PLA-Production-v1.1`. Run a test plate before continuing production.

### 2.4 Cleaning Protocol

Cleaning is optional for most units in normal production. Apply only when:
- Stringing removal left residual debris inside bore
- Filament color contamination from AMS transition (a few units at the start of a color switch)
- Unit has visible surface dust from storage

**Cleaning procedure:** Warm water (not hot), soft-bristle brush (old toothbrush), 20 seconds per unit. Dry fully on rack — minimum 2 hours at room temperature, or 30 minutes in front of a fan. **Never package damp PLA.** Moisture sealed inside a closed box causes surface cloudiness within 24-48 hours.

### 2.5 Rail-Specific Post-Processing

Rails require approximately 45 seconds additional post-processing per unit:
1. Deburr slot entry points at both rail ends with the flat of a craft knife tip — 10-15 seconds (removes minor layer step artifact at the slot throat)
2. Run fingernail along clamp jaw underside — confirm no layer separation at Z-seam junction at arm-to-body transition
3. Attach 4x 3M SJ5302 rubber bumper pads to the clamp base underside (prevents desk scratch complaints) — pre-stage a small tray of bumpers adjacent to QC station; 15 seconds per rail

**Note on rails vs. clips:** Rails drive a disproportionate share of revenue (the starter bundle at $49.99 is the highest-margin SKU) but require 3-5x more print time and slightly more post-processing. Manage rail inventory print-to-order through Month 2; switch to 2-unit pre-built buffer when rail orders exceed 5/week consistently.

---

## Part 3: Batch Queueing Strategy

### 3.1 Single-Printer Weekly Schedule (Months 1-3)

**P1S print time estimates (confirmed range):**
- 12-clip plate: 50-65 minutes
- Single rail (desk_clamp): 150-180 minutes
- Single rail (adhesive): 120-150 minutes
- Plate cool-down + harvest + IPA wipe + reload: 25-30 minutes per cycle

**Operating cycle at 20 units/week (2 plates):**

| Day | Action | Notes |
|-----|--------|-------|
| Monday PM | Queue Plate 1 overnight (12 clips) | Start by 10 PM for morning harvest |
| Tuesday AM | Harvest Plate 1; start Plate 2 immediately | Post-process Plate 1 while Plate 2 prints |
| Tuesday AM-PM | Plate 2 runs; label and ship Plate 1 orders | Parallel workflow |
| Tuesday PM | Harvest Plate 2; post-process; package | |
| Wednesday | Fulfillment for Plate 2 orders; queue rail run if orders pending | Print rails during daytime (supervised start) |
| Thursday | Buffer/reprint slot; review QC log; reorder filament if <500g | |
| Friday | Weekly ops review; prep print queue for following week | |

**Output at this cadence:** 20-24 clips/week (2 plates) + 2-4 rails/week on-demand. Consistent with Month 2 volume targets.

**Operating cycle at 40-50 units/week (4-5 plates):**

| Day | Morning | Evening |
|-----|---------|---------|
| Monday | Harvest overnight plate; start Plate 2 | Queue Plate 3 overnight |
| Tuesday | Harvest Plate 3; start Plate 4 | Queue Plate 5 overnight |
| Wednesday | Harvest Plate 5; post-process; pack all week's orders | Rail run (daytime) |
| Thursday | Full fulfillment day; batch labels; USPS | Plate 6 overnight if backlog |
| Friday | Buffer; QC review; reorder filament | |

**Output:** 48-60 clips/week (4-5 plates) + 8-12 rails on-demand.

### 3.2 Cool-Down Time Between Batches

The P1S has no meaningful thermal recovery requirement between plates at PLA temperatures (the printer operates well below its heat limits). The inter-batch gap is driven entirely by plate cooling for part release, not printer thermal management.

**Inter-batch minimum gap:** 20 minutes from print completion to harvest (for clips on P1S with active cooling). Do not artificially extend this — the printer can begin the next job the moment you have harvested and reloaded the plate.

**Consecutive plate rule:** Running consecutive plates back-to-back is fine for clips. For rails, allow the build plate to cool fully before reloading — the larger rail footprint means the bed surface retains heat longer, and a partially warm plate on the second run increases first-layer adhesion variance.

**Overnight batch sequence:** The P1S can run multiple plates sequentially overnight if pre-queued in Bambu Studio. Queue 2-3 clip plates as a sequential queue before bed; harvest the accumulated bin in the morning. This is the primary throughput multiplier for a single-printer operation. Without AutoFarm3D (see Part 6), the printer stops after each plate completes. With AutoFarm3D or SimplyPrint FarmLoop, it auto-queues the next job immediately.

### 3.3 Parallel Post-Processing Workflow

**The interleave rule:** While the printer is running, the operator is doing something else. The printer is the production worker; the operator manages scheduling, QC, and fulfillment.

| Current batch status | Operator task | Notes |
|---------------------|---------------|-------|
| Plate 1 printing (50-65 min) | Post-process and pack previous batch | Full parallel — no dependency |
| Plate 1 cooling (20-30 min) | Check Etsy orders; generate labels; pack orders | Free parallel window |
| Harvest Plate 1 (2-3 min) | Plate swapped and queued | Brief hands-on; then back to parallel work |
| Plate 2 printing | Run Gate 2-3 QC on Plate 1 units; package fulfilled orders | Full parallel again |

**Effective operator hours per 12-clip plate cycle:** 40-45 minutes total active time, spread across a 90-minute real-time window (50 min print + cool-down + harvest). The remaining 45-50 minutes of that window are free for non-print tasks.

### 3.4 Daily Operations Checklist

Use this every operating day. Print and post at workstation.

```
ModRun Daily Ops — Date: ___________   Units in finished-goods stock: _____

MORNING (10-15 min)
[ ] Check Bambu app: overnight print status / failure alerts
[ ] Harvest any completed overnight batch (flex PEI plate, sweep to bin)
[ ] Visual Gate 1 sweep: stringing across bore? warping? delamination? → scrap bin
[ ] Reload plate; confirm correct 3MF version loaded; start print
[ ] Check filament remaining on active spool — reorder if <300g

REVIEW ORDERS (5 min)
[ ] Open Etsy Seller Dashboard: any new orders? priority today (ship by) orders?
[ ] Cross-check against finished-goods stock — any SKUs to print urgently?
[ ] Note any customer messages requiring response

PRODUCTION (while printer runs)
[ ] Post-process previous batch: brim removal, stringing removal, cleaning if needed
[ ] Gate 2: caliper on 1 unit per 20 — snap arm thickness, bore gap
[ ] Gate 3: functional snap test on 1 unit per plate
[ ] Transfer passing units to finished-goods bin; log rejects with defect type

PACKAGING (parallel with current print)
[ ] Pull units from finished-goods bin to match order queue
[ ] Box each order: clip(s) in zip-lock bag; clips-only into poly mailer; rail orders into kraft box
[ ] Rail orders: attach 4x rubber bumper pads before boxing
[ ] Verify contents match order SKU and quantity before sealing

FULFILLMENT (once daily batch)
[ ] Pirate Ship → import Etsy orders (auto-syncs; or manually import CSV)
[ ] Match all pending orders to saved package presets by SKU
[ ] Batch print all labels (Rollo printer: 90 seconds for up to 20)
[ ] Affix labels, seal boxes, stage outbound pile for USPS pickup
[ ] Mark all orders as shipped in Etsy (triggers automatic tracking emails)

END OF DAY
[ ] Queue next print batch (overnight start if possible)
[ ] Swap filament spool if <300g remaining
[ ] Log: units produced ___  |  rejects ___  |  shipped ___
[ ] Review low-stock SKUs — print queue if any below 5-unit buffer
[ ] Respond to any unanswered Etsy messages (24hr response required for Star Seller)
```

---

## Part 4: Quality Gates and Failure Recovery

### 4.1 Acceptance Criteria

**Dimensional tolerances:**

| Dimension | Acceptable Range | Reject Trigger |
|-----------|-----------------|----------------|
| Snap arm width at root | Design spec +/-0.4mm | >0.4mm deviation or visible under-extrusion |
| Snap arm minimum thickness | 1.2-1.6mm (nominal 1.4mm) | <1.2mm (fracture risk) or >1.7mm (no click) |
| Clip bore diameter | +/-0.3mm from nominal | >0.3mm — cable fit compromised |
| Rail slot width | +/-0.3mm | Clip will not seat |
| Overall clip length | +/-0.5mm | Cosmetic only; accept |

**FDM reality check:** A calibrated P1S achieves +/-0.1-0.2mm repeatability. The acceptance bands above are deliberately wider than the printer's natural capability — they account for filament diameter batch variation and ambient temperature swings. Expected reject rate at steady state: 1-3%.

**Functional tests:**

| Test | Method | Pass | Fail |
|------|--------|------|------|
| Snap arm engagement | Insert and remove a reference cable 5x | Smooth click, no grinding, no rattle | Binding, cracking, or play |
| Load retention | Mount clip to rail, hang 200g weight 30 seconds | Clip stays seated | Clip releases or visibly deforms |
| Bore clearance | Pass target-diameter cable through bore | Slides with light friction | Binding requiring force, or falls through |
| Snap arm flex recovery | Flex arm to 50% travel, release | Returns to neutral, no cracking | Set, permanent deformation, or crack |

**Surface finish:**
- Accept: visible layer lines (FDM inherent), uniform color, seam on inside face, minor brim removal marks on underside
- Accept on base face only: slight warping up to 0.5mm (base face is not visible in use)
- Reject: stringing across bore interior (functional interference), visible delamination (layer gaps), burn marks, color contamination, warping on snap arm face

### 4.2 Three-Gate QC Decision Tree

**Gate 1 — Visual (100% of units, 5 seconds each):**
At harvest. Every unit passes through Gate 1. This is not optional even at scale.

```
Unit in hand
    |
    v
Obvious defect? (stringing across bore, delamination, color contamination)
    |
   YES → Scrap bin
    |
    NO → Finished goods staging
```

**Gate 2 — Dimensional (sampled, 1:20 ratio):**
Caliper measurement of snap arm thickness and bore gap on every 20th unit. If a measurement is outside acceptance: measure the next 10 units. If 2+ out of spec: halt run, investigate.

**Gate 3 — Functional snap test (1 per plate):**
Run on one unit from each plate before the plate's units enter finished goods. If Gate 3 fails: stop production run entirely, do not ship from this plate. Diagnose before next plate.

**Sampling rates by volume:**
- Months 1-3: Gate 2 at 1:20; Gate 3 every plate
- Month 4+: Gate 2 stays at 1:20 (permanent); Gate 3 reduces to every other plate after 4 consecutive clean weeks

### 4.3 Failure Recovery Protocols

**Print failures during job:**

| Failure | Auto-detect? | Recovery |
|---------|-------------|---------|
| Nozzle jam | Yes (P1S pauses; alert sent) | Cold pull: 200C push-through, 90C pull-out; if jams repeat, replace 0.4mm nozzle (~$5; stock 3 spares) |
| Spaghetti / first-layer failure | Yes (camera AI detection) | Cancel immediately; run auto bed-level (5 min); wipe PEI with 91% IPA; restart |
| Filament runout | Yes (AMS sensor) | Auto-pause; load new spool; resume — seam visible at resumption point, acceptable for functional parts |
| Power loss | No | Job lost; restart from beginning |
| AMS color contamination | No | Cancel; run AMS purge cycle (3g purge filament); inspect next 2 units after restart |

**Post-production defects:**

| Pattern | Diagnosis | Action |
|---------|-----------|--------|
| Isolated unit reject (<3% rate) | Normal FDM variance | Scrap and add to next batch |
| Batch reject rate 3-8% | Filament moisture or temperature drift | Dry active spool in food dehydrator at 45C for 6 hours; recheck nozzle temp |
| Batch reject rate >8% | Slicer profile issue or printer calibration drift | Halt production; run full P1S calibration suite (bed leveling, flow calibration, resonance calibration); reprint 5-unit test plate before resuming |
| Systematic dimensional error (all units same dimension off) | FDM_TOLERANCE drift between filament brands | Rerun CadQuery with adjusted tolerance; new test print; new 3MF version |
| Persistent stringing across all units | Retraction settings or nozzle temp too high | Retraction +0.5mm; version-bump profile to v1.1; retest 1 plate |
| Snap arm fracture at root | Nozzle temp <218C, or min layer time <6sec, or wall count 3 instead of 4 | Verify profile settings; increase nozzle temp to 225C; reprint |

### 4.4 Customer Replacement Protocols

| Situation | Response | Free Replacement? |
|-----------|----------|------------------|
| Clip doesn't fit cable | Ask cable diameter; ship correct bore size | Yes, 1x (different SKU) |
| Snap arm broke within 30 days of normal use | Design or QC issue | Yes, 1x + note the batch in QC log |
| Snap arm broke on first installation | Bad unit that passed QC | Yes, 1x + apology insert in replacement package |
| Snap arm broke after 90 days | Normal wear; explain FDM limitations | 15% discount code for repurchase; no free replacement |
| Customer requests refund | If <$15 at stake, replace without return | Yes — protecting reviews at $15 is correct economics |
| Color complaint ("not quite what I expected") | FDM color variance is inherent | Offer partial refund (10-15%) or free future order; do not replace |

**Acceptable replacement rate:** Under 1% of shipped units. At 20/week volume, this is less than 1 replacement per 5 weeks. Budget $15-25/month for replacement COGS in Months 1-3.

**When a customer complaint triggers a production review:**
A complaint describing a specific failure mode (e.g., "snap arm cracked on second install") triggers a pull of 5 units from the same production day and lot for functional snap testing. If 2+ fail: that lot has a latent QC issue. Proactively contact anyone from that lot who has not yet left a review with a preemptive discount or replacement offer.

---

## Part 5: Packaging BOM and Fulfillment Setup

### 5.1 Packaging Bill of Materials

**Per SKU packaging, with current sourced pricing (May 2026):**

| SKU | Box/Mailer | Padding | Accessories | Label | Total Packaging COGS |
|-----|-----------|---------|-------------|-------|---------------------|
| Single clip (1x) | 6x9" poly mailer $0.07 | Bubble wrap pouch $0.04 | — | $0.01 | $0.12 |
| 3-clip bundle | 6x9" poly mailer $0.07 | Zip-lock bag $0.02 + kraft padding $0.02 | — | $0.01 | $0.12 |
| Rail only (desk_clamp) | 6x4x2" kraft box $0.63 | Kraft padding $0.05 | 4x 3M bumper pads $0.28 | $0.01 | $0.97 |
| Starter bundle (rail + 3 clips) | 6x4x2" kraft box $0.63 | Kraft padding $0.07 | 4x bumper pads $0.28, zip-lock bag $0.02 | $0.01 | $1.01 |

**Important correction from v1.1:** The prior version estimated kraft boxes at $0.15/unit. Current MrBoxOnline pricing shows $0.63/unit at 50-count quantities, dropping to $0.576/unit at 18+ bundles (900 units). The $0.15 figure was incorrect. Until order volume exceeds 500 boxes/quarter, budget $0.57-0.63 per kraft box. The per-unit economics in Section 7 reflect this correction.

**Supplier specifications:**
- Poly mailers: Shop4Mailers 6x9" self-seal, 2.35 mil — Amazon ASIN B07T7GKNBT, ~$7/100-pack
- Kraft boxes (6x4x2"): MrBoxOnline (mrboxonline.com) — 50-pack at $31.50; 18+ packs at $27.90/50-pack
- Bubble wrap pouches (clips): Amazon 100-pack self-seal pouches, ~$4/100
- 3M Bumper Pads (rails): Amazon SJ5302 clear bumpers, ~$7/pack of 100 units (4 per rail order = $0.28/order)
- Thank-you cards (optional): Vistaprint 500-run, $0.06/card

**Packaging station setup:** Allocate a 24x36" surface adjacent to the printer. Stage open boxes and pre-filled padding packets. Pre-open poly mailers in a dispenser stack. Keep rubber bumper pad tray permanently at station. A well-staged packaging station reduces per-unit packaging time by 30-40% versus reaching for each component separately.

### 5.2 Label Generation — Pirate Ship Integration

**One-time setup (30 minutes):**
1. Create Pirate Ship account at pirateship.com (free; no monthly fee; pay-per-label only)
2. Connect Etsy shop: Pirate Ship → Integrations → Etsy → authorize
3. Create saved package presets by SKU:
   - "Single Clip": poly mailer, 1.5 oz, USPS Ground Advantage
   - "3-Clip Bundle": poly mailer, 4 oz, USPS Ground Advantage
   - "Rail Only (Desk)": kraft 6x4x2" box, 7 oz, USPS Ground Advantage
   - "Starter Bundle": kraft 6x4x2" box, 11 oz, USPS Ground Advantage

**USPS Ground Advantage rate guidance (May 2026, Pirate Ship commercial below-retail rates):**
- Sub-1-pound packages: rates start well below the 1lb tier
- 1lb package: $5.30 (zones 1-4), approximately $5.90-6.70 for zones 5-8
- ModRun orders weigh 1.5-11 oz; blended shipping cost estimate $3.50-5.00 for zones 1-5, up to $5.50-6.50 for cross-country zones

**Practical guidance:** Use $4.50 as the blended shipping cost assumption for margin modeling. Zone mix for a US seller is roughly 40% zones 1-4, 40% zones 5-6, 20% zones 7-8. At these weights and a national zone mix, $4.25-5.00 is well-supported by prior research and current rate structure.

**Daily label batch (5 minutes for up to 20 orders):**
1. Pirate Ship auto-syncs Etsy orders every 15 minutes; or manually import
2. Select all pending orders
3. Assign each to saved package preset by SKU (takes seconds with presets set up)
4. Batch purchase all labels in one click
5. Rollo X1040 prints all labels in sequence (~90 seconds for 10 labels)
6. Affix, seal, stage for USPS pickup

**USPS free scheduled pickup:** usps.com/pickup — carrier picks up from your door daily. No post-office trip needed until volume exceeds 30 packages/day.

### 5.3 Inventory Buffer Management

| Volume Stage | Clip Buffer Target | Rail Buffer | Logic |
|-------------|-------------------|-------------|-------|
| Month 1-2 (5-20/week) | 8-10 clips per active SKU | 0 (print-to-order) | 2-week demand at low volume; never hold idle working capital |
| Month 3 (20-40/week) | 15-20 clips | 0-2 rails | 1-week buffer; clips can reprint overnight |
| Month 4+ (40-75/week) | 25-50 clips | 3-5 rails | Cover 3-day demand spike; rails switch to print-ahead at >5/week |

**SKU inventory discipline:** Label storage bins by SKU and color (e.g., "6mm clip — black," "8mm clip — white"). Never mix SKUs in a bin. A 2-shelf unit holds 200+ clips through Month 5.

**Reorder trigger for filament:** Reorder when active spool reaches 300g remaining. At 75g/clip + 135g/rail, 300g covers 4 clips or 2 rails — enough for one plate while the order arrives. Always maintain one emergency spool of black PLA+ at retail price.

---

## Part 6: Automation ROI Decisions

### 6.1 AutoFarm3D Door Opener

**Product:** AutoFarm3D Door Opener for Bambu X1 Carbon (made by 3DQue, shop.3dque.com)
**Hardware cost:** $129/printer
**Software:** QuinlyVision AI detection — $9.99-$40/month
**What it does:** Opens printer door post-job, uses toolhead to sweep parts from VAAPR release bed, closes door, starts next job — enabling true unattended overnight multi-plate production

**Compatibility note:** The AutoFarm3D door opener is designed for the X1 Carbon, not the P1S. The P1S door mechanism differs. Verify P1S compatibility at shop.3dque.com or on the 3DQue Discord before purchasing. SimplyPrint FarmLoop (see 6.2) achieves the job-queueing benefit without the physical door mechanism and works with both P1S and X1 Carbon.

**Decision rule: Evaluate at 15+ units/week sustained for 2 consecutive weeks.** Below that, overnight runs are short enough that manual harvest next morning is not a meaningful cost. Above it, each additional overnight plate-cycle (earning an additional 12 clips per plate unattended) pays for the hardware within weeks.

### 6.2 Automation Trigger Table

| Tool | Cost | Buy Trigger | ROI Logic |
|------|------|-------------|-----------|
| Rollo X1040 label printer | $100 one-time | Month 1 (immediately) | Eliminates inkjet per-label waste; pays back in ~50 labels; thermal label readability is noticeably better than inkjet for USPS scanning |
| SimplyPrint (farm management) | $0-$20/month | Month 2 or 2nd printer | FarmLoop enables sequential plate jobs without operator intervention; AI failure detection (included free hours); not cost-positive on 1 printer at <20 units/week |
| Craftybase (inventory tracking) | $20/month | Month 2 (~40 orders/month) | Automates COGS tracking for Schedule C; auto-calculates cost-of-goods sold per Etsy sale; saves 2-3 hrs/month of spreadsheet work |
| Bulk filament (10kg bundle) | $11.50/kg vs. $15.90 retail | Month 2 (>3kg/month usage at 12 clips/plate) | $44/10kg savings = 50+ clips' worth of free filament |
| Second printer (Bambu P1S) | $699 | Month 4-5 (sustained >25 units/week for 2 weeks) | Single P1S ceiling at 30 units/week (practical, not theoretical max); second printer doubles throughput; 5-week payback at 50 units/week |
| Part-time post-processor | $15-18/hr, 10-15 hrs/week | Month 5-6 (>40 units/week demand, packaging >2 hrs/day) | Frees operator for QC, listing management, new product development; $600-720/month |
| Dedicated shipping workstation | $200-400 (table, organizer, scale) | Month 3 (>20 orders/week) | Staging efficiency; reduces per-order pack time 30-40%; pay-as-you-go from revenue |

---

## Part 7: Monthly Volume Projections and Scaling Roadmap

### 7.1 Six-Month Demand and Production Schedule

**Assumption basis:**
- Demand is the constraint, not printer capacity. A single P1S can produce 120+ clips/day at full utilization.
- Month 1-2 demand is driven by Etsy algorithm indexing and initial review velocity, not marketing spend.
- Month 3+ organic demand accelerates if average rating is 4.8+ and listing is Etsy-SEO optimized.
- Revenue model uses $24.99 blended ASP per order (3-clip bundle primary, weighted with rail and starter bundle mix).

**Week-by-week early-phase production schedule:**

| Week | Units | Plates | Primary Activity | Notes |
|------|-------|--------|-----------------|-------|
| W1 (post-test) | 12 | 1 | Validation plate; QC; STL lock | Do not ship before Gate 3 passes |
| W2 | 12 | 1 | Photography session; Etsy listing creation | Publish Thursday-Friday |
| W3 | 24 | 2 | First orders (if any); operational rhythm | First label print; first ship |
| W4 | 24 | 2 | Build 10-unit buffer stock | Do not empty buffer to fill orders |
| W5 | 36 | 3 | Enable Etsy Ads $1/day | Monitor CTR vs. impressions |
| W6 | 36 | 3 | Review Week 5 ad data | Adjust 2-3 tags based on search term data |
| W7 | 36 | 3 | Add 6-clip kit listing | Demand signal: 3-pack selling? |
| W8 | 48 | 4 | Order 10kg filament bundle | First bulk purchase trigger |

**Month-by-month scaling roadmap:**

| Month | Units/Week | Units/Month | Plates/Week | Key Operational Event |
|-------|-----------|-------------|-------------|----------------------|
| 1 | 10 | 40 | 1-2 | STL lock, profile freeze, first Etsy listings, first reviews |
| 2 | 20 | 80 | 2-3 | Bulk filament order; Craftybase setup; Etsy Ads ramp |
| 3 | 35 | 140 | 3-4 | Near printer utilization ceiling; AutoFarm3D/SimplyPrint evaluation |
| 4 | 45 | 180 | 4-5 | Second printer decision point; rail inventory buffer starts |
| 5 | 55 | 220 | 5-6 (2 printers) | Second printer operational; part-time post-processor evaluation |
| 6 | 70 | 280 | 6-7 (2 printers) | Secondary product launch (Desk Headphone Hook); contractor hired |

### 7.2 Per-Unit Economics at Each Volume Stage

**Corrected COGS model incorporating accurate packaging costs:**

| Cost Component | Month 1-2 (5-20/wk) | Month 3-4 (30-50/wk) | Month 5-6 (50-70/wk) |
|----------------|--------------------|--------------------|-------------------|
| Filament (75g clip) | $1.19 ($15.90/kg retail) | $0.86 ($11.50/kg 10kg bundle) | $0.79 ($10.49/kg Anycubic pallet) |
| Electricity | $0.02 | $0.02 | $0.02 |
| Printer depreciation | $0.07 ($699/5yr) | $0.07 | $0.05 (second printer amortizes) |
| Consumables (nozzle, PEI) | $0.02 | $0.02 | $0.02 |
| Packaging (poly mailer + padding) | $0.14 | $0.12 | $0.10 |
| Scrap allowance (5% of filament cost) | $0.06 | $0.04 | $0.04 |
| **COGS per clip (manufacturing)** | **$1.50** | **$1.13** | **$1.02** |

**Note on v1.1 COGS figure ($1.03/unit):** The prior version underestimated packaging costs ($0.15 box vs. actual $0.57-0.63). The corrected figure is $1.50/clip at launch pricing. The gap narrows to $1.13 at bulk filament pricing (Month 3). This is still 6-23x cheaper than service bureaus and does not materially change the margin structure.

**Full per-order economics (3-clip bundle at $24.99 ASP):**

| Component | Month 1-2 | Month 3-4 | Month 5-6 |
|-----------|-----------|-----------|-----------|
| Gross revenue | $24.99 | $24.99 | $24.99 |
| Etsy fees (6.5% + $0.20 + ~3% payment) | -$3.55 | -$3.55 | -$3.55 |
| Net revenue received | $21.44 | $21.44 | $21.44 |
| COGS (3 clips) | -$4.50 | -$3.39 | -$3.06 |
| Packaging (poly mailer) | -$0.12 | -$0.12 | -$0.10 |
| Shipping (blended zones 1-5) | -$4.50 | -$4.50 | -$4.50 |
| **Net profit per order** | **$12.32** | **$13.43** | **$13.78** |
| **Net margin** | **49.3%** | **53.7%** | **55.1%** |

**AOV leverage reconfirmed:** Shipping ($4.50) and Etsy fees ($3.55) are fixed per order regardless of order size. Every $1 increase in AOV yields roughly $0.90 of additional net profit. The starter bundle at $49.99 (rail + 3 clips) produces:
- Net revenue: $46.44 (after Etsy fees)
- COGS: ~$5.20 (3 clips + rail materials)
- Packaging: $1.01
- Shipping: $5.00 (heavier, wider zone mix)
- **Net profit: $35.23 (70.5% margin)**

Pushing even 20% of orders toward the starter bundle materially improves total margin without any COGS or operational change.

### 7.3 Six-Month Revenue Projection

| Month | Units Shipped | Gross Revenue | Etsy Fees | Net After COGS + Shipping | Cumulative Net |
|-------|--------------|---------------|-----------|--------------------------|----------------|
| 1 | 40 | $1,000 | $95 | $493 | $493 |
| 2 | 80 | $2,000 | $190 | $1,074 | $1,567 |
| 3 | 140 | $3,500 | $333 | $1,880 | $3,447 |
| 4 | 180 | $4,500 | $428 | $2,414 | $5,861 |
| 5 | 220 | $5,500 | $523 | $2,950 | $8,811 |
| 6 | 280 | $7,000 | $665 | $3,754 | $12,565 |
| **Total** | **940** | **$23,500** | **$2,234** | **$12,565** | |

*Revenue model: $24.99/order average (3-clip bundle primary), 1 order = 1 unit in this model for simplicity. Real AOV with starter bundles and rail orders will be higher. Net calculation deducts Etsy fees, corrected COGS, and blended $4.50 shipping. Does not include imputed labor cost.*

**Breakeven:** Prior research established 122 units/month as the breakeven on fixed overhead (~$570/month including depreciation, electricity, software, packaging). Under the corrected COGS model, breakeven shifts slightly higher — approximately 135-140 units/month at Month 1-2 cost structure. Month 4 (180 units) is well above breakeven.

### 7.4 Per-Unit Labor Time and Scaling Curve

| Volume | Weekly Labor Hours | Per-Unit Active Labor | Labor as % of Net Revenue |
|--------|-------------------|----------------------|--------------------------|
| 10/wk (Month 1) | 1.5 hrs | 9 min | 26% (imputed $15/hr) |
| 20/wk (Month 2) | 2.5 hrs | 7.5 min | 22% |
| 40/wk (Month 3) | 4 hrs | 6 min | 18% |
| 60/wk (Month 4-5) | 5.5 hrs | 5.5 min | 16% |
| 100/wk (Month 6+) | 7 hrs | 4.2 min | 12% |

Labor amortization, not filament cost, drives the per-unit improvement from 10 to 100 units/week. The $3+ per-unit COGS drop from Month 1 to Month 6 is approximately: $0.40 filament savings + $2.70 labor amortization. Scaling is primarily a labor efficiency story.

---

## Part 8: Supply Chain Integration

### 8.1 Filament Replenishment Schedule

| Volume Stage | Supplier | Format | Price/kg | Lead Time | Reorder Trigger |
|-------------|----------|--------|----------|-----------|-----------------|
| Launch (M1-2) | eSUN via Amazon | 1kg spool ($15.90) | $15.90 | 1-3 days | 300g remaining |
| Growth (M2-3) | eSUN via Amazon | 10kg bundle (~$115) | $11.50 | 2-5 days | 2kg remaining |
| Scale (M4-6) | Anycubic direct | 50kg pallet (~$525) | $10.49 | 7-14 days | 10kg remaining |

**Color mix to stock (do not over-order):**
- Black: 60% of demand (never be out of stock on black)
- White: 25% of demand
- Grey or accent: 15% of demand
- Stock maximum 2 spools of any non-black color until demand velocity is confirmed

**Emergency reserve:** Always maintain 1 full retail-price black spool separate from production inventory. This is insurance, not inventory. Replenish it immediately after use.

### 8.2 Etsy Listing Cadence and Optimization

**Week 1 post-test-print:**
- Create 3 core listings in Etsy draft mode (use post-test-print-doc-2-etsy-listing-design-templates.md)
- Publish all listings Thursday 10AM-2PM for maximum initial indexing window

**Active SKUs at launch:**
- `MODRUN-CLIP-3PK` — 3-clip bundle, $24.99, available in black/white/grey
- `MODRUN-RAIL-DESK` — desk clamp rail, $34.99
- `MODRUN-BUNDLE-STARTER` — rail + 3 clips, $49.99 (highest-margin SKU; feature prominently)

**Daily platform routine:**
- 5 min: Etsy Stats review (impressions, clicks, conversion rate; note trends)
- 2 min: Respond to any messages (24-hour response = Star Seller requirement)
- Weekly: Pull Etsy Stats search terms — adjust 2-3 tags in lowest-CTR listing

**Optimization cadence:** Every 2 weeks, identify the lowest click-through listing and test one title or tag change. Hold for 2 weeks of data before evaluating. Do not make simultaneous changes to multiple listings — it prevents isolating what drove any improvement.

---

## Part 9: Six-Month Risk Register

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| Test print fails — design rework needed | 15% | 2-4 week delay | Already baked into timeline; use delay for Etsy copy and photo prep using existing test print units |
| Demand lower than forecast Months 1-2 | 40% | Revenue below projection | No downside: single printer at 10 units/week has the same fixed cost as at 30; demand is recoverable |
| Demand higher than forecast (good problem) | 20% | Order backlog; review risk if ship time slips | Update Etsy processing time to 7 business days; queue plates; order AutoFarm3D or second printer immediately |
| Key hardware (P1S) failure | 5%/year | Full production stop | Under 1-year warranty; Bambu support turnaround 3-5 days; update Etsy to extended processing; service bureaus for emergency gap |
| Etsy policy violation / listing removal | 8% | Revenue disruption | CadQuery source with git timestamps is original-design documentation — respond to any notice within 24 hours with provenance evidence |
| Filament tariff increase | 20% | COGS increase $1-3/kg | Maintain 2 supplier relationships (eSUN + Anycubic) for domestic-warehouse stock; US-manufactured filament (HATCHBOX) as domestic backup at ~$22/kg |
| USPS rate increase | Annual certainty | Shipping cost spike | Pirate Ship auto-applies new commercial rates; review margin immediately; adjust listed prices if margin drops below 45% |

---

## Part 10: Implementation Sequence

### Day 0 (Test Print Approval — 60 minutes)
- [ ] Record confirmed FDM_TOLERANCE; regenerate v1.0 STLs; commit with tag
- [ ] Create `ModRun-PLA-Production-v1` slicer profile in Bambu Studio
- [ ] Save all 6 production 3MF plate files (12-clip plate per bore size + rail plates)
- [ ] Order 2x eSUN PLA+ 1kg black + 1x white (Amazon Prime)
- [ ] Order 100x 6x4x2" kraft boxes (MrBoxOnline) + 100x poly mailers (Amazon)

### Week 1 (First Production Run)
- [ ] Print 12-clip validation plate (Day 1 morning) — run all three QC gates
- [ ] If Gate 3 passes: print second plate — this is inventory
- [ ] Photograph products: 90-minute shoot per post-test-print-doc-3 brief — do not wait
- [ ] Create Etsy listings in draft mode
- [ ] Set up Pirate Ship: connect Etsy, create package presets, test-print one label
- [ ] Publish listings Thursday-Friday 10AM-2PM
- [ ] Enable Etsy Ads $1/day per listing immediately

### Week 2-4 (Operational Rhythm)
- [ ] Run 2-3 plates/week; log actual timings from daily ops checklist
- [ ] Refine packaging station setup based on actual friction points
- [ ] Set up Craftybase or spreadsheet-based COGS tracking before first order ships
- [ ] Build 10-unit finished-goods buffer before running active promotions
- [ ] Respond to every Etsy message within 24 hours

### Month 2 (Scaling Decisions)
- [ ] Order eSUN 10kg bundle when first 1kg spool is 80% consumed
- [ ] Add 6-clip kit listing to Etsy (if 3-pack is selling consistently)
- [ ] Evaluate Craftybase Studio plan ($20/month) at >40 orders/month
- [ ] Review slicer profile — version bump only if systematic QC issue found
- [ ] Evaluate SimplyPrint FarmLoop if running 3+ plates/week manually

### Month 3-6 (Growth Mode)
- [ ] Second printer decision at sustained >25 units/week for 2 consecutive weeks
- [ ] Part-time post-processor evaluation at >40 units/week (packaging time exceeds 2 hrs/day)
- [ ] Launch secondary product (Desk Headphone Hook) using the same production workflow — new CadQuery file, new slicer profile, new listing
- [ ] Monthly: compare actual COGS to model; adjust pricing tier if filament costs shift more than 10%
- [ ] Month 4: move rails to 2-unit buffer inventory once rail order rate exceeds 5/week

---

## Confidence and Open Items

**High confidence (cross-verified across mfg-farm research corpus):**
- P1S print parameters — verified against manufacturing-automation-architecture.md and scaling-production-research.md
- Breakeven ~135 units/month on corrected COGS model (previously 122 on underestimated packaging)
- Etsy fee structure (6.5% + $0.20 + ~3% payment) from market-research.md
- Filament pricing tiers from supplier-economics.md (eSUN retail $15.90/kg, bulk $11.50/kg, Anycubic pallet $10.49/kg)
- Packaging cost correction: kraft boxes $0.57-0.63/unit at MrBoxOnline, not $0.15 as in v1.1

**Medium confidence:**
- Post-processing time estimates (40 min for 12-unit harvest + brim/stringing/QC) — actual time depends on geometry and support presence. Confirm from first production plate and update the daily ops checklist with actuals.
- Shipping cost blended estimate ($4.50) — this is modeled from zone mix assumptions; actual will vary by customer location. Pirate Ship dashboard will show real cost after 30 days of live orders; update model from actuals.
- AOV mix assumption (60% clip bundles, 25% rails, 15% starter bundles) — entirely speculative until 30 days of Etsy data. Real mix may favor starter bundles heavily if photography emphasizes the system.

**Open items requiring test print data:**
- Exact clips per plate (model assumes 12 per 256x256mm build area; actual layout to be confirmed from first production plate)
- Actual print time per 12-clip plate (estimated 50-65 min; varies with geometry and print settings)
- Whether stringing removal is needed (depends on final design retraction settings; may be zero with well-tuned profile)
- Confirmed FDM_TOLERANCE value (determines production STL parameters; expected 0.12-0.18mm based on test print feedback)

---

*Version 2.0 — Supersedes v1.1 (2026-05-06)*
*Key changes from v1.1:*
*- Printer model corrected throughout: Bambu P1S (not X1 Carbon, which appears in v1.1 automation sections)*
*- Packaging cost corrected: kraft boxes $0.57-0.63/unit (not $0.15); per-unit COGS updated accordingly*
*- Clock-time per-unit step timeline added (Section 1.3)*
*- Week-by-week production schedule added for early phase (Section 7.1)*
*- Rail-specific post-processing detail added (Section 2.5)*
*- AutoFarm3D P1S compatibility caveat added (Section 6.1)*
*- Corrected net margin calculation: 49-55% (not 67% in v1.1 which omitted packaging correction)*
*Next review: Post first-production-run (Week 1 after test print passes)*
*Related: manufacturing-automation-architecture.md, post-test-print-workflow.md, scaling-production-research.md, etsy-shop-launch-kit.md*
