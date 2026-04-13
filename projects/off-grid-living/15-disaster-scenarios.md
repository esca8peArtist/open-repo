---
title: "Domain 15: Disaster Scenarios"
project: off-grid-living
status: complete
created: 2026-04-13
cross-refs: [03-water, 04-food-production, 05-food-preservation, 06-energy-power, 07-heating-cooling, 08-medical-health, 09-waste-sanitation, 10-tools-fabrication, 11-shelter-construction, 12-communications, 13-community-organization, 14-finances-trade]
---

# Domain 15: Disaster Scenarios

> The question is not whether a major disruption will affect your homestead.
> It is which disruption, and when. An extended power outage affects nearly
> every rural American at some point. A severe storm may destroy years of
> infrastructure work in hours. An economic shock can strand you without supply
> chains you didn't know you depended on. And the scenarios most people don't
> want to think about — pandemic, widespread civil breakdown, nuclear event —
> are exactly the ones that demand the most precise planning, because improvising
> under them is far more costly than having thought it through in advance.
>
> This chapter does not offer generalities. It offers specific, time-indexed
> response protocols for each major scenario, decision trees with named triggers,
> checklists organized by phase, and real numbers for what preparation costs.
> The goal is that when an event begins, you spend zero time figuring out what
> to do first. That thinking has already been done.
>
> **Cross-reference principle**: Every disaster scenario draws on the systems
> built in domains 3–14. This chapter synthesizes those systems under pressure.
> Where detailed technical procedures exist in other domains, they are referenced
> rather than repeated here.

---

## 15.1 Scenario Framework

### 15.1.1 Taxonomy

Disruption scenarios divide into four categories. Understanding the category matters
because it determines your primary response vector.

**Natural (Environmental)**
Driven by weather, geology, and climate. Timeline is usually hours to days of warning;
onset is fast; aftermath can last weeks to months.
- Severe weather: tornadoes, hurricanes, ice storms, blizzards, extreme heat
- Flooding: flash flood, riverine flood, dam failure
- Wildfire: structure fire, interface fire, regional conflagration
- Geological: earthquake, tsunami, volcanic eruption, landslide
- Extended drought: multi-year, affects food and water systems

**Technological / Industrial**
Failures of complex infrastructure. Warning is often zero. Duration ranges from hours
(local transformer failure) to permanent (irreversible infrastructure collapse).
- Extended grid failure (regional or national)
- Industrial accident: chemical plant explosion, pipeline rupture, dam failure
- Nuclear power plant accident (Chernobyl/Fukushima scale)
- EMP (electromagnetic pulse): natural (Carrington-class solar storm) or weapon-induced
- Supply chain collapse: fuel, pharmaceuticals, manufactured goods

**Societal**
Driven by human systems: economics, politics, conflict. Onset is gradual; the slow
ramp allows early adaptation — if you recognize the signals.
- Economic collapse: hyperinflation, currency failure, financial system seizure
- Supply chain disruption: multi-month or multi-year breakdown
- Civil unrest: local to widespread
- Armed conflict: regional or national; war on home soil
- Governance failure: loss of rule of law at regional or national scale

**Biological**
Driven by pathogens. Onset is detectable but deceptively slow; by the time it is
declared a crisis, community spread is already advanced.
- Pandemic: respiratory, vector-borne, food-borne at massive scale
- Agricultural disease: crop blight, livestock epidemic affecting food supply
- Deliberate bioterrorism: engineered pathogen release

### 15.1.2 Probability × Impact Matrix

The following matrix reflects US conditions. "Probability" is the chance that a
given homestead will experience this event in a 30-year planning horizon.
"Impact" rates severity assuming no preparation.

| Scenario | Probability (30 yr) | Impact (no prep) | Impact (prepared) | Priority |
|----------|--------------------|-----------------|--------------------|----------|
| Extended power outage (1–7 days) | Very High (>90%) | Moderate | Low | 1 |
| Severe storm / natural disaster | Very High (>80%) | Moderate–High | Low | 1 |
| Extended grid failure (30+ days) | Moderate (20–40%) | Very High | Moderate | 2 |
| Pandemic | Moderate (30–50%) | High | Low–Moderate | 2 |
| Economic disruption / inflation | High (60–80%) | Moderate–High | Low | 2 |
| Severe drought (multi-year) | Moderate–High (40–60%) | High | Moderate | 2 |
| Civil unrest (regional) | Moderate (15–30%) | Moderate–High | Low | 3 |
| Wildfire (interface) | Variable by region | High | Moderate | 2 (West) |
| EMP (Carrington-class solar) | Low–Moderate (5–15%) | Very High | Moderate | 3 |
| Nuclear power plant accident | Low (<5%) | High (if downwind) | Low | 4 |
| Nuclear detonation (fallout) | Very Low (<2%) | Extreme | Moderate | 4 |
| Widespread civil breakdown | Very Low (<5%) | Extreme | Moderate | 4 |

*Prioritization drives preparation budget allocation. Tier 1 preps deliver the
most expected value per dollar spent. Tier 4 preps are justified only after
Tier 1–3 preparations are solid.*

### 15.1.3 Compound and Cascading Events

The most dangerous scenarios are not single events but cascades: one disruption
weakens a system, which creates a second failure, which creates a third. The
historical record of major disasters is largely a record of cascades.

**Common compound pairings:**

| Primary Event | Common Cascade | Why |
|--------------|----------------|-----|
| Hurricane | Grid failure + flooding | Storm destroys transmission; flood cuts roads |
| Grid failure | Supply chain breakdown | Fuel pumps, refrigeration, logistics all fail |
| Pandemic | Economic disruption | Workforce reduction, supply chain, fiscal stress |
| Economic collapse | Civil unrest | Scarcity plus loss of institutional trust |
| Nuclear event | EMP + fallout | High-altitude detonation creates E1 EMP before fallout descends |
| Earthquake | Fire + infrastructure failure | Ruptured gas lines, broken water mains |
| Drought | Food system stress + economic pressure | Crop failure drives prices, debt, displacement |

**Cascade trigger recognition**: When you are in Scenario A, begin monitoring
specifically for the conditions that produce the secondary event. A major
hurricane in your region means you immediately assess grid status, fuel supply,
and road access — because those are the most probable second-order failures.

### 15.1.4 Cross-Domain Interlocks Under Disaster

Every domain in this guide becomes a disaster-response asset. Understanding the
dependency chain helps you prioritize what to protect first.

```
POWER (domain 6) ──┬── WATER PUMP (domain 3) ──── DRINKING WATER
                   ├── REFRIGERATION (domain 5) ── FOOD SAFETY
                   ├── COMMS (domain 12) ─────────── SITUATIONAL AWARENESS
                   └── MEDICAL EQUIPMENT (domain 8) ─ HEALTH MANAGEMENT

FUEL (domain 6) ───┬── HEATING (domain 7) ──────── HYPOTHERMIA PREVENTION
                   ├── GENERATOR BACKUP ────────────── CRITICAL LOAD SUPPORT
                   └── VEHICLE ─────────────────────── EVACUATION CAPACITY

FOOD STORES (domain 5) ─── CALORIES WITHOUT RESUPPLY ── INDEPENDENCE FROM SUPPLY CHAIN

COMMUNITY (domain 13) ──── LABOR, INTELLIGENCE, SECURITY, MUTUAL AID
```

**The critical insight**: Systems that are redundant and independent under
normal conditions become life-saving infrastructure under disaster. A homestead
with its own well, stored food, off-grid power, and a working radio is vastly
more resilient than a suburban house even if both buildings are physically identical.

---

## 15.2 Extended Power Outage

### 15.2.1 Context and Scale

Power outages affecting rural homesteads fall into three distinct scales:

- **Type 1 (hours to 3 days)**: Local distribution failure, tree down on line.
  Grid-connected homesteads disrupted; off-grid homesteads unaffected.
- **Type 2 (3–30 days)**: Regional storm, equipment failure, partial grid event.
  Both grid-connected and partial-off-grid systems stressed.
- **Type 3 (30 days to 12+ months)**: Major infrastructure failure, cyberattack,
  cascading grid collapse, Carrington-class solar event. Affects everyone.

A fully off-grid homestead with adequate battery storage, solar, and backup
generation experiences Type 1 as a non-event. Type 2 requires load management.
Type 3 requires full scenario response.

*This section addresses Type 2–3 scenarios. For Type 1, your existing off-grid
systems (see domain 6) handle it automatically.*

### 15.2.2 Hour-by-Hour and Day-by-Day Response Timeline

**Hour 0–1: Assessment and Inventory**

1. Confirm power is out — not just a breaker trip. Check neighbors, listen to
   weather radio, attempt cell and internet.
2. Note the time. This is "Hour 0" for all subsequent calculations.
3. Read battery state of charge (SOC). Record it.
4. Check fuel levels: generator, propane, vehicle, spare cans.
5. Check refrigerator and freezer temperatures. At normal temp, a full freezer
   holds safe temperature for 48 hours; a half-full freezer for 24 hours.
6. Check medications requiring refrigeration. Begin mental countdown.
7. Tune NOAA weather radio (162.400–162.550 MHz). Tune to local AM station for
   emergency broadcast.
8. Contact immediate community network (GMRS or ham radio check-in).
9. Make a written note of everything observed. Paper, not phone.

**Hour 1–6: Stabilization**

1. Implement Priority Load Shedding (see §15.2.4 below).
2. If generator is available and Type 2+ outage is confirmed: fuel assessment.
   Calculate days of runtime at current load (see §15.2.3).
3. Move critical temperature-sensitive medications to a cooler with ice if
   refrigeration is not stable.
4. Fill water storage containers if on a pressure-pump well — your pressure tank
   has limited reserve. Fill bathtubs, cisterns, every available container now
   before pressure fails.
5. Verify vehicles are fueled. Fill if below half-tank (fuel pumps need power).
6. Communicate with community: establish check-in schedule, compare notes on
   scope of outage, coordinate who has what resources.

**Day 1: Situation Confirmation**

1. Morning check-in: battery SOC trend, generator fuel consumed overnight.
2. Assess refrigerated and frozen food. Begin consuming most perishable items.
   Begin canning or dehydrating any food that will not last the duration.
3. Formally assess: is this Type 1 (expect restoration within 24 hours) or Type 2+?
   Type 1 indicators: power company is responding, you can reach them, scope is local.
   Type 2+ indicators: regional scope, no utility contact, no estimated restoration time.
4. If Type 2+: activate food and water conservation protocols.
5. Check weather forecast. Heat wave or cold snap during outage significantly
   changes resource consumption.
6. Document SOC and fuel at end of day to establish consumption rate.

**Week 1: Operational Rhythm**

1. Daily check-ins on community radio net (set times; see domain 12 §12.4).
2. Monitor and log battery SOC daily. If solar is producing, calculate net
   consumption. Adjust loads as needed.
3. Generator fuel budget: Type 2 outage means fuel resupply may be difficult.
   Prioritize essential loads only.
4. Food: refrigerator contents consumed or preserved by day 3–4. Chest freezer
   with full load safe to day 4–5 without power; open only to remove large
   batches for cooking and preservation.
5. Water: if on pressure well and pump is electric, determine remaining water
   in storage. Calculate daily consumption and burn-down rate.
6. Medical: check medication inventory status. Remote consultation options?
   (See domain 8 §8.7 for telemedicine protocols during grid-down.)
7. Community: begin resource pooling. Who has generator fuel to share? Who has
   well water to share? Who has medical needs that are time-sensitive?
8. Monitor scanner and ham radio for grid restoration estimates.

**Month 1: Adaptation Phase**

At one month, a Type 3 outage is confirmed. This is no longer an "outage" —
it is a new operational baseline. Adjust mentally and operationally.

1. Fuel conservation is paramount. Generator may need to be rationed to 2–4
   hours/day for critical loads (charging, refrigeration, pumping).
2. Lifestyle adaptation: LED lights, early sleep, daylight-centric work schedule
   dramatically reduces power needs.
3. Food: rely primarily on stored, preserved, and garden-fresh produce. Begin
   hunting and fishing if appropriate season.
4. Water: establish gravity-fed or manual-pump backup if electric pump is primary
   (see domain 3 §3.3 for hand pump options).
5. Community: formalize mutual aid agreements, establish regular work parties,
   assign labor to community-critical tasks.
6. Seek intelligence: ham radio nets, shortwave receivers, travelers. What is the
   scope nationally? Is there any restoration timeline?
7. Supply chain: what supplies are running low? What can be sourced locally
   vs. regionally? Begin planning trading expeditions.

**Month 3+: Long-Term Grid-Down Operations**

Assume no grid restoration is imminent. Operate as fully self-sufficient.

1. Energy: maximize solar, micro-hydro (if available), wood gasifier (if built).
   Generator reserved for emergencies and critical fabrication.
2. Food: seasonal production calendar operating. All preservation methods active.
3. Water: gravity or hand-pump system normalized; rainwater harvesting optimized.
4. Trade: engage regional barter networks. Surplus skills and goods become currency.
5. Infrastructure: begin hardening against whatever damaged the grid. Redundant
   backups to your backups.
6. Mental health: community social calendar. Purpose and contribution. (See
   domain 13 §13.7 for community mental health protocols.)

### 15.2.3 Generator Fuel Calculation

Knowing exactly how long your fuel will last is critical for rationing decisions.

**Base formula:**
```
Runtime (hours) = Fuel volume (gallons) / Fuel consumption rate (gal/hr)
```

**Consumption rate by generator size and load:**

| Generator Size | 25% Load | 50% Load | 75% Load | 100% Load |
|----------------|----------|----------|----------|-----------|
| 3,500W gasoline | 0.22 gal/hr | 0.37 gal/hr | 0.52 gal/hr | 0.68 gal/hr |
| 6,500W gasoline | 0.33 gal/hr | 0.53 gal/hr | 0.73 gal/hr | 0.95 gal/hr |
| 7,500W propane | 0.65 gal/hr | 0.97 gal/hr | 1.25 gal/hr | 1.55 gal/hr |
| 12,000W diesel | 0.40 gal/hr | 0.65 gal/hr | 0.90 gal/hr | 1.15 gal/hr |

*Propane consumption shown in liquid gallons. 1 gallon liquid propane ≈ 91,500 BTU.
Propane storage: 500-gallon tank = 400 usable gallons after bottom reserve.*

**Worked example:**
- 6,500W generator, 50% load (typical essential household loads)
- 30-gallon fuel can
- Runtime = 30 ÷ 0.53 = 56.6 hours ≈ 2.4 days
- For 30-day coverage at 4 hours/day: 4 × 30 × 0.53 = 63.6 gallons needed

**Fuel storage guidelines:**
- Gasoline: 6–12 months maximum with fuel stabilizer (PRI-G or Sta-Bil)
  Without stabilizer: 3–6 months before degradation.
- Diesel: 12–24 months with stabilizer (PRI-D). Treat for microbes (biocide).
- Propane: indefinite shelf life. Regulated by tank condition, not fuel age.
- Ethanol-free gasoline stores significantly better than E10/E15.

**Fuel safety**: Store in UL-listed containers, away from ignition sources, in a
ventilated outbuilding. Legal limits by jurisdiction for residential storage:
typically 25 gallons in detached outbuilding.

### 15.2.4 Priority Load Shedding

When battery SOC falls below 50% or fuel becomes scarce, shed loads in this order.
Do not skip directly to eliminating comfort items — systematic shedding extends
runtime far more than most people expect.

**Tier 1 — Never cut (survival-critical):**
- Well pump or water storage (minimum daily fill cycle)
- CPAP or other life-supporting medical devices
- Refrigeration for insulin or other critical medication requiring cold chain
- NOAA weather radio (draws <1W)
- Emergency communications (ham radio receive: <5W; transmit on schedule only)

**Tier 2 — Maintain as long as fuel/power available:**
- Chest freezer (most efficient per BTU of food preserved)
- Refrigerator (if medications not requiring it, consider cutting after Day 3 if
  food has been preserved/consumed)
- Water pump for daily bathing and sanitation
- Battery charging for tools and communications gear

**Tier 3 — Reduce but do not eliminate:**
- Lighting (switch to candles and kerosene lamps for ambient; reserve battery
  lighting for task-critical work)
- Inverter for 120V loads (run inverter only when actively using 120V devices,
  not continuously)

**Tier 4 — Cut immediately in emergency:**
- Electric water heater (propane or wood-heated water only)
- Washing machine (hand-wash or defer)
- Power tools except for emergency repair
- Entertainment electronics
- Electric cooking (propane or wood stove only)
- Air conditioning (fans and passive cooling only unless medical emergency)

**Load shedding math example:**
A 20 kWh battery bank at 80% usable = 16 kWh before damage.
Essential loads: well pump (500W × 1 hr/day = 0.5 kWh), freezer (100W avg =
2.4 kWh/day), fridge (150W avg = 3.6 kWh/day), lighting (50W × 5 hr = 0.25 kWh),
comms (30W × 4 hr = 0.12 kWh).
Total: ~6.87 kWh/day.
At 6.87 kWh/day with no solar: 16 ÷ 6.87 = 2.3 days of autonomy before damage.
With 2 kW solar (winter, 4 peak sun hours = 8 kWh/day): net draw = 0 kWh/day.
Load shedding pays enormous dividends in extended winter outages.

### 15.2.5 Communication Failure Cascade

When grid power fails, communications infrastructure fails in a predictable sequence.
Understand the timeline to plan your listening and transmission schedule.

| Timeframe | What Fails | What Survives |
|-----------|-----------|---------------|
| Hour 0–4 | Cell capacity (overloaded), internet at residential level | Cell voice (limited), text SMS, AM/FM broadcast |
| Hour 4–12 | Most cell towers (generator fuel exhausted), cable internet | AM/FM (stations on generator), NOAA weather radio |
| Hour 12–48 | Many AM/FM stations (smaller generators out), some cell towers | Major AM stations, ham radio (operator-powered), NOAA |
| Day 2–7 | Regional internet hubs (fuel supply chain fails) | Ham radio, shortwave, satellite (Iridium, Starlink on battery) |
| Week 1+ | All non-hardened infrastructure | Ham radio nets, shortwave broadcast, pre-positioned satellite |

**Your communication fallback sequence:**
1. Cell/internet — use while available
2. NOAA weather radio — continuous, battery-powered
3. GMRS radio — coordinate with neighbors within 5–20 miles
4. Ham VHF/UHF — regional repeater network and simplex
5. Ham HF — national and international nets, Winlink email
6. Satellite messenger (Garmin inReach, SPOT) — global one-way or two-way SMS
7. Shortwave receiver — BBC, VOA, amateur broadcasting, WWVH time signal

See domain 12 §12.6 for grid-down communication protocols and net schedules.

### 15.2.6 Food, Medication, and Water Impacts

**Refrigerated food safety — temperature tracking:**

| Hours Without Power | Refrigerator State | Freezer State |
|--------------------|--------------------|---------------|
| 0–4 | Safe if unopened | Safe if unopened |
| 4–8 | Marginal; consume leftovers | Safe if full |
| 8–12 | Danger zone for dairy, meat, leftovers | Safe if full |
| 12–24 | Discard dairy/meat/leftovers >40°F | Safe if full (half-full: marginal) |
| 24–48 | Discard most; root vegetables/hard produce OK | Half-full may have thawed edges |
| 48+ | Refrigerator contents lost | Full freezer: most still solid |

**Medication cold chain** (common medications requiring refrigeration at 36–46°F):
- Insulin: begin rotating from refrigerator to cooler with ice at Hour 4.
  Unopened vials: 28–30 days at room temperature (up to 77°F). Use this window.
  Open vials: 28 days at room temperature. Do not re-refrigerate once warmed.
- Some antibiotics (liquid): room temperature 10–14 days; powder formulations
  are stable for months without refrigeration.
- Vaccines: no storage option without cold chain; evacuation if vaccines are
  critical for community member (rabies PEP, immunocompromised patient).
- Biologics (EpiPen, some cancer drugs): treat as insulin — cooler, then room temp.

**Water impacts and response:**
If on a grid-powered well: pressure tank holds approximately 30–60 gallons post-outage.
- Fill all containers immediately at Hour 0 (see §15.2.2 Hour 0–1).
- Estimate family consumption: 1 gallon/person/day drinking/cooking minimum;
  add 0.5 gallon/person/day sanitation (sponge bathing, toilet flush).
- 4 people × 1.5 gal/day = 6 gal/day. A 60-gallon reserve lasts 10 days.
- Hand pump backup (see domain 3 §3.3): essential for Type 3 outage.
- Rainwater catchment: have collection containers pre-positioned at downspouts.

### 15.2.7 Grid Restoration Indicators and Reconnection Safety

**Indicators that restoration is approaching:**
- Utility trucks visible on main roads doing damage assessment
- Ham radio nets carrying official restoration estimates
- Partial restoration in adjacent areas (look for lights at night)
- Cell service restoration in the area (towers are often restored before residential)

**Reconnection safety checklist:**
Before reconnecting to restored grid power:
1. Ensure your transfer switch (manual or automatic) is in the OFF/GENERATOR
   position before grid power is restored — to prevent backfeed.
2. Inspect all circuits for damage from the event (lightning surge, physical damage).
3. Reset GFCI outlets and breakers as power is restored.
4. Test refrigerator and freezer temperatures before restocking.
5. For solar/battery systems: check that grid-tie inverter handshake is correct
   before enabling grid-tie mode. Some inverters require a 5-minute stable grid
   signal before they will reconnect.
6. Inspect any outdoor wiring or equipment for storm/freeze damage before
   energizing.

---

## 15.3 Severe Storm and Natural Disaster

### 15.3.1 Tornado

Tornado warning systems give 13 minutes of average lead time nationally; rural
areas often get less due to sparse radar coverage and topography.

**Pre-season preparation (annual, April–June in most US tornado-prone areas):**
- Designate and mark your shelter location: basement, storm cellar, or interior
  room on lowest floor away from windows.
- Stock shelter with: water (1 gallon/person), food (3-day supply), first aid kit,
  battery radio (NOAA), flashlights, blankets, medications, important documents.
- Test NOAA weather radio. Replace batteries. Confirm alert tone is enabled.
- Identify two exit routes from every building.
- Mark rally point with community if separated.
- Inspect outbuildings: secure anything that can become a projectile (tools,
  lumber, equipment). Chain fuel tanks to ground anchors.

**Warning received (Tornado WARNING, not Watch — Warning = tornado confirmed):**
1. Move to shelter immediately. Do not wait to see it.
2. Mobile homes: abandon immediately. Go to designated community shelter or
   lowest point in the most substantial nearby structure.
3. Interior rooms on lowest floor: bathroom, closet, under stairs.
4. Cover yourself with mattresses, blankets, heavy coats. Flying debris is
   the primary cause of injury.
5. Do not open windows (this myth costs lives — the pressure equalization
   benefit is negligible; the time cost is lethal).

**Post-tornado assessment:**
1. Wait for official all-clear before leaving shelter. Multiple cells can follow.
2. Check for gas leaks (smell, hissing sound). If suspected: do not use switches
   or matches. Evacuate and shut off main gas at meter.
3. Photograph all damage before cleanup (insurance documentation).
4. Check structural integrity before re-entering: foundation cracks, roof load,
   wall lean. A structurally compromised building can collapse with delayed timing.
5. Check on neighbors — designated community check-in protocol (see domain 13).
6. Document damage to community damage log.

### 15.3.2 Hurricane

Hurricanes provide days of advance warning. This is both an advantage and a
trap — it encourages optimism and delayed decision-making.

**Category-based decision matrix:**

| Category | Winds | Storm Surge | Default Action | Exception |
|----------|-------|-------------|----------------|-----------|
| Cat 1–2 | 74–110 mph | 4–8 ft | Shelter-in-place with prep | Low-lying, flood-prone: evacuate |
| Cat 3 | 111–129 mph | 9–12 ft | Shelter-in-place if structure is sound | Manufactured homes: evacuate; coastal: evacuate |
| Cat 4 | 130–156 mph | 13–18 ft | Evaluate structure seriously | Most wood-frame: evacuate |
| Cat 5 | 157+ mph | 19+ ft | Evacuate unless in hardened structure | Only concrete/steel below grade: shelter |

**Your structure evaluation:**
- Manufactured home or mobile home: always evacuate from Cat 2+.
- Wood-frame structure: shelter for Cat 1–2; evacuate for Cat 3+ if in surge zone.
- Concrete block or poured concrete with metal roof: shelter for Cat 3; evaluate for Cat 4.
- Elevation: storm surge (not wind) kills most hurricane victims. If you are below
  the projected surge elevation, elevation is more important than structure quality.

**72-hour pre-landfall checklist:**
- Fill all water storage containers (municipal water may fail).
- Run dishwasher and laundry — last chance for a while.
- Fill all vehicles with fuel.
- Fill propane tank if not full.
- Secure or bring in all outdoor items (anything under 50 lbs will become airborne at 100 mph).
- Install storm shutters or plywood over windows (3/4" plywood, screwed not nailed).
- Cut dead branches and weak trees close to structure — these are primary projectile sources.
- Position generator and fuel outside of likely flood zone.
- Photograph property and contents for insurance.
- Charge all batteries, devices, power banks.
- Withdraw cash from ATM (power outage will take ATMs offline).
- Fill bathtubs with water (WaterBob bladder is better: 100 gallons, $30).
- Inform community network of your shelter/evacuation decision.

**Post-hurricane:**
- Wait for official all-clear — eye wall passage feels like the storm is over; it is not.
- Do not drive through standing water: 6 inches of moving water can knock a person
  down; 12 inches can float a small vehicle; 2 feet can sweep away an SUV.
- Chainsaw work: fallen trees on structures. Safety first (domain 10 §10.2 chainsaw protocols).
- Begin generator operation for refrigeration within 4 hours.
- Boil water advisory: assume all municipal water is contaminated until cleared.

### 15.3.3 Ice Storm

Ice storms are uniquely destructive because of their effect on infrastructure: trees
and power lines fail under ice load, roads become impassable, and heating becomes
critical at exactly the moment power fails.

**Pre-season preparation (October, Northern US):**
- Wood stove or masonry heater fully operational with 3+ cords of dry wood staged
  (see domain 7 §7.1 for wood heating specifications).
- Propane backup: 250+ gallon tank, full before November.
- Water: heat tape on exposed pipes powered by generator-compatible circuit.
  Backup: shut off and drain pipes to vulnerable sections; keep above 55°F with
  wood heat in main structure.
- Alternative cooking: propane or wood cook stove. Electric stoves fail with power.
- Vehicle: tire chains or winter tires. Keep fuel above 3/4 tank through March.
- Chainsaw: maintained and fueled. Ice storm aftermath involves significant tree work.

**During ice storm:**
1. Stay indoors. Ice-coated surfaces cause falls; ice-laden trees drop branches without warning.
2. If heating fails: consolidate family into smallest, most insulated space. Body heat
   is significant in a small room; a 10×10 room with 4 people and candles holds 50°F
   when it is 20°F outside.
3. Do not use generators, camp stoves, or charcoal grills indoors. Carbon monoxide
   kills more storm victims than the storm itself.
4. Prevent pipe freezing: open cabinet doors under sinks on exterior walls. If power
   is lost, drip faucets to keep water moving in at-risk pipes.

### 15.3.4 Wildfire

Wildfire at the wildland-urban interface is the fastest-moving and most frequently
fatal of the natural disaster scenarios for rural homesteads.

**Defensible space standards (California NFPA, applicable broadly):**

Zone 1 (0–30 feet from structure):
- Remove all dead vegetation, dry leaves, pine needles.
- Space plants: shrubs 10+ feet apart, trees 10+ feet apart and trimmed to 6-foot clearance.
- Ember-resistant ground cover (gravel, bare earth) immediately around structure.
- No wood piles, mulch, or combustibles within 5 feet of structure.
- Ember-resistant vents (1/16" mesh or smaller).

Zone 2 (30–100 feet from structure):
- Thin trees to reduce canopy fire ladder.
- Remove dead vegetation.
- Mow grass to 4 inches or less.
- Stack wood piles at 30+ feet.

**Structure hardening:**
- Metal roof: standing seam steel or aluminum. Composition shingles ignite from embers.
- Enclosed eaves: open eaves are the primary ember entry point.
- Dual-pane windows: single pane fails at radiant heat temperatures a fire produces at 50 feet.
- Deck materials: composite or concrete instead of wood.
- Ember-resistant vents: $10–$30 each; replace standard vents.

**Evacuation decision matrix:**

| Condition | Action |
|-----------|--------|
| Fire 20+ miles away, no evacuation order | Monitor, prep go-bag, water house |
| Fire 10–20 miles, evacuation WARNING | Load go-bag, load vehicles, identify evacuation route |
| Fire 5–10 miles OR evacuation ORDER | Leave now. Do not wait for flames to be visible |
| Fire visible OR ember rain | Leave immediately. Do not stop for anything |

*Once you can see flames or smell smoke strongly, the safe departure window may be measured
in minutes. Every model of catastrophic wildfire fatalities shows victims who waited too long.*

**Go-bag contents (pre-packed, immediately accessible):**
- Documents: passports/IDs, insurance docs, medications list, land deed (or copies in cloud)
- Cash: $500 minimum
- Medications: 30-day supply of all critical medications
- Phone charger, battery bank
- 3-day food and water
- Change of clothes per person
- First aid kit
- Radio (GMRS or ham, NOAA receiver)
- Laptop/hard drive with critical data

**Pre-evacuation structure actions (15 minutes):**
1. Close all windows, doors, vents. Leave unlocked for firefighters.
2. Remove combustibles from deck and porch.
3. Connect garden hoses to exterior spigots; fill trash cans, buckets with water.
4. Move combustible patio furniture inside.
5. Shut off gas at meter.
6. Leave interior lights on (visibility for firefighters in smoke).
7. Leave a note on door: number of people and pets evacuated, destination.

### 15.3.5 Earthquake

Earthquakes provide zero warning. Preparation must be complete before the event.

**Structural vulnerabilities:**
- Cripple walls (short walls between foundation and floor): reinforce with plywood sheathing.
- Hot water heater and propane tanks: seismic straps prevent tip-over and gas line rupture.
- Masonry chimneys: most common structural failure; anchor to house framing.
- Large objects on high shelves: secure with museum putty or cabinet latches.
- Propane tank connections: flexible connectors only; rigid pipe cracks at fittings.

**During an earthquake:**
Drop — Cover — Hold On. Under a sturdy table, against an interior wall, away from windows.
Do not run outside (most injuries are from falling debris in doorways or while running).
Do not use elevator.

**Post-earthquake:**
1. Check for gas leaks before anything else. Natural gas and propane both create
   explosion and fire risk. If any doubt, open windows and evacuate.
2. Do not use electrical switches if gas leak is possible.
3. Expect aftershocks for hours to days.
4. Check water supply: municipal water main breaks are common; use stored water.
5. Assess chimney before lighting wood stove — a cracked chimney can cause
   house fire. Inspect for cracking, displacement.
6. Check propane system: inspect all connections, smell-test for leaks.

### 15.3.6 Flooding

**Site selection is the primary defense**: 100-year floodplain means a 26% chance of
flooding in a 30-year period. Buy FEMA flood maps before purchasing land (msc.fema.gov,
free). Elevation of structure above Base Flood Elevation (BFE) by 2–3 feet is the
minimum standard.

**Flash flood response:**
- Flash flood watch: monitor water levels in upstream drainages.
- Flash flood warning: move vehicles, equipment, and stored goods to high ground immediately.
- Never drive through moving water. The road surface may be gone under the water.

**Flood preparation (seasonal, if in flood-adjacent zone):**
- Critical equipment: generator, fuel, communications gear stored above projected flood level.
- Food and supply stores: above flood level, ideally second floor or high-ground outbuilding.
- Document backup: critical paper documents in waterproof bags; digital copies offsite.
- Sandbags: 100 pre-filled bags stored near structure; 3-inch sand layer stops 4-inch water flow.

---

## 15.4 Pandemic and Biological Event

### 15.4.1 The Off-Grid Advantage and Its Limits

An off-grid homestead with food and water independence begins a pandemic scenario
with significant structural advantages. The core transmission risk — repeated
contact with many infected people in public spaces — is dramatically reduced for
a household that does not need to visit grocery stores, gas stations, or workplaces.

The limits: supply chains for medications, parts, and inputs still require interface
with the outside world. Community members with jobs or school-age children in town
create ongoing exposure. Agricultural inputs (fuel, seed, feed) may require contact.
Perfect isolation for a rural homestead is more achievable than for an urban
household, but not automatic.

### 15.4.2 Isolation Protocols and Quarantine Setup

**Pre-pandemic preparation (always maintained):**
- 6-month food supply at minimum (see domain 5 §5.2 for storage quantities).
- 90-day supply of all routine medications (prescription stockpile protocols by state).
- PPE: N95 respirators (NIOSH-approved), nitrile gloves, eye protection, disposable
  gowns. Minimum stock: 100 N95 per person, 500 gloves per person, 50 gowns per household.
- Disinfection supplies: bleach (1 gallon = 48 gallons of 0.1% disinfectant solution),
  rubbing alcohol, soap.
- Medical monitoring equipment: pulse oximeter, thermometer, blood pressure cuff (§8.2).

**Quarantine zone design** (when an exposure has occurred):

Designate zones with physical separation:

```
CLEAN ZONE              BUFFER ZONE           QUARANTINE ZONE
(main household)     (transition space)    (separate room/outbuilding)
     |                      |                       |
 Full access           PPE required             Confirmed/suspected case
 No suspected          Decontamination          Dedicated toilet and basin
 exposure              protocols apply          Separate entry if possible
```

- Quarantine zone: ideally a separate structure or outbuilding. If not available:
  a room with its own exterior window for ventilation, a dedicated bathroom if
  possible, or a dedicated chamber pot.
- Duration of quarantine: follow current CDC guidance for the specific pathogen.
  For respiratory illness in the absence of specific guidance, use 10–14 days
  from last exposure or symptom resolution, whichever is later.
- Caregiver protocol: one designated caregiver uses N95, gloves, and eye protection
  for all contact. Same caregiver maintains consistent exposure instead of rotating.

**Decontamination station (buffer zone):**
- Bleach solution: 1 tablespoon liquid bleach per gallon of water. Effective against
  most pathogens including enveloped viruses. Prepare fresh daily (chlorine degrades).
- Hand sanitizer station: 70%+ isopropyl alcohol, or wash with soap for 20 seconds.
- Gown removal: remove before exiting buffer zone. Outer gloves off first, then gown,
  then inner gloves, then wash hands.

### 15.4.3 Symptom Triage and Medical Response

Cross-reference domain 8 §8.5 for complete respiratory illness management.

**Triage categories for pandemic respiratory illness:**

| Presentation | Home Management | Evacuation Trigger |
|-------------|-----------------|-------------------|
| Mild: fever <102°F, cough, fatigue, no dyspnea | Rest, hydration, ORS, ibuprofen/acetaminophen | Sustained temp >104°F or deterioration at 72 hrs |
| Moderate: fever >102°F, significant fatigue, oxygen sat 94–96% | Close monitoring, pulse ox q4h, increase fluids | O2 sat <94% or declining |
| Severe: O2 sat <94%, respiratory rate >30/min, confusion | Evacuate immediately | This IS the evacuation trigger |
| Critical: cyanosis, loss of consciousness | Evacuate immediately, begin supportive care | Now |

**Pulse oximeter use**: At sea level, O2 saturation should be 95–100%. Below 94% is
concerning; below 90% is dangerous and requires supplemental oxygen or evacuation.
Purchase a quality pulse oximeter before a pandemic: Masimo MightySat or Nonin OnOx
($150–$250) for accuracy. Cheap units may misread by 3–5%.

**Antivirals**: Oseltamivir (Tamiflu) is available by prescription for influenza; limited
stockpile options. For novel pathogens, treatment options may be unavailable. Supportive
care (hydration, fever management, positioning) is the primary tool.

**Cytokine storm recognition**: Some severe viral illnesses trigger an over-response of
the immune system — high fever persistent despite antipyretics, rapid deterioration,
confusion, rash. This is a medical emergency and requires evacuation.

### 15.4.4 Supply Chain Disruption Response

A pandemic that lasts 6–18 months will cause cascading supply chain disruptions.
Based on COVID-19 patterns (2020–2021), the typical failure sequence is:

| Month | What disrupts | Response |
|-------|---------------|----------|
| 1–2 | Retail consumer goods, N95, OTC medications | Activate existing stockpile |
| 2–4 | Wholesale supply chains, hardware, some food categories | Prioritize local/regional sourcing |
| 3–6 | Industrial inputs: fuel, fertilizer, animal feed | Reduce livestock where appropriate; secure fuel |
| 6–12 | Skilled labor shortages: healthcare, maintenance, agriculture | Community skill-sharing critical |
| 12–18 | Long-duration: structural economic damage, business closures | Barter networks, regional self-sufficiency |

**Activate pre-positioned stockpile** (domain 5 food preservation triggers):
- Supply chain alert (retail shelves showing >30% shortfall in staples): begin
  drawing on stockpile; do not attempt to resupply during panic-buying peak.
- Begin making preservation runs: pressure canning all fresh meat within 48 hours
  of purchase rather than freezing if power reliability is uncertain.

### 15.4.5 Community Cohesion vs. Isolation

The tension in a pandemic: the community you need for resilience is also the
primary vector of transmission.

**Resolution framework:**

Stage 1 (pre-confirmed community exposure): Maintain community ties. Limit exposure
to high-risk outside contacts. Screen visitors for symptoms. Keep informed.

Stage 2 (community exposure confirmed, disease is active locally): Shift to
small-group bubbles. Your immediate household + 1–2 trusted adjacent households
who have maintained the same protocols. Supply sharing continues. Physical meetings
with distancing and masking.

Stage 3 (severe outbreak, high mortality): Minimize all outside contact. Maintain
only essential supply exchanges. Radio communication replaces in-person meeting.
Quarantine any new arrivals for full incubation period before integration.

**Community health status OPSEC**: Do not broadcast the health status of specific
community members outside your core trust network. A community known to have sick
members may attract avoidance, which disrupts mutual aid exactly when it is needed.
Equally, a community broadcasting full health invites unwanted contact. Neutral
responses: "We're managing." "We're being cautious."

### 15.4.6 COVID-19 Lessons Applied to Homestead Context

COVID-19 (2020–2022) was a real-world test of pandemic response at all scales.
Key lessons directly applicable to off-grid homesteads:

**What helped:**
- Pre-existing food stockpiles: those with 3+ months of food experienced the 2020
  supply chain shock as an inconvenience rather than a crisis.
- Rural location: lower ambient transmission risk, less dependence on urban infrastructure.
- Skills diversity: homesteaders who could do their own construction, grow food,
  and provide services were economically resilient when supply chains failed.
- Community trust networks: those with established neighbors/community who could
  share resources and labor had better outcomes than isolated households.

**What failed:**
- Medication continuity: supply chains for prescription medications (including
  hydroxychloroquine, azithromycin) were disrupted. Lesson: 90-day minimum stockpile,
  multiple sourcing pathways including telehealth prescriptions.
- Information quality: misinformation at pandemic scale was itself a casualty hazard.
  Lesson: reliable primary sources (CDC, WHO, NEJM) plus ham radio nets providing
  local confirmed information.
- Mental health: isolation took severe tolls even in otherwise resilient communities.
  Social structure and scheduled community contact matter as much as food and water.
- Single-point dependencies: those relying on a single grocery store, single pharmacy,
  or single income source were most vulnerable. Redundancy in all systems.

**Long-duration (12–18 month) planning:**
At the 12-month mark, the primary challenges shift from acute health management to:
- Economic: how long can you maintain income? (See §15.5 and domain 14.)
- Psychological: community cohesion, purpose, social structure.
- Supply: what inputs have you been unable to replace? Where are the critical gaps?
- Agricultural: what plantings did you defer? What livestock did you reduce?

---

## 15.5 Economic Collapse

### 15.5.1 Early Warning Signals

Economic collapse is not binary. It progresses through observable stages. Recognizing
the early signals allows gradual adaptation rather than crisis response.

**Tier 1 signals (early, 6–18 months before severe disruption):**
- Sustained inflation >8% annually, especially in food and fuel
- Interest rates rising rapidly to combat inflation
- Dollar falling against multiple major currencies
- Supply shortages appearing in specific categories (semiconductors, lumber, food
  categories) without resolution
- Government debt reaching levels triggering creditor concern
- Regional bank failures or stress (FDIC activity increases)

**Tier 2 signals (intermediate, 3–6 months before acute disruption):**
- Sustained food inflation >15% annually
- Fuel shortages or rationing appearing
- Supply chain breakdowns affecting basic consumer goods (toilet paper scenario)
- Unemployment rising rapidly
- Dollar value dropping sharply (>20% in 6 months)
- Stock market significant correction (>40%)
- Banks restricting withdrawals or limiting transactions

**Tier 3 signals (acute, weeks to acute crisis):**
- Bank runs beginning
- ATM limits or cash rationing
- Fuel station queues and rationing
- Grocery store empty shelves in multiple categories simultaneously
- Government emergency declarations related to economic conditions
- Currency exchange rates becoming unstable or exchanges closing

**Response triggers:**
At Tier 1: begin debt reduction, food stockpiling, and asset reallocation.
At Tier 2: complete debt elimination, full stockpile activation, reduce financial
system exposure, increase physical hard goods.
At Tier 3: minimize financial system transactions, maximize self-sufficiency,
activate community mutual aid networks.

### 15.5.2 Inflation and Currency Devaluation Response

**Asset allocation principles under inflation:**

| Asset Type | Inflation Performance | Action |
|-----------|----------------------|--------|
| Cash savings | Loses value at inflation rate | Minimize; keep only 3-month operating reserve |
| Treasury I-bonds | Tracks inflation; limited to $10k/year | Max out annual purchase |
| Real estate (paid off) | Appreciates with inflation | Maintain; no leverage |
| Physical goods (food, fuel, tools) | Appreciates at or above inflation | Stockpile while prices rise |
| Productive skills | High and rising value | Invest in training |
| Productive land (owned outright) | Appreciates; produces ongoing value | Primary asset |
| Debt (variable rate) | Cost rises with inflation | Eliminate immediately |
| Precious metals | Holds value; limited utility | Modest hedge, not primary strategy |
| Barter goods (liquor, tobacco, coffee, ammo) | High demand, stable utility | Modest stock |

**Hard goods that hold value in economic disruption** (historically validated):
- Food staples: rice, beans, wheat, salt, cooking oil, sugar — these are money.
- Fuel: propane, gasoline, diesel — barter commodity during shortages.
- Medical supplies: antibiotics, pain relievers, first aid consumables.
- Tools: hand tools, mechanical tools — skills + tools are the primary economic unit.
- Ammunition: historically high demand/value during unrest, but legal and ethical
  considerations govern this trade.
- Seeds: open-pollinated vegetable seeds, grain seeds — foundational productive asset.
- Alcohol: ethanol spirits (production, barter, medical use).

### 15.5.3 Debt and Property Exposure Minimization

In an economic collapse scenario, debt is one of the greatest vulnerabilities.
Creditors can foreclose on productive land and structures precisely when you
need them most.

**Priority debt hierarchy:**
1. Mortgage on primary homestead: highest priority to eliminate or protect.
   Property tax: secondary — delinquent property taxes can trigger tax sale.
2. Business debt: eliminate or restructure.
3. Vehicle debt: pay off vehicles; own them outright.
4. Consumer debt: eliminate entirely.

**Property protection structures:**
- LLC: placing homestead land in an LLC can provide liability protection but does not
  protect against mortgage foreclosure.
- Homestead exemption: file in your state. Protects a defined amount of home equity
  from creditor claims in many states.
- Trust structures: irrevocable land trust for long-term asset protection, but
  complex; requires attorney.
- Paid-off land with no debt: simplest and most robust protection. Even if the
  dollar is worthless, a paid-off productive homestead has inherent value.

### 15.5.4 Income Bridge Runway Formula

"Income bridge runway" is the time your household can function at current standard
of living without any new income. Calculating it precisely defines how long you
can survive an income disruption.

**Formula:**
```
Runway (months) = Liquid Assets / Monthly Burn Rate

Monthly Burn Rate = Fixed Obligations + Variable Expenses - Homestead Self-Sufficiency Offset

Homestead Self-Sufficiency Offset = Food production value + Utility offset + Skilled labor value
```

**Example calculation:**
- Liquid assets: $45,000 (savings + liquid investments)
- Fixed obligations: $800/month (property tax $200 + insurance $300 + fuel $300)
- Variable expenses: $1,200/month (food, supplies, medical, vehicle)
- Self-sufficiency offset: $1,400/month (food production $800 + no electric bill $400 + firewood $200)
- Monthly burn rate: ($800 + $1,200) - $1,400 = $600/month
- Runway: $45,000 / $600 = 75 months = 6.25 years

Compare to a non-homestead household at $3,500/month burn rate with the same savings:
$45,000 / $3,500 = 12.9 months.

The homestead's self-sufficiency converts liquid assets into years instead of months.

**Cross-reference**: Domain 14 §14.3 for detailed income bridge and financial resilience planning.

### 15.5.5 Multi-Year Scenario Timeline

**Months 1–3 (Acute disruption):**
- Minimize all discretionary spending.
- Do not sell productive assets (land, tools, animals) under panic conditions.
- Activate all food production and preservation.
- Begin aggressive barter for needs you cannot produce.
- Maintain community relationships — these are your economic network.
- Identify which of your skills are high-value in a barter economy.

**Months 3–12 (Stabilization or deepening):**
- Establish regular trade relationships: who needs what you produce? What do you need?
- Reduce livestock to what you can reliably feed if animal feed supply is disrupted.
- Focus crop planning on highest-calorie, lowest-input crops.
- Assess which infrastructure investments have the best ROI in the current environment.
- Consider hosting apprentices or paying in food/shelter to expand labor.

**Months 12–36 (New normal or recovery):**
- Economic norms have either stabilized at a new lower level or recovery has begun.
- A homestead that survived to this point has demonstrated viability.
- Document what worked, what failed, what you wish you had prepared.
- Begin modest reinvestment in the most productive systems.
- Re-engage with any cash economy that has emerged.

**Barter economy principles:**
- Your most valuable barter assets are skills, not goods. A skilled welder,
  medic, or carpenter will always find trade.
- Perishable goods have little barter value unless you are trading locally and quickly.
- Tools and the knowledge to use them are more durable than the goods they produce.
- Do not reveal the full extent of your stores to non-core community members.
- Record all trades in a community ledger (see domain 13 §13.5 for trade ledger protocols).

---

## 15.6 Civil Unrest and Social Breakdown

### 15.6.1 Threat Tier Assessment

Civil unrest exists on a spectrum. Response should be calibrated to actual threat level,
not to fear. Over-response is expensive and socially damaging; under-response is dangerous.

**Threat Tier Framework:**

| Tier | Description | Geographic Scope | Examples | Response Level |
|------|-------------|-----------------|---------|----------------|
| 0 | Normal | N/A | Daily life | Standard operations |
| 1 | Local unrest | Single city, <50 miles | Riot after verdict, local protest | Monitor, avoid affected areas |
| 2 | Regional unrest | Multi-county, 50–200 miles | Urban unrest spreading to suburbs | Reduce travel, increase monitoring, community check-in |
| 3 | Widespread unrest | Statewide or multi-state | Political transition disruption, supply crisis | Minimize outside travel, community lockdown protocols |
| 4 | Societal breakdown | National or permanent | Governance collapse, mass displacement | Full defensive posture, no outside contact |

**Threat escalation indicators:**
- Tier 0→1: news of significant urban unrest, looting reported in nearest city
- Tier 1→2: unrest spreading to smaller cities and suburbs; law enforcement overwhelmed
- Tier 2→3: National Guard or military deployment; fuel or food supply incidents
- Tier 3→4: law enforcement ceasing to function; no restoration timeline; displacement of urban populations into rural areas

### 15.6.2 Security Perimeter Design

Security is layered. Each layer adds delay and detection, which multiplies response time.

**Layer 1 — Perimeter (property boundary):**
- Fencing: a defined boundary establishes legal and psychological ownership.
  No-climb 5-strand barbed wire: $0.08–$0.15/foot for wire; visible deterrent.
  High-tensile woven wire: better but costlier ($1–$3/foot installed).
- Gates: lockable. Heavy chain and quality padlock minimum.
- Posted signage: "No Trespassing," "Private Property." Legal and deterrence value.
- Observation: elevated vantage points to see approach. Trail cameras at entry points
  (solar-powered, cellular or SD card; $50–$200 each).

**Layer 2 — Perimeter approach detection:**
- Dogs: the most effective early detection system. Livestock guardian dogs (LGDs)
  already serving a farm function; highly attuned to unusual activity.
- Motion-activated lighting: solar-powered ($40–$120 per unit). Activates at night;
  floods approach lane; psychological deterrent.
- Trail cameras: motion-triggered photo/video on all vehicle approach paths.
- Noise deterrents: gravel driveways carry footfall and vehicle sound; avoid soft
  surfaces on approach paths.

**Layer 3 — Approach road / entry lane:**
- Single controlled entry point for vehicles: gate with locking mechanism.
- Clear line of sight from structure to gate: you should be able to see and identify
  arrivals before they can reach your door.
- Signage at entry: establishes that arrivals know they are approaching private property.

**Layer 4 — Structure:**
- Solid-core exterior doors (not hollow-core).
- Deadbolts on all exterior doors. Three-point locking systems add significant resistance.
- Window security film ($1–$3/sq ft): slows glass breach significantly.
- Reinforced door frames: most residential doors fail at the frame strike plate, not the lock.
  Install 3-inch screws into framing for all exterior strike plates.
- Interior safe room: one room with reinforced door and communication capability.

### 15.6.3 Information OPSEC — What Not to Broadcast

The "gray man" principle applied to a homestead: do not make yourself a target by
broadcasting your relative abundance.

**What to not publicly reveal:**
- Volume of food storage
- Exact quantity and type of weapons
- Generator or fuel stores
- Cash or precious metals holdings
- Community member names, skills, or vulnerabilities
- Specific security measures or their gaps

**What is acceptable to share with vetted neighbors:**
- General capability ("we're doing fine")
- Skills you are willing to trade
- General community structure
- Emergency contact protocols

**Social media and the homestead**:
Social media posts showing abundant harvests, full freezers, stacked firewood, or
large equipment are a security liability during Tier 2+ civil unrest. During stable
times, this content can serve legitimate purposes (marketing, community-building),
but when Tier 2+ conditions develop, stop posting anything that signals abundance or
reveals security arrangements.

### 15.6.4 Community Trust Building and Vetting

At Tier 3–4, community is both your greatest asset and your greatest vulnerability.
Unknown people seeking integration must be vetted before gaining access to core resources.

**Vetting principles (adapted from domain 13 §13.3):**

- **Observation period**: Before a new person or family has access to core resources,
  they should participate in community labor and demonstrate consistent behavior over
  a minimum of 2–4 weeks.
- **Reference check**: Who vouches for this person? What is the vetting status of the
  person vouching? Is there a chain of trust?
- **Skill assessment**: What skills does this person bring? Are they actually skilled
  (verify, don't just accept)?
- **Character assessment**: What were the circumstances of departure from their
  previous location? What is the story, and does it hold up?
- **Trial assignment**: Assign tasks that reveal character: Are they honest about
  what they can do? Do they work hard when no one is watching? Do they share fairly?

**Immediate aid without integration**: People in immediate medical distress, children,
or severely vulnerable individuals should receive humanitarian aid (food, first aid)
without requiring vetting. This is both an ethical standard and a community resilience
principle — communities known for humanity attract better outcomes than communities
known for exclusion.

### 15.6.5 Rules of Engagement: Legal and Ethical Framing

This section outlines a framework — not legal advice for your jurisdiction. Know
your state's specific laws before any defensive action.

**Legal framework principles:**
- Most US states recognize the right to defend yourself and others from imminent
  serious harm, proportionate to the threat.
- "Castle doctrine" states extend this right to your home without duty to retreat.
  Verify your state.
- Defense of property alone (not persons) has more variable legal status — in many
  states, deadly force to defend property (without threat to persons) is not legally justified.
- In a Tier 3–4 scenario where law enforcement is not functioning, legal frameworks
  may be inapplicable in practice — but documenting your actions and reasoning matters
  if law enforcement reconstitutes.

**Operational principles:**
1. **De-escalation first**: most threats are deterred by visible preparation, clear
   communication, and calm confidence. An armed community that communicates clearly
   ("We are a community; we will not provide additional resources; please move on")
   deters most opportunistic threats.
2. **Deadly force is a last resort and a burden you carry permanently**. The goal is
   to never reach that point.
3. **Community authority structure**: decisions about defensive force should not be
   made by any individual. Community leadership (see domain 13 §13.4 for emergency
   decision-making protocols) should govern significant defensive decisions.
4. **Documentation**: in any defensive encounter, document immediately (written, audio):
   time, sequence of events, actions taken, outcomes.

### 15.6.6 Cache Locations and Resource Dispersion

A single storage location creates a single point of failure. Resource dispersion
ensures no single event eliminates critical assets.

**Dispersion principle:**
- Do not store all food in one location.
- Do not store all fuel in one location.
- Do not store all communications equipment in one location.
- Do not store all medical supplies in one location.

**Practical dispersion layout:**

| Resource | Primary | Secondary | Cache |
|----------|---------|-----------|-------|
| Food (30 days) | Main structure root cellar | Outbuilding storage | Off-property (trusted neighbor, buried cache) |
| Water (72 hours) | Main structure tanks | Outbuilding gravity tank | Vehicle (50-gallon tank) |
| Fuel | Outbuilding (100 gal) | Second outbuilding (50 gal) | Buried (if legal) |
| Communications | Main structure Faraday | Vehicle Faraday kit | Buried PVC pipe cache |
| Medical supplies | Main structure | Vehicle first-aid kit | Community medical cache |
| Weapons/ammunition | Main structure safe | Secondary location | — |

**Buried cache guidelines:**
- PVC pipe (4-inch diameter, sealed end caps with O-ring): waterproof and durable.
- Oxygen absorbers and desiccant inside for any organic contents.
- Depth: 18–36 inches; below frost line in cold climates.
- Location marking: GPS coordinates plus physical landmarks; written record in
  encrypted document.
- Contents: rotate regularly; buried food has a shortened shelf life compared to
  climate-controlled storage.

### 15.6.7 Bug-In vs. Bug-Out Decision Matrix

This is one of the most consequential decisions in a crisis. Defaulting to either
choice without analysis is dangerous.

**Bug-In is almost always preferable when:**
- Your homestead has adequate food, water, power, and security.
- Roads are blocked, contested, or dangerous.
- Your destination is not more secure than your current location.
- You have livestock, crops, or infrastructure that cannot be abandoned.
- Weather conditions make travel dangerous.
- The threat is diffuse rather than directed at your location.

**Bug-Out is necessary when:**
- A direct and immediate physical threat is approaching (wildfire, flood, directed violence).
- Your supply systems have failed and cannot be restored.
- A chemical, biological, radiological, or nuclear threat has made your location
  uninhabitable.
- Community has dissolved and you are isolated and vulnerable.
- A medical emergency requires immediate evacuation to care.

**Bug-Out decision triggers (pre-defined, not situational):**

Define these in advance. During a crisis, your judgment is impaired by stress.
Pre-committing to specific triggers removes the deliberation at the worst possible time.

| Trigger | Action |
|---------|--------|
| Wildfire visible OR ember rain within 1 mile | Immediate bug-out |
| Evacuation order from official authority | Bug-out within 30 minutes |
| Armed hostile group within sight of property | Bug-out if overwhelmingly outnumbered; defend if equipped |
| Confirmed CBRN contamination of site | Immediate bug-out to pre-planned clean site |
| Food stores below 14-day supply with no resupply path | Bug-out to secondary location |
| Community security decision (vote): departure | Comply with community decision |

**Bug-out bag** (vehicle-loaded, always ready): same as Go-bag in §15.3.4 plus:
- Water: 5 gallons per person
- Shelter: tarp, sleeping bag, fire kit
- Navigation: paper maps of region, compass
- Cash: $1,000+ in small bills
- Community cache access: location notes, keys if applicable

**Destinations hierarchy:**
1. Pre-arranged secondary homestead location (friend, family, community member)
2. Pre-planned campsite in wilderness area with pre-positioned cache
3. Distant family location (>100 miles from origin)
4. Public shelter (last resort — loses privacy, security, and autonomy)

---

## 15.7 Nuclear Event

### 15.7.1 Scenario Types and Response Differences

Nuclear events require different responses based on the type of event.
Conflating them leads to either under-reaction (dirty bomb treated as nuclear
detonation) or paralysis (nuclear detonation treated as a dirty bomb).

**Type 1: Dirty Bomb (Radiological Dispersal Device — RDD)**
A conventional explosive device that scatters radioactive material. No nuclear
explosion occurs. The primary hazards are:
- Blast and shrapnel from conventional explosive (primary immediate threat)
- Radiological contamination of a localized area (city blocks to a few miles)
- Psychological impact and panic (often exceeds radiological risk in actual harm)
The effective radius of lethal radiological contamination from even a large dirty bomb
is typically measured in blocks to miles, not dozens of miles.

Response: Evacuate the immediate area. Shelter-in-place if you cannot evacuate
(building filters radiological particles). Decontaminate clothing and skin. Monitor
official guidance. This is not the scenario requiring fallout shelters.

**Type 2: Nuclear Power Plant Accident (Chernobyl / Fukushima Scale)**
Core meltdown or explosion releasing radioactive material into the atmosphere.
The plume trajectory depends on wind direction and weather. Key isotopes of concern:
- Iodine-131 (I-131): thyroid risk; 8-day half-life; Potassium Iodide (KI) is effective.
- Cesium-137 (Cs-137): soil contamination; 30-year half-life.
- Strontium-90 (Sr-90): bone absorption; 29-year half-life.

Response: If within 50 miles of plant and downwind, consider evacuation. Take KI
if instructed by authorities. Seal structure against air infiltration. Avoid fresh
produce from the area for weeks after release.

**Type 3: Nuclear Detonation (Strategic or Tactical Weapon)**
This requires the most extensive planning. Response zones:

- **Ground zero to ~1 mile** (for a 1 MT weapon; scales with yield): virtually
  unsurvivable without extreme pre-hardened deep bunker. Evacuation before the event
  is the only viable option.
- **1–10 miles**: significant blast, thermal, and prompt radiation. Hardened below-grade
  shelter required. Survival possible with preparation.
- **10–100+ miles**: fallout zone. This is the survivable zone with correct response.
  The quality of your shelter-in-place response in the first 24 hours determines survival.

### 15.7.2 Fallout Timeline and Radiation Physics

**The 7-10 Rule** (foundational principle of fallout survival):
Radiation from nuclear fallout decays predictably:
- For every 7× increase in time after detonation, radiation intensity decreases by 10×.
- 1 hour after burst = baseline intensity (100%)
- 7 hours = 10% of baseline
- 49 hours (≈2 days) = 1% of baseline
- 2 weeks = 0.1% of baseline

**Practical implication**: Surviving the first 24–48 hours in good shielding eliminates
the vast majority of your total radiation exposure. After 2 weeks, outdoor activity with
precautions is possible in most fallout zones (though long-lived isotopes remain).

**Fallout timeline for response planning:**

| Timeframe | What is happening | Your priority action |
|-----------|-------------------|---------------------|
| Hour 0 (detonation) | Blast, heat, prompt radiation | If not in blast zone: get indoors, shelter immediately |
| Hours 0–2 | Fallout begins descending (ground zero outward on wind) | Seal shelter, begin monitoring |
| Hours 2–24 | Peak fallout deposition; highest radiation levels | Remain in shelter, zero outdoor exposure |
| Hours 24–72 | Radiation declining rapidly (7-10 rule) | Remain in shelter; very brief outdoor trips only if critical |
| Days 3–14 | Continued decline; 1–2% of peak by day 14 | Short outdoor excursions possible; monitor dosimeter |
| Week 2+ | Most gamma radiation has decayed; residual contamination | Carefully re-emerge; food/water precautions continue |
| Month 1+ | Short-lived isotopes gone; long-lived remain | Soil testing before farming; water testing |

**Fallout arrival time** (distance from ground zero, 15 mph average wind):
- 10 miles: approximately 40 minutes
- 50 miles: approximately 3.3 hours
- 100 miles: approximately 6.7 hours
- 200 miles: approximately 13 hours

If you are 100+ miles from a detonation, you have hours to prepare shelter.

### 15.7.3 Shelter-in-Place Protocol and Shielding

**Shielding is everything.** The key metric is the Protection Factor (PF):
PF = how many times the building reduces radiation compared to outdoor exposure.

| Structure Type | Protection Factor | % Reduction |
|----------------|------------------|-------------|
| Open field | PF 1 | 0% |
| Wood-frame house (above grade) | PF 2–5 | 50–80% |
| Brick/masonry house (above grade) | PF 5–10 | 80–90% |
| Office building (middle floor, away from windows) | PF 10–100 | 90–99% |
| Basement (typical residential) | PF 10–50 | 90–98% |
| Basement (concrete block walls, 2+ ft earth overhead) | PF 50–200 | 98–99.5% |
| Root cellar / underground (3+ ft earth) | PF 200–1000 | 99.5–99.9% |

**Material shielding effectiveness** (halving thickness — depth that cuts dose by 50%):
- Water: 9 inches
- Concrete: 3.3 inches
- Earth: 3.6 inches
- Steel: 1 inch
- Wood: 11 inches
- Lead: 0.4 inches

To achieve PF 50, you need approximately 20–24 inches of earth or 15–18 inches of concrete.

**Shelter-in-place procedure:**

1. Get inside the best available structure immediately.
2. Move to the lowest floor, most interior space (interior walls absorb radiation;
   distance from windows is critical).
3. Seal the structure: close and lock all windows and doors. Tape window and door gaps
   with plastic sheeting and painter's tape. Cover fireplace/stove openings.
4. Turn off HVAC (fans and air systems bring outdoor air, and fallout particles, inside).
5. If time before fallout arrives: fill all containers with water (stored water is safe;
   fallout contamination is a surface phenomenon — water in sealed containers is protected).
6. Tune to emergency broadcast (battery-powered NOAA radio).
7. Do not go outside for the first 24 hours except under life-threatening emergency.
8. If you must go outside in first 24 hours: cover exposed skin completely, wear N95
   or improvised mask (multi-layer cloth, wet if possible), and decontaminate on return
   (remove outer clothing outside, shower thoroughly, bag and seal clothing).

**Homestead fallout shelter design** (upgrading root cellar or basement):

A root cellar built to domain 11 §11.7 specifications already provides substantial
protection. Upgrades for fallout shelter function:

- Seal ventilation: add a filter box with HEPA filter on the air intake. Positive
  pressure (air flows out, not in) is preferable; requires a small fan with backup power.
- Seal door with weatherstripping and threshold seal.
- 14-day supplies pre-positioned (2,000 cal/person/day + water at 1 gallon/person/day).
- Radiation monitoring equipment (see §15.7.4).
- Communications: battery-powered NOAA radio, hand-crank backup.
- Sanitation: portable toilet, waste bags, or 5-gallon bucket with lid and absorbent.
- KI tablets accessible at shelter location.
- Emergency contact list, paper records.

**CBRN shelter hardening cost estimate:**
| Item | Cost |
|------|------|
| HEPA ventilation filter unit (inline) | $80–$200 |
| Door sealing weatherstrip and threshold | $30–$80 |
| 2-week food supply (per person) | $200–$400 |
| 50-gallon water storage (WaterBob or cans) | $30–$80 |
| Geiger counter (see §15.7.4) | $100–$400 |
| KI tablets (130mg, 14-day supply per person) | $10–$20/person |
| Battery radio (NOAA) | $25–$60 |
| Total for 4-person shelter upgrade | $800–$1,800 |

### 15.7.4 Radiation Measurement: Instruments and Thresholds

**Instrument types:**

| Instrument | What it measures | Use case | Cost |
|-----------|-----------------|----------|------|
| Geiger-Müller counter | Gamma and beta radiation (cpm or mR/hr) | Active monitoring; real-time dose rate | $100–$400 |
| Dosimetry badge (TLD) | Cumulative exposure (mSv or rem) | Personal accumulated dose tracking | $10–$30 each |
| Electronic dosimeter | Real-time dose rate + cumulative | Best all-around; limited battery | $200–$600 |
| RADTriage card | Semi-quantitative cumulative | Backup; no battery required | $10–$30 each |

**Recommended minimum kit per household:**
- 1 Geiger-Müller counter: Radex RD1503+ ($80–$120) or Mazur PRM-9000 ($400).
  The Radex is adequate for most purposes; the Mazur is more accurate.
- 4 dosimetry badges: one per person; order from Landauer or REMCO ($10–$25 each/quarter).
- 2 RADTriage cards as no-battery backup.

**Dose thresholds (US regulatory and health reference levels):**

| Dose (cumulative) | Health Effect | Context |
|-------------------|---------------|---------|
| 1 mSv | Annual US public limit (non-emergency) | Normal background is ~3 mSv/year |
| 50 mSv | Radiation worker annual limit | No acute health effects; slight long-term cancer risk |
| 100 mSv | Threshold for detectable increased cancer risk | Long-term monitoring warranted |
| 250 mSv | Emergency worker protective action limit | FEMA/EPA emergency guidelines |
| 500 mSv | Nausea begins (acute radiation syndrome threshold) | Significant exposure |
| 1,000 mSv (1 Sv) | Mild Acute Radiation Syndrome (ARS) | ~10% 30-day mortality without treatment |
| 4,000–5,000 mSv | LD50/30 (dose lethal to 50% within 30 days) | Without medical care |

**Decision thresholds for shelter-in-place vs. emergence:**
- Outdoor dose rate <1 mR/hr (10 microSv/hr): generally safe for daily outdoor activities.
- Outdoor dose rate 1–10 mR/hr: brief outdoor activities acceptable (< 1 hour/day).
- Outdoor dose rate >10 mR/hr: limit outdoor time severely; shelter is preferable.
- Outdoor dose rate >100 mR/hr: emergency only; maximum 30-minute exposure.

Note: mR/hr to mSv/hr conversion: 1 mR/hr ≈ 0.01 mSv/hr (for gamma radiation).

### 15.7.5 Potassium Iodide (KI): Protocol

KI protects only the thyroid from I-131 (radioactive iodine). It does NOT protect
against other radiation or other organs. Use it only when indicated.

**Indicated when:**
- Nuclear power plant accident within 50 miles (upwind or uncertain wind direction)
- Nuclear detonation within 100–200 miles and explosion-produced I-131 contamination
  is possible (depends on weapon type)
- Official public health guidance recommends it

**NOT indicated when:**
- You are beyond 100 miles from a power plant accident
- The event is a dirty bomb (unless authorities specifically say I-131 is present)
- The event is more than 24 hours past (thyroid absorption window has passed)

**Dosing protocol (FDA guidance):**

| Age | Dose | Notes |
|-----|------|-------|
| Newborns (<1 month) | 16 mg | Only if no alternatives; monitor closely |
| Infants (1 month – 3 years) | 32 mg | Crush tablet, mix with fluid |
| Children (3–12 years) | 65 mg | Can swallow half a 130mg tablet |
| Adolescents (12–18 years) and adults 18–40 | 130 mg | Standard adult dose |
| Adults 40+ | 130 mg only if very high dose expected | Lower thyroid cancer risk with age |
| Pregnant/breastfeeding (any age) | 130 mg | Highest priority group |

**Timing**: Take as soon as possible before or within 3–4 hours of exposure.
Effectiveness drops significantly after 12 hours; limited benefit after 24 hours.

**Frequency**: Once daily for duration of exposure risk. Do not take more frequently —
excess iodine causes its own thyroid disruption.

**Sources**: ThyroSafe (65mg) and ThyroShield (liquid) are FDA-approved brands.
Purchase from ANBEX or pharmacy. Cost: $10–$20 for a 14-day supply per person.

**Contraindications**: Thyroid disease, iodine allergy, Dermatitis herpetiformis —
consult physician. Risk-benefit still generally favors use in high-dose scenarios.

### 15.7.6 Food and Water Safety After Nuclear Event

**Water safety:**

| Water Source | Safety Status | Notes |
|-------------|---------------|-------|
| Sealed tank/cistern (filled before event) | Safe | Surface contamination cannot penetrate sealed containers |
| Municipal water (before confirmation) | Assume unsafe | Municipal treatment may not remove radioisotopes |
| Well water (deep well, after fallout) | Generally safer | Soil filtration removes most particles; test before drinking |
| Running surface water (after fallout) | Unsafe for 30+ days | Receives direct fallout deposition |
| Rainwater collected after event | Unsafe for weeks | Wash-down from fallout-contaminated surfaces |
| Standing surface water | Unsafe indefinitely | High contamination potential |

Decontamination of water: activated carbon filter followed by ion exchange resin removes
most radioisotopes. Standard RO systems remove 90–95% of Sr-90 and Cs-137.

**Food safety:**

| Food Type | Concern | Guidance |
|-----------|---------|----------|
| Stored, sealed food (pre-event) | None | Fully safe |
| Root vegetables (in ground) | Low | Soil provides shielding; peel before eating; wash thoroughly |
| Leafy greens (grown post-event) | High | Avoid for 30–90 days depending on contamination levels |
| Fruit with intact skin (grown post-event) | Moderate | Peel thoroughly; avoid for 2–4 weeks |
| Grains (sealed storage, pre-event) | None | Fully safe |
| Milk (from grazing animals, post-event) | High | Avoid for 30 days minimum; I-131 concentrates in milk |
| Meat from grazing animals (post-event) | Moderate | Reduce grazing; supplement with stored feed |
| Eggs | Low–Moderate | Poultry fed stored feed produce safer eggs |
| Freshwater fish (post-event) | High | Avoid for 90+ days |
| Honey | Moderate | Depends on bee foraging area and contamination levels |

**Long-lived isotope management** (Cs-137, Sr-90, after first weeks):
- Deep tillage (12–18 inches) dilutes surface-deposited Cs-137 into soil volume.
- Adding potassium to soil competes with Cs-137 for plant uptake — lime and potash reduce
  crop Cs-137 by 50–80%.
- Zeolite added to soil binds Cs-137, reducing plant uptake.
- Prussian blue (pharmaceutical) taken orally reduces Cs-137 body burden — prescription required.
- Test soil with professional testing service before resuming food production.

### 15.7.7 EMP Correlation

A nuclear detonation at altitude (30–400 km above Earth's surface) produces a massive
electromagnetic pulse (EMP) before any fallout arrives. This is the primary vector of
infrastructure damage in a strategic nuclear exchange.

**EMP types from nuclear burst:**
- E1 (microseconds): highest frequency, instantaneous, damages electronics and microprocessors.
- E2 (milliseconds): similar to lightning strike; most surge protectors provide some protection.
- E3 (seconds to minutes): similar to Carrington-class geomagnetic storm; damages transformers
  and long-line infrastructure.

The combination means: first communications and electronics fail (E1), then grid
transformers fail (E3). Recovery timeline for E3-damaged large transformers: months to years.

**EMP hardening cross-reference**: See domain 12 §12.9 for Faraday cage construction,
EMP-hardened communications equipment list, and solar system surge protection.

Minimum: keep a backup NOAA hand-crank radio and a backup Geiger counter in a Faraday
enclosure (metal ammo can with gasket, or metal trash can with foil-sealed lid).
Cost: $30–$80 for a steel ammo can; $15–$40 in RF-absorbing foam.

### 15.7.8 Geographic Positioning Principles

**The primary rule**: do not be within 10 miles of a high-value target unless you have
a hardened below-grade structure.

**US high-value target categories:**
- ICBM fields (Minuteman III silos): Montana, North Dakota, Wyoming, Nebraska, Colorado
- SSBN submarine bases: Kings Bay (GA), Bangor (WA)
- STRATCOM headquarters: Offutt AFB (NE)
- Major cities (population >500,000): primary targets in countervalue strategy
- Major ports: Norfolk, San Diego, Pearl Harbor, Bremerton
- Key industrial infrastructure: refinery clusters (Houston, LA), power grid nodes

**Fallout plume modeling:**
The FEMA NUREG/CR-7002 document provides reference scenarios. HPAC (Hazard Prediction
and Assessment Capability) is the primary US government tool. Public access equivalent:
- nukemap.org: interactive nuclear effects calculator; enter weapon yield, target, see
  blast radii and fallout plumes.
- Ready.gov nuclear guidance: basic public shelter protocols.

**Prevailing wind considerations:**
US prevailing winds are generally west-to-east. A detonation over a western city means
the fallout plume extends eastward. A rural homestead 200 miles east of a city is downwind.
A homestead 200 miles west is upwind. Know your local prevailing wind direction and the
location of the nearest probable targets relative to your homestead.

### 15.7.9 Re-Emergence Timing and Contamination Assessment

**Minimum shelter time** by scenario:
- Power plant accident (no detonation): 24–72 hours (follow official guidance; I-131
  primary concern is first 2 weeks).
- Nuclear detonation, upwind (>200 miles): 48–72 hours before emergence with precautions.
- Nuclear detonation, direct fallout zone (50–200 miles downwind): minimum 2 weeks.
  At 2 weeks, outdoor radiation levels are typically <1% of peak.

**Re-emergence checklist:**
1. Take outdoor radiation readings with Geiger counter. Record.
2. If dose rate <1 mR/hr: proceed with caution.
3. Cover skin: long sleeves, pants, hat, N95 mask, gloves for initial assessments.
4. Check water sources: test before drinking any surface or rainwater.
5. Check food: garden produce contamination assessment (see §15.7.6).
6. Contact community via radio to share readings and coordinate.
7. Decontaminate clothing after outdoor work: shake outside, wash separately, dry inside.
8. Monitor cumulative dose on dosimeter. Stay under 50 mSv cumulative in first 30 days.

---

## 15.8 Cascading and Compound Events

### 15.8.1 Decision Priority Under Multiple Scenario Activation

When two or more scenarios activate simultaneously, decision-making becomes harder
because every resource allocation benefits one scenario and reduces capacity for another.
A pre-planned priority framework prevents paralysis.

**Triage principle for compound events**: Prioritize the threat with the fastest
onset and highest irreversibility first. A wildfire can destroy your homestead in
minutes; an economic disruption will take months to become acute. The wildfire is
the immediate priority even if the economic disruption is broader in scope.

**Irreversibility hierarchy** (from most to least urgent):
1. Immediate physical threat to life (fire, flood, armed threat) — act first, immediately
2. Time-critical health (medical emergency, radiation exposure in first hours) — act within hours
3. Short-term resource failure (power, water, fuel running out in days) — act within 24 hours
4. Medium-term supply failure (food running out in weeks) — plan within 48 hours
5. Long-term economic/social disruption — adapt over weeks to months

### 15.8.2 Common Compound Scenarios: Playbooks

**Compound Scenario 1: Hurricane + Extended Grid Failure**

The most common severe compound event in the US. Response:
- Day 0 (storm): execute §15.3.2 hurricane protocol.
- Day 0–3 (aftermath): execute §15.2.2 Day 1–Week 1 power outage protocol.
- Primary tensions: fuel consumption (generator for refrigeration and power) vs.
  debris clearance (chainsaw fuel consumption) vs. communications monitoring.
- Resolution: chainsaw work by daylight; generator for refrigeration in evening;
  minimize other loads. Community labor sharing for debris clearing.

**Compound Scenario 2: Pandemic + Economic Disruption**

The 2020–2021 COVID-19 experience demonstrated this compound. Response:
- Phase 1 (pandemic onset): execute §15.4.2 isolation protocols; activate stockpile.
- Phase 1 simultaneously: begin §15.5.1 Tier 1 economic warning response (debt
  reduction, hard goods acquisition).
- Phase 2 (supply chains failing): §15.4.4 supply chain response + §15.5.5 Month 1–3.
- Key tension: isolation (pandemic) vs. community interaction (economic resilience).
- Resolution: small, stable, vetted community bubbles. Reduce outside contact while
  maintaining tight inner community.

**Compound Scenario 3: Nuclear Detonation + Civil Unrest**

The cascade that follows a nuclear event in a major city includes:
- Mass displacement of urban population into rural areas
- Supply chain collapse
- Civil unrest in areas not directly affected by the blast

Response priority sequence:
1. First 24–48 hours: execute §15.7 nuclear fallout protocol; shelter in place.
2. Days 3–7: re-emergence assessment + tier threat assessment for incoming displaced populations.
3. Week 2+: community security posture (§15.6) + economic disruption response (§15.5).
4. Critical: the shelter-in-place requirement in the first 24 hours means you are
   not interacting with the displaced population at the moment they are most panicked
   and most dangerous. This is a feature, not a bug.

**Compound Scenario 4: Drought + Economic Disruption**

Multi-year drought reduces food production and drives regional economic stress.
- Year 1 (early drought): water conservation protocols (domain 3 §3.5); supplemental
  irrigation from stored sources.
- Year 2 (established drought): reduce water-intensive crops; increase drought-tolerant
  varieties; expand water storage capacity.
- Year 2+ (economic pressure): commodity prices rising — homestead production now has
  genuine barter/market value. Engage regional trade networks.
- Long-term: perennial drought-adapted species (established before drought) are
  the most resilient investment.

### 15.8.3 Resource Conservation Under Compound Pressure

When multiple scenarios are active simultaneously, resources deplete faster than
single-scenario modeling predicts. Conservation frameworks:

**Fuel hierarchy under compound stress:**
1. Heating/life safety: cannot reduce
2. Medical equipment: cannot reduce
3. Water: reduce to minimum viable (1 gal/person/day)
4. Refrigeration: consolidate to smallest, most efficient unit
5. Lighting: candles, kerosene, minimum battery
6. Generator hours: <4 hours/day for essential charging
7. Vehicle use: essential trips only; combine all errands

**Food conservation formula under extended scenarios:**
Normal caloric need: 2,000 cal/day/adult at rest
Caloric need under heavy physical labor (common in disaster aftermath): 3,000–3,500 cal/day
Minimum survival intake: 1,200 cal/day (not sustainable >3–4 weeks)
Comfortable reduced intake: 1,500–1,800 cal/day (sustainable long-term with health monitoring)

Extending a 6-month supply to 9 months by reducing to 1,600 cal/day is viable for most
healthy adults. Note the dietary balance tradeoff: reduced calories must still provide
adequate protein (0.8g/kg body weight minimum), essential fats, and micronutrients.

### 15.8.4 Community Role Assignment Under Cascading Stress

Pre-assigned roles reduce decision friction when cascading events hit.

| Role | Primary Function | Secondary Function |
|------|-----------------|-------------------|
| Security lead | Threat assessment, perimeter monitoring | Community communication |
| Medical lead | Health monitoring, triage, treatment | Medical stockpile management |
| Food/water lead | Resource conservation, food production | Preservation and rationing |
| Power/mechanical lead | Energy system maintenance, fuel management | Vehicle and equipment maintenance |
| Communications lead | Radio monitoring, community coordination | Information assessment and sharing |
| Community lead | Decision facilitation, morale, conflict resolution | External negotiation |

Under compound events, each lead reports to the community decision body daily. Decisions
requiring resource allocation above individual domain scope require community consensus
(see domain 13 §13.4 for governance under emergency).

---

## 15.9 Decision Matrix (Master)

The following master matrix maps scenarios to phases and priority actions. Use this
table for rapid orientation when an event begins. Execute the scenario-specific section
for detailed protocols.

**Threat Level Colors:**
- GREEN: Monitoring posture; no action required
- YELLOW: Preparation and heightened monitoring; no deployment
- ORANGE: Active response initiated; resource deployment
- RED: Maximum response; survival posture

| Scenario | Early Warning (YELLOW) | Onset (ORANGE) | Stabilization (ORANGE) | Recovery (YELLOW→GREEN) |
|----------|----------------------|----------------|----------------------|------------------------|
| Extended Power Outage | Monitor outage scope; fill water containers; check fuel | Load shed to essentials; inventory food/fuel; community check-in | Daily SOC and fuel logs; food preservation; community mutual aid | Grid restoration check; reconnection safety; restock |
| Hurricane | 72-hr checklist; decision: shelter vs. evacuate | Execute shelter or evacuation protocol | Post-storm assessment; generator; comms | Debris clearance; damage documentation; systems restoration |
| Tornado | Monitor NOAA; shelter stock inspection | Move to shelter immediately | Wait for all-clear; assess damage | Gas/structural safety check; community check-in |
| Wildfire | Zone defensible space check; go-bag ready | Evacuation decision matrix (§15.3.4) | If sheltered: seal structure; if evacuated: monitor from safe location | Return assessment; structure inspection; contamination check |
| Pandemic | PPE stockpile; medication supply; supply chain monitoring | Isolation protocol; symptom triage; community bubble | Quarantine management; supply chain adaptation | Gradual reopening; immunity assessment; mental health |
| Economic Collapse | Debt reduction; hard goods; Tier 1 signals | Tier 2 signals: eliminate debt; Tier 3: minimize financial system | Barter network; reduced expenditure; community mutual aid | New economic baseline; income stream assessment |
| Civil Unrest | Tier assessment; reduce visibility; community check-in | Security perimeter activation; OPSEC; comms monitoring | Community lockdown protocol; vetting new arrivals | Threat level reassessment; gradual normal operations |
| Nuclear (Fallout) | Fill water; shelter inspection; Faraday cache; KI check | Shelter-in-place immediately; seal structure; NOAA radio | Dose monitoring; 7-10 rule timing; food/water assessment | Re-emergence checklist; contamination testing; community coordination |
| EMP | Faraday cache verification; communications test | Unpack EMP-hardened comms; assess electronic damage | Radio nets for situational awareness; power assessment | Grid monitoring; equipment audit; community comms |
| Compound | Triage by irreversibility; role assignments | Execute highest-priority single-scenario protocol first | Sequence remaining responses; resource conservation mode | Prioritized recovery from each concurrent scenario |

---

## 15.10 Scenario Planning Exercises

### 15.10.1 Why Tabletop Exercises Matter

Every military and emergency management professional will tell you the same thing:
a plan that has never been practiced is not a plan. It is a document. The first time
you test your hurricane response should not be during an actual hurricane.

Tabletop exercises are structured discussions where participants walk through a scenario
step by step, identifying gaps, testing assumptions, and building shared understanding.
They require no special equipment and can be done in an evening.

Full-scale drills test physical execution: are the supplies where you thought they were?
Can everyone actually find the shelter? Does the generator start? How long does it take
to fill water containers?

**Combined approach**: run tabletops quarterly; run full-scale drills at least once per year.

### 15.10.2 Tabletop Exercise Format

**Participants**: all adult community members who will be involved in emergency response.
**Duration**: 60–90 minutes per scenario.
**Facilitator**: a neutral facilitator (community lead or external) who presents the
scenario and keeps discussion moving without leading the answers.
**Documentation**: one person records gaps, decisions, and follow-up actions.

**Structure:**
1. **Scenario brief** (5 minutes): Facilitator presents scenario conditions.
   Example: "It is 2 AM. Your NOAA radio has just issued a tornado warning.
   The tornado is 12 miles away moving at 35 mph toward your location."
2. **Round 1 — First 10 minutes** (15 minutes): Each person states what they do.
   Discussion. Where do decision conflicts emerge?
3. **Inject** (5 minutes): Facilitator adds a complication. "Your go-to shelter
   (root cellar) has standing water in it from last week's rain."
4. **Round 2 — Response to inject** (15 minutes): Re-plan. What now?
5. **Round 3 — Recovery** (15 minutes): Scenario is over. What did the response
   cost you? What was damaged? What do you need to do in the next 72 hours?
6. **After-action review** (15 minutes): What worked well? What would you change?
   What gaps need to be addressed before the next exercise?

**Documentation output**: After-action report with:
- Identified gaps (specific, not generic)
- Assigned corrective actions with owner and deadline
- Inventory corrections (update stored supply lists if reality differed)

### 15.10.3 Exercise Scenarios by Type

**Exercise 1: Extended Power Outage (Level 1 — Beginner)**
Scenario: Power out at 6 PM on a Friday in January. Temperature is 12°F.
No estimated restoration time. Cell service unreliable.
Test points: load shedding sequence, heating backup activation, community check-in,
food management, water backup.
Physical drill: actually run the generator and do load calculations; check propane level;
test the NOAA radio.

**Exercise 2: Wildfire Evacuation (Level 1 — Time-Critical)**
Scenario: Wildfire is 8 miles away. Wind is toward your property. Evacuation order
just issued. You have 20 minutes before roads may be impassable.
Test points: go-bag location and readiness, vehicle fuel, animal handling, document
location, designated rally point, community notification.
Physical drill: actually pack the go-bag; time yourself; confirm document location.

**Exercise 3: Medical Emergency During Grid-Down (Level 2 — Complex)**
Scenario: Extended power outage, Day 3. A community member has chest pain radiating
to left arm, sweating, nausea. Cell service down. Nearest hospital is 45 miles.
Test points: symptom assessment (domain 8 criteria), evacuation decision, vehicle
fuel, road conditions assessment, community medical kit location, pain management
protocol, documentation.
Discussion: does your vehicle have fuel? Who drives? Who stays? Who monitors the
medical kit? Who communicates with the hospital by radio in advance?

**Exercise 4: Pandemic Response (Level 2 — Duration)**
Scenario: A novel respiratory pathogen has been confirmed 60 miles away. Fatality
rate is 3%. Schools are closing tomorrow. Supply runs are now risky.
Test points: isolation protocol design, PPE stockpile assessment, quarantine space
identification, symptom monitoring protocol, 90-day supply assessment, community
bubble negotiation.
Discussion: who is the designated medical coordinator? What are the specific rules
for community members who have jobs in town?

**Exercise 5: Civil Unrest — Refugee Wave (Level 3 — Ethical Complexity)**
Scenario: Regional civil unrest. A city 80 miles away is experiencing widespread
disorder. Several vehicles of unknown people have appeared on the road past your
property over three days.
Test points: threat tier assessment, security perimeter status, OPSEC review,
community meeting and decision process, vetting criteria discussion, aid provision
standards.
Discussion: what is your policy on strangers seeking help? Under what conditions
do you help, and how? What is your community's decision-making process for this?

**Exercise 6: Nuclear Fallout (Level 3 — Technical)**
Scenario: 6:00 AM. Emergency broadcast states a nuclear detonation occurred 150 miles
away. Wind is currently from that direction at 18 mph. Fallout expected in 7 hours.
Test points: shelter readiness, Geiger counter location, KI tablet protocol, water
filling timeline, communication with community, HVAC shutdown, seal procedures, 14-day
supply status.
Physical drill: actually locate and test the Geiger counter; find the KI tablets; time
the shelter sealing procedure; check 14-day supply.

### 15.10.4 Annual Planning Calendar

| Month | Exercise Type | Domain Focus | Physical Drill |
|-------|--------------|-------------|----------------|
| January | Power outage tabletop | Heating backup, generator fuel | Test generator cold-start; check propane level |
| February | Medical emergency tabletop | Medical kit, evacuation route | Drive evacuation route; time to hospital |
| March | Community meeting: supply audit | Food and water storage | Full inventory of food, water, fuel, medical |
| April | Wildfire preparedness inspection | Defensible space, go-bag | Defensible space walkthrough; go-bag update |
| May | Tornado drill | Shelter readiness | Time shelter-to-shelter movement; check shelter supplies |
| June | Community security review | Perimeter, OPSEC | Trail camera check; perimeter walk |
| July | Economic disruption tabletop | Finances, barter readiness | Calculate current runway (§15.5.4 formula) |
| August | Full-scale evacuation drill | Bug-out bag, vehicles, animals | Full evacuation rehearsal with timing |
| September | Pandemic response tabletop | Isolation protocol, PPE | Count and inventory PPE stockpile |
| October | Nuclear/CBRN tabletop | Shelter, KI, dosimetry | Locate and test Geiger counter; check KI expiration |
| November | Communication drill | Radio nets, backup comms | Full communications test: all tiers, all devices |
| December | Annual after-action review | All domains | Review year's exercises; update all plans and inventories |

**Documentation requirement**: Every exercise produces a written record (even brief notes).
File it. Review it before the next year's same exercise. Are last year's gaps fixed?

---

## 15.11 Cost Table

### 15.11.1 Preparation Tiers

- **Minimal**: Bare-bones life safety. Buys survival for a short-duration event.
- **Moderate**: Practical homestead resilience. Covers most scenarios for most durations.
- **Comprehensive**: Full-spectrum, long-duration resilience across all scenario types.

Prices are 2025–2026 retail. Many items can be sourced used at 30–60% of new price.
Cross-reference domain 14 §14.5 for financing and prioritization framework.

| # | Item | Category | Minimal | Moderate | Comprehensive | Notes |
|---|------|----------|---------|----------|---------------|-------|
| 1 | NOAA Weather Radio (battery + solar) | Power Outage | $25 | $60 | $80 | Midland WR400 or Sangean |
| 2 | Generator (gasoline, 3,500–4,000W) | Power Outage | $500 | — | — | Essential for Minimal tier |
| 3 | Generator (propane, 7,000W) | Power Outage | — | $1,800 | — | Better for storage; Honda EU7000 |
| 4 | Generator (dual-fuel or tri-fuel, 12,000W) | Power Outage | — | — | $3,500 | Dual-fuel with propane/gasoline flexibility |
| 5 | Fuel storage (30-gallon gas cans, treated) | Power Outage | $120 | — | — | 6× 5-gallon UL-listed cans |
| 6 | Fuel storage (100 gallons, in-outbuilding) | Power Outage | — | $300 | — | Steel tank + pump |
| 7 | Propane system (500-gallon tank, full) | Power Outage | — | $1,500 | $2,000 | Amerigas/Ferrellgas; lease or own |
| 8 | Manual transfer switch (generator) | Power Outage | $150 | $300 | $600 | Reliance Controls 6-circuit |
| 9 | Battery bank + inverter (off-grid or backup) | Power Outage | — | $3,000 | $8,000 | 10–20 kWh LiFePO4 |
| 10 | Solar panel array (supplemental) | Power Outage | — | $2,000 | $6,000 | 2–5 kW DIY install |
| 11 | 6-month food stockpile (per adult) | Pandemic / Economic | $1,200 | $2,400 | $4,000 | Calorie-complete; cross-ref domain 5 |
| 12 | 12-month food stockpile (per adult) | Pandemic / Economic | — | $4,500 | $7,500 | Requires root cellar or equivalent |
| 13 | Water storage (55-gallon drums × 4) | All scenarios | $200 | — | — | Food-grade poly drums |
| 14 | Water storage (250-gallon IBC totes × 2) | All scenarios | — | $400 | — | Used food-grade IBC |
| 15 | Water filtration (Berkey + ceramic) | All scenarios | $280 | $350 | $400 | Big Berkey 2.25 gal/hr |
| 16 | Hand pump (well; Bison or Simple Pump) | Power Outage / All | — | $1,800 | $2,500 | Installed; cross-ref domain 3 |
| 17 | PPE kit (N95 × 100, gloves × 500, goggles) | Pandemic | $150 | $300 | $600 | Per household; restock annually |
| 18 | Medical stockpile (antibiotics, etc.) | Pandemic / Medical | $200 | $600 | $1,500 | Cross-ref domain 8; Rx required |
| 19 | Pulse oximeter (quality) | Pandemic | $30 | $150 | $250 | Masimo MightySat for Comprehensive |
| 20 | First aid kit (comprehensive) | All scenarios | $80 | $250 | $600 | Include suture kit, SAM splints |
| 21 | Go-bag (pre-packed, per person) | Storm / Bug-out | $150 | $300 | $500 | Per person; rotate contents annually |
| 22 | WaterBob bathtub storage bladder | Hurricane / Nuclear | $30 | $30 | $60 | 2 units for Comprehensive |
| 23 | Storm shutters or plywood kit | Hurricane | $100 | $400 | $800 | Pre-cut plywood or commercial shutters |
| 24 | Sandbags (pre-filled, 100 count) | Flooding | — | $150 | $300 | Store in outbuilding |
| 25 | Geiger-Müller counter | Nuclear | — | $120 | $400 | Radex RD1503+ (Moderate); Mazur PRM-9000 (Comprehensive) |
| 26 | Dosimetry badges (4-person kit, 1 year) | Nuclear | — | $100 | $200 | Landauer Luxel annual subscription |
| 27 | RADTriage cards (backup dosimetry) | Nuclear | $30 | $30 | $60 | No battery required |
| 28 | Potassium Iodide (KI) tablets (14-day supply per person) | Nuclear | $40 | $80 | $80 | ThyroSafe 65mg; 4-person household |
| 29 | HEPA air filter (inline, shelter ventilation) | Nuclear / CBRN | — | $120 | $300 | For shelter sealing |
| 30 | Faraday cage (ammo can + foam) | EMP / Nuclear | $50 | $80 | $200 | For comms equipment protection |
| 31 | Ham radio (handheld VHF/UHF) | All scenarios | $35 | $100 | $250 | Baofeng UV-5R (Minimal); Yaesu FT-60R (Moderate) |
| 32 | Ham radio (HF transceiver) | Extended outage / All | — | $800 | $2,500 | Xiegu G90 (Moderate); Icom IC-7300 (Comprehensive) |
| 33 | GMRS radios (family set, 4-pack) | All scenarios | $120 | $300 | $500 | Midland GXT1000VP4 |
| 34 | Garmin inReach Mini (satellite messenger) | All scenarios | — | $350 | $700 | + $15–$65/month subscription |
| 35 | Security cameras (solar, cellular) | Civil unrest | — | $400 | $1,200 | 4–8 unit perimeter system |
| 36 | Door reinforcement kit (3-inch strike plate screws, jamb armor) | Civil unrest | $80 | $200 | $400 | Door Armor or equivalent |
| 37 | Buried cache (PVC pipe, 4-inch, 8 ft) | Civil unrest | — | $80 | $200 | Per cache location |
| 38 | Document safe (fire-rated) | All scenarios | $100 | $300 | $600 | Honeywell or Sentry |
| 39 | Portable solar charger (100W foldable) | All scenarios | $80 | $150 | $250 | For device charging when generator off |
| 40 | Cash reserve (small bills) | Economic / Civil unrest | $500 | $2,000 | $5,000 | Physical cash; not bank-dependent |
| 41 | Precious metals (silver coins) | Economic collapse | — | $500 | $2,000 | 1-oz silver rounds; small denomination |
| 42 | Seed bank (open-pollinated, 1-year supply per person) | All long-term | $80 | $200 | $500 | Seed Savers Exchange or comparable |
| 43 | Barter goods (alcohol, tobacco, coffee, OTC meds) | Economic / Civil unrest | $200 | $500 | $1,500 | Rotate stock annually |
| 44 | Chainsaw (maintained, spare chains) | Storm recovery | $350 | $600 | $900 | Stihl MS 271 (Moderate); MS 391 (Comprehensive) |
| 45 | Tabletop exercise facilitation guide | All scenarios | $0 | $0 | $0 | This document + domain 13 |

**Tier Summary:**

| Tier | Approximate Total Investment | Coverage |
|------|---------------------------|----------|
| Minimal | $3,500–$5,500 | Basic storm and short-outage resilience; limited pandemic/nuclear prep |
| Moderate | $18,000–$28,000 | Comprehensive coverage for all common scenarios; nuclear basic; 6-month food supply |
| Comprehensive | $50,000–$80,000 | Full-spectrum resilience; 12-month food supply; long-duration nuclear capability; complete comms |

*These figures do not include land, structures, or core off-grid systems (solar, well, etc.)
which are covered in domains 3, 6, and 11. The costs above are supplemental disaster-preparation
layers on top of a functional off-grid homestead.*

**Cross-reference**: Domain 14 §14.2 for total homestead budgeting and priority spending.
For most homesteads, the Moderate tier represents the best risk-adjusted investment,
covering the scenarios with the highest probability while providing meaningful capacity
for the low-probability, high-impact events.

---

## Summary: The Five Principles

**1. Preparation depth determines response quality.**
A well-practiced community with 6 months of food and tested communication protocols
responds to disaster with deliberate action. An unprepared community responds with
panic. The gap in outcomes is not a matter of luck — it is a direct product of
preparation depth.

**2. Systems independence creates resilience.**
Each system (water, food, power, communications, medical) that is independent of
outside infrastructure is one fewer system that fails when the grid does. Build
independence progressively — every domain document in this guide contributes to
a compound resilience that is far greater than the sum of its parts.

**3. Community is the ultimate force multiplier.**
No individual or nuclear family can maintain full readiness across all scenario types
without community support. The mutual aid networks built in domain 13, the trust
established through trade and collaboration in domain 14, and the communication
protocols in domain 12 are not secondary to disaster preparation — they are disaster
preparation.

**4. Decision trees beat in-crisis thinking.**
Pre-defining your triggers (when to evacuate, when to shelter, when to bug out, when
to activate mutual aid) removes the most dangerous element from disaster response:
the compromised judgment of a person under extreme stress. Write your triggers down.
Review them annually. Practice them.

**5. Practice converts planning into capability.**
A tabletop exercise costs an evening and reveals gaps that would otherwise surface
only during an actual crisis. A full-scale drill costs a day and converts procedural
knowledge into physical memory. Both are non-negotiable investments for any community
that takes its resilience seriously.

---

*Cross-references: Domain 3 (water systems), Domain 5 (food preservation and storage),
Domain 6 (energy and power), Domain 7 (heating and cooling), Domain 8 (medical and health),
Domain 11 (shelter construction, CBRN hardening), Domain 12 (communications, EMP hardening),
Domain 13 (community organization, governance under emergency), Domain 14 (finances, trade,
economic resilience)*
