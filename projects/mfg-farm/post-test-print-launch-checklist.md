---
title: ModRun Post-Test-Print Launch Checklist
date: 2026-05-06
status: ready-to-execute
scope: Complete action sequence from successful test print through first live Etsy sale
related: post-test-print-EXECUTION-INDEX.md, supplier-economics.md, etsy-seo-strategy.md, bundle-strategy.md, cost-model-spreadsheet.csv
---

# ModRun Post-Test-Print Launch Checklist

**This is the sequence you follow the moment you confirm a successful test print. Every item is binary: done or not done. No optional sections.**

**Estimated time to first Etsy listing live**: 10–14 days from test print confirmation.
**Estimated time to first sale**: 14–21 days.
**Estimated time to supplier agreement locked**: 21 days.

---

## Part 1: Physical Validation (Day 0 — Immediately After Print)

This is the gate. Nothing in Parts 2–5 starts until all go criteria below pass. Budget 90 minutes.

### 1.1 Dimensional Tolerance Checks

You need a digital caliper. Measure five clips from the print batch, not just one.

| Measurement | Target | Accept | Reject |
|---|---|---|---|
| Clip jaw width (engagement face) | Per CAD | Within ±0.5mm | Beyond ±1.0mm |
| Rail channel width | Per CAD | Within ±0.5mm | Beyond ±1.0mm |
| Cable channel diameter (min) | 3mm seat | 2.8–3.2mm | Outside this range |
| Cable channel diameter (max) | 10mm seat | 9.5–10.5mm | Outside this range |
| Part height overall | Per CAD | ±0.5mm | Beyond ±1.0mm |

Record all five measurements. Average them. If any single measurement rejects, stop and execute the No-Go protocol below before continuing.

**Why five clips**: A single clip might be a statistical outlier. Five gives you enough data to distinguish a systematic tolerance issue (all five off in the same direction) from a random one (one outlier).

### 1.2 Fit-Test Protocol

Perform all of the following in sequence. Each must pass.

- [ ] Snap one clip onto the rail. It should engage with a tactile click and seat fully without forcing.
- [ ] Attempt to pull the clipped assembly apart by hand using moderate force (not brute force). It should hold.
- [ ] Unsnap and re-snap the same clip 10 times without noticeable loosening or plastic cracking. This is your fatigue test.
- [ ] Insert a 5mm USB cable into the clip channel. It should seat without binding and stay in place when the rail is held horizontally.
- [ ] Insert a 3mm cable (thin Micro-USB or aux cable). Same test. No binding.
- [ ] Insert a 8mm cable (typical USB-C or DisplayPort). Same test. No binding.
- [ ] Shake the assembled rail+clip+cable assembly gently. Cable should not fall out.

If any step fails, note the exact failure mode with a photo before stopping. The failure mode determines whether you need a CadQuery parameter adjustment (dimensional), a print settings adjustment (surface/fit), or both.

### 1.3 Surface Quality Evaluation

Evaluate under normal room lighting, not magnified. This is a commercial product, not a precision instrument. The standard is "would this look acceptable in a professional Etsy listing photo?"

**Accept:**
- Visible layer lines on non-engagement surfaces (this is expected for FDM)
- Minor stringing that can be removed by hand in under 5 seconds
- Slight elephant foot at base that does not affect fit

**Reject (stop and reprint):**
- Layer separation or delamination visible to the naked eye
- Warping exceeding 1mm at any edge when placed on a flat surface
- Visible voids or gaps in walls
- Stringing dense enough to be visible in photos without post-processing
- Any sharp flash or burrs at the clip jaw (these will scratch cable jackets)
- Color inconsistency: gradient or fading suggesting filament issue

**Pass standard**: All five clips pass visual inspection. At least four of five are photo-ready without any cleanup work.

### 1.4 Assembly Confirmation

- [ ] Assemble one complete rail+clip unit as a customer would receive it.
- [ ] Photograph the assembled unit from three angles: front, side, top.
- [ ] Confirm the assembly would survive shipping: no parts can fall off during normal handling.
- [ ] Confirm no sharp edges that a customer would encounter when installing.

### 1.5 Print Settings Confirmation (Record These Permanently)

The settings that produced your successful test print are now your production baseline. Record them immediately.

| Parameter | Value |
|---|---|
| Nozzle temperature | _______ °C |
| Bed temperature | _______ °C |
| Layer height | _______ mm |
| Infill percentage | _______ % |
| Print speed | _______ mm/s |
| Filament brand and color | _______ |
| Bambu profile used | _______ |
| Total print time | _______ min |

Save this to a text file in the `stl/` directory as `production-settings.txt`. This becomes the canonical settings file. Every future production run starts from these settings.

### 1.6 No-Go Protocol

If any test in 1.1–1.4 fails, do the following before touching anything else:

1. Photograph the failure with a ruler or caliper in frame.
2. Open the CadQuery source file for the failing component.
3. Identify which parameter controls the failing dimension (jaw width, channel diameter, etc.).
4. Adjust that single parameter by the measured deviation. Do not adjust multiple parameters at once.
5. Export new STL, slice with production settings from 1.5.
6. Print one clip (not a full batch).
7. Re-run only the tests that previously failed.
8. Repeat until all tests pass.

Do not proceed to Part 2 until all tests in Part 1 pass.

---

## Part 2: Etsy Listing Finalization (Days 1–5)

### 2.1 Mockup Review Checklist

Before publishing any listing, verify every visual element against this list.

**Primary thumbnail (most important image):**
- [ ] Lifestyle photo showing clips installed on a real desk — cables organized, not a white-background product shot
- [ ] The clip is legible at 300x300px (Etsy's mobile square crop)
- [ ] No text overlaid on the image (Etsy penalizes this in some categories)
- [ ] Color of clips in photo matches the color listed in the title
- [ ] Desk in photo looks professional — no clutter visible that is not intentional styling

**Image sequence (7 images total if possible):**
1. Lifestyle hero: clips installed, desk context, real cables
2. Close-up of clip jaw mechanism showing cable fit
3. Scale reference: clip next to a USB-A port or ruler
4. Color variant lineup (black, white, grey minimum)
5. Rail-plus-clip assembly showing the full system
6. Pack size comparison (3-pack vs. 20-pack side by side)
7. Installation step sequence (3-panel showing: peel adhesive backing, press to desk, snap cable in)

**Video (optional but recommended):**
- 15–30 seconds showing a cable snapping into the clip
- No music is better than bad music
- Record horizontal, not vertical

If you are using Canva for mockups before professional photos are ready, Canva's Smartmockups or Placeit can place your product render onto a realistic desk environment. This is an acceptable short-term substitute for real photos if your test print is not yet photogenic. Replace with real photography within 14 days.

### 2.2 Title and Tag Optimization

Reference `etsy-seo-strategy.md` for full keyword research. These are the production-ready values.

**Listing 1 — Cable Clips (3-pack, entry point):**

Title (exact):
```
Cable Management Clips — 3D Printed, Modular | Desk Wire Organizer | Custom Colors Available
```
Character count: 95 — first 40 characters visible on mobile: "Cable Management Clips — 3D Printed, Modul"

Tags (all 13, in priority order):
```
desk cable organizer
wire management clips
cord organizer desk
cable clip holder
home office organization
3D printed accessories
gaming setup accessories
desk setup organization
work from home gift
minimalist desk decor
cable management gift
standing desk clips
monitor cable holder
```

**Listing 2 — Starter Kit Bundle (1 rail + 3 clips):**

Title (exact):
```
Desk Cable Organizer System | Modular Cable Clips | 3D Printed Wire Management for Home Office
```

Tags:
```
complete cable management kit
desk cable organizer system
modular cable management
standing desk cable organizer
home office desk accessories
cable management system
3D printed cable management
desk setup cable management
desk organization gift
work from home setup
gaming desk cable organizer
under desk cable management
cord management desk
```

**Listing 3 — 20-Clip + 2-Rail Bundle (highest-margin SKU):**

Title (exact):
```
Cable Management Kit 20-Pack — 3D Printed Modular | Desk Wire System | Home Office Gaming Setup
```

Tags:
```
desk setup organization
gaming setup accessories
home office cable organizer
cable management clips
3D printed desk accessories
desk cable management kit
minimalist cable management
standing desk accessories
work from home desk organizer
cable clip organizer
monitor cable holder
desk organization system
gaming desk wire management
```

### 2.3 Description Framework

Use this structure for every listing. Fill in the bracketed sections with actual numbers from your production settings and COGS model.

**Opening (first 250 characters — these display in search previews):**

> Cable clutter is a precision problem. Generic clips either hold too loosely or grip too hard. ModRun cable management clips are parametrically designed to tolerance — jaw width measured in fractions of a millimeter, not "approximately fits."

**Core function section:**
- Jaw width: [dimension]mm
- Compatible cable diameters: 3mm–10mm (USB-C, HDMI, ethernet, USB-A, aux)
- Material: PLA+ (rigid, not flexible — permanent installation)
- Adhesive: 3M VHB tape included (desk surface safe, removable)
- Available colors: Black, White, Grey [add any confirmed colors]

**Options section:**
- What sizes/quantities you offer and their prices
- Custom color availability and lead time
- Note that the rail system is sold separately (link to Listing 2)

**Social proof hook (update this after first 10 reviews):**
> Rated [X].X stars by [N] customers. Questions? Message the shop — response within 24 hours.

**Cross-sell close:**
> Part of the complete ModRun system. Add a mounting rail (sold separately) to build a modular cable management run along your entire desk edge.

**Keyword density check**: The phrase "cable management" or "cable clips" should appear naturally 3–4 times in the first 300 words. Do not stuff. Etsy's NLP recognizes semantic variants.

### 2.4 Pricing Configuration

These are the production prices based on the cost model. Do not undercut them.

| SKU | COGS at 20/week | Target retail | Gross margin | Notes |
|---|---|---|---|---|
| 3-clip Essentials Pack | $1.40 material + $4.25 shipping = $5.65 blended | $12.99 | ~57% | Entry point; builds review velocity |
| Starter Kit (1 rail + 3 clips) | ~$3.10 + $4.75 shipping = $7.85 | $28.99 | ~73% | Highest volume/margin balance |
| 20-clip + 2-rail Bundle | ~$4.50 + $5.50 shipping = $10.00 | $44.99–$49.99 | ~78% | Highest-margin SKU; push this |
| Single clip (inquiry/custom) | ~$0.90 + $4.25 shipping = $5.15 | $8.99 | ~43% | Only list to capture search; push upsell |

**Shipping strategy**: Charge for shipping on individual clips and Essentials packs. Offer free shipping on Starter Kit and Bundle. This improves the bundle's perceived value and aligns with Etsy's algorithm preference for lower-priced-looking shipping signals on higher-AOV orders.

**Etsy fee math (to internalize):**
- Etsy transaction fee: 6.5% of item price + shipping
- Etsy payment processing: 3% + $0.25 per transaction
- Listing fee: $0.20 per listing (not per sale, per new listing published)
- Net after fees on $28.99 Starter Kit (with $0 shipping): ~$25.70

### 2.5 Shop Settings Before Publishing

These must be set before any listing goes live or the first order will have no policy protection.

- [ ] Shop announcement written (160 chars max): "Original parametric cable management for creators and professionals. Ships in 2 business days."
- [ ] Processing time: set to 2 business days on all listings
- [ ] Return policy: "Returns accepted within 30 days if item arrives damaged. Contact me first." This is the minimum needed to protect Star Seller qualification.
- [ ] Shipping profile created with USPS Ground Advantage, calculated rates
- [ ] Shop sections created: "ModRun Essentials," "ModRun Starter Kits," "ModRun Bundles"
- [ ] About section completed (minimum 3 sentences about the design and manufacturing process — this signals to Etsy that you are an original-design seller)
- [ ] Profile photo uploaded
- [ ] Banner image uploaded
- [ ] All shop policies filled in (returns, shipping, privacy)

### 2.6 Publish Sequence

Do not publish all listings at the same time. Each listing gets a 7–14 day recency boost when first published. Stagger them to maintain some boost-driven impressions while each listing builds organic history.

**Publication schedule:**
- Day 5 (or when photos are ready, whichever is later): Publish Listing 1 (Essentials 3-pack)
- Day 7: Publish Listing 2 (Starter Kit)
- Day 10: Publish Listing 3 (20-clip + 2-rail Bundle)

**Optimal publish time**: Wednesday or Thursday, between 10 AM and 2 PM Eastern. Etsy traffic peaks Thursday afternoon.

**After publishing each listing:**
1. Search Etsy for "cable management clips" and confirm your listing appears (may take 24 hours to index).
2. Check that the thumbnail crops correctly on mobile.
3. Click through the listing as a buyer would — confirm price, photos, and description render correctly.

---

## Part 3: Supplier Contact Sequence (Days 1–21)

This section tells you exactly who to contact, in what order, and what to say. Do not skip steps or change the sequence without understanding why the sequence is designed this way.

### 3.1 Why This Sequence Matters

The contact sequence is designed around two priorities: (1) get a usable supply agreement in place before your Etsy traffic peaks, and (2) use competition between suppliers to create leverage without burning relationships.

You contact Anycubic before eSUN because Anycubic responds in 2–5 days while eSUN takes 1–3 weeks. You use Anycubic's faster response to create urgency in your eSUN conversation. You do not contact Polymaker until Month 2 because their MOQ ($1,000 minimum order) is premature at launch volumes.

### 3.2 Day 1 Contacts (Send All Three This Day)

**Contact 1 — Anycubic (Primary Backup; fastest to respond)**

Contact channel: store.anycubic.com → Contact/Wholesale inquiry form, or wholesale@anycubic.com
Subject: Wholesale Inquiry — 3D Print Production Business, 20–50kg/Month PLA

Body:
> Hi Anycubic team,
>
> I'm scaling a 3D print production business focused on cable management accessories. Currently printing on a Bambu P1S AMS system. Monthly PLA consumption is approximately 20–30kg now, scaling to 50kg within 3 months.
>
> I'm comparing wholesale options for my primary filament supplier. I saw your 50kg pallet pricing at $10.49/kg. I'd like to understand:
> - Is that pricing available without MOQ constraints, or do I need to commit to a full pallet?
> - Do you offer any additional pricing for monthly volume commitments?
> - What's your current lead time from order to delivery (US warehouse)?
>
> I'm making a primary supplier decision this week. Happy to share projected volumes if helpful.
>
> Best,
> [Your name]

**What you want from this email**: A confirmed price per kg at 10–50kg quantities, and a lead time. That is all. Do not negotiate yet — just get numbers.

**Contact 2 — eSUN Direct (Target Primary Supplier)**

Contact channel: esun3dstore.com → Wholesale/contact form
Subject: Wholesale Inquiry — Monthly PLA Commitment, 20–50kg

Body:
> Hi eSUN team,
>
> I operate a production 3D printing business (Bambu P1S, AMS system) manufacturing cable management accessories. I'm evaluating direct wholesale relationships for PLA+ 1.75mm. Current and projected monthly volume:
>
> - Month 1: 15–20kg
> - Month 3: 30–50kg
> - Month 6: 50–100kg
>
> I've been purchasing your 10kg bundles via Amazon at approximately $12/kg. I'm interested in understanding your direct wholesale pricing at these volume levels, payment terms, and lead times from your US warehouse.
>
> I'm finalizing a supplier decision within two weeks. Would a 15-minute call work, or can you send over a quote sheet?
>
> Best,
> [Your name]

**Contact 3 — Push Plastic (Domestic Tariff Hedge — Pre-Qualify Only)**

Contact channel: pushplastic.com → Bulk Pricing Application form
Message:
> Interested in domestic PLA sourcing as a hedge against tariff escalation. Currently running 15–20kg/month, expecting 50kg+ by Q4 2026. Looking to understand your pricing tiers and lead times. No immediate order — evaluating options.

This email is low-stakes. You are establishing a relationship before you need it. Push Plastic does not need to become your primary supplier — but having a domestic option on file before a tariff escalation forces you to scramble is worth the 10-minute investment.

### 3.3 Days 3–5: Anycubic Response (Expected)

When Anycubic responds (expect 2–5 days), your goal is to lock in a trial order to pre-qualify their filament before depending on it.

**If their quoted price is at or below $10.50/kg at 10kg:**
Reply:
> Thanks for the quick response. That pricing works for an initial order. I'd like to place a test order of 10kg (black PLA Basic) to validate AMS compatibility on my Bambu P1S before committing to larger volumes. Can you confirm the order process and expected delivery time?

**If their quoted price is above $10.50/kg at 10kg:**
Reply:
> Thanks. I'm seeing your 50kg pallet listed at $10.49/kg on your store. Is there a path to that pricing at 10–20kg for an initial order, with a commitment to scale to 50kg within 90 days? I'm comparing with two other suppliers this week.

Do not anchor below $10.49/kg on the first counter. You are trying to match their public pricing, not squeeze them below it.

**Pre-qualification test order (if they accept):**
Order 5–10kg of black PLA Basic. When it arrives:
- [ ] Run a 3-hour AMS job with this filament uninterrupted
- [ ] Print 10 clips and measure tolerances against your production baseline
- [ ] Check for diameter consistency: measure 5 spots on the spool with calipers (target ±0.02mm)
- [ ] Log lead time from order to doorstep
- [ ] Note packaging (vacuum sealed vs. open bag)

Score against your production baseline. If it passes, Anycubic becomes your secondary supplier. If it fails AMS feeding, it stays as an emergency-only option.

### 3.4 Days 7–14: eSUN Response Window

eSUN typically responds in 1–3 weeks. If you haven't heard back by Day 10, send one follow-up:
> Hi, following up on my wholesale inquiry from [date]. Still evaluating primary suppliers — would love to include eSUN in the comparison. Can you send a quick price sheet at 20kg and 50kg/month volume levels?

**When eSUN responds**, compare their wholesale price to:
- Your current Amazon bundle price (~$12/kg for eSUN 10kg)
- Anycubic's quoted price (~$10.49/kg)

**eSUN negotiation target**: $10.00–$11.00/kg at 20kg/month commitment. This is achievable.

If eSUN's wholesale price is lower than Anycubic's: make eSUN your primary. Keep Anycubic as backup.
If eSUN's wholesale price matches or beats Anycubic only at higher quantities: use Amazon bundles as primary for now, switch to eSUN direct at Month 3.

### 3.5 Days 14–21: Supplier Decision and First Bulk Order

By Day 14 you should have quotes from at least Anycubic and eSUN (possibly both).

**Decision framework — choose Primary Supplier:**

| Criterion | Weight | Anycubic | eSUN direct |
|---|---|---|---|
| Price at 10kg | 40% | ~$10.49/kg | ~$11–12/kg (to be confirmed) |
| AMS compatibility (from test order) | 30% | TBD from test | 9/10 confirmed |
| Lead time | 20% | 3–7 days | 5–7 days |
| Payment terms | 10% | Card/prepay | Card or potential Net-30 |

Fill in Anycubic's AMS score from your test order before deciding. If Anycubic passes AMS testing and is $1–1.50/kg cheaper, make them primary despite the lower reputation score. If they fail AMS testing, stay on Amazon eSUN bundles until eSUN direct pricing comes back.

**First bulk order:**
- Order 3x your expected monthly consumption. At 20 units/week (20g average per unit), that is 20 units × 4 weeks = 80 units × 75g average = 6kg/month. 3x = 18kg.
- Round up to the nearest price break: order 20kg.
- Confirm with supplier that this initiates the wholesale relationship.

### 3.6 Month 2 Contacts (Do Not Do These Before Month 2)

These contacts are premature at launch. Add them to your calendar for Day 45.

- **Overture PETG wholesale** (overture3d.com/pages/wholesale): Contact when PETG SKU is confirmed at 30+ units/month. Ask for 35% wholesale discount program.
- **Polymaker wholesale** (us-wholesale.polymaker.com): Contact when monthly filament spend exceeds $500. Minimum order $1,000. Their value is payment terms (Net-30) and quality consistency, not per-kg price.

---

## Part 4: Production Run Sizing and SKU Strategy

### 4.1 Initial Production Run

For Week 1, print in small batches aligned to expected order velocity. Do not build inventory you cannot sell. Etsy listing conversion for a new shop in a competitive category is typically 1–3% of views. With 50–200 views/day in Week 1 (realistic for a new listing with recency boost), expect 0–6 orders/day in the first week.

**Week 1 production target**: 20 units. This covers 3–5 orders with bundle-level quantities.
**Week 2 production target**: 30 units. Build a 3-day buffer.
**Week 3–4**: Match production to actual order velocity (daily average × 5 days = weekly run).

Print to order, not to inventory, for the first 30 days. The risk of overstocking outweighs the risk of short-term stockouts at this volume. A 1–2 day delay on an order is acceptable. A $500 inventory write-off of unsellable clips is not.

### 4.2 SKU Launch Sequence

Do not launch all SKUs simultaneously. Each Etsy listing needs time to build its own LQS. Launch in this order:

**Week 1 — Listing 1 only (Essentials 3-pack, $12.99)**
Rationale: Lowest price point = most clicks = fastest LQS accumulation = fastest path to first review. You need reviews before you push high-AOV bundles.

**Week 2 — Add Listing 2 (Starter Kit, $28.99)**
Rationale: Once you have 2–3 reviews on Listing 1, the shop has credibility. Now add the higher-margin SKU.

**Week 3 — Add Listing 3 (20-clip + 2-rail Bundle, $44.99–$49.99)**
Rationale: Bundle buyers tend to be more deliberate. They will look at your reviews before committing $45–$50. Wait until you have at least 5 reviews before publishing this.

**Week 4+ — Consider single-clip listing ($8.99)**
Add only if you are seeing search impressions for "cable clip" single-unit queries in your Etsy Stats dashboard. This SKU is primarily a search-entry-point, not a revenue driver.

### 4.3 Bundle Configuration (Production-Ready)

These are the confirmed SKU configurations based on the bundle strategy analysis. Use these as-is.

**SKU B1 — Essentials 3-Pack**
- 3x cable clips (mixed sizes: 1 × 8mm jaw, 1 × 10mm jaw, 1 × 12mm jaw recommended; or all 10mm if single-size design)
- Color: customer choice (black default)
- Packaging: 9x12" poly mailer, clips in zip bag, thank-you card
- Filament: 3 × ~4g = 12g total per order
- Print time: ~35 minutes
- List price: $12.99 + shipping

**SKU B2 — Starter Kit**
- 1x aluminum/PLA rail (500mm, or your current rail design length)
- 3x standard clips
- Packaging: poly mailer (this fits if rail is printed in sections) or small box if rail ships assembled
- Filament: rail ~85g + 3 clips ~12g = ~97g total
- Print time: ~90 minutes
- List price: $28.99, free shipping

**SKU B3 — 20-Clip + 2-Rail Bundle**
- 20x clips (all 10mm jaw; mixed sizes add complexity at this quantity)
- 2x rails
- Packaging: padded mailer or small box, clips in zip bags organized by size
- Filament: 20 clips ~80g + 2 rails ~170g = ~250g total
- Print time: 4–5 hours (batch print clips overnight, rails separately)
- List price: $44.99–$49.99, free shipping
- Margin note: This is your highest-margin SKU. At $47.99 with ~$10.00 COGS at 20/week volume, gross margin is approximately 79%.

---

## Part 5: Shipping and Packaging Strategy

### 5.1 Shipping Setup (Do Before First Order)

- [ ] Create account at pirateship.com (free)
- [ ] Connect your Etsy shop to Pirate Ship (OAuth integration — takes 5 minutes in Pirate Ship dashboard → Stores)
- [ ] Verify commercial rate pricing for your most common order type:
  - Essentials 3-pack (approximate weight: 50–80g + packaging = 150g total): USPS First Class Package, ~$4.25 at commercial rates
  - Starter Kit (~400g total): USPS Ground Advantage, ~$5.25–$6.50 depending on zone
  - 20-clip Bundle (~600g): USPS Ground Advantage, ~$6.50–$8.50 depending on zone

Run a rate calculation on Pirate Ship using your ZIP code and three representative destination ZIPs (local, cross-country, mid-range) before setting Etsy's shipping rates. Zone matters significantly — a 600g parcel to Zone 8 (West Coast to East Coast) costs $2–3 more than Zone 2.

Note: USPS has a temporary 8% surcharge active from April 26, 2026 through January 17, 2027. This is already priced into Pirate Ship's displayed commercial rates.

### 5.2 Packaging Materials Checklist

Order before your Etsy listing goes live. Lead time on poly mailers from Shop4Mailers is 3–5 days.

- [ ] 9x12" poly mailers, 2.5mil (Shop4Mailers: 1000-count at ~$0.05/unit). Fits Essentials packs and Starter Kits without rails.
- [ ] Small cardboard box (6x4x3" or similar) for Starter Kit if rail cannot fold into a poly mailer. Local ULine or Amazon. Target: $0.25–0.40/unit.
- [ ] Zip bags (4x6", 2mil): for organizing clips inside mailers. Amazon pack of 200 for ~$6.
- [ ] Thank-you card: print at home on card stock. 3x4" size. Include shop URL, QR code to shop, and a one-line review request.
- [ ] Clear tape + packing tape: for sealing poly mailers and boxes.
- [ ] Kitchen scale (if you don't have one): for weighing packages before creating labels. Target: 0.1g precision, postal-approved. Amazon, ~$12–20.

**First order minimum supplies**: 50 poly mailers, 1 small box roll, 50 zip bags, 50 thank-you cards. This covers your first 2–4 weeks.

### 5.3 Weight Calculations

Use these to set accurate calculated shipping weights in Etsy's shipping profile. If you underestimate, you eat the difference. If you overestimate, buyers pay more than necessary (harms conversion).

| Order | Clip+rail weight | Packaging weight | Total shipped weight | USPS service |
|---|---|---|---|---|
| Essentials 3-pack | ~40g | ~50g (mailer + card) | ~90g | First Class Package |
| Starter Kit | ~100g (clips) + ~90g (rail) = 190g | ~100g (mailer or light box) | ~290g | Ground Advantage |
| 20-clip + 2-rail | ~80g clips + ~180g rails = 260g | ~150g (padded mailer or box) | ~410g | Ground Advantage |

Set Etsy's package dimensions accurately. USPS Ground Advantage is dimensional-weight priced above certain thresholds. For your product sizes, actual weight dominates, but enter real dimensions anyway.

### 5.4 Margin Impact of Shipping by SKU

Understand this before pricing. Shipping is your largest COGS component on single-unit orders.

| SKU | List price | Est. shipping | Net after Etsy fees | Shipping as % of net |
|---|---|---|---|---|
| Essentials 3-pack ($12.99 + $4.50 shipping) | $12.99 | $4.50 (buyer pays) | $11.65 | Buyer-absorbed |
| Starter Kit ($28.99, free shipping) | $28.99 | ~$5.50 (you absorb) | $25.70 | 21% of net |
| 20-clip Bundle ($47.99, free shipping) | $47.99 | ~$7.00 (you absorb) | $43.30 | 16% of net |

The bundle model works because the fixed shipping cost becomes a smaller percentage of revenue as AOV increases. A $5.50 shipping cost on a $28.99 order is 19%. On a $47.99 order it is 15%. This is why pushing buyers toward bundles is not just a revenue tactic — it is the primary margin mechanism.

### 5.5 Packaging Upgrade Timeline

Launch with plain poly mailers. Do not spend on custom packaging until you have 20+ orders per week.

| Volume threshold | Packaging upgrade | Cost per unit | When to activate |
|---|---|---|---|
| 0–20 orders/week | Plain 9x12" poly mailer | $0.05 | Launch through Month 2 |
| 20–50 orders/week | Plain mailer + printed thank-you card with QR code | $0.08 | Month 2+ |
| 50+ orders/week | Custom-printed mailer (Packlane, 500-unit minimum, ~$0.76–$1.10/unit) | ~$1.00 | Month 4+ |

Custom packaging at Packlane requires 10–14 day lead time and a minimum of 500 units. Do not order custom packaging until you have consistent 50+/week velocity to avoid sitting on 400 unused custom mailers.

---

## Part 6: Week-by-Week Timeline

This is the ground-level schedule. Every item is either done on that day or moved to the next available slot — there is no "later" bucket.

### Day 0 (Test Print Confirmation Day)

Morning:
- [ ] Run full physical validation protocol (Part 1: 90 minutes)
- [ ] Confirm go/no-go decision
- [ ] Record production settings to file

Afternoon (if Go):
- [ ] Send supplier contact emails to all three: Anycubic, eSUN, Push Plastic (30 min)
- [ ] Order packaging materials: poly mailers, zip bags, thank-you card stock (15 min on Amazon/Shop4Mailers)
- [ ] Open Etsy seller account if not already open (30 min)
- [ ] Draft Listing 1 title, tags, description in Etsy draft mode — do not publish yet (45 min)
- [ ] Identify a photographer: search Fiverr for "product photography Etsy" or "3D printed product photography." Send photography brief (`post-test-print-doc-3-lifestyle-photography-brief.md`) to three candidates.

End of Day 0 deliverable: Three supplier emails sent. Etsy account exists. Listing 1 is in draft. Photographer search initiated.

### Day 1

- [ ] Confirm receipt of supplier emails (no response yet — that is fine)
- [ ] Complete Etsy shop settings (2.5 above): policies, shipping profiles, shop sections, about page
- [ ] Draft Listing 2 (Starter Kit) in draft mode
- [ ] Print a second batch of 5 clips for photography samples (these will be your hero props)
- [ ] Select packaging (confirm your poly mailer order was placed)
- [ ] Create a simple tracking spreadsheet: columns are Date, Listing, Views, Clicks, Favorites, Orders, Revenue. You will update this daily.

### Day 2

- [ ] Anycubic may respond (check email)
- [ ] If photographer responded: review quotes, select one, send the brief document
- [ ] Draft Listing 3 (20-clip Bundle) in draft mode
- [ ] Print a complete assembly for photography: 1 full rail + 3 clips installed
- [ ] Review all three draft listings together: do the titles sound distinct? Do the tags overlap without being identical?

### Day 3

- [ ] Confirm photographer shoot date. Target: Day 7–10.
- [ ] If Anycubic responded: review their quote against the decision framework (3.5). Reply with test order request.
- [ ] Finalize pricing on all three listings. Run the margin calculation for each SKU against your actual COGS.
- [ ] Create Pirate Ship account and connect to Etsy. Run rate estimate for each SKU (5.1).
- [ ] Packaging materials should arrive around now. Confirm receipt.

### Day 4–5

- [ ] Set up your shipping station: scale, tape, labels, mailers, zip bags all in one location
- [ ] Create the daily fulfillment process on paper: sequence of steps from "order notification" to "label printed to drop at USPS." You are designing muscle memory before you need it under order pressure.
- [ ] If eSUN has responded: log their quote, begin comparison
- [ ] Test print 2–3 units of each SKU component to ensure production workflow is repeatable

### Day 6

- [ ] Confirm photographer shoot for Day 7 or 8
- [ ] Prepare props for shoot: desk setup, cables, any props listed in the photography brief
- [ ] If not using a professional photographer: take your own lifestyle photos today using natural window light, phone camera, and the assembled clips on a real desk. These will not be your final photos but can get the listing live sooner.
- [ ] Have the Etsy listings 90% complete in draft (all text, no photos)

### Day 7 (Target: First Listing Goes Live)

Option A (photographer shoots today):
- [ ] Complete shoot (2 hours)
- [ ] Photographer delivers edited photos within 24 hours
- [ ] Continue to Day 8

Option B (using your own photos for now):
- [ ] Upload your best lifestyle photo as thumbnail for Listing 1
- [ ] Publish Listing 1 at 10 AM–2 PM your time
- [ ] Note: Plan to replace with professional photos within 7 days

### Day 8

If using professional photographer:
- [ ] Receive photos
- [ ] Upload to Listing 1, 2, 3 in Etsy draft
- [ ] Publish Listing 1 now (10 AM–2 PM)

### Day 10

- [ ] Publish Listing 2 (Starter Kit)
- [ ] Check Etsy Stats: is Listing 1 getting impressions? At least 10 views in first 72 hours is a healthy signal.
- [ ] Anycubic test order should have arrived (if ordered Day 3). Run AMS test.

### Day 14

- [ ] Publish Listing 3 (20-clip Bundle) — only if Listing 1 has at least 3 views/day and no major issues flagged
- [ ] eSUN direct response likely by now. Compare pricing and decide primary supplier.
- [ ] Check Etsy Search Visibility page (Shop Manager → Marketing → Search Visibility). Look for any listings flagged with low visibility scores.

### Week 3 (Days 15–21)

- [ ] Supplier negotiation conclusion: by Day 21, you must have selected a primary supplier and have a confirmed pricing agreement (even if informal via email)
- [ ] Place first bulk filament order (Part 3.5: target 20kg)
- [ ] If you have received your first order: fulfill it within 24 hours. Message the customer same-day of purchase. Ship within 2 business days.
- [ ] Review first-week Etsy performance: views, click-through rate, favorites. If CTR is below 1%, the thumbnail needs to change.
- [ ] Respond to any Etsy messages within 24 hours — this is the response rate metric that feeds Star Seller qualification.

### Week 4 (Days 22–28)

- [ ] First bulk filament order arrives
- [ ] Etsy listings have been live 14+ days — check if any are gaining organic traction (rising views without paid ads)
- [ ] If you have 3+ reviews: consider enabling Etsy Ads at $1–2/day on Listing 2 (Starter Kit) to accelerate LQS.
- [ ] Contact Anycubic or eSUN about moving to a monthly order rhythm
- [ ] Begin planning headphone hook addition to shop (Phase 2, not before Week 4)

---

## Part 7: Success Criteria (Know When You Have Launched)

You have completed the launch when all of these are true simultaneously:

1. All three primary Etsy listings are live and indexed (verified in search)
2. At least one supplier has confirmed pricing and you have placed one bulk order
3. You have fulfilled at least one customer order door-to-door
4. Your daily fulfillment process can be completed in under 3 hours (print → pack → label)
5. You have at least one verified 5-star review
6. Packaging materials are stocked to cover 2 weeks of expected demand
7. Your tracking spreadsheet has at least 7 days of data

When all seven are true, you have launched. Everything after this is operations and growth.

---

## Quick Reference: Key Numbers

| Metric | Value | Source |
|---|---|---|
| Target COGS (20/week, blended) | $6.77/unit blended | cost-model-spreadsheet.csv |
| Target gross margin (Starter Kit) | 72–73% | bundle-strategy.md |
| Bundle gross margin (20+2 SKU) | ~78–79% | calculated from COGS model |
| Filament target price (primary) | $10.49–$12.00/kg | supplier-economics.md |
| Review rating minimum for Star Seller | 4.8 stars | etsy-seo-strategy.md |
| Star Seller message response requirement | 95% within 24 hours | etsy-seo-strategy.md |
| Etsy transaction + payment fee | ~9.5% of revenue | etsy-seo-strategy.md |
| January search intensity vs. baseline | 120–150% | etsy-seo-strategy.md |
| Optimal publish time | Wed/Thu, 10 AM–2 PM ET | etsy-seo-strategy.md |
| USPS surcharge active through | January 17, 2027 | supplier-economics.md |

---

*All source documents are in `/home/awank/dev/SuperClaude_Framework/projects/mfg-farm/`. The execution index at `post-test-print-EXECUTION-INDEX.md` links to five detailed pre-staging documents (email templates, listing templates, photography brief, operations SOP, supplier matrix) that expand on every section above.*
