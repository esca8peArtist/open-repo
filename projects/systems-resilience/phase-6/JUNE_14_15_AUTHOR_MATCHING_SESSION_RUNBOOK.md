---
title: "June 14–15 Author Matching Session Runbook"
project: systems-resilience
phase: 6
wave: 1
status: PRODUCTION-READY — execute June 14 08:00 CDT
created: 2026-06-10
purpose: "Day-by-day logistics, decision trees, go/no-go gates, and post-matching outputs for the Phase 6 Wave 1 June 14-15 author matching session."
session_lead: "Orchestrator + Project Lead"
non_negotiable_dates:
  - "June 14: Final call-backs + rubric application"
  - "June 15: Final selection + offer delivery"
  - "June 12: Reply-by deadline for outreach (confirms who is in the pool)"
  - "June 20: Wave 1 launch — immovable"
cross_references:
  - PHASE_6_AUTHOR_RECRUITMENT_TARGET_LIST.md
  - AUTHOR_DOMAIN_MAPPING_RUBRIC.md
  - RECRUITMENT_OUTREACH_TEMPLATES.md
  - PHASE_6_WAVE_2_ACTIVATION_CHECKLIST.md
  - RESEARCH_BRIEF_TEMPLATE_SUITE.md
word_count: ~2,800
---

# June 14–15 Author Matching Session Runbook
## Phase 6 Wave 1 — Author Recruitment Execution

> **Purpose of this document**: This runbook governs the two-day author matching session that converts the June 10–12 recruitment outreach into confirmed domain assignments. All decisions, go/no-go calls, and contingency activations are logged here. Post-session output is `AUTHOR_ROSTER_JUNE_15.md` committed to `projects/systems-resilience/phase-6/`.

---

## Pre-Session Prerequisites (Confirm by June 13 EOD)

Before June 14 08:00 CDT, all of the following must be true:

- [ ] PHASE_6_AUTHOR_RECRUITMENT_TRACKING.md is current — all outreach logged, all replies noted
- [ ] June 12 non-respondents have received the reminder email (Template 4)
- [ ] AUTHOR_DOMAIN_MAPPING_RUBRIC.md Section 2 quick reference card is printed or open in a second window
- [ ] PHASE_6_AUTHOR_RECRUITMENT_TARGET_LIST.md fallback candidates section (Section 8) is reviewed — fallback contacts identified for any domain where primary Tier A has not confirmed
- [ ] Reply pool counted: how many confirmed (yes or conditional yes), how many pending (no response), how many declined
- [ ] For each "conditional yes": the condition is documented and a response is drafted

**Minimum viable pool for a full June 14 session**: At least 6 confirmed or conditional-yes candidates across at least 4 of the 6 domains. If fewer than 6 confirmations by June 13 EOD, activate contingency path (see Section 6).

---

## June 14 — Morning Block (08:00–12:00 CDT)

### 08:00–09:00: Final Tier A Call-Backs

*Purpose*: Resolve any "conditional yes" responses and confirm availability for the 4 Tier A candidates with the strongest domain fit scores. This is a phone or video call — not email.

**Call agenda (15 minutes per candidate)**:
1. Confirm the specific domain assignment you are considering for them
2. Confirm availability: start date June 20, 8 hrs/week, 8 weeks
3. Confirm payment terms are acceptable (two-milestone structure)
4. Ask: any scope conditions we need to discuss before you commit?
5. If confirmed: "I will send a formal offer with domain brief by June 15 afternoon."

**Decision rule**: If a candidate cannot confirm June 20 start or 8 hrs/week, do not hold the Tier A slot. Move immediately to fallback (Tier A fallback or Tier B promoted).

**Call-back priority order** (fill from PHASE_6_AUTHOR_RECRUITMENT_TARGET_LIST.md):
- D60: Primary A candidate → fallback if declined
- D61: Primary A candidate → fallback if declined
- D62: Primary A candidate → fallback if declined
- D63: Primary A candidate → fallback if declined
- D64: Primary A candidate → fallback if declined
- D65: Primary A candidate → fallback if declined

**Log each call result** in PHASE_6_AUTHOR_RECRUITMENT_TRACKING.md immediately after the call. Do not rely on memory.

---

### 09:00–10:00: Non-Respondent Assessment

*Purpose*: For each candidate who has not replied to June 10–12 outreach by June 14 08:00 CDT, make a go/no-go call on activating fallback.

**Decision rule for non-respondents**:

```
IF candidate is Tier A primary AND no reply after 2 outreach attempts (June 10 + June 12 reminder):
  → Activate fallback candidate for that domain
  → Do not wait — fallback activation begins June 14 09:00

IF candidate is Tier B AND no reply:
  → Move to next Tier B candidate in target list
  → One more attempt via email is acceptable (send June 14 AM, acknowledge short window)

IF candidate is Tier C AND no reply:
  → Deprioritize; Tier C slots are not critical path for June 20 launch
  → Can be filled June 15–17 from referral network if needed
```

**Non-respondent fallback activation sequence**:
1. Identify the domain with the weakest confirmed author pool
2. Pull fallback candidate from Section 8 of PHASE_6_AUTHOR_RECRUITMENT_TARGET_LIST.md
3. Send a compressed outreach email using Template 1 (Tier A) or Template 2 (Tier B) with a modified close: "Decision window is June 14 by 5 PM CDT — I am trying to confirm by end of day."
4. Log in tracking sheet.

---

### 10:00–12:00: Rubric Application Session

*Purpose*: Apply the five-dimension rubric from AUTHOR_DOMAIN_MAPPING_RUBRIC.md Section 2 to every confirmed candidate. This takes 10–15 minutes per candidate. Run it for all candidates, not just Tier A.

**Rubric application process**:

For each confirmed candidate:
1. Open their most recent public profile (institutional page, SSRN, ResearchGate, organization website)
2. Score D1 (Domain Knowledge): based on publication titles, research descriptions, stated expertise
3. Score D2 (Long-Form Writing): based on publication format — books and practitioner guides score 4–5; academic papers only score 2–3; no long-form history scores 1
4. Score D3 (Markdown/Digital): estimated from digital collaboration context; academics with GitHub or plain-text publishing score 3+; standard academic profile scores 2
5. Score D4 (Research/Citation): based on publication citation quality and annotated bibliography work; PhD researchers score 3+
6. Score D5 (Domain Practitioner Grounding): based on documented hands-on, field, or implementation experience — NOT just research about practitioners. This is the hardest score to assess from public profile; use notes from call-back conversations.

**Rubric output per candidate**:
```
[CANDIDATE_NAME]
D1: ___ / 5
D2: ___ / 5
D3: ___ / 5
D4: ___ / 5
D5: ___ / 5
TOTAL: ___ / 25
TIER: A (20-25) / B (14-19) / C (6-13) / HOLD (<6)
Override rules triggered? Y/N (see rubric Section 2 — Modified Tier Assignment Rules)
```

**Override rules to check**:
- D1 = 1: Do not assign regardless of total score
- D2 = 1: Do not assign regardless of total score
- D5 = 1 AND D1 = 2: Tier C maximum with scope reduction
- D4 < 3: Tier B maximum; project lead citation audit at T+7

**Target completion**: All confirmed candidates scored by 12:00 CDT.

---

## June 14 — Afternoon Block (13:00–17:00 CDT)

### 13:00–15:30: Domain-Author Matching Algorithm Execution

*Purpose*: Apply the Section 3 matching algorithm from AUTHOR_DOMAIN_MAPPING_RUBRIC.md to generate optimal domain assignments.

**Algorithm execution sequence**:

**Step 1** — For each candidate, run the domain eligibility screen:
- Domain 60 eligible if D1 ≥ 3 AND D5 ≥ 3 (both required)
- Domain 61 eligible if D1 ≥ 3 AND D5 ≥ 3
- Domain 62 eligible if D1 ≥ 3 AND D5 ≥ 3
- Domain 63 eligible if D1 ≥ 3 AND D5 ≥ 3
- Domain 64 eligible if D1 ≥ 3 AND D5 ≥ 3
- Domain 65 eligible if D1 ≥ 3 AND D5 ≥ 3

**Step 2** — For each eligible domain, calculate assignment score:
```
Assignment Score = (D1 × 2) + (D5 × 2) + D2 + D4
```

**Step 3** — Apply domain difficulty modifiers:
```
Domain 60: Assignment Score – 2
Domain 61: Assignment Score – 1
Domain 62: Assignment Score – 2
Domain 63: Assignment Score + 0
Domain 64: Assignment Score + 0
Domain 65: Assignment Score – 1
```

**Step 4** — Rank each candidate's eligible domains by adjusted score. Primary assignment = highest-ranked domain.

**Step 5** — Conflict resolution:
- If two Tier A candidates rank the same domain #1: higher D5 score gets that domain; other candidate takes their second-ranked domain.
- If no Tier A or Tier B is eligible for a domain: assign highest-scoring Tier C with project lead co-research support. Flag domain for additional source sprint.

**Tier-to-domain assignment rules**:
- Tier A candidates → primary domain assignments (highest-difficulty domains if eligible: 60, 62 first)
- Tier B candidates → secondary domain assignments OR Tier A-overflow domains
- Tier C candidates → either + mandatory mentorship pairing with adjacent Tier A/B author

**Split-domain eligibility check** (run for each Tier A candidate):
```
IF candidate Tier = A (score 20+):
  AND two candidate domains are in approved adjacent pairs:
    (63+64, 61+62, 64+65)
  AND candidate confirmed 8-10 hrs/week:
  → Split-domain eligible; confirm with candidate before assigning
  → Default remains solo assignment; split is opt-in by candidate
```

---

### 15:30–17:00: Domain Assignment Draft — First Pass

*Purpose*: Produce a draft assignment table for every domain 60–65.

**Draft assignment table template**:

| Domain | Primary Author | Tier | Rubric Score | Backup Author | Backup Tier | Status |
|--------|---------------|------|-------------|---------------|-------------|--------|
| 60 — Int'l Coordination | | | | | | CONFIRMED / PENDING / FALLBACK |
| 61 — Intergenerational | | | | | | |
| 62 — Infrastructure | | | | | | |
| 63 — Ecosystem Restoration | | | | | | |
| 64 — Economic Resilience | | | | | | |
| 65 — Governance Scaling | | | | | | |

**Coverage check**:
- All 6 domains must have at least one confirmed or strongly-likely author by end of June 14
- At least 3 domains should have Tier A primaries
- No domain should have only a Tier C author without a mentorship pairing identified

---

## June 14 — Evening Block (17:00–20:00 CDT)

### 17:00–18:30: Mentorship Pairing Assignment

*Purpose*: For each Tier B and Tier C author, assign a mentorship pairing with the nearest Tier A or strong Tier B author in an adjacent domain.

**Mentorship pairing logic**:
```
Tier C author in Domain X:
  → Pair with Tier A author in highest-adjacent domain
  → Adjacent pairings: 63↔64, 61↔62, 64↔65, 60↔61
  → Mentorship commitment: 1-2 questions/week, informal draft feedback at T+5
  → Confirm mentor availability separately from research commitment
```

**Mentorship pairing does not add hours to mentor**: The pairing is informal (2–3 questions/week answerable in 15–20 minutes). If mentor is already split-domain or has confirmed tight availability (6 hrs/week), do not assign mentorship pairing — use project lead as Tier C support instead.

---

### 18:30–20:00: End-of-Day Assessment

*Purpose*: Assess readiness for June 15 final selection session.

**End-of-June-14 checklist**:
- [ ] All confirmed candidates have rubric scores applied
- [ ] Draft domain assignment table is complete (all 6 domains have at least one assigned or fallback candidate)
- [ ] Domains with no Tier A assignment are flagged — identify whether Tier B lead is viable or whether additional outreach is needed June 15 AM
- [ ] Mentorship pairings drafted for all Tier C assignments
- [ ] Split-domain eligibility confirmed or denied for all Tier A candidates

**Go/No-Go for June 15**:
- If 5–6 domains have confirmed or strongly-likely authors: proceed full June 15 selection session
- If 3–4 domains have confirmed authors, 1–2 pending: June 15 morning call-backs focus on pending domains; proceed with confirmed domains regardless
- If fewer than 3 domains have confirmed authors: activate Section 6 contingency (scope reduction + accelerated recruitment)

---

## June 15 — Morning Block (08:00–12:00 CDT)

### 08:00–09:30: Final Selection and Backup Planning

*Purpose*: Finalize domain assignments and confirm go/no-go for each domain.

**Per-domain go/no-go decision**:

```
FOR EACH DOMAIN (60-65):

  IF primary author confirmed AND rubric score ≥ 14 (Tier B+):
    → GO for this domain; include in June 20 launch

  IF primary author is Tier C only (score 6-13):
    → CONDITIONAL GO: project lead co-research support required
    → Scope reduced to 3,000–4,500 words
    → Weekly check-ins required
    → Flag for early (T+3) outline review before proceeding to production

  IF no confirmed author:
    → DOMAIN GAP: activate fallback options below
```

**Domain gap fallback options** (choose one, in this order):
1. **Activate next fallback candidate** from Section 8 of target list — send compressed outreach June 15 AM with same-day response request
2. **Defer domain to Wave 2** (late June): note in AUTHOR_ROSTER_JUNE_15.md that this domain is deferred; no impact on confirmed domains
3. **Reduce to 2-domain scope** for a split-domain Tier A author: if one Tier A has confirmed a single domain but is eligible and available for a second adjacent domain, offer split assignment
4. **Orchestrator self-execute**: project lead produces research brief outline + source library; contract a prose editor to complete narrative. Slowest option; use only if domains 1–3 are unavailable.

---

### 09:30–11:00: Backup Author Identification

*Purpose*: For each confirmed domain, name the backup author who could step in if the primary drops after June 20.

**Backup author criteria**:
- Must be already-contacted (on target list or referral from recruited authors)
- Must have received outreach or be identifiable from fallback list
- Must be flagged as "available if needed" — do not reach out cold for backup designation without prior contact

**Backup roster entry per domain**:
```
Domain ___: Primary — [NAME] (Tier ___, confirmed June ___) | Backup — [NAME] (Tier ___, status: CONTACTED/IDENTIFIED/NOT YET CONTACTED)
```

---

### 11:00–12:00: Resource Contention Check

*Purpose*: Confirm there is no resource conflict with Domain 51 user execution (noted as "light lift, no conflict expected" in project spec).

**Domain 51 check** (June 9 execution):
- Domain 51 is a stockbot-adjacent operational task; orchestrator capacity impact is minimal
- Phase 6 author matching session is research/coordination work, not infrastructure deployment
- Conclusion: no resource contention with Domain 51. Proceed without adjustment.

**June 20–30 stockbot expansion window** (from PHASE_6_WAVE_2_ACTIVATION_CHECKLIST.md):
- Stockbot expansion June 20–30 is a CAUTION/ROLLBACK window; orchestrator response target extends to 6 hours (from 4)
- Phase 6 Wave 1 author onboarding June 20 does not conflict; author communications are async
- No author contact should promise same-day orchestrator response; all communications state 6-hour response target June 20–27

---

## June 15 — Afternoon Block (13:00–17:00 CDT)

### 13:00–15:00: Offer Generation

*Purpose*: Generate a custom offer document for each confirmed author. This is the formal invitation with all details — domain assignment, research brief reference, timeline, payment schedule.

**Offer document structure** (one per confirmed author, send by 17:00 CDT June 15):

```
Subject: Phase 6 Domain [XX] — Confirmed Author Invitation + Brief

[CANDIDATE_NAME],

This is the formal confirmation of your invitation to author the Phase 6 Domain [XX] research brief for the Systems Resilience Project.

DOMAIN ASSIGNMENT: [DOMAIN_NUMBER] — [DOMAIN_NAME]
TIER ASSIGNMENT: [A / B / C]
START DATE: June 20, 2026
COMMITMENT: [8 / 4-6 / 2-4] hours per week, 8 weeks
WORD TARGET: [8,000-10,000 / 7,000-9,000 / 3,000-4,500] words

TIMELINE:
- June 20 (T+0): Kickoff. Onboarding kit sent. Post acknowledgment in Matrix domain room.
- June 23 (T+3): Outline due (H2/H3 structure + section purpose notes).
- June 27 (T+7): Non-negotiable first-draft checkpoint — 50% draft with all headings and Sections 1-2 narrative-complete.
- July 2 (T+12): Full first draft.
- July 5 (T+15): Final publication-ready draft (post peer review).

PAYMENT:
- Milestone 1: Outline approval, June 23 — [FIRST_PAYMENT_AMOUNT]
- Milestone 2: Final draft accepted, July 5 — [SECOND_PAYMENT_AMOUNT]
Payment via [PAYMENT_METHOD]. Please confirm payment details by June 18.

ATTACHED:
- Research Brief: RESEARCH_BRIEF_DOMAIN_[XX].md (scope, research questions, deliverable format)
- Onboarding Kit: Platform access, source library location, peer reviewer contact
- Timeline Card: Key dates and checkpoints

Next step: Reply to confirm receipt and confirm payment method by June 18.

[SENDER_NAME]
[SENDER_EMAIL]
```

---

### 15:00–16:30: Timeline Confirmation

*Purpose*: For each confirmed domain, verify the research brief deliverable date (July 5 per Wave 1 plan) is achievable given the author's confirmed availability.

**Timeline viability check**:
```
Tier A author, 8 hrs/week, June 20 start:
  T+3 outline → T+7 50% draft → T+12 full draft → T+15 final
  → Viable for July 5 gate IF June 20 start is confirmed

Tier B author, 4-6 hrs/week, June 20 start:
  T+3 outline → T+7 50% draft checkpoint (may not be 50% — escalate if less than 30%)
  → Viable with T+3 check-in added; project lead reviews outline before production
  → July 5 gate is achievable; not 100% certain without T+7 check

Tier C author, 2-4 hrs/week, June 20 start:
  Reduced scope (3,000-4,500 words); T+5 progress check added
  → July 5 gate may shift to July 11-12 for Tier C authors
  → Flag any Tier C domain assignment: July 5 is a conditional gate, not hard
```

---

### 16:30–17:00: June 15 Go/No-Go Decision

*Purpose*: Final gate before Phase 6 Wave 1 is committed.

**Go/No-Go criteria for Phase 6 Wave 1 launch (June 20)**:

| Criterion | Go | No-Go |
|-----------|-----|-------|
| Authors confirmed for 5–6 domains | ≥ 5 domains have confirmed author | ≤ 3 domains confirmed; activate contingency |
| Tier A coverage | ≥ 3 Tier A authors confirmed | 0–1 Tier A confirmed; assess scope reduction |
| No domain has only Tier C | All domains either Tier A/B or Tier C with mentor | A domain has Tier C with no mentor identified |
| Backup authors identified | ≥ 4 of 6 domains have named backup | ≤ 2 domains have backup authors |
| Payment terms confirmed | ≥ 4 authors have confirmed payment method | No author has confirmed payment method |
| Timeline viability | ≥ 4 domains viable for July 5 gate | Fewer than 3 domains viable for July 5 |

**Decision tree output**:

```
IF all criteria = GO:
  → Phase 6 Wave 1 launches June 20, full scope (6 domains)
  → Generate AUTHOR_ROSTER_JUNE_15.md and commit to repo

IF 4-5 criteria = GO (1-2 borderline):
  → Phase 6 Wave 1 launches June 20 with explicit risk note
  → Borderline criteria flagged in ORCHESTRATOR_STATE.md
  → Contingency for lagging domain activated (see Section 6)

IF fewer than 4 criteria = GO:
  → Do NOT launch June 20 at full scope
  → Activate deferred-domain path: launch with 3-4 strongest domains June 20
  → Continue recruitment June 16-19 for remaining domains
  → Late start (June 25) for lagging domains acceptable with July 5 gate extended to July 12
```

---

## Section 6: Contingency Plans

### Contingency A: Recruitment Lags — Fewer Than 4 Confirmed Authors by June 15

**Detection**: June 14 morning assessment shows fewer than 4 confirmations.

**Response**:
1. **Defer 1 domain to Wave 2 (late June)**: Choose the domain with lowest source readiness (Domain 60 or 62 per difficulty modifier). Document in ORCHESTRATOR_STATE.md that this domain is Wave 2 not Wave 1. No disruption to other domains.
2. **Accelerate 1 domain for early start**: If one domain has a Tier A author with high confidence, offer a June 17 soft start (2 days early) to bank research time before others launch. Only applicable if June 17 start is genuinely additive.
3. **Reduce scope**: Instead of 6 domains at 8,000–10,000 words each, launch 4 domains at full scope. Document scope reduction in AUTHOR_ROSTER_JUNE_15.md.

### Contingency B: Tier A Author Drops After June 20 (Mid-Sprint)

**Detection**: Author silent in Matrix for 48+ hours, or explicit withdrawal.

**Response sequence** (complete within 24 hours):
1. Contact author via email and Matrix DM — confirm withdrawal vs. technical issue.
2. If withdrawn: assess draft state. If T+3 outline complete → reassign to backup author (Section 8 of target list or referral from other confirmed authors). If no outline → project lead produces outline; backup author starts from outline rather than blank page.
3. If technical issue → troubleshoot access same day; follow DEPLOYMENT_PLAYBOOK_NEXTCLOUD_MATRIX.md access recovery.
4. Notify remaining authors: brief message in general channel ("One domain is being re-assigned; no impact on your track").

### Contingency C: Domain Has No Eligible Author at Any Tier

**Detection**: Algorithm run June 14 afternoon shows no candidate with D1 ≥ 3 AND D5 ≥ 3 for a specific domain.

**Response**:
1. Pull from fallback list (Section 8 of target list) and assess fallback against the same eligibility screen.
2. If fallback also ineligible: assign most-proximate Tier B or Tier C author with explicit project lead co-research support (project lead conducts 3–5 background research sessions to pre-build the source foundation; author produces narrative from pre-built materials).
3. If co-research path is not feasible (project lead bandwidth insufficient): defer domain to Wave 2. Document decision.

---

## Section 7: Post-Matching Outputs

### AUTHOR_ROSTER_JUNE_15.md — Required Post-Session Deliverable

Commit to `projects/systems-resilience/phase-6/` by June 15 17:00 CDT.

**File content**:

```yaml
---
title: "Phase 6 Wave 1 Author Roster — June 15, 2026"
status: CONFIRMED
generated: 2026-06-15
phase_6_wave_1_launch: 2026-06-20
---
```

```
DOMAIN ASSIGNMENTS — WAVE 1

Domain 60 — International Coordination
  Primary Author: [NAME]
  Tier: [A/B/C]
  Rubric Score: [X]/25
  Start Date: June 20
  Confirmed: [YES/CONDITIONAL]
  Backup Author: [NAME]
  Payment Terms Confirmed: [YES/NO]

Domain 61 — Intergenerational Knowledge Transmission
  [same fields]

Domain 62 — Infrastructure Interdependencies
  [same fields]

Domain 63 — Ecosystem Restoration
  [same fields]

Domain 64 — Community Economic Resilience
  [same fields]

Domain 65 — Institutional Learning and Governance Scaling
  [same fields]

MENTORSHIP PAIRINGS
  [Tier C Author] ↔ [Tier A/B Mentor] (Domain [XX])

DEFERRED DOMAINS (if any)
  Domain [XX]: deferred to [date]; reason: [BRIEF NOTE]

JUNE 15 GO/NO-GO DECISION
  Decision: GO / CONDITIONAL GO / REDUCED SCOPE LAUNCH
  Notes: [any flagged risks]
  Phase 6 Wave 1 Launch: June 20, 2026 — CONFIRMED / MODIFIED
```

---

## Session Timing Summary

| Block | Date | Time (CDT) | Activity |
|-------|------|-----------|---------|
| Pre-session | June 13 EOD | — | Verify tracking sheet, reply pool, fallback contacts |
| Call-backs | June 14 | 08:00–09:00 | Final Tier A confirmations |
| Non-respondents | June 14 | 09:00–10:00 | Fallback activation decisions |
| Rubric application | June 14 | 10:00–12:00 | Score all confirmed candidates |
| Matching algorithm | June 14 | 13:00–15:30 | Domain assignments computed |
| Draft table | June 14 | 15:30–17:00 | First-pass assignment table |
| Mentorship pairings | June 14 | 17:00–18:30 | Tier C pairings confirmed |
| EOD assessment | June 14 | 18:30–20:00 | Go/no-go for June 15 session |
| Final selection | June 15 | 08:00–09:30 | Per-domain go/no-go decisions |
| Backup planning | June 15 | 09:30–11:00 | Backup roster finalized |
| Resource check | June 15 | 11:00–12:00 | Domain 51 + stockbot contention check |
| Offer generation | June 15 | 13:00–15:00 | Offer documents sent to all confirmed authors |
| Timeline confirm | June 15 | 15:00–16:30 | Viability check per tier |
| Final go/no-go | June 15 | 16:30–17:00 | Phase 6 Wave 1 launch decision |
| Roster commit | June 15 | 17:00 | AUTHOR_ROSTER_JUNE_15.md committed |

---

*Runbook Version 1.0 — Phase 6 Wave 1 — Prepared June 10, 2026 (Item 69). Execute June 14 08:00 CDT. Post-session output: AUTHOR_ROSTER_JUNE_15.md committed to projects/systems-resilience/phase-6/ by June 15 17:00 CDT.*
