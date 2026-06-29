---
title: "Phase 2 Post-Deadline Contingency Decision Tree — Automated Branch Routing"
created: "2026-06-29"
session: "General Research Agent — Item 33"
status: "PRODUCTION-READY — mechanical routing, no human judgment required"
trigger: "Send execution timestamp from INBOX.md post"
output: "Branch assignment (A/B/C) + link to execution guide"
deadline: "July 1 2026 00:00 UTC"
---

# Phase 2 Post-Deadline Contingency Decision Tree
## Automated Branch Routing — Input: Date → Output: Branch

**Design principle**: This decision tree is fully mechanical. Input the send execution date, read the single output branch, execute that branch. No analysis, no judgment, no re-evaluation required.

**Companion file**: PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md (full execution procedures per branch)

---

## Input: How to Get the Send Execution Date

The user posts send completion to INBOX.md in one of these formats:

```
[resistance-research] Domain 51/48 sends executed 2026-[MM]-[DD] [HH]:[MM] UTC
```

or

```
[resistance-research] Domain 51/48 sends executing 2026-[MM]-[DD]
```

Extract the date from this post. This is the **Send Execution Date**.

If no INBOX.md post exists and the current date is July 1 or later: treat Send Execution Date as **unknown/future**. Apply the Branch B trigger (July 1 00:00 UTC passed without confirmation = minimum Branch B).

---

## Primary Decision Tree

```
STEP 1: Read the Send Execution Date from INBOX.md
        ↓
STEP 2: Is the Send Execution Date June 29 or June 30?
        ↓
  YES → BRANCH A (No contingency needed)
        Action: Post to user: "Branch A — sends on time. Normal Tier 2 per PHASE_2_CONTINGENCY_DECISION_TREE.md"
        Stop.
        ↓
  NO  → Continue to Step 3
        ↓
STEP 3: Is the Send Execution Date July 1 through July 7 (inclusive)?
        ↓
  YES → BRANCH B (Slipped <7 days — condensed protocol)
        Action: Post to user: "Phase 2 contingency activated (Branch B). See PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md Branch B"
        Stop.
        ↓
  NO  → Continue to Step 4
        ↓
STEP 4: Is the Send Execution Date July 8 or later?
        ↓
  YES → BRANCH C (Slipped >7 days — full contingency)
        Action: Post to user: "Phase 2 contingency activated (Branch C). Emergency protocol. See PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md Branch C"
        Stop.
        ↓
  NO (date unknown, no INBOX post, and current date ≥ July 1):
        → BRANCH B (default until sends confirmed)
        Action: Post to user: "Branch B contingency triggered (July 1 deadline passed, sends not confirmed). Branch B dormant until INBOX.md confirmation received. If sends execute July 8+, upgrade to Branch C."
        Stop.
```

---

## Trigger Conditions Table (Exact Thresholds)

| Condition | Branch | Activation Time |
|-----------|--------|----------------|
| INBOX.md confirmation received, date is June 29 or June 30 | A | No activation — dormant |
| INBOX.md confirmation received, date is July 1 00:00 UTC – July 7 23:59 UTC | B | Immediate on confirmation receipt |
| July 1 00:00 UTC arrives with no INBOX.md confirmation | B (dormant) | Triggers automatically at July 1 00:00 UTC |
| INBOX.md confirmation received, date is July 8 00:00 UTC or later | C | Immediate on confirmation receipt |
| July 8 00:00 UTC arrives with no INBOX.md confirmation | C (escalate from B) | Triggers automatically at July 8 00:00 UTC |
| INBOX.md confirmation received after July 8, regardless of stated date | C | Immediate on confirmation receipt |

**Timezone note**: All times are UTC. July 1 00:00 UTC = June 30 20:00 Eastern / June 30 17:00 Pacific.

---

## Pre-Authorized Actions Per Branch

No further user decisions are required once a branch activates. These actions are authorized in advance.

### Branch A — Pre-Authorized Actions

1. Post "Branch A — no contingency" confirmation to INBOX.md
2. Set T+7 checkpoint reminder (7 days from send date)
3. Route to PHASE_2_CONTINGENCY_DECISION_TREE.md (existing June 17 document) for T+7 signal routing

No contingency files needed. No user judgment required.

### Branch B — Pre-Authorized Actions

1. Post "Phase 2 contingency activated (Branch B)" to INBOX.md
2. Load PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md Branch B section
3. Execute Branch B date calculation table (derive all target dates from send date)
4. Execute Branch B 8-contact Domain 51 priority list (PHASE_2_CONTINGENCY_CONTACT_TIER_MATRIX.md Branch B Domain 51 group)
5. Execute Branch B 8-contact Domain 48 priority list (PHASE_2_CONTINGENCY_CONTACT_TIER_MATRIX.md Branch B Domain 48 group)
6. Activate Tier 3 early (send day + 2) — no T+7 gate required for Tier 3 in Branch B
7. Set 72h escalation check: if 0 replies, activate all remaining Tier 3 immediately
8. Send ACLU VA July 8–12 (Virginia July 15 gate)

User does not need to re-evaluate any of the above. Execute mechanically.

### Branch C — Pre-Authorized Actions

1. Post "Phase 2 contingency activated (Branch C) — emergency protocol" to INBOX.md
2. Assess Virginia July 15 gate immediately: sends by July 11 → ACLU VA immediate; July 12+ → skip ACLU VA
3. Rewrite all CA-specific language in templates to federal framing (see Branch C template modifications)
4. Execute Branch C 6-contact emergency group (PHASE_2_CONTINGENCY_CONTACT_TIER_MATRIX.md Branch C emergency 6)
5. If Saturday–Sunday send: execute Priority 1–3 immediately; defer Priority 4–6 to Monday 08:00 local
6. Send Domains 49–50 stakeholder notification emails (see Branch C section in PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md)
7. Schedule August 1–7 deferred contact group (do not send July 12–31 for Hill-adjacent contacts)
8. Activate Domains 49–50 research August 1 (not July)

User does not need to re-evaluate any of the above. Execute mechanically.

---

## INBOX.md Post Templates (User Copy-Paste)

When sends execute, user posts one of these to INBOX.md:

**Sends on time (June 29–30)**:
```
[resistance-research] Domain 51/48 sends executed 2026-06-[DATE] [TIME] UTC — Branch A
```

**Sends slipped July 1–7**:
```
[resistance-research] Domain 51/48 sends executed 2026-07-[DATE] [TIME] UTC — Branch B
```

**Sends slipped July 8+**:
```
[resistance-research] Domain 51/48 sends executed 2026-07-[DATE] [TIME] UTC — Branch C
```

---

## Orchestrator Discord Notification Template

When Branch B or C activates, orchestrator posts to user Discord with this format:

**Branch B**:
```
Phase 2 contingency activated (Branch B). Domain 51/48 sends slipped past July 1. 
Condensed Tier 2 protocol active. 8-contact high-urgency list + early Tier 3.
Estimated execution: 2–3h spread July 2–10.
See: PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md (Branch B section)
```

**Branch C**:
```
Phase 2 contingency activated (Branch C) — EMERGENCY PROTOCOL. 
Domain 51/48 sends slipped 7+ days. Full contingency: 6-contact emergency list,
August 1 post-recess window, CA deadline framing retired.
Estimated execution: 4–5h spread July–August.
Virginia July 15 gate: assess IMMEDIATELY (sends by July 11 = ACLU VA viable).
See: PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md (Branch C section)
```

---

## Edge Cases

**If sends execute for one domain but not the other**:
- Apply the branch for the LATER domain (most conservative)
- Example: Domain 48 executes June 30, Domain 51 executes July 3 → Branch B for Domain 51 only; Domain 48 runs Branch A contact schedule

**If Gist URL returns 404 on execution day**:
- Do not proceed with sends until Gist is restored
- Restoration procedures: DOMAIN_48_GIST_CREATION_STEPS.md (Domain 48), DOMAIN_51_CONTINGENCY_SB_299_FALLBACK.md (Domain 51)
- Branch clock continues ticking — Gist restoration does not pause the branch trigger dates
- If Gist restoration takes >24h and execution date crosses a branch boundary: apply the stricter branch

**If user posts partial confirmation (Domain 51 only, Domain 48 pending)**:
- Apply branch logic separately: Domain 51 routes to its branch; Domain 48 remains pending
- Domain 48-specific contacts (Sentencing Project, PPI, Brennan Center, Worth Rises, CLC Restore Your Vote, M4BL) are governed by Domain 48's execution date
- Domain 51-specific contacts (CLC campaign finance, Issue One, True North, Democracy 21, ECU) are governed by Domain 51's execution date

---

## Decision Tree Summary Card (Print-Ready)

```
┌─────────────────────────────────────────────────────────┐
│     PHASE 2 CONTINGENCY — BRANCH ROUTER                 │
│─────────────────────────────────────────────────────────│
│  Sends executed June 29–30?    → BRANCH A (none)        │
│  Sends executed July 1–7?      → BRANCH B (condensed)   │
│  Sends executed July 8+?       → BRANCH C (emergency)   │
│  July 1 00:00 UTC — no post?   → BRANCH B (trigger)     │
│  July 8 00:00 UTC — no post?   → BRANCH C (escalate)    │
│─────────────────────────────────────────────────────────│
│  Branch B: 2–3h | 8 contacts | July 2–10                │
│  Branch C: 4–5h | 6 contacts | July 8–August 7          │
│─────────────────────────────────────────────────────────│
│  Full procedures:                                        │
│  PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md        │
│  Contact lists:                                         │
│  PHASE_2_CONTINGENCY_CONTACT_TIER_MATRIX.md             │
└─────────────────────────────────────────────────────────┘
```

---

*Created June 29, 2026 (Item 33, Exploration Queue). This document replaces ad-hoc branch determination for post-July-1 slippage. Companion files: PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md (execution procedures), PHASE_2_CONTINGENCY_CONTACT_TIER_MATRIX.md (contact lists), PHASE_2_CONTINGENCY_EXECUTION_PROCEDURES.md (copy-paste templates), PHASE_2_CONTINGENCY_FINANCIAL_MODEL.md (impact analysis). Existing June 17 decision tree (PHASE_2_CONTINGENCY_DECISION_TREE.md) remains active for T+7 signal routing after sends execute.*
