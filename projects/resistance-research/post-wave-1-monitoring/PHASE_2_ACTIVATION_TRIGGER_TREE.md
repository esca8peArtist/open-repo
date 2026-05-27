# Phase 2 Activation Trigger Tree

**Date Created**: 2026-05-27 (Session 1708)  
**Trigger Event**: May 28 Synthesis Outcome Classification  
**Purpose**: Route synthesis outcome to correct Phase 2 domain activation decision  
**Decision Window**: May 28 19:45–20:00 UTC (15 minutes)

---

## Outcome Classification Entry Point

START: What is the synthesis outcome classification?

```
READ post-synthesis-outcome-2026-05-28.md → Outcome Classification field
```

---

## DECISION TREE (ASCII)

```
Outcome Classification
├── STRONG (Confidence ≥ 90%, Response Completion ≥ 75%)
│   │
│   └─→ PHASE 2 FULL EXPANSION: Domains 56 + 58 + 59
│       ├─ Immediate Action (19:45–20:00 UTC):
│       │  ├─ Email orchestrator: "May 28 synthesis STRONG. Spawning Domains 56/58/59 agents."
│       │  ├─ Spawn Agent 1: resistance-research (Domain 56 Civil Service, June 1–10)
│       │  ├─ Spawn Agent 2: resistance-research (Domain 58 Tribal Sovereignty, June 1–5)
│       │  └─ Spawn Agent 3: resistance-research (Domain 59 Economic Precarity, June 1–July 1)
│       │
│       ├─ Distribution Schedule:
│       │  ├─ May 28: Domain 56 distribution (user executes 14:00–18:00 UTC) ← ALREADY SCHEDULED
│       │  ├─ June 1: Domain 39 distribution (user executes 13:00–14:00 UTC) ← ALREADY SCHEDULED
│       │  ├─ June 1–5: Domain 58 rapid distribution if Trump v. Barbara issued
│       │  └─ June 15–July 1: Domain 59 production + distribution window
│       │
│       └─ CHECKIN.md Entry:
│           "May 28 synthesis STRONG (confidence 90%+). Phase 2 expansion activated:
│            - Domains 56 + 39 distribution May 28 + June 1 (user executes)
│            - Domain 56 research production June 1–10 (Agent)
│            - Domain 58 production June 1–5 (Agent, Trump v. Barbara rapid-response active)
│            - Domain 59 production June 1–July 1 (Agent)
│            Next checkpoints: May 28 Domain 56 send, June 1 Domain 39 send."
│
│
├── MODERATE (Confidence 80%, Response Completion 60–74%)
│   │
│   └─→ PHASE 2 SELECTIVE ACTIVATION: Domains 56 + 39 + 59 (hold Domain 58 pending ruling)
│       ├─ Immediate Action (19:45–20:00 UTC):
│       │  ├─ Email orchestrator: "May 28 synthesis MODERATE. Executing selective Phase 2 path."
│       │  ├─ Spawn Agent 1: resistance-research (Domain 59 Economic Precarity only)
│       │  ├─ Email Tier 1 law school + civil rights contacts:
│       │  │   Subject: "Domain 58 (Tribal Sovereignty) Contingency Briefing Ready"
│       │  │   Body: "May 28 synthesis outcome is MODERATE. Domain 58 rapid-response 
│       │  │          infrastructure is staged and ready for immediate activation 
│       │  │          upon Trump v. Barbara ruling (expected late June–early July). 
│       │  │          Briefing will be distributed within 24 hours of ruling. 
│       │  │          Continue monitoring for ruling announcement."
│       │  └─ DO NOT spawn Domain 56 or Domain 58 agents (content ready, staging complete)
│       │
│       ├─ Distribution Schedule:
│       │  ├─ May 28: Domain 56 distribution (user executes 14:00–18:00 UTC) ← ALREADY READY
│       │  ├─ June 1: Domain 39 distribution (user executes 13:00–14:00 UTC) ← ALREADY READY
│       │  ├─ [Contingent on Trump v. Barbara]: Domain 58 activation (24-hour window upon ruling)
│       │  └─ June 15–July 1: Domain 59 production + distribution
│       │
│       └─ CHECKIN.md Entry:
│           "May 28 synthesis MODERATE (confidence 80%). Phase 2 selective activation:
│            - Domains 56 + 39 distribution May 28 + June 1 (user executes)
│            - Domain 59 production June 1–July 1 (Agent spawned)
│            - Domain 58 contingency briefing staged; awaiting Trump v. Barbara ruling
│            - If ruling issued: Domain 58 activated within 24 hours (Agent spawned)
│            Next checkpoint: May 28 Domain 56 distribution; June 1 synthesis check for Trump v. Barbara."
│
│
├── WEAK (Confidence 75%, Response Completion 40–59%, Velocity declining)
│   │
│   └─→ PHASE 2 RESEARCH HOLD: Continue contingency path, do NOT spawn agents
│       ├─ Immediate Action (19:45–20:00 UTC):
│       │  ├─ Email orchestrator: "May 28 synthesis WEAK. Maintaining TOO_EARLY contingency path."
│       │  ├─ DO NOT spawn ANY Phase 2 agents
│       │  ├─ Schedule May 29 18:00 UTC re-synthesis attempt
│       │  ├─ Email user: "May 28 synthesis shows WEAK engagement metrics (40–59% completion, 
│       │  │              declining velocity). Signal data may improve by May 29 due to 
│       │  │              Friday weekend delay. Attempting re-synthesis May 29 18:00 UTC 
│       │  │              with complete 7-day response data. Phase 2 research pending May 29 outcome."
│       │  └─ Continue Domain 56 + 39 distribution as planned (per TOO_EARLY contingency design)
│       │
│       ├─ Distribution Schedule:
│       │  ├─ May 28: Domain 56 distribution (user executes 14:00–18:00 UTC) — PROCEEDS REGARDLESS
│       │  ├─ June 1: Domain 39 distribution (user executes 13:00–14:00 UTC) — PROCEEDS REGARDLESS
│       │  ├─ May 29 18:00 UTC: Re-synthesis attempt with complete May 18-28 data
│       │  └─ June 1+: Phase 2 research activation contingent on May 29 outcome
│       │
│       └─ CHECKIN.md Entry:
│           "May 28 synthesis WEAK (confidence 75%, 40–59% completion). Contingency hold:
│            - Domains 56 + 39 distribution May 28 + June 1 (user executes, unaffected)
│            - Phase 2 research (Domains 56/58/59) held pending May 29 re-synthesis
│            - May 29 18:00 UTC: Re-synthesis with complete 7-day data
│            - If May 29 outcome is STRONG/MODERATE: Phase 2 agents spawned May 30
│            - If May 29 outcome is WEAK/TOO_EARLY: Contingency path continues June 1+
│            Next checkpoint: May 29 18:00 UTC re-synthesis."
│
│
├── TOO_EARLY (Confidence 85%, Response Completion <40% OR insufficient data)
│   │
│   └─→ PHASE 2 RESEARCH HOLD: Continue contingency path, do NOT spawn agents
│       ├─ Immediate Action (19:45–20:00 UTC):
│       │  ├─ Email orchestrator: "May 28 synthesis TOO_EARLY (expected per contingency design)."
│       │  ├─ DO NOT spawn ANY Phase 2 agents (Domain 56/39 ready, Domains 57/58/59 pre-researched)
│       │  ├─ Update CHECKIN.md and WORKLOG.md
│       │  └─ Log outcome: "TOO_EARLY classification confirms contingency path is working correctly"
│       │
│       ├─ Distribution Schedule:
│       │  ├─ May 28: Domain 56 distribution (user executes 14:00–18:00 UTC) — PROCEEDS REGARDLESS
│       │  ├─ June 1: Domain 39 distribution (user executes 13:00–14:00 UTC) — PROCEEDS REGARDLESS
│       │  ├─ June 1–5: Phase 2 research activation (if user fills signal log by May 31)
│       │  │             OR contingency path continues if user does not update signal log
│       │  └─ July+: Deferred Phase 2 domains (57/58/59) activated post-distribution
│       │
│       └─ CHECKIN.md Entry:
│           "May 28 synthesis TOO_EARLY (confidence 85%, <40% completion). Contingency path active:
│            - Domains 56 + 39 distribution May 28 + June 1 (user executes)
│            - Phase 2 research held (all 5 domains pre-researched, ready for signal log completion)
│            - Per TOO_EARLY contingency design: distribution proceeds regardless of synthesis outcome
│            - If user fills signal log by May 31: Phase 2 agents spawned June 1
│            - If user does not fill: Phase 2 activation deferred to June 15+
│            - Tier 1 contingency briefing for Domain 58 (Trump v. Barbara awaiting ruling)
│            Next checkpoint: June 1 (user decision on Phase 2 research activation)."
│
│
└── CRISIS (Confidence 100%, Trump v. Barbara CONSTITUTIONAL holding issued)
    │
    └─→ IMMEDIATE OVERRIDE: Domain 58 activation, 24-hour rapid-response window
        ├─ Immediate Action (19:45–20:00 UTC, EMERGENCY):
        │  ├─ Email orchestrator + emergency channel: "ALERT: Trump v. Barbara ruling issued 
        │  │                                          (CONSTITUTIONAL holding). CRISIS override 
        │  │                                          activated. Domain 58 24-hour rapid-response window open."
        │  ├─ Spawn Emergency Agent: resistance-research (Domain 58 CRISIS rapid-response)
        │  ├─ Load CRISIS_DOMAIN_58_RAPID_RESPONSE.md playbook (from domain-58-rapid-response.md)
        │  ├─ Email Tier 1 tribal sovereignty + voting rights + civil rights contacts:
        │  │   Subject: "URGENT: Domain 58 Analysis Ready — Trump v. Barbara Ruling"
        │  │   Body: "Trump v. Barbara (birthright citizenship) ruling issued today. 
        │  │          Tribal sovereignty implications documented in attached analysis. 
        │  │          Key findings: [1-2 sentence summary]. Gist available for institutional 
        │  │          briefing + rapid-response strategy. Download: [link to Domain 58 Gist]."
        │  └─ Execute 24-hour delivery window (May 28 20:00 UTC → May 29 20:00 UTC)
        │
        ├─ Distribution Schedule (EMERGENCY):
        │  ├─ May 28 20:00–24:00 UTC: Domain 58 rapid-response research (Agent working 4h emergency shift)
        │  ├─ May 29 00:00–04:00 UTC: Domain 58 document finalization + Gist publication
        │  ├─ May 29 04:00–08:00 UTC: Tier 1 distribution to tribal sovereignty + voting rights contacts
        │  ├─ May 29 20:00 UTC: CRISIS window closure (normal ops resume)
        │  ├─ May 28: Domain 56 distribution (user executes 14:00–18:00 UTC) — UNAFFECTED
        │  └─ June 1: Domain 39 distribution (user executes 13:00–14:00 UTC) — UNAFFECTED
        │
        └─ CHECKIN.md Entry:
            "CRISIS ALERT: Trump v. Barbara (birthright citizenship) CONSTITUTIONAL holding issued May 28.
             Domain 58 (Tribal Sovereignty) CRISIS rapid-response activated (24-hour window).
             - Emergency research executed May 28 20:00–May 29 04:00 UTC (Agent 4h shift)
             - Tier 1 distribution to tribal sovereignty + voting rights contacts May 29 04:00–08:00 UTC
             - Domain 58 Gist live: [Gist URL]
             - Domains 56 + 39 distribution May 28 + June 1 (user executes, unaffected)
             - Phase 2 research activation: Domain 58 COMPLETE; Domains 56/59 activation TBD
             Next checkpoint: May 29 20:00 UTC (CRISIS window closure + normal Phase 2 resumption)."
```

---

## Decision Lookup Table (Fast Reference)

| Outcome | Confidence | Completion | Agent Spawn? | Domain 56/39 | Domain 58 | Domain 59 | Next Checkpoint |
|---|---|---|---|---|---|---|---|
| **STRONG** | 90%+ | ≥75% | ✅ All 3 (56, 58, 59) | ✅ May 28/June 1 | ✅ June 1–5 | ✅ June 1–July 1 | May 28 send |
| **MODERATE** | 80% | 60–74% | ✅ Domain 59 only | ✅ May 28/June 1 | 🔶 Contingency brief | ✅ June 1–July 1 | June 1 send |
| **WEAK** | 75% | 40–59% | ❌ None | ✅ May 28/June 1 | ❌ Hold | ❌ Hold | May 29 re-synthesis |
| **TOO_EARLY** | 85% | <40% | ❌ None | ✅ May 28/June 1 | ❌ Hold | ❌ Hold | June 1 user decision |
| **CRISIS** | 100% | — | ✅ Domain 58 emergency | ✅ May 28/June 1 | ✅ 24h emergency | ✅ TBD | May 29 08:00 UTC |

---

## Email Template: Tier 1 Contingency Briefing (MODERATE outcome only)

```
TO: [Tier 1 law school + civil rights contacts]
FROM: orchestrator@claude.local
SUBJECT: Domain 58 (Tribal Sovereignty) Contingency Briefing Ready — Trump v. Barbara
DATE: May 28, 2026 19:55 UTC

Body:
---

Dear [Contact],

The May 28 Phase 1 Wave 1 synthesis indicates MODERATE engagement across constituencies. 
Domain 58 (Tribal Sovereignty) has been staged for rapid-response activation.

We are monitoring the Supreme Court's Trump v. Barbara decision (expected late June–early July). 
This case concerns birthright citizenship and carries implications for tribal citizenship, 
voting rights, and SAVE Act interactions with tribal identification systems.

When the ruling is issued, Domain 58 analysis will be ready for immediate distribution 
within 24 hours. A briefing document is pre-staged with:
- Constitutional implications for tribal citizenship
- Voting rights impact across tribal nations
- State-level strategic response options
- Movement leverage points (tribal sovereignty, voting rights, immigration legal aid)

If you would like to be notified upon ruling issuance, reply to this email with "ALERT" 
and we will contact you within 1 hour of the ruling becoming public.

Best regards,
Orchestrator
---
```

---

## Execution Responsibility Matrix

| Task | Owner | When | Duration |
|---|---|---|---|
| Outcome classification | Orchestrator | May 28 19:00–19:45 UTC | 45 min |
| Decision tree execution | Orchestrator | May 28 19:45–20:00 UTC | 15 min |
| Email notifications | Orchestrator | May 28 20:00–20:10 UTC | 10 min |
| Agent spawning (if applicable) | Orchestrator | May 28 20:10–20:20 UTC | 10 min |
| CHECKIN.md + WORKLOG.md update | Orchestrator | May 28 20:20–20:30 UTC | 10 min |
| Domain 56 distribution (user) | User | May 28 14:00–18:00 UTC | 30 min |
| Domain 39 distribution (user) | User | June 1 13:00–14:00 UTC | 30 min |

---

**Business Value**: May 28 synthesis outcome triggers immediate Phase 2 activation with zero ambiguity; removes 2–3 hour post-outcome routing delay; enables same-day agent spawning if synthesis is STRONG/MODERATE.

**Commitment**: Session 1708, May 27 2026
