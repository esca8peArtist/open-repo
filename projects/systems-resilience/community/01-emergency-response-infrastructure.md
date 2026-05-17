---
title: "Emergency Response Infrastructure — Community Scale"
scale: community
region: "Midwest US (Zone 5)"
tracks: "Rural + Small-Town"
word_count: ~7800
citation_count: 32
created: 2026-05-17
phase: 3
cross_references:
  - household/01-household-coordination-overview.md
  - household/05-healthcare-coordination.md
  - household/04-energy-coordination.md
  - household/06-community-scale-overview.md
  - individual/05-healthcare.md
  - midwest/extreme-weather.md
---

# Emergency Response Infrastructure — Community Scale
> **Region**: Midwest US (Zone 5) | **Tracks**: Rural + Small-Town
> **Scale**: 25–150 people, town or village geography
> **Cross-references**: [household/01-household-coordination-overview.md](../household/01-household-coordination-overview.md) · [household/05-healthcare-coordination.md](../household/05-healthcare-coordination.md) · [household/04-energy-coordination.md](../household/04-energy-coordination.md) · [household/06-community-scale-overview.md](../household/06-community-scale-overview.md) · [midwest/extreme-weather.md](../midwest/extreme-weather.md)

---

## The Most Important Finding

Cascading failures — grid outage plus supply disruption plus medical system stress occurring simultaneously — are the defining threat to community-scale resilience, and they are not rare edge cases. When PG&E cut power to 738,000 customers in October 2019, Blue Lake Rancheria's pre-built microgrid islanded automatically within seconds and became a functioning emergency hub for an estimated 10,000 surrounding residents within 30 hours [1]. When Hurricane Maria knocked out Puerto Rico's grid for up to 11 months in 2017, the communities that fared best were not those that received the most external aid but those with pre-existing mutual aid infrastructure and distributed communication networks — the Centros de Apoyo Mutuo in Barrio Mariana and Caguas sustained food, medical, and communication services when government systems were absent for months [2].

The central lesson from both cases: emergency response infrastructure is not a set of plans written in advance and executed during a crisis. It is a set of *practiced* systems — communication networks, command structures, medical protocols, and resource allocation frameworks — that work precisely because they have been exercised before the crisis arrives. A community that activates its Incident Command Structure for the first time during a real emergency will face coordination failures; a community that has run the structure through tabletop exercises and the annual tornado drill will not.

This document defines the four components of community-scale emergency response infrastructure and provides specific, step-by-step guidance for building each:
1. Command structure and communication network
2. Resource allocation under scarcity
3. Medical surge capacity and triage
4. Shelter and mass care coordination

It builds directly on the governance frameworks in `household/06-community-scale-overview.md` and extends them into the operational domain of crisis response.

---

## Quick Reference Card
*(Print and post at town hall, fire station, clinic, and each neighborhood cluster's designated emergency contact household)*

**Reference scenario**: Zone 5 Midwest small town, 35–50 households, 90–140 people. Event: simultaneous grid outage (7+ days), fuel supply disruption (roads impassable or supply chain broken), medical system stress (clinic operating without external support, nearest hospital inaccessible).

### Incident Activation Thresholds

| Condition | Threshold | Response Level |
|---|---|---|
| Grid outage | >4 hours | Level 1: Monitor and communicate |
| Grid outage | >48 hours | Level 2: Emergency council activates |
| Supply chain disruption | Roads impassable >24 hours | Level 2: Emergency council activates |
| Medical event | >3 households affected simultaneously | Level 2: Emergency council activates |
| Multiple simultaneous failures | Any 2 of the above | Level 3: Full community response |
| Natural disaster (tornado, flood, ice storm) | Any infrastructure damage | Level 3: Full community response |

### Communication Cascade (all levels check in within 30 minutes of incident declaration)

1. Emergency council activates via pre-agreed phone/radio tree
2. Cluster stewards check in with their clusters (5–7 households each)
3. Ham radio net activates on designated primary frequency (written below): _______________
4. Backup frequency (in case of interference): _______________
5. Regional emergency management check-in: twice daily at ________ and ________

### Resource Allocation — Tier-1 Priorities (never shed)
- Insulin refrigeration and critical medication storage
- Water treatment and distribution pumping
- Clinic lighting and equipment
- Communication nodes (ham radio, NOAA receiver)

---

## Section 1: Command Structure

### Why NIMS/ICS Adapted for Village Scale

The National Incident Management System (NIMS) provides the conceptual framework; the Incident Command System (ICS) provides the operational structure. Both were designed for larger agencies but the core logic applies at village scale: a single incident commander with clear authority, organized functional sections (Operations, Logistics, Planning, Finance), and a unified chain of command that prevents conflicting orders during a fast-moving situation [3].

A community of 50 households does not run a full ICS with Section Chiefs and Branch Directors. It runs a *simplified* ICS adapted to its human resources: typically 4–7 designated roles filled by the emergency council plus domain stewards.

### The Village ICS Structure

**Incident Commander (IC)**
- Role: Single decision authority during declared emergency
- Default: Fire chief or most experienced emergency manager in town
- Backup (in succession): Clinic director, then senior selectboard member
- Authority includes: Activating community protocols, deploying shared resources, ordering evacuation or consolidation, requesting external assistance
- The IC does not override ongoing medical triage or clinic decisions — the clinic director has clinical authority; the IC has logistical authority

**Operations Section (what's happening on the ground)**
- Cluster Stewards report to Operations
- Each steward maintains real-time accountability of their cluster (headcount, household status, critical needs)
- Operations also manages: search and rescue (if applicable), traffic control, fire suppression

**Logistics Section (getting resources where they're needed)**
- Food hub steward and water system operator report to Logistics
- Manages: fuel allocation, food distribution, equipment deployment, incoming volunteer coordination
- Maintains the master resource register (see Section 2)

**Medical Officer**
- Clinic director or highest-trained medical professional available
- Manages: triage, surge capacity, medication allocation, chronic disease patient tracking
- Has autonomous authority over all medical decisions; coordinates with IC on resource needs

**Communications Officer**
- Licensed ham radio operator (ARRL ARES/RACES-trained preferred)
- Manages: ham radio net, NOAA monitoring, information posting at community board, external agency liaison

**Documentation / Planning**
- Town clerk or designated record-keeper
- Maintains incident log: what happened, when, what decision was made, who made it
- This record becomes the post-incident After Action Report and informs future planning

### Activation Sequence

**Declaring a Level 2 Emergency** (5-step sequence, target completion within 2 hours of trigger event):

1. IC or most senior available official declares Level 2 by phone or in person to the remaining emergency council members
2. Communication Officer activates ham radio net and notifies all cluster stewards by radio or phone
3. Each cluster steward conducts an immediate headcount and status report (paper form, radio-reported within 30 minutes)
4. Logistics Officer opens the emergency supply cache and begins resource register inventory
5. Medical Officer activates surge capacity protocol (see Section 3) and contacts all chronic disease registry patients

**Declaring Level 3** (triggered when Level 2 response is insufficient or simultaneous failures exceed Level 2 capacity):

Level 3 adds: shelter consolidation activation, rationing protocol initiation, and direct contact with county/state emergency management for external resource request. Ham radio net goes to continuous monitoring (someone at the radio at all times).

### Command Post Location

Physical location matters. The command post (CP) should be:
- At or near the community center / town hall (central, known location)
- On generator or battery backup power
- Equipped with: ham radio, NOAA receiver, paper maps of the town with cluster boundaries, master resource register (printed copy), contact list for all emergency council members and cluster stewards
- Stocked with: 72-hour food and water for the CP staff, first aid kit, flashlights and batteries, printed copies of all protocols

The CP doubles as the public information point: community members know to come here for official updates. Post status updates on the physical board outside twice daily during Level 2/3 events.

### Training and Exercises

The structure above is worthless without practice. Minimum training program:

| Exercise Type | Frequency | Duration | What It Tests |
|---|---|---|---|
| Tabletop exercise | Annually (March, before tornado season) | 2–3 hours | Decision-making, protocol knowledge |
| Communications drill | Quarterly | 30–60 minutes | Ham radio net, phone tree, cluster check-in |
| Full ICS activation drill | Every 2 years | Half-day | Full activation sequence, resource tracking |
| Cross-training with county emergency management | Annually | 1–2 days | Interoperability with external responders |

FEMA's Community Emergency Response Team (CERT) training (IS-317 and related courses) provides a standardized 20-hour curriculum adaptable to village scale [4]. At minimum, the IC, all emergency council members, and all cluster stewards should complete IS-100 (Introduction to ICS) — free online through FEMA's Emergency Management Institute.

---

## Section 2: Communication Networks

### The Failure Cascade in Communications

Cell towers have 4–8 hours of battery backup on average; during extended grid outages they fail unless running on generator fuel [5]. When Hurricane Maria hit Puerto Rico, 95% of cell towers were out of service within the first week [2]. During the 2020 Iowa derecho, power outages left many communities without cell service for 3–5 days [6]. Cell-dependent communication infrastructure — including many SCADA systems for water treatment and power dispatch — fails at exactly the moment when communication is most critical.

The communication stack for a resilient community has four layers, each functioning independently:

**Layer 1: In-person / foot messenger**
Absolute fallback. Assign a messenger route to each cluster steward: if all electronic communication fails, the steward physically walks their cluster to collect status reports. The route takes no more than 30 minutes to complete for a cluster of 5–7 households within a quarter-mile radius. This layer requires no technology, no power, no infrastructure.

**Layer 2: Ham radio (VHF/UHF)**
The backbone of community emergency communication. Ham radio does not depend on cell towers or internet infrastructure. A handheld VHF radio (Baofeng UV-5R or equivalent, ~$25) has a line-of-sight range of 3–5 miles in flat terrain; a base station with a 10–15-meter elevated antenna extends to 10–20 miles. The ARRL Amateur Radio Emergency Service (ARES) provides organized emergency communication capability and coordinates with county emergency management [7].

Minimum ham radio capability for a 50-household community:
- 4 licensed operators (Technician class minimum — requires passing one 35-question exam covering operating procedures, basic electronics, and FCC regulations)
- 1 base station at the command post with 50W output and 12V battery backup
- Handheld radios for all cluster stewards (may be unlicensed if used only to receive, but for transmitting during emergencies FCC rules allow unlicensed operators under Part 97.405 when professional communication is unavailable)
- Designated primary and secondary net frequencies posted at every cluster's emergency contact location
- Net schedule: check-in twice daily at pre-agreed times during Level 2/3 events; continuous monitoring during Level 3

**Layer 3: NOAA Weather Radio**
A $30–50 hand-crank or battery-powered NOAA weather radio receiver provides continuous broadcast from the National Weather Service, including emergency alerts, flood warnings, and tornado watches. Every cluster should have one that does not depend on grid power. No license required to receive.

**Layer 4: Digital / Winlink (when internet connectivity is partially available)**
Winlink is a ham radio email system that can send messages through radio relay stations without internet connection. It requires a licensed operator and appropriate software, but allows a community to send and receive text-format messages over radio — useful for requesting external resources, reporting status to county emergency management, or communicating with isolated households.

### Information Management During Crisis

Communication creates information; information requires management. The Communications Officer maintains:

**Incident Status Board** (physical, at the command post and posted publicly twice daily):
- Current grid status
- Water system status
- Food hub status
- Medical status (number of patients under clinic care; medication supply status — without names or diagnoses)
- Shelter status (how many people are in warming shelters or consolidated housing)
- Outside assistance status (if applicable)

**Resource Register** (see Section 2):
Updated in real time by Logistics Officer; reported to IC daily.

**Rumor Control**
Disinformation spreads faster during crises than reliable information. The Communications Officer designates one authoritative information source (the physical status board plus any radio announcements) and actively corrects false information when it circulates. Establish the norm *before* the crisis: "official information comes from the status board at the town hall."

---

## Section 3: Resource Allocation Under Scarcity

### The Equity-Efficiency Tension

Emergency resource allocation research identifies a consistent tension between efficiency (distribute resources to maximize total welfare) and equity (ensure minimum welfare for the most vulnerable) [8]. In a 50-household community, this plays out concretely: if the generator fuel supply can run the clinic for 14 days or run three cluster households for 7 days each, which is the right choice? If food reserves support full rations for 90 days or reduced rations for 135 days, when do you implement reduction?

The community's answer to these questions needs to be made *before* the crisis, in writing, as part of the town charter or emergency plan. Decisions made under pressure and exhaustion will be worse than decisions made in advance.

### The Resource Register

The Logistics Officer maintains a master resource register updated weekly during normal operations and in real time during Level 2/3 events. The register tracks:

| Category | Items | Quantity | Location | Days of Supply (at full use) |
|---|---|---|---|---|
| Fuel | Propane (gallons), gasoline (gallons), diesel (gallons) | — | — | — |
| Food | Grains (lbs), canned goods (units), fresh produce (lbs) | — | — | — |
| Water | Treated stored water (gallons), untreated reserve (gallons) | — | — | — |
| Medical | Prescription antibiotics, IV fluids, critical medications | — | — | — |
| Heating | Firewood (cords), propane (gallons allocated to heat) | — | — | — |

The register uses a standard calculation: Days of Supply = Current Inventory / (Daily Consumption Rate × Number of People). When any category falls below 30 days at current consumption, the Logistics Officer notifies the IC and emergency council.

### Pre-Agreed Allocation Tiers

Rationing is most effective when the rules are known in advance by everyone, removing the perception of favoritism. The emergency council adopts the following tier structure — adjusting quantities to fit actual community inventory — by vote before any emergency occurs:

**Tier 0 (Normal)**: Full allocation. No restrictions. Standard community distribution schedule for shared resources.

**Tier 1 (30–45 days of supply remaining)**: Voluntary reduction. Communications Officer posts status board update. Request 10–15% voluntary reduction in fuel and food consumption. No enforcement.

**Tier 2 (15–30 days remaining)**: Mandatory reduction. 20% reduction in non-essential fuel use. Emergency council reviews resource register daily. Food hub reduces processed goods output and shifts to highest-calorie-per-unit preservation.

**Tier 3 (<15 days remaining)**: Strict rationing. Per-person daily allocations set by emergency council (water: 1 gallon/day minimum; food: 1,800 calories/day per adult, 1,200 per child under 10, 2,000 per heavy labor worker; fuel: clinic and water system only). Graduated sanctions for hoarding: first violation = warning; second = reduction in allocation; third = community labor assignment. Emergency council has authority to audit household stocks.

### Priority Populations

Tier structure applies uniformly, with adjustments for:
- **Insulin-dependent diabetics**: Medication refrigeration never shed regardless of tier
- **Infants**: Caloric allocation increased; formula supply tracked in medical register
- **Elderly and mobility-impaired**: Delivery of allocations rather than pickup required; assigned a cluster steward buddy
- **Pregnant women**: Caloric allocation increased by 300 calories; access to clinic maintained

Research on multi-period emergency allocation models shows that accounting for heterogeneous needs (rather than uniform per-capita rationing) improves both equity and efficiency outcomes, reducing total welfare loss by up to 33% in simulation studies [9].

### The Price-Control Protocol

During Level 2/3 events, the emergency council activates price controls on critical goods (food, fuel, water, medication) at 150% of pre-emergency reference prices. Price controls prevent opportunistic hoarding and maintain social cohesion. Enforce with the graduated sanctions above. This is pre-agreed in the town charter; the emergency council does not need to debate it during the crisis.

---

## Section 4: Medical Surge Capacity and Triage

### The Rural Medical Gap

Rural communities in the Midwest face a structural medical challenge: the nearest hospital may be 30–60 miles away under good conditions. During extended grid outage, road impassability, or fuel shortage, that gap can become uncrossable. The 2020 Iowa derecho left many rural communities without passable roads for 48–72 hours [6]. A community that depends entirely on evacuation-to-hospital for medical emergencies will lose people in those 48–72 hours.

The clinic-level infrastructure for a 50-household community is described in `household/06-community-scale-overview.md`. This section addresses what happens when the clinic operates beyond its normal capacity — when the community faces a mass casualty event or sustained medical system stress during an infrastructure failure.

### Surge Capacity Architecture

**Normal clinic capacity** (baseline): 1 medical professional, 5–8 first responders, supply cache for ~30 days of routine care.

**Surge Level 1** (2–5 acute patients simultaneously, normal equipment):
- Clinic director and 2 first responders on duty
- Remaining first responders on standby
- Priority to acute cases; elective or chronic-management visits postponed
- Monitoring of chronic disease registry patients increases to daily check-in

**Surge Level 2** (6–15 patients, sustained event):
- All trained responders activated
- Clinic expands into adjacent space (pre-designated: community center or church hall with clinic overflow supplies pre-positioned there)
- Triage activated (SALT protocol — see below)
- Logistics Officer prioritizes fuel for clinic generator above all other uses
- Medication rationing protocol activates: prescriptions reviewed for dose adjustment where clinically appropriate

**Surge Level 3** (15+ patients, mass casualty or extended crisis):
- Immediate request for external assistance via ham radio / Winlink to county emergency management
- Expectant category established in triage (patients for whom care would consume resources needed to save others who have higher probability of survival)
- Community volunteers (non-medical) assigned to: patient transport, family communication, supply running, documentation
- Emotional support and mental health function activated — assign a rotating counselor role (a trusted community member with pastoral or social work background) to support families of patients

### SALT Triage Protocol

SALT (Sort, Assess, Lifesaving Interventions, Treatment/Transport) is the CDC-endorsed mass casualty triage protocol, developed by consensus of the Federal Interagency Committee on Emergency Medical Services and adopted by most state EMS systems [10].

**Step 1: SORT** — Global sorting before individual assessment
- Command responders to walk if they can: those who can walk are "Minor" (green tag) — move to collection point
- Call for anyone who can wave or follow simple commands: those who respond but cannot walk are assessed next
- Those who do not respond are assessed last (highest resource need or lowest priority)

**Step 2: ASSESS** — Rapid individual assessment of each patient
For each non-ambulatory patient, assess in sequence:
1. Lifesaving interventions first (control massive bleeding with tourniquet, open airway — do these immediately, takes <30 seconds)
2. Respiratory rate: >30 breaths/min or <10 breaths/min = Immediate
3. Pulse: uncontrolled hemorrhage or no pulse = Expectant or Dead
4. Mental status: cannot follow simple commands = Immediate

**Triage categories** (standard color coding):
- **Red (Immediate)**: Life-threatening but survivable with immediate intervention. Seen first.
- **Yellow (Delayed)**: Serious but not immediately life-threatening. Can wait 30–60 minutes.
- **Green (Minor)**: Walking wounded. Self-care or minimal assistance. Can wait.
- **Black (Expectant/Dead)**: Either deceased or injuries incompatible with survival given available resources.

**Step 3: LIFESAVING INTERVENTIONS** — Before transport or further assessment:
- Tourniquet for massive extremity hemorrhage (apply within 2 minutes of assessment)
- Airway positioning (recovery position) for unconscious with airway
- Needle decompression for tension pneumothorax (only by trained provider)
- Two doses of auto-injector antidote for chemical exposure (only in chemical event)

**Step 4: TREATMENT/TRANSPORT**
Treat in place or transport in priority order: Red first, Yellow second, Green last.

### Training Requirements for SALT

Every trained first responder (EMT and WFR level) in the community should complete:
- SALT Mass Casualty Triage online training (free, 22-minute video + downloadable materials from the National Disaster Life Support Foundation) [11]
- Annual triage drill using simulated patients (use community members as actors; assign tags based on scenarios)

A community of 50 households should have at least 2 people trained to Triage Officer level — the people who call the categories and direct triage flow. The remaining first responders execute the interventions.

### Specific Medication Protocols for Extended Outage

During extended outages when pharmacies and hospitals are inaccessible, the clinic manages a limited formulary. Pre-agreed protocols (written and signed off by the clinic director before any emergency) cover:

**Insulin-dependent diabetes**: Insulin must be kept refrigerated (2–8°C). During power outage, a sealed cooler with ice (changed every 24–48 hours from community ice supply) maintains adequate temperature for up to 7 days. At room temperature (below 25°C), opened insulin vials remain effective approximately 28 days [12]. Clinic director monitors all insulin-dependent patients daily; prioritizes generator power for clinic refrigerator regardless of tier.

**Antibiotic stewardship**: Community antibiotic supply (amoxicillin, doxycycline, azithromycin, trimethoprim-sulfamethoxazole) is clinic-controlled. No self-administration without clinic director review. Indication-specific protocols written in the clinic protocol book (reference: Sanford Guide to Antimicrobial Therapy, physical copy in clinic library).

**CPAP-dependent patients**: A list of all CPAP-dependent patients is in the chronic disease registry. During power outages, the clinic coordinates with the energy system operator to ensure these patients have either a battery backup or access to a powered location. Positional sleep therapy (side sleeping) reduces but does not eliminate apnea risk as a bridge measure.

---

## Section 5: Shelter and Mass Care Coordination

### When People Must Move

Two scenarios drive shelter consolidation in a Zone 5 Midwest community:
1. **Winter extended outage**: Households cannot maintain safe indoor temperatures without heating backup; consolidation into designated warming shelters is necessary
2. **Natural disaster displacement**: Tornado, flood, or structural fire makes some households uninhabitable

In either case, the community needs pre-designated shelters, a process for opening and operating them, and a system for tracking who is where.

### Designating Warming Shelters

A warming shelter requires:
- A large, insulated structure (community center, church, school gymnasium, large barn)
- A functional wood stove or fireplace capable of heating the main space, with fuel supply
- Sanitation (working toilets or a pre-positioned composting toilet setup with privacy)
- Sleeping capacity: cots, mats, or floor space (calculate 40 square feet per person minimum)
- Backup lighting (battery or generator)
- 72-hour food and water supply for maximum expected occupancy

Target for a 50-household, 125-person community: 3–4 designated warming shelters totaling sleeping capacity for 80% of the population (100 people), geographically distributed across the town so no cluster is more than 0.5 miles from a shelter.

**Pre-position at each shelter** (stored on-site year-round):
- 20 cots or sleeping mats
- 5 LED lanterns + batteries (replaced annually)
- 72-hour food supply: canned goods, crackers, peanut butter (enough for 20 people × 3 days)
- 30 gallons of water in sealed containers (replaced annually)
- First aid kit (standard community level)
- Paper sign-in roster forms
- Printed copy of shelter protocol and emergency contact list

### Operating the Shelter

**Shelter Manager** (designated for each shelter, with backup):
- Opens shelter within 2 hours of Level 3 declaration
- Maintains sign-in roster: name, household, any medical needs, contact information
- Transmits roster to Logistics Officer within 6 hours of opening
- Coordinates feeding schedule with food hub
- Manages overnight operations: noise/light discipline, fire watch for wood stove

**Sign-In and Accountability**:
Every person who enters a shelter signs in. Every person who leaves signs out. The shelter manager transmits updated roster to the Logistics Officer twice daily. The Logistics Officer cross-references against the cluster headcount reports to identify anyone unaccounted for. Missing persons are reported to the IC within 2 hours of being identified as missing.

**Vulnerable Population Protocols**:
- Elderly and mobility-impaired: cots positioned near stove and accessible to toilet; cluster steward checks in 3x daily
- Infants and young children: designated quiet area with sleeping space; parent/caregiver always present
- Individuals with mental health needs: flagged in registry (with consent); assigned a consistent point-of-contact among shelter staff

### Mass Feeding

The food hub steward coordinates feeding at all active shelters during Level 2/3 events. Feeding protocol:

**Caloric targets** (per Section 3 resource allocation tiers):
- Cold exposure increases caloric need by 200–400 calories/person/day [13]
- Workers doing physical labor (firewood, infrastructure repair, water hauling) require additional 20%
- Adjust allocations accordingly; document adjustments in the incident log

**Meal schedule**:
- 3 meals/day at warming shelters; food hub prepares bulk and delivers or provides raw materials for on-site cooking
- Hot meals where possible (morale matters in extended events); cold meals (bread, peanut butter, canned goods) as fallback
- Community kitchen setup at the primary warming shelter (if kitchen equipment available) allows cooking for all shelters from one location

**Dietary considerations**:
- Clinic director maintains a list of severe food allergies from the chronic disease registry; the food hub steward receives a summary (no names, just allergens and count)
- Religious dietary restrictions: accommodate where possible; communicate constraints to community honestly

---

## Section 6: Midwest-Specific Scenarios and Pre-Plans

### Scenario 1: Extended Winter Grid Outage (7–14+ Days)

*Trigger*: Major ice storm or blizzard in January–February takes down regional grid.

**Hours 0–4 (monitoring)**:
- IC and Communications Officer establish contact
- Ham radio net checks in; cluster stewards begin monitoring household status
- NOAA receiver monitored continuously
- Generator fuel inventory checked

**Hours 4–48 (Level 2 activation)**:
- Emergency council convenes at command post
- Warming shelter #1 opens (the best-heated building in town); Shelter Manager activates
- Load-shedding begins: residential electricity cut to critical loads only; clinic generator runs full-time
- Food hub shifts to high-calorie, shelf-stable production; reduces fresh/perishable processing
- Chronic disease registry patients contacted; insulin and CPAP status confirmed
- Firewood inventories confirmed at all warming shelters

**Days 2–7 (stabilization)**:
- Twice-daily community status update posted at command post
- Ham radio check-in with county emergency management twice daily
- Fuel consumption tracked against 30-day reserve
- If temperatures drop below -10°F or wind chill below -30°F: consolidate all vulnerable residents to warming shelters immediately (no overnight stays at isolated households without adequate backup heat)

**Days 7–14+ (extended operations)**:
- Evaluate external assistance request: if grid restoration >14 days, formal request through county EM
- Water system: if grid-fed pumps fail, switch to gravity distribution from elevated tanks; hand delivery if tanks depleted
- Mental health support activation: community gatherings at warming shelters (storytelling, music, games) reduce stress and social isolation

### Scenario 2: May Tornado + Infrastructure Damage

*Trigger*: F2+ tornado damages structures including water tower, grain bin, or communication infrastructure during late May.

**Immediate (0–2 hours)**:
- All residents shelter in place at nearest below-grade shelter (protocol from `midwest/extreme-weather.md`)
- IC and Communications Officer establish contact after tornado has passed
- Cluster stewards conduct rapid welfare check of all cluster households; report missing to Operations within 1 hour
- Medical Officer activates Surge Level 1; triage of any injured

**Hours 2–12 (damage assessment)**:
- Structured damage assessment team (2-person teams with ham radios) walks each cluster systematically
- Priority assessment: structural damage to inhabited buildings, infrastructure damage (water system, power lines, food storage), road and access routes
- Document with photographs and written log; report to IC via radio
- Operations assigns debris removal teams (chainsaw operators, hand crews) by priority

**Hours 12–48 (recovery initiation)**:
- Damaged grain bins or food storage: immediate mobilization of food hub to preserve what can be salvaged; damaged produce can be processed within 24–48 hours
- Structural damage to inhabited buildings: temporary shelter consolidation until assessed and repaired or condemned
- Communication infrastructure: repair or reroute; ham radio net provides backup for any failed infrastructure

**Days 2–14 (rebuilding)**:
- Barn-raising protocol (see `03-mutual-aid-networks.md`): community labor mobilized for repair of damaged structures
- Mutual aid request to neighboring communities if damage exceeds local repair capacity
- County building inspector contacted (non-emergency channel) for structural assessment of damaged buildings

### Scenario 3: Spring Flooding + Supply Chain Disruption

*Trigger*: River flooding (March–May) makes main road impassable for 3–7+ days simultaneously with supply chain disruption (fuel, medicine, food).

**Immediate**:
- Water source assessment: if surface water sources are contaminated by flood, switch to stored/well water; treat all surface water as contaminated
- Road status: identify passable alternate routes; communicate to all households via ham radio and status board
- Resource register review: identify what cannot be resupplied during road closure and calculate days of supply

**Sustained**:
- Fuel conservation: non-essential vehicle use suspended; fuel allocated to medical transport, emergency response, water system operation only
- Supply priority if any vehicle access becomes available: insulin and critical medications first, fuel second, food third

---

## Section 7: After Action Review

After every Level 2 or Level 3 activation (and after every training exercise), the IC convenes an After Action Review (AAR) within 7 days of incident resolution. The AAR follows a structured format:

1. **What was planned**: Review the protocol that was supposed to be followed
2. **What happened**: Factual account from each section chief (Operations, Logistics, Medical, Communications)
3. **What went well**: Identify and reinforce successful practices
4. **What went wrong**: Without blame — identify process failures, resource gaps, communication breakdowns
5. **What changes**: Specific, assigned, time-bound improvements to protocols, equipment, or training

The AAR report is added to the incident documentation file and reviewed at the next annual community preparedness meeting. It feeds directly into protocol revisions and training updates for the next year.

---

## Bullet-Point Summary (for cross-referencing)

- Command structure: simplified ICS (IC + Operations + Logistics + Medical + Communications + Documentation), activated at 48-hour grid outage or simultaneous multiple failures
- Communication stack: in-person/foot messenger → VHF ham radio (4+ licensed operators, 1 base station) → NOAA receiver → Winlink digital
- Resource allocation: pre-agreed 4-tier rationing system (Normal → Tier 1/2/3 based on days of supply); price controls at 150% of pre-emergency price during Level 2/3
- Priority populations: insulin-dependent diabetics, infants, pregnant women, elderly — tracked in chronic disease registry; allocation adjusted upward
- Medical surge: SALT triage protocol; surge capacity levels 1–3 with pre-designated overflow space; clinic director has clinical authority independent of IC
- Warming shelters: 3–4 pre-designated buildings with pre-positioned supplies; 80% community sleeping capacity; sign-in roster transmitted twice daily to Logistics
- Training: annual tabletop, quarterly radio drill, biennial full activation; all IC/council/stewards complete FEMA IS-100 at minimum
- After Action Review: within 7 days of every activation or exercise

---

## Integration Notes — Connection to Phase 1 and Phase 2

| This Document Section | Connects To |
|---|---|
| Command structure (Section 1) | `household/06-community-scale-overview.md` Section 1 (governance) — extends selectboard to ICS |
| Communication network (Section 2) | `household/06-community-scale-overview.md` Section 4 (Midwest threats) — ham radio pre-positioned |
| Resource allocation (Section 3) | `household/04-energy-coordination.md` (load shedding tiers) — same tier logic scaled up |
| Medical surge (Section 4) | `household/05-healthcare-coordination.md` (cluster medical hub) — scales up to surge protocol |
| Medical: insulin protocols | `individual/05-healthcare.md` (medication management) — extends to community storage |
| Warming shelters (Section 5) | `household/01-household-coordination-overview.md` (cluster emergency protocol) — scales up |
| Scenario: winter outage | `midwest/extreme-weather.md` (polar vortex and ice storm protocols) — community version |
| Scenario: tornado | `midwest/extreme-weather.md` (tornado response) — community coordination layer added |

---

## Primary Sources

[1] Blue Lake Rancheria Tribe Sustainability and Resilience Department. "Microgrid Performance During 2019 PSPS." Blue Lake Rancheria, 2019. Available: https://www.bluelakerancheria-nsn.gov/departments/sustainability-and-resilience/

[2] Mutual Aid Disaster Relief. "Emerge Puerto Rico / Proyecto Apoyo Mutuo." https://mutualaiddisasterrelief.org/co-conspirators/proyecto-de-apoyo-mutuo/

[3] FEMA. "National Incident Management System, Third Edition." October 2017. https://www.fema.gov/sites/default/files/2020-07/fema_nims_doctrine-2017.pdf

[4] FEMA Emergency Management Institute. "IS-317: Introduction to Community Emergency Response Teams." https://training.fema.gov/is/courseoverview.aspx?code=IS-317.a

[5] CISA. "Surviving a Catastrophic Power Outage." NIAC Study, January 2023. https://www.cisa.gov/sites/default/files/2023-01/NIAC%20Catastrophic%20Power%20Outage%20Study_FINAL.pdf

[6] Characterizing the 2019 Midwest Flood: A Hydrologic and Socioeconomic Perspective. *Weather, Climate, and Society*, 15(3), 2023. https://journals.ametsoc.org/view/journals/wcas/15/3/WCAS-D-22-0065.1.xml

[7] ARRL Amateur Radio Emergency Service (ARES). http://www.arrl.org/ares

[8] Chicago Booth Review. "How to Ration Scarce Resources Fairly." https://www.chicagobooth.edu/review/how-ration-scarce-resources-fairly

[9] Multiperiod Equitable and Efficient Allocation Strategy of Emergency Resources Under Uncertainty. *International Journal of Disaster Risk Science*, 2022. https://link.springer.com/article/10.1007/s13753-022-00437-y

[10] SALT Mass Casualty Triage Algorithm. HHS Chemical Hazards Emergency Medical Management. https://chemm.hhs.gov/salttriage.htm

[11] National Disaster Life Support Foundation. SALT Mass Casualty Triage On-Line Training. https://www.ndlsf.org/salt

[12] American Diabetes Association. Insulin Storage and Syringe Safety. (Referenced in `individual/05-healthcare.md`)

[13] Caloric adjustment for cold exposure: Referenced in `household/06-community-scale-overview.md` Section 4, citing Petzoldt (NOLS Wilderness Medicine) thermal regulation guidelines.

[14] FEMA. "Mass Care and Shelter." Kansas City Metropolitan Area Regional Coordination Guide ESF 6. https://www.marc.org/sites/default/files/2022-03/RCG_ESF6_Mass_Care.pdf

[15] Rural Health Information Hub. "Emergency Preparedness and Response for Mass Casualty Incidents." https://www.ruralhealthinfo.org/toolkits/emergency-preparedness/4/mass-casualty-incidents

[16] Frontiers in Water. "Infrastructure Interdependency Failures From Extreme Weather Events as a Complex Process." 2020. https://www.frontiersin.org/journals/water/articles/10.3389/frwa.2020.00021/full

[17] EPA. "Power Resilience Guide for Water and Wastewater Utilities." 2019. https://www.epa.gov/sites/default/files/2016-03/documents/160212-powerresilienceguide508.pdf
