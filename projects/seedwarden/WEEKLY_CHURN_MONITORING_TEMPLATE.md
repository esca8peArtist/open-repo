---
title: "Weekly Churn Monitoring Template — Q3 Subscriber Retention"
date: 2026-06-29
version: 1.0
status: production-ready
scope: "Jun 29 – Aug 3, 2026 (Women's Health through Digestive Support launches). Six-row weekly grid."
cross-references:
  - SEEDWARDEN_Q3_DAILY_SUBSCRIBER_CHURN_MONITORING.md (full daily procedure reference)
  - WEEK_1_2_EMAIL_MONITORING_DASHBOARD.md (email open/click monitoring)
  - PHASE_3_EMAIL_ENGAGEMENT_ALERT_PROCEDURES.md (escalation decision trees)
  - PHASE_3_EXECUTION_LOG.md (metric recording)
---

# Weekly Churn Monitoring Template

**Purpose**: Six-row grid tracking daily unsubscribe rates for Women's Health bundle launch week (Jun 29–Jul 4). Provides churn percentage calculation, GREEN/RED status, and same-day decision tree. Duplicate the tab structure for each subsequent bundle week.

**Data source**: Kit.com > Subscribers > Unsubscribes > filter "last 24 hours" (pull daily at 22:00 UTC).

**Churn % formula**: Daily Unsubs / Current Subscriber Base × 100

---

## GRID: WEEK 1 — WOMEN'S HEALTH LAUNCH (JUN 29–JUL 4)

| **Date** | **Daily Unsubscribes** | **Current Subscriber Base** | **Churn %** | **Status** | **Action** |
|----------|------------------------|----------------------------|-------------|------------|------------|
| Jun 29 | [Kit.com count] | [Subscriber count at send] | =[Col B/Col C×100] | GREEN/RED | [See decision tree] |
| Jun 30 | [Kit.com count] | [Running count after Jun 29 unsubs] | =[formula] | GREEN/RED | |
| Jul 1 | [Kit.com count] | [Running count] | =[formula] | GREEN/RED | |
| Jul 2 | [Kit.com count] | [Running count] | =[formula] | GREEN/RED | |
| Jul 3 | [Kit.com count] | [Running count] | =[formula] | GREEN/RED | |
| Jul 4 | [Kit.com count] | [Running count] | =[formula] | GREEN/RED | |

**Weekly total**:
- Total unsubs Jun 29–Jul 4: [SUM of Column B]
- Starting subscriber count (Jun 29 pre-send): [from Jun 29 subscriber base column]
- Week 1 cumulative churn %: [Total unsubs / Starting count × 100]

---

## THRESHOLD DEFINITIONS

### Status Logic (Column E)

```
Churn % < 0.5% per day:
  → Status = GREEN
  → Action = None. Log "GREEN" and continue.

Churn % > 0.5% per day:
  → Status = RED
  → Action = Immediate same-day investigation (see decision tree below)
```

**Why 0.5% is the RED threshold**: A list of 500 subscribers losing >2.5 unsubscribes/day on a non-send day is a signal of content fatigue, spam placement, or audience mismatch — not normal attrition. Normal non-send-day attrition is 0–2 unsubscribes on a 500-person list.

**Send-day context**: On email send days (Jun 29, Jul 6, Jul 13, Jul 20, Aug 3), unsubscribe rates are expected to be higher than non-send days. Apply the same 0.5% threshold but note in the Action column: "Send day — [X] unsubs expected vs. baseline."

---

## DECISION TREE (RED THRESHOLD TRIGGERED)

### Step 1: Confirm the Count

Pull again from Kit.com 30 minutes after initial pull. Confirm number is stable (not a display glitch):

```
IF second pull matches first pull:
  → Confirmed RED. Proceed to Step 2.

IF second pull is significantly different:
  → Kit.com display lag. Wait 2 hours and re-pull before acting.
```

---

### Step 2: Check Timing Correlation

```
Was an email sent today or yesterday?

IF YES (email sent today or yesterday):
  → Send-correlated unsub spike. Check:
    (a) Subject line: was it more promotional than usual? If YES, next email revise tone.
    (b) Unsubscribe reasons from Kit.com > Subscribers > Unsubscribes > Reason column.
        Common reasons: "Too many emails" = frequency issue; "Not relevant" = audience mismatch.
    → If reason is "Too many emails": increase send gap (push next email 3–5 days)
    → If reason is "Not relevant": check subscriber source (are these sign-ups from a mismatched lead magnet?)

IF NO (no email sent in last 48 hours):
  → Organic/passive unsub spike. Check:
    (a) Spam folder landing (test send to Gmail + Outlook + Apple to see if landing in spam)
    (b) List staleness (were these subscribers confirmed but non-engaged for 60+ days?)
  → If spam: contact Kit.com support; review sender reputation
  → If staleness: consider excluding unengaged segment from next send
```

---

### Step 3: Check Spam Complaints

Kit.com tracks spam complaints separately from unsubscribes.

Navigate: Kit.com > Settings > Deliverability > Spam Complaints (or check Campaign Report > Spam).

```
IF spam complaints > 0.1% of sends:
  → This is a deliverability-threatening threshold.
  → Do NOT send next email until spam rate drops below 0.1%.
  → Action: Remove all non-openers from last 60 days before next send.
  → Action: Revise subject line to remove any words triggering spam filters (free, urgent, !!).

IF spam complaints < 0.1%:
  → No deliverability threat. Unsub spike is behavioral, not technical.
  → Continue with send schedule; adjust content per Step 2 findings.
```

---

### Step 4: Adjust Send Time (Optional)

If churn spikes appear on the same day of the week:

```
Pattern: Churn >0.5% on Mondays specifically
  → Subscribers may be clearing inboxes after weekend; Monday is a high-unsub day for email lists
  → Solution: Test shifting next email to Tuesday or Wednesday (reduce Monday friction)

Pattern: Churn >0.5% after every email send
  → Indicates send frequency is too high OR content relevance declining
  → Solution: Add one additional free-content send (educational only, no CTA) before next promotional email
  → This "primes" the list and reduces unsub reaction to next promotional email
```

---

## DUPLICATE THIS TEMPLATE FOR EACH BUNDLE WEEK

### Tab Structure for Google Sheets

- Tab 1: Week 1 — Women's Health (Jun 29–Jul 4)
- Tab 2: Week 2 — Respiratory (Jul 5–Jul 11)
- Tab 3: Week 3 — Sleep & Nervines (Jul 12–Jul 18)
- Tab 4: Week 4 — Immunity Support (Jul 19–Jul 25)
- Tab 5: Week 5 — Digestive (Jul 26–Aug 3)
- Tab 6: Cumulative — All Weeks (aggregate unsub count, cumulative churn %, starting vs. ending subscriber base)

Each tab: same 5-column structure. Same threshold rules. Same decision tree applies in all weeks.

---

## CUMULATIVE CHURN TRACKER (FILL WEEKLY)

Update every Monday as part of weekly review:

| Week | Bundle | Start Subscribers | End Subscribers | Net Loss | Cumulative Churn % |
|------|--------|------------------|----------------|----------|-------------------|
| Week 1 | Women's Health | [FILL Jun 29] | [FILL Jul 4] | [Start - End] | [Loss/Start × 100] |
| Week 2 | Respiratory | [FILL Jul 5] | [FILL Jul 11] | | |
| Week 3 | Sleep & Nervines | [FILL Jul 12] | [FILL Jul 18] | | |
| Week 4 | Immunity | [FILL Jul 19] | [FILL Jul 25] | | |
| Week 5 | Digestive | [FILL Jul 26] | [FILL Aug 3] | | |
| **Total** | All bundles | [Week 1 start] | [Week 5 end] | [Total loss] | **[Cumulative %]** |

**Acceptable cumulative churn over 5 weeks**: <8% (i.e., retain at least 92% of Jun 29 starting list through Aug 3).

**At risk**: If cumulative churn exceeds 5% by Week 3 (Jul 18), review email cadence immediately before sending Weeks 4 and 5.

---

## RETENTION MESSAGING TEMPLATES

These are standing retention messages ready to deploy if RED churn is confirmed. Activate based on unsubscribe reason identified in Step 2.

### Template A: "Frequency Adjustment" (Deploy if "Too many emails" reason)

Subject: Quick note — adjusting our send schedule

Body:
> "Hi [first name], I noticed a few subscribers recently mentioned they're receiving more emails than they'd like from us. I've updated our send schedule — you'll hear from us no more than once per week going forward, with each email focused on a single herb or botanical topic. If you're open to staying on, I think you'll find the cadence more comfortable from here. Either way, I appreciate you having been part of this community. — [Name], Seedwarden"

Send to: Recent unsubscribers via re-engagement path (Kit.com allows sending to unsubscribed segments with specific consent triggers; verify before using).

---

### Template B: "Content Relevance" (Deploy if "Not relevant" reason)

Subject: Wrong list? Let me check.

Body:
> "Hi [first name], if you signed up for [lead magnet topic] and the content we're sending doesn't match what you expected — I want to know. We focus specifically on [herb/botanical education + identification + growing] for home growers and herbalism students. If that's not what you came for, no hard feelings. If it is what you came for and the recent emails missed the mark, I'd genuinely like your feedback: just reply to this email with what you'd rather see. — [Name], Seedwarden"

---

*Document prepared: June 29, 2026. Activate Week 1 tab at Jun 29 send. Update daily at 22:00 UTC. Complete cumulative tracker every Monday. Cross-reference SEEDWARDEN_Q3_DAILY_SUBSCRIBER_CHURN_MONITORING.md for full segment analysis, Kit.com navigation details, and list health scoring procedures.*
