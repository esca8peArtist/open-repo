---
title: "Journalist Security at Scale: Operational Security for Investigative Journalists, Photojournalists, and News Organizations"
project: cybersecurity-hardening
created: 2026-05-06
status: scenario-specific-guide
phase: Phase 2
session: 844
depends_on:
  - threat-model.md
  - opsec-playbook.md
  - implementation-guide.md
  - palantir-threat-model.md
  - PHASE_2_SEQUENCING_STRATEGY.md
  - encrypted-messaging-implementation-guide.md
confidence: high — threat claims grounded in documented government capabilities (CBP Directive 3340-049B January 2026, FISA Section 702 PCLOB reports, NSL statutory authority and ODNI transparency statistics, Babel Street DHS contract documentation, Clearview AI ICE contract, Mobile Fortify 100,000+ deployment record); Section 702 authorization is in active legislative flux — Congress passed a 45-day extension April 30, 2026, current authorization expires mid-June 2026 minimum; the authorization landscape should be treated as current to June 2026 and reviewed thereafter
audience: Investigative journalists (print, digital, broadcast, freelance), photojournalists and documentary filmmakers, news organization IT security teams, legal counsel to news organizations, press freedom organizations (PEN America, Committee to Protect Journalists, Freedom of the Press Foundation)
---

# Journalist Security at Scale

**This playbook is not legal advice and does not substitute for legal counsel to the news organization. Legal questions — including subpoena response, shield law claims, and Section 702 compliance — require organization-specific counsel. The highest-ROI action for any news organization facing a subpoena is legal consultation before any response. No exception.**

---

**Executive Summary for Investigative Journalists, News Organizations, and IT Security Teams**: The threat model for journalists in 2026 is a specific subset of the general government surveillance stack — but it has unique features that generic security guides do not address. CBP has full device search authority at U.S. international border crossings without a warrant, making every international reporting trip a potential source-exposure event. PRISM (Section 702 FISA) gives the FBI compelled access to journalist email, cloud storage, and communications when those channels touch foreign sources — regardless of legal journalistic privilege. National Security Letters compel carrier and ISP metadata disclosure without judicial authorization and with permanent gag orders, meaning neither the journalist nor their news organization is notified. Babel Street continuously monitors public journalist social media profiles. And Clearview AI and Mobile Fortify are available at enforcement actions journalists cover.

None of these threats require illegal activity by the journalist. They are the operational environment journalists enter when they cross a border, receive documents from a foreign source, report from an enforcement action, or receive a tip through an unprotected channel.

**The single most impactful distinction between this playbook and the Institutional Whistleblowing Playbook**: the whistleblower playbook focuses on protecting the source during the act of disclosure. This playbook focuses on protecting the journalist's operational security when receiving and working with leaked information — including border crossing device security, source compartmentalization architecture, and the Signal safety number verification requirement that distinguishes secure from insecure source communication. These are qualitatively different problems with different countermeasures.

**The single finding that matters most before you read further**: Signal safety number verification is a prerequisite for secure source communication, not an optional step. An unverified Signal contact is one where a government-controlled intermediary could substitute their keys and read every message. For sensitive sources — particularly foreign sources under PRISM risk — verification is not an enhancement. It is the baseline.

---

## Part 1: Understanding the Journalist Threat Surface

### 1.1 CBP Device Search Authority at Border Crossings

U.S. Customs and Border Protection agents have full authority to search electronic devices at international border crossings — airports, land crossings, and sea ports — without a warrant, without probable cause, and without judicial authorization of any kind.

The statutory basis is the "border search exception" to the Fourth Amendment, recognized by the Supreme Court in *United States v. Flores-Montano* (2004) and applied to electronic devices by CBP Directive 3340-049B, revised January 2026. The Directive distinguishes two search types:

**Basic search**: A manual review of accessible device content — the agent scrolls through your photos, messages, and documents. Can be conducted at the officer's discretion without any stated suspicion. No supervisory approval required.

**Advanced search**: A forensic extraction using software tools (Cellebrite UFED is CBP's documented platform). Connects your device to extraction hardware that can recover deleted files, app data, location history, cached passwords, and message history. Requires supervisory approval and "reasonable suspicion of activity in violation of the laws enforced or administered by CBP, or a national security concern."

The 2026 Directive includes a provision for sensitive materials — journalistic content, attorney-client communications, and medical records — that requires supervisory involvement before review. But this provision does not prevent device seizure and advanced extraction: it only governs the review process for flagged sensitive categories. A forensic image of your device can be taken and reviewed later under the sensitive-materials protocol, meaning source identities, draft documents, and message history can be copied before any content review determination is made.

**The operational implication for journalists**: CBP searched 55,318 devices at ports of entry in fiscal year 2025, a 16.7% increase from two years prior. Journalists crossing with source-identifying data, unpublished documents, or active Signal conversations are statistically at risk. The countermeasure is not legal argument at the border — the law currently permits the search. The countermeasure is eliminating the data before you cross. Part 2 of this playbook addresses the travel device protocol in full.

**Ongoing litigation note**: EFF filed an amicus brief in the U.S. Court of Appeals for the Third Circuit in March 2026 arguing that border searches of electronic devices require a warrant. As of May 2026, this litigation has not changed CBP's legal authority. Journalists should operate under the existing rule — that warrantless border device searches are lawful — and not rely on litigation outcomes as operational security.

Sources: [CBP Directive 3340-049B (January 2026)](https://www.cbp.gov/sites/default/files/2026-01/cbp_directive_3340-049b_jan_2026_508.pdf), [EFF — Border Searches](https://www.eff.org/issues/border-searches), [EFF — Journalist Security Checklist for Border Travel](https://www.eff.org/deeplinks/2025/06/journalist-security-checklist-preparing-devices-travel-through-us-border)

---

### 1.2 PRISM and Section 702: Compelled Access to Journalist-Source Communications

PRISM operates under Section 702 of the Foreign Intelligence Surveillance Act (FISA), 50 U.S.C. § 1881a. Under Section 702, the FBI can serve directives on electronic communications service providers — Gmail (Google), iCloud (Apple), Outlook (Microsoft), Yahoo Mail, and others — compelling them to provide the content of communications for targeted individuals.

**What Section 702 means for journalists covering international stories**: When a journalist communicates with a foreign source through any of the above platforms, that communication is at meaningful risk of PRISM collection. The statutory authority targets the foreign source (a "non-U.S. person reasonably believed to be located outside the United States"), but the collection incidentally captures the journalist's side of the communication. That incidentally collected U.S.-person communication — the journalist's email or message — is then searchable by the FBI without an additional warrant, through the "backdoor search" mechanism documented in the PCLOB's 2023 Section 702 report.

The PCLOB found that the FBI conducted warrantless backdoor searches of Section 702-acquired communications for: Black Lives Matter protesters, U.S. government officials, journalists, political commentators, and 19,000 donors to a congressional campaign. These were not criminal investigations — they were queries run against the 702 database on individuals the FBI had reason to examine.

**The 2026 authorization status**: Congress reauthorized Section 702 via the Reforming Intelligence and Securing America Act (RISAA) on April 20, 2024, with a sunset of April 20, 2026. On April 30, 2026, Congress passed a 45-day extension after failing to reach consensus on reforms. As of May 2026, Section 702 authority extends at minimum through mid-June 2026. Regardless of the specific reauthorization timeline, PRISM has operated continuously since 2007 and has been reauthorized repeatedly. Journalists should treat it as a permanent capability, not a temporary one.

**What this means operationally**: If you use Gmail, iCloud, Outlook, or standard SMS to communicate with a foreign source, those communications are potential PRISM collection targets. The countermeasures in Part 5 address this directly.

Sources: [FISA Section 702 — Brennan Center 2026 Resource Page](https://www.brennancenter.org/our-work/research-reports/section-702-foreign-intelligence-surveillance-act-fisa-2026-resource-page), [Congress extends FISA 702 for 45 days — NPR](https://www.npr.org/2026/04/29/g-s1-119094/congress-fisa-702), [EFF — Congress Must Reject New Insufficient 702 Reauthorization Bill](https://www.eff.org/deeplinks/2026/04/congress-must-reject-new-insufficient-702-reauthorization-bill)

---

### 1.3 National Security Letters: Compelled Metadata Disclosure Without Notice

National Security Letters (NSLs) are administrative subpoenas issued by the FBI without judicial authorization. They compel phone carriers, ISPs, and financial institutions to disclose customer records. The statutory authority spans three statutes: 18 U.S.C. § 2709 (electronic communications), 12 U.S.C. § 3414 (financial records), and 15 U.S.C. § 1681u (consumer reports).

**What NSLs compel** from phone carriers and ISPs:
- Records of all calls placed and received: numbers, timestamps, duration, cell tower location data
- Internet connection records: IP addresses, domains connected to, timestamps (but not content)
- Subscriber information: the identity behind an account

**What NSLs cannot compel**: message content from encrypted messaging services. Signal, served with an NSL in 2016, disclosed only account creation date and last connection date — because that is all Signal retains. This is Signal's documented minimum-retention design.

**The journalism-specific risk**: An NSL metadata timeline showing a journalist repeatedly calling a government employee on the same day classified documents went missing creates a circumstantial record — even without any message content. NSLs are accompanied by permanent gag orders: the carrier or ISP cannot disclose the NSL to the journalist. The journalist does not know the NSL was served. The FBI can reconstruct who the journalist called, when, how frequently, and from where — without the journalist or their legal counsel learning this happened until a criminal proceeding begins, if ever.

The ODNI reports that the FBI issues approximately 10,000–15,000 NSLs annually in recent years. The specific targeting of journalists is not separately tracked in the public transparency reports, but the FBI's own Domestic Investigations and Operations Guide (DIOG) establishes that NSLs can be used in any national security investigation, including leak investigations.

Sources: [ODNI Annual Statistical Transparency Report, Calendar Year 2024](https://www.dni.gov/index.php/newsroom/reports-publications/reports-publications-2025/4071-astr-cy24), [EFF — National Security Letters](https://www.eff.org/issues/national-security-letters), [Signal — What NSL disclosed](https://signal.org/bigbrother/)

---

### 1.4 Babel Street: Continuous Social Media Monitoring of Journalist Profiles

Babel Street is a commercial OSINT platform with confirmed DHS, ICE, CBP, and State Department contracts. Its "persistent search" feature continuously monitors any new public content matching flagged individuals, keywords, or geographic areas — without a new analyst query being initiated. The system automates scraping and real-time flagging at scale.

As documented in the activist playbook and `palantir-threat-model.md`, Babel Street was used against pro-Palestine student protesters and feeds directly into the State Department's "Catch and Revoke" visa revocation pipeline. For journalists, the relevant risk is different from activists: the primary concern is not visa revocation, but profile-building. A journalist's public social media, published articles, Twitter/X posts, and LinkedIn profile create a behavioral and relationship map that Babel Street can ingest and query. If a journalist publicly interacts with individuals who are themselves Babel Street investigation targets, that interaction creates a relationship node in the system.

**Journalist-specific implication**: Public reporting, public social media engagement with sources, and public attribution by sources ("as I told journalist X") can all create relationship nodes in the Babel Street system. This is not a reason to stop public reporting — it is a reason to understand that the journalist's public identity and the journalist's source compartmentalization are two separate surfaces requiring separate protection strategies.

---

### 1.5 Biometric Surveillance at Enforcement Actions

Photojournalists and documentary filmmakers covering ICE enforcement actions, protests, or other law enforcement operations face two biometric threats documented in the broader corpus:

**Clearview AI**: Clearview holds a confirmed $9.2M ICE contract. Its facial recognition system is queried against a database of 30+ billion scraped images. A photojournalist who appears in publicly indexed images — from a publication's website, LinkedIn, press badge photos, or prior coverage — is potentially identifiable via Clearview query at any enforcement action where law enforcement is present.

**Mobile Fortify**: ICE's handheld biometric identification app has been used more than 100,000 times since launch. Photojournalists are physically present at the enforcement scenes these agents work. An ICE agent who photographs a photojournalist — intentionally or incidentally while photographing the scene — creates a biometric query that can return identity matches against DHS HART platform records. Part 7 addresses physical security protocols at enforcement actions.

---

### 1.6 Deepfake Threats to Journalist Identity and Credibility

As documented in `PHASE_2_SEQUENCING_STRATEGY.md` Section 1.3, deepfake generation tools capable of creating synthetic video that passes basic authenticity checks are now accessible with minimal technical skill. For journalists with public video presence — broadcast reporters, documentary filmmakers, interview subjects — fabricated video attributing statements they never made is a documented and realistic threat.

This is distinct from government surveillance and is included here because: (a) the fabrication threat is most acute against journalists with established credibility, and (b) countermeasures require proactive provenance documentation that most journalists do not currently practice. Part 6 addresses newsroom-level provenance documentation.

---

## Part 2: Border Crossing Device Security

### 2.1 The Core Principle: No Source-Identifying Data Crosses the Border on Your Device

CBP's full-device search authority means that any device you carry across a border is a potential source-exposure event. The correct countermeasure is structural: maintain a travel device with no source-identifying data, and access source material only after clearing customs on a different network from an account that was not accessible on the device during transit.

This is not inconvenient in theory — it requires discipline and advance preparation. The journalists who lose source data at borders are not those who ignored a complex protocol; they are those who forgot to log out of their usual Signal account before a flight, or who carried their working laptop with documents in the bag without thinking about the border context.

### 2.2 Travel Device Protocol

**Travel device selection**: The travel device should be separate from your working device and configured fresh before each international trip. Preferred option: a dedicated travel laptop (or a Pixel phone configured for this purpose) that you restore to a clean state before crossing.

**What the travel device must not contain**:
- Any Signal account (log out and deregister before travel — see Step 2.3)
- Any ProtonMail, encrypted email, or personal email account
- Any documents related to current investigations, sources, or unpublished stories
- Any contact lists that include source names or pseudonyms
- Any browser history referencing sources, story subjects, or encrypted communication tools
- Any VPN credentials that are linked to your identity (log out and delete before travel)
- Cloud storage apps that are logged into accounts with source-related documents

**What the travel device should contain**: Only applications necessary for the trip — standard browser (Safari, Chrome), standard email (the organizational account you use for press inquiries, not source communication), and any tools you legitimately need for the assignment without source-related data.

**Verification before travel**: Run through the checklist in Part 8 (Tier 1) 24 hours before departure. This is not paranoia — it is the same discipline a journalist applies to fact-checking before publication.

### 2.3 Signal Account Management for Border Crossings

Signal does not support a "travel mode" that hides conversations. The only safe option when crossing a border is to deregister your Signal number from the travel device before crossing, and re-register after clearing customs.

**Step-by-step border Signal protocol**:

1. Before crossing: Open Signal on your usual device > Settings > Account > Delete Account. This removes your Signal account from the device and from Signal's servers. Your message history is deleted from the device. Your contacts will see your account as unavailable.

2. On the travel device: Do not register Signal. The device should not have Signal installed.

3. After clearing customs: On the other side of the border, re-register Signal on your usual device or a reconstituted device using your number. Your message history will not restore (it was deleted when you deregistered), but you can resume contact with established contacts. Note: you will need to re-verify safety numbers with sensitive contacts after re-registering, because re-registration generates a new key pair.

**Why this matters**: An active Signal account on a device is accessible to CBP during an advanced search — the messages are stored locally on the device and Cellebrite UFED has a Signal extraction module. Deregistering before crossing deletes local message storage. An unregistered Signal app (or no Signal installed) gives CBP nothing to extract.

### 2.4 Cloud Storage Strategy: Encrypted Access Post-Customs

Working documents for an investigation should be stored in encrypted cloud storage (ProtonDrive or Cryptomator-encrypted storage on any provider) and accessed only after clearing customs.

**The rule**: Do not be logged into any cloud account on the travel device during transit. The travel device should not have the ProtonDrive app installed, should not have Google Drive logged in, and should not have iCloud enabled. After clearing customs on a different network, log in, access your documents, and resume work.

**Why "after clearing customs on a different network" matters**: If CBP detains you for secondary inspection and compels you to unlock your device, a logged-in cloud account allows them to browse cloud-stored documents in real time. A device with no cloud credentials prevents that browsing, even if the device itself is searched.

### 2.5 Network Separation at the Border

Do not connect to the free Wi-Fi network inside airport customs or border processing facilities. These networks are operated by or available to the facility where CBP works. Any network traffic from a logged-in device on that network is visible. Use your phone's cellular data for any personal communication during and immediately after the crossing process, not facility Wi-Fi.

---

## Part 3: Source Communication Compartmentalization

### 3.1 Why Standard Signal on a Personal Phone Is Insufficient for Sensitive Sources

Signal is end-to-end encrypted and is the correct baseline for source communication. But using Signal on the same phone and account you use for personal communication creates several unacceptable risks:

**Entity resolution via contact list**: If your personal Signal account is subpoenaed or your device forensically extracted, your contact list — including source contacts under any pseudonym — is exposed in a single extraction event. A contact list showing you have regular Signal communication with "J.D." or a number registered to a burner phone creates a lead even without message content.

**Metadata co-mingling**: Your personal phone creates a metadata pattern linking your daily life (location, timing, frequency of communication) to your source contact pattern. A Palantir-style behavioral analysis applied to carrier metadata can identify which contacts align with reporting on specific topics — even without content.

**Safety number verification failure**: If your Signal account has multiple contacts and you have not verified safety numbers, you cannot be certain that a government-controlled intermediary has not replaced your source's keys. This is the man-in-the-middle attack vector that safety number verification is designed to prevent. On a high-contact personal account, it is practically impossible to verify every safety number. On a dedicated source communication device with a limited contact list, verification is feasible.

**Device seizure exposure**: If your personal device is seized — at a border, during an arrest at a protest you are covering, or pursuant to a subpoena — it yields your entire source contact history in a single event.

### 3.2 The Dedicated Source Communication Device

**The correct architecture**: A dedicated GrapheneOS device with its own phone number, used exclusively for source communication, physically separated from your personal and professional devices.

**Setting up the dedicated device**:

1. **Hardware**: A Google Pixel 6 or later (Pixel 8 preferred for hardware memory tagging). GrapheneOS installation instructions at grapheneos.org. Cost: $200–$500 for the Pixel hardware; GrapheneOS is free.

2. **Phone number**: Register Signal with a VoIP number rather than a carrier-traceable SIM. Recommended providers for journalists: MySudo (provides isolated numbers with separate data compartments), JMP.chat (XMPP-based VoIP with strong privacy properties), or Google Voice (lower privacy but widely accepted — use only if the stronger options are not feasible). The VoIP number must never be linked to your personal carrier identity: purchase the account on a different device, on a different network, with a payment method not connected to your primary identity.

3. **Signal registration**: Register Signal on the dedicated device with the VoIP number. Set disappearing messages to a default appropriate to your risk level (7 days for most investigative journalism; 24 hours for the most sensitive ongoing source contact).

4. **Isolation discipline**: The dedicated device must never appear in the same location at the same time as your primary personal device. If they are co-located, the metadata correlation between the two devices is the entity-resolution link that defeats the separation. When not in use, the dedicated device should be powered off and stored away from your primary phone. See `PHASE_2_SEQUENCING_STRATEGY.md` Section 2.1 for the full compartmentalization architecture.

5. **GrapheneOS configuration**: Set auto-reboot to 18 hours (Settings > Security > Auto-reboot Timer). This ensures the device returns to Before First Unlock (BFU) state after 18 hours without use — at which point Cellebrite extraction is severely limited because encryption keys are not loaded in memory. Details in `implementation-guide.md` and `PHASE_2_SEQUENCING_STRATEGY.md` Section 2.5.

### 3.3 Signal Settings for Source Security on the Dedicated Device

Beyond the baseline of using a dedicated device, Signal has several settings that are specifically relevant for source security and are frequently misconfigured:

**Disappearing messages**: Set the default timer. For investigative work, 7-day disappearing messages balance operational continuity with limiting the time window for stored messages to be exposed. For the most sensitive ongoing source relationships, reduce to 24 hours or 1 hour. Disappearing messages do not prevent interception during transmission — they limit exposure from device forensics after the fact.

**Phone number privacy**: Settings > Privacy > Phone Number > Who can find me by number: set to "Nobody." This prevents anyone who has your VoIP number from confirming you use Signal on that number — limiting Babel Street OSINT's ability to link your VoIP number to your Signal presence.

**Note sync disabled**: Settings > Chats > Generate link previews: Off. Settings > Notifications > Show in notifications: Name only (not message content). Ensure that Signal's optional "Note to Self" sync feature, if enabled, does not expose source conversation previews in system notifications visible on a locked screen.

**Sealed sender**: Signal uses sealed sender by default, which hides the sender's identity from Signal's servers when delivering messages. Ensure you are running a current Signal version — sealed sender has been enabled by default since Signal version 4.x.

---

## Part 4: SecureDrop at News Organizations

### 4.1 What SecureDrop Is and How It Differs From Journalist-Owned Secure Channels

SecureDrop is an open-source whistleblower submission platform developed and maintained by the Freedom of the Press Foundation (FPF). As of 2026, SecureDrop operates at more than 70 media organizations worldwide, including The New York Times, The Washington Post, The Guardian, ProPublica, The Intercept, Der Spiegel, NBC News, and the Associated Press.

**The critical architectural distinction from journalist-owned Signal or encrypted email**: SecureDrop is source-facing infrastructure operated by the news organization, not by individual journalists. This creates two protections that journalist-owned channels cannot provide:

First, anonymity by design: SecureDrop sources access the submission interface exclusively through the Tor network. There is no clearnet interface. A source accessing SecureDrop via Tor Browser has their IP address masked before the request reaches the server — the server sees only a Tor exit node, not the source's real IP. SecureDrop servers are configured to not log IP addresses, and FPF conducts regular security audits to verify this configuration.

Second, encrypted at rest before transmission: All submissions are encrypted with the organization's GPG public key before they leave the source's browser. The SecureDrop server operator cannot read submissions. A warrant served on the news organization's server yields only encrypted data that the organization cannot be compelled to decrypt (because decryption requires the journalist's private key, which is on an air-gapped workstation that is not served by the warrant). This is a legally meaningful protection in addition to a technical one.

**For journalists on the receiving side**: The SecureDrop Workstation — the system journalists use to read and reply to submissions — runs Qubes OS and Tails on an air-gapped system physically isolated from the newsroom's network infrastructure. Journalists working with SecureDrop submissions work in an environment that is not connected to the general internet and cannot be remotely compromised through the newsroom's network.

### 4.2 SecureDrop Protocol: End-to-End Encryption for Journalist Replies

The current SecureDrop architecture provides strong protection for source-to-journalist submissions. Journalist replies have historically used only network-layer (Tor) encryption, not end-to-end encryption, which is a weaker protection for the journalist's side of the conversation.

The SecureDrop Protocol (SDP) is FPF's in-development upgrade that adds end-to-end encrypted journalist-to-source replies with peer-reviewed security properties. The SecureDrop mobile app — which will significantly reduce the friction for sources who currently must access SecureDrop via Tor Browser on a desktop — was feature-complete as of late 2025 and pending a security audit for release in 2026.

**What this means for newsrooms currently running SecureDrop**: Until the new Protocol is deployed at your specific installation, journalist-to-source replies should be treated as network-layer protected only. For the most sensitive ongoing source relationships, consider the source communication architecture in Part 3 (dedicated Signal device) for two-way dialogue, and SecureDrop for initial anonymous document submission.

### 4.3 SecureDrop Setup: Resources for Organizations Not Yet Deployed

If your news organization does not operate SecureDrop, FPF provides setup support directly. The process:

1. Contact FPF at securedrop.org/priority-support/ — FPF provides configuration guidance and hardware recommendations.
2. SecureDrop requires dedicated server hardware (a minimum of two servers: the Application Server and the Monitor Server), a network firewall, and the air-gapped SecureDrop Workstation for journalist use.
3. FPF's enterprise support tier includes ongoing security audit, incident response, and version upgrade support.

**Minimum viable deployment timeline**: A news organization that commits staff time and hardware can be operationally live on SecureDrop within 4–6 weeks. The operational discipline requirement — staff training on the air-gapped workstation, maintenance of the Workstation, and verification of the organization's .onion address in the FPF directory — is the ongoing investment.

**The FPF directory**: The authoritative directory of SecureDrop installations and their verified .onion addresses is at securedrop.org/directory. This is the source sources should use to verify a news organization's address. News organizations should ensure their listing in this directory is current.

Sources: [Freedom of the Press Foundation — SecureDrop](https://freedom.press/organizations/securedrop/), [SecureDrop — Looking Back at 2025](https://freedom.press/tech/news/securedrop-looking-back-at-2025/), [SecureDrop Directory](https://securedrop.org/directory)

---

## Part 5: Foreign Source Communication Under PRISM

### 5.1 The Legal Landscape: Section 702 and Journalist-Foreign Source Privilege

This is the most legally complex section in this playbook, and it requires an explicit upfront clarification: **journalist-source privilege under state shield laws does not constrain Section 702 surveillance**. Section 702 is a foreign intelligence authority, not a domestic law enforcement authority. Shield laws are state statutes (and, in proposed form, the federal PRESS Act, which has not been enacted as of May 2026) that govern subpoenas and compelled testimony in judicial proceedings. They have no bearing on intelligence collection conducted under FISA authority.

**The current state of journalist-source legal protection**:

*State shield laws*: 40 states plus the District of Columbia have enacted shield laws providing some protection against compelled disclosure of journalist sources. The scope varies significantly — some states provide absolute privilege; others provide qualified privilege (a court can override it upon showing sufficient need). Shield law protection applies in state judicial proceedings and, in most cases, in federal judicial proceedings in those states. The relevant states for investigative journalism organizations include New York (absolute privilege for confidential sources under New York Civil Rights Law § 79-h), California (absolute privilege under California Evidence Code § 1070), and the District of Columbia (qualified privilege).

*Federal shield law*: There is no federal shield law as of May 2026. The PRESS Act (S.2074/H.R. 4481) has passed the Senate unanimously twice (2022, 2024) but has not been enacted into law. In federal criminal proceedings, the First Amendment provides a weaker and more qualified protection than state shield laws, and courts have disagreed on its scope.

*The gap that matters for PRISM*: Section 702 collection is not a judicial proceeding. It is an intelligence collection authority. No shield law — state or federal — prevents the intelligence community from collecting journalist-foreign source communications under 702 authority. The protection shield laws provide is at the point of compelled judicial disclosure (when the government wants to use the information in a proceeding against the journalist or someone else), not at the point of collection.

**Practical implication**: A journalist's communications with a foreign source over Gmail are collectable under PRISM regardless of whether the journalist could successfully invoke a shield law if the government tried to subpoena the same communications in a judicial proceeding. The collection happens at the network level, before any judicial process begins.

**The countermeasure architecture is technical, not legal**: Because no legal protection prevents Section 702 collection, the operational countermeasure is ensuring the communications are not collectable by PRISM-reachable services. Signal, properly configured, is not a PRISM endpoint. Gmail is. The distinction is the platform, not the legal protection.

### 5.2 Signal Safety Number Verification: The PREREQUISITE for Secure Foreign Source Communication

**This is the single most important operational requirement in this playbook. It is not a best practice. It is a prerequisite.**

Signal uses end-to-end encryption where each user's messages are encrypted with the recipient's public key. The safety number for a conversation is a cryptographic fingerprint derived from both parties' public keys. When the safety number matches on both ends, you and your source hold each other's real public keys and only your devices can decrypt messages in that conversation.

If a government agency — or any attacker — were to perform a man-in-the-middle attack on your Signal conversation by substituting their own keys for your source's keys, the safety number you see would be different from the safety number your source sees. Safety number verification catches this attack. Without verification, you cannot know whether your "encrypted" conversation is actually encrypted between you and your source, or between you and an intermediary who is also reading the messages before re-encrypting them for your source.

**The specific risk for foreign source communication**: Foreign sources may be under surveillance by their own governments, by U.S. intelligence services, or by other actors. A foreign source who uses a device or phone number that has been compromised at the software level may unknowingly be using keys that an adversary controls. Safety number verification catches this scenario: if the source's keys have been replaced, the safety numbers will not match and you will know before sending anything sensitive.

**How to verify safety numbers with a foreign source**:

*Preferred method — in-person QR code scan*: When you and your source meet in person, open Signal > the conversation > the source's name > View Safety Number. One of you taps "Scan Code" and scans the other's QR code. If the codes match, tap "Mark as Verified." This is the gold standard: it is unforgeable and requires no secondary channel.

*Remote verification — out-of-band channel*: If in-person verification is not possible, compare safety numbers over a different channel where you have independent confidence in the identity of the person you are communicating with. Options: a phone call (voice confirmation that the numbers match), a video call, or comparison via a professional social media account where you have independent identity confirmation. You read aloud half the safety number; your source reads the other half. Do not compare safety numbers over the same Signal conversation you are trying to verify — that defeats the purpose.

**After a source's phone number changes, a new device, or a reinstall of Signal**: The safety number for your conversation will change. Signal will notify you of this change with a gray message in the conversation. **Do not continue sending sensitive material until you have re-verified the safety number through an out-of-band channel.** A changed safety number is the signal that the keys have changed — which can happen legitimately (the source got a new phone) or maliciously (the source's keys were replaced). Re-verification resolves the ambiguity. There is no acceptable shortcut.

Sources: [Signal — What is a safety number?](https://support.signal.org/hc/en-us/articles/360007060632-What-is-a-safety-number-and-why-do-I-see-that-it-changed), [Freedom of the Press Foundation — Checking identities in Signal](https://freedom.press/digisec/blog/ask-a-security-trainer-checking-identities-in-signal/), [RSF — How to be safe using Signal](https://safety.rsf.org/how-to-be-safe-while-using-signal/)

### 5.3 Foreign Number Registration Strategy

Registering your dedicated source communication Signal account with a foreign phone number — or with a VoIP number that is not linked to your U.S. carrier identity — provides one additional layer of metadata protection: an NSL served on a U.S. carrier cannot return records for a number that is not registered with that carrier.

**The practical options**:

*International SIM purchased locally*: When reporting in a foreign country, purchasing a local prepaid SIM (in cash, if possible) and registering Signal with that number for the duration of the reporting trip creates a number with no U.S. carrier records. After the trip, you can migrate your sources to a new contact channel on your return.

*Persistent non-carrier number*: MySudo provides virtualized phone numbers not tied to a carrier, with separate data compartments per number. JMP.chat provides XMPP/SIP-based VoIP with stronger privacy properties. Either option, registered outside your primary identity, provides persistent protection without the operational complexity of rotating SIMs.

**The limitation of non-carrier registration**: A non-carrier number does not prevent PRISM collection of your Signal message metadata through the server-side Signal infrastructure. It limits what a U.S. carrier NSL can yield. Both protections are meaningful; neither alone is complete. The combination — dedicated device, non-carrier number, verified safety numbers, Signal's sealed sender — creates a comprehensive protection against the documented threats.

### 5.4 Signal Settings for the PRISM Risk Environment

Beyond the settings in Part 3.3, the following are specifically relevant for foreign source communication:

**Note to Self sync**: If enabled, Signal syncs messages across your devices. If your Signal account is on multiple devices (phone and desktop, for example), a subpoena to your desktop Signal installation yields messages that are also on your phone. For the dedicated source communication device, register Signal on one device only. Do not link the dedicated device's Signal account to Signal Desktop.

**Read receipts**: Settings > Privacy > Read Receipts: Off. Read receipts confirm to the sender that you have opened their message — useful for normal communication, but it creates a timestamp record of when you were actively using the device that can be correlated with other behavioral data.

**Typing indicators**: Settings > Privacy > Typing Indicators: Off. Same rationale as read receipts.

**Registration lock**: Settings > Account > Registration Lock: On. This requires your PIN before anyone can re-register your Signal number on a new device, preventing a government agency (or other adversary) from hijacking your Signal number by porting your phone number and registering a new device before you notice.

---

## Part 6: Newsroom IT Security and Team Protocols

### 6.1 Why Individual Journalist Security Is Insufficient Without Organizational Protocols

The threat model for investigative journalism is asymmetric: the weakest link in a reporting team's security is the point of compromise. A journalist who maintains a perfectly compartmentalized dedicated source device is exposed if their editor discusses the same source in a Slack message, if the news organization's IT system is compromised, or if a colleague responds to a subpoena without coordinating with legal counsel first.

Newsroom security is a team protocol problem, not an individual problem. The individual countermeasures in this playbook are necessary but not sufficient. This section addresses the organizational layer.

### 6.2 Organizational Device Management

**Device separation policy**: News organizations should establish a written policy specifying which devices are appropriate for which categories of work:
- Organizational-issued devices (managed, monitored, and in some cases legally owned by the organization) are appropriate for published work, standard editorial communication, and public-record newsgathering.
- Personal devices and dedicated compartmentalized devices (journalist-owned, unmanaged) are appropriate for source communication — specifically because organizational devices are subject to the organization's IT management and, in some jurisdictions, to legal claims that the organization's IT systems are a discoverable repository.

**Separate communication channels for sensitive work**: The news organization's standard email (Exchange, Gmail Workspace, Outlook) is subject to organizational IT oversight, cloud provider access, and PRISM if it handles international communications. For source-related communication, journalists should not use organizational email channels. Dedicated encrypted communication should be the organizational standard for source-related discussion between journalists and their editors.

**ProtonMail for sensitive editorial communication**: Organizations that adopt ProtonMail (Swiss jurisdiction, end-to-end encrypted between ProtonMail accounts) for editorial discussion of sensitive investigations get a meaningful protection upgrade over standard email: Swiss law rather than PRISM authority governs compelled access to ProtonMail server content, and end-to-end encryption means ProtonMail itself cannot read the messages. This is not a complete substitute for Signal-level protection, but it is significantly better than Gmail or Exchange for editorial discussion.

### 6.3 Team Training on PRISM and NSL Risks

All editorial staff involved in investigations with foreign sources or national security implications should understand:

1. **Email platforms are PRISM endpoints**: Gmail, iCloud, Outlook, and standard SMS are reachable by Section 702 collection. Staff should not discuss sensitive source identities or investigation details over these channels.

2. **NSL gag orders mean no notice**: If a carrier or ISP is served with an NSL for staff metadata, neither the organization nor the staff member will be notified. The news organization cannot retroactively protect metadata that was disclosed before counsel was engaged. The countermeasure is prospective: using communication tools with minimal metadata retention (Signal, ProtonMail) as the default, not as an exception.

3. **Safety number verification is team discipline**: If multiple journalists on the same team communicate with the same source over Signal, each must independently verify safety numbers. A source's keys verified by one journalist are not thereby verified for another journalist's separate Signal account.

4. **Subpoena response is a legal decision, not an IT decision**: If the news organization receives a subpoena for journalist-source communications, the response is a legal decision that requires counsel review before any production. Premature or overly broad document production in response to a government subpoena is a documented cause of source exposure. The organization should have an established legal counsel relationship for this purpose before any subpoena arrives.

### 6.4 Encrypted Communication Standards for Editorial Teams

**For source-related discussion within the editorial team**:
- Signal groups with a limited, vetted membership (the reporting team + direct editorial supervisors only)
- Disappearing messages enabled (7 days is workable for editorial continuity; shorter for the most sensitive ongoing investigations)
- All members have verified safety numbers with each other

**For document collaboration on sensitive investigations**:
- Avoid Google Docs, Microsoft OneDrive, and Dropbox for sensitive investigation materials — all are PRISM-reachable providers
- ProtonDrive or Cryptomator-encrypted storage on any provider preserves end-to-end encryption for stored documents
- For the highest-sensitivity investigation documents: a physically air-gapped computer, not networked, for drafting and storage until publication

**For communication with legal counsel**:
- Signal with verified safety numbers between reporters and counsel
- Attorney-client privilege protects communications content from compelled production in judicial proceedings — but not from PRISM collection upstream. Maintaining Signal as the channel for sensitive legal discussions limits NSL metadata exposure (only Signal server data is accessible, not the content), though it does not prevent the existence of the communication channel from being discovered.

### 6.5 Legal Counsel for Subpoena Response

Every news organization covering sensitive national security or government accountability investigations should have an established relationship with press freedom legal counsel before a subpoena arrives. Organizations without existing counsel should contact:

**Reporters Committee for Freedom of the Press (RCFP)**: rcfp.org — provides legal support and a legal defense hotline (1-800-336-4243) for journalists and news organizations facing subpoenas, prior restraint attempts, and press freedom threats.

**Volunteer shield law analysis**: RCFP publishes a state-by-state shield law analysis (rcfp.org/reporters-privilege/) that is the authoritative current reference on which states have shield laws, what they cover, and their qualified vs. absolute scope.

**The PRESS Act**: Even though no federal shield law currently exists, several federal courts have recognized a First Amendment-based qualified privilege for journalists in some circumstances. Legal counsel can assess whether this applies in a specific subpoena context.

---

## Part 7: Physical Security During Investigations

### 7.1 Photojournalist Safety at Enforcement Actions

Photojournalists covering ICE enforcement actions, raids, or protests face the biometric threats described in Part 1.5. Operational countermeasures:

**At enforcement action perimeters**:
- Maintain physical distance from ICE agents with Mobile Fortify devices. At close range, a deliberate scan by an agent positioned to capture your face is a different threat than a CCTV camera at 20 meters. Distance degrades the quality of any incidental biometric capture.
- Carry press credentials prominently and in a form that can be displayed without physical engagement with agents. The legal protection press credentials provide is limited, but their presence establishes your journalistic role in any after-the-fact dispute about why you were present.
- Document your own presence: photograph or video your own position and the surrounding scene immediately upon arrival. This establishes a contemporaneous record that you were present as a journalist covering the event, not as a participant.

**Equipment considerations**:
- For photojournalists: a dedicated camera rather than a smartphone provides better operational separation. A camera's contents are not searchable by Mobile Fortify in the same way a phone is. A phone seized by law enforcement yields everything on the device; a camera seized yields only the current memory card.
- If using a smartphone for documentation: use a dedicated phone for journalism work (separate from your personal phone) and have the personal phone powered off or in a Faraday bag while working. This limits any biometric co-location linkage between your professional documentation activity and your personal identity.

### 7.2 Facial Recognition Countermeasures in Field Reporting

The countermeasures documented in the activist playbook (mask + hat + sunglasses combination) are relevant for photojournalists who cover enforcement actions as an ongoing beat. The key distinction: an activist has a tactical reason to avoid identification at a specific event. A photojournalist has an ongoing professional public identity — most journalists are publicly identifiable by name and photo.

The practical application is different: facial recognition countermeasures for journalists are less about defeating identification in a specific encounter and more about creating a documented record that you were engaged in professional journalism rather than becoming a Clearview AI query result associated with enforcement action biometric databases. Press credentials, published bylines, and organizational identification serve this purpose.

For journalists who cover beats where source protection requires that their own presence not be traced (undercover reporting, investigations where the organization has not published the reporter's identity): apply the full activist-level countermeasures (Part 4 of the activist playbook). These are legitimate operational security measures for journalists in this specific context.

### 7.3 ALPR Avoidance for Investigation Coverage

Vehicle license plates are not protectable at enforcement actions. The practical countermeasure is the same as for activists: for reporting on a specific location or event that you want to remain unlinked to your professional identity (reporting on a detention facility without alerting administrators to your vehicle's presence), use a rental vehicle or transit rather than a personal vehicle. ALPR data from a vehicle registered to a journalist appearing repeatedly near a detention facility, an enforcement district office, or a potential source's workplace creates a mapping of the journalist's reporting footprint that can be subpoenaed or searched.

### 7.4 Documentation of Law Enforcement Surveillance of Journalists

Journalists who are surveilled while reporting — photographed by law enforcement at a scene, subject to device search at a border, notified of a subpoena — should document and report to press freedom organizations:

**Committee to Protect Journalists (CPJ)**: cpj.org — CPJ documents journalist harassment, including surveillance and border incidents, in its annual Journalist Safety Index. Reporting to CPJ creates a public record.

**Reporters Committee for Freedom of the Press (RCFP)**: rcfp.org/reporters-privilege/ — RCFP's legal defense resources include shield law invocation support and can advise on documenting surveillance incidents.

**Freedom of the Press Foundation (FPF)**: freedom.press — FPF documents security incidents against journalists and publishes surveillance-related threats to press freedom. FPF also provides a 24/7 digital security helpline for journalists.

**Society of Professional Journalists (SPJ)**: spj.org — The SPJ Freedom of Information committee provides resources for journalists facing government obstruction, including FOIA-based strategies for learning whether they have been subjects of law enforcement inquiries.

---

## Part 8: Implementation Paths

### Tier 1: Essential (All Journalists Doing Sensitive Reporting — No Exceptions)

These measures apply to any journalist covering national security, immigration enforcement, law enforcement, or any other beat where source protection is a genuine operational concern.

1. **Travel device protocol before international travel**: Remove Signal, email accounts, and source-related documents from any device crossing a border. Time: 2–3 hours for setup before first trip; 30 minutes maintenance before each subsequent trip.

2. **Dedicated source communication device**: Install GrapheneOS on a Pixel phone and register Signal with a VoIP number separate from your carrier identity. Configure disappearing messages (7-day default), privacy settings as specified in Part 3.3. Time: 4–8 hours for initial setup.

3. **Signal safety number verification for active sources**: For every current source contact on your dedicated Signal device, complete safety number verification via in-person QR scan or out-of-band channel before sending sensitive material. Time: varies by number of active sources; typically 15–30 minutes per source for remote verification.

4. **SecureDrop assessment**: If your news organization does not operate SecureDrop, raise this with your organization's leadership or IT team. If it operates SecureDrop, verify your organization's listing in the FPF directory at securedrop.org/directory. Time: 1 hour for assessment; 4–6 weeks for organizational deployment if not yet live.

5. **Legal counsel identification**: Identify the news organization's press freedom counsel and their contact information for subpoena response. If the organization has no designated press freedom counsel, contact RCFP (1-800-336-4243) to identify available resources. Time: 1 hour.

**Total Tier 1 time estimate**: 8–15 hours initial investment, plus per-trip maintenance.

---

### Tier 2: Intermediate (Investigative Reporters with Active Foreign Sources or National Security Coverage)

All of Tier 1, plus:

6. **ProtonMail for sensitive editorial communication**: Establish ProtonMail accounts for editorial discussion of sensitive investigation materials with your editor and direct team. Migrate source-related editorial discussion off organizational email. Time: 2–3 hours for account setup and team onboarding.

7. **Encrypted document storage**: Move investigation documents from Google Drive, Dropbox, or iCloud to ProtonDrive or a Cryptomator-encrypted container. Time: 2–4 hours depending on volume of materials.

8. **NSL risk review with counsel**: Brief your organization's legal counsel on the NSL risk for ongoing investigations — specifically, which of your source relationships would be exposed by a carrier NSL. Establish which communication channels are in use and whether they provide adequate metadata protection. Time: 1–2 hour meeting with counsel.

9. **Team safety number verification**: For reporting teams of 2+ journalists working on the same investigation, all team members should verify safety numbers with each other and with any shared sources. This requires coordination to schedule. Time: 30–60 minutes per team member.

10. **FOIA request for your own records**: If you have reason to believe you have been subject to law enforcement inquiry, file Freedom of Information Act (FOIA) requests for your own records from FBI and CBP. The CBP FOIA portal is cbp.gov/travel/cbp-traveler-protection/privacy-act; the FBI FOIA portal is fbi.gov/services/information-management/foipa. These requests are slow and may return redacted results, but the act of filing creates a record that you sought information through legal channels, and partial disclosures have historically revealed surveillance incidents to journalists. Time: 2–3 hours to prepare and file.

**Total Tier 2 time estimate**: 10–15 additional hours beyond Tier 1.

---

### Tier 3: Advanced (Investigative Reporters Under Active Legal Threat, International Correspondents, High-Profile Investigations)

All of Tier 1 and Tier 2, plus:

11. **Full compartmentalization architecture**: Implement the three-device architecture — personal device, professional device, dedicated source device — with no geographic co-location between the source device and the personal device. See `PHASE_2_SEQUENCING_STRATEGY.md` Section 2.1 for full architecture detail.

12. **Tails OS for sensitive document handling**: For the most sensitive investigation documents — particularly those that have arrived via SecureDrop and need to be processed before publication — use a Tails OS installation on a USB drive booted on an air-gapped computer. Tails routes all internet traffic through Tor and leaves no trace on the host computer. Document metadata scrubbing (using mat2 on Tails) removes author information, creation dates, revision history, and device identifiers from files before they enter your normal workflow.

13. **International SIM strategy for international reporting trips**: For extended international reporting trips, purchase a local SIM in cash for source communication registration. Use this number for Signal while in-country; migrate sources to a new contact channel before returning to the US.

14. **Personal FOIA audit and legal retainer**: For journalists who have received prior government scrutiny, who are involved in ongoing high-profile investigations, or who cover classified program leaks: retain individual press freedom counsel independent of organizational counsel. Organizational counsel represents the organization's interests; individual counsel represents your interests, which may not always align. RCFP can provide referrals (1-800-336-4243).

15. **Deepfake provenance documentation**: For broadcast journalists, documentary filmmakers, or any journalist who appears in video that could be subject to deepfake fabrication targeting your credibility: establish a practice of retaining original, unedited video files with timestamp metadata and sharing them with legal counsel or a trusted third party immediately after recording. This creates an authenticated baseline for comparison if fabricated content appears.

**Total Tier 3 time estimate**: 20–30 additional hours beyond Tier 2, plus ongoing discipline.

---

## Part 9: FAQ for Journalists and News Organization Security Teams

**Q: I already use Signal. Why do I need a separate device?**

Signal on your personal phone is secure against interception in transit, but it is not compartmentalized against the two most realistic threats to investigative journalists: device seizure (at a border or during a law enforcement encounter while covering a story) and contact-list exposure (if your personal phone is forensically extracted, all your source contacts — even pseudonymous ones — are visible as a list of Signal contacts). A dedicated device with a limited contact list, verified safety numbers, and no connection to your personal identity surface limits exposure in both threat scenarios. Signal's encryption protects the message content; compartmentalization protects the source relationship.

**Q: Does shield law protection cover my digital communications?**

Shield laws protect you from being compelled to disclose sources in judicial proceedings — not from having your communications collected by intelligence authorities under Section 702 or subject to NSL metadata disclosure. The protection operates at the point of legal compulsion (a subpoena in a proceeding), not at the point of collection. For digital communications, the practical protection is technical, not legal: using Signal and ProtonMail rather than Gmail and SMS means the communications are encrypted in a form that a shield law claim in court can protect from further compelled production — but it cannot retroactively protect communications that were already collected by PRISM before any legal proceeding began.

**Q: When should I verify Signal safety numbers versus when is it excessive?**

Verify safety numbers before sending any material that would expose a source if intercepted. This is not a high bar: it covers any communication that identifies who a source is, what they have told you, or what documents they have provided. For casual professional contacts — a PR person, a government spokesperson you communicate with on the record — safety number verification is not necessary. For any source whose identity must remain confidential, it is prerequisite. The effort required is 5–10 minutes per source for remote out-of-band verification. The cost of not doing it is that your encryption may not be protecting who you think it is.

**Q: Our newsroom uses Google Workspace. Can we keep using it for sensitive editorial discussions?**

Google Workspace is a PRISM-reachable platform. Google can be served with a Section 702 directive compelling production of communications content. For editorial discussion of source identities, sensitive investigation details, or documents provided by confidential sources: no, Google Workspace is not appropriate for these communications. The answer is not to abandon Google Workspace for all purposes — it is to establish ProtonMail (or Signal for the most sensitive discussions) as a parallel channel specifically for source-related editorial communication, and to train staff on what belongs in each channel.

**Q: I'm a freelance journalist without a news organization's IT support. How do I implement this?**

Freelancers are well-suited to the individual countermeasures in Tiers 1 and 2, which are self-implementable without organizational IT support. The primary gap for freelancers is SecureDrop — most freelancers cannot operate their own SecureDrop instance. The alternative: direct sources to SecureDrop at established news organizations (any organization in the FPF directory will receive submissions that you as a contributing journalist can arrange to receive), and establish your secure source communication channel (dedicated GrapheneOS device, verified Signal) as your primary incoming channel. For publications you contribute to regularly, arrange with their security or legal team for a shared SecureDrop arrangement. FPF also provides direct digital security training and helpline support for freelancers (freedom.press/digisec/).

**Q: What do we do if we receive a subpoena for journalist-source communications?**

Do not respond to the subpoena without legal counsel review. The first call is to your news organization's legal counsel or to RCFP (1-800-336-4243). The subpoena's scope, the jurisdiction, the applicable shield law, and whether a motion to quash is available all require legal analysis before any document production. Premature production is the common error — organizations that respond cooperatively to a government request without counsel review may inadvertently produce documents beyond the legal requirement, exposing sources unnecessarily. The legal counsel review determines what, if anything, must be produced; it is not an optional step.

**Q: How do I know if an NSL has been served on my carrier?**

You generally cannot know, because NSLs carry permanent gag orders preventing carriers from disclosing the NSL to the target. The FBI's guidelines do require internal authorization before issuing NSLs targeting journalists, but this does not create a notification obligation. The practical answer is that you cannot know retroactively — you can only limit prospective exposure by using communication tools with minimal metadata retention (Signal registered with a non-carrier VoIP number, ProtonMail) so that a future NSL yields minimal usable metadata.

---

## Resource Directory

### Press Freedom Legal Support
- **Reporters Committee for Freedom of the Press**: rcfp.org | Legal defense hotline: 1-800-336-4243 | Shield law guide: rcfp.org/reporters-privilege/
- **Committee to Protect Journalists (CPJ)**: cpj.org | Documents journalist harassment and surveillance incidents; Journalist Safety Index
- **Freedom of the Press Foundation — Digital Security**: freedom.press/digisec/ | 24/7 digital security helpline for journalists; digital security training
- **PEN America**: pen.org | Press freedom advocacy and journalist protection programs
- **Society of Professional Journalists**: spj.org | FOIA resources and press freedom legal support referrals

### Secure Communication Infrastructure
- **SecureDrop**: securedrop.org | Secure source submission; directory of verified organizational installations
- **SecureDrop Priority Support (for organizations)**: securedrop.org/priority-support/
- **Signal**: signal.org | Safety number verification guide: support.signal.org/hc/en-us/articles/360007060632
- **FPF — Signal Beginners' Guide**: freedom.press/digisec/blog/signal-beginners/
- **FPF — Checking Identities in Signal**: freedom.press/digisec/blog/ask-a-security-trainer-checking-identities-in-signal/

### Device Security
- **GrapheneOS**: grapheneos.org | Hardened mobile OS for dedicated source communication device
- **Tails OS**: tails.boum.org | Air-gapped OS for sensitive document handling
- **EFF — Journalist Border Security Checklist**: eff.org/deeplinks/2025/06/journalist-security-checklist-preparing-devices-travel-through-us-border

### Surveillance Threat Documentation
- **CBP Directive 3340-049B (January 2026)**: cbp.gov/sites/default/files/2026-01/cbp_directive_3340-049b_jan_2026_508.pdf — Current CBP border device search policy
- **EFF — Third Circuit Border Search Brief (March 2026)**: eff.org/deeplinks/2026/03/eff-third-circuit-electronic-device-searches-border-require-warrant
- **Brennan Center — Section 702 Resource Page 2026**: brennancenter.org/our-work/research-reports/section-702-foreign-intelligence-surveillance-act-fisa-2026-resource-page
- **ODNI — NSL Transparency Report CY2024**: dni.gov/index.php/newsroom/reports-publications/reports-publications-2025/4071-astr-cy24
- **EFF — National Security Letters**: eff.org/issues/national-security-letters

### Legal Citations
- **Border search exception authority**: *United States v. Flores-Montano*, 541 U.S. 149 (2004)
- **CBP advanced search policy**: CBP Directive 3340-049B (January 2026)
- **Section 702 FISA (PRISM authority)**: 50 U.S.C. § 1881a; Reforming Intelligence and Securing America Act (RISAA), Pub. L. No. 118-49 (2024)
- **NSL authority**: 18 U.S.C. § 2709, 12 U.S.C. § 3414, 15 U.S.C. § 1681u
- **New York shield law (absolute privilege)**: New York Civil Rights Law § 79-h
- **California shield law (absolute privilege)**: California Evidence Code § 1070
- **PRESS Act (proposed federal shield law, not enacted)**: S.2074/H.R. 4481, 119th Congress
- **First Amendment reporter's privilege**: *Branzburg v. Hayes*, 408 U.S. 665 (1972) (qualified privilege recognized in dissent and in subsequent circuit decisions)

---

## Summary Checklist

**Tier 1 — All journalists doing sensitive reporting**:
- [ ] Travel device protocol completed before each international trip (Signal deregistered, accounts logged out, documents removed)
- [ ] Dedicated GrapheneOS source communication device set up with VoIP number
- [ ] Signal on dedicated device: disappearing messages configured, phone number privacy set to Nobody, registration lock enabled
- [ ] Safety numbers verified with all active sources on dedicated device
- [ ] SecureDrop assessment completed (organization running it, or escalated to leadership)
- [ ] Press freedom counsel identified for subpoena response

**Tier 2 — Investigative reporters with foreign sources or national security coverage**:
- [ ] ProtonMail established for sensitive editorial communication with editor and team
- [ ] Investigation documents migrated from PRISM-reachable cloud storage to ProtonDrive or Cryptomator-encrypted storage
- [ ] NSL risk reviewed with legal counsel
- [ ] Team safety numbers verified with all investigation team members
- [ ] CBP and FBI FOIA requests filed if prior law enforcement inquiry is suspected

**Tier 3 — Reporters under active legal threat or international correspondents**:
- [ ] Three-device compartmentalization architecture implemented (personal / professional / source)
- [ ] Tails OS USB prepared for sensitive document handling
- [ ] International SIM strategy in place for international reporting trips
- [ ] Individual press freedom counsel retained (independent of organizational counsel)
- [ ] Deepfake provenance documentation practice established for video presence

---

**Legal notice**: This playbook is not legal advice and does not substitute for legal counsel to the news organization or to individual journalists. The shield law landscape, Section 702 authorization status, and CBP directive scope are subject to rapid change in 2026. All citations are accurate as of May 6, 2026. Consult with RCFP or qualified press freedom counsel for organization-specific legal guidance.

**Version**: 1.0
**Last updated**: May 6, 2026
**Next review**: July 26, 2026 (aligned with corpus quarterly review; Section 702 authorization status should be verified at that point)
**Cross-references**: threat-model.md, opsec-playbook.md, implementation-guide.md, palantir-threat-model.md, encrypted-messaging-implementation-guide.md, activist-organizing-playbook.md (Part 4: physical countermeasures), whistleblower-playbook.md (Part 3: SecureDrop receiving-side), PHASE_2_SEQUENCING_STRATEGY.md Sections 1.2, 1.3, 2.1, 2.5, 3.6
