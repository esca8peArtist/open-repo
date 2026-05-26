---
title: "Phase 6 Communication Infrastructure Scoping — Regulatory, Technical, and Integration Pathways"
project: systems-resilience
phase: 6
wave: 1
status: READY — June 1 decision handoff
version: 1
purpose: "Deep scoping on communication infrastructure: regulatory landscape, technical requirements by scenario, cross-domain integration pathways, and June 1 decision handoff structure."
created: 2026-05-26
word_count: ~2600
decision_window: 2026-06-01
cross_references:
  - PHASE_6_RESEARCH_OUTLINE.md
  - phase-6/meshtastic-community-networking-research.md
  - phase-6/phase-6-meshtastic-lora-mesh-networking.md
  - PHASE_5_WAVE_2_MICROGRIDS_RESEARCH.md
  - PHASE_5_WAVE_2_PHASE_6_EXECUTION_SEQUENCING.md
  - phase-3/03-information-infrastructure.md
---

# Phase 6 Communication Infrastructure Scoping
## Regulatory Landscape, Technical Requirements, Cross-Domain Integration

> **Lead finding**: A Zone 5 community can deploy a legally compliant, encrypted, zero-infrastructure mesh communication network for $485–$2,520 with no license, no registration, and no FCC approval required. The 915 MHz ISM band under 47 CFR 15.247 is a genuine free-use resource. The primary constraint is not regulatory — it is skill and organizational commitment. The community that tests Meshtastic for 30 days before crisis has functional emergency communication. The community that waits until the grid fails does not.

---

## Section 1: Regulatory Landscape

### FCC Part 15 — Unlicensed Operation (900 MHz and 2.4 GHz ISM Bands)

**900 MHz ISM band (902–928 MHz) — Meshtastic native:**

The regulatory authority is 47 CFR Part 15.247. This provision governs digital modulation and spread-spectrum transmitters in three ISM bands: 902–928 MHz, 2400–2483.5 MHz, and 5725–5850 MHz. Key parameters for Meshtastic deployments:

- **Maximum transmitter output power**: 1 watt (30 dBm). Most Meshtastic hardware transmits at 100 mW (20 dBm) to 630 mW (28 dBm). The Heltec V4 at 28 dBm and SenseCAP P1-Pro are the highest-power commercial options and remain within legal limits.
- **Antenna gain and EIRP**: When using antennas with gain above 6 dBi, the transmitter output power must be reduced to keep EIRP within regulatory bounds. For a 9 dBi antenna (common gain for omnidirectional collinear antennas), the transmitter must be reduced by 3 dB from maximum. This trades transmitter power for directional gain without increasing EIRP.
- **Modulation requirement**: The 6 dB bandwidth of the transmitted signal must exceed 500 kHz. LoRa at 915 MHz with a bandwidth of 125, 250, or 500 kHz (selectable) meets this requirement at 250 kHz and above; the default 250 kHz setting in Meshtastic is compliant.
- **No license required**: Part 15 devices operate without FCC license, registration, or fee. The device manufacturer bears certification responsibility; the operator does not.
- **Encryption**: Part 15 places no restriction on encryption. AES-256 channel encryption in Meshtastic is fully legal in ISM band operation. (This is a critical distinction from amateur radio, which prohibits encryption in most contexts.)
- **Duty cycle**: Part 15 in the 902–928 MHz band imposes no duty cycle restriction. Meshtastic nodes may transmit continuously if traffic demands.

Sources: [eCFR 47 CFR 15.247](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/part-15/subpart-C/subject-group-ECFR2f2e5828339709e/section-15.247) · [DigiKey — Unlicensed 915 MHz Band](https://www.digikey.com/en/articles/unlicensed-915-mhz-band-fits-many-applications-and-allows-higher-transmit-power) · [Raveon Technologies — FCC Part 15 ISM Regulations](https://www.raveon.com/wp-content/uploads/2019/05/AN203FCC-ISM.pdf)

**2.4 GHz ISM band — WiFi and Bluetooth spillover:**

The 2.4 GHz band (2400–2483.5 MHz) is also governed by 47 CFR 15.247. Meshtastic's primary use is at 915 MHz, but the 2.4 GHz band is relevant for:
- Node configuration via Bluetooth (BLE on ESP32/nRF52840 platforms): short-range, inside the 15.247 band, no separate regulatory issue
- Node-to-LAN WiFi bridging for MQTT gateway function (ESP32-based hardware): standard 802.11 WiFi, FCC Part 15 certified as part of the chip module certification

Maximum transmitter output in 2.4 GHz spread-spectrum: 1 watt, with the same antenna-gain offset rule. Commercial WiFi devices operate at 100 mW (20 dBm) or less; well within limits.

### Amateur Radio Bands — Community Coordination Frequencies

Amateur radio licensing is not required for Meshtastic ISM-band operation. It becomes relevant when:
1. A community wants the higher transmit power permitted on amateur frequencies (up to 1,500 W on HF; up to 1,500 W on VHF with limitations)
2. A community needs long-range coordination beyond Meshtastic's mesh hop range
3. Operators want to participate in ARES/RACES emergency networks

**Key amateur radio bands for Zone 5 community coordination:**

| Band | Frequency Range | License Required | Propagation | Best Use |
|---|---|---|---|---|
| 2 meters | 144–148 MHz | Technician | Line-of-sight, 20–50 km typical | Local voice/data, repeater-linked |
| 70 centimeters | 420–450 MHz | Technician | Line-of-sight, 15–40 km | Local voice/data, linked repeaters |
| 40 meters | 7.0–7.3 MHz | General | Ground wave + skywave, 50–1,500 km | Regional emergency communication |
| 20 meters | 14.0–14.35 MHz | General | Skywave, 500–5,000+ km | Long-distance coordination |
| 80 meters | 3.5–4.0 MHz | General | Ground wave + skywave, 50–2,000 km | Regional, night propagation |

The 40m band (7.0–7.3 MHz) is the primary Midwest emergency communication band: it propagates reliably day and night at distances of 100–800 km in Zone 5. Net operations typically use 7.175–7.300 MHz voice (USB) and 7.040–7.125 MHz digital modes.

The 2m FM national simplex calling frequency is **146.520 MHz** — the standard cross-community contact frequency if repeater infrastructure is down. A community should have at least one Technician-licensed operator for local 2m network access.

### FCC Licensing: Technician and General Class

**Technician class:**
- 35-question pool examination; 26 correct required to pass (74.3% minimum)
- Prerequisite: none (first license class)
- FCC application fee: $35 (electronic via ULS system)
- Exam session fee: typically $15 (charged by Volunteer Examiner session)
- Privileges: all amateur bands above 30 MHz (2m, 70cm, 6m, 23cm, and microwave bands); limited HF privileges on 10m, 15m, 40m, and 80m CW/digital only
- Study resources: HamStudy.org (free, adaptive), ARRL Technician manual, Mometrix practice exams
- Time to license: 2–4 weeks of part-time study; exam available continuously through online testing (ARRL online exam sessions) or in-person VE sessions

**General class:**
- 35-question examination; 26 correct required
- Prerequisite: Technician class license (or concurrent testing for both)
- FCC application fee: $35 (upgrade or new)
- Exam session fee: typically $15
- Privileges: all 29 amateur service bands including all HF bands; critical for 40m voice coordination
- Study resources: HamStudy.org (same platform), ARRL General manual
- Time to license (Technician holder): 2–6 additional weeks of part-time study

**Zone 5 VE exam logistics:**
ARRL maintains a VE session finder at arrl.org; Zone 5 states (Illinois, Iowa, Wisconsin, Indiana, Ohio) have frequent in-person session availability through local amateur radio clubs. Remote online exam sessions (established during COVID-19 protocols) remain available through GLAARG, W5YI-VEC, and HamStudy Exam portal — no travel required.

**FCC enforcement in rural Zone 5:**
Enforcement history for Part 15 violations in rural areas is minimal. The FCC Enforcement Bureau prioritizes interference complaints from licensed services; a community operating Meshtastic within Part 15 power limits in rural agricultural territory faces negligible compliance risk. The primary enforcement pattern is against deliberate interference or significantly over-power unlicensed transmitters.

The amateur radio enforcement corollary: an unlicensed operator on amateur frequencies (not ISM) faces potential fine ($10,000–$100,000 first offense). Operating on 915 MHz ISM under Part 15 requires no license; operating on 146.520 MHz amateur simplex without a Technician license is a legal violation. The distinction matters — community members should understand which mode they are using.

Sources: [FCC Amateur Radio Service](https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service) · [FCC Operator Class Privileges](https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service/operator-class) · [ARRL Getting Your Technician License](http://www.arrl.org/getting-your-technician-license) · [ARRL Getting Licensed Step by Step](http://www.arrl.org/getting-licensed-step-by-step) · [HamStudy — How to Get Licensed](https://hamstudy.org/content/how) · [FCC Examinations](https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service/examinations) · [Meshtastic FAQ](https://meshtastic.org/docs/faq/) · [Hoosier Mesh — Amateur Radio and Meshtastic](https://hoosiermesh.org/docs/reference/ham-radio/)

---

## Section 2: Technical Requirements by Scenario

### Scenario A: Small Community (15–30 people, single village, 2–5 mile radius)

**Profile**: A single intentional community or tight rural neighborhood with a shared sense of collective identity; members know each other; coordination is primarily local; this is the minimum viable community communication deployment.

**Hardware:**
- 5 Meshtastic nodes minimum (3 backbone + 2 mobile/household)
- Backbone: 3 × RAK WisBlock Starter Kit ($35 each) + 10W solar panel + LiFePO4 18650 (2×) + IP65 enclosure + 6 dBi omnidirectional antenna. Total per backbone node: ~$115
- Household: 2 × LILYGO T-Beam Supreme ($45 each) for mobile or household use
- Total infrastructure cost: approximately $435–$550

**Placement:**
- 1 backbone node at highest available point (grain elevator rooftop, water tower, or barn peak)
- 1 backbone node at community hub (common building, church, or homestead center)
- 1 backbone node at community edge for coverage extension
- Estimated coverage: 5–10 km radius in flat terrain, 3–5 km with significant tree cover

**Operational overhead:**
- Initial setup: 2–4 hours for technically capable person; Meshtastic Web Flasher requires no command line
- Monthly: 1 network test (30 minutes) — all nodes confirm message delivery; check battery voltage on backbone solar nodes
- Quarterly: firmware update audit; battery condition check; antenna connector inspection (moisture ingress at SMA connector is primary weatherproofing failure mode)
- Annual: channel PSK rotation; node inventory audit; documentation update

**Bandwidth profile:**
- Text messages: primary use; handles coordination, status, requests
- Position tracking: GPS location of household nodes visible to all
- Telemetry: battery level, temperature from sensor-equipped nodes (optional)
- What it cannot do: voice, images larger than 200 bytes, video

**Zone 5 specific:**
- Backbone nodes must use LiFePO4 batteries for winter outdoor operation (Zone 5 minimum: -10°F to -20°F; standard NMC lithium loses 30–50% capacity at 0°C)
- Solar panels tilted at 43–45 degrees south-facing for winter optimization (Zone 5 latitude: 41–47°N)
- Annual node inspection in November before first hard freeze — check enclosure seal, desiccant condition, antenna connection

---

### Scenario B: Regional Coalition (3–5 villages, 50–100 people, 10–20 mile radius)

**Profile**: Multiple neighboring communities with formal mutual-aid agreements; requires inter-community communication beyond what single-village mesh provides; the primary coordination challenge is geography and the need for reliable inter-village links.

**Hardware:**
- 12–20 Meshtastic nodes (5–7 backbone + 30–35 household + 5 mobile)
- Backbone: 6 × RAK WisBlock with solar + LiFePO4; 2–3 placed at highest inter-village elevation points (ridgelines, water towers) for inter-community backbone links
- Household: 35 × T-Beam Supreme
- Mobile: 5 × T-Beam Supreme for coordinators and responders
- High-power backbone option for inter-community gaps: Heltec V4 (28 dBm) with 9 dBi directional Yagi antenna for specific point-to-point long links where omnidirectional coverage is insufficient
- Total infrastructure cost: approximately $2,500–$4,000 depending on backbone hardware choices

**Network design:**
- Channel preset: MediumSlow for any network expected to exceed 40 active nodes (MediumSlow eliminates congestion that LongFast suffers at this scale)
- Hop count: 4–5 hops adequate for 3–5 village geometry
- Inter-village channel: shared coalition PSK on a named channel; distributed in person at coalition formation; not stored on phones
- Local channels: each village maintains private local PSK for intra-community traffic
- Role assignments: backbone nodes → Router; household nodes → Client; mobile nodes → Client Mute to avoid rebroadcast congestion

**Coverage:**
- Inter-village distance: 5–15 km between villages typical in Zone 5 rural Illinois/Iowa; a single high-elevation backbone node at each village edge provides the inter-village link
- If inter-village gap exceeds 15 km: add a mid-point repeater (hill, silos, or dedicated tower mount); alternatively, a 9 dBi Yagi-equipped Heltec V4 can extend reliable point-to-point link range to 20–25 km in flat terrain

**Operational overhead:**
- Weekly: network coordinator checks node status via map view (MQTT local dashboard on Raspberry Pi)
- Monthly: cross-community message test (all 3–5 villages exchange test messages)
- Quarterly: joint community drill — simulated grid-down exercise, all active household nodes, inter-village coordination messaging
- Key rotation: annually at minimum; rotate inter-community coalition PSK separately from local PSKs

**Bandwidth profile:**
- Status broadcasts: community supply status (food, fuel, medical supplies, seed inventory)
- Mutual aid requests: formatted text request to coalition channel ("Village A requesting chainsaw operator for storm damage, 3 days")
- Resource availability: coalition-level inventory sharing (see cross-domain integration below)

---

### Scenario C: Distributed Network (Multiple Regions, 200+ People, 100+ Miles)

**Profile**: A geographically distributed resilience network spanning multiple Zone 5 counties or crossing state lines; requires hierarchical architecture because pure Meshtastic flood routing degrades above ~100 active nodes. This scenario requires deliberate protocol design choices and volunteer-led network administration.

**Hardware:**
- 40+ Meshtastic nodes with hierarchical roles
- Regional backbone: 8–12 high-power nodes (Heltec V4 or SenseCAP P1-Pro) at regional elevation high points; some may use directional Yagi antennas for specific 20–40 km point-to-point links
- Community mesh: each sub-community operates its own Scenario A/B mesh; the backbone provides inter-community connectivity
- HF amateur radio backbone: for links exceeding 25–30 km or where terrain prevents reliable LoRa propagation; HF 40m SSB voice or digital modes (WINLINK, Vara FM) for inter-regional coordination; requires General class operators at each regional hub

**Network management:**
- Designated network coordinator (volunteer role): firmware update authority, node inventory, maintenance scheduling, key management
- Protocol boundary management: if MeshCore firmware is used on backbone infrastructure nodes (a design choice that improves large-network performance), this creates a protocol boundary that Meshtastic-only household nodes cannot cross; backbone-to-community gateways must explicitly bridge traffic
- MQTT local broker: Raspberry Pi running Mosquitto at network coordinator's location; collects all node status, message history, GPS tracks; access limited to network coordinator

**Operational overhead:**
- Volunteer-led network administration (estimate: 2–4 hours/week for network coordinator)
- Quarterly training cycles: network configuration training for new community members joining the coalition
- Annual certification: all backbone nodes inspected, firmware updated, keys rotated, documentation updated

**Bandwidth at this scale:**
- Hierarchical messaging: local mesh traffic stays on local channels; only inter-regional coordination traffic routes through backbone
- Latency: at 40+ active nodes and 4–5 hops, message delivery can take 10–30 seconds; acceptable for coordination text; plan communication protocol around this expectation

Sources: [Is LongFast Holding Your Mesh Back? — Meshtastic Blog](https://meshtastic.org/blog/why-your-mesh-should-switch-from-longfast/) · [Disk91 — Critical Analysis of Meshtastic Protocol](https://www.disk91.com/2024/technology/lora/critical-analysis-of-the-meshtastic-protocol/) · [DEV Community — Building Reliable Meshtastic Networks](https://dev.to/vlad_avramut/how-to-build-reliable-meshtastic-networks-in-real-deployments-48b1) · [Austin Mesh Learn](https://www.austinmesh.org/learn/) · [DEV Community — Infrastructure Meltdown with Meshtastic 2026](https://dev.to/noperai42eng/how-to-survive-an-infrastructure-meltdown-with-meshtastic-and-meshcore-2026-dej)

---

## Section 3: Cross-Domain Integration

### Seedwarden Integration

The Seedwarden project manages seed supply chains, planting schedules, and inter-community seed exchange at small-farm and apartment-grower scale. The communication infrastructure integration points:

**Seed availability broadcasts:**
A Meshtastic coalition channel can carry structured seed inventory announcements — variety name, quantity, collection date, collection location. This replaces informal "asking around" with a systematic broadcast that all coalition members receive. Format example:
```
SEED: Butternut squash, 2oz, 2025 harvest, dry-stored, available @Farm7. Reply to coordinate pickup.
```
This fits in a Meshtastic text message (under 200 characters). The receiving community uses the mesh to arrange inter-village pickup logistics.

**Seedwarden supply chain status during MRH or supplier backlog:**
When suppliers like MRH have backlog periods (documented in Seedwarden project tracking), the mesh network enables rapid inter-community coordination of existing seed inventory — communities can survey what is already in storage across the coalition and reallocate before reordering from suppliers.

**Seasonal coordination:**
Planting coordination messages broadcast across the coalition before Zone 5's narrow planting windows (corn: May 1–20, soybeans: May 10–June 5, winter wheat: September 15–October 10) enable equipment sharing, labor exchange, and coordinated pest management — all dependent on reliable inter-community communication.

### Phase 5 Microgrids Integration

The Phase 5 Wave 2 microgrids research (PHASE_5_WAVE_2_MICROGRIDS_RESEARCH.md) documents community-scale off-grid power design. The communication layer integration is bidirectional:

**Mesh carries microgrid status:**
- Battery state of charge (from monitoring system to mesh via node telemetry or automated text broadcast): "MG1 SOC: 78%, solar input, est. 96h autonomy"
- Generation status: surplus generation available for neighbors (e.g., V2G coordination, community freezer charging)
- Critical threshold alerts: SOC below 20% broadcasts to coalition channel for mutual aid planning
- Load-shedding requests: coordinator broadcasts to household nodes requesting demand reduction

**Microgrid powers mesh:**
- The nodes themselves draw <150 mA worst case — negligible load on any microgrid battery bank
- A 5V USB output from the microgrid's 12V or 48V bus (via $3–$8 buck converter) powers all Heltec or T-Beam backbone nodes indefinitely while battery bank holds
- Backbone nodes at remote heights (grain elevator, water tower) use dedicated independent solar + LiFePO4 — no connection to house electrical system required

**Failure cascade detection:**
The community with Meshtastic mesh that also monitors microgrid status can detect cascading failures before they propagate: a node going offline (lost battery power) triggers investigation of the power source; systematic node dropout across a community signals a microgrid event in progress. Without the communication layer, this information is invisible until someone physically checks each site.

### Off-Grid-Living Equipment Overlap

The off-grid-living project (17 production-ready documents, published on GitHub) establishes individual and household resilience foundations. Communication infrastructure overlaps at three points:

**Shared tool library coordination:**
A community with a shared tool library (chainsaws, tillers, welders, pressure washers — equipment documented in Track A of the Phase 6 research outline) requires scheduling and logistics coordination. The mesh carries tool availability broadcasts and reservation requests: "Chainsaw available at workshop, need by Friday - claim by Thursday via mesh or text." This replaces coordination that otherwise requires reliable cellular or in-person visits.

**Maintenance schedule coordination:**
Seasonal maintenance windows (pre-planting March, post-harvest October — the repair clinic model from Track A) require community-wide scheduling. Mesh broadcasts of maintenance events, parts orders, and skill availability enable bulk ordering coordination across the community fleet — reducing parts procurement costs by consolidating shipments.

**Supply chain resilience — coordinating bulk equipment orders:**
Individual households ordering repair parts independently pay retail and absorb separate shipping costs. A community coordinated via mesh can aggregate orders: "Parts order to Shoup going out Friday — add items to coalition spreadsheet by Wednesday." This is a low-bandwidth coordination task that Meshtastic handles well.

### Zone 5 Agricultural Context

**Seasonal coordination windows:**
Zone 5 agriculture has narrow, high-consequence windows where communication failures have outsized impact:
- Corn planting (May 1–20): equipment failures, weather holds, and labor coordination are all time-sensitive
- Soybean planting (May 10–June 5): overlaps with corn harvest cleanup
- Hay cutting (June–August, 3–4 cuttings): weather windows of 3–5 dry days; cutting decision requires weather information sharing
- Winter wheat planting (September 15–October 10): soil temperature and moisture coordination
- Corn harvest (October–November): equipment downtime during harvest is highest-consequence scenario

Mesh network status messages and equipment-sharing coordination during these windows have directly measurable agricultural productivity value. The community that cannot communicate cannot coordinate hay equipment sharing during a 3-day dry window.

**Weather data sharing:**
The mesh can carry informal precipitation and temperature observations from distributed nodes across the community geography — a local weather network that supplements official forecasts. Example: three nodes 5 miles apart each measuring temperature via the Meshtastic telemetry module create a micro-climate map useful for planting timing decisions. This is not a substitute for NWS forecasts; it is a granularity layer above them.

**Pest and disease outbreak early warning:**
First observation of a pest or disease outbreak (corn rootworm, soybean aphid, sudden death syndrome) broadcast to the coalition channel enables coordinated response — neighboring farms can respond before the outbreak spreads. This is a practical example of mesh-enabled community intelligence that no individual household can replicate alone.

---

## Section 4: June 1 Decision Handoff

### Decision Trigger and Dependencies

The June 1 user decision determines Phase 5 Wave 2 sequencing across three paths (from PHASE_5_WAVE_2_DECISION_FRAMEWORK.md):
- **Path A: Community-scale implementation** — directly activates Phase 6 Track B (Meshtastic) as a critical enabling technology; mesh is the coordination layer for community-scale microgrid and mutual aid operations
- **Path B: Household-scale hardening** — Track B deploys as optional enhancement; individual households can implement Scenario A without community decision dependency
- **Path C: Integrated governance + infrastructure** — Track B is a component of the governance infrastructure; mesh provides the communication layer for governance coordination across distributed household nodes

**Phase 6 activation sequence post-June 1 decision:**

If community-scale path is selected:
1. June 1–5: Phase 5 Wave 1 publication proceeds (production-ready, 14.6K words)
2. June 5–15: Phase 6 Track A + Track B integration into `PHASE_6_FRAMEWORK.md` — editorial work synthesizing existing pre-research documents; 2–3 days of writing
3. June 10–July 10: Phase 5 Wave 2 author writing (35% preliminary drafts already staged)
4. July 1–15: Phase 6 document suite finalized, research markers resolved where data is available

If household-scale path is selected:
1. Phase 6 Track B is staged but not time-critical; deployment can begin at household level without community coordination
2. Track A (farm equipment) proceeds independently of Phase 5 path decision — applicable at all scales
3. Integration work deferred to July–August; no June acceleration needed

### Research Blockers Status

**Track A (Farm Equipment):** Zero research blockers for Phase 6 activation. Pre-research documents cover documentation sources, open-source ecosystem, skill architecture, community repair clinic model, and parts sourcing strategy. Six [RESEARCH NEEDED] markers exist but are enhancement items, not activation requirements.

**Track B (Meshtastic):** Zero research blockers for Phase 6 activation. Security vulnerabilities (CVE-2025-52464, CVE-2025-55293) are patched in firmware v2.6.11 — deployment guidance updated to require v2.6.11 as minimum. Three [TECHNICAL SPEC NEEDED] items exist for Zone 5-specific data but are refinement items; the general guidance is actionable now.

**Regulatory landscape:** FCC Part 15 status confirmed from current eCFR (47 CFR 15.247); amateur radio licensing requirements confirmed from FCC.gov and ARRL. No regulatory changes affecting this scope as of May 2026.

### Phase 6 Integration with PHASE_5_WAVE_2_PHASE_6_EXECUTION_SEQUENCING.md

The execution sequencing analysis (Session 1547) identifies the Hybrid Option 3 as the recommended approach — it is consistent with this scoping document's findings:
- Phase 6 research is complete (all pre-research documents finalized May 26)
- Only editorial integration is needed before June 1 activation; no new research sprints required
- Critical path is Phase 5 Wave 1 publication (user-gated), not Phase 6 research
- Phase 6 Track B (Meshtastic) becomes critical faster if community-scale path is selected; activate Track B integration first in that scenario

**What the user needs to decide on June 1:**
1. Phase 5 Wave 2 path selection (A: community-scale, B: household, C: integrated)
2. Whether to proceed with Phase 6 Track A and Track B integration immediately (June 5–15) or defer to July
3. Phase 5 Wave 1 publication approval (separate user action; production-ready documents are staged)

**What does not require a June 1 decision:**
- Meshtastic hardware purchase (Scenario A minimum viable: $66 for 2 Heltec V3 nodes — appropriate for personal testing regardless of community path decision)
- Amateur radio license study (can begin independently; 2–4 weeks Technician study, then General; non-blocking for Meshtastic ISM deployment)
- Farm equipment documentation archiving (2–4 hours of downloading and organizing; can begin today)

The three items above are the pre-decision actions that accelerate Phase 6 regardless of which path is selected on June 1. They are low-cost, low-commitment, and fully reversible.

---

*Confidence levels: High on FCC regulatory details (confirmed from current eCFR and FCC.gov); High on amateur radio licensing structure (confirmed from FCC.gov and ARRL); High on Meshtastic hardware specifications and security status (official Meshtastic docs plus published CVEs); High on Zone 5 agricultural timing (established Midwest extension literature); Medium on inter-village propagation estimates at 15–30 km range (extrapolated from flat-terrain LoRa data; empirical Zone 5 inter-village data is a research gap noted explicitly in the outline). All regulatory references are current as of May 2026; annual check recommended for FCC spectrum policy changes affecting 902–928 MHz band.*
