---
title: "Seedwarden Q3 Week 3-4 Subscriber Churn Monitoring and Recovery"
date: 2026-07-13
version: 1.0
status: production-ready
sprint-window: July 13 – July 27, 2026
scope: "Daily unsubscribe rate tracking, root cause investigation, recovery procedures, and win-back sequence activation for Week 3-4 peak execution"
cross-references:
  - SEEDWARDEN_Q3_DAILY_SUBSCRIBER_CHURN_MONITORING.md (Week 1-2 churn baseline and methodology)
  - SEEDWARDEN_Q3_DAILY_EMAIL_MONITORING_CHECKLIST.md (email open/click thresholds)
  - SEEDWARDEN_Q3_WEEK3_4_DAILY_OPS_CHECKLIST.md (daily execution integration)
  - SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md (escalation if churn persists)
---

# Seedwarden Q3 Week 3-4 Subscriber Churn Monitoring and Recovery

**Purpose**: Daily tracking of subscriber unsubscribe rates during Week 3-4 peak launch activity (Jul 13-27). Three bundle sends occur in this window (Sleep Jul 13, Practitioner Jul 15, Immunity Jul 20), creating elevated churn risk. This document operationalizes detection, investigation, and recovery for any churn spike.

**Baseline**: Week 1-2 daily unsubscribe rate average (establish from SEEDWARDEN_Q3_DAILY_SUBSCRIBER_CHURN_MONITORING.md daily logs). Proxy baseline if Week 1-2 data unavailable: 0.2-0.4% daily unsubscribe rate (standard for launch-phase high-frequency email).

**Check cadence**: Daily at 22:00 UTC, without exception. Takes 10 minutes.

---

## Section 1: Daily Churn Tracking Template

### Template Format

Run this template every day at 22:00 UTC. Log all fields before closing.

```
Date: [YYYY-MM-DD]
Time checked: 22:00 UTC

SUBSCRIBER COUNT
Total subscribers (beginning of day): [NUMBER]
  (Source: Kit.com > Subscribers > count at top of page)
Unsubscribes (last 24 hours): [NUMBER]
  (Source: Kit.com > Subscribers > Unsubscribes > filter "Last 24 hours")
Daily unsubscribe rate: [UNSUB COUNT] / [TOTAL] × 100 = [RATE%]

THRESHOLD APPLICATION
Week 1-2 baseline daily rate: [%] (from SEEDWARDEN_Q3_DAILY_SUBSCRIBER_CHURN_MONITORING.md)
Today's rate vs. baseline:
  [ ] At or below baseline → expected normal churn
  [ ] 0.1-0.2% above baseline → slightly elevated; monitor
  [ ] >0.2% above baseline → elevated; investigate

Standard threshold status:
  [ ] GREEN (<0.3%)
  [ ] YELLOW (0.3-0.5%)
  [ ] RED (>0.5%)

EMAIL CORRELATION
Email sent today or yesterday? [ ] Yes — subject: __________ send time: __________
                                [ ] No

UNSUBSCRIBE REASONS (Kit.com > Unsubscribes > Reason column)
  Too many emails: [#] out of [today's total] = [%]
  Not relevant: [#] = [%]
  Prefer other format: [#] = [%]
  Other / Blank: [#] = [%]

NOTES
[Contextual notes: bundle launch day, promotional send, any external factors]

STATUS AFTER APPLYING ALL LOGIC: [GREEN / YELLOW / RED]
```

### 30-Day Log Table (Jul 13 – Aug 3)

| Date | Total Subs | Unsub Count | Rate % | Email Sent? | Top Reason | Status | Action Taken |
|------|-----------|------------|--------|-------------|-----------|--------|--------------|
| Jul 13 | | | | Yes (Sleep launch) | | | |
| Jul 14 | | | | No | | | |
| Jul 15 | | | | Yes (Practitioner) | | | |
| Jul 16 | | | | No | | | |
| Jul 17 | | | | No | | | |
| Jul 18 | | | | No | | | |
| Jul 19 | | | | No | | | |
| Jul 20 | | | | Yes (Immunity) | | | |
| Jul 21 | | | | No | | | |
| Jul 22 | | | | No | | | |
| Jul 23 | | | | No | | | |
| Jul 24 | | | | No | | | |
| Jul 25 | | | | No | | | |
| Jul 26 | | | | No | | | |
| Jul 27 | | | | No | | | |
| Jul 28 | | | | No | | | |
| Jul 29 | | | | No | | | |
| Jul 30 | | | | No | | | |
| Jul 31 | | | | No | | | |
| Aug 1 | | | | No | | | |
| Aug 2 | | | | No | | | |
| Aug 3 | | | | Yes (Digestive) | | | |

---

## Section 2: Threshold Definitions and Escalation Logic

### 2.1 Standard Thresholds (from SEEDWARDEN_Q3_DAILY_SUBSCRIBER_CHURN_MONITORING.md)

| Zone | Daily Rate | Action |
|------|-----------|--------|
| GREEN | <0.3% | Log and continue. No action. |
| YELLOW | 0.3-0.5% | Monitor 3 consecutive days. If sustained: escalate to RED procedures. |
| RED | >0.5% | Investigate immediately (within 2 hours). Root cause required before next send. |

### 2.2 Week 3-4 Elevated Risk Days

Because three email sends occur in 8 days (Jul 13, 15, 20), the Week 3-4 window carries higher unsubscribe risk than Week 1-2 (which had only 2 sends in 8 days). Account for this in threshold interpretation:

| Day type | Expected baseline | Adjusted interpretation |
|----------|-----------------|------------------------|
| Email send day | +0.1-0.2% above baseline | YELLOW threshold temporarily rises to 0.4-0.5% on send day and day-after; only RED at >0.6% |
| 2-3 days post-send | Return to baseline expected | Standard GREEN/YELLOW/RED thresholds apply |
| 4+ days post-send (no send) | Baseline or below | Standard thresholds; any elevation suggests list health issue |

**Example interpretation**:
- Jul 13 (Sleep launch day): 0.4% unsubscribe rate → YELLOW adjusted (expected send-day bump; apply 3-day monitoring window, not immediate escalation)
- Jul 16 (3 days post-Sleep, no send): 0.4% unsubscribe rate → YELLOW standard (3-day monitoring window begins)
- Jul 16 (same day): 0.6% unsubscribe rate → RED (above even adjusted threshold)

### 2.3 Three-Send Window Alert

The Jul 13-20 period (3 sends in 8 days) is the highest-churn-risk period of the entire Q3 sprint. Apply this heightened monitoring rule:

```
CUMULATIVE SEND ALERT — Active Jul 13-20 (3 sends window)

After each send (Jul 13, Jul 15, Jul 20), the cumulative unsubscribe toll increases.
Track cumulative unsubscribes:

  Post-Email 3 (Jul 13 + 48hr): [# unsubscribes since Jul 13]
  Post-Email 4a (Jul 15 + 48hr): [# unsubscribes since Jul 13]
  Post-Email 4b (Jul 20 + 48hr): [# unsubscribes since Jul 13]

If cumulative unsubscribes in Jul 13-22 window > 1.5% of starting subscriber count:
  → Sustained churn event. Activate Recovery Procedure 3 (pause + re-engagement sequence)
  → Do not send Email 5 (Digestive, Aug 3) without completing recovery first
  → Log activation date and cumulative rate in PHASE_3_EXECUTION_LOG.md
```

---

## Section 3: Root Cause Investigation Procedure

When YELLOW (sustained 3+ days) or RED (any day) is triggered:

### Step 1: Email Send Correlation Check

```
Check Kit.com > Campaigns > Recent sends (last 7 days)

Was an email sent same day or day before spike?
  [ ] YES — Subject line: ________________
             Send time: ________________
             Days since prior email: [#]
  [ ] NO — No recent send; list health likely the issue
```

If YES to email send: assess the send.

**Email send assessment**:
- Content tone: Was it primarily Promotional (selling) or Educational (teaching)?
  - If Promotional: likely contributing to unsubscribe spike (audience fatigue with sales content)
  - If Educational: content mismatch (audience did not find content relevant)
- Frequency: How many days between this send and the previous send?
  - <7 days between sends in a high-frequency window: frequency fatigue likely
  - 7-10+ days between sends: frequency is not the primary issue
- Subject line: Did it match the email body?
  - If subject promised value but body was primarily promotional: expectation mismatch → churn trigger

### Step 2: Root Cause Determination (All Scenarios)

```
DETERMINE ROOT CAUSE:

Root Cause A — Frequency Fatigue
Indicators:
  - Email send was within 5 days of prior send
  - Unsub rate spikes on send day or day-after
  - >20% of unsub reasons cite "too many emails"
Action: Pause sends for 24-48 hours; apply Recovery Procedure 1

Root Cause B — Content Mismatch
Indicators:
  - Unsub rate spikes day-after send (subscriber read it, then unsubscribed)
  - >20% of unsub reasons cite "not relevant"
  - Email open rate was OK (>15%) but clicks were low (<2%)
Action: Revise next email subject + body framing; apply Recovery Procedure 2

Root Cause C — Bad Subject Line
Indicators:
  - Unsub spike same day as send (subscriber saw subject line and immediately unsubscribed)
  - Open rate was LOW (<15%) on that send (subject line did not entice opening)
  - No specific reason pattern in unsub reasons (mixed/blank reasons)
Action: Audit subject lines in upcoming emails; apply Recovery Procedure 2

Root Cause D — Competitor Offer / External Event
Indicators:
  - Unsub spike with no recent send (not email-triggered)
  - Multiple audience members moving to a competitor's offer or seasonal interest shift
  - No dominant reason in unsub feedback
Action: Monitor 3 days; if sustained, apply Recovery Procedure 3 (re-engagement)

Root Cause E — Supply/Product Issue
Indicators:
  - A specific product received negative feedback (Etsy reviews, social comments)
  - Unsub rate spike follows negative product feedback event
  - Unsub reasons include "lost trust" or custom other-reason text referencing the product
Action: Address product issue first; then apply Recovery Procedure 2 (content clarity)

Root Cause F — List Health (Not Send-Triggered)
Indicators:
  - Gradual unsubscribe accumulation (no spike correlated to any send)
  - High percentage of cold subscribers in list (>25% no opens in 90 days)
  - Unconfirmed subscribers >15% of list
Action: Run list health cleanup; apply Recovery Procedure 4 (list hygiene)
```

### Step 3: Document Root Cause

```
Root cause identified: [A / B / C / D / E / F]
Evidence summary: ___________
Recovery procedure selected: [1 / 2 / 3 / 4]
Activation date/time: ___________
Expected resolution: ___________
```

---

## Section 4: Recovery Procedures

### Recovery Procedure 1 — Frequency Pause

**Use when**: Root Cause A (frequency fatigue). Daily unsubscribe >0.5% OR YELLOW sustained 3+ days, correlated with high-frequency send period.

**Steps**:
1. Pause all email sends for 24 hours (no new sends during pause window)
2. Review upcoming send schedule: extend next send by minimum 7 days from last send
   - Example: If Email 4 was Jul 20 and caused RED, move Email 5 from Aug 3 to Aug 10
3. Analyze unsubscribe feedback: Kit.com > Unsubscribes > Reason column for last 72 hours
4. Revise next email subject line: shift from announcement frame to value/curiosity frame
   - Before: "Immunity Support — 4 herbs for seasonal defense"
   - After: "Why elderberry works in week 1 but fails in week 2 (the timing secret)"
5. Test revised email on 10% of subscriber segment (if list is large enough for meaningful test, i.e., >500 subscribers)
6. If test open rate >20% and unsubscribe rate <0.3%: send to full list
7. If test open rate <15% or unsubscribe >0.3%: revise again before full list send

**Log template**:
```
Recovery Procedure 1 — Frequency Pause
Activation date: ___________
Pause window: [24/48] hours — no sends until [date]
Next send date (revised): ___________
Subject line revised: [YES: from "___" to "___"] / [NO]
10% segment test: [YES — results: open rate [%], unsub [%]] / [NOT APPLICABLE]
Full send: [CLEARED / HELD — reason: ___]
Resolution: [RESOLVED on [date] / ACTIVE]
```

### Recovery Procedure 2 — Email Copy Review

**Use when**: Root Cause B (content mismatch) or Root Cause C (bad subject line). Unsubscribers cite "not relevant" or churn correlates with a specific send's content.

**Steps**:
1. Do NOT pause sends (audience needs continuity; pausing signals instability)
2. Pull the email that triggered the spike:
   - Kit.com > Campaigns > [campaign name] > View email
   - Review: subject line, first 3 sentences, CTA, educational-to-promotional ratio
3. Identify the content flaw:
   - Is the opening sentence a "we" statement? ("We just launched...") → rewrite to "you" statement ("You've been asking about sleep herbs...")
   - Is the email >50% promotional language? → rewrite opening to 80% educational / 20% promotional
   - Does the CTA link resolve correctly? → verify Etsy link is live
4. Draft revised version for next email:
   - Shift frame: If prior email was "here's our bundle," next should be "here's the herb that surprised us and why"
   - Add educational opening (min 3 sentences of plant science or preparation detail before any product mention)
5. Review with fresh eyes before send: does this email teach something? Does it feel like it's FOR the reader, not about the product?
6. Send revised email on standard schedule (do not delay)

**Log template**:
```
Recovery Procedure 2 — Email Copy Review
Activation date: ___________
Email audited: [subject line, send date]
Flaw identified: [We-frame / Over-promotional / CTA broken / Subject mismatch]
Revision made: [specific change]
Next email subject: "___________"
Send date (standard schedule): ___________
Resolution: [RESOLVED on [date] / ACTIVE]
```

### Recovery Procedure 3 — 24-Hour Pause + Segment Analysis

**Use when**: RED trigger (>0.5%) sustained 2+ days, OR cumulative unsubscribe >1.5% of list in Jul 13-22 window (three-send alert from Section 2.3). This is a more serious intervention than Procedure 1.

**Steps**:
1. Pause sends for 24 hours immediately upon trigger
2. Run full list health check (Kit.com):
   - Unconfirmed subscribers: filter "Status = Unconfirmed" — count and % of list
     - If >15%: remove immediately (Kit.com > Subscribers > filter "Unconfirmed" > suppress)
   - Cold subscribers (no opens in 90 days): filter "Last Opened > 90 days ago"
     - If >25%: suppress from next 2 sends (create suppression segment)
   - Log pre- and post-cleanup counts
3. Run segment analysis on current unsubscribers (which segment is churn concentrated in?):
   - New (0-7 days): if >2% rate → opt-in flow or first email issue
   - Early (8-30 days): if >0.8% → content expectation mismatch
   - Long-term (>30 days): if >0.4% → fatigue or content drift
   - High-engagement (2+ recent opens): if any → critical signal; tone/content mismatch
4. Identify targeted recovery segment: the segment with highest abnormal churn
5. Send recovery email to targeted segment within 48-72 hours of pause end:
   - If frequency fatigue: use Win-Back Template A (Section 5 below)
   - If content mismatch: use Win-Back Template B (Section 5 below)
6. Monitor unsubscribe rate for 3 days post-recovery send
7. If rate drops below 0.3% within 3 days: close escalation
8. If rate stays above 0.3% after 3 days: escalate to SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md Section 3

**Log template**:
```
Recovery Procedure 3 — Pause + Segment Analysis
Activation date: ___________
Trigger: [Cumulative 1.5% / Daily RED >0.5% sustained]
Pause window: 24 hours | Sends paused until: ___________

List health actions:
  Unconfirmed removed: [#] ([%] of list) on [date]
  Cold suppressed: [#] ([%] of list) on [date]
  Pre-clean total: [#] | Post-clean total: [#]

Segment analysis:
  Churn concentrated in: [New / Early / Long-term / High-engagement / Uniform]
  Segment-specific rate: [%]
  Root cause: ___________

Recovery email:
  Template used: [A / B] (see Section 5)
  Target segment: ___________
  Send date: ___________

3-day post-send monitoring:
  Day 1 rate: [%] | Day 2 rate: [%] | Day 3 rate: [%]
  Resolution: [RESOLVED — rate dropped to [%]] / [ESCALATED to Week 5-6 contingency]
```

### Recovery Procedure 4 — List Hygiene Cleanup

**Use when**: Root Cause F (list health issue). Gradual unsubscribe accumulation with no send correlation; high cold-subscriber percentage.

**Steps**:
1. Run full Kit.com list audit (same as Procedure 3 Step 2)
2. Remove unconfirmed subscribers (suppress, do not delete)
3. Suppress cold subscribers (no opens in 90 days) from next 2 sends
4. Calculate new "clean" total subscriber count
5. Rebaseline daily unsubscribe rate using clean total (rate% will appear to drop because denominator decreased)
6. For suppressed cold subscribers: schedule a separate win-back campaign (Template C, Section 5) 14 days after suppression
7. Do NOT apply win-back immediately; cold subscribers need a gap before re-engagement outreach

**Log template**:
```
Recovery Procedure 4 — List Hygiene
Activation date: ___________
Trigger: [Gradual accumulation / High cold % / High unconfirmed %]

Cleanup actions:
  Unconfirmed suppressed: [#] | New total after: [#]
  Cold (90d) suppressed: [#] | New total after: [#]
  Final clean total: [#]

Rebaselined daily rate: [%] (was [old rate]% before cleanup)
Status post-cleanup: [GREEN / YELLOW / still RED]

Win-back campaign for cold segment:
  Scheduled for: ___________
  Template: C (see Section 5)
  Target: [#] cold subscribers
```

---

## Section 5: Win-Back and Re-engagement Templates

### Template A — Frequency Adjustment Win-Back

**Use when**: Recovery Procedure 1 or Procedure 3, when unsubscribe reasons are dominated by "too many emails."

**Target segment**: Active subscribers who have NOT yet unsubscribed (preventing further churn), specifically long-term subscribers (>14 days) and high-engagement subscribers.

**Timing**: Send 24-48 hours after pause period ends.

**Subject line options** (choose one):
- "A quick note about how often you'll hear from us"
- "We're adjusting our email schedule — here's what changes"
- "Fewer emails, same quality — what's changing"

**Email body**:

```
Subject: A quick note about how often you'll hear from us

Hi [First Name],

We've been launching three new herbal bundles in July — Sleep & Nervines,
the Practitioner Tier, and Immunity Support. That's a lot of email from us
in a short window.

We noticed. And we're adjusting.

Starting now, you'll hear from us once every 10-14 days, not once a week.
Same content quality — herbs, preparation guidance, seasonal timing. Just
with more space between.

If the recent frequency felt like too much: we hear you, and it changes now.
If you found it useful: each email still has new content you won't see
anywhere else.

Either way, the next email is [DATE]. After that, one every 10-14 days
through the end of the Q3 launch season (August 3).

Thank you for being here.

[Signature]
Seedwarden

---
P.S. If you want to stay but get even fewer emails, reply to this message.
We'll note your preference and adjust. No judgment either way.
```

**Metrics to track post-send (3 days)**:
- Open rate: target >18% (lower than standard; audience is at-risk)
- Unsubscribe rate same-day: target <0.2% (if higher, frequency adjustment messaging did not resolve concern)
- Reply rate: any replies signal very high engagement; note and respond personally

---

### Template B — Content Relevance Win-Back

**Use when**: Recovery Procedure 2 or Procedure 3, when unsubscribe reasons are dominated by "not relevant."

**Target segment**: Long-term subscribers (>14 days) who have opened at least one prior email.

**Timing**: Send within 48 hours of identifying content mismatch as root cause.

**Subject line options**:
- "The next 3 emails you'll get from us — and why they're different"
- "We may have been talking about the wrong things. Here's what's next."
- "3 herbs, 3 bundles, 3 weeks — here's what's coming"

**Email body**:

```
Subject: The next 3 emails you'll get from us — and why they're different

Hi [First Name],

We've been focused on launching guides. Maybe too focused on the launch,
and not enough on what you actually came here for.

Here's what the next 3 emails will cover:

July 20 — IMMUNITY SUPPORT
  Not just a product launch. The real reason elderberry falls short for most
  people (and the 2-herb protocol that makes it work).

August 3 — DIGESTIVE SUPPORT
  The gut-herb relationship that mainstream herbalism glosses over.
  Why ginger and licorice work together differently than either works alone.

After that — a longer break.
  We're going to slow down. One email every 3-4 weeks after August.
  More depth. Less frequency.

If this sounds better than what you've been getting: stay. It gets more
educational from here. If it's still not what you're looking for: no hard
feelings — the unsubscribe link is always at the bottom.

We'd rather have a smaller list of engaged readers than a large list of
people who don't find value in what we send.

[Signature]
Seedwarden
```

**Metrics to track post-send (3 days)**:
- Open rate: target >20% (indicating genuine curiosity about the content preview)
- Click rate: target >2% (link to any herb detail page or Etsy listing)
- Unsubscribe rate same-day: target <0.15%
- If unsubscribe rate > 0.3% on this email: the audience is departing at high rate regardless of content adjustments; escalate to SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md Section 3

---

### Template C — Cold Subscriber Win-Back (Dormant Re-Engagement)

**Use when**: Recovery Procedure 4 (list hygiene), for the cold segment (no opens in 90 days) that was suppressed. Send 14 days after suppression, as a separate one-time campaign.

**Target segment**: Subscribers with zero opens in the last 90 days who have NOT unsubscribed.

**Timing**: 14 days after suppression date (per Recovery Procedure 4 Step 6).

**Subject line options**:
- "We launched 4 herbal guides — did you miss them?"
- "Three bundles launched. One more coming August 3. Catch up here."
- "You've been quiet — here's what's been happening at Seedwarden"

**Email body**:

```
Subject: We launched 4 herbal guides — did you miss them?

Hi [First Name],

It's been a while since we last connected. We've been busy this summer.

Here's what launched since you last opened an email from us:

WOMEN'S HEALTH BUNDLE
  Hormonal balance, menstrual cycle support, stress-responsive herbs.
  [Link: Etsy listing]

RESPIRATORY HEALTH BUNDLE
  Seasonal immunity, clear airways, elderberry preparation guide.
  [Link: Etsy listing]

SLEEP AND NERVINES BUNDLE
  Deep rest, nervous system calm, valerian and passionflower protocols.
  [Link: Etsy listing]

IMMUNITY SUPPORT BUNDLE
  Year-round defense, elderberry timing, ashwagandha thyroid awareness.
  [Link: Etsy listing]

ONE MORE COMING AUGUST 3:
  Digestive Support — gut health from the garden.

If one of those is interesting to you: click through and take a look.
These are substantial, researched guides. Not just product pages.

If none of it is relevant anymore: no problem. The unsubscribe link is
below, and we'll remove you without any follow-up.

We'd genuinely rather you choose one way or the other. Dormant subscribers
don't help either of us.

[Signature]
Seedwarden

---
P.S. If there's a topic you wish we'd covered — reply and tell us.
We're planning Q4 content now.
```

**Metrics to track (3 days post-send)**:
- Open rate: target >15% (cold segment expected to perform lower than main list)
- Click rate: target >3% (cold segment clicking = genuine re-engagement)
- Unsubscribe rate: expected 0.5-1.5% (cold segment exits at higher rate; this is acceptable and desired — list cleanup effect)
- Post-campaign action:
  - If open rate >15% AND click rate >3%: re-activate this segment to main list
  - If open rate <15% OR click rate <3% after 2 re-engagement sends: permanently suppress this segment from future sends

---

## Section 6: Weekly Churn Summary (Every Monday)

Run every Monday at 08:00 UTC for prior week.

### Week 3 Churn Summary (complete by Jul 20 08:00 UTC)

```
Week 3 (Jul 13-19) Churn Summary

DAILY RATES:
  Jul 13 (Sleep launch): [%] | Status: [G/Y/R]
  Jul 14: [%] | Status: [G/Y/R]
  Jul 15 (Practitioner): [%] | Status: [G/Y/R]
  Jul 16: [%] | Status: [G/Y/R]
  Jul 17: [%] | Status: [G/Y/R]
  Jul 18: [%] | Status: [G/Y/R]
  Jul 19: [%] | Status: [G/Y/R]

WEEK 3 AVERAGES:
  7-day average unsubscribe rate: [%]
  Status: GREEN (<0.3%) / YELLOW (0.3-0.5%) / RED (>0.5%)
  vs. Week 1-2 baseline: [+/-]%
  Trend: [Stable / Elevated / Improving]

CUMULATIVE THREE-SEND ALERT:
  Total unsubscribes Jul 13-19: [#]
  As % of starting subscriber count (Jul 13): [%]
  Alert threshold (1.5%): [NOT TRIGGERED / TRIGGERED on [date]]

ESCALATIONS THIS WEEK:
  YELLOW events: [None / Days: ___]
  RED events: [None / Days: ___]
  Recovery procedures activated: [None / Procedure ___ on [date]]
  List health cleanup: [None / Removed [#] unconfirmed, [#] cold on [date]]

UNSUBSCRIBE REASON ANALYSIS (Week 3 totals):
  Too many emails: [%] of week's unsubs [Dominant reason? >20%: Y/N]
  Not relevant: [%] of week's unsubs [Dominant reason? Y/N]
  Prefer other format: [%]
  Other/Blank: [%]

OUTLOOK FOR WEEK 4:
  Immunity launch (Jul 20) expected to cause spike? [YES — monitor closely / NO]
  Send gap (Jul 20 after Jul 15): [# days]
  Pre-emptive action if Week 3 was elevated: [None / Adjusted subject line / Extended gap]
```

### Week 4 Churn Summary (complete by Jul 28 08:00 UTC)

Use identical template structure. Add the following field:

```
WEEK 3 vs. WEEK 4 COMPARISON:
  Week 3 avg daily rate: [%] | Week 4 avg daily rate: [%]
  Change: [+/-]%

IF Week 4 avg > Week 3 avg by >0.2%:
  → Sustained churn elevation. Activate Recovery Procedure 3.
  → Assess whether Email 5 (Digestive, Aug 3) should be delayed or subject-adjusted.

IF Week 4 avg ≤ Week 3 avg:
  → Churn is stable or improving. Continue standard monitoring into Week 5-6.
```

---

## Section 7: Escalation to Week 5-6 Contingency

### Automatic Escalation Triggers

The following conditions automatically escalate to SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md. No additional judgment required.

| Trigger | Condition | Section to Activate |
|---------|-----------|---------------------|
| Churn persists after Recovery Procedure 3 | Unsubscribe rate >0.3% for 3+ days after recovery email sent | SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md Section 3 |
| Cumulative three-send alert triggered | >1.5% of list unsubscribed Jul 13-22 | SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md Section 3 |
| Email open rate <15% + churn >0.3% simultaneously | Both metrics in RED on same day | SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md Section 2 (deliverability check) |
| Week 4 churn average higher than Week 3 by >0.2% | Sustained escalation trend | SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md Section 3 |

### Pre-Escalation Information to Gather

Before activating SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md:

1. Daily rates for all of Week 3-4 (from 30-day log table, Section 1)
2. Recovery procedures already tried and their results
3. List health post-cleanup subscriber count and cold/unconfirmed percentages
4. Unsubscribe reason breakdown (% by category for Weeks 3-4 combined)
5. Most recent email open rates and click rates (from SEEDWARDEN_Q3_DAILY_EMAIL_MONITORING_CHECKLIST.md)

---

## Section 8: Kit.com Navigation Reference (Week 3-4)

All data sources for this document are in Kit.com. Navigation paths:

| Data needed | Kit.com path |
|-------------|-------------|
| Daily unsubscribe count | Subscribers > Unsubscribes > filter "Last 24 hours" |
| Unsubscribe reasons | Subscribers > Unsubscribes > Reason column |
| Total subscriber count | Subscribers > top of page "Active subscribers" count |
| Cold subscribers (no opens 90d) | Subscribers > filter "Last Opened" > before [90 days ago] |
| Unconfirmed subscribers | Subscribers > filter "Status = Unconfirmed" |
| Recent email sends | Campaigns > sorted by date |
| Campaign open rate | Campaigns > [name] > Analytics > Open Rate |
| Subscriber history (7-day trend) | Account > Insights > Subscriber Growth > last 7 days |

---

*Document status: Production-ready. Version 1.0 created July 13, 2026. Covers Week 3-4 churn monitoring (Jul 13-27) with built-in escalation to SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md. All thresholds explicit. All escalation triggers mechanical. Recovery procedures are sequential steps, not judgment calls. Cross-references: SEEDWARDEN_Q3_DAILY_SUBSCRIBER_CHURN_MONITORING.md (Week 1-2 baseline), SEEDWARDEN_Q3_DAILY_EMAIL_MONITORING_CHECKLIST.md (email monitoring integration).*
