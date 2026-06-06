---
title: "Phase 2 Metrics Collection Protocol"
created: "2026-06-07"
version: 1.0
status: production-ready
scope: >
  Step-by-step procedure for collecting metrics during Domain 51 Wave 1 execution 
  window (Days 1-7, June 9-16, 2026). Includes daily and hourly snapshot templates, 
  manual collection process, alert thresholds, and troubleshooting procedures.
word_count: ~1800
deadline: "June 7, 2026 — ready for June 9 execution start"
companion_files:
  - PHASE_2_WAVE_1_POST_EXECUTION_ANALYSIS_FRAMEWORK.md
  - PHASE_2_WAVE_1_CONTINGENCY_DECISION_MATRIX.md
  - DOMAIN_51_JUNE_16_CHECKPOINT_METRICS_TEMPLATE.md
  - DOMAIN_51_JUNE_16_DECISION_LOGIC.md
purpose: >
  Operationalizes daily/hourly monitoring during Wave 1 execution window. Provides 
  manual tracking templates, procedure for on-time data collection, real-time alert 
  thresholds to detect engagement friction early, and backup procedures if automated 
  tracking fails. Enables orchestrator auto-monitoring during June 9-16 window while 
  user handles distribution execution.
---

# Phase 2 Metrics Collection Protocol

**Version 1.0 — June 7, 2026**

This document specifies the step-by-step procedure for collecting and tracking engagement metrics during Domain 51 Wave 1 execution (June 9-16). The metrics collection is designed for **passive monitoring with minimal manual intervention**: most data flows from Bitly and Campaign Monitor automatically, with manual email review required only on June 16 for the Day 7 checkpoint.

---

## 1. Pre-Execution Setup (June 7-9)

### 1.1 Campaign Monitor Campaign Setup

**Objective**: Enable open-rate tracking for all Wave 1 sends

**Procedure** (15 minutes):

1. Log in to Campaign Monitor (campaignmonitor.com) with account credentials
2. Create a new email campaign: "Domain 51 Wave 1 — June 9-12"
3. Configure campaign settings:
   - [ ] Enable open tracking: ON (required for email open rate metrics)
   - [ ] Enable click tracking: ON (required for Bitly/template link tracking)
   - [ ] Enable bounce reporting: ON (required for delivery verification)
4. Add all Wave 1 email templates to the campaign:
   - [ ] Email 4 (Campaign Legal Center)
   - [ ] Email 5 (Issue One)
5. Set up open-rate reporting dashboard:
   - [ ] Enable daily email delivery to your email address with summary stats
   - [ ] Configure: Send report at 20:00 UTC daily (will catch same-day opens)
6. Verify campaign is ready: Send test email to personal inbox; confirm open tracking trigger

**Expected output**: Campaign Monitor dashboard ready with open-rate tracking enabled. Daily email reports will arrive at 20:00 UTC on June 9, 10, 11, 12 with cumulative open counts for each Wave 1 send.

---

### 1.2 Bitly Setup

**Objective**: Track click-through on Domain 51 Gist short link(s)

**Procedure** (10 minutes):

1. Log in to Bitly.com (bitly.com)
2. Verify Domain 51 Gist short link is live:
   - [ ] Link format: bit.ly/domain-51-campaign-finance (or equivalent)
   - [ ] Manual test-click: Confirm it resolves to the Gist
3. Add to Bitly tracking dashboard (if not already present):
   - Navigate to: Dashboard → Links → Search for "domain 51"
   - Verify: Link is active, click history is enabled
4. Enable daily click summaries:
   - [ ] Set up Bitly email report (daily 19:00 UTC) with click counts
   - [ ] Or: Manual daily check of Bitly dashboard (3 minutes) for click counts

**Expected output**: Bitly dashboard ready with daily click tracking. You will see daily click counts for June 9-16 showing cumulative clicks and spike detection.

---

### 1.3 Gmail Label Setup

**Objective**: Organize incoming replies for easy review at Day 7 checkpoint

**Procedure** (5 minutes):

1. Create new Gmail label: `phase2-outreach/wave1/domain-51`
   - [ ] Right-click on "Labels" in left sidebar
   - [ ] Select "Create new label"
   - [ ] Enter: `phase2-outreach/wave1/domain-51`
2. Create filter to auto-label replies from Wave 1 contacts:
   - [ ] Go to Settings → Filters and Blocked Addresses → Create new filter
   - [ ] From: `{ymaluf@campaignlegalcenter.org} OR {npenniman@issueone.org} OR {cterrell@commoncause.org} OR {lwvc@lwvc.org} OR {cleanmoney@cleanmoney.org}`
   - [ ] Apply label: `phase2-outreach/wave1/domain-51`
   - [ ] Create filter
3. Verify: Search Gmail for `label:phase2-outreach/wave1/domain-51` — should return 0 results until replies arrive

**Expected output**: Gmail is ready to automatically label incoming replies. At Day 7 checkpoint (June 16), search the label to find all Domain 51 replies in one view.

---

## 2. Daily Monitoring (June 9-16, Seven Days)

### 2.1 Hourly Snapshot Template (Manual, First 24-48 Hours Only)

**Why hourly tracking for Days 1-2 only**: Early spikes reveal delivery success and immediate engagement. Days 3-7 monitoring is less time-sensitive and moves to daily check.

**Procedure** (3 minutes per check, June 9-10 only):

| Time | Data Point | Source | Value | Notes |
|------|-----------|--------|-------|-------|
| **June 9, 09:05 UTC** | Wave 1 send confirmation | Email send log | Sent to [4 contacts] | Log send time, recipient count |
| **June 9, 10:00 UTC** | Bitly clicks (1h post-send) | Bitly dashboard | ___ clicks | Check for immediate engagement |
| **June 9, 12:00 UTC** | Bitly clicks (3h post-send) | Bitly dashboard | ___ clicks | Expected: 0-2 (most opens happen 6-24h after send) |
| **June 9, 18:00 UTC** | Bitly clicks (9h post-send) | Bitly dashboard | ___ clicks | Expected: 0-3; spike >3 would indicate very fast engagement |
| **June 9, 20:00 UTC** | Campaign Monitor report | Email report | Open count: ___ | Report arrives automatically; record cumulative count |
| **June 10, 09:00 UTC** | Bitly clicks (24h post-send) | Bitly dashboard | ___ clicks | Peak engagement window; expected: 2-5 clicks |
| **June 10, 10:00 UTC** | Campaign Monitor report | Email report | Open count: ___ | Updated cumulative |
| **June 10, 18:00 UTC** | Bitly clicks (end of Day 2) | Bitly dashboard | ___ clicks | End-of-engagement-window check |

**Alert threshold**: If Bitly clicks = 0 by end of June 10 (after 24h for initial opens), escalate to root-cause check: email delivery issue or link problem (see Section 4 troubleshooting).

---

### 2.2 Daily Snapshot Template (Manual, June 11-15)

**Procedure** (5 minutes per day, June 11-15):

For each of these 5 days, run at 09:00 UTC:

| Date | Bitly Clicks (Cumulative) | Daily Delta | Spike? | Notes |
|------|---|---|---|---|
| **June 11** | ___ | ___ | Y/N | |
| **June 12** | ___ | ___ | Y/N | Domain 51 Wave 2 sends conclude; monitor for Wave 2 engagement |
| **June 13** | ___ | ___ | Y/N | Weekend; engagement may slow |
| **June 14** | ___ | ___ | Y/N | |
| **June 15** | ___ | ___ | Y/N | Day before checkpoint; final engagement window check |

**Spike detection**: If daily delta is ≥3 clicks (higher than usual daily count), note in "Notes" column with possible explanation (e.g., "June 11 spike may correspond to Common Cause CA send timing").

**Data source**: Bitly dashboard daily summary or email report.

---

### 2.3 Email Monitoring (Passive, June 9-16)

**Procedure**: Rely on Gmail auto-labels from Section 1.3.

**Passive monitoring**: Emails automatically labeled `phase2-outreach/wave1/domain-51` will accumulate in that label. No manual action required until Day 7 checkpoint.

**Active check** (optional, June 13-14): If you want real-time reply visibility during Wave 1 window, manually search Gmail on June 13 evening: `label:phase2-outreach/wave1/domain-51` to see what replies have arrived so far. This is optional; no action required.

---

## 3. Day 7 Checkpoint Data Collection (June 16, 09:00-09:30 UTC)

On June 16 morning at 09:00 UTC, execute the final metrics collection using DOMAIN_51_JUNE_16_CHECKPOINT_METRICS_TEMPLATE.md (see companion document). This is the formal, complete data pull that feeds into the composite signal score and contingency routing decision.

### 3.1 Campaign Monitor Final Pull (5 minutes)

1. Log in to Campaign Monitor dashboard
2. Navigate to "Domain 51 Wave 1" campaign
3. Record final open counts for each Wave 1 recipient:
   - [ ] Campaign Legal Center: ___ opens
   - [ ] Issue One: ___ opens
4. Calculate final open rate: (total opens) / (confirmed delivered) × 100 = ___%
5. **Critical check**: If open rate <25%, stop and run emergency delivery diagnosis (Section 4 troubleshooting)

### 3.2 Bitly Final Pull (5 minutes)

1. Log in to Bitly dashboard
2. Navigate to Domain 51 Gist short link
3. Record cumulative click count for June 9-16 period: ___ total clicks
4. Review daily breakdown (Bitly shows daily distribution):
   - June 9 (send day): ___ clicks
   - June 10: ___ clicks
   - June 11: ___ clicks
   - June 12-16: ___ clicks (combined)
5. **Critical check**: If total clicks = 0, stop and run emergency delivery diagnosis

### 3.3 Email Reply Collection (8 minutes)

1. Open Gmail
2. Search: `label:phase2-outreach/wave1/domain-51`
3. Review all results (expected: 0-4 replies)
4. For each reply, record:
   - [ ] From email address
   - [ ] Date received
   - [ ] Reply type: Auto-reply/OOO | Form acknowledgment | Substantive | Forward | Adoption statement
   - [ ] Score (1-5): 1=OOO, 2=ack, 3=substantive, 4=forward, 5=adoption
5. Manually score each reply in the metrics template (Section 5)
6. Count Score 3+ replies: ___ total
7. Calculate substantive reply rate: (Score 3+ count) / (confirmed delivered) × 100 = ___%

---

## 4. Alert Thresholds & Early Warning Triggers

Monitor for the following alert conditions during Days 1-7. If triggered, escalate for root-cause diagnosis:

### 4.1 Delivery Alert: 0 Clicks + 0 Opens (Days 1-3)

**Trigger**: By end of June 11 (Days 3 post-send June 9):
- Bitly clicks = 0 (no Gist access)
- Campaign Monitor open count = 0 (no email opens)
- Combined with Gmail replies = 0 (no manual follow-up from contacts)

**Escalation procedure** (execute immediately if triggered):
1. Check email delivery: Gmail search `from:{contact emails} undeliverable OR bounce OR returned`
2. Check spam folder: Manually review Gmail spam folder for bounce-backs
3. Check Bitly link: Click domain-51 Bitly link manually; verify it resolves
4. Review Campaign Monitor send log: Verify Wave 1 sends actually transmitted
5. **Outcome**: If delivery is confirmed BUT engagement is zero, escalate to user for contingency decision (see PHASE_2_WAVE_1_CONTINGENCY_DECISION_MATRIX.md Section 4 — Failure Path)

### 4.2 Engagement Alert: Day 7 Composite Score <3

**Trigger**: After metrics collection on June 16 (see Section 3):
- Calculate composite signal score (DOMAIN_51_JUNE_16_CHECKPOINT_METRICS_TEMPLATE.md Section 6)
- If composite score <3 (below WEAK threshold)

**Escalation procedure**:
1. Generate escalation briefing per PHASE_2_WAVE_1_CONTINGENCY_DECISION_MATRIX.md (appropriate path: Weak or Failure)
2. Email briefing to user by June 16 EOD
3. User decision deadline: June 17, 18:00 UTC

### 4.3 Hourly Spike Alert: Unexpected High Click Volume (Days 1-2)

**Trigger**: Bitly shows ≥5 clicks on a single day (June 9-10)

**Investigation procedure**:
1. Review Bitly daily breakdown: Which day showed the spike?
2. Cross-reference spike date against email send date:
   - Spike on June 9 afternoon/evening = within 24h of June 9 Wave 1 send = confirmed delivery + high interest
   - Spike on June 10 = delayed opens (normal, not concerning)
   - Spike on unexpected date (June 13+) = organic amplification or network referral (note in metrics)
3. **Action**: Spike is a positive signal, not a problem. Note in metrics but no escalation required.

---

## 5. Backup Procedures (If Automated Tools Fail)

### 5.1 If Campaign Monitor is Unavailable

**Fallback**: Use Bitly clicks as proxy for email engagement. Bitly clicks ≈ email opens (correlation ~0.80-0.85).

**Procedure**:
- Assume: 1 Bitly click ≈ 1 email open
- If Bitly clicks = 4, estimate email open rate ≈ 50-75% (conservative estimate)
- Proceed with Bitly-based signal assessment

### 5.2 If Bitly is Unavailable

**Fallback**: Use Campaign Monitor open counts + email reply counts.

**Procedure**:
- Treat email open rate + reply rate as complete engagement signal
- Estimate Bitly clicks: If Campaign Monitor shows 75% open rate (3 of 4), estimate Bitly clicks ≈ 3-4
- Proceed with Campaign Monitor-based signal assessment

### 5.3 If Gmail Labels / Filters Are Misconfigured

**Fallback**: Manual email search on Day 7 checkpoint.

**Procedure**:
- Gmail search: `from:{ymaluf@campaignlegalcenter.org} OR from:{npenniman@issueone.org} ...` (full contact list)
- Manually review all results and score each reply
- Time required: 10 minutes (more than automated label check)

---

## 6. Data Entry Template (Print and Complete by Hand if Needed)

For June 16 Day 7 checkpoint, use this template if you prefer manual entry (otherwise use DOMAIN_51_JUNE_16_CHECKPOINT_METRICS_TEMPLATE.md directly):

```
DOMAIN 51 — DAY 7 CHECKPOINT DATA ENTRY
Collected: June 16, ____:____ UTC

SECTION 1: EMAIL OPEN RATE
Campaign Legal Center (ymaluf@)        Opens: ___ / Delivered: 1 = ___%
Issue One (npenniman@)                 Opens: ___ / Delivered: 1 = ___%
TOTAL WAVE 1                           Opens: ___ / Delivered: 4 = ___%

SECTION 2: BITLY CLICKS
Domain 51 Gist (bit.ly/domain-51)      Clicks: ___ (June 9-16)
Spike detected on: ____________         Yes/No

SECTION 3: EMAIL REPLIES
From: _________________ Date: _____    Type: _______ Score: ___
From: _________________ Date: _____    Type: _______ Score: ___
From: _________________ Date: _____    Type: _______ Score: ___
Total replies: ___ / Confirmed delivered: 4 = ___%
Score 3+ replies: ___ / Confirmed delivered: 4 = ___%

SECTION 4: ADOPTION SIGNALS
Signal 1: ________________________      Confirmed: Y/N
Signal 2: ________________________      Confirmed: Y/N
Total adoption signals: ___

SECTION 5: COMPOSITE SCORE CALCULATION
Open rate (%) × 2:                     ___ × 2 = ___
Bitly clicks/5 × 2:                    (___ / 5) × 2 = ___
Reply rate Score 3+ (%) × 2:           ___ × 2 = ___
Adoption signals × 1:                  ___ × 1 = ___
COMPOSITE SCORE:                       ___ / 10

ROUTING: STRONG (8-10) / MODERATE (5-7) / WEAK (3-4) / FAILURE (<3)
```

---

## 7. Troubleshooting Guide

### Issue: Bitly Link Returns 404

**Symptom**: Click on Domain 51 Bitly short link; get 404 or "Link not found" error

**Root cause**: Bitly link may have expired, been deleted, or URL is mistyped

**Procedure**:
1. Verify Bitly short link format: bit.ly/domain-51-campaign-finance (check casing, hyphens)
2. Log in to Bitly dashboard; search for "domain 51"
3. If link exists in dashboard but returns 404: Click "Edit" → verify destination URL is the Gist; update if needed
4. If link does not exist in dashboard: Create new Bitly short link pointing to Domain 51 Gist
5. Update all email templates with new short link if recreated
6. Send brief follow-up to all Wave 1 contacts: "We had a technical issue with the first link. Here is the corrected link: [new Bitly]"

**Time required**: 10 minutes

---

### Issue: 0 Campaign Monitor Opens Despite Confirmed Send

**Symptom**: Campaign Monitor shows emails were sent, but open count = 0 after 24 hours

**Root cause**: Open tracking may not be enabled, or emails landed in spam

**Procedure**:
1. Check Campaign Monitor open tracking: Settings → Email tracking → Open tracking = ON
2. Check Gmail spam folder: Search `from:{recipient emails}` in [Gmail]/Spam folder
3. If emails are in spam: Ask contacts to move to inbox; send follow-up note
4. If tracking is off: Enable tracking; send re-send to contacts (Day 3-4 follow-up)

**Time required**: 15 minutes

---

### Issue: Replies Arriving Outside Gmail Label

**Symptom**: You see replies in inbox but they don't appear in `phase2-outreach/wave1/domain-51` label

**Root cause**: Gmail filter may not be catching all variations of contact emails, or filter syntax is incorrect

**Procedure**:
1. Verify filter is active: Settings → Filters and Blocked Addresses → Search for "domain-51"
2. Check filter syntax: Should include all contact email variations (may need to update if contacts use different email aliases)
3. Manually add label to any missed replies: Open email → Labels → Add label: `phase2-outreach/wave1/domain-51`
4. Update filter to catch additional email addresses if discovered

**Time required**: 5 minutes

---

### Issue: Bitly Shows Clicks But Campaign Monitor Shows 0 Opens

**Symptom**: Bitly dashboard shows 3+ clicks on domain-51 link, but Campaign Monitor open count = 0

**Likely explanation**: Clicks are organic (non-email) traffic (e.g., shared link, web search, direct), not email opens. OR: Bitly clicks and Campaign Monitor are time-lagged (Campaign Monitor data lags 2-4 hours behind real-time clicks).

**Action**: Not a problem. Use Bitly clicks as primary engagement signal if Campaign Monitor is delayed. Proceed with Day 7 checkpoint using both data points.

---

## 8. Daily Time Budget Summary

| Activity | Time | Days | Total |
|----------|------|------|-------|
| Hourly snapshots (2 days) | 3 min × 8 checks | June 9-10 | 24 min |
| Daily snapshots (5 days) | 5 min × day | June 11-15 | 25 min |
| Email review (passive) | 0 min | June 9-16 | 0 min |
| Day 7 checkpoint (active data pull) | 20 min | June 16 | 20 min |
| **Total user time for metrics collection** | | | **~70 minutes** |
| **Per day average** | | | **~10 minutes/day** |

---

*Prepared June 7, 2026. Companion to PHASE_2_WAVE_1_POST_EXECUTION_ANALYSIS_FRAMEWORK.md. Deploy June 9-16 during Wave 1 execution window.*
