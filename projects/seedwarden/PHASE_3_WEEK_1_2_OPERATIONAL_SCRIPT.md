---
title: "Phase 3 Week 1-2 Operational Script — Streamlined Daily Runbook"
date: 2026-06-29
version: 1.0
status: active
sprint-window: June 29 – July 13, 2026
cross-references:
  - PHASE_3_WEEK_1_2_DAILY_EXECUTION_CHECKLIST.md (full day-by-day detail)
  - PHASE_3_WEEK_1_2_CONTENT_BLOCKS_READY_TO_SHIP.md (all copy-paste content)
  - PHASE_3_WEEK_1_2_VERIFICATION_TEMPLATES.md (measurement grids)
  - PHASE_3_WEEK_1_2_ALERT_THRESHOLDS.md (escalation criteria)
---

# Phase 3 Week 1-2 Operational Script

**Purpose**: Streamlined human-friendly runbook for operating Phase 3 Week 1-2. Daily overhead target: 30-45 minutes. This script reduces decision fatigue to the minimum — everything is pre-decided, pre-written, and pre-scheduled. Your job is execution, not content creation.

**Source of truth for each task**:
- Content: `PHASE_3_WEEK_1_2_CONTENT_BLOCKS_READY_TO_SHIP.md`
- Metrics verification: `PHASE_3_WEEK_1_2_VERIFICATION_TEMPLATES.md`
- Go/no-go decisions: `PHASE_3_WEEK_1_2_ALERT_THRESHOLDS.md`
- Day-by-day detail: `PHASE_3_WEEK_1_2_DAILY_EXECUTION_CHECKLIST.md`

---

## DAILY OPERATING CADENCE

Three sessions per day. Total: 30-45 minutes.

| Session | Time | Duration | Primary Activity |
|---------|------|----------|-----------------|
| Morning brief | 8:00-8:15am ET | 5-15 min | Pull yesterday's metrics, verify today's pre-send checklist |
| Execution window | 9:00-9:15am ET | 10-15 min | Send email and/or post social content — this is fixed time |
| Evening review | 6:00-6:20pm ET | 15-20 min | Log today's metrics, check contractor status, note escalations |

On contractor deliverable days (Jul 5, Jul 8), add 20-30 minutes for quality gate review. These happen 2 times in Weeks 1-2 and are the only days overhead exceeds 45 minutes.

---

## MORNING BRIEF (5-15 minutes, 8:00am ET)

Run this every morning before 8:30am ET.

**Step 1 — Pull yesterday's metrics** (3 min):
- Open Kit dashboard: record prior email open rate and click rate in WORKLOG.md (if an email was sent yesterday)
- Open social platform notifications: scan for comments requiring reply
- Scan contractor email inbox: any new submissions or questions?

**Step 2 — Verify today's pre-send checklist** (5-10 min — only on email/post days):
On days when an email or social post ships:
- Confirm [ETSY_LINK] is filled in (not a placeholder) — open the link in a browser and verify it resolves
- Confirm Kit campaign is set to correct send time (9:00am ET) and audience (full list)
- Confirm social post is scheduled in scheduler for 9:00am ET on correct platforms
- Send yourself a test email if any doubt about rendering

On days with no email and no scheduled post, morning brief is 3 minutes (metrics only).

**Step 3 — Check for escalations** (2 min):
Review `PHASE_3_WEEK_1_2_ALERT_THRESHOLDS.md` relevant gates for today's date. Any thresholds triggered yesterday that require follow-up action today?

---

## 9AM ET EXECUTION WINDOW (10-15 minutes, fixed)

This window is the single most important operational discipline in Phase 3. Every email and social post ships at 9:00am ET. The 9am window is fixed because:
- Email open rates are highest for the 9am-12pm ET window for this audience demographic
- Social algorithm boosts are partially a function of consistent posting schedule
- Contractors and Etsy shoppers in all US time zones are active from 9am ET forward

**Standard execution sequence** (10 minutes):

1. Open Kit.com dashboard (1 min): confirm email campaign is dispatched (not stuck in queue)
2. Open scheduler (Buffer/Later/native) (2 min): confirm social posts are live on all scheduled platforms
3. Verify Etsy link is live (1 min): click through from email template to bundle listing — confirm $[price] shows and "Add to cart" works
4. Screenshot verification (2 min): screenshot Kit send count, screenshot social posts from platform native view (not scheduler)
5. Log screenshots (1 min): save to `assets/phase-3-email-screenshots/` and `assets/phase-3-social-screenshots/`
6. Scan for immediate engagement (3 min): any comments on social posts? Reply or note for follow-up.

On non-send days (no email, no post): skip execution window entirely. Use those 10 minutes for contractor follow-up or quality gate review.

---

## MID-DAY CHECK (5 minutes, 12pm ET — only on email send days)

Run at noon on Jun 29, Jul 6, and Jul 13 only.

- Open Kit dashboard: confirm delivery rate >95% (Gate 1 — see `PHASE_3_WEEK_1_2_ALERT_THRESHOLDS.md`)
- Check preliminary open rate (3-hour): note but do not act on — wait for 24-hour baseline
- Scan Etsy: any views/sales since this morning?

Total time: 5 minutes. Skip on non-send days.

---

## EVENING REVIEW (15-20 minutes, 6pm ET)

Run every evening during active weeks. This is where metrics are recorded and decisions are logged.

**Step 1 — Email metrics** (5 min, only on days 1 and 2 after a send):
- Open Kit dashboard
- Record in WORKLOG.md:
  - Date and email campaign name
  - Open rate (% and raw count)
  - Click rate (% and raw count)
  - Bounces and unsubscribes
- Compare against threshold in `PHASE_3_WEEK_1_2_ALERT_THRESHOLDS.md`
- If YELLOW or RED: log escalation template in WORKLOG.md and execute response steps

**Step 2 — Social engagement** (5 min):
- Open each social platform (LinkedIn, Instagram, YouTube)
- Record in WORKLOG.md: likes, comments, saves/shares for each active post
- Reply to any unanswered comments (4-hour reply SLA)
- If any post has zero engagement at 8 hours: run Gate 4 response

**Step 3 — Contractor status** (5 min on deliverable days, 2 min otherwise):
- Check for any contractor emails received today
- If a deliverable was due today: confirm receipt and log status (received / not received)
- Reply to any contractor questions (24-hour SLA from when they sent)
- If a deliverable is missing: log in WORKLOG.md, determine follow-up timing

**Step 4 — Next-day prep** (3 min):
- Confirm tomorrow's email is scheduled (if applicable)
- Confirm tomorrow's social post is scheduled (if applicable)
- Note any items requiring morning brief attention

---

## CONTRACTOR INTERACTION PROTOCOL

Contractors run on a parallel track. This section describes exactly when to touch each contractor and for how long.

**Week 1 (Jun 29 – Jul 5): Onboarding window**

| Day | Date | Action | Time Required |
|-----|------|--------|--------------|
| Day 2 | Jul 1 | Send onboarding kits to all 6 contractors | 15-20 min (pre-populated templates) |
| Day 2 | Jul 1 | Send kickoff call invites | 10 min |
| Days 3-4 | Jul 2-3 | Conduct kickoff calls (3 tracks) | 70 min total (20+30+20) |
| Day 3 | Jul 2-4 | Answer any contractor questions | <5 min per question, 24hr SLA |
| Day 5 | Jul 5 | Review Session 1 photos | 20-30 min (quality gate checklist) |
| Day 5 | Jul 5 | Send praise or correction email | 10-15 min (pre-populated template, fill in specifics) |

**Week 2 (Jul 6 – Jul 13): Active production window**

| Day | Date | Action | Time Required |
|-----|------|--------|--------------|
| Day 7 | Jul 6 | Weekly check-in to all 6 contractors | 15-20 min (pre-populated template, 6× sends) |
| Day 8 | Jul 7 | Session 1 final approval decision | 10 min |
| Day 9 | Jul 8 | Writer first draft receipt check | 5 min |
| Days 9-11 | Jul 8-10 | Writer first draft review (48hr window) | 45-60 min total (spread across 3 days) |
| Day 11 | Jul 10 | Send writer approval or revision notes | 10-15 min |
| Day 11 | Jul 10 | Process Milestone 2 payment (photo, if Session 1 approved) | 5 min |
| Days 12-13 | Jul 11-12 | Session 2 photo receipt and review | 20 min |

**Total contractor interaction time, Weeks 1-2**: approximately 4-5 hours spread across 15 days. This is the preparation for weeks of quality content — front-loaded investment.

---

## WEEKLY RHYTHM (FRIDAYS)

Every Friday, spend 20-30 minutes on a brief weekly aggregate review.

**Friday Jul 4 (end of Week 1)**:
- Aggregate email open rate and social engagement totals so far
- Confirm all kickoff calls complete and any blockers resolved
- Confirm Respiratory bundle is live on Etsy draft, ready for Jul 6 launch
- Note Week 1 to-dos for the weekend (Session 1 photo review)
- Time: 20 minutes

**Friday Jul 11 (end of Week 2)**:
- Aggregate Week 1-2 combined metrics — run `PHASE_3_WEEK_1_2_VERIFICATION_TEMPLATES.md` V4 (Weekly Aggregate)
- Confirm Sleep & Nervines bundle is upload-ready for Jul 13
- Confirm all contractor Week 1-2 deliverables have a clear status (received/approved/revision/escalated)
- Log Week 1-2 summary in WORKLOG.md (4-5 lines: email results, social results, contractor status, one concern, Week 3 pacing decision)
- Time: 30 minutes

---

## DECISION AUTHORITY

Not every situation requires escalation. This section defines what you can decide alone and what requires logging in WORKLOG.md.

**Decide alone (no log required)**:
- Sending emails and posts at scheduled times
- Approving a contractor deliverable that clearly passes all quality gates
- Replying to social media comments
- Minor subject line adjustments (same topic, different wording) for future emails

**Log in WORKLOG.md (no escalation, just record)**:
- Any metric that hits YELLOW threshold
- Any contractor deliverable received more than 24 hours late (but received)
- Any Etsy technical issue that was resolved
- Any social post that posted late (but posted correctly)
- Decision to use A/B subject line test for Email 2 or Email 3

**Log and execute contingency response**:
- Any metric that hits RED threshold
- Any contractor deliverable not received within 48 hours of due date
- Any Kit deliverability issue affecting >10% of sends
- Design lock missed (all Canva covers not final by EOD Jul 3)

---

## TIME BUDGET SUMMARY

| Activity | Days Active | Time per Day | Total Time (15 days) |
|----------|-------------|-------------|---------------------|
| Morning brief | 15 | 5-15 min | ~90 min |
| Execution window (email/post days) | 9 | 10-15 min | ~115 min |
| Mid-day check (email send days) | 3 | 5 min | 15 min |
| Evening review | 15 | 15-20 min | ~250 min |
| Contractor interaction (onboarding, reviews) | 8 | 10-70 min | ~300 min |
| Weekly aggregate reviews (Fridays) | 2 | 20-30 min | 50 min |
| **Total** | | | **~820 min (~13.7 hours across 15 days)** |
| **Per day average** | | | **~55 min** |
| **Excluding contractor-heavy days (Jul 2-3, Jul 5, Jul 8-10)** | | | **~30-35 min/day** |

Contractor-heavy days (kickoff calls, photo review, draft review) average 90-120 minutes each. There are 5 such days in Weeks 1-2. Every other day averages 30-35 minutes.

**Versus unoptimized baseline**: Without pre-written content blocks, each email send requires 45-90 minutes of content creation. Each social post requires 20-45 minutes of drafting. Over 15 days with 9 content deployment events and 3 email sends: 12-18 hours of content-creation overhead alone, plus execution and monitoring. Pre-prepared content reduces this to the 13-14 hour total above, with overhead concentrated on high-value contractor review and quality gate verification rather than content drafting.

---

## WORKLOG.MD ENTRY TEMPLATE (copy at end of each day)

```
### [DATE] — [DAY NAME]

**Email** (if applicable):
- Campaign: [name]
- Send time: [time ET]
- Send count: [number]
- Delivery rate: [%]
- Open rate (24hr or preliminary): [%]
- CTR: [%]
- Status: [ ] GREEN [ ] YELLOW [ ] RED

**Social**:
- Posts live today: [Post number(s) and platform(s)]
- LinkedIn engagement: [likes / comments / impressions]
- Instagram engagement: [likes / comments / saves]
- YouTube engagement: [views / likes]
- Comments replied to: [ ] All [ ] [number] pending

**Contractors**:
- Deliverables received today: [describe or "none"]
- Deliverables reviewed/approved today: [describe or "none"]
- Contractor questions answered: [ ] Yes [ ] None today
- Milestone payments processed: [describe or "none"]

**Escalations**:
- Any YELLOW or RED thresholds triggered: [describe or "none"]
- Actions taken: [describe or "none"]

**Tomorrow's prep**:
- Email scheduled: [ ] Yes [ ] No / N/A
- Social post scheduled: [ ] Yes [ ] No / N/A
- Contractor action needed: [describe]
```

---

## WEEK 3 PACING TRIGGER

At EOD Jul 13, after the Sleep & Nervines launch executes, run the Week 1-2 retrospective (from `PHASE_3_WEEK_1_2_DAILY_EXECUTION_CHECKLIST.md`, Day 14).

**The single decision at Week 3 entry**:

Combined Week 1-2 results (record actuals):
- Email combined opens: _____ (target >250)
- Social combined engagements: _____ (target >500)
- Contractors on schedule: _____ / 4 (target 3+/4)

**If all three targets met**: Week 3 proceeds at normal pace. Sleep & Nervines launch confirmed Jul 13 (already done). Immunity launch Jul 20. No changes to timeline.

**If any target missed**: Review `PHASE_3_WEEK_1_2_ALERT_THRESHOLDS.md` Gate 8 compressed timeline option before starting Week 3 morning brief on Jul 14.

---

*Prepared: June 29, 2026. Operational overhead calibrated based on pre-populated content (PHASE_3_WEEK_1_2_CONTENT_BLOCKS_READY_TO_SHIP.md) removing content-creation from the daily overhead budget. The 30-45 min/day target assumes all content blocks are loaded into Kit and social scheduler before Jun 29. If pre-loading is not complete by Jun 29 morning, add 2-3 hours of scheduler setup on Day 0.*
