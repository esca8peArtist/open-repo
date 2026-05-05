---
title: ModRun Production Workflow v1 — Post-Test-Print Execution Guide
date: 2026-05-05
status: active
version: 1.0
scope: Post-test-print production workflow, scaling roadmap, economics, packaging, failure recovery
related: production-scaling-research.md, scaling-production-research.md, fulfillment-workflow.md, post-test-print-doc-4-first-week-operations-sop.md
---

# ModRun Production Workflow v1

**Purpose**: The test print is done. This document is what happens next — a single, start-to-finish production guide that takes you from validated STL to shipped order, at every volume tier from 1 unit through 100+ per week.

**Lead finding**: The bottleneck at 1–20 units/week is not the printer — it's discipline. Plate utilization, profile version-locking, and a consistent QC gate are the only habits that matter at this stage. The printer can run 16 hours a day. The question is whether your workflow lets it.

---

## 1. Post-Test-Print Workflow

### 1.1 STL Generation and Version Locking

After the test print, you will almost certainly need one tolerance adjustment before production. The most likely change: `FDM_TOLERANCE` (currently 0.15mm per side) may need to move to 0.10mm (tighter snap fit) or 0.20mm (looser fit if clip binds in rail slot). Make that change in the CadQuery source, regenerate the STL, and lock it as v1.0.

Directory structure to establish immediately:

```
/modrun-production/
  /cadquery/        — .py source files (git-tracked)
  /stl/
    /v1.0/          — First validated production STLs
    /test-prints/   — Test variants; never mixes with production
  /sliced/
    /production/    — Active .3mf files per plate configuration
    /archive/       — Superseded plate configs
```

File naming convention: `modrun_clip_6mm_v1.0_12up_0.20mm_20pct.3mf`

This encodes: product, bore size, version, units-per-plate, layer height, infill. Never overwrite v1.0. When a change is needed, increment to v1.1 and re-validate before production.

### 1.2 Slicing — Production Profile

Save these settings as `ModRun-PLA-Production-v1` in Bambu Studio and do not deviate for production runs.

| Parameter | Value | Rationale |
|---|---|---|
| Layer height | 0.20mm | 0.15mm adds 25–30% print time for no functional benefit on a cable clip |
| Walls | 3–4 | 3 minimum for snap arm; 4 adds insurance on rail clamp corners |
| Infill density | 20% | Below this, snap arm becomes brittle at installation |
| Infill pattern | Gyroid | Isotropic load distribution; critical for a snap arm that deflects in two directions |
| Outer wall speed | 150–200mm/s | 200mm/s achievable without dimensional loss on P1S/PLA+ |
| Infill speed | 300–500mm/s | Has negligible effect on part quality |
| Minimum layer time | 8 seconds | Prevents soft snap arm from being overheated by successive passes |
| Nozzle temp | 222°C | Slightly above eSUN nominal; improves interlayer adhesion at snap arm section |
| Bed temp | 55°C | Standard PEI adhesion for PLA+ |
| Supports | None | Both parts are designed support-free |
| First layer | Default Bambu squish | IPA-wipe the PEI plate before every plate run |

### 1.3 Plate Configuration

**Clips:** Target 12 per plate in a 4×3 grid, 8mm spacing. This is the production standard. Do not print fewer than 8 per plate in production — single-unit or small-batch plate loading is a significant throughput waste.

**Rails:** 1 desk_clamp rail per plate, or 2 adhesive-variant rails per plate. If running a mixed plate, 1 rail + 4 clips is a good utilization configuration.

### 1.4 Print Execution — Expected Times

| Product | Plate config | Print time | Effective time per unit |
|---|---|---|---|
| Clip (6mm bore) | 12 per plate | 40–50 min | 3.5–4.5 min |
| Clip (12mm bore) | 12 per plate | 50–65 min | 4.5–5.5 min |
| Rail (desk_clamp) | 1 per plate | 2.5–3.5 hr | 2.5–3.5 hr |
| Rail (adhesive) | 2 per plate | 1.5–2.5 hr | 45–75 min |

Monitor first 3 minutes of every plate for bed adhesion. Monitor final 10% for detachment or warping. The Bambu P1S AI failure detection is enabled by default in 2026 firmware — verify this is active before unattended runs.

### 1.5 Post-Processing

ModRun parts are support-free by design. Post-processing is minimal.

**Clips:** Flex the PEI plate to release. Parts should pop free when the plate cools to ~40°C. Do not force removal on a hot plate. Harvest time per 12-clip plate: under 60 seconds.

**Rails (desk_clamp):** The slot openings may have minor stringing. A 10–15 second pass with a deburring tool or craft knife on each slot entry is the only required finishing step. Do not sand the clamp faces — they need dimensional accuracy for desk-edge grip.

**Per-unit post-processing time:**
- Clip (standard): 5–8 seconds (pop, inspect, bin)
- Rail (desk_clamp): 40–50 seconds (harvest + slot deburring + inspect)
- Rail (adhesive): 25–35 seconds (harvest + pocket-floor check + inspect)

### 1.6 Quality Control Gates

Run three checkpoints, in sequence. Do not skip them even on "obvious" good runs.

**Gate 1 — Visual at harvest (every unit, 5 sec each):**
- Snap arm present and intact
- Cable bore opening not fused shut by stringing
- No warping visible at base
- First layer fully adhered (no corner lifting)

**Gate 2 — Dimensional spot check (1 per 20 units, 30 sec):**
- Snap arm width: 7.6mm ± 0.3mm (use digital calipers)
- Rail slot width: within ±0.3mm of design
- Any consistent dimensional drift triggers a printer inspection before the next run

**Gate 3 — Functional test (1 per plate, 60 sec):**
- Press clip into rail slot: expect a tactile click with no binding
- Insert a test cable (appropriate bore size): clip should retain without falling out
- Remove and reinsert clip 3 times: no cracking or permanent deformation in snap arm
- This is the critical test for FDM_TOLERANCE and SNAP_NUB_HEIGHT correctness

If Gate 3 fails, stop the production run. Diagnose before the next plate.

### 1.7 Photography

Product photography before first listing and after each design change. Not every production run.

**Setup:** Overhead shot on a matte white or grey surface, natural daylight or LED panel. No flash. Show the clip snapped onto an actual cable, and the rail mounted to a desk edge. Use your phone — the Etsy buyer is looking at a 400×400px thumbnail; a clean iPhone shot in good light beats a mediocre DSLR shot in bad light.

**Shots needed per SKU:**
1. Hero shot — clip on cable, clean background (listing thumbnail)
2. Detail shot — snap arm visible, showing the flex mechanism
3. In-use shot — clip on rail, multiple cables organized
4. Scale reference — clip next to a common cable type

Re-photograph when: new color, design revision, or you want to test a listing image swap to improve conversion.

### 1.8 Listing and Fulfillment

Listing is already prepared (per the Etsy launch kit). After successful test print, the only listing update required is: confirm the bore size range in the listing copy reflects the actual validated sizes from the test print, and mark listing as Active.

Fulfillment SLA: ship within 3 business days of order. At 1–5 units/week, a same-day or next-day print-and-ship cadence is easily achievable.

---

## 2. Scaling Roadmap

### Tier 1 — 1 to 20 units/week (Months 1–2)

**Single Bambu P1S, solo operator.**

The printer runs 3–5 days per week, averaging 2–4 hours of printing per day. Weekly active time: approximately 14–16 hours of printing plus 1.5 hours post-processing and packaging. Total hands-on time: about 5–6 hours per week (print is largely unattended).

**Batch discipline:** Print in 12-clip batches from day one. Never print one clip per plate. A single 12-clip overnight run Sunday night stocks you for Monday–Wednesday order fulfillment.

**QC sampling:** Full Gate 1 + Gate 2 + Gate 3 on every plate. At this volume, there is no cost to full QC.

**Weekly schedule pattern:**
- Sunday PM: Queue overnight clip run (12–24 clips; 1–2 plates)
- Monday AM: Harvest, QC, add to finished goods stock
- Mon–Fri: Print-to-order for rails as orders arrive; pull clips from stock
- Friday PM: Review QC log, replenish filament if under 1 spool

**Per-unit time breakdown at 20-unit/week tier:**
- STL/slicer setup (amortized): 0.5 min
- Print time (effective, at 12-up): 4 min
- Plate harvest: 0.5 min
- Post-processing: 0.1 min (clips); 0.75 min (rails)
- QC (Gates 1 + 2 + 3 amortized): 0.5 min
- Photography: 0 min (already done)
- Packaging + label: 1.5 min
- Shipping admin: 0.25 min (batch Pirate Ship, amortized)
- **Total per clip: ~7 min | Total per rail: ~10 min**

### Tier 2 — 20 to 50 units/week (Months 3–4)

**Single Bambu P1S approaching full utilization.**

At 50 units/week with a clip-heavy mix, the printer runs approximately 35 hours/week. This requires intentional scheduling: overnight clip runs 3–4 nights per week, rail runs during the day. The printer is active roughly 70% of operating hours — near the practical ceiling for a single machine.

**Key actions at this tier:**
- Schedule is the product. Build a weekly print calendar (Sunday: queue; Mon/Wed/Fri nights: overnight clip runs; Tue/Thu daytime: rails).
- Maintain 1.5–2 weeks of clip finished goods inventory. Clips can be batch-printed and stocked; rails remain print-to-order.
- Track plate utilization in the QC log. Any plate with <10 clips is a waste event.
- Begin ordering filament in 10kg bundles rather than per-spool.

**Scaling trigger:** When the printer runs at 80%+ utilization for 2 consecutive weeks AND you have a backorder queue, order the second printer. Expected trigger: week 8–12 at sustained 35–40 units/week demand.

**Per-unit time breakdown at 50-unit/week tier:**
- Print time (effective): 4 min (clips) / 45 min (rails)
- Post-processing: 0.1 min (clips) / 0.75 min (rails)
- QC (Gate 1 always; Gates 2+3 at 1:20 sampling): 0.15 min (clips)
- Packaging + label: 1.25 min (batch efficiency improving)
- Shipping admin: 0.1 min (Pirate Ship batch, amortized at 50+/week)
- **Total per clip: ~6 min | Total per rail: ~8 min**

### Tier 3 — 50 to 100+ units/week (Months 5–6)

**Two Bambu P1S printers, dedicated print schedule.**

Two printers running 12-clip plates simultaneously produce 24 clips per 50-minute cycle. In a 16-hour production day, two printers yield approximately 288+ clips — well above the 100-unit/week threshold. Rail throughput doubles to 10–14 per day.

**Workflow shift with two printers:**
- Printer 1 runs clips overnight (unattended, AI failure detection active)
- Printer 2 runs rails during the day (rails require more harvest attention due to slot deburring)
- Post-processing and packaging become the active bottleneck above 80 units/week
- Consider a 10-hour/week contractor for packaging and shipping admin when packaging exceeds 3 hours/day consistently (approximately 100+ units/week threshold)

**QC sampling shift at this tier:**
- Gate 1 (visual): every unit
- Gate 2 (dimensional): 1 per 30 units (1.5kg filament throughput)
- Gate 3 (functional): 1 per plate (unchanged)
- Full batch audit: triggered by any Gate 3 failure or elevated Gate 1 reject rate

**Per-unit time breakdown at 100-unit/week tier:**
- Print time (effective): 4 min (clips) / 45 min (rails)
- Post-processing: 0.1 min (clips) / 0.75 min (rails)
- QC (sampling): 0.1 min (clips)
- Packaging + label: 1.1 min (thermal label printer + batch workflow)
- Shipping admin: 0.05 min (fully batched)
- **Total per clip: ~5.5 min | Total per rail: ~7.5 min**

---

## 3. Production Economics

### 3.1 Per-Unit COGS

All estimates use PLA+ at $12/kg (10kg bundle rate), Bambu P1S depreciated over 5,000 hours at $699 purchase price ($0.14/hr), and $15/hr labor.

**Clip (6mm bore, ~3g, 12-up plate at 45 min):**

| Component | Cost |
|---|---|
| Filament (3g at $12/kg) | $0.04 |
| Electricity ($0.025/hr × 45min ÷ 12) | $0.002 |
| Printer depreciation ($0.14/hr × 45min ÷ 12) | $0.009 |
| Scrap buffer (5%) | $0.002 |
| Post-processing labor (8 sec @ $15/hr) | $0.03 |
| Packaging (mailer shared ÷ 3 clips in bundle) | $0.03 |
| **COGS per clip** | **$0.11** |

**Rail (desk_clamp, ~85g, 3hr per plate):**

| Component | Cost |
|---|---|
| Filament (85g at $12/kg) | $1.02 |
| Electricity ($0.025/hr × 3hr) | $0.075 |
| Printer depreciation ($0.14/hr × 3hr) | $0.42 |
| Scrap buffer (5%) | $0.06 |
| Post-processing labor (45 sec @ $15/hr) | $0.19 |
| Packaging (small box) | $0.25 |
| **COGS per rail** | **$2.02** |

Material is a negligible input for clips — the $0.04 filament cost is swamped by packaging and labor. For rails, printer depreciation dominates at $0.42/unit. Both products operate at extraordinary material efficiency.

### 3.2 Per-Unit Labor Hours by Volume

| Volume tier | Labor min per clip | Labor min per rail | Effective $/hr output |
|---|---|---|---|
| 1–5/week (single-unit ops) | ~12 min | ~18 min | Low; overhead-dominated |
| 20/week | ~7 min | ~10 min | $15–18/hr equivalent |
| 50/week | ~6 min | ~8 min | $20–25/hr equivalent |
| 100/week | ~5.5 min | ~7.5 min | $25–30/hr equivalent |

Labor efficiency improves with volume because packaging, shipping admin, and QC overhead are amortized across more units per session.

### 3.3 Gross Margin per Order

**3-clip bundle on Etsy at $24.99:**

| Component | Cost |
|---|---|
| Clip COGS × 3 | $0.33 |
| Packaging (poly mailer + zip bag) | $0.18 |
| Shipping (USPS First Class, ~120g, zone 4 avg.) | $4.50 |
| Etsy transaction fee (6.5%) | $1.62 |
| Etsy payment processing (~3% + $0.25) | $1.00 |
| **Total cost per order** | **$7.63** |
| **Revenue** | **$24.99** |
| **Gross profit** | **$17.36** |
| **Gross margin** | **69.5%** |

**Rail (desk_clamp) on Etsy at $34.99:**

| Component | Cost |
|---|---|
| Rail COGS | $2.02 |
| Packaging (small box + padding) | $0.35 |
| Shipping (USPS First Class, ~200g) | $5.50 |
| Etsy transaction fee (6.5%) | $2.27 |
| Etsy payment processing | $1.30 |
| **Total cost per order** | **$11.44** |
| **Revenue** | **$34.99** |
| **Gross profit** | **$23.55** |
| **Gross margin** | **67.3%** |

### 3.4 Equipment Investment and Break-Even

**Startup capital (single printer, launch):**
- Bambu P1S: $699
- Starting filament (3 spools PLA+): $60
- Packaging supplies (100 mailers, 50 small boxes, zip bags): $40
- Pirate Ship: free
- Thermal label printer (optional at launch): $180
- **Total: ~$800–$980**

**Monthly revenue at 20 units/week (60% clips / 40% rails):**
- 12 clip orders/week × $24.99 × 4.3 = ~$1,290
- 8 rail orders/week × $34.99 × 4.3 = ~$1,204
- Total gross: ~$2,494/month

**Monthly net at 20 units/week (after COGS, shipping, fees):**
- Gross margin blended at 68%: ~$1,696
- Fixed costs (filament, packaging, depreciation): ~$150/month
- **Net profit: ~$1,250–$1,500/month**

**Break-even on startup capital:** $980 ÷ $1,300/month ≈ **3.5 weeks.** The printer pays for itself before the end of Month 1 at 20-unit/week production.

**Second printer trigger and payback:**
- Investment: $699
- Timing: When first printer runs at 80%+ utilization for 2 consecutive weeks (expected weeks 8–12)
- Payback: 3–5 weeks at 50-unit/week throughput

---

## 4. Packaging and Shipping

### 4.1 Packaging Selection

**Launch default (orders 1–100): Generic poly mailers**
- Source: Amazon or ULINE
- Size: 9×12" for clips; 10×13" for small rail packages
- Cost: $0.05–$0.10 per mailer
- No branding, but fast and functional
- Use kraft tissue paper inside for cushioning and a cleaner unboxing feel ($0.03/order)

**Rails:** Pack in a small rigid mailer or corrugated box. A 200mm rail will not lie flat in a poly mailer without risk of crease damage to the clamp arm. Generic small corrugated boxes (Amazon, 7×4×3"): $0.15–$0.25 each.

**Growth phase (orders 100–500): noissue custom-branded mailers**
- Minimum order: 100 units
- Cost: ~$0.20–$0.35/unit with custom print
- Compostable option available — aligns well with Etsy's buyer values
- Order when monthly order volume hits 50+/month

**Scale phase (orders 500+): EcoEnclose custom mailers**
- Minimum order: 500 units for custom printing
- Cost: ~$0.15–$0.25/unit
- 100% recycled material; Etsy official partner
- Strong review psychology: buyers mention eco packaging in positive reviews

### 4.2 Padding Strategy

For clips in a poly mailer, a sheet of crumpled kraft paper or tissue wrapping is sufficient. Clips are dense PLA+ — they do not crack from moderate shipping impacts. The failure mode is cosmetic scuffing, not structural damage.

For rails, include two or four small foam corner pieces or a folded kraft paper insert to prevent the clamp arm from taking impact directly. The 4mm CLAMP_ARM_THICKNESS is robust, but a direct corner impact during transit can chip the layer boundary. Add 3M rubber bumper pads (4 per rail, $0.20–$0.32 COGS) — this both protects the clamp arm in shipping and solves the "scratched my desk" review problem in one move.

### 4.3 Postage Label Workflow

Use **Pirate Ship** as the default shipping platform. It provides USPS commercial rates below retail with no monthly fee.

**Workflow:**
1. Export day's Etsy orders as CSV from Etsy Orders page
2. Import into Pirate Ship (batch import supports up to 100 orders per import)
3. Pre-fill weights by product SKU: single clip ~30g package, 3-pack ~120g, rail ~200g
4. Select USPS First Class Package for all orders under 450g (~1 lb)
5. Purchase labels in batch — takes under 2 minutes for a day's orders
6. Print on thermal label stock (Rollo X1038 at $180, or comparable — eliminates ink cost, saves ~$0.06/label, and removes the cut-and-tape step)
7. Apply labels, drop at USPS or schedule pickup

**Fulfillment time SLA:** Process time listed in Etsy: 3–5 business days. Actual target: ship within 2 business days of order. Beating the stated SLA consistently generates positive reviews and repeat purchases.

**Tracking:** Pirate Ship automatically generates USPS tracking numbers. Mark order as shipped in Etsy to trigger the automatic customer tracking email. Send a personal follow-up message using the shipping notification template within 1 hour of marking shipped.

---

## 5. Failure and Recovery

### 5.1 Common Print Failure Modes

**Bed adhesion loss** (most common at scale):
- Symptoms: Print lifts during run; spaghetti or partial part
- Causes: Contaminated PEI plate, inadequate first-layer squish, PEI plate degradation
- Prevention: IPA wipe before every plate; check Z-offset weekly; replace PEI plate every 300–500 prints
- Impact: Full plate loss — at 12-clip plates, this is 12 units. At $0.04 filament cost each, material loss is under $0.50; the real cost is 50 minutes of printer time.

**Snap arm brittleness** (highest consequence failure):
- Symptoms: Clip passes visual QC but snap arm snaps on first customer installation
- Causes: Under-extruded layers at the 1.4mm arm section; print speed too high on thin cross-section; nozzle temp too low; minimum layer time too short
- Prevention: Minimum layer time 8 seconds; nozzle at 222°C; 3+ walls; functional test on every plate catches this before it ships
- Impact: This is the warranty event. A snapped arm on arrival = negative review + replacement cost. Prevention ROI is high.

**Stringing across cable bore opening:**
- Symptoms: Thin filament bridges close the 65% bore gap
- Causes: Travel temperature too high; retraction not tuned
- Prevention: Standard P1S PLA+ profile handles this; verify retraction is enabled
- Rework: Remove strings with tweezers (15–20 sec per unit); viable rework

**Nozzle clog:**
- Symptoms: Missing layers, under-extrusion, suddenly thin prints
- Causes: Contaminated or moisture-damaged filament; burnt material in nozzle
- Prevention: Store filament sealed with desiccant; cold pull monthly if using the same nozzle; the P1S has a filament clog detector — verify it is enabled
- Impact: Can ruin a full plate if not caught early. The clog detector should catch this within 2–3 layers.

**Layer adhesion failure at Z-seam:**
- Symptoms: Visible crack or weak point at the seam line
- Causes: Z-seam placed at mechanically stressed location
- Prevention: In Bambu Studio, set Z-seam to "Back" — places it at the rear face of the clip, away from the snap arm

### 5.2 Failure Rate Assumptions

| Production stage | Expected failure rate | Units wasted/week at 20/wk |
|---|---|---|
| First 2 weeks (profile calibration) | 8–15% | 1.6–3 units |
| Mature production (PLA+, locked profile) | 3–5% | 0.6–1 unit |
| Catastrophic event (clog, power loss) | Full plate loss (rare) | 0–12 clips |

A 3–5% steady-state scrap rate is the production benchmark for a well-tuned FDM setup. At $0.10 average COGS per clip, 1 unit of scrap per week costs $0.10. For rails at $2.02 COGS, 1 wasted rail per month costs $2.02. Scrap is not a significant financial risk — it is a quality signal and a printer health indicator.

Do not accept a scrap rate above 8% for more than one week without diagnosing. Common causes: nozzle wear, moisture in filament, PEI plate degradation.

### 5.3 Reprint Workflow for Customer Replacements

When a customer reports a defect (broken snap arm, dimensional failure, shipping damage):

1. Respond within 2 hours: acknowledge, apologize briefly, confirm replacement is printing now
2. Print the replacement the same day — queue it ahead of the standard batch
3. Ship replacement First Class with tracking; communicate tracking immediately
4. Do not ask the customer to return the defective unit — the return shipping cost exceeds the $0.04–$2.02 COGS of the replacement part
5. If two or more customers report the same defect within the same week: stop the production run, pull the entire batch, and run a targeted functional test before shipping any more units from that filament lot or print profile

**Replacement shipping cost:** USPS First Class, ~$4.00–$5.50 per replacement. This is the true cost of a quality failure, not the $0.04 filament. Prevention ROI for the functional test gate is enormous.

### 5.4 Warranty and Satisfaction Guarantee

State in the Etsy listing: "30-day satisfaction guarantee. If your ModRun clip or rail breaks or doesn't fit as described, message me and I'll replace it free."

This framing converts a potential negative review into a direct message, giving you a chance to recover before the review is posted. PLA+ cable management accessories are low-stress mechanical items — the genuine claim rate at steady-state production should be under 1%.

Do not offer cash refunds as the first option. Offer replacement first. Most customers want the product to work, not their money back.

---

## 6. Six-Month Scaling Projection

### Months 1–2: Baseline and Optimization (Target: 20 units/week)

**Primary goal:** Validate the production profile, establish QC discipline, collect first reviews.

**Week 1–2:** Print in batches of 5–12 clips plus 1–2 rails. Validate Gate 3 functional test on every plate. Log every scrap event. Expected scrap rate: 8–12% while dialing in the profile.

**Week 3–4:** Profile should be locked. Scrap rate drops to 3–6%. Shift to overnight clip runs. Begin stocking 1–2 weeks of finished clip inventory. Rails remain print-to-order.

**Week 5–8:** Target 20 units/week steady state. Establish the weekly rhythm: Sunday queue, Mon/Wed/Fri overnight clip runs, daily rail prints. Monthly revenue target: $1,800–$2,500 gross, ~$1,200–$1,500 net.

**Key metrics to track:**
- Scrap rate by week (target: trending toward 3% by week 8)
- Printer utilization (hours/week; target: 12–16 hrs/week at 20 units)
- Order-to-ship time (target: consistently under 3 business days)
- Review velocity (target: 5+ reviews by end of Month 2)

### Months 3–4: Volume Push (Target: 50 units/week)

**Primary goal:** Test the limits of single-printer capacity without buying hardware.

**Scaling tactics:**
- Increase to daily print sessions rather than 3×/week
- Queue overnight clip runs 4–5 nights/week
- Optimize plate configurations toward maximum utilization
- Begin ordering filament in 10kg bundles ($11–13/kg vs. $15–17 per-spool)
- Implement noissue branded packaging (improves review quality)

**Printer utilization at 50 units/week:** approximately 35 hours/week. The printer runs near-continuously, roughly 5 hours/day. This is manageable but leaves no buffer for maintenance. Schedule a weekly printer maintenance window: clean nozzle, inspect PEI plate, re-run bed calibration.

**End of Month 4 decision point:** If demand is consistently above 40 units/week and you have a backorder queue, order the second P1S. Payback at 50 units/week: 3–5 weeks. Monthly revenue at 50 units/week: ~$5,000–$6,200 gross.

### Months 5–6: Infrastructure for 100+/week

**Primary goal:** Two-printer operation, parallel workflow, contractor-readiness.

**Two-printer operating model:**
- Printer 1: dedicated to clips; overnight runs, 3–4 nights/week
- Printer 2: dedicated to rails and custom/PETG orders during the day
- Two printers at 12-clip plates = 24 clips per 50-minute cycle = ~290 clips/16-hour production day
- This is the ceiling for a solo operator handling fulfillment; above 100 units/week, packaging and shipping admin exceeds 3 hours/day and a part-time contractor is warranted

**Contractor calculus:** A 10-hour/week packaging helper at $15/hour costs $600/month. At 100 units/week gross revenue of ~$10,000–$12,500/month, that is a 4.8–6% labor overhead — acceptable. The contractor handles: harvest-to-bin, packaging, label application, and USPS drop. You handle: print queue, QC, Etsy communications, and printer maintenance.

**Infrastructure investments by Month 6:**
- Thermal label printer ($180): reduces per-label cost and eliminates cut-and-tape labor
- Postal scale ($25): catches overweight packages before surcharges hit
- Second PEI plate per printer ($20 each): allows immediate plate swap on completion without waiting for cooling
- Bambu Farm Manager (free): centralized job dispatch across both printers

**Month 6 target state:**
- 100+ units/week throughput
- Two printers running on a scheduled print calendar
- Branded packaging (noissue or EcoEnclose) active
- 25+ Etsy reviews with 4.8+ average rating
- Monthly gross revenue: $10,000–$12,500
- Monthly net: $6,500–$8,000 (after COGS, fees, shipping, contractor)

---

## Immediate Next Steps (Post-Test-Print)

1. Run the test print. Note: snap arm flex, clip-in-rail fit, cable retention, any dimensional anomalies.
2. If FDM_TOLERANCE adjustment needed: change in CadQuery source, regenerate STL, label as v1.0, re-slice.
3. Save production slicer profile as `ModRun-PLA-Production-v1`. Do not modify it for production runs.
4. Print a validation batch of 12 clips (one full plate). Run all three QC gates.
5. If all three gates pass: you are in production. Set up the QC log. Queue the first sales batch.
6. Ship the first 3–5 orders. Measure order-to-ship time. Adjust the daily rhythm if needed.
7. After first 20 orders shipped: review QC log for patterns, review Etsy stats for conversion rate, adjust listing if conversion is under 2%.

---

*Sources: production-scaling-research.md, scaling-production-research.md, fulfillment-workflow.md, post-test-print-doc-4-first-week-operations-sop.md — all in `/projects/mfg-farm/`. Print time estimates based on Bambu P1S specification and volumetric flow constraints for PLA+ at 0.4mm nozzle / 0.20mm layer height. COGS verified against eSUN PLA+ at April 2026 Amazon pricing. USPS rates reflect the 8% temporary surcharge in effect through January 17, 2027.*
