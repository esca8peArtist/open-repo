---
title: "Resource Contention Analysis — Multi-Project June 2026 Picture"
project: systems-resilience
phase: 5
status: DECISION-SUPPORT — user decision due May 31
decision_deadline: 2026-05-31
created: 2026-05-27
purpose: "June resource contention matrix for Option A/B/C across all active projects"
companion_docs:
  - PUBLICATION_OPTION_IMPACT_MATRIX.md
  - PARALLEL_EXECUTION_FEASIBILITY.md
  - JUNE_PHASE_6_RESOURCE_ALLOCATION.md
  - DECISION_SUPPORT_RECOMMENDATIONS.md
---

# Resource Contention Analysis — Multi-Project June 2026

> Lead finding: June 1–15 is the single highest-contention window in the June portfolio, regardless
> of which publication option is selected. The key difference between options is whether that
> contention is concentrated into a bounded 5-day spike (Option A), sustained through a mandatory
> 14-day window (Option B), or spread as a low-but-unrelenting 6-week tail (Option C). Option A
> creates the most recoverable contention profile. Option B creates the most dangerous single-window
> risk. Option C creates the highest total June–July resource drain.

---

## 1. Active Projects Competing for June Resources

Three projects activate or peak between June 1–15 simultaneously:

| Project | June scope | Peak window | Primary resource type | Weekly hours |
|---|---|---|---|---|
| **Systems-resilience Phase 5 publication** | Wave 1+2 pub (June 5 or June 15) + Wave 3 pub (June 30 or included) | June 1–5 (A) or June 1–14 (B) or ongoing (C) | Orchestrator (editorial) | See weekly breakdown below |
| **Systems-resilience Phase 6 launch** | Domain A/C/D research (Domains 60–65 equivalent) | June 1–August 30; peak June 1–25 | Research agent + Orchestrator review | 20–28 hrs/week (research agent); 5–10 hrs/week (Orchestrator review) |
| **Stockbot Lever B AMZN/JPM deployment** | JPM model decision + deployment (config-only or retrain) | May 28–June 1 (config-only) or June 1–15 (retrain) | Stockbot subagent + Orchestrator (coordination) | 17 hrs total (config-only) or 76 hrs total (retrain); 5–8 Orchestrator coordination hours in either case |
| **Open-repo Phase 5.1 post-merge deployment** | libzim wheel deployment + alembic upgrade + ZIM validation | June 1–15 | Engineering subagent | 21 hrs total; no Orchestrator writing demand |
| **Resistance-research Phase 2 distribution** | Domain 56/39 distribution sprint + synthesis outcome routing | May 28–June 5 (sprint) then monitoring | Research agent | 8–12 hrs (sprint), then passive monitoring |

---

## 2. Orchestrator Hours: The Shared Bottleneck

All five project streams require Orchestrator coordination in June 1–15. The Orchestrator is the
single non-parallelizable resource — it cannot review Phase 6 drafts and execute Option B editorial
integration simultaneously at full quality.

### Orchestrator demand June 1–15 by source

| Source | Hours June 1–5 | Hours June 6–10 | Hours June 11–15 | Total June 1–15 |
|---|---|---|---|---|
| Phase 5 publication (Option A: Wave 1+2 editorial + publication) | 13–18 | 2–4 (monitoring only) | 2–4 (monitoring) | 17–26 |
| Phase 5 publication (Option B: integrated editorial) | 8–12 | 10–15 | 8–12 | 26–39 |
| Phase 5 publication (Option C: Week 1 pair + Week 2 prep) | 6–10 | 8–12 | 8–12 | 22–34 |
| Phase 6 setup (briefing, domain activation — all options) | 2–4 | 0 (research agent runs) | 8–12 (first draft review) | 10–16 |
| Stockbot Lever B coordination (config-only) | 3–5 (resolves before June 5) | 0 | 0 | 3–5 |
| Stockbot Lever B coordination (retrain path) | 3–5 | 3–5 | 0–2 | 6–12 |
| Open-repo Phase 5.1 deployment decision | 1–2 | 0 | 0 | 1–2 |
| Resistance-research synthesis routing | 2–4 | 0–2 | 0 | 2–6 |

### Combined Orchestrator load June 1–15 by option (including stockbot config-only, open-repo, resistance-research)

| Option | June 1–5 | June 6–10 | June 11–15 | Total June 1–15 |
|---|---|---|---|---|
| **Option A** | 21–33 hrs | 4–8 hrs | 10–16 hrs | **35–57 hrs** |
| **Option B** | 16–27 hrs | 13–22 hrs | 16–26 hrs | **45–75 hrs** |
| **Option C** | 14–21 hrs | 11–19 hrs | 16–26 hrs | **41–66 hrs** |

Sustainable Orchestrator capacity is approximately 20–25 hours/week (from `JUNE_PHASE_6_RESOURCE_ALLOCATION.md`
estimate). The June 1–5 window under Option A (21–33 hrs total over 5 days = 4–7 hrs/day) is above
daily sustainable pace but bounded. Under Option B and C, the elevated demand extends through June 15.

**The June 1–5 spike under Option A is the most recoverable of the three profiles.** After June 5,
Option A Orchestrator demand drops sharply to monitoring and author feedback cycles. Option B and C
remain above 10 hrs/week through June 14.

---

## 3. Author Hours: Wave 2 Author Hiring Window by Option

Author hours are distinct from Orchestrator hours — the author works independently during production,
with only 3–4 Orchestrator feedback cycles in the June 10–July 10 window. However, the onboarding
sprint (June 1–9 under Option A, June 8–20 under Option B) does require Orchestrator coordination.

| Activity | Option A | Option B | Option C |
|---|---|---|---|
| Author onboarding start | June 1 | June 8 (Orchestrator in editorial integration June 1–7) | June 1 |
| Author production start | June 10 | June 20 | June 10 |
| Author draft delivery | July 10 | July 20–22 | July 10 |
| Orchestrator author feedback cycles | 3–4 (June 10–July 10) | 3–4 (June 20–July 20) | 3–4 (June 10–July 10) |
| Author–Orchestrator overlap with publication work | LOW — editorial peaks end June 5 | HIGH — editorial integration June 1–14 + author onboarding June 8–20 simultaneous | MEDIUM — ongoing rolling cycles mean author feedback always shares bandwidth |

If the Wave 2 author hiring needs to begin June 1–5 (Option A timing), that means the author
outreach and acceptance by May 30 is a real gate. If outreach has not confirmed author availability
by May 30, Option A's author onboarding slips to June 8–10 — which is operationally equivalent
to Option B's author start date. Under that scenario, the publication option no longer determines
author timing; author availability becomes the binding constraint independently.

**Author hiring contingency by option:**
- Option A: Author unavailable → self-execute fallback runs June 10–July 10 (50 hrs Orchestrator)
  on an independent track from June 5 publication and June 30 Wave 3 publication. No cascade.
- Option B: Author unavailable → self-execute fallback runs June 20–July 20, overlapping with
  post-publication reader response monitoring (June 15–30). Moderate cascade risk.
- Option C: Author unavailable → self-execute fallback runs concurrently with rolling publication
  cycles. Highest cascade risk.

---

## 4. Infrastructure: Jetson Monitoring During Lever B Deployment

The Jetson (xxsb-01, 100.120.18.84) hosts the stockbot production environment. Lever B deployment
requires either:

- **Config-only path** (accept lgbm_ho for JPM): ~17 hours total, completes May 28–June 1.
  Orchestrator coordination: 3–5 hours, entirely in the May 28–June 1 window.
  Effect on June publication options: NONE. Completes before any publication option editorial begins.

- **Retrain path** (JPM ridge_wf): ~2–3 hours Jetson compute + 76 hours total (setup, training,
  validation, deployment). Orchestrator coordination: 5–8 hours spread June 1–15.
  Effect on June publication options:
  - Option A: 5–8 hrs over 15 days = 0.3–0.5 hrs/day. Easily absorbed alongside Option A's
    June 5 editorial completion. No genuine contention.
  - Option B: 5–8 hrs concentrated in June 1–10 (overlaps Option B's mandatory 14-day editorial
    window). MODERATE contention — adds 5–8 hrs to an already stretched window.
  - Option C: 5–8 hrs spread across first two rolling cycles. LOW-MEDIUM contention.

**Can Jetson monitoring run in parallel with publication editorial work?**
Yes. Jetson monitoring is passive (stockbot subagent + periodic health checks). It does not compete
with editorial writing, research agent production, or author onboarding. The only shared resource
is Orchestrator attention for Lever B configuration decisions, which is bounded (one decision point:
retrain vs. config-only).

**Infrastructure risk scenario**: If Jetson becomes unreachable during the June 1–5 window
(as happened May 22–26), the Orchestrator would need to diagnose and resolve the connectivity issue.
This takes 2–4 hours under normal circumstances. Under Option A, the June 5 editorial deadline
has 5 calendar days of buffer from June 1. Under Option B, the June 15 deadline has 14 days of
editorial work to complete — a 2–4 hour infrastructure interruption is absorbed more easily.
However, if the Jetson issue extends to a multi-day outage (as in May), Option B's mandatory
14-day editorial window is the option most at risk of being disrupted.

---

## 5. Weekly Breakdown: June Resource Hours per Project per Option

### Option A

| Week | Systems-resilience (pub) | Systems-resilience (Phase 6) | Stockbot (Lever B) | Open-repo | Resistance-research | Orchestrator total |
|---|---|---|---|---|---|---|
| **June 1–7** | 18–23 (Wave 1+2 editorial, pub, monitoring) | 22–28 (research agent) + 4–6 (Orch setup/review) | 5–8 (retrain coordination, if needed) | 10–12 (subagent) | 6–10 (sprint) | **34–49** |
| **June 8–14** | 4–6 (Wave 1+2 monitoring) + 10–15 (author onboarding) | 22–28 (research agent) + 6–10 (Orch first-draft review) | 0–3 (monitoring) | 8–10 (subagent) | 2–4 (monitoring) | **26–44** |
| **June 15–21** | 8–12 (Wave 3 editorial pass) + 3–6 (author feedback cycle 1) | 15–20 (integration work, research agent) + 4–8 (Orch integration review) | 0 | 0 | 0 | **15–26** |
| **June 22–30** | 6–10 (Wave 3 pub + author feedback cycle 2) | 20–25 (research agent, steady state) + 4–6 (Orch) | 0 | 0 | 0 | **10–16** |
| **June total (Orchestrator)** | 43–64 | 18–30 | 5–11 | 0 | 2–4 | **~85–109 total** |

---

### Option B

| Week | Systems-resilience (pub) | Systems-resilience (Phase 6) | Stockbot (Lever B) | Open-repo | Resistance-research | Orchestrator total |
|---|---|---|---|---|---|---|
| **June 1–7** | 12–18 (cross-ref integration, master TOC) | 22–28 (research agent) + 2–4 (Orch setup only) | 5–8 (retrain coordination) | 10–12 | 6–10 (sprint) | **35–52** |
| **June 8–14** | 14–20 (Wave 3 quality pass + pub prep + author onboarding start) | 22–28 (research agent) + 6–10 (Orch first-draft review) | 0–3 | 8–10 | 2–4 | **38–57** |
| **June 15–21** | 3–5 (pub logistics + author onboarding completion + monitoring) + 4–8 (author first-draft checkpoint) | 15–20 (research agent) + 4–8 (Orch integration review) | 0 | 0 | 0 | **15–27** |
| **June 22–30** | 6–10 (author feedback cycle 1–2) | 20–25 (research agent, steady state) + 4–6 (Orch) | 0 | 0 | 0 | **10–16** |
| **June total (Orchestrator)** | 43–61 | 16–28 | 5–11 | 0 | 2–4 | **~88–118 total** |

---

### Option C

| Week | Systems-resilience (pub) | Systems-resilience (Phase 6) | Stockbot (Lever B) | Open-repo | Resistance-research | Orchestrator total |
|---|---|---|---|---|---|---|
| **June 1–7** | 10–16 (Week 2 pair: editorial + announcement + feedback monitoring from Week 1) | 22–28 (research agent) + 3–5 (Orch setup/review) | 5–8 | 10–12 | 6–10 | **34–51** |
| **June 8–14** | 10–16 (Week 3 pair + Week 2 feedback decision + author onboarding) | 22–28 (research agent) + 4–8 (Orch first-draft review) | 0–3 | 8–10 | 2–4 | **30–47** |
| **June 15–21** | 10–16 (Week 4 pair + Week 3 feedback + author first-draft checkpoint) | 15–20 (research agent) + 4–8 (Orch integration, partially deferred) | 0 | 0 | 0 | **26–40** |
| **June 22–30** | 10–14 (Week 5 pair + Week 4 feedback + author feedback cycle 1) | 20–25 (research agent) + 4–6 (Orch) | 0 | 0 | 0 | **20–30** |
| **June total (Orchestrator)** | 40–62 (publication only) | 15–27 | 5–11 | 0 | 2–4 | **~110–168 total** |

Note: Option C's total June Orchestrator hours are highest of any option because each weekly cycle
generates non-batchy work (announcement, feedback monitoring, integration decision). The rolling
schedule cannot be front-loaded or compressed — it is inherently week-by-week.

---

## 6. Risk Assessment: Which Option Creates Highest/Lowest Contention?

### Highest contention risk: Option C

Sustained 5–6 week publication tail creates the largest cumulative Orchestrator drain (110–168
hours over June and extending into July). The compounding effect: each week of rolling publication
shares bandwidth with Phase 6 domain review, author feedback cycles, and (in June 1–15) stockbot
and open-repo monitoring. There is no moment in June where the Orchestrator can focus exclusively
on Phase 6 or author production without a rolling publication event competing.

**Option C contention risk: HIGH (especially for Phase 6 quality and Wave 2 author timeline)**

### Moderate contention risk: Option B

The June 1–14 editorial integration window is the single most dangerous concentration point.
Ten to fifteen hours of cross-reference work must complete within 14 calendar days, shared with:
- Stockbot retrain coordination (if retrain path selected): 5–8 hrs
- Author onboarding start (June 8): 12–15 hrs
- Open-repo Phase 5.2 deployment decisions: 2–3 hrs
- Phase 6 domain first-draft reviews (June 14–18): 8–12 hrs

If any of these runs long or requires replanning, the June 15 publication date slips. Under Option B,
the June 15 date has no buffer — it is both the deadline and the single gate.

**Option B contention risk: MEDIUM-HIGH (concentrated in June 1–14; single-gate risk)**

### Lowest contention risk: Option A

The June 1–5 editorial peak is real (21–33 Orchestrator hours in 5 days) but bounded. After June 5:
- Wave 1+2 editorial is complete
- Publication is live
- Orchestrator drops to passive monitoring
- Phase 6 domain production is in full swing (research agent)
- Author onboarding is complete; production writing begins June 10

The remaining June weeks (June 6–30) operate with significantly lower Orchestrator demand, allowing
Phase 6 review, Wave 3 editorial (June 15–27), and author feedback cycles to distribute without
competition.

**Option A contention risk: LOW (bounded June 1–5 spike; distributed, manageable June 6–30)**

---

## 7. Contention Risk Summary

| Risk dimension | Option A | Option B | Option C |
|---|---|---|---|
| Peak contention severity (June 1–15) | HIGH for 5 days, then LOW | MEDIUM-HIGH for 14 days | MEDIUM for 6 weeks |
| Contention recovery speed | Fast (drops sharply after June 5) | Medium (drops after June 15) | Slow (stays elevated through July 4) |
| Single-gate failure risk | LOW (two independent gates) | HIGH (one mandatory gate) | MEDIUM (each week is a potential slip) |
| Phase 6 quality impact | LOW | LOW-MEDIUM (first-draft reviews mildly delayed) | MEDIUM (ongoing competition with rolling cycles) |
| Author production impact | LOW (independent track) | MEDIUM (delayed start + July crunch) | MEDIUM-HIGH (rolling cycles compete with feedback cycles) |
| Multi-project collision (stockbot + open-repo) | LOW | MEDIUM (June 1–14 dangerous window) | LOW per week, MEDIUM cumulatively |
| **Overall contention verdict** | **Lowest** | **Moderate** | **Highest** |

---

*Created: 2026-05-27 | Status: DECISION-SUPPORT — awaiting user decision by 2026-05-31*
