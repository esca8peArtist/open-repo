---
title: Post-Test-Print Quick Reference — Print & Post This
project: mfg-farm
created: 2026-05-06
format: printable checklist (intended for paper or mobile reference)
scope: daily execution guide; one page per week
---

# POST-TEST-PRINT QUICK REFERENCE

**Print this document. Post on desk. Reference daily.**

---

## PRE-START (Do Now, Before Test Print Completes)

- [ ] Order silicone bumper pads (100-pack, AliExpress) — 7–14 day lead time
- [ ] Confirm filament: 500g+ Matte Black PLA+ on hand
- [ ] Verify Pirate Ship account (test one label print)
- [ ] Clear desk/workspace for printing Friday

**Status:** Ready / Blocked (if blocked, note why: _______________)

---

# WEEK 1: Design Validation & Photos

**Duration:** 6 hours (mostly active)  
**Deadline:** All work done by Sunday evening

### Day 1–2: ModRun STL Refinement
```
Time: 30 min
□ Inspect test-print (rail jaw, clip snap)
□ Photo test-print issues (if any)
□ Generate refined STLs (tolerance 0.15–0.25)
□ Git commit with tolerance value
```

### Day 1–3: Hooks Fit-Test & Print
```
Time: 3 hours
□ Measure desk thickness with calipers
□ Generate 3 hook STL variants
□ Slice 25mm variant (0.20mm layer, 25% gyroid)
□ Print 1× 25mm hook (25 min)
□ Cool 30 min
□ Test fit: jaw pressure OK? No rock >1mm?
  Pass? → Tolerance locked ✓
  Tight? → Rerun with 0.25 tolerance
  Loose? → Rerun with 0.10 tolerance
□ Test cable post: no wobble, smooth tip
□ Print 4-unit QA batch (one plate, 95 min)
□ Store in 4×6" zip bags
```

### Day 4–7: Photography
```
Time: 2.5 hours
□ Set up desk: same as current ModRun photos
□ ModRun session: 5 shots minimum
  □ Hero (clip on rail, cable organized)
  □ Close-up (snap-fit detail)
  □ Ecosystem (rail + clip + hook visible)
  □ [Bonus] Angle shots (3)
□ Hooks session: 5 shots minimum
  □ Hero (hook on desk, headphones hanging)
  □ Cable post detail (main differentiator)
  □ 3 sizes (12/25/40mm labeled)
  □ Under-desk clamp angle
  □ Ecosystem (hook + ModRun rail)
□ Edit photos: crop to 80%, +10% brightness, +5% contrast
□ Export: 2000×2000px, filename as {product}-{number}-{description}.jpg
□ Organize in project/mfg-farm/photos/ folder
```

### End-of-Week 1 Verification
```
□ ModRun STL committed to git
□ Hooks tolerance locked
□ 4 hook units printed & QA'd
□ 8+ photos taken & edited
□ NO more design changes planned
```

**Week 1 Status:** ☐ On track  ☐ Slipped 1 day  ☐ Slipped 2+ days (escalate)

---

# WEEK 2: Etsy Listings & Supplier Outreach

**Duration:** 2 hours  
**Deadline:** All work done by Friday

### Day 8–10: Etsy Listing Creation
```
Time: 1.5 hours

MODRUN UPDATE:
□ Open existing ModRun listing (Etsy Shop Manager)
□ Add 3 new photos: ecosystem shot, lifestyle, detail
□ Add cross-sell text to description:
  "Complete your desk setup — see our headphone hook 
   (cable management included) in this shop."
□ Save as draft

HEADPHONE HOOKS — NEW LISTING:
□ Create new Etsy listing (draft mode)
□ Paste title: "Desk Headphone Hook with Cable Manager | 
               3D Printed Clamp | Custom Color"
□ Paste full description from headphone-hooks-etsy-listing.md Section 2
□ Replace {{VARIABLES}}: city, state, processing days
□ Upload 5–7 photos in order:
  [1] Hero lifestyle
  [2] Cable post detail
  [3] Three sizes
  [4] Under-desk clamp
  [5] Ecosystem (hook + ModRun)
  [6] Color flat-lay (optional)
  [7] Scale reference (optional)
□ Set up personalization field:
  Label: "Select desk thickness + color"
  Instructions: [paste from template]
□ Set price: $12.99
□ Set shipping: USPS First Class, buyer pays
□ Set processing time: 1–3 business days
□ Set quantity: 100
□ Add all 13 tags (copy from template):
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
□ Save as draft (DO NOT publish yet)
```

### Day 11–14: Supplier Outreach
```
Time: 30 min
□ Send email to eSUN direct: contact@esun3dstore.com
  Subject: Bulk PLA+ Inquiry — 20–50 kg/month potential
  [Use template from main execution doc]
□ Send email to Anycubic: store.anycubic.com contact form
  (inquiry only — not ready for 50kg pallet yet)
□ Log quotes in spreadsheet as responses arrive
□ Do NOT make any purchases yet
```

### End-of-Week 2 Verification
```
□ ModRun listing updated & published (or keep as draft)
□ Hooks listing complete in draft (all fields filled)
□ Zero {{VARIABLES}} remaining in Hooks listing
□ Supplier emails sent (minimum 2 vendors)
□ Photo package ready for upload
```

**Week 2 Status:** ☐ On track  ☐ Slipped 1 day  ☐ Slipped 2+ days (escalate)

---

# WEEK 3: Inventory Production & Setup

**Duration:** 11.5 hours (8 hrs passive print monitoring)  
**Deadline:** All units printed & packaged by Saturday

### Day 15–16: Print 25mm Standard Batch
```
Time: 8 hours (mostly passive)
□ Slice 25mm_with_post in Bambu Studio (0.20mm, 25% infill)
□ Label plates: "Queue 1–5, Day 15–16"
□ Start Plate 1 (4 units, ~95 min): 9 AM
  [While printing, prep next plate in Slicer]
□ When Plate 1 finishes: remove, cool, bag → Start Plate 2
□ Repeat for Plates 3–5
□ Total time at printer: spread across 2 days
□ Cool all 20 units minimum 30 min before QA
□ Bag in 4×6" zip-lock bags; label "25mm, Date printed"
□ Store on shelf
```

### Day 16–17: Print Variants + QA
```
Time: 3 hours
□ Print 12mm variant (Plate 1, 4 units, 95 min)
□ Print 40mm variant (Plate 2, 4 units, 95 min)
  [Total: 3 hours print time; can batch-run if parallel printer available]
□ QA ALL 30 UNITS (90 min):
  For each unit:
  □ Inspect jaw: no cracks, smooth edges
  □ Check cable post: no wobble, smooth tip
  □ Test jaw grip: appropriate pressure
  □ Weigh (target 22–28g) — note if >2g off estimate
□ If bumper pads have arrived:
  □ Press-fit 2 pads into upper jaw pocket
  □ Press-fit 2 pads into lower jaw pocket
  □ Pads must sit flush (±0.2mm)
  □ Press hard — they're self-adhesive, should stay
  If bumper pads NOT arrived yet:
  □ Mark units "pads pending"
  □ Plan to install within 2 days
□ Final bag all units: 4×6" zip bags, labeled by variant
□ Store on shelf; inventory ready to ship
```

### Day 15–19: Packaging & Social Prep
```
Time: 1.5 hours (parallel to printing)
□ Print 30 thank-you cards + headphone hook URLs
  (Use existing template, add Etsy link)
□ Create "cross-sell" cards: "Complete Your Setup" with both URLs
□ Stock 30 of each card type on desk
□ Print/organize poly mailers, bubble wrap, zip bags
  → Create "Fulfillment station" on desk/shelf corner
□ Draft social content (save to local file):
  □ Instagram caption (60 chars) + photo
  □ TikTok script (15 sec, 3 scenes)
  □ Reddit r/battlestations post (3 sentences)
  □ Email subject lines + body (if you have list)
□ Schedule Instagram post for Day 22 10 AM
□ Save TikTok script for Day 22 recording
```

### End-of-Week 3 Verification
```
□ 30 hooks printed, QA'd, bagged
□ Bumper pads installed (or pending with follow-up plan)
□ Packaging supplies stocked & organized
□ Social content drafted & ready to post
□ Hooks listing still in draft; ready to publish
□ ModRun inventory balanced (if ran production batches)
```

**Week 3 Status:** ☐ On track  ☐ Bumper pads delayed  ☐ Print issue (_____)

---

# WEEK 4: LAUNCH & FIRST ORDERS

**Duration:** 4 hours active + 10 min/day ongoing  
**Deadline:** Publish by Thursday 10 AM

### Day 22: PUBLISH & LAUNCH

**10:00 AM — Publish Listing**
```
□ Open Etsy Shop Manager
□ Click "Publish" on Headphone Hooks draft listing
□ Confirm listing is live within 5 min
□ Copy listing URL
```

**10:30 AM — Enable Etsy Ads**
```
□ Go to Ads Manager (Etsy Shop Manager sidebar)
□ Create new campaign: "Headphone Hook Launch"
□ Budget: $1.00/day maximum
□ All 13 tags as keywords
□ Broad match
□ Confirm ads are running
```

**11:00 AM — Post Instagram**
```
□ Open Instagram
□ Post hero photo with caption:
  "New: Parametric Headphone Hook — desk clamp + cable 
   organizer in one. Fits 12–40mm desks. $12.99. Pairs with 
   ModRun cable system. [LINK] #desksetup #3dprinting"
□ Add link in bio if not already there
```

**5:00 PM — Post TikTok**
```
□ Record 15-second video (2–3 takes):
  Scene 1 (5s): Hook on desk, headphones in it, zoom to cable post
  Scene 2 (5s): Loop cable around post, show clean setup
  Scene 3 (5s): "Finally, a headphone hook that manages cables. 
                Etsy link in bio."
□ Post with caption: "Etsy link in bio"
□ Like/reply to comments immediately
```

### Day 23: Continue Social + Email (Optional)

**2:00 PM — Post Reddit**
```
□ Go to r/battlestations
□ Post new thread with photo + caption:
  "Designed and printed a headphone hook that actually 
   manages cables. Clamps 12–40mm desks, no tools. 
   Etsy link in comments if curious."
□ Reply to comments; keep tone casual
□ Upvote relevant replies
```

**9:00 AM — Send Email** (if you have list)
```
□ Draft subject: "New: Parametric Headphone Hook — 10% off for you"
□ Draft body: Include product description + 10% discount code
□ Send to email list
□ Track open rate (should be >30%)
```

### Day 24–28: Fulfillment & Monitoring

**DAILY (Morning, 5 min):**
```
□ Check Etsy Shop Manager for new orders
□ Check Etsy Stats: Views, CTR, Favorites (screenshot for records)
□ Check Q&A for new questions; reply <4 hours
□ Check Instagram/TikTok/Reddit for comments
```

**PER ORDER (10–15 min):**
```
□ Verify personalization: which size + color ordered?
□ Grab matching unit from shelf
□ Wrap in 4×6" zip bag (or ship as-is if no bag)
□ Wrap in bubble wrap (2–3 layers)
□ Place in 9×12" poly mailer
□ Add thank-you card
□ Add cross-sell card (ModRun + Hooks)
□ Print shipping label via Pirate Ship (USPS First Class)
□ Tape label to mailer
□ Seal with clear packing tape
□ Drop in mailbox or USPS
□ Mark order "shipped" in Etsy (include tracking #)
```

**Day 26–27: Metrics Check-In**

```
□ Review Etsy Shop Stats:
  ☐ Views >50? 
  ☐ CTR >1%?
  ☐ Favorites >5?
  ☐ Sales ≥1?
□ If Views <50 & CTR <1%:
  □ Replace hero photo with under-desk angle shot
  OR
  □ Increase Etsy Ads to $2/day
□ If all metrics healthy:
  □ Continue as-is; monitor daily
```

**Day 28: Margin Validation (30 min)**

```
□ Calculate actual COGS for units shipped:
  □ Filament weight (count units × 26g avg) → cost at $0.013/g
  □ Bumper pads (units × 2 pads × actual cost)
  □ Packaging (materials actually used)
  □ Etsy fees (from Shop Manager dashboard)
  □ Shipping labels (units × $0.35 Pirate Ship rate)
  □ Labor (4 min per unit × $15/hr = $1.00/unit)
□ Total COGS per unit shipped ÷ revenue per unit
□ Calculate margin %: (Revenue - COGS) / Revenue = ___%
□ Margin should be >70%
  ✓ Yes, on track
  ✗ No, <70% — investigate which cost rose
    (See margin alert protocol in revenue-ramp-metrics.md)
```

### End-of-Week 4 Verification

```
□ Hooks listing live & generating traffic
□ Etsy Ads running
□ 2–5 orders shipped
□ Margin >70% on all units shipped
□ Customer feedback: positive or actionable
□ Inventory replenishment: started if >5 units shipped
□ Revenue: Week 4 $450–575 target
```

**Week 4 Status:** ☐ Launch successful  ☐ Below target (slipped)  ☐ Above target (over-performed!)

---

# REVENUE TRACKING (Weekly, Sunday 6 PM)

Fill in every Sunday evening; update `revenue-ramp-metrics.md`

```
WEEK [1/2/3/4] — Sunday, [DATE]

Units shipped:
  ModRun rails: ___
  ModRun clips (bundles): ___
  Headphone hooks: ___
  Total: ___

Revenue:
  Gross: $___
  Etsy fees: $___
  Net: $___

Margin: ___%
  (Target: >70%)

Inventory on hand:
  Hooks: ___
  Filament (kg): ___
  Bumper pads: ___

Etsy metrics:
  Views: ___
  CTR: ___%
  Favorites: ___
  
Decisions this week:
  ☐ Increase ad spend
  ☐ Replace hero photo
  ☐ Start restock batch
  ☐ Price test
  ☐ No action needed
```

---

# EMERGENCY CONTACTS & CONTINGENCIES

**If X happens, do Y:**

| Issue | Action | Time to Resolve |
|---|---|---|
| Print fails mid-queue | Stop print, clear nozzle, restart plate | 30 min |
| Bumper pads late (Day 21+) | Ship without pads; follow up with replacement | 2–3 days |
| Order arrives with fit problem | Reply within 4 hours; offer replacement | 1–2 days |
| Etsy <50 views by Day 27 | Increase ads to $2/day OR change hero photo | 1 day |
| Filament runs out | Order emergency spool from Amazon Prime | Same day |
| Customer wants refund | Offer replacement first; refund if insisted | 1 day |

---

# SUCCESS METRICS: Print & Post

**By end of Week 4, you should have:**

```
DESIGN ✓
  [✓] ModRun STL refined & tested
  [✓] Hooks fit-test passed
  [✓] Tolerance locked

LISTINGS ✓
  [✓] ModRun updated with cross-sell
  [✓] Hooks listing live with photos
  [✓] All 13 tags live

INVENTORY ✓
  [✓] 30 units printed & QA'd
  [✓] Bumper pads installed
  [✓] Ready to ship

REVENUE ✓
  [✓] Week 4 revenue: $450–$575 gross
  [✓] Margin >70%
  [✓] 2–5 orders shipped
  [✓] 0 customer complaints

OPERATIONS ✓
  [✓] Social posts live (2–3 platforms)
  [✓] Email sent (if list exists)
  [✓] Orders processed <3 days
  [✓] Daily metrics monitored
```

---

**Print this page. Tape to your desk. Reference daily.**

**When test print passes, Day 1 = this checklist begins.**

---

*Last updated: 2026-05-06*  
*Status: READY FOR EXECUTION*
