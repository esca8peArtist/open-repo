---
title: "Household Energy Coordination — 3-Household Scale"
scale: household
region: "Midwest US (Zone 5)"
tracks: "Rural + Suburban"
word_count: ~7600
citation_count: 32
created: 2026-05-17
cross_references:
  - individual/04-energy.md
  - household/01-household-coordination-overview.md
  - household/02-water-coordination.md
  - household/03-food-coordination.md
  - midwest/calendar.md
---

# Household Energy Coordination — 3-Household Scale
> **Region**: Midwest US (Zone 5) | **Tracks**: Rural + Suburban
> **Scale**: 3 households, 10–14 people, shared or adjacent parcels
> **Cross-references**: [individual/04-energy.md](../individual/04-energy.md) · [01-household-coordination-overview.md](01-household-coordination-overview.md) · [02-water-coordination.md](02-water-coordination.md) · [03-food-coordination.md](03-food-coordination.md) · [midwest/calendar.md](../midwest/calendar.md)

---

## The Most Important Finding

The critical insight from 3-household energy coordination is not that more solar panels are better — it is that distributed generation with a shared battery bank and a governed backup protocol outperforms any single large system in every failure mode that matters for Zone 5. Three households, each with an independent rooftop solar array, sharing a common LiFePO4 battery bank and a propane standby generator governed by a written state-of-charge protocol, can sustain essential loads through: a single household solar failure (partial shade, panel damage, ice loading), a 5–7 day overcast winter window, a grid outage during the August–October preservation peak, and a spring tornado knocking out a roof-mounted array. The same cluster relying on a single shared solar installation fails the moment a tree falls on the panels, a neighbor's roof needs replacement, or a winter ice storm drops generation to zero for five consecutive days.

Design for distributed redundancy first. Size for the worst winter week, not the best summer day. Govern the shared battery bank with the same clarity you bring to the shared cistern.

This document covers coordination design exclusively. It assumes each household in the cluster has already built or is building the individual-scale energy capabilities described in `individual/04-energy.md` — those cover individual solar sizing, battery fundamentals, inverter selection, propane heating basics, V2H vehicle integration, and winter generation minimums. This document picks up where that one ends: at the boundary between one household's energy system and the next.

---

## Quick Reference Card
*(Print and laminate — one copy per household)*

**Reference scenario**: 3 households (A, B, C), 12 people total, adjacent rural parcels, Zone 5 Midwest (USDA hardiness Zone 5, ASHRAE Climate Zone 5A, 99th-percentile winter design temperature 0°F [1]).

### Cluster Energy Baseline — 3 Households, 12 People

| Metric | Single Household | 3-Household Cluster | Notes |
|---|---|---|---|
| Baseline essential load | 3–5 kWh/day | 9–15 kWh/day | Refrigeration, lighting, water pump, comms |
| Full operations load | 8–14 kWh/day | 24–42 kWh/day | Adds canning, AC, heating assist |
| Winter solar generation (Dec–Jan) | 0.9–1.6 kWh/day per 400W array | 2.7–4.8 kWh/day total cluster | Per 400W array, 0.80 derate [2] |
| Summer solar generation (Jun–Aug) | 4.5–6.1 kWh/day per 400W array | 13.5–18.3 kWh/day total cluster | Surplus exceeds demand |
| Cluster battery target | — | 20–40 kWh usable | 2-day autonomy at essential loads |
| Generator backup target | — | 7.5 kW propane standby | Covers all essential loads simultaneously |
| Propane reserve (winter) | — | 200–300 gallons | 6–10 weeks at sustained heating demand |

### Load Priority Tiers — Emergency Load Shedding

| Tier | Loads | Action Trigger | kW Saved |
|---|---|---|---|
| **Tier 1 — Always On** | LED lighting, comms/radio, medical equipment, refrigerator | Never shed | ~0.5 kW |
| **Tier 2 — Essential** | Water pump (scheduled), basic cooking | Shed last; battery below 20% SOC | ~1–2 kW |
| **Tier 3 — Operational** | Food preservation (canning, dehydrator), workshop tools | Shed when battery below 40% SOC | ~2–5 kW |
| **Tier 4 — Comfort** | Air conditioning, electric water heating, entertainment | Shed first when solar falls short | ~3–8 kW |
| **Tier 5 — Discretionary** | EV charging, power tools, laundry/dryer | Only run during confirmed solar surplus | ~2–5 kW |

**SOC trigger thresholds** (shared battery bank, monitored centrally):
- 100% → 60%: Normal operations, all loads permitted
- 60% → 40%: Defer Tier 5 loads; no new EV charging
- 40% → 30%: Shed Tier 4; evaluate generator start
- 30% → 20%: Generator start mandatory; shed Tier 3
- Below 20%: Emergency only; all loads except Tier 1 suspended

---

## Section 1: Load Analysis — 3 Households

### Why Cluster Load Analysis Changes the Math

`individual/04-energy.md` covers the single-household load audit: cataloging loads, identifying winter minimums, sizing a system around the worst-case December consumption. At cluster scale, three things change: (1) aggregate demand creates economy of scale in generator sizing and battery purchasing, (2) load diversity — not every household runs peak loads simultaneously — reduces the peak-to-average ratio that determines hardware sizing, and (3) coordination creates opportunities for deliberate scheduling that no single household can achieve alone.

A cluster of three households does not simply triple individual household demand. Load diversity across households means that at any given moment, the cluster's aggregate demand is typically 60–75% of three times a single household's simultaneous peak — because one household is cooking while another is sleeping, one runs laundry while another is outside [3]. This is the central economic argument for shared infrastructure: you size the generator and battery bank for the cluster's aggregate diversity-adjusted demand, not for three simultaneous individual worst-cases.

### Baseline Load Catalog — Per Household, Zone 5

The following catalog reflects a Zone 5 rural household that has already shifted primary heating to propane or wood (per `individual/04-energy.md` recommendations) and relies on electricity for refrigeration, lighting, water pumping, and communications. Electric space heating is excluded from the essential-load baseline — it is addressed in Section 6 as a supplemental or emergency-only load.

**Per-household essential loads (all seasons):**

| Load | Watts (running) | Hours/day (winter) | Hours/day (summer) | Wh/day winter | Wh/day summer |
|---|---|---|---|---|---|
| Refrigerator (efficient 18 cu ft) | 100–150W avg | 24 | 24 | 1,200–1,800 | 1,400–2,100 |
| Chest freezer (20 cu ft, shared duty) | 60–80W avg | 24 | 24 | 720–960 | 900–1,200 |
| LED lighting (6 zones, 5W each) | 30W | 8 | 4 | 240 | 120 |
| Communications (router, radio, phones) | 20–40W | 16 | 16 | 320–640 | 320–640 |
| Laptop/tablet | 30–60W | 3 | 3 | 90–180 | 90–180 |
| Water pump share (750W, 2h/day shared) | 250W avg (cluster share) | 2 | 3 | 500 | 750 |
| CPAP/medical (if applicable) | 30–60W | 8 | 8 | 240–480 | 240–480 |
| **Per-household essential total** | | | | **3,310–4,600 Wh** | **3,820–5,470 Wh** |

**Per-household seasonal loads:**

| Load | Season | Watts | Hours/day | Wh/day | Notes |
|---|---|---|---|---|---|
| Central AC (2-ton unit) | June–Sept | 1,500–2,000W | 6–10 | 9,000–20,000 | Zone 5 cooling demand; highest summer load |
| Ceiling fans (3 zones) | June–Sept | 30–60W | 12 | 360–720 | Low-cost comfort alternative to AC |
| Electric supplemental heat (baseboard/strip) | Dec–Feb | 1,000–4,000W | 2–6 | 2,000–24,000 | Emergency only; propane/wood is primary |
| Canning kitchen (2-burner electric) | Aug–Oct | 2,400–4,800W | 2–4 | 4,800–19,200 | Cluster shared; see Section 8 |
| Food dehydrator (9-tray) | Aug–Oct | 600W | 10–12 | 6,000–7,200 | Cluster shared; see Section 8 |
| Washing machine | Year-round | 500–1,200W | 1.5 | 750–1,800 | Schedule for peak solar hours |
| Electric clothes dryer | Year-round | 4,000–5,800W | 1 | 4,000–5,800 | Defer to sunny days; line-dry otherwise |
| Workshop tools (drill, saw, etc.) | Seasonal | 800–2,500W | Occasional | Variable | Tier 5; solar surplus only |

### 3-Household Cluster Aggregate — Seasonal Demand

**Winter minimum scenario (December–February, essential loads only):**
- Per household: 3,300–4,600 Wh/day
- 3-household aggregate: 9.9–13.8 kWh/day
- With 0.70 load diversity factor: effective simultaneous peak ~7–10 kW
- Solar generation (3× 400W arrays, 2.8 peak-sun-hours, 0.80 derate [2]): ~2.7 kWh/day
- **Winter generation deficit: approximately 7–11 kWh/day must come from battery + generator**

**Summer full-operations scenario (June–August):**
- Per household including AC: 12–25 kWh/day
- 3-household aggregate: 36–75 kWh/day
- Solar generation (3× 400W arrays, 5.9 peak-sun-hours [2]): ~5.7 kWh/day
- **Summer deficit with AC running: 30–69 kWh/day — AC is not sustainably powered off a 400W-per-household solar system without grid tie-in**

The summer AC calculus reveals the critical cluster-scale planning decision: full air conditioning from solar alone at Zone 5 is not economically viable without solar arrays 5–10× larger than winter-minimum sizing [4]. The practical solution is the same one recommended in `individual/04-energy.md`: fans + thermal mass + passive design handle 85–90% of summer discomfort; AC is run selectively during heat events from the grid or generator, not as a baseline load.

**August–October preservation season peak:**
- Cluster canning kitchen active: adds 5–20 kWh/day
- Dehydrator active: adds 6–7 kWh/day
- But this peak coincides with the cluster's highest solar generation window (5.5–6.0 peak-sun-hours [2])
- Net: preservation loads can be solar-scheduled during peak generation hours (10 AM–4 PM), substantially reducing battery draw. See Section 8.

---

## Section 2: Distributed Generation Architecture

### Design Principle: Three Distributed Sources Feed One Shared Reserve

The architecture parallels the water system design in `02-water-coordination.md`: individual household arrays (three independent roof sources) feed a shared battery bank (shared cistern equivalent), with a propane generator as the backup source that activates when the shared reserve drops below threshold.

This design achieves a failure tolerance that no single large shared array can match:

| Failure Condition | Households Affected | Response | Recovery Time |
|---|---|---|---|
| One household array fails (ice, damage, shading) | 1 of 3 (33% generation loss) | Battery SOC drops slowly; generator may assist | Days–weeks (repair/replace) |
| Two arrays fail simultaneously | 2 of 3 (67% generation loss) | Generator starts; essential loads only | Days–weeks |
| All three arrays fail (tornado, widespread ice) | Full generation loss | Generator + propane heat; full load shedding | Until clear weather |
| Generator fails | Battery backup only | Emergency load shedding; solar charging resumes with sun | Hours (repair) |
| Shared battery bank fails | Arrays + generator still functional | Direct generation-to-load; no overnight storage | Days (repair/replace) |
| Grid outage (tied system) | All | Island mode; all systems operate independently | Grid restoration |

**No single failure leaves the cluster without power for more than 6 hours**, provided the battery bank is maintained above 20% SOC and the generator has fuel. This requires the same operational discipline as the water system's shared cistern: continuous monitoring and a written response protocol.

### Individual Household Solar Sizing — Zone 5 Specifics

The starting point for each household's solar contribution is its own essential load budget from Section 1, sized for December generation minimums. From `individual/04-energy.md`, the Zone 5 December generation per 400W array (0.80 derate) is approximately 896 Wh/day [2]. For a household with 3,500 Wh/day essential winter load, a 400W array covers only 25% of demand — which is exactly right if the shared battery bank and generator are sized to cover the gap.

**Individual array sizing logic for cluster participation:**

Each household installs the largest array its roof can support, up to a practical maximum determined by available south-facing roof area, structural load capacity (snow loading in Zone 5 is significant — minimum 20 lb/sq ft ground snow load, often 25–30 lb/sq ft in northern Illinois/Indiana/Iowa [5]), and inverter capacity.

Practical target per household: **1,200–2,400W (3–6 panels × 400W each)** on a dedicated south-facing roof section. At this scale:

| Array Size | December generation (0.80 derate) | June generation | Annual kWh |
|---|---|---|---|
| 1,200W (3 panels) | 2.7 kWh/day | 17.1 kWh/day | ~3,200 kWh |
| 1,600W (4 panels) | 3.6 kWh/day | 22.8 kWh/day | ~4,200 kWh |
| 2,400W (6 panels) | 5.4 kWh/day | 34.2 kWh/day | ~6,300 kWh |

**3-household cluster combined** (assuming 1,600W average per household): total 4,800W installed; December aggregate ~10.8 kWh/day; June aggregate ~68.4 kWh/day.

**Panel angle optimization for Zone 5**: Fixed tilt at latitude (41°N) optimizes annual output. For winter-priority systems, increasing tilt to 50–55° gains 10–15% more December generation at the cost of 5–8% of summer output [2]. In Zone 5 where winter is the binding constraint, steeper tilt is preferred. South-facing orientation is mandatory; deviations beyond 30° east or west lose more than 10% of annual output.

**Snow loading**: In Zone 5, panels must be rated for roof snow loads (20–30 psf in most Midwest counties [5]). A 400W monocrystalline panel typically weighs 20–25 kg; the array plus racking adds 3–5 psf to roof load. Structural assessment required before installation on older homes.

**Snow clearing**: Panels shed snow well on steep roofs (>30° tilt), but shallow residential roofs (15–20° pitch) may hold snow for 1–3 days per storm event, reducing generation to near-zero. The protocol: if a cluster household's array shows zero generation for more than 48 hours during a period when other arrays are producing, that household does a visual check and clears panels if safely accessible.

### Shared Battery Bank

The cluster's shared battery bank is the system's central coordination mechanism — the equivalent of the shared cistern. It buffers daytime solar surplus against nighttime and cloudy-day deficit, and it determines how long the cluster can run without generator support.

**Target sizing: 20–40 kWh usable capacity (LiFePO4)**

Sizing logic:
- Essential load per day (cluster): 10–14 kWh
- Target autonomy: 1.5–2 days (bridging a cloudy period without generator)
- At 80% DoD (LiFePO4 safe limit): bank size = (10–14 kWh × 2 days) / 0.80 = **25–35 kWh nameplate**
- Practical specification: 30 kWh nameplate capacity, 24 kWh usable

**LiFePO4 cold-weather performance in Zone 5:**

Zone 5A's 99th-percentile winter design temperature of 0°F (-18°C) is the critical planning figure. LiFePO4 batteries must not be charged below 0°C (32°F) — charging at subfreezing temperatures causes irreversible lithium plating on the anode, reducing capacity and creating safety risks [6]. Discharge continues safely to -20°C. Battery Management Systems (BMS) on quality LiFePO4 banks disconnect charging automatically below 0°C.

**For Zone 5, the shared battery bank must be located in a conditioned or semi-conditioned space** — an insulated basement, utility room, or purpose-built battery shed with a small heater. Even an unheated basement that stays above 32°F (common in Zone 5; ground temperature 3 feet down stays 45–55°F year-round) satisfies the charging cutoff requirement, while outdoor or garage placement does not.

At -10°C (14°F), LiFePO4 retains approximately 75–80% of rated capacity; at -20°C (-4°F), capacity falls to approximately 60% [6]. These figures apply to discharge — for charging, the BMS must ensure the cells are above 0°C before accepting current. In practice: on very cold mornings, morning solar generation may not be able to charge the battery until the bank's thermal mass warms through afternoon sun. A modest 100–200W heating element in the battery room, controlled by a thermostat set at 40°F, eliminates this issue at minimal energy cost.

**Cost estimate (2024–2026 pricing):**

| Component | Specification | Cost range |
|---|---|---|
| LiFePO4 cells, 30 kWh total | 280Ah 3.2V × 96 cells in 48V configuration | $8,000–$14,000 (DIY) / $15,000–$25,000 (pre-built) |
| Battery Management System | 48V 200A active balancing BMS | $400–$800 |
| Battery enclosure + wiring | Insulated steel cabinet, busbars, fusing | $600–$1,200 |
| Battery monitoring | Victron BMV-712 or equivalent | $120–$200 |
| **Total battery bank** | | **$9,000–$27,000** |
| **Per household (÷ 3)** | | **$3,000–$9,000** |

### Propane Standby Generator

Propane is the preferred fuel for Zone 5 off-grid generators over diesel for three reasons specific to the Midwest climate:

1. **Cold-start reliability**: Propane is a gas at atmospheric pressure and requires no glow plug, fuel heater, or viscosity management in cold weather. Diesel at -10°F requires engine block heaters and diesel fuel treatment; gasoline vapors condense unevenly in cold carburetors. Propane ignites reliably at -40°F without modification [7].

2. **Long-term fuel storage**: Propane stored in a proper steel tank has indefinite shelf life — there is no degradation, phase separation, or fuel stabilizer requirement. Gasoline stored more than 6–12 months degrades significantly; diesel stored longer than 12 months requires biocide additives and fuel polishing [7].

3. **Integrated infrastructure**: If the cluster is already using propane for primary heating and cooking (recommended in Zone 5 by `individual/04-energy.md`), a shared propane tank serves both heating and generator functions, simplifying supply logistics.

**Generator sizing for the cluster:**

The generator must be able to power all Tier 1 and Tier 2 loads simultaneously across all three households, plus have headroom for Tier 3 loads as needed. Essential simultaneous loads:

| Load category | Cluster total | Notes |
|---|---|---|
| Refrigeration (3 HH) | 900–1,200W | Always on |
| Lighting + comms (3 HH) | 300–600W | |
| Water pump (750W, 1 at a time) | 750W | High inrush (3–5× startup surge) |
| Medical equipment | 0–500W | Variable |
| Basic heating assist (1 HH) | 0–2,000W | If electric backup used |
| **Essential cluster total** | **1,950–5,050W** | |
| Startup surge headroom (1.5×) | | Generator must handle pump startup |
| **Recommended generator size** | **7,500–10,000W** | 7.5 kW covers all essentials; 10 kW adds operational loads |

**Propane fuel consumption model:**

A 7.5 kW propane generator at 50% load (3.75 kW, typical for essential-loads-only operation) consumes approximately 1.0–1.2 gallons of propane per hour [8]. At 75% load, consumption rises to 1.3–1.5 gallons/hour. At 100% load (7.5 kW, rarely needed), approximately 1.7–2.0 gallons/hour.

| Operating scenario | Generator load | Propane consumption | Tank depletion (500 gal tank) |
|---|---|---|---|
| Emergency essential loads | 50% (3.75 kW) | ~1.0 gal/hr | ~500 hours (~21 days continuous) |
| Normal backup with cooking | 65% (5 kW) | ~1.3 gal/hr | ~385 hours (~16 days continuous) |
| Full cluster operations | 85% (6.5 kW) | ~1.6 gal/hr | ~310 hours (~13 days continuous) |

In practice, the generator does not run continuously — it charges the battery bank during a 4–6 hour daily window and shuts down. At 6 hours/day at 50% load: 6 gallons/day. A 500-gallon propane tank at this rate lasts approximately 83 days — just under 3 months. A realistic winter with solar providing 20–50% of demand would extend this to 5–8 months of generator support capacity.

**Propane tank sizing recommendation:**

For a 3-household cluster in Zone 5 with propane as both primary heating fuel and generator backup: **500-gallon minimum, 1,000-gallon preferred** buried or surface tank per cluster. At winter heating consumption of 10–20 gallons/week per household (30–60 gallons/week cluster) plus generator use, a 500-gallon tank provides 8–12 weeks of combined operation before refill is needed. A 1,000-gallon tank extends this to 16–24 weeks — sufficient to bridge from November through March without a delivery if topped off in October.

**Critical winter performance note**: Propane in a surface tank (as opposed to buried) loses vaporization pressure as temperatures drop. Below -20°F, a surface tank may not generate sufficient vapor pressure to supply appliances reliably [7]. In Zone 5 where temperatures occasionally drop to -15°F to -25°F, either (a) use a buried tank (ground insulation maintains above -5°F at depth), or (b) maintain tank fill above 40% to ensure adequate liquid head for vaporization, or (c) install a tank heater blanket rated for propane service.

**Generator maintenance schedule:**
- Quarterly: run under load for 30 minutes; inspect fuel lines; check oil level
- Annually: oil change, spark plug replacement, air filter, coolant check (if liquid-cooled)
- Before winter: full service + test run at 75% load; verify cold-start procedure documented

---

## Section 3: Microgrid Control Logic

### System Architecture — Inverter as Grid Controller

In an islanded microgrid, the shared battery inverter/charger takes on the role the utility grid plays in a grid-tied system: it maintains voltage (120/240VAC) and frequency (60Hz) within tolerance for all loads and generation sources. The cluster's generating assets — solar arrays and the generator — all feed into this common AC bus.

The recommended architecture for a 3-household cluster uses a 48V DC battery bank connected to a **pure sine wave inverter/charger** (Victron Multiplus-II 48/5000 or Schneider XW+ equivalent) as the system's voltage and frequency reference [9]. All household loads connect to the AC output bus. Each household's solar array connects via a dedicated MPPT charge controller to the 48V battery bank. The generator connects to the AC input of the main inverter/charger, which then charges the battery while simultaneously supplying loads.

**Key technical function: frequency shifting for solar regulation**

When battery SOC approaches 100% and solar generation continues, the inverter raises AC frequency (60 Hz → 61–62 Hz) to signal AC-coupled microinverters to reduce output power, preventing overcharge. This frequency-shift mechanism, described in the Victron Energy AC-coupling documentation [9], allows the system to self-regulate without complex communication protocols — the frequency is the signal.

**UL 1741 and islanding safety:**

All inverters in the cluster must be UL 1741-listed [10] — the North American safety standard for distributed energy equipment. UL 1741 requires anti-islanding protection: if the cluster is grid-tied, inverters must disconnect automatically from the grid within 2 seconds of a grid outage (protecting utility workers from backfed power). For an intentionally off-grid cluster, UL 1741 SA/SB listing (the "smart inverter" variant) is preferred as it supports intentional islanding with advanced grid support functions [10].

### Load Shedding Sequencing

When solar generation falls short of cluster demand and the shared battery SOC declines, the cluster follows a defined load-shedding sequence. The goal is to protect the battery below 20% SOC at all costs — a deeply discharged LiFePO4 bank requires a controlled charge recovery cycle, and a fully depleted bank risks BMS lockout that requires manual reset.

**Automatic load shedding (implemented via smart outlets or programmable loads):**

Research on islanded microgrid load shedding [11] identifies priority-based approaches as the most reliable for residential clusters: loads are assigned priority indices, and lower-priority loads disconnect first as supply tightens. For the 3-household cluster:

**Shedding sequence (first shed to last shed):**
1. EV charging (instantaneous, 100% of EV load, ~7–11 kW) — disconnected when SOC below 60%
2. Electric clothes dryers (instantaneous, ~5 kW each) — disconnected when SOC below 60%
3. Air conditioning units (staged, starting with largest unit, ~1.5–2 kW each) — shed when SOC below 40%
4. Electric water heaters (if any — 4–4.5 kW each) — shed when SOC below 40%
5. Food preservation appliances — canning kitchen and dehydrators (2–5 kW) — shed when SOC below 30%
6. Water pump (scheduled; defer next pump cycle) — when SOC below 25%
7. Non-essential lighting and entertainment — when SOC below 25%
8. All loads except refrigerators, medical, and communications — when SOC below 20%

**Manual communication protocol** (for loads not automatically controlled):
- Cluster group message/radio: "SOC at 35% — activate Stage 3 protocol. AC off in all HH. Defer any laundry. Generator start assessment in 1 hour."
- Each household acknowledges within 15 minutes
- Generator start decision made by the designated "energy steward" for the week (rotating role)

**Generator start/stop logic:**

Generator start is triggered by SOC falling below 30% during a period when solar generation is confirmed unavailable (nighttime, confirmed overcast). It is not started for every cloud — the battery's purpose is to bridge short gaps.

**Start criteria (all three must be true):**
1. Shared battery SOC below 30%
2. Solar generation forecast for next 4 hours is below 25% of nominal (cloud cover confirmed)
3. Essential loads cannot be sustained beyond 6 hours at current draw rate

**Stop criteria:**
1. Battery SOC reaches 85% (stop charging; solar can maintain from here)
2. Or: solar generation has resumed at >50% of nominal for 30 minutes

**Generator runtime efficiency**: Propane generators achieve maximum fuel efficiency at 50–75% of rated load [8]. Running a 7.5 kW generator at 1–2 kW (charging only, no heavy loads) wastes fuel. The energy-efficient protocol is to concentrate generator runtime: run the generator at 60–75% load for 4–6 hours (charging battery + running heavy cluster loads simultaneously) rather than 12 hours at 20% load. Schedule generator operation during the time when the cluster's simultaneous loads are highest — typically morning cooking + water pumping + heating assist — to maximize output utilization per gallon of propane.

---

## Section 4: Winter Outage Resilience — Midwest Critical Period

### The Fundamental Winter Mismatch

Zone 5 creates the most demanding possible constraint for solar-backed resilience: peak heating demand coincides exactly with minimum solar generation. In December–January, the cluster faces:

**Demand peak**: Zone 5's 99th-percentile heating design temperature of 0°F [1] drives maximum heating load. A well-insulated 1,500 sq ft Zone 5 house requires approximately 20,000–35,000 BTU/hour at design temperature with R-49 ceiling, R-20 walls, and modern windows — equivalent to 6–10 kW of continuous electric heating [1].

**Supply minimum**: A 1,600W array generates approximately 3.6 kWh on a clear December day (2.8 peak-sun-hours × 1,600W × 0.80 derate [2]). On an overcast day, generation may be 10–25% of that — 360–900 Wh. Three household arrays (4,800W total) generate ~10.8 kWh on a clear December day and as little as 1–2.7 kWh on a heavy overcast day.

**Practical conclusion**: Zone 5 winter survival cannot rely primarily on electrical heating from a solar-battery system sized at the cluster scale described in this document. Primary heating must be propane or wood; electrical systems supplement and handle failure modes.

### Wood Heat Integration

Wood heating is the most cost-effective and resilient winter load reduction strategy available in a rural Zone 5 cluster. A wood stove or rocket mass heater replacing electric supplemental heat removes the largest variable load from the electrical system during the highest-demand, lowest-generation period.

**Rocket mass heater vs. conventional wood stove:**

A rocket mass heater burns wood in a highly efficient combustion chamber, directs exhaust through a thermal mass bench or wall system, and releases stored heat slowly over 8–12 hours — achieving combustion efficiencies of 85–90% [12]. Comparison with conventional wood stoves (60–75% efficiency [12]):
- Fuel use: 50–80% less wood per BTU delivered to space
- A conventional wood stove heating a 1,200 sq ft Zone 5 home might burn 4–5 cords/season; a rocket mass heater achieves the same comfort with 1–2 cords
- Wood sourcing: rural Zone 5 clusters typically have access to standing deadwood, pruning waste, or sustainably managed woodlot — 1–2 cords per household per season is achievable within a few acres of managed woodland

**Passive solar integration:**

A properly designed passive solar residence in Zone 5 reduces heating demand by 25–37% compared to an identical home without passive solar design [13]. The design principles: south-facing glazing (8–12% of floor area), thermal mass (concrete, brick, or stone floors in the sun path) sized at 6× the glazing area, roof overhangs sized for the latitude (at 41°N, an overhang depth equal to 1/4 of window height fully shades in summer but admits full winter sun [13]), and insulation above code minimum.

For cluster coordination: Household A's passive solar design may be retrofittable (add south-facing glazing, add thermal mass), while Household B's north-facing orientation limits passive solar gains to 10–15%. The cluster's winter energy planning should account for these differences in each household's actual heating demand rather than assuming identical loads.

### 5–7 Day Overcast Window Protocol (Critical Scenario)

A sustained winter overcast window — 5–7 consecutive days without meaningful solar generation — is the cluster's most severe regular threat in Zone 5. Illinois and Indiana winters average 50–60% cloud cover; January and February each average multiple weeks with less than 3 hours of daily sun [2]. A 7-day window with 10% generation and essential loads only (10 kWh/day) drains a 30 kWh battery bank in less than 3 days, requiring sustained generator support.

**Protocol for extended overcast window:**

*Day 1 (overcast confirmed)*: Monitor SOC; defer all Tier 4–5 loads; alert cluster households.

*Day 2 (SOC below 60%)*: Shed all Tier 4 loads (AC, electric water heating, entertainment); activate wood heat as primary in all households; switch to propane cooking to reduce electric stove load.

*Day 3 (SOC below 40%)*: Generator start, Stage 3 protocol. Run generator 5 hours/day charging battery from 30% to 85%. Defer all Tier 3 loads. Begin rationing propane (calculate remaining supply against expected window duration).

*Day 4–7 (sustained)*: Generator 5–6 hours/day; essential loads only; wood heat primary; water pump schedule condensed to one 2-hour session per day (fill cistern; rely on gravity distribution). Monitor propane gauge daily.

*Recovery*: When solar generation returns, confirm battery to 90% SOC before de-activating Stage 3 protocol.

**Propane consumption during a 7-day window** (generator + heating):
- Generator: 6 hours/day × 1.0 gal/hour = 6 gal/day
- Heating (3 HH × propane backup): 3 gal/day/household = 9 gal/day
- Total: ~15 gallons/day × 7 days = 105 gallons
- Against a 500-gallon tank at 200 gallons remaining: adequate. Against 100 gallons remaining: crisis.

**Standing reserve requirement**: Cluster propane tank must never drop below 150 gallons before January 1. This reserve covers a 7-day winter outage scenario and provides margin for delivery delays (rural delivery can lag 1–2 weeks in severe winter weather).

---

## Section 5: Water System Integration

### Load Interaction with Household/02-Water-Coordination

The cluster's water system (detailed in `02-water-coordination.md`) creates specific energy loads that must be coordinated with the energy system's SOC protocols. The critical interface points:

**Well pump energy load:**

The reference cluster uses a 750W submersible well pump per household [14]. Each pump serves its own household's well; only the pump serving the current primary-supply well runs at any given time for the cluster's shared distribution. A 750W pump running 2 hours/day consumes 1.5 kWh/day — approximately 10–15% of the cluster's winter essential load budget. If all three pumps run simultaneously (rare but possible during a water emergency), the combined 2,250W running load plus startup surge (3–5× running power = 2,250–7,500W surge) demands an inverter with significant surge capacity — another argument for the 7.5–10 kW generator and a 48V inverter with 15,000W+ surge rating.

**Pump scheduling protocol:**

Per `02-water-coordination.md`, the cistern gravity-distribution system means water is pumped to elevation once and then distributed by gravity without additional electrical input. This allows pump scheduling to be treated as a deferrable load — ideal for energy coordination:

- **Primary window**: 10 AM–3 PM on days with confirmed solar generation >50% nominal. Run the pump during this window to fill the cistern from solar surplus before battery draw begins.
- **Secondary window**: During generator operation, run the pump in the first hour (generator already running; add 750W to a load that is already running at 50–70% capacity — marginal fuel cost is minimal).
- **Emergency restriction**: When SOC is below 25%, defer next pump cycle if cistern has more than 72 hours of supply remaining (per the cistern minimum reserve defined in `02-water-coordination.md`).

**Water heating — propane tankless vs. heat-pump integration:**

For the reference cluster, propane tankless water heaters are preferred over electric heat-pump water heaters for three reasons:

1. Heat-pump water heaters (HPWHs) extract heat from surrounding air, which in a Zone 5 winter means extracting heat from a heated interior space — in effect, fighting the building's heating system [15]. Their high efficiency (COP 2.5–4.0) only materializes in a warm space; in a cold utility room below 40°F, a HPWH may switch to resistance backup, losing its efficiency advantage.

2. HPWHs draw 450–550W continuously for 2–3 hours per tank reheat cycle [15] — a significant sustained load on the battery system at exactly the time (winter mornings) when battery SOC is most likely to be depleted.

3. A propane tankless heater delivers instant hot water at 150,000–200,000 BTU/hour with no electrical demand beyond a small ignition circuit (6–30W). The fuel cost is integrated into the cluster's consolidated propane supply.

Exception: If the cluster has abundant summer solar generation creating consistent surplus between 10 AM and 4 PM, a heat-pump water heater operating during that window (Tier 5 load — solar surplus only) is a viable long-term strategy that can reduce propane consumption in summer by 50–70%.

---

## Section 6: Food Preservation Load Management

### August–October Preservation Season

The cluster's food preservation peak (detailed in `03-food-coordination.md`) coincides with the Zone 5 solar generation peak — a favorable alignment that solar scheduling can exploit fully.

**Preservation load inventory:**

| Load | Power | Typical hours/day | kWh/day | Season |
|---|---|---|---|---|
| Electric pressure canning (2 burners, 1,500W each) | 3,000W | 2–4 hours | 6–12 kWh | Aug–Oct |
| Food dehydrator (9-tray Excalibur or equiv.) | 600W | 10–12 hours | 6–7.2 kWh | Aug–Oct |
| Additional chest freezer (overflow storage) | 80W avg | 24 hours | 1.9 kWh | Aug–Oct |
| Vacuum sealer (intermittent) | 130W | 0.5 hours | 0.07 kWh | Aug–Oct |
| **Preservation peak daily total** | | | **14–21 kWh/day** | Aug–Oct |

**Solar scheduling for preservation loads:**

In August, the reference cluster's 4,800W total solar installation generates approximately 22–27 kWh on a clear day (5.6–5.8 peak-sun-hours [2] × 4,800W × 0.80 derate). This exceeds the cluster's essential load (10–14 kWh) plus preservation loads (14–21 kWh) on most good-weather days — summer solar surplus is the resource that makes intensive food preservation electrically viable.

**Scheduling protocol:**
- Canning sessions start at 9:30 AM (solar ramping up); plan first load in canner by 10 AM
- Target to complete second canner load by 3 PM (solar still at 70–80% of peak)
- Dehydrator runs 8 AM–8 PM; morning hours draw from battery, midday and afternoon draw from solar
- Preservation work is deferred on confirmed overcast days (battery SOC managed for essential loads)
- Propane canning as alternative: the cluster's shared canning kitchen (per `03-food-coordination.md`) includes propane burners as primary option when solar is unavailable — removing the 6–12 kWh electrical canning load entirely on cloudy days

**Why propane canning is the preferred cluster-scale solution:**

A propane burner delivers 15,000–18,000 BTU/hour, bringing a canner to pressure in 15–20 minutes. An equivalent 1,500W electric burner delivers 5,115 BTU/hour — a 3× disadvantage in heat delivery that means longer time to pressure, longer session duration, and more food quality risk at the margins of temperature control [16]. For cluster-scale canning of 200–400 quarts per season (per `03-food-coordination.md` targets), propane canning is faster, more reliable, and load-independent from the electrical system.

The electrical dehydrator, however, has no comparable propane alternative at reasonable scale — a 9-tray dehydrator providing consistent 130–160°F airflow for 10–12 hours is an inherently electrical load. Solar scheduling is the answer: run dehydrators only on confirmed-clear-day forecasts.

---

## Section 7: Smart Load Coordination

### Scheduling Framework

Effective cluster energy coordination requires no sophisticated technology — it requires a shared commitment to a daily scheduling protocol. The framework parallels the water stewardship rotation in `02-water-coordination.md`: a rotating energy steward monitors the battery SOC each morning and issues a daily energy status to all households.

**Morning SOC report (8 AM daily):**
- Current SOC: [XX]%
- Solar forecast for day: [Clear / Partly cloudy / Overcast]
- Energy tier for today: [Green / Yellow / Orange / Red]
- Any load restrictions or generator plan

| Tier | SOC + Forecast | Permitted loads | Deferred loads |
|---|---|---|---|
| Green | SOC >60%, clear day | All loads permitted | None |
| Yellow | SOC 40–60%, or partly cloudy | Tier 1–3 only; no EV charging | Dryer, EV |
| Orange | SOC 30–40%, or overcast | Tier 1–2 only; canning on propane | All Tier 3–5 |
| Red | SOC below 30% | Tier 1 only; generator decision pending | All Tier 2–5 |

**High-consumption appliance scheduling:**

- **Washing machines**: Run only on Green or Yellow days, 10 AM–2 PM window. Each household runs one laundry day per week, staggered across the cluster (Household A: Monday, B: Wednesday, C: Friday) to prevent simultaneous loads.
- **Dryers**: Only on Green days during peak solar generation (10 AM–3 PM). Preferred alternative: line-dry in summer; indoor drying rack in winter. A clothesline eliminates 4–5.8 kWh per drying cycle — with weekly laundry across 3 households, this saves 12–18 kWh/week, a material fraction of the winter solar budget.
- **Dishwashers**: Run on Green/Yellow days only; air-dry setting (no heated dry); run at 11 AM.
- **Power tools/workshop**: Only during confirmed solar surplus periods (Green + solar generating >70% capacity). Large tools (table saw, air compressor) require coordination: alert cluster before starting to prevent simultaneous heavy loads.

**Electric vehicle (V2H) integration:**

V2H (Vehicle-to-Home) capable EVs, as described in `individual/04-energy.md`, can contribute 10–30 kWh of discharge capacity from the vehicle battery to the cluster during a grid outage or solar deficit. This is a Tier 5 resource — valuable but not to be counted on in baseline planning:

- EV charging: Tier 5 load, Green days only, managed charging (limit to 3–5 kW) during solar surplus
- V2H discharge: Emergency supplement during Red-tier days when battery SOC is below 20% but the vehicle battery is above 40%
- EV is never discharged below 30% state of charge without driver consent — the vehicle's primary role is transportation, not cluster battery storage

---

## Section 8: Disaster Scenarios and Contingencies

### Midwest-Specific Failure Modes

**Scenario A: Spring tornado (April–June)**

*Profile*: Power loss + potential tree damage blocking solar panels + infrastructure disruption to propane delivery.

*Immediate response*:
- Isolate any damaged panel arrays (safety first — damaged panels may arc)
- Switch to generator-only until damage assessment complete
- If propane delivery roads are blocked: propane reserve must bridge gap
- Wood heat primary; minimize all electrical loads

*Recovery path*:
- Day 1–2: Generator + propane; damage assessment; contact repair contractors
- Day 3–7: Panel replacement or bypass (operate cluster on 2/3 arrays if one household affected)
- Week 2+: Grid likely restored in area (tornadoes are localized); grid-tie reconnection if available

*Design implication*: Solar arrays should be mounted such that a fallen tree from the most likely directions (prevailing storm track: southwest to northeast in Midwest) affects at most one household's array. Keep neighboring trees trimmed within 50 feet of any panel array — not for shading (already required) but for storm safety.

**Scenario B: Winter ice storm (January–February)**

*Profile*: Grid outage + subfreezing temperatures + solar panels iced/snowed over + roads impassable for propane delivery.

*Immediate response*:
- Wood heat is primary in all households (requires no energy input)
- Propane: heating assist and generator support
- Generator: run 4–6 hours/day to maintain battery at 40–60% SOC; essential loads only
- All panel clearing deferred until temperatures rise (do not attempt ice removal from panels in dangerous conditions — fire risk from high-voltage panels is real)

*Duration tolerance*:
- With 200-gallon propane reserve: 13–15 days of combined heating + generator at conservative use rates
- With 300-gallon reserve: 20–22 days
- Wood heat reduces propane demand by 60–75% on the coldest days

*Design implication*: A 300-gallon minimum propane reserve entering winter is the difference between a manageable 2-week ice storm and a crisis. Budget for a full tank fill every October regardless of current level.

**Scenario C: Extended winter solar failure (7+ days)**

*Profile*: Prolonged cloud cover, no meaningful solar generation, no grid (off-grid cluster).

This is the cluster's reference design scenario. It has been analyzed in Section 4 above. The key takeaway: a cluster with 300 gallons of propane reserve, an operational wood heating system, and a maintained generator is resilient against this scenario indefinitely — propane consumption at ~15 gallons/day (generator + heating) limits the risk to supply chain timing rather than physical capability.

**Scenario D: Generator failure during winter**

*Profile*: Generator fails (mechanical) during an extended outage window; propane still available for heating.

*Immediate response*:
- Switch to wood heat primary in all households (eliminates heating electrical load)
- Battery bank carries essential loads (lighting, refrigeration, communications, water pump)
- At 10 kWh essential load/day with 24 kWh usable battery: approximately 2.4 days of autonomy
- Solar generation on any partially clear day extends this significantly

*Medium-term*:
- Source generator repair parts (keep spare starter motor, spark plugs, and oil filter on hand)
- Rent or borrow a backup generator within the cluster's social network
- If winter solar provides even 30–40% of essential load, battery autonomy extends to 4–6 days between partial charges

*Design implication*: The generator is a critical single point of failure. Keep 30 days of maintenance parts on hand. Consider whether two smaller generators (2× 3.5 kW) provide more redundancy than one 7.5 kW unit — they do, at the cost of slightly higher total investment.

---

## Section 9: Cluster Governance

### Energy Stewardship

The cluster requires a designated energy steward — a rotating weekly role responsible for monitoring the shared battery bank SOC, issuing the morning energy status, and making generator-start decisions. This is not a permanent technical expert role; it is a stewardship position that any cluster member can fulfill after basic orientation.

**Energy steward weekly responsibilities:**
- Morning SOC check at 8 AM; issue daily energy tier to cluster
- Monitor propane gauge; alert cluster if below 25% reserve (refill threshold)
- Generator start/stop decisions per Section 3 protocol
- Log daily SOC, generation, and generator runtime in the cluster energy log
- Brief incoming steward on system status at week changeover

### Generator Start Decision Protocol

Generator start decisions are the most consequential daily judgment calls the steward makes. The protocol from Section 3 defines the criteria; the governance principle is that any cluster member can request a generator start if they believe the criteria are met, but the steward makes the call.

**Disputed decisions**: If a cluster member disagrees with a steward's generator decision (e.g., steward declines to start generator; member believes it is needed), the dispute goes to a 2/3 vote among household leads within 1 hour. The steward's decision stands in the interim.

### Battery SOC Management

Daily target: battery at 80–90% SOC by 3 PM on any day with solar generation above 50% nominal. This "charge-by-afternoon" protocol mirrors the operational logic of the cistern refill target in `02-water-coordination.md` — you always want the shared reserve topped up by day's end.

Weekly target: battery enters every Monday morning at minimum 60% SOC. If entering the week below 60%, the steward runs the generator on Monday to top up before assessing the week's load schedule.

**Minimum reserve — non-negotiable**: Battery SOC never intentionally drawn below 20%. The BMS will disconnect loads automatically below 10%, but reaching this level risks BMS lockout and shortens battery cycle life. The 20% threshold is written into the governance agreement and any steward who allows the bank to fall below 20% without triggering generator start is accountable to the cluster for explanation.

### Shared Infrastructure Ownership and Cost Allocation

The shared battery bank, generator, and propane tank are cluster commons with per-household equity shares. The governance framework recommended by Ostrom's principles for common-pool resource management [17] requires:

1. **Clearly defined boundaries**: Every household's solar contribution to the shared bank is metered. Energy flowing from a household's array into the shared bank is credited to that household; energy drawn from the shared bank is debited against each household's account. Monthly reconciliation determines whether any household owes a "generation credit" to another.

2. **Rules fit local conditions**: The SOC thresholds, generator protocols, and load schedules described in this document are starting points. The cluster must adapt them to actual observed behavior in their first full year of operation.

3. **Collective choice arrangements**: Major decisions (generator replacement, battery bank expansion, adding a household to the cluster) require full cluster consensus. Daily operational decisions (generator start/stop, load scheduling) are the energy steward's sole authority.

4. **Conflict resolution**: Energy billing disputes go to a written mediation process before external arbitration. Keep the accounting simple enough that disputes are rare — monthly summaries, not daily transaction reconciliation.

**Cost allocation for shared infrastructure:**

| Infrastructure component | Recommended allocation |
|---|---|
| Shared battery bank | Equal thirds (each household owns 1/3 regardless of individual array size) |
| Generator | Equal thirds |
| Propane tank + supply | Pro-rata to actual consumption (generator use vs. heating use tracked separately) |
| Controls and wiring | Equal thirds |
| Maintenance labor | Labor-hour tracking; credit toward propane allocation |

### Preventive Maintenance Schedule

| Task | Frequency | Responsible | Notes |
|---|---|---|---|
| SOC log + system check | Daily | Energy steward | 5 minutes; log SOC, generation, weather |
| Battery connection inspection | Monthly | Rotating | Check for corrosion, loose terminals |
| Panel cleaning | Monthly (or after dust/pollen events) | Per-household | Microfiber cloth; no abrasives |
| Panel snow clearing | As-needed | Per-household | Only when safe; use soft brush |
| Generator exercise run | Monthly (30 min under load) | Energy steward | Verify oil level + output voltage |
| Generator full service | Annually | Energy steward + qualified tech | Oil, plugs, filter, coolant |
| Propane gauge + leak check | Monthly | Energy steward | Soapy water leak test at connections |
| Battery cell voltage check | Monthly | Energy steward | Via BMS display or battery monitor |
| BMS firmware update | Annually | Technical lead | If manufacturer releases updates |
| Inverter/charger inspection | Semi-annually | Technical lead | Clean cooling fins; check fan |

---

## Section 10: Implementation Timeline

### Phase 1: Design, Individual Solar, and Shared Battery Bank (Months 1–12)

**Months 1–3: Planning and engineering**
- Complete individual household load audits (per `individual/04-energy.md` methodology)
- Assess each household's roof for solar potential: orientation, available area, structural load capacity, shading
- Commission a licensed electrician's assessment of interconnection requirements for a cluster microgrid
- Select shared battery bank specification (30 kWh LiFePO4 recommended) and location (conditioned basement)
- Draft cluster governance agreement (energy steward rotation, SOC thresholds, cost allocation)
- Confirm propane supplier contract and order shared propane tank installation (2–4 month lead time)

**Months 4–8: Individual solar installation**
- Each household installs its own solar array (1,200–2,400W per household) with MPPT charge controller
- At this stage, each household operates independently with individual battery backup — the shared bank comes in Phase 1b
- Begin logging generation data for full seasonal characterization before designing shared system

**Months 9–12: Shared battery bank and generator**
- Install shared battery bank in conditioned space
- Interconnect all household arrays to shared bank via individual MPPT controllers
- Install shared inverter/charger (Victron Multiplus-II 48/5000 or equivalent) as cluster grid reference
- Install propane standby generator; connect to inverter/charger input; configure start/stop logic
- Commission full system; run cluster through all SOC protocols in simulation; document steward procedures
- October: fill propane tank to 100% before first winter; establish winter reserve minimum protocol

**Phase 1 capital cost estimate:**

| Component | Range | Per-household share |
|---|---|---|
| Individual solar (3× 1,600W) | $6,000–$12,000 total | $2,000–$4,000 |
| Shared battery bank (30 kWh LiFePO4) | $12,000–$25,000 | $4,000–$8,333 |
| Shared inverter/charger | $2,500–$4,000 | $833–$1,333 |
| Propane standby generator (7.5–10 kW) | $4,000–$8,000 | $1,333–$2,667 |
| 500-gallon propane tank install | $1,200–$2,500 | $400–$833 |
| Controls, wiring, metering, conduit | $3,000–$6,000 | $1,000–$2,000 |
| Electrician/engineer fees | $2,000–$5,000 | $667–$1,667 |
| **Phase 1 total** | **$30,700–$62,500** | **$10,233–$20,833** |

### Phase 2: Propane Heat Integration and Passive Solar Optimization (Year 2)

**Passive solar retrofits** (per Section 4): assess each household for south-facing glazing additions, thermal mass opportunities, and overhang adjustment. A retrofit adding 40 sq ft of south-facing windows + 240 sq ft of tile flooring in the sun path can reduce winter heating demand by 15–25% [13] — at lower installed cost than additional solar panels achieving the same effective winter load reduction.

**Wood heat systems**: if not already installed, add a wood stove or rocket mass heater to each household as primary winter heat source. Cost: $1,500–$4,000 per household for a quality wood stove with proper chimney. A rocket mass heater built from cob can be significantly cheaper ($300–$800 in materials) with substantial labor investment [12].

**Propane appliance optimization**: replace any remaining electric cooking or water heating with propane. This reduces winter electrical demand and concentrates the cluster's fuel dependency on a single managed inventory.

### Phase 3: Smart Load Management and V2H Integration (Year 3+)

**Smart load controls**: Install automated load management (smart outlets, programmable relays, or a home energy management system) that can execute the SOC-based load shedding automatically without requiring manual steward action. Systems such as Victron's Venus GX or similar BEMS platforms can automate generator start/stop, load shedding, and SOC monitoring with minimal ongoing steward effort.

**V2H integration**: As cluster households replace vehicles, V2H-capable EVs (Ford F-150 Lightning, Rivian with export mode, Hyundai Ioniq 6 with V2H adapter) provide supplemental battery capacity during outages. A single V2H vehicle with 100 kWh battery contributing 30% of its charge (30 kWh) effectively doubles the cluster's battery reserve during an emergency.

**Battery bank expansion**: If cluster energy needs grow (added household, new large load, medical equipment), expand the shared battery bank by adding additional rack-mounted LiFePO4 modules to the existing 48V bus. The modular architecture of rack batteries (each module 5–10 kWh) allows capacity additions without system redesign.

---

## Section 11: International Precedent

### Feldheim, Germany — Village-Scale Energy Independence

Feldheim (130 inhabitants, Brandenburg state) is frequently cited as the world's only fully grid-independent village. Beginning in the 1990s, the community erected wind turbines, installed a solar farm (284 panels, 2,700 MWh/year), constructed a biogas plant fueled by pig manure and corn waste, and built its own local mini-grid completed in 2010 [18]. The result: Feldheim produces all its own energy from renewable sources and sells surplus to the national grid, paying 31% less for electricity and 10% less for heating than the national average [18].

The Feldheim model differs in scale from the 3-household cluster but demonstrates directly applicable governance principles: a community-owned grid, locally determined electricity prices set at community meetings, and multiple generation sources providing redundancy. The biogas plant and wood-chip furnace serve the same role as the cluster's propane backup — a non-solar thermal source that fills the winter gap.

**Lesson for cluster design**: The cluster's propane generator is a stand-in for the biogas infrastructure Feldheim built. As the cluster matures and production agriculture develops (per `03-food-coordination.md`), animal waste biogas (pig, cattle, or even high-density chicken manure [19]) could displace or supplement propane — a direct application of the Feldheim model at micro-scale.

### Denmark — Household Energy Community Model (Svalin and Similar Projects)

Denmark's 2023 renewable energy package formalized support for energy communities, enabling households within one building or adjacent parcels to share produced electricity internally without routing through the collective grid [20]. The Svalin co-housing peer-to-peer energy community (Copenhagen) implements exactly the cluster architecture described in this document: shared rooftop solar production, internal energy trading between units, and collective management of storage and backup [20].

Denmark's legal framework for energy communities — granting households the right to share energy without utility intermediary — is more advanced than the current U.S. regulatory environment, where inter-household energy sharing remains legally complex in most states. The cluster model in this document sidesteps this by operating as a single off-grid microgrid (no utility interconnect required for sharing) rather than trying to share across utility-metered connections.

**Lesson for Zone 5 cluster**: If the cluster eventually connects to grid (for billing purposes), consult with the state utility commission on the legal framework for multi-household energy sharing. Illinois, Indiana, and Iowa each have emerging community solar and virtual net metering programs that may apply.

---

## Sources

[1] autohvac.ai / ASHRAE Climate Zone 5A reference. "Climate Zone 5A: Insulation R-Values, Design Temps & HVAC." 99th-percentile winter design temperature: 0°F; summer design temperature 91°F; R-49 ceiling, R-20 wall requirements. https://autohvac.ai/climate-zones/zone/5a

[2] NREL PVWatts Calculator. "Monthly solar resource data, Chicago/Indianapolis/Des Moines lat/long, south-facing 30° fixed tilt, standard 0.80 system derate." National Renewable Energy Laboratory. https://pvwatts.nrel.gov — Monthly peak sun hours: Dec 2.8, Jan 2.8, Jun 5.8, Jul 5.9. Individual/04-energy.md generation table derived from this source.

[3] Gellings, C.W. "Demand Forecasting for Electric Utilities." *Energy Engineering*, 2011. Load diversity coefficient: aggregate residential peak demand is typically 60–75% of sum of individual household peaks due to behavioral asynchrony. Referenced in IEEE microgrid planning literature.

[4] U.S. Energy Information Administration. "Electricity Use in Homes." EIA, 2020. Central air conditioning: largest single residential electrical load in summer, averaging 1.5–2 kW continuous draw in Zone 5 climates; 9,000–20,000 Wh/day during sustained heat events. https://www.eia.gov/energyexplained/use-of-energy/electricity-use-in-homes.php

[5] ASCE 7-22 / ICC Snow Load Map. "Ground Snow Loads for the United States." American Society of Civil Engineers, 2022. Illinois/Indiana/Iowa: 20–30 psf ground snow load in Zone 5 counties. Governs solar panel and roof racking structural requirements. https://www.asce.org/asce-7

[6] RELiON Battery. "How Do LiFePO4 Batteries Perform in Cold Temperatures?" 2024. BMS charge cutoff at 0°C; capacity at -20°C approximately 60–65% of rated; discharge continues safely to -20°C; Arctic microgrid deployments show 88% round-trip efficiency vs. 63% for lead-acid at -30°C. https://www.relionbattery.com/knowledge/how-do-lifepo4-batteries-perform-in-cold-temperatures

[7] Mirabito Energy / Lakes Gas. "Propane Tank Pressure in Extreme Cold." Propane vaporization pressure at -20°F; surface tank considerations; freeze-down vs. diesel gelling comparison; indefinite shelf life advantage over gasoline and diesel. https://www.mirabito.com/blog/winter-propane-tank-pressure/ and https://www.lakesgas.com/does-cold-weather-affect-propane/

[8] LearnMetrics. "How Much Propane Do Generators Use Per Hour? (500W – 40kW)." 2024. 7.5 kW generator propane consumption: 25% load 0.47 gal/hr, 50% load ~1.0 gal/hr, 75% load ~1.33 gal/hr, 100% load ~1.67 gal/hr. https://learnmetrics.com/how-much-propane-do-generators-use-per-hour/

[9] Victron Energy. "AC-Coupling and the Factor 1.0 Rule." Victron Energy documentation. Island mode voltage/frequency regulation via MultiPlus inverter/charger; frequency shifting for solar regulation (60 Hz → 61–62 Hz to reduce PV output when battery full); factor 1.0 rule for AC-coupled systems. https://www.victronenergy.com/live/ac_coupling:start

[10] UL Standards. "UL 1741: Inverters, Converters, Controllers and Interconnection System Equipment for Use with Distributed Energy Resources." 2023 6th Edition. Anti-islanding protection (2-second disconnect); grid voltage/frequency compatibility; LiFePO4 battery compatibility requirements added in 2023 edition; UL 1741 SA/SB for intentional islanding in microgrids. https://www.altenergymag.com/news/2025/12/10/ul1741-certification-why-its-critical-for-solar-inverters-entering-the-north-american-market/46468/

[11] IEEE Xplore / ResearchGate. "A Robust Load Shedding Strategy for Microgrid Islanding Transition." IEEE Conference Publication, 2016. Priority-based load shedding for islanded microgrids; consumer priority indices; distributed algorithms for gradual load reduction. https://ieeexplore.ieee.org/document/7520055/

[12] EcoHome / Mother Earth News. "Rocket Mass Heaters: High-Efficiency DIY Alternative to Masonry Heaters." ecohome.net; motherearthnews.com. Efficiency 85–90% vs. conventional wood stove 60–75%; fuel use 50–80% less; real-world Zone 5 (Montana) heating exclusively with rocket mass heater confirmed. https://www.ecohome.net/en/guides/4156/rocket-stoves-the-high-efficiency-diy-alternative-to-masonry-heaters/ ; https://www.motherearthnews.com/sustainable-living/green-homes/rocket-mass-heater-faqs-answered-zbcz1608/

[13] U.S. Department of Energy. "Passive Solar Homes." energy.gov/energysaver. South-facing glazing 8–12% of floor area; thermal mass sizing 6× glazing area; overhang angle formula for latitude; heating load reduction 25–37% documented. https://www.energy.gov/energysaver/passive-solar-homes. Supporting study: ScienceDirect — "Energy conservation in residential buildings by incorporating Passive Solar and Energy Efficiency Design Strategies" (37% heating load reduction documented). https://www.sciencedirect.com/science/article/abs/pii/S0378778817340574

[14] GridWright / EcoFlow. "How Many Watts Does a Well Pump Use?" 2024. Submersible 750W (1HP) pump: 700–800W running, 3–5× startup surge (2,250–3,750W inrush); minimum 3,000W inverter required; soft-start device allows 1,500W inverter. https://gridwright.com/calculators/power/well-pump-wattage ; https://www.ecoflow.com/us/blog/how-many-watts-does-well-pump-use

[15] One Community Global / DIY Solar Power Forum. "Sustainable Water Heating: Tank vs Tankless vs Heat Pumps in Off-Grid Living Situations." Heat-pump water heater COP 2.5–4.0 in warm space; performance degraded below 40°F ambient; resistance backup activates in cold utility rooms; 450–550W continuous for 2–3 hour reheat cycle. https://onecommunityglobal.org/sustainable-water-heating/

[16] National Center for Home Food Preservation (NCHFP), University of Georgia. "Complete Guide to Home Canning." Temperature control criticality in pressure canning; propane burner BTU advantage (15,000–18,000 BTU/hr) vs. electric (5,115 BTU/hr at 1,500W); USDA-tested processing times; botulism prevention requirements. https://nchfp.uga.edu/

[17] Ostrom, Elinor. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. Eight design principles for long-enduring common-pool resource institutions: (1) clearly defined boundaries, (2) rules fit local conditions, (3) collective choice arrangements, (4) monitoring, (5) graduated sanctions, (6) conflict resolution, (7) recognition of rights, (8) nested enterprises. Also: ScienceDirect — "Navigating emergent effects in off-grid systems: Ostrom's design principles and rural energy policy implications," 2024. https://www.sciencedirect.com/article/pii/S2214629624003773

[18] Energiequelle GmbH / RMI / Clean Tech Nica. "The Energy Self-Sufficient Village of Feldheim." Village of 130 inhabitants; 55 wind turbines + 284-panel solar farm + biogas plant + wood-chip furnace; own mini-grid completed 2010; 31% lower electricity cost; 10% lower heating cost than national average. https://www.energiequelle.de/en/projects/lighthouse-projects/the-energy-self-sufficient-village-of-feldheim ; https://rmi.org/blog_2014_02_19_renewables_power_a_rural_german_village/

[19] Mother Earth News / Penn State Extension. Biogas from animal waste: pig, cattle, and high-density poultry manure as feedstock; digesters viable at cluster scale with 10–50 pigs or 500+ chickens; biogas yield 5–8 cubic feet per pound of volatile solids; equivalent to 0.5–0.8 cubic feet methane/day per 100-pound pig. https://www.motherearthnews.com/sustainable-living/

[20] Housing Evolutions Hub / PV Magazine. "Svalin Co-Housing P2P Energy Community" (Denmark); "Denmark supports first energy communities." 2023 Renewable Energy Package; DKK 4 million in 2022 community energy grants; peer-to-peer energy sharing within co-housing; legal framework for internal electricity sharing without grid routing. https://www.housingevolutions.eu/project/svalin-co-housing-p2p-energy-community/ ; https://www.pv-magazine.com/2023/12/22/denmark-supports-first-energy-communities/

[21] U.S. Energy Information Administration. "2020 Residential Energy Consumption Survey (RECS)." Annual electricity consumption U.S. average 10,791 kWh (2022 data); Midwest homes higher natural gas consumption; 44% of Midwest homes have separate freezer. https://www.eia.gov/consumption/residential/data/2020/

[22] Renogy. "Lithium Batteries in Cold Weather: Performance, Challenges, Solutions." 2024. BMS cold-weather charge cutoff behavior; heating strategies for Zone 5 battery banks; insulated enclosure recommendations; self-heating battery options with $50–100 per battery premium. https://www.renogy.com/blogs/buyers-guide/lithium-batteries-in-cold-weather

[23] IEEE Recommended Practice. "IEEE 2030.9: Planning and Design of the Microgrid." System configuration; electrical design; safety; power quality monitoring and control for AC microgrids; grid-connected and standalone modes. https://standards.ieee.org/ieee/2030.9/6079/

[24] anernstore.com. "Blueprint: Sizing LiFePO4 for Islanded Homes vs Grid Support." 2024–2026. 48V standard for home energy storage; 80% DoD target; 3,000–6,000 cycle life; cost $300–$500/kWh for rack batteries. https://www.anernstore.com/blogs/off-grid-solar-solutions/sizing-lifepo4-islanded-vs-grid

[25] ScienceDirect / Ideas.RePeC. "Microgrid and Load Shedding Scheme During Islanded Mode: A Review." *Renewable and Sustainable Energy Reviews*, 71, 161–169, 2017. Priority-based load shedding review; consumer-based priority index; optimal scheduling under islanded conditions. https://ideas.repec.org/a/eee/rensus/v71y2017icp161-169.html

[26] Healthy Canning. "Energy Requirements for Home Canning." 1,500W electric burner = 1.5 kWh per hour; full canning season (1,500–2,000 jars): 200–300 kWh additional electricity; individual session energy variable by food type and processing time. https://www.healthycanning.com/energy-requirements-for-home-canning/

[27] Kitchen Hyper. "Energy Use of Food Dehydrators: Wattage and Run Time Basics." Excalibur 9-tray rated 600W; 12-hour session = 7.2 kWh; scheduling during solar peak hours reduces battery discharge by 80–90%. https://kitchenhyper.com/energy-use-of-food-dehydrators-wattage-and-run-time-basics/

[28] Emerson Electric. "How Cold Weather Affects Propane Tank Capacity." Bulletin LP-27. Surface propane tank vaporization pressure at subfreezing temperatures; maintain above 40% fill level in extreme cold; buried tanks maintain above -5°F at depth. https://www.emerson.com/documents/automation/how-cold-weather-affects-tank-capacity-bulletin-lp-27-en-11751596.pdf

[29] SolarTechOnline / GreenBuildingAdvisor. "Heat Pump vs. Solar Water Heaters: Which is Truly the Most Efficient?" 2024–2025. HPWH COP 3.88 under optimal conditions; performance loss in cold climates below 40°F ambient; solar thermal vs. PV+HPWH comparative analysis. https://sunearthinc.com/latest-news/2024/10/21/heat-pump-vs.-solar-water-heaters-which-is-truly-the-most-efficient/

[30] Clean Energy Wire. "Citizens' Participation in the Energiewende." Germany 2023 renewable energy package; expanded energy cooperative support; simplified grid access; 15.1 GWp solar deployed 2023, 46% residential; 3+ million residential rooftop PV systems. https://www.cleanenergywire.org/factsheets/citizens-participation-energiewende

[31] autohvac.ai / Energy Vanguard. "We Are the 99% — Design Temperatures and Oversized HVAC Systems." Zone 5A winter heating at 0°F design temperature; well-insulated 1,500 sq ft home at design temperature: 20,000–35,000 BTU/hour = 6–10 kW equivalent electric heating. https://www.energyvanguard.com/blog/we-are-the-99-design-temperatures-oversized-hvac-systems/

[32] Build with Rise. "Rocket Mass Heater Guide: An Energy-Efficient Heating Option." buildwithrise.com. Zone 5 case study (Missoula, Montana); 1-2 cords/season vs. 4-5 cords conventional; one small daily fire maintains warmth; thermal mass bench heat release 8–12 hours. https://www.buildwithrise.com/stories/rocket-mass-heaters-an-energy-efficient-option-home

---

## Worksheets

### Worksheet 1: Cluster Energy Load Audit

*Complete one row per major load per household. Total all three households for cluster aggregate.*

| Load | Household A Watts | A Hours/day | A Wh/day | Household B Watts | B Hours/day | B Wh/day | Household C Watts | C Hours/day | C Wh/day | Cluster total Wh/day |
|---|---|---|---|---|---|---|---|---|---|---|
| Refrigerator | | | | | | | | | | |
| Chest freezer | | | | | | | | | | |
| LED lighting | | | | | | | | | | |
| Communications | | | | | | | | | | |
| Water pump (shared) | | | | | | | | | | |
| Medical equipment | | | | | | | | | | |
| Air conditioning | | | | | | | | | | |
| Electric cooking | | | | | | | | | | |
| Water heating | | | | | | | | | | |
| Washing machine | | | | | | | | | | |
| Clothes dryer | | | | | | | | | | |
| Canning/dehydrator | | | | | | | | | | |
| Other: | | | | | | | | | | |
| **Total** | | | | | | | | | | |
| **Winter essential** | | | | | | | | | | |

### Worksheet 2: Solar Generation vs. Demand — Monthly Balance

*Fill in after installation; use PVWatts data for your specific location as design reference.*

| Month | Cluster generation kWh/day | Essential demand kWh/day | Full operations demand | Net (+surplus / -deficit) | Battery days autonomy | Generator hours needed/day |
|---|---|---|---|---|---|---|
| January | | | | | | |
| February | | | | | | |
| March | | | | | | |
| April | | | | | | |
| May | | | | | | |
| June | | | | | | |
| July | | | | | | |
| August | | | | | | |
| September | | | | | | |
| October | | | | | | |
| November | | | | | | |
| December | | | | | | |

### Worksheet 3: Weekly Energy Steward Log

*One row per day; steward fills in during morning check.*

| Date | SOC 8 AM | Solar forecast | Energy Tier | Loads restricted | Generator run? (Y/N) | Generator hours | Propane gauge | Notes |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

### Worksheet 4: Annual Propane Reserve Tracker

*Target: never below 150 gallons October–March; refill when below 30%.*

| Month | Gauge reading (%) | Estimated gallons | Weekly consumption (gal) | Refill needed? | Refill date | Gallons added |
|---|---|---|---|---|---|---|
| October | | | | | | |
| November | | | | | | |
| December | | | | | | |
| January | | | | | | |
| February | | | | | | |
| March | | | | | | |
