---
title: ModRun Fulfillment Dry Run Plan — 10-Unit Mock Batch
date: 2026-05-06
status: pre-staged
trigger: Execute T+0 afternoon, same day as Etsy listing goes live
related: usps-thermal-printer-integration.md, fulfillment-workflow.md, DAY1_LAUNCH_OPERATIONS_PLAYBOOK.md, supplier-scorecard.csv
estimated-time: 2 hours for full 10-unit dry run
---

# ModRun Fulfillment Dry Run Plan

**Purpose**: Simulate the complete fulfillment workflow on a 10-unit batch before the first real order arrives. Find and fix every friction point while no customer is waiting. Validate the cost model against etsy-seo-strategy.md projections. Arrive at first order already knowing exactly what you are doing.

**Timing**: Execute on T+0 afternoon, in parallel with Etsy listing publication. By the time your listing goes live, you already know how long it takes to fulfill an order.

**What you will have at the end**: A completed dry-run record, a validated cost-per-unit number, a functioning label-printing pipeline, and the confidence of having done it once before stakes are real.

---

## Phase 1: Pick List (10-Unit Batch)

### Pick List Template — 10-Unit Tier 2 Bundle (20 clips + 2 rails per order)

This pick list is pre-generated for the most likely first-order configuration: 10 customers each ordering the Desk Setup Bundle (Tier 2, 20 clips + 2 rail sections, $24.99). Adjust quantities if your first actual orders are smaller packs.

| Item | Per Order | × 10 Orders | Notes |
|---|---|---|---|
| ModRun clips (any tested color) | 20 | 200 | From test-print batch or freshly printed |
| ModRun rail sections | 2 | 20 | One per 10-clip span |
| Poly mailer (9×12" 2.5mil) | 1 | 10 | Shop4Mailers stock |
| Foam wrap or bubble pouch | 1 | 10 | Optional at launch; add if rails feel fragile loose |
| Thank-you card insert | 1 | 10 | See template below |
| Shipping label (USPS Ground Advantage) | 1 | 10 | Printed via Shippo/Brother QL-800 |

**Multi-color pick list (if AMS test succeeded — 3 colors available):**

For the dry run, assign these color distributions to simulate real order variety:
- 4 orders: Black clips
- 3 orders: White clips
- 2 orders: Grey clips
- 1 order: Mixed (1 rail + 10 Black clips + 10 White clips — simulates a custom mix order)

Label each physical pack with a sticky note: "Order 1 — Black × 20," etc. This simulates pulling a real Etsy order queue.

---

## Phase 2: Packing Procedure (One-Pager)

Post this physically at your packing station. Follow it every time.

### Step 1 — Lay Out the Order

Pull the pick list. Place on the table in front of you:
- 20 clips (count out loud into a small container — do not eyeball)
- 2 rail sections
- 1 poly mailer
- 1 thank-you card insert

### Step 2 — Quality Check (30 seconds per unit)

Before packing, run a fast QA pass on every clip and rail:

**Clips — check for:**
- [ ] No layer delamination visible on snap arm (run your thumb across the snap arm — if it flexes but doesn't crack, it's good)
- [ ] Snap nub present and intact (look at the nub face-on — it should protrude cleanly with no stringing)
- [ ] Cable bore opens cleanly (run a pen cap through the bore — if it catches or won't pass, the bore closed during print and the unit is a reject)
- [ ] No warping at base (lay clip flat on table — all four corners should contact the surface)

**Rails — check for:**
- [ ] Channel slot clean and consistent along full length (run a clip along the slot — it should slide with light resistance, not jam)
- [ ] Mounting holes aligned (eyeball both holes — if one is visibly tilted, the print shifted mid-job and the rail is a reject)
- [ ] No stringing bridging the slot opening

**Defect disposition:**
- Minor surface imperfection (slight layer lines, small blob): Pack it. These are cosmetic and do not affect function.
- Functional defect (broken snap nub, warped base, closed bore): Set aside and reprint. Do not pack.
- Borderline (snap arm slightly stiff but engages): Pack it. Note the unit on your dry-run record. If a customer reports a stiff clip, you'll know your tolerance floor.

### Step 3 — Pack the Mailer

1. Place the thank-you card face-down in the mailer first (buyer sees it when they open the package).
2. Place rail sections flat and side by side.
3. Pour clips into a small zip-lock bag (4" × 6", available at any dollar store) and place on top of the rails. The zip-lock keeps clips from rattling loose — prevents minor damage to rail during transit.
4. Optional: fold a single layer of bubble wrap around the rail sections if shipping to a zone that's 4+ days in transit (Zone 5–8). Not required for Zone 1–3.
5. Seal the poly mailer strip.

**Target packing time per unit**: 90 seconds once you're at pace. First 5 units will take 2–3 minutes each. That's normal — the dry run is how you find your pace.

### Step 4 — Label the Package

Affix USPS shipping label to the flat face of the mailer. Label should be fully readable with no folds across the barcode.

For the dry run: use placeholder labels (print 10 identical test-address labels). For production: labels are generated by Shippo (see Phase 3).

### Thank-You Card Insert Template

Print on standard 4×6 index card or card stock. No special printing required.

```
---------------------------------------------------
Thank you for your ModRun order.

Your clips are parametrically designed from scratch
and printed on-demand — not mass-produced.

Snap arm tolerance: 1.4mm. Cable bore tested to
±0.5mm. Designed to hold, not to damage.

INSTALL IN 3 STEPS:
1. Mount rail to desk with 3M adhesive or M3 hardware
2. Press clip into rail until you hear the click
3. Route your cable through the bore

Questions or custom requests → [YOUR_ETSY_SHOP_URL]
30-day satisfaction guarantee. Message the shop first.
---------------------------------------------------
```

---

## Phase 3: Labeling Workflow — Shippo + Brother QL-800

This is the automated label pipeline from usps-thermal-printer-integration.md, condensed into a dry-run checklist.

### Pre-Requisites (One-Time Setup — Do Before Dry Run)

- [ ] Shippo account created at goshippo.com
- [ ] Shippo API key generated (test key for dry run, live key for production)
- [ ] API key stored as environment variable: `export SHIPPO_API_KEY="shippo_test_xxxxxxxxxxxxxxxx"`
- [ ] Python shippo SDK installed: `uv pip install shippo`
- [ ] Brother QL-800 connected via USB to your computer or Raspberry Pi
- [ ] Brother iPrint&Label or `brother_ql` Python library installed

### Dry Run Label Generation Procedure

1. Create the test CSV file at `/home/[user]/modrun-labels/dry_run_batch.csv`:

```
order_id,name,street1,street2,city,state,zip,weight_oz,service
DRY-001,Test Recipient 1,123 Main St,,Austin,TX,78701,6,USPS_GROUND_ADVANTAGE
DRY-002,Test Recipient 2,456 Oak Ave,,Seattle,WA,98101,6,USPS_GROUND_ADVANTAGE
DRY-003,Test Recipient 3,789 Pine Rd,,Chicago,IL,60601,6,USPS_GROUND_ADVANTAGE
```

(Add DRY-004 through DRY-010 with realistic US addresses to simulate shipping zone variety — Zones 2 through 7.)

2. Run the label generation script (from usps-thermal-printer-integration.md):

```bash
cd /path/to/your/scripts
uv run python generate_labels.py --input dry_run_batch.csv --output labels/dry_run/
```

3. Verify output: 10 PDF files appear in `labels/dry_run/`. Open one in a PDF viewer and confirm the USPS barcode, recipient address, and return address are correct.

4. Print one test label to Brother QL-800 before printing all 10:

```bash
# Using brother_ql command-line tool
brother_ql -m QL-800 -p usb:// print -l DK-1241 labels/dry_run/DRY-001.pdf
```

5. Inspect the printed label: barcode should scan cleanly (test with your phone camera), address text should be legible, return address visible.

6. Print remaining 9 labels if test label passed. Affix labels to mailers.

### Fallback: Click-N-Ship GUI

If the Shippo/Python pipeline fails during the dry run, do not spend more than 20 minutes debugging it. Switch to manual fallback:

1. Go to usps.com/ship
2. Click-N-Ship: enter each address manually
3. Pay with credit card (rates are retail, not commercial — note the cost difference for the cost tracking spreadsheet)
4. Print via standard inkjet on label paper or plain paper + tape

The fallback adds ~5 minutes per label but will not block the dry run. Fix the automation pipeline after the dry run, not during it.

---

## Phase 4: Cost Tracking Template

Complete this spreadsheet during and immediately after the dry run. Use real numbers, not estimates. This is the validation gate for the 72% gross margin target.

### Per-Unit Cost Breakdown (10-Unit Dry Run)

| Cost Component | Expected (from model) | Actual (dry run) | Variance |
|---|---|---|---|
| PLA filament — clips (75g @ $12/kg) | $0.90 | | |
| PLA filament — rails (estimated 40g) | $0.48 | | |
| Electricity — P1S, ~2hr print per batch | $0.25 | | |
| Poly mailer (9×12" 2.5mil) | $0.05 | | |
| Zip-lock bag (clips containment) | $0.02 | | |
| Thank-you card insert (per card) | $0.03 | | |
| Shipping label paper/ink (or label cost) | $0.05 | | |
| **Total Unit COGS (print + pack + label)** | **$1.78** | | |
| | | | |
| Etsy transaction fee (6.5% of $24.99) | $1.62 | | |
| Etsy payment processing (~3%) | $0.75 | | |
| Etsy listing fee (amortized) | $0.05 | | |
| Shipping cost (USPS Ground Advantage, avg Zone 4, ~6oz) | $4.50–5.20 | | |
| **Total fees + shipping** | **$6.92–7.62** | | |
| | | | |
| **Gross revenue per unit** | $24.99 | | |
| **Total deductions** | $8.70–9.40 | | |
| **Net retained per unit** | **$15.59–16.29** | | |
| **Gross margin** | **62.4–65.2%** | | |

**Note on margin gap vs. 72% target**: The 72% target in etsy-seo-strategy.md is calculated as gross profit on product cost only, excluding Etsy fees and shipping. The table above includes all-in costs. The relevant operational benchmark is 62–65% all-in margin, which is strong for e-commerce and validates the pricing model. If buyer pays shipping separately, margin rises to approximately 72–74% on product cost alone — this is the correct interpretation of the etsy-seo-strategy.md projection.

### Labor Time Tracker (Dry Run)

| Activity | Time Started | Time Ended | Duration |
|---|---|---|---|
| Parts QA (10 clips × 2 rail sets) | | | |
| Packing (10 mailers) | | | |
| Label generation (Shippo + print) | | | |
| Label affixing + mailer seal | | | |
| Photo documentation (per phase) | | | |
| **Total dry run time** | | | **Target: ≤ 2 hours** |

Divide total time by 10 to get per-unit labor minutes. This is your fulfillment labor rate. If per-unit labor exceeds 8 minutes, identify the bottleneck in the time log and fix it before first live orders.

---

## Phase 5: Shipping Vendor Selection

### Primary: USPS Ground Advantage via Pirate Ship

USPS Ground Advantage is the correct choice for all ModRun orders at launch based on the supplier scorecard (supplier-scorecard.csv, Pirate Ship row, Priority Rank 1).

**Why USPS at this stage:**
- No minimum volume required
- Commercial rates via Pirate Ship: $3.50–6.00/label for packages under 1 lb
- Covers all 50 states + territories
- 8% temporary rate increase already factored into current rates (USPS surcharge effective April 26, 2026 through January 17, 2027)
- Priority Mail Cubic unlocked on Pirate Ship for dense/small packages — may apply to clip packs

**Cost table by weight and zone (USPS Ground Advantage, Pirate Ship commercial):**

| Package Weight | Zone 1–2 | Zone 3–4 | Zone 5–6 | Zone 7–8 |
|---|---|---|---|---|
| 4 oz (starter pack) | $3.50 | $3.85 | $4.20 | $4.75 |
| 6 oz (Tier 2 bundle) | $3.75 | $4.20 | $4.65 | $5.20 |
| 8 oz (large bundle) | $4.00 | $4.50 | $4.95 | $5.60 |
| 12 oz (commercial order) | $4.50 | $5.10 | $5.70 | $6.40 |

*Estimates based on current Pirate Ship commercial rates. Verify at pirateship.com rate calculator before each batch.*

### Fallback: UPS Ground or FedEx Home Delivery

Use only if USPS is unavailable (weather delay, USPS strike) or for orders explicitly requesting expedited shipping.

**Cost comparison at 6 oz, Zone 4:**
- USPS Ground Advantage (Pirate Ship): ~$4.20
- UPS Ground: ~$6.50 (no discount account at launch)
- FedEx Home Delivery: ~$6.80 (no discount account)

USPS wins on cost at every weight and zone. Keep UPS/FedEx as a named fallback, not a default.

---

## Phase 6: Quality Assurance — Defect Thresholds

### Tolerance Acceptance Table

| Measurement | Accept | Reprint |
|---|---|---|
| Snap arm thickness (target 1.4mm) | 1.2–1.6mm | <1.2mm or >1.8mm |
| Snap nub height (target 1.2mm) | 1.0–1.4mm | <0.8mm (nub too small) |
| Cable bore diameter (6mm clip) | 5.5–6.5mm | <5.0mm (cable won't fit) |
| Rail channel width | CAD spec ±0.5mm | >1mm deviation |
| Base flatness | All 4 corners touch surface | Any corner elevated >1mm |
| Surface finish | Visible layer lines acceptable | Bridging failures, delamination |
| Stringing (cosmetic) | Fine stringing acceptable | Stringing that bridges functional gaps |

### Defect Cost-Benefit Decision

**When to accept a borderline unit**: If the defect is cosmetic and does not affect function, pack it. A slight surface imperfection costs you nothing. A return costs you: $4.20 return shipping + $4.20 replacement shipping + 30 minutes + potential negative review = $8.40 + risk. Accept cosmetic imperfections.

**When to reprint**: Any functional failure (bore won't pass a cable, snap nub broken off, snap arm cracked, rail channel jammed). The unit will generate a return if shipped. Reprint costs: $1.78 COGS. Not reprinting costs: $8.40 + review risk. Reprint every functional failure without hesitation.

**Defect rate target**: ≤5% of units printed. If dry run reveals a higher defect rate, stop and investigate — likely a print settings issue (temperature, first-layer adhesion, or FDM_TOLERANCE requiring adjustment).

---

## Phase 7: Dry Run Photo Documentation

Document each phase of the dry run with your phone camera. These photos serve two purposes: (a) a training record so you can onboard help later, and (b) content for Etsy listing photos showing the packing process (social proof that increases buyer confidence).

**Minimum documentation shots:**

1. QA station — parts laid out before packing (top-down view)
2. Packing table — one order in progress (mailer open, parts being placed)
3. Sealed mailers with labels applied (stack of 10, labels visible)
4. Brother QL-800 printing a label (optional but good process documentation)

These photos do not need editing. They are reference photos, not marketing photos.

---

## Dry Run Completion Checklist

After completing all phases, verify:

- [ ] 10 units packed and labeled (or as many as test-print parts allow)
- [ ] Cost tracking spreadsheet filled in with actual figures
- [ ] Labor time log complete
- [ ] Defect log: how many reprints required, and why
- [ ] Label pipeline tested: Shippo + Brother QL-800 (or fallback documented)
- [ ] Shipping cost validated against cost tracking table
- [ ] Thank-you card insert template printed and tested (fits in mailer, legible)
- [ ] Margin per unit calculated and compared to target

**Decision gate**: If actual all-in margin is below 55%, pause and investigate. Either COGS is higher than modeled, or shipping costs are running above Zone 4 average. Fix before scaling.

If margin is 60%+ all-in, proceed. The model is validated. You are ready for live orders.
