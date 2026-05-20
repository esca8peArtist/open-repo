---
title: "Community Implementation Playbook — Tier 3 Coordination Framework"
project: systems-resilience
region: "Midwest US (Zone 5)"
phase: 5
tier: 3
scale: community
scale_range: "50–150 people (federation of 5–10 households)"
status: preliminary-draft
draft_depth: "35% — structure complete, section summaries written, key citations staged"
created: 2026-05-20
target_words: 8000–9000
target_citations: 35–45
dependencies:
  - phase-5/tier-2-household-coordination-infrastructure-guide.md
  - phase-5/tier-2-veterinary-care-guide.md
  - phase-5/tier-2-psychological-support-guide.md
  - phase-5/tier-2-conflict-resolution-deep-dive.md
  - phase-3/01-governance-decision-making.md
  - phase-3/02-food-systems-supply-chain.md
  - phase-3/03-information-infrastructure.md
  - phase-3/04-security-and-defense.md
  - phase-3/05-scaling-pathways-and-thresholds.md
wave_2_sequencing_note: "MUST BE LAST. All four Tier 2 Phase 5 documents must be in first-draft form before this document is written. Section 4 is structurally dependent on those drafts."
critical_prerequisite: "Do not begin writing this document until Veterinary Care, Psychological Support, and Conflict Resolution are in first-draft form."
---

# Community Implementation Playbook
## Tier 3 Coordination Framework: From Households to Community

> **Region**: Midwest US (Zone 5) | **Scale**: 50–150 people (federation of 5–10 households)
> **Phase**: 5 — Integration Capstone | **Tier**: 3 — Community Coordination
> **CRITICAL PREREQUISITE**: All Phase 5 Tier 2 documents must be complete before this document enters full production

---

## The Most Important Finding

The question that Phase 5's Tier 2 documents collectively leave unanswered is the hardest one: when your household has functioning governance, a trained conflict facilitator, veterinary protocols, and psychological support infrastructure — how do you federate with the household 0.8 miles down the road? Phase 3 describes community governance at 100+ people. This document describes the transition — the specific steps, structures, and decision gates that take a cluster of internally coherent households and build them into a functioning community.

The critical finding from studying long-running communities: the federation threshold is not reached by accumulating people. It is reached by accumulating governance capacity and then adding people to it. Communities that attempt to scale horizontally before building vertical governance capacity (the internal household layer documented in Phase 5 Tier 2) fragment. The reason is predictable: informal personal-trust-based governance works only until the group exceeds the cognitive capacity for direct personal relationships. Elinor Ostrom's eight design principles for governing the commons, derived from 800+ documented cases across six continents, specify that successful commons governance requires defined membership, participatory rule modification, and nested tiers — all of which require a functioning internal governance layer before federation is possible. [1][2]

The Zone 5 Midwest context adds one factor that most community resilience literature does not address: the Zone 5 homestead cluster is already spatially distributed. Households are not in a shared building or a close neighborhood — they may be 0.5–5 miles apart. Federation must account for winter travel constraints, physical communication limits, and the practical reality that a delegate council cannot meet daily in January across 5 miles of unplowed roads. The information infrastructure solutions (AREDN mesh, runner protocol from the Household Coordination guide) are the physical layer; this document provides the governance layer that runs on top of them.

---

## Section 1: The Federation Problem — From Households to Community

### The Dunbar Threshold and Why It Matters

Dunbar's number — approximately 150 — identifies the cognitive limit for stable social groups that depend on personal relationships for governance. [3] Beyond this threshold, governance must formalize: written rules replace known reputations, representative structures replace direct participation, and enforcement mechanisms must be explicit rather than implicit.

The threshold is not a hard wall; it is an inflection point. The typical failure pattern: a community cluster reaching 60–100 people discovers that its informal consensus process (which worked well at 20–30) produces paralysis or resentment at scale. The original core group's decision-making norms no longer serve a larger body. New members lack the social history that made informal governance functional. The community fractures into competing sub-groups, each with its own informal norms.

The solution — building formal governance capacity *before* reaching the threshold — is straightforward in principle and politically difficult in practice. Every pre-threshold governance decision faces resistance from some members who experienced the informal system as more authentic. The Phase 3 governance document addresses this directly (the transition planning process); this document focuses on the household-to-federation step that precedes it.

### Four Federation Models for Zone 5 Application

**Delegate Council** (recommended primary model for Zone 5 household clusters):
- Each household selects a delegate with a defined mandate and term
- Delegates meet as the inter-household coordinating body for shared decisions
- Decisions requiring consensus of all households are escalated to a household assembly process
- Case studies: Zapatista EZLN community councils; Rojava canton-level governance; the Phase 3 governance document's primary model
- Zone 5 applicability: High. Works with spatially distributed households. Winter communication constraints are addressed by pre-establishing proxy authority and asynchronous decision protocols.

**Working Group Federation**:
- Issue-specific cross-household working groups (food, water, security, health) with rotating leads
- No standing delegate council; coordination happens through domain-specific working groups
- Case studies: Twin Oaks and East Wind at 70–100 person scale [4]
- Zone 5 applicability: Moderate. Works well for functional coordination but produces governance gaps when disputes arise that span multiple domains.

**Sociocratic Circle Organization**:
- Domain circles with representatives to a general circle
- Consent-based decision-making (objections addressed before decisions proceed, not veto-based)
- Case studies: Cohousing communities at 15–50 household scale; increasing adoption in Midwest intentional communities
- Zone 5 applicability: High for communities with the time to invest in sociocracy training. Higher training requirement than delegate council.

**Ostrom Commons Governance**:
- Nested tiers of authority for specific shared natural resources (water systems, shared land, grain storage)
- Not a complete governance system but the appropriate structure for any shared resource commons
- Essential for Zone 5 communities sharing a water source, common land, or significant stored resources
- This is not an alternative to delegate council or sociocracy — it is a complement for the specific resources that require commons-style governance

**Recommendation for Zone 5 household clusters starting from scratch**: Delegate council as the inter-household governance structure, with sociocratic circle organization as an aspirational upgrade once 12+ months of delegate council functioning is established, and Ostrom commons governance for any shared resource that is held in common from the start.

**Source anchors**: Ostrom [1]; Life with Alacrity Revised Ostrom [2]; Dunbar [3]; Twin Oaks SIT capstone [4]; PMC 9118649 [5]; Rojava/Chiapas autonomous institutions [6]; Sociocracy For All [7]; Cohousing Association [8].

---

## Section 2: Shared Resource Governance — The Commons Problem

### When Households Share Resources, They Create a Commons

Any resource that multiple households share access to — a water cistern, a root cellar, a seed library, shared farming equipment, a community grain purchase — is a commons: a shared resource with potential for over-exploitation or under-maintenance by individual free-riders. This is not a cynical observation about human nature; it is a structural reality about resources without clear individual ownership. Ostrom's contribution was demonstrating that communities can govern commons successfully without either privatization or top-down control, when they apply a set of identifiable design principles. [1]

### Ostrom's Eight Design Principles Applied to Zone 5 Shared Resources

The eight principles, with Zone 5 household cluster application for each:

**1. Clearly defined membership and boundaries**
Who has access to the shared resource? This must be explicit. For a shared water cistern: which households have draw rights? What is the maximum draw per household per week? New household integration must include explicit commons access onboarding.

**2. Rules match local conditions**
Resource governance rules must fit the actual resource and the actual community. Generic templates fail. The Zone 5 water commons in winter is a different resource than in summer — draw rates, freeze risk, priority allocation in shortage all require Zone 5-specific rules.

**3. Collective choice arrangements**
Those who use the commons have meaningful input into its rules. In the household cluster: all households with commons access have a voice in commons governance. This is not the same as the household cluster's general governance — it is specific to each shared resource.

**4. Effective monitoring**
Usage must be monitored. For food storage: documented deposits and withdrawals with timestamps. For water: usage records. For seed library: check-out records and germination rate reporting for returned seeds. Monitoring is not surveillance — it is the information system that enables trust.

**5. Graduated sanctions**
Overuse or breach of commons rules is addressed through escalating consequences: conversation first, formal warning second, temporary access restriction third, membership review for pattern violations. This prevents the situation where a household loses access entirely for a first offense, creating resentment and retaliation.

**6. Conflict resolution mechanisms**
The commons requires its own dispute resolution mechanism for commons-specific conflicts (contested usage records, allocation disputes). This can be the household cluster's existing conflict resolution infrastructure, but it must be explicitly designated for commons disputes — not assumed.

**7. Minimal recognition of rights to organize**
The commons governing body must have recognized legitimacy. If a household cluster's commons governance decisions can be overridden by an outside authority (a landowner, a government body, an individual with property rights), the commons will collapse whenever it is under pressure. Zone 5 homestead clusters must pay attention to property rights structure when establishing shared resources.

**8. Nested governance for large-scale commons**
For commons that span more than 4–5 households or involve significant infrastructure, nested governance — sub-groups managing sub-resources under an overarching framework — is more durable than flat governance. Example: a shared watershed managed at the sub-watershed level with inter-household coordination for overall resource allocation.

### Zone 5 Shared Resource Types and Governance Notes

| Resource Type | Primary Commons Risk | Key Ostrom Principle | Zone 5 Specific |
|---|---|---|---|
| Water system (shared well or cistern) | Free-rider draw in shortage; infrastructure maintenance neglect | Rules match local conditions; Monitoring | Winter freeze risk management; spring snowmelt recharge window |
| Root cellar / food storage | FIFO discipline failure; unequal deposit/withdrawal; spoilage accountability | Monitoring; Graduated sanctions | Zone 5 winter temperature management; spring transition vulnerability |
| Seed library | Germination rate degradation; variety loss; no return after borrowing | Effective monitoring; Collective choice | Zone 5 seed storage conditions (temperature, humidity); spring seed selection pressure |
| Shared equipment (tractors, tillers, saws) | Maintenance neglect; damage accountability; priority conflicts at peak season | Graduated sanctions; Conflict resolution | Compressed Zone 5 planting and harvest windows create peak demand conflicts |

**Source anchors**: Ostrom [1]; Life with Alacrity [2]; Agrarian Trust Ostrom application [9]; Farmers Land Trust farmland commons [10]; ScienceDirect Ostrom Mixteca Alta [11]; P2P Foundation Commons [12].

---

## Section 3: Delegate Selection and Inter-Household Communication

### The Representation Problem

The person who is best at internal household coordination is not necessarily the person who represents the household well externally. The person who is most persuasive in a council setting may not be accountable to their household's actual positions. Delegate selection is not obvious and should not be treated as obvious.

### Delegate Selection Criteria

A household delegate should meet the following criteria:
- Accountability: the delegate reports back to the household after every council meeting. This is not optional. Representation without accountability is representation in name only.
- Clear mandate: the delegate knows their household's positions on standing agenda items before entering the council. For major decisions, the household has pre-deliberated and the delegate carries a specific position, not open discretion.
- Communication capacity: the delegate can accurately represent positions they may personally disagree with. This is the hardest criterion. Many households designate their most persuasive advocate rather than their most accurate reporter.
- Defined term: delegate rotation prevents permanent entrenchment. Quarterly rotation at minimum; semi-annual is common in functioning communities. The transition should include a structured handoff.

### Information Flow Protocol

The runner protocol (from the Household Coordination guide) and the AREDN mesh (from Phase 3 information infrastructure document) handle the physical communication layer. This section provides the governance protocol layer:

**Post-council reporting**: Within 24 hours of any delegate council meeting, the delegate convenes a household briefing — formal (household meeting) or informal (immediate report on return). All households receive the same information simultaneously; no information advantage.

**Pre-decision deliberation**: For decisions requiring full household input, the delegate council distributes the question to all households with a defined deliberation window (48–72 hours for most decisions; 7 days for constitutional decisions). Households deliberate internally; delegates carry the resulting positions.

**Asynchronous decision-making for winter months**: When Zone 5 winter makes travel or regular in-person council meetings impractical, the delegate council must have an established protocol for asynchronous decision-making: what decisions can be made by written communication (signal fire protocol from Phase 3 information infrastructure — or radio, or AREDN if available)? What decisions require waiting for in-person council? What decisions are pre-delegated to individual households for emergency response?

### The Inter-Household Meeting Structure

A functioning delegate council meeting:
- **Cadence**: Monthly for standing operations; as-needed for emergencies
- **Agenda development**: Circulated 72 hours in advance; each household may add items
- **Quorum**: All delegates present or represented by proxy (proxy authority must be delegated in writing by the absent delegate)
- **Decision threshold**: By type — operational decisions (simple majority); resource allocation decisions (supermajority, two-thirds); constitutional decisions affecting membership or governance structure (consensus or near-consensus, pre-defined)
- **Documentation**: Written minutes circulated to all households within 24 hours; maintained in each household's information binder

---

## Section 4: Scaling Phase 5 Tier 2 Documents to Community

### From Household Capability to Community Asset

[NOTE FOR FULL DRAFT: This section is structurally dependent on the three Phase 5 Tier 2 documents being in first-draft form. The community-scale extensions described here must accurately reflect and extend what those documents actually say, not what this planning document anticipated they would say. Write this section last, using the actual drafts of the three Tier 2 documents as source material.]

The following framework descriptions represent the current planning-level understanding. They will be refined and extended in the full draft.

**Veterinary Care → Community Veterinary Cooperative**

A community of 5–8 households can share veterinary resources that no single household can justify or afford:

- *Shared equipment cache*: Large-animal obstetric equipment (calving chains, calf pullers), dehorning equipment (banders and caustic paste, not just physical dehorners), incubators for poultry hatching, portable livestock scale. Cost-sharing makes premium equipment accessible.
- *Community vaccination cold chain*: Some livestock vaccines require refrigeration and are available in quantities larger than a single household needs. A shared cold chain (dedicated cooler with monitoring, shared among 5–8 households) allows bulk purchasing and shared storage.
- *Rotating training schedule*: The Pet Emergency Academy Livestock First Aid certification can be hosted as a community event — the cost of bringing a trainer decreases per-person as group size increases. Practical skills (obstetric assistance, stomach tubing, injectable medication administration) are better learned with supervision and multiple practice runs than alone from a manual.
- *Veterinary school extension relationship*: A community of 50–100 people representing a significant livestock count has more leverage with veterinary school extension programs (Purdue Large Animal, Iowa State Food Animal, University of Illinois) than a single household. A community can justify a scheduled annual farm visit from a vet school extension team.

**Psychological Support → Community Grief Infrastructure**

The household-scale grief and acknowledgment rituals described in the Psych Support guide become more powerful and more sustainable at community scale:

- *Inter-household PFA network*: Each household's trained PFA practitioners become nodes in a community-level support network. When a household-level crisis exceeds the capacity of a single household's practitioners (severe PTSD, suicide crisis, multiple simultaneous losses), the community network provides backup.
- *Community-scale seasonal events*: The four seasonal anchor events in the Psych Support guide become community events — planting day shared work gathering, harvest celebration, winter solstice community meal. These events are qualitatively different from household events: the social density, the visibility of community continuity, and the shared meaning-making across household boundaries produce psychological effects that household-level events cannot achieve.
- *Community memorial practice*: Deaths and major losses within the community require acknowledgment at community scale, not just within the affected household. The community needs a shared practice for honoring its members.

**Conflict Resolution → Inter-Household Mediation Panel**

Three households each designating one trained mediator creates a six-to-nine-person inter-household mediation panel where no mediator mediates their own household's disputes:

- *Cross-household neutrality*: The most significant advantage of a community-scale mediation panel is structural neutrality. Within a household, the CRF knows all parties personally. The inter-household panel allows a mediator from a different household — with no personal stake in the outcome — to facilitate the most difficult disputes.
- *Inter-household conflict scope*: The disputes most likely to fracture a forming community are inter-household conflicts: boundary disputes, shared resource allocation conflicts, incidents involving members of different households. These are precisely the disputes that the household CRF cannot handle impartially.
- *Panel composition and rotation*: Panel members serve for defined terms (semi-annual recommended). No mediator mediates disputes involving their household or anyone they have a close relationship with.

---

## Section 5: The Phase 3 Connection — Activating Existing Community Domains

### The Activation Matrix

Phase 3's five domain documents describe community-scale functions that require a federation of organized households to operate. This matrix maps the specific Phase 3 activation requirements onto the household-level prerequisites that Phase 5 has built.

[NOTE FOR FULL DRAFT: Read all five Phase 3 domain documents before drafting this section. The claims below are from the planning document synthesis and require verification against the actual Phase 3 content.]

| Phase 3 Function | Phase 3 Document | Phase 5 Household Prerequisite | Current Gap |
|---|---|---|---|
| Delegate council (community governance) | Phase 3: Governance | Each household has: internal governance structure; designated delegate; documented charter | Phase 5 Tier 2 Household Coordination guide provides the household-side infrastructure |
| Community food hub + shared storage | Phase 3: Food Systems | Each household has: 6-month supply rotation; procurement relationship documentation; surplus identification process | Household Coordination guide Section 3 covers procurement; surplus sharing protocol is a federation deliverable |
| Kiwix server + skills census | Phase 3: Information Infrastructure | Each household has: individual skill inventory; household information binder; offline reference library | Tier 1 Education guide covers skill documentation; Household Coordination guide covers binder maintenance |
| Mutual defense network | Phase 3: Security | Each household has: established watch protocol; inter-household contact network; communication plan | Household Coordination guide Section 5 covers watch and communication; inter-household linking is a federation deliverable |
| Dunbar transition planning | Phase 3: Scaling Pathways | Each household has: governance charter with constitutional amendment procedure; documented membership criteria | Household Coordination guide covers governance charter; Tier 3 document adds inter-household integration procedure |
| Community veterinary cooperative | Phase 5 Tier 3 (this document) | Each household has: individual veterinary protocols; supply cache; designated veterinary coordinator | Veterinary Care guide provides household foundation; community cooperative is built on it |
| Community grief infrastructure | Phase 5 Tier 3 (this document) | Each household has: trained PFA practitioners; ritual calendar; quiet space designated | Psych Support guide provides household foundation; community layer extends it |
| Inter-household mediation panel | Phase 5 Tier 3 (this document) | Each household has: designated CRF; NVC training; restorative circle familiarity | Conflict Resolution guide provides household foundation; inter-household panel is built on it |

### What Phase 3 Activation Actually Requires

The Phase 3 documents are community-scale operational guides. They describe *what* the community needs to do, not *how households form into a community capable of doing it*. The Phase 5 Tier 2 documents provide the formation layer. Without that layer:

- A delegate council cannot function if the households sending delegates have no internal governance discipline — delegates with no mandate accountability and no household deliberation process produce a council of individuals, not representatives
- A community food hub cannot function if households have not documented their own supply chains and surplus capacity — the hub has nothing to draw on
- A community information infrastructure cannot serve as a community asset if households have not built their own information binder practice — Kiwix content and skills census data must originate from household-level documentation

Phase 5 Tier 2 does not replace Phase 3. It is the prerequisite layer.

**Source anchors**: All five Phase 3 domain documents (internal); PMC 9683026 [13]; Commons Transition Primer mutual aid networks [14].

---

## Section 6: Implementation — The 18-Month Federation Timeline

### Realistic Assumptions

This timeline assumes:
- A cluster of 3–5 households that each have functioning internal governance (Phase 5 Tier 2 complete)
- Geographically proximate (within 5 miles, travel feasible in all but extreme winter conditions)
- Shared interest in federation (not assuming full consensus from Day 1 — the timeline includes a decision gate)
- Zone 5 Midwest seasonal calendar (winter constraints on meeting frequency, planting/harvest season constraints on available time)

### The 18-Month Timeline

**Month 1: Relationship and Assessment**
- Informal meeting of household representatives (not formal delegates yet): introduce governance structures, share information binder formats, assess alignment
- Identify shared resources that already exist (e.g., shared fencing, shared access road, shared equipment)
- Decision gate: is the cluster ready to pursue formal federation, or is informal coordination sufficient for now?

**Month 2: Formal Delegate Selection and First Council**
- Each participating household selects a delegate using the criteria from Section 3
- First formal delegate council meeting: establish meeting cadence, agenda-building process, decision thresholds
- Establish documentation protocol: shared meeting minutes accessible to all households

**Months 3–4: Shared Resource Identification and Ostrom Framework Adoption**
- Identify all currently or potentially shared resources
- For each shared resource: define membership (who has access), monitoring protocol, allocation rules, and sanctions
- Document these in a shared commons charter
- Decision gate: which resources are ready for shared governance? Which require more groundwork?

**Month 4–5: Community Skills Census**
- Using each household's existing skill inventory (from Tier 1 Education guide), compile a community-wide skills census
- Identify skill redundancies (covered by multiple households) and skill gaps (covered by no household)
- Identify training priorities: which gaps are load-bearing for community function?
- Load into community information system (Kiwix server if online; shared binder if offline)

**Month 6: First Community Tabletop Exercise**
- Conduct a tabletop exercise involving all households: a 6-hour simulated extended disruption scenario
- Test: delegate council decision-making under simulated time pressure; shared resource activation; inter-household communication; medical and psychological support coordination
- Document lessons and structural gaps revealed

**Months 6–8: AREDN Mesh or Communication Infrastructure**
- If resources allow: AREDN mesh linking all households (see Phase 3 information infrastructure document for deployment guidance)
- If not: establish radio net, runner protocol, signal protocols
- Goal: reliable communication between all households independent of cellular/internet infrastructure

**Months 8–12: Community Resource Assets Activation**
- Community veterinary cooperative: shared equipment cache, joint purchase of bulk vaccines, community training event
- Community seed library: establish check-out system, germination rate tracking, seed saving rotation
- Community equipment pool: shared tractor, tools, specialized equipment under Ostrom governance
- Inter-household mediation panel: designate panel members, establish referral protocol

**Month 12: Governance Review and Charter Amendment**
- Full community review of the delegate council's first year: what worked? What governance structures need adjustment?
- Amend the inter-household governance charter to reflect what was learned
- Conduct community psychological support review: are grief infrastructure and seasonal events functioning?

**Months 12–18: Dunbar Transition Planning**
- If community is approaching 100+ people: activate Phase 3 scaling pathways document's Dunbar transition planning process
- Draft the community's constitutional plan for managing the Dunbar threshold
- Decision: is the community approaching integration with additional households? What is the integration protocol?

**Month 18: Full System Test**
- Conduct a 48-hour full-community exercise (weekend tabletop or actual drill)
- All Phase 3 domain systems tested simultaneously: governance, food, information, security, health
- All Phase 5 household systems activated: veterinary, psychological, conflict resolution
- Document gaps and create a Year 2 priority list

### Implementation Checklist by Milestone

[Full draft note: expand each milestone into a 5–8 item checklist with clear completion criteria and responsible household roles.]

**Source anchors**: PMC 9683026 [13]; Eco-Savvy commune blueprint [15]; Ostrom 1990 [1]; Phase 3 internal documents [all five].

---

## Interdependencies

**Prerequisites (all must be complete before this document enters full production)**:
- `phase-5/tier-2-household-coordination-infrastructure-guide.md` — the household governance foundation
- `phase-5/tier-2-veterinary-care-guide.md` — Section 4.1 of this document requires the community veterinary cooperative to accurately extend what that document says
- `phase-5/tier-2-psychological-support-guide.md` — Section 4.2 extends what that document says about community grief infrastructure
- `phase-5/tier-2-conflict-resolution-deep-dive.md` — Section 4.3 extends what that document says about the inter-household mediation panel
- All five Phase 3 domain documents — Section 5 maps household prerequisites against Phase 3 activation requirements; this requires reading the actual Phase 3 content

**This document closes Phase 5**:
- It is the terminus of the Phase 5 corpus
- It connects the individual/household layer (Phase 5 Tier 1 and Tier 2) to the community layer (Phase 3)
- After this document, the systems-resilience corpus from individual skill through community federation is complete

---

## Production Notes for Full Draft

**Critical prerequisites for Step 1 (before any prose writing)**:
1. Re-read all five Phase 3 domain documents. The activation matrix in Section 5 must accurately reflect the Phase 3 requirements.
2. Read the first drafts of all three Tier 2 documents. Section 4 community extensions must accurately reflect their content.
3. Verify AREDN mesh 6–8 month deployment claim against Phase 3 information infrastructure document.

**Sections requiring most work at full draft**:
1. Section 5 (Phase 3 activation matrix) — the structural core; write this first
2. Section 2 (Ostrom commons application) — well-sourced but requires careful Zone 5 customization
3. Section 6 (18-month timeline) — requires seasonal realism and integration with AREDN and Phase 3 timelines

**Target citation count at full draft**: 35–45. Currently 15 external sources staged + 8 internal Phase 3/Phase 5 documents. Will require approximately 15–20 additional targeted sources, primarily from: sociocracy in community settings, Zone 5 commons management examples, AREDN deployment case studies.

**Scope decision needed from user**: Full 7,500–9,000 word development (all sections above at full depth) vs. abbreviated 4,000-word cross-reference synthesis that maps Phase 5 to Phase 3 without fully developing the federation mechanics. The full scope is the default; abbreviated scope is an option if session constraints require it.

---

## Staged Citations

[1] Ostrom, E., "Governing the Commons: The Evolution of Institutions for Collective Action," Cambridge University Press, 1990. (Standard academic citation)
[2] Allen, C., "A Revised Ostrom's Design Principles for Collective Governance of the Commons," Life with Alacrity, 2015. https://www.lifewithalacrity.com/article/a-revised-ostroms-design-principles-for-collective-governance-of-the-commons/
[3] [Dunbar's number primary source — Robin Dunbar, "Neocortex size as a constraint on group size in primates," Journal of Human Evolution, 1992; or Dunbar, "How Many Friends Does One Person Need?" 2010]
[4] McCarty, K., "Twin Oaks: A Case Study of an Intentional Egalitarian Community," SIT Digital Collections, 2020. https://digitalcollections.sit.edu/capstones/2494/
[5] PMC 9118649, "Collaborative Governance at the Start of an Integrated Community Approach," BMC Public Health, 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9118649/
[6] Peace in Kurdistan Campaign, "Autonomy Institutions in Chiapas and Rojava: What Lessons?" accessed 2026. https://www.peaceinkurdistancampaign.com/autonomy-institutions-in-chiapas-and-rojava-what-lessons/
[7] Sociocracy For All, "Sociocracy in Intentional Communities Conference 2024," 2024. https://www.sociocracyforall.org/intentional-communities-conference-2024/
[8] Cohousing Association of the US, "Sociocracy," accessed 2026. https://www.cohousing.org/sociocracy/
[9] Agrarian Trust, "Ostrom's Eight Design Principles for a Successfully Managed Commons," accessed 2026. https://www.agrariantrust.org/ostroms-eight-design-principles-for-a-successfully-managed-commons/
[10] Farmers Land Trust, "How the Farmland Commons Integrates All Eight of Elinor Ostrom's Principles," 2024. https://www.thefarmerslandtrust.org/how-the-farmland-commons-integrates-all-eight-of-elinor-ostroms-principles-for-a-successful-commons/
[11] ScienceDirect, "Governing the Commons in Mexico's Mixteca Alta: Linking Ostrom's Design Principles and Comunalidad," 2022. https://www.sciencedirect.com/science/article/abs/pii/S1389934122001757
[12] P2P Foundation Wiki, "Elinor Ostrom's Eight Commons Governance Design Principles," accessed 2026. https://wiki.p2pfoundation.net/Elinor_Ostrom%E2%80%99s_Eight_Commons_Governance_Design_Principles
[13] PMC 9683026, "An Analysis of an Inventory of Community Resilience Frameworks," 2022. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9683026/
[14] Commons Transition Primer, "Case Study: Mutual Aid Networks," accessed 2026. https://primer.commonstransition.org/4-more/5-elements/case-studies/case-study-mutual-aid-networks/
[15] Eco-Savvy, "How to Start a Commune: A Practical 2024 Blueprint," 2024. https://www.eco-savvy.blog/how-to-start-commune

---

*Phase 5 Wave 2 — Preliminary Draft*
*Prepared: 2026-05-20 | Status: 35% complete (structure + section summaries + citations staged)*
*Full production target: Wave 2c (LAST — after all Tier 2 documents complete)*
*Document path: `projects/systems-resilience/phase-5-wave-2-community-implementation-playbook.md`*
*Full production path: `projects/systems-resilience/phase-5/tier-3-community-coordination-framework.md`*
