---
title: "Week 1-2 Email Operations Runbook"
project: career-training
phase: "2"
created: 2026-06-29
status: execution-ready
confidence: 90%
period: "Days 8-21 post-Phase-1-launch"
prerequisite: "KIT_ACCOUNT_SETUP_EXECUTION_CHECKLIST.md — all steps complete and smoke test passed"
---

# Week 1-2 Email Operations Runbook

**Purpose**: Daily and weekly operating procedures for Kit email infrastructure during Days 8-21 after Phase 1 launch. Covers monitoring routines, delivery verification, open/click tracking, subscriber behavior analysis, and troubleshooting templates.

**Scope**: This runbook covers the period after Kit setup is complete and the first real subscribers are arriving. It does not cover Kit account creation (KIT_ACCOUNT_SETUP_EXECUTION_CHECKLIST.md) or welcome email copy (WELCOME_SEQUENCE_DRAFT.md).

**Time investment**: 10-15 minutes per day for daily checks; 30-45 minutes for weekly reviews.

---

## Operating Rhythm

| Cadence | Duration | Activities |
|---------|----------|-----------|
| Daily check | 10-15 min | Kit subscriber count, email delivery confirmation, reply monitoring |
| Mid-week check (Wednesday) | 15 min | GA4 traffic source review, module click-through rate |
| End-of-week review | 30-45 min | Compile week's metrics, PASS/FAIL assessment, next week prep |

---

## Daily Check Procedure

**When**: Each morning, before any other work. Takes 10-15 minutes.

### Daily Kit Check (5 minutes)

1. Go to https://app.kit.com
2. Dashboard shows subscriber count prominently — record today's number in the daily log (below)
3. Click Subscribers icon → check for new subscribers since yesterday
4. For each new subscriber:
   - Verify correct tag is applied (should match which form they submitted)
   - If subscriber has `generic` tag: normal (they used the homepage form)
   - If subscriber has NO tag at all: this is a problem — see Troubleshooting Section A
5. Check Automations or Sequences: click your active automation → look for any subscribers stuck in "error" state or not progressing through steps

**What to record in the daily log**:
```
Day N | Date: __________ | New subscribers today: ___ | Total: ___
  Tags: residential-gc: ___ | industrial-gc: ___ | specialty-sub: ___ | generic: ___
  Any email delivery errors: [ ] None [ ] Yes (detail: ___)
  Any subscriber without a tag: [ ] None [ ] Yes (count: ___)
  Any email replies received: [ ] None [ ] Yes (note below)
```

### Daily GA4 Check (3 minutes)

1. Go to https://analytics.google.com → select your Construction Career Training property
2. Click Reports → Overview
3. Record today's numbers:
   - Users (unique)
   - Sessions
   - Top traffic source today

**Trigger to escalate**: If sessions drop to zero for 2+ consecutive days, the site may be down. Visit the live URL from a different device or browser to confirm.

### Daily Inbox Check (2 minutes)

Check the reply-to email address you set in Kit Settings. Any subscriber who replies to the welcome sequence is a high-engagement signal.

**When a reply arrives**:
- Reply within 24 hours (even if brief)
- Replies are typically questions about: which module to start with, whether content is updated, whether there's a PDF version
- Note the question topic in your reply tracker — repeat questions become FAQ entries or LinkedIn post ideas

**Reply response templates**:

Template A — "Which module should I start with?":
```
Thanks for writing — that's the right question to ask early.

For [Residential GC / Industrial GC / Specialty Sub] path: start with Module [X].
It's the one that covers [brief description of module's practical value].

From there, [Module Y] builds directly on it.

Let me know how it goes — always good to hear from someone actually in the field.

[Your name]
```

Template B — "Is there a PDF version?":
```
The full modules are on the site (no PDF right now), but the [California GC 
Pre-Licensing Checklist / Construction Drawing Quick-Reference Card] is a 
downloadable PDF — you can get it at [SIGNUP URL] if you haven't already.

Working on adding more printable resources. Anything specific you'd want 
to download and keep on the job site?

[Your name]
```

Template C — "When was this last updated?":
```
Good question. Module 14 (Site Safety / Cal/OSHA) was updated to reflect 
the July 2025 fall-protection height change (now 6 ft trigger for residential).

I update modules when regulations change. The next planned update is 
Module 12 (GC Business Setup) to reflect 2026 CSLB fee schedule changes.

What prompted the question — are you working on something specific?

[Your name]
```

---

## Daily Log Template — Days 8-21

Copy this table into a personal tracking spreadsheet. Fill in each row daily.

```
DAILY EMAIL OPERATIONS LOG — PHASE 2 WEEKS 1-2
================================================

Day 8  | Date: ___ | Sessions: ___ | New subs: ___ | Total subs: ___ | Source: ___
Day 9  | Date: ___ | Sessions: ___ | New subs: ___ | Total subs: ___ | Source: ___
Day 10 | Date: ___ | Sessions: ___ | New subs: ___ | Total subs: ___ | Source: ___
Day 11 | Date: ___ | Sessions: ___ | New subs: ___ | Total subs: ___ | Source: ___
Day 12 | Date: ___ | Sessions: ___ | New subs: ___ | Total subs: ___ | Source: ___
Day 13 | Date: ___ | Sessions: ___ | New subs: ___ | Total subs: ___ | Source: ___
Day 14 | Date: ___ | Sessions: ___ | New subs: ___ | Total subs: ___ | Source: ___
       | WEEK 1 TOTALS: Sessions: ___ | New subs: ___ | Conversion: ___% |
Day 15 | Date: ___ | Sessions: ___ | New subs: ___ | Total subs: ___ | Source: ___
Day 16 | Date: ___ | Sessions: ___ | New subs: ___ | Total subs: ___ | Source: ___
Day 17 | Date: ___ | Sessions: ___ | New subs: ___ | Total subs: ___ | Source: ___
Day 18 | Date: ___ | Sessions: ___ | New subs: ___ | Total subs: ___ | Source: ___
Day 19 | Date: ___ | Sessions: ___ | New subs: ___ | Total subs: ___ | Source: ___
Day 20 | Date: ___ | Sessions: ___ | New subs: ___ | Total subs: ___ | Source: ___
Day 21 | Date: ___ | Sessions: ___ | New subs: ___ | Total subs: ___ | Source: ___
       | WEEK 2 TOTALS: Sessions: ___ | New subs: ___ | Conversion: ___% |
```

---

## Weekly Review Procedure — End of Week 1 (D+14) and End of Week 2 (D+21)

**When**: After the last daily check of the week. Takes 30-45 minutes.

### Part 1: Pull Email Performance Metrics from Kit

**Where to find these in Kit**:
- Automation analytics: Automations → your automation → subscriber count per step
- Sequence analytics: Sequences → your sequence → click "Analytics" or "Stats"
- Individual email analytics: click into a specific email within the sequence → see open rate, click rate

**Metrics to pull at D+14**:

| Metric | How to Find | This Week | Target | PASS/FAIL |
|--------|------------|-----------|--------|-----------|
| Day 0 email open rate | Sequence → Email 1 analytics → Open rate | ___% | ≥35% | |
| Day 3 email open rate | Sequence → Email 2 analytics → Open rate | ___% | ≥28% | |
| Day 3 module link click rate | Email 2 → Click rate on module link | ___% | ≥20% | |
| Total subscribers | Dashboard or Subscribers view → total count | ___ | ≥15 by D+21 | |
| Unsubscribe rate | Sequence analytics → Unsubscribe count / Total sent | ___% | <5% | |
| Bounce rate (email delivery) | Look for "hard bounced" or "failed" subscribers | ___% | <2% | |

**Metrics to pull at D+21** (same as above, plus):

| Additional Metric | How to Find | Value | Target | PASS/FAIL |
|-------------------|------------|-------|--------|-----------|
| Day 7 email open rate | Sequence → Email 3 analytics | ___% | ≥28% | |
| Day 7 LinkedIn click rate | Email 3 → click rate on LinkedIn link | ___% | Informational | |
| Path distribution | Subscribers → filter by each path tag | Residential: ___% | No single path > 75% | |
| Subscribers who opened 2+ emails | Subscribers → filter by "opened 2+ emails" | ___ | Informational | |

### Part 2: Pull Site Traffic from GA4

**Where to find these in GA4**:
- Reports → Acquisition → Traffic acquisition (for traffic sources)
- Reports → Engagement → Pages and screens (for module engagement)
- Reports → Engagement → Events (for `email_signup_conversion` event count)

| GA4 Metric | This Week | Prior Week | Trend |
|-----------|-----------|-----------|-------|
| Total sessions | ___ | ___ | Up/Down/Flat |
| Unique users | ___ | ___ | |
| Homepage engagement rate | ___% | ___% | |
| Email signup conversion events | ___ | ___ | |
| Top traffic source | ___ | ___ | |
| Top module page views | ___ | ___ | |
| LinkedIn referral sessions | ___ | ___ | |

### Part 3: PASS/FAIL Assessment

Use the metric targets from PHASE_2_LAUNCH_TIMELINE_WEEK_0_8.md and PHASE_2_GROWTH_STRATEGY_AND_COHORT_ANALYSIS.md failure triggers:

**Week 1 (D+14) PASS thresholds** — every metric below must be PASS or investigated:

| Check | Threshold | Result | Status |
|-------|-----------|--------|--------|
| Email capture rate | ≥2% of sessions | ___% | PASS / FAIL |
| Day 0 open rate | ≥35% | ___% | PASS / FAIL |
| Day 3 open rate | ≥28% | ___% | PASS / FAIL |
| No spam folder placement | 0 test emails in spam | | PASS / FAIL |
| Automation delivering correctly | All 3 sequence emails triggering | | PASS / FAIL |
| Subscriber tag accuracy | All subscribers have a path tag | | PASS / FAIL |

**Week 2 (D+21) PASS thresholds**:

| Check | Threshold | Result | Status |
|-------|-----------|--------|--------|
| Total subscribers | ≥15 | ___ | PASS / FAIL |
| Day 0 open rate sustained | ≥35% for subscribers who joined Week 2 | ___% | PASS / FAIL |
| Day 7 open rate (subscribers from Week 1) | ≥28% | ___% | PASS / FAIL |
| Module click rate | ≥20% from Day 3 email | ___% | PASS / FAIL |
| Unsubscribe rate | <5% of total sent | ___% | PASS / FAIL |
| LinkedIn referral sessions | ≥5 if any LinkedIn posts published | ___ | PASS / FAIL |

### Part 4: Next Week Prep

After reviewing metrics, complete these actions before ending the weekly review:

**D+14 (end of Week 1)**:
- [ ] Document any FAIL metrics in the decision log (below)
- [ ] If email capture rate FAIL: schedule form placement adjustment before next week
- [ ] If open rate FAIL: draft A/B subject line variant for next 25 subscribers
- [ ] Draft first 3 LinkedIn posts for Week 3 (case study format — see PHASE_2_LAUNCH_TIMELINE_WEEK_0_8.md Week 3-4 schedule)
- [ ] Identify highest-engagement module from GA4 → this becomes the topic of first LinkedIn post

**D+21 (end of Week 2)**:
- [ ] Fill in the Week 1-2 Metrics Snapshot from PHASE_2_LAUNCH_TIMELINE_WEEK_0_8.md
- [ ] Complete PHASE_2_HANDOFF_DOCUMENT.md Section 3 (Week 1 monitoring triggers)
- [ ] Confirm LinkedIn posting cadence is ready for Week 3 launch
- [ ] Send first outreach email to construction association (see PHASE_2_LAUNCH_TIMELINE_WEEK_0_8.md Week 3-4 partnership outreach section)
- [ ] Confirm re-engagement automation is ready (to be activated at D+30 for subscribers who joined Week 1)

---

## Email Delivery Troubleshooting

### Troubleshooting Section A: Subscriber Has No Tag

**Symptom**: New subscriber appears in Kit without any path tag (tag column is empty).

**Cause**: Usually means the subscriber submitted the generic homepage form, which should apply the `generic` tag. If even the `generic` tag is missing, the form was not configured correctly.

**Fix**:
1. Open the form in Kit that the subscriber used (check subscriber's source in their profile)
2. Go to the form's Incentive or Settings tab
3. Confirm the correct tag is selected in "Add tag" field
4. Click Save
5. Apply the missing tag to the affected subscriber manually: open subscriber profile → click "Add tag" → select the appropriate path tag
6. Test: submit the form again with a test email and confirm the tag appears

**Prevention**: After any form setting change, always submit a test subscription to verify the tag is applied.

---

### Troubleshooting Section B: Welcome Email Not Received

**Symptom**: New subscriber appears in Kit with correct tag but reports no welcome email; or you notice in Kit that the automation/sequence did not advance.

**Diagnosis steps**:
1. Check Kit → Subscribers → find the subscriber → look at their email history
2. Does Kit show the Day 0 email as "sent" or "failed"?

**If shown as "sent" but subscriber reports not receiving it**:
- Ask the subscriber to check spam folder and "Promotions" tab
- Check: was the subscriber's email address typed correctly? (Kit shows the address in the subscriber profile)
- If sent to a corporate email (Outlook): Microsoft filtering can delay Kit emails by 15-30 minutes on new sender domains; also possible it went to a "Focused Inbox" category
- If the email is not in spam and did not arrive after 30 minutes: suspect temporary email server issue. Ask subscriber to re-subscribe with the same email; Kit should re-trigger the sequence.

**If shown as "failed" or not shown at all**:
- The automation/sequence may not have triggered. Check:
  - Is the form linked to the automation trigger? (Automations → your automation → check trigger settings)
  - Is the Sequence linked to the form? (Forms → your form → check Incentive settings for sequence enrollment)
- If the link is broken, reconnect it and apply the subscriber to the sequence manually: Subscribers → find the subscriber → "Add to sequence" → select the welcome sequence

**If Kit shows no record of the email** (not in sent, not in failed):
- The subscriber was not added to the correct sequence
- Open subscriber profile → "Subscriptions" section → add them manually to the correct path sequence

---

### Troubleshooting Section C: Email Landing in Spam

**Symptom**: Test subscriber or real subscriber reports the welcome email landed in spam or promotions.

**Immediate actions**:

1. Ask subscriber to: (a) mark the email "Not Spam," (b) add your sender address to their contacts. Both actions improve inbox placement for future emails from your domain.

2. Test your own email with Mail-Tester.com (free tool):
   - Go to mail-tester.com — it generates a unique test email address
   - In Kit, send a broadcast to that test address
   - Return to Mail-Tester after 2 minutes and check your spam score
   - Target: 8/10 or higher
   - Score below 7/10: investigate the specific issues Mail-Tester identifies

3. Check sender domain authentication status:
   - Kit Settings > Email Sending > look for SPF/DKIM/DMARC verification status
   - If domain is not authenticated: go to your DNS provider and add the records Kit provides
   - If domain is already authenticated but emails still go to spam: the content may be triggering filters

4. Review subject lines for spam trigger words:
   - Avoid: "FREE," "GUARANTEE," "CLICK HERE," excessive punctuation (!!), all-caps words
   - The current subject lines in WELCOME_SEQUENCE_DRAFT.md are clean — if you modified them, review your edits
   - Tool: SpamAssassin subject line tester (available at various online tools)

5. Check Kit's sender reputation:
   - Kit Settings > account section — look for any deliverability warnings
   - If Kit shows a warning about high complaint rate, the issue may be with Kit's shared IP reputation (not your specific content). Contact Kit support (note: free plan has no email support — use the community forum).

**If spam problem persists after 48 hours and sender domain is authenticated**:
- The root cause is likely the email content itself or Kit's shared IP reputation for your region
- Run the full EMAIL_DELIVERABILITY_TEST_RESULTS.md test protocol to identify the specific failure point
- Escalation path: see EMAIL_DELIVERABILITY_TEST_RESULTS.md Section "If Test Fails" for Failure Mode 1

---

### Troubleshooting Section D: Open Rate Below 25%

**Symptom**: Day 0 welcome email open rate is below 25% after 20+ sends.

**Diagnosis**: Low open rate at Day 0 is almost always a subject line or sender name problem. The email content does not matter if it is never opened.

**A/B test procedure** (manual, since Kit automation A/B is paid-only):
1. For the next 30 subscribers:
   - First 15 subscribers: send current subject line ("You're in. Here's where to start.")
   - Next 15 subscribers: send alternate subject line ("Your construction career training is ready")
2. After 30 sends, compare open rates in Kit
3. If neither subject line reaches 35% open rate, test a third variant: "Quick note — your first module"

**Other open rate issues and fixes**:

| Cause | Diagnosis | Fix |
|-------|-----------|-----|
| Sender name unfamiliar | Subscriber doesn't recognize "Construction Career Training" as the sender | Change sender name to your personal name (first and last) — people open emails from people, not brands |
| Apple Mail Privacy inflation | Apple pre-fetches tracking pixels, inflating opens artificially | Not a real open rate problem — if 40%+ of subscribers use Apple Mail, your reported open rate is higher than actual; this is a known limitation of all ESPs |
| Emails going to Promotions tab | Gmail categorizes as promotional; many subscribers never check Promotions | Include a "Move this email to your Primary tab" instruction in the Day 0 email footer |
| Wrong audience acquired | Subscribers signed up for the lead magnet but are not interested in the curriculum | Review the lead magnet — if the checklist attracts people who just want the PDF and won't engage with the curriculum, the magnet is working against you. Test removing the mandatory email gate on the PDF. |

---

### Troubleshooting Section E: High Unsubscribe Rate

**Symptom**: More than 5% of total email sends result in unsubscribes in a 7-day window.

**Context**: Some unsubscribes are normal and healthy — people who are not the right audience should self-select out. An unsubscribe rate under 5% is acceptable. Over 5% indicates the emails are not matching what subscribers expected when they signed up.

**Diagnosis questions**:
1. Which email in the sequence generates the most unsubscribes? (Check Kit sequence analytics per email step)
2. At what day does the unsubscribe spike occur?
   - Day 0-2 unsubscribe: The lead magnet attracted the wrong audience (they wanted the PDF, not the curriculum)
   - Day 7 unsubscribe: The LinkedIn invitation in the Day 7 email felt pushy; soften the ask
   - Day 3 unsubscribe: The safety-focused module excerpt is not matching subscriber expectations; test a different module topic for the Day 3 email

**Fix by unsubscribe timing**:
- High Day 0-2 unsubscribes: Review the signup form copy. If the form over-promises ("Join 1,000 construction professionals") or under-describes what they are signing up for, revise it. The form should describe exactly what the email sequence covers.
- High Day 7 unsubscribes: Soften the LinkedIn ask. Change "Follow us on LinkedIn" to "We post case studies on LinkedIn if you want them outside the inbox" — less pushy, same information.
- Uniform high unsubscribes across all days: The fundamental content is not what this audience wants. Survey the leavers: add a Kit "unsubscribe reason" question (Kit supports this) and review responses for patterns.

---

## Metrics Baseline Tracker — Week 1-2

Complete this at D+21. This baseline is used to calibrate Week 3-8 targets and interpret deviations.

```
BASELINE METRICS — D+21 (end of Week 2)
=========================================

SUBSCRIBERS:
  Total subscribers: ___
  Residential GC: ___  (___%)
  Industrial GC:  ___  (___%)
  Specialty Sub:  ___  (___%)
  Generic:        ___  (___%)
  Email capture rate (subscribers / total site sessions): ___%

EMAIL PERFORMANCE:
  Day 0 open rate (all paths, average): ___%
  Day 3 open rate (all paths, average): ___%
  Day 7 open rate (all paths, average): ___%
  Day 3 module link click rate: ___%
  Unsubscribe rate (% of all emails sent): ___%
  Bounce rate (hard bounces): ___%
  Any spam folder placement: [ ] None [ ] Yes (investigate)

SITE TRAFFIC:
  Total sessions D+8 to D+21: ___
  Average daily sessions: ___
  Top traffic source: ___
  LinkedIn referral sessions: ___
  Top module by page views: ___

PASS/FAIL SUMMARY:
  Email capture ≥2%:         [ ] PASS [ ] FAIL
  Day 0 open rate ≥35%:      [ ] PASS [ ] FAIL
  Day 3 open rate ≥28%:      [ ] PASS [ ] FAIL
  Module click rate ≥20%:    [ ] PASS [ ] FAIL
  Total subscribers ≥15:     [ ] PASS [ ] FAIL

DECISION GATES:
  Proceed to LinkedIn launch (Week 3)?  [ ] YES [ ] NO (resolve: ___)
  Any open items before Week 3?         [ ] None [ ] Yes (list: ___)
```

---

## Escalation Protocol

If any of the following occur, escalate immediately (do not wait for the end-of-week review):

| Escalation Trigger | Immediate Action | Document In |
|-------------------|-----------------|------------|
| Kit account suspended or locked | Contact Kit community forum; review recent sends for spam complaints; do not send any new emails until resolved | This runbook + EMAIL_DELIVERABILITY_TEST_RESULTS.md |
| All emails going to spam across all providers | Run Mail-Tester.com immediately; pause new subscriber acquisition until resolved | EMAIL_DELIVERABILITY_TEST_RESULTS.md Failure Mode 1 |
| Automation completely stops firing | Check Kit status page (status.kit.com); if Kit is operational, rebuild automation from scratch | KIT_ACCOUNT_SETUP_EXECUTION_CHECKLIST.md Step 8 |
| 10+ consecutive days, zero new subscribers with live forms | Verify forms are rendering on live site; submit a test from incognito mode; confirm GA4 is tracking signup events | KIT_ACCOUNT_SETUP_EXECUTION_CHECKLIST.md Step 9 |
| Open rate below 15% sustained over 14 days | Major subject line overhaul required; contact a single known subscriber and ask them to forward the email to their work email to test placement | Troubleshooting Section D above |

---

## Sources

- WELCOME_SEQUENCE_DRAFT.md — email copy for all days and path variants
- KIT_ACCOUNT_SETUP_EXECUTION_CHECKLIST.md — setup procedures this runbook depends on
- PHASE_2_LAUNCH_TIMELINE_WEEK_0_8.md — weekly milestones and KPI targets
- EMAIL_DELIVERABILITY_TEST_RESULTS.md — deliverability benchmarks and troubleshooting
- PHASE_2_GROWTH_STRATEGY_AND_COHORT_ANALYSIS.md — failure triggers and escalation thresholds
- PHASE_2_ENROLLMENT_FUNNEL_ARCHITECTURE.md — funnel stage metrics and failure mode diagnosis
- [Kit Sequence Analytics — Kit Help Center](https://help.kit.com/en/articles/2502585-sequence-analytics)
- [Kit Status Page](https://status.kit.com)
- [Mail-Tester.com — Email Spam Score Tool](https://www.mail-tester.com)
- [Email Marketing Benchmarks 2026 — Mailchimp](https://mailchimp.com/resources/email-marketing-benchmarks/)
- [Construction Industry Email Open Rate Benchmarks — Campaign Monitor 2025](https://www.campaignmonitor.com/resources/guides/email-marketing-benchmarks/)
