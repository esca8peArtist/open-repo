---
title: "Day 7 Checkpoint Decision Tree — Phase 2 Domain 58/59 Activation Logic"
created: 2026-06-03
scope: "Go/no-go logic for Phase 2 Domain 58/59 activation based on Week 1 adoption metrics"
status: production-ready
run_date: "June 7-8, 2026 (Day 7 from Domain 39 June 1 send)"
companion: "day-7-14-30-decision-trees.md (base decision trees), PHASE_2_ACTIVATION_DECISION_TREE.md"
---

# Day 7 Checkpoint Decision Tree
## Phase 2 Domain 58/59 Activation Logic

**Run date**: June 7-8, 2026 (Day 7 from Domain 39 June 1 send)

This document supplements `day-7-14-30-decision-trees.md` with Phase 2 Domain 58/59 specific logic. The base Day 7 tree (HOLD/MONITOR/ESCALATE/CONTACT_VERIFY) runs first. The Phase 2 sequencing logic here runs only after the base determination.

---

## Part 1: Base Day 7 Determination (from day-7-14-30-decision-trees.md)

**Data to pull (Google Sheets dashboard):**

| # | Metric | Source | Value |
|---|--------|--------|-------|
| 1 | Week 1 Bitly clicks (total) | Gist_Views tab > col I, row 2 | [ ] |
| 2 | Total bounces | Contacts tab > =COUNTIF(G:G,"Bounced") | [ ] |
| 3 | Total replies (any score) | Contacts tab > summary row "Any reply" | [ ] |

**Run the tree (in order):**

```
1. Bounces >= 3?
   YES -> CONTACT_VERIFY
         Fix email list; resend to corrected addresses
         Restart Day 7 clock (new send = today)
         Document in CHECKIN.md
   NO  -> Continue

2. Bitly clicks >= 15?
   YES -> Check replies (Step 3)
   NO  -> Is it 5-14?
          YES -> MONITOR (recheck Day 14)
          NO  -> Is it 0-4 with confirmed delivery?
                 YES -> ESCALATE (delivery diagnostic)
                 NO  -> [impossible if delivery confirmed]

3. Replies >= 2?
   YES -> DETERMINATION: HOLD
   NO  -> DETERMINATION: MONITOR (recheck Day 14)
```

**Base determination**: [HOLD / MONITOR / ESCALATE / CONTACT_VERIFY]

---

## Part 2: Phase 2 Domain 58/59 Activation Logic

Run Part 2 only after Part 1 determination is HOLD or MONITOR. If Part 1 = ESCALATE or CONTACT_VERIFY, focus on delivery repair before Phase 2 sequencing.

### Additional data to pull (for Phase 2 sequencing only):

| # | Metric | Source | Value |
|---|--------|--------|-------|
| A | Score 3+ replies from Law Schools | Replies tab: constituency = "Law School", score >= 3 | [ ] |
| B | Score 3+ replies from Imm Legal Aid | Replies tab: constituency = "Imm Legal Aid", score >= 3 | [ ] |
| C | Score 3+ replies from Civil Rights | Replies tab: constituency = "Civil Rights", score >= 3 | [ ] |
| D | Score 3+ replies from Labor | Replies tab: constituency = "Labor", score >= 3 | [ ] |
| E | Score 3+ replies from Mutual Aid | Replies tab: constituency = "Mutual Aid", score >= 3 | [ ] |
| F | Score 3+ replies from Academic | Replies tab: constituency = "Academic", score >= 3 | [ ] |
| G | Any Score 4-5 reply | Contacts tab: any Reply_Score >= 4 | [ ] |

### Phase 2 Domain 58/59 Decision Logic

```
START — Run after base Part 1 determination

    ├─ Is base determination HOLD or MONITOR?
    │  NO  -> Skip Phase 2 sequencing; focus on delivery repair
    │  YES -> Continue
    │
    ├─ Score 5 received from any contact?
    │  YES -> PRE-ACTIVATE PHASE 2 IMMEDIATELY (all domains)
    │         Action:
    │         1. Log in Adoptions tab as Confirmed
    │         2. Update CHECKIN.md "Needs Your Input" same day
    │         3. Stage Domain 58 outreach materials for send within 48h
    │         4. Stage Domain 59 outreach materials for send within 48h
    │         5. Do NOT wait for Day 30 checkpoint
    │
    │  NO  -> Continue
    │
    ├─ Score 4 received from 2+ contacts within Days 1-7?
    │  YES -> PRE-DAY-30 STRONG SIGNAL
    │         Action:
    │         1. Log both in Adoption Signal Registry as Probable
    │         2. Update CHECKIN.md with "Score 4 cluster" note
    │         3. Stage Domain 58 outreach materials (ready for Day 14 send)
    │         4. Stage Domain 59 outreach materials (ready for Day 14 send)
    │         5. Next checkpoint: Day 14 (confirm Score 4 is sustaining)
    │
    │  NO  -> Continue
    │
    ├─ DOMAIN 58 ACTIVATION CHECK
    │  (Tribal Sovereignty — target audience: law schools, civil rights orgs, academic)
    │
    │  Condition: A >= 2 OR B >= 1 OR C >= 2 OR F >= 1
    │  (i.e., strong signal from at least one of Domain 58's primary constituencies)
    │
    │  YES -> DOMAIN 58 EARLY SIGNAL DETECTED
    │         Status: Stage for Day 14-21 outreach window
    │         Action:
    │         1. Flag in CHECKIN.md: "Domain 58 early signal — staging for Day 14 outreach"
    │         2. Pull Domain 58 contact list from DOMAIN_58_CONTACT_VERIFICATION.md
    │         3. Verify DOMAIN_58_GIST_URL.md is current
    │         4. Prepare personalized outreach referencing specific Score 3+ replies as social proof
    │         5. Do NOT send yet — wait for Day 14 reconfirmation
    │         Next gate: Day 14 recheck (if base = HOLD, skip to Day 30)
    │
    │  NO  -> DOMAIN 58 HOLD
    │         Status: No early signal; stage at Day 30 STRONG or MODERATE
    │         Action: No action yet on Domain 58
    │
    ├─ DOMAIN 59 ACTIVATION CHECK
    │  (Economic Precarity — target audience: labor unions, mutual aid, academic)
    │
    │  Condition: D >= 1 OR E >= 1 OR F >= 1
    │  (i.e., any Score 3+ signal from Domain 59's primary constituencies)
    │
    │  YES -> DOMAIN 59 EARLY SIGNAL DETECTED
    │         Status: Stage for Day 14-21 outreach window
    │         Action:
    │         1. Flag in CHECKIN.md: "Domain 59 early signal — staging for Day 14 outreach"
    │         2. Pull Domain 59 contact list from domain-59-send-templates.md
    │         3. Verify Domain 59 Gist (70b18a6f26dc879e3399c6d147d882ba) is accessible
    │         4. Prepare personalized outreach referencing specific Score 3+ replies
    │         5. Do NOT send yet — wait for Day 14 reconfirmation
    │         Next gate: Day 14 recheck
    │
    │  NO  -> DOMAIN 59 HOLD
    │         Status: No early signal; stage at Day 30 MODERATE or better
    │         Action: No action yet on Domain 59
    │
    └─ NEITHER DOMAIN SHOWS EARLY SIGNAL
       Status: Normal trajectory — both domains activate at Day 30 checkpoint
       Action: No Phase 2 sequencing changes; proceed to Day 14 or Day 30 checkpoint
```

---

## Part 3: Day 14 Gate (applies only if Day 7 = MONITOR or early signal detected)

Run this on June 14-15, 2026 (Day 14 from Domain 39 send).

### Data to pull (Day 14):

| Metric | Value |
|--------|-------|
| Cumulative Bitly clicks | [ ] |
| Score 3+ reply rate | [ ] |
| Domain 58 constituency signal count | [ ] |
| Domain 59 constituency signal count | [ ] |

### Day 14 Phase 2 Gate:

```
Cumulative clicks >= 25 AND base determination upgrades to HOLD?
  YES -> Confirm Phase 2 sequencing (58 and 59) per Day 30 normal track
  NO  -> Apply Modification 2 (framing revision) before any Phase 2 sends

Domain 58 early signal confirmed (Score 3+ still holding, no reversal)?
  YES -> Send Domain 58 outreach to staged contact list (Day 14-21 window)
  NO  -> Hold Domain 58 to Day 30

Domain 59 early signal confirmed?
  YES -> Send Domain 59 outreach to staged contact list (Day 14-21 window)
  NO  -> Hold Domain 59 to Day 30
```

---

## Part 4: Day 30 Full Go/No-Go for Phase 2 Domains 58/59

Run on June 27-28, 2026.

This supersedes any early signal decisions. The Day 30 determination drives final Phase 2 sequencing.

### Domain 58 Go/No-Go Matrix:

| Day 30 Determination | Domain 58 Status |
|---------------------|-----------------|
| STRONG | Launch immediately — Day 1 alongside Domain 39 |
| MODERATE | Launch Week 5-6 (July 5-12) with social proof from Score 3+ replies |
| WEAK | Hold — do not send until ASSESS or better at Day 60 |
| ASSESS | Launch if Law School or Civil Rights constituency at Score 3+ threshold |
| FAILURE | User decision — hold pending 48h review |

### Domain 59 Go/No-Go Matrix:

| Day 30 Determination | Domain 59 Status |
|---------------------|-----------------|
| STRONG | Launch immediately — Day 1-2 |
| MODERATE | Launch Week 6-8 (July 12-26) |
| WEAK | Hold — Modifications 1-3 must complete before Domain 59 outreach |
| ASSESS | Launch if Labor or Mutual Aid constituency shows any Score 3+ signal |
| FAILURE | User decision — hold |

### Social Proof Requirements (for both domains):

Before sending Domain 58 or 59, confirm at least one of:
- 1 Score 4 reply from a contact in the target constituency
- 2+ Score 3 replies that reference the domain's topic area
- 1 confirmed adoption (Score 5) from any constituency that can be cited

Without social proof, Domain 58/59 sends face the same cold-contact disadvantage as the initial Wave 1. The value of Phase 2 is the social proof compounding effect.

---

## Quick Reference — Checkpoint Template for CHECKIN.md

Copy after completing Parts 1 and 2:

```
## Phase 1 Day 7 + Phase 2 Sequencing — [DATE]

**Base Determination**: [HOLD / MONITOR / ESCALATE / CONTACT_VERIFY]

**Metrics**:
- Total Bitly clicks: [X]
- Total replies: [X]
- Score 3+ replies: [X]
- Bounces: [X]

**Phase 2 Sequencing**:
- Domain 58 (Tribal Sovereignty): [EARLY SIGNAL / HOLD / STAGE DAY 14]
- Domain 59 (Economic Precarity): [EARLY SIGNAL / HOLD / STAGE DAY 14]
- Pre-Day-30 trigger (Score 4 cluster or Score 5): [YES: [description] / NO]

**Next checkpoint**: [Day 14, June 14 / Day 30, June 27]
**Actions taken**: [list]
```

---

## Reference Files

| File | Purpose |
|------|---------|
| `day-7-14-30-decision-trees.md` | Full base decision tree (Part 1) |
| `PHASE_2_ACTIVATION_DECISION_TREE.md` | Full Phase 2 activation tree |
| `DOMAIN_58_CONTACT_VERIFICATION.md` | Domain 58 contact list |
| `domain-59-send-templates.md` | Domain 59 email templates |
| `DOMAIN_58_GIST_URL.md` | Domain 58 Gist URL (confirmed live) |
| `DISTRIBUTION_GIST_URLS.md` | All live Gist URLs |
| `PHASE_1_MEASUREMENT_SPREADSHEET_SPEC.md` | Sheets formula reference |
