---
title: "Track B Day 3 Decision Logic Flowchart — June 8, 2026"
created: 2026-06-06
status: pre-staged
execution-date: 2026-06-08
purpose: >
  If-then decision logic for Day 3 checkpoint (June 8). Takes filled-in
  TRACK_B_JUNE_8_CHECKPOINT_METRICS_TEMPLATE.md and routes to:
  - Continue normal execution (GO)
  - Monitor with contingency plan (CAUTION)
  - Execute remediation immediately (NO-GO)
  Execution time: 2–3 minutes to route.
---

# Track B Day 3 Decision Logic Flowchart
**Checkpoint**: June 8, 2026 at 08:00 UTC  
**Input**: Metrics from TRACK_B_JUNE_8_CHECKPOINT_METRICS_TEMPLATE.md  
**Output**: GO / CAUTION / NO-GO with specific next action

---

## Quick Decision Matrix

Fill in metrics. Locate your combination below. Follow the arrow.

| Email Open Rate | Gist Views | Influencer Activity | Sales/Kit | **DECISION** |
|---|---|---|---|---|
| GO (≥20%) | GO | GO | GO | ✅ **GO** → Continue calendar |
| GO | GO | GO | CAUTION | ✅ **GO** → Continue calendar |
| GO | GO | CAUTION | * | ✅ **GO** → Continue + monitor influencers |
| GO | CAUTION | * | * | ⚠️ **CAUTION** → Execute Scenario 2 (Gist) |
| CAUTION | * | * | * | ⚠️ **CAUTION** → Execute Scenario 1 (Email) |
| NO-GO | * | * | * | 🔴 **NO-GO** → Execute Scenario 1 (Email) + escalate |
| * | NO-GO | * | * | 🔴 **NO-GO** → Execute Scenario 2 (Gist) + escalate |
| * | * | NO-GO | * | 🔴 **NO-GO** → Execute Scenario 3 (Influencers) + escalate |

---

## Decision Flowchart (Detailed)

### START: Review metrics from template

**Q1: Is email open rate ≥ 20%?**

```
YES → Q2
NO  → Is email open rate 10–19%? YES → CAUTION (See Scenario 1 below)
                                NO  → NO-GO (See Scenario 1 below)
```

---

### Q2: Is Gist view count > 70?

```
YES → Q3
NO  → Is Gist view count 30–70? YES → CAUTION (See Scenario 2 below)
                                 NO  → NO-GO (See Scenario 2 below)
```

---

### Q3: Did influencer activity reach GO threshold?

```
GO (≥1 public share) → Q4
CAUTION (responses but no public shares) → CAUTION (See Scenario 3 below)
NO-GO (0 responses from all 15) → NO-GO (See Scenario 3 below)
```

---

### Q4: Did Kit + Etsy reach GO threshold?

```
GO (≥5 Kit subscribers OR ≥1 Etsy order) → **OVERALL: GO** ✅
CAUTION (Kit: 1–4 subscribers, OR Etsy: views but 0 orders) → **OVERALL: CAUTION** ⚠️
NO-GO (Kit: 0 subscribers AND Etsy: listing Draft/not created) → **OVERALL: NO-GO** 🔴
```

---

## Decision Outcomes

### ✅ OVERALL: GO

**All thresholds passed. Continue normal execution.**

**Actions**:
1. Log in CHECKIN.md: "Track B Day 3 checkpoint: GO on all metrics. Continue calendar execution."
2. Continue social calendar per SOCIAL_CALENDAR.md (scheduled posts June 8–14)
3. Plan Day 7 checkpoint execution for June 11 at 08:00 UTC
4. No contingency execution required

**Expected status**: Metrics on track. Phase 2 decision (launch Phase 2 content) can proceed if Day 7 also confirms GO.

---

### ⚠️ OVERALL: CAUTION

**At least one metric is in CAUTION range. Execute specific scenario response. Continue monitoring.**

**What to do**:
1. Identify which metric(s) triggered CAUTION
2. Find the matching Scenario number below
3. Execute the CAUTION response (2–5 minutes)
4. Log actions in CHECKIN.md
5. Re-assess at Day 7 checkpoint

**If two metrics trigger CAUTION simultaneously**: Execute both scenario responses. Do not skip either.

**If one metric is NO-GO and another is CAUTION**: Jump to NO-GO section. The NO-GO dominates.

---

### 🔴 OVERALL: NO-GO

**One or more metrics failed NO-GO threshold. Execute immediate remediation.**

**What to do**:
1. Identify which metric(s) triggered NO-GO
2. Find the matching Scenario number below
3. Execute the NO-GO response (5–15 minutes)
4. Escalate to user per TRACK_B_JUNE_8_CONTINGENCY_ESCALATION_PROTOCOL.md
5. Plan rapid re-check (same day if possible, before Day 7 checkpoint)

**If two metrics trigger NO-GO simultaneously**: See Scenario 8 (Multi-Failure Escalation) in CONTINGENCY_TRIGGER_DECISION_TREE.md before executing individual responses.

---

## Scenario Reference Card

| Scenario | Metric | NO-GO Trigger | CAUTION Response | NO-GO Response |
|----------|--------|---------------|------------------|--|
| 1 | Email open | <10% | Revise subject line, send re-engagement | Check SPF/DKIM, send via Gmail to Tier 1, fix deliverability |
| 2 | Gist views | <30 views | Cross-post to r/homesteading (Reddit), monitor URL placement | Create Etsy test listing, post to Pinterest, test alternate channels |
| 3 | Influencers | 0 responses from all 15 | Continue outreach manually, DM non-responders | Revise message framing, escalate to user for contact refresh |
| 4 | Kit subscribers | 0 (if Etsy also 0) | Ensure Kit CTA is live, check Kit automations | Pivot to Kit-gated PDF as primary monetization path |

**→ For full details on each scenario, see CONTINGENCY_TRIGGER_DECISION_TREE.md**

---

## Quick-Check Thresholds (Copy to phone)

**Paste this into your notes for Day 3 at 08:00 UTC**:

| Metric | GO | CAUTION | NO-GO |
|--------|----|---------| |
| Email open % | ≥20% | 10–19% | <10% |
| Gist views | >70 | 30–70 | <30 |
| Influencer shares | ≥1 public share | Responses, no shares | 0 responses |
| Kit subscribers | ≥5 | 1–4 | 0 |
| Etsy orders | ≥1 | Views, no orders | None |

---

## Example Walk-Through

**Scenario: You fill in metrics on June 8 at 08:00 UTC**

- Email open rate: 18%  
- Gist views: 52  
- Influencer shares: 2 accounts confirmed they will share today (but not shared yet)  
- Kit subscribers: 3  
- Etsy orders: 0  

**Decision path**:
1. Q1: Is email ≥20%? NO → Is email 10–19%? YES → CAUTION
2. Stop here. Email is CAUTION, so overall decision is at least CAUTION.
3. Check: Any NO-GO metrics? Gist (52 = CAUTION), Influencers (responses = CAUTION), Kit (3 = CAUTION), Etsy (0 = normal for Day 3).
4. **Overall: CAUTION** → Execute Scenario 1 (Email) response
5. Action: Revise email subject line, send re-engagement to non-openers within 24 hours
6. Log: "Day 3 checkpoint: CAUTION on email open (18%). Executing re-engagement campaign with revised subject line. Other metrics on track. Continue calendar."
7. Schedule Day 7 re-check for June 11

---

## Next Steps After Decision

**If GO**: Proceed to Day 7 checkpoint planning (June 11)  
**If CAUTION**: Execute scenario, monitor for escalation, Day 7 re-check mandatory  
**If NO-GO**: Execute scenario, escalate per protocol, re-check same-day if possible  

---

**Decision made by**: ___________ | **Date/Time**: ___________ | **Overall Status**: ☐ GO ☐ CAUTION ☐ NO-GO
