---
title: "Phase 6 Domain A — Recruitment Decision Checkpoint"
project: systems-resilience
phase: 6
domain: "A (Community Economic Resilience)"
created: 2026-06-01
decision_deadline: "June 3, 2026 EOD UTC (23:59 UTC)"
extension_option: "June 4, 2026 (24-hour extension — specific conditions required)"
fallback_activation: "June 3, 2026 23:59 UTC (if no author confirmed)"
---

# Phase 6 Domain A — Recruitment Decision Checkpoint
## June 3, 2026 EOD UTC

---

## Overview

This document is the authoritative decision tree for the June 3, 2026 author recruitment decision. The orchestrator evaluates the response state at EOD June 3 UTC and executes one of three paths. No exceptions to this timeline without explicit user authorization.

**Timeline context**:
- June 1–2: Recruitment emails sent (18 targets across 3 tiers)
- June 3 EOD UTC: Decision point — author confirmed, extended, or fallback activated
- June 4–9: Onboarding window (if author confirmed or extended)
- June 10: Production start (author-led or self-execute)
- July 10: First draft deadline (same regardless of path)
- August 30: Publication target (same regardless of path)

---

## Decision Tree — June 3 EOD UTC

Evaluate responses received as of June 3, 23:59 UTC. Apply the following logic in order:

---

### PATH A: Author-Led (Proceed with Confirmed Author)

**Trigger**: 3 or more positive responses received AND at least 1 candidate meets all three confirmation criteria

**Three confirmation criteria** (all required for confirmation):
1. Candidate explicitly confirms 20–22 hours/week availability June 10 — July 10
2. Writing sample received and reviewed — demonstrates practitioner voice at 1,500+ words
3. Candidate articulates Domain A scope in their own words (confirms they understand what they're writing)

**Immediate actions (June 3 — complete within 4 hours of EOD)**:

1. Select primary author from confirmed candidates using the selection hierarchy below
2. Send onboarding kit to primary author (6 documents — see PHASE_6_AUTHOR_RECRUITMENT_TRACKING.md)
3. Send "thank you, we'll be in touch" to all other respondents who expressed interest (do not burn these contacts — they may be reviewers or Phase 7 authors)
4. Log decision in WORKLOG.md: "Phase 6 Domain A: Author [NAME] confirmed. Path A activated. Onboarding begins June 3."
5. Update PHASE_6_AUTHOR_RECRUITMENT_TRACKING.md with confirmed author details
6. Send onboarding briefing email (from PHASE_6_AUTHOR_ONBOARDING_KIT.md) to confirmed author

**Primary author selection hierarchy** (when multiple candidates qualify):
- Priority 1: Academic/practitioner straddler with both theoretical grounding and practitioner writing voice (e.g., Cornwell, Nembhard, Bollier)
- Priority 2: Cooperative practitioner with 25+ years direct experience and documented writing (e.g., McNamara, Dickinson, Hoyt)
- Priority 3: Mutual aid organizer with contemporary experience and strong practitioner voice (e.g., Luna, Rowan)
- Tiebreaker: Zone 5 geographic proximity and agricultural cooperative experience weight toward higher priority

**Backup author protocol**: If primary author selected, also send a "holding interest" note to the second-best qualified candidate — do not formally recruit them, but keep the channel open in case primary author drops out before June 10.

---

### PATH B: One-Day Extension (June 4 EOD UTC)

**Trigger**: 1–2 positive responses received BUT at least 1 candidate has not yet provided writing sample OR has not confirmed exact availability

**Extension conditions** (at least one of the following must be true):
- A high-priority candidate (Tier 1 Academic or Tier 2 Cooperative Practitioner) has expressed strong interest but requests 24 hours to confirm availability or send writing sample
- A candidate has provided a strong writing sample but not yet confirmed availability due to timezone or scheduling delay
- 2+ candidates are in active negotiation on compensation terms and both have confirmed domain knowledge and writing capacity

**Extension is NOT appropriate if**:
- Only Tier 3 (mutual aid) candidates have responded and none have provided writing samples
- Responses are limited to generic "sounds interesting, tell me more" without specifics
- No candidate has confirmed they understand Domain A scope
- Any candidate's writing sample has been reviewed and does not meet practitioner voice standard

**June 4 extension actions**:
1. Send a follow-up note to the 1–2 interested candidates: "We're holding the decision open until June 4 EOD UTC. I need [writing sample / availability confirmation] by then to move forward."
2. Log extension decision in WORKLOG.md: "Phase 6 Domain A: PATH B activated. June 4 extension. Candidates holding: [NAMES]. Awaiting: [specific items]."
3. Set a calendar reminder for June 4, 20:00 UTC — hard cutoff for extended response
4. If by June 4 20:00 UTC neither candidate has provided the missing confirmation, activate PATH C (self-execute fallback) immediately

---

### PATH C: Self-Execute Fallback

**Trigger**: One of the following conditions:
- Zero positive responses received by June 3 EOD UTC
- Responses received but no candidate meets confirmation criteria (enthusiasm without availability or writing sample quality)
- PATH B extension expires (June 4 20:00 UTC) without candidate confirmation
- Writing samples received from all interested candidates, none meet practitioner voice standard

**Immediate actions (June 3 23:59 UTC or June 4 20:00 UTC)**:

1. Activate PHASE_6_DOMAIN_A_AUTO_FALLBACK_EXECUTION_RUNBOOK.md
2. Log fallback activation in WORKLOG.md: "Phase 6 Domain A: PATH C activated [DATE/TIME UTC]. Self-execute fallback begins. Orchestrator-led production June 10 — July 15."
3. Send gracious decline to all candidates who responded (even if unsuitable): "We've decided to proceed with an internal research path for this document. Thank you for your interest — we may reach out for Phase 7 opportunities."
4. Update PHASE_6_AUTHOR_RECRUITMENT_TRACKING.md: mark all candidates with final status
5. Proceed with fallback timeline (see below)

**Self-execute fallback timeline** (from PHASE_6_DOMAIN_A_AUTO_FALLBACK_EXECUTION_RUNBOOK.md):
- June 10 — July 15: Orchestrator autonomous development sprint (5-week window)
- July 10: First draft delivery (45–55K words, all 10–12 sections)
- July 15: Final draft with feedback incorporation
- August 1–14: Preparation for August 30 publication
- August 30: Publication (same date as author-led path — no slippage)

**Fallback confidence**: 85% on-time delivery (vs. 95% with dedicated author). The 10% confidence reduction reflects absence of domain specialist review and reduced ability to course-correct on practitioner voice without an author who has lived the subject matter. Mitigation: peer review at T+14 (June 24) by a cooperative economics practitioner to catch practitioner voice errors before final draft.

---

## Writing Sample Quality Criteria

When reviewing writing samples from interested candidates, apply the following criteria:

**Pass (proceed to confirmation)**:
- Sample reads as practitioner documentation, not academic essay
- Concrete examples and case studies anchor every major claim
- Author distinguishes between what the evidence shows and what they're recommending (epistemic honesty)
- Writing is accessible to a community organizer without specialized economics training
- Sample is at least 1,500 words and demonstrates sustained argument structure, not just notes or bullets

**Conditional (request a different sample)**:
- Sample is academic in voice but candidate has separate evidence of non-academic writing
- Sample is strong but too short (800–1,500 words) — request a longer sample before confirming
- Sample is in a tangentially related domain (not community economics) but voice quality is strong — acceptable if candidate demonstrates domain knowledge in the response email

**Fail (do not proceed with this candidate)**:
- Sample reads as exclusively academic — no practitioner application, no concrete case studies
- Sample contains significant factual errors about cooperative economics or commons governance
- Sample is primarily opinion or advocacy without grounding in evidence
- Candidate cannot provide any writing sample at all

---

## Compensation Negotiation Authority

The orchestrator has authority to agree to any of the following without escalating to user decision:

- Option 1 (flat fee): Up to $5,000 total for Domain A (within the $3,000–5,000 range established in PHASE_6_AUTHOR_HIRING_AND_ONBOARDING_FRAMEWORK.md)
- Option 2 (co-authorship): Co-authorship credit — no fee constraint
- Option 3 (equity/revenue share): Revenue share from publication income — at orchestrator's discretion, not to exceed 20% of net distribution income

Escalate to user decision if:
- A candidate requests more than $5,000
- A candidate requests a hybrid that includes both a fee above $3,000 AND co-authorship credit (unusual combination — user should weigh in)
- A candidate requests changes to the intellectual property terms (CC BY-SA license)

---

## June 3 EOD UTC — Decision Log Template

Complete this section at EOD June 3 UTC and log in WORKLOG.md:

```
PHASE 6 DOMAIN A RECRUITMENT DECISION — June 3, 2026 EOD UTC

Total emails sent: [N]
Total responses received: [N]
Candidates with strong interest: [N] — [NAMES]
Candidates who declined: [N] — [NAMES]
No response: [N] — [NAMES]

Writing samples reviewed: [N]
Writing samples meeting practitioner voice standard: [N] — [NAMES]

Availability confirmed (20–22 hrs/wk June 10–July 10): [N] — [NAMES]

Candidates meeting all 3 confirmation criteria: [N] — [NAMES]

PATH ACTIVATED: A / B / C

If Path A: Primary author selected: [NAME]. Onboarding kit sent: [TIME UTC].
If Path B: Extension granted to: [NAME(S)]. Extension deadline: June 4 20:00 UTC.
If Path C: Self-execute fallback activated: [TIME UTC].
```

---

## Post-Decision Actions by Path

### After Path A Confirmation

| Action | Responsible | Deadline |
|--------|-------------|----------|
| Send onboarding kit (6 documents) | Orchestrator | June 3 — within 4 hours of decision |
| Author confirms receipt of onboarding kit | Author | June 4 12:00 UTC |
| Agreement signed (short-form) | Both parties | June 5 |
| 20% first milestone payment initiated | Orchestrator | June 5 |
| Source library folder shared with author | Orchestrator | June 5 |
| Author verifies source library access | Author | June 7 |
| Author submits research outline | Author | June 9 17:00 UTC |
| Orchestrator reviews and approves outline | Orchestrator | June 10 12:00 UTC |
| Production writing begins | Author | June 10 |

### After Path B Extension

| Action | Responsible | Deadline |
|--------|-------------|----------|
| Extension notice sent to candidate(s) | Orchestrator | June 3 23:59 UTC |
| Hard cutoff for candidate response | Author candidate | June 4 20:00 UTC |
| Path A or C decision (per June 4 response) | Orchestrator | June 4 20:30 UTC |

### After Path C Activation

| Action | Responsible | Deadline |
|--------|-------------|----------|
| Fallback activation logged in WORKLOG.md | Orchestrator | June 3 23:59 UTC or June 4 20:00 UTC |
| Decline emails sent to all respondents | Orchestrator | June 4 12:00 UTC |
| Fallback runbook opened and initiated | Orchestrator | June 4 |
| Production sprint begins | Orchestrator | June 10 |
| Peer reviewer identified for T+14 review | Orchestrator | June 7 |

---

## Contingency: Author Drops Out After Confirmation (June 3–9 Window)

If a confirmed author drops out after June 3 but before production begins (June 10):

1. Immediately activate PATH C (self-execute fallback) — the production timeline does not change; June 10 is the hard start
2. Review the candidate list for the next-best qualified candidate who expressed interest during June 1–3 — if they have not been formally declined, send the contingency outreach email (PHASE_6_AUTHOR_ONBOARDING_KIT.md, Appendix A)
3. If contingency candidate confirms within 48 hours, proceed with author-led path
4. If no contingency candidate available within 48 hours, proceed with self-execute fallback
5. First milestone payment (20%) is not processed until agreement is signed — no payment obligation if author drops out before signing

---

## Reference Documents

| Document | Location | Purpose |
|----------|----------|---------|
| Recruitment templates (A/B/C) | PHASE_6_AUTHOR_RECRUITMENT_TEMPLATES.md | Email templates used for outreach |
| Candidate contact list | phase-6-domain-a-recruitment/recruitment_targets.csv | Full pipeline with emails and angles |
| Personalized emails | phase-6-domain-a-recruitment/personalized_emails/ | 18 ready-to-send emails, one per candidate |
| Outreach tracking log | PHASE_6_DOMAIN_A_RECRUITMENT_OUTREACH_LOG.md | Send record and response tracking |
| Onboarding kit | PHASE_6_AUTHOR_ONBOARDING_KIT.md | Documents to send to confirmed author |
| Fallback runbook | PHASE_6_DOMAIN_A_AUTO_FALLBACK_EXECUTION_RUNBOOK.md | Self-execute fallback procedures |
| Hiring framework | PHASE_6_AUTHOR_HIRING_AND_ONBOARDING_FRAMEWORK.md | Qualification criteria and stage gates |
| Domain scope | PHASE_6_CANDIDATE_COMMUNITY_ECONOMIC_RESILIENCE.md | Research questions, scope, source library |

---

*Decision checkpoint active June 1 — June 4, 2026.*  
*Created: June 1, 2026.*  
*Author: Research Agent, Session 2026-06-01.*
