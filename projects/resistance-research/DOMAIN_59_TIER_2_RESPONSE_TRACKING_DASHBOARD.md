---
title: "Domain 59 — Tier 2 Response Tracking Dashboard (June 25–July 2)"
subtitle: "7-Day Real-Time Monitoring for Wave 2 Sends (EPI/Demos/NELP)"
created: "2026-06-25"
status: "PRODUCTION-READY"
user_executes: "Daily checkpoint — 5-10 minutes per day"
hard_deadline: "June 30, 2026 (OBBBA midterm framing window)"
---

# Domain 59 — Tier 2 Response Tracking Dashboard

**June 25–July 2, 2026**

Real-time monitoring template for Wave 2 sends (Economic Policy Institute, Demos, National Employment Law Project). Use this dashboard to track reply signals, engagement patterns, and daily activation decisions.

---

## Wave 2 Send Status

| Contact | Organization | Email Sent | Send Date | Send Time (UTC) | Confirmed Sent? |
|---------|--------------|-----------|-----------|-----------------|-----------------|
| Research director | Economic Policy Institute | researchdept@epi.org | June 24 | [ ] | [ ] |
| Policy team | Demos | info@demos.org | June 24 | [ ] | [ ] |
| Policy team | NELP | info@nelp.org | June 25–30 | [ ] | [ ] |

**Pre-fill after sending**:
- Check each email in your sent folder
- Record exact send time (UTC)
- Mark "Confirmed sent" once you verify delivery (watch for bounce-back within 2 hours)

---

## 7-Day Monitoring Tracker

**Baseline from Wave 1** (June 9–11 sends):
- CBPP: MODERATE reply June 17 ("Thank you for sharing. This is very relevant to our work." + forwarded to research team)
- MomsRising: MODERATE reply June 17 ("Acknowledged interest. Thank you for this framing.")
- AFL-CIO: No reply by June 24
- ITEP: No reply by June 24
- NWLC: No reply by June 24

---

## Daily Checkpoint Table (Fill in After Each Inbox Check)

| Date | Day | EPI Status | Demos Status | NELP Status | Daily Signal | Reply Rate | Sentiment | Escalation Notes |
|------|-----|-----------|--------------|-------------|--------------|------------|-----------|------------------|
| June 24 | 0 (send day) | Sent | Sent | — | — | — | — | Wave 2 A & B launched; 90-min spacing maintained |
| June 25 | 1 | [ ] Reply? | [ ] Reply? | [ ] Sent today | [ ] Strong [ ] Moderate [ ] Weak [ ] Bounce | [ ]% (0/3) | Pending | NELP send window active — proceed if no escalation signals |
| June 26 | 2 | [ ] Reply? | [ ] Reply? | [ ] Reply? | [ ] Strong [ ] Moderate [ ] Weak [ ] Bounce | [ ]% (0/3) | Pending | 48-hour window closing; any bounce signals trigger contingency check |
| June 27 | 3 | [ ] Reply? | [ ] Reply? | [ ] Reply? | [ ] Strong [ ] Moderate [ ] Weak [ ] Bounce | [ ]% (0/3) | Pending | **CHECKPOINT Q1**: Responses suggest proceeding with post-holiday follow-up? |
| June 28 | 4 | [ ] Reply? | [ ] Reply? | [ ] Reply? | [ ] Strong [ ] Moderate [ ] Weak [ ] Bounce | [ ]% (0/3) | Pending | Sentiment pattern emerging — assess tone consistency |
| June 29 | 5 | [ ] Reply? | [ ] Reply? | [ ] Reply? | [ ] Strong [ ] Moderate [ ] Weak [ ] Bounce | [ ]% (0/3) | Pending | 48 hours to OBBBA window closure; any Tier 3 activation signals? |
| June 30 | 6 | [ ] Reply? | [ ] Reply? | [ ] Reply? | [ ] Strong [ ] Moderate [ ] Weak [ ] Bounce | [ ]% (0/3) | Pending | **DEADLINE**: OBBBA midterm framing lock. Log final Wave 2 baseline. |
| July 1 | 7 | [ ] Reply? | [ ] Reply? | [ ] Reply? | [ ] Strong [ ] Moderate [ ] Weak [ ] Bounce | [ ]% (0/3) | Pending | T+7 checkpoint — execute Day 14 decision tree logic (TIER_2_ACTIVATION_DECISION_TREE.md) |

---

## Signal Definitions & Scoring

### Reply Signal Types (Classify Each Response)

| Signal | Definition | EPI Example | Demos Example | NELP Example | Score |
|--------|-----------|-------------|---------------|--------------|-------|
| **STRONG** | Named reply from decision-maker or policy staff; request to discuss or cite; offer to integrate into brief/testimony | Heidi Shierholz or named EPI researcher replies requesting call; offers to cite wage pathway in EPI brief | Taifa Smith Butler or Demos policy director replies with specific engagement request; mentions "equal say/equal chance" framing | Rebecca Dixon or NELP policy staff replies; requests discussion of worker classification + democratic participation frame; offers to share with state affiliates | +3 points each |
| **MODERATE** | General inbox acknowledgment; routing confirmation; request for full document; "thank you, forwarded to team" | Info@epi.org general response; "Thank you. Forwarding to research team." No specific follow-up. | Demos general team response; "We appreciate this framing. Currently evaluating uses." | NELP general acknowledgment; "Thank you for sharing. Will review." | +1 point each |
| **WEAK** | Auto-acknowledgment only; generic "out of office" or form response; no content engagement | Auto-responder; "We receive many submissions. Will review if relevant." | Auto-responder only | Auto-responder only | 0 points |
| **BOUNCE** | Hard bounce; invalid email; server rejection | Email returned "user unknown" | Email returned "recipient unavailable" | Email returned undeliverable | -2 points; triggers contingency |

---

## Daily Checkpoint Questions (Ask Yourself — 5-10 min per day)

Use these questions to guide your daily decision-making. Write brief answers in the "Daily Checkpoint Notes" section below.

### June 25 (Day 1)
**Q1: Did EPI or Demos send confirm delivery? Any bounces?**
- If ANY bounce: → Execute CONTINGENCY_ROUTING_IF_SEND_FAILS.md immediately (verify contact email, resend within 48 hours)
- If both confirmed: → Mark checkpoint complete, proceed to June 26

**Q2: Is NELP email address info@nelp.org still current?**
- If yes: Send NELP on schedule (June 25 preferred, June 30 hard cutoff)
- If no: Update from nelp.org/contact before sending

---

### June 26 (Day 2)
**Q1: Any replies yet from EPI, Demos, or NELP?**
- If STRONG from any contact: → Move to Q2 (Tier 2 activation pathway)
- If MODERATE or WEAK: → Continue monitoring; no immediate action
- If BOUNCE: → Execute contingency check (CONTINGENCY_ROUTING_IF_SEND_FAILS.md)

**Q2: Do any STRONG replies suggest Tier 3 activation is credible?**
- Example: EPI researcher says "This is directly relevant to our June Senate Finance testimony" → STRONG signal = 40%+ confidence in Tier 3 readiness
- Log specific quote indicating Tier 3 pathway

---

### June 27 (Day 3)
**Q1: What's the combined reply rate? (EPI + Demos + NELP that have been sent)**
- Calculate: (# of replies received) / (# of orgs that have received send) = reply rate %
- **Scoring**: ≥40% = Strong pathway; 20-40% = Investigate pathway; <20% = Weak/contingency pathway
- Document rate in "Daily Reply Rate" column above

**Q2: Any pattern in sentiment across replies?**
- Example: All replies emphasize "democratic participation" language → High confidence in framing reception
- Example: Replies are polite but generic → Moderate confidence; may need follow-up
- Example: Any skeptical language ("but this oversimplifies...") → Weak confidence; investigate
- Log sentiment pattern in "Sentiment" column

---

### June 28 (Day 4)
**Q1: Have you received any meeting/call requests?**
- If YES from any contact: This is a STRONG signal. Schedule immediately (within 24-48 hours). Offer 15-min discussion of "how democratic participation framing complements your existing advocacy."
- If NO: Continue monitoring through June 30

**Q2: Should we proceed with any post-Wave-2 follow-up sends?**
- Example: If EPI replies positively but Demos bounces, do you resend to Demos or wait?
- Decision: Wait until June 30 checkpoint. Only resend if bounce was confirmed in contingency check (see CONTINGENCY_ROUTING_IF_SEND_FAILS.md)

---

### June 29 (Day 5)
**Q1: Do responses suggest stronger messaging angle for any recipient type?**
- Example: NELP replies mention "gig worker scheduling" repeatedly → possible messaging strength for Tier 3 gig-adjacent orgs
- Example: Demos replies emphasize "midterm electoral implications" → messaging strength for electoral-focused Tier 3
- Log any new messaging angles suggested by replies

**Q2: Is OBBBA still active in news/legislative environment?**
- Check: Senate Finance Committee activity June 29-30. Any markup happening?
- If YES: Messaging angle is still relevant → proceed with normal follow-up
- If NO: OBBBA window closing → prioritize consolidating existing replies before June 30 hard deadline

---

### June 30 (Day 6 — HARD DEADLINE)
**Q1: Final Wave 2 baseline. What's the complete signal count?**
- Count STRONG signals: ____ (multiply by 3 points each)
- Count MODERATE signals: ____ (multiply by 1 point each)
- Count WEAK signals: ____ (0 points)
- Count BOUNCES: ____ (multiply by -2 points each)
- **Total Score**: ____ points

**Q2: Proceed to TIER_2_ACTIVATION_DECISION_TREE.md — what's your pathway?**
- Strong (≥6 points): Activate Tier 3 before July 7
- Investigate (3-5 points): Escalate for user review; prepare alternative messaging for July follow-up
- Weak (<3 points): Trigger CONTINGENCY_ROUTING_IF_SEND_FAILS.md assessment
- Log final recommendation

---

### July 1 (Day 7 — T+7 CHECKPOINT)
**Execute Decision Tree**:
- Open `TIER_2_ACTIVATION_DECISION_TREE.md`
- Follow the Strong/Investigate/Weak pathway logic
- Record final decision on whether to activate Tier 3 or pivot strategy

---

## Daily Checkpoint Notes (Fill In Daily)

### June 25 (Day 1)
- EPI send confirmed: [ ]
- Demos send confirmed: [ ]
- NELP action: [ ] Not yet sent [ ] Send today [ ] Send tomorrow (June 26)
- Notes: _______________________________________________________________

### June 26 (Day 2)
- New replies today: [ ] EPI [ ] Demos [ ] NELP — count: ____
- Bounces: [ ] None [ ] EPI [ ] Demos — action: ___________
- Notes: _______________________________________________________________

### June 27 (Day 3)
- Reply rate %: ____ (# replies / # sends completed)
- Sentiment pattern: [ ] Positive [ ] Neutral [ ] Mixed [ ] Skeptical
- Notes: _______________________________________________________________

### June 28 (Day 4)
- Meeting/call requests: [ ] Yes [ ] No — if yes, scheduled for: ___________
- Follow-up sends needed?: [ ] No [ ] Yes — target: _____________________
- Notes: _______________________________________________________________

### June 29 (Day 5)
- New messaging angles emerging?: [ ] No [ ] Yes — describe: _____________
- OBBBA legislative status: [ ] Still active [ ] Winding down — source: ____
- Notes: _______________________________________________________________

### June 30 (Day 6)
- Final Wave 2 signal score: ____ points (STRONG: +3, MODERATE: +1, WEAK: 0, BOUNCE: -2)
- Pathway recommendation (from Decision Tree): [ ] Strong [ ] Investigate [ ] Weak
- Tier 3 activation ready?: [ ] Yes [ ] No — confidence: ____%
- Notes: _______________________________________________________________

### July 1 (Day 7)
- Decision Tree pathway executed: [ ]
- Final outcome: [ ] Activate Tier 3 [ ] Hold for follow-up [ ] Pivot strategy
- Next steps: _______________________________________________________________

---

## Quick Reference: What Each Signal Means

| If You See This | You Should Do This | Rationale |
|---|---|---|
| STRONG reply (≥1 from any contact) | Respond within 24 hours. Offer 15-min call or 1-page summary. | This is the highest-value engagement. Time-sensitive. |
| 2+ MODERATE replies | Continue monitoring. No action needed yet. Prepare for potential follow-up June 30. | Indicates organizational awareness. Waiting for them to act is appropriate. |
| All WEAK or no replies by June 26 | Check CONTINGENCY_ROUTING_IF_SEND_FAILS.md. Verify email addresses. Assess whether content angle needs adjustment. | Bounce or no-reply patterns require diagnosis before follow-up. |
| Any BOUNCE | Execute contingency check immediately. Resend to verified address within 48 hours. | Bounces create a 48-hour recovery window. Don't miss it. |
| STRONG + meeting request | Schedule call for June 28-July 2. Prepare: (1) 1-minute elevator pitch on how framing complements their work, (2) list of 2-3 follow-up questions about their advocacy priorities. | Meeting is Tier 2 → Tier 3 activation pathway. Preparation is critical. |

---

## Gist View Tracking (Optional — Low Priority)

GitHub Gist view count provides indirect signal of organizational engagement. Check daily if you want; not required for decision-making.

| Date | Gist Views (Cumulative) | New Views 24h | Notes |
|------|------------------------|--------------|-------|
| June 24 | _____ | — | Baseline at Wave 2 send |
| June 25 | _____ | _____ | |
| June 26 | _____ | _____ | 48h post-send window |
| June 27 | _____ | _____ | |
| June 28 | _____ | _____ | |
| June 29 | _____ | _____ | |
| June 30 | _____ | _____ | Final baseline |
| July 1 | _____ | _____ | T+7 checkpoint |

**Interpretation guide**:
- ≥50 new views 48-72h post-send = Probable organizational review
- 10-50 new views = Some engagement
- <10 new views = Limited external engagement (not necessarily negative — orgs may read without logging in)

---

## Cross-References

- **Wave 2 Send Execution**: DOMAIN_59_TIER2_SEND_TEMPLATES.md (templates + timing + contingency contact info)
- **Bounce Recovery**: CONTINGENCY_ROUTING_IF_SEND_FAILS.md (email verification, retry logic, alternative channels)
- **Activation Decision Logic**: TIER_2_ACTIVATION_DECISION_TREE.md (Strong/Investigate/Weak decision matrix + Tier 3 next steps)
- **Wave 1 Baseline Reference**: DOMAIN_59_DISTRIBUTION_EXECUTION_LOG.md (Wave 1 2 MODERATE responses June 17 baseline)
- **Full Contact Info**: DOMAIN_59_CONTACT_REACHABILITY_SNAPSHOT.md (verified addresses + org alt contacts as of June 10)

---

## Print This & Use It

**Format for user**: Print this dashboard or open as reference during daily inbox checks. Fill in "Daily Checkpoint Notes" each day (5-10 min). Refer to checkpoint questions before making follow-up decisions. Move to Decision Tree on July 1.

**Success criteria**: Every day logged. No missed checkpoints June 25-July 1. All signals classified. Bounce/contingency alerts triggered within 24 hours of detection.

---

*Created June 25, 2026. Production-ready. User executes daily June 25–July 2. Wave 2 sends (EPI/Demos/NELP) launched June 24-25. OBBBA hard deadline June 30.*
