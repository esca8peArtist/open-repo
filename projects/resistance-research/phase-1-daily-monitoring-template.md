---
title: "Phase 1 Daily Monitoring Template"
subtitle: "One-page fill-in-ready daily report — 10 minutes to complete"
created: 2026-05-17
status: production-ready — active from May 18 first send
scope: "Day 1–7 post-distribution daily monitoring for Wave 1 Batch 1 (5 contacts) through Wave 1 completion"
audience: "thorn — fill once daily at 20:00 UTC May 18–24"
companion_files:
  - phase-1-measurement-day-0-checklist.md
  - WAVE_1_MONITORING_DASHBOARD.md
  - PHASE_1_DISTRIBUTION_MEASUREMENT_PLAYBOOK.md
  - DISTRIBUTION_EXECUTION_LOG.md
estimated_fill_time: "10 minutes per day"
---

# Phase 1 Daily Monitoring Template

**Fill this once per day at 20:00 UTC.** Copy the blank template for each new day. Paste completed versions into `DISTRIBUTION_EXECUTION_LOG.md` as your daily log entry.

Days covered by this template: **May 18 (Day 1) through May 24 (Day 7)**, the Day 7 weekly synthesis trigger.

---

## Blank Daily Template — Copy for Each Day

```
PHASE 1 DAILY MONITORING REPORT — [DATE] — Day [N]

=== SENDS TODAY ===
Sent today (new contacts):             [ ] / 45 total Tier 1 target
Cumulative sent (all batches):         [ ]
Batch 1 / Batch 2 / Batch 3:          [ ] / [ ] / [ ]

=== DELIVERY STATUS ===
Bounces today:                         [ ]
Cumulative bounce count:               [ ]
Bounce rate (%):                       [ ]%   THRESHOLD: >10% = STOP and diagnose
OOO replies received today:            [ ]   (confirms delivery — log sender names)
OOO senders:                           [name(s) or "none"]

=== ENGAGEMENT SIGNALS TODAY ===
New replies received:                  [ ]
Cumulative replies:                    [ ]
Running reply rate:                    [ ]%   TARGET: ≥15% by Day 7 (Path A+37)
New Gist clicks (Bitly or estimate):   [ ]
Cumulative Gist views (delta from baseline):  +[ ] views across all 8 Gists
Domain 37 Gist views (delta):          +[ ]   NOTE: Domain 37 should lead all individual Gists

=== REPLY CLASSIFICATION (fill one row per reply received today) ===
Contact | Org | Reply Type | Score (0–5) | Domains Mentioned | Tier 2? | Key Quote
--------|-----|-----------|-------------|------------------|---------|----------
[name]  | [org] | [type]  | [0–5]       | [domain#s]       | Y/N/M   | "[quote or paraphrase]"

Reply Type options: Integration / Implementation / Referral / Clarification / Critique / Acknowledgment / Decline / None

=== SECTOR BREAKDOWN (cumulative) ===
Law Schools: sent [ ], replied [ ], reply rate [ ]%   SECTOR TARGET: ≥20% by Day 14
Policy Orgs: sent [ ], replied [ ], reply rate [ ]%   SECTOR TARGET: ≥18% by Day 7
Immigration Legal: sent [ ], replied [ ], reply rate [ ]%
Election Orgs: sent [ ], replied [ ], reply rate [ ]%   SECTOR TARGET: ≥25% by Day 10 (Path A+37)
Congressional Staff: sent [ ], replied [ ], reply rate [ ]%

=== ANOMALY FLAGS ===
[Check each — mark Y if present, N if not present]
Bounce rate >10%:                      Y / N   — If Y: STOP, diagnose (see Contingency Block A)
Sector with 5+ sends showing 0% reply by Day 5:  Y / N   — If Y: sector contingency (see Block B)
Zero Gist views AND zero replies AND no OOO at H+48:  Y / N   — If Y: delivery failure (see Block C)
2+ contacts raising same objection:    Y / N   — If Y: framing review (see Block D)
Multiple contacts from same org replying independently:  Y / N   — If Y: cascade signal (flag Tier 2)
Single contact who forwarded to 3+ colleagues:  Y / N   — If Y: bridge node (log in Tier 2 section)

=== TIER 2 CANDIDATE UPDATE ===
New Tier 2 candidates identified today:  [ ]
Cumulative Tier 2 candidates:             [ ]   TARGET: 3–5 by Day 7

New candidates today:
  Contact: [name] — [org]
  Criteria met: Integration signal / Engagement score 3+ / Network multiplier (circle met)
  Score: [ ] / 5
  Next action: Follow-up by [date] with [what — domain extract / call offer / coalition frame]

=== POLICY UPTAKE SIGNALS ===
New policy uptake signals today:       [ ]
Cumulative policy uptake signals:      [ ]   TARGET: 1+ by Day 3; 3+ by Day 7

Signal description: [Contact name] — [what they said they'll do — be specific]
Work product mentioned: [brief / testimony / hearing / report / case / none]
Follow-up required by: [date — within 5 business days if signal is explicit integration]

=== DOMAIN PULL DISTRIBUTION (cumulative) ===
Which domains have been mentioned by name in replies?
(update this running list — it directly informs Phase 2 sequencing)

Domain | Times Mentioned | By Whom
-------|----------------|--------
1      |                |
6      |                |
37     |                |   TARGET: Domain 37 should lead (Path A+37 hypothesis)
28     |                |
29     |                |
57     |                |
58     |                |
[other]|                |

=== DECISION POINT FOR TODAY ===
[Circle one, then fill the action]
GREEN — all metrics on track, no anomaly flags: No action required. Continue monitoring.
YELLOW — 1 metric below threshold OR 1 anomaly flag: [describe the flag and the corrective]
RED — bounce rate >10% OR zero signals at H+48 OR 2+ same objection: [describe contingency triggered]

Today's status: GREEN / YELLOW / RED

If YELLOW or RED, action taken today:
[Fill here]

=== TOMORROW'S PRIORITY ===
[What is the most important monitoring action tomorrow?]
[Fill here — example: "Check Weiser / Chenoweth for first reply (Day 5 for law school contacts)"]

=== TIME SPENT TODAY ===
Monitoring and logging:  [ ] minutes
Responding to contacts:  [ ] minutes
Total:                   [ ] minutes   (target: <15 min monitoring + <30 min responses = <45 min/day)
```

---

## Decision Thresholds — Quick Reference

Use this table to determine whether an anomaly requires a contingency action or just a note.

| Metric | Threshold | Day | Action if Breached |
|--------|-----------|-----|-------------------|
| Bounce rate | >10% (>1 of first 10 sends) | Any | STOP sends. Diagnose delivery. See PHASE_1_CONTINGENCY_STRATEGY.md Trigger 1 |
| Overall reply rate | <8% at H+72 (Day 3) | Day 3 | Deploy follow-up diagnostic (see Contingency Block B) |
| Overall reply rate | <12% by Day 7 | Day 7 | Run sector-specific retargeting before Batch 2 scale |
| Gist views (total delta) | <5 views above baseline by Day 3 | Day 3 | Delivery suspect — run self-test; check spam |
| Election org reply rate (Path A+37) | <15% by Day 10 | Day 10 | Pivot to battleground-state orgs (PA, MI, WI, AZ, NV) |
| Law school reply rate | <15% by Day 14 | Day 14 | Pivot to dept chairs and faculty centers |
| Same objection from 2+ contacts | Any occurrence | Any | Halt affected template — review framing before Batch 2 |
| Zero engagement signals all sectors | Any at H+48 | Day 2 | Delivery failure — check spam, re-verify email addresses |
| Tier 2 candidates | 0 by Day 7 | Day 7 | Lower identification threshold to "1 criterion met" for Day 7–14 window |

---

## Contingency Blocks — Fast Reference

Use these if anomaly flag fires. Full playbooks in linked documents.

### Block A — Bounce Rate >10%
1. Pause all pending sends immediately
2. Open Gmail — filter for "Mail Delivery Subsystem" — identify which addresses bounced
3. Verify each bounced address at institutional website (takes 5 min per contact)
4. For each bounced contact: use alternate address from `PHASE_1_WAVE1_EXECUTION_PREP.md` Section 1
5. Resend to alternate within 24h; reset H+0 clock for that contact
6. If 3+ bounces in same domain (e.g., all .edu): wait 48h before resend — possible domain-level filter
7. Full detail: PHASE_1_CONTINGENCY_STRATEGY.md Trigger 1

### Block B — Low Reply Rate at H+72 (0–1 of 5)
1. Do not yet declare failure — first check: is silence law-school specific? (Law school reply cycle is 5–10 days; absence at Day 3 is normal for Goodman/Chenoweth)
2. If fast-cycle contacts (Elias, Bassin) are ALSO silent: investigate delivery. Check Bitly/Gist for any click signals.
3. If Gist shows clicks but zero replies: content is being read but not generating response — extend window to Day 7 for all contacts before taking remedial action
4. If Gist shows zero clicks AND zero replies AND no OOO: delivery failure suspected — go to Block A
5. Full detail: POST_WAVE_1_PHASE_1_MEASUREMENT_FRAMEWORK.md Section 7 Scenario B

### Block C — Zero Engagement at H+48 (no replies, no OOO, no Gist views)
1. Send test email to yourself from sending account — does it arrive in inbox or spam?
2. If spam: sending account flagged. Move to clean account for resend.
3. If inbox: verify all 5 contact addresses against institutional directories
4. If one address bounced and Gmail filed the notification as spam: addresses may be fine but you missed the bounce
5. Re-verify before resending. This is recoverable.
6. Full detail: POST_WAVE_1_PHASE_1_MEASUREMENT_FRAMEWORK.md Section 7 Scenario A

### Block D — Pattern Objection (2+ Contacts Same Critique)
1. Log both critiques verbatim in Tab 1 Notes column
2. Compare: are they the same factual claim, the same framing concern, or the same ideological objection?
3. Factual claim: check source citation in domain file — if contact is right, fix the Gist immediately; notify both contacts
4. Framing concern: add diagnostic caveat before next batch send; do not revise substantive content
5. Ideological objection: do not revise; document for Phase 2 messaging calibration
6. Pause Batch 2 template prep until correction confirmed
7. Full detail: POST_WAVE_1_PHASE_1_MEASUREMENT_FRAMEWORK.md Section 7 Scenario C

---

## Daily Templates Pre-Filled for Days 1–3

### Day 1 — May 18 Abbreviated Template (first-day priorities only)

```
PHASE 1 DAILY MONITORING — 2026-05-18 — Day 1

SENDS: 5 sent (Goodman, Weiser, Chenoweth, Bassin, Elias)
BOUNCES: [ ]  (check within 2h of last send at 10:30 UTC)
OOO REPLIES: [ ]  (any = positive delivery confirmation)
EARLY REPLIES: [ ]  (unexpected at Day 1 but possible from Elias or Bassin)

GIST VIEW DELTA (baseline vs 20:00 UTC):
  Main proposal: +[ ]
  Domain 37:     +[ ]
  All others:    +[ ] combined
  NOTE: 0–5 total views at Day 1 evening is normal. 10+ is a strong signal.

ANOMALY FLAGS: Bounce rate >10%: Y / N
               Zero signals by H+6: Y / N (if Y, run delivery test)

DAY 1 EXPECTED STATE: 5 sent, 0 bounces, 0 replies, 0–5 Gist views above baseline.
If actual state matches expected: GREEN — no action.

TOMORROW'S FOCUS: H+24 morning check (10:00 UTC May 19) — first reply window opens.
TIME SPENT: [ ] min
```

### Day 2 — May 19 Template

```
PHASE 1 DAILY MONITORING — 2026-05-19 — Day 2

SENDS TODAY: [ ]  (Batch 2 prep, no sends until after H+72 assessment)
CUMULATIVE SENT: 5

BOUNCES DETECTED TODAY: [ ]
OOO REPLIES: [ ]  (OOO from law school = confirms delivery; law school reply expected in 5–10 days)

ENGAGEMENT SIGNALS:
  New replies:         [ ]   ELIAS AND BASSIN are fastest cycle (2–3 days) — a reply today is expected
  Running reply rate:  [ ]%
  Gist view delta H+24: +[ ] views total   TARGET: 5–15 views at H+24 signals contacts opening email

REPLY CLASSIFICATION:
[fill per reply received, using blank template above]

DAY 2 EXPECTED STATE: 0–1 replies (Elias most likely first mover). Gist views 3–15 above baseline.
Zero replies at Day 2 is normal for academic contacts. Check BOTH whether policy orgs (Weiser, Bassin) 
are also silent AND whether Elias (fastest cycle) has replied.

ANOMALY: If Elias AND Bassin are silent AND Gist shows <3 views delta: suspicious — check Block B.

TOMORROW'S FOCUS: H+48 check (10:00 UTC May 20) — preliminary rate calculation.
TIME SPENT: [ ] min
```

### Day 3 — May 20 Template

```
PHASE 1 DAILY MONITORING — 2026-05-20 — Day 3

CUMULATIVE SENT: 5 (Batch 1 complete; Batch 2 pending H+72 PASS/NEAR-MISS determination tonight)
CUMULATIVE BOUNCES: [ ]
CUMULATIVE REPLIES: [ ]
RUNNING REPLY RATE: [ ]%   TARGET: ≥10% (1 of 5 = 20% — above target; 0 = 0% — below target)

H+48 ENGAGEMENT SNAPSHOT:
  Gist views delta from baseline (total): +[ ]
  Domain 37 Gist specifically:            +[ ]   (should be highest individual Gist if Path A+37 is resonating)
  Bitly clicks (if tracking):              [ ]

REPLY ANALYSIS:
[fill per reply received]

PHASE 2 GATE PRELIMINARY STATUS (fill tonight before H+72 determination):
  Tier (a) — Reply rate: PASS (3+ replies) / NEAR-MISS (2) / FAR-MISS (0–1)
  Tier (b) — Forwarding signal: PASS (1+ chain) / MISS (0)
  Tier (c) — Policy uptake signal: PASS (1+ signal) / MISS (0)
  Preliminary determination: PASS / NEAR-MISS / FAR-MISS
  
  If PASS → Batch 2 launch target: May 22
  If NEAR-MISS → Modified Batch 2 strategy (see POST_WAVE_1_PHASE_1_MEASUREMENT_FRAMEWORK.md Section 3 Path B)
  If FAR-MISS → Diagnostic sequence required (Section 7 Scenario A/B)

  Gate 4 — User approval for Phase 2: [decision required tonight before May 22 Batch 2 launch]

DAY 3 EXPECTED STATE: 1–2 replies. Click rate 15–25%. Reply rate 10–20%. 2–4 Tier 2 candidates.
TIME SPENT: [ ] min
```

---

## Weekly KPI Targets — Days 1–7

Use these to answer "are we on track?" at any point during Week 1.

| KPI | Day 1 | Day 2 | Day 3 (H+72) | Day 5 | Day 7 |
|-----|-------|-------|-------------|-------|-------|
| Batch 1 reply rate | 0–20% | 0–40% | **10%+ (PASS gate)** | 20%+ | 40%+ |
| Avg engagement score | N/A | N/A | 2.5+ | 2.5+ | 3.0+ |
| Policy uptake signals | 0 | 0–1 | **1+ (PASS gate)** | 2+ | 3+ |
| Active forwarding chains | 0 | 0–1 | **1+ (PASS gate)** | 1+ | 2+ |
| Tier 2 candidates identified | 0 | 0–2 | 2–3 | 3–4 | **3–5 (target)** |
| Gist view delta (total) | 0–5 | 5–20 | 20–50 | 50–100 | 75–150 |
| Domain 37 leading all individual Gists | — | — | Y/N | Y/N | Y/N |

---

*Prepared: May 17, 2026 — Item 34 (Phase 1 Measurement Staging)*
*Cross-references: PHASE_1_DISTRIBUTION_MEASUREMENT_PLAYBOOK.md (Sections 2–3); POST_WAVE_1_PHASE_1_MEASUREMENT_FRAMEWORK.md (Sections 1–2, 7); WAVE_1_MONITORING_DASHBOARD.md (Sections 1–5); phase-1-week-1-synthesis.md (Week 1 synthesis framework)*
