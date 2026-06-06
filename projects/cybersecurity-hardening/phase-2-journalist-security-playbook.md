---
title: "Journalist Security Playbook: Source Protection, Device Hardening, and Counter-Surveillance for Reporters"
project: cybersecurity-hardening
created: 2026-05-07
status: production-ready
phase: Phase 2
version: 1.1
depends_on:
  - threat-model.md
  - opsec-playbook.md
  - implementation-guide.md
  - PHASE_2_SEQUENCING_STRATEGY.md
  - THREAT_ENVIRONMENT_Q2_2026_UPDATE.md
  - OPSEC_PLAYBOOK_Q2_2026_PATCHES.md
confidence: high — grounded in confirmed CBP device search statistics, FISA Section 702 documented FBI abuses, Freedom of the Press Foundation 2026 digital security checklist, SecureDrop 2025 annual review, CPJ 2025-2026 press freedom deterioration reporting, Committee to Protect Journalists border-crossing incidents, EFF journalist-specific security guidance; updated June 6, 2026 with DOJ guideline rescission (RCFP analysis, FPF, CPJ), FISA 702 Senate June 5 vote (Roll Call, CBS News), Cellebrite Spring 2026 release (Cellebrite.com, Forensic Focus), and Clearview AI field deployment (Biometric Update, contract records)
audience: Investigative reporters, documentary filmmakers, photojournalists, freelancers with sensitive sources, news organization IT/security teams, journalism school security trainers
word_count: ~4,500
last_updated: 2026-06-06
changelog: v1.1 — Q2 2026 threat integration (5 patches): Section 1.4 rewrite (DOJ guideline rescission + rapid escalation protocol); Section 1.2 FISA 702 June 6 Senate failure; Section 2.1 new (Clearview AI field threat); Section 3.3 new (Cellebrite Safeguard Mode); Section 4.3 FISA status correction
---

# Journalist Security Playbook

**For journalism educators and newsroom security teams**: This guide addresses the specific threat environment facing journalists and sources in the United States as of June 2026. Version 1.1 integrates five Q2 2026 threat patches: DOJ journalist protection guideline rescission (active since April 2025, first activations May–June 2026), FISA 702 legislative crisis (Senate vote failure June 5, 2026), Cellebrite Safeguard Mode (Spring 2026 release), Clearview AI live field identification threat, and FISA Section 4.3 status correction. The threat is qualitatively different from what it was four years ago: CBP device searches at U.S. border crossings have increased, the FBI has conducted documented warrantless backdoor searches of Section 702-acquired communications databases that include journalist queries, and the CPJ's Emergencies team conducted 26 journalist safety training sessions in a single 11-month window — a record pace reflecting a documented deterioration in press freedom conditions.

Three things distinguish this playbook from general security guidance: (1) it maps threats to the specific points in a journalist's workflow where they arise — border crossings, source communication, document receipt, publication, and field reporting; (2) it addresses the absence of a federal shield law and what that concretely means for source protection; and (3) it integrates current operational tools — SecureDrop, Signal, the EFF 2025 journalist security checklist, and CPJ border-crossing protocols — into a workflow rather than an undifferentiated list.

Cross-references to `opsec-playbook.md` and `implementation-guide.md` throughout. If a journalist has completed the core device hardening guide, those measures apply directly to this playbook's device recommendations.

---

## Section 1: Threat Vectors — The Six Specific Risks Journalists Face in 2026

### 1.1 CBP Border Device Searches — No Warrant Required

**The legal foundation**: U.S. Customs and Border Protection has full authority under the "border search exception" to search electronic devices at any international port of entry — airports, land crossings, and sea ports — without a warrant, without probable cause, and without judicial authorization. CBP Directive 3340-049B distinguishes between "basic" searches (manual inspection of visible data) and "advanced" searches (forensic extraction using external equipment). Advanced searches require reasonable suspicion and supervisor approval, but basic searches require nothing. A CBP officer can open your phone, scroll through your contacts, read your messages, and photograph what they see.

**2025–2026 escalation for journalists**: The Committee to Protect Journalists reported a significant deterioration in U.S. press freedom conditions through 2025, with a record 26 safety training sessions conducted in the first 11 months of the year. CJR documented journalists being detained and having devices searched at border zones. The CPJ formally endorsed an updated reporter privacy protection bill in April 2026 to strengthen journalist protections against "unreasonable government searches and seizures in connection with their reporting" — an endorsement that would not be necessary if the current regime were adequate. The EFF and ACLU filed an amicus brief in the Third Circuit seeking a warrant requirement for border device searches; as of May 2026, no such requirement has been imposed.

**What is at risk**: On a journalist's work device at a border crossing: all source contacts, unencrypted message history, notes, draft articles, source documents, and any cloud-synced materials from iCloud, Google Drive, or Dropbox. A CBP officer who conducts an advanced search can copy everything and share it with DHS, FBI, or other agencies.

**The specific risk for sources**: If a journalist's device contains a source's contact information, location, or identifying details, a CBP border search can expose a source to enforcement action without any judicial authorization, and without the journalist's consent. The device-as-source-exposure-vector is the primary border crossing threat.

**Countermeasure**: Section 3 — the clean-device border crossing protocol.

---

### 1.2 FISA Section 702 — Warrantless Access to Journalist-Source Communications

**What it does**: Section 702 of the Foreign Intelligence Surveillance Act authorizes the collection of communications of non-U.S. persons located abroad. The collection is "incidental" — the government targets foreigners, but their communications with U.S. persons (including U.S. journalists) are collected in the same operation. Once collected, the FBI has authority to search ("query") the Section 702 database using terms including the identities of U.S. journalists and their sources.

**Documented abuse**: The Foreign Intelligence Surveillance Court found "persistent and widespread" abuses of Section 702 query authority, specifically including warrantless searches for U.S. journalists, political commentators, and civil society figures. The RCFP documented that an expansion of Section 702 explicitly references the capability to conduct "press queries" — searches targeting journalists by name or identity. The FBI's documented use of Section 702 to warrantlessly search the communications of journalists violates the spirit of the First Amendment reporter's privilege, even where courts have not yet established a clear legal rule.

**Congressional status as of June 6, 2026**: Section 702 expires June 12. The Senate voted 47-52 on June 5 on a motion to proceed to long-term reauthorization — the measure failed. Seven Republicans joined Democrats in opposition, citing both privacy concerns and objections to Trump's appointment of Bill Pulte as acting director of national intelligence. Senate Majority Leader Thune acknowledged "a few days from now, on June 12, that program goes dark" and suggested leadership would attempt another procedural vote before the deadline. A legislative lapse is possible for the first time in this reauthorization cycle.

A reform amendment requiring a warrant for "U.S. person queries" (which would protect journalist queries in the Section 702 database) did not advance in any form. The Government Surveillance Reform Act of 2026 (S.4082), which would have imposed this requirement, has not been enacted. No warrant protection for journalist communications in Section 702 databases has materialized.

**What a lapse does and does not change for journalists**: Even if Section 702 expires on June 12, the Foreign Intelligence Surveillance Court (FISC) issued an administrative order separately extending operational authority for existing Section 702 certifications through 2027. NSA collection of foreign-targeted communications continues under FISC authority regardless of congressional outcome. FBI query authority for new queries of the existing database is the contested legal question if the statute lapses — but this ambiguity does not protect data that has already been collected. For journalists using Signal: no operational change regardless of the June 12 outcome. Signal has zero stored content for the FBI to query, by design.

**Practical implication**: Any journalist who regularly communicates with sources outside the United States — whistleblowers in foreign governments, human rights defenders, diaspora community sources, or any non-U.S. person abroad — should assume those communications may be collected under Section 702 and that their identity may be queried in the database by FBI analysts.

**Countermeasure**: Section 4.3 — Signal with foreign sources, safety number verification protocol.

---

### 1.3 National Security Letters — Compelled Disclosure Without Judicial Authorization

**What they are**: National Security Letters (NSLs) are administrative subpoenas issued by the FBI without any judicial authorization — no warrant, no grand jury, no judge. NSLs can compel telecommunications carriers, internet service providers, and financial institutions to disclose subscriber information, communication records, and financial records. NSLs include a non-disclosure requirement (gag order) that prevents the recipient from telling anyone — including the subject of the NSL — that the letter was received.

**Journalist-specific risk**: If the FBI issues an NSL to a journalist's phone carrier or ISP, the carrier can be compelled to disclose call records, SMS message records, IP address connection logs, and subscriber account details. The journalist will not be notified. The source will not be notified. The disclosure happens silently, without any opportunity for legal challenge before it occurs.

**What NSLs cannot reach**: Encrypted content. An NSL compels metadata records, not the content of encrypted communications. Signal messages are content — they cannot be compelled via NSL from the carrier because the carrier does not have them (Signal's server retains only account creation date and last connection date). But Signal call records (who called whom, when, for how long) are metadata that carriers hold if the calls were made over traditional telephony to Signal contacts' numbers.

**Countermeasure**: Section 4.1 — VoIP-registered Signal; Section 4.4 — metadata minimization.

---

### 1.4 Grand Jury Subpoenas for Source Testimony — DOJ Guidelines Rescinded, Threat Now Active

**CRITICAL UPDATE (June 2026)**: The voluntary DOJ guidelines that constrained journalist subpoenas have been formally rescinded. This threat is no longer theoretical — it is current policy in active use. Read this section as present-tense risk, not contingent risk.

**The federal shield law gap**: As of June 2026, there is no federal shield law protecting journalist-source confidentiality. The PRESS Act (S.2074), which would have created a federal reporter's privilege barring compelled disclosure of source identities, passed the House unanimously but died in the Senate. State shield laws — 49 states and D.C. have some form — do not apply in federal court. A federal grand jury can subpoena a journalist to testify about their sources, and a federal judge can hold the journalist in civil contempt (up to 18 months) for refusing.

**DOJ guidelines — rescinded April 2025**: Department of Justice guidelines (28 C.F.R. § 50.10) previously limited when federal prosecutors could subpoena journalists and required Attorney General approval. In April 2025, Attorney General Pam Bondi issued a memorandum formally revoking the Biden-era version of those guidelines. The previous prohibition on using subpoenas, court orders, or search warrants against journalists who possess and publish classified information obtained in newsgathering — with the presumption against journalist subpoenas — is no longer DOJ policy. Prosecutors are no longer required to exhaust alternatives before subpoenaing journalist records, and no special AG approval threshold applies.

**2026 documented activations — the threat is operational**:

*January 2026 — Washington Post reporter Hannah Natanson*: The FBI executed a search warrant at Natanson's home in connection with a classified information investigation of a government contractor. Agents compelled Face ID unlock of her devices. This is the first documented forced biometric journalist device search under the revised guidelines.

*May 2026 — Wall Street Journal, Iran war coverage*: DOJ issued grand jury subpoenas to WSJ reporters for source records related to reporting on the U.S.-Israel conflict in Iran. President Trump personally directed acting AG Todd Blanche to pursue the investigation, providing a stack of news articles labeled "treason" in a handwritten note. DOJ stated the subpoenas target leakers rather than the journalists themselves — but identifying leakers requires accessing journalist records. The Committee to Protect Journalists condemned the subpoenas on May 26, 2026.

**When the risk is highest**: Grand jury subpoenas for source testimony are most likely when a journalist publishes classified information or information from a government leak. Under the Bondi framework, any leak-adjacent reporting involving national security topics carries active subpoena risk. The government can and does access journalist phone carrier records, email metadata, and anything held by a third party (carrier, ISP, Google, Microsoft) without prior notice to the journalist.

**Rapid escalation protocol — what to do if you receive legal process**:

If you receive a subpoena, search warrant, or any legal process targeting your source communications or device contents:

1. **Do not comply or respond before speaking to counsel.** A subpoena is not a court order requiring immediate compliance. You have time to seek legal advice before any response is due.
2. **Call RCFP's 24/7 legal hotline immediately**: Reporters Committee for Freedom of the Press — 1-800-336-4243 or rcfp.org. They provide free legal referrals and direct representation in many cases.
3. **Contact Freedom of the Press Foundation**: freedom.press — they coordinate with media law attorneys and can advise on technical protective measures that remain legally defensible post-subpoena.
4. **Notify your newsroom's legal counsel before anyone else at your organization.** Do not discuss the subpoena's contents with colleagues until your attorney advises on confidentiality scope.
5. **Do not delete or alter records.** Once you receive legal process, deletion of potentially responsive records creates obstruction exposure. Consult your attorney before taking any action with devices or accounts referenced in the subpoena.
6. **Document your devices' current state before any CBP or FBI contact.** Take notes on what is on each device at the time of any encounter — this creates a baseline for challenging claims about what was extracted.

**Legal aid contacts for journalists facing legal process**:
- Reporters Committee for Freedom of the Press: rcfp.org / 1-800-336-4243 (24/7 hotline)
- Freedom of the Press Foundation (digital security + legal coordination): freedom.press
- Committee to Protect Journalists Emergency Line: cpj.org/emergency
- Media law counsel referral via SPJ: spj.org (Society of Professional Journalists)
- ACLU First Amendment Project (for First Amendment challenges to compelled testimony): aclu.org

**Metadata minimization during subpoena response**: If you are under active legal scrutiny, metadata minimization becomes legally constrained — consult your attorney before deleting anything. However, for communications that postdate a subpoena, the following practices remain available and legally defensible:
- Continue using Signal for all new source communications (Signal produces only account creation date and last connection date in response to legal process — message content does not exist on Signal's servers to be produced)
- Do not initiate new source contacts via phone carrier calls, SMS, or email platforms that retain logs
- Receive all new source documents via SecureDrop, not email (SecureDrop retains no metadata linking submissions to sources or journalists)
- For in-person source meetings during active legal proceedings: leave all devices at home or power them off before leaving; do not bring any device that has been near your sources

**Countermeasure**: The most durable source protection is operational, not legal — the "can't testify about what you don't know" principle. A journalist who genuinely does not know their source's identity (because the source used SecureDrop anonymously) cannot be compelled to reveal it. See Section 5 for legal framework; Section 6.1 for legal support resources.

---

### 1.5 PRISM and Upstream Collection — Newsroom Email and Cloud Storage

**What it is**: PRISM (operated under Section 702) compels major internet companies — Google, Microsoft, Apple, Meta, Yahoo — to provide communications content for targeted non-U.S. persons. "Upstream" collection captures communications in transit on the internet backbone. Together, they mean that a journalist's email communications with foreign sources, newsroom Google Workspace or Microsoft 365 accounts, and cloud-stored documents may be collected if the journalist communicates with any Section 702 target.

**Specific risk for newsrooms**: Most newsrooms use Google Workspace or Microsoft 365 for email and document storage. These platforms are PRISM providers. If a newsroom employee corresponds with a foreign source who is a Section 702 target, those emails are collected. The source's identity is in the collected communication. The collection is automatic — it does not require a decision by any FBI agent to target the journalist specifically.

**Countermeasure**: End-to-end encrypted communications for all sensitive source contact (Signal, SecureDrop). Source-related documents not stored in cloud services accessible to PRISM providers.

---

### 1.6 Metadata and Operational Security Gaps — The Pattern-of-Life Problem

**The threat that technical encryption does not address**: Even if the content of journalist-source communications is perfectly encrypted, metadata — who contacted whom, when, from where, for how long, through what service — creates a pattern-of-life profile that can identify sources. The government does not need to decrypt Signal messages to know that a journalist connected to a particular government agency's IP address at the same time a classified document was transmitted. Correlation of journalist metadata with agency metadata is a documented investigation technique.

**Specific metadata vectors**: Phone carrier call records; Signal account-registration phone numbers (which tie a Signal account to a real phone identity); IP addresses from Signal, email, or SecureDrop connections; location data generated by devices present in the same area as sources; and credit card records showing travel that correlates with source contact events.

**Countermeasure**: Section 4.4 — metadata minimization protocol; Section 3.4 — financial operational security.

---

## Section 2: Role-Specific Threat Mapping

| Journalist Type | Primary Threat | Secondary Threat | Highest-Priority Action |
|---|---|---|---|
| Investigative reporter (government) | NSL metadata disclosure, PRISM email collection | Grand jury subpoena | SecureDrop + VoIP Signal registration + source need-to-know principle |
| Foreign-focused reporter | FISA Section 702 warrantless queries | NSL carrier records | Signal safety number verification; foreign source communication only on dedicated device |
| Field reporter / photojournalist | CBP device search (border), Mobile Fortify (protest field reporting), Clearview AI facial ID from byline photos | ALPR if covering enforcement | Clean travel device; Tier 2 physical measures from activist playbook for enforcement event coverage; see Section 2.1 for Clearview AI countermeasures |
| Documentary filmmaker | Evidence/footage on device; CBP search; subpoena for interview footage | Grand jury for outtakes | Encrypted external drives not transported with device; footage uploaded before returning to U.S. |
| Freelancer | All of the above + personal device used for everything | No institutional legal support | Account-device separation; personal and source devices never the same |
| News organization security team | Organizational email in PRISM pipeline; newsroom network intrusion | Staff device security gaps | Mandate SecureDrop for document receipt; newsroom Signal policy; Tor for all source comms |

### 2.1 Clearview AI — Live Facial Recognition Threat for Field Reporters (Q2 2026)

**New threat as of June 2026**: Clearview AI's facial recognition database — now containing 50+ billion images scraped from the internet — is confirmed operational under active contracts with ICE Homeland Security Investigations ($9.2M), CBP ($225,000, signed February 11, 2026), FBI, and U.S. Marshals. Unlike the DHS HART database (which requires prior government booking or biometric enrollment), Clearview draws from publicly available internet photos. This means a journalist's published byline photo, press conference appearance, conference badge photo, or any public social media image may already be in Clearview's index.

**Why this is qualitatively different for journalists**: Most journalists covering enforcement operations or protests do not expect to be personally identified through government databases. The standard risk model assumed identification required prior arrest or government enrollment. Clearview breaks this assumption. Any journalist with a public digital presence — which is nearly all journalists — has images in Clearview's likely search index.

**The protest and field reporting scenario**: ICE and FBI agents are confirmed using Clearview AI at enforcement operations and protest events (February 2026 Biometric Update reporting, confirmed by current and former DHS officials). A photojournalist or video journalist working enforcement coverage or a protest can be identified through Clearview from partial face images, combined with photo context available from their public internet presence, even while wearing a press credential that does not visibly state their name.

**Countermeasures for field reporters at enforcement events**:
- Use a different appearance from your published byline photo where feasible — especially hairstyle and glasses/no-glasses, which are low-cost changes that meaningfully affect facial recognition matching
- Cover distinctive facial features (visible tattoos, distinctive piercings) that appear in your indexed public photos
- Do not wear press lanyard or credential in enforcement-zone surveillance camera range if you are working a story where your personal identification creates source exposure risk
- Cover the lower half of your face; Clearview's ear and side-profile training data is less extensive than full-face frontal image data
- Note that these measures reduce new-match confidence but do not guarantee non-identification from prior indexed images — consider them risk reduction, not elimination

**What cannot be undone**: Images already scraped and indexed by Clearview cannot be removed from its database through any available opt-out mechanism. Future exposure reduction is the only available control: review public social media privacy settings so new photos are not publicly accessible; communicate removal requests to publication photo editors where byline photos can be updated or made less prominent.

**Source**: Biometric Update (February 2026); CBP contract records; ICE HSI contract records; Section 1.3c of THREAT_ENVIRONMENT_Q2_2026_UPDATE.md.

---

## Section 3: Border Crossing Protocol — The Clean-Device Standard

### 3.1 The Clean Travel Device

Every journalist crossing an international border should cross with a travel device that is clean: no source contacts, no Signal message history, no source documents, no email accounts with sensitive correspondence, no active cloud-sync of sensitive materials.

**How to implement a clean travel device**:
1. Obtain a dedicated travel device (a low-cost iPhone or Android that is not your primary work device — or borrow a loaner device from your newsroom's security team if available)
2. Factory reset the device before each trip
3. Do not log into your primary email account on the travel device
4. Do not install Signal with your primary number; if you need Signal for travel communication, use a temporary VoIP number
5. Do not sync cloud storage containing source materials to the travel device
6. If you need travel contact information: write it on paper, not in your phone

**For the primary work device**: Before travel, log out of all accounts, remove Signal from the device, and leave the device at home or with a trusted colleague. The device that does not cross the border cannot be searched at the border.

### 3.2 If CBP Demands Device Access

1. **Do not voluntarily unlock your device.** CBP can ask; you are not required to comply with a basic search. For advanced searches (requiring reasonable suspicion and supervisor approval), refusal is legally available but may result in device seizure and may affect your entry if you are a non-U.S. person.
2. **State your profession.** CBP Directive 3340-049B states that "work related information carried by journalists shall be handled in accordance with any applicable federal law and CBP policy." Asserting your journalist status does not legally protect you, but it creates a record of the encounter and may trigger additional CBP review before an advanced search proceeds.
3. **Document everything.** Note the officer's name and badge number, the time and location, the specific demands made, and whether your device was physically removed from your presence. Report the incident to CPJ (cpj.org/emergency) and your newsroom's legal counsel immediately after clearing customs.
4. **If your device is seized**: Contact your newsroom's legal counsel immediately. If you are a freelancer without legal support, contact the Reporters Committee for Freedom of the Press (rcfp.org) or CPJ. Device seizures for forensic analysis require additional legal justification and create a paper trail that your counsel can challenge.

### 3.3 Cellebrite Safeguard Mode — Why Power Off Is Now More Critical Than a Locked Screen

**Q2 2026 update — new forensic threat**: Cellebrite's Spring 2026 release (April 2026) introduced a capability called "Safeguard Mode" that materially changes the threat profile for journalist devices at border crossings and law enforcement encounters.

**What Safeguard Mode does**: Prior to Safeguard Mode, an iOS device in AFU (After First Unlock) state would automatically reboot after 72 hours of inactivity, returning the device to BFU (Before First Unlock) state — a much more protected state where Cellebrite's extraction capability is substantially limited. Safeguard Mode "mitigates the impact of iOS inactivity reboot timers by preserving access to a device" after it has been physically secured. If an agent gains AFU access to a device (i.e., the device is unlocked or recently unlocked when seized), they can place it in Safeguard Mode and extract it later without losing AFU access to the 72-hour reboot.

**What this means for journalists**: A device that has been unlocked — including one that is merely screen-locked rather than powered off — is in AFU state. A screen lock alone is no longer sufficient protection if a device is seized by law enforcement with access to Cellebrite. An agent can preserve AFU access indefinitely using Safeguard Mode and conduct full extraction later.

**The countermeasure that remains effective**: Power off the device completely before any anticipated seizure event. A fully powered-off device enters BFU (Before First Unlock) state. Cellebrite cannot establish the AFU access that Safeguard Mode requires against a powered-off device. Cellebrite's Spring 2026 release confirmed AFU extraction capability for iOS 26 and iPhone 17 series — but BFU extraction capability for current iOS versions remains substantially more limited.

**Additional iOS 26 coverage confirmed**: Cellebrite's Spring 2026 release achieves full AFU-state extraction for iPhones running iOS 26.4 and earlier, including iPhone 17 series, with keychain export of stored credentials, tokens, and application artifacts.

**Practical rule**: Before any international border crossing, protest coverage, or any encounter where device seizure is possible — power off the device completely, not just lock the screen. The existing clean-device protocol (Section 3.1) addresses what should be on the device; this section addresses the physical state of the device at the moment of any seizure risk.

### 3.4 Financial Operational Security at Borders

Credit card and payment records document travel in detail that can be used to establish source contact patterns. If a journalist travels to meet a source, payment records create evidence of the trip independent of the journalist's testimony. For travel related to sensitive investigations:
- Pay for travel with cash or a prepaid card where feasible
- Do not use a loyalty program tied to your identity for the trip
- Use a hotel rate paid in cash at check-in

---

## Section 4: Source Protection — Operational Framework

### 4.1 SecureDrop — The Primary Secure Channel for Document Submission

SecureDrop is operated by the Freedom of the Press Foundation and is the standard for anonymous document submission at major newsrooms. As of 2026, SecureDrop is operational at 65+ organizations including the New York Times, Washington Post, The Guardian, ProPublica, The Intercept, Los Angeles Times, and AP.

**How SecureDrop protects sources**:
- Sources access the newsroom's SecureDrop instance through a Tor hidden service address (.onion URL) — the source's IP address is not visible to the journalist or to SecureDrop servers
- Submissions are encrypted with the newsroom's GPG key before being received — even Freedom of the Press Foundation cannot read them
- Sources receive a randomly generated codename that allows follow-up communication without revealing identity
- No JavaScript execution on submission; no tracking pixels; no analytics

**2025–2026 updates**: The SecureDrop Workstation officially left pilot stage with improvements including driverless printing support. The SecureDrop app (journalist-facing) was rewritten and is pending a security audit before release in early 2026. The SecureDrop Protocol (new end-to-end encrypted messaging standard) is under active development and will close the current gap where journalist-to-source replies are network-layer encrypted but not end-to-end encrypted.

**If your newsroom does not have SecureDrop**: Freedom of the Press Foundation provides setup assistance and hosting support. Contact fpf.org/securedrop. Setup time is approximately two weeks. This is the correct standard for any newsroom that receives document leaks.

**For sources before SecureDrop is available at your newsroom**: The Signal Sealed Sender option reduces metadata exposure. Briar (briarproject.org) allows Tor-routed encrypted messaging without phone number registration. For highest-risk sources: the source should access a library computer, download Tor Browser from torproject.org, and access the newsroom's SecureDrop address from there.

### 4.2 Signal — The Communication Standard, Correctly Used

Signal is the standard for journalist-source voice and messaging. Its server-side security is genuine: Signal retains only account creation date and last connection date in response to legal process. No message content, no contacts, no call records. But "Signal is secure" requires four conditions:

1. **Signal must be registered with a VoIP number, not a carrier SIM.** If your Signal account is registered with your real phone number, that number is a carrier record that can be obtained via NSL. Use a VoIP service (MySudo at mysudo.com, JMP.chat at jmp.chat, or TextNow) to obtain a number not associated with your physical SIM card. Register Signal with the VoIP number only.

2. **Safety numbers must be verified out-of-band.** Signal's safety number system detects key changes that could indicate a man-in-the-middle attack (including government-substituted keys). For each sensitive source, verify safety numbers in person or via a second secure channel. Do not assume that the person you are communicating with on Signal is who they claim to be without out-of-band verification.

3. **Disappearing messages must be enabled.** Set a disappearing message timer for all sensitive conversations (recommended: 24 hours or 1 week, depending on your need to retain source communication for legal defense). Messages that do not exist on the device cannot be compelled or extracted.

4. **Signal note-sync must be disabled.** Signal has a feature that syncs notes to Signal servers. For journalists, this is a potential collection point. Disable it in Signal Settings > Privacy > Linked Devices.

### 4.3 Foreign Source Communications — Section 702 Mitigation

**FISA status correction (June 6, 2026)**: Section 702 expires June 12, 2026. The Senate failed to advance reauthorization on June 5 (47-52 vote). Even if Section 702 lapses, the FISC issued an order extending existing certifications through 2027 — NSA collection of foreign-targeted communications continues under FISC authority regardless of congressional outcome. No warrant protection for journalist communications has been enacted. The practical guidance below is unchanged regardless of the June 12 outcome: Signal users face zero surveillance change because Signal has no stored content for the FBI to query.

For sources outside the United States:
- Signal over a mobile data connection, not WiFi (WiFi IP addresses can be legally associated with a location via ISP records; mobile data uses carrier IP addresses that are more difficult to associate with specific individuals)
- Safety number verification is required before trusting any foreign source's Signal account — government actors have substituted keys on foreign accounts in documented cases
- Do not conduct sensitive communications via email, WhatsApp (which is a PRISM provider via Meta), or any platform that discloses data under Section 702 compulsion
- For document receipt: SecureDrop, not email

### 4.4 Metadata Minimization Protocol

Even perfect encryption leaves metadata. Reduce it:
- **Phone-off protocol for sensitive meetings**: When physically meeting a source, leave your phone at home or power it off and Faraday-bag it. Your phone's location history correlates you with the source's known location.
- **Tor Browser for research**: Any research related to your story — searches for public records, review of documents, reading about the subject — leaves browser history and IP records. Use Tor Browser for all research related to sensitive stories.
- **Dedicated journalist device for source communications**: Source communications should happen on a device that has never been associated with your primary identity. A dedicated GrapheneOS device registered with a VoIP number and accessed only through non-home networks creates a separation between your personal digital identity and your source communication identity.

---

## Section 5: Legal Framework — What Protection Actually Exists

### 5.1 The Federal Shield Law Gap

There is no federal shield law as of May 2026. The PRESS Act's unanimous House passage and Senate failure represents the current ceiling of federal legislative protection. In federal court proceedings — including grand jury investigations, federal civil litigation, and federal criminal cases — a journalist can be compelled to testify about sources, with contempt sanctions (up to 18 months civil contempt, potentially criminal contempt) for refusal.

**What this means in practice**:
- In federal investigations of classified information leaks, the government can and does subpoena journalists
- The safest source protection strategy is one that does not depend on the journalist's willingness to go to jail: use SecureDrop, so you do not know the source's identity; enable disappearing messages, so the message history does not exist; use Signal with a VoIP number, so the metadata trail does not lead to a real phone

**The "can't testify about what you don't know" principle**: The most durable source protection is operational, not legal. A journalist who genuinely does not know their source's identity — because the source used SecureDrop anonymously — cannot reveal it under any legal compulsion.

### 5.2 State Shield Laws

49 states and D.C. have some form of journalist's privilege. These protect against state court compulsion and, in some circumstances, grand jury proceedings initiated in state court. California, New York, Connecticut, and Illinois have relatively strong shield laws. Texas has a qualified privilege. State protections do not apply in federal proceedings.

**Practical utility**: State shield laws protect most working journalists in most ordinary legal contexts (state civil litigation, state criminal proceedings, state legislative demands). They do not protect against federal grand jury subpoenas in leak investigations, which is where the risk is highest.

### 5.3 The DOJ Journalist Subpoena Guidelines

28 C.F.R. § 50.10 requires the Attorney General to approve subpoenas to journalists in most circumstances and establishes procedural requirements (notice, negotiation, exhaustion of alternatives) before a journalist subpoena may issue. Under the Biden-era updates to these guidelines (2021), journalists are entitled to advance notice of subpoenas and an opportunity to challenge them before compliance. These are department policy, not law, and can be changed by executive action.

**Practical note**: The guidelines provide meaningful protection in the current administration's cases but can be rescinded or narrowed by any future AG. They are not reliable long-term structural protection.

---

## Section 6: Implementation Checklists

### Checklist A: Before Any International Travel

- [ ] Identify which device you will cross the border with; factory reset it if needed
- [ ] Log out of all email accounts on travel device
- [ ] Remove Signal from the travel device or unlink it from your primary account
- [ ] Upload or delete any source-related documents from the travel device
- [ ] Log out of all cloud storage with sensitive materials (Google Drive, Dropbox, iCloud)
- [ ] Write emergency contact numbers on paper — not in phone
- [ ] Brief your editor or news director that you are crossing with a clean device; they should know in case you are detained
- [ ] Have the Committee to Protect Journalists emergency contact (cpj.org/emergency) and RCFP (rcfp.org) saved in paper form

### Checklist B: Before Initial Contact With a Sensitive Source

- [ ] Has your newsroom set up SecureDrop? If not, refer the source to a newsroom that has it until yours does
- [ ] Is your Signal registered with a VoIP number, not your carrier SIM?
- [ ] Have you verified Signal safety numbers out-of-band with this source?
- [ ] Have you set a disappearing message timer for this conversation?
- [ ] Have you disabled Signal note-sync (Settings > Privacy > Linked Devices)?
- [ ] For in-person meetings: phone powered off and Faraday-bagged, not just silenced

### Checklist C: Day-Of Field Reporting at Enforcement Events or Protests

- [ ] Bring the travel/reporting device (not primary device), or apply Tier 2 activist playbook measures
- [ ] Enable auto-reboot (GrapheneOS: 18-hour auto-reboot in BFU/AFU distinction context)
- [ ] Wear press credential visibly; note that this is not legal protection against Mobile Fortify biometric scanning
- [ ] Know where to upload footage before returning home (Signal Note-to-Self or encrypted cloud backup)
- [ ] Upload all documentation immediately after leaving the field — before any encounter with law enforcement where device seizure is possible
- [ ] NLG number or local legal observer contact written on arm

### Checklist D: Ongoing Newsroom Security Practices

- [ ] Monthly: Review which staff have SecureDrop access and whether access is appropriately limited
- [ ] Quarterly: Verify that all staff Signal accounts are registered with VoIP numbers, not carrier SIMs
- [ ] After each major story involving sensitive sources: delete source communications per agreed retention schedule
- [ ] Before any legal proceeding involving source protection: retain First Amendment or media law counsel (Reporters Committee for Freedom of the Press provides referrals — rcfp.org)

---

## Section 7: Escalation Matrix

### Level 1: Standard Precautions (All Journalists)

Signal registered with VoIP number, disappearing messages enabled, SecureDrop for document receipt, Tor Browser for sensitive research. Clean-device protocol for all international travel. EFF journalist security checklist reviewed annually.

### Level 2: Elevated Risk (Covering Government Leak Stories, Classified Material)

All Level 1 measures, plus: dedicated source-communication device (GrapheneOS, VoIP Signal only), in-person safety number verification for all active sources, no source information stored in newsroom cloud infrastructure, legal counsel engaged before publication (not after subpoena arrives), phone-off protocol for all source meetings.

### Level 3: Under Active Legal Scrutiny (Subpoena Received or Expected, Grand Jury Investigation)

All Level 2 measures, plus: First Amendment media law attorney retained proactively; review and deletion of non-essential source communication records (consult counsel on legal hold implications first); assessment of what the journalist knows about source identity and whether the "I don't know" protection is available; coordination with newsroom legal team, Freedom of the Press Foundation, and RCFP.

---

## Section 8: Tools and Resources

### Secure Communication
- **SecureDrop**: securedrop.org — document submission; 65+ newsrooms
- **Signal**: signal.org — encrypted messaging; use with VoIP number
- **Tor Browser**: torproject.org — anonymous research
- **Briar**: briarproject.org — Tor-routed mesh messenger, no phone number required
- **MySudo**: mysudo.com — VoIP number for Signal registration
- **JMP.chat**: jmp.chat — XMPP-based VoIP number

### Device Security
- **GrapheneOS**: grapheneos.org — hardened Android (Pixel 6–9)
- **Mullvad VPN**: mullvad.net — no-logs VPN; cash payment accepted
- **VeraCrypt**: veracrypt.fr — encrypted containers for source documents on laptop

### Legal Support
- **Reporters Committee for Freedom of the Press**: rcfp.org — legal defense resources, 24/7 hotline
- **Freedom of the Press Foundation**: freedom.press — SecureDrop setup, journalist digital security training
- **Committee to Protect Journalists**: cpj.org/emergency — emergency support for journalists under threat
- **National Lawyers Guild**: nlg.org — for journalists covering protests who are arrested

### Training and Current Guidance
- **EFF 2025 Journalist Security Checklist**: eff.org/deeplinks/2025/06/journalist-security-checklist-preparing-devices-travel-through-us-border
- **Freedom of the Press Foundation 2026 Digital Security Checklist**: freedom.press/digisec/blog/journalists-digital-security-checklist/
- **CPJ Digital Safety**: cpj.org/safety

---

## Summary: Five Principles That Matter Most

1. **The clean device at every border crossing** — your primary device should not cross international borders with source contacts or materials on it. A factory-reset travel device that gets searched by CBP reveals nothing.

2. **SecureDrop, not email, for document receipt** — a source who submits through SecureDrop over Tor is anonymous to you, to your newsroom, and to law enforcement subpoena. A source who emails you is none of those things.

3. **Signal registered with a VoIP number, not your SIM** — the NSL-accessible data is carrier records. A VoIP number registered to no one's physical identity removes the carrier-accessible metadata anchor.

4. **Verify safety numbers in person** — Signal's encryption is only as strong as the certainty that you are communicating with the right person. Safety number verification defeats government key substitution.

5. **Know what you don't know** — the "can't testify about what you don't know" principle is the most durable source protection. SecureDrop anonymity, disappearing messages, and not retaining source identification documents means that no legal compulsion can extract what does not exist.

---

**Version**: 1.1 (Q2 2026 threat integration)
**Created**: May 7, 2026
**Last updated**: June 6, 2026
**Next scheduled review**: July 26, 2026 (quarterly corpus review)
**Cross-references**: `opsec-playbook.md`, `implementation-guide.md`, `threat-model.md`, `phase-2-activist-organizing-security-playbook.md` (Sections 4–5 directly applicable for field reporting at protests), `phase-2-whistleblowing-playbook.md` (source-recipient perspective), `THREAT_ENVIRONMENT_Q2_2026_UPDATE.md` (source for v1.1 patches)

---

## Sources

- [EFF — Journalist Security Checklist for Border Travel, 2025](https://www.eff.org/deeplinks/2025/06/journalist-security-checklist-preparing-devices-travel-through-us-border)
- [Freedom of the Press Foundation — 2026 Journalist Digital Security Checklist](https://freedom.press/digisec/blog/journalists-digital-security-checklist/)
- [CPJ — Calls for US press freedom reforms against warrantless surveillance, April 2026](https://cpj.org/2026/04/cpj-urges-us-lawmakers-to-enact-reforms-to-protect-press-freedom-from-warrantless-surveillance/)
- [CPJ — Endorses updated reporter privacy protection bill, April 2026](https://cpj.org/2026/04/cpj-endorses-updated-reporter-privacy-protection-bill-against-unreasonable-government-searches-and-seizures/)
- [CPJ — Record demand for safety training, December 2025](https://cpj.org/2025/12/cpj-acceleration-of-us-press-freedom-concerns-spike-demand-for-safety-training/)
- [RCFP — Section 702 expansion and press queries](https://www.rcfp.org/section-702-press-queries/)
- [Brennan Center — Section 702 FISA 2026 resource page](https://www.brennancenter.org/our-work/research-reports/section-702-foreign-intelligence-surveillance-act-fisa-2026-resource-page)
- [NPR — What to know about Section 702 surveillance, April 2026](https://www.npr.org/2026/04/14/nx-s1-5768270/what-to-know-about-section-702-surveillance)
- [NPR — Congress extends FISA 702 for 45 days, April 2026](https://www.npr.org/2026/04/29/g-s1-119094/congress-fisa-702)
- [SecureDrop — Looking back at 2025](https://securedrop.org/news/looking-back-at-2025/)
- [Freedom of the Press Foundation — SecureDrop 2025 Year in Review](https://freedom.press/tech/news/securedrop-looking-back-at-2025/)
- [CBP — Border Search of Electronic Devices Directive 3340-049B](https://www.cbp.gov/document/directives/cbp-directive-no-3340-049b-border-search-electronic-devices)
- [CDT — Protecting Electronic Devices When Crossing US Borders](https://cdt.org/insights/protecting-electronic-devices-when-crossing-u-s-borders/)
- [EFF — Border Searches overview](https://www.eff.org/issues/border-searches)
- [CJR — Journalists under threat at border zones](https://www.cjr.org/the_media_today/border-ports-entry-threat-press-freedom.php)
- [SPJ — The PRESS Act: What it is and why it matters](https://www.spj.org/the-press-act-what-it-is-and-why-its-important-to-get-it-passed/)
- [ACLU — Jailing journalists: why we need a federal reporter's shield bill](https://www.aclu.org/news/free-speech/jailing-journalists-why-we-need-federal-reporters-shield-bill)
- [PrivacyOn — Privacy Guide for Journalists 2026](https://www.privacyon.com/blog/privacy-guide-for-journalists)

### Q2 2026 Patch Sources (v1.1 additions)

- [RCFP — DOJ rescinds Biden-era protections for press (special analysis)](https://www.rcfp.org/doj-rescinds-news-media-guidelines-analysis/)
- [Freedom of the Press Foundation — Trump DOJ repeals protections for journalist-source confidentiality](https://freedom.press/issues/trump-doj-repeals-protections-for-journalist-source-confidentiality/)
- [Washington Post — Justice Dept. subpoenas Wall Street Journal, May 12, 2026](https://www.washingtonpost.com/national-security/2026/05/12/justice-dept-subpoenas-wall-street-journal-escalating-investigations-into-media-leaks/)
- [CPJ — CPJ condemns Trump's order for DOJ to subpoena journalists](https://cpj.org/2026/05/cpj-condemns-trumps-order-for-doj-to-subpoena-journalists/)
- [The Hill — DOJ subpoenas Wall Street Journal over Iran war leaks](https://thehill.com/homenews/administration/5873861-wall-street-journal-subpoena/)
- [Roll Call — FISA reauthorization stalls in early-morning Senate vote, June 5, 2026](https://rollcall.com/2026/06/05/fisa-reauthorization-stalls-in-early-morning-senate-vote/)
- [CBS News — Senate fails to extend FISA as deadline nears](https://www.cbsnews.com/news/senate-fisa-vote-extension/)
- [Congress.gov — S.4082 Government Surveillance Reform Act of 2026](https://www.congress.gov/bill/119th-congress/senate-bill/4082)
- [Cellebrite — Spring 2026 Release: Digital Forensics Updates](https://cellebrite.com/en/products/launches-releases/spring-release-2026/)
- [Forensic Focus — Inside the Cellebrite Spring 2026 Release](https://www.forensicfocus.com/webinars/inside-the-cellebrite-spring-2026-release/)
- [Biometric Update — ICE, FBI expand facial recognition use to protest investigations, February 2026](https://www.biometricupdate.com/202602/ice-fbi-expand-facial-recognition-use-to-protest-investigations)
- [Biometric Update — ICE expands field biometric identification with $25M iris recognition contract](https://www.biometricupdate.com/202605/ice-expands-field-biometric-identification-with-25m-iris-recognition-contract)
- [Immigration Policy Tracking Project — ICE contracts with Clearview AI](https://immpolicytracking.org/policies/reported-ice-contracts-with-clearview-ai-for-facial-recognition-technology/)
