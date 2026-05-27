---
title: "Phase 6 Orchestrator Burn Forecast — June 1 to July 15"
project: systems-resilience
phase: 6
status: DECISION-SUPPORT — input to June 1 scheduling decisions
decision_deadline: 2026-05-31
activation_target: 2026-06-01
created: 2026-05-28
session: 1711
purpose: "Quantify Orchestrator load June 1–July 15 under Phase 6 execution. Three scenarios plus concurrent project interactions. Scheduling recommendations and calendar template."
source_data:
  - RESOURCE_CONTENTION_ANALYSIS.md
  - PARALLEL_EXECUTION_FEASIBILITY.md
  - JUNE_PHASE_6_RESOURCE_ALLOCATION.md
companion_docs:
  - PHASE_6_DOMAIN_SELECTION_TOOLKIT.md
  - PHASE_6_GO_LIVE_CHECKLIST.md
---

# Phase 6 Orchestrator Burn Forecast — June 1 to July 15

> Lead finding: Sustainable Orchestrator capacity is 20–25 hours/week. Under Option A publication and solo or A+C domain selection, June 1–15 peaks at 24–33 hours/week but drops sharply after June 5. Under Option B publication with two-domain Phase 6, June 1–14 is dangerous (38–52 hours/week combined demand). The scheduling recommendation: adopt Option A publication, select Phase 6 domains from A or A+C, and defer Governance Scaling to September. Every scenario is detailed below.

---

## 1. Parallel Execution Model

Phase 6 execution involves three simultaneous tracks for the first six weeks. Understanding the ownership split is essential for burn estimation.

**Track 1: Author writing (author-owned)**  
The external author produces 38,000–45,000 words of domain content between June 10 and August 9. The author works independently with the source library and pre-research foundation. Orchestrator interaction is limited to: onboarding (June 1–9, 12–15 hrs total), checkpoint reviews (4 reviews at June 29, July 13, July 27, August 9), and response to ad-hoc scope or source questions (estimated 1–2 hrs/week during production).

Orchestrator load from author management: 12–15 hrs (onboarding) + 3–5 hrs per checkpoint (4 checkpoints) + 1–2 hrs/week (ad-hoc) = 26–31 hrs over 9 weeks. This averages 3–3.5 hrs/week of Orchestrator time — below the noise floor of weekly planning.

**Track 2: Research agent production (research agent-owned)**  
The Phase 6 research agent handles source library compilation, pre-research completion, and first-draft section writing for the selected domain(s). The research agent does not require Orchestrator coordination during production sprints — it operates independently given a briefing. Orchestrator interaction points: domain briefing (June 1–3, 2–3 hrs), first-draft review (June 10–15, 8–12 hrs), integration review (June 15–25, 10–15 hrs).

Orchestrator load from research agent management: 20–30 hrs over June, dropping to near-zero in July as the agent reaches production steady-state.

**Track 3: Phase 5 publication execution (Orchestrator-owned)**  
Under Option A: editorial peak June 1–5 (13–18 hrs), then drops to monitoring. Under Option B: editorial window June 1–14 (26–39 hrs total). Under Option C: 6–9 hrs/week sustained through July 4.

This track competes directly with Tracks 1 and 2 for Orchestrator capacity in June 1–15. It is the primary contention driver.

**The force multiplier**: Once the author is in production (June 10), the research agent and author are generating ~50,000–65,000 words of domain content per month with minimal Orchestrator load. The Orchestrator functions as a reviewer and quality gate, not a producer. This is the efficient state. The goal is to reach it by June 10 without crashing quality in the June 1–9 ramp.

---

## 2. Weekly Burn Breakdown by Scenario

Orchestrator hours only (research agent and author hours are separate; their time does not limit Orchestrator capacity).

### Scenario 1: Option A Publication + Solo Economic Resilience (Lowest Burn)

This is the recommended scenario: earliest Phase 5 publication, lowest Phase 6 ramp contention, author starts June 10 at full confidence.

| Week | Phase 5 pub | Phase 6 setup/review | Author onboarding | Other projects | Orch total | Capacity status |
|---|---|---|---|---|---|---|
| **June 1–7** | 13–18 (editorial peak) | 2–3 (domain briefing) | 6–8 (onboarding sprint) | 3–6 (stockbot + rr) | **24–35** | ABOVE SUSTAINABLE — manageable, bounded |
| **June 8–14** | 2–4 (monitoring) | 8–12 (first-draft review) | 4–6 (source list review, outline review) | 0–2 (rr monitoring) | **14–24** | AT CAPACITY |
| **June 15–21** | 8–12 (Wave 3 editorial) | 10–15 (integration work) | 2–3 (author feedback cycle 1) | 0 | **20–30** | AT/ABOVE CAPACITY — concentrated mid-June spike |
| **June 22–30** | 6–10 (Wave 3 pub) | 4–6 (domain steady state) | 3–5 (author feedback) | 0 | **13–21** | WITHIN CAPACITY |
| **July 1–7** | 0 | 3–5 (research agent domain review) | 2–3 (author check-in) | 0 | **5–8** | WELL BELOW CAPACITY |
| **July 8–15** | 0 | 0 | 3–5 (checkpoint prep: June 29 review) | 0 | **3–5** | WELL BELOW CAPACITY |
| **June total** | 29–44 | 24–36 | 15–22 | 3–8 | **71–110** |

Note: June 15–21 has a secondary spike from the overlap of Wave 3 editorial (under Option A, Wave 3 publishes June 30) and Phase 6 integration work. This overlap is manageable — the two tracks are distinct document sets — but it means June 15–21 is not a low-demand week. Plan for it.

**Peak hours in a single week (worst case)**: June 1–7, 35 hours. This is a 40% overrun above sustainable 25-hour capacity. It is bounded to 7 days and drops after June 5 when the editorial peak resolves.

### Scenario 2: Option A Publication + A+C (Economic + Skills) — Recommended Two-Domain

Adding Domain C (Skills Development) increases Orchestrator load modestly in June but significantly in July, because the second domain's first-draft review lands in the July window when Scenario 1 would be in low-demand recovery.

| Week | Phase 5 pub | Phase 6 Econ | Phase 6 Skills | Author mgmt | Other | Orch total | Status |
|---|---|---|---|---|---|---|---|
| **June 1–7** | 13–18 | 2–3 | 2–3 | 6–8 | 3–6 | **26–38** | ABOVE SUSTAINABLE |
| **June 8–14** | 2–4 | 8–12 | 6–9 (source sprint review) | 4–6 | 0–2 | **20–33** | AT/ABOVE CAPACITY |
| **June 15–21** | 8–12 | 10–15 | 3–5 (first-draft briefing) | 2–3 | 0 | **23–35** | ABOVE CAPACITY |
| **June 22–30** | 6–10 | 4–6 | 8–12 (Skills first-draft review) | 3–5 | 0 | **21–33** | ABOVE CAPACITY |
| **July 1–7** | 0 | 3–5 | 10–15 (Skills integration) | 4–6 | 0 | **17–26** | AT CAPACITY |
| **July 8–15** | 0 | 3–5 (Econ checkpoint prep) | 3–5 | 5–8 (Econ June 29 checkpoint review — 4–5 hrs) | 0 | **11–18** | WITHIN CAPACITY |

The A+C two-domain scenario sustains above-capacity demand through June 22–30 and into early July. It does not reach the dangerous single-week peaks of Option B, but it is persistently elevated. This is manageable if: (a) the author is productive and not generating high-frequency questions, and (b) the research agent for Domain C does not require intensive Orchestrator debugging during the source sprint.

**Peak hours in a single week (worst case)**: June 1–7, 38 hours. Same peak week as Scenario 1, slightly elevated by Skills domain briefing.

### Scenario 3: Option A Publication + A+D (Economic + Governance) — Higher Burn

Domain D (Governance Scaling) has the highest Orchestrator load of the three candidates because of the 8–10 day source sprint, scope management overhead, and weekly scope audits.

| Week | Phase 5 pub | Phase 6 Econ | Phase 6 Gov | Author mgmt | Other | Orch total | Status |
|---|---|---|---|---|---|---|---|
| **June 1–7** | 13–18 | 2–3 | 4–6 (extended source sprint management) | 6–8 | 3–6 | **28–41** | ABOVE CAPACITY |
| **June 8–14** | 2–4 | 8–12 | 8–12 (Gov source sprint + early sections) | 4–6 | 0–2 | **22–36** | ABOVE CAPACITY |
| **June 15–21** | 8–12 | 10–15 | 6–9 (Gov first-draft review + scope audit 1) | 2–3 | 0 | **26–39** | SIGNIFICANTLY ABOVE |
| **June 22–30** | 6–10 | 4–6 | 8–12 (Gov integration + scope audit) | 3–5 | 0 | **21–33** | ABOVE CAPACITY |
| **July 1–7** | 0 | 3–5 | 10–15 (Gov full production review) | 4–6 | 0 | **17–26** | AT CAPACITY |
| **July 8–15** | 0 | 3–5 | 8–12 (Gov scope audit 2) | 5–8 | 0 | **16–25** | AT/ABOVE CAPACITY |

The A+D scenario has no recovery window until after July 13 (when Governance Scaling reaches steady-state production). For the full first six weeks, Orchestrator demand is at or above sustainable capacity. This is the scenario most at risk of quality degradation — not from capacity collapse, but from accumulated context-switching overhead and the inability to give any single project extended focused attention.

**Peak hours in a single week (worst case)**: June 15–21, 39 hours. This is the most dangerous week: Wave 3 editorial, Phase 6 Economic integration, and Phase 6 Governance scope review all land simultaneously.

### Option B Publication Warning

Under Option B publication, the June 1–14 editorial integration window (26–39 hrs Orchestrator over 14 days) stacks on top of all Phase 6 setup demands. Combined peak weeks under Option B + A+C:

| Week | Combined demand | Status |
|---|---|---|
| June 1–7 | 35–52 hours | CRITICAL — above sustainable capacity by 2× |
| June 8–14 | 38–57 hours | CRITICAL |
| June 15–21 | 15–27 hours | RECOVERS sharply after June 15 publication |

Option B with two-domain Phase 6 creates a genuine two-week period where Orchestrator demand consistently exceeds capacity. Quality degradation risk is real in this scenario. This is documented in `RESOURCE_CONTENTION_ANALYSIS.md` (Section 2). Strongly recommend against combining Option B publication with two-domain Phase 6 selection.

---

## 3. Concurrent Project Interactions

### Seedwarden Phase 3 Hiring (June 22–July 13 per project status)

Seedwarden Phase 3 (seven files verified, June 22–July 13 execution window per ORCHESTRATOR_STATE.md) requires Orchestrator hiring infrastructure similar to Phase 6 author hiring. Timing interaction:

- If Seedwarden Phase 3 hiring activates June 22, it adds approximately 8–12 hours of Orchestrator hiring/onboarding load in the June 22–July 5 window.
- Under Scenario 1 (solo Economic Resilience), this window is manageable — Orchestrator is at 13–21 hours/week June 22–30.
- Under Scenario 2 (A+C), June 22–30 is already 21–33 hours. Adding 8–12 hours from Seedwarden hiring brings the week to 29–45 hours — above sustainable capacity.

**Scheduling recommendation**: If Seedwarden Phase 3 and Phase 6 two-domain selection are both active, defer Seedwarden Phase 3 hiring start by 1 week (to June 29 or July 6). This preserves a recovery window between Phase 6 June 22–28 peak and Seedwarden Phase 3 July 1–13 hiring sprint.

### Resistance-Research Phase 2 Execution (May 28–June 5 sprint)

The resistance-research May 28 distribution sprint (Domain 56/39, per ORCHESTRATOR_STATE.md) peaks May 28–June 5 and drops to monitoring by June 8. Interaction with Phase 6:

- The May 28–June 5 sprint is almost entirely within the author outreach/onboarding window, not the Phase 6 research ramp.
- Orchestrator demand from resistance-research: 6–10 hours (sprint), then passive monitoring 2–4 hours June 5–15.
- No genuine conflict with Phase 6 ramp. Minor schedule pressure June 1–3 (three parallel tracks: resistance-research sprint ending, Phase 5 editorial peak starting, Phase 6 briefing starting). Batch these into a June 1 decision session to minimize context-switching.

### Stockbot Lever B Deployment (May 28–June 15)

Stockbot Lever B (JPM model decision + deployment) has two paths: config-only (3–5 Orchestrator hours, completes by June 1) or retrain (5–8 Orchestrator hours over June 1–15). Both paths are documented in `RESOURCE_CONTENTION_ANALYSIS.md` (Section 4).

Under config-only path: Stockbot is resolved before Phase 6 ramp begins. Zero interaction.

Under retrain path (if selected): 5–8 hours of Orchestrator coordination spread June 1–15. This adds to the June 1–7 peak week but does not compound any other scenario materially. Under Option A + solo Economic Resilience, retrain adds a maximum 1–2 hours/day in June 1–7, bringing peak day from approximately 5 hours to 6–7 hours. Manageable.

Scheduling interaction for retrain path: Batch Stockbot retrain coordination into the June 1 morning decision session. If retrain is activated, the Orchestrator coordination tasks (model validation decisions, deployment configuration) are scheduled for June 2–4 mornings before Phase 5 editorial work. Do not interleave Stockbot and Phase 5 editorial in the same work block.

---

## 4. Scheduling Recommendations (June 1–15)

These recommendations minimize context-switching and protect quality in the peak window.

**Recommendation 1: June 1 is a single decision day, not an execution day.**  
Every pending decision (Phase 5 publication option, Phase 6 domain selection, author onboarding start, Stockbot Lever B config decision, open-repo Phase 5.2 path) lands on June 1. Batch them into a single 2-hour decision session. Dispatch each track after decisions are made. Do not attempt to execute Phase 5 editorial, Phase 6 briefing, and Stockbot simultaneously on June 1.

**Recommendation 2: Phase 5 editorial gets June 1–5 priority.**  
Under Option A, the June 5 publication is the hardest deadline in the June 1–15 window. It gates Wave 1+2 reader access and frees the Orchestrator for Phase 6 review. Protect this track. All other June 1–5 work is secondary.

**Recommendation 3: Phase 6 domain briefing on June 2–3, not June 1.**  
The research agent briefing (2–3 hours) does not need to happen on June 1. Scheduling it June 2–3 eliminates one context switch on the busiest day. The research agent can begin source library compilation June 3; domain first drafts begin June 7–10 regardless of a 1-day briefing slip.

**Recommendation 4: Author onboarding is asynchronous June 1–4.**  
Send the onboarding email and file package June 1. The author reads and reviews June 1–4 independently. Orchestrator interaction begins June 5 (source list questions) and June 8–9 (research outline review). This stacks author onboarding in the low-demand June 5–9 window, not the June 1–5 editorial peak.

**Recommendation 5: Defer Governance Scaling scope audit 1 to June 22 (not June 15).**  
If Domain D is selected, the first scope audit is recommended at Week 3 of production (approximately June 22 rather than June 15). This avoids stacking the scope audit on top of Wave 3 editorial (which also runs June 15–25 under Option A). One-week deferral of the audit does not materially affect scope management — the first production sprint (June 15–22) is the highest-momentum period; auditing during production disrupts less than auditing just as production begins.

**Recommendation 6: Pause open-repo Phase 5.3 through June 15.**  
Open-repo Phase 5.2 Wave 1 is merged (per ORCHESTRATOR_STATE.md). Phase 5.3 (if planned) should not activate until June 16 at earliest. No engineering decisions should be queued for the June 1–15 window. Defer all open-repo Phase 5.3 planning to the June 16–20 period when Orchestrator capacity recovers.

---

## 5. Team Context: Author as Force Multiplier

The author changes the June–August economics materially. Without an author, the Orchestrator must produce the domain document itself (50–60 Orchestrator hours for a 45,000-word document). With a qualified author, the Orchestrator provides 12–15 hours of onboarding and 12–20 hours of checkpoint reviews — 24–35 total hours versus 50–60 hours self-produced.

The net saving is 15–35 Orchestrator hours per domain. For two domains, the saving is 30–70 hours. This is the equivalent of 3–4 additional weeks of Orchestrator capacity reallocated to other project work.

**How to maximize this force multiplication:**

Invest in onboarding quality, not quantity. The most common error in author-assisted production is under-investing in the first week (scope alignment, source verification, research outline) and over-investing in late-stage corrections. A research outline that takes 2 hours to review on June 9 prevents 10 hours of revision at the July 13 checkpoint. The first-week investment has the highest ROI of any Orchestrator time in the author engagement.

Give feedback at checkpoints, not continuously. Authors produce best when they have extended uninterrupted production windows. Checkpoint reviews (June 29, July 13, July 27, August 9) concentrate Orchestrator feedback into four predictable events. Ad-hoc feedback between checkpoints should be reserved for factual errors or scope violations only — not structural suggestions or style preferences.

Trust the pre-research foundation. The Phase 6 domain candidate files and pre-research chapters are comprehensive enough that the author can produce the first 10,000–15,000 words without Orchestrator support. The instinct to "check in" on weeks 2–3 of production should be resisted unless the Friday status email signals a problem.

---

## Calendar Template: Allocated Orchestrator Hours/Day per Project per Week

| Date | Systems-resilience (pub) | Systems-resilience (Phase 6) | Author mgmt | Stockbot | Resistance-research | Seedwarden | Daily total |
|---|---|---|---|---|---|---|---|
| **June 1** | 3–4 hrs (editorial kickoff; decision session) | 1 hr (dispatch briefing) | 1 hr (send onboarding email) | 1 hr (Lever B decision) | 1 hr (rr synthesis routing) | 0 | 7–8 hrs |
| **June 2** | 3–4 hrs (editorial) | 2 hrs (research agent briefing) | 0 | 1 hr (Lever B setup) | 1 hr (rr sprint) | 0 | 7–8 hrs |
| **June 3** | 3–4 hrs (editorial) | 0 | 0 | 0 | 1 hr (rr sprint) | 0 | 4–5 hrs |
| **June 4** | 3–4 hrs (editorial) | 0 | 0 | 0 | 1 hr (rr sprint) | 0 | 4–5 hrs |
| **June 5** | 3–4 hrs (pub day) | 0 | 1 hr (source list Q&A) | 0 | 0 | 0 | 4–5 hrs |
| **June 6–7** | 0 (monitoring) | 0 | 1 hr/day | 0 | 0 | 0 | 1–2 hrs/day |
| **June 8** | 0 | 3–4 hrs (first-draft review begins) | 2 hrs (outline review) | 0 | 0 | 0 | 5–6 hrs |
| **June 9** | 0 | 3–4 hrs (first-draft review) | 2 hrs (outline final review) | 0 | 0 | 0 | 5–6 hrs |
| **June 10** | 0 | 3–4 hrs (first-draft review) | 0 | 0 | 0 | 0 | 3–4 hrs |
| **June 11–14** | 0 | 2–3 hrs/day (integration review) | 1 hr/day | 0 | 0 | 0 | 3–4 hrs/day |
| **June 15** | 3 hrs (Wave 3 editorial begins) | 2–3 hrs (integration) | 0 | 0 | 0 | 0 | 5–6 hrs |
| **June 16–21** | 2–3 hrs/day (Wave 3 editorial) | 2–3 hrs/day (integration) | 1 hr/day | 0 | 0 | 0 | 5–7 hrs/day |
| **June 22–28** | 2–3 hrs/day (Wave 3 pub prep) | 1–2 hrs/day (steady state) | 1 hr/day | 0 | 0 | 0 | 4–6 hrs/day |
| **June 29** | 0 | 0 | 4–5 hrs (Checkpoint 1 review) | 0 | 0 | 0 | 4–5 hrs |
| **June 30** | 1–2 hrs (Wave 3 pub day) | 1 hr | 1 hr | 0 | 0 | 0 | 3–4 hrs |
| **July 1–12** | 0 | 1–2 hrs/day | 1 hr/day | 0 | 0 | 0–2 hrs/day | 2–5 hrs/day |
| **July 13** | 0 | 0 | 4–5 hrs (Checkpoint 2 review) | 0 | 0 | 0 | 4–5 hrs |

This calendar assumes Option A publication and solo Economic Resilience selection. For A+C or A+D two-domain selection, add 1–2 hours/day to the Phase 6 column in June 15–30.

---

*Created: 2026-05-28 (Session 1711)*  
*Source data: RESOURCE_CONTENTION_ANALYSIS.md, PARALLEL_EXECUTION_FEASIBILITY.md, JUNE_PHASE_6_RESOURCE_ALLOCATION.md*
