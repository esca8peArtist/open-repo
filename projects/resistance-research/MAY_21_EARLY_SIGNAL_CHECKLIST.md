---
title: "May 21 Early-Signal Checklist — Wave 1 Monitoring (May 18–21)"
item: "61-companion"
created: 2026-05-18
status: STAGED — do not execute until May 21 10:30 UTC
scope: "72-hour monitoring window metrics: what to track, where it lives, who captures it, decision moment"
monitoring_window: "May 18 10:32 UTC — May 21 10:30 UTC"
decision_moment: "May 21 10:30 UTC (collect) → 10:45 UTC (classify) → 11:00 UTC (activate path) → 14:00 UTC (user confirms Phase 2)"
primary_decision_doc: "WAVE_1_SYNTHESIS_FRAMEWORK.md (Item 61)"
---

# May 21 Early-Signal Checklist

**Purpose**: Operational staging document for the May 18–21 monitoring window. Answers four questions: what metrics are we tracking, where are they recorded, who tracks them, and what happens at the decision moment. Do not execute this checklist until May 21 10:30 UTC. Use WAVE_1_MONITORING_DASHBOARD.md for daily monitoring during May 18–20.

---

## PART 1: Metrics Being Tracked (May 18–21)

Six metrics are active during the 72-hour window. Each has a defined data source and a defined threshold that feeds the May 21 classification.

### Metric 1 — Substantive Reply Count (Score 3+)

**What it is**: A reply that goes beyond acknowledgment — includes a clarification question, substantive critique, implementation request, referral to a colleague, or citation in work product.

**Scoring guide**:
- Score 5 (Integration): Contact cited the research in a filing, brief, publication, or testimony. One Score 5 = STRONG override regardless of all other metrics.
- Score 4 (Implementation / Referral): Contact asked how to operationalize the framework, or said they are forwarding to a colleague or AG contact.
- Score 3 (Substantive question): Contact asked a specific question referencing a domain by number, or raised a methodological critique.
- Score 1-2 (Acknowledgment): "Thanks, will read" or generic interest. Does NOT count toward the quality reply threshold.
- Score 0 (Silence): No reply. Normal for law school contacts through Day 10.

**Where recorded**: Email inbox (primary), WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv (authoritative log), WAVE_1_MONITORING_DASHBOARD.md Section 1 daily table.

**Who captures it**: User reviews inbox. Orchestrator can prompt with: "Log any replies in WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv with the verbatim quote and your score assignment before May 21 10:30 UTC."

**Decision threshold**: 3+ quality reply points = STRONG; 1-2 quality reply points = MODERATE; 0 = WEAK (pending delivery check).

---

### Metric 2 — Acknowledgment-Only Reply Count (Score 1-2)

**What it is**: Replies that confirm delivery and interest but contain no substantive content. "Thanks, I'll take a look" is the canonical example.

**Where recorded**: Email inbox, WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv (Reply Type column: "Ack").

**Who captures it**: User reviews inbox.

**Decision threshold**: Acknowledgment replies do NOT contribute to quality reply points. They confirm delivery is working. One acknowledgment reply lifts a WEAK classification to MODERATE (borderline) only if combined with Gist delta > 10.

---

### Metric 3 — Hard Bounce Count

**What it is**: Non-delivery notification from the receiving mail server. Indicates a permanently invalid address.

**Where recorded**: Email inbox (bounce notifications arrive as email). Log in WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv Email Status column ("Bounce").

**Who captures it**: User reviews inbox. Bounces can arrive 24-72 hours after send — check the full inbox, not just unread mail.

**Decision threshold**: 0 bounces = proceed normally. 1 bounce = note alternate address from DISTRIBUTION_OUTREACH_CONTACTS.md before classifying; remove from adjusted contact count. 2+ bounces = PAUSE — fix delivery before classifying. Bounce count does NOT signal content failure.

**Alternate addresses** (pre-verified):
- Ryan Goodman: ryan@justsecurity.org (alternate for ryan.goodman@nyu.edu)
- Wendy Weiser: via Brennan Center contact form (wweiser@brennancenter.org is primary, confirmed May 14)
- Erica Chenoweth: erica_chenoweth@hks.harvard.edu (underscore required — do not omit)
- Ian Bassin: ian@protectdemocracy.org (confirmed May 14)
- Marc Elias: melias@elias.law (NOT perkinscoie.com — that address is stale)

---

### Metric 4 — OOO (Out of Office) Reply Count

**What it is**: Automated out-of-office or vacation reply.

**Where recorded**: Email inbox. Log in WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv Notes column with return date.

**Who captures it**: User reviews inbox.

**Decision threshold**: OOO contacts are removed from the adjusted contact count (they are pending, not failures). Subtract OOO count from 5 before calculating reply rate. If Weiser or Elias are OOO, the effective denominator for classification drops accordingly. Reschedule follow-up for return date + 1 business day.

---

### Metric 5 — Gist View Delta (Bitly Click Count)

**What it is**: The net increase in Gist link clicks since May 18 send time, as measured in the Bitly dashboard. Proxy for open-but-did-not-reply engagement — confirms delivery and content interest without a direct reply.

**Where recorded**: Bitly dashboard (bitly.com/dashboard). Baseline was recorded at May 18 pre-send. Net delta = post-send count minus baseline.

**Who captures it**: User checks Bitly dashboard. No orchestrator access to Bitly — this is a manual check.

**Decision threshold**:
- Gist delta > 10 with zero quality replies = MODERATE (borderline) — someone is reading, even if not replying
- Gist delta > 5 with 1 quality reply = confirms MODERATE
- Gist delta = 0 with zero quality replies AND zero bounces = suspected delivery failure — run delivery check before confirming WEAK

**Note**: If baseline Gist view count was not recorded before the May 18 send, use the May 18 10:30 UTC count as proxy. Any views above that baseline count toward the delta.

---

### Metric 6 — Integration / Referral Signal Count (Score 4-5)

**What it is**: The highest-value signal type. A contact who cites the research in a document, forwards it to a colleague by name, or asks how to incorporate it into ongoing litigation or advocacy.

**Where recorded**: Email inbox. Verbatim quote logged in WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv Notes column. Cross-reference in WAVE_1_MONITORING_DASHBOARD.md Section 1 Tier 2 column (mark "Yes").

**Who captures it**: User reviews inbox and logs verbatim quote.

**Decision threshold**: ONE Score 5 signal = STRONG override. ONE Score 4 signal contributes 2 quality reply points. Any integration/referral signal triggers immediate Batch 2 preparation regardless of all other metrics.

---

## PART 2: Where Metrics Are Recorded

| Metric | Primary Location | Authoritative Log | Access |
|--------|-----------------|-------------------|--------|
| Substantive replies (Score 3+) | Email inbox | WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv | User email + CSV |
| Acknowledgment replies (Score 1-2) | Email inbox | WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv | User email + CSV |
| Hard bounces | Email inbox (bounce notifications) | WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv | User email + CSV |
| OOO replies | Email inbox (auto-replies) | WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv Notes | User email + CSV |
| Gist view delta | Bitly dashboard | Note in WAVE_1_MONITORING_DASHBOARD.md Section 2 | Manual Bitly check |
| Integration signals (Score 4-5) | Email inbox | WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv (verbatim) | User email + CSV |

**Email replies are sent to**: The sending address used for the May 18 Batch 1 emails. Replies go to the sender's inbox by default — there is no separate monitoring inbox. All reply tracking is manual review of the user's outbound email account.

**No automated parsing**: The monitoring infrastructure is manual. The orchestrator cannot access the email inbox, the Bitly dashboard, or real-time reply content. The user must review the inbox and log signals in the CSV. The orchestrator reads the CSV and dashboard files to prepare analysis when given the data.

---

## PART 3: Who Tracks What

| Action | Responsible | Timing | How |
|--------|------------|--------|-----|
| Check inbox for replies, bounces, OOOs | User | Daily at 20:00 UTC (or earlier if notified) | Open email client, review incoming messages |
| Log replies in WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv | User | Same session as inbox check | Fill columns: Reply Received, Reply Date, Reply Type, Engagement Score, Notes (verbatim) |
| Check Bitly dashboard for Gist delta | User | Daily at 20:00 UTC | Open bitly.com/dashboard, note total clicks across all Gist links shared in Batch 1 emails |
| Record daily summary in WAVE_1_MONITORING_DASHBOARD.md Section 2 | User or orchestrator (if user provides data) | Daily at 20:00 UTC | Fill the real-time status block |
| Run May 21 classification | Orchestrator (using user-provided data) OR user following WAVE_1_SYNTHESIS_FRAMEWORK.md | May 21 10:30–10:45 UTC | Follow WAVE_1_SYNTHESIS_FRAMEWORK.md Section 3 decision table |
| Activate Batch 2-3 path | User | May 21 11:00 UTC | Open relevant Section 4 in WAVE_1_SYNTHESIS_FRAMEWORK.md, queue emails from execution/phase-1-personalized-batch-2.md |
| Confirm Phase 2 research path | User | May 21 14:00 UTC | Explicit confirmation to orchestrator |

**Daily monitoring schedule during May 18-21**:
- May 18 (Day 0): Emails sent 08:00-10:00 UTC. No reply expected within first hours. Check at 20:00 UTC.
- May 19 (Day 1): Policy org contacts (Weiser, Bassin) are in their expected response window. Check at 09:00 UTC and 20:00 UTC.
- May 20 (Day 2): Marc Elias at the outer end of his 48h window. Provisional classification available if 2+ substantive replies are in. Check at 09:00 UTC (provisional classification for MAY_21_31_BATCH_2_3_COORDINATION_FRAMEWORK.md Section 6 early gate) and 20:00 UTC.
- May 21 (Day 3): 10:30 UTC — monitoring window closes. Collect all 6 metrics. Run final classification per WAVE_1_SYNTHESIS_FRAMEWORK.md.

---

## PART 4: Decision Moment — May 21 10:30 UTC

### The Sequence (30-minute window)

```
10:30 UTC — Monitoring window closes
  Action: Open inbox. Open Bitly dashboard.
  Collect all 6 metrics from WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv.
  Verify CSV is fully populated (every row for Batch 1 filled, even if Score = 0).

10:45 UTC — Classify
  Action: Open WAVE_1_SYNTHESIS_FRAMEWORK.md Section 3.
  Run the classification decision table (top to bottom, stop at first match).
  Fill in the classification record block (Section 3.4).
  If WEAK suspected: run delivery check (Section 3.2) before confirming.
  Note law school window: Goodman and Chenoweth silence at 72h is expected and does not penalize classification.

11:00 UTC — Activate path
  STRONG → Open Section 4A. Pull execution/phase-1-personalized-batch-2.md Priority Group 1.
            Queue 5 sends for today. Queue Domain 42 state AG emails in parallel.
  MODERATE → Open Section 4B. Pull Priority Group 1 contacts. Queue for May 21-22 send.
             Queue Domain 42 state AG emails (path-independent, send today).
  WEAK → Open Section 4C. Do NOT send Batch 2. Log WEAK in CHECKIN.md "Needs Your Input."
          Send Domain 42 state AG emails regardless (deadline exception).
          Begin delivery diagnostic.

  ALL PATHS → Update CHECKIN.md with: classification result, path activated, "awaiting 14:00 UTC user confirmation."

14:00 UTC — User decision gate
  User confirms: "Proceed with [STRONG / MODERATE / WEAK] path."
  User confirms Phase 2 research start date.
  User confirms Domain 42 coordination is active.
```

### Buffer Window

The 30-minute buffer (10:30–11:00 UTC) is analysis time, not a delay. If signals are unambiguous (e.g., 3+ quality replies already logged by May 20 morning), the classification can proceed earlier. The 10:30 UTC gate is the outer boundary of the monitoring window, not a mandatory waiting point.

The 14:00 UTC gate is a hard user-confirmation requirement. No Phase 2 research sprints and no large Batch 2 send sequences begin without explicit user confirmation at this gate.

---

## PART 5: Scenario Quick-Reference

At 10:30 UTC May 21, one of the following scenarios is active. Use this table to jump directly to the correct path.

| What you see in inbox + Bitly | Classification | Immediate document to open |
|-------------------------------|----------------|---------------------------|
| 1+ contact cited research in a filing or named a colleague (Score 5 or 4 with specific referral) | STRONG | WAVE_1_SYNTHESIS_FRAMEWORK.md Section 4A |
| 2-3 substantive replies (Score 3+) from policy orgs or Elias | STRONG | WAVE_1_SYNTHESIS_FRAMEWORK.md Section 4A |
| 1 substantive reply (Score 3+) from any contact | MODERATE | WAVE_1_SYNTHESIS_FRAMEWORK.md Section 4B |
| 0 substantive replies but 1+ acknowledgments OR Gist delta > 5 | MODERATE (borderline) | WAVE_1_SYNTHESIS_FRAMEWORK.md Section 4B |
| 0 substantive replies, 0 acknowledgments, 0 bounces, some Gist clicks | WEAK (pending delivery check) | WAVE_1_SYNTHESIS_FRAMEWORK.md Section 3.2 then 4C |
| 0 replies, 0 Gist clicks, 0 bounces — full silence | WEAK — suspected technical failure | WAVE_1_SYNTHESIS_FRAMEWORK.md Section 3.2 (delivery check first) |
| 1+ hard bounces received | PAUSE | Fix delivery. Check alternate addresses (Part 1, Metric 3 above). |

**Law school reminder**: Ryan Goodman and Erica Chenoweth silence at 72 hours is NOT a negative signal. Their response window extends through May 28. Remove them from the denominator mentally when assessing May 21 signals — the classification turns on the policy org contacts (Weiser, Bassin) and Elias.

---

## PART 6: Post-Decision Logging

After the 14:00 UTC user confirmation, log the following in CHECKIN.md under a new section "WAVE 1 CLASSIFICATION — May 21":

```
Classification: [STRONG / MODERATE / WEAK]
Classification time: [UTC]
Quality Reply Points at classification: [number]
Reply Rate (adjusted): [%]
Gist delta: [number]
Integration signals (Score 4-5): [count]
Path activated: [Section 4A / 4B / 4C]
Domain 42 state AG sends: [queued / sent / pending]
Phase 2 research start confirmed: [date and domain]
Law school window status: OPEN — extends through May 28
May 25 secondary gate: SCHEDULED
```

The May 25 secondary gate is where law school signals (Goodman, Chenoweth) are incorporated into a final confirmation of the classification. If either produces a Score 3+ reply between May 21 and May 25, upgrade the classification accordingly before finalizing Phase 2 research sequencing.

---

*Staged: May 18, 2026. Sources: WAVE_1_SYNTHESIS_FRAMEWORK.md (Item 61, May 18); WAVE_1_MONITORING_DASHBOARD.md (May 17); WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv (populated May 18); MAY_21_31_BATCH_2_3_COORDINATION_FRAMEWORK.md (May 18). Do not execute until May 21 10:30 UTC.*
