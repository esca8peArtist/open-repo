---
title: "TIER 3 Threat Model: State-Level and Sophisticated Adversaries"
project: cybersecurity-hardening
created: 2026-04-29
status: complete
confidence: high — grounded in leaked government documents, academic research, court filings, and investigative journalism
depends_on: threat-model.md, opsec-playbook.md
---

# TIER 3 Threat Model: State-Level and Sophisticated Adversaries

**Purpose**: This document extends the existing threat model (which covers Palantir-powered administrative surveillance, data broker pipelines, and standard law enforcement tools) into the territory of **sophisticated, well-resourced adversaries**: NSA/FBI with full legal authority, state intelligence services operating in or against the United States, and organized crime groups with professional technical capability. The threat actors described here can bypass many of the countermeasures that are sufficient for TIER 1 and TIER 2 protection.

**Who this applies to**: Journalists covering intelligence and national security beats; political dissidents with ties to foreign governments that the U.S. treats as adversary nations; activists whose organizing is the direct subject of federal investigation; defense attorneys in national security cases; sources who have provided highly classified information to media; people targeted by hostile foreign intelligence services.

**Scope**: This is a capabilities document, not a legal analysis. The goal is accurate threat modeling — understanding what adversaries can actually do — so that countermeasures can be calibrated correctly.

> **Tier 1-2 Foundation**: This document assumes familiarity with the TIER 1-2 threat environment: commercial data broker pipelines, Palantir ELITE/ICM/ImmigrationOS, social media monitoring, standard subpoena process, and IMSI catchers. Those threats remain active at TIER 3; they are not replaced by the advanced capabilities described here. TIER 3 actors add layers on top of TIER 1-2 infrastructure.

---

## I. Threat Actor Profiles

### A. NSA: Signals Intelligence at Scale

The National Security Agency is the primary U.S. government signals intelligence (SIGINT) entity. Its capabilities are the most comprehensively documented of any intelligence agency, partly due to the Snowden disclosures (2013) and partly due to Congressional testimony in subsequent years.

**Core authorities**:

- **Section 702 of FISA (50 U.S.C. § 1881a)**: Permits warrantless collection targeting foreigners overseas when collection occurs in the U.S. — meaning, from U.S. telecommunications infrastructure. As of 2025, the NSA had **349,823 surveillance targets** under Section 702. The critical point for U.S. persons: collection "inevitably sweeps in" Americans' communications when they communicate with foreign targets. The FBI is then authorized to query this data. A federal district court ruled in February 2025 that FBI queries of Section 702 data using U.S.-person identifiers require a warrant — but compliance with this ruling is actively contested and the FISA Court's oversight is classified. ([Brennan Center for Justice](https://www.brennancenter.org/our-work/research-reports/section-702-foreign-intelligence-surveillance-act-fisa-2026-resource-page), [CNBC, April 2026](https://www.cnbc.com/2026/04/17/section-702-fisa-congress-surveillance.html))

- **Executive Order 12333**: Permits collection of foreign intelligence outside U.S. borders, with significantly fewer restrictions than FISA. Used for bulk collection from undersea cables and foreign telecommunications infrastructure. Most of the NSA's actual collection volume occurs under EO 12333, which has essentially no judicial oversight.

**Technical collection systems**:

- **PRISM**: Direct collection from service providers — Google, Apple, Microsoft, Facebook/Meta, Yahoo, Skype, YouTube, AOL, and PalTalk. Under PRISM, the NSA receives content (emails, chats, photos, documents) stored on provider servers. Disclosed 2013 in Snowden documents. Still operational. ([ACLU PRISM analysis](https://www.aclu.org/news/national-security/guide-what-we-now-know-about-nsas-dragnet-searches-your))

- **XKEYSCORE / Upstream Collection**: The NSA intercepts communications directly from the **internet backbone** — the fiber optic cables and routing infrastructure that carry the world's internet traffic. Room 641A at AT&T's San Francisco facility, confirmed in 2006, is a documented example of a domestic intercept point. XKeyscore allows analysts to search content and metadata by email, phone number, IP address, keyword, or browser type **without prior authorization for each search**. As of 2008, the system had 150 field sites and 700+ servers globally. ([The Intercept](https://theintercept.com/2015/07/01/nsas-google-worlds-private-communications/), [Wikipedia — Upstream collection](https://en.wikipedia.org/wiki/Upstream_collection))

**Practical implication**: Unencrypted communications (email, SMS, standard calls) transiting U.S. internet infrastructure should be assumed to be available to NSA analysts. Properly implemented end-to-end encryption defeats content collection but not metadata collection (who communicates with whom, when, from what IP address, how often).

---

### B. FBI: Targeted Investigation with Legal Authority

Where the NSA operates at mass collection scale, the FBI focuses on targeted investigation of specific individuals using a broader legal toolkit than local law enforcement.

**Key authorities beyond standard law enforcement**:

- **National Security Letters (NSLs)**: Administrative subpoenas issued by the FBI without judicial approval, requiring telecommunications providers, financial institutions, and credit agencies to produce records. NSLs contain a gag order prohibiting the recipient from disclosing the request. Signal disclosed (in response to published orders) that it received NSLs and could provide only account creation date and last connection date — because that is all it retains. ([Signal's transparency](https://signal.org/bigbrother/), opsec-playbook.md §1.1)

- **FISA Title I warrants**: Full-content surveillance orders from the FISA Court, used for individuals assessed as agents of foreign powers. These orders compel carriers and device manufacturers to assist — with no disclosure to the target. The gag mechanism is indefinite by default.

- **Section 702 backdoor searches**: As described above, the FBI queries NSA-collected data using U.S.-person identifiers. Congressional testimony in late 2025 and early 2026 confirmed that FBI agents have used Section 702 queries to search for communications of protesters, members of Congress, congressional staff, journalists, and 19,000 donors to a political campaign. ([Brennan Center testimony, December 2025](https://www.brennancenter.org/our-work/research-reports/testimony-reforming-section-702-foreign-intelligence-surveillance-act))

- **Parallel construction**: A documented FBI practice where evidence obtained through classified surveillance is "laundered" through parallel, discoverable investigative methods so that the original collection method is never disclosed in court. This makes it impossible for defense counsel to challenge the original collection. ([Reuters investigation on DEA parallel construction](https://www.reuters.com/article/us-dea-sod-idUSBRE97409R20130805))

**Device forensics at arrest or search warrant**: When the FBI executes a search warrant and seizes devices, they have access to a full forensic laboratory and no time pressure. This is categorically different from a traffic stop or border encounter.

---

### C. CBP/DHS: Border Search Authority

Customs and Border Protection has extraordinary legal authority at and near borders that does not apply domestically.

**Legal framework**:

- The **border search exception** to the Fourth Amendment permits CBP to search travelers and their belongings, including electronic devices, without a warrant or probable cause. This applies at ports of entry and at the **"functional border"** — any location within 100 miles of an international border. Approximately two-thirds of the U.S. population lives within this zone.

- CBP Directive 3340-049A divides device searches into:
  - **Basic search**: Manual examination of an unlocked device, no suspicion required.
  - **Advanced search**: Connecting the device to forensic equipment (Cellebrite UFED, Magnet Axiom) for full extraction. Requires "reasonable suspicion" as a policy matter — but this is an internal CBP policy standard, not a constitutional requirement, and is not enforced externally.

- In FY2024, CBP conducted **47,047** device searches: 42,725 basic and 4,322 advanced. ([CBP official statistics](https://www.cbp.gov/travel/cbp-search-authority/border-search-electronic-devices), [DHS Directive, November 2024](https://www.dhs.gov/sites/default/files/2025-02/2024_1126_cbp_border_searches_of_electronic_devices_at_ports_of_entry.pdf))

- **Current legal challenge**: The Riley v. California (2014) Supreme Court ruling required warrants for phone searches incident to arrest, and some circuit courts have applied this reasoning to border searches. However, the circuit courts are split, and the Supreme Court has not directly resolved the border context. The Fifth Circuit declined to require a warrant for border device searches. CBP currently operates as if advanced searches require only internal policy compliance, not a warrant.

**Practical implication**: Any device that crosses the U.S. border — or that a traveler carries into the United States — is subject to forensic extraction without warrant. A device that contains unencrypted data or that can be accessed once unlocked is exposed at border crossing points.

---

### D. State Intelligence Services (Foreign Adversaries)

The U.S. Department of Homeland Security has confirmed that foreign intelligence services from **China, Iran, Israel, Russia, and Saudi Arabia** have exploited SS7 vulnerabilities to track individuals on U.S. soil. ([TechCrunch — SS7 surveillance vendor](https://techcrunch.com/2025/07/18/a-surveillance-vendor-was-caught-exploiting-a-new-ss7-attack-to-track-peoples-phone-locations/))

These actors are relevant to:
- Journalists covering foreign governments or their intelligence services
- Dissidents from those countries residing in the U.S.
- Dual nationals
- Anyone with professional ties to entities those governments consider adversarial

Foreign intelligence services operate outside U.S. law and have no legal restrictions on their methods within the U.S. beyond what they can practically evade. Their technical capabilities frequently equal or exceed domestic law enforcement tools.

---

### E. Organized Crime with Technical Capability

The most capable organized crime groups — including groups operating as proxies for nation-states or with former intelligence service personnel — can access:

- **Commercial spyware** (Pegasus, Predator, FinFisher): State-grade zero-click mobile exploits available for purchase to well-funded criminal or quasi-state actors. Pegasus was confirmed deployed against journalists, attorneys, and activists in the U.S. by Citizen Lab research.
- **SS7 intercept services**: Available on criminal marketplaces to any buyer with sufficient funds. Used in confirmed 2024 banking fraud operations across Europe that drained millions of euros from accounts.
- **Physical surveillance and social engineering**: More reliable than technical interception for most organized crime threat profiles.

The Europol [IOCTA 2024](https://www.europol.europa.eu/publication-events/main-reports/internet-organised-crime-threat-assessment-iocta-2024) documents the increasing sophistication of organized criminal groups, including the blurring of lines between criminal organizations, cybercrime-as-a-service providers, and state-linked groups.

---

## II. Expanded Attack Surface

### A. Phone Network Interception: SS7 and 3GPP Attacks

**What SS7 is**: Signaling System 7 is the protocol suite that manages call routing, SMS delivery, and roaming authentication across cellular networks globally. It was designed in 1975 with an assumption that only trusted parties (carriers) would have access. That assumption is now false.

**Current attack capabilities** (confirmed in academic research and commercial deployment):

1. **Location tracking**: Using `ProvideSubscriberInfo` messages, an attacker with SS7 access can query any carrier's network for the physical location of a subscriber, typically to the nearest cell tower. In urban areas this can narrow to a few hundred meters. A 2025 incident confirmed a commercial surveillance vendor was exploiting a new SS7 bypass to track individuals this way. ([TechCrunch, July 2025](https://techcrunch.com/2025/07/18/a-surveillance-vendor-was-caught-exploiting-a-new-ss7-attack-to-track-peoples-phone-locations/))

2. **SMS interception**: `SendRoutingInfoForSM` queries allow an attacker to redirect SMS delivery, capturing one-time passcodes, authentication codes, and message content. This defeats SMS-based two-factor authentication entirely and explains why security guidance universally recommends TOTP authenticators or hardware keys over SMS 2FA.

3. **Call interception**: Calls can be rerouted through attacker-controlled infrastructure using SS7 manipulation. This requires more sophisticated access than location tracking but is within documented capability.

4. **Denial of service**: A target's phone can be de-registered from the network, preventing incoming calls and messages, using SS7 commands.

**Who has SS7 access**: Legitimate access is limited to licensed telecommunications carriers. However, research and journalism confirm that:
- Some governments have direct or compelled access through their domestic carriers
- Commercial "roaming aggregators" provide SS7 access to many parties with limited vetting
- SS7 access can be purchased on criminal marketplaces
- Surveillance vendors sell SS7-based tracking services

**5G transition (3GPP)**: 5G's Diameter and HTTP/2-based signaling protocols address some SS7 weaknesses but introduce new attack surfaces. 4G (LTE) Diameter protocol has documented vulnerabilities analogous to SS7. Full 5G SA (standalone) architecture improves security, but most deployments currently use 5G NSA (non-standalone) which falls back to 4G core — retaining SS7/Diameter exposure. The transition will take years to complete globally. ([SOCRadar SS7 analysis](https://socradar.io/blog/why-ss7-attacks-are-the-biggest-threat-to-mobile-security-exploiting-global-telecom-networks/), [63Sats SS7 vs GTP analysis](https://63sats.com/blog/ss7-vs-gtp-from-listening-to-calls-to-hijacking-5g-internet))

**Countermeasure implication**: SS7 attacks are **carrier-level** and cannot be defeated by anything installed on the phone. They affect the signaling layer, not the device. The only effective countermeasures are: (1) not using the standard phone number/carrier system for communications; (2) encrypting all communications end-to-end so that intercepted content is ciphertext; (3) using hardware security keys or TOTP rather than SMS 2FA.

---

### B. Hardware Keyloggers and Physical Implants

**What they are**: Devices inserted into the hardware path between a keyboard and a computer (or embedded in peripherals) that capture every keystroke before encryption occurs. Since keystrokes are captured before any software encryption layer, even full-disk encryption and strong authentication are defeated.

**Confirmed capabilities**:

- Inline USB keyloggers (KeyGrabber Forensic, AirDrive series) are commercially available tools used by law enforcement with physical access to a target's workspace. They capture keystrokes to onboard storage or transmit via Wi-Fi.
- The NSA's ANT catalog (compiled 2008-2009, disclosed by Snowden) documented modified USB cables with embedded radio transceivers (`COTTONMOUTH-I`), modified keyboard chips with data capture capability, and replacement device interfaces containing implants. These were TAO (Tailored Access Operations) tools. ([ANT catalog — Grokipedia](https://grokipedia.com/page/ANT_catalog))
- The O.MG Cable (publicly available red team tool) demonstrates the current commodity state of cable implants: a USB-C or Lightning cable indistinguishable by appearance from a legitimate cable, containing a microcontroller capable of executing commands on a connected device and transmitting over Wi-Fi. ([Hak5 O.MG Cable](https://shop.hak5.org/products/omg-cable))

**When this applies**: Hardware implants require **physical access** to a target's workspace. They are used in the context of: covert entry search (court-authorized "black bag" operations), compromised supply chains (see §II.C), or interception of devices in transit. Physical access is a prerequisite — this threat is relevant to people under active, targeted investigation with judicial authorization for covert search.

**Countermeasure implication**: Tamper-evident sealing of device ports, physical inspection of peripherals before use, and ideally a dedicated air-gapped system for the most sensitive work defeats most hardware implant vectors. Physical workspace security is as important as software security at this tier.

---

### C. Supply Chain Compromise

**Hardware interdiction**: The NSA's Tailored Access Operations unit documented practice of intercepting equipment during shipping to targets, installing firmware or hardware implants, then repackaging and forwarding. The ANT catalog described this as standard procedure for high-value targets. The disclosed tools included firmware implants for Dell PowerEdge servers (`DEITYBOUNCE`) that survived OS reinstallation by persisting in BIOS/SMM. ([The Privacy Issue — hardware supply chain](https://theprivacyissue.com/government-surveillance/pwned-on-arrival-hardware-supply-chain))

**UEFI firmware implants**: Modern firmware implants (ESPecter, 2021) can persist across OS reinstallation and disk replacement by residing in the UEFI/EFI System Partition. These are deployed by both nation-state actors and sophisticated criminal groups. Survival through a clean OS install is the key capability — standard remediation procedures (reformat, reinstall) do not remove them. ([ESET UEFI malware analysis](https://www.welivesecurity.com/2017/10/19/malware-firmware-exploit-sense-security/))

**Software supply chain**: Compromise of software development infrastructure (SolarWinds 2020, Codecov 2021, XZ Utils 2024) allows malicious code to be distributed through legitimate update channels to thousands of targets simultaneously. This is primarily a nation-state technique. For individuals, the relevant variant is: receiving a device or software from someone who has compromised it, or using software from repositories that have been compromised upstream.

**Countermeasure implication**: Purchase hardware through unpredictable channels (in-person, cash, not delivered to home address). Verify firmware integrity where tools exist to do so. For the highest-sensitivity work, use hardware that has never connected to any network since delivery and whose firmware can be verified. Do not use devices with unknown provenance.

---

### D. Forensic Extraction Toolkits

When a device is physically seized, the following tools are in standard law enforcement deployment:

**Cellebrite UFED (Universal Forensic Extraction Device)**:
- The dominant law enforcement mobile forensics platform, supporting 30,000+ device models
- Capabilities include: logical extraction, file system extraction, physical extraction (full flash memory), deleted data recovery, bypassing PINs and biometric locks
- DHS published test results for Cellebrite UFED4PC v7.69.0.1397 in April 2025, confirming current operational status ([DHS test results, April 2025](https://www.dhs.gov/sites/default/files/2025-04/25_0424_st_test_results_for_mobile_device_acquisition_tool-cellebrite_ufed4pc_v7.69.0.1397-pa_v7.68.0.25.pdf))
- Android support as of February 2025: variable by model. Most Samsung, Motorola, and older Android devices are more exposed than current Google Pixel running GrapheneOS. ([Osservatorio Nessuno — Cellebrite Android analysis](https://osservatorionessuno.org/blog/2025/03/a-deep-dive-into-cellebrite-android-support-as-of-february-2025/))

**Magnet GrayKey (now Magnet Forensics)**:
- Focused on iOS and modern Android extraction
- Against iOS 18 and iOS 18.0.1: partial extraction only from iPhone 12–16 series. "Partial" likely means unencrypted files, file metadata, and folder structure — not decrypted app data
- Against iOS 18.1 and later: GrayKey reportedly cannot extract any data — this was confirmed in the November 2024 leak and subsequent analysis
- iPhone 11 and older: **full extraction** confirmed
- Pixel 9: partial data, only in After First Unlock (AFU) state
- The tool is updated continuously; a gap that exists today may close in months ([Schneier on Security — GrayKey capabilities](https://www.schneier.com/blog/archives/2024/11/what-graykey-can-and-cant-unlock.html), [Freedom of the Press Foundation](https://freedom.press/digisec/blog/new-leaks-on-police-phone-unlocking-tech/), [MacRumors iOS 18 analysis](https://www.macrumors.com/2024/11/19/graykey-ios-18-partial-unlock/))

**Magnet Axiom**:
- Analytics and analysis platform that processes extractions from Cellebrite, GrayKey, and other tools
- Provides AI-powered analysis, timeline reconstruction, connection mapping, and cloud data acquisition
- Integrates cloud evidence: iCloud, Google Drive, Facebook, Instagram, Uber, and dozens of other service providers — cloud data often bypasses device encryption entirely
- Can recover deleted data and unallocated space if a physical extraction is available
- DHS test results for Axiom v8.1.0 published March 2025 ([DHS — Axiom v8.1.0 test results](https://www.dhs.gov/sites/default/files/2025-03/25_0324_st_test_results_for_mobile_device_acquisition_tool-magnet_axiom_v8.1.0.42087.pdf), [Magnet Forensics product page](https://www.magnetforensics.com/products/magnet-axiom/))

**NIST SP 800-101 Rev. 1 — Federal Forensic Standard**:
The National Institute of Standards and Technology's Guidelines on Mobile Device Forensics defines the five-level acquisition hierarchy used by U.S. federal forensic examiners: Manual → Logical → File System → Physical → Chip-off. Chip-off forensics — physically removing and directly reading flash memory chips — can recover data even from locked devices if hardware encryption is weak or keys are stored improperly. ([NIST CSRC — SP 800-101 Rev. 1](https://csrc.nist.gov/pubs/sp/800/101/r1/final))

**Countermeasure state-of-play as of April 2026**:
- iPhone running **iOS 18.1 or later + strong numeric PIN (not biometric)**: GrayKey partial or no extraction. Biometrics are compellable in most U.S. jurisdictions under current case law; PINs may be protected by Fifth Amendment (circuit split). **Critical**: enable iPhone's automatic reboot after 72 hours without unlock (iOS 18+) — this returns the device to Before First Unlock (BFU) state, which defeats AFU-dependent tools.
- **Google Pixel running GrapheneOS**: Provides the strongest Android forensic resistance. Secure Element (Titan M2) rate-limits PIN attempts and can auto-wipe after a configurable number of failures. However: GrayKey and Cellebrite continue to invest in Pixel support. The gap is real but not permanent.
- **Samsung Knox**: Less resistance than Pixel/GrapheneOS. Cellebrite has demonstrated fuller extraction capability against Samsung devices.

---

### E. Signals Intelligence: Backbone and RF Collection

Beyond SS7, signals intelligence includes:

**Radio frequency (RF) interception**: IMSI catchers (Stingray, Crossbow) force phones to connect to attacker-controlled base stations, capturing device identifiers, location, and (with some models) call content. These are TIER 2 threats addressed in opsec-playbook.md. At TIER 3, state-level actors can deploy passive RF collection at scale without a detectable active device.

**Tor deanonymization research**: Academic and government research has shown that **traffic analysis attacks** against Tor can correlate entry and exit traffic patterns to deanonymize users — without breaking Tor's encryption. The FBI and NSA have confirmed research into Tor deanonymization. The practical implication is that Tor provides strong anonymity against local network observers but may be vulnerable to a global passive adversary (one who can observe both the entry and exit points simultaneously). For most operational purposes, Tor remains the best available tool. For nation-state adversaries with global surveillance infrastructure, Tor's anonymity guarantee weakens.

**End-to-end encrypted metadata**: Even when content is encrypted, the metadata of who communicates with whom, when, and from what IP address is visible to carriers, ISPs, and upstream infrastructure. NSA upstream collection captures this metadata at scale. Tor and VPNs address IP-layer metadata; Signal and similar apps conceal content but carrier metadata (connection to Signal servers, timing) remains visible to your carrier and can be obtained via NSL.

---

### F. Communication Sabotage Vectors

**Signal-specific threats at TIER 3**:

1. **Linked device injection**: The primary real-world attack against Signal accounts is adding an attacker-controlled device as a "linked device." This was confirmed as an active Russian intelligence technique in 2025, using malicious QR codes disguised as group invite links. A compromised linked device receives all messages in real time without the phone being physically seized. ([Security Magazine — Signal vulnerabilities](https://www.securitymagazine.com/articles/101539-behind-the-signal-leak-vulnerabilities-in-high-security-communication), opsec-playbook.md §1.1)

2. **Desktop client exposure**: Peer-reviewed research found Signal Desktop stores attachments locally in unencrypted form on the host filesystem. Physical access to or malware on the computer exposes all attachment content. ([LabNews Signal security analysis](https://lab-news.de/en/signal-wie-sicher-ist-der-messenger-wirklich-peer-review-studien-zeigen-schwachstellen/))

3. **Delivery receipt metadata**: A 2025 academic paper demonstrated that delivery receipts can be manipulated to reveal online/offline status patterns without the target's awareness, enabling behavioral profiling.

4. **TeleMessage / unofficial forks**: CISA added TeleMessage Signal (an unofficial, non-Signal-Foundation fork) to its Known Exploited Vulnerabilities catalog following a breach that exposed messages from U.S. government officials. Third-party Signal forks do not provide the same security guarantees as the official application. ([SC Media — TeleMessage CISA](https://www.scworld.com/news/telemessage-signal-app-lands-on-cisas-exploited-vulnerability-list))

5. **Server-side attacks**: Signal's servers do not store message content, but they do manage encrypted group membership information and sealed sender tokens. A server-side compromise would not reveal message content but could reveal social graph information. This is a theoretical concern given Signal Foundation's small size relative to the adversaries at this tier.

**UUID harvesting**: Mobile advertising identifiers (IDFA on iOS, GAID on Android) link app behavior across applications. At TIER 3, an adversary who has obtained your advertising ID through any data source can correlate your activity across apps, devices, and time periods. This is a TIER 1-2 data broker threat but operates as a persistent identifier at TIER 3 as well. Apple's App Tracking Transparency and Android's advertising ID reset options reduce but do not eliminate this vector.

---

## III. Practical Scenario Examples

### Scenario 1: Journalist Covering the Intelligence Community

**Profile**: A U.S.-based journalist who covers NSA, CIA, and military operations. Has received documents from a current intelligence community employee through encrypted channels. Has communicated with multiple current and former intelligence officials.

**Active threat vectors at this profile**:
- NSL for carrier metadata records showing Signal connection patterns (who the journalist connects with, when, duration) — does not require a court order
- FISA Title I application if journalist's source is designated an "agent of a foreign power" — warrant obtained ex parte from the FISA Court with no disclosure
- Section 702 query of any communications that touched a foreign server
- Subpoena to Signal (would yield only account creation date and last connection date per Signal's confirmed production)
- Physical surveillance at home and office with potential covert entry
- Covert search of computer equipment, potentially including hardware implant deployment
- Border interrogation and device search at any international travel

**Key risk**: The journalist's source is a bigger exposure than the journalist. If the source is identified and arrested, device forensics on the source's equipment may reveal the communication channel. The journalist's own device security matters less than the source's.

**Countermeasure priority**: Air-gapped document handling for received materials; source communication via out-of-band, non-attributable channels; legal retainer with a First Amendment specialist; awareness that border crossing is a search event.

---

### Scenario 2: Dissident from an Adversary Nation Living in the U.S.

**Profile**: A Chinese or Iranian national with U.S. lawful permanent resident status who is publicly critical of their home government's policies. Has attended protests. Communicates with family members in their home country.

**Active threat vectors**:
- Foreign intelligence service using SS7 attacks to track location and intercept SMS (confirmed DHS concern for China, Iran, Russia, Saudi Arabia)
- Commercial spyware (Pegasus, Predator-class) deployed via zero-click vulnerability in iMessage, WhatsApp, or browser — documented against dissidents globally
- Physical surveillance by foreign intelligence personnel operating in the U.S. (documented Chinese "police stations" and Iranian assassination plots on U.S. soil)
- U.S. government Section 702 collection on communications with contacts in the home country — the foreign contact's communications are the legal target; the U.S.-based dissident's end is incidentally collected
- FBI investigation if U.S. government believes the individual may be connected to a foreign intelligence network (even if they are not)

**Key risk**: Two simultaneous adversaries (U.S. government and foreign government) with partially aligned interests. Communications with family in the home country are intercepted by multiple parties. The phone number itself is an identifier trackable via SS7.

**Countermeasure priority**: Separation of identity — the phone number used for communications with sensitive contacts must not be tied to the person's legal identity or SIM card in a way that allows SS7 targeting. Use of Signal (not SMS) for all sensitive communications. Awareness that the threat is not only U.S. law enforcement.

---

### Scenario 3: Activist Organizing Against Federal Policy

**Profile**: A U.S. citizen organizing large-scale civil disobedience actions against ICE operations. Has communicated arrest tactics in Signal group chats. Has been identified in OSINT monitoring by DHS.

**Active threat vectors at TIER 3 (escalating from TIER 2)**:
- FISA Title I warrant is unlikely (requires foreign power connection) — but FBI predicated investigation may be opened under domestic terrorism authorities
- Grand jury subpoenas to communications platforms (Signal would produce minimal data; less secure platforms would produce substantial data)
- IMSI catchers at actions to map social networks of attendees
- Geofence warrants covering protest sites — currently in Supreme Court review, previously used to identify attendees by device location
- Informant infiltration of organizing groups — human intelligence at this scale is more reliable than technical interception
- IRS LCA platform cross-referencing financial donations to identify funders and supporters

**Key risk**: At this profile, the primary threat is human intelligence (informants) and metadata aggregation, not content interception. Signal encryption protects content; it does not protect the social graph of who is in the group, when the group was active, or who the administrators are.

**Countermeasure priority**: Group operational security — compartmentalization of information within the group (not everyone needs to know everything); separate communication channels by security level; legal structure that provides attorney-client privilege for planning communications.

---

## IV. Summary: TIER 3 Coverage and What Remains for TIER 4+

### What TIER 3 Covers

| Vector | Adversary | TIER 3 Status |
|--------|-----------|---------------|
| SS7/carrier-level phone intercept | State intelligence, organized crime | Covered — carrier-level attack, require out-of-band solution |
| Hardware keyloggers and implants | FBI TAO, state intelligence | Covered — physical access required, physical countermeasures available |
| Supply chain firmware compromise | NSA TAO, nation-states | Covered — hardware sourcing and verification protocols |
| GrayKey/Cellebrite forensics | Federal law enforcement | Covered — device configuration countermeasures documented |
| FISA 702 / NSL surveillance | FBI, NSA | Covered — provider selection and data minimization |
| Border device search | CBP | Covered — border crossing protocols |
| Signal linked-device injection | Foreign intelligence, FBI | Covered — configuration and verification practices |
| XKEYSCORE upstream collection | NSA | Covered — encryption and metadata minimization |

### What TIER 4+ Would Cover

**TIER 4 threats** are those where standard countermeasures are either unavailable, illegal to implement in a U.S. context, or require nation-state resources to counter. These include:

- **Zero-click mobile exploits (Pegasus-class)**: Exploitation of unpatched vulnerabilities in iMessage, WhatsApp, or browser engines without user interaction. Countermeasure is: keep devices fully updated (shrinks the window), use Lockdown Mode (iOS) which reduces attack surface at cost of functionality, or avoid smartphones entirely for the most sensitive communications. There is no complete defense.
- **Full SIGINT against Tor**: A global passive adversary with visibility into both Tor entry and exit nodes can deanonymize users through traffic correlation. This requires intelligence-agency-scale infrastructure and is not a practical threat to most individuals but is a real theoretical limit.
- **Chip-level hardware attacks**: Electron microscopy, focused ion beam analysis of hardware chips to extract cryptographic keys or reconstruct deleted memory content. Requires a government forensics laboratory and significant time. Applies to seized hardware in the most sensitive cases.
- **Coercion and legal compulsion**: An adversary with legal authority who has arrested the person can compel biometric authentication in most jurisdictions, and in some contexts can compel PIN disclosure (the Fifth Amendment question is not fully resolved). Technical security does not protect against legal compulsion.
- **Jurisdiction-independent SIGINT**: Intelligence sharing among Five Eyes partners (UK, Canada, Australia, New Zealand) means that communications collected "outside" the U.S. may still reach U.S. intelligence through sharing arrangements that circumvent domestic restrictions.

---

## Sources

- [Brennan Center — FISA Section 702, 2026 Resource Page](https://www.brennancenter.org/our-work/research-reports/section-702-foreign-intelligence-surveillance-act-fisa-2026-resource-page)
- [CNBC — Section 702 short-term extension, April 2026](https://www.cnbc.com/2026/04/17/section-702-fisa-congress-surveillance.html)
- [NPR — FISA Section 702 explainer, April 2026](https://www.npr.org/2026/04/14/nx-s1-5768270/what-to-know-about-section-702-surveillance)
- [Brennan Center — Congressional testimony, December 2025](https://www.brennancenter.org/our-work/research-reports/testimony-reforming-section-702-foreign-intelligence-surveillance-act)
- [The Intercept — XKeyscore analysis](https://theintercept.com/2015/07/01/nsas-google-worlds-private-communications/)
- [ACLU — NSA dragnet searches guide](https://www.aclu.org/news/national-security/guide-what-we-now-know-about-nsas-dragnet-searches-your)
- [Wikipedia — Upstream collection](https://en.wikipedia.org/wiki/Upstream_collection)
- [TechCrunch — SS7 surveillance vendor exploit, July 2025](https://techcrunch.com/2025/07/18/a-surveillance-vendor-was-caught-exploiting-a-new-ss7-attack-to-track-peoples-phone-locations/)
- [SOCRadar — SS7 threat analysis](https://socradar.io/blog/why-ss7-attacks-are-the-biggest-threat-to-mobile-security-exploiting-global-telecom-networks/)
- [63Sats — SS7 vs GTP/5G analysis](https://63sats.com/blog/ss7-vs-gtp-from-listening-to-calls-to-hijacking-5g-internet)
- [Schneier on Security — GrayKey capabilities](https://www.schneier.com/blog/archives/2024/11/what-graykey-can-and-cant-unlock.html)
- [Freedom of the Press Foundation — GrayKey leaks](https://freedom.press/digisec/blog/new-leaks-on-police-phone-unlocking-tech/)
- [MacRumors — GrayKey iOS 18 partial unlock](https://www.macrumors.com/2024/11/19/graykey-ios-18-partial-unlock/)
- [Magnet Forensics — GrayKey product page](https://www.magnetforensics.com/products/magnet-graykey/)
- [Magnet Forensics — Axiom product page](https://www.magnetforensics.com/products/magnet-axiom/)
- [DHS — Axiom v8.1.0 test results, March 2025](https://www.dhs.gov/sites/default/files/2025-03/25_0324_st_test_results_for_mobile_device_acquisition_tool-magnet_axiom_v8.1.0.42087.pdf)
- [DHS — Cellebrite UFED4PC test results, April 2025](https://www.dhs.gov/sites/default/files/2025-04/25_0424_st_test_results_for_mobile_device_acquisition_tool-cellebrite_ufed4pc_v7.69.0.1397-pa_v7.68.0.25.pdf)
- [NIST CSRC — SP 800-101 Rev. 1, Mobile Device Forensics](https://csrc.nist.gov/pubs/sp/800/101/r1/final)
- [CBP — Border Search of Electronic Devices](https://www.cbp.gov/travel/cbp-search-authority/border-search-electronic-devices)
- [DHS — CBP Border Search Directive, November 2024](https://www.dhs.gov/sites/default/files/2025-02/2024_1126_cbp_border_searches_of_electronic_devices_at_ports_of_entry.pdf)
- [ANT catalog — Grokipedia](https://grokipedia.com/page/ANT_catalog)
- [The Privacy Issue — hardware supply chain compromise](https://theprivacyissue.com/government-surveillance/pwned-on-arrival-hardware-supply-chain)
- [ESET — UEFI malware analysis](https://www.welivesecurity.com/2017/10/19/malware-firmware-exploit-sense-security/)
- [Security Magazine — Signal vulnerabilities](https://www.securitymagazine.com/articles/101539-behind-the-signal-leak-vulnerabilities-in-high-security-communication)
- [SC Media — TeleMessage CISA KEV](https://www.scworld.com/news/telemessage-signal-app-lands-on-cisas-exploited-vulnerability-list)
- [LabNews — Signal peer-reviewed vulnerabilities](https://lab-news.de/en/signal-wie-sicher-ist-der-messenger-wirklich-peer-review-studien-zeigen-schwachstellen/)
- [Europol — IOCTA 2024](https://www.europol.europa.eu/publication-events/main-reports/internet-organised-crime-threat-assessment-iocta-2024)
- [Osservatorio Nessuno — Cellebrite Android analysis, March 2025](https://osservatorionessuno.org/blog/2025/03/a-deep-dive-into-cellebrite-android-support-as-of-february-2025/)
