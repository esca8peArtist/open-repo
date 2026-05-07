---
title: "May 30 Phase 2 Launch Readiness Audit"
date: 2026-05-07
session: exploration-queue-item-32
status: decision-ready
scope: Full dependency map, critical path, go/no-go framework, contingency scenarios, user actions, day-by-day checklist
deadline: 2026-05-30
hard-gate: 2026-05-10
---

# May 30 Phase 2 Launch Readiness Audit

**Prepared**: May 7, 2026
**Critical deadline**: May 30, 2026 (23 days)
**Hard gate decision**: May 10, 2026 (3 days)
**Infrastructure status**: Track B Phase 2 100% complete. All strategy, copy, specs, and content written. Waiting on user account creation.

---

## Section 1: All May 30 Dependencies Mapped

Every item that must be complete before a May 30 launch is listed below. Nothing is missing from this list. Surprises at launch time mean something here was ignored.

### Dependency Block 1: Account Creation (Must complete May 5-7)

These are the foundation. Every other track depends on them.

| Dependency | Action Required | Time Estimate | Blocking What |
|---|---|---|---|
| Instagram Business account | Create at instagram.com, switch to Business, upload logo, add bio | 20 min | Day 1 Reel upload, all scheduling, bio link publication |
| TikTok Business account | Download app, create account, switch to Business, upload logo, add bio | 15 min | Day 1 Reel upload, TikTok scheduling |
| Pinterest Business account | Create at pinterest.com, convert to Business, upload logo, add bio | 15 min | Pin scheduling, Pinterest batch upload |
| Kit (kit.co) account | Create account at kit.co, set sender name "Seedwarden", configure timezone | 10 min | Landing page, all email automation |
| Kit landing page | Build single-column page, 3 fields (name/email/zone), publish | 30-45 min | Bio links, Kit automation, zone card delivery |
| Landing page URL added to all three bios | Add the live Kit URL to Instagram, TikTok, Pinterest bio links | 10 min | Email list building begins |

**Total time: 100-115 minutes in one sitting.**

As of May 7, all of these items are listed as NOT STARTED or BLOCKED in TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md. This block is 3 days overdue from the May 5-6 target. This is the most urgent item in the entire launch plan.

### Dependency Block 2: Canva Brand Kit (Must complete May 5-8)

| Dependency | Action Required | Time Estimate | Blocking What |
|---|---|---|---|
| Brand Kit creation in Canva | Log in to canva.com, create Brand Kit "Seedwarden", add 10 colors, add 3 fonts, upload logo | 30 min | All zone card builds, Pinterest pin production, Instagram carousel builds |
| Zone 5 master zone card | Build master template in Canva from scratch, full content from CANVA_ZONE_CARD_BATCH_WORKFLOW.md | 150-180 min | All other 7 zone cards (they clone from this one) |
| Zone 6 card | Clone Zone 5, update zone-specific content | 30 min | Complete 8-card set |
| Zones 3 and 4 | Clone Zone 5, change band color to #3D6B8A Cool, update content | 75 min combined | Complete 8-card set |
| Zones 7 and 8 | Clone Zone 5, change band color to #C9943A Warm, update content | 75 min combined | Complete 8-card set |
| Zones 9 and 10 | Clone Zone 5, change band color to #A0522D Hot, update content | 75 min combined | Complete 8-card set |
| Zone card PDF review (all 8) | Visual check of all 8 cards for placeholder text, band color accuracy, frost dates | 30 min | Kit upload, Google Drive links |

**Total: 7.5-9 hours of Canva work across May 8-17.**

### Dependency Block 3: Plant Sourcing and Shoot Prep (Hard gate: May 9)

| Dependency | Action Required | Time Estimate | Blocking What |
|---|---|---|---|
| Germination tray started | Basil or lettuce in any tray, moistened, covered, warmest spot in home | 15 min (window closed May 5) | Seedling sprout props for Cluster A shoot |
| Props sourcing run | Garden center, grocery store, optional craft store | 1-2 hours travel | May 10-11 shoot cannot begin without props |
| Print run | 20-25 pages of product PDFs, black and white, home printer | 30 min | Physical props showing in flat-lay shots |
| Kraft seed envelopes | Order from Amazon by May 7 for 2-day delivery | 10 min online | Seed-adjacent products in Cluster A shoot |
| All props assembled and verified | Cross-check against SHOOT_PROPS_CHECKLIST.md before shoot morning | 20 min | Smooth shoot execution |

**Germination tray note**: The last viable start date listed in TRACK_B_FINAL_EXECUTION_GUIDE.md was May 5. As of May 7, a 9-10-day-old sprout started today would not be ready until May 16-17, which is after the May 10-11 shoot. If the tray has not been started, the contingency is to use grocery-store bean sprout trays as props or to move two Cluster A products (Seed Saving Manual, Zone Calendar) into the stock compositing workflow.

### Dependency Block 4: May 10-11 Photo Shoot (Primary gate: drives May 30 vs June 6)

| Dependency | Action Required | Time Estimate | Blocking What |
|---|---|---|---|
| Cluster A shoot (flat-lay, seeds/garden) | Saturday May 10, 9am-1:30pm, 16 shots on wood surface with window light | 4.5 hours | 9 seed/garden product listing images |
| Cluster B shoot (urban/container) | Saturday May 10, 3pm-5pm, 8 shots on window sill or balcony | 2 hours | 4 urban/container product listing images |
| Cluster C shoot (kitchen/preservation) | Sunday May 11, 9am-11am, 6 shots on kitchen counter | 2 hours | 3 food preservation product listing images |
| Image culling | May 12, select 30 best from 80-100 raw captures | 2 hours | Editing phase cannot begin |
| Batch editing in Lightroom Mobile or Snapseed | May 13-14, 30 selects processed to consistent profile | 3-4 hours | Etsy-ready exports |
| Export 30 final JPEGs at 2400x2400px | May 14, saved to marketing/lifestyle-photos/etsy-ready/ | 1 hour | Etsy uploads, social content for launch week |

### Dependency Block 5: Cluster D+E Stock Compositing (May 15)

| Dependency | Action Required | Time Estimate | Blocking What |
|---|---|---|---|
| Clusters D+E compositing in Canva | Overlay mockup images onto staged stock background images, 10 composites (5 products x 2 slots) | 3-4 hours | 5 products with Etsy listing images live by May 15 |
| Upload composited images to Etsy (Clusters D+E) | Add slot 4 and slot 5 images to 5 Etsy listings | 30 min | Earliest possible Etsy listing improvement |

Stock images for Clusters D and E are already staged in `assets/stock-raw/`. This block does not depend on the photo shoot.

### Dependency Block 6: Zone Card PDF Upload and Kit Automation (May 17-22)

| Dependency | Action Required | Time Estimate | Blocking What |
|---|---|---|---|
| Upload all 8 zone card PDFs to Google Drive | Share each PDF with "anyone with the link can view", copy download URLs | 30 min | Email 1 cannot link to zone cards |
| Record all 8 Google Drive links | Paste links into TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md table | 10 min | Kit email build reference |
| Create all 15 Kit tags | Zone tags (8) and interest cohort tags (7) | 15 min | Automation cannot route subscribers |
| Build Email 1 (8 zone variants) | One email per zone, zone-specific PDF link, subject line template | 60-90 min | Zone card delivery to subscribers |
| Build Emails 2-5 | Full copy already written in marketing/email-and-launch-plan.md | 60-90 min | Welcome sequence incomplete |
| Wire zone routing automation in Kit | Trigger: form completion. Step 1: apply zone tag. Step 2: send zone-matched Email 1 | 30 min | Automation live |
| End-to-end test: Zone 5 (incognito) | Sign up from incognito window, confirm Email 1 arrives, confirm PDF download works | 15 min | Cannot go live until test passes |
| End-to-end test: Zone 7 (incognito) | Repeat for Zone 7 | 10 min | Cannot go live until test passes |

### Dependency Block 7: Social Scheduling and Launch Week Preparation (May 22-29)

| Dependency | Action Required | Time Estimate | Blocking What |
|---|---|---|---|
| Etsy lifestyle image uploads (Clusters A, B, C) | Upload edited JPEGs to Etsy slots 4 and 5 for 12 products | 1 hour | Etsy listings compete with lifestyle images |
| Buffer or Later account setup | Connect Instagram, TikTok, Pinterest accounts | 30 min | Scheduled posts cannot be loaded |
| Load 60-day calendar into scheduler | Copy captions from phase-2-social-content-calendar-60day.md, attach images, set times | 3-4 hours | Launch-day posts automated |
| Batch-produce 15+ Pinterest pins | Build in Canva using lifestyle images and pin template specs | 2-3 hours | Pinterest launch content volume |
| May 29 test email send | Send test to secondary address, confirm Kit automation still live | 10 min | Launch-day confidence |
| May 29 scheduled post review | Confirm all scheduled posts show correct captions and times | 20 min | No errors at launch |

### Dependency Block 8: Launch Day Execution (May 30)

| Time | Action | Notes |
|---|---|---|
| 10:00am | Upload any remaining Etsy lifestyle images | Only if not completed May 22-25 |
| 12:00pm | Send Kit launch broadcast to full subscriber list | Requires live list with subscribers |
| 2:00pm | Instagram launch post | Pre-scheduled in Buffer/Later or manual upload |
| 3:00pm | TikTok launch post | Manual native upload recommended |
| 4:00pm | Pinterest launch pins | Trigger scheduler or post manually |
| End of day | Log all upload dates in WORKLOG.md | Starts conversion measurement window |

---

## Section 2: Critical Path Analysis

The critical path is the longest sequence of dependent tasks. Any delay on the critical path delays May 30. Tasks off the critical path have "slack" — they can slip without affecting the launch date.

### The Critical Path (Tasks That Determine May 30 vs June 6)

```
[Social accounts created] → [Kit landing page live] → [Bio links added]
        ↓
[Brand Kit set up in Canva]
        ↓
[Zone 5 master card built] → [Zones 6, 3, 4, 7, 8, 9, 10 built] → [All 8 PDFs exported]
        ↓
[Zone PDFs uploaded to Google Drive] → [Kit Email 1 variants built] → [Emails 2-5 built]
        ↓
[Kit automation wired] → [End-to-end test passes]
        ↓
[May 10-11 photo shoot] → [May 12 image culling] → [May 13-14 batch editing]
        ↓
[Etsy lifestyle images exported] → [Etsy slots 4-5 updated for Clusters A, B, C]
        ↓
[Launch-week social posts scheduled in Buffer/Later]
        ↓
**MAY 30 LAUNCH**
```

### Which Tasks Gate Others (Dependency Locks)

**Account creation is a total lock.** Nothing else is live-testable until social accounts exist and the Kit landing page is published. The Kit landing page URL must be in the bio before any post or reel drives traffic. Without the bio link, every piece of social content is a dead end.

**The Zone 5 master card gates all other 7 cards.** Zones 6, 3, 4, 7, 8, 9, 10 all clone from Zone 5. Building Zone 5 first (150-180 min) unlocks 6.5-7 hours of cloning work. Attempting to build any other zone first is wasted time.

**Zone card PDFs gate Kit Email 1.** Kit Email 1 contains the zone-specific PDF download button. Until PDFs exist in Google Drive with shareable links, Email 1 cannot be completed. This means the Kit automation cannot be tested or finalized until PDFs are built.

**The May 10-11 shoot gates the lifestyle-photo-dependent portion of launch.** 12 products (Clusters A, B, C) need real lifestyle photography. If the shoot slips to May 17-18, the editing and export timeline compresses, Etsy upload moves to May 20-22, and launch-week social content using lifestyle images becomes a shorter window. The full impact is that May 30 becomes a soft launch with lifestyle images; the hard launch with all Etsy slots full slides to June 6.

**Cluster D+E compositing does not depend on the shoot.** Stock images are already staged. This block can run May 15 regardless of what happens to the shoot.

### Slack Time by Task

| Task | Latest Possible Start | Slack from Today (May 7) |
|---|---|---|
| Social accounts + Kit account | May 7 (TODAY — already 2 days late) | Zero. Every day lost here compresses everything downstream. |
| Brand Kit setup | May 8 | 1 day |
| Germination tray / sprout contingency decision | May 7 | Zero — contingency must be decided today |
| Props sourcing run | May 9 | 2 days |
| Kraft envelope order | May 7 | Zero — need 2-day shipping to arrive by May 9 |
| Zone 5 master card build | May 8 | 1 day |
| Zones 6, 3, 4 build | May 10-11 (can do evenings of shoot days) | 3 days |
| Zones 7, 8, 9, 10 build | May 11-17 | Up to 10 days |
| Photo shoot (primary dates) | May 10-11 | Zero — next viable weekend only |
| Image culling | May 12 | 0 days (immediate after shoot) |
| Batch editing | May 13-14 | 1 day |
| Cluster D+E compositing | May 15-17 | 2 days |
| Zone card PDF export and Google Drive upload | May 17 | 10 days |
| Kit Email 1 build (all 8 variants) | May 17-19 | 10 days |
| Emails 2-5 build | May 19-22 | 12 days |
| Kit automation wiring | May 21-22 | 14 days |
| End-to-end Kit test | May 22 | 15 days |
| Etsy lifestyle uploads (Clusters A-C) | May 22-25 | 15 days |
| Buffer/Later scheduling | May 25-29 | 18 days |
| Pinterest pin batch production | May 25-29 | 18 days |

The most dangerous slack zone is the illusion that social accounts and Kit setup can be deferred a few more days. They cannot. Each day of delay on account creation compresses the zone card build window, which compresses Kit automation setup, which reduces the time for pre-launch testing.

---

## Section 3: May 10 Go/No-Go Framework

May 10 is a hard gate for plant sourcing orders (independent of Track B) and is the first day of the photo shoot. By end of day May 9, the following assessment determines whether May 30 is still the viable launch date.

### "Go" Criteria at May 10 — All Must Be True

1. **Social accounts live**: Instagram, TikTok, and Pinterest accounts exist with @seedwarden (or fallback handle), profile photos, and bio text. Account type: Business on all three.

2. **Kit landing page published**: The landing page at kit.co is live, accessible at a real URL, with three form fields (name, email, zone dropdown), and the CTA "Send My Zone Card" is visible. Page is not in draft mode.

3. **Bio links active**: The Kit landing page URL appears in all three social bios. Any person who finds the account can click through to the landing page.

4. **Brand Kit created in Canva**: The Seedwarden Brand Kit exists with all 10 colors and 3 fonts. The logo is uploaded. This can be confirmed by logging into Canva and opening Brand Hub.

5. **Zone 5 master card at least 50% built**: The most time-consuming Canva task must have started. Being 50% through the Zone 5 master template by May 10 is the minimum threshold to confirm the full 8-card set will be complete by May 17.

6. **Props sourcing complete**: All items on SHOOT_PROPS_CHECKLIST.md are in hand or a specific documented substitute has been identified. The shoot cannot begin May 10 morning with outstanding prop gaps.

### "Go With Flag" — Items That Can Slip to May 15 Without Killing May 30

These items are not required at May 10 but must be resolved by May 15:

- Zone 5 master card fully complete (50% is enough at May 10, 100% required by May 13)
- Day 1 Reel filmed and uploaded (can be Day 4 or Day 5 instead, with some early momentum loss)
- Day 3 Carousel built in Canva (can slide to May 12-13)
- First 6 Pinterest pins built (can slide to May 12-14)
- Kraft envelopes ordered (if late, a paper envelope substitute works for the shoot)

### "No-Go" Triggers at May 10 — Any One of These Forces a Reassessment

1. Social accounts still do not exist by May 10 start.
2. Kit landing page not published by May 10 start.
3. Brand Kit not created in Canva by May 10 start.
4. Props sourcing not done by May 9 evening.
5. Zone 5 master card build not started.

If any "No-Go" trigger is true, the choice is not between May 30 and failure — it is between May 30 and June 6. June 6 is a fully documented contingency path. The email automation and Cluster D+E images can still go live May 30; only the lifestyle-photo-dependent content moves to June 6.

---

## Section 4: Contingency Scenarios

### Scenario A: Photo Shoot Slips to May 17-18

**What causes this**: Weather is unusable for window light, illness, or unexpected schedule conflict May 10-11.

**Impact on May 30 launch**:
- Editing window compresses from 3 days (May 12-14) to 2 days (May 19-20)
- Etsy lifestyle image uploads move from May 15-20 to May 20-23
- Launch-week social content using lifestyle images: available but with less curation time
- Kit automation, zone card builds, and Cluster D+E compositing are all unaffected — those proceed on schedule

**What stays on May 30**:
- Kit landing page live and collecting emails
- Zone card delivery automation live and tested
- Cluster D+E Etsy images uploaded
- Instagram, TikTok, Pinterest accounts live with content
- May 30 launch broadcast via Kit email

**What may be incomplete at May 30**:
- 12 Etsy product listings (Clusters A, B, C) may have only 3 images instead of 5 at launch
- Launch-week social posts may use mockup images instead of lifestyle photos in some slots

**Decision rule**: If shoot must move to May 17-18, the May 30 launch still happens. Etsy slots 4-5 for Clusters A, B, C fill by June 3-6. This is a soft launch that becomes a full launch within one week.

**Do not delay zone card builds or Kit automation** while waiting on shoot rescheduling — those work streams are fully independent.

### Scenario B: One Social Platform Will Not Verify Business Account

**What causes this**: Platform ID verification delays, restricted account review, or availability conflict with a handle.

**Impact on May 30 launch**:
- Each platform is independently useful. If only two of three accounts are live, launch proceeds.
- Priority order: Instagram first, Pinterest second, TikTok third.
- Instagram has the highest ROI for Seedwarden's content type (carousels + Reels reach growers). Pinterest has the highest passive reach (pins live for months). TikTok can launch 1-2 weeks after May 30 without affecting May launch metrics.

**Handle fallback protocol**:
- Primary: @seedwarden
- Fallback order: @seedwarden.co, @seedwarden.seeds, @seedwarden_guides
- Use the same handle across all platforms regardless of which fallback is chosen.
- Record actual handles in WORKLOG.md on the day accounts are created.

**If TikTok verification delays past May 22**: Skip TikTok for May 30. Launch Instagram and Pinterest on schedule. Add TikTok in the first week of June. The 60-day content calendar still applies when TikTok launches — just start from the Day 1 content regardless of calendar date.

### Scenario C: Canva Brand Kit Setup Delays

**What causes this**: Canva account access issues, the Brand Hub feature not appearing in the free tier, or font availability changes.

**Impact**:
- If Brand Hub is unavailable on the current Canva tier, all colors and fonts can be set manually per-design. This adds 10-15 minutes per zone card build but does not block the build.
- If Playfair Display is missing from Canva's library: substitute Libre Baskerville (same visual role, freely available in Canva).
- If Lato is missing: substitute Source Sans 3 (confirmed identical in use, documented in TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md).
- If Cormorant Garamond is missing: substitute EB Garamond (same serif character).

**No scenario makes zone card production impossible.** Brand Kit is a time-saver, not a blocker. If setup takes longer than expected, begin Zone 5 with manually configured styles and migrate to Brand Kit when it is resolved.

### Scenario D: Kit Account Setup Delayed Past May 22

**What causes this**: Account verification holds, landing page builder UI changes, or unexpected platform restrictions.

**Short-term workaround (1-3 days)**:
- First subscribers can be manually welcomed with a direct Gmail send.
- Zone cards can be attached as email attachments to a manual send from wanka95@gmail.com.
- This is a documented workaround, not a long-term solution. Do not operate this workaround past 72 hours.

**Impact on May 30**:
- If Kit automation is fully live by May 25, the 5-day buffer before launch is adequate.
- If Kit is not live by May 25, launch-day email broadcast sends to an empty or very small list. May 30 becomes a social-only launch, with email coming online in the first week of June.
- Kit delay does not affect social scheduling, Etsy uploads, or zone card builds.

---

## Section 5: User Action Audit

All decisions and actions below require the user to log into consumer apps. The agent cannot perform any of these. Time estimates are from the reference documents and reflect completion in a single focused session.

| Action | When | Est. Time | Status | Blocks |
|---|---|---|---|---|
| Create Instagram Business account | May 7 (TODAY) | 20 min | NOT DONE | Everything social |
| Create TikTok Business account | May 7 (TODAY) | 15 min | NOT DONE | Everything social |
| Create Pinterest Business account | May 7 (TODAY) | 15 min | NOT DONE | Everything social |
| Create Kit account at kit.co | May 7 (TODAY) | 10 min | NOT DONE | Landing page, all automation |
| Build and publish Kit landing page | May 7 (TODAY) | 30-45 min | NOT DONE | Bio links, email capture |
| Add Kit landing page URL to all 3 bios | May 7 (TODAY, after above) | 10 min | NOT DONE | Email list building |
| Set up Canva Brand Kit (colors, fonts, logo) | May 7-8 | 30 min | NOT DONE | All Canva design work |
| Order Kraft seed envelopes from Amazon | May 7 (TODAY) | 10 min | UNKNOWN | Shoot props |
| Props sourcing run | May 7-9 | 1-2 hours | NOT DONE | May 10 shoot |
| Print run (20-25 pages) | May 8-9 | 30 min | NOT DONE | Shoot physical props |
| Decide germination tray contingency | May 7 (TODAY) | 5 min | DECISION NEEDED | Shoot Cluster A props |
| Film Day 1 Reel (origin story, 30-45 sec) | May 7-8 | 45-60 min filming | NOT DONE | First social impression |
| Upload Day 1 Reel to Instagram and TikTok | May 7-8 | 15 min | NOT DONE | Social momentum |
| Build Zone 5 master card in Canva | May 8-9 | 150-180 min | NOT DONE | All 7 other zone cards |
| Build Zone 6 card (clone from Zone 5) | May 9-10 | 30 min | NOT DONE | 8-card set |
| Build Day 3 Carousel in Canva (5 slides) | May 8-9 | 45-60 min | NOT DONE | Day 3 Instagram post |
| Build first 6 Pinterest pins | May 8-9 | 60-90 min | NOT DONE | Pinterest Week 1 schedule |
| Photo shoot — Cluster A (Saturday morning) | May 10, 9am-1:30pm | 4.5 hours | UPCOMING | 9 seed/garden products |
| Photo shoot — Cluster B (Saturday afternoon) | May 10, 3pm-5pm | 2 hours | UPCOMING | 4 urban products |
| Photo shoot — Cluster C (Sunday morning) | May 11, 9am-11am | 2 hours | UPCOMING | 3 preservation products |
| Image culling (80-100 captures → 30 selects) | May 12 | 2 hours | UPCOMING | Editing phase |
| Batch edit 30 selects in Lightroom Mobile or Snapseed | May 13-14 | 3-4 hours | UPCOMING | Export-ready images |
| Export 30 final JPEGs at 2400x2400px | May 14 | 1 hour | UPCOMING | Etsy uploads, social content |
| Cluster D+E Canva compositing (10 images) | May 15 | 3-4 hours | UPCOMING | 5 Etsy products with lifestyle images |
| Upload Cluster D+E images to Etsy slots 4-5 | May 15 | 30 min | UPCOMING | Earliest Etsy improvement |
| Build Zones 3, 4, 7, 8, 9, 10 cards | May 10-17 (can batch across evenings) | 5-6 hours total | NOT DONE | Kit Email 1 variants |
| Zone card PDF review (all 8) | May 15-17 | 30 min | NOT DONE | Kit upload |
| Upload all 8 zone PDFs to Google Drive | May 17 | 30 min | UPCOMING | Kit Email 1 links |
| Create all 15 Kit tags | May 17 | 15 min | NOT DONE | Kit automation |
| Build Kit Email 1 (all 8 zone variants) | May 17-19 | 60-90 min | NOT DONE | Zone card delivery |
| Build Kit Emails 2-5 | May 19-21 | 60-90 min | NOT DONE | Welcome sequence |
| Wire Kit zone routing automation | May 21-22 | 30 min | NOT DONE | Automation live |
| End-to-end test: Zone 5 (incognito window) | May 22 | 15 min | NOT DONE | Launch go/no-go |
| End-to-end test: Zone 7 (incognito window) | May 22 | 10 min | NOT DONE | Launch go/no-go |
| Upload lifestyle images to Etsy (Clusters A, B, C) | May 22-25 | 1 hour | UPCOMING | Full Etsy product coverage |
| Set up Buffer or Later, connect 3 platforms | May 25 | 30 min | NOT DONE | Post scheduling |
| Load 60-day calendar into scheduler | May 25-29 | 3-4 hours | NOT DONE | Automated launch posts |
| Batch-produce 15+ Pinterest pins | May 25-29 | 2-3 hours | NOT DONE | Pinterest launch volume |
| May 29 test email send | May 29 | 10 min | UPCOMING | Automation confidence check |
| May 29 scheduled post review | May 29 | 20 min | UPCOMING | No errors at launch |
| May 30 launch day execution | May 30 | 2 hours monitoring | UPCOMING | Launch |

**Total user-hours required (May 7-30)**: Approximately 40-50 hours across 23 days, or 1.75-2.2 hours per day on average. The first 5 days (May 7-11) are the most intensive: approximately 18-22 hours including shoot day.

---

## Section 6: May 7-30 Day-by-Day Execution Checklist

### May 7 (TODAY — 3 items are zero-slack)

- [ ] Create Instagram Business account (20 min)
- [ ] Create TikTok Business account (15 min)
- [ ] Create Pinterest Business account (15 min)
- [ ] Create Kit account at kit.co (10 min)
- [ ] Build and publish Kit landing page — 3 fields, CTA "Send My Zone Card" (30-45 min)
- [ ] Add Kit landing page URL to all 3 social bios (10 min)
- [ ] Order Kraft seed envelopes on Amazon (10 min, for May 9 arrival)
- [ ] Germination tray decision: if not started by May 5, decide now whether to use grocery bean sprouts or move Cluster A products to stock compositing

### May 8

- [ ] Set up Canva Brand Kit: 10 colors, 3 fonts, upload logo (30 min)
- [ ] Begin Zone 5 master zone card in Canva — aim to complete 50% (75-90 min session)
- [ ] Film Day 1 Reel (origin story, 30-45 seconds) — review script in phase-2-social-content-calendar-60day.md Day 1

### May 9

- [ ] Complete Zone 5 master zone card in Canva (remaining 75-90 min)
- [ ] Build Zone 6 card (clone from Zone 5, 30 min)
- [ ] Upload Day 1 Reel to Instagram (as Reel, not video)
- [ ] Upload Day 1 Reel to TikTok (native upload, not cross-post from Instagram)
- [ ] Props sourcing run — garden center, grocery store, optional craft store (1-2 hours)
- [ ] Print run: 20-25 pages from product PDFs (30 min)

### May 10 (SHOOT DAY 1)

- [ ] Confirm all Cluster A props are assembled (quick morning check against SHOOT_PROPS_CHECKLIST.md)
- [ ] 9:00am-1:30pm: Cluster A shoot — 16 shots, wood surface, window light
- [ ] 3:00pm-5:00pm: Cluster B shoot — 8 shots, window sill or balcony
- [ ] Evening: Build Zone 3 card in Canva if energy allows (40 min clone session)

### May 11 (SHOOT DAY 2)

- [ ] 9:00am-11:00am: Cluster C shoot — 6 shots, kitchen counter
- [ ] Afternoon: Build Zone 4 card in Canva (35 min clone from Zone 3)
- [ ] Afternoon: Build Day 3 Carousel in Canva — 5 slides (45-60 min)
- [ ] Post Day 3 Carousel to Instagram

### May 12

- [ ] Image culling: review all captures, select 30 best (2 hours)
- [ ] Build Zone 7 card in Canva (40 min clone from Zone 5, warm band color)

### May 13

- [ ] Batch edit 30 selected photos — session 1 (Cluster A, 9 products, 18 images) — Lightroom Mobile or Snapseed (2 hours)
- [ ] Build Zone 8 card in Canva (35 min clone from Zone 7)
- [ ] Build first 6 Pinterest pins in Canva (60-90 min using pin-template-specs.md)

### May 14

- [ ] Batch edit 30 selected photos — session 2 (Clusters B and C, 7 products, 12 images) (2 hours)
- [ ] Export all 30 final JPEGs at 2400x2400px to marketing/lifestyle-photos/etsy-ready/
- [ ] Schedule 6 Pinterest pins in Pinterest native scheduler (Tue-Fri, 8pm-11pm)

### May 15

- [ ] Cluster D+E Canva compositing — 10 images (3-4 hours)
- [ ] Upload Cluster D+E composited images to Etsy listing slots 4-5 (30 min)
- [ ] Begin Zone 9 card in Canva (40 min clone from Zone 5, hot band color)

### May 16

- [ ] Complete Zone 9 card if not finished May 15
- [ ] Build Zone 10 card (35 min clone from Zone 9)
- [ ] Full 8-card visual review: check each card for placeholder text, frost date accuracy, band color match

### May 17

- [ ] Export all 8 zone card PDFs from Canva (PDF Print, Flatten PDF checked)
- [ ] Upload all 8 zone card PDFs to Google Drive
- [ ] Set each Google Drive file to "Anyone with the link can view"
- [ ] Copy download-format links (change /view?usp=sharing to /uc?export=download&id=[FILE_ID])
- [ ] Record all 8 links in TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md zone card table

### May 18-19

- [ ] Create all 15 Kit tags (8 zone tags + 7 interest cohort tags)
- [ ] Build Kit Email 1, Zone 5 variant — test delivery first (30 min)
- [ ] Build Kit Email 1, Zone 6 variant (15 min, clone Zone 5 variant and substitute zone)
- [ ] Build Kit Email 1, Zones 3 and 4 variants
- [ ] Build Kit Email 1, Zones 7 and 8 variants

### May 20-21

- [ ] Build Kit Email 1, Zones 9 and 10 variants — all 8 Email 1 drafts complete
- [ ] Build Kit Email 2 (Heirloom Seed Philosophy — copy from marketing/email-and-launch-plan.md)
- [ ] Build Kit Email 3 (Seed Saving Story — add click-tracked link with seed-saver tag)
- [ ] Build Kit Email 4 (Catalog Introduction — 3 tracked links with city-grower, seed-saver, preservationist tags)
- [ ] Build Kit Email 5 (First Offer — include SEEDWARDEN15 coupon code)
- [ ] Create Etsy discount code SEEDWARDEN15 (15% off) in Etsy Shop Manager

### May 22

- [ ] Wire zone routing automation in Kit: form completion → apply zone tag → send matched Email 1
- [ ] End-to-end test, Zone 5: incognito window, sign up, confirm email delivery, confirm PDF download
- [ ] End-to-end test, Zone 7: repeat
- [ ] Behavioral tag test: manually send Email 3 to test email, click tracked link, confirm seed-saver tag applied
- [ ] Upload remaining lifestyle images to Etsy slots 4-5 (Cluster C first, then B, then A)

### May 23-24

- [ ] Continue Etsy lifestyle image uploads for all remaining Clusters A and B products
- [ ] Build Buffer or Later account, connect Instagram and Pinterest
- [ ] Select top 10 lifestyle images for launch-week social use

### May 25-28

- [ ] Load all scheduled posts into Buffer or Later: May 26-30 content (captions from 60-day calendar)
- [ ] Batch-produce 15+ Pinterest pins using lifestyle images and pin-template-specs.md
- [ ] Upload Pinterest pins to native scheduler (Tue-Fri, 8pm-11pm)

### May 29

- [ ] Send test email from incognito window — confirm Kit automation still live and Email 1 delivers correctly
- [ ] Review all scheduled social posts in Buffer/Later — confirm captions, images, and times are correct
- [ ] Confirm Kit landing page is still live and accessible
- [ ] Note any Etsy listing slots still missing images — these upload first thing May 30

### May 30 — Launch Day

- [ ] 10:00am: Upload any remaining Etsy lifestyle images
- [ ] 12:00pm: Send Kit broadcast email to full subscriber list
- [ ] 2:00pm: Instagram launch post live (manual or via scheduler)
- [ ] 3:00pm: TikTok launch post — upload natively
- [ ] 4:00pm: Pinterest launch pins — trigger scheduler or post manually
- [ ] End of day: Log all upload dates in WORKLOG.md

---

*Prepared: May 7, 2026. Session: exploration-queue-item-32. Reference documents: TRACK_B_FINAL_EXECUTION_GUIDE.md, TRACK_B_SOCIAL_ACCOUNT_CHECKLIST.md, TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md, TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md. All time estimates sourced from or consistent with those documents.*
