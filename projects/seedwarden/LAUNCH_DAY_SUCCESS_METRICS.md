---
title: "May 30 Launch Day Success Metrics & Escalation Thresholds"
date: 2026-05-27
version: 1.0
status: PRODUCTION-READY
scope: Quantified metrics for Day 1 success, decision thresholds, and escalation rules
references:
  - LAUNCH_DAY_HOUR_BY_HOUR_RUNBOOK.md (time-gated execution)
  - CONTINGENCY_DECISION_THRESHOLDS.md (Day 3/7 follow-up metrics)
---

# May 30 Launch Day Success Metrics & Escalation Thresholds

**Purpose**: Define what "successful launch day" means quantitatively. Provide clear decision rules for when to continue vs. escalate.

---

## Core Principle: Minimum Viable Launch

**The Etsy listing is the only hard requirement.**

Everything else is reach amplification. If Etsy listings go live and are discoverable, the launch happened. Everything else is gravy.

```
Etsy listings live              = LAUNCH IS REAL (minimum viable)
+ Kit broadcast sent            = EMAIL LAUNCH (primary outreach)
+ 2+ social posts live          = SOCIAL LAUNCH (secondary reach)
+ GA4 tracking confirmed        = ANALYTICS ACTIVE (measurement)
```

If only Etsy listings go live and nothing else works, the launch still happened. Week 1 is when reach is built.

---

## Day 1 (May 30) Success Metrics

### Tier 1: Critical Success Metrics (Launch Happened or Didn't)

| Metric | Target | Threshold | Measure At |
|--------|--------|-----------|------------|
| Etsy listings published | 8 | ≥6 of 8 | 08:15 UTC, final check at 21:00 UTC |
| Kit broadcast sent | 1 email | Sent (≥1 recipient) | 12:05 UTC |
| Social posts live | 4 posts | ≥3 of 4 | 14:00 UTC |
| GA4 pageviews (full day) | 200+ | ≥50 | 21:00 UTC |

**Decision rule**: If ALL Tier 1 metrics are met → **SUCCESSFUL LAUNCH**

If ANY Tier 1 metric is missed:
- Etsy <6 published: FAILURE (core product not available)
- Kit not sent: Continue with email fallback (Gmail)
- Social <3 posts: DEGRADED (reach is lower, but email should compensate)
- GA4 <50 pageviews: INVESTIGATE tracking, but continue (may be a metrics issue, not reach issue)

---

### Tier 2: Performance Metrics (How Well Did It Go?)

Measure these at 18:00 UTC (10 hours into launch) and again at 21:00 UTC (full day).

| Metric | Good | Acceptable | Poor |
|--------|------|----------|------|
| **GA4 pageviews (10 hr)** | 300+ | 100–299 | <100 |
| **Instagram reach** | 300+ | 100–299 | <100 |
| **Kit email open rate** | 20%+ | 10–19% | <10% |
| **TikTok views** | 200+ | 50–199 | <50 |
| **Reddit upvotes** | 20+ | 5–19 | <5 |
| **Pinterest saves** | 10+ | 2–9 | <2 |

**Interpretation**:

- **Good**: Launch day exceeded expectations. Strong early traction. Continue normal outreach for Days 2–7. Consider paid amplification if budget available.
- **Acceptable**: Launch day met minimum expectations. Normal for new product launch. Continue organic outreach. No paid amplification needed yet.
- **Poor**: Launch day underperformed. Diagnose: did all social posts go live? Is GA4 tracking broken? Proceed normally; Day 3 and Day 7 are more meaningful checkpoints (influencer shares, organic growth happen later).

**Do NOT panic if metrics are "Poor" on Day 1.** This is the most common scenario. Organic reach for new accounts is always low on Day 1. The launch is not a failure; it is a normal slow start.

---

### Tier 3: Engagement & Click Metrics (Demand Signal)

Measure at 21:00 UTC.

| Metric | Good | Acceptable | Poor |
|--------|------|----------|------|
| **Kit email click-through rate** | 10%+ | 3–9% | <3% |
| **Etsy CTR from GA4 referrals** | 15%+ | 5–14% | <5% |
| **Social comments + likes (total)** | 50+ | 10–49 | <10 |
| **Reddit comments** | 10+ | 2–9 | <2 |

**Interpretation**:

- **Good**: Audience is engaging with content. Low click-through might indicate strong product-market fit (people want it, clicking through to Etsy). High engagement shows audience interest.
- **Acceptable**: Normal engagement. People visited but did not all convert to deep actions. Expected for Day 1.
- **Poor**: Low engagement. This could indicate: audience is not the right fit, content did not resonate, or the CTA (call-to-action) was unclear. Plan Day 2–3 follow-up with clearer messaging.

---

## Hourly Checkpoint Metrics

Reference these at the specified times in LAUNCH_DAY_HOUR_BY_HOUR_RUNBOOK.md

### 08:15 UTC — Etsy Publish Checkpoint

| Metric | Expected | Action if Met | Action if Missed |
|--------|----------|---|---|
| Etsy listings published | 8 | Proceed to 09:30 | Troubleshoot F5; recover or proceed with 6–7 |

### 10:00 UTC — First Metrics Check

| Metric | Expected | Action if Met | Action if Missed |
|--------|----------|---|---|
| GA4 pageviews | 30–200 | Continue | <30: Check GA4 tracking. 0–5: Severe tracking issue, escalate F8 |
| Etsy listings discoverable | All 8 visible in search | Continue | Try search by zone name; if not found, Etsy may have filtering. Proceed. |

### 14:00 UTC — Mid-Day Checkpoint

| Metric | Expected | Action if Met | Action if Missed |
|--------|----------|---|---|
| GA4 pageviews (6 hours) | 100–500 | Continue | <100: Diagnose social post failures. 0–30: Escalate |
| Social posts live | 3+ of 4 | Continue | <3: Use workarounds to post manually |
| Kit broadcast sent | Delivered | Continue | Not sent: Use Gmail fallback |

### 15:00 UTC — Critical Go/No-Go Decision

| Metric | Decision | Action |
|--------|----------|--------|
| GA4 pageviews ≥ 100 | CONTINUE | Proceed to 21:00 UTC checkpoint |
| GA4 pageviews 50–99 | CONTINUE (monitor) | Proceed; systems are working, traffic is just lower than baseline |
| GA4 pageviews <50 | DIAGNOSE | Spend 30 min troubleshooting. If recovered, CONTINUE. If not, escalate. |
| Any account suspension | ESCALATE | Stop outreach immediately; contact Orchestrator |

### 18:00 UTC — Evening Checkpoint

| Metric | Expected | Action if Met | Action if Missed |
|--------|----------|---|---|
| GA4 pageviews (10 hours) | 200–1,000 | Continue to 21:00 final | 100–199: On track, metrics ramping slower. Continue. <100: Escalate |
| Kit email opens | 5–30% | Continue | <5%: Wait until Day 2 morning; email opens accumulate over 24 hours |
| Reddit upvotes | 5–25 | Continue | <5 on visible post: Let it rest, check again tomorrow |

### 21:00 UTC — Final Checkpoint & Debrief

| Metric | Target | Status | Next Step |
|--------|--------|--------|-----------|
| Etsy listings published | ≥6 of 8 | ___ | If ≥6: Launch succeeded. If <6: Escalate |
| Kit broadcast sent | ≥1 | ___ | If yes: Email outreach succeeded. If no: Activate fallback |
| Social posts live | ≥3 of 4 | ___ | If ≥3: Social launch succeeded. If <3: Continue daily on Days 2–7 |
| GA4 pageviews | ≥50 (or note tracking issue) | ___ | If ≥50: Metrics working. If 0 and no tracking issue: Escalate F8 |

---

## Success Criteria Rubric

### Launch Outcome: SUCCESSFUL

**All of these must be true**:
- ✓ At least 6 of 8 Etsy listings published
- ✓ At least 1 kit broadcast sent (even if to 0 subscribers, it is not an error)
- ✓ At least 3 of 4 social posts live
- ✓ GA4 tracking confirmed working OR a known issue identified and documented

**Narrative**: "Launch day was successful. All systems are operational. Reach will grow organically over Days 2–7 and accelerate at Day 3 checkpoint with influencer shares."

---

### Launch Outcome: SUCCESSFUL WITH RECOVERY

**If any of these happened**:
- 1–2 Etsy listings failed to publish, but you recovered with 6+ live
- Kit broadcast failed but was resent via Gmail fallback
- 1 social post failed to auto-publish but was manually posted
- GA4 had a temporary tracking glitch but is now working

**Narrative**: "Launch day succeeded with minor recovery actions. All systems are now operational. One [system] required fallback procedure [name], but was recovered successfully by [time]. Expect normal trajectory from here."

---

### Launch Outcome: SUCCESSFUL WITH DEGRADED REACH

**If all these are true**:
- ✓ At least 6 Etsy listings published
- ✓ Email broadcast sent
- ✓ Only 2 of 4 social posts live (but at least 1)
- ⚠ GA4 pageviews 50–200 by 21:00 UTC (below normal but not zero)

**Narrative**: "Launch day succeeded, but reach was constrained by [reason: limited social posts / low initial engagement / new account algorithm]. All core systems are operational. Reach will grow over Days 2–7 as organic distribution happens."

**Do NOT panic here.** New product accounts always have low reach on Day 1. This is expected.

---

### Launch Outcome: REQUIRES INVESTIGATION

**If any of these are true**:
- <6 Etsy listings published after recovery attempts
- Email broadcast failed and Gmail fallback did not work
- <2 social posts live after recovery attempts
- GA4 shows 0 pageviews and tracking cannot be fixed

**Action**: 
1. Do NOT close the launch
2. Escalate to Orchestrator with: exact metrics, recovery procedures used, and what failed
3. Proceed with whatever systems ARE working (e.g., if Etsy works but social failed, people can still find the listings)
4. Plan recovery for Days 2–3

---

## Escalation Rules

**Escalate to Orchestrator immediately if**:

| Condition | Severity | Time to Escalate | Who to Contact |
|-----------|----------|---|---|
| 3+ Etsy listings fail to publish | CRITICAL | Within 15 min | Orchestrator + screenshot |
| Kit broadcast fails AND Gmail fallback fails | HIGH | Within 15 min | Orchestrator + error message |
| GA4 shows 0 pageviews and tracking code cannot be verified | MEDIUM | Within 30 min | Orchestrator + screenshot |
| Any social platform shows account suspension | CRITICAL | Immediately | Orchestrator + screenshot |
| A failure persists after 60 minutes of troubleshooting using decision trees | HIGH | At 60 min mark | Orchestrator + decision tree reference |
| Multiple platforms show simultaneous failures (Etsy + Kit + Instagram all fail) | CRITICAL | Within 10 min | Orchestrator + summary of all issues |

---

## Decision Tree: When to Escalate

```
START: Launch day metric or system issue
       |
       v
Is this a known platform lag or temporary glitch?
       |
    YES → Wait 5–10 minutes. Check again.
           If resolved: Continue.
           If persists: Go to "Is there a workaround?"
       |
    NO → Has this issue persisted for >30 minutes?
           |
           YES → Is there a documented workaround in LAUNCH_DAY_ROLLBACK_PROCEDURES.md?
                  |
                  YES → Use the workaround. Document outcome.
                        If workaround fixes the issue: Continue.
                        If workaround fails: Go to "Escalate"
                  |
                  NO → Go to "Escalate"
           |
           NO → Continue monitoring. Next checkpoint is [TIME]. Will revisit then.

Escalate:
  1. Take a screenshot or note the exact error
  2. Document: time, failure mode, what you tried, why it failed
  3. Post to #alerts Discord: timestamp + failure + screenshot + reference decision tree
  4. Do NOT continue making changes while waiting for Orchestrator response
```

---

## Metric Tracking Template

Create `LAUNCH_DAY_METRICS.md` on May 30 and fill in as you go:

```markdown
# May 30 Launch Day — Real-Time Metrics Log

**Launch start time**: 08:00 UTC
**Today's date**: May 30, 2026

---

## 08:15 UTC — Etsy Publish Checkpoint

Etsy listings published: ___ of 8
Status: [ ] ON TRACK [ ] RECOVERING [ ] ESCALATED

---

## 10:00 UTC — First Metrics Check

GA4 pageviews (2 hours): ___
Etsy listings discoverable: [ ] YES [ ] NO
Status: [ ] ON TRACK [ ] INVESTIGATING

---

## 14:00 UTC — Mid-Day Checkpoint

GA4 pageviews (6 hours): ___
Instagram reach (impressions): ___
TikTok views: ___
Kit broadcast: [ ] SENT [ ] FAILED [ ] FALLBACK USED
Status: [ ] ON TRACK [ ] DEGRADED [ ] RECOVERING

---

## 18:00 UTC — Evening Checkpoint

GA4 pageviews (10 hours): ___
Kit email opens: ___% (estimate)
Instagram reach (total): ___
Reddit upvotes: ___
Status: [ ] ON TRACK [ ] ACCEPTABLE [ ] INVESTIGATE

---

## 21:00 UTC — Final Summary

**TIER 1 METRICS (Launch Happened?)**
- Etsy listings: ___ of 8 ✓
- Kit broadcast: ✓
- Social posts: ___ of 4 ✓
- GA4 tracking: ✓

**TIER 2 METRICS (How Well?)**
- GA4 pageviews (full day): ___
- Instagram reach: ___
- TikTok views: ___
- Reddit upvotes: ___

**TIER 3 METRICS (Engagement)**
- Kit email CTR: ___% 
- Email-to-Etsy clicks: ___
- Social comments+likes: ___

**Launch Day Outcome**: [ ] SUCCESSFUL [ ] SUCCESSFUL WITH RECOVERY [ ] SUCCESSFUL WITH DEGRADED REACH [ ] REQUIRES INVESTIGATION

**Narrative**:
[Your summary of Day 1 in 2–3 sentences]

**Unresolved Issues** (if any):
[List any known issues and recovery plans for Days 2–3]
```

---

## Day 1–7 Metric Curve (Expected Values)

These are historical baselines for similar new-product organic launches. Use these to contextualize Day 1 results.

| Metric | Day 1 | Day 2 | Day 3 | Day 7 |
|--------|-------|-------|-------|-------|
| GA4 pageviews | 50–500 | 100–800 | 200–1,500 | 500–3,000+ |
| Instagram reach | 50–200 | 100–300 | 200–500 | 500–1,500+ |
| Email opens | 5–20% | 15–30% | 20–40% | 30–50%+ |
| Reddit upvotes | 0–20 | 10–40 | 25–60 | 50–150+ |
| Total revenue | $0–20 | $20–80 | $100–300 | $500–2,000+ |

**Important**: Day 1 is always the lowest. Organic growth accelerates on Days 2–3 as posts gain visibility, influencers see and share, and email subscribers begin opening emails over 24–48 hours.

Do NOT judge launch success by Day 1 metrics alone. Day 3 and Day 7 metrics are more meaningful.

---

## Communication Template: Status Update to Stakeholders

Use this template to post hourly or every-2-hours status updates to LAUNCH_DAY_STATUS_UPDATES.md and Discord:

```markdown
## [HH:MM UTC] — Launch Status Update

**Overall Status**: [ ] ON TRACK [ ] DEGRADED [ ] RECOVERING

**Key Metrics (This Hour)**:
- GA4 pageviews: +___ this hour (cumulative: ___)
- Email opens: ___% (if available from Kit dashboard)
- Social engagement: [Brief summary, e.g., "Instagram: 3 new comments, 1 share"]

**Completed Actions**:
- [ ] [Action] at [Time]

**Known Issues**:
- [Issue 1 + recovery plan]
- [Issue 2 + recovery plan]

**Next Checkpoint**: [Time]

**Notes**: [Any observations, anomalies, interesting patterns]
```

---

## Post-Launch Day (May 31) Quick Reference

**Do this on May 31 morning (06:00 UTC)**:

1. **Collect full Day 1 metrics** from all platforms:
   - GA4: Export pageviews by day
   - Instagram: Check Insights > Impressions, reach, engagement
   - TikTok: Check Analytics > Video plays, average watch time
   - Pinterest: Check Analytics > Outbound clicks
   - Reddit: Check post score and comments
   - Kit: Check final open rate (emails open over 24–48 hours)

2. **Compare to thresholds** in this doc:
   - Did you hit Tier 1 success metrics? → LAUNCH WAS SUCCESSFUL
   - Did you hit Tier 2 "Good" on 2+ metrics? → Strong Day 1
   - Did you hit Tier 2 "Poor" on 3+ metrics? → Normal. Day 1 is always slower. Wait for Day 3.

3. **Plan Day 2–7 activities** based on CONTINGENCY_DECISION_THRESHOLDS.md:
   - Continue daily social posting (follow social calendar)
   - Send follow-up emails if Kit has subscribers
   - Monitor Day 3 checkpoint (June 2, 20:00 UTC) for influencer activation decision

4. **Update CHECKIN.md** with Day 1 summary (see LAUNCH_DAY_STATUS_TEMPLATE.md for format)

---

*Prepared: May 27, 2026. Seedwarden Launch Operations.*
*Companion docs: LAUNCH_DAY_HOUR_BY_HOUR_RUNBOOK.md, CONTINGENCY_DECISION_THRESHOLDS.md*
