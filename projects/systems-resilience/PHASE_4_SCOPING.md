---
title: "Phase 4 Scoping — Optional Expansion Beyond Community Scale"
project: systems-resilience
region: "Midwest US (Zone 5)"
created: 2026-05-17
phase: 4
status: scoping
audience: "Project lead (Anya) — decision document"
word_count: ~4000
---

# Phase 4 Scoping — Optional Expansion

> **Purpose**: Decision document for whether, when, and in what order to produce Phase 4 content.  
> **Not a research document**: This is scoping only — enough detail to decide, not enough to execute.  
> **Phase 1-3 status**: All three phases complete. ~100,000 words, 280+ citations, 35+ case studies.

---

## The Core Question

Phase 1-3 covers individual survival → household coordination → community-scale crisis response. Each phase was written because there was no production-ready alternative that met the specificity standard (exact quantities, Zone 5 timing, primary sources).

Phase 4 is genuinely optional. Before deciding, the question to answer is:

> "What critical failure mode does Phase 1-3 leave unaddressed?"

The honest answer: Phase 1-3 assumes a community can survive a 3–24 month disruption. Phase 4 addresses what happens if disruption extends beyond 2 years — or if the disruption is deep enough that schools don't reopen, equipment can't be serviced, agricultural supply chains don't restore, and local government must operate without federal/state support. Phase 4 is not crisis response. It is **civilizational continuity at village scale**.

This changes the stakes. Phase 4 topics are not supplements to Phase 1-3 — they are the next layer of the stack, activated only when the shorter-duration responses have been exhausted or when Anya chooses to document long-term self-sufficiency practices.

---

## Topic 1: Education and Knowledge Preservation

### What Would Be Covered

**The core problem**: Modern knowledge is stored in institutions (schools, libraries, internet infrastructure, professional licensing bodies) that fail in the same cascades that trigger Phase 3 activation. A community can sustain itself physically — water, food, energy, medical — and still lose the next generation's ability to read, reason mathematically, diagnose complex problems, or maintain technical systems.

**Document architecture** (one deep-dive, ~8,000-10,000 words):

**Section 1: Knowledge Inventory and Priority Triage**
- Taxonomy of knowledge at risk: literacy, numeracy, core sciences (biology, physics, chemistry), applied skills (carpentry, metalworking, medicine, agriculture), civic/governance competency
- Prioritization framework: What must every adult know? What must at least one person in a village know? What can be rebuilt from books alone?
- Practical tool: Community Knowledge Audit worksheet (identify gaps, redundancies, single points of failure)

**Section 2: Oral Transmission Methods**
- Structured oral history methodology (drawn from NEH Cultural and Community Resilience Program, Foxfire Project model)
- Apprenticeship design: pairing elders with working-age adults and youth; competency-based milestone tracking
- Story as mnemonic: Indigenous approaches to encoding procedural knowledge in narrative (Pacific Rim and Mediterranean case studies from IDRiM 2025)
- Zone 5 Midwest context: Agricultural knowledge from elder farmers (planting dates, soil reading, pest identification) is most urgent given 20+ year generational transmission lag

**Section 3: Analog Documentation Infrastructure**
- Paper and ink durability: acid-free archival paper, pigment-based ink vs. dye-based ink longevity
- Book selection protocol: which books to print, bind, and weatherproof (Kiwix ZIM files printable selections, Project Gutenberg public domain practical manuals)
- Filing and retrieval: physical indexing systems that work without computers
- Distributed copies: the 3-location rule (original + two redundant physical copies in geographically separated locations)

**Section 4: Offline Digital Infrastructure**
- Kiwix server on Raspberry Pi (~$50 hardware, ~$0 software): serves Wikipedia, medical references, Khan Academy, Project Gutenberg to any WiFi device without internet
- Content selection for Midwest resilience: which ZIM files to download (offline Wikipedia, Wiktionary, iFixit repair manuals, Khan Academy STEM, medical references)
- Power requirements: Raspberry Pi 4 runs on 5W; 10Ah battery can power it for 20+ hours
- Failure modes: SD card failure (use high-endurance cards; maintain 2 copies), hardware failure (one spare Pi stored)

**Section 5: Structured Learning Without Schools**
- Learning pod design: 6–12 children, one adult facilitator (not necessarily a credentialed teacher)
- Curriculum sequencing: literacy → numeracy → applied science → skills apprenticeship (borrowing from homeschool curricula and Foxfire Project)
- Assessment without credentials: competency demonstration over testing; portfolio approach
- Adult continuing education: agricultural extension model adapted for post-disruption context (peer teaching, rotating subject expertise)

**Zone 5 Midwest Specifics**:
- Seed Savers Exchange Heritage Farm (Decorah, Iowa) as model for living knowledge preservation (botanical knowledge preserved through practice, not just documentation)
- Prairie ecosystem knowledge (native plants, foraging, soil indicators) at high risk of loss as elder naturalists age out
- Farm-specific knowledge (tile drainage patterns, drainage district maps, soil surveys) increasingly digitized and thus at risk

### Key Sources (Education/Knowledge)

1. NEH Cultural and Community Resilience Program — oral history methodology: [neh.gov/blog/preserving-resilience-through-oral-histories](https://www.neh.gov/blog/preserving-resilience-through-oral-histories-snapshot-nehs-cultural-and-community-resilience)
2. Foxfire Series (Volumes 1-12, Penguin Random House) — apprenticeship-based knowledge capture from Appalachian elders: [penguinrandomhouse.com/series/foxfire-series](https://www.penguinrandomhouse.com/series/C84/foxfire-series/)
3. Kiwix — offline Wikipedia and educational content server: [kiwix.org](https://kiwix.org/en/)
4. Offline Knowledge Hubs guide — practical implementation of digital survival libraries: [offgridsurvival.com/offline-knowledge-hubs](https://offgridsurvival.com/offline-knowledge-hubs-building-your-own-digital-survival-library/)
5. Kiwix in Tanzania — field evidence of rural offline deployment: [diff.wikimedia.org](https://diff.wikimedia.org/2024/02/03/kiwix-as-a-tool-to-access-educational-and-informational-content-offline-in-tanzania/)
6. UNESCO Disaster Risk Management for Documentary Heritage (2024 toolkit — 6 training modules): [unesdoc.unesco.org](https://unesdoc.unesco.org/ark:/48223/pf0000391132)
7. IDRiM Journal (2025) — traditional knowledge as disaster resilience: [idrimjournal.com](https://www.idrimjournal.com/article/138086-disaster-preparedness-through-traditional-drr-related-knowledge-a-comparative-study-of-the-cultures-of-prevention-in-the-pacific-rim-and-mediterranea.pdf)
8. Seed Savers Exchange — living knowledge preservation through practice: [seedsavers.org](https://seedsavers.org/preservation/)
9. Project Gutenberg — 70,000+ public domain books including practical manuals: [gutenberg.org](https://www.gutenberg.org/)
10. Village Earth Appropriate Technology Library — 1,050 books on self-reliance: [villageearth.org/appropriate-technology-library](https://villageearth.org/home/appropriate-technology-library/)

### Scope Estimate

| Component | Hours |
|---|---|
| Research (oral history, offline infra, curriculum design) | 4–6 |
| Section 1-2 (knowledge inventory + oral transmission) | 3–4 |
| Section 3-4 (documentation + offline digital) | 3–4 |
| Section 5 (structured learning) | 2–3 |
| Zone 5 specifics, sources, cross-references | 1–2 |
| **Total** | **13–19 hours** |

**Output**: 1 deep-dive document, ~8,000–10,000 words, 25–35 citations

---

## Topic 2: Agricultural Intensification

### What Would Be Covered

**The core problem**: Phase 1 covers a 400 sq ft garden for one person; Phase 2 covers coordinated household food production. But neither covers what happens when a community of 50-150 people must produce most of its calories locally — when supply chains are disrupted not for weeks but for years. This requires a qualitatively different approach: multi-year crop planning, perennial systems that reduce annual labor, community-scale seed saving, and soil-building practices that compound over time.

**Document architecture** (two deep-dives, ~8,000-10,000 words each):

**Document A: Perennial Systems and Food Forest Design (Zone 5)**

Section 1: The Case for Perennials
- Annual vs. perennial energy accounting: annual garden requires ~60 hours/person/year of cultivation; established food forest requires ~15 hours/person/year after Year 5
- Perennial system yield timeline: establishment cost (3-5 years before full production) vs. 20-50 year production window
- Zone 5 hardy perennial food crops: hazelnuts, elderberries, serviceberries (saskatoon), pawpaw, persimmon (native), hardy kiwi (some varieties), raspberries, currants, gooseberries, asparagus, Jerusalem artichoke, ramps, ostrich fern (fiddleheads)
- Kernza (intermediate wheatgrass): perennial grain developed at the Land Institute (Salina, Kansas); 10-foot roots; 96% more nitrate absorption than corn/soy; yields 500-800 lbs/acre after establishment

Section 2: Food Forest Design for Midwest Climate
- 7-layer food forest design adapted for Zone 5: canopy (nut trees), sub-canopy (fruit trees), shrub layer (berries), herbaceous (vegetables/herbs), ground cover (nitrogen fixers), root zone (tubers), climbing (vines)
- Spatial layout calculations: what 1 acre can produce in a Zone 5 food forest vs. conventional garden
- Savanna Institute case studies: 14 farms across Minnesota, Iowa, Illinois, Wisconsin in woody perennial polyculture research; Red Fern Farm (Wapello, Iowa) long-term data

Section 3: Intercropping and Three Sisters Intensification
- Three Sisters (corn-bean-squash) yield premium: 28-53% land efficiency gain vs. monoculture (documented in Phase 1 agriculture doc — Phase 4 scales this to field production)
- Community-scale Three Sisters field design: 1/4 acre per 4 people for caloric supplement
- Other documented intercropping combinations: tomato-basil, garlic-roses (pest management), winter rye-vetch cover crop blend

Section 4: Soil Building at Multi-Year Scale
- Soil organic matter targets: 3-5% SOM in Zone 5 clay-loam soils; below 2% is degraded; above 5% is exceptional
- Year-by-year soil building protocol: cover crops → compost → biochar → compost tea → reduced tillage sequence
- No-till transition for Midwest soils: first 2-year results (Iowa State University field data, 2025)
- Community composting design: 3-bin system serving 50-150 people; 500 sq ft footprint; 8-12 cubic yards output/year

**Document B: Community Seed Saving and Variety Selection**

Section 1: Seed Saving Fundamentals
- Open-pollinated vs. hybrid: why hybrids cannot be saved; which variety categories can be
- Isolation distances for Zone 5 seed saving: corn (1 mile), squash (500 ft), tomato (25 ft), beans (self-fertile)
- Seed viability lifespans (stored at 40°F, <40% RH): tomato (4 years), corn (2-3 years), bean (3 years), squash (4 years), parsnip (1 year — must save annually)

Section 2: Heirloom Variety Selection for Zone 5
- Criteria: 90-day or shorter maturity (Zone 5 frost-free window 150-165 days, but late spring/early fall frosts compress reliable window); drought tolerance; disease resistance to Midwest-specific pathogens (gray leaf spot, northern corn blight, late blight on tomatoes)
- Recommended varieties with sources: Seed Savers Exchange catalogue (14,000+ varieties; Heritage Farm in Decorah, Iowa — accessible as regional source)
- Regional variety documentation: county-level heirloom varieties with local adaptation (e.g., Minnesota Midget cantaloupe, North Star cherry, Bloody Butcher corn)

Section 3: Community Seed Library Setup
- Physical infrastructure: envelopes, airtight jars or mylar bags, silica gel desiccant, freezer for long-term storage
- Governance: check-in/check-out system; renewal requirement (save and return seeds within 2 seasons)
- Catalog and indexing: paper card catalog with germination rates, source, planting notes
- Midwest seed library examples: Omaha Sprouts regional buying guide; local seed swap networks

### Key Sources (Agriculture)

1. Savanna Institute — Midwest agroforestry research, 14-farm study: [besjournals.onlinelibrary.wiley.com](https://besjournals.onlinelibrary.wiley.com/doi/full/10.1002/pan3.10275)
2. Woody perennial polycultures in the U.S. Midwest — Ecosphere (2022): [esajournals.onlinelibrary.wiley.com](https://esajournals.onlinelibrary.wiley.com/doi/full/10.1002/ecs2.3890)
3. Land Institute — Kernza perennial grain: [landinstitute.org/our-work/perennial-crops/kernza](https://landinstitute.org/our-work/perennial-crops/kernza/)
4. Agroforestry for Food Project — University of Illinois long-term trial: [sustainability.illinois.edu/research/agroforestry-for-food-project](https://sustainability.illinois.edu/research/agroforestry-for-food-project/)
5. Red Fern Farm (Wapello, Iowa) — on-farm perennial polyculture case study
6. Modern Farmer — Midwest agroforestry farmers: [modernfarmer.com/2024/02/midwest-agroforestry-farmers](https://modernfarmer.com/2024/02/midwest-agroforestry-farmers/)
7. Seed Savers Exchange — heirloom variety collection and community exchange: [seedsavers.org](https://seedsavers.org/preservation/)
8. Omaha Sprouts — Midwest regional seed buying guide: [omahasprouts.org/post/midwest-seed-buying-guide](https://www.omahasprouts.org/post/midwest-seed-buying-guide)
9. Regenerative cropping systems — Upper Midwest transition study (Journal of Environmental Quality, 2025): [acsess.onlinelibrary.wiley.com](https://acsess.onlinelibrary.wiley.com/doi/10.1002/jeq2.70084)
10. MDPI — Perennial polycultures in sustainable agriculture: [mdpi.com/2071-1050/9/12/2267](https://www.mdpi.com/2071-1050/9/12/2267)
11. Edible forest in Normal, Illinois — urban food forest demo site: [extension.illinois.edu](https://extension.illinois.edu/news-releases/edible-forest-takes-root-normal)
12. Perennial grains overview — EESI: [eesi.org/articles/view/perennial-grains-could-be-the-future-of-sustainable-agriculture](https://www.eesi.org/articles/view/perennial-grains-could-be-the-future-of-sustainable-agriculture)

### Scope Estimate

| Component | Hours |
|---|---|
| Research (perennial species, Zone 5 yield data, seed saving protocols) | 5–7 |
| Document A: Perennial systems + food forest design | 5–7 |
| Document B: Seed saving + variety selection | 4–6 |
| Cross-references to Phase 1 agriculture + Phase 2 food coordination | 1–2 |
| **Total** | **15–22 hours** |

**Output**: 2 deep-dive documents, ~8,000–10,000 words each, 30–40 combined citations

---

## Topic 3: Governance Scaling

### What Would Be Covered

**The core problem**: Phase 3 covers governance for 25–150 people within a single community. But when disruptions extend and adjacent communities can no longer function independently, governance must scale up: towns that share water sources, roads, or medical facilities must coordinate. Districts of 500–2,000 people require formal inter-municipal agreements, resource allocation mechanisms, and conflict resolution procedures that don't yet exist in most Midwest rural areas.

**Document architecture** (one deep-dive, ~8,000-10,000 words):

**Section 1: The Governance Gap**
- Phase 3 ends at ~150 people (village scale). Between 150-500 people (small town or multi-village district), formal governance exists (selectboard, town council) but is often poorly designed for extended disruption
- The Christchurch lesson: top-down Canterbury Earthquake Recovery Commission (CERC) created after the 2011 earthquake slowed grassroots recovery; bottom-up organizations (Greening the Rubble, community gardens, civil society groups) performed better in immediate crisis; the tension between formal authority and informal capacity is the central governance problem at Phase 4 scale
- Polycentric governance (Ostrom): nested decision-making at village, district, and regional levels; each level has defined scope; conflict resolution escalates upward only when lower levels fail

**Section 2: Formal Governance Structures**
- Selectboard/town council authority during declared emergencies: what emergency powers exist in Midwest states; what can be enacted locally vs. requires state authorization
- FEMA Continuity of Government (COG) requirements: every municipality should have a COG plan; template from FEMA Local Elected Officials Guide (2025)
- Inter-municipal agreements (IMAs): how towns formally agree to share resources (mutual aid agreements, Memoranda of Understanding); template structure for water sharing, road maintenance, medical facility access
- Regional council design for 500-2,000 people: rotating representation, quorum rules, binding vs. advisory decisions

**Section 3: Resource Allocation Under Scarcity**
- Ostrom's 8 Design Principles for sustainable commons governance (adapted for Midwest towns):
  1. Clearly defined boundaries
  2. Rules match local conditions
  3. Collective choice arrangements
  4. Monitoring
  5. Graduated sanctions
  6. Conflict resolution mechanisms
  7. Recognized right to organize
  8. Nested enterprises
- Rationing protocols: what to ration (fuel, food, medical supplies, water), how to ration (household-based, needs-based, lottery), who decides (Emergency Council with civilian oversight)
- Price controls vs. barter: evidence from disaster economics; why price gouging prevention requires substitutes (time banking, community exchange — already covered in Phase 3 mutual aid networks)

**Section 4: Conflict Resolution at Scale**
- The three common conflicts in extended disruption: access to shared resources, labor obligations vs. autonomy, in-group/out-group tension (who counts as community)
- Restorative justice vs. punitive enforcement: practical options without functioning courts
- Mediator training: who in a community can serve as mediator; 3-day training curriculum outline (based on Community Boards conflict resolution model)
- Documentation: why written records of decisions matter even in crisis; simple record-keeping system

**Section 5: Regional Coordination (500–2,000 People)**
- Inter-community communication networks: radio nets, courier systems, scheduled assemblies
- Mutual aid beyond Phase 3 scale: when one community's surplus meets another's deficit; tracking and reciprocity across communities
- Case study: Transition Towns network (992 registered communities in 67 countries) — what works at regional coordination scale

**Zone 5 Midwest Specifics**:
- County Emergency Management Coordinators: existing state-funded role that Phase 4 governance connects to
- National Association of Counties resilience frameworks: Midwest-specific resources
- Township government structure in Midwest states (Iowa, Illinois, Minnesota): unique to Midwest; township trustees have specific emergency powers distinct from municipal governments

### Key Sources (Governance)

1. Elinor Ostrom — Governing the Commons; 8 Design Principles: [wikipedia.org/wiki/Elinor_Ostrom](https://en.wikipedia.org/wiki/Elinor_Ostrom)
2. Polycentric Governance of Complex Economic Systems — Ostrom Nobel Lecture: [nobelprize.org](https://www.nobelprize.org/uploads/2018/06/ostrom_lecture.pdf)
3. FEMA Local Elected Officials Guide (2025): [fema.gov](https://www.fema.gov/sites/default/files/documents/fema_npd_local-elected-officials-guide_2025.pdf)
4. LSE Cities — Emergency Governance for Cities and Regions: [lse.ac.uk](https://www.lse.ac.uk/Cities/Assets/Documents/EGI-Publications/PB02-EN.pdf)
5. NLC — Local Leaders' Role Before, During and After Disasters: [nlc.org](https://www.nlc.org/article/2023/09/01/local-leaders-role-before-during-and-after-disasters/)
6. Christchurch post-earthquake governance — bottom-up case study: [researchgate.net](https://www.researchgate.net/publication/312192326_Bottom-Up_Governance_after_a_Natural_Disaster_A_Temporary_Post-Earthquake_Community_Garden_in_Central_Christchurch_New_Zealand)
7. Disaster Resiliency of U.S. Local Governments — COVID-19 lessons (PMC): [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC7300832/)
8. All Resilience is Local — implications of federal devolution: [teneo.com](https://www.teneo.com/insights/articles/all-resilience-is-local-implications-of-federal-devolution-of-disaster-preparedness-response/)
9. Pew Charitable Trust — $1 mitigation = $6 recovery (cost-benefit data point for governance investment)
10. MRSC — Local Government Emergency Planning: [mrsc.org](https://mrsc.org/explore-topics/public-safety/emergencies/emergency-planning)

### Scope Estimate

| Component | Hours |
|---|---|
| Research (Ostrom, FEMA frameworks, Christchurch, township law) | 4–6 |
| Sections 1-2 (governance gap + formal structures) | 3–4 |
| Sections 3-4 (resource allocation + conflict resolution) | 3–4 |
| Section 5 (regional coordination + Zone 5 specifics) | 2–3 |
| **Total** | **12–17 hours** |

**Output**: 1 deep-dive document, ~8,000-10,000 words, 25-35 citations

---

## Topic 4: Technology Repair and Maintenance

### What Would Be Covered

**The core problem**: Phase 1-3 documents assume the equipment works. A solar panel system, hand pump, generator, radio, chainsaw, or water filtration system is worth nothing when it fails and there is no repair technician, no parts, and no internet-based repair guide. The Right to Repair movement has documented exactly how fragile the current model is: John Deere's 2026 $99M settlement acknowledged that farmers were locked out of their own equipment by software restrictions. In an extended disruption, every piece of critical equipment will eventually fail. The community that can repair it survives; the one that can't doesn't.

**Document architecture** (two deep-dives, ~7,000-9,000 words each):

**Document A: Community Repair Infrastructure**

Section 1: The Repair Gap
- Dependency audit: what equipment does a 50-150 person Midwest community depend on? (generators, well pumps, solar systems, chainsaws, hand tools, vehicles, radio equipment, medical devices)
- Failure mode analysis: what fails first, how fast, and what are consequences?
- The Right to Repair context: 20 states introduced farm equipment right-to-repair bills in 2025; John Deere $99M settlement (April 2026); what this means for community repair capacity going forward

Section 2: Community Tool Library and Repair Shop
- Tool library design: governance (borrowing rules, maintenance responsibility, deposit system), storage (weatherproof building, inventory system), skill requirements for high-risk tools
- Essential tool inventory for a 50-150 person community: hand tools (non-electric), power tools (cordless), specialty tools (wire strippers, multimeter, soldering iron, pipe threader)
- Community repair shop design: 400 sq ft minimum; benches, vises, parts storage, reference library
- iFixit + Repair Café model: iFixit's 30,000+ free repair guides + Repair Café's 2,200+ community repair events worldwide; integration into community repair culture

Section 3: Repair Knowledge Infrastructure
- Offline repair manual library: iFixit repair guides (downloadable), Village Earth Appropriate Technology Library (1,050 books, 150,000+ pages), equipment-specific manuals downloaded and printed
- Skill training: identify 2-3 people per equipment category to train before disruption; Community Boards repair training model
- Specialty knowledge at risk: electronics diagnosis (oscilloscope use, circuit tracing), hydraulics (pump rebuild, valve replacement), welding (MIG, stick, oxy-acetylene)

**Document B: Equipment-by-Equipment Maintenance Protocols**

Section 1: Solar Power System Maintenance
- Panel cleaning schedule: every 3-6 months (dust/debris); more often in high-dust periods (harvest)
- Battery maintenance: flooded lead-acid (check specific gravity quarterly, equalize annually), AGM/lithium (monitoring only); replacement intervals
- Inverter/charge controller diagnostics: error code interpretation without internet; common failure modes and field fixes
- NREL off-grid installation and maintenance manual: [docs.nrel.gov](https://docs.nrel.gov/docs/fy24osti/89249.pdf)

Section 2: Well Pump and Water System Maintenance
- Hand pump maintenance (Simple Pump, PVC pitcher pump): annual seal inspection, leathercup replacement interval (3-5 years), cylinder rod inspection
- Electric submersible pump: signs of failure (reduced flow, cycling, air in line); pull-and-inspect procedure without contractor
- Water storage tank inspection: sediment accumulation, liner inspection, screen replacement
- Pressure tank maintenance: air charge check, bladder failure diagnosis

Section 3: Generator Maintenance
- Oil change intervals: every 100 hours (standard recommendation); every 50 hours under heavy load
- Carburetor cleaning: gasoline gum deposits after 30 days of storage; ethanol-blend fuel acceleration of degradation; Seafoam treatment protocol
- Startup without grid: cold-weather starting (below 20°F), load management
- Fuel storage: rotation schedule; stabilizer use; expected shelf life (treated gasoline: 1-3 years; diesel: 1-2 years)

Section 4: Small Engine Maintenance (Chainsaw, Tractor, Water Pump)
- Chainsaw: chain sharpening (file diameter by chain pitch, 2-stroke fuel mix, bar oil, air filter cleaning)
- Small tractor/ATV: belt inspection, hydraulic fluid check, tire pressure and seating
- Hand tools: forge-welding as last resort; handle replacement; axe eye tightening (water swelling)

Section 5: Electronics and Communication Equipment
- Radio (GMRS/ham): antenna inspection, battery replacement, programming without software (manual programming from spec sheet)
- Basic electronics diagnosis: multimeter use (continuity, voltage, resistance); identifying failed components (capacitors, fuses, diodes)
- Soldering: through-hole component replacement; flux cleaning; joint inspection
- Limits: modern microcontrollers are essentially unrepairable without specialist equipment; design for replaceable components from the start

**Zone 5 Midwest Specifics**:
- Freeze protection: pipe trace heat tape, pump house insulation, winterization protocols for outdoor equipment
- Corrosion: Midwest road salt + humid summers accelerate metal corrosion; annual inspection schedule calibrated to Zone 5 weather
- Harvest season load: equipment used at 200-300% normal intensity during August-October; pre-harvest inspection checklist

### Key Sources (Technology Repair)

1. iFixit — 30,000+ free repair guides, Right to Repair advocacy: [ifixit.com](https://www.ifixit.com/)
2. iFixit + Repair Café partnership: [ifixit.com/News/66508/ifixit-and-repair-cafe-join-forces](https://www.ifixit.com/News/66508/ifixit-and-repair-cafe-join-forces)
3. Repair Café Foundation — 2,200+ community repair events worldwide: [repaircafe.org](https://www.repaircafe.org/)
4. NREL — Off-Grid Solar System Installation, Operations, and Maintenance: [docs.nrel.gov/docs/fy24osti/89249.pdf](https://docs.nrel.gov/docs/fy24osti/89249.pdf)
5. Solar United Neighbors — Solar Owner's Manual: [solsmart.org](https://solsmart.org/wp-content/uploads/imported-files/English-SolarUnitedNeighbors-Solar-Owners-Manual-2021.pdf)
6. Simple Pump — off-grid well pump maintenance: [simplepump.com/off-grid](https://www.simplepump.com/off-grid)
7. InspectAPedia — Water pump and tank repair manuals: [inspectapedia.com](https://inspectapedia.com/water/Water-Pump-Repair-Manuals.php)
8. Village Earth Appropriate Technology Library — 1,050 books on self-reliance technologies: [villageearth.org](https://villageearth.org/home/appropriate-technology-library/)
9. John Deere Right to Repair — PIRG resource: [pirg.org/resources/john-deere-and-right-to-repair-over-the-years](https://pirg.org/resources/john-deere-and-right-to-repair-over-the-years/)
10. John Deere $99M settlement (April 2026) — Farm Policy News: [farmpolicynews.illinois.edu](https://farmpolicynews.illinois.edu/2026/04/deere-settles-class-action-right-to-repair-lawsuit/)
11. National Agricultural Law Center — Right to Repair update: [nationalaglawcenter.org](https://nationalaglawcenter.org/update-on-right-to-repair/)
12. Whole Earth Catalog archive — appropriate technology reference: [wholeearth.info](https://wholeearth.info/)

### Scope Estimate

| Component | Hours |
|---|---|
| Research (equipment-specific manuals, NREL data, iFixit protocols) | 5–7 |
| Document A: Community repair infrastructure | 4–5 |
| Document B: Equipment-by-equipment protocols | 5–7 |
| Zone 5 specifics, cross-references | 1–2 |
| **Total** | **15–21 hours** |

**Output**: 2 deep-dive documents, ~7,000–9,000 words each, 30–40 combined citations

---

## Phase 4 Roadmap

### Recommended Sequencing

**Recommended order: Technology Repair → Agricultural Intensification → Education/Knowledge → Governance**

Rationale:

1. **Technology Repair first**: Equipment failure is the most immediate practical gap in Phase 1-3. If a solar system or well pump fails, Phase 1-3 cannot execute. Equipment-by-equipment maintenance protocols require no new social infrastructure and can be used immediately by individual practitioners. This is the highest-value addition with the least dependency on other Phase 4 content.

2. **Agricultural Intensification second**: Perennial systems and seed saving build on Phase 1's individual agriculture document and Phase 2's food coordination. The perennial food forest design document connects directly to the Zone 5 Midwest calendar and individual/06-agriculture.md already written. Seed saving is the hardest topic to catch up on after a disruption begins — it requires at least one full growing season of lead time.

3. **Education/Knowledge third**: Depends on community having survived long enough (2+ years of disruption) to need systematic knowledge preservation. Also depends on having the physical infrastructure (Raspberry Pi server, printed manuals) that Technology Repair helps maintain. High value but not time-urgent in the way equipment maintenance and food production are.

4. **Governance last**: Governance scaling is genuinely Phase 5 territory for most communities — it becomes urgent only after a multi-year disruption or when adjacent communities must formally coordinate. The Phase 3 mutual aid networks and emergency response infrastructure provide enough governance infrastructure for 0–24 months of disruption. Governance scaling extends this to 2-5+ years.

**Alternative sequencing if Anya wants a single-topic Phase 4**:

- If only one document: **Agricultural Intensification** — most actionable now, builds on what's already planted
- If only two documents: **Agricultural Intensification + Technology Repair**

### Dependencies Between Topics

```
Phase 3 (complete)
    ↓
Technology Repair ──────────────────→ enables all Phase 4 topics
    ↓
Agricultural Intensification ────→ requires working equipment + Phase 1 agriculture
    ↓
Education/Knowledge ─────────────→ requires stable community + working offline infrastructure
    ↓
Governance Scaling ──────────────→ requires stable community + 2+ years experience
```

### Timeline

**Assuming Phase 1-3 are deployed and in use**:

| Period | Work |
|---|---|
| June 2026 | Phase 4 launch — Technology Repair Documents A+B (15-21 hours) |
| July 2026 | Agricultural Intensification Documents A+B (15-22 hours) |
| August 2026 (optional) | Education/Knowledge Preservation (13-19 hours) |
| September 2026 (optional) | Governance Scaling (12-17 hours) |

This is a reasonable 4-month expansion if the full Phase 4 scope is approved. A minimal 2-topic Phase 4 (Technology Repair + Agricultural Intensification) could be complete by end of July 2026.

### Total Resource Estimate

| Topic | Hours Range | Documents | Words |
|---|---|---|---|
| Technology Repair | 15–21 | 2 | ~16,000 |
| Agricultural Intensification | 15–22 | 2 | ~18,000 |
| Education/Knowledge | 13–19 | 1 | ~9,000 |
| Governance Scaling | 12–17 | 1 | ~9,000 |
| **Phase 4 Total** | **55–79 hours** | **6 docs** | **~52,000 words** |

Compare: Phase 3 totaled ~40,000 words across 4 documents + overview.

### Success Criteria Per Topic

**Technology Repair**:
- [ ] Community repair inventory checklist completed for all critical equipment categories
- [ ] Offline repair manual library assembled (iFixit guides + equipment manuals printed and filed)
- [ ] At least 2 people per equipment category trained on maintenance procedures
- [ ] Community tool library governance document written and adopted

**Agricultural Intensification**:
- [ ] Food forest design completed for 1-5 acre community plot (species selection, spacing, layout)
- [ ] Perennial planting begun (even if 3-5 years from full production)
- [ ] Community seed library established (50+ varieties, physical catalog, governance rules)
- [ ] Annual seed-saving practiced for at least 5 staple crops

**Education/Knowledge**:
- [ ] Community Knowledge Audit completed (skills census, documented gaps, single points of failure identified)
- [ ] Kiwix server operational on Raspberry Pi with appropriate ZIM files loaded
- [ ] 3 copies of core reference library in geographically distributed locations
- [ ] Learning pod structure established for school-age children (even if informal)

**Governance Scaling**:
- [ ] Inter-municipal agreements (IMAs) signed with 2+ neighboring communities
- [ ] Regional council structure defined (representation, quorum, decision authority)
- [ ] Rationing protocol documented and tested (tabletop exercise)
- [ ] Conflict resolution mediator(s) identified and trained

---

## Scope Validation

### How Each Topic Connects to Phase 1-3

| Phase 4 Topic | Phase 1 Cross-Reference | Phase 2 Cross-Reference | Phase 3 Cross-Reference |
|---|---|---|---|
| Technology Repair | 04-energy.md (solar system basics); 01-water.md (pump systems) | 04-energy-coordination.md (household solar); 02-water-coordination.md (well/cistern) | 02-infrastructure-interdependency.md (cascade from equipment failure) |
| Agricultural Intensification | 06-agriculture.md (soil principles, Three Sisters); 02-food.md (garden sizing) | 03-food-coordination.md (food preservation hub) | 03-mutual-aid-networks.md (labor sharing, crop exchange) |
| Education/Knowledge | 05-healthcare.md (medical reference without professionals) | 01-household-coordination-overview.md (skill documentation) | 03-mutual-aid-networks.md (skills census) |
| Governance Scaling | (individual governance not covered) | 01-household-coordination-overview.md (household charter) | 01-emergency-response-infrastructure.md (ICS, emergency council) |

All four Phase 4 topics are natural extensions of existing Phase 1-3 content, not new subject areas. They deepen or scale content that is already present.

### Gaps Between Phase 3 and Phase 4

Three gaps are visible in the current Phase 1-3 content:

**Gap 1: Equipment Maintenance Is Assumed, Not Taught**
Phase 1-3 documents assume equipment works. Solar panels, hand pumps, generators, and radios are referenced but maintenance and repair procedures are not documented. This is the most critical gap — a solar panel that fails in Year 2 of a disruption cannot be replaced through normal supply chains.

**Gap 2: Food Production Is Annual-Garden-Scale**
Phase 1 covers a 400 sq ft garden (individual). Phase 2 covers coordinated household production. Neither addresses the 5-10 year horizon of perennial food systems or the community-scale production needed to feed 50-150 people without external food supply chains. Seed saving is referenced in Phase 1's agriculture document but not developed into a community practice.

**Gap 3: Knowledge Is Assumed to Persist**
Phase 1-3 assume that practitioners can read, do arithmetic, and access technical information when needed. None of the documents address what happens when this assumption fails — when the Kiwix server runs out of power, printed manuals are lost, and the person who knew how to run the water treatment system dies. Knowledge preservation is the most under-addressed risk in the current content.

Governance scaling is less a gap than a natural extension — Phase 3's governance framework works at 150 people; Phase 4 governance scales to 500+.

### What Phase 5 Would Look Like

Phase 5 would address true long-term civilizational continuity (5+ year horizon, potentially permanent infrastructure failure):

- **Metalworking and Manufacturing**: blacksmithing, foundry work, basic machine tools; producing replacement parts from raw materials
- **Medical System Continuity**: training paramedical practitioners to handle conditions currently requiring specialist care (surgery, obstetrics, dentistry); herbal medicine as partial substitute for pharmaceutical supply chains
- **Communication Infrastructure**: building and maintaining long-range radio networks (amateur radio mesh networks, Winlink, digital modes); point-to-point communication between distant communities
- **Economic Institutions**: designing formal community economic systems (local currency, land tenure, labor contracts) that function without federal banking or property law enforcement
- **Regional Federation**: governance frameworks for 2,000–10,000 people (county-level coordination); formal constitutions and legal frameworks

Phase 5 is genuinely speculative territory — most communities will not need it. It is appropriate only if disruption extends beyond 5 years or if planning for the most extreme failure scenarios.

---

## Decision Framework for Anya

### Option A: Full Phase 4 (All Four Topics)

**When to choose**: When Phase 1-3 are actively in use by a community and practitioners are asking for next-layer content. When a 2+ year disruption scenario is actively being planned for.

**Time commitment**: 55–79 hours of research and writing, 4-5 months (June–October 2026)  
**Output**: 6 documents, ~52,000 words

### Option B: Minimal Phase 4 (Technology Repair Only)

**When to choose**: When the highest-value addition is actionable immediately and Phase 4 budget is limited. Technology Repair addresses the most critical unaddressed practical gap.

**Time commitment**: 15–21 hours, 1 month (June 2026)  
**Output**: 2 documents, ~16,000 words

### Option C: Agricultural Intensification + Technology Repair

**When to choose**: When Phase 1-3 users are asking about long-term food production and equipment maintenance. These two topics have the most direct continuity from Phase 1-3 content.

**Time commitment**: 30–43 hours, 2 months (June–July 2026)  
**Output**: 4 documents, ~34,000 words

### Option D: Defer Phase 4

**When to choose**: When Phase 1-3 are not yet in active use by a community, or when other projects have higher priority. Phase 1-3 are sufficient for 0–24 month disruption response and represent a complete, defensible knowledge base.

**Recommendation**: If Phase 1-3 are being actively implemented and community practitioners are asking "what comes next?", start with Option B (Technology Repair) in June 2026. It is the highest-value, lowest-dependency addition and takes only 1 month. If that goes well and demand continues, add Agricultural Intensification in July 2026, reaching Option C by end of July.

---

## Summary Table

| Topic | Documents | Hours | Priority | Dependency |
|---|---|---|---|---|
| Technology Repair | 2 | 15–21 | **1st** | Phase 1-3 only |
| Agricultural Intensification | 2 | 15–22 | **2nd** | Phase 1-3 + Technology Repair |
| Education/Knowledge | 1 | 13–19 | **3rd** | Phase 1-3 + Technology Repair |
| Governance Scaling | 1 | 12–17 | **4th** | Phase 1-3 complete + 2yr experience |
| **Phase 4 Total** | **6** | **55–79** | | |

---

*Scoping document prepared May 17, 2026. All sources verified as of that date. Research depth is preliminary — production documents would require an additional research pass per topic.*
