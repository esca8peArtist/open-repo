---
title: "Phase 4 Synthesis Framework — Integration Architecture & Gap Analysis"
project: systems-resilience
region: "Midwest US (Zone 5)"
phase: 4
status: synthesis
created: 2026-05-20
word_count: ~3800
audience: "Project lead — synthesis architecture for Phases 1–3, gap identification, Phase 5 decision support"
decision_deadline: 2026-06-01
cross_references:
  - individual/01-water.md
  - individual/02-food.md
  - individual/03-shelter.md
  - individual/04-energy.md
  - individual/05-healthcare.md
  - individual/06-agriculture.md
  - household/01-household-coordination-overview.md
  - phase-3/01-governance-decision-making.md
  - phase-3/02-food-systems-supply-chain.md
  - phase-3/03-information-infrastructure.md
  - phase-3/04-security-and-defense.md
  - phase-3/05-scaling-pathways-and-thresholds.md
  - PHASE_4_IMPLEMENTATION_FRAMEWORK.md
  - PHASE_5_OPTIONS_DECISION_FRAMEWORK.md
---

# Phase 4 Synthesis Framework — Integration Architecture & Gap Analysis

> **Region**: Midwest US (Zone 5) | **Scales**: Individual → Household → Community
> **Phase**: 4 — Synthesis | **Decision deadline**: June 1, 2026
> **Purpose**: Integrate findings from Phases 1–3; map gaps; define Phase 5 path options with decision framework

---

## Most Important Finding

The three phases form a coherent stack, but they do not meet in the middle. Phase 1 covers one person. Phase 3 covers 100+. The household scale (8–25 people) — which is the most common unit for anyone actually planning coordinated resilience — must currently interpolate between two documents written for different scales. This is not a minor documentation gap: it is the primary reason that implementation stalls between "individual hardening" and "community coordination." Phase 5 must choose whether to fill the individual gaps first, build the institutional bridges, or attempt both simultaneously.

The second critical finding: governance and information infrastructure are the load-bearing structures of the entire corpus. Every Phase 3 domain depends on them. Every Phase 5 path must address them. They cannot be deferred to a later planning phase.

---

## Section 1: Load-Bearing Infrastructure Map

### What "Load-Bearing" Means in This Corpus

Not all domains carry equal structural weight. Some domains fail catastrophically if absent; others fail gracefully with improvisation. The distinction determines implementation sequence and Phase 5 prioritization.

**Load-bearing** means: if this domain fails, it takes other domains down with it. The failure is not localized — it cascades.

**Gracefully-failing** means: if this domain fails, the community loses capacity but can continue operating in a degraded state. The failure is painful but not cascading.

### The Load-Bearing Map

**Tier 1 — Foundational (load-bearing, cascading failure):**

- **Governance**: The assembly structure, decision authority, and conflict resolution mechanisms. If governance is absent or illegitimate, food distribution becomes force-governed, security becomes vigilante, and information becomes rumor. Every other domain requires governance authorization to function at community scale. The Phase 3 governance document establishes this clearly: communities in Hurricane Katrina and Maria that improvised governance under food pressure without pre-established authority structures experienced the worst outcomes — not because they lacked food, but because they couldn't make binding decisions about what to do with it.

- **Information Infrastructure**: The communication network and knowledge management system. Governance depends on accurate information to make legitimate decisions. A resource allocation decision made on inaccurate inventory data loses legitimacy when the error surfaces. Information infrastructure is constitutive of governance — not merely useful for it. The Phase 3 information infrastructure document establishes that GMRS radio, skill censuses, and documented inventories must be operational before governance can be formally activated. This is the correct sequence: information first, then governance.

**Tier 2 — Sequential dependencies (fail if Tier 1 is absent):**

- **Food Systems**: Distribution of food resources under scarcity is the highest-conflict governance decision communities face. Food systems logistics (aggregation, storage, distribution) described in Phase 3 are technically sound. But without governance authority behind distribution decisions, the logistics break down immediately. Phase 3's food document and governance document must be read as a pair, not independently.

- **Security**: The Phase 3 security document establishes the counter-intuitive finding that internal conflict — not external threat — is the dominant security burden after the first two weeks. Internal conflicts arise from governance failures (contested decisions) and food failures (perceived distribution unfairness). Security hardware addresses neither cause. Communities with functioning governance and adequate food distribution face dramatically lower security burdens than communities with weapons but no legitimate authority structure.

**Tier 3 — Infrastructure dependencies (require individual stability first):**

- **Water**: Individually gating (failure within days) but does not cascade at community scale in the same way as governance. If one household's water system fails, others can provide water. If governance fails, no one has authority to decide who provides water to whom.

- **Energy**: Individual and household energy systems are largely independent. Community-scale energy coordination matters primarily for load-shedding and critical infrastructure (medical equipment, communication systems). Failure is degrading but not cascading.

- **Healthcare**: Downstream of all other domains. Healthcare failures are amplified by water failure, food failure, shelter failure, and energy failure — but healthcare itself does not cascade into governance or food failure. A community with no medical coordinator struggles; it does not collapse.

### The Dunbar Threshold: 150 People Is the Critical Inflection

The Phase 3 scaling document identifies three cognitive thresholds. Of these, the 150-person Dunbar threshold is the most immediately actionable for Phase 5 planning.

Below 150: Direct assembly governance works. Everyone knows everyone. Trust is personal. Decisions can be made by consensus in a room.

At 150: The cognitive limits of personal-trust-based governance are reached. Communities at this threshold require structural governance — not because people become less trustworthy, but because the brain cannot maintain active trust relationships with more than ~150 people. This is not a social preference; it is a neurological constraint documented across military units, religious communities, corporate divisions, and village anthropology across cultures.

**Phase 5 implication**: Any implementation path that targets 15–50 person groups will hit the 150-person threshold if the community grows, if refugee absorption occurs, or if neighboring groups merge under crisis. The governance restructuring procedures at that threshold must be documented in the charter before crisis arrives, not improvised when population grows. This is the single most important forward-planning action that Phase 5 can deliver regardless of which path is chosen.

---

## Section 2: Cross-Scale Integration Map

### Individual → Household → Community: Where They Connect

The three phases were researched sequentially, not as an integrated system. This creates the 8–25 person gap but also creates integration points that Phase 4 synthesis reveals.

**Water (Individual → Household → Community):**

Individual: 20 liters/person/day, independent filter + storage. Self-contained.
Household (3–6): One shared system with 2 trained operators. The Phase 2 coordination document covers this.
Household (8–25): The Phase 2 document breaks. At 15 people, a system designed for 6 produces water stress. At 25, you need either multiple independent systems or significantly larger capacity with a written maintenance schedule and at least 2 trained operators.
Community (100+): Phase 3 covers aggregated water systems and monitoring. This scale requires a designated water coordinator with formal accountability.

**Integration gap**: 8–25 people. No document addresses the scaling mathematics or the governance structure for shared water systems at this range.

**Food (Individual → Household → Community):**

Individual: 400 sq ft garden, 90-day stored food buffer, foraging + hunting procurement. Phase 1 covers this completely.
Household: Coordinated garden scaling (Phase 2), preservation equipment sharing (Phase 2), food stores coordination (Phase 2).
Household (8–25): 4,000–5,000 sq ft of intensive growing space for caloric near-sufficiency at 15 people. This is 10x the Phase 1 individual scale, requiring coordinated planting schedules, shared preservation equipment, and a documented record of production. Phase 2 covers coordination architecture; Phase 1 provides the per-person mathematics. Neither addresses the combination.
Community (100+): Phase 3 food systems document covers aggregation, storage, distribution networks, and production planning at community scale.

**Integration gap**: 8–25 people, and the handoff from Phase 2 household-scale to Phase 3 community-scale food systems.

**Governance (Individual → Household → Community):**

Individual: No governance document. Individuals make their own decisions.
Household (3–6): One-page charter (Phase 2 household coordination overview). Informal decisions.
Household (8–25): Charter insufficient without meeting cadence, quorum rules, and conflict protocol. No document covers this.
Community (100–1,000): Phase 3 governance document covers delegate councils, accountability mechanisms, conflict resolution structures, and assembly procedures.

**Integration gap**: 8–150 people. Phase 3 governance begins at ~100 people (community scale). The charter-to-council transition is undocumented.

### The Seedwarden Connection

Seedwarden provides two cross-project integration points for Phase 4:

**Veterinary care prerequisite**: Seedwarden's small-scale livestock field manual covers basic animal husbandry (housing, feeding, routine health monitoring). Phase 4 veterinary care — if selected — picks up at health emergency management, obstetric interventions (dystocia in cattle, goats, and pigs is a routine crisis on a working farm), zoonotic disease identification, and emergency slaughter protocols. These are distinct from and build on the seedwarden document. Phase 4 should cite seedwarden as prerequisite, not duplicate it.

**Seed saving and foraging**: Seedwarden's seed-saving field manual, harvest preservation, and native plants guide are fully developed. Phase 4 should not attempt to cover this territory. The connection point for Phase 4 is the community seed library governance structure (who decides what varieties to save, how check-out/renewal works, how to maintain population diversity over multiple seasons) — which is governance, not agronomy.

### The Off-Grid-Living Connection

Six integration points where off-grid-living is the existing depth reference:

1. **Medical care (08-medical-health.md)**: The most complete medical reference in the project ecosystem. Phase 4 psychological support, if selected, extends into mental health, grief facilitation, and winter depression management — it does not duplicate physical care. Off-grid-living is the physical care reference; Phase 4 is the mental health extension.

2. **Tools and fabrication (10-tools-fabrication.md)**: General fabrication, metalworking, woodworking covered. Phase 4 equipment repair, if selected, specializes for Zone 5 Midwest farm equipment failure modes: diesel tractor field repair, small engine maintenance, grain handling equipment, solar/battery fault diagnosis. Off-grid-living is the general foundation; Phase 4 is the specialized farm-equipment layer.

3. **Skills framework (16-skills-knowledge.md)**: The Tier 1–4 competency framework (Novice/Competent/Proficient/Expert) should be adopted by any Phase 4 education document rather than inverted. No parallel framework is needed.

4. **Community organization (13-community-organization.md)**: Covers governance scale patterns. Phase 4 governance expansion builds on this for the 8–150 person range.

5. **Heating and cooling (07-heating-cooling.md)**: Already the reference for Zone 5 shelter-energy integration. No duplication needed.

6. **Disaster scenarios (15-disaster-scenarios.md)**: Phase 3 cascade failure research connects here. No duplication needed.

### The Resistance-Research Connection

Two integration points:

**Information commons and distributed knowledge**: The resistance-research materials on democratic information infrastructure directly inform the offline knowledge library design in Phase 3's information infrastructure document. Phase 4 education or institutional bridge documents should cross-reference this rather than research the same territory independently.

**Governance legitimacy**: Resistance-research's work on democratic resilience parallels the Phase 3 delegate council model. If Phase 5 Option A (community-scale implementation) is selected, governance templates should cross-reference both bodies of work for theoretical legitimacy grounding.

---

## Section 3: Gap Analysis by Scale

### Individual-Scale Gaps (5 Identified)

The following gaps are not about inadequate coverage of documented domains — they are about domains that were never covered or were found to be missing only after Phase 3 revealed what a community actually needs.

**Gap 1 — Education and Pedagogy (planned-but-absent, highest priority)**

This was the original `06-education.md` in PLAN.md and was never built. The individual education document is the only planned document from the original project specification that does not exist. This is not an optional extension — it is a structural absence in the corpus.

What it covers: what to teach when formal schools fail, how to teach it without credentialed instructors, how to manage mixed-age learning groups, what reference materials to prioritize, how the Zone 5 winter indoor period becomes the natural learning window, and how the Kiwix offline server infrastructure enables access to educational content (Wikipedia, Khan Academy, medical references) without internet. Off-grid-living's Tier 1–4 skills framework provides the competency scaffolding; this document provides the pedagogical method.

**Gap 2 — Veterinary Care (agricultural production dependency, high priority)**

Livestock health is a direct food security variable in Zone 5 agricultural context. Loss of a dairy animal or breeding pair to an untreated condition translates to measurable nutritional loss within weeks. Veterinary care is one of the hardest skills to improvise — the knowledge base is large, the stakes per individual animal are high, and the consequences of errors (failed dystocia management, misidentified zoonotic disease) are severe.

Seedwarden covers basic husbandry. Off-grid-living does not cover livestock health at all. The Phase 1 agriculture and food documents cover livestock only in aggregate caloric terms. No document in the corpus covers: routine vaccination schedules for cattle, pigs, chickens, and goats; wound care and limb injuries; obstetric emergencies; zoonotic disease identification; emergency slaughter protocols for sick animals.

**Gap 3 — Psychological Support and Trauma-Informed Care (Zone 5 amplified risk)**

The healthcare document covers acute physical emergencies. It does not cover the dominant health burden in extended disruption: depression, anxiety, grief, PTSD, and interpersonal psychological trauma. Zone 5 winter (November–March) significantly amplifies this: seasonal affective disorder is endemic even under normal conditions; extended disruption compresses sleep, increases isolation, and removes normal coping structures.

A community without anyone trained in psychological first aid, grief facilitation, or basic crisis support frameworks will experience cumulative social deterioration. This is not a clinical requirement — WHO's Psychological First Aid field guide describes lay-person-applicable frameworks specifically designed for resource-constrained environments.

**Gap 4 — Farm Equipment Repair (Zone 5 farm-specific)**

The Phase 4 scoping document and PHASE_4_RESEARCH_INITIALIZATION.md both identify this gap, and off-grid-living's general tools document establishes the foundation. What is absent: Zone 5 Midwest farm-specific repair protocols. A failed tractor during planting season in a Zone 5 community represents a catastrophic agricultural production shortfall. The failure modes for diesel tractors (fuel system, hydraulics, alternator), small engines (chainsaw, tiller), grain handling equipment, and solar/battery systems require specialized knowledge distinct from general toolworking.

**Gap 5 — Conflict Resolution and Mediation (governance facilitation)**

Phase 3 governance documents describe structural mechanisms — delegate councils, accountability procedures, assembly quorum. They do not address the facilitation skills needed to operate these mechanisms under stress. A community mediator must: de-escalate interpersonal conflicts before they reach assembly, facilitate meetings where resource allocation is contested, distinguish between conflicts resolvable through process and those requiring removal decisions. These are learnable skills with established frameworks (interest-based negotiation, restorative circles) that are entirely absent from the corpus.

This gap is partially covered by the Phase 3 governance document's structural language, but the facilitation skills layer — what does the mediator actually do in the room — is missing.

### Household-Scale Gaps (1 Primary)

**The 8–25 Person Scaling Gap**

Phase 2 covers 3–6 people. Phase 3 covers 100+. The most common scale for intentional resilience planning — extended family networks, neighborhood clusters, rural cooperative households — falls in the 8–25 person range that has no dedicated documentation.

This is not about adding new domains. It is about scaling the existing five household coordination documents (water, food, energy, healthcare, and the overview) to a range that is 3–4x larger than Phase 2 assumed. The specific scaling points where Phase 2 breaks:

- Water: Multiple systems or significantly larger capacity required at 15+ people
- Food: 10x growing space, coordinated preservation, documented inventory (not informal shared awareness)
- Energy: Designated energy coordinator, written load-shedding tiers, weekly load planning
- Healthcare: Two TCCC/WFR-trained coordinators (not one), written health histories for all members
- Governance: Charter plus monthly meeting cadence, quorum rules, explicit conflict protocol

The 8–25 person household is the most underserved scale in the entire corpus. Phase 5 path selection should consider whether addressing this gap directly is higher-leverage than either the individual gaps (Gap 1–5 above) or the institutional bridge layer.

### Community-Scale Gaps (Noted, Largely Addressed)

Phase 3 is the most complete of the three phases. Five domains at 100–1,000 person scale with 28,700+ words and 170+ citations. The community-scale documents are production-ready.

The residual community-scale gaps are:

**Economic resilience**: How a community-scale economy functions without dollar-based systems (barter, mutual credit, cooperative finance) is mentioned in Phase 2 but not operationalized in Phase 3. This was not in scope for Phase 3.

**Legal structure interface**: How an informal mutual aid network enters contracts, holds property collectively, or accesses government resources legally. Phase 3 describes governance but not legal standing.

Both of these are more appropriately addressed in Phase 5 institutional bridge work (Option B or hybrid) than as Phase 4 gap-filling.

---

## Section 4: Phase 5 Path Option Architecture

This section establishes the decision architecture for the three Phase 5 paths. Full decision framework with scope, hours, timelines, and success metrics is in `PHASE_5_OPTIONS_DECISION_FRAMEWORK.md`. This section provides the synthesis-level rationale.

### Option A: Individual-Scale Gap Filling

**What it addresses**: The five individual-scale gaps identified above (education, veterinary care, psychological support, farm equipment repair, conflict resolution). This option deepens the individual/household layer before moving outward.

**Synthesis rationale**: Phase 1 is strong in physical domains (water, food, shelter, energy, healthcare, agriculture) but the education document was never built and three additional high-impact gaps (veterinary, psychological, equipment repair) were discovered only after Phase 3 revealed community operational needs. A community implementing Phase 3 governance and food systems protocols will quickly encounter these gaps: children needing instruction, livestock needing care, equipment failing without repair knowledge, conflicts needing facilitation, and people struggling psychologically through Zone 5 winters.

**Load-bearing analysis**: Option A gap-filling is not load-bearing in the governance/information infrastructure sense, but it is directly operationally enabling for any community that is actually functioning. You cannot implement Phase 3 food systems without veterinary care for livestock. You cannot implement Phase 3 governance without conflict resolution facilitation skills. You cannot sustain Phase 1 equipment without repair protocols.

**Connection to Phase 3**: Education → Phase 3 information infrastructure (the Kiwix server design in Phase 3's document is an information system; the pedagogy for using it is an education document). Veterinary care → Phase 3 food systems (livestock health directly affects food system output). Psychological support → Phase 3 security (psychological deterioration is a security risk; the Phase 3 security document identifies internal conflict as the primary threat). Conflict resolution → Phase 3 governance (the structural mechanisms exist; the facilitation skills to run them do not).

### Option B: Household-Scale Institutional Bridges

**What it addresses**: The interface layer between informal household networks and surviving institutions (rural clinics, legal structures, schools). This option is higher-complexity research (the documentary record for these interfaces is thinner) but potentially higher strategic value for Phase 5 implementation planning.

**The three highest-leverage bridges:**

*Clinic relationships*: Rural FQHCs and critical access hospitals have staff with teachable skills (wound care, medication management, chronic disease monitoring), pharmaceutical supplies accessible through community agreements, and diagnostic equipment that can be community-maintained. Pre-crisis skill-sharing relationships extend clinic capability into the community and extend the community's healthcare independence from the clinic. This bridge runs in both directions.

*Legal structure*: A 150-person mutual aid network has no legal standing. It cannot enter contracts, hold property collectively, or access government cost-share programs (NRCS EQIP, FEMA BRIC) without legal organization. The lightest-weight legal vehicles in Midwest states — agricultural cooperatives, nonprofit 501(c)(3)s, LLC structures, township commissions — each have different access profiles and administrative burdens. This research question has significant regional variation and requires state-specific investigation.

*Schools as resilience hubs*: A rural school building is typically the largest, most energy-intensive, most structurally sound building in a small community. When schools close, the infrastructure does not disappear. Research questions: what protocols govern community access to school buildings, how do household networks support educational continuity, and what curriculum records should be preserved?

**Load-bearing analysis**: Option B institutional bridges are not immediately load-bearing for Phase 3 implementation, but they become increasingly important as implementation matures. A community that has functioning governance, food systems, and information infrastructure will hit the institutional interface wall when it needs legal standing, medical backup, or school space. Without pre-established relationships, these interfaces must be improvised under pressure.

**Connection to Phases 1–3**: Clinic bridge → Individual healthcare (Phase 1) + household healthcare coordination (Phase 2) + Phase 3 information infrastructure (medical records, skill census). Legal structure → Phase 3 governance (governance needs legal standing to operate beyond informal mutual aid). Schools → Phase 4 education gap + Phase 3 information infrastructure (school as knowledge hub location).

### Hybrid Option: Combined Approach with Critical Path

**What it addresses**: Two individual-scale gaps (education and veterinary care, the highest-impact and most Zone 5-specific) combined with two institutional bridges (clinic relationships and legal structure, the highest-leverage and most Phase 5-enabling).

**Synthesis rationale for this specific combination**:

- Education + veterinary care are the two gaps most likely to be encountered in the first year of Phase 3 implementation. Education was planned but never built; veterinary care directly affects food security.
- Clinic relationships and legal structure are the two bridges most required for Phase 5 community-scale implementation. Without legal standing, governance remains informal. Without clinic relationships, healthcare is entirely self-reliant.
- This pairing avoids the hybrid's usual weakness (diluted coverage across too many fronts) by targeting the highest-priority item from each option rather than attempting all of either option.

**Critical path within hybrid**: Education first (foundational — the Kiwix offline server serves both knowledge preservation and educational infrastructure, and it connects to the information infrastructure work already in Phase 3). Veterinary care second (food security dependency — this is the gap most likely to produce measurable harm if left unfilled). Legal structure third (enables everything that follows in institutional bridge work — without legal standing, clinic relationships and school access agreements cannot be formalized). Clinic relationships fourth (builds on legal structure; creates pre-crisis relationships that extend healthcare capacity).

---

## Section 5: Success Metrics Framework

### What Good Looks Like (Not Just That Documents Exist)

Success metrics serve two purposes: confirming that implemented systems work, and providing early warning when they are degrading before they fail. Documents existing on a server are not success. Systems functioning under test conditions are success.

### Phase 4 Document-Level Success Metrics

**Education and Pedagogy document**:
- Piloted by 3+ test readers (at least one with school-age children)
- Kiwix server setup guide tested on actual Raspberry Pi hardware
- Learning pod curriculum outline used by at least one informal group for 30+ days
- Knowledge audit template completed for at least one test community

**Veterinary Care document**:
- Reviewed by at least one practicing large-animal veterinarian or agricultural extension agent
- Emergency calving/kidding procedure tested in simulation (walkthrough with livestock owner)
- Zoonotic disease identification guide cross-referenced against USDA APHIS diagnostic resources
- Vaccination schedule tables verified against current AVMA recommendations

**Psychological Support document**:
- Reviewed by at least one mental health professional with rural or disaster-context experience
- Psychological First Aid (WHO) checklist adapted for Zone 5 winter context
- Grief facilitation framework piloted in at least one community discussion setting

**Farm Equipment Repair document**:
- Each procedure walkthrough tested against a specific equipment failure scenario
- Spare parts inventory cross-referenced against parts availability in rural Midwest supply chains
- At least 2 Zone 5 case studies from actual farmers or extension service records

**Conflict Resolution document**:
- Mediation framework piloted in at least one tabletop exercise
- Role descriptions for community mediator tested against actual Phase 3 governance structure
- Restorative practices procedure reviewed against Phase 3 conflict resolution mechanisms (no duplication)

### Cross-Domain Phase 5 Success Metrics

**At Month 3 post-decision** (immediate implementation):
- Governance setup complete for chosen scale (charter ratified, coordinators designated, meeting cadence established)
- Resource inventory conducted (food, fuel, medical, tools, skills — documented location and quantity)
- Communication system tested (GMRS for groups; phone trees for individuals)

**At Month 6**:
- Individual water supply operational for all members (72-hour test passed)
- 90-day food reserve documented and accessible
- Community assembly has met 6+ times with decisions documented
- At least one conflict resolved through formal mediation process
- Succession plan exists for every domain specialist role

**At Month 12**:
- Scaling thresholds documented in charter (150-person transition plan pre-approved by assembly)
- Option-specific milestones (see PHASE_5_OPTIONS_DECISION_FRAMEWORK.md for path-specific metrics)
- Knowledge transfer begun for every critical skill (not just one person holding each domain)

### The 6-Month Viability Test (Inherited from Phase 4 Framework)

A community that can pass all of the following at 6 months has sufficient implementation integrity to survive extended disruption:

- [ ] Independent water supply operational for all members (72-hour test passed)
- [ ] 90-day food reserve documented and accessible
- [ ] Community assembly has met at least 6 times, decisions documented
- [ ] GMRS radio network tested, all coordinators equipped
- [ ] At least one conflict resolved through formal mediation process
- [ ] Resource inventory (food, fuel, medical) maintained and current
- [ ] Succession plan exists for every domain specialist role
- [ ] Scaling thresholds and governance restructuring procedures documented in charter

**Failure on any of these at 6 months is not a catastrophe — it is a signal of which system needs immediate attention before crisis arrives.**

---

## Section 6: Quick-Start Phase 4 Modules (Launchable Post-Decision)

These modules launch immediately after June 1 decision with zero additional research required. They are derived from existing Phase 3 documents and existing Phase 4 architecture documents.

### Module 1: Governance Setup for 15–30 Person Groups

**Why it can start immediately**: Phase 3 governance document provides the full theoretical framework. The PHASE_4_IMPLEMENTATION_FRAMEWORK.md provides the household-to-community scaling sequence. A governance setup module synthesizes these into a 1–2 page operational template for groups below the community-scale threshold.

**Content**: One-page charter template (decision procedures, coordinator roles, conflict protocol, meeting cadence) + coordinator designation worksheet + monthly meeting agenda template + the 6-month viability checklist calibrated to 15–30 person scale.

**Who can use it immediately**: Any household network or neighborhood cluster regardless of which Phase 5 path is selected. Governance setup is path-agnostic.

**Time to launch**: Same day as decision. No new research required.

### Module 2: Resource Inventory and Skill Census

**Why it can start immediately**: Phase 3 information infrastructure document provides the design. Phase 4 implementation framework provides the sequence and the specific forms needed.

**Content**: One-page household resource inventory form (food stores, fuel, medical supplies, tools, equipment) + one-page community skills census form (medical, mechanical, agricultural, communication, legal expertise) + update schedule (weekly for food, monthly for others) + communication system setup checklist (GMRS channel assignments, contact list format).

**Who can use it immediately**: Any group, any path.

**Time to launch**: Same day as decision.

### Module 3: Education Quick-Start (Path A or Hybrid)

**Why it can start immediately**: Kiwix setup is documented in PHASE_4_SCOPING.md Section 4. Off-grid-living's skills framework is the competency scaffolding. The module synthesizes these into a setup guide.

**Content**: Kiwix server setup on Raspberry Pi (hardware list, software installation, ZIM file selection for Zone 5 Midwest context) + community knowledge audit template (who knows what, what's documented, what's at single-point-of-failure risk) + apprenticeship pairing worksheet (mentor + learner + skill domain + milestone dates).

**Who can use it immediately**: Groups selecting Option A or Hybrid. Works immediately without the full education document.

**Time to launch**: 3–5 days post-decision (Raspberry Pi sourcing may have lead time).

### Module 4: Governance Drill (Tabletop Exercise)

**Why it can start immediately**: Phase 3 governance document describes the contested resource allocation scenario as a testing mechanism. This module operationalizes it.

**Content**: A structured 90-minute tabletop exercise in which a facilitator presents a contested resource allocation scenario (heating fuel shortage, food distribution dispute, or new member admission decision) to the group and measures: time to decision, participation rate, acceptance of outcome, and whether the resolution mechanism was used. This is the governance legitimacy test from the success metrics framework.

**Who can use it immediately**: Any group with a ratified charter.

**Time to launch**: Same day as decision. Requires a facilitator and a charter — nothing else.

---

## Cross-Project Overlap Risk Register

The following document pairs have overlap risk that Phase 4 and Phase 5 should actively avoid:

| Domain | Existing Coverage | Phase 4/5 Scope | Risk if Duplicated |
|---|---|---|---|
| Physical medical care | off-grid-living/08-medical-health.md | Mental health extension only | Wasted effort; inconsistent clinical guidance |
| General tools/fabrication | off-grid-living/10-tools-fabrication.md | Zone 5 farm equipment only | Diluted specificity |
| Livestock husbandry basics | seedwarden/small-scale-livestock-field-manual | Emergency care and obstetrics only | Undermines seedwarden as prerequisite |
| Seed saving and preservation | seedwarden/seed-saving-field-manual + harvest-preservation | Community seed library governance only | Duplicates seedwarden unnecessarily |
| Governance structure | Phase 3/01-governance-decision-making.md | Facilitation skills only (not structure) | Contradicts Phase 3 structural model |
| Information commons | resistance-research materials | Cross-reference only | Parallel knowledge bases diverge |

---

## Summary: Phase 4 Status and Phase 5 Readiness

**Phase 1 (Individual)**: 8 documents complete (water, food, shelter, energy, healthcare, agriculture, moisture extraction, plus the PLAN.md). Education document planned but never built. Five additional gaps identified.

**Phase 2 (Household)**: 5 household coordination documents complete (overview + water, food, energy, healthcare). Covers 3–6 people. 8–25 person range is undocumented.

**Phase 3 (Community)**: 5 community-scale documents complete (28,700+ words, 170+ citations). Governance, food systems, information infrastructure, security, scaling pathways. Most complete phase in the corpus.

**Phase 4 (Synthesis)**: Architecture complete (this document + PHASE_4_IMPLEMENTATION_FRAMEWORK.md + PHASE_4_SCOPING.md). Research not yet initiated. Awaiting June 1 path decision.

**Phase 5**: Decision gate June 1, 2026. Three paths available. See `PHASE_5_OPTIONS_DECISION_FRAMEWORK.md`.

**The corpus is production-ready for Phases 1–3.** Phase 4 research is the next execution step. Phase 5 path selection enables immediate execution post-decision with zero setup lag using the quick-start modules above.

---

*Phase 4 Synthesis Framework completed: 2026-05-20*
*Phase 5 decision deadline: June 1, 2026*
*Execution begins: June 2, 2026*
