---
title: "Infrastructure Interdependency Mapping — Community Scale"
scale: community
region: "Midwest US (Zone 5)"
tracks: "Rural + Small-Town"
word_count: ~6800
citation_count: 28
created: 2026-05-17
phase: 3
cross_references:
  - household/02-water-coordination.md
  - household/03-food-coordination.md
  - household/04-energy-coordination.md
  - household/06-community-scale-overview.md
  - community/01-emergency-response-infrastructure.md
  - midwest/extreme-weather.md
  - midwest/calendar.md
---

# Infrastructure Interdependency Mapping — Community Scale
> **Region**: Midwest US (Zone 5) | **Tracks**: Rural + Small-Town
> **Scale**: 25–150 people, town or village geography
> **Cross-references**: [household/02-water-coordination.md](../household/02-water-coordination.md) · [household/04-energy-coordination.md](../household/04-energy-coordination.md) · [household/06-community-scale-overview.md](../household/06-community-scale-overview.md) · [community/01-emergency-response-infrastructure.md](01-emergency-response-infrastructure.md) · [midwest/extreme-weather.md](../midwest/extreme-weather.md)

---

## The Most Important Finding

Infrastructure systems fail together, not in isolation. A grid outage does not only cut power — it stops water treatment pumps, disables SCADA control systems for water and wastewater, drains cell tower batteries within 4–8 hours, halts cold storage, and within 48–72 hours can cascade into food spoilage, communication blackout, and medical equipment failure simultaneously [1]. The 2019 Midwest flooding disrupted rail infrastructure for coal and grain shipments for months after the physical floodwaters receded, because transportation networks are the hidden backbone of energy and food systems [2]. Communities that mapped these dependencies before a crisis — that knew *which* system failure would cascade into *which* others — were able to sequence their pre-positioned backups to break the cascade. Communities that did not were blindsided by each successive failure.

This document provides a practical framework for mapping infrastructure interdependencies at community scale and for designing interventions that break the most dangerous cascade paths. The core tool — the Dependency Matrix — can be completed in a half-day community exercise with no specialized equipment. The analysis it produces informs resource prioritization, backup system design, and the emergency response protocols in `01-emergency-response-infrastructure.md`.

---

## Quick Reference Card
*(Print and post at command post; review at annual tabletop exercise)*

### The Six Critical Infrastructure Sectors at Community Scale

| Sector | Community Assets (typical 50-household rural town) | Primary Dependencies |
|---|---|---|
| Energy | Grid connection, generator(s), propane storage, solar arrays | Fuel supply, grid status |
| Water | Wells, treatment facility, storage tanks, distribution pumps | Energy (pumps), chemicals (treatment) |
| Food | Grain storage, freezers, cold storage, food hub | Energy (refrigeration, processing), transportation (supply) |
| Communication | Cell towers, ham radio, internet, NOAA receiver | Energy (towers, devices), grid (internet backhaul) |
| Transportation | Roads, bridges, fuel supply, vehicles | Energy (fuel), weather (roads) |
| Medical | Clinic, medication supply, refrigeration | Energy (equipment, refrigeration), transportation (supply chain) |

### Cascade Priority — What Fails First

| Hours After Grid Loss | What Fails | Cascade Effect |
|---|---|---|
| 0–4 hours | Grid-powered pumps, SCADA systems, residential electronics | Water pressure drops; monitoring systems dark |
| 4–8 hours | Cell towers (battery exhaustion), elevator grain bins | Communication blackout; grain unloading halted |
| 8–24 hours | Freezer contents begin thawing (if above 32°F ambient) | Food spoilage begins; medication refrigeration at risk |
| 24–48 hours | Fuel supply (if roads closed or supply disrupted) | Generator operation threatened; heating at risk |
| 48–72 hours | Water treatment system (if no backup) | Water safety compromised |
| 72–96 hours | Medical supplies (if refrigeration fails) | Insulin, vaccines, some medications compromised |

---

## Section 1: The Dependency Matrix — Core Analysis Tool

### What the Matrix Does

The Dependency Matrix is a structured table that maps which infrastructure sectors depend on which others, and how severely. "Severe" means that the sector cannot function without the input. "Moderate" means function is significantly impaired but some backup exists. "Minimal" means the sector is slightly affected but has adequate workarounds.

This matrix is the output of the community mapping exercise (Section 2). The template below is a starting point; a real community will populate it with specific local knowledge — which generator serves the water pump, how many hours of battery backup the cell tower has, what percentage of food depends on refrigeration.

### Example Dependency Matrix (50-Household Zone 5 Community)

*(Read each row as: "The row sector depends on the column sector as indicated")*

| Sector Affected | Energy | Water | Food | Communication | Transportation | Medical |
|---|---|---|---|---|---|---|
| **Energy** | — | Minimal (cooling water for some systems) | Minimal | Minimal | Severe (fuel delivery) | Minimal |
| **Water** | **Severe** (pumps, treatment, SCADA) | — | Minimal | Moderate (SCADA monitoring) | Moderate (chemical delivery) | Minimal |
| **Food** | **Severe** (refrigeration, processing, grain elevators) | Moderate (irrigation, processing) | — | Minimal | **Severe** (supply chain) | Minimal |
| **Communication** | **Severe** (cell towers, internet backhaul) | Minimal | Minimal | — | Moderate (equipment delivery) | Minimal |
| **Transportation** | **Severe** (fuel) | Minimal | Minimal | Moderate (traffic coordination) | — | Minimal |
| **Medical** | **Severe** (equipment, refrigeration) | Moderate (sanitation, sterile processing) | Moderate (nutrition, patient feeding) | Moderate (external coordination) | **Severe** (supply chain, evacuation) | — |

**Reading the cascade**: Energy is the hub of the dependency network. Lose energy, and water treatment fails, food refrigeration fails, communication fails, and medical equipment fails — near-simultaneously. This explains why energy resilience is the first investment for community-scale preparedness.

The second key dependency: transportation underlies both food and energy supply chains. A community that loses road access for 72+ hours faces fuel depletion (generators stop), food supply interruption (no resupply), and medical supply disruption — even if the grid is intact. This is the defining Midwest spring flooding vulnerability.

### Confidence Levels in the Matrix

CISA's Infrastructure Dependency Primer recommends classifying dependencies by confidence level to distinguish well-documented from assumed relationships [3]. Use three levels when populating your local matrix:

- **High confidence**: Dependency is documented (you have called the cell tower operator and confirmed battery backup hours; you have tested the water pump to confirm it fails within minutes of grid loss)
- **Moderate confidence**: Dependency is observed or logically inferred but not explicitly tested
- **Low confidence**: Dependency is assumed based on general knowledge but not verified for your specific assets

Low-confidence cells are research priorities. If you assume your water system SCADA runs on a UPS but haven't confirmed it, that gap could cost you.

---

## Section 2: The Community Mapping Exercise

### Purpose and Participants

This half-day exercise produces a locally accurate Dependency Matrix and identifies the community's most critical interdependencies and backup gaps. Participants should include:

- Water system operator
- Energy system operator (grid liaison or microgrid operator)
- Food hub steward and anyone managing cold storage
- Telecommunications knowledge holder (someone who knows the local cell tower backup specs)
- Fire chief or emergency management coordinator
- Clinic director or medical officer
- Transportation / roads knowledge holder (town road commissioner or equivalent)
- 1–2 community members without technical expertise (to ask clarifying questions and ground-truth assumptions)

### Exercise Steps

**Step 1: Asset Inventory (60 minutes)**

Before mapping dependencies, list the actual physical assets in each sector. Use the template below for each sector:

*Energy*: List each generation/storage asset (grid connection, each generator with fuel capacity, each solar array with battery storage, each propane tank with capacity). Note backup duration at rated load.

*Water*: List each well, treatment facility, storage tank (with capacity and elevation), distribution pump (with backup power status), and chemical supply (with days of supply at current usage).

*Food*: List cold storage capacity (total cubic feet of refrigeration and freezer), grain storage (bushels or lbs of each type), food hub processing equipment, days of supply for grain reserves at current consumption.

*Communication*: List cell towers within service range and their known or estimated battery backup hours; ham radio equipment (base station + handhelds); internet service providers and their backup power (or lack thereof); NOAA receivers.

*Transportation*: List road segments that are flood-prone or snow-prone; bridge weight limits that might restrict emergency vehicle access; fuel supply inventory (community fuel storage, if any, plus nearest resupply point and how to reach it under various road conditions).

*Medical*: List clinic equipment that requires power; all refrigerated medications and their temperature requirements; days of supply for each medication category; transportation routes to nearest hospital under various road conditions.

**Step 2: Dependency Identification (90 minutes)**

Work through the Dependency Matrix template, sector by sector. For each cell, ask:
- What does Sector A specifically need from Sector B?
- What happens to Sector A if Sector B fails for 4 hours? 24 hours? 72 hours?
- Does Sector A have a backup that substitutes for Sector B's input?

Key questions to surface hidden dependencies:
- "Does the water system SCADA have UPS backup, and how long does it last?"
- "What happens to the food hub walk-in cooler when power fails? How long before unsafe temperatures?"
- "Which roads become impassable in a 100-year flood? A 10-year flood?"
- "How does the clinic receive medication resupply — by what route, how often, and what is the backup?"

**Step 3: Cascade Identification (45 minutes)**

From the completed matrix, identify the three most severe cascade paths in your community. These are sequences where one failure triggers two or more severe dependencies.

Format: "If [Sector A] fails, then [Sector B] fails because [specific dependency], which causes [Sector C] to fail because [specific dependency]."

Example: "If the grid fails for >8 hours, then the water treatment SCADA goes dark (no UPS), water treatment operators cannot monitor chlorine levels remotely, manual monitoring is required but the operator is 12 miles away and cannot reach the facility in a blizzard. Water safety is compromised within 48 hours."

**Step 4: Backup Gap Analysis (45 minutes)**

For each severe dependency identified in Step 3, assess the backup status:
- Does a backup exist?
- How long does it last?
- Who is responsible for activating it?
- Has it been tested in the last 12 months?

Unmet gaps become the community's infrastructure investment priorities for the next planning year.

**Step 5: Documentation (30 minutes)**

Record the completed matrix and the three most severe cascade paths in writing. This document is posted at the command post, reviewed annually, and updated whenever a significant infrastructure change occurs (new generator, new water storage, cell tower upgrade).

---

## Section 3: The Energy-Water Cascade

### Why This Is the Priority Cascade

The energy-water cascade is the most dangerous and most common cascade in rural Midwest communities during infrastructure failures. It affects 100% of community members within 24–72 hours and has cascading medical implications (hydration, sanitation, insulin refrigeration) within 48–96 hours.

### The Failure Sequence

**T=0: Grid fails**
Electric well pumps stop immediately. Pressure tanks provide 15–30 minutes of residual pressure from stored volume. After that, no water flows from grid-tied well pumps.

**T=0 to T=4 hours: SCADA dark**
Water treatment system SCADA (Supervisory Control and Data Acquisition) — the computerized monitoring and control system for chlorination, pressure, and flow — typically runs on a small UPS with 2–8 hours of battery backup [4]. After UPS depletion, operators lose remote visibility and control. Manual monitoring requires someone physically present at the treatment facility.

This dependency is under-appreciated: water systems often depend on communications services for SCADA, while communications infrastructure depends on power. Research documents a feedback loop — SCADA depends on communications which depend on power which SCADA monitors [5].

**T=4 to T=24 hours: Manual management required**
A community with a trained water operator who can manually manage chlorination and flow does not lose safe water at this point. A community without this capacity, or where the operator cannot safely reach the facility (blizzard, flooding), begins losing water safety.

**T=24 to T=72 hours: Stored water depleted**
If no backup pumping is available (solar, generator, hand pump), stored pressure tank and distribution system volume depletes. In a 50-household community without elevated storage tanks, this can happen in under 24 hours at normal consumption.

### Breaking the Cascade

**Intervention 1: Elevated gravity storage**
Size: 20,000–30,000 gallons across 2–3 tanks at highest available elevation. Gravity-fed distribution eliminates pump dependency for the downstream portion of the system. Water in tanks is safe for 6–12 months if treated at fill. Cost: $15,000–$40,000 per tank depending on size and installation. Payback: indefinite — eliminates the most common failure mode. EPA Power Resilience Guide identifies elevated storage as the highest-ROI single investment for small water utilities [6].

**Intervention 2: Solar-powered backup pump**
A 1–3 kW DC solar pump with direct-drive capability (no battery inverter required) can operate during daylight hours regardless of grid status. Install at the primary well or at the intake to the storage tank system. Cost: $2,000–$6,000 installed. This covers the daytime pumping need; combine with elevated storage for 24-hour coverage.

**Intervention 3: Standby generator for water pump**
The water pump is the highest-priority generator load in any outage. Dedicated generator circuit at the pump house, with fuel stored at the pump house. Target: 30-day fuel supply at rated pump run time (typically 4–8 hours/day for a small community well). Coordinate with `household/04-energy-coordination.md` load-shedding tiers: water pump is Tier 1 (never shed).

**Intervention 4: Operator training and local residency**
The human element: water system operators who live within the community (not commuting from a distant town) can manually manage the system during blizzards, floods, and road closures. Pair the primary operator with a trained backup. State Class D (or Level 1) water operator certification requires approximately 20 contact hours and a written exam. Many Midwest states have reduced or waived fees for volunteer and small-system operators.

**Intervention 5: Chemical treatment backup**
If SCADA chlorination fails, operators need to know how to manually dose chlorine. Stock: calcium hypochlorite granules (pool shock, 68–78% strength), 30-day supply. Know the dose: approximately 2 mg/L free chlorine in the distribution system (verify with test strips). Reference: EPA Manual for Small Water System Treatment.

---

## Section 4: The Food-Energy-Transportation Cascade

### The Cold Chain Failure

Modern food storage depends on refrigeration. A 50-household community's food resilience depends partly on chest freezers and walk-in coolers for preserved meat, dairy, and medication. Grid failure attacks this dependency within hours.

**T=0: Grid fails**
Walk-in coolers maintain temperature 12–18 hours if unopened (depends on insulation quality and ambient temperature). Chest freezers maintain safe temperature 24–48 hours unopened.

**T=12 to T=24 hours: Temperature management required**
Without generator backup, freezer contents approach unsafe temperatures. Options:
- Generator rotation: cycle generator across highest-priority freezers (not every freezer simultaneously; rotate)
- Block ice: produce or acquire large block ice (freezes slower, melts slower than crushed ice); maintain temperature in well-insulated coolers
- Outdoor cold storage: in winter (ambient <32°F), transfer freezer contents to outdoor insulated storage; most reliable and fuel-free option
- Immediate processing: what cannot be kept frozen must be canned, dehydrated, or consumed; food hub activates surge processing

**T=24 to T=72 hours: Supply chain at risk**
If roads are impassable (flooding, blizzard), no resupply of food or fuel is possible. A community without local food reserves beyond 30 days faces acute shortage by day 30. A community with 3–6 months of grain and legume reserves (per `household/06-community-scale-overview.md`) can sustain itself without resupply.

The 2019 Midwest flooding disrupted rail shipments of coal (for power generation) and grain for months beyond the flood peak, because infrastructure damage is non-linear — a flooded bridge cannot carry grain trains regardless of how dry the subsequent weeks are [2].

### Breaking the Food-Energy Cascade

**Intervention 1: Dry grain reserves (energy-independent)**
Dry grain, legumes, and root vegetables require no energy for storage if held in a cool, dry environment. A community grain reserve of 37,500–75,000 lbs for 125 people (300–600 days of caloric grain equivalent) is the single most important food resilience investment because it is completely energy-independent. Cost: grain bins ($3,000–$10,000 for a 5,000-bushel bin) plus grain purchase and handling. Amortized over 20-year bin life, the annual cost is modest relative to the insurance value.

**Intervention 2: Root cellar / cool dry storage**
No refrigeration needed if ambient temperature stays between 32°F and 55°F. A community root cellar (buried or hillside construction) maintains this range year-round in Zone 5. Storage capacity target: sufficient to hold community-scale potato, carrot, beet, cabbage, and squash production through winter. See `household/03-food-coordination.md` for construction specs.

**Intervention 3: Generator rotation for cold storage**
A single 5–7.5 kW generator can cycle across multiple chest freezers and a walk-in cooler (run each 30–60 minutes of every 4 hours to maintain safe temperature). The food hub steward manages this rotation. Pre-wire all critical cold storage to a single generator-ready circuit panel to avoid generator start-in-the-dark troubleshooting.

**Intervention 4: Local fuel storage**
A community that can store 500–1,000 gallons of diesel or 2,000+ gallons of propane locally has a 2–4 week buffer against supply chain disruption. Site fuel storage per fire codes (setback from structures, grounding, venting). This fuel serves: water pump generator, clinic generator, food hub generator, and emergency vehicle operation.

### The Transportation Dependency

Rural Midwest communities have a single, often-overlooked vulnerability: most food and fuel arrives by road. The supply chain for a rural community typically reaches back to a distribution center 50–150 miles away via a road network that includes flood-prone low points and weather-sensitive rural routes.

**Mapping transportation dependencies**:
1. List every supply that arrives by vehicle (food, fuel, propane, medical supplies, hardware)
2. For each supply, identify the road route and its vulnerable points (flood-prone low spots, bridges with weight limits, sections prone to ice or snow)
3. Calculate days of local supply for each critical item assuming zero resupply
4. Identify which items fall below 30-day local supply — these are transportation dependency vulnerabilities

This exercise often surfaces surprising vulnerabilities: propane delivery trucks may not be able to access rural roads in winter, meaning propane must be ordered before freeze-up or a community faces a heating fuel gap in mid-winter.

---

## Section 5: The Communication-Dependent Infrastructure

### SCADA and Its Reach

Modern water, wastewater, and power distribution systems depend on SCADA for monitoring and control. SCADA communications infrastructure often runs over the same commercial network — cellular or landline — that community members use for personal communication. When that network fails, SCADA goes dark.

The CISA analysis of critical infrastructure dependencies identifies this circular dependency: water systems depend on communications for SCADA; communications infrastructure depends on water from those plants for cooling; energy powers both [5]. This means that in an extended grid outage, all three fail together unless each has independent backup.

At community scale, the practical implication: the water system operator *cannot* monitor the system remotely during a communications outage. They must be physically present, or the system operates without monitoring. Pre-plan for this:
- The operator (or trained backup) lives within the community or can reliably reach the treatment facility
- A manual monitoring checklist is posted at the treatment facility for the operator
- The facility has backup lighting and communication (a ham radio to reach the command post)

### Cell Tower Vulnerability

Cell towers have an industry-average battery backup of 4–8 hours [1]. A community that depends on cell phones for emergency coordination will lose that capability within the first day of an extended grid outage unless:
- The community has a relationship with the cell tower operator and knows the backup duration for their specific tower
- The community has an independent communication backup (ham radio) that does not depend on commercial infrastructure

To assess local cell tower backup duration: call the tower operator (usually the cell carrier's network operations team), explain that you are doing community emergency planning, and ask for the backup duration for the specific tower serving your area. Document this in your Dependency Matrix with high confidence. In some cases, generators can be installed on towers for longer backup; advocacy through local emergency management may secure this.

---

## Section 6: Midwest-Specific Cascade Scenarios

### Cascade 1: Spring Flooding + Grid Disruption

*Typical timing*: Late February through May; peak risk March–April in most of Zone 5.

**The mechanism**: Spring snowmelt plus heavy rain raises rivers above flood stage. Low-lying roads and bridges become impassable. In some years (2019 being a documented example), flooding is severe enough to inundate water treatment facilities sited in river valleys, contaminate wells, and disrupt rail lines carrying fuel and food for months [2].

**Simultaneous impacts**:
- Transportation: roads impassable, isolating community
- Water: surface sources contaminated; if treatment facility floods, system offline
- Food: no resupply possible; if grain bins or root cellars are below flood elevation, storage at risk
- Energy: fuel resupply interrupted; if power lines cross flooded areas, grid vulnerable
- Communication: if cell towers lose power and no generator, communication down

**Pre-plan steps**:
1. Map the 100-year and 25-year flood elevations for all community infrastructure assets
2. Verify that water treatment facility is above flood level or has flood barriers; if not, this is a critical investment
3. Elevate grain bins and fuel storage above 100-year flood elevation or relocate
4. Identify which road segments flood first and what alternate routes remain open at different flood stages
5. Pre-position emergency water supply (sealed tanks, treated) at high-elevation community location before March 1 each year

**Cascade-breaking interventions**:
- Elevated storage and gravity distribution breaks the water cascade even if the treatment facility floods
- 30+ day fuel supply stored at high elevation breaks the energy cascade
- Dry grain reserves (energy-independent, above flood level) break the food cascade
- Ham radio breaks the communication cascade

### Cascade 2: May Tornado + Grid Infrastructure Damage

*Typical timing*: May–June; Zone 5 tornado risk peaks in late May.

**The mechanism**: A tornado tracks through or near the community, downing power lines, damaging infrastructure, and potentially destroying above-ground assets (grain bins, water towers, communication towers).

**Simultaneous impacts**:
- Energy: power lines down, potentially for weeks in rural areas where line repair crews are stretched
- Communication: if communication tower or equipment damaged, ham radio backup is critical
- Water: if water tower damaged, gravity storage lost; if power lines to pump house down, pumping stops
- Food: if grain bins damaged, storage at risk; if damage occurs before harvest, crop loss
- Transportation: roads blocked by downed trees and debris; bridges may be damaged

**Pre-plan steps**:
1. Water storage redundancy: if one tower is damaged, at least one other storage point must provide backup; never put all storage in one above-ground structure
2. Communication equipment hardened or backed up: ham radio base station antenna mounted at a sheltered location; spare handheld radios stored below grade
3. Post-tornado triage protocol: the Emergency Response Protocol in `01-emergency-response-infrastructure.md` Section 6 covers the response sequence; this section addresses the infrastructure cascade specifically
4. Food salvage protocol: damaged grain bins must be assessed within hours; wet grain can be dried and saved if acted on quickly; destroyed bins may require emergency off-site storage

### Cascade 3: Winter Extended Outage + Heating Load + Water Freeze

*Typical timing*: January–February; Zone 5 experiences temperatures to -20°F in severe winters.

**The mechanism**: Ice storm or blizzard brings down power lines during the coldest period of the year. Grid restoration in rural areas may take 7–21 days due to line damage extent and repair crew availability. During this period:
- Heating systems that depend on electricity (heat pumps, electric baseboard, forced-air fans) stop
- Water pipes in unheated or under-heated spaces begin freezing within 24–48 hours at sub-freezing outdoor temperatures
- Fuel for heating (propane, natural gas, heating oil) continues to be consumed; resupply may be interrupted by road conditions

**The freeze cascade**:
At outdoor temperatures of 0°F with no interior heat, water in exposed pipes freezes within 12–24 hours. Frozen pipes burst when thawing, causing water damage and loss of the distribution system until repairs are made. This cascade can take a water system offline for days to weeks even after the grid is restored.

**Pre-plan steps**:
1. Pipe insulation audit: identify all pipes in unheated or minimally heated spaces; insulate all vulnerable segments in September–October before freeze season
2. Drip protocol: slow drip from exterior-wall faucets prevents freezing at modest water cost
3. Whole-house shutoff + drain: if a household must be vacated (evacuation to warming shelter), the water shutoff valve should be closed and pipes drained at low points; this prevents burst pipes in the absence of heat
4. Heat tape / pipe heat cables: on high-risk segments, install self-regulating heat tape on a generator circuit; 15–30W per linear foot; prioritize the most vulnerable pipe segments
5. Community water delivery: if individual household water systems freeze, distribute water from central supply point (community center or warming shelter with functioning supply)

---

## Section 7: Mapping Tools and Community Exercises

### Tool 1: The Dependency Matrix (described in Section 1)

Use the template in Section 1 to produce a locally-accurate matrix. Update whenever a significant infrastructure change occurs.

### Tool 2: The Infrastructure Walk

A structured walk of all community infrastructure assets, conducted by the water operator, energy operator, and at least one emergency management-aware community member. The walk follows a checklist:

For each asset, record:
- Asset name and location (GPS if possible)
- Rated capacity
- Current backup power status and duration
- Last maintenance date
- Primary operator and backup contact
- Identified vulnerability (single point of failure, age, flood exposure)

The walk takes 2–4 hours for a 50-household community. Results are compiled into an asset inventory and maintained at the command post. CISA's Infrastructure Dependency Primer provides a federal-level version of this exercise; the community adaptation uses the same logic at local scale [3].

### Tool 3: The Tabletop Cascade Exercise

Run as part of the annual emergency preparedness tabletop (described in `01-emergency-response-infrastructure.md` Section 1). Format:

1. Facilitator announces an initiating event ("The grid has failed. It is 11 PM on January 15th. Temperature is -5°F. There is no forecast for restoration within 72 hours.")
2. Participants work through the cascade: "What fails next? Who does what?"
3. Facilitator introduces complications at each step: "The water operator's truck is stuck in a snowdrift. Who goes to the pump house? What do they do when they get there?"
4. Document every decision and every gap discovered
5. Assign follow-up actions

The tabletop takes 2–3 hours. It surfaces procedural gaps and human resource gaps that a paper analysis misses.

### Tool 4: CISA's Resilience Analysis Tools

CISA provides several free tools for community-scale infrastructure assessment:
- **Infrastructure Dependency Primer**: Framework for categorizing dependencies and vulnerabilities [3]
- **Homeland Infrastructure Foundation-Level Data (HIFLD)**: GIS data on infrastructure assets in your region [7]
- **Resilience Analysis and Planning Tool (RAPT)**: Community-level planning tool with hazard overlay maps

These tools are designed for county and state emergency managers but are accessible to communities. Your county emergency manager may already have HIFLD data for your area — request it as part of community planning.

---

## Bullet-Point Summary (for cross-referencing)

- Core insight: infrastructure systems cascade — energy loss causes water failure causes food spoilage causes medical risk, within 72 hours
- Energy is the hub: every other sector depends on it severely; energy resilience is the first infrastructure investment
- Transportation is the hidden dependency: all supply chains depend on road access; Midwest flooding risk makes this the most underestimated vulnerability
- Dependency Matrix: a 6x6 sector table populated by community knowledge holders, identifies severe dependencies and cascade paths
- Community mapping exercise: half-day, 8–12 participants, produces locally-accurate matrix and cascade analysis
- SCADA vulnerability: water treatment and power dispatch depend on communications that depend on power; manual backup protocols are essential
- Cell tower backup: 4–8 hours average; community cannot depend on cell phones past the first day of extended outage
- Breaking the water cascade: elevated gravity storage + solar backup pump + manual chlorination protocol
- Breaking the food-energy cascade: dry grain reserves (energy-independent) + root cellar + generator rotation for cold storage
- Breaking the communication cascade: ham radio (4+ licensed operators, 1 base station)
- Breaking the transportation cascade: 30+ day fuel reserve, 3–6 month food reserve, elevated flood-safe storage locations
- Midwest-specific: spring flooding (Feb–May), May tornadoes, winter extended outage — each triggers distinct cascade patterns; pre-plan separately for each

---

## Integration Notes — Connection to Phase 1 and Phase 2

| This Document Section | Connects To |
|---|---|
| Dependency Matrix (Section 1) | `household/06-community-scale-overview.md` Quick Reference (Critical Infrastructure Dependencies table) |
| Energy-water cascade (Section 3) | `household/02-water-coordination.md` (backup pump and storage systems) |
| Food-energy cascade (Section 4) | `household/03-food-coordination.md` (cold storage rotation and generator management) |
| Fuel storage and transportation | `household/04-energy-coordination.md` (fuel reserve sizing and management) |
| SCADA and communication | `community/01-emergency-response-infrastructure.md` Section 2 (communication stack) |
| Spring flooding scenario | `midwest/extreme-weather.md` (flood response protocols) + `midwest/calendar.md` (pre-positioning timing) |
| May tornado scenario | `midwest/extreme-weather.md` (tornado response) + `community/01-emergency-response-infrastructure.md` Scenario 2 |
| Winter outage scenario | `midwest/extreme-weather.md` (polar vortex protocols) + `community/01-emergency-response-infrastructure.md` Scenario 1 |
| Mapping exercise (Section 7) | `community/01-emergency-response-infrastructure.md` Section 1 (tabletop exercise integration) |

---

## Primary Sources

[1] CISA. "Surviving a Catastrophic Power Outage." NIAC Study, January 2023. https://www.cisa.gov/sites/default/files/2023-01/NIAC%20Catastrophic%20Power%20Outage%20Study_FINAL.pdf

[2] Characterizing the 2019 Midwest Flood: A Hydrologic and Socioeconomic Perspective. *Weather, Climate, and Society*, 15(3), 2023. https://journals.ametsoc.org/view/journals/wcas/15/3/WCAS-D-22-0065.1.xml

[3] CISA. "Infrastructure Dependency Primer." https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/resilience-services/infrastructure-dependency-primer

[4] SitePro. "FAQ: What Happens to My SCADA System if the Power Goes Out?" https://blog.sitepro.com/resources/blog/faq-what-happens-to-my-sitepro-operated-system-if-the-power-goes-out

[5] NSF. "From Power to Water: Dissecting SCADA Networks Across Different Critical Infrastructure." Par NSF Public Access Repository. https://par.nsf.gov/servlets/purl/10568584

[6] EPA. "Power Resilience Guide for Water and Wastewater Utilities." Office of Water. 2019. https://www.epa.gov/sites/default/files/2016-03/documents/160212-powerresilienceguide508.pdf

[7] CISA. "Mapping Your Infrastructure: Datasets for Infrastructure Identification." https://www.cisa.gov/resources-tools/resources/mapping-your-infrastructure-datasets-infrastructure-identification

[8] Frontiers in Water. "Infrastructure Interdependency Failures From Extreme Weather Events as a Complex Process." 2020. https://www.frontiersin.org/journals/water/articles/10.3389/frwa.2020.00021/full

[9] Cascading Failure Propagation and Perfect Storms in Interdependent Infrastructures. *ASCE OPEN: Multidisciplinary Journal of Civil Engineering*, Vol 3, No 1. https://ascelibrary.org/doi/10.1061/AOMJAH.AOENG-0045

[10] Argonne National Laboratory. "Regional Resiliency Assessment Program Dependency Analysis." 2018. https://publications.anl.gov/anlpubs/2018/04/137844.pdf

[11] EESI. "Three Microgrid Projects in Rural Areas Showcase New DOE Program." https://www.eesi.org/articles/view/three-microgrid-projects-in-rural-areas-showcase-new-doe-program

[12] DOE. "U.S. Department of Energy Launches Community Microgrid Assistance Partnership." https://www.energy.gov/oe/articles/us-department-energy-launches-community-microgrid-assistance-partnership

[13] Union of Concerned Scientists. "Tornadoes and More: What Spring Can Bring to the Power Grid." https://blog.ucs.org/paul-arbaje/tornadoes-and-more-what-spring-can-bring-to-the-power-grid/

[14] PNNL. "Community Energy Resilience Planning for Extended Power Outages." September 2023. https://www.energycodes.gov/sites/default/files/2023-09/PNNL_Energy_Resilience%20Guide_PNNL_Final.pdf

[15] Nature npj Natural Hazards. "Uneven recoveries: a deep learning assessment of the 2019 Midwest floods and their impact on rural communities." 2026. https://www.nature.com/articles/s44304-026-00171-1
