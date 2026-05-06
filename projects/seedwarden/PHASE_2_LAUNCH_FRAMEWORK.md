---
title: "Phase 2 Launch Framework — Master Reference"
date: 2026-05-06
status: production-ready
session: 819
deadline: May 30, 2026 (June 6 fallback)
scope: 25-day execution timeline, tool integration map, launch sequence, contingency path, pre-launch checklist
---

# Phase 2 Launch Framework
## Single Reference Document

**What this document is**: A navigation layer over the five Phase 2 launch planning files produced in Session 819. Each section below names the right document for each use case, summarizes its key decision points, and states the one thing that cannot be skipped.

**Target user**: The orchestrator agent or the user, when deciding what to read and in what order.

---

## Five-File Overview

| File | Use When | Critical Dependency It Owns |
|---|---|---|
| `phase-2-launch-timeline.md` | Planning track sequencing, checking what is on the critical path, deciding whether to activate the June 6 fallback | Day 1 (May 6) account setup is the unlock for all other tracks |
| `phase-2-tool-integration-map.md` | Executing a cross-tool handoff, diagnosing a broken integration, setting up API connections | Google Drive URL format (`?export=download&id=`) is the single most common failure point |
| `may-30-launch-sequence.md` | Launch day itself, minute by minute | Kit broadcast must show "Scheduled" — not "Draft" — before May 30 |
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

## Critical Path in Order

These are the items where a delay of N days produces a launch-date slip of N days:

1. Canva Brand Kit setup (unlocks zone card production)
2. Zone 5 master template (unlocks all other zone cards — built by cloning from Zone 5)
3. All 8 zone cards complete and exported as PDFs (unlocks Kit email load)
4. All 8 Google Drive download URLs captured and tested (unlocks Kit automation wiring)
5. Kit Email 1 loaded for all 8 zones (unlocks Kit automation test)
6. Kit automation end-to-end tested for 2 zones (unlocks Kit automation go-live)
7. Kit automation live by May 25 (unlocks subscriber collection before launch day)
8. Kit broadcast staged for May 30 12pm (unlocks email launch)

---

## Non-Critical Items (can slip without launch impact)

- Photo shoot (only affects Etsy slots 4-5 and lifestyle social posts — not email or zone card delivery)
- Zones 9 and 10 (can launch with 6 zones; deliver 9 and 10 in June)
- Pinterest batch 2 pins
- Buffer OAuth re-authorization (can be done day-of if needed, takes 5 min)
- Post-purchase email automation (can be added after launch)
- Zapier Etsy → social automation (optional for Phase 2)

---

## Staggered Launch Sequence Summary

**May 30 execution order** (detailed in `may-30-launch-sequence.md`):

| Time | Action | Rationale |
|---|---|---|
| 8:00am | Final QA — all four verification blocks | 60-minute window, fixes must happen here |
| 9:00am | Baseline metrics record; browser setup | Before-state anchors attribution |
| 10:00am | Etsy: confirm all 21 listings at 5-image status | Etsy algorithm gets 2 hours to register before email spike |
| 12:00pm | Kit: verify broadcast shows "Sent" by 12:05pm | Email reaches subscriber list with known-live listings |
| 2:00pm | Instagram + TikTok launch posts go live via Buffer | Social reaches coldest audience last; 2-hr gap from email |
| 3:30pm | Pinterest launch pins go live | Staggered from Instagram/TikTok to extend content footprint |
| End of day | Metrics log in WORKLOG.md + customer-analytics.csv | Conversion window measurement starts today |

---

## Tool Integration Summary

Six integration points in Phase 2:

| From | To | Format | Manual or Automated |
|---|---|---|---|
| Canva | Google Drive | PDF Print, 1-4MB, zone naming convention | Manual (download + upload) |
| Google Drive | Kit email editor | Direct download URL (`uc?export=download&id=`) | Manual (URL paste per zone) |
| Canva | Etsy | JPEG 2400×2400px, 90%, <2MB | Manual (Etsy image editor) |
| Canva | Buffer/Later | Platform-specific crops (1080sq, 1000×1500, 9:16) | Manual (upload per post) |
| Kit | Subscriber inbox | SPF/DKIM authenticated automated sends | Automated after setup |
| Buffer/Later | Social platforms | OAuth API (re-authorize May 28) | Automated after scheduling |

The most fragile handoff is Google Drive to Kit. The specific URL format required (`uc?export=download&id=[ID]`) is counter-intuitive — Google Drive's default share link format does not work for email delivery. This is documented and the test procedure (incognito window, confirm download dialog not viewer) is non-negotiable.

---

## June 6 Fallback: One-Line Decision Rule

**If by May 20, the photo shoot has not happened on May 10-11 or rescheduled to May 17-18**: Activate the June 6 path. Update Buffer/Later, reschedule the Kit broadcast, shift Etsy upload window. Email automation still launches May 25 regardless. Teaser social content can run May 30.

Full decision logic in `june-6-contingency-path.md`.

---

## Pre-Launch Validation Schedule

| Date | Validation Section | Key Thing Being Confirmed |
|---|---|---|
| May 24-25 | Canva: zone card export + lifestyle images | PDFs downloadable, all 42 lifestyle images exported correctly |
| May 25-26 | Etsy: listing completeness + coupon | All 21 listings at 5 images, SEEDWARDEN15 active |
| May 25-27 | Kit: account + automation + e2e test | Automation live, two zones tested, broadcast staged |
| May 27-28 | Social: Buffer scheduling + connections | All posts scheduled, OAuth active |
| May 28-29 | Final 48h: re-authorize Buffer, re-test Drive links | No surprises on launch morning |
| May 29 | Go/No-Go decision written in WORKLOG.md | Four tracks reviewed, proceed or shift to June 6 |

---

## Success Metrics: What "Launched Successfully" Means

### Etsy (by 12pm May 30)
- All 21 listings active with 5 images
- Zero listing errors
- SEEDWARDEN15 coupon active

### Email (by 6pm May 30)
- Broadcast delivery rate >90%
- Bounce rate <2%
- Open rate >35% (note: inflated by Apple MPP — click rate is more reliable signal)
- Click rate >8%

### Social (by end of Day 1)
- Instagram impressions >50
- TikTok views >50
- Pinterest impressions >30 (by Day 2 — indexing delay expected)
- New email sign-ups from social >3

### Week 1 Targets (by June 6)
- Kit subscriber count: 65+ (50 at launch + 15 from launch week activity)
- Etsy total orders: 4+ (from Email 5 coupon redemptions + organic)
- Welcome email open rate: >40%
- Email 3 click rate: >15% (primary high-intent signal)

---

## File Locations (all in `projects/seedwarden/`)

| File | Path |
|---|---|
| 25-day master timeline | `projects/seedwarden/phase-2-launch-timeline.md` |
| Tool integration map | `projects/seedwarden/phase-2-tool-integration-map.md` |
| Launch day sequence | `projects/seedwarden/may-30-launch-sequence.md` |
| June 6 contingency | `projects/seedwarden/june-6-contingency-path.md` |
| Pre-launch checklist | `projects/seedwarden/phase-2-pre-launch-checklist.md` |
| This synthesis document | `projects/seedwarden/PHASE_2_LAUNCH_FRAMEWORK.md` |

Pre-existing reference files these documents draw from:

| File | Purpose |
|---|---|
| `phase-2-execution-timeline.md` | Phase 2 production timeline, dependency map (Session 717) |
| `TRACK_B_FINAL_EXECUTION_GUIDE.md` | All user-facing actions with exact steps (Session 728) |
| `tool-integration-map.md` | Per-handoff failure modes and export specs (Session 819) |
| `launch-day-script.md` | Detailed T-2h through T+24h action blocks (Session 819) |
| `contingency-paths.md` | Pre-decided recovery protocols for 5 disruption scenarios (Session 819) |
| `kit-account-setup-guide.md` | Complete Kit configuration reference (Session 819) |
| `marketing/email-and-launch-plan.md` | Full email copy for all 5 sequence emails + launch broadcast |

---

*Generated: 2026-05-06. Session 819. Scope: Phase 2 Launch Execution Framework (5 deliverable files + this synthesis). Launch target: May 30, 2026. Fallback: June 6, 2026.*
