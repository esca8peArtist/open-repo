---
title: "Phase 2 Threat Integration Checklist — Q2 2026"
project: cybersecurity-hardening
created: 2026-06-06
status: production-ready
version: 1.0
purpose: >
  Maps each new Q2 2026 threat finding to specific Phase 2 playbooks requiring updates,
  with implementation priority (HIGH/MEDIUM/LOW), specific section targets, and
  ready-to-integrate patch language. Use this checklist to update playbooks before
  July 2026 Phase 2 Wave 1 distribution.
source_document: THREAT_ENVIRONMENT_Q2_2026_UPDATE.md (2026-06-06)
prior_verification: PHASE_2_THREAT_VERIFICATION_MAY_2026.md (2026-05-21)
playbooks_in_scope:
  - phase-2-immigration-surveillance-evasion-playbook.md
  - phase-2-activist-organizing-security-playbook.md
  - phase-2-journalist-security-playbook.md
---

# Phase 2 Threat Integration Checklist — Q2 2026

**How to use this document**: Each section below corresponds to one of the three Phase 2 playbooks. For each new threat, the checklist specifies: the section to update, the specific addition needed, and whether it requires new guidance or is an existing guidance reinforcement with updated evidence. Priority ratings:

- **HIGH**: New threat type or material escalation that changes operational recommendations
- **MEDIUM**: Updated evidence for existing recommendations; strengthens existing guidance
- **LOW**: Contextual update; adds factual accuracy without changing recommendations

---

## Playbook 1: Immigration + Surveillance Evasion Playbook

**File**: `phase-2-immigration-surveillance-evasion-playbook.md`
**Current version**: 1.1 (May 7, 2026)

### UPDATE-IMM-01 — Iris Scanning Added to Field Toolkit
**Priority**: HIGH
**Section to update**: Section 1.3 (Mobile Fortify) — expand to cover the full biometric field toolkit
**What to add**: ICE finalized a $25.1M no-bid contract with Bi2 Technologies on May 22, 2026, deploying 1,570+ mobile iris scanners to agents nationwide (contract effective June 1, 2026). The iris scanners access a database of 5M+ booking and arrest records from 47 states. Combined with Mobile Fortify facial recognition, ICE field agents now have a two-stage biometric pipeline: identification at distance (Mobile Fortify/Clearview AI) and identity confirmation at close range (iris scan).

**Practical implication**: Iris scanning requires close-range contact. This changes the checkpoint encounter scenario — agents who cannot confirm facial identification may move to iris scanning as a secondary confirmation step. The countermeasure remains: assert Fifth Amendment right to silence; do not volunteer biometric data; request attorney presence. The legal status of compelled iris scanning in non-arrest encounters is unsettled. Do not consent.

**Patch text for Section 1.3**:
> **UPDATE (June 2026): Iris Scanning Added to Field Toolkit.** On May 22, 2026, ICE finalized a $25.1M contract with Bi2 Technologies for 1,570+ mobile iris scanners, effective June 1, 2026. The scanners access a 5M+ record database from 47 states. ICE agents may use iris scanning as a secondary step when facial identification is uncertain. **Do not consent to iris scanning outside of a formal arrest processing context. Compelled iris scanning in a street or checkpoint encounter without arrest is legally unsettled — assert your right to consult an attorney before submitting to any biometric collection.**

---

### UPDATE-IMM-02 — Clearview AI 50B Image Database Documented
**Priority**: HIGH
**Section to update**: Section 1.3 (Mobile Fortify)
**What to add**: The prior playbook described Mobile Fortify as using the NEC facial recognition engine against the DHS HART database (150M+ records). A parallel layer is now confirmed: ICE Homeland Security Investigations holds a $9.2M Clearview AI contract; Clearview's database contains 50+ billion images scraped from the internet. This gives HSI (which handles non-deportation investigations — labor trafficking, financial crime, organized crime) a far larger facial recognition surface than the DHS HART database alone.

**Why the distinction matters**: ELITE and ImmigrationOS (ERO enforcement) are primarily covered by the NEC/HART stack. Workplace raids, financial investigations, and organized crime investigations by HSI are covered by the Clearview layer. If a client has any connection to an HSI investigation (not just deportation enforcement), Clearview AI's database is in scope. Clearview's internet-scraped database includes profile photos, news photos, protest photos, and any public photo ever posted — sources that are not in HART.

**Patch text for Section 1.3 (addition)**:
> **ICE Clearview AI Contract (HSI, $9.2M)**: Parallel to the Mobile Fortify/HART stack, ICE's Homeland Security Investigations division uses Clearview AI — a database of 50+ billion images scraped from the internet — for investigations beyond deportation operations. If a client is connected to any HSI investigation, any public photo (social media, news coverage, protest photos, community organization website) may be in scope for facial identification. **Countermeasure**: data broker opt-out (removes commercial records), but image scraping cannot be undone for photos already posted publicly. Future public photos should be evaluated against your exposure level — see Section 3 (social media hygiene).

---

### UPDATE-IMM-03 — DOGE SSA Data Expands Immigration Enforcement Pipeline
**Priority**: HIGH
**Section to update**: Section 1.1 (ELITE threat model); add as new subsection 1.6 or add to the Palantir threat model section
**What to add**: DOGE obtained unauthorized access to Social Security Administration data for 300M+ Americans, including immigration status. Court filings (January 2026) confirmed DOGE employees were coordinating with a political advocacy group to match SSA data against state voter rolls. New System of Record Notices (SORNs) expanded data sharing between SSA and other agencies.

**Why this matters for immigration clients**: SSA holds immigration status data, Social Security numbers, wage histories, and home addresses. This data, if incorporated into the ICE enforcement pipeline (which the ELITE system already draws from Medicaid data under a December 2025 data-sharing agreement), would add wage and employment history to the address confidence scoring system. The threat is not that all SSA data is currently in ELITE — it is that the legal and technical pathway to that integration was opened without authorization and is being normalized via SORNs.

**Patch text for new subsection 1.6**:
> **1.6 DOGE — Federal Benefit Data as an Enforcement Pipeline**
> In January 2026, court filings revealed that DOGE employees at the Social Security Administration improperly accessed records for 300M+ Americans — including immigration status, bank account numbers, and wage histories — and coordinated with a political advocacy group to match SSA data against voter rolls. The Trump administration admitted to mishandling the data. A federal court issued a preliminary injunction on June 6, 2026 halting further DOGE access to OPM data.
> **Your exposure**: If you have ever received Social Security benefits, a Social Security number, or wage income reported to SSA, your records were part of the accessed dataset. SSA's immigration status data can identify undocumented individuals in the database.
> **Your countermeasure**: This data cannot be removed from SSA records. The practical countermeasure is to minimize what other data sources (commercial data brokers) contribute to enforcement confidence scores — because the SSA data cannot be deleted, reducing commercial supplement data reduces the combined confidence score.

---

### UPDATE-IMM-04 — Thomson Reuters CLEAR Contract Expiration Note
**Priority**: MEDIUM
**Section to update**: Section 1.1 (ELITE — address confidence scoring, Thomson Reuters subsection)
**What to add**: The LEIDS-5 contract expired May 31, 2026. No confirmed renewal as of June 6, 2026. Thomson Reuters faced significant internal pressure (200+ employee letter) and union shareholder campaigns at the June 10 shareholder vote. However, broader ICE-Thomson Reuters data sharing relationships exist at ~$60M in estimated active contracts. CLEAR opt-out remains a recommended action regardless of contract status.

**Patch text (add to Section 1.1 Thomson Reuters paragraph)**:
> *(June 2026 update: The LEIDS-5 contract expired May 31, 2026. As of June 6, no confirmed renewal has been announced. However, Thomson Reuters maintains multiple DHS/ICE contract vehicles totaling ~$60M. CLEAR opt-out remains a recommended action — removing your records from CLEAR at source protects you regardless of which specific contract vehicle provides access.)*

---

### UPDATE-IMM-05 — DHS Admin Subpoenas Affect Immigration-Adjacent Accounts
**Priority**: MEDIUM
**Section to update**: Section 3 (Social media hygiene) or equivalent
**What to add**: DHS issued hundreds of administrative subpoenas to Google, Meta, Reddit, and Discord to unmask users of anti-ICE accounts. Google, Meta, and Reddit partially complied before legal challenges were filed. The subpoena authority requires no judicial authorization. This threat applies directly to immigrants and advocates who operate anonymous social media accounts posting about ICE activity.

**Patch text (addition to social media section)**:
> **DHS Administrative Subpoenas — Anonymous Account Risk**: DHS has issued hundreds of administrative subpoenas (no court authorization required) to Google, Meta, Reddit, and Discord to unmask anonymous accounts that posted about ICE raids or criticized ICE operations. Google, Meta, and Reddit have partially complied. The ACLU successfully challenged some subpoenas, but disclosures may have already occurred before legal challenge.
> **What this means**: Any account registered with a real email address, phone number, or credit card, or accessed from an IP address connected to your identity, can be unmasked via subpoena. Compliance by the platform is not guaranteed to wait for a legal challenge.
> **Countermeasure**: If you operate accounts posting about ICE activity or immigration enforcement, those accounts must be created and operated with complete separation from your real identity — separate email (ProtonMail, not Gmail), no phone verification, VPN during account creation and every use session, payment via cash or Monero, accessed only from dedicated device not linked to your real identity. See the anonymity guide in this playbook for full protocol.

---

## Playbook 2: Activist Organizing + Protest Security Playbook

**File**: `phase-2-activist-organizing-security-playbook.md`
**Current version**: 1.1 (May 7, 2026)

### UPDATE-ACT-01 — FBI Integration Confirmed at Protests
**Priority**: HIGH
**Section to update**: Section 1.4 (Layer 4 — Mobile Fortify) and/or a new Layer 5 entry for FBI-specific threat
**What to add**: Current and former DHS officials have confirmed that agents at protests in Minneapolis used at least two facial recognition systems simultaneously: Mobile Fortify AND Clearview AI (with the 50B+ image database). FBI agents (not just ICE) are using facial recognition to add individuals to investigative databases from protest footage. The February 2026 class action (Hilton v. Noem, Tincher v. Noem) documents a pattern across at least two states.

**Priority reason**: The prior playbook framed facial recognition at protests as an ICE tool. FBI integration changes the threat actor picture — FBI's investigative authority extends to domestic terrorism investigations, which have a different legal basis and different downstream consequences than immigration enforcement. FBI investigative database placement is not about deportation; it is about federal criminal investigation potential.

**Patch text (addition to Section 1.4)**:
> *(June 2026 update: ICE agents at Minneapolis protests are confirmed using at least two facial recognition systems: Mobile Fortify (NEC/HART) and Clearview AI (50B+ images). FBI agents are independently using facial recognition at protests to add individuals to federal investigative databases. FBI database placement is not immigration enforcement — it creates federal criminal investigation exposure. Two federal class action lawsuits (Hilton v. Noem, Maine; Tincher v. Noem, Minnesota) were filed February 2026 documenting agents scanning observers' faces, photographing plates, following people home, and informing them they are in "domestic terrorist databases." DHS officially denies the existence of a domestic terrorist database.)*

---

### UPDATE-ACT-02 — DHS Admin Subpoenas for Activist Accounts
**Priority**: HIGH
**Section to update**: Section 1.5 (Account unmasking) — expand with current data
**What to add**: Since the playbook was written, DHS withdrew some subpoenas under legal pressure (ACLU challenges), but confirmed partial compliance by Google, Meta, and Reddit. New details: the subpoenas targeted accounts criticizing ICE or posting ICE agent location alerts; Columbia University was targeted to share information about a student protester; a Philadelphia man received a subpoena four hours after emailing a DHS official — two federal agents then appeared at his home.

**The four-hour timeline** is the critical new detail. It establishes that DHS is monitoring and subpoenaing communications in near-real-time, not just investigating historical accounts. The practical implication: there is no grace period to establish anonymity after a communication. Anonymous infrastructure must be in place before any sensitive communication occurs.

**Patch text (addition to Section 1.5)**:
> *(June 2026 update: The scale of DHS administrative subpoenas has grown to hundreds. Google, Meta, and Reddit partially complied. New cases include: a Philadelphia man subpoenaed four hours after emailing a DHS official, with federal agents appearing at his home two weeks later; Columbia University targeted to share data on a student protester. The ACLU successfully challenged some subpoenas, but DHS withdrew them after partial compliance, meaning disclosures may have already occurred. The practical implication: anonymous infrastructure must be established before any communication — there is no retroactive anonymity. Account architecture already established with full separation from real identity is not affected by subpoenas targeting the account's email or phone registration.)*

---

### UPDATE-ACT-03 — DOGE Data Enables Activist Organization Targeting
**Priority**: MEDIUM
**Section to update**: Add to existing Palantir threat section or standalone note in organizational threats section
**What to add**: DOGE's voter roll matching using SSA data specifically targeted political advocacy organizations. Court filings confirm that DOGE was coordinating with "an unidentified political advocacy group" to use federal benefit data to "find evidence of voter fraud and to overturn election results." This is the first documented case of federal benefit database access being used against political advocacy organizations.

**Why it matters for activist organizers**: If your organization appears in any federal benefit database — through staff health insurance (ACA/Medicaid), any payroll connection to SSA records, or grant funding traced to federal programs — your organization's staff may appear as nodes in DOGE-accessible datasets. The relationship-mapping capability documented in the Palantir/IRS section of the prior Q2 update now has a parallel in DOGE's access to SSA.

**Patch text (addition, new note)**:
> **DOGE Federal Data as Organizational Threat**: In January 2026, court filings revealed DOGE employees at SSA coordinating with a political advocacy group to match federal benefit data against voter rolls targeting named political adversaries. If your organization has any staff receiving government benefits, any connection to ACA/Medicaid enrollment, or any payroll information submitted to SSA, your organization's staff may be in DOGE-accessible datasets. This threat cannot be mitigated by operational security practices — it is a structural data exposure. It reinforces the importance of financial separation between organizational and personal financial identities, and consultation with a privacy attorney if your organization is actively targeted.

---

### UPDATE-ACT-04 — ICE Iris Scanning at Enforcement Events
**Priority**: MEDIUM
**Section to update**: Section 1.4 (Layer 4 — Field Biometric Identification)
**What to add**: Iris scanning ($25.1M Bi2 contract, June 1 deployment) adds a close-range biometric confirmation step beyond Mobile Fortify's facial recognition. For protest observers and enforcement monitors who may be approached by ICE agents, this adds a second biometric risk beyond photography.

**Patch text (addition to Section 1.4)**:
> *(June 2026 update: ICE deployed iris scanning capability nationally on June 1, 2026 via a $25.1M Bi2 Technologies contract covering 1,570+ handheld scanners. Close-range iris scanning is a second biometric identification step. If approached by ICE agents, the same principle applies: assert your right not to submit to biometric collection outside a formal arrest processing context and request attorney presence. Legal status of compelled iris scanning in non-arrest encounters is unsettled.)*

---

### UPDATE-ACT-05 — Aerial Surveillance Gait Recognition Trajectory
**Priority**: LOW
**Section to update**: Section 1.2 (Layer 2 — Aerial Surveillance)
**What to add**: The 2026 threat trajectory includes LiDAR-based gait recognition as a complement to aerial drone surveillance. Not currently deployed at US protests, but in development. The practical current-state implication: existing clothing-based masking protocols that defeat facial recognition and mask aerial drone identification by face are still adequate. The long-term (2027+) trajectory adds gait as a defeating condition for current countermeasures.

**Patch text (footnote addition to Section 1.2)**:
> *(Future trajectory note: LiDAR-based gait recognition — which can identify individuals by walking pattern regardless of facial covering or clothing — is in early domestic deployment at border installations. Not currently deployed at US protest sites. This technology, combined with aerial LiDAR drones, would defeat the clothing-based masking countermeasures in Section 4.2. Monitor for deployment announcements; current countermeasures remain adequate for 2026.)*

---

## Playbook 3: Journalist Security Playbook

**File**: `phase-2-journalist-security-playbook.md`
**Current version**: 1.0 (May 7, 2026)

### UPDATE-JOUR-01 — DOJ Journalist Protections Formally Rescinded (April 2025) and Activated (May 2026)
**Priority**: HIGH — This is the highest-priority update across all three playbooks.
**Section to update**: Section 1.4 (Grand Jury Subpoenas for Source Testimony) — major expansion required
**What to add**: The playbook correctly described DOJ guidelines as "voluntary policies" that "can be changed by the AG at any time." That change occurred: AG Bondi rescinded the guidelines in April 2025. The playbook was written in May 2026 and did not reflect the rescission. The first high-profile activation occurred in May 2026 with WSJ reporter subpoenas. This requires updating Section 1.4 from future-conditional to present-tense-active language.

**Specific new content for Section 1.4**:
1. Bondi memo (April 2025): Full rescission of the Biden 28 C.F.R. § 50.10 protections. The previous prohibition on subpoenaing journalists for source identification in national security leak investigations is no longer DOJ policy.
2. Washington Post reporter search (January 2026): FBI executed a search warrant at Hannah Natanson's home, including compelled Face ID unlock of her devices — the first documented forced biometric journalist device search under the revised guidelines.
3. WSJ reporter subpoenas (May 2026): Grand jury subpoenas targeting reporter records in the Iran war coverage case. President personally directed the AG via handwritten note labeling the coverage "treason." CPJ condemned the subpoenas May 26, 2026.

**Patch text (replacement/major expansion of Section 1.4)**:

**Section 1.4: Grand Jury Subpoenas — DOJ Guidelines Rescinded, Threat Now Active**

> **CRITICAL UPDATE (June 2026)**: DOJ journalist protection guidelines were rescinded in April 2025 by AG Bondi. This is no longer theoretical risk — it is current policy.
>
> **What no longer exists**: The Biden-era 28 C.F.R. § 50.10 guidelines previously prohibited DOJ from subpoenaing journalists to identify sources when reporting on government leaks, with narrow exceptions. AG Bondi's April 2025 memorandum formally rescinded that policy. Prosecutors are no longer required to seek alternatives before subpoenaing journalist records.
>
> **2026 documented activations**:
> - January 2026: FBI executed a search warrant at Washington Post reporter Hannah Natanson's home. Agents compelled Face ID unlock of her devices. The case involves a classified information investigation of a government contractor.
> - May 2026: DOJ issued grand jury subpoenas to Wall Street Journal reporters for source records related to Iran war coverage. President Trump personally directed AG Blanche to pursue the investigation, labeling the articles "treason" in a handwritten note. CPJ condemned the subpoenas on May 26, 2026.
>
> **What this means operationally**:
> - Journalists who report on national security, classified information, or topics where the administration claims leak damage now face active subpoena risk, not theoretical risk.
> - The DOJ "will not seek to compel journalist testimony" assurance that previously shaped source protection calculations is no longer valid.
> - Source protection planning must assume that phone records, email metadata, and anything held by a third party (carrier, ISP, Google, Microsoft) can be compelled without prior notice to the journalist.
> - The correct protective measures — Signal for all source communication, VoIP-registered phone, no real-name email for source contact, SecureDrop for document transfer — are more urgent than when the playbook was written, not less.
>
> **The Shield law gap is now actively exploited**: The federal PRESS Act passed the House unanimously but remains stalled in the Senate. As of June 2026, there is no federal shield law. State shield laws do not apply in federal court. A journalist who receives a federal grand jury subpoena cannot invoke reporter's privilege in federal proceedings in most circuits.
>
> **Source: RCFP analysis, Freedom of the Press Foundation, CPJ, Washington Post, The Hill.*

---

### UPDATE-JOUR-02 — FISA 702 June 12 Expiration Uncertainty
**Priority**: HIGH
**Section to update**: Section 1.2 (FISA Section 702) — update the "Congressional status as of May 2026" paragraph
**What to add**: The prior document described Section 702 as extended 45 days through June 12. The Senate vote on June 5, 2026 failed 47-52. The program is in a genuine expiration risk window for the first time. However, the FISC backstop (extending existing certifications through 2027 regardless of congressional outcome) means Signal users face zero practical change.

**Patch text (replacement of "Congressional status as of May 2026" paragraph)**:
> **Congressional status as of June 6, 2026**: Section 702 expires June 12. The Senate voted 47-52 on June 5 to advance a reauthorization bill, failing the motion to proceed. Seven Republicans joined Democrats in opposition; Senate leadership planned another procedural vote the following week. A legislative lapse is possible for the first time in this reauthorization cycle.
>
> **What a lapse would and would not change**: Even if Section 702 expires on June 12, the Foreign Intelligence Surveillance Court (FISC) issued an administrative order separately extending operational authority for existing certifications through 2027. NSA collection continues under FISC authority regardless of congressional outcome. FBI query authority for new queries of the existing database is the area of legal uncertainty if the statute lapses.
>
> **For Signal users**: The operational recommendation is unchanged. Signal has zero data the FBI can query via Section 702, by design. Whether Congress reauthorizes or allows expiration, Signal users face no practical surveillance change. The recommendation to use Signal for all sensitive source communications is independent of the FISA outcome.

---

### UPDATE-JOUR-03 — Cellebrite iOS 26 Extraction — Device Seizure Protocols
**Priority**: HIGH
**Section to update**: Section 3 (Clean-device border crossing protocol) — add note on current Cellebrite capabilities
**What to add**: Cellebrite's Spring 2026 release confirmed iOS 26 and iPhone 17 AFU-state extraction, plus the new Safeguard Mode that defeats the 72-hour auto-reboot countermeasure if the device is secured in unlocked state.

**Why this matters specifically for journalists**: The clean-device protocol already recommends powering off the device before border crossings. Cellebrite's Safeguard Mode only works if they achieve AFU access first — if the device is powered off (BFU state), extraction is still substantially limited. The power-off countermeasure remains the most effective available. But the prior guidance should add explicit context: powering off is critical specifically because of Safeguard Mode — a locked screen is not sufficient because an agent can wait out the 72-hour auto-reboot window using Safeguard Mode once AFU access is established.

**Patch text (addition to Section 3 — clean device protocol)**:
> **Cellebrite Spring 2026 Update — Power Off Is Essential**: Cellebrite's April 2026 update confirmed extraction capability for iOS 26 and iPhone 17. Critically, it introduced "Safeguard Mode" — a capability that preserves AFU (After First Unlock) access to a device indefinitely, defeating the iOS 72-hour automatic reboot that previously put devices back into the more protected BFU (Before First Unlock) state.
>
> **What this means**: If your device is seized while unlocked (AFU state), Cellebrite can now preserve that access indefinitely. A locked screen alone is not sufficient — agents can put the device in Safeguard Mode and return to it later.
>
> **The countermeasure that remains effective**: Power off the device completely before any anticipated seizure event (border crossing, enforcement contact, protest). A fully powered-off device is in BFU state; Cellebrite cannot establish the AFU access that Safeguard Mode requires. BFU extraction capability is substantially more limited than AFU. Power off is the single most important step before any seizure risk.

---

### UPDATE-JOUR-04 — Clearview AI and Journalist Identification at Protests and Events
**Priority**: MEDIUM
**Section to update**: Section 2 (Field security) or equivalent
**What to add**: Clearview AI's 50B+ image database includes photos scraped from the internet — including journalist byline photos, press conference photos, conference photos, and any public profile photo. Unlike the HART database (which requires a government booking or enrollment), Clearview can identify a journalist from any public photo. ICE HSI and CBP have confirmed Clearview contracts. Photojournalists at protest or enforcement events may be identified through Clearview even with masks if any portion of their face, distinctive features, or clothing pattern matches a public photo.

**Patch text (addition to field security section)**:
> **Clearview AI and Journalist Identification**: ICE and CBP are confirmed Clearview AI users. Clearview's database of 50+ billion scraped internet images includes journalist profile photos, press conference photos, and public event photos. A photojournalist or video journalist covering enforcement operations or protests may be identifiable via Clearview even with partial masking if a prior public photo provides adequate matching features.
>
> **Countermeasure**: For field coverage of enforcement operations or protests where ICE or federal agents may be present, consider: (1) use a different appearance from your published byline photo where possible; (2) do not use press credential lanyard or identifying press gear that links you to a trackable public identity if you are in a contested surveillance zone; (3) cover identifying tattoos or other distinctive features visible in your public photos. Note that these measures are imperfect — Clearview's database may include images that predate these countermeasures.

---

### UPDATE-JOUR-05 — DOJ Revocation of Guidelines Changes Source Communication Risk Assessment
**Priority**: HIGH (crosscutting — affects all sections involving source communication)
**Section to update**: Section overview / threat assessment framing
**What to add**: The threat framing in the existing playbook treats the grand jury subpoena and NSL risks as distinct. The DOJ guideline rescission collapses this distinction — any leak-related reporting can now result in journalist subpoena regardless of prior norms. The threat model should add a note that source communication security is now a legal self-protection issue for the journalist, not only a source protection issue.

**Patch text (add to Section 1 overview or add as Section 1.5)**:
> **1.5 The DOJ Guideline Rescission — Source Communication is Now Journalist Self-Protection**
>
> Prior to April 2025, the distinction between protecting sources (for their safety) and protecting journalist communications (for the journalist's legal protection) was conceptually different. The DOJ guideline rescission collapsed this distinction.
>
> Under the old guidelines: prosecutors needed AG approval to subpoena journalist records; the threshold was high; the presumption was against subpoenas.
>
> Under the Bondi memorandum (April 2025): no special threshold. Standard federal subpoena and search warrant authority applies. A journalist is treated like any other witness who may have knowledge of a federal crime.
>
> **The practical result**: If a journalist communicates with a source using Gmail, their email is producible. If they call a source on a phone number registered in their name, the call records are producible via NSL to the carrier. If they receive documents via a personal email account or cloud storage service, those documents are producible. Signal messages are not producible — Signal has no message content.
>
> **This means source communication security protects the journalist, not only the source.** A journalist who uses Signal from the first contact with a source, routes calls through VoIP numbers, and receives documents via SecureDrop is protecting themselves from being a direct evidence conduit that the DOJ can subpoena. This is a self-interest argument that is now available alongside the source protection argument.

---

## Cross-Playbook Priorities Summary

| Update ID | Playbook | Priority | Type | Estimated Length |
|-----------|----------|----------|------|-----------------|
| UPDATE-JOUR-01 | Journalist | HIGH | Major expansion (Section 1.4 rewrite) | ~400 words |
| UPDATE-JOUR-03 | Journalist | HIGH | Addition (Section 3 note) | ~150 words |
| UPDATE-JOUR-05 | Journalist | HIGH | New section (Section 1.5) | ~200 words |
| UPDATE-JOUR-02 | Journalist | HIGH | Paragraph replacement (Section 1.2) | ~150 words |
| UPDATE-IMM-01 | Immigration | HIGH | Section 1.3 expansion + patch text | ~150 words |
| UPDATE-IMM-02 | Immigration | HIGH | Section 1.3 addition | ~150 words |
| UPDATE-IMM-03 | Immigration | HIGH | New subsection 1.6 | ~200 words |
| UPDATE-ACT-01 | Activist | HIGH | Section 1.4 addition | ~150 words |
| UPDATE-ACT-02 | Activist | HIGH | Section 1.5 expansion | ~150 words |
| UPDATE-IMM-05 | Immigration | MEDIUM | Social media section addition | ~150 words |
| UPDATE-ACT-03 | Activist | MEDIUM | New organizational threat note | ~150 words |
| UPDATE-ACT-04 | Activist | MEDIUM | Section 1.4 note | ~100 words |
| UPDATE-IMM-04 | Immigration | MEDIUM | Paragraph addition (Section 1.1) | ~75 words |
| UPDATE-JOUR-04 | Journalist | MEDIUM | Field security section addition | ~150 words |
| UPDATE-ACT-05 | Activist | LOW | Section 1.2 footnote | ~75 words |

**Execution sequence for July 2026 distribution readiness**:
1. All HIGH items first: UPDATE-JOUR-01, UPDATE-JOUR-03, UPDATE-JOUR-05, UPDATE-JOUR-02, UPDATE-IMM-01, UPDATE-IMM-02, UPDATE-IMM-03, UPDATE-ACT-01, UPDATE-ACT-02
2. MEDIUM items as capacity allows before July 26 Wave 1: UPDATE-IMM-05, UPDATE-ACT-03, UPDATE-ACT-04, UPDATE-IMM-04, UPDATE-JOUR-04
3. LOW item can be deferred to post-Wave-1 update cycle: UPDATE-ACT-05

**Total estimated addition to playbooks**: ~2,350 words across three playbooks. No existing guidance should be deleted — all updates are additions or replacements of specific dated-paragraph language.

---

*Version 1.0 — 2026-06-06. Based on THREAT_ENVIRONMENT_Q2_2026_UPDATE.md (2026-06-06). All patch text is ready for direct insertion. Review against current playbook text before inserting to verify section alignment — document versioning may have changed section numbers since the May 7, 2026 playbook creation.*
