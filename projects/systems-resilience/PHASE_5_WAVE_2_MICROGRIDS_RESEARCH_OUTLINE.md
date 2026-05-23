---
title: Phase 5 Wave 2 — Microgrids & Distributed Energy Research Outline
project: systems-resilience
scope: Distributed microgrids and community-scale renewable energy systems for Zone 5 (Midwest)
status: OUTLINE (research execution scheduled for May 22 20:30+ UTC)
target_completion: May 23 02:00 UTC (4–6 hours)
deliverable: PHASE_5_WAVE_2_MICROGRIDS_RESEARCH.md (4,000+ words, 50+ sources)
---

# Phase 5 Wave 2: Microgrids & Distributed Energy Research Outline

## Research Objectives

1. **Architecture Variations**: Understand different microgrid designs (AC/DC, control systems, islanding)
2. **Regulatory Landscape**: Map community solar + battery storage regulations as of May 2026
3. **DIY/Open-Source Projects**: Identify peer-reviewed case studies and reproducible designs
4. **Zone 5 Integration**: Midwest-specific climate, agricultural integration, supply chains
5. **Grid-Outage Resilience**: Design patterns for 120+ hour sustained loss, cascading failures

## Research Areas (by section)

### Section 1: Microgrid Architecture Fundamentals (800 words)
- **AC microgrids**: Standard (120/240V), advantages (existing infrastructure), disadvantages (large inverters required)
- **DC microgrids**: Solar-native (DC output), advantages (reduced conversion losses), disadvantages (fewer off-the-shelf components)
- **Hybrid AC/DC**: Emerging standard, solves for residential solar + battery + loads
- **Control architectures**: 
  - Centralized (single controller, vulnerable single point of failure)
  - Decentralized/peer-to-peer (each asset negotiates with neighbors, resilient, complex)
  - Tiered (local clusters → regional → grid-connected)
- **Islanding protocols**: How microgrids detect grid failure and disconnect safely
  - Synchronous islanding (instantaneous)
  - Asynchronous islanding (planned, communication-based)
  - Unintentional islanding (dangerous, must prevent)
- **Key technical standards**: IEEE 1547 (interconnection), IEC 61850 (microgrid communications), CIGRE (architecture frameworks)

**Research sources to identify**:
- NREL microgrid architectures (3–4 papers)
- IEEE Microgrid Standards Committee publications
- Real-world case studies (Orkney Islands UK, Hawaii, Calif. remote communities)

### Section 2: Community Solar + Battery Storage Regulatory Landscape (May 2026) (1,200 words)
- **Community solar status** (May 2026 snapshot):
  - States with net metering: 42 (as of 2024, check for changes)
  - Community solar programs: 29 states (aggregate capacity ~4 GW)
  - Regulatory drivers: state clean energy mandates, utility interconnection standards, tax incentives (IRA Section 48 / 45 passed 2022)
- **Federal policy** (as of May 2026):
  - IRA tax credits for residential solar (30% through 2032, declining to 26% by 2034)
  - Standalone battery storage tax credit (30% through 2032) — major change May 2024
  - Energy Storage Grand Challenge (ESGC) goals and timelines
  - Inflation Reduction Act funding for community energy projects
- **State regulatory variations**:
  - Net metering models: full retail rate vs. avoided-cost vs. hybrid (map variations by state)
  - Community solar ownership: utility-led vs. third-party vs. municipal vs. nonprofit
  - Distributed battery storage: interconnection timelines, charge/discharge protocols
  - Midwest-specific (Zone 5): Illinois, Wisconsin, Michigan, Minnesota, Missouri rules
- **Utility resistance**: How utilities are fighting distributed energy and community solar (legal tactics, regulatory capture)
- **Emerging regulations**: AI-driven demand response, vehicle-to-grid (V2G), microgrids as "virtual power plants"

**Research sources to identify**:
- NCCETC state-by-state policy tracker
- IRENA community energy reports
- Midwest Energy Efficiency Alliance (MEEA) state benchmarks
- Individual state PUC decisions (Illinois, Wisconsin, Michigan, Minnesota)
- Utility regulatory filings (ComEd, Xcel, DTE, Consumers Energy)

### Section 3: DIY & Open-Source Microgrid Projects (1,000 words)
- **Academic case studies**:
  - UC San Diego microgrid (naval base, DC + battery hybrid)
  - Colorado State University remote microgrid
  - University of Illinois Urbana-Champaign distributed systems lab
  - ETH Zurich off-grid + resilience research
- **Community-led projects** (peer-reviewed / documented):
  - Orkney Islands (Scotland) multi-island microgrids
  - Remote community solar + battery projects (Alaska, Hawaii, Appalachia)
  - Agricultural microgrid projects (dairy farms, crop irrigation powered by distributed solar)
- **Open-source software stacks**:
  - OpenFMB (Open Field Message Bus) — NREL-backed grid communications standard
  - PandaPower (Python power flow analysis)
  - MATPOWER (MATLAB microgrid modeling)
  - CoolProp (thermodynamic modeling for thermal storage)
- **Open-source hardware**:
  - Arduino/Raspberry Pi-based inverter controllers
  - Open Inverter Project (automotive EV inverter adapted for solar)
  - DIY battery management systems (Orion, JBD BMS open-source variants)
- **Cost benchmarks**:
  - Small community microgrid (100–500 kW): $2–4M capital (2024 pricing, check for inflation)
  - Solar + battery per kWh (DC side): $150–250/kWh (residential), $80–150/kWh (utility-scale)
  - Inverter + controller: $0.50–$1.00/W (microinverters) to $0.05–$0.15/W (string inverters)

**Research sources to identify**:
- NREL Open Microgrids Initiative
- IEEE Xplore microgrid case studies
- ResearchGate / Scholar profiles of microgrid researchers
- GitHub open-source projects (PandaPower, OpenFMB examples)

### Section 4: Zone 5 (Midwest) Integration & Climate Considerations (1,200 words)
- **Climate & weather patterns**:
  - Solar capacity factor (May 2026 baseline): Illinois ~13%, Wisconsin ~12.5%, Michigan ~11%, Minnesota ~12.5%, Missouri ~13.5%
  - Wind capacity factor: Illinois ~35%, Minnesota ~40%, Michigan ~28%, Wisconsin ~32%, Missouri ~28%
  - Seasonal mismatch (summer peak solar, winter peak heating demand + lower solar)
  - Extreme weather: winter ice storms (grid outage risk), summer thunderstorms (inverter shutdown risk), drought (thermal cooling for generators/batteries)
- **Agricultural integration**:
  - Dairy farms: high daytime electrical loads (milking, cooling, feed prep), potential for solar + battery + biogas
  - Crop irrigation: seasonal demand (May–August), solar + grid hybrid designs
  - Cold storage facilities: winter heating efficiency + summer cooling load, thermal batteries (phase-change materials, ice storage)
  - Crop drying equipment: on-farm propane heating → solar thermal + thermal battery potential
- **Infrastructure peculiarities**:
  - Rural electric co-ops (not investor-owned utilities): more receptive to distributed energy, but less IT infrastructure
  - Aging distribution lines (many rural areas): voltage stability concerns with high solar penetration
  - Limited natural gas availability in some counties: electric heating/cooling = larger battery demands
  - Seasonal migration patterns (summer cabins, winter migration): demand swings
- **Supply chain geography**:
  - Manufacturing nearness: most solar panels imported (China), inverters globally distributed, batteries (Minnesota has Essense Energy, Wisconsin has Oshkosh EV battery)
  - Service radius (technician availability): rural technician shortage
  - Parts availability in winter: logistics challenges for battery/inverter replacement during outage season
- **Economic drivers**:
  - Crop insurance + grid resilience: bundled value propositions (harvest security + grid income)
  - Carbon capture credits: biochar from crop residues → carbon credits (blockchain verification emerging)
  - Midwest manufacturing renaissance: incentive programs for distributed energy manufacturing (state/federal)

**Research sources to identify**:
- USDA Rural Utilities Service (RUS) renewable energy programs
- State energy office databases (Illinois, Wisconsin, Michigan, Minnesota, Missouri)
- University of Wisconsin-Madison Agricultural Engineering department (microgrid research)
- Iowa State University renewable energy integration labs
- Midwest Energy News / Great Plains Gazette coverage of farm energy projects

### Section 5: Grid-Outage Resilience & Cascading Failure Scenarios (1,200 words)
- **Grid failure modes**:
  - Geomagnetic storm (solar event): widespread blackout, recovery time 3–12 months if transformers destroyed
  - Wildfire + transmission line damage (Midwest less vulnerable than West, but increasing frequency)
  - Winter ice storm (Midwest-specific): lines down 48–120+ hours in affected areas
  - Cyber attack on SCADA systems: intentional outage, recovery 24–48 hours
  - Cascading failure (brownout → overload → shutdown → outage): rapid progression
- **Microgrids as resilience anchors** (120+ hour sustained outage scenarios):
  - Hospital/clinic microgrids: maintain basic power (OR, ICU, pharmacy)
  - Water pumping & treatment: rural areas dependent on electric pumps (outage = water unavailable)
  - Food cold chain: refrigeration failure, spoilage risk
  - Heating (winter) & cooling (summer): life-safety critical
  - Communications: cell towers, internet backhaul (most require battery backup, but battery capacity limited)
- **Microgrid operation during outage**:
  - Instant load shedding (disconnect non-critical loads within milliseconds)
  - Frequency stabilization (without grid reference, islanded microgrids must self-stabilize)
  - Voltage control (inverters must provide voltage support without grid synch signal)
  - Demand flexibility (dynamic load shifting when renewable generation fluctuates)
- **Cascading failure prevention**:
  - Intentional microgrid formation (automated detection of grid failure, negotiation to island)
  - Black start capability (microgrids must be able to restart without external power)
  - Storage sizing (rule of thumb: 4–6 hours local load × 2–3 redundancy factor for Midwest winter scenario)
  - Supply chain resilience (spare parts cached locally, technician training programs)
- **Multi-microgrid coordination** during extended outage:
  - Mesh networking between islanded microgrids (sharing excess generation, load balancing)
  - Priority load determination (who gets power first: hospital? water? heating? food?)
  - Negotiation protocols (P2P or centralized? fair allocation algorithms?)
- **Case studies of grid-outage resilience**:
  - 2021 Texas freeze (rolling blackouts, inadequate storage/heating)
  - 2003 Northeast blackout (cascading failure analysis)
  - Puerto Rico Hurricane Maria (slow recovery, microgrids emerged as recovery tool)

**Research sources to identify**:
- EPRI (Electric Power Research Institute) cascading failure studies
- NREL islanding and microgrid resilience research
- Argonne National Laboratory grid resilience modeling
- NERC (North American Electric Reliability Corporation) standards for microgrids
- DOD/DoE Energy Resilience research (military bases pioneering microgrid integration)

---

## Research Execution Plan

**Start time**: May 22 20:30 UTC (after checkpoint outcome logged)
**Target completion**: May 23 02:00 UTC (4–6 hours)

### Hour 1: Sections 1–2 (Architecture + Regulatory)
- Web search for recent (2024–2026) NREL microgrid reports
- State regulatory tracker compilation (5 Midwest states)
- IRA Section 48/45 tax credit current status (May 2026)

### Hour 2: Section 3 (DIY & Open-Source)
- GitHub open-source project audit (code maturity, documentation)
- IEEE Xplore case study compilation
- Cost benchmarks from 2024 NREL solar/battery market reports

### Hour 3: Section 4 (Zone 5 Integration)
- USDA RUS database searches (recent Midwest projects)
- State energy office websites (Illinois, Wisconsin, Michigan, Minnesota, Missouri)
- Agricultural engineering research (farm microgrid case studies)

### Hour 4: Section 5 (Grid-Outage Resilience)
- NREL resilience research summary
- EPRI cascading failure models
- Puerto Rico Hurricane Maria recovery analysis (lessons learned)

### Hour 5: Synthesis & Writing
- Draft executive summary (300 words)
- Integrate sources across all sections
- Create cross-references to Phase 5 Wave 1 content (individual-scale systems)

### Hour 6: Finalization & Review
- Verify 4,000+ word count and 50+ source citations
- Check Midwest-specific data accuracy
- Commit to master with WORKLOG update

---

## Sources to Compile (Initial List)

### Regulatory & Policy
- [ ] NREL Community Energy Handbook 2026 (updated from 2023)
- [ ] IRA Renewable Energy & Storage Tax Credit Summary (Treasury Department)
- [ ] FERC Order 2222 (virtual power plants & aggregation) implementation status
- [ ] Illinois PUC Docket on community solar
- [ ] Wisconsin Focus on Energy program outcomes

### Technical & Architectural
- [ ] NREL OpenMG (Open Modeling Guidelines) for Microgrids
- [ ] IEEE 1547-2018 & IEEE 2030.9-2019 (interconnection + microgrid standards)
- [ ] NREL Microgrid Modeling Toolbox documentation

### Case Studies & Projects
- [ ] NREL Aliso Viejo Microgrid (peer-reviewed case study)
- [ ] UC San Diego Microgrid (architecture + lessons learned)
- [ ] Orkney Islands microgrids (European resilience model)

### Climate & Midwest-Specific
- [ ] NOAA Climate Normals (Zone 5 weather patterns)
- [ ] NREL Solar Radiation Database for Midwest
- [ ] USDA NRCS Renewable Energy Programs in Midwest

### Grid Resilience
- [ ] EPRI Cascading Blackout Prevention (technical report)
- [ ] Argonne National Lab Grid Resilience Index
- [ ] NERC BPS Reliability Standards (balancing authority coordination)

### Open-Source & DIY
- [ ] PandaPower GitHub (power flow modeling)
- [ ] OpenFMB NREL documentation
- [ ] Renewable Energy World magazine (DIY project profiles)

---

## Estimated Output Structure

```
PHASE_5_WAVE_2_MICROGRIDS_RESEARCH.md

1. Executive Summary (300 words)
2. Introduction (400 words) — why microgrids matter for Phase 5 resilience
3. Section 1: Architecture Fundamentals (800 words + diagrams)
4. Section 2: Regulatory Landscape May 2026 (1,200 words + state-by-state table)
5. Section 3: DIY & Open-Source Projects (1,000 words + project matrix)
6. Section 4: Zone 5 Integration (1,200 words + climate data table)
7. Section 5: Grid-Outage Resilience & Cascading Failures (1,200 words + scenario matrices)
8. Cross-Domain Bridges (400 words) — how this integrates with Phase 5 Wave 1
9. Key Recommendations (400 words) — highest-leverage microgrid designs for Midwest
10. Sources (50+ citations, alphabetized by author)

Total: 4,000–4,500 words, highly sourced, production-ready for Phase 5 Wave 2 decision gate.
```

---

## Parallel Execution with Item 35a

This research (Item 35c) has **NO DEPENDENCIES** on checkpoint outcome. Execution timeline:
- **20:30 UTC** (May 22): Begin research in parallel with Item 35a finalization
- **02:00 UTC** (May 23): Complete and commit to master
- **Post-May 23**: Feeds into Phase 5 decision gate for user review (expected June 1)

No blocking on Items 35b or checkpoint outcome. Ready to execute now.

