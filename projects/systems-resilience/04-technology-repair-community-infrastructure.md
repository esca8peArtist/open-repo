---
title: "Technology Repair and Maintenance — Community Infrastructure"
phase: 4a
status: complete
word_count: ~7100
audience: "Project lead (Anya) — community scale, 50–150 people, Midwest Zone 5"
created: 2026-05-17
cross_references:
  - individual/04-energy.md
  - individual/01-water.md
  - household/04-energy-coordination.md
  - household/02-water-coordination.md
  - community/02-infrastructure-interdependency.md
  - community/03-mutual-aid-networks.md
---

# Technology Repair and Maintenance — Community Infrastructure

> **Region**: Midwest US (Zone 5) | **Scale**: 50–150 people
> **Phase**: 4a — Equipment repair capacity before professional services are available
> **Cross-references**: [individual/04-energy.md](individual/04-energy.md) · [individual/01-water.md](individual/01-water.md) · [community/02-infrastructure-interdependency.md](community/02-infrastructure-interdependency.md) · [community/03-mutual-aid-networks.md](community/03-mutual-aid-networks.md)

---

## The Most Important Finding

Phase 1–3 documents assume equipment works. They do not. A solar panel system, hand pump, generator, radio, or chainsaw will eventually fail — and in an extended disruption, the supply chain for professional repair technicians fails before the equipment does. The community that has already built repair capacity — the tools, the manuals, the trained people — before the disruption survives equipment failure. The community that has not built that capacity faces a cascade: one failed water pump stops irrigation, which reduces food production, which stresses the community precisely when it can least afford stress. Equipment failure is not a technical problem to be solved later. It is a foundational resilience gap that must be addressed now.

The good news: the legal and knowledge landscape for community repair has improved dramatically. The iFixit offline archive contains 44,000+ repair guides in a 2.5 GB download. The Village Earth Appropriate Technology Library holds 1,050 books on self-reliance technology on a single USB drive [1][2]. And the John Deere $99 million settlement in April 2026 — forcing Deere to provide farmers and independent shops with diagnostic tools for at least 10 years — signals a broader shift in who legally controls the right to fix equipment [3].

---

## Section 1: The Repair Gap

### Dependency Audit — What a Midwest Community of 50–150 Depends On

Before building repair capacity, you need to know what you are repairing. The following audit is calibrated to a Zone 5 Midwest community of 50–150 people running the systems described in Phase 1–3.

**Critical Infrastructure (failure within 48 hours causes cascade)**

| Equipment | Role | Failure consequence |
|---|---|---|
| Well pump (electric submersible) | Water supply | No water within hours |
| Generator (2–10 kW portable) | Emergency power | Medical equipment, communication, winter heating backup |
| Solar charge controller | Battery regulation | Overcharge destroys battery bank within days |
| Pressure tank (water system) | Even water delivery | Rapid pump cycling burns out motor |
| GMRS/ham radio | Community communication | Situational awareness lost |

**High-Dependence Infrastructure (failure within days causes degradation)**

| Equipment | Role | Failure consequence |
|---|---|---|
| Solar panel array | Off-grid power generation | Battery draw-down over 2–5 days |
| Inverter | DC-to-AC conversion | Cannot run AC loads from battery |
| Chainsaw | Firewood cutting, tree clearing | Labor-intensive manual alternatives |
| Small tractor / ATV | Field transport, field prep | Agricultural operations severely hampered |
| Water storage tanks | Buffer supply | Loss of storage redundancy |

**Supporting Equipment (failure within weeks degrades operations)**

| Equipment | Role | Failure consequence |
|---|---|---|
| Hand pump (backup water) | Backup when electric pump fails | Depends on electric pump having already failed |
| Hand tools (axes, saws, shovels) | Firewood, construction, garden | Increased labor, reduced output |
| Water filtration systems | Potable water safety | Must default to boiling |
| Communication batteries | Radio power | 2–4 hours of operation then silent |

**Zone 5 Midwest Timing Note**: The most dangerous failure windows are December–February (when well pump or generator failure in sub-zero temperatures becomes life-threatening within hours) and August–October (when harvest-season equipment is running at 200–300% normal intensity and failure costs unharvested food). Pre-season inspection in October and April addresses both windows. See [community/02-infrastructure-interdependency.md](community/02-infrastructure-interdependency.md) for the full cascade mapping.

### Failure Mode Analysis — What Fails First and How Fast

Field experience and manufacturer documentation identify consistent patterns:

**Fastest failures (hours to days):**
- Generator carburetor gum from ethanol-blend fuel stored more than 30 days without stabilizer [4]
- Pressure tank bladder failure (waterlogged tank causes rapid pump cycling that burns motor within days)
- Solar charge controller failure from overtemperature (no ventilation in enclosed mounting box)
- Radio battery failure (standard NiMH batteries lose capacity 20% per year; lithium cells last 3–5 years)

**Medium failures (months):**
- Chainsaw chain dullness (every 2–3 hours of cutting without sharpening causes excessive bar and engine wear)
- Generator oil degradation (every 100 hours of run time; every 50 hours under heavy load) [5]
- Solar panel efficiency loss from dust accumulation (15–25% output reduction at moderate soiling levels) [6]
- Hand pump leathercup wear (annual inspection recommended; replacement every 1–5 years depending on use intensity)

**Long-term failures (years):**
- Battery bank capacity loss (flooded lead-acid: 3–5 year lifespan with proper maintenance; 2 years without)
- Inverter capacitor failure (common after 5–10 years; detectable by bulging capacitor bodies or erratic output)
- Submersible pump bearing wear (7–15 years typical lifespan; sand-laden water accelerates failure)
- Well casing corrosion (20–30 year horizon in most Midwest soils; Zone 5 road salt accelerates surface-level corrosion)

**The asymmetry**: Short-term failures (carburetor gum, flat battery) are preventable at near-zero cost through scheduled maintenance. Long-term failures (pump replacement, battery bank replacement) are capital expenses that require advance stocking of parts or the financial capacity to purchase replacement equipment when supply chains re-open. Community repair strategy must address both: prevent the preventable failures through scheduled maintenance, and stock critical replacement parts (leathercups, pump capacitors, generator carburetors, battery cells) before disruption begins.

### Right to Repair — 2025–2026 Context

The Right to Repair movement has direct practical implications for community repair capacity.

**The core problem the movement addresses**: Modern equipment, especially agricultural machinery, is locked behind proprietary diagnostic software that only manufacturer-authorized dealers can access. A John Deere tractor with a fault code will not run until a dealer with "Service ADVISOR" software clears the code — even if the mechanical problem has already been fixed. This created a repair monopoly at exactly the moment rural communities most needed repair independence [7].

**What changed in April 2026**: John Deere agreed to a $99 million settlement in a consolidated class-action antitrust lawsuit filed in U.S. District Court for Northern Illinois. The settlement terms require Deere to provide farmers and independent repair shops with the same diagnostic tools and repair resources available to authorized dealers, on fair and reasonable terms, for at least 10 years [3][8]. The FTC's separate suit against Deere — filed January 2025 and alleging Sherman Act violations — remains active, adding further pressure for structural change [9].

**Legislative progress**: As of 2026, 20+ states have introduced farm equipment right-to-repair bills, with Colorado, Minnesota, and California having enacted laws or comprehensive regulations. Iowa's house passed a right-to-repair bill in April 2026 with bipartisan support [10]. The federal FARM Act (Freedom for Agricultural Repair and Maintenance), introduced in 2025, would establish a nationwide statutory right to repair farm equipment. Washington state enacted its own Right to Repair Act in May 2025 [10].

**What this means practically for a community repair program**:
1. Diagnostic software for John Deere equipment must now be made available — communities should document this in their tool library (see Section 2) and identify who has the equipment and training to use it
2. Independent repair shops now have clearer legal standing to obtain parts and documentation from manufacturers
3. The broader cultural shift is normalizing repair as a legal and practical right, not a warranty violation
4. Communities should download offline repair documentation now, while internet access is available, rather than assuming it will be accessible when needed

---

## Section 2: Community Tool Library and Repair Shop

### Tool Library Design

A community tool library is not a pile of equipment in someone's garage. It is a governed, inventoried, maintained system that makes shared tools accessible when needed and returns them to service after use. The governance structure is as important as the tools themselves.

**Governance framework** (adapted from tool lending library models operated by local governments and non-profits across the US) [11]:

*Membership and access:*
- Community membership required to borrow — a signed agreement that establishes responsibilities, not a financial barrier
- Tiered access: all members can borrow hand tools and basic power tools; specialty tools (welding equipment, pipe threader, oscilloscope) require demonstrated competency or supervision
- Checkout period: 3 days for standard tools, 1 day for high-demand single items (grinder, pipe threader)
- Waiting list system for high-demand tools during harvest season

*Accountability:*
- Condition documented at checkout with notes and photo (phone works; a dedicated camera stored with the library is more reliable off-grid)
- Three categories of return condition: normal wear (no action), minor damage (borrower contributes $5–15 repair fund), major damage or loss (full replacement value)
- Late returns: $1–2/day after the checkout period, capped at 25% of replacement value; three late returns results in suspension pending review
- A "three strikes" rule for repeated violations before membership review

*Maintenance responsibility:*
- Designated library steward (one person per quarter, rotating) responsible for weekly condition checks
- Maintenance fund built from membership contributions and damage fees
- Annual full inventory and condition inspection before winter (October) and spring (April)
- Volunteer maintenance sessions (monthly, 2 hours) for sharpening, oiling, handle replacement

*Storage:*
- Weatherproof building or dedicated lockable section of community repair shop
- Inventory list posted inside lid of each storage bin or drawer, and maintained in paper master list
- Tools organized by category: hand tools, power tools, specialty, safety equipment
- Power tool chargers stored with the tools; battery condition logged

**Essential tool inventory for 50–150 people**

The following list is organized by priority. Acquire and maintain in this sequence.

*Hand tools (non-electric) — acquire before any power tools:*
- Hammers: 2 × claw hammer (16 oz), 1 × ball-peen hammer, 1 × sledgehammer (8 lb)
- Saws: 2 × crosscut hand saw, 1 × hacksaw with spare blades (18- and 24-tooth), 1 × coping saw
- Wrenches: 2 full sets open-end/box-end (SAE + metric), 2 × adjustable wrench (12"), 1 × pipe wrench (18"), 1 × pipe wrench (24")
- Pliers: 2 × slip-joint, 2 × needle-nose, 2 × locking (Vise-Grips), 1 × lineman's pliers, 1 × wire strippers (10–22 AWG)
- Screwdrivers: 4 × flathead (various), 4 × Phillips (#1, #2, #3), 2 × Robertson (if working with Canadian-made equipment)
- Chisels: set of 4 wood chisels (1/4" to 1"), 2 × cold chisel
- Files: bastard mill file, smooth mill file, round file set (for chainsaw sharpening — 3/16", 7/32", 5/16"), flat file
- Measuring: 2 × 25 ft tape measure, combination square, level (2 ft), marking gauge
- Cutting: utility knife with spare blades, tin snips (straight + left/right aviation)
- Digging: 2 × round-point shovel, 1 × square-point shovel, 1 × post-hole digger, 1 × mattock

*Power tools (cordless preferred — grid-independent):*
- Drill/driver: 2 × cordless drill (18V or 20V platform with 2 batteries each)
- Circular saw: 1 × cordless (same battery platform as drill)
- Grinder: 1 × angle grinder (electric, corded acceptable — used for metal work at bench)
- Reciprocating saw: 1 × cordless
- Jigsaw: 1 × cordless
- Battery platform consistency is critical: standardize on one voltage platform (e.g., 20V DeWalt or Milwaukee M18) so all batteries are interchangeable. Maintain 6–8 batteries total with two chargers.

*Specialty tools (higher cost, lower frequency — shared makes more sense):*
- Multimeter: 2 × digital multimeter (Fluke or equivalent; ranges: DC/AC voltage, resistance, continuity, diode test, capacitance)
- Soldering iron: 1 × temperature-controlled (Hakko or equivalent), solder, flux
- Wire crimpers and terminal kit: complete ratcheting crimper set, assorted terminals
- Pipe work: pipe cutter (1/4"–2"), pipe threader with dies (1/2", 3/4", 1"), plumber's torch + solder + flux paste
- Welding: see Section 3 (specialty knowledge) — welding equipment is high-value, high-risk; requires trained operator
- Hydraulic jack: 2 × 3-ton floor jack
- Chain hoist (come-along): 1 × 2-ton, 1 × 4-ton — for pulling equipment, moving heavy objects
- Tractor jack / hi-lift jack: 1 unit for farm equipment
- Leak detection: 1 × FLIR thermal camera (identifies hot spots in electrical systems, detects water leaks in walls) — expensive ($300+) but invaluable for diagnosis; justify with community cost share
- Battery hydrometer: for flooded lead-acid battery specific gravity testing
- Torque wrench: 1 × 1/2" drive (20–150 ft-lb), 1 × 3/8" drive (10–75 ft-lb)

*Safety equipment (non-negotiable — do not allow tool use without):*
- Eye protection: 10 × safety glasses (clear), 4 × face shield
- Hearing protection: 10 pairs disposable foam, 4 × reusable earmuffs
- Gloves: 10 pairs mechanics gloves, 10 pairs leather work gloves
- Fire extinguisher: 2 × ABC dry chemical (5 lb), inspected annually
- First aid kit: OSHA-compliant for 10+ person workshop

### Community Repair Shop Design

The community repair shop is the physical space where diagnosis, repair, and maintenance work happens. It is distinct from the tool library storage area, though they may be in the same building.

**Minimum viable shop (400 sq ft):**

A 20 × 20 ft space is sufficient for 2–3 people to work simultaneously on different repairs. This can be a dedicated building, a well-organized section of a barn or garage, or a prefabricated structure. The key requirements are:

- **Lighting**: Excellent natural light supplemented by 4–6 overhead LED shop lights (4 ft T8 or equivalent). Dark corners cause missed diagnoses and injuries.
- **Ventilation**: Operable windows on two walls minimum; exhaust fan for welding and painting. Welding fumes in enclosed spaces cause long-term respiratory damage.
- **Flooring**: Concrete preferred (spills are cleanable; fire-resistant); if dirt floor, lay concrete pavers under bench area. Nothing on bare wood floor near welding or grinding.
- **Workbenches**: 2 × 8 ft workbenches at 34–36" height (adjustable for the person using them). Heavy-duty construction — 2× lumber or welded steel frame. Minimum 600 lb capacity each.
- **Bench vises**: 1 × 6" machinist vise and 1 × 5" woodworking vise (pipe jaws for round stock). Mount on bench ends; these are primary holding devices for most work.
- **Parts storage**: Metal shelving (fire-resistant), labeled bins for fasteners (sorted by type and size), dedicated shelf for parts in active repair, dedicated area for "parts donors" (broken equipment kept for components)
- **Reference library**: One drawer or shelf dedicated to printed repair manuals, equipment documentation, and reference guides. Physical copies only — digital-only reference fails when power is out.
- **Electrical**: Minimum 4 × 20A circuits; 1 × 240V outlet for welding and large power tools. Proper grounding throughout. GFCI on all outlets near water or in wet conditions.
- **Heating**: Shop must be heated to at least 50°F for hands-on work (dexterity fails below this). Propane forced-air heater is the most reliable off-grid option; wood stove acceptable but requires fire safety attention.

**Parts inventory strategy:**

Stock critical consumables before disruption, using the failure mode analysis from Section 1 as a guide:

| Category | Stock 5-year supply of: |
|---|---|
| Generator | Air filter, oil filter, spark plugs (2 per unit), carburetor rebuild kit |
| Water pump | Pressure tank bladder (match tank brand), pump capacitor, foot valve, check valve |
| Hand pump | Leathercup seals (6 per pump), cylinder rod O-rings |
| Solar system | 20A and 30A fuses, inline fuse holders, MC4 connectors, Anderson connectors |
| Electrical | Assorted wire nuts, terminal crimps, 12 and 10 AWG wire (50 ft spools) |
| Chain/small engine | Chainsaw chains (2 per saw), bar oil (10 gallons), 2-stroke oil (5 gallons) |
| Fasteners | Assorted stainless screws and bolts (SAE and metric), locknuts, washers |

**Community repair shop governance:**
- Scheduled "open shop" hours (Saturday morning, for example) when equipment is in use and mentoring is available
- Posted emergency contact list: who to call for each equipment category when repair is beyond shop capacity
- Logbook: record every repair (date, equipment, problem, solution, parts used, time) — this becomes institutional memory
- Tool sign-out log co-located with tool storage

### iFixit and Repair Café Integration

The Repair Café model — where community members bring broken items to volunteer-staffed repair events — provides a template for how community repair culture is built and maintained [12].

**What the iFixit/Repair Café partnership provides:**

iFixit and the Repair Café Foundation have collaborated since 2015. The partnership provides:
- Discounts on tools and replacement parts for registered Repair Cafés
- Tool grants — in 2019, iFixit supplied 100 Repair Cafés globally with tools
- Integration of iFixit's step-by-step repair guides into Repair Café events

As of 2026, more than 2,500 Repair Cafés operate worldwide — including across the Netherlands, France, Germany, the UK, the US, South Africa, India, and Japan [13]. The model is scalable: a Repair Café can be a monthly event at a community center with 3–5 volunteer repair specialists, or it can evolve into a permanent staffed space.

**Adapting the Repair Café model for a Zone 5 Midwest community:**

For a community of 50–150 people operating the systems described in Phase 1–3, the Repair Café model becomes a monthly maintenance event rather than a consumer-facing fix-it clinic:

- Pre-harvest (late July/early August): full system check of all critical equipment; carburetor cleaning, oil changes, chain sharpening, battery tests
- Post-harvest (November): winterization of outdoor equipment; full inventory of parts needed for spring; inspection of any damage from harvest-season load
- Mid-winter (January): indoor electrical and electronics work; radio maintenance, battery capacity testing, inverter inspection
- Spring startup (April): recommission all systems; replace any consumables identified in November inventory

Monthly open shop sessions between these events handle smaller repairs and maintain repair culture. The key is that repair is treated as a routine community activity, not an emergency response.

**Offline iFixit library:**

iFixit's entire guide archive — 44,000+ guides, 456,000+ images — is available as a 2.5 GB downloadable package in the Kiwix .zim format, compatible with Kiwix reader software [14]. This is the most important single preparation for knowledge-independent repair:

1. Download the iFixit Kiwix package at library.kiwix.org (English package, ~2.5 GB)
2. Install Kiwix reader on a laptop or Raspberry Pi
3. Store the .zim file on two separate USB drives (one primary, one backup)
4. Print selected critical guides (well pump, generator, chainsaw) and file in the shop reference library

This ensures that when internet access is unavailable, the repair knowledge is still accessible.

---

## Section 3: Repair Knowledge Infrastructure

### Offline Repair Manual Library

The community shop reference library should contain physical copies of critical repair documentation. The internet will not always be available. Even when it is available, diagnostic work in a dark shop with greasy hands benefits from a printed manual that can be set on the bench, not a phone screen.

**Library structure (one drawer or shelf, clearly labeled):**

*Tier 1 — Print and laminate (highest-use reference):*
- Quick-reference maintenance schedule (compiled from this document and Document B; one page per equipment type)
- Multimeter reference card (voltage ranges, continuity symbols, diode test procedure)
- Chainsaw file size chart by chain pitch
- Generator oil type and capacity by model
- Battery specific gravity table (temperature-corrected)
- Emergency shutdown procedures for all major systems

*Tier 2 — Print and file in labeled folders:*
- Generator owner's manual (for each generator owned by the community)
- Solar charge controller manual (for each unit — error codes are model-specific)
- Inverter manual (for each unit)
- Well pump manufacturer documentation (submersible pump model, pressure tank model)
- Hand pump maintenance guide (Simple Pump or equivalent)
- Chainsaw service manual (Stihl, Husqvarna, or the models you own)
- Small tractor service manual (model-specific)

*Tier 3 — Digital backup on USB (accessed via laptop when power is available):*
- iFixit Kiwix archive (2.5 GB, all 44,000+ guides)
- Village Earth Appropriate Technology Library (1,050 books, 150,000+ pages on single USB) [2]
- Equipment PDF manuals for all community-owned equipment

**Village Earth Appropriate Technology Library:**
This library is the most comprehensive offline reference for appropriate technology and self-reliance systems. The $69 USB drive contains 1,050 books covering water systems, energy, construction, metalworking, agriculture, and related subjects — comparable in scope to what a small technical college library would hold for these topics. The drive includes a Linux operating system and Calibre ebook reader, so it is self-contained and does not require a functioning operating system on the host computer [2]. Order one before disruption. Store two copies.

**Printed manual strategy:**
For each critical piece of equipment, download the service manual (not just the owner's manual) and print it. Service manuals include:
- Complete parts diagrams with part numbers
- Diagnostic flowcharts
- Torque specifications for reassembly
- Electrical schematics

Stack Overflow and YouTube are not reliable when the internet is unavailable. A printed service manual is.

### Skill Training — Who Knows What

The most critical repair infrastructure is not tools or manuals — it is people. A community of 50–150 people has enough labor to support 2–3 people per equipment category with meaningful repair competency, if training is prioritized before disruption.

**Skills mapping by equipment category:**

| Equipment category | Minimum competency needed | 2-person minimum training |
|---|---|---|
| Generator | Oil change, carburetor cleaning, startup procedure | Achievable in 4-hour session |
| Well pump | Pressure tank diagnosis, bladder replacement, hand pump maintenance | Achievable in 6-hour session + hands-on practice |
| Solar system | Battery testing, connection inspection, charge controller diagnostics | Achievable in 8-hour session |
| Chainsaw | Chain sharpening, air filter, fuel mix, safe operation | Achievable in 4-hour session |
| Basic electrical | Multimeter use, wire joining, fuse replacement | Achievable in 6-hour session |
| Radio communication | Programming, battery replacement, antenna inspection | Achievable in 3-hour session |
| Welding | MIG or stick welding basics | 20+ hours minimum; recruit an existing welder |

**Training approach:**

The Community Boards model — drawing on peer training and conflict mediation traditions — applies directly to repair knowledge: train the people who will be most present and most motivated, not necessarily the most formally credentialed. A farmer who has run chainsaws for 20 years may need only a 2-hour session to add chain sharpening and carburetor cleaning to their knowledge base. A retired electrician may need only documentation review to extend their skills to solar system diagnosis [15].

For each equipment category:
1. Identify the 1–2 community members who currently have the most experience with this equipment
2. Invest in one structured training session (manufacturer, extension service, trade school, or experienced peer) that covers maintenance and common failure modes — not just operation
3. Document what was learned in the shop logbook; have the trainee write a 1-page summary of the procedure they were taught
4. Have the newly trained person train a second person within 3 months (teaching is the best test of understanding)

**Coordination with Phase 3 mutual aid:** See [community/03-mutual-aid-networks.md](community/03-mutual-aid-networks.md) for the community skills census framework. Repair skills should be documented in that census alongside medical, agricultural, and construction skills.

### Specialty Knowledge at Risk

Some repair knowledge cannot be acquired through a half-day training session. Three categories require either a specialist in the community or an explicit plan for what happens when that knowledge gap is encountered:

**Electronics diagnosis beyond basic multimeter work:**

Modern circuit boards contain components — microcontrollers, surface-mount ICs, multilayer PCBs — that cannot be repaired without specialist equipment (oscilloscope, reflow station, schematic access). The honest boundary is:
- Replaceable-component level repair (fuses, through-hole capacitors, relays, switches): achievable with basic training and tools
- IC-level diagnosis: requires oscilloscope and schematic — achievable with a trained electronics technician in the community
- Microcontroller-level repair: essentially impossible without factory programming tools; design for this by stocking spare complete units (inverter, charge controller, radio) rather than expecting board-level repair

If you have someone in the community with electronics or electrical engineering background, prioritize getting them trained specifically on the community's equipment. If you don't, prioritize equipment selection that uses replaceable modules.

**Hydraulics:**

Hydraulic systems on tractors, loaders, and log splitters fail in ways that require specialized knowledge to diagnose: cylinder rod seal replacement, valve body cleaning, pump rebuild, hydraulic line flaring and fitting. A community farm that depends on a tractor loader should have at least one person trained in basic hydraulic maintenance. Training sources: Caterpillar, John Deere, and NAPA offer hydraulic system courses; community colleges with agriculture programs often run short hydraulic courses.

**Welding:**

Welding (MIG, stick, and oxy-acetylene) is one of the highest-value repair skills for a community with metal infrastructure — broken tractor frames, cracked implement parts, structural repairs on buildings. It is also one of the most dangerous without proper training. The practical path:
- Recruit an existing welder in the community — someone who welds is far more common in rural Midwest communities than in urban ones
- Invest in the equipment: a 110/220V MIG welder with gas (CO2/argon mix) is the most practical for community repair; oxy-acetylene is more versatile (can cut, braze, weld) but requires ongoing gas supply; stick welding (arc welding) is the most infrastructure-independent (only requires electrodes, no gas)
- Stock welding consumables: MIG wire (2 lb spools of .030" ER70S-6), electrode rods for stick (E6011 for all-position, E7018 for structural), flux paste for oxy-acetylene brazing
- Designate the shop's welding area with non-combustible flooring, welding curtains, and a fire extinguisher within arm's reach

---

## Section 4: Building Repair Culture — The Social Infrastructure

Technical knowledge and physical tools are necessary but not sufficient for community repair capacity. A community that owns a multimeter but has never taught anyone to use it is no better off than one without a multimeter. A community that has repair manuals locked in someone's house is not meaningfully different from one that has no manuals. The social infrastructure — who knows what, who teaches whom, how repair events are organized, and how institutional memory is maintained — is the layer that makes the physical and knowledge infrastructure functional.

### The Three Failure Modes of Community Repair Programs

Community repair programs fail in predictable ways:

**Failure mode 1: Single-point-of-knowledge.** One person in the community knows how to repair the water pump. That person moves away, gets sick, or becomes unavailable during a disruption. The knowledge is gone. The fix is redundancy: 2–3 people per equipment category at minimum, with documented procedures that don't depend on personal memory.

**Failure mode 2: Tool hoarding.** Tools accumulate in the personal possession of whoever buys them or has storage space. When those tools are needed by someone else, they are unavailable, unknown, or inaccessible. The fix is the tool library (see Section 2) — not because private ownership of tools is wrong, but because community awareness of what tools exist and how to access them is the infrastructure that makes a collection of tools into a community resource.

**Failure mode 3: Repair as emergency, not routine.** Repair skills atrophy when they are only exercised in crisis. The community member who learned to clean a carburetor in a training session 3 years ago may not remember the procedure when the generator won't start at midnight in January. The fix is regular practice: monthly maintenance sessions, pre-season inspections, and repair events that treat maintenance as routine rather than exceptional.

### Training Program Design

A training program for community repair does not require a professional instructor. It requires someone who already knows the procedure, a structured occasion to demonstrate it, and documentation of what was demonstrated.

**Training session format (4–8 hours per equipment category):**

*Before the session:*
- Identify who is being trained (2–3 people per category)
- Identify who is training them (current knowledge holder, or arrange outside trainer)
- Gather the actual equipment and required tools
- Print the relevant service manual section or procedure sheet

*During the session:*
- Demonstrate the procedure with the actual equipment (not a whiteboard)
- Narrate every step as you do it; explain why, not just what
- Have trainees perform the procedure themselves under supervision — watching is not learning
- Identify the 3–5 most common failure points specific to that equipment (where will they get stuck? where do people make mistakes?)

*After the session:*
- Trainee writes a 1-page summary of the procedure in their own words — this is the most important part; it surfaces gaps in understanding and creates a procedure sheet for the shop
- File the procedure sheet in the shop reference library
- Log the training in the community skills census (see [community/03-mutual-aid-networks.md](community/03-mutual-aid-networks.md) for the skills inventory framework)
- Schedule a follow-up hands-on practice within 60 days while the learning is fresh

**Recommended training sequence for a community of 50–150:**

Year 1 priority (highest risk categories):
1. Generator maintenance (oil change, carburetor cleaning, startup procedure) — 4 hours
2. Well pump and pressure tank (pressure testing, bladder diagnosis, hand pump maintenance) — 6 hours
3. Chainsaw maintenance and safe operation (chain sharpening, fuel mix, safe techniques) — 4 hours
4. Basic electrical (multimeter use, wiring connections, fuse replacement) — 6 hours

Year 2:
5. Solar system maintenance (panel cleaning, battery testing, charge controller diagnostics) — 8 hours
6. Small tractor maintenance (oil change, belt inspection, hydraulic fluid, grease) — 4 hours
7. Radio maintenance and programming (battery replacement, antenna, manual programming) — 3 hours
8. Basic plumbing (pressure tank replacement, pipe joining, shutoff valves) — 4 hours

Year 3 and ongoing:
9. Welding fundamentals (recruit an existing welder; community provides equipment) — 20+ hours
10. Hydraulics basics (tractor hydraulic system, cylinder seals) — 8 hours
11. Basic electronics diagnosis and soldering (for those with aptitude) — 12 hours

**External training resources:**

- County Extension Services: most Midwest counties maintain an agricultural extension office with workshops on farm equipment maintenance; free or low-cost
- Community colleges with agriculture programs: typically offer single-day and weekend workshops in small engine repair, hydraulics, welding, and electrical
- Manufacturer training: Husqvarna, Stihl, and other equipment manufacturers offer dealer training programs that are sometimes open to non-dealers; worth asking
- 4-H alumni and FFA members in the community: often have practical mechanical training that is underutilized in adult contexts

### Community Annual Repair Calendar

The Repair Café model adapted for a Zone 5 Midwest agricultural community organizes into four anchor events per year, each tied to the agricultural and weather calendar. Between these events, an open shop session (1 Saturday morning per month) handles smaller repairs and maintains skills.

**Event 1: April Recommission (first weekend in April)**

Spring startup after winter dormancy. Most critical event because frozen-weather damage is discovered here and must be addressed before planting season.

Agenda (half-day, 4 hours):
- Open all systems that were winterized: drain cocks closed, heat tape tested, hoses reconnected
- Water system: restart submersible pump; verify pressure tank air charge; run the hand pump and inspect for winter seal damage
- Generator: run load test; check oil; inspect carburetor (likely varnished if not run since November)
- Solar system: clean panels (months of winter grime); check all connections; equalize flooded batteries if not done in October
- Chainsaw: sharpen chain; clean air filter; fresh 2-stroke mix
- Document any equipment damage discovered and assign repair responsibilities

**Event 2: Pre-Harvest Inspection (last weekend of July)**

The highest-stakes inspection event. Anything that is going to fail during harvest must be caught here.

Agenda (half-day, 4 hours):
- Tractor: oil and filter change; hydraulic fluid; all belts; grease all zerks; battery
- Generator: oil change; spark plug check; carburetor service if stored since April
- Water system: submersible pump flow rate check; storage tank level; pressure tank
- Communication: radio battery tests; antenna inspection; channel frequency verification

**Event 3: Post-Harvest Winterization (first weekend of November)**

Transition to winter. Everything that might freeze must be protected. Damage from harvest-season load is documented and addressed before winter conceals it.

Agenda (full day, 8 hours):
- Water system: winterize above-ground plumbing; verify heat tape operation on pump house; drain exterior hose bibs and irrigation lines
- Generator: final oil change of the year; add fuel stabilizer to tank; run to distribute; store in heated space
- Chainsaw and outdoor power equipment: clean thoroughly; drain fuel or add stabilizer; inspect and repair any harvest-season damage; sharpen chainsaw chain
- Tractor: corrosion inspection of undercarriage (wash before inspection); grease all pivot points; park in covered storage
- Inventory: conduct full inventory of consumable parts stocked in the shop; order anything that has run low before winter supply chains tighten

**Event 4: Mid-Winter Electronics Day (third Saturday of January)**

Indoor work during the coldest and least-agriculture-active period of the year.

Agenda (half-day, 4 hours):
- Radio and communications: battery capacity testing; programming verification; antenna inspection (from indoors where possible)
- Solar system electrical inspection: connection tightness; wiring integrity; inverter internal inspection
- Battery bank: specific gravity testing; terminal cleaning; capacity assessment
- Knowledge work: update the shop logbook; review repair records from the past year; identify training gaps

### Institutional Memory — The Shop Logbook

The shop logbook is the single most important administrative tool in the community repair program. It converts individual experience into community knowledge.

**What to record in every entry:**
- Date
- Equipment (make, model, serial number if known)
- Reported problem
- Diagnostic steps taken and findings
- Repair performed (step-by-step if it was complex)
- Parts used (part numbers if available)
- Time to complete
- Who performed the repair
- Notes for next time (what was harder than expected, what would have helped to know)

**Over time, the logbook reveals:**
- Which pieces of equipment fail most often (candidates for replacement or parts pre-stocking)
- Which repairs are most time-consuming (where training investment has the highest return)
- Seasonal patterns (does the generator always fail in August? that's carburetor gum from summer storage)
- Individual skill development (who has performed which repairs; who is ready to train others)

Store the logbook in the shop (not in someone's home). Keep a copy of the most recent year's entries in a second location. The logbook is irreplaceable institutional memory — treat it as such.

**Digital backup of logbook and shop records:**

Photograph logbook pages monthly and store on the community's offline digital storage. If the shop logbook is ever destroyed, the photographs allow recreation of essential information. The Village Earth Appropriate Technology Library USB and the iFixit Kiwix archive should be stored with the logbook backup.

---

## Section 5: Economic Framework for Community Repair

Community repair infrastructure costs money to build and maintain. A community of 50–150 people needs a realistic economic model for how the tool library, repair shop, and training program are funded and sustained. This section provides that model.

### Capital Cost Estimates

**Phase 1 — Tool library establishment (Year 1):**

| Category | Items | Estimated cost |
|---|---|---|
| Hand tools (full set) | Hammers, saws, wrenches, pliers, screwdrivers, files, measuring | $400–$600 |
| Power tools (cordless) | 2 drills, circular saw, grinder, reciprocating saw + 8 batteries + 2 chargers | $800–$1,200 |
| Specialty tools | 2 multimeters, soldering iron, pipe cutter, pipe threader, come-alongs | $500–$800 |
| Safety equipment | Eye protection, hearing, gloves, fire extinguisher, first aid | $300–$500 |
| Tool storage | Metal shelving, storage bins, pegboard | $200–$400 |
| **Phase 1 total** | | **$2,200–$3,500** |

**Phase 2 — Repair shop (Year 1–2):**

| Category | Items | Estimated cost |
|---|---|---|
| Structure | Dedicated space (converted, not built) — electrical work and partitioning | $500–$2,000 |
| Workbenches | 2 × 8 ft heavy-duty benches (can be built from 2× lumber) | $200–$500 |
| Bench vises | 1 × 6" machinist vise + 1 × woodworking vise | $150–$400 |
| Lighting | 4–6 × LED shop lights | $150–$300 |
| Parts storage | Metal shelving, labeled bins, fastener organizer | $300–$600 |
| **Phase 2 total** | | **$1,300–$3,800** |

**Phase 3 — Parts pre-stocking (Year 1–3):**

| Category | 5-year supply estimate | Cost |
|---|---|---|
| Generator consumables | Filters, plugs, carburetor kits, oil | $150–$300 per generator |
| Water system parts | Bladder, capacitor, leathercups, valves | $200–$400 |
| Solar consumables | Fuses, connectors, wire | $100–$200 |
| Small engine | Chainsaw chains, filters, 2-stroke oil | $150–$250 |
| Welding consumables | Wire, electrodes, flux | $200–$400 |
| **Phase 3 total** | | **$800–$1,550** |

**Total community investment to establish full repair infrastructure:** $4,300–$8,850 over 2–3 years, or roughly $30–$60 per person for a 150-person community. This is a one-time investment that provides repair capability for a decade or more with maintenance.

### Ongoing Funding Model

The tool library and repair shop require ongoing funding for:
- Consumable replacement (blades, drill bits, sandpaper, oil, lubricants)
- Tool repair and replacement (tools wear out or are damaged)
- Parts pre-stocking replenishment

Funding mechanisms that have worked in community tool libraries and repair programs across the US [11]:

**Membership dues:** Annual membership fee of $20–$50 per household; sliding scale (pay what you can) maintains access for low-income members. A 50-household community at $30/year generates $1,500/year — sufficient for consumables and modest tool replacement.

**Equipment levy:** For community-owned systems (solar array, water pump, generator), a portion of the energy or water cost is designated as a maintenance fund. If the community charges $10/month per household for shared energy services, 10–15% ($1–$1.50) deposited to the repair fund generates $600–$900/year from 50 households.

**Repair event revenue:** Repair Cafés that serve the broader public (not just community members) sometimes charge modest fees or accept donations. A semi-annual "community repair day" open to neighboring households could generate supplementary income while building external relationships.

**Labor as currency:** In the mutual aid framework described in [community/03-mutual-aid-networks.md](community/03-mutual-aid-networks.md), repair services can be logged in a time banking system — community members who perform repairs for others earn credits that can be exchanged for other community goods and services.

### Repair vs. Replace — The Decision Framework

Not every failed piece of equipment should be repaired. Some decisions about repair vs. replace require a framework:

**Repair when:**
- The failure is a known consumable with available replacement parts (carburetor, leathercup, capacitor, fuse)
- Repair cost (parts + labor time) is less than 50% of replacement cost
- Replacement parts are in stock and supply chains are disrupted (during active disruption: repair everything that can be repaired)
- The equipment is otherwise in good condition and has useful life remaining

**Replace when:**
- The failure is in a structural or fundamental component (engine block, pump motor housing, inverter PCB) and repair would cost more than replacement
- The equipment is at or past its expected service life and has a history of repeated failures
- A better-suited replacement is available (e.g., replacing a generator-dependent system with solar to reduce generator dependence)
- The failure cannot be addressed with available skills and tools, and no specialist is accessible

**During active disruption:**
The calculus changes entirely during a disruption when supply chains are unavailable. During disruption:
- Repair everything that can possibly be repaired, even at high labor cost — you cannot buy a replacement
- Cannibalize failed equipment for parts to repair working equipment of the same type
- Document all repairs for post-disruption review (some decisions made under pressure will need to be revisited)
- Establish a "parts donor" category in the shop: failed equipment that cannot be repaired but may yield working components for future repairs

---

## Community Repair Infrastructure — Pre-Disruption Checklist

The following checklist is designed to be completed before a disruption begins. Each item addresses a gap that is easy to close with normal supply chains and very difficult to close without them.

**Immediate (within 1 month):**
- [ ] Download iFixit Kiwix archive (2.5 GB) and store on 2 USB drives
- [ ] Order Village Earth Appropriate Technology Library USB ($69)
- [ ] Print one-page maintenance schedule for each critical equipment type
- [ ] Conduct community skills census: who currently knows how to maintain which equipment?
- [ ] Identify 2 people per category who want to learn

**Short-term (1–3 months):**
- [ ] Establish community tool library: inventory what already exists; identify gaps
- [ ] Designate tool storage space and create checkout system
- [ ] Stock critical consumables: generator filters/plugs, hand pump leathers, pressure tank parts
- [ ] Schedule first community maintenance event (Saturday morning, 3 hours)
- [ ] Download and print service manuals for all major community-owned equipment

**Medium-term (3–12 months):**
- [ ] Build or designate community repair shop space (400+ sq ft)
- [ ] Install workbenches and bench vises
- [ ] Acquire specialty tools (multimeter, soldering iron, pipe threader)
- [ ] Train 2 people in each equipment category
- [ ] Hold first pre-harvest maintenance event

---

## Sources

[1] iFixit — Free Repair Manual and offline Kiwix archive: https://www.ifixit.com/ and https://www.ifixit.com/News/64006/download-every-ifixit-guide-for-free

[2] Village Earth Appropriate Technology Library — 1,050 books on self-reliance technology: https://villageearth.org/home/appropriate-technology-library/

[3] John Deere $99 million Right to Repair settlement, April 2026 — Farm Policy News (University of Illinois): https://farmpolicynews.illinois.edu/2026/04/deere-settles-class-action-right-to-repair-lawsuit/

[4] Sea Foam Motor Treatment — carburetor gum prevention and cleaning protocol: https://seafoamworks.com/small-engine-maintenance/

[5] Generator maintenance intervals — Mi-T-M and FIRMAN manufacturer guidelines: https://www.mitm.com/blog/generator-maintenance/

[6] Solar panel dust accumulation and performance loss — multiple sources including Enphase and Sandbar Solar: https://enphase.com/blog/homeowners/solar-panel-cleaning-and-maintenance-guide

[7] Right to Repair farm equipment background — National Agricultural Law Center: https://nationalaglawcenter.org/update-on-right-to-repair/

[8] John Deere settlement terms — Capital Press: https://capitalpress.com/2026/04/07/john-deere-agrees-to-pay-99-million-to-settle-right-to-repair-antitrust-suit/

[9] FTC suit against John Deere — National Agricultural Law Center: https://nationalaglawcenter.org/ftc-files-suit-against-john-deere/

[10] Right to Repair legislative landscape 2025–2026 — Iowa Capital Dispatch and state-level tracking: https://iowacapitaldispatch.com/2026/04/27/iowa-house-passes-right-to-repair-bill-on-farm-equipment/

[11] Community tool library governance models — USDN Sustainable Consumption Toolkit: https://sustainableconsumption.usdn.org/initiatives-list/tool-lending-libraries

[12] iFixit and Repair Café partnership details: https://www.ifixit.com/News/66508/ifixit-and-repair-cafe-join-forces

[13] Repair Café Foundation — 2,500+ locations worldwide: https://www.repaircafe.org/en/about/

[14] iFixit Kiwix offline archive — 44,000+ guides, 456,000+ images, 2.5 GB: https://www.ifixit.com/News/64006/download-every-ifixit-guide-for-free

[15] Community Boards conflict resolution and peer training model (referenced for training approach): Community Boards, San Francisco — peer mediation and community education: https://communityboards.org/

[16] Arnold & Porter analysis of John Deere settlement and Right to Repair landscape 2026: https://www.arnoldporter.com/en/perspectives/blogs/consumer-products-and-retail-navigator/2026/04/john-deeres-99-million-settlement-and-the-right-to-repair-landscape

[17] FARM Act (Freedom for Agricultural Repair and Maintenance) — 119th Congress federal legislation: https://www.congress.gov/bill/119th-congress/house-bill/5857/text

[18] Washington State Right to Repair Act (HB 1483, signed May 2025): https://statecapitallobbyist.com/technology/states-advance-right-to-repair-legislation-to-empower-consumers-and-cut-costs/

[19] iFixit multimeter repair guide — community-authored reference: https://www.ifixit.com/Guide/How+To+Use+A+Multimeter/25632

[20] Tool library governance — The Tool Library model (application and policies): https://thetoollibrary.org/wp-content/uploads/2016/04/TLApplicationSpring2019.pdf
