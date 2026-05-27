---
title: "Phase 5 Publication Timeline Impact Analysis"
project: systems-resilience
item: EXPLORATION_QUEUE Item 43
status: COMPLETE — awaiting user decision by May 31
decision_deadline: 2026-05-31
created: 2026-05-27
version: 1
purpose: "Timeline impact matrix + parallel execution + resource contention analysis for publication options A/B/C"
---

# Phase 5 Publication Timeline Impact Analysis

> Prepared May 27, 2026. User decision deadline: May 31, 2026.

---

## Section 1: Timeline Impact Matrix

This matrix covers June resource hours, author hiring windows, Phase 6 parallelization windows, Lever B deployment readiness, and Wave 2 author contingency activation for each of the three publication options.

---

### Option A: Staged — Wave 1+2 by June 5, Wave 3 by June 30 (Score 30/40, Recommended)

#### June Resource Hours

| Activity | Window | Estimated Hours | Owner |
|---|---|---|---|
| Wave 1+2 final editorial pass (frontmatter, cross-refs, master TOC) | June 1-3 | 8-10 | Orchestrator |
| Wave 1+2 publication logistics + announcement | June 3-5 | 3-5 | Orchestrator |
| Wave 1+2 reader feedback monitoring | June 5-20 | 4-6 (passive, distributed) | Orchestrator |
| Author onboarding sprint | June 1-9 | 12-15 | Orchestrator + Author |
| Author writing production | June 10-July 10 | 80-100 | Author (primary) |
| Wave 3 cross-reference editorial pass | June 15-25 | 8-12 | Orchestrator |
| Wave 3 frontmatter standardization + TOC | June 23-27 | 3-5 | Orchestrator |
| Wave 3 publication + announcement | June 28-30 | 2-3 | Orchestrator |
| **Total Orchestrator (June)** | — | **40-56 hours** | — |
| **Total Author (June)** | — | **80-100 hours** | — |

**Peak Orchestrator load**: June 1-5 (publication logistics concurrent with author onboarding). Estimated 15-20 hours in this single window — above sustainable single-week rate but bounded to five calendar days.

---

#### Author Hiring Timeline

| Gate | Date | Action |
|---|---|---|
| Author status confirmation | May 29 (outreach sent) | Confirm June 1 availability |
| Author acceptance deadline | May 30 | Accept or decline confirmed |
| Co-author contingency (if needed) | May 31 | Co-author recruited (Candidates: Dr. Sarah Cho, Michael James, Jennifer Park) |
| Onboarding sprint | June 1-9 | Briefing, research kit, outline, first-draft checkpoint |
| Full production writing | June 10-July 10 | 80-100 hours author capacity |
| Draft delivery | July 10 | Complete draft to Orchestrator |
| Peer review + revision | July 10-15 | Final quality pass |
| Joint publication (if timed with Wave 3) | July 15 | Optional — Wave 3 publishes June 30 per Option A timeline |

Note: Under Option A, Wave 3 publishes June 30. The Wave 2 author content is a separate undertaking from the Wave 3 editorial pass — they do not block each other. Wave 3 editorial (June 15-27) and Wave 2 author production (June 10-July 10) run concurrently without dependency.

---

#### Phase 6 Parallelization Window

Phase 6 framework completion is scheduled for May 31 (decision doc filed). The question is whether Phase 6 research can start June 5 simultaneously with Wave 1+2 publication, or must wait.

**Answer: Phase 6 can start June 1-5 in pre-production mode and full production from June 5.**

The Phase 6 framework is already complete: candidate outlines for Domains A, C, and D are committed, selection matrix and sequencing recommendation are filed. The only dependency is the user domain selection decision, which is due May 31.

Assuming May 31 decision is received:

| Phase 6 Activity | Earliest Start | Dependency on Option A |
|---|---|---|
| Domain A/C/D research agent briefing | June 1 | None — framework complete |
| Source library compilation (pre-production) | June 1-3 | None |
| First-draft production (Domains A, C, D parallel) | June 3-5 | None — no dependency on Wave 1+2 publication date |
| Domain first drafts complete | June 7-10 | None |
| Phase 6 integration document | June 15-August 30 | None |

**Key finding**: Under Option A, there is no genuine sequencing dependency between Wave 1+2 publication (June 3-5) and Phase 6 research start (June 1-5). Both can execute simultaneously. The wave publication requires ~15 hours of Orchestrator editorial work in June 1-5; Phase 6 requires a research agent, not the same bandwidth. They compete for Orchestrator coordination time (setup, handoffs, decisions) but not for writing-production hours.

---

#### Jetson Infrastructure / Lever B Readiness Checkpoint

Lever B decision window is May 27-31. Deployment window is May 28-June 1 (config-only path) or June 1-15 (if JPM retrain required).

| Lever B Scenario | Deployment Window | Hours | Impact on Option A |
|---|---|---|---|
| Config-only (accept lgbm_ho for JPM) | May 28-June 1 | ~17 hours | No conflict with Option A — Jetson work completes before Option A editorial begins June 1-3 |
| JPM retrain (ridge_wf) | June 1-June 15 | ~76 hours | Overlap with Option A June 1-5 editorial window — Orchestrator load spike manageable (stockbot subagent carries retrain; Orchestrator overhead ~5-8 coordination hours) |

**Verdict**: Lever B at either path does not block Option A. Config-only is cleanest (completes before Option A editorial starts). Retrain path creates June 1-5 coordination load but does not share writing resources.

---

#### Wave 2 Author Co-Author Contingency Windows

| Trigger | Date | Action | Impact on Option A |
|---|---|---|---|
| Author confirms | May 30 | Proceed with onboarding June 1-9 | None — Option A timeline intact |
| Author declines | May 30 | Co-author recruitment (3 candidates) | June 1-9 author onboarding shifts to co-author; timeline unchanged |
| No response by May 30 16:00 UTC | May 30 | Assume decline; activate co-author path | Same as above |
| Co-author also unavailable | May 31 | Self-execute fallback (Option B1/B2/B3) | Orchestrator writes guides June 10-July 10; 50+ hours; Wave 3 publication (June 30) unaffected |

Option A is the most resilient option for author contingency activation because the Wave 3 publication (June 30) and the author writing production (June 10-July 10) are on independent tracks. Author unavailability does not touch the June 5 or June 30 publication gates.

---

### Option B: Unified — Full 66,442-word Release June 15 (Score 24/40)

#### June Resource Hours

| Activity | Window | Estimated Hours | Owner |
|---|---|---|---|
| Cross-reference integration (Wave 3 → Wave 1+2 explicit links) | June 1-7 | 6-10 | Orchestrator |
| Master TOC across all 12 documents (66K words, 5 waves) | June 1-7 | 4-6 | Orchestrator |
| Frontmatter standardization (12 documents) | June 3-10 | 3-5 | Orchestrator |
| Final quality pass (Wave 3 structural consistency) | June 7-14 | 6-10 | Orchestrator |
| Publication logistics + announcement | June 13-15 | 3-5 | Orchestrator |
| Author onboarding sprint | June 8-20 | 12-15 | Orchestrator + Author |
| **Total Orchestrator (June)** | — | **22-36 hours editorial** | — |
| **Total Author (June)** | — | **40-60 hours (production starts June 20+)** | — |

Note: Option B's editorial load (22-36 hours) is lower than Option A's total Orchestrator hours in June, but it is concentrated in a single two-week window (June 1-14) with a hard deadline. Option B's 10-15 hour cross-reference integration is not optional — Wave 3 documents were written without explicit cross-references to Wave 1+2.

---

#### Author Hiring Timeline (Option B)

Under Option B, Wave 1+2 content is not public until June 15. The author cannot reference the published Wave 1+2 documents during their onboarding.

| Gate | Date | Action |
|---|---|---|
| Author status confirmation | May 29-30 | Same as Option A |
| Author acceptance deadline | May 30-31 | Same as Option A |
| Onboarding sprint | June 8-20 | Delayed by 7 days vs. Option A (Orchestrator is in editorial integration June 1-7) |
| Full production writing | June 20-July 20 | Starts 10 days later than Option A |
| Draft delivery | July 20 | 10-day slip vs. Option A |
| Publication | July 25+ | 10-15 days later than Option A author path |

**Key degradation**: Option B's editorial concentration in June 1-14 delays author onboarding by ~7 days and author writing production by 10 days. If author availability is constrained to June or has a July deadline, Option B creates unnecessary pressure.

---

#### Phase 6 Parallelization Window (Option B)

| Phase 6 Activity | Earliest Start | Notes |
|---|---|---|
| Domain A/C/D research agent briefing | June 1 | No dependency on publication option |
| First-draft production | June 1-5 | Research agent is independent of publication editorial track |
| Domain first drafts complete | June 7-10 | No dependency |

Phase 6 is not blocked by Option B. The editorial integration (June 1-14) uses Orchestrator coordination time, creating moderate contention if Phase 6 setup also requires Orchestrator decisions in June 1-5. Stagger: Phase 6 research agent briefed June 1; full Phase 6 activation decisions made June 2-3 in a single session.

---

#### Jetson Lever B (Option B)

Same analysis as Option A. Lever B timeline is independent of publication option.

---

### Option C: Rolling Modular — Weekly pairs starting May 30 (Score 27/40)

#### June Resource Hours

| Activity | Window | Estimated Hours | Owner |
|---|---|---|---|
| Per-week editorial pass + announcement (weeks 2-6) | June 6 - July 4 | 4-6 hours/week × 5 weeks = 20-30 | Orchestrator |
| Feedback monitoring + integration decision per pair | Ongoing | 2-3 hours/week × 5 weeks = 10-15 | Orchestrator |
| Author onboarding sprint | June 1-9 (or delayed to June 8-20) | 12-15 | Orchestrator + Author |
| Author production writing | June 10-July 10 | 80-100 | Author |
| **Total Orchestrator (June)** | — | **42-60 hours** | — |
| **Total Author (June)** | — | **80-100 hours** | — |

**Critical flag**: Option C has the highest Orchestrator hours in June of any option (42-60) because each weekly release pair requires a dedicated editorial cycle and promotion event. These cannot be batched and are distributed across 5 weeks.

---

#### Author Hiring Timeline (Option C)

Option C does not have a distinct author hiring advantage. Onboarding June 1-9, production June 10-July 10 is identical to Option A. However, the ongoing rolling-release coordination (2-3 hours/week monitoring) competes with author onboarding for Orchestrator attention in June 1-14.

---

#### Phase 6 Parallelization Window (Option C)

Option C creates the most Phase 6 contention of any option. Each weekly pair requires active Orchestrator promotion and feedback monitoring through July 4. This overlaps with Phase 6 Domain A/C/D first-draft review windows and integration work.

**Verdict**: Phase 6 can start June 1-5 (research agent is independent), but Orchestrator review of Phase 6 Domain first drafts (expected June 7-10) will compete with Option C's Week 2 publication cycle (June 6). This creates a scheduling conflict requiring explicit prioritization — Phase 6 domain reviews should be deferred to June 11-14 if Option C is selected.

---

## Section 2: Parallel Execution Feasibility Analysis

### Core Question: Can Phase 6 Start June 5 Simultaneously with Wave 1+2 (Option A)?

**Yes. Phase 6 research starts June 1-5 without conflict.**

The architecture is clean: Phase 6 research is writer-agent work (domain A, C, D research production). Wave 1+2 publication is Orchestrator editorial work (frontmatter, TOC, cross-references). These are different roles and different hours. The only shared resource is the Orchestrator's coordination bandwidth (scheduling, decisions, handoffs).

Estimated shared Orchestrator coordination demand June 1-5:
- Wave 1+2 editorial setup + publication logistics: 5-8 hours
- Phase 6 research agent briefing + domain activation: 2-3 hours
- Stockbot Lever B resolution (assuming config-only path): 3-5 coordination hours
- Open-repo Phase 5.1 post-merge deployment: 2-4 hours
- Resistance-research synthesis routing: 2-3 hours
- **Total Orchestrator coordination June 1-5**: 14-23 hours

This is tight but achievable in a 5-day window if decisions are batched into 1-2 sessions rather than spread across the week. The JUNE_PHASE_6_RESOURCE_ALLOCATION document estimated 18 hours/week Orchestrator coordination load for June 1-15, which aligns with this estimate.

---

### Resource Constraint: Single Orchestrator + Author (Hired June 1-9)

**If author is hired June 1-9, can Wave 2 production AND Phase 6 parallelization both proceed June 10-July 10?**

The honest answer is: yes, but not without explicit prioritization.

**What actually competes June 10-July 10:**

| Track | June 10-July 10 hours | Owner | Conflict with other tracks? |
|---|---|---|---|
| Wave 2 author production | 80-100 (author) + 15-20 (Orchestrator review/feedback) | Author + Orchestrator | LOW — author is self-directing with periodic Orchestrator feedback cycles |
| Phase 6 domain A/C/D drafts (started June 1-7) | If Domain first drafts complete June 7-10: integration + revision June 10-30 = 20-30 hours | Orchestrator + research agent | MEDIUM — Orchestrator review of Phase 6 domain drafts competes with author feedback cycles |
| Wave 3 editorial pass (Option A) | 8-12 hours + 2-3 publication hours | Orchestrator | MEDIUM — concentrated June 15-27, overlaps Wave 2 production and Phase 6 integration |

**The bottleneck is Orchestrator review cycles, not production capacity.** Authors write independently; research agents research independently. The Orchestrator becomes the constraint when it must simultaneously:
1. Review Wave 2 author draft sections (feedback turnaround 24-48 hours per checkpoint)
2. Review Phase 6 Domain A/C/D integration (consolidation editing + final passes)
3. Execute Wave 3 editorial pass (June 15-25)

**Recommended stagger (Option A chosen):**
- June 10-20: Priority to Wave 2 author onboarding + first-draft feedback. Phase 6 domain integration deferred to June 16+.
- June 16-25: Phase 6 integration concurrent with Wave 3 editorial pass — both are research-document work, different enough to avoid fatigue.
- June 25-July 10: Wave 2 author production continues; Phase 6 secondary domains (E, F, H) can begin if capacity allows.
- July 10-15: Wave 2 draft received; Orchestrator peer review. Phase 6 integration document starts.

This stagger means Phase 6 Domains A/C/D are complete by June 25-30, not June 10 as the aggressive scenario suggests. The difference is 15-20 days. This is acceptable — Phase 6 has no external publication deadline in June.

---

### Best-Case vs. Realistic-Case Timelines per Option

| Milestone | Option A Best Case | Option A Realistic | Option B Best Case | Option B Realistic | Option C Best Case | Option C Realistic |
|---|---|---|---|---|---|---|
| First content reaches readers | June 5 | June 6-7 | June 15 | June 15-17 | May 30 | May 30 |
| Full corpus available | June 30 | June 30 | June 15 | June 17-20 | July 4 | July 10-15 |
| Phase 6 Domain A/C/D first drafts | June 7-10 | June 10-14 | June 7-10 | June 10-14 | June 7-10 | June 11-15 |
| Wave 2 author draft complete | July 10 | July 12-15 | July 20 | July 22-25 | July 10 | July 12-15 |
| Phase 6 integration complete | August 30 | September 5-10 | August 30 | September 5-10 | September 15-20 | October 1 |

The realistic-case differences between Option A and Option B converge for Phase 6 (both land August 30-September 10). The main divergence is corpus availability: Option A puts 43K words in reader hands on June 5-7; Option B puts 66K words in reader hands June 15-20.

---

## Section 3: Resource Contention Analysis

### Active June Resource Demands (All Projects)

The following demands are pulling on shared Orchestrator + agent capacity in June 2026:

| Demand | Window | Hours | Agent Type | Conflict Risk |
|---|---|---|---|---|
| Systems-resilience Wave 1+2 publication (Option A) | June 1-5 | 13-15 Orchestrator | Orchestrator | Moderate (peaks June 1-5) |
| Systems-resilience Wave 3 editorial + publication | June 15-30 | 13-18 Orchestrator | Orchestrator | Low (spread across 15 days) |
| Systems-resilience Wave 2 author (writing) | June 10-July 10 | 80-100 Author + 15-20 Orchestrator | Author + Orchestrator | Low (author-driven; Orchestrator feedback cycles 3-4 per month) |
| Phase 6 Domains A/C/D production | June 1-25 | 60 research agent + 15-20 Orchestrator review | Research agent + Orchestrator | Moderate (Orchestrator review June 10-25) |
| Stockbot Lever B expansion (config-only path) | May 28-June 1 | 17 total | Stockbot subagent | Very Low (resolves before June 1) |
| Stockbot Lever B expansion (retrain path) | June 1-15 | 76 total | Stockbot subagent + 5-8 Orchestrator | Low (subagent-driven; Orchestrator overhead minimal) |
| Open-repo Phase 5.1 post-merge deployment | June 1-15 | 21 total | Engineering subagent | Very Low (no shared resources with systems-resilience) |
| Resistance-research Phase 2 distribution | May 28-June 15 | 8-12 research agent | Research agent | Low-Moderate (research agent overlap with Phase 6 June 1-15) |

---

### Can All Three Projects Proceed Simultaneously in June?

**Three projects = Systems-resilience publication + Stockbot Lever B + Open-repo Phase 5.1.**

**Verdict: Yes, all three can proceed simultaneously in June, with one qualified caveat.**

The resources do not directly collide because:
- Stockbot Lever B uses a stockbot subagent (or Orchestrator for config changes only). Under the config-only path (17 hours), it is complete by June 1. Under the retrain path (76 hours), the Jetson does the compute; the Orchestrator touches it for 5-8 coordination hours.
- Open-repo Phase 5.1 post-merge deployment is engineering-only (libzim wheel deployment, alembic upgrade, manual ZIM test). No research agent, no writing agent. 21 hours, engineering subagent only.
- Systems-resilience publication uses the Orchestrator for editorial passes and a research agent for Phase 6 domain production.

The **one genuine bottleneck** is the Orchestrator coordination bandwidth in June 1-10. All four concurrent work streams (stockbot, open-repo, resistance-research synthesis routing, systems-resilience publication) require Orchestrator decisions and setup in this same window. JUNE_PHASE_6_RESOURCE_ALLOCATION estimated 18-25 Orchestrator coordination hours for June 1-15.

**Mitigation**: Batch all June 1 decisions into a single session. The JUNE_PHASE_6_RESOURCE_ALLOCATION document already flags this: "single June 1 decision session covering all 4 pending items." This converts 4 separate coordination spikes into one.

---

### Which Option Minimizes June Contention?

| Metric | Option A | Option B | Option C |
|---|---|---|---|
| Peak Orchestrator hours (June 1-10) | 15-20 concentrated, then drops | 18-25 sustained through June 14 | 14-20 per week sustained 6 weeks |
| Research agent conflicts (Phase 6 vs. resistance-research) | MEDIUM (June 1-15 overlap, staggerable) | MEDIUM (same) | HIGH (ongoing 6-week overlap) |
| Total June Orchestrator hours | 40-56 | 22-36 editorial + 15-20 author coordination = 37-56 | 42-60 |
| Flexibility to absorb unexpected delays | High — two independent publication gates | Low — single gate; delay pushes to July | Very Low — weekly cadence; one slip compounds |

**Option A minimizes contention better than Option B or C because:**
1. The June 1-5 editorial peak is bounded — it ends. By June 6, the Orchestrator is in monitoring mode (passive) for Wave 1+2 feedback.
2. The Wave 3 editorial pass (June 15-25) is 8-12 hours spread over 10 days, compatible with concurrent Wave 2 author feedback cycles.
3. If any one task slips, the other tasks are not immediately blocked.

**Option B concentrates risk**: the June 1-14 window requires 22-36 hours of editorial integration, and any slip pushes the single publication gate into July. Under Option B, if the Orchestrator needs to allocate 5-8 hours to Stockbot retrain coordination in June 1-10, the June 15 editorial deadline is at risk.

**Option C creates the highest sustained load**: 5-6 consecutive weeks of editorial cycles and promotion events, running concurrently with Wave 2 author production, Phase 6 domain integration, and (potentially) resistance-research Phase 2 monitoring. Option C is not recommended on resource grounds alone.

---

### Which Option Maximizes Parallelization?

**Option A maximizes parallelization** because it front-loads publication (Wave 1+2 June 5) and then allows the rest of June to run in true parallel:

- Phase 6 Domains A/C/D: research agent, June 1-25
- Wave 2 author production: author, June 10-July 10
- Wave 3 editorial: Orchestrator, June 15-25 (8-12 hours, compatible with author feedback cycles)
- Stockbot monitoring: stockbot subagent, ongoing
- Open-repo deployment: engineering subagent, June 1-15

After June 10, all five work streams are running on separate tracks with minimal shared Orchestrator demand. This is the closest approximation to full parallel execution achievable across the June portfolio.

---

## Section 4: Decision Support Recommendations

### Weighted Analysis: Option A June Resource Cost vs. Options B/C

Option A's total June Orchestrator cost (40-56 hours) appears higher than Option B's editorial-only cost (22-36 hours). This comparison is misleading. The true comparison is:

**Option A June Orchestrator cost (total)**: 40-56 hours
**Option B June Orchestrator cost (total)**: 22-36 editorial + 15-20 author coordination + 3-5 publication logistics = 40-61 hours

When author coordination is included, Option B's total June Orchestrator load is comparable to or slightly higher than Option A. Option B does not save June hours — it just sequences them differently, and at higher risk because the editorial load is concentrated into a mandatory 14-day window.

**Net score on resource efficiency**: Option A is marginally better.

---

### Recommendation: Option A, with Explicit June Stagger

**Option A is recommended** for the following reasons, each grounded in the resource analysis above.

**1. Phase 6 can start June 1, regardless of publication option.** The Phase 6 framework is complete. Domain A/C/D research can activate June 1 whether Option A, B, or C is chosen. Publication timing does not gate Phase 6. This removes one of the most common objections to staged publication (the concern that Wave 1+2 publication somehow delays Phase 6).

**2. Option A creates the most available June parallelization window.** After the June 1-5 editorial peak, the Orchestrator drops to passive monitoring mode for Wave 1+2 feedback. The remaining June weeks (June 6-30) can sustain parallel work on Phase 6 domains, Wave 3 editorial, Wave 2 author feedback, and other projects without competition for the same resources at the same time.

**3. Option A's risk is bounded. Option B's risk is not.** Option A has two independent publication gates (June 5, June 30). If June 5 slips to June 8, nothing downstream is affected — the June 30 gate stands independently. If Option B's June 15 gate slips to June 20, the entire corpus is delayed. In a June with high concurrent demand (stockbot, open-repo, resistance-research), Option A's buffered structure is operationally superior.

**4. The 30/40 score difference over Options B and C reflects real advantages**, not arbitrary weighting. Option B's only advantages are unified corpus coherence (valid) and single distribution event (operationally convenient but not mission-critical). Both of these can be partially recovered within Option A: include a "Volume 2 coming June 30" note in the Wave 1+2 release, and promote Wave 3 actively as the second distribution event.

**5. Option C is not recommended.** The 6-week rolling cadence requires sustained Orchestrator attention that is incompatible with the concurrent Phase 6 production, Wave 2 author onboarding, and other active projects. The incremental quality gains (targeted audience routing, iterative feedback) do not justify the 6-8 week execution tail.

---

### Recommendation on Phase 6 Start

**Start Phase 6 June 1 regardless of which publication option is selected.**

The Phase 6 framework is ready, domain selection is due May 31, and research agents do not compete with editorial bandwidth. The only constraint is Orchestrator setup time (2-3 hours for briefing and activation), which can be absorbed in the June 1 decision session.

If user selects Domains A + C + D (all three, parallel): 60 total hours, research agent(s) June 1-25. Orchestrator review of domain drafts: June 10-15 (Option A) or June 10-14 (Option B). Either way, Phase 6 domain first drafts complete before Wave 3 editorial begins.

---

### Recommendation on Author Contingency Resilience

**Option A is the most resilient publication option if the Wave 2 author is unavailable.**

Under Option A:
- Author unavailability affects only the Wave 2 guide content (psychological support, conflict resolution second versions), not the Wave 1+2 or Wave 3 publication timelines.
- June 5 and June 30 publication gates are independent of author availability.
- The self-execute fallback (Orchestrator writes both guides, 50+ hours) fits within the June 10-July 10 window without compressing any other June gate.

Under Option B:
- Author unavailability forces the Orchestrator to simultaneously manage the June 1-14 editorial integration AND the author contingency decision in the same window.
- Higher cognitive load, higher risk of editorial quality degradation.

Under Option C:
- Author unavailability plus 6 weeks of rolling publication equals the highest sustained coordination burden of any combination.

**If there is any doubt about author availability**, Option A provides the cleanest contingency structure.

---

### Option-Specific Contingencies Summary

| Scenario | Option A Response | Option B Response | Option C Response |
|---|---|---|---|
| Author unavailable | Self-execute June 10-July 10; publication gates unaffected | Self-execute; added to June 1-14 editorial load | Self-execute + ongoing weekly releases = highest load |
| Stockbot retrain required (76h) | No impact; retrain runs on Jetson, June 1-15, independent track | Mild Orchestrator competition June 1-10 with editorial integration | No impact on rolling schedule |
| Phase 6 domain selection delayed to June 3 | No impact; research agent activated June 3-5 | No impact | No impact |
| Wave 1+2 release receives critical gap feedback | Wave 3 can absorb feedback (June 15-25 editorial window open) | No revision window — corpus already locked by June 15 | Per-pair feedback integration possible but operationally demanding |
| Open-repo Phase 5.2 requires Orchestrator decision June 1-5 | Batch into June 1 session; tolerable | Same | Same |
| Resistance-research synthesis activates strong-signal Phase 2 | Research agent overlap June 1-15 managed by stagger (resistance sprint ends by June 5) | Same | HIGH risk — concurrent with all rolling releases |

---

## Decision Summary

| Criterion | Winner | Rationale |
|---|---|---|
| Publication impact speed | Option A | 43K words available June 5 vs. June 15 (B) or May 30 (C start, but tail extends to July) |
| Phase 6 acceleration | Tie (A/B) | Phase 6 can start June 1 under any option; publication timing is not the gate |
| June resource constraints | Option A | Bounded peak June 1-5; drops to passive after Wave 1+2 publish; most parallelization window June 6-30 |
| Author contingency resilience | Option A | Two independent publication gates; author unavailability affects only guide production, not corpus publication |
| Corpus coherence | Option B | Single release, single URL — but partially recoverable in Option A via "Volume 2" announcement |
| Overall | Option A | Recommended (30/40 score reflects genuine advantage on 5 of 8 attributes) |

**User decision prompt**:

- Select Option A: Confirm no Wave 3 content additions needed before June 30. Confirm author status by May 30. Phase 6 domain selection due May 31.
- Select Option B: Confirm 10-15 hours editorial integration capacity available June 1-14. Confirm June 15 is a hard publication commitment.
- Select Option C: Confirm 6 consecutive weeks of weekly editorial and promotion capacity through July 4.

---

*Created: 2026-05-27 | Status: COMPLETE — awaiting user decision by 2026-05-31 | Prepared for: EXPLORATION_QUEUE Item 43*
