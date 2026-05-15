---
title: "Post-Test-Print Production Scaling Strategy"
project: mfg-farm
created: 2026-05-15
status: active — awaiting test print result
scope: "Full production roadmap for PASS and FAIL scenarios; material optimization; capital decision framework; manufacturing technology comparison"
related:
  - POST_TEST_PRINT_REVENUE_MAXIMIZATION.md
  - production-scaling-research.md
  - material-sourcing-supplier-economics.md
  - cost-model-spreadsheet.csv
  - supplier-scorecard.csv
  - etsy-seo-strategy.md
confidence: high — sourced from verified cost models, material datasheets, and current manufacturing cost comparisons
---

# Post-Test-Print Production Scaling Strategy

**Lead finding:** The test print outcome forks the immediate timeline, but the 90-day destination is the same regardless of result. If the snap arm passes, revenue begins within 2–3 weeks. If it fails, a 1–2 week design iteration delay is the worst case, not a project threat. The economics in this document are built from the verified `cost-model-spreadsheet.csv` — at 20 units/week, the business is profitable from month one. The decision that matters most right now is not pass or fail — it is having the correct evaluation criteria ready before you pull the print from the bed, so you do not waste time on subjective assessments.

---

## Part 1: If the Test Print Passes

### 1.1 Evaluation Criteria (Read Before Opening the Print Bay)

Do not evaluate the test print on overall aesthetics. Evaluate each gate independently and in order. A failure at Gate 1 ends the evaluation — do not proceed to Gate 2 if Gate 1 fails.

| Gate | Pass Criterion | Fail Criterion | Action on Fail |
|------|---------------|----------------|----------------|
| Gate 1: Snap-arm engagement | Arm clicks into position smoothly, holds cable under 5N lateral pull, releases cleanly with one thumb | Arm cracks, does not click, rattles, or requires two hands to release | Stop. See Part 2 (Fail path). |
| Gate 2: Dimensional accuracy | Measured arm thickness 1.35–1.45mm (FDM_TOLERANCE at 1.4mm target ±0.05mm tolerance window) | Any measurement outside 1.30–1.50mm | Minor iteration (Section 1.3 near-pass) |
| Gate 3: Support-free surface quality | Clean snap-arm face, no visible layer delamination or scar > 1mm | Torn surface on snap-arm functional face | Design iteration on overhangs |
| Gate 4: Bore accuracy | 6mm bore within ±0.5mm; cable slides in without binding or slop | Bore too tight (cable jams) or too loose (cable falls out) | Parameter adjustment — bore diameter offset |

A "near-pass" (Gates 2–4 marginal, Gate 1 solid) is a one-day fix, not a project stop. Record the specific deviation values — they become the calibration data for the v1.0 production profile.

---

### 1.2 Production Volume Roadmap

The ramp sequence from first production unit to 100+ units/month is structured around two constraints: printer utilization and post-processing time. At each stage, the binding constraint shifts — understanding which one you are hitting at any given moment prevents both under-investment and premature scaling.

#### Stage 1: Validation Run (Units 1–10, Week 1–2 Post-Pass)

**Purpose**: Confirm the production slicer profile is stable. Identify any first-run failure modes that did not appear in the test print (inter-plate consistency, first-layer variation across the bed, cooling artifacts on small features).

- Print configuration: 12-clip plate (parallel, not sequential mode)
- Expected print time: 4.5–5.5 hours per 12-clip plate at 0.20mm, 3 walls, 20% infill
- Accept a 5–8% scrap rate at this stage; do not adjust tolerance settings yet
- Harvest all 12 units. Inspect each individually for Gate 1–4 criteria
- If 10+ of 12 pass all gates: production profile is locked. Proceed to Stage 2
- If fewer than 10 pass: identify the failure pattern (bed edge vs. center, first layer vs. mid-print) and address before Stage 2

**Binding constraint at Stage 1**: Print quality, not volume.

#### Stage 2: First Etsy Orders (Units 10–50, Weeks 2–6)

**Purpose**: Generate the first real customer data. Order velocity at this stage informs every downstream decision about volume, SKU mix, and marketing spend.

- Target 20 units/week (2 plates of 12 clips or mixed clip + rail plates per week)
- Print queue: build a 24–48 hour queue ahead of current production. Do not re-slice from scratch per session — version-lock the production `.3mf` profile
- Post-processing time: approximately 90 seconds per order (harvest, inspect, bag, label)
- Expected monthly net at 20/week: $1,200–$1,400 (from `cost-model-spreadsheet.csv` realistic scenario)
- List on Etsy Thursday 10 AM–2 PM (peak search traffic window per `etsy-seo-strategy.md`)
- Enable Etsy Ads at $1/day from day one of listing

**Binding constraint at Stage 2**: Order demand. The printer can handle 20/week with hours to spare. The question is whether customers find the listing.

#### Stage 3: Growth Phase (Units 50–200/month, Months 2–4)

**Trigger**: Two consecutive weeks above 30 units/week sustained demand.

- Begin planning second Bambu P1S acquisition ($699–799, 3–5 week payback at full utilization)
- Do not purchase the second printer until demand is confirmed — premature capital deployment at this stage is the most common mistake in small FDM operations
- Introduce the PETG premium SKU (higher heat deflection for server room / gaming rig customers — see `material-sourcing-supplier-economics.md` Section 1.3 for the heat deflection case)
- Begin bulk filament ordering: 10kg bundles at $12/kg (vs. $14–15/kg for single spools) once monthly usage exceeds 2kg
- Expand to headphone hook Batch 2 — this SKU has zero dependency on ModRun snap arm geometry and can run on the same production profile

**Binding constraint at Stage 3**: Marketing and listing visibility. The printer can handle this volume. The constraint is order velocity.

#### Stage 4: Scale Operation (100+ units/month, Months 4–8)

**Trigger**: 50+ units/week for two consecutive weeks OR printer running 35+ hours/week.

- Second printer acquisition confirmed
- Introduce contractor post-processing: 10 hours/week at $15/hr ($600/month) — net-positive if it enables handling 100+ vs. 70 units/week
- Monthly gross at 100/week: approximately $13,000. Net after all costs: $7,000–$8,500
- Amazon FBA onboarding: justify at 50+ units/week when Etsy reaches capacity. FBA fees are higher (28–32% of revenue vs. Etsy's ~9.5%) but remove proportional order management overhead
- Third printer trigger: 80+ units/week from 2-printer fleet sustained

---

### 1.3 Automation Sequence

Automate in order of highest leverage per hour of setup time. The following sequence reflects what can be automated immediately versus what requires iteration and validation before automating.

**Automate First (Week 1–2 after pass)**:
1. **Slicer profiles**: Lock the production `.3mf` file. This is not an automation — it is the foundation that prevents automation from drifting. Tag it in git as `v1.0`. From this point, never re-slice for production runs.
2. **Shipping label generation**: Connect Etsy to ShipStation or use Etsy's built-in label purchase. Batch-printing labels takes 3–5 minutes for a day's orders.
3. **Order notification workflow**: Etsy automatically sends buyer notifications. Enable "auto-receipt" and "auto-complete" so the buyer journey requires zero manual touchpoints until shipment.

**Automate Second (Month 1–2)**:
4. **Print queue scheduling**: Build a simple spreadsheet or Notion dashboard that maps weekly demand forecast → plate configurations → print start times. This is not software automation — it is workflow automation that prevents ad-hoc single-unit print runs, which are the primary efficiency killer at 20/week.
5. **Reorder trigger**: Set a low-filament alert. When active spool stock drops below 2 spools, place the next order. This prevents stockout delays that interrupt production momentum.

**Automate Third (Month 3–6)**:
6. **Bambu Connect remote monitoring**: The Bambu P1S supports remote camera monitoring and pause-on-failure via Bambu Cloud. Enable this for overnight runs — it eliminates the need to physically check the printer mid-job.
7. **Review request automation**: Etsy allows scheduled review-request messages. Set this to trigger 3 days after delivery confirmation. Reviews compound listing visibility over time.
8. **CadQuery STL regeneration script**: Write a single shell script that runs all `.py` design files and outputs versioned STLs to `/stl/vX.X/`. This makes design iteration a one-command operation rather than a manual re-run process.

**Do not attempt to automate** (at this scale):
- Quality inspection. Each unit requires a physical snap-arm test before shipment. At 100 units/month, inspection takes less than 20 minutes per batch — automation here costs more to build than it saves.
- Customer support responses. Individual messages require contextual judgment. Template replies for common questions (lead time, custom bore diameter, bulk pricing) are sufficient.

---

### 1.4 Supplier Negotiation Checklist

The current supplier scorecard (`supplier-scorecard.csv`) documents eSUN and Overture as the two primary candidates. The following checklist translates that analysis into executable negotiation steps at three volume tiers.

#### 1 Unit (Pre-Negotiation — Current State)

- Purchase from Amazon Prime at market rate: eSUN PLA+ 1kg black, approximately $14–15/kg
- No negotiation possible at this volume. Accept the rate.
- Use this period to build a purchase history that justifies future bulk pricing

#### 10 Units/Month (~2–3kg filament/month)

- Still below MOQ for direct supplier negotiation
- Switch to Amazon Subscribe & Save for filament (5% discount, reliable delivery cadence)
- Place 2-spool orders (2kg per order) rather than single-spool to reduce per-order shipping cost
- Begin evaluating eSUN's direct store on Amazon (often $1–2/kg cheaper than third-party sellers)

#### 100 Units/Month (~5–8kg filament/month)

- At this volume, contact eSUN directly (support@esun3d.com) or via Alibaba for wholesale pricing
- State: monthly volume (kg), specific SKUs (PLA+ black, PLA+ white), preferred delivery cadence
- Target price: $9–11/kg for 10kg+ orders (vs. $14–15/kg retail)
- Request: NET 30 payment terms (not required, but worth asking)
- MOQ: eSUN typically sets 5kg MOQ per color for direct orders — achievable at 100 units/month
- Parallel: evaluate Anycubic Mega PLA+ ($10.49/kg at 50kg order per `production-scaling-research.md`) as a backup supplier for price anchoring in the negotiation

**Supplier negotiation script** (can be used verbatim in email):

> We are a small-batch FDM manufacturer producing cable management accessories. We currently use [eSUN PLA+ / Overture PLA+] and are looking to establish a direct purchasing relationship. Our current monthly usage is approximately [X]kg and is growing. We are interested in your wholesale pricing for PLA+ in black and white at 10kg+ order quantities. Can you share a current price sheet and MOQ requirements?

---

### 1.5 Fulfillment Setup

**Packaging (to be ordered by Day 2 after pass)**:
- 100× kraft mailer boxes (for rail orders): 9×6×4 inch, approximately $0.25–0.40 each from ULINE or Amazon
- 100× poly mailers (for clip-only orders): 6×9 inch, approximately $0.08 each
- 100× zip-lock bags (for clip bundles inside mailers): approximately $0.03 each
- Thermal label printer (if not already available): Rollo X1038 or Dymo LabelWriter 4XL ($80–120, one-time cost, required for volume above 5 orders/day)

**Shipping logistics**:
- Primary carrier: USPS First Class Package (under 1 lb). Clip bundles (120g): $4.00–4.50. Rail orders (200g boxed): $5.00–5.50
- Etsy's discounted USPS rates: access via Etsy Ship (integrated at checkout). Provides 30–40% discount vs. post office counter rates
- Processing time commitment on Etsy: list as 3–5 business days. Do not understate this — one late shipment in the first two weeks damages the seller rating disproportionately
- Ship daily if above 5 orders/day. Ship 3×/week if below 5 orders/day (batching reduces post office trips without materially affecting delivery dates)

**Returns and defects**:
- Expected defect rate: 2–4% at mature production. During the first two weeks, budget 5–8%
- Return policy: "Defective items replaced or refunded within 30 days of delivery. Buyer responsible for return shipping on non-defective items." This is standard for Etsy physical goods and protects against snap-arm-related warranty claims
- For defective returns: log each defect type (snap arm, bore accuracy, cosmetic). When defect rate for any single failure mode exceeds 3%, investigate at the production level before the next batch

**Inventory management**:
- Storage requirements at 100 units/month: approximately 0.5 cubic feet for printed inventory in transit (3–5 days of stock), plus 1 cubic foot for filament (10–12 spools). This fits in a standard desk drawer and a shelf.
- Do not build inventory more than 2 weeks ahead of expected demand. FDM parts have no shelf-life problem, but excess inventory ties up capital and space without benefit at this volume
- Rotation strategy: FIFO. Print oldest designs first when design versions coexist (prevents selling v1.0 stock after v1.1 has been validated)
- Reorder trigger for consumables: order packaging materials when stock drops below 30-unit buffer (approximately 2 weeks of supply at 20/week)

---

### 1.6 Quality Control SOP

**Pre-print (every plate)**:
1. Clean PEI plate with IPA wipe. Dry 30 seconds.
2. Confirm slicer profile matches production version: `ModRun-PLA-Production-v1`. Verify layer height (0.20mm), walls (3), infill (20%), temps (nozzle 220–225°C, bed 55°C).
3. Verify filament spool is the approved production brand (eSUN PLA+ or Overture PLA+). Do not mix brands within a plate.
4. Confirm the `.3mf` file is from `/sliced/production/` directory, not a test file.

**Post-print harvest (every unit)**:
1. Physical snap-arm test: engage and release twice. Both operations must be smooth and audible (click). Reject if: no click, cracked arm, rattles after engagement.
2. Dimensional spot-check (every 6th unit as representative sample): measure snap-arm thickness with calipers. Accept range 1.35–1.45mm.
3. Visual inspection: no stringing across bore, no base warping, no surface blobs on snap-arm face. Cosmetic layer lines are acceptable and expected.
4. Set aside rejects in a separate container labeled "DEFECTS". Photograph before disposal.

**Defect rate targets**:
- Weeks 1–2 (calibration period): accept up to 10% defect rate
- Month 1 (established production): target below 5%
- Month 3+ (mature production): target below 3%
- If defect rate exceeds 8% in any single plate: pause production, identify root cause before next run

**Batch sign-off**:
- Log each plate in a simple production log: date, plate config, units printed, units passed, defect count and type
- This log becomes your QC audit trail if a customer reports a batch defect

---

## Part 2: If the Test Print Fails

### 2.1 Failure Classification

Not all failures are equal. Before deciding on a response, classify the failure type — this determines whether you need a design change, a parameter change, or a material change.

| Failure Type | Symptom | Root Cause | Response |
|---|---|---|---|
| Type A: Arm cracks on engagement | Snap arm shatters during first engagement test | Insufficient arm thickness or PLA+ brittleness at this geometry | Increase SNAP_ARM_THICKNESS parameter; consider PETG |
| Type B: Arm doesn't click | Arm deflects but doesn't engage the retention feature | FDM_TOLERANCE too tight — arm is deforming past the catch point | Increase FDM_TOLERANCE from 1.4mm → 1.6–1.8mm |
| Type C: Arm rattles after engagement | Arm clicks in but cable vibrates loose | FDM_TOLERANCE too loose — arm is engaging but not gripping | Reduce FDM_TOLERANCE from 1.4mm → 1.2–1.3mm |
| Type D: Arm doesn't release cleanly | Requires two hands to disengage | Over-constrained snap geometry; arm is too stiff | Reduce wall count on arm from 3 → 2, or add chamfer to catch feature |
| Type E: Bore too tight or too loose | Cable won't insert or falls out immediately | CadQuery bore diameter needs offset correction | Adjust `BORE_DIAMETER` parameter in `modrun_clip.py` |
| Type F: Surface delamination on arm face | Layer separation on snap-arm face | Temperature too low; print speed too fast on arm geometry | Increase nozzle temp to 225–230°C; reduce outer wall speed |

A single test print can produce multiple failure types simultaneously. Address Type A or B first — structural engagement is the primary function. Surface quality (Type F) is a secondary concern.

---

### 2.2 Design Iteration Strategy

**Iteration 1: Tolerance Adjustment Only (24–36 hours)**

If the failure is Type B or C (engagement geometry), the fix is a single parameter change in `modrun_clip.py`:

```python
# Current production value
FDM_TOLERANCE = 1.4  # mm

# Type B (no click): increase to
FDM_TOLERANCE = 1.6  # or 1.8 if 1.6 also fails

# Type C (rattle): decrease to
FDM_TOLERANCE = 1.2  # or 1.3
```

Re-run the CadQuery script, re-export STL, re-slice (do not use the previous plate file), print a single test unit. Evaluate immediately — do not print a full plate until the single unit passes Gate 1.

**Cost impact of Iteration 1**: Single test unit uses approximately 3–4g of PLA+ (< $0.10 material cost). Time cost: 45–60 minutes print time plus 30 minutes design and slicer work. Total delay from failure to next test print: approximately 4–6 hours if done same-day.

**Iteration 2: Structural Redesign (2–4 days)**

If Iteration 1 does not resolve the failure (Type A: arm cracking), a structural redesign is required:

1. Increase `SNAP_ARM_THICKNESS` by 0.2–0.4mm increments in `modrun_clip.py`
2. Add internal rib to snap arm base (requires CadQuery sketch modification, approximately 1–2 hours of design work)
3. Add fillet at cantilever root (reduces stress concentration — the most common root cause of snap arm fracture in FDM parts). The fillet radius should be 0.5–1.0mm at the base of the arm.

**Alternative for Type A**: Switch to PETG for the test print before structural redesign. PETG's elongation-at-break (50–200% vs. PLA+'s 5–8%) may resolve the cracking failure without any design changes. PETG test print uses the same profile with adjusted temperatures (240–250°C nozzle, 70–80°C bed). This is a 4-hour path vs. a 2-day redesign path.

**Iteration 3: Full Arm Redesign (1–2 weeks)**

If Iterations 1 and 2 both fail, the snap arm geometry itself is incompatible with FDM at this scale. This is the lowest-probability outcome but must be planned for:

- Option A: Replace cantilever snap with a living hinge design (requires full CadQuery redesign, approximately 8–12 hours)
- Option B: Replace snap fit with a friction fit + thumb-screw tension (eliminates the snap-arm reliability requirement entirely; less elegant but more FDM-tolerant)
- Option C: Switch to SLA (resin) for the snap arm component only — higher precision (±0.05mm vs. FDM's ±0.3mm for small features), no layer-adhesion brittleness, but higher per-unit cost (see Section 4 for cost comparison)

**Reprint timeline after each iteration**:
- Iteration 1 (tolerance adjust): test print within 4–6 hours of failure assessment
- Iteration 2 (structural): redesign 1–2 days + test print 1 day = 2–3 days total
- Iteration 3 (full redesign): 1–2 weeks

**Total worst-case delay**: 2 weeks from initial failure to production-ready design. This does not affect Batch 2 (headphone hooks) — that SKU can begin its own print queue immediately regardless of ModRun status.

---

### 2.3 Materials Research: Alternatives with Better Tolerance Specs

The following materials are ranked by FDM snap-fit suitability. Data sourced from manufacturer datasheets and community validation (Prusa forums, RepRap community, filament brand comparison databases).

#### Top 5 Materials for Snap-Fit FDM (2025–2026 Data)

**1. Prusament PLA** (Prusa Research, ~$25/kg)
- Diameter tolerance: ±0.02mm (tightest in class — filament-level precision directly reduces part-level variance)
- Elongation at break: 4–6%
- Snap-fit rating: Good for single-use installation snaps; borderline for cyclic use
- Best for: ModRun use case (one-time installation flex, not repeated opening/closing)
- Note: Prusament's tighter diameter tolerance reduces layer-width variation, which is the primary source of snap-arm dimensional drift in FDM

**2. Polymaker PolyLite PLA** (~$19/kg)
- Diameter tolerance: ±0.03mm (community-verified: 70% of spools are within ±0.01mm)
- Elongation at break: 6–8%
- Snap-fit rating: Good — slightly more flexible than standard PLA+
- Best for: High-volume production where Prusament's premium price ($25 vs. $12–14/kg eSUN) matters

**3. eSUN PLA+** (~$12–14/kg) — current production material
- Diameter tolerance: ±0.03mm
- Elongation at break: 5–8%
- Snap-fit rating: Good for single-use installation. Adequate for repeated (but infrequent) cycling
- Best for: Cost-optimized production at scale. Best price-to-performance ratio at 10kg+ order volumes

**4. PETG (any major brand — eSUN, Overture)** (~$14–18/kg)
- Diameter tolerance: ±0.05mm
- Elongation at break: 50–200% (by far the best in this list)
- Snap-fit rating: Excellent — will survive repeated deflection cycles without cracking
- Heat deflection: 70–75°C vs. PLA+'s 55–60°C
- Best for: Snap arms that will experience repeated cycling; gaming rig / server room applications
- Trade-off: Slightly less dimensionally accurate than PLA+; more prone to stringing (manage with retraction tuning)

**5. Bambu PLA Basic/Matte** (~$18–22/kg for Bambu brand)
- Diameter tolerance: ±0.02–0.03mm (Bambu's quality control is among the tightest for FDM filament)
- Elongation at break: 5–7%
- Snap-fit rating: Good — optimized for Bambu printers' flow calibration
- Best for: If you already own a Bambu P1S and want plug-and-play calibration with zero profile adjustment
- Note: Higher cost than eSUN/Overture, but eliminates filament-specific slicer tuning time

**Recommendation for failure path**: If snap arm cracks (Type A failure), switch to PETG (Option 4) before redesigning. The material change is faster than a structural redesign and will likely resolve the issue. If snap arm doesn't engage (Type B failure), stay with PLA+ and adjust FDM_TOLERANCE — material is not the problem.

---

## Part 3: FDM Optimization for Snap-Fit Precision

### 3.1 Current Industry Best Practices (2024–2026)

The following represents the current consensus from FDM snap-fit literature (Protolabs Network, Formlabs, Hubs.com, and RepRap community documentation as of 2025–2026):

**Clearance and tolerance design rules**:
- Specify 0.5mm clearance for FDM snap-fit connectors as the baseline. This is the current industry standard per Protolabs Network's snap-fit joint design guide (2025)
- The ModRun design's FDM_TOLERANCE of 1.4mm is a gap-to-feature ratio, not a direct clearance specification — it is the total material removed from the snap arm to create the flex zone. This is appropriate and within normal FDM design practice
- Apply the full clearance value to only one part in a mating pair (the moving part), not split across both — this is the rule most commonly violated in FDM snap-fit designs that fail

**Cantilever snap arm geometry best practices**:
- Taper the arm from 1.5× thickness at the base to 1× thickness at the tip. This distributes the bending stress more evenly, reducing the peak stress at the root (the cracking point)
- Add a minimum 0.5mm fillet radius at the cantilever root. This is the most impactful single geometry change for preventing root fracture in FDM
- Keep arm length-to-thickness ratio between 4:1 and 8:1. Below 4:1, the arm is too stiff and the part breaks instead of deflecting. Above 8:1, the arm deflects so much it misses the catch feature
- Deflection during assembly should not exceed 50% of the arm length at the catch point — exceeding this is the primary cause of Type A failures

**Extrusion width rule for small features**:
- For features smaller than 3× the nozzle diameter (0.4mm nozzle = 1.2mm threshold), dimensional accuracy degrades significantly
- The snap arm at 1.4mm is above this threshold, but only marginally. Any tolerance dial-in must account for the fact that the arm is printed in approximately 3–4 perimeter passes — the outer two passes define the functional geometry

### 3.2 Layer Height Trade-Offs: 0.15mm vs. 0.20mm

The test print is specified at 0.20mm layer height. This is the correct choice for production, with one important nuance.

| Parameter | 0.15mm | 0.20mm | Recommendation |
|---|---|---|---|
| Print time impact | +25–30% longer | Baseline | 0.20mm for production |
| Z-axis dimensional accuracy | ±0.15mm | ±0.20mm | 0.15mm only if Gate 2 consistently fails |
| Snap arm Z-height precision | Better | Adequate | 0.20mm is adequate for ModRun geometry |
| XY dimensional accuracy | No impact — XY accuracy is independent of layer height | No impact | Use 0.20mm |
| Visual quality | Smoother surface | Visible layer lines (acceptable for cable clips) | 0.20mm acceptable for Etsy listings |

**Practical conclusion**: Use 0.20mm for all production. Switch to 0.15mm only if snap arm height (Z dimension) is consistently failing Gate 2 measurement — and even then, prefer a FDM_TOLERANCE adjustment over a layer height change, since layer height changes increase print time significantly.

### 3.3 Nozzle Material Impact

The test print and production runs are using a standard brass nozzle. This is appropriate for PLA+. A note on nozzle material options for future reference:

- **Brass nozzle (0.4mm)**: Standard. Appropriate for all PLA variants, PETG, and most standard filaments. Maximum operating temp approximately 300°C. No impact on dimensional accuracy.
- **Hardened steel nozzle**: Required for abrasive filaments (carbon fiber, glow-in-the-dark, metal-fill). Does NOT improve dimensional accuracy for PLA+ or PETG — the nozzle material does not affect snap arm precision.
- **Copper/plated copper nozzle**: Better thermal conductivity improves melt consistency at high speeds. Marginally useful at speeds above 300mm/s. Not needed at the current production profile.

**Decision**: Do not change nozzle material for the current production run. The brass nozzle is the correct tool for PLA+ at 220–225°C. Hardened steel is only required if you introduce carbon-fiber PLA for a premium SKU.

---

## Part 4: Capital and Manufacturing Technology Decision Framework

### 4.1 FDM vs. SLS vs. Injection Molding — When the Math Changes

The current production model (FDM on Bambu P1S) is the correct choice at every volume level up to approximately 500 units/month for this part geometry and price point. The following analysis documents when and why alternatives become competitive.

#### FDM Production Economics (Your Current Path)

| Volume | Monthly revenue (blended $24.99 AOV) | Net margin | Notes |
|---|---|---|---|
| 20/week (80/month) | ~$2,000 | 67–73% | Solo sustainable, no additional capital |
| 50/week (200/month) | ~$5,000 | 73% | Single printer at full utilization |
| 100/week (400/month) | ~$10,000 | 70–72% | Second printer required |
| 200/week (800/month) | ~$20,000 | 68–70% | Third printer, part-time contractor |

#### SLS (Selective Laser Sintering) — Outsourced

SLS produces dimensionally accurate parts (±0.3mm) in PA12 nylon, which has significantly better snap-fit fatigue performance than PLA+. However:

- Cost per part (outsourced, 100-unit batch): approximately $5–12 per clip depending on service provider (Craftcloud, Shapeways, Hubs.com)
- This destroys the margin model. At $5–12/clip COGS and $12–15 retail price for individual clips, there is no viable business
- SLS is worth evaluating at the point where you want to position a premium "lifetime warranty" SKU at $25–35+ per clip for server rack applications — a niche market that may exist but has not yet been validated

**Decision**: SLS is not viable for the core ModRun product at any volume that competes with FDM margins. Do not pursue until a validated premium market segment is identified.

#### SLA (Resin) — Outsourced or In-House

SLA provides ±0.05mm dimensional accuracy — substantially better than FDM for snap arm geometry. This makes it a credible fallback for the Type A (cracking) failure scenario.

- In-house SLA (Elegoo Saturn 4 Ultra, ~$400): Could produce snap arms at approximately $0.50–1.50 per part depending on resin cost
- Post-processing overhead: SLA requires wash-and-cure cycle per plate (25–35 minutes additional per batch). This adds labor cost
- Material cost: engineering resin (ABS-like) at approximately $35–60/kg — 3–4× the cost of PLA+
- Best use case: If FDM snap arm consistently fails at prototype stage and structural redesign does not resolve it, SLA for snap arms only (with FDM for the clip body) becomes a viable hybrid approach

**Decision**: Evaluate SLA only if Iteration 3 of the failure path is reached. Do not invest in SLA infrastructure preemptively.

#### Injection Molding — When the Numbers Work

Based on current manufacturing cost comparisons (Formlabs 2025, Fictiv 2025, be-cu.com analysis):

- Aluminum mold (prototype tooling): $2,000–10,000 upfront
- Per-part cost after mold: $0.50–2.00 (vs. FDM's $0.35–0.75 material cost, but FDM includes no mold amortization)
- Break-even vs. FDM: 1,000–13,000 units depending on part complexity. For a small latch component (directly comparable to ModRun clip), one study found break-even at 13,050 units
- At ModRun's current margin model, 13,050 units represents approximately 12–15 months of production at 100/week

**Decision trigger**: When monthly unit production exceeds 500/month for 3 consecutive months AND the design is locked (no further design iteration expected), request three injection molding quotes (Xometry, Fictiv, local). Compare per-unit cost including mold amortization over a 24-month horizon against the FDM cost model. The decision will likely fall between 5,000 and 10,000 total units depending on part geometry.

**Practical timeline**: Injection molding is a Year 2 or Year 3 decision for this business. Do not model it into the current launch plan.

---

## Part 5: Go/No-Go Decision Tree and Timeline

### 5.1 Decision Tree (Execute Within 24 Hours of Test Print)

```
TEST PRINT COMPLETE
       |
       v
Gate 1: Snap arm clicks, holds, releases?
       |
   YES / NO
   |       |
   v       v
Gates 2-4  FAIL PATH
(below)    See Part 2
   |
   v
Gates 2-4 all pass?
       |
   YES / NO
   |       |
   v       v
PASS      Near-pass?
           |
       YES / NO
       |       |
       v       v
   One-day   Full Part 2
   fix (see  Iteration 1
   Sec 1.3)
       |
       v
PRODUCTION READY

```

### 5.2 Post-Decision Timeline

#### If PASS (or Near-Pass Resolved)

| Day | Action |
|-----|--------|
| Day 0 (test print harvested) | Lock FDM_TOLERANCE in git as v1.0. Tag `/stl/v1.0/` as write-protected. |
| Day 0 (evening) | Start first 12-clip production plate. Print overnight. |
| Day 1 (morning) | Harvest and inspect production plate. Place materials order (2× eSUN PLA+ black, 1× white, 100× poly mailers, 100× kraft boxes). |
| Day 1–2 | Photograph product: 5 required shots per `post-test-print-doc-3-lifestyle-photography-brief.md`. Do not publish without photos. |
| Day 3–7 | Continue printing. Build 20-unit inventory buffer before listing goes live. |
| Day 7 | Publish Etsy listing (Thursday 10 AM–2 PM). Enable Etsy Ads at $1/day. |
| Day 7–14 | First customer orders. Monitor daily. Inspect every unit before shipment. |
| Week 2–4 | Validate 20/week production cadence. Contact headphone hook design queue for Batch 2 ramp. |
| Month 2 | Review order velocity. If above 30/week for two weeks: initiate second printer research. |
| Month 3 | Evaluate PETG premium SKU based on customer feedback. Begin direct supplier contact at 5kg/month+ usage. |

#### If FAIL

| Day | Action |
|-----|--------|
| Day 0 | Classify failure type (A–F per Part 2.1). Identify the single highest-priority gate failure. |
| Day 0 (same day) | Execute Iteration 1 (tolerance adjustment) if Type B or C. Print single test unit. |
| Day 1 | Evaluate Iteration 1 result. If pass: proceed to production. If fail: classify as Type A and evaluate PETG switch vs. Iteration 2. |
| Day 1–3 | PETG test print (if Type A) OR structural redesign (Iteration 2). |
| Day 3–5 | Evaluate second test result. Decision: production if pass; full redesign (Iteration 3) if fail. |
| Day 1 (parallel, regardless) | Begin headphone hook Batch 2 print queue. This SKU is not blocked by ModRun status. |
| Week 2+ | Continue headphone hook production for Etsy revenue while ModRun redesign resolves. |

### 5.3 Etsy Listing and Supplier Onboarding Timeline (Pass Path)

- Supplier negotiation email: send on Day 14 (after first production plate is confirmed stable, before placing bulk orders). Template available in `post-test-print-doc-1-supplier-negotiation-email-templates.md`.
- First production order (filament + packaging): Day 1 (Amazon Prime, same-day or next-day delivery).
- Bulk filament first purchase: Month 2 when monthly usage exceeds 2kg/month.
- Etsy listing live date: Day 7–10 (Thursday preferred for peak traffic).
- First customer order expected: Day 7–21 depending on listing visibility and Etsy Ads performance.
- Etsy Ads budget review: after 7 days. If ROAS (return on ad spend) is above 2:1, increase to $3/day. If below 1:1 after 14 days, pause and review listing title/tags before resuming.

---

*Created: 2026-05-15. Awaiting test print result. Both paths (PASS and FAIL) are fully documented above — the only required user action is evaluating the print against the Gate 1–4 criteria in Section 1.1, then following the appropriate path. No new research or planning is required before the test print is evaluated.*

*Sources: Protolabs Network snap-fit joint design guide; Formlabs FDM vs. SLA vs. SLS cost comparison 2025; be-cu.com injection molding break-even analysis; Prusament, eSUN, Polymaker filament datasheets; Hubs.com snap-fit design guide; Fictiv injection molding economics.*
