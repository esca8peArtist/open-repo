---
title: 100-Unit Operations Blueprint — ModRun Print Farm
date: 2026-05-05
status: production-ready
tags: [mfg-farm, modrun, operations, print-farm, scaling, labor, facility, queue-management]
confidence: high
related: ../production-scaling-research.md, ../multi-printer-architecture.md, ../workforce-scaling-research.md, ../scaling-production-research.md
---

# 100-Unit Operations Blueprint: Scaling ModRun from 20 to 100+ Units/Week

**Lead finding:** The path from 20 to 100 units/week is not primarily a hardware problem — it is a process discipline problem that hardware eventually solves. A single Bambu P1S running disciplined overnight batches at 12-up plate loading can sustain 50 units/week solo. The jump to 100+ requires a second printer and 10–15 hours/week of contracted labor for packaging; it does not require a dedicated facility until week 24 or later. Under-capitalization kills more small print businesses than under-capacity does. Do not buy hardware ahead of demonstrated demand.

---

## Section 1: Print Farm Architecture (Equipment Decisions)

### 1.1 The Single-vs-Multi-Printer Decision

The decision to add printers should be demand-triggered, not aspiration-triggered. The relevant threshold: when a single printer has run at 80%+ utilization (roughly 13+ hours/day) for two consecutive weeks and backorders are accumulating, add a second printer. Not before.

**What one Prusa-class printer actually handles at 20 units/week:**

Twenty units per week with a 60/40 clip-to-rail revenue mix means approximately 12 clips and 8 rails per week. On a Bambu P1S:

- Clips: 12 clips at 12-up batching = 1 plate run (~50 minutes). One clip plate covers the weekly clip quota.
- Rails: 8 rails at 1 per plate = 8 plate runs (~3 hours each = 24 hours). This is the real constraint — rails are the time hog.
- Total print time at 20 units/week: approximately 26 hours of active printing.

A P1S running 16 hours/day has 112 hours/week available. At 20 units/week you are using roughly 23% of single-printer capacity. This is nowhere near capacity — the constraint at 20 units/week is demand, not hardware.

At 50 units/week (30 clips + 20 rails): ~3 clip plates (2.5 hrs) + ~20 rail plates (60 hrs) = ~62 hours of printing. Still within one printer's 112-hour weekly budget, but approaching the rails ceiling. This is where overnight queuing discipline becomes mandatory.

At 100+ units/week (60 clips + 40 rails): ~5 clip plates (4 hrs) + ~40 rail plates (120 hrs) = ~124 hours. This exceeds a single printer's capacity. A second printer is not optional here.

**Decision rule:** Run demand validation for 6–8 weeks before purchasing additional hardware. If the single printer is not running 14+ hours/day, add a printer is the wrong answer. Improve Etsy SEO, photography, and pricing first.

### 1.2 Equipment Comparison: Which Printer Platform

The three platforms worth evaluating for a production scale-up are the Bambu P1S (the recommended baseline), the Prusa MK4S, and the Creality K1 Max.

| Metric | Bambu P1S | Prusa MK4S | Creality K1 Max |
|---|---|---|---|
| Price (2026) | $699 | $799 | $599–649 |
| Build volume | 256 × 256 × 256mm | 250 × 210 × 220mm | 300 × 300 × 300mm |
| Max print speed | 500mm/s | 500mm/s | 600mm/s |
| Enclosure | Yes (critical for ABS/ASA) | No (open frame) | Yes |
| AMS (multi-spool) | Yes ($299 add-on) | No (native) | No |
| Ecosystem | Closed (Bambu Studio) | Open (PrusaSlicer/OrcaSlicer) | Semi-open (Creality Slicer) |
| Fleet management | Bambu Farm Manager (free) | Prusa Connect (free) | Limited (3rd party needed) |
| Failure detection | AI camera + AMS sensors | Camera only (manual) | Camera only |
| Slicer AMS integration | Native + automatic | Manual profile switching | Manual |
| Nozzle change | 90 seconds (quick-swap) | Tool-required | Tool-required |
| Community parts availability | Moderate (growing) | Excellent | Moderate |
| 1-year reliability rating (community consensus) | High | Very high | Medium-high |

**Recommendation: Standardize on Bambu P1S for the production fleet.** The closed ecosystem is a worthwhile trade for the AMS filament runout switching (prevents overnight failures from killing a 10-hour batch) and Bambu Farm Manager multi-printer coordination. Mixed fleets create slicer profile management overhead that compounds as you add printers. Every printer in your farm should be the same model.

The Creality K1 Max's larger build volume (300 × 300mm) is attractive in theory — you could fit 16–20 clips per plate versus 12–16 on the P1S. In practice, Creality's fleet management tooling is immature relative to Bambu's and the larger bed increases first-layer adhesion failure risk with PLA on a flat large surface. Not recommended for the production fleet.

The Prusa MK4S is an excellent printer for prototyping and individual production but its open frame means no thermal stability at scale, and Prusa Connect's fleet features lag Bambu Farm Manager for multi-printer queue management.

### 1.3 Throughput Modeling by Volume

All estimates use Bambu P1S, 0.20mm layer height, PLA+, 12 clips per plate (50 min/plate), 1 desk_clamp rail per plate (3 hr/plate), 16-hour operational day, 85% utilization (accounts for plate changes and occasional failures). Capital cost reflects street price at time of purchase.

| Weekly target | Clip plates/week | Rail plates/week | Total print hrs/week | Printers needed | Fleet capital cost | Monthly filament cost |
|---|---|---|---|---|---|---|
| 20 units/week | 1 | 8 | 26 hrs | 1 | $699 | ~$55 |
| 50 units/week | 3 | 20 | 66 hrs | 1 (near ceiling) | $699 | ~$130 |
| 100 units/week | 5 | 40 | 130 hrs | 2 | $1,398 | ~$260 |
| 150 units/week | 7–8 | 60 | ~195 hrs | 2–3 | $1,398–$2,097 | ~$380 |
| 200 units/week | 10 | 80 | ~260 hrs | 3 | $2,097 | ~$510 |

Notes:
- 50 units/week on 1 printer is technically achievable but requires consistent overnight queuing (10+ hour overnight runs, 5 nights/week). Any production disruption — a failed plate, a maintenance day — cascades to backorders.
- 100 units/week is the natural 2-printer inflection. Add the second printer when the first runs at capacity for 2 consecutive weeks.
- If product mix shifts toward clips (lower print time per unit), one printer can handle more units; if it shifts toward rails, you hit the ceiling sooner. Rails at 3 hours each are the governing constraint.

**Sensitivity to product mix:** A 100-unit week that is 80% clips and 20% rails requires only ~75 hours of printing — achievable on 1 printer with careful scheduling. A 100-unit week that is 50% rails (50 rails × 3 hrs = 150 hrs) requires 2 printers. Know your actual order mix before committing to capital expenditure.

### 1.4 Facility Requirements

**Phase 1 (1 printer, 20–50 units/week):** A spare bedroom, home office corner, or clean garage bench is entirely adequate. Space requirement: 1.5m × 0.5m bench footprint for the printer + AMS, plus 0.5m of harvest/staging space. Total: approximately 2m² of active workspace. No special permits needed in most municipalities for a single enclosed printer producing PLA parts (see `multi-printer-architecture.md` Section 5.2 on home occupation permits).

**Phase 2 (2–3 printers, 50–150 units/week):** Minimum 8–10m² of dedicated workspace. The layout that works: a continuous 3m bench against one wall for printers, a 0.6m harvest/QC station at one end, and a 1m packing table against an adjacent wall. This fits in a standard one-car garage bay with room for filament storage and outbound staging.

**Phase 3 (3–5 printers, 150–300+ units/week):** 12–18m² dedicated space. At this scale, HVAC matters:
- Cooling: 3–5 Bambu P1S units each drawing 85–100W sustained during printing (peak 350W during initial bed heat-up, then settling to ~85–100W average) adds 255–500W of steady-state heat. A portable 6,000–8,000 BTU AC unit ($200–350) handles this load comfortably and doubles as humidity control.
- Ventilation: P1S enclosed printers with HEPA/activated carbon filters reduce VOC and particle output significantly. Still: maintain minimum 6 air changes per hour in the print room (NIOSH/EPA guidance for multi-printer FDM spaces; 8 ACH is conservative but not required for PLA+ specifically). A 110 CFM bathroom exhaust fan venting to exterior ($60 + short duct run) running during operating hours satisfies the 6 ACH requirement for a 10–12m² room.
- Power: 3 printers on a single 15A circuit is safe for PLA printing (PLA beds at 55°C draw far less than ABS at 100°C). 5 printers require a 20A circuit or split across two 15A circuits. Use dedicated power strips rated for continuous load; no daisy-chaining.
- Storage: Filament on a labeled wall rack; active spools in sealed dry boxes with silica gel. Finished goods in labeled bins. Safety stock of 3 spools per active color is the reorder trigger point (see `material-sourcing-supplier-economics.md`).

---

## Section 2: Queue Management and Batch Optimization

### 2.1 Print Job Orchestration by Volume

The scheduling philosophy is simple: maximize overnight unattended hours (zero marginal labor cost) and use daytime hours for packaging, QA, and shipping. Printers that stop because of poor scheduling are printers you are paying to sit idle.

**20 units/week schedule (1 printer, solo):**

| Day | Morning (7–9am) | Day (9am–5pm) | Evening (5–7pm) | Overnight (10pm–7am) |
|---|---|---|---|---|
| Monday | Harvest overnight clips (if queued Sunday night) | QA + package + ship | Queue overnight rail batch | Print 3 rails (9 hrs) |
| Tuesday | Harvest 3 rails, QA + package | Etsy admin, photography | Queue clip plate | Print 2 clip plates (2 hrs), queue next rails |
| Wednesday | Harvest clips, QA | Pack + ship orders | Queue rails | Print 3 rails |
| Thursday | Harvest rails | Pack + ship | Queue clip plate | Print 1–2 clip plates |
| Friday | Harvest, final QA | Pack + ship; batch label print | Rest | Optional makeup run |

Bottleneck at 20 units/week: none. Print time is low, labor is light. The risk at this scale is inconsistency — skipping QA, delaying shipping, neglecting Etsy SEO. Operations discipline matters more than throughput optimization.

**50 units/week schedule (1 printer, maximum solo load):**

The printer must run near-continuously. Target 14+ hours/day including overnight queuing. Key discipline changes:
- Overnight clip batches become standard (8–10 clip plates queued as a single overnight job = 96–120 clips)
- Rail plates run on a defined afternoon cycle (3-hour windows, 4 plates/day = 4 rails/day)
- Packaging is a daily fixed task, not batched at week's end. Pack and ship every morning from prior day's output.

Bottleneck at 50 units/week: rail print time. Each rail ties up the printer for 3 hours. If you need 20 rails per week, that is 60 hours of printer time for rails alone. With a 16-hour operational day (112 hours/week), 60 hours of rails plus 5 clip plates leaves 47 hours of slack — still manageable solo but with little buffer for failures.

**100+ units/week schedule (2 printers):**

Dedicate one printer to clips (overnight batch mode, 12-up plates, 10-hour overnight = 120+ clips per night) and one printer to rails (daytime operation, 5 rail plates/day = 35 rails/week). This clean separation eliminates scheduling complexity: you never need to interrupt a rail job to make room for a clip batch or vice versa. Each printer has one job type, one plate config, one profile. Simplicity is the operating principle.

Bottleneck at 100 units/week with 2 printers: packaging and QA labor. At 100 units/week (roughly 15 orders/day at average order size), packing takes 1.5–2 hours/day. This is the point where contracted packaging help — 10 hours/week at $15/hour — makes economic sense.

### 2.2 Batch Sizing Strategy

Larger batches reduce per-unit setup cost (plate prep, job dispatch) but increase in-progress inventory. The tradeoff:

| Batch size | Setup cost/unit | In-progress inventory | Risk if failure | Recommendation |
|---|---|---|---|---|
| 1 unit | ~8 min (full plate turnaround) | Negligible | Low | Test prints only |
| 12 clips (1 plate) | ~5 min (plate prep + dispatch) | 3–4g PLA, $0.04 material | 1 plate lost | Standard production |
| 48 clips (4-plate queue) | ~1.5 min amortized | ~12–15g material | 1 plate lost | Good for daily batching |
| 120 clips (10-plate overnight) | ~0.5 min amortized | ~36–45g material | 1 plate from overnight | Recommended when demand justified |
| 200+ clips (multi-session) | Near-zero setup/unit | ~60–80g material | 1 plate per failure | Only at 100+/week when demand proven |

Working capital tied up in in-progress inventory is trivial for clips ($0.04 COGS/clip) and modest for rails ($2.02 COGS/rail). The real working capital risk at small scale is not inventory — it is equipment (printers) purchased before demand is proven. Keep batch sizes at the maximum the printer can manage overnight; the WIP carrying cost is negligible.

### 2.3 Print Failure Tolerance Budget

Failures at scale are a percentage game. Target: 3–5% scrap rate at mature production (PLA+, well-tuned P1S profile). What that means by volume:

| Weekly volume | Scrap rate | Failed units/week | COGS lost/week (clips) | COGS lost/week (rails) |
|---|---|---|---|---|
| 20 units/week | 5% | 1 unit | ~$0.10 | ~$2.02 |
| 50 units/week | 5% | 2–3 units | ~$0.25 | ~$5.05 |
| 100 units/week | 5% | 5 units | ~$0.50 | ~$10.10 |
| 100 units/week | 10% (early production) | 10 units | ~$1.00 | ~$20.20 |

Financial scrap cost is genuinely low. The operational risk is throughput: a 10% scrap rate on a 12-clip plate means 1–2 failed clips per plate — manageable. A full plate loss (bed adhesion failure, filament clog) eliminates 12 clips or 1 rail — a 50-minute or 3-hour setback. At 100 units/week with 2 printers, losing one plate per day to failure means you are operating at roughly 90% of target throughput. Design for this: your weekly schedule should have 10–15% schedule slack built in (roughly 1–2 hours/day of unallocated capacity per printer) to absorb the expected failure rate without affecting shipping commitments.

**First-pass success rate target:** 95%+ at mature production. The three failure modes most likely to reduce this below target are: bed adhesion loss (clean PEI before every plate), snap arm layer delamination (nozzle temp 222°C, minimum layer time 8 seconds), and filament runout mid-job (AMS multi-spool switching, maintain 500g+ on active spools). All three are preventable with process discipline.

### 2.4 Print Queue Software Stack

The software decision is not about features — it is about what is free, reliable, and appropriate to your scale.

| Stage | Volume | Recommended stack | Cost | Setup time |
|---|---|---|---|---|
| Launch | 1 printer | Bambu Studio + Bambu app | Free | 30 min |
| Growth | 2 printers | Bambu Farm Manager + Printago free tier | Free | 2–3 hrs |
| Scale | 3–5 printers | Bambu Farm Manager + Printago paid tier | ~$20–40/month | 4–6 hrs |
| Advanced | 5+ printers | Printago paid + Filametrics (beta 2026) | ~$40–80/month | 8–12 hrs |

**Bambu Farm Manager** (free, local network) handles multi-printer queue dispatch, staggered startup (prevents power spikes from simultaneous bed heating), batch job assignment, and print status monitoring. This is the primary control surface for a 2–5 printer fleet. Set it up before the second printer arrives so the workflow is established before you need it.

**Printago free tier** (free, cloud) adds material-aware routing — it will not dispatch a clip profile to a printer loaded with the wrong filament color. This eliminates a common failure mode at multi-printer scale: starting a job on the wrong machine. At one concurrent job (free tier limit), it complements Farm Manager for the routing intelligence that Farm Manager lacks.

**Avoid:** OctoPrint/OctoFarm for Bambu printers. The unofficial Bambu OctoPrint plugin is functional but incomplete and is not supported by Bambu Lab. Adding unsupported plugins to production machines is a reliability risk.

---

## Section 3: Post-Processing and Automation

### 3.1 Support Removal

ModRun clips and rails are explicitly designed for support-free printing in their default orientations. This is a deliberate design choice that eliminates the largest post-processing time sink in FDM production.

Zero support removal is a meaningful competitive advantage versus operations running designs that require it. Manual support removal on a complex FDM part takes 3–8 minutes per unit; at $15/hour labor that is $0.75–$2.00/unit. At 100 units/week, that is $75–$200/week in labor that ModRun's support-free design eliminates entirely.

If a future product variant requires supports, evaluate whether the design can be modified (orientation change, split-print-then-assemble) before accepting ongoing support removal costs.

### 3.2 Cleaning and QA Protocol

**At 20 units/week (visual inspection + functional test):**

Per-unit QA takes 5–10 seconds for clips, 30–40 seconds for rails. Full weekly QA at 20 units/week: approximately 8–12 minutes. This should happen at harvest, not at packing time — catching failures at harvest prevents them from entering the finished goods bin.

The four checkpoints (detailed in `production-scaling-research.md` Section 1.7):
1. Visual: snap arm present, no stringing across cable bore, first layer adhered
2. Dimensional spot check (1 per 20 units): snap arm width and clip slot entry with calipers
3. Functional (1 per plate batch): clip seats in rail with tactile click; cable seats without falling out
4. Stress test (1 per new filament batch): 5 insertion cycles without snap arm deformation

Tools needed at launch: digital calipers ($15–25), a go/no-go test rail section (print one from the production rail STL), a sample cable at each bore diameter being sold. Total QA tooling cost: under $30.

**At 100+ units/week (dimensional sampling + go/no-go jig):**

At 100 units/week, full manual functional testing of every unit is not practical. Shift to statistical sampling: functional test 1 unit per plate batch (every 12 clips or 1 rail), visual inspect 100% at harvest, and dimensional caliper check 5% of units (5 per 100 produced). This protocol takes approximately 3 minutes per plate batch for clips and 2 minutes for rails — about 25–30 minutes per 100 units produced.

**Camera-based automated inspection** becomes cost-effective at 200+ units/week. A Raspberry Pi with a camera module and OpenCV running a basic dimensional check script can verify snap arm presence, bore gap openness, and general part completeness in under 2 seconds per part. Build cost: $60–120 for the hardware; 8–16 hours of Python scripting. This eliminates the human visual inspection step, which is the largest QA labor component at scale. Implement when optical inspection labor exceeds $200/month — roughly at 250+ units/week.

**Commercial optical inspection** (structured-light scanners, CMM systems) is not appropriate for this product at any expected volume. The break-even on a $5,000+ inspection system would require volumes above 500 units/week of high-margin product. Go/no-go gauges and statistical sampling at 5% are the correct approach up to 1,000+ units/week.

### 3.3 Finishing Alternatives (If Required)

ModRun's PLA+ parts should not require finishing for launch. If a premium surface finish SKU becomes warranted:

**Vibratory tumbling ($80–$500):** A Harbor Freight entry-level vibratory tumbler ($80 when on sale) with small plastic media runs 50–200 clips in 2–4 hours unattended, removing minor burrs and improving surface texture. ROI trigger: only worthwhile if selling a premium-finish SKU at $3–5 above standard. Not recommended at launch.

**Chemical smoothing (acetone vapor for ABS/ASA only):** Not applicable to PLA+. ABS smoothing in acetone vapor creates a near-injection-molded surface but requires switching from PLA to ABS, introducing a harder-to-print material with different COGS. Not recommended unless the product moves to ABS/ASA for other reasons (heat resistance, outdoor use).

**XTC-3D epoxy coating:** Adds 8–12 minutes per part and $0.30–$0.50 material cost. Creates an injection-molded appearance. Only appropriate as a defined premium SKU at a $5–8 price premium.

**Practical recommendation for post-processing timeline:**

| Volume | Post-processing approach | Time per unit | Labor cost/unit |
|---|---|---|---|
| 20 units/week | Harvest + visual inspect + deburr rail slots | 5–40 sec | $0.02–$0.17 |
| 50 units/week | Same | 5–40 sec | $0.02–$0.17 |
| 100+ units/week | Same + statistical sampling | 3–5 sec clips, 30 sec rails | ~$0.02–$0.13 |

Post-processing is not the bottleneck. Packaging and shipping logistics are.

### 3.4 Packaging and Time-to-Ready Model

The true time-per-unit-ready metric includes print time, post-processing, packaging, and labeling. Here is the model:

| Stage | Time per clip | Time per rail | Notes |
|---|---|---|---|
| Print (effective/unit at 12-up batching) | 4–5 min | 180 min | Rails are the slow component |
| Post-processing (harvest + QA) | 8–10 sec | 40–50 sec | Support-free design keeps this minimal |
| Packaging (poly mailer + bag + label) | 90–120 sec | 120–150 sec | Includes label application |
| Batch shipping upload (amortized at 15 orders/day) | ~10 sec | ~10 sec | Pirate Ship batch = 5 min for 30 orders |
| **Total time-to-ready per unit** | **~6–7 min** | **~185 min** | Print dominates for rails |

Packaging becomes the proportional bottleneck as volume grows, not print time. At 100 units/week (roughly 15 orders/day), packaging consumes 30–40 minutes/day. This is manageable solo but the first task to delegate when contractor help is hired.

---

## Section 4: Labor Economics

### 4.1 Per-Unit Labor Cost by Scale

All estimates use $15/hour for packaging/post-processing labor and $0/hour for owner's operational labor (opportunity cost, not direct cost).

| Volume | Weekly labor hours | Weekly labor cost | Labor cost/unit | Who does it |
|---|---|---|---|---|
| 20 units/week | ~4 hrs (printing setup + pack + ship + admin) | $0 direct (owner) | $0 direct | Solo owner |
| 50 units/week | ~10 hrs total | $0 direct (owner) | $0 direct | Solo owner (stretched but viable) |
| 100 units/week | ~18 hrs total | ~$0 direct + $150/week contractor (10 hrs packaging) | ~$1.50 direct | Owner + part-time contractor |
| 150 units/week | ~25 hrs total | ~$225/week contractor (15 hrs) | ~$1.50 direct | Owner + part-time contractor |
| 200 units/week | ~35 hrs total | ~$300–$400/week (20–25 hrs contractor) | ~$1.50–$2.00 direct | Owner + regular part-time |

**Key observation:** Per-unit direct labor cost stays relatively flat at $1.50–$2.00 across the 100–200 unit range because packaging labor scales linearly with orders, not superlinearly. The efficiency gains come from batching (printing 10 plates overnight versus 1 plate at a time) rather than labor productivity improvements. The labor complexity at 150+ units/week is not cost per unit — it is coordination: scheduling a consistent contractor, maintaining QA standards without direct supervision, and handling the occasional contractor availability gap.

**Owner time freed by contractor packaging help (100 units/week):**
- Before contractor: ~5–6 hours/week on packaging + labeling
- After contractor (10 hrs/week): ~1 hour/week for QA spot-checks and outbound staging
- Owner time recovered: ~4–5 hours/week for product development, Etsy SEO, photography, or new SKU research

At $3,000–5,000/month net revenue at 100 units/week, those 4–5 recovered hours per week are worth more applied to growth work than packaging clips.

### 4.2 Hiring Timeline and ROI Breakpoints

**Do not hire before the numbers justify it.** The sequence:

1. **Month 0–2:** Solo. 20 units/week. No contractor needed. Owner handles all tasks in 3–4 hours/day.

2. **Month 3–4:** Still solo or light 1099 contractor (4–6 hrs/week) for packaging overflow when orders spike. Contractor sourced from local maker space or Nextdoor. Written 1099 agreement with NDA required before any business details are shared. Cost: ~$240–$360/month.

3. **Month 5–6:** 50 units/week. If operations consume 5+ hours/day, formalize a regular contractor (8–10 hrs/week). Revenue at this stage: $5,000–$8,000/month. Contractor packaging cost: $480–$600/month = 6–12% of revenue. Justified.

4. **Month 6+:** 100+ units/week. Regular contractor at 10–15 hrs/week is the right structure. Formal W-2 hire is not yet justified — the IRS 1099 classification test becomes risky when a contractor works more than 15–20 hours/week on a fixed schedule at your facility doing core repetitive functions. Stay below this threshold or transition to W-2. Full-time W-2 hire becomes viable when revenue exceeds $8,000–$10,000/month consistently and contractor hours are at the reclassification boundary.

**Revenue breakpoint for part-time W-2 employee:**
- Part-time W-2 at 20 hrs/week, $15/hour base: $300/week
- Total employer cost at 1.3x burden rate: $390/week = ~$1,680/month
- Required monthly revenue to keep labor at 20% of revenue: $8,400/month
- Achievable at: roughly 80–100 units/week with good ASP (average sale price)

**Revenue breakpoint for full-time employee:**
- Full-time W-2 at 40 hrs/week, $15/hour base: $600/week
- Total cost: $780/week = ~$3,380/month
- Required revenue at 20% labor ratio: $16,900/month
- Achievable at: roughly 200+ units/week — well beyond the 100-unit scope of this blueprint

### 4.3 Training Cost

Part-time contractor or production assistant training for clip/rail operations:
- Print harvest + restart protocol: 30 minutes
- Visual QC checklist: 45 minutes (laminated checklist + pass/fail photo reference)
- Packaging procedure: 45 minutes
- Shipping software (Pirate Ship): 30 minutes
- **Total initial training: 2.5–3 hours** at $15/hour = $37.50–$45.00 one-time cost

The QC checklist is the critical document. Before any contractor starts, produce a laminated one-page reference with:
- Three pass examples (good snap arm, clean bore opening, aligned slot entry)
- Three fail examples (deformed snap arm, stringing across bore, underfused layers)
- The functional test (press clip into test rail: expect click, not rattle or binding)

A contractor reaching independent QC operation within one training session is achievable with this document. Spot-check 10% of contractor-inspected units for the first four weeks; reduce to 5% once defect pass-through rate stays below 0.5%.

---

## Section 5: Facility Scalability Roadmap

### 5.1 Phase-by-Phase Facility Requirements

**Month 1–2: Test print + 20 units/week (home/small workshop, single printer)**

Minimum viable setup: 2m² bench space, standard 15A outlet, basic ventilation (room with openable window or small exhaust fan). PLA+ prints are low-risk at this scale. No facility upgrade needed. Total capital: printer + filament + basic packaging = $800–$950.

**Month 3–4: Scaling to 50 units/week (near-full single-printer utilization)**

If operating from home, the only facility change is ensuring consistent 24/7 operation won't disturb household members (printer noise, overnight running). The P1S at production speeds produces approximately 45–50 dB — quieter than a refrigerator at distance. An attached garage or dedicated workshop room is ideal. No facility capital needed.

**Month 5–6: 100+ units/week (second printer, dedicated workspace)**

With two printers, designate a proper workspace. A one-car garage bay (nominally 14m²) is the ideal entry point: enough space for 2 printers + staging + packing table, already zoned for light workshop use in most municipalities, and easy to ventilate. Facility cost: $0 (use existing garage) or $300–$500/month for a shared studio/makerspace rental if home space is unavailable.

**Year 2: Multi-product portfolio, 500+ units/week**

At 500+ units/week across 4–5 products, dedicated commercial space becomes practical. A 500–750 sq ft commercial unit in a light industrial zone ($1,000–$2,500/month depending on market) accommodates 8–10 printers, a dedicated packing station, and bulk filament storage. This triggers the full employer compliance stack (business insurance, occupancy permit, potentially a home occupation exit). Staff at this scale: 1 full-time production/operations person at $16–20/hour, plus owner split between production oversight and business development.

Revenue at 500 units/week: approximately $25,000–$40,000/month gross (blended clip/rail mix at current pricing). Net after all costs at this scale: $10,000–$18,000/month. This is the Year 2 target for an aggressively executed operation.

### 5.2 Year 2 Multi-Product Vision

The multi-product portfolio strategy (clips, rails, headphone hooks, bin labels, plant markers) at 100+ units/week each represents the Year 2 upside. Key operational implications:

- Each new product requires its own production profile, plate configuration, and QA checklist — roughly 4–8 hours of setup work per SKU.
- Filament inventory management becomes more complex (5+ active SKUs may require 3–5 colors each = 15+ active spools). Implement Printago's material tracking at this stage.
- The 5-product farm at 100 units/week each = 500 units/week total requires approximately 8–10 printers at current throughput rates — a $5,600–$7,000 fleet investment phased over 18–24 months as demand is validated product by product.

**The critical discipline for multi-product scaling:** Validate each new product to 20 units/week of sustained demand before expanding its production. Never add hardware for a product that has not proven market fit. The operational pattern is identical to the single-product path: prototype → test print → 20 units/week → validate demand → scale to 50 → 100.

---

## Section 6: Fulfillment Scaling — 3PL vs. In-House

### 6.1 The Decision Framework

The 3PL decision is fundamentally about time arbitrage. A 3PL costs more per order than in-house fulfillment but returns 30–40 minutes of daily labor that can go toward growth work (Etsy SEO, product design, photography). The break-even question is: is your time worth more than the per-order cost delta?

At 100 units/week (~430 orders/month), the calculation is straightforward:

| Fulfillment model | Cost structure | All-in cost/order | Monthly cost |
|---|---|---|---|
| In-house (Pirate Ship + Etsy labels) | Shipping + $0.30/order packaging materials | ~$4.80 | ~$2,064 |
| ShipMonk | $2.50 pick + $0.50/add item + storage + shipping | ~$8.50–$11.00 | ~$3,655–$4,730 |
| Simpl Fulfillment | ~$7/order flat (pick, pack, ship, materials) | ~$7.00 | ~$3,010 |
| ShipBob | $0.30/pick + 15–30% shipping markup + $275 min | ~$9–$13 | ~$3,870–$5,590 |

Notes: Shipping costs (~$4.50/order) are included in all figures for comparability. ShipMonk has a $250/month minimum; at 430 orders/month this is not the binding constraint. ShipBob requires a $975 setup fee and a 400-order/month minimum — feasible at 100 units/week but the setup cost needs amortization.

**Cost gap:** At 430 orders/month, in-house costs approximately $1,600–$2,700 less per month than any 3PL option. This is the price of 3PL convenience.

**When 3PL makes sense anyway:**
- You have proven demand at 100+ units/week and want to decouple fulfillment from your schedule (evenings/weekends back)
- You are adding Amazon FBA simultaneously — running both Etsy in-house and Amazon FBA is manageable; running Etsy in-house plus a second 3PL is not
- You are traveling or working a demanding day job that makes consistent daily shipping impossible

**When in-house is clearly better:**
- Sub-100 units/week: the $250/month 3PL minimums represent 25–50% of your net profit
- Product requires custom packaging or fit notes (3PLs charge $0.25–$1.00/order for custom inserts)
- Order mix is variable (some weeks 20 units, some weeks 80) — 3PLs charge storage on unsold inventory even during slow weeks

### 6.2 In-House Fulfillment at 100 Units/Week

The efficient in-house workflow at 100 units/week (roughly 15 orders/day):

**Morning packaging window (30–40 minutes/day):**
1. Pull previous day's finished goods from bins
2. Match to open orders (Etsy + Amazon dashboards open simultaneously)
3. Pack: poly mailers for clip bundles, small corrugated boxes for rails
4. Apply shipping label (printed in batch from Pirate Ship or ShipStation)
5. Stack by carrier for dropoff or scheduled USPS pickup

**Shipping label workflow at 100 orders/week:**

Pirate Ship has a native Etsy integration (affected by Etsy's October 2024 API changes but still functional for order import). At 15 orders/day, manually importing from CSV takes 2–3 minutes. Pirate Ship batch mode prints 15+ labels in one session at no extra cost.

ShipStation ($9.99–$29.99/month) offers automatic Etsy order sync and automation rules (auto-select service tier by order weight). At 100 orders/week, ShipStation's $9.99/month Starter plan (up to 50 shipments/month) is insufficient; the $29.99/month Growth plan (up to 500 shipments/month) is the right tier. The $30/month cost is recovered in roughly 30 minutes of saved manual data entry monthly — worth it above 75 orders/week.

**Packaging materials cost at 100 units/week:**
- Poly mailers 6×9" (clips): $0.09–$0.12 each in bulk (500-count cases)
- Small corrugated mailers 6×4×4" (rails): $0.35–$0.55 each
- Fragile/padding void fill (rails): $0.05–$0.10
- Thank-you card inserts: $0.05 each if used
- Blended materials cost at 70/30 clip-rail mix: ~$0.18–$0.25/order

### 6.3 3PL Evaluation Shortlist

For when 3PL becomes viable (Month 8–12 at aggressive growth):

**Simpl Fulfillment** — Best fit for this operation. Flat ~$7/order including pick, pack, ship, and materials. No setup fee, no monthly minimum, free receiving for inbound shipments created in their software. Etsy and Shopify integrations. Ideal for the 300–1,000 orders/month range. Con: fewer warehouse locations than ShipBob (affects West Coast delivery speed).

**ShipMonk** — $2.50 pick fee + $0.50/additional item, no setup fee, free inbound receiving. Storage: $1–$4/bin/month. $250/month minimum. Better for operations with multiple SKUs or variable order sizes. Has Etsy integration. At 430 orders/month of single-item clip bundles, cost structure: ~$2.50/order pick + $0.50 packaging + $4.50 shipping = ~$7.50/order before storage.

**Amazon FBA** — Not a true 3PL but the most cost-effective fulfillment option for the Amazon channel specifically. FBA fees for a 3-oz poly mailer: ~$3.50–$4.50/unit (size tier: small standard). FBA eliminates per-order packing labor for Amazon orders but adds complexity (inventory prep, FBA labeling, inbound shipment creation). Best adoption timing: once Etsy is reliably producing 50+ units/week and Amazon Handmade is a secondary channel.

### 6.4 Returns and Restock Protocol

At 100 units/week, expect 2–5 returns/month (2–5% return rate is typical for Etsy physical goods). The protocol:

1. Inspect returned unit against QA checklist: does the snap arm function? Is the bore diameter correct?
2. Pass: restock to finished goods bin (no reprint needed)
3. Fail (customer-caused deformation or missing component): photograph for records, scrap or photo archive
4. Refund: issue via Etsy within 48 hours of receipt. Do not wait to inspect before refunding — Etsy's review system penalizes slow refunds more than the occasional return fraud.
5. Pattern tracking: log all returns with reason code. Three returns with the same reason code = a design or QA protocol issue, not random noise.

---

## Appendix: Key Operating Metrics to Track from Day One

| Metric | Target | Measurement frequency |
|---|---|---|
| Printer utilization (hrs/day active) | 10+ at 20/wk; 14+ at 50/wk; 16+ at 100/wk | Daily (logged in production spreadsheet) |
| Scrap rate (% of units failing QA) | < 5% mature; < 10% first 2 weeks | Per plate batch |
| First-pass success rate | > 95% | Per plate batch |
| Post-processing time per unit | < 10 sec clips; < 50 sec rails | Weekly spot-check |
| Orders shipped on time (per Etsy SLA) | > 98% | Weekly |
| Filament stock days on hand | 14–21 days per active color | Weekly |
| Contractor QA defect pass-through | < 0.5% | Weekly spot-check of contractor work |

---

## Sources

- Prior ModRun production research: `../production-scaling-research.md`, `../multi-printer-architecture.md`, `../workforce-scaling-research.md`, `../scaling-production-research.md`
- [Bambu Lab P1S Specifications](https://us.store.bambulab.com/products/p1s)
- [Bambu Lab Power Consumption — Wiki](https://wiki.bambulab.com/en/general/power-consumption)
- [Bambu Farm Manager Quick Start Guide](https://wiki.bambulab.com/en/software/bambu-farm-manager)
- [Bambu Farm Manager: Local Fleet Control](https://blog.bambulab.com/bambu-lab-introduces-local-fleet-control-with-bambu-farm-manager/)
- [Printago: Commerce OS for 3D Print Farms](https://printago.io/)
- [Printago Complete Bambu Lab Print Farm Guide 2026](https://printago.io/blog/bambu-lab-print-farm-guide-2026)
- [Printago + Filametrics Unified Platform Announcement](https://3dprintingindustry.com/news/printago-and-filametrics-announce-unified-platform-for-automated-3d-print-farms-246775/)
- [3DCentral: How to Start and Scale a 3D Print Farm Business](https://3dcentral.ca/how-to-start-and-scale-a-3d-print-farm-business-the-complete-guide/)
- [ADP Industries: Best 3D Printer 2026 — 6-Printer Farm Operator Review](https://www.adpindustries.com/blog/best-3d-printer-2026/)
- [Bambu Lab vs Creality vs Prusa: Definitive 2026 Comparison — ADP Industries](https://adpindustries.com/blog/bambu-lab-vs-creality-vs-prusa-2026/)
- [Prusa Pro: How to Build a 3D Printing Farm](https://pro.prusa3d.com/insights/guides/how-to-build-a-3d-printing-farm)
- [ShipMonk Transparent Fulfillment Pricing](https://www.shipmonk.com/pricing)
- [ShipBob Pricing Breakdown — Simpl Fulfillment Analysis](https://www.simplfulfillment.com/breakdowns/shipbob-pricing)
- [Simpl Fulfillment vs ShipBob Comparison](https://www.simplfulfillment.com/support-center/simpl-fulfillment-vs-shipbob-comparison)
- [Pirate Ship Etsy Integration](https://www.pirateship.com/integrations/etsy)
- [Etsy API Changes October 2024 — Third-Party Shipping Impact](https://github.com/etsy/open-api/discussions/1303)
- [ShipStation vs Pirate Ship — Veeqo Comparison](https://www.veeqo.com/blog/shipstation-vs-pirateship-comparison)
- [SBA: How Much Does an Employee Cost You](https://www.sba.gov/blog/how-much-does-employee-cost-you)
- [NIOSH: Approaches to Safe 3D Printing — 2024 Guide for Small Businesses](https://www.cdc.gov/niosh/docs/2024-103/pdfs/2024-103.pdf)
- [3D Printer Ventilation Requirements — 3DPrintscape](https://3dprintscape.com/how-much-ventilation-does-a-3d-printer-need/)
