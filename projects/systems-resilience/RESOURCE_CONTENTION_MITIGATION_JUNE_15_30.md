---
title: "Resource Contention Mitigation — June 15–30"
project: systems-resilience
phase: 6
wave: 2
status: PRODUCTION-READY — June 15 deployment
created: 2026-06-04
revised: 2026-06-04
planning_period: 2026-06-15 to 2026-06-30
initiatives:
  stockbot: "June 11–30 expansion, 76h total"
  wave_2_onboarding: "June 20–23, 20h"
  wave_2_drafting: "June 24–30, 40–50h goal"
  resistance_research: "Batch 2 June 9+, 60h total"
cross_references:
  - PHASE_6_WAVE_2_ACTIVATION_CHECKLIST.md
  - WAVE_2_DOMAIN_SEQUENCING_FRAMEWORK.md
  - ORCHESTRATOR_STATE.md
word_count: ~1,900
---

# Resource Contention Mitigation — June 15–30
## Allocation Scenarios, Hour Estimates, and Escalation Triggers

**Prepared**: June 4, 2026 (production deployment)
**High-contention window**: June 15–30, 2026
**Initiatives in contention**:
- Stockbot June 11–30 expansion: **76 total hours**
- Phase 6 Wave 2 onboarding: **20 hours** (June 20–23)
- Phase 6 Wave 2 first-draft sprint: **40–50 hours** (June 24–30)
- Resistance-research Batch 2: **60 total hours** (June 9+, peak June 9–15, monitor-only June 16+)

**Lead**: Orchestrator (scenario execution) + User (escalation decisions at named decision points)

---

## Part 1: Three Initiatives — Hour Profiles

### Initiative 1: Stockbot June 11–30 Expansion (76h Total)

**What**: Deploy AMZN and JPM tickers to Jetson production cluster; execute multi-ticker backtesting and validation; initialize Month 1 live trading protocols with HMM Lever B configuration.

**Hour distribution**:

| Period | Hours | Activity |
|--------|-------|----------|
| June 11–15 | 22h | Deployment prep, SSH verification, backtesting setup |
| June 16–23 | 32h peak | Active deployment, multi-ticker backtesting, validation checkpoints (8h/day June 16–17, then declining) |
| June 24–30 | 14h monitor | Live trading initialization, model monitoring, anomaly response only |
| June 30+ | monitor only | Steady-state monitoring (~3h/week) |

**Orchestrator coordination requirement**: 20–25h of the 76h total requires orchestrator decisions (SSH debugging, deployment approval, rollback calls). The remainder is stockbot subagent execution.

**Time-critical reason**: Jetson thermal constraint (81–84°C idle, 87.8°C under compute; documented in project memory). Extended compute window closes if multi-ticker deployment does not complete by June 30. Deployment must run during the cool-weather operational window.

**Risk flag**: If stockbot enters CAUTION state (model drift detected) or ROLLBACK state (trading halted) during June 16–17 peak window, the 32h deployment block expands to 40–50h (diagnostic sprint required). This is the primary scenario-routing trigger.

---

### Initiative 2: Phase 6 Wave 2 Onboarding (20h)

**What**: Author orientation, Nextcloud+Matrix access provisioning, source library delivery, outline review, T+0 kickoff messages, peer reviewer coordination. June 20–23 window.

**Hour distribution**:

| Activity | Hours | Date |
|----------|-------|------|
| Onboarding kit delivery + author confirmations | 4h | June 20 |
| Access provisioning checks (Nextcloud+Matrix) | 2h | June 20–21 |
| Domain folder population (source libraries, outlines) | 6h | June 20–21 |
| T+0 kickoff message review (one per author) | 3h | June 20–21 |
| T+3 outline review and feedback | 5h | June 23–24 |
| **Total** | **20h** | June 20–24 |

**Orchestrator requirement**: All 20h require orchestrator (cannot be delegated to subagent). Low-intensity but non-compressible: each author needs a personal response to their kickoff message and outline.

---

### Initiative 3: Phase 6 Wave 2 First-Draft Sprint (40–50h)

**What**: Author support, T+7 checkpoint assessment (June 27), T+10 full-draft review (June 30), peer reviewer coordination, escalation handling, Wave 1 publication cross-reference support. June 24–30 window.

**Hour distribution**:

| Activity | Hours | Date |
|----------|-------|------|
| Author support (questions, scope clarification, 4-6h/day June 24–28) | 20–25h | June 24–28 |
| T+7 checkpoint assessment (review 5 partial drafts, ~2h each) | 10h | June 27–28 |
| T+10 full-draft review prep (scheduling, peer reviewer briefing) | 5h | June 29–30 |
| Wave 1 publication cross-reference support (authors citing Wave 1 docs) | 5–10h | June 24–30 |
| **Total** | **40–50h** | June 24–30 |

**Note on 40h vs 50h**: The 40h estimate assumes authors are Tier A/B (self-directed, minimal blocking questions). The 50h estimate applies if 2+ authors are Tier C (extended check-ins, scope re-narrowing needed). Actual orchestrator hours will track against this estimate starting June 24.

---

### Initiative 4: Resistance-Research Batch 2 (60h Total, Monitor-Only June 16+)

**What**: Domain 51 (Campaign Finance) June 9–12 execution; Domain 57 (Multilateral Withdrawal) June 13–15 final distribution; Batch 2 monitoring June 16–30.

**Hour distribution**:

| Period | Hours | Activity |
|--------|-------|----------|
| June 9–15 | 50h | Active research execution (Domains 51, 57) — research agent primary, orchestrator coordination 8–10h |
| June 16–30 | 10h monitor | Response monitoring, contact follow-up only. No new research agent activations unless triggered by Senate Finance markup news. |
| **Total** | **60h** | June 9–30 |

**June 16+ status**: Resistance-research enters monitor-only mode after June 15 Batch 2 completion. Orchestrator coordination drops to ~1–2h/week (monitoring dashboard reviews, contact response triage). This frees significant orchestrator bandwidth for Wave 2.

---

## Part 2: Three Allocation Scenarios

### Scenario A: Full Parallel (Recommended Default)

**Assumption**: Stockbot deployment on schedule (no CAUTION/ROLLBACK state); Wave 2 authors ≥4 confirmed; resistance-research Batch 2 completes by June 15.

**Allocation June 15–30**:

| Initiative | June 15–23 | June 24–30 | Agent |
|------------|-----------|-----------|-------|
| Stockbot expansion | 54h (deployment peak) | 14h (monitor) | Stockbot subagent primary; orchestrator 18h coordination |
| Wave 2 onboarding | 20h (June 20–24) | — | Orchestrator (non-compressible) |
| Wave 2 first-draft | — | 40h (full intensity) | Orchestrator primary; author-driven |
| Resistance-research | 10h (monitor, June 15) | 4h monitor | Research agent; orchestrator 2h/week |

**Total orchestrator hours June 15–30**:
- June 15–23 (9 days): 18h stockbot + 20h Wave 2 onboarding = **38h** (4.2h/day average — feasible)
- June 24–30 (7 days): 14h stockbot monitor + 40h Wave 2 drafting + 4h resistance monitor = **58h** (8.3h/day — high but bounded)
- **Two-week total**: **96h orchestrator** across all initiatives

**Risk**: June 24–30 at 8.3h/day is above sustainable 6h/day capacity. Mitigated by: (a) stockbot June 24–30 is monitor-only (low decision overhead), and (b) resistance-research June 24+ is passive monitoring. The intensive work is Wave 2 drafting support — which is author-driven and can be handled in batches rather than constant real-time response.

**Feasibility**: Yes, if agents are compartmentalized. Stockbot subagent operates independently; orchestrator reviews outputs at morning and evening checkpoints (30 min each), not continuously. Wave 2 author support is async — orchestrator processes all author questions in 2 dedicated sessions/day (09:00 UTC and 17:00 UTC) rather than continuous availability. This reduces the effective orchestrator synchronous load.

**Context fragmentation risk**: Medium. Three separate project contexts active simultaneously (stockbot trading model, Wave 2 domain research, resistance-research monitoring). Mitigated by ORCHESTRATOR_STATE.md daily status updates that anchor each context before switching.

**Outcome**: All three initiatives active June 15–30 without delay. Wave 2 first-draft checkpoint June 27 met. Stockbot deployment complete June 30. Resistance-research Batch 2 distribution complete June 15.

---

### Scenario B: Sequential Waves (Stockbot-First)

**Assumption**: Stockbot deployment requires intensive focus June 15–23 (CAUTION state detected, or SSH connectivity issues requiring diagnostic sprint); Wave 2 cannot receive full orchestrator support until June 24.

**Allocation June 15–30**:

| Initiative | June 15–23 | June 24–30 | Agent |
|------------|-----------|-----------|-------|
| Stockbot expansion | 54h (full intensity, priority) | 14h (monitor) | Stockbot subagent + orchestrator 25h coordination |
| Wave 2 onboarding | 12h (light: kit delivery, access only; no outline reviews until June 24) | 20h (delayed full onboarding) | Orchestrator (compressed) |
| Wave 2 first-draft | — | 30h (reduced — 1 week less runway) | Orchestrator partial |
| Resistance-research | 10h (monitor completion) | 4h monitor | Research agent |

**Total orchestrator hours June 15–30**:
- June 15–23: 25h stockbot + 12h Wave 2 light = **37h** (4.1h/day — manageable)
- June 24–30: 14h stockbot monitor + 20h Wave 2 onboarding + 30h Wave 2 drafting = **64h** (9.1h/day — high)
- **Two-week total**: **101h orchestrator**

**Wave 2 impact**: Wave 2 onboarding starts June 20 as planned (kit delivery is low-overhead and proceeds even under Scenario B), but outline reviews are deferred to June 24. Authors submit outlines June 23 but receive feedback June 24–25. T+7 first-draft checkpoint slips from June 27 to July 1. T+10 full draft slips from June 30 to July 4. T+14 revision complete slips from July 4 to July 8. Publication readiness gate slips from July 5 to July 9.

**Net delay**: **4 days to Wave 2 publication readiness gate**. This is acceptable — Phase 7 pilot recruitment can begin July 10 instead of July 7 with no material impact.

**Risk**: June 24–30 at 9.1h/day is unsustainable for a full week. Mitigation: by June 28, stockbot monitor drops to 1h/day; Wave 2 author support front-loads on June 24–27 (outline feedback window) and eases June 28–30 (authors are independently drafting).

**When to activate**: If stockbot enters CAUTION state during June 16–17 OR if SSH connectivity issues are detected on June 15 that require 2+ day diagnostic sprint. Do not activate preemptively — only activate if stockbot blocking condition is confirmed.

---

### Scenario C: Stockbot-First, Wave-2-Throttled (Compromise)

**Assumption**: Stockbot deployment requires high intensity June 15–23 but Wave 2 June 20 start is politically immovable (author contracts signed, June 20 commitment made). Wave 2 proceeds at reduced intensity June 20–23, then full intensity June 24–30.

**Allocation June 15–30**:

| Initiative | June 15–23 | June 24–30 | Agent |
|------------|-----------|-----------|-------|
| Stockbot expansion | 54h (full intensity June 15–23) | 14h (monitor) | Stockbot subagent + orchestrator 22h coordination |
| Wave 2 onboarding | 20h at light load (kit delivery, access setup; author questions batched once/day) | — | Orchestrator (throttled response time: 24h instead of 4–6h) |
| Wave 2 first-draft | — | 20–30h (moderate, not full intensity) | Orchestrator partial; authors primary |
| Resistance-research | 10h (monitor) | 4h monitor | Research agent |

**Total orchestrator hours June 15–30**:
- June 15–23: 22h stockbot + 20h Wave 2 onboarding (throttled) = **42h** (4.7h/day — feasible)
- June 24–30: 14h stockbot monitor + 25h Wave 2 drafting = **39h** (5.6h/day — sustainable)
- **Two-week total**: **81h orchestrator** (most efficient scenario)

**Wave 2 June 20 start preserved**: Authors begin June 20 as committed. However, orchestrator response time during June 20–23 is 24 hours (not 4–6 hours). Authors are warned in the onboarding kit that this window has reduced orchestrator availability (stockbot peak overlap). Tier A authors are unaffected. Tier B/C authors may experience 1-day delays on scope questions — this is the quality cost of Scenario C.

**First-draft quality note**: With 20–30h of orchestrator drafting support instead of 40–50h, the T+7 checkpoint review is lighter (orchestrator skims rather than deep-reviews partial drafts). First-draft quality will be somewhat lower on June 27 — requiring a more substantive editorial pass July 1–5. This is the defined cost of Scenario C: accept a July 1–5 editorial pass rather than a June 30 clean submission.

**Publication readiness gate**: July 5 as planned — but with the understanding that 1–2 domains may require a second editorial pass July 1–5, pushing their individual readiness to July 7–10 (within the July 10–25 publication window — no Phase 7 impact).

**When to activate**: Default fallback if orchestrator load tracking shows Scenario A will breach 10h/day during June 24–30. Also activates automatically if stockbot deployment is not complete by June 23 EOD.

---

## Part 3: Recommendation Matrix

| Condition | Recommended Scenario |
|-----------|---------------------|
| Stockbot: no CAUTION/ROLLBACK, deployment on track | **Scenario A** (full parallel) |
| Stockbot: CAUTION state June 16–17 | **Scenario B** immediately — Wave 2 pipeline shifts 4 days |
| Stockbot: ROLLBACK state (trading halted) | **Scenario B** immediately — stockbot stability is critical; Wave 2 delay acceptable |
| Agent budget permits parallel teams | **Scenario A** — compartmentalization resolves context fragmentation |
| Agent budget constrained (single orchestrator) | **Scenario C** — compromise achieves June 20 Wave 2 start, accepts quality tradeoff |
| Orchestrator load forecast >10h/day any day in June 24–30 | Shift from **A** to **C** at that point |
| Wave 2 author roster <4 confirmed June 15 | **Scenario C** regardless of stockbot state — reduced author count reduces support hours needed |

**Primary recommendation**: Attempt Scenario A. At June 19 EOD, check orchestrator load forecast for June 24–30. If forecast exceeds 10h/day average, immediately downgrade to Scenario C. Do not wait for overload to manifest — preempt it.

---

## Part 4: Specific Hour Allocation by Initiative

The following allocations represent the **Scenario A default** with Scenario C numbers noted where they differ:

| Initiative | June 15–23 Hours | June 24–30 Hours | June 15–30 Total |
|------------|-----------------|-----------------|-----------------|
| Stockbot (76h total, June 11–30) | 32h active deployment (June 16–23) | 14h monitor | **46h in window** |
| Wave 2 onboarding | 20h (June 20–24) | — | **20h** |
| Wave 2 first-draft | — | 40–50h (Scenario A) / 20–30h (Scenario C) | **40–50h (A) / 20–30h (C)** |
| Resistance-research Batch 2 | 10h monitor (through June 15 completion) | 4h monitor June 16–30 | **14h in window** |
| **Orchestrator total (Scenario A)** | **38h** | **58h** | **96h** |
| **Orchestrator total (Scenario C)** | **42h** | **39h** | **81h** |

---

## Part 5: Contingency Triggers

### Trigger 1: Stockbot CAUTION State Detected June 16–17

**Definition**: HMM model drift exceeds threshold OR live trading anomaly detected requiring 4+ hour diagnostic.

**Immediate action** (within 1 hour of detection):
- Pause all non-critical Wave 2 orchestrator responses (defer to 24h queue).
- Shift to Scenario B: stockbot diagnostic sprint takes orchestrator priority June 16–23.
- Wave 2 authors notified via Matrix `#wave2-general`: "Orchestrator availability reduced through June 23 due to infrastructure maintenance. Response time 24h. Peer mentors are your primary contact. June 20 start date unchanged."
- Outline review for T+3 (June 23) shifted to June 24–25.

### Trigger 2: Stockbot ROLLBACK State (Trading Halted)

**Definition**: Live trading halted by safety circuit; full model audit required.

**Immediate action**:
- Scenario B activates. Stockbot stability is non-negotiable — it has live capital exposure. Wave 2 delay (4 days) is explicitly acceptable per the recommendation matrix above.
- User notification within 30 minutes of ROLLBACK state: escalate decision on whether to extend diagnostic window beyond 7 days (which would push Scenario B into full Wave 2 deferral territory).

### Trigger 3: Orchestrator Load Exceeds 10h/Day for 3 Consecutive Days in June 24–30

**Definition**: Orchestrator logs show 10+ actual hours/day (not estimated) for 3 days in a row.

**Immediate action**:
- Shift from Scenario A to Scenario C. Reduce Wave 2 drafting support from 40–50h to 20–30h remaining in window.
- Tier A authors: no change.
- Tier B authors: next scheduled check-in deferred by 2 days.
- Tier C authors: scope reduction conversation accelerated — bring word count target down to 3,000 words immediately.
- Notify user: "Downshifting to Scenario C to protect orchestrator sustainability. Wave 2 editorial pass moved to July 1–5. Publication readiness gate still July 5 for most domains."

### Trigger 4: Resistance-Research Batch 2 Senate Finance Markup Breaks June 20+

**Definition**: Breaking news on Senate Finance CTC markup or major legislative development after June 15 that requires new domain research.

**Immediate action**:
- Assess: is new research required (new domain activation, 20+ hours), or is monitoring and contact follow-up sufficient (2–4 hours)?
- If new domain: defer to July 1 Batch 3. Protect June 20–30 for Wave 2 and stockbot.
- If monitoring only: handle within existing 4h/week resistance-research monitor budget. No scenario change.

---

## Part 6: Communication Protocol (June 15–30)

**Daily escalation format** (Thursday EOD, async to user):

```
WEEK [N] CHECKPOINT (June [X]–[Y])

Orchestrator hours logged: [total]
Active scenario: [A / B / C]

ON TRACK:
- [project]: [status in one line]

AT RISK:
- [project]: [risk description] | Risk level: [LOW/MEDIUM/HIGH]
  Proposed mitigation: [one sentence]

DECISIONS NEEDED BY [DATE] [TIME] UTC:
1. [Decision] — options: [A] [B] | Default if no response: [action]

RECOMMENDATION:
[One sentence on current scenario + any trigger watch]
```

**Trigger-activated escalation** (any time, user notification within 30 min):

```
SCENARIO CHANGE ALERT — [Date] [Time] UTC

Trigger: [trigger description]
Activating: Scenario [B / C]
Impact: [one sentence on Wave 2 timeline impact]
Stockbot status: [one line]
User decision required: [YES/NO]
If YES: [decision description with deadline]
```

---

**Summary**: June 15–30 is the highest-intensity orchestrator window of the Phase 6 launch. The recommended approach is Scenario A (full parallel) if agent budget permits and stockbot is on track. The primary routing trigger is stockbot CAUTION/ROLLBACK state in June 16–17: if detected, Scenario B activates immediately (4-day Wave 2 delay acceptable, stockbot stability non-negotiable). If orchestrator load proves unsustainable in Scenario A, Scenario C provides a compromise solution that preserves the June 20 Wave 2 start while accepting a modest quality tradeoff on first drafts. All three scenarios converge on the same Wave 2 publication readiness gate — July 5 (Scenario A), July 9 (Scenario B), or July 5–10 (Scenario C) — within the acceptable range for Phase 7 pilot recruitment beginning July 7–10.
