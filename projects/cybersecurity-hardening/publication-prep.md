---
title: "Publication Prep: OpSec Corpus (Threat Model + Playbook + Implementation Guide)"
project: cybersecurity-hardening
created: 2026-04-26
status: draft
purpose: TOC, glossary, and executive summary for the three-document corpus
---

# Publication Prep: OpSec Corpus

This file contains the publication-prep materials for the three-document cybersecurity-hardening corpus:
- `threat-model.md` — Government surveillance infrastructure (440 lines)
- `opsec-playbook.md` — Defensive countermeasures by tier
- `implementation-guide.md` — Step-by-step setup (9,600 words, 1,022 lines)

---

## Executive Summary

**Who this is for**: People in the United States who face elevated risk from government surveillance — and who need to act on that risk now, not after a theoretical future crisis. That population includes immigration advocates, healthcare workers serving undocumented people, labor organizers, protest participants, journalists, civil rights litigants, and anyone with immigration status vulnerability. It also includes ordinary people who want to understand what the government's commercial surveillance infrastructure actually looks like and what they can do about it.

**What the threat actually is**: This corpus begins with what the government can actually do — confirmed, sourced, not speculative. Palantir Technologies held $970 million in federal contracts in 2025 and is the data integration backbone connecting ICE, CBP, the IRS, the Army, and other federal agencies into a unified intelligence environment. ICE's ELITE platform uses commercial location data and address confidence scoring to generate deportation target lists at neighborhood scale, without individual warrants. The Venntel data pipeline harvests location data from ordinary smartphone apps and sells it to law enforcement. LexisNexis holds a $9.75 million DHS contract and provides ICE with historical address records. The IRS's Lead and Case Analytics platform, built by Palantir, maps social networks among investigation targets using communications metadata.

These systems are not speculation about future capabilities. They are active government programs with contract values, official documentation, and documented operational use. The threat model in this corpus is built entirely on primary sources — FOIA disclosures, government contracts, court filings, and investigative journalism.

**What you can do about it**: The countermeasure architecture in this corpus is designed to degrade the effectiveness of these specific systems, not to achieve theoretical perfect privacy. The approach is tiered. Tier 1 covers the baseline protections relevant to anyone with elevated exposure — data broker opt-outs, Signal configuration, basic device hygiene. Tier 2 adds the full technical stack: a dedicated GrapheneOS device with the ad-SDK tracking disabled at the OS level, Signal registered to a VoIP number with no carrier identity link, and a VPN-then-Tor browsing configuration. Tier 3 adds additional layers for people with reason to believe they are direct targets of active investigation.

The most important action for most people is one that requires no technical expertise: submitting opt-outs to the data brokers that law enforcement queries without a warrant. LexisNexis, BeenVerified, Spokeo, WhitePages, and fifteen other brokers feed directly or indirectly into the systems described above. Reducing your data profile in those databases degrades the confidence scoring that drives targeting decisions. This takes two to four hours, costs nothing, and is the Part 0 of the implementation guide for that reason.

**What this corpus is and is not**: Three documents working together. The threat model provides the intelligence foundation — confirmed capabilities with citations. The OpSec playbook translates those capabilities into a countermeasure strategy organized by tier. The implementation guide gives you the exact steps, in the correct order, with verification checkpoints that tell you whether each step actually worked. None of these documents assumes technical expertise for the Tier 1 sections. Tier 2 and Tier 3 assume willingness to follow detailed instructions but not prior experience with any of the tools.

This corpus does not cover: organizational security for groups (a different threat model), physical surveillance countermeasures (TSCM), international travel security, or the legal strategy around compelled decryption. Those topics are referenced as out-of-scope where relevant, with pointers to appropriate external resources.

**An honest statement of limits**: No individual countermeasure is foolproof against a targeted investigation with full government resources and a valid court order. What this corpus addresses is the bulk commercial surveillance infrastructure — the data broker pipelines, the location data market, the ad-tech tracking layer — that operates without warrants and at scale. Friction against these systems is achievable and meaningful. The goal is not to be invisible. The goal is to not be an easy target.

---

## Table of Contents — Full Corpus

### Document 1: Threat Model (`threat-model.md`)

I. The Central Threat: Palantir as the Integration Layer
- A. Scale and Financial Commitment
- B. Platform Architecture (Gotham / Foundry / AIP)
- C. Confirmed Tools: ELITE, ImmigrationOS, IRS LCA, Venntel integration

II. NSA Signals Intelligence
- Section 702 FISA surveillance (foreign-origin interception, U.S. person query rules)
- Upstream collection from internet backbone
- PRISM program scope

III. FBI Investigative Capabilities
- National Security Letters (NSLs) — no judicial approval required
- Grand jury subpoenas for Signal metadata
- FISA warrants and Section 215 records

IV. Law Enforcement Data Brokers
- LexisNexis / Accurint: $9.75M DHS contract
- Thomson-Reuters CLEAR
- Venntel and the location data market
- LexisNexis ELITE address confidence scoring pipeline

V. DOGE Data Consolidation
- Status as of April 2026
- Confirmed cross-agency database access
- Legal challenges and status

VI. Social Media Monitoring
- Babel Street: confirmed contract, keyword/social graph capabilities
- ImmigrationOS social media component
- CBP social media vetting at entry

VII. Threat Matrix
- Capability × Tier matrix (who faces what, at what probability)

---

### Document 2: OpSec Playbook (`opsec-playbook.md`)

**Part 1**: Communications Defense
- 1.1 Signal: what it protects, what it doesn't, configuration by tier
- 1.2 Email: why it is not salvageable for high-stakes communications
- 1.3 Session and Briar: offline-capable alternatives

**Part 2**: Network Anonymization
- 2.1 VPN selection criteria (jurisdiction, payment, log policy)
- 2.2 Tor: capability, limitations, traffic analysis resistance
- 2.3 VPN-then-Tor: the recommended configuration and why

**Part 3**: Device Security
- 3.1 GrapheneOS: why Android, why Pixel, what it provides
- 3.2 iOS as a Tier 1 option
- 3.3 Laptop: full-disk encryption, BIOS password, firmware security

**Part 4**: Identity Compartmentalization
- 4.1 Separate identities for separate activities
- 4.2 VoIP numbers and pseudonymous accounts
- 4.3 Payment anonymization (Monero, prepaid cards)

**Part 5**: Physical and Operational Security
- 5.1 Physical device security
- 5.2 Behavioral OpSec: what you say, to whom, over which channels
- 5.3 Border crossing and checkpoint protocols

**Part 6**: Document and File Security
- 6.1 Metadata: what files contain and how it becomes evidence
- 6.2 ExifTool and MAT2 for metadata removal
- 6.3 VeraCrypt for sensitive files at rest
- 6.4 age encryption for file transfer

**Part 7**: Social Media and Public Presence
- 7.1 What Babel Street and ImmigrationOS ingest
- 7.2 Reducing your public social media footprint
- 7.3 Protest and event security

**Part 8**: Data Broker Reduction
- 8.1 How law enforcement uses data brokers
- 8.2 The 20 highest-priority brokers
- 8.3 Automation services

**Part 9**: Legal Preparation
- 9.1 Know-your-rights framework
- 9.2 Compelled decryption: current Fifth Amendment case law
- 9.3 Incident response planning

**Part 10**: Threat Model Reassessment
- 10.1 Tier escalation signals
- 10.2 Quarterly review process

**Summary Tier Tables**

---

### Document 3: Implementation Guide (`implementation-guide.md`)

**Part 0**: Data Broker Opt-Outs (All Tiers — No Technical Expertise Required)
- Step 0.1: Federal opt-out programs (OptOutPrescreen, DMAchoice, NAI, DAA)
- Step 0.2: Data broker opt-outs by priority (20 brokers, ranked by law enforcement relevance)
- Step 0.3: Automation services (EasyOptOuts / DeleteMe)
- Verification and Troubleshooting

**Part 1**: Hardware Selection (Tier 2+)
- Step 1.1: Choosing a Pixel model (supported devices, support window table)
- Step 1.2: Where to buy (supply chain considerations by tier)
- Step 1.3: Verifying carrier-unlocked status
- Verification

**Part 2**: GrapheneOS Installation (Tier 2+)
- Step 2.1: Pre-installation checklist
- Step 2.2: Access the web installer
- Step 2.3: Connect device in fastboot mode
- Step 2.4: Run the web installer (5 stages with what-to-expect for each)
- Verification (4-point bootloader lock confirmation)
- Troubleshooting (device not found, OEM grayed out, bootloader won't lock, boot loop)

**Part 3**: Post-Install GrapheneOS Configuration (Tier 2+)
- Step 3.1: Initial setup (skip Google account; PIN not biometric)
- Step 3.2: Auto-reboot (18 hours; BFU state explanation)
- Step 3.3: Network permission controls (per-app network denial)
- Step 3.4: Sandboxed Google Play in secondary profile
- Step 3.5: Delete advertising ID
- Step 3.6: USB data controls (Cellebrite mitigation)
- Step 3.7: Screen lock timeout
- Verification checklist and Troubleshooting

**Part 4**: Signal Setup Sequence (All Tiers)
- Step 4.1: VoIP number (MySudo / Google Voice / JMP.chat, by tier)
- Step 4.2: Install Signal and register (including APK on GrapheneOS)
- Step 4.3: Phone number privacy settings (must be set before first contact)
- Step 4.4: Disappearing messages (defaults by tier)
- Step 4.5: Safety Numbers verification
- Step 4.6: Orbot routing for Signal (Tier 3 only)
- Verification (5-point test) and Troubleshooting

**Part 5**: Tor Browser and Mullvad VPN (Tier 2+)
- Step 5.1: Mullvad account setup (account number, cash/Monero/prepaid payment)
- Step 5.2: Mullvad configuration (kill switch, jurisdiction selection)
- Step 5.3: Mullvad leak test (must pass before Tor)
- Step 5.4: Tor Browser installation (official source only; signature verification)
- Step 5.5: Tor Browser security settings (Safest mode)
- Step 5.6: The VPN-then-Tor sequence (order of operations)
- Step 5.7: Behavioral rules for Tor Browser (7 rules that deanonymize if violated)
- Verification (check.torproject.org + mullvad.net/check + circuit visualization)
- Troubleshooting (not using Tor, won't connect, slow, Mullvad disconnects)

**Part 6**: File Encryption and Metadata Minimization (Tier 1+)
- Step 6.1: Document metadata stripping with ExifTool
- Step 6.2: Safer document sharing practices
- Step 6.3: VeraCrypt encrypted containers (Tier 3; Hidden Volume explanation)
- Step 6.4: age encryption for file transfer
- Verification and Troubleshooting

**Part 7**: Quick-Start Checklists by Tier
- Tier 1 Minimum Viable Setup (~10 items, 3–5 hours)
- Tier 2 Setup (adds ~12 items, 4–6 additional hours)
- Tier 3 Setup (adds ~10 items, 3–4 additional hours)

**Part 8**: Maintenance Schedule
- Monthly (15–20 min): OS updates, Tor Browser, Signal, permission review
- Quarterly (1–2 hrs): data broker re-submission, Mullvad leak re-test, threat intel review, Safety Numbers
- Annual (2–3 hrs): Mullvad account rotation, VeraCrypt passphrase rotation, device support status, legal landscape review

---

## Glossary

**ad-SDK location tracking**: Mobile apps commonly include third-party advertising software development kits (SDKs) that collect and transmit location data to advertising networks. The aggregate location data is purchased by brokers like Venntel and resold to government agencies. GrapheneOS's per-app network permission controls prevent apps from transmitting this data.

**age**: A simple, modern file encryption tool written by Filippo Valsorda. Unlike PGP, age requires no key-signing infrastructure — you encrypt to a recipient's public key and only the holder of the corresponding private key can decrypt. Appropriate for encrypting files before sharing over any channel.

**BFU (Before First Unlock)**: The state a device is in after it powers on but before the user enters their PIN or passphrase for the first time. In BFU state, the device's full-disk encryption keys are not loaded into memory. Forensic tools including Cellebrite cannot extract data from a device in BFU state without the PIN. GrapheneOS's auto-reboot feature (which can be set to 18 hours) returns the device to BFU state after inactivity.

**Babel Street**: A commercial intelligence company with confirmed law enforcement contracts. Babel Street's platform ingests social media, news, and online forum content and enables keyword search and social graph analysis. ImmigrationOS (see below) includes Babel Street-derived social media monitoring capabilities.

**bootloader**: Low-level firmware that starts the phone's operating system before Android/GrapheneOS loads. An unlocked bootloader allows any operating system to be installed. A locked bootloader verifies that only the expected, unmodified OS boots — this is called verified boot. GrapheneOS requires that the bootloader be re-locked after installation to restore verified boot protections.

**Cellebrite**: A commercial forensic company that makes devices used by law enforcement to extract data from seized mobile phones. Cellebrite tools work by establishing a USB connection to the device. GrapheneOS's USB data controls (Settings > Security > USB accessories > No new USB accessories) prevent new USB connections while the screen is locked, limiting Cellebrite's primary attack vector.

**CISA (Cybersecurity and Infrastructure Security Agency)**: A U.S. federal agency within DHS responsible for national cyber defense. CISA's 2025 communications security guidance (relevant after the Salt Typhoon telecom compromise) recommends encrypted messaging apps, including Signal, for sensitive communications.

**Diceware**: A method for generating strong, memorable passphrases by rolling dice to select words from a standardized word list (the EFF's word list is the standard). A six-word diceware passphrase has approximately 77 bits of entropy — more than sufficient for VeraCrypt containers and KeePassXC master passphrases.

**disappearing messages**: A Signal feature that automatically deletes messages after a set time period (options from 30 seconds to 4 weeks). Activated per-conversation or as a system-wide default. If a device is seized, disappearing messages limit how far back conversation history extends. Signal encrypts message content, but once a device is unlocked, the content is accessible — disappearing messages reduce the exposure window.

**ELITE (Enhanced Leads Identification and Targeting for Enforcement)**: A Palantir platform deployed for ICE under a $29.9 million contract (2025–2026+). ELITE displays potential deportation targets as pins on a map, generates "address confidence scores" indicating how likely an individual is to be at a given address, and integrates location data from commercial data brokers, LexisNexis Accurint, and DMV records. Confirmed in operation in 2026; described by ICE as an "operational leads management" tool.

**ExifTool**: A free command-line tool for reading and modifying file metadata. Works on documents, images, PDFs, and most other file types. Used to strip author names, GPS coordinates, creation timestamps, edit history, and machine names from files before sharing them. Available for macOS, Windows, and Linux.

**fastboot mode**: A low-level phone mode that allows communication between the phone and a computer for bootloader operations. Entered by holding Volume Down + Power simultaneously during startup. Required for GrapheneOS installation and for unlocking/relocking the bootloader.

**F-Droid**: An open-source app store for Android (and GrapheneOS). Hosts free and open-source software only, with no tracking or advertising. Signal and Orbot are available on F-Droid. On GrapheneOS, F-Droid is the preferred source for security-critical apps to avoid the Google Play ecosystem.

**forward secrecy**: A cryptographic property where session keys are deleted after each session, so that a future compromise of a long-term key cannot decrypt past sessions. Signal's Double Ratchet protocol provides forward secrecy: if a session key is later compromised, historical messages remain encrypted.

**GrapheneOS**: A privacy- and security-hardened Android operating system. Runs on Google Pixel phones. Key additions over stock Android include: per-app network permission controls (denying internet access to apps that don't need it), per-app storage scope controls, a hardened memory allocator, verified boot on re-locked bootloader, and auto-reboot to BFU state. Does not include Google Play Services at the system level — Google Play can be installed in sandboxed form in a secondary user profile.

**ImmigrationOS**: A Palantir platform under a $30 million ICE contract (April 2025; prototype due September 2025). Designed to aggregate immigration enforcement data from multiple government databases into a unified "end-to-end" lifecycle tracking system for immigrants. Includes social media monitoring capabilities derived from Babel Street data.

**IMEI (International Mobile Equipment Identity)**: A unique identifier assigned to every mobile phone at manufacture. Tied to the device itself, not the SIM. Law enforcement can request carrier records associated with an IMEI, and IMSI catchers can capture IMEI data from nearby devices. Buying a device for security purposes with cash (Tier 3) prevents the purchase record from linking your identity to the device's IMEI.

**IMSI catcher (Stingray)**: A device that mimics a cell tower to intercept communications from nearby phones. Can collect the IMSI (a SIM card identifier) and IMEI of all phones in range, enabling identification of who was present at a location. Used by federal law enforcement and some local police departments. Tor/VPN configurations do not protect against IMSI catchers because the attack occurs at the cellular network layer, not the internet protocol layer.

**kill switch (VPN)**: A VPN feature that blocks all internet traffic if the VPN connection drops unexpectedly, preventing momentary exposure of your real IP address. Mullvad's kill switch is enabled by default and cannot be disabled.

**KeePassXC**: A free, open-source password manager. Stores passwords in an encrypted database file that you control — unlike cloud-based password managers, the database is not held by a third party. Available for macOS, Windows, and Linux. Recommended for storing Mullvad account numbers, VeraCrypt container passphrases, and other sensitive credentials.

**LCA (Lead and Case Analytics)**: A Palantir platform built for the IRS Criminal Investigation division under a $130 million contract. Maps social networks among investigation targets using communications metadata (calls, texts, emails). The existence of this platform means that IRS CI has analytical capabilities beyond traditional financial investigation.

**LexisNexis Accurint**: A data aggregation platform operated by LexisNexis. Holds a confirmed $9.75 million DHS contract giving ICE access to its database. Accurint ingests DMV records, address history, criminal records, professional licenses, property records, and other public data. Palantir's ELITE platform integrates Accurint data for address confidence scoring.

**MAT2 (Metadata Anonymisation Toolkit 2)**: A GUI tool for stripping metadata from files. Available by default in Tails OS and installable on Ubuntu/Debian. Performs the same function as ExifTool but with a drag-and-drop interface.

**MAIDS (Mobile Advertising ID)**: A persistent identifier assigned to a mobile device by the operating system and used by advertising networks to track behavior across apps. In Android, this is called the GAID (Google Advertising ID). Venntel and similar location data brokers use MAIDs to link location data from different apps to a single device/person. Deleting the advertising ID (Settings > Privacy > Ads > Delete advertising ID on GrapheneOS) severs this persistent identifier.

**MLAT (Mutual Legal Assistance Treaty)**: The legal mechanism by which U.S. law enforcement must request data from companies based in foreign jurisdictions (e.g., Mullvad in Sweden). MLAT process is substantially slower and more procedurally demanding than an NSL or subpoena served domestically. Choosing a VPN provider in a non-U.S. jurisdiction is partly a strategy to impose MLAT requirements on any U.S. government data request.

**Monero (XMR)**: A privacy-focused cryptocurrency with confidential transactions (amounts hidden), stealth addresses (recipient unlinkable), and ring signatures (sender unlinkable). Unlike Bitcoin, Monero transactions are not publicly traceable by design. Used in this corpus as the recommended payment method for Mullvad when financial privacy is a concern.

**Mullvad**: A Swedish VPN provider with a confirmed no-log policy (Swedish authorities have attempted to compel user data and received nothing). Mullvad does not use email addresses — accounts are identified only by a random 16-digit number. Accepts cash by mail and Monero. Recommended in this corpus over other VPNs because of the combination of jurisdiction (GDPR/MLAT barrier for U.S. law enforcement), payment privacy, and verified no-log policy.

**MySudo**: An app that creates multiple pseudonymous phone numbers and email addresses. Used in this corpus as the source of a VoIP number for Signal registration — registering Signal with a MySudo number separates Signal identity from carrier identity. Costs approximately $1/month for a single number. Accepts prepaid gift cards as payment.

**NSL (National Security Letter)**: A form of administrative subpoena used by the FBI without judicial approval to compel production of records from communications providers. NSLs include a gag order preventing the recipient from disclosing the request. Signal has received NSLs and disclosed only account creation date and last connection date — because it retains no other data to produce.

**obfs4/Snowflake**: Tor pluggable transports — tools that obfuscate Tor traffic to make it look like ordinary HTTPS traffic. Used when Tor is blocked at the network level (e.g., some workplace or public WiFi networks). Configured in Tor Browser under Settings > Connection > Use a bridge.

**OEM unlocking**: A setting on Android devices that allows the bootloader to be unlocked. Required before GrapheneOS installation. On carrier-locked devices, this setting is grayed out. Found at Settings > System > Developer Options > OEM unlocking (Developer Options must first be enabled by tapping Build Number 7 times).

**OpSec (Operational Security)**: Originally a military term for preventing adversaries from obtaining information about your operations. In the context of this corpus, it refers to the practices and tools that prevent surveillance systems from accumulating actionable data about you.

**Orbot**: An Android app that routes traffic through Tor. In per-app VPN mode, Orbot can route only specific apps (such as Signal) through Tor, rather than routing all device traffic. Used in this corpus for Tier 3 Signal users to prevent carrier metadata from revealing Signal connection patterns.

**Palantir**: See ELITE, ImmigrationOS, and LCA entries. Palantir Technologies is the central surveillance infrastructure contractor in this threat model, holding $970 million in federal contracts in 2025.

**Safety Numbers (Signal)**: A cryptographic fingerprint representing the combination of your and a contact's identity keys in a Signal conversation. If Safety Numbers match between both parties (verified in person or via out-of-band channel), it confirms you are communicating directly without a device interposition attack. Safety Numbers change when a contact reinstalls Signal or changes devices.

**Sandboxed Google Play**: GrapheneOS's mechanism for running Google Play Services and Play Store apps without granting them OS-level privileges. When installed in a secondary user profile, Google Play operates in complete isolation from the main profile's data and apps.

**Section 702 (FISA)**: A provision of the Foreign Intelligence Surveillance Act authorizing the NSA to collect communications of non-U.S. persons located outside the United States — but the collection occurs on U.S. internet infrastructure, meaning substantial U.S. person communications are incidentally captured. NSA can query this incidentally collected data for U.S. persons under certain conditions. Section 702 has been repeatedly reauthorized; as of April 2026, the renewal debate is ongoing.

**Signal Protocol**: The cryptographic protocol underlying Signal's end-to-end encryption. Combines Double Ratchet algorithm (providing forward secrecy and break-in recovery) and X3DH (Extended Triple Diffie-Hellman, for asynchronous key agreement). Has been formally analyzed and widely adopted, including by WhatsApp and Google Messages for their E2E modes.

**Tails**: A Linux operating system that runs entirely from a USB drive, leaves no trace on the computer it runs on, and routes all traffic through Tor by default. Appropriate for high-risk sensitive work where the host computer itself may be compromised or surveilled.

**TSCM (Technical Surveillance Countermeasures)**: Physical security practices and equipment for detecting and neutralizing surveillance devices (hidden microphones, cameras, GPS trackers on vehicles). Out of scope for this corpus but referenced in the opsec-playbook.md for Tier 3 users who face physical surveillance.

**Tor (The Onion Router)**: A network of volunteer relays that anonymizes internet traffic by routing it through three encrypted hops before it exits to the destination. The entry (Guard) node knows your IP but not your destination. The exit node knows your destination but not your IP. No single relay knows both. Tor Browser bundles the Tor client with a hardened Firefox variant configured to minimize fingerprinting.

**Venntel**: A commercial location data broker that aggregates GPS data from ordinary smartphone apps and sells it to government agencies. Venntel has confirmed contracts with ICE, CBP, and other federal agencies. The underlying data comes from apps that include advertising SDKs that collect location data. The purchase of Venntel data by law enforcement does not require a warrant under current law.

**verified boot**: A security feature that checks the cryptographic signature of the operating system at startup. If the OS has been modified (by malware, by a third party with physical access, or by an unauthorized OS installation), verified boot detects the mismatch and refuses to start. Requires a locked bootloader to function. One of the primary security properties that GrapheneOS preserves and that makes re-locking the bootloader after installation non-optional.

**VeraCrypt**: A free, open-source disk encryption tool. Creates encrypted file containers (a single file that functions as an encrypted virtual drive) or can encrypt entire partitions. The standard choice for encrypting sensitive files at rest on a laptop. Succeeded TrueCrypt (which was discontinued under unclear circumstances in 2014); VeraCrypt has been independently audited.

**VoIP number (Voice over IP)**: A phone number that operates over the internet rather than through a carrier SIM. Used in this corpus to register Signal with a number not linked to carrier identity. MySudo and JMP.chat provide VoIP numbers; Google Voice does so but links to a Google account.

**VPN (Virtual Private Network)**: A tool that encrypts your internet traffic and routes it through a server operated by the VPN provider, hiding your real IP address from websites and your traffic destination from your ISP. A VPN does not anonymize you to the VPN provider — they see your real IP. This is why provider choice, jurisdiction, and log policy matter. In this corpus, VPN is used primarily to hide Tor usage from the ISP (VPN-then-Tor configuration), not as a standalone anonymization tool.

---

*Glossary covers 40 terms. For tool-specific questions, consult the official documentation linked in the Key Sources section of each document. For legal questions, consult the National Lawyers Guild (nlg.org), EFF (eff.org), or ACLU (aclu.org).*
