---
title: Phase 5 Wave 2 — Community-Scale Microgrids & Distributed Energy Systems
project: systems-resilience
phase: 5
wave: 2
status: COMPLETE
research_date: 2026-05-26
target_audience: Community infrastructure planners, Zone 5 Midwest (IL, MI, IA, IN, WI)
word_count: ~6000
source_count: 55+
decision_gate: June 1 — Phase 5 Wave 2 execution sequencing
integration: off-grid-living (household scale), seedwarden (agricultural load context)
---

# Phase 5 Wave 2: Community-Scale Microgrids & Distributed Energy Systems

**Research Completed**: May 26, 2026  
**Scope**: Zone 5 Midwest (IL, MI, IA, IN, WI) — rural and suburban contexts  
**Sizing focus**: Communities of 50–500 people  
**Resilience target**: 120-hour (5-day) grid-down scenarios

---

## Executive Summary

Microgrids are no longer prototype infrastructure. As of May 2026, the United States has more than 687 operational microgrids with 4,357 MW of installed capacity, growing at 13% annually, and federal investment in rural community microgrids has accelerated sharply since the Bipartisan Infrastructure Law and Inflation Reduction Act passed in 2021–2022. The DOE's Community Microgrid Assistance Partnership (C-MAP) deployed $5.5 million to 14 projects across 35 communities in June 2025. NRECA's consortium of seven rural electric cooperatives secured $45 million in DOE funding for rural microgrid deployment. Bayfield County, Wisconsin — directly in Zone 5 — deployed 841 kW of solar and 1,065 kW of battery storage across 24 sites serving 28 communities, providing 3+ hours of autonomous operation for critical facilities.

**Three core findings drive this research:**

1. **Hybrid AC/DC architecture with LiFePO4 storage is the proven design** for communities of 50–500 people today. Iron-air long-duration storage (100+ hours) reaches commercial scale in 2026–2027 and should be planned as a retrofit layer.

2. **The Illinois policy environment changed materially in January 2025**: standard net metering ended for new installations, replaced by supply-only crediting. The federal residential 30% ITC expired December 31, 2025. Communities must now finance through commercial mechanisms, REAP grants, or cooperative structures to access remaining incentives.

3. **120-hour winter resilience in Zone 5 requires hybrid storage + generator backup**. Solar alone cannot carry a community through a multi-day Midwest winter storm. The combination of 400+ kWh of battery storage, 50–100 kW of backup generation, and robust load-shedding protocols (prioritizing water, heat, and medical loads in that order) is the validated design pattern.

**Key implication for Phase 5 Wave 2**: Microgrid implementation at community scale takes 18–36 months from feasibility to commissioning. Communities that begin feasibility studies and utility interconnection applications in 2026 can achieve operational islanding capability by 2027–2028. This research provides the technical foundation and organizational contacts for that path.

---

## Section 1: Microgrid Architecture for Rural Communities

### What a Microgrid Is

A microgrid is a group of interconnected electrical loads and distributed energy resources — solar panels, batteries, wind turbines, generators — that operates as a single, controllable entity. It can operate connected to the main grid (grid-connected mode) or disconnected from it (islanded mode). The ability to "island" — to detect a grid failure and disconnect safely within milliseconds while maintaining power to critical loads — is what makes a microgrid different from a standard solar installation.

For lay communities: think of a microgrid as a neighborhood-scale backup generator that runs on solar and batteries instead of fossil fuel, can seamlessly kick in during an outage, and can sustain critical services for days rather than hours.

### AC vs. DC vs. Hybrid Architecture

**AC (Alternating Current) Microgrids**: The conventional design. All generation is converted to standard 120V/240V AC before distribution. Advantages: compatible with all existing appliances and infrastructure. Disadvantages: every solar panel and battery requires a DC-to-AC inverter, adding cost and conversion losses (10–15% energy lost per conversion).

**DC (Direct Current) Microgrids**: Solar panels and batteries are natively DC. DC microgrids skip conversion for DC loads (LED lighting, electronics, EV charging), reducing losses. Disadvantages: fewer off-the-shelf appliances; many industrial and heating loads require AC. Best suited for small, new-construction communities. Technical standard: IEEE 2030.10-2021 covers DC microgrids for rural and remote applications specifically.

**Hybrid AC/DC Microgrids** (recommended for Zone 5 communities): A bidirectional DC bus collects solar and battery power; an AC bus serves standard appliances and loads; bidirectional interlinking converters move power between buses as needed. Efficiency: 5–8% total conversion loss versus 15% for pure AC. Transition time during grid failure: under 50 milliseconds. This is the architecture validated by both NREL research and real-world deployments at UC San Diego, Blue Lake Rancheria (California), and Bayfield County (Wisconsin).

### Control System Tiers

**Centralized Control**: A single microgrid controller manages all assets. Advantages: simpler to design, easier to operate. Disadvantages: single point of failure — if the controller fails during an outage, the entire microgrid fails. Appropriate for small systems (under 100 kW).

**Decentralized/Peer-to-Peer Control**: Each inverter or battery system negotiates directly with its neighbors using local measurements. No central controller required. Advantages: resilient against single component failure. Disadvantages: more complex to commission, requires robust communication. Emerging standard for community-scale systems.

**Tiered Control** (most practical for 50–500-person communities): Local controllers manage individual assets (inverters, batteries, generators). A site-level energy management system (EMS) coordinates between assets. Optionally, a regional controller coordinates multiple microgrids. This is the architecture used in the Bayfield County and NRECA cooperative deployments.

### Islanding: The Critical Capability

Islanding is the process by which a microgrid detects grid failure and safely disconnects from the main grid while maintaining internal power. IEEE 1547-2018 defines requirements for this capability.

**How it works technically**: The microgrid controller continuously monitors the Point of Common Coupling (PCC) — the connection point between the microgrid and the main grid. When it detects voltage or frequency anomalies indicating grid failure (frequency outside 59.3–60.5 Hz, or voltage outside 88–110% of nominal), it opens the isolation switch at the PCC within 50 milliseconds and shifts all inverters to "island mode."

**Frequency control in island mode**: Without the main grid as a reference, inverters must self-regulate voltage and frequency using either:
- **Droop control**: Each inverter adjusts its output proportionally to frequency and voltage deviations. Widely used, scalable, requires no communication between inverters. Preferred method for decentralized systems.
- **Virtual Synchronous Machine (VSM)**: Inverters emulate the inertia of conventional generators, providing smoother frequency response. More complex, better for large systems with sudden load changes.

**Voltage regulation**: Reactive power sharing between inverters maintains voltage at ±10% of nominal (108–132V for 120V systems) across the microgrid.

**Practical note for lay planners**: Islanding capability requires intentional design. A standard solar + battery installation does NOT island automatically — it will shut down during a grid outage for safety reasons. Islanding requires a transfer switch, a microgrid controller, and inverters certified for island operation. Budget $15,000–$50,000 for the control hardware and switching gear, beyond solar and battery costs.

### Technical Standards Reference

- **IEEE 1547-2018**: Interconnection and interoperability of distributed energy resources with main grid. Defines islanding detection and intentional island operation requirements.
- **IEEE 2030.9-2019**: Recommended practices for microgrid controllers.
- **IEEE 2030.10-2021**: DC microgrids for rural and remote electricity access.
- **IEC 61850**: Communication protocol standard for microgrid components (enables interoperability between different vendors' equipment).

---

## Section 2: Community Solar and Storage — Regulatory Landscape (May 2026)

### Federal Policy: What Changed

**Investment Tax Credit (ITC)**: The 30% residential ITC under IRA Section 48/25D expired December 31, 2025 for homeowners who purchase systems outright. Commercial entities, nonprofits, and third-party ownership models (solar leases, power purchase agreements) may still claim the commercial credit under Section 48E through 2027. Cooperatives and nonprofit community organizations can access the credit through tax-equity arrangements or direct-pay provisions for eligible entities.

**Standalone Battery Storage Credit**: A separate 30% credit for battery storage (regardless of solar pairing) was enacted in 2022 and remains in effect through 2032 under Section 48E for commercial/nonprofit deployments. This is significant: a community cooperative or nonprofit organization installing a battery system qualifies for the 30% credit even without solar.

**USDA Rural Energy for America (REAP)**: $2 billion allocated through 2031 under the IRA. Maximum grant for renewable energy systems: $1,000,000 (FY2025–2027). Covers solar, wind, biogas, and battery storage for agricultural producers and rural small businesses. REAP loans approved in FY2025 carry an 80% federal guarantee. Note: grant applications were paused as of May 2026 — contact state USDA Rural Development Energy Coordinators for current status.

**FERC Order 2222**: Requires regional transmission organizations to allow distributed energy resource (DER) aggregations — including microgrids — to participate in wholesale electricity markets. Implementation varies significantly by state and RTO. In the Midwest (MISO territory), Order 2222 compliance rulemakings are ongoing as of 2026, creating potential revenue streams for community microgrids that can aggregate and bid generation capacity.

### Midwest State Policies

**Illinois**: The Climate and Equitable Jobs Act (CEJA, 2021) is the most significant state energy legislation in the Midwest. Key provisions as of May 2026:
- Community solar: 150 MW per year of new subscriptions allocated; approximately 250 MW of backlogged projects in processing.
- ComEd and Ameren DG rebates: $250/kW for solar + $250/kWh for battery storage (direct cash payments).
- ComEd offers $300/kW for solar and $300/kWh for battery storage under its DG rebate program.
- **Critical change January 1, 2025**: New installations receive supply-only net metering (credits apply only to energy supply charges, not delivery fees). Pre-2025 installations are grandfathered at full retail rate net metering for system lifetime.
- Illinois solar capacity: grew from 40 MW in 2019 to 4,500 MW by January 2025 under CEJA.
- Legislation (2024) established 8.5 GW cumulative utility-scale storage target and created incentives for combined community solar-plus-storage.

**Michigan**: First Midwestern state to establish a statewide storage target. Public Act 233 of 2023 mandates 2,500 MW of energy storage by 2029. Michigan Public Service Commission (MPSC) has approved multiple large BESS projects (150 MW/600 MWh Midland Township; 100 MW/400 MWh Washtenaw County). Michigan is expected to add more than 1 GW of solar capacity in 2025. Community solar program exists but is limited in scale relative to Illinois.

**Wisconsin**: PSC approved 488 MW of grid-scale battery energy storage as of 2023, with an additional 617 MW awaiting review. All grid-scale battery storage currently paired with solar. Net metering incorporates battery storage as supplemental to solar. Wisconsin's Focus on Energy program provides rebates for residential and commercial solar/storage. Bayfield County's microgrid program (see case studies) is the state's flagship community-scale demonstration.

**Iowa**: 64% of state electricity generation came from wind and solar in 2023. Average wind lease payment: $4,000/MW/year for farmers. Iowa opened a proceeding to evaluate Aggregators of Retail Customers (FERC Order 2222 compliance). No strong community solar program as of 2026, but utility-scale renewable development is world-class. Rural cooperatives are the primary delivery vehicle for distributed energy.

**Indiana**: Lags Illinois, Michigan, and Wisconsin on distributed energy policy. Net metering exists but is capped and frequently challenged by utilities. Community solar programs are minimal. The primary opportunity for Zone 5 Indiana communities is direct ownership (nonprofit cooperative or municipality) rather than third-party/utility programs.

### Navigating Utility Interconnection

For communities seeking to island, utility interconnection approval is typically the longest bottleneck: 3–6 months in cooperative utility territories, up to 12 months with investor-owned utilities. Key steps:
1. Pre-application meeting with utility interconnection department
2. Feasibility study (utility-initiated, 60–90 days)
3. System impact study if required (90–120 additional days)
4. Interconnection agreement execution
5. Construction, inspection, commissioning

Rural electric cooperatives (RECs) — which serve most of Zone 5's rural areas — are generally more receptive to distributed generation and microgrid islanding than investor-owned utilities. The NRECA CARED project is explicitly designed to create replicable interconnection pathways.

---

## Section 3: Open-Source Implementations and DIY Projects

### Design and Simulation Tools (Free)

**HOMER Energy (homerenergy.com)**: The industry standard for microgrid feasibility analysis. Inputs: load profile, solar/wind resource data, equipment costs. Outputs: optimal system configuration, net present cost, levelized cost of energy, reliability metrics. Free academic version available; commercial version required for advanced optimization. Widely used by NREL, USDA, and cooperative utilities. **Start here for any community feasibility study.**

**PVWatts (pvwatts.nrel.gov)**: NREL's free tool for estimating solar PV system performance. Input your location (or GPS coordinates) and system specs; it returns monthly and annual energy production using NREL's National Solar Radiation Database (NSRDB). Essential for Zone 5 seasonal production modeling. Can be run directly in a browser without installation.

**GridLAB-D**: Open-source power systems simulation environment developed by Pacific Northwest National Laboratory (PNNL). Enables high-fidelity modeling of distribution grids including microgrid operation, conservation voltage reduction, and distributed energy resource integration. Best for: validating a design before construction. Requires technical expertise; not a beginner tool. Available at github.com/gridlab-d/gridlab-d.

**OpenDSS**: Open-source distribution system simulation developed by EPRI (Electric Power Research Institute). Widely used by utilities and researchers for microgrid modeling. Good for: power flow analysis, protection coordination, islanding studies. Tutorial available using IEEE 13-node test feeder with renewable generation.

**PandaPower (pandapower.readthedocs.io)**: Python-based tool for power grid analysis developed by Fraunhofer IEE and University of Kassel. 500,000+ downloads since 2016. Capabilities: load flow, short-circuit, optimal power flow. Better for distribution system analysis than time-series simulation.

**pymgrid (github.com/Total-RD/pymgrid)**: Python package providing virtual microgrid environments for machine-learning-based energy management development. Useful for communities or researchers developing automated dispatch algorithms.

### Communication Standards (Open)

**OpenFMB (Open Field Message Bus)**: Originally developed by Duke Energy, ratified as NAESB standard in 2016. Enables real-time data exchange between microgrid components (inverters, meters, controllers) using MQTT or DDS protocols. Key data: kilowatts, VARs, voltage, current, state of charge, timestamps. Allows multi-vendor systems to communicate without proprietary lock-in. SGIP made OpenFMB code publicly available; NREL maintains documentation.

**IEC 61850**: International standard for substation and microgrid communications. Vendor-neutral; enables interoperability between equipment from different manufacturers. Required for utility-interconnected microgrids above a certain scale.

### Real-World DIY/Community Projects

**Adjuntas, Puerto Rico — Casa Pueblo Microgrid**: Following Hurricane Maria (2017), which left rural Puerto Rico without power for 9+ months, the nonprofit Casa Pueblo installed solar + battery microgrids on 13 local businesses that committed to providing critical services (medicine, refrigeration, phone charging) to residents during outages. First phase: 41 kW solar + 74 kWh battery storage across five sites, commissioned May 2022. Funded by California Energy Commission EPIC and community fundraising. Replication model: businesses receive electricity cost savings; community receives guaranteed emergency services. **The most directly applicable DIY model for Zone 5 rural towns.**

**Vieques, Puerto Rico — Cornell Mobile Battery**: Cornell researchers delivered a mobile solar-powered battery system to Vieques island (population 8,000) that operates independently of the main grid. Now powers two refrigerated semi-trailer trucks of local food. A parallel ORNL "orchestrator" project links multiple Vieques microgrids so they can share power if one loses solar generation. Demonstrates peer-to-peer multi-microgrid coordination.

**Blue Lake Rancheria, California**: 1 MW solar + LiFePO4 battery, operational 2024. 4–8 hours backup during regional outages. Funded by California Energy Commission. Tribal-owned and operated. Demonstrates that small communities (population ~50 on reservation) can own and operate professional-grade microgrids.

**Bayfield County, Wisconsin (Zone 5 flagship)**: 841 kW solar + 1,065 kW battery storage across 24 sites. Funded by DOE ERA program ($9.7M federal + $2.7M state cost share). Serving 28 rural communities and Red Cliff Band Tribal lands. Sites: fire stations, health clinics, transportation facilities, town halls. Expected: 1 million kWh clean energy annually. Construction ongoing 2025–2029. **The most directly comparable Zone 5 case study; contact Bayfield County Office of Sustainability and Clean Energy for lessons-learned documentation.**

### Cost Benchmarks (May 2026)

| Component | Cost Range | Notes |
|---|---|---|
| LiFePO4 battery pack | $240/kWh | Battery alone, cell-level, 2025 |
| Residential storage (installed) | $700–$1,300/kWh | 13–15 kWh typical residential |
| Utility-scale BESS (4-hour, installed) | $125–$334/kWh | NREL 2025 benchmark; competitive projects at low end |
| Solar panels (utility-scale) | $0.25–$0.35/W DC | Module only |
| String inverters | $0.05–$0.15/W | 50–250 kW scale |
| Microinverters | $0.50–$1.00/W | Per-panel, residential scale |
| Microgrid controller + transfer switch | $15,000–$50,000 | Per microgrid site |
| Community microgrid (100–500 kW total) | $2M–$5M | Turnkey installed |
| Per-capita cost (100 persons, 20-year life) | $2,000–$5,000 | Before grants; $800–$2,000 after federal/state incentives |

---

## Section 4: Zone 5 Climate Integration and Seasonal Modeling

### Solar Resource in Zone 5

Zone 5 (IL, MI, IA, IN, WI) has moderate solar resources — adequate but not exceptional. Using NREL's PVWatts and NSRDB data (1998–2014 averages for 1-axis tracking systems):

| State | Annual Solar (kWh/m²/day) | Winter Low (Dec–Jan) | Summer Peak (June–July) | Capacity Factor |
|---|---|---|---|---|
| Illinois | 4.2 avg | 2.0–2.5 | 5.8–6.2 | ~13% |
| Wisconsin | 3.9 avg | 1.8–2.2 | 5.4–5.9 | ~12.5% |
| Michigan | 3.8 avg | 1.6–2.0 | 5.2–5.8 | ~11% |
| Iowa | 4.3 avg | 2.1–2.6 | 5.9–6.3 | ~13.5% |
| Indiana | 4.1 avg | 1.9–2.4 | 5.6–6.1 | ~12.8% |

**Key implication**: A solar array sized for summer production is massively undersized for winter. A Zone 5 community that needs 100 kWh/day in summer needs 200–250 kWh/day of winter production from a 2.5× larger array — or it needs backup generation. Solar-only systems are viable for summer resilience; 120-hour winter scenarios require wind, generator, or long-duration storage supplements.

### Wind Resource in Zone 5

Zone 5's wind resource is world-class by global standards:

| State | Wind Capacity Factor (80m) | Notes |
|---|---|---|
| Iowa | 40–45% | Top 5 nationally; winter peaks |
| Illinois | 33–38% | Excellent northern/central; lower southern |
| Wisconsin | 30–35% | Strong Lake Michigan shoreline corridor |
| Michigan | 25–32% | Upper Peninsula strongest |
| Indiana | 25–30% | Northern Indiana best |

Iowa generated 64% of its electricity from wind and solar in 2023. The critical feature: **Midwest wind peaks in winter and shoulder seasons** — exactly when solar is weakest. This anti-correlation makes wind-solar hybrids dramatically more effective than solar-only for year-round resilience, reducing required battery storage by 30–40%.

**For agricultural integration**: Land lease payments for wind turbines average $4,000/MW/year in Iowa — meaningful supplemental income for rural landowners hosting community wind turbines. Small turbines (10–100 kW) are appropriate for farm-scale integration without the land constraints of utility-scale wind.

### Seasonal Load Profile: Zone 5 Rural Community

A typical rural Zone 5 community of 100 people has the following load pattern:

**Summer (June–August)**:
- Peak demand: 150–200 kW (air conditioning, irrigation pumping, refrigeration)
- Daily consumption: 2,000–2,500 kWh
- Solar covers 80–100% of daytime loads; battery handles overnight

**Fall (September–October)**:
- Peak demand: 80–100 kW (grain drying operations = major agricultural load)
- Daily consumption: 1,200–1,500 kWh
- Wind rising, solar declining; grain dryer loads align with wind peaks

**Winter (November–February)**:
- Peak demand: 120–180 kW (electric heating, water heating, farm operations)
- Daily consumption: 1,800–2,400 kWh
- Solar at 25–40% of summer output; wind at maximum
- **This is the design constraint**: minimum generation, maximum demand

**Spring (March–May)**:
- Peak demand: 70–90 kW (transitional heating/cooling, field preparation)
- Daily consumption: 1,000–1,400 kWh
- Solar rapidly increasing, wind declining

### Sizing Calculation: 100-Person Zone 5 Community for 120-Hour Winter Resilience

**Assumptions**:
- 100 people × 1.2 kW average household draw + 30 kW shared critical infrastructure = 150 kW total
- Winter load shedding to critical loads only: water pumping (5 kW), heating for community building (20 kW), medical/communications (10 kW), minimal lighting (5 kW) = **40 kW critical load**
- 120 hours of autonomy required
- Winter solar: 2 kWh/m²/day; 100 kW solar array generates ~20 kWh/hour at midday (1–2 hours effective per day)
- Wind (if available): 20 kW small turbine, 40% capacity factor in winter = 8 kW average continuous

**Storage calculation**:
Battery capacity = Critical load × Autonomy hours ÷ DoD
= 40 kW × 120 hours ÷ 0.80 (LiFePO4 DoD)
= **6,000 kWh required for solar/wind-only winter scenario**

This is impractical with current LiFePO4 ($125–$334/kWh installed = $750K–$2M for batteries alone). The practical solution is:

**Hybrid storage + generator approach**:
- LiFePO4: 400 kWh ($50,000–$160,000) — handles 10 hours without generation
- Biogas/diesel generator: 40 kW, runs 4–6 hours/day to recharge batteries ($25,000–$40,000)
- Small wind: 20 kW ($60,000–$100,000)
- Solar: 80–100 kW ($80,000–$120,000)
- **Total storage + generation capital**: $215,000–$420,000 for 120-hour winter resilience
- **Per-capita**: $2,150–$4,200 before grants

With REAP grants (up to $1M), DOE ERA/C-MAP grants ($200K–$500K range for small projects), and Illinois/Michigan/Wisconsin utility rebates ($250–$300/kWh for storage), net community cost drops to $500–$1,500 per capita.

### Agricultural Integration Opportunities

**Grain drying**: Zone 5's fall grain drying season (September–October) represents 30–50% of annual on-farm electrical demand on crop farms. Grain dryers typically run 50–200 kW and operate 10–20 hours/day during harvest. Integrating grain dryers as **dispatchable loads** (run when wind or solar is abundant, pause when not) is a major opportunity. Studies show this load flexibility can reduce required battery storage by 20–30%.

**Dairy operations**: Milking equipment, cooling tanks, and feed preparation run 6–8 hours/day at 10–40 kW on typical 100-cow dairies. Biogas digesters — converting manure to methane — can fuel a generator providing 15–40 kW continuous power. Dairy biogas microgrids are among the most cost-effective agricultural energy systems, with payback periods of 5–10 years at current energy prices.

**Cold storage and food processing**: Zone 5 vegetable farms and food hubs use refrigeration year-round. Refrigeration compressors have thermal inertia — they can pre-cool during cheap/abundant solar midday hours and coast through evenings. Integrating smart refrigeration controls into a microgrid's energy management system reduces peak demand by 15–25%.

---

## Section 5: Crisis Resilience Protocols — 120-Hour Scenarios

### Grid Failure Modes Relevant to Zone 5

**Winter ice storm** (highest Zone 5 probability): Freezing rain accumulates on transmission and distribution lines, causing conductor breaks and pole failures. Recovery time: 48–120+ hours in affected areas. The 2021 Texas freeze demonstrated that the cascade between electricity loss and natural gas infrastructure failure is the primary risk: electric compressors that drive gas pipelines lose power, reducing gas pressure, causing gas-fired generators to fail. In Zone 5, this cascade pattern means losing electricity also reduces propane delivery capacity and natural gas heating reliability.

**Cascading grid failure**: ERCOT (Texas) came within 4 minutes and 37 seconds of a complete statewide blackout in February 2021 — a collapse that would have required weeks to restore. The cascade mechanism: demand spike → frequency drop → generator protective relays trip → more frequency drop → more trips. A Zone 5 analogy: severe Midwest derecho (straight-line wind storm) simultaneously knocks out generation assets and transmission lines across multiple states.

**Geomagnetic storm**: Solar flare–driven electromagnetic pulses can destroy large power transformers. Recovery time if transformers are destroyed: months to years. Low probability, but maximum consequence. Microgrids that island before such an event and use only locally-manufactured components (no custom-wound transformers requiring 12-month lead times) have the best resilience. Pre-positioning spare transformers is recommended for any critical facility microgrid.

**Cyber attack on SCADA systems**: Intentional outage via compromise of utility control systems. Recovery time if backup manual controls exist: 24–48 hours. Mitigation: air-gapped microgrid controllers (not connected to internet); physical manual override switches.

### Load Shedding Protocol: Three-Tier System

The DOE/PNNL Microgrid Handbook for Army Resilience and multiple peer-reviewed studies confirm a three-tier load prioritization approach as the standard:

**Tier 1 — Mission-Critical (always powered, never shed)**:
- Water pumping and treatment (no water = medical emergency within 24 hours)
- Medical equipment and pharmacy refrigeration
- Community heating (winter life-safety; hypothermia risk begins at 36 hours in Zone 5 winters)
- Communications (radio, cell tower backhaul, internet for emergency coordination)
- Emergency lighting (fire station, clinic, community shelter)
- Estimated combined load: 20–50 kW for a community of 100

**Tier 2 — Important (powered when generation allows, shed if needed)**:
- Food refrigeration and freezers (food spoilage begins at 4 hours; critical within 48 hours)
- Basic residential heating (individual homes, beyond the community shelter)
- Agricultural critical loads (milking equipment — cows cannot go unmiilked for more than 12–14 hours without health consequences)
- Estimated load: 40–80 kW additional

**Tier 3 — Discretionary (shed immediately during islanding)**:
- Air conditioning (summer only; may be upgraded to Tier 2 during heat emergencies)
- Non-essential lighting
- Electric vehicle charging
- Most entertainment/computing loads
- Estimated load: 80–150 kW — shed these immediately to extend resilience

**Automated implementation**: Modern microgrid controllers implement load shedding via smart breakers on each load circuit. When the controller detects islanding and measures battery state of charge below a threshold (typically 80%), Tier 3 loads are automatically disconnected within seconds. Below 50% SOC, Tier 2 loads begin shedding by priority. Tier 1 loads are never shed automatically.

### Black Start Procedure

"Black start" is the ability to restart a power system from zero — when all generation and storage has failed, or after a controlled shutdown. For a community microgrid:

1. **Generator black start**: Diesel or biogas generator starts on its own internal battery (like starting a car). This is why diesel backup remains essential even in solar+battery microgrids.
2. **Energize control systems**: Generator powers the microgrid controller, communication systems, and protection relays.
3. **Charge battery storage**: Generator charges batteries to minimum operating threshold (typically 20% SOC).
4. **Bring solar/wind online**: Once battery provides voltage reference, solar inverters and wind turbines can synchronize to the microgrid and take over generation.
5. **Re-energize loads in sequence**: Tier 1 first, then Tier 2 as generation exceeds demand.
6. **Transition to autonomous operation**: Once renewable generation exceeds load, generator can be shut down.

**Time to black start**: With a functioning generator, 15–30 minutes. Trained operator required — this is a key reason to invest in community training programs.

### Multi-Microgrid Coordination

ORNL research (Vieques) demonstrated a novel orchestrator system allowing adjacent microgrids to share generation when one loses solar (cloud cover, damage). In Zone 5, this means a town with a fire station microgrid and a school microgrid can potentially support each other during extended outages. Technical requirement: communication link between microgrid controllers (can be radio or wired) + shared islanding protocol.

For Zone 5 communities planning multiple buildings: design for peer-to-peer coordination from the beginning, even if it is not implemented until Phase 2. The cost of adding communication ports at installation time ($500–$2,000 per site) is far less than retrofitting later.

---

## Section 6: Organizations Working on Community Energy

Ten organizations with direct relevance to Zone 5 community microgrid implementation:

1. **DOE Office of Electricity — C-MAP (Community Microgrid Assistance Partnership)**: Direct funding and technical assistance for rural/remote community microgrids. 14 projects active as of June 2025. Application portal at energy.gov/oe/community-microgrid-assistance-partnership.

2. **NRECA (National Rural Electric Cooperative Association)**: Led the $45M DOE CARED consortium. Technical resources and training for rural electric cooperatives. Publishes case studies via cooperative.com. Contact: NRECA Research division.

3. **Clean Coalition**: Established the Community Microgrid Initiative. Developed standardized methodology for deploying community microgrids that provide 25%+ local renewable energy while maintaining grid reliability. Active regulatory filings with California and Midwest utilities. clean-coalition.org/community-microgrids.

4. **EESI (Environmental and Energy Study Institute)**: Publishes accessible case studies and policy analysis on rural microgrids and cooperative energy. eesi.org — multiple Zone 5-relevant articles.

5. **IREC (Interstate Renewable Energy Council)**: Four years of post-Maria Puerto Rico work developing replicable community solar+storage deployment models. irecusa.org. Relevant resources on permitting, interconnection, and workforce development.

6. **RMI (Rocky Mountain Institute)**: Hurricane-proof energy work for Puerto Rico; solar+wind+storage portfolio analysis. Published 2019 finding that clean energy portfolios outperform natural gas investments economically. rmi.org.

7. **Wisconsin Energy Institute / RENEW Wisconsin**: Regional technical resources and advocacy. Bayfield County projects honored in RENEW Wisconsin 2023 Clean Energy Honor Roll. energy.wisc.edu.

8. **Chequamegon Bay Renewable Energy Resources (CBRER)**: Local Zone 5 organization in Bayfield County area. Direct contact for Bayfield microgrid lessons learned. cheqbayrenewables.org.

9. **muGrid Analytics**: Technical consulting firm that designed the Bayfield County microgrid system. Published case studies. mugrid.com/projects/bayfield. Directly relevant for Zone 5 project development.

10. **Earthjustice / Citizens Utility Board (Illinois)**: Legal and regulatory advocacy for distributed energy rights in Illinois. Citizens Utility Board publishes accessible community solar guides. citizensutilityboard.org.

---

## Section 7: Implementation Timeline and Resource Requirements

### Phase 1: Community Assessment and Feasibility (Months 1–6)

**Actions**:
- Baseline energy audit: document all loads (demand in kW, annual consumption in kWh, seasonal patterns)
- Map critical facilities: which buildings must have power during an outage? (clinic, fire station, water pump, community shelter, food storage)
- Identify renewable resources: solar rooftop availability, ground-mount land, wind exposure
- Run HOMER Energy model with PVWatts data for your location
- Contact state USDA Rural Development Energy Coordinator for REAP status
- Contact utility interconnection department for pre-application meeting

**Resources needed**: 1 part-time project coordinator (existing community staff or volunteer engineer), $5,000–$15,000 for HOMER Energy subscription and professional energy audit if needed.

**Outputs**: Feasibility report with system sizing recommendation, preliminary cost estimate, list of applicable grants/incentives.

### Phase 2: Funding and Permitting (Months 6–18)

**Actions**:
- Submit REAP grant application (when open; up to $1M for renewable energy systems)
- Apply to DOE C-MAP if eligible (underserved, rural, or Indigenous community)
- File utility interconnection application (start early — this is the longest timeline item)
- Engage state rebate programs (Illinois CEJA DG rebate, Michigan MPSC programs, Wisconsin Focus on Energy)
- Explore municipal bond, rural development loan, or cooperative financing for remaining capital
- Hire engineer for one-line diagrams, protection coordination study, building permits

**Resources needed**: $50,000–$150,000 engineering services; legal counsel for utility agreements; project manager.

**Timeline warning**: Utility interconnection approval alone takes 3–12 months. Do not order equipment until interconnection agreement is in hand.

### Phase 3: Installation and Commissioning (Months 15–24)

**Actions**:
- Procure equipment (6–12 week lead times for inverters and large batteries; order early)
- Install solar arrays, battery enclosures, wind turbines if applicable
- Install microgrid controller, transfer switches, protection relays
- Commission: tune inverter droop settings, test load shedding sequences, perform intentional islanding test under controlled conditions
- Train community operators: black start procedure, load shedding manual override, safety protocols

**Costs at this phase** (100-person community, critical-load focus):
- 80 kW solar: $80,000–$120,000
- 400 kWh LiFePO4 storage: $50,000–$130,000
- 40 kW backup generator: $25,000–$40,000
- 20 kW wind (if applicable): $60,000–$100,000
- Microgrid controller + switchgear: $20,000–$50,000
- Electrical installation labor: $80,000–$150,000
- **Total**: $315,000–$590,000 before incentives

### Phase 4: Operation and Evolution (Year 2 onward)

**Actions**:
- Track reliability metrics: outage events prevented, percentage of critical load served during grid outages
- Monitor battery state of health; plan cell replacement at year 8–12
- Plan iron-air storage retrofit (2027–2028): Form Energy's commercial product provides 100-hour storage at an estimated $77–$100/kWh installed, dramatically extending winter resilience without generator reliance
- Add second microgrid sites (school, agricultural cooperative) and link via OpenFMB peer-to-peer coordination
- Document and share lessons learned with EESI, NRECA, and DOE C-MAP for national knowledge base

---

## Section 8: Cross-Domain Integration

### Connection to Off-Grid-Living Project

The household scale (off-grid-living project) and community scale (this research) are complementary layers:

**Household layer** (off-grid-living): 40–50 homes × 5 kW solar + 10–20 kWh battery = 200–250 kW distributed generation capacity. Each home operates autonomously for 1–2 days during outages.

**Community layer** (this research): Central 80–100 kW solar + 20 kW wind + 400 kWh battery + 40 kW generator = community critical infrastructure protected for 5+ days.

**Combined effect**: During a 120-hour outage, households manage their own needs for the first 24–48 hours using individual systems, while the community microgrid continuously maintains water, heat, medical, and communications infrastructure. By day 3, community members whose individual batteries are depleted can gather at community-powered facilities. This is the layered resilience architecture.

**Key technical bridge**: If individual homes have grid-tied inverters, they shut down during a grid outage (anti-islanding protection). To contribute to the community microgrid, they need either (a) dedicated off-grid inverters with manual transfer switches, or (b) smart inverters that can synchronize to the community microgrid bus. Plan for this in the community microgrid controller design — it requires "smart grid" capable inverters at the household level (e.g., Enphase IQ8, SMA Sunny Boy Storage) that can operate in both grid-connected and islanded modes.

### Connection to Seedwarden Project

Agricultural loads are both a challenge and an asset for community microgrids:

**Challenge**: Irrigation pumps (5–50 kW), grain dryers (50–200 kW), and dairy cooling (10–40 kW) are large, variable loads that can destabilize a small microgrid if they cycle on/off without coordination.

**Asset**: These loads are dispatchable — they can be shifted in time. A grain dryer that runs when wind generation is high and pauses when batteries are low is a "virtual generator" that stores renewable energy as dried grain. A cold storage facility that pre-chills during solar peaks is a thermal battery.

Seedwarden project integration: embed load flexibility logic into the seedwarden seed storage protocol. Cold storage facilities that protect seeds and food should be designed with thermal mass (insulation + thermal flywheel capacity) that allows 6–12 hours of operation without active cooling — enabling them to coast through grid-down periods without draining the community microgrid.

---

## Sources (55+ Citations)

### Architecture and Technical Standards
1. [IEEE 1547-2018 Intentional Island Requirements — NREL](https://www.nrel.gov/grid/ieee-standard-1547/requirements-for-intentional-islands)
2. [NREL IEEE 1547-2018 Standard Guidance](https://www.nrel.gov/grid/ieee-standard-1547/)
3. [IEEE 2030.10-2021 DC Microgrids for Rural Applications — IEEE Xplore](https://ieeexplore.ieee.org/document/9646866)
4. [Grid-Aware Islanding and Resynchronisation of AC/DC Microgrids — arXiv 2025](https://arxiv.org/pdf/2503.04597)
5. [DC Microgrid Architecture for Rural Electrification — IEEE Xplore](https://ieeexplore.ieee.org/document/7104427)
6. [Sustainable Rural Electrification via Solar PV DC Microgrids — MDPI Processes](https://www.mdpi.com/2227-9717/8/11/1417)
7. [Energy Management Strategy for Rural DC Microgrid — MDPI Applied Sciences](https://www.mdpi.com/2076-3417/8/4/585)
8. [Droop Control in Islanded Microgrids — IET Renewable Power Generation 2025](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/rpg2.13186)
9. [Virtual Synchronous Machine Control for Islanded AC Microgrids — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0378779620307744)
10. [NREL Microgrid Voices of Experience — NREL Report fy21osti/75909](https://docs.nrel.gov/docs/fy21osti/75909.pdf)
11. [NREL IEEE 1547-2018 Adaptation for Local Grid Codes — NREL Report fy24osti/87756](https://docs.nrel.gov/docs/fy24osti/87756.pdf)
12. [Finite-Control-Set MPC for Islanded Hybrid Microgrids — arXiv](https://arxiv.org/pdf/1802.04435)
13. [Backward Neural Network for Islanded DC Microgrid Control — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11233949/)
14. [Coordinated Energy Management for DC Microgrid with Hybrid Storage — Wiley Engineering Reports 2025](https://onlinelibrary.wiley.com/doi/full/10.1002/eng2.70241)

### Community Deployment and Policy
15. [DOE C-MAP Community Microgrid Assistance Partnership](https://www.energy.gov/oe/community-microgrid-assistance-partnership)
16. [DOE C-MAP Launch Announcement](https://www.energy.gov/oe/articles/us-department-energy-launches-community-microgrid-assistance-partnership)
17. [EESI Three Microgrid Projects Rural DOE Program](https://www.eesi.org/articles/view/three-microgrid-projects-in-rural-areas-showcase-new-doe-program)
18. [EESI Microgrids and Energy Improvements in Rural Areas](https://www.eesi.org/articles/view/microgrids-and-energy-improvements-in-rural-areas)
19. [EESI Three Rural Cooperatives Clean Energy](https://www.eesi.org/articles/view/powering-affordable-clean-energy-in-rural-areas-showcasing-three-rural-cooperatives)
20. [NRECA CARED Project $45M DOE Award](https://www.electric.coop/co-op-consortium-selected-for-45m-in-doe-funding-for-rural-microgrids)
21. [NRECA Microgrid Deployment Funding Selection](https://www.electric.coop/nreca-consortium-of-electric-co-ops-selected-for-microgrid-deployment-funding)
22. [DOE $8M Microgrid Innovation Announcement](https://www.energy.gov/oe/articles/us-department-energy-announces-8m-microgrid-innovation)
23. [Clean Coalition Community Microgrid Initiative](https://clean-coalition.org/community-microgrid-initiative/)
24. [NRECA RESDP Case Study WREA August 2024](https://www.cooperative.com/programs-services/bts/Rural-Energy-Storage-Deployment-Program/Documents/RESDP-Case-Study-WREA-August-2024.pdf)
25. [NREL Technical Assistance for Microgrids in Remote Communities 2024](https://www.nrel.gov/news/detail/program/2024/technical-assistance-supports-microgrids-in-remote-communities)

### Bayfield County Case Study (Zone 5)
26. [Bayfield County Wisconsin Microgrid — WPR](https://www.wpr.org/economy/bayfield-county-microgrid-extreme-weather-power-xcel-energy)
27. [Bayfield County Microgrid — muGrid Analytics Case Study](https://www.mugrid.com/projects/bayfield)
28. [Bayfield County RENEW Wisconsin 2023 Honor Roll — AltEnergyMag](https://www.altenergymag.com/news/2024/03/20/bayfield-countys-microgrid-projects-honored-in-renew-wisconsins-2023-clean-energy-honor-roll/41625/)
29. [Bayfield County Community Energy Resilience Update — Official County Document](https://www.bayfieldcounty.wi.gov/DocumentCenter/View/19952/Solar-Energy-Summary-25x25-2026)
30. [Wisconsin Energy Institute Podcast: Resilience through Microgrids](https://energy.wisc.edu/news/podcast-creating-resilience-through-microgrids)
31. [Chequamegon Bay Renewable Energy Resources — Local Zone 5 Organization](https://www.cheqbayrenewables.org/)

### Storage Technology
32. [NREL Cost Projections for Utility-Scale Battery Storage 2025 — fy25osti/93281](https://docs.nrel.gov/docs/fy25osti/93281.pdf)
33. [LiFePO4 Battery Cost Guide 2025 — SolarTechOnline](https://solartechonline.com/blog/lithium-iron-phosphate-battery-solar-guide/)
34. [Cost of Battery Storage Per kWh 2026 — Ambit Energy / VIP Energy](https://vipenergyservice.com/energy-storage/cost-of-battery-storage-per-kwh/)
35. [Form Energy Iron-Air Battery Expansion 2026](https://discoveryalert.com.au/form-energy-iron-air-battery-expansion-economics-2026/)
36. [Minnesota PUC Approves Xcel/Form Energy 10MW/1000MWh Battery — Utility Dive](https://www.utilitydive.com/news/minnesota-puc-xcel-form-energy-battery-sherco-solar/685460/)
37. [Form Energy + Crusoe 12 GWh Iron-Air Agreement](https://formenergy.com/form-energy-crusoe-announce-agreement-for-12-gigawatt-hours-of-iron-air-batteries-for-ai-data-centers/)
38. [Google Minnesota 30GWh Form Energy Iron-Air Battery — Energy Storage News](https://www.energy-storage.news/google-minnesota-data-centre-energy-deal-includes-30gwh-multi-day-iron-air-batteries-from-form-energy/)
39. [Iron-Air Battery Form Energy $405M Raise + GE Vernova — Utility Dive](https://www.utilitydive.com/news/iron-air-battery-developer-long-duration-storage-form-energy-collaboration-ge-vernova/730633/)

### Illinois / Midwest Regulatory Policy
40. [Illinois CEJA Implementation — ICC](https://www.icc.illinois.gov/programs/climate-and-equitable-jobs-act-implementation)
41. [Illinois Solar Incentives 2026 — EnergySage](https://www.energysage.com/local-data/solar-rebates-incentives/il/)
42. [Illinois Solar Incentives Changing 2026 — Windfree Solar](https://windfree.us/illinois-solar-incentives-are-changing-what-homeowners-need-to-know-in-2026/)
43. [Illinois Battery Storage Legislation 8.5 GW — Energy Storage News](https://www.ess-news.com/2024/10/16/illinois-energy-storage-legislation-calls-for-8-5-gw-of-projects-through-2050/)
44. [ComEd / Ameren Illinois Energy Rebates 2026 — RebateAtlas](https://rebateatlas.org/states/illinois/)
45. [Michigan BESS Planning Guide — Graham Sustainability Institute](https://graham.umich.edu/project/bess-guide)
46. [Michigan BESS 150MW/600MWh Approval — Energy Storage News](https://www.energy-storage.news/esa-announces-approval-for-150mw-600mwh-michigan-bess/)
47. [Michigan Public Act 233 of 2023 — Battery Storage Target](https://graham.umich.edu/media/files/BESS-guide.pdf)
48. [Wisconsin Solar and Storage — SEIA](https://seia.org/state-solar-policy/wisconsin-solar/)
49. [FERC Order 2222 DER Aggregation Explainer](https://www.ferc.gov/ferc-order-no-2222-explainer-facilitating-participation-electricity-markets-distributed-energy)
50. [FERC Order 2222 Tracker November 2024](https://cuswebsite.blob.core.windows.net/2222tracker/Tracker-Report-November-2024.pdf)
51. [FERC 2026 Outlook for Storage and Inverter-Based Resources — Morgan Lewis](https://www.morganlewis.com/pubs/2026/03/federal-regulatory-outlook-for-electric-storage-qfs-and-inverter-based-resources)
52. [Citizens Utility Board — Community Solar Illinois](https://www.citizensutilityboard.org/community-solar-illinois/)

### USDA and Rural Energy Programs
53. [USDA REAP Renewable Energy Systems Program](https://www.rd.usda.gov/programs-services/energy-programs/rural-energy-america-program-renewable-energy-systems-energy-efficiency-improvement-guaranteed-loans)
54. [USDA REAP IRA Funding Overview](https://www.rd.usda.gov/inflation-reduction-act/rural-energy-america-program-reap)
55. [USDA New ERA Project Announcements](https://www.rd.usda.gov/new-energy-deployment/new-era-project-announcements)

### Grid Resilience and Crisis Analysis
56. [NREL Black Start Grid Modernization](https://nrel.gov/grid/black-start.html)
57. [NREL Solar-HERO All-Data Grid Recovery](https://www.nrel.gov/news/detail/program/2023/nrel-and-partners-build-all-data-approach-for-automated-grid-recovery)
58. [NREL Valuing Resilience for Microgrids — NARUC](https://pubs.naruc.org/pub/1B571AB6-1866-DAAC-99FB-2509F05E4A67)
59. [PNNL Microgrid Handbook for Army Resilience — PNNL-38494](https://www.pnnl.gov/main/publications/external/technical_reports/PNNL-38494.pdf)
60. [Load Shedding Preplan for Unplanned Microgrid Islanding — ScienceDirect 2025](https://www.sciencedirect.com/science/article/pii/S0142061525004806)
61. [Islanded Microgrid Restoration with Graph Analysis — arXiv](https://arxiv.org/pdf/2103.16709)
62. [2021 Texas Power Crisis Cascading Risks — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2214629621001997)
63. [DEITABASE Texas 2021 Grid Failure Analysis — UMich LIMOS](https://limos.engin.umich.edu/deitabase/2024/12/27/2021-texas-power-grid-failure/)
64. [Lessons from the Texas Big Freeze — Energy Innovation](https://energyinnovation.org/wp-content/uploads/2021/05/Lessons-from-the-Texas-Big-Freeze.pdf)

### Puerto Rico Case Studies
65. [EESI Microgrids in Puerto Rico Keep Rural Communities Connected](https://www.eesi.org/articles/view/microgrids-in-puerto-rico-keep-rural-communities-connected)
66. [Cornell/Vieques Mobile Battery Microgrid Resilience — Cornell Chronicle](https://news.cornell.edu/stories/2026/04/storm-ravaged-vieques-microgrid-builds-resilience)
67. [ORNL Puerto Rican Microgrid Orchestrator Research](https://www.ornl.gov/news/researchers-bring-more-reliable-electricity-puerto-rican-microgrids)
68. [IREC Puerto Rico Post-Maria Rebuilding](https://irecusa.org/blog/irec-news/four-years-after-hurricane-maria-irec-is-helping-puerto-rico-rebuild/)
69. [Earthjustice Distributed Solar and Battery for Puerto Rico](https://earthjustice.org/feature/distributed-rooftop-solar-battery-puerto-rico)
70. [RMI Hurricane-Proof Energy for Puerto Rico](https://rmi.org/hurricane-proof-energy-for-puerto-rico/)

### Open-Source Tools and Platforms
71. [HOMER Energy — homerenergy.com](https://homerenergy.com/)
72. [PVWatts — NREL](https://pvwatts.nrel.gov/)
73. [GridLAB-D Open-Source Simulation — ResearchGate](https://www.researchgate.net/publication/224312177_GridLAB-D_An_Open-Source_Power_Systems_Modeling_and_Simulation_Environment)
74. [OpenDSS Microgrid Simulation — Springer](https://link.springer.com/chapter/10.1007/978-981-19-6383-4_42)
75. [PandaPower 500K Downloads — Fraunhofer IEE](https://www.iee.fraunhofer.de/en/presse-infothek/press-media/2024/pandapower-open-source-tool-for-modelling-analyzing-power-grids.html)
76. [OpenFMB for DER Management — SEPA Green Ovations](https://sepapower.org/knowledge/green-ovations-open-source-smarts-openfmb-supports-der-management/)
77. [OpenFMB Microgrid Communications — OSTI](https://www.osti.gov/servlets/purl/1885229)
78. [pymgrid Open-Source Virtual Microgrid — arXiv](https://arxiv.org/pdf/2011.08004)
79. [Real-Time Energy Management for Community Microgrids — arXiv 2025](https://arxiv.org/pdf/2506.22931)

### Midwest Renewable Energy Context
80. [Midwest Solar and Wind Capacity — Illinois Clean Energy](https://cleanenergy.illinois.gov/tracking-illinois-progress/midwest-solar-wind-capacity.html)
81. [Iowa Utility-Scale Wind and Solar — Iowa State AgPolicy Review](https://agpolicyreview.card.iastate.edu/winter-2022/utility-scale-wind-and-solar-development-iowa-trends-prospects-and-land-factor)
82. [NREL Wind and Solar Hybrid Plants for Energy Resilience](https://research-hub.nrel.gov/en/publications/wind-and-solar-hybrid-power-plants-for-energy-resilience/)
83. [AgriTechTomorrow Agricultural Microgrids 2025](https://www.agritechtomorrow.com/story/2025/07/enhance-farm-resilience-with-agricultural-microgrids/16782/)
84. [Peoples Company — Renewable Energy in Midwest Future](https://peoplescompany.com/blog/renewable-energy-in-the-midwest-powering-the-future)
85. [Tribal Community Energy Resilience with Microgrids — Microgrid Knowledge](https://www.microgridknowledge.com/remote-microgrids/article/55039224/tribal-communities-want-energy-resilience-with-microgrids-is-the-us-stepping-up)

---

## Confidence Assessment and Evidence Gaps

**High confidence** (multiple sources, consistent data):
- LiFePO4 battery cost trends ($240/kWh cell-level, $125–$334/kWh installed at utility scale)
- Illinois CEJA rebate structure and January 2025 net metering change
- Bayfield County microgrid technical specifications (841 kW solar, 1,065 kW storage, 28 communities)
- Load shedding tier protocols (multiple peer-reviewed and DOD sources)
- Iron-air battery (Form Energy) commercial status — production at Weirton WV, 2025–2026 first deliveries

**Moderate confidence** (fewer sources, some extrapolation):
- Zone 5 seasonal solar capacity factors (derived from NREL databases; specific values require PVWatts run for each community location)
- Sizing calculations for 100-person community (based on general rules of thumb; actual sizing requires site-specific load audit)
- Iron-air cost per kWh for community scale (current data is utility-scale at $77–$100/kWh; community-scale pricing may differ significantly)

**Evidence gaps**:
- No peer-reviewed case studies found for Zone 5 Indiana community microgrids specifically
- Limited data on interconnection timelines specifically for rural electric cooperatives in Illinois vs. investor-owned utilities — Bayfield County used Xcel Energy's cooperative territory
- Long-duration storage (iron-air) pricing for systems under 1 MW — Form Energy data is for 10 MW+ utility contracts; small community pricing unknown
- FERC Order 2222 revenue potential for Midwest microgrids — proceeding still active; numbers cannot be projected reliably

---

*Research complete. Document integrates Phase 5 Wave 2 deliverable scope. Cross-referenced to off-grid-living (household layer) and seedwarden (agricultural loads) projects. Recommended next step: commission community-specific HOMER Energy model using site load data and PVWatts output for the target location.*
