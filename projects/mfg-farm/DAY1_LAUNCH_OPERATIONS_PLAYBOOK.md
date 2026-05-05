---
title: ModRun Day 1 Launch Operations Playbook
date: 2026-05-05
version: 2.0
status: ready-for-execution
confidence: high
related:
  - post-test-print-launch-prep.md
  - fulfillment-workflow.md
  - etsy-shop-launch-kit.md
  - cost-model-spreadsheet.csv
  - cadquery/modrun_clip_b123d.py
  - cadquery/modrun_rail_b123d.py
---

# ModRun Day 1 Launch Operations Playbook

**Trigger**: Execute immediately upon test print go-decision (all Phase 1 criteria met per post-test-print-launch-prep.md)
**Scope**: Everything required to go from "test print passed" to "first order shipped" — and sustain daily operations thereafter
**Target Timeline**: Day 0 (go-decision) through Day 7 (first orders shipped and post-ship follow-up initiated)
**Estimated Setup Time**: 5–6 hours across Days 0–1, then 20–30 minutes per day ongoing

---

## Design Philosophy

This playbook has one job: eliminate improvisation. Every section is a checklist, a procedure, or a decision tree. Nothing here requires you to research or judgment-call in the moment. The research phase is complete. This is execution.

Read the whole document once before starting. Then work section by section. Do not skip gates.

---

## Part 1: Pre-Launch Checklist

**Complete before publishing any Etsy listing. Estimated total: 5–6 hours across Days 0–1.**

All tasks are grouped into tracks that can run in parallel. Tracks A and B can overlap; Track C can start immediately and run in the background.

---

### Track A — Design Finalization and Print Settings (Day 0, ~2 hours)

This track closes the loop between the test print result and the production files.

**A-1: Document test print results**

Run one modrun_clip (6mm bore) and one modrun_rail (desk_clamp variant) at production settings before doing anything else:

| Parameter | Production value |
|---|---|
| Nozzle temp | 210–215°C |
| Bed temp | 60°C (PEI plate) |
| Layer height | 0.20mm |
| Infill | 15% gyroid |
| Perimeter speed | 200mm/s |
| Supports | None |
| Material | eSUN PLA+ (or in-stock equivalent) |

Measure the printed parts with digital calipers and record:

| Measurement | Target | Actual | Pass/Fail |
|---|---|---|---|
| Clip engagement width | CAD spec ±0.5mm | | |
| Rail channel width | CAD spec ±0.5mm | | |
| Cable channel bore, 6mm clip | 6.0mm ±0.5mm | | |
| Snap arm thickness | 1.4mm (SNAP_ARM_THICKNESS) | | |
| Snap nub height | 1.2mm (SNAP_NUB_HEIGHT) | | |
| Nub recess depth in rail | 1.4mm (NUB_RECESS_DEPTH) | | |

Snap engagement quality (circle one): Too tight — Correct — Too loose — Does not engage

Surface finish (circle one): Excellent — Acceptable (light layer lines) — Unacceptable

Warping at base (circle one): None — Minor (<1mm) — Unacceptable (>2mm)

- [ ] All measurements recorded and documented

**A-2: Adjust FDM_TOLERANCE if needed**

Both scripts share the same default constant:

```
FDM_TOLERANCE = 0.15  # mm — added clearance each side
```

This is the primary dial for clip-to-rail fit. Adjustment rules:

| Symptom | Diagnosis | Adjustment |
|---|---|---|
| Clip requires significant force to engage | Clip is oversized — tolerance too low | Increase FDM_TOLERANCE by 0.05mm |
| Clip seats but snaps out under gentle pull | Tolerance correct but nub too small | Increase SNAP_NUB_HEIGHT by 0.1mm in clip script |
| Clip falls off without any pull force | Clip is undersized — tolerance too high | Decrease FDM_TOLERANCE by 0.05mm |
| Nub does not engage at all | Recess depth mismatched | Increase NUB_RECESS_DEPTH by 0.1mm in rail script |
| Cable too tight in bore | Bore gap ratio too narrow | Increase BORE_GAP_RATIO by 0.05 in clip script (default 0.65) |

**Threshold for acceptable fit**: Clip should engage with approximately the same force as pressing a key cap onto a keyboard switch — firm, audible click, no rattle. If two grown adults would disagree on whether the fit is tight or loose, it is within tolerance. If anyone would agree it is wrong, adjust.

The 0.05mm increment is intentional — FDM printers typically cannot reproduce anything smaller, so finer adjustments are noise.

- [ ] FDM_TOLERANCE (and any other constants) updated in both scripts if needed
- [ ] If no adjustment needed: note "Test print validated — FDM_TOLERANCE 0.15mm production-ready"

**A-3: Regenerate STL files (if adjustments were made)**

```bash
cd projects/mfg-farm/cadquery
python modrun_clip_b123d.py --output-dir ../stl/
python modrun_rail_b123d.py --output-dir ../stl/
```

- [ ] STL files verified in `projects/mfg-farm/stl/`
- [ ] At least one STL opened in Bambu Studio (drag-and-drop) to confirm no mesh errors, missing faces, or non-manifold warnings

**A-4: Lock production settings card**

Write these down and tape them next to the printer. Do not rely on memory.

```
MODRUN PRODUCTION SETTINGS — PLA+
================================
Nozzle: _____°C      Bed: _____°C
Layer height: 0.20mm
Infill: 15% gyroid
Perimeter speed: 200mm/s
Supports: NONE

Plate capacity — clips: _____ units (~90 min)
Plate capacity — rails: _____ units (~80–180 min)
FDM_TOLERANCE confirmed: _____ mm
Material in use: _____ (brand, color, lot)
Settings confirmed: _____ (date)
```

- [ ] Settings card physically posted at printer

---

### Track B — Etsy Listing Finalization (Day 0–1, ~1.5 hours)

**B-1: Photo prioritization and preparation**

You need at minimum 2 photos to publish a listing; 5 is the Etsy algorithm target. Plan to shoot all photos in one 45-minute session with the test print parts.

**Photo priority ranking by conversion impact** (highest first):

1. **Lifestyle shot** — rail mounted or propped on a desk edge, 2–3 cables routed through clips, shot from slightly above. This is the single highest-converting photo type on Etsy for functional accessories. Use it as the thumbnail if you can only choose one.
2. **Hero shot** — clip alone, angled, white background. Shows snap arm and cable bore geometry. Best as listing thumbnail if lifestyle shot is not ready on Day 0.
3. **Assembly shot** — clip snapped into rail at 45-degree camera angle. Proves the system works.
4. **Cable-in-clip shot** — a real USB-C or HDMI cable seated in the clip. Shows functional scale.
5. **Scale reference** — clip next to a common object (pen, coin). Eliminates the most common pre-purchase question.
6. **Multi-unit shot** — 3 clips on a rail, showing a full installed set.
7. **Material close-up** — extreme close-up of surface finish and snap nub detail.
8. **Rail hero** — rail alone, full length, angled to show slot geometry.

**Minimum viable launch set (2–3 photos)**: Hero shot (or lifestyle) + Assembly shot + Cable-in-clip shot.

**Equipment**: White foam-core board ($3) as background. Overcast window light or $20 ring light. Phone camera is sufficient. Resolution target: 2048×2048px minimum.

- [ ] Minimum 2 photos captured, transferred, and renamed clearly (e.g., `modrun_clip_hero.jpg`)
- [ ] Lifestyle shot captured if test print parts allow (will dramatically improve conversion rate from Day 1)

**B-2: Review and finalize listing copy**

Before publishing, verify against `etsy-shop-launch-kit.md`:

- [ ] Title includes primary keywords: "cable clips," "cable management," "3D printed," "modular," "desk"
- [ ] Description includes the 30-day satisfaction guarantee language
- [ ] Description includes "original parametric design" language (required for Etsy Creativity Standards compliance)
- [ ] All 13 tags are loaded, prioritized by search volume: cable clips, cable management, desk organizer, 3d printed, cable organizer, desk accessories, home office, workspace, office organization, cable holder, 3d print gift, desk cable clips, modular cable
- [ ] Variants configured correctly: Material (PLA+ / PETG Pro) × Color (Black / White / Grey)
- [ ] Copy does not conflict with test print results — if snap requires more force than expected, remove any "effortless" language from installation description

**B-3: Set pricing**

Reference from `cost-model-spreadsheet.csv` at 20 units/week throughput (blended COGS: $6.77/unit):

| SKU | Price | Gross Margin |
|---|---|---|
| Basic Clips (3-pack) | $22.99 | ~58–60% |
| Rail System (single) | $12.99 | ~62% |
| Starter Bundle (rail + 3 clips) | $28.99 | ~65% |
| Launch promo — Starter Bundle | $24.99 (first 30 days) | ~58% — drives first reviews |

Do not make single clips your primary SKU at $8.99. USPS Ground Advantage at $3.85–5.09 consumes 43–57% of that price before any COGS. The 3-pack is the minimum viable order unit.

- [ ] All listing prices verified against margin targets above

**B-4: Configure shipping profile**

In Etsy Shop Manager → Settings → Shipping, create "Standard Domestic":

- Processing time: 2 business days
- Carrier: USPS, Calculated (Etsy calculates by customer ZIP)
- Representative weights:
  - Single clip: 0.22 lbs (3.5 oz product + mailer)
  - 3-pack clips: 0.44 lbs (7 oz product + mailer)
  - Single rail: 0.38 lbs (6 oz product + mailer)
  - Starter Bundle: 0.75 lbs (12 oz product + box)

- [ ] Shipping profile created and applied to all listing drafts
- [ ] Test the calculator: add one listing to your own cart and verify the shipping rate populates

**B-5: Pre-publish gate**

- [ ] All listing drafts have: photos uploaded, tags entered, pricing set, shipping profile applied
- [ ] Business bank account verified with Etsy (2–3 day verification after adding routing/account number — do not publish until complete or payouts will be held)
- [ ] Pirate Ship account created at pirateship.com and connected to Etsy store (Settings → Store Connections → Etsy → Authorize)

**Recommended publish time**: Thursday, 10 AM–2 PM. Etsy indexes new listings within 15–30 minutes. Thursday gives two full business days of organic visibility before weekend browsing traffic peaks.

---

### Track C — Inventory and Packaging Setup (Day 0–1, ~2 hours, can run in background)

**C-1: Print initial inventory batch**

Target: 20 QC-passed units on the shelf before listings go live.

Print schedule (single Bambu P1S, 16-hour operating window across Day 0–1):

| Session | Content | Approx. Print Time | Units |
|---|---|---|---|
| Session 1 | 8× clip, black, 6mm bore — full plate | ~90 min | 8 clips |
| Session 2 | 2× rail, black, desk_clamp | ~180 min | 2 rails |
| Session 3 | 8× clip, white, 6mm bore — full plate | ~90 min | 8 clips |
| Session 4 | 2× rail, white + 4× clip, grey | ~210 min | 2 rails + 4 clips |

Total: ~570 minutes (~9.5 hours print time). Run Session 1 immediately after test print validation while working on Track B.

- [ ] Initial batch printing started on Day 0
- [ ] At least 10 QC-passed units on shelf before listings go live

**C-2: Inventory tracking spreadsheet**

Create a Google Sheet titled "ModRun Inventory." Tabs: Inventory, Orders, Defect Log, Print Settings, Weekly Summary.

**Inventory tab columns**:

| Unit # | SKU | Print Date | Batch | QC Status | Status | Order # | Customer | Ship Date | Tracking # |
|---|---|---|---|---|---|---|---|---|---|

SKU format: `clip_pla_black_6mm`, `rail_pla_white_desk`, etc.

Status values: Ready / Fulfilling-[order#] / Shipped-[tracking] / Defective-[type]

- [ ] Spreadsheet created with all tabs and columns
- [ ] Initial batch units entered as they pass QC (status: "Ready")

**C-3: Order packaging materials**

Order immediately — Amazon Prime delivers in 2–5 days. Hold listings until packaging is in hand.

| Item | Source | Qty | Cost | Notes |
|---|---|---|---|---|
| Poly mailers 9×12" 2.5mil white | Shop4Mailers or Amazon | 500 units | ~$25 | Primary packaging |
| Packing tape 2" clear | Amazon | 6-pack | ~$12 | H-seal for boxes |
| Digital postal scale (0.1oz precision) | Amazon | 1 | ~$20 | Required for label accuracy |
| Crinkle paper fill | Amazon | 1 lb pack | ~$8 | $0.02/unit perceived-value add |
| Thank-you card stock (4×6" index cards) | Amazon or Staples | 50-sheet pack | ~$8 | Print at home in Canva |

**Total packaging startup cost: ~$73**

Optional but high-ROI early investment: Rollo X1040 thermal label printer (~$130). Eliminates ink costs and reduces label time from 3 minutes to under 1 minute per order. Not required for the first 20–30 orders.

- [ ] Packaging materials ordered
- [ ] Expected delivery date confirmed — if arriving after Day 3, hold listings until in hand

---

## Part 2: Fulfillment Standard Operating Procedure

**Target time per order: 10–14 minutes.** The largest component is print time (passive); active labor is 12–15 minutes per batch. This SOP governs every single order from placement through carrier handoff.

---

### Step 1: Order Received (2 minutes)

**Trigger**: Etsy email notification or Etsy Seller App push notification.

1. Open the order in Etsy Shop Manager. Note in inventory spreadsheet: Order #, customer last name, order timestamp, SKU(s) ordered.
2. Check finished goods shelf:
   - **Stock available**: Mark unit status "Fulfilling — [order #]." Proceed to Step 2.
   - **Stock not available**: Start a print job immediately. Send this message to the customer via Etsy Messages:
     > "Hi [Name], thank you for your order! We are printing your [product] now — it will ship within 1–2 business days. We'll send tracking as soon as it's on its way."
3. Verify address completeness. Check for: apartment/suite number, correct ZIP code format, no obvious truncation. If incomplete, message the customer before generating a label.

---

### Step 2: Quality Control — Pre-Pack Inspection (3 minutes per unit)

**Every unit ships through this gate. No exceptions.**

**Visual inspection (45 seconds)**:

- [ ] No layer delamination — hold under LED task light (CRI ≥90); check snap arm and thin walls specifically
- [ ] No warping at base — place on flat surface, should not rock
- [ ] No nozzle crash artifacts (gouges, blobs, surface tears)
- [ ] Surface finish commercially acceptable: light layer lines OK; stringing, rough texture, blobs = reject
- [ ] No color streaking from filament transition
- [ ] All edges smooth — no sharp burrs that could catch on a cable

**Functional test (60 seconds)**:

- [ ] Snap clip onto the dedicated reference rail (one non-sale rail kept at the packing station for this purpose)
- [ ] Cycle on and off 5 times: engagement must be firm, click audible, release clean
- [ ] Insert a 5mm cable (or pen) into the bore: must seat without binding
- [ ] Weigh on postal scale: must be within ±5g of the reference unit weight (establish reference on first production unit and record it in the Print Settings tab)

**If unit fails**:
1. Photograph immediately (automatic timestamp = defect log record)
2. Mark in spreadsheet: "Defective — [type]" (e.g., "Defective — layer separation at snap arm")
3. Pull next unit from ready shelf
4. If no backup: start print, notify customer (template above)
5. Set defective unit in labeled "SCRAP" bin — do not discard immediately; these are data

---

### Step 3: Packing (4–5 minutes per order)

**Gather materials before starting**:
- 9×12" poly mailer (single clips, 3-packs, single rails)
- Small corrugated box 8×6×4" (Starter Bundle — rail + clips)
- Crinkle paper
- Pre-printed thank-you card
- Packing tape

**Poly mailer sequence (single clips, 3-packs, single rails)**:
1. Wrap unit(s) in one layer of crinkle paper, fold over
2. Place in center of mailer
3. Place thank-you card face-up on top
4. Peel and press the self-adhesive strip from center outward — verify seal is complete at all edges

**Box sequence (Starter Bundle, multi-component kits)**:
1. One layer of crinkle paper in box bottom
2. Rail along one side; clips alongside with crinkle paper between components to prevent rattle
3. Thank-you card + printed installation guide (half-letter, folded in thirds)
4. Top layer of crinkle paper
5. Close and H-seal with packing tape: one strip center seam, one strip each end flap (3 pieces total)

**Thank-you card content** (design once in Canva, print as needed on 4×6" card stock):

```
Thank you for your ModRun order.

Assembly: Press clip into rail slot until you hear a click.
No glue or tools needed. Cables load from the side.

Questions? Message us on Etsy — we respond within 24 hours.
30-day satisfaction guarantee. Anything wrong, we make it right.

— ModRun
```

---

### Step 4: Labeling and Carrier Selection (3 minutes per order)

**Weigh the sealed package** on the postal scale. Reference weights:

| Package | Contents | Approx. Weight |
|---|---|---|
| Single clip, poly mailer | 1 clip + mailer | 3.5 oz |
| 3-pack clips, poly mailer | 3 clips + mailer | 7.0 oz |
| Single rail, poly mailer | 1 rail + mailer | 6.0 oz |
| Starter Bundle, small box | 1 rail + 3 clips + box | 12.0 oz |

**Carrier selection decision tree**:

| Package weight | Destination | Recommended carrier | Why |
|---|---|---|---|
| Under 13 oz (under 1 lb) | Any US address | **USPS Ground Advantage** | Cheapest tracked option for lightweight parcels; typically $3.85–5.09 |
| Under 13 oz, customer needs fast delivery | Within 500 miles | **USPS Priority Mail** | If Priority is <$1.50 more than Ground Advantage, upgrade — 1–3 days vs. 2–5 days; customers notice |
| 13 oz–5 lbs | Any US address | **USPS Ground Advantage** | Still cheaper than UPS Ground for most zones at this weight range |
| 5+ lbs (multi-unit bulk) | Any US address | **UPS Ground via Pirate Ship** | UPS Ground becomes competitive at 5+ lbs; compare rates at time of label purchase |

**USPS vs. UPS comparison for typical ModRun order weights**:

| Weight | USPS Ground Advantage | UPS Ground (Pirate Ship commercial) | Verdict |
|---|---|---|---|
| 3.5 oz (single clip) | $3.85–4.20 | $8.50–10.00 | USPS by wide margin |
| 7 oz (3-pack) | $4.10–4.80 | $8.50–10.00 | USPS by wide margin |
| 12 oz (Starter Bundle) | $4.80–5.40 | $8.50–10.50 | USPS by wide margin |
| 32 oz (bulk, 8+ clips) | $7.00–9.00 | $9.00–11.00 | USPS narrowly; compare at time of purchase |

**Conclusion**: Use USPS Ground Advantage for all standard orders. Only compare UPS if a single package exceeds 5 lbs (not expected at current SKU mix).

**Label generation in Pirate Ship**:
1. Log in → Ship → Import Orders → select Etsy store
2. All open unshipped orders appear with addresses pre-filled
3. Enter package weight from scale for each order
4. Select USPS Ground Advantage → Get Rates → Buy Label
5. Print all session labels as batch PDF
6. Affix label to largest face of package — no creases or bubbles over the barcode
7. If printing on plain paper: cover label with a strip of clear packing tape for moisture protection

**Carrier dropoff**:
- USPS Priority/Ground Advantage: Drop at any USPS location or schedule free USPS pickup at usps.com/pickup (next business day morning). Pickup becomes the high-leverage time saver once you have 3+ packages per day — eliminates a trip entirely.

**Update inventory spreadsheet**: Mark unit status "Shipped — [tracking#] — [date]". Enter tracking number and ship date.

If Pirate Ship "auto-mark as shipped" is enabled, Etsy auto-updates and sends tracking to the customer. If not enabled, manually mark as shipped in Etsy the same day — Etsy's on-time shipping metric is based on mark-as-shipped date, not USPS scan date.

---

### Step 5: Post-Shipment Follow-Up (2–3 minutes per order, Day 3–7)

**Day 3 after shipping**: Check USPS tracking. If "Delivered": no action. If "In Transit" and approaching Day 5 with no delivery scan:

> "Hi [Name], your ModRun order is on its way — tracking shows it's in transit and should arrive very soon. Tracking: [number]. Let us know if anything comes up!"

**Day 7 after shipping** (if no review posted yet — use template from Part 4):

Send the review request template. This single touchpoint is the highest-ROI 2 minutes in the customer lifecycle.

---

### Cost Tracking — Per Order

Log these fields in the Orders tab of your Google Sheet immediately after shipping:

| Column | What to enter |
|---|---|
| Order ID | Etsy order number |
| SKU | Product and variant |
| Print Time (min) | Actual print time from slicer readout |
| Material Cost ($) | Units × $0.42 (or actual filament cost/g × grams) |
| Packaging Cost ($) | Mailer $0.08 + crinkle $0.02 + tape $0.01 + card $0.05 = $0.16 typical |
| Shipping Cost ($) | Actual Pirate Ship label cost |
| Platform Fees ($) | Etsy transaction 6.5% + payment processing ~3% of sale price |
| Customer Price ($) | What customer paid |
| Gross Margin ($) | Customer Price − (Material + Packaging + Shipping + Platform Fees) |
| Gross Margin % | Gross Margin / Customer Price |

Review this tab weekly to catch any drift from model assumptions. The cost model projects $0.42 material, $0.20 packaging, $4.10 shipping, $1.62 platform fees at 20 units/week. If actual numbers diverge more than 10%, investigate before scaling.

---

### Time Audit — Labor Hours Per Unit

Validate this against your actual time in Week 1:

| Activity | Estimated Time | Notes |
|---|---|---|
| Print time | 11–25 min/clip; 80–180 min/rail | Passive — printer runs unattended |
| Post-processing | 1–2 min/unit | Support removal (none required with current settings), visual check |
| QC inspection | 2–3 min/unit | Visual + functional test |
| Packing | 3–4 min/unit | Wrapping, mailer, card, seal |
| Label generation | 1–2 min/order | Pirate Ship import + print |
| USPS dropoff (amortized) | 5 min / 3 orders | Batching reduces this to under 2 min/order |
| **Total active labor/unit** | **~10–13 min** | At 20 units/week = 3.3–4.3 hours/week |

At $15/hr opportunity cost and 11 minutes average active labor per unit, labor cost = $2.75/unit. The cost model assumes $0.38/unit at 20/week, which reflects 90-second active packaging time per batched order — **not** per unit. This is correct if you batch 3+ orders per session. Do not do one-at-a-time fulfillment after the first week.

**Batching rule**: Pack and ship in sessions of 3+ orders. Never make a single USPS trip for a single package unless an order is time-critical. Batching reduces per-order active time from ~13 minutes to ~8 minutes by eliminating setup overhead.

---

## Part 3: Quality Control Procedures

### Post-Test-Print Tolerance Validation

This section applies only on Day 0 when evaluating the test print. If the test print passed, record the confirmed parameters and move on.

**FDM_TOLERANCE calibration procedure**:

The default `FDM_TOLERANCE = 0.15` in both scripts adds 0.15mm of clearance on each side of the clip's engagement surfaces. At 0.15mm, the clip-to-rail fit should be snug but effortless. If the test print deviates:

- **Too tight (clip requires noticeable force)**: Your printer is running slightly oversized. Increase `FDM_TOLERANCE` to 0.20mm. Reprint one clip only. Evaluate.
- **Too loose (clip clicks in but wiggles perceptibly)**: Printer is undersizing. Decrease `FDM_TOLERANCE` to 0.10mm. Reprint and evaluate.
- **Snaps out under gentle horizontal pull**: Snap nub is too small relative to recess. Before adjusting tolerance, try increasing `SNAP_NUB_HEIGHT` in the clip script from 1.2mm to 1.3mm. This is the more targeted fix.
- **Cannot engage at all**: Check that `NUB_RECESS_DEPTH` in the rail script (default 1.4mm) is >= `SNAP_NUB_HEIGHT` in the clip script (default 1.2mm). They must not conflict.

**Snap arm evaluation from test print**:

The snap arm is 1.4mm thick (`SNAP_ARM_THICKNESS`). At 1.4mm in PLA+ with 0.20mm layer height (7 layers), you should see a stiff but flexible arm with no cracking after 5 engage/disengage cycles. Evaluation criteria:

- Arm springs back fully after deflection: correct
- Arm shows whitening or micro-cracking at root: too thin or material issue — increase to 1.5mm
- Arm requires so much force to deflect that engagement is difficult: too thick — decrease to 1.3mm (also check FDM_TOLERANCE first)

**Print settings confirmation**:

The following settings produce the test-print target. Do not deviate from confirmed values in production:

| Parameter | Nominal | Accept if | Reject if |
|---|---|---|---|
| Layer height | 0.20mm | 0.20mm exactly | Any other value — changes dimensional accuracy |
| Infill | 15% gyroid | 15–25% | Below 15% (structural risk at snap arm); above 25% (unnecessary) |
| Wall count | 3 perimeters | 3–4 | Below 3 (snap arm integrity risk) |
| Nozzle temp | 210–215°C | 210–220°C | Below 205°C (adhesion failure) or above 225°C (stringing) |
| Bed temp | 60°C | 58–63°C | Below 55°C (warping risk) |

---

### Ongoing QC — Per Unit (Every Unit, Every Batch)

**Visual inspection checklist**:

- [ ] No layer delamination (gaps between layers) — especially at snap arm root and body top edge
- [ ] No warping at base — unit sits flat, does not rock on flat surface
- [ ] No nozzle crash artifacts — no gouges, blobs, or surface tears
- [ ] Surface finish commercially acceptable — light layer lines accepted; stringing, rough texture, or blobs = reject
- [ ] No color inconsistency — no streaks from incomplete filament purge on color change
- [ ] All edges smooth — no burrs that could catch on cable insulation

**Functional test**:

- [ ] Clip snaps onto reference rail, cycles on/off 5 times — engagement firm, release clean
- [ ] Cable bore loads a 5mm cable (or equivalent pen) without binding
- [ ] Weight within ±5g of reference unit (established from first production batch)

**Dimensional spot-check (5 units per week, random selection)**:

Once per week, pull 5 random units from the finished goods shelf and measure with calipers:

- Clip engagement width vs. CAD spec (tolerance ±0.5mm)
- Cable bore diameter (tolerance ±0.5mm)
- Overall clip height (tolerance ±1.0mm)

Log in the Defect Log tab. If any dimension drifts beyond ±0.5mm across two consecutive spot-checks, investigate the printer (Z-offset drift, bed level, nozzle wear).

---

### Defect Classification and Response Protocol

**Defect categories**:

| Category | Examples | Customer risk | Response |
|---|---|---|---|
| **Cosmetic** | Light stringing, minor surface roughness, very slight color variation | Low — functional, looks OK | Do not ship if objectively noticeable; ship if minor and passes functional test |
| **Fit** | Clip too loose or too tight, bore grips cable but is stiff | Medium — product works but experience is poor | Do not ship; reprint; adjust parameters if systematic |
| **Structural** | Layer delamination, cracked snap arm, warped base | High — may fail in use | Never ship; mandatory reprint; photograph and log |

**Customer notification: which defects warrant proactive outreach?**

A unit that slips through QC and ships with a defect requires outreach based on type:

- **Cosmetic defect discovered after shipping**: Do not contact proactively. If customer messages about it, offer replacement or refund immediately.
- **Fit defect discovered after shipping**: Contact within 24 hours. Offer replacement. Do not wait for the customer to complain — if you know it shipped wrong, own it.
- **Structural defect discovered after shipping**: Contact within 2 hours. Offer immediate replacement at priority shipping and full refund option. This is the only category that warrants proactive escalation.

**Replacement/refund decision tree**:

```
Customer reports defect
    ↓
Is the defect cosmetic only (no functional impact)?
    YES → Offer 10% discount on next order OR replacement
    NO → Continue
    ↓
Is the defect a fit issue (loose/tight but still usable)?
    YES → Offer replacement at no charge (ship within 2 business days)
    NO → Continue
    ↓
Is the defect structural (broken, cracked, non-functional)?
    YES → Offer immediate choice: full refund (no return) OR replacement (priority shipping)
        → Never ask customer to return a broken plastic part ($0.42 material cost; not worth the friction)
```

**Cost-benefit for replacement vs. refund**:

- Material cost per unit: $0.42
- Replacement shipping cost: $3.85–5.09 (USPS Ground Advantage)
- Total replacement cost: ~$4.50–5.50
- Full order revenue at stake: $22.99–28.99
- **Decision rule**: Always offer replacement as primary option. Replacement preserves the review opportunity and costs $4.50–5.50 vs. losing $22.99–28.99 in revenue plus a potential negative review.

**Defect documentation**:

Every defect gets:
1. Photo (phone, automatic timestamp)
2. Entry in Defect Log tab: date, unit #, print session, defect type, root cause hypothesis, action taken, photo filename

**Defect rate targets**:
- Critical defects (structural): <1% of all units printed
- All defects: <5% in Month 1; <3% by Month 2
- If any single week exceeds 5%: pause production, diagnose before resuming

---

## Part 4: Customer Service Templates

All templates are copy-paste ready. Personalize the customer name and bracketed fields. Keep responses under 150 words — Etsy customers convert at higher review rates with concise, warm messages over formal prose.

---

**Shipping Notification** — send manually when you mark the order shipped (Etsy sends the auto-tracking email, but a personal message materially improves review rate):

> Hi [Name],
>
> Your ModRun cable management system is packed and on its way.
>
> Tracking: [TRACKING NUMBER]
> Carrier: USPS Ground Advantage
> Expected arrival: [DATE — typically 2–5 business days from today]
>
> Assembly tip: press each clip into a rail slot from above until you feel a click. No tools needed. Cables load from the side.
>
> Any questions, just reply here — I respond within 24 hours.
>
> Thanks for the order.

---

**Delivery Confirmation Check-In** — send 1–2 days after expected delivery if no review and no issues reported:

> Hi [Name], hope everything arrived and your cables are staying put!
>
> If you have a moment, a review on Etsy makes a real difference for a small shop — it helps other people with the same cable problem find us.
>
> And if anything isn't quite right with your order, let me know — I'll make it right, no questions.

---

**Return Request Handling** — respond within 4 hours during business hours, 24 hours maximum:

First, diagnose root cause before responding:

| Customer says | Likely root cause | Response path |
|---|---|---|
| "It broke" | Structural defect — snap arm or body | Replacement or full refund, no return required |
| "It doesn't fit my rail" | Wrong bore size selected, or wrong variant | Clarify which bore size they need; send correct replacement |
| "The fit is too loose/tight" | Tolerance mismatch or FDM_TOLERANCE needs adjustment | Replacement from next corrected batch |
| "Changed my mind" | Buyer preference | Politely note print-on-demand policy; offer store credit as gesture |

Template response to return requests:

> Hi [Name], I'm sorry this isn't working for you — let me fix it.
>
> Can you tell me a bit more about what's happening? [Describe the specific issue or attach a photo if it helps.] That way I can make sure whatever I send next is exactly right.
>
> In the meantime: if you'd prefer a full refund, I can process that today with no return required. Just say the word.

---

**Feedback Request** — send 7–10 days after confirmed delivery (after customer has had time to use the product):

> Hi [Name], hope the ModRun system has been working well for you.
>
> If you're happy with it, a quick review on Etsy would really help — it only takes a minute and it makes a big difference for a small operation.
>
> And if there's anything you'd change or improve, I'd genuinely like to know — I iterate on the design based on real feedback.
>
> Thanks either way.

**On review incentives and Etsy policy**: Etsy's policies prohibit offering compensation (including discount codes) in exchange for a review. You may offer a discount as a gesture of goodwill for a customer who had a poor experience — that is distinct from attaching a discount to a positive review request. Do not send discount codes alongside review requests. The templates above comply with current policy.

---

**Proactive Delay Notice** — send if you cannot ship within your stated 2-business-day window:

> Hi [Name], just a heads-up — your order is printing now and will ship within [X] business days (slightly later than our usual window). I wanted to let you know proactively.
>
> Tracking will be sent as soon as it ships. Thank you for your patience — we make sure everything is right before it goes out.

---

**Negative Feedback Response** — respond within 4 hours; 24 hours maximum:

> Hi [Name], I'm sorry about [SPECIFIC ISSUE]. That's not what I want your experience to be.
>
> Two options — you choose:
>
> Option 1: I'll send a replacement at no charge. It will go out within 2 business days.
>
> Option 2: Full refund today, no return required.
>
> If you're open to sharing a photo of the issue, it helps me improve the product — but there's no obligation.
>
> What would you prefer?

---

## Part 5: Daily and Weekly Operations Calendar

### Daily Routine (20–30 minutes/day at 1–5 orders/day)

**08:00 — Check overnight print status** (5 minutes)
- Remove completed parts from printer bed
- Log completed units in inventory spreadsheet (status: "Ready" pending QC)
- If print failed mid-job: restart the job before anything else; log the failure in Defect Log

**08:30 — Post-processing** (5 minutes)
- Visual inspection of overnight batch
- Functional test of snap engagement (reference rail at packing station)
- Units that pass QC: move to finished goods shelf
- Units that fail: move to SCRAP bin, photograph, log, start reprint

**09:00 — Fulfill pending orders** (10–15 minutes per 3-order batch)
- Check Etsy Orders for any new orders since last check
- For all orders with stock available:
  - Pack packages (Step 3 SOP above)
  - Generate Pirate Ship labels as batch
  - Seal and stack for carrier

**12:00 — Start next print batch** (5 minutes setup, then passive)
- Load STL files into Bambu Studio
- Verify print settings match production standard card
- Start print job and leave it running

**16:00 — Check Etsy orders and prepare shipping** (5 minutes)
- Catch any orders that arrived since 09:00
- Generate any remaining labels
- Stack packages with morning batch for combined dropoff

**17:00 — USPS handoff** (15 minutes including transit time)
- Drop all packages at nearest USPS location
- Alternative: schedule USPS pickup at usps.com/pickup (free; activates for next business day morning — set this up once you have 3+ packages per day)
- Update inventory spreadsheet: shipped units and tracking numbers
- Mark orders as shipped in Etsy (if Pirate Ship auto-sync has not done it)

**Evening — Start overnight print** (5 minutes setup)
- Load a full plate of the most in-demand SKU
- Start print
- The printer runs unattended; modern Bambu P1S with AMS has reliable auto-resume
- Check filament level before starting any job over 2 hours

**Total active time at 1–3 orders per day**: 20–30 minutes (excluding print monitoring, which is passive).

---

### Weekly Routine (30 minutes, Friday evening or Monday morning)

**Inventory review**:
- Count finished goods by SKU. Reorder triggers:
  - Black clips: reorder if fewer than 8 units on shelf
  - White clips: reorder if fewer than 8 units on shelf
  - Rails (any color): reorder if fewer than 3 units on shelf
  - Any SKU under 5 units: add to this week's print schedule as priority

**Cost tracking review**:
- Tally the Orders tab for the week: total revenue, total material, packaging, shipping, platform fees
- Calculate actual gross margin vs. model (72–73% target at 20 units/week)
- If actual margin is more than 5 points below model: identify which cost category is driving the variance (usually shipping — check actual Pirate Ship costs vs. $4.10 model assumption)

**Print count and production metrics**:
- Units produced this week
- Units QC-passed vs. total printed (defect rate)
- Print time vs. estimated (validate slicer estimates against actual job times)
- Any filament changes — update material cost if switching suppliers

**Etsy performance review**:
- Total orders received this week
- Etsy Stats: views, click-through rate by listing, conversion rate (orders / views)
- Which tags drove impressions (visible in Etsy Ads if running)
- Which listings are generating traffic and which are stagnant

**Customer feedback review**:
- Any new reviews — save positive quotes to a "Review Quotes" note for future listing copy updates
- Any open messages or complaints — resolve before the week closes
- Defect log: did any defect type appear more than once? If yes, schedule a 5-unit test batch next week to validate a fix

**Filament inventory check**:
- Current stock on hand (kg)
- Expected consumption next week (units × 0.075 kg/unit blended)
- If under 2 weeks of supply: order eSUN PLA+ 10kg bundle (ASIN B0G2KSS613 black, equivalent for white) immediately. At $12/kg and 6kg/month consumption at 20/week, a 10kg case covers 5–6 weeks.

---

### Post-First-Week Review Checklist (End of Day 7)

Run this review after the first full week of live listings. Be honest — this is calibration data, not a grade.

**Visibility**:
- [ ] How many views did each listing receive?
- [ ] If under 50 views per listing in 7 days: SEO problem — revisit tags using eRank.com free tier; compare your tags to top-ranking results for "cable management" and "cable clips"
- [ ] If over 50 views but no orders: photo or pricing problem — try the lifestyle shot as thumbnail if not already; consider 15% discount on Starter Bundle for 30 days

**Conversion**:
- [ ] What was the view-to-order conversion rate? (Orders / Views)
- [ ] Etsy typical range: 1–3%. Under 1%: photo or price issue. Over 3%: listing is performing — scale traffic
- [ ] Did any listing generate favorites but no orders? Favorites are purchase intent — follow up on them later (Etsy does not let you message people who favorite but do not buy; this is just data)

**Defect rate**:
- [ ] Total units printed vs. QC-passed
- [ ] If defect rate over 5% in Week 1: this is expected during initial calibration. Identify the dominant defect type and adjust before Week 2

**Fulfillment**:
- [ ] All orders shipped within 2 business days?
- [ ] Actual time per order batch (log this): is it within the 10–14 minute estimate?
- [ ] Packaging cost per unit: actual vs. $0.16 model assumption

**Month 1 milestones**:

| Week | Target | Decision if not met |
|---|---|---|
| Week 1 | Launch live; 2–5 orders received | If zero orders by Day 5: check listing visibility, share with 5–10 potential buyers |
| Week 2 | Fulfill all Week 1 orders; refine packing process; identify top SKU | If defect rate >5%: pause, diagnose, reprint test batch before continuing |
| Week 3 | 5–10 cumulative orders; first review received; optimize print settings if needed | If no reviews: send review request template to all shipped orders |
| Week 4 | Evaluate performance; decide on scaling (new SKUs, Etsy Ads budget increase, second printer planning) | If under 5 cumulative orders: hold scaling; focus on SEO and photos before adding production capacity |

---

## Part 6: Quick Reference Checklists

These are designed to be printed and posted at the packing station. Reference them for every fulfillment cycle until the procedure is automatic.

---

### Quick Reference: Pre-Print Checklist

```
PRE-PRINT — run before every batch
[ ] STL files confirmed in slicer (correct variant, correct bore size)
[ ] Print settings match production standard card (nozzle, bed, layer, infill)
[ ] Filament loaded and correct color confirmed
[ ] Bed clean (wipe PEI with IPA if it has been more than 3 prints since last clean)
[ ] AMS filament levels sufficient for the job
[ ] First layer adhesion confirmed on start — watch the first 2 minutes
```

---

### Quick Reference: Post-Print QC Checklist

```
POST-PRINT QC — every unit, every time
[ ] No layer delamination at snap arm or walls
[ ] No warping (place flat, check for rocking)
[ ] No crash artifacts (blobs, gouges)
[ ] Surface finish acceptable (light layer lines OK; stringing/roughness = reject)
[ ] Snaps onto reference rail — firm click, clean release (5 cycles)
[ ] Cable bore loads 5mm cable without binding
[ ] Weight within ±5g of reference unit
PASS → move to finished goods shelf
FAIL → photograph, log in Defect Log tab, set in SCRAP bin
```

---

### Quick Reference: Pack and Ship Checklist

```
PACK AND SHIP — per order
[ ] Order # and SKU confirmed from inventory spreadsheet
[ ] Unit pulled from finished goods shelf — unit # noted in spreadsheet
[ ] Crinkle wrap applied
[ ] Unit placed in mailer or box
[ ] Thank-you card included
[ ] Mailer sealed (verify all edges) OR box H-sealed (3 strips tape)
[ ] Package weighed on postal scale — weight recorded
[ ] Pirate Ship label generated (correct address, correct weight)
[ ] Label affixed — flat, no creases over barcode
[ ] Inventory spreadsheet updated: status "Shipped — [tracking] — [date]"
[ ] Etsy order marked as shipped (verify auto-sync or mark manually)
```

---

### Cost Tracking Spreadsheet — Full Column Reference

Create this as the "Orders" tab in your Google Sheet. One row per order.

| Column | Data to enter | Example |
|---|---|---|
| Order ID | Etsy order number | 3291847561 |
| Date | Order date | 2026-05-08 |
| SKU | Product and variant | starter_bundle_black |
| Units | Number of units in order | 1 |
| Print Time (min) | Actual slicer print time | 90 |
| Material Cost ($) | Units × grams × $/gram | $0.84 |
| Packaging Cost ($) | Mailer + fill + card + tape | $0.16 |
| Shipping Cost ($) | Actual Pirate Ship label cost | $5.09 |
| Platform Fees ($) | Etsy 6.5% + ~3% payment | $2.72 |
| Customer Price ($) | What customer paid | $28.99 |
| Gross Margin ($) | Price − (Material + Pkg + Ship + Fees) | $20.18 |
| Gross Margin % | Gross Margin / Price | 69.6% |
| Notes | Anything abnormal | e.g., "delay — reprint" |

**Weekly summary row**: Sum Material, Packaging, Shipping, Fees. Compare to weekly revenue. Gross margin should track to 72–73% at 20 units/week (model basis). Flag any week below 65%.

---

### Daily Operations Checklist (copy-paste into calendar)

```
MODRUN DAILY OPS
================
AM
[ ] 08:00 — Check overnight print; remove completed parts
[ ] 08:30 — QC batch; move passes to shelf; log fails; reprint if needed
[ ] 09:00 — Fulfill all pending orders (pack, label, seal)
[ ] 12:00 — Start next print batch

PM
[ ] 16:00 — Check Etsy for new orders; generate any remaining labels
[ ] 17:00 — USPS dropoff (or confirm pickup scheduled)
[ ] 17:15 — Update inventory spreadsheet (shipped status + tracking)
[ ] 17:20 — Mark shipped orders in Etsy

Evening
[ ] Start overnight print if printer can run unattended
[ ] Check filament level before starting any job >2 hours
```

---

### Supplier and Platform Quick Reference

| Supplier/Service | What for | Where | Cost |
|---|---|---|---|
| eSUN PLA+ 10kg Black | Primary filament | Amazon ASIN B0G2KSS613 | ~$110–130 |
| eSUN PLA+ 10kg White | Primary filament | Amazon (search eSUN white 10kg) | ~$110–130 |
| Anycubic 50kg pallet | Phase 2 bulk (Month 3+) | store.anycubic.com | $524.73 (~$10.49/kg) |
| Shop4Mailers 9×12" 500pk | Poly mailers | shop4mailers.com | ~$25 |
| Pirate Ship | USPS commercial rates | pirateship.com | No fees |
| eRank.com (free tier) | Etsy SEO tag research | erank.com | Free |
| Etsy Shop Manager | Orders, stats, listings | etsy.com/your/account | N/A |

---

**Playbook status**: Ready for immediate activation upon test print go-decision.
**Version**: 2.0
**Last updated**: 2026-05-05
**Next review**: End of Month 1 — validate actual defect rate, order volume, and COGS vs. model assumptions; update print settings card if tolerance adjustments were made post-launch.
