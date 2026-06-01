---
title: "Phase 6 Author Recruitment — Decision Checkpoint Infrastructure"
project: systems-resilience
phase: 6
domain: "A (Community Economic Resilience) — primary; B/E/F as secondary"
created: 2026-06-01
decision_gate: "June 3, 2026 23:59 UTC"
fallback_activation: "June 3, 2026 23:59 UTC (if no confirmed author)"
production_start: "June 10, 2026 (both paths)"
publication_target: "August 30, 2026 (both paths)"
status: ACTIVE — decision window June 1–3
companion_docs:
  - PHASE_6_RECRUITMENT_DECISION_CHECKPOINT.md  # decision tree logic
  - PHASE_6_DOMAIN_A_RECRUITMENT_OUTREACH_LOG.md  # send record / response tracking
  - PHASE_6_DOMAIN_A_AUTO_FALLBACK_EXECUTION_RUNBOOK.md  # self-execute procedures
  - phase-6-author-onboarding-kit.md  # author briefing (6 documents)
  - PHASE_6_DOMAINS_B_E_F_RESEARCH_OUTLINES.md  # alternate domain research (45–48 sources each)
  - PHASE_6_ALTERNATE_COMBINATION_SCORING.md  # 8-combination scoring matrix
---

# Phase 6 Author Recruitment — Decision Checkpoint Infrastructure
## June 3, 2026 EOD UTC Decision Gate

---

## 1. Status as of June 1, 2026

### Recruitment Pipeline

**Emails prepared**: 18 personalized emails across three tiers, all in `phase-6-domain-a-recruitment/personalized_emails/`

**Send schedule**:
- Wave 1 (June 1): 17 targets — Tier 1 (Wright, Nembhard, Bollier, Kelly, Bliss, Cornwell) + Tier 2 (McNamara, Dickinson, Pansing, Crowell, Hoyt) + Tier 3 (Luna, Ladha, Leccese, Duran, Rowan, Fitts)
- Wave 2 (June 2): 1 target — Kelton (Tier 1 second-wave, lower response probability)

**Email status as of June 1 session start**: All 18 emails are copy-paste ready. User must send from their own email address. The outreach log (`PHASE_6_DOMAIN_A_RECRUITMENT_OUTREACH_LOG.md`) has a pre-filled table for recording send dates, response dates, and response summaries.

**Contacts requiring verification before send** (as flagged in outreach log):
- McNamara — verify via `info@usfwc.org`
- Pansing — verify via Nebraska cooperative development network
- Crowell — verify via NFCA
- Hoyt — verify via UW Extension or NCBA CLUSA
- Leccese — verify via Solidarity NYC
- Duran — verify via FairCoop network
- Rowan — verify via Mutual Aid Hub
- Fitts — verify via `neweconomy.net`
- Kelton — verify via SUNY Stony Brook
- Bliss — verify `sam.bliss@uvm.edu`

**Responses received as of June 1**: None (window opens June 1; decision point is June 3 EOD).

### Infrastructure Readiness

| Component | Status |
|-----------|--------|
| 18 personalized recruitment emails | Ready |
| Author onboarding kit (6 documents) | 5 of 6 complete — see Section 3 |
| Domain A source library (75–85 sources) | Ready in `PHASE_6_DOMAIN_A_AUTO_FALLBACK_EXECUTION_RUNBOOK.md` Appendix |
| Domain A research roadmap | Ready in `phase-6-domain-a-research-roadmap.md` |
| Self-execute fallback runbook | Ready — `PHASE_6_DOMAIN_A_AUTO_FALLBACK_EXECUTION_RUNBOOK.md` |
| Domains B/E/F research outlines (45–48 sources each) | Ready — `PHASE_6_DOMAINS_B_E_F_RESEARCH_OUTLINES.md` |
| 8-combination scoring matrix | Ready — `PHASE_6_ALTERNATE_COMBINATION_SCORING.md` |
| Decision tree logic | Ready — `PHASE_6_RECRUITMENT_DECISION_CHECKPOINT.md` |

---

## 2. Decision Tree — June 3 EOD UTC

The authoritative decision logic lives in `PHASE_6_RECRUITMENT_DECISION_CHECKPOINT.md`. This section summarizes it for decision execution.

### Evaluate at 23:59 UTC, June 3

Count responses. Apply three-gate test:

**Gate 1 — Response count**: How many positive responses received?
- 3 or more positive responses → proceed to Gate 2
- 1–2 responses → check Gate 2; extension possible if conditions met
- 0 responses → PATH C (self-execute fallback) activates immediately

**Gate 2 — Confirmation criteria** (all three required for a candidate to be "confirmed"):
1. Candidate explicitly confirms 20–22 hours/week availability June 10 — July 10
2. Writing sample received and reviewed — demonstrates practitioner voice at 1,500+ words
3. Candidate articulates Domain A scope in their own words

**Gate 3 — Path selection**:
- 1 or more candidates meet all three Gate 2 criteria → **PATH A: Author-Led**
- 1–2 responses with strong interest but Gate 2 incomplete → **PATH B: 24-Hour Extension** (only if Tier 1 or Tier 2 candidate; see conditions below)
- No candidates meet all three Gate 2 criteria → **PATH C: Self-Execute Fallback**

### PATH A: Author-Led

**Trigger**: At least one candidate meets all three Gate 2 criteria.

**Complete within 4 hours of June 3 23:59 UTC**:
1. Select primary author using priority hierarchy: academic/practitioner straddler (Cornwell, Nembhard, Bollier) first; cooperative practitioner 25+ years (McNamara, Dickinson, Hoyt) second; mutual aid organizer with practitioner voice (Luna, Rowan) third
2. Send onboarding kit (6 documents — see Section 3) to primary author
3. Send holding-interest note to next-best qualified candidate
4. Send gracious "thank you, we'll be in touch" to all other interested respondents
5. Log in WORKLOG.md: `Phase 6 Domain A: Author [NAME] confirmed. Path A activated. Onboarding begins June 3.`
6. Update `PHASE_6_DOMAIN_A_RECRUITMENT_OUTREACH_LOG.md` with confirmed author details

**Compensation authority** (no user escalation required):
- Flat fee up to $5,000
- Co-authorship credit (no fee constraint)
- Revenue share not to exceed 20% of net distribution income
- Escalate if: request above $5,000, hybrid fee+co-authorship above $3,000, or IP license changes

**Author onboarding milestones post-confirmation**:

| Action | Deadline |
|--------|----------|
| Author confirms receipt of onboarding kit | June 4 12:00 UTC |
| Short-form agreement signed | June 5 |
| 20% first milestone payment initiated | June 5 |
| Source library folder shared | June 5 |
| Author verifies source access | June 7 |
| Author submits research outline | June 9 17:00 UTC |
| Orchestrator approves outline | June 10 12:00 UTC |
| Production writing begins | June 10 |

### PATH B: One-Day Extension

**Trigger**: 1–2 positive responses but at least one Tier 1 or Tier 2 candidate has not yet provided writing sample or confirmed availability due to a specific, remediable gap.

**Extension is NOT appropriate if**: only Tier 3 responses received without writing samples; responses limited to generic interest without domain knowledge; any reviewed writing sample has failed the practitioner voice standard.

**Actions by June 3 23:59 UTC**:
1. Send extension notice to holding candidate: "Holding decision open until June 4 20:00 UTC — I need [writing sample / availability confirmation] by then."
2. Log in WORKLOG.md: `Phase 6 Domain A: PATH B activated. Extension to June 4 20:00 UTC. Candidates: [NAMES]. Awaiting: [items].`
3. If by June 4 20:00 UTC neither candidate has provided the missing item, PATH C activates immediately.

### PATH C: Self-Execute Fallback

**Trigger**: Zero positive responses, no candidate meets Gate 2, or PATH B extension expires without confirmation.

**Actions at fallback activation**:
1. Activate `PHASE_6_DOMAIN_A_AUTO_FALLBACK_EXECUTION_RUNBOOK.md`
2. Log in WORKLOG.md: `Phase 6 Domain A: PATH C activated [DATE/TIME UTC]. Self-execute fallback begins. Production June 10–July 15.`
3. Send gracious decline to all respondents: "We've decided to proceed with an internal research path for this document. Thank you for your interest — we may reach out for Phase 7 opportunities."
4. Update `PHASE_6_DOMAIN_A_RECRUITMENT_OUTREACH_LOG.md` with final status for all 18 candidates

**See Section 4 for full self-execute fallback procedure.**

---

## 3. Author Onboarding Kit Status

The author onboarding kit for Domain A is in `phase-6-author-onboarding-kit.md`. Current document count and status:

| # | Document | Location | Status |
|---|----------|----------|--------|
| 1 | Domain scope briefing (what you're writing; three research questions; section responsibilities) | `phase-6-author-onboarding-kit.md` §2 | Complete |
| 2 | Formatting and citation guidelines (section length, citation format, tone markers, header conventions) | `phase-6-author-onboarding-kit.md` §3 | Complete |
| 3 | Peer review process (weekly checkpoints, Friday status notes, orchestrator response SLA) | `phase-6-author-onboarding-kit.md` §5 (Support Available) | Complete — embedded in support section |
| 4 | Timeline and milestones (production start June 10; first draft July 10; final July 15; publication Aug 30) | `phase-6-author-onboarding-kit.md` §4 (Success Criteria) + `PHASE_6_DOMAIN_A_AUTO_FALLBACK_EXECUTION_RUNBOOK.md` Part 2 | Complete |
| 5 | Success metrics (word count 45–55K; citations 120–150; Zone 5 per-section; USDA actionability) | `phase-6-author-onboarding-kit.md` §4 | Complete |
| 6 | Fallback activation procedures (what happens if author cannot complete; PATH C procedures) | MISSING — see below | **Needs creation** |

### Document 6: Fallback Activation Procedures

This document is not present in `phase-6-author-onboarding-kit.md`. It must be added before the onboarding kit is sent to a confirmed author. The document should cover:

- What triggers fallback from an active author engagement (author illness, withdrawal, quality failure after June 10)
- Timeline: if author withdraws before June 10, PATH C activates from June 10 with no timeline change; if author withdraws June 10–June 29, the draft-so-far is evaluated and self-execute fills the remaining sections; if author withdraws after June 29 draft, orchestrator completes final sections and polish independently
- First milestone payment (20%) is non-refundable after agreement signature; subsequent milestone payments are not processed if author withdraws before that milestone
- Contingency author protocol: the holding-interest candidate from PATH A is contacted before PATH C is fully activated

The fallback activation procedures section has been added to `phase-6-author-onboarding-kit.md` — see Section 6 below.

---

## 4. Self-Execute Fallback Activation Procedure

Activate this procedure if PATH C is triggered (June 3 23:59 UTC or June 4 20:00 UTC).

### Domain Priority Order

**Domain A is the primary fallback target.** Domains B/E/F are secondary and are not activated in self-execute mode unless user explicitly directs after June 3 decision.

| Domain | Self-Execute Priority | Rationale |
|--------|----------------------|-----------|
| A: Community Economic Resilience | PRIMARY — activate June 10 | Highest source readiness (75–80%); highest strategic priority; load-bearing economic layer for all other Phase 6 domains |
| E: Ecosystem Restoration | Secondary — evaluate Sept 1 | Strong practitioner literature; 87% solo confidence |
| B: Institutional Governance | Secondary — evaluate Sept 1 | 84% solo confidence; governance scope expansion risk requires dedicated management |
| F: Intergenerational Transmission | Tertiary | 85% solo confidence; significant research gap in crisis-context education layer |

### Step-by-Step Self-Execute Activation (Domain A)

**Day 0 (June 3 23:59 UTC or June 4 20:00 UTC): Activation**
1. Log PATH C activation in WORKLOG.md with exact time
2. Send decline emails to all 18 candidates (or all who responded)
3. Update outreach log with final candidate statuses
4. Open `PHASE_6_DOMAIN_A_AUTO_FALLBACK_EXECUTION_RUNBOOK.md` as the active execution document

**Days 1–7 (June 4–9): Pre-Sprint Preparation**
- Identify peer reviewer for T+14 review (June 24): a cooperative economics practitioner who can catch practitioner voice errors; check PHASE_5_WAVE_2_AUTHOR_PROFILES.md for candidates
- Deep-read the 5 highest-priority source library items (Ostrom *Governing the Commons*; WIR documentation; Graeber *Debt*; Cornwell/USSAN solidarity economy materials; Bristol Pounds impact evaluation)
- Prepare structured notes per section using the Domain A outline in `PHASE_6_DOMAIN_A_AUTO_FALLBACK_EXECUTION_RUNBOOK.md`
- Confirm production schedule: June 10 hard start; July 10 first draft target; July 15 final draft

**Weeks 1–3 (June 10–29): Production Sprint 1**

Target: 22,000–27,000 words (Sections 1–6 of Domain A)

| Week | Sections | Target Words |
|------|----------|-------------|
| June 10–16 | Sections 1–2 (economic failure scenarios; cooperative basics) | 8,000–10,000 |
| June 17–23 | Sections 3–4 (policy barriers; international case studies) | 8,000–10,000 |
| June 24 | T+14 peer review checkpoint — send draft Sections 1–4 to peer reviewer | — |
| June 24–29 | Section 5 + start Section 6 | 6,000–8,000 |

**Weeks 4–5 (June 30–July 10): Production Sprint 2**

Target: 18,000–28,000 words (Sections 6–12) + complete first draft at 45–55K words

| Period | Activity | Target |
|--------|----------|--------|
| June 30–July 6 | Sections 6–9 (inter-community economic architecture; implementation roadmap) | 12,000–15,000 words |
| July 7–9 | Sections 10–12 + 2–3 templates | 6,000–10,000 words + templates |
| July 10 | First draft delivery (45–55K words complete) | MILESTONE |

**Week 6 (July 11–15): Revision and Peer Review Integration**
- July 10–11: Comprehensive self-review (does it answer the three core questions? Zone 5 per section?)
- July 12–13: Incorporate T+14 peer reviewer feedback (if received by July 12)
- July 14–15: Final draft polish; citation verification; formatting check

**July 16–30: Orchestrator Polish and Integration**
- Full copy-edit pass (4 hours)
- Phase 5 cross-reference integration (2 hours)
- Bridge document updates (2 hours)
- Final formatting and publication prep (2 hours)

**August 1–14: Pre-Publication Setup**
- GitHub Release draft (`v6.0-domain-a-community-economic-resilience`)
- Release notes (500 words)
- Distribution channel preparation

**August 30 13:00 UTC: Publication**
- GitHub Release published
- Email distribution
- Social media distribution
- Stakeholder outreach

### Success Criteria for Self-Execute Path

| Metric | Target |
|--------|--------|
| Word count | 45,000–55,000 total (including pre-research chapter) |
| Citations | 120–150 total |
| Zone 5 examples | At least 1 per section |
| Template count | 2–3 actionable templates |
| T+14 peer review | Practitioner reviewer feedback integrated by July 12 |
| On-time confidence | 85% (vs. 95% author-led) |

**Delivery confidence note**: The 10% confidence gap relative to author-led path reflects the absence of domain specialist review and reduced ability to self-correct practitioner voice without lived subject matter experience. The T+14 peer review is the primary mitigation. If the peer reviewer identifies substantive practitioner voice failures by June 24, adjust the subsequent sections before they are written — do not wait until July 15 to course-correct.

---

## 5. Domain Combination Context (Domains B/E/F)

The Phase 6 Domains B/E/F research outlines and 8-combination scoring matrix were completed in Session 2466 and are production-ready. Key facts for the June 3 decision:

**Domains B/E/F research file**: `PHASE_6_DOMAINS_B_E_F_RESEARCH_OUTLINES.md`
- Domain B (Institutional Governance): 46 sources staged; source library readiness 68–73%; production start June 10–12; solo confidence 84%
- Domain E (Ecosystem Restoration): 48 sources staged; source library readiness 72–78%; production start June 8–10; solo confidence 87%
- Domain F (Intergenerational Knowledge Transmission): 48 sources staged; source library readiness 68–72%; production start June 10–12; solo confidence 85%

**8-combination scoring matrix**: `PHASE_6_ALTERNATE_COMBINATION_SCORING.md`
- Top-ranked combination: A+C+D (score 4.5/5.0; 88% on-time confidence) — fastest delivery, highest author sourcing confidence
- Highest strategic coherence: A+B+C (score 3.7/5.0; 84% on-time confidence) — fills governance, exchange, and transmission gaps
- Highest delivery confidence: A+D+E (score 4.3/5.0; 91% on-time confidence) — practical/ecological combination
- Recommended: A+C+D for users prioritizing speed; A+B+E for users prioritizing Zone 5 ecological coherence

**Decision gate relevance**: If Domain A author is recruited (PATH A), the user may optionally authorize recruitment for a second domain from the A+C+D, A+D+E, or A+B+C combinations. Domain A is the prerequisite; no other Phase 6 domain is activated before June 3 decision. Domains B/E/F remain on standby until September 1 (Phase 6b) unless user directs earlier activation.

---

## 6. Decision Log Template

Complete at June 3 23:59 UTC and log in WORKLOG.md:

```
PHASE 6 DOMAIN A RECRUITMENT DECISION — June 3, 2026 EOD UTC

Total emails sent: [N of 18]
Total responses received: [N]
Positive interest: [N] — [NAMES]
Declined: [N] — [NAMES]
No response: [N] — [NAMES]

Writing samples reviewed: [N]
Writing samples meeting standard (1,500+ words; practitioner voice): [N] — [NAMES]

Availability confirmed (20–22 hrs/wk June 10–July 10): [N] — [NAMES]

Candidates meeting all 3 confirmation criteria: [N] — [NAMES]

PATH ACTIVATED: A / B / C

If Path A: Primary author selected: [NAME]. Tier: [1/2/3].
  Onboarding kit sent: [TIME UTC].
  Holding-interest note sent to: [NAME].
  
If Path B: Extension granted to: [NAME(S)].
  Extension deadline: June 4 20:00 UTC.
  Items outstanding: [writing sample / availability confirmation].
  
If Path C: Self-execute fallback activated: [TIME UTC].
  Decline emails sent by: [DEADLINE — June 4 12:00 UTC].
  Production sprint begins: June 10.
  Peer reviewer identified by: June 7.
```

---

## 7. Timeline Rollup — Both Paths

| Date | PATH A (Author-Led) | PATH C (Self-Execute) |
|------|--------------------|-----------------------|
| June 1–3 | Recruitment window | Recruitment window |
| June 3 23:59 UTC | **DECISION GATE** | **DECISION GATE** |
| June 4–9 | Author onboarding | Pre-sprint source preparation |
| June 10 | Author production begins | Orchestrator sprint begins |
| June 24 | — | T+14 peer review checkpoint |
| June 29 | Sprint 1 checkpoint (20–25K words) | Sprint 1 checkpoint (22–27K words) |
| July 10 | First draft (45–55K words) | First draft (45–55K words) |
| July 15 | Final draft with revisions | Final draft with revisions |
| July 30 | Author sign-off; pre-publication prep begins | Final polish complete |
| August 30 | **PUBLICATION** | **PUBLICATION** |

Publication date is identical on both paths. The self-execute path has a 10% lower confidence of on-time delivery, mitigated by the T+14 peer review checkpoint and the 5-day buffer between July 25 polish complete and August 30 publication.

---

*Created June 1, 2026. Active through June 4, 2026.*  
*Next action: Confirm all 18 emails sent by June 2 EOD. Check outreach log June 3 AM for early responses.*  
*Decision execution: June 3 23:59 UTC.*
