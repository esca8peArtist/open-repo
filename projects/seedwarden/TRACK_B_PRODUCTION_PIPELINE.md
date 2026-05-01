---
title: "Phase 2 Track B — Production Pipeline and Publication Sequence"
prepared: 2026-05-01
session: 694
status: active — no blockers — proceed immediately
scope: Social media, lifestyle photography, email funnel, zone card lead magnet
references:
  - TRACK_B_LAUNCH_STATUS.md
  - TRACK_B_READINESS_CHECKLIST.md
  - TRACK_B_EXECUTION_KICKOFF.md
  - MAY_CONTENT_EXECUTION_PLAN.md
  - phase-2-execution-timeline.md
  - concurrent-track-execution-plan.md
---

# Phase 2 Track B — Production Pipeline and Publication Sequence

**Summary**: Track B has no remaining user-action blockers that require external dependencies (no Etsy verification, no payment holds, no platform approval). The two gates to begin — social account creation (30-60 min) and Canva Brand Kit setup (30 min) — are immediately executable. All production specifications, scripts, templates, and content copy are confirmed production-ready.

**Current date**: May 1, 2026. The Phase 2 target launch window is May 30, 2026. Twenty-nine calendar days remain.

---

## Section 1: Track B Product List — Confirmed Scope

Track B covers four product workstreams that run in parallel. All four are required for the May 30 Phase 2 live launch.

### Workstream 1: Social Media Launch

**Products**: Instagram, TikTok, Pinterest accounts with active content

**Publication output**:
- TikTok and Instagram Reels: 5 videos in May (4-5/week cadence from June onward)
- Instagram Carousels: 2 per week
- Pinterest: 6 pins in May (batch-scheduled); 10-15 per week from June
- Instagram Stories: daily, informal, behind-the-scenes

**Content specifications**: Production-ready. Full copy, hooks, scripts, hashtags, and CTAs for all May content are in `MAY_CONTENT_EXECUTION_PLAN.md`. The 60-day calendar is in `phase-2-social-content-calendar-60day.md`. The 3-month calendar is in `marketing/social-media-calendar-may-july-2026.md`.

**Asset status**:
- All 21 product mockup images exist at 2400x2400px in `/projects/seedwarden/mockups/`
- 5 pin templates fully specified in `pin-template-specs.md`
- Canva implementation guide in `CANVA_EXECUTION_PLAYBOOK.md`
- Brand kit hex codes and fonts in `TRACK_B_LAUNCH_STATUS.md` Condition 2

**Lifestyle photo dependency**: Not required for Weeks 1-2. Mockup images are sufficient for all May content. Lifestyle photos upgrade conversion quality from Week 3 onward once Etsy listing data signals which products need them.

---

### Workstream 2: Lifestyle Photography (Slots 4-5 for 21 Etsy Listings)

**Products**: 21 Etsy listings each currently at 3-image status; Phase 2 adds slots 4 and 5

**Cluster assignments and method**:

| Cluster | Products | Method | Images Staged |
|---------|----------|--------|--------------|
| D — Survival / Outdoors (4 products) | Survival Garden, Hunting Manual, Livestock Manual, Meat/Fish Preservation | Stock (Pexels) — compositing pending | 8 of 8 staged |
| E — Native Plants (1 product) | Native Plants Regional Guide | Wikimedia CC BY-SA (slot 4) + Pexels (slot 5) | 2 of 2 staged |
| C — Food Preservation (3 products) | Harvest Preservation, Fermented Harvest, Grow Your Own Hot Sauce | Physical shoot (kitchen) | 0 of 6 — pending shoot |
| A — Seeds / Garden (9 products) | Seed Saving Manual, Heirloom Guide, Anti-Catalog, Companion Chart, Zone Calendar, Food Sovereignty, Apartment Seed Kit, Urban Planner, Free Veg Guide | Physical shoot (window flat-lay) | 0 of 18 — pending shoot |
| B — Urban / Container (4 products) | Container Blueprint, Apartment Growing, Apartment Plant Catalog, Seed Swap Kit | Physical shoot (indoor potted plants) | 0 of 8 — pending shoot |

**Clusters D and E (10 images)**: Raw stock files staged in `assets/stock-raw/`. Awaiting compositing step in Canva. No new sourcing required.

**Clusters A, B, C (32 images)**: Physical photo shoot required. Props plan is in `CLUSTER_C_PROPS_ACQUISITION_PLAN.md`. Shoot schedule targets May 10-11. See `PHOTO_SHOOT_SCHEDULE_AND_PROPS.md` and `TRACK_B_READINESS_CHECKLIST.md` Section 1 for full equipment and location checklist.

**Critical path note for germination**: If the germination tray was not started April 30, start today (May 1). 5-7-day sprouts are needed for the Cluster A shoot. A May 1 start gives 9-day sprouts by May 10 — still within the photogenic window.

---

### Workstream 3: Zone Quick-Start Card Lead Magnet (8 PDFs)

**Products**: 8 zone-specific planting cards (Zones 3-10), delivered via Kit email automation

**Build specifications**: Complete. Zone content tables (frost dates, crops, storage tips, variety spotlights) are in `CANVA_ZONE_CARD_BATCH_WORKFLOW.md`. The step-by-step Canva build guide is in `CANVA_ZONE_CARD_DESIGN_GUIDE.md`. Build timeline is in `ZONE_CARD_PRODUCTION_TIMELINE.md`.

**Status of "This Month" content**: May 2026 task blocks are written for all 8 zones in `CANVA_ZONE_CARD_BATCH_WORKFLOW.md`. They are ready to paste into Canva at build time.

**Output path**: `assets/zone-cards/zone-[number]-quick-start-card.pdf`

**Kit delivery integration**: Full setup instructions including subscriber zone routing are in `PHASE_2_EMAIL_STRATEGY.md`. Kit free tier supports all required functionality (8 download URLs, zone-conditional delivery, welcome sequence).

---

### Workstream 4: Email Automation Funnel

**Products**: 3-email welcome sequence (Days 0, 5, 12), delivered via Kit to all Zone Card subscribers

**Email copy**: Production-ready. All 3 emails with subject lines, body copy, and Kit setup notes are in `MAY_CONTENT_EXECUTION_PLAN.md` Section "Email Sequences."

Email 1 (Zone Card delivery) requires 8 zone-specific variants — one per zone. Copy structure and Kit routing instructions are documented.

Email 2 (seed saving educational, Day 5) and Email 3 (companion planting, Day 12) each have a single version that sends to all subscribers.

**Platform**: Kit free tier (kit.co). The account must be created before Zone Card PDFs can be uploaded and before the sign-up form can go live.

---

## Section 2: Production-Readiness Audit

### Documents With Confirmed No TODOs

The following files have been reviewed and confirmed free of placeholder text, unfilled fields, and pending decisions:

| File | Purpose | Status |
|------|---------|--------|
| `MAY_CONTENT_EXECUTION_PLAN.md` | Day-level May execution plan; full post copy and email text | Production-ready |
| `phase-2-social-content-calendar-60day.md` | Day 1-60 post hooks, scripts, captions, hashtags | Production-ready |
| `CANVA_ZONE_CARD_BATCH_WORKFLOW.md` | Per-zone content tables + Canva session workflow | Production-ready (May 2026 content included) |
| `CANVA_ZONE_CARD_DESIGN_GUIDE.md` | Step-by-step Canva build reference | Production-ready |
| `PHASE_2_EMAIL_STRATEGY.md` | Kit platform setup, automation architecture | Production-ready |
| `TRACK_B_EXECUTION_KICKOFF.md` | Day-by-day 14-day action checklist | Production-ready |
| `PHOTO_SHOOT_SCHEDULE_AND_PROPS.md` | May 10-11 shoot schedule, props list, print list | Production-ready |
| `TRACK_B_READINESS_CHECKLIST.md` | Go/no-go gate for photo shoot and Canva build | Production-ready |
| `TRACK_B_LAUNCH_STATUS.md` | Five launch conditions with current status assessment | Production-ready |
| `pin-template-specs.md` | 5 Pinterest pin templates with full specifications | Production-ready |
| `CANVA_EXECUTION_PLAYBOOK.md` | Canva implementation guide for all template types | Production-ready |

### Two Remaining User Gates (No External Dependencies)

| Gate | Time Required | Unblocks |
|------|--------------|---------|
| Social account creation (Instagram, Pinterest, TikTok with handle `seedwarden`) | 30-60 minutes | All content scheduling; Day 1 Reel upload; bio link publication |
| Canva Brand Kit setup (6 hex colors, 3 fonts, logo upload) | 30 minutes | All Canva work: pin templates, zone cards, carousel slides |

Neither gate requires any external approval or platform verification. Both are user-operated in consumer apps.

---

## Section 3: Publication Sequence and Timeline

### Phase 1 — Immediate (May 1-7)

**Priority: Get the first social posts scheduled before any other Track B work.**

Day 1 (May 1):
- Create Instagram, Pinterest, TikTok accounts — handle `seedwarden` (or `seedwarden.co` / `seedwarden.seeds` if taken)
- Set up Canva Brand Kit with brand colors and fonts per `TRACK_B_LAUNCH_STATUS.md` Condition 2
- Create Kit (kit.co) free account; build Zone Card sign-up landing page
- Add Kit landing page link to all three social bios
- Confirm germination tray has been started (May 1 is the last low-risk start date for May 10 shoot)

Days 2-3 (May 2-3):
- Film and edit Day 1 Reel — origin story, 30-45 seconds, talking head or B-roll (script in `phase-2-social-content-calendar-60day.md` Day 1)
- Upload Day 1 Reel to Instagram as Reel; upload same video natively to TikTok — do not cross-post
- Record Day 1-2 Instagram Stories (behind-the-scenes, 5-7 Stories)

Days 3-4 (May 3-4):
- Build Day 3 Carousel in Canva (5 slides, product mockups, specs in `phase-2-social-content-calendar-60day.md` Day 3)
- Build first 6 Pinterest pins (Pin 1.3 from `MAY_CONTENT_EXECUTION_PLAN.md` + 5 Tier 1 product pins)
- Schedule all 6 Pinterest pins via Pinterest native scheduler (Tuesday-Friday, 8pm-11pm local time)
- Post Day 3 Carousel to Instagram

Days 5-7 (May 5-7):
- Begin props sourcing run using `TRACK_B_READINESS_CHECKLIST.md` Section 1B checklist
- Source print run: 1-2 pages per product (20-25 pages total) — submit to print shop by May 8 for 24-hour turnaround
- Build Canva Zone 5 master template following `CANVA_ZONE_CARD_DESIGN_GUIDE.md` Part 2-4 (90 min)
- Build Zone 6 card (clone + content swap, 30 min)

**Phase 1 output**: Social accounts live, Day 1 Reel published, first 6 Pinterest pins scheduled, Canva Brand Kit ready, Zone 5 and 6 cards built.

---

### Phase 2 — Photo Shoot Preparation and Production (May 7-14)

Days 7-9 (May 7-9):
- Complete all props sourcing; verify every item in `TRACK_B_READINESS_CHECKLIST.md` Section 1B
- Collect printed product pages from print shop
- Assemble shoot materials by cluster (boxed separately by cluster)
- Scout and confirm shooting location: window for Clusters A and B, kitchen counter for Cluster C
- Build Zone cards 3 and 4 in Canva (clone Zone 5, change zone band color + content, 45 min each)

May 10 (Saturday) — Shoot Day 1:
- 9:00am-1:30pm: Cluster A shoot — 8 products, 16 shots, wooden surface with window light
- 3:00pm-5:00pm: Cluster B shoot — 4 products, 8 shots, urban/window sill setting
- Do not edit during shoot day

May 11 (Sunday) — Shoot Day 2:
- 9:00am-11:00am: Cluster C shoot — 3 products, 6 shots, kitchen counter setting
- Build Zone cards 7 and 8 in Canva (same afternoon, after shoot, 45 min each)

**Phase 2 output**: 30 RAW images captured across all physical clusters; Zones 3, 4, 7, 8 built.

---

### Phase 3 — Processing, Zone Card Completion, and Scheduling (May 12-22)

May 12:
- Image culling: 80-100 RAW captures down to 30 selects
- Do not edit during culling pass — select only

May 13-14:
- Batch editing per `TRACK_B_READINESS_CHECKLIST.md` Section 1F photography consistency guide
- Export 30 final 2400x2400px JPEG images to `marketing/lifestyle-photos/etsy-ready/`
- Export 60 social variant crops (1:1 Etsy, 4:5 Instagram, 16:9 Pinterest) — skip variant crops if time is short; prioritize Etsy-ready files first

May 15:
- Begin Canva compositing: apply Cluster D/E staged stock images + product PDF overlay in Canva
- 10 composites (5 products x 2 slots); see `phase-2-production-checklist.json` W4-05 for technique
- Log all composited filenames in WORKLOG.md per the existing image sourcing table format

May 15-17:
- Build Zone cards 9 and 10 in Canva (45 min each)
- Full 8-card review (print test or PDF review of all 8 cards)
- Replace placeholder footer URLs `[ETSY-ZONE-CALENDAR-LINK]` and `seedwarden.com/zone` with live URLs if available; leave as placeholder if not yet live

May 17-22:
- Upload all 8 zone card PDFs to Kit file library
- Wire zone-conditional automation: subscriber zone dropdown field routes to correct PDF download
- Build welcome sequence in Kit (Email 1: 8 zone variants; Email 2: Day 5; Email 3: Day 12)
- Test end-to-end for Zone 5: sign up, receive Email 1 with Zone 5 PDF download, confirm delivery
- Test end-to-end for one other zone (Zone 7 recommended — largest population in Zone 7 belt)
- Publish Kit landing page URL to all social bios; update from "opening soon" if applicable

**Phase 3 output**: 30 lifestyle photos edited and staged, Cluster D/E composites complete, all 8 zone cards built and uploaded, email automation live and tested.

---

### Phase 4 — Social Content Scheduling and Launch Coordination (May 22-30)

May 20-25:
- Continue May content cadence: Week 3 posts (seed saving basics, see `MAY_CONTENT_EXECUTION_PLAN.md`)
- Begin selecting top 10 lifestyle images from 30 for launch-week social use
- Write captions for launch-week posts drawing from `phase-2-social-content-calendar-60day.md`

May 25-29:
- Schedule all launch-week social posts in Buffer/Later for May 30 + Days 31-33
- Post Week 4 social content per `MAY_CONTENT_EXECUTION_PLAN.md` (Zone Card re-promotion, apartment growing)
- Batch-produce 15+ Pinterest pins for Tier 1-2 products using lifestyle images
- Verify Kit email automation is live and uninterrupted (send test to a second email address)

May 30 — Phase 2 Live Launch:
- 10:00am: Upload all Etsy lifestyle images to slots 4-5 for available listings (Cluster D/E first; physical shoot products as edited)
- 12:00pm: Trigger Kit launch email to full list
- 2:00pm-4:00pm: Social posts go live, staggered across platforms (not all at once)
- Log all upload dates in WORKLOG.md — 30-day conversion measurement window starts from this date

---

## Section 4: Etsy Upload Sequencing by Cluster

When adding lifestyle images to Etsy listings, follow this upload priority. Do not wait for all 21 products to be ready before uploading any — upload each cluster as it becomes ready.

| Priority | Cluster | Products | Target Upload Date |
|----------|---------|----------|--------------------|
| 1 | D — Stock (composited) | Survival Garden, Hunting Manual, Livestock Manual, Meat/Fish Preservation | May 15 (after compositing) |
| 2 | E — Wikimedia/Pexels | Native Plants Regional Guide | May 15 (alongside Cluster D) |
| 3 | C — Physical | Harvest Preservation, Fermented Harvest, Grow Your Own Hot Sauce | May 15-17 (after editing) |
| 4 | B — Physical | Container Blueprint, Apartment Growing, Apartment Plant Catalog, Seed Swap Kit | May 16-18 |
| 5 | A — Physical | All 9 seed/garden products | May 16-20 |

**Upload rule**: Add exactly 2 images per listing (slot 4 and slot 5). Do not change any other listing element during the upload — isolate the photography variable for clean before/after conversion data.

**Attribution note for Native Plants slot 4**: The Wikimedia image (Joe Mabel, CC BY-SA 3.0) requires attribution in the Etsy listing description footer. Add the line: "Background photo (listing image 4): Joe Mabel, CC BY-SA 3.0, via Wikimedia Commons."

---

## Section 5: Success Metrics — May and Launch Week

Pull data every Friday. Log in WORKLOG.md.

| Metric | Week 2 Target (May 14) | Week 4 Target (May 30) | Source |
|--------|------------------------|------------------------|--------|
| Instagram followers | 50+ | 150+ | Instagram Insights |
| Pinterest monthly views | 500+ | 2,000+ | Pinterest Analytics |
| TikTok followers | 25+ | 100+ | TikTok Analytics |
| Email list subscribers | 10+ | 50+ | Kit subscribers dashboard |
| Welcome email open rate | — | 40%+ | Kit email analytics |
| Etsy listing views (all) | 50+ | 200+ | Etsy Shop Stats |

**Recovery protocol**: If Week 2 Instagram followers are below 20, review Day 1 Reel completion rate in Insights. If completion rate is below 30%, re-record the hook — the first 3 seconds are the algorithm signal. The hook, not the production quality, determines reach on a new account.

If Week 2 Pinterest views are below 200, increase pin frequency to 3-4 per day for the following week. Pinterest distributes pins that are already generating engagement faster than new pins; batch 15+ pins and let the algorithm select which ones surface.

---

## Section 6: Risk Register — Track B

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Social handle `seedwarden` unavailable on a platform | Low-medium | Low | Use `seedwarden.co` or `seedwarden.seeds`; document actual handles in WORKLOG.md |
| Germination tray not started (sprouts not ready for May 10 shoot) | Medium | Low | Use grocery-store bean sprout or microgreen tray as prop substitute; or use stock photography for 2 products (Seed Saving Field Manual, Zone Calendar) |
| May 10-11 shoot unavailable | Low | Medium | Reschedule to May 17-18 (same format). Pushes Phase 4 launch to June 6; no revenue impact. |
| Canva compositing creates unconvincing product-in-scene appearance | Low | Low | Test compositing on one Cluster D product before running all 10; fallback is flat 2D label overlay |
| Kit account setup delayed | Low | Low | Email automation launches after zone cards are ready regardless; first subscribers can be manually welcomed with a direct email if automation is delayed by 1-2 days |
| Etsy account still not verified at launch | Confirmed open | Low for Track B | Track B is independent; CTAs say "link in bio to get your zone card" (email capture). When Etsy goes live, update CTAs. No Track B content needs to be redone. |

---

## Section 7: File and Directory Reference

All output files for Track B are staged in these directories:

| Directory | Contents |
|-----------|---------|
| `/projects/seedwarden/assets/stock-raw/` | Raw staged Cluster D and E stock images (10 files) |
| `/projects/seedwarden/marketing/lifestyle-photos/etsy-ready/` | Final 2400x2400px JPEG exports (receives output from both stock compositing and physical shoot editing) |
| `/projects/seedwarden/marketing/lifestyle-photos/pins/` | Social variant crops (1000x1500px Pinterest, 1080x1350px Instagram) |
| `/projects/seedwarden/assets/zone-cards/` | Zone card PDFs (8 files, post-build) |
| `/projects/seedwarden/mockups/` | Existing slots 1-3 mockup images (63 files, confirmed complete) |

**Naming conventions**:
- Lifestyle photos (Etsy): `[product-slug]-slot4.jpg` and `[product-slug]-slot5.jpg`
- Social variant crops: `[product-slug]-ig.jpg` (Instagram), `[product-slug]-pin.jpg` (Pinterest)
- Zone cards: `zone-[number]-quick-start-card.pdf`

---

**Prepared**: 2026-05-01, Session 694
**Status**: No blockers — proceed on all four workstreams immediately
**Next milestone**: Social accounts live + Day 1 Reel published (target: May 2-3, 2026)
