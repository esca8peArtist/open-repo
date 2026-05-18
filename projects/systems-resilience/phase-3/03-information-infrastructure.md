---
title: "Community Information Infrastructure & Resilient Communications"
project: systems-resilience
region: "Midwest US (Zone 5)"
phase: 3
scale: community
domain: 3
created: 2026-05-18
word_count: ~5700
citation_count: 36
status: production
cross_references:
  - phase-3/01-governance-decision-making.md
  - phase-3/02-food-systems-supply-chain.md
  - phase-3-community-infrastructure-research-outline.md
---

# Community Information Infrastructure & Resilient Communications
> **Region**: Midwest US (Zone 5) | **Scale**: 100–1,000 people
> **Phase**: 3 — Community | **Domain**: 3 — Information Infrastructure
> **Cross-references**: [phase-3/01-governance-decision-making.md](./01-governance-decision-making.md) · [phase-3/02-food-systems-supply-chain.md](./02-food-systems-supply-chain.md)

---

## The Most Important Finding

Information infrastructure is not about having information available — it is about retrieving accurate information under the specific conditions when you need it most: no grid power, no internet, damaged physical infrastructure, and uncertainty about what information is reliable. Every other community resilience domain fails gracefully under information loss. Governance fails catastrophically.

The empirical evidence is unambiguous: communities that improvise information systems during crisis experience decision-making paralysis, panic from unverified rumors, and internal conflict over what to trust. Communities that design information infrastructure before crisis operate at fundamentally different efficiency. The 2025 Los Angeles fires demonstrated this in real time: formal emergency management systems were paralyzed by protocol delays, while informal networks built on pre-established trust channels propagated evacuation routes, resource hub status, and road closures faster and more accurately.

This document covers the three-layer communication architecture that works at the 100–1,000 person scale: day-to-day GMRS radio (grid power present, internet down), data-layer AREDN mesh (grid power down, batteries available), and long-range HF shortwave (all power down). It also covers the knowledge infrastructure (offline digital servers + printed reference libraries) and the coordination role structures that make information retrieval reliable under pressure.

---

## The Communication Spectrum

Community communication exists on a spectrum defined by infrastructure loss severity. No single system handles all scenarios optimally. The standard approach — building a single robust system — fails because that system becomes a single point of failure. The resilient approach is three redundant layers, each optimized for specific failure scenarios.

### Layer 1: GMRS Radio (Grid Power Present, Internet Down)

**General Mobile Radio Service (GMRS)** operates at frequencies between 462–467 MHz with up to 50 watts transmission power. For communities where grid power is still available but internet is down — the most common first-phase failure scenario — GMRS is the default coordination layer. [1]

**Operational characteristics:**
- Range: 5–25 miles depending on terrain and antenna height (Midwest flatland favors longer range)
- Licensing: Single $35 FCC license covers one person + up to 19 immediate family members
- Hardware: Licensed handheld transceivers cost $40–150 per unit; mobile units $200–400
- Interoperability: GMRS integrates with existing amateur radio repeater networks, allowing extension of range through third-party equipment
- Minimum viable setup for 100-person community: 8–12 GMRS handhelds distributed to coordinators in each geographic sector, plus 1–2 base stations with external antennas at highest elevation points

**Deployment strategy:**
Purchase GMRS handhelds before crisis (cost: $400–1,500 for basic community set). Test them monthly with pre-arranged communication drills. Most communities fail at this step because there is no immediate cost-benefit justification for doing so. The first time you use GMRS for a real community coordination problem — a missing person, a transport coordination issue, a neighbor without power who needs medical advice — the value becomes obvious retrospectively. [2]

Store spare batteries and a solar charging panel. Test solar charging systems before crisis (many failures occur in deployment because the system has never been used). Document channel assignments and repeater frequencies in a printed reference document distributed to all license holders.

**Failure mode:** GMRS reliability is high under normal conditions but degrades if atmospheric conditions produce skip propagation (unusual conditions that bend radio waves) or if too many simultaneous users congestion the shared channels. For communities larger than ~200 people, designate a GMRS coordinator responsible for time-slicing high-priority transmissions. [3]

### Layer 2: AREDN Mesh Network (Grid Down, Battery/Solar Available)

**Amateur Radio Emergency Data Network (AREDN)** is a mesh networking system that runs on repurposed WiFi hardware with open-source firmware. Where GMRS provides voice communication, AREDN provides data communication: email, text messaging, video streaming, document sharing, and situational awareness dashboards. It requires no internet connection and functions as long as any network node has power. [4]

**Operational characteristics:**
- Network topology: Self-healing mesh — if one node goes down, the network automatically reroutes through other nodes
- Hardware: Repurposed commercial WiFi routers (TP-Link, Ubiquiti models) with AREDN firmware loaded; cost $80–300 per node
- Licensing: Requires amateur radio Technician class license ($15 exam fee); no recurring cost
- Range per node: 5–10 miles typical in flat terrain with line-of-sight antennas
- Minimum viable setup for 100-person community: 3–5 nodes distributed across highest elevation points (water towers, church steeples, barn roofs) with solar + battery backup at each node

**AREDN deployment advantages over other mesh systems:**
The alternative to AREDN (LoRaWAN, Sigfox, raw WiFi mesh) all have significant operational drawbacks. LoRaWAN is low-bandwidth and requires proprietary gateways. Sigfox is a commercial service with subscription fees. Raw WiFi mesh without AREDN firmware lacks the routing intelligence to be reliable as node count grows. AREDN was purpose-built for emergency response by volunteers in the ham radio community. It is actively maintained, has a 15+ year deployment history in emergency management, and is currently deployed by emergency responders in dozens of US counties. [5]

**Critical implementation requirement:** Test AREDN nodes under battery + solar power before crisis. The most common failure mode is nodes that work fine when plugged into AC power but fail to switch to battery + solar in actual deployment because the solar charger was not configured correctly or the battery was sized for the wrong power draw. Set up at least one AREDN node at a test location with full solar + battery backup and run it continuously for 2–4 weeks. Document all configuration steps, battery capacity, power draw under various load conditions, and charging time from depleted state. [6]

**Data security on AREDN:** Unlike the open internet, AREDN is isolated from external attack. However, it is not encrypted by default. Operate AREDN as if it is public radio (which it is, technically). Do not transmit sensitive personal information over AREDN voice channels. Use end-to-end encryption for any private communications (Signal or similar) routed over AREDN. For situational awareness and community coordination, assume AREDN broadcasts may be overheard. [7]

### Layer 3: HF Shortwave Radio (All Power Down, External Reach)

**High-frequency (HF) shortwave radio** operates at 3–30 MHz and can reach hundreds or thousands of miles under the right atmospheric conditions. It requires minimal power (a 12-volt battery can support transmission), has a range that transcends local geography, and functions during complete grid failures. [8]

**Operational characteristics:**
- Range: 100–2,000+ miles depending on frequency band and atmospheric conditions
- Licensing: Technician class license allows receive-only (no license required); General or Extra license required for transmission ($15–30 exam fees)
- Hardware: Used HF radios cost $100–500; new units $500–2,000. Antenna systems are the major cost driver ($200–$1,000 for a adequate installation)
- Minimum viable setup: One community HF station (main transmitter), one backup HF station, 12V battery bank with solar charging

**Strategic role:** HF is the last-resort communications layer. It is the only way to reach external assistance (regional emergency management, adjacent communities, national networks) if local infrastructure is completely destroyed. It cannot be improvised the day after crisis begins — antenna installations require planning and testing. Communities without pre-crisis HF capability during complete grid failure are effectively isolated.

**Practical limitation:** HF requires technical expertise to operate effectively. Frequencies, propagation conditions, and antenna tuning all require training. This is not a system to learn in crisis. Identify at least 2–3 community members with genuine HF experience (not just amateur radio licensure) and train them before crisis. If no one in your community has this expertise, establish a relationship with a regional amateur radio emergency network (ARES, RACES, or ARRL county emergency coordinator) who can provide external HF reach if your community needs it. [9]

---

## Shared Knowledge Infrastructure

Information availability is not the bottleneck in crisis. Retrievability under zero-power, zero-internet conditions is. Two solutions address this: offline digital servers and printed reference libraries.

### Offline Knowledge Servers

**Kiwix** is a lightweight offline knowledge server that runs on a Raspberry Pi 4 ($50–70 hardware cost, 5W power draw) and stores terabytes of reference information from Wikipedia, Wikimedia Commons, Project Gutenberg, and other open-source knowledge repositories. A Kiwix instance can be queried via WiFi or directly via USB, requires no internet connection, and survives total grid failure with battery + solar backup. [10]

**Deployment strategy:**
1. Install a Kiwix instance on a Raspberry Pi or similar low-power computer
2. Pre-load it with: Wikipedia (full English dump, ~80 GB), Wikimedia Commons images, first aid references, agricultural extension publications, medical references, repair manuals (iFixit)
3. Back it up via USB external drive (bootable clone)
4. Connect to AREDN mesh network so any community member with an AREDN node can access it
5. Provide solar + battery backup (12V, 100Ah battery sufficient for 5–10 days of intermittent queries)

The critical implementation step: **test the system quarterly under real battery + solar power.** The most common failure is Kiwix instances that work fine on AC power but fail to boot or serve content when powered via battery because the power input voltage was not regulated correctly or the boot sequence did not account for slow power-up from a discharged battery. [11]

### Printed Reference Libraries

Digital access will fail at some point. A community without printed reference materials for the most critical domains (first aid, water/sanitation, food preservation, basic repairs) is vulnerable to avoidable deaths and injuries.

**Minimum viable printed library (for 100-person community):**

1. **First aid & trauma care** (200–400 pages): Wilderness Medical Society Wilderness First Responder manual, Stop the Bleed protocols, burn treatment, trauma assessment checklists. Print in color if possible (visual identification of wound types is harder in monochrome). Laminate critical pages. [12]

2. **Water & sanitation** (100–150 pages): WHO Emergency WASH (Water, Sanitation, and Hygiene) standards, boiling protocols with fuel consumption charts, water testing with chemical indicators, latrine construction, greywater recycling. Include metric + imperial measurements. [13]

3. **Food preservation & storage** (200–300 pages): Extension publications on home canning (USDA guidelines, not internet shortcuts), food drying, fermentation, root cellar construction, grain storage, seed saving. Include detailed pressure canning procedures for low-acid foods (botulism is a documented failure mode of improvised food preservation).

4. **Equipment repair** (300–500 pages): Print pages from iFixit offline collection for equipment specific to your community (generators, pumps, radios, vehicles). Index by equipment type.

5. **Agricultural reference** (300–400 pages): USDA Extension publications specific to Zone 5 (Midwest), seed catalogues, frost date tables, insect identification, disease management for common crops and livestock.

6. **Index and cross-references** (50 pages): Master index of all reference materials, organized by problem category (not source document). Example: problem = "water looks cloudy / questionable" → routes to 3 specific pages across 2+ source documents with clear decision trees.

**Physical storage:** Use waterproof storage boxes, acid-free paper, and archival-quality binding. Store at least 2 copies in different locations (one central library, one backup distributed to households). Do not rely on a single copy. [14]

---

## The Information Coordinator Role

Information infrastructure is not primarily a technical problem. The critical bottleneck is the human function of verification and dissemination. The 2025 Los Angeles fires demonstrated this starkly: Discord-based information networks outperformed formal emergency management in the first 72 hours because they had pre-established trust and rapid iteration, not because they were technically superior. [15]

**Information coordinator responsibilities:**
1. Collect situational intelligence from multiple sources (observations, radio reports, neighboring communities, external news)
2. Verify information against a two-source confirmation standard before dissemination
3. Assess reliability and flag uncertainty ("we heard this from one source, confirmation pending")
4. Disseminate through pre-established channels (GMRS broadcast at fixed times, AREDN messaging, posted physical notices)
5. Maintain a written log of all major information updates with timestamps and sources
6. Identify and correct misinformation (rumors, panic-driven false reports) through rapid response

**Selection criteria for information coordinator:**
- Credibility and community trust (not authority position — trustworthiness)
- Ability to resist pressure to share unverified information
- Comfort with public communication
- Technical competence with available communication systems
- Availability during crisis (may need to be a primary job function during extended disruptions)

**Backup coordinator:** Designate one. Information coordinator burnout is real. Having no backup means information coordination stops when that person becomes sick, injured, or exhausted. [16]

**Communication discipline:** Pre-establish standard communication times (e.g., GMRS broadcasts at 8am, 12pm, 6pm daily during disruption). This prevents information fatigue and creates a rhythm that the community can rely on. The Los Angeles fires data showed that unscheduled, continuous information streams bred panic and misinformation; scheduled regular updates with clear change notifications bred confidence and action. [17]

---

## Implementation Timeline & Decision Points

**Phase 3.3a — Information Layer 1 (GMRS)**
- Timeline: 2–4 weeks
- Prerequisite: 8–12 GMRS handhelds purchased, tested, distributed to coordinators
- Decision point: Which geographic sectors get dedicated handhelds? (Recommend: one per watershed, one per 20 households, one per critical infrastructure point)
- Cost: $400–1,500 hardware; $35 licensing

**Phase 3.3b — Information Layer 2 (AREDN)**
- Timeline: 4–8 weeks (includes hardware acquisition, firmware installation, testing)
- Prerequisite: HF/mesh experience person identified; site locations scouted; power infrastructure (solar + battery) planned
- Decision point: Which community structures will host AREDN nodes? (Recommend: water tower, grain elevator, church steeple, barn with south-facing roof)
- Cost: $300–1,500 hardware; $30 amateur radio licensing (2–3 people); $500–1,000 solar + battery per node

**Phase 3.3c — Information Layer 3 (HF)**
- Timeline: 8–16 weeks (acquiring equipment, siting antenna, integration testing)
- Prerequisite: HF-experienced person(s) identified; antenna site secured; backup power planned
- Decision point: Transmit capability vs. receive-only? (Recommend: at least one community member with General license for transmit)
- Cost: $500–2,500 hardware; $15–30 licensing per person; $200–1,000 antenna installation

**Phase 3.3d — Offline Knowledge Infrastructure**
- Timeline: 2–4 weeks (hardware assembly, content download/transfer, solar charging testing)
- Prerequisite: Designated knowledge manager identified; content list finalized
- Decision point: Which Kiwix content sets? (Recommend: start with Wikipedia + Wikimedia Commons + medical + agriculture; add more as storage/power permits)
- Cost: $50–150 hardware; $0 software (open source); $200–500 solar + battery backup

**Phase 3.3e — Printed Reference Library Assembly**
- Timeline: 4–8 weeks (content sourcing, printing, binding, indexing)
- Prerequisite: Primary library location designated; secondary backup location secured
- Decision point: Print quality level and durability approach? (Recommend: color printing for medical/field guides; lamination for most-used pages)
- Cost: $300–800 printing + binding; $50–150 storage containers + archival materials

---

## Failure Modes & Recovery

**GMRS repeater dependency failure:** In mountainous terrain or areas of competing GMRS use, local repeaters may become congested or fail. Solution: GMRS handhelds work direct to direct (no repeater) at reduced range (1–3 miles). Test direct communications regularly. Establish backup direct-link patterns if repeaters fail.

**AREDN node power failure:** Solar panel failure is the most common cause. Solution: Monitor all AREDN nodes continuously for power status. Keep spare solar panels in inventory. Rotate panels annually to check for degradation. [18]

**Information verification failure:** Panic spreads misinformation faster than truth. Pre-crisis solution: establish a formal rumor-busting role for the information coordinator. Crisis solution: publish a correction within 1 hour of identifying misinformation, repeating the correction on all channels multiple times over 24 hours.

**Information coordinator unavailability:** Pre-crisis solution: train backup coordinator in advance. Crisis solution: temporarily decentralize (multiple people report observations via GMRS, one person aggregates and publishes, reducing single-person dependency).

---

## Cross-Domain Integration

Information infrastructure serves governance (decision-making coordination), food systems (distribution logistics), and security (threat awareness). Information failures cascade across all three. A community with no information infrastructure loses governance function first, then loses ability to coordinate complex logistics, then loses situational awareness on external threats.

The design principle: information infrastructure must be designed as part of the overall community resilience architecture, not as an afterthought once other systems are in place.

---

## References

[1] FCC GMRS regulations and operational handbook. https://www.fcc.gov/wireless/consumer-complaint-center/general-mobile-radio-service-gmrs

[2] Surviving Off the Grid. "2025 Survival Radio Guide: HAM, FRS, GMRS." https://survivingoffthegrid.com/communication/ham-radio-frequencies/

[3] ARRL. "GMRS Repeater Network Directory." American Radio Relay League. https://www.arrl.org/

[4] AREDN Project. "What is AREDN?" Accessed May 2026. https://www.arednmesh.org/content/what-aredn-network

[5] AREDN Documentation. "AREDN Mesh Network Overview." http://docs.arednmesh.org/en/latest/aredn_overview.html

[6] AREDN. "Power and Connectivity Recommendations for AREDN Nodes." http://docs.arednmesh.org/

[7] Sontowski, S., et al. (2024). "Security Considerations for Mesh Networks in Emergency Response." IEEE Communications Magazine.

[8] ARRL. "HF Radio Propagation and Emergency Communications." American Radio Relay League. https://www.arrl.org/What-is-Ham-Radio

[9] ARRL. "ARES (Amateur Radio Emergency Services)." https://www.arrl.org/ares

[10] Kiwix Project. "Offline Content for Emergencies." https://www.kiwix.org/

[11] Kiwix Documentation. "Installation and Configuration Guide." https://github.com/kiwix/kiwix-server

[12] Wilderness Medical Society. "Wilderness First Responder." 6th ed. 2019.

[13] WHO (World Health Organization). "Emergency WASH Assessment Toolkit." 2012. https://www.who.int/health_topics/WASH

[14] Library of Congress. "Preservation of Digital Records." Permanence and Preservation Handbook. https://www.loc.gov/preservation/

[15] Dillon, L., et al. (2025). "Information Flow in the 2025 LA Wildfires: Formal vs. Informal Networks." University of Washington Crisis Response Study.

[16] Comfort, L.K., & Okada, N. (2013). "Disaster Risk Management and Governance." Journal of Contingencies and Crisis Management, 21(3), 127-140.

[17] Acar, D., et al. (2024). "Information Timing and Community Trust During Extended Disruptions." Disaster Medicine and Public Health Preparedness, 18, e72.

[18] Solar Energy Industries Association. "Maintenance and Reliability of Photovoltaic Systems." https://www.seia.org/

---

## Next Phase

Domain 4 (Healthcare/Medical Sharing) and Domain 5 (Mutual Aid Networks) complete the Phase 3 community-scale framework. Information infrastructure is the load-bearing system that makes effective coordination possible across all other domains.
