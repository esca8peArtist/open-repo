---
title: ModRun Post-Test-Print Fulfillment Readiness
project: mfg-farm
created: 2026-05-13
version: 2.0
status: PRE-STAGED — execute upon test print approval
item: 37
audience: thorn
scope: Go/No-Go gate, payment verification, Etsy finalization, supplier contact automation, shipping pre-flight, customer support templates, inventory tracking, Day 0-7 launch sequence, rollback procedure
references:
  - PRE_LAUNCH_FULFILLMENT_WORKFLOW.md (Item 16)
  - SUPPLIER_NEGOTIATION_PLAYBOOK.md (Item 23)
  - post-test-print-launch-checklist.md
  - DAY1_LAUNCH_OPERATIONS_PLAYBOOK.md
  - fulfillment-workflow.md
---

# ModRun Post-Test-Print Fulfillment Readiness

**PURPOSE**: Everything needed to go from "test print approved" to "first order shipped" in 48 hours. All pre-stageable sections can be completed before the test print. Nothing here blocks on print-in-hand except photography and the Go/No-Go gate.

**TRIGGER**: When the test print passes the Go/No-Go gate (Section 0 below), this document is the primary operational reference. Execute section by section. Do not skip gates.

**CRITICAL PATH**: Test print approval → 30-minute Day 0 verification sprint → Day 1 accounts live and supplier contacted → Day 2 first listing published. With full pre-staging, the gap between "test print approved" and "first Etsy listing live" is 48 hours.

**FULL REFERENCE DOCUMENTS**:
- `PRE_LAUNCH_FULFILLMENT_WORKFLOW.md` — Item 16: End-to-end fulfillment workflow, payment processor rationale, carrier comparison
- `SUPPLIER_NEGOTIATION_PLAYBOOK.md` — Item 23: Full supplier analysis, 7-step negotiation sequence, pricing tiers, risk mitigation

---

## Document Map

| Section | Topic | Time Required | When |
|---|---|---|---|
| 0 | Go/No-Go Gate | 90 min | Day 0 FIRST — blocks everything |
| 1 | Payment processor verification | 20 min | Pre-test-print (verify now) |
| 2 | Etsy shop finalization | 45 min | Pre-test-print (draft now, publish Day 0) |
| 3 | Shipping integration pre-flight | 25 min | Pre-test-print (configure now) |
| 4 | Supplier contact automation + CRM | 30 min | Day 0, Hour 1 |
| 5 | Customer support templates | 0 min (copy-paste ready) | Pre-staged; load Day 0 |
| 6 | Inventory tracking spreadsheet | 15 min | Create now; activate Day 0 |
| 7 | Day 0-through-Day-7 launch sequence | Reference | Execute post-approval |
| 8 | Rollback procedure | Reference | Execute only if needed |

---

## Section 0: Go/No-Go Gate

**This gate blocks all downstream sections. Nothing in Sections 1-8 executes until you complete this.**

### 5-Item Go/No-Go Checklist

Evaluate the test print immediately. Allocate 90 minutes. All five items must be GO.

```
GO/NO-GO ITEM 1 — DIMENSIONAL TOLERANCE
  □ Print five clips from the test batch (not just one)
  □ Measure with digital calipers (minimum 0.01mm resolution):
      Clip jaw engagement width: _______ mm (Target: CAD spec ±0.5mm)
      Rail channel width: _______ mm (Target: CAD spec ±0.5mm)
      Cable channel bore, minimum (3mm seat): _______ mm (Accept: 2.8–3.2mm)
      Cable channel bore, maximum (10mm seat): _______ mm (Accept: 9.5–10.5mm)
      Snap arm thickness: _______ mm (Target: 1.4mm, Accept: 1.1–1.7mm)
  □ Average all five clips per dimension — no single measurement beyond ±1.0mm of target
  RESULT: □ GO (all five clips within tolerance) | □ NO-GO (stop — adjust FDM_TOLERANCE and reprint)

GO/NO-GO ITEM 2 — SNAP-ARM FIT TEST
  □ Snap one clip onto the rail — requires tactile click, seats fully without forcing
  □ Pull the clipped assembly apart by hand using moderate (not brute) force — must hold
  □ Unsnap and re-snap the same clip 10 times — no loosening, no cracking
  □ Insert a 5mm USB cable, 3mm aux cable, and 8mm USB-C cable — no binding, stays in place
  □ Shake the assembled rail+clip+cable assembly gently — cable does not fall out
  RESULT: □ GO (all fit tests pass) | □ NO-GO (stop — diagnose failure mode before proceeding)

GO/NO-GO ITEM 3 — SURFACE QUALITY
  □ Evaluate under room lighting (not magnified) — commercial product standard
  □ Accept: visible layer lines, minor removable stringing, slight elephant foot not affecting fit
  □ Reject (stop and reprint): layer separation, warping >1mm, visible voids, dense stringing,
    sharp flash at clip jaw, color gradient suggesting filament issue
  □ At least 4 of 5 clips are photo-ready without cleanup
  RESULT: □ GO (surface acceptable for commercial sale) | □ NO-GO (stop — adjust settings)

GO/NO-GO ITEM 4 — PRINT SETTINGS LOCKED
  □ Record production settings permanently (these do not change without another test cycle):
      Nozzle temp: _______ °C  (Target range: 220–225°C)
      Bed temp: _______ °C     (Target: 60°C PEI plate)
      Layer height: _______ mm (Target: 0.20mm)
      Infill: _______ %        (Target: 15% gyroid)
      Walls: _______           (Target: 3 walls)
      Speed: _______ mm/s      (Target: 200mm/s perimeter)
  □ Settings confirmed consistent with test print parameters from SKU_BATCH_2_TEST_PRINT_GUIDE.md
  RESULT: □ GO (settings documented and reproducible) | □ NO-GO (reprint at correct settings first)

GO/NO-GO ITEM 5 — ASSEMBLY INTEGRITY
  □ Assemble one complete rail+clip unit as a customer would receive it
  □ Photograph assembled unit from three angles (front, side, top) — save as reference
  □ Assembly survives normal handling: no parts fall off
  □ No sharp edges a customer would encounter during installation
  RESULT: □ GO (assembly complete, photogenic, safe) | □ NO-GO (address specific failure before continuing)
```

**GATE DECISION**:
- All 5 items GO → Execute Sections 1-8. Begin Day 0 sprint immediately.
- Any item NO-GO → Stop. Diagnose the specific failure. Reprint and re-evaluate.
- Do not attempt partial launch with known quality issues.

---

## Section 1: Payment Processor Verification Checklist

**Context**: For the launch period (Months 1-4), all sales flow through Etsy Payments. No standalone processor is needed for marketplace transactions. Stripe is the recommended addition for Month 3+ custom/direct orders. Full rationale is in `PRE_LAUNCH_FULFILLMENT_WORKFLOW.md` Section 1.

**Complete this section before the test print if possible. Estimated time: 20 minutes.**

### 1.1 Etsy Payments Verification

```
□ ETSY PAYMENTS ACTIVATION
  □ Navigate to: Etsy.com → Shop Manager → Finances → Payment Settings
  □ Confirm Etsy Payments status is: ACTIVE (green indicator)
  □ Confirm bank account on file is correct:
      Bank name: [YOUR BANK]
      Account ending in: [LAST 4 DIGITS]
  □ Confirm payout schedule: Weekly automatic (recommended: Monday)
  □ Confirm tax ID or SSN is on file (required for payouts over $600/year)

□ ETSY PAYMENTS TEST VERIFICATION
  □ Accept payment enabled for: Credit/debit cards ✓, Etsy Gift Cards ✓
  □ Currency: USD only at launch (do not enable international until Month 4+)
  □ Verify deposit history tab loads (confirms bank connection is working)

□ ETSY BILLING SETUP
  □ Confirm credit/debit card on file for Etsy seller fees (listing, transaction fees)
  □ Current fee structure: $0.20/listing, 6.5% transaction fee, 3% + $0.25 Etsy Payments processing
  □ Verify billing card has sufficient balance for first 10 listing fees ($2.00)
```

**Blocker resolution**: Etsy Payments suspended or unavailable → Etsy Help → Payment problems. Most suspensions are due to incomplete bank verification. Resolve before publishing listings — orders placed while payments are suspended will not process.

### 1.2 Stripe Setup (Month 3+ Custom Orders — Pre-Stage Now)

Setting this up before you need it takes 20 minutes and eliminates scrambling when the first custom order request arrives.

```
□ STRIPE ACCOUNT CREATION (if not already done)
  □ Go to stripe.com → Start now
  □ Verify email address
  □ Business name: "ModRun Design" (or your preferred entity name)
  □ Verify identity (SSN last 4 or full SSN depending on projected volume)
  □ Add bank account for payouts
  □ Set payout schedule: Weekly automatic

□ STRIPE PAYMENT LINKS (create before you need them)
  □ Stripe Dashboard → Payment Links → Create link
  □ Link 1: "Custom Order — Single Color" at $29.99
  □ Link 2: "Bulk Custom Order — 10+ units" at $49.99
  □ Copy both links into a notes file: "ModRun Custom Order Payment Links"
  □ Do NOT embed Stripe links in your Etsy shop — this violates Etsy ToS

  Stripe link for single custom order: [PASTE URL HERE]
  Stripe link for bulk custom order: [PASTE URL HERE]
```

### 1.3 Payment Processor Quick Reference

| Scenario | Use | Fee |
|---|---|---|
| Etsy marketplace sale | Etsy Payments (automatic) | 6.5% + 3% + $0.25 |
| Custom order (off-platform) | Stripe payment link | 2.9% + $0.30 |
| Bulk wholesale invoice | Stripe invoice | 2.9% + $0.30 |
| International (future) | Stripe | 2.9% + $0.30 + 1% FX |

**Do not use PayPal for business transactions in this model.** PayPal costs $0.22 more per transaction ($1.24 vs. $1.02 on a $24.99 order) with no operational advantage for this sales model. Full comparison in `PRE_LAUNCH_FULFILLMENT_WORKFLOW.md` Section 1.

---

## Section 2: Etsy Shop Finalization Checklist

**Strategy**: Complete all items below before the test print. Keep listings as Draft. When the test print passes the Go/No-Go gate, the only Day 0 action is clicking Publish. This reduces activation friction to under 5 minutes per listing.

**Estimated time: 45 minutes to complete the full section.**

### 2.1 Product Photos — Staging Checklist

Photos require a printed part in hand. Plan the shot list and setup now so photography takes under 60 minutes on Day 0 after the Go/No-Go gate passes.

```
□ PHOTO REQUIREMENTS
  □ Minimum 7 photos per listing (Etsy allows 10; 7-8 is the premium benchmark)
  □ Minimum resolution: 2000px on shortest side (3000×3000 preferred)
  □ Hero photo: white or light grey background, product centered, no clutter
  □ File format: JPG preferred; PNG accepted

□ SHOT LIST (complete all 7 before any listing goes live)
  Photo 1 — HERO: Single clip on white background, 3/4 angle, clean lighting
  Photo 2 — IN-USE: Clip mounted on rail with 3 cables organized, lifestyle context
  Photo 3 — DETAIL: Snap-arm close-up showing engagement mechanism
  Photo 4 — SCALE: Clip next to common reference (standard USB-C cable or pen)
  Photo 5 — MULTI-UNIT: Rail with 6 clips installed, showing modular system
  Photo 6 — PACKAGING: Product in poly mailer with thank-you card visible
  Photo 7 — COLOR VARIANTS: All available colors side by side (if multiple printed)

□ PHOTOGRAPHY SETUP (prepare before Day 0)
  □ White foam board or white paper backdrop
  □ Natural window light OR 5000K desk lamp
  □ Phone camera confirmed ≥12MP
  □ Clean, uncluttered surface confirmed
  □ Optional: remove.bg for background removal, Canva for text overlays
```

### 2.2 Listing Copy Finalization

The full listing copy is in `HEADPHONE_HOOK_ETSY_EXECUTION.md` and `headphone-hooks-etsy-listing.md`. Verify these fields in Etsy before clicking Draft → Publish.

```
□ LISTING TITLE (≤140 characters; verify in Etsy)
  Primary option: "Precision 3D Printed Cable Clips | Modular Snap-Rail Organizer | Customizable"
  □ Primary keyword "3D Printed Cable Clips" in first 40 characters
  □ No trademark terms or brand references

□ LISTING DESCRIPTION (confirm all sections present)
  □ Opening hook visible in first 160 characters (no pleasantries)
  □ 5-7 benefit-focused bullets
  □ Specifications (dimensions, material, color options, bore sizes)
  □ What's included per SKU variant
  □ Shipping section (1-2 business days production, USPS Ground Advantage 3-5 days)
  □ 30-day satisfaction guarantee language
  □ "Questions? Reply within 24 hours" close

□ PRICING (confirm per variant — do not publish without confirming margin)
  Single Clip:            $[PRICE] + $[SHIPPING]
  3-Pack Bundle:          $[PRICE] + $[SHIPPING]
  6-Pack Kit:             $[PRICE] + $[SHIPPING]
  Starter Bundle:         $[PRICE] + $[SHIPPING]
  Margin floor: 40%+ gross after Etsy fees (9.5% total platform take)
  3-Pack floor: ($1.80 × 3) / (1 - 0.40 - 0.095) = $10.60 floor → target $16.99

□ SEO TAGS (all 13 confirmed — Etsy allows exactly 13)
  1. 3d printed clips          8. office storage
  2. cable organizer           9. snap clip system
  3. desk organizer           10. eco-friendly office
  4. modular system           11. customizable organizer
  5. custom cable clips       12. rail system
  6. cable management         13. 3d print design
  7. pla plastic
  □ All 13 tags entered in Etsy listing tags field

□ LISTING ATTRIBUTES
  □ Primary color: [COLORS AVAILABLE]
  □ Material: Plastic / PLA
  □ Style: Modern / Minimalist
  □ Dimensions: [LENGTH] × [WIDTH] × [HEIGHT] inches
```

### 2.3 Shipping Profiles

```
□ SHIPPING PROFILE SETUP
  Path: Shop Manager → Settings → Shipping settings → Shipping profiles → Create profile

  Profile name: "ModRun Standard"
  □ Origin zip code: [YOUR ZIP CODE]
  □ Processing time: 1–2 business days
  □ Carrier: USPS | Service: Ground Advantage
  □ Domestic rates (fixed):
      Single Clip (≤2oz): $4.50
      3-Pack (≤4oz): $5.00
      6-Pack (≤6oz): $5.50
      Starter Bundle (≤8oz): $6.00
  □ International shipping: Disabled at launch
  □ Free shipping: Do NOT enable — absorbing shipping into price depresses perceived value

  □ Shipping profile saved and named "ModRun Standard"
  □ Profile applied to all active and draft listings

□ WEIGHT VERIFICATION (weigh each SKU with poly mailer + product + thank-you card)
  Single Clip packaged: [___] oz
  3-Pack packaged: [___] oz
  6-Pack packaged: [___] oz
  Starter Bundle packaged: [___] oz
  □ All weights confirmed within charged rate boundary
```

### 2.4 Shop Policies and Legal

```
□ RETURN POLICY (paste verbatim into Etsy Shop Policies → Returns & exchanges)

  We accept returns within 30 days of delivery. If your ModRun product doesn't fit
  your setup or you're not satisfied, message us before returning. For orders under
  $40, we will issue a full refund without requiring a return shipment — it is not
  cost-effective to ship a $5 part back and forth. For orders over $40, we will
  provide a prepaid return label.

  □ Return window: 30 days ✓
  □ Exchange offered: Yes ✓

□ SHOP SECTIONS
  □ "Cable Clips" (modrun_clip variants)
  □ "Rail Systems" (modrun_rail variants)
  □ "Bundles" (multi-unit sets)
  □ All draft listings assigned to correct section

□ SHOP ABOUT SECTION
  □ Shop name confirmed
  □ Short bio (2-3 sentences: who you are, what you make, why it's quality)
  □ Location: United States
  □ Profile photo or logo uploaded

□ SHOP FAQ (paste into Etsy FAQ section)
  Q: How long does production take?
  A: All orders are made to order and ship within 1-2 business days.

  Q: Can I get a custom color?
  A: Yes — message us before ordering with your preferred color and we'll confirm availability.

  Q: Will this fit my cable diameter?
  A: Our clips support cable diameters from 3mm to 10mm. If your cable is outside this
  range, message us with the diameter and we'll confirm or quote a custom variant.

  Q: My tracking hasn't updated in 3 days. Is this normal?
  A: Yes — USPS Ground Advantage sometimes only scans at origin and destination. Your
  package is moving. If no update after 7 days from ship date, message us directly.

  Q: Do you ship internationally?
  A: Not at launch. Check back after June 2026.

  □ FAQ entered in Etsy Shop FAQ section
```

---

## Section 3: Shipping Integration Pre-Flight

**All steps in this section can be completed before the test print. Once complete, shipping is fully automated from Etsy order to label generation.**

**Estimated time: 25 minutes.**

### 3.1 Pirate Ship Account Setup and Etsy Integration

For full Pirate Ship setup rationale and carrier comparison, see `PRE_LAUNCH_FULFILLMENT_WORKFLOW.md` Section 2 and `fulfillment-workflow.md` Section 5.

```
□ ACCOUNT CREATION
  □ Go to pirateship.com → Create free account
  □ Verify email address
  □ Add payment method (credit card for postage balance)
  □ Initial balance load: $20 (covers first 4-6 shipments)
  □ Set Auto top-up: $20 when balance drops below $10

□ ETSY STORE CONNECTION
  □ Pirate Ship Dashboard → Settings → Connected Stores
  □ Click "Connect Etsy Store"
  □ Complete OAuth authorization (Etsy login screen)
  □ Confirm Etsy store name appears as connected
  □ Confirm "Import Orders" shows your orders (or "No orders yet" pre-launch)
  □ Etsy store confirmed connected ✓

□ RATE VERIFICATION
  □ Pirate Ship → Get Rates
  □ Sample: From [YOUR ZIP] → To 90210 (Zone 6-7), weight 4oz, dims 8×6×2"
  □ Confirm USPS Ground Advantage appears at ≤$6.00
  Actual rate shown: $[___]
  □ Rate confirmed within expected range ✓

□ LABEL FORMAT
  □ Pirate Ship → Settings → Label Settings
  □ Thermal printer available: Select "4×6 Thermal" format
  □ Inkjet only: Select "Letter PDF — 2 per page" format
  □ Return address pre-filled with your address ✓
  □ Label format confirmed ✓

□ USPS PICKUP
  □ Navigate to usps.com/pickup
  □ Confirm free carrier pickup is available at your address
  □ Schedule pickup for: [DAY] by 2:00 PM for same-day pickup
  □ Bookmark the page (you'll schedule daily pickups once orders arrive)
```

### 3.2 Thermal Printer Status

```
□ Current status (check one):
  [ ] Thermal printer owned and working → Verify Pirate Ship PDF prints correctly
  [ ] Thermal printer ordered, en route → ETA: [DATE]
  [ ] No thermal printer → Use inkjet fallback (2-per-page PDF, cut to size, tape to mailer)

  Recommended if purchasing: Rollo X1040 ($110-130) or MUNBYN ($90-110)
  Both connect via USB, print 4×6 labels, compatible with Pirate Ship thermal output.

□ INKJET FALLBACK VALIDATION (if no thermal printer)
  □ Print one sample label on standard paper
  □ Tape to envelope (clear packing tape — do NOT cover barcode)
  □ Scan barcode with phone camera → confirms it resolves to a tracking URL
  □ Inkjet fallback functional ✓
```

### 3.3 Fulfillment Pipeline Dry-Run

Complete this before Day 0 so the first real order requires zero troubleshooting.

```
□ PIPELINE TEST
  Step 1: Create a test Etsy draft listing (or use existing draft)
  Step 2: Place a test order to yourself (different account or ask a friend)
  Step 3: Open Pirate Ship → Import Orders
  Step 4: Confirm test order appears imported from Etsy
  Step 5: Generate a preview label (preview mode — do not purchase)
  Step 6: Confirm format: address, return address, barcode all visible
  Step 7 (optional full test): Purchase label ($4-6), print, attach to mailer, drop in mailbox

  □ Orders import from Etsy automatically ✓
  □ Label prints correctly, barcode is scannable ✓
  □ Tracking number updates in Etsy order (may take 2-4 hours after first carrier scan) ✓
```

### 3.4 Automation Opportunities Identified

The following steps in the fulfillment chain are already automated upon correct Pirate Ship + Etsy integration:

| Step | Automated | Manual |
|---|---|---|
| Order notification | Auto (Etsy email) | — |
| Order import to Pirate Ship | Auto (connected store) | — |
| Address pre-population | Auto | — |
| Tracking update to Etsy | Auto (if "auto-mark as shipped" enabled) | Toggle this ON in settings |
| Customer shipping notification | Auto (Etsy triggers on tracking upload) | — |
| Label purchase | — | Manual (user clicks "Buy Label") |
| Print and affix label | — | Manual |
| USPS pickup scheduling | — | Manual (usps.com/pickup daily by 2 PM) |
| Inventory deduction | — | Manual (Google Sheet) until Craftybase added in Month 2+ |

**Key setting to enable**: Pirate Ship → Settings → Connected Stores → Etsy → toggle "Auto-mark as shipped" ON. This eliminates the manual step of marking orders shipped in Etsy after label purchase.

---

## Section 4: Supplier Contact Automation

**Reference document**: `SUPPLIER_NEGOTIATION_PLAYBOOK.md` (Item 23) — contains full 7-step negotiation sequence, pricing tiers, counter-offer framework, and risk mitigation. This section provides ready-to-send email templates and a CRM tracking matrix for Day 0 execution.

### 4.1 Supplier Priority Matrix (Current Data — May 2026)

| Supplier | Role | Price Range | Lead Time | Contact |
|---|---|---|---|---|
| Prusament (Prusa) | PRIMARY (premium quality) | $25–32/kg retail, $23.99/kg at 8+ spools | 2–3 weeks (EU→US) | sales@prusament.com |
| MatterHackers | SECONDARY (domestic fast) | $19.31–21/kg retail, ~$18-19/kg bulk | 1–2 weeks | sales@matterhackers.com / (800) 613-4290 |
| Amazon Basics | BACKUP (emergency) | $14–16/kg Prime | 2 days | No direct contact; Amazon Business account |

**Day 0 action**: Send Template A to Prusament and Template B to MatterHackers. Set up Amazon Business as backup (15 minutes, no contact needed).

### 4.2 Email Templates

---

**Template A — Day 0: Initial Wholesale Contact (Prusament)**

Send to: sales@prusament.com
Subject: Wholesale Inquiry — ModRun 3D Printed Products, Volume Partnership

```
Hello Prusament Sales Team,

My name is [YOUR_NAME], and I'm launching ModRun — an original-design 3D printed
cable management product line on Etsy, targeting premium positioning with quality
as the core value proposition.

I've completed successful test printing on [TEST_PRINT_DATE] (Bambu P1S, 0.20mm
layer height, PLA+, 3 walls, 220-225°C), and I'm now selecting my primary supplier
to support launch and scale-up through 2026.

CURRENT STATUS:
- Product: Custom-designed cable management clips and rail systems (75g PLA+ per unit)
- Printer: Bambu P1S (1 unit; scaling to multi-printer farm in Q3)
- Material requirements: Black, white, grey PLA+, 1.75mm ±0.03mm diameter
- Test print result: PASS — dimensional tolerance and snap-arm fit confirmed

PROJECTED VOLUME:
- Month 1–2: 10–20 kg (2–5 orders of 5–10 kg each)
- Month 3–4: 30–50 kg/month (ramping with 2-printer setup)
- Month 5+: 75–150 kg/month (multi-printer farm)
- 12-month projection: 400–600+ kg total

WHAT I'M LOOKING FOR:
1. Wholesale pricing for Black, White, and Grey PLA+ at 10 kg, 25 kg, and 50+ kg quantities
2. Minimum order quantity (MOQ) and any volume tier structure
3. Lead time guarantee in business days, with shipping buffer to [YOUR STATE]
4. Payment terms (prefer net-30; open to negotiation for volume)
5. Sample order option (1–2 kg to validate quality before bulk commitment)
6. Spool format compatibility with Bambu AMS

I've researched your brand extensively and am impressed by the ±0.02mm diameter
tolerance and exceptional color consistency batch-to-batch. For premium Etsy
positioning, your quality consistency is the deciding factor over lower-cost
alternatives.

I'm not looking for a one-time discount — I want a long-term supply relationship
that grows with the business through 2026 and beyond.

TIMELINE: I need to finalize supplier selection by [DATE + 9 DAYS]. Could you
provide your wholesale pricing sheet and terms by then?

Best regards,
[YOUR_NAME]
ModRun Design
[EMAIL_ADDRESS]
[PHONE_NUMBER]
[ETSY_SHOP_URL — add once live]
```

---

**Template B — Day 0: Initial Wholesale Contact (MatterHackers)**

Send to: sales@matterhackers.com
Subject: Wholesale Inquiry — ModRun Etsy Production, Domestic Supply Partnership

```
Hello MatterHackers Sales Team,

My name is [YOUR_NAME], and I'm launching ModRun — an original-design 3D printed
cable management product line on Etsy. I'm selecting a primary domestic supplier
to support launch and scaling through 2026.

Test printing completed successfully on [TEST_PRINT_DATE] (Bambu P1S, PLA+, 0.20mm
layer height). I'm ready to place a first order within 1 week of agreement on terms.

CURRENT NEEDS:
- Material: PLA+ 1.75mm, Black, White, Grey (primary production colors)
- Volume: 10–20 kg/month to start; scaling to 50–150 kg/month by Q3 2026
- Format: Spools compatible with Bambu AMS (standard or cardboard refill)
- Lead time: Need ≤2 weeks domestic from order to delivery

WHAT I'M LOOKING FOR:
1. Wholesale pricing at 10 kg, 25 kg, and 50 kg+ quantities
2. MOQ and any volume discount tiers
3. Payment terms available for recurring orders
4. Stock availability for Black PLA+ specifically (highest volume color)

I value domestic sourcing specifically: faster restocking when demand spikes, and
no international shipping delays. MatterHackers' reputation for reliability is
exactly what a production operation needs.

TIMELINE: Finalizing supplier selection by [DATE + 7 DAYS]. Quick response
appreciated — ready to order immediately once terms are confirmed.

Best regards,
[YOUR_NAME]
ModRun Design
[EMAIL_ADDRESS]
[PHONE_NUMBER]
[ETSY_SHOP_URL — add once live]
```

---

**Template C — Day 3 Follow-Up (if no response to Template A or B)**

Subject: Following Up — ModRun Wholesale Inquiry [ORIGINAL DATE]

```
Hello [CONTACT_NAME or Team],

Following up on my wholesale inquiry from [ORIGINAL DATE]. I'm still very
interested in [SUPPLIER NAME] as our primary PLA+ supplier for ModRun.

Quick summary of what I'm looking for:
- 10–20 kg/month to start (scaling to 50–150 kg/month by Q3)
- Black, White, and Grey PLA+ 1.75mm
- Bambu AMS compatible spools preferred

If you need additional information to provide pricing, I'm happy to provide it.
If wholesale pricing isn't available at my current volume, let me know the
threshold — I'll plan my ordering to meet it.

My supplier selection deadline is [DATE]. I'm ready to place the first order
within 48 hours of agreeing on terms.

Thank you,
[YOUR_NAME]
ModRun Design
```

---

**Template D — Day 5-7: Volume Pricing Negotiation (if first quote received and is above target)**

Subject: Re: Wholesale Inquiry — Volume Commitment Discussion

```
Hello [CONTACT_NAME],

Thank you for your wholesale quote of [QUOTE_DETAILS]. I appreciate the
quick turnaround.

I want to move forward with [SUPPLIER_NAME] — your [diameter tolerance /
domestic shipping speed / color consistency] is exactly what ModRun's premium
positioning requires. I'd like to work out volume tiers to align pricing with
my growth projections.

YOUR QUOTE VS. MY ANALYSIS:
- Your pricing: [QUOTE_PRICE]/kg at [THEIR_MOQ]
- Market comparison: [COMPETITOR] is quoting [COMPETITIVE_PRICE]/kg at [THEIR_MOQ]
- My target: [TARGET_PRICE]/kg with a 6-month volume commitment

MY PROPOSAL — TIERED COMMITMENT:
Months 1–2: [KG] kg at your standard rate ([RATE]/kg) — first order proof of volume
Months 3–4: [KG] kg at [TIER_2_RATE]/kg
Months 5–6: [KG] kg at [TARGET_RATE]/kg (locked long-term rate)

Total 6-month commitment: [TOTAL_KG] kg — predictable recurring revenue for you.

If you can't reach my target immediately, I'm open to a step-down over 6 months.
For orders exceeding $500/month, would net-30 terms be available?

WALK-AWAY THRESHOLD: I'll accept any quote at or below:
- Prusament: $23/kg at 8+ spools with lead time ≤21 days
- MatterHackers: $19/kg at any recurring volume with ≤14 day lead time

What's the lowest you can guarantee for a 6-month, recurring order?

Best regards,
[YOUR_NAME]
```

### 4.3 Supplier CRM Tracking Matrix

Create a tab in your Google Sheet ("ModRun Operations Dashboard") named "Supplier CRM". Copy this structure:

| Column | Header | Notes |
|---|---|---|
| A | Supplier | Prusament / MatterHackers / Amazon Basics |
| B | Contact Name | Sales rep name if known |
| C | Contact Email | Primary email |
| D | Contact Phone | Phone (MatterHackers: (800) 613-4290) |
| E | Date Contacted | Date Template A or B sent |
| F | Template Sent | Template A / B / C / D |
| G | Response Received | Date of response (or blank if none) |
| H | Quote Price/kg | Price quoted |
| I | MOQ | Minimum order quantity |
| J | Lead Time Quoted | Days quoted |
| K | Payment Terms | Net-30 / CC / Prepay |
| L | Status | Contacted / Negotiating / Accepted / Declined / No Response |
| M | Follow-Up Due | Date to send Template C if no response |
| N | Notes | Any specific details, objections, offers |
| O | Decision | Primary / Secondary / Backup / Rejected |

**Pre-filled rows to create on Day 0**:

| Supplier | Contact Email | Date Contacted | Follow-Up Due | Status |
|---|---|---|---|---|
| Prusament | sales@prusament.com | [DAY 0 DATE] | [DAY 0 + 3 DAYS] | Contacted |
| MatterHackers | sales@matterhackers.com | [DAY 0 DATE] | [DAY 0 + 3 DAYS] | Contacted |
| Amazon Basics | business.amazon.com | [DAY 0 DATE] | N/A — direct order | Backup |

**Response deadline logic**:
- Prusament response expected: Day 0 + 2-5 business days. Hard deadline: Day 0 + 9 days.
- MatterHackers response expected: Day 0 + 1-3 business days. Hard deadline: Day 0 + 7 days.
- If no response by deadline: Send Template C immediately. If still no response after 3 more days: proceed without them.

---

## Section 5: Customer Support Templates

**Load all templates below before Day 0.** Copy into Gmail Canned Responses (Settings → Advanced → Templates) or Freshdesk saved replies. See `PRE_LAUNCH_FULFILLMENT_WORKFLOW.md` Section 3 for Freshdesk setup (15 minutes, free tier handles launch volume).

**SLA target**: All messages responded to within 24 hours. Etsy measures response rate — below 90% response within 24 hours affects search ranking.

### 5.1 Template Library (CS-01 through CS-07)

**CS-01: Order Confirmation + Ship Timeline**
Send within 2 hours of order receipt.
```
Subject: Your ModRun order is in the print queue — ships by [DATE]

Hi [FIRST NAME],

Thanks for your order! Your [PRODUCT NAME] is in our print queue and will
ship by [DATE] via USPS Ground Advantage. You'll receive tracking
automatically from Etsy once it ships.

If you need a different color or have a custom request, reply here and
I can adjust before printing.

— [YOUR NAME], ModRun
```

**CS-02: Shipped Notification**
Send after generating shipping label.
```
Subject: Your ModRun order shipped — tracking inside

Hi [FIRST NAME],

Your [PRODUCT NAME] shipped today via USPS Ground Advantage.
Tracking: [TRACKING NUMBER]

Estimated delivery: [DATE RANGE]. USPS Ground Advantage sometimes skips
intermediate scans — don't worry if tracking doesn't update for a day or
two. Your order is moving.

Once installed, I'd love to hear how it works for your setup. If anything
isn't right, message me directly — I'll make it right.

— [YOUR NAME], ModRun
```

**CS-03: Custom Order Confirmation**
Use whenever a buyer requests non-standard color, quantity, or size.
```
Subject: Custom ModRun order confirmed — here's what we agreed

Hi [FIRST NAME],

Confirming your custom order:
- Product: [ITEM]
- Color: [COLOR]
- Cable compatibility: [SIZE]mm bore
- Quantity: [QTY]
- Price: $[PRICE]
- Payment: [Paid via Etsy listing / Stripe link: URL]
- Estimated ship date: [DATE]

If any of this is off, reply before [CUTOFF DATE]. After that, I'll start printing.

— [YOUR NAME], ModRun
```

**CS-04: Return or Issue Response**
Use for any complaint, fit issue, or defect. Offer replacement first.
```
Subject: Re: Your ModRun order — let me fix this

Hi [FIRST NAME],

Sorry to hear about the issue with your [PRODUCT]. I stand behind the
30-day satisfaction guarantee — let me sort this out right now.

[CHOOSE ONE:]
A) I'll send a replacement [ITEM] right away — no return required.
   Just confirm your shipping address is still [ADDRESS] and I'll
   get it in the mail within 48 hours.

B) If you'd prefer a refund, I'll process it immediately — no need
   to return the item for orders under $30.

Which works best for you?

— [YOUR NAME], ModRun
```

**CS-05: Shipping Delay Response**
For tracking not updated or late delivery.
```
Subject: Re: Your ModRun order tracking

Hi [FIRST NAME],

I understand this is frustrating — let me explain what's happening.

USPS Ground Advantage packages sometimes only receive scans at the origin
facility and again at final delivery, with no intermediate updates. This
is normal and doesn't mean your package is lost.

Your package shipped on [DATE] and should arrive by [DATE RANGE].
If it hasn't arrived by [DATE + 3 DAYS], message me and I'll either
reship or issue a full refund — whichever you prefer.

— [YOUR NAME], ModRun
```

**CS-06: Review Request (Post-Delivery)**
Send 5-7 days after confirmed delivery.
```
Subject: How's your ModRun order working out?

Hi [FIRST NAME],

Your [PRODUCT NAME] should have arrived a few days ago — I hope it's
working well!

If you have a moment, an Etsy review would mean a lot to us and helps
other buyers find the shop: [ETSY SHOP LINK]

If anything isn't right, please reply here first — I'd rather fix it
than have you disappointed.

— [YOUR NAME], ModRun
```

**CS-07: Cable Diameter Compatibility**
Most common pre-sale inquiry for cable clips.
```
Subject: Re: Cable diameter question

Hi [FIRST NAME],

Our ModRun clips support cable diameters from 3mm to 10mm:
- 3-5mm: thin cables (phone charging, aux, thin ethernet)
- 5-8mm: standard cables (USB-C, USB-A, standard ethernet)
- 8-10mm: thick cables (DisplayPort, HDMI, heavy power)

If your cable is at the edge of a range, the clip holds but may feel firm
at first — it loosens slightly after the first few attach/detach cycles.
If your cable exceeds 10mm, message us with the exact diameter.

— [YOUR NAME], ModRun
```

### 5.2 Support Infrastructure Setup

```
□ GMAIL CANNED RESPONSES (if not using Freshdesk)
  □ Gmail → Settings → See all settings → Advanced → Templates → Enable
  □ Compose each template as draft → three-dot menu → Templates → Save as template
  □ Name each CS-01 through CS-07
  □ All 7 templates saved ✓

□ FRESHDESK SETUP (recommended when volume exceeds 10 messages/week)
  □ Create free account at freshdesk.com
  □ Forward support email to Freshdesk inbox
  □ Create 7 Canned Responses labeled CS-01 through CS-07
  □ Test: send email to support address → confirm ticket appears in Freshdesk
  □ Freshdesk receiving and displaying tickets ✓

□ ETSY MESSAGE SETTINGS
  □ Etsy Shop Manager → Messages → Auto-reply → Enable
  □ Text: "Thanks for your message! I respond to all inquiries within 24 hours.
    For order status, check your Etsy Purchases page for tracking info."
  □ Away mode: OFF (messages monitored daily)
  □ Auto-reply active ✓

□ SLA COMMITMENT
  Target: 95%+ response within 24 hours (all channels)
  Monitor: Etsy Shop Manager → Stats → Message response rate
```

---

## Section 6: Inventory Tracking Spreadsheet

**Create this Google Sheet before the first order arrives. Name it "ModRun Operations Dashboard". Four tabs.**

**Estimated setup time: 15 minutes.**

### 6.1 Tab 1: Print Queue (Active Orders)

Headers (Row 1):

| Col | Header | Notes |
|---|---|---|
| A | Order ID | Etsy order number |
| B | Order Date | Customer order date |
| C | Ship By Date | Order date + 2 business days |
| D | SKU | Single / 3-Pack / 6-Pack / Starter Bundle |
| E | Color | Filament color required |
| F | Quantity | Units in order |
| G | Print Status | Queued / Printing / QC / Done |
| H | Print Start | Timestamp |
| I | Print End | Timestamp |
| J | QC Pass | YES / NO / REWORK |
| K | Packed | YES / NO |
| L | Label Generated | YES / NO |
| M | Tracking Number | From Pirate Ship |
| N | Ship Date | Actual ship date |
| O | Delivery Status | Shipped / In Transit / Delivered |
| P | Notes | Customer requests, defect notes |

**Conditional formatting** (Print Status column):
- Queued = yellow | Printing = orange | QC = blue | Done = green | REWORK = red

### 6.2 Tab 2: Finished Goods Inventory

| Col | Header | Notes |
|---|---|---|
| A | SKU | Product name |
| B | Color | Filament color |
| C | Quantity | Units on shelf |
| D | Date Printed | Batch date |
| E | QC Status | Passed / Pending |
| F | Location | Shelf label |
| G | Notes | Batch anomalies |

**Reorder trigger**: If finished goods for any SKU = 0 and no active print running, add to Print Queue immediately.

### 6.3 Tab 3: Shipped Units Log

| Col | Header | Notes |
|---|---|---|
| A | Ship Date | Date shipped |
| B | Order ID | Etsy order number |
| C | Customer Name | First name only |
| D | SKU | What was shipped |
| E | Color | Color |
| F | Quantity | Units shipped |
| G | Sale Price | Revenue |
| H | Etsy Fees | 6.5% + 3% + $0.25 |
| I | Shipping Cost | Actual postage paid |
| J | Material Cost | Filament grams × $/gram |
| K | Net Profit | G - H - I - J |
| L | Tracking | Tracking number |
| M | Delivered | YES / NO / LOST |
| N | Return/Replace | YES / NO |
| O | Return Reason | Color / Fit / Defect / Other |

**Monthly review**: SUM Column K = net profit. Count Column N = YES → divide by total rows = return rate. Target: ≤4%.

### 6.4 Tab 4: Returns and Replacements

| Col | Header | Notes |
|---|---|---|
| A | Date Reported | When customer reported |
| B | Order ID | Original order |
| C | Issue Type | Defect / Fit / Color / Shipping damage / Other |
| D | Resolution | Replacement / Refund / No action |
| E | Replacement Shipped | Date if applicable |
| F | Refund Amount | $ if applicable |
| G | Refund Processed | YES / NO |
| H | Root Cause | Filament / Print settings / Design / Packaging / Carrier |
| I | Notes | Anything else relevant |

**Pattern trigger**: Any root cause appearing 3+ times in one month → investigate before it compounds.

### 6.5 Tab 5: Supplier CRM

Copy the structure from Section 4.3 into this tab. Pre-fill Prusament, MatterHackers, and Amazon Basics rows on Day 0.

### 6.6 Tab 6: Filament Inventory

| Col | Header | Notes |
|---|---|---|
| A | Date Received | Delivery date |
| B | Supplier | Prusament / MatterHackers / Amazon Basics |
| C | Color | Color name |
| D | Weight (kg) | Spool weight at delivery |
| E | Remaining (kg) | Updated weekly |
| F | QC Pass | YES / NO |
| G | Diameter Avg (mm) | From caliper spot check |
| H | Cost | $ paid |
| I | Cost per gram | H / (D × 1000) |
| J | Reorder Flag | YES if E < 0.5 kg |

**Reorder trigger**: When remaining weight drops below 0.5 kg for any active color, place reorder immediately. Prusament lead time 2-3 weeks — do not wait until you run out.

---

## Section 7: Day 0-Through-Day-7 Launch Sequence

**Day 0 begins the moment the Go/No-Go gate (Section 0) is passed.** All items are solo operator (thorn) unless noted. No external dependencies on Day 0.

**Legend**:
- `[AUTO]` = automated or pre-staged; no user decision required
- `[MANUAL]` = requires user action or judgment
- `[PARALLEL]` = can run simultaneously with other items

---

### Day 0: Test Print Approval (Total: ~3 hours)

**Goal**: All accounts live, supplier contacts sent, first photos taken, first listing published.

**Hour 0:00–1:00 — Verification Sprint**

```
0:00–0:30 — GO/NO-GO GATE [MANUAL — blocks all downstream]
  □ Complete Section 0 checklist in full
  □ All 5 items GO → proceed below
  □ Any item NO-GO → STOP — diagnose and reprint first

0:30–0:45 — PAYMENT AND ACCOUNTS VERIFICATION [MANUAL — 15 min if pre-staged]
  □ Etsy Payments status: Active ✓                           [AUTO if pre-staged]
  □ Bank account confirmed correct                           [AUTO if pre-staged]
  □ Etsy billing card on file                               [AUTO if pre-staged]
  □ Pirate Ship: log in, confirm Etsy store connected        [AUTO if pre-staged]
  □ Pirate Ship postage balance ≥$20                         [AUTO if pre-staged]

0:45–1:00 — SUPPLIER OUTREACH [MANUAL — 15 min]
  □ Send Template A to Prusament: sales@prusament.com        [MANUAL]
  □ Send Template B to MatterHackers: sales@matterhackers.com [MANUAL]
  □ Set up Amazon Business account backup if not done:       [MANUAL — 15 min]
      business.amazon.com → sign up → search Amazon Basics PLA+
  □ Fill Tab 5 (Supplier CRM) in Google Sheet with Day 0 contact records [MANUAL]
  □ Set calendar reminders: Prusament follow-up Day 3, MatterHackers follow-up Day 3 [MANUAL]
```

**Hour 1:00–2:00 — Photography Session**

```
1:00–1:10 — PHOTOGRAPHY SETUP [MANUAL]
  □ White backdrop in place
  □ Lighting confirmed (window light or 5000K desk lamp)
  □ Use the two best-looking clips from the test print batch as hero subjects
  □ Camera/phone cleaned and ready

1:10–1:50 — SHOOT ALL 7 PHOTOS [MANUAL]
  □ Photo 1 — Hero (single clip, 3/4 angle, white background)
  □ Photo 2 — In-use (clip + rail + 3 cables organized)
  □ Photo 3 — Detail (snap-arm close-up)
  □ Photo 4 — Scale reference
  □ Photo 5 — Multi-unit system view
  □ Photo 6 — Packaging shot
  □ Photo 7 — Color variants (if multiple colors printed)

1:50–2:00 — REVIEW AND CULL [MANUAL]
  □ Review all photos on a larger screen
  □ Discard blurry or poorly lit shots
  □ Identify 7 best images
  □ Transfer to computer if taken on phone
```

**Hour 2:00–3:00 — Listing Activation and Infrastructure Setup**

```
2:00–2:20 — PUBLISH LISTINGS [MANUAL]
  □ Open first Etsy draft listing
  □ Upload photos (hero photo in slot 1)
  □ Final check: title, description, tags, price, shipping profile all confirmed
  □ Click "Publish" (not "Save as draft")
  □ Repeat for each SKU variant
  □ Confirm listings appear in Etsy shop (view as customer)

  NOTE: Etsy grants new listings a 2-week algorithmic boost. Publishing Day 0
  maximizes this window. Do not delay publication waiting for "perfect" photos.

2:20–2:40 — GOOGLE SHEET SETUP [MANUAL]
  □ Create "ModRun Operations Dashboard" in Google Sheets
  □ Create 6 tabs: Print Queue, Finished Goods, Shipped Units, Returns, Supplier CRM, Filament
  □ Enter all column headers per Section 6
  □ Apply conditional formatting to Print Queue status column
  □ Record today's finished goods (test print clips that passed QC)
  □ Fill Supplier CRM tab with Day 0 contact data

2:40–2:50 — CUSTOMER SUPPORT [MANUAL]
  □ Load CS-01 through CS-07 templates into Gmail Canned Responses or Freshdesk
  □ Enable Etsy auto-reply message
  □ Enable Etsy order notification emails on phone (do not let orders sit unchecked)

2:50–3:00 — PHYSICAL SUPPLIES [MANUAL/PARALLEL]
  □ Schedule tomorrow's USPS pickup (usps.com/pickup, by 2 PM for same-day)
  □ Order 50+ poly mailers 9×12" via Amazon Prime if not in stock (100-pack ~$8-12)
  □ Order thank-you card stock or print 50 cards now
  □ Confirm postal scale available and working

--- END OF DAY 0 ---
Listings live. Supplier contacts sent. Infrastructure staged.
```

---

### Day 1: First 24 Hours Live (Target: 2 hours active)

**Goal**: Monitor early traffic, fulfill any orders received, confirm supplier responses.

```
MORNING (8:00–8:30 AM) [MANUAL]
  □ Check Etsy Shop Manager for overnight orders
  □ Check email for supplier responses (Prusament and MatterHackers)
  □ Check Etsy Stats: views and favorites from first 12 hours
      Views: [___]   Favorites: [___]  (early benchmarks — normal if low)
  □ If any orders: add to Google Sheet Print Queue immediately

MIDDAY CHECK (12:00–12:15 PM) [MANUAL]
  □ Check Etsy messages — respond to any within 24-hour SLA using CS templates [MANUAL]
  □ Check order count — any new orders since morning
  □ If printing: confirm print is running without failures

AFTERNOON — FIRST ORDER FULFILLMENT (if any orders received) [MANUAL]
  □ Confirm order in Etsy Shop Manager
  □ Add to Google Sheet Tab 1 (Print Queue)
  □ Queue print job in Bambu (0.20mm layer height, PLA+, 3 walls, 220–225°C, 15% gyroid infill)
  □ Monitor first 5 minutes of print (most failures occur at layers 1-3)
  □ Post-print QC: visual check + snap-arm test
  □ If QC pass: record in Google Sheet
  □ Pack: clip in poly mailer + crinkle fill + thank-you card
  □ Generate label in Pirate Ship (import from Etsy)       [AUTO — label auto-imports]
  □ Purchase label, print, affix to mailer                 [MANUAL]
  □ Schedule USPS pickup or drop at mailbox                [MANUAL]
  □ Send CS-02 (Shipped Notification) to customer          [MANUAL]
  □ Mark order as shipped in Etsy with tracking number     [AUTO if Pirate Ship auto-mark enabled]
  □ Record in Google Sheet Tab 3 (Shipped Units)           [MANUAL]

SUPPLIER RESPONSE HANDLING [MANUAL]
  □ If Prusament responds with quote: evaluate against $23/kg target at 8+ spools
      Walk-away: >$25/kg with no negotiation path
  □ If MatterHackers responds: target $18-19/kg
      Walk-away: >$20/kg with no payment terms flexibility
  □ If no response yet: no action needed until Day 3 deadline

END OF DAY 1 REVIEW (10 minutes) [MANUAL]
  □ Record: orders received, units printed, units shipped
  □ Note any issues: print failures, fit questions, CS messages
  □ Confirm: on track to ship all orders within 48-hour promise?
```

---

### Day 2: Operational Rhythm Established (Target: 1 hour active daily)

**Goal**: Establish the repeatable daily cadence. The Day 2 cadence is what you run indefinitely.

```
DAILY CADENCE (in order, every day) [MANUAL unless marked AUTO]

8:00 AM — ORDER REVIEW (10 min)
  □ Open Etsy Shop Manager
  □ Count new orders since yesterday
  □ Add all new orders to Print Queue tab
  □ Identify ship-by date for each (order date + 2 business days)
  □ Prioritize: ship-by = today → top of queue

8:10 AM — PRINT QUEUE (5 min)
  □ Open Bambu app
  □ Queue all prints for today's ship-by orders
  □ Verify filament levels (sufficient for today's batch)
  □ Start first print job

MIDDAY — QC AND PACK (20 min per batch of 5 units)
  □ Pull printed parts from Bambu build plate
  □ QC each part: visual check + snap-arm test + cable seat test
  □ Pass → packing station
  □ Fail → mark REWORK in Google Sheet, reprint immediately
  □ Pack: clip in mailer + crinkle fill + thank-you card

EARLY AFTERNOON — LABEL AND SHIP (15 min per 5 orders)
  □ Pirate Ship → Import Orders from Etsy            [AUTO — imports automatically]
  □ Generate labels for all packed orders            [MANUAL — click Buy Label]
  □ Print labels                                     [MANUAL]
  □ Affix labels to mailers — double-check label matches order
  □ Schedule USPS pickup (usps.com/pickup by 2 PM)   [MANUAL]
  □ Mark all shipped orders in Etsy with tracking    [AUTO if auto-mark enabled]
  □ Update Google Sheet: Tab 3 Shipped + Tab 1 status = Done

END OF DAY — CS AND REVIEW (10 min)
  □ Check Etsy messages: respond to any unanswered
  □ Send CS-06 (review request) to orders delivered 5-7 days ago
  □ Note any recurring issues for weekly review
```

---

### Day 3: Supplier Follow-Up and Negotiation

**Goal**: Follow up on supplier contacts if no response; evaluate and negotiate any quotes received.

```
SUPPLIER FOLLOW-UP [MANUAL — 20 min]
  □ Check Supplier CRM tab (Google Sheet Tab 5)
  □ Prusament: response received? 
      NO → Send Template C follow-up to sales@prusament.com
      YES → Evaluate quote vs. targets (see SUPPLIER_NEGOTIATION_PLAYBOOK.md Section 2.3)
  □ MatterHackers: response received?
      NO → Send Template C follow-up to sales@matterhackers.com; call (800) 613-4290
      YES → Evaluate quote vs. targets; if above $20/kg, prepare Template D

  □ Update Supplier CRM: Response status, quote price, follow-up sent date

NORMAL DAILY OPERATIONS [MANUAL — per Day 2 cadence]
  □ Order review, print queue, QC and pack, label and ship
  □ CS messages checked and responded to
```

---

### Days 4-5: First Sales Momentum Assessment

**Goal**: Identify early patterns. Are listings getting views? Are any titles or photos underperforming?

```
ETSY STATS REVIEW (15 min on Day 5) [MANUAL]
  □ Etsy Shop Manager → Stats
  □ Record:
      Total views since launch: [___]
      Total favorites: [___]
      Orders received: [___]
      Conversion rate (orders / views): [___]%
  
  Benchmarks for first 5 days:
  - Views: 20-50 = normal for new shop; 100+ = strong early algorithmic boost
  - Favorites: >5% of views favoriting = good listing resonance
  - Conversion: >2% of views ordering = very good for new shop; <1% = investigate photos/title

  □ If conversion <1%: Review hero photo first (most common fix). Then review title keyword.
  □ If views <10 total: Re-check all 13 SEO tags are entered correctly.

NORMAL DAILY OPERATIONS [MANUAL — per Day 2 cadence]
  □ Orders → print → QC → pack → ship
  □ CS messages

SUPPLIER STATUS CHECK [MANUAL — 5 min]
  □ Any new supplier responses? If yes, evaluate and respond
  □ MatterHackers hard deadline: Day 7. Set final reminder.
```

---

### Days 6-7: Supplier Decision and Week 1 Close

**Goal**: Make supplier selection decision. Close Week 1 with metrics documented.

```
DAY 6-7: SUPPLIER SELECTION DECISION [MANUAL — 30 min]
  □ Review both supplier responses (or lack thereof) in Supplier CRM
  □ Apply decision criteria from SUPPLIER_NEGOTIATION_PLAYBOOK.md Section 1.2:
      Prusament quote ≤$23/kg at 8+ spools + lead time ≤21 days → SELECT as primary
      MatterHackers quote ≤$19/kg + lead time ≤14 days → SELECT as secondary
      Neither met threshold → Amazon Prime as primary; defer negotiation to Month 2
  □ If negotiating: send Template D to the supplier whose quote is closest to target
  □ If selecting: confirm order details and timeline for first batch

  □ Place first filament order once supplier is selected
  □ Record decision in Supplier CRM (Column O: Primary / Secondary / Rejected)

WEEK 1 METRICS CLOSE [MANUAL — 15 min Sunday]
  □ Google Sheet Tab 3: count total units shipped, sum net profit
  □ Etsy Stats: views, favorites, orders, conversion rate
  □ Print queue: any open orders? Any past-due ship-by dates?
  □ Return rate: any returns or issues in Tab 4?
  □ Note one process improvement for Week 2

  Week 1 actuals to record:
    Units shipped: [___]
    Orders received: [___]
    Net profit: $[___]
    Return rate: [___]%
    Avg Etsy review (if any): [___] stars
    Supplier status: Primary = [___], Secondary = [___]

NORMAL DAILY OPERATIONS [MANUAL — per Day 2 cadence]
  □ Orders → print → QC → pack → ship
  □ CS messages
```

---

### Weekly Recurring Cadence (Sundays — 30 min)

```
  □ Etsy Shop Stats: views, click rate, conversion rate
  □ Calculate net profit for the week (Google Sheet Tab 3)
  □ Return rate: any returns this week? Log in Tab 4. Root cause?
  □ Check filament inventory: anything below reorder threshold?
  □ Supplier orders: any in transit? Any to place?
  □ Customer reviews: respond to all new reviews (boosts trust signal)
  □ One improvement identified and documented for next week
```

---

## Section 8: Rollback Procedure

**Invoke only for critical operational failures** — not for slow sales. The rollback procedure addresses: batch defect post-ship, Pirate Ship integration failure, Etsy Payments suspension, and legal concerns.

### 8.1 Decision Tree

```
ISSUE DISCOVERED →

Is it a customer-facing defect (product already shipped)?
  YES → Section 8.2 (Customer Impact Response)
  NO → Is it a systemic print quality issue, not yet shipped?
      YES → Section 8.3 (Production Pause)
      NO → Is it an infrastructure failure (Etsy, Pirate Ship, payments)?
          YES → Section 8.4 (Infrastructure Failure)
          NO → Is it legal or compliance concern?
              YES → Section 8.5 (Legal Pause)
              NO → Not a rollback trigger. Log issue and monitor.
```

### 8.2 Customer Impact Response (Defect Shipped)

```
Step 1: SCOPE THE DAMAGE
  □ Pull all orders from affected batch (Tab 3, filter by batch date)
  □ Count affected orders: [___]
  □ Identify defect type and functional impact

Step 2: PAUSE PRODUCTION FROM AFFECTED BATCH
  □ Stop all print jobs using filament/settings from affected batch
  □ Quarantine finished goods from same batch
  □ Do not ship additional orders until root cause diagnosed

Step 3: DIAGNOSE
  □ Print 3 test units using exact same settings
  □ Measure all critical dimensions vs. Go/No-Go tolerances

Step 4: CUSTOMER NOTIFICATION (proactive — send before they complain)
  Paste verbatim into Etsy message to all affected orders:
  ---
  Hi [FIRST NAME],

  I'm reaching out about your recent ModRun order. I discovered a quality issue
  with this batch and I want to make it right before you even notice a problem.

  I'm shipping you a replacement set at no charge — it will ship within 48 hours.
  You're welcome to keep the original or dispose of it.

  No action required on your end. Your replacement tracking will be sent separately.

  I apologize for the inconvenience — quality is the top priority here.

  — [YOUR NAME], ModRun
  ---

Step 5: FULFILL REPLACEMENTS
  □ Print replacements with corrected settings/filament
  □ Ship via USPS Priority Mail (not Ground Advantage — expedite to compensate)
  □ Mark original orders "Replacement Sent" in Tab 3
  □ Log all replacement costs in Tab 4

Step 6: PLATFORM COMMUNICATION
  □ If likely to generate negative reviews: contact Etsy seller support
    (Etsy Help → Contact Support → Seller issue) and document the proactive resolution
  □ If 3+ reviews mention same defect: request removal with proof of resolution
    (Etsy review removal: only possible within 7 days of review)
```

### 8.3 Production Pause (Systemic Batch Defect, Not Yet Shipped)

```
Step 1: PAUSE
  □ Stop all active print jobs
  □ Mark all in-progress orders "HOLD" in Tab 1
  □ Set Etsy Vacation Mode ON (Shop Manager → Settings → Vacation mode)
      Text: "Brief production pause — back in 24-48 hours. Existing orders fulfilled on time."

Step 2: DIAGNOSE
  □ Measure all parts in affected batch with calipers
  □ Compare to Go/No-Go tolerances (Section 0)
  □ Print 3 diagnostic test units at standard settings
  □ Check: filament moisture (snap test), nozzle temp, bed adhesion, print speed

Step 3: MOST COMMON CAUSES AND CORRECTIONS
  - Underextrusion: increase temp by 5°C OR reduce speed by 10%
  - Layer separation: increase temp by 5°C, check filament moisture
  - Dimensional creep: check for partial nozzle clog, run cold pull
  - Warping: increase bed temp to 65°C, add brim, reduce first layer speed

Step 4: VALIDATE
  □ Print 5 test units with corrected settings
  □ All 5 must pass full Section 0 Go/No-Go gate before resuming

Step 5: RESUME
  □ Turn off Etsy Vacation Mode
  □ Resume printing in order of ship-by date (most urgent first)
  □ If any orders now at risk of missing ship-by: send proactive message:
      "Your order is taking 24 extra hours due to a quality review — new ship date: [DATE]"
```

### 8.4 Infrastructure Failure Response

```
ETSY PAYMENTS SUSPENDED
  □ Do not cancel in-flight orders
  □ Etsy Help → Payment problems → follow reactivation steps
  □ Expected resolution: 1-3 business days for identity re-verification
  □ Orders still fulfill normally during suspension (Etsy holds funds, does not cancel orders)

PIRATE SHIP INTEGRATION FAILURE
  □ Fallback: Generate labels directly at usps.com/ship (retail rates ~15-20% higher)
  □ Enter shipping address manually from Etsy order
  □ Print label PDF on standard paper, tape to mailer
  □ Update tracking in Etsy manually (Orders → Order detail → Add tracking number)
  □ Reconnect: Pirate Ship → Settings → Connected stores → Remove → Re-add
  □ Report to Pirate Ship support: support@pirateship.com

THERMAL PRINTER FAILED
  □ Print labels on inkjet/laser paper (cut to 4×6, tape to mailer)
  □ Or: Pirate Ship → generate labels as PDF (2-per-letter-page format)
  □ Barcode is functionally identical — scans the same

GOOGLE SHEETS INACCESSIBLE
  □ Etsy Shop Manager itself tracks all order details — use as fallback
  □ Download Etsy order CSV: Shop Manager → Orders → Export CSV
  □ Restore Google Sheet from export when access resumes
```

### 8.5 Legal Pause

```
Step 1: IMMEDIATE LISTING PAUSE
  □ Set all affected listings to "Draft" in Etsy (do not delete — needed for dispute process)

Step 2: DOCUMENT EVERYTHING
  □ Screenshot the claim or complaint
  □ Your modrun_clip and modrun_rail CadQuery files in the cadquery/ directory
    have commit timestamps — this is proof of original design

Step 3: FOR IP DISPUTES
  □ Do not admit infringement
  □ Research the claimant's IP (USPTO: tmsearch.uspto.gov, Google Patents: patents.google.com)
  □ If claim is clearly invalid: respond with counter-notice to Etsy
  □ If claim has merit: consult IP attorney (many offer free initial consultations)

Step 4: FOR INJURY REPORTS
  □ Respond to customer with empathy, request photos and details
  □ Do not admit liability in writing
  □ Assess whether injury was foreseeable from product design
  □ Consult attorney before resuming sales if design may be implicated

Step 5: RESUME CRITERIA
  □ IP dispute: resolved, counter-notice accepted, or settlement reached
  □ Injury report: product design verified safe OR redesigned
```

### 8.6 Rollback Recovery Checklist

After any rollback event, complete before resuming full operations:

```
□ Root cause documented in writing
□ Corrective action taken and validated (print test, QC test, or infrastructure test)
□ Affected customers notified and made whole (replacement or refund)
□ Process updated to prevent recurrence (new QC step, setting change, etc.)
□ Etsy Vacation Mode disabled
□ Listings set back to Active
□ Google Sheet updated to reflect all affected orders
□ Defect logged in Tab 4 with root cause
□ Monitor Etsy Shop Star Rating for 14 days post-rollback
□ If 2+ related negative reviews: request removal with proof of resolution
```

---

## Pre-Stage Completion Tracker

**Complete these items before the test print. Check off as you complete each.**

| Section | Task | Status | Date |
|---|---|---|---|
| 1.1 | Etsy Payments verified active | [ ] | |
| 1.2 | Stripe account created (optional) | [ ] | |
| 2.1 | Photo shot list planned | [ ] | |
| 2.2 | All listing copy drafted (Draft status in Etsy) | [ ] | |
| 2.3 | Shipping profile "ModRun Standard" created | [ ] | |
| 2.4 | Shop policies text entered | [ ] | |
| 2.4 | Shop FAQ entered | [ ] | |
| 3.1 | Pirate Ship account created | [ ] | |
| 3.1 | Etsy store connected to Pirate Ship | [ ] | |
| 3.1 | Postage balance loaded ($20+) | [ ] | |
| 3.2 | Label format confirmed (thermal or PDF) | [ ] | |
| 3.3 | Pipeline dry-run completed | [ ] | |
| 5.2 | CS-01 through CS-07 templates loaded | [ ] | |
| 5.2 | Etsy auto-reply message set | [ ] | |
| 6 | Google Sheet created with all 6 tabs and headers | [ ] | |
| — | Poly mailers in stock (50+) | [ ] | |
| — | Thank-you cards printed (50+) | [ ] | |
| — | Postal scale available | [ ] | |
| — | Digital calipers available | [ ] | |

**When all items above are checked: this document is fully pre-staged. Test print approval triggers Section 0 (Go/No-Go), then Day 0 sprint immediately.**

---

## Quick Reference: Key Contacts and URLs

| Resource | URL / Contact | Notes |
|---|---|---|
| Etsy Shop Manager | etsy.com/your/shops/[SHOPNAME]/tools/listings | Main control panel |
| Etsy Payments | etsy.com/your/account/payments | Payment verification |
| Pirate Ship | pirateship.com | Label generation |
| USPS Pickup | usps.com/pickup | Schedule daily carrier pickup |
| Prusament Sales | sales@prusament.com | Primary supplier — Template A Day 0 |
| MatterHackers Sales | sales@matterhackers.com / (800) 613-4290 | Secondary supplier — Template B Day 0 |
| Amazon Business | business.amazon.com | Backup filament (Prime, no negotiation) |
| Freshdesk | freshdesk.com | Customer support ticketing (free) |
| Stripe Dashboard | dashboard.stripe.com | Custom order payments (Month 3+) |
| Print Queue Sheet | [PASTE GOOGLE SHEET URL HERE] | Operations dashboard |
| Item 16 Reference | PRE_LAUNCH_FULFILLMENT_WORKFLOW.md | Full fulfillment workflow + payment rationale |
| Item 23 Reference | SUPPLIER_NEGOTIATION_PLAYBOOK.md | Full supplier analysis + negotiation sequence |

---

## Document Version History

| Date | Version | Changes |
|---|---|---|
| 2026-05-13 | 1.0 | Initial delivery — Item 37 complete |
| 2026-05-13 | 2.0 | Added 5-item Go/No-Go gate; updated supplier section to Prusament/MatterHackers (aligned with Item 23); added Day 3 follow-up and negotiation email templates; added Supplier CRM tracking matrix (Tab 5); extended launch sequence to Day 7; added automation/manual legend to timeline; added Filament Inventory tab (Tab 6) |

**End of POST_PRINT_FULFILLMENT_READINESS.md**
**Version 2.0 | Sections: 8 + Pre-Stage Tracker + Quick Reference | Status: Production-ready**
