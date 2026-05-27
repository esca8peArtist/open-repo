---
title: "Decision Support Recommendation — Phase 5 Publication Option (May 31 Decision)"
project: systems-resilience
phase: 5
status: FINAL RECOMMENDATION — user decision due May 31
decision_deadline: 2026-05-31
created: 2026-05-27
purpose: "Weighted scoring synthesis, primary recommendation, contingency fallback, May 31 checklist, June 1 next steps"
companion_docs:
  - TIMELINE_IMPACT_MATRIX.md
  - PARALLEL_EXECUTION_FEASIBILITY.md
  - PHASE_5_PUBLICATION_DECISION_FRAMEWORK.md
  - DECISION_SUPPORT_RECOMMENDATIONS.md
---

# Decision Support Recommendation — Phase 5 Publication Option

> This document synthesizes all prior analysis into a single actionable recommendation for the May 31
> user decision. If you want the evidence chain, read `TIMELINE_IMPACT_MATRIX.md` and
> `PARALLEL_EXECUTION_FEASIBILITY.md` first. If you want the recommendation, read only this document.

---

## 1. Weighted Scoring Summary

Three scoring dimensions replace the original 8-attribute framework score to add new analytical layers:
publication confidence, Phase 6 acceleration, and risk mitigation. Each is scored 1–10 and weighted
equally (33% each).

### Dimension 1: Publication Impact Confidence (33%)

Measures how quickly the corpus reaches the target community, whether the publication artifact supports
the mission (community resilience practitioners, organized groups, household implementers), and whether
the publication event is structured to maximize community uptake and engagement.

| Option | Score | Key rationale |
|---|---|---|
| **Option A** | 8/10 | 43,621 words (Wave 1+2) reaches the highest-leverage practitioner segment — community organizers, facilitators, governance leaders — by June 5. Wave 1+2 arc (energy infrastructure → human systems → implementation playbook) is independently coherent without Wave 3. Wave 3 (22,821 words: food, water, livestock, fuel, healthcare, education) is the operational household layer, needed after communities are organized. The natural reading sequence matches Option A's publication sequence. |
| **Option B** | 6/10 | Full 66,442-word corpus June 15 is a stronger single-artifact reference for institutional sharing and network distribution. Arrives 10 days later than Option A's primary content. No reader digests 66K words in one sitting; the unified structure is more authoritative on paper than functionally advantageous in practice. |
| **Option C** | 5/10 | First content May 30, but only 2 documents (~15K words). Full corpus not available until July 10–15 — the longest tail of any option. Per-pair digestibility is highest, but audience engagement required to sustain 6 consecutive weekly releases is operationally demanding and the authority artifact is weakest (fragmented pairs, no unified reference until July). |

### Dimension 2: Phase 6 Acceleration (33%)

Measures how early Phase 6 research activates, how smoothly June runs, and whether the publication
option creates bottlenecks for Phase 6 completion by the August 30 target.

| Option | Score | Key rationale |
|---|---|---|
| **Option A** | 8/10 | Phase 6 starts June 1 (domain selection decision due May 31 is the only gate; publication option is not a gate). After June 5 publication, Orchestrator drops to monitoring mode — frees bandwidth for Phase 6 Domain A/C/D first-draft reviews June 10–15. Integration work June 15–25 runs alongside Wave 3 editorial without significant contention. Domains E/F/H second-wave activated June 20–25. Completion: August 30 – September 5 (high confidence, 80%). |
| **Option B** | 7/10 | Phase 6 starts June 1 (identical to A). Orchestrator setup mildly delayed June 2–4 due to editorial kickoff. Domain A/C/D first-draft reviews slip 2–4 days to June 14–18. Phase 6 integration June 22–27. Completion: August 30 – September 5 (same end date, high confidence). Primary risk: July 1–20 crunch (author production + Phase 6 integration + publication response monitoring stack simultaneously). |
| **Option C** | 4/10 | Phase 6 starts June 1 but Orchestrator bandwidth for Phase 6 review and integration is persistently contested by rolling publication cycles through July 4. Phase 6 Domain A/C/D integration slips to July 1–10. Domains E/F/H second-wave activation defers to July 10–15. Completion: September 20 – October 1 (low confidence, 35–45%). The 3–4 week Phase 6 delay is entirely attributable to the 6-week rolling tail. |

### Dimension 3: Risk Mitigation (33%)

Measures exposure to single-gate failure, multi-project June 1–15 collision, author contingency
cascade, Jetson infrastructure interference, and the ability to absorb unexpected disruptions.

| Option | Score | Key rationale |
|---|---|---|
| **Option A** | 9/10 | Two independent publication gates (June 5, June 30). June 1–5 editorial spike is bounded and recoverable. Author unavailability does not affect either publication gate — self-execute fallback runs independently on the June 10–July 10 track. Wave 1+2 reader feedback can be incorporated into Wave 3 editorial (June 15–27 window open). Stockbot retrain coordination (5–8 hrs) absorbed post-June 5. Jetson offline event (as occurred May 22–26) does not affect any publication gate. All risk vectors are bounded and non-cascading. |
| **Option B** | 5/10 | Single mandatory publication gate June 15. Any June 1–14 disruption — Jetson retrain coordination, author onboarding decision, resistance-research synthesis activation, open-repo deployment decision — directly threatens the June 15 deadline. No feedback integration window exists before the unified release. If June 15 slips, the entire 66K-word corpus is delayed to July. |
| **Option C** | 4/10 | Each of 6 weekly cycles is a potential slip point. Six cycles across 6 weeks means compounding drift risk. If one pair receives significant criticism, the decision to revise it before subsequent pairs creates execution pressure. The 6-week execution tail overlaps with summer scheduling variability, author production deadlines, and Phase 6 integration — creating the broadest risk exposure window. |

### Composite Weighted Scores

| Dimension | Weight | Option A | Option B | Option C |
|---|---|---|---|---|
| Publication impact confidence | 33% | 8 × 0.33 = **2.64** | 6 × 0.33 = **1.98** | 5 × 0.33 = **1.65** |
| Phase 6 acceleration | 33% | 8 × 0.33 = **2.64** | 7 × 0.33 = **2.31** | 4 × 0.33 = **1.32** |
| Risk mitigation | 33% | 9 × 0.33 = **2.97** | 5 × 0.33 = **1.65** | 4 × 0.33 = **1.32** |
| **Total weighted score** | 100% | **8.25 / 10** | **5.94 / 10** | **4.29 / 10** |

This weighted analysis is consistent with the original 8-attribute framework score (30/40 A vs 24/40 B
vs 27/40 C) but surfaces the risk dimension more directly. Option A's 2.31-point margin over Option B
is driven primarily by risk profile: Option A's two independent publication gates make it nearly immune
to single-point failure. Option B's single mandatory gate is vulnerable to the known June 1–14
multi-project load.

---

## 2. Primary Recommendation: Option A

**Select Option A (Staged): Publish Wave 1+2 by June 5. Publish Wave 3 by June 30.**

Option A is optimal for five reasons that reinforce each other:

**Reason 1 — Highest publication confidence score (8/10).** Wave 1+2 is already polished and
production-ready after multiple revision cycles. No additional editorial work is required before June 5.
The Wave 1+2 corpus — microgrids, veterinary care, psychological support, conflict resolution, community
playbook — is independently coherent. A community that receives these 43K words on June 5 can begin
organizing, planning, and implementing without waiting for Wave 3. Wave 3 (food, water, livestock,
fuel, education) is the operational layer communities need once they are organized — the natural
reading sequence matches the publication sequence.

**Reason 2 — Phase 6 parallel acceleration is feasible starting June 1.** Publication timing does not
gate Phase 6. The domain outlines, selection matrix, and sequencing recommendation are already
committed. After the May 31 domain selection decision, research agents can be briefed June 1 and
begin source library compilation immediately. The Wave 1+2 editorial work (Orchestrator, June 1–5)
and the Phase 6 source library build (research agent, June 1–5) use different capacity — they run
in parallel without competition. After June 5, the Orchestrator drops to passive monitoring for Wave
1+2 feedback, fully freeing bandwidth for Phase 6 Domain A/C/D first-draft reviews June 10–15.

**Reason 3 — Author hiring window is earliest and most viable.** Author onboarding June 1–9 is
possible under Option A because the Orchestrator is not in a mandatory editorial integration window.
Author production writing starts June 10, giving 30 working days (June 10–July 10) for 80–100 hours
of draft production — an appropriate pace of 25–35 hrs/week. Under Option B, onboarding delays to
June 8–20 and production compresses to 20 working days, raising the July 20 delivery risk to
MEDIUM confidence (55–65%). Option A maintains HIGH confidence (85%) for July 10 delivery.

**Reason 4 — Risk profile is the most resilient of any option.** Option A's two independent
publication gates (June 5, June 30) mean that any single disruption — Jetson connectivity issue,
author unavailability, Lever B retrain anomaly — cannot block both publication events simultaneously.
Under Option B, the single June 15 gate is the most exposed: anything that absorbs 8+ Orchestrator
hours in June 1–14 directly threatens the deadline. Option A absorbs the same disruptions post-June 5
without affecting June 30.

**Reason 5 — The June 5 date allows feedback integration that Option B cannot offer.** Publishing
Wave 1+2 on June 5 creates a 3–4 week window (June 5–30) to collect practitioner feedback before
Wave 3 is finalized. If readers identify gaps in Wave 1+2 content (missing equipment specifics,
unclear protocols, Zone 5 regional gaps), that feedback can inform the Wave 3 editorial pass June
15–27. Under Option B, all 12 documents publish simultaneously with no revision window — the
Wave 3 quality risk (documents written in a final sprint) is locked in at publication.

Option A's single legitimate weakness is corpus coherence: a reader who encounters Wave 1+2 before
Wave 3 is available may not recognize the full scope of the project. This is fully mitigated by
including a clear "Volume 2 (Practical Operations): coming June 30" announcement in the Wave 1+2
release — a 50-word addition that resolves the reader confusion risk at zero cost.

---

## 3. Contingency Recommendation: Option B (If Author Unavailable)

**If the Wave 2 author confirms unavailability by May 30 AND the user has confirmed 10–15 hours of
editorial integration capacity for June 1–14 AND a specific institutional distribution partner has
been identified that requires a single canonical reference URL by June 15, then Option B becomes
a viable alternative.**

This is a conjunction: all three conditions must hold simultaneously for Option B to be competitive
with Option A. The probability that all three hold is low; the probability that one or two hold is
moderate.

Under the self-execute fallback scenario (author unavailable, Orchestrator writes Wave 2 guide content):
- Option A: self-execute activates June 10–July 10 independently; June 5 and June 30 publication
  gates are unaffected; Orchestrator load June 10–July 10 rises by 50 hours but is manageable
  because the editorial peaks are complete
- Option B: self-execute activates simultaneously with June 1–14 editorial integration; Orchestrator
  must run mandatory cross-reference work AND wave 2 guide writing at the same time; quality
  degradation risk is real

**If author is unavailable, Option A becomes even more preferred, not less.** The contingency for
"author unavailable" is not a reason to shift to Option B — it is a reason to confirm Option A.

If the user's primary concern is the "Volume 2 gap" (risk that Wave 3 readers miss the Wave 1+2
foundation), the mitigation is within Option A: include a "Volume 2 of 2" header in the Wave 1+2
release, a brief foreword noting the June 30 follow-on, and a single "complete corpus incoming"
announcement when Wave 3 publishes June 30. This addresses the coherence concern without accepting
Option B's operational risk.

---

## 4. Decision-Making Checklist for May 31 Decision

Three questions are sufficient to select the option:

**Question 1: Is wave parallelization (staged release) acceptable, or is a single unified corpus artifact required?**

- If parallelization acceptable (staged) → Option A or Option C
- If single artifact required (e.g., institutional partner, academic citation, network distribution needs one URL) → Option B
- Recommendation: Unless a specific institutional partner has been named who requires single-volume reference, parallelization is acceptable. Answer: proceed to Question 2.

**Question 2: Has the Wave 2 author been confirmed available for June 1 onboarding?**

- If author confirmed by May 30 → Option A (June 1 onboarding, July 10 delivery, HIGH confidence)
- If author declined or no response by May 30 16:00 UTC → self-execute fallback activates; Option A still recommended (fallback runs on independent track); confirm author decline is accepted and self-execute timeline June 10–July 10 is workable
- If author situation is uncertain → Option A is still recommended; uncertainty does not favor Option B (see Section 3 above)

**Question 3: Have Phase 6 research domains been selected (A + C + D recommended)?**

- If domains A + C + D approved → Phase 6 briefing activates June 1; this is independent of publication option
- If domain selection delayed to June 3 → No effect on publication option; Phase 6 briefing slips 2–3 days; domain first drafts still complete by June 14
- If domain selection has not been made → This is the only true Phase 6 dependency; confirm selection by May 31

If all three questions are answered (parallelization acceptable, author situation resolved, domain
selection complete), Option A activation is confirmed with no further preconditions.

---

## 5. Next Steps Post-Decision: June 1 Activation Timeline

### If Option A Selected (Recommended)

**May 28–31 (pre-decision window)**:
- Author outreach confirmation: receive accept/decline by May 30 16:00 UTC
- Co-author contingency (if needed): activate by May 31 (Candidates: Dr. Sarah Cho, Michael James, Jennifer Park — see AUTHOR_HIRING_RUNBOOK.md)
- Phase 6 domain selection: due May 31 (Domains A + C + D recommended; see phase-6-selection-matrix.md)
- Stockbot Lever B decision: config-only vs retrain (due May 27–31; see LEVER_B_DECISION_FRAMEWORK.md)

**June 1 (activation session — all decisions batched into single session)**:
- Phase 6 research agent briefing (2–3 hrs; Domain A/C/D outlines, source lists, sequencing recommendation)
- Author onboarding sprint kickoff (if author confirmed): orient, research kit, first-draft outline structure
- Wave 1+2 editorial kickoff: frontmatter standardization pass, cross-reference check, master TOC draft (Wave 1+2 only)
- Open-repo Phase 5.1 deployment confirmation (1–2 hrs Orchestrator decision)
- Stockbot Lever B configuration: activate AMZN + JPM on selected model path

**June 1–3**:
- Wave 1+2 final editorial pass (8–10 hrs Orchestrator): frontmatter, cross-references, master TOC
- Phase 6 source library build (research agent, independent)

**June 3–5**:
- Wave 1+2 publication logistics and announcement preparation
- Write "Volume 2 coming June 30" note for inclusion in Wave 1+2 release
- Author: begin first-draft section outline with Orchestrator feedback

**June 5–7**:
- Publish Wave 1+2 (43,621 words). Distribute via planned channels.
- Announce: "Volume 2 (Practical Operations): 22,821 words, arriving June 30"

**June 5–20**:
- Monitor Wave 1+2 reader feedback (passive, 1–2 hrs/week). Note structural gaps relevant to Wave 3.
- Author production writing: June 10 start, first checkpoint June 15–16
- Phase 6 Domain A/C/D first-draft production (research agent); Orchestrator first-draft review June 10–15

**June 15–27**:
- Wave 3 light editorial pass: add cross-references to Wave 1+2 documents where relevant, standardize frontmatter, write Wave 3 table of contents (8–12 hrs Orchestrator)
- Incorporate any substantive Wave 1+2 feedback (June 5–20 collection) into Wave 3 editorial if applicable
- Phase 6 integration work concurrent with Wave 3 editorial (different document sets; compatible)
- Author feedback cycle 2 (June 18–20)

**June 28–30**:
- Publish Wave 3 (22,821 words). Announce to same distribution channels: "The complete systems-resilience corpus is now available. Wave 3 covers food preservation, water systems, livestock care, seed saving, healthcare offline, fuel production, and educational governance."
- Activate Phase 6 Domains E/F/H second-wave (if Domains A/C/D first drafts complete by June 25)

### If Option B Selected (Fallback)

**June 1 (batch session)**:
- Same Phase 6 briefing, same stockbot + open-repo decisions (identical to Option A)
- Begin cross-reference integration (Wave 3 → Wave 1+2 explicit links): 6–10 hrs, June 1–7

**June 1–7**:
- Cross-reference integration across all 12 documents
- Master TOC (66K words, 5 waves): 4–6 hrs

**June 7–14**:
- Wave 3 structural consistency review: 6–10 hrs
- Author onboarding sprint start: June 8 (delayed 7 days from Option A)

**June 13–15**:
- Publish full 66,442-word corpus. Single announcement, single URL.

**June 20–July 20**:
- Author production writing (delayed 10 days from Option A)

### If Option C Selected (Not Recommended)

If selected despite recommendation, the user should confirm: (a) 6 consecutive weeks of editorial
and promotion capacity through July 4, (b) acceptance that Phase 6 completion shifts to
September 20–October 1, and (c) acceptance that Wave 2 author feedback cycles will persistently
compete with rolling publication management.

The rolling schedule (May 30 – July 4) would proceed as documented in
`PHASE_5_PUBLICATION_DECISION_FRAMEWORK.md` Section "Option C: Rolling Modular." Orchestrator load
is the highest of any option across the entire period (42–72 hrs/month June–July).

---

## 6. Summary

| Question | Answer |
|---|---|
| **Recommended option** | Option A (Staged) — weighted score 8.25/10 |
| **Decision deadline** | May 31, 2026 (23:59 UTC) |
| **First action required** | Confirm author status by May 30; confirm Phase 6 domain selection by May 31 |
| **Option B acceptable if** | All three conditions hold: (1) 10–15 hrs editorial integration capacity June 1–14 confirmed, (2) specific institutional partner requires single-volume reference, (3) author unavailability accepted with Option B fallback plan |
| **Option C acceptable if** | Dedicated community manager available for 6-week rolling promotion AND Phase 6 September completion is acceptable AND Wave 2 author delivery July 20+ is acceptable |
| **Default if no decision by May 31** | Option A default activation is recommended — June 1 editorial prep can begin without explicit decision; Option A is the standing recommendation |
| **Single most important confirmation** | Wave 2 author availability by May 30. This determines whether the June 1 onboarding advantage materializes. Everything else is recoverable. |

---

*Created: 2026-05-27 | Status: FINAL RECOMMENDATION | Companion: TIMELINE_IMPACT_MATRIX.md, PARALLEL_EXECUTION_FEASIBILITY.md*
