---
title: "Wave 2 Outcome Decision Tree"
created: "2026-06-28"
status: "production-ready"
trigger: "Domain 51/48 Wave 1 sends (June 23-24) + Domain 59 Tier 2 sends (June 25-30)"
execution_time: "<30 minutes to activate any branch"
cross_references:
  - domain-specific-escalation-procedures.md
  - retroactive-scotus-protocol.md
  - PHASE_2_CONTINGENCY_DECISION_TREE.md
  - DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md
  - DOMAIN_48_CONTACT_LIST_AND_STRATIFICATION.md
  - domain-59-send-templates.md
---

# Wave 2 Outcome Decision Tree
## Response-Rate Scenarios and Activation Thresholds

**Prepared**: June 28, 2026 (Item 18 — Exploration Queue)
**Trigger event**: Domain 51/48 Wave 1 sends (June 23-24) + Domain 59 Tier 2 sends (EPI/Demos/NELP, June 25-30)
**Measurement window**: Day 3 post-send (first check), Day 7 (branch confirmation)
**User execution time**: <30 minutes to activate any branch — all actions pre-staged

---

## How to Use This Tree

1. On Day 3 after your sends (3 days after last send in each domain), count replies.
2. Use the threshold table below to identify your signal level.
3. Execute the branch instructions — all contacts, templates, and timing already staged.
4. On Day 7, re-check. If signal has improved, hold current path. If signal has deteriorated, follow the escalation note.

**This tree covers three domains independently.** Each domain has its own signal level. You may be LOW on Domain 59 and MODERATE on Domain 51 simultaneously — apply the correct branch per domain.

---

## Signal Classification

### Definition of a "Reply" (for counting purposes)

A reply counts toward your threshold if it is:
- Named reply from an identifiable staff person (not auto-responder or OOO)
- Substantive content — even a sentence ("I forwarded this to our policy team") counts
- Request for conversation, call, or additional materials
- Offer to circulate, cite, or use the research

Auto-acknowledgments, form responses, and out-of-office messages do NOT count.

### Thresholds (apply per domain, per Day 3 count)

| Signal Level | Day 3 Reply Count | Day 7 Reply Count | Interpretation |
|---|---|---|---|
| **HIGH** | 4+ replies | 5+ replies | Momentum — accelerate Tier 2 |
| **MODERATE** | 2-3 replies | 3-4 replies | On track — continue original timeline |
| **LOW** | 1 reply | 1-2 replies | Weak signal — contingency review |
| **ZERO** | 0 replies | 0 replies | No signal — activate escalation immediately |

**Note on Day 3 vs. Day 7**: Day 3 is an early read. Do NOT make major routing decisions based on Day 3 alone if you are in LOW territory — wait for Day 7 confirmation. Exception: ZERO on Day 3 triggers immediate contingency (see Branch Z below).

---

## Pre-Check Worksheet (5 minutes, Day 3)

Fill this in before entering the tree:

```
DOMAIN 59 — Tier 1 Wave (CBPP, ITEP, NWLC, MomsRising, AFL-CIO — sent June 2-3):
  - Any substantive replies received since sends?  [ ] YES  [ ] NO
  - Count of qualifying replies (Day 3):  _____ / 5

DOMAIN 59 — Tier 2 Wave (EPI, Demos, NELP — scheduled June 25-30):
  - Sends completed? (EPI: _____, Demos: _____, NELP: _____)
  - Count of qualifying replies (Day 3 from last send):  _____ / 3
  - COMBINED Domain 59 Tier 1 + Tier 2 qualifying replies:  _____ / 8

DOMAIN 51 (CLC, Issue One — Wave 1; Common Cause CA, LWV CA, Clean Money — Wave 2):
  - Count of qualifying replies (Day 3):  _____ / 5

DOMAIN 48 (Sentencing Project, PPI, Brennan, Worth Rises — Wave 1):
  - Count of qualifying replies (Day 3):  _____ / 4

AGGREGATE:
  Total contacts across all domains (Tier 1 + Tier 2):  _____
  Total qualifying replies Day 3:  _____
  Domains at HIGH (4+):  _____ of 3
  Domains at MODERATE (2-3):  _____ of 3
  Domains at LOW/ZERO (0-1):  _____ of 3
```

---

## Branch A — LOW SIGNAL (0-1 replies by Day 3 in any domain)

**Threshold**: 0 or 1 qualifying reply by Day 3 from Wave 1 sends in a given domain.

**This branch applies per-domain.** If Domain 59 is LOW but Domain 51 is MODERATE, apply Branch A only to Domain 59.

### Option A-1: Retry Tier 1 with Modified Template (Timing: Day 5-7)

Use when: 0-1 replies, the send went to the correct address, and no bounce received.

Rationale: Low reply rates are often timing-driven, not interest-driven. DC policy staff have highly variable inbox attention — Thursday afternoon sends get buried; Monday morning sends compete with Hill schedule. A re-send with modified angle hits a different attention cycle.

**Modification requirements** (change at least two of these):
- Subject line: reframe from research-sharing to "time-sensitive" or deadline-specific hook
- Opening paragraph: lead with the most urgent current event (e.g., for Domain 59: the Senate Finance markup deadline June 30; for Domain 51: the CA Fair Elections Act July 1 deadline)
- Send time: if original was Tuesday-Wednesday, retry Thursday 09:00-11:00 UTC
- Angle: shift from "research I want to share" to "I noticed your recent [tweet/testimony/statement] on X — this analysis directly supports that position"

**Template modification instructions for each domain**: See domain-specific-escalation-procedures.md, Section per domain.

**Do not re-send to the same address on the same day.** Minimum 48-hour gap between sends to the same contact.

### Option A-2: Skip Tier 2, Accelerate Domain 57 (Timing: Day 7, if LOW persists)

Use when: LOW persists at Day 7, Domain 57 infrastructure is ready (Gist + templates staged), and the August 10 deadline is the higher-leverage window.

Rationale: If engagement signal is persistently low across Wave 2 sends, the strategic question is whether to continue pushing into low-signal territory or to redirect attention to Domain 57 where the August 10 news cycle (multilateral withdrawal, summer foreign policy window) offers a distinct leverage window. Domain 57 has its own contact list (CFR, Brookings Foreign Policy, Carnegie Endowment) that does not overlap with Domains 51/48/59 — redirecting to Domain 57 does not sacrifice the existing relationships.

**Activation steps**:
1. Verify Domain 57 Gist URL is live and loading (check DOMAIN_57 or the relevant staging file)
2. Confirm 5+ Domain 57 contacts staged with templates
3. Begin Domain 57 sends: target July 7-10 window (4 weeks before August 10 deadline)
4. Leave Domain 59 Tier 2 on monitoring hold — do not abandon, but do not force additional sends

### Option A-3: Activate Domain 59 Tier 2 Immediately — EPI/Demos/NELP (Timing: Day 5, if LOW)

Use when: Domain 59 Tier 1 shows LOW (0-1 replies by Day 3) and Domain 59 Tier 2 sends are not yet complete.

Rationale: If Tier 1 (CBPP, ITEP, NWLC, MomsRising, AFL-CIO) shows low engagement, the Tier 2 organizations (EPI, Demos, NELP) represent a distinct contact network with different institutional alignments — EPI's labor-economics framing reaches audiences that economic-justice framing at CBPP may not. Activating Tier 2 faster (Day 5 instead of the scheduled June 25-30 spacing) compresses the timeline to catch the June 30 markup window.

**Activation decision rule**:

```
IF Domain 59 Tier 1 Day 3 replies = 0:
   → Activate Tier 2 (EPI/Demos/NELP) on Day 5
   → Compress spacing to 12h between sends (EPI → Demos → NELP on successive mornings)
   → Do not wait for Day 7 confirmation

IF Domain 59 Tier 1 Day 3 replies = 1:
   → Wait for Day 7 confirmation before activating Tier 2 early
   → If Day 7 still LOW (1-2 replies): activate Tier 2 accelerated

IF Domain 59 Tier 1 Day 3 replies = 2+:
   → This is MODERATE territory — do not use A-3, continue original Tier 2 schedule
```

**When LOW persists through Day 7 (1-2 replies): Use Option A-3 (Tier 2 activation) as the primary path.** Option A-1 and A-2 are secondary fallbacks. If LOW persists and you activate A-3, run A-3 first (Tier 2 sends) and reassess on Day 10 before deciding on A-2 (Domain 57 redirect).

---

## Branch B — MODERATE SIGNAL (2-3 replies by Day 3)

**Threshold**: 2-3 qualifying replies by Day 3 from Wave 1 sends.

**This is the expected baseline signal.** No structural changes required.

### B-1: Continue Tier 2 on Original Timeline

**Domain 59 Tier 2 (EPI/Demos/NELP)**: Send on the June 25-30 scheduled spacing (EPI first, then Demos 24h later, then NELP 24h after Demos). 24h spacing prevents mailbox fatigue across organizations in adjacent policy networks.

**Domain 51 Tier 2**: No pre-staged Tier 2 needed unless reply rate falls below 1 response from 5 contacts by Day 7. If that happens, apply the CA Fair Elections Act fallback from domain-specific-escalation-procedures.md (Section 2).

**Domain 48 Tier 2**: No pre-staged Tier 2 until Day 10. NAACP LDF and Fines and Fees Justice Center remain on contingency hold (activate only on strong signal OR if Tier 1 drops to 0-1 by Day 10).

### B-2: Prepare Domain 59 Final Send Sequence

By Day 5, confirm the following are ready for the final Domain 59 push (Senate Finance window closes June 30):

```
[ ] EPI send completed or scheduled
[ ] Demos send completed or scheduled
[ ] NELP send completed or scheduled
[ ] Any Day 1-3 replies logged in DISTRIBUTION_EXECUTION_LOG.md
[ ] Senate Finance markup date confirmed (June 30 or updated if rescheduled)
[ ] Follow-up emails drafted for any contacts who did not reply within 7 days
```

### B-3: Monitor for Escalation to HIGH

If reply count moves from 2-3 to 4+ between Day 3 and Day 7, transition to Branch C (HIGH SIGNAL) without waiting for the next formal check.

---

## Branch C — HIGH SIGNAL (4+ replies by Day 3)

**Threshold**: 4 or more qualifying replies by Day 3 across Wave 1 sends in any domain.

This is a positive outlier result. The response rate in typical advocacy research distribution is 15-25%; 4+ replies by Day 3 indicates active interest from multiple organizations, not just courtesy acknowledgment.

### C-1: Accelerate Tier 2 Timeline

**Domain 59**: Combine EPI and Demos into a single send window — send both on the same day (June 26 if sends have not yet happened, or the next available morning after HIGH signal is confirmed). 12h spacing (EPI morning, Demos afternoon). NELP follows 24h after Demos.

Rationale: HIGH signal indicates organizations in this policy network are actively processing the research. Momentum has a decay curve — sending Tier 2 faster catches organizations while interest is live.

**Domain 51**: If CA Fair Elections Act contacts are not yet reached, activate immediately. Do not wait for the July 1 deadline to approach.

**Domain 48**: Activate NAACP LDF send from contingency hold. Use NAACP LDF Template from DOMAIN_48_CONTACT_LIST_AND_STRATIFICATION.md Tier B contacts.

### C-2: Prepare Phase 3 Early Activation Signal

HIGH signal at Wave 2 is the strongest input available for Phase 3 readiness assessment. Document it:

```
[ ] Log HIGH signal confirmation in DISTRIBUTION_EXECUTION_LOG.md
[ ] Note which organizations replied and with what level of engagement
[ ] Flag for Phase 3 consideration: if 2+ organizations request additional research or
    indicate interest in November-January distribution, tag as "Phase 3 coalition candidate"
[ ] Do NOT initiate Phase 3 work until November 4 — but preserve the relationship signals
    for the Phase 3 execution runbook
```

### C-3: Consider Early Phase 3 Signal Activation (Conditional)

This step requires user judgment. Apply only if ALL of the following are true:

1. HIGH signal confirmed in 2 or more domains simultaneously (not just one domain)
2. At least one organization has explicitly requested additional research or offered to include the research in testimony
3. Phase 3 November 4 deadline is not at risk from premature distribution

If all three are true: notify the user immediately (log in CHECKIN.md under "Needs Your Input") and describe the opportunity. Do not activate Phase 3 autonomously.

---

## Branch Z — ZERO SIGNAL (0 replies by Day 3, confirmed by Day 5)

**Threshold**: Exactly zero qualifying replies by Day 3, confirmed again at Day 5.

This is the emergency path. Zero responses from multiple organizations in multiple domains is not normal noise — it suggests either (a) delivery failure (emails going to spam, wrong addresses), (b) timing failure (all sends hit a dead week like July 4th adjacency), or (c) framing failure (the subject line is not generating opens).

### Z-1: Diagnose Before Escalating

**Day 5 triage** (10 minutes):

```
Delivery check:
[ ] Any bounce notices in sent folder?  YES → update addresses, re-send
[ ] Any out-of-office / auto-acknowledgments?  YES → confirms delivery, signals absence not disinterest
[ ] Gist URL loading correctly?  Check the Gist URL from a new browser tab

Timing check:
[ ] When were sends made? If June 23-24 → were those Monday-Tuesday around a holiday?
[ ] If June 25-30 → were those during a summer slow period for DC organizations?

Framing check:
[ ] Review subject lines against current news cycle — is the hook stale?
[ ] Is there a more urgent recent event that would be a stronger hook?
```

### Z-2: Escalate to Tier 2 Immediately (if delivery confirmed)

If delivery is confirmed (no bounces, some OOO received) and Day 5 still shows zero substantive replies:

1. Activate Domain 59 Tier 2 (EPI/Demos/NELP) immediately — use compressed 12h spacing
2. Activate Domain 51 CA Fair Elections fallback (Democracy Forward + CREW + Sunlight Foundation) — see domain-specific-escalation-procedures.md, Section 2
3. Activate Domain 48 Tier 2 (Sentencing Reform + Voting Rights Nexus path) — see domain-specific-escalation-procedures.md, Section 3

### Z-3: Pivot to Alternative Amplification Channels

If ZERO persists through Day 7 across all Tier 1 and early Tier 2 sends:

1. Check ALTERNATIVE_AMPLIFICATION_CHANNELS.md for non-email distribution paths
2. Consider posting the Gist URL to relevant policy listservs (law professor listservs, election law community, labor economics networks)
3. Consider whether a Twitter/X thread summarizing the key finding would drive Gist traffic and inbound organizational interest

---

## Day 7 Confirmation Checkpoint

On Day 7 after sends, re-run the Pre-Check Worksheet above. Apply these confirmation rules:

| Day 3 Signal | Day 7 Signal | Action |
|---|---|---|
| LOW | Still LOW (1-2) | Confirm Branch A-3 (Tier 2 fast-activate) if not already done |
| LOW | Moved to MODERATE | Shift to Branch B; hold Tier 2 on original schedule |
| LOW | Moved to HIGH | Shift to Branch C; accelerate Tier 2; activate Phase 3 monitoring |
| ZERO | Still ZERO | Confirm Branch Z; escalate to alternative channels |
| MODERATE | Held MODERATE | Confirm Branch B; continue original Tier 2 schedule |
| MODERATE | Moved to HIGH | Shift to Branch C |
| HIGH | Confirmed HIGH | Confirm Branch C; compress Tier 2; document Phase 3 signal |

---

## Cross-Domain Notes

**Domain 59 governs the June 30 markup deadline.** All Domain 59 sends (Tier 1 + Tier 2) must complete before June 28 to allow time for engagement before the markup window closes. If any Domain 59 sends are not yet complete as of June 28, prioritize them above all other Wave 2 actions.

**Domain 51 July 1 deadline is hard.** The CA Fair Elections Act coalition window is July 1. If CA Fair Elections contacts have not received Domain 51 materials by June 28, send them now regardless of which branch the overall signal puts you in.

**Domains are independent routing decisions.** Do not let LOW signal in one domain prevent HIGH signal activation in another. Apply each branch to its domain independently.

---

*Prepared June 28, 2026. All branches pre-staged — no re-analysis required at activation. Execution time: <30 minutes per branch.*
