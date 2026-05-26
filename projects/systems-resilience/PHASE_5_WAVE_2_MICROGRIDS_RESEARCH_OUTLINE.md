---
title: "Phase 5 Wave 2 — Microgrids & Community Energy: Deep Research Outline"
project: systems-resilience
phase: 5
wave: 2
status: production
created: 2026-05-26
word_count: ~5200
source_count: 48
decision_gate: "June 1, 2026 — Phase 5 microgrid implementation decision"
audience: "Community infrastructure planners, Zone 5 Midwest (IL, MI, IA, IN, WI)"
cross_references:
  - PHASE_5_WAVE_2_MICROGRIDS_RESEARCH.md
  - MICROGRID_ARCHITECTURE_DECISION_MATRIX.md
  - PHASE_5_WAVE_2_MICROGRIDS_IMPLEMENTATION_SKETCH.md
  - PHASE_4_FRAMEWORK.md
  - projects/off-grid-living
  - projects/seedwarden
---

# Phase 5 Wave 2: Microgrids & Community Energy — Deep Research Outline

> **Scope**: Zone 5 Midwest (IL, MI, IA, IN, WI) — communities of 50–500 people  
> **Resilience target**: 72–120 hour (3–5 day) grid-down scenarios  
> **Companion documents**: `PHASE_5_WAVE_2_MICROGRIDS_RESEARCH.md` (6,000-word base),  
> `MICROGRID_ARCHITECTURE_DECISION_MATRIX.md`, `PHASE_5_WAVE_2_MICROGRIDS_IMPLEMENTATION_SKETCH.md`

---

## Most Important Finding

The leading finding from this research cycle is that the **technical barriers to community-scale microgrids are largely solved; the bottlenecks are regulatory, financial, and organizational**. The IEEE 1547-2018 / UL 1741 SB standards framework is mature. Hybrid AC/DC architecture with LiFePO4 storage is validated at scale in Zone 5 (Bayfield County, Wisconsin). The open-source toolchain — HOMER Energy, GridLAB-D, OpenDSS, PandaPower/VeraGrid, OpenFMB, OpenADR 3.0 — is sufficient for a technically competent community to design, simulate, and operate a professional-grade microgrid without proprietary software lock-in.

What is hard: utility interconnection timelines (3–12 months), financing in a post-ITC expiration environment (December 31, 2025), and MISO Order 2222 DER aggregation (full compliance delayed to 2029–2030). Communities that begin feasibility and interconnection applications in 2026 can achieve operational islanding capability by 2027–2028 — if governance is established first.

**Implication for Phase 4 sequencing**: This confirms the Phase 4 Framework's finding that governance comes before energy infrastructure. A community without an established cooperative or municipal authority cannot sign utility interconnection agreements, apply for grants, or operate a microgrid through personnel turnover. The microgrid decision-making structure must exist before the first engineering study is commissioned.

---

## Section 1: Microgrid Architecture Typologies

### 1.1 AC vs. DC vs. Hybrid — What Actually Matters for Zone 5

**Standard AC (480V/277V three-phase; 120/240V single-phase residential)**

The default architecture for any community with existing grid-tied infrastructure. Three-phase 480V/277V is the standard for commercial and agricultural loads in Zone 5 (motors, grain dryers, dairy cooling systems). Single-phase 120/240V serves residential loads. Advantages: universal equipment compatibility, large installer pool, utility-familiar configuration. Disadvantages: every solar array and battery must convert DC to AC (10–15% conversion loss per stage); pure AC systems require centralized inverters at the point of common coupling, creating a single failure bottleneck.

For Zone 5 communities retaining legacy AC wiring in existing farm buildings, pure AC is often the cost-minimizing path for short-term deployment. The long-term efficiency penalty accumulates to 15–20% of total generation over a 25-year system life.

**DC Microgrids (48V bus: residential/small-scale; 380–400V bus: commercial scale)**

Solar panels and LiFePO4 batteries are natively DC. Eliminating the DC-to-AC conversion stage reduces losses to 3–5% total for DC loads. IEEE 2030.10-2021 was specifically written for DC microgrids in rural and remote electrification applications. Zone 5 fit: low-to-medium. DC at 48V suits new-construction off-grid homesteads and small installations. DC at 380–400V (emerging standard for building-scale DC distribution) is viable for communities willing to rewire, but requires DC-rated breakers (still niche procurement, limited installer training), and is incompatible with most existing agricultural motor loads without DC drives.

**Hybrid AC/DC (Recommended for Zone 5 existing communities)**

A bidirectional DC bus at 48V or 400V collects solar generation and battery storage. An AC bus at 120/240V or 480V/277V serves standard loads. Grid-forming (GFM) inverters bridge the buses and maintain voltage/frequency in island mode without a generator reference. This architecture achieves 5–8% total conversion losses (vs. 15% pure AC), supports mixed existing/new loads, and is validated at the Bayfield County, Wisconsin deployment — the most directly comparable Zone 5 case study.

The critical enabling technology is **grid-forming inverters** (GFM), as distinct from traditional grid-following inverters (GFL). Grid-following inverters synchronize to an external grid reference and shut down when the grid fails. Grid-forming inverters can establish their own voltage and frequency reference, enabling true island operation without a generator running. This distinction is the central technical decision in any microgrid project: only GFM inverters support true islanding. Key GFM-capable products for Zone 5: SMA Sunny Island, Schneider Electric XW+, Victron Quattro (48V DC bus applications), Enphase IQ8 (residential scale, first product certified to UL 1741 3rd edition/SB, December 2025).

### 1.2 Voltage Level Reference

| Application | AC Voltage | Notes |
|---|---|---|
| Residential loads | 120/240V single-phase | Standard US residential |
| Light commercial | 120/208V three-phase | Small commercial buildings |
| Agricultural/commercial | 277/480V three-phase | Motors, grain dryers, dairy equipment |
| Utility distribution | 4 kV – 34.5 kV | Primary distribution; step-down transformers required |
| DC bus (small systems) | 48V DC | Standard for residential battery/solar systems |
| DC bus (commercial) | 380–400V DC | Emerging standard; limited installer pool |

### 1.3 Control Hierarchies

**Centralized control**: Single energy management system (EMS) governs all assets. Appropriate for systems under 100 kW. Failure mode: single controller failure disables entire microgrid — unacceptable for life-safety applications unless controller redundancy is built in.

**Decentralized/droop control**: Each inverter self-regulates based on local frequency and voltage measurements using droop curves. No communication required between inverters. In frequency droop: each inverter reduces output when frequency rises (excess generation) and increases output when frequency falls (deficit). In voltage droop: reactive power sharing maintains voltage balance. This is the preferred architecture for Zone 5 community microgrids because it is resilient against communication failures — a realistic failure mode during the grid-down events the microgrid is designed to survive.

**Tiered control (practical recommendation)**: Local droop control at each inverter, coordinated by a site-level EMS that optimizes dispatch and monitors state of charge, with an optional regional coordinator linking multiple microgrid sites via OpenFMB. This is the architecture used in both the Bayfield County deployment and the NRECA CARED cooperative consortiums.

### 1.4 Inverter Topology Selection

**String inverters** (one inverter per array string, 50 kW – 1 MW range): Lower per-watt cost ($0.05–0.15/W), proven at utility scale, straightforward maintenance. Failure mode: one inverter failure takes down an entire string. Best for larger community arrays (80 kW+) with monitoring to catch failures quickly.

**Central inverters** (one large inverter for the entire array, 250 kW – 1 MW+): Lowest per-watt cost at scale, minimal components. Single point of failure for the entire generation side. Not recommended for community resilience applications without redundant units.

**Microinverters** (one inverter per panel): Per-panel optimization, rapid shutdown compliance, panel-level monitoring. Cost: $0.50–$1.00/W — 5–10x more expensive than string. Best for residential-scale contributions to a community microgrid where partial shading (trees, roof valleys) would penalize string performance, and where panel-level islanding capability (e.g., Enphase IQ8's "sunlight backup" mode) provides household-level resilience before community-scale infrastructure is complete.

For Zone 5 community microgrids at 80–200 kW scale: string inverters for the main array, microinverters on roof-mounted residential contributions.

### 1.5 Islanding Detection Protocols and Anti-Islanding Standards

**Why islanding detection is mandatory**: IEEE 1547-2018 requires that any DER cease energizing the utility grid within 2 seconds of island formation — to protect lineworkers who may be working on de-energized lines that the DER is now energizing from the community side. Unintentional islanding (a DER continuing to energize the grid without the utility's knowledge) is the core safety concern.

**Intentional islanding** (what community microgrids do deliberately) requires explicit design, utility approval, and an interconnection agreement that specifies the islanding protocol. IEEE 1547-2018 Section 8 governs intentional island requirements.

**Passive detection methods** — the microgrid controller monitors grid parameters and detects anomalies:

- **Rate of Change of Frequency (RoCoF / ROCOF)**: Monitors df/dt. When the grid disconnects, generation/load imbalance causes frequency to change rapidly. Threshold: typically ±0.5 Hz/s triggers island detection. IEEE Xplore research (2022) confirms ROCOF is one of the two most studied techniques for GFM inverter islanding detection. Limitation: large microgrids with near-balanced generation/load have small RoCoF, creating a non-detection zone.

- **Rate of Change of Voltage (ROCOV)**: Monitors dV/dt. Similar logic; catches voltage-driven islanding events that ROCOF misses.

- **Phase angle jump detection**: Monitors sudden phase angle shift between inverter output and grid reference. Fast response but high nuisance trip rate during normal grid switching events.

- **Frequency deviation**: IEEE 1547-2018 defines Over/Under Frequency trip settings: mandatory trip at <57.0 Hz (0.16 seconds) and >60.5 Hz (varies by Category A/B/C setting). These are anti-islanding backstops.

- **Voltage deviation**: Under/Over Voltage: mandatory trip at <50% nominal (0.16 seconds) through multiple thresholds. Inverter ceases to energize grid if voltage falls out of range.

**Active detection methods** (inject perturbation, observe response):

- **Slip Mode Frequency Shift (SMS)**: Inverter deliberately shifts its frequency reference slightly. A connected grid resists the shift; an islanded grid drifts, triggering detection. Low nuisance trip rate, widely implemented.

- **Sandia Frequency Shift (SFS)**: Accelerates the frequency drift by making the shift proportional to the observed drift rate. More aggressive but faster detection.

**UL 1741 SB (Supplement B) and the 3rd Edition (2025)**

UL 1741 is the safety certification for inverters. UL 1741 SB tests the advanced grid-support functions required by IEEE 1547-2018: volt-VAR response, volt-watt response, frequency-watt response, and ride-through requirements. In December 2025, Enphase's IQ8 Microinverter became the first product certified to UL 1741 3rd edition, aligning certification more directly with IEEE 1547-2018's companion testing standard (IEEE 1547.1). For Zone 5 procurement: require UL 1741 SB or 3rd-edition certification for any inverter in a utility-interconnected microgrid. Non-certified inverters will not pass utility interconnection review.

**California Rule 21** as a model: California's Rule 21 was the first state interconnection standard to require IEEE 1547-2018 advanced grid functions. Illinois, Michigan, and Wisconsin utilities follow IEEE 1547-2018 directly without a state supplement — making California Rule 21 experience directly applicable to Zone 5 system commissioning.

---

## Section 2: Community-Scale Battery Storage Systems

### 2.1 LiFePO4 Chemistry — Why It Is the Correct Choice for Zone 5

LiFePO4 (lithium iron phosphate) is the preferred chemistry for community microgrids on three dimensions: safety, cycle life, and cold-weather performance.

**Safety**: LiFePO4 has the most thermally stable cathode chemistry in commercial lithium batteries. Thermal runaway requires significantly higher temperatures than NCA (lithium nickel cobalt aluminum) or NMC (nickel manganese cobalt). For Zone 5 installations in farm buildings or community-owned structures without fire suppression: LiFePO4 is the appropriate choice. NCA (used in early Tesla Powerwall) has superior energy density but higher fire risk.

**Cycle life vs. Depth of Discharge (DoD)**: LiFePO4 offers 2,000–6,000 cycles at 80% DoD, versus 500–1,500 cycles for NMC at equivalent DoD. For a community battery cycled daily, this translates to 5–16 years of life versus 1.5–4 years for NMC. The DoD tradeoff: at 80% DoD (recommended), LiFePO4 reaches rated cycle life. At 50% DoD (conservative), cycle life extends to 8,000+ cycles but effective capacity is halved — meaning you need twice the installed capacity. Recommended practice: size LiFePO4 banks for 80% DoD, run at 60–70% DoD in daily operation, and treat the remaining 10–20% as emergency reserve.

**72–120 hour sizing and the 3–5 day capacity recommendation**: For Phase 5's target resilience window, the sizing logic is:
- Critical community load during islanding (load-shed to essential services): 40–60 kW for a 100-person community
- 72-hour winter scenario: 40 kW × 72 hours = 2,880 kWh required from storage alone (before solar/wind contribution)
- 120-hour scenario: 40 kW × 120 hours = 4,800 kWh
- Practical hybrid (storage covers overnight + cloudy periods; biogas/diesel generator runs 4–6 hours/day): battery covers 16–18 hours/day × 5 days = 400–540 kWh from battery + 100–120 kWh from 2 hours of daily solar + 200 kWh from generator = ~800 kWh total per day

The Phase 5 recommendation: **400–600 kWh of LiFePO4 storage** paired with a 40 kW backup generator. This covers 10+ hours of critical loads without generation, provides resilience against solar and wind gaps, and keeps battery capital in the $50K–$200K range (installed). Full 120-hour solar/wind-only coverage requires 4,800+ kWh — impractical at current pricing without long-duration storage technology.

### 2.2 BMS Architecture: Centralized vs. Distributed Cell Monitoring

**Centralized BMS**: One master controller monitors all cells via a communication bus. Lower cost, simpler design. Failure mode: BMS failure renders the entire battery bank inoperable. Acceptable for residential scale; suboptimal for community-critical infrastructure.

**Distributed BMS** (recommended for community scale): Each module (typically 15–20 cells) has its own monitoring board. A master controller aggregates data but individual modules can continue operating if the master fails. More expensive (adds $5–15/kWh to battery cost) but appropriate when the battery is life-safety infrastructure.

**Key BMS functions for Zone 5 winter operation**:
- Cell voltage monitoring: alert if any cell drops below 2.5V (LiFePO4 minimum) or rises above 3.65V (maximum)
- Temperature monitoring: block charging if any cell is below 0°C (32°F) — charging at sub-freezing temperatures causes irreversible lithium plating that reduces cycle life by 50–80%
- Self-heating activation: 2025-generation LiFePO4 battery systems include integrated heating films that warm cells to >5°C before accepting charge current. This adds $10–25/kWh to system cost but is non-negotiable for Zone 5 winter operation
- State of Health (SoH) tracking: monitors capacity fade over time; triggers replacement recommendation at 80% of original capacity

### 2.3 Thermal Management for Zone 5 Winter (-10°C Operation)

Zone 5 winters regularly produce ambient temperatures of -10°C to -25°C in unheated structures. LiFePO4 discharge performance at -10°C degrades to approximately 70–80% of rated capacity. Charge acceptance below 0°C is essentially zero without heating.

**Battery enclosure design for Zone 5**:
- Insulated enclosure: R-20 minimum (equivalent to 5.5 inches of spray foam) — reduces heating energy demand significantly
- Thermostatically controlled heating: maintain cells above 5°C for charging, above -10°C for discharge
- Ventilation: LiFePO4 does not off-gas hydrogen under normal operation, but thermal runaway scenarios require ventilation. Design for 4–6 air changes per hour with passive vents that open at elevated temperature
- Heating energy budget: maintaining a 400 kWh battery bank above 5°C in a -20°C environment with proper insulation requires approximately 0.5–1.5 kW continuous — budget this in load calculations

---

## Section 3: Distributed Generation Options for Zone 5

### 3.1 Solar PV

Zone 5's solar resource is adequate rather than excellent. Key parameters from NREL NSRDB (1-axis tracking):

| State | Annual avg (kWh/m²/day) | Dec–Jan minimum | Capacity factor |
|---|---|---|---|
| Iowa | 4.3 | 2.1–2.6 | ~13.5% |
| Illinois | 4.2 | 2.0–2.5 | ~13% |
| Indiana | 4.1 | 1.9–2.4 | ~12.8% |
| Wisconsin | 3.9 | 1.8–2.2 | ~12.5% |
| Michigan | 3.8 | 1.6–2.0 | ~11% |

The 15–20% capacity factor range specified in the task brief is accurate for annual averages; winter capacity factors drop to 7–10%. A 100 kW array generates ~13 MWh/month in July and ~6 MWh/month in January at Zone 5 latitudes.

**Snow and ice management**: Optimal array tilt for Zone 5 (latitude 41–46°N) is 35–40° from horizontal. This is steep enough that snow slides off within 1–2 days of a storm in most cases without active clearing. Ground-mounted arrays at 40° tilt outperform flat commercial roof mounts in winter by 15–25% due to self-clearing. Install the lowest panel edge at minimum 18 inches above typical snow depth (typically 12–24 inches in Zone 5). For critical-load microgrids, include one manual snow brush (no metal edges) per array and a clear dispatch protocol for when to clear vs. wait.

**Bifacial panels**: 5–15% additional yield from albedo reflection off snow on the ground — a meaningful winter bonus in Zone 5. Price premium is modest (5–10% over standard panels); bifacial is the correct choice for new Zone 5 installations.

### 3.2 Micro-Wind

Zone 5's average wind speeds (10–14 mph at 30m height, 12–18 mph at 80m) are excellent for utility-scale turbines but marginal for small turbines. Small turbine performance is rated at 12.5 m/s (28 mph); most Zone 5 sites see 4–7 m/s (9–16 mph) average at 20–30m hub height.

**Savonius vs. HAWT for low-wind zones**: Horizontal-axis wind turbines (HAWT) have better efficiency (Cp ~0.45) but require minimum wind speeds of 7–10 mph to start generating. Savonius vertical-axis turbines start generating at 4–5 mph (Cp ~0.15–0.25) but are less efficient at typical wind speeds. For Zone 5 rural sites with consistent wind exposures (open fields, hilltops), HAWT at 15–20 kW scale (e.g., Bergey Excel 15) are the appropriate choice — they have documented 25+ year operational lifetimes in the Midwest. Savonius designs are better suited to urban constrained sites or very low-wind locations, but their low efficiency at useful wind speeds makes them less attractive economically.

**Key Zone 5 wind advantage**: Winter wind peaks align with lowest solar output — the anti-correlation makes wind-solar hybrid 30–40% more storage-efficient than solar-only. Iowa's winter wind capacity factor exceeds 40%; even southern Illinois exceeds 30% in January. For 120-hour winter resilience, a 20 kW wind turbine running at 35% winter capacity factor provides 7 kW average continuous — sufficient to meaningfully extend battery autonomy.

### 3.3 Biogas from Agricultural Waste

Zone 5's agricultural density makes biogas a realistic generation option:

**Dairy manure digestion**: A 100-cow dairy produces ~6,000 gallons/day of manure slurry. A covered lagoon or plug-flow digester converts this to ~50,000 cubic feet/day of biogas (55–65% methane). A 40 kW biogas generator running 6 hours/day at this scale produces ~240 kWh/day — enough to carry an evening charge cycle for 400 kWh of LiFePO4 storage. Capital cost for a complete on-farm digester + generator: $150,000–$300,000. USDA REAP grants can cover 25–50% of this cost (when programs are open).

**Crop residue and food waste**: Anaerobic digestion of crop residues and food waste generates 200–1,200 m³ of biogas per tonne of volatile solids depending on feedstock. Community-scale community digesters processing mixed agricultural waste (manure + food waste + crop residue) can achieve better economics than single-feedstock systems.

**Critical limitation for Zone 5**: Anaerobic digestion is mesophilic — optimal performance at 35°C. Zone 5 winter ambient temperatures require digester heating (4–7% of biogas output consumed to maintain digester temperature). At -20°C ambient with poor insulation, heating demand rises to 15–20% of output. Thermophilic digesters (55°C) are more efficient per unit but more sensitive to temperature variations — not recommended for first-time community installations.

**Biogas as grid backup fuel**: A key resilience advantage of biogas is storage. Unlike solar (intermittent) or wind (intermittent), a pressurized biogas tank provides dispatchable generation on demand. A 10,000 gallon compressed biogas tank at modest pressure holds sufficient fuel for 100–200 hours of backup generator operation. This is the "fuel independence" value proposition of agricultural biogas microgrids.

### 3.4 Diesel Backup: Role, Sizing, and Fuel Storage

Diesel generators remain essential for Zone 5 community microgrids as black-start capability and deep-winter backup. The question is not whether to include diesel but how to right-size and constrain its role:

**Role definition**: Diesel should run during the 4–6 darkest winter days when solar is minimal and wind is insufficient to maintain battery charge. Target: 4–6 hours/day during worst-case winter outages. If the microgrid is correctly sized, diesel should consume under 200 gallons/week during worst-case winter operation.

**Efficiency and emissions**: Modern tier-4 diesel generators operate at 30–40% thermal efficiency (better than older units). At 40 kW output, fuel consumption is approximately 2.5–3.5 gallons/hour. At 6 hours/day during a 5-day winter outage: ~90–105 gallons total. This is a manageable fuel stock for a community facility.

**Fuel storage**: 250–500 gallons of stabilized diesel (Sta-Bil diesel treatment) stored on-site provides 2–5 weeks of backup generation at reduced winter usage. Above-ground double-wall tanks with secondary containment are required by most Zone 5 fire codes for tanks over 275 gallons. Diesel remains stable for 6–12 months without additives; treated diesel is stable for 12–24 months.

**Fallback positioning**: The explicit design goal should be to make diesel operation the exception, not the baseline. A microgrid that runs its diesel backup during every winter night has been undersized on renewable generation or storage.

---

## Section 4: Regulatory Landscape — May 2026

### 4.1 Federal Framework

**IEEE 1547-2018**: The national standard for DER interconnection. Mandated by the Energy Policy Act of 2005. All Zone 5 utility interconnections reference this standard. Key requirements: anti-islanding, ride-through, voltage/frequency response, intentional island provisions. Most recent version: 2018 (current); revision cycle ongoing.

**UL 1741 (safety certification) and UL 1741 SB/3rd edition (advanced grid functions)**: The UL 1741 3rd edition (finalized 2025) aligns certification testing with IEEE 1547.1 testing methods, improving consistency across jurisdictions. As of December 2025, first product certifications are emerging. Zone 5 utility interconnection departments will increasingly require UL 1741 SB or 3rd-edition certification for new interconnections.

**ITC expiration (December 31, 2025)**: The 30% residential Investment Tax Credit under IRA Section 25D expired. Commercial/nonprofit/cooperative entities retain access to the 30% commercial credit under Section 48E through 2027, using tax-equity structures or direct-pay provisions. Battery storage credit (Section 48E) remains in effect through 2032 at 30% for qualifying commercial entities.

**FERC Order 2222**: Requires RTOs to allow DER aggregations in wholesale markets. In MISO territory (Zone 5), full implementation delayed to 2029–2030. Limited Type I (demand response) participation currently being rolled out. MISO minimum offer: 100 kW — accessible for community microgrids of 200 kW+ scale but revenue is uncertain until 2029.

**USDA REAP grants**: Up to $1M per renewable energy system through FY2031. Applications paused as of May 2026 per federal program freeze. Contact state USDA Rural Development Energy Coordinators for current status and expected reopening timeline.

### 4.2 Zone 5 State Policies (May 2026)

**Illinois**: CEJA (2021) remains the most consequential Midwest energy legislation. As of January 1, 2025, new solar installations receive supply-only net metering (credits applied only to energy supply charges, not delivery charges). Pre-2025 installations are grandfathered at full retail rate for system lifetime. Community solar: 393 MWac installed as of January 2025, 150 MW/year new allocations with a 250 MW processing backlog. Storage incentive: ComEd $300/kW solar + $300/kWh storage rebate; Ameren $250/kW + $250/kWh. Illinois community solar participation is available without requiring a behind-the-meter solar installation — a cooperative or household can subscribe to a community solar garden and receive bill credits. 8.5 GW cumulative storage target through 2050 established in 2024 legislation.

**Michigan**: Michigan Public Act 233 (2023): 2,500 MW of storage by 2029 — the first binding storage mandate in the Midwest. MPSC approved 150 MW/600 MWh and 100 MW/400 MWh BESS projects in 2024–2025. Michigan is expected to add over 1 GW of solar in 2025. Community solar program exists but small-scale relative to Illinois. Michigan cooperative utilities (Cherryland, Thumb Electric, HomeWorks) are generally receptive to DG interconnections.

**Iowa**: 64% of electricity from wind and solar in 2023 — nationally leading. Wind lease payments averaging $4,000/MW/year provide meaningful supplemental agricultural income. Iowa opened Order 2222 compliance proceedings for Aggregators of Retail Customers. No strong community solar program as of 2026 — rural cooperatives (IAEC members) are the primary vehicle for distributed energy. The Iowa connection: a Zone 5 community in Iowa seeking 120-hour winter resilience can leverage the state's exceptional wind resource and cooperative utility relationships more effectively than any other Zone 5 state.

**Wisconsin**: PSC approved 488 MW of battery storage as of 2023, 617 MW awaiting review. Focus on Energy program: $150/kW solar rebate + $150/kWh storage rebate for commercial/nonprofit. Bayfield County's microgrid program (841 kW solar, 1,065 kWh storage across 24 sites, 28 communities) is the state's flagship and the most directly applicable Zone 5 case study. Xcel Energy's cooperative territory in Wisconsin has demonstrated a viable interconnection pathway for community microgrids.

**Indiana**: Net metering exists but is capped and subject to ongoing utility challenge. Community solar programs are minimal. The practical path for Zone 5 Indiana communities: direct cooperative ownership or municipal utility rather than investor-owned utility programs. Indiana's rural electric cooperatives (REMC) serve most rural areas and have more DG-receptive interconnection processes than Duke Energy Indiana or Indiana Michigan Power.

### 4.3 Community Solar Models in Practice

**Minnesota model**: Minnesota's Value of Solar (VOS) tariff attempted to credit distributed solar at its true grid value (above retail rate). As of 2025, regulators are shifting from VOS to simplified net metering, drawing criticism for undervaluing locational benefits. LMI Accessible Community Solar Garden (CSG) program has approved 179 MW across 133 gardens as of December 2025. Proposed SF 2393 (2025 legislative session) would sunset the LMI CSG program by 2030 — status uncertain. Minnesota community solar gardening requires no behind-meter installation; residents subscribe to a remote garden.

**Colorado model**: SB24-207 (Community Solar Modernization Act, 2024) streamlines solar farm development and expands LMI access. Colorado's model allows third-party ownership of community solar gardens, broadening financing options beyond direct community ownership.

**Illinois model**: CEJA's community solar framework is the most mature in the Midwest. 150 MW/year allocations, income-qualified subscriber access, third-party ownership allowed. The processing backlog (250 MW) reflects program popularity but also permitting and interconnection delays.

**For Zone 5 communities not in Illinois or Minnesota**: Direct ownership through a cooperative or municipal utility is more reliable than relying on third-party community solar programs. The most resilient path is to own the generation outright — subscriber programs provide bill savings but not physical control over the infrastructure.

---

## Section 5: Case Studies

### 5.1 Military Bases — Proven Long-Duration Islanding

**Fort Liberty (formerly Fort Bragg), North Carolina**: The JSOC compound microgrid, designed for 14-day continuous island operation, provides the most documented military microgrid specification. The system integrates generation sources (solar, generators), automatic transfer switches, master controller, synchronization controllers, and protection relays for compound-level islanding from Fort Liberty's main distribution system. The National Defense Authorization Act of 2026 authorized $80 million for expanded power generation and resilient microgrid capability at Fort Liberty. The Army's stated goal: all bases equipped with microgrids by 2035 as part of carbon-free electricity objectives. Published guidance: PNNL-38494 *Microgrid Handbook for Army Resilience* (2024) — the most rigorous publicly available technical guide for community-scale islanding design, load shedding protocols, and protection coordination.

**Applicability to Zone 5**: Military microgrid design requirements (continuous operation, no single points of failure, defined load shedding tiers, black start capability, trained operators) map directly onto community resilience requirements. PNNL-38494 is publicly available and should be a primary reference for Zone 5 community microgrid engineering design.

### 5.2 Island Grids — Renewable Integration at Scale

**Puerto Rico post-Hurricane Maria (2017–present)**: Hurricane Maria left rural Puerto Rico without power for 9+ months in some areas — the most consequential modern case study of grid failure and distributed energy recovery. Key lessons:
- The nonprofit Casa Pueblo installed 41 kW solar + 74 kWh storage across five critical businesses (clinic, pharmacy, food storage), commissioned May 2022. The model: businesses provide critical community services in exchange for energy cost savings. Direct applicability to Zone 5 rural towns.
- Cornell/Vieques mobile battery project: powers two refrigerated trailers serving as local food storage, operating independently of the main grid. ORNL's orchestrator system links multiple Vieques microgrids for peer-to-peer power sharing when one site loses solar generation.
- RMI analysis (2019): clean energy portfolios (solar + wind + storage) outperform natural gas investment economically for island grids. This finding strengthened the economic case for Zone 5 rural microgrids.

**Hawaii grid modernization**: Hawaiian Electric's Integrated Grid Plan targets 100% renewable by 2045. Current status (2026): 36% renewable generation, up from under 10% in 2010. The 2026–2030 second-cycle Integrated Grid Plan cycle includes systematic microgrid deployment with defined islanding protocols. Key technical challenge mirrored in Zone 5: high solar penetration creates voltage rise and reverse power flow on distribution feeders — requires smart inverter volt-VAR response (mandated by IEEE 1547-2018, tested by UL 1741 SB) to maintain power quality. Hawaii's experience shows that distribution-level voltage management becomes the binding constraint above ~30% solar penetration — Zone 5 communities should design for voltage management from the start.

**Bornholm, Denmark**: Island of 40,000 people; serves as Denmark's primary smart grid demonstration. Connected to Swedish grid by 60 kV AC cable but capable of island operation. EcoGrid EU project demonstrated that automated demand response (households with smart heating controls) reduced peak load by approximately 670 kW (1.2% of peak) using 5-minute real-time price signals. The key lesson: households with equipment responding automatically to price signals accounted for 87% of peak reduction — human behavioral response was minimal without automation. For Zone 5: design load control into the microgrid's demand response from day one (OpenADR 3.0); do not rely on manual consumer response to grid conditions.

### 5.3 University Microgrids — Technical Benchmarks

**MIT Campus Microgrid**: MIT's Central Utilities Plant (CUP) is anchored by a 22 MW gas turbine providing simultaneous heat and electricity through cogeneration. The upgraded smart microgrid design enables MIT to take most or all campus load off the regional grid when needed — islanding capability for a 178-acre campus serving 11,000+ students and faculty. MIT added 500 kW of rooftop solar in 2024. The cogeneration architecture (thermal + electrical) is directly applicable to Zone 5 community microgrids with combined heat and power (CHP) plants fueled by biogas.

**Colorado State University**: Pivot Energy is developing a 5.75 MW community solar project for CSU, expected construction start winter 2025–2026, completion Q4 2026. This is an off-site community solar subscription model rather than a campus microgrid with islanding capability — but demonstrates the scale and economics of university-scale community solar financing in a Rocky Mountain context comparable to Zone 5 conditions.

### 5.4 Tribal Microgrids — Governance and Capital Lessons

**Navajo Nation**: USDA announced $100+ million through the Powering Affordable Clean Energy Program for the Navajo Tribal Utility Authority — solar-powered facilities and battery storage generating 30+ MW for ~40,000 tribal customers. An Ojo Encino Chapter solar project started July 2025, expected completion June 2026 (household-level solar + community microgrid + powerline infrastructure). Navajo Power has secured a 750 MW/3 GWh solar+storage land lease — demonstrating the scale of tribal energy development capacity. Critical governance lesson: tribal sovereignty enables faster permitting than state/county processes in many cases, but capital access remains the primary constraint. Federal programs (IRA direct-pay, USDA REAP, DOE Loan Programs Office) are the primary financing mechanisms.

**Red Lake Nation and White Earth Nation (Minnesota)**: Received $3.15M and $1.75M respectively from the Biden DOE for solar+battery microgrids at community schools. These are the most Zone 5-proximate tribal microgrid examples. Design pattern: school as the anchor load (operates 250 days/year, predictable demand, community gathering point during emergencies).

**Governance insight**: Tribal microgrids succeed when the tribal entity controls operations directly (Tribal Utility Authority model) rather than relying on outside contractors for ongoing O&M. The Blue Lake Rancheria (California) tribal microgrid, owned and operated by the tribe, is the reference case for this model — 1 MW solar + LiFePO4 battery, operational 2024, serving 50-person tribal population.

### 5.5 Electric Cooperative Microgrids — Zone 5 Nearest-Neighbor Models

**Bayfield County, Wisconsin**: 841 kW solar + 1,065 kWh storage across 24 sites, 28 rural communities including Red Cliff Band tribal lands. $9.7M federal (DOE ERA) + $2.7M state cost share. Design firm: muGrid Analytics (mugrid.com). Utility partner: Xcel Energy's cooperative territory. Status: construction ongoing 2025–2029. Expected: 1 million kWh/year clean energy. The most directly applicable Zone 5 case study — contact Bayfield County Office of Sustainability and Clean Energy or muGrid Analytics for lessons-learned documentation before commissioning any Zone 5 microgrid project.

**Resilient Minneapolis Project**: 1,450 kW solar + 2,000 kW storage across four Minneapolis school buildings — a clustered microgrid approach serving as community resilience anchors in low-income neighborhoods. This project demonstrates the urban variant of the model: distributed assets linked by communication but geographically clustered, with schools as the load anchor and community gathering site.

**Minnesota LMI Community Solar Garden Program**: 179 MW approved across 133 gardens as of December 2025. The cooperative governance model (member-owned, democratic control) aligns well with Zone 5 community values and provides an organizational template for community energy development without requiring a new legal entity from scratch.

---

## Section 6: Open-Source Microgrid Platforms

### 6.1 Design and Optimization Tools

**HOMER Energy (homerenergy.com)**: Industry standard for hybrid microgrid feasibility. Inputs: load profile, solar/wind resource, equipment costs. Outputs: optimal system size, net present cost, levelized cost of energy, reliability metrics. Start here for any Zone 5 community feasibility study. Free academic version available; commercial license ($1,500–$3,000/year) required for advanced optimization.

**PVWatts (pvwatts.nrel.gov)**: NREL's free browser-based tool for solar production modeling. Input coordinates and system specs; output: monthly and annual energy production from NREL National Solar Radiation Database. Essential for Zone 5 seasonal variation modeling — run both July (peak summer) and January (worst-case winter) scenarios before finalizing system size.

**GridLAB-D (github.com/gridlab-d/gridlab-d)**: Open-source distribution system simulator from Pacific Northwest National Laboratory (PNNL). Enables high-fidelity transient modeling of microgrids including protection coordination and islanding behavior. Not a beginner tool — requires power systems engineering expertise. Best use: validating control system settings and protection coordination before construction.

**OpenDSS (EPRI)**: Open-source distribution system simulator developed by the Electric Power Research Institute. Industry standard for power flow analysis, voltage regulation studies, and DER integration studies. Widely used by utilities for interconnection feasibility studies. A community seeking to understand what their utility's interconnection study will find should run OpenDSS on their proposed microgrid configuration first.

**PandaPower / VeraGrid (formerly GridCal)**: PandaPower is a Python library for power grid analysis (500,000+ downloads, Fraunhofer IEE/University of Kassel). GridCal was a widely used Python-based power systems software; the project was renamed VeraGrid (github.com/SanPen/VeraGrid) after a trademark dispute. Both are actively maintained. Best for: scripted power flow analysis, short-circuit calculations, optimal power flow. Integration: can be used with Python data science tools for custom load modeling and dispatch optimization.

**pymgrid (github.com/Total-RD/pymgrid)**: Python virtual microgrid environments for ML-based energy management development. Useful for communities developing automated dispatch algorithms — allows simulation of different control strategies without physical hardware.

**PSCAD (Manitoba Hydro International)**: The gold standard for electromagnetic transient (EMT) simulation of power systems. In 2025, NREL developed a generic multi-functional EMT model for grid-forming inverters in PSCAD. Used for protection coordination studies, fault analysis, and transient stability analysis that ground-level power flow tools miss. Required for any microgrid that will be peer-reviewed by a utility before interconnection. Not open-source (commercial license required) but is the accepted standard for utility-required EMT studies.

### 6.2 Communication and Demand Response Standards

**OpenFMB (Open Field Message Bus)**: Originally developed by Duke Energy, now a NAESB-ratified standard. Enables real-time data exchange between microgrid components using MQTT or DDS protocols — kilowatts, voltage, state of charge, frequency, timestamps. Allows multi-vendor systems to communicate without proprietary lock-in. NREL maintains documentation. For Zone 5 community microgrids with multiple sites: OpenFMB enables the ORNL multi-microgrid orchestrator model (demonstrated in Vieques) where adjacent sites share excess generation.

**OpenADR 3.0 (Open Automated Demand Response)**: The latest version of the US DOE/NIST-backed demand response signaling standard. OpenADR 3.0 (specification finalized 2024) uses RESTful APIs and JSON, with OAuth + TLS 1.2 security. Enables microgrids to receive automated price and grid-condition signals from utilities and respond by adjusting loads — load shifting for water heating, grain drying, refrigeration, and EV charging. The Bornholm case study confirms that automated demand response (households with smart controllers) outperforms manual behavioral response by 87%. For Zone 5: integrate OpenADR 3.0 compatible controllers for large dispatchable loads (grain dryers, water heaters, cold storage) from initial installation. Retrofit cost is much higher than inclusion at construction.

**IEC 61850**: International standard for substation and distribution grid communications. Required for utility-interconnected microgrids above 100 kW scale in most utility territories. Defines how protection relays, switches, meters, and controllers communicate using vendor-neutral protocols. Compatibility with IEC 61850 is required for any microgrid that will interface with utility SCADA systems.

### 6.3 Open-Source Hardware and DIY Approaches

**Raspberry Pi / Arduino microgrid monitoring**: For communities with technical members who can program, Raspberry Pi-based systems can log solar generation, battery state of charge, load data, and grid status to a local database, with alerts via SMS or email. This is not a control system replacement — it is a monitoring layer. Open-source projects: ESPHome (ESP32-based sensors for energy monitoring), Home Assistant (dashboarding), Node-RED (automation flows for alerts and simple control logic).

**Open Inverter Project**: Community-developed firmware for electric vehicle inverters repurposed for solar applications. Not yet production-ready for grid-connected microgrids, but relevant for off-grid household-scale installations within the community. Monitor github.com/openinverter for maturity.

**NIST RAMSES Microgrid Testbed**: NIST's Real-Time Automation Controls Laboratory (RACL) hosts a hardware-in-the-loop microgrid testbed. Primarily a research tool, but NIST publishes testbed specifications and protocols that inform best practices for community microgrid commissioning.

---

## Section 7: Integration with Phase 4 and Phase 5 Wave 1

### 7.1 Governance Prerequisites (Phase 4 Integration)

The Phase 4 Framework's most important finding is that governance infrastructure is the load-bearing structure. For microgrids specifically, this means:

**Before commissioning an engineering study**: The community must have an established legal entity (cooperative, nonprofit, or municipal authority) capable of signing contracts. Utility interconnection agreements are legally binding contracts. Grant applications require an organizational signatory with federal tax identification. An informal group of neighbors cannot sign an interconnection agreement.

**Governance module prerequisites from Phase 4**:
- Decision-making authority: Who approves capital expenditures above $X? Who can commit the organization to a 25-year interconnection agreement?
- Conflict resolution: Microgrid governance will generate disputes (who bears cost of reliability incidents, how is excess generation compensated, what happens when a member wants to leave the cooperative). Phase 4's conflict resolution modules should be referenced explicitly in the microgrid cooperative's bylaws.
- Transparent operations: Monthly energy generation and consumption reports to all members. Financial accounts audited annually. These are standard cooperative governance requirements and directly address the trust-building function identified in Phase 4.

**The cooperative governance model for Zone 5**: An electric cooperative is the most natural legal structure for a community microgrid in Zone 5. It is familiar to rural communities (most Zone 5 rural areas are already served by electric cooperatives), provides democratic member control (one member, one vote), has established legal precedent in all five Zone 5 states, and qualifies for nonprofit/cooperative tax treatment that enables Section 48E direct-pay provisions.

### 7.2 Connection to Phase 5 Wave 1 Microgrids Section

Phase 5 Wave 1 (household coordination infrastructure tier) addressed individual and household-scale energy resilience — off-grid inverters, household batteries, and load prioritization. The community microgrid layer in Wave 2 operates as the next tier up in the layered resilience architecture:

- **Household tier** (Phase 5 Wave 1): 40–50 homes × 5 kW solar + 10–20 kWh battery = 200–250 kW distributed generation, 1–2 days autonomy per household
- **Community tier** (this research): 80–100 kW central solar + 20 kW wind + 400 kWh battery + 40 kW generator = 5+ days autonomy for critical infrastructure

The technical bridge: household grid-tied inverters shut down during grid outages (anti-islanding protection). To contribute to the community microgrid, household inverters must be GFM-capable (e.g., Enphase IQ8, SMA Sunny Boy Storage) or have manual transfer switches that disconnect from utility before connecting to the community bus. Design for this at the household inverter procurement stage — retrofit cost is much higher.

### 7.3 Seedwarden Project Integration

The Seedwarden project's medicinal herb and food production distribution operates in Zone 5's agricultural context. Three integration points:

**Cold storage for seeds and herbs**: Seed storage facilities should be designed as Tier 1 loads in the community microgrid's load shedding protocol — temperature control for seeds is a long-horizon food security investment that justifies always-on power allocation. Design cold storage enclosures with thermal mass (R-40+ insulation, thermal flywheel capacity) to coast 6–12 hours without active cooling, reducing peak demand on the microgrid battery.

**Medicinal herb drying**: Herb drying facilities can be designed as Tier 3 (discretionary) loads that run preferentially during solar midday peaks, using excess renewable generation rather than storage. This is a demand-side optimization that extends battery autonomy.

**Distribution infrastructure**: Seedwarden's planned medicinal herb distribution network benefits from a microgrid-powered community cold chain — refrigerated storage at distribution hubs maintaining seed and processed herb quality during the 72-hour+ grid-down scenarios that are the design basis for this research.

---

## Sources (48 Annotated Citations)

### Architecture and Technical Standards
1. [IEEE 1547-2018 — Interconnection and Interoperability of DERs with Area Electric Power Systems](https://standards.ieee.org/ieee/1547/5915/) — National standard for all Zone 5 utility interconnections; Section 8 governs intentional island requirements
2. [IEEE 2030.10-2021 — DC Microgrids for Rural and Remote Electricity Access](https://ieeexplore.ieee.org/document/9646866) — Specific standard for DC microgrid rural applications
3. [UL 1741 3rd Edition / Supplement B — Grid Support Inverter Certification](https://www.kitecompliance.ai/vertical-compliance/ul-1741) — Safety and grid-support certification; first UL 1741 3rd-ed product (Enphase IQ8) certified December 2025
4. [UL 1741 vs. IEEE 1547 — Certification Differences Explained](https://electricaltrader.com/blogs/news/ul-1741-vs-ieee-1547-certification-differences) — Clarifies which standard governs safety (UL 1741) vs. grid performance (IEEE 1547)
5. [Effective ROCOF-Based Islanding Detection for Different Types of Microgrid — IEEE Xplore](https://ieeexplore.ieee.org/document/9693167/) — Peer-reviewed ROCOF detection for GFM and GFL inverter microgrids
6. [Anti-Islanding Protection: Guide to Inverters and Compliance](https://www.kitecompliance.ai/navigating-compliance/anti-islanding-protection) — Accessible overview of IEEE 1547-2018 anti-islanding requirements
7. [Islanding Detection for Grid-Forming Inverters — Imperix](https://imperix.com/doc/implementation/islanding-detection-for-grid-forming-inverters) — Technical implementation guide for GFM inverter islanding detection methods
8. [Grid-Aware Islanding and Resynchronisation of AC/DC Microgrids — arXiv 2025](https://arxiv.org/pdf/2503.04597) — Most recent peer-reviewed control theory for hybrid microgrid islanding
9. [NREL Generic EMT Model for Grid-Forming Inverters (PSCAD) — NREL/TP-5D00-88660](https://docs.nrel.gov/docs/fy25osti/88660.pdf) — 2025 NREL PSCAD model for GFM inverters; reference for EMT simulation
10. [Co-Simulation of PSS/E, OpenDSS, and PSCAD for Power Systems Stability Analysis — NREL 2025](https://research-hub.nrel.gov/en/publications/co-simulation-of-psse-opendss-and-pscad-for-power-systems-stabili/) — Multi-tool simulation methodology for microgrid interconnection studies
11. [Default IEEE 1547-2018 Setting Requirements — Unitil](https://unitil.com/sites/default/files/2022-09/Default_IEEE1547-2018_Settings_Requirements_Issued.pdf) — Example utility implementation of IEEE 1547-2018 settings; useful for Zone 5 pre-application preparation
12. [Droop Control in Islanded Microgrids — IET Renewable Power Generation 2025](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/rpg2.13186) — Peer-reviewed droop control for islanded AC microgrids
13. [IEEE 2030.9-2019 — Recommended Practices for Microgrid Controllers](https://standards.ieee.org/ieee/2030.9/6918/) — Control architecture guidance for site-level EMS

### Storage Technology
14. [LiFePO4 Cold Weather Performance — Self-Heating Battery Technology White Paper](https://www.lithpower.com/the-thermodynamics-of-winter-a-white-paper-on-self-heating-lifepo4-technology/) — Technical analysis of Zone 5-relevant winter performance; self-heating BMS designs
15. [How Cold Weather Affects LiFePO4 Batteries — Neexgent](https://www.neexgent.com/article/how-cold-weather-affects-lifepo4-batteries.html) — Cell-level cold-weather degradation mechanisms; charging prohibition below 0°C
16. [LiFePO4 Battery Thermal Management Systems — Anern](https://www.anernstore.com/blogs/diy-solar-guides/lifepo4-battery-thermal-management) — Enclosure design guide; heating energy budgets for Zone 5 temperatures
17. [NREL Cost Projections for Utility-Scale Battery Storage 2025 — fy25osti/93281](https://docs.nrel.gov/docs/fy25osti/93281.pdf) — Authoritative cost benchmarks: $125–$334/kWh installed at utility scale
18. [Commercial Battery Energy Storage 200 kWh to 1 MWh — GSL Energy](https://www.gsl-energy.com/commercial-energy-storage-system-capacity-analysis-solutions-from-200kwh-to-1mwh.html) — Commercial-scale (community-relevant) battery cost and configuration analysis
19. [Grid-Scale Battery Storage in 2026 — Costs and Technology Guide](https://www.polinovelbess.com/info/grid-scale-battery-storage-2026-costs-technolo-103489640.html) — Updated 2026 pricing benchmarks; $125–$300/kWh installed for competitive projects
20. [Form Energy Iron-Air Battery — Commercial Scale 2026](https://discoveryalert.com.au/form-energy-iron-air-battery-expansion-economics-2026/) — Long-duration storage technology reaching commercial scale; $77–$100/kWh target
21. [Minnesota PUC Approves Xcel/Form Energy 10MW/1,000MWh Iron-Air Battery — Utility Dive](https://www.utilitydive.com/news/minnesota-puc-xcel-form-energy-battery-sherco-solar/685460/) — Zone 5-adjacent first commercial iron-air deployment

### Regulatory — Federal
22. [FERC Order 2222 — DER Aggregation Explainer](https://www.ferc.gov/ferc-order-no-2222-explainer-facilitating-participation-electricity-markets-distributed-energy) — Official FERC explanation of DER market participation rules
23. [FERC Order 2222 Tracker — May 2025](https://cuswebsite.blob.core.windows.net/2222tracker/Tracker-Report-May-2025.pdf) — Current state of RTO compliance filings; MISO delayed to 2029–2030
24. [MISO Order 2222 — DEAR Implementation Timeline 2029–2030](https://blog.yesenergy.com/yeblog/distributed-energy-resources-a-state-of-the-market-report) — MISO-specific delay context; minimum 100 kW offer size
25. [USDA REAP Renewable Energy Systems Program](https://www.rd.usda.gov/programs-services/energy-programs/rural-energy-america-program-renewable-energy-systems-energy-efficiency-improvement-guaranteed-loans) — Primary federal grant program for Zone 5 rural energy; up to $1M per project
26. [Federal Regulatory Outlook for Electric Storage 2026 — Morgan Lewis](https://www.morganlewis.com/pubs/2026/03/federal-regulatory-outlook-for-electric-storage-qfs-and-inverter-based-resources) — 2026 regulatory landscape for storage and inverter-based resources

### Regulatory — Zone 5 States
27. [Illinois CEJA Implementation — ICC](https://www.icc.illinois.gov/programs/climate-and-equitable-jobs-act-implementation) — Official implementation tracker; storage incentives, community solar allocations
28. [Illinois Solar Incentives 2026 — EnergySage](https://www.energysage.com/local-data/solar-rebates-incentives/il/) — Updated rebate amounts; January 2025 net metering change implications
29. [Illinois Energy Storage Legislation 8.5 GW — Energy Storage News](https://www.ess-news.com/2024/10/16/illinois-energy-storage-legislation-calls-for-8-5-gw-of-projects-through-2050/) — 2024 storage target legislation context
30. [Michigan BESS Planning Guide — Graham Sustainability Institute](https://graham.umich.edu/project/bess-guide) — Comprehensive Michigan battery storage deployment guidance
31. [Michigan Public Act 233 of 2023 — 2,500 MW Storage Mandate](https://graham.umich.edu/media/files/BESS-guide.pdf) — Text and analysis of Michigan's storage mandate
32. [Wisconsin Solar and Storage — SEIA](https://seia.org/state-solar-policy/wisconsin-solar/) — Wisconsin policy overview; Focus on Energy rebate programs
33. [Minnesota LMI Community Solar — 179 MW Approved, 2026](https://pv-magazine-usa.com/2026/03/19/minnesota-lmi-community-solar-reaches-179-mw-amid-regulatory-shifts/) — Current Minnesota community solar program status
34. [Solar Policy Report Q2 2025 — 252 Actions Nationally](https://www.solarpowerworldonline.com/2025/07/solar-policy-report-finds-numerous-net-metering-community-solar-updates-in-q2-2025/) — Comprehensive Q2 2025 policy action tracker across Zone 5 states
35. [Iowa Wind Lease Payments and Cooperative Development](https://agpolicyreview.card.iastate.edu/winter-2022/utility-scale-wind-and-solar-development-iowa-trends-prospects-and-land-factor) — Iowa wind economics; $4,000/MW/year lease rates for agricultural landowners

### Case Studies
36. [Fort Liberty Microgrid — Army Microgrid Program 2026](https://www.army.mil/article/255597/developing_microgrids_to_deliver_energy_resilience) — Military microgrid development program; 14-day islanding design standard
37. [PNNL Microgrid Handbook for Army Resilience — PNNL-38494](https://www.pnnl.gov/main/publications/external/technical_reports/PNNL-38494.pdf) — Comprehensive engineering guide for load shedding, protection, and black start; primary reference for Zone 5 community microgrid design
38. [Army to Equip All Bases with Microgrids by 2035 — Microgrid Knowledge](https://www.microgridknowledge.com/editors-choice/article/11427449/army-to-equip-all-bases-with-microgrids-by-2035-as-part-of-carbon-free-electricity-goal) — Policy context for military microgrid program scale
39. [Hawaiian Electric Integrated Grid Plan 2026–2030](https://www.hawaiianelectric.com/hawaiian-electric-finalizes-integrated-grid-plan-to-decarbonize-its-energy-system-by-2045-stabilize-rates) — Hawaii's detailed microgrid deployment roadmap; voltage management lessons
40. [Bornholm Island Smart Grid — EcoGrid EU Project](https://microgridknowledge.com/microgrid-lab-bornholm-ecogrid-eu/) — Demand response lessons; automated vs. behavioral response findings
41. [Bornholm as Test and Demonstration Site — DTU](https://balticenergyisland.com/wp-content/uploads/2023/10/Bornholm-test_demonstration-site-DTU.pdf) — Technical specifications; island mode operation from Swedish grid connection
42. [MIT Microgrid — 22 MW Cogeneration Campus System](https://energy.mit.edu/news/the-microgrid/) — University-scale CHP microgrid; combined heat and power model applicable to Zone 5 community buildings
43. [Navajo Nation Ojo Encino Solar + Microgrid Project — July 2025](https://opvp.navajo-nsn.gov/260305-solar-energy-project-for-ojo-encino-families/) — Tribal chapter-scale microgrid with community powerline infrastructure
44. [USDA $100M for Navajo Tribal Utility Authority Solar](https://www.kjzz.org/tribal-natural-resources/2025-01-20/usda-announces-100-million-solar-power-investment-for-navajo-tribal-utility-authority) — Federal program financing model for tribal microgrids
45. [Bayfield County Microgrid — muGrid Analytics Case Study](https://www.mugrid.com/projects/bayfield) — Most directly applicable Zone 5 case study; contact for lessons-learned documentation
46. [Resilient Minneapolis Project — 1,450 kW Solar + 2,000 kW Storage](https://www.renewableenergyworld.com/power-grid/microgrid/minneapolis-microgrid-project-is-a-blueprint-for-community-resilience/) — Urban Zone 5 clustered microgrid; schools as resilience anchors
47. [Minnesota Emerging as Microgrid Technology Hub — MinnPost 2025](https://www.minnpost.com/energy/2025/08/minnesota-is-emerging-as-a-hub-for-microgrid-technology-unlocking-cleaner-more-reliable-local-power-oati/) — Minnesota cooperative utility microgrid deployment context

### Open-Source Tools
48. [OpenADR 3.0 — Five Use Cases for Renewable Energy](https://codibly.com/blog/articles/5-use-cases-openadr-3-0) — Practical OpenADR 3.0 implementation guidance; microgrids as demand response participants
49. [OpenFMB for DER Management — SEPA Green Ovations](https://sepapower.org/knowledge/green-ovations-open-source-smarts-openfmb-supports-der-management/) — OpenFMB architecture and implementation for multi-site microgrids
50. [GridCal/VeraGrid — Cross-Platform Power Systems Software — GitHub](https://github.com/sanpen/gridcal) — Open-source Python power flow and optimization; note: renamed to VeraGrid (github.com/SanPen/VeraGrid) after trademark dispute

---

## Confidence Assessment and Evidence Gaps

**High confidence** (multiple consistent sources, verified against primary standards):
- IEEE 1547-2018 islanding requirements and UL 1741 SB compliance framework
- LiFePO4 cold-weather charging prohibition below 0°C and self-heating BMS requirements for Zone 5
- Bayfield County, Wisconsin specifications (841 kW solar, 1,065 kWh storage, 24 sites, 28 communities)
- Illinois January 2025 net metering change (supply-only for new installations)
- MISO Order 2222 delayed to 2029–2030 (confirmed by multiple independent sources)
- Fort Liberty (Fort Bragg) microgrid 14-day islanding design specification

**Moderate confidence** (fewer sources, some extrapolation required):
- Zone 5 biogas economics — limited peer-reviewed data for Zone 5 specifically; numbers extrapolated from Ontario and Iowa data
- Colorado State University microgrid specifications — the 1.6 MW figure commonly referenced could not be independently verified; CSU's confirmed project is a 5.75 MW community solar subscription, not a campus microgrid
- ROCOF threshold settings for Zone 5 community microgrids — ±0.5 Hz/s is widely cited but specific utility requirements vary; pre-application meeting required

**Evidence gaps** (active uncertainty; do not commit based on this research alone):
- Indiana cooperative utility (REMC) interconnection timelines for microgrids — no Zone 5 Indiana case study found; contact Indiana REMC association directly
- Iron-air battery community-scale pricing — all Form Energy data is utility-scale (10 MW+); pricing for 100–500 kWh community systems unknown
- OpenADR 3.0 compatibility with Zone 5 utility SCADA systems — Zone 5 utilities vary in demand response program maturity; verify with specific utility before designing OpenADR integration
- USDA REAP grant reopening timeline — programs were paused as of May 2026; this is the highest-priority information to verify before beginning grant applications
