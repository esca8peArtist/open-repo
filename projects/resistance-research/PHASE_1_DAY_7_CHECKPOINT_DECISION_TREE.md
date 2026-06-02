---
title: "Phase 1 Day 7 Checkpoint Decision Tree — Consolidated"
created: 2026-06-02
version: 1.0
status: production-ready
run_date: "June 7-8, 2026 (Day 7 from Domain 39 June 1 send)"
scope: >
  Consolidated Day 7 decision tree integrating base HOLD/MONITOR/ESCALATE/CONTACT_VERIFY
  determination with Phase 2 Domain 58/59 activation logic. Run in 15-20 minutes.
  All inputs drawn from Google Sheets dashboard and Gmail label.
companion: "phase-1-adoption/DAY_7_CHECKPOINT_DECISION_TREE.md (full technical reference)"
---

# Phase 1 Day 7 Checkpoint Decision Tree

**Run date**: June 7-8, 2026

**Total time**: 15-20 minutes

**Output**: (1) Base determination HOLD/MONITOR/ESCALATE/CONTACT_VERIFY; (2) Phase 2 Domain 58/59 sequencing decision; (3) CHECKIN.md update

---

## Before You Start: Pull These Three Numbers

Open Google Sheets `Phase 1 Impact Dashboard — June 2026`.

| # | What | Where | Value |
|---|------|-------|-------|
| 1 | Total Bitly clicks (all links, Days 1-7) | Gist_Views tab > Cumulative column, Week 1 row | [ ] |
| 2 | Total replies received (any score) | Contacts tab > "Any reply" summary cell | [ ] |
| 3 | Total bounces | Contacts tab > "Bounced" summary cell or =COUNTIF(G3:G200,"Bounced") | [ ] |

Also run the script to generate the automated Day 7 summary:

```bash
python3 /home/awank/dev/SuperClaude_Framework/projects/resistance-research/phase-1-adoption/phase-1-adoption-tracking-script.py --day7-report
```

Review `data/week-01-*-summary.md` for any alerts the script flagged automatically.

---

## Part 1: Base Day 7 Determination

Run this tree with your three numbers. Follow in order. Stop at the first match.

```
STEP 1 — Check bounces
   Bounces >= 3?
   YES  ->  CONTACT_VERIFY
            Actions:
            1. Identify which email addresses bounced (check sent folder for failure notifications)
            2. Find corrected addresses via org websites or LinkedIn
            3. Resend to corrected addresses
            4. Restart Day 7 clock from the corrected send date
            5. Update Contacts tab: Delivery_Status = "Bounced" for failed; "Unknown" for resent
            6. Flag in CHECKIN.md under "Needs Your Input"
            7. Do NOT proceed to Phase 2 sequencing until delivery is confirmed
   NO   ->  Continue to Step 2

STEP 2 — Check click velocity
   Total Bitly clicks >= 15?
   YES  ->  Proceed to Step 3
   NO   ->  Is it 5-14?
            YES  ->  MONITOR
                     Interpretation: delivery confirmed; open rate below target;
                     secondary wave or delayed openers may arrive by Day 14
                     Action: recheck at Day 14 (June 14-15)
                     Proceed to Phase 2 sequencing below (Part 2)
            NO   ->  Is it 0-4?
                     YES (delivery confirmed)  ->  ESCALATE
                                                    Interpretation: emails may have gone to spam,
                                                    or Bitly links were not embedded in sent emails
                                                    Actions:
                                                    1. Check sent folder — are Bitly links (bit.ly/drp-d56
                                                       and bit.ly/drp-d39) present in sent emails?
                                                    2. If YES to Bitly links: possible spam filtering —
                                                       send a brief re-send to 2 test contacts with a
                                                       plain-text message and no links
                                                    3. If NO to Bitly links: raw Gist URLs were sent;
                                                       Bitly data unavailable for Week 1; use reply rate
                                                       as primary signal instead; note in CHECKIN.md
                                                    4. Do NOT resend the full outreach — diagnose first
                                                    Do NOT proceed to Phase 2 sequencing until resolved
                     YES (delivery NOT confirmed)  ->  CONTACT_VERIFY (see above)

STEP 3 — Check reply rate
   Total replies (any score) >= 2?
   YES  ->  DETERMINATION: HOLD
            Interpretation: click velocity and reply rate meet Day 7 targets;
            Phase 1 is on track for Day 30 MODERATE or STRONG
            Proceed to Phase 2 sequencing (Part 2)
   NO   ->  DETERMINATION: MONITOR
            Interpretation: click velocity sufficient but reply signal weak;
            this is not a failure at Day 7 — a 5-7 day delay in institutional replies is normal
            Action: recheck at Day 14 (June 14-15)
            Proceed to Phase 2 sequencing (Part 2)
```

**Base determination**: [HOLD / MONITOR / ESCALATE / CONTACT_VERIFY]

---

## Part 2: Phase 2 Domain 58/59 Activation Logic

Run Part 2 ONLY if Part 1 determination is HOLD or MONITOR.
If Part 1 = ESCALATE or CONTACT_VERIFY: focus entirely on delivery repair before running this section.

### Pull Additional Signal Data

From Google Sheets Replies tab, check constituency-level Score 3+ replies.

You need the count in each column from the Replies tab constituency summary block:

| Signal | Constituency | Min threshold | Value |
|--------|-------------|--------------|-------|
| A | Law School | Score 3+ count | [ ] |
| B | Imm Legal Aid | Score 3+ count | [ ] |
| C | Civil Rights | Score 3+ count | [ ] |
| D | Labor | Score 3+ count | [ ] |
| E | Mutual Aid | Score 3+ count | [ ] |
| F | Academic | Score 3+ count | [ ] |
| G | Any single contact | Reply Score = 4 | [ ] |
| H | Any single contact | Reply Score = 5 | [ ] |

If the Replies tab constituency summary formulas are not yet set up: manually count Score 3+ replies in the Replies tab filtered by Constituency column.

---

### Phase 2 Decision Tree

```
START — Run after Part 1 determination is HOLD or MONITOR

PRIORITY OVERRIDE — Score 5 or Score 4 cluster:

   Was any Score 5 reply received in Days 1-7?
   YES  ->  PRE-ACTIVATE PHASE 2 IMMEDIATELY (both domains)
            Actions (same day as detection):
            1. Log in Adoptions tab as Confirmed
            2. Update CHECKIN.md "Needs Your Input":
               "SCORE 5 RECEIVED — Phase 2 pre-activation triggered [date] from [Org]"
            3. Pull Domain 58 contact list (DOMAIN_58_CONTACT_VERIFICATION.md)
            4. Pull Domain 59 contact list (domain-59-send-templates.md)
            5. Stage both for outreach within 48 hours
            6. Use Score 5 adoption as social proof in Domain 58/59 outreach emails
            7. Do NOT wait for Day 30 checkpoint
            [DONE — both domains activated]
   NO   ->  Continue

   Were 2 or more Score 4 replies received in Days 1-7?
   YES  ->  PRE-DAY-30 STRONG SIGNAL
            Actions:
            1. Log both contacts in Adoptions tab as Probable
            2. Update CHECKIN.md: "Score 4 cluster — 2+ contacts — Phase 2 staging"
            3. Pull Domain 58 contact list; prepare draft outreach referencing Score 4 replies
            4. Pull Domain 59 contact list; prepare draft outreach referencing Score 4 replies
            5. Next gate: Day 14 (June 14-15) — confirm Score 4 signals are holding before sending
            [Domain 58 status: STAGE FOR DAY 14]
            [Domain 59 status: STAGE FOR DAY 14]
   NO   ->  Continue to domain-specific checks

DOMAIN 58 (Tribal Sovereignty) — primary audience: law schools, civil rights orgs, immigration legal aid, academic

   Condition: A >= 2 OR B >= 1 OR C >= 2 OR F >= 1
   (i.e., at least one primary constituency has Score 3+ signal at the Day 7 minimum)

   YES  ->  DOMAIN 58 EARLY SIGNAL DETECTED
            Actions:
            1. Flag in CHECKIN.md: "Domain 58 early signal — [which constituency] — staging Day 14"
            2. Pull Domain 58 contact list from DOMAIN_58_CONTACT_VERIFICATION.md
            3. Verify Domain 58 Gist accessible:
               https://gist.github.com/esca8peArtist/0caf4e1ab5661355ea2df5e53d3c169f
            4. Draft personalized outreach referencing specific Score 3+ reply as social proof
               (quote: "A [law school / civil rights org] contact asked specifically about [topic]")
            5. Do NOT send yet — wait for Day 14 confirmation
            Next gate: Day 14 — if signal is still holding, send Domain 58 outreach Day 14-21 window
            [Domain 58 status: STAGE FOR DAY 14]

   NO   ->  DOMAIN 58 HOLD
            No early signal from Domain 58 primary constituencies
            Next gate: Day 30 — will activate at MODERATE or STRONG determination
            [Domain 58 status: HOLD — STAGE AT DAY 30]

DOMAIN 59 (Economic Precarity) — primary audience: labor unions, mutual aid networks, academic

   Condition: D >= 1 OR E >= 1 OR F >= 1
   (i.e., any Score 3+ signal from at least one of Domain 59's three primary constituencies)

   YES  ->  DOMAIN 59 EARLY SIGNAL DETECTED
            Actions:
            1. Flag in CHECKIN.md: "Domain 59 early signal — [which constituency] — staging Day 14"
            2. Pull Domain 59 contact list from domain-59-send-templates.md
            3. Verify Domain 59 Gist accessible:
               https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba
            4. Draft personalized outreach referencing specific Score 3+ reply as social proof
            5. Do NOT send yet — wait for Day 14 confirmation
            Next gate: Day 14 — if signal is still holding, send Domain 59 outreach Day 14-21 window
            [Domain 59 status: STAGE FOR DAY 14]

   NO   ->  DOMAIN 59 HOLD
            No early signal from Domain 59 primary constituencies
            Next gate: Day 30 — will activate at MODERATE or STRONG determination
            [Domain 59 status: HOLD — STAGE AT DAY 30]

NEITHER DOMAIN SHOWS EARLY SIGNAL:
   Normal trajectory. Both domains activate on Day 30 schedule.
   No Phase 2 sequencing changes at this time.
   Next checkpoint: Day 14 (June 14-15) if base = MONITOR
                    Day 30 (June 27-28) if base = HOLD
```

---

## Part 3: Day 14 Gate (run June 14-15 if Day 7 = MONITOR or early signal detected)

### Data to pull at Day 14

| Metric | Value | Source |
|--------|-------|--------|
| Cumulative Bitly clicks | [ ] | Gist_Views tab, Cumulative column |
| Cumulative Score 3+ replies | [ ] | Contacts tab, Score 3+ replies summary |
| Domain 58 constituency signal (A + B + C) | [ ] | Replies tab, Law School + Imm Legal Aid + Civil Rights Score 3+ |
| Domain 59 constituency signal (D + E + F) | [ ] | Replies tab, Labor + Mutual Aid + Academic Score 3+ |

### Day 14 determination

```
Cumulative clicks >= 25 AND Score 3+ replies >= 2?
   YES  ->  UPGRADE to HOLD; confirm Phase 2 sequencing per Day 30 normal track
   NO   ->  Apply Modification 2 (framing revision) before any new sends

Domain 58 early signal still holding (Score 3+ from A or B or C still active)?
   YES  ->  SEND Domain 58 outreach to staged contacts within Day 14-21 window
   NO   ->  HOLD Domain 58 to Day 30 standard track

Domain 59 early signal still holding (Score 3+ from D or E or F still active)?
   YES  ->  SEND Domain 59 outreach to staged contacts within Day 14-21 window
   NO   ->  HOLD Domain 59 to Day 30 standard track
```

---

## Part 4: Day 30 Full Go/No-Go (run June 27-28)

This supersedes all early signal decisions. The Day 30 determination sets final Phase 2 sequencing.

### Domain 58 Go/No-Go Matrix

| Day 30 Determination | Domain 58 Action |
|---------------------|-----------------|
| STRONG | Launch Domain 58 immediately (Days 1-2 of Phase 2 launch) |
| MODERATE | Launch Weeks 5-6 (July 5-12) — use Score 3+ replies from law school/civil rights as social proof |
| WEAK | Hold — do not send until ASSESS or better at Day 60 |
| ASSESS | Launch only if Law School or Civil Rights constituency is at Score 3+ threshold |
| FAILURE | User decision — hold pending 48-hour CHECKIN.md review |

### Domain 59 Go/No-Go Matrix

| Day 30 Determination | Domain 59 Action |
|---------------------|-----------------|
| STRONG | Launch Domain 59 Days 1-2 of Phase 2 launch |
| MODERATE | Launch Weeks 6-8 (July 12-26) — use Labor or Mutual Aid Score 3+ as social proof |
| WEAK | Hold — Modifications 1-3 must complete before Domain 59 outreach |
| ASSESS | Launch only if Labor or Mutual Aid constituency shows any Score 3+ signal |
| FAILURE | User decision — hold |

### Social proof requirement (applies to both Domain 58 and 59 sends)

Before sending either domain, confirm at least ONE of:
- 1 Score 4 reply from a contact in the target constituency
- 2+ Score 3 replies that reference the domain topic area
- 1 confirmed adoption (Score 5) from any constituency

Without social proof, Domain 58/59 outreach faces the same cold-contact disadvantage as the initial Wave 1. The compounding value of Phase 2 depends on demonstrating that existing recipients are engaging — which is the social proof mechanism.

---

## Part 5: CHECKIN.md Update Template

After completing Parts 1 and 2, copy this block into `CHECKIN.md` under the current date entry:

```
## Phase 1 Day 7 Checkpoint — [DATE]

**Run date**: [YYYY-MM-DD]

**Inputs**:
- Total Bitly clicks (Days 1-7): [X]
- Total replies (any score): [X]
- Total bounces: [X]

**Base Determination**: [HOLD / MONITOR / ESCALATE / CONTACT_VERIFY]

**Phase 2 Sequencing**:
- Domain 58 (Tribal Sovereignty): [EARLY SIGNAL — STAGE DAY 14 / HOLD — DAY 30 / PRE-ACTIVATED]
- Domain 59 (Economic Precarity): [EARLY SIGNAL — STAGE DAY 14 / HOLD — DAY 30 / PRE-ACTIVATED]
- Priority override (Score 4 cluster or Score 5): [YES: description / NO]

**Score 3+ constituency signals**:
- Law School: [X] | Imm Legal Aid: [X] | Civil Rights: [X]
- Academic: [X] | Faith: [X] | Labor: [X] | Mutual Aid: [X]

**Actions taken**:
- [ ] Script run: python3 phase-1-adoption-tracking-script.py --day7-report
- [ ] Checkpoints tab updated with this row
- [ ] Synthesis_Log tab updated
- [ ] Domain 58 contact list staged: [YES / NO — N/A]
- [ ] Domain 59 contact list staged: [YES / NO — N/A]

**Next checkpoint**: [Day 14, June 14-15 / Day 30, June 27-28]

**Files updated**:
- [ ] CHECKIN.md (this entry)
- [ ] Google Sheets Checkpoints tab
- [ ] monitoring/phase-1-week-1-synthesis-[YYYY-MM-DD].md
```

---

## Part 6: Constituency-Level Thresholds Quick Reference

These are the minimum signals for Day 7 Phase 2 early activation. None of these require HOLD determination — they apply equally to MONITOR outcomes.

### Domain 58 (Tribal Sovereignty) constituency requirements

Primary audience: law schools, immigration legal aid, civil rights organizations, academic researchers

| Constituency | Day 7 minimum signal | Weight |
|-------------|---------------------|--------|
| Law School | >= 2 Score 3+ replies | High — law school engagement predicts litigation toolkit adoption |
| Imm Legal Aid | >= 1 Score 3+ reply | High — immigration context is core to tribal sovereignty framing |
| Civil Rights | >= 2 Score 3+ replies | High — civil rights organizations are primary Domain 58 users |
| Academic | >= 1 Score 3+ reply | Medium — academic engagement signals research citation pathway |

**Early signal trigger**: ANY one of these thresholds met at Day 7.

### Domain 59 (Economic Precarity) constituency requirements

Primary audience: labor unions, mutual aid networks, academic researchers

| Constituency | Day 7 minimum signal | Weight |
|-------------|---------------------|--------|
| Labor | >= 1 Score 3+ reply | High — labor unions are Domain 59's primary institutional deployment pathway |
| Mutual Aid | >= 1 Score 3+ reply | High — mutual aid network coordinators have immediate implementation capacity |
| Academic | >= 1 Score 3+ reply | Medium — confirms research validity pathway |

**Early signal trigger**: ANY one of these thresholds met at Day 7.

### Important timing note — constituency-specific reply cycles

**Law Schools**: A Score 3 reply from a faculty member at Day 7 predicts Score 5 adoption (citation, syllabus inclusion) within 60-90 days — the normal academic publication cycle. Do not expect Score 5 from academic contacts by Day 30.

**Immigration Legal Aid**: Adoption timeline can be days if active litigation is in progress. Any mention of a pending case in a Score 3+ reply should escalate to CHECKIN.md immediately with a same-day response to the contact.

**Labor Unions**: Training cycle timing drives adoption. If a union contact says "our next training cycle is in September," log the Score 3 reply and set a calendar reminder for August 15 to follow up.

**Mutual Aid**: National umbrella contacts (Score 3) predict less than local network coordinators (Score 3). A Score 3 from a local coordinator is a stronger leading indicator than a Score 4 from a national umbrella contact.

---

## Reference Files

| File | Purpose |
|------|---------|
| `phase-1-adoption/DAY_7_CHECKPOINT_DECISION_TREE.md` | Full technical reference (the v2.0 canonical source) |
| `phase-1-adoption/WEEK_1_DATA_COLLECTION_FRAMEWORK.md` | Day 1-7 checklist, reply triage, scoring calibration |
| `PHASE_1_WEEKLY_MEASUREMENT_TEMPLATES.md` | Google Sheets formulas and Weeks 2-4 guidance |
| `PHASE_1_ADOPTION_DEPLOYMENT_GUIDE.md` | Setup and daily operations guide |
| `PHASE_1_MEASUREMENT_SYSTEM.md` | Full adoption scale definitions and Day 30/60 criteria |
| `DOMAIN_58_CONTACT_VERIFICATION.md` | Domain 58 contact list |
| `domain-59-send-templates.md` | Domain 59 email templates |
| `CHECKIN.md` | Escalation target — update same day for any Score 4+ or Phase 2 decision |
