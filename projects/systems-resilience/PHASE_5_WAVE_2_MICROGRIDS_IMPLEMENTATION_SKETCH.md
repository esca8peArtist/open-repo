---
title: "Phase 5 Wave 2 — Community Microgrid Implementation Sketch: Zone 5, 50–100 Person Scale"
project: systems-resilience
phase: 5
wave: 2
status: production
created: 2026-05-26
word_count: ~2400
decision_gate: "June 1, 2026 — feasibility and go/no-go for Phase 5 microgrid"
audience: "Community infrastructure decision-makers, project leads"
cross_references:
  - PHASE_5_WAVE_2_MICROGRIDS_RESEARCH_OUTLINE.md
  - MICROGRID_ARCHITECTURE_DECISION_MATRIX.md
  - PHASE_5_WAVE_2_MICROGRIDS_RESEARCH.md
  - PHASE_4_FRAMEWORK.md
---

# Phase 5 Wave 2: Community Microgrid Implementation Sketch

> **Scale target**: 50–100 person Zone 5 Midwest community  
> **Architecture**: Option C — Hybrid AC/DC (see Decision Matrix)  
> **Sizing basis**: 200 kW continuous generation, 1 MWh storage  
> **Resilience target**: 72–120-hour winter grid-down autonomy for critical loads  
> **Timeline**: 18 months from governance formation to first island operation

---

## Most Important Finding

Community microgrid implementation is not primarily a technology problem. It is a governance, financing, and regulatory navigation problem. The technology (hybrid AC/DC with LiFePO4) is commercially mature and proven in Zone 5. The blocking variables are: (1) establishing the legal entity that can sign contracts, (2) navigating utility interconnection on a 6–14 month timeline, and (3) assembling the capital stack in a post-residential-ITC expiration environment. Communities that treat this as an engineering project first will stall on governance. Communities that form the cooperative entity first and begin utility pre-application meetings immediately will commission on an 18-month schedule.

---

## Section 1: Feasibility for Zone 5 50–100 Person Community

### Load Assessment Baseline

A Zone 5 community of 100 people (approximately 35–40 households + shared facilities) has the following load profile:

| Load category | Normal demand | Critical load (island mode) | Notes |
|---|---|---|---|
| Residential (40 households) | 80–120 kW | 20–30 kW | Island mode: heat (winter), refrigeration, basic lighting only |
| Water system (pump + treatment) | 5–15 kW | 5–15 kW | Always on; never shed |
| Community health/medical | 5–10 kW | 5–10 kW | Tier 1; never shed |
| Communications (radios, internet backhaul) | 1–3 kW | 1–3 kW | Tier 1; never shed |
| Agriculture (dairy, grain storage) | 30–80 kW seasonal | 10–20 kW | Dairy milking 2×/day; cold storage; shed grain dryer |
| Community building (shelter/dining) | 10–20 kW | 10–20 kW | Heating in winter; becomes community refuge |
| **Total normal** | **131–248 kW** | — | — |
| **Total critical (island)** | — | **51–98 kW** | Approximately 40–50% of normal peak |

**Design basis**: Size to serve 60 kW continuous critical load during island operation. Normal grid-connected peak of 200 kW. Storage for 17 hours at critical load without generation = 1,020 kWh. With daily solar/wind input (reduced winter estimate: 50 kWh/day from 100 kW array + 20 kW wind) and 4 hours of daily generator operation (160 kWh/day), **400–600 kWh of LiFePO4 storage achieves 5-day resilience** in Zone 5 winter conditions with the hybrid approach.

### What 200 kW Continuous Generation Means in Zone 5

- 200 kW solar array on 0.8–1.2 acres of ground mount (south-facing, 35° tilt) — available at most Zone 5 rural community sites
- 20–40 kW small wind turbine (Bergey Excel 15–40 kW range) at 35–40% winter capacity factor: 7–14 kW average continuous in winter
- 40 kW biogas/diesel generator: dispatchable, runs 4–6 hours/day during worst-case winter operation
- Combined effective continuous capacity during winter worst-case: 25–35 kW from renewables + 40 kW generator = 65–75 kW — sufficient to serve 60 kW critical load while charging battery

---

## Section 2: Capital Cost Estimates (CAPEX)

### System Component Breakdown

**Scenario A: Minimum Viable Microgrid** (critical facilities only: clinic, fire station, water pump, community hall)

| Component | Quantity | Unit cost | Subtotal |
|---|---|---|---|
| Solar array (80 kW, ground mount) | 1 | $80,000–$120,000 | $80,000–$120,000 |
| GFM string inverters (4× 20 kW SMA/Schneider) | 4 | $5,000–$9,000 | $20,000–$36,000 |
| LiFePO4 battery bank (400 kWh, containerized) | 1 | $50,000–$130,000 | $50,000–$130,000 |
| Diesel/biogas backup generator (40 kW) | 1 | $25,000–$40,000 | $25,000–$40,000 |
| Microgrid controller + transfer switch | 1 | $20,000–$50,000 | $20,000–$50,000 |
| DC bus wiring and protection | — | — | $10,000–$20,000 |
| AC distribution connections (4 facilities) | — | — | $30,000–$60,000 |
| Engineering and commissioning | — | — | $50,000–$80,000 |
| Permitting and interconnection fees | — | — | $10,000–$25,000 |
| **Scenario A Total** | | | **$295,000–$561,000** |

**Scenario B: Full Community Microgrid** (critical facilities + partial residential coverage)

| Component | Quantity | Unit cost | Subtotal |
|---|---|---|---|
| Solar array (200 kW, ground mount) | 1 | $160,000–$240,000 | $160,000–$240,000 |
| GFM inverters (200 kW total) | System | $35,000–$65,000 | $35,000–$65,000 |
| LiFePO4 battery bank (1 MWh) | 2× containers | $125,000–$334,000 | $125,000–$334,000 |
| Small wind turbine (20 kW Bergey Excel) | 1 | $60,000–$100,000 | $60,000–$100,000 |
| Diesel/biogas backup generator (40–60 kW) | 1 | $30,000–$50,000 | $30,000–$50,000 |
| Microgrid controller + transfer switches | System | $25,000–$60,000 | $25,000–$60,000 |
| DC bus infrastructure | — | — | $15,000–$30,000 |
| AC distribution to community (feeder upgrade) | — | — | $80,000–$200,000 |
| Monitoring and communication (OpenFMB) | — | — | $15,000–$30,000 |
| Engineering, permitting, commissioning | — | — | $80,000–$130,000 |
| Contingency (10%) | — | — | $62,500–$123,900 |
| **Scenario B Total** | | | **$687,500–$1,362,900** |

**Scenario C: Full System with Long-Duration Storage Retrofit (2028–2029)**

Scenario B, plus addition of 500 kWh Form Energy iron-air long-duration storage at $77–$100/kWh commercial scale:
- Iron-air battery addition: $38,500–$50,000 (500 kWh × $77–$100/kWh)
- Integration and controls: $15,000–$25,000
- **Scenario C addition**: $53,500–$75,000
- **Scenario C Total**: $741,000–$1,438,000

### Grant and Incentive Impact

With available incentives applied to Scenario B:
- USDA REAP grant (if open; 25–50% of system cost up to $1M): $171,875–$500,000
- Section 48E commercial storage credit (30% of battery system, cooperative/nonprofit entity): $37,500–$100,200
- Illinois ComEd/Ameren DG rebate ($300/kW solar + $300/kWh storage): $60,000 solar + $300,000 storage = $360,000 (Illinois only)
- Wisconsin Focus on Energy ($150/kW + $150/kWh): $30,000 solar + $150,000 storage = $180,000 (Wisconsin only)
- **Estimated net community cost (Illinois + all incentives): $0–$300,000 for Scenario B** — at favorable incentive combination, community cost approaches zero
- **Estimated net community cost (Zone 5 average, without Illinois-specific rebates): $300,000–$800,000**

**Per-capita cost** (100 persons, Scenario B, 20-year life):
- Before grants: $6,875–$13,629
- After grants (Illinois environment): $0–$3,000
- After grants (Zone 5 average): $3,000–$8,000

---

## Section 3: Community Governance Model

### Cooperative Model (Recommended)

A rural electric cooperative (REC) is the most natural legal structure for a Zone 5 community microgrid. All five Zone 5 states have established cooperative law frameworks. Key elements:

**Formation**: Articles of incorporation as a nonprofit cooperative under state cooperative statutes (e.g., Illinois Cooperative Act, Michigan Cooperative Association Act). Timeline: 3–6 months with legal counsel. Cost: $3,000–$10,000 in legal fees.

**Governance structure**:
- Member households and businesses are voting members (one member, one vote)
- Elected board of directors (5–9 members): responsible for major financial decisions, long-term agreements, personnel
- Operations manager (paid or volunteer): day-to-day dispatch, maintenance coordination, member communication
- Technical committee: engineers and technically capable members who oversee commissioning, O&M decisions, and expansion planning

**Financial structure**:
- Member equity: each member purchases a membership share ($500–$2,000 range) at formation
- Project financing: combination of grants (REAP), tax-equity arrangements for Section 48E credit, cooperative bonds or rural development loans for remainder
- Revenue: electricity bill savings for members, potential wholesale market revenue (FERC 2222, post-2029), grid services revenue from utility for frequency regulation and demand response

**Conflict resolution**: Adopt explicit conflict resolution bylaws referencing Phase 4's dispute resolution protocols. Key decisions requiring supermajority (75%+): taking on debt above X threshold, changing the rate structure, dissolving the cooperative. All other decisions by simple majority.

### Municipal Utility Model

If a Zone 5 community is incorporated as a village or township, a municipal utility authority can be formed by ordinance. Advantages: legal authority to issue municipal bonds at favorable rates, tax-exempt financing, existing staff to manage O&M. Disadvantages: elected governance can be less technically competent than cooperative model; political transitions can disrupt long-term projects.

### Nonprofit Model

A 501(c)(3) nonprofit energy organization qualifies for Section 48E direct-pay provisions (allows nonprofits to receive the tax credit as a direct payment from the IRS rather than offsetting tax liability). This is advantageous if the community does not have sufficient tax burden to use tax equity. Formation timeline: 6–12 months (IRS determination). Cost: $5,000–$15,000 in legal and filing fees.

### Governance Decision for Phase 5

The Phase 4 Framework's sequencing principle applies: establish the cooperative or nonprofit entity before commissioning any engineering study. The legal entity formation is Phase 1 in the implementation timeline below. Without it, no grant applications can be submitted and no interconnection agreement can be signed.

---

## Section 4: 18-Month Implementation Timeline

### Phase 1 — Governance and Feasibility (Months 1–4)

**Actions**:
- Form legal entity (cooperative, nonprofit, or municipal authority): retain legal counsel, draft bylaws, file articles of incorporation
- Hold founding member meeting: ratify governance structure, elect interim board, define geographic scope
- Commission community energy audit: document all loads (kW demand, kWh annual, seasonal patterns), identify critical facilities
- Run HOMER Energy model with PVWatts data for community location: generate 3 system sizing scenarios (minimum viable, full community, phased)
- Schedule pre-application meeting with utility interconnection department: understand timeline, study requirements, and any known constraints on the distribution feeder

**Resources required**: Legal counsel ($3,000–$10,000), part-time project coordinator (volunteer or contractor, $0–$15,000), HOMER Energy license ($1,500–$3,000), energy audit ($5,000–$15,000)

**Go/no-go decision point**: At month 4, the board reviews the HOMER output, preliminary cost estimate, and utility pre-application findings. Decision: proceed to full engineering design, pause to secure additional funding, or select a smaller initial scope.

### Phase 2 — Engineering Design and Interconnection Application (Months 4–10)

**Actions**:
- Hire power systems engineering firm experienced with GFM inverter microgrids (muGrid Analytics, Clean Coalition, or similar)
- Engineering deliverables: one-line diagrams, protection coordination study, power flow analysis (OpenDSS or PSCAD), equipment specifications, construction drawings
- File utility interconnection application: initiate utility-side feasibility study (60–90 days) and system impact study if required (additional 90–120 days)
- Submit REAP grant application (if open) — this is time-sensitive; do not wait for engineering to be complete before submitting
- Apply to DOE C-MAP (Community Microgrid Assistance Partnership) if eligible: underserved, rural, or Indigenous community
- Apply to state rebate programs: Illinois CEJA DG rebates, Michigan MPSC programs, Wisconsin Focus on Energy

**Critical path note**: Utility interconnection approval is the longest-duration item and cannot be shortened by paying more. Start the interconnection application as early in Phase 2 as possible — the earlier it is filed, the earlier the clock starts. Delays in this phase are the primary reason community microgrid projects miss their target commissioning dates.

**Resources required**: Engineering firm ($50,000–$130,000), grant writing support ($5,000–$20,000), legal counsel for utility agreement ($5,000–$15,000)

### Phase 3 — Procurement (Months 8–14)

**Actions**:
- Issue Request for Proposals (RFP) to solar EPC contractors: specify GFM inverters, LiFePO4 battery brand and specification, OpenFMB-compatible controller
- Evaluate bids: score on technical compliance, contractor experience with GFM microgrids, warranty terms, local installer qualifications
- Execute interconnection agreement with utility (when approved — do not order equipment before this is signed)
- Order long-lead equipment: GFM inverters (8–16 weeks lead time), LiFePO4 containers (10–20 weeks), wind turbine (12–20 weeks)
- Secure all permits: building, electrical, environmental (stormwater for ground mount), county/township approvals

**Critical path note**: The interconnection agreement signature is the procurement release gate. Equipment ordered before interconnection approval creates inventory risk if the application is denied or modified. Coordinate procurement to align with expected interconnection approval date.

**Resources required**: EPC contractor selection, legal review of EPC contract ($3,000–$8,000), $100,000–$200,000 deposit on equipment (typically 30–50% of equipment cost)

### Phase 4 — Installation (Months 12–17)

**Actions**:
- Site preparation: concrete pads for battery containers and generator, mounting foundations for solar arrays and wind tower, conduit trenching
- Electrical installation: DC bus wiring, inverter mounting, battery container connections, transfer switch installation, feeder connections to existing buildings
- Microgrid controller installation and configuration: program load shedding tiers, droop control setpoints, ROCOF thresholds, black start sequence
- OpenFMB configuration: set up MQTT broker, configure DER data points, test data exchange between controller and inverters
- OpenADR 3.0 integration (if utility offers demand response program): configure load controllers for water heater, cold storage, and agricultural loads

**Resources required**: EPC contractor labor ($80,000–$150,000 in the Scenario B estimate above); community volunteers for site preparation and non-licensed work can reduce labor cost by $10,000–$25,000

### Phase 5 — Commissioning and Training (Months 16–18)

**Actions**:
- Factory acceptance testing (FAT) for microgrid controller: verify setpoints, load shedding logic, black start sequence with vendor before field deployment
- Field commissioning: energize circuits in sequence (generator → controller → battery → solar → loads), tune droop setpoints, verify protection relay coordination
- Intentional islanding test: with utility coordination, open the PCC switch and verify microgrid maintains voltage/frequency within ±5% for >30 minutes
- Load bank testing: apply artificial loads to verify load shedding tiers operate correctly at 80%, 60%, 40%, 20% battery state of charge
- Operator training: minimum two community members trained on black start procedure, load shedding manual override, battery state monitoring, routine maintenance inspection
- Document and submit to DOE C-MAP / EESI for national knowledge base

**Success gate**: First successful intentional island test, sustained for minimum 24 hours, serving all Tier 1 critical loads, with battery state of charge remaining above 40% at test conclusion.

### Phase 6 — Ongoing Operation (Month 18+)

**Actions**:
- Monthly reporting to cooperative members: energy generated, grid outages prevented, battery state of health, financial performance
- Annual battery capacity test: measure actual vs. rated capacity; plan cell replacement if capacity falls below 80% of original
- Year 2 planning: assess whether to add second microgrid site (school, agricultural cooperative), connect via OpenFMB peer-to-peer coordination
- Year 3–4 planning: evaluate Form Energy iron-air retrofit ($77–$100/kWh) for extending winter autonomy without generator reliance
- Year 5: reassess cooperative membership, evaluate expansion to 200-person scale if community demand warrants

---

## Section 5: Prerequisite Phase 4 Modules

The Phase 4 Framework identified energy infrastructure as fifth in the governance → information → food → security → energy implementation sequence. The following Phase 4 governance and infrastructure modules must be operational before microgrid commissioning:

**Required before microgrid formation**:
- Phase 4 Governance Module: decision-making authority structure (who approves contracts, who can encumber the community's finances)
- Phase 4 Information Infrastructure Module: communications system (the microgrid's monitoring dashboard requires internet or radio backhaul to notify operators of faults)
- Phase 4 Conflict Resolution Module: explicit procedures for disputes between microgrid members (these will occur and must have a resolution path before they arise)

**Required before full commissioning**:
- Phase 4 Security Module: physical security for battery enclosures and generator — these are high-value, theft-attracting assets in a rural setting
- Phase 5 Wave 1 Household Coordination: if household-scale inverters are planned as contributions to the community microgrid, Phase 5 Wave 1's household energy protocols must be in place to coordinate individual system settings

---

## Section 6: Success Metrics

| Metric | Baseline (Year 0) | Target (Year 1) | Target (Year 3) |
|---|---|---|---|
| Days of autonomy (critical loads) | 0 days | 5+ days (winter design basis) | 7+ days |
| Grid outage events served (>2 hours) | 0 | All events ≤ 5-day duration | All events ≤ 10-day duration |
| Renewable fraction (annual) | 0% | 70%+ | 85%+ |
| Levelized cost of energy (LCOE) | Utility rate ($0.12–0.18/kWh) | <$0.15/kWh | <$0.12/kWh |
| Battery state of health (SoH) | 100% | >95% | >90% |
| Community adoption rate (% members enrolled in cooperative) | 0% | 80%+ | 95%+ |
| Operator training completion | 0 | 2 trained operators | 4 trained operators |
| Generator operating hours per year | N/A | <300 hours | <150 hours |
| Carbon emissions (tCO2e/year, grid-connected baseline) | ~200 tCO2e | ~60 tCO2e | ~30 tCO2e |

**The most important metric is community adoption rate.** A technically perfect microgrid that 40% of community members refuse to join or fund is a failed project. The cooperative governance model, transparent monthly reporting, and explicit conflict resolution procedures are the tools that drive adoption above 80%. Technical excellence matters; but governance success determines whether the project sustains through personnel turnover, financial stress, and the inevitable first major outage event.

---

## Summary: Is This Feasible?

**Yes, with conditions.**

A Zone 5 community of 50–100 people can commission a 200 kW / 1 MWh hybrid microgrid within 18 months and within a $700K–$1.4M capital budget (before grants). With Illinois CEJA incentives, USDA REAP grants (when open), and Section 48E storage credits, the net community cost can fall to $0–$300,000. The technology is proven, the regulatory pathway is established, and the Zone 5 ecosystem of cooperatives, engineering firms (muGrid Analytics, Clean Coalition), and federal programs (DOE C-MAP, NRECA CARED) provides direct support.

The three conditions for success:

1. **Governance first**: Form the cooperative or nonprofit entity before any engineering work. Six months of governance formation delays are cheaper than six months of contract disputes with no legal signatory.

2. **Cooperative utility territory**: Pursue sites within rural electric cooperative territory rather than investor-owned utility territory. The interconnection timeline and cost difference is 6–12 months and $20,000–$60,000.

3. **Phased scope**: Start with Scenario A (critical facilities: clinic, fire station, water, community hall) in Phase 1. Expand to Scenario B (broader community coverage) in Phase 2. Plan for Scenario C (long-duration storage retrofit) in Phase 3. A microgrid that serves 4 critical facilities is operationally valuable on day one; a microgrid design that encompasses 100% of community load may never reach commissioning due to scope and capital requirements.

**June 1 decision recommendation**: Authorize feasibility study (HOMER Energy model + utility pre-application meeting) and legal entity formation simultaneously, in parallel. Both can proceed independently and both are required before a go/no-go on full engineering design.
