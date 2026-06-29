---
title: "Phase 3 Week 1-2 Verification Templates — Quality Gates and Monitoring"
date: 2026-06-29
version: 1.0
status: active
sprint-window: June 29 – July 13, 2026
cross-references:
  - PHASE_3_WEEK_1_2_DAILY_EXECUTION_CHECKLIST.md (when to run each gate)
  - PHASE_3_WEEK_1_2_ALERT_THRESHOLDS.md (numeric escalation criteria)
  - PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md (photo quality gate source)
  - PHASE_3_LAUNCH_MARKETING_CALENDAR.md (expected metric ranges)
---

# Phase 3 Week 1-2 Verification Templates

**How to use**: Run each template at the checkpoint specified. Record actuals in the Expected vs. Actual grids. All thresholds are numeric — no subjective judgment required. Cross-reference `PHASE_3_WEEK_1_2_ALERT_THRESHOLDS.md` when any metric falls outside the expected range.

---

## TEMPLATE V1 — EMAIL VERIFICATION (Run after each email send)

**Run at**: After each send at 9am ET, then again at 1-hour, 24-hour, and 48-hour checkpoints.

### V1-A: Send Verification (run at 9am ET, within 15 minutes of send)

| Check | Expected | Actual | Pass/Fail |
|-------|----------|--------|-----------|
| Send initiated in Kit | Exactly 9:00am ET | _____ | [ ] |
| Send count matches subscriber count | [your list size] ± 2% | _____ | [ ] |
| Kit campaign status shows "Sent" | "Sent" | _____ | [ ] |
| Test email received in your inbox | Yes, before broadcast | [ ] Yes [ ] No | [ ] |
| [ETSY_LINK] is a live, correct URL | Yes — resolves to bundle | [ ] Yes [ ] No | [ ] |

**Action if any row Fails**: Do not proceed. Check Kit for send error message. Common issues:
- Send count 0: Kit automation did not trigger — manually requeue or re-send
- [ETSY_LINK] broken: send follow-up email with corrected link within 1 hour ("Quick correction on the link in today's email")
- Campaign stuck in "Queued": check Kit account status for sending limits

**Screenshot required**: Take screenshot of Kit dashboard showing sent count and send time. Save to `assets/phase-3-email-screenshots/` with filename `email-[bundle-slug]-send-[date].png`.

---

### V1-B: 1-Hour Delivery Check (run at 10am ET)

| Metric | Expected | Actual | Status |
|--------|----------|--------|--------|
| Delivery rate | >95% | _____% | [ ] GREEN [ ] YELLOW [ ] RED |
| Hard bounce count | <1% of sends | _____ bounces | [ ] GREEN [ ] YELLOW [ ] RED |
| Spam complaint count | <0.1% of sends | _____ complaints | [ ] GREEN [ ] YELLOW [ ] RED |
| Preliminary open rate (1hr) | 8-15% | _____% | [ ] Tracking [ ] Below floor |

**YELLOW thresholds**: Delivery <95% or hard bounces >1% — investigate Kit account health.
**RED thresholds**: Delivery <90% or spam complaints >0.1% — see `PHASE_3_WEEK_1_2_ALERT_THRESHOLDS.md` Alert Level RED.

---

### V1-C: 24-Hour Open Rate Check

Run the following grid for each email after 24 hours from send.

**Email 1 — Women's Health (check at 9am ET, Jun 30)**:

| Metric | Expected Range | Actual | Status |
|--------|---------------|--------|--------|
| Open rate (24hr) | 22-28% | _____% | [ ] GREEN [ ] YELLOW [ ] RED |
| Click-through rate | 3-5% | _____% | [ ] GREEN [ ] YELLOW [ ] RED |
| Etsy click count | [list size × 0.03 to 0.05] | _____ | [ ] Tracking |
| Unsubscribes | <0.5% | _____% | [ ] GREEN [ ] YELLOW |

**Email 2 — Respiratory Health (check at 9am ET, Jul 7)**:

| Metric | Expected Range | Actual | Status |
|--------|---------------|--------|--------|
| Open rate (24hr) | 22-28% | _____% | [ ] GREEN [ ] YELLOW [ ] RED |
| Click-through rate | 3-5% | _____% | [ ] GREEN [ ] YELLOW [ ] RED |
| Etsy click count | [list size × 0.03 to 0.05] | _____ | [ ] Tracking |
| Unsubscribes | <0.5% | _____% | [ ] GREEN [ ] YELLOW |

**Status definitions**:
- GREEN: Within expected range
- YELLOW: 15-22% open rate — log, monitor, run 3-step investigation before next send (see Alert Threshold 2)
- RED: <15% open rate — immediate investigation required (see Alert Threshold 1)

---

### V1-D: 48-Hour Final Baseline (run 48 hours after send)

Open rates stabilize at ~48 hours. This is the authoritative baseline for this campaign.

**Email 1 final baseline (record at 9am ET, Jul 1)**:
- Final open rate: _____ %
- Final CTR: _____ %
- Total Etsy clicks: _____
- Revenue attributed to email (if trackable): $_____ 

**Email 2 final baseline (record at 9am ET, Jul 8)**:
- Final open rate: _____ %
- Final CTR: _____ %
- Total Etsy clicks: _____
- Revenue attributed to email: $_____

**Cross-email comparison** (fill in after Email 2 baseline):

| | Email 1 (Women's Health) | Email 2 (Respiratory) | Delta |
|--|--|--|--|
| Open rate | _____% | _____% | _____ pts |
| CTR | _____% | _____% | _____ pts |
| Etsy clicks | _____ | _____ | _____ |

If Email 2 open rate is more than 5 percentage points lower than Email 1: investigate subject line and list fatigue before Email 3 (Jul 13).

---

## TEMPLATE V2 — SOCIAL VERIFICATION (Run after each post)

**Run at**: Within 10 minutes of scheduled post time, then every 2 hours for 8 hours post-launch.

### V2-A: Post Live Verification (run within 10 minutes of scheduled time)

For each post, confirm it went live within 2 minutes of scheduled time. If a post does not appear within 5 minutes of scheduled time, check the scheduler manually.

| Post | Scheduled Time | Actual Live Time | Platform(s) | Pass/Fail |
|------|---------------|-----------------|-------------|-----------|
| Post 1 | Jun 29, 9:00am ET | _____ | LinkedIn / Instagram / YouTube | [ ] |
| Post 2 | Jun 30, 9:00am ET | _____ | LinkedIn | [ ] |
| Post 3 | Jul 1, 9:00am ET | _____ | Instagram | [ ] |
| Post 4 | Jul 2, 9:00am ET | _____ | LinkedIn / Instagram | [ ] |
| Post 5 | Jul 3, 9:00am ET | _____ | LinkedIn | [ ] |
| Post 6 | Jul 6, 9:00am ET | _____ | LinkedIn / Instagram / YouTube | [ ] |
| Post 7 | Jul 7, 9:00am ET | _____ | YouTube / Instagram | [ ] |
| Post 8 | Jul 8, 9:00am ET | _____ | LinkedIn | [ ] |
| Post 9 | Jul 9, 9:00am ET | _____ | Instagram | [ ] |

**If post does not appear within 5 minutes**: Log in to platform natively and post manually from `PHASE_3_WEEK_1_2_CONTENT_BLOCKS_READY_TO_SHIP.md`. Note the delay in WORKLOG.md. If this happens twice: switch from scheduler to native posting.

**Screenshot required**: Screenshot of each post showing platform, timestamp, and first engagement. Save to `assets/phase-3-social-screenshots/` with filename `post-[number]-[platform]-[date].png`.

---

### V2-B: 2-Hour Engagement Check (run at 11am ET for 9am posts)

Check engagement 2 hours post-publish. Reply to any comments within 4 hours of the comment being posted.

**Platform expected ranges (Week 1-2 baseline — first-time audience build)**:

| Platform | Metric | Expected (2hr) | Expected (8hr) | Expected (24hr) |
|----------|--------|---------------|---------------|----------------|
| LinkedIn | Likes | 5-15 | 15-40 | 25-80 |
| LinkedIn | Comments | 0-3 | 1-5 | 2-8 |
| LinkedIn | Impressions | 200-500 | 400-900 | 600-1,500 |
| Instagram | Likes | 10-30 | 30-80 | 50-150 |
| Instagram | Comments | 0-2 | 1-4 | 2-8 |
| Instagram | Saves | 2-8 | 5-15 | 10-30 |
| YouTube Shorts | Views | 10-50 | 30-150 | 50-300 |
| YouTube Shorts | Likes | 0-5 | 2-10 | 5-20 |

**Note**: These are Week 1-2 first-audience ranges. Launch posts (Posts 1, 6) typically see 1.5-2x these baselines. Video content (Posts 7) typically sees 2-3x these baselines on YouTube.

---

### V2-C: 8-Hour Engagement Log (run at 5pm ET for 9am posts)

Track all 9 posts through the 8-hour window. Record in the grid below.

| Post | Platform | Likes (8hr) | Comments (8hr) | Shares/Saves (8hr) | Reply to comments? | Status |
|------|----------|-------------|---------------|-------------------|-------------------|--------|
| 1 — Women's Health launch | LinkedIn | _____ | _____ | _____ | [ ] | _____ |
| 1 — Women's Health launch | Instagram | _____ | _____ | _____ | [ ] | _____ |
| 1 — Women's Health launch | YouTube | _____ views | _____ | _____ | [ ] | _____ |
| 2 — Red Clover | LinkedIn | _____ | _____ | _____ | [ ] | _____ |
| 3 — Harvest timing | Instagram | _____ | _____ | _____ | [ ] | _____ |
| 4 — Grower feature | LinkedIn | _____ | _____ | _____ | [ ] | _____ |
| 4 — Grower feature | Instagram | _____ | _____ | _____ | [ ] | _____ |
| 5 — Expectorant/demulcent | LinkedIn | _____ | _____ | _____ | [ ] | _____ |
| 6 — Respiratory launch | LinkedIn | _____ | _____ | _____ | [ ] | _____ |
| 6 — Respiratory launch | Instagram | _____ | _____ | _____ | [ ] | _____ |
| 6 — Respiratory launch | YouTube | _____ views | _____ | _____ | [ ] | _____ |
| 7 — Mullein ID | YouTube | _____ views | _____ | _____ | [ ] | _____ |
| 7 — Mullein ID | Instagram | _____ | _____ | _____ | [ ] | _____ |
| 8 — Echinacea species | LinkedIn | _____ | _____ | _____ | [ ] | _____ |
| 9 — Contractor spotlight | Instagram | _____ | _____ | _____ | [ ] | _____ |

**Decision point**: If any post shows 0 likes AND 0 comments at the 8-hour mark: check whether the post is actually live (view natively on the platform, not through the scheduler). Zero engagement at 8 hours is a posting failure signal, not an audience signal.

---

### V2-D: Week 1-2 Social Cumulative (run EOD Jul 13)

| Metric | Target (Week 1-2 total) | Actual | Status |
|--------|------------------------|--------|--------|
| Total LinkedIn engagements | >200 | _____ | [ ] GREEN [ ] YELLOW [ ] RED |
| Total Instagram engagements | >300 | _____ | [ ] GREEN [ ] YELLOW [ ] RED |
| Total YouTube views | >500 | _____ | [ ] Tracking |
| Total engagements across all platforms | >500 | _____ | [ ] GREEN [ ] YELLOW [ ] RED |
| Comments requiring reply | All replied within 4hr | [ ] All replied [ ] _____ missed | [ ] |

---

## TEMPLATE V3 — CONTRACTOR HANDOFF VERIFICATION

**Run at**: Day 3 (photo kickoff), Day 5 (first content submission), Day 7 (Session 1 delivery).

### V3-A: Day 3 Kickoff Call Verification (run Jul 2-3)

Confirm all three contractor tracks have completed kickoff calls.

| Track | Contractor Name | Kickoff Call Completed | Call Date | Deliverable Date Confirmed | Status |
|-------|----------------|----------------------|-----------|--------------------------|--------|
| Photographer | _____ | [ ] Yes [ ] No | _____ | Session 1: Jul 5 | [ ] ON TRACK [ ] AT RISK |
| Writer | _____ | [ ] Yes [ ] No | _____ | First draft: Jul 8 | [ ] ON TRACK [ ] AT RISK |
| Specialist | _____ | [ ] Yes [ ] No | _____ | First section: Jul 10 | [ ] ON TRACK [ ] AT RISK |

**If any kickoff call not completed by EOD Jul 3**: Follow up immediately. If contractor is unreachable by Jul 4: assess contingency path per `PHASE_3_LAUNCH_CONTINGENCY_ROUTING.md`.

---

### V3-B: Day 5 Content Submission Verification (run Jul 6-8)

Photographer: Session 1 due Jul 5. Writer: first draft due Jul 8.

**Photographer Session 1 quality gate** (from `PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md`):

| Gate | Standard | Actual | Pass/Fail |
|------|----------|--------|-----------|
| Image count | Exactly 5 images | _____ | [ ] |
| Image types | Top-down flat-lay, 45° flat-lay, lifestyle ×2, close-up detail | _____ | [ ] |
| Minimum resolution | 2000×2000px on each image | _____ | [ ] |
| White balance | Consistent across all 5 | [ ] Consistent [ ] Inconsistent | [ ] |
| Color space | sRGB on each image | [ ] Yes [ ] No | [ ] |
| Shadow check | No harsh shadows on herbs or guide cover text | [ ] Pass [ ] Fail | [ ] |
| File naming | `respiratory-[type]-[sequence].jpg` | [ ] Correct [ ] Incorrect | [ ] |
| Commercial license | Confirmed per contract | [ ] Confirmed | [ ] |

**Overall Session 1 decision**: [ ] APPROVED — send Template 3A (Praise)  [ ] RESHOOT NEEDED — send Template 3B (Course Correction)  [ ] NOT RECEIVED — trigger contingency

**Writer first draft quality gate**:

| Gate | Standard | Actual | Pass/Fail |
|------|----------|--------|-----------|
| Word count | 3,600 words ± 10% (3,240-3,960) | _____ words | [ ] |
| FTC compliance | All therapeutic claims qualified with evidence-tier framing | [ ] Pass [ ] Issues found | [ ] |
| Latin binomials | Correct for all species | [ ] Pass [ ] Errors found | [ ] |
| Citation count | Minimum 5 per herb (approximate) | _____ | [ ] |
| Contraindication section | Present and complete | [ ] Present [ ] Missing | [ ] |
| CITES sidebar | Present where applicable (Black Cohosh, Goldenseal if present) | [ ] Present [ ] N/A | [ ] |
| Content placeholders | Zero [TBD] or [FILL IN] items | [ ] Clean [ ] _____ placeholders | [ ] |

**Overall writer draft decision**: [ ] APPROVED — send Template 3A (Praise)  [ ] REVISION NEEDED — send Template 3B (Course Correction)  [ ] NOT RECEIVED — contingency

---

### V3-C: Day 7 Handoff Verification (run Jul 5-8)

This is the primary Week 1 contractor checkpoint: all four primary deliverables (3 onboarded tracks + Session 1) should have a clear status.

| Deliverable | Due Date | Received | Decision | Email Sent | Payment Due |
|-------------|----------|----------|----------|------------|-------------|
| Contractor onboarding confirmation (all 6) | Jul 2 | _____ / 6 | [ ] | [ ] | Milestone 1 paid |
| Session 1 photography | Jul 5 | [ ] Yes [ ] No | [ ] Approved [ ] Reshoot | Template 3A or 3B | Milestone 2 on approval |
| Writer first draft (Respiratory) | Jul 8 | [ ] Yes [ ] No | [ ] Approved [ ] Revision | Template 3A or 3B | Milestone 2 on approval |
| Specialist first section | Jul 10 | [ ] Yes [ ] No | [ ] Approved [ ] Revision | Template 3A or 3B | Milestone 2 on approval |

**Week 1 contractor scorecard** (fill in EOD Jul 10):
- Handoffs on schedule (received by due date): _____ / 3
- Handoffs approved without revision: _____ / 3
- Handoffs requiring revision: _____
- Handoffs not received: _____ (trigger contingency if >0)

---

## TEMPLATE V4 — WEEKLY AGGREGATE VERIFICATION (Run EOD Jul 13)

This is the combined Week 1-2 sign-off gate. All three signal categories must be assessed before confirming Week 3 pacing.

### V4-A: Email Signal Aggregate

| Campaign | Open Rate | CTR | Etsy Clicks | Status |
|----------|-----------|-----|-------------|--------|
| Email 1 (Women's Health) | _____% | _____% | _____ | [ ] GREEN [ ] YELLOW [ ] RED |
| Email 2 (Respiratory) | _____% | _____% | _____ | [ ] GREEN [ ] YELLOW [ ] RED |
| Combined total opens | _____ | — | — | Target >250: [ ] Met [ ] Not met |

### V4-B: Social Signal Aggregate

| Platform | Total Engagements (Wk 1-2) | Avg per Post | Status |
|----------|--------------------------|--------------|--------|
| LinkedIn | _____ | _____ | [ ] GREEN [ ] YELLOW [ ] RED |
| Instagram | _____ | _____ | [ ] GREEN [ ] YELLOW [ ] RED |
| YouTube | _____ views | _____ | [ ] Tracking |
| Combined | _____ | — | Target >500: [ ] Met [ ] Not met |

### V4-C: Contractor Signal Aggregate

| Contractor Track | Handoffs Due Wk 1-2 | On Time | Status |
|-----------------|---------------------|---------|--------|
| Photography | 1 (Session 1) | [ ] Yes [ ] No | [ ] ON TRACK [ ] AT RISK |
| Writing | 1 (Respiratory draft) | [ ] Yes [ ] No | [ ] ON TRACK [ ] AT RISK |
| Specialist | 1 (first section) | [ ] Yes [ ] No | [ ] ON TRACK [ ] AT RISK |
| Onboarding (all 6) | 6 of 6 kits received | _____ / 6 | [ ] ON TRACK [ ] AT RISK |
| Combined: 3+ / 4 on schedule | Target: 3/4+ | _____ / 4 | [ ] Met [ ] Not met |

### V4-D: Week 3 Pacing Decision

| Signal Category | Result | Gate |
|----------------|--------|------|
| Email: >250 total opens | [ ] Met [ ] Not met | GREEN requires Met |
| Social: >500 total engagements | [ ] Met [ ] Not met | GREEN requires Met |
| Contractors: 3/4+ on schedule | [ ] Met [ ] Not met | GREEN requires Met |

**Week 3 pacing**:
- All 3 GREEN: Proceed to Week 3 at normal pace (Jul 13 Sleep & Nervines launch confirmed)
- Any YELLOW: Review `PHASE_3_WEEK_1_2_ALERT_THRESHOLDS.md` for compressed timeline option
- Any RED: Log in WORKLOG.md, escalate to contingency assessment

---

*Prepared: June 29, 2026. All thresholds sourced from PHASE_3_LAUNCH_MARKETING_CALENDAR.md (email targets) and PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md (photo quality gates). Expected ranges are Week 1-2 baselines for a first-launch audience — expect Week 3-6 to trend higher as social algorithm momentum builds.*
