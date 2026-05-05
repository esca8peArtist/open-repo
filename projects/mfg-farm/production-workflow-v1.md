---
title: ModRun Production Workflow v1 — Post-Test-Print Execution Guide
date: 2026-05-05
status: active
version: 1.0
scope: Post-test-print production workflow, scaling roadmap, QC protocol, supplier transition, Month 1 launch
related: production-scaling-research.md, phase-2-supplier-research.md, post-test-print-doc-2-etsy-listing-design-templates.md, post-test-print-doc-3-lifestyle-photography-brief.md, cost-model-spreadsheet.csv
---

# ModRun Production Workflow v1

**Lead finding:** The test print is the gate. Once it passes, every subsequent action in Month 1 is already designed — STLs lock, the slicer profile locks, the Etsy listing goes live, and the printer runs nights. The bottleneck at 1–20 units/week is never the printer; it is plate discipline and QC consistency. A single Bambu P1S running 12-clip plates on a Sunday-through-Friday overnight schedule produces 20+ saleable units per week with under 6 active hours of operator time. This document covers what happens the moment the test print is evaluated through the end of Month 3.

---

## Section 1: Post-Test-Print Workflow

### 1.1 Evaluate the Test Print (30 Minutes)

Run through this checklist the moment the test print is in hand. This evaluation dictates all subsequent steps.

**Snap arm function:**
- Deflect the snap arm manually to approximately 50% of full travel. It should flex without cracking, return to position without permanent set, and produce a light tactile resistance. If the arm snaps: nozzle temp is too low or minimum layer time is too short — both are slicer fixes, not design fixes.
- Insert a test cable of the target bore diameter. The cable should seat with a definite click, resist gentle pulling, and release cleanly when the arm is pressed. If it rattles: increase FDM_TOLERANCE in CadQuery from 0.15mm to 0.20mm. If it binds and requires force: decrease FDM_TOLERANCE to 0.10mm.

**Rail slot fit:**
- Press a clip into the rail slot. The clip should engage with a click and slide along the slot without binding. Rail-to-clip tolerance uses the same FDM_TOLERANCE parameter — one adjustment fixes both interfaces simultaneously.

**Dimensional verification:**
- Snap arm width: measure with digital calipers at the narrowest point of the arm. Design value: 7.6mm. Acceptable range: 7.3–7.9mm. Outside this range, check for over-extrusion (arm too wide) or under-extrusion (arm too narrow).
- Cable bore opening: measure the gap width at the open face of the clip. Design basis: BORE_GAP_RATIO of 0.65 of bore diameter. Verify the gap is not fused shut by stringing.
- Clamp arm thickness (rail): measure with calipers at the mid-span. Design value: 4mm. Acceptable range: 3.8–4.2mm.

**Decision tree:**
- All checks pass: proceed to 1.2 (STL lock) immediately.
- FDM_TOLERANCE adjustment only: adjust in CadQuery, regenerate STL, re-slice, print a single validation clip (not a full plate), re-run functional test. If it passes, lock as v1.0.
- Structural failure (snap arm cracking): adjust slicer parameters (increase nozzle temp to 225°C, set minimum layer time to 10 seconds, verify wall count is 4), reprint, re-evaluate. This is a slicer fix, not a design change.
- Both tolerance and structural issues: fix structural first (slicer), then tolerance (CadQuery). Do not attempt both simultaneously — you need to isolate which variable resolved each issue.

### 1.2 STL Generation and Version Locking

Once functional test passes, lock the production STLs before running any production batch.

**CadQuery regeneration command (from repo root):**
```bash
uv run python cadquery/modrun_clip.py --export stl/v1.0/modrun_clip_6mm_v1.0.stl
uv run python cadquery/modrun_rail.py --export stl/v1.0/modrun_rail_deskclamp_v1.0.stl
```

Generate all bore-diameter variants you plan to sell at launch (6mm, 8mm, 12mm are the primary three). Each variant becomes a separate production STL file.

**Directory structure to establish immediately:**

```
/modrun-production/
  /cadquery/            — .py source files (git-tracked with version tags)
  /stl/
    /v1.0/              — First validated production STLs (never overwritten)
    /v1.1/              — Any tolerance-adjusted variants after production issues
    /test-prints/       — Experimental variants; never mixed with production files
  /sliced/
    /production/        — Active .3mf files per plate configuration
    /archive/           — Superseded plate configs (keep for reference)
  /qc-log/              — CSV quality logs by week
```

**File naming convention:** `modrun_clip_6mm_v1.0_12up_0.20mm_20pct.3mf` encodes product, bore size, version, units-per-plate, layer height, and infill percentage. This eliminates ambiguity about which file produced which batch.

**Version discipline:** Never overwrite v1.0. If a tolerance adjustment is needed post-production, create v1.1 and validate it before switching over. The CadQuery source makes regeneration trivial — changing FDM_TOLERANCE and re-running takes under 60 seconds.

### 1.3 Slicing — Production Profile

Save the following settings as `ModRun-PLA-Production-v1` in Bambu Studio. This profile is frozen for all production runs. Do not adjust it experimentally without creating a named copy first.

| Parameter | Value | Rationale |
|---|---|---|
| Layer height | 0.20mm | 0.15mm adds 25–30% print time with no functional benefit for cable clips |
| Wall count | 4 | 3 is the minimum; 4 adds insurance at rail clamp corners and snap arm root |
| Infill density | 20% | Below 20%, snap arm brittleness risk increases; above 25%, time adds without strength gain |
| Infill pattern | Gyroid | Isotropic load distribution; the snap arm deflects in two axes — gyroid handles this best |
| Outer wall speed | 150–200mm/s | P1S can achieve 200mm/s on PLA+ without dimensional loss |
| Infill speed | 300–500mm/s | Negligible effect on part quality; let the printer run fast here |
| Minimum layer time | 8 seconds | Prevents successive nozzle passes from depositing on still-soft plastic at snap arm |
| Nozzle temperature | 222°C | Slightly above eSUN/Overture PLA+ nominal; improves interlayer adhesion at thin sections |
| Bed temperature | 55°C | Standard for PLA+ on PEI; no glue required on clean PEI |
| Supports | None | Both clip and rail are designed support-free in default orientation |
| Z-seam position | Back | Places the seam at the rear face, away from the snap arm — prevents seam-line weakness at snap |
| Bed adhesion | PEI plate, IPA wipe | Clean plate with isopropyl before every plate run; neglect this and you get first-layer failures |

**Critical setting:** The minimum layer time of 8 seconds is not optional. On a 12-clip plate, the snap arm section is very thin — the nozzle cycles back to each arm tip in roughly 3–5 seconds at full speed. Without the minimum layer time enforced, you deposit hot PLA onto PLA that has not yet solidified, producing a distorted arm. The Bambu P1S will handle this automatically if the minimum layer time is set correctly in the profile.

### 1.4 Plate Configuration and Print Time

**Standard production plates:**
- Clips: 12 per plate in a 4×3 grid, 8mm spacing minimum. Never print fewer than 8 per plate in production. Single-unit print runs waste printer capacity.
- Rails (desk_clamp): 1 per plate. Can add 4–6 clips alongside a single rail to maximize utilization on a mixed plate.
- Rails (adhesive variant): 2 per plate. Lower Z-height allows two per run.

**Print time estimates (Bambu P1S, 0.4mm nozzle, PLA+, Quality preset):**

| Product | Plate config | Print time | Effective time per unit |
|---|---|---|---|
| Clip, 6mm bore | 12-up plate | 40–50 min | 3.5–4.5 min |
| Clip, 12mm bore | 12-up plate | 50–65 min | 4.5–5.5 min |
| Rail, desk_clamp | 1 per plate | 2.5–3.5 hr | 2.5–3.5 hr |
| Rail, adhesive | 2 per plate | 1.5–2.5 hr | 45–75 min per rail |
| Mixed (1 rail + 4 clips) | 1 plate | 2.5–3.5 hr | Rail + bonus clips |

**Print monitoring:** Monitor the first 3 minutes of every plate for bed adhesion confirmation. After that, the P1S AI failure detection handles the rest for unattended runs — verify this feature is enabled in the machine settings before leaving a printer unattended overnight.

**Plate turnaround:** Allow 4–6 minutes between plate completions (plate cooling to ~40°C for flex-release, IPA wipe, re-load). On a 16-hour production day, this dead time totals approximately 60–90 minutes across 10–12 print cycles. Factor this into weekly capacity math.

### 1.5 Post-Processing Steps

ModRun parts are support-free by design. Post-processing is minimal and can be performed entirely at the printer station.

**Clips:**
1. Wait for PEI plate to cool to ~40°C (2–3 minutes after print completes).
2. Flex the PEI plate gently; clips release cleanly without tools.
3. Pop each clip free, inspect visually (Gate 1, below), place in pass bin or fail bin.
4. Harvest time per 12-clip plate: under 60 seconds at steady-state operation.

**Rails (desk_clamp):**
1. Allow plate to cool fully before removal (rail's larger footprint retains heat longer — wait 4–5 minutes).
2. Remove rail from plate; the slot openings may have minor stringing at the entry points.
3. Pass a deburring tool or craft knife tip along each slot entry: 10–15 seconds per rail.
4. Run fingernail across the underside of the clamp jaw to confirm no layer separation.
5. Inspect clamp arm for any Z-seam cracking at the arm-to-body junction.
6. Total post-processing per rail: 40–50 seconds.

**Rails (adhesive variant):**
1. Remove from plate after cooling.
2. Press fingernail across each adhesive pocket floor to verify the pocket base is complete (no missing layers from under-extrusion). This is the highest-risk inspection point for the adhesive variant.
3. Total post-processing: 25–35 seconds.

**What not to do:** Do not sand, prime, or coat parts for launch. Surface finish from the P1S at 0.20mm layer height is clean and functional. Any finishing that adds more than 30 seconds per part is not justified by launch pricing — revisit only if a premium SKU is introduced.

### 1.6 Tolerance Verification Protocol

After the first production batch and periodically thereafter, verify that dimensional accuracy is holding.

**Measurement points (calipers required — $15–25 for adequate accuracy):**

| Measurement | Design value | Acceptable range | Frequency |
|---|---|---|---|
| Snap arm width | 7.6mm | 7.3–7.9mm | 1 per 20 units |
| Clip slot entry width | Bore + 2× FDM_TOLERANCE | ±0.3mm | 1 per 20 units |
| Rail slot width | Per design | ±0.3mm | 1 per 10 rails |
| Clamp arm thickness | 4mm | 3.8–4.2mm | 1 per 10 rails |
| Adhesive pocket depth | 1.5mm | 1.3–1.7mm | 1 per 10 adhesive rails |

If any measurement falls outside acceptable range for 2 consecutive spot checks, halt production on that printer and run Z-offset calibration and bed leveling before restarting.

### 1.7 Etsy Photography Workflow

Photograph before the first listing goes live. Re-photograph only when a design revision occurs or a listing image swap is needed to improve conversion.

**Minimum required shots (see post-test-print-doc-3-lifestyle-photography-brief.md for full brief):**
1. Hero lifestyle shot — clip on real desk cable, clean background; this is the Etsy thumbnail
2. Snap-fit detail shot — close-up of the cable seated in the mechanism
3. Before/after installation — same desk, cables loose vs. cables organized
4. Flat-lay color options — all available colors side-by-side, overhead angle
5. In-context full desk — 2–3 clips in use simultaneously, showing the system

**Photography checklist before listing activation:**
- [ ] All photos are 1000×1000px minimum, square aspect ratio
- [ ] Hero shot shows the clip holding a cable (not just the clip alone)
- [ ] No blurry photos (test on mobile phone — if it looks soft, reshoot)
- [ ] Consistent color grading across all photos (batch-edit in Lightroom with neutral white balance)
- [ ] File names are descriptive: `modrun-hero-desk-setup.jpg`, `modrun-detail-snapfit.jpg`, etc.

**Quick setup for a solo shoot (no photographer needed at launch):**
- North-facing window, or an LED panel with a soft diffuser
- Matte white or light gray poster board as background
- Phone on a mini tripod for overhead flat-lay; handheld for lifestyle shots
- Natural cable variety on the desk (USB-C, USB-A, audio) for realism

### 1.8 Etsy Listing and Launch

The Etsy listing copy, tags, and pricing are already prepared in `post-test-print-doc-2-etsy-listing-design-templates.md`. After photography, the only required customization before activating is confirming:
- The bore size range in the listing description reflects the validated sizes from the test print
- Processing time matches your real production cadence (use "3–5 business days" to give buffer; target delivering in 2)
- All photos are uploaded with the hero shot as Photo 1

**Launch timing:** Publish all listings simultaneously between 10 AM and 2 PM on a Thursday. This is when Etsy's algorithm gives new listings the highest organic impression priority during the initial indexing window.

**Etsy Ads:** Enable immediately at $1/day per listing. At this budget, you generate enough click data to identify which tags drive real traffic within 7 days, without meaningful financial risk. The data is more valuable than the sales it generates at $1/day.

### 1.9 Days 1–30 Batch Scheduling Template

After the test print is approved, execute this day-by-day cadence.

**Days 1–3: Slicer Validation**
- Day 1 AM: Print one full production plate (12 clips, `ModRun-PLA-Production-v1` profile). Do not sell from this plate — it is calibration validation.
- Day 1 PM: Run all three QC gates (see Section 4) on all 12 units. If Gate 3 (functional test) fails, diagnose and fix before Day 2.
- Day 2 AM: If Day 1 plate passed: print a rail validation plate (1 desk_clamp rail). Run Gate 3 — confirm clip-to-rail slot engagement.
- Day 3: If both plates passed: lock profiles, tag STLs as v1.0, begin production.

**Days 4–7: First Sales Batch**
- Night of Day 3: Queue overnight clip run (12 clips). Label this run `BATCH 001 PRODUCTION`.
- Day 4 AM: Harvest, run all three QC gates, transfer passing units to finished goods bin.
- Day 4 afternoon: Activate Etsy listings. Set inventory count to match finished goods on hand.
- Days 4–7 daily rhythm: AM — check orders, harvest overnight plate; PM — pack orders, queue next overnight run if stock drops below 10 units.
- Log every QC event in `production-qc-log.csv`: date, printer, plate config, units attempted, pass count, fail count, failure mode.

**Days 8–14: Steady-State Cadence**
- Sunday night: queue 2-plate overnight run (24 clips). This becomes the weekly anchor.
- Mon/Wed/Fri: overnight clip runs (1–2 plates = 12–24 clips per night).
- Tue/Thu daytime: rail runs as orders arrive (print-to-order, no stock held).
- Daily ritual: AM (check orders, harvest, QC), PM (pack and ship, queue next run).
- Target by end of Week 2: 10–15 units shipped, 0–2 returns, 2+ reviews requested in order messages.

**Days 15–21: Process Tightening**
- Review QC log from Weeks 1–2. Identify patterns: specific plate position failing, specific time of day, filament lot correlation?
- If scrap rate exceeds 8%: perform preventive maintenance before Week 3 batch (IPA-wipe and inspect PEI plate; Z-offset calibration; cold-pull nozzle cleaning; re-run bed leveling).
- Increase overnight clip frequency to 4 nights/week if order rate exceeds 15 units/week.
- Begin measuring order-to-ship time: ship date minus order date. Target: under 2 business days (beats stated 3–5 day SLA, drives positive reviews).

**Days 22–30: Month 1 Close**
- Day 22: Review Etsy stats. Check favorites rate (target >5%), conversion rate (target >2%), review count (target 5+), average rating (target 4.8+).
- Day 25: If conversion rate is below 2%, swap a listing image (try the before/after installation shot as the hero) or edit the first two sentences of the description to sharpen the value proposition.
- Day 27: Filament audit. If under 1.5 spools of any color, order 10kg bundle now.
- Day 30 decision point:
  - Orders faster than production: accelerate to daily clip runs; evaluate second printer for Month 2.
  - Orders at steady 20/week pace: continue current rhythm into Month 2. No hardware change.
  - Orders below 15/week: review listing conversion metrics; consider a $10 Etsy Ads bump in Month 2 once you have 10+ reviews to support conversion.

**Batch interleaving rule:** While a 12-clip plate is printing (40–50 minutes), the operator should be harvesting the previous plate, packing orders, printing labels in Pirate Ship, and preparing materials for the next pack session. Never wait idle for a print to finish. The printer is the worker; you are the scheduler.

---

## Section 2: 1 to 20 Units/Week Scaling Path

### 2.1 Weekly Capacity Math

At 20 units/week with a 60% clip / 40% rail mix by revenue:
- Clips needed: ~12 units/week (four 3-clip bundle orders)
- Rails needed: ~8 units/week

**Clip production:**
- One 12-clip plate takes 45 minutes to print.
- 12 clips / 45 minutes = ~16 clip plates needed per week for 12 clips → actually 1 plate covers 12 clips, leaving 0 surplus.
- Practical schedule: 2 plates per week (24 clips produced; 12 held as inventory buffer).
- Two plates = 90 minutes of print time for clips.

**Rail production:**
- One rail per plate at 3 hours. At 8 rails/week, that is 8 × 3 hours = 24 hours of rail print time.
- In practice, rails are print-to-order; you queue each rail as the order arrives rather than holding inventory. This makes the 24-hour print time non-blocking because it is spread across the week.

**Total weekly print hours at 20 units:**
- Clips: 2 plates × 45 min = 1.5 hours
- Rails: 8 plates × 3 hours = 24 hours
- Plate turnaround dead time: ~30 minutes total
- **Total: ~26 hours/week print time**

The single Bambu P1S runs approximately 26 hours per week at 20 units/week — well within its practical capacity (40+ hours/week continuous). No second printer is needed until demand consistently exceeds 35–40 units/week.

### 2.2 Constraint Analysis at This Tier

At 1–20 units/week, there is no real bottleneck. Print time is ample. Post-processing is trivial (under 1 hour/week). Packaging takes under 3 hours/week.

The only operational risks at this tier:
1. **Plate underutilization:** Printing fewer than 8 clips per plate wastes throughput. Always fill the plate.
2. **Unmonitored overnight failures:** Enable Bambu P1S AI failure detection; set up the Bambu handy app to push failure notifications to your phone.
3. **Inventory stockout on clips:** Keep a 10-unit minimum of finished clips on hand. A 12-clip overnight run covers a week of clip demand with buffer.

### 2.3 Post-Processing and Packaging as % of Week

| Activity | Time per week (20 units) | % of operator time |
|---|---|---|
| Print monitoring/setup | ~2 hours | 25% |
| Harvest and QC | ~45 min | 9% |
| Post-processing (rails) | ~30 min | 6% |
| Packaging and labels | ~45 min | 9% |
| Etsy/admin | ~30 min | 6% |
| **Total active hours** | **~5.5–6 hours** | Active time only |

Print is 26 hours but is largely passive. Total hands-on operator time is roughly 5.5–6 hours per week at 20 units/week — achievable alongside a full-time job.

### 2.4 Equipment Utilization Summary

- Bambu P1S utilization: ~26 hours / ~40 practical weekly maximum = 65% utilization
- No second printer needed until utilization exceeds 80% for two consecutive weeks
- PEI plate replacement interval: every 300–500 plates; at 10 plates/week, this is 30–50 weeks

---

## Section 3: 20 to 100 Units/Week Scaling Path

### 3.1 From 20 to 50 Units/Week (Months 3–4)

At 50 units/week (same 60/40 clip/rail mix):
- Clip print hours: ~5 plates/week × 45 min = 3.75 hours
- Rail print hours: ~20 rails/week × 3 hours = 60 hours
- Total print hours: ~64 hours/week

One printer cannot sustain 64 print-hours in a 7-day week without approaching 100% utilization and leaving no maintenance buffer. In practice, the clip/rail mix in early months skews toward clips — buyers try clips first, then add rails. Assume a 70% clip / 30% rail mix in Months 3–4.

Revised at 70/30 mix (50 units/week):
- Clip print hours: ~30 clips/week = 2.5 plates × 45 min = ~1.9 hours
- Rail print hours: ~15 rails/week × 3 hours = 45 hours
- Total: ~47 hours/week

One printer at ~47 hours/week is near-full utilization. The printer runs 6–7 hours every day. This is manageable solo but requires intentional scheduling:

**Scheduling discipline at 50 units/week:**
- Overnight clip runs 4–5 nights/week (12–24 clips per run, unattended)
- Rail runs during daytime when the operator can harvest and deburr promptly
- Weekly printer maintenance window: Sunday morning — nozzle cold pull, PEI plate inspection, bed leveling calibration

**Second printer trigger:** When the single printer runs at 80%+ utilization for 2 consecutive weeks AND a backorder queue is accumulating. At 50 units/week, you are close to that threshold if rail demand is high. The trigger is typically around week 8–12 at sustained demand. Cost: $699–$799 for a second Bambu P1S. Payback: 3–5 weeks at 50-unit/week throughput.

**Filament sourcing shift:** At 25–30kg/month consumption (50 units/week, blended clip/rail weights), transition from per-spool Amazon purchases to 10kg bundles ($11–13/kg) and qualify Anycubic's 50kg pallet deal ($10.49/kg) as a backup supplier. Place one Anycubic test order in Month 2 to validate AMS compatibility on your specific printer before committing to pallet quantities.

### 3.2 From 50 to 100 Units/Week (Months 5–6)

Two printers. This is the threshold where operational mode shifts from "solo hobbyist with discipline" to "small manufacturing operation."

**Two-printer operating model:**
- Printer 1: dedicated to clips; overnight runs Sunday through Thursday, 12–24 clips per night
- Printer 2: dedicated to rails and PETG/custom orders during the day
- At 12-clip plates on both printers simultaneously: 24 clips per 50-minute cycle
- In a 16-hour production day: approximately 290+ clips or 5–6 rails — well above 100 units/week

**Post-processing becomes the bottleneck above 80 units/week:**
- Post-processing per clip: 5–8 seconds
- Post-processing per rail: 40–50 seconds
- At 80 clips/week + 20 rails/week: ~11 minutes clips + ~17 minutes rails = ~28 minutes/week post-processing
- This is not the bottleneck — packaging is

**Packaging as the true bottleneck:**
- 90–120 seconds per order × 100 orders/week = 150–200 minutes = 2.5–3.5 hours/week
- This is still manageable solo

The contractor threshold is at packaging-plus-admin exceeding 3 hours/day consistently, which happens around 100–120 units/week. A 10-hour/week 1099 contractor at $15/hour ($600/month) is the right hire: they handle harvest-to-bin, packaging, label application, and USPS drop. The operator retains print queue management, QC gates, Etsy communications, and printer maintenance.

### 3.3 Supplier Transition Protocol: FDM to Outsourced Manufacturing

For most cable management SKUs, Bambu P1S in-house FDM remains cost-competitive well into Month 12. The cost model shows FDM COGS for clips at $0.08–$0.13 and rails at $1.79–$2.38 — injection molding at comparable volumes (under 10,000 units/year) is more expensive, not cheaper.

The decision to evaluate external manufacturing applies only when:
- Annual volume of a single SKU exceeds 5,000–10,000 units (where tooling amortization becomes favorable)
- A premium surface finish is required (injection molding) or a different material property is needed (e.g., polycarbonate impact resistance)
- You are adding a new product that does not benefit from parametric design flexibility

**If evaluating external manufacturing in Month 6+:**
1. Get 3 quotes from domestic SLA/SLS vendors for small-batch (500–2,000 units) test runs alongside your in-house FDM
2. Compare landed COGS including shipping and lead time risk
3. In-house FDM breaks even against most small-batch external manufacturing under ~2,000 units/run at current filament prices
4. Continue in-house FDM as the primary channel; use external manufacturing only for SKUs that genuinely cannot be made on FDM (e.g., flexible overmolded parts, metal-insert assemblies)

### 3.4 Packaging and Shipping Workflow at Scale

**Packaging progression:**

| Order volume | Recommended format | Cost/unit | When to switch |
|---|---|---|---|
| 1–100 total orders | Generic poly mailer, 9×12" | $0.05–$0.10 | — |
| 50+/month | noissue custom-branded mailers | $0.20–$0.35 | Month 2–3 |
| 200+/month | EcoEnclose custom mailers | $0.15–$0.25 | Month 4–5 |
| Rail orders (all tiers) | Generic corrugated box, 7×4×3" | $0.15–$0.25 | Launch through Month 6 |

Include 4× 3M rubber bumper pads with each rail ($0.20–$0.32 COGS) from launch. This solves the "scratched my desk" review before it becomes one.

**Label printing workflow (Pirate Ship, daily batch):**
1. Export day's Etsy orders as CSV from Etsy Orders page
2. Import into Pirate Ship (supports up to 100 orders per batch import)
3. Pre-fill package weights by SKU (single clip: 30g; 3-clip bundle: 120g; rail: 200g)
4. Select USPS Ground Advantage for all orders under 450g
5. Purchase and print batch labels — under 2 minutes per day's orders
6. Mark all orders as shipped in Etsy immediately (triggers automatic tracking email to customers)

**Thermal label printer ROI:** Rollo X1038 (~$180 one-time) eliminates per-label ink cost (~$0.06–$0.08/label on inkjet), removes the cut-and-tape step, and produces cleaner-looking labels. At 50+ labels/week, payback is within 4–6 months.

### 3.5 Inventory Management

**Finished goods targets by tier:**

| Weekly volume | Target clip stock (units) | Rail stock | Rationale |
|---|---|---|---|
| 1–20/week | 10–20 clips | 0 (print-to-order) | 1-week buffer; clips are fast to reprint |
| 20–50/week | 20–40 clips | 0–4 rails | 2-week buffer; reduces rush risk |
| 50–100/week | 40–80 clips | 5–10 rails | Buffer handles demand spikes |

**Filament safety stock:**
- Maintain a minimum of 2 full spools (2kg) of each active color at all times
- Reorder trigger: any color drops below 1 spool (1kg)
- At 20 units/week, a single spool lasts approximately 2–3 weeks
- At 50 units/week, order in 10kg bundles; plan 1 order per month per primary color

**Reorder points:**
- eSUN PLA+ 10kg bundle (Amazon Prime): order 5 days before projected stockout (2-day delivery + 3 days buffer)
- Anycubic pallet (50kg, direct): order 10 days before stockout (7-day lead time + 3 days buffer)
- Poly mailers: reorder at 50-unit stock level (3–5 day Amazon delivery); order in 500-unit quantities for pricing

---

## Section 4: Quality Control Protocol

### 4.1 Per-Unit QC — Three Gates

Run all three gates every plate run. Do not reduce to sampling for Gates 1 and 3 until you are at 50+ units/week.

**Gate 1 — Visual inspection at harvest (every unit, 5 seconds each):**
- Snap arm present and not deformed or broken
- Cable bore opening gap not fused shut by stringing (if stringing bridges the gap, it is reworkable: remove with tweezers in 15 seconds)
- First layer fully adhered (no corner lifting visible on the underside)
- No obvious delamination or layer separation visible on exterior
- For rails: slot entries free of major obstruction; clamp arm surface continuous with no cracking at Z-seam junction

**Disposition:** Pass → pass bin. Fail (structural: snap arm broken) → scrap. Fail (reworkable: stringing across bore) → rework bin.

**Gate 2 — Dimensional spot check (1 per 20 clips or 1 per 10 rails, 30 seconds):**
Use digital calipers. Measure the three points below. Record results in the QC log.

| Point | Design value | Acceptable range |
|---|---|---|
| Snap arm width (narrowest) | 7.6mm | 7.3–7.9mm |
| Snap arm length | Per design | ±0.5mm |
| Clip bore entry gap width | BORE × BORE_GAP_RATIO | ±0.3mm |
| Rail slot width (clips slide in here) | Per design | ±0.3mm |

If two consecutive spot checks fail on the same dimension: halt the run and diagnose before the next plate. Consistent dimensional drift indicates Z-offset drift, over-extrusion, or under-extrusion — each has a specific fix.

**Gate 3 — Functional test (1 per plate, 60 seconds):**
This test is non-negotiable. A part can pass Gate 1 and Gate 2 and still fail Gate 3 due to snap arm brittleness (which visual and dimensional checks cannot detect).

1. Press clip into rail slot: expect a tactile click with no binding, no excessive force required
2. Insert a test cable of the target bore diameter: clip should retain cable without falling out under gentle pull
3. Remove and reinsert the clip 3 times: snap arm should show no cracking, deformation, or permanent set
4. Flex the snap arm manually to approximately half its travel range: should return to neutral position without any visible cracking

**If Gate 3 fails:** Stop the production run immediately. Do not ship any units from this plate. Diagnose: nozzle temperature? minimum layer time? wall count? Adjust profile, print a single test clip, re-run Gate 3 before continuing production.

### 4.2 Per-Batch QC — Extended Stress Test

Run this test on the first plate of each new filament lot (new spool or new supplier) and once every 2 weeks during steady production.

1. Remove and reinsert a sample clip 5 times: snap arm should show no fatigue
2. Flex the snap arm to approximately 80% of full travel: should return without permanent set
3. Apply a cable and attempt to pull it free with steady firm force: the clip should retain the cable until approximately 1–2kg of pull force (not required to measure precisely — if it pulls free with light finger tension, the nub height is undersized)

**Stress test failure:** If a clip fails the extended stress test but passed Gate 3, the issue is filament quality or slicer calibration drift. Pull units from the prior 2–3 production days and run Gate 3 on samples from each day to determine when the issue began.

### 4.3 Failure Categories and Disposition

| Failure type | Category | Disposition |
|---|---|---|
| Snap arm snapped | Structural | Scrap; do not rework — PLA+ cannot be bonded structurally |
| Layer separation at Z-seam | Structural | Scrap if at snap arm or clamp junction; sell as B-grade if cosmetic only |
| Stringing across cable bore | Reworkable | Remove with tweezers (15 sec); re-inspect Gate 1 before sale |
| Dimensional out-of-spec | Tolerance | Scrap; adjust slicer or CadQuery parameter before next run |
| Bed adhesion failure (partial) | Print failure | Scrap entire plate; inspect PEI plate and Z-offset |
| Minor surface cosmetic defect | Cosmetic | Sell as B-grade or in discount bundles; never ship to a customer who paid full price without disclosure |
| Stringing in slot (rail) | Reworkable | Deburr with craft knife (15–20 sec); re-inspect |
| Adhesive pocket floor incomplete | Structural | Scrap; check extrusion multiplier |

### 4.4 Failure Rate Thresholds

| Stage | Acceptable scrap rate | Action if exceeded |
|---|---|---|
| First 2 weeks | Up to 15% | Expected during profile calibration; diagnose if not improving week-over-week |
| Weeks 3–8 | Under 8% | Review QC log for pattern; perform maintenance if no clear cause |
| Mature production (Month 2+) | Under 5% | Target steady-state benchmark |
| Any single plate | Under 20% (max 2–3 fails out of 12) | If a plate exceeds 25% fail rate, inspect printer before the next run |

**Production halt trigger:** If a customer reports a snap arm failure, and you have units from the same filament lot and production day still in inventory, pull those units and run Gate 3 on samples before shipping. A 1% or higher field failure rate in a single week is a production halt event — diagnose root cause before resuming.

### 4.5 QC Log

Maintain a running spreadsheet (`production-qc-log.csv`) with the following columns:

```
Date | Printer | Plate config | Units attempted | Pass | Fail | Failure mode | Filament lot | Notes
```

Review weekly. Patterns to watch:
- Failure rate increasing on a specific printer → maintenance trigger
- Failures clustering on a specific filament lot → lot quality issue; contact supplier
- Snap arm failures increasing → check nozzle temperature and minimum layer time setting
- Bed adhesion failures increasing → replace or resurface PEI plate

---

## Section 5: Month 1 Launch Checklist

This checklist gates the first customer shipment. Every item must be checked before a single unit ships to a paying customer.

### 5.1 Design and STL Readiness

- [ ] Test print completed and all QC gates passed
- [ ] FDM_TOLERANCE adjusted (if needed) and validated with a second print
- [ ] Production STLs generated for all launch SKUs (6mm clip, 12mm clip, desk_clamp rail minimum)
- [ ] STLs archived in `/stl/v1.0/` with correct naming convention
- [ ] CadQuery source files committed to git with version tag `v1.0`
- [ ] Production slicer profile saved as `ModRun-PLA-Production-v1` in Bambu Studio
- [ ] Slicer profile settings documented (Layer height, walls, infill, nozzle temp, min layer time)

### 5.2 Validation Batch

- [ ] One full production plate (12 clips) printed from production slicer profile
- [ ] All three QC gates passed on the validation plate
- [ ] Gate 3 (functional test) specifically documented: date, result, notes
- [ ] Scrap rate for validation plate recorded in QC log
- [ ] Mixed plate (1 rail + 4 clips) printed and all QC gates passed

### 5.3 Supplier Setup

- [ ] eSUN PLA+ 10kg bundle ordered (Amazon Prime); at minimum 2 colors (black, white)
- [ ] Pirate Ship account created; Etsy shop connected; test shipping label printed
- [ ] 100+ poly mailers (9×12") on hand
- [ ] 50+ corrugated boxes (7×4×3") on hand for rails
- [ ] Zip-lock bags (for clip bundles) on hand
- [ ] Kraft tissue paper or padding on hand (for poly mailer cushioning)
- [ ] Thank-you cards designed and printed (optional at launch but recommended; $0.05–$0.10/unit at Vistaprint 500-run)
- [ ] 3M rubber bumper pads purchased (for rail orders; 4 per order)

### 5.4 Etsy Listing Readiness

- [ ] Listing copy written and reviewed (title, description, tags — per post-test-print-doc-2-etsy-listing-design-templates.md)
- [ ] All 5 photos taken, edited, and uploaded (hero lifestyle shot confirmed as Photo 1)
- [ ] Pricing confirmed: clips at target price (model basis: $24.99 for 3-clip bundle), rails at $34.99
- [ ] Shipping profile configured in Etsy (processing time: 3–5 business days; shipping: USPS First Class)
- [ ] FAQ answers pre-written in Etsy shop Q&A section
- [ ] Shop policies written (30-day satisfaction guarantee, replacement protocol)
- [ ] Listing in draft mode, ready to activate

### 5.5 First 20 Units Ready to Ship

- [ ] 20 units (mix of clips and rails per planned inventory) printed and in finished goods bin
- [ ] All 20 units passed Gate 1 (visual) and a sample passed Gates 2 and 3
- [ ] Units organized by SKU in labeled bins (not mixed in a single box)
- [ ] Packaging materials staged at packing station
- [ ] Packing slip template ready (or confirmation that Etsy order printout serves this purpose)
- [ ] Pirate Ship configured for one-click label generation by SKU weight

### 5.6 Operations Process Documented

- [ ] QC log spreadsheet (`production-qc-log.csv`) created and first validation batch entered
- [ ] Weekly print schedule written down (which nights are clip runs, which days are rail runs)
- [ ] Filament reorder trigger defined in writing (reorder at 1 spool remaining)
- [ ] Customer replacement protocol written: response time, reprint timeline, no-return policy for defectives
- [ ] Order-to-ship time tracked from Day 1 (date order received, date shipped — track in a spreadsheet)

### 5.7 Customer Fulfillment SOP (Pick-Pack-Ship)

For each order received:

1. Confirm product variant and quantity in Etsy order confirmation
2. Pull units from finished goods bin (clips); queue a print job immediately if a rail order arrives and no rail is in stock
3. Inspect each unit for in-transit damage before packing (Gate 1 repeat: 5 seconds)
4. For clip bundles: place clips in a zip-lock bag, then into poly mailer with a folded kraft sheet as padding; add thank-you card
5. For rails: place rail in corrugated box with foam corner pieces or crumpled kraft; affix 4× rubber bumper pads to the clamp base before boxing; close and tape
6. Print shipping label in Pirate Ship (batch all day's labels at once; takes 2 minutes)
7. Apply label; mark order as shipped in Etsy immediately (triggers tracking email to customer)
8. Drop off at USPS or schedule pickup (Pirate Ship supports free pickup scheduling)
9. Record ship date in tracking spreadsheet

**Processing time commitment:** Aim to ship every order within 2 business days of receipt, regardless of the stated 3–5 day Etsy processing time. Beating the stated SLA consistently is the single highest-leverage action for generating 5-star reviews.

---

## Six-Month Revenue and Scaling Projection

| Month | Target volume | Printer count | Gross revenue | Net profit | Key milestone |
|---|---|---|---|---|---|
| Month 1 | 20 units/week | 1 | ~$2,500 | ~$1,250–$1,500 | Startup capital recovered |
| Month 2 | 25–30 units/week | 1 | ~$3,000–$3,600 | ~$1,500–$1,800 | 20+ reviews; conversion rate optimized |
| Month 3 | 35–45 units/week | 1 | ~$4,200–$5,400 | ~$2,100–$2,700 | Printer near full utilization |
| Month 4 | 50 units/week | 1 (→ 2) | ~$6,000 | ~$3,000–$3,600 | Second printer ordered |
| Month 5 | 65–80 units/week | 2 | ~$7,800–$9,600 | ~$4,000–$5,000 | Two-printer rhythm established |
| Month 6 | 100+ units/week | 2 | ~$12,000+ | ~$6,500–$8,000 | Contractor evaluation threshold |

Revenue basis: $24.99 per clip order (3-clip bundle), $34.99 per rail order, blended at 60% clips / 40% rails by order count. Net profit after Etsy fees (~9.5%), COGS, and shipping. No contractor cost through Month 5; $600/month contractor added at Month 6.

---

## Assumptions Made in This Document

The following assumptions were made where test-print data is not yet available:

1. **FDM_TOLERANCE at 0.15mm will require adjustment.** The functional fit of clip-to-rail and clip-to-cable in FDM is always printer-specific. The adjustment will be either 0.10mm (tighter) or 0.20mm (looser) — the exact value comes from the test print evaluation.

2. **Print times of 40–50 minutes for a 12-clip plate.** This is based on P1S specifications and PLA+ at 0.4mm nozzle, 0.20mm layer height, and Quality preset. Actual time on your specific printer with your slicer profile should be measured on the first production plate and this document updated accordingly.

3. **Clip-to-rail mix of 60% clips / 40% rails by order count.** Real demand mix will emerge from the first 30–60 days of Etsy data. If rails significantly outperform clips, the total weekly print hours will increase substantially (rails are 3–4x longer per unit than clip batches), and the second-printer trigger arrives sooner.

4. **USPS Ground Advantage rates as of May 2026 (including the 8% temporary surcharge through January 2027).** Shipping costs in this document reflect this elevated rate environment. Rates will decrease in January 2027.

5. **Scrap rate of 8–15% in weeks 1–2, trending to 3–5% at mature production.** These are industry benchmarks for FDM PLA+ production. Your actual calibration curve may be faster (if the printer is already well-tuned) or slower (if significant tolerance adjustment is needed).

---

*Sources: production-scaling-research.md, phase-2-supplier-research.md, cost-model-spreadsheet.csv, post-test-print-doc-2-etsy-listing-design-templates.md, and post-test-print-doc-3-lifestyle-photography-brief.md — all in /projects/mfg-farm/. COGS verified against eSUN PLA+ at April 2026 Amazon pricing ($12/kg at 10kg bundles). USPS rates reflect the 8% temporary surcharge in effect through January 17, 2027 (Pirate Ship commercial rates). Printer depreciation at $0.14/hr based on $699 Bambu P1S and 5,000-hour depreciation life. Etsy fees: 6.5% transaction + ~3% payment processing.*
