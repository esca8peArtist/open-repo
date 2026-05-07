---
title: "Tier 2 Immigration Attorney Implementation Guide: Encrypted Practice Operations and Subpoena Defense"
project: cybersecurity-hardening
created: 2026-05-07
status: production-ready
phase: Tier 2
audience: Immigration attorneys, law clinic directors, paralegals, accredited representatives, legal clinic trainers
depends_on:
  - immigration-attorney-implementation-guide.md
  - opsec-playbook.md
  - palantir-threat-model.md
word_count: ~2,400
---

# Tier 2 Immigration Attorney Implementation Guide

**Most important finding**: Attorney-client privilege protects the *content* of your communications with clients. It does not protect metadata — who you communicated with, when, how often, from what location. ICE administrative subpoenas issued to Google, Microsoft, and phone carriers obtain metadata without privilege applying. A subpoena to your firm for client contact records is not blocked by privilege. The legal defense against metadata exposure is architectural: use tools that produce no compellable metadata, not privilege assertions after the fact.

---

## Part 1: Legal Privilege Landscape — What Is and Is Not Protected

### 1.1 Attorney-Client Privilege Scope

The attorney-client privilege (ACP) protects confidential communications between an attorney and a client made for the purpose of obtaining or providing legal advice. In the immigration context this covers:

- Your legal advice, case strategy, and representation communications
- Client disclosures of facts relevant to their case
- Work product: mental impressions, strategies, case theories

**What ACP does not protect**:

- Metadata: the fact that you communicated, when, how often, from what IP address or phone number
- Your client's location or address — this is a fact, not a communication, and is compellable via subpoena to third parties (data brokers, utility companies, employers) without privilege applying
- Documents your client gave you that existed independently of the attorney-client relationship (pre-existing documents)
- Communications made in furtherance of a crime or fraud (the crime-fraud exception)

**The metadata gap is the primary attack surface in 2025–2026**: ICE administrative subpoenas issued to Google, Apple, and phone carriers seek call logs, email metadata, and location data. These requests produce records showing that your phone contacted a specific number on a given date — identifying your client as an ICE target without any privilege assertion being available. *Source: ACLU, "Know Your Rights: ICE Administrative Subpoenas" (April 17, 2025) — https://assets.aclu.org/live/uploads/2025/04/ACLU-KYR-on-ICE-administrative-subpoenas-4.17.25.pdf*

### 1.2 ICE Administrative Subpoenas — Response Playbook

ICE issues administrative subpoenas under 8 U.S.C. § 1225(d)(4) and related authority. Unlike grand jury subpoenas, they are self-issued — no court approval required. However, they are not self-executing: ICE must go to a federal court to enforce them if you object.

**Five-step response sequence for law clinics and firms**:

1. **Do not comply on receipt.** You are not required to produce records immediately. An administrative subpoena has the force of a civil document request, not a court order. Compliance before asserting objections waives those objections.
2. **Immediately preserve and log.** Document the subpoena, date received, contents, and any accompanying communications. This is your litigation record if enforcement is sought.
3. **Assert privilege in writing within 10 days.** Send a written response asserting attorney-client privilege over all client communications and work product. Identify categories of responsive material but do not produce them.
4. **Consult the National Immigration Project (NIPNLG) or your state bar ethics hotline.** NIPNLG maintains a 2026 attorney and legal representative training calendar covering administrative subpoena response — https://nipnlg.org. The ILRC's "ICE's Use of Subpoenas to Circumvent State and Local Laws" (April 2025) is a primary reference — https://www.ilrc.org/sites/default/files/2025-04/ICE%E2%80%99s%20use%20of%20subpoenas%20to%20Circumvent%20State%20&%20Local%20Laws.pdf
5. **Force ICE to court for enforcement.** If ICE seeks a court order compelling compliance, you litigate the privilege claim. Courts have recognized privilege in this context; the key precedent is *Prisoners' Legal Services v. DHS* (SDNY pending 2026), which challenges ICE interference with privileged legal mail at detention facilities. Source: Robert F. Kennedy Human Rights — https://rfkhumanrights.org/litigation/pls-v-dhs-protecting-the-first-amendment-and-attorney-client-privilege-in-ice-detention/

### 1.3 E-Discovery and Metadata Protection

If your firm is ever subject to civil litigation that includes e-discovery, metadata in your documents (creation date, author, revision history, tracked changes) is discoverable. Standard practice:

- Before producing any document, strip metadata using a dedicated metadata removal tool (Metadata Anonymisation Toolkit, or ExifTool for images)
- Produce in PDF/A format (which preserves content but eliminates most embedded metadata) rather than .docx
- Log all document production in a privilege log: document title, date, author, privilege basis, whether produced or withheld

---

## Part 2: Client Intake Security Procedures

### 2.1 Secure Intake Form Design

The intake form is the highest-risk document in your practice: it names the client, their address, immigration status, family members, and employer. If this form exists as a Google Form, a Dropbox file, or an unencrypted email attachment, it is accessible via an administrative subpoena with no privilege protection.

**Secure intake architecture (deploy in 30 minutes)**:

Option A — Encrypted web form: Use Proton Forms (available with Proton Business at $6.99/user/month — https://proton.me/mail/security) or JotForm with HIPAA encryption enabled. Data is encrypted at rest; Proton cannot produce content to law enforcement. Avoid any form that stores data on U.S.-based Google or Microsoft servers.

Option B — In-person paper intake with encrypted scan: Complete intake on paper, scan immediately to an encrypted device, shred the paper. The encrypted device uses FileVault (macOS) or BitLocker (Windows) — no cloud sync.

Option C — Signal Note-to-Self for basic intake: For small clinics with limited tech resources, conduct verbal intake and record essential facts in Signal's "Note to Self" feature on an attorney device set to disappearing messages (1 week). Signal stores nothing on servers; content disappears from device automatically.

**Intake checklist — minimum required fields for an encrypted form**:

- [ ] Name (aliases acceptable for initial intake)
- [ ] Preferred contact method and contact details
- [ ] Country of birth and citizenship
- [ ] Current immigration status and any prior orders
- [ ] Case type (removal defense, affirmative relief, etc.)
- [ ] Emergency contact (family member with separate contact info)
- [ ] Signed consent to representation and data handling policy

### 2.2 Encrypted Waiting Room — Client Communication Before Representation

Before a client becomes an official client, they contact you through uncontrolled channels (public website, referral, phone). This pre-representation communication is not covered by attorney-client privilege. Treat it as adversarially observable.

**Protocol for pre-representation contact**:

- Use a dedicated Signal phone number (registered via MySudo — https://getsudo.com — for $2.99/month, creates a virtual number without carrier metadata linking to the attorney) for initial contact.
- Instruct all inbound callers: "We prefer to communicate via encrypted messaging. I will send you a link to set up Signal." Then send a signal.org/install link via MySudo SMS.
- Once the client has Signal, conduct all subsequent communications through Signal only.
- Do not collect identifying information (name, address, A-number) until Signal is established and the representation engagement is signed.

### 2.3 Client Device Hardening Advice for Non-Technical Clients

Your clients may be using Android phones with advertising SDKs that transmit GPS location to commercial data brokers — the same brokers who sell that data to ICE. The immigration attorney-implementation-guide.md in this corpus covers the full device hardening protocol. For non-technical clients, use this simplified script:

**Three-step script for clinic staff to deliver in 5 minutes**:

"There are apps on your phone that track where you go and sell that information. We want to help you stop that. It takes five minutes.

Step 1 — Turn off ad tracking: On iPhone, go to Settings → Privacy & Security → Tracking → turn off 'Allow Apps to Request to Track.' On Android, go to Settings → Privacy → Ads → Delete Advertising ID.

Step 2 — Turn off location for social media: Go to Settings → Privacy → Location Services. For each app (Facebook, Instagram, TikTok, Snapchat), change to 'Never.'

Step 3 — Don't post your location on social media. Before any social media post, check: can someone figure out where I am or where I live from this?"

Distribute as a printed card in Spanish, Haitian Creole, Tigrinya, Somali, or other languages relevant to your clinic's client population. The card should include the QR code for signal.org/install.

---

## Part 3: Evidence Preservation — Legally Defensible Audit Trails

### 3.1 FOIA Litigation Metadata Protection

If your client is involved in FOIA litigation or you are pursuing FOIA requests on their behalf, agency-produced documents contain metadata that can reveal which agency official accessed, modified, or transmitted the document — and when. This metadata is valuable but must be preserved immediately on receipt.

**Preservation protocol**:

1. On receipt of FOIA-produced documents, immediately save the original files to an encrypted local drive without opening them in any editing application.
2. Create a hash of each file (SHA-256) on receipt and record the hash in a timestamped log. This creates a forensically defensible chain of custody if the authenticity of documents is later challenged.
3. Do not open FOIA-produced .docx or .pdf files in Microsoft Office or Adobe Acrobat without first examining them in a hex editor or metadata viewer — some government-produced files contain tracking pixels or embedded identifiers.

### 3.2 Subpoena Response — Evidence Preservation Hold

When a subpoena arrives at your firm, immediately issue a litigation hold to all staff: no deletion of any responsive material pending resolution. This hold must be documented in writing and distributed to all staff who might have responsive records.

**Litigation hold template (adapt to firm letterhead)**:

"Effective [date], all personnel are instructed to preserve all records, communications, and documents related to [client name/case category] pending resolution of the subpoena received [date]. Do not delete, overwrite, or transfer any such records. Preserve all emails, Signal messages (disable disappearing messages for affected conversations immediately), case management records, and physical files. Contact [supervising attorney] with any questions."

---

## Part 4: Training Materials for Legal Clinics and Law Schools

### 4.1 Four-Hour Clinic Deployment Curriculum

**Learning objectives**: After completing this training, clinic staff can: (1) deploy Signal for all client communications; (2) respond to ICE administrative subpoenas without immediate compliance; (3) advise clients on device hardening in plain language; (4) establish secure intake procedures that create no compellable metadata.

**Hour 1: Threat Model (60 minutes)**

- 20 min: Lecture — What ICE can actually get without a court order (administrative subpoenas, data broker contracts, metadata). Use concrete case: a client's Google Maps location history sold to a data broker then purchased by ICE.
- 20 min: Hands-on — Participants search themselves on Spokeo, WhitePages, and BeenVerified. What does ICE see when they search your client?
- 20 min: Lecture — What attorney-client privilege actually protects (content, not metadata) and the crime-fraud exception.

**Hour 2: Communication Tools (60 minutes)**

- 30 min: Hands-on — Each participant installs Signal on their phone. Sets up disappearing messages (1 week default). Practices sending an encrypted message. Trainer demonstrates what a Signal server subpoena returns (account creation date and last connection — nothing else).
- 15 min: Lecture — ProtonMail for email (when to use vs. Signal, limitations when emailing to Gmail/Outlook addresses).
- 15 min: Hands-on — Each participant creates a Proton account and sends an encrypted email to another participant's Proton account.

**Hour 3: Intake and Documentation (60 minutes)**

- 20 min: Demo — Existing intake form review. Trainer identifies each field that creates a compellable record outside privilege protection. Clinic director commits to at least one structural change.
- 20 min: Hands-on — Participants practice the five-step subpoena response protocol using a mock subpoena scenario.
- 20 min: Hands-on — Participants practice the three-step client device hardening script. Role-play: one participant is the staff member, one is a non-English-speaking client with a translator present.

**Hour 4: Integration and Clinic Policy (60 minutes)**

- 30 min: Clinic director writes (or adapts) a one-page written security policy covering: which tools are required for client communications; how intake data is stored; who is authorized to respond to subpoenas; how to issue a litigation hold.
- 30 min: Q&A and scenario practice. Trainer presents three scenarios: (1) ICE arrives at the clinic asking to speak with a client who is present; (2) a subpoena arrives for client contact records; (3) an attorney's phone is seized at a border crossing while returning from an international conference.

### 4.2 Training for Non-English-Speaking Staff and Volunteers

Many immigration law clinics operate with bilingual volunteers who may not be attorneys. For non-attorney staff:

- Provide a one-page protocol card (laminated, posted at intake desk) covering: how to communicate with clients (Signal only); what to say if law enforcement arrives (do not admit clients are present; do not produce records without attorney authorization; call supervising attorney immediately).
- Conduct a 30-minute volunteer orientation covering: what the clinic protects and why; what volunteers can and cannot do (they cannot waive privilege; they cannot consent to records production); what the chain of command is for security incidents.

### 4.3 Success Metrics for Clinic Deployment

A clinic that has completed this training meets the following criteria:

- [ ] 100% of client communications move to Signal within 30 days of training
- [ ] Intake form produces no metadata stored on U.S. Big Tech servers
- [ ] All staff have received and signed the written security policy
- [ ] Supervising attorney has read and understood the five-step subpoena response protocol
- [ ] Client device hardening script delivered to all new clients at intake
- [ ] Litigation hold procedure documented and tested with a mock scenario

**Target deployment time**: A fully-equipped clinic (supervisor + 2–3 staff) can complete initial deployment within 4 hours of this guide. ProtonMail account creation, Signal setup, and intake form migration are each 30-minute tasks. The subpoena response protocol requires reading (1 hour) and one mock drill.

---

## Part 5: Tool Recommendations and Trade-offs

| Tool | Cost | Setup Time | Protects | Does Not Protect | Trade-off |
|---|---|---|---|---|---|
| Signal | Free | 5 min | Message content, metadata on Signal servers | Metadata at carrier level (that Signal was used) | Clients must install; non-technical friction |
| ProtonMail | Free / $3.99/mo | 10 min | Email content (Proton-to-Proton E2E) | Metadata to non-Proton addresses | Only fully E2E between Proton users |
| MySudo | $2.99/mo | 10 min | Real phone number from Signal/call identity | Nothing if subpoenaed (MySudo retains some metadata) | Adds one layer; not a complete solution |
| Tresorit | $10/mo | 30 min | Case files (Swiss jurisdiction, requires Swiss court order) | Nothing if U.S. court issues MLAT request | Significant barrier vs. Google/Dropbox |
| OnionShare | Free | 20 min | Document transfer (Tor, no central server) | Nothing if recipient device is compromised | Requires Tor Browser on both ends |
| Proton Drive | Included | 15 min | Files (Swiss jurisdiction, end-to-end encrypted) | Nothing under MLAT | Better UX than OnionShare for clients |

---

## Sources

1. ACLU, "Know Your Rights: ICE Administrative Subpoenas" (April 17, 2025) — https://assets.aclu.org/live/uploads/2025/04/ACLU-KYR-on-ICE-administrative-subpoenas-4.17.25.pdf
2. ILRC, "ICE's Use of Subpoenas to Circumvent State and Local Laws" (April 2025) — https://www.ilrc.org/sites/default/files/2025-04/ICE%E2%80%99s%20use%20of%20subpoenas%20to%20Circumvent%20State%20&%20Local%20Laws.pdf
3. Robert F. Kennedy Human Rights, "Prisoners' Legal Services v. DHS" — https://rfkhumanrights.org/litigation/pls-v-dhs-protecting-the-first-amendment-and-attorney-client-privilege-in-ice-detention/
4. NYCLU, "Civil Rights Orgs Sue DHS and NY ICE Detention Facility" — https://www.nyclu.org/press-release/civil-rights-orgs-sue-dept-of-homeland-security-ny-ice-detention-facility-for-first-amendment-violations/
5. National Immigration Project, 2026 Attorney & Legal Rep Trainings Calendar — https://nipnlg.org/sites/default/files/2026-01/2026-trainings-print.pdf.pdf
6. Cyrus Mehta Immigration Blog, "Ethical Obligations of the Attorney to Safeguard Information About a Client's Whereabouts" (December 2024) — https://blog.cyrusmehta.com/2024/12/ethical-obligations-of-the-attorney-to-reveal-information-about-a-client-with-a-removal-order-under-trump-2-0.html
7. DHS/ICE Privacy Impact Assessment, ICE Subpoena System (PIA-027) — https://www.dhs.gov/publication/dhsice-pia-027-ice-subpoena-system
8. ACLU, "DHS Uses Administrative Subpoenas to Obtain Critics' Personal Data" — https://immpolicytracking.org/policies/dhs-uses-administrative-subpoenas-to-obtain-personal-data-from-critics/
9. Freedom of the Press Foundation, "ProtonMail Pro Tips" — https://freedom.press/digisec/blog/protonmail-pro/
10. LegistAI, "Secure Client Intake Form Templates for Immigration Law" — https://www.legistai.com/secure-client-intake-form-templates-for-immigration-law-downloadable-examples/
