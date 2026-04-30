---
title: ModRun Production Scaling & Automation — Comprehensive Manufacturing Playbook
date: 2026-04-30
status: active
tags: [mfg-farm, modrun, production, scaling, automation, cost-model, 3d-printing, fdm]
confidence: high
related: material-sourcing-supplier-economics.md, multi-printer-architecture.md, workforce-scaling-research.md, pricing-strategy.md
---

# ModRun Production Scaling & Automation

**Lead finding:** At the 1-printer, 1–20 units/week stage, print time is not the binding constraint — post-processing discipline and batch plate utilization are. The single highest-leverage action before scaling to a second printer is filling every build plate to capacity (8–12 clips or 1–2 rails per plate) and eliminating single-unit print runs. At 20 units/week with one Bambu P1S, the operation is profitable, manageable solo, and requires no new hardware. The decision to add a second printer triggers around week 8–12 if demand consistently exceeds 30 units/week for two consecutive weeks. Labor for post-processing becomes the bottleneck above 50 units/week, not print speed.

---

## Section 1: Additive Manufacturing Best Practices for Batch Production

### 1.1 Print Queue Optimization

The fundamental principle for a small FDM farm is **plate saturation before print launch**. Every print job that occupies a printer at less than 80% build volume utilization is a missed efficiency opportunity. For ModRun products:

**ModRun Clips (modrun_clip_b123d.py):** The clip body is small — approximately 14mm tall, 10mm deep, and (bore + 4mm wall) wide. The 6mm-bore variant is roughly 16mm × 10mm × 14mm. On a Bambu P1S 256mm × 256mm bed, you can comfortably fit **12–16 clips per plate** in a grid arrangement with 5mm spacing, all printing simultaneously. This is the target plate configuration: never print fewer than 8 clips per plate unless you are printing a custom bore-diameter prototype for testing.

**ModRun Rails (modrun_rail_b123d.py):** At 200mm length × 24mm depth × ~50mm total height (with clamp arm), rails are large parts. The desk_clamp variant will occupy roughly 200mm × 52mm × 50mm of build volume. You can print **1 rail per plate** with ample room for a few accessory clips alongside it (4–6 clips plus 1 rail = strong plate utilization). The adhesive variant is shorter in Z (~22mm total) and can be printed 2 per plate if oriented lengthwise.

**Sequential vs. parallel batching:** For small clips, parallel batching (all on one plate simultaneously) is almost always better than sequential one-at-a-time printing. Sequential mode (printing one part fully before the next) is only useful for extremely tall parts with a small footprint where inter-part contamination from a failure would be costly, or when you want to isolate a test variant from the main batch.

**Queue workflow:** Build a print queue 24–48 hours ahead. For a standard week at 20 units, that means pre-slicing 2–3 plate configurations (12-clip plate, 8-clip plate, 1-rail + 4-clip plate) and saving them as named profiles in Bambu Studio. Do not re-slice from scratch every day — version-lock your production slicing profiles.

### 1.2 File Management and Version Control

Establish a three-tier directory structure from day one:

```
/modrun-production/
  /cadquery/          -- Source .py files (version-controlled in git)
  /stl/
    /v1.0/            -- First production-validated STLs (post test print)
    /v1.1/            -- Any tolerance-adjusted variants
    /test-prints/     -- Experimental variants, never mixed with production
  /sliced/
    /bambu-profiles/  -- .3mf project files per plate configuration
    /production/      -- Current active plate .3mf files
    /archive/         -- Superseded plate configs
```

**Naming convention:** `modrun_clip_6mm_v1.0_12up_0.20mm_20pct.3mf` — encodes product, variant, version, units per plate, layer height, and infill. This eliminates "which file was that last good print?" failures entirely.

**Version discipline:** When the test print reveals a tolerance adjustment (highly likely — FDM_TOLERANCE may need to change from the current 0.15mm default), increment the STL version before any production run. Never overwrite v1.0. The CadQuery source files make regeneration trivial: change SNAP_ARM_THICKNESS or FDM_TOLERANCE, re-run the script, re-export STL, re-slice, save as new version.

### 1.3 Batch Sizing Strategy

| Batch size | Use case | Tradeoffs |
|---|---|---|
| 1 unit | Test print only | Never use in production — printer utilization is wasted |
| 5 units | Early validation (week 1–2 after test print passes) | Acceptable for validating full production profile; not efficient long-term |
| 12–16 clips or 1–2 rails | Standard production batch (20–50 units/week) | Optimal for single P1S; balances plate utilization with manageable harvest |
| 24–32 clips | High-volume batch (50+ units/week) | Requires longer print job but reduces restarts; good for overnight runs |

**Recommendation:** Standard production batch is 12 clips per plate for clips, 1 rail + 4 clips per plate for rails. This maximizes throughput without over-complicating the harvest workflow.

### 1.4 Print Settings Consistency

Lock down a production profile and do not deviate from it for production runs. The following settings are validated as appropriate for ModRun's use case (PLA+, snap-fit cable management accessories):

| Parameter | Recommended Setting | Rationale |
|---|---|---|
| Layer height | 0.20mm | Balances dimensional accuracy with print speed; 0.15mm adds 25–30% time with marginal quality gain for this use case |
| Infill density | 20–25% | Sufficient for non-load-bearing cable management; 15% risks brittleness in snap arm; 30%+ adds unnecessary print time and material |
| Infill pattern | Gyroid or Lightning | Gyroid provides isotropic strength (good for snap arm); Lightning saves material if gyroid is too slow |
| Perimeters/walls | 3 | Provides sufficient wall strength for snap arm integrity; do not reduce below 3 |
| Top/bottom layers | 4 | Prevents top-surface voids |
| Print speed | 250–300mm/s outer wall; 500mm/s infill | Bambu P1S default "Quality" profile is appropriate |
| Bed temp (PLA+) | 55°C | Standard; no adjustment needed unless first layer adhesion issues |
| Nozzle temp (PLA+) | 220–225°C | Run slightly hotter than PLA to improve layer adhesion on snap arm |
| Support | None required | Both clip and rail are designed for support-free printing in their default orientations |
| Bed adhesion | PEI plate, no glue needed | Clean PEI plate with IPA before each plate; skip this and you will have first-layer failures |

**Temperature consistency:** Use the same PLA+ brand per production run. Switching brands mid-batch is acceptable if you verify the temperature profile matches — different brands have different glass transition characteristics. eSUN PLA+ and Overture PLA+ perform identically at 220–225°C on the P1S.

### 1.5 Layer Height and Infill — ModRun Specific

The snap arm in modrun_clip_b123d.py is the most mechanically demanding feature: a 1.4mm-thick cantilever (SNAP_ARM_THICKNESS) that deflects during installation and must return to shape. Layer adhesion strength on this arm is directly proportional to nozzle temperature (higher temp = better layer fusion) and inversely proportional to print speed on that feature.

**For the snap arm specifically:** The Bambu P1S will automatically reduce speed when printing small cross-sections due to its minimum layer time setting. Ensure minimum layer time is set to at least 5 seconds. This prevents the nozzle from depositing hot plastic on top of still-soft plastic, which causes snap arm deformation and brittleness.

**Infill below 20% is not recommended** for the snap arm region. If you must reduce material use, apply variable infill (20% in snap arm region, 15% in cable bore region) — this is achievable in Bambu Studio via modifier meshes, though it adds slicing complexity. The simpler approach: 20% uniform infill for all production units.

### 1.6 Post-Processing Workflow

**For clips (no required post-processing):** ModRun clips are designed for support-free printing. Standard workflow is: remove plate from printer, flex plate to release parts, inspect, sort pass/fail, bag. Target: under 60 seconds per plate of 12 clips.

**For rails (minimal post-processing):** Rails print without supports in default orientation. The clamp variant may have minor stringing or artifacts in the slot openings. A quick pass with a deburring tool or craft knife on the slot entries is a 10–15 second operation per rail. No sanding needed for functional use.

**If surface finish is a customer requirement (future premium SKU):** XTC-3D epoxy coating adds 8–12 minutes per part but creates a near-injection-molded surface. Not recommended at launch — adds cost and complexity. Better path is to refine the print settings to get a clean surface than to add a finishing step.

**Per-unit post-processing time estimates:**
- Clip, standard (no finishing): 3–5 seconds (remove, inspect, bin)
- Rail, standard (slot deburring): 20–30 seconds per rail
- Clip, light sanding (optional premium): 3–5 minutes (not recommended at launch)

### 1.7 Quality Control Checkpoints

Build a **go/no-go gate** at harvest, not before shipping. The goal is to catch failures immediately after printing, before they enter the finished goods bin.

**Checkpoint 1 — Visual inspection at harvest (5 seconds per part):**
- First layer fully adhered (no warping or lifting at corners)
- Snap arm present and not deformed or broken
- Cable bore opening gap present (not fused shut)
- No obvious stringing bridging the snap arm

**Checkpoint 2 — Dimensional spot check (1 per 20 units, ~30 seconds):**
- Snap arm width within ±0.3mm of design (7.6mm for SNAP_ARM_WIDTH)
- Clip slot entry width within ±0.3mm (should accept rail slot freely)
- Use digital calipers; cost $15–25 for adequate accuracy

**Checkpoint 3 — Functional test (1 per batch run, i.e., ~1 per plate):**
- Press clip into rail slot: should seat with a tactile click
- Press test cable (appropriate bore size) into clip: should retain without falling out
- This is the critical test for SNAP_NUB_HEIGHT and SNAP_ARM_THICKNESS correctness

**Checkpoint 4 — Stress test (1 per new filament batch):**
- Remove and reinsert clip 5 times in the rail: snap arm should not show cracking or deformation
- Flex snap arm manually to 50% deflection: should return to position without permanent set

**Scrap rate targets:** Aim for under 5% at production scale with a well-tuned profile. Early production (first 1–2 weeks) may run 8–12% until the profile is dialed. Any plate with more than 2 failed units (out of 12) should trigger a printer inspection before the next run.

---

## Section 2: Turnaround Time Modeling

### 2.1 Print Duration Per Unit

All estimates assume Bambu P1S, 0.4mm nozzle, 0.20mm layer height, PLA+, 20–25% infill, 3 walls, "Quality" preset.

**modrun_clip_b123d.py — 6mm bore variant (most common SKU):**
- Part dimensions: approximately 16mm W × 10mm D × 14mm H + snap arm (~8mm extension)
- Estimated print volume: ~2.5–3.5 cm³ (~3–4g per clip at 1.24 g/cm³ PLA+ density)
- Print time per single clip (solo): ~10–15 minutes
- Print time for 12 clips per plate (parallel): ~35–50 minutes
- Effective time per clip at 12-up batching: ~3–4 minutes

**modrun_clip_b123d.py — 12mm bore variant (thicker cables):**
- Larger body (bore + 4mm wall = ~20mm W)
- Print time for 12-up plate: ~50–65 minutes
- Effective time per clip: ~4–5 minutes

**modrun_rail_b123d.py — desk_clamp variant:**
- Part dimensions: 200mm L × ~52mm H × 24mm D
- Estimated print volume: ~60–75 cm³ (~75–95g)
- Print time: 2.5–3.5 hours per rail (single unit per plate)
- At 1 rail + 4 clips per plate: 2.5–3.5 hours total, producing 1 rail + 4 clips

**modrun_rail_b123d.py — adhesive variant:**
- Lower Z height (~22mm total), faster print
- Print time: 1.5–2.5 hours
- At 2 adhesive rails per plate: 1.5–2.5 hours, producing 2 rails

**Key implication:** Clips are high-velocity items (35–50 clips/printer/day at 16hr production); rails are slow (5–7 rails/printer/day). If customer demand skews toward rails, a second printer is needed sooner than if demand skews clips.

### 2.2 Cooling and Removal Time

- Plate removal: 2–3 minutes cooling after job completes (PEI plate; flex to release when cooled to 40–45°C)
- Parts removal from plate: 30–60 seconds for a 12-clip plate; 30 seconds for a single rail
- Plate re-prep (IPA wipe): 60–90 seconds
- Total turnaround between plate runs: **4–6 minutes** (negligible relative to print time)

On a 16-hour production day, this dead time totals approximately 60–90 minutes across 10–12 print cycles — reducing effective production time to 14.5–15 hours. This is already factored into the throughput estimates above.

### 2.3 Post-Processing Time Per Unit

| Part | Support removal | Deburring/finishing | Inspection | Total per unit |
|---|---|---|---|---|
| Clip (standard) | None | None | 5 sec | ~5–8 sec |
| Rail (standard) | None | 20–30 sec slot deburring | 15 sec | ~40–50 sec |
| Clip (premium sanded) | None | 3–5 min | 15 sec | ~3.5–5.5 min |
| Rail (premium coated) | None | 8–12 min XTC-3D coating | 30 sec | ~9–13 min |

**At launch, target zero finishing on clips and 30-second deburring on rails. Premium finishing is a future SKU, not a launch requirement.**

### 2.4 Assembly, Packaging, and Shipping Prep

| Task | Time per unit | Notes |
|---|---|---|
| Bundle assembly (3-clip bundle) | 30–45 sec | Bag clips together in zip-lock insert |
| Package in poly mailer | 45–60 sec | Mailer, padding if required, seal |
| Label application | 15–20 sec | Pre-printed via Pirate Ship batch or label printer |
| Batch shipping upload | 5–10 min per day | One daily batch submission; amortizes to 3–5 sec per unit at 50+/day |

**Total packaging + labeling time per order:** 90–120 seconds for a 3-clip bundle order. At $15/hour labor, this is $0.38–$0.50 per order in post-processing labor.

### 2.5 Total Throughput by Volume Level

| Throughput | Print time/week | Post-processing/week | Packaging/week | Total active hours | Feasibility |
|---|---|---|---|---|---|
| 1 unit/week | ~45 min | ~2 min | ~2 min | ~1 hr | Trivially solo |
| 5 units/week | ~4 hr | ~10 min | ~10 min | ~4.5 hr | Solo, weekend-only viable |
| 20 units/week | ~14 hr | ~40 min | ~40 min | ~15.5 hr | Solo, 2–3 hr/day, manageable |
| 50 units/week | ~35 hr | ~1.5 hr | ~1.5 hr | ~38 hr | Approaches 1-printer capacity; near full-time printing |
| 100 units/week | ~70 hr | ~3 hr | ~3 hr | ~76 hr | Requires 2nd printer; solo still manageable post-processing |

*Assumes 60% clips / 40% rails by revenue mix; clips at 40min effective per plate of 12, rails at 3hr per plate of 1.*

### 2.6 Bottleneck Identification

At 1–20 units/week: **No real bottleneck.** Print time is ample; packaging is trivial.

At 20–50 units/week: **Print time is the binding constraint** — one printer cannot keep pace without near-continuous operation. The printer runs ~14–35 hours/week. Below 50, still single-person-manageable without automation.

At 50–100 units/week: **Print time requires 2nd printer or 16-hour daily operation.** Post-processing (30–40 sec/rail) becomes the secondary constraint. If rail demand is high, post-processing takes 1.5–3 hours/week — manageable solo but beginning to demand schedule discipline.

Above 100 units/week: **2nd printer is essential.** Post-processing labor becomes the daily scheduling challenge. This is the contractor hire trigger point: a local 1099 helper for 10 hours/week at $15/hour covers all packaging and post-processing at 100–150 units/week.

### 2.7 Scaling Inflection Points

- **Add 2nd printer when:** Single printer runs at 80%+ utilization for 2 consecutive weeks AND backorders are accumulating. Typical trigger at 30–40 units/week sustained demand. Cost: $699–$799 for a P1S.
- **Add 3rd printer when:** 2-printer fleet consistently runs 16 hrs/day AND demand exceeds 80 units/week. Expected timeline: Month 8–12 if growth trajectory holds.
- **Hire post-processing contractor when:** Packaging + post-processing exceeds 3 hours/day consistently (roughly 100+ units/week). Cost: $15–18/hour, 10–15 hours/week = $600–$1,080/month. Break-even: when labor cost is less than the lost sales from capacity constraints.

---

## Section 3: Supplier Sourcing Strategy

*(This section builds on and extends `material-sourcing-supplier-economics.md` with packaging, shipping, and component sourcing not covered in that document.)*

### 3.1 Filament Supplier Comparison

Five production-viable suppliers for PLA+ at 2026 pricing:

| Supplier | $/kg retail | $/kg at 10kg | $/kg at 50kg | AMS compat. | Tariff risk | Notes |
|---|---|---|---|---|---|---|
| **eSUN (Amazon Prime)** | $15–17 | $11–13 (10kg bundle) | ~$10 (estimate, direct) | Excellent | Moderate (Chinese) | Default launch supplier; Prime shipping is the key advantage |
| **Overture (Amazon)** | $14–18 | $11–14 (multi-pack) | Contact required | Good | Moderate (Chinese) | Up to 35% wholesale discount; strong community reliability data |
| **Polymaker** | $16–19 | $14.99 (wholesale) | $12–14 (estimate) | Excellent | Moderate (Chinese) | Vacuum packaging; best moisture protection; $1,000 MOQ for wholesale |
| **Anycubic** | $14–16 | $10.49 (50kg deal) | $10.49 | Good (not validated for AMS) | Moderate (Chinese) | Best $/kg publicly available; AMS compatibility requires verification |
| **Push Plastic** | $20–26 | $18–22 | $15–18 (subscription) | Moderate | Low (US-made) | Domestic tariff hedge; 20–35% premium over Chinese suppliers |

**Volume pricing reality:** At 1–20 units/week, monthly filament consumption is under 5kg. Buy eSUN PLA+ via Amazon Prime, no bulk order needed. At 20–50 units/week, transition to 10kg bundle orders. At 50+ units/week, Anycubic 50kg deal becomes the best $/kg option. See `material-sourcing-supplier-economics.md` Section 3 for full decision tree.

**Material alternatives for ModRun:**

| Material | Print success rate | Heat deflection | Cost vs. PLA+ | ModRun verdict |
|---|---|---|---|---|
| Standard PLA | 92–95% | 50–55°C | −$1–2/kg | Do not use — deformation risk near active electronics |
| **PLA+ (recommended)** | **92–95%** | **55–60°C** | **Baseline** | **Default production material** |
| PETG | 77–91% | 70–75°C | +$2–6/kg | Premium SKU only; justify +$2–4 retail premium |
| TPU | 60–80% | Variable | +$5–15/kg | Not appropriate — clips don't need flexibility |
| Nylon | 70–80% | 80–90°C | +$8–20/kg | Not appropriate — hygroscopic, difficult to print |

### 3.2 Packaging Suppliers

**Option A: Generic poly mailers (launch default)**
- Source: Amazon, ULINE
- Cost: $0.05–$0.10 per mailer (100-pack $6–10)
- Pros: cheapest, ships same day
- Cons: no eco-story, no branding
- Best for: First 50–100 orders while you validate the product

**Option B: EcoEnclose custom-printed mailers (growth phase)**
- Cost: ~$0.15–$0.25/unit at 500-unit minimum custom print
- Eco claim: 100% recycled/responsibly sourced material; Etsy official partner
- Minimum order: 500 units for custom printing
- Lead time: 2–3 weeks for first run
- Verdict: Strong Etsy aesthetic alignment; invest in custom EcoEnclose mailers when order volume hits 200+/month

**Option C: noissue custom packaging**
- Cost: ~$0.20–$0.35/unit for custom mailers at 100-unit minimum
- Lower MOQ than EcoEnclose, compostable options available
- Good for test of branded packaging before committing to 500-unit EcoEnclose run
- Verdict: Use noissue for a branded packaging pilot at 50–100 order scale

**For rails (larger form factor):**
- Rigid mailers or small corrugated boxes are needed for 200mm rails
- EcoEnclose corrugated boxes: ~$0.40–$0.60 per box at 250-unit minimum
- Generic small boxes (Amazon): ~$0.15–$0.25 each
- Rails should ship in a box with minimal crumple packing; the part is robust but the clamp arm is a stress point

### 3.3 Shipping Logistics

Use **Pirate Ship** as the default shipping platform — it provides USPS commercial rates (below retail) with no monthly fee, batch label printing, and easy Etsy order import.

**Per-unit shipping cost estimates (Pirate Ship commercial rates, 2026):**

| Order type | Weight | USPS service | Cost range | Notes |
|---|---|---|---|---|
| 1 clip, poly mailer | ~50g total | First Class Package | $3.50–$4.50 | Most common Etsy single-unit order |
| 3-clip bundle, poly mailer | ~120g total | First Class Package | $4.00–$5.50 | Bundle pricing unlocks better per-unit economics |
| 1 rail, small box | ~150–200g total | First Class Package | $4.50–$6.00 | Rail is dense; packaging adds significant weight |
| Multi-unit order (5+ clips) | 250–500g | Ground Advantage | $5.00–$7.00 | Zone-dependent; cross-country adds $1–2 |

*Note: USPS implemented an 8% temporary rate increase effective April 26, 2026, through January 17, 2027. These estimates reflect current elevated rates.*

**Amazon FBA shipping for rails/clips (future channel):**
Amazon FBA for a sub-1lb standard-size item: $3.06–$4.25 fulfillment fee + 15% referral fee (home & kitchen category). On a $24.99 item, Amazon takes approximately $7–8 in total fees (28–32%). Combined with COGS, FBA margins are lower than Etsy but volume potential is higher. FBA makes sense when you are shipping 50+ units/week and cannot manage individual Etsy orders at that volume.

### 3.4 Component Sourcing

**Zip-lock bags (for bundling clips):** Amazon, $0.01–$0.03 each at 500-pack. Essential for presenting multiple clips as a bundle without them rattling loose.

**Labels:** Use Pirate Ship shipping labels (integrated label printing, thermal labels, no ink cost). For product labels/thank-you cards: Canva-designed 4×6" cards printed at Vistaprint, ~$0.05–$0.10/unit at 500-unit run. Optional at launch but high-value for reviews solicitation.

**Rubber bumper pads (for desk clamp rail):** Small 3M rubber bumper pads ($5–8 for a pack of 100) protect desk edges from clamp scratch. Consider including 4 pads with each rail — adds $0.20–$0.32 COGS but meaningfully reduces "scratched my desk" reviews.

**Lead times:**
- Filament (Amazon Prime): 1–2 days
- Filament (direct supplier bulk): 7–21 days
- Custom mailers (EcoEnclose/noissue): 14–21 days first order
- Corrugated boxes (Amazon bulk): 2–5 days
- Component hardware (Amazon): 1–3 days

---

## Section 4: Cost Structure Modeling at Scale

### 4.1 Unit Cost Build-Up

All estimates use PLA+ at $12/kg (10kg bulk rate), Bambu P1S ($699 printer cost, 5,000-hour depreciation life), and $15/hour labor. Shipping is excluded from COGS and handled as a pass-through at Etsy (customer-paid) or netted against revenue at Amazon.

**Clip (6mm bore, 3g print weight, ~35-min print time at 12-up batching):**

| COGS Component | Low | Mid | High | Assumptions |
|---|---|---|---|---|
| Filament (3g at $12/kg) | $0.03 | $0.04 | $0.05 | Waste + support negligible for clips |
| Electricity ($0.025/hr × 35min ÷ 12) | $0.001 | $0.001 | $0.002 | Negligible |
| Printer depreciation ($0.14/hr × 35min ÷ 12) | $0.007 | $0.007 | $0.007 | Negligible per unit at 12-up |
| Scrap allowance (5% buffer) | $0.002 | $0.002 | $0.003 | 5% at mature production |
| Post-processing labor (5 sec @ $15/hr) | $0.02 | $0.02 | $0.02 | Harvest + inspect only |
| Packaging (poly mailer ÷ 3 clips) | $0.02 | $0.03 | $0.05 | Share across bundle |
| **COGS per clip (before shipping)** | **$0.08** | **$0.10** | **$0.13** | |

**Rail (desk_clamp variant, 85g, 3-hr print time, 1 per plate):**

| COGS Component | Low | Mid | High |
|---|---|---|---|
| Filament (85g at $12/kg) | $0.90 | $1.02 | $1.20 |
| Electricity ($0.025/hr × 3hr) | $0.075 | $0.075 | $0.090 |
| Printer depreciation ($0.14/hr × 3hr) | $0.42 | $0.42 | $0.42 |
| Scrap allowance (5%) | $0.05 | $0.06 | $0.08 |
| Post-processing labor (45 sec @ $15/hr) | $0.19 | $0.19 | $0.19 |
| Packaging (small box) | $0.15 | $0.25 | $0.40 |
| **COGS per rail (before shipping)** | **$1.79** | **$2.02** | **$2.38** |

**Critical observation:** Material cost for clips is almost negligible — $0.04/clip. The real cost drivers at clip scale are **packaging** and **labor for packaging/shipping admin**. For rails, printer depreciation is the dominant COGS item ($0.42), followed by filament ($1.02). Both products have exceptional raw material efficiency.

### 4.2 Full COGS Including Shipping and Platform Fees

**Scenario: 3-clip bundle on Etsy at $24.99**

| Component | Cost |
|---|---|
| Clip COGS × 3 | $0.30 |
| Packaging (poly mailer + bag + thank-you card) | $0.20 |
| Shipping (USPS First Class, 120g, zone 4 avg.) | $4.50 |
| Etsy transaction fee (6.5% of $24.99) | $1.62 |
| Etsy listing fee ($0.20, amortized over 100 sales) | $0.002 |
| Etsy payment processing (~3% + $0.25) | $1.00 |
| **Total cost per order** | **$7.62** |
| **Revenue** | **$24.99** |
| **Gross profit** | **$17.37** |
| **Gross margin** | **69.5%** |

**Scenario: Rail (desk_clamp) on Etsy at $34.99**

| Component | Cost |
|---|---|
| Rail COGS | $2.02 |
| Packaging (small box + padding) | $0.35 |
| Shipping (USPS First Class, 200g) | $5.50 |
| Etsy transaction fee (6.5%) | $2.27 |
| Etsy payment processing | $1.30 |
| **Total cost per order** | **$11.44** |
| **Revenue** | **$34.99** |
| **Gross profit** | **$23.55** |
| **Gross margin** | **67.3%** |

### 4.3 Margin Analysis at Production Scale

See `cost-model-spreadsheet.csv` for full throughput-level modeling. Summary:

| Weekly throughput | Gross margin (blended) | Key constraint |
|---|---|---|
| 1/week | 55–62% | High per-unit overhead; single unit shipping kills economics |
| 5/week | 62–67% | Improving with bundle discipline |
| 20/week | 67–70% | Optimal for solo operation; approaching mature margin |
| 50/week | 68–71% | Printer running near-full utilization; no new costs yet |
| 100/week | 65–68% | 2nd printer depreciation added; contractor labor emerging |

*Margins compress slightly at 100/week due to 2nd printer depreciation and labor. They recover and exceed at 150+/week when the 2nd printer is fully amortized.*

### 4.4 Break-Even Analysis

**Initial investment:**
- Bambu P1S: $699–$799
- Starting filament (3 spools × $20): $60
- Packaging supplies (100 mailers, 50 boxes, bags): $40
- Pirate Ship (free), Etsy shop ($0.20/listing)
- **Total startup capital: ~$800–$950**

**Monthly fixed costs at launch:**
- Printer depreciation: ~$28/month ($699 ÷ 25 months, assuming 16 hrs/day, 5,000-hr life)
- Etsy shop maintenance: $0 (no subscription)
- Filament (20 units/week × 52g avg × $12/kg × 4.3 weeks): ~$54/month
- Packaging: ~$20/month at 20 units/week

**Monthly revenue at 20 units/week (blended clips and rails):**
- Assume 60% clips (12/week × $24.99 bundle of 3), 40% rails (8/week × $34.99)
- Clip revenue: 12 × $24.99 × 4.3 = $1,290/month
- Rail revenue: 8 × $34.99 × 4.3 = $1,204/month
- Total: ~$2,494/month gross

**Monthly profit at 20 units/week:**
- Revenue: $2,494
- COGS (material + packaging + depreciation): ~$400
- Shipping: ~$450
- Etsy fees (6.5% + payment): ~$375
- Net profit: ~$1,269/month

**Break-even on startup capital:** $950 ÷ $1,269/month ≈ **0.75 months** — startup capital is recovered in the first month of 20-unit/week production. This is an exceptionally fast payback for a manufacturing operation.

### 4.5 Scaling Inflection Points

**Trigger 1: Add 2nd printer (~$700 investment)**
- When: 30–40 units/week sustained demand
- Payback: 3–5 weeks at full utilization
- Effect: Doubles clip capacity to 70–80 clips/day; enables 50+ units/week throughput

**Trigger 2: Hire post-processing contractor (10 hrs/week, $15/hr = $600/month)**
- When: Post-processing + packaging exceeds 3 hours/day AND order volume is 100+ units/week
- Revenue at that volume: ~$8,000–12,000/month
- Labor as % of revenue: 5–7.5% — acceptable

**Trigger 3: Amazon FBA onboarding**
- When: Etsy order volume is reliable 50+ units/week AND you want diversification
- Preparation: Order FBA labels, ship inventory in bulk; transition 20–30% of production to FBA channel
- FBA reduces per-order labor to near-zero (Amazon handles fulfillment) at cost of ~12% additional fee load

---

## Section 5: Automation Opportunities

### 5.1 Print Queue Software

**Bambu Farm Manager (free):** The official Bambu Lab tool for managing multiple P1S/X1 printers. Supports real-time status display, batch job dispatch, firmware updates, and multi-user management. Available via the Bambu Studio desktop app. This is the zero-cost starting point for fleet management — use it from day 1 of the second printer.

**Printago (free tier):** A third-party commercial OS for 3D print farms. Works with OrcaSlicer and Bambu Studio; can route jobs to printers with matching materials automatically. Free tier supports unlimited printer connections but limits concurrent job processing (paid tiers add multiple simultaneous job routing). For a 1–3 printer operation, the free tier is sufficient. Printago also integrates with inventory tracking — tracking filament consumption per job is available at paid tiers.

**FDM Monster (open-source, free):** Server-based farm management with OctoPrint, Klipper, and Bambu LAN mode support. More complex to set up than Printago but fully free and self-hosted. Appropriate once the farm grows to 5+ printers and you want granular data logging without a SaaS subscription.

**OctoPrint with Bambu plugin:** An unofficial OctoPrint plugin exists for Bambu printers (jneilliii/OctoPrint-BambuPrinter on GitHub). Integration is partial — Bambu's closed ecosystem makes full OctoPrint support incomplete as of 2026. Do not rely on this as a primary management tool; use Bambu Farm Manager instead.

**Recommendation by stage:**
- 1–2 printers: Bambu Farm Manager (free), manual queue management
- 3–5 printers: Add Printago free tier for automated job routing
- 5+ printers: Evaluate Printago paid tier or FDM Monster for full production tracking

### 5.2 Batch Labeling and Tracking

**Shipping label printing:** Pirate Ship supports CSV import from Etsy order exports — batch-print an entire day's shipping labels in under 2 minutes. Combined with a thermal label printer (Rollo X1038, ~$180; or Zebra LP2844, ~$150 refurbished), the per-label cost drops to ~$0.04 vs. $0.08–$0.12 for inkjet labels.

**Inventory and job tracking (lightweight):** A simple Google Sheet or Notion database tracking `[Date] [Plate config] [Units produced] [Pass/Fail count] [Filament lot] [Printer]` takes 30 seconds per plate run to update and provides the data needed to track scrap rates by printer, by filament brand, and over time. This is the minimum viable QC log — do not rely on memory.

**Barcode generation:** At 50+ SKUs, generate barcodes for each variant using Canva (free) or Barcode Generator (free online). Print on Avery labels. Etsy does not require barcodes, but Amazon requires FNSKU barcodes for FBA — generate these free through Amazon Seller Central.

### 5.3 Post-Processing Automation

**Vibratory tumbler for surface finishing (if required):**
- Entry-level vibratory tumbler: $50–$80 (Harbor Freight when on sale)
- Industrial mini vibratory (Inovatec, similar): $200–$500
- Effective for: removing minor burrs, smoothing layer lines on clips
- Cycle time: 2–6 hours for smooth finish, unattended
- Capacity: 50–200 small clips per run
- ROI trigger: Only worthwhile if you sell a "premium smooth finish" SKU at $3–5 above standard. At standard FDM quality, tumbling is not needed for ModRun clips.

**Ultrasonic cleaner for support removal:** Not applicable — ModRun designs are support-free. Ultrasonic cleaning is relevant for resin prints; skip this for PLA/PETG FDM.

**Automated plate removal:** The Bambu P1S PEI plate self-releases when cooled to ~40°C by natural convection. No mechanical automation needed. Do not interrupt the cooling cycle — premature removal causes plate warping.

### 5.4 Packaging Workflow Automation

**Poly mailer sealer ($30–$80):** A heat impulse sealer creates a proper seal on poly mailers in 2 seconds vs. self-adhesive strip (3–5 sec). ROI is minimal for under 100 orders/day; use self-adhesive mailers at this scale.

**Label printer (as above):** Thermal label printer ($150–$180) pays back in ink savings within 3–6 months at 50+ labels/week. Also eliminates the "print, cut, tape" workflow — a meaningful ergonomic improvement for daily use.

**Weight verification scale ($20–$40):** A postal scale at the packing station serves two purposes: (1) catch overweight packages before they trigger USPS surcharges, and (2) use weight as a quality proxy — a missing clip or a failed print that somehow passed visual inspection will be detectably underweight if you know your target weight.

### 5.5 Inventory Management

**Filament stock:** Track by color and brand. Maintain a simple reorder trigger: when any color drops below 1 full spool (1kg), place an order. At 20 units/week, a single spool of PLA+ lasts approximately 2–3 weeks. Safety stock: 2–3 spools of primary color (black or grey for ModRun's expected SKU mix).

**Finished goods inventory:** For a print-on-demand operation, keep 1–2 weeks of finished stock on hand. Etsy buyers expect 3–5 day processing time; 1 week of stock provides buffer for printer downtime or a demand spike. At 20 units/week, this is 20–40 units in the finished goods bin — trivially small.

**Etsy/Amazon inventory sync:** Etsy does not have a native inventory auto-sync for physical goods. Use a free tool like Vela or EtsyHunt to monitor active listing quantity. Manually update inventory counts weekly — takes under 5 minutes. As volume grows, consider Shopify with Etsy integration (Shopify $29/month) for centralized inventory across channels.

### 5.6 Automation ROI Analysis

| Automation | Cost | Monthly savings | Payback |
|---|---|---|---|
| Pirate Ship (free) | $0 | $30–$50/month vs. retail USPS | Immediate |
| Thermal label printer | $150–$180 | $15–$25/month in ink at 50+ labels/week | 6–12 months |
| Bambu Farm Manager (free) | $0 | ~1–2 hr/week recovered | Immediate |
| Printago (free tier) | $0 | Job routing automation at 2+ printers | Immediate |
| Google Sheet QC log (free) | $0 | Enables failure prevention; hard to quantify | Immediate |
| Postal scale ($30) | $30 | Prevents surcharge errors; ~$5–10/month | 3–6 months |
| Vibratory tumbler ($80) | $80 | Only if selling premium-finish SKU (+$3–5/unit) | 10–30 units at premium |
| Poly mailer heat sealer ($50) | $50 | Marginal time savings; primarily ergonomic | Not recommended pre-100 orders/day |

**Within-6-month ROI automations:** Pirate Ship (immediate), Bambu Farm Manager (immediate), Printago free tier (immediate), postal scale (3–6 months). All of these cost nothing or under $40.

**1-year ROI automations:** Thermal label printer at $150–$180 investment pays back within 6–12 months at 50+ labels/week.

**Do not pursue within year 1:** Automated plate removal hardware, commercial-grade vibratory tumblers ($2,000+), or warehouse management software. These are appropriate at 500+ units/week.

---

## Section 6: Failure Mode Prevention and Quality Control

### 6.1 Common FDM Failure Modes

**Bed adhesion loss (most common at scale):**
- Symptom: Print lifts from bed during print; partial part or spaghetti pile
- Cause: Contaminated PEI plate, inadequate first layer squish, print started too fast, PEI degradation
- Prevention: IPA wipe before every plate; check Z-offset calibration weekly; replace PEI plate when adhesion degrades (every 300–500 prints approximately)
- Scrap impact: Full plate loss; estimated 1–2× per 50 plate runs at a well-maintained printer

**Stringing between parts:**
- Symptom: Thin filament threads connecting clip bodies across a plate
- Cause: Travel moves at too-high temperature; retraction settings not tuned
- Prevention: Ensure retraction is enabled; PLA+ typically prints well at 220°C without stringing on P1S default profiles
- Scrap impact: Minor; stringing is cosmetic and usually removable by hand. Does not cause scrap unless it bridges the cable bore.

**Warping (rare with PLA+ on PEI):**
- Symptom: Corners lifting during print; dimensional error in final part
- Cause: Ambient temperature fluctuation, draft from HVAC, inadequate bed temp
- Prevention: Keep print room above 18°C; avoid cold drafts; P1S enclosure largely eliminates this for PLA+
- Scrap impact: Low for PLA+ on enclosed printer

**Layer adhesion failure (snap arm specific):**
- Symptom: Snap arm snaps on first installation rather than flexing
- Cause: Under-extruded layers, print speed too high on thin section, cold nozzle, low infill
- Prevention: Ensure minimum layer time ≥5 seconds; nozzle temp 220–225°C for PLA+; 3 walls minimum; never reduce below 20% infill
- Scrap impact: Medium — these parts pass visual inspection but fail functional test. Critical to catch at functional checkpoint (1 per batch)

**Nozzle clog:**
- Symptom: Missing layer sections, under-extrusion, suddenly thin prints
- Cause: Contaminated or moisture-damaged filament, printing too cold, burnt material in nozzle
- Prevention: Store filament sealed with desiccant; replace nozzle at Bambu's recommended interval (every 1–2 kg of PLA); cold pull to clear partial clogs
- Scrap impact: Variable — can ruin a full 12-clip plate if not caught early. The P1S has a filament clog detector; enable this feature.

### 6.2 ModRun-Specific Risk Profile

Based on the geometry in both CAD files:

**Snap arm brittleness (modrun_clip_b123d.py):** The 1.4mm SNAP_ARM_THICKNESS is thin. If printed with poor layer adhesion (cold nozzle, too-fast print, under-extrusion), the arm will snap rather than flex. This is the single highest-risk feature in the design. The BORE_GAP_RATIO of 0.65 means the cable opening is 65% of bore diameter — if the gap closes (stringing across the opening), the clip becomes non-functional. These two features must be in every functional test.

**Slot dimensional tolerance (both parts):** FDM_TOLERANCE is set to 0.15mm in both files. If the test print reveals that clips bind or rattle in rail slots, adjust FDM_TOLERANCE before any production run. A 0.05mm change (to 0.20mm or 0.10mm) can mean the difference between a click-fit and a rattle-loose joint. This is why the test print is a prerequisite to all production.

**Rail clamp arm stress (modrun_rail_b123d.py):** The C-clamp arm (CLAMP_ARM_THICKNESS = 4mm) is robust, but the corner junction between the clamp back and lower jaw is a stress concentration point. If a customer applies excessive clamping torque, this joint may crack. Print orientation matters: the layer lines should run perpendicular to the anticipated stress direction (vertical, for the default print orientation). Do not print rails on their side.

**Adhesive base variant — pocket depth risk:** The ADHESIVE_PAD_DEPTH of 1.5mm creates thin pockets. If printed slightly under-extruded, the floor of the pocket may be incomplete, reducing adhesive contact area. Inspect adhesive base rails carefully — push a fingernail across each pocket floor to verify integrity.

### 6.3 Scrap Rate Estimation

Based on industry data (FDM print farm benchmarks, Sovol3D production guide, 3DPrintOps cost analysis):

| Production stage | Expected scrap rate | At 20 units/week | At 100 units/week |
|---|---|---|---|
| First 2 weeks (profile calibration) | 8–15% | 1.6–3 units/week | N/A |
| Mature production (PLA+, well-tuned) | 3–6% | 0.6–1.2 units/week | 3–6 units/week |
| Mature production (PETG) | 8–14% | 1.6–2.8 units/week | 8–14 units/week |
| Catastrophic event (clog, power loss) | 100% of affected plate | 0–12 clips lost | 0–24 clips lost |

*Note: Research indicates hobbyist FDM failure rates can run as high as 41% (including human error), but a dedicated production operation with locked print profiles and regular maintenance should achieve 3–6% at steady state.*

**Scrap cost at 5% rate, 20 units/week:** ~1 unit/week wasted. At $0.10 COGS/clip, this is under $0.10/week — negligible. At rail scale (20 rails/week at $2.02 COGS): $2.00/week in scrap — still very low.

### 6.4 Rework vs. Scrap Decision Criteria

| Failure type | Rework viable? | Decision |
|---|---|---|
| Stringing across cable bore | Yes | Remove with tweezers or heat gun brief pass; 30 sec rework |
| Snap arm snapped (single arm) | No | Scrap — structural failure, cannot be repaired |
| Partial layer adhesion (cosmetic only) | Conditional | If functional test passes, sell as Grade B or scrap; do not ship structural failures |
| Dimensional oversize (clips don't fit rail) | No | Scrap — rework with heat would destroy part; adjust tolerance and reprint |
| First layer texture issue (functional, ugly) | Conditional | If snap test passes and bore is functional, sell at discount or in bundles |
| Support artifact inside snap slot | Yes | Deburr with craft knife; 15 sec rework |

**Rework rule:** Only rework if the repair takes under 2 minutes and does not compromise the functional snap-fit. PLA+ cannot be welded or adhesive-repaired in a way that restores structural integrity at the snap arm. If in doubt, scrap it — at $0.04–$0.10 COGS per clip, the marginal cost of scrapping is trivial compared to a customer review about a broken clip.

### 6.5 Quality Log and Failure Prevention

Maintain a simple quality log from day one. Minimum viable log (Google Sheet):

| Date | Printer | Plate config | Units attempted | Pass | Fail | Failure mode | Filament lot | Notes |
|---|---|---|---|---|---|---|---|---|

Review this log weekly. Patterns to watch for:
- Failure rate increasing on specific printer → maintenance trigger
- Failures clustering on specific filament lot → lot quality issue; contact supplier
- Snap arm failures increasing → check nozzle temperature and minimum layer time
- Bed adhesion failures increasing → replace/resurface PEI plate

**Failure playbook (post on shop wall):** Write a one-page reference for the 5 most common failures with their immediate response actions. This prevents guesswork during a production run and enables a contractor to maintain quality without constant supervision.

---

## Assumptions and Confidence Notes

**High confidence (grounded in live pricing and CAD geometry):**
- Filament cost per unit (eSUN/Overture at $12/kg, verified April 2026 pricing)
- Printer depreciation rate ($0.14/hr at $699 P1S, 5,000-hr life)
- Etsy fee structure (6.5% transaction + 3% payment processing)
- USPS 8% temporary surcharge in effect through January 2027
- Print geometry and mass estimates derived directly from modrun_clip_b123d.py and modrun_rail_b123d.py constants
- Scrap rate 3–6% for mature PLA+ production (industry benchmarks)

**Medium confidence (benchmarked but not verified on this specific hardware/profile):**
- Print time estimates (35–50 min for 12-clip plate on P1S): based on Bambu P1S speed specs and volumetric flow constraints; actual time requires first production run to confirm
- Rail print time (2.5–3.5 hr): estimated from geometry volume; P1S at production speed may achieve closer to 2.5 hr
- Post-processing time per unit: based on workforce-scaling-research.md benchmarks; actual time subject to first-run measurement

**Gaps requiring test print validation:**
- Actual snap arm function (stiffness, nub engagement) — cannot be assessed from CAD alone
- FDM_TOLERANCE calibration (0.15mm may need adjustment to 0.10–0.20mm depending on specific printer)
- Plate capacity for 12-clip parallel batching (need to verify no thermal crosstalk or cooling issues with dense clip arrangement)

---

## Sources

- [Sovol3D: 3D Print Farm Management — Swarm Printing for Small-Batch Production](https://www.sovol3d.com/blogs/news/3d-print-farm-management-swarm-printing-for-small-batch-production)
- [3D-Demand: Small Batch Production with 3D Printing](https://www.3d-demand.com/blog/small-batch-production-3d-printing)
- [3DTechValley: Small Batch 3D Printing Production Guide (2026)](https://www.3dtechvalley.com/small-batch-3d-printing/)
- [Fabbaloo: 3D Printer Filament Prices in 2025 — From $5 Bulk Deals to Premium Brands](https://www.fabbaloo.com/news/3d-printer-filament-prices-in-2025-from-5-bulk-deals-to-premium-brands)
- [Overture3D: Wholesale Program](https://overture3d.com/pages/wholesale)
- [MatterHackers: Bulk 3D Printing Filament](https://www.matterhackers.com/store/l/matterhackers-bulk-3d-filament/sk/MX40GN8F)
- [EcoEnclose: Custom-Branded Sustainable Packaging](https://www.ecoenclose.com/eco-friendly-custom-packaging/)
- [noissue: Custom Packaging](https://noissue.co/)
- [Bambu Lab Wiki: Bambu Farm Manager Quick Start Guide](https://wiki.bambulab.com/en/software/bambu-farm-manager)
- [Printago: Commerce OS for 3D Print Farms](https://printago.io/)
- [3DPrinteros: Using Bambu Printer API Tools for Automation](https://www.3dprinteros.com/articles/using-bambu-printer-api-tools-for-automation-and-workflow-integration)
- [Bambu Lab Wiki: Volumetric Speed](https://wiki.bambulab.com/en/knowledge-sharing/volumetric-speed)
- [Formlabs: Vibratory Tumbling for 3D Printed Parts](https://formlabs.com/blog/vibratory-tumbling-finishing-for-sls-3d-printed-parts/)
- [Tronix3D: Revolutionizing 3D Printed Part Finishing with Vibratory Tumbling](https://www.tronix3d.com/t3d-blog/revolutionizing-3d-printed-part-finishing-with-vibratory-tumbling)
- [ScienceDirect: Causes of Desktop FDM Fabrication Failures](https://www.sciencedirect.com/science/article/pii/S2212827118312861)
- [3DPrintOps: The Real Cost of Running a 3D Printing Business](https://www.3dprintops.com/blog/3d-printing-business-costs-breakdown)
- [Pirate Ship: Get Cheaper Rates than USPS Commercial Pricing](https://www.pirateship.com/usps/commercial-pricing)
- [Amazon FBA Fees 2026 — AMZ Prep](https://amzprep.com/amazon-fba-fees/)
- [etshop.ai: From 3D Printing to $18K on Etsy](https://www.etshop.ai/to-sell-on-etsy/from-3d-printing-to-18k-on-etsy-top-tips-to-start-your-business-4979)
- [3DSourced: Complete 3D Printer Materials Cost Guide](https://www.3dsourced.com/guides/3d-printing-materials-cost/)
