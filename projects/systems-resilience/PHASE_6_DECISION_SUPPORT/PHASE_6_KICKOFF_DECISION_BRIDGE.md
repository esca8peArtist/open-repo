---
title: "Phase 6 Kickoff Decision Bridge — May 31 to June 1 Activation"
project: systems-resilience
phase: 6
status: COPY-PASTE-READY
decision_deadline: 2026-05-31
activation_date: 2026-06-01
created: 2026-05-27
purpose: "User decision routing: check a box on May 31, agent activates with the right brief on June 1. Zero planning lag."
---

# Phase 6 Kickoff Decision Bridge

**User action required**: Read Section 1. Check boxes. Done. The rest executes automatically on June 1.

---

## Section 1: User Decision Checklist

**Check the box(es) next to your selected domain(s). Then write one sentence in CHECKIN.md (template in Section 2).**

### Your Phase 6 Domain Selection

- [ ] **Domain A — Community Economic Resilience** (Domain 64)
  - Fastest delivery. August 9 target. 95% confidence. Lowest setup friction.
  - Agent brief: `PHASE_6_COMMUNITY_ECONOMIC_AGENT_BRIEF.md`

- [ ] **Domain B — Intergenerational Skills Development** (Domain 61)
  - Medium complexity. August 23 target. 88% confidence. Education background beneficial.
  - Agent brief: `PHASE_6_INTERGENERATIONAL_SKILLS_AGENT_BRIEF.md`

- [ ] **Domain C — Governance Scaling** (Domain 65)
  - Highest complexity. August 30 target. 78% confidence. Political science background strongly recommended.
  - Agent brief: `PHASE_6_GOVERNANCE_SCALING_AGENT_BRIEF.md`

### Timing Preference

- [ ] All selected domains launch June 1 in parallel
- [ ] Economic Resilience first (June 1), Skills Development concurrent, Governance Scaling deferred to September 1
- [ ] Economic Resilience + Skills Development June 1; Governance Scaling September 1 (recommended for 3-domain selection)

---

## Section 2: CHECKIN.md Template

Copy the following block into CHECKIN.md on May 31 under the heading "Phase 6 Domain Selection":

```
## Phase 6 Domain Selection

**Chosen domain(s)**: [Domain A (Economic) / Domain B (Skills) / Domain C (Governance) / list two or three]

**Primary reason**: [One sentence — e.g., "Phase 5 left the resource exchange question completely open and we need that layer before Phase 7."]

**Timing preference**: [All parallel June 1 / Economic first then parallel / Economic + Skills June 1, Governance September 1]

**Author expertise**: [Any domain where you have a specific author in mind — e.g., "Skills author has adult learning background"]

**Additional constraints**: [Optional — any scope boundaries, particular subsections to prioritize, or questions for orchestrator]
```

---

## Section 3: Automated Routing

When you have written your decision in CHECKIN.md, the orchestrator executes the following on June 1 based on your selection. No further action required from you.

### If Domain A (Economic Resilience) is selected:

**Agent activation command**:
```
You are the Phase 6 research agent for Community Economic Resilience (Domain 64).
Your full brief is at:
projects/systems-resilience/PHASE_6_DECISION_SUPPORT/PHASE_6_COMMUNITY_ECONOMIC_AGENT_BRIEF.md

Read the brief in full before beginning any research. Week 1 task: source library
verification. Production start: June 8. First checkpoint: June 15 (outline complete +
sources verified). First-draft milestone: July 13.
```

**Orchestrator actions June 1**:
1. Deliver the agent brief to the research agent
2. Log activation in WORKLOG.md: "Phase 6 Domain 64 (Community Economic Resilience) activated June 1. Agent brief delivered. Production start June 8. Checkpoint schedule: June 15, June 29, July 13, July 27, August 9."
3. Add to ORCHESTRATOR_STATE.md: Domain 64 in active research, target August 9
4. Schedule checkpoint pings: June 15, June 29, July 13, July 27, August 9

### If Domain B (Skills Development) is selected:

**Agent activation command**:
```
You are the Phase 6 research agent for Intergenerational Skills Development (Domain 61).
Your full brief is at:
projects/systems-resilience/PHASE_6_DECISION_SUPPORT/PHASE_6_INTERGENERATIONAL_SKILLS_AGENT_BRIEF.md

Read the brief in full before beginning any research. CRITICAL: Scope is bounded to
12-15 critical skills only — not comprehensive education theory. Week 1 task: source
library verification + learning curve gap research initiated. Production start: June 10.
First checkpoint: June 15 (outline + learning curve gap status).
```

**Orchestrator actions June 1**:
1. Deliver the agent brief to the research agent
2. Note in handoff: "Scope enforcement is active — enforce 12-15 skills ceiling at weeks 3, 6, 9. Education background helps; note author background in first checkpoint."
3. Log activation in WORKLOG.md with checkpoint schedule: June 15, June 29, July 13, July 27, August 23
4. Add to ORCHESTRATOR_STATE.md: Domain 61 in active research, target August 23

### If Domain C (Governance Scaling) is selected:

**Agent activation command**:
```
You are the Phase 6 research agent for Governance Scaling and Institutional Adaptation
(Domain 65). Your full brief is at:
projects/systems-resilience/PHASE_6_DECISION_SUPPORT/PHASE_6_GOVERNANCE_SCALING_AGENT_BRIEF.md

Read the Scope Management Protocol in the brief before reading anything else. The governance
literature is vast; scope enforcement is not passive — it requires active audits. Week 1-1.5
task: extended source library work, particularly governance failure case studies in
resource-constrained settings. Production start: June 15. First checkpoint: June 15 (source
library + outline). Hard scale ceiling: 150-500 person federation only.
```

**Orchestrator actions June 1**:
1. Deliver the agent brief to the research agent
2. Note in handoff: "Political science background strongly recommended. If author lacks this, add 2-3 weeks to timeline. Book weekly scope audits June 22, July 13, August 3 before starting."
3. Log activation in WORKLOG.md with checkpoint schedule: June 15, June 29, July 13, July 27, August 30
4. Add to ORCHESTRATOR_STATE.md: Domain 65 in active research, target August 30

### If two or three domains are selected:

Deliver all relevant agent briefs simultaneously. Each agent reads only their brief. Coordination sync schedule is in each brief's "Notes on Concurrent Execution" section.

For Economic + Governance pairing: calendar a July 13 sync (30 min) and mark it in ORCHESTRATOR_STATE.md.
For Economic + Skills pairing: no required syncs. Share July 13 drafts asynchronously.
For Governance + Skills pairing: calendar June 29 and July 27 syncs (30 min each).

---

## Section 4: 15-Minute Activation Protocol

This is what happens in the 15 minutes after you write your decision in CHECKIN.md on May 31 — or what the orchestrator executes on June 1 morning.

### Minutes 1-5: Decision Read and Route

1. Orchestrator reads CHECKIN.md "Phase 6 Domain Selection" entry
2. Identifies which domain(s) are selected
3. Identifies timing preference (parallel vs. staged)
4. Routes to the correct agent brief(s) in this directory
5. Notes any author expertise or scope constraints specified

### Minutes 5-10: Agent Brief Delivery and Initialization

For each selected domain:
1. Locate the agent brief in `projects/systems-resilience/PHASE_6_DECISION_SUPPORT/`
2. Deliver brief to research agent with activation command (from Section 3 above)
3. Agent confirms receipt and reads brief in full (this is the agent's first 30-60 minute task — reading the brief is not optional)
4. Log activation in WORKLOG.md

### Minutes 10-15: State Update and Checkpoint Calendar

1. Update ORCHESTRATOR_STATE.md: mark Phase 6 as active, list domain(s), list completion target(s)
2. Add Phase 6 checkpoint dates to any existing project calendar or ORCHESTRATOR_STATE.md checkpoint section
3. If two domains selected: note any required inter-domain sync dates
4. Confirm nothing in Phase 5 publication execution (if proceeding simultaneously) conflicts with Phase 6 start

**Result**: By minute 15, the research agent has the brief, the orchestrator has logged the activation, and the checkpoint calendar is set. Research begins without any additional planning sessions.

---

## Section 5: Quick-Reference Card

```
PHASE 6 DECISION — QUICK REFERENCE

USER DECISION (May 31):
  Write in CHECKIN.md → domain(s) selected + timing

AGENT BRIEFS (June 1 — copy-paste ready):
  Domain A (Economic)    → PHASE_6_COMMUNITY_ECONOMIC_AGENT_BRIEF.md
  Domain B (Skills)      → PHASE_6_INTERGENERATIONAL_SKILLS_AGENT_BRIEF.md
  Domain C (Governance)  → PHASE_6_GOVERNANCE_SCALING_AGENT_BRIEF.md

DECISION MATRIX (if still deciding):
  → PHASE_6_DOMAIN_DECISION_MATRIX.md

FEASIBILITY / RISK:
  → PHASE_6_FEASIBILITY_ASSESSMENT.md

DELIVERY TARGETS:
  Domain A → August 9    (95% confidence)
  Domain B → August 23   (88% confidence)
  Domain C → August 30   (78% confidence)
  A + B    → August 23   (90% confidence, both)
  A + C    → August 23/30 (90% / 82% confidence)
  All 3    → A+B Aug 23, C Oct 15 (recommended)

REQUIRED SYNCS:
  A solo   → none
  B solo   → none
  C solo   → none
  A + B    → none required (optional async July 13)
  A + C    → July 13 (30 min)
  B + C    → June 29 + July 27 (30 min each)

FASTEST ACTIVATION:
  Select Domain A only. Agent activates June 1.
  Source verification June 1-7. Production June 8.
  First deliverable June 15 (outline + verified sources).
  On-time delivery August 9.
```

---

## Section 6: If User Does Not Decide by May 31

If CHECKIN.md has no "Phase 6 Domain Selection" entry by May 31 23:59 UTC, the orchestrator executes the default activation on June 1:

**Default**: Activate Domain A (Community Economic Resilience) only.

Rationale: Highest confidence, lowest risk, most immediately actionable. The default protects June 1 activation while the user considers their full selection. User can add Domain B or C at any point in June — the briefs are ready, the production timelines accommodate a delayed start through approximately June 15 with a 1-week target extension each.

**Delayed start adjustments**:
- Domain A delayed start June 8: target shifts from August 9 to August 16 (one week slip, confidence unchanged)
- Domain B delayed start June 15: target shifts from August 23 to August 30 (confidence unchanged at 88%)
- Domain C delayed start June 22: target shifts from August 30 to September 13 (confidence rises slightly to 80% — more source resolution time)
