# Exploration Queue

> Autonomous research and architectural planning items that advance project Goals beyond immediate blockers.
> These are exploratory work items that are independent of user action items.
> Status legend: ✅ (complete) ✍️ (in-progress) ⏳ (queued) ⌛ (deferred)

## Active Items (Session 1451+)

### 1. ⏳ stockbot — Gate 2 Post-Checkpoint Architecture Decision Framework
**Scope**: Research three post-May-22-checkpoint scenarios and decision tree for Gate 2 (live trading expansion).
- **Scenario A**: Equity-only continuation (AAPL lgbm_ho + ridge_wf, risk management focus)
- **Scenario B**: Covered-call overlay (Gap 4 naked-call prevention + options coordination)
- **Scenario C**: Multi-strategy ensemble (equity + covered-calls + trend-following, 5+ assets)
- **Deliverables**: 
  - `GATE_2_ARCHITECTURE_DECISION_FRAMEWORK.md` (3,000-4,000 words)
  - Decision tree with financial impact analysis per scenario
  - Implementation timeline and dependencies per scenario
- **Owner**: stockbot subagent
- **Deadline**: May 23 (post-checkpoint decision window)

### 2. ⏳ cybersecurity-hardening — Trump v. Barbara Birthright Citizenship Rapid-Response Update
**Scope**: Research post-birthright-citizenship-ruling implications for immigration surveillance threat model.
- **Context**: Trump v. Barbara SCOTUS case (expected June-July 2026) may narrow birthright citizenship
- **Research**: Threat implications, BIA reorganization context, tribal sovereignty dimension
- **Deliverables**: `trump-v-barbara-rapid-response.md` v3 supplement (1,500-2,000 words), Domain 58 update
- **Owner**: general-research agent
- **Deadline**: May 23 (before Phase 2 finalization)

### 3. ⏳ mfg-farm — Multi-Printer Scaling Architecture (3-5 Printer Farm Design)
**Scope**: Design manufacturing scaling from single-printer launch to 3-5 printer farm (Q2-Q4 2026).
- **Technical**: Material diversity, queue management, print coordination, parallel slicing
- **Economic**: Cost per printer, revenue impact, staffing, supplier scaling
- **Deliverables**: `MULTI_PRINTER_SCALING_ROADMAP.md` (4,000-5,000 words), `PRINTER_FARM_EQUIPMENT_SPECIFICATIONS.md`
- **Owner**: mfg-farm subagent
- **Deadline**: May 24 (before June 3 scaling launch)

---

## Completed Items (Session 1450)

### ✅ seedwarden — Practitioner Relationship Roadmap & Affiliate Partnership Ecosystem
**Completed**: May 21 (Session 1450). All files delivered, Tier A partners ready for June 1 activation.

### ✅ mfg-farm — Pre-Production Supply Chain Risk Mitigation Strategy
**Completed**: May 21 (Session 1450). Vendor backups identified, MOQ/lead time analysis, safety stock budget ready.

### ✅ cybersecurity-hardening — Windows Encryption Transition Guide (VeraCrypt Certificate Crisis)
**Completed**: May 21 (Session 1450). June 27 hard deadline documented, BitLocker alternatives researched.

---

## Deferred Items (Post-May-25)

### ⌛ resistance-research — Phase 2 Batch 1 Architecture (post-synthesis)
**Context**: May 21 19:00 UTC synthesis determines Phase 2 launch path. Post-synthesis Phase 1 Batch 2 architecture planning (May 25+).
**Deadline**: May 22-25 post-synthesis

### ⌛ systems-resilience — Phase 5 Wave 3 Expansion (June 1+)
**Context**: Phase 5 Wave 2 research complete. Wave 3 addresses remaining Tier gaps.
**Deadline**: June 15

### ⌛ open-repo — Phase 5.2 Planning (post-merge)
**Context**: Phase 5.1 MVP ready for user merge review.
**Deadline**: June 1+

---

## Queue Management Rules

- **Capacity**: Target 2-3 active items per session
- **Trigger**: When all projects blocked and queue <3 items, add new items
- **Assignment**: Pair each item with agent profile; leverage parallel execution
