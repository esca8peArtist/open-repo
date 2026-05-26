---
title: "May 30 Pre-Launch Checklist — Seedwarden Track B (Session 1693)"
date: 2026-05-27
version: 1.0
status: PRODUCTION-READY
scope: 24-hour countdown checklist for May 30 08:00 UTC launch
references:
  - LAUNCH_DAY_HOUR_BY_HOUR_RUNBOOK.md (full execution detail)
  - LAUNCH_DAY_DECISION_TREES_DETAILED.md (troubleshooting)
  - LAUNCH_DAY_ROLLBACK_PROCEDURES.md (pause/revert procedures)
  - LAUNCH_DAY_SUCCESS_METRICS.md (Tier 1-3 thresholds)
  - LAUNCH_DAY_STATUS_TEMPLATE.md (Discord + CHECKIN templates)
---

# May 30 Pre-Launch Checklist
## Seedwarden Track B Zone Cards — 24-Hour Countdown

**Launch target**: May 30, 2026 08:00 UTC
**Checklist window**: May 29 18:00 UTC through May 30 21:00 UTC

---

## May 29 — Evening Prep (18:00–22:00 UTC)

### 18:00 UTC — Final Template Review
- [ ] Open `HERBALIST_PARTNERSHIP_EMAIL_TEMPLATE.md` — read Templates A through E in full
- [ ] Confirm all 15 contacts have been assigned a template (see `INFLUENCER_STAGING_VERIFICATION.md` Section 2)
- [ ] Insert the Gist/Kit landing page URL into `[LANDING_PAGE_URL]` placeholder in all 5 templates
- [ ] Send test email to yourself from each template variant — verify formatting, links, subject line
- [ ] Open `TRACK_B_SOCIAL_SCHEDULING_TEMPLATES.md` — confirm all 4 launch posts are drafted and queued

### 20:00 UTC — System Pre-Check
- [ ] Log in to all 4 platforms: Instagram (Buffer), TikTok Creator Studio, Pinterest, Reddit
- [ ] Verify all 8 Etsy Zone Card listings exist in Draft status — Zone 3, 4, 5, 6, 7, 8, 9, 10
- [ ] Confirm Kit broadcast email is drafted and ready (set send time to 12:00 UTC May 30)
- [ ] Verify GA4 Real-Time dashboard loads (analytics.google.com > Real-Time > Overview)
- [ ] Confirm `[LANDING_PAGE_URL]` in Kit broadcast email matches the Gist/landing page URL from templates

### 21:00 UTC — Go/No-Go Decision
- [ ] Review `MAY_29_GO_NO_GO_DECISION_TEMPLATE.md` — work through each gate criterion
- [ ] If all gates PASS: confirm launch proceeds at 08:00 UTC tomorrow
- [ ] If any gate FAILS: consult `LAUNCH_DAY_DECISION_TREES_DETAILED.md` for recovery path
- [ ] Sleep — launch day execution begins in 11 hours

---

## May 30 — Launch Day Execution

### 06:00 UTC — Pre-Launch System Check (2 hours before go)
- [ ] **Etsy**: All 8 listings confirmed in Draft status — do not publish yet
- [ ] **Kit**: Broadcast email confirmed Scheduled at 12:00 UTC — do not send yet
- [ ] **Social schedulers**: All 4 platform posts queued for 08:30–09:00 UTC window
- [ ] **GA4**: Real-Time dashboard live and showing zero or baseline traffic (expected)
- [ ] **Test GA4**: Visit one Etsy listing in incognito tab — confirm page_view event appears in GA4 Real-Time within 60 seconds
- [ ] Brew coffee. Launch in 2 hours.

### 08:00 UTC — LAUNCH
- [ ] Publish all 8 Etsy Zone Card listings (set status from Draft to Active)
- [ ] Verify each listing is publicly visible in Etsy search (spot-check 2 zones by name)
- [ ] Start social media posts — Instagram, TikTok, Pinterest, Reddit (08:30–09:00 UTC)
- [ ] Send 3 highest-priority influencer emails (Sabrena Gwin AHG, Susan Leopold UpS, John Gallagher LearningHerbs)
- [ ] Post launch announcement in Discord #launch-updates using `LAUNCH_DAY_STATUS_TEMPLATE.md`

### 08:15 UTC — Etsy Publish Checkpoint
- [ ] Confirm all 8 listings published and visible
- [ ] If fewer than 6 are live: consult `LAUNCH_DAY_DECISION_TREES_DETAILED.md` > Failure Mode F5
- [ ] Log status in Discord: "08:15 UTC checkpoint — [N]/8 listings live"

### 10:00 UTC — First Metrics Check
- [ ] GA4 pageviews: target 30–200 (any number >0 means tracking works)
- [ ] If GA4 shows 0: consult Decision Trees > Failure Mode F8 (tracking issue)
- [ ] Send remaining Tier 1 influencer outreach (Juliet Blankespoor, Herbal Academy)
- [ ] Check Kit email scheduled status — confirm it will send at 12:00 UTC

### 12:00 UTC — Email Launch
- [ ] Kit broadcast email sends automatically at 12:00 UTC
- [ ] Verify send confirmation in Kit dashboard within 5 minutes
- [ ] If Kit fails: send Gmail fallback immediately (see `LAUNCH_DAY_ROLLBACK_PROCEDURES.md` > Email Rollback)
- [ ] Send Tier 2 influencer outreach batch (Reddit mods, Discord admins)

### 14:00 UTC — Main Distribution + Mid-Day Checkpoint
- [ ] GA4 pageviews (6 hours): target 100–500
- [ ] Instagram reach: target 100+ (check post analytics)
- [ ] Send Tier 3 outreach (Seattle Herbalism Society, remaining Discord admins)
- [ ] Post Discord update: "14:00 UTC checkpoint — [metrics summary]" using status template
- [ ] If metrics "Poor" (GA4 <100): consult Decision Trees — diagnose social post failures, not a failure signal yet

### 18:00 UTC — First Metrics Checkpoint (Tier 2 Evaluation)
- [ ] GA4 pageviews (10 hours): target 300+ (Good), 100–299 (Acceptable), <100 (Poor)
- [ ] Instagram reach: target 300+ (Good)
- [ ] Kit email open rate: target 20%+ (Good), 10–19% (Acceptable)
- [ ] TikTok views: target 200+ (Good)
- [ ] Reddit upvotes: target 20+ (Good)
- [ ] Pinterest saves: target 10+ (Good)
- [ ] Post Discord update: "18:00 UTC checkpoint — [Tier 2 metrics]" using status template
- [ ] Decision: "Poor" on Day 1 is NORMAL — do not panic-rollback; continue organic outreach

### 21:00 UTC — Day 1 Summary + Next-Day Plan
- [ ] Record final metrics: GA4 pageviews (full day, target 200+), social reach, email opens
- [ ] Evaluate Tier 1 success criteria:
  - Etsy listings published ≥6 of 8: PASS or FAIL
  - Kit broadcast sent: PASS or FAIL
  - Social posts live ≥3 of 4: PASS or FAIL
  - GA4 pageviews ≥50: PASS or FAIL
- [ ] Write Day 1 summary using `LAUNCH_DAY_STATUS_TEMPLATE.md` end-of-day section
- [ ] Post summary to Discord #launch-updates
- [ ] Paste end-of-day summary into CHECKIN.md for orchestrator record
- [ ] Plan Day 2: follow-up outreach, monitor influencer responses, check Etsy stats

---

## Quick Reference — Failure Mode Decision Trees

| Symptom | Action |
|---------|--------|
| Etsy listing won't publish | F5 — check listing completeness, retry in new browser tab |
| Kit email not sending | F3 — send Gmail fallback immediately |
| GA4 showing 0 pageviews | F8 — check GA4 tag in Etsy, incognito test |
| Social post scheduler failure | F6 — post manually from apps |
| Reddit post removed | F7 — reframe as community question, repost |
| Low engagement all channels | Normal Day 1; check Day 3 checkpoint |

Full details: `LAUNCH_DAY_DECISION_TREES_DETAILED.md`

---

## Tier 1 Success Criteria (Launch Happened or Didn't)

From `LAUNCH_DAY_SUCCESS_METRICS.md`:

| Metric | Target | Minimum Threshold |
|--------|--------|-------------------|
| Etsy listings published | 8 | ≥6 |
| Kit broadcast sent | 1 email | Sent |
| Social posts live | 4 | ≥3 |
| GA4 pageviews (full day) | 200+ | ≥50 |

**If all Tier 1 met**: SUCCESSFUL LAUNCH.
**If Etsy <6 published**: FAILURE — core product unavailable.
**All other Tier 1 misses**: Degraded launch, not failure. Continue.

---

*Checklist created: Session 1693, May 27, 2026*
*Pre-flight verification complete: all 8 zone PDFs, 15 influencers, 5 runbooks confirmed PRODUCTION-READY*
