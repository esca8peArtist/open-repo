---
title: "OpSec Playbook: Defensive Countermeasures Against Government Surveillance"
project: cybersecurity-hardening
created: 2026-04-26
status: complete
depends_on: threat-model.md
confidence: high — grounded in confirmed threat capabilities, current tool documentation, case law, and EFF/ACLU guidance
---

# OpSec Playbook: Defensive Countermeasures Against Government Surveillance

**Purpose**: This guide maps defensive tools and practices directly to the confirmed threat capabilities documented in `threat-model.md`. Every recommendation is grounded in a specific threat vector. This is not a general privacy guide — it is a countermeasure guide against Palantir's data-linking capability, NSA signals intelligence, FBI investigative tools, law enforcement data brokers, and the DOGE cross-agency data fusion architecture (SSA access confirmed operational as of June 2025; see Part 8 for current litigation status).

**Who this is for**:
- **Tier 1 (Baseline)** — Journalists, immigration advocates, healthcare workers who advise undocumented people, labor organizers. Elevated risk from data-broker pipelines and administrative surveillance.
- **Tier 2 (Intermediate)** — Activists, civil rights litigants, protest organizers, people with immigration status vulnerability. Risk from OSINT aggregation, IMSI catchers, social media monitoring, and Palantir ELITE targeting.
- **Tier 3 (Advanced)** — People who have reason to believe they are direct targets of investigation: individuals who have received subpoenas or legal process, sources for journalists covering national security, people facing deportation enforcement.

**How to use this guide**: Identify your tier, implement the recommendations for your tier completely before going to the next. Partial implementation often produces false confidence while leaving critical gaps.

---

## Part 1: Communications Defense

### Threat from Model
Signal metadata (who you communicate with, when, how often) is visible to your carrier and can be obtained via NSL. NSA upstream collection intercepts communications metadata from backbone infrastructure. FBI can compel connection records from Signal (they have done so via grand jury subpoena — Signal disclosed only account creation date and last connection date because that is all it retains). The IRS LCA platform explicitly maps "social networks among investigation targets" using "communications metadata: calls, texts, emails." Babel Street and ImmigrationOS include real-time social media monitoring.

### 1.1 Signal — Primary Encrypted Messenger

**What it protects against**: Content interception by carrier, ISP, NSA backbone taps, and any party without device access. Signal's end-to-end encryption using the Signal Protocol (Double Ratchet + X3DH) has survived formal cryptographic analysis. The protocol provides forward secrecy (past messages cannot be decrypted if a session key is later compromised) and break-in recovery.

**What it does not protect against**:
- Metadata: your carrier sees that you're sending data to Signal's servers. Law enforcement with an NSL can get that.
- Device compromise: if your phone is seized or infected with malware, encrypted messaging provides no protection.
- The other end: if the person you're messaging is arrested, their device may reveal the conversation.
- Social engineering: the NSA warned in February 2025 that Russian intelligence was compromising Signal accounts by tricking users into adding attacker-controlled devices via malicious QR codes disguised as group invite links. This is the primary real-world attack vector — not cryptographic.
- Delivery receipt metadata: a 2025 academic paper demonstrated that delivery receipts can reveal online/offline status patterns.

**Configuration for each tier**:

*Tier 1*:
- Enable disappearing messages (default to 1 week for all conversations, shorter for sensitive ones)
- Enable Screen Lock and Screen Security (prevents screenshots)
- Set Note to Self for sensitive notes rather than a cloud service

*Tier 2*:
- Enable usernames (Settings > Profile > tap the @ field) and set "Who can find me by my number" to Nobody (Settings > Privacy > Phone Number)
- This prevents someone who has your phone number from confirming you use Signal or contacting you that way
- Register Signal using a Google Voice or MySudo number rather than your primary carrier number — this separates your Signal identity from your carrier identity
- Verify Safety Numbers with important contacts in person or via a separate channel before sharing sensitive information
- Never scan QR codes to join Signal groups from untrusted sources (the primary 2025 attack vector)

*Tier 3*:
- Register Signal using a temporary VoIP number purchased via Tor (MySudo, JMP.chat) that is not linked to your identity
- Route Signal traffic through a VPN or Tor to prevent carrier-level metadata about Signal connection times. On Android, use Orbot in VPN mode (select Signal as an app to tunnel) — this routes Signal's network traffic through Tor at the OS level. On iOS, use a full-device VPN; Orbot on iOS does not provide equivalent per-app Tor routing.
- Use Signal on a dedicated device (see Device section) that is not associated with your primary identity
- Rotate usernames periodically

**Download**: [signal.org](https://signal.org) | [GitHub](https://github.com/signalapp/Signal-Android)

---

### 1.2 Briar — High-Anonymity Mesh Messenger (Tier 2–3)

**What it protects against**: Briar routes all communications through Tor by default, preventing metadata analysis of who is communicating with whom. Briar requires no phone number, no email address, and no central server. It can operate over Bluetooth and WiFi in addition to internet, enabling communication in network blackout scenarios.

**What it does not protect against**: Contact discovery requires in-person QR code exchange or Bluetooth proximity, which has its own physical surveillance risks. Briar is mobile-only (Android). The Tor routing adds latency.

**When to use it**: When you need to communicate with someone without a phone number link, when you need to establish a contact without any server record, or when you are in a situation where network access may be monitored or disrupted.

**Operational tradeoff**: High security, high friction. Most users find it impractical as a daily driver. Use it for specific high-sensitivity contacts.

**Download**: [briarproject.org](https://briarproject.org)

---

### 1.3 Email — Limitations First

**Threat context**: NSA PRISM compels email providers (Google, Microsoft, Yahoo) to provide stored email content for targeted individuals under Section 702. FBI can compel email content with a warrant or FISA order. Email metadata (who you email, when, subject lines) is retained by providers and accessible via NSL without a warrant.

**What ProtonMail/Tutanota protect against**: Email content at rest on the provider's servers. Proton and Tutanota use zero-knowledge encryption — they cannot decrypt your emails even if subpoenaed. Proton is incorporated in Switzerland and subject to Swiss law (though they have complied with Swiss court orders for IP addresses when legally compelled, as they did in a 2021 climate activist case).

**What they do not protect against**:
- Email metadata. The sender, recipient, timestamp, and subject line are almost always visible to the provider and can be legally compelled. Subject lines are sometimes encrypted (Proton does this for Proton-to-Proton messages) but the metadata around the email is not.
- The other end. If you email a Gmail address, Google receives the plaintext. End-to-end encryption only works Proton-to-Proton or when both parties use PGP keys.
- Account linkage. If you register your Proton account with your real identity or access it from your real IP, you've defeated the purpose.

**Configuration**:
- *Tier 1*: Use Proton Mail ([proton.me](https://proton.me)) for sensitive communications. Communicate with other Proton users where possible.
- *Tier 2*: Create your Proton account over Tor. Use a username unconnected to your identity. Access via Tor Browser or Proton's .onion address.
- *Tier 3*: For truly sensitive communications, email is the wrong tool. Use Signal, Briar, or in-person communication.

---

### 1.4 XMPP + OMEMO — Federated Encrypted Chat

**Context**: XMPP is a federated, open protocol. OMEMO is an E2E encryption extension based on the Signal Protocol's Double Ratchet. Unlike Signal, XMPP can be self-hosted, removing reliance on a single company.

**Limitations**: XMPP inherently leaks metadata — XMPP servers see who is communicating with whom, even if not the content. A 2024 technical analysis argued that XMPP metadata leaks are severe enough that XMPP should generally not be trusted for private communication. OMEMO implementation quality varies significantly across clients. Most implementations remain on OMEMO spec version 0.3.0 with known limitations.

**Verdict**: For this threat model, XMPP+OMEMO is not recommended as a primary tool. Signal or Briar are superior on every relevant dimension. XMPP is appropriate if you need to self-host your communications infrastructure and are technically capable of doing so securely.

---

## Part 2: Metadata Minimization

### Threat from Model
Palantir ELITE generates an "address confidence score" by correlating location data across Medicaid records, DMV records, USCIS records, ALPR data, and commercial broker data. Venntel collects location data from ad SDKs in smartphone apps and sells it to ICE. The IRS LCA platform uses IP address records. ICE explicitly filed a market research request in January 2026 seeking ad-tech data. Your phone is continuously broadcasting your location to data brokers through app SDKs.

### 2.1 Your Phone Is a Location Tracking Device — Threat is Structural

Every commercial Android or iPhone running apps with advertising SDKs is generating location records that are being harvested and sold to law enforcement without a warrant. This is not theoretical — the DHS Inspector General confirmed CBP, ICE, and the Secret Service all purchased location data from brokers, and ICE is actively seeking to expand this capability. This is the most underappreciated threat in the current landscape.

**The technical mechanism**: Apps install advertising SDKs (from Google, Facebook, dozens of smaller brokers) that log GPS location and transmit it to data brokers. The location is associated with a Mobile Advertising Identifier (MAID). Brokers aggregate millions of these location streams and sell the resulting database. Law enforcement queries by location (e.g., "who was at this protest?") or by individual identifier. No warrant required.

**Counter-measure hierarchy** (in order of effectiveness):

1. **Leave your phone at home** when attending protests, sensitive meetings, or any location you do not want in government databases. A phone in a Faraday bag still has its last-known location recorded. A phone left at home creates a verifiable record that you were not at a location. This is not paranoia — it is the single most effective location privacy measure available.

2. **Faraday bag** (when leaving phone at home is not feasible): Mission Darkness and GoDark make certified signal-blocking bags (~$50-80). Test by calling the phone after placing it in the bag — if it rings, the bag is inadequate. A Faraday bag blocks all radio signals: cell, WiFi, Bluetooth, GPS. However: the last location your phone recorded before going into the bag is already in the data broker's database. The bag only stops future tracking.

3. **GrapheneOS with network permission controls** (see Device section): GrapheneOS includes per-app network access controls that prevent apps from communicating even if they have other permissions. Combined with disabling advertising IDs, this substantially reduces ad-SDK location harvesting.

4. **Disable advertising ID**: On iOS: Settings > Privacy & Security > Tracking > disable. On Android: Settings > Privacy > Ads > Delete advertising ID. This does not eliminate tracking but severs the durable link between sessions.

5. **Never install unnecessary apps**: Every additional app is an additional data channel. A phone with 5 apps leaks orders of magnitude less data than one with 50.

---

### 2.2 Phone Number Compartmentalization

**Threat context**: Your phone number is a durable identifier that connects carrier records (location, call metadata), Signal account, Google/Apple account, and any service you've given it to. Palantir ICM stores phone records. NSA can query by phone number across collected metadata.

**Options by tier**:

*Tier 1*: Enable Signal usernames; set phone number visibility to Nobody as described in 1.1.

*Tier 2*: Use MySudo ([getsudo.com](https://getsudo.com)) or Google Voice for a secondary number that forwards calls. Use this number for any service that doesn't need your real number. MySudo supports multiple separate phone identities on one device.

*Tier 3*: Prepaid SIM card purchased with cash at a physical retailer, activated without providing real identity. Important caveats: (a) in the U.S. there is currently no federal law requiring ID to purchase a prepaid SIM, but retailer policies vary; (b) the SIM must be activated without connecting it to your real device (use a factory-reset dedicated phone); (c) the SIM must not be used in proximity to your real phone — cell towers can correlate two devices that are always co-located; (d) the SIM provides no location privacy in itself — it still connects to cell towers and generates carrier records. The goal of a burner SIM is identity separation, not location anonymity.

---

### 2.3 Breaking Pattern-of-Life Analysis

**Threat context**: Palantir Gotham's pattern-of-life analysis maps where a person is, has been, and is likely to go. ELITE's address confidence score is explicitly a prediction of current location based on historical data. Analysts look for stable anchors (home, workplace, recurring locations) and can distinguish between genuine randomization and staged countermeasures.

**What effective pattern disruption looks like**:

1. **Vary routes and timing**: Don't leave home at the same time every day. Change transit routes weekly. This is low-cost and degrades location prediction accuracy significantly.

2. **Physical location separation for sensitive activity**: Don't conduct sensitive communications from your home or workplace. A coffee shop you visit rarely, paid in cash, provides a significantly different location anchor than your home.

3. **Keep your sensitive-activity phone off when traveling to and from sensitive locations**: Turn it on only at the destination, conduct the activity, turn it off before leaving. The carrier sees the phone appear and disappear at a location; it does not record the travel pattern to and from that location.

4. **Don't let personal and activist identities share physical locations**: If your activist phone and your personal phone are ever in the same place, cell tower records can correlate them. This is how parallel identity construction fails.

5. **Vehicle OpSec**: Modern vehicles with connected features (OnStar, Ford Sync, any telematics system) transmit location data that can be subpoenaed from the manufacturer. For sensitive travel, use a vehicle without telematics features or a rental paid cash. Turn your phone off — not just silenced — before getting in the vehicle.

---

## Part 3: Network Anonymization

### Threat from Model
NSA upstream collection intercepts internet backbone traffic. ISPs can see that you're using Tor (but not what you're doing on Tor). NSA can see Tor exit node traffic (the traffic leaving the Tor network) but cannot trace it back to the user without a traffic correlation attack. VPN providers can be subpoenaed, and U.S.-based VPN providers are subject to National Security Letters.

### 3.1 Tor Browser — Realistic Threat Model

**What Tor protects against**: Your ISP cannot see what websites you visit. The destination website cannot see your IP address. Local network surveillance (coffee shop, office, IMSI catcher) cannot see your browsing. Even Tor exit nodes see only the traffic, not who initiated it.

**What Tor does not protect against**:
- Traffic correlation by a global passive adversary (the NSA): If an adversary can observe both your entry traffic (your connection to the Tor guard node) and the exit traffic (the traffic leaving the Tor network), they can correlate timing and volume patterns to link your identity to your destination. This attack is theoretically feasible for the NSA given its backbone surveillance capability. It is computationally expensive and requires active operation against a specific target — it is not a bulk surveillance technique.
- Your ISP (or carrier) can see that you use Tor. In some threat models, using Tor is itself a red flag. Use Tor bridges (obfs4, Snowflake) to obfuscate Tor usage from your ISP if this is a concern.
- Browser fingerprinting: Tor Browser hardens against this, but custom configurations (adding extensions, changing window size) weaken the anonymity set. Use Tor Browser as downloaded, without modifications.
- Exit node attacks: Unencrypted traffic leaving a Tor exit node can be read by the exit node operator. Always use HTTPS (Tor Browser enforces this where available). Do not submit credentials or personal information over Tor to sites without HTTPS.
- Device-level deanonymization: JavaScript exploits, malicious PDFs, and application-level leaks can reveal your real IP. Tor Browser's security slider (Security Settings > Safest) disables JavaScript and mitigates this.

**When to use Tor**:
- Researching sensitive topics without creating a browser history tied to your IP
- Accessing .onion services (SecureDrop, Briar, Proton's onion address)
- Creating accounts that should not be linked to your real identity

**When Tor is not sufficient**: For truly high-stakes activity against a targeted adversary with NSA-level capabilities, Tor alone is not sufficient. Tor + additional physical security (dedicated device, air-gapped communications) is the appropriate measure.

**Tor Browser**: [torproject.org](https://www.torproject.org) — download only from this official source.

---

### 3.2 VPN — The Reality

**The fundamental limitation**: A VPN shifts trust from your ISP to the VPN provider. Your ISP can no longer see your traffic — but your VPN provider sees all of it. A U.S.-based VPN provider is subject to NSLs, FISA orders, and court orders. A foreign VPN provider may be beyond U.S. jurisdiction, but:
- The U.S. CLOUD Act allows the U.S. to compel data from U.S.-based companies regardless of where the data is stored
- If the VPN provider has any U.S. business presence, it is subject to U.S. legal process
- VPN providers have been known to comply with legal process despite no-log claims

**What "no-log" actually means**: A genuine no-log VPN provider cannot provide traffic logs because it does not retain them. This has been tested in practice — when Turkish authorities seized an ExpressVPN server in a 2017 murder investigation, they found no logs. NordVPN has stated it has never provided customer data to law enforcement. These track records are meaningful but not guarantees.

**VPNs that have demonstrated court-verified no-log policies** (as of 2025): Mullvad (accepts cash and Monero, no email required to sign up), ProtonVPN (Swiss jurisdiction, audited), IVPN (Gibraltar jurisdiction, audited). [Detailed analysis: vpnsuggest.com/court-proven-vpn-no-log-policies-legal-cases](https://vpnsuggest.com/court-proven-vpn-no-log-policies-legal-cases/)

**What VPNs protect against in this threat model**:
- Prevents ISP from selling your browsing data to data brokers (a real commercial surveillance threat)
- Hides your IP address from websites you visit
- Protects against local network surveillance
- Hides Tor usage from your ISP (if you route Tor through a VPN — "VPN then Tor")

**What VPNs do not protect against**:
- A targeted investigation with legal process against the VPN provider
- NSA backbone surveillance (VPN traffic is encrypted but still visible as a flow to the VPN server)
- Any identifying behavior inside the VPN (logging into your real accounts, for instance)

**Jurisdiction matters**: Mullvad (Sweden), ProtonVPN (Switzerland), and IVPN (Gibraltar) are outside U.S. jurisdiction for routine legal process. A U.S. court order must go through Mutual Legal Assistance Treaty process to reach them — a significant procedural barrier. This matters for Tier 2 and 3 users.

*Tier 1 recommendation*: ProtonVPN free tier provides meaningful protection against commercial surveillance.
*Tier 2–3 recommendation*: Mullvad VPN ($5/month, accepts cash). Pay with cash or Monero. Do not create an account with identifying information.

---

### 3.3 Tor + VPN Stacking

Two configurations exist:

**VPN then Tor (VPN → Tor)**: Connect to VPN, then use Tor Browser through the VPN. This hides your Tor usage from your ISP (your ISP sees VPN traffic, not Tor). The VPN provider knows you use Tor but cannot see your Tor destination. Appropriate when your ISP monitoring is a concern and you want to prevent being flagged as a Tor user.

**Tor then VPN (Tor → VPN)**: Route your VPN through Tor. The VPN provider cannot see your real IP. This is technically complex and rarely necessary for the threat model described here. Not recommended for most users.

**Recommendation**: VPN then Tor (Tier 2+) is appropriate when ISP-level Tor flagging is a concern.

---

## Part 4: Device and OS Hardening

### Threat from Model
DOGE has demonstrated willingness to transfer government data to unauthorized servers. FBI and ICE conduct device seizures. Forensic tools (Cellebrite UFED, GrayKey) can extract data from unencrypted or post-seizure devices. Clearview AI's contract with ICE includes biometric matching. The threat at device level is primarily physical seizure and forensic extraction, not remote compromise for most users.

**Mobile biometric identification in field encounters**: ICE's Mobile Fortify application enables agents to conduct biometric identification outside formal processing encounters. The handheld app allows agents in the field to photograph an individual and run contactless fingerprint and facial recognition scans from their smartphones against DHS biometric databases in real time. The app has been used over 100,000 times since launch. This capability extends biometric identification risk from fixed checkpoints (border crossings, detention facilities) to any location where an ICE agent is present — traffic stops, street corners, protests. Countermeasures must account for this mobile, ad hoc deployment context, in addition to device seizure and forensic extraction risks.

### 4.1 Mobile OS Comparison

**GrapheneOS** (Android-based, Pixel devices only)
- Adds hardened memory allocator, exploit mitigations, sandboxed Google Play (Google Services run in an isolated sandbox with reduced permissions)
- Per-app network access controls prevent apps from phoning home even with internet permission
- Longer key derivation delays forensic brute-force of PIN
- Apple is subject to U.S. law enforcement requests; GrapheneOS removes the manufacturer as a data source entirely
- iOS 18 has a 72-hour **inactivity** reboot feature (introduced in iOS 18.0, timer shortened from 168 hours to 72 hours in iOS 18.1): if an iPhone is not unlocked for 72 hours it reboots into Before First Unlock (BFU) state, complicating forensics — this is a meaningful security improvement
  - GrapheneOS has its own auto-reboot feature (default: **18 hours** of inactivity, configurable from 10 minutes to 72 hours), which is more aggressive than Apple's 72-hour default and is an additional advantage of GrapheneOS
- The GrapheneOS project withdrew its server infrastructure from France in November 2025 after French police labeled it a "criminal tool" in media (Le Parisien, Nov. 19, 2025) and a French cybercrime prosecutor publicly threatened legal action if the project refused law enforcement cooperation — indicating governments view it as a real operational threat
- **Verdict**: For a threat model centered on law enforcement forensics and data broker prevention, GrapheneOS is the strongest choice. Requires a Google Pixel device.
- **Download/install**: [grapheneos.org](https://grapheneos.org)

**iOS (iPhone)**
- Cellebrite UFED is blocked on iOS 17.4+. GrayKey achieves only partial access on iOS 18 devices as of 2025. This is a meaningful forensics barrier.
- Apple complies with U.S. law enforcement requests. Apple's iCloud backups contain message content that can be subpoenaed. If iCloud backup is enabled, Apple holds a copy of much of your data.
- iCloud backup undermines device encryption for most users — law enforcement subpoenas Apple for iCloud data, not the physical device.
- Configuration: disable iCloud backup for sensitive apps (Settings > [account] > iCloud > toggle off Messages, Photos, etc.) or disable iCloud backup entirely and back up locally (encrypted iTunes/Finder backup).
- **Verdict**: Better than stock Android against forensic tools. Weaker than GrapheneOS against data retention/legal compulsion. Acceptable for Tier 1; sufficient for Tier 2 with iCloud backup disabled; insufficient for Tier 3 where manufacturer risk is a concern.

**Stock Android (Samsung, Pixel with stock OS, etc.)**
- Shares carrier telemetry with manufacturer. Google Services track location. Android forensics tools have broader capability than iOS tools.
- Not appropriate for Tier 2+ in this threat model.

**Windows on Mobile**: Not relevant to mobile.

---

### 4.2 Desktop OS

**Tails OS** (amnesic live OS, boots from USB)
- Runs entirely in RAM. Leaves no trace on the host computer. All traffic routed through Tor.
- Designed for the "borrowing a computer" scenario — use a library computer or any computer without leaving forensic evidence.
- Does not have persistent storage by default (this can be configured but reduces the amnesia model).
- **Use case**: One-time sensitive tasks, accessing Tor from an untrusted device, creating anonymous accounts.
- **Download**: [tails.net](https://tails.net)

**Qubes OS** (hypervisor-based compartmentalization)
- Runs each activity in a separate virtual machine ("qube"). A compromised browser qube cannot access files in a work qube. A malicious PDF opened in an isolated qube cannot spread to the rest of the system.
- Edward Snowden's recommendation for desktop security.
- Hardware requirements: 16–32GB RAM, CPU with virtualization support. Not suitable for older or budget hardware.
- Learning curve is significant. Routine tasks require understanding which qube to use.
- **Use case**: High-value targets who routinely handle potentially hostile documents or need strict compartmentalization between identities.
- **Download**: [qubes-os.org](https://www.qubes-os.org)

**Fedora / Ubuntu with full-disk encryption**
- Reasonable baseline for Tier 1–2 that doesn't require Qubes-level complexity.
- Configure LUKS full-disk encryption at installation.
- Tier 2 addition: use separate user accounts or separate Linux installations for separate identities.

**Windows**
- Windows telemetry sends usage data to Microsoft by default. This data can be subpoenaed.
- BitLocker encryption is available but requires a Microsoft account to store the recovery key by default — storing your recovery key in Microsoft's cloud defeats the purpose of local encryption.
- BitLocker uses TPM-based key storage that does not protect against a sophisticated forensics attack on a powered-off device in some configurations.
- **Verdict**: Windows is not appropriate for Tier 2+ in this threat model. It can be used for Tier 1 non-sensitive activity.

---

### 4.3 Full Disk Encryption

**What it protects against**: Physical seizure of a powered-off device. If your laptop is seized while powered off and encrypted, forensic tools cannot extract your data without your passphrase (or a significant flaw in the encryption implementation).

**What it does not protect against**:
- Evil Maid attacks: If your device is accessed without your knowledge (e.g., seized and returned, or hotel room entry), an attacker can install a bootkit that captures your passphrase on next entry. BIOS/UEFI secure boot with verified boot chain (Qubes supports this via Anti-Evil-Maid) partially mitigates this.
- Cold-boot attacks: DRAM retains data for seconds to minutes after power loss. An attacker with physical access to a running device can freeze the RAM and extract it. Mitigation: power off devices fully when not in use; enable memory encryption if your CPU supports it (AMD SEV, Intel TME).
- Device seizure while powered on: A device in use can be forensically accessed before encryption engages.
- Legal compulsion: In the U.S., courts are split on whether providing an encryption passphrase is testimonial under the Fifth Amendment (see Part 8).

**Configuration**:
- Linux: LUKS2 with Argon2id key derivation (more resistant to brute force than LUKS1/PBKDF2). Set a passphrase of 6+ random words (diceware method).
- macOS: FileVault 2 (enabled by default in recent versions). Store recovery key locally, not with Apple.
- Windows: BitLocker without TPM-only mode; set a strong PIN or passphrase in addition to TPM.
- Mobile: Both GrapheneOS and iOS use hardware-backed encryption tied to your PIN. Use a 6+ digit PIN (not biometrics as the primary unlock — police can compel fingerprint/face unlock in many jurisdictions, but not a PIN/passphrase).

---

### 4.4 USB and Physical Security

- **USB attacks**: Malicious USB devices can compromise a system on connection. Don't plug in unknown USB devices. Qubes OS mitigates USB attacks by running USB controllers in an isolated qube.
- **Physical access is game over**: If an adversary has physical, unobserved access to your device, assume it is compromised. No software countermeasure survives sustained physical access by a well-resourced adversary.
- **BIOS/Firmware**: Enable UEFI Secure Boot. Set a BIOS password to prevent booting from USB without authorization. Check BIOS integrity if you have reason to believe your device was accessed without your knowledge.

---

## Part 5: Identity Compartmentalization

### Threat from Model
This is the core Palantir capability: identity resolution across disparate records. Confirmed capability: Palantir Gotham can search by tattoo, physical description, partial address, vehicle, associate's name, or immigration number to link records to an individual. The IRS LCA platform maps social networks — if your activist identity uses the same financial account as your personal identity, the IRS has the link. DOGE's cross-agency data fusion program has moved from construction to partial operation: the Supreme Court ruled in June 2025 that DOGE personnel could access SSA records (Social Security numbers, address history, benefit payment history, employer records), and the Fourth Circuit vacated an injunction against that access in April 2026. A DOGE employee has been confirmed to have shared SSA data with a political advocacy group, and SSA's own court filings acknowledged data was transferred to a non-SSA server the agency can no longer access. The "master database" is not a single central repository — it is a distributed query architecture across Palantir Foundry instances at multiple agencies that are interoperable via a common API. This makes it significantly harder to block through a single legal challenge. The practical scope of accessible data now confirmed to include: SSA records (SSN, address, employer, benefit history), IRS data (tax returns, financial social graph via LCA platform), DHS/ICE records (immigration status, biometric identifiers, travel history), and Medicaid/HHS enrollment data.

**The principle**: Separate identities cannot share any persistent link. One shared data point — a phone number that appeared on both registration forms, a payment card used for both purposes, a device that was logged into both accounts, a GPS location record placing both phones at the same address — defeats the compartmentalization.

### 5.1 Identity Architecture

**Define your identities explicitly** before establishing them. A common structure:
- **Real identity**: Government ID, employer, bank accounts, healthcare, all legal obligations. Not linked to activist activity.
- **Activist/organizing identity**: Used for organizing communications, Signal contacts for sensitive work, any email accounts for activism, any social media used for organizing.
- **Public-facing identity** (if applicable): For public writing, journalism, or any public-facing role that may be separated from your real identity.

**The rules of separation** (each must be absolute for compartmentalization to work):
1. Separate devices per identity (or separate OS installations that never share the same boot session)
2. Separate email providers per identity
3. Separate payment methods per identity (no shared cards, no shared bank accounts)
4. Never access one identity's accounts from another identity's device
5. Never use one identity's phone number to register another identity's accounts
6. Never let both phones be powered on at the same physical location (cell tower correlation)

---

### 5.2 Payment Compartmentalization

**Threat context**: The IRS LCA platform ingests bank statements and financial transactions. Palantir's data integration connects financial records to identity. Shared payment methods across identities are the most common failure mode.

**Options**:
- *Tier 1*: Use a separate debit card for activist purchases (a prepaid card bought with cash and loaded with cash).
- *Tier 2*: Prepaid Visa/Mastercard gift cards purchased with cash for one-time sensitive purchases. Use these for VPN subscriptions, cloud storage, any service used by your secondary identity.
- *Tier 3*: Monero (XMR) cryptocurrency for digital payments that require real anonymity. Unlike Bitcoin (where the IRS LCA platform has confirmed cryptocurrency wallet analysis capability), Monero uses ring signatures and stealth addresses to make transaction tracing computationally infeasible. Acquiring Monero without a KYC exchange is necessary for the privacy model to hold. LocalMonero (the primary P2P XMR exchange) permanently shut down in May 2024. Current no-KYC options: **Haveno** (Tor-native decentralized exchange built specifically as a LocalMonero successor, running atomic swaps), **Bisq** (Bitcoin-focused DEX with XMR/BTC markets, no KYC), or cash purchases at Bitcoin ATMs followed by atomic swap conversion to Monero via a non-custodial tool (Cake Wallet supports this). Avoid centralized exchanges — Binance, Coinbase, and Kraken have all delisted or restricted XMR in major markets.

---

## Part 6: Data at Rest Protection

### Threat from Model
FBI and ICE conduct device seizures in connection with arrests and searches. The threat is forensic extraction after seizure — not remote compromise. VeraCrypt hidden volumes provide a legal defense layer (contested); plain full-disk encryption provides forensic protection for powered-off devices.

### 6.1 VeraCrypt and Hidden Volumes

**What it provides**: VeraCrypt encrypts files, containers, and entire volumes. The hidden volume feature allows two passphrases: one that reveals a decoy volume with innocuous content, one that reveals the real volume. This is the technical implementation of "plausible deniability."

**Legal reality of plausible deniability**: Courts in the U.S. are split on whether compelling decryption violates the Fifth Amendment. The act of producing a decrypted drive may be "testimonial" (implying that you know the passphrase and that the decrypted data exists) — several circuits have held this. However, if law enforcement already knows encrypted data exists (e.g., they can see the encrypted partition), they may succeed in compelling decryption by arguing the "foregone conclusion" doctrine. VeraCrypt's hidden volume provides a technical but not guaranteed legal defense.

**What it definitively protects against**: Unauthorized forensic extraction of an encrypted container by any party who does not have the passphrase and against whom you are not legally compelled to decrypt.

**Practical use**: Use VeraCrypt encrypted containers for sensitive files on a computer where full-disk encryption is already in place. Think of it as a second layer for files that are specifically sensitive.

**Download**: [veracrypt.fr](https://www.veracrypt.fr)

---

### 6.2 Password Management

**KeePassXC** (local, no cloud):
- Stores passwords in an encrypted local database (`.kdbx` file). Never transmits passwords over the network.
- The database itself is portable — can be copied to an encrypted USB drive.
- Requires you to handle your own backup (which is both a feature and a risk).
- Audited by the EU-FOSSA project with no security issues found.
- Best for Tier 2–3 users who do not want any cloud dependency.
- **Download**: [keepassxc.org](https://keepassxc.org)

**Bitwarden** (cloud-synced, open source, self-hostable):
- Zero-knowledge architecture: Bitwarden cannot decrypt your vault even if subpoenaed.
- Can be self-hosted via Vaultwarden (unofficial Bitwarden-compatible server) to eliminate third-party cloud dependency entirely.
- More convenient for cross-device access.
- Supports YubiKey as a second factor.
- Audited by third-party security firms.
- **Download/self-host**: [bitwarden.com](https://bitwarden.com) | [github.com/dani-garcia/vaultwarden](https://github.com/dani-garcia/vaultwarden)

**Recommendation**: KeePassXC for Tier 2–3 (no cloud exposure). Bitwarden self-hosted for those who need cross-device sync without cloud dependency. Never use browser-built-in password managers for sensitive credentials — they sync to the browser vendor's cloud.

---

### 6.3 Hardware Security Keys

YubiKey hardware security tokens (two-factor authentication that requires physical possession of the hardware key) provide protection against phishing and remote account takeover. A stolen password is not sufficient to log in — the attacker must also have the physical key.

**Relevant because**: Account takeover (getting into your email, Signal backup, cloud storage) is a documented law enforcement technique that does not require a warrant if the adversary can obtain your password through other means. A hardware key closes this attack surface.

**Purchase**: [yubico.com](https://www.yubico.com) — buy directly from Yubico, not third-party resellers, to ensure supply chain integrity.

---

## Part 7: Behavioral OpSec

### Threat from Model
ImmigrationOS includes automated OSINT and social media monitoring. Babel Street performs real-time social media monitoring with sentiment analysis. Palantir Gotham maps "family relationships" and "all known associates." The FBI's use of parallel construction means that even if digital surveillance is legally constrained, operational leads can come from monitoring and be rebuilt through conventional means.

### 7.1 Device Discipline

- **One device, one identity**. Never log into an account associated with one identity from a device associated with another.
- **Separate browser profiles are not identity separation**. Different browser profiles on the same device can be correlated by browser fingerprint, IP address, timing patterns, and any browser vulnerabilities. Identity separation requires separate devices.
- **Disable biometric unlock for sensitive devices**. In most U.S. jurisdictions, law enforcement can compel biometric unlock (fingerprint, face) but not a passphrase/PIN. The Fifth Amendment protection for PINs is more robust than for biometrics. Use a PIN of 6+ digits.
- **Disappearing messages by default**. If a message doesn't need to be permanent, it shouldn't be. Configure Signal to delete messages after 1 week by default.

---

### 7.2 Meeting Security

- **Phone away from the meeting** (or off). A phone in the room is a recording device and a location ping, even if you trust everyone present. If the meeting must remain off the record, phones go in a separate room or in Faraday bags.
- **Assume any room can be bugged**. This is not paranoia for high-risk individuals — FBI consensual monitoring (a participant in the meeting wears a recording device) is a routine investigative tool that requires no warrant. If you would not say something in front of a recorder, assume it should be discussed in an environment where you have verified the people present.
- **Sensitive conversations in physically private spaces**. Not in a restaurant, not on the phone, not via text. In person, in a verified space, with trusted people.

---

### 7.3 Communication Discipline

- **Signal group chat security**: Every person added to a group is a potential weak link. A single arrested or compromised group member can reveal the group's membership and content (if disappearing messages are off). Keep sensitive groups small. Do not add people you have not verified in person.
- **Forward secrecy is real but not magic**: Signal's Double Ratchet means that compromising one message doesn't compromise all previous ones — but it does compromise all future ones until the session is re-keyed. If you believe your device or a contact's device is compromised, close the conversation and start a new one.
- **Don't discuss sensitive topics over platforms you don't control**: Not Slack, not WhatsApp, not Google Meet, not Discord. These platforms' operators can be subpoenaed and comply routinely. ImmigrationOS's social media monitoring capability confirms that public and semi-public social media is actively monitored.
- **Assume public social media is read by law enforcement**. This is confirmed — ImmigrationOS includes real-time social media monitoring. Babel Street has confirmed government contracts for OSINT aggregation. Treat public social media as a broadcast to investigators.

---

### 7.4 Financial Discipline

- Maintain strict separation between identities at the financial level. A shared debit card is a data point in the IRS LCA platform. A shared bank account is a graph edge in Palantir's social network analysis.
- Do not use Venmo, Cash App, or Zelle for sensitive transactions — these services are subpoena-able and maintain transaction records. Cash or Monero for anything sensitive.

---

## Part 8: When Technical Measures Are Not Enough — Legal Layers

### Threat from Model
The IRS LCA platform performs "massive-scale" data mining with court-confirmed legal authority. DOGE's cross-agency data fusion architecture is no longer merely "contested" — SSA data access is operationally confirmed following the June 2025 Supreme Court ruling and the April 2026 Fourth Circuit decision removing injunctive limits; the litigation continues on underlying merits but no current injunction blocks DOGE access. [Quarterly review gate: July 2026 — update to reflect litigation merits resolution if any court has issued a final ruling on DOGE data access authority.] FBI NSLs require no judicial approval. Section 702 is reauthorizing. The legal framework for U.S. government surveillance is expansive and the remedies are slow.

### 8.1 Understanding What Law Enforcement Can Compel

**From your devices directly** (if you are arrested or your device is seized):
- A PIN or passphrase: Fifth Amendment protection is contested. Courts are split. Do not rely on this as your primary defense — encrypt everything and assume you may be ordered to decrypt.
- Biometrics (fingerprint/face): Generally compellable by court order. Use a PIN.

**From service providers via legal process**:
- Signal: only account creation date and last connection time. (Confirmed via grand jury subpoena response.)
- Proton Mail: IP address when legally compelled in Swiss proceedings. Email metadata.
- Google/Apple: Extensive. Email content, backups, location history, connected device logs.
- VPN providers with genuine no-log policies: little to nothing.

**Via data broker purchase (no warrant required)**:
- Commercial location data via ad-tech SDKs
- Public records (address history, associates, relatives)
- Vehicle location via ALPR networks
- Social media posts (public)

### 8.2 Jurisdiction Strategy for Data

**The CLOUD Act complication**: Even data stored on European servers is potentially accessible to U.S. law enforcement if the company is U.S.-based. AWS, Google Cloud, and Microsoft Azure are U.S. companies — storing data on their European servers does not defeat U.S. legal process.

**What provides genuine jurisdictional protection**:
- Data on servers operated by companies with no U.S. business presence and incorporated in jurisdictions with strong data protection laws (Iceland, Switzerland, Germany, Netherlands).
- Services: Proton (Switzerland), Mullvad (Sweden), Disroot (Netherlands), Systemli (Germany).
- GDPR Article 48 prohibits EU-based companies from complying directly with U.S. CLOUD Act requests — they are supposed to require an MLAT (Mutual Legal Assistance Treaty) process. This creates significant procedural friction for U.S. law enforcement.
- **Practical implication**: Using a non-U.S. service for sensitive data (email, file storage) raises the legal bar for U.S. government access from "NSL" to "international treaty process." This is meaningful friction, not a guarantee.

### 8.3 The Fifth Amendment Reality

Do not rely on Fifth Amendment protection against compelled decryption as a primary defense. The legal landscape is:
- Circuits are split: some require a warrant, some allow compelled decryption under the "foregone conclusion" doctrine.
- VeraCrypt hidden volumes provide a technical but not legally certain defense.
- The strongest defense against compelled decryption is designing systems so that no single device contains all sensitive information. Distributing sensitive information across encrypted containers on separate devices, with separate passphrases, complicates the "foregone conclusion" analysis.

**Engage a lawyer before a crisis**: Organizations that provide legal support include the National Lawyers Guild ([nlg.org](https://www.nlg.org)), Electronic Frontier Foundation ([eff.org](https://www.eff.org)), and the ACLU. Know who to call before you need to call them.

---

## Part 9: Organizational OpSec

### Threat from Model
ImmigrationOS includes automated OSINT and real-time social media monitoring that can identify organizational networks. Palantir ICM stores "family relationships" and social connections. NSA contact chaining extends two to three hops from a single target — a person arrested or surveilled can expose their entire network.

### 9.1 Organizational Communications

- **Use Signal for all internal sensitive communications**. Not WhatsApp (Facebook-owned, metadata retained), not Slack (corporate, subject to enterprise legal holds), not Discord (U.S.-based, has complied with law enforcement requests), not email.
- **Use separate Signal accounts for organizational vs. personal communications** where possible. This limits the damage if one account is compromised.
- **Enable Signal's Note to Self** for sensitive notes that should not exist on a cloud service.
- **SecureDrop for document receipt from sources**: [securedrop.org](https://securedrop.org). For organizations that receive sensitive documents from whistleblowers or sources, SecureDrop provides Tor-based anonymous submission. Maintained by Freedom of the Press Foundation.
- **OnionShare for ad-hoc file sharing**: [onionshare.org](https://onionshare.org). Creates a temporary .onion address for file transfer. Eliminates the need to use email or cloud storage for sensitive file exchange. Used by the Movement for Black Lives.

### 9.2 Compartmentalization Within Organizations

- **Need-to-know discipline**: Not everyone in an organization needs to know about every operation. Compartmentalization limits the damage any single arrested or surveilled member can cause.
- **Role separation**: People who manage public-facing communications should not have access to operational details. People who conduct logistics should not have access to the full contact list.
- **Separate Signal groups by sensitivity level**: One group for general coordination (assume anyone arrested could reveal membership), a separate, smaller group for operational planning (higher trust threshold for membership).

### 9.3 Incident Response

**If a member is arrested or their device is seized**:
1. Assume any communications on that device are now accessible to law enforcement.
2. Immediately rotate Signal Safety Numbers with that contact (or remove them from sensitive groups).
3. Assess what information they had access to. Notify others if their operational security may be compromised.
4. Do not discuss the situation on any digital channel — in person only.
5. Activate legal support immediately (NLG, ACLU, or pre-arranged legal contact).

**If you receive legal process (subpoena, NSL, court order)**:
1. Contact a lawyer immediately. Do not comply without legal advice.
2. Do not destroy or alter evidence — this creates obstruction charges.
3. Inform your organization's legal support in a way that does not violate any gag order attached to the process.

---

## Part 10: Monitoring and Threat Intelligence

### 10.1 How to Know If You Are Surveilled

**Indicators of active investigation**:
- Unexpected contact from law enforcement agents about your associations
- Friends or family members contacted by law enforcement asking about you
- Unusual vehicles consistently parked near your home or workplace
- Subpoenas or NSLs served to services you use (you may not learn of NSLs directly due to gag orders)
- Social media monitoring: you receive responses to posts within minutes that suggest automated monitoring
- "Knock and talks" — law enforcement visits to your home or workplace without a warrant

**Note**: Many of these indicators are also present in routine law enforcement activity unrelated to surveillance. The presence of multiple indicators is more significant than any single one.

---

### 10.2 Threat Intelligence Sources

Track these sources for early warning about new surveillance capabilities, new contracts, and new legal developments:

- **EFF Deeplinks**: [eff.org/deeplinks](https://www.eff.org/deeplinks) — Primary source for digital rights legal analysis and new surveillance tool reporting.
- **404 Media**: [404media.co](https://www.404media.co) — Investigative reporting on surveillance technology; broke the ELITE user guide story.
- **The Intercept**: [theintercept.com](https://theintercept.com) — Long-form investigative reporting on surveillance and national security; broke the Palantir IRS story.
- **Surveillance Self-Defense (EFF)**: [ssd.eff.org](https://ssd.eff.org) — Regularly updated practical guidance; had major updates in 2025.
- **Privacy Guides**: [privacyguides.org](https://www.privacyguides.org) — Maintained community recommendations for privacy tools; updated more frequently than EFF SSD.
- **Techdirt**: [techdirt.com](https://www.techdirt.com) — Legal and policy analysis on surveillance law.

**Quarterly reassessment**: The threat model in this guide was current as of April 2026. Surveillance capabilities expand; tool vulnerabilities are discovered; legal frameworks shift. Reassess your threat model and tooling every quarter:
1. Has any new Palantir contract expanded the data-linking capability?
2. Has any new legal decision changed the Fifth Amendment landscape?
3. Have any tools you rely on been compromised or acquired by a potentially adverse party?
4. Has your personal threat level changed?

---

## Part 11: IMSI Catcher Detection

### Threat from Model
ICE, FBI, DEA, NSA, Secret Service, U.S. Marshals, and military all operate cell-site simulators. ICE and DHS have deployed them without following their own rules. Plane-mounted stingrays have been used over cities by FBI and U.S. Marshals. DHS removed its facial recognition oversight policy in February 2026 with no replacement.

### Rayhunter — Open Source Stingray Detection

The EFF released Rayhunter in March 2025, updated through September 2025. Rayhunter runs on an Orbic mobile hotspot (approximately $20) and analyzes cell network traffic in real time for IMSI catcher indicators: downgrade attacks (forcing 2G), unusual IMSI requests, and suspicious base station behavior.

**Important context**: Rayhunter detects, does not block. If it detects a cell-site simulator, your options are: leave the area, power off your phone, or place it in a Faraday bag. The detection value is primarily for documenting patterns (to support legal challenges or civil rights litigation) and for personal awareness.

**EFF's September 2025 update** reported findings from initial deployment — including detection events in proximity to law enforcement activity. This is a useful community monitoring tool, not a complete defense.

**GitHub**: [github.com/EFForg/rayhunter](https://github.com/EFForg/rayhunter)

---

### Mobile Fortify — Handheld Field Biometric Identification

ICE deployed Mobile Fortify in 2025 — a handheld smartphone app that allows agents to photograph an individual in the field and run contactless fingerprint and facial recognition scans against DHS biometric databases (including the Homeland Advanced Recognition Technology platform, which retains biometric data for 75–100 years from date of birth). The app has been used more than 100,000 times since launch. Mobile Fortify changes the physical encounter threat geometry in a way the standard IMSI catcher model does not: biometric collection no longer requires a formal government processing facility. It can occur at a traffic stop, on a street corner, or at a protest perimeter — any location where an ICE agent is present. Practical countermeasures carry over from existing facial recognition guidance: a medical-grade mask (N95 or FFP2) covering the nose and mouth disrupts the lower facial geometry that most recognition algorithms require; a hat with a full brim reduces overhead and oblique angle acquisition; sunglasses defeat periorbital feature extraction. A documented accuracy problem with Mobile Fortify matters for threat modeling: in at least one reported case, the same individual scanned twice in the same encounter was returned two different (both incorrect) names, meaning false-positive identification shifts the burden of proof onto the person who is wrongly matched. If you are approached and believe you may have been incorrectly identified by a field device, do not confirm or deny identity without legal counsel — the match is not legally conclusive. Avoid predictable movement patterns (daily commute at fixed times, habitual gathering locations) that allow pattern-of-life analysis to predict where you will be; Mobile Fortify's value to investigators increases when combined with Palantir's ELITE address confidence scoring, so the same behavioral randomization that degrades ELITE scoring (Part 2.3) also degrades the predictive value of any Mobile Fortify encounter data.

---

## Summary: Tier-by-Tier Minimum Viable OpSec

### Tier 1 (Baseline — Journalists, Advocates, Healthcare Workers)
- Signal with disappearing messages enabled (1 week default)
- ProtonMail for sensitive email; Proton-to-Proton where possible
- Full-disk encryption on all devices (FileVault on Mac, LUKS on Linux, BitLocker with strong PIN on Windows if necessary)
- Use a PIN (not biometric) for phone unlock
- Disable iCloud backup for sensitive apps (iOS) or use GrapheneOS
- Mullvad or ProtonVPN for browsing
- KeePassXC for passwords

### Tier 2 (Intermediate — Activists, Organizers, Protest Participants)
All of Tier 1, plus:
- Signal usernames enabled; "Who can find me by my number" set to Nobody (Settings > Privacy > Phone Number)
- GrapheneOS on a Pixel device for the sensitive-activity phone
- Separate dedicated device for activist activity; never co-locate with personal phone
- Register Signal on secondary phone with a VoIP number not linked to identity
- Burner SIM purchased with cash for secondary device (used only away from home)
- Leave phone at home for protests and sensitive meetings; use Faraday bag when this isn't possible
- VPN then Tor (connect Mullvad first, then launch Tor Browser) for sensitive research — hides Tor usage from your ISP
- Briar for contacts where zero phone-number metadata is required
- Separate payment method (cash-loaded prepaid card) for activist-related purchases
- Proton Mail accessed only over Tor, registered over Tor
- OnionShare for sensitive document exchange

### Tier 3 (Advanced — Direct Targets of Investigation)
All of Tier 2, plus:
- Qubes OS or Tails OS for sensitive digital activity
- Signal registered on a VoIP number purchased via Tor, on a dedicated device never used near home or workplace
- Monero for all digital payments connected to sensitive activity
- VeraCrypt encrypted containers for sensitive files (additional layer beyond full-disk encryption)
- YubiKey hardware security key for all critical accounts
- Data hosted only on non-U.S. providers (Proton, Mullvad, Disroot, Systemli)
- Legal representation identified and contacted proactively (NLG, EFF, ACLU)
- Incident response plan established with organizational contacts

---

## Key Sources

- [EFF Surveillance Self-Defense](https://ssd.eff.org/) — foundational practical guide
- [EFF: Meet Rayhunter (March 2025)](https://www.eff.org/deeplinks/2025/03/meet-rayhunter-new-open-source-tool-eff-detect-cellular-spying)
- [Signal: Phone Number Privacy and Usernames](https://signal.org/blog/phone-number-privacy-usernames/)
- [GrapheneOS: grapheneos.org](https://grapheneos.org)
- [Tor Project: torproject.org](https://www.torproject.org)
- [Privacy Guides: privacyguides.org](https://www.privacyguides.org)
- [Briar Project: briarproject.org](https://briarproject.org)
- [SecureDrop: securedrop.org](https://securedrop.org)
- [OnionShare: onionshare.org](https://onionshare.org)
- [VeraCrypt: veracrypt.fr](https://www.veracrypt.fr)
- [NSA Signal warning (February 2025) — CBS News](https://www.cbsnews.com/news/nsa-signal-app-vulnerabilities-before-houthi-strike-chat/)
- [VPN no-log court-proven policies analysis](https://vpnsuggest.com/court-proven-vpn-no-log-policies-legal-cases/)
- [GrapheneOS vs. iOS security comparison — Cape.co](https://www.cape.co/blog/grapheneos-vs-ios)
- [CLOUD Act vs. GDPR conflict — Exoscale](https://www.exoscale.com/blog/cloudact-vs-gdpr/)
- [NACDL Compelled Decryption Primer](https://www.nacdl.org/Content/Compelled-Decryption-Primer)
- [Freedom Press Foundation: Enable Signal Usernames (journalists)](https://freedom.press/digisec/blog/enable-signal-usernames/)
- [GrapheneOS exits France — what it means for encryption (Proton, November 2025)](https://proton.me/blog/grapheneos-france)
- [iOS 18 inactivity reboot feature — Magnet Forensics analysis](https://www.magnetforensics.com/blog/understanding-the-security-impacts-of-ios-18s-inactivity-reboot/)
- [LocalMonero shutdown — CoinDesk](https://www.coindesk.com/opinion/2024/05/16/localmonero-shutdown-is-another-blow-for-privacy-tech)

*This document depends on `threat-model.md` for the underlying threat capability analysis. All recommendations should be reassessed as the threat model is updated.*
