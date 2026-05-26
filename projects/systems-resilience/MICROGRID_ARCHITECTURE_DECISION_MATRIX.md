---
title: "Microgrid Architecture Decision Matrix — Zone 5 (Midwest) 6-Topology Comparison"
project: systems-resilience
phase: 5
wave: 2
status: production
created: 2026-05-26
word_count: ~2800
decision_gate: "June 1, 2026 — architecture selection for Phase 5 community microgrid"
audience: "Community infrastructure decision-makers and technical leads"
cross_references:
  - PHASE_5_WAVE_2_MICROGRIDS_RESEARCH_OUTLINE.md
  - PHASE_5_WAVE_2_MICROGRIDS_RESEARCH.md
  - PHASE_5_WAVE_2_MICROGRIDS_IMPLEMENTATION_SKETCH.md
---

# Microgrid Architecture Decision Matrix — Zone 5 (Midwest)

> **Decision scope**: Architecture selection for a Zone 5 community of 50–500 people  
> **Primary constraint**: 72–120-hour winter grid-down resilience  
> **Secondary constraint**: Capital cost within $2.5–5M total system budget  
> **Regulatory context**: Zone 5 states (IL, MI, IA, IN, WI), rural electric cooperative territory preferred

---

## How to Use This Matrix

This matrix evaluates six microgrid architecture typologies against Zone 5-specific conditions. Each option is scored on six dimensions, with detailed rationale and cost drivers. The recommendation is stated at the end, but the matrix is designed to remain useful if community constraints differ from the baseline assumptions.

**Scoring conventions used below**:
- Zone 5 Fit: Very High / High / Medium / Low / Very Low
- Costs are 2025–2026 figures; apply 3–5% annual escalation for planning beyond 2027
- "Community scale" in this matrix means 50–500 people, 80–300 kW continuous generation, 400–2,000 kWh storage

---

## Option A: AC Islanding Network

**Architecture**: 480V three-phase backbone connecting all generation and large loads; residential loads served via step-down transformers (480V → 120/240V). Grid-following or grid-forming inverters convert DC from solar and batteries to AC. Single or redundant microgrid controller at the point of common coupling (PCC) manages islanding.

**Technical Specifications**:
- Voltage: 480V/277V three-phase backbone (standard utility distribution voltage for farms and commercial loads)
- Islanding detection: Frequency/voltage monitoring at PCC; ROCOF or phase-angle jump passive detection; optional active detection (Sandia Frequency Shift)
- Inverter type: String or central inverters (grid-following for grid-connected mode; requires separate grid-forming capability for island mode via dedicated island-forming unit or GFM-capable string inverters)
- Control: Centralized EMS at the PCC; optional droop control at each inverter for decentralized backup

**Capital Cost (100-person community, 100 kW solar + 40 kW generator + 400 kWh storage)**:
- Solar array (100 kW): $80,000–$120,000
- Inverters: $15,000–$30,000 (string inverters at $0.15–0.30/W installed)
- Step-down transformers (480V → 120/240V): $5,000–$20,000 per transformer; 2–4 transformers needed: $10,000–$80,000 total
- Battery storage (400 kWh LiFePO4): $50,000–$130,000
- Backup generator (40 kW): $25,000–$40,000
- Microgrid controller + transfer switch: $20,000–$50,000
- Electrical installation labor: $80,000–$150,000
- **Estimated total**: $280,000–$570,000 (before grants)

**Pros**:
- Standard utility equipment familiar to all Zone 5 electricians and utility interconnection staff
- Transformer-isolated fault zones: a fault on one branch does not propagate to others
- Large installer pool reduces procurement risk and O&M costs
- Well-understood regulatory pathway through IEEE 1547-2018 interconnection process
- Supports all existing agricultural motor loads (pumps, grain dryers) without modification

**Cons**:
- Higher transformer cost for residential step-down ($10,000–$80,000 incremental)
- Central controller is a single point of failure unless redundant units are installed ($5,000–$15,000 for backup controller)
- 10–15% conversion losses from DC-to-AC inversion at every solar/battery interface
- Centralized architecture scales poorly above 500 kW without redesign

**Zone 5 Fit: Medium**

Rationale: Option A is the lowest-risk entry point for communities with existing grid-tied wiring and no technical staff on-site. It is the familiar architecture for Zone 5 utilities and electricians. The transformer cost and conversion losses are real disadvantages, but the reduced commissioning complexity and installation risk are valuable for first-time community microgrid projects. Recommended for communities prioritizing simplicity and the largest possible installer pool over long-term efficiency.

**Best community profile**: Rural town with existing 480V agricultural wiring, no technical staff, relationship with a cooperative utility, and a first-phase focus on critical facility backup (fire station, clinic, community hall) rather than whole-community coverage.

---

## Option B: DC Microgrid

**Architecture**: 48V DC bus (small systems) or 380–400V DC bus (building-scale systems) connecting all generation, storage, and DC loads directly. AC loads served through DC-to-AC inverters at point of use. No large central AC distribution transformer.

**Technical Specifications**:
- Voltage: 48V DC (household scale, residential battery banks) or 380–400V DC (emerging building standard, IEEE 2030.10-2021)
- Islanding: Simpler than AC (no frequency reference needed); voltage-based protection at DC bus
- Inverter type: Bidirectional DC-DC converters (battery ↔ bus), DC-AC inverters at each AC load point
- Control: Master controller on DC bus monitors voltage; droop control is straightforward (voltage droop replaces frequency droop)

**Capital Cost (100-person community, 100 kW solar + 400 kWh storage — new construction only)**:
- Solar array: $80,000–$120,000 (identical to Option A — DC arrays are native to DC bus)
- DC-DC converters (battery charge controllers): $15,000–$30,000
- DC-rated breakers and switchgear: 30–50% premium over AC equipment: $10,000–$25,000 incremental
- DC-AC inverters at each building (point-of-use): $20,000–$50,000 for 4–6 buildings
- Battery storage (400 kWh): $50,000–$130,000 (identical to Option A)
- Building wiring upgrades to DC-compatible: $30,000–$80,000 per building for existing wiring retrofit
- **Estimated total (new construction)**: $220,000–$450,000
- **Estimated total (existing building retrofit)**: $350,000–$700,000+

**Pros**:
- Solar panels and batteries are natively DC — no conversion losses in the generation/storage layer (3–5% total losses vs. 15% for Option A)
- Simplified island mode: voltage-based control eliminates frequency synchronization complexity
- Ideal for new-construction communities with modern DC loads (LED lighting, electronics, EV charging)
- Battery direct-connect to DC bus reduces number of conversion stages, improving round-trip efficiency

**Cons**:
- Requires DC-rated breakers and disconnects (still niche in Zone 5; limited supplier pool; premium pricing)
- Incompatible with most existing agricultural motor loads (pumps, grain dryers, dairy equipment) without DC motor replacements or DC drives — significant retrofit cost
- Very limited installer pool in Zone 5: DC microgrid design and commissioning expertise is rare outside major metro areas
- Insurance complications: most Zone 5 rural property insurance does not have standard underwriting for DC distribution systems
- No Zone 5 community deployments documented as of May 2026; limited local regulatory precedent

**Zone 5 Fit: Low to Medium**

Rationale: Option B is technically elegant and the right architecture for purpose-built new communities with modern DC-native loads. For Zone 5 communities with existing farm buildings, aged wiring, and motor-heavy agricultural loads, it is currently impractical. DC microgrids at the building scale (48V for a single new-construction homestead) are the appropriate application, not community-scale retrofit projects. Revisit in 3–5 years as DC equipment ecosystem matures.

**Best community profile**: New-construction intentional community on greenfield land, with technical founders capable of commissioning novel systems and a plan to build all loads from scratch to DC standards.

---

## Option C: Hybrid AC/DC Microgrid (Recommended)

**Architecture**: A bidirectional DC bus at 48V or 400V collects solar and battery DC power. A 480V/120/240V AC bus serves standard loads. Bidirectional interlinking converters (BIC) — also called bidirectional inverters or grid-forming inverters — bridge the buses. The AC bus can operate in grid-connected mode (synchronized to utility) or island mode (frequency and voltage maintained by the GFM inverters without utility reference).

**Technical Specifications**:
- DC bus voltage: 48V (household/small-community scale) or 400V (commercial scale, preferred for 80+ kW systems)
- AC bus voltage: 480V/277V three-phase (agricultural/commercial loads) + 120/240V residential
- Inverter type: Grid-forming (GFM) bidirectional inverters — SMA Sunny Island, Schneider Electric XW+, Victron Quattro, Enphase IQ8 (residential scale)
- Islanding: GFM inverters establish voltage/frequency reference independently; island transfer <50 milliseconds; no generator required for island initialization if battery is charged
- Control: Decentralized droop control at each GFM inverter + site-level EMS for optimization and monitoring

**Capital Cost (100-person community, 100 kW solar + 20 kW wind + 400 kWh storage + 40 kW generator)**:
- Solar array (100 kW): $80,000–$120,000
- GFM inverter/BIC system: $25,000–$50,000 (premium over standard inverters: 15–20%)
- DC bus wiring and protection: $10,000–$25,000
- Battery storage (400 kWh LiFePO4): $50,000–$130,000
- Wind turbine (20 kW): $60,000–$100,000
- Backup generator (40 kW): $25,000–$40,000
- AC distribution and existing load connections: $30,000–$60,000
- Microgrid controller + monitoring: $15,000–$35,000
- Electrical installation labor: $80,000–$150,000
- **Estimated total**: $375,000–$710,000 (before grants)

**Pros**:
- Best overall efficiency: 5–8% total conversion losses vs. 15% for pure AC
- Works with all existing AC loads (motor pumps, grain dryers, dairy equipment) AND native DC generation/storage — no load replacement required
- GFM inverters enable true island operation without generator running: <50ms transfer, battery-backed frequency/voltage reference
- Phased migration path: start with AC backbone, add DC bus and GFM inverters as budget allows
- Validated at Bayfield County (Wisconsin) and UC San Diego deployments — the most proven architecture for Zone 5-scale communities
- Scalable: modular GFM inverter stacks can grow from 50 kW to 500+ kW without architectural redesign

**Cons**:
- More complex commissioning than pure AC: requires power systems engineer experienced with GFM inverter droop tuning and DC bus protection coordination
- GFM inverters carry a 15–20% cost premium over standard grid-following inverters
- Dual-bus architecture requires more detailed protection coordination study before utility interconnection
- Installer pool smaller than pure-AC: requires contractors certified on specific GFM inverter platforms (SMA, Schneider, Victron)

**Zone 5 Fit: Very High**

Rationale: Option C is the validated production architecture for Zone 5 community microgrids. The Bayfield County deployment — the most Zone 5-relevant case study — uses this architecture. GFM inverters are now commercially mature (SMA Sunny Island has been in production for 15+ years; Enphase IQ8 received UL 1741 3rd-edition certification December 2025). The 15–20% inverter cost premium is justified by the islanding capability it enables. This is the Phase 5 recommendation.

**Best community profile**: Any Zone 5 rural community of 50–500 people with existing infrastructure, mixed AC loads, and a governance structure capable of managing an 18–30 month implementation process. This is the architecture for the June 1 Phase 5 decision.

---

## Option D: Low-Frequency AC (LFAC)

**Architecture**: Distribution at 16.7–50 Hz instead of the US standard 60 Hz. Originally developed for railroad electrification (16.7 Hz is European rail standard). Theoretical advantage: at lower frequencies, skin effect is reduced, allowing smaller-diameter conductors to carry more current over long distances.

**Technical Specifications**:
- Frequency: 16.7–50 Hz (vs. US standard 60 Hz)
- Voltage: Custom-specified; not standardized for community microgrids
- Control: Requires custom power electronics for all loads — no off-the-shelf compatibility
- Islanding: Feasible but entirely custom; no commercial controllers exist for community-scale LFAC

**Capital Cost**: Not quantifiable with available commercial equipment; LFAC at this scale is a research project, not a procurement exercise.

**Pros**:
- Reduced skin effect allows smaller copper cross-section for equivalent current capacity over long distances (>2 km distribution runs)
- Potentially attractive for dispersed rural communities with 1–3 mile distribution spans between generation and loads

**Cons**:
- Custom infrastructure required: no commercial Zone 5 contractors, no commercial controllers, no commercial protection equipment
- All loads require custom frequency converters or replacement with DC-native equipment
- Zero local installer expertise in Zone 5
- No UL listings or IEEE standards for 16.7–50 Hz community microgrids in US context
- Insurance: standard underwriters will not cover non-standard frequency distribution systems

**Zone 5 Fit: Very Low**

Rationale: LFAC is a legitimate research topic with niche applications (long-distance rail, offshore wind collection). It is not commercially viable for Zone 5 community microgrids as of 2026 and will not be for at least 5–10 years. Including it here for completeness; it should not be considered for any near-term Phase 5 deployment.

**Best community profile**: None currently applicable. Monitor for 2030+ if rural distribution distances exceed 3 miles and DC alternatives remain expensive.

---

## Option E: Radial AC with Centralized BESS Hub

**Architecture**: Traditional utility radial distribution topology — a single large Battery Energy Storage System (BESS) at a central hub point on the distribution feeder acts as the microgrid anchor. Solar generation may be distributed along the feeder or co-located with the BESS. The BESS provides grid services (frequency regulation, voltage support) when grid-connected and becomes the island reference when grid-disconnected.

**Technical Specifications**:
- Voltage: Standard utility 4kV–34.5 kV primary distribution, stepped down to 120/240V or 480V at service points
- Islanding: BESS at hub establishes voltage/frequency reference; simpler control logic than distributed architectures; island detection by monitoring PCC (single point)
- Battery type: Utility-scale BESS, typically containerized (Fluence, Tesla Megapack, LG ESS): 500 kWh–2 MWh per container
- Control: Centralized BESS management system (vendor-proprietary plus IEC 61850)

**Capital Cost (100-person community, 200 kW solar distributed + 1 MWh centralized BESS + 100 kW generator)**:
- Distributed solar (200 kW along feeder): $160,000–$240,000
- Centralized 1 MWh BESS (utility-scale containerized): $125,000–$334,000 (NREL 2025 benchmark)
- Grid interconnection and protection: $30,000–$80,000
- Generator backup: $40,000–$70,000
- Controls and monitoring: $20,000–$40,000
- Installation labor and civil works: $100,000–$200,000
- **Estimated total**: $475,000–$964,000

**Pros**:
- Uses standard utility-scale equipment with established procurement and installation pathways
- Single BESS centralizes control logic — simpler EMS design
- Utility-scale pricing for BESS ($125–$334/kWh) is significantly lower than residential scale ($700–$1,300/kWh)
- Most familiar architecture for Zone 5 utilities' interconnection engineers

**Cons**:
- Single point of failure: if the central BESS fails, the entire microgrid loses islanding capability
- Centralized control bottleneck: BESS management system failure during an outage disables distributed solar's ability to serve loads
- Scalability constraint: adding more load requires central BESS upgrade (cannot modularly expand)
- Not suitable for communities with geographically dispersed loads over 1–2 mile radius without significant primary feeder investment
- Centralized BESS enclosures require fire suppression and HVAC (10–15% of BESS capital)

**Zone 5 Fit: Medium**

Rationale: Option E is appropriate as a fallback for communities with limited distributed generation and a desire to leverage utility-scale economics for storage. It is used by many utility-sponsored community resilience programs (including some NRECA cooperative models). The single-point-of-failure concern is the primary disadvantage. Mitigation: specify N+1 redundancy in the BESS (two 500 kWh containers rather than one 1 MWh container, with independent BMS). This adds 20–30% to BESS capital but eliminates the reliability concern.

**Best community profile**: Community with one or two large existing loads (cooperative grain elevator, dairy processing facility) that anchors the load center, with generation potentially co-located at the same site. Suitable where installation of distributed GFM inverters would require significant wiring upgrades.

---

## Option F: Modular Nested Microgrids

**Architecture**: Tiered architecture — household-scale microgrids (individual homes with solar + battery) federate into block-scale microgrids (8–15 homes), which federate into district-scale microgrids (the community). Each tier operates independently but can share power across tiers when generation or storage is abundant in one tier. Communication between tiers uses OpenFMB or proprietary protocols. Hierarchical control: household EMS → block coordinator → district EMS.

**Technical Specifications**:
- Household scale: 3–10 kW solar, 10–20 kWh LiFePO4, GFM microinverter (Enphase IQ8 or equivalent)
- Block scale: 50–100 kW shared solar, 100–200 kWh shared storage, block coordinator controller
- District scale: 100–300 kW shared solar, 400–800 kWh shared storage, 40–80 kW generator, district EMS
- Inverter type: Smart GFM inverters required at all tiers (15–20% cost premium)
- Communication: OpenFMB between tiers; IEC 61850 for utility interconnection at district level
- Control: Hierarchical EMS — district coordinates blocks, blocks coordinate households; each layer operates autonomously if upper layer fails

**Capital Cost (100-person community across 4 blocks of 25 people each)**:
- 40 household systems (3 kW solar + 10 kWh battery each): $40,000 × 40 = $1,600,000 (at $700–$1,300/kWh for residential-scale battery)
- 4 block-scale systems (80 kW solar + 200 kWh storage each): $120,000 × 4 = $480,000
- 1 district-scale system (100 kW solar + 400 kWh storage + 40 kW generator): $350,000–$550,000
- Block and district communication infrastructure: $30,000–$60,000
- **Estimated total**: $2,460,000–$2,640,000+

Note: household-scale costs dominate. If household systems are individually financed (homeowner ownership), the community-financed portion is $860,000–$1,110,000 for block + district tiers only.

**Pros**:
- Maximum fault isolation: a fault at one household or block does not affect other blocks
- Scalable: community can start with district tier (Phase 1), add block tier (Phase 2), integrate household tier (Phase 3) as households upgrade
- Community-aligned granularity: each household retains energy autonomy as a floor even if upper tiers fail
- Aligns with Phase 5's household → community → regional scaling model
- ORNL multi-microgrid orchestrator (demonstrated in Vieques, Puerto Rico) enables peer-to-peer power sharing between blocks without central coordinator

**Cons**:
- Most expensive per capita: $2,460,000+ for 100 people = $24,600/person (before grants)
- Complex multi-layer control: requires software engineering expertise to commission and maintain the EMS stack across three tiers
- Synchronization overhead: sharing power between tiers requires frequency/voltage synchronization coordination, which adds latency and failure modes
- Smart inverters at all tiers add 15–20% cost premium vs. standard inverters
- Longest implementation timeline: 30–48 months for full tier deployment

**Zone 5 Fit: High (with phased implementation)**

Rationale: Option F has the highest theoretical resilience — no single failure cascades beyond its tier — and the best alignment with Phase 5's layered architecture. The cost concern is manageable if household-scale systems are individually financed and the community treasury only funds block + district tiers. The control complexity concern is real but manageable if standard GFM inverter platforms (Enphase IQ8, SMA Sunny Island) are used consistently across tiers rather than mixing vendors.

**Best community profile**: Communities willing to implement over 3–5 years with phased investment. Ideal if community members are already considering household-scale solar+battery upgrades (the household investments serve double duty as both individual resilience and microgrid building blocks). Requires a technical coordinator who understands multi-tier EMS integration.

---

## Comparative Summary Table

| Dimension | A: AC Islanding | B: DC Microgrid | C: Hybrid AC/DC | D: LFAC | E: Radial + BESS | F: Modular Nested |
|---|---|---|---|---|---|---|
| Zone 5 Fit | Medium | Low–Med | **Very High** | Very Low | Medium | High |
| Estimated CAPEX (100-person) | $280K–$570K | $350K–$700K | $375K–$710K | N/A | $475K–$964K | $860K–$1.1M (community tiers) |
| CAPEX per kW (continuous) | $2,800–$5,700 | $3,500–$7,000 | $3,750–$7,100 | N/A | $2,375–$4,820 | $4,300–$5,500 |
| Conversion efficiency | 85–90% | 95–97% | 92–95% | N/A | 88–92% | 90–95% |
| Islanding transfer time | 100–500 ms | <50 ms | <50 ms | N/A | 100–500 ms | 50–200 ms per tier |
| 120-hour winter resilience | Moderate | High (new) | High | N/A | Moderate | Very High |
| Installer pool (Zone 5) | Large | Very small | Medium | None | Medium–Large | Medium |
| Regulatory complexity | Low | High | Medium | Very High | Low–Med | Medium–High |
| Scalability (50→500 people) | Low | Low | High | Very Low | Medium | Very High |
| Single-point-of-failure risk | Medium | Low | Low | N/A | High | Very Low |
| Commissioning timeline | 18–24 months | 24–40 months | 18–30 months | N/A | 18–30 months | 30–48 months (full) |
| Recommended for Phase 5 | Fallback | No | **Yes** | No | Conditional | Conditional |

---

## Recommendation

**Primary recommendation: Option C (Hybrid AC/DC) for Phase 5 implementation.**

The evidence from Zone 5 deployments (Bayfield County), engineering literature, and comparative cost analysis converges on Option C as the correct architecture for the June 1 decision. It achieves Very High Zone 5 Fit across all evaluation dimensions, uses commercially mature equipment, has a medium-sized but qualified installer pool, and is the architecture used by muGrid Analytics — the firm that designed the nearest Zone 5 case study.

**Conditional secondary recommendation: Option F (Modular Nested) for communities with 3–5 year implementation horizon and household-level investment coordination capability.** If the community can coordinate household-scale solar+battery purchases alongside the community tier, Option F's layered resilience is superior. The implementation complexity is real but manageable with consistent GFM inverter platform selection.

**Fallback: Option A (AC Islanding) if installer availability or budget constraints make Option C infeasible.** Option A foregoes efficiency but uses the largest installer pool and simplest regulatory pathway. Acceptable for Phase 1 critical-facility-only coverage while Option C is procured for Phase 2 full-community build-out.

**Do not implement**: Option D (LFAC) or Option B (DC) for existing-infrastructure Zone 5 communities in the current technology cycle.

---

## Decision Checklist for June 1

Before selecting an architecture on June 1, confirm the following:

1. **Governance entity established?** The selected architecture requires a signing authority. If no cooperative or municipal entity exists, governance formation takes 3–6 months and is the first-priority action regardless of architecture choice.
2. **Utility territory identified?** Investor-owned utility (ComEd, DTE, Indiana Michigan Power) vs. rural electric cooperative (Bayfield Electric, NRECA member) affects interconnection timeline by 6–12 months. Cooperative territory strongly preferred for Option C.
3. **REAP grant status confirmed?** Applications were paused as of May 2026. If REAP is reopening, submit within first available window — do not delay engineering for grant status.
4. **Site-specific load audit completed?** CAPEX estimates above are planning-level. A $5,000–$15,000 professional energy audit of actual loads, seasonal patterns, and critical load identification is required before engineering design begins.
5. **GFM inverter procurement lead time checked?** SMA and Schneider GFM inverters carry 8–16 week lead times; Enphase IQ8 is generally available within 4 weeks. Account for this in the installation schedule.
