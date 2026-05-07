---
title: "Phase 2 Expansion Strategy: Threat Model Deepening, Advanced Protection, and Distribution Scale"
project: cybersecurity-hardening
created: 2026-05-06
status: strategic-plan
author: research-agent
depends-on:
  - threat-model.md
  - palantir-threat-model.md
  - opsec-playbook.md
  - implementation-guide.md
  - PHASE_2_SEQUENCING.md
  - phase-2-prioritization-criteria.md
  - may-2026-advanced-threats.md
---

# Phase 2 Expansion Strategy: Cybersecurity Hardening

**Bottom line up front**: Phase 1 distribution built on a Palantir-centric threat model that accurately maps the integration layer. Phase 2 must widen the threat model to encompass the full government intelligence stack — specifically the biometric, aerial, and device-forensics capabilities that have expanded substantially in 2025–2026 and are not adequately addressed by the current corpus. Four research tracks carry the most weight: (1) government surveillance full-stack expansion beyond Palantir; (2) advanced identity compartmentalization for high-risk scenarios; (3) scenario-specific implementation playbooks for the six highest-risk use cases; and (4) Tier 2 audience expansion to communities and organizations not yet reached. The Phase 2 dependency question is addressed directly in Section 6: you do not need Phase 1 adoption data before beginning Phase 2 research tracks 1 and 2, but you should not publish or distribute Phase 2 content until at least the Week 7 data gate from PHASE_2_SEQUENCING.md — i.e., Tier 1 follow-up is complete and at least one engagement signal exists.

---

## Section 1: Updated Threat Model — Government Surveillance Full Stack

### 1.1 What Phase 1 Got Right

The existing threat model (`threat-model.md` and `palantir-threat-model.md`) is accurately grounded in primary sources and addresses the most consequential single system in current immigration and civil society surveillance: Palantir as the data integration backbone. That framing is correct and remains current. The $29.9M ELITE contract, $30M ImmigrationOS contract, $130M IRS LCA platform, and $300M USDA Foundry deployment are all confirmed and documented with primary source citations. The threat model's core insight — that Palantir does not hold data, it enables unified queries across data that already exists — is the correct mental model and should anchor Phase 2 as well.

### 1.2 Five Capability Gaps Phase 1 Does Not Fully Address

**Gap 1: FBI Biometric Intelligence (FACE Services + AI Expansion)**

The existing corpus documents Clearview AI's $9.2M ICE contract. What it does not address is the FBI's parallel biometric infrastructure, which is larger and more integrated.

The FBI operates two parallel facial recognition systems: the Next Generation Identification (NGI) system at the Criminal Justice Information Services Division, and the Facial Analysis, Comparison, and Evaluation (FACE) Services unit. NGI consolidates fingerprints, palm prints, iris scans, face images, and identifying marks into a single biometric repository. FACE Services runs probe photos from open FBI investigations against NGI and against state-level facial recognition systems through data-sharing agreements.

The AI expansion is the material 2026 change: the FBI reported 50 AI use cases in its 2025 AI inventory, up from 19 the prior year, with 27 categorized as law enforcement. The new deployments focus specifically on biometric identification, facial recognition, and investigative triage. The FBI has also issued an RFI (November 21, 2025) seeking AI-powered drones with integrated facial recognition and license plate recognition capabilities. The combination of fixed biometric databases with drone-mounted real-time facial recognition represents a qualitatively new surveillance surface that the Phase 1 countermeasures address only partially.

**Practical threat upgrade**: The current corpus addresses Clearview AI as the facial recognition threat and recommends countermeasures appropriate for a static database. FBI's FACE Services + AI expansion adds: (a) query capability across NGI's 150+ million civil and criminal biometric records, (b) state-level ALPR and facial recognition system access via data-sharing agreements, and (c) the trajectory toward autonomous drone-mounted facial recognition in real-world environments where mask countermeasures are harder to maintain.

Sources: [FedScoop — FBI AI biometric expansion](https://fedscoop.com/fbi-ai-inventory-law-enforcement-biometric-facial-recognition/), [The Intercept — FBI AI surveillance drones](https://theintercept.com/2025/11/21/fbi-ai-surveillance-drones-facial-recognition/)

---

**Gap 2: DHS Biometric Full Stack — HART Platform and the Biometric Entry-Exit Expansion**

The Phase 1 corpus correctly identifies Clearview AI and the ELITE address-confidence scoring system. The DHS biometric stack goes substantially deeper.

DHS operates the Homeland Advanced Recognition Technology (HART) platform as the successor to the Automated Biometric Identification System (IDENT). Congress appropriated $271 million for the DHS Office of Biometric Identity Management in FY 2026, confirming continued investment. HART is hosted in AWS GovCloud and is designed to retain biometric data for 75 to 100 years after the subject's date of birth.

The 2025–2026 biometric expansion is structural, not marginal: DHS proposed a rule in November 2025 to expand biometric collection for immigration purposes by removing age restrictions (collecting from children) and requiring biometrics from some U.S. citizens who interact with non-citizen family members in immigration proceedings. A final CBP rule effective December 26, 2025 authorizes collection of facial biometrics from all noncitizens at airports, land ports, and sea ports — phased rollout underway.

ICE deployed Mobile Fortify, a handheld field identification app, which allows agents in the field to photograph an individual and run contactless fingerprint and facial recognition scans from their smartphones against DHS biometric databases. The app has been used over 100,000 times since launch. A documented accuracy problem: in at least one reported case, the same individual scanned twice in the same interaction was returned two different names, both incorrect — underscoring the false-positive risk of field deployment, which shifts the burden of proof onto the person incorrectly identified.

**Practical threat upgrade**: Mobile Fortify changes the threat geography from fixed checkpoints (border crossings, CCTV networks) to any public space where an ICE agent is present. The pre-ELITE threat model assumed biometric collection required a formal processing encounter. Mobile Fortify enables unambiguous biometric identification at a traffic stop, on a street corner, or at a protest. Countermeasures must address this mobile, ad hoc deployment context.

Sources: [404 Media — Mobile Fortify leaked emails](https://www.404media.co/ice-is-using-a-new-facial-recognition-app-to-identify-people-leaked-emails-show/), [Biometric Update — Mobile Fortify NEC](https://www.biometricupdate.com/202601/ice-facial-recognition-app-mobile-fortify-powered-by-nec), [EFF — Rights orgs demand halt to Mobile Fortify](https://www.eff.org/deeplinks/2025/11/rights-organizations-demand-halt-mobile-fortify-ices-handheld-face-recognition), [Nextgov — DHS biometrics expansion](https://www.nextgov.com/policy/2025/11/dhs-proposes-biometrics-expansion-immigrants-dropping-age-restrictions-and-requiring-biometrics-some-us-citizens/409274/)

---

**Gap 3: Aerial Surveillance Expansion — Drone Infrastructure**

The Phase 1 corpus does not address drone surveillance. This is now an active, documented capability deployed against the populations the corpus serves.

ICE's September 2025 single-month surveillance spending of $1.4 billion — the highest in 18 years — included drones. The Skydio X10D model purchased by ICE can detect individuals from 7.5 miles and identify them from 0.8 miles. Documented operational deployment: CBP flew a military-grade MQ-9 Predator drone over anti-ICE protests in Los Angeles. LAPD deployed Skydio drones at least 31 times to surveil a No Kings protest on January 31, 2026. NYPD deployed nine drones over Manhattan's No Kings march in October, with a 3,200% drone flight increase confirmed for protest surveillance. Drone footage was used to identify and arrest protesters.

The FAA rule of January 16, 2026 banned third parties from flying drones within 3,000 feet of active ICE operations — granting ICE sole airspace authority during raids. This gives ICE a de facto aerial exclusion zone around its own enforcement activities, preventing citizen documentation of operations while preserving ICE's own aerial surveillance capability.

**Practical threat upgrade**: Drone surveillance is operational, not theoretical. The countermeasures that work at ground level (face masks against static cameras) are partially effective against aerial platforms — but aerial angle and coverage area are categorically different. The current corpus has no countermeasure guidance for aerial surveillance environments.

Sources: [The Intercept — LAPD Skydio drone surveillance No Kings protest](https://theintercept.com/2026/04/20/lapd-skydio-drone-surveillance-no-kings-protest-ice/), [DronexL — ICE $85 billion surveillance machine](https://dronexl.co/2026/02/02/ices-surveillance-skydio-drones/), [ACLU — Drones for intimidation](https://www.aclu.org/news/privacy-technology/drones-for-intimidation)

---

**Gap 4: Device Forensics — Cellebrite and the Phone-as-Evidence Problem**

The Phase 1 corpus correctly identifies GrapheneOS as the recommended device platform and addresses the USB attack surface. What is underaddressed is the Cellebrite ecosystem and what it concretely means for device security posture.

ICE holds an $11 million Cellebrite contract, confirmed in 2025 reporting. Cellebrite UFED is capable of physical extraction from devices — not just logical extraction of accessible data, but recovery of deleted files and deep-level storage access. Cellebrite Physical Analyzer now includes a module for accessing Signal app data from extracted device images. This is the most significant caveat to the "Signal is secure" guidance in the current corpus: Signal's server-side security (it retains nothing) is intact, but Signal data on a physically extracted device is accessible if the device is unlocked or the extraction occurs in an active session.

GrapheneOS's response: GrapheneOS blocks new USB connections when the device is locked at both the Linux kernel level and at the USB-C/pogo pin controller level. A 2026 peer-reviewed forensic analysis confirms that GrapheneOS "considerably complicates the remote acquisition of user data" and improves on Android security. GrapheneOS also addressed CVE-2024-53104, a heap buffer overflow likely exploited by forensic tools, in the February 2025 Android Security Bulletin. The hardened_malloc project and hardware memory tagging (MTE on Pixel 8+) provide additional protection against the heap exploitation pathways that forensic tools commonly use.

The critical vulnerability: none of these protections apply to a powered-off phone that is surrendered or seized when PIN/passphrase-locked, if the user has a weak passphrase. GrapheneOS's PIN-scramble feature (random keyboard layout at each unlock attempt) and duress PIN (wipes device on a specific PIN entry) are the relevant second-layer protections. The current implementation guide describes GrapheneOS installation but does not cover duress PIN configuration or the "Before First Unlock" (BFU) versus "After First Unlock" (AFU) distinction that determines whether Cellebrite can access encrypted data.

Sources: [EFF — ICE surveillance shopping spree](https://www.eff.org/deeplinks/2026/01/ice-going-surveillance-shopping-spree), [ScienceDirect — GrapheneOS forensic analysis 2026](https://www.sciencedirect.com/science/article/pii/S2666281726000053), [GrapheneOS FAQ](https://grapheneos.org/faq)

---

**Gap 5: Cross-Agency Fusion — The DOGE Master Database, Post-Supreme Court**

The Phase 1 corpus correctly documents the DOGE data consolidation effort and notes that at least 15 federal lawsuits were challenging it as of early 2026. The litigation landscape has evolved materially.

Supreme Court ruling (June 2025): In Social Security Administration v. AFSCME, the Supreme Court struck down the Fourth Circuit injunction that had blocked DOGE access to SSA data. DOGE personnel can now access SSA's personally identifiable information. The Court's ruling did not resolve the underlying merits — it held only that plaintiffs had not shown likely success. But the practical effect is that SSA access is operational.

Fourth Circuit follow-on (April 2026): The Fourth Circuit vacated the lower court's preliminary injunction on SSA data access, finding plaintiffs had not shown irreparable harm. Even the authoring judge (Toby Heytens) described the whistleblower revelations about DOGE data misuse as "even more alarming" — but ruled the harm showing insufficient for injunctive relief. This is a loss for plaintiffs in the near term: SSA data access is available to DOGE-affiliated personnel pending final merits resolution.

The confirmed scope of misuse: a DOGE employee signed an agreement to share SSA data with a political advocacy group that wanted to overturn election results in certain states. SSA's own court filing admitted DOGE had wider data access than previously disclosed, and that data had been transferred to a non-SSA server the agency can no longer reach.

The operational picture: cross-agency data fusion is not a future capability. The EO directing agencies to end "information silos" is in effect. SSA data is accessible. IRS-DHS data sharing is contested but partially operational (circuit court ruling allows it to proceed). Palantir's Foundry instances at multiple agencies are interoperable via the "mega API" architecture. The master database exists as a distributed query architecture, not a single central database — which is precisely what makes it difficult to block through a single legal challenge.

**Practical threat upgrade**: The Phase 1 corpus describes the DOGE data consolidation as an emerging threat with litigation-dependent status. Post-Supreme Court, SSA access is real. The corpus should be updated in the next quarterly review to reflect this and to note the specific categories of SSA data now accessible (full SSN-linked identity records, benefit payment history, employer records, and address history).

Sources: [Supreme Court — DOGE Social Security access](https://www.democracydocket.com/news-alerts/supreme-court-allows-doge-to-access-social-security-data/), [Nextgov — Fourth Circuit DOGE SSA](https://www.nextgov.com/digital-government/2026/04/appeals-court-removes-limits-doge-access-ssa-data-despite-alarming-revelations/412786/), [Axios — DOGE SSA data misuse](https://www.axios.com/2026/01/20/doge-employees-social-security-information-court-filing)

---

### 1.3 New 2026 Attack Surfaces: AI/ML in Law Enforcement

Three AI/ML deployment patterns are materially new in 2026 and not addressed in the Phase 1 corpus:

**Autonomous flagging via Palantir AIP**: Palantir's AIP (Artificial Intelligence Platform) integrates large language models and autonomous agents on top of Gotham and Foundry data pipelines. AIP agents can perform analysis and generate leads autonomously — without an analyst initiating the query. The Army's $10B ESA explicitly incorporates AIP. The practical threat: an AIP agent can continuously monitor structured data streams (transaction records, ALPR hits, address updates, social media monitoring) and autonomously flag individuals when pattern thresholds are crossed — without a human analyst making an active decision to investigate. This shifts the threat from "a human analyst runs a query on you" to "the system monitors you continuously and surfaces you when an algorithm determines you are relevant." The criteria and thresholds are proprietary and not independently audited.

**Behavioral biometrics and pattern-of-life analysis**: The ELITE address confidence score (Phase 1 corpus) is the visible output of a pattern-of-life analysis that operates on the full Palantir ontology. What is not addressed in Phase 1: the behavioral fingerprinting dimension. Palantir's entity resolution and pattern-of-life systems are sensitive to behavioral patterns, not just identity anchors. Regular commute routes, predictable schedules, consistent spending patterns, and habitual location clusters all generate behavioral signatures that can identify individuals even when their identity anchors (name, SSN, phone number) are pseudonymous. This is the "metadata fingerprint" problem: the current corpus focuses on identity anchors (data broker opt-outs) but does not address behavioral de-anonymization.

**AI-generated evidence fabrication**: As documented in the May 2026 Advanced Threats analysis, ProKYC and similar tools can generate synthetic identity documents and deepfake video that pass commercial liveness checks. The threat to the guide's populations is not primarily financial fraud — it is the risk of AI-fabricated evidence being used to construct false records in law enforcement databases. A fabricated arrest record or fabricated social media post attributed to a target could seed a Palantir profile with false derogatory information. This is not confirmed as an active law enforcement tactic against civil society; it is documented as a capability available to malicious actors who have access to government systems.

---

### 1.4 Updated Threat Matrix: Full Government Intelligence Stack

| System | Agency | 2026 Status | Phase 1 Coverage | Phase 2 Gap |
|--------|--------|-------------|-----------------|-------------|
| Palantir ELITE/ImmigrationOS/ICM | ICE | Active; ICM sole-source Sept 2026 | Comprehensive | Update for ICM deployment |
| Palantir IRS LCA | IRS Criminal Investigation | Active; $130M+ | Comprehensive | Note shift toward political targeting |
| Palantir USDA Foundry | USDA | New April 22, 2026 | Not covered | Add federal workforce surveillance angle |
| DOGE cross-agency Foundry | DHS/SSA/IRS | Post-SCOTUS: SSA access operational | Partial (pre-SCOTUS) | **Update required: SCOTUS ruling** |
| FBI FACE Services + NGI | FBI | Expanding: 50 AI use cases in 2025 | Clearview only | **New: FBI biometric system scope** |
| DHS HART biometric platform | DHS/OBIM | $271M FY26 appropriation | Partial | **New: HART data retention scope** |
| ICE Mobile Fortify | ICE | 100,000+ field uses | Not covered | **New: handheld field biometrics** |
| Drone surveillance (Skydio/MQ-9) | ICE/CBP/LAPD/NYPD | Active protest deployment | Not covered | **New: aerial surveillance countermeasures** |
| Cellebrite UFED + Physical Analyzer | ICE (+ widespread LE) | $11M ICE contract; Signal module | Partial | **Deepen: BFU/AFU, duress PIN** |
| Babel Street + ImmigrationOS OSINT | ICE/DHS | Active for protest monitoring | Social media basics | Deepen: behavioral OSINT reduction |
| NSA Section 702 (PRISM/Upstream) | NSA | Extended to June 2026 minimum | Documented | Note: June 12 deadline update needed |
| FBI NSLs + ECPA orders | FBI | Ongoing | Documented | No major gap |
| ALPR (Vigilant, Flock Safety) | CBP/ICE/local LE | Flock Safety in 5,000+ communities | Documented | Aerial ALPR (drone-mounted) gap |

---

## Section 2: Advanced Protection Techniques

### 2.1 Identity Compartmentalization Architecture

The Phase 1 corpus recommends a single hardened device (GrapheneOS) and a single primary communication channel (Signal). For elevated-risk populations — immigration advocates, activist organizers, journalists with high-profile sources — single-identity architecture is insufficient because the government's entity resolution system can cross-correlate behavioral signatures across a single identity even when that identity is hardened.

**The correct mental model for high-risk populations**: Operate in contexts, not identities. Each context (professional work, activist organizing, personal life, source communication) should have separate device hardware, separate communication channels, separate financial instruments, and no temporal or geographic correlation across contexts.

**Practical compartmentalization architecture**:

*Device level*: Minimum two devices — a primary device for professional/personal life and a dedicated device for sensitive work. The dedicated device should run GrapheneOS, have no app overlap with the primary device, and ideally be purchased with cash from a physical store (not online, which creates a purchase record). The two devices must never appear in the same location at the same time — co-location is the primary entity-resolution anchor in Palantir's LAPD training documentation. When in the same physical space, one device must be in airplane mode or in a Faraday bag.

*Network level*: Each context should have a distinct network fingerprint. The primary device uses your home network or carrier data. The sensitive device uses Tor over a different network (public WiFi + Mullvad, never your home ISP). IP co-location is a standard entity-resolution signal.

*Communication level*: Sensitive communications (Signal with verification) on the dedicated device. No cross-pollination: sources who contact you on Signal should not be the same contacts as your professional Signal account. If a source is compromised and their device forensically extracted, the only Signal contacts revealed are those on the sensitive device's profile.

*Financial level*: Cash for anything associated with the sensitive context. Monero (XMR) as a privacy-preserving digital payment method where cash is not practical, with the critical caveat that Monero must never have touched a regulated U.S. exchange with KYC data (Coinbase, Kraken, etc.) — Monero's on-chain privacy is genuine, but the entry/exit points are the vulnerability. Self-hosted wallets, peer-to-peer exchanges (LocalMonero equivalents post-delisting), or in-person coin swaps preserve the privacy of Monero's transaction graph.

*Temporal level*: Context switching should have temporal gaps. Moving between contexts at predictable times creates a behavioral pattern that correlates contexts even when physical separation is maintained. Random timing, or timing that aligns with natural cover activities, breaks the temporal correlation.

---

### 2.2 Advanced Metadata Minimization — Eliminating Behavioral Fingerprints

The Phase 1 corpus focuses on identity anchor minimization (data broker opt-outs, MAID elimination through GrapheneOS, Signal for communications). Behavioral fingerprinting operates at a layer above identity anchors and can re-identify pseudonymous actors through pattern analysis.

**Behavioral fingerprint categories and countermeasures**:

*Typing cadence and device interaction patterns*: Commercially available behavioral biometric systems (BioCatch, BehavioSec) can identify individuals by how they type, scroll, and interact with a touchscreen — patterns stable enough to identify users across anonymized sessions with high accuracy. This is primarily a threat in organized fraud contexts, but the same technical capability is available to government systems. Countermeasure: use the Tor Browser's protections against behavioral fingerprinting (standardized viewport, limited JavaScript exposure, anti-fingerprinting patches). GrapheneOS's sandboxed Google Play provides per-app permission isolation but does not address behavioral biometrics at the OS input layer. The practical countermeasure is awareness: for the highest-risk activities, use Tails OS on a dedicated computer, which prevents any persistent behavioral baseline from accumulating.

*Wi-Fi probe requests*: Every smartphone with Wi-Fi enabled passively broadcasts probe requests for networks it has previously connected to. These probe requests are visible to any nearby Wi-Fi scanner. An operator with a network of passive Wi-Fi scanners can track device movement across an area by correlating probe request patterns. Countermeasure: GrapheneOS supports MAC address randomization and disables probe requests for known networks when not actively scanning. Ensure this is enabled. Never connect the sensitive device to any named network that is also connected by the primary device.

*Acoustic signatures and ultrasonic beacons*: A small number of commercial tracking products embed ultrasonic beacons in audio content (television, in-store audio) that are inaudible to humans but detectable by smartphone microphones, allowing correlation of who is in the same physical space. This is a niche threat — primarily documented as a commercial tracking practice, not a government surveillance technique. Countermeasure: use a microphone access control policy (GrapheneOS per-app microphone permissions, revoke when not in use). This is already in the Phase 1 corpus but the ultrasonic beacon mechanism is not explained.

*Battery and power consumption fingerprinting*: Demonstrated in academic research that power consumption patterns during normal device use are sufficient to de-anonymize Tor browser sessions on mobile devices. Countermeasure: use a dedicated laptop running Tails OS for Tor browsing (battery drain on a laptop is far harder to fingerprint across sessions than on a smartphone).

---

### 2.3 Physical Surveillance Countermeasures

The Phase 1 corpus does not address physical surveillance countermeasures beyond recommending awareness of ALPR and IMSI catchers. The 2026 expansion of drone surveillance makes this a material gap.

**Ground-level surveillance countermeasures**:

*Facial recognition*: A medical-grade mask (N95 or FFP2, not cloth) covering nose and mouth defeats the lower half of the facial geometry that most algorithms rely on. Hats with full brims reduce overhead camera angle acquisition. Sunglasses defeat periorbital feature extraction but not necessarily infrared cameras in lower light. The combination of mask + hat + sunglasses substantially degrades facial recognition accuracy in NIST benchmarks, though no combination achieves 100% defeat against all systems.

*ALPR*: License plates cannot be obscured without a legal violation. The practical countermeasure is route variation — avoiding predictable routes at predictable times. For high-risk events, use a vehicle not associated with your identity (rental car paid in cash, or a friend's vehicle). The ALPR network is extensive enough in urban areas that single-trip ALPR avoidance is not feasible; the goal is reducing the density of trackable data points, not achieving zero.

*Mobile device detection*: IMSI catchers and passive Wi-Fi scanners detect device presence. For high-risk physical events (protests, sensitive meetings), leave all devices at home or power them off and store in a Faraday bag. Airplane mode is insufficient — baseband firmware can still respond to cell tower pings while the OS shows airplane mode enabled. Full power-off, or Faraday containment, is the standard.

**Aerial surveillance countermeasures**:

*Drone-mounted cameras*: Aerial platforms collect at oblique or overhead angles that defeat ground-level mask countermeasures when faces are visible. The practical countermeasures: stay under cover (building overhangs, tree canopy, scaffolding) when drone presence is suspected. Umbrellas defeat overhead identification for individuals directly below. Distributed movement in crowds reduces the value of aerial surveillance by making individual tracking computationally expensive. Wearing generic, common-colored clothing (dark or neutral tones, no distinctive logos) eliminates the clothing-based re-identification that drones use when facial recognition fails.

*MQ-9 Predator and high-altitude platforms*: Military-grade surveillance drones at altitude are not defeatable through individual countermeasures — their sensors can track through partial occlusion at long range. The practical response is to be aware of airspace notifications (ADS-B Exchange or FlightAware show active drone flights; large public events sometimes generate posted NOTAMs) and to assume that any large-scale public action in a contested political environment is being monitored aerially.

---

### 2.4 Financial Transaction Privacy

The Phase 1 corpus addresses data broker opt-outs and notes that cryptocurrency at regulated exchanges is accessible to the IRS LCA platform. Phase 2 should deepen this for high-risk populations.

**The practical financial privacy architecture for high-risk individuals**:

*Cash*: The single most effective financial privacy tool. Cash leaves no transactional record accessible to Palantir's financial data pipeline. Cash transactions below $10,000 are not subject to mandatory FinCEN Currency Transaction Reports (CTRs). Cash transactions structured specifically to stay under $10,000 thresholds are themselves illegal (structuring, 31 U.S.C. § 5324), so the guidance here is not to structure — it is to recognize that legitimate cash transactions below CTR thresholds leave minimal financial surveillance footprint.

*Monero*: Monero (XMR) uses ring signatures, stealth addresses, and RingCT to obscure sender, receiver, and transaction amount on the blockchain. This is genuinely different from Bitcoin privacy: Chainalysis and the IRS have publicly acknowledged significant difficulty tracing Monero transactions, and the IRS has offered $625,000 for a Monero tracing solution. However, the critical vulnerability is the entry and exit point: if you have ever linked a Monero wallet to a regulated U.S. exchange with KYC data, the exchange has your wallet address linked to your SSN. The IRS LCA platform has access to exchange compliance data (Coinbase specifically documented in contract language). Self-custody from non-KYC sources is the prerequisite for Monero's privacy to be meaningful in practice.

*Financial account compartmentalization*: High-risk individuals and organizations should maintain financial accounts not linked to sensitive advocacy work. The IRS LCA platform maps social networks among investigation targets — if your organization's financial accounts show regular transactions with an entity under investigation, you become part of that entity's social graph. Compartmentalized accounts for sensitive work, with no transaction overlap with personally identifiable financial accounts, limits the social graph expansion that Palantir-enabled investigation routinely uses.

---

### 2.5 Device-Level Forensic Hardening

Phase 2 should extend the GrapheneOS implementation guide with the following currently-missing sections:

**Before First Unlock (BFU) vs. After First Unlock (AFU)**:

When a device is powered on but the PIN/passphrase has not yet been entered (BFU state), encryption keys are not loaded into memory. Cellebrite UFED's physical extraction capability is significantly limited against a BFU device — data partitions remain encrypted and inaccessible without the decryption passphrase. Once the passphrase has been entered (AFU state), encryption keys are in memory and Cellebrite can access substantially more data. The practical implication: power off the device before any anticipated contact with law enforcement. A device handed over while powered on is in AFU state and significantly more vulnerable than a device that is off.

**Duress PIN / Wipe Passphrase**:

GrapheneOS supports a "wipe passphrase" — a secondary PIN that, when entered, wipes the device's encryption keys, rendering data unrecoverable. This is distinct from the "duress PIN" feature sometimes described in security literature; it is a configuration in GrapheneOS Settings > Security > Wipe passphrase. For individuals who may face coerced device surrender, this provides a last-resort data destruction option. Note: using a wipe passphrase in a legal encounter may have independent legal consequences (potential obstruction issues), and individuals should consult with counsel about their specific legal context before relying on this as a primary strategy.

**Auto-Reboot Configuration**:

GrapheneOS supports automatic device reboot after a configurable time period of inactivity. When the device reboots, it returns to BFU state. Setting auto-reboot to 12–24 hours means that a seized device left overnight before forensic extraction begins is in BFU state rather than AFU state. This is a low-friction, high-value configuration that requires one setting change.

**UEFI/Firmware Note for Laptops**:

For laptop users with Tails OS and VeraCrypt (Tier 2 and above), the LogoFAIL vulnerability (UEFI image-parsing buffer overflow, unpatched on approximately 95% of affected x86 devices as of 2026) represents a potential persistence mechanism that survives OS reinstallation and disk re-encryption. Mitigation: verify UEFI firmware updates from device manufacturers are current, use Secure Boot where supported, and be aware that high-value targets of nation-state-level adversaries should consider devices with documented firmware security programs (ThinkPad BIOS security documentation, Purism's coreboot-based hardware).

---

## Section 3: Implementation Playbooks for High-Risk Scenarios

### 3.1 Why Scenario Playbooks vs. Tier-Based Guidance

The Phase 1 corpus uses a tier structure (Tier 1 = journalists/advocates/healthcare workers, Tier 2 = activists/organizers/protest participants, Tier 3 = direct investigation targets). This structure is sound for general guidance but insufficient for the highest-risk scenarios, which require sequence-specific, situation-specific action protocols that cut across tiers.

Phase 2 should produce six scenario playbooks as standalone documents that link back to the main corpus but address the specific sequencing, timing, and contextual factors of each scenario.

---

### 3.2 Playbook 1: Immigration Advocacy and Surveillance Evasion

**Target audience**: Undocumented individuals, DACA recipients, individuals in removal proceedings, immigration attorneys working with at-risk clients.

**Threat profile specific to this population**: ELITE neighborhood targeting (address confidence scoring); ImmigrationOS self-deportation monitoring (behavioral signals interpreted as intent to flee); Mobile Fortify field biometric identification; HHS/Medicaid data flowing to ELITE; family members as surveillance anchors in ICM social graph.

**Playbook-specific guidance beyond Phase 1 corpus**:

1. *Medical care and Medicaid*: The Phase 1 corpus notes that HHS/Medicaid records feed ELITE. The practical implication for the playbook: individuals with concerns about ELITE exposure should understand that their Medicaid enrollment address is a live data source for ELITE confidence scoring. This is a genuine harm-benefit tradeoff: Medicaid provides essential health services, and individual withdrawal from Medicaid does not meaningfully reduce aggregate ELITE data quality. The guidance here is *not* to withdraw from Medicaid — that would cause direct medical harm for uncertain protection benefit. The guidance is to understand that Medicaid address records should match any other address you want to be your known location (not a sanctuary location or safe house).

2. *Address management*: ELITE's address confidence scoring aggregates utility bills, credit applications, HHS records, DMV records, and license plate reader hits near an address. Any administrative interaction that creates a record at a new address updates ELITE's confidence scoring within days to weeks. If a safe-house or temporary shelter address needs to remain off the ELITE radar: create no administrative records there (no utility enrollment, no mail delivery, no DMV change, no bank statement delivery, no ACA enrollment change). Keep the address invisible by keeping all administrative records pointing elsewhere.

3. *Family and social graph awareness*: ICM stores family relationships. Anyone with immigration system history at any point has family relationships documented. This means that immigration enforcement can use family members as anchors to locate a target. Counter: understand which family members are in ICM and avoid predictable family contact patterns during elevated enforcement risk. Signal for all family communications, end-to-end encrypted, with disappearing messages enabled.

---

### 3.3 Playbook 2: Activist Organizing and Counter-Surveillance

**Target audience**: Protest organizers, political activists, community defense networks, anyone with a public political presence in a context where retaliation risk is elevated.

**Threat profile specific to this population**: Babel Street social media OSINT for keyword and sentiment monitoring; drone aerial surveillance at protests; ALPR vehicle tracking approaching and departing protest sites; Mobile Fortify field identification at protest perimeters; ImmigrationOS "Catch and Revoke" social media cross-referencing for visa holders; deepfake political content fabricated using activists' public video presence.

**Playbook-specific guidance beyond Phase 1 corpus**:

1. *Social media hygiene before public actions*: Set all accounts to maximum privacy settings at least 72 hours before a public action. Babel Street aggregates public content continuously; content posted within the immediate action window is the highest-risk. Review and archive or delete posts that identify regular locations, travel patterns, or event planning details. Do not post event logistics in public-facing formats — use closed Signal groups for coordination.

2. *Vehicle and transit*: Drive to a protest location in a vehicle not associated with your identity (or take transit) to avoid ALPR correlation of your vehicle approaching known protest sites. If driving your own vehicle is unavoidable, arrive at times that are not temporally correlated with your other known activities. Parking in the same block as every public action creates an ALPR signature that maps to your identity.

3. *Layered physical countermeasures*: Mask + hat + sunglasses for all above-ground, publicly visible activity at protests. Change at least one distinctive clothing item (swap a top layer) before leaving the protest area to break the re-identification chain that drones and CCTV networks use when tracking individuals exiting a dispersal.

4. *Duress/emergency communication protocol*: Establish a "check-in" protocol with a trusted contact who is not at the action. If check-in is missed by 30 minutes, the trusted contact contacts the designated legal support line (NLGSF, legal aid, etc.) with your last known location. Pre-save the National Lawyers Guild number as the first contact in your Signal address book.

---

### 3.4 Playbook 3: Financial Resistance

**Confidence note**: This playbook addresses legal financial privacy practices. It does not address illegal sanctions evasion, money laundering, or structuring — those are federal crimes and are not the concern of this corpus. The threat the corpus addresses is the IRS LCA platform's use for politically-targeted financial surveillance of advocacy organizations and individuals, and the data broker financial pipeline that feeds Palantir's social-graph mapping.

**Target audience**: Advocacy organizations, mutual aid networks, individual donors to causes under political scrutiny, activists who have reason to believe they may be under IRS or FinCEN investigation.

**Threat profile**: IRS LCA financial social graph mapping; FinCEN SAR reporting; Palantir Foundry connecting financial data to immigration and biometric records; DOGE-era IRS-DHS data sharing (currently contested in litigation); cryptocurrency exchange KYC data in IRS LCA pipeline.

**Playbook-specific guidance beyond Phase 1 corpus**:

1. *Organizational financial hygiene*: Advocacy organizations under political scrutiny should maintain clear documentation that all financial activity is consistent with the organization's stated mission. The IRS LCA platform maps relationships across financial records — if your organization's accounts show transactions that could be mischaracterized as foreign-influenced, politically adversarial, or structuring-adjacent, document the legitimate purpose of each transaction category. This is legal documentation defense, not financial concealment.

2. *Donor privacy*: For organizations that wish to protect small donor privacy: donations processed through fiscal sponsorship organizations (a 501(c)(3) sponsor that receives and disburses funds) reduce the number of direct donor records associated with the organization. This is a legal and common practice in the nonprofit sector.

3. *Cryptocurrency use*: If an organization accepts cryptocurrency donations for privacy reasons: Monero provides genuine on-chain privacy. Bitcoin does not — all Bitcoin transactions are public on the blockchain, and chain-analysis firms (Chainalysis, contracted by IRS) can trace Bitcoin with significant accuracy. The caveat for Monero remains: any funds that have touched a regulated exchange with KYC records create a link between the organization's wallet and the exchange account holder's SSN in the IRS LCA database.

---

### 3.5 Playbook 4: Institutional Whistleblowing

**Target audience**: Federal government employees, contractors, and employees of private companies who hold evidence of illegal government conduct and are considering disclosure.

**Threat profile**: All government surveillance capabilities apply at elevated intensity to targets suspected of insider disclosure. Device forensics (Cellebrite) is the primary threat — the government can compel device surrender under investigation. Network monitoring of government networks is comprehensive and leaves audit logs. PRISM-authorized access to email, cloud storage, and communications metadata of government employees suspected of disclosure to journalists is legally available.

**Playbook-specific guidance beyond Phase 1 corpus**:

1. *SecureDrop as the primary secure channel*: SecureDrop is operational at more than 65 news organizations, including the New York Times, Washington Post, The Guardian, ProPublica, and The Intercept. SecureDrop sources access the system exclusively through Tor (both interfaces are Tor hidden services), and submissions are encrypted at rest with GPG. The source's IP address is not accessible to the journalist. As of 2026, SecureDrop is completing a mobile app (post-security audit) and a new SecureDrop Protocol with end-to-end encrypted messaging and peer-reviewed security properties.

2. *Critical operational requirement*: Never access SecureDrop from a device, network, or location associated with your identity. The standard failure mode for whistleblowers is accessing the submission system from a government device, a home network traceable to their residential address, or a phone registered in their name. SecureDrop must be accessed from a public computer or a dedicated, air-gapped device, over a network with no identity anchor, using Tor.

3. *Legal protection framework*: The Whistleblower Protection Act covers disclosures about illegality, waste, fraud, and abuse to Congress, Inspectors General, and the Office of Special Counsel — but explicitly does not cover disclosures to the press. The Government Accountability Project (whistleblower.org) provides legal support to federal whistleblowers, including immigration enforcement whistleblowers, as of its 2025 reporting. Connecting with legal counsel before disclosure is the highest-ROI action for any whistleblower — not as a deterrent but to understand what legal protection, if any, applies to your specific disclosure.

4. *The parallel construction risk*: Even if a whistleblower's identity is protected during the disclosure process, law enforcement can use the substance of the disclosure to initiate an investigation and then "rebuild" a case using parallel conventional evidence. Document all potentially retaliatory actions against you from the moment of any investigation opening. The documentary record of retaliation is essential for both legal protection and public accountability.

Sources: [SecureDrop](https://securedrop.org/), [Freedom of the Press Foundation digital security](https://freedom.press/digisec/), [Government Accountability Project immigration whistleblowers](https://whistleblower.org/immigration/)

---

### 3.6 Playbook 5: Journalist Security at Scale

**Target audience**: Investigative journalists, documentary filmmakers, photojournalists, news organization IT and security teams.

**Threat profile**: CBP device search authority at border crossings (no warrant required); PRISM compelled access to journalist email and cloud storage when communicating with foreign sources; NSL compelled disclosure of journalist metadata from carriers and internet providers without judicial authorization; Babel Street social media monitoring of journalists' public profiles; Clearview AI and Mobile Fortify if journalists are present at enforcement actions or protests.

**Playbook-specific guidance beyond Phase 1 corpus**:

1. *Border crossing device security*: CBP has full device search authority at U.S. international border crossings without a warrant or probable cause. Journalists crossing with source material should maintain a "travel device" with no source-identifying data. The travel device should have no active accounts, no Signal messages, no email, and no documents. Source material should be stored in encrypted cloud storage not accessible on the travel device (not even logged into the account), retrieved only after clearing customs on a different network. This is the "border crossing clean device" protocol.

2. *Source compartmentalization*: Journalists who use Signal for source communication should not have source contacts in the same Signal account as their personal contacts. A dedicated GrapheneOS device with its own phone number (registered with a VoIP service, not a carrier-traceable SIM) for source communication separates the source communication surface from the journalist's personal and professional identity surface.

3. *SecureDrop at your news organization*: For organizations that receive document leaks: SecureDrop is the appropriate channel. If your organization does not operate SecureDrop, Freedom of the Press Foundation provides setup support. The 2026 SecureDrop mobile app will significantly reduce the friction for sources, who currently must access SecureDrop exclusively through Tor Browser on a desktop. The new SecureDrop Protocol adds end-to-end encryption for journalist-source replies, closing a gap in the current system where journalist-to-source replies were only network-layer encrypted.

4. *PRISM and the foreign source problem*: Journalists who communicate with sources outside the United States over email, standard messaging apps, or cloud storage are at meaningful risk of having their communications compelled under PRISM (Section 702). Signal, properly used with a foreign-registered number and with note-sync to Signal servers disabled, significantly limits PRISM-accessible metadata. But Signal's safety number verification (in-person or via an out-of-band channel) is required to prevent a government-controlled intermediary from substituting their own keys in a foreign source's account.

---

## Section 4: Tier 2 Audience Expansion

### 4.1 Who Else Needs Phase 2?

The Tier 1 distribution targets legal aid, community organizations, and mutual aid networks. The Tier 2 distribution targets digital rights organizations, academic programs, security researcher communities, and journalist organizations. Phase 2 audience expansion addresses three additional high-priority communities not adequately served by the current distribution architecture.

**Community 1: Domestic Violence Survivors and Advocates**

The threat model is structurally distinct from the government surveillance model in the current corpus. The primary adversary in DV contexts is an intimate partner with pre-existing device access, shared account credentials, shared family plans with location-sharing enabled, and potentially legal access to shared financial accounts. Stalkerware (apps like FlexiSPY, Hoverwatch, or mSpy that run invisibly on a device) is the dominant threat vector and is not addressed anywhere in the current corpus.

Countermeasures required for DV survivor safety are also distinct: device replacement (not just hardening, because stalkerware can survive a factory reset if it has root access), account separation (creating new accounts on a new device, not resetting passwords on existing accounts because the abuser may have account recovery access), and the "safety planning" framework that DV advocates use to assess exit risk before making any changes to device or account security. The National Network to End Domestic Violence's Safety Net project maintains current guidance at nnedv.org/content/safety-net/.

Audience size and distribution network: approximately 10+ million DV survivors in the U.S. DV organizations are a well-organized, nationally coordinated distribution network. The National Domestic Violence Hotline, state coalitions, and local shelters represent a distribution infrastructure comparable to the immigration legal aid network in Tier 1.

**Community 2: Labor Organizers and Workers in Organizing Drives**

The threat model here is employer surveillance of organizing activity: workplace monitoring software (keyloggers, email monitoring, productivity surveillance tools), social media monitoring for union sentiment, and the risk of firing for organizing-protected activity before legal protections attach. The IRS LCA platform's confirmed shift toward investigating "left-leaning groups" adds a government surveillance dimension when labor organizations have financial relationships that might attract IRS scrutiny.

The USDA's Palantir contract, which includes a $75M workforce surveillance component for return-to-office compliance monitoring with real-time analytics, establishes the precedent that federal workforce surveillance is a Palantir product. This is not directly relevant to private-sector labor organizing but is evidence of the direction.

Distribution network: AFL-CIO, SEIU, UFW, NDWA, and independent union organizing networks are already in the Tier 3 distribution pipeline. Phase 2 labor playbook would be the content deliverable they need to actually use the corpus with their membership.

**Community 3: Election Workers and Poll Watchers**

This is a new and growing risk population: local election officials and poll workers are subject to documented harassment, intimidation, and surveillance by hostile actors including organized political groups and potentially by state-level political actors. The threat profile includes: physical surveillance at polling locations, social media harassment campaigns using personal information harvested from public records, and the potential for false-positive identification via facial recognition technology at polling locations where ICE or law enforcement is present.

CISA's withdrawal of election security support (EI-ISAC shutdown, $10M cooperative agreement terminated) has removed the primary federal resource that election officials previously relied on for cyber incident response. The distribution gap: this community is not currently served by the corpus and has no obvious existing distribution network for cybersecurity resources. Connection point: the Election Assistance Commission (EAC) and state-level associations of election officials are the appropriate Tier 2 contact for this community.

---

### 4.2 Which Organizations Should Receive Phase 2 Training?

Beyond the Tier 3 distribution pipeline already planned (policy organizations, labor, academic law/policy schools), Phase 2 training delivery should target:

| Organization Type | Representative Examples | Rationale |
|-------------------|------------------------|-----------|
| DV legal and advocacy organizations | NNEDV Safety Net, state DV coalitions, VAWA-funded programs | DV survivors face intimate partner surveillance threat; existing distribution trust network |
| Labor union organizing departments | AFL-CIO organizing department, SEIU, UFW, NDWA | Workers under employer surveillance + potential IRS LCA financial scrutiny |
| Election administration networks | State associations of election officials, EAC liaisons | CISA gap leaves this community without federal cyber support |
| Public defender offices | Federal Defender organizations, state public defender offices | Attorneys representing immigration and civil rights defendants need to understand the surveillance infrastructure used to build cases against their clients |
| Sanctuary city legal offices | City attorneys in sanctuary jurisdictions | Need to understand data-sharing constraints and legal exposure when cooperating with ICE requests |
| ITIN filer tax preparer networks | Volunteer Income Tax Assistance (VITA) programs, community tax prep organizations | ITIN filers are specifically in the IRS-DHS data-sharing pipeline; tax preparers who work with undocumented clients need to understand the risk |

---

### 4.3 New Formats for Phase 2 Audiences

The Phase 1 distribution uses a three-document corpus (threat model, playbook, implementation guide) distributed as a GitHub Gist. This format works well for Tier 1 and 2 audiences who have the bandwidth to read long-form technical documents. Phase 2 audiences require additional formats:

**Short video primers (3–5 minutes each)**: Covering: "What is ELITE and why does my address matter?", "How to use Signal safely", "What to do if ICE approaches you", "How to protect your phone before a protest." Video format dramatically expands accessibility for populations with limited literacy, limited English proficiency, or limited bandwidth for long-form reading.

**Interactive decision trees**: "If you are [community member / activist / journalist]: what do you need to do?" Branching decision trees that route users to the relevant sections of the corpus based on their risk profile and resources. The phase-2-prioritization-criteria.md document identifies the need for a Texas-specific supplement for readers without access to the California DROP platform; a decision tree is the most efficient format for handling state-specific routing without producing a separate document for each state.

**Role-based playbooks**: The six scenario playbooks in Section 3 of this document are the Phase 2 deliverables for this format. Each playbook is standalone and addresses its audience's specific threat profile without requiring them to read the full corpus first.

**Translated materials**: Spanish is the priority first translation. A substantial portion of the Tier 1 immigration advocacy audience communicates primarily in Spanish. Translation of the Phase 1 implementation guide's Part 0 (data broker opt-outs) is the highest-ROI translation project — it requires no technical knowledge to execute and has direct impact for the most at-risk population. Digital Defenders Partnership and organizations like Access Now provide translation support for security guides serving at-risk communities.

---

## Section 5: Implementation Timeline — 6 to 12 Months

### Month 1–2: Phase 1 Completion and Data Collection

These months are defined by PHASE_2_SEQUENCING.md's Tier 1 active outreach (Weeks 1–3) and follow-up period (Weeks 4–7). Phase 2 research and content development can begin in parallel.

*Research tracks (begin now, do not wait for adoption data)*:
- Draft the threat model update for Mobile Fortify, drone surveillance, and the post-SCOTUS DOGE/SSA status
- Research HART biometric retention scope and update the DHS biometric threat section
- Draft the immigration advocacy playbook (Section 3.2 above)

*Do not distribute*: No Phase 2 content should be distributed until the Week 7 gate (minimum Tier 1 transition criteria met per PHASE_2_SEQUENCING.md Section 2).

### Month 3–4: Threat Model Update and Tier 2 Distribution

The quarterly review is scheduled for July 26, 2026. This is the correct moment to publish the Phase 2 threat model update as a Gist revision.

*Deliverables for July 26, 2026 quarterly review*:
- Updated threat model section V (Biometrics) to include Mobile Fortify
- New Section XI (Aerial Surveillance) covering drone capabilities and countermeasures
- Updated DOGE section to reflect post-SCOTUS SSA access status
- Updated Section III (NSA) to reflect June 12 FISA 702 outcome

*Tier 2 distribution*: Per PHASE_2_SEQUENCING.md, Tier 2 active outreach begins Week 5 (concurrent with Tier 1 follow-up). By Month 3–4, Tier 2 outreach to digital rights organizations (2A) and journalist organizations (2D) should be complete or near completion.

### Month 5–6: Scenario Playbook Production

Each playbook is a 1,500–2,500 word standalone document. Production sequence based on population risk and distribution network readiness:

1. Immigration advocacy playbook (Playbook 1) — first, because Tier 1 distribution creates the natural distribution channel
2. Journalist security playbook (Playbook 5) — second, because Tier 2 journalist outreach creates the distribution channel
3. Activist organizing playbook (Playbook 2) — third, because Tier 3 policy and labor outreach creates distribution channel
4. Whistleblowing playbook (Playbook 4) — fourth, because SecureDrop availability at 65+ organizations provides distribution infrastructure
5. Financial resistance playbook (Playbook 3) — fifth, because this requires no specialized distribution channel
6. DV survivor playbook — sixth, requires separate NNEDV/DV coalition outreach that is not in existing distribution pipeline

### Month 7–9: Tier 2 Audience Expansion Outreach

Separate outreach track from the main Tier 1/2/3 distribution, targeting the Phase 2 new audiences identified in Section 4.

*Priority outreach contacts for Phase 2 audience expansion*:
- NNEDV Safety Net Program (nytimes.com — they publish technology safety resources)
- AFL-CIO Technology Institute
- National Association of State Election Directors (NASED)
- National Association of Election Officials (Election Center)
- National Legal Aid and Defender Association (for public defenders)
- Volunteer Income Tax Assistance (VITA) programs

### Month 10–12: Format Diversification and Translation

Contingent on adoption data from Months 1–9 showing that format is a barrier:

- Spanish translation of Part 0 (data broker opt-outs) and a one-page summary of key actions
- Decision tree document for state-specific routing (Texas supplement as first priority)
- Video primer scripting (content only — production requires external resources)

---

## Section 6: Success Metrics

### Distribution Adoption Metrics (From Existing Framework)

The phase-2-prioritization-criteria.md document establishes the quantitative thresholds for Phase 2 launch authorization. Those thresholds apply here:

- 1,000+ cumulative Gist views (minimum Phase 2 launch trigger)
- 3+ Tier 1 organizations at Stage 2+ engagement
- 100+ feedback form submissions
- Top 3 gaps cited by 30%+ of respondents

These are the minimum thresholds. Phase 2 research tracks 1 and 2 (threat model expansion and advanced protection techniques) should be completed regardless — they improve the quality of the existing corpus and are independent of distribution adoption.

### Phase 2-Specific Impact Metrics

**Threat model reach**: How many organizations have received and engaged with the updated threat model (post-July quarterly update)? Track separately from Phase 1 corpus distribution.

**Scenario playbook adoption**: Has any playbook been cited, adapted, or distributed by an organization outside the original Tier 1–3 distribution pipeline? This is the strongest indicator that playbooks are genuinely useful in context.

**Phase 2 audience penetration**: At least one DV organization, one labor union organizing department, or one election administration network has received and responded to Phase 2 targeted outreach. This is the minimum indicator that Phase 2 audience expansion is working.

**Legal and litigation citation**: The highest-impact outcome metric. If any element of the threat model or a scenario playbook is cited in a legal filing, court testimony, amicus brief, or legislative testimony, this represents maximum institutional impact — it means the corpus is functioning as an authoritative reference document in the adversarial legal context for which it was designed.

---

## Section 7: Dependencies — Does Phase 2 Require Phase 1 Adoption Data?

### The Short Answer

Phase 2 research and content development does not require Phase 1 adoption data. The threat model expansion (Section 1) and advanced protection techniques (Section 2) should be developed now. They are improvements to the existing corpus that make it more accurate and more useful regardless of distribution status.

Phase 2 distribution and playbook publication should wait for the Week 7 gate — the minimum Tier 1 transition criteria in PHASE_2_SEQUENCING.md Section 2. The reason: playbooks designed for specific populations (immigration advocates, journalists, etc.) are most effectively distributed through the organizational relationships that Tier 1 outreach builds. Publishing playbooks before any Tier 1 organizational relationships are established means distributing into a vacuum with no trust-network amplification.

### The Quarterly Update as the Natural Phase 2 Launch

The July 26, 2026 quarterly review (Gate 4 in PHASE_2_SEQUENCING.md) is the natural Phase 2 content launch moment. By July 26:

- Tier 1 active outreach will be complete (Weeks 1–3)
- Tier 1 follow-up will be complete or nearly complete (Weeks 4–7)
- At least 40 organizations will have been contacted and at least some response signal will exist
- Tier 2 outreach (Weeks 5–12) will be partially complete
- The FISA 702 June 12 deadline will have resolved one way or another — this is material to the NSA threat model section

A Gist update on July 26 that incorporates the threat model expansions in Section 1 of this document, together with the first playbook (immigration advocacy), gives Phase 2 a concrete launch artifact that aligns with the existing review cycle.

### What Adoption Data Should Inform Phase 2 Sequencing

Adoption data does matter for deciding *which* Phase 2 content gets built next after the initial threat model update. Per phase-2-prioritization-criteria.md:

- If Tier 1 legal aid organizations are the most engaged group: prioritize the immigration advocacy playbook and the legal aid organizational hardening guide
- If Tier 2 journalist organizations are the most engaged group: prioritize the journalist security playbook and SecureDrop integration guidance
- If feedback shows that specific tools are failing (Tails on ARM hardware, GrapheneOS installation failures): prioritize the relevant implementation guide deepening before adding new content
- If feedback is dominated by the same geographic limitation (Texas users asking about DROP alternatives): prioritize the Texas supplement as the first format diversification deliverable

---

## Section 8: Urgent Threats and Gaps — Flags for Phase 1 Launch Decision

Three findings from this research should influence the user's decision on Phase 1 launch timing:

**Flag 1: ICE Mobile Fortify changes the physical encounter threat profile (High Priority)**

Mobile Fortify's field deployment — 100,000+ uses, powered by NEC facial recognition, with 15-year biometric data retention, and no consent mechanism — is a material change from the Phase 1 corpus's biometric threat model. The current corpus's countermeasures (mask at protests, GrapheneOS for device security) remain correct, but the guide's framing implies that biometric collection requires a formal government processing encounter. Mobile Fortify has moved biometric collection to any public street encounter. This should be updated in the corpus before or concurrent with Tier 1 distribution, not deferred to the July quarterly review.

Specifically, the opsec-playbook.md's biometric section should add a sentence explaining Mobile Fortify's field deployment capability and confirming that the same countermeasures apply (face covering in any encounter context, not just formal checkpoints).

**Flag 2: Supreme Court's DOGE/SSA ruling changes the data fusion threat from potential to operational (Medium Priority)**

The Phase 1 corpus notes that at least 15 lawsuits were challenging DOGE data access as of early 2026. The June 2025 Supreme Court ruling allowing DOGE access to SSA data, combined with the April 2026 Fourth Circuit decision removing injunctive limits, changes the threat model status from "challenged, potentially constrained" to "operational, pending underlying merits." The specific implication: SSA data (SSN, address history, benefit history, employer records) is now actively accessible to DOGE-affiliated personnel and flowing toward DHS. This is not a new capability — it is a change in the legal constraint on an existing capability. The corpus should be updated to reflect the current litigation status accurately.

This is a quarterly review item (July 26, 2026) rather than a pre-launch emergency. The underlying countermeasures do not change; the framing of the litigation as an ongoing constraint does change.

**Flag 3: Cellebrite's Signal module changes the "Signal is secure" framing for seized devices (High Priority)**

The Phase 1 corpus states, accurately, that Signal's server-side security means law enforcement can compel only account creation date and last connection date from Signal. This is still true. What is not currently in the corpus: Cellebrite Physical Analyzer can access Signal app data from a physically extracted device image. The condition is that the device must be in AFU state (unlocked) or the passphrase must be known. A device in BFU state (powered off) remains significantly protected against Cellebrite extraction.

The practical guidance update: the corpus should add the BFU/AFU distinction and the recommendation to power off devices before any anticipated law enforcement encounter. This is a meaningful addition — many users may currently believe that Signal's server-side protection makes device seizure a lesser risk than it actually is in AFU state.

This should be added to the implementation guide before Tier 1 distribution, not deferred.

---

## Section 9: Summary and Recommendations

**What Phase 2 is**: An expansion of the threat model to the full government intelligence stack beyond Palantir; production of six scenario-specific playbooks for high-risk populations; expansion of the distribution audience to DV survivors, labor organizers, and election workers; and format diversification (decision trees, translations, video scripts) to reach populations for whom long-form technical documents are not accessible.

**What Phase 2 is not**: A replacement of Phase 1. The three-document corpus (threat model, playbook, implementation guide) is the foundation. Phase 2 builds depth, breadth, and format variety on top of it.

**Recommended sequencing**:

1. Immediately (before Tier 1 launch or concurrently): Update opsec-playbook.md to add Mobile Fortify field biometrics context (one paragraph). Update implementation-guide.md to add the BFU/AFU distinction and auto-reboot configuration for device seizure scenarios. These are not Phase 2 content — they are corrections to Phase 1 accuracy.

2. July 26, 2026 (quarterly review): Publish threat model updates for Mobile Fortify, drone surveillance, HART biometrics, and post-SCOTUS DOGE/SSA status. Publish the immigration advocacy scenario playbook (first Phase 2 content deliverable).

3. Months 3–6 (after Week 7 adoption gate): Produce remaining scenario playbooks in the sequence in Section 5. Begin Phase 2 audience expansion outreach.

4. Months 7–12 (contingent on adoption data): Format diversification (Spanish translation, decision trees) and video primer scripting.

**The single most important Phase 2 finding**: The threat has expanded faster than the countermeasures. Drone aerial surveillance, Mobile Fortify handheld biometrics, and Cellebrite's Signal extraction module are all operational capabilities not addressed in the Phase 1 corpus. They do not invalidate any Phase 1 guidance — GrapheneOS, Signal, and data broker opt-outs remain the correct countermeasures. But the threat model framing needs to accurately reflect the 2026 operational landscape, and three specific sections of the existing corpus need updates before wide distribution.

---

## Sources

- [FedScoop — FBI AI biometric expansion, 50 AI use cases](https://fedscoop.com/fbi-ai-inventory-law-enforcement-biometric-facial-recognition/)
- [The Intercept — FBI AI surveillance drones RFI November 2025](https://theintercept.com/2025/11/21/fbi-ai-surveillance-drones-facial-recognition/)
- [Biometric Update — Mobile Fortify NEC vendor confirmed](https://www.biometricupdate.com/202601/ice-facial-recognition-app-mobile-fortify-powered-by-nec)
- [404 Media — Mobile Fortify leaked user manual and emails](https://www.404media.co/ice-is-using-a-new-facial-recognition-app-to-identify-people-leaked-emails-show/)
- [EFF — Rights organizations demand halt to Mobile Fortify](https://www.eff.org/deeplinks/2025/11/rights-organizations-demand-halt-mobile-fortify-ices-handheld-face-recognition)
- [Nextgov — DHS biometrics expansion proposal November 2025](https://www.nextgov.com/policy/2025/11/dhs-proposes-biometrics-expansion-immigrants-dropping-age-restrictions-and-requiring-biometrics-some-us-citizens/409274/)
- [Biometric Update — Congress deepens DHS biometrics investment $271M FY26](https://www.biometricupdate.com/202601/congress-deepens-investment-in-dhs-biometrics)
- [ACE — HART DHS AI biometric tracking explained](https://ace-usa.org/blog/research/research-technology/hart-explained-dhss-plan-to-use-ai-in-biometric-tracking/)
- [The Intercept — LAPD Skydio drone surveillance No Kings protest April 2026](https://theintercept.com/2026/04/20/lapd-skydio-drone-surveillance-no-kings-protest-ice/)
- [DronexL — ICE $85 billion surveillance Skydio protest drones](https://dronexl.co/2026/02/02/ices-surveillance-skydio-drones/)
- [ACLU — Drones for intimidation](https://www.aclu.org/news/privacy-technology/drones-for-intimidation)
- [Palabra — Predator drones shift to protest surveillance](https://www.palabranahj.org/archive/predator-drones-shift-from-border-patrol-to-protest-surveillance)
- [ScienceDirect — Forensic analysis of GrapheneOS 2026](https://www.sciencedirect.com/science/article/pii/S2666281726000053)
- [EFF — ICE surveillance shopping spree (Cellebrite $11M contract)](https://www.eff.org/deeplinks/2026/01/ice-going-surveillance-shopping-spree)
- [Democracy Docket — Supreme Court allows DOGE SSA data access](https://www.democracydocket.com/news-alerts/supreme-court-allows-doge-to-access-social-security-data/)
- [Nextgov — Fourth Circuit removes limits on DOGE SSA access April 2026](https://www.nextgov.com/digital-government/2026/04/appeals-court-removes-limits-doge-access-ssa-data-despite-alarming-revelations/412786/)
- [Axios — DOGE employees may have improperly accessed SSA data](https://www.axios.com/2026/01/20/doge-employees-social-security-information-court-filing)
- [State of Surveillance — DOGE 12 lawsuits centralized database](https://stateofsurveillance.org/news/doge-privacy-act-lawsuits-centralized-database-government-surveillance-2026/)
- [SecureDrop — 2025 year in review, mobile app and protocol](https://freedom.press/tech/news/securedrop-looking-back-at-2025/)
- [Freedom of the Press Foundation — 2026 journalist digital security checklist](https://freedom.press/digisec/blog/journalists-digital-security-checklist/)
- [Government Accountability Project — immigration whistleblower support](https://whistleblower.org/immigration/)
- [State of Surveillance — Advanced OPSEC surveillance-resistant digital life](https://stateofsurveillance.org/guides/advanced/surveillance-resistant-digital-life/)
- [State of Surveillance — Protest without surveillance guide 2025](https://stateofsurveillance.org/guides/advanced/protest-without-surveillance/)
- [State of Surveillance — How to defeat facial recognition 2025](https://stateofsurveillance.org/guides/advanced/how-to-defeat-facial-recognition/)
- [TechPolicy.Press — How ICE will spy on protesters, how to protect privacy](https://www.techpolicy.press/how-ice-will-spy-on-protesters-and-how-you-can-protect-your-privacy/)
- [Blockhead — Sanctions evasion through crypto surged 694% in 2025](https://www.blockhead.co/2026/03/06/sanctions-evasion-through-crypto-surged-sevenfold-in-2025-chainalysis-report-shows/)
- [CCN — 10 countries restricting Monero/Zcash 2026](https://www.ccn.com/education/crypto/countries-banning-monero-zcash-2026/)
- [ImmpolicyTracking — ICE launches Mobile Fortify facial recognition app](https://immpolicytracking.org/policies/ice-launches-new-facial-recognition-app-to-identify-people/)
- [NPR — ICE agents have new tools including Mobile Fortify November 2025](https://www.npr.org/2025/11/08/nx-s1-5585691/ice-facial-recognition-immigration-tracking-spyware)

---

*Created: 2026-05-06. All research conducted using public sources as of May 2026. Confidence level: high on confirmed capabilities and court rulings; medium on operational deployment scope for systems reported via single-source journalism. Quarterly update checkpoint: July 26, 2026.*

---

## Playbook Completion Status

**Status updated: 2026-05-07**

All six scenario playbooks are now complete. The production sequence originally specified in Section 5 was compressed into a single session given availability of research and automation.

| Playbook | File | Status | Word Count | Session |
|---|---|---|---|---|
| 1. Immigration Surveillance Evasion | `phase-2-immigration-surveillance-evasion-playbook.md` | Complete — v1.1 | ~3,200 | 875 |
| 2. Activist Organizing Security | `phase-2-activist-organizing-security-playbook.md` | Complete — v1.1 | ~3,400 | 875 |
| 3. Financial Resistance | `phase-2-financial-resistance-playbook.md` | Complete — v1.0 | ~3,500 | 882 |
| 4. Institutional Whistleblowing | `phase-2-whistleblowing-playbook.md` | Complete — v1.0 | ~3,700 | 882 |
| 5. Journalist Security | `phase-2-journalist-security-playbook.md` | Complete — v1.0 | ~3,600 | 882 |
| 6. DV Survivor Safety | `phase-2-dv-survivor-safety-playbook.md` | Complete — v1.0 | ~3,800 | 882 |

**All six playbooks are now production-ready for Tier 2 pilot launch.**

### Distribution Readiness by Playbook

**Ready for immediate distribution (pending Week 7 gate)**:
- Immigration Surveillance Evasion: Distribute through Tier 1 legal aid organizations already in outreach pipeline
- Activist Organizing Security: Distribute through Tier 2 digital rights and civil liberties organizations
- Journalist Security: Distribute through Tier 2 journalist organizations (CPJ, Freedom of the Press Foundation, SPJ, newsroom security teams)
- Institutional Whistleblowing: Distribute through Government Accountability Project, National Whistleblower Center, and SecureDrop newsroom network

**Requires separate outreach infrastructure (Tier 3 expansion track)**:
- Financial Resistance: Distribute through nonprofit attorneys, advocacy organizations, labor union organizing departments; no single distribution channel but broad applicability
- DV Survivor Safety: Requires separate NNEDV/DV coalition outreach (NNEDV Safety Net Project, state DV coalitions, VAWA-funded programs); do not distribute through Tier 1–2 general channels — this audience needs DV-advocate-mediated distribution

### Remaining Phase 2 Work

Per Section 5 timeline, remaining work after playbook production:

- **Immediately**: Threat model updates for PHASE_2_SEQUENCING_STRATEGY.md Section 8 flags (Mobile Fortify framing in opsec-playbook.md, BFU/AFU in implementation-guide.md) — these are Phase 1 corrections, not Phase 2 content
- **July 26, 2026**: Quarterly review + threat model Gist update (Mobile Fortify, drone surveillance, HART biometrics, post-SCOTUS DOGE/SSA status)
- **Month 7–9**: Tier 2 audience expansion outreach (NNEDV, AFL-CIO, NASED, NALED, NLADA, VITA)
- **Month 10–12**: Spanish translation of Part 0 (data broker opt-outs); Texas supplement decision tree; video primer scripting
