---
title: "Day 7 Checkpoint Routing Decision Tree"
subtitle: "June 17-18, 2026 — STRONG / MODERATE / WEAK Branch Dispatch"
created: "2026-06-14"
status: "production-ready — execute at 17:00 UTC June 17, 2026"
execution_time: "<30 minutes (data entry + routing decision + next-action dispatch)"
data_in: "POST_WAVE_2_ENGAGEMENT_ANALYSIS_TEMPLATE.md Section 8 (completed at checkpoint)"
domains: [51, 59]
hard_deadlines:
  domain_59: "June 25-30, 2026 (Senate Finance CTC markup)"
  domain_51: "July 1, 2026 (California Fair Elections Act messaging window)"
companion_docs:
  - "POST_WAVE_2_ENGAGEMENT_ANALYSIS_TEMPLATE.md (data collection feeds this tree)"
  - "DOMAIN_51_RAPID_ACTIVATION_RUNBOOK.md (STRONG and MODERATE branch execution)"
  - "DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md (STRONG and MODERATE branch execution)"
  - "DOMAINS_51_59_SEQUENTIAL_ACTIVATION_TIMING.md (2-day stagger plan)"
  - "PHASE_2_RESOURCE_ALLOCATION_CONTINGENCY_MATRIX.md (capacity planning per branch)"
note: >
  This decision tree does NOT require pre-existing Wave 1-2 data. It is completed at
  the Day 7 checkpoint when data arrives from POST_WAVE_2_ENGAGEMENT_ANALYSIS_TEMPLATE.md.
  Execution time is <30 minutes because all next-action content is pre-staged.
---

# Day 7 Checkpoint Routing Decision Tree

**Version 1.0 — June 14, 2026**

**Lead finding**: The Day 7 checkpoint produces a binary-plus outcome: STRONG, MODERATE, or WEAK engagement. Each branch routes to a specific pre-staged execution package with no ambiguity. The decision tree takes <30 minutes because the analysis template (Section 8 of POST_WAVE_2_ENGAGEMENT_ANALYSIS_TEMPLATE.md) has already done the aggregation work. This document is the dispatch tool, not the analysis tool.

**Critical rule**: Domain 59 (Economic Precarity / CTC) proceeds on the Domain 59 express Senate path even in the WEAK engagement branch, because the Senate Finance markup is an immovable external deadline. The engagement signal governs Phase 2 expansion scope — it does not override legislative window urgency.

---

## Step 1: Pre-Flight Checks (5 minutes)

*Complete before entering the decision tree. These checks determine whether the tree runs on clean data or requires a diagnostic branch first.*

### 1.1 Infrastructure Verification

| Check | URL / Source | Status | Action if Failed |
|-------|---|---|---|
| Domain 59 Gist live | https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba | [ ] HTTP 200 / [ ] 404 | Recreate from domain-59-economic-precarity-democratic-infrastructure.md (10 min). Do BEFORE any sends. |
| Domain 51 Gist live | https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372 | [ ] HTTP 200 / [ ] 404 | Recreate from domain-51-campaign-finance-dark-money.md (10 min). Do BEFORE any sends. |
| Senate Finance markup status | https://www.finance.senate.gov/hearings | [ ] ACTIVE / [ ] PASSED / [ ] STALLED | See Section 2.1 for passed/stalled handling. |
| California ballot status | https://ballotpedia.org/California_Public_Funding_of_Elections_Measure_(2026) | [ ] ON BALLOT / [ ] REMOVED | See Section 2.2 for removed handling. |
| Montana I-194 status | ballotpedia.org (I-194 entry) | [ ] QUALIFIED / [ ] FAILED / [ ] PENDING | Affects Domain 51 state sends only. |

### 1.2 Send Confirmation Counts (from POST_WAVE_2_ENGAGEMENT_ANALYSIS_TEMPLATE.md)

Transfer these values from Section 8 of the analysis template:

- Total sends confirmed delivered: _____
- Total hard bounces: _____
- Total Score 3+ replies received: _____
- Any Score 4-5 reply: [ ] YES / [ ] NO
- Gist view delta (any positive): [ ] YES / [ ] NO
- Delivery rate: _____%

**Trigger: if delivery rate is below 80%** (more than 2 bounces from 10 sends): run POST_WAVE_2_ENGAGEMENT_ANALYSIS_TEMPLATE.md Section 7.1 Delivery Diagnostic before proceeding. Do not enter the routing branches until delivery is confirmed. Estimated diagnostic time: 5 minutes.

---

## Step 2: Determine Engagement Branch

*Apply exactly one of the three threshold tests. Use the first threshold that matches.*

### Branch Determination Table

| Test | Threshold | Branch Assigned |
|------|---|---|
| Score 3+ reply count ≥ 3 AND delivery rate ≥ 90% | 3 or more replies from any combination of D51/D59 contacts | **STRONG** |
| Score 3+ reply count = 1 OR 2, OR Score 4-5 reply received (even if only 1), OR delivery rate 80-89% with any reply | 1-2 substantive replies, or any single high-value reply | **MODERATE** |
| Score 3+ reply count = 0 AND no Score 4-5 reply AND delivery rate ≥ 80% | Zero substantive replies, delivery confirmed | **WEAK** |
| Score 3+ reply count = 0 AND delivery rate < 80% | Delivery failure with zero replies | **DIAGNOSTIC** (see Step 3, DIAGNOSTIC branch) |

**My engagement branch at Day 7 checkpoint**: [ ] STRONG / [ ] MODERATE / [ ] WEAK / [ ] DIAGNOSTIC

---

## Step 3A: STRONG Branch

*Condition: 3+ Score 3+ replies across both domains, and delivery rate ≥ 90%.*
*Estimated time to execute this branch: 15-20 minutes.*

### STRONG Branch: What This Means

Three or more substantive replies from 10 outreach contacts (30%+ substantive reply rate) in 7 days is above the upper bound for cold advocacy email engagement in this organizational sector. Per PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Section 4, Phase 1's "strong" Day 30 threshold for most constituencies was 25-50% — achieving this in 7 days across a cold Phase 2 send represents leading-indicator overperformance.

This branch does not slow down. It activates both domains immediately at full scope.

### STRONG Branch: Decision Checklist

- [ ] **Domain 59 express Senate path executes TODAY** (Day 0 of the stagger, per DOMAINS_51_59_SEQUENTIAL_ACTIVATION_TIMING.md Section 2)
  - AFL-CIO: feedback@aflcio.org (T+0)
  - CBPP: cbpp@cbpp.org (T+45 min)
  - NWLC: info@nwlc.org (T+90 min)
  - Templates: DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md Part 1
  - Log in: domain-59-send-log-june1.md
  - Time required: 45 minutes active

- [ ] **Domain 59 full 10-14h research sprint activates** (Days 1-4)
  - Zone structure: DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md Parts 3-6
  - Day 1 focus: Zone 1 (causal evidence) + Zone 2 (OBBBA provisions)
  - Deliverable: Senate staff briefing supplement (400 words, OBBBA provision-to-pathway mapping)

- [ ] **Domain 51 Tier 1 expansion executes Day 1** (June 18-19)
  - OpenSecrets: info@opensecrets.org (Email 3A, DOMAIN_51_RAPID_ACTIVATION.md)
  - Democracy 21: fwertheimer@democracy21.org (Email 3B)
  - Public Citizen: cholman@citizen.org (Email 3C)
  - Log in: DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md
  - Time required: 30 minutes active

- [ ] **Domain 51 full 10-14h research sprint activates** (Days 1-4, parallel with D59)
  - Zone structure: DOMAIN_51_RAPID_ACTIVATION_RUNBOOK.md Zones 1-5
  - Day 1 focus: Zone 2 (Crypto/AI PAC architecture)
  - Deliverable: Zone 1 addendum flagged to Brendan Fischer (CLC) and Erin Chlopak

- [ ] **Cross-domain integration note drafted** (Day 2)
  - Target: CBPP (after D59 reply), or AFL-CIO (after D59 engagement)
  - Content: FEC enforcement collapse (D51) + 42-point voter participation gap (D59) synthesis
  - Template: DOMAINS_51_59_SEQUENTIAL_ACTIVATION_TIMING.md Section 4.1
  - Send only AFTER at least one target has engaged with their primary domain

### STRONG Branch: Resource Requirement

| Activity | Time Required | When |
|---|---|---|
| D59 express path | 45 min active | Day 0 (today) |
| D51 Tier 1 expansion | 30 min active | Day 1 |
| D59 research sprint | 10-14h (4-5 days) | Days 1-5 |
| D51 research sprint | 10-14h (4-5 days) | Days 1-5, parallel |
| Monitoring + logging | 30 min/day | Daily |
| Cross-domain synthesis note | 20 min | Day 2 |

**Full STRONG branch activation requires approximately 22-30 researcher-hours over 5 days.** Per PHASE_2_RESOURCE_ALLOCATION_CONTINGENCY_MATRIX.md Row 1 (STRONG + adequate capacity), this is the default plan when capacity allows.

### STRONG Branch: Timeline Adjustments

No calendar adjustments needed. The STRONG branch runs on the pre-planned stagger schedule from DOMAINS_51_59_SEQUENTIAL_ACTIVATION_TIMING.md Section 2. Both domains execute within their external deadline windows:
- Domain 59 Senate Finance window (June 25-30): Express path executes June 17 — 8 days of runway.
- Domain 51 California window (July 1): Tier 1 expansion executes June 18-19 — 12 days of runway.

### STRONG Branch: Messaging Pattern Notes

A 30%+ reply rate in 7 days is a messaging alignment signal. Record which template subject line and opening paragraph generated the most replies. Apply these as the model for Tier 2 sends. Do not modify templates that are generating replies — message stability matters for a coherent organizational voice.

---

## Step 3B: MODERATE Branch

*Condition: 1-2 Score 3+ replies, OR any Score 4-5 reply, OR 80-89% delivery with at least 1 reply.*
*Estimated time to execute this branch: 12-18 minutes.*

### MODERATE Branch: What This Means

One or two substantive replies in 7 days is the expected outcome for a cold advocacy send of this size. It confirms that (a) at least some outreach is reaching engaged readers, (b) the messaging is not generating active rejection, and (c) the research content is finding a receptive audience in at least one organizational context.

The MODERATE branch faces a genuine resource constraint decision: Domain 59's Senate Finance window and Domain 51's California window both require activation within the next 10-14 days, but the engagement signal does not definitively confirm that both full 10-14h research sprints are warranted. The MODERATE branch provides a selective activation choice.

### MODERATE Branch: Decision Checkpoint — Which Domain to Prioritize?

**Apply this logic in order:**

1. Is the Senate Finance CTC markup still active (finance.senate.gov)?
   - [ ] YES → Domain 59 express path executes TODAY. Non-negotiable. This is an immovable external deadline. Proceed to Domain 59 checklist below.
   - [ ] NO (bill passed or stalled) → Domain 59 pivots to 2027 Reform Coalition frame. Domain 59 express path still executes, but with modified templates.

2. Which domain received the substantive reply?
   - [ ] Domain 59 received the reply → Domain 59 confirmed; run full assessment for Domain 51 scope.
   - [ ] Domain 51 received the reply → Both domains still activate at MODERATE scope. Domain 59 urgency (Senate Finance) overrides Domain 51's reply signal for sequencing.
   - [ ] Neither domain received a substantive reply but delivery is confirmed → MODERATE-LOW. Run Domain 59 express path (legislative urgency), Domain 51 Tier 1 sends to only the highest-priority contact (CLC or OpenSecrets). Defer state-level sends to Day 14.

### MODERATE Branch: Option A — Domain 59 Express + Domain 51 Tier 1 Only

*Use when capacity is constrained OR when replies came from only one domain. Covers both external deadlines with minimal time investment.*

- [ ] **Domain 59 express path TODAY** (45 minutes)
  - AFL-CIO: feedback@aflcio.org
  - CBPP: cbpp@cbpp.org
  - NWLC: info@nwlc.org
  - Templates: DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md Part 1
  - Skip full D59 research sprint for now — existing 44-citation research document is sufficient for express path

- [ ] **Domain 51 Tier 1 expansion (first 2 contacts only)** within 48 hours
  - OpenSecrets: info@opensecrets.org (highest reply probability, most domain-aligned)
  - Democracy 21: fwertheimer@democracy21.org (clean DISCLOSE Act direct argument)
  - Defer Public Citizen and state-level sends to Day 14 engagement signal assessment
  - Time required: 20 minutes active

- [ ] **No research sprints** in this option. Both domains distribute from existing research documents.
  - Total active time: 65 minutes over Days 0-1.

**Option A covers both external deadlines in under 90 minutes total.**

### MODERATE Branch: Option B — Domain 59 Express + Domain 51 Full Tier 1

*Use when capacity allows 10-12h over 4-5 days and replies came from at least one domain.*

- [ ] **Domain 59 express path TODAY** (45 minutes)
- [ ] **Domain 59 Zones 1-2 research sprint** Days 1-2 (4-5 hours) — generates Senate staff briefing supplement
- [ ] **Domain 51 full Tier 1 expansion** Days 1-2 (30 minutes active)
- [ ] **Domain 51 Zones 1-2 research sprint** Days 2-3 (4-5 hours)
- [ ] State-level sends (Domain 51) Day 4-5 per stagger timing
- Total: 10-12 hours over 4-5 days

*Option B is the standard MODERATE activation. It represents the middle path between STRONG (full 22-30h) and Option A (minimal 90 minutes).*

**Choose Option A or Option B**: [ ] A / [ ] B

### MODERATE Branch: Next-Action Checklist

Common to both options:

- [ ] Confirm Senate Finance markup status before sending any Domain 59 templates
- [ ] Log all sends in domain-59-send-log-june1.md immediately after each send
- [ ] Set Day 14 reminder: assess whether MODERATE branch should escalate to STRONG based on accumulated signal
- [ ] At Day 14: if 3+ total replies across both domains, re-run this tree at STRONG branch level for Tier 2 contacts

### MODERATE Branch: Timeline Adjustments

- Domain 59 Senate Finance window: Express path on Day 0 gives 8 days of runway. Adequate.
- Domain 51 California window: Tier 1 sends on Days 1-2 gives 12-13 days of runway. Adequate.
- Research sprints (if run): Compress to Zones 1-2 per domain if time is constrained. Zones 3-5 can defer to Day 14+ without losing either external deadline.

### MODERATE Branch: Messaging Pattern Notes

With 1-2 replies, identify the specific content element that generated the response. Was it:
- The Senate Finance markup urgency framing (Domain 59)?
- The FEC enforcement collapse data (Domain 51)?
- A specific statistic (42-point voter participation gap, 26 million children below CTC threshold)?

Apply the resonant framing element as the lead in Tier 2 sends, regardless of whether it came from a Domain 51 or Domain 59 template. Messaging synthesis across domains is valid when a single argument is generating the clearest signal.

---

## Step 3C: WEAK Branch

*Condition: Zero Score 3+ replies, no Score 4-5 reply, delivery rate ≥ 80%.*
*Estimated time to execute this branch: 20-25 minutes (includes diagnostic + contingency activation).*

### WEAK Branch: What This Means

Zero substantive replies at Day 7 with confirmed delivery is within the normal range for cold advocacy outreach. It is not a failure signal at Day 7. The median cold-contact reply cycle for organizational advocacy recipients is 7-14 days, not 0-7 days. The WEAK branch at Day 7 is "no signal yet" — not "Phase 2 has failed."

The WEAK branch has two parts: (1) a diagnostic investigation to confirm no structural problem exists, and (2) a deferred activation protocol that holds Tier 2 sends until Day 14 while still executing on the Domain 59 legislative urgency.

### WEAK Branch: Diagnostic Investigation (run first, 10 minutes)

| Check | Result | Action |
|-------|--------|--------|
| Delivery confirmation: are all sends shown as sent (not bounced) in outbox? | [ ] ALL CONFIRMED / [ ] SOME BOUNCED | If bounced: switch to backup email per contact snapshots. |
| Gist URL check: Domain 59 Gist view count has ANY positive delta since send? | [ ] YES (clicks occurred) / [ ] NO (zero delta) | YES: research is being read passively. This is not a failure — it is a leading indicator. NO: may be Gist URL not embedded, or email went to spam. |
| Gist URL check: Domain 51 Gist view count has ANY positive delta since send? | [ ] YES / [ ] NO | Same interpretation as above. |
| Spam folder check: Any auto-bounce notifications that landed in spam rather than inbox? | [ ] YES (found bounces) / [ ] NO (clean) | YES: rescue bounced sends using backup emails. |
| Subject line audit: Review sent emails — was the Gist URL embedded as a clickable hyperlink or as plain text? | [ ] HYPERLINK / [ ] PLAIN TEXT | PLAIN TEXT reduces click-through. Note for Tier 2 sends. |

**If any diagnostic check reveals a structural problem (bounces miscategorized, Gist URL not embedded, delivery issue)**: Fix the structural issue and re-run sends to affected contacts before proceeding. This is not a WEAK branch scenario — it is a delivery infrastructure correction.

**If all diagnostic checks pass**: Confirmed delivery + zero replies = passive reader scenario. Proceed to WEAK branch deferred activation.

---

### WEAK Branch: Deferred Phase 2 Activation

Domain 59 (legislative urgency) and Domain 51 (ballot campaign urgency) have different rules in the WEAK branch.

**Domain 59 — WEAK branch rule**: The Senate Finance markup is an immovable external deadline. The Domain 59 express Senate path STILL EXECUTES regardless of engagement signal, because the legislative advocacy value exists whether or not prior outreach has generated replies. A CBPP policy brief that reaches Senate Finance Committee staff is valuable independent of whether CBPP replied to our email.

- [ ] **Domain 59 express path executes TODAY, regardless of engagement branch**
  - AFL-CIO: feedback@aflcio.org (T+0)
  - CBPP: cbpp@cbpp.org (T+45 min)
  - NWLC: info@nwlc.org (T+90 min)
  - Framing check: Is Senate Finance markup still active? → USE TEMPLATES AS WRITTEN
  - Bill passed? → Switch to 2027 Reform Coalition frame (DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md Part 7)
  - Stalled? → "Failure proves the need for a sustained coalition" — stronger urgency frame
  - Time required: 45 minutes active

**Domain 51 — WEAK branch rule**: Defer Tier 1 expansion to Day 14. The California Fair Elections Act July 1 window is 13+ days away — there is time to wait for additional signal before committing to full Tier 1 expansion.

- [ ] **Domain 51 — hold Tier 1 expansion until Day 14**
  - Do not send to OpenSecrets, Democracy 21, or Public Citizen before Day 14.
  - Rationale: Unlike Domain 59, Domain 51 has no immovable deadline in the June 17-21 window. The July 1 California lock is recoverable if Tier 1 expansion sends begin on Day 14 (June 28) — 3 days of runway remain.
  - Exception: If Domain 51 Wave 1 contacts (CLC or Issue One) reply between Day 7 and Day 14, activate Tier 1 expansion immediately upon reply receipt.

### WEAK Branch: Timeline Adjustments

| Activity | STRONG/MODERATE Schedule | WEAK Branch Adjustment |
|---|---|---|
| D59 express path | Day 0 (June 17) | Day 0 (June 17) — NO CHANGE. Legislative window overrides. |
| D51 Tier 1 expansion | Day 1 (June 18) | Day 14 (June 28). Still before July 1 CA window. |
| D59 research sprint | Days 1-4 | Defer full sprint; proceed with express path only. Day 14: assess whether to begin sprint. |
| D51 research sprint | Days 1-4 | Defer entirely. Day 14: assess based on accumulated signal. |
| Day 14 re-assessment | N/A | REQUIRED. Run WEAK branch re-check using 14-day accumulated data. |

### WEAK Branch: Day 14 Re-Assessment (schedule now)

At Day 14 (July 1, 2026), re-assess with 14 days of accumulated signal. The Day 14 check uses the same thresholds as this tree:
- 3+ Score 3+ replies across both domains → upgrade to STRONG branch, activate all Tier 2 contacts
- 1-2 Score 3+ replies → upgrade to MODERATE branch, activate Domain 51 Tier 1 expansion
- Still 0 replies → run POST_WAVE_2_ENGAGEMENT_ANALYSIS_TEMPLATE.md Section 7.3 Systemic Zero-Engagement Diagnostic and proceed to publication channel submission

**Schedule Day 14 reminder now**: July 1, 2026, 17:00 UTC.

### WEAK Branch: Messaging Pattern Analysis

Zero replies does not tell you that the messaging is wrong — it tells you nothing yet. However, use the Day 7-14 window to review:
1. Subject line clarity: Does the subject line communicate the specific urgency (Senate Finance markup, California ballot) or is it a generic research-sharing subject?
2. Opening paragraph specificity: Does the opening paragraph name the specific organization's mission connection, or is it a general advocacy overview?
3. Gist link placement: Is the Gist URL placed above the fold (visible without scrolling) or buried below signature?

Apply any identified improvements to Tier 2 sends when those sends activate at Day 14+.

---

## Step 3D: DIAGNOSTIC Branch

*Condition: delivery rate below 80% (more than 2 bounces from 10 sends) AND zero replies.*
*Estimated time: 15-20 minutes including resolution.*

### DIAGNOSTIC Branch: This Is Not Failure — This Is Infrastructure

A below-80% delivery rate from a 10-contact send pool almost certainly indicates a bounce that was not properly classified during the send review. Resolution takes 5-10 minutes.

### DIAGNOSTIC Branch: Resolution Checklist

- [ ] Run POST_WAVE_2_ENGAGEMENT_ANALYSIS_TEMPLATE.md Section 7.1 Delivery Diagnostic (5 minutes)
- [ ] For each hard bounce: switch to backup email from DOMAIN_51_CONTACT_REACHABILITY_SNAPSHOT.md or DOMAIN_59_CONTACT_REACHABILITY_SNAPSHOT.md
- [ ] Re-send to bounced contacts using backup email within 24 hours
- [ ] Do NOT activate Tier 1 expansion until bounce resolution is complete
- [ ] After bounce resolution: re-classify as WEAK branch (not DIAGNOSTIC) and proceed with WEAK branch protocol

**Domain 59 exception applies here too**: If the DIAGNOSTIC branch fires but the Senate Finance markup is still active, the Domain 59 express path STILL executes with confirmed-deliverable contacts. Bounce resolution is required only for the specific bounced contacts, not for all contacts.

---

## Step 4: Next-Action Dispatch Summary

*One-page summary of what happens immediately after the checkpoint, whichever branch you are on.*

### Immediate Actions by Branch (complete within 2 hours of checkpoint)

| Branch | Domain 59 Action (Today) | Domain 51 Action (Today) | First Research Action |
|--------|---|---|---|
| STRONG | Express path: AFL-CIO, CBPP, NWLC (45 min) | Pre-flight Domain 51 (30 min prep) | Begin D59 Zone 1 research (Day 1) |
| MODERATE-A | Express path: AFL-CIO, CBPP, NWLC (45 min) | No Domain 51 send today | None — express path only |
| MODERATE-B | Express path: AFL-CIO, CBPP, NWLC (45 min) | Pre-flight Domain 51 (30 min prep) | Begin D59 Zones 1-2 (Day 1) |
| WEAK | Express path: AFL-CIO, CBPP, NWLC (45 min) | No Domain 51 send — hold to Day 14 | None |
| DIAGNOSTIC | Express path (D59 confirmed-deliverable contacts only) | Bounce resolution for bounced contacts | Defer until bounce resolved |

### Logging Requirements (execute alongside sends)

- [ ] Log all Domain 59 sends in: `projects/resistance-research/domain-59-send-log-june1.md`
- [ ] Log all Domain 51 sends in: `DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md`
- [ ] Run orchestration script status check: `uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --all-domains-status`
- [ ] Log any replies received: `uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --log-reply [contact#] --signal [STRONG/MODERATE/WEAK] --summary "[brief note]"`
- [ ] Log checkpoint result in WORKLOG.md: branch determined, domains activated/deferred, next checkpoint date

### WORKLOG Entry Template (paste into WORKLOG.md after checkpoint)

```
## June 17-18, 2026 — Day 7 Checkpoint

**Branch**: [STRONG / MODERATE-A / MODERATE-B / WEAK / DIAGNOSTIC]
**Domain 59 replies received**: [count] (Score 3+: [count])
**Domain 51 replies received**: [count] (Score 3+: [count])
**Domain 59 Gist view delta**: [number]
**Domain 51 Gist view delta**: [number]
**Delivery rate**: [%] ([bounces] bounces from [total] sends)
**Senate Finance markup status**: [ACTIVE / PASSED / STALLED]
**California ballot status**: [ON BALLOT / REMOVED]

**Actions taken today (Day 7)**:
- Domain 59 express path: [executed / deferred / not applicable]
- Domain 51 Tier 1 expansion: [executed / deferred to Day 14 / not applicable]

**Next checkpoint**: [Day 14 = July 1, 2026 at 17:00 UTC — if WEAK or MODERATE-A]
**Next checkpoint**: [Day 14 = ongoing per STRONG branch stagger — if STRONG or MODERATE-B]

**Resource plan**: [reference PHASE_2_RESOURCE_ALLOCATION_CONTINGENCY_MATRIX.md row for this scenario]
```

---

## Step 5: Contingency Overrides

*These conditions override the branch logic above. Check these last.*

### Override 1 — External Deadline Passed: Senate Finance CTC Markup Closed

**If Senate Finance markup has closed before checkpoint**:
- Domain 59 pivots to "2027 Reform Coalition" frame per DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md Part 7, Contingency 1.
- Do not cancel sends — reframe. All 14 Domain 59 contacts remain valid for the 2027 legislative cycle build.
- This override applies regardless of engagement branch.

### Override 2 — Gist 404 at Checkpoint

**If either Gist URL returns 404**:
- Fix Gist immediately before any sends in that domain (10-minute procedure per DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md Part 1, Check 2).
- No sends to that domain until Gist is live.
- This procedure takes precedence over all branch logic.

### Override 3 — Strong Early Signal Arrived Before Checkpoint

**If Score 4-5 reply received before Day 7 (i.e., during Days 1-6)**:
- Do not wait for Day 7 checkpoint. Activate STRONG branch immediately.
- CBPP replying about Senate Finance testimony is the prototype Score 5 event. If CBPP replies with a request for Senate staff briefing materials, activate all STRONG branch checklists that day.

### Override 4 — Opt-Out Event

**If 2+ opt-out or explicit no-contact responses from same domain**:
- Halt that domain's remaining scheduled sends pending framing review.
- Proceed with the other domain unaffected.
- See POST_WAVE_2_ENGAGEMENT_ANALYSIS_TEMPLATE.md Section 6, Trigger 3 for details.

---

*Decision tree prepared June 14, 2026. All execution package references point to production-ready files committed to master. No data required to use this document — data arrives at checkpoint from POST_WAVE_2_ENGAGEMENT_ANALYSIS_TEMPLATE.md Section 8.*
