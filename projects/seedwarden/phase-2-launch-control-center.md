---
title: "Phase 2 Launch Control Center"
subtitle: "Day-by-day calendar, critical path, dependencies, success metrics, and decision gates"
date: 2026-05-06
status: production-ready
target-launch: 2026-05-30
fallback-launch: 2026-06-06
references:
  - TRACK_B_FINAL_EXECUTION_GUIDE.md
  - phase-2-execution-timeline.md
  - phase-2-day-by-day-execution.md
  - may-30-launch-sequence.md
  - june-6-contingency-path.md
  - phase-2-tool-integration-map.md
---

# Phase 2 Launch Control Center

**Purpose**: This is the single master document for Phase 2 execution. It supersedes "week of" vague planning and replaces it with day-level specificity, explicit dependency gates, quantified success metrics, and documented decision points. Open this every morning. Close it every evening. Nothing else is needed for orientation.

**Launch target**: May 30, 2026
**Documented fallback**: June 6, 2026
**Days to primary target as of May 6**: 24

---

## Part 1: Critical Path — What Unlocks What

The following chains are absolute. A downstream task cannot begin until its upstream gate is complete. Any chain that breaks shifts the launch date.

### Chain A: Zone Cards → Email Delivery (Highest Risk Chain)

```
Canva Brand Kit setup (30 min)
    UNLOCKS →
Zone 5 master card build (3 hrs)
    UNLOCKS →
Zones 6, 3, 4, 7, 8, 9, 10 (duplicate builds, 35-45 min each)
    UNLOCKS →
All 8 PDF exports (PDF Print quality, correct naming)
    UNLOCKS →
Google Drive upload + sharing permission set to "Anyone with link"
    UNLOCKS →
Direct download URL capture (?export=download&id= format)
    UNLOCKS →
Kit Email 1 zone variant URL replacement
    UNLOCKS →
End-to-end test (Zone 5 + Zone 7 incognito sign-up)
    UNLOCKS →
Kit automation published (landing page accepts live subscribers)
    UNLOCKS →
Social bio link goes live (permanent, not "coming soon")
```

**Hard deadline for Zone 5 master card**: Must be in draft form by May 14. If Zone 5 is not started by May 14, the Kit automation cannot be live by May 25, which means 5 days of pre-launch list-building are lost and the downstream test window compresses to unacceptable.

**Hard deadline for all 8 PDFs in Kit**: May 28. This is 2 days before launch and gives time to re-test download URLs if permissions were reset in Drive.

---

### Chain B: Photo Shoot → Etsy 5-Image Status

```
Props sourcing (May 5-9, any time)
  AND
Germination tray started (April 30 — past deadline; fallback: bean sprout tray or mock prop)
    TOGETHER UNLOCK →
May 10-11 shoot (Clusters A, B, C — 30 RAW images)
    UNLOCKS →
Image culling: 80-100 RAW → 30 selects (May 12, 2 hrs)
    UNLOCKS →
Batch editing (May 12-13, 3-4 hrs)
    UNLOCKS →
Export 30 JPEGs to /marketing/lifestyle-photos/etsy-ready/
    UNLOCKS →
Canva lifestyle compositing (upload lifestyle photo → overlay product mockup → 2400×2400px export)
    UNLOCKS →
Etsy slot 4 + slot 5 upload (21 listings)
    UNLOCKS →
Etsy 5-image status (Phase 2 visual upgrade live)
```

**If shoot slips to May 17-18**: This chain shifts by 7 days. Etsy lifestyle images land May 28-June 4 instead of May 22-25. June 6 fallback path activates. Chain A (zone cards → email) is unaffected — run it on the original schedule.

---

### Chain C: Social Accounts → Bio Link → Email List Building

```
Instagram, TikTok, Pinterest accounts created (May 5-6)
    UNLOCKS →
Profile images, bios, and contact details filled
    UNLOCKS →
Kit landing page URL added to all three bios
    (BLOCKED UNTIL: Kit landing page published — Chain A, Step 4)
    UNLOCKS →
Organic subscriber acquisition from social bio clicks
    UNLOCKS →
Email list at target count before broadcast (50+ subscribers on May 30)
```

**If social accounts not created by May 9**: Instagram and Pinterest still get created. TikTok can launch May 16 without impacting the May 30 target (TikTok is lowest-velocity for this audience; Instagram and Pinterest bio links drive the bulk of organic email sign-ups).

---

### Chain D: Etsy Coupon → Email 5 Conversion

```
SEEDWARDEN15 coupon created in Etsy (by May 20)
    UNLOCKS →
Email 5 goes live with valid coupon code (May 16 for first subscriber)
    UNLOCKS →
Coupon redemption window (5 days from Email 5 receive date)
    PRODUCES →
First Phase 2 attributed purchases
```

**Critical timing note**: First subscriber who signs up on May 6 (day Kit landing page goes live) hits Email 5 on May 16. The coupon must be active in Etsy by May 16. Creating it May 20 as originally planned may miss the first subscribers. Recommendation: create SEEDWARDEN15 on the same day the Kit landing page is published (Action 3 in the master guide, May 5-6).

---

## Part 2: Day-by-Day Calendar — May 6 through June 2

### May 6 (Wednesday) — Foundation Day

**Priority**: All three. These actions are the prerequisite gate for everything.

| Time | Action | Duration | Reference |
|---|---|---|---|
| Morning | Create Instagram Business account, upload logo, fill bio | 15 min | TRACK_B_SOCIAL_ACCOUNT_CHECKLIST.md |
| Morning | Create TikTok Business account, upload logo, fill bio | 15 min | TRACK_B_SOCIAL_ACCOUNT_CHECKLIST.md |
| Morning | Create Pinterest Business account, upload logo, fill bio | 15 min | TRACK_B_SOCIAL_ACCOUNT_CHECKLIST.md |
| Morning | Set up Canva Brand Kit (6 brand colors + 4 zone band colors, 3 fonts, logo upload) | 30 min | TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md Part 1 |
| Afternoon | Create Kit account at kit.co (email: wanka95@gmail.com, sender: Seedwarden) | 15 min | TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md Step 1 |
| Afternoon | Create all 15 Kit tags (8 zone tags + 7 behavioral/lifecycle tags) | 15 min | TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md Step 2 |
| Afternoon | Build Kit landing page ("Your Free Zone Quick-Start Card" — 3 fields, dropdown Zone 3-10) | 45 min | TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md Step 3 |
| Afternoon | Publish Kit landing page; copy URL; add to all 3 social bios | 10 min | social-media-setup.md |
| Afternoon | Create SEEDWARDEN15 coupon in Etsy (15% off, all listings, no expiry in Etsy) | 5 min | Etsy Shop Manager > Marketing > Coupons |
| Evening | Film Day 1 Reel (origin story, 30-45 sec, talking head) | 30 min | phase-2-social-content-calendar-60day.md Day 1 |

**Done signal for May 6**: Three social accounts live with bios and Kit URL. Canva Brand Kit saved. Kit landing page published with working URL in all bios. SEEDWARDEN15 coupon active.

---

### May 7 (Thursday) — First Content Day

| Time | Action | Duration | Reference |
|---|---|---|---|
| Morning | Upload Day 1 Reel to Instagram (Reels section) | 5 min | — |
| Morning | Upload same video natively to TikTok (do not cross-post) | 5 min | TRACK_B_SOCIAL_ACCOUNT_CHECKLIST.md |
| Afternoon | Begin Zone 5 master card in Canva — Session 1A: layout only (header, 3-col body, footer) | 90 min | CANVA_ZONE_CARD_BATCH_WORKFLOW.md |
| Afternoon | Begin props sourcing checklist review — confirm what is on hand vs. what to source | 15 min | SHOOT_PROPS_CHECKLIST.md |
| Evening | Build Day 3 Carousel in Canva (5 slides, "5 guides for people growing their own food") | 60 min | phase-2-social-content-calendar-60day.md Day 3 |

---

### May 8 (Friday) — Zone 5 Content and Props

| Time | Action | Duration | Reference |
|---|---|---|---|
| Morning | Zone 5 master card — Session 1B: populate Zone 5 content (frost dates, crops, tips, variety spotlight) | 60 min | CANVA_ZONE_CARD_BATCH_WORKFLOW.md Zone 5 |
| Morning | Zone 5 PDF export test — download as PDF Print quality, open in viewer, confirm no issues | 15 min | TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md Part 2 |
| Afternoon | Props sourcing run: garden center (terracotta pots, trowel, germination tray), grocery store (mason jars, hot peppers, garlic), fabric store (1 yard dark linen if needed) | 90 min | SHOOT_PROPS_CHECKLIST.md |
| Afternoon | Print 20-25 pages of product PDFs for shoot props (color if available; B&W acceptable) | 45 min | PHOTO_SHOOT_SCHEDULE_AND_PROPS.md Part 4 |
| Evening | Label 3 seed envelopes: "Brandywine Tomato 2026," "Dragon Tongue 2026," "Black Krim 2026" | 10 min | — |
| Evening | Post Day 3 Carousel to Instagram | 5 min | MAY_CONTENT_EXECUTION_PLAN.md |

**Done signal for May 8**: Zone 5 card in full draft, PDF export test passed. Props sourced and on hand. Print pages printed.

---

### May 9 (Saturday) — Zone 6 Card and Shoot Prep Final

| Time | Action | Duration | Reference |
|---|---|---|---|
| Morning | Build Zone 6 card: duplicate Zone 5, substitute Zone 6 content, verify no Zone 5 text remains | 45 min | CANVA_ZONE_CARD_BATCH_WORKFLOW.md Zone 6 |
| Morning | Zone 6 PDF export test | 10 min | — |
| Morning | Build first 6 Pinterest pins in Canva | 90 min | pin-template-specs.md |
| Afternoon | Schedule 6 Pinterest pins (Tue-Fri, 8-11pm) in Pinterest native scheduler | 20 min | TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md Part 3 |
| Afternoon | Shoot pre-check: confirm all props on hand, germination tray status, printed pages flat (not folded), phone charged, window location confirmed | 30 min | PHOTO_SHOOT_SCHEDULE_AND_PROPS.md Part 5 |
| Afternoon | Set phone camera: white balance to Daylight or Cloudy (not Auto), clear 3+ GB storage, enable selfie timer 3 seconds | 10 min | — |
| Evening | Stage Cluster A props on shoot surface; do a test shot; confirm exposure and focus | 20 min | phase-2-day-by-day-execution.md Day 1 |

**Done signal for May 9**: Zones 5 and 6 cards complete (draft). 6 Pinterest pins scheduled. Shoot surface tested. All props confirmed.

---

### May 10 (Sunday) — Photo Shoot Day 1

| Time | Action | Duration |
|---|---|---|
| 8:30am | Shoot setup: lay out Cluster A props, bounce board positioned, test shot reviewed | 20 min |
| 9:00am-1:30pm | Session 1 — Cluster A: 16 shots, Products 1-8 (flat-lay then contextual per product) | 4.5 hrs |
| 1:30pm | Immediate transfer: Cluster A files → /marketing/lifestyle-photos/raw/cluster-a/ | 15 min |
| 3:00pm-5:00pm | Session 2 — Cluster B: 8 shots, Products 9-12 (potted herb, window sill, balcony context) | 2 hrs |
| 5:00pm | Immediate transfer: Cluster B files → /marketing/lifestyle-photos/raw/cluster-b/ | 15 min |

**Done signal for May 10**: 24+ RAW files imported across Clusters A and B. All 8 Cluster A products have at least one flat-lay and one contextual shot without critical focus errors.

---

### May 11 (Monday) — Photo Shoot Day 2 and Culling

| Time | Action | Duration |
|---|---|---|
| 9:00am-11:00am | Session 3 — Cluster C: 6 shots, Products 13-15 (mason jars, kitchen counter) | 2 hrs |
| 11:00am | Immediate transfer: Cluster C files → /marketing/lifestyle-photos/raw/cluster-c/ | 15 min |
| Afternoon | Image culling: all 80-100 RAW files → tag green (usable) / red (cull) / yellow (backup) | 2 hrs |
| Afternoon | Cull to 30 selects: 2 per product (1 flat-lay, 1 contextual), all 15 products | — |
| Evening | Build Zone 3 card in Canva (duplicate from Zone 5, substitute content, change band to #3D6B8A Cool) | 45 min |

**Done signal for May 11**: 30 RAW selects identified and tagged. All 15 products have 2 selects each. Zone 3 card in draft.

---

### May 12 (Tuesday) — Batch Editing

| Time | Action | Duration |
|---|---|---|
| Morning | Open all 30 selects in Lightroom Mobile or Snapseed | 15 min |
| Morning-Afternoon | Create edit preset on best Cluster A image: Exposure +0.3, Highlights -20, Shadows +25, WB 5200-5500K, Saturation -5, Clarity +10 | 30 min |
| Afternoon | Sync preset to all Cluster A images; adjust outliers individually | 45 min |
| Afternoon | Edit Cluster B images (same preset; adjust WB for late-afternoon warmth if needed) | 30 min |
| Evening | Edit Cluster C images (pull WB to 5000-5200K; mason jar contents should look appetizing, not orange) | 30 min |
| Evening | Build Zone 4 card in Canva (duplicate from Zone 3, substitute Zone 4 content) | 40 min |

---

### May 13 (Wednesday) — Export and Kit Account Setup Start

| Time | Action | Duration |
|---|---|---|
| Morning | Export all 30 files: 2400px long edge, 1:1 crop (square), JPEG, 88-90% quality | 60-90 min |
| Morning | File naming: [product-slug]-lifestyle-flat.jpg (slot 4), [product-slug]-lifestyle-context.jpg (slot 5) | — |
| Morning | File size check: all must be under 2MB. Use squoosh.app for anything over | 15 min |
| Morning | Save to /marketing/lifestyle-photos/etsy-ready/; confirm 30 files present | 10 min |
| Afternoon | Kit account: add SPF record to domain DNS (v=spf1 include:sendgrid.net ~all) | 20 min |
| Afternoon | Kit account: add DKIM record (CNAME from Kit Settings > Email Settings) | 10 min |
| Afternoon | Build Zone 7 card in Canva (duplicate from Zone 5, band #C9943A Warm) | 45 min |

**Done signal for May 13**: 30 JPEG files in /etsy-ready/, correctly named, all under 2MB. Kit DNS records added (DNS propagation begins: confirm in 24-48h).

---

### May 14 (Thursday) — Canva Lifestyle Compositing Begins and Kit DNS Verify

| Time | Action | Duration |
|---|---|---|
| Morning | Verify Kit DNS: Settings > Email Settings > SPF and DKIM status. Should show green. If still pending, wait another 24h. | 10 min |
| Morning | Send test email from Kit to wanka95@gmail.com; confirm it arrives in inbox (not spam) | 5 min |
| Morning | Build Zone 8 card in Canva (duplicate from Zone 7, band #C9943A Warm, different content) | 40 min |
| Afternoon | Canva lifestyle compositing — begin SW-Master-FlatLay template build: 2400×2400px canvas, best Cluster A flat-lay as background, product mockup overlay with drop shadow, Deep Forest Green brand strip at bottom | 2.5 hrs |
| Evening | Test export SW-Master-FlatLay: confirm product visible at thumbnail size (7% zoom test) | 15 min |

**Decision gate end of day May 14**: Is the May 10-11 shoot complete with 30 usable selects? If yes: proceed to May 30 path. If no (shoot not yet happened): assess May 17-18 window and read june-6-contingency-path.md.

---

### May 15 (Friday) — Cluster D+E Stock Compositing and Kit Landing Page Verify

| Time | Action | Duration |
|---|---|---|
| Morning | Canva compositing — Cluster D+E (5 products × 2 slots = 10 images using stock-raw/ files): upload each stock background, overlay product mockup from /mockups/, export 2400×2400px JPEG | 2-3 hrs |
| Afternoon | Upload Cluster D+E images to Etsy slots 4-5 (5 products): Etsy Shop Manager > Listings > Edit > Photos | 30 min |
| Afternoon | Upload Cluster C images to Etsy slots 4-5 (3 kitchen products) | 20 min |
| Afternoon | Build Kit Email 1 — Zone 5 variant. Subject: "Your Zone 5 Quick-Start Card is ready, [First Name]." Use [ZONE-5-PDF-URL] placeholder for download button. | 45 min |
| Evening | Zone 9 card in Canva (duplicate from Zone 5, band #A0522D Hot) | 45 min |

**Done signal for May 15**: Cluster D+E and C (8 products total) are at 5-image status in Etsy. Zone 9 card in draft.

---

### May 16 (Saturday) — Kit Email Build Sprint

| Time | Action | Duration |
|---|---|---|
| Morning | Build Kit Email 1 — remaining 7 zone variants (duplicate Zone 5 variant, change zone number in subject, opening sentence, and download link placeholder for each) | 60 min |
| Morning | Build zone routing automation in Kit: Trigger = form submitted; Tag subscriber by zone; Route to correct Email 1 variant | 30 min |
| Afternoon | Build Kit Email 2 (Day 2 delay): heirloom seed philosophy — no tracked links, no product offer | 25 min |
| Afternoon | Build Kit Email 3 (Day 5 delay): seed saving mistake story — embed tracked link to Seed Saving Field Manual with "seed-saver" click trigger | 30 min |
| Evening | Build Kit Email 4 (Day 7 delay): catalog introduction — 3 tracked links with tags (city-grower, seed-saver, preservationist) | 35 min |
| Evening | Build Kit Email 5 (Day 10 delay): first offer — SEEDWARDEN15 coupon, product recommendations, 5-day window framing | 30 min |
| Evening | Zone 10 card in Canva (duplicate from Zone 9, substitute Zone 10 content) | 40 min |

**Done signal for May 16**: All 5 welcome emails built in Kit sequence with correct delays (Day 0, 2, 5, 7, 10). All 8 Email 1 zone variants built. Zone routing automation in Kit (draft state).

---

### May 17 (Sunday) — Zone Card QA and Canva Lifestyle Sprint

| Time | Action | Duration |
|---|---|---|
| Morning | Full zone card QA: open all 8 cards in Canva folder. Run per-card checklist (zone number, no content leakage from Zone 5, footer placeholder brackets visible, PDF export test passes) | 90 min |
| Afternoon | Canva lifestyle compositing — Cluster B (4 products × 2 slots = 8 images) | 90 min |
| Afternoon | Build SW-Master-Tablet template: 2400×2400px, contextual (hands/use) background photo, same brand strip | 60 min |
| Evening | Upload Cluster B images to Etsy slots 4-5 (4 urban/container products) | 20 min |

---

### May 18 (Monday) — Canva Lifestyle Sprint: Cluster A First Half

| Time | Action | Duration |
|---|---|---|
| Evening | Canva lifestyle compositing — Cluster A, Products 1-4 (8 images) | 90 min |

---

### May 19 (Tuesday) — Canva Lifestyle Sprint: Cluster A Second Half

| Time | Action | Duration |
|---|---|---|
| Evening | Canva lifestyle compositing — Cluster A, Products 5-8 (8 images) | 90 min |

---

### May 20 (Wednesday) — Kit Automation Test and Etsy Upload Continue

| Time | Action | Duration |
|---|---|---|
| Morning | Upload Cluster A Products 1-4 lifestyle images to Etsy slots 4-5 | 25 min |
| Afternoon | Upload Cluster A Products 5-8 lifestyle images to Etsy slots 4-5 | 25 min |
| Afternoon | Verify: all 21 Etsy listings now showing 5-image stacks in Shop Manager | 10 min |
| Evening | Lifestyle image QA: open all 21 composited images in Canva grid — run technical checklist and brand consistency check (CANVA_EXECUTION_PLAYBOOK.md Section 6.2-6.4) | 60 min |

**Done signal for May 20**: All 21 Etsy listings at 5-image status (slots 4 and 5 populated). All composited images pass QA.

---

### May 21 (Thursday) — Footer URL Replacement in Zone Cards

| Time | Action | Duration |
|---|---|---|
| Morning | Confirm Kit landing page URL (should have been live since May 6) | 5 min |
| Morning | Confirm Etsy store URL is live (Phase 1 listings active) | 5 min |
| Evening | Open all 8 zone cards in Canva. Replace [KIT-URL] and [ETSY-URL] brackets with live URLs. | 30 min |
| Evening | Re-export all 8 zone cards as PDF Print quality after URL replacement | 30 min |
| Evening | Name files exactly: zone-3-quick-start-card.pdf through zone-10-quick-start-card.pdf | 5 min |

---

### May 22 (Friday) — Google Drive Upload and Kit URL Wiring

| Time | Action | Duration |
|---|---|---|
| Morning | Create Google Drive folder: "Seedwarden Zone Cards — Live" | 5 min |
| Morning | Upload all 8 zone card PDFs to the folder | 15 min |
| Morning | Set sharing on each file: "Anyone with the link can view" (not Restricted) | 10 min |
| Morning | Copy direct download URL for each file using format: https://drive.google.com/uc?export=download&id=[FILE-ID] | 20 min |
| Morning | Test each URL in incognito: download dialog must appear (not viewer, not "request access") | 20 min |
| Morning | Log all 8 URLs in WORKLOG.md labeled by zone number | 10 min |
| Afternoon | Open Kit Email 1 — each of 8 zone variants. Replace [ZONE-X-PDF-URL] placeholder with the corresponding Google Drive download link | 30 min |
| Afternoon | Preview each Email 1 variant in Kit: confirm full URL including ?export=download parameter was not stripped | 15 min |

**Done signal for May 22**: All 8 zone card PDFs uploaded to Drive with working download links. All 8 Kit Email 1 zone variants have live URLs in the download button.

---

### May 23 (Saturday) — Kit End-to-End Test and Automation Go-Live

| Time | Action | Duration |
|---|---|---|
| Morning | Test 1 (Zone 5): open Kit landing page in incognito. Sign up with secondary email, Zone 5. Confirm Email 1 arrives within 60s. Confirm PDF downloads (not viewer). Confirm zone-5 and new-subscriber tags applied. Confirm Email 2 queued for Day 2. | 20 min |
| Morning | Test 2 (Zone 7): repeat full test with Zone 7 selected | 15 min |
| Morning | Test 3 (behavioral tag): manually send Email 3 to test email; click Seed Saving Field Manual link; confirm seed-saver tag applied | 10 min |
| Afternoon | If all 3 tests pass: publish Kit automation. The landing page now delivers zone cards to live subscribers automatically. | 2 min |
| Afternoon | If any test fails: document failure point in WORKLOG.md. Fix before publishing. Fastest failure fixes: Drive sharing permission (5 min), Kit URL format (5 min), automation routing logic (15 min). | Variable |
| Afternoon | Re-authorize all Buffer/Later social connections (OAuth reset: up to 90-day fresh window for Instagram/Pinterest, 60 days for TikTok) | 10 min |

**Done signal for May 23**: All 3 end-to-end tests pass. Kit automation published. Automation is live and accepting real subscribers. Buffer connections re-authorized.

---

### May 24 (Sunday) — Select Top Lifestyle Images and Begin Social Scheduling

| Time | Action | Duration |
|---|---|---|
| Afternoon | Select 10 top lifestyle images for launch-week social use (from /etsy-ready/ folder) | 30 min |
| Afternoon | Crop social variants from top lifestyle images: Instagram (1080×1080px JPEG), Pinterest (1000×1500px JPEG) | 45 min |
| Evening | Begin loading 60-day social calendar content into Buffer/Later (start with Week 1 launch posts) | 45 min |

---

### May 25 (Monday) — Batch Produce Pinterest Pins

| Time | Action | Duration |
|---|---|---|
| Evening | Batch-produce 10+ Pinterest pins using lifestyle images (1000×1500px JPEG, Canva templates from pin-template-specs.md) | 90 min |
| Evening | Schedule Pinterest pins for Week 1 post-launch (June 1-4, 3-4 pins per day, 8-11pm slots) | 20 min |

---

### May 26 (Tuesday) — Social Scheduling: Launch Week Posts

| Time | Action | Duration |
|---|---|---|
| Evening | Load all May 30 launch posts into Buffer/Later: Instagram 2pm, TikTok 2pm, Pinterest 3:30pm | 45 min |
| Evening | Load May 31-June 2 social posts (Days 2-4 of launch week) into Buffer/Later | 45 min |
| Evening | Preview each scheduled post in Buffer/Later — confirm image attached, caption complete, correct time | 15 min |

---

### May 27 (Wednesday) — Full QA Sprint

| Time | Action | Duration |
|---|---|---|
| Morning | Zone card QA (final): open all 8 PDFs in a viewer. Verify zone numbers correct, no placeholder brackets remain, footer URLs live | 45 min |
| Morning | Lifestyle image QA (final): open all 21 Etsy listings in public browser. Confirm slots 4 and 5 images are visible and correctly ordered | 30 min |
| Afternoon | Kit launch broadcast draft: Broadcasts > New Broadcast > subject "Phase 2 is live — your zone card library just doubled" > paste broadcast copy from marketing/email-and-launch-plan.md > Send to "All Confirmed Subscribers" | 30 min |
| Afternoon | Kit broadcast: set schedule for May 30 12:00pm. Confirm status reads "Scheduled" — not "Draft" | 5 min |
| Evening | Social scheduler: confirm all May 30 posts show "Scheduled" status, no "Reconnect" errors on any platform | 10 min |

---

### May 28 (Thursday) — Buffer Re-Auth and Final Checks

| Time | Action | Duration |
|---|---|---|
| Morning | Re-authorize all Buffer/Later connections (Instagram, TikTok, Pinterest) — this resets OAuth tokens to today's fresh window | 15 min |
| Morning | Open Buffer Settings > Connected Accounts — confirm all 3 show green/active (no "Reconnect" warning) | 5 min |
| Afternoon | Test Kit landing page from incognito one more time — confirm automation still live, form accepts input, Email 1 delivers | 15 min |
| Afternoon | Verify all 8 Google Drive zone card URLs still deliver download (not "Request Access") — Drive permissions can reset | 20 min |
| Afternoon | Verify SEEDWARDEN15 coupon in Etsy: Marketing > Coupons > confirm "Active" status and 15% discount | 5 min |
| Evening | Record pre-launch baseline metrics in customer-analytics.csv: Etsy shop views (7-day), orders (all time), Kit subscribers, Instagram followers, TikTok followers, Pinterest monthly viewers | 15 min |

---

### May 29 (Friday) — Staging and Pre-Launch QA

| Time | Action | Duration |
|---|---|---|
| Morning | Send test email to secondary address — confirm Kit welcome automation still live (sign up from incognito, confirm Email 1 arrives) | 10 min |
| Morning | Confirm all scheduled social posts in Buffer/Later show correct times and captions | 10 min |
| Afternoon | Verify Kit broadcast: status must read "Scheduled," time must show "May 30 12:00pm [your timezone]" | 5 min |
| Afternoon | Open Etsy Shop Manager > Listings — confirm all 21 listings show "Active" status (green) | 10 min |
| Afternoon | Open 5 random listings in public browser (incognito) — confirm lifestyle images visible in slots 4 and 5 | 10 min |
| Evening | Read launch-day-script.md top to bottom. No decisions on launch day — only execution. | 20 min |

**Done signal for May 29**: Kit automation live and delivering. Broadcast scheduled. Social posts scheduled. All 21 Etsy listings at 5-image active status. Pre-launch metrics logged. Everything is staged. May 30 is execution, not preparation.

---

### May 30 (Saturday) — LAUNCH DAY

See `phase-2-launch-day-checklist.md` for the minute-by-minute execution sequence.

**Summary schedule**:
- 8:00am-9:00am: Final QA block (Etsy, Kit, social, zone card delivery)
- 9:00am-9:55am: Record pre-launch baselines; open monitoring tabs; protect time
- 10:00am: Etsy launch confirmed (all 21 listings at 5-image status, SEEDWARDEN15 active)
- 12:00pm: Kit broadcast sends automatically — verify by 12:05pm
- 2:00pm: Instagram and TikTok posts go live (Buffer auto)
- 3:30pm: Pinterest pins go live (Buffer auto)
- 7:00pm-9:00pm: End-of-day metric log; respond to any buyer messages within 4 hours

---

### May 31 (Sunday) — Day After Launch

| Time | Action | Duration |
|---|---|---|
| Morning | Check Etsy views and orders at 8am | 5 min |
| Morning | Check Kit broadcast: open rate and click rate (expect 35%+ opens, 8%+ clicks) | 5 min |
| Morning | Respond to any buyer Etsy messages or email replies to broadcast | 15 min |
| Evening | Check Kit subscriber count: new sign-ups from launch day should show | 5 min |
| Evening | Check social engagement: Instagram impressions and profile visits, TikTok views | 5 min |

---

### June 1 (Monday) — Launch Week Day 3

| Time | Action | Duration |
|---|---|---|
| Evening | Check Kit automation: Email 1 delivery complete for all launch-day subscribers? | 5 min |
| Evening | Check Etsy traffic trend: is Day 3 traffic above Day 1 baseline (organic growth from social)? | 5 min |
| Evening | If any subscriber replies to Email 1 asking a question: respond personally (Kit Conversations or Gmail) | Variable |

---

### June 3 (Wednesday) — Day 5 Benchmark

| Time | Action | Duration |
|---|---|---|
| Evening | Kit Email 3 check: open rate for subscribers who received it (40%+ target) | 5 min |
| Evening | Behavioral tag check: how many subscribers now have seed-saver, city-grower, or preservationist tags? | 5 min |

---

### June 6 (Saturday) — Week 1 Full Review (Decision Gate)

| When | What | Where | Reference |
|---|---|---|---|
| Morning | Full Week 1 metrics review (see Part 4 success metrics table) | Kit, Etsy, social analytics | phase-2-week-1-success-metrics.md |
| Morning | Which products have the highest Etsy views and conversion? | Etsy Shop Manager > Stats | — |
| Morning | Which email cohort tags are most common? | Kit > Subscribers > filter by tag | — |
| Morning | Week 2 feature decision: which 2-3 products to spotlight in Week 2 social and email | Based on metrics above | phase-2-week-1-success-metrics.md Section 3 |

---

## Part 3: Risk Mitigation

### Risk 1: Photo Shoot Delayed to May 17-18

**Trigger**: May 10-11 shoot is unavailable due to weather, scheduling conflict, or equipment.

**Impact**: Cluster A, B, C lifestyle images arrive May 21 instead of May 13. Etsy lifestyle upload shifts from May 15-20 to May 28-June 4. Launch shifts from May 30 to June 6.

**What does NOT change**: Zone card production, Kit email setup, Kit automation testing, social account setup — all proceed on original schedule. Kit automation goes live May 23 regardless.

**Immediate actions upon deciding to defer shoot**:
1. Log decision in WORKLOG.md: "June 6 contingency activated. Trigger: photo shoot delay. Date decided: [date]."
2. Update Buffer/Later launch posts from May 30 to June 6 (same times: 2pm Instagram/TikTok, 3:30pm Pinterest)
3. Update Kit broadcast from May 30 12pm to June 6 12pm
4. Run May 30 teaser track instead: post zone card preview graphic ("Your free zone guide is ready — link in bio") and behind-the-scenes shoot content

**Revenue impact**: Zero. Phase 1 Etsy listings continue generating sales throughout the delay. The broadcast reaches the same list on June 6, which by then has 24-36 additional subscribers from the extra list-building days.

---

### Risk 2: Canva Zone Card Production Runs Long

**Trigger**: User is new to Canva Brand Kit — actual time is 2.5-3 hours per card instead of the documented 90-minute estimate for subsequent cards.

**Float in the schedule**: Zone card production has 8 days of float in the May 30 plan (May 7-28 window vs. the minimum May 7-21 window). At 3 hours per card × 8 cards = 24 hours, this is completable in 2 hours per evening over 12 evenings.

**Minimum viable path if time is acute**: Launch May 30 with 4 zone cards (Zones 5, 6, 7, 8 — highest US population concentration). Send "Zone 3, 4, 9, 10 coming Week 2" placeholder Email 1 to subscribers in those zones, with a follow-up email when those cards go live.

**Priority build order under compression**: Zone 5, Zone 6, Zone 7, Zone 8. Zones 3, 4, 9, 10 can release June 6-8 with no impact on launch.

---

### Risk 3: Kit Account Verification Blocked

**Trigger**: Kit account creation is delayed by email verification issues or business account review (sometimes triggered by a new account sending sequences to a list).

**Fallback — email-list-only launch**: 
- Collect email addresses via a Google Form (free, no account required): form fields are First Name, Email, and Growing Zone (radio buttons for Zones 3-10)
- Deliver zone cards manually via Gmail as email attachments (one reply per sign-up)
- Send welcome sequence manually from Gmail on the Day 2, 5, 7, 10 schedule
- This is not scalable, but at launch list sizes (5-50 subscribers) it is completely manageable
- Add Kit back in Week 2 when verification resolves: import the manual list, load subscribers into Kit, resume automation from wherever each subscriber is in the sequence

**Trigger for Google Form fallback**: Kit account not approved/live by May 20.

---

### Risk 4: Buffer/Later OAuth Token Silent Failure

**Trigger**: Social posts fail to publish on May 30 because a platform's OAuth token expired between setup and launch.

**Detection**: On May 30 at 8am QA, check Buffer Settings > Connected Accounts for any "Reconnect" or expired status.

**Recovery (launch morning)**: Re-authorize the expired connection (2 min per platform). Scheduled posts should then publish at their set time.

**Recovery (if posts fail silently)**: Log into each platform directly. Copy caption from phase-2-social-content-calendar-60day.md Day 30. Upload the corresponding image from /marketing/lifestyle-photos/etsy-ready/. Post manually. 15 minutes total across 3 platforms.

---

### Risk 5: Etsy Listing Removed or Flagged by Etsy

**Trigger**: One or more listings are placed under review or removed by Etsy policy enforcement between upload and launch.

**Detection**: May 30 8am QA: all 21 listings must show "Active" status. Any "Under Review" or "Removed" status triggers this protocol.

**Recovery**: 
- Check the specific listing for any policy violation note in Shop Manager
- If listed as Draft accidentally: click "Publish" (30 seconds)
- If under Etsy review: do not recreate the listing. Email Etsy support immediately. The review typically resolves in 24-48 hours. Launch proceeds with 20 active listings; the reviewed listing goes live when Etsy clears it.
- If violation is found (uncommon for PDF guides): review the product description and tags against Etsy's digital goods policies. Common issues: pricing claims in titles ("best"), health claims, copyright terms in descriptions. Correct and re-list.

---

## Part 4: Success Metrics — Launch Week Targets

### May 30 (Day 1 — Launch)

| Channel | Metric | Target | Minimum Acceptable | Source |
|---|---|---|---|---|
| Etsy | Listings at 5-image status | 21 of 21 | 18 of 21 | Etsy Shop Manager > Listings |
| Etsy | SEEDWARDEN15 coupon active | Yes | Yes | Etsy > Marketing > Coupons |
| Etsy | Organic views (10am-12pm pre-email window) | Any | — | Shop Manager > Stats > Today |
| Kit | Broadcast delivery rate | >90% | >80% | Kit > Broadcasts > Stats |
| Kit | Broadcast bounce rate | <2% | <5% | Kit > Broadcasts > Stats |
| Kit | Broadcast open rate (6 hrs post-send) | >35% | >20% | Kit > Broadcasts > Stats |
| Kit | Broadcast click rate (6 hrs post-send) | >8% | >3% | Kit > Broadcasts > Stats |
| Kit | New subscribers (launch day) | >5 | >1 | Kit > Subscribers |
| Instagram | Impressions (Day 1) | >50 | >20 | Instagram Insights |
| TikTok | Views (Day 1) | >50 | >20 | TikTok Analytics |
| Pinterest | Impressions (by Day 2) | >30 | >10 | Pinterest Analytics |

### June 6 (Day 7 — Week 1 Review)

| Channel | Metric | Target | If Below Target |
|---|---|---|---|
| Kit | Total subscribers | 50+ | Review landing page conversion rate; test alternative CTA wording in bio |
| Kit | Welcome email open rate (Email 1) | 60%+ | Check spam placement; verify SPF/DKIM still active |
| Kit | Email 3 open rate | 40%+ | Weak Email 3 open rate forecasts low Email 5 redemption; consider revising Email 3 subject line |
| Kit | Subscribers with cohort tags | 20%+ of list | Click-through rate on Emails 3-4 is low; make links more prominent |
| Etsy | Shop views (7-day) | 200+ | Total views from launch broadcast + social + organic |
| Etsy | New orders (launch week) | 2+ | Even one order = product/messaging validation |
| Etsy | Listing conversion rate | 1-3% | Below 1%: review top-traffic listing for title/tag optimizations |
| Instagram | Followers | 150+ | Below 100: review Reel completion rate (below 30% = re-hook first 3 seconds) |
| Pinterest | Monthly views | 2,000+ | Below 1,000: increase to 4 pins/day for Week 2 |
| TikTok | Followers | 100+ | Below 50: confirm video uploaded natively (not cross-posted link) |

---

## Part 5: Decision Gates

### Gate 1 — May 14 (End of Day)

**Question**: Is the May 10-11 shoot complete with 30+ usable RAW files?

- YES: Proceed on May 30 path. All 25-day calendar above is active.
- NO: Photo shoot moves to May 17-18. Activate June 6 contingency path (june-6-contingency-path.md). Zone card and Kit tracks proceed unchanged.

---

### Gate 2 — May 23 (After Kit End-to-End Test)

**Question**: Did all 3 end-to-end tests pass (Zone 5, Zone 7, Email 3 behavioral tag)?

- YES: Publish Kit automation. Begin organic subscriber collection.
- NO: Do not publish automation. Diagnose failure (see TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md Step 6 troubleshooting). Do not add Kit landing page URL to social bios until test passes.

---

### Gate 3 — May 30 (8:00am QA)

**Question**: Are all of the following true? (1) All 21 Etsy listings "Active" with 5 images. (2) Kit broadcast status "Scheduled" for 12pm. (3) Buffer shows all 3 platforms "Connected" with no errors. (4) All 8 zone card download URLs deliver PDF in incognito.

- ALL YES: Launch proceeds as scheduled.
- ANY NO: Fix in the 8am-10am window. All documented failure modes have fixes under 15 minutes. None requires postponing launch.

---

### Gate 4 — June 6 (Week 1 Review)

**Question**: Which products are performing and which zones have the most subscribers?

**Decision output**:
- Top 2 products by Etsy views → feature in Week 2 social (Instagram Reel spotlights, Pinterest product pins)
- Top cohort tag by subscriber count → lead Week 2 newsletter content with that topic
- If Email 5 coupon redemptions are 0 out of 5+ Email 5 recipients: email coupon may not be reaching the inbox; review spam placement
- If total week-1 orders are 0: do not panic — Phase 2 is an organic-first strategy; recheck Etsy SEO on 3 highest-traffic listings (title first words, tags using 13 of 13 allowed)

---

*Generated: 2026-05-06. Primary references: TRACK_B_FINAL_EXECUTION_GUIDE.md, phase-2-day-by-day-execution.md, may-30-launch-sequence.md, june-6-contingency-path.md, phase-2-tool-integration-map.md. This document integrates all prior execution planning into a single day-level calendar. Other documents remain authoritative for their specific content.*
