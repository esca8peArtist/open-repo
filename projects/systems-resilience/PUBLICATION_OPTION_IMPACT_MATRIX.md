---
title: "Publication Option Impact Matrix — Phase 5 Options A/B/C"
project: systems-resilience
phase: 5
status: DECISION-SUPPORT — user decision due May 31
decision_deadline: 2026-05-31
created: 2026-05-27
purpose: "Comprehensive cross-option comparison table for Phase 5 publication decision"
companion_docs:
  - PHASE_5_PUBLICATION_DECISION_FRAMEWORK.md
  - PHASE_5_PUBLICATION_TIMELINE_IMPACT_ANALYSIS.md
  - PARALLEL_EXECUTION_FEASIBILITY.md
  - RESOURCE_CONTENTION_ANALYSIS.md
  - DECISION_SUPPORT_RECOMMENDATIONS.md
---

# Publication Option Impact Matrix

> Prepared May 27, 2026. User decision deadline: May 31, 2026.
>
> This matrix extends the decision-matrix scoring in `PHASE_5_PUBLICATION_DECISION_FRAMEWORK.md` with
> downstream impact estimates: concrete hour counts, date ranges, and risk classifications derived from
> actual Phase 5 production data. It does NOT repeat the attribute-scoring analysis; it adds new
> analytical layers the prior document does not contain.

---

## Core Impact Matrix

| Metric | Option A (Staged) | Option B (Unified) | Option C (Rolling) |
|---|---|---|---|
| **Publication option score (existing framework)** | 30/40 — recommended | 24/40 | 27/40 |
| **First content reaches readers** | June 5–7 | June 15–17 | May 30 (first pair only) |
| **Full 66K corpus available to readers** | June 30 | June 15–17 | July 10–15 |
| **June Orchestrator hours (editorial + coordination)** | 40–56 hrs (peak June 1–5, then drops) | 37–61 hrs (concentrated June 1–14) | 42–60 hrs (sustained June 1–July 4) |
| **Author hiring window (onboarding start)** | June 1–9 | June 8–20 (7-day slip vs. A) | June 1–9 or June 8–20 |
| **Author production writing start** | June 10 | June 20 (10 days later) | June 10 or June 20 |
| **Author draft delivery** | July 10 | July 20–22 | July 10 or July 20 |
| **Phase 6 research start (earliest)** | June 1 (pre-production); June 3–5 (full production) | June 1 (same — publication option does not gate Phase 6) | June 1 (same) |
| **Phase 6 Domains A/C/D first drafts complete** | June 7–14 (realistic) | June 7–14 (same) | June 11–15 (2–4 day slip due to Orchestrator contention) |
| **Phase 6 integration document start** | June 15–20 | June 15–20 | June 25–July 1 |
| **Phase 6 completion estimate** | August 30 – September 5 | August 30 – September 5 | September 20 – October 1 |
| **Wave 3 production completion** | June 28–30 (editorial pass June 15–27) | June 15 (included in unified release) | July 4 (last pair in rolling schedule) |
| **Risk: publication delay (if one component slips)** | LOW — two independent gates; June 5 slip does not affect June 30 | HIGH — single gate; any June 1–14 slip pushes the entire corpus to July | MEDIUM-HIGH — each weekly slip cascades; 5-week tail means compounding drift |
| **Coordination complexity** | Simple — two clean events 25 days apart | Medium — one hard-deadline integration across 12 documents | Complex — 5–6 separate editorial and promotion cycles with ongoing feedback monitoring |
| **Stakeholder activation impact** | Phased — community practitioners get actionable Wave 1+2 content June 5; Wave 3 follows June 30 | Immediate (all at once, June 15) — but 10 days later than Option A Wave 1+2 | Drip — first content May 30, but full corpus not available until July 10–15 |
| **Feedback integration window** | HIGH — 3–4 week window (June 5–30) to collect Wave 1+2 feedback before Wave 3 finalizes | NONE — all content published simultaneously; no revision window | HIGH — per-pair feedback possible, but operationally complex to integrate within rolling schedule |
| **Self-execution fallback viability (if author unavailable)** | HIGH — Wave 3 publication and author production are independent tracks | MEDIUM — author decision coincides with editorial integration peak (June 1–14) | LOW — ongoing rolling schedule creates highest sustained coordination burden |
| **Open-repo / stockbot contention (June 1–15)** | LOW — Wave 1+2 editorial (June 1–5) is bounded; stockbot and open-repo proceed independently | MEDIUM — Option B's June 1–14 editorial window overlaps peak open-repo and stockbot activity | LOW-MEDIUM — each weekly cycle is short, but 6 cycles over 6 weeks accumulate |

---

## Extended Dimensions

### Dimension A: Orchestrator Load Profile (June weekly breakdown)

| Week | Option A | Option B | Option C |
|---|---|---|---|
| **June 1–5** | 15–20 hrs (Wave 1+2 editorial + publication) | 10–14 hrs (cross-reference integration start) | 10–14 hrs (Week 2 pair editorial + Week 1 feedback monitoring) |
| **June 6–14** | 4–8 hrs (Wave 1+2 monitoring, passive) | 12–20 hrs (editorial completion + master TOC + Wave 3 quality pass) | 14–20 hrs (Weeks 2–3 pair cycles + feedback) |
| **June 15–27** | 8–12 hrs (Wave 3 editorial pass) | 3–5 hrs (publication logistics, monitoring) | 12–18 hrs (Weeks 4–5 pair cycles) |
| **June 28–30** | 2–3 hrs (Wave 3 publication) | 0–1 hr | 6–10 hrs (Week 6 cycle + tail monitoring) |
| **June total** | 29–43 hrs (editorial/publication only) | 25–40 hrs (editorial/publication only) | 42–62 hrs (editorial/publication only) |

Note: Author coordination hours (15–20 hrs in June under Options A/C, 15–20 hrs delayed start under Option B) are additional to the above in all cases.

---

### Dimension B: Reader Community Impact Sequence

| Reader type | Option A timing | Option B timing | Option C timing |
|---|---|---|---|
| Community organizer, governance facilitator | June 5 (gets Playbook + Conflict Resolution + Microgrids immediately) | June 15 | Week 1 May 30 (Playbook + Microgrids) OR Week 2 June 6 |
| Animal care practitioner | June 5 (Veterinary Care Guide) | June 15 | Week 3 June 13 |
| Household-scale practitioner (food, water, fuel) | June 30 (Wave 3) | June 15 | Weeks 4–6 (June 20–July 4) |
| Institution or network seeking single-volume reference | June 30 (after both volumes) | June 15 (strongest artifact) | July 10+ (when all pairs complete) |

Option B is the only option that delivers the single-volume reference by June 15. For all other reader types, Option A is equivalent or faster.

---

### Dimension C: Infrastructure Checkpoint Interactions

The Jetson infrastructure state (stockbot Lever B deployment) directly intersects with the June 1–15 window for all options.

| Infrastructure event | Timing | Option A interaction | Option B interaction | Option C interaction |
|---|---|---|---|---|
| Lever B config-only path (AMZN/JPM accept lgbm_ho) | May 28–June 1 | Completes before Option A editorial begins; no overlap | Same; no overlap | Same |
| Lever B retrain path (JPM ridge_wf, ~2–3 hrs Jetson compute + 5–8 hrs Orchestrator coordination) | June 1–15 | Orchestrator overhead (5–8 hrs) tolerable alongside June 1–5 editorial peak | MEDIUM conflict — 5–8 Orchestrator hours compete with June 1–14 editorial integration | LOW — weekly cycles absorb coordination without single-window conflict |
| Jetson health monitoring (ongoing) | June 1–30 | Monitoring is passive; stockbot subagent carries it | Same | Same |

---

### Dimension D: Author Hiring Window Sensitivity

| Gate | Option A | Option B | Option C | Sensitivity |
|---|---|---|---|---|
| Author status confirm | May 29–30 | May 29–30 | May 29–30 | Same for all — author availability is confirmed pre-option-selection |
| Onboarding start | June 1 | June 8 (7-day slip) | June 1 or June 8 | Option B delays onboarding because Orchestrator is in June 1–7 editorial integration |
| First draft checkpoint | June 6–9 | June 13–16 | June 6–9 or June 13–16 | Option B misses the early-June feedback window |
| Full production start | June 10 | June 20 | June 10 | 10-day delay under Option B |
| Draft delivery | July 10 | July 20–22 | July 10 | Option B compresses the author's remaining calendar time if summer schedules tighten |
| Peak author–Orchestrator overlap risk | LOW — author writes independently June 10–July 10 with 3–4 feedback cycles | MEDIUM — Orchestrator simultaneously managing post-publication response and author feedback | MEDIUM-HIGH — rolling cycles and author feedback cycles compete weekly |

---

### Dimension E: Contingency Resilience (Single-Point Failure Scenarios)

| Failure mode | Option A exposure | Option B exposure | Option C exposure |
|---|---|---|---|
| Author unavailable May 30–June 10 | LOW — publication gates unaffected; self-execute fallback runs June 10–July 10 independently | MEDIUM — self-execute activated during June 1–14 editorial peak; risk of quality degradation | HIGH — self-execute must run alongside ongoing weekly publication cycles |
| Stockbot retrain extends beyond June 5 | LOW — retrain is on Jetson compute track; 5–8 Orchestrator coordination hours absorbed post-June 5 | MEDIUM — extends into Option B's mandatory editorial window | LOW — retrain is independent of rolling schedule |
| Open-repo Phase 5.2 decision requires Orchestrator input June 1–5 | LOW — batch into June 1 session | MEDIUM — adds to Option B's June 1–7 editorial integration load | LOW |
| Wave 1+2 reader feedback identifies structural gap | LOW — Wave 3 editorial window (June 15–27) is open to absorb feedback | HIGH — no revision window; all content is locked post-June 15 | MEDIUM — pair-by-pair revision theoretically possible but operationally demanding |
| Resistance-research synthesis (May 28) triggers Phase 2 activation sprint | LOW — resistance sprint (3–5 days) completes before Option A's main Phase 6 review cycles | MEDIUM — competes with June 1–7 editorial window if sprint extends | LOW-MEDIUM |

---

## Matrix Summary Score (New Dimensions Only)

For the eight attributes in the original decision matrix, Option A scores 30/40. The five new dimensions above add additional evidence across the same directional pattern:

| New Dimension | Option A | Option B | Option C |
|---|---|---|---|
| Orchestrator load profile (manageability) | Best — front-loaded and bounded | Medium — sustained peak in mandatory window | Worst — longest sustained commitment |
| Reader sequence alignment (community readiness match) | Best for organizers and practitioners | Best for institutional single-volume seekers | Best for week-by-week engagement (highest coordination cost) |
| Infrastructure checkpoint interference | Lowest | Moderate (June 1–14 vulnerable) | Lowest |
| Author hiring window sensitivity | Best — 10 days earlier author start | Worst — 10-day slip, compressed calendar | Comparable to A |
| Contingency resilience | Best — independent publication gates | Worst — single gate, highest cascade risk | Middle — each cycle is small but 6 cycles accumulate |

**Across both the original 8-attribute matrix and the 5 new dimensions, Option A holds the strongest aggregate position.**

---

## Decision Prompt

Select one by May 31, 2026:

- [ ] **Option A (Staged, Recommended)**: Publish Wave 1+2 (43,621 words) June 5. Wave 3 (22,821 words) June 30. Phase 6 starts June 1. Author onboarding June 1–9.
- [ ] **Option B (Unified)**: Hold all 12 documents for June 15 integrated release. Confirm 10–15 hours editorial integration capacity June 1–14. Phase 6 starts June 1 (independent of publication).
- [ ] **Option C (Rolling)**: Weekly thematic pairs starting May 30. Confirm 5–6 consecutive weeks of editorial and promotion capacity through July 4.

---

*Created: 2026-05-27 | Companion: PHASE_5_PUBLICATION_DECISION_FRAMEWORK.md | Status: DECISION-SUPPORT*
