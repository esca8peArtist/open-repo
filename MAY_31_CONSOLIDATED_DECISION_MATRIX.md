---
title: "May 31 Consolidated Decision Matrix"
project: "Multi-Project Coordination"
created: 2026-05-27
decision_deadline: 2026-05-31
execution_target: 2026-06-01
status: READY FOR USER DECISION
---

# May 31 Consolidated Decision Matrix

**TL;DR**: Three decisions are due by May 31. Each decision unlocks a different June 1-15 timeline. This document shows you what you're choosing and what happens next.

---

## The Three Decisions

### Decision 1: Stockbot Lever B — Model Type (Due May 27 EOD)
**Question**: JPM model architecture — retrain for diversity or use existing?

**Option A: Retrain JPM ridge_wf** (preserves architecture diversity)
- Timeline: Training takes 2-3 hours; deployment takes 30 min
- Total activation: May 28-31 (can start immediately after decision)
- June 1 status: 4-session engine deployed and validated, ready for live trading
- Risk profile: Medium (retrain is new code path, but architecture is proven)
- Advantages: Matches original specification (JPM is mean-reverting, ridge_wf is linear), validates ridge_wf on financials ticker
- Disadvantages: 2-3 hours delay vs. Option B

**Option B: Update config to use existing JPM lgbm_ho** (faster activation)
- Timeline: Config update takes 30 min; deployment takes 15 min
- Total activation: May 26-27 (can deploy today)
- June 1 status: 4-session engine deployed and running, ready for live trading
- Risk profile: Low (lgbm_ho is already trained and tested)
- Advantages: Immediate deployment, zero training risk
- Disadvantages: Loses architecture diversity (both AAPL and JPM use same model type)

**Impact on June 1-15**:
- **Option A**: 4-session engine validates May 28-31; June 1+ can begin live trading + position monitoring
- **Option B**: 4-session engine validates today; June 1+ can begin live trading + position monitoring
- **Either way**: June 1+ status is identical (4-session engine live and trading)

**Execution packages ready**: ✅ `OPTION_A_RIDGE_WF_RETRAIN_RUNBOOK.md` + `OPTION_B_CONFIG_UPDATE_RUNBOOK.md` (committed May 27)

**Recommendation**: **Option A** (aligns with original specification, validates ridge_wf, validates architecture diversity at cost of 2-3 hours)

---

### Decision 2: Systems-Resilience Phase 5 — Publication Timing (Due May 31)
**Question**: How to sequence 66,442 words of Phase 5 content to maximize community impact?

**Option A: Staged** (Wave 1+2 June 5, Wave 3 June 30)
- Publish 43,621 words immediately; announce 22,821-word supplement coming June 30
- June 1-5: Editorial cleanup + publication prep (light work)
- June 5: Release Wave 1+2 (Microgrids, Vet Care, Psych Support, Conflict Resolution, Implementation Playbook)
- June 6-25: Collect reader feedback; light revision of Wave 3 based on practitioner signal
- June 30: Release Wave 3 (Food, Water, Livestock, Seed, Healthcare, Fuel, Education)
- Decision score: **30/40** (fastest impact, best feedback loop, clearest audience narrative)
- June resource impact: 20-25 hours (light)
- Phase 6 start window: June 1 (immediate, no conflict)

**Option B: Unified** (Full 66.4K release June 15)
- Hold all 12 documents until June 15 for comprehensive editorial integration
- June 1-14: Master table of contents, cross-reference cleanup, frontmatter standardization (10-15 hours orchestrator time)
- June 15: Release all 66,442 words as single comprehensive reference
- Advantage: Strongest artifact for outreach; definitive "bible" position
- Disadvantage: 14-day delay in getting content to practitioners; no feedback loop before publication
- Decision score: **24/40** (strongest artifact, weakest speed/digestibility)
- June resource impact: 30-35 hours (heavy)
- Phase 6 start window: June 1 (can overlap with editorial work)

**Option C: Rolling modular** (Weekly pairs May 30+)
- Publish 6 thematic pairs across 6 weeks (May 30, June 6, 13, 20, 27, July 4)
- Highest audience engagement; highest coordination cost
- Requires weekly editorial + announcement + feedback monitoring cycle
- Decision score: **27/40** (best engagement, highest orchestration cost)
- June resource impact: 40-45 hours (heavy, sustained)
- Phase 6 start window: June 1 (can overlap but with increased contention)

**Recommendation**: **Option A** (fast impact, real feedback loop, lightest resource cost, clears Phase 6 runway immediately)

---

### Decision 3: Systems-Resilience Phase 6 — Domain Selection (Due May 31)
**Question**: Which three domains should launch as Phase 6 Week 1 (June 1-10 research)?

**Domain A: Community Economic Resilience** (20 hours)
- Covers mutual credit, labor exchange, gift economies, cooperative structures, community currencies
- Highest gap fill (Phase 5 has food/water/energy, but nothing on economic coordination)
- Sources: Elinor Ostrom commons governance, Transition Towns, Vermont Time Banks, Totnes Pound
- Value score: 8.5/10 | Citability: High | Hours: 20 | Start date: June 1

**Domain C: Skills Development and Knowledge Transmission** (20 hours)
- Covers apprenticeship, skill inventory, knowledge preservation against expert loss
- Makes Phase 5 executable (procedures are useless without trained people)
- Sources: Adult learning literature, skill-sharing networks, knowledge preservation case studies
- Value score: 8.2/10 | Citability: High | Hours: 20 | Start date: June 1

**Domain D: Governance Scaling** (20 hours)
- Covers constitutional design as community grows from 20→50→100→200 people
- Extends Phase 5 conflict resolution (this is the "next level up" question)
- Sources: Sociocracy, deliberative democracy, Mondragon evolution, kibbutz failure analysis
- Value score: 8.1/10 | Citability: High | Hours: 20 | Start date: June 1

**All three recommended?** Yes. These three are the Phase 6 Week 1 critical path. Together they address:
- **How do you organize?** (Domain D — governance)
- **How do you exchange value?** (Domain A — economics)
- **How do you build the people?** (Domain C — skills)

**Alternative selections**:
- If resource-constrained: Pick A (highest gap fill) + C (foundational)
- If governance-focused: Pick D + C (scaling + capability)
- If economic-focused: Pick A + D (economics + structure)
- **Least recommended**: Any single domain (they are interdependent; together they form a coherent arc)

**Execution ready**: ✅ All three domain outlines committed (May 27); research can begin June 1 immediately

**Recommendation**: **All three (A+C+D)**

---

## Decision Routing: What Happens After You Choose

### Scenario 1: Stockbot Option A + Phase 5 Option A + Phase 6 A+C+D (RECOMMENDED)
**June 1 Timeline**:
- May 27 afternoon: JPM ridge_wf training begins (2-3 hrs)
- May 28 morning: JPM training completes; Jetson deployment begins
- May 28-31: 4-session validation + risk aggregation verification
- June 1 06:00 UTC: COORDINATION MEETING
  - Confirm Phase 6 Domains A+C+D approved
  - Confirm Phase 5 Wave 1+2 publication on June 5
  - Stockbot 4-session deployment verified and cleared for live trading
- June 1-3: Phase 5 editorial cleanup
- June 1 afternoon: Phase 6 Domains A, C, D research begins (parallel execution)
- June 3-5: Phase 5 Wave 1+2 publication prep finalizes
- June 5: Phase 5 Wave 1+2 published (43,621 words)
- June 7-10: Phase 6 first-draft checkpoints (Domains A, C, D parallel deliverables)

**Resource loading**: 
- Stockbot: 3-4 hours (training + deployment validation)
- Systems-resilience: 20-25 hours Phase 5 (editorial) + 60 hours Phase 6 Week 1 (parallel research)
- **Total June 1-10 load**: Medium (publications overlap with research parallelization, no bottleneck)

**Contingency triggers**:
- If Jetson deployment fails May 28: fallback to Option B (config update, same-day deployment)
- If Phase 5 editorial slips: Phase 6 research continues independently (no blocking relationship)
- If Phase 6 Domain writer unavailable June 1: co-author recruitment (24h window, pre-identified candidates)

---

### Scenario 2: Stockbot Option B + Phase 5 Option B + Phase 6 A+C
**June 1 Timeline**:
- May 26-27: JPM config update (30 min) + Jetson deployment (15 min)
- May 27-28: 4-session validation complete
- June 1 06:00 UTC: COORDINATION MEETING
  - Confirm Phase 5 unified release schedule (publication June 15)
  - Confirm Phase 6 Domains A+C (Domain D deferred)
  - Stockbot deployment verified and cleared
- June 1-14: Phase 5 editorial integration (10-15 hours; master TOC, cross-references)
- June 1 afternoon: Phase 6 Domains A, C research begins (parallel, 20 hrs each)
- June 7-10: Phase 6 first drafts delivered
- June 15: Phase 5 full 66.4K corpus published

**Resource loading**:
- Stockbot: 1-2 hours total (minimal)
- Systems-resilience: 30-35 hours Phase 5 (editorial, sustained June 1-14) + 40 hours Phase 6 Week 1
- **Total June 1-10 load**: Heavy (editorial work + research overlap creates sustained 50+ hrs/week)
- **Contention risk**: HIGH — editorial bottleneck delays publication until June 15; Phase 6 research competes for same time budget

**Contingency triggers**:
- If editorial slips past June 1-14 window: Phase 5 publication delays to June 22 (pushes entire publication timeline)
- If Phase 6 writer unavailable June 1: reduces to 20 hours (Domain A only); Domain C deferred to Week 2

---

### Scenario 3: Stockbot Option A + Phase 5 Option C + Phase 6 A+C+D
**June 1 Timeline**:
- May 27: JPM ridge_wf training + deployment validation
- June 1 06:00 UTC: COORDINATION MEETING (all go decisions)
- May 30: Phase 5 Week 1 published (Playbook + Microgrids, ~15K words)
- June 1 afternoon: Phase 6 Domains A, C, D research begins
- June 6: Phase 5 Week 2 published (Psych Support + Conflict Resolution, ~18K words)
- June 1-30: Phase 5 rolling publication + Phase 6 parallel research both active

**Resource loading**:
- Stockbot: 3-4 hours
- Systems-resilience: 40-45 hours Phase 5 (rolling publication cycles) + 60 hours Phase 6 (parallel)
- **Total June 1-30 load**: Heavy (highest sustained load; 6-week rolling publication cycle)
- **Contention risk**: HIGHEST — publication cycles compete with Phase 6 research for same time budget

**Contingency triggers**:
- If publication cycle slips: ripple effect delays all subsequent weeks
- If Phase 6 research slips: can pause publications for sprint (reduces publication cadence temporarily)
- **Most fragile scenario**: Recommended only if publisher/promoter availability is guaranteed for full 6 weeks

---

## One-Click Recommendation

**RECOMMENDED PATH**: Stockbot Option A + Phase 5 Option A + Phase 6 A+C+D

**Why this path**:
1. **Stockbot Option A**: Aligns with original architecture specification; validates ridge_wf; cost of 2-3 hours is negligible given deployment is May 28-31 (not June 1)
2. **Phase 5 Option A**: Fastest community impact (June 5 vs. June 15); real feedback loop before Wave 3 finalization; lightest resource cost (20-25 hours vs. 30-35 or 40-45)
3. **Phase 6 A+C+D**: Three-domain arc is coherent and non-redundant; addresses the "trinity" of Phase 6 questions (govern, exchange value, build people)

**June 1-15 Resource Summary** (Option A all selections):
- Stockbot: 3-4 hours (May 28-31, no June contention)
- Systems-resilience: 85-100 hours total (20-25 Phase 5 editorial + 60 Phase 6 research), distributed as:
  - June 1-5: 20-25 hours (editorial + research setup)
  - June 6-15: 60 hours Phase 6 parallel (independent of Phase 5, no bottleneck)
- **No critical bottlenecks; Phase 5 publication clears June 5, Phase 6 research independent**

---

## How to Decide

**For each decision, pick one option**:

1. **Stockbot Lever B**: Option A (retrain ridge_wf) or Option B (config update)?
   - Pick A if: You want architecture diversity and validation of ridge_wf
   - Pick B if: You want immediate deployment with zero training risk
   - **Recommended**: Option A

2. **Phase 5 Publication**: Option A (staged), B (unified), or C (rolling)?
   - Pick A if: You want fast impact and real feedback loop
   - Pick B if: You want a single comprehensive reference artifact
   - Pick C if: You want sustained weekly engagement and have publication bandwidth for 6 weeks
   - **Recommended**: Option A

3. **Phase 6 Domains**: All three (A+C+D), subset, or different selection?
   - Pick all three if: You want coherent Week 1 launch covering governance/economics/skills
   - Pick A+C if: You want to start smaller (2 domains) and add D in Week 2
   - Pick different if: You have alternative priorities (see domain selection matrix)
   - **Recommended**: All three (A+C+D)

---

## Decision Template (For Your May 31 Meeting)

```
USER DECISIONS — May 31, 2026

1. Stockbot Lever B — JPM Model Type
   [ ] Option A: Retrain JPM ridge_wf (2-3 hrs, May 28-31 deployment)
   [ ] Option B: Config update to lgbm_ho (30 min, immediate deployment)

2. Systems-Resilience Phase 5 — Publication Timing
   [ ] Option A: Staged (Wave 1+2 June 5, Wave 3 June 30)
   [ ] Option B: Unified (Full 66.4K June 15)
   [ ] Option C: Rolling (Weekly pairs May 30+)

3. Systems-Resilience Phase 6 — Domain Selection
   [ ] All three: Domains A+C+D (Community Econ + Skills + Governance)
   [ ] Subset: A+C only (deferring Governance to Week 2)
   [ ] Subset: A only (deferring Skills and Governance)
   [ ] Different selection: [specify]

Decision timestamp: _____________
Approved by: _____________
```

---

## Reference Documents

| Document | Purpose | Location |
|----------|---------|----------|
| `OPTION_A_RIDGE_WF_RETRAIN_RUNBOOK.md` | Stockbot ridge_wf training execution | projects/stockbot/ |
| `OPTION_B_CONFIG_UPDATE_RUNBOOK.md` | Stockbot config-only execution | projects/stockbot/ |
| `PHASE_5_PUBLICATION_DECISION_FRAMEWORK.md` | Full Phase 5 analysis (Options A, B, C) | projects/systems-resilience/ |
| `JUNE_1_ACTIVATION_SUMMARY.md` | Phase 6 readiness + decision gate | projects/systems-resilience/ |
| `phase-6-selection-matrix.md` | All 10 Phase 6 domains compared | projects/systems-resilience/ |

---

**Created**: 2026-05-27 | **Decisions due**: 2026-05-31 23:59 UTC | **Execution target**: 2026-06-01 06:00 UTC
