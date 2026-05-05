---
title: "Phase 2 Execution Roadmap — Post-Phase-1-Launch Implementation Calendar"
created: 2026-05-05
status: active — ready for implementation post-Phase-1-launch
purpose: "Sequential vs. parallel options, resource allocation, decision gates, success metrics, and 12-month execution calendar for Phase 2 domain research"
cross_references:
  - phase-2-domain-prioritization-matrix.md
  - domain-38-40-strategic-analysis.md
  - phase-2-domain-selection-framework.md
  - ITEM44_DOMAIN41_CANDIDATES.md
  - ITEM26_DOMAIN40_CANDIDATES.md
  - measurement-and-iteration-framework.md
word_count: ~2,100
---

# Phase 2 Execution Roadmap

**Prepared**: May 5, 2026  
**Timeline anchor**: This document assumes Phase 1 launches during the week of May 5, 2026. All Month references are relative to the Phase 1 launch week. Absolute calendar months are provided where policy windows make the calendar date the binding constraint.

---

## Part I: Implementation Architecture Options

Three implementation architectures are available for Phase 2 domain production. Each involves different trade-offs between speed, resource concentration, and risk.

---

### Option 1: Sequential (Domains one at a time)

**Mechanics**: Each domain is fully researched, written, reviewed, and distributed before the next domain begins. One orchestrator agent working at a time.

**Advantages**:
- Maximum quality per domain; no resource competition
- Clearest feedback loop: Phase 1 signal from each distributed domain informs the next domain's framing
- Lowest risk of research errors from parallel context fragmentation
- Easiest to manage from the user's oversight perspective

**Disadvantages**:
- Slowest path to coverage: 8 Tier-1/2 domains at 2–3 weeks each = 16–24 weeks (4–6 months)
- Several policy windows close during this timeline. The June 12 FISA deadline and November 3 midterm are hard constraints that sequential production cannot serve simultaneously
- Labor and Reproductive Rights domains compete for the same research agent time as Voting Systems, which is more urgent

**Verdict**: Sequential is appropriate for domains that have no competing hard deadlines. It is **not** sufficient for the May–June 2026 cluster, where FISA (June 12) and midterm prep (July distribution target) are concurrent.

---

### Option 2: Parallel (2–3 domains simultaneously)

**Mechanics**: 2–3 orchestrator agents research and write simultaneously. Domains are distributed as they complete rather than waiting for other domains to finish.

**Advantages**:
- Fastest path to coverage: 8 domains in 8–10 weeks if parallelism is maintained
- Serves concurrent policy windows: FISA (June 12) and Voting Systems (July) can be produced simultaneously rather than sequentially
- Captures the reinforcing-domain effect: Voting Systems and Disability Rights are stronger together; Intelligence Oversight and Domestic Intelligence complement each other

**Disadvantages**:
- Higher resource demand: 2–3 simultaneous research agents
- Risk of context fragmentation: parallel agents working on related domains (Intel Oversight + Domestic Intelligence) may produce redundant or contradictory framing
- Requires explicit cross-referencing coordination to prevent each domain from becoming an island

**Verdict**: Parallel is appropriate for the May–June 2026 window where FISA and Voting Systems must both be produced before their windows close. Parallelism should be constrained to 2 simultaneous domains maximum to maintain quality.

---

### Option 3: Hybrid (Primary Sequential + Targeted Parallel)

**Mechanics**: One primary sequential track for the highest-scoring domains; one targeted parallel track for time-locked domains that cannot wait for the sequential queue.

**Recommended configuration**:

**Track A (Sequential Primary)**: Voting Systems → Reproductive Rights → Labor Rights → Constitutional Architecture  
**Track B (Targeted Parallel)**: FISA Intel Oversight (June 12 deadline) + Tribal Sovereignty (SCOTUS ruling trigger)

Track B runs parallel to Track A specifically because it is triggered by external calendar events (June 12 FISA deadline; *Trump v. Barbara* ruling) rather than internal production sequencing.

**Advantages**:
- Captures both hard-deadline urgency (Track B) and maximum quality (Track A sequential)
- Fiscal Authority can be produced in Track A during a natural pause (between Repro Rights completion and Labor Rights start)
- Disability Rights can be assigned as Track B when SAVE Act Senate consideration is scheduled

**Disadvantages**:
- More complex coordination than either pure option
- Requires explicit domain deconfliction for Intel Oversight (Track B) and Domestic Intelligence (Track A, Month 3–4)

**Verdict**: Hybrid is the recommended architecture. It serves the June 12 FISA window and the *Trump v. Barbara* ruling trigger without sacrificing the sequential quality that the highest-complexity domains require.

---

## Part II: Resource Allocation

### Agent Assignment by Domain

| Domain | Track | Recommended Agent Type | Estimated Hours | Backup If First Unavailable |
|--------|-------|----------------------|-----------------|----------------------------|
| 38-B (Voting Systems) | A-Primary | General Research Agent (high constitutional law depth) | 14–18 hours | Orchestrator |
| 38-A (Intel Oversight) | B-Parallel | General Research Agent (national security + civil liberties) | 12–15 hours | Orchestrator |
| 40-B (Tribal Sovereignty) | B-Parallel | General Research Agent (federal Indian law depth) | 10–14 hours | Orchestrator |
| 41-B (Disability Rights) | A-Secondary | General Research Agent (civil rights + administrative law) | 10–14 hours | Orchestrator |
| 40-C (Fiscal Authority) | A-Fill | General Research Agent (administrative + appropriations law) | 8–10 hours | Any available |
| 39-A (Repro Rights) | A-Primary | General Research Agent (constitutional law + political science) | 14–18 hours | Orchestrator |
| 39-B (Labor Rights) | A-Primary | General Research Agent (labor law + political economy) | 12–16 hours | Orchestrator |
| 41-A (Domestic Intel) | A-Primary | General Research Agent (constitutional law + security) | 12–15 hours | Orchestrator |
| 40-A (Const. Architecture) | A-Primary | General Research Agent (constitutional law depth) | 12–16 hours | Orchestrator |

**Total Phase 2 research hours (Tier 1+2)**: 105–131 hours across 9 domains  
**At 3-hour sessions**: 35–44 sessions  
**At current autonomous research cadence**: approximately 10–12 weeks to complete Tier 1+2

---

## Part III: Decision Gates and Contingency Triggers

Six explicit decision gates determine Phase 2 sequencing adjustments. These gate conditions override the baseline timeline.

---

**Gate 1 — FISA June 12 Outcome** (triggers by June 12, 2026)

*Condition A (three-year extension passes without warrant requirement)*: Domain 38-A (Intel Oversight) is completed and distributed immediately after the vote. The domain frames the warrant-requirement failure as a democratic design problem that remains unresolved. This is the expected outcome and has been planned for in the research roadmap.

*Condition B (extension lapses or fails)*: Domain 38-A is distributed before the lapse with explicit "what happens next" framing. The surveillance-tracking.md update (identified in phase-2-expansion-roadmap.md Part II) activates immediately — this is a 300-500 word update, not a new domain.

*Condition C (warrant requirement included)*: Domain 38-A adjusts its framing to document what the warrant requirement actually does and what remains unresolved (commercial data broker loophole). Still distribute; the domain's reform analysis remains relevant.

---

**Gate 2 — *Trump v. Barbara* SCOTUS Ruling** (triggers June/July 2026)

*Condition A (ruling confirms Indian Citizenship Act, rejects birthright citizenship revocation)*: Domain 40-B (Tribal Sovereignty) is immediately completed and distributed. The ruling validates the sovereignty analysis; the domain frames the FY2026 budget cuts as the more immediate threat.

*Condition B (narrow ruling that avoids the tribal citizenship question)*: Domain 40-B is completed and distributed with an analysis of what the non-ruling means for future challenges. The budget-crisis angle remains the lead.

*Condition C (ruling undermines Indian Citizenship Act)*: Domain 40-B becomes urgent Tier 1 regardless of queue position. This is the worst-case legal scenario and requires immediate production and maximum-priority distribution to NARF and NCAI.

---

**Gate 3 — Phase 1 Feedback (Week 6 post-launch)**

The feedback-driven Tier reassignment described in phase-2-domain-selection-framework.md applies here. At Week 6 (approximately June 15, 2026), Phase 1 feedback data is aggregated. Three possible triggers:

- If 3+ contacts from different sectors ask about FISA/surveillance without being prompted: Intel Oversight (38-A) is confirmed Tier 1 and moves to the front of Track B.
- If election protection organizations show adoption: Voting Systems (38-B) is confirmed Tier 1 and production continues at full priority.
- If civil rights or health sector contacts ask about OBBBA specifics beyond Domain 31: The phase-2-domain-candidate-1-medicaid-crisis.md addendum is elevated to Tier 1b (not a full domain, but a targeted distribution to health-sector contacts).

---

**Gate 4 — SAVE Act Senate Action** (triggers when Senate schedules the bill)

If the SAVE Act (H.R.22) reaches Senate floor consideration or markup in 2026, Domain 41-B (Disability Rights) immediately activates regardless of queue position. The SAVE Act's disability provisions are the most time-sensitive advocacy intervention point in the entire Phase 2 set. This is a Track B parallel activation.

---

**Gate 5 — 2026 Midterm Results** (November 3, 2026)

*Democratic House gain (+15 seats or more)*: Constitutional Architecture (40-A) and Congressional Fiscal Authority (40-C) become immediately higher-priority in Phase 3 planning. A changed House majority activates the legislative pathways these domains describe.

*Republican House retention*: Emphasis shifts to litigation-vector domains (Voting Systems, Disability Rights, Domestic Intelligence) and state-level ballot initiative campaigns. Constitutional Architecture deferred to post-2028 window.

*Democratic Senate gain (+5 seats, achieving 55+ majority)*: DISCLOSE Act (campaign finance / 41-C) and John Lewis VRA (38-B follow-up) become actionable legislative vehicles. Dark Money domain elevates from Tier 3 to Tier 2.

---

**Gate 6 — Callais Redistricting Implementation** (ongoing, through 2026)

As states begin implementing redistricting under the new intent standard, active litigation will produce factual records that should be incorporated into Domain 38-B (Voting Systems) as a post-production update. If three or more states have enacted or implemented demonstrably discriminatory maps by September 2026, a targeted Domain 38-B update should be produced before November 3.

---

## Part IV: Success Metrics by Domain

Each domain has a distinct primary success metric that reflects its specific institutional adoption target.

| Domain | Primary Success Metric | Secondary Metric | Timeline |
|--------|----------------------|------------------|----------|
| 38-B (Voting Systems) | One election protection organization (Brennan Center, Democracy Docket, or ACLU Voting Rights Project) cites or references the domain document in their 2026 pre-election advocacy | Two law school election law clinics assign the document | 60 days post-distribution |
| 38-A (Intel Oversight) | One Senate Judiciary or Intelligence Committee staff member references the framework in a hearing context; or one civil liberties organization cites the document in a FISA brief | Congressional Research Service produces a report that cites the domain's structural analysis | 90 days post-distribution |
| 40-B (Tribal Sovereignty) | NCAI or NARF cites or distributes the domain document to their member network | One tribal governance news outlet (Native News Online, Indian Country Today) references the framework | 45 days post-ruling distribution |
| 41-B (Disability Rights) | State Protection and Advocacy (P&A) system in at least one state adopts the domain document for client advocacy | NDRN references the document in SAVE Act Senate testimony | 30 days post-distribution |
| 40-C (Fiscal Authority) | Brookings, CBPP, or Bipartisan Policy Center references the domain document in subsequent impoundment analysis | One academic law review cites the framework's constitutional analysis | 120 days post-distribution |
| 39-A (Repro Rights) | One ballot initiative campaign (Missouri or Nevada) uses the democratic-participation framing in public communications | Women's law journal assigns the document as supplementary reading | 90 days post-distribution |
| 39-B (Labor Rights) | AFL-CIO or a major state labor federation references the domain document in voter contact materials | EPI cites the domain in labor-democracy analysis | 90 days post-distribution |
| 41-A (Domestic Intel) | ACLU National Security Project or Brennan Center Liberty and National Security Program cites the document; or one Senate Judiciary Democrat uses the Church Committee II frame in public statements | One law school national security clinic adopts the document | 120 days post-distribution |
| 40-A (Const. Architecture) | Common Cause or Wolf-PAC references the domain in their Article V campaign materials | One law school constitutional law clinic assigns the document | 120 days post-distribution |

**Framework-level success metric**: At least 3 of the 9 domains above achieve their primary success metric within 90 days of distribution. This is the adoption-velocity threshold that confirms the Phase 2 feedback-to-research pipeline is working. If fewer than 3 achieve primary success by 90 days, the sequencing logic (not the research quality) should be audited — the signal problem is in distribution timing or audience targeting, not domain content.

---

## Part V: 12-Month Execution Calendar (Post-Phase-1-Launch)

*Phase 1 launch = Week 0 of May 5, 2026*

### Month 1 (May 5 – June 4, 2026)

**Primary activities**:
- Phase 1 Batch 1 outreach wave (Tier 1 contacts — 25 high-leverage)
- Track B: Begin Intel Oversight (38-A) research — production target May 22
- Track B: Begin Tribal Sovereignty (40-B) research — initial sections through May 29; hold SCOTUS section
- Track A: Begin Voting Systems (38-B) research — production target June 5

**Decision gates active**: FISA June 12 deadline; tribal SCOTUS ruling incoming

**End-of-month checkpoint**: FISA extension passed or lapsed; Intel Oversight distributed to Senate contacts; Voting Systems draft in progress

---

### Month 2 (June 4 – July 3, 2026)

**Primary activities**:
- Intel Oversight distributed (first week of June; June 12 deadline coverage)
- Voting Systems distributed by June 20 to election protection organizations
- Gate 1 fires: FISA outcome documented, domain adjusted and distributed
- Gate 3 fires: Phase 1 Week 6 feedback aggregated; Tier assignments confirmed or adjusted
- Track A: Disability Rights (41-B) research begins — if SAVE Act scheduled for Senate, activates as Track B
- Tribal Sovereignty: *Trump v. Barbara* ruling expected; finalize and distribute within 2 weeks of ruling

**Decision gates active**: Phase 1 Week 6 feedback (June 15); SAVE Act Senate timing; *Trump v. Barbara* ruling

**End-of-month checkpoint**: Voting Systems and Intel Oversight both distributed; Tribal Sovereignty in final production; Disability Rights draft in progress

---

### Month 3 (July 3 – August 3, 2026)

**Primary activities**:
- Disability Rights distributed by July 15 (SAVE Act Senate advocacy window)
- Tribal Sovereignty distributed within 2 weeks of *Trump v. Barbara* ruling (likely July)
- Congressional recess begins: Senate in session first week of August only; House has single recess break week Aug 31–Sept 3
- Track A: Reproductive Rights research begins — production target July 25
- Track A-Fill: Fiscal Authority research begins in parallel — production target July 28 (low complexity, 8–10 hours)
- Track A-Fill: Labor Rights research begins — production target July 30

**Congressional calendar note**: Both chambers will be in August recess for most of August; the pre-recess window (July and early August) is the last opportunity to reach congressional staff before the post-Labor Day return. All July distributions should include explicit congressional contact outreach.

**End-of-month checkpoint**: Disability Rights and Tribal Sovereignty distributed; Reproductive Rights, Labor Rights, and Fiscal Authority in late production

---

### Month 4 (August 3 – September 3, 2026)

**Primary activities**:
- Reproductive Rights, Labor Rights, Fiscal Authority distributed in a coordinated wave (August 5–15) before August recess deepens
- Phase 2 feedback collection begins (ballot initiative campaigns, labor unions, think tanks respond to July/August domains)
- Track A: Domestic Intelligence (41-A) research begins — production target September 5
- Congressional recess (most of August): use to target non-congressional audiences (law schools, think tanks, labor unions, ballot initiative campaigns)

**End-of-month checkpoint**: Tier 1 + Tier 2 domains (7 of 9) either distributed or in final production; feedback from July/August distributions beginning to arrive

---

### Month 5 (September 3 – October 3, 2026)

**Primary activities**:
- Domestic Intelligence (41-A) distributed September 15 (before House and Senate return to full legislative session)
- Track A: Constitutional Architecture (40-A) research begins — production target October 1
- Phase 2 feedback aggregation: assess which domains are achieving primary success metrics; adjust Month 6 priorities
- Gate 6: Callais redistricting implementation review — if 3+ states have enacted maps, Domain 38-B update triggered

**End-of-month checkpoint**: 8 of 9 domains produced; Constitutional Architecture in production; feedback assessment complete

---

### Month 6 (October 3 – November 3, 2026)

**Primary activities**:
- Constitutional Architecture distributed by October 15 — before Michigan November ballot decision on Article V rescission
- Pre-midterm distribution: all 9 domains in the hands of all Tier 1 and Tier 2 contacts by October 25
- Midterm prep outreach wave: targeted communications to election protection organizations, state AG offices, and voting rights law clinics with the full Phase 2 set
- Gate 5: Midterm result monitoring (November 3)

**End-of-month checkpoint**: All 9 Phase 2 Tier 1+2 domains distributed; November 3 midterm

---

### Months 7–12 (November 2026 – May 2027)

**Post-midterm Phase 2b and Phase 3 planning**:

*Month 7 (November)*: Midterm results analysis; Gate 5 fires; determine which Tier 3 domains elevate based on congressional composition change. Domain 37 post-midterm update (if Path A+37 was selected) triggered in December 2026.

*Month 8–9 (December–January)*: Phase 3 domain scoping. Domain 41-C (Dark Money) research if midterm produced Democratic Senate gain. Dark Money full-cycle data from 2026 midterm available for the first time. International Human Rights (Domain 41-5) research if UPR preparation timeline warrants.

*Month 10–12 (February–April 2027)*: Phase 2b distribution round to Phase 1 contacts who adopted the framework. Second distribution wave targeting new institutions identified through Phase 2 feedback. Institutional partnership formalization targets: at least one formal NGO, think tank, or law school partnership by Month 12.

---

## Part VI: Risk Register

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| FISA punted beyond June 12 (another short-term extension) | Medium | Low — domain remains relevant regardless of FISA outcome | Update Intel Oversight framing to cover the next deadline; the structural analysis is timeline-independent |
| *Trump v. Barbara* ruling delayed beyond July 2026 | Low-Medium | Medium — Tribal Sovereignty production delayed | Produce all sections except the SCOTUS analysis and hold for ruling; distribute the pre-ruling research as a "stakes" document ahead of the ruling |
| SAVE Act Senate consideration delayed to 2027 | Medium | Low — domain remains relevant; advocacy window for ADA enforcement and SSA staffing restoration remains open | Adjust Disability Rights distribution to focus on SSA/NVRA angle and ADA enforcement rather than SAVE Act-specific provisions |
| Phase 1 generates low feedback volume (below 8% response rate) | Medium | High — delays Phase 2 feedback-loop validation | Fall back to urgency-based sequencing (prioritization matrix) rather than feedback-driven sequencing; proceed with Tier 1 production regardless of feedback volume |
| Research agent capacity insufficient for parallel Track B | Low | Medium — FISA and Tribal Sovereignty cannot be produced simultaneously | Prioritize FISA (June 12 hard deadline) over Tribal Sovereignty; produce Tribal Sovereignty immediately after Intel Oversight completes |
| Callais implementation faster than expected (states act in May 2026) | Medium | Medium — Voting Systems needs faster production | Begin Voting Systems production in parallel with Intel Oversight in May; do not wait for Track A sequence |

---

*Document prepared May 5, 2026. Cross-references: phase-2-domain-prioritization-matrix.md (scoring and rankings), domain-38-40-strategic-analysis.md (candidate deep-dives), phase-2-domain-selection-framework.md (feedback-driven selection logic), measurement-and-iteration-framework.md (success metric infrastructure).*
