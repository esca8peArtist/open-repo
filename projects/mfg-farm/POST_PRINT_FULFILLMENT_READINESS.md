---
title: ModRun Post-Test-Print Fulfillment Readiness
project: mfg-farm
created: 2026-05-13
version: 1.0
status: PRE-STAGED — execute upon test print approval
item: 37
audience: thorn
scope: Payment verification, Etsy finalization, shipping pre-flight, customer support templates, inventory tracking, Day 0-2 launch sequence, rollback procedure
references:
  - PRE_LAUNCH_FULFILLMENT_WORKFLOW.md
  - SUPPLIER_NEGOTIATION_PLAYBOOK.md
  - post-test-print-launch-checklist.md
  - DAY1_LAUNCH_OPERATIONS_PLAYBOOK.md
  - fulfillment-workflow.md
---

# ModRun Post-Test-Print Fulfillment Readiness

**PURPOSE**: This document pre-stages every fulfillment verification and setup step so that Day 0 (test print approval) leads directly to Day 1 launch with zero setup friction. All items in this document can be completed or verified before the test print. Nothing here requires the test print to be in-hand — it is a pre-flight checklist, not a post-approval SOP.

**TRIGGER**: When the test print passes the go/no-go gate (per `post-test-print-launch-checklist.md` Part 1), this document becomes the primary operational reference. All seven sections below are ready for immediate execution.

**CRITICAL PATH**: Test print approval (user) → 30-minute Day 0 verification sprint → Day 1 accounts live and supplier contacted → Day 2 first listing published. If this document is fully pre-staged, the gap between "test print approved" and "first Etsy listing live" is 48 hours, not 10 days.

---

## Document Map

| Section | Topic | Time Required | When |
|---|---|---|---|
| 1 | Payment processor verification | 20 min | Pre-test-print (verify now) |
| 2 | Etsy shop finalization | 45 min | Pre-test-print (draft now, publish Day 0) |
| 3 | Shipping integration pre-flight | 25 min | Pre-test-print (configure now) |
| 4 | Customer support templates | 0 min (copy-paste ready) | Pre-staged; load Day 0 |
| 5 | Inventory tracking spreadsheet | 15 min | Create now; activate Day 0 |
| 6 | Day 0–1–2 launch sequence | Reference | Execute post-approval |
| 7 | Rollback procedure | Reference | Execute only if needed |

---

## Section 1: Payment Processor Verification Checklist

**Context**: For the launch period (Months 1-4), all sales flow through Etsy Payments. No standalone processor is needed for marketplace transactions. However, Etsy Payments must be fully configured before the first listing goes live or orders will not process. Stripe is recommended for custom/direct orders that may begin in Month 3+ (see `PRE_LAUNCH_FULFILLMENT_WORKFLOW.md` Section 1 for full rationale).

**Complete this section before the test print if possible. Estimated time: 20 minutes.**

### 1.1 Etsy Payments Verification

```
□ ETSY PAYMENTS ACTIVATION
  □ Navigate to: Etsy.com → Shop Manager → Finances → Payment Settings
  □ Confirm Etsy Payments is listed as ACTIVE (green indicator)
  □ Confirm bank account on file is correct:
      Bank name: [YOUR BANK]
      Account ending in: [LAST 4 DIGITS]
  □ Confirm payout schedule is set (Recommended: weekly automatic on Monday)
  □ Confirm tax ID or SSN is on file (required to receive payouts over $600/year)

□ ETSY PAYMENTS TEST VERIFICATION
  □ Check that "Accept payment" is enabled for: Credit/debit cards ✓, Etsy Gift Cards ✓
  □ Confirm currencies accepted: USD only at launch (do not enable international currencies until Month 4+)
  □ Verify deposit history tab loads (confirms the connection to your bank is working)

□ ETSY BILLING SETUP
  □ Confirm a credit/debit card is on file for Etsy seller fees (listing fees, transaction fees)
  □ Verify your Etsy fee billing method has sufficient balance/credit
  □ Review current fee structure: $0.20/listing, 6.5% transaction fee, 3% + $0.25 Etsy Payments processing
```

**Blocker resolution**: If Etsy Payments shows as suspended or unavailable, visit Etsy Help → Payment problems. Most suspensions are due to incomplete bank account verification. Resolve before publishing listings — orders placed while payments are suspended may not process.

### 1.2 Stripe Setup (For Custom/Direct Orders — Month 3+)

This is optional at launch but takes 20 minutes to set up and eliminates scrambling later when your first custom order request arrives.

```
□ STRIPE ACCOUNT CREATION (if not already done)
  □ Go to stripe.com → Start now
  □ Verify email address
  □ Add business details: Business name "ModRun Design" or similar
  □ Verify identity (SSN last 4 or full SSN depending on volume)
  □ Add bank account for payouts
  □ Set payout schedule: Weekly automatic (avoids rolling holds)

□ STRIPE PAYMENT LINK (create before you need it)
  □ Stripe Dashboard → Payment Links → Create link
  □ Set up a $29.99 "Custom Order" payment link (most common custom order price)
  □ Set up a $49.99 "Bulk Custom Order" link (for 10+ unit custom orders)
  □ Copy both links into a notes file titled "ModRun Custom Order Payment Links"
  □ Do NOT embed Stripe links in your Etsy shop — this violates Etsy ToS

□ STRIPE ACCOUNT STATUS CONFIRMATION
  Current Stripe account status: [ ] Not set up [ ] Created [ ] Verified [ ] Active
  Payment link for single custom order: [PASTE URL HERE]
  Payment link for bulk custom order: [PASTE URL HERE]
```

### 1.3 Payment Processor Quick Reference

| Scenario | Use | Fee |
|---|---|---|
| Etsy marketplace sale | Etsy Payments (automatic) | 6.5% + 3% + $0.25 |
| Custom order (off-platform contact) | Stripe payment link | 2.9% + $0.30 |
| Bulk wholesale invoice | Stripe invoice | 2.9% + $0.30 |
| International payment (future) | Stripe (cleaner FX) | 2.9% + $0.30 + 1% FX |

**Never accept PayPal for business transactions in this context.** PayPal has $0.22 higher per-transaction cost with no operational benefit for this sales model, and PayPal disputes favor buyers in a way that creates unnecessary chargeback exposure.

---

## Section 2: Etsy Shop Finalization Checklist

**Strategy**: Complete all items below before the test print. Mark the listing as Draft, not Published. When the test print passes, the only action is clicking Publish. This reduces Day 0 friction to under 5 minutes for listing activation.

**Estimated time: 45 minutes to complete the full section.**

### 2.1 Product Photos — Staging Checklist

Photos must be staged and ready to upload. They do not need to be taken before the test print — but the shot list and setup should be planned so photography takes under 60 minutes on Day 0 or Day 1.

```
□ PHOTO REQUIREMENTS
  □ Minimum 5 photos per listing (Etsy shows up to 10; use 7-8 for premium positioning)
  □ Minimum resolution: 2000px on shortest side (3000x3000 or larger preferred)
  □ First photo (hero): white or light grey background, product centered, no clutter
  □ File format: JPG preferred; PNG accepted

□ REQUIRED SHOT LIST (complete all 7)
  Photo 1 — HERO: Single clip on white background, 3/4 angle, clean lighting
  Photo 2 — IN-USE: Clip mounted on rail with 3 cables organized, lifestyle context
  Photo 3 — DETAIL: Snap-arm close-up showing the engagement mechanism
  Photo 4 — SCALE: Clip next to common reference object (standard USB-C cable or pen)
  Photo 5 — MULTI-UNIT: Rail with 6 clips installed, showing modular system
  Photo 6 — PACKAGING: Product in poly mailer or on thank-you card, shows professionalism
  Photo 7 — COLOR VARIANTS: If multiple colors available, all colors side by side

□ PHOTOGRAPHY SETUP (prepare before Day 0)
  □ White foam board or white paper backdrop acquired
  □ Natural window light OR desk lamp with daylight bulb (5000K)
  □ Phone camera confirmed to take ≥12MP photos (all modern smartphones sufficient)
  □ No props that suggest scale inaccurately (no hands unless gloved)
  □ Clean, uncluttered surface confirmed

□ PHOTO EDITING (optional but improves conversion rate by 15-25%)
  □ Free option: remove.bg for background removal, Canva for minor editing
  □ Paid option: Adobe Lightroom mobile ($10/month) for consistent color correction
  □ Do NOT over-edit: artificially brightened colors lead to color-disappointment returns
```

### 2.2 Listing Copy Finalization

```
□ LISTING TITLE (review and confirm — 140 character max)
  Primary option:
  "Precision 3D Printed Cable Clips | Modular Snap-Rail Organizer | Customizable"
  [ ] Title confirmed ≤140 characters
  [ ] Primary keyword "3D Printed Cable Clips" appears in first 40 characters
  [ ] No trademark terms or brand references

□ LISTING DESCRIPTION (confirm all sections present)
  [ ] Opening hook (first 160 characters visible in search — do not waste on pleasantries)
  [ ] Bullet-point feature list (5-7 bullets, benefit-focused not feature-focused)
  [ ] Specifications section (dimensions, material, color options, bore sizes)
  [ ] What's included (per SKU variant)
  [ ] Shipping section (1-2 business days production, USPS Ground Advantage 3-5 days)
  [ ] Satisfaction guarantee language (30-day)
  [ ] "Questions? Reply within 24 hours" close

□ PRICING (confirm per variant)
  Single Clip:          $[PRICE] + $[SHIPPING] shipping
  3-Pack Bundle:        $[PRICE] + $[SHIPPING] shipping
  6-Pack Kit:           $[PRICE] + $[SHIPPING] shipping
  Starter Bundle (clips + rail): $[PRICE] + $[SHIPPING] shipping
  
  Target: 40%+ gross margin after Etsy fees (6.5% + 3% = 9.5% total platform take)
  Working backward from 40% margin at $1.80/unit PLA+ material cost:
  3-Pack minimum price = ($1.80 × 3) / (1 - 0.40 - 0.095) = $10.60 floor → sell at $16.99

□ SEO TAGS (all 13 confirmed)
  1. 3d printed clips
  2. cable organizer
  3. desk organizer
  4. modular system
  5. custom cable clips
  6. cable management
  7. pla plastic
  8. office storage
  9. snap clip system
  10. eco-friendly office
  11. customizable organizer
  12. rail system
  13. 3d print design
  [ ] All 13 tags entered in Etsy listing tags field

□ LISTING ATTRIBUTES (complete all applicable)
  [ ] Primary color: [COLORS AVAILABLE]
  [ ] Material: Plastic / PLA
  [ ] Occasion: N/A
  [ ] Style: Modern / Minimalist
  [ ] Dimensions: [LENGTH] x [WIDTH] x [HEIGHT] inches
```

### 2.3 Shipping Profiles

```
□ SHIPPING PROFILE SETUP (Shop Manager → Settings → Shipping settings → Shipping profiles)
  
  Profile name: "ModRun Standard"
  
  □ Origin zip code: [YOUR ZIP CODE]
  □ Processing time: 1–2 business days
  □ Carrier: USPS
  □ Service: Ground Advantage
  □ Domestic rate:
      □ Single Clip (≤2oz): Fixed $4.50 (covers up to Zone 8)
      □ 3-Pack (≤4oz): Fixed $5.00
      □ 6-Pack (≤6oz): Fixed $5.50
      □ Starter Bundle (≤8oz): Fixed $6.00
  □ International shipping: Disabled at launch (enable at Month 4+ after process is proven)
  □ Free shipping offer: Do NOT enable — absorbing shipping into price depresses perceived value
  
  [ ] Shipping profile saved and named "ModRun Standard"
  [ ] Profile applied to all active and draft listings

□ WEIGHT VERIFICATION (required for accurate rate calculation)
  Weigh each SKU with packaging (poly mailer + product + thank-you card) on postal scale:
  Single Clip packaged weight: [___] oz
  3-Pack packaged weight: [___] oz
  6-Pack packaged weight: [___] oz
  Starter Bundle packaged weight: [___] oz
  [ ] All weights confirmed ≤ charged rate boundary
```

### 2.4 Shop Policies and Legal

```
□ RETURN POLICY (copy verbatim into Etsy Shop Policies → Returns & exchanges)
  
  Paste this exact text:
  ---
  We accept returns within 30 days of delivery. If your ModRun product doesn't fit 
  your setup or you're not satisfied, message us before returning. For orders under 
  $40, we will issue a full refund without requiring a return shipment — it is not 
  cost-effective to ship a $5 part back and forth. For orders over $40, we will 
  provide a prepaid return label.
  ---
  
  [ ] Return policy text confirmed in Etsy Shop Policies
  [ ] Return window: 30 days ✓
  [ ] Exchange offered: Yes ✓

□ SHOP SECTIONS
  [ ] Create section: "Cable Clips" (for modrun_clip variants)
  [ ] Create section: "Rail Systems" (for modrun_rail variants)
  [ ] Create section: "Bundles" (for multi-unit sets)
  [ ] All draft listings assigned to correct section

□ SHOP ABOUT SECTION (required for buyer trust)
  [ ] Shop name confirmed
  [ ] Short bio written (2-3 sentences: who you are, what you make, why it's quality)
  [ ] Location: United States (city/state optional)
  [ ] Profile photo or logo uploaded

□ SHOP FAQ SECTION (copy this, paste into Etsy FAQ)
  Q: How long does production take?
  A: All orders are made to order and ship within 1-2 business days.
  
  Q: Can I get a custom color?
  A: Yes — message us before ordering with your preferred color and we'll confirm availability.
  
  Q: Will this fit my cable diameter?
  A: Our clips support cable diameters from 3mm to 10mm. If you have an unusually thick 
  or thin cable, message us with the diameter and we'll confirm compatibility.
  
  Q: My tracking hasn't updated in 3 days. Is this normal?
  A: Yes — USPS Ground Advantage sometimes only scans at origin and destination. Your 
  package is still moving. If no update after 7 days from ship date, message us.
  
  Q: Do you ship internationally?
  A: Not at launch. Check back after June 2026.
  
  [ ] FAQ entered in Etsy Shop FAQ section
```

---

## Section 3: Shipping Integration Pre-Flight

**All steps in this section can be completed before the test print. Once complete, shipping will be fully automated from Etsy order to label generation.**

**Estimated time: 25 minutes.**

### 3.1 Pirate Ship Account Setup and Etsy Integration

```
□ ACCOUNT CREATION
  □ Go to pirateship.com → Create free account
  □ Verify email address
  □ Enter payment method (credit card for postage balance top-up)
      Recommended initial balance load: $20 (covers first 4-6 shipments)
  □ Set "Auto top-up" to $20 when balance drops below $10

□ ETSY STORE CONNECTION
  □ Pirate Ship Dashboard → Carrier Accounts or Settings → Connected Stores
  □ Click "Connect Etsy Store"
  □ Complete OAuth authorization (Etsy login screen — authorize Pirate Ship)
  □ Confirm Etsy store name appears as connected in Pirate Ship
  □ Confirm "Import Orders" shows your Etsy orders (or "No orders yet" if pre-launch)
  [ ] Etsy store confirmed connected to Pirate Ship ✓

□ RATE VERIFICATION (verify USPS Ground Advantage rates)
  □ Pirate Ship → Get Rates
  □ Enter sample shipment: From [YOUR ZIP] → To 90210 (Los Angeles, Zone 6-7)
  □ Weight: 4oz
  □ Dimensions: 8×6×2 inches
  □ Confirm USPS Ground Advantage appears and shows rate ≤$6.00
  Actual rate shown: $[___]
  [ ] Rate confirmed within expected range

□ LABEL TEMPLATE SETUP
  □ Pirate Ship → Settings → Label Settings
  □ Label format: PDF (for inkjet printing) OR 4x6 thermal (if thermal printer available)
  □ If thermal printer: Select "4x6 Thermal" format
  □ If inkjet only: Select "Letter PDF — 2 per page" format
  □ Confirm return address pre-filled with your address
  [ ] Label format confirmed

□ PICKUP SCHEDULE SETUP
  □ Navigate to usps.com/pickup
  □ Set up free carrier pickup at your address
  □ Schedule pickup for: [DAY OF WEEK] by 2:00 PM for same-day pickup
  □ Note: You can schedule individual pickups per day; no need for recurring schedule at launch volumes
  [ ] USPS pickup process confirmed and bookmarked
```

### 3.2 Thermal Printer Status

```
□ THERMAL PRINTER SITUATION
  Current status (check one):
  [ ] Thermal printer owned and working → Verify Pirate Ship PDF prints correctly (test print a sample label)
  [ ] Thermal printer ordered and en route → ETA: [DATE]
  [ ] No thermal printer → Use inkjet fallback (print 2-per-page PDF, cut with scissors, tape to mailer)
  
  Thermal printer recommendation if purchasing: Rollo X1040 ($110-130) or MUNBYN ($90-110)
  Both connect via USB, print 4x6 labels, and are compatible with Pirate Ship's thermal PDF output.

□ INKJET FALLBACK VALIDATION (if no thermal printer)
  □ Print one sample Pirate Ship label on standard paper
  □ Tape securely to envelope or package (clear packing tape works; do NOT cover barcode)
  □ Scan barcode with phone camera — it should resolve to a tracking URL
  [ ] Inkjet fallback confirmed functional ✓
```

### 3.3 Fulfillment System Integration Test

This is a dry-run of the full label pipeline. Complete this before Day 0 so the first real order requires zero troubleshooting.

```
□ PIPELINE TEST
  Step 1: Create a test Etsy listing marked "Draft" (or use an existing draft)
  Step 2: Place a test order to yourself using a different email/account
         (or ask a friend to place and immediately cancel, then manually process)
  Step 3: Open Pirate Ship → Import Orders
  Step 4: Confirm test order appears imported from Etsy
  Step 5: Generate a sample label (do not purchase; Pirate Ship has a "preview" mode)
  Step 6: Confirm label format is correct (address, return address, barcode visible)
  Step 7: If full test, purchase label ($4-6), print, attach to mailer, drop in mailbox
  
  [ ] Pipeline test complete — labels import from Etsy automatically ✓
  [ ] Label prints correctly and barcode is scannable ✓
  [ ] Tracking number updates in Etsy order (may take 2-4 hours after scan) ✓
```

---

## Section 4: Customer Support Templates

**All templates below are production-ready. Copy into Gmail "Canned Responses" (Settings → Advanced → Templates) or into Freshdesk's saved reply library before Day 0.**

**Freshdesk setup (15 minutes)**: Create free account at freshdesk.com, forward your support email to Freshdesk inbox, enable Etsy email notifications to forward. Per `PRE_LAUNCH_FULFILLMENT_WORKFLOW.md` Section 3, Freshdesk free tier handles up to 2 agents at no cost.

**SLA target**: All customer messages responded to within 24 hours. Etsy measures your response rate — falling below 90% response within 24 hours affects search ranking.

### 4.1 Template Library

**Template CS-01: Order Confirmation + Ship Timeline**
Send within 2 hours of order receipt, especially for first-time buyers.
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

**Template CS-02: Shipped Notification**
Send after generating shipping label. Etsy sends an auto-notification but this personalizes it.
```
Subject: Your ModRun order shipped — tracking inside

Hi [FIRST NAME],

Your [PRODUCT NAME] shipped today via USPS Ground Advantage.
Tracking: [TRACKING NUMBER]

Estimated delivery: [DATE RANGE]. USPS Ground Advantage sometimes skips 
intermediate scans, so don't worry if tracking doesn't update for a day 
or two — your order is moving.

Once installed, I'd love to hear how it works for your setup. If anything 
isn't right, message me directly — I'll make it right.

— [YOUR NAME], ModRun
```

**Template CS-03: Custom Order Confirmation**
Use whenever a buyer requests a non-standard color, quantity, or size.
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

If any of this is off, reply before [CUTOFF DATE] and I'll adjust. 
After that, I'll start printing.

— [YOUR NAME], ModRun
```

**Template CS-04: Return or Issue Response**
Use for any complaint, fit issue, or defect report. Offer replacement first.
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

**Template CS-05: Shipping Delay Response**
For cases where tracking hasn't updated or delivery is running late.
```
Subject: Re: Your ModRun order tracking

Hi [FIRST NAME],

I understand this is frustrating — let me explain what's happening.

USPS Ground Advantage packages sometimes only receive scans at the 
origin facility and again at final delivery, with no intermediate 
updates. This is normal and doesn't mean your package is lost.

Your package shipped on [DATE] and should arrive by [DATE RANGE]. 
If it hasn't arrived by [DATE + 3 DAYS], message me and I'll either 
reship or issue a full refund — whichever you prefer.

— [YOUR NAME], ModRun
```

**Template CS-06: Review Request (Post-Delivery)**
Send 5-7 days after confirmed delivery. Etsy reviews are your primary ranking signal.
```
Subject: How's your ModRun order working out?

Hi [FIRST NAME],

Your [PRODUCT NAME] should have arrived a few days ago — I hope it's 
working well for your setup!

If you have a moment, an Etsy review would mean a lot to us and helps 
other buyers find the shop. You can leave one here: [ETSY SHOP LINK]

If anything isn't right, please reply here first — I'd rather fix it 
than have you disappointed.

— [YOUR NAME], ModRun
```

**Template CS-07: Fit Question Response**
The most common pre-sale inquiry for cable clips.
```
Subject: Re: Cable diameter question

Hi [FIRST NAME],

Great question — compatibility matters a lot with cable clips.

Our ModRun clips support cable diameters from 3mm to 10mm:
- 3-5mm: thin cables (phone charging, aux, thin ethernet)
- 5-8mm: standard cables (USB-C, USB-A, standard ethernet)
- 8-10mm: thick cables (DisplayPort, HDMI, thick power)

If your cable is at the edge of a range (like exactly 10mm), the clip 
will hold but may feel firm at first — it loosens slightly with the first 
few attach/detach cycles.

If you're not sure of your cable diameter, measure with a ruler or caliper 
across the widest point. If it's over 10mm, message me — we may be able 
to make a custom variant.

— [YOUR NAME], ModRun
```

### 4.2 Support Infrastructure Setup Checklist

```
□ GMAIL CANNED RESPONSES (if not using Freshdesk)
  □ Gmail → Settings → See all settings → Advanced → Templates → Enable
  □ Compose each template as a draft → three-dot menu → Templates → Save draft as template
  □ Name each template with CS-01 through CS-07 prefix for easy retrieval
  [ ] All 7 templates saved ✓

□ FRESHDESK SETUP (if using Freshdesk — recommended for volume >10 messages/week)
  □ Create free account at freshdesk.com
  □ Forward support email to Freshdesk inbox
  □ Create 7 "Canned Responses" (Solutions → Canned Responses → New)
  □ Label each with CS-01 through CS-07
  □ Test: send email to support address, confirm it appears as Freshdesk ticket
  [ ] Freshdesk receiving email and tickets visible ✓

□ ETSY MESSAGE SETTINGS
  □ Etsy Shop Manager → Messages → Auto-reply
  □ Enable auto-reply for new messages:
    Text: "Thanks for your message! I respond to all inquiries within 24 hours. 
    For order status, check your Etsy Purchases page for tracking info."
  □ Set away mode OFF (ensure messages are monitored daily)
  [ ] Auto-reply active ✓

□ SLA COMMITMENT
  Response target: 24 hours (all channels)
  Escalation: If you miss 24 hours, respond with apology + resolution within next 4 hours
  Etsy metric to watch: Etsy Shop Manager → Stats → Message response rate
  Target: 95%+ response within 24 hours
```

---

## Section 5: Inventory Tracking Spreadsheet

**Create this Google Sheet before the first order arrives. Copy the schema below exactly. The spreadsheet has four tabs.**

**Estimated setup time: 15 minutes.**

### 5.1 Tab 1: Print Queue (Active Orders)

Create a Google Sheet with this structure. Name it "ModRun Operations Dashboard".

**Sheet columns** (Row 1 = headers):

| Column | Header | Notes |
|---|---|---|
| A | Order ID | Etsy order number |
| B | Order Date | Date customer placed order |
| C | Ship By Date | Order date + 2 business days |
| D | SKU | Single Clip / 3-Pack / 6-Pack / Starter Bundle |
| E | Color | Color filament required |
| F | Quantity | Number of units |
| G | Print Status | Queued / Printing / QC / Done |
| H | Print Start | Timestamp when print job started |
| I | Print End | Timestamp when print completed |
| J | QC Pass | YES / NO / REWORK |
| K | Packed | YES / NO |
| L | Label Generated | YES / NO |
| M | Tracking Number | Auto-fill from Pirate Ship |
| N | Ship Date | Date actually shipped |
| O | Delivery Status | Shipped / In Transit / Delivered |
| P | Notes | Any customer requests, defect notes |

**Conditional formatting** (color the Status column):
- Queued = yellow background
- Printing = orange background
- QC = blue background
- Done = green background
- REWORK = red background

### 5.2 Tab 2: Finished Goods Inventory

Track units that have been printed and passed QC but not yet assigned to an order.

| Column | Header | Notes |
|---|---|---|
| A | SKU | Product name |
| B | Color | Filament color |
| C | Quantity | Units on shelf |
| D | Date Printed | Batch date |
| E | QC Status | Passed / Pending |
| F | Location | Where stored (shelf label) |
| G | Notes | Anything unusual about this batch |

**Reorder trigger**: If finished goods for any SKU drop to 0 and no active print is running, add an order to the Print Queue immediately. Never ship-on-demand if finished goods are available — pre-printing reduces ship-by risk.

### 5.3 Tab 3: Shipped Units Log

Permanent record of all shipped orders. This feeds return/replacement tracking and monthly revenue review.

| Column | Header | Notes |
|---|---|---|
| A | Ship Date | Date shipped |
| B | Order ID | Etsy order number |
| C | Customer Name | First name only for privacy |
| D | SKU | What was shipped |
| E | Color | Color |
| F | Quantity | Units shipped |
| G | Sale Price | Revenue from this order |
| H | Etsy Fees | 6.5% + 3% + $0.25 |
| I | Shipping Cost | Actual postage paid |
| J | Material Cost | Filament cost (grams × $/gram) |
| K | Net Profit | Col G - H - I - J |
| L | Tracking | Tracking number |
| M | Delivered | YES / NO / LOST |
| N | Return/Replace | YES / NO |
| O | Return Reason | If YES: color / fit / defect / other |

**Monthly review**: At month-end, SUM Column K for net profit. Calculate return rate (count of Column N = YES / total rows). Target: return rate ≤4%.

### 5.4 Tab 4: Return and Replacement Workflow

Track every return or replacement request end-to-end.

| Column | Header | Notes |
|---|---|---|
| A | Date Reported | When customer reported issue |
| B | Order ID | Original Etsy order number |
| C | Issue Type | Defect / Fit / Color / Shipping damage / Other |
| D | Resolution | Replacement / Refund / No action needed |
| E | Replacement Shipped | Date if applicable |
| F | Refund Amount | $ if applicable |
| G | Refund Processed | YES / NO |
| H | Root Cause | Filament quality / Print settings / Design / Packaging / Carrier |
| I | Notes | Anything else relevant |

**Monthly review**: Categorize root causes. If any root cause appears 3+ times in one month, flag for investigation before it becomes a pattern. Filament quality issues go to the supplier. Print settings issues go to the machine calibration log. Design issues go back to the CAD file.

### 5.5 Filament Inventory Sub-Tracker

Add this to Tab 2 or create a separate Tab 5.

| Column | Header | Notes |
|---|---|---|
| A | Date Received | Delivery date |
| B | Supplier | Prusament / MatterHackers / Amazon Basics |
| C | Color | Color name and hex if known |
| D | Weight (kg) | Spool weight at delivery |
| E | Remaining (kg) | Updated manually each week |
| F | QC Pass | YES / NO (per Gate 1 checklist in SUPPLIER_NEGOTIATION_PLAYBOOK.md) |
| G | Diameter Avg (mm) | From caliper spot check |
| H | Cost | $ paid |
| I | Cost per gram | Col H / (Col D × 1000) |
| J | Reorder Flag | YES if Col E < 0.5 kg |

**Reorder trigger**: When remaining weight drops below 0.5kg for any active color, place a reorder immediately. Lead times of 2-3 weeks (Prusament) mean you cannot wait until you run out.

---

## Section 6: Day 0–Day 1–Day 2 Launch Sequence

**This is the primary execution timeline. Day 0 begins the moment the test print passes its go/no-go evaluation per `post-test-print-launch-checklist.md` Part 1.**

**Responsible party**: All items are solo operator (thorn) unless noted. No external dependencies on Day 0.

### Day 0: Test Print Approval (Target: 3 hours total)

**Goal**: All accounts live, supplier contacted, first photos taken.

#### Day 0, Hour 1: Verification Sprint (0:00–1:00)

```
0:00–0:10 — RUN GO/NO-GO GATE
  □ Dimensional check: 5 clips measured with calipers (per Section 1.1–1.4 of post-test-print-launch-checklist.md)
  □ Fit-test protocol complete (snap, pull, re-snap × 10, cable seat tests)
  □ Surface quality evaluation — all 5 clips pass visual
  □ Print settings logged permanently: nozzle temp, layer height, walls, speed
  DECISION: ✅ GO → continue below | ❌ NO-GO → stop, diagnose, reprint

0:10–0:20 — PAYMENT VERIFICATION
  □ Etsy Payments status: Active ✓
  □ Bank account confirmed correct ✓
  □ Etsy billing card confirmed on file ✓
  (If Section 1 was pre-staged, this takes 5 minutes.)

0:20–0:35 — ETSY LISTINGS CHECK
  □ All draft listings exist in Etsy Shop Manager
  □ Shipping profile "ModRun Standard" applied to all listings
  □ Pricing confirmed for all variants
  □ Tags — all 13 entered for each listing
  □ Shop policies section populated (return policy verbatim)
  □ Shop FAQ populated

0:35–0:45 — PIRATE SHIP VERIFICATION
  □ Log into pirateship.com
  □ Confirm Etsy store still connected
  □ Confirm postage balance ≥$20
  □ Confirm label format set correctly (thermal or PDF)

0:45–1:00 — SUPPLIER OUTREACH (Day 0 action per SUPPLIER_NEGOTIATION_PLAYBOOK.md)
  □ Send Template 1 (Initial Contact) to Prusament: sales@prusament.com
  □ Send Template 1 to MatterHackers: sales@matterhackers.com
  □ Set calendar reminder: Prusament response deadline May 22 / MatterHackers May 20
  □ Set up Amazon Business account as backup (15 min if not done)
```

#### Day 0, Hour 2: Photography Session (1:00–2:00)

```
1:00–1:10 — PHOTOGRAPHY SETUP
  □ White backdrop in place
  □ Lighting confirmed (window light or 5000K desk lamp)
  □ Camera/phone cleaned and ready
  □ Print 1 pristine test clip and 1 pristine rail section for hero shots

1:10–1:50 — SHOOT ALL 7 PHOTOS
  □ Photo 1 — Hero (single clip, 3/4 angle, white background)
  □ Photo 2 — In-use (clip + rail + 3 cables organized)
  □ Photo 3 — Detail (snap-arm close-up)
  □ Photo 4 — Scale reference
  □ Photo 5 — Multi-unit system view
  □ Photo 6 — Packaging shot
  □ Photo 7 — Color variants (if multiple colors printed)

1:50–2:00 — REVIEW AND CULL
  □ Review all photos on larger screen if possible
  □ Discard any blurry or poorly lit shots
  □ Identify the 7 best images to upload
  □ Transfer to computer if taken on phone
```

#### Day 0, Hour 3: Listing Activation and Inventory Setup (2:00–3:00)

```
2:00–2:20 — UPLOAD PHOTOS AND PUBLISH LISTINGS
  □ Open first Etsy draft listing
  □ Upload photos (drag into photo slots — hero in position 1)
  □ Final check: title, description, tags, price, shipping profile all correct
  □ Click "Publish" (not "Save as draft")
  □ Repeat for each SKU variant
  □ Confirm listings appear in Etsy shop (view as customer)
  
  NOTE: Etsy grants new listings a 2-week algorithmic boost. Publishing Day 0 
  maximizes this window. Do not delay listing publication waiting for "perfect" 
  photos — good is better than absent.

2:20–2:40 — GOOGLE SHEET SETUP
  □ Open Google Sheets → Create new sheet
  □ Name it "ModRun Operations Dashboard"
  □ Create 4 tabs: Print Queue, Finished Goods, Shipped Units, Returns
  □ Enter all column headers per Section 5 above
  □ Apply conditional formatting to Print Queue status column
  □ Add today's finished goods: record all clips/rails that passed test print QC

2:40–2:50 — CUSTOMER SUPPORT TEMPLATES
  □ Load all 7 CS templates into Gmail Canned Responses or Freshdesk
  □ Enable Etsy auto-reply message
  □ Set phone/email to receive Etsy order notifications (don't let orders sit unchecked)

2:50–3:00 — USPS PICKUP SCHEDULE
  □ Navigate to usps.com/pickup
  □ Schedule tomorrow's pickup (by 2 PM tomorrow for same-day pickup)
  □ Or confirm mail carrier pickup time for your address
  □ Order 50 poly mailers (9×12") via Amazon Prime if not already in stock
    Search: "9x12 poly mailers white" — 100-pack for $8-12
  □ Order thank-you card stock or pre-print 50 thank-you cards

--- END OF DAY 0 ---
Listings are live. Supplier contacts sent. Infrastructure staged.
```

### Day 1: First 24 Hours Live (Target: 2 hours active)

**Goal**: Monitor first orders, fulfill any that come in, confirm supplier responses.

```
MORNING (8:00–8:30 AM)
  □ Check Etsy Shop Manager for any overnight orders
  □ Check email for supplier responses (Prusament and MatterHackers)
  □ Check Etsy stats: views and favorites from first 12 hours
      Note views count: [___]
      Note favorites count: [___]
  □ If any orders: add to Google Sheet Print Queue immediately

MIDDAY CHECK (12:00–12:15 PM)
  □ Check Etsy messages — respond to any within 24-hour SLA using CS templates
  □ Check order count — any new orders since morning
  □ If printing: check Bambu status, no failures flagged in Bambu app

AFTERNOON — FIRST ORDER FULFILLMENT (if any orders received)
  □ Confirm order in Etsy Shop Manager
  □ Add order to Google Sheet (Tab 1: Print Queue)
  □ Queue print job in Bambu:
      Settings: 0.20mm layer height, PLA+, 3 walls, 220–225°C, 15% gyroid infill
  □ Monitor first 5 minutes of print (most failures occur at layer 1-3)
  □ Post-print QC: visual check + snap-arm functional test
  □ If QC pass: record in Google Sheet (QC Pass = YES)
  □ Pack: clip into poly mailer with crinkle fill and thank-you card
  □ Generate label in Pirate Ship (import from Etsy order)
  □ Purchase label, print, affix to mailer
  □ Schedule USPS pickup or drop at mailbox/USPS

  □ Send CS-02 (Shipped Notification) to customer
  □ Mark order as shipped in Etsy with tracking number
  □ Record in Google Sheet Tab 3 (Shipped Units)

SUPPLIER RESPONSE HANDLING (if responses received)
  □ If Prusament responds with quote: evaluate per SUPPLIER_NEGOTIATION_PLAYBOOK.md Section 2.3
      Walk-away threshold: >$20/kg with no negotiation flexibility
  □ If MatterHackers responds with quote: negotiate to $18-19/kg target
  □ If no response: set reminder to follow up in 2 business days

END OF DAY 1 REVIEW (takes 10 minutes)
  □ Record in Google Sheet: orders received, units printed, units shipped
  □ Note any issues: print failures, fit questions, CS messages received
  □ Calculate: are you on track to ship all orders within 48-hour promise?
```

### Day 2: Operational Rhythm Established (Target: 1 hour daily cadence)

**Goal**: Establish repeatable daily rhythm. The Day 2 cadence is the same cadence you run indefinitely.

```
DAILY CADENCE (in order, every day)

8:00 AM — ORDER REVIEW (10 min)
  □ Open Etsy Shop Manager
  □ Count new orders since yesterday
  □ Add all new orders to Print Queue tab (Google Sheet)
  □ Identify "ship by" date for each (order date + 2 business days)
  □ Prioritize: any orders with ship-by = today move to top of queue

8:10 AM — PRINT QUEUE MANAGEMENT (5 min)
  □ Open Bambu app
  □ Queue all prints needed for today's ship-by orders
  □ Verify filament levels (sufficient for today's batch)
  □ Start first print job

MIDDAY — QC AND PACK (20 min per batch of 5 units)
  □ Pull printed parts from Bambu build plate
  □ QC each part: visual check, snap-arm test, cable seat test
  □ Pass → move to packing station
  □ Fail → mark as REWORK in Google Sheet, reprint immediately
  □ Pack each order: clip in mailer + crinkle fill + thank-you card

EARLY AFTERNOON — LABEL AND SHIP (15 min per 5 orders)
  □ Open Pirate Ship → Import Orders from Etsy
  □ Generate labels for all packed orders
  □ Print labels (thermal or PDF)
  □ Affix labels to mailers
  □ Double-check: each label matches the correct order
  □ Schedule USPS pickup via usps.com/pickup (by 2 PM for same-day)
  □ Mark all shipped orders in Etsy with tracking numbers
  □ Update Google Sheet: Shipped Units tab + Print Queue status = Done

END OF DAY — CS AND REVIEW (10 min)
  □ Check Etsy messages: respond to any unanswered within SLA
  □ Send CS-06 (review request) to orders delivered 5-7 days ago
  □ Review today's stats: orders received, units shipped, CS messages
  □ Note any recurring issues for weekly review

WEEKLY ACTIONS (Sundays — 30 min)
  □ Review Etsy Shop Stats: views, click rate, conversion rate
  □ Calculate net profit for the week (Google Sheet Tab 3)
  □ Review return rate: any returns this week? Log in Tab 4.
  □ Check filament inventory: anything below reorder threshold?
  □ Check supplier order status if order is in transit
  □ Review customer reviews: 5-star goal; respond to any reviews (boosts trust)
```

---

## Section 7: Rollback Procedure

**When to invoke**: If a critical issue is discovered during or immediately after launch that could damage customer experience, reputation, or order integrity. Examples that warrant rollback: batch defect discovered after orders shipped, Pirate Ship integration failure causing lost tracking, Etsy Payments suspended mid-launch, or print settings discovered to be systematically out of tolerance across multiple units.

**What rollback does NOT mean**: Rollback is not "pause if things are slow." It is a specific response to a critical operational failure. Low initial sales are not a rollback trigger — that is normal.

### 7.1 Decision Tree: When to Invoke

```
ISSUE DISCOVERED →

Is it a customer-facing defect (product already shipped to customer)?
├── YES → Go to 7.2 (Customer Impact Response)
└── NO → Is it a systemic print quality issue (defect in current batch, not yet shipped)?
    ├── YES → Go to 7.3 (Production Pause)
    └── NO → Is it an infrastructure failure (Etsy, Pirate Ship, payments)?
        ├── YES → Go to 7.4 (Infrastructure Failure Response)
        └── NO → Is it a legal or compliance concern (product liability, IP, etc.)?
            ├── YES → Go to 7.5 (Legal Pause)
            └── NO → Not a rollback trigger. Log the issue and monitor.
```

### 7.2 Customer Impact Response (Defect Shipped)

**Trigger**: You discover that a batch of parts with a critical defect has already been shipped to customers. This could be discovered via customer complaints, a post-ship QC review, or a dimensional measurement that reveals the shipped batch was out of tolerance.

```
IMMEDIATE ACTIONS (complete within 4 hours of discovery)

Step 1: SCOPE THE DAMAGE
  □ Pull all orders fulfilled from the affected batch (Google Sheet Tab 3, filter by batch date)
  □ Count affected orders
  □ Identify what the defect is and what it means for the customer (functional failure? cosmetic? safety?)
  Affected order count: [___]
  Defect type: [___]

Step 2: PAUSE NEW PRODUCTION FROM AFFECTED BATCH
  □ Stop all print jobs using filament or settings from the affected batch
  □ Quarantine any finished-goods inventory from the same batch
  □ Do NOT ship any additional orders until root cause is diagnosed

Step 3: DIAGNOSE ROOT CAUSE
  □ Print 3 test units using the exact same settings
  □ Measure all critical dimensions
  □ Compare to go/no-go tolerances from post-test-print-launch-checklist.md
  Root cause identified: [ ] Print settings [ ] Filament quality [ ] Design issue [ ] One-time anomaly

Step 4: CUSTOMER NOTIFICATION (proactive outreach)
  Send this message to all affected orders via Etsy:

  ---
  Hi [FIRST NAME],

  I'm reaching out about your recent ModRun order. I discovered a quality issue with 
  this batch and I want to make it right before you even notice a problem.

  I'm shipping you a replacement set at no charge — it will ship within 48 hours. 
  You're welcome to keep the original or dispose of it.

  No action required on your end. Your replacement tracking will be sent separately.

  I apologize for the inconvenience — quality is the top priority here and this 
  shouldn't have made it through QC.

  — [YOUR NAME], ModRun
  ---

Step 5: FULFILL REPLACEMENTS
  □ Print replacement units using corrected settings/filament
  □ Ship replacements via USPS Priority Mail (not Ground Advantage — expedite to compensate)
  □ Mark original orders as "Replacement Sent" in Google Sheet
  □ Log all replacement costs in Tab 4 (Returns)

Step 6: PLATFORM COMMUNICATION
  □ If the defect is likely to generate 1-star reviews: contact Etsy seller support
    (Etsy Help → Contact Support → Seller issue) and explain that you proactively 
    issued replacements. This creates a record if reviews arrive.
  □ If 3+ reviews arrive mentioning the same defect: request Etsy review removal 
    (only possible within 7 days of review and requires proof of resolution)
```

### 7.3 Production Pause (Systemic Batch Defect, Not Yet Shipped)

**Trigger**: QC inspection of printed parts reveals a systematic issue — multiple parts in a batch are out of tolerance or functionally defective. No affected units have shipped.

```
Step 1: PAUSE PRINT QUEUE
  □ Stop all active print jobs
  □ Mark all in-progress orders in Google Sheet as "HOLD"
  □ Set Etsy listings to Vacation Mode (Shop Manager → Settings → Vacation mode → ON)
      Vacation mode text: "Brief production pause — back in 24-48 hours. 
      Existing orders will be fulfilled on time."

Step 2: DIAGNOSE
  □ Measure all parts in the affected batch with calipers
  □ Compare to tolerances in post-test-print-launch-checklist.md
  □ Print 3 diagnostic test units at standard settings
  □ Check: filament moisture (snap test), nozzle temperature, bed adhesion, print speed

Step 3: CORRECT
  Most common causes and corrections:
  - Underextrusion → increase temp by 5°C or reduce speed by 10%
  - Layer separation → increase temp by 5°C, check filament moisture
  - Dimensional creep → check for nozzle partial clog, run cold pull
  - Warping → increase bed temp to 65°C, add brim, reduce first layer speed

Step 4: VALIDATE
  □ Print 5 test units with corrected settings
  □ All 5 must pass full go/no-go gate before resuming production
  □ Document new production settings permanently

Step 5: RESUME
  □ Turn off Etsy Vacation Mode
  □ Resume printing in order of ship-by date (most urgent first)
  □ Update Google Sheet: remove HOLD status from affected orders
  □ If any orders now at risk of missing ship-by date: send CS-02 variant proactively:
      "Your order is taking 24 extra hours due to a quality review — new ship date: [DATE]"
```

### 7.4 Infrastructure Failure Response

**Trigger**: Etsy Payments suspended, Pirate Ship cannot import orders, thermal printer failed, Google account locked.

```
ETSY PAYMENTS SUSPENDED
  □ Do NOT cancel in-flight orders
  □ Go to Etsy Help → Payment problems → follow steps to reactivate
  □ Expected resolution: 1-3 business days for identity re-verification
  □ During suspension: Etsy holds funds but does not cancel orders — fulfill normally
  □ If suspension lasts >3 days: contact Etsy seller support directly

PIRATE SHIP INTEGRATION FAILURE
  □ Fallback: Generate labels directly at usps.com/ship (retail rates ~15-20% higher)
  □ Enter shipping address manually from Etsy order
  □ Print label PDF on standard paper, tape to mailer
  □ Update tracking in Etsy manually (Orders → Order detail → Add tracking number)
  □ Report issue to Pirate Ship support: support@pirateship.com
  □ Reconnect Etsy store: Pirate Ship → Settings → Connected stores → Remove → Re-add

THERMAL PRINTER FAILED
  □ Fallback: Print labels on inkjet/laser paper (cut to 4x6, tape to mailer)
  □ Or: generate labels at Pirate Ship and print as PDF (2-per-letter-page format)
  □ Both are functionally identical — barcode scans the same

GOOGLE SHEETS INACCESSIBLE
  □ Etsy Shop Manager itself tracks all order details — use it as fallback
  □ Download Etsy order CSV: Shop Manager → Orders → Export CSV
  □ Restore Google Sheet from export when access resumes
```

### 7.5 Legal Pause

**Trigger**: Suspected IP conflict (another seller claims your design infringes their IP), customer reports injury, or product liability concern.

```
Step 1: IMMEDIATE LISTING PAUSE
  □ Set all affected listings to "Draft" (not active) in Etsy
  □ Do not delete listings — Etsy's removal protocol requires the listing to exist for disputes

Step 2: DOCUMENT EVERYTHING
  □ Screenshot the claim/complaint
  □ Document your original design process (CadQuery files have commit timestamps)
  □ Your modrun_clip and modrun_rail CAD files in the project directory are your proof of original design

Step 3: FOR IP DISPUTES
  □ Do not admit infringement or engage emotionally
  □ Research the claimant's IP (search USPTO database at tmsearch.uspto.gov or patents.google.com)
  □ If their claim is clearly invalid: respond with a counter-notice to Etsy
  □ If their claim has merit: consult an IP attorney (many offer free initial consultations)

Step 4: FOR INJURY REPORTS
  □ Respond to customer with empathy, request photos and details
  □ Do not admit liability in writing
  □ Assess whether the injury was foreseeable from product design
  □ If product design may be implicated: consult attorney before resuming sales

Step 5: RESUME CRITERIA
  □ IP dispute: resolved, counter-notice accepted by Etsy, or settlement reached
  □ Injury report: product design reviewed and verified safe OR product redesigned
```

### 7.6 Rollback Recovery Checklist

After any rollback event, complete this before resuming full operations:

```
□ Root cause documented in writing (what failed, why, when discovered)
□ Corrective action taken and validated (print test, QC test, or infrastructure test)
□ Affected customers notified and made whole (replacement or refund)
□ Process updated to prevent recurrence (new QC step, setting change, etc.)
□ Etsy Vacation Mode disabled
□ Listings set back to Active
□ Google Sheet updated to reflect all affected orders (status corrected)
□ Defect logged in Tab 4 with root cause
□ Review Etsy Shop Star Rating — monitor for new reviews over next 14 days
□ If 2+ related negative reviews: request removal with proof of resolution
```

---

## Completion Status Tracker

**Pre-stage these items before the test print. Check off as you complete them.**

| Section | Task | Status | Date |
|---|---|---|---|
| 1.1 | Etsy Payments verified active | [ ] | |
| 1.2 | Stripe account created (optional) | [ ] | |
| 2.1 | Photo shot list planned | [ ] | |
| 2.2 | All listing copy drafted (draft status) | [ ] | |
| 2.3 | Shipping profile "ModRun Standard" created | [ ] | |
| 2.4 | Shop policies text entered | [ ] | |
| 3.1 | Pirate Ship account created | [ ] | |
| 3.1 | Etsy store connected to Pirate Ship | [ ] | |
| 3.1 | Postage balance loaded ($20+) | [ ] | |
| 3.2 | Label format confirmed (thermal or PDF) | [ ] | |
| 3.3 | Pipeline test completed | [ ] | |
| 4.2 | CS-01 through CS-07 templates loaded | [ ] | |
| 4.2 | Etsy auto-reply message set | [ ] | |
| 5.1–5.5 | Google Sheet created with all 4 tabs | [ ] | |
| — | Poly mailers in stock (50+) | [ ] | |
| — | Thank-you cards printed (50+) | [ ] | |
| — | Postal scale available | [ ] | |
| — | Digital calipers available | [ ] | |

**When all items above are checked: this document is fully pre-staged. Test print approval triggers Day 0 sprint (Section 6) immediately.**

---

## Quick Reference: Key Contacts and URLs

| Resource | URL / Contact | Notes |
|---|---|---|
| Etsy Shop Manager | etsy.com/your/shops/[SHOPNAME]/tools/listings | Main control panel |
| Etsy Payments | etsy.com/your/account/payments | Payment verification |
| Pirate Ship | pirateship.com | Label generation |
| USPS Pickup | usps.com/pickup | Schedule daily carrier pickup |
| Prusament Sales | sales@prusament.com | Primary supplier — email Day 0 |
| MatterHackers Sales | sales@matterhackers.com | Secondary supplier — email Day 0 |
| Amazon Business | business.amazon.com | Backup filament (immediate Prime) |
| Freshdesk | freshdesk.com | Customer support ticketing (free) |
| Stripe Dashboard | dashboard.stripe.com | Custom order payments (Month 3+) |
| Print Queue Sheet | [PASTE GOOGLE SHEET URL HERE] | Operations dashboard |

---

## Document Version History

| Date | Version | Changes |
|---|---|---|
| 2026-05-13 | 1.0 | Initial delivery — Item 37 complete |

**End of POST_PRINT_FULFILLMENT_READINESS.md**
**Total sections: 7 | Estimated coverage: 650 lines | Status: Production-ready**
