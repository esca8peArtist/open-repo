---
title: "Phase 2 Launch Framework — Master Reference"
date: 2026-05-06
updated: 2026-05-06
status: production-ready
session: 819
deadline: May 30, 2026 (June 6 fallback)
scope: 25-day execution timeline, tool integration map, launch sequence, contingency path, pre-launch checklist
---

# Phase 2 Launch Framework
## Master Reference — Navigation, Critical Path, and Success Metrics

**What this document is**: A navigation layer over the seven Phase 2 launch planning files. Each section names the right document for each use case, summarizes its key decision points, and states the one thing that cannot be skipped. Start here on any day you need to orient.

**Target launch date**: May 30, 2026
**Fallback date**: June 6, 2026
**Today**: May 6, 2026 — 24 days to launch

---

## Eight-File Overview

| File | Use When | Critical Dependency It Owns |
|---|---|---|
| `phase-2-launch-timeline.md` | Planning track sequencing, checking what is on the critical path, deciding whether to activate the June 6 fallback | Day 1 (May 6) account setup is the unlock for all other tracks |
| `phase-2-tool-integration-map.md` | Executing a cross-tool handoff, diagnosing a broken integration, setting up API connections | Google Drive URL format (`?export=download&id=`) is the single most common silent failure point |
| `TRACK_B_SOCIAL_ACCOUNT_CHECKLIST.md` | Creating Instagram, TikTok, and Pinterest accounts | All three accounts must be Business type; same handle on all three platforms |
| `TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md` | Canva Brand Kit setup, zone card build sequence, export specs, Buffer/Later scheduling configuration | Brand Kit must be configured before any Canva zone card or pin production begins |
| `TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md` | Kit account setup, landing page, 5-email sequence, zone routing, 3-test protocol | Zone card PDFs must exist before Kit Email 1 can be loaded |
| `may-30-launch-sequence.md` | Launch day itself, minute by minute, with rollback procedures for 4 failure scenarios | Kit broadcast must show "Scheduled" — not "Draft" — before May 30 |
| `june-6-contingency-path.md` | Photo shoot pushed to May 17-18, or Phase 1 Etsy delayed | Decision must be made by May 20 — not May 27 |
| `phase-2-pre-launch-checklist.md` | May 24-29 validation, go/no-go decision May 29 | All 8 Google Drive download links must be incognito-tested before launch |

---

## State of Play: What Has Not Happened Yet

As of May 6, 2026, these are the three Track B user actions that have not been completed:

1. **Social account creation**: Instagram, TikTok, and Pinterest business accounts not yet created. This is the dependency gate for Day 1 Reel upload, bio link placement, and social scheduling.
2. **Canva Brand Kit setup**: Brand Kit not yet configured in Canva. This is the dependency gate for all zone card production and social graphic templates.
3. **Kit account and landing page**: Kit account not yet created, landing page not yet built. This is the dependency gate for zone card delivery, email automation, and bio link go-live.

Once these three items are complete (estimated May 6-7, 90-120 minutes total), every other track can proceed independently and in parallel.

---

## ASCII Critical Path Diagram

```
MAY 6-30 CRITICAL PATH — Phase 2 Launch

May 6-7: GATE ACTIONS (must complete before all downstream tracks)
+-----------+  +--------------+  +-----------------+
| SOCIAL    |  | CANVA BRAND  |  | KIT ACCOUNT +   |
| ACCOUNTS  |  | KIT SETUP    |  | LANDING PAGE    |
| 45 min    |  | 30 min       |  | 45 min          |
+-----------+  +--------------+  +-----------------+
     |                |                   |
     v                v                   v
     ALL TRACKS BELOW UNLOCK SIMULTANEOUSLY
     |                |                   |
     v                v                   v
+-----------+  +--------------+  +-----------------+
| Social    |  | ZONE CARD    |  | Zone cards must |
| content   |  | PRODUCTION   |  | complete before |
| posting   |  | May 7-19     |  | Kit can be      |
| (parallel)|  | 8 cards      |  | configured      |
|           |  | 7.5-9 hrs    |  |                 |
+-----------+  +--------------+  +-----------------+
                      |                   |
                      v                   |
             +----------------+           |
             | PHOTO SHOOT    |           |
             | May 10-11      |           |
             | (parallel —    |           |
             | only needed    |           |
             | for Etsy slots)|           |
             +----------------+           |
                      |                   v
                      v          +-----------------+
             +----------------+  | KIT EMAIL BUILD |
             | IMAGE EDITING  |  | May 19-24       |
             | May 12-14      |  | Emails 1-5      |
             +----------------+  | 8 zone variants |
                      |          +-----------------+
                      v                   |
             +----------------+           v
             | ETSY UPLOAD    |  +-----------------+
             | Slots 4-5      |  | KIT AUTOMATION  |
             | May 15-24      |  | LIVE by May 25  |
             +----------------+  +-----------------+
                      |                   |
                      v                   v
             +----------------+  +-----------------+
             | SOCIAL CONTENT |  | BROADCAST       |
             | SCHEDULING     |  | STAGED for      |
             | May 25-29      |  | May 30 12pm     |
             | Buffer/Later   |  +-----------------+
             +----------------+           |
                      |                   |
                      v                   v
             +-----------------------------------------+
             |         MAY 30 LAUNCH DAY              |
             |  10am Etsy  |  12pm Email  |  2pm Social|
             +-----------------------------------------+

CRITICAL PATH (delay = launch slips):
Zone 5 master card (May 7-9) → All 8 cards (by May 19) → Google Drive upload (May 19-21)
→ Kit Email 1 build (May 19-22) → Kit end-to-end test (May 24-25) → Kit live (May 25)
→ Broadcast staged (by May 29) → LAUNCH May 30 12pm

NON-CRITICAL (can slip without launch impact):
Photo shoot, Zones 9-10, Pinterest batch 2, post-purchase automation, Zapier
```

---

## User Action Checklist: What You Must Do vs. What Is Automated

This table separates every Phase 2 task by who executes it. Nothing in the "User" column can be done by the agent. Everything in the "Automated" column runs without intervention once it is set up.

### User-Required Actions (you must physically do these)

| # | Action | Time | Deadline | Unblocks |
|---|---|---|---|---|
| U1 | Create Instagram Business account (@seedwarden) | 20 min | May 7 | All social scheduling |
| U2 | Create TikTok Business account (@seedwarden) | 15 min | May 7 | TikTok content |
| U3 | Create Pinterest Business account (@seedwarden) | 15 min | May 7 | Pinterest pins |
| U4 | Set up Canva Brand Kit (6 colors, 3 fonts, logo) | 30 min | May 7 | All Canva production |
| U5 | Create Kit account + build landing page + publish | 45 min | May 7 | Email automation |
| U6 | Add Kit landing page URL to all three social bios | 10 min | May 7 | Lead capture from Day 1 |
| U7 | Check germination tray / start if not started | 5 min | May 6 (last date) | Cluster A shoot viability |
| U8 | Source all shoot props (3 store stops) | 2-3 hrs | May 9 | May 10-11 shoot |
| U9 | Print 20-25 product pages as shoot props | 20 min | May 9 | May 10-11 shoot |
| U10 | Film Cluster A shoot (9 products, 18 shots) | 4.5 hrs | May 10 9am-1:30pm | 18 lifestyle images |
| U11 | Film Cluster B shoot (4 products, 8 shots) | 2 hrs | May 10 3-5pm | 8 lifestyle images |
| U12 | Film Cluster C shoot (3 products, 6 shots) | 2 hrs | May 11 9-11am | 6 lifestyle images |
| U13 | Cull photos — 80-100 RAW to 30 selects | 2 hrs | May 12 | Editing phase |
| U14 | Batch edit 30 selects in Lightroom Mobile | 2 hrs | May 13 | Export phase |
| U15 | Export 30 JPEGs to `etsy-ready/` (2400x2400px) | 1.5 hrs | May 14 | Etsy upload |
| U16 | Build Zone 5 master card in Canva | 2.5-3 hrs | May 8-9 | All 7 remaining zone cards |
| U17 | Build Zones 3, 4, 6, 7, 8, 9, 10 (clone from Zone 5) | 5-6 hrs | May 11-17 | Kit Email 1 |
| U18 | QA all 8 zone cards — no placeholder text | 45 min | May 17-18 | Export phase |
| U19 | Export all 8 PDFs at PDF Print quality | 20 min | May 19 | Google Drive upload |
| U20 | Upload all 8 PDFs to Google Drive, set sharing | 20 min | May 19 | Kit email load |
| U21 | Test all 8 Drive URLs in incognito | 10 min | May 19-21 | Kit automation |
| U22 | Build Kit Email 1 (8 zone variants with download links) | 3-4 hrs | May 22 | Automation |
| U23 | Build Kit Emails 2-5 | 2-3 hrs | May 23 | Sequence |
| U24 | Create SEEDWARDEN15 coupon in Etsy | 10 min | By May 20 | Email 5 |
| U25 | Wire zone-conditional automation in Kit | 45 min | May 23-24 | Go-live |
| U26 | Run end-to-end test Zone 5 (incognito sign-up) | 15 min | May 24-25 | Automation live |
| U27 | Run end-to-end test Zone 7 | 15 min | May 24-25 | Automation confirmed |
| U28 | Composite Cluster D+E images in Canva (10 images) | 3-4 hrs | May 15 | Etsy upload |
| U29 | Upload all 21 Etsy products to slots 4-5 | 2 hrs | By May 29 | Etsy phase of launch |
| U30 | Schedule all launch social posts in Buffer/Later | 60 min | May 25-29 | Social phase |
| U31 | Stage Kit broadcast for May 30 12pm | 15 min | By May 29 | Email launch |
| U32 | Re-authorize all Buffer connections | 5 min | May 28 | Social phase |
| U33 | Final pre-launch QA (checklist in pre-launch-checklist.md) | 2-3 hrs | May 24-29 | Go/no-go decision |
| U34 | Write May 29 WORKLOG entry — go/no-go decision | 10 min | May 29 | Launch confidence |

**Total user time**: Approximately 40-50 hours distributed across May 6-29.
**Day-level breakdown**: See `phase-2-launch-timeline.md` for each day's task table.

---

### Automated Actions (run without your intervention after setup)

| # | Action | When It Fires | What Triggers It | Prerequisite Setup |
|---|---|---|---|---|
| A1 | Email 1 sends to new subscriber with zone card link | Within 60 seconds of sign-up | Form submission on Kit landing page | U5, U20, U22, U25 complete |
| A2 | Zone routing: correct PDF delivered per zone selection | Simultaneously with A1 | Subscriber's zone dropdown value | U25 complete |
| A3 | "zone-[N]" tag applied to subscriber profile | Simultaneously with A1 | Zone dropdown value on form | U25 complete |
| A4 | Email 2 sends to subscriber | Day 2 after sign-up | Kit sequence scheduler | U23 complete |
| A5 | Email 3 sends to subscriber | Day 5 after sign-up | Kit sequence scheduler | U23 complete |
| A6 | "seed-saver" tag applied | When subscriber clicks Email 3 product link | Click event in Kit | U23 complete (behavioral tag set up) |
| A7 | Email 4 sends to subscriber | Day 7 after sign-up | Kit sequence scheduler | U23 complete |
| A8 | "city-grower", "preservationist" tags applied | When subscriber clicks Email 4 links | Click events in Kit | U23 complete |
| A9 | Email 5 sends to subscriber with coupon | Day 10 after sign-up | Kit sequence scheduler | U23, U24 complete |
| A10 | Instagram launch post goes live | May 30 2:00pm | Buffer scheduled post | U30 complete |
| A11 | TikTok launch post goes live | May 30 2:00pm | Buffer scheduled post | U30 complete |
| A12 | Pinterest launch pins go live | May 30 3:30pm | Buffer scheduled post | U30 complete |
| A13 | Etsy coupon activates for buyers | Live from May 20 onward | Shopper enters SEEDWARDEN15 at checkout | U24 complete |

**Note on the launch broadcast (Kit)**: The broadcast does NOT send automatically. It must be manually staged and confirmed as "Scheduled" (not "Draft") in Kit before May 30. This is item U31 above.

---

## Critical Path in Order

These are the items where a delay of N days produces a launch-date slip of N days:

1. Canva Brand Kit setup (May 6-7) — unlocks all Canva production
2. Zone 5 master template (May 7-9) — unlocks all 7 remaining zone cards
3. All 8 zone cards complete and exported (by May 19) — unlocks Kit Email 1 build
4. All 8 Google Drive download URLs captured and incognito-tested (May 19-21) — unlocks Kit automation wiring
5. Kit Email 1 loaded for all 8 zones (May 22) — unlocks automation test
6. Kit automation end-to-end tested for 2 zones (May 24-25) — unlocks Kit go-live
7. Kit automation live by May 25 — unlocks subscriber collection before launch day
8. Kit broadcast staged for May 30 12pm (by May 29) — unlocks email launch

---

## Non-Critical Items (can slip without launch impact)

| Item | Latest Slip | Notes |
|---|---|---|
| Photo shoot | May 17-18 | Only affects Etsy slots 4-5 and lifestyle social — not email, zone cards, or Kit |
| Zones 9 and 10 | May 27 (3-day float) | Launch with 6 zones; deliver 9-10 in June. Kit Email 1 shows placeholder message for those zones. |
| Cluster D/E compositing | May 25 | Stock images staged; float is generous. |
| Pinterest batch 2 pins | May 28 | Nice-to-have social engagement |
| Buffer OAuth re-authorization | May 28 (day-of is fine) | Takes 5 min if expired |
| Post-purchase automation | After launch | Phase 3 feature |
| Zapier Etsy → social | After launch | Optional automation |

---

## Staggered Launch Sequence Summary

**May 30 execution order** (full minute-by-minute in `may-30-launch-sequence.md`):

| Time | Action | Rationale |
|---|---|---|
| 8:00am | Final QA — four verification blocks (Etsy, Kit, Social, Drive) | 60-minute window; fixes happen here, not at launch time |
| 9:00am | Baseline metrics record; browser setup | Before-state anchors all Phase 2 attribution |
| 10:00am | Etsy: confirm all 21 listings at 5-image status | Etsy algorithm gets 2 hours to register before email spike; organic buyers in this window are highest-quality signal |
| 12:00pm | Kit: verify broadcast shows "Sent" by 12:05pm | Email reaches subscriber list with confirmed-live listings; email drives controlled traffic spike |
| 2:00pm | Instagram + TikTok launch posts go live via Buffer | Social reaches coldest audience last; 2-hour gap from email prevents reach overlap |
| 3:30pm | Pinterest launch pins go live | Staggered from Instagram/TikTok to extend content footprint across the day |
| End of day | Metrics log in WORKLOG.md + customer-analytics.csv | 30-day conversion measurement window starts today |

---

## Tool Integration Summary

Six integration handoffs in Phase 2:

| From | To | Format | Manual or Automated | Risk Level |
|---|---|---|---|---|
| Canva | Google Drive | PDF Print quality, 1-4MB, `zone-[N]-quick-start-card.pdf` naming | Manual (download + upload) | Low |
| Google Drive | Kit email editor | Direct download URL (`uc?export=download&id=`) | Manual (URL paste per zone) | **HIGH** — wrong URL format is a silent failure |
| Canva | Etsy | JPEG 2400×2400px, 90% quality, <2MB | Manual (Etsy image editor) | Low |
| Canva | Buffer/Later | Platform-specific crops (1080sq, 1000×1500, 9:16) | Manual (upload per post) | Low |
| Kit | Subscriber inbox | SPF/DKIM authenticated automated sends | Automated after setup | Low after DNS verified |
| Buffer/Later | Social platforms | OAuth API (must re-authorize May 28) | Automated after scheduling | Medium (OAuth expiry) |

**The most fragile handoff**: Google Drive to Kit. The `uc?export=download&id=[ID]` URL format is required — Google Drive's default share link opens a viewer page, not a download dialog. Subscribers who click a viewer link cannot download their zone card. Test all 8 URLs in an incognito window before loading into Kit. This test is non-negotiable.

Full handoff specs, failure modes, and the QA checklist are in `phase-2-tool-integration-map.md`.

---

## June 6 Fallback: One-Line Decision Rule

**If by May 20, the photo shoot has not happened on May 10-11 AND is not rescheduled to May 17-18**: Activate the June 6 path. Update Buffer/Later, reschedule the Kit broadcast, shift Etsy upload window. Email automation still launches May 25 regardless.

Full decision logic and revised timeline in `june-6-contingency-path.md`.

---

## Pre-Launch Validation Schedule

| Date | Validation Section | Key Thing Being Confirmed |
|---|---|---|
| May 24-25 | Canva: zone card export + lifestyle images | PDFs downloadable, all 42 lifestyle images at correct specs |
| May 25-26 | Etsy: listing completeness + coupon | All 21 listings active with 5 images, SEEDWARDEN15 active |
| May 25-27 | Kit: account + automation + e2e test | Automation live, 2 zones tested, broadcast staged |
| May 27-28 | Social: Buffer scheduling + connections | All posts scheduled, OAuth active |
| May 28-29 | Final 48h: re-authorize Buffer, re-test Drive links | No surprises on launch morning |
| May 29 | Go/No-Go decision written in WORKLOG.md | Four tracks reviewed; proceed or shift to June 6 |

Full 7-day validation checklist is in `phase-2-pre-launch-checklist.md`.

---

## Success Metrics Table: What "Launched Successfully" Looks Like

### May 30 Launch Day Success Criteria

| Track | Target | Minimum Acceptable | Indicates Failure |
|---|---|---|---|
| **Etsy** — Listings live | 21 of 21 listings active with 5 images | 18 of 21 (remaining 3 uploaded within 24 hrs) | Any listing in "Draft" status at 10am |
| **Etsy** — Coupon | SEEDWARDEN15 active with 15% off | Same | Coupon expired or not found |
| **Etsy** — Organic views (10am-12pm) | Any organic views | 1+ | Zero views by 12pm may indicate Etsy algorithm issue |
| **Email** — Broadcast sent | Shows "Sent" or "Sending" by 12:05pm | "Sending" (in queue) | Still "Scheduled" or "Draft" at 12:20pm |
| **Email** — Delivery rate | >90% | >80% | Below 80%: bounce/spam issue (DNS records) |
| **Email** — Bounce rate | <2% | <5% | Above 5%: list hygiene issue |
| **Email** — Open rate (6 hrs) | >35% | >20% | Below 20%: subject line or spam filter issue |
| **Email** — Click rate (6 hrs) | >8% | >3% | Below 3%: CTA rendering or mobile display issue |
| **Social** — Instagram impressions | >50 by EOD | >20 | Under 10: content not indexed yet (normal on Day 1) |
| **Social** — TikTok views | >50 by EOD | >20 | Under 10: may be suppressed (confirm video not cross-posted) |
| **Social** — Pinterest impressions | >30 by Day 2 | >10 by Day 2 | Indexing delay of 24-48 hrs is normal for Pinterest |
| **Social** — New email sign-ups | >3 from social Day 1 | >0 | Zero: bio link broken; check Kit landing page URL in bio |

### Week 1 Targets (by June 6)

| Metric | Target | Minimum | Source |
|---|---|---|---|
| Kit subscriber count | 65+ | 50+ | Kit dashboard |
| Welcome email open rate | 40%+ | 30% | Kit analytics |
| Email 3 click rate | 15%+ | 8% | Kit analytics — primary high-intent signal |
| Etsy total orders (Phase 2 attributable) | 4+ | 1+ | Etsy Shop Manager > Orders |
| Instagram followers | 150+ | 75+ | Instagram Insights |
| Pinterest monthly viewers | 2,000+ | 500+ | Pinterest Analytics |
| TikTok followers | 100+ | 40+ | TikTok Analytics |

### 30-Day Conversion Window Targets (by June 30)

| Metric | Target | Significance |
|---|---|---|
| Kit subscriber count | 200+ | Validates social bio conversion rate |
| Etsy listing conversion rate | 2%+ (up from Phase 1 baseline) | Lifestyle image impact signal |
| Revenue attributable to email sequence | 1+ orders per 10 subscribers | Validates Email 5 coupon design |
| Instagram followers | 400+ | Organic social growth rate |
| Products with measurable CTR lift | 5+ (from Phase 1 baseline) | Validates lifestyle image investment |

---

## File Locations (all in `projects/seedwarden/`)

| File | Purpose |
|---|---|
| `phase-2-launch-timeline.md` | 25-day master timeline, day-by-day task tables, critical path, 5 trigger conditions |
| `phase-2-tool-integration-map.md` | Workflow diagram, data flow per handoff, API status, QA checklist (34 items) |
| `TRACK_B_SOCIAL_ACCOUNT_CHECKLIST.md` | Instagram, TikTok, Pinterest step-by-step setup with exact bio copy |
| `TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md` | Brand Kit config, zone card build sequence, export specs, Buffer setup |
| `TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md` | Kit account, 15 tags, landing page, zone routing, 5-email build, 3-test protocol |
| `may-30-launch-sequence.md` | Minute-by-minute launch day guide with 4 rollback procedures |
| `june-6-contingency-path.md` | Photo slip recovery, May 14 decision gate, what can still launch May 30 |
| `phase-2-pre-launch-checklist.md` | 7-day validation (May 24-29), go/no-go decision template |
| `PHASE_2_LAUNCH_FRAMEWORK.md` | This document — navigation, critical path, user/automated split, success metrics |

Pre-existing reference files these documents draw from:

| File | Purpose |
|---|---|
| `TRACK_B_FINAL_EXECUTION_GUIDE.md` | All user-facing actions with exact steps (Session 728) |
| `TRACK_B_PRODUCTION_PIPELINE.md` | Full pipeline and publication sequence (Session 694, updated 724) |
| `tool-integration-map.md` | Per-handoff failure modes (Session 819) |
| `launch-day-script.md` | T-2h through T+24h action blocks (Session 819) |
| `contingency-paths.md` | Pre-decided recovery protocols for 5 disruption scenarios (Session 819) |
| `kit-account-setup-guide.md` | Complete Kit configuration reference (Session 819) |
| `marketing/email-and-launch-plan.md` | Full email copy for all 5 sequence emails + launch broadcast |
| `MAY_CONTENT_EXECUTION_PLAN.md` | Day-level May execution plan + email sequence copy |
| `phase-2-social-content-calendar-60day.md` | 60-day post hooks, scripts, captions, hashtags |
| `SHOOT_PROPS_CHECKLIST.md` | May 10-11 shoot props list by cluster and store type |
| `PHOTO_SHOOT_SCHEDULE_AND_PROPS.md` | May 10-11 shoot schedule with times and shot sequences |
| `KIT_SETUP_NOTES.md` | Step-by-step Kit platform setup with all 15 tags |
| `CANVA_SETUP_STATUS.md` | Brand Kit spec and zone card build status tracker |
| `CANVA_ZONE_CARD_BATCH_WORKFLOW.md` | Per-zone content tables with May 2026 seasonal blocks |
| `CANVA_ZONE_CARD_DESIGN_GUIDE.md` | Step-by-step Canva build instructions |

---

*Generated: 2026-05-06. Session 819. Expanded: 2026-05-06. Launch target: May 30, 2026. Fallback: June 6, 2026. This document supersedes the prior version of PHASE_2_LAUNCH_FRAMEWORK.md. All referenced source documents remain authoritative for their specific content — this guide is the navigation layer only.*
