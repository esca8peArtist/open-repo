---
title: "Household Network Coordination — Overview"
scale: household
region: "Midwest US (Zone 5)"
tracks: "Rural + Suburban"
word_count: ~6800
citation_count: 38
created: 2026-05-17
cross_references:
  - individual/01-water.md
  - individual/02-food.md
  - individual/03-shelter.md
  - individual/04-energy.md
  - individual/05-healthcare.md
  - individual/06-agriculture.md
---

# Household Network Coordination — Overview
> **Region**: Midwest US (Zone 5) | **Tracks**: Rural + Suburban
> **Scale**: 2–5 households, 8–20 people, shared property or adjacent parcels
> **Cross-references**: [individual/01-water.md](../individual/01-water.md) · [individual/02-food.md](../individual/02-food.md) · [individual/04-energy.md](../individual/04-energy.md) · [individual/05-healthcare.md](../individual/05-healthcare.md)

---

## The Most Important Finding

A single-household resilience system has a single point of failure at every node — one pump, one generator, one person who knows where the filters are. A 3-household cluster with distributed responsibilities and shared critical equipment tolerates the simultaneous failure of *two* of those nodes before the third household is in danger. The coordination overhead is real but bounded: a cluster of 3 households requires roughly 4–6 hours of shared governance work per month, and the capital savings on pooled equipment alone typically exceed $8,000–$20,000 compared to each household building identical redundant systems.

This document covers *how to coordinate* rather than what individual households need. It assumes readers have built or are building individual-scale competencies from the `individual/` documents first. Coordination improves resilience; it does not substitute for individual capability.

---

## Quick Reference Card
*(Print and share with all cluster households)*

**Reference scenario used throughout this document**: 3 households, 12 people total, 5 acres accessible across adjacent rural parcels, 60 miles from the nearest urban center, Zone 5 Midwest.

### Cluster Composition — Three Complementary Household Types

| Household Type | What They Provide | What They Need from Others | Key Equipment |
|---|---|---|---|
| **Infrastructure household** | Well, generator, electrical knowledge | Labor, food processing help, medical depth | Electric well pump, 7kW generator, hand pump |
| **Storage household** | Root cellar, bulk storage capacity, cool dark space | Energy for refrigeration, pump access | 500-bu root cellar, chest freezers, grain bins |
| **Labor household** | Physical capacity, time flexibility, animal husbandry | Infrastructure access, storage space | Small livestock, tools, garden equipment |

No real household maps perfectly onto one type. The table identifies *comparative advantages* that determine who manages which domain.

### Why Coordination Beats Isolation

| Scenario | Single Household Result | 3-Household Cluster Result |
|---|---|---|
| Well pump fails | No water until repaired (1–7 days) | Neighbors supply water within hours; repair is unhurried |
| Generator fails in winter | No backup power; heat at risk | One household's generator covers critical loads for all three |
| Primary farmer injured | Food production halts 2–4 weeks | Other households cover field tasks; injured household recovers |
| Medical crisis | Family manages alone; may evacuate | Neighbors cover water, food, energy so patient household can focus |
| One household must leave | All resilience capacity lost | Network continues; two households remain functional |

---

## Section 1: Governance and Decision-Making

### Why Governance Comes First

Every resource-sharing failure between neighbors traces back to governance, not resources. Two households sharing a generator with no written protocol will fight over it the first time one family wants to run power tools during the other's sleeping hours. Governance agreements written *before* crises are worth ten times more than ones negotiated during them.

### Four Governance Models for Small Clusters

**1. Informal consensus (2–3 households, existing friends or family)**
All major decisions require agreement from all households. Works when relationships are strong and decisions are infrequent. Fails when households disagree about resource priorities under stress. Supplement with a written one-page agreement on the three most contested domains: energy allocation, food storage access, and emergency response authority.

**2. Domain-specialist authority (3–5 households)**
Each household owns decision-making for one domain — one household manages the water system, one manages energy, one manages food production. Day-to-day decisions within a domain are made by the responsible household; inter-domain decisions require brief consensus. This is the recommended model for 3-household clusters. It mirrors how the Foundation for Intentional Community describes effective distributed authority in small communities. [1]

**3. Rotating leadership (3–5 households)**
One household is "lead" for a 3-month rotation, coordinates meetings, tracks shared inventory, makes tie-breaking calls. Distributes burden, ensures no single household dominates. Best for clusters where no household has clear domain expertise.

**4. Sociocratic consent (4–6 households)**
Formal sociocracy replaces "does everyone agree?" with "does anyone have a reasoned objection?" Proposals move forward if no one objects. Well-documented among larger intentional communities [2]; overkill for a 3-household cluster but valuable at 5+.

**Recommendation for most rural clusters**: domain-specialist authority with a one-page written agreement. Review annually.

### What Agreements to Document

A minimal written agreement for a 3-household cluster covers:

1. **Shared asset list**: what equipment is jointly owned or access-shared, replacement cost, who maintains it
2. **Access rules**: how does a household request use of shared equipment? Is there a notice requirement?
3. **Emergency authority**: who can make decisions without consensus in an emergency? (Define "emergency" explicitly — typically: imminent threat to life or shared asset within 24 hours)
4. **Labor exchange baseline**: expected hours per month each household contributes to cluster maintenance tasks
5. **Exit terms**: if one household leaves, how are jointly owned assets handled?
6. **Dispute process**: first step is direct conversation; second step is a cluster meeting; third step is written arbitration with a neutral third party

A simple MOU template from LegalZoom, PandaDoc, or legaltemplates.net can be adapted for this purpose in under two hours. [3] These are not legally binding in the contract sense but create accountability and shared memory.

### Legal Structures Worth Knowing

| Structure | Best For | Cost to Form | Complexity |
|---|---|---|---|
| Verbal agreement | 2 households, family | $0 | Minimal; fragile |
| Written MOU | 2–5 households | $0–$200 | Low; no enforcement |
| Agricultural cooperative | Shared land ownership, crop sales | $500–$2,000 state filing | Medium; formal governance required |
| LLC (member-managed) | Shared assets with formal ownership, liability protection | $100–$500 state filing | Medium; annual maintenance |
| Land trust | Long-term shared land stewardship | $1,000–$5,000 setup | High; permanent structure |

For most informal neighbor clusters: a written MOU with annual review. For clusters acquiring shared land or equipment valued above $10,000: an agricultural cooperative or LLC is worth the setup cost. Dancing Rabbit Ecovillage, which achieves per-capita resource use under 10% of average Americans, uses a land trust as its foundation precisely because permanent shared stewardship requires permanent legal structure. [4]

---

## Section 2: Resource Pooling Economics

### The Pooling Decision Framework

Not every resource improves with pooling. The test is three questions:

1. **Is the resource used intermittently?** A grain mill runs 2–3 times per year. Sharing three households' mill needs on one unit works. A water filter runs daily — each household needs their own.
2. **Is there a meaningful cost reduction?** A 1,000-gallon propane tank shared by 3 households costs $833/household vs. $1,500 each for three 500-gallon tanks. [5] A generator shared by 3 households costs $1,667/household vs. $5,000 each.
3. **Does the failure mode affect all households?** If the shared grain mill breaks, it's an inconvenience. If the shared well pump breaks, it's an emergency. Shared critical systems need backup redundancy already built in.

### Pooling vs. Individual — Master Decision Table

| Resource | Pool? | Why | Individual Cost | Shared Cost (÷3) | Savings |
|---|---|---|---|---|---|
| Backup generator (7kW) | Yes | Intermittent use; 1 per cluster sufficient | $5,000 each = $15,000 | $5,000 total = $1,667/hh | $10,000 |
| Solar array + batteries | Partial | Shared generation but individual allocation caps | $8,000/hh = $24,000 | $15,000 total = $5,000/hh | $9,000 |
| 1,000-gal propane tank | Yes | Volume discounts 15–30%; fewer deliveries | $1,500/500-gal = $4,500 | $2,500 = $833/hh | $2,000 |
| Root cellar (large) | Yes | One large cellar cheaper than 3 small | $3,000/hh = $9,000 | $4,000 total = $1,333/hh | $5,000 |
| Grain mill | Yes | Used 2–6x/year | $800 each = $2,400 | $800 total = $267/hh | $1,600 |
| Pressure canner (large) | Yes | Harvest season only; scheduling works | $500 each = $1,500 | $500 total = $167/hh | $1,000 |
| Chest freezer (large) | Partial | 1 shared + 1 per household for privacy | $400 each = $1,200 | $400 + backup = flexible | Variable |
| Food storage (dry goods) | No | Resilience requires independent supply | Individual | Individual | — |
| Medications | No | Personal, privacy, independent access essential | Individual | Individual | — |
| Water hand pump | No | Each household must be independently functional | $500–$1,500 each | Same | — |
| Seed vault (heirloom) | Yes | Genetic diversity improves with larger collection; lower per-household cost | $400 each = $1,200 | $400 total = $133/hh | $800 |
| Processing equipment (dehydrator, press) | Yes | Seasonal peak use; can schedule | $300 each = $900 | $400 total = $133/hh | $500 |
| Medical reference library | Yes | One set sufficient; no wear | $200 each = $600 | $200 total = $67/hh | $400 |
| Ham radio base station | Yes | One capable base serves cluster | $600–$1,500 each | $800 total = $267/hh | $900 |

**Total estimated savings from pooling on a 3-household cluster: $31,200 vs. fully independent systems.**

The "No" items are not negotiable. Individual food storage, individual medication supply, and individual hand pumps are the foundation from which coordination is built. If a household's participation in the cluster becomes unavailable — due to conflict, departure, or incapacity — each household must be able to function independently for a minimum of 30 days.

---

## Section 3: Coordinated Water Systems

*Building on [individual/01-water.md](../individual/01-water.md)*

### Baseline: What Each Household Needs Independently

Before coordinating, each household must have:
- Functional water source (well, spring, or reliable surface water with treatment)
- 14-day independent water storage (minimum 1 gal/person/day)
- Hand pump or gravity-fed backup if on electric well

### Cluster Architecture: 3-Well + Shared Storage

**Distributed wells**: 3 wells on 3 properties means the cluster tolerates 2 simultaneous well failures before anyone is at risk. Contrast this with a single shared well where 1 failure affects all 12 people. The cost of a drilled residential well in the Midwest runs $3,000–$9,000 depending on depth, averaging around $5,500 for a 150-foot well at $30–$45/foot. [6] Three individual wells cost roughly $16,500 total — but each household was going to need their own well anyway. The coordination value is in maintenance and backup, not in buying fewer wells.

**Hand pumps**: Every well in the cluster must have a manually operable pump. The Simple Pump (simple-pump.com) installs inside a standard well casing alongside an electric pump; full manual operation at any depth up to 350 feet costs $1,100–$1,500 installed. [7] This is a non-negotiable individual investment — do not count on neighbors' wells during a failure because their wells may be the ones that have failed.

**Shared above-ground storage tank**: A 500-gallon polyethylene tank ($400–$600) mounted 10–12 feet off the ground provides gravity-fed pressure to all three households via shared supply lines. The tank is filled by whichever household's well is currently operational. In a normal situation, the infrastructure household's electric pump fills it; in a failure scenario, any household's hand pump can manually fill it through a garden hose. Governance question for water: which household owns maintenance responsibility for the shared tank, supply lines, and fittings? Assign it explicitly.

**Shared filtration station**: One quality ceramic + activated carbon countertop filter (Berkey Big Berkey, $350–$450) and one UV pen (SteriPen, $50–$80) shared among households for treating uncertain surface water during extended failures. Each household still maintains individual backup filtration (Sawyer Squeeze per individual/01-water.md). The cluster's shared filter handles higher-volume processing needs (canning water, bathing, animals) more efficiently.

**Failure mode protocol — water:**
- *One well fails*: Other two households supply water to affected household via shared tank. Timeline: restored within 2 hours.
- *Shared tank fails (crack, contamination)*: Households revert to individual hand pump + individual 14-day storage. Cluster water coordination suspended until tank is repaired/replaced.
- *Water-responsible household member becomes unavailable*: Cluster must identify backup maintainer in advance (not during crisis). Include this in governance agreement.

**Water coordination economics:**

| System | Individual (3 households) | Cluster |
|---|---|---|
| Three wells | $16,500 (each household's own) | $16,500 (same; wells remain individual) |
| Shared 500-gal tank + lines | — | $800 |
| Three individual 300-gal tanks | $1,200 | — |
| Net saving | — | $400 |
| Real value | 0 failure tolerance | 2-failure tolerance |

The savings on water are modest; the resilience gain is substantial.

---

## Section 4: Coordinated Food Systems

*Building on [individual/02-food.md](../individual/02-food.md)*

### Individual Baseline

Each household should produce and store 3–6 months of food independently before attempting coordination. Coordination then extends capacity and reduces labor per calorie — it does not replace independent capacity.

### Cluster Food Architecture: Integrated 3-Acre Farm

**Land distribution**: On 5 shared or adjacent acres, 3 acres go into integrated food production:
- 1 acre corn/beans/squash (Three Sisters, labor-intensive at planting and harvest, lighter in between)
- 0.5 acre potatoes and sweet potatoes
- 0.5 acre market garden (vegetables, herbs)
- 0.5 acre fruit/nut perennials (initial labor-heavy, largely self-sustaining after year 3)
- 0.5 acre forage crops for animals if any household keeps livestock

At estimated Zone 5 yields, this 3-acre integrated system can produce 18,000–24,000 lbs of food per year — enough for 10–14 adults at 2,000 calories/day with appropriate preservation. [8] The individual/02-food.md document covers 1-person 1-acre production; the cluster achieves economies of both labor and inputs.

**Labor coordination**: Each household commits a defined number of hours per week during growing season (typically 10–15 hours/household/week during peak, 3–5 hours during off-peak). A rotating coordination calendar prevents conflict over who tends what:

| Task | Timing | Responsible Household | Labor Hours |
|---|---|---|---|
| Spring soil prep | April | Labor household | 20 hours |
| Planting corn/beans | May | Rotating | 12 hours |
| Garden weeding | June–August | Rotating weekly | 6 hours/week |
| Hay cutting (if applicable) | June–July | Infrastructure household (tractor) | 8 hours |
| Harvest coordination | August–October | All households | 30–60 hours/household |
| Canning/preserving | August–October | Storage household primary | 40 hours/household |
| Root cellar management | October–April | Storage household | 2 hours/month |

**Shared processing equipment:**
- One 23-quart All American pressure canner ($350–$450): handles 7 quarts at a time; cluster processes 200–300 quarts per harvest season; 3 households scheduling use on alternating days eliminates bottleneck
- Country Living or WonderMill grain mill ($400–$600): runs 2–4 times per year for cornmeal and wheat flour; shared easily
- Commercial-grade food dehydrator (Excalibur 9-tray, $350–$500): handles cluster's herb, tomato, and fruit drying needs in 3–4 seasonal runs
- Shared chest freezer (20 cu ft, $400–$600): cluster overflow freezer in storage household's root cellar area, separate from individual household freezers

**Seed banking**: One shared seed vault stored in the storage household's root cellar covers all three households' seed diversity. Guidelines:
- Each household contributes 50% of its seed saving to the shared vault (keeping 50% individually for redundancy)
- Shared vault rotates fresh seeds every 2–4 years by planting test rows
- Heirloom open-pollinated varieties only (no hybrids — seeds must be true-to-type for vault to have value)
- Target: 40–60 distinct varieties covering all major food categories (alliums, brassicas, legumes, grains, roots, fruiting vegetables)
- Commercial cost comparison: a curated 50-variety heirloom collection runs $200–$400 from reputable seed companies such as Baker Creek, Seed Savers Exchange, or Southern Exposure Seed Exchange [9]; the cluster's shared vault provides better genetic diversity through broader selection

**Animal coordination**: Livestock sharing is possible but requires the most detailed governance. Two households sharing a small goat herd (3–5 does):
- Milking schedule: morning milking rotates by week (each household milks every other week at a minimum)
- Veterinary costs: split equally unless an animal is injured by a specific household's equipment
- Exit clause: if one household wants out of the arrangement, a 90-day transition period lets the remaining household absorb or rehome animals
- The labor household is the natural owner of any shared livestock given their time availability; other households contribute feed costs and veterinary fund contributions

**Food cooperative structure**: The cooperative farming literature (Civil Eats, Cooperative Development Institute) consistently shows that small agricultural cooperatives survive difficult years better than individual farms because the financial and labor risk is distributed. [10] A bad crop year on a single household can be a crisis; across three households with different plantings and different microclimates on their 5 acres, at least partial harvest is almost always available.

---

## Section 5: Coordinated Energy Systems

*Building on [individual/04-energy.md](../individual/04-energy.md)*

### Individual Baseline

Each household should have at minimum a small standalone solar system (200–400W panels, 5–10 kWh battery) before cluster-scale energy coordination makes sense. Individual systems provide independence; cluster coordination provides backup and peak-demand capacity.

### Cluster Energy Architecture: Shared Generation + Individual Allocation

**Shared solar array**: A 2.5–4 kW array mounted on the most favorable south-facing roof or ground mount, feeding a shared 20–30 kWh lithium battery bank, provides primary generation for the cluster's shared loads (well pump, shared freezer, ham radio base). Each household retains their individual smaller system for private loads. This matches the model of community solar aggregation documented by NREL, adapted to a residential scale. [11]

**Load allocation**: Each household draws a defined maximum per day from the shared system (6–8 kWh/household, depending on system size and season). Overages default to the household's own individual battery. Priority hierarchy is documented in the governance agreement:

1. Medical equipment (CPAP, insulin refrigeration, powered mobility)
2. Shared well pump and pressure system
3. Shared freezer and refrigeration
4. Communications (ham radio, phone charging)
5. Lighting
6. Tools and processing equipment

**Metering between households**: A simple energy monitor (Emporia Energy, $20–$40/monitor) on each household's circuit from the shared bank tracks consumption. Monthly settlements are simple: households exceeding allocation by more than 5 kWh/month contribute proportionally to the next fuel/propane purchase or invest in the next battery expansion.

**Shared backup generator**: One 7kW diesel or dual-fuel generator ($3,000–$5,000) serves the cluster. Its primary role is not daily operation — it is the emergency backup when solar generation falls below 30% of normal for 3+ consecutive days (common in Midwest December–January). Weekly test runs (15 minutes) confirm operability. Fuel: 200-gallon diesel storage in the infrastructure household's outbuilding, rotated annually with a fuel stabilizer treatment.

**Propane pooling**: A 1,000-gallon above-ground propane tank ($2,500 purchase price plus $500 installation) replaces three individual 500-gallon tanks ($1,500 each = $4,500 total). [12] Beyond the $2,000 upfront savings, route-day bulk deliveries at a shared location qualify for $0.10–$0.25/gallon discount over individual small deliveries; at 1,500 gallons per year cluster-wide consumption, savings are $150–$375/year. [13] The tank is on the storage or infrastructure household's property; a recorded easement agreement grants all households access rights.

**Energy failure modes:**
- *Solar generation drops below 20%*: Activate generator for 4–6 hours/day, prioritizing shared battery charge. Reduce all non-critical loads.
- *Shared battery fails*: Households fall back to individual systems; shared loads (well pump, freezer) temporarily shift to individual coverage on rotation.
- *Generator fails in winter*: Trigger emergency governance protocol. Households consolidate — moving critical loads and people to the most shelter-efficient building if prolonged failure. Propane heaters (Mr. Heater Big Buddy, 18,000 BTU, $130) serve as non-electric thermal backup in each household.

**Cluster energy economics:**

| System | Individual (3 households) | Cluster |
|---|---|---|
| Solar + batteries | $8,000/hh = $24,000 | $15,000 shared + $4,000/hh individual = $27,000 |
| Generator | $5,000 each = $15,000 | $5,000 shared = $1,667/hh |
| Propane tank | $1,500 each = $4,500 | $3,000 shared = $1,000/hh |
| Total | $43,500 | $35,000 |
| Net savings | — | $8,500 |

---

## Section 6: Coordinated Healthcare

*Building on [individual/05-healthcare.md](../individual/05-healthcare.md)*

### Individual Baseline

Each household must maintain its own first-aid supply, its own 6-month medication stockpile, and basic wound care capability before cluster health coordination adds value.

### Cluster Health Architecture: Skill Distribution + Shared Specialty Supplies

The critical insight from healthcare coordination is that skills distribute better than supplies. Each cluster household should specialize and cross-train:

**Skill distribution target:**
- *Household A (infrastructure)*: Field medicine/trauma — tourniquet application, wound closure, fracture management; cross-trains others quarterly
- *Household B (storage)*: Herbal and chronic care — extended care for non-acute conditions, herbal remedies, nutritional support during illness; cross-trains others semi-annually
- *Household C (labor)*: Obstetric awareness and pediatric basics — childbirth support, infant care, pediatric fever and illness management

No household specializes exclusively — each maintains basic competency in all domains. The specialization means each cluster has at least one person with deep knowledge in each area, not that non-specialists are helpless.

**Shared specialty supplies** (stored at storage household's root cellar in a dedicated waterproof container):
- Emergency dental kit: oil of cloves, temporary filling material, dental picks, mirror — covers dental pain management when professional care is unavailable
- Suture and staple kit with practice materials (skill training, not emergency deployment)
- Otoscope and blood pressure cuff (one cluster set sufficient)
- Pulse oximeter (one cluster set)
- Ophthalmoscope (basic; for assessing serious eye injuries)
- Medical reference library: Wilderness Medicine by Auerbach (5th edition), Where There Is No Doctor by Werner, Merck Manual Home Edition, The Herbal Medicine-Maker's Handbook

Each household maintains individual first-aid supplies for daily use. The shared specialty cache is for situations requiring equipment beyond individual capability.

**Crisis support protocol**: When one household has a health crisis:
- Other households cover that household's shared responsibilities (water, energy monitoring, animal care) for up to 4 weeks
- One designated cluster health liaison coordinates information about the patient's needs (with consent)
- Labor household provides meal delivery and physical assistance
- Transition back to normal rotation happens in 2-week increments as capacity allows

**Telemedicine coordination**: If any household has internet connectivity (satellite internet such as Starlink, or a cell signal amplifier), the cluster designates that connection as the medical communications link during crises. Shared power prioritizes that connection during low-generation periods.

---

## Section 7: Skill and Knowledge Distribution

The individual-scale documents assume one person learns everything. The cluster enables task division — one person learns water systems deeply, another learns herbal medicine, another learns structural repair. The key is cross-training so no single person's absence creates a knowledge gap.

### Cluster Skill Inventory Template

*(Fill out collaboratively in Month 1; update annually)*

| Skill Domain | Who Has It | Depth | Cross-Training Schedule |
|---|---|---|---|
| Water system maintenance | — | — | — |
| Electrical/solar troubleshooting | — | — | — |
| Vehicle/small engine repair | — | — | — |
| Food preservation (canning, fermenting) | — | — | — |
| Seed saving + plant identification | — | — | — |
| Animal care + veterinary basics | — | — | — |
| Construction + carpentry | — | — | — |
| Field medicine (trauma, wound care) | — | — | — |
| Herbal medicine + chronic care | — | — | — |
| Communications (ham radio, electronics) | — | — | — |

**Cross-training cadence**: One 2-hour session per month, rotating domain. At 12 domains across 12 months, every household has attended instruction in every domain within one year. Notes from each session go into the cluster's shared knowledge notebook.

**Knowledge capture**: One shared three-ring binder or waterproof notebook contains:
- System diagrams for every shared infrastructure element
- Contacts list (equipment suppliers, local well drillers, veterinarians, county extension agents)
- Maintenance schedules with completion logs
- Emergency protocols (one laminated page per scenario)

If the person who knows how to operate the shared grain mill moves away, the notebook's step-by-step operation guide fills the gap. This is not theoretical — intentional communities consistently cite undocumented knowledge as the primary cause of operational failures when key members leave. [14]

---

## Section 8: Communication and Coordination Logistics

### Regular Cadence

| Meeting Type | Frequency | Duration | Purpose |
|---|---|---|---|
| Cluster check-in | Weekly | 30 minutes | Status on shared systems; upcoming labor needs |
| Domain review | Monthly | 2 hours | Detailed review of one domain + skill training session |
| Full inventory review | Quarterly | 3–4 hours | Shared resource count, condition assessment, planning |
| Annual governance review | Annually | Half-day | Revise agreements, settle accounts, re-elect domain leads |

**Weekly check-in format**: Each household reports in 5 minutes: water system status, energy system status, any equipment or health issues, upcoming labor needs. One household chairs; rotating by month.

### Grid-Down Communication Protocol

When grid power and cellular networks fail, the cluster needs an independent communication system. The PACE framework (Primary, Alternate, Contingency, Emergency) applies: [15]

- **Primary**: GMRS radio network — one GMRS license ($35, covers entire immediate family for 10 years, FCC.gov) per household, handheld radios ($40–$80 each). Range: 1–5 miles line-of-sight in Midwest rural terrain. Pre-agreed check-in channel: GMRS Channel 15, 09:00 and 18:00 daily.
- **Alternate**: FRS walkie-talkie (license-free) for short-range (<0.5 mile) within the cluster. Every household has 2 units already.
- **Contingency**: Physical runner or vehicle. Pre-agreed meeting location (infrastructure household's main building) if radio contact fails for >12 hours.
- **Emergency**: Visible signal. A defined location (fence post, flagpole) where a specific flag or object signals "come to this property now." Each household assigns 1 person to check the signal point daily at dawn.

**Ham radio base station** (Baofeng UV-5R for mobile, $30–$40; Yaesu FT-991A for base, $700–$800): shared base station at infrastructure household provides broader regional monitoring (weather, emergency broadcasts) without each household investing in a full station. [16] At least one cluster member should obtain a Technician-class ham radio license (free exam prep at HamStudy.org; $15 exam fee).

### Information Management

**Shared resource inventory** (maintained by storage household monthly):
- Solar battery state of charge (morning reading)
- Propane level (dip stick reading monthly)
- Food storage quantity by category (quarterly)
- Water storage level (weekly)
- Generator fuel level (weekly)
- Shared equipment operational status

**Cluster communication log** (binder at infrastructure household): dates, topics, decisions made, labor exchanges completed. This is the cluster's institutional memory when individual recollections conflict.

---

## Section 9: Load Planning — Cluster Scale

### Individual vs. Cluster Electrical Load Comparison

| Load | Individual Household | 3-Household Cluster | Notes |
|---|---|---|---|
| Lighting | 40–60 Wh/day | 120–180 Wh/day | Linear scale |
| Phone/device charging | 20–40 Wh/day | 60–120 Wh/day | Linear scale |
| Well pump (shared) | 500–2,000 Wh/day | 500–2,000 Wh/day | Single shared pump; no scaling |
| Shared freezer | 1,000–1,500 Wh/day | 1,000–1,500 Wh/day | Single unit |
| Individual freezers | 500/hh/day | 1,500 Wh/day | 3 units |
| Communications | 10–20 Wh/day | 30–60 Wh/day | + base station 50 Wh/day |
| Processing equipment (seasonal) | 500 Wh/use | 500 Wh/use | Shared unit, same load |
| **Baseline cluster total** | **~1,100 Wh/day/hh** | **~5,000 Wh/day** | |

**Seasonal planning — Zone 5 Midwest:**

| Season | Solar Generation | Battery State | Strategy |
|---|---|---|---|
| Summer (Jun–Aug) | 5.5–6.5 peak hours | Charging surplus by noon | Run processing equipment mid-day; bank excess |
| Shoulder (Mar–May, Sep–Nov) | 3.5–5.0 peak hours | Balanced | Normal operation; monitor week-by-week |
| Winter (Dec–Feb) | 2.5–3.5 peak hours | Deficit likely | Generator 2–4 hrs/day; reduce non-critical loads |
| Canning season spike (Aug–Oct) | Peak solar | Battery full | Run pressure canner in clusters 10am–4pm for max solar; 6–8 kWh/day for 3–4 weeks |

**Load management triggers:**
- Battery below 40%: suspend all non-critical loads (processing equipment, entertainment, power tools)
- Battery below 25%: start generator for 4-hour charge cycle; prioritize well pump and freezer
- Battery below 15%: emergency protocol — generator runs continuously until 50% restored; cluster consolidates to most efficient building

---

## Section 10: Failure Modes and Recovery Scenarios

### Scenario A: Generator Failure, December, Mid-Winter Storm

**Conditions**: 3-household cluster, 5 days of heavy cloud cover forecast, shared generator fails to start. Temperature: 18°F overnight.

**Response timeline**:
- Hour 1: Infrastructure household attempts generator repair. Failure confirmed. Cluster radio check-in called.
- Hour 2: Cluster meeting. Shared battery at 60% (2 days of baseline load). Propane levels confirmed (400 gallons remaining = 3 months at normal rate). Decision: consolidate heating to storage household's building (best insulated); infrastructure and labor households move sleeping operations there.
- Day 1–3: All households maintain individual duties. Shared battery drops to 40% by Day 2. Load shedding: no power tools, no dehydrator, minimal lighting. Well pump 2x/day only.
- Day 3: Generator parts ordered from regional supplier (60 miles). Estimated 4-day delivery. Propane backup heaters active in infrastructure household's building for daytime work.
- Day 7: Generator repair complete. Normal operations resume. Cluster reviews: were propane reserves adequate? Was backup generator parts kit available? (Add to shared inventory.)

**Lesson**: A generator parts kit ($50–$150: fuel filter, air filter, spark plugs, starter rope, oil) stored at the infrastructure household eliminates 4 of the 7 days above.

### Scenario B: Water Well Failure, July, Canning Season

**Conditions**: Storage household's well pump burns out during peak canning season. 12 people, 3 acres of garden at peak production, canning operation running daily.

**Response timeline**:
- Day 1: Storage household reports pump failure at morning check-in. Infrastructure household's well pump begins supplying shared tank. Labor household's hand pump provides backup to storage household directly via garden hose (0.25 mile, gravity-assisted).
- Day 1–3: Normal operations continue. Shared tank is refilled from infrastructure household's pump twice daily. Storage household's canning continues on schedule.
- Day 4: Well driller contacted. Estimated $800–$1,200 for pump replacement. Cluster covers cost from shared maintenance fund (see governance agreement).
- Day 7: Pump replaced. Storage household's well restored. Shared tank returns to multi-source resupply.

**Lesson**: The cluster absorbed a significant equipment failure without interrupting the canning season — the single most important food production event of the year. An individual household would have faced a crisis during their busiest week.

### Scenario C: Month 5, Winter Approaching, Primary Coordinator Unavailable

**Conditions**: The person who manages the cluster's shared systems documentation (water, energy, food) is hospitalized unexpectedly. November. Winterization not yet complete.

**Response timeline**:
- Week 1: Cluster meets; shared notebook consulted. Winterization checklist is documented (Section 12 of this document). Tasks distributed: infrastructure household handles water system winterization; labor household handles propane and generator checks; storage household handles root cellar final stocking and inventory.
- Week 2: Winterization complete without the coordinator. Knowledge notebook proves its value — the well insulation specification, propane tank inspection protocol, and generator load-testing procedure are all documented.
- Month 2: Coordinator returns. Cluster operates normally.

**Lesson**: The shared knowledge notebook and documented protocols are the cluster's most important resilience investment after physical infrastructure. A cluster that depends on one person's memory is not resilient — it is fragile.

---

## Section 11: Midwest Seasonal Coordination Calendar

### Spring (March–May): Activation and Planting

**March:**
- Well inspection and pump check (infrastructure household)
- Seed vault review and selection for current season (storage household)
- Generator service (oil change, filter replacement, load test)
- Shared equipment audit (all households)

**April:**
- Soil preparation for 3-acre cluster farm (all households, labor-intensive)
- Water system de-winterization (infrastructure household leads)
- GMRS radio batteries checked and spare batteries charged

**May:**
- Corn, beans, squash planting (all households, coordinated scheduling)
- Root cellar cleaning and airing (storage household)
- Annual governance review if not completed in winter

### Summer (June–August): Production Peak

**June–July:**
- Market garden succession planting (rotating households)
- Hay cutting and storage if applicable (infrastructure household equipment)
- Processing equipment calibration (pressure canner test batch, dehydrator run)
- Shared freezer stocked with first harvest (storage household coordinates)

**August:**
- Canning season begins; shared equipment scheduling posted for cluster
- Seed saving from earliest varieties (storage household coordinates vault update)
- Propane delivery scheduled before fall price increase (typically August–September)

### Fall (September–November): Harvest and Winterization

**September–October:**
- Primary harvest coordination: all households provide labor for major crops
- Root cellar stocking target: 90-day supply for all 12 people by October 15
- Shared freezer stocked to 80% capacity
- Generator tested under full load before cold season

**November:**
- Water system winterization: insulate above-ground pipes, drain exposed lines, verify heat tape on well head
- Propane level check: minimum 300 gallons entering December (covers 3 months at 100 gal/month cluster average)
- Final skill-sharing session before winter's reduced mobility

### Winter (December–February): Maintenance and Planning

**December–February:**
- Weekly radio check-ins maintained even if in-person meetings difficult
- Monthly indoor cluster meeting for planning next year
- Equipment repair and maintenance (indoor work)
- Annual governance review and agreement renewal (January ideal)
- Seed catalog review; order placed by February 1

---

## Section 12: Start-Small Implementation Roadmap

Most readers are not starting with 3 like-minded households ready to sign agreements. The typical starting point is 1–2 households looking to begin coordination with existing neighbors. This roadmap is sequential; do not skip phases.

### Month 1: Identify and Establish Relationship

**Actions:**
1. Identify 1–2 neighboring households with geographic proximity (ideally <0.5 mile), willingness to talk, and some existing mutual goodwill
2. Open conversation framing: "I'm working on making our household more self-sufficient, and I realized some things work better with neighbors than alone. Would you be interested in talking about how we might help each other?"
3. Identify 2–3 immediate, low-stakes areas for coordination (not shared ownership — just communication): "If either of us needs to borrow a tool, we're welcome to ask" or "Let's exchange phone numbers and check in if there's severe weather."
4. Do not start with formal agreements. Start with relationship.

**Success metric**: At least one neighbor is actively interested in further conversation.

### Months 2–3: Low-Stakes Coordination

**Actions:**
1. Establish basic communication — exchange contact information, agree on a radio channel if any household has GMRS radios
2. Informal skill sharing: "I'm canning tomatoes this weekend, want to come watch?" or "I'm checking the well pump — want to see how it works?"
3. Identify one shared problem: "Neither of us has a grain mill, and we're both interested in grinding flour. Would you want to split the cost of one?"
4. Complete a simplified version of the cluster skill inventory — just a brief conversation about who knows what

**Success metric**: At least one informal coordination event has happened (shared activity, borrowed tool, joint purchase).

### Months 4–6: First Shared Investment

**Actions:**
1. Make first shared purchase — a grain mill, a pressure canner, or a GMRS radio for each household
2. Draft a simple one-page written agreement covering: who stores it, how to request use, how replacement costs are handled if it breaks
3. Establish monthly meeting (30–60 minutes; informal, at someone's kitchen table)
4. Complete a basic resource inventory for each household

**Success metric**: One jointly owned piece of equipment is in use and the ownership arrangement is working.

### Months 6–12: Expand Coordination

**Actions:**
1. Add domain-specialist assignments (each household takes lead responsibility for 1 domain)
2. Begin skill-sharing sessions (monthly, rotating domains)
3. Evaluate whether any capital investment makes sense (shared propane tank, shared generator, shared solar expansion)
4. Review and expand the one-page written agreement to cover new shared assets
5. Complete shared knowledge notebook structure (system diagrams, contacts, protocols)

**Success metric**: Each household has attended at least 3 skill-sharing sessions; each domain has a designated lead.

### Year 2+: Infrastructure Investment

**Actions:**
1. Major shared system investment (propane tank, solar expansion, shared storage tank)
2. Formalize governance — upgrade from MOU to cooperative or LLC if shared asset value exceeds $10,000
3. Consider expanding network to 4th or 5th household if relationship and geographic conditions allow
4. Conduct first full annual governance review, including financial accounting of labor and cost sharing

---

## Section 13: When to Scale to Community Level

### Signals That a 5-Household Cluster is Ready to Grow

At 5 households (roughly 20–30 people), informal coordination begins to strain. The signals are:
- Meetings take more than 2 hours consistently because too many people want to speak
- Decisions are appealed or relitigated after they are supposedly made
- One household consistently provides more labor than others without explicit acknowledgment
- New households want to join but the cluster has no process for adding members

At this point, governance needs formal structure: defined roles (coordinator, treasurer, secretary), financial accounting, and a membership process. This is the boundary between the household-scale model described in this document and the community-scale model that will be covered in `community/01-community-coordination-overview.md`.

### What Scales Well and What Does Not

**Scales well with more households:**
- Solar generation and storage (larger shared array serves more households at lower cost per household)
- Bulk purchasing (propane, seed, supplies)
- Skill depth (more people means more total specialized knowledge)
- Labor for large projects (barn raising, major harvest, infrastructure installation)

**Scales poorly with more households:**
- Informal consensus decision-making (beyond 5 households, someone always disagrees)
- Trust-based resource sharing without formal accounting
- Emergency coordination without a designated authority
- Individual-style communication (radio check-ins, binder logs) — needs dedicated coordination infrastructure

The household-scale model is optimized for 2–5 households. At 6+, use the community-scale governance model.

---

## Worksheets and Templates

### Worksheet A: Cluster Skill Inventory (Complete Month 1)

| Skill | Household A | Household B | Household C | Cross-Training Done? |
|---|---|---|---|---|
| Water system maintenance | | | | |
| Electrical/solar | | | | |
| Small engine repair | | | | |
| Food preservation (canning) | | | | |
| Food preservation (fermenting) | | | | |
| Seed saving | | | | |
| Animal care | | | | |
| Construction/carpentry | | | | |
| Trauma/wound care | | | | |
| Herbal/chronic care | | | | |
| Communications/electronics | | | | |
| Navigation/land management | | | | |

Rate each: 0 = no knowledge, 1 = basic awareness, 2 = functional competency, 3 = can teach others.

### Worksheet B: Shared Resource Inventory (Update Quarterly)

| Item | Location | Owner/Custodian | Condition | Last Serviced | Replacement Cost |
|---|---|---|---|---|---|
| Generator (7kW) | | | | | |
| Propane tank (1,000 gal) | | | | | |
| Shared water tank (500 gal) | | | | | |
| Pressure canner (23 qt) | | | | | |
| Grain mill | | | | | |
| Food dehydrator | | | | | |
| Chest freezer (shared) | | | | | |
| Ham radio base station | | | | | |
| GMRS radios (set) | | | | | |
| Medical specialty kit | | | | | |
| Seed vault | | | | | |
| Shared knowledge notebook | | | | | |

### Worksheet C: Coordination Schedule Template

| Week | Cluster Responsible | Energy Check | Water Check | Livestock (if any) | Notes |
|---|---|---|---|---|---|
| 1 | Household A | A | A | B | |
| 2 | Household B | B | B | C | |
| 3 | Household C | C | C | A | |
| 4 | Household A | A | A | B | |

### Worksheet D: Emergency Contact List (Laminated Copy Per Household)

| Role | Name | Contact | Backup Contact |
|---|---|---|---|
| Cluster coordinator | | | |
| Water system lead | | | |
| Energy system lead | | | |
| Medical lead | | | |
| Food/storage lead | | | |
| Nearest well driller | | | |
| Nearest propane supplier | | | |
| County extension agent | | | |
| Nearest veterinarian | | | |
| Nearest medical clinic | | | |

---

## Primary Sources and Citations

[1] Foundation for Intentional Community. "Governance for Healthy Communities." ic.org, May 2025. https://www.ic.org/governance-for-healthy-communities-5-2025/

[2] Sociocracy For All. "Sociocracy in Intentional Communities." sociocracyforall.org. https://www.sociocracyforall.org/community/

[3] PandaDoc. "Free Memorandum of Understanding Template 2026." pandadoc.com. https://www.pandadoc.com/memorandum-of-understanding-template/

[4] Litfin, Karen. "Achieving One-Planet Living Through Transitions in Social Practice: A Case Study of Dancing Rabbit Ecovillage." ResearchGate. https://www.researchgate.net/publication/306314471

[5] HomeGuide. "2026 Propane Tanks Costs: 100, 250 & 500 Gallon Tank Prices." homeguide.com. https://homeguide.com/costs/propane-tank-cost

[6] Angi/HomeAdvisor. "How Much Does Well Drilling Cost? [2026 Data]." angi.com. https://www.angi.com/articles/how-much-does-well-drilling-cost.htm

[7] Simple Pump Company. "Residential Hand Pump Systems." simple-pump.com. Pricing from manufacturer specifications, 2025.

[8] USDA NRCS. Crop yield data for Zone 5 Midwest — used for caloric yield estimates in 02-food.md; cluster values are direct extrapolation. nrcs.usda.gov.

[9] Seed Savers Exchange. "Heirloom Open-Pollinated Seed Collections." seedsavers.org. Pricing from 2025 catalog.

[10] Cooperative Development Institute. "The Co-op Farming Model Might Help Save America's Small Farms." cdi.coop. https://cdi.coop/the-co-op-farming-model-might-help-save-americas-small-farms/

[11] NREL. "Community Solar and Beyond." National Renewable Energy Laboratory, 2024. https://www.nrel.gov/solar/market-research-analysis/program/2024/community-solar-and-beyond

[12] Habitatista. "7 Ways to Save: Bulk Propane vs Retail Options." habitatista.com. https://www.habitatista.com/30758/7-ways-to-save-bulk-propane-vs-retail-options/

[13] Liquid Propane. "Propane Cost per Gallon: What American Homeowners Pay." liquidpropane.com. https://liquidpropane.com/propane-cost-per-gallon-what-american-homeowners-pay/

[14] Schiavelli, Maria, and Blake Gumprecht. "A Case Study Analysis of Dancing Rabbit Ecovillage." Communal Societies, Grand Valley State University, 2018. https://scholarworks.gvsu.edu/cgi/viewcontent.cgi?article=1213&context=communalsocieties

[15] Salt & Prepper. "Group Communications Protocols for Your MAG." saltandprepper.com. https://www.saltandprepper.com/learn/community/group-communications-protocols

[16] GMRS.io. "GMRS for Emergency Communication Guide." gmrs.io. https://www.gmrs.io/guide/emergency-communication

[17] FCC. "General Mobile Radio Service (GMRS)." fcc.gov. https://www.fcc.gov/wireless/bureau-divisions/mobility-division/general-mobile-radio-service-gmrs

[18] Canadian Preppers Network. "Building a 5-Family Mutual Aid Circle (Without Looking Crazy)." canadianpreppersnetwork.com. https://canadianpreppersnetwork.com/building-a-5-family-mutual-aid-circle-without-looking-crazy/

[19] AlwaysReadyHQ. "12 Community Skills Sharing Tips That Build Neighborhood Resilience." alwaysreadyhq.com. https://www.alwaysreadyhq.com/9434/community-skills-sharing-for-preparedness/

[20] NREL. "Resilience and Economics of Microgrids with PV, Battery Storage, and Diesel Generators." NREL Technical Report NREL/TP-5D00-78837, 2021. https://docs.nrel.gov/docs/fy21osti/78837.pdf

[21] NREL. "Technical Assistance Supports Microgrids in Remote Communities." NREL News, 2024. https://www.nrel.gov/news/detail/program/2024/technical-assistance-supports-microgrids-in-remote-communities

[22] Tanis, et al. "A Comprehensive Review on Peer-to-Peer Energy Trading: Market Structure, Operational Layers, Energy Cooperatives and Multi-Energy Systems." IET Renewable Power Generation, 2025. https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/rpg2.70075

[23] Wikipedia. "Community-Supported Agriculture." en.wikipedia.org. https://en.wikipedia.org/wiki/Community-supported_agriculture

[24] Local Futures. "The Radical Roots of Community Supported Agriculture." localfutures.org. https://www.localfutures.org/the-radical-roots-of-community-supported-agriculture/

[25] Global Ecovillage Network. "Why Dancing Rabbit Changed Its Governance." ecovillage.org. https://ecovillage.org/why-dancing-rabbit-changed-its-gover-2/

[26] Werner, David, Carol Thuman, and Jane Maxwell. Where There Is No Doctor. Hesperian Foundation, 2017. Free PDF: hesperian.org. Standard reference for community health workers.

[27] Auerbach, Paul S. Wilderness Medicine, 7th Edition. Elsevier, 2017. Standard field medicine reference.

[28] USDA Rural Development. "Rural Decentralized Water Systems Grant Program." rd.usda.gov. https://www.rd.usda.gov/programs-services/water-environmental-programs/rural-decentralized-water-systems-grant-program

[29] EPA. "USDA Water Grants and Loans Available to Water and Wastewater Utilities." epa.gov. https://www.epa.gov/fedfunds/usda-water-grants-and-loans-available-water-and-wastewater-utilities

[30] USDA Rural Development. "Funding Available for Drilling Household Water Wells." rd.usda.gov. https://www.rd.usda.gov/node/17042

[31] BPNews. "Community Tanks Benefit Both Residents and Propane Retailers." bpnews.com. https://bpnews.com/feature-articles/community-tanks-benefit-both-residents-and-propane-retailers

[32] AlwaysReadyHQ. "11 Strategies for Forming Local Mutual Aid Groups That Build Community Strength." alwaysreadyhq.com. https://www.alwaysreadyhq.com/9719/strategies-for-forming-local-mutual-aid-groups/

[33] Thunderbird Disco Homestead. "Mutual Aid: Community Preparedness and Neighborhood Resilience Networks." thunderbirddisco.com. https://www.thunderbirddisco.com/blog/mutual-aid-community-preparedness

[34] Shareable. "Key Choice-Points for Starting an Intentional Community." shareable.net. https://www.shareable.net/key-choice-points-for-starting-an-intentional-community/

[35] FarmstandApp. "7 Cooperative Farming Arrangements That Support Small Farmers." farmstandapp.com. https://www.farmstandapp.com/103911/7-options-for-cooperative-farming-arrangements/

[36] Common Ground Ecovillage. "Governance by Peers." commonground.eco. https://www.commonground.eco/governance-by-peers/

[37] ICMatch. "Guidelines: Governance of Intentional Community — Cooperative Living Communities." icmatch.org. https://icmatch.org/guidelines-for-intentional-community-agreements/governance-of-intentional-community/

[38] EcoFlow Blog. "How to Communicate If the Power Grid Goes Down." ecoflow.com. https://www.ecoflow.com/us/blog/power-outage-family-communication-guide

---

## Cross-References

- [individual/01-water.md](../individual/01-water.md) — individual water baseline, hand pump specifications, treatment procedures
- [individual/02-food.md](../individual/02-food.md) — individual food production baseline, caloric planning, seed saving
- [individual/03-shelter.md](../individual/03-shelter.md) — shelter hardening; relevant to cluster consolidation scenarios
- [individual/04-energy.md](../individual/04-energy.md) — individual solar sizing, load shedding framework
- [individual/05-healthcare.md](../individual/05-healthcare.md) — MARCH protocol, supply lists, medication stockpile
- [midwest/calendar.md](../midwest/calendar.md) — Zone 5 seasonal timing for all coordination activities
- [midwest/extreme-weather.md](../midwest/extreme-weather.md) — emergency protocols applicable during cluster crises
- *household/02-water-coordination.md* (forthcoming) — detailed cluster water system design and maintenance
- *household/03-food-coordination.md* (forthcoming) — cooperative farming protocols, labor scheduling, animal sharing
- *community/01-community-coordination-overview.md* (forthcoming) — scaling to 20–100 people
