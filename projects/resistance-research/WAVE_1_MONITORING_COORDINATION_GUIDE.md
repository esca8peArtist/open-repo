---
title: "Wave 1 Post-Distribution Monitoring Coordination Guide"
created: 2026-05-18
status: active — automation running hourly from 10:32 UTC May 18
scope: "May 18-21 real-time engagement tracking. Orchestrator checks for engagement data every hour; user inputs signals as they arrive. Daily rollups at 20:00 UTC."
coordination: "Orchestrator-managed: reads files, processes data, generates summaries. User-provided: email opens/bounces (Bitly), replies (inbox), Gist clicks (analytics)."
---

# Wave 1 Monitoring Coordination Guide

**Distribution window**: May 18–20, 2026 (Batch 1: May 18 08:00–10:00 UTC)
**Monitoring window**: May 18–21, 2026 (72 hours post-send)
**Batch 1 contacts**: 5 pre-verified (Goodman, Weiser, Chenoweth, Bassin, Elias)
**Orchestrator role**: Hourly status checks, data processing, daily summaries
**User role**: Input engagement signals as they arrive (Bitly opens, email replies, Gist analytics)

---

## Section 1: What to Input — Signal Types & Timing

### Opens (Bitly Dashboard / Email Tracking)

**When to check**: Bitly dashboard for click URLs, email tracking for open pixels
**Timeline**: First opens typically appear 1–4 hours after send (May 18 12:00–16:00 UTC)
**For each contact, record**:
- Contact name & organization
- Open timestamp (time email was opened)
- Bitly click timestamp (if Gist link clicked)

**Example entry** (add to WAVE_1_MONITORING_DASHBOARD.md Section 1 table):
```
| 2026-05-18 | Ryan Goodman | Just Security | Email B1 | Opened (24h) | — | 0 | No | Opened 12:15 UTC (4.25h after send) |
```

### Replies (Email Inbox)

**When to check**: Email inbox every 2–4 hours
**Timeline**: First replies typically 24–48h after send (May 19–20), some same-day (May 18 evening)
**For each reply, record**:
- Sender name
- Reply type (see Section 4 classification below)
- Reply quality score (0–5)
- Tier 2 indicator (Yes/No)

**Example entry** (replace "Sent/Pending" with "Replied" and fill reply columns):
```
| 2026-05-18 | Ryan Goodman | Just Security | Email B1 | Replied | Clarification question | 3 | Yes | Asked about Domain 28 methodology; indicates close reading |
```

### Gist Analytics (GitHub Gist Dashboard)

**When to check**: GitHub Gist analytics (click `...` → Views)
**Timeline**: First views typically 2–6 hours after send
**For each Gist, record**:
- Gist title (e.g., "Domain 1 Electoral Systems")
- Total views to date
- Unique visitors
- Timestamp of last view

**Update in**:
- WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv, column `gist_views_48h`
- Daily summary (20:00 UTC) in WAVE_1_MONITORING_DASHBOARD.md Section 2

### Bounces & Delivery Issues (Email Provider)

**When to check**: Email sent folder, bounce notifications
**Timeline**: Bounces appear immediately (0–2 hours after send)
**For each bounce, record**:
- Contact email address
- Bounce reason (invalid, spam, etc.)
- Bounce timestamp

**Update in**:
- WAVE_1_MONITORING_DASHBOARD.md Section 2, "Bounced" counter
- Daily summary (20:00 UTC)

---

## Section 2: Where to Input — File & Location Guide

### Real-Time Input (As Signals Arrive)

**File**: `WAVE_1_MONITORING_DASHBOARD.md` → Section 1: Daily Tracking Table
**Cadence**: Update as signals arrive (opens: every 2h; replies: check inbox 2x/day)
**Format**: Add rows to the table for each new signal. Use template provided in dashboard file.

### Daily Aggregation (20:00 UTC Each Day)

**File**: `WAVE_1_MONITORING_DASHBOARD.md` → Section 2: Real-Time Status Summary
**Cadence**: Once daily at 20:00 UTC (May 18, 19, 20)
**Content**:
- Cumulative sends, opens, clicks, replies
- Engagement breakdown by contact and sector
- Early warning signals (bounces, non-engagement)
- Observations for next 24h

**Format**: Copy this template and fill in:
```
### Agent Monitoring Pass — May 18, 2026, ~20:00 UTC

SENDS
  Sent today:                   5 (Batch 1)
  Cumulative sent:              5 / 45 total Tier 1 target
  Batch 1 (credibility anchors): 5 / 5 COMPLETE

DELIVERY
  Bounced:                      [number]
  Bounce rate:                  [%]
  Delivered confirmed:          [number]

ENGAGEMENT SIGNALS
  Opened (24h window):          [number]
  Gist clicked (48h window):    [number]
  Replied:                      [number]
  Replied substantively (2+):   [number]

OBSERVATIONS & NEXT STEPS
  [Write 2-3 sentences about what engagement patterns you see so far. What's working? What's surprising?]
  [Any immediate adjustments needed for Batch 2 timing or messaging?]
```

### CSV Scoring (Daily, End-of-Day)

**File**: `WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv`
**Cadence**: Once daily at 20:00 UTC (aggregate all signals from that day)
**Content**: Update columns for each contact:
- `date_sent` → contact's send date
- `opened_within_24h` → boolean (Yes/No) or timestamp
- `gist_views_48h` → integer count
- `reply_received` → boolean (Yes/No)
- `reply_type` → classification (Q, Critique, Ack, Integration, etc.)
- `score_0_5` → engagement quality 0–5
- `tier_2_candidate` → boolean (Yes/No)
- `notes` → any relevant observations

**Format**: Rows already pre-populated for Batch 1 contacts. Just update columns as data arrives.

---

## Section 3: Daily Monitoring Checklist (What the Orchestrator Does)

**10:32 UTC (NOW — May 18)**: Orchestrator activation
- ✅ Monitoring infrastructure verified (dashboard, CSV, templates present)
- ✅ Batch 1 sends confirmed (5 emails sent, 08:00–10:00 UTC)
- ✅ This guide created
- ⏳ **First hourly check scheduled for 11:32 UTC** (1h after Wave 1 close)

**Hourly checks (11:32 UTC onwards, May 18–21)**:
1. Read WAVE_1_MONITORING_DASHBOARD.md for user input
2. If new engagement signals present: process and update CSV
3. If CSV has been updated: calculate running score + Tier 2 indicators
4. Log status to WORKLOG.md every 4 hours

**Daily aggregation (20:00 UTC each day, May 18–20)**:
1. Tabulate all engagement signals from past 24h
2. Update Section 2 (Status Summary) in WAVE_1_MONITORING_DASHBOARD.md
3. Calculate cumulative opens %, reply rate %, average score
4. Identify patterns: are opens fast/slow? Are replies substantive?
5. Flag any Tier 2 candidates (score 4+ or integration signals)
6. Write 3-5 sentence observation block (what surprised you? what worked?)
7. Suggest next actions (Batch 2 timing, Batch 3 adjustment)
8. Commit dashboard + CSV to master

**May 21, 20:00 UTC (Final monitoring pass)**:
1. Aggregate all 72h engagement data
2. Calculate Phase 2 decision triggers:
   - STRONG: ≥60% reply rate, ≥3 Tier 2 candidates, integration signals present
   - MODERATE: 30-59% reply rate, 1-2 Tier 2 candidates
   - WEAK: <30% reply rate, 0 Tier 2 candidates, mostly silence
3. Write final summary to PHASE_2_LAUNCH_DECISION_TRIGGERS.md
4. Flag user for May 25 checkpoint decision (STRONG/MODERATE/WEAK path selection)

---

## Section 4: Reply Type Classification (For Your Reference)

When you reply to an email and classify it, use these categories:

| Category | Description | Score | Tier 2? |
|----------|-------------|-------|---------|
| Q — Clarification | Asks for more detail on a domain, methodology, or framing | 3 | Possible — watch for follow-up |
| Critique | Substantive methodological or factual pushback | 3 | Possible — high-value signal |
| Ack — Acknowledgment | "Thanks, I'll read it" or similar with no follow-up content | 1 | No |
| Integration signal | Mentions using research in their work, case, testimony, publication | 5 | **Yes** |
| Implementation | Asks how to use framework operationally (clinic, brief, coalition) | 4 | **Yes** |
| Referral | Connected you to a colleague or organization | 4 | **Yes** — track secondary contact |
| Decline | Opted out or said not relevant | 0 | No — note reason |
| None | No reply in tracking window | 0 | No |

---

## Section 5: Tier 2 Escalation Triggers

A contact becomes a "Tier 2 candidate" if they show any of these signals:
1. **Integration signal** (mentioning use in their work) — immediate escalation
2. **Implementation question** (asking how to use operationally) — immediate escalation
3. **Referral** (connecting you to colleague/org) — track secondary contact
4. **Critique + follow-up** (substantive pushback with follow-up question within 24h) — possible escalation
5. **Clarification + fast reply** (question asked + answered within 6h, rapid iteration) — possible escalation

Any contact meeting criteria 1–3 becomes automatic Tier 2 candidate. Criteria 4–5 require human judgment (user input in notes column).

---

## Section 6: Orchestrator Availability

**Hourly monitoring active**: May 18, 10:32 UTC — May 21, 20:00 UTC
**How to provide input**:
1. Add rows to WAVE_1_MONITORING_DASHBOARD.md Section 1 table as signals arrive
2. Update CSV columns for each contact once daily (before 20:00 UTC)
3. No special format required — free-form data entry, orchestrator will process

**If no new signals by 22:00 UTC**: Orchestrator will note in WORKLOG.md ("no engagement by 22h mark — normal for law school contacts"), continue hourly checks

**If engagement patterns shift**: Orchestrator will update Phase 2 decision framework in real-time

---

## Section 7: Key Dates & Decision Windows

| Date | Event | Action |
|------|-------|--------|
| May 18, 08:00–10:00 UTC | Wave 1 sends (Batch 1) | ✅ Complete |
| May 18, 10:32 UTC onwards | Hourly monitoring begins | Orchestrator active |
| May 18–20, 20:00 UTC | Daily aggregation | Run daily monitoring pass |
| May 21, 20:00 UTC | Final 72h summary | Calculate STRONG/MODERATE/WEAK signals |
| May 25, 09:00 UTC | Week 1 checkpoint | User decides Phase 2 path (or earlier if STRONG signals) |
| May 20 or 21, evening | Batch 2 decision | User approves timing based on Batch 1 momentum |

---

## Section 8: What Success Looks Like

**By end of May 21 (72h window)**:

| Metric | STRONG | MODERATE | WEAK |
|--------|--------|----------|------|
| Reply rate | ≥60% | 30–59% | <30% |
| Open rate (estimated) | ≥80% | 50–79% | <50% |
| Tier 2 candidates | ≥3 | 1–2 | 0 |
| Integration signals | 1+ | 0 | 0 |
| Notes | Users actively discussing, asking implementation questions | Some interest, curious questions, no commitments | Silence or polite acknowledgments only |

**Action implications**:
- **STRONG**: Batch 2 send May 20 (accelerate). Phase 2 prepped for early launch.
- **MODERATE**: Batch 2 send May 21 (on schedule). Phase 2 decision May 25.
- **WEAK**: Hold Batch 2, revise messaging, re-evaluate May 25 before proceeding.

---

*Last updated by orchestrator: May 18, 2026, 10:32 UTC*
