# Systems Resilience Phase 7+ Roadmap

**Document purpose**: Post-June-3 decision execution planning for orchestrator use
**Prepared**: June 2, 2026
**Decision gate**: June 3, 2026 (platform + author selections)
**Publication gate**: June 5, 2026 13:00 UTC

---

## Part 1: Phase 6 Completion State at the June 3 Decision Gate

When the user confirms platform and author decisions on June 3, the following work is already complete and requires no additional autonomous effort:

**Research corpus (complete and committed):**

- Phase 5: 66,442 words across 12 documents, 423 citations, zero placeholders. Wave 1+2 locked for June 5 publication (45,380 words). Wave 3 complete and pending.
- Phase 6 pre-research committed May 26: Farm Equipment Repair Track A (44,000+ words, 78 sources); Meshtastic Communications Track B (15,600 words, 71 sources).
- Domain A pre-research outline (Community Economic Resilience): complete source library (75-80% readiness), Zone 5 application notes, timeline estimate. File: `phase-6-candidate-community-economic-resilience.md`.
- Domain C pre-research outline (Skills Development): complete. File: `phase-6-candidate-skills-development.md`.
- Domain D pre-research outline (Governance Scaling): complete. File: `phase-6-candidate-governance-scaling.md`.

**Platform infrastructure (NOT yet built — awaits June 3 user decision):**

- Option A (Discourse self-hosted): 6-8 hours of technical setup needed on June 3-4.
- Option B (Mighty Networks): 3-4 hours of configuration needed on June 3.
- Option C (Nextcloud + Matrix on raspby1): 6-10 hours of setup needed on June 3-5.

**Author recruitment (NOT yet confirmed — awaits June 3 decision):**

- 18 personalized outreach emails are copy-paste ready (see `PHASE_6_AUTHOR_RECRUITMENT_TEMPLATES.md`). No author has accepted as of June 2. The auto-fallback (self-execute via Orchestrator) activates June 3 if the user selects that path or if no author is confirmed.

---

## Part 2: What Phase 7 Accomplishes

Phase 6's ten candidate domains (A through J) are the content production engine. Phase 7 is the operationalization and distribution layer. The knowledge corpus exists; Phase 7 converts it into working community infrastructure and external reach.

Phase 7 has three goals:

**Goal 1 — Content completion (all ten domains).**
Phase 6 launches Domains A, C, D in Week 1 and Domains E, F, H, I in Weeks 2-3. Domains B, G, J are Week 3+ and not guaranteed complete before August 31. Phase 7 either completes the remaining domains or formally closes Phase 6 scope and accepts the corpus as-is.

**Goal 2 — Distribution and outreach.**
The corpus must reach practitioners: cooperative developers, community emergency response teams, Transition Town networks, Mutual Aid Hub organizers, county extension offices (Iowa State, University of Wisconsin, University of Illinois), and Zone 5 homesteading communities. The activation checklist specifies 50+ organizational contacts per domain. Phase 7 executes distribution.

**Goal 3 — Community platform operations.**
Whichever platform is selected on June 3 must be operationally active: 8-12 community builders onboarded, knowledge base populated, monthly governance cycles running via Loomio (if adopted), and a sustainable volunteer coordination cadence established.

---

## Part 3: Implementation Dependencies Before Phase 7 Can Start

Phase 7 cannot begin until:

1. **At least three Phase 6 domains are published** (not just drafted — committed to the GitHub Pages site and accessible). Target: July 15 for Domains A, C, D based on the hybrid execution model.
2. **Community platform is operational** with at least five active volunteer builders. Without minimum community mass, there is no audience for Phase 7 distribution or co-authoring.
3. **Phase 5 Wave 1+2 has been live for at least 30 days** (i.e., July 5 if published June 5). The Wave 1+2 corpus is the proof-of-quality that recruitment emails and outreach cite. Distribution without a live publication has no anchor.
4. **User review of first Phase 6 drafts** (checkpoint at July 13-15). Phase 7 scoping depends on what the user approves for Phase 6 publication. If domains are redirected or reduced in scope at the July checkpoint, Phase 7 changes accordingly.

Earliest Phase 7 start: **July 15, 2026**, assuming the hybrid execution model stays on schedule, Domains A/C/D publish on time, and platform community reaches minimum mass.

Realistic Phase 7 start: **August 1, 2026**, giving buffer for the July 13 checkpoint review and any domain revisions.

---

## Part 4: Week-by-Week Execution Roadmap (June 5 to August 31)

### Phase 6 Active Window: June 5 — July 31

**Week 1 (June 5-11): Platform live + Domain research begins**

- June 5: Phase 5 Wave 1+2 published to GitHub Pages (45,380 words). Email announcement sent.
- June 5-8: Platform operational (Option A/B/C per user selection). First 5 community builders invited.
- June 5-9: Author onboarding — human author or self-execute path activated.
- June 8-11: Domain A, C, D research sprints begin (parallel, independent).

**Week 2 (June 12-18): Domain research in progress + Wave 3 editorial**

- June 10-14: Wave 3 editorial pass (cross-references to Wave 1+2 added; 10-15 hours). No new content.
- Domain A, C, D: each at approximately 40-50% draft. Checkpoint: have 25+ sources documented.
- Platform: second cohort of builders (6-10 total) onboarded; first discussion threads created.

**Week 3 (June 19-25): Domain drafts at 80% + Wave 3 publication prep**

- Domain A, C, D: first complete drafts. Author review + Orchestrator editorial pass.
- June 28-30: Phase 5 Wave 3 publication target (22,821 words, Option A staging).
- Domain E (Mutual Aid Networks) research begins — depends on governance framing from Domain D.

**Week 4 (June 26 — July 2): Domain A, C, D final editorial + Wave 3 live**

- Domain A, C, D: final editorial passes. Citation audit. Zero placeholders verified.
- June 30: Phase 5 Wave 3 published. Full 66,442-word corpus now public.

**Week 5-6 (July 3-16): Checkpoint preparation + July 13 gate**

- Domain A, C, D: submitted for user review ahead of July 13 checkpoint.
- July 13: User reviews Domain A, C, D drafts. Decision: publish as-is, revise, or hold.
- If approved: Domain A, C, D committed to master; GitHub Pages updated.

### Phase 7 Entry Window: August 1 — August 31

**Week 9 onwards (August 1+): Phase 7 launch — distribution begins**

Phase 7 starts with the domains that are published and approved. Distribution package assembled for each published domain with Gist templates, Tier 1 contact lists (50+ organizations per domain), and email sequences (3-touch outreach).

---

## Part 5: Decision Tree by Platform Choice

**If Option A selected (Discourse self-hosted):**
- Phase 6 execution: Discourse online by June 4 (DNS propagation June 3 → June 4).
- Phase 7 implications: Strongest integration with GitHub Pages publication site; embed widgets surface community discussion alongside documentation.
- Constraint: No collaborative document editing (requires external tools or wiki posts).

**If Option B selected (Mighty Networks):**
- Phase 6 execution: Functional community in 2-3 hours on June 3.
- Phase 7 implications: Best mobile engagement; native iOS/Android apps maximize volunteer engagement.
- Constraint: API locked to paid tiers; community and publication in separate silos. Highest vendor lock-in risk.

**If Option C selected (Nextcloud + Matrix on raspby1):**
- Phase 6 execution: 6-10 hours of Docker setup on June 3-5.
- Phase 7 implications: Only option supporting native collaborative document editing. Full off-grid capability.
- Constraint: Two UX surfaces (Nextcloud + Element); higher onboarding burden; no native push notifications.

---

## Part 6: Risk Factors That Could Delay Phase 7

**Risk 1: Author delivery failure (HIGH impact, MEDIUM probability)**
Trigger for escalation: Author has not submitted a 20% draft by June 22. Response: Orchestrator takes over remaining scope.

**Risk 2: Platform stability (MEDIUM impact, LOW probability)**
Mitigation: Three implementation guides are production-ready with conservative time estimates.

**Risk 3: Community builder recruitment stalling (HIGH impact, MEDIUM-HIGH probability)**
Mitigation: Publishing Wave 1+2 before recruiting gives outreach emails a live, substantial artifact to point to.

**Risk 4: User approval delays at checkpoints (MEDIUM impact, MEDIUM probability)**
Mitigation: Pre-stage review checklist in each domain document for quick user approval. Target 3-day user review window.

---

## Part 7: Phase 7 Milestone Summary

| Milestone | Target Date | Dependency |
|---|---|---|
| Platform operational | June 5 | User June 3 decision |
| Phase 5 Wave 1+2 published | June 5 13:00 UTC | No blocking dependencies |
| First 5 builders onboarded | June 8 | Platform live |
| Phase 5 Wave 3 published | June 30 | Editorial pass complete |
| Domain A, C, D first drafts | July 10 | Author or self-execute |
| July 13 checkpoint — user review | July 13 | Draft delivery |
| Domain A, C, D published | July 15 | User approval |
| Phase 7 entry | August 1 | Three domains published + 8 builders active |
| Distribution package assembled | August 1-7 | Published domains |
| Tier 1 outreach begins | August 1 | Distribution package |
| September 1 user review | September 1 | All August deliverables |

---

**Confidence level**: High for timeline structure and dependency sequencing. Medium for community builder recruitment projections. Medium-low for Phase 7 distribution impact.

**Primary uncertainties**: Community platform will have zero active members until user completes June 5-8 recruitment. Author delivery confidence is 85% (human author) vs 95% (self-execute orchestrator path). Platform stability is low-risk for all three options, but Mighty Networks has highest vendor lock-in risk if pricing increases.
