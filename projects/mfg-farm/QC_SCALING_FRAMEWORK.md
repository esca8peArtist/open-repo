---
title: QC Scaling Framework — ModRun Cable Management Products
project: mfg-farm (ModRun / Etsy Print Farm)
created: 2026-05-21
status: production-ready
version: 1.0
scope: Single-printer QC through 8-printer farm — automated techniques, defect classification, sampling plans, industry benchmarks
related:
  - cost-model.md
  - ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md
  - MULTI_PRINTER_SCALING_ROADMAP.md
  - QC_LABOR_COST_MODEL.md
  - CUSTOMER_SATISFACTION_TARGETS.md
---

# QC Scaling Framework — ModRun Cable Management Products

**Lead finding**: A well-calibrated single-printer operation running PLA+ achieves a 3–5% defect rate on functional parts with a 60-second per-unit visual inspection. At 8 printers, you cannot inspect every unit without labor costs exceeding the value of defects caught. The correct architecture is a three-stage model: automated in-process monitoring (Stage 1, zero marginal cost), mandatory first-article inspection per production run (Stage 2, 30 minutes per run), and AQL-based statistical sampling on finished goods (Stage 3, scales logarithmically not linearly with volume). This framework keeps QC labor below $0.15/unit at every scale point.

---

## Part 1: Baseline — Failure Rate Reality for FDM Production

### 1.1 What the Industry Data Says

Published research on FDM failure rates spans a wide range because the category mixes uncalibrated hobbyists with optimized production operations:

- **Uncalibrated / beginner setups**: 20–41% failure rates (ResearchGate study on printer farm failure data; 26% attributable to human error alone)
- **Well-calibrated, single-material consumer FDM**: 3–7% functional failure (based on Prusa production data indicating 93–95% success rates on optimized machines)
- **ModRun target**: 3–5% scrap rate at calibration maturity (existing scaling-cost-model.csv assumption; 10–12% for the first two weeks of any new profile)
- **Production-grade SLS/industrial FDM**: under 2% failure — not achievable with desktop FDM at this scale point

The 3–5% benchmark from cost-model.csv is the correct planning figure. It is consistent with industry data for a disciplined, single-material PLA+ operation on an enclosed Bambu P1S. The 10–12% ramp figure for new profiles is also conservative and correct.

**Critical implication**: At 20 units/week (Phase 0), a 5% scrap rate means 1 bad unit per week. At 700 units/week (8 printers, Phase 3), it means 35 units per week — $140–175 in lost material at $4–5 material value per unit. The QC system must catch defects before they ship, not catch them in customer returns. The cost of a shipped defect is $8–15 (refund + replacement + labor) versus $0.40–0.60 (material scrap).

### 1.2 ModRun Defect Budget

Using cost-model.csv COGS assumptions:

| Stage | Defect Rate | Units/Week (8 printers) | Scrap Units/Week | Material Loss/Week |
|-------|-------------|------------------------|-------------------|--------------------|
| First 2 weeks of new profile | 10–12% | 700 | 70–84 | $28–34 |
| Calibrated production (mature) | 3–5% | 700 | 21–35 | $8–14 |
| Target after process lock | <3% | 700 | <21 | <$8 |

Budget $0.04/unit scrap allowance (from scaling-cost-model.csv) as a COGS line item. This equals $28/week at 700 units/week — consistent with the calibrated 3–5% range.

---

## Part 2: Defect Classification System

### 2.1 Three-Tier Severity Model

The industry standard for consumer product QC (ISO 2859-1 / ANSI Z1.4) uses a three-tier defect classification. This is adapted below specifically for cable management clips, hooks, wraps, and labels.

#### Critical Defects (Zero tolerance — unit must be scrapped, do not ship)

Critical defects create a functional failure or safety/return risk. Any single critical defect in a batch warrants tightening to 100% inspection for the remainder of that run.

| Defect | Description | Test Method | Root Cause |
|--------|-------------|-------------|------------|
| **Snap arm fracture** | Arm breaks or has visible crack under normal engagement force | Manual flex test: engage/release once | Over-extrusion, layer delamination, wrong orientation, thin arm |
| **Delamination** | Layer separation visible on load-bearing walls | Manual flex/pull test | Bed temp too low, moisture in filament, bad layer bonding |
| **Warping** (structural) | Base bows >1mm preventing flat adhesion to surface | Place on flat surface, check gap | Bed adhesion failure, no brim on large footprint |
| **Snap arm missing** | Under-extrusion caused arm to not form | Visual | Filament jam, extruder skip, clog |
| **Wrong geometry** | Part is obviously wrong shape/size | Visual comparison to reference | Profile mismatch, wrong 3MF queued |
| **Severe stringing** crossing channel | Strings block the cable channel making part non-functional | Visual + finger check of channel | Retraction miscalibrated |

#### Major Defects (Cause for rejection in statistical sampling; unit may be shipped only if no cosmetic-tier alternative exists)

Major defects do not make the part immediately non-functional but significantly reduce its value or expected lifespan.

| Defect | Description | Test Method | Root Cause |
|--------|-------------|-------------|------------|
| **Snap arm permanently deformed** | Arm bent from print bed warping but still engages | Visual, manual test | Warping during cooling |
| **Significant under-extrusion** | Visible gaps in walls >0.5mm wide | Visual | Partial clog, extruder tension |
| **Layer shift** | Visible X/Y shift in part body | Visual | Belt issue, vibration, print speed |
| **Dimensional deviation >0.2mm** on snap engagement feature | Clip either cannot engage or requires excessive force | Caliper check of snap arm width | Slicer profile error, filament shrinkage |
| **Elephant foot** >1mm | First layers splayed out significantly | Visual + caliper | Bed temp too high, first layer too close |
| **Stringing inside cable channel** (minor obstruction) | Thin strings crossing cable path | Visual | Retraction settings |

#### Minor Defects (Acceptable for sale; note in batch log; cosmetic only)

Minor defects are visible imperfections that do not affect function or customer expectation for a 3D-printed product. Etsy customers buying from a "handmade/3D-printed" shop have different expectations than buyers of injection-molded products — minor surface texture variation is part of the product category's identity, not a defect to apologize for.

| Defect | Description | Threshold | Root Cause |
|--------|-------------|-----------|------------|
| **Layer lines visible** | Normal FDM texture on outer surfaces | Always acceptable | Normal FDM characteristic |
| **Light stringing** (not in channel) | Fine hairs on non-functional surfaces | Acceptable if <5mm strings | Retraction settings |
| **Minor color variation** between batches | Slightly different shade of black/white | Acceptable unless noticeable in same order | Filament lot difference |
| **Slight surface zitting** | Small bumps on outer surfaces | Acceptable if <1mm | Pressure advance settings |
| **Seam line** | Visible start/stop seam on outer wall | Always acceptable | Normal FDM characteristic |
| **Brim residue** | Small nub from removed brim | Acceptable if flush within 0.5mm | Brim removal |

### 2.2 Product-Specific Defect Priority by SKU

Different products have different failure modes. The snap arm is the critical feature for clips; it is absent on hooks and labels.

| Product | Critical Failure Mode | Second-Most-Critical | Minor is Acceptable |
|---------|----------------------|----------------------|---------------------|
| **Cable clip** (snap arm) | Snap arm fracture or missing | Snap arm dimensional deviation >0.2mm | Layer lines, light stringing |
| **Headphone hook** | Wall delamination, hook curve deformed | Stringing in hook curve | Surface texture |
| **Cable wrap / velcro tab** | Delamination, tab too thin | Dimensional deviation making fit too loose | Color variation |
| **Cable labels** | Text unreadable, hole too small for cable pass-through | Warping preventing flat stick | Surface texture |
| **Desk rail / mount** | Delamination on load-bearing wall, screw hole misaligned | Elephant foot >1.5mm | Layer lines |

---

## Part 3: Three-Stage QC Architecture

### 3.1 Stage 1 — In-Process Monitoring (Automated, Zero Marginal Labor Cost)

Stage 1 catches defects while they are forming, before the print completes. This is the highest-leverage intervention point because catching a failure at layer 10 saves 90% of the filament and 90% of the print time.

**Tool: SimplyPrint AI Failure Detection**

SimplyPrint's AI detects spaghetti printing (extruder depositing into air), warping (part lifting from bed), and blobbing (over-extrusion creating blob events) via webcam analysis. It sends alerts and can automatically pause/cancel prints. Detection typically occurs within 60–90 seconds of failure onset. Cost: $10/month for up to 10 printers.

Setup requirements:
- Webcam positioned to see the full build plate (Bambu P1S has built-in camera — this satisfies the requirement)
- SimplyPrint connected in LAN mode to each printer
- Alert routing: push notification to phone + optional auto-cancel on "spaghetti" events

**Bambu P1S First-Layer Inspection (Built-in)**

The P1S uses Micro Lidar scanning during the first layer to detect adhesion failures and alignment issues. It does not replace visual inspection but provides an automated checkpoint at the most critical print stage (first 2–5 minutes). Known limitation: it does not reliably detect partial first-layer failures. Use it as a supplement, not a replacement, for first-article inspection.

**Implementation cost**: $0 additional hardware (P1S camera + SimplyPrint Starter). $10/month software for 2+ printers.

**What Stage 1 catches**: Catastrophic failures (spaghetti, full detachment, major warping). It does not catch dimensional deviations, minor stringing, or part-level defects that develop after the first few layers.

**Stage 1 target**: Catch 70–80% of catastrophic failures before print completion. This reduces material waste by an estimated 60–70% compared to discovering failures post-print.

### 3.2 Stage 2 — First-Article Inspection (Per Production Run)

Stage 2 is mandatory before releasing any production run. It consumes 20–30 minutes at the start of each new color batch or profile change and catches systematic errors that Stage 1 misses.

**First-Article Protocol (30-minute checklist)**:

1. Print 1 unit at the start of any new color or profile change
2. Allow cooling (5 minutes minimum for PLA+ — do not inspect a hot print)
3. Inspect against the following checklist:

| Check | Method | Pass Criterion | Fail Action |
|-------|--------|----------------|-------------|
| **Surface finish** | Visual — check all sides | No stringing across channel, no major zitting | Adjust retraction/temp, reprint |
| **Layer adhesion** | Bend test — flex part 10° at thickest cross-section | No cracking sound, no visible delamination | Check filament moisture, bed temp |
| **Snap arm integrity** | Engage/release snap arm 3× | No cracking, arm returns to neutral position | Check arm geometry in slicer, adjust orientation |
| **Snap arm engagement force** | Qualitative — should engage with one finger, not two | Not too tight (requires palm pressure) or too loose (falls off) | Adjust tolerance in CAD ±0.05mm |
| **Snap arm dimensions** (caliper) | Caliper check at arm base width and height | Within ±0.1mm of target spec | Re-slice with corrected flow rate |
| **Cable channel width** | Caliper check | Within ±0.2mm of target | Adjust profile, reprint |
| **Base flatness** | Place on flat surface | Rocks <0.5mm | Check warping, bed adhesion |
| **Dimensional overall** | Caliper: length, width, height | All within ±0.3mm | Profile correction |

**First-article result routing**:
- All pass: Release production run, log lot number and result
- 1–2 minor issues: Note, adjust for next run, release current run with heightened Stage 3 sampling
- Any critical failure: Hold run, diagnose, do not release until corrected first article passes

**Frequency**: Once per color change, once per profile change, once per new filament lot. Not once per individual print.

**Labor cost**: 20–30 minutes per production run. At 2 runs/day per printer (color batching), this is 40–60 minutes of QC time per printer per day — a significant but fixed cost regardless of how many units are in the batch.

### 3.3 Stage 3 — Statistical Sampling of Finished Goods (AQL-Based)

Stage 3 is where the scaling efficiency comes from. You do not inspect every unit at 8 printers. You use statistical sampling to detect systematic problems with high confidence.

**Standard Used: ISO 2859-1 / ANSI Z1.4, General Inspection Level II**

This is the global standard for acceptance sampling, used by consumer electronics manufacturers, toy companies, and every major importer. It gives you a statistically defensible sampling rate keyed to lot size.

**ModRun AQL Levels by Defect Class**:
- Critical defects: AQL 0.65 (zero tolerance — any critical defect in sample = reject batch)
- Major defects: AQL 2.5 (≤2.5% major defects acceptable per lot)
- Minor defects: AQL 4.0 (cosmetic issues — higher tolerance is appropriate)

**Lot Size Definition for ModRun**: A "lot" is one production run on one printer in one color. Typical lot size at calibration maturity: 20–50 units per color per printer per day.

**AQL Sampling Table (ISO 2859-1, General Inspection Level II)**:

| Lot Size | Code Letter | Sample Size | AQL 0.65 (Critical) Ac/Re | AQL 2.5 (Major) Ac/Re | AQL 4.0 (Minor) Ac/Re |
|----------|-------------|-------------|----------------------------|------------------------|------------------------|
| 2–8 | A | 2 | 0/1 | 0/1 | 0/1 |
| 9–15 | B | 3 | 0/1 | 0/1 | 0/1 |
| 16–25 | C | 5 | 0/1 | 0/1 | 0/1 |
| 26–50 | D | 8 | 0/1 | 0/1 | 0/1 |
| 51–90 | E | 13 | 0/1 | 1/2 | 1/2 |
| 91–150 | F | 20 | 0/1 | 1/2 | 2/3 |
| 151–280 | G | 32 | 0/1 | 2/3 | 3/4 |
| 281–500 | H | 50 | 0/1 | 3/4 | 5/6 |
| 501–1,200 | J | 80 | 1/2 | 5/6 | 7/8 |

Ac = accept if this many or fewer defects found; Re = reject if this many or more defects found.

**Practical Application by Scale Point**:

1 printer, 20 units/day lot: Code C, 5 units sampled. Pull 5 units from each daily run, inspect. At 20 units/day that is 25% sampling — high, but you only have 5 units to check. Time cost: 5 minutes.

2 printers, 40 units/day per printer: Code D/E, 8–13 units sampled. Pull from each printer's daily output. Total: 16–26 units inspected across both printers. Time cost: 10–15 minutes.

4 printers, 50 units/day per printer: Code D/E, 8–13 units per printer lot. Total: 32–52 units across 4 printers. Time cost: 20–30 minutes.

8 printers, 50 units/day per printer: Code D/E, 8–13 units per printer lot. Total: 64–104 units across 8 printers. Sampling rate at this scale: 16–26%. Time cost: 40–60 minutes.

**Critical observation**: Sampling volume scales much more slowly than production volume. Going from 1 to 8 printers (8× production) increases Stage 3 inspection time by only 8× in absolute units — but because sampling is logarithmic with lot size, you can actually batch across printers and reduce total inspection time when lots from the same profile/color run are aggregated.

**Cross-printer lot aggregation (advanced)**: If all 8 printers are running the same profile and color in the same batch, you can treat the full day's output as one lot (400 units). Code H, sample size 50. Total: 50 units inspected instead of 104. This is a 50% reduction in Stage 3 labor and is statistically valid under ISO 2859-1 when production conditions are identical.

---

## Part 4: Automation Without Expensive Hardware

### 4.1 Weight Sampling (Budget: $10–25 for a kitchen scale)

**What it catches**: Significant under-extrusion (part printed with missing walls/infill), accidental duplicate prints of wrong-size clips, catastrophic material voids.

**Protocol**: Weigh 1 unit from each lot. Record baseline weight per SKU on first good production run. Acceptable range: ±10% of baseline.

- Cable clip (0.5"): baseline ~2g. Acceptable: 1.8–2.2g.
- Cable clip (0.75"): baseline ~3g. Acceptable: 2.7–3.3g.
- Headphone hook: baseline ~8–10g. Acceptable: 7.2–11g.

**Cost**: $10–25 one-time (OXO kitchen scale accurate to 1g). Adequate for clips and hooks; not precise enough for dimensional QC.

**Limitation**: Weight sampling does not catch dimensional deviations within specification range (a clip that weighs correctly but has a snap arm tolerance deviation), stringing, or warping. It is a fast triage tool, not a dimensional check.

**Recommendation**: Use weight sampling as a rapid first pass on sampled units. Units that fail weight check get full caliper inspection. Units that pass weight check still get snap arm functional test.

### 4.2 Digital Calipers (Budget: $20–50)

**What it catches**: Snap arm dimensional deviation, channel width errors, overall part geometry.

**Protocol**: Three-point caliper check per sampled unit:
1. Snap arm base width (critical dimension)
2. Cable channel internal width
3. Overall part length (detects layer shift)

Each measurement takes 20 seconds. Three measurements per unit: 60 seconds per unit.

**Recommended tool**: iGaging IP54 Electronic Digital Caliper ($25–35, Amazon). Resolution 0.01mm, sufficient for ±0.1mm tolerance checking. Full IP54 splash rating not required but helpful in dusty print environments.

**When to use**: On every unit in Stage 2 (first-article) and on critical-dimension checks within Stage 3 sampling. Not required on every sampled unit for Stage 3 minor-defect checking — visual inspection is sufficient for most minor defects.

### 4.3 Functional Snap Test (No Equipment Required)

**What it catches**: Critical snap arm failures — the most important defect class.

**Protocol**: Engage and release the snap arm on a reference cable mock-up (a 3.5mm zip tie or similar diameter rod works). One engage-release cycle. Check:
- Did the arm spring back to neutral position?
- Did it make any cracking sound?
- Does it hold the cable mock-up without slipping?

**Time**: 10 seconds per unit. This is the single most important QC check for cable clips and should be done on every sampled unit. It directly tests the critical defect category.

**Reference cable mock-up**: Print a calibration gauge rod at 3.5mm diameter (5-minute print, PLA). Use this as the functional test fixture. Re-print if damaged.

### 4.4 Visual Inspection (No Equipment Required)

**What it catches**: Stringing (including channel-blocking strings), layer shift, delamination, elephant foot, surface zitting.

**Protocol**: 30-second visual check under consistent lighting. Rotate part through all six faces. Check cable channel with fingertip for obstruction.

**Lighting requirement**: A single bright LED desk lamp ($20–30) positioned at 45 degrees catches stringing that overhead lighting misses. At scale, position a dedicated lamp at the QC bench. Consistent lighting is essential — visual inspection in dim conditions misses minor defects consistently.

### 4.5 What NOT to Buy at Phase 0–2

These tools are commonly recommended for QC in professional manufacturing but do not add value at ModRun's scale through 8 printers:

**3D scanner ($150–500)**: Dimensional verification beyond calipers. Not needed — caliper three-point checking catches all dimensional defects that matter for cable clips. A 3D scanner would catch micro-deviations in geometry that have no effect on function or customer satisfaction.

**CT scanner or X-ray ($3,000+)**: Internal void detection. Absolutely not applicable to consumer cable clips. Internal voids that do not cause surface-level delamination are acceptable in gyroid infill parts.

**CMM (Coordinate Measurement Machine)**: Industrial-grade dimensional verification. Only relevant for aerospace or medical parts. Overkill by 3 orders of magnitude for PLA cable clips.

**Automated vision system ($500–5,000)**: Camera-based automated inspection. Only cost-justified above 2,000–3,000 units/day. At 700 units/week (Phase 3), manual sampling remains cheaper than the system's capital cost amortized over useful life.

---

## Part 5: Sampling Plans by Scale Point

### 5.1 1 Printer — 20 Units/Week (Phase 0)

**Inspection regime**: 100% functional inspection of every unit. At 20 units/week, the time cost is manageable and you are still validating your production profile.

**Protocol per unit** (60 seconds):
- 10 sec: Weight check (kitchen scale)
- 10 sec: Visual — channel clear, no major stringing, no delamination
- 10 sec: Functional snap test
- 30 sec: Caliper check on every 5th unit (snap arm width, channel width)

**Total QC time**: 20 minutes/week at 60 seconds per unit. This is acceptable and recommended during the validation phase.

**Trigger to move to sampling**: Once you have 100 consecutive units with zero critical defects and <3% major defects (3 or fewer in 100), you have established process capability. Move to sampling at the 100-unit milestone.

### 5.2 2 Printers — 50 Units/Week (Phase 1)

**Inspection regime**: AQL sampling, Code D/E. 8–13 units per 26–50-unit lot per printer.

**Protocol**:
- Pull 10 units from each printer's daily output (random, not first/last)
- Full 60-second inspection per sampled unit (weight + visual + snap test)
- Caliper check on 3 of the 10 units (snap arm and channel width)
- Record results in batch log (see log template below)

**Total QC time**: 20 minutes/day for both printers combined. ~140 minutes/week. About 2.5 hours.

**Escalation rule**: If any sampled unit has a critical defect, immediately inspect all remaining units from that printer's current lot. Identify root cause before next run.

### 5.3 4 Printers — 100–150 Units/Week (Phase 2)

**Inspection regime**: AQL sampling, Code E/F. 13–20 units per lot per printer. With color batching, treat all printers running the same profile/color as one lot.

**Protocol**:
- Morning batch (all printers, one color): treat as single lot. Sample 20 units from combined output.
- Afternoon batch (second color): sample 13–20 units from combined output.
- Caliper check: 5 units per session (snap arm + channel).
- Total sampled per day: ~40 units from combined output of 4 printers.

**Sampling rate**: 40 units inspected / ~200 units produced = 20%. This is higher than necessary by AQL standards but appropriate for Phase 2 when the multi-printer fleet is still accumulating calibration history.

**Total QC time**: 45–60 minutes/day. About 5–7 hours/week.

### 5.4 8 Printers — 700 Units/Week (Phase 3)

**Inspection regime**: Cross-printer lot aggregation. If all 8 printers run the same profile/color in the same batch window, treat the full session output as one lot.

**Example**: 8 printers × 50 units/day per printer = 400 units/day. Treat as one lot (Code H, sample size 50). Pull 50 random units for inspection.

**Sampling rate**: 50/400 = 12.5%. This is statistically valid for AQL 2.5 on a 400-unit lot.

**Protocol**:
- Pull 50 random units from the combined output of the daily run
- Full 60-second inspection: weight + visual + snap test
- Caliper check on 15 of the 50 units
- Record pass/fail with printer ID on each failed unit (to identify printer-level drift)

**Total QC time**: 70–90 minutes/day for 50 units. About 8–10 hours/week.

**Key insight**: QC time at 8 printers (8–10 hours/week) is only 4× the QC time at 1 printer (2 hours/week) despite producing 35× more units. This is the efficiency gain from statistical sampling versus 100% inspection.

**Failure root cause tracking**: When Stage 3 sampling catches defects, record which printer produced them. Over 4 weeks, if any printer produces >2× the defect rate of the fleet average, that printer needs maintenance (nozzle swap, bed recalibration, belt tension check) before the next production run.

---

## Part 6: Batch Log Template

Every production run should be logged. This is the data source for printer-level drift detection.

```
Date: ___________
Printer ID: P1 / P2 / P3 / P4 / P5 / P6 / P7 / P8
Filament lot: ___________  Color: ___________
Profile version: ___________
Units in lot: ___________

First-Article Results:
  Surface finish: PASS / FAIL (notes: _______)
  Snap arm functional: PASS / FAIL
  Snap arm dimension: ___mm (spec: ___mm)
  Channel width: ___mm (spec: ___mm)
  Overall length: ___mm (spec: ___mm)
  First-article decision: RELEASE / HOLD / ADJUST

Stage 3 Sampling (if applicable):
  Sample size: ___
  Critical defects found: ___  (fail if >0)
  Major defects found: ___  (AQL 2.5 Ac/Re: ___)
  Minor defects found: ___  (AQL 4.0 Ac/Re: ___)
  Batch decision: ACCEPT / REJECT / TIGHTEN NEXT RUN

Notes: ___________________________
Logged by: ___________________________
```

This log need not be digital at Phase 0–1. A paper logbook per printer is sufficient and faster. Move to a shared Google Sheet at Phase 2 when printer-level cross-comparison becomes useful.

---

## Part 7: Industry Benchmarks and Where ModRun Positions

### 7.1 Reference Standards for Consumer 3D-Printed Products

There is no ISO standard specifically for consumer 3D-printed products equivalent to injection-molding standards like ISO 9001 or ASTM D3935. The relevant standards for positioning are:

**ISO 2859-1 (Sampling Procedures for Inspection by Attributes)**: The AQL framework used in this document. Industry-standard for consumer goods inspection worldwide. Adopting this standard allows ModRun to represent its QC process in professional terms to wholesale buyers or B2B customers in Phase 3+.

**ASTM F2792 / ISO 17296**: Additive manufacturing terminology standards — not directly applicable to QC process but useful for technical descriptions in product listings.

**Consumer Product Safety Improvement Act (CPSIA)**: Applicable to children's products. Cable clips are not children's products; CPSIA does not apply unless ModRun enters toy/nursery product categories.

### 7.2 Competitive Positioning

Etsy sellers of 3D-printed cable management products fall into three quality tiers:

**Tier 1 — Hobbyist/uncalibrated (most Etsy competition)**: No defined QC process. Ships anything that comes off the printer. Review scores 3.5–4.3 stars. Return rate estimated 5–8% based on low-rating complaint patterns visible in reviews. Defect rate shipped to customers: unknown but observable from "snap arm broke on first use" review language.

**Tier 2 — Process-aware (minority of Etsy competition)**: Visual inspection every unit, functional test before shipping. Review scores 4.5–4.8 stars. Return rate estimated 2–4%.

**Tier 3 — Production-grade QC (rare on Etsy; more common on Amazon)**: AQL sampling, documented inspection protocols, first-article testing. Review scores 4.8–5.0 stars. Return rate estimated 0.5–2%.

**ModRun target**: Tier 3 process rigor from Phase 0 onward, while Phase 0 output volume (~20 units/week) allows 100% inspection at negligible extra cost. The operational investment in logging and first-article inspection at Phase 0 builds the process discipline that scales to Phase 3 without workflow changes — only the sampling rate changes.

### 7.3 Etsy Quality Expectations and Platform Standards

The Etsy Star Seller program requires:
- 4.8 average rating or above over the trailing 3-month window (updated July 2025 from the prior 95% five-star requirement)
- Case rate below Etsy's minimum service level standard (Etsy does not publish the exact number, but sellers report that 1–2 cases per 100 orders is the boundary)
- On-time shipping: 95%+ of orders shipped within stated processing time

**What this means for QC**: A single critical defect shipped to a customer creates a case. At 5 orders/week (Phase 0), one case in a week is a 20% case rate — catastrophic for Star Seller status. QC's first job is case prevention, not scrap reduction.

The economic calculus: a single case costs $8–15 (replacement + labor). At 20 units/week, preventing 1 case per month by inspecting every unit (2 hours/week, $30 labor) yields a $15 return on $120 monthly labor investment. The ROI on 100% inspection at Phase 0 is negative — but the platform metrics impact makes it worthwhile regardless of direct economics.

### 7.4 Real-World Precedents from 3D Printing Sellers

Published seller practices are sparse — most Etsy sellers do not document their QC processes publicly. The following is derived from forum observations (Reddit /r/3Dprinting, /r/EtsySellers, Bambu Lab community forums) and print farm operator discussions:

**Common practice among Etsy 3D print sellers (2024–2025)**:
- Most sellers at <50 units/week perform 100% visual inspection but no functional testing
- Snap fit failure is the most common complaint in 3D-printed products reviews
- Sellers who ship pre-tested (functional snap test) have measurably fewer negative reviews on snap-mechanism products
- Few sellers use weight sampling or calipers — this represents a genuine competitive advantage that ModRun can claim in product descriptions ("each clip snap-tested before shipping")

**What differentiates high-rated sellers**:
- First-article testing per color batch (prevents systematic run failures from shipping)
- Functional test of the snap mechanism (not just visual)
- Packaging that prevents shipping damage (layer separation from impact is distinct from printing defect)

---

## Part 8: Integration Points

### 8.1 Link to cost-model.md

The scaling-cost-model.csv includes a scrap allowance of $0.04/unit in COGS. This figure assumes 3–5% scrap at calibrated production — consistent with Stage 2 (first-article) preventing batch failures and Stage 3 (sampling) catching systematic drift before it scales.

At Phase 0 (1 printer, 20 units/week), the actual scrap cost is higher per unit because the printer is still in profile calibration (10–12% first-week scrap assumed in scaling-cost-model.csv). The $0.04/unit figure is a mature-state target.

**QC labor is not currently a separate COGS line in cost-model.md.** The labor row in cost-model.csv ($0.62/unit at 20 units/week) includes post-processing, packaging, and shipping prep. QC labor should be tracked separately in QC_LABOR_COST_MODEL.md and periodically reconciled against the master cost model. At Phase 0–1, QC labor is absorbed into owner time at opportunity cost.

### 8.2 Link to ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md

Section 6 (Contingency Plans) in the launch checklist identifies "snap arm too tight in production batches" as Risk 3, with the fix "calibrate printer before each print batch, adjust CAD tolerance -0.05mm per batch." This framework supersedes that response:

- The correct fix for a systematic snap arm tolerance issue is a Stage 2 first-article catch, not mid-run adjustment
- Adjusting CAD tolerance mid-batch risks making already-printed units in-batch incompatible with new units
- The Stage 2 protocol detects this at the start of each color batch and gates release on caliper confirmation

Also relevant: the launch checklist states "each clip tested for minimum 500 snap cycles before shipping" in the product description template. This is aspirational marketing language, not the actual QC protocol. The actual protocol is one snap test per sampled unit at Stage 3. Adjust the listing description to "each clip snap-tested before shipping" — accurate and verifiable.

### 8.3 Link to MULTI_PRINTER_SCALING_ROADMAP.md

Section 1.5 of the scaling roadmap describes a three-stage QC model (pre-print calibration, first-article, batch sampling at 1-in-50). This framework extends that model with:
- Specific defect classification criteria (critical/major/minor per SKU)
- AQL table with exact sample sizes and accept/reject numbers
- Explicit protocol per scale point
- Batch log template
- Stage 1 (SimplyPrint AI) automation detail

The 1-in-50 random pull described in the scaling roadmap corresponds to a 2% sampling rate. For lots under 90 units, ISO 2859-1 Level II requires more than 2% — typically 8–20 units regardless of lot size for lots under 90 units. The roadmap's "1-in-50" heuristic is appropriate only for lots of 500+ units. For Phase 0–1 (lots of 20–50 units), use the AQL table in this document.

---

## Sources

- [QIMA — AQL Acceptable Quality Limit Overview and Tables](https://www.qima.com/aql-acceptable-quality-limit)
- [QCAdvisor — AQL Table and Defect Classification](https://www.qcadvisor.com/blog/acceptable-quality-limit/)
- [ISO 2859-1:1999 — Sampling Procedures for Inspection by Attributes](https://www.iso.org/obp/ui/#iso:std:iso:2859:-1:ed-2:v1:en)
- [3D-Printed.org — What Is the Failure Rate of 3D Printing? (2025 Edition)](https://www.3d-printed.org/what-is-the-failure-rate-of-3d-printing/)
- [SigmaFilament — Filament for Print Farms: Failure Rate Reduction Guide](https://sigmafilament.com/filament-for-print-farms-guide/)
- [Nota3D — Quality Control in 3D Printed Manufacturing (2025)](https://nota3d.com/2025/02/07/quality-control-in-3d-printed-manufacturing/)
- [SimplyPrint — AI Failure Detection Feature Documentation](https://simplyprint.io/features/ai-detection)
- [SimplyPrint — AI Failure Detection Helpdesk Article](https://help.simplyprint.io/en/article/the-simplyprint-ai-failure-detection-feature-1blpac7/)
- [Unionfab — Guide to 3D Printed Snap Fits (2025)](https://www.unionfab.com/blog/2025/06/3d-print-snap-fit)
- [Etsy Seller Handbook — How to Get 5-Star Reviews](https://www.etsy.com/seller-handbook/article/476775452989)
- [CraftyBase — How to Become an Etsy Star Seller in 2026](https://craftybase.com/blog/how-to-become-etsy-star-seller)
- [Etsy Help — How the Review System Works for Sellers](https://help.etsy.com/hc/en-us/articles/360000572708-How-the-Review-System-Works-for-Sellers)
- [Etsy Help — Service Level Standards](https://help.etsy.com/hc/en-us/articles/360000345068-Service-Level-Standards)
- [Hackaday — Oh Snap! 3D Printing Snapping Parts Without Breakage](https://hackaday.com/2022/11/11/oh-snap-3d-printing-snapping-parts-without-breakage/)
- [LayerMath — 3D Print Farm: Real Costs, Pricing and Profit Models (2026)](https://layermath.com/blog/how-to-run-a-3d-print-farm)
- mfg-farm/scaling-cost-model.csv — per-unit COGS including scrap allowance
- mfg-farm/MULTI_PRINTER_SCALING_ROADMAP.md — three-stage QC model baseline
- mfg-farm/8-printer-farm-cost-model.md — labor structure at scale
- mfg-farm/ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md — launch-week risk scenarios
