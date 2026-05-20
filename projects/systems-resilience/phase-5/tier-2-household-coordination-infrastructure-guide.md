---
title: "Household Coordination Infrastructure Guide"
project: systems-resilience
region: "Midwest US (Zone 5)"
phase: 5
tier: 2
dimension: 1
scale: household
scale_range: "8–25 people"
created: 2026-05-20
word_count: ~7200
citation_count: 28
status: first-draft
dependencies:
  - individual/01-water.md
  - individual/02-food.md
  - individual/03-shelter.md
  - individual/04-energy.md
  - individual/05-healthcare.md
  - individual/06-agriculture.md
  - household/01-household-coordination-overview.md
  - household/03-food-coordination.md
  - household/04-energy-coordination.md
  - phase-3/01-governance-decision-making.md
  - phase-3/02-food-systems-supply-chain.md
  - phase-3/03-information-infrastructure.md
  - phase-3/04-security-and-defense.md
  - phase-3/05-scaling-pathways-and-thresholds.md
follow_up:
  - phase-5/tier-3-community-coordination-framework.md
  - phase-5/tier-2-veterinary-care-guide.md
  - phase-5/tier-2-psychological-support-guide.md
---

# Household Coordination Infrastructure Guide
> **Region**: Midwest US (Zone 5) | **Scale**: 8–25 people (one household unit)
> **Phase**: 5 — Bridge Layer | **Tier**: 2 — Household Coordination
> **Dependencies**: [Tier 1 individual documents](../individual/) · [Phase 3 community domains](../phase-3/)
> **Forward reference**: [Tier 3 community coordination](./tier-3-community-coordination-framework.md)

---

## The Most Important Finding

The biggest failure mode in household resilience planning is not inadequate supplies. It is the absence of coordination infrastructure before those supplies are needed. A household of 15 people with six months of food, a water system, and a solar array will disintegrate under extended stress without a functioning governance framework, documented role assignments, and practiced conflict resolution. The same household with half the supplies but a working decision-making structure will adapt, improvise, and survive.

This document bridges the gap identified in the Phase 4 synthesis: Phase 1 covers individual capability, Phase 3 covers community scale (100+), and neither addresses the household (8–25 people) as a coordination unit. That unit is where most practical resilience planning actually begins — and where it most often breaks down.

The evidence from long-running intentional communities confirms this: Twin Oaks (100 people, 55+ years continuous operation) and East Wind (75 people, 50+ years) survive not because they have more land or more tools than comparable groups, but because they have governance structures that distribute authority without fragmenting it, and conflict resolution mechanisms that de-escalate before disputes become community-threatening. [1][2] The same principles apply at household scale with fewer structural complications and a lower implementation burden.

---

## Section 1: Bridge Architecture — From Individual to Community

### What the Household Scale Is

The household coordination unit in this framework is not a single dwelling. It is the decision-making and resource-sharing unit that sits between an individual and a formal community. In practice this takes three forms:

**Nuclear-family household (4–6 people)**: Blood relatives in a single dwelling. The smallest viable resilience unit. Extreme vulnerability to individual failure (illness, injury, death removes 20–25% of capacity). Requires outside connections — a 4-person household attempting full autonomy is a single-point-of-failure system.

**Extended-family household (8–15 people)**: Multiple generations or related family units sharing a property or adjacent parcels. The modal household for intentional rural resilience. Has enough labor diversity to support 24-hour watch rotations, specialized food production, and role separation without over-relying on any individual. The reference scenario throughout this document.

**Chosen-family household (10–25 people)**: Unrelated individuals who have formed a deliberate community — a small intentional community, a cooperative farmstead, or a neighborhood cluster that has moved toward shared infrastructure. Has the most complex governance requirements but the greatest skill diversity and labor pool.

All three types benefit from the same coordination infrastructure. The complexity scales with headcount; the structure is identical.

### Why Household Coordination Is the Critical Middle Layer

Phase 3's scaling analysis establishes that the 150-person Dunbar threshold is the key transition point for community governance. [3] But 150 people is 6–10 households. The threshold is approached household by household. The question for any forming community is not "how do we govern 150 people?" — it is "can each of our constituent households coordinate internally well enough to be a reliable node in a community?"

A community built from internally coherent households can federate upward. A community trying to simultaneously build internal household structure and inter-household coordination under crisis conditions fails at both.

The practical implication: household coordination infrastructure should be operational before community-scale coordination is attempted. The Phase 3 governance document establishes that you cannot improvise governance under contested authority. The same is true at household scale, at lower stakes and with more opportunity to correct before crisis.

### Decision Architecture: Household vs. Community Level

Not every decision should go to the household assembly. A working decision architecture separates three tiers:

**Individual-discretion decisions**: Personal schedule, personal health management, personal relationships outside the household. No household review required.

**Household-domain decisions** (handled at household level):
- Internal resource allocation (food, water, energy, medical supplies)
- Role assignments and labor scheduling
- Internal conflict resolution (first two escalation steps)
- Onboarding of new members
- Security posture within the household perimeter
- Day-to-day procurement and inventory management

**Inter-household / community decisions** (refer upward to community coordination):
- External relationships and trade agreements
- Security coordination with adjacent households or community
- Surplus sharing or emergency resource transfer
- Decisions affecting more than one household
- Issues that household conflict resolution cannot resolve internally

This tiered structure matters because it prevents two failure modes: households that refer everything externally (creating dependency and paralysis at community scale) and households that never refer externally (creating isolation and resource hoarding).

---

## Section 2: Household Governance Framework

### The Core Design Principle

Household governance fails in two predictable ways: charismatic authority (one strong personality makes all decisions, creating a single point of failure and resentment from others) and paralytic consensus (nothing can happen without universal agreement, so contentious decisions never get made). The evidence from intentional communities is that neither extreme works under extended stress. [4]

The model that works at 8–25 person scale is **domain-specialist authority with assembly override**. Each domain (food, water, energy, security, health, communication) has one designated coordinator who holds operational authority within their domain. Major decisions — those affecting multiple domains, community resources, or significant risk — require assembly review. The assembly can override any specialist decision by a defined majority.

This is structurally similar to Twin Oaks' manager system [1] and East Wind's managerial authority framework, [2] scaled down to household requirements.

### Role Structure

Every household should designate the following roles before a crisis requires them. Roles are not permanent assignments — they rotate (see below) — but at any given time, these functions must have identified owners:

**Coordinator**: Calls meetings, tracks decisions in the household log, ensures follow-through, and serves as the primary contact for external communication. Has no special authority over substantive questions. Can be recalled by the assembly.

**Food Manager**: Manages food inventory, meal planning, procurement decisions, and preservation scheduling. Authorizes routine food expenditures. Major inventory decisions (consuming emergency reserves, changing the 6-month rotation plan) require assembly approval.

**Water/Sanitation Manager**: Manages water storage, filtration systems, and sanitation protocols. Has authority to restrict water use during shortage. Reports weekly on reserves.

**Energy Manager**: Manages fuel, solar/battery systems, generator protocols, and energy rationing decisions. Controls energy allocation during scarcity periods.

**Medical Coordinator**: Manages medical supplies, tracks household health status, and serves as first responder for medical events. Does not need to be a clinician — this role is primarily logistical.

**Security Coordinator**: Manages watch rotation schedules, access control protocols, and external communication regarding security threats. Coordinates with adjacent households on shared early-warning systems.

**Communications Coordinator**: Manages radio equipment, maintains the household information system (log, procedures manual, skill inventory), and handles information security.

Households of 8–12 people typically need one person holding 2–3 roles. Households of 15–25 people can assign each role to a different individual. The goal is that no single person holds more than 3 roles — above that, the failure risk of losing one person becomes critical.

### Meeting Cadence

**Weekly household meeting (30–45 minutes)**: Domain managers report on their domain status. Open agenda items are addressed. A note-taker records decisions in the household log. Quorum: 75% of resident adults. No quorum, no binding decisions.

**Monthly review meeting (90 minutes)**: Full inventory review across all domains. Role performance review (is each coordinator doing what they said they would do?). Rotation decisions. Strategic planning for the upcoming month. External coordination status (what is the household's relationship with adjacent households and community?).

**Emergency convening (immediate)**: Any household member can call a full-household meeting for issues that require immediate collective decision. The coordinator facilitates. Emergency decisions made with quorum (75%) are binding. Decisions made without quorum are provisional — they bind for up to 72 hours and must be ratified at the next full meeting.

### Consensus Models for Household Scale

Unanimous consensus works at 4–6 people and fails above that. Not because people become less cooperative, but because the probability that one person will block a necessary decision increases with each additional member. Under crisis conditions, blocked decisions become dangerous.

The recommended model for 8–25 person households is **modified consent** (distinct from consensus): a proposal moves forward if no one raises a *reasoned objection* — one that cites a specific harm to the household's ability to function. Objections based on personal preference ("I don't like this") do not block; objections based on operational concerns ("this will exhaust our fuel reserve before the next resupply window") do. [5]

Thresholds for specific decision types:
- **Routine operational decisions** (daily/weekly): Domain coordinator authority, no meeting required
- **Domain-significant decisions** (affects resources or risk): Modified consent, weekly meeting
- **Constitutional decisions** (role changes, new members, emergency reserve expenditure): Two-thirds majority at monthly meeting
- **Emergency decisions**: Simple majority with quorum, 72-hour provisional validity

### Conflict Resolution

The Phase 3 security document establishes that internal conflict — not external threat — is the dominant security burden after the first two weeks of extended disruption. [6] Household-scale conflict is the raw material of community-scale conflict. De-escalation at household level prevents escalation to community level.

The intentional community literature consistently identifies the same failure pattern: conflicts are suppressed to maintain harmony, resentment accumulates underground, and the conflict explodes during a crisis when de-escalation capacity is lowest. [4] The solution is not to prevent conflict but to give it legitimate channels before it goes underground.

**Four-step resolution protocol** (adapted from community living practice [7]):

**Step 1 — Direct conversation**: The involved parties attempt resolution privately. Both parties are expected to state their concern in terms of impact ("when X happens, I am unable to do Y") rather than attribution ("you always do X"). Resolution requires no household involvement. If resolution is not reached within 48 hours, escalate.

**Step 2 — Facilitated conversation**: A third household member (not a partisan of either side) facilitates a structured conversation. The facilitator's role is to ensure both parties are heard and to help articulate what resolution would look like. Not a judge. If resolution is not reached, escalate.

**Step 3 — Domain coordinator review**: If the conflict involves a domain (food allocation, energy priority), the relevant domain coordinator reviews it as an operational matter. The coordinator makes a decision that is subject to assembly appeal. This step converts personal conflict into an operational question where domain expertise and household policy apply.

**Step 4 — Full assembly review**: The assembly convenes with the conflict framed as a governance question: does the household need to change its policy, its role assignments, or its membership composition? The assembly decides by two-thirds majority. This step is rare in functional households but must be available and known to all members.

**The line to draw**: Conflict resolution handles disagreements about decisions and policies. If a household member poses a physical threat or engages in repeated coercive behavior, that is a membership issue, not a conflict resolution issue. Membership termination requires two-thirds majority and must be documented with specific behavioral cause.

### Leadership Rotation vs. Expertise-Based Authority

The debate in intentional community practice between leadership rotation (everyone eventually holds every role) and expertise-based authority (the most skilled person holds each role) resolves differently at household scale than at community scale.

For a 15-person household, the correct model is **expertise-primary with mandatory apprenticeship**. The most qualified person manages the water system; a designated apprentice shadows them and can take over if the primary is incapacitated. Role rotation happens at 12-month intervals unless the outgoing coordinator requests extension and the assembly approves. The apprentice becomes the primary; the previous primary becomes a senior resource.

The apprenticeship requirement prevents the worst single failure mode in household governance: institutional knowledge residing in one person who leaves.

### The Household Decision Log

Every binding decision gets a log entry. Format:

```
Date | Topic | Decision Made | Vote (if applicable) | Who Accountable | Review Date
```

The log lives in the household's physical binder (printed, not digital — the log must survive grid failure) and has a designated keeper (the Coordinator). All household members have read access. The log is reviewed at each monthly meeting and decisions without documented follow-through are flagged.

This is not bureaucracy for its own sake. It is the institutional memory system that prevents disputes about "what we decided" from consuming governance bandwidth that should go toward decisions about "what to do next."

---

## Section 3: Household Food Systems Coordination

### Baseline Caloric Planning for 8–25 People

At household scale, food planning begins with a caloric floor: how many calories per day does this household need to sustain baseline function, and how long can it sustain that floor from stored supply?

**Reference figures for Zone 5 Midwest**:
- Adult working moderate labor: 2,200–2,800 calories/day
- Adult light activity: 1,800–2,200 calories/day
- Child (under 12): 1,200–1,800 calories/day
- Pregnant/nursing adult: add 300–500 calories/day

For a 15-person household (12 adults, 3 children), a conservative daily caloric requirement is 28,000–32,000 calories/day, or approximately 8.4–9.6 million calories for a 90-day supply and 16.8–19.2 million calories for a 180-day supply.

Caloric density of common storage foods (dry weight):
- White rice: 1,600 calories/pound
- Dried beans: 1,500 calories/pound
- Hard wheat berries: 1,500 calories/pound
- Rolled oats: 1,700 calories/pound
- White sugar: 1,730 calories/pound
- Vegetable oil: 3,500 calories/pound (most calorie-dense, best stored in airtight sealed containers)

A 90-day caloric supply for 15 people requires approximately 5,300–6,000 pounds of shelf-stable food at mixed caloric densities. This is achievable with a dedicated storage room (20' x 12' x 8' space holds approximately 8,000 lbs in organized shelving) and $4,000–$8,000 in procurement cost at current prices.

### Role Assignments: The Four Food Functions

**Procurement Manager**: Sources all external food. Maintains relationships with local farms, seed suppliers, and bulk food distributors. Manages the annual procurement calendar (bulk grain purchase in October when prices are lower; seed orders in January; livestock procurement in spring). Controls food budget. Reports to Food Manager.

**Storage Manager**: Maintains the physical inventory. Implements FIFO (first-in, first-out) rotation — older items to the front, newer items behind. [8] Conducts monthly inventory counts against the household log. Flags items approaching expiration. Manages the root cellar calendar (what goes in when, what comes out when).

**Meal Coordinator**: Plans the weekly meal schedule for the entire household. Balances nutrition, caloric adequacy, palatability, and inventory rotation. Coordinates with Storage Manager on what is approaching depletion. In disruption scenarios, scales meals down according to an approved rationing protocol rather than improvising.

**Preservation Specialist**: Manages all food processing: canning, fermenting, dehydrating, smoking, root cellar storage. Coordinates the preservation peak (August–October in Zone 5) when tomato harvest, corn, beans, squash, and root vegetables all require processing within narrow windows. Maintains equipment (pressure canner, dehydrator, fermentation crocks, chest freezers).

For households below 12 people, one person may hold multiple food functions. The Food Manager role (Section 2) holds accountability for the overall food system; these four functions are operational sub-roles that can be distributed.

### 6-Month Supply Rotation Protocol

A 6-month supply that is not rotated becomes a 6-month supply that expires unnoticed and is replaced at emergency cost under pressure. Rotation requires discipline, not complexity.

**Monthly rotation protocol**:
1. Storage Manager conducts physical count on the 1st of each month (30 minutes)
2. Items expiring within 60 days move to "active use" shelf — these are consumed in the next two months before the new stock replaces them
3. New procurement (fresh produce, preserved items from harvest) enters rear of shelving
4. Inventory log updated with new quantities and oldest expiration dates
5. Food Manager receives monthly report: current days-of-supply at current consumption rate

**Minimum viable 6-month inventory for 15 adults** (stored calories only; does not include fresh production):
- Rice: 800 lbs
- Dried beans (mixed): 600 lbs
- Hard wheat or cornmeal: 600 lbs
- Rolled oats: 300 lbs
- Vegetable oil (sealed): 80 lbs
- Sugar or honey: 150 lbs
- Salt: 50 lbs
- Canned goods (vegetables, protein): 400–600 cans
- Preserved/dehydrated items from previous harvest: variable

This inventory totals approximately 9–10 million calories at conservative estimates — roughly 180 days at 2,200 calories/person/day for 15 people. Zone 5 harvest season (May–October) supplements this with fresh production; the inventory is the floor, not the ceiling.

### Seasonal Labor Coordination

Zone 5 Midwest food production demands are not evenly distributed across the year. The labor calendar:

**January–March**: Seed inventory, seed order, equipment maintenance, indoor seed starting (February–March). 2–4 hours/week household food labor.

**April–May**: Transplanting, early direct seeding, soil preparation, cold-frame management. 10–15 hours/week.

**June–July**: Cultivation, irrigation, harvest of early crops (peas, salad greens, early beans). 8–12 hours/week.

**August–October**: Peak preservation season. Simultaneous harvest, processing, and preservation across all major crops. 25–35 hours/week for the full household. This is the period where labor coordination is most critical — all preservation functions are sequential-path-critical (tomatoes must be processed within days of ripeness; corn cannot wait). The Preservation Specialist must have pre-committed labor from the full household for this window.

**November–December**: Root cellar monitoring, fermentation management, equipment cleaning, planning for next year. 3–5 hours/week.

The household food labor budget: roughly 800–1,200 hours/year for a 15-person household maintaining a full garden and preservation operation. That averages 55–80 hours/person/year, or roughly 1–1.5 hours/person/day during the growing season and much less in winter. This is compatible with other household functions if labor is coordinated and the August–October peak is staffed appropriately.

### Supply Chain Relationships

The Phase 3 food document establishes that community-scale food resilience depends on relationships with local farms, regional food hubs, and direct supply chains that bypass concentrated processing nodes. [9] The same principle applies at household scale, at smaller volume and lower complexity.

Household supply chain priorities:
- **Seed supplier relationship**: One or two seed companies with heirloom/open-pollinated varieties. Annual order placed in January. Backup: household seed saving (see individual/06-agriculture.md).
- **Bulk grain source**: Local grain elevator or regional organic grain supplier. Bulk purchase in October post-harvest when prices are lower. Minimum: 500 lbs per purchase for price efficiency.
- **Local farm relationships**: 2–3 farms within 30 miles providing produce, livestock, or eggs at direct-purchase prices. These relationships take years to develop — they should be established before they are needed.
- **Equipment parts network**: Know where spare parts for critical food equipment (pressure canner gaskets, dehydrator mesh, water bath canner lids) are available locally. Major distributors ship within days under normal conditions; a local hardware store relationship matters when shipping is disrupted.

---

## Section 4: Household Information Infrastructure

### Communication in Three Failure Modes

Following the three-layer architecture documented in Phase 3 [10], household communication must be functional at three levels of infrastructure failure:

**Normal disruption (internet and cell down, grid power present)**: GMRS radio is the household primary communication layer. A $35 FCC household license covers all immediate family members and is extended by community practice to chosen-family households. Minimum household radio kit: one GMRS base station with external antenna (installed at highest elevation point on the property — second story, barn roof, or water tower), plus one handheld per adult assigned to a watch or work role. Cost: $400–800 for a functional 15-person household kit. Channel assignments are pre-designated and posted in the household binder.

**Extended disruption (grid down, battery/solar available)**: AREDN mesh or LoRaWAN text-messaging provides data communication between the household and adjacent households or community nodes. At minimum, one AREDN node with a solar-charged battery backup extends the communication layer to low-bandwidth digital messaging. Cost: $200–400 per node including antenna and solar. Requires an amateur radio Technician license ($15 exam fee) for at least one household member.

**Severe disruption (all power uncertain, external reach needed)**: A portable HF shortwave receiver (receive-only, $100–300) allows the household to monitor FEMA emergency broadcasts, shortwave news from outside the affected region, and amateur radio emergency networks without transmitting. At least one household member holding a General class amateur radio license can transmit on HF, extending the household's reach to regional and national networks.

**Runner protocol** (zero electronics): If all electronic communication fails or is compromised, the household defaults to the runner system used in pre-electronic military and civil administration. Designated runners (typically the youngest physically able adults) carry written messages between household and community nodes on a defined schedule (morning, midday, evening). Messages are brief, on standardized forms, signed and dated. Runners use pre-agreed routes with pre-agreed checkpoints.

### Knowledge Preservation

The household's greatest knowledge vulnerability is the departure or incapacitation of a single person who holds critical operational knowledge in their head. A household where one person knows how to bleed the fuel lines and no one else does has a single point of failure that a wrench does not fix.

**Household knowledge system — three components**:

**1. The Printed Procedures Binder**: A physical binder (waterproof, duplicate copies in two locations) containing written procedures for every critical household operation: water system startup and shutdown, generator fuel sequence, solar system battery state-of-charge protocol, food preservation process for each major crop, medical emergency protocols, and radio communication procedures. Each procedure is written to be executed by someone who has never done it before. Plain language. Numbered steps. Updated whenever a procedure changes.

**2. The Skills Inventory**: A one-page list, updated at each monthly meeting, of who in the household has what skills. Format: skill category (medical, electrical, mechanical, agricultural, construction, communication, food processing, etc.) plus the name of the primary holder and the apprentice. If any skill has only one holder and no apprentice, that is flagged as a vulnerability and addressed at the next monthly meeting.

**3. The Household Log**: Described in Section 2. This is institutional memory for decisions, not for procedures. The log answers "what did we decide?" The binder answers "how do we do this?"

### Information Security

Not all household information should be communicated externally. The household holds sensitive information in several categories:

**Food and supply inventory**: The household's stock levels are potentially sensitive under scarcity. Knowing a household has six months of food is enough reason for a desperate group to target it. Policy: supply quantities are not discussed outside the household. When asked by outsiders, a non-specific response ("we have enough for now") is appropriate. Supply quantities shared with community coordination should be aggregate and context-specific (for mutual aid purposes, not for general knowledge).

**Security posture**: Watch schedules, observation post locations, and security protocols are household-internal. Even within a community, the specifics of one household's security arrangements are need-to-know.

**Medical records**: Individual health information is personal and should not be shared with community coordination without the individual's consent, except in medical emergencies.

**External communications policy**: The Communications Coordinator determines what information is transmitted over radio. Assume all GMRS and AREDN transmissions can be overheard. Default: communicate logistics (requests, confirmations, timing) not inventory or strategic information over radio.

---

## Section 5: Household Security and Defense Coordination

### The Actual Threat Profile

Phase 3's security document establishes what the evidence shows: in extended disruptions, the dominant security burden is not organized external raiders but desperate individuals and internal conflict. [6] A Midwest rural household's security posture should be calibrated to the actual threat landscape rather than the dramatized one.

**Weeks 1–2**: Most activity is opportunistic — people checking on neighbors, abandoned-property looting, search for information. External security posture: welcoming but observant. Information about who is moving, where, and why is valuable.

**Weeks 3–8**: Resource pressure increases. Individuals seeking food and supplies become more persistent. Organized groups moving through the region are possible but still uncommon. External security posture: access control at entry points. Not hostile — the goal is to know who is approaching and make deliberate decisions about engagement, not to repel all contact.

**Months 2+**: Extended disruption reveals which communities are stable and which are failing. Stable communities become targets for pressure from failing communities. Resource conflicts with adjacent households or communities are possible. External security posture: integrated with community-scale mutual defense network.

At every stage, internal conflict management (Section 2) is the primary security function. A 15-person household that resolves its governance disputes without escalation to physical threat has eliminated the leading cause of security incidents.

### Distributed Awareness: The Watch System

A household of 8–25 people cannot maintain continuous 24-hour watched perimeter. That level of security requires military-scale resources and degrades alertness-per-person rapidly. The realistic goal is **layered early warning** at three distances:

**Outer ring** (100–400 meters): Passive early warning systems — motion-triggered IR sensors wired to in-household alert lights or audio signals. These require no active monitoring. Battery-powered IR sensor kits ($50–200 per sensor) cover road access points, field edges, and trail approaches. When triggered, they alert the household without revealing that a watch is present.

**Middle ring** (30–100 meters): Visible deterrents and channeling. Natural barriers (dense plantings, fencing with gates), visible signage ("Private property — community members only"), and lighting at night indicate that the property is occupied and organized. Channeling means that the path of least resistance leads to a designated approach point rather than allowing unobserved approach from multiple directions.

**Inner ring** (0–30 meters): The entry control point. One designated approach to the main inhabited structures. The first contact with any unknown arrival happens here, by a designated household member who has been briefed on the contact protocol.

**Watch rotation for an extended disruption (15-person household)**:

A 24-hour cycle divided into 4-hour shifts requires 6 slots/day. For a 15-person household (12 capable adults), each adult stands watch approximately 4 hours every 2 days — roughly 14 hours/week of watch obligation per person. This is demanding but sustainable. Reduce to 8-hour shifts if your early-warning perimeter is reliable enough that you can afford lower alert sensitivity overnight.

Watch shift documentation: each watch maintains a log (time, anything observed, any contacts or events). The Security Coordinator reviews the watch log daily.

### Contact Protocol for Unknown Arrivals

When an unknown person or group approaches:

1. **Observe before engaging**: Use the outer ring early warning time to observe from cover. How many people? What are they carrying? What is their body language?
2. **Single contact point**: One designated household member (not a visible majority) makes first contact. This person is calm, not armed-visibly, and friendly. Their role is information gathering: who are they, where are they going, what do they need?
3. **Assess and decide**: Based on the interaction, the contact decides: (a) provide limited assistance and information (directions, a water refill), then disengage; (b) refer the person to community coordination for more significant requests; (c) signal the household for backup if the situation is threatening.
4. **Document every contact**: Name (if given), description, party size, stated need, response provided, time and date. This record is intelligence for community-wide awareness.

### Non-Kinetic Security Measures

The most effective household security measures are not weapons. They are information management, social relationship maintenance, and supply diversion.

**Information management**: Do not advertise food or supply quantities, generator sound levels, or security gaps. A household that appears adequately equipped but not notably well-supplied is a less attractive target than one that advertises abundance.

**Supply diversion**: If you have trade-surplus items (minor household goods, specific medical supplies, non-critical food), these can be shared with genuinely desperate individuals as a substitute for letting them know about your primary reserves. This is not charity — it is the cheapest possible security measure.

**Social relationships**: A household embedded in a network of known and trusting neighbors is dramatically safer than an isolated household. Community security is covered in Phase 3; at household level, the investment is maintaining 3–5 known relationships with adjacent households or community members who will vouch for your household in ambiguous situations.

**Obfuscation**: A household should not look like a tempting target from the outside. Vehicle count, light discipline (no obvious light from well-stocked storage areas at night), and verbal discipline (not discussing inventory in earshot of strangers) are all non-kinetic security measures.

---

## Section 6: Household Economic Coordination

### Resource Budgeting: The Household Balance Sheet

A household's economic function is to sustain 8–25 people through a defined period with defined inputs. Before any economic coordination is possible, the household needs a resource balance sheet: what we have, what we consume, what we produce, and what the gap is.

**Monthly resource accounting (minimum viable)**:

| Resource | Current Inventory | Monthly Consumption | Months of Supply | Production Rate |
|---|---|---|---|---|
| Calories (stored) | X lbs/million cal | Y cal/month | Z months | G cal/month (harvest season) |
| Water (stored) | X gallons | Y gallons/month | Z months | G gallons/month (well/rain) |
| Fuel (heating/cooking) | X gallons/cords | Y units/month | Z months | 0 (typically) |
| Medical supplies | Inventory list | Variable | Estimate | 0 |
| Energy (solar/battery) | X kWh capacity | Y kWh/month | Ongoing if sun | kWh/month (solar) |

This accounting takes 20 minutes per month once the initial inventory is complete. The output — months of supply in each category — is the household's most important operational indicator. Any category below 60 days triggers a procurement or production response.

### Labor Economics: Internal Allocation vs. External Trade

The labor economics of a household are simpler than community scale but require the same deliberate design. Total available labor hours per week for a 15-person household with 12 working-age adults (assuming 8 hours/day, 6 days/week labor availability):

Maximum: 576 hours/week
After personal/rest time allowance (25%): ~432 hours/week available for household functions

Typical allocation:
- Food production and preservation (growing season peak): 150–200 hours/week
- Food preparation and cleanup: 40–50 hours/week
- Water management: 10–15 hours/week
- Energy management: 5–10 hours/week
- Security/watch: 40–60 hours/week (6 × 4-hour shifts × 2 people = 48 hours/week minimum)
- Healthcare and hygiene: 15–20 hours/week
- Construction and maintenance: 20–40 hours/week (highly variable)
- Governance and coordination: 5–10 hours/week
- Education (if children present): 15–30 hours/week

Total: 300–435 hours/week, which is at or near the sustainable capacity of 12 adults. This confirms that a 15-person household at full resilience operation is not a leisurely arrangement — it is a full employment situation. Labor efficiency gains from specialization and coordination (the Phase 3 food document cites a 30% efficiency gain from 3-household cooperation [9]) are real but do not create abundant slack.

**External labor trade**: Tasks that the household has no capacity to handle internally — specialized medical procedures, complex mechanical repair, specific construction skills — are candidates for external trade. The household offers surplus food, labor assistance during harvest, or goods in exchange. These relationships should be established before they are needed.

### Skills Inventory and Specialization

A 15-person household should conduct a skills inventory at formation and update it annually. The inventory covers:

**Domain 1 — Agriculture and Food**: Soil preparation, seed starting, crop identification, irrigation management, harvest timing, food preservation (canning, fermentation, dehydration, root cellaring), animal husbandry, butchering.

**Domain 2 — Construction and Repair**: Basic carpentry, roofing, plumbing, electrical (DC systems), welding, woodstove/masonry, small engine repair.

**Domain 3 — Medical**: First aid certification, advanced wound care, childbirth assistance, medication management, dental basic care, mental health support.

**Domain 4 — Energy and Technology**: Solar panel installation and troubleshooting, battery bank management, generator maintenance, radio operation, basic electronics repair.

**Domain 5 — Security and Communication**: Radio operation, navigation (map and compass), first aid, watch protocol, conflict de-escalation.

**Domain 6 — Education and Knowledge**: Teaching, writing, record-keeping, library management, training facilitation.

For each skill, the inventory records: primary holder (name), apprentice (name or "none"), and proficiency level (basic/intermediate/expert). Skills with no apprentice are vulnerabilities. Skills with no holder at any level are household capability gaps requiring either training or external relationship.

### Trade Relationships and Emergency Reserves

A household embedded in a community trades its surplus for goods it cannot produce. The trade framework operates on relationship, not markets:

**Identify 3–5 adjacent households or community nodes** with complementary specializations. If your household is strong in food production but weak in mechanical repair, find a household with mechanical skills and build a relationship before you need them.

**Maintain non-food reserves for trade**: Spare medical supplies above household minimum, seeds above household production need, fuel above household energy budget, and specific knowledge (the person who knows how to fix the water pump) are all tradeable assets. Identify what your household has that others are likely to need.

**Emergency reserve policy**: The household maintains a reserve category distinct from the 6-month supply — 30 days of food and 30 days of fuel that are not touched for internal use and are available only for genuine emergency response: a neighboring household loses their supply to fire or flood, a medical emergency requires immediate resource commitment. The reserve policy is decided at a monthly meeting and reviewed quarterly. Emergency reserves are controlled by the assembly, not any individual coordinator.

---

## Section 7: Individual → Household Transition Checklist

### What Individuals Should Bring

This checklist is for individuals who are preparing to join or form a household unit. The assumption is that the individual has worked through some or all of the Tier 1 individual documents. Before joining a household, an individual should be able to answer yes to most of the following:

**Physical capability**:
- [ ] I can perform sustained moderate physical labor for 6–8 hours per day
- [ ] I have no untreated conditions that would significantly limit my labor contribution without medical accommodation
- [ ] I have identified any medication needs and have a 90-day supply plan

**Skill contribution** (at least one domain at intermediate or expert level):
- [ ] Food: I can grow from seed, preserve by at least two methods, and plan meals for a week from stored ingredients
- [ ] Technical: I can diagnose and perform basic repair on water pump, generator, or solar system
- [ ] Medical: I hold current first aid and CPR certification; or I have clinical training
- [ ] Construction: I can frame, roof, or do finish work at a functional level
- [ ] Communication: I hold or am pursuing GMRS/amateur radio license

**Knowledge**:
- [ ] I have read [individual/01-water.md](../individual/01-water.md) and can implement its protocols
- [ ] I have read [individual/02-food.md](../individual/02-food.md) and understand Zone 5 caloric planning
- [ ] I have read [individual/05-healthcare.md](../individual/05-healthcare.md) and maintain my own health records
- [ ] I understand what the Dunbar threshold means and why household governance matters

**Emotional and social readiness**:
- [ ] I have practiced conflict resolution in high-stakes relationships (family, close cohabitation)
- [ ] I can accept decisions I disagree with when made through a legitimate process
- [ ] I have disclosed any significant interpersonal challenges or conflict history to the household formation team

**What skills the household should already have before you join**:
- Established governance structure (meeting cadence, decision-making framework, conflict resolution protocol documented)
- At least one person per domain (food, water, energy, medical, security)
- 60 days of food and water in inventory
- At least one GMRS radio in operation

### Onboarding Process for New Members

Adapted from intentional community practice [11] and sized for household scale:

**Weeks 1–2 (Visitor/Observer)**: The incoming member attends all household meetings as an observer. They shadow each domain coordinator for one half-day shift. They read the Printed Procedures Binder. They have no vote during this period.

**Weeks 3–6 (Provisional Member)**: The incoming member takes on labor assignments. They are assigned to one domain with a designated mentor. They participate in weekly meetings with voice but no vote on constitutional decisions (new members, emergency reserve use, role changes).

**Week 7 (Skills and Fit Assessment)**: The incoming member and household have a documented conversation: what skills have been demonstrated, what gaps remain, what interpersonal issues have emerged. The household decides by simple majority to proceed to full membership or extend the provisional period.

**Full Membership**: Full voting rights, domain assignment (primary or apprentice), inclusion in the watch rotation. The household log records the membership date and skills inventory for the new member.

**Critical principle**: The onboarding period exists to let both parties gather information, not to test loyalty. If a fundamental incompatibility emerges — skill mismatch, governance philosophy conflict, interpersonal conflict that cannot be resolved — it is better for both parties to identify this in week four than in month eight.

---

## Section 8: Implementation Timeline

### Pre-Formation Work (Before Household Is Established)

Weeks 1–2:
- Identify who will form the household: names, current locations, stated commitment level
- Conduct a preliminary skills inventory across the prospective group
- Identify gaps that must be filled before the household is viable (does anyone hold medical? energy? food preservation?)
- Hold a formation meeting and make the explicit decision to proceed

Weeks 3–4:
- Draft the Governance Agreement: one or two pages covering decision-making model, meeting cadence, conflict resolution steps, and constitutional thresholds. This document does not need to be complex — it needs to be written and agreed to.
- Designate interim domain coordinators (these will be revisited at the first monthly meeting)
- Begin the physical inventory: what food, water, energy, and medical supplies does the combined group currently have?

### Forming Household Setup (Weeks 5–12)

Weeks 5–6:
- Establish physical household location and access arrangements
- Install primary communication system (GMRS base station, channel assignments documented)
- Conduct the first formal weekly meeting and begin the household log
- Complete the Printed Procedures Binder (first draft; 80% complete is adequate to start)

Weeks 7–8:
- Establish the 6-month food rotation system: build the inventory, assign Storage Manager, begin monthly counting protocol
- Establish water storage: minimum 30 days at 2 gallons/person/day (see individual/01-water.md for system sizing)
- Establish energy baseline: generator, solar, or both; fuel reserves documented

Weeks 9–10:
- Establish watch protocol and begin light-schedule monitoring (not full 24-hour watch, but a morning/evening check at access points)
- Conduct the first monthly meeting with full review
- Complete the skills inventory and identify vulnerabilities

Weeks 11–12:
- Address any skills vulnerabilities identified: training, external relationship establishment, or membership expansion
- Onboard any additional members using the protocol from Section 7
- Conduct a table-top exercise: simulate a 72-hour grid-down scenario and walk through household response using the Procedures Binder

### Established Household: 3-Month Autonomous Operation Benchmark

A household is ready for 3-month autonomous operation when all of the following are true:
- [ ] 90-day food supply in inventory and rotated monthly
- [ ] 30-day water supply in storage; primary collection system operational
- [ ] Energy supply adequate for essential loads for 30 days without resupply
- [ ] All critical household skills have identified primary and apprentice holders
- [ ] Communication system tested under simulated grid-down conditions
- [ ] Governance agreement in place, signed by all full members
- [ ] Household log active and maintained
- [ ] Watch and contact protocol practiced at least once (table-top or live exercise)
- [ ] External relationships established with at least 2 adjacent households

### The 6-Month Target (Community Integration Ready)

A household integrated into community coordination (Tier 3) should additionally have:
- 180-day food supply in inventory
- Established trade relationships and surplus commodities identified
- AREDN or equivalent data communication link to at least one community node
- Household delegate identified and onboarded to community governance process
- Security coordination integrated with community early-warning network

The timeline to 6-month community integration for an established household with committed members: 6–8 months of active work. For a forming household starting from scratch: 10–14 months. These timelines are not conservative — they reflect the actual implementation burden of doing this well rather than on paper.

---

## Citations and Sources

[1] Twin Oaks Community, "About Twin Oaks: Governance," twinoaks.org/about-twinoaks-community/faqs-frequently-asked-questions. Accessed May 2026. Twin Oaks' planner-manager governance system, 38.5-hour weekly labor quota, and 55+ years of continuous operation provide the best-documented US case study in household-to-community-scale governance.

[2] East Wind Community, "Self Governance," eastwind.org/self-governance; "Our Labor System," eastwind.org/our-labor-system. Accessed May 2026. 35-hour labor quota, direct democracy with defined thresholds, concerns process with 10% member veto, 50+ years in Missouri Ozarks.

[3] Robin Dunbar, "Neocortex size as a constraint on group size in primates," *Journal of Human Evolution* 22, no. 6 (1992): 469–493. The 150-person threshold for stable trust-based social networks; see Phase 3 governance document [phase-3/01-governance-decision-making.md] for full treatment of the Dunbar literature and its contested status post-2021.

[4] Foundation for Intentional Community, "How to Handle Conflict in Intentional Communities," communityfinders.com/conflict-in-intentional-communities/. Accessed May 2026. Consistent documentation of suppression-to-explosion cycle and the conditions under which conflict de-escalation works in small cohabitation groups.

[5] Sociocracy For All, "Sociocracy — Basic Concepts and Principles," sociocracyforall.org/sociocracy/. Accessed May 2026. Modified consent model: objection must be reasoned (operational harm) to block a proposal. Distinct from consensus. Applied in cohousing communities at 8–50 household scale.

[6] Phase 3: Community Security & Mutual Defense Structures, phase-3/04-security-and-defense.md, systems-resilience project. Internal conflict as dominant security burden after 2 weeks; failure mode documentation from post-hurricane and post-wildfire disruption data.

[7] Habitatista, "7 Effective Approaches to Conflict Resolution in Communal Living," habitatista.com/74859/7-effective-approaches-to-conflict-resolution-in-communal-living/. Accessed May 2026. Four-step de-escalation sequence from direct conversation to facilitated review to policy decision.

[8] MESS Brands, "How to Implement FIFO Rotation at Home," messbrands.com/inspiration/how-to-implement-fifo-rotation-at-home/. Accessed May 2026. FIFO protocol for household food storage; priority items expiring within 6 months.

[9] Phase 3: Community Food Systems & Supply Chain Resilience, phase-3/02-food-systems-supply-chain.md, systems-resilience project. Community-scale food hub model; local farm relationships; 30% labor efficiency gain from household cooperation.

[10] Phase 3: Community Information Infrastructure & Resilient Communications, phase-3/03-information-infrastructure.md, systems-resilience project. Three-layer communication architecture: GMRS, AREDN mesh, HF shortwave.

[11] Foundation for Intentional Community, "Designing a Community Membership Process," ic.org/designing-a-community-membership-process/. Accessed May 2026. Visitor-to-provisional-to-full-membership sequence; skills assessment and social fit evaluation.

[12] Sociocracy.info, "Switching to Sociocracy in Cohousing Communities," sociocracy.info/switching-to-sociocracy/. Accessed May 2026. Application of sociocratic circle structure in cohousing at 12–50 household scale; domain-based circle authority.

[13] Phase 3: Scaling Pathways & Governance Transitions, phase-3/05-scaling-pathways-and-thresholds.md, systems-resilience project. 100-person direct participation structure; specialist accountability to assembly; institutional memory failure modes.

[14] Phase 4 Synthesis Framework, PHASE_4_SYNTHESIS_FRAMEWORK.md, systems-resilience project. Load-bearing infrastructure map; governance and information as Tier 1 dependencies; the household gap as Phase 5 priority.

[15] FEMA / Wallaby Goods Emergency Food Storage Calculator, wallabygoods.com/pages/food-calculator. Accessed May 2026. Per-person caloric requirements for emergency planning; 2,000 cal/day baseline, higher for working adults.

[16] Off Grid Web, "How to Build a Six-Month Food Supply," offgridweb.com/preparation/how-to-build-a-six-month-food-supply/. Accessed May 2026. Storage quantities, caloric density figures, and FIFO rotation principles for extended food supply.

[17] CommGearReport, "GMRS for Neighborhood Watch and CERT," commsgearreport.com/gmrs-for-neighborhood-watch-and-cert-communications-plan/. Accessed May 2026. GMRS implementation for neighborhood-scale coordination; battery conservation through scheduled monitoring windows.

[18] GMRS.io, "Emergency Communication Guide," gmrs.io/guide/emergency-communication. Accessed May 2026. Simplex channel selection, CTCSS tone discipline, and scheduled net protocol for grid-down communication.

[19] FCC, "General Mobile Radio Service," fcc.gov/wireless/bureau-divisions/mobility-division/general-mobile-radio-service-gmrs. Accessed May 2026. Licensing requirements: $35/10 years, covers licensee plus immediate family members; up to 50W on designated channels.

[20] Household Food Coordination — 3-Household Scale, household/03-food-coordination.md, systems-resilience project. Zone 5 yield reference table; caloric production figures; 3-household efficiency gains and shared preservation equipment.

[21] Household Energy Coordination — 3-Household Scale, household/04-energy-coordination.md, systems-resilience project. Distributed generation with shared battery bank; 99th-percentile winter design temperature 0°F.

[22] Household Network Coordination Overview, household/01-household-coordination-overview.md, systems-resilience project. Domain-specialist authority model; 3-household governance frameworks; sociocratic consent at 4–6 household scale.

[23] East Wind Community, "Our Labor System," eastwind.org/our-labor-system. Accessed May 2026. Labor scoop sheet system; banking of surplus hours; 35-hour base quota with 27-hour holiday weeks.

[24] Cohousing Association of the United States, "Community as Economic Engine," cohousing.org/community-as-economic-engine/. Accessed May 2026. Skills sharing, labor allocation, and economic coordination in cohousing communities.

[25] Phase 3: Community Governance & Decision-Making Structures, phase-3/01-governance-decision-making.md, systems-resilience project. Zapatista, Rojava, Mondragon, and WWII rationing board case studies; Ostrom's 8 Design Principles; delegate council model for 150–500 people.

[26] Off The Grid News, "Early Warning Systems for Homesteads and Off-Grid Life," offthegridnews.com/defense/home-defense/early-warning-systems-for-homesteads-and-off-grid-life/. Accessed May 2026. IR motion sensors, zone-based alerting, and layered early warning for rural properties.

[27] Calling Up Justice, "Bartering versus Mutual Aid," callingupjustice.com/bartering-versus-mutual-aid-which-is-better-for-your-community/. Accessed May 2026. Comparative analysis of barter vs. mutual aid networks for community resilience; combination approach recommended.

[28] Sociocracy for All, "Skill Building for a Culture of Collaboration," ic.org/skill-building-for-a-culture-of-collaboration/. Accessed May 2026. Role-based skill development and knowledge transfer in intentional community settings.

---

## Cross-References

**Tier 1 individual documents** (prerequisite reading):
- [individual/01-water.md](../individual/01-water.md) — water system sizing and management
- [individual/02-food.md](../individual/02-food.md) — caloric planning and food preservation fundamentals
- [individual/03-shelter.md](../individual/03-shelter.md) — shelter hardening
- [individual/04-energy.md](../individual/04-energy.md) — individual energy systems
- [individual/05-healthcare.md](../individual/05-healthcare.md) — medical self-sufficiency
- [individual/06-agriculture.md](../individual/06-agriculture.md) — Zone 5 growing and seed saving

**Existing household-scale documents** (peer reading):
- [household/01-household-coordination-overview.md](../household/01-household-coordination-overview.md) — 3-household cluster model
- [household/03-food-coordination.md](../household/03-food-coordination.md) — food coordination at 3-household scale
- [household/04-energy-coordination.md](../household/04-energy-coordination.md) — energy coordination at 3-household scale

**Phase 3 source documents** (community-scale reference):
- [phase-3/01-governance-decision-making.md](../phase-3/01-governance-decision-making.md) — full treatment of governance structures
- [phase-3/02-food-systems-supply-chain.md](../phase-3/02-food-systems-supply-chain.md) — community food systems
- [phase-3/03-information-infrastructure.md](../phase-3/03-information-infrastructure.md) — communication architecture
- [phase-3/04-security-and-defense.md](../phase-3/04-security-and-defense.md) — security structures
- [phase-3/05-scaling-pathways-and-thresholds.md](../phase-3/05-scaling-pathways-and-thresholds.md) — Dunbar transition and federated models

**Phase 5 Tier 2 documents** (parallel development):
- [phase-5/tier-2-veterinary-care-guide.md](./tier-2-veterinary-care-guide.md) — animal health at household scale (planned)
- [phase-5/tier-2-psychological-support-guide.md](./tier-2-psychological-support-guide.md) — mental health coordination (planned)
- [phase-5/tier-2-conflict-resolution-deep-dive.md](./tier-2-conflict-resolution-deep-dive.md) — extended conflict resolution protocols (planned)

**Phase 5 Tier 3** (forward reference):
- [phase-5/tier-3-community-coordination-framework.md](./tier-3-community-coordination-framework.md) — how household units federate into 100+ person community (planned)
