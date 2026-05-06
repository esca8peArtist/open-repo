---
title: Post-Test-Print Revenue Maximization Sequence — 4-Week Execution Plan
project: mfg-farm
created: 2026-05-06
status: execution-ready — triggers on test-print success confirmation
scope: Days 1–28 post-test-print pass; ModRun refinement + Headphone Hooks launch coordination
confidence: high — all materials complete; timing is coordinated, resource-dependent only on test-print outcome
audience: Anya
target-outcome: $6,900–$7,500/month baseline (ModRun + Product 2 live) vs. $2,500 current
---

# Post-Test-Print Revenue Maximization Sequence

**Status: BLOCKING until test print succeeds.** The moment you confirm "test print is good," clock starts on this plan. All materials are ready; this document is the day-by-day execution map.

**High-level goal:** Scale ModRun production AND launch Headphone Hooks Product 2 in parallel (Weeks 2–4), hitting $600–$800 cumulative gross revenue in Month 1, ramping to $6,900–$7,500/month by Month 6.

---

## Pre-Sequence: Pre-Test-Print Actions (Start Now, Don't Wait)

These actions have zero dependencies on test-print success. Execute now to save 1–2 weeks post-test-print.

| Task | Owner | Timeline | Dependencies | Status |
|---|---|---|---|---|
| Order silicone bumper pads (100-pack, AliExpress 3M Bumpon SJ5302) | Anya | Today | Payment method | READY |
| Confirm filament inventory: 500g+ Matte Black PLA+ available | Anya | Today | Existing stock | READY |
| Create Etsy draft folder for upcoming listings; copy template from `headphone-hooks-etsy-listing.md` into Etsy UI | Anya | This week | Etsy account | READY |
| Verify Pirate Ship account for shipping label printing (test 1 label) | Anya | This week | Pirate Ship login | READY |
| Review final photography setup: desk, lighting, headphones props — no new purchases needed | Anya | This week | Existing setup | READY |

**Blocker release:** Once you post "test print complete + passes QA," message the confirmation and **Day 1 of this sequence begins immediately.**

---

## Timeline Overview: Weeks 1–4 Post-Test-Print

```
WEEK 1: Design validation + initial photography
WEEK 2: STL refinement + Etsy draft listings
WEEK 3: Inventory build + launch coordination
WEEK 4: Publish + first orders + optimization
```

**Parallel workstreams:**
- **Stream A (ModRun Refinement):** STL tweaks, supplier outreach, Etsy optimization
- **Stream B (Headphone Hooks Launch):** Photo shoots, QA, listing creation, inventory build
- **Stream C (Social + Email):** Content calendar, cross-sell setup, launch announcement

All streams run in parallel with coordinated timing gates (checkpoints).

---

# WEEK 1: Design Validation & Photography Foundation

## Day 1–2: ModRun STL Refinement Sequence

**Trigger:** Test print completes successfully.

### Actions

1. **Review test-print results** (30 min)
   - Inspect rail clamp grip: is jaw pressure adequate? Does it grip 6mm desk without slipping?
   - Inspect clip snap-fit: are press-fit tolerances tight? Any cracking on first install?
   - Photograph test-print artifacts (if any issues exist)
   - Document observations in commit message

2. **Generate refined STLs** (15 min)
   ```bash
   cd projects/mfg-farm/cadquery
   python modrun_rail.py --tolerance 0.20 --output-dir ../stl/
   python modrun_clip.py --tolerance 0.20 --output-dir ../stl/
   ```
   - If test print showed loose jaw: reduce tolerance to 0.15
   - If test print showed tight fit: increase tolerance to 0.25
   - Save refinement notes in git commit with exact tolerance value used

3. **Commit design lock** (5 min)
   ```bash
   git add projects/mfg-farm/stl/modrun_rail_*.stl projects/mfg-farm/stl/modrun_clip_*.stl
   git commit -m "fix(modrun-stl): Refinement post-test-print — tolerance locked at 0.20mm on Bambu P1S eSUN PLA+"
   ```

### Deliverable
- Refined STLs committed and ready for production batch printing

---

## Day 1–3: Headphone Hooks — Print & Fit-Test Sequence

**Parallel to ModRun refinement; starts same time.**

### Actions

1. **Generate headphone hook STLs** (10 min) — if not yet done
   ```bash
   cd projects/mfg-farm/cadquery
   python headphone_hooks.py --output-dir ../stl/
   ```
   Outputs three variants: 12mm, 25mm (standard), 40mm

2. **Print & fit-test 25mm variant** (60 min active work + 25 min print time)
   - Slice 25mm_with_post in Bambu Studio: 0.20mm layer, 25% gyroid, 3 perimeters
   - Launch print (25 min)
   - While printing: measure actual desk edge thickness in workspace with calipers (critical for fit validation)
   - Cool 30 min after print
   - Test fit on 25mm desk edge or shim:
     - **Pass criteria:** Slides on with light one-hand pressure; no side-to-side rock >1mm; does not slide under 300–400g static load
     - **If too tight:** `python headphone_hooks.py --tolerance 0.25 --output-dir ../stl/` Reprint.
     - **If too loose:** Edit tolerance to 0.10 in `headphone_hooks.py`. Reprint.
     - **If passes:** Record final tolerance in git commit

3. **Test cable post** (5 min)
   - Loop USB-C cable around post (5mm OD); should have clearance
   - Post should not wobble at base
   - Fingertip across hook tip should be smooth (no sharp edge)

4. **Print three-variant batch for photography** (90 min total print time)
   - 4-unit plate of 25mm standard (one plate = ~95 min; this is your photography inventory)
   - Store on shelf in 4×6" zip bags

### Deliverable
- Tolerance locked; 25mm variant fit-tested and approved
- Four units printed and ready for photography

---

## Day 4–7: Photography Foundation (Shared Setup)

**Parallel to design work; no print dependencies after Day 3.**

### Actions

1. **Photography Session 1: ModRun System** (90 min active shooting)
   - Use existing desk setup (same as current ModRun listings)
   - Shots needed:
     - Hero: clip on rail, cable organized, clean desk → use in updated ModRun listing
     - Close-up: snap-fit install detail → use in FAQ section
     - Ecosystem: rail + multiple clips + new headphone hook → will use for cross-sell
   - 5 shots minimum; 8–10 preferred
   - Post-processing: Crop to 80% subject, +10% brightness, +5% contrast, export 2000×2000px

2. **Photography Session 2: Headphone Hooks** (60 min active shooting)
   - Use same desk/lighting setup
   - Shots needed (minimum 5 required; 7 recommended):
     1. **Hero:** Hook on desk, headphones hanging, cable looped on post (natural light, organized desk)
     2. **Cable post detail:** Close-up showing cable wrapped around post (primary differentiator)
     3. **Three sizes:** 12mm / 25mm / 40mm side by side on white background, labeled
     4. **Under-desk clamp:** Angle shot showing rubber pads, jaw geometry, desk contact
     5. **Ecosystem:** Hook + ModRun rail in same frame (cross-sell photo)
     6. **Color flat-lay:** 5 colors on white background (print later after color samples; skip for now if samples not ready)
     7. **Scale reference:** Hook next to ruler or household object

   - Post-processing (same as ModRun): Crop to 80%, +10% brightness, +5% contrast, 2000×2000px

### Deliverable
- 8–10 ModRun photos (5 hero/detail + 3–5 ecosystem/lifestyle)
- 5–7 Headphone Hooks photos (minimum 5; color flat-lay can be skipped if samples delayed)
- All photos edited and filed as `{product}-{shot-number}-{description}.jpg`

---

## Checkpoint 1: End of Week 1

**Verification checklist:**
- [ ] ModRun STL refined, tolerance locked, committed to git
- [ ] Headphone Hooks 25mm tolerance locked, 4-unit batch printed
- [ ] 13+ total photographs taken, edited, ready for listings
- [ ] All design work complete — zero CAD changes planned for Weeks 2–4

**Go/No-Go Gate:** If all checkboxes pass → proceed to Week 2. If any fail, resolve within 24 hours before moving forward.

---

# WEEK 2: Etsy Listings Preparation & Supplier Outreach

## Day 8–10: Etsy Listing Creation (Both Products, Draft Mode)

**No dependencies; parallel execution on both listings.**

### ModRun Listing Update (Existing Listing Optimization)

**Actions:**

1. **Navigate to existing ModRun listing** in Etsy Shop Manager (draft or live)

2. **Update "Shop Updates" section with three new photos** from Week 1 photography
   - Add ecosystem shot (ModRun rail + headphone hooks)
   - This refreshes the listing in Etsy algorithm without changing core description

3. **Update description** (add cross-sell section)
   - Insert before shipping info:
   ```
   COMPLETE YOUR DESK SETUP
   This cable management rail pairs with our headphone hook (cable post included). 
   See our headphone hook listing for cable management + desk organization.
   ```

4. **Test price increase A/B variant** (optional but recommended)
   - Current ModRun 3-clip bundle: $24.99
   - Create a listing variant (if Etsy supports): test at $29.99 for 2 weeks post-launch
   - Monitor conversion rate vs. current; if >85% of current, keep higher price

### Headphone Hooks Listing Creation (New Listing, Draft)

**Actions:**

1. **Create new listing in Etsy (draft mode only)**
   - Do not publish yet

2. **Fill title field:**
   ```
   Desk Headphone Hook with Cable Manager | 3D Printed Clamp | Custom Color
   ```

3. **Fill description** from `headphone-hooks-etsy-listing.md` Section 2
   - Replace all `{{VARIABLES}}`:
     - `{{CITY}}`: Your city
     - `{{STATE}}`: Your state
     - `{{PROCESSING_DAYS}}`: 1–3 (confirm based on print capacity)
   - Copy and paste full description from template

4. **Upload 5–7 photos** in order (use Week 1 photography)
   - Photo 1: Hero (lifestyle, headphones hanging)
   - Photo 2: Cable post detail (close-up)
   - Photo 3: Three sizes (12/25/40mm labeled)
   - Photo 4: Under-desk clamp angle
   - Photo 5: Ecosystem (hook + ModRun rail)
   - Photo 6: Color flat-lay (if color samples exist; otherwise skip)
   - Photo 7: Scale reference (if you have it; otherwise skip)

5. **Set up personalization field:**
   - Label: "Select desk thickness + color"
   - Instructions: Paste from `headphone-hooks-etsy-listing.md` Section 3

6. **Set pricing and shipping:**
   - Price: $12.99
   - Shipping: USPS First Class, buyer pays (profile: "Small item — USPS First Class" from ModRun)
   - Processing time: 1–3 business days
   - Quantity: 100 (printed to order)
   - Return policy: 14 days

7. **Add tags** (13 maximum, from `headphone-hooks-etsy-listing.md` Section 5):
   1. headphone hook
   2. desk headphone holder
   3. headset stand desk
   4. 3d printed desk accessory
   5. headphone desk clamp
   6. cable organizer desk
   7. gaming desk setup
   8. headset hanger
   9. desk organizer
   10. gamer gift
   11. home office accessory
   12. headphone stand
   13. custom 3d print

8. **Save as draft** (do not publish)

### Deliverable
- ModRun listing: updated with new ecosystem photos and cross-sell copy
- Headphone Hooks listing: complete draft with all photos, tags, personalization fields, ready to publish

---

## Day 11–14: Supplier Outreach for Bulk Pricing (Parallel to Listing Work)

**Goal:** Secure 100-unit MOQ pricing on filament + packing supplies for post-launch scaling.

### Actions

1. **Filament supplier outreach** (select top 2 of 3)

   **Template email:**
   ```
   Subject: Bulk PLA+ Inquiry — 100/month Potential | Etsy Seller

   Hi [Contact],

   I'm an Etsy seller (mfg-farm) specializing in 3D-printed desk accessories. 
   I'm currently purchasing eSUN PLA+ 10kg bundles from Amazon (~$12/kg). 
   I'm scaling production to 100–200 units/month over the next 2–3 months.

   Before ramping up to bulk orders, I'm checking pricing for:
   • 20–50 kg/month at 25+ kg/month volume
   • Consistent colors: Matte Black + Matte White preferred
   • Lead time to order → delivery

   Current supplier: eSUN (Amazon)
   Requirement: Must beat $12/kg to justify switching

   What's your best pricing for 25 kg/month commitment?
   Any volume discounts at 50+ kg/month?

   Thanks,
   [Your name]
   ```

   **Send to (in priority order):**
   1. eSUN direct: contact@esun3dstore.com
      - eSUN 10kg case bulk pricing (they offer wholesale)
   2. Anycubic direct: via store.anycubic.com contact form
      - Anycubic 50kg pallet is not worth it yet at <25 kg/month; but inquiry plants seed for Month 3
   3. Overture (Amazon): use Amazon Q&A to ask about bulk partnerships

2. **Packaging supplier outreach** (optional but recommended)

   **Actions:**
   - Pirate Ship already integrated → no change needed
   - Shop4Mailers: 1,000-pack poly mailers at $50 (~$0.05/unit vs. $0.08 current) — order Day 15
   - Bumper pads: track AliExpress order status — arrive by Day 14–21 target

3. **Save all responses** in a local file `supplier-outreach-log.txt` with dates and pricing quotes

### Deliverable
- 2–3 supplier outreach emails sent
- Pricing responses logged (responses come in over 1–3 days)

---

## Checkpoint 2: End of Week 2

**Verification checklist:**
- [ ] ModRun listing updated with new photos and cross-sell copy
- [ ] Headphone Hooks listing complete in draft mode (all photos, tags, personalization, pricing)
- [ ] Supplier outreach emails sent (2–3 vendors)
- [ ] Zero `{{VARIABLES}}` remaining unfilled in Headphone Hooks listing

**Go/No-Go Gate:** If ready → proceed to Week 3 (publish headphone hooks listing + build inventory).

---

# WEEK 3: Inventory Build & Launch Coordination

## Day 15–17: Inventory Production Sequence

**Goal:** Print 30 units of headphone hooks (20× 25mm standard, 5× 12mm, 5× 40mm) for launch week fulfillment.

### Actions

1. **Print ModRun production batch** (if planning to update current inventory)
   - 10-unit batch of modrun_rail_adhesive (or modrun_rail_desk_clamp variant)
   - 20-unit mixed batch of modrun_clip (various jaw sizes from recent orders or future queue)
   - **Timing:** Schedule these prints for "background" capacity — fill gaps between headphone hook prints

2. **Print headphone hooks: 25mm standard (primary product)** (120 min total, 5 plates)
   - Plate 1: 4 units (27 min per unit = ~95 min per plate)
   - Repeat plates 2–5 for 20 total units
   - **Timing:** Start Day 15 morning; should complete by Day 16 afternoon
   - Cool and bag each plate's output in 4×6" zip-lock bags; label by date

3. **Print headphone hooks: variants** (60 min total, 2 plates)
   - Plate 1: 4 units of 12mm variant
   - Plate 2: 4 units of 40mm variant
   - (Note: Print 4 per plate, so 5 units means 2 plates for 8 units; trim 3 for demo, keep 5 finished)
   - Cool and bag; label by variant

4. **QA + assembly: All 30 units** (90 min active work, spread across Days 16–17)
   - Inspect each unit: jaw grip, no layer artifacts, tip smooth
   - **Once bumper pads arrive** (track AliExpress status):
     - Press-fit 2 silicone pads into upper and lower jaw pockets on all 30 units
     - Pads should sit flush (±0.1–0.2mm from surface)
   - Bag all 30 units in 4×6" zip-lock bags by variant; store on shelf

### Deliverable
- 30 finished, QA'd, pad-equipped headphone hooks ready to ship
  - 20× 25mm standard (main product)
  - 5× 12mm (variant)
  - 5× 40mm (variant)

---

## Day 15–19: Launch Coordination & Cross-Sell Setup

**Parallel to inventory production.**

### Actions

1. **Prepare packaging inserts** (30 min)
   - Print 30 thank-you cards with Etsy listing URLs included
   - Alternatively, use existing thank-you cards and add a sticker label with headphone hook URL
   - Create a second insert card: "Complete your desk setup" cross-sell card with both ModRun and headphone hook Etsy links
   - Stock 30 of each insert type on desk (ready for fulfillment)

2. **Update ModRun packaging** (if not done in Week 2)
   - Add headphone hook URL to all outgoing ModRun orders (physical card insert)
   - Start Monday of Week 3; apply to all orders shipped Week 3+

3. **Plan social announcement content** (1 hour)
   - Draft Instagram post caption (60 chars max for headline)
   - Draft TikTok video script (15 seconds, two takes)
   - Draft Reddit r/battlestations post (3–4 sentences, casual)
   - Save to `social-launch-content.txt` for execution on Day 21

4. **Email list prep** (optional but recommended)
   - If you have email list from past ModRun sales, draft email:
     - Subject: "New: Parametric Headphone Hook — desk cable management included"
     - Body: 50 words max; include link + discount code (10% first-time hook order)
   - Save as draft; send on Day 22 (post-publication)

### Deliverable
- 30 packaging inserts ready
- Social content drafted and ready to post
- Email draft prepared (optional)

---

## Checkpoint 3: End of Week 3

**Verification checklist:**
- [ ] 30 headphone hooks printed, QA'd, packed, ready to ship
- [ ] Bumper pads installed on all 30 units (or marked "pending pads" if still in transit)
- [ ] ModRun and headphone hooks listings both finalized (ModRun updated, Hooks in draft ready to publish)
- [ ] Packaging inserts prepared and stocked
- [ ] Social content drafted

**Go/No-Go Gate:** Ready to publish headphone hooks listing → proceed to Week 4.

---

# WEEK 4: Launch & First-Week Operations

## Day 22–23: Publish & Social Launch

**Target publication time: Thursday 10 AM–2 PM (Etsy algorithm peak posting window)**

### Actions

1. **Publish Headphone Hooks Etsy listing** (5 min)
   - Navigate to Etsy Shop Manager
   - Click "Publish" on headphone hooks draft listing
   - Confirm listing is live within 5 min

2. **Enable Etsy Ads immediately** (10 min)
   - Budget: $1.00/day maximum
   - Campaign name: "Headphone Hook Launch"
   - Target: all 13 tags
   - Broad match

3. **Post social announcements** (30 min total)
   - **Instagram:** Schedule post for 10 AM local time (or post immediately if already past 10 AM)
     - Caption: `New: Parametric Headphone Hook — desk clamp + cable organizer in one. 12–40mm desk compatibility. $12.99. Pairs with ModRun cable system. [link] #desksetup #3dprinting`
     - Photo: Hero shot (headphones hanging, cable looped on post)
   
   - **TikTok:** Record 15-second video same day
     - Show hook installation, cable wrap, comparison to Amazon alternatives
     - Caption: `Finally, a headphone hook that actually manages cables. Etsy link in bio.`
   
   - **Reddit r/battlestations:** Post in-comment
     - Subreddit: r/battlestations
     - Format: `Designed and printed a headphone hook that manages cables. Clamps 12–40mm desks, no tools. Etsy link in comments if curious.`
     - Keep tone casual, non-salesy

4. **Send email announcement** (if email list exists)
   - Subject: "New: Parametric Headphone Hook — desk cable management included"
   - Body: Include 10% first-time discount code (create in Etsy Shop Manager)
   - Send at 9 AM or 1 PM local time (peak email open rates)

5. **Update ModRun listing with cross-sell link** (5 min)
   - Add to ModRun description: `"Complete your desk setup — see our headphone hook (cable management included) in this shop."`

### Deliverable
- Headphone hooks listing live and generating impressions
- Etsy Ads running at $1/day
- Social posts live on 2–3 platforms
- Email sent (if applicable)

---

## Day 24–28: First-Week Operations & Optimization

### Actions

1. **Order fulfillment process** (daily, 10–15 min per order)
   - Check Etsy Shop Manager each morning for new orders
   - **Fulfillment SOP:**
     1. Print shipping label via Pirate Ship (USPS First Class)
     2. Grab matching variant (12/25/40mm) from shelf
     3. Bag in 4×6" zip-lock bag
     4. Wrap in bubble wrap (2–3 wraps)
     5. Place in poly mailer (9×12")
     6. Add thank-you card + headphone hook cross-sell insert
     7. Add shipping label
     8. Tape and seal poly mailer
     9. Mark order as "shipped" in Etsy
   - **Timeline target:** Process orders within 1–3 business days of order receipt

2. **Etsy metrics monitoring** (daily, 2 min per check)
   - Review Etsy Shop Stats each morning (Track views, click-through rate, favorites)
   - **Targets for Week 4:**
     - Views: 50–100 total
     - Click-through rate: >1% from search impressions
     - Favorites: 5–10
     - Sales: 2–5 units
   
   - **If CTR <1% by Day 26:**
     - A/B test: Replace hero photo with under-desk angle photo
     - Or: Switch title to Alt A: `3D Printed Headphone Clamp Stand | Desk Hook + Cable Organizer | Custom Color`
   
   - **If views <50 by Day 27:**
     - Increase Etsy Ads budget to $2/day for next 2 weeks

3. **Customer response protocol** (aim for <4 hour response time)
   - Q&A questions: Respond same day
   - Messages from potential buyers: Respond <4 hours
   - Response time is a ranking factor for Etsy algorithm

4. **Inventory replenishment plan** (for repeat orders)
   - Each unit shipped subtracts from your 30-unit buffer
   - If >5 units ship by Day 27, start printing next 20-unit batch immediately (to be ready for Week 5 demand)

5. **Confidence check: Margin validation** (Day 28, 30 min)
   - Calculate actual COGS for units shipped:
     - Filament cost (actual grams printed ÷ $0.013/g)
     - Bumper pads (2 per unit × actual cost)
     - Packaging (actual materials used)
     - Shipping label cost
     - Etsy fees (visible in Etsy dashboard)
   - Compare to cost model: should be ~$3.13/unit all-in COGS
   - If actual >$3.50/unit: investigate which cost component rose; see margin alert protocol in revenue-ramp-metrics.md

### Deliverable
- All orders shipped within stated processing time
- Metrics tracked and optimization actions taken (if needed)
- Inventory replenishment started (if >5 units shipped)
- Confidence check passed (margin within tolerance)

---

## Checkpoint 4: End of Week 4 = Launch Complete

**Verification checklist:**
- [ ] Headphone hooks listing live and generating traffic
- [ ] 2–5 orders shipped (or >$50 revenue generated)
- [ ] Etsy metrics tracked; optimization actions taken if CTR or views below target
- [ ] Social posts live (Instagram + at least one other platform)
- [ ] ModRun cross-sell inserted into all new orders
- [ ] Margin validation passed (COGS in line with cost model)

**Success metrics:**
- Week 4 revenue target: $150–$250 from headphone hooks (3–8 units at $12.99 + shipping)
- Month 1 cumulative revenue: $600–$800 across all products (ModRun + hooks)
- Customer feedback: 0 complaints; any Q&A issues resolved promptly

---

# SUPPORTING MATERIALS: Parallel Sequences

## Sequence A: ModRun STL Refinement & Supplier Outreach

**Days 1–3:** Design refinement (described above in Week 1)

**Days 8–14:** Supplier outreach (described above in Week 2)

**Days 15–21:** Inventory balance and listing updates (parallel to headphone hooks production)

**Key decision point (Day 21):** If supplier quotes come back favorably (eSUN wholesale <$11.50/kg or Anycubic offers better rate), log in decision document for Month 2 activation.

---

## Sequence B: Social Media & Email Launch Coordination

### Platform Timeline

| Platform | Day | Time | Content | Duration |
|---|---|---|---|---|
| Instagram | 22 | 10 AM | Hero photo + caption (60 chars) | Scheduled 1 week in advance |
| TikTok | 22 | Any time | 15-sec video installation demo | Record 2–3 takes, post best |
| Reddit | 23 | 2 PM | r/battlestations casual post | Comment format, 3 sentences |
| Email | 24 | 9 AM or 1 PM | "New product" announcement + 10% code | Send if you have email list |
| ModRun packaging insert | 22 onwards | Every order | URL + description card | Print 30 copies Week 3 |

### Content Assets (Draft Now, Post Later)

**Instagram post:**
```
New: Parametric Headphone Hook — desk clamp + cable organizer in one. 
Fits 12–40mm desks. $12.99. Pairs with ModRun cable system. [link] 
#desksetup #3dprinting #homelablife
```

**TikTok script (15 seconds):**
- Scene 1 (5 sec): Hook on desk, headphones in it, zoom in on cable post
- Scene 2 (5 sec): Loop cable around post, show how clean it looks
- Scene 3 (5 sec): "Finally, a headphone hook that manages cables. Etsy link in bio."

**Reddit r/battlestations:**
```
Designed and printed a headphone hook that actually manages cables. 
Clamps 12–40mm desks, no tools, no scratching. Printed in PLA+. 
Etsy link in my profile if curious.
[Post hero photo]
[In comments, add Etsy URL and answer questions]
```

**Email subject line options:**
1. "New: Parametric Headphone Hook — 10% off for you"
2. "Headphone cable management that actually works"
3. "Your ModRun kit is incomplete without this"

---

## Sequence C: MOQ Negotiations & Pricing Tiers

### Supplier Response Processing (Days 14–21)

As supplier responses arrive:

1. **Log all quotes** in `supplier-pricing-log.csv`:
   ```
   Supplier, Price/kg, MOQ (kg), Lead Time, Notes
   eSUN Amazon, $12.00, 10, 2 days, current
   eSUN Direct, $11.50, 25, 3 days, [if they quote]
   Anycubic, $10.49, 50, 5 days, pallet only
   Overture, $12.00, 10, 2 days, backup
   ```

2. **Calculate breakeven** for each option:
   - Current spend: 20 kg/month × $12/kg = $240/month
   - eSUN wholesale (if $11.50): 20 kg × $11.50 = $230/month → $10/month savings (low)
   - Anycubic pallet (at 25+ kg/month): 50 kg × $10.49 = $524 upfront; savings = $30/month → 17-month payback (not yet justified)
   - **Decision:** Defer bulk switch until Month 3 when 25+ kg/month is sustainable

3. **Place small order with new supplier** (optional Month 2 action):
   - If eSUN wholesale quotes <$11/kg, place test order of 25 kg
   - Validate material quality matches Amazon version
   - Then commit to 50-kg pallet in Month 3

### Pricing Tier Strategy (Implement Week 4+)

Once headphone hooks have 10+ reviews, test price increase:

| SKU | Launch Price | Test Price (Week 6+) | Conversion Target |
|---|---|---|---|
| Single hook | $12.99 | $14.99 | Hold ≥80% of current conversion |
| 3-pack bundle | $32.99 | $37.99 | Hold ≥80% of current conversion |
| ModRun 3-clip bundle | $24.99 | $29.99 | Test only after hooks stabilize |

**Execution (Day 42):** If hook conversion rate >5% and average review 4.5+, enable price test in Etsy for 2 weeks.

---

# Revenue Tracking Template: Weeks 1–4

Copy this weekly and fill in actuals every Sunday at 6 PM. Update `revenue-ramp-metrics.md` with cumulative totals.

```
WEEK [N] REVENUE TRACKING — [DATE]

UNITS SHIPPED
  ModRun rails: ___
  ModRun clips (bundles): ___
  Headphone hooks (25mm): ___
  Headphone hooks (variants): ___
  Total units this week: ___

GROSS REVENUE
  ModRun revenue: $___
  Headphone hooks revenue: $___
  Total gross: $___
  Etsy fees paid: $___
  Ads spend (Etsy): $___
  Net revenue: $___

MARGIN CHECK
  Total COGS (filament + packaging + labor + depreciation): $___
  Gross margin %: ___% (should be >70%)
  If <70%: investigate which cost rose (see margin alert protocol)

INVENTORY STATUS
  ModRun clips on hand: ___
  ModRun rails on hand: ___
  Headphone hooks on hand: ___
  Filament (total kg): ___
  Bumper pads (estimated packs): ___

ETSY METRICS
  Total views (all listings): ___
  ModRun views this week: ___
  Hook views this week: ___
  Total favorites: ___
  Click-through rate (hook listing): ___%
  
ORDERS & CUSTOMER FEEDBACK
  Total orders this week: ___
  Processing time met? Yes / No
  Returns/complaints: ___
  Average review rating: ___._ / 5
  
THIS WEEK'S DECISION POINT:
  [ ] No action needed
  [ ] Increase Etsy Ads spend (if views <50/week)
  [ ] Replace hero photo (if CTR <1%)
  [ ] Start inventory replenishment (if >5 units shipped)
  [ ] Price test decision (if >10 reviews received)
```

---

# Decision Gates & Trigger Events (Days 1–28)

## Trigger 1: Supplier Quote Arrives Showing <$11/kg Wholesale
**Probability:** Medium (50%)
**Decision:** Do not switch supplier yet. Log quote; reassess in Month 2 when volume >25 kg/month.
**Action:** Reply to supplier: "Thank you for the quote. I'm currently at 20 kg/month and will revisit bulk pricing when I hit 25+ kg/month volume (projected Month 3). I'll reach out then."

## Trigger 2: Bumper Pads Delayed >7 Days Beyond Day 14
**Probability:** Low (20%)
**Decision:** Ship units without pads; include note "Bumper pads will be included in tracking #2 shipment by [DATE]."
**Action:** Have replacement pads pressed and shipped to first customers by Day 21 max. Offer full refund to any customer who requests it (unlikely).

## Trigger 3: Headphone Hooks Gets <50 Views by Day 27
**Probability:** Low (15%) — Etsy Ads should drive minimum 50 views
**Decision:** Increase Etsy Ads to $2/day for next 2 weeks.
**Action:** Double Etsy Ads budget on Day 27.

## Trigger 4: First Order Arrives with Fit Issue (Jaw Too Tight/Loose)
**Probability:** Medium (40%)
**Decision:** Offer replacement with different tolerance; offer refund if preferred.
**Action:** Follow customer service template in `headphone-hooks-execution-checklist.md` Section 6.

## Trigger 5: First Order Ships But Customer Requests Price Refund (Saw Cheaper on Amazon)
**Probability:** Low (5%) — unlikely at $12.99 launch price
**Decision:** Do not refund; point to unique features (cable post, custom color, Etsy reviews/support).
**Action:** Draft response: "Our hook includes a cable-wrap post and custom color options. Standard Amazon hooks don't. The personalization and US-made support are the value. Happy to help if the fit is wrong."

---

# Confidence Notes

**High confidence (90%+):**
- All design files are production-ready (test-print validates)
- Etsy listing templates are complete and tested (from ModRun baseline)
- Cost model is accurate to within 5% (validated against actual ModRun COGS)
- Supplier contacts and email templates are ready to go
- Photography setup is existing (no new capital required)

**Medium confidence (70–89%):**
- Week 1 unit volume projections (5–8 hooks in first 7 days) depend on Etsy algorithm traction and Etsy Ads effectiveness
- Supplier response timeline (quote within 24–48 hours) may slip to 3–5 days for some vendors
- Bumper pad arrival timeline (7–14 days from AliExpress) has historical variance of ±3 days

**Lower confidence (<70%):**
- Social media organic reach (TikTok/Reddit virality is unpredictable)
- First customer review timing and content (depends on shipping speed and buyer behavior)
- Price elasticity test at $14.99 (untested in this market segment; depends on review accumulation)

**Dependency risks:**
- Test print outcome (single point of failure; mitigated by design pre-validation)
- Bumper pad delivery (manageable contingency: ship without pads, follow up)
- Etsy algorithm placement (managed by Etsy Ads spend; not controllable but predictable)

---

# Key Documents Referenced

- `headphone-hooks-execution-checklist.md` — Detailed Day 1–28 tasks and photo brief
- `headphone-hooks-etsy-listing.md` — Complete listing copy, tags, pricing strategy
- `headphone-hooks-cost-model.md` — Bill of materials, labor, revenue projections
- `revenue-ramp-metrics.md` — Weekly tracking template, margin monitoring, scaling triggers
- `cost-model-spreadsheet.csv` — ModRun baseline COGS and sensitivity analysis
- `modrun_rail.py`, `modrun_clip.py`, `headphone_hooks.py` — CadQuery design files

---

# Success Metrics: Month 1 Completion

**Revenue targets:**
- Week 1: $125–$200 (ModRun + hooks)
- Week 2: $200–$300
- Week 3: $300–$450
- Week 4: $450–$575
- **Month 1 cumulative: $1,075–$1,525 gross** (target: $600–$800 for hooks alone)

**Operational targets:**
- All orders shipped within 1–3 business day processing time
- Zero customer complaints on fit or quality
- Etsy ratings: 4.5+ average on first 5 reviews
- ModRun + Hooks cross-sell visible in 100% of outgoing orders

**Scaling readiness by Month 2:**
- Headphone hooks at 5–10 units/week sustained demand
- ModRun at 10–15 units/week
- Supplier pricing locked in or negotiation in progress
- Monthly burn-in test on second product (Product 3: magnetic bin labels) design complete

---

**Document status:** EXECUTION-READY  
**Last updated:** 2026-05-06  
**Trigger:** Test print completion ✓ or pending?

*When test print passes, this plan launches immediately. All materials are prepared; no dependencies remain.*

