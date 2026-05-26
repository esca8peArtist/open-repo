---
title: "Phase 6 Wave 2 Research Agenda"
project: systems-resilience
phase: 6
wave: 2
status: STAGED — awaiting June 1 path decision
version: 1
created: 2026-05-26
word_count: ~3800
decision_gate: 2026-06-01
activation_window: 2026-06-01 to 2026-06-15 (Path-dependent)
author: General Research Agent
cross_references:
  - phase-6/PHASE_6_RESEARCH_OUTLINE.md
  - phase-6/farm-equipment-repair-research.md
  - phase-6/meshtastic-community-networking-research.md
  - PHASE_5_WAVE_2_MICROGRIDS_RESEARCH.md
  - phase-5-path-decision-framework.md
  - PHASE_5_WAVE_2_PHASE_6_EXECUTION_SEQUENCING.md
---

# Phase 6 Wave 2 Research Agenda

> **Lead finding**: Wave 2 research candidates across all three paths share a structural throughline: the most dangerous gap is not knowledge scarcity but execution architecture. Every domain below — food preservation, water systems, household energy, community healthcare, economic autonomy, and justice structures — has a robust body of technical documentation already available. The deficit is in how communities organize, schedule, and institutionalize those practices before they are needed. Wave 2 research should be organized around this framing: not "what to do" but "how communities have successfully built the capacity to do it under realistic constraints."

---

## Part 1: Wave 1 Recap (Farm Equipment + Communication Infrastructure)

Wave 1 (completed May 26, 2026; Session 1654) produced two parallel research tracks:

**Track A: Farm Equipment Repair Guide** — 44,000+ words across three documents, 78 sources. The core finding was that the documentation problem for Zone 5 agricultural self-sufficiency has effectively closed: Archive.org, ATTRA/NCAT, university extension networks, and FarmHack collectively provide free coverage of almost every equipment category a 20–100 household community needs. The unsolved problem is skill development embedded in the community calendar before crisis. Three equipment tiers were researched in depth: hand tools (Section 1, 8 categories), small equipment (Section 2, 6 categories), and hydraulic systems (Section 3, 5 subsystems). The April 2026 John Deere $99 million right-to-repair settlement and the EPA's February 2026 guidance removed the largest legal barriers to independent repair, but diagnostic software access will not materialize until late 2026 at earliest. Six [RESEARCH NEEDED] markers remain for production: cold-temperature hydraulic seal chemistry, pump bypass specifications for Zone 5 small tractor models, pressure washer freeze-damage protocols, and long-term ethanol-blend fuel storage.

**Track B: Meshtastic Mesh Networking** — 15,600+ words across two documents, 71 sources. The Meshtastic June 2025 cryptographic vulnerabilities (CVE-2025-52464 at CVSSv4 9.5; CVE-2025-55293) were both patched in firmware v2.6.11 and are no longer deployment blockers, but all communities starting in 2026 must run v2.6.11 or later and regenerate all PKI keys. Five hardware platforms were compared for Zone 5 deployment; the RAK WisBlock and Heltec LoRa32 V3/V4 were identified as optimal for backbone and household nodes respectively. A three-tier network architecture (backbone solar nodes → household nodes → mobile responder nodes) was validated against real-world deployments including Am Mellensee, Germany (nine-village simulation, September 2025) and Hurricane Helene mutual aid networks (September 2024). FCC Part 15 unlicensed operation confirmed from eCFR. The primary remaining research gap is Zone 5-specific inter-village link performance at 15–30 km separation in Midwest agricultural terrain.

**Wave 1 status**: Both tracks are execution-ready for a June 1 launch decision. Zero new research is required before the June 1 decision. The [RESEARCH NEEDED] and [TECHNICAL SPEC NEEDED] markers are scoped for resolution during the June 5–15 Phase 6 editorial integration sprint.

---

## Part 2: Wave 2 Research Topics by Path

The June 1 decision selects between three execution paths:
- **Path A**: Community-scale implementation (50–100 person communities; collective infrastructure)
- **Path B**: Individual/household hardening (household-scale resilience; individual agency)
- **Path C**: Integrated governance + infrastructure (institutional architecture; inter-community coordination)

Wave 2 research is organized by path. Each topic includes scope, timeline estimate, priority within Wave 2 sequence, and source library starting points.

---

### Path A: Community-Scale Implementation — Wave 2 Candidates

Path A Wave 2 deepens the physical infrastructure layer established by the Wave 1 farm equipment and communication research. Communities that have solved repair and coordination still need food storage, water security, and waste management to achieve multi-season resilience.

---

#### A-1: Community-Scale Food Preservation and Storage

**Scope**: This domain covers the preservation infrastructure required for a 20–100 household Zone 5 community to maintain a reliable food supply through a Zone 5 winter (November–March) and into an extended disruption. The core research questions are: what preservation methods (canning, lacto-fermentation, root cellaring, dehydration, freeze-drying) provide the best caloric density per unit of capital investment and labor input at community scale? What shared infrastructure model (community canning center, root cellar co-op, preservation party schedule) has the best documented adoption rate in comparable communities? How much storage volume per household is required to carry 50–100 people through a 4–6 month disruption?

The research should cover three layers: (1) preservation method comparison (caloric density, shelf life, energy inputs, skill barrier, equipment cost); (2) community infrastructure models (shared walk-in coolers, community canning days, cooperative cold storage — documented real-world examples in Midwest context); (3) community preservation calendar integration (how to sequence harvest → preservation → consumption to minimize waste and maintain nutritional diversity through winter).

Key gaps to resolve: community-scale lacto-fermentation yields and logistics (individual fermentation is well-documented; 50-gallon batch management is not); root cellar sizing formulas for Zone 5 harvest quantities (MSU Extension has foundational materials but zone-specific sizing for community scale is not consolidated); freeze-drying at community scale (equipment cost vs. yield tradeoff — Harvest Right community units cost $3,500–$5,500 and process 7–16 lbs per batch, which is not well-calibrated against community need).

This topic bridges directly with Phase 4b agricultural intensification work: communities that planted perennials in 2026 need preservation infrastructure by Year 2 (2028) to capture those yields. Research should identify the critical path decision — which preservation infrastructure must be built now vs. which can be deferred until harvest volumes justify it.

**Timeline estimate**: 12–18 research hours for a production-quality document. Priority: Wave 2 first tranche (activate immediately post-June 1 Path A decision).

**Source library starting points**:
- National Center for Home Food Preservation (nchfp.uga.edu) — USDA-approved canning protocols, the authoritative source
- MSU Extension root cellar handout (Cold Cellars for Year-Round Local Food and Farming, 2024)
- NRDC Composting 101 and community food preservation methodology
- FarmstandApp community storage resources documentation
- Survival Stronghold 2026 food shock and fermentation documentation (practical field perspective)
- Iowa State Extension food preservation publications (zone-specific, academic rigor)
- Practical Farmers of Iowa — community food systems resources
- FAO Small-Scale Food Processing guide (technical parameters, global applicability)
- Fermentation association resources (Cultures for Health, Wild Fermentation network)
- Rodale Institute food systems research

---

#### A-2: Community Water Systems (Collection, Purification, Distribution)

**Scope**: This domain covers water security infrastructure for 20–100 household communities that cannot depend on municipal water supply. Research questions: what collection methods (rainwater harvesting, groundwater wells, surface water diversion) are viable in Zone 5? What purification approaches (slow sand filtration, UV treatment, chlorination, ceramic filtration) are appropriate at community scale without electricity dependency? How is distribution engineered and managed — gravity-fed systems, hand pumps, storage tanks — and what is the capital and maintenance profile of each option?

Zone 5 specifics are critical here. Zone 5 winters create freeze risk for surface water infrastructure. Rural northern Illinois and Iowa are predominantly on groundwater (private wells and municipal well systems); southern Wisconsin has more surface water availability. The research must distinguish: communities on private wells (repair + backup infrastructure), communities on municipal supply (alternative infrastructure), and communities near surface water (collection + purification).

The emerging 2026 research context shows solar-powered decentralized purification systems reaching cost parity with grid-tied systems (ScienceDirect 2026), modular containerized treatment units becoming viable for community-scale deployment, and AUC Group's expandable water treatment architecture optimized for small communities. Academic literature from PMC/NIH on decentralized wastewater treatment is now comprehensive.

Key gaps: quantitative sizing formulas for Zone 5 rainfall-based rainwater harvesting at community scale (annual precipitation: 33–38 inches in northern Illinois/Iowa; Zone 5 winter creates storage and freeze challenges); slow sand filtration build specifications for Zone 5 materials availability; Zone 5-specific well repair and hand pump conversion guidance (many rural properties have capped older wells that can be converted to hand pump operation).

This topic integrates directly with the Phase 5 microgrid research: solar-powered water pumping and UV treatment is a key use case for community microgrid load planning. It also integrates with Track B (Meshtastic) through automated water level and contamination monitoring using node telemetry.

**Timeline estimate**: 14–20 research hours for a production-quality document. Priority: Wave 2 first tranche (activate immediately post-June 1 Path A decision; water is foundational to all other community functions).

**Source library starting points**:
- DOE Energy Saver: Planning a Microhydropower System and Microhydropower Systems
- Waterlines journal: Decentralized Solar Powered Water Purification Systems (2025)
- ScienceDirect 2026: Sustainable water purification for off-grid communities
- AUC Group: Affordable Expandable Water Treatment for Communities
- Today's Homeowner 2026: Complete Guide to Off-Grid Water Systems
- Appropedia: Water collection and purification at small community scale
- NRCS: Water management for small farms and rural properties
- State well regulations (Illinois DNR, Iowa DNR, Wisconsin DNR) — legal framework for water collection
- WHO: Small Community Water Supplies (technical guidance series)
- Center for Appropriate Technology (CAT, UK) — grey and rainwater systems technical library

---

#### A-3: Community-Scale Waste Management (Composting, Biogas, Greywater)

**Scope**: This domain covers the waste stream management that prevents the most common failure mode in community resilience scenarios: sanitation collapse. Research questions: what composting systems are appropriate for 20–100 people without municipal collection? Can biogas production at this scale provide meaningful energy yield while managing organic waste? What greywater recycling approaches are legally permissible and practically viable in Zone 5 states?

The 2026 regulatory environment has shifted favorably: California SB 279 expanded composting capacity for community composters (a regulatory signal of broader trends); Minnesota and Illinois have seen incremental movement on residential greywater regulations. The PMC literature on community composting strategies (2024) establishes the methodology framework; three-stage biodegradable composter research (2024) provides technical parameters.

Key findings to develop: (1) community composting at 50-person scale requires dedicated bulking agent management (shredded green waste, cardboard, straw) and thermophilic cycle management to kill pathogens and weed seeds — not well-documented at this specific scale; (2) small-scale biogas (6-10 cubic meter fixed-dome or floating-drum digesters) has extensive developing-world documentation but limited Zone 5 temperature adaptation data (methane production drops below 15°C, creating winter performance gaps); (3) greywater recycling for irrigation is legally complex state-by-state — Illinois: prohibited for household use, with agricultural exceptions possible; Iowa: case-by-case; Wisconsin: limited residential pilot programs.

This research should include a Zone 5 legal landscape table for all three waste systems and identify which approaches are viable under current state law vs. which require regulatory advocacy or operate in grey areas.

**Timeline estimate**: 10–14 research hours. Priority: Wave 2 second tranche (activate 2–3 weeks post-June 1, after water and food preservation are underway).

**Source library starting points**:
- PMC/NCBI: Community composting strategies for biowaste treatment (2024)
- BioCycle magazine: organics recycling state-of-the-art 2026
- NRDC: Composting 101 and community food waste
- Ecologix Environmental Systems: Decentralized wastewater treatment
- SNV Netherlands: Small-scale biogas digest at community scale (developing-world documentation with adaptation pathway)
- Approtech Society: Fixed-dome biogas constructors guide
- Illinois EPA, Iowa DNR, Wisconsin DNR: Greywater and composting regulations
- Graywater Action: Legal landscape and model codes
- Humanure Handbook (Joseph Jenkins): composting human waste at community scale
- FAO: Biogas technology, a training manual

---

### Path B: Individual/Household Hardening — Wave 2 Candidates

Path B Wave 2 focuses on the individual household as the resilience unit. Unlike Path A's collective infrastructure, Path B assumes the household may need to function without reliable community coordination for extended periods. Wave 1 farm equipment and communication research applies here through generator maintenance and household radio nodes, but the specific gaps are in energy independence, medical self-sufficiency, food production, and psychological endurance.

---

#### B-1: Household Energy Systems (Solar, Battery, Backup Generation)

**Scope**: This domain covers household-scale energy independence for Zone 5 residential properties. Research questions: what solar + battery system configuration is appropriate for a Zone 5 household seeking 3–5 day autonomy (covers 90% of grid outage scenarios)? What are the realistic winter performance parameters for LiFePO4 battery systems in Zone 5 conditions? What generator sizing and fuel storage strategy bridges the gap between battery autonomy and extended winter outages?

The 2026 context is materially different from 2024: the federal residential 30% ITC expired December 31, 2025 (Phase 5 microgrid research confirmed this). Illinois net metering for new installations ended January 2025 (supply-only crediting now). This means households evaluating off-grid or hybrid solar in mid-2026 are working in a post-incentive environment, which changes the economic calculation significantly. Research must provide current-state cost modeling, not pre-2025 figures.

The 2026 hardware landscape is clear: LFP (lithium iron phosphate) dominates residential off-grid in 2026 due to temperature stability, 15–20 year calendar life, and 6,000–8,000 deep cycles. System sizing for Zone 5 residential: a typical 3-bedroom home needs 8–12 kW solar, 20–30 kWh battery (covering 1.5–2 days at full load; 3–4 days at reduced load). Medium home systems cost $21,800–$34,500 in current dollars. Micro-hydro is an option only for properties with year-round flowing water with adequate head (rare in Zone 5 flat terrain; relevant primarily in southern Wisconsin ridge-and-valley). Residential wind under 10 kW is viable in exposed rural locations (annual average wind speed >10 mph, typical in open Iowa and northern Illinois).

This topic integrates with the Phase 5 microgrid research (household solar as the input to community microgrid aggregation) and with Track A farm equipment research (generator maintenance applies identically to backup generation systems).

Key gaps: Zone 5 winter battery performance data under sustained cold (LiFePO4 discharge at 0°F to -10°F); snow load and panel efficiency modeling for Zone 5 January through February; cost comparison of on-grid hybrid systems vs. full off-grid under the new post-ITC Illinois/Iowa incentive structures.

**Timeline estimate**: 12–16 research hours. Priority: Wave 2 first tranche, Path B (activate immediately post-June 1 Path B decision).

**Source library starting points**:
- Renogy 2026: Sizing Your Off-Grid Solar System with Solar Calculator
- Renewable Outdoors 2026: Complete Off-Grid Power System Guide
- Solar Tech Online: Off Grid Solar System Complete Guide 2025
- EcoFlow: How to Size a Home Solar System in 2025
- Anern: LiFePO4 Deep Winter Loads — Myths and Performance Data
- ADKMesh: Best Meshtastic Solar Node Builds 2026 (solar sizing methodology applicable to household scale)
- Sundance Power: Micro Hydro, Wind, Solar integration resources
- DOE Energy Saver: Microhydropower Systems and Planning guides
- Montana Renewable Energy Association: Micro-hydro resources
- Illinois DCEO: Solar incentive landscape post-2025 (current net metering policy)
- Iowa Economic Development Authority: Rural energy programs
- Renogy, EcoFlow, Battle Born — manufacturer technical specifications

---

#### B-2: Household Medical Preparedness

**Scope**: This domain covers household-level medical self-sufficiency for Zone 5 families facing scenarios where hospital access is degraded or unavailable for extended periods. Research questions: what wound care and emergency trauma supplies are essential for a household kit extending beyond 72 hours? What OTC medications and herbal alternatives provide the highest coverage for common acute conditions? What diagnostic capabilities (pulse oximetry, blood pressure, temperature, blood glucose) can be maintained at household level? What training programs provide the minimum competency for austere medicine at household level?

The 2026 research landscape shows meaningful convergence between conventional emergency medicine and herbal/austere medicine: Herbal Medics Academy's Wilderness Herbal First Responder (WHFR) certification (80 hours on-site + 20 hours online) combines wilderness medicine and off-grid herbalism with certification. FEMA CERT Basic (three-day free course) provides community-level triage and first aid. The Wilderness First Responder (WFR) certification is the recognized standard for extended care in remote settings (70–80 hours). These training pathways should be mapped against each other and against community needs.

The critical framing for this research is the "austere medicine" paradigm: techniques and materials available to a household without electricity or supply chain access, for conditions that cannot wait for evacuation. Primary focus areas: hemorrhage control (tourniquets, hemostatic agents, wound packing — now standard STOP THE BLEED curriculum); infection management (wound care, antibiotic alternatives when prescription access fails); cardiac/respiratory emergencies (CPR, AED access at community level); chronic disease management (insulin storage, blood pressure medication alternatives).

This topic has direct cross-project relevance: the DV Survivor Safety Playbook (Session 1654) establishes medical preparedness as part of the acute escape phase. That overlap should be documented explicitly.

**Timeline estimate**: 14–18 research hours. Priority: Wave 2 second tranche, Path B (medical preparedness is urgent but slightly less time-sensitive than energy independence).

**Source library starting points**:
- Herbal Medics Academy: WHFR curriculum, Herbal First Aid Course, HOME intensive
- FEMA CERT Basic: official curriculum and materials
- Stop the Bleed: hemorrhage control training program
- Wilderness Medical Associates and NOLS Wilderness Medicine: WFR curriculum
- The Prepared: Home medical supplies list for emergency preparedness
- PrimalSurvivor: OTC medications to stockpile (evidence-reviewed)
- PMC/NIH: Austere medicine research literature
- Rosemary Gladstar's Medicinal Herbs and Matthew Wood's herbalism texts: herbal alternatives for acute conditions
- Medical wilderness texts: William Forgey "Wilderness Medicine" 6th ed.; Eric Weiss "Wilderness Medicine Handbook"
- Mayo Clinic: First aid kits and home medical supply guidance
- PreparedMedical.com: 2026 family health and medical readiness guide

---

#### B-3: Household Food Production (High-Yield Gardening, Aquaponics, Mushroom Cultivation)

**Scope**: This domain covers household-scale food production capable of supplementing 20–40% of caloric needs from a Zone 5 residential property. Research questions: what gardening methods (intensive raised beds, Korean natural farming, Back to Eden wood chip method) maximize caloric yield per square foot in Zone 5? What is the realistic capital cost, skill barrier, and caloric yield of a household aquaponics system? What mushroom cultivation approaches (indoor log inoculation, exterior wood chip beds, oyster bag cultivation) provide the best protein-per-square-foot in Zone 5?

The 2026 aquaponics data is significant: USDA figures show aquaponics uses up to 90% less water than traditional methods and can produce up to 20 times field-crop yields in the same footprint (Farmonaut 2026; FAO Small-Scale Aquaponic Food Production technical reference). A household system producing tilapia + leafy greens can be built for $800–$2,500 and maintained by one person 30–45 minutes daily. Zone 5 winter operation requires heated greenhouse or basement setup — this is the primary capital and energy cost driver and must be addressed directly.

Mushroom cultivation is underresearched in the resilience context. Oyster mushrooms (Pleurotus ostreatus) are cold-tolerant, can be cultivated on straw or wood chips, require minimal infrastructure, and produce 1 lb of protein-dense food per lb of substrate in 3–5 weeks. Shiitake (Lentinula edodes) on oak logs is a 2–3 year investment with 5–7 year production cycle — suitable for perennial food forest integration. King Stropharia (garden giant, Stropharia rugosoannulata) on wood chip beds integrates directly with the Back to Eden garden method and requires zero additional infrastructure if wood chip beds are already in place.

This topic bridges with Phase 4b agricultural intensification work (food forest perennials) and with Path A-1 food preservation (aquaponics yield needs preservation infrastructure for surplus months).

**Timeline estimate**: 12–16 research hours. Priority: Wave 2 second tranche, Path B.

**Source library starting points**:
- FAO: Small-Scale Aquaponic Food Production (openknowledge.fao.org — free technical reference)
- Farmonaut 2026: Aquaponics farming potential and trends
- USDA SARE: Small-scale integrated farming systems
- Tradd Cotter "Organic Mushroom Farming and Mycoremediation" — primary text for outdoor cultivation
- Fungi Perfecti (Paul Stamets resources): mushroom cultivation protocols
- Cornell Small Farms: high-yield market garden production
- Eliot Coleman "Four Season Harvest" and "New Organic Grower" — Zone 5 intensive production
- Back to Eden documentary and research (wood chip gardening method)
- University of Illinois Extension: gardening guides Zone 5-specific
- Practical Farmers of Iowa: intensive vegetable production research

---

### Path C: Integrated Governance + Infrastructure — Wave 2 Candidates

Path C Wave 2 addresses the institutional architecture that must exist for Paths A and B to function at scale beyond a single community. The Wave 1 communication infrastructure research (Meshtastic) already established the technical layer for inter-community coordination; Path C Wave 2 builds the human and legal architecture that runs on top of it.

---

#### C-1: Regional Economic Autonomy (Local Currency, Barter, Supply Chain Localization)

**Scope**: This domain covers the economic systems that allow a regional network of communities (200–2,000 people across multiple villages) to trade, allocate resources, and sustain economic activity when national supply chains are disrupted or when the community is intentionally reducing external dependencies. Research questions: what local currency and time-banking systems have achieved sustained adoption in US rural communities? What barter network protocols work at the scale of 3–10 communities? How do communities localize supply chains for their most critical inputs?

The 2025-2026 landscape shows several relevant developments: the Schumacher Center for a New Economics publishes ongoing local currency research (Ithaca Hours, BerkShares, and newer implementations); Resilience.org published a March 2025 analysis on community currencies going beyond simple barter; the Rapid Transition Alliance documented case studies from European local currencies saving local economies; Nature Index has an active topic cluster on community currencies and local economic systems. The Ekhilur cooperative in Spain pioneered a payment system approach that maximizes euro circulation within the local economy without creating a parallel currency — a potentially lower-friction model for US communities.

Local Exchange Trading Systems (LETS) have been studied academically since the 1990s; the Cambridge Journal of Public Policy published an appraisal establishing their theoretical basis. The critical 2026 research gap is US rural implementation: most documented LETS and local currency systems are urban or semi-urban. Zone 5 Midwest communities present a different context: agricultural surplus trading, equipment sharing, labor exchange, and seed banking are the most likely primary exchange categories.

This topic integrates directly with Path A community infrastructure (food systems create surplus for exchange) and with Phase 5 governance scaling work (Elinor Ostrom's commons governance framework applies directly to community currency design).

**Timeline estimate**: 14–18 research hours. Priority: Wave 2 first tranche, Path C (economic architecture is the enabling layer for other coordination).

**Source library starting points**:
- Schumacher Center for a New Economics: Local Currencies in the 21st Century publications
- Appropedia: Community currencies activism and LETS documentation
- Rapid Transition Alliance: Local currencies case studies
- Resilience.org: Beyond community currencies (March 2025)
- Cambridge Core Journal of Public Policy: New Barter Economy — LETS appraisal
- Nature Index: Community currencies and local economic systems
- Ithaca Hours documentation and retrospective analysis
- BerkShares (Berkshire region MA) — 20-year case study, operational documentation
- E.F. Schumacher "Small is Beautiful" — foundational text
- Michael Shuman "Local Economy Solution" — supply chain localization framework
- Practical Farmers of Iowa: local food supply chain documentation

---

#### C-2: Community Justice and Dispute Resolution Without State Systems

**Scope**: This domain covers the institutional architecture for resolving conflict, addressing harm, and maintaining social cohesion in communities that cannot or choose not to depend on state criminal justice systems. Research questions: what restorative justice models have been validated at community scale (20–500 people) without requiring professional staff or ongoing state support? What dispute resolution mechanisms exist for property, resource allocation, and interpersonal harm? How do communities design and legitimate processes that community members trust and comply with?

The 2026 context shows significant momentum: the National Association of Community and Restorative Justice (NACRJ) 10th National Conference (July 7–10, 2026, New Orleans) drew 1,902 attendees — a 10x growth from 183 in 2007, reflecting a maturing field. Minnesota's Office of Restorative Practices (established 2023) has now distributed $8 million over two years to local programs. Harvard Law's spring 2025 workshop "From seeing conflicts as property to scaling down the state" reflects academic alignment with community-led models. The Sentencing Project's 2025 restorative justice diversion research provides evidence-based parameters.

The academic anchor is Elinor Ostrom's commons governance research (Nobel Prize 2009; eight design principles for sustainable commons management). Principle 7 (minimal recognition of rights to organize) and Principle 6 (mechanisms that allow users to resolve disputes) are directly applicable. PMC/NIH published a 2024 paper on how Ostrom's principles help naive groups create effective enforcement systems — directly actionable for community design.

Key research gaps: horizontal (non-hierarchical) decision processes for resource allocation under scarcity — situations where restorative approaches are insufficient and a legitimated allocation mechanism is required; community response to serial harm when restorative approaches have been exhausted; inter-community disputes (the hardest case — two communities in conflict with no shared authority).

This topic bridges with Phase 5 governance scaling work (regional federation and legal institutions) and with Phase 4b governance path research (Ostrom framework was introduced there; this deepens it significantly).

**Timeline estimate**: 12–16 research hours. Priority: Wave 2 second tranche, Path C.

**Source library starting points**:
- NACRJ: National Association of Community and Restorative Justice — 2026 conference materials
- Center for Justice Innovation: 2025 impact report and restorative justice methodology
- PMC/NIH: Ostrom's restorative justice design principles and group enforcement (2024)
- Sentencing Project: Restorative Justice Diversion evidence review 2025
- Elinor Ostrom "Governing the Commons" — foundational text on self-governance design
- Harvard Negotiation and Mediation Clinical Program: ADR methodology
- Kay Pranis "Circle Processes" — talking circles and peacemaking circles implementation guide
- Community Boards San Francisco: 45+ year operational model for volunteer community conflict resolution
- Hollow Water Community Holistic Circle Healing program (Canada) — documented community healing without incarceration
- Transform Harm (Mia Mingus, adrienne maree brown resources): transformative justice frameworks

---

#### C-3: Community Education Systems (Knowledge Transfer, Skill Training, Youth Development)

**Scope**: This domain covers the formal and informal education infrastructure that allows communities to transmit critical skills, technical knowledge, and cultural values across generations without depending on external school systems. Research questions: what apprenticeship models are viable for Zone 5 rural communities? How do communities design curriculum for skills that don't exist in formal educational systems (fermentation, equipment repair, natural building, animal husbandry, water management)? What youth development frameworks build agency and community attachment while maintaining academic competency?

The 2026 research context: JFF (Jobs for the Future) has an active Strengthening Education-to-Career Pathways in Rural Areas initiative. PMC published research on positive youth development in rural communities integrating social work, psychology, and education (2024). The agricultural extension and 4-H models (both well-documented) provide validated frameworks for rural skill transmission. The Foxfire model (Appalachian experiential education, 1966–present) documents 55 years of community knowledge transmission through youth-led oral history and documentation projects.

The critical insight for resilience communities: education systems should be designed so that teaching is itself a form of skill reinforcement — when community members teach fermentation, equipment repair, or map-reading, the act of teaching deepens their own competency while transmitting to the next generation. The most resilient communities are those where the distinction between "learner" and "teacher" is fluid and rotational.

Zone 5-specific priorities: agricultural timing knowledge (planting calendars, frost dates, seed saving windows — this knowledge erodes rapidly when commercial inputs replace experiential practice); equipment maintenance (documented in Wave 1 but the transmission challenge is different from the technical content); water and sanitation management; food preservation timing and safety.

**Timeline estimate**: 10–14 research hours. Priority: Wave 2 third tranche, Path C (education systems are the longest investment horizon; can be staged later without blocking other Path C work).

**Source library starting points**:
- JFF: Strengthening Education-to-Career Pathways in Rural Areas (2026)
- PMC: Positive youth development in rural communities (2024)
- Foxfire Fund (foxfire.org): 55-year model of community knowledge documentation
- 4-H National: Agricultural youth development curriculum
- Highlander Research and Education Center: popular education methodology
- Reggio Emilia approach: project-based community learning (Italian origin; US adaptations extensive)
- Ivan Illich "Deschooling Society" — theoretical foundation for community-led learning networks
- John Holt "How Children Learn" — autonomous learning and skill acquisition
- Cornell Small Farms apprenticeship program documentation
- MOSES Organic Farming Conference: farmer training and mentorship model

---

## Part 3: Wave 2 Timeline and Sequencing

### Time Estimates by Path

| Topic | Path | Research Hours | Priority Tranche | Earliest Start | Primary Blocker |
|---|---|---|---|---|---|
| A-1: Food Preservation | A | 12–18 | Wave 2 T1 | June 1 + Path A decision | Path A selection |
| A-2: Community Water Systems | A | 14–20 | Wave 2 T1 | June 1 + Path A decision | Path A selection |
| A-3: Waste Management | A | 10–14 | Wave 2 T2 | 2 weeks post-June 1 | A-1 and A-2 baseline done |
| B-1: Household Energy | B | 12–16 | Wave 2 T1 | June 1 + Path B decision | Path B selection |
| B-2: Household Medical | B | 14–18 | Wave 2 T2 | 2 weeks post-June 1 | Path B selection |
| B-3: Food Production | B | 12–16 | Wave 2 T2 | 2 weeks post-June 1 | Path B selection |
| C-1: Economic Autonomy | C | 14–18 | Wave 2 T1 | June 1 + Path C decision | Path C selection |
| C-2: Community Justice | C | 12–16 | Wave 2 T2 | 2 weeks post-June 1 | Path C selection |
| C-3: Education Systems | C | 10–14 | Wave 2 T3 | 4 weeks post-June 1 | C-1 and C-2 complete |

**Total Wave 2 research scope**:
- Path A alone: 36–52 hours
- Path B alone: 38–50 hours
- Path C alone: 36–48 hours
- All three paths combined: 110–150 hours

This is a 3–4 week intensive sprint if two research agents work in parallel, or 6–8 weeks sequential. The hybrid execution model from PHASE_5_WAVE_2_PHASE_6_EXECUTION_SEQUENCING.md (Option 3) suggests beginning Wave 2 research during June 10–July 10 alongside Phase 6 editorial integration, which fits within these estimates.

---

## Part 4: Cross-Domain Bridges to Phase 5

Wave 2 research does not operate in isolation. Each topic connects to previously completed Phase 5 research in ways that should be made explicit in Wave 2 documents:

**A-1 Food Preservation ↔ Phase 4b Agricultural Intensification**: The food forest and seed saving work from Phase 4b creates the harvest volumes that require preservation infrastructure. Wave 2 should explicitly size preservation capacity against Phase 4b yield projections (beginning Year 2, 2028).

**A-2 Community Water ↔ Phase 5 Microgrids**: Solar-powered water pumping and UV purification are primary use cases for community microgrid load planning (documented in PHASE_5_WAVE_2_MICROGRIDS_RESEARCH.md). Wave 2 should include a water load estimate in the microgrid load analysis.

**A-3 Waste Management ↔ Phase 4b Agricultural Intensification**: Compost output from community waste management directly feeds Phase 4b food forest soil-building. The biogas yield estimate from a 50-person community (approximately 2–4 kW thermal equivalent daily) contributes to microgrid load balancing.

**B-1 Household Energy ↔ Phase 5 Microgrids**: Household solar as the aggregated input to community microgrid. Wave 2 should explicitly model the aggregation of 20 household 8–12 kW systems into a community microgrid, including islanding protocols and load sharing.

**B-2 Household Medical ↔ DV Survivor Safety Playbook**: Medical preparedness protocols developed in the DV Survivor Safety Playbook (Session 1654) are directly applicable to household medical preparedness. Wave 2 should cross-reference the stalkerware removal and crisis response protocols as part of the austere medicine context.

**B-3 Food Production ↔ Phase 4b Agricultural Intensification**: Aquaponics and intensive household gardening complement the perennial food forest — different yield timing curves mean household production can carry protein and greens in early years (Year 1–4) while perennials establish.

**C-1 Economic Autonomy ↔ Phase 5 Governance Scaling**: The Ostrom commons framework introduced in Phase 5 Governance Scaling (Path C analysis) extends directly to community currency design. Ostrom Principle 2 (congruence between rules and local conditions) is the design basis for a Zone 5 rural currency emphasizing agricultural surplus exchange.

**C-2 Community Justice ↔ Phase 5 Governance Scaling + Regional Federation**: The regional governance federation research (regional-governance-federation-framework.md) establishes the inter-community coordination architecture; Wave 2 justice research deepens the dispute resolution layer of that framework.

**C-3 Education Systems ↔ Phase 4b Knowledge Preservation**: Phase 4b Knowledge Preservation (Kiwix, oral history, community knowledge audit) is the documentation layer; Wave 2 Education Systems is the transmission layer. Together they form a complete knowledge resilience architecture.

---

## Part 5: June 1 Decision Handoff

### Immediate Activation (June 1–5, path-dependent)

**If Path A selected**: Activate A-1 (Food Preservation) and A-2 (Community Water) simultaneously. These are the two highest-leverage community resilience gaps and have no internal dependencies between them. A-3 (Waste Management) begins 2 weeks later when A-1 and A-2 baselines are established.

**If Path B selected**: Activate B-1 (Household Energy) immediately — this is the fastest path to household resilience uplift and integrates directly with the completed microgrid research. B-2 and B-3 begin in parallel 2 weeks later.

**If Path C selected**: Activate C-1 (Economic Autonomy) immediately — economic architecture is the enabling layer that makes C-2 and C-3 functional. C-2 (Community Justice) begins 2 weeks later. C-3 (Education Systems) begins 4 weeks later after the institutional governance layer is established.

**If multiple paths selected** (likely in Phase 6 integrated approach): Activate T1 topics across all selected paths simultaneously (A-1 + B-1 + C-1). These have no cross-path dependencies and can run in parallel with a 2-agent execution model.

### Staged for Later (June 15+)

All T2 and T3 topics across every path are staged for the second half of June. This staging is not about deprioritization — it is about sequencing so that foundational research (energy, water, economic architecture) establishes the framing that makes the secondary topics more focused and less likely to require rework.

### Deferrable Without Harm (Path-conditional)

Topics that can be deferred to August without meaningful loss:
- C-3 (Education Systems): longest investment horizon, no seasonal urgency, integrates with Knowledge Preservation which already has substantial Phase 4b foundation
- A-3 (Waste Management): can be deferred if community is not yet producing surplus harvest (pre-2028 for perennial yields)
- B-3 (Food Production): if agricultural intensification (Path A) is the primary food strategy, household production is supplemental and can be developed later

---

*Confidence assessment: High on Wave 1 recap (primary documents read). High on source library identification (web search 2026 current). Medium on time estimates (extrapolated from Wave 1 actual performance; Wave 2 topics have less pre-existing foundation). Medium-high on path sequencing (based on documented Phase 5 path decision framework and cross-domain bridge analysis; actual sequencing subject to June 1 user decision). Research markers (RESEARCH NEEDED) within each topic scope are explicit gaps identified during this pre-staging, not during production research.*
