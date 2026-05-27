---
title: "May 31 Consolidated User Decision Support"
subtitle: "All Three Major May 31 Decisions in One Place"
created: 2026-05-27
deadline: 2026-05-31 23:59 UTC
status: READY FOR USER REVIEW
decision_format: "Decision matrix + routing tree + contingency checklist"
---

# May 31 Consolidated Decision Support

> **For**: Anya's May 31 decision meeting
> **From**: Orchestrator (Session 1746)
> **Deadline**: May 31, 2026 23:59 UTC
> **What this is**: Single document consolidating all three major decisions due by May 31, with routing matrix showing how each decision combination affects June 1-15 timeline
> **What this enables**: June 1 06:00 UTC launch with zero decision delays

---

## Three Decisions Due May 31

| # | Decision | Options | Impact Scope | Deadline |
|---|----------|---------|--------------|----------|
| **1** | **systems-resilience Phase 5 publication timing** | Option A (staged June 1+30) / Option B (unified June 15) / Option C (rolling June 5+) | June 1-July 15; affects Phase 6 start window; determines author hiring timeline | May 31 23:59 UTC |
| **2** | **systems-resilience Phase 6 domain selection** | 1-3 domains from {A: Economic, C: Skills, D: Governance} | June 1-15 resource allocation; determines research sprint scope; 20h each domain | May 31 23:59 UTC |
| **3** | **stockbot Lever B deployment impact routing** | Already decided (retrain JPM ridge_wf) — routing to Timeline A/B/C based on pre-flight outcome (May 30) | June 1-15 resource contention with systems-resilience Wave 2 author hiring; determines Jetson expansion timing | May 30 AM pre-flight pass/fail determines routing (binary) |

---

## Decision #1: Phase 5 Publication Timing

### Three Options Summary

| Dimension | **Option A: Staged** | **Option B: Unified** | **Option C: Rolling** |
|-----------|:---:|:---:|:---:|
| **Release timing** | June 1 (43.6K words Wave 1+2) + June 30 (Wave 3) | June 15 (full 66.4K) | May 30 start, weekly through July 4 |
| **Editorial effort** | ~5 hours | ~12 hours | ~25 hours (cumulative) |
| **Reader onboarding ease** | High (43K is digestible) | Medium (66K is comprehensive) | Low (fragmented, requires active seeking) |
| **Feedback loop** | 4 weeks to revise Wave 3 | No revision post-publication | 6 weeks rolling, but complicates Wave 3 finalization |
| **Authority positioning** | "Two-volume reference" | "Definitive 66K guide" | "Weekly research drops" |
| **June resource impact** | Low (publication is light-touch) | Medium (10-15 hour editorial sprint June 1-14) | High (6 announcement cycles + feedback monitoring) |
| **Total score** | **30/40** | **24/40** | **27/40** |
| **Recommendation** | ✅ **RECOMMENDED** | | |

### Why Option A Wins

1. **June 1 impact**: Core practitioners get 43.6K words immediately — all highest-leverage content (energy, veterinary, psychological support, governance, execution playbook)
2. **Feedback velocity**: 4-week window to incorporate reader feedback into Wave 3 before June 30 publication
3. **Resource efficiency**: Two light-touch publication events vs. one heavy editorial sprint (Option B) or six announcement cycles (Option C)
4. **Author hiring flexibility**: Wave 1+2 publication June 1 doesn't block Phase 6 domain research from starting June 1 (they operate independently; Wave 2 author work happens June 10-July 10)
5. **Risk mitigation**: If Wave 3 has gaps discovered in June feedback, you have time to revise before June 30

### June Timeline Impact (Option A)

```
June 1:    Phase 5 Wave 1+2 published (43.6K words)
June 1-5:  Phase 6 domain research can start (independent of Wave 1+2 publication)
June 10:   Wave 2 author onboarding (if selected)
June 30:   Phase 5 Wave 3 published (22.8K words) + Wave 2 author production begins simultaneously
July 10:   Wave 2 author first draft checkpoint
July 15:   Wave 2 author final delivery; Phase 5 complete
```

---

## Decision #2: Phase 6 Domain Selection

### Three Recommended Domains (Choose 1-3)

All three domains can be researched **simultaneously** (no prerequisites on each other). Total research time: 20 hours each.

#### Domain A: Community Economic Resilience
- **Solves**: How communities coordinate exchange, resource distribution, compensation when markets fail
- **Extends**: Phase 5 community playbook (adds economic layer to governance)
- **Hours**: 20 (June 1-15)
- **Choose if**: Your Phase 5 answer to "how do we distribute resources fairly?" needs an economic framework
- **Precedent**: Elinor Ostrom commons work, Transition Towns, LETS systems, community currencies

#### Domain C: Skills Development & Knowledge Transmission
- **Solves**: How communities build, verify, and preserve practical competency across generations
- **Extends**: Phase 5 educational governance (adds adult skill development execution layer)
- **Hours**: 20 (June 1-15)
- **Choose if**: Your community realizes "we're concentrated expertise in 2-3 people" or "nobody under 30 knows how to [critical skill]"
- **Precedent**: Adult learning theory, apprenticeship literature, FEMA CERT training architecture

#### Domain D: Governance Evolution & Scaling
- **Solves**: What breaks in Phase 5 governance when community scales 20 → 50 → 100+ people
- **Extends**: Phase 5 conflict resolution + playbook (adds constitutional/scaling layer)
- **Hours**: 20 (June 1-15)
- **Choose if**: Your question is "our consensus model works at 20 people—what happens at 100?" or "we need founding documents"
- **Precedent**: Sociocracy, deliberative democracy, Mondragon cooperative scaling case studies

### Selection Matrix

| Scenario | Domains | Total Hours | June Capacity | Recommendation |
|----------|---------|:---:|:---:|---|
| **Solo** (1 domain) | Pick A OR C OR D | 20h | ✅ Fits easily in June 1-15 | Lower risk; allows author hiring focus |
| **Dual** (2 domains) | Pick A+C OR A+D OR C+D | 40h | ✅ Fits June 1-15 with parallel execution | Balanced; captures 2 dependency gaps |
| **Trio** (all 3) | A+C+D | 60h | ⚠️ Tight; requires all three researchers June 1-15 | Highest value; only feasible if author hiring deferred to June 15+ |

### Recommended Combination: Trio (A+C+D)

**Reasoning**:
- Phase 5 leaves all three gaps unfilled
- None of the three domains have prerequisites on each other (can parallelize)
- June 1-15 is a natural research sprint (14 days, 3 parallel researchers = 60 hours total)
- Phase 6 completion by June 30 would create a complete two-volume system (Phase 5 + Phase 6 = 10 documents addressing all community resilience domains)
- Author hiring happens June 10-30 (does not conflict with Phase 6 research)

**If resource-constrained**: Start with Domain D (Governance Evolution) as the most time-critical. Communities organizing under stress need scaling governance first; economics and skills are secondary.

---

## Decision #3: Stockbot Lever B Deployment Impact Routing

### Current Status

- **May 22 checkpoint outcome**: STILL_MISS_B2 (3 confirmed round trips, 0 AAPL sells)
- **Lever B decision**: EXECUTED (retrain JPM ridge_wf)
- **JPM model status**: Training complete, committed to git (commit `9d9ea41`)
- **Pre-deployment validation**: All 5 gates (G1-G5) passed
- **May 28 deployment**: Ready to execute

### May 30 Pre-Flight Binary Decision

**What determines Timeline A vs B**: Pre-flight outcome on May 30 AM

| Pre-Flight Result | Timeline | June 1 Status | June 1-15 Resource Impact |
|---|---|---|---|
| **PASS (paper → live approved)** | **Timeline A: Expansion GO** | 4-session AMZN/JPM activated June 1 | **HIGH contention**: 76 hours multi-ticker work + systems-resilience Phase 6 (60h) + Wave 2 author (if all three domains) |
| **FAIL (stay paper longer)** | **Timeline B: Option B1 (covered-call overlay)** | Alternative strategy activated; multi-ticker expansion deferred | **LOW contention**: 17 hours Option B1 implementation + systems-resilience Phase 6 (60h) = 77h total |

### Resource Contention Analysis

#### Timeline A (Expansion GO)
```
Stockbot June 1-15:        76 hours (4-session deployment, risk validation, live trading ops)
systems-resilience June 1-15:  60 hours (Phase 6 Domains A+C+D parallel research)
systems-resilience June 10-July 10: 80 hours (Wave 2 author if Option A chosen)
─────────────────────────────────────────
TOTAL June 1-15 hours:     76 + 60 = 136 hours (simultaneous)
June author capacity:      40-50 hours (typical human capacity per person)

CONTENTION RATING:         MEDIUM-HIGH
FEASIBILITY:               Possible if Wave 2 author work is 25% task switching (likely given orchestration review needs)
RISK FACTOR:               If pre-flight PASS but author unavailable, Jetson expansion proceeds alone (acceptable fallback)
```

#### Timeline B (Option B1)
```
Stockbot June 1-15:        17 hours (Option B1 covered-call implementation)
systems-resilience June 1-15:  60 hours (Phase 6 Domains A+C+D parallel research)
systems-resilience June 10-July 10: 80 hours (Wave 2 author if Option A chosen)
─────────────────────────────────────────
TOTAL June 1-15 hours:     17 + 60 = 77 hours (simultaneous)

CONTENTION RATING:         LOW
FEASIBILITY:               Comfortable fit; even with full Wave 2 author (80h/month), no bottleneck
RISK FACTOR:               Stockbot stays in paper trading 2-4 weeks longer; go-live pushed to late June
```

### Key Decision Insight

**Your Phase 5 / Phase 6 decision does NOT depend on the stockbot pre-flight outcome.**

Both Timeline A and Timeline B allow:
- Phase 5 Option A publication on June 1
- Phase 6 Domains A+C+D research June 1-15
- Wave 2 author onboarding June 10 (if author available)

The pre-flight outcome only determines **stockbot resource intensity** (76h vs 17h), not **whether Phase 6 can proceed**.

---

## Three-Decision Routing Matrix

Below are all 2×3×2 = 12 possible decision combinations and their June 1-15 impact.

### Template: (Phase 5 Option | Phase 6 Scope | Stockbot Timeline)

| Combination | Phase 5 | Phase 6 | Stockbot | Total June Hours | Contention | Recommendation |
|---|---|---|---|:---:|---|---|
| **1** | A | A+C+D | Timeline A (GO) | 136 | MEDIUM | ✅ Optimal if author available |
| **2** | A | A+C+D | Timeline B (B1) | 77 | LOW | ✅ Conservative; lower risk |
| **3** | A | Dual (D+C) | Timeline A | 96 | LOW | Alternative if author late |
| **4** | A | Solo (D) | Timeline A | 80 | LOW | Minimum; covers governance scaling |
| **5** | B | A+C+D | Timeline A | 150 | HIGH | ⚠️ Avoid (editorial sprint conflicts) |
| **6** | B | A+C+D | Timeline B | 87 | MEDIUM | Possible if author light-touch |
| **7** | B | Solo (D) | Timeline A | 90 | MEDIUM | Possible; trades Phase 6 scope for editorial polish |
| **8** | C | A+C+D | Timeline A | 165 | VERY HIGH | ❌ Not recommended |
| **9** | C | A+C+D | Timeline B | 102 | MEDIUM | Possible; requires careful orchestration |
| **10** | C | Solo (D) | Timeline A | 105 | MEDIUM | Possible; focuses on minimum Phase 6 |
| **11** | A | None | Timeline A | 76 | LOW | Defer Phase 6; focus stockbot + Wave 2 author |
| **12** | A | None | Timeline B | 17 | VERY LOW | Maximum flexibility; defer both Phase 6 and Jetson expansion |

### Recommended Path: Combination #1
**Decision**: Phase 5 Option A + Phase 6 Trio (A+C+D) + Timeline A (if pre-flight PASS)
- **Rationale**: Maximizes value (full Phase 6 plus June 1 publication) while remaining within reasonable contention (136h over 14 days is 10h/day across 2-3 researchers—feasible)
- **Contingency**: If pre-flight FAIL, automatically drop to Timeline B and reduce stockbot hours to 17h (drops total to 77h, very comfortable)

---

## Daily Execution Timeline: June 1-15 (Assuming Recommendation Accepted)

```
════════════════════════════════════════════════════════════════════
MAY 31 EVENING — User makes decision #1, #2, #3
════════════════════════════════════════════════════════════════════

JUNE 1, 06:00 UTC — Orchestrator activation
├─ Wave 1+2 publication checklist confirmed
├─ Phase 6 Domains A+C+D assigned to parallel researchers (Agent team spawning)
├─ Jetson infrastructure pre-flight preparation begins
└─ Systems-resilience notification to Wave 2 author candidate (if selected)

JUNE 1-5 — Wave 1 publication + Phase 6 research sprint begins
├─ systems-resilience: Phase 6 domain research underway (all three parallel)
├─ Wave 1+2 published June 1 (no further action needed)
├─ stockbot: Pre-flight observation phase (May 28-30 monitoring data reviewed)
└─ Wave 2 author: Standby mode (await June 10 confirmation)

JUNE 10 — Wave 2 author onboarding (if author confirmed available)
├─ Author receives research kit + outline + first 5 sources
├─ Author commits to June 10-July 10 production sprint
├─ systems-resilience: Phase 6 research checkpoint (mid-sprint review)
└─ stockbot: Pre-flight decision checkpoint (May 30 AM pre-flight outcome routing)

JUNE 15 — Phase 6 domain research completes
├─ Domains A, C, D first drafts delivered
├─ systems-resilience: Integration with Phase 5; begin Wave 3 light revision if Option A
├─ Wave 2 author: Week 1 production (Psychological Support Guide outline + research complete)
└─ stockbot: June 1-15 deployment checklist signed off

JUNE 30 — Wave 3 publication + Wave 2 author 50% checkpoint
├─ Phase 5 Wave 3 published (if Option A) OR preparation complete (if Option B)
├─ Wave 2 author: Halfway through production (50% draft completion)
├─ systems-resilience: Phase 6 domains integrated into Phase 5 (if proceeding to Phase 7 planning)
└─ stockbot: Live trading operations ongoing (if Timeline A + pre-flight PASS)

JULY 10 — Wave 2 author final delivery
├─ Psychological Support Guide + Conflict Resolution Guide complete
├─ Phase 5 + Phase 6 integration complete
├─ All Phase 5-6 work eligible for Q3 publication integration
└─ Phase 7 roadmap discussion (if user decides to continue)
```

---

## Contingency Triggers & Fallback Decisions

### If Pre-Flight FAILS on May 30

**Automatic routing**: Drop from Timeline A to Timeline B
- Stockbot hours drop from 76 to 17 (Option B1 covered-call overlay)
- Total June contention drops to 77 hours (very comfortable)
- Phase 5 Option A publication unchanged
- Phase 6 trio research unchanged
- **No user decision required** — orchestrator automatic routing

### If Wave 2 Author Unavailable on June 1

**Contingency options**:
1. **Option B2 (Co-author)**: Recruit identified co-author backup (Dr. Sarah Cho, Michael James, or Jennifer Park); split 50% + 50% workload June 10-July 10
2. **Option B3 (Self-execute)**: Orchestrator solo-writes Psychological Support + Conflict Resolution (40-50 hours, quality = 8/10 vs author-written 9.5/10)
3. **Defer**: Skip Wave 2 author in June; publish Wave 1+2 without Wave 2 polish; author work moves to July-August

**Default recommendation**: Option B2 (co-author) — lowest risk, maintains July 15 completion date

### If Phase 6 Research Scope Too Ambitious

**Automatic fallback**: Solo Domain D (Governance Evolution)
- Governance scaling is the most time-critical gap
- 20 hours fits any contention scenario
- Domains A and C can be deferred to July-August without blocking June milestones

---

## One-Page Decision Form

### Circle your answers (or copy into CHECKIN.md):

**Question 1 – Phase 5 Publication Timing**: Choose ONE
- [ ] **Option A (Staged)** — June 1 (Wave 1+2) + June 30 (Wave 3) ← RECOMMENDED
- [ ] **Option B (Unified)** — June 15 (full 66K)
- [ ] **Option C (Rolling)** — May 30-July 4 (weekly releases)

**Question 2 – Phase 6 Domain Selection**: Choose ONE or MORE
- [ ] **Domain A** (Community Economic Resilience)
- [ ] **Domain C** (Skills Development & Knowledge Transmission)
- [ ] **Domain D** (Governance Evolution & Scaling)
- [ ] **Trio recommendation** (all three A+C+D) ← RECOMMENDED
- [ ] **None** (defer Phase 6 to June 15+)

**Question 3 – Wave 2 Author Status** (decision by June 1):
- [ ] **Confirmed available** for June 10-July 10 production sprint
- [ ] **Conditional** (will confirm by June 5)
- [ ] **Unavailable** (will use co-author or defer)

**Stockbot Timeline** (automatic, based on May 30 pre-flight result):
- Pre-flight PASS → Timeline A (expansion GO)
- Pre-flight FAIL → Timeline B (Option B1 overlay)

---

## Orchestrator Readiness Checklist

- ✅ Phase 5 Wave 1+2 ready to publish June 1 (all 43.6K words committed, cover letter drafted)
- ✅ Phase 6 domain outlines complete; researchers standing by for June 1 assignment
- ✅ Stockbot pre-flight preparation complete; deployment playbooks staged
- ✅ Wave 2 author candidate briefing materials ready (research kit, outline, source list)
- ✅ All contingency playbooks staged (Option B1, co-author recruitment, Phase 6 fallback to solo Domain D)

**Status**: Ready for May 31 user decision. No blocking dependencies. June 1 06:00 UTC activation is go.

---

## Questions? Email responses due by May 31 18:00 UTC

If you have clarifying questions about any of the three decisions, please reply via:
- Email: wanka95@gmail.com
- Discord: #decisions channel
- Inline comments in this document

Orchestrator will incorporate clarifications into revised routing matrix by May 31 22:00 UTC.

---

**Document**: MAY_31_CONSOLIDATED_DECISION_SUPPORT.md
**Prepared by**: Orchestrator (Session 1746)
**Status**: PRODUCTION-READY FOR USER REVIEW
**Last updated**: 2026-05-27 17:15 UTC
