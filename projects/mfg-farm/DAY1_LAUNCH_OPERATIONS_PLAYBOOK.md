---
title: ModRun Day 1 Launch Operations Playbook
date: 2026-05-01
version: 1.0
status: ready-for-execution
confidence: high
related:
  - post-test-print-launch-prep.md
  - fulfillment-workflow.md
  - phase-2-supplier-research.md
  - pricing-strategy.md
  - cost-model-spreadsheet.csv
  - cadquery/modrun_clip_b123d.py
  - cadquery/modrun_rail_b123d.py
---

# ModRun Day 1 Launch Operations Playbook

**Trigger**: Execute immediately upon test print confirmation (go criteria met per post-test-print-launch-prep.md Phase 1)
**Scope**: Everything required to receive, fulfill, and support the first customer order — and sustain it
**Target Timeline**: Day 0 (test print go) through Day 7 (first orders shipped)
**Estimated Total Setup Time**: 5-6 hours across Days 0-1, then 15-30 minutes/day ongoing

---

## Why This Document Exists

The business plan, pricing model, supplier research, CadQuery models, and Etsy listing copy are complete. What has been missing is the operational layer — the specific, decision-free procedures that let you act immediately when an order arrives without improvising under pressure. This playbook closes that gap.

The design principle here is zero-friction execution. Every section is a checklist or a step-by-step procedure. Nothing requires judgment calls or research. The research has already been done; this document is the distillation.

---

## Part 1: Pre-Launch Checklist (Days 0-1)

All tasks here must be complete before the Etsy listing goes live. Estimated total: 5-6 hours across two days. Tasks are grouped by track so you can run tracks A and B in parallel where time allows.

---

### Track A — Design Finalization (Day 0, ~2 hours)

This track closes the loop between the test print and the production files.

**Step 1: Run the test print and document results**

- [ ] Print one modrun_clip (6mm bore) and one modrun_rail (desk_clamp variant) using production settings:
  - Nozzle: 210-215°C | Bed: 60°C | Layer height: 0.2mm | Infill: 15% gyroid | Speed: 200mm/s perimeter
  - Material: eSUN PLA+ Black (or equivalent in-stock PLA+)
- [ ] Photograph results against a white background: top view, side view, clip-in-rail assembly, close-up of snap nub engagement
- [ ] Measure critical dimensions with digital calipers:
  - Clip engagement width (target: CAD spec ±0.5mm)
  - Rail channel width (target: CAD spec ±0.5mm)
  - Cable channel diameter on 6mm bore clip (target: 6mm ±0.5mm)
- [ ] Document in a single note (can be a phone note or a new sheet in the Google Sheets tracker):
  - Measured vs. target for each dimension
  - Snap engagement quality: too tight / correct / too loose
  - Surface finish quality: acceptable / unacceptable (reason)
  - Any warping: none / minor (<1mm) / unacceptable (>2mm)

**Step 2: Update CadQuery parameters if needed**

The primary adjustment point is `FDM_TOLERANCE` in both scripts. Both files share the same default:

```python
FDM_TOLERANCE = 0.15  # mm — added clearance each side
```

Adjustment rules based on test print:
- Clip too tight in rail (requires force): increase `FDM_TOLERANCE` by 0.05mm increments
- Clip too loose (falls out of rail): decrease `FDM_TOLERANCE` by 0.05mm increments
- Snap nub not engaging: check `SNAP_NUB_HEIGHT` in `modrun_clip_b123d.py` (default 1.2mm) and `NUB_RECESS_DEPTH` in `modrun_rail_b123d.py` (default 1.4mm)
- Cable too tight in bore: increase bore diameter in clip script (`bore_diameter` argument); the bore gap ratio `BORE_GAP_RATIO` (default 0.65) controls how wide the side opening is

- [ ] Open `projects/mfg-farm/cadquery/modrun_clip_b123d.py` and `modrun_rail_b123d.py`, update constants as determined above
- [ ] Save both files

**Step 3: Re-generate STL files**

```bash
cd projects/mfg-farm/cadquery
python modrun_clip_b123d.py --output-dir ../stl/
python modrun_rail_b123d.py --output-dir ../stl/
```

If the test print required no tolerance adjustments, skip this step — the existing STL files are production-ready.

- [ ] Verify STL files were written to `projects/mfg-farm/stl/`
- [ ] Open at least one STL in a preview tool (Bambu Studio works — drag-and-drop) and confirm no mesh errors, missing faces, or non-manifold geometry

**Step 4: Lock in print settings as production standard**

Document the exact settings that produced the passing test print. Write them down and tape them next to the printer (or add to your Google Sheets tracker as a "Print Settings" tab):

| Parameter | Value |
|---|---|
| Material | (brand, grade, color) |
| Nozzle temp | °C |
| Bed temp | °C |
| Layer height | mm |
| Infill % | % |
| Infill pattern | gyroid |
| Perimeter speed | mm/s |
| Print time — single clip | min |
| Print time — single rail | min |
| Plate capacity — clips | units |
| Plate capacity — rails | units |
| Notes | any slicer-specific settings |

- [ ] Settings documented and physically posted near printer or in tracker

---

### Track B — Etsy Listing Finalization (Day 0-1, ~1.5 hours)

**Step 5: Product photography**

You need a minimum of 2 photos per listing to go live (5 is the algorithm-optimal number). Shoot all photos in one session — 30-45 minutes with basic setup.

Equipment: White foam-core board ($3 at dollar store) as background. Natural window light (overcast day is ideal) or a $20 ring light. Phone camera is sufficient (modern phone cameras outperform most compact cameras for product work).

Required shots (capture all 8 in one session; use across all listings):

1. **Hero shot** — clip alone, angled view on white background, shows snap arm and cable bore detail
2. **Rail hero** — rail alone, full length view, angled to show slot geometry
3. **Assembly shot** — clip snapped into rail at 45-degree camera angle, clearly shows the fit
4. **Cable in clip** — a real cable (USB-C or HDMI) seated in the clip, showing functional use
5. **Scale reference** — clip next to a common object (a pen, a coin) so customers understand the size
6. **Multi-unit** — 3 clips arranged on a rail, showing a complete installed set
7. **Lifestyle shot** — rail mounted on a desk edge (or propped to simulate) with 2-3 cables routed through clips, from slightly above. This is the highest-converting photo type on Etsy.
8. **Material close-up** — extreme close-up showing surface finish, layer lines, and snap nub detail

Resolution target: 2048×2048px minimum. Etsy compresses above this, so there is no benefit to shooting at 4K for the listing itself; shoot at max resolution and resize down.

- [ ] All 8 shots captured and transferred to computer
- [ ] 3-5 shots selected per listing (hero + lifestyle + 2-3 detail shots is the standard set)
- [ ] Photos renamed clearly (e.g., `modrun_clip_hero.jpg`, `modrun_rail_lifestyle.jpg`)

**Step 6: Review and finalize listing copy**

The listing copy from `pricing-strategy.md` covers all tier positioning and SEO tags. Before publishing:

- [ ] Confirm product description accurately reflects the test-print-validated product. If tolerance adjustments changed the fit characteristics (e.g., snap now requires less force), update any copy that references installation difficulty.
- [ ] Confirm the 30-day satisfaction guarantee language is in every description
- [ ] Confirm the "original parametric design" language is present (required for Etsy Creativity Standards compliance)
- [ ] Confirm tags are loaded. Priority tags by search volume (from `post-test-print-launch-prep.md` Section Phase 4): cable clips, cable management, desk organizer, 3d printed, cable organizer, desk accessories, home office, workspace, office organization. Add color and material tags (black, white, PLA, PETG) as variant-level tags.

**Step 7: Set pricing**

Reference from `cost-model-spreadsheet.csv` at 20/week throughput:
- Total COGS/unit: $6.77 (blended at this volume level)
- This includes $0.42 material, $0.38 labor, $0.20 packaging, $1.62 platform fees, $4.10 blended shipping

Launch price recommendation:
- Basic Clips (3-pack): **$22.99** — 58-60% gross margin at current COGS
- Rail System (single): **$12.99** — 62% gross margin
- Starter Bundle (rail + 3 clips): **$28.99** — 65% gross margin
- Optional launch promotion: 15% off Starter Bundle for first 30 days = **$24.99** (drives early reviews with minimal margin sacrifice)

Do not launch the single clip at $8.99 as a primary SKU. The shipping-to-price ratio at single clip orders is punishing: USPS Ground Advantage at $3.85-5.09 eats 43-57% of the $8.99 price before COGS. The 3-pack is the minimum viable unit.

- [ ] Prices set in each listing draft and verified against margin targets above

**Step 8: Configure shipping profile**

In Etsy Shop Manager → Settings → Shipping:

Create "Standard Domestic" shipping profile:
- Processing time: 2 business days
- Carrier: USPS
- Shipping type: Calculated (Etsy calculates rates by customer ZIP)
- Representative weight:
  - Single clip: 0.22 lbs (3.5 oz product + mailer)
  - 3-pack clips: 0.44 lbs (7 oz product + mailer)
  - Rail: 0.38 lbs (6 oz product + mailer)
  - Starter Bundle: 0.75 lbs (12 oz product + box)

- [ ] Shipping profile created and applied to all listing drafts
- [ ] Test the calculator: Add one listing to your own cart (as a test) and verify the shipping rate populates for your address

---

### Track C — Inventory and Supplier Setup (Day 0-1, ~2 hours)

**Step 9: Order initial print batch**

You need finished goods inventory before orders start arriving. Target: 20 units ready before publishing listings.

Print schedule for initial batch (single Bambu P1S, assume 16-hour operating window):

| Session | Content | Print Time | Units |
|---|---|---|---|
| Session 1 | 8x modrun_clip (black, 6mm bore) full plate | ~90 min | 8 clips |
| Session 2 | 2x modrun_rail (black, desk_clamp) | ~180 min | 2 rails |
| Session 3 | 8x modrun_clip (white, 6mm bore) full plate | ~90 min | 8 clips |
| Session 4 | 2x modrun_rail (white, desk_clamp) + 4x clip (grey) | ~210 min | 2 rails + 4 clips |

Total: 20 units, approximately 10-11 hours of print time. Run sessions across Day 0 and Day 1 while setting up the Etsy listing in parallel.

QC each session's output before storing (see Part 2, Step 2 below). Do not store units that fail QC — reprint immediately so you have accurate finished-goods counts.

- [ ] Initial batch printing started on Day 0
- [ ] At least 10 units QC-passed and on the shelf before listings go live

**Step 10: Set up inventory tracking spreadsheet**

Open Google Sheets. Create a new sheet titled "ModRun Inventory." Add these columns:

| Column | Purpose |
|---|---|
| Unit # | Auto-increment (1, 2, 3...) |
| SKU | e.g., `clip_pla_black_6mm` |
| Print date | Date printed |
| Print session | Which batch it came from |
| QC status | Pass / Fail — [defect type] |
| Status | Ready / Fulfilling — [order#] / Shipped — [tracking] / Defective |
| Order # | Etsy order number when assigned |
| Customer | Last name only |
| Ship date | Date package dropped at USPS |
| Tracking # | USPS tracking number |

Enter all initial batch units as rows when they come off the printer and pass QC.

- [ ] Spreadsheet created with all columns
- [ ] Initial batch units entered with status "Ready"

**Step 11: Order packaging materials**

Order immediately so materials arrive before your first orders ship. Estimated delivery: 2-5 days Amazon Prime.

| Item | Source | Qty | Approx. Cost | Notes |
|---|---|---|---|---|
| Poly mailers 9×12" 2.5mil white | Shop4Mailers or Amazon | 500 units | ~$25 | Primary packaging for all single and 3-pack orders |
| Packing tape 2" clear | Amazon | 6-pack | ~$12 | H-seal pattern on all boxes |
| Digital postal scale (0.1oz precision) | Amazon | 1 unit | ~$20 | Required for accurate Pirate Ship label weights |
| Crinkle paper / tissue wrap | Amazon | 1 lb pack | ~$8 | Optional — adds perceived value for $0.02/unit |
| Thank-you card stock (4×6" index cards or card-weight paper) | Amazon or Staples | 50-sheet pack | ~$8 | Print at home |

**Total packaging startup cost: ~$73**

A thermal label printer (Rollo X1040, ~$130) is a strong early investment — it eliminates ink costs and speeds up the label step from 3 minutes to under 1 minute per order. Not required for the first 20-30 orders, but plan for it.

- [ ] Packaging materials ordered
- [ ] Delivery date confirmed; if arriving after Day 3, note this and plan to hold listings until materials are in hand

**Step 12: Supplier onboarding (if outsourcing initial batches)**

If you are printing in-house on the Bambu P1S, skip this step. If you are placing an outsourced batch order:

Email primary supplier (eSUN via Amazon wholesale, or Anycubic direct) with the following:

Subject: Production inquiry — ModRun cable management — PLA, 20-unit initial batch

Body:
> We are preparing to launch a parametric cable management product (clips and rails) on Etsy. Initial production target is 20 units, with weekly sustaining orders of 20-50 units.
>
> Material specification: PLA+ 1.75mm, Black, White, Grey.
> Print settings: 0.2mm layer height, 15% gyroid infill, 210°C nozzle, 60°C bed.
> Files: STL files available to share upon inquiry.
>
> Requesting: (1) quote for 10kg PLA+ in Black + 10kg in White, (2) lead time, (3) availability of Net 30 terms.
>
> Monthly volume projection: 3-5 kg in Month 1, scaling to 20+ kg by Month 3.

- [ ] Supplier email sent (if outsourcing)
- [ ] eSUN Amazon ASIN B0G2KSS613 (black PLA Basic 10kg) verified in stock for immediate order

**Step 13: Create Pirate Ship account**

1. Go to pirateship.com, create free account
2. Add credit card as payment method
3. Connect Etsy store: Settings → Store Connections → Etsy → Authorize
4. Enable "Auto-mark as shipped" toggle in the Etsy integration settings
5. Print one test label (you can void it for free within 28 days if unused)

- [ ] Pirate Ship account created and Etsy integrated
- [ ] Test label printed to confirm the workflow

---

### Final Pre-Launch Gate

Before clicking Publish on any listing:

- [ ] At least 10 QC-passed units on the inventory shelf
- [ ] Packaging materials in hand (or in transit with confirmed 2-3 day arrival)
- [ ] All listing drafts have: photos uploaded, tags entered, pricing set, shipping profile applied
- [ ] Pirate Ship connected to Etsy
- [ ] Inventory tracking spreadsheet has initial stock entered
- [ ] Business bank account verified (Etsy needs bank for Payments; 2-3 day verification after adding routing/account number)

**Recommended publish day and time**: Thursday, between 10 AM and 2 PM. Etsy's algorithm indexes new listings within 15-30 minutes. Thursday gives the listing two full business days of organic visibility before the weekend, which is when Etsy sees highest browsing traffic.

---

## Part 2: Fulfillment Standard Operating Procedure

This SOP governs every order from placement through delivery confirmation. Target total time per order: 10-12 minutes.

---

### Step 1: Order Received (2 minutes)

Trigger: Etsy sends an email notification when an order is placed. If you have the Etsy Seller App installed on your phone, you will also receive a push notification.

Actions:
1. Open the order in Etsy Shop Manager (or the Etsy Seller App)
2. Note in the inventory tracking spreadsheet:
   - Order # (from Etsy)
   - Customer last name
   - Order timestamp
   - SKU(s) ordered
3. Check finished goods shelf: Is the required SKU and color available?
   - **Yes**: Mark unit status "Fulfilling — [order #]" in the spreadsheet. Proceed to Step 2.
   - **No**: You must print before shipping. Start a print job immediately, then send this message to the customer via Etsy Messages:

   > "Hi [Name], thank you for your order! We are printing your [product] now — it will be on its way within 1-2 business days. We appreciate your patience and will send tracking as soon as it ships."

4. Verify address completeness in the Etsy order. Check for apartment/suite number, correct ZIP code format, and legible street address. If anything looks incomplete, message the customer immediately: "Just confirming your delivery address — can you verify [specific detail]?"

---

### Step 2: Quality Control Check (3 minutes per unit)

Every unit ships through this gate. No exceptions.

**Visual inspection (30-45 seconds)**:
- Hold unit under good lighting (an LED task light with CRI ≥90 shows defects clearly)
- [ ] No layer delamination (look for gaps between layers, especially at thin walls and snap arm)
- [ ] No warping at base (place on flat surface — unit should not rock)
- [ ] No nozzle crash artifacts (gouges, blobs, surface tears)
- [ ] Surface finish is commercially acceptable (light layer lines: acceptable. Obvious roughness, stringing, or blobs: not acceptable)
- [ ] For PETG: No significant stringing visible (minor stringing can be trimmed with craft knife — note it in the batch log)
- [ ] Color consistent throughout (no streaks from filament transition)

**Functional test (60 seconds)**:
- [ ] Snap the clip onto the reference rail (keep one designated reference rail — not for sale — mounted near your packing area)
- [ ] Cycle on and off 5 times. The engagement should be firm but not require excessive force. Release should be clean.
- [ ] Insert a 5mm cable (or a pen of equivalent diameter) into the cable bore. Should seat without binding.
- [ ] Weight within ±5g of reference unit (use postal scale; weigh a known-good unit when you first establish the production run and note the reference weight)

**If a defect is found**:
1. Photograph it with your phone (automatic timestamp creates a record)
2. Mark unit in spreadsheet as "Defective — [defect type]" (e.g., "Defective — layer separation at snap arm")
3. Pull the next available unit from the ready shelf
4. If no backup unit is available, start a print job and notify the customer (as above)
5. Set defective units aside in a labeled bin ("SCRAP/REWORK") — do not throw them away immediately; they are data for your defect analysis

**If the unit passes**, mark it in the spreadsheet as "QC passed — [date]" and proceed to packing.

---

### Step 3: Packing (5 minutes per order)

**Gather materials**:
- 9×12" poly mailer (for single clips, 3-packs, single rails)
- Small corrugated box 8×6×4" (for Starter Bundle — rail + clips together)
- Crinkle paper or tissue wrap
- Thank-you card (pre-printed — see template in Part 4)
- Packing tape

**Packaging sequence**:

*For poly mailer orders (single clips, 3-packs, single rails)*:
1. Wrap the unit(s) in crinkle paper or tissue — one layer, fold it over
2. Place unit in center of mailer
3. Place thank-you card face-up on top of unit
4. Seal the self-adhesive strip on the mailer (press firmly from center outward)
5. Verify the seal is complete on all edges

*For box orders (Starter Bundle, any multi-component kit)*:
1. Place a single layer of crinkle paper in the bottom of the box
2. Place rail in the box, along one side
3. Nest clips alongside the rail with crinkle paper between components to prevent rattling
4. Place thank-you card and, for bundles, a printed installation instruction sheet (half-letter, folded in thirds — print template on demand from home printer)
5. Add a top layer of crinkle paper
6. Close box flaps and seal with packing tape in H-pattern (one strip across the center seam, one strip along each end flap — 3 pieces total)

**Thank-you card content** (print at home on card stock, 4×6" format, design once in Canva):
```
Thank you for your ModRun order.

Snap-fit assembly — no tools or adhesive needed.
Insert the rail into position, then press each clip into a slot
until you hear a click. Cables load from the side.

Questions? Message us on Etsy — we respond within 24 hours.
30-day satisfaction guarantee. Anything wrong, we make it right.

— ModRun
```

---

### Step 4: Labeling and Shipping (3 minutes per order)

1. Weigh the sealed package on the postal scale. Typical weights:
   - Single clip in mailer: ~3.5 oz
   - 3-pack clips in mailer: ~7 oz
   - Single rail in mailer: ~6 oz
   - Starter Bundle in box: ~12 oz

2. Log into Pirate Ship → Ship → Import Orders
3. Select your Etsy store → Import Orders (all open unshipped orders appear with addresses pre-filled)
4. For each order:
   - Enter the package weight (from your scale)
   - Select USPS Ground Advantage (default for under 1 lb; if Priority Mail is less than $1.50 more, upgrade — customers notice 1-3 day delivery vs. 2-5 day)
   - Click "Get Rates" and select the cheapest appropriate service
   - Click "Buy Label"
5. Print all labels for the session as a batch PDF

6. Affix label to package:
   - Smooth placement — no creases or bubbles over the barcode
   - Center the label on the largest face of the package
   - If printing on plain paper (not a thermal label), cover the label with a strip of clear packing tape to protect it from moisture

7. Drop packages at the nearest USPS location, or schedule a USPS pickup at usps.com/pickup (free; pickup happens the next business day morning). USPS pickup is the highest-leverage time saver in this workflow once you have 3+ packages shipping per day.

8. Update the inventory tracking spreadsheet:
   - Unit status: "Shipped — [tracking#] — [date]"
   - Enter tracking number and ship date in the order row

9. If Pirate Ship's "auto-mark as shipped" integration is enabled, Etsy will be updated automatically and the customer receives a tracking email. If not enabled, manually go to the Etsy order → Mark as Shipped → enter tracking number. Do this the same day as shipping — Etsy's on-time shipping rate metric is based on when you mark it shipped, not when USPS scans it.

---

### Step 5: Post-Shipment Follow-Up (1 minute per order, Day 3-5)

**Day 3 after shipping**: Check USPS tracking for the order (search the tracking number at usps.com or in the Etsy order page). If the tracking shows "Delivered," no action needed — the customer received it.

If tracking shows "In Transit" (normal) and no delivery scan by Day 5, send a brief message:

> "Hi [Name], your ModRun order is on its way — tracking shows it's in transit and should arrive very soon. Tracking: [number]. Let us know if anything comes up!"

This proactive check distinguishes you from most Etsy sellers and generates reviews.

**Day 7 after shipping** (if no review posted yet):

> "Hi [Name], hope your cables are staying organized! If you're happy with your ModRun system, we'd really appreciate a quick review on Etsy — it helps other cable-conscious buyers find us. Thank you either way!"

---

## Part 3: Quality Control and Defect Tracking

### Defect Log Setup

Create a tab in your Google Sheets tracker titled "Defect Log." Add these columns:

| Column | Purpose |
|---|---|
| Date | Date defect discovered |
| Unit # | Cross-references inventory sheet |
| Print session | Which batch produced this unit |
| Defect type | From the classification table below |
| Root cause hypothesis | Best guess at why it happened |
| Action taken | Scrapped / Reprinted / Adjusted settings |
| Photo filename | Timestamp-named photo from your phone |

**Defect classification**:

| Type | Description | Likely Cause | Action |
|---|---|---|---|
| Layer separation | Visible gaps between layers, especially at snap arm | Nozzle temp too low, print speed too high, wet filament | Adjust temp +5°C; check filament moisture |
| Snap fit too loose | Clip falls off rail under gentle pull | FDM_TOLERANCE too high — clip is undersized | Decrease FDM_TOLERANCE by 0.05mm, reprint test |
| Snap fit too tight | Clip requires significant force to engage | FDM_TOLERANCE too low — clip is oversized | Increase FDM_TOLERANCE by 0.05mm, reprint test |
| Warping | Base of part curved, part rocks on flat surface | Bed temp too low, ambient temperature, bed surface | Clean bed; increase bed temp; add brim (test only) |
| Stringing (PETG) | Fine strands between part features | Print temp too high, retraction settings | Lower temp by 5°C; increase retraction |
| Color streak | Color inconsistency across part | Recent filament change — inadequate purge | Purge more material on next color change; scrap this unit |
| Elephant's foot | First layer wider than designed | Bed too close (Z-offset calibration), bed temp too high | Recalibrate Z-offset; lower bed temp by 3°C |
| Incomplete print | Part truncated mid-height | Power interruption, filament runout, AMS failure | Check filament level before long jobs; enable auto-resume if available |

**Defect rate targets**:
- Critical defects (snap fit failure, layer separation): <1% of all units printed
- All defects combined: <5% through Month 1; target <3% by Month 2
- If defect rate exceeds 5% in any single week: pause production, diagnose, and fix before resuming

**Monthly defect review (30 minutes)**:

At the end of each month, review the defect log and calculate:
1. Defect rate by type (which type is most frequent?)
2. Defect rate by print session (is one printer or time-of-day producing more defects?)
3. Any trend in frequency (increasing or decreasing week over week?)
4. Cost of defects: units wasted × $0.42 material cost + labor time to reprint

If a defect type appears more than 3 times in a month, it is a systematic problem. Address it by adjusting the corresponding CadQuery parameter or print setting, printing a 5-unit test batch, verifying the fix, and then updating the production standard settings sheet.

---

## Part 4: Customer Service Templates

All templates below are copy-paste ready. Personalize the customer name and any bracketed fields. Keep responses under 150 words — Etsy customers respond better to concise, warm messages than to formal prose.

---

**Order Confirmation** — Etsy handles this automatically. No action required.

---

**Shipping Notification** — Send manually when you mark the order as shipped in Etsy. (Etsy sends the tracking auto-email, but a personal message improves the customer experience and review rate.)

> Hi [Name],
>
> Your ModRun cable management system is packed and on its way!
>
> Tracking: [TRACKING NUMBER]
> Expected arrival: [DATE — Ground Advantage typically 2-5 days from ship date]
>
> Quick tip: Insert the clip into the rail slot with a gentle downward press until you feel a click. No glue or tools needed. Questions? Just reply here — I respond within 24 hours.
>
> Thanks for the order!

---

**Delivery Check-In** — Send Day 7 if no review and no issues reported:

> Hi [Name], hope the ModRun system is working well for your setup! If you have a moment, a review on Etsy would mean a lot — it helps other folks with cable chaos find us.
>
> And if anything isn't perfect with your order, let me know directly — I'm happy to make it right.

---

**Proactive Delay Notice** — Send if you cannot ship within your stated 2-business-day window for any reason:

> Hi [Name], just a heads-up — your order is printing now and will ship within [X] business days (slightly later than our usual timeline). I wanted to let you know proactively so there are no surprises.
>
> Tracking will be sent as soon as it ships. Thank you for your patience — we're making sure it's exactly right before it goes out.

---

**Negative Feedback Response** — For any report of defect, poor fit, or customer dissatisfaction. Respond within 24 hours, ideally within 4 hours during business hours.

> Hi [Name], I'm really sorry to hear about [ISSUE]. That's not the experience I want you to have.
>
> Here are two options — you choose what works best for you:
>
> Option 1: I'll send a replacement at no charge and cover shipping. It will go out within 2 business days.
>
> Option 2: Full refund, no return required. I'll process it today.
>
> If you're open to sharing a photo of the issue, it helps me improve the product for future customers — but there's no obligation.
>
> What would you prefer?

---

**Positive Review Request** — After the Day 7 check-in above generates a response, or if a customer messages with praise:

> Thank you so much — that's great to hear! If you have a moment, leaving a quick review on Etsy would really help us grow. It only takes a minute and makes a big difference for a small operation like ours.
>
> [Etsy shop link or instruction: "Just go to your purchases and click 'Leave a review'"]
>
> Thanks again!

---

## Part 5: Daily and Weekly Operations Rhythm

### Daily Routine (15-30 minutes/day)

The goal is a predictable daily loop that you can complete without thinking:

**Morning (10 minutes)**:
1. Check email or Etsy Seller App for new orders from the past 24 hours
2. If 1-2 orders: Note them in the inventory spreadsheet and check finished goods shelf
3. If 3+ orders: Batch all orders together — you will pack and ship them in one session end-of-day
4. Check finished goods shelf against reorder triggers (see inventory section below)
5. Start any needed print jobs before leaving for other work

**Afternoon (10-15 minutes, 2-4 PM)**:
1. Harvest completed prints, run QC on each unit
2. For all orders with stock available: Pack packages, generate Pirate Ship labels
3. Drop at USPS or set packages by door for USPS pickup if scheduled

**Evening (2 minutes)**:
1. Mark all shipped orders in Etsy (if Pirate Ship auto-sync hasn't done it)
2. Update inventory spreadsheet with shipped units and tracking numbers
3. Start overnight print job if printer can run unattended (batch of same-color clips on a stable profile)

**Total daily time at 1-3 orders/day**: 20-30 minutes.

---

### Weekly Routine (30 minutes, Monday morning)

**Inventory review**:
- Count finished-goods units by SKU. Note any SKU below its reorder trigger:
  - Basic Clips (black, white): reorder trigger = fewer than 8 units
  - Rails: reorder trigger = fewer than 3 units
  - Any color: if under 5 units, add to this week's print schedule

**Defect log review**:
- Any defect type appearing more than once this week? If yes, add a root-cause note and schedule a 5-unit test batch to validate a fix.

**Sales velocity check**:
- How many orders shipped last week?
- What was the SKU and color mix?
- Is any SKU consistently outselling projections? (This is your signal to increase its buffer stock)

**Supplier check**:
- Is filament inventory sufficient for 2+ weeks of expected production?
- If under 2 weeks: Place eSUN Amazon order (B0G2KSS613 for black, equivalent ASIN for white). Target: 10kg case per color per month at 20/week throughput.
- At $12/kg (10kg eSUN bundle rate), 10kg = ~$120. At 75g per unit × 20/week × 4 weeks = 6kg/month. A 10kg case covers 5-6 weeks of production with buffer.

**Customer feedback review**:
- Read any new Etsy reviews and save positive quotes to a "Review Quotes" note (for use in future listing copy updates)
- Review any open Etsy messages and respond if not already addressed

---

### Monthly Routine (1 hour, first Monday of each month)

**COGS validation**:
- Pull last month's filament purchases from your records
- Calculate actual $/kg paid vs. the $12/kg assumption in the cost model
- If actual COGS is higher than model: Investigate supplier pricing and consider timing or vendor changes
- Check if monthly filament spend has crossed the $150 threshold (25+ kg/month). If yes, evaluate the Anycubic 50kg pallet deal at $10.49/kg ($524.73) — at 25kg/month this pays back in ~5 weeks of savings

**Performance metrics**:
- Total units shipped vs. monthly target
- Defect rate: units scrapped / units printed
- On-time shipping rate: orders shipped within 2 business days / total orders
- Average order value: revenue / order count
- Gross margin: (revenue - COGS) / revenue — compare to model targets

**CadQuery / design review**:
- Review defect log for any tolerance-related issues
- If snap fit complaints appear more than twice in the month, update FDM_TOLERANCE and regenerate STL files
- If any new cable diameter requests came in via customer messages, note them as candidates for new bore variants

**Supplier relationship update**:
- Once monthly sales reach 20-50 units, send eSUN a wholesale inquiry with your volume figures (see phase-2-supplier-research.md Section 5.1 for contact approach)
- Once monthly filament spend reaches $150+, place one Anycubic test order to validate their lead time and AMS compatibility with your P1S before committing to a 50kg order

---

## Part 6: Timeline and Success Metrics

### Week 1 Targets (Days 0-7 post-launch)

| Metric | Target | How to Measure |
|---|---|---|
| Listings published | All draft listings live | Etsy Shop Manager → Listings |
| Orders received | 2-5 (realistic for first week with no external traffic) | Etsy Orders tab |
| Units shipped | Equal to orders received | Inventory spreadsheet |
| On-time shipping rate | 100% (all orders shipped within 2 business days) | Compare order date vs. ship date |
| Defect rate | <5% (1 defect per 20 units) | Defect log |
| Customer satisfaction | Zero unresolved complaints | Etsy Messages |

**Week 1 is calibration, not growth.** The purpose is to prove the fulfillment SOP works end-to-end on real orders, catch any fit or quality issues before they generate reviews, and establish the daily operational rhythm.

If zero orders arrive in the first 5 days:
1. Check Etsy Stats → Views. If views are below 50 in 5 days, SEO is the issue — revisit tags using eRank.com free tier
2. If views are above 50 but no conversions, pricing or photos are the issue — try dropping the Starter Bundle 15% for 30 days to drive the first purchase
3. Share the listings with 5-10 people who might genuinely buy. Early Etsy purchases from real buyers (even friends) accelerate the algorithm's trust score

---

### Month 1 Targets (Days 0-30)

| Metric | Target | Decision if Not Met |
|---|---|---|
| Cumulative orders | 10-20 | Under 5: Revisit photos, tags, pricing. Do not scale supplier commitments. |
| Gross margin | ≥58% on Starter Bundle | If below target, audit actual COGS vs. model assumptions |
| Defect rate | <5% | If above 5%: Pause, diagnose, adjust before resuming |
| Average review rating | ≥4.5 stars | If below 4.5: Identify which aspect of the product is generating complaints |
| First review received | Yes | If no review by Day 30, send the review-request message template |
| Supplier lead time validated | <5 days for eSUN Amazon Prime | If longer: Order further in advance; build 3-week buffer |

**Month 1 decision gate**: After 30 days, decide on supplier commitment:
- Fewer than 5 orders: Do not commit to any bulk supplier order. Continue Amazon Prime as-needed.
- 5-20 orders: Place eSUN 10kg Amazon bundle (ASIN B0G2KSS613) for next month's supply.
- 20+ orders: Lock in eSUN 10kg case per color and contact Anycubic to pre-qualify the 50kg pallet deal.

---

### 3-Month Targets (Days 0-90)

| Metric | Target |
|---|---|
| Cumulative orders | 40-80 |
| Monthly run rate | 20-40 orders/month by Month 3 |
| Cumulative reviews | 10+ reviews, 4.5+ average |
| Gross margin | Holding at ≥60% (supplier COGS improving as volume rises) |
| Validated COGS | Actual material cost/unit within ±15% of $0.42 model assumption |
| Defect rate | <3% |
| Supplier relationship | eSUN wholesale inquiry sent; Anycubic test order placed |

**3-month decision gate**: Scale or hold?
- If running at 20-40 orders/month by Month 3, the business is on track. Begin planning the second printer investment (Bambu P1S, ~$700). Payback at this order rate: 6-8 weeks.
- If running at fewer than 20 orders/month: Hold printer 2. Focus on Etsy SEO, consider a small Etsy Ads spend ($1-3/day) for 2-4 weeks to generate algorithmic momentum. Do not add production capacity before demand justifies it.

---

## Appendix: Quick Reference Cards

### Print Settings Card (post near printer)

```
MODRUN PRODUCTION SETTINGS — PLA
Nozzle: 210-215°C
Bed: 60°C (PEI plate)
Layer height: 0.20mm
Infill: 15% gyroid
Perimeter speed: 200mm/s
Supports: NONE
Clips per plate: 8
Rails per plate: 2

Time — single clip: ~25 min
Time — full plate (8 clips): ~90 min
Time — single rail: ~80 min
FDM_TOLERANCE: [update after test print]
```

---

### Pirate Ship Weight Reference

| Package | Contents | Approx. Weight |
|---|---|---|
| 3-pack clips, poly mailer | 3 clips + mailer | 7 oz |
| Single rail, poly mailer | 1 rail + mailer | 6 oz |
| Starter Bundle, small box | 1 rail + 3 clips + box | 12 oz |
| Single clip, poly mailer | 1 clip + mailer | 3.5 oz |

---

### Supplier Contact Reference

| Supplier | Product | Where to Order | Approx. Cost |
|---|---|---|---|
| eSUN (Amazon) | PLA+ 10kg Black | Amazon ASIN B0G2KSS613 | $110-130 |
| eSUN (Amazon) | PLA+ 10kg White | Amazon ASIN B0G2KWC5XL | $110-130 |
| Anycubic | PLA 50kg (Phase 2) | store.anycubic.com/products/pla-basic-50-100kg-deals | $524.73 |
| Shop4Mailers | 9×12" poly mailers 500-pack | shop4mailers.com | ~$25 |
| Pirate Ship | USPS labels (commercial rates) | pirateship.com | No fees |

---

### Etsy Seller Platform Reference

- Orders and messages: etsy.com/your/account
- Stats and traffic: etsy.com/your/stats
- Listings management: etsy.com/your/listings
- Shipping profiles: etsy.com/your/shipping-templates
- Etsy Seller App (recommended): iOS App Store or Google Play

---

**Playbook Status**: Ready for immediate activation on test print go-decision
**Version**: 1.0
**Confidence**: High — all cost figures, supplier pricing, and shipping rates sourced from verified April 2026 data across phase-2-supplier-research.md, cost-model-spreadsheet.csv, and fulfillment-workflow.md
**Next review**: End of Month 1 — validate actual vs. projected defect rate, order volume, and COGS; update print settings card if tolerance adjustments were made
