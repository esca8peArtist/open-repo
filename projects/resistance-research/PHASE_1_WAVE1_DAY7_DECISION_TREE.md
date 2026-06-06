---
title: "Phase 1 Wave 1 — Day 7 Checkpoint Decision Tree"
created: 2026-06-06
version: 1.0
status: production-ready
scope: >
  Engagement level routing to Phase 2 activation paths. Run June 17, 2026
  immediately after completing PHASE_1_WAVE1_ANALYSIS_TEMPLATE.md.
  Input: composite score from Analysis Template Section 4.
  Output: Path A / B / C / FAILURE routing + Domain 51 / 59 sequencing + Domain 54 pre-check trigger.
checkpoint_date: "June 17, 2026"
execution_time: "5-8 minutes (after metrics collected)"
companion_files:
  - PHASE_1_WAVE1_ANALYSIS_TEMPLATE.md (run first — provides composite score)
  - PHASE_1_WAVE1_CONTINGENCY_ROUTING.md (run if Path C or FAILURE)
  - DOMAIN_51_JUNE_16_DECISION_LOGIC.md (domain-specific routing companion)
---

# Phase 1 Wave 1 — Day 7 Checkpoint Decision Tree
## June 17, 2026

**Run this document only after completing PHASE_1_WAVE1_ANALYSIS_TEMPLATE.md.**

**Required inputs** (transfer from Analysis Template, Section 4):
- Composite score: ___/40
- Total Score 3+ replies: ___
- Total Gist clicks (all domains): ___
- Constituencies with Score 3+ signal: ___ / 7
- Any Score 5 (explicit adoption): Y / N
- Any Score 4 (forward or network signal): Y / N; Count: ___

---

## PART 1 — Priority Override Check

Run this before anything else. These conditions override all threshold routing.

```
PRIORITY CHECK 1: Score 5 (Explicit Adoption)

  Was any Score 5 reply received between June 10-17?
  YES  -->  PRIORITY OVERRIDE: Path A activated immediately regardless of composite score.
            Actions (same day):
            1. Log adoption in CHECKIN.md under "Score 5 confirmed — [Org] — [Date]"
            2. Activate Domain 51 immediate: pull DOMAIN_51_JUNE_16_DECISION_LOGIC.md,
               execute Section 3.1 (STRONG path), send Tier 2 contacts within 48 hours
            3. Activate Domain 59 immediate: pull domain-59-send-templates.md,
               send to next wave of contacts within 48 hours
            4. Use the adoption as social proof in all subsequent outreach emails:
               add one sentence — "A [law school / civil rights org / labor union] contact
               has already committed to integrating this into [their work]" — to opening
               paragraph of all Domain 51/59 emails
            5. Flag Domain 54 pre-check: pull DOMAIN_54_RESEARCH_OUTLINE.md and
               verify Gist is live — Domain 54 activation window opens immediately
            6. Proceed to Phase 2 without further checkpoint gates
            [DONE — skip Part 2 entirely]
  NO   -->  Continue to Priority Check 2


PRIORITY CHECK 2: Score 4 cluster (2+ forwards or network signals)

  Were 2 or more Score 4 replies received June 10-17?
  YES  -->  STRONG SIGNAL CONFIRMED
            Actions:
            1. Log both contacts in CHECKIN.md as "Score 4 cluster — Phase 2 staging"
            2. Treat as composite score STRONG regardless of open/click metrics
            3. Proceed to PATH A actions below
            4. Note: Score 4 cluster without a Score 5 means Phase 2 activates but
               without social-proof language in outreach until Score 5 is confirmed
  NO   -->  Continue to Part 2 (threshold routing)
```

---

## PART 2 — Threshold Routing by Composite Score

**Input**: Composite score from Analysis Template Section 4 (range 0-40).

```
IF composite score 30-40  -->  PATH A (STRONG)
IF composite score 18-29  -->  PATH B (MODERATE)
IF composite score 8-17   -->  PATH C (WEAK)
IF composite score 0-7    -->  FAILURE PATH
```

**My composite score**: ___  
**Routing decision**: PATH ___ (circle one: A / B / C / FAILURE)

---

## PATH A — STRONG SIGNAL
### Trigger: Composite 30-40 OR Priority Override (Score 5 / Score 4 cluster)
### Signal: 3+ responses / 100+ Gist views / 4+ constituencies engaged

**Interpretation**: Wave 1 engagement validates the research and the contact list. Recipients are reading, clicking, and engaging substantively. Phase 2 acceleration is warranted.

---

### Path A — Domain 51 Routing

**Activation**: IMMEDIATE (within 48 hours of June 17 checkpoint)

Next-action checklist:
- [ ] Verify Domain 51 Gist is live: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372
- [ ] Pull DOMAIN_51_JUNE_16_DECISION_LOGIC.md and confirm you are in Section 3.1 (STRONG path)
- [ ] Pull DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md — activate Tier 2 contacts (state-level contacts: Montana I-194, Michigan Clean Elections, New Mexico campaign finance reform orgs)
- [ ] Send Domain 51 Tier 2 outreach June 17-19 (48-hour window)
- [ ] Email framing: reference any Score 3+ replies from Domain 51 Wave 1 contacts as social proof
- [ ] Log all sends in DISTRIBUTION_EXECUTION_LOG.md under "Domain 51 Tier 2 Activation — Path A"

**Success criteria** (Day 14, June 24 secondary checkpoint):
- Domain 51 Tier 2 open rate ≥30%
- At least 1 Score 3+ reply from Tier 2 contacts
- Gist clicks continue at ≥5/week pace

---

### Path A — Domain 59 Routing

**Activation**: IMMEDIATE (within 48 hours of June 17 checkpoint)

Next-action checklist:
- [ ] Verify Domain 59 Gist is live: https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba
- [ ] Pull domain-59-send-templates.md — templates 1-5 are production-ready
- [ ] Identify next wave contacts: CBPP, ITEP, NWLC, Economic Security Project, labor union contacts not yet reached in June 10-13 window
- [ ] Send Domain 59 Wave 2 outreach June 17-20 window
- [ ] Email framing: if any labor or mutual aid contacts showed Score 3+ in June 10-13 wave, reference as social proof
- [ ] Log all sends in DISTRIBUTION_EXECUTION_LOG.md under "Domain 59 Wave 2 Activation — Path A"

**Success criteria** (Day 14, June 24 secondary checkpoint):
- Domain 59 Wave 2 open rate ≥30%
- At least 1 Score 3+ reply from labor or mutual aid contacts

---

### Path A — Domain 54 Pre-Check

**Trigger**: Path A activates Domain 54 pre-check

- [ ] Pull DOMAIN_54_RESEARCH_OUTLINE.md — verify research scope and completeness
- [ ] Verify Domain 54 Gist URL in DOMAIN_54_GIST_URL.txt — confirm live
- [ ] Check DOMAIN_54_PRELIMINARY_FINDINGS.md — is this ready for distribution or still in research phase?
- [ ] Decision gate: If Domain 54 Gist is live AND preliminary findings complete → add to June 24-30 send window
  - If Domain 54 is still research-only → flag for agent research sprint before July 10 checkpoint
- [ ] Log Domain 54 status in CHECKIN.md: "Domain 54 pre-check: [READY FOR DISTRIBUTION / NEEDS RESEARCH / HOLD]"

---

### Path A — Resource Estimate

| Activity | Time Required | When |
|----------|--------------|------|
| Domain 51 Tier 2 contact verification | 30 min | June 17-18 |
| Domain 51 Tier 2 email personalization and sends | 60-90 min | June 17-19 |
| Domain 59 Wave 2 contact verification | 20 min | June 17-18 |
| Domain 59 Wave 2 email sends | 60-75 min | June 17-20 |
| Domain 54 pre-check | 15 min | June 17 |
| CHECKIN.md update | 10 min | June 17 |
| **Total** | **3.0-3.7 hours** | June 17-20 |

**Next checkpoint**: June 24 (Day 14) — verify Path A sends are generating engagement before Domain 54 send decision.

---

## PATH B — MODERATE SIGNAL
### Trigger: Composite 18-29
### Signal: 1-2 responses / 25-99 Gist views / 2-3 constituencies engaged

**Interpretation**: Wave 1 has confirmed delivery and some substantive engagement, but not at high velocity. Normal institutional reply cycle timing may explain the gap. Phase 2 proceeds on the original schedule with selective follow-up in highest-engagement constituencies.

---

### Path B — Pre-Action: Constituency Triage

Before executing Domain 51/59 routing, identify which constituencies showed signal. This determines where follow-up is worth the time investment.

| Constituency | Score 3+ count | Signal level | Follow-up warranted? |
|---|---|---|---|
| Law Schools | ___ | | Y / N |
| Immigration/Civil Rights | ___ | | Y / N |
| Academic | ___ | | Y / N |
| Faith | ___ | | Y / N |
| Labor | ___ | | Y / N |
| Mutual Aid | ___ | | Y / N |
| Campaign Finance/Gov | ___ | | Y / N |

**Rule**: Follow-up is warranted for any constituency with Score 3+ ≥ 1. For constituencies at zero, hold until Day 30 rather than resending — resending to unresponsive contacts in the first 14 days generates negative signals (unsubscribes, spam flags).

---

### Path B — Domain 51 Routing

**Activation**: Selective follow-up + on-schedule (June 12-15 original timeline, or next available window)

Next-action checklist:
- [ ] Review Domain 51 constituency signal: Did CLC or Issue One (Wave 1) show Score 3+?
  - YES: Send Tier 2 contacts June 17-22, referencing their reply as social proof
  - NO: Continue Domain 51 monitoring. Day 30 checkpoint (July 10) is primary routing gate
- [ ] Did Common Cause CA or LWV CA (Wave 2, June 12-13) show Score 3+?
  - YES: Send Montana/Michigan/New Mexico Tier 2 contacts June 17-22
  - NO: Hold Tier 2 activation until Day 30 checkpoint
- [ ] Log Domain 51 routing in CHECKIN.md: "Domain 51 Day 7 Path B — [constituencyX scored / all HOLD]"
- [ ] Set reminder: Day 30 checkpoint July 10 for full Domain 51 Phase 2 go/no-go

**Resource estimate**: 1.5-2.5 hours for selective follow-up (if triggered), 0 hours if all constituencies hold.

---

### Path B — Domain 59 Routing

**Activation**: On original schedule (June 12-15 window, now shifted to June 17-22 if not yet sent)

Next-action checklist:
- [ ] Check Domain 59 send status: Were CBPP, ITEP, NWLC sends completed in June 3-5 window (per CHECKIN.md)?
  - If YES (already sent): Monitor existing sends. Do not re-send.
  - If NO (not yet sent): Execute Domain 59 sends June 17-22 — see domain-59-send-templates.md
- [ ] Did labor or mutual aid constituencies show any engagement in June 10-17?
  - YES: Send Domain 59 Wave 2 referencing labor signal as social proof
  - NO: Send Domain 59 Wave 2 as planned without social proof framing
- [ ] Log: "Domain 59 Day 7 Path B — [status: on schedule / selective follow-up / monitoring]"

**Resource estimate**: 60-90 min for Domain 59 sends if not previously completed.

---

### Path B — Domain 54 Pre-Check

**Trigger**: Path B triggers Domain 54 pre-check but does NOT activate distribution

- [ ] Pull DOMAIN_54_RESEARCH_OUTLINE.md — confirm research phase status
- [ ] Log: "Domain 54 pre-check: [RESEARCH PHASE — not ready for distribution / HOLD]"
- [ ] Set reminder: Domain 54 distribution readiness review at July 10 Day 30 checkpoint

---

### Path B — Success Criteria and Escalation

**Day 14 secondary checkpoint (June 24)**:

```
Did selective follow-up contacts (constituencies with Score 3+) generate any new Score 3+ replies?
  YES  -->  Upgrade to Path A. Activate all Path A actions.
  NO   -->  Continue Path B monitoring.

Did any constituency hit 0 opens AND 0 replies AND 0 Gist clicks?
  YES  -->  Run PHASE_1_WAVE1_CONTINGENCY_ROUTING.md for that constituency.
            This is a constituency-specific failure, not a global failure.
  NO   -->  Proceed to Day 30 checkpoint July 10.
```

**Day 30 gate (July 10)**: Full Phase 2 go/no-go across all domains. If Path B has shown at least 2+ total Score 3+ replies by July 10, activate full Phase 2 with social proof framing. If still below 2, escalate to user for channel strategy review.

**Next checkpoint**: June 24 (Day 14) for any constituency with selective follow-up pending. July 10 (Day 30) for all constituencies.

---

## PATH C — WEAK SIGNAL
### Trigger: Composite 8-17
### Signal: 0 responses / <25 Gist views / 0-1 constituencies engaged

**Interpretation**: Wave 1 delivery may have succeeded but engagement failed, or delivery itself is suspect. Root-cause investigation is required before any Phase 2 sends. Phase 2 operates independently from Wave 1 signal (i.e., proceed with Domain 54 research regardless; hold Phase 2 distribution until root cause resolved).

---

### Path C — Root Cause Investigation (Required Before Any Phase 2 Routing)

**Execute this before any other Path C actions. Time budget: 15-20 minutes.**

```
STEP 1: Confirm email delivery

  Check sent folder for all June 10-13 sends.
  Are send timestamps present for all contacts?
  NO  -->  Delivery never occurred. Check draft folder. Re-send using Section 3
           of PHASE_1_WAVE1_CONTINGENCY_ROUTING.md (Recovery: Delivery Not Confirmed).
  YES -->  Delivery occurred. Continue to Step 2.

STEP 2: Check bounce rate

  Search inbox for bounce-back notifications from June 10-17.
  Bounce count: ___
  Bounce rate: ___/total_sent = ___%
  
  If >10% bounce rate:
    -->  CONTACT_VERIFY path. Run PHASE_1_WAVE1_CONTINGENCY_ROUTING.md,
         Section 1 (delivery failure / bounce rate).
         Do NOT proceed to Phase 2 until bounce addresses corrected.
  If <10% bounce rate:
    -->  Delivery confirmed for most contacts. Continue to Step 3.

STEP 3: Check Gist URL accessibility

  Open each Gist URL (list in Analysis Template Section 2) in an incognito window.
  Any 404 or 403?
  YES  -->  Gist inaccessible. Run PHASE_1_WAVE1_CONTINGENCY_ROUTING.md,
            Section 2 (Gist URL broken or untrustworthy).
  NO   -->  All Gists accessible. Continue to Step 4.

STEP 4: Diagnose open rate failure

  Email confirmed sent AND Gist confirmed live AND open rate <20%:
  Most likely causes:
    a) Subject line was too technical or used spam-trigger words
       ("reform", "democratic framework", "feedback request" in isolation)
    b) Send was caught in .edu or nonprofit spam filter
    c) June 10-13 timing hit a conference or academic calendar gap
    d) Contact is no longer at the email address (soft bounce, not hard bounce)

  Test: Send a plain-text email to yourself from the same sender account.
  Does it arrive in your inbox within 5 minutes, or go to spam?
    SPAM  -->  Sender account has a spam reputation issue.
               Run PHASE_1_WAVE1_CONTINGENCY_ROUTING.md, Section 4 (sender reputation).
    INBOX -->  Sender account is clean. Subject line or timing was the likely cause.
               Run Section 5 of PHASE_1_WAVE1_CONTINGENCY_ROUTING.md (subject line revision).
```

---

### Path C — Phase 2 Routing (Post-Investigation)

Domain 51 and Domain 59 routing under Path C depends on root cause finding:

| Root Cause | Domain 51 Action | Domain 59 Action |
|---|---|---|
| Delivery confirmed, subject line weak | Hold Domain 51 Tier 2 until subject-line revision tested (7 days). Re-send to 2 test contacts with new subject. | Same — hold until test confirms new framing works |
| Gist URL broken | Fix Gist URL first. Re-send to original contacts with corrected link + apology note. Then proceed as Path B. | Fix Gist URL. Re-send. |
| Bounce rate >10% | Fix addresses. Re-send corrected batch. Restart Day 7 clock from corrected send date. | Same |
| Sender spam reputation | Switch to alternative email account or channel. Do not re-send until sender reputation cleaned up (48-72h). | Same |
| No root cause found (delivery confirmed, Gist live, sender clean) | Escalate to user — see below | Same |

**If no root cause found**: Escalate to user via CHECKIN.md. Include:
- Confirmed sends: [list]
- Confirmed deliveries: [how confirmed]
- Gist status: [live URLs]
- Sender reputation test result: [INBOX]
- Reply count: 0
- Hypothesis: Domain-audience mismatch or contact list quality issue

---

### Path C — Domain 54 Action

Under Path C, Domain 54 pre-check proceeds independently of Wave 1 signal:
- [ ] Pull DOMAIN_54_RESEARCH_OUTLINE.md
- [ ] This is a research step, not a distribution decision — research regardless of Wave 1 outcome
- [ ] Domain 54 distribution timing: decided at July 10 Day 30 checkpoint based on Wave 1 recovery trajectory

---

### Path C — Success Criteria

Path C exits when:
1. Root cause identified and remediated, AND
2. Re-send to 2-3 test contacts generates at least 1 open within 72 hours

If root cause remediation takes >7 days, escalate to user at Day 14 (June 24) checkpoint regardless of status.

---

## FAILURE PATH
### Trigger: Composite 0-7
### Signal: 0 opens confirmed / 0 clicks / 0 replies / confirmed send with confirmed delivery

**Interpretation**: Significant engagement failure. Wave 1 reached recipients but generated no response whatsoever. This is a content/audience mismatch or a fundamental channel failure. Escalation to user is mandatory before any Phase 2 action.

---

### Failure Path — Immediate Actions (same day as June 17 checkpoint)

- [ ] Flag in CHECKIN.md under "Needs Your Input" — use this template:

```
## Phase 1 Wave 1 Day 7 — FAILURE SIGNAL [June 17, 2026]

Composite score: ___/40 (FAILURE threshold)

Confirmed sends: [list all June 10-13 sends with org names]
Confirmed delivery: [how confirmed — bounce-free sent log / reply count = 0]
Gist status: [all URLs live — verified June 17]
Sender reputation: [inbox test result]
Reply count: 0 / [total_sent]
Gist clicks: [total] 

Root causes investigated:
1. Delivery: [CONFIRMED / NOT CONFIRMED]
2. Gist accessibility: [ALL LIVE / ISSUE FOUND: description]
3. Subject line: [sent lines listed here]
4. Sender spam: [CLEAN / FLAGGED]

Options for user decision:
A) Stakeholder substitution — resend to secondary tier contacts with simplified pitch
B) Channel shift — submit to Lawfare, Just Security, or democracy-focused law reviews
   instead of direct email
C) Framing revision — shift from full-framework overview to single-domain operational pitch
D) Hold Phase 2 entirely — wait for organic signal before any new sends

Recommended option: A + C. Resend to 3 secondary-tier contacts (state-level affiliates,
not national directors) with a 2-paragraph simplified pitch leading with the most operationally
relevant finding for each contact. Test framing before full re-send.

User decision requested by: June 19 (48 hours). If no response by June 19,
default to Option D (hold Phase 2) until July 10 Day 30 checkpoint.
```

- [ ] Do NOT send any Domain 51, Domain 59, or Domain 54 distribution until user responds
- [ ] Do NOT send follow-up emails to original Wave 1 contacts — this generates spam flags

---

## PART 3 — Phase 2 Domain Routing Quick Reference

This table summarizes Phase 2 routing decisions across all paths. Complete after Part 2.

| Domain | Path A | Path B | Path C | Failure |
|--------|--------|--------|--------|---------|
| Domain 51 (Campaign Finance) | IMMEDIATE — Tier 2 June 17-19 | Selective follow-up OR June 12-15 on schedule | HOLD — root cause investigation first | HOLD — user decision required |
| Domain 59 (Economic Precarity) | IMMEDIATE — Wave 2 June 17-20 | On schedule June 17-22 | HOLD — root cause investigation first | HOLD — user decision required |
| Domain 54 (Pre-Check) | ACTIVATE pre-check now | ACTIVATE pre-check, hold distribution | Research continues independently | Research continues independently |

**My routing**:
- Domain 51: ____________ (Path ___, action: ________________________)
- Domain 59: ____________ (Path ___, action: ________________________)
- Domain 54: ____________ (Path ___, action: ________________________)

---

## PART 4 — Constituency-Specific Phase 2 Routing

When aggregate signal is MODERATE (Path B), individual constituencies may warrant different treatment. Check each.

### Domains 39/56 strong, Domains 58/59 weak — Route toward highest-engagement domains

```
IF law school constituency showed Score 3+ AND faith/labor showed 0:
  -->  Phase 2 should prioritize law school framing (judicial, constitutional domains)
       before labor/mutual aid framing (economic precarity domain)
  -->  Implication: run Domain 58 (Tribal Sovereignty — law school primary audience) before Domain 59
       even if original sequence called for Domain 59 first

IF immigration/civil rights showed Score 3+ AND academic showed 0:
  -->  Phase 2 should prioritize civil rights legal framing
  -->  Implication: Domain 58 (Tribal Sovereignty) is the highest-leverage next domain
       — direct audience match with immigration legal aid constituency

IF labor showed Score 3+ AND law school showed 0:
  -->  Phase 2 should lead with economic/labor domains
  -->  Implication: Domain 59 (Economic Precarity) is highest-leverage next domain
       — direct audience match with labor constituency

IF mutual aid showed Score 3+ AND academic showed 0:
  -->  Domain 59 is correct next domain; skip academic framing in initial outreach
  -->  Frame Domain 59 send around immediate community resource implications,
       not research validity
```

**My constituency routing adjustment** (fill only if on Path B):
- Highest-engagement constituency: _______________
- Domain sequence adjustment: _______________

---

## PART 5 — Post-Decision Summary Block

Fill after completing Parts 1-4.

**Date**: June 17, 2026  
**Composite score**: ___/40  
**Path selected**: A / B / C / FAILURE  

**Phase 2 decisions**:
- Domain 51 status: _______________
- Domain 59 status: _______________  
- Domain 54 pre-check status: _______________

**Weak-signal constituencies** (Score 3+ = 0 at Day 7): _______________

**Next checkpoint date**: _______________  
**Next checkpoint trigger**: _______________

**Files updated**:
- [ ] PHASE_1_WAVE1_ANALYSIS_TEMPLATE.md (data filled)
- [ ] PHASE_1_WAVE1_DAY7_DECISION_TREE.md (this document, routing filled)
- [ ] CHECKIN.md (checkpoint summary block added)
- [ ] DISTRIBUTION_EXECUTION_LOG.md (any new sends logged)
- [ ] Engagement inventory spreadsheet (new rows added)

---

## Reference Files

| File | Purpose |
|------|---------|
| `PHASE_1_WAVE1_ANALYSIS_TEMPLATE.md` | Run first — collects all input metrics |
| `PHASE_1_WAVE1_CONTINGENCY_ROUTING.md` | Failure mode handlers for Path C and FAILURE |
| `DOMAIN_51_JUNE_16_DECISION_LOGIC.md` | Domain 51 specific STRONG/MODERATE/WEAK routing |
| `domain-59-send-templates.md` | Domain 59 email templates for Wave 2 activation |
| `DOMAIN_54_RESEARCH_OUTLINE.md` | Domain 54 research scope for pre-check |
| `DOMAIN_54_GIST_URL.txt` | Domain 54 Gist URL for accessibility verification |
| `DISTRIBUTION_EXECUTION_LOG.md` | Log all new sends here |
| `CHECKIN.md` | All escalations and user decision requests go here |

---

*Prepared June 6, 2026. Companion to PHASE_1_WAVE1_ANALYSIS_TEMPLATE.md and PHASE_1_WAVE1_CONTINGENCY_ROUTING.md.*
