---
title: Post-Test-Print Launch Contingency Branches
date: 2026-05-21
version: 1.0
status: decision-ready
purpose: Route test print outcome to specific launch timeline; eliminate May 24-25 ambiguity
related: ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md, post-test-print-launch-prep.md, cost-model-spreadsheet.csv
---

# Post-Test-Print Launch Contingency Branches

**Created**: 2026-05-21 (Session 1447)  
**Status**: Ready to execute on May 24 morning based on test print results  
**Purpose**: Specify exact go/no-go decisions and timeline adjustments for each test outcome scenario. Eliminates discovery delays and enables immediate launch execution upon test completion (May 22-23).

**Use this document**: Review before May 22 test print. On May 24 morning, check test outcome against decision tree (Section 1), then execute the corresponding branch timeline (Sections 2-5).

---

## Section 1: Decision Tree & Branch Points

### Test Outcome Evaluation Criteria

Evaluate test print against these criteria on **May 23-24 morning** (2-3 hours after print completes):

| Criterion | PASS Threshold | PASS-WITH-ADJUSTMENTS Threshold | FAIL Threshold |
|-----------|-----------------|-------------------------------|----------------|
| **Snap-arm clearance (FDM tolerance)** | ±0.5mm from CAD, clips on/off smoothly in 3+ cycles without binding | 0.1-0.5mm deviation from CAD; engagement requires force but functional after 5 cycles | >0.5mm deviation OR clip falls off rail OR requires pliers to remove |
| **Surface finish** | No delamination, <1mm warping, consistent color | Light layer lines acceptable, <1.5mm warping, minor color variation | Visible layer separation, >2mm warping, stringiness on snap arm |
| **Dimensional tolerances** | Rail channel and clip width ±0.5mm from CAD spec | Rail/clip off by 0.1-0.5mm; workable with next-batch adjustment | Off by >0.5mm; requires redesign |
| **Functional cycles** | Snap on/off cleanly 5+ times without cracking | Snaps on/off but shows minor stress marks after 5 cycles | Snap arm cracks on 2nd or 3rd cycle |
| **Cable fit** | 3-10mm cables seat snugly without binding | Cables fit with minor gap or minor binding | Cables too loose or too tight; non-functional |

---

### Branch Routing Decision Tree

**Use the flowchart below to route to correct branch (Sections 2-5):**

```
                        TEST PRINT COMPLETE (May 23-24)
                                 |
                                 v
                    Does snap arm pass functional test?
                    (Snaps on/off cleanly 5+ cycles, no cracking)
                           YES / NO / PARTIAL
                          /    |      \
                         /     |       \
                        v      v        v
                      YES    PARTIAL    NO
                       |        |        |
                       v        v        v
         All dimensions   Some sizes   MAJOR ISSUE
         within ±0.5mm?   work, some   (cracks, won't engage)
            |      |      don't work   |
           YES    NO            |      v
            |      |            v    [FAIL BRANCH]
            |      |     [PARTIAL-FAIL BRANCH]  Redesign needed
            |      |                            Launch delayed
            |      v                            June 6-13 target
            |   [PASS-WITH-                     (Section 5)
            |    ADJUSTMENTS BRANCH]
            |   May 26 re-print
            |   May 27-June 1 shop setup
            |   June 1 launch OR fallback
            |   (Section 4)
            |
            v
         [PASS BRANCH]
         May 25-29 shop setup
         May 30 launch
         (Section 2)
```

---

## Section 2: PASS Branch (Full Speed Launch)

**Condition**: Snap arm tolerance ±0.5mm, all dimensions correct, cable fit acceptable, no cracking on 5+ cycles.

**Decision**: ✅ **GO** — Proceed directly to ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md Part 1, launch May 30.

**Launch window**: May 30 (Thursday) — June 2 (Sunday)

### Timeline Overview (May 24-June 3)

```
MAY 2026
Date    Day     Activity                              Status
----    ---     --------                              ------
May 24  Fri     Test print evaluation ✓ PASS         ~2-3h eval time
                Approve design for production
                
May 25  Sat     [START] Shop setup begins
                Etsy shop creation
                Policies + shipping profile config
                Payment method activation
                
May 26  Sun     Listing photography prep
                Shop banner/icon design
                
May 27  Mon     Product listing drafting (5 SKUs)
                Description writing, tag research
                
May 28  Tue     Listings to draft status
                Final SEO review, pricing verify
                
May 29  Wed     Final review + approval
                Inventory status check
                
May 30  Thu     🚀 LAUNCH DAY (Morning)
                Publish all 5 listings simultaneously
                Monitor first 2 hours
                
May 31  Fri     Day 2 operations
                Ship all Thu-Fri orders by 3 PM
                
Jun 01  Sat     Day 3 operations
                Continue print + ship
                
Jun 02  Sun     Day 4 review + metrics
                Analytics review
                Customer feedback check

JUNE 2026
Jun 03  Mon     Week 2 begins
                Continue daily operations
```

### Phase-by-Phase Execution (May 25-29)

#### **Phase A: Etsy Shop Foundation (May 25-26, Saturday-Sunday)**

**Goal**: Shop account live and configured with all policies, ready for product listing upload.

**Time estimate**: 2-3 hours total (split across 2 days)

**May 25 (Saturday) — 1.5 hours**:
- [ ] Create Etsy shop: Register at etsy.com/sell
  - Shop name: "ModRun Design" (lock this immediately)
  - Location: Your state
  - Primary location: Home
  - Confirm email verification
- [ ] Activate Etsy Payments:
  - Link business bank account (from post-test-print-launch-prep.md Phase 2)
  - Submit W-9 / tax ID (EIN preferred)
  - Confirm card on file for label purchase credits
- [ ] Create shipping profile (per ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md Phase 1a):
  - "Standard Domestic USPS Ground Advantage"
  - Processing time: 2 business days
  - Estimated weight: 0.27 lbs (includes clip + mailer)
  - Use Pirate Ship rates (currently $3.85-4.60 under 1 lb, Zone 4 avg)

**May 26 (Sunday) — 1.5 hours**:
- [ ] Shop policies:
  - Return Policy: 30-day returns, seller-paid return label
  - About Shop: "ModRun specializes in precision 3D-printed cable management. Original parametric designs, made-to-order, tested for quality."
  - Privacy policy: Use Etsy template
  - Terms of Service: Use Etsy template with IP clause
- [ ] Shop visual assets:
  - Banner (3360x840): Use Canva, place product photo with "Original Design. Precision Manufactured." text
  - Icon (500x500): Clean product photo or geometric logo
  - Announcement: "New ModRun cable management products launching May 30. Pre-orders ship within 2 business days."

**May 25-26 Verification**:
- [ ] Test Etsy login from phone app
- [ ] Confirm bank account micro-deposits pending (2-3 business day wait, should clear by May 27-28)
- [ ] Verify shipping profile calculates rates correctly (add sample product, test checkout)

---

#### **Phase B: Product Listing Creation (May 27-29, Monday-Wednesday)**

**Goal**: All 5 product listings in draft status, SEO verified, ready for simultaneous publish.

**Time estimate**: 4-5 hours total

**May 27 (Monday) — 2 hours**:
- [ ] Photography setup (if not already done):
  - White foamcore background + ring light (or natural window light)
  - Hero shot: Cable clip on neutral background, detail shot of snap arm
  - Lifestyle shot: Clip installed on cables, desk context
  - Color variants side-by-side (if printing multiple colors)
  - Size comparison (coin or ruler in frame)
  - Target: 1000x1000px minimum per image, 5-7 images per listing
  
**May 28 (Tuesday) — 2 hours**:
- [ ] Write product descriptions for 5 SKUs (use templates from ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md Phase 1b):
  - Basic Clip (PLA) — $4.99 single / $12.99 3-pack
  - Rail System (single) — $7.99 single / $19.99 3-pack
  - Premium Clips (PETG) — $8.99 single / $22.99 3-pack
  - Modular Rail Kit — $14.99
  - Starter Bundle (3 clips + 1 rail) — $22.99
  
  **Description checklist per listing**:
  - Title (80 char max): E.g., "Snap-Fit Cable Clip PLA — 3D Printed Cable Management"
  - SEO tags (13 tags): cable clips, cable management, desk organizer, 3D printed, cable organizer, home office, organization, workspace, desk accessories, PLA, modular, snap fit, precision
  - Price: Verify against cost-model-spreadsheet.csv (target margin ≥54%)
  - Shipping profile: "Standard Domestic USPS Ground Advantage"
  - Quantity: Conservative launch stock (based on inventory available)
    - Basic Clip: 15 units
    - Rail System: 8 units
    - Premium Clips: 5 units
    - Kits: 3 units each
  - Variants: Material (PLA / PETG) and Color (Black / White / Grey) where applicable

**May 29 (Wednesday) — 1 hour**:
- [ ] Final listing review (draft status, not yet published):
  - Proofread all titles, descriptions for typos
  - Verify margins on pricing (use calculator: [Price - COGS] ÷ Price = margin %)
    - Basic Clip: $4.99 - $1.50 COGS = 70% margin ✓
    - Rail System: $7.99 - $2.50 COGS = 69% margin ✓
    - Starter Bundle: $22.99 - $7.00 COGS = 70% margin ✓
  - Verify shipping calculates correctly (test checkout with sample address)
  - Use eRank (free tier) to validate tags for search volume (target 10,000+ monthly searches per tag)
  - All photos uploaded and cropped to 1000x1000px minimum
  
- [ ] Inventory pre-staging:
  - Confirm all pre-printed stock is QC'd and sorted by SKU
  - Count finished units: Basic Clip (black/white/grey), Rail Systems, Premium Clips, Kits
  - Move to fulfillment shelf with bin labels
  - Test order: Create a test Etsy purchase flow (add to cart, calculate shipping, confirm pickup address) — do NOT complete payment, just verify UX
  
- [ ] Backup verification:
  - Confirm bank account micro-deposits cleared (if not, payment may not process; have backup card ready)
  - Print backup of all listing descriptions + photos (in case Etsy connection fails on launch day)

---

#### **Phase C: Pre-Launch Inventory & Supplier Coordination (May 24-29, Parallel)**

**Goal**: Confirm 40-50 pre-printed units available for May 30 launch; verify supplier availability for Month 2 scaling.

**May 24-25**: Inventory count
- [ ] Physical inventory: Count all finished clips, rails, kits. Total minimum: 40 units.
- [ ] Any units below threshold, print to fill (print time: 2-4h per unit, batch printing 6-8 units per plate).
- [ ] QC all units against fulfillment-workflow.md Section 2 checklist (dimensional tolerance, surface finish, functional test).

**May 25-26**: Supplier confirmation
- [ ] Verify eSUN Amazon availability (ASIN B0G2KSS613): Check stock, confirm 2-5 day Prime delivery.
- [ ] Confirm Anycubic 50kg pallet availability (store.anycubic.com): Bookmark, ready to order if May 30-June 2 demand hits 20+ units/day.
- [ ] Email Pirate Ship support: Confirm account is active and USPS commercial rates are locked in (should be instant).

---

### Launch Day Execution (May 30, Thursday)

**Publish time**: 10:00 AM — 2:00 PM ET (optimal per Etsy algorithm data)

**Hour 0 (9:00-10:00 AM)**:
- [ ] Final system check:
  - Test Etsy login + shop visibility
  - Confirm email notifications are enabled
  - Open Etsy app on phone for real-time order alerts
  - Test Pirate Ship integration (Settings → Store Integrations → Etsy → Authorize if not done)
  
**Hour 1 (10:00-11:00 AM) — PUBLISH**:
- [ ] Publish all 5 listings simultaneously:
  - Go to each draft listing, review once more, click "Publish"
  - Refresh Etsy search: "ModRun" or "cable clip" — all products should appear within 15 minutes
  - Screenshot shop page for record-keeping
  - Post launch announcement to social media (if accounts exist):
    - Instagram: "🎉 Just launched on Etsy: ModRun cable clips. Original design, precision 3D-printed, ready to ship today! Link in bio."
    - Twitter/X: "Live on Etsy: ModRun cable management clips. Snap-fit design, tested for durability, all in-stock items ship same day. etsy.com/shop/modrundesign"
  - Send launch email (if you have a personal contact list): "Excited to announce ModRun is now on Etsy! First 10 buyers get a free bonus clip. Check it out: [link]"

**Hour 2-6 (11:00 AM — 4:00 PM)**:
- [ ] Monitor orders:
  - Check Etsy app every 15-30 minutes for incoming orders
  - Respond to any shop messages within 30 minutes (target <1 hour)
  - Note: It may take 12-24 hours for first order; algorithm is indexing new listings
  
**Hour 6-8 (4:00-6:00 PM)**:
- [ ] Print orders received by 2 PM cutoff:
  - For each order: verify address, match to SKU, print from pre-printed stock or queue print job
  - QC each unit (dimensional spot-check, visual inspection)
  - Package with care: product in poly mailer + thank-you card + ModRun sticker (if available)
  - Prep shipping labels
  
**Hour 8+ (6:00+ PM)**:
- [ ] Ship by 6 PM cutoff:
  - Use Pirate Ship: Import orders → Select USPS Ground Advantage → Purchase labels → Print
  - Drop at USPS counter or schedule USPS pickup
  - Update Etsy order status to "Shipped" (triggers auto-notification to customer with tracking)
  - End-of-day summary: "X orders shipped, X units delivered to customer mailbox in 2-3 days"

---

### Days 2-4 Operations (May 31 — June 2)

**Repeat daily cycle**:

| Time | Action | Notes |
|------|--------|-------|
| **8:00 AM** | Check Etsy messages | Respond within 1 hour |
| **8:30 AM** | Print queue for day | Print all orders from previous day + overnight |
| **12:00 PM** | QC + packaging | Inspect, package, prep labels |
| **2:00 PM** | Ship cutoff | All orders shipped by this time |
| **4:00 PM** | Update Etsy | Mark as shipped, include tracking |
| **6:00 PM** | End-of-day snapshot | Count units shipped, note any issues |

**Conversion monitoring**:
- Track shop visits vs. orders (goal: 2-5% conversion rate)
- If conversion <2% by May 31 afternoon:
  - Reduce price by $1 on slowest product (test on May 31-June 1)
  - Check photo order (swap best-performing photo to position 1)
  - Reorder title keywords (put primary keyword first)

**Customer feedback** (if any reviews post):
- Respond positively to all reviews
- Note any quality issues or requests
- Screenshot positive reviews (use for testimonials)

---

### End-of-Launch Metrics (June 2-3)

**Sunday (June 2) evening — analytics review**:

| Metric | Target | Calculation | Action if Below |
|--------|--------|-------------|-----------------|
| **Total orders (Thu-Sun)** | 5-15 units | Count from Etsy | <3 orders? See conversion troubleshooting below |
| **Conversion rate** | 2-5% | Orders / Shop Visits | <2%? Reduce price $1 temporarily |
| **Avg order value** | $20-30 | Total revenue / Orders | Low AOV? Bundle pricing ineffective; adjust |
| **Customer satisfaction** | 0 complaints | No messages about quality | Any complaints? Note for May 31 batch adjustments |
| **Repeat customers** | N/A at launch | (OK to be zero at launch) | — |

**Conversion troubleshooting checklist**:
- [ ] Are listings appearing in Etsy search for "cable clip"? (Use incognito browser to check)
- [ ] Do product photos show detail clearly? (Compare against top 3 competitors on Etsy search)
- [ ] Is pricing competitive? (Search "3D printed cable clip" on Etsy; note competitor prices)
- [ ] Are tags validated for search volume? (Use eRank to confirm 10,000+ searches)
- [ ] Any technical issues with cart/checkout? (Test purchase flow as customer)

---

### Gantt Timeline — PASS Branch (May 24-June 3)

```
PASS BRANCH TIMELINE
═════════════════════════════════════════════════════════════

May 24 (Fri)      [2-3h eval]
                  Test print evaluation → PASS ✓
                  Design approved

May 25 (Sat)      [Shop Foundation — 1.5h]
                  ├─ Etsy shop creation
                  ├─ Payments + W-9 setup
                  └─ Shipping profile config
                        (continues into May 26)

May 26 (Sun)      [Photography + Policies — 1.5h]
                  ├─ Banner/icon design
                  └─ Policy pages setup
                  [Inventory prep begins]
                  ├─ QC pre-printed stock
                  └─ Batch print to 40+ units

May 27 (Mon)      [Listing Creation — 2h]
                  ├─ Photography setup
                  ├─ Write descriptions (5 SKUs)
                  └─ Tag research

May 28 (Tue)      [Listing Config — 2h]
                  ├─ Upload photos
                  ├─ Configure variants
                  ├─ Set quantities
                  └─ Listings to draft status

May 29 (Wed)      [Final Review — 1h]
                  ├─ Proofread all listings
                  ├─ Verify pricing margins
                  ├─ Test checkout flow
                  └─ Approve all 5 listings

May 30 (Thu)      [🚀 LAUNCH DAY]
                  ├─ 10:00 AM: Publish all 5 listings
                  ├─ 11:00 AM-4:00 PM: Monitor for orders
                  └─ 6:00 PM: Ship all day's orders
                  [Day 1 metrics: X orders, Y conversion]

May 31 (Fri)      [Day 2 Operations]
                  ├─ 8:00 AM: Print + ship
                  └─ Evening: Monitor conversion
                  [Day 2 metrics: X orders]

Jun 01 (Sat)      [Day 3 Operations]
                  ├─ Print + ship cycle
                  └─ Monitor for issues
                  [Day 3 metrics: X orders]

Jun 02 (Sun)      [Day 4 Review]
                  ├─ Analytics review
                  ├─ Customer feedback check
                  └─ Conversion analysis
                  [4-day total: 5-15 orders ✓]

Jun 03 (Mon)      [Week 2 Begins]
                  ├─ Continue daily operations
                  ├─ Monitor conversion rate
                  └─ Prepare for supplier scaling
```

---

## Section 3: PASS-WITH-ADJUSTMENTS Branch (Rapid Redesign)

**Condition**: Snap arm 0.1-0.5mm off from CAD; functional but requires minor tolerance adjustment. OR: Warping 1-1.5mm; requires print setting adjustment.

**Decision**: ⚠️ **CONDITIONAL GO** — Iterate once, re-print May 26, re-test May 26 afternoon. If pass, launch May 27-29. If fail, fall back to FAIL branch.

**Launch window**: May 27-June 1 (1-3 day delay vs. PASS branch)

### Rapid Iteration Sequence (May 24-26)

#### **May 24-25 (Friday-Saturday) — Design Adjustment (2-3 hours)**

**Rapid turnaround**:
- [ ] Document exact deviation: Measure snap arm clearance with calipers, note specific dimension
  - Example: "Snap arm 0.3mm too tight — requires 0.15mm increase in channel width"
  - Example: "Clip warped 1.2mm at corner — likely bed temperature or cooling rate issue"
  
- [ ] CAD adjustment (30-45 minutes):
  - Open CadQuery file: projects/mfg-farm/cadquery/modrun_clip_b123d.py
  - Adjust tolerance parameter: If too tight, increase channel width +0.2mm. If too loose, decrease -0.2mm.
  - If warping: Leave CAD unchanged; adjust print settings instead (see below)
  - Save revised CAD, export STL
  
- [ ] Print setting adjustment (if warping observed):
  - Nozzle temp: Reduce by 5°C (210°C → 205°C) to reduce thermal stress, OR increase by 5°C if under-extrusion
  - Bed temp: May 26 print at 55°C (vs. 60°C) to reduce thermal shock during cooling
  - Cooling: Enable part cooling fan at 50% from layer 5 (vs. default) to reduce warping
  - Layer height: Keep at 0.2mm (validated)

- [ ] Generate new test print settings in Bambu Studio:
  - Slice revised STL with adjusted settings
  - Export to SD card or MicroSD for printer
  - Check print time: Should be similar (±5 min) to original test print

**May 26 (Sunday) — Re-Print & Re-Test (3-4 hours)**

- [ ] Queue re-print job on Bambu P1S:
  - Load filament (should be same spool as original test, for consistency)
  - Level build plate (standard pre-print routine)
  - Start print job (estimated time: 25-45 min depending on object size)
  - Monitor first 3 layers for adhesion, then passive monitoring
  
- [ ] During print (30-45 min wait):
  - Review shop setup checklist (Phase B above) — write product descriptions in parallel
  - Take product photography if not already done
  
- [ ] Re-test (15-20 minutes after print cools):
  - Measure snap arm clearance with calipers: ✓ within ±0.5mm?
  - Test functional cycles: ✓ snaps on/off cleanly 5+ times?
  - Check warping: ✓ <1mm deviation?
  - Cable fit: ✓ 3-10mm cables seat without binding?
  
  **If ✓ all pass**: Proceed to Adjusted Timeline below  
  **If ✗ any fail**: Escalate to FAIL branch (Section 5) — one iteration is the limit for May launch window

---

### Adjusted Timeline (May 26-June 1)

**If May 26 re-test passes, execute this timeline:**

```
PASS-WITH-ADJUSTMENTS TIMELINE
═════════════════════════════════════════════════════════════

May 24 (Fri)      [2-3h eval]
                  Test print: Initial design issue detected
                  Iterate required

May 25 (Sat)      [Design adjustment — 2-3h]
                  ├─ CAD parameter update
                  ├─ Print settings revision
                  └─ File export to SD card

May 26 (Sun)      [Re-print + Re-test — 3-4h]
                  ├─ Re-print job (25-45 min)
                  ├─ Parallel: Write listings, photography
                  ├─ Re-test (15-20 min)
                  └─ ✓ PASS → Proceed
                      ✗ FAIL → Escalate to FAIL branch

May 27 (Mon)      [Shop Foundation — 2h]
                  ├─ Etsy shop creation
                  ├─ Payments + policies
                  ├─ Shipping profile
                  └─ Visual assets

May 28 (Tue)      [Listings to Draft — 2-3h]
                  ├─ Finalize photos
                  ├─ Upload descriptions
                  ├─ Configure variants/quantities
                  └─ Listings in draft (ready to publish)

May 29 (Wed)      [Final Review — 1h]
                  ├─ Proofread + margin check
                  ├─ Test checkout
                  └─ Approve all 5 listings

May 30 (Thu)      [Inventory prep day]
                  ├─ Pre-print additional stock (if capacity)
                  ├─ QC all stock
                  └─ Sort by SKU (staging for launch)

May 31 (Fri)      [🚀 LAUNCH DAY (1 day later)]
                  ├─ 10:00 AM: Publish all 5 listings
                  ├─ 11:00 AM-4:00 PM: Monitor for orders
                  └─ 6:00 PM: Ship day's orders
                  [Day 1 metrics: X orders]

Jun 01 (Sat)      [Day 2 Operations]
                  ├─ Print + ship cycle
                  └─ Monitor conversion
                  [Day 2 metrics: X orders]

Jun 02 (Sun)      [Day 3 + Review]
                  ├─ Operations continue
                  ├─ Analytics review
                  └─ Conversion analysis

Jun 03 (Mon)      [Week 2 Begins]
                  ├─ Continue daily operations
                  └─ Prepare for scaling
```

---

### Fallback Plan: If May 26 Re-Print Still Has Issues

**Scenario**: Re-print on May 26 still shows tolerance deviation OR warping >1mm after setting adjustment.

**Decision**: Do NOT attempt third iteration. Instead:

1. **Pivot to FAIL branch** (Section 5):
   - Keep existing test print (functional even if imperfect) as reference unit
   - Launch with **magnetic bin labels** instead of clips (see Section 5 for timeline)
   - Schedule ModRun clip v2 for June 15 launch as secondary product
   
2. **Timeline consequence**:
   - Etsy shop still launches May 31 (no further delay)
   - Inventory is labels (2-hour design), not clips (5 hours CAD + test)
   - AliExpress magnet lead time: 5-7 days (order May 26, arrive June 1 for June 2 launch)
   - Margin: Labels cheaper than clips, still 65%+ gross margin
   
3. **Capital impact**: Magnetic label orders ~$0.80 COGS vs. $1.50 for clips; lower per-unit cost allows aggressive pricing ($2.99 bundle for 10 labels) to gain initial reviews

---

## Section 4: FAIL Branch (Redesign + Pivot)

**Condition**: Snap arm cracks on 2nd-3rd cycle, OR won't engage clip on rail, OR dimensional deviation >0.5mm, OR warping >2mm.

**Decision**: ❌ **NO-GO** — Halt clip launch. Pivot to magnetic bin label product instead. Clip v2 redesign for June 15 launch.

**Launch window**: May 30-June 2 with labels; clip v2 launch target June 15

### Immediate Actions (May 24-25)

**May 24-25 (Friday-Saturday) — Pivot Decision & Design Start (2-3 hours)**

- [ ] **Confirm failure mode**:
  - Photograph the crack (macro photo of snap arm)
  - Measure deviation: How much tighter/looser than CAD spec?
  - Note: Can this be fixed with tolerance adjustment (PASS-WITH-ADJUSTMENTS) or is it structural (FAIL)?
  
  **If structural** (snap arm material thickness insufficient, geometry weak point):
  - Option A: Redesign snap arm geometry (add radius, increase thickness) — 4-5 hour design + 2 test cycles = too late for May 30
  - Option B: Pivot product instead
  
  **DECISION**: Proceed with pivot (Option B)

- [ ] **Magnetic bin label design** (quick path to revenue):
  - Existing design: projects/mfg-farm/cadquery/sku_batch_2_magnetic_labels.py
  - Use existing CAD or fast-design new variant
  - Labels: 1.5" x 2.5" with adhesive back + magnetic strip
  - Print time: NONE (no 3D printing required)
  - Sourcing: AliExpress custom magnets, Sticker Mule labels
  
  **Design timeline**:
  - May 25: Finalize label design (text, colors, SKU variants)
  - May 26: Order pre-printed label stock (AliExpress or Etsy print-on-demand)
  - May 27-28: Assemble labels + magnets
  - May 29-31: Test magnetic strength, validate look-and-feel
  - June 1-2: Inventory ready for shipping

---

### Magnetic Label Launch Path (May 26-June 2)

**Parallel to label sourcing: Pivot shop to label-primary product**

#### **May 26-27 — Sourcing & Supplier Outreach**

**Order magnets** (AliExpress, 5-7 day lead time):
- [ ] Search AliExpress: "adhesive magnetic strips" or "self-adhesive magnets"
- [ ] Order: ~500 units of 1.5"x0.5" magnetic strips (~$15-25 for 500 units)
- [ ] Estimated arrival: June 1-2 (in time for June 2 launch)
- [ ] Backup: If lead time slips, Etsy shop still launches June 2 without physical magnets; fulfill with digital download of label designs + Amazon magnet fulfillment

**Print labels** (two options):
- Option A: Sticker Mule (Fast, professional, eco-friendly)
  - 500 custom labels: $80-120
  - Lead time: 3-5 days (arrives May 29-31)
  - Quality: Premium finish
  
- Option B: Etsy print-on-demand (NO inventory risk)
  - Partner with existing Etsy print-on-demand label vendors
  - Dropship directly: Labels printed, not you
  - Margin: Lower (40-50%) but zero inventory risk
  - Suitable if FAIL branch is extended redesign; use POD as holding pattern

**DECISION**: Use Sticker Mule (Option A) for brand control + better margin (65%+ gross)

#### **May 28-29 — Shop Configuration (2 hours)**

- [ ] Reuse Etsy shop from Phase B (already created):
  - Update shop announcement: "Introducing ModRun Magnetic Bin Labels — organize your space with style. Coming June 2."
  - Shop section: "Labels & Organization"
  - Update banner with label product photo
  
- [ ] Create 3 label product listings (May 28):
  - **Label Set #1 — Kitchen Organization** (5 labels + 5 magnets): $4.99
    - Labels: Pantry, Spices, Coffee, Tea, Snacks
    - Material: Weather-resistant vinyl + premium adhesive
    - Magnetic backing for fridge/whiteboard mounting
    - Colors: Black text on white background (or choose 2-3 color options)
    
  - **Label Set #2 — Garage & Tools** (5 labels + 5 magnets): $4.99
    - Labels: Nails, Screws, Bolts, Washers, Hardware
    - Waterproof vinyl + industrial adhesive
    
  - **Label Set #3 — Workspace** (5 labels + 5 magnets): $4.99
    - Labels: Cables, Adapters, Accessories, Chargers, Misc
    - Durable vinyl + strong magnets
  
  - **Variant SKU — Custom Labels** (digital file only): $2.99
    - Customers provide text/design
    - You print on-demand via Sticker Mule or print service
    - Fulfillment: Email PDF within 24h

- [ ] Photos (reuse if possible from sku_batch_2 research):
  - Hero: Labels on fridge/whiteboard with magnets
  - Detail: Close-up of label text + magnetic strip
  - Lifestyle: Organized pantry/desk with labels in place
  - Color variants: Show all 3 sets
  - Minimum 5 images per listing

- [ ] Pricing validation:
  - COGS: Labels ~$0.40 per 5-pack, magnets ~$0.10, packaging ~$0.05 → $0.55 total
  - Price: $4.99 per set → 89% gross margin (vs. 70% for clips)
  - Platform fees: ~$0.75 per order
  - Net margin after fees: ~70% (matches clip margin, despite lower COGS)

#### **May 30 — Inventory Staging (May 29-31)**

**May 29-30**:
- [ ] Labels arrive (if on-time from Sticker Mule)
- [ ] Assemble: Peel + apply magnetic strips to back of each label set
- [ ] QC: Test magnetic strength on metal surfaces (fridge, whiteboard)
- [ ] Package: 5-label set + 5-magnet strips in small kraft mailer
- [ ] Stock: 50-100 sets ready to ship

---

#### **May 31-June 2 — Label Launch & Initial Sales**

- [ ] **Launch Day (May 31, Friday)**:
  - Publish all 3 label listings (10 AM-2 PM)
  - Announce on social media: "🏷️ Just launched: ModRun Magnetic Labels. Organize your home, office, or garage with style. Live on Etsy now! [link]"
  - Monitor for orders; same daily cycle as clip launch (print → QC → ship)
  
- [ ] **June 1-2 — Monitor conversion**:
  - Same metrics as clip launch (conversion rate, AOV, customer feedback)
  - Labels have different Etsy search dynamics (larger addressable market for "labels")
  - Target: 5-10 orders by June 2
  
---

### Clip v2 Redesign Track (Parallel, June 2-15)

**While labels generate revenue, redesign clips in parallel:**

#### **June 2-8 — CAD Redesign (10-15 hours)**

- [ ] **Analysis of May 24 failure**:
  - Review photos/measurements of cracked snap arm
  - Root cause: Is snap arm too thin? Wrong material? Stress concentration at base?
  
- [ ] **Geometry fixes**:
  - Option A: Thicken snap arm from 3mm to 4mm (adds stiffness, may increase engagement force)
  - Option B: Add radius at snap-arm base (eliminates stress concentration point)
  - Option C: Reduce snap-arm length by 10% (easier to engage, still functional)
  - Option D: Hybrid materials (PLA for body, PETG for snap arm for added strength)
  
- [ ] **CAD implementation** (10-15 hours):
  - Modify CadQuery script: projects/mfg-farm/cadquery/modrun_clip_b123d.py
  - Parametric approach: Create variant geometry + test locally
  - Export 3 STL variants (thin/medium/thick snap arm)
  - Commit to git with notes on design rationale

#### **June 9-12 — Test Print Round 2 (2-3 iterations)**

- [ ] **Variant A test print** (June 9):
  - Print updated snap-arm design
  - Stress test: 10 snap cycles (vs. 5 in original test)
  - Measure clearance: Still ±0.5mm? Or shifted?
  - Result: PASS / PASS-WITH-ADJUSTMENTS / FAIL
  
- [ ] **If PASS**: Proceed to June 15 launch (skip variants B & C)
- [ ] **If PASS-WITH-ADJUSTMENTS**: Print variant B (June 10), retest (June 10 afternoon)
- [ ] **If FAIL**: Print variant C (June 11), retest (June 11 afternoon)
  
  Whichever variant passes first becomes ModRun Clips v2 launch design

#### **June 13-15 — v2 Launch Setup**

- [ ] **Create new product listing**:
  - Reuse Etsy shop (already live with labels)
  - New listing: "ModRun Snap Clip v2 — Enhanced Design, Precision 3D Printed"
  - Pricing: $4.99-5.99 (slight premium vs. labels, positioning as premium cable management)
  - Inventory: Print 20+ units June 12-13 in advance
  
- [ ] **Announce v2 launch** (June 15):
  - Etsy shop announcement: "New: ModRun Clips v2 — redesigned snap mechanism. Check out the new design!"
  - Email to customers who bought labels: "Our new cable clip is here! Use code LABELBUYER10 for 10% off your first clip order."

---

### Gantt Timeline — FAIL Branch (May 24-June 15)

```
FAIL BRANCH TIMELINE
═════════════════════════════════════════════════════════════

May 24 (Fri)      [Failure detected]
                  Test print: FAIL (snap arm cracks)
                  Decision: Pivot to labels + redesign clips

May 25 (Sat)      [Pivot planning — 2h]
                  ├─ Analyze failure mode
                  ├─ Scope label design
                  └─ Order magnet sourcing (AliExpress)

May 26 (Sun)      [Label design finalization — 2h]
                  ├─ Design label variants (kitchen, tools, workspace)
                  ├─ Design file for Sticker Mule
                  └─ Order label printing (Est. arrive May 29-31)

May 27 (Mon)      [Shop setup — 2h]
                  ├─ Etsy shop (reuse from Phase B)
                  ├─ Update banner to label focus
                  └─ Policy pages + shipping

May 28 (Tue)      [Label listings — 2h]
                  ├─ Product photography
                  ├─ Write 3 listings (Kitchen/Tools/Workspace)
                  ├─ Configure variants
                  └─ Upload to draft status

May 29 (Wed)      [Final review + Inventory — 1h]
                  ├─ Proofread listings
                  ├─ Test checkout
                  └─ Label stock arrives (if on-time)

May 30 (Thu)      [Assemble + Stage — 2h]
                  ├─ Receive magnets (if on-time)
                  ├─ Apply magnets to labels
                  ├─ QC magnetic strength
                  └─ Stage 50-100 label sets

May 31 (Fri)      [🚀 LAUNCH DAY — Labels]
                  ├─ 10:00 AM: Publish 3 label listings
                  ├─ Monitor for orders
                  └─ 6:00 PM: Ship day's orders
                  [Day 1 metrics: X orders]

Jun 01 (Sat)      [Day 2 + Parallel: Clip redesign starts]
                  ├─ Label: Print + ship cycle
                  └─ Clip: CAD analysis + geometry redesign
                        [10-15h CAD work begins]

Jun 02 (Sun)      [Day 3 + Redesign continues]
                  ├─ Label: Continue ops + analytics
                  └─ Clip: CAD variants in progress

Jun 03 (Mon)      [Clip v1 failure analysis]
                  └─ Root cause documented, design approach chosen

Jun 04-08 (Tue-Sat) [Clip v2 CAD development]
                  └─ Parametric design + 3 variants modeled

Jun 09 (Sun)      [Clip v2 Test Print A]
                  ├─ Print variant A
                  ├─ Stress test 10+ cycles
                  └─ Evaluate: PASS?

Jun 10 (Mon)      [Clip v2 Evaluate + Iterate]
                  ├─ If PASS: Proceed to Jun 15
                  ├─ If ADJUST: Print variant B, test
                  └─ If FAIL: Print variant C, test

Jun 11 (Tue)      [Clip v2 Final test (if needed)]
                  ├─ Variant C test print
                  └─ Confirm passing design

Jun 12-13 (Wed-Thu) [Clip v2 Inventory]
                  ├─ Print 20+ units of passing design
                  ├─ QC all units
                  └─ Stage for launch

Jun 14 (Fri)      [Clip v2 Listing prep]
                  ├─ Create new "ModRun Clips v2" listing
                  ├─ Photography (new variant)
                  └─ Draft status, ready to publish

Jun 15 (Sat)      [🚀 CLIP V2 LAUNCH]
                  ├─ Publish Clips v2 listing
                  ├─ Announce: "New design, same quality"
                  └─ Begin day 1 operations
                  [Parallel: Labels still operating]

[June 15 onward: Two-product shop]
├─ Magnetic Labels (revenue generator, high margin)
└─ ModRun Clips v2 (premium product, growing customer base)
```

---

## Section 5: PARTIAL-FAIL Branch (Launch Functional Sizes Only)

**Condition**: Some clip sizes work (e.g., 0.5" clips snap correctly), others fail (e.g., 0.75" clips too tight). This is rare with parametric CAD, but possible if print settings cause differential warping by size.

**Decision**: ⚠️ **CONDITIONAL GO** — Launch only with passing sizes. Iterate on failing sizes separately. 

**Launch window**: May 30-June 2 with partial product range; full range by June 6-8.

### Partial Launch Strategy (May 25-30)

#### **May 24-25 — Triage Test Results**

- [ ] Document which sizes pass and which fail:
  - Example: "0.5" clips (PLA) ✓ PASS; 0.75" clips (PLA) ✗ FAIL; 1.0" clips (PETG) ✓ PASS"
  - Measure and compare: Do failing sizes have common characteristic (e.g., all larger sizes affected by warping)?
  
- [ ] **Root cause hypothesis**:
  - If only large sizes fail: Likely warping due to longer print time or bed cooling. Solution: Slow print speed, reduce nozzle temp by 5°C.
  - If only PETG fails: PETG material issue (different density, cooling behavior). Solution: Adjust PETG-specific print profile.
  - If random mix: Possibly filament inconsistency within same spool. Solution: Use new spool for re-test.

#### **May 25-26 — Parallel Path**

**Path A: Launch prep with passing sizes**
- [ ] Reduce Etsy inventory quantities to match only passing sizes
  - Example: List 0.5" clips with 20 units stock, but DON'T list 0.75" variant
  - Add note in listing: "Additional sizes coming soon (June 6)"
  
**Path B: Re-test failing sizes**
- [ ] Print failing size variants with adjusted settings (same as PASS-WITH-ADJUSTMENTS branch)
- [ ] Target: Re-test complete by May 29, results available for June 5+ listings

---

#### **May 25-29 — Partial Launch Setup**

Follow PASS branch timeline (Section 2) with modifications:

- [ ] **Etsy shop setup**: Identical to PASS branch (Phase A, May 25-26)

- [ ] **Product listings (May 27-29)**: 
  - List only passing-size variants (e.g., 0.5" clips, 1.0" clips)
  - Leave failing sizes unlisted temporarily
  - In listing description: "Currently available in 0.5" and 1.0" sizes. Additional sizes being validated — check back June 6."
  - Tags: "3D printed cable clip" (avoid size-specific tags like "0.75 inch" for unlisted sizes)

- [ ] **Inventory staging**:
  - Stock all passing-size variants
  - Do NOT stock failing sizes yet

---

#### **May 30-June 2 — Partial Launch Execution**

- [ ] **Publish day (May 30)**: Same as PASS branch, but only publish passing-size variants
- [ ] **Daily operations (May 31-June 2)**: Same as PASS branch
  - Expected sales: Only from passing sizes (will be lower AOV, but still validates product-market fit)
- [ ] **Monitor**: Conversion rate, customer feedback on available sizes

---

#### **May 26-June 5 — Parallel Failing-Size Iteration**

While partial shop operates, redesign failing sizes:

- [ ] **May 26-27**: Re-print failing-size variants with adjusted settings (0.75" clips, e.g.)
- [ ] **May 27-28**: Re-test; evaluate PASS / PASS-WITH-ADJUSTMENTS / FAIL
- [ ] **If PASS by May 28**: Queue these for production May 29; add to Etsy listings May 31 (second listing update)
- [ ] **If PASS-WITH-ADJUSTMENTS**: Do one more iteration May 29; finalize by May 30; list June 1
- [ ] **If FAIL**: Keep out of catalog; note as deferred to v2 redesign

---

#### **June 1-5 — Second Listing Wave**

- [ ] **June 1 or 2**: Once failing sizes re-test PASS:
  - Create new Etsy listing for previously-failed size: "ModRun Cable Clip 0.75" — Now Available!"
  - Reuse photos + description from first listing (just adjust title + sizing details)
  - Set inventory for re-printed stock
  - Post to shop announcement: "Popular demand: 0.75" clips now back in stock!"

- [ ] **June 5-6 — Full-range review**:
  - Check if all size variants are now listed + in stock
  - Update shop announcement: "Full size range now available (0.5", 0.75", 1.0")"

---

### Gantt Timeline — PARTIAL-FAIL Branch (May 24-June 5)

```
PARTIAL-FAIL BRANCH TIMELINE
═════════════════════════════════════════════════════════════

May 24 (Fri)      [Triage]
                  Test print results: Mixed pass/fail by size
                  Decision: Launch passing sizes, iterate failing

May 25 (Sat)      [Dual-track begins]
                  Track A: Shop setup (Phase A)
                  Track B: Re-test failing sizes (settings adjust)

May 26 (Sun)      [Shop Foundation — 1.5h]
                  ├─ Etsy shop creation
                  ├─ Payments + policies
                  └─ Visual assets
                  [Track B: Failing sizes reprinting]

May 27 (Mon)      [Listing creation — passing sizes only — 2h]
                  ├─ Photography (passing sizes featured)
                  ├─ Write descriptions
                  └─ Note: "Additional sizes coming soon"
                  [Track B: Re-test failing sizes]

May 28 (Tue)      [Listings to draft (passing only) — 2h]
                  ├─ Upload photos
                  ├─ Configure passing-size variants only
                  └─ Draft status
                  [Track B: Evaluate re-test results]

May 29 (Wed)      [Final review — 1h]
                  ├─ Proofread listings (passing sizes only)
                  ├─ Approve for launch
                  └─ Inventory: Stock passing sizes only
                  [Track B: If failing sizes pass, queue for printing]

May 30 (Thu)      [🚀 LAUNCH DAY — Partial Range]
                  ├─ 10:00 AM: Publish passing-size listings
                  ├─ Monitor for orders
                  └─ 6:00 PM: Ship day's orders
                  [Partial range live; failing sizes still iterating]

May 31 (Fri)      [Day 2]
                  ├─ Print + ship (passing sizes only)
                  ├─ Monitor conversion
                  └─ [Track B: Print more failing-size units if passed]

Jun 01 (Sat)      [Day 3]
                  ├─ Passing-size operations
                  └─ [Track B: Re-printed failing sizes ready for staging]

Jun 02 (Sun)      [Day 4 + Review]
                  ├─ Passing-size analytics
                  ├─ Customer feedback (all positive on available sizes)
                  └─ [Track B: Prepare new listing for failing-size comeback]

Jun 03 (Mon)      [Week 2 — Prep for 2nd wave]
                  └─ Draft new listing for failing-size variant

Jun 04-05 (Tue-Wed) [Failing-size listing publication]
                  ├─ Publish new listing: "Sizes Now Available: [0.75" / 1.0"]"
                  └─ Inventory linked to re-printed stock

Jun 06 (Thu)      [Full-range review]
                  ├─ All size variants now live
                  ├─ Update shop announcement: "Complete range available"
                  └─ Continue daily operations

[June 6 onward: Full-feature shop with all sizes available]
```

---

## Section 6: Contingency Risk Factors & Mitigation

### Risk 1: Test Print Takes Longer Than Expected

**Scenario**: Test print scheduled for May 22-23 but doesn't complete until May 24 or 25.

**Mitigation**:
- **Decision deadline**: No later than May 25 afternoon (Saturday). If test still printing on May 25, defer to June 2-3 launch window instead.
- **Accelerated shop setup**: If test completes May 24 evening, you have May 25-29 to complete setup (5 days vs. 4). All timelines still achievable.
- **Inventory prep**: Begin pre-printing inventory on May 24 regardless of test result (batch-print clips in background while test runs). If test passes, you're ahead. If test fails, pre-printed inventory becomes scrap or repurposing stock.

---

### Risk 2: Supplier Lead Times Slip (Magnets/Labels in FAIL Branch)

**Scenario**: FAIL branch triggered on May 24. Label printing ordered May 26, but Sticker Mule or AliExpress arrives May 31+ instead of May 29-30.

**Mitigation**:
- **Plan A (Sticker Mule backup)**: Order 2x locations:
  - Sticker Mule (May 26, expect May 29-31)
  - Secondary: Local print shop or Vistaprint express (May 26, expect May 28)
  - Use whichever arrives first
  
- **Plan B (Dropship approach)**: If both delays, pivot to Etsy print-on-demand label vendor:
  - No inventory held
  - Dropship fulfillment (third-party prints and ships)
  - Margin: 40-50% (lower) but zero inventory risk
  - Announcement: "Custom labels available on-demand — ship within 3 business days"
  - Use May 31-June 2 to test dropship approach; convert to in-house if sales validate demand
  
- **Plan C (Email-only launch)**: 
  - If physical magnets unavailable, launch label designs as **digital downloads** only
  - Price: $2.99 for 5-label design PDF (customers print locally)
  - Fulfillment: Email PDF within 24h
  - Positioning: "Professional label templates, print at home or your local print shop"
  - Bridge until physical inventory arrives

---

### Risk 3: Re-Print Still Fails (PASS-WITH-ADJUSTMENTS Branch)

**Scenario**: May 26 re-print with adjusted CAD/settings still shows tolerance deviation >0.5mm or warping >1.5mm.

**Mitigation**:
- **One-iteration rule**: Do NOT attempt third test print. Instead, escalate to FAIL branch immediately:
  - Time lost: Too late for May 30 launch with clips
  - Better ROI: Pivot to labels (2-hour design) vs. spending 5+ more hours on clip redesign
  - Decision: "Not today, but soon" — commit to clips v2 for June 15 (documented in FAIL timeline, Section 4)
  
- **Preserve momentum**: Etsy shop still launches May 31 (no further delay) with labels as holding product. Clips v2 joins in June as premium offering.

---

### Risk 4: Etsy Micro-Deposits Delay (May 25-28)

**Scenario**: Bank verification for Etsy Payments takes longer than expected; account not verified by May 29, blocking payment processing on launch day.

**Mitigation**:
- **Preemptive action** (May 24): 
  - Initiate bank verification immediately after test print decision
  - Provide Etsy with both bank account and backup card (PayPal or debit card)
  - If micro-deposits arrive by May 27-28: Use bank account (commercial rates, lower fees)
  - If micro-deposits delay past May 29: Fall back to backup card (manual processing, slightly higher fee but functional)

- **Backup plan**:
  - Etsy allows PayPal as legacy payment method
  - Link personal PayPal account to Etsy shop before May 29
  - If bank verification incomplete, payments process via PayPal until bank account clears

---

### Risk 5: Printer Failure / Filament Issue

**Scenario**: Bambu P1S has hardware failure on May 25-26, or filament spool develops quality issues during print.

**Mitigation**:
- **Printer failure**:
  - If failure detected before May 26 re-print (PASS-WITH-ADJUSTMENTS branch): Escalate to FAIL branch, shift to label product. No printer needed for labels.
  - If failure after May 30 launch: Inventory you pre-printed before launch covers orders for 3-5 days. Meanwhile, get printer repaired or source replacement. Bambu support: 2-3 day turnaround for warranty claims.
  
- **Filament quality**:
  - Use same spool for test print AND production batch (if test passes) — consistency matters
  - If spool develops issues mid-production (layer delamination, diameter inconsistency), switch to backup spool and adjust feed rate by ±2%
  - Keep 2-3 backup spools of black PLA on hand by May 25

---

### Risk 6: Demand Exceeds Inventory in First 48 Hours

**Scenario**: May 30-31 orders spike beyond pre-printed stock (>15 orders by May 31 afternoon).

**Mitigation**:
- **Pause listings** (temporary):
  - If you run out of stock, Etsy allows listing to go inactive
  - Pause product listing 2-3 hours while you print replacement batch
  - Note in shop announcement: "Current demand exceeds our printed inventory. We're producing more now; orders placed today will ship May 31."
  - Resume listing once new batch printed + in QC
  
- **Queue management**:
  - Implement "Lead Time: 3-5 business days" on listings by June 1 if demand >10 orders/day
  - This sets customer expectations and buys you buffer time for printing
  
- **Scale path** (June 3+):
  - Activate 2nd printer (purchase Bambu P1S second unit, ~$700)
  - Order bulk filament (50kg pallet from Anycubic, $524, arrives June 7-10)
  - Hired contractor for post-processing if volume >100 units/week

---

### Risk 7: Conversion Rate Below 2% (All Branches)

**Scenario**: By May 31 afternoon, shop visits >50 but orders <1 (conversion <2%).

**Mitigation**:
- **Immediate diagnostic** (May 31 afternoon):
  - Run A/B test: Are listings appearing in Etsy search for "cable clip"? (Test in incognito browser)
  - Review top 5 competitor listings: Compare photo quality, pricing, descriptions
  - Check cart/checkout flow: Try a test purchase to verify no UX issues
  
- **Quick fixes** (implement May 31-June 1):
  - Price reduction: Reduce introductory price by $1 on slowest product (test conversion lift)
  - Photo reorder: Swap hero image to best-performing variant (if you have A/B data from photos)
  - Title reorder: Move primary keyword (e.g., "cable clip") to position 1 in title
  - Tag adjustment: Use eRank to verify tags are high-volume (10,000+ searches)
  
- **If no improvement by June 2**:
  - Pause listings for 48-72 hours (remove from Etsy search)
  - Analyze: Are you in wrong category? Is product-market fit missing?
  - Consider temporary 20-30% discount to generate first reviews (reviews build algorithm trust)
  - Relaunch June 4-5 with optimized photos + lower price

---

### Risk 8: Quality Issue Discovered Post-Launch

**Scenario**: First customer receives clip on June 1-2, reports snap arm is too tight or broke on install.

**Mitigation**:
- **Day-1 response** (same day customer reports):
  - Offer full refund immediately (email within 2 hours)
  - Ask permission to take replacement unit back for analysis
  - Take clear photos of the issue for your records
  
- **Root cause analysis** (June 2-3):
  - Compare returned unit to test print: Is this an anomaly or systemic tolerance issue?
  - If anomaly: Note in log, no action needed
  - If systemic: Halt all orders, escalate to re-test branch immediately (may require design adjustment)
  
- **Customer management**:
  - Respond positively to any negative review (within 24 hours)
  - Offer resolution: Replacement + shipping paid, or full refund
  - Use feedback to improve next batch
  
- **Scaling up**: Post-print quality assurance is critical. By June 3+, implement per-batch QA (measure 5 clips per print batch with calipers, verify tolerance).

---

## Section 7: Capital & Cost Impact by Branch

### COGS & Margin Comparison

| Branch | Product | Unit COGS | Launch Price | Gross Margin | Notes |
|--------|---------|-----------|--------------|--------------|-------|
| **PASS** | ModRun Clips | $1.50 | $4.99 | 70% | PLA+ material $0.40, labor $0.50, platform fees $0.75, other $0.35 |
| **PASS-WITH-ADJUSTMENTS** | ModRun Clips v1.1 | $1.50 | $4.99 | 70% | Identical to PASS (minor tolerance tweak, no material change) |
| **FAIL** | Magnetic Labels | $0.55 | $4.99 | 89% | Labels $0.40, magnets $0.10, packaging $0.05. Lower COGS, same price = higher margin |
| **FAIL** | Clips v2 (later) | $1.50 | $5.99 | 75% | Redesigned after June 2; premium positioning with slight price increase |
| **PARTIAL-FAIL** | Mixed (passing sizes) | $1.50 | $4.99 | 70% | First listing only with available sizes; full range by June 6 |

---

### Capital Requirements by Branch (May 24-June 15)

| Branch | Printer | Filament | Packaging | Labels/Magnets | Total |
|--------|---------|----------|-----------|----------------|-------|
| **PASS** | Already own | $30 (5 kg stock) | $50 (mailers/tape) | N/A | $80 |
| **PASS-WITH-ADJUSTMENTS** | Already own | $30 (5 kg stock) | $50 | N/A | $80 |
| **FAIL (labels)** | Already own | $0 (no printing) | $30 | $120 (label printing) + $25 (magnets) | $175 |
| **FAIL (clips v2 redesign)** | Already own | $60 (re-test + v2 batch) | $50 | $120 | $230 |
| **PARTIAL-FAIL** | Already own | $40 (re-test batches) | $50 | N/A | $90 |

**Assumption**: You already own Bambu P1S ($699). All capital figures are incremental expenses for May 24-June 15 period.

---

### Revenue Forecast (30-Day Window Post-Launch)

| Branch | Launch Date | Expected Orders (30 days) | AOV | Revenue | Net Profit (after COGS + platform fees) |
|--------|-------------|---------------------------|-----|---------|-------------------------------------------|
| **PASS** | May 30 | 10-20 clips | $24.99 | $250-500 | $150-300 (68% net margin) |
| **PASS-WITH-ADJUSTMENTS** | May 31 | 8-15 clips | $24.99 | $200-375 | $120-225 (1-day launch delay impact) |
| **FAIL (labels)** | May 31 | 15-30 label sets | $4.99 | $75-150 | $50-105 (70% net margin) |
| **FAIL (clips v2)** | June 15 | 8-15 clips | $24.99 | $200-375 | $120-225 (clips v2 launch; labels still running) |
| **PARTIAL-FAIL** | May 30 (partial) | 6-12 units (passing only) | $24.99 | $150-300 | $90-180 (limited by partial range) |

**Note**: Forecasts are conservative (based on 2-5% Etsy conversion rates for new shops). Actual performance depends on photo quality, SEO implementation, and social media promotion.

---

## Section 8: Decision Checklist for May 24 Morning

**Print this section and use as a 5-minute checklist when test print completes:**

### Test Print Evaluation (May 24, 8:00-10:00 AM)

- [ ] **Snap-arm functional test**:
  - Clip snaps onto reference rail cleanly? YES / NO / PARTIAL
  - Releases without force? YES / NO / PARTIAL
  - Snap 5 cycles without cracking? YES / NO / PARTIAL
  - Cable fits (3-10mm range)? YES / NO
  
  **Result**: ✓ PASS / ⚠️ PASS-WITH-ADJUSTMENTS / ❌ FAIL

- [ ] **Dimensional check** (calipers + CAD spec):
  - Snap-arm clearance: ___mm (Target: ±0.5mm)
  - Rail channel width: ___mm (Target: ±0.5mm)
  - Deviation: ______mm
  
  **Result**: ✓ Within ±0.5mm / ⚠️ 0.1-0.5mm deviation / ❌ >0.5mm deviation

- [ ] **Surface quality**:
  - Layer separation visible? YES / NO
  - Warping: ___mm max (Target: <1mm)
  - Surface finish acceptable? YES / NO
  
  **Result**: ✓ PASS / ⚠️ Minor issues / ❌ Unacceptable

---

### Routing Decision (10:00 AM)

**Use decision tree (Section 1) to route to corresponding branch:**

- [ ] **All criteria PASS** → **SECTION 2: PASS BRANCH** (May 30 launch)
- [ ] **Snap works but tolerance off 0.1-0.5mm** → **SECTION 3: PASS-WITH-ADJUSTMENTS** (May 26 re-test, May 31 launch)
- [ ] **Snap arm cracks / won't engage** → **SECTION 4: FAIL BRANCH** (Pivot to labels May 31, clips v2 June 15)
- [ ] **Some sizes pass, some fail** → **SECTION 5: PARTIAL-FAIL BRANCH** (May 30 launch partial range)

---

### Next Actions by 10:30 AM

| Branch | Action | Owner | Deadline |
|--------|--------|-------|----------|
| **PASS** | Approve design for production. Start Phase A shop setup (May 25). | You | May 25, 8:00 AM |
| **PASS-WITH-ADJUSTMENTS** | Document deviation. Update CAD or print settings. Queue re-print for May 26 morning. | You | May 26, 8:00 AM |
| **FAIL** | Analyze failure mode. Order label printing + magnets (May 26). Scope clips v2 redesign. | You | May 26, 8:00 AM |
| **PARTIAL-FAIL** | Document passing/failing sizes. Adjust CAD for failing sizes. Queue for May 26 re-test. | You | May 26, 8:00 AM |

---

## Final Notes

**This document is designed for execution, not reading.** 

- **Before May 22**: Skim Sections 1-5 to understand the decision tree and your branch options.
- **May 23-24 morning** (test complete): Use Section 8 checklist to route to your branch (2-3 minute decision).
- **May 24-31**: Execute the corresponding branch timeline (Sections 2-5). All timelines are mechanical; no further planning needed.
- **June 1-15**: Monitor operations, handle customer feedback, prepare for next phase of scaling.

**Key principle**: Eliminate May 24-25 ambiguity. By reviewing this document before the test print, you'll make your go/no-go decision in under 5 minutes and execute launch immediately.

**Questions before test print**:
- Do you have Etsy account + email ready for shop creation?
- Do you have business bank account open (from post-test-print-launch-prep.md Phase 2)?
- Do you have inventory pre-printed (target: 40+ units by May 24)?
- Do you have product photos ready (or can shoot May 25-26)?

If you answered "no" to any of these, complete those tasks before May 22 test print begins.

---

**Status**: ✅ Ready for execution  
**Confidence**: High (aligned with ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md, cost model validated)  
**Version**: 1.0 (Session 1447, May 21, 2026)
