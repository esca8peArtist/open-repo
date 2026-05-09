---
title: "Institutional Whistleblowing Security Playbook: Evidence Exfiltration, Secure Channels, and Long-Term Operational Security for Government and Corporate Whistleblowers"
project: cybersecurity-hardening
created: 2026-05-09
status: production-ready
phase: Phase 2
version: 1.0
depends_on:
  - opsec-playbook.md
  - threat-model.md
  - phase-2-whistleblowing-playbook.md
  - phase-2-journalist-security-playbook.md
confidence: high — grounded in CISA Insider Threat Mitigation Guide (January 2026), False Claims Act FY2025 record enforcement ($6.8B settlements, 1,297 qui tam filings), SEC whistleblower program FY2025 annual report, Charles Borges OSC complaint (SSA/DOGE case), Daniel Berulis NLRB case, SecureDrop 2025 annual review, Freedom of the Press Foundation documentation, Teramind/Exabeam insider threat detection platform specifications, Splunk/CrowdStrike SIEM behavioral analysis capabilities, Office of Special Counsel FY2026 budget documentation
audience: Federal government employees, federal contractors, private sector employees at companies with government contracts, critical infrastructure employees at CISA-regulated organizations, financial services employees (SEC/FINRA-regulated), employees at defense contractors with DoD access
word_count: ~3,900
legal_notice: This guide addresses lawful whistleblowing through protected channels. Nothing in this guide advises unauthorized disclosure of classified national security information, which carries criminal liability under the Espionage Act. The legal channels and operational security measures described here are specifically designed for disclosures that qualify for protection under the Whistleblower Protection Act, False Claims Act, SEC whistleblower rules, or equivalent statutes. Consult a whistleblower attorney before taking any action.
---

# Institutional Whistleblowing Security Playbook

**For attorneys, compliance officers, and HR professionals advising potential whistleblowers**: The 2025–2026 environment produced the most significant institutional whistleblowing cases in years — simultaneously demonstrating that whistleblower protections work (the Charles Borges case produced Congressional investigations and IG referrals) and that the retaliatory surveillance capability is more sophisticated than any previous era. The DOJ reported record False Claims Act enforcement in FY2025: $6.8 billion in settlements, 1,297 qui tam actions filed. The SEC awarded $60M+ to 48 whistleblowers. The protective structure is real. The adversarial surveillance capability is also real. This playbook maps both.

**The critical difference from journalist security**: A journalist's relationship with a source is relatively brief; the journalist bears most of the operational security burden; the source needs to make one or a few secure transfers and then go dark. An institutional whistleblower typically faces a longer timeline — building a case over months, maintaining evidence without detection, working inside a hostile institution while preparing to disclose — and faces a technically sophisticated adversary (corporate IT, government SIEM, insider threat programs) that has pre-existing access to the whistleblower's digital footprint. The challenge is not a single secure transfer; it is sustained operational security over an extended evidence-building period inside the adversary's own network.

---

## Section 1: Threat Model — What Institutional Whistleblowers Face in 2026

### 1.1 Government Network Monitoring — The FISMA Surveillance Architecture

**The comprehensive monitoring baseline**: Every U.S. government network operates under FISMA (Federal Information Security Management Act) requirements that mandate continuous monitoring of all network activity. Every file accessed, every email sent, every document printed, every USB device connected, every external upload attempt from a government computer generates a log entry. These logs are retained for minimum periods specified by NIST 800-92 (minimum 1 year, typically 3+ years for sensitive agencies), and can be queried retroactively.

**SIEM behavioral analytics**: Modern government SIEM platforms (Splunk, IBM QRadar, Microsoft Sentinel) apply behavioral analysis that automatically flags:
- Large volumes of file downloads or unusual data access patterns outside normal work scope
- Access to files outside the user's organizational unit or cleared scope
- Off-hours access with high-volume file activity
- Connections to external email services, file transfer sites, or cloud storage from government networks
- USB device connections, particularly to unregistered devices
- Print spooler activity for large documents outside normal patterns

These flags do not require a human decision to initiate — they are automated alerts that route to insider threat program analysts.

**The DOGE-specific threat layer**: For employees at agencies that DOGE has accessed — SSA, IRS, DHS, OPM, and others — DOGE-affiliated personnel have documented access to agency data systems beyond normal oversight channels. The NLRB whistleblower case (Daniel Berulis) documented DOGE accounts being created with unusual access rights and suspicious network traffic attributed to those accounts. Any internal communication about DOGE data access or DOGE misconduct may be visible to DOGE personnel through their system access before a whistleblower complaint is formally filed.

**The absolute rule**: Never access, copy, document, or transmit evidence from a government computer or government network. All evidence collection and disclosure must occur on personal equipment, on personal networks, and on personal time.

---

### 1.2 Corporate Insider Threat Programs — The Private Sector Equivalent

**What major employers deploy (2026)**:

The leading insider threat detection platforms deployed by large private employers — particularly at financial services firms, defense contractors, and critical infrastructure companies — have substantially matured in 2026:

- **Teramind**: Captures keystrokes, screen/video recording, file operations, application usage, and real-time screen analysis. Behavioral analytics flag anomalous patterns automatically. Some deployments include covert mode (employees are not notified of monitoring). As of 2026, Teramind is one of the most widely deployed corporate monitoring platforms.
- **Exabeam**: AI-based behavioral analysis comparing current activity against the user's own historical baseline. Flags deviations without requiring security analysts to manually review logs. Particularly effective at detecting gradual data exfiltration (slow, sustained access to sensitive documents over weeks).
- **Microsoft Purview (formerly Compliance Center)**: Deployed in Microsoft 365 environments, Purview monitors email, Teams, SharePoint, and OneDrive for sensitive content patterns, data transfer to external accounts, and policy violations. Organizations using Microsoft 365 can enable "insider risk management" policies that automatically alert when users access and transfer large volumes of sensitive files.
- **CrowdStrike Falcon**: Endpoint detection and response (EDR) monitoring kernel-level device activity, including USB connections, network connections, process execution, and file operations. In a CrowdStrike-monitored environment, every action on the monitored device is logged.

**The behavioral baseline problem**: Insider threat platforms are most dangerous because they establish a behavioral baseline for each user and flag deviations. If you work in accounting and suddenly start accessing HR files, or if your access patterns shift from 9-to-5 to midnight on weekends, the anomaly triggers an alert. Incremental behavior changes are flagged just as surely as sudden ones if the system has a long enough baseline.

**CISA's January 2026 guidance**: CISA published new insider threat mitigation guidance on January 28, 2026, recommending multi-disciplinary insider threat management teams combining HR, legal, IT security, and physical security. The guidance explicitly covers "trusted insiders" who may be motivated by ideology, financial stress, or grievance — language that encompasses would-be whistleblowers. CISA's guidance is for critical infrastructure operators; it signals the sophistication of the institutional adversary.

---

### 1.3 Device Forensics — Cellebrite and Corporate IT Investigation

**The personal device seizure risk**: If a whistleblower becomes the subject of an internal investigation before disclosure, employers can request (and courts can compel) production of personal devices as part of discovery or an HR investigation. BYOD (Bring Your Own Device) programs complicate this further: if you use a personal device for work purposes under a BYOD agreement, the employer may assert a right to access work-related data on the device.

**Cellebrite in corporate investigations**: Corporate investigators routinely retain firms with Cellebrite capabilities for internal investigations. Unlike law enforcement, corporate investigators are not subject to Fourth Amendment constraints — they can examine devices that have been surrendered voluntarily (under threat of termination) or pursuant to civil litigation discovery. The Cellebrite UFED Premium tool can extract data from most Android and iOS devices in AFU (After First Unlock) state.

**The BFU protection principle**: A device in BFU (Before First Unlock) state — powered off and not unlocked since boot — presents significant barriers to Cellebrite extraction. Power down all personal devices before any anticipated employment action, HR meeting, or investigation conversation. An auto-reboot timer (GrapheneOS: configurable from 1 hour to 7 days; recommended 18 hours) ensures that a seized device not accessed promptly returns to BFU state.

---

### 1.4 PRISM and Section 702 — Email and Communications Exposure

Section 702's PRISM program compels major internet companies to provide communications content for targeted non-U.S. persons. Government whistleblowers who communicate with foreign journalists, foreign NGOs, or foreign government sources face a compound risk: their communications are potentially collected under Section 702, and the government can query the database using their identity. See `phase-2-journalist-security-playbook.md` Section 1.2 for full technical detail on Section 702.

**The specific risk for government-to-media communication**: If a federal employee communicates with a journalist at a major news organization about potential misconduct, and that journalist has previously communicated with a foreign source who is a Section 702 target, the FBI may have access to the journalist's communication records — including the identity of government employees who contacted the journalist — without a warrant and without judicial oversight.

**Mitigation**: SecureDrop submission (anonymous, no email contact) as the initial approach. Direct contact with a journalist should occur only after establishing an anonymous communication channel via SecureDrop. See Section 4.

---

### 1.5 Keystroke Logging and Screen Capture — The Most Underestimated Risk

On employer-managed devices and in some BYOD agreements, keystroke logging can capture every word you type — including search queries related to whistleblowing, drafts of disclosure documents, and communication with attorneys. Screen capture tools (Teramind, Microsoft Purview) can record screenshots on a time interval or triggered by flagged activities.

**The personal device rule**: Any research, communication, or documentation related to potential whistleblowing must occur exclusively on personal devices, on personal networks, on personal time. Not on an employer-managed device — even if you believe the device is not monitored. Not on a work network — even through a personal device connected to corporate WiFi. Not on personal accounts accessed from a work computer.

---

## Section 2: Legal Framework — What Protections Actually Exist

### 2.1 Whistleblower Protection Act (Federal Employees)

The Whistleblower Protection Act (WPA) protects federal employees who disclose "information about gross mismanagement, a gross waste of funds, an abuse of authority, or a substantial and specific danger to public health or safety." Coverage applies to disclosures to Congress, IGs, the Office of Special Counsel, and now (under the Whistleblower Protection Enhancement Act) to supervisors.

**Critical limitation**: The WPA does not protect disclosures of classified information through non-authorized channels. A federal employee who discloses classified information to a journalist is not protected by the WPA — they face criminal prosecution under the Espionage Act. The Intelligence Community Whistleblower Protection Act (ICWPA) provides a narrow channel for classified disclosures to Congressional intelligence committees, with specific procedural requirements.

**2026 status**: The Office of Special Counsel remains functional for receiving WPA complaints. OSC has a 45-day deadline to complete a preliminary determination on whistleblower retaliation complaints. In the DOGE era, OSC received substantially increased complaint volume and has been resource-constrained. Supplement OSC filing with a direct complaint to the relevant agency IG and Congressional oversight committees.

### 2.2 False Claims Act (Government Contractor Employees)

The False Claims Act (31 U.S.C. § 3729–3733) allows private individuals to bring qui tam actions on behalf of the government against contractors who commit fraud against federal programs. The qui tam relator (whistleblower) receives 15–30% of any government recovery. FY2025 saw record FCA enforcement: $6.8 billion in settlements and judgments, with 1,297 qui tam actions filed — both records.

**The key FCA procedural requirement**: Qui tam complaints are filed under seal in federal district court. They remain sealed while DOJ investigates. This seal period — typically 18 months to several years — means the employer does not know about the case during the investigation. The qui tam relator is protected from retaliation by 31 U.S.C. § 3730(h), which provides for reinstatement, double back pay, and attorney fees for retaliated-against employees.

**The mandatory pre-filing requirement**: FCA qui tam complaints must be filed in federal court before any public disclosure of the fraud. If you disclose the fraud to a journalist before filing the qui tam complaint, you may be disqualified as the original source and lose the qui tam award. File first, disclose second — the "first-to-file" bar means the sequence matters legally.

### 2.3 SEC and CFTC Whistleblower Programs

The SEC's whistleblower program (Dodd-Frank Section 21F) awards between 10–30% of sanctions exceeding $1 million to individuals who provide original information about securities law violations. FY2025: $60M+ awarded to 48 individuals. The CFTC has a parallel program for commodity market violations.

**Anonymous submission**: Both programs allow anonymous submission through an attorney. The whistleblower's identity is not disclosed to the SEC/CFTC unless enforcement action is taken and disclosure becomes necessary. This is the preferred submission path for employees with significant exposure concerns.

**The original information requirement**: SEC/CFTC awards require "original information" — information not previously known to the agency, not derived solely from public sources, and not already the subject of an existing enforcement action. Internal compliance reports that you generated are "original information" if they have not been shared with the agency.

### 2.4 Dodd-Frank Anti-Retaliation Provisions

Dodd-Frank Section 21F(h) prohibits retaliation against individuals who provide information to the SEC, assist in SEC investigations, or make internal reports of potential securities violations. The Supreme Court's decision in Digital Realty Trust v. Somers (2018) clarified that Dodd-Frank's anti-retaliation protections apply only to individuals who report to the SEC — not purely internal reporters. Report to the SEC (even anonymously through an attorney) before relying on Dodd-Frank's anti-retaliation protection.

---

## Section 3: Evidence Collection Without Detection

### 3.1 The Iron Rule — Evidence Collection Must Be Off-Network

**Never copy, photograph, or document evidence using employer-provided equipment or networks.** The specific technical reason: network monitoring captures all data transfer events. A file copy from a network share to a USB drive generates a log entry at the file server, the endpoint SIEM (Teramind/CrowdStrike), and potentially the DLP (Data Loss Prevention) system. Even a screenshot taken on an employer laptop is captured by screen-recording monitoring software.

**Lawful off-network evidence collection methods**:

1. **Memory and contemporaneous notes**: Write down from memory, on your personal device, on your personal network, what you witnessed — after leaving the employer's premises. Contemporaneous personal notes made outside the work environment are discoverable but are not captured by employer monitoring. Write detailed notes immediately after observing relevant events, before memory degrades.

2. **Photographs of physical displays**: If a document is displayed on a screen, you can photograph the screen with your personal phone while not connected to any employer network. This creates a copy of the document content without generating a network log event. Limitations: photograph quality, partial visibility.

3. **Public documents and congressional disclosures**: Many government documents that seem confidential are actually releasable under FOIA or are publicly available through congressional oversight requests. Identify whether the evidence you need is accessible through legal channels before attempting any collection.

4. **Personal observation of in-person conversations**: Notes about in-person conversations, meetings, verbal statements, and observed conduct are personal observations — not documents copied from employer systems. Detailed contemporaneous notes of in-person meetings are strong evidence and not captured by any employer monitoring.

**What is never acceptable**: Copying classified documents to personal devices, removing hard-copy classified materials from secure facilities, or transmitting classified information through unsecured channels. These actions create criminal liability under the Espionage Act regardless of the whistleblowing intent.

### 3.2 The Dedicated Evidence Device

If you are building a case over an extended period, maintain evidence on a dedicated personal device that has never been used for work purposes:

- A dedicated device purchased with cash (or through a retailer not linked to your employer identity)
- Never connected to any employer network, not even to charge from an employer outlet that also provides data
- Running GrapheneOS (for Android Pixel 6–9) or factory-reset iOS with all cloud backup disabled
- Encrypted storage: GrapheneOS encrypts by default; iOS encrypts by default with a strong alphanumeric passphrase (not biometric)
- Auto-reboot enabled: GrapheneOS auto-reboot timer set to 18 hours so that a seized device returns to BFU state
- Stored in a location your employer would not search — your home, not your office, not your car in the employer parking lot

**Signal on the dedicated device**: Registered with a VoIP number (MySudo, JMP.chat) not associated with your employer identity. Signal is end-to-end encrypted and retains minimal server-side data (only account creation date and last connection). Disappearing messages enabled on all sensitive conversations.

### 3.3 The Pattern-of-Life Problem — Maintaining a Normal Work Profile

The most dangerous period for a whistleblower is the weeks before disclosure, when evidence collection is most active. Insider threat behavioral analytics will flag a sudden change in your work pattern. Counter-detection measures:

- **Do not change your usual working hours** on your employer device. If you normally access the system from 8am to 5pm, do not begin logging off-hours sessions.
- **Do not access document categories outside your normal scope** on employer systems. If you work in procurement, do not suddenly start reviewing HR or executive correspondence on the employer network.
- **Do not search for whistleblower resources on employer networks**. Search "whistleblower attorney" or "SecureDrop" only on personal devices, on personal networks.
- **Do not discuss potential whistleblowing with colleagues via employer communications channels** (email, Teams, Slack, work phone). These channels are logged. Discuss sensitive matters in person, off-premises.

---

## Section 4: Secure Transmission — Getting Evidence to the Right People

### 4.1 SecureDrop — The Correct Channel for Media Disclosure

If your evidence involves public interest matters best disclosed through journalism, SecureDrop is the correct first contact channel. See `phase-2-journalist-security-playbook.md` Section 4.1 for full technical detail.

**Whistleblower-specific guidance for SecureDrop**:

1. Access SecureDrop from a device that has never been associated with your employer identity. The dedicated evidence device (Section 3.2) running Feather Tor Browser is appropriate.

2. Use a library computer, university WiFi, or public WiFi that is not geographically correlated with your home or work address for the SecureDrop access. Metadata showing repeated SecureDrop connections from your home IP address can identify you even if the submission itself is anonymous.

3. Do not access SecureDrop during your normal work hours — timing correlation can link the submission time to your work absence.

4. The SecureDrop codename you receive on first submission is your identity for all future communications with that outlet. Write the codename on paper; do not store it digitally in any account connected to your real identity.

5. Major outlets with active SecureDrop instances: New York Times (nytimes.com/tips), Washington Post (washingtonpost.com/tips), The Intercept (theintercept.com/source/), ProPublica (propublica.org/tips). The full directory is at securedrop.org/directory.

### 4.2 Attorney Contact — The Most Protected Channel

Communication with an attorney for the purpose of seeking legal advice is protected by attorney-client privilege. Employer monitoring that captures attorney-client communications can be challenged in court as privilege-violating. The protective structure:

1. Identify a whistleblower attorney before any other disclosure. Resources: Government Accountability Project (whistleblower.org), National Whistleblower Center (whistleblowers.org), Government Ethics lawyers, False Claims Act firms (Phillips & Cohen, Katz Banks Kumin LLP).

2. Contact the attorney from your personal device, on a personal network, not on employer time. Use email or phone for initial contact — attorney-client privilege attaches from the first consultation, not from a formal engagement.

3. If communicating sensitive details by email, use ProtonMail (protonmail.com) or Tutanota (tutanota.com) — zero-knowledge encrypted email services. Create the account on a personal device over a VPN or Tor, not from your home IP if you are concerned about IP-address surveillance.

4. Signal with the attorney's Signal account (verify safety numbers out-of-band at the first in-person meeting) is appropriate for ongoing sensitive communication. Disappearing messages enabled.

5. For highest security: in-person meetings at the attorney's office, conducted with both parties' phones powered off and left in a Faraday bag in the attorney's reception area. Phones in Attorney-Client Meeting rooms can be used for eavesdropping if compromised by stalkerware or if subpoenaed call records show the meeting time and location.

### 4.3 Congressional Disclosure — The Most Robust Protection for Federal Employees

Congressional disclosure is explicitly protected by the WPA and the First Amendment's Speech and Debate Clause (Article I, Section 6) — communications made to Congress or Congressional staff cannot be used as the basis for prosecution or retaliation against the communicating party. For federal employees whose evidence involves classified information, the ICWPA provides specific procedures for classified disclosures to Congressional intelligence committees.

**How to contact Congress securely**:
- Contact the staff director of the relevant oversight committee (House Oversight, Senate Judiciary, Senate Armed Services, Senate Intelligence, etc.) by phone or encrypted email
- The relevant committee depends on the subject matter: DOGE-related misconduct (House Oversight, Senate Homeland Security), financial fraud (Senate Banking, House Financial Services), national security (Senate/House Intelligence)
- For classified disclosures: contact the committee through official channels and request guidance on the ICWPA process before making any disclosure
- Correspondence with Congressional staff is protected; do not share classified materials through unofficial digital channels even when contacting Congress

---

## Section 5: Operational Security for the Long Game

### 5.1 The Extended Timeline — Monthly Operational Review

Unlike an activist facing a discrete event, an institutional whistleblower may spend 6–24 months building a case, working with attorneys, and awaiting legal action while remaining employed. Operational security over this period requires:

**Monthly checklist**:
- [ ] Have I communicated anything about this matter on employer systems in the past 30 days? If yes: document what was said and when; consult attorney about privilege and disclosure risk.
- [ ] Has my behavior on employer systems deviated from my normal pattern? Review with fresh eyes.
- [ ] Is the dedicated evidence device still physically secured and in my control?
- [ ] Are Signal disappearing messages enabled on all relevant conversations?
- [ ] Has the attorney-client communication channel been maintained using the correct secure method?
- [ ] Has any colleague raised questions about my activities that suggest internal monitoring alerts?

### 5.2 Compartmentalization — What to Tell Whom

**Need-to-know principle**: No colleague, family member, or friend should know the content of your evidence, your attorney relationship, or the timing of any disclosure unless their knowledge is necessary for the case. The most common way whistleblowers are identified before they are ready is through a trusted person who was told too much.

**Practical application**:
- Tell your attorney everything. Attorney-client privilege protects this disclosure.
- Tell your partner or spouse only what they need to know for safety planning — that you are working with an attorney, that they should not discuss the matter with anyone, and what to do if you are retaliated against.
- Tell no colleagues anything. Not even colleagues who share your concern about the misconduct. If they are interviewed by the employer's internal investigators, they cannot reveal what they do not know.
- Do not post on social media — even vaguely — about "whistleblowing," "retaliation," or work stress during the case-building period. Social media posts are admissible in employment proceedings and will be used against you.

### 5.3 Retaliation Documentation — Build the Record in Real Time

If you are retaliated against, the strength of your legal claim depends on contemporaneous documentation of the retaliation. Begin documenting now:

- **Performance record**: Save copies of positive performance evaluations, commendations, and favorable emails outside the employer system before the case-building period begins. If you are retaliated against, the employer will often claim that adverse employment actions were based on pre-existing performance concerns. Having documentation of your performance history before the whistleblowing disclosure rebuts this.
- **Adverse action log**: After any adverse employment action (poor review, reassignment, exclusion from meetings, verbal reprimand), document it immediately in a personal note with date, time, who was present, what was said, and what preceded it. Do this outside the employer network.
- **Comparator evidence**: Note colleagues with similar performance and responsibilities who did not receive adverse actions. This supports a comparator argument.
- **Timeline documentation**: Maintain a chronology of events — evidence observed, attorney contacted, OSC complaint filed, disclosure made — with dates. The closer the timing of retaliation to a protected disclosure, the stronger the inference of retaliatory intent.

---

## Section 6: Scenario Playbooks

### Scenario A: CISA/DHS Employee with Evidence of Improper Data Sharing

**Context**: A CISA employee has witnessed DOGE-affiliated personnel accessing agency threat intelligence databases with access credentials not authorized by normal security protocols. The employee has personal notes documenting the access events but cannot copy the system logs.

**Decision tree**:
1. Consult an attorney before any disclosure. Contact Government Accountability Project (whistleblower.org) or a WPA specialist.
2. File an OSC complaint (Form OSC-14) using a personal device and personal network. OSC contact: osc.gov or 202-804-7000.
3. Contact the CISA Inspector General through the agency IG hotline (DHS IG: oig.dhs.gov/hotline). IG disclosures are protected under the WPA.
4. Contact the Senate Homeland Security Committee and House Oversight Committee by phone, using the staff director or majority/minority counsel contact found on the committee website.
5. If media disclosure: SecureDrop to a national outlet (NYT, WaPo, The Intercept) from a library computer using Tor. Do not contact journalists by personal email or phone.

**What not to do**: Copy system logs or classified threat intelligence to personal devices. Access CISA systems off-hours to gather evidence. This creates criminal liability and destroys the protected status of the disclosure.

### Scenario B: Defense Contractor Employee with Evidence of Federal Procurement Fraud

**Context**: An employee at a DoD-contracted IT firm has evidence that the company has billed the government for work not performed (invoices for person-hours that were not logged). The employee has access to internal billing records but no ability to copy them without employer detection.

**Decision tree**:
1. Contact a False Claims Act attorney immediately. The qui tam process requires filing before any public disclosure. Phillips & Cohen (phillipsandcohen.com), Katz Banks Kumin LLP (katzbanks.com), and Whistleblower Law Collaborative are specialized FCA firms.
2. Collect evidence through lawful off-network means: photographs of billing documents displayed on screen, handwritten contemporaneous notes from memory, personal observation of billing discussions in meetings.
3. Attorney files the qui tam complaint under seal in federal district court. The seal period means the employer does not know about the case.
4. During the seal period: maintain normal work behavior; do not discuss the case with colleagues; document any adverse employment actions immediately.
5. After DOJ decision to intervene or decline: the case becomes public. If DOJ intervenes, DOJ litigates; the relator's attorney remains involved for the award calculation. If DOJ declines, the relator can proceed independently.

**Financial context**: FCA qui tam awards in FY2025 averaged approximately $5.2M per case where the government recovered funds. In large procurement fraud cases, awards can reach tens of millions. The financial incentive is real and documented.

### Scenario C: SEC-Regulated Financial Services Employee with Evidence of Securities Fraud

**Context**: A compliance officer at a broker-dealer has evidence that the firm has been systematically mismarking securities to inflate portfolio valuations for fee purposes.

**Decision tree**:
1. Contact an SEC whistleblower attorney for anonymous submission planning. The attorney submits Form TCR (Tip, Complaint, or Referral) to the SEC on your behalf, maintaining your anonymity.
2. Compile evidence using off-network, personal device methods: screen photographs of mismarked positions, contemporaneous notes of valuation discussions, memory documentation of specific instances.
3. Before filing with the SEC: do not report internally if you are concerned about retaliation. Post-Digital Realty, internal reporting does not provide Dodd-Frank anti-retaliation protection; SEC filing does. Consult your attorney on the internal vs. external reporting sequence.
4. After SEC filing: maintain normal work behavior; do not discuss the submission with colleagues. The SEC investigation may take 1–3 years.
5. SEC interviews: if the SEC contacts you for an interview, this is legally protected activity. Retain your attorney to accompany you to any SEC investigative interview. You are not required to voluntarily interview without counsel.

### Scenario D: Corporate Employee Under Active Insider Threat Investigation

**Context**: An employee who has been collecting evidence of corporate misconduct has been notified of an internal investigation and HR interview. They believe the investigation may be related to their evidence collection.

**Immediate actions (next 48 hours)**:
1. Contact a whistleblower attorney before attending any HR investigation interview. Do not attend without counsel present or at minimum telephonically available.
2. Power off all personal devices. Enable auto-reboot if using GrapheneOS. Remove biometric login from all devices.
3. Transfer custody of all evidence materials to attorney (in-person, physically, not digitally) immediately. Attorney-client privilege attaches and the evidence is now privileged.
4. Do not access, modify, or delete any employer systems or data — even data you believe you are entitled to access. Doing so during an active investigation creates obstruction exposure.
5. If you have a Signal contact for the attorney: confirm safety numbers in person at your first meeting if you have not already.
6. Do not discuss the investigation with colleagues, on social media, or in any digital channel.
7. Document every step of the investigation process in a personal contemporaneous note: who called, what was said, when the interview was scheduled, who attended.

---

## Section 7: Incident Response — If You Are Identified Before Disclosure

### Immediate Triage (First Hour)

1. **Power off all personal devices** that contain case-related evidence. Physical power-off, not sleep mode.
2. **Contact your attorney** by phone from a landline or a borrowed device not associated with your identity.
3. **Do not touch employer systems** — log off and do not log back on until you have attorney guidance.
4. **Do not communicate with colleagues** about the situation.
5. **Do not delete anything** — on employer systems, personal devices, or messaging apps. Deletion during an investigation creates obstruction liability. Evidence preservation (litigation hold) obligations may already be triggered.

### First 24 Hours

- Attorney consultation to assess the nature of the investigation and whether disclosure should be accelerated
- OSC complaint filed if not already filed — this creates a protected disclosure record before any adverse employment action
- If classified information is involved: contact the agency IG through the classified disclosure channel before any contact with journalists
- Document the timeline of the investigation notification and your response in a personal note

---

## Section 8: Tools and Resources

### Secure Communication
- **SecureDrop directory**: securedrop.org/directory — 65+ newsrooms
- **Signal**: signal.org — VoIP-registered number (MySudo, JMP.chat)
- **ProtonMail**: protonmail.com — encrypted email for attorney contact
- **Tor Browser**: torproject.org — for anonymous SecureDrop access and research

### Device Security
- **GrapheneOS**: grapheneos.org — hardened Android (Pixel 6–9); auto-reboot; BFU/AFU management
- **Tails OS**: tails.boum.org — amnesic OS for secure document handling
- **VeraCrypt**: veracrypt.fr — encrypted containers for evidence storage on personal devices

### Legal Resources
- **Government Accountability Project**: whistleblower.org — WPA specialists; federal employee cases
- **National Whistleblower Center**: whistleblowers.org — FCA and other statutes
- **False Claims Act clearinghouse**: Phillips & Cohen (phillipsandcohen.com), Katz Banks Kumin LLP (katzbanks.com)
- **SEC Whistleblower Office**: sec.gov/whistleblower — anonymous submission portal
- **CFTC Whistleblower Office**: whistleblower.cftc.gov
- **Office of Special Counsel (federal employees)**: osc.gov; Form OSC-14 for retaliation complaints
- **DHS Inspector General**: oig.dhs.gov/hotline
- **DOJ Inspector General**: oig.justice.gov/hotline
- **Government Ethics Lawyers**: Government Ethics Center, Public Employees for Environmental Responsibility (peer.org)
- **Reporters Committee for Freedom of the Press**: rcfp.org — media law support if proceeding through a journalist

### Training and Reference
- **CISA — Insider Threat Mitigation Guide, January 2026**: cisa.gov/resources-tools/resources/insider-threat-mitigation-guide
- **ODNI — Insider Threat Guide**: dni.gov/index.php/ncsc-what-we-do/ncsc-insider-threat
- **Oversight.gov — Where to report fraud, waste, or abuse**: oversight.gov/where-report-fraud-waste-abuse-or-retaliation

---

## Summary: Five Principles That Matter Most

1. **Personal device, personal network, personal time** — the entire evidence-building and disclosure process must occur outside the employer's monitoring infrastructure. This is not optional. A single use of employer systems for evidence-related activity can surface the entire operation to employer investigators months later.

2. **Attorney first, everything else second** — the sequence is: consult an attorney, then decide the disclosure path. The False Claims Act's first-to-file bar means that disclosing to a journalist before filing the qui tam may forfeit your legal award. Attorney-client privilege protects the consultation. No disclosure path should be initiated without attorney guidance.

3. **SecureDrop, not email, for media contact** — direct journalist contact by email or phone creates metadata records (carrier records, IP logs, journalist's email records) that can identify you before any legal protection attaches. Anonymous SecureDrop submission over Tor creates no such records.

4. **Normal behavior on employer systems during the build period** — insider threat behavioral analytics flag the deviations that feel most natural to a nervous whistleblower: off-hours access, unusual file review, searches for legal resources. Do all of this on personal equipment only.

5. **Documentation of retaliation starts now, not after retaliation occurs** — the best evidence for a retaliation claim is documentation made before and contemporaneous with the adverse action, not reconstructed after the fact. Your performance history, comparator data, and the timeline of your disclosures are the building blocks of any legal claim.

---

**Version**: 1.0
**Created**: May 9, 2026
**Next scheduled review**: August 9, 2026 (quarterly review)
**Cross-references**: `opsec-playbook.md` (Sections 3–4 on device hardening), `phase-2-whistleblowing-playbook.md` (base whistleblowing guidance), `phase-2-journalist-security-playbook.md` (SecureDrop, Section 702 threat detail for media contact), `threat-model.md` (Palantir architecture)

---

## Sources

- [CISA — Insider Threat Mitigation Guide, January 2026](https://www.cisa.gov/resources-tools/resources/insider-threat-mitigation-guide)
- [CISA — New Guidance on Assembling Multi-Disciplinary Insider Threat Management Teams (InsidePrivacy, January 2026)](https://www.insideprivacy.com/insider-threats/cisa-releases-new-guidance-on-assembling-multi-disciplinary-insider-threat-management-teams/)
- [The Register — CISA insider-threat warning comes with an ironic twist, January 29, 2026](https://www.theregister.com/2026/01/29/cisa_insider_threat_guidance/)
- [Katz Banks Kumin — Social Security Whistleblower Files Retaliation Complaint with OSC (Borges case)](https://katzbanks.com/news/social-security-administration-whistleblower-files-retaliation-complaint-with-the-office-of-special-counsel/)
- [Legal Reader — Whistleblower Protections in the DOGE Era: A Legal Guide](https://www.legalreader.com/whistleblower-protections-in-the-doge-era-a-legal-guide/)
- [Spiggle Law — Blowing the Whistle in 2026: A Guide for Employees](https://spigglelaw.com/blowing-the-whistle-2026-employee-rights/)
- [Federal Register — Whistleblower Incentives and Protections, April 2026](https://www.federalregister.gov/documents/2026/04/01/2026-06271/whistleblower-incentives-and-protections)
- [DOJ — False Claims Act FY2025 statistics (record $6.8B)](https://www.justice.gov/opa/pr/false-claims-act-settlements-and-judgments-exceed-68-billion-fiscal-year-2025)
- [Flashpoint — Insider Threat Defense 2026](https://flashpoint.io/blog/insider-threats-2025-intelligence-2026-strategy/)
- [Teramind — AI Insider Threat Monitoring Tools 2026](https://www.teramind.co/blog/ai-insider-threat-monitoring-tools/)
- [Exabeam — Best Insider Threat Detection Tools 2026](https://www.exabeam.com/explainers/insider-threats/best-insider-threat-detection-tools-top-5-this-year/)
- [Living Security — 6 Best Insider Threat Detection Tools for 2026](https://www.livingsecurity.com/blog/insider-threat-detection-tools)
- [SenseOn — 6 Best Insider Threat Detection Tools in 2026](https://www.senseon.io/blog/6-best-insider-threat-detection-tools)
- [SecureDrop — Looking Back at 2025](https://securedrop.org/news/looking-back-at-2025/)
- [Freedom of the Press Foundation — SecureDrop 2025 Year in Review](https://freedom.press/tech/news/securedrop-looking-back-at-2025/)
- [Oversight.gov — Where to Report Fraud, Waste, Abuse, or Retaliation](https://www.oversight.gov/where-report-fraud-waste-abuse-or-retaliation)
- [SEC — Whistleblower Program Overview](https://www.sec.gov/whistleblower)
- [Office of Special Counsel — OSC-14 Complaint Form](https://www.whistleblowers.gov/complaint_page)
- [Oberheiden P.C. — Ultimate Guide for DOGE Whistleblowers](https://federal-lawyer.com/ultimate-guide-for-doge-whistleblowers/)
- [Phillips & Cohen — Whistleblower Protection Lawyer resources](https://www.phillipsandcohen.com/whistleblower-protection-lawyer/)
- [Government Accountability Project — Resources](https://whistleblower.org/)
- [ODNI — National Insider Threat Task Force](https://www.dni.gov/index.php/ncsc-what-we-do/ncsc-insider-threat)
