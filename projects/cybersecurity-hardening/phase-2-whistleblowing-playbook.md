---
title: "Institutional Whistleblowing Playbook: Evidence Preservation, Secure Transmission, Legal Protection, and Retaliation Defense"
project: cybersecurity-hardening
created: 2026-05-07
status: production-ready
phase: Phase 2
version: 1.0
depends_on:
  - threat-model.md
  - opsec-playbook.md
  - implementation-guide.md
  - PHASE_2_SEQUENCING_STRATEGY.md
confidence: high — grounded in confirmed False Claims Act FY2025 record enforcement ($6.8B settlements, 1,297 qui tam filings), SEC whistleblower program FY2025 annual report ($60M+ in awards), DOGE/SSA whistleblower cases (Charles Borges OSC filing), SecureDrop 2025 updates, Freedom of the Press Foundation documentation, Office of Special Counsel FY2026 budget justification, and Government Accountability Project immigration whistleblower support documentation
audience: Federal government employees, federal contractors, employees of private companies with government contracts, state and local government employees, private sector employees with evidence of fraud against the government
word_count: ~3,700
---

# Institutional Whistleblowing Playbook

**For attorneys advising potential whistleblowers and workshop facilitators**: The whistleblowing landscape changed materially in 2025–2026. The DOGE-era data access controversies produced the most significant whistleblower case against a sitting administration in years: Charles Borges, SSA's Chief Data Officer, filed a whistleblower complaint with the Office of Special Counsel documenting DOGE's improper access to Social Security data. Congress and the SSA Inspector General opened independent investigations. The DOJ reported record False Claims Act enforcement in FY2025: $6.8 billion in settlements and judgments, with 1,297 qui tam actions filed by whistleblowers — both records. The SEC awarded $60M+ to 48 individual whistleblowers in FY2025.

The 2026 context also includes significant risk: federal employees who expose DOGE-related misconduct face an administration that has demonstrated willingness to use the full surveillance apparatus against critics and leakers. The operational security requirements for DOGE-era whistleblowers are higher than for typical False Claims Act relators, because the adversarial government has access to the surveillance tools described throughout this corpus.

This playbook is structured in the sequence a potential whistleblower should follow: pre-disclosure preparation, evidence collection without detection, secure transmission, legal protection structure, retaliation documentation, and ongoing security.

---

## Section 1: Threat Model — What Government Whistleblowers Face in 2026

### 1.1 Network Monitoring on Government Systems — The Primary Detection Risk

**The surveillance architecture**: All U.S. government networks are subject to comprehensive monitoring under the Federal Information Security Management Act (FISMA) and subsequent executive orders. Every file accessed, every email sent, every document printed, every USB device connected, and every external upload attempt from a government network generates a log entry. The monitoring is continuous, automated, and retroactive — a security team can reconstruct your network activity for months before any disclosure if an investigation is opened.

**Specific capabilities**: Government network security tools (including commercial products like Splunk and CrowdStrike, as well as agency-specific SIEM platforms) perform behavioral analysis that can flag anomalous data access patterns — large volumes of file downloads, access to files outside your normal scope of work, off-hours access, and connections to cloud storage or external email services. These flags do not require human initiation; they are automated.

**The DOGE-specific threat**: For employees at agencies that DOGE has accessed (SSA, IRS, DHS, OPM, and others), DOGE-affiliated personnel have documented access to agency data systems. Any internal communication about DOGE data access, DOGE misconduct, or opposition to DOGE data requests may be visible to DOGE personnel through their access to agency systems, before a formal whistleblower complaint is filed.

**The foundational rule**: Never access, copy, document, or transmit evidence from a government computer or government network. All evidence collection and disclosure must occur on personal equipment, on personal networks, and on personal time.

### 1.2 Device Forensics — Cellebrite and the Personal Device Risk

The Cellebrite threat (documented fully in `opsec-playbook.md` and `implementation-guide.md`) applies with full force to whistleblowers who are subjects of investigation. ICE's $11M Cellebrite contract, FBI Cellebrite access, and Department of Justice Cellebrite use are documented. If a government whistleblower becomes the subject of a leak investigation, their personal devices — phone, laptop, tablet — can be seized and subjected to forensic extraction.

**The BFU/AFU distinction for whistleblowers**: A device that is powered off and surrendered in Before First Unlock (BFU) state is significantly more protected against Cellebrite extraction than a device in After First Unlock (AFU) state. Power off all personal devices before any anticipated law enforcement contact. An auto-reboot timer (GrapheneOS: 18 hours) ensures that a seized device that is not accessed promptly returns to BFU state automatically.

**What Cellebrite can extract from an AFU device**: All Signal message history (if Signal app is on the device and the device is unlocked or had been unlocked since last boot), photos, documents, browser history, contacts, and app data. Disappearing messages, if set to 24 hours or less, will have already deleted messages that were received more than 24 hours before seizure.

**Countermeasure**: Section 3 — dedicated evidence device; Section 4 — SecureDrop operational security.

### 1.3 PRISM and Section 702 — Email and Cloud Storage Exposure

Personal email (Gmail, Outlook/Hotmail, Yahoo) and cloud storage (Google Drive, Dropbox, iCloud) are PRISM providers. If a whistleblower uses personal Gmail to draft or transmit evidence, and the recipient or any related party is a Section 702 target, those communications may be collected under PRISM before any formal investigation is opened. The collection is automatic — it does not require a decision to target the whistleblower specifically.

**The specific risk**: Drafting a disclosure document in Google Docs and emailing a draft to a journalist's Gmail address creates at least three PRISM-accessible data points before the disclosure is published.

**Countermeasure**: Encrypted offline document creation; SecureDrop transmission; no email for any whistleblower-related communications.

### 1.4 Parallel Construction — The Risk After Disclosure

Parallel construction is a documented investigative technique in which law enforcement uses information from surveillance or a confidential informant to identify a target, then independently re-develops an evidentiary case using legally admissible sources so that the original surveillance does not need to be disclosed in court. For whistleblowers: even if the government cannot prove how it identified a leaker (because the identification came from classified surveillance), it can use that knowledge to direct investigation toward legally admissible evidence.

**Practical implication**: A whistleblower who believes their disclosure was operationally secure should not assume that secure transmission prevents investigation. Law enforcement can identify you through parallel evidence (your known proximity to the disclosed information, access logs that narrow the field of potential leakers) even if your SecureDrop submission was untraceable. Document all potentially retaliatory actions from the moment any investigation is opened — this documentary record is essential for both legal defense and public accountability.

### 1.5 Retaliation — The Most Immediate Operational Risk

Retaliatory personnel actions (firing, demotion, security clearance revocation, administrative investigation, job transfer) are the primary immediate consequence facing most whistleblowers. The Office of Special Counsel (OSC) documented a sharp increase in whistleblower retaliation complaints from federal employees in 2025–2026, coinciding with DOGE-related terminations and the administration's aggressive use of personnel actions.

**DOGE-era retaliation patterns**: DOGE-related retaliation has taken forms that are difficult to challenge legally: reassignment to new positions (not dismissal), changes in performance review criteria, security clearance review (which effectively sidelines an employee during the review period), and "administrative leave" pending investigations. These actions can continue for months before they rise to a legal challenge threshold.

---

## Section 2: Legal Protection Framework

### 2.1 False Claims Act (Qui Tam)

**What it covers**: The False Claims Act (31 U.S.C. §§ 3729–3733) allows private individuals to file suit on behalf of the government against contractors, companies, and individuals who have defrauded the federal government. A qui tam plaintiff (the whistleblower/relator) is entitled to 15–30% of the government's recovery. FY2025 saw record FCA enforcement: $6.8 billion in settlements and judgments, with 1,297 qui tam actions filed.

**Anti-retaliation protection**: The FCA explicitly prohibits retaliation against employees who report fraud. If an employee is fired, demoted, or harassed because they reported FCA violations, they are entitled to reinstatement, double back pay, and attorneys' fees (31 U.S.C. § 3730(h)).

**Coverage scope**: Applies to any company or individual with federal contracts or receiving federal funds — hospitals receiving Medicare/Medicaid, defense contractors, technology companies with government contracts, universities with federal grants, and the full range of government vendors.

**DOGE relevance**: Companies that provided false certifications to obtain government contracts, inflated invoices, or misrepresented services delivered are FCA targets. DOGE's actions in canceling contracts may have created disputes in which one party or the other made misrepresentations — these could be FCA-actionable.

### 2.2 Whistleblower Protection Act (Federal Employees)

**What it covers**: The Whistleblower Protection Act (WPA) protects federal employees who disclose information about violations of law, gross mismanagement, gross waste of funds, abuse of authority, or substantial and specific danger to public health or safety — to authorized recipients (Congress, Inspectors General, the Office of Special Counsel, or the public).

**Critical limitation**: The WPA does not protect disclosures to the press. Disclosures to journalists are not protected under the WPA and do not shield the employee from adverse personnel actions or criminal prosecution under the Espionage Act (for classified information).

**Protected disclosure channels**:
- Congress (any member or staff, under Rule XI protections for congressional disclosures)
- Inspectors General (every major federal agency has an OIG; most accept anonymous disclosures via hotline)
- Office of Special Counsel (osc.gov — the primary federal body for whistleblower retaliation complaints)
- Any supervisor or management official, in good faith

**OSC remedies**: OSC can demand the agency undo retaliation, compensate the employee, and take action against the retaliating supervisor. OSC has unique authority to seek a temporary stay of a pending personnel action during its investigation — this is the fastest available legal relief for an employee facing imminent adverse action.

### 2.3 SEC Whistleblower Program (Private Sector)

**What it covers**: The SEC whistleblower program under Dodd-Frank allows individuals to report securities law violations to the SEC in exchange for 10–30% of sanctions exceeding $1M. In FY2025, the SEC received approximately 27,000 tips and awarded $60M+ to 48 individuals. The program has anti-retaliation provisions — employers cannot fire, demote, or harass employees who report to the SEC.

**DOGE relevance**: Companies whose stock price was affected by their responses to DOGE-related government actions (data sharing, contract changes, access to federal systems) may have made material misrepresentations to investors — SEC-actionable.

**Filing note**: SEC tips can be filed anonymously through the SEC's online tip portal (sec.gov/whistleblower) with an attorney. Anonymous tips are accepted; identifying information is required only if you wish to claim an award.

### 2.4 Sarbanes-Oxley (Private Sector Employees)

**What it covers**: SOX (18 U.S.C. § 1514A) protects employees of publicly traded companies who report fraud to the SEC, DOJ, Congress, or "any person with supervisory authority over the employee." SOX retaliation complaints are filed with OSHA within 180 days of the adverse personnel action.

**OSHA whistleblower program**: OSHA administers approximately 20 federal whistleblower statutes, covering industries from financial services to environmental protection to transportation safety. If you are unsure which statute covers your situation, the DOL's whistleblower protection program website (dol.gov/agencies/osha/whistleblower) has a statute finder.

### 2.5 Protections That Do Not Exist

**Classified information**: Disclosing classified information to the press is not protected under any federal whistleblower statute. It is a potential criminal offense under the Espionage Act (18 U.S.C. § 793). This does not mean classified information whistleblowers have no options — Congress, IGs, and the IC IG all have authority to receive classified disclosures through secure channels. But disclosing classified information to a journalist is not whistleblowing protection — it is potential federal prosecution.

**No protection for press disclosures under WPA**: This bears repeating because it is the most consequential gap. The WPA protects disclosures to Congress, IGs, and OSC. It does not protect disclosures to the media, regardless of the public interest in the information.

---

## Section 3: Evidence Collection Without Detection

### 3.1 The Foundational Rule — Never Use Government Equipment

No whistleblower evidence collection should occur on government computers, government phones, government networks (including government WiFi), or government cloud storage. Any electronic footprint on government systems creates an audit trail accessible to the same agencies being reported on.

**What government equipment includes**: Your work laptop, work-issued phone, work email account, government network (VPN or physical), government printers, government USB drives, and any shared drive on a government system.

**What is permitted**: Memory — your own recollection. Notes taken on personal paper (not printed from government systems). Observations documented on personal equipment, on personal time, on personal networks.

**The exception for pre-existing personal copies**: If you lawfully received a document that was sent to your personal email address (not a government email) as part of legitimate work correspondence, that personal copy may be documentable. Consult with a whistleblower attorney before relying on this.

### 3.2 Dedicated Evidence Device

For any whistleblower who anticipates collecting or transmitting documentary evidence, a dedicated evidence device — purchased with cash, never connected to your home network, registered to no identity — is the correct architecture.

**Device setup**:
1. Purchase a low-cost laptop or tablet with cash from a retail store (not online — no purchase record)
2. Do not register the device with a manufacturer account; skip account setup during initialization
3. Do not connect it to your home WiFi network or any network associated with your identity
4. Use it exclusively on public WiFi (library, coffee shop) that is not a network you regularly use
5. Install Tails OS (tails.boum.org) on a USB drive; boot from Tails OS for all evidence-related work. Tails leaves no traces on the device's hard drive and routes all connections through Tor

**Document creation on the evidence device**:
- Create all evidence documentation in LibreOffice (included in Tails) or as plain text
- Do not use Google Docs, Microsoft Word with cloud save, or any cloud-connected application
- Save documents to the encrypted persistent storage volume in Tails (not the device's internal storage)

### 3.3 What to Document and How

**What constitutes useful evidence**:
- Official documents that can be lawfully copied from public-facing systems (e.g., publicly accessible government databases, reports already published, Freedom of Information Act-released materials)
- Your own contemporaneous notes of what you directly observed, heard, or participated in — with dates, times, locations, and names of other participants
- Correspondence sent to your personal email address (not government email) by colleagues or supervisors
- Public statements by officials that contradict the misconduct you are documenting

**Documentation best practices**:
- Date and timestamp every entry at the time of observation, not retroactively
- Note the basis for each entry (I personally observed X; Y told me Z on Date; document A states B)
- Do not speculate — document what you know, not what you infer
- Do not take photos of classified documents, classified screens, or any material that has classification markings

**What to avoid**:
- Copying files from government systems to personal storage (USB, personal email, cloud upload) — this is independently prosecutable as unauthorized removal of government property or computer fraud, separate from any whistleblower protections
- Photographing classified documents or classified screens
- Retaining classified information at home

---

## Section 4: Secure Transmission — SecureDrop Protocol

### 4.1 SecureDrop — The Standard for Anonymous Document Submission to Journalists

SecureDrop is operational at 65+ news organizations including the New York Times, Washington Post, The Guardian, ProPublica, and The Intercept. For a whistleblower who wishes to disclose to a journalist:

**The SecureDrop protocol**:
1. Use your dedicated evidence device booted into Tails OS
2. Connect to public WiFi that is not associated with your identity and that you do not regularly use
3. Open Tor Browser (built into Tails)
4. Navigate to the news organization's SecureDrop .onion address (found at securedrop.org/directory or the newsroom's public website)
5. Follow the submission prompts; upload documents or enter information
6. Write down your randomly generated source codename — this is the only way to check for journalist responses
7. Do not return to the SecureDrop interface from any device or network associated with your identity

**After submission**: The journalist will respond via the SecureDrop interface. Check for responses by returning to the same .onion address with your codename, on the same device configuration, from a different public network.

### 4.2 Critical Operational Failures to Avoid

The standard failure mode for whistleblowers is not cryptographic — it is operational. In documented cases, whistleblowers exposed themselves by:

- Accessing SecureDrop or journalist contact portals from a work device or work network — the government's network logs show exactly what was accessed
- Accessing SecureDrop from a home network that is traceable to their residential address via ISP records (even over Tor, the connection pattern to Tor entry nodes is logged by the ISP)
- Using a personal phone (carrier-traceable) to contact a journalist before or after using SecureDrop
- Emailing journalist questions or asking for their SecureDrop address from a personal email account that is PRISM-accessible
- Posting about the misconduct on any identifiable social media account before completing the disclosure

**The rule**: SecureDrop from Tails from public WiFi from the evidence device, with no cross-contamination between that device and any account or network associated with your identity.

### 4.3 For Disclosures to Congress or the Inspector General

For disclosures to Congress or IGs (protected under the WPA for federal employees):
- Contact a whistleblower attorney first to understand your specific legal exposure before approaching Congress
- Congressional staff can receive sensitive information in secure facilities (SCIFs) if classified material is involved
- Inspector General offices accept anonymous disclosures via hotline or secure online portal
- Government Accountability Project (whistleblower.org) provides direct legal support and referrals for federal employees and contractors

---

## Section 5: Legal Support — Who to Call Before You Act

### 5.1 The Single Most Important Action: Consult Counsel First

The single highest-ROI action for any potential whistleblower is retaining a whistleblower attorney before any disclosure — not after a subpoena arrives, not after a personnel action, but before. The reasons:

1. Your attorney-client communications are privileged. Everything you tell your attorney before disclosure is protected by attorney-client privilege. Nothing you say to a journalist, a friend, a spouse, or a colleague is protected.
2. Your attorney can assess which legal protection framework, if any, applies to your specific disclosure — FCA, WPA, SEC program, SOX, or a combination.
3. Your attorney can advise whether internal reporting (to IG or OSC) before external disclosure triggers greater legal protection or reduces risk.
4. Your attorney can help you understand exactly what documentation you should preserve and what you should not attempt to collect.

**Cost note**: Qui tam False Claims Act attorneys typically work on contingency — they are paid from the government's recovery, not by the relator. SEC whistleblower attorneys also often work on contingency. WPA/OSC retaliation attorneys may require retainer fees but can apply for fee shifting if retaliation is established.

### 5.2 Whistleblower Legal Resources

- **Government Accountability Project**: whistleblower.org — direct legal support for federal employees and contractors, including DOGE-era cases and immigration enforcement whistleblowers. Provides attorney referrals and direct advocacy.
- **National Whistleblower Center**: whistleblowers.org — resources and attorney referrals
- **Office of Special Counsel**: osc.gov — file WPA retaliation complaints; seek temporary stays of adverse personnel actions
- **Whistleblowers.gov (DOL)**: whistleblowers.gov — official OSHA whistleblower program, covering 20+ federal statutes
- **SEC Whistleblower Program**: sec.gov/whistleblower — anonymous tips accepted; 10–30% of sanctions over $1M
- **False Claims Act qui tam attorneys**: Contact through whistleblower.org or NWLC (National Whistleblower Legal Center)

### 5.3 Specific Support for DOGE-Related Disclosures

As of May 2026, the Government Accountability Project is providing specific support for federal employees with information about DOGE data misuse, DOGE personnel misconduct, or retaliation for raising concerns about DOGE's access to agency data. The OSC has opened investigations into DOGE-related retaliation complaints. The SSA OIG has an active investigation following whistleblower disclosures about DOGE's misuse of SSA data.

---

## Section 6: Retaliation Documentation and Response

### 6.1 Document Every Potentially Retaliatory Action

From the moment you file a whistleblower complaint, make any internal disclosure, or take any action that your employer might learn about: keep a contemporaneous log of every personnel action, communication, meeting, and interaction with management. A retaliation case is built on documented pattern, not isolated events.

**What to document**:
- Date, time, location, and participants in any meeting where your performance, conduct, or complaint is discussed
- Exact language used (direct quotes, not paraphrase) in any conversation about your complaint or status
- Written communications (save copies to personal storage outside government systems)
- Timeline of performance reviews, ratings, assignments, and responsibilities before and after your disclosure
- Any changes in access, work assignments, schedule, or treatment that correlate with your disclosure

**Form**: A dated, timestamped log kept in encrypted storage on personal equipment, not on government systems.

### 6.2 OSC Temporary Stay — The Fastest Available Relief

If you have filed a WPA complaint with OSC and are facing a pending adverse personnel action (firing, demotion, security clearance revocation), you can request a temporary stay of the personnel action while OSC investigates. OSC has authority to seek stays directly from the agency. This does not resolve the underlying case — it buys time to build the legal record while preventing the immediate harm.

**Timeline**: File a stay request as early as possible. OSC requests stay within 3 business days of a complete stay request submission. Agencies must comply with OSC stay requests pending formal adjudication.

### 6.3 Message Discipline — What to Say and to Whom

Once any disclosure is made:
- All communications about the disclosure, the underlying misconduct, and your legal strategy should occur only with your attorney
- Do not discuss the disclosure with colleagues, friends, or family in settings where communications could be monitored or subpoenaed
- Do not post about the disclosure on social media before consulting with your attorney
- If contacted by investigators or government counsel: "I am represented by counsel. Please direct all inquiries to [attorney name and contact]."
- If subpoenaed to testify before a grand jury: your attorney must be present or available; you may invoke your Fifth Amendment right not to self-incriminate

---

## Section 7: Implementation Checklists

### Checklist A: Before Any Disclosure

- [ ] Retained a whistleblower attorney (or consulted with GAP/NWC for attorney referral)
- [ ] Identified which legal protection framework covers your specific situation (FCA, WPA, SEC, SOX, OSHA)
- [ ] Identified the correct disclosure channel (IG, OSC, Congress, SEC, or press via SecureDrop)
- [ ] Purchased dedicated evidence device with cash; installed Tails OS
- [ ] All evidence documentation created on personal equipment, personal time, personal network only
- [ ] No document or file copied from government systems to personal storage

### Checklist B: Secure Transmission via SecureDrop

- [ ] Device booted into Tails OS
- [ ] Connected to public WiFi not associated with your identity
- [ ] Accessed SecureDrop .onion address through Tor Browser
- [ ] Source codename written down and stored securely (not in phone or email)
- [ ] No personal phone, personal email, or personal social media used in connection with this submission

### Checklist C: Post-Disclosure Ongoing Security

- [ ] Contemporaneous log of all personnel actions, communications, and potential retaliation started
- [ ] All communications about disclosure, legal strategy, and underlying facts routed through attorney
- [ ] Personal devices in BFU posture before any anticipated law enforcement contact (full power-off)
- [ ] Data broker opt-outs submitted for personal identity (LexisNexis Accurint, secondary brokers) — see immigration playbook Section 2 for complete list
- [ ] Escalation contact (attorney) available and briefed on current situation

---

## Summary: Five Principles That Matter Most

1. **Consult counsel before acting** — attorney-client privilege is the only communication protection that is absolute. Everything you tell anyone else before retaining counsel is potentially compellable. The highest-ROI action costs nothing more than a phone call.

2. **Never use government equipment for evidence collection** — the audit trail on government systems is the primary detection vector. All documentation must happen on personal equipment, personal time, personal networks.

3. **SecureDrop from Tails from public WiFi** — the three-layer operational requirement for anonymous journalist disclosure. Any shortcut defeats the protection.

4. **Document retaliation contemporaneously** — a WPA or FCA retaliation case is built on documented pattern. The log must be contemporaneous, specific, and maintained in personal encrypted storage from the moment any disclosure is made.

5. **Know what is and is not protected** — disclosures to the press are not protected under the WPA. Disclosures to Congress, IGs, and OSC are protected. Classified information disclosed to the press is potential Espionage Act territory. Know exactly where your disclosure falls before you make it.

---

**Version**: 1.0
**Created**: May 7, 2026
**Next scheduled review**: July 26, 2026 (quarterly corpus review)
**Cross-references**: `opsec-playbook.md` (device security), `implementation-guide.md` (BFU/AFU and Cellebrite), `phase-2-journalist-security-playbook.md` (journalist-side SecureDrop protocol), `threat-model.md`, `PHASE_2_SEQUENCING_STRATEGY.md` (Section 3.5)

---

## Sources

- [False Claims Act Enforcement in 2026 — Foley & Lardner](https://www.foley.com/insights/publications/2026/03/false-claims-act-enforcement-in-2026-2/)
- [DOJ FY2025 False Claims Act record — whistleblowers.org](https://crokefairchild.com/2026/02/whistleblowers-and-the-false-claims-act/)
- [SEC Whistleblower Program FY2025 Results — Outten & Golden](https://www.outtengolden.com/newsroom/sec-whistleblower-program-results-for-fy-2025-whistleblowers-continue-to-level-the-playing-field-for-investors-and-promote-market-integrity/)
- [SEC Awards Over $60M to Whistleblowers in FY2025 — Phillips & Cohen](https://www.phillipsandcohen.com/sec-awards-over-60-million-to-whistleblowers-in-fy25/)
- [SEC Whistleblower Program FY2025: "Reason for Cautious Optimism" — Phillips & Cohen](https://www.phillipsandcohen.com/sec-whistleblower-program-annual-report-for-fy-2025-shows/)
- [DOGE SSA data: Congress and OIG investigating — OPB](https://www.opb.org/article/2026/03/12/new-investigations-look-at-doge-and-social-security-data/)
- [Guide for DOGE Whistleblowers — Oberheiden P.C.](https://federal-lawyer.com/ultimate-guide-for-doge-whistleblowers/)
- [Blowing the Whistle in 2026: Employee rights guide — Spiggle Law](https://spigglelaw.com/blowing-the-whistle-2026-employee-rights/)
- [Whistleblower Protection Laws comprehensive guide — KKC](https://kkc.com/frequently-asked-questions/us-whistleblower-protection-laws/)
- [Office of Special Counsel FY2026 Congressional Budget Justification](https://www.osc.gov/~assets/docs/fy-2026-congressional-budget-justification.pdf)
- [Government Accountability Project — immigration whistleblower support](https://whistleblower.org/immigration/)
- [SecureDrop — 2025 year in review](https://securedrop.org/news/looking-back-at-2025/)
- [Freedom of the Press Foundation — SecureDrop documentation](https://freedom.press/tech/news/securedrop-looking-back-at-2025/)
- [FinCEN Whistleblower Program emergency deadline — Federal Register](https://www.federalregister.gov/documents/2026/04/01/2026-06271/whistleblower-incentives-and-protections)
- [PHASE_2_SEQUENCING_STRATEGY.md — Section 3.5 Whistleblowing Playbook](./PHASE_2_SEQUENCING_STRATEGY.md)
- [EFF — ICE surveillance (Cellebrite contract, device security context)](https://www.eff.org/deeplinks/2026/01/ice-going-surveillance-shopping-spree)
