---
title: "Phase 6 Wave 1 Execution Checklist — T+0 to T+14"
project: systems-resilience
phase: 6
wave: 1
status: PRODUCTION-READY — activate June 1 06:00 UTC upon user scope confirmation
decision_deadline: 2026-05-31T23:59:00Z
activation_start: 2026-06-01T06:00:00Z
wave_end: 2026-06-15T23:59:00Z
created: 2026-05-27
companion_docs:
  - PHASE_6_AUTHOR_ONBOARDING_KIT.md
  - PHASE_6_COORDINATION_TEMPLATES.md
  - PHASE_6_ACTIVATION_READINESS_CHECKLIST.md
  - PHASE_6_FRAMEWORK_DEPENDENCY_MAP.md
  - PHASE_6_SCOPE_AND_READINESS.md
domains:
  - international-coordination
  - intergenerational-knowledge-transmission
  - infrastructure-interdependencies
  - ecosystem-restoration
  - economic-resilience
  - institutional-learning
---

# Phase 6 Wave 1 Execution Checklist
## T+0 to T+14 — June 1 06:00 UTC to June 15 23:59 UTC

> **Lead note**: This checklist is the orchestrator's ground-level guide for the first 14 days of Phase 6 Wave 1 execution. It assumes the user has confirmed domain selection by May 31 23:59 UTC. If fewer than all six domains are selected, skip the irrelevant domain rows but preserve all process gates — the timeline and decision structure apply identically to any subset of two or more domains.

---

## Pre-June-1 Readiness Gates (May 31 EOD)

All gates must be green before T+0 kickoff. Any red gate at May 31 23:00 UTC triggers the relevant contingency procedure in the Contingency Triggers section.

### Gate R-1: User Scope Decision (Due May 31 23:59 UTC)

- [ ] User has confirmed domain selection: all six, or specify subset
  - Domains in scope: international coordination / intergenerational transmission / infrastructure interdependencies / ecosystem restoration / economic resilience / institutional learning
  - Domains deferred: [user specifies]
- [ ] Sequencing confirmed: Wave 1 domains (D+0 to D+7 ramp) vs. Wave 2 domains (D+7 to D+14 ramp)
  - Default Wave 1 fast-track: economic resilience + infrastructure interdependencies (most independent of other domains)
  - Default Wave 1 secondary: international coordination + intergenerational transmission (some benefit from Wave 1 framing)
  - Default Wave 2 domains: ecosystem restoration + institutional learning (integrate most from earlier domain outputs)
- [ ] User has acknowledged the June 15 publication-readiness gate (T+14): research complete and peer-reviewed, not necessarily published
- [ ] Any out-of-scope constraints documented (topics not to include, audiences not to address, institutional framings to avoid)

**Responsible party**: Orchestrator confirms receipt and logs decision in ORCHESTRATOR_STATE.md

### Gate R-2: Author Roster Confirmed (Due May 31 18:00 UTC)

- [ ] All confirmed authors identified by domain assignment
- [ ] Each author has: confirmed availability June 1–15 (Wave 1), confirmed preferred communication channel, confirmed time zone
- [ ] For any domain without a confirmed author: self-execution path or contingency author identified (see Contingency Trigger CT-1)
- [ ] Author briefing email drafted (see PHASE_6_AUTHOR_ONBOARDING_KIT.md section 1) and ready to send June 1 06:01 UTC
- [ ] Payment terms agreed and first-milestone disbursement path confirmed (author must see payment confirmed on or before June 3)

**Responsible party**: Orchestrator verifies against author-outreach-tracking.md

### Gate R-3: Research Kit Assembly (Due May 31 16:00 UTC)

Per confirmed domain:

- [ ] Pre-research document exists and is committed to master (phase-6/ subdirectory)
- [ ] Source library staged: minimum 20 verified accessible URLs per domain, annotated in markdown table
- [ ] Phase 5 model documents identified for each domain (which Phase 5 document is the closest tonal/structural model the author should match)
- [ ] Cross-domain integration map reviewed: PHASE_6_FRAMEWORK_DEPENDENCY_MAP.md confirms which domains share terminology, which must align before writing begins
- [ ] Domain-specific out-of-scope boundary documented in one paragraph — what this document explicitly does not cover

**Responsible party**: Orchestrator confirms kit completeness per PHASE_6_AUTHOR_HIRING_AND_ONBOARDING_FRAMEWORK.md section 3

### Gate R-4: Infrastructure Check (Due May 31 14:00 UTC)

- [ ] Project directory structure confirmed: `projects/systems-resilience/phase-6/` contains one file per confirmed domain
- [ ] Git working tree is clean on master (no uncommitted changes to phase-6/ files)
- [ ] ORCHESTRATOR_STATE.md updated with Phase 6 Wave 1 activated status and domain list
- [ ] Peer reviewer roster identified: minimum one peer reviewer per domain (credentials, contact, response timeline expectation of T+10 to T+12)

---

## T+0: June 1 06:00 UTC — Wave 1 Kickoff

### 06:00–07:00 UTC: Orchestrator Pre-Flight

The first hour is orchestrator-only. Do not contact authors until the pre-flight checklist is complete.

- [ ] Read ORCHESTRATOR_STATE.md — confirm no blocking conditions have emerged overnight (Jetson status, stockbot health, any late-breaking scope changes)
- [ ] Confirm all R-1 through R-4 gates are green. If any gate is amber or red, execute the relevant contingency before author contact
- [ ] Log kickoff timestamp in WORKLOG.md: "Phase 6 Wave 1 activated T+0 June 1 06:00 UTC. Domains in scope: [list]. Authors confirmed: [count]. Author gaps: [count if any]."
- [ ] Verify: today's date matches the planned activation date. If activation has been deferred from June 1 for any reason, recalibrate all T+ references in this checklist by the number of days of deferral

### 07:00–09:00 UTC: Author Briefings Sent

Send the kickoff email (from PHASE_6_AUTHOR_ONBOARDING_KIT.md, Author Briefing Template) to each confirmed author simultaneously. Do not stagger unless you want staggered response times.

- [ ] Email sent to: [domain 1 author name] — domain: economic resilience
- [ ] Email sent to: [domain 2 author name] — domain: infrastructure interdependencies
- [ ] Email sent to: [domain 3 author name] — domain: international coordination
- [ ] Email sent to: [domain 4 author name] — domain: intergenerational transmission
- [ ] Email sent to: [domain 5 author name] — domain: ecosystem restoration
- [ ] Email sent to: [domain 6 author name] — domain: institutional learning
- [ ] For any domain without a confirmed author as of T+0: send contingency recruitment email (see CT-1)

### 09:00–17:00 UTC: Project Setup

- [ ] Create or verify phase-6/ directory structure:
  ```
  projects/systems-resilience/phase-6/
  ├── domain-economic-resilience.md        [placeholder committed]
  ├── domain-infrastructure-interdependencies.md
  ├── domain-international-coordination.md
  ├── domain-intergenerational-transmission.md
  ├── domain-ecosystem-restoration.md
  └── domain-institutional-learning.md
  ```
  Each placeholder file must contain: YAML frontmatter (title, author, domain, status: IN-PROGRESS, created date), a single H1 heading, and a "Research begins T+0" note. Commit to master.

- [ ] Shared source library folder shared with each author (Google Drive, Git folder, or equivalent). Each author folder contains:
  - The 20–30 pre-staged sources annotated for their domain
  - The relevant Phase 5 model document
  - The domain candidate file (pre-research outline)
  - PHASE_6_AUTHOR_ONBOARDING_KIT.md (their copy)
  - This checklist (their milestones highlighted)

- [ ] Peer reviewer roster emailed: introductory note explaining the timeline (peer review begins T+10, 48-hour turnaround requested, feedback via structured template in PHASE_6_COORDINATION_TEMPLATES.md)

### 17:00 UTC: T+0 Day-End Review

- [ ] Author receipt confirmations received? (Expect 70–80% same-day responses. Non-responsive authors get one follow-up at T+1 09:00 UTC before CT-1 activates.)
- [ ] Any scope questions from authors requiring orchestrator clarification? Log and respond within 4 hours.
- [ ] All placeholder files committed to master?
- [ ] WORKLOG.md updated with T+0 status

---

## T+1 through T+6: Research Production Sprint (June 2–7)

### Daily Standup Protocol (Every Day, 08:00 UTC)

Run the daily standup asynchronously unless a blocking issue requires synchronous discussion. Use the Daily Standup Template from PHASE_6_COORDINATION_TEMPLATES.md. The standup takes 15–30 minutes per domain if async; 30 minutes total if sync.

**Daily standup agenda for T+1 through T+6:**

1. **Research progress check** (per domain, 2-3 sentences max):
   - Word count delivered yesterday: [N] words
   - Primary sources integrated: [N] new citations
   - Sections completed: [section names]
   - Sections in progress: [section names]
   - Expected sections to complete today: [section names]

2. **Blocker check** (mark Y/N and escalate if Y):
   - Source access blocked (paywall, dead link): Y/N — if Y, see Source Access Protocol below
   - Scope boundary question requiring orchestrator input: Y/N — if Y, log and respond within 4 hours
   - Word count tracking significantly under target: Y/N — if Y, see CT-3
   - Cross-domain coordination needed: Y/N — if Y, coordinate authors same-day

3. **Peer review queue** (T+6 and later):
   - Any sections ready for peer review ahead of T+10 gate: Y/N
   - If Y: send to designated peer reviewer with structured feedback template

4. **Publication readiness flag** (mark from T+10 onward):
   - Domain on track for T+14 readiness gate: Y/N/AT-RISK

**Source Access Protocol**: When an author reports a source inaccessible (paywall, link rot, institutional access required), the orchestrator uses WebSearch/WebFetch within 2 hours to identify an accessible substitute. If no substitute is found within 4 hours, the section proceeds with a [CITATION NEEDED] marker and a same-day alternative sourcing sprint is added to the orchestrator's queue. Do not let source gaps block writing momentum.

### T+1 (June 2): Orientation Confirmation Day

All T+1 author interactions are about ensuring each author has what they need to write, not about reviewing output.

- [ ] Confirm each author has read their four required orientation documents (model doc, domain candidate file, onboarding kit, pre-research chapter)
- [ ] Confirm each author's outline approach: are they working from the pre-staged outline in their domain candidate file, or proposing a variation? Variations require orchestrator sign-off before the author invests in them. Expected variations at T+1 are fine — expected variations at T+5 are a scope risk.
- [ ] For authors who have not responded by T+1 09:00 UTC: send one follow-up. If no response by T+1 17:00 UTC: activate CT-1.
- [ ] Log any outstanding scope clarifications in a running FAQ document (PHASE_6_SCOPE_FAQ.md) — share with all authors so clarifications propagate.

**Expected output at T+1 EOD**: Zero writing expected. Author understanding confirmed. Outline approach confirmed or variation flagged.

### T+2 (June 3): Research Kit Verification Complete

- [ ] Each author has opened and confirmed access to all pre-staged sources
- [ ] Any inaccessible sources flagged and substituted
- [ ] Authors for Wave 1 fast-track domains (economic resilience, infrastructure interdependencies) have begun outlining Section 1 of their document
- [ ] Source count per domain updated in daily standup log
- [ ] Cross-domain coordination note: if economic resilience and infrastructure interdependencies authors are working in parallel, check that their foundational framing of "community resilience" is consistent — a 15-minute coordination note resolves most framing divergences before they entrench in drafts

**Expected output at T+2 EOD**: Section outlines in progress for fast-track domains. Source library access confirmed for all domains.

### T+3 (June 4): Outline Review Gate

This is the first formal decision gate of Wave 1. Each author must submit their section-by-section outline by T+3 17:00 UTC.

**Outline requirements (per domain):**
- 8–12 major sections identified
- Each section: 2–3 sentence scope description, primary sources assigned (minimum 3 per section), estimated word count (4,000–6,000 words/section), one-sentence Zone 5 or community-context implication note
- Total target word count for the domain document stated explicitly
- Out-of-scope boundaries noted at the section level (not just document level)
- Integration points with other Phase 6 domains noted (where does this document cite or rely on outputs from other domains?)

**Orchestrator outline review (T+3 17:00 UTC to T+4 12:00 UTC):**

Review each outline against:
- [ ] Does it cover the core research questions from the domain candidate file?
- [ ] Is the Zone 5 or community context grounded in each section, or floating at abstraction level?
- [ ] Are the integration points with other domains realistic (not requiring outputs that won't exist until later waves)?
- [ ] Is the scope boundary held? Any section that drifts into Phase 5 territory (already covered) or into a different Phase 6 domain (scope overlap) needs a boundary correction before writing begins
- [ ] Is the estimated word count per section proportionate to the research depth in that section?

**Outline review SLA**: Orchestrator returns feedback by T+4 12:00 UTC. Feedback is structured as: (A) approved as submitted, (B) approved with minor notes (author proceeds, incorporates notes in writing), or (C) revision required (author revises outline, resubmits by T+5 EOD — see CT-3 if revision is extensive).

**Expected output at T+3 EOD**: All domain outlines submitted by 17:00 UTC. Orchestrator review begins immediately.

### T+4 (June 5): Outline Feedback and First Writing Day

- [ ] Outline feedback sent to all authors by 12:00 UTC
- [ ] Authors with "approved" or "approved with minor notes" outlines begin Section 1 writing
- [ ] Authors with "revision required" outlines: resubmit by T+5 EOD; do not begin writing until revision is approved
- [ ] Fast-track domain authors (economic resilience, infrastructure interdependencies): should complete Section 1 first draft today (4,000–6,000 words expected)
- [ ] Daily standup confirms outline status and writing start

**Milestone T+4**: Outline review cycle closes. All authors should know their section architecture by end of day.

### T+5 (June 6): Wave 2 Domain Ramp

Wave 2 domains (ecosystem restoration, institutional learning) begin their onboarding today. Their T+0 equivalent starts at T+5.

- [ ] Wave 2 domain authors receive their briefing email (same template as T+0, dated for today)
- [ ] Wave 2 domain research kits delivered
- [ ] Wave 2 domain orientation reading begins
- [ ] Wave 1 fast-track domains (economic resilience, infrastructure interdependencies): Section 1 and 2 writing in progress; expect 8,000–12,000 words delivered by T+7
- [ ] International coordination and intergenerational transmission authors: Sections 1–2 outlines approved or in revision; writing begun

**Daily standup focus on T+5**: Check fast-track domain progress against word count target. First warning if any domain is tracking below 50% of expected word count for T+7 checkpoint.

### T+6 (June 7): Week 1 Status Review

At T+6 17:00 UTC, conduct the first full wave-level status review (use Weekly Sync format from PHASE_6_COORDINATION_TEMPLATES.md, abbreviated to 30 minutes).

- [ ] Word count per domain at T+6 EOD (target for fast-track domains: 8,000–12,000 words in draft)
- [ ] Citation count per domain (target: 20+ citations integrated in submitted sections)
- [ ] Peer reviewer introductions confirmed (each domain's reviewer has been contacted and confirmed availability for T+10 review)
- [ ] Any scope drift detected in submitted sections? Flag for same-day correction
- [ ] Resource contention check: any domain requiring orchestrator research support that is blocking author progress?
- [ ] Wave 2 domain authors on track for T+7 outline submission

Log T+6 status in WORKLOG.md. This is the last log entry before the T+7 first-draft checkpoint.

---

## T+7 (June 8): First-Draft Checkpoint

**This is the first major quality gate of Wave 1.** All fast-track domain authors must submit their first-draft package by T+7 12:00 UTC.

### First-Draft Submission Requirements

Each author submits to the orchestrator:

1. **Draft sections delivered**: Minimum 2 sections (8,000–15,000 words depending on section count and word count distribution)
2. **Citation log**: Running bibliography of all sources used so far (any format; orchestrator will verify formatting at T+14)
3. **Status note** (3–5 sentences): What sections are complete, what is in progress, any research gaps discovered, any scope questions
4. **Word count projection**: Based on current pace, will the full document be complete by T+14? If not, what is the realistic completion date?

### Orchestrator T+7 Evaluation (T+7 12:00 UTC to T+8 09:00 UTC)

Evaluate each draft against the Research Quality Threshold:

**Pass criteria (all must be met):**
- [ ] Word count on track: ≥50% of section targets met, or credible projection to completion by T+14
- [ ] Citation depth adequate: ≥15 distinct source citations in submitted sections; no section over 3,000 words with fewer than 5 citations
- [ ] Zone 5 / community context present: at least 2 sections show specific community application (named institutions, specific geographic context, or operational case studies)
- [ ] Practitioner voice consistent: document reads as practitioner documentation, not academic writing (use Phase 5 model documents as calibration reference)
- [ ] No major scope violations: document does not reproduce Phase 5 content, does not drift into another Phase 6 domain without cross-reference, stays within confirmed out-of-scope boundaries

**At-risk indicators (one trigger = escalation discussion; two triggers = CT-3 activates):**
- Total submitted word count is under 5,000 words without explanation
- Fewer than 10 distinct citations in submitted sections
- No Zone 5 or community context in any section
- Voice has drifted significantly academic (compare against model doc)

**Fail criteria (immediately activates CT-2 — research dead-end — or CT-3 — author unavailability):**
- No submission by T+7 17:00 UTC without advance notice from author
- Submitted draft is structurally different from approved outline without orchestrator discussion
- Research gap so severe that the document's core thesis cannot be supported with accessible sources

### T+7 Decision Gate Summary

For each domain, the orchestrator makes one of three decisions by T+8 09:00 UTC:

| Decision | Condition | Action |
|---|---|---|
| **Green — proceed** | All pass criteria met | Confirm with author; continue at pace |
| **Amber — at-risk watch** | One at-risk indicator present | 20-minute synchronous call; agree on corrective actions by T+8 EOD |
| **Red — escalate** | Fail criterion triggered or two+ at-risk indicators | Activate CT-2 or CT-3 immediately |

Log all T+7 gate decisions in WORKLOG.md before end of T+7.

---

## T+8 through T+9: Mid-Wave Production (June 9–10)

### T+8 (June 9): Feedback Loop Closes

- [ ] Orchestrator feedback sent to all authors by 09:00 UTC
- [ ] Authors with Green status: continue writing; no additional checkpoints until T+10
- [ ] Authors with Amber status: check-in by T+8 17:00 UTC to confirm corrective actions underway
- [ ] Wave 2 domain authors (ecosystem restoration, institutional learning): outline submissions due by T+8 17:00 UTC; orchestrator review follows same T+3–T+4 process scaled to their timeline

**Mid-wave production targets (T+8 to T+10):**
- Fast-track domains (economic resilience, infrastructure interdependencies): 60–70% of full document in draft by T+10
- Secondary domains (international coordination, intergenerational transmission): 40–50% of full document in draft by T+10
- Wave 2 domains (ecosystem restoration, institutional learning): outlines approved; Section 1 writing begun by T+10

### T+9 (June 10): Peer Review Queue Preparation

By T+9, the orchestrator prepares the peer review queue so peer reviewers are ready to receive material at T+10.

- [ ] Confirm each peer reviewer's availability for T+10–T+12 review window
- [ ] Send peer reviewers the structured review template (from PHASE_6_COORDINATION_TEMPLATES.md — Peer Review Triage Process)
- [ ] Brief peer reviewers on domain scope: 2–3 sentence domain summary + the specific review criteria they should evaluate (completeness, citation depth, community context accuracy, practitioner voice)
- [ ] Identify any peer reviewer conflicts: if a peer reviewer is unfamiliar with Zone 5 context, pair them with a Zone 5 community practitioner for a 15-minute orientation call
- [ ] Confirm peer review return deadline: T+12 17:00 UTC (48 hours from T+10 send)

---

## T+10 (June 11): Peer Review Begins

### Peer Review Submission (T+10 06:00–12:00 UTC)

All fast-track and secondary domain authors submit their current draft for peer review by T+10 12:00 UTC, regardless of completion status. Incomplete drafts are reviewed for what exists; peer reviewers flag sections that require additional sourcing or completeness before T+14.

**Peer review submission package per domain:**
1. Current draft (however complete, clearly marked with [IN PROGRESS] on unfinished sections)
2. Domain scope summary (1 paragraph)
3. Three specific questions for the peer reviewer (sections where the author wants targeted feedback)
4. Citation list (may be informal at this stage; formatting verified at T+14)

### Peer Review Triage (T+10 12:00 UTC)

Orchestrator routes each domain's draft to the confirmed peer reviewer. Each reviewer receives:
- The submission package
- The structured review template (see PHASE_6_COORDINATION_TEMPLATES.md)
- The confirmed return deadline: T+12 17:00 UTC
- Contact information for the domain author (for any clarifying questions)

Log all T+10 submissions in a peer review tracking table:

| Domain | Author | Submitted T+10 | Words at submission | Peer reviewer | Review deadline | Returned |
|---|---|---|---|---|---|---|
| Economic resilience | [name] | Y/N | [N] | [name] | T+12 17:00 | — |
| Infrastructure interdependencies | [name] | Y/N | [N] | [name] | T+12 17:00 | — |
| International coordination | [name] | Y/N | [N] | [name] | T+12 17:00 | — |
| Intergenerational transmission | [name] | Y/N | [N] | [name] | T+12 17:00 | — |
| Ecosystem restoration | [name] | Y/N | [N] | [name] | T+12 17:00 | — |
| Institutional learning | [name] | Y/N | [N] | [name] | T+12 17:00 | — |

---

## T+11 through T+12: Peer Review Window (June 12–13)

### T+11 (June 12): Production Continues During Review

Authors continue writing during the peer review window. The peer review is not a blocking gate for production — it is a parallel track.

- [ ] Authors continue producing content in unreviewed sections
- [ ] Orchestrator monitors for peer reviewer questions (route to authors within 2 hours)
- [ ] Any peer reviewer delay flagged and escalated (CT-4 trigger: peer review delayed)
- [ ] Wave 2 domain authors: 20–30% of document in draft by T+11 EOD
- [ ] All domain authors: update word count in daily standup log

### T+12 (June 13): Peer Review Returns Due

All peer reviews due by T+12 17:00 UTC.

**If a peer review is not returned by T+12 17:00 UTC:**
- Send one reminder at T+12 09:00 UTC
- If no response by T+12 17:00 UTC: activate CT-4 (peer review delay contingency)

**Orchestrator peer review integration (T+12 17:00 UTC onward):**
- [ ] Review each peer review return against the structured template criteria
- [ ] Identify: (A) factual corrections, (B) citation requests, (C) scope concerns, (D) community context gaps
- [ ] Prioritize feedback: corrections and citation requests are mandatory for T+14; scope concerns and context gaps are advisory
- [ ] Send consolidated feedback to each author by T+12 23:00 UTC, categorized as mandatory and advisory

---

## T+13 (June 14): Integration Sweep

T+13 is the final full production day. Authors address mandatory peer review feedback and complete remaining sections.

### Author T+13 Tasks

- [ ] Address all mandatory peer review items (factual corrections, citation gaps)
- [ ] Complete any remaining unfinished sections (minor gaps acceptable if flagged with [CITATION NEEDED] or [NEEDS EXPANSION])
- [ ] Run a placeholder scan: search document for [, TODO, TBD, fill, NEEDS — list all and resolve what is resolvable
- [ ] Cross-reference check: verify any references to other Phase 6 domains point to the correct file and section
- [ ] Final word count confirmation: document should be at 60–90% of target word count by T+13 EOD (below 60% triggers CT-3 conversation)

### Orchestrator T+13 Tasks

- [ ] Track all six domains against publication readiness matrix (see PHASE_6_COORDINATION_TEMPLATES.md — Publication Readiness Assessment)
- [ ] Identify any domains likely to miss the T+14 gate — begin contingency scope adjustment conversation now, not at T+14
- [ ] Cross-domain consistency check: do the six domain documents use consistent terminology for foundational concepts (resilience, community, Zone 5, institutional, etc.)? Inconsistencies at this stage are fixed in light editing, not rewrites.
- [ ] Prepare T+14 gate agenda: list each domain, its completion estimate, and any outstanding items

---

## T+14 (June 15): Publication-Readiness Gate

The Wave 1 execution ends at T+14 23:59 UTC. The gate is publication readiness, not publication — documents may still require final formatting and citation verification before actual distribution, but the research substance and peer review integration must be complete.

### T+14 Delivery Requirements

Each domain document must meet or credibly project meeting all nine publication readiness criteria (from the Publication Readiness Assessment Matrix in PHASE_6_COORDINATION_TEMPLATES.md):

1. Domain completeness: ≥80% of target word count
2. Citation depth: ≥25 distinct, accessible citations (verified accessible)
3. Peer review integration: all mandatory feedback items addressed
4. Publication template: YAML frontmatter complete, zero placeholder markers
5. Contact stratification: Tier 1/2/3 distribution contacts identified for the domain
6. Timeline confirmation: distribution timeline confirmed (user decision)
7. Community context: Zone 5 or direct community application in every major section
8. Cross-domain bridges: at least 2 explicit integration points with other Phase 6 domain documents
9. Practitioner voice: document matches Phase 5 model document voice standard

**Scoring**: Each criterion scores 0, 0.5, or 1. Minimum score for Wave 1 publication readiness: 7.0/9.0. Documents scoring 6.0–6.9 move to "conditional readiness" with a list of items to complete before distribution. Documents scoring below 6.0 trigger a scope adjustment conversation.

### T+14 Gate Review (08:00–17:00 UTC)

- [ ] Orchestrator completes publication readiness assessment for each domain
- [ ] Scores logged per domain
- [ ] Domains at ≥7.0: confirmed wave 1 complete; author notified; milestone payment processed
- [ ] Domains at 6.0–6.9: conditional readiness items listed; author and orchestrator agree on completion timeline (expected: within 5 business days of T+14)
- [ ] Domains below 6.0: scope adjustment meeting scheduled within 24 hours

### T+14 Wave 1 Completion Log (17:00 UTC)

Update WORKLOG.md and ORCHESTRATOR_STATE.md:

```
Phase 6 Wave 1 complete — T+14 June 15 2026
Domains completed: [N]/6
Publication readiness scores:
  Economic resilience: [X.X]/9
  Infrastructure interdependencies: [X.X]/9
  International coordination: [X.X]/9
  Intergenerational transmission: [X.X]/9
  Ecosystem restoration: [X.X]/9
  Institutional learning: [X.X]/9
Domains at conditional readiness: [list]
Domains deferred to Wave 2: [list]
Wave 2 activation: [date] per user decision
```

---

## Decision Gates Summary

| Gate | Timing | Trigger | Owner | Decision |
|---|---|---|---|---|
| **R-1: Scope** | May 31 23:59 | User domain selection | User | Confirm domains; orchestrator logs |
| **R-2: Authors** | May 31 18:00 | Author roster complete | Orchestrator | Confirm or activate CT-1 |
| **R-3: Research kit** | May 31 16:00 | Pre-research assembled | Orchestrator | Confirm or flag gap |
| **R-4: Infrastructure** | May 31 14:00 | Directory + git clean | Orchestrator | Confirm or fix |
| **T+3: Outline review** | June 4 17:00 | Author outline submitted | Orchestrator | Approve / approve with notes / revise |
| **T+7: First draft** | June 8 12:00 | First-draft submission | Orchestrator | Green / Amber / Red |
| **T+10: Peer review** | June 11 12:00 | Draft sent to reviewer | Orchestrator | Confirm submission and routing |
| **T+12: Review returns** | June 13 17:00 | Peer review received | Orchestrator | Route feedback to authors |
| **T+14: Publication gate** | June 15 17:00 | Full Wave 1 assessment | Orchestrator | Readiness score per domain |

---

## Contingency Triggers

### CT-1: Author Unavailability

**Activation condition**: An author fails to respond to T+0 kickoff email by T+1 17:00 UTC; OR an author confirms unavailability after T+0; OR an author goes silent during production without advance notice.

**Fallback procedure (activate within 4 hours of trigger):**

1. **Immediate**: Log the gap. Confirm which domain(s) are affected. Check if any other confirmed authors have capacity to absorb the domain (authorship expansion — only viable if the domain is closely adjacent to their confirmed domain and the added workload is under 15 hours).
2. **Hour 0–4**: Contact contingency author list for the affected domain (from PHASE_6_AUTHOR_HIRING_AND_ONBOARDING_FRAMEWORK.md Stage 1 source channels). Send the contingency recruitment email (PHASE_6_AUTHOR_ONBOARDING_KIT.md Appendix — Contingency Author Template). Set a 24-hour response deadline.
3. **Hour 4–24**: If contingency author responds and accepts: brief them on the accelerated timeline (the T+3 outline gate shifts to T+5 for this author; T+7 gate shifts to T+9; T+10 peer review shifts to T+12 — all still within Wave 1 window if confirmed by T+2).
4. **If no author confirmed by T+3**: Activate self-execution path. Orchestrator takes the domain directly. Timeline: outline by T+4, first draft by T+9, peer review by T+12. Quality is slightly lower (orchestrator has less domain expertise than a specialist author) but Wave 1 completion is preserved.
5. **Timeline impact**: If self-execution path activates, the domain scores 6.5–7.0 at T+14 gate rather than 7.5–8.5. It remains publication-ready; the author-writing path produces higher quality but self-execution produces publishable material.

**Do not**: Cancel the domain. Defer publication readiness to Wave 2 for any domain where pre-research is complete. The pre-research foundation makes self-execution viable.

### CT-2: Research Dead-End

**Activation condition**: An author reports at any checkpoint (T+3, T+7, or during production) that the core thesis of a section or the domain document cannot be supported by accessible sources — either because the sources do not exist, are behind insurmountable paywalls, or directly contradict the framing established in the pre-research.

**Assessment protocol (within 4 hours of report):**

1. Orchestrator runs a 1-hour independent source search using WebSearch and WebFetch targeting the specific gap
2. If sources are found: provide them to the author; continue
3. If sources are not found but the framing can be adjusted: schedule a 20-minute call with the author to reframe the section — the goal is a narrower, more defensible claim, not a wholesale rewrite
4. If the gap is in a minor section (under 5% of total word count): mark as [RESEARCH GAP — DOCUMENTED] and note the gap explicitly in the document as a known limitation. This is acceptable for Wave 1.
5. If the gap is in a major section (over 15% of total word count): escalate to orchestrator scope decision. Options: (A) bring in a specialist co-reviewer who can identify sources; (B) reframe the section around what IS documented; (C) reclassify the section as a synthesis gap (not a failure — a legitimate finding that the literature has not addressed this question well)

**Do not**: Allow an undocumented gap to persist. Every major gap that cannot be filled must be named explicitly in the document. Wave 1 documents that acknowledge their own limitations are more credible than documents that paper over them.

### CT-3: Scope Creep

**Activation condition**: Orchestrator detects in outline review (T+3) or first-draft review (T+7) that a domain document is incorporating topics from Phase 5 (already covered), another Phase 6 domain (overlap risk), or entirely new research territory beyond the confirmed scope.

**Scope review protocol:**

1. Identify the specific sections at risk. Write a 2–3 sentence scope boundary note for each at-risk section.
2. Contact the author within 4 hours with a scope correction request: "Section [X] is entering territory covered by [Phase 5 Wave 2 conflict resolution document / Domain D institutional learning / etc.]. Please confirm scope of this section addresses [specific confirmed scope item] and references [existing document] rather than re-covering it."
3. Author responds within 24 hours. If scope is confirmed trimmed: proceed. If author disputes: schedule a 20-minute call within 48 hours to resolve.
4. If scope creep is resolved by T+4 (for T+3 detections) or T+9 (for T+7 detections): no timeline impact.
5. If scope creep detection happens at T+10 or later (during peer review): the peer reviewer flags it; orchestrator issues a mandatory scope correction before T+14 gate.

**Prevention**: The T+3 outline review is the primary scope-creep prevention mechanism. Approving an outline is approving the scope. If the outline passes and the draft deviates, the outline approval is the reference point for scope enforcement — not the draft.

### CT-4: Peer Review Delays

**Activation condition**: A peer reviewer fails to return their review by T+12 17:00 UTC.

**Fallback procedure:**

1. Send one reminder at T+12 09:00 UTC (6 hours before deadline)
2. If no return by T+12 17:00 UTC: activate backup reviewer. Each domain should have a confirmed backup reviewer identified by T+9. If no backup was confirmed, orchestrator conducts an expedited internal review using the structured template (2–3 hours per domain).
3. For the primary reviewer: log the delay. If the review arrives between T+13 and T+14, incorporate mandatory items only (factual corrections, critical citation gaps). Advisory items are deferred to post-Wave-1 refinement.
4. No domain fails the T+14 publication readiness gate solely because of a peer reviewer delay if the orchestrator internal review has been completed.

**Prevention**: Confirm peer reviewer availability at T+9, not T+10. If a reviewer signals uncertain availability at T+9, activate the backup immediately rather than waiting.

### CT-5: Scope Reduction (User Defers Domains)

**Activation condition**: User decides by May 31 that fewer than six domains should proceed in Wave 1. This is not an emergency — it is a planned contingency.

**Procedure:**
1. Remove deferred domains from all T+ checklists above. Their placeholder files remain committed; mark status as DEFERRED-WAVE-2.
2. Reallocate peer reviewer slots — if a peer reviewer was assigned a deferred domain, reassign them to cover a higher-priority active domain for depth review.
3. No other timeline changes. The T+3/T+7/T+10/T+14 gates apply identically to any 2-6 domain subset.
4. Log deferred domain list in ORCHESTRATOR_STATE.md with reason and expected Wave 2 activation window.

---

## Milestone Schedule Summary

| T-day | Date | Milestone | Owner |
|---|---|---|---|
| May 31 EOD | — | All R-gates green; scope confirmed | User + Orchestrator |
| T+0 | June 1 | Author briefings sent; project directories created | Orchestrator |
| T+1 | June 2 | Author receipt confirmed; outline approach confirmed | Authors |
| T+2 | June 3 | Research kit verified; writing begun (fast-track) | Authors |
| T+3 | June 4 | Outlines submitted (all domains) | Authors |
| T+4 | June 5 | Outline feedback returned; writing begins all active domains | Orchestrator |
| T+5 | June 6 | Wave 2 domain ramp begins | Orchestrator |
| T+6 | June 7 | Week 1 status review | Orchestrator |
| T+7 | June 8 | First-draft checkpoint — quality gate | Orchestrator |
| T+8 | June 9 | Feedback loop closes; Wave 2 outlines due | Authors + Orchestrator |
| T+9 | June 10 | Peer reviewer queue prepared; confirmed | Orchestrator |
| T+10 | June 11 | All drafts submitted to peer review | Authors |
| T+11 | June 12 | Production continues; peer review in progress | Authors |
| T+12 | June 13 | Peer reviews returned; feedback to authors | Reviewers |
| T+13 | June 14 | Integration sweep; mandatory feedback addressed | Authors |
| T+14 | June 15 | Publication-readiness gate; Wave 1 complete | Orchestrator |

---

*This checklist is production-ready. Copy-paste the relevant day's section into each daily standup. Update gate decisions in WORKLOG.md at each milestone. Contact the orchestrator within 4 hours if any contingency trigger activates — do not wait for the next scheduled standup.*
