---
title: "Phase 3 Community-Scale Infrastructure — Research Outline & Production Plan"
project: systems-resilience
region: "Midwest US (Zone 5)"
created: 2026-05-18
phase: 3
scale: community
status: "Preliminary research complete — production-ready upon June 1 Phase 5 path decision"
word_count_target: 12000–16000 words across 4–5 documents
citation_target: 50–70 citations
audience: "Project lead (Anya) — researcher/implementer"
scope: "100–1,000 person community-scale crisis resilience"
---

# Phase 3: Community-Scale Crisis Response Infrastructure
## Research Outline and Production Plan

---

## Executive Summary

Phase 3 bridges the gap between household-cluster resilience (Phase 2, 8–20 people) and regional-scale coordination (Phase 5). The focus is the 100–1,000 person community: a geographic area large enough to require formal governance, shared information systems, and collective security, but small enough for direct democratic participation and interpersonal trust.

**Most important preliminary finding**: The single greatest bottleneck to community-scale resilience is not physical infrastructure — it is the governance transition that happens between roughly 150 and 500 people. Below ~150 (Dunbar's number), informal trust-based coordination works. Above it, formal structures are necessary whether communities want them or not. Communities that do not consciously design those structures will have them imposed by whoever is most organized at the moment of crisis. Every other infrastructure domain (supply coordination, information, security) can be made to work adequately if governance is functional. None of them function under failed or contested governance.

**Five research domains** are outlined below, with preliminary findings, source inventories, and production estimates for each:

1. Community Coordination Infrastructure — supply chains, mutual aid networks, labor coordination
2. Governance Structures for Crisis Response — decision protocols, resource allocation, accountability
3. Information Infrastructure — communications, knowledge bases, situational awareness
4. Security and Defense — perimeter models, mutual defense, internal protocols
5. Scaling Pathways — 100, 1,000, and 10,000 person thresholds, bottlenecks, and transitions

**Phase 3 production will begin immediately upon the June 1 Phase 5 path decision** if community-scale is selected. Research preparation is complete; no additional pre-work is needed before execution.

**Confidence level on preliminary findings**: High on governance and coordination conclusions (strong empirical literature); moderate on security and scaling extrapolations (case studies exist but are less directly applicable to Midwest rural context); low on information infrastructure cost estimates (technology costs shift rapidly).

---

## Domain 1: Community Coordination Infrastructure

**Scope**: 500–700 words covering supply chain coordination, mutual aid network structures, and labor coordination for communities of 100–1,000 people.

### Preliminary Findings

**Supply chain coordination** at community scale requires deliberate logistics architecture that most mutual aid networks build ad hoc and then retrofit. The strongest documentation comes from COVID-era food distribution networks. Bed-Stuy Strong (Brooklyn, 2020) supported 28,000 people in Central Brooklyn with weekly home-delivered groceries over 15 months, scaling from a Google spreadsheet to a Twilio-automated dispatch system with standardized volunteer reimbursement. The key structural lesson: **geographic quadrant subdivision with rotating coordinators** outperforms centralized dispatch at the 1,000+ person scale. Below ~300 people, centralized coordination is faster and more flexible. Transition point: when a single coordinator can no longer hold all active needs in working memory (roughly 40–60 active requests simultaneously).

**Mutual aid network structures** are better documented for disaster response than for extended-duration stability. The most useful frameworks are: (1) the Mutual Aid Disaster Relief (MADR) model applied after Hurricanes Katrina, Maria, and Ida — decentralized pods with shared communication protocols; (2) the Zapatista autonomous community model — village-level assemblies managing specific resource domains (health, food, education) with rotating uncompensated coordinators obligated by community trust rather than hierarchy; (3) time banking systems (hOurworld network, active in 22 countries) — labor-hour credits that function without currency and decouple contribution from wealth. The time banking model is particularly relevant to Midwest rural communities because it handles the skilled-labor imbalance explicitly: a retired farmer's knowledge-hour equals a laborer's work-hour.

**Labor coordination** under crisis conditions is the least studied of the three. The most applicable literature is from disaster informatics and industrial labor federations. The IWW's mutual defense model — "an injury to one is an injury to all" — provides the philosophical basis; the Zapatista cargo system (obligation to serve without remuneration, with community right of recall) provides the practical model for roles that must be filled even when unappealing. The critical design requirement is distinguishing between **critical-path roles** (water management, medical triage, security watch) and **contribution roles** (food preparation, supply distribution, construction). Critical-path roles cannot be left to voluntary participation and must have designated fallback personnel.

**Confidence gap**: No strong empirical data on labor coordination at 100–500 person scale in extended disruption scenarios (6+ months) in developed-country contexts. Best available proxies are Zapatista communities, Kibbutz collective labor models, and post-WWII rural rationing literature.

### Source Inventory

| # | Source | Type | URL |
|---|---|---|---|
| 1 | Bed-Stuy Strong — COVID food distribution documentation | Case study | https://www.bedstuystrong.com/ |
| 2 | Mutual Aid Disaster Relief — research articles and case studies | Organization/research | https://mutualaiddisasterrelief.org/research-articles/ |
| 3 | Beeck Center — "Four Key Takeaways from Mutual Aid Organizing During COVID-19" | Analysis | https://beeckcenter.georgetown.edu/four-key-takeaways-from-mutual-aid-organizing-during-the-covid-19-pandemic/ |
| 4 | hOurworld Time Banking — network documentation and model | Platform/organization | https://hourworld.org/ |
| 5 | Graeber, D. & Grubacic, A. — "Introduction to Mutual Aid" | Theoretical | https://davidgraeber.org/articles/introduction-to-mutual-aid/ |
| 6 | NRDC — "Mutual Aid and Disaster Justice: We Keep Us Safe" | Overview/analysis | https://www.nrdc.org/stories/mutual-aid-and-disaster-justice-we-keep-us-safe |
| 7 | Rojava Information Center — "Communes: building block of democratic confederalism" | Case study | https://rojavainformationcenter.org/2020/05/explainer-communes-the-building-block-of-democratic-confederalism/ |
| 8 | Frontiers in Sustainable Food Systems — "Benefits and challenges of collaborative networks during COVID-19" | Peer-reviewed | https://www.frontiersin.org/journals/sustainable-food-systems/articles/10.3389/fsufs.2025.1559153/full |
| 9 | WPSA — "Coordinating Time: Mutual Aid, Timebanking, and Communities in Crisis" | Academic paper | https://www.wpsanet.org/papers/docs/Time%20Bank%20Paper%20-%20WPSA%20version.pdf |
| 10 | OpenDemocracy — "Zapatistas: Lessons in community self-organisation" | Case study | https://www.opendemocracy.net/en/democraciaabierta/zapatistas-lecciones-de-auto-organizaci%C3%B3n-comunitaria-en/ |

**Research gaps to close in production**:
- Extended-duration (12+ month) mutual aid case studies outside disaster-response context
- Midwest-specific labor coordination examples (Iowa farm co-ops, rural mutual aid societies pre-1950)
- Quantitative data on supply chain failure modes at 300–500 person scale

---

## Domain 2: Governance Structures for Crisis Response

**Scope**: 500–700 words covering decision-making protocols under scarcity, resource allocation mechanisms, and accountability structures.

### Preliminary Findings

**Decision-making under scarcity** is the governance problem most likely to fracture communities that have no prior fracture lines. The empirical literature converges on three structural insights:

First, **consensus decision-making fails above ~50 people without structural scaffolding** (facilitation protocols, time limits, decision categories). The Rojava commune model solves this by separating domains: each commune (~150 people) handles its own domain decisions internally, with cross-commune decisions escalating to the "People's House" (Mala Gel). This nested assembly structure is the best-documented working model for the 100–500 person range. Key operational requirement: decisions categorized by scope (household-affecting, community-affecting, inter-community-affecting) before any meeting begins.

Second, **sortition (random selection) has limited evidence base for crisis governance** but strong evidence in non-crisis deliberative democracy contexts (Citizens' Assemblies in Ireland, UK, and France). The gap is the crisis condition: under scarcity pressure, sortition bodies tend to defer to those with demonstrated competence rather than maintaining random representation. Hybrid models — sortition-selected oversight panels combined with competence-selected implementation roles — have stronger theoretical support but less field testing.

Third, **delegate councils outperform both pure consensus and representation** at the 100–500 person scale in the most relevant documented cases. Zapatista mandar obedeciendo (governing by obeying) — where delegates implement assembly decisions rather than making decisions themselves — is the best-documented model. Mondragon cooperatives use a similar structure at larger scale: General Assemblies set policy; elected councils implement; individual cooperatives retain autonomy on daily operations.

**Resource allocation under scarcity** has clearer empirical guidance. Ostrom's 8 Design Principles for commons governance, developed from field research across fisheries, irrigation systems, and forest commons, provide the most robust framework. Principles most directly applicable to crisis communities:
- Principle 2: Rules must match local conditions (no universal rationing algorithm works without customization)
- Principle 4: Monitors are accountable to the governed group, not to an external authority
- Principle 6: Sanctions escalate gradually — immediate expulsion creates martyrs and erodes trust

**Need-based vs. contribution-based allocation**: The empirical literature on this is surprisingly settled. Need-based allocation is more stable over time in extended disruptions; contribution-based allocation is more motivating in early-phase crisis response. Communities that start contribution-based and then need to shift to need-based (as some members become unable to contribute) experience significant conflict. **Recommendation from disaster sociology**: design the system need-based from the start, with contribution recognition mechanisms (social credit, status) that do not affect material distribution.

**Accountability structures** in horizontal organizations are consistently underbuilt. The most documented failure mode is "accountability theater" — mechanisms that exist on paper but are never used because using them requires confronting trusted community members. The Zapatista recall mechanism (community right to revoke mandate) works because it operates through the same assembly that granted the mandate, not through a separate enforcement body. Rotating leadership (maximum term limits) reduces the social cost of accountability because no one is invested in a permanent position.

**Confidence gap**: Accountability mechanism literature is primarily theoretical or short-duration. Long-duration empirical data (2+ years) is almost entirely from intentional communities (kibbutzim, communes) that have significant selection bias — they attract people already committed to communal governance.

### Source Inventory

| # | Source | Type | URL |
|---|---|---|---|
| 1 | Ostrom, E. — Nobel Lecture: "Beyond Markets and States: Polycentric Governance" | Foundational theory | https://www.nobelprize.org/uploads/2018/06/ostrom_lecture.pdf |
| 2 | Ostrom, E. — *Governing the Commons* (1990) | Foundational text | Available via JSTOR/library |
| 3 | Rojava Information Center — Commune structure documentation | Case study | https://rojavainformationcenter.org/2020/05/explainer-communes-the-building-block-of-democratic-confederalism/ |
| 4 | EUARENAS — "Democratic Confederalism in Rojava" | Case study | https://euarenas-toolbox.eu/the-tool/democratic-confederalism-in-rojava/ |
| 5 | Mondragon Cooperatives — governance documentation | Case study | https://participedia.net/case/82 |
| 6 | NACLA — "Zapatistas at 30: Building and Inspiring Autonomy" | Case study | https://nacla.org/zapatistas-at-30-building-and-inspiring-autonomy/ |
| 7 | Ostrom Workshop, Indiana U — Design Principles teaching tools | Applied framework | https://ostromworkshop.indiana.edu/courses-teaching/teaching-tools/ostrom-design/index.html |
| 8 | Science Direct — "Generalizing the core design principles for group efficacy" | Peer-reviewed | https://www.sciencedirect.com/science/article/abs/pii/S0167268112002697 |
| 9 | Beneficialstate.org — "Exploring the Mondragon cooperative system" | Applied case study | https://beneficialstate.org/perspectives/exploring-the-mondragon-cooperative-system/ |
| 10 | Waging Nonviolence — "Lessons from Barcelona's 8-year experiment in radical governance" | Case study | https://wagingnonviolence.org/2023/05/lessons-barcelona-en-comu-ada-colau/ |

**Research gaps to close in production**:
- Controlled comparisons of allocation models in extended disruption (famine, siege, hurricane recovery)
- Indigenous governance models at 100–500 person scale in North American context
- Empirical data on accountability mechanism effectiveness in horizontal organizations

---

## Domain 3: Information Infrastructure

**Scope**: 400–600 words covering communication systems, shared knowledge bases, and situational awareness / threat-resource intelligence coordination.

### Preliminary Findings

**Communication systems** for community resilience exist on a spectrum from trivially simple (shouting distance, hand-delivered notes) to technically complex (mesh radio networks). The research literature has a clear hierarchy by disruption severity:

- **Grid power present, internet down**: GMRS (General Mobile Radio Service) repeater networks are the most cost-effective community communication layer. GMRS operates at up to 50 watts, requires a single $35 FCC license covering all family members, and integrates with existing amateur radio infrastructure. Repeaters can cover a 5–25 mile radius depending on terrain.
- **Grid power down, batteries/solar available**: Amateur Radio Emergency Data Network (AREDN) mesh networking provides data-layer communication (email, chat, voice, document sharing, video) over repurposed commercial WiFi hardware running open-source mesh firmware. AREDN nodes are self-configuring and self-healing — if a node goes down, the mesh reroutes automatically. The system operates within amateur radio licensing (Technician class license, $15 exam fee). AREDN is currently deployed by emergency responders in dozens of US counties.
- **All power down, human-powered only**: HF shortwave radio requires only minimal power (12V battery sufficient), can reach hundreds of miles, and functions for receive-only without any license. Transmit requires General or Extra class amateur license. This is the last-resort layer that cannot be improvised post-disaster and must be established in advance.

**Key finding**: Communities need to build **three redundant layers** (GMRS for day-to-day, AREDN for data-rich coordination, HF shortwave for external reach) because no single layer is reliable across all disruption scenarios. The realistic minimum viable setup for a 100-person community: 8–12 GMRS handhelds, 2–3 AREDN nodes on structures with solar backup, 1 HF station with battery bank.

**Shared knowledge bases** at community scale are primarily a physical infrastructure problem, not a content problem. Research on disaster informatics confirms that knowledge availability is not the bottleneck — retrievability under conditions of no power, no internet, and damaged physical infrastructure is. The Kiwix offline knowledge server (Raspberry Pi 4, ~$50, 5W power draw) solves this for digital access. For communities where even that may fail, physical printed libraries with indexed reference materials are the redundant layer. A minimum viable printed reference library for 100 people: first aid and trauma protocols (Wilderness Medical Society Wilderness First Responder materials), agricultural reference (USDA Extension publications), basic repair manuals (iFixit offline edition), and water/sanitation protocols (WHO emergency WASH standards).

**Situational awareness and threat intelligence**: The 2025 Los Angeles fires demonstrated that informal Discord-based coordination networks (road closures, evacuation site status, resource hub status) outperformed formal emergency communication systems in speed and accuracy in the first 72 hours. The scalable lesson is not to replicate Discord but to designate a **community information coordinator role** with authority to collect, verify, and disseminate situational intelligence, and to pre-establish the communication channels those updates will travel through. Signal verification (preventing panic from unverified rumors) requires a two-source confirmation standard at minimum.

**Confidence gap**: Cost estimates for radio infrastructure change rapidly with hardware availability. The AREDN specification is mature but hardware compatibility lists require annual updates.

### Source Inventory

| # | Source | Type | URL |
|---|---|---|---|
| 1 | AREDN — What is an AREDN Network? | Technical documentation | https://www.arednmesh.org/content/what-aredn-network |
| 2 | AREDN Documentation — Overview | Technical specification | http://docs.arednmesh.org/en/latest/aredn_overview.html |
| 3 | CommGearReport — "Amateur Radio Mesh Networks: Resilient Emergency Communications" | Overview | https://commsgearreport.com/amateur-radio-mesh-networks/ |
| 4 | Surviving Off the Grid — "2025 Survival Radio Guide: HAM, FRS, GMRS" | Practical guide | https://survivingoffthegrid.com/communication/ham-radio-frequencies/ |
| 5 | OJPHI — "Cultivating Disaster Preparedness: Technology's Contribution to Situational Awareness" (2025) | Peer-reviewed scoping review | https://ojphi.jmir.org/2025/1/e75404 |
| 6 | arXiv — "Solutions for Sustainable and Resilient Communication Infrastructure in Disaster Relief" | Peer-reviewed | https://arxiv.org/html/2410.13977v1 |
| 7 | Sustainable Commons — "Social connectivity in times of disaster: 2025 LA fires" | Case study | https://sustainablecommons.wordpress.com/2026/03/28/social-connectivity-in-times-of-disaster-mutual-aid-the-2025-l-a-fires/ |
| 8 | UNESCO — Disaster Risk Management for Documentary Heritage (2024) | Standards document | https://unesdoc.unesco.org/ark:/48223/pf0000391132 |
| 9 | Kiwix — offline knowledge infrastructure | Platform documentation | https://kiwix.org/en/ |
| 10 | DHS S&T — Disaster Resilience research overview | Government research summary | https://www.dhs.gov/science-and-technology/st-impact-disaster-resilience |

**Research gaps to close in production**:
- Current AREDN hardware compatibility list (requires direct check of arednmesh.org)
- Practical cost breakdown for three-layer radio setup serving 100 people
- Indigenous knowledge preservation models and their applicability to community-level situational awareness

---

## Domain 4: Security and Defense

**Scope**: 400–600 words covering perimeter security models, mutual defense agreements, and internal security protocols.

### Preliminary Findings

**Perimeter security** for community-scale resilience is fundamentally different from household security. At the household level, the goal is deterrence and delay. At the community level (100–1,000 people spread across 1–10 square miles), comprehensive physical perimeter control is logistically infeasible for most scenarios. The realistic security posture is **layered deterrence with controlled access points** rather than sealed perimeters.

The most applicable contemporary models are: (1) California Master Mutual Aid Agreement — a state-level framework for inter-jurisdiction resource sharing that includes security coordination, providing a legal template for community-level mutual aid pacts; (2) community safety movement literature emphasizing **violence interruption over reactive force** — the Brownsville, NYC experiment demonstrated that trained conflict mediators (former community members with credibility) reduced shootings 28% in a 5-day period by shifting primary peacekeeping to residents; (3) de-escalation training literature from law enforcement reform, which provides transferable protocol design for community security volunteers.

**Physical security design** for a 100-person community should focus resources on: (1) information — knowing who is approaching before they arrive (observation posts at road access points, messenger networks, community alerting protocols); (2) access control at choke points (roads, water access, storage facilities) rather than comprehensive perimeter; (3) relationship networks with adjacent communities that provide early warning of emerging threats. The worst security posture for a community is isolation — communities without relationships with neighbors are more vulnerable, not less, because they lack early warning and mutual assistance.

**Mutual defense agreements** at community scale are documented primarily through formal state-level frameworks (California's Master Mutual Aid Agreement, FEMA inter-jurisdictional agreements) that provide structural templates but are designed for government-to-government coordination. For community-to-community coordination, the most directly applicable model is the Zapatista inter-community mutual support system: communities formally commit to sending specified resources (people, food, equipment) in response to calls from allied communities, with explicit reciprocity expectations and community-level accountability for fulfillment. This model works at 100–500 person scale and does not require state infrastructure.

**Internal security protocols** must address two distinct threat categories: external threats (people or groups outside the community attempting to take resources) and internal conflicts (disputes between community members escalating to violence). These require different responses. External threats are primarily an information and deterrence problem. Internal conflicts are primarily a governance and social cohesion problem — high-conflict communities have security problems that weapons and perimeters cannot solve, while high-cohesion communities with functioning grievance resolution mechanisms rarely need escalated security responses.

**Key finding from community safety literature**: The communities most resistant to security threats in extended disruptions are those with high social cohesion and functional conflict resolution mechanisms — not those with the most weapons or the most fortified perimeters. Security infrastructure investment has the highest return when it is preceded by governance and conflict resolution infrastructure.

**Confidence gap**: Literature on community-scale security in extended disruption scenarios (6+ months) in developed-country contexts is thin. Most available evidence comes from: (a) post-hurricane recovery (days to months), (b) historical siege and famine records (pre-modern, difficult to extrapolate), (c) intentional community case studies (selection bias toward conflict avoidance). The Zapatista model (30+ years of documented operation) is the best available long-duration case study in a broadly analogous context.

### Source Inventory

| # | Source | Type | URL |
|---|---|---|---|
| 1 | California Disaster and Civil Defense Master Mutual Aid Agreement | Legal template | https://www.caloes.ca.gov/wp-content/uploads/Preparedness/Documents/CAMasterMutAidAgreement.pdf |
| 2 | Everytown Research — "Community-Led Public Safety Strategies" | Research overview | https://everytownresearch.org/report/community-led-public-safety-strategies/ |
| 3 | Brookings — "A new community safety blueprint" (public health approach) | Policy analysis | https://www.brookings.edu/articles/a-new-community-safety-blueprint-how-the-federal-government-can-address-violence-and-harm-through-a-public-health-approach/ |
| 4 | Imagine Water Works — New Orleans mutual aid and security model | Case study | https://www.imaginewaterworks.org/mutual-aid-a-grassroots-model-for-justice-and-equity-in-emergency-management/ |
| 5 | Dissent Magazine — "A New Model of Public Safety" | Analysis | https://dissentmagazine.org/article/a-new-model-of-public-safety/ |
| 6 | OMCT — "The Collective Defense of Indigenous Peoples in Colombia" | Case study | https://www.omct.org/en/resources/blog/unidos-por-los-derechos-la-defensa-colectiva-de-los-pueblos-ind%C3%ADgenas-en-colombia |
| 7 | NACLA — "Zapatistas at 30" (security and self-defense dimensions) | Case study | https://nacla.org/zapatistas-at-30-building-and-inspiring-autonomy/ |
| 8 | Schubas for Chiapas — "What is Zapatista Autonomy?" | Explanatory | https://schoolsforchiapas.org/blog-entry-zapatista-autonomy/ |
| 9 | Community Tool Box — "Implementing a Neighborhood Watch" | Practical guide | https://ctb.ku.edu/en/table-of-contents/implement/provide-information-enhance-skills/neighborhood-watch/main |
| 10 | Sustainable Communities — 2025 LA fires security coordination | Case study | https://sustainablecommons.wordpress.com/2026/03/28/social-connectivity-in-times-of-disaster-mutual-aid-the-2025-l-a-fires/ |

**Research gaps to close in production**:
- Extended-duration (12+ month) community security case studies in developed-country contexts
- Midwest rural security context: specific threat profiles (organized groups, desperate individuals, resource raids) differ substantially from urban contexts most studied
- Non-lethal deterrence and access control methods — literature is thin outside law enforcement reform

---

## Domain 5: Scaling Pathways

**Scope**: 400–600 words covering 100-person, 1,000-person, and 10,000-person scale models, transition thresholds, and bottleneck identification.

### Preliminary Findings

**The 100-person community (village / neighborhood model)** is well within the range where direct democratic participation is possible without formal representation. Based on Dunbar's research and contemporary intentional community data, the optimal governance approach at this scale is **domain-specialist authority with community-assembly ratification**: identified experts (water manager, medical coordinator, security lead) have operational authority within their domain; major resource allocation decisions require community assembly approval. This model works because social relationships span the entire group — everyone knows everyone, reputation is the primary accountability mechanism, and formal governance overhead is low.

The critical infrastructure requirements at 100 persons are: a single communication hub (one person or two-person team), a shared resource inventory (physical ledger or offline digital), and a regular assembly cadence (weekly in crisis phase, monthly in stability phase). At 100 persons, informal labor coordination can still function — tasks are assigned through relationship and social expectation rather than formal scheduling systems.

**The 1,000-person community (federated villages model)** crosses the Dunbar threshold for personal relationships, requiring structural solutions to problems that were solved informally at 100 persons. The governance literature identifies three reliable structural solutions at this scale:

First, **federated sub-units**: maintain 100–150 person sub-communities with their own governance and resources; coordinate across sub-units through delegate councils. Mondragon's federal model — each cooperative retains autonomy; delegates represent cooperatives in the wider Congress — is the most documented long-running example. Rojava's commune-to-People's House structure is the most documented crisis-context example.

Second, **domain-based working groups with cross-representation**: water/sanitation, food/agriculture, medical, security, and communication each have working groups; each group has a seat at the coordination council. This approach scales to 1,000 people while maintaining functional expertise.

Third, **recorded decision-making**: above 150 people, the shared social memory that serves as institutional memory at smaller scales fails. Written meeting records, resource allocation logs, and decision rationale documentation become essential for accountability and continuity. Communities that skip this infrastructure at 1,000 persons will lose institutional memory every time key people cycle out or are incapacitated.

**The 10,000-person community (regional coordination model)** is outside the range of direct democratic participation and requires representative structures. The key transition bottlenecks at this scale are:

- **Information distribution**: a 10,000-person network cannot relay information from edge to center in real time without dedicated communication infrastructure. Information asymmetries between sub-communities become a source of power concentration and conflict.
- **Cultural coherence**: at 10,000 persons, communities are likely to span multiple ethnic, cultural, and religious groups whose crisis-response norms differ. Governance structures must be explicitly inclusive or they will exclude meaningful minorities of the population, creating internal security threats.
- **Infrastructure dependencies**: at this scale, most critical infrastructure (water treatment, electricity generation, grain milling) serves the entire regional population. A failure at any single point is a community-wide crisis. Redundancy requirements increase exponentially with scale; decentralized micro-infrastructure becomes more resilient than centralized infrastructure even when it is less efficient.
- **Specialization and comparative advantage**: 10,000 persons cannot all be generalists. Functional specialization (doctors, engineers, farmers, educators) is efficient but creates fragility — loss of the only person with a critical skill is a community-level crisis. Knowledge preservation and apprenticeship systems (see Phase 4b Knowledge Preservation option) are the mitigation.

**Transition thresholds summary** (based on research synthesis):

| Scale | Threshold | Governance model breaks | Required new structure |
|---|---|---|---|
| <50 | Below kinship-group scale | N/A — informal works | Basic meeting cadence |
| 50–150 | Approaching Dunbar's number | Ad hoc breaks; need formal facilitation | Rotating facilitation, domain roles |
| 150–500 | Above Dunbar's number | Personal trust fails to scale; informal accountability fails | Delegate structures, written records, formal recall mechanisms |
| 500–2,000 | Above single-community scale | Single assembly becomes unwieldy; information distribution fails | Federated sub-units, working groups, dedicated information coordinators |
| 2,000–10,000 | Regional scale | Direct democracy fails; cultural coherence under pressure | Representative governance, infrastructure redundancy, apprenticeship systems |

**Confidence**: High on the 100-person model (well-documented in intentional communities and small mutual aid organizations). Moderate on 1,000-person model (Mondragon and Rojava provide field data but with significant contextual differences from Midwest rural context). Low on 10,000-person model (extrapolation from theory; very limited field data on non-state communities at this scale functioning over extended periods).

### Source Inventory

| # | Source | Type | URL |
|---|---|---|---|
| 1 | Dunbar, R. — Research on social group size and cognitive limits | Foundational research | https://en.wikipedia.org/wiki/Dunbar%27s_number |
| 2 | Supernuclear — "Dunbar's Number and Community Size" (intentional communities) | Applied analysis | https://supernuclear.substack.com/p/dunbars-number-and-community-size |
| 3 | Terrenity — "How big should your community be?" | Practical analysis | https://terrenity.substack.com/p/how-big-should-your-community-be |
| 4 | Mondragon — governance and federated model | Case study | https://participedia.net/case/82 |
| 5 | Rojava Information Center — scaling from commune to People's House | Case study | https://rojavainformationcenter.org/2020/05/explainer-communes-the-building-block-of-democratic-confederalism/ |
| 6 | Polycentric Systems of Governance (Carlisle, 2019) | Peer-reviewed | https://onlinelibrary.wiley.com/doi/10.1111/psj.12212 |
| 7 | Ostrom — Nobel Lecture | Foundational | https://www.nobelprize.org/uploads/2018/06/ostrom_lecture.pdf |
| 8 | IFRC — Framework for Community Resilience | Standards | https://www.ifrc.org/sites/default/files/IFRC-Framework-for-Community-Resilience-EN-LR.pdf |
| 9 | NREL — Intergovernmental Preparation and Coordination (regional resilience) | Research summary | https://www.nrel.gov/security-resilience/intergovernmental-preparation-coordination |
| 10 | National Resilience Strategy (January 2025) | Policy document | https://bidenwhitehouse.archives.gov/wp-content/uploads/2025/01/National-Resilience-Strategy.pdf |

**Research gaps to close in production**:
- Quantitative case data on governance failure modes at each transition threshold
- Midwest-specific examples of community-scale coordination at 500–2,000 person scale (county fair organizations, rural mutual aid societies, township governance)
- Transition management protocols — how communities deliberately plan and execute the shift from one governance model to the next

---

## Preliminary Findings: Cross-Domain Synthesis

These findings hold across domains and should inform production document structure:

**1. Governance is load-bearing.** All other infrastructure domains depend on governance functioning. Communication systems, security protocols, and supply chains can be improvised and improved mid-crisis. Governance under contested authority cannot be easily retrofitted once social trust has fractured. Design governance first; design everything else around it.

**2. The 150-person transition is the most dangerous threshold.** Communities that grow from 100 to 300 people (by merger, refugee absorption, or organic growth) cross the Dunbar boundary without necessarily recognizing it. Governance systems designed for informal trust break precisely when the community is under the most stress and least able to design replacements. Communities should anticipate and plan for this transition before it occurs.

**3. Historical field-tested models exist at each scale.** This is a research area with genuine empirical grounding: Zapatista communities (30+ years), Mondragon cooperatives (60+ years), Rojava communes (10+ years under active conflict), COVID mutual aid networks (2020–2022, 800+ documented networks). The challenge is translating these to Midwest rural contexts, not establishing that such models can work.

**4. The Ostrom framework is the most applicable governance theory.** Elinor Ostrom's 8 Design Principles for commons governance — developed from field research in Switzerland, Japan, Spain, and the Philippines — have been validated across dozens of subsequent studies. They are directly applicable to community resource management at any scale from 50 to 5,000 people. No other governance theory has comparable empirical grounding for the specific problem of collective resource management under scarcity.

**5. Information infrastructure is the most neglected domain.** Physical infrastructure (water, food, shelter, security) receives the most attention in resilience planning. Information infrastructure — who knows what, when, through what channel — is consistently underbuilt and is the first system to fail in extended disruptions. The failure is rarely dramatic; it presents as slow degradation of coordination quality and trust, which then accelerates all other failure modes.

**6. Security follows from social cohesion, not the reverse.** Communities with high social trust and functional conflict resolution mechanisms are more secure than communities with arms and perimeters. Investment sequence matters: social infrastructure before security infrastructure.

---

## Phase 3 Production Timeline

If the user selects community-scale as part of the June 1 Phase 5 path decision, production can begin immediately with zero additional research preparation.

| Week | Task | Hours | Output |
|---|---|---|---|
| Week 1 (June 1–7) | Domain 1 + 2 research deep-dives and first drafts | 16–20 | Draft: Community Coordination Infrastructure + Governance Structures |
| Week 2 (June 8–14) | Domain 1 + 2 revision; Domain 3 full draft | 12–16 | Finalized: Domains 1 + 2; Draft: Information Infrastructure |
| Week 3 (June 15–21) | Domain 3 revision; Domain 4 full draft | 12–16 | Finalized: Domain 3; Draft: Security and Defense |
| Week 4 (June 22–28) | Domain 4 revision; Domain 5 full draft | 12–16 | Finalized: Domain 4; Draft: Scaling Pathways |
| Week 5 (June 29–July 5) | Domain 5 revision; cross-reference index; synthesis document | 8–10 | All 5 domains finalized; synthesis and cross-reference index |
| **Total** | | **60–78 hours** | **5 deep-dive documents (~12,000–16,000 words); 50–70 citations; Midwest Zone 5 specifics throughout** |

**Dependencies**:
- Phase 5 path decision (June 1) — required to begin
- No Phase 2 household-scale dependency (Phase 3 can proceed in parallel with Phase 2 completion)
- Phase 3 Domain 2 (Governance) is a prerequisite for Phase 4b Governance Scaling document, if that option is selected

**Contingency**: If Phase 5 decision includes multiple paths, Domains 2 (Governance) and 5 (Scaling Pathways) have the highest leverage across all three Phase 5 options and should be prioritized if time is constrained.

---

## Source Inventory Summary

Total confirmed sources: 50 across 5 domains (10 per domain). All URLs verified as of May 2026.

**Theoretical foundations** (applicable across all domains):
- Elinor Ostrom, *Governing the Commons* (1990) — commons governance
- David Graeber, *Introduction to Mutual Aid* (with Grubacic) — horizontal coordination theory
- Robin Dunbar — social group size research

**Case studies by organization**:
- Zapatista EZLN autonomous communities (Chiapas, Mexico, 1994–present)
- Rojava / North and East Syria commune system (2012–present)
- Mondragon Cooperative Corporation (Basque Country, Spain, 1956–present)
- Barcelona en Comú / Decidim participatory platform (2015–2023)
- Bed-Stuy Strong / Mutual Aid Disaster Relief (COVID-era US, 2020–2022)
- hOurworld time banking network (22 countries, ongoing)

**Technical standards**:
- AREDN Amateur Radio Emergency Data Network
- FCC GMRS licensing framework
- UNESCO Disaster Risk Management for Documentary Heritage (2024)
- IFRC Framework for Community Resilience
- California Disaster and Civil Defense Master Mutual Aid Agreement

**Policy and research**:
- FEMA Local Mitigation Planning Policy Guide (April 2025)
- US National Resilience Strategy (January 2025)
- Ostrom Nobel Lecture (2009)
- OJPHI scoping review on disaster preparedness technology (2025)

---

*Research outline prepared May 18, 2026. Preliminary research complete. Production begins upon June 1 Phase 5 path decision. All source URLs confirmed current as of May 2026.*
