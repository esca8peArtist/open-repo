---
title: "Phase 5 Wave 2 — Distributed Microgrids as Community Resilience Infrastructure"
project: systems-resilience
phase: 5
wave: 2
domain: distributed-microgrids
status: PRODUCTION-READY
research_date: 2026-05-26
scope: Zone 5 Midwest (IL, MI, IA, IN, WI) — 50–5000-person community scale
resilience_target: 120-hour sustained grid failure
decision_gate: "May 31–June 1 — Phase 5 Wave 2 execution order"
word_count: ~4600
source_count: 50+
cross_references:
  - projects/systems-resilience/PHASE_5_WAVE_2_MICROGRIDS_RESEARCH.md (companion deep-dive, 6,000 words)
  - projects/off-grid-living (household scale)
  - projects/seedwarden (agricultural load context)
---

# Phase 5 Wave 2: Distributed Microgrids as Community Resilience Infrastructure

**Research completed**: May 26, 2026
**Scope**: Zone 5 Midwest (IL, MI, IA, IN, WI) — rural and peri-urban contexts
**Sizing focus**: Communities of 50–5,000 people across three scales
**Resilience target**: 120-hour (5-day) sustained grid failure in winter conditions

---

## Executive Summary

Microgrids are the most mature, federally-funded, and technically proven path to sustained community-scale power independence available as of 2026. The United States has more than 687 operational microgrids with 4,357 MW of installed capacity growing at 13% annually. Federal investment has accelerated sharply: the DOE Community Microgrid Assistance Partnership (C-MAP) deployed $5.5 million across 14 projects in June 2025, and NRECA's cooperative consortium secured $45 million in DOE funding for rural deployment. Bayfield County, Wisconsin — directly in Zone 5 — became the flagship case study: 841 kW solar and 1,065 kW battery storage across 24 sites serving 28 communities, providing autonomous islanded operation for critical facilities during outages.

Three findings are critical for Zone 5 communities:

**1. Hybrid AC/DC architecture with LiFePO4 storage is the proven design** for communities of 50–500 people. Grid-forming inverters (not grid-following) are essential for islanded operation; they provide voltage and frequency reference without a synchronous generator. Iron-air long-duration storage (100+ hours) reaches commercial scale in 2026–2027 and should be planned as a retrofit layer for 500–5,000-person systems.

**2. The Illinois regulatory environment changed materially in January 2025** and two federal tax credits expired December 31, 2025. Net metering for new Illinois installations is now supply-only (no delivery credit). The residential 30% ITC is gone. Communities must now finance through commercial tax-equity structures, REAP grants, cooperative ownership, or DOE C-MAP assistance to access remaining incentives. Wisconsin, Michigan, and Iowa retain stronger distributed-energy frameworks.

**3. 120-hour winter resilience in Zone 5 requires hybrid storage plus generator backup.** Zone 5 December solar produces only 25–40% of summer output. Solar-only systems cannot carry a community through a multi-day Midwest ice storm. The validated design: 400+ kWh LiFePO4 battery + 40–50 kW biogas/diesel generator backup + 20 kW small wind + 80–100 kW solar = 120-hour critical-load resilience at $215,000–$420,000 capital cost before grants. After REAP, C-MAP, and state rebates, net community cost drops to $500–$1,500 per capita.

**Key implementation implication**: Microgrid commissioning from feasibility study to islanding capability takes 18–36 months. Communities that begin feasibility and utility interconnection applications in mid-2026 can achieve operational status by 2027–2028. Begin now.

---

## Section 1: Microgrid Architecture Typologies

### AC, DC, and Hybrid Configurations

A microgrid is a bounded, controllable group of distributed energy resources and electrical loads — solar panels, batteries, wind turbines, generators, EV chargers — that can operate either connected to the main grid or as a self-sustaining island. The islanding capability — detecting grid failure and disconnecting safely within milliseconds while maintaining internal power — is what distinguishes a microgrid from a standard solar installation.

**AC Microgrids (Alternating Current)**: The conventional design. All generation is converted to standard 120V/240V AC before distribution. Every solar panel and battery requires a DC-to-AC inverter, producing 10–15% conversion losses per stage. Advantages: compatible with all existing appliances and infrastructure; uses standardized electrician skills. Disadvantages: conversion losses accumulate; large inverter arrays required; every conversion point is a failure point. Standard voltage levels: 120/240V single-phase residential, 208/480V three-phase commercial. For communities, three-phase 480V distribution with step-down transformers at each building is the most common design.

**DC Microgrids (Direct Current)**: Solar panels and batteries are natively DC; DC microgrids eliminate conversion for DC loads (LED lighting, electronics, EV charging), reducing losses to 3–5%. IEEE 2030.10-2021 specifically covers DC microgrids for rural and remote applications. Disadvantages: fewer off-the-shelf appliances; industrial motors, water pumps, and heating elements require either AC or purpose-built DC versions. Voltage levels: 48V for small systems (under 10 kW), 380V DC for building-scale, 750V DC for community distribution. Best suited for new-construction communities with predominantly DC loads.

**Hybrid AC/DC Microgrids (recommended for Zone 5 communities)**: A bidirectional DC bus collects solar and battery power at 380–750V DC; an AC bus serves standard appliances via bidirectional interlinking converters. Total conversion loss: 5–8% versus 15%+ for pure AC. Transition time during grid failure: under 50 milliseconds. This architecture is validated by NREL research, UC San Diego (33 MW campus microgrid), Blue Lake Rancheria (California tribal microgrid), and Bayfield County, Wisconsin. It is the standard recommended by IEEE 2030.9-2019 (Recommended Practices for Microgrid Controllers).

### Inverter Topologies and Grid-Forming vs. Grid-Following

The inverter is the most critical component in any islanded microgrid. Two fundamentally different control modes exist:

**Grid-Following Inverters (GFL)**: The standard in almost all residential and commercial solar installations. A GFL inverter synchronizes to an external voltage and frequency reference provided by the main grid. It cannot establish its own frequency. Consequence: a GFL inverter shuts down automatically when the main grid fails, as anti-islanding protection required by IEEE 1547. **A community with only GFL inverters cannot island**; it will lose power the moment the grid fails, regardless of how much solar and battery capacity it has.

**Grid-Forming Inverters (GFM)**: Can establish their own voltage and frequency reference, operating as a "virtual synchronous machine." GFM inverters are essential for any islanded microgrid. Key control techniques:
- **Droop control**: Each inverter proportionally adjusts output based on frequency and voltage deviations. No communication required between inverters. Widely used, scalable, stable for up to ~80–85% inverter-based resource (IBR) penetration in islanded operation. [MDPI Electronics 2024, NREL fy25osti/96530]
- **Virtual Synchronous Generator (VSG/VSM)**: Inverters emulate the rotational inertia of a synchronous generator, providing smoother frequency response during sudden load changes. More complex; preferred for large systems (500+ kW) with variable loads like grain dryers. [IET Renewable Power Generation 2024]
- **Virtual oscillator control (VOC)**: Emerging technique using nonlinear oscillator dynamics for decentralized control; supports 100% IBR penetration. Research stage but progressing to commercialization. [arXiv 2025]

**Practical note**: Modern grid-forming capable inverters include Schneider Electric XW+, SMA Sunny Island, Victron Quattro, and Enphase IQ8 (microinverter-scale). All Zone 5 community microgrid designs must specify GFM-capable inverters at the inverter procurement stage — retrofitting later is expensive.

### VFD vs. Fixed-Frequency Backup

Variable Frequency Drives (VFDs) are used to control motor-driven loads (water pumps, irrigation pumps, HVAC compressors, grain handling equipment). In an islanded microgrid, VFDs introduce a critical compatibility issue:

**VFDs as frequency-sensitive loads**: VFDs convert incoming AC to DC and back to variable-frequency AC. Many older VFDs are sensitive to frequency deviations outside ±2–5% of nominal (60 Hz). In an islanded microgrid using droop control, frequency may deviate to 58–62 Hz during transients. This causes older VFDs to trip on under/over-frequency protection, creating unexpected load drops that destabilize the microgrid.

**Mitigation options**:
1. Specify VFDs rated for ±5–10% frequency tolerance (most modern VFDs, manufactured post-2015)
2. Use fixed-frequency backup (synchronous generator) as grid reference whenever VFD-driven loads are active during islanded operation
3. Implement intentional load sequencing: bring VFD loads online one at a time after islanding is stable

**Fixed-frequency backup (diesel/biogas generator)**: A synchronous generator provides a stable 60 Hz reference regardless of renewable generation variability. For Zone 5 communities operating through winter storms where solar is minimal, a 40–100 kW diesel or biogas generator serving as frequency reference allows the entire community's VFD-equipped motors to operate normally. This is the design rationale for keeping synchronous generation even in heavily renewable-penetrated microgrids.

### Central vs. Distributed Control

**Centralized control**: Single energy management system (EMS) controller manages all assets. Appropriate for systems under 200 kW with 5–10 assets. Failure mode: EMS hardware failure disables entire microgrid. Cost advantage: single software license; simpler commissioning.

**Decentralized/peer-to-peer control**: Each inverter, battery, and generator negotiates with neighbors using local measurements (frequency, voltage, state of charge). No single point of failure. IEEE 2030.9 recommends multi-agent decentralized control for microgrids expected to operate autonomously for extended periods. Commercially available via OpenFMB protocol (NAESB standard, NREL-maintained). Appropriate for Zone 5 communities expecting 72–120-hour outages where EMS hardware failure is a real risk.

**Tiered control (practical standard for 50–500-person communities)**: Local controllers on each asset (inverter, battery string, generator) report to a site-level EMS; the EMS coordinates assets and handles load shedding; optional regional controller links multiple microgrids. This is the architecture deployed at Bayfield County (muGrid Analytics design) and in the NRECA CARED cooperative consortium. Recommended for Zone 5 communities.

### Islanding Detection Protocols

IEEE 1547-2018 defines three islanding scenarios:

1. **Unintentional islanding (prohibited)**: Grid-following inverters inadvertently form an island, creating safety hazard for utility workers. Must be detected and prevented within 2 seconds by passive (frequency/voltage deviation) or active (frequency shifting, impedance measurement) detection methods.
2. **Planned islanding**: Community EMS sends intentional island command before grid disconnection. Transfer time: 100–300 milliseconds. Zero power interruption if transfer switch is sufficiently fast.
3. **Automatic unplanned island formation**: EMS detects grid failure (frequency outside 59.3–60.5 Hz or voltage outside 88–110% of nominal), opens the Point of Common Coupling (PCC) isolation switch within 50 ms, and shifts all GFM inverters to island mode. Power interruption: under 50 ms (imperceptible for most loads; may cause momentary flicker for sensitive equipment). This is the target for Zone 5 winter-outage resilience.

**Hardware cost for islanding capability**: Transfer switch + isolation relay + EMS hardware: $15,000–$50,000 per microgrid site. This cost is separate from and in addition to solar, battery, and inverter costs.

---

## Section 2: Community-Scale Battery Storage

### LiFePO4 Chemistry: Why It Dominates Community-Scale Storage

Lithium Iron Phosphate (LiFePO4 or LFP) batteries are the dominant chemistry for community-scale storage as of 2026 for five reasons:

1. **Thermal stability**: LFP cathode does not undergo the exothermic decomposition that causes thermal runaway in NMC (Nickel Manganese Cobalt) chemistries. LFP cells can reach 270°C before decomposition; NMC cells fail at 150–180°C. For Zone 5 communities where battery enclosures may be in outbuildings subject to temperature extremes, this safety margin is critical.
2. **Cycle life**: LFP delivers 3,000–6,000 full charge-discharge cycles at 80% depth of discharge (DoD) before dropping to 80% capacity. At one full cycle per day (daily solar + overnight discharge), that is 8–16 years of service life without cell replacement. This exceeds the 10-year warranty periods offered by utility-scale BESS vendors including Tesla Megapack, BYD, and CATL.
3. **Operating temperature range**: Discharge: -20°C to 60°C (adequate for Zone 5 winter conditions). Charge: 0°C to 45°C (charging below 0°C requires battery heating). This matters: a battery bank in an unheated Midwest outbuilding on a -15°C January night must have active heating or the BMS will prevent charging.
4. **Cost trajectory**: Cell-level LFP: $240/kWh (2025, cell-only). Installed utility-scale BESS: $125–$334/kWh depending on project scale and duration (NREL fy25osti/93281, 2025). Community-scale (50–500 kW, 4-hour duration): $250–$400/kWh installed. Residential scale (10–20 kWh): $700–$1,300/kWh installed.
5. **Cobalt-free**: LFP contains no cobalt, avoiding both supply-chain ethical risks and the price volatility that affects NMC chemistries tied to Democratic Republic of Congo mining output.

**Limitation for 120-hour scenarios**: LFP's energy density (90–160 Wh/kg) is lower than NMC (150–220 Wh/kg). For a 120-hour storage requirement, LFP requires significantly more physical space and weight. At 40 kW critical load for a 100-person community over 120 hours: 6,000 kWh of LFP at 160 Wh/kg = 37,500 kg (37.5 tonnes) of cells alone. This is impractical as a pure battery-only solution, which is why the hybrid LFP + generator backup approach is the validated design.

**Iron-air long-duration storage (emerging)**: Form Energy's iron-air batteries operate on an oxidation/reduction cycle (iron "rusting" and "derusting"), achieving 100-hour storage duration at an estimated $77–$100/kWh installed for utility-scale deployments. Minnesota PUC approved Xcel Energy's 10 MW/1,000 MWh Form Energy deployment in 2024. Form Energy's Weirton, WV factory entered production in 2025. Community-scale pricing (under 1 MW) is unknown as of May 2026 — current contracts are 10 MW+. Plan for iron-air as a 2028+ retrofit layer once community-scale pricing is available.

### BMS Architecture for Sustained Discharge

A Battery Management System (BMS) monitors and controls every cell in a battery pack. For community-scale sustained discharge (120-hour scenarios), BMS architecture requires specific attention:

**Cell-level monitoring**: Temperature sensors on every cell (or every 4–8 cells in a module). During a 120-hour discharge at low rates (C/20 to C/5), cell temperature rises are modest (2–5°C above ambient), but cold ambient temperatures create a more dangerous scenario: in an unheated Zone 5 enclosure at -15°C, cells can drop below the BMS's charge inhibit threshold (typically 0°C). The BMS must trigger heating pads or blankets to maintain cells above 0°C before accepting charge from a generator or solar array.

**State of Charge (SOC) estimation**: During extended low-rate discharge, Coulomb counting (integrating current over time) accumulates error. A well-designed community BMS uses Kalman filter or extended Kalman filter SOC estimation combined with open-circuit voltage measurements during brief rest periods to recalibrate SOC. This is important for operators making load-shedding decisions: if the displayed SOC is inaccurate by ±10%, the community may shed critical loads prematurely or fail to shed discretionary loads in time.

**Cell balancing during discharge**: Passive balancing (dissipating excess energy as heat in resistors) is inadequate during sustained discharge cycles because it adds to thermal load and wastes energy. Active balancing (transferring energy between cells via DC-DC converters) maintains cell-to-cell SOC within ±1% without heat generation. Specified for any community-scale system expected to operate for 72+ hours without maintenance.

**Communication interfaces**: Community BMS must communicate with the microgrid EMS via CANbus, Modbus TCP, or IEC 61850 MMS. The EMS dispatches the battery based on whole-system state (solar output, wind output, generator status, load) rather than letting the BMS operate autonomously. Autonomous BMS operation without EMS oversight can result in suboptimal dispatch during multi-day outages.

### Thermal Management During 120-Hour Discharge

**Zone 5 winter temperature challenge**: Bayfield County, Wisconsin records January average lows of -14°C (-7°F) and extreme lows of -30°C. Battery enclosures must be either insulated (R-20+ wall insulation) or actively heated. Enclosure heating load: approximately 1–3 kW per 100 kWh of battery capacity to maintain 10°C minimum enclosure temperature at -20°C ambient. This heating load must be factored into the critical load budget for 120-hour scenarios.

**Heat generation during discharge**: At community scale (100–500 kW system), battery discharge rates during sustained islanding are typically C/10 to C/20 (10–5% of rated capacity per hour). At these low rates, cell heat generation is minimal: 0.1–0.3°C/hour temperature rise. Active cooling is not required for sustained low-rate discharge in Zone 5 conditions; passive ventilation is sufficient above 10°C ambient.

**Enclosure design**: Battery enclosures for Zone 5 should include thermal mass (concrete or masonry floor), R-20+ insulation, electric resistance heating on a separate Tier 1 power circuit (always energized during outage), and passive ventilation with automated dampers (closed during cold weather, open during summer). Cost: $15,000–$40,000 for a 100–400 kWh enclosure.

### Sizing Models by Community Scale

The following models assume Zone 5 winter critical-load scenarios with load shedding in effect. Critical loads only (water pumping, community heating, medical, communications, emergency lighting).

**50-person community (hamlet/small farm cluster)**:
- Critical load: 8–12 kW
- Daily critical consumption: 200–290 kWh
- LFP storage for 120 hours (no generation): 1,200–1,750 kWh
- Practical hybrid: 200 kWh LFP + 15 kW generator + 20 kW solar + 5 kW small wind
- Capital: $100,000–$200,000 before grants
- Per-capita before grants: $2,000–$4,000
- Applicable funding: USDA REAP grant (up to $1M), DOE C-MAP (if meets eligibility criteria), state utility rebates

**500-person community (small rural town)**:
- Critical load: 80–120 kW
- Daily critical consumption: 1,900–2,900 kWh
- LFP storage for 120 hours (no generation): 12,000–17,400 kWh — impractical as pure battery
- Practical hybrid: 400–600 kWh LFP + 100 kW generator + 200 kW solar + 50 kW wind
- Capital: $800,000–$1,800,000 before grants
- Per-capita before grants: $1,600–$3,600
- Applicable funding: REAP ($1M cap per project), DOE C-MAP, NRECA CARED model, community bond

**5,000-person community (small city/large township)**:
- Critical load: 800–1,200 kW
- Daily critical consumption: 19,000–29,000 kWh
- Practical design: 2,000–4,000 kWh LFP + 1,000 kW generator + 2 MW solar + 500 kW wind + demand response platform
- Capital: $8,000,000–$18,000,000 before grants (utility-scale pricing applies at this size)
- Per-capita before grants: $1,600–$3,600 (economies of scale offset larger absolute cost)
- Applicable funding: FERC Order 2222 wholesale market participation revenue, IRA Section 48E commercial battery credit (30%), DOE GRIP program, state infrastructure bonds
- Architecture note: at 5,000-person scale, FERC Order 2222 wholesale market participation becomes economically meaningful — the community microgrid can bid into MISO capacity markets as an aggregated distributed resource, generating revenue to offset capital costs. MISO Order 2222 compliance proceedings are ongoing as of May 2026.

---

## Section 3: Distributed Generation Strategies for Zone 5

### Solar PV: Resource and Sizing

Zone 5 has moderate solar resources adequate for community microgrids when paired with other generation. Using NREL PVWatts (1-axis tracking, NSRDB 1998–2014 averages):

| State | kWh/m²/day (annual avg) | December production (% of June) | Capacity factor |
|---|---|---|---|
| Illinois | 4.2 | 34% | ~13% |
| Wisconsin | 3.9 | 33% | ~12.5% |
| Michigan | 3.8 | 31% | ~11% |
| Iowa | 4.3 | 35% | ~13.5% |
| Indiana | 4.1 | 33% | ~12.8% |

**Key implication**: A 100 kW array producing 520 kWh/day in June produces only 170 kWh/day in December. Winter solar alone cannot sustain a Zone 5 community through a 5-day outage. Solar is the backbone of summer resilience; winter requires wind, generator, or long-duration storage to complement it.

**Sizing decision (rules of thumb)**:
- Size solar primarily for annual energy production, not peak output
- Target 1.5–2× critical daily load capacity in June production to ensure adequate summer autonomy
- Accept 60–70% shortfall vs. critical load in December — generator or wind fills the gap
- Flat/low-tilt arrays (10–15°) produce more total energy annually than steep tilts in Zone 5; tilted arrays (35–45°) produce relatively more in winter (when needed most)
- For 120-hour winter scenarios, a steeper tilt (35–40°) is preferable despite lower annual yield

### Wind: Zone 5's Seasonal Complement to Solar

Midwest wind is world-class and anti-correlated with solar seasonally — wind peaks in winter when solar is weakest, making the combination dramatically more effective than solar alone.

| State | Wind capacity factor at 80m hub height | Seasonal peak |
|---|---|---|
| Iowa | 40–45% | October–March |
| Illinois | 33–38% | October–March |
| Wisconsin | 30–35% | September–April |
| Michigan | 25–32% | September–April |
| Indiana | 25–30% | October–March |

**Small wind (10–100 kW)**: Appropriate for farm-scale and community-scale integration without utility-scale land requirements. 20 kW small wind turbine at 35% capacity factor = 7 kW average continuous output = 168 kWh/day. Capital: $60,000–$100,000 installed. Requires 1–3 acres of setback clearance from structures. Key vendors: Northern Power Systems (NPS), Bergey Windpower, Enercon small turbines. **For Zone 5 winter resilience, a small wind turbine is the highest-leverage single addition to a solar + battery microgrid**, reducing required generator run-time and battery storage by 30–40%.

Iowa wind lease payments: $4,000/MW/year — meaningful for rural landowners hosting wind turbines as part of a community energy project. [Iowa State AgPolicy Review]

**Renewable penetration limits**: In islanded AC microgrids using droop-controlled GFM inverters, stable operation is achievable at 80–85% instantaneous IBR (solar + wind) penetration with careful droop parameter tuning. At 85–100% instantaneous penetration, VSG or VOC control is required for frequency stability. The practical guidance for Zone 5 communities: design for 70% average renewable penetration (solar + wind covering 70% of annual energy), with the generator providing the remaining 30% and serving as frequency reference when renewable output is insufficient. [NREL fy25osti/96530; IET RPG 2024]

### Hydroelectric: Niche Applications

Zone 5 has limited small hydro potential except in specific locations (Michigan Upper Peninsula, Wisconsin northern rivers, Iowa/Illinois mill sites). Where a year-round stream with 5+ meters of head is available, micro-hydro (1–50 kW) is the most reliable and lowest-maintenance generation source available — continuous output regardless of weather, day/night, or season. A 5 kW run-of-river micro-hydro unit on a qualifying stream provides 43,800 kWh/year continuously. Capital: $20,000–$80,000 for 5–20 kW systems. If a qualifying stream exists on or adjacent to community land, micro-hydro should be evaluated first before any other generation source.

### Biogas from Agricultural Waste

Biogas (primarily methane) produced by anaerobic digestion of animal manure, food waste, or crop residues is the most Zone 5-appropriate fuel source for generator backup in community microgrids:

**Why biogas matters for Zone 5**:
- Diesel fuel supply chains can fail during extended winter outages (roads closed, fuel deliveries disrupted)
- Propane tanks require periodic refilling; a 2-month propane supply is possible but costly
- Biogas can be produced on-site from agricultural waste streams, creating a genuinely closed-loop fuel supply

**Wisconsin case study**: EnTech Solutions and Northern Biogas commissioned a microgrid-powered biogas facility in Springfield, Wisconsin, including 2.8 MW solar PV, batteries, and inverters. The facility processes waste from 4,000+ dairy cows into renewable natural gas. [Microgrid Knowledge, 2024]

**Iowa scale**: Marshall Ridge Renewable Energy Center processes waste from 8,000 Holsteins through three anaerobic digesters, producing renewable fuel. Iowa has permitted 15 new digester facilities since 2021. Iowa dairy biogas development is accelerating despite water quality concerns raised by investigative journalism. [Investigate Midwest, 2024]

**Community-scale biogas specification**:
- Minimum viable: 50-cow dairy or equivalent organic waste stream = 10–20 kW continuous generator output
- 200-cow dairy = 30–50 kW continuous
- Food waste + manure co-digestion (100-person community food waste + 50-cow dairy) = 15–25 kW continuous
- Generator fuel flexibility: biogas-adapted diesel generators (Caterpillar, Cummins biogas options) can operate on 60–70% biogas / 30–40% diesel blends without full conversion; full biogas conversion requires spark-ignited generator

**Sizing constraint**: Biogas production rate must match generator fuel demand. Over-generating biogas requires gas storage (biogas bag = low pressure, relatively cheap) or gas injection into pipeline (requires compression and interconnection). Under-generating biogas requires diesel supplementation.

### Fuel Backup: Diesel and Propane

For communities without biogas resources, diesel and propane remain the most practical generator fuels for Zone 5 winter backup:

**Diesel**: Higher energy density, well-understood supply chain, excellent cold-weather operability (with winterized fuel or additive). Generator cost: $15,000–$40,000 for 40 kW unit, $40,000–$80,000 for 100 kW unit. Fuel consumption: 40 kW generator at 50% load = ~4 L/hour diesel. 120 hours at 50% load = 480 L. A 2,000-liter on-site tank provides 250 hours of reserve at 40 kW 50% load — adequate for a 5-day outage with recharge cycles. Key limitation: refueling in extended winter emergencies. Minimum 90-day on-site fuel supply recommended.

**Propane**: Suitable for Zone 5 conditions (-40°C vaporization temperature; propane does not gel in cold weather unlike diesel). Dual-fuel engines can run on propane or natural gas. 500-gallon propane tank: ~$1,000 installed; 2,000-gallon: ~$3,500 installed. Propane energy content ~26 MJ/L versus diesel's ~36 MJ/L — propane generators run ~30% more fuel by volume for equivalent output.

---

## Section 4: Regulatory and Grid Interconnection Landscape (May 2026)

### Federal Policy Status

**Investment Tax Credit (ITC)**: The 30% residential ITC under IRA Section 25D expired December 31, 2025 for individual homeowners. Commercial entities, nonprofits, rural cooperatives, and tax-equity-structured community organizations may access the commercial ITC under Section 48E through 2027. Direct-pay provisions under Section 6417 allow eligible tax-exempt entities (nonprofits, cooperatives, tribal governments) to receive ITC as a direct cash payment rather than as a tax credit — this is the primary federal financing mechanism for community organizations.

**Standalone Battery Storage (Section 48E)**: 30% credit for battery storage independent of solar pairing. Valid through 2032 for commercial and nonprofit deployments. A community nonprofit or cooperative can install LFP battery storage and receive 30% of system cost back as a direct payment. This is materially significant for Zone 5 rural communities.

**USDA REAP (Rural Energy for America Program)**: $2 billion allocated through 2031 under IRA. Maximum grant: $1,000,000 for renewable energy systems. REAP applications were paused as of May 2026 — contact state USDA Rural Development Energy Coordinators (IL, WI, MI, IA, IN offices) for current status. REAP loans carry 80% federal guarantee (FY2025–2027).

**FERC Order 2222 (DER Aggregation)**: Requires regional transmission organizations to allow DER aggregations — including community microgrids — to participate in wholesale electricity markets. In MISO territory (Zone 5), compliance rulemakings are ongoing as of May 2026. Potential revenue stream for 500+ kW community microgrids that can aggregate and bid into MISO capacity markets. Timeline to operationalize: 2026–2028. [FERC 2222 Tracker, November 2024; Morgan Lewis 2026 Outlook]

### Zone 5 State Policies

**Illinois**: The Climate and Equitable Jobs Act (CEJA, 2021) is the most significant state energy legislation in the Midwest.
- Net metering (post-January 1, 2025): supply-only credit for new installations. Pre-2025 installations grandfathered at full retail net metering for system lifetime. This is a material economic change — new Illinois installations receive roughly 40–50% less value per exported kWh than pre-2025 installations.
- ComEd / Ameren DG rebates: $250–$300/kW for solar, $250–$300/kWh for battery storage (direct cash rebates for residential and community scale).
- Illinois storage target: 8.5 GW cumulative by 2050 (legislation enacted 2024). Community solar + storage combinations receive priority processing.
- Key contact for community solar + microgrid: Citizens Utility Board (citizensutilityboard.org); Illinois Power Agency (IPA) for community solar program applications.

**Michigan**: Public Act 233 of 2023 mandates 2,500 MW of energy storage by 2029 — the first statewide storage mandate in the Midwest. MPSC has approved 150 MW/600 MWh and 100 MW/400 MWh large BESS projects. Michigan is adding 1+ GW of solar capacity annually as of 2025. Proposed legislation would prevent utilities from charging standby rates to building owners with microgrids not in use. [Canary Media, 2025]. Graham Sustainability Institute (University of Michigan) published a BESS Planning Guide specifically for Michigan communities.

**Wisconsin**: PSC approved 488 MW of grid-scale battery storage as of 2023, with 617 MW pending. Focus on Energy program provides rebates for residential and commercial solar/storage. Bayfield County's microgrid program is Wisconsin's flagship community demonstration. The state's rural electric cooperative territory is Zone 5's most receptive interconnection environment for distributed energy.

**Iowa**: 64% of state electricity from wind and solar in 2023 — a world-leading renewable share. Average wind lease payment $4,000/MW/year. Iowa opened an Aggregators of Retail Customers (ARC) proceeding for FERC Order 2222 compliance. No strong community solar program as of 2026 — rural cooperative ownership is the primary vehicle.

**Indiana**: Lags other Zone 5 states. Net metering capped and frequently challenged by utilities. The primary opportunity for Zone 5 Indiana communities is direct ownership through nonprofit cooperative or municipality rather than third-party utility programs. Customers interconnected before July 2022 receive full retail NEM for 30 years (one of the longest grandfather periods nationally). [The Green Watt, 2026]

### Interconnection Timelines and Fee Structures

Utility interconnection approval is typically the longest timeline bottleneck and the most underestimated cost for community microgrid projects:

**Rural Electric Cooperatives (RECs)**: Most Zone 5 rural areas are served by RECs. Pre-application meeting: 2–4 weeks. Feasibility study: 60–90 days. Interconnection agreement execution: 30–60 days additional. Total: 4–7 months for systems under 500 kW. RECs are generally more receptive to distributed generation than investor-owned utilities (IOUs) — they have cooperative incentive alignment with member-owners pursuing energy independence.

**Investor-Owned Utilities (ComEd/Ameren in IL, Consumers Energy/DTE in MI, We Energies/Alliant in WI)**: Feasibility study: 60–90 days. System impact study (if triggered by capacity thresholds): 90–120 additional days. Interconnection agreement: 30–60 days. Total: 8–14 months. At large-scale (500+ kW), transmission-level impact studies can extend timelines to 18–24 months. The MISO interconnection backlog now stretches to 5+ years for utility-scale generation — but community-scale distribution-connected microgrids typically bypass MISO queues and use state-level utility interconnection processes.

**Standby charges**: Michigan has proposed legislation preventing utilities from charging standby rates to microgrid owners when systems are not in use. Illinois and Wisconsin continue to allow standby charges for customer-owned generation above certain sizes. Budget $500–$5,000/year standby charge for a 100–500 kW community system connected to an Illinois IOU.

**Interconnection cost per system**: Application fees ($500–$2,000 non-refundable), engineering study costs ($5,000–$25,000 for systems under 1 MW), protection equipment (transfer switches, isolation relays): $15,000–$50,000. Total interconnection-related costs (excluding generation equipment): $25,000–$80,000 for a 100–500 kW community microgrid.

---

## Section 5: Proven Case Studies

### Military Microgrids

**Fort Bliss (El Paso, TX) — Army's Pioneer Microgrid**: Fort Bliss built the Army's first-ever microgrid in 2013: 120 kW solar + 300 kW storage. Expanded to 15 MW distributed energy resources + 8 MW battery storage serving 142 buildings. Islanding protocol validated through multiple real-world test events. The Army Tactical Microgrid Standard (TMS) requires generators capable of "operating in islanded conditions with load requirements." The Army's target: a microgrid on every installation by 2035, with enough renewables + storage to self-sustain critical missions by 2040. [Microgrid Knowledge; Army.mil; PNNL-38494 Handbook]

**PNNL Microgrid Handbook for Army Resilience (PNNL-38494)**: The most comprehensive publicly available technical guide for microgrid design and operation, derived from Army installations. Three-tier load prioritization protocol, black start procedures, and islanding detection guidance are directly transferable to Zone 5 community microgrids. Available free at pnnl.gov.

### Island Grids

**Puerto Rico — Casa Pueblo Microgrid (Adjuntas)**: Following Hurricane Maria (2017), which left rural Puerto Rico without power for 9+ months, the nonprofit Casa Pueblo installed solar + battery microgrids across 13 local businesses. Phase 1: 41 kW solar + 74 kWh battery storage across five sites, commissioned May 2022. During Hurricane Fiona (2022), the Castaner microgrid kept lights on while surrounding areas lost power for days. Key lesson: **automatic transfer switch is critical** — without it, restarting after a storm requires manual on-site intervention. IREC documented the Castaner deployment as the replication model for rural community microgrids. [IREC, 2022; EESI, 2024]

**Vieques Island, Puerto Rico — ORNL Multi-Microgrid Orchestrator**: Cornell researchers delivered a mobile solar-powered battery system to Vieques (population 8,000). A parallel ORNL "orchestrator" system links multiple Vieques microgrids to share power between them when one loses solar generation. This demonstrated the first operational peer-to-peer multi-microgrid coordination in a real community setting. DOE released $325 million for the Programa de Comunidades Resilientes in August 2024, funding solar + battery for healthcare facilities and community centers. [Cornell Chronicle, 2026; ORNL News; DOE GDO, 2024]

**Hawaii — Hawaiian Electric ETIPP and Moloka'i Nanogrids**: Hawaiian Electric achieved 36% RPS in 2024, targeting 100% by 2045. ETIPP (Energy Transitions Initiative Partnership Project) identifies optimal Oahu microgrid locations. Ho'Ahu Energy Cooperative on Moloka'i issued RFP for 15 off-grid nanogrids (4 kW solar + 11 kWh battery each). Maui: AES Kuihelani Solar (60 MW + 240 MWh BESS) came online May 2024. [Hawaiian Electric; Microgrid Knowledge, 2024]

### University and Campus Microgrids

**UC San Diego**: 33 MW campus microgrid including gas-turbine cogeneration, solar, fuel cell, steam, and diesel. Can island from the main grid within milliseconds. Learned from the 2011 Southwest blackout (when they failed to shed load fast enough, causing a 5-hour outage): the post-2015 powerMAX protection system now detects and sheds noncritical loads within 50 ms of grid failure. **The UCSD case established the technical standard for fast load shedding that all community microgrid designs now follow.** [SEL; Microgrid Knowledge]

**Bronzeville Community Microgrid (Chicago, IL — Zone 5)**: ComEd's 7.7 MW community microgrid serving ~770 customers in Chicago's historically Black Bronzeville neighborhood. Completed simulated islanding test April 2019. Includes 750 kW PV, 500 kW/2 MWh energy storage, 5 MW dispatchable natural gas generation. Fully within Zone 5 and directly relevant as a utility-led community microgrid model in Illinois regulatory territory. [ComEd; Adaptation Clearinghouse]

### Tribal Microgrids

**Blue Lake Rancheria (California)**: 1 MW solar + LiFePO4 battery, tribal-owned and operated. Operational 2024. Demonstrates that communities of ~50 reservation residents can own and operate professional-grade microgrids. 4–8 hours backup during regional outages.

**Pine Ridge Reservation (Oglala Lakota Nation, SD)**: In 2025, the Oglala Lakota Nation deployed the first plug-in solar system permitted and legally interconnected by a U.S. electric utility: 100 portable 6.4 kW solar appliances (640 kW total), funded by a $5.5 million Bush Foundation Community Innovation Grant. Project Tiospaye works toward net-zero emissions via retrofits, electrification, and on-site renewables. [North American Clean Energy; ASES]

**Rosebud Sioux Reservation (SD)**: Sicangu Village Solar Project was forced to scale from 150 kW to 149 kW because South Dakota imposes a $4,000/month fee on projects 150 kW and above — demonstrating that state-level regulatory thresholds create perverse incentives that community planners must navigate. [multiple sources]

**Navajo Nation**: Kayenta Solar Program (phases I and II) totals 56 MW across 198 acres. NTUA received $100 million from USDA's Powering Affordable Clean Energy program in January 2025. Navajo Power Home received $5 million IRA grant for 1,000 off-grid solar + battery homes by end of 2025. 2024 federal funding loss (Trump administration) disrupted multiple tribal energy projects — a key risk factor for any tribal community planning federal-grant-funded infrastructure. [AZ Mirror; KJZZ; Utility Dive, 2025]

**Key tribal microgrid lesson**: Tribal land sovereignty creates unique advantages (no state utility commission jurisdiction; sovereign regulatory environment) and unique barriers (BIA lease approval timelines; federal funding vulnerability). Zone 5 tribal communities (Menominee in Wisconsin, Pokagon Band in Michigan/Indiana, Ho-Chunk in Wisconsin) should consult the Scale Microgrids "Tribal Lands" resource and DOE's Tribal Energy Program directly.

### Intentional Communities

**Dancing Rabbit Ecovillage (Rutledge, MO — Zone 5 adjacent)**: One of the largest collections of natural buildings in the Midwest. Dancing Rabbit operates under a covenant restricting fossil fuel use. Current electricity configuration relies on grid connection with individual household solar installations; the community is exploring but has not yet implemented a formal microgrid with islanding. This gap illustrates a common pattern in intentional communities: strong motivation for energy independence combined with governance complexity that delays formal microgrid implementation. [Dancing Rabbit; FIC]

**Earthhaven Ecovillage (Black Mountain, NC)**: Properties near Earthhaven feature off-grid solar. No documented community-scale islanded microgrid. North Carolina regulatory context differs substantially from Zone 5.

**Practical assessment**: As of May 2026, no well-documented intentional community microgrid with islanding capability and formal operational protocols was identified in available literature. The most replicable model for intentional communities at 50–500-person scale remains the Puerto Rico Casa Pueblo approach: anchor to existing businesses or community buildings (not residences) to provide critical services during outages, keep initial scope to 3–5 buildings with 40–80 kWh battery storage, and expand from a proven base.

---

## Section 6: Open-Source and DIY Microgrid Platforms

### Simulation and Design Tools

**HOMER Energy (homerenergy.com)**: The industry standard for community microgrid feasibility analysis. Inputs: site load profile, NREL solar/wind resource data (imported automatically from NSRDB), equipment costs, grant amounts. Outputs: optimal system configuration, net present cost, levelized cost of energy, reliability statistics (LPSP — Loss of Power Supply Probability). Free academic version; commercial version for advanced optimization. Start here for every Zone 5 community feasibility study.

**PVWatts (pvwatts.nrel.gov)**: NREL's free browser-based tool for solar production estimation. Enter GPS coordinates and system size; receive monthly kWh production using NSRDB data. Essential for Zone 5 seasonal production modeling and sizing.

**GridLAB-D (github.com/gridlab-d/gridlab-d)**: Open-source distribution system simulation from PNNL. High-fidelity modeling of microgrid operation, conservation voltage reduction, and DER integration. Best for validating a design before construction. Requires power systems engineering background.

**OpenDSS**: Open-source distribution system simulation from EPRI. Widely used by utilities and researchers for protection coordination and islanding studies. Good first tool for communities with an electrical engineer volunteer.

**PandaPower (pandapower.readthedocs.io)**: Python-based power flow analysis from Fraunhofer IEE. 500,000+ downloads; well-documented. Best for communities with Python-comfortable technical members who want to model power flow without a full SCADA simulation.

**pymgrid (github.com/Total-RD/pymgrid)**: Python virtual microgrid environment for machine-learning-based energy management development. Useful for communities developing automated dispatch algorithms or training operators on energy management decisions.

### Communication and Control Standards

**OpenFMB (Open Field Message Bus)**: NAESB-ratified standard (originally Duke Energy, ratified 2016). Enables real-time data exchange between microgrid components (inverters, meters, controllers) using MQTT or DDS protocols. Allows multi-vendor systems to communicate without proprietary lock-in. SGIP made OpenFMB code publicly available; NREL maintains documentation. Essential for any community building a multi-vendor system and expecting long-term maintainability.

**OpenADR 3.0**: Open Automated Demand Response standard for coordinating DERs and flexible loads with the utility grid. RESTful API + JSON structure (simpler to implement than OpenADR 2.0b). OpenLEADR-rs is an open-source Rust implementation (Linux Energy Foundation, launched October 2024). Relevant for Zone 5 communities seeking to participate in utility demand response programs for revenue while maintaining islanding capability. [OpenADR Alliance; Lawrence Berkeley Lab CalFlexHub, 2024]

### DIY Arduino/Raspberry Pi: What Is Realistic

Academic research has demonstrated Arduino-based islanded microgrid controllers: PV-driven smart microgrid using two Arduino Uno boards + photoresistor + relays, total cost ~$100 in research settings. A Raspberry Pi 4 provides sufficient computing power for HOMER-derived dispatch logic in a 50 kW community system.

**What is realistic for a 50–500-person community**:
- A Raspberry Pi or similar SBC can serve as the EMS controller for a community microgrid under 100 kW with appropriate industrial I/O shields (ADC inputs for current sensing, GPIO relay outputs for load shedding)
- Total EMS hardware cost: $500–$2,000 for a DIY controller vs. $15,000–$50,000 for commercial EMS
- Key constraint: **certification and liability**. A DIY controller on a utility-interconnected microgrid may not meet IEEE 1547 Type Testing requirements. Use commercial-grade inverters with certified protection relays; the DIY component should be the energy management dispatch logic, not the safety-critical protection relays
- Recommended DIY stack: Raspberry Pi 4 (EMS) + Victron Cerbo GX (communications hub, $500) + OpenFMB-compatible inverters (SMA or Victron) + commercial transfer switch. Total EMS cost: $2,000–$5,000 rather than $15,000–$50,000

**GitHub projects with direct applicability**:
- OpenVFD (github.com/carneeki/OpenVFD): Variable Frequency Drive for ATmega328 Arduinos — useful for small pump/motor control in a community microgrid
- pymgrid: virtual environment for testing dispatch algorithms before deployment
- PandaPower: power flow verification during design

### Commercial Turn-Key Options

**BoxPower (boxpower.io)**: Modular, rapidly deployable microgrid-in-a-box systems for remote locations. Solar + battery + remote monitoring software. Deployed in Alaska remote communities. Commission time: under 12 months vs. industry average 18–36 months. Scale: 10 kW–500 kW. Pricing: not public; comparable to standard installed microgrid costs.

**Scale Microgrids — Rapid Response Modular Microgrid (R2M2)**: Standardized product design, integrated and tested before deployment. Commission time: under 12 months. Relevant for Zone 5 communities that want vendor-managed installation rather than self-managed engineering.

**Enchanted Rock**: Natural gas-powered microgrid specialist for hospitals and critical facilities. Managed services model. Less applicable for communities seeking renewable-primary microgrids.

**muGrid Analytics (mugrid.com)**: Technical consulting firm that designed Bayfield County's microgrid system. Published case studies and direct Zone 5 experience. The most directly relevant engineering firm for Zone 5 community microgrid development.

---

## Section 7: Cross-Domain Integration

### Connection to Phase 5 Wave 1: Individual and Household Scale

Phase 5 Wave 1 documents (Tier 1 individual and Tier 2 household) establish the household-scale energy baseline that community microgrids extend and amplify:

**Household layer** (Phase 5 Wave 1 Tier 2): 40–50 homes, each with 5 kW solar + 10–20 kWh battery = 200–250 kW distributed generation capacity. Individual homes operate autonomously for 1–2 days during outages.

**Community layer** (this domain): Central 80–100 kW solar + 20 kW wind + 400 kWh battery + 40 kW generator = community critical infrastructure protected for 5+ days.

**Combined layered resilience**: During a 120-hour outage, households manage their own needs for the first 24–48 hours using individual systems, while the community microgrid continuously maintains water, heat, medical, and communications infrastructure. By day 3, when individual batteries are depleted, community members gather at community-powered facilities. This is the layered resilience architecture that makes the combination far more robust than either layer alone.

**Critical technical bridge**: Standard grid-tied inverters (grid-following) shut down during grid outages. For household solar to contribute to the community microgrid, homes need either (a) dedicated off-grid inverters with manual transfer switches, or (b) smart GFM-capable inverters (Enphase IQ8, SMA Sunny Boy Storage) that can synchronize to the community microgrid bus. Plan for GFM-compatible inverters at the household level from initial Phase 2 (household) installation — retrofitting later costs $800–$2,000 per home.

### Connection to Phase 4: Agriculture and Food Systems

The agricultural domain (Phase 4 intensification, seedwarden) is both a challenge and an asset for community microgrids:

**Agricultural loads as microgrid stressors**: Irrigation pumps (5–50 kW), grain dryers (50–200 kW), dairy cooling (10–40 kW), and milking equipment are large, variable loads that can destabilize a small microgrid if they cycle on/off without coordination. A 100 kW grain dryer starting without forewarning can cause a 20–40 Hz/second frequency drop in a 500 kW islanded microgrid — enough to trigger inverter protection trips if not anticipated.

**Agricultural loads as dispatchable flexibility**: These same loads can be shifted in time to follow renewable generation availability. A grain dryer that runs when wind generation is high and pauses when batteries are low is a "virtual generator" that stores renewable energy as dried grain. A cold storage facility that pre-chills during solar peaks is a thermal battery. Grain drying load flexibility alone can reduce required battery storage by 20–30% in a Zone 5 farm-based community microgrid. [AgriTech Tomorrow, 2025]

**Seedwarden integration**: Cold storage facilities protecting seeds and food should be designed with thermal mass (insulation + thermal flywheel capacity) allowing 6–12 hours of operation without active cooling. This enables them to coast through grid-down periods without draining the community microgrid. Target thermal mass: 0.5–1 kWh of thermal capacity per kWh of refrigeration load — achievable with phase-change material panels or water thermal mass within the storage enclosure.

**Biogas circular economy**: Dairy or hog farm waste streams → anaerobic digestion → biogas → generator fuel → electricity. Digester heat from generator waste heat keeps the digester at optimal temperature (35–38°C). This closed-loop system can provide continuous on-site power (15–50 kW) for combined farm + adjacent community use. The economics work at 50+ animal units.

### Connection to Water Systems and Communications (Wave 2 Domains)

**Water systems**: Rural water supply in Zone 5 relies almost entirely on electric submersible pumps. A grid outage without microgrid backup means no running water within 6–12 hours for communities on well systems. Water pumping should be classified Tier 1 (never shed) in every Zone 5 community microgrid load-shedding protocol. Design the microgrid specifically to maintain 5–15 kW of water pump power continuously.

**Communications**: Cell tower backup power (typically 4–8 hours of batteries) runs out within the first day of a grid outage. For a Zone 5 community with its own microgrid, providing a dedicated 1–3 kW power circuit to the nearest cell tower backhaul or community mesh radio node is high-leverage for emergency coordination. This may require a separate metered connection or a formal agreement with the cell carrier.

---

## Risk Assessment: What Limits Microgrid Viability

**High probability, manageable risks**:
- Interconnection timeline slippage (mitigate: start utility interconnection application first, 12+ months before target operational date)
- Generator fuel supply disruption in extended winter outage (mitigate: 90+ day on-site fuel storage; biogas complement for Zone 5 farm communities)
- Battery cell degradation (mitigate: specify LFP with 10-year warranty; budget for cell replacement at year 8–12)
- Operator training gap (mitigate: annual black-start drill; laminated quick-reference procedures at each site)

**Lower probability, higher consequence risks**:
- Utility standby charge increases (monitor state PUC proceedings; support Citizens Utility Board advocacy in Illinois)
- Federal grant program instability (the tribal experience in 2025 — funding loss under Trump administration — is a warning; do not begin construction without funding committed and contracts signed)
- FERC Order 2222 implementation delay (do not rely on wholesale market revenue in project pro formas until MISO compliance is operationalized; treat as upside, not baseline)
- Geomagnetic storm destroying grid transformers (low probability; months-long recovery time; pre-position at least one spare distribution transformer for critical-path facilities)

**Structural constraints**:
- Illinois net metering change (January 2025) reduces revenue from grid-connected operation, extending payback periods. Cooperative ownership models (where communities own generation and consume it collectively) are more resilient to net metering reductions than prosumer-export models.
- Capital cost remains the primary barrier for the smallest communities (50 people). At $2,000–$4,000 per capita before grants and $500–$1,500 after grants, a 50-person community needs $25,000–$75,000 net capital — manageable through community bond or cooperative membership fee structures.

---

## Implementation Pathway: 50-Person to 500-Person Community

**Phase 1 — Assessment (Months 1–4)**
- Baseline energy audit: document all loads (kW demand, annual kWh, seasonal pattern)
- Map critical facilities: which 3–5 buildings must have power during 120-hour outage?
- Run PVWatts for your GPS coordinates; import into HOMER Energy for preliminary sizing
- Contact USDA Rural Development Energy Coordinator (state office) for REAP status
- Contact utility interconnection department for pre-application meeting
- Deliverable: feasibility report with sizing recommendation, preliminary cost estimate, applicable grants

**Phase 2 — Funding and Permitting (Months 4–14)**
- Submit REAP grant application (when open; up to $1M)
- Apply to DOE C-MAP if eligible (rural, underserved, tribal community)
- File utility interconnection application (start early — 4–12 months)
- Engage state rebate programs (Illinois ComEd/Ameren DG rebates, Michigan MPSC, Wisconsin Focus on Energy)
- Explore cooperative bond, rural development loan, or municipal bond for remaining capital
- Hire engineer for one-line diagrams, protection coordination study, permits

**Phase 3 — Installation and Commissioning (Months 12–24)**
- Procure equipment: 6–12 week lead times for inverters and batteries; order early
- Install solar arrays, battery enclosures, wind turbines if applicable
- Install microgrid controller (commercial or DIY Raspberry Pi + OpenFMB), transfer switches, protection relays
- Commission: tune inverter droop settings, test load-shedding sequences, perform intentional islanding test
- Train operators: black start procedure, load-shedding override, safety protocols, annual drill schedule

**Phase 4 — Scaling (Year 3+)**
- Add second microgrid sites (school, agricultural cooperative) and link via OpenFMB peer-to-peer
- Evaluate iron-air storage retrofit (Form Energy 2028+ community scale)
- Monitor reliability metrics: outage events prevented, percentage of critical load served
- Submit lessons learned to EESI, NRECA, DOE C-MAP for national knowledge base

---

## Sources (50+ Citations)

### Architecture and Technical Standards
1. [IEEE 1547-2018 Islanding Requirements — NREL](https://www.nrel.gov/grid/ieee-standard-1547/)
2. [IEEE 2030.9-2019 Microgrid Controller Recommended Practices — IEEE Xplore](https://ieeexplore.ieee.org/document/8675485)
3. [IEEE 2030.10-2021 DC Microgrids for Rural Applications — IEEE Xplore](https://ieeexplore.ieee.org/document/9646866)
4. [Stability Analysis with High Renewable Penetration — NREL fy25osti/96530](https://docs.nrel.gov/docs/fy25osti/96530.pdf)
5. [Grid-Forming Control for IBR Systems — IET Renewable Power Generation 2024](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/rpg2.12991)
6. [Stability of Power Systems with High IBR Penetration — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0038092X20305442)
7. [Droop Control in Islanded Microgrids — IET RPG 2025](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/rpg2.13186)
8. [Virtual Synchronous Machine Control — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0378779620307744)
9. [NREL Microgrid Voices of Experience — NREL fy21osti/75909](https://docs.nrel.gov/docs/fy21osti/75909.pdf)
10. [Grid-Aware Islanding and Resynchronisation — arXiv 2025](https://arxiv.org/pdf/2503.04597)
11. [Stability Analysis with High Renewable Penetration — MDPI Electronics 2024](https://www.mdpi.com/2079-9292/14/24/4871)
12. [DC Microgrid for Rural Electrification — IEEE Xplore](https://ieeexplore.ieee.org/document/7104427)

### LiFePO4 and Battery Storage
13. [LiFePO4 Thermal Management — Anern Store](https://www.anernstore.com/blogs/diy-solar-guides/lifepo4-battery-thermal-management)
14. [LiFePO4 BMS Parameters 2025 — Docan Power](https://www.docanpower.com/Read%20the%20latest%20blogs%20and%20customer%20feedbacks%20from%20Docan%20Power/lifepo4-battery-bms-25-key-parameters-for-smart-management-in-2025)
15. [LiFePO4 Battery Solar Guide 2025 — SolarTechOnline](https://solartechonline.com/blog/lithium-iron-phosphate-battery-solar-guide/)
16. [NREL Battery Storage Cost Projections 2025 — fy25osti/93281](https://docs.nrel.gov/docs/fy25osti/93281.pdf)
17. [Form Energy Iron-Air Battery Expansion 2026 — DiscoveryAlert](https://discoveryalert.com.au/form-energy-iron-air-battery-expansion-economics-2026/)
18. [Minnesota PUC Xcel/Form Energy Iron-Air Approval — Utility Dive](https://www.utilitydive.com/news/minnesota-puc-xcel-form-energy-battery-sherco-solar/685460/)
19. [Cost of Battery Storage per kWh 2026 — VIP Energy](https://vipenergyservice.com/energy-storage/cost-of-battery-storage-per-kwh/)

### Community Deployment and Federal Programs
20. [DOE C-MAP Community Microgrid Assistance Partnership](https://www.energy.gov/oe/community-microgrid-assistance-partnership)
21. [DOE C-MAP Launch Announcement](https://www.energy.gov/oe/articles/us-department-energy-launches-community-microgrid-assistance-partnership)
22. [NRECA CARED $45M DOE Award](https://www.electric.coop/co-op-consortium-selected-for-45m-in-doe-funding-for-rural-microgrids)
23. [EESI Microgrids in Rural Areas](https://www.eesi.org/articles/view/microgrids-and-energy-improvements-in-rural-areas)
24. [Clean Coalition Community Microgrid Initiative](https://clean-coalition.org/community-microgrid-initiative/)
25. [USDA REAP Program](https://www.rd.usda.gov/programs-services/energy-programs/rural-energy-america-program-renewable-energy-systems-energy-efficiency-improvement-guaranteed-loans)
26. [FERC Order 2222 DER Aggregation Explainer](https://www.ferc.gov/ferc-order-no-2222-explainer-facilitating-participation-electricity-markets-distributed-energy)
27. [FERC 2026 Outlook — Morgan Lewis](https://www.morganlewis.com/pubs/2026/03/federal-regulatory-outlook-for-electric-storage-qfs-and-inverter-based-resources)

### Bayfield County and Zone 5 Case Studies
28. [Bayfield County Microgrid — WPR](https://www.wpr.org/economy/bayfield-county-microgrid-extreme-weather-power-xcel-energy)
29. [Bayfield County — muGrid Analytics](https://www.mugrid.com/projects/bayfield)
30. [Bayfield County — RENEW Wisconsin Honor Roll](https://www.altenergymag.com/news/2024/03/20/bayfield-countys-microgrid-projects-honored-in-renew-wisconsins-2023-clean-energy-honor-roll/41625/)
31. [Bronzeville Microgrid Chicago — Adaptation Clearinghouse](https://www.adaptationclearinghouse.org/resources/bronzeville-microgrid-chicago-illinois.html)
32. [ComEd Bronzeville Islanding Test — T&D World](https://www.tdworld.com/distributed-energy-resources/article/20972898/comed-simulates-islanding-with-its-bronzeville-community-microgrid)

### Military and Campus Microgrids
33. [Fort Bliss Microgrid Case Study — Microgrid Knowledge](https://www.microgridknowledge.com/home/article/11433395/military-microgrid-fort-bliss-case-study)
34. [Army Microgrid Development — Army.mil](https://www.army.mil/article/255597/developing_microgrids_to_deliver_energy_resilience)
35. [PNNL Microgrid Handbook for Army Resilience — PNNL-38494](https://www.pnnl.gov/main/publications/external/technical_reports/PNNL-38494.pdf)
36. [UC San Diego Microgrid — SEL](https://selinc.com/highlights/ucsd-microgrid/)
37. [UC San Diego Microgrid Reliability — Microgrid Knowledge](https://microgridknowledge.com/research-heavy-uc-san-diego-counts-microgrid-reliability/)

### Puerto Rico and Island Cases
38. [IREC Castaner Microgrid — Hurricane Fiona](https://irecusa.org/blog/local-energy-climate-solutions/solar-microgrid-keeps-the-lights-on-in-castaner-puerto-rico-during-hurricane-fiona/)
39. [Cornell/Vieques Microgrid Resilience — Cornell Chronicle 2026](https://news.cornell.edu/stories/2026/04/storm-ravaged-vieques-microgrid-builds-resilience)
40. [ORNL Puerto Rico Microgrid Orchestrator](https://www.ornl.gov/news/researchers-bring-more-reliable-electricity-puerto-rican-microgrids)
41. [DOE Puerto Rico $325M Grid Funding 2024](https://www.energy.gov/gdo/puerto-rico-grid-recovery-and-modernization)
42. [Hawaiian Electric Microgrid Services Tariff](https://www.hawaiianelectric.com/about-us/our-vision-and-commitment/resilience/microgrid-services-tariff)
43. [Moloka'i Nanogrids — Microgrid Knowledge](https://www.microgridknowledge.com/remote-microgrids/article/55236523/momentum-for-molokai-micro-power-rural-hawaiian-island-seeks-15-nanogrids)

### Tribal Microgrids
44. [Pine Ridge Plug-in Solar — North American Clean Energy](https://www.nacleanenergy.com/solar/a-tribal-led-breakthrough-plug-in-solar-on-the-pine-ridge-reservation)
45. [Navajo Nation Solar — USDA $100M Announcement](https://www.kjzz.org/tribal-natural-resources/2025-01-20/usda-announces-100-million-solar-power-investment-for-navajo-tribal-utility-authority)
46. [Tribal Energy Sovereignty — Stanford & the West 2025](https://andthewest.stanford.edu/2025/for-tribal-governments-can-energy-sovereignty-and-economic-self-sufficiency-go-hand-in-hand/)
47. [Tribal Nations Federal Funding Loss 2025 — Utility Dive](https://www.utilitydive.com/news/tribal-nations-federal-funding-solar-energy-trump/807890/)
48. [Scale Microgrids Tribal Lands Resource](https://www.scalemicrogrids.com/blog/americas-energy-transition-must-include-tribal-lands)

### Midwest Regulatory Policy
49. [Illinois Net Metering Post-2025 — Citizens Utility Board](https://www.citizensutilityboard.org/illinois-net-metering-post-2025/)
50. [Illinois Solar Incentives 2026 — EnergySage](https://www.energysage.com/local-data/solar-rebates-incentives/il/)
51. [Michigan Microgrid Bill — Canary Media](https://www.canarymedia.com/articles/enn/michigan-lawmakers-propose-microgrid-bill-to-boost-resilience)
52. [Michigan BESS Planning Guide — Graham Institute U-Michigan](https://graham.umich.edu/project/bess-guide)
53. [Wisconsin Solar and Storage — SEIA](https://seia.org/state-solar-policy/wisconsin-solar/)
54. [Net Metering by State 2026 — The Green Watt](https://www.thegreenwatt.com/net-metering-by-state/)

### Open-Source Tools, Biogas, and Distributed Generation
55. [HOMER Energy — homerenergy.com](https://homerenergy.com/)
56. [PVWatts NREL](https://pvwatts.nrel.gov/)
57. [OpenFMB for DER Management — SEPA](https://sepapower.org/knowledge/green-ovations-open-source-smarts-openfmb-supports-der-management/)
58. [OpenADR 3.0 — Lawrence Berkeley Lab CalFlexHub 2024](https://calflexhub.lbl.gov/wp-content/uploads/sites/41/2024/08/Transforming-demand-response-using-OpenADR-3.0.pdf)
59. [OpenLEADR-rs Open-Source OpenADR 3.0 — OpenADR Alliance](https://www.openadr.org/)
60. [BoxPower Modular Microgrids](https://boxpower.io/)
61. [Wisconsin Biogas Microgrid — Microgrid Knowledge](https://www.microgridknowledge.com/distributed-energy/article/11427521/microgrid-powered-facility-in-wisconsin-produces-renewable-natural-gas-for-california/)
62. [Iowa Dairy Biogas Digesters — Investigate Midwest 2024](https://investigatemidwest.org/2024/11/04/iowa-dairies-with-biogas-digesters-are-growing-their-herds-which-concerns-water-quality-advocates/)
63. [ATTRA Mid-Scale Biodigester On-Farm Energy](https://attra.ncat.org/a-mid-scale-anaerobic-biodigester-creates-on-farm-renewable-energy/)
64. [Agricultural Microgrids 2025 — AgriTech Tomorrow](https://www.agritechtomorrow.com/story/2025/07/enhance-farm-resilience-with-agricultural-microgrids/16782/)
65. [Iowa Wind and Solar — Iowa State AgPolicy Review](https://agpolicyreview.card.iastate.edu/winter-2022/utility-scale-wind-and-solar-development-iowa-trends-prospects-and-land-factor)

---

*Cross-reference: `/projects/systems-resilience/PHASE_5_WAVE_2_MICROGRIDS_RESEARCH.md` (companion document, 6,000 words — deeper treatment of islanding protocols, Zone 5 seasonal modeling, implementation timeline, and organizational contacts).*

*This document last updated: 2026-05-26. Decision gate: May 31–June 1 Phase 5 Wave 2 execution order.*
