---
title: "Organizational OpSec Playbook: Institutional Security for NGOs, Labor Unions, and Legal Service Providers"
project: cybersecurity-hardening
created: 2026-05-06
status: complete
phase: Phase 2
session: 846
depends_on:
  - opsec-playbook.md
  - threat-model.md
  - palantir-threat-model.md
  - organizational-defense-playbook.md
  - PHASE_2_SEQUENCING_STRATEGY.md
  - activist-organizing-playbook.md
  - immigration-attorney-implementation-guide.md
confidence: high — grounded in documented government capabilities, confirmed contract data, case law, Cloudflare Project Galileo incident data, SPLC/FBI case analysis, and current threat intelligence from EFF, Access Now, and CyberPeace Institute
audience: Executive directors, operations directors, board members, and security leads at NGOs, labor unions, and immigration legal service organizations operating under elevated government surveillance and enforcement pressure
---

# Organizational OpSec Playbook: NGOs, Labor Unions, and Legal Service Providers

**Lead finding**: Organizations facing state-level adversaries in 2026 cannot protect their members, clients, or staff by deploying individual tools alone. The attack surface at the organizational level is structurally different from the individual level — it includes supply chain entry points, staff onboarding gaps, member/donor data flows, inter-chapter communications, board governance vulnerabilities, and the exposure created by any single staff member's device or account. Between May 2024 and March 2025, Cloudflare's Project Galileo blocked 108.9 billion cyber threats against civil society organizations — averaging 325 million attacks per day. These organizations were not incidental targets. The threat is deliberate, sustained, and organizational in scope. This playbook addresses the organizational layer that individual security guides cannot cover.

**What this document does not replace**: Individual OpSec guidance from `opsec-playbook.md` and `implementation-guide.md` applies to every staff member and should be completed alongside organizational measures. This playbook addresses what the organization must do that individual action cannot accomplish.

**Scope**: This playbook covers three institutional sectors that share a common threat profile while having sector-specific vulnerabilities:
- **NGOs and civil rights organizations** — nonprofit advocacy groups, policy organizations, civil rights litigation organizations, human rights documentation groups
- **Labor unions and worker organizing networks** — AFL-CIO affiliated locals, independent union organizing drives, rank-and-file networks, worker centers
- **Immigration legal service providers** — legal aid organizations, immigration clinics, law school clinics serving undocumented individuals, sanctuary law networks

---

## Part 1: Organizational Threat Model

### 1.1 How Organizational Targets Differ from Individual Targets

The government's surveillance architecture (documented in `threat-model.md` and `palantir-threat-model.md`) is designed to resolve individuals. Palantir's entity resolution constructs ontological links between persons, locations, communications, and financial transactions. When applied to an organization, it extends these same mechanisms to institutional structures: the member roster becomes a social graph; the financial records become a relationship map; the communications infrastructure becomes an interception surface.

Four structural features of organizations create vulnerabilities that do not exist for individuals:

**Multiple entry points, single blast radius**: An organization with 20 staff has 20 potential phishing targets, 20 potential device seizure vectors, 20 potential coercion targets. A single successful entry point can expose the entire organization's data — member lists, case files, donor records, internal communications — if access controls are not properly segmented.

**Supply chain dependency**: Organizations depend on case management software, CRM systems, email platforms, cloud storage, payment processors, and donor management tools. Every vendor relationship is a potential entry point. The MOVEit breach (2023) compromised 620+ organizations through a single vendor's software vulnerability. For NGOs with fewer IT resources than the BBC or British Airways, the supply chain risk is not smaller — it is larger.

**Persistence across personnel turnover**: An individual can take countermeasures starting today and achieve meaningful protection within weeks. An organization's vulnerabilities persist through staff turnover, board transitions, and technology migrations. A security culture requires institutional embedding, not just individual awareness.

**Public-facing presence**: Organizations have websites, public social media accounts, published tax filings (Form 990 for US nonprofits), and press coverage. These public surfaces are both necessary for mission and a significant intelligence resource for adversaries. The Form 990 discloses organizational structure, executive compensation, and broad financial information — creating an intelligence baseline that a hostile actor can use before any active surveillance begins.

### 1.2 The Government Surveillance Stack Against Organizations

The same surveillance infrastructure documented in `threat-model.md` operates against organizations, with several additions specific to institutional contexts.

**IRS Lois Lerner-era targeting playbook, renewed**: The IRS LCA (Lois Lerner-Connected) platform is described in `PHASE_2_SEQUENCING_STRATEGY.md` as a financial social graph mapping system with confirmed shift toward investigating "left-leaning groups." The October 2025 Wall Street Journal report confirmed planned IRS changes to enable politically motivated investigations of nonprofits and their donors. A September 2025 Presidential Memorandum created a new National Joint Terrorism Task Force to investigate organizations participating in "criminal conspiracies" — a broad framing that civil society lawyers have assessed as covering advocacy organizations engaged in constitutionally protected activity. Combined, these represent the reinstitution of the targeting infrastructure that the Lois Lerner scandal documented: IRS scrutiny of 501(c)(3) and 501(c)(4) organizations based on perceived political alignment.

**FOIA as reverse surveillance tool**: ICE uses FOIA requests strategically — to confirm organizational capacity, map staff contacts, and audit communications. Democracy Forward and the American Immigration Council have documented cases where immigration organizations' own FOIA requests triggered ICE cross-referencing. A critical vulnerability: immigration organizations that submit FOIA requests about their own clients risk alerting ICE to client identities. The ILRC documented in 2025 that clients with removal orders face risk from their own attorneys' FOIA submissions.

**Administrative subpoenas without judicial authorization**: DHS and ICE issued hundreds of administrative subpoenas to major tech platforms (Google, Reddit, Discord, Meta) between late 2025 and early 2026, seeking to unmask identities behind anonymous accounts posting bilingual ICE raid alerts, monitoring ICE agent locations, and sharing immigration legal information. Unlike warrants, administrative subpoenas require no judicial oversight prior to issuance. For organizations whose members use commercial platforms, every DHS-issued administrative subpoena to Google or Meta is a potential membership roster exposure event.

**ICE Graphite spyware (zero-click deployment)**: ICE acknowledged in April 2026 that it uses Graphite, developed by Israeli firm Paragon Solutions. Graphite is a "zero-click" spyware capable of accessing encrypted messages, activating device cameras and microphones, and tracking individuals in real time — without requiring the target to click a link or interact with malicious content. WhatsApp disclosed in early 2025 that approximately 90 journalists and civil society members in multiple countries had been targeted with Graphite. Congressional lawmakers warned that ICE's Graphite access, combined with administrative subpoena authority, could enable deployment against "people living in the United States as part of their ideological battle against constitutionally protected protest." Zero-click spyware bypasses most organizational security measures, including encrypted messaging. Its documented use against civil society makes it the highest-severity threat in this sector.

**SPLC as case study in government pressure against civil rights organizations**: In October 2025, the FBI ended its operational relationship with the Southern Poverty Law Center under conservative political pressure. In April 2026, DOJ filed a federal criminal indictment against the SPLC — charging it with fraud related to a confidential informant program that SPLC maintained it ran in coordination with FBI, which saved lives by infiltrating violent extremist groups. Whether or not the fraud charges have merit (which legal scholars assessed as contested and potentially politically motivated), the trajectory illustrates the operational threat: a well-resourced civil rights organization was subjected to a federal criminal indictment, a severed relationship with its primary federal law enforcement contact, and the full exposure of its confidential source program — within eight months. The lesson for civil rights organizations is not to abandon informant programs, but to understand that any program touching sensitive or legally ambiguous activity is a potential indictment vector under a hostile administration.

**FBI counterterrorism attention to climate and protest organizations**: The Intercept documented in February 2026 that FBI counterterrorism agents, including a Joint Terrorism Task Force agent, visited the home of a former member of Extinction Rebellion NYC for questioning. FBI queries on organizations described as political, religious, or media groups surged from 227 in 2024 to 839 in 2025, according to the Privacy and Civil Liberties Oversight Board. This is not a marginal trend — it is a documented, quantified escalation in FBI attention to organizations engaged in constitutionally protected political activity.

### 1.3 Sector-Specific Threat Profiles

#### NGOs and Civil Rights Organizations

Primary threats:
- IRS scrutiny of 501(c)(3) mission compliance and "political activity" as defined by an administration hostile to the organization's cause
- Donor targeting: subpoenas or administrative demands for donor lists, compelled disclosure of non-public donor information
- Board governance exposure: public Form 990 filings disclose large donors, executive compensation, and program details that can be weaponized
- Government pressure on foundation funders: grant-making foundations face direct pressure to withdraw funding from disfavored organizations
- DDoS and cyber attacks: Cloudflare's Project Galileo data confirms 8.9 billion attack requests blocked against human rights and civil society organizations in a single 10-month period
- Public-facing attack surface: websites, social media, and publication infrastructure are targetable

Secondary threats:
- Third-party vendor compromise (supply chain)
- Phishing targeting staff and board members
- Insider threat (coercion of staff with family in hostile jurisdictions; ideological infiltration)

#### Labor Unions and Worker Organizing Networks

Primary threats:
- **Employer surveillance during organizing drives**: AI-powered surveillance tools that predict unionization risk (Amazon's Whole Foods surveillance program documented workers' communication patterns; Google employees alleged company installed browser extensions to deter organizing). Employers have legal access to many communications on company devices and networks.
- **NLRB deterioration**: The NLRB, compromised in 2025 with management-side lawyers installed in leadership positions and its board rendered non-functional by a disputed firing, can no longer be relied upon as a backstop against employer retaliation. Union elections fell 30% in 2025 amid this suppression.
- **FBI informant penetration**: COINTELPRO targeted labor unions with "militant" leadership from 1956 to 1971, placing informers in 85% of domestic intelligence investigations. The legal framework that ended COINTELPRO (the Church Committee reforms) has been progressively eroded. The 2025 "domestic terrorism" framing in executive orders provides legal basis for renewed FBI scrutiny of "militant labor" activity.
- **Member data exposure**: Unions hold Social Security numbers, home addresses, compensation data, and grievance records for every member. A breach of this data is both a privacy harm and an intelligence resource for employers and government investigators.
- **IRS financial scrutiny**: Union financial records are subject to Department of Labor LM-2 disclosure requirements (for unions with >$250,000 in annual receipts) and IRS scrutiny of 501(c)(5) status. A politically motivated IRS audit of a major union's finances is both disruptive and publicly embarrassing.

Secondary threats:
- Workplace platform surveillance (Teams, Slack, email) during organizing drives on employer systems
- Cross-chapter communications security for multi-local organizing campaigns
- Social media OSINT targeting organizers by employer-hired union-busting consultants

#### Immigration Legal Service Providers

Primary threats (heavily documented in `immigration-attorney-implementation-guide.md`):
- **Client data as government intelligence target**: ICE's entire enforcement architecture centers on address and relationship data. A subpoena to an immigration legal aid organization for client files, contact history, and address information provides the exact data points that feed the ELITE confidence scoring system.
- **FOIA as intelligence mechanism**: ICE tracks FOIA requests submitted on behalf of clients with removal orders. A well-intentioned FOIA submission can trigger enforcement action against the client.
- **IRS-ICE data sharing**: The April 2025 MOU allows ICE to access IRS employer records. March 2026 DHS request for employment records on "virtually every worker in the country" would, if fulfilled, include workers served by legal aid organizations.
- **Device seizures at border crossings**: CBP has authority to search devices at border crossings without a warrant. Immigration attorneys who travel internationally with case files on their devices are exposed.
- **Zero-click spyware (Graphite)**: If deployed against immigration advocacy or legal communities, Graphite could access attorney-client communications on devices without any user action.
- **Administrative subpoenas to platforms**: Attorneys who communicate with clients via Gmail, WhatsApp, or other commercial platforms are exposed when DHS issues administrative subpoenas to those platforms.

Secondary threats:
- Physical surveillance of offices (ALPR tracking vehicles of staff and clients)
- Confidential informants within client communities reporting on organization's activities
- Phishing targeting staff credentials to gain access to case management databases

---

## Part 2: Three-Tier Organizational Security Framework

The following framework maps to organizational resource levels and threat exposure. Tier 1 (Essential) is the minimum viable security posture — every organization should complete all Tier 1 actions regardless of resource constraints. Tier 2 (Advanced) addresses organizations with elevated threat exposure or resources to invest. Tier 3 (Hardened) addresses organizations that are direct targets of government investigation or operate with nation-state-level adversaries.

### Tier 1: Essential Baseline (All Organizations)

**Communications infrastructure**

1. **Move sensitive internal communications to Signal or Wire**. The choice depends on organizational context. Signal provides maximum cryptographic security and minimal organizational control. Wire provides equivalent encryption with admin controls (SSO, user management, ability to remove compromised users), which makes it preferable for organizations with more than 10 staff. The key limitation of Signal for organizations: "By default, any user can unilaterally contact any other user if they know their phone number or username" and there is no central admin capability to remove a compromised account from all conversations. Wire addresses this. For small organizations or highly distributed organizing networks, Signal remains appropriate.

2. **Establish two separate communication channels**: one for general organizational work (email and standard tools) and one for sensitive discussions (encrypted messaging). Never conduct sensitive strategic discussions, member organizing plans, or legal strategy on the general channel. This compartmentalization limits the damage from a single account compromise.

3. **Configure disappearing messages** for sensitive channels: 1 week maximum for most discussions; 24 hours for the most sensitive. Disappearing messages mean that a device seized after the retention window contains no conversation history — significantly limiting forensic recovery.

4. **Separate client/member communications from staff communications**: Organizations serving high-risk clients (immigration legal aid, domestic violence services, labor organizing drives) should maintain separate communication systems for external client contact versus internal staff coordination.

**Account security**

5. **Enforce multi-factor authentication (MFA) on all organizational accounts**: email, cloud storage, donor management, case management, social media, domain registrar, and DNS provider. MFA with hardware keys (YubiKey) is the highest standard — phishing-resistant. TOTP apps (Ente Auth, Aegis) are acceptable. SMS-based MFA is vulnerable to SIM swapping and should be disabled where possible.

6. **Deploy a shared password manager** (Bitwarden Teams at $3/user/month; 1Password Teams). Shared organizational accounts should be managed through the password manager with access control per role — not stored in shared spreadsheets or communicated via chat.

7. **Conduct quarterly access reviews**: identify all staff with access to sensitive systems (case management, donor databases, financial accounts), confirm their access is still appropriate to their current role, and revoke dormant access. Staff who leave the organization should have all access revoked within 24 hours of departure, not at end of a quarterly cycle.

**Data protection**

8. **Encrypt all sensitive data at rest**: Full-disk encryption on all staff laptops (FileVault for macOS, BitLocker or LUKS for Windows/Linux). Encrypted cloud storage for case files and member data (Tresorit, ProtonDrive, or equivalent Swiss-jurisdiction services that require non-US legal process for access).

9. **Data minimization policy**: Organizations should collect only the data they need for operations and delete it on a documented retention schedule. For immigration legal aid: client case files retained only as long as professionally required. For unions: member data retained per collective bargaining agreement and labor law requirements, not indefinitely in legacy systems. Minimizing stored data minimizes the damage from any breach or compelled disclosure.

10. **Separate member/client data from public-facing systems**: Member rosters, client lists, donor databases, and case files should never share infrastructure with the organization's public website. Compromising a WordPress installation should not yield access to the Salesforce CRM or legal case management database.

**Physical security**

11. **PIN-only device unlock, biometrics disabled**: Law enforcement can legally compel biometric unlock but generally cannot compel a memorized PIN under Fifth Amendment protections. All organizational devices should have biometric unlock disabled. For emergency use: on iPhone, hold side + volume down briefly to disable Face ID; on Android, power off before any law enforcement encounter to enter BFU (Before First Unlock) state, where encryption keys are not loaded into memory.

12. **Document retention and destruction policy**: Paper documents containing sensitive information should be shredded, not recycled. Digital documents that are no longer needed should be permanently deleted with a verified deletion tool, not merely moved to trash.

**Incident response baseline**

13. **Designate an incident commander**: One person who is responsible for coordinating response to any security incident. This person should have out-of-band contact information for all staff, pre-established contact with a legal aid organization, and a relationship with at least one external security resource (Access Now Digital Security Helpline, CiviCERT, or Freedom of the Press Foundation for press organizations).

14. **Establish an out-of-band communication channel**: A Signal group, phone tree, or secondary email list that does not depend on your primary organizational infrastructure. If your email and internal systems are compromised or down, staff must have a way to communicate. Test this channel at least twice a year.

15. **Apply for Cloudflare Project Galileo** (free enterprise-grade DDoS and web application firewall protection for qualifying civil society organizations): [cloudflare.com/galileo](https://www.cloudflare.com/galileo/). Human rights and civil society organizations saw 8.9 billion attack requests blocked through this program. This is zero-cost protection for a documented, high-volume threat.

---

### Tier 2: Advanced Organizational Security (Elevated Threat Exposure)

**Secure communications infrastructure**

16. **Deploy Wire or Element (Matrix protocol) for organizational communications**: Both provide organizational admin controls (SSO/SCIM integration, audit logs, ability to remove compromised users) that Signal does not. For organizations with federated chapters or multi-office structures, Element's federated server architecture allows each chapter to host its own server while maintaining encrypted cross-chapter communication.

17. **Separate the secure channel from active devices during sensitive discussions**: High-value strategy discussions (union contract negotiations, litigation strategy, media embargoes, source communications) should occur on dedicated devices that are not connected to the organizational network. Treat the sensitive discussion device the same way a journalist treats a source-communication device — separate hardware, separate accounts, never co-located with the primary work device.

18. **Implement Signal username-based anonymization for external contacts**: Tier 2 staff should configure Signal usernames and disable phone number discoverability. External contacts (community members, clients, press) reach staff via username, not phone number. This separates the organizational contact surface from carrier-accessible phone number records.

**Infrastructure hardening**

19. **Enable DNSSEC and registrar lock on all organizational domains**: Registrar account compromise is the simplest path to DNS hijacking — redirecting your website and email to attacker infrastructure. Enable registrar lock (prevents unauthorized transfers), use hardware key MFA on the registrar account, and enable DNSSEC on all domains. Use a registrar with strong account security (Cloudflare Registrar or Namecheap with hardware key MFA).

20. **Conduct vendor security assessments for all tools handling sensitive data**: For every vendor that processes member data, client files, or financial records, verify: (a) where data is hosted (US-hosted is subject to US legal process without international coordination requirements); (b) what their government data request response policy is (does the vendor notify you before complying?); (c) whether they carry Cyber Liability insurance; (d) whether they can provide a recent SOC 2 Type II report.

21. **Implement least-privilege access controls in all sensitive systems**: CRM, case management, donor database, and financial accounts should use role-based access that reflects the principle of least privilege. No single staff member should have access to all sensitive systems. An administrator compromise should not yield access to client case files; a caseworker compromise should not yield access to donor records.

**Member and client data protection**

22. **Encrypted client intake channels**: Legal service providers should provide clients with an encrypted intake option. SecureDrop (for organizations receiving sensitive documents) or a vetted encrypted web form (using Formspree with end-to-end encryption or a Tor hidden service form) keeps client contact information off commercial platforms.

23. **Separate client/member databases from staff directories**: The same database that contains staff names and contact information should not contain client or member records. Compartmentalization means that a subpoena for organizational records targets one category at a time, and organizational staff identity is not exposed when client records are sought.

24. **Data residency review**: Assess whether sensitive data is stored in US-hosted cloud infrastructure. US-hosted data is subject to US subpoenas, NSLs, and PRISM-authorized collection. Swiss-jurisdiction providers (Proton, Tresorit) require Swiss legal process for access — a significant additional barrier. For the most sensitive data categories (case files, member SSNs, donor identities for organizations under political scrutiny), Swiss or EU-hosted storage materially changes the legal process burden.

**Operational security**

25. **Staff security onboarding**: All new staff should complete a documented security onboarding that covers: the organizational threat model (who the adversaries are and what they want), the organizational security tier and required tools, the incident reporting procedure, and device and account expectations. This is not a one-time IT orientation — it is a mission-aligned security briefing.

26. **Visitor and contractor access policy**: Visitors should not have access to internal networks. Contractors with legitimate access to sensitive systems should have time-limited, scoped access and should be subject to the same access review cycle as staff. Every contractor relationship is a potential insider threat vector.

27. **Physical office security baseline**: Document storage for case files and membership records should be locked when staff are not present. High-sensitivity documents (source identities, confidential strategy, donor lists where privacy is legally protected) should be stored in a locked cabinet separate from general office files. A written document classification policy (see Section 4.2 below) determines what goes where.

---

### Tier 3: Hardened (Direct Investigation Targets)

Organizations that have received government legal process (subpoenas, FOIA requests indicating adversarial use, NSLs, or government-initiated investigations) should implement the following in addition to all Tier 1 and 2 measures.

28. **Retain a specialized digital rights legal team**: The ACLU, National Lawyers Guild, Electronic Frontier Foundation, and state ACLU affiliates have litigation experience with government subpoenas for organizational records. Engage counsel before receiving legal process, not after. Having a retainer relationship with digital rights legal counsel before a subpoena arrives means you can respond within hours rather than days.

29. **Activate legal privilege protections before legal process arrives**: Attorney-client privilege protects communications with legal counsel. Work product protection protects litigation preparation. Organizations that are anticipating adversarial government attention should route sensitive communications through or about their legal counsel to maximize applicable privilege protections. Document the scope of privilege protection with counsel before a crisis.

30. **Maintain an air-gapped backup system**: An encrypted external drive, kept off-network and stored in a physically secure location, containing all essential organizational records. If your cloud infrastructure is seized or compromised, you can restore operations from the air-gapped backup without paying ransom or waiting for a court order. The backup should be updated monthly and stored at a separate physical location from the main office.

31. **Counter-surveillance for key staff and leadership**: Executive directors and senior leadership of organizations under active investigation are potential targets for Mobile Fortify field biometrics (documented in `PHASE_2_SEQUENCING_STRATEGY.md` Section 1.2), aerial surveillance, and ALPR vehicle tracking. Key staff should implement the individual physical counter-surveillance measures from `opsec-playbook.md` Part 5: face covering at all public events, vehicle rotation for travel to sensitive locations, device-off or Faraday containment at high-risk public gatherings.

32. **Zero-click spyware countermeasures (Graphite/Paragon)**: Graphite bypasses traditional security measures by exploiting zero-day vulnerabilities without any user interaction. The primary countermeasures are: (a) aggressive OS and application update cadence (zero-day exploits are typically patched in subsequent updates — organizations under active surveillance risk should mandate same-day OS security updates); (b) GrapheneOS for the highest-risk devices (its hardened memory allocator and attack surface reduction materially complicates exploitation); (c) Lockdown Mode for iOS devices of key leadership (disables certain features that zero-click exploits have historically targeted, including WebKit JIT compilation and FaceTime); (d) periodic device replacement on a 12-18 month cycle for individuals under highest active risk.

33. **Canary warrant process**: Establish a documented "warrant canary" or equivalent — a regular public statement that the organization has not received certain categories of legal process. If the statement is not updated, stakeholders know to interpret the absence as a signal. The Freedom of the Press Foundation maintains guidance on warrant canary implementation at [freedom.press](https://freedom.press).

---

## Part 3: Sector-Specific Guidance

### 3.1 NGOs and Civil Rights Organizations

**The Form 990 exposure problem**: Every US 501(c)(3) organization files a public Form 990 that discloses gross revenues, expenses, net assets, executive compensation, highest-paid contractors, and programmatic descriptions. Form 990 is available to the public through GuideStar/Candid and the IRS website within months of filing. A hostile government actor, employer, or opposition researcher can derive substantial operational intelligence from Form 990 alone — executive names and compensation, organizational structure, top funders (for large grants), and programmatic scope. This cannot be avoided for 501(c)(3) organizations. The mitigation: treat Form 990 as a published threat intelligence document about your organization and make security decisions accordingly. Keep sensitive programmatic activities in discretionary funds that do not require detailed public disclosure.

**Donor privacy protection**: North Carolina passed a law in 2025 prohibiting most state and local government agencies from collecting or disclosing personal information about nonprofits' donors, members, or volunteers — a significant development that other states may follow. At the federal level, organizations can protect small donor privacy by: (a) using fiscal sponsorship to aggregate donations through a sponsoring 501(c)(3) that receives donations on the organization's behalf (reducing the number of organizational donor records); (b) accepting cash donations at events; (c) accepting Monero cryptocurrency for privacy-preserving digital donations (noting that Monero provides genuine on-chain privacy, unlike Bitcoin, which is fully traceable); (d) noting clearly in your privacy policy that donor information will be disclosed only as legally required — and retaining legal counsel to resist any disclosure that is not legally compelled.

**DDoS protection and web infrastructure**: Civil society websites face documented, high-volume DDoS attacks. The minimum viable protection is Cloudflare Project Galileo (free). Organizations that publish sensitive research or documentation (human rights organizations, investigative journalism outlets, legal aid organizations) should additionally use multiple DNS providers (Cloudflare + AWS Route53), enable registrar lock, and maintain an offline version of critical content that can be published from alternative infrastructure if the primary site is taken down.

**Responding to FBI visits**: The FBI visited the home of a former Extinction Rebellion member for questioning in February 2026. Organizations should brief all current and former members on their rights during FBI contacts: the right to decline to answer questions without counsel present; the right to immediately call an attorney; the obligation not to lie to federal agents (18 U.S.C. § 1001), which means silence is preferable to an inaccurate statement; and the right to ask whether they are free to go (if yes, leave). The National Lawyers Guild maintains a Green and Black Cross rapid response line for activists facing law enforcement contact.

### 3.2 Labor Unions and Worker Organizing Networks

**The employer surveillance threat during organizing drives**: Employer surveillance of union organizing is the dominant threat during organizing campaigns, and it is largely legal. Employers can monitor email, chat, and web activity on company devices and networks. Amazon's monitoring of Whole Foods employees for unionization risk indicators is documented. Google employees alleged company monitoring of organizing activity. The NLRA protects employees' rights to organize, but the NLRB is not currently functional as an enforcement mechanism.

**Organizing communications must occur off company infrastructure**: All union organizing discussions must occur outside of company email, company Slack, company Teams, and company devices. The failure mode is using company tools for organizing conversations — employers have lawful access to all of it. Workers should use personal devices on personal networks (not company WiFi) for all organizing communications. Signal is the appropriate tool — free, easily deployed across large worker populations, and with no employer-accessible server logs.

**Member data security requirements**: Union member data (SSNs, home addresses, compensation records, grievance files) must be treated as highly sensitive. Legacy union databases that lack MFA, encryption at rest, and role-based access controls are a documented risk. The practical minimum: move member data off spreadsheets onto a purpose-built union management platform with built-in security features, or a self-hosted database with full-disk encryption and MFA access controls. Breached union member data is a resource for both government investigators and hostile employers.

**The NLRB void and alternative enforcement mechanisms**: With the NLRB effectively non-operational in 2025–2026, unions facing employer surveillance and retaliation have fewer federal enforcement options. The practical alternatives: document every surveillance incident with dates, descriptions, and witnesses, building a legal record for future NLRB restoration or civil rights litigation; file state-level complaints where state labor law provides broader protections (California, New York, Illinois); and maintain relationships with labor-side employment attorneys who can bring unfair labor practice charges in anticipation of NLRB restoration.

**Cross-chapter and multi-local communications**: Large unions with multiple locals, chapters, or regions face the challenge of secure communications at scale. Wire's federated server architecture allows each local to host its own server while maintaining cross-chapter encrypted communications. Signal works for individual communications but does not provide the organizational control features needed for multi-chapter administration (removing compromised users, auditing membership, managing access). Wire Teams is appropriate at this scale.

**Legal defense fund**: Every labor union engaged in an active organizing drive should maintain a legal defense fund with a labor-side law firm on retainer. When employers use NLRB complaints, arbitration, or civil litigation as organizing suppression tools, the response timeline matters. A retainer relationship means same-day legal response rather than a week of searching for counsel.

### 3.3 Immigration Legal Service Organizations

**The attorney-client privilege calculation**: Attorney-client privilege is a legal defense, not a technical one. It protects communications from compelled disclosure but does not prevent subpoenas from being issued, does not prevent servers from being seized pending litigation, and does not protect information that was shared with third parties outside the privileged relationship. The practical implications: (a) client communications should be on platforms where the organization — not a commercial provider — controls the data (on-premises servers, or end-to-end encrypted platforms that cannot be compelled for content by a US court); (b) limit the number of people within the organization who have access to case-level client information to those with a professional need-to-know; (c) never store client-identifying information in systems that also store publicly accessible organizational information.

**FOIA request hygiene**: Attorneys should consult the ILRC guidance (2025): do not submit FOIA requests on behalf of clients with removal orders without explicit, informed client consent and a risk assessment. USCIS regularly shares FOIA request data with ICE. A FOIA submission intended to help a client can trigger enforcement action. This is a documented, current threat — not a theoretical one.

**IRS-ICE data sharing response**: The April 2025 MOU allows ICE access to IRS employer records for individuals with removal orders or under investigation. Immigration organizations that assist clients in navigating tax compliance (especially ITIN filers) should understand that this data is now accessible to ICE. Advice to clients should reflect this reality: ITIN filers' employer records are in ICE's potential reach under the MOU. This does not mean advising clients to avoid tax compliance — noncompliance creates worse legal exposure — it means ensuring clients understand the changed data landscape.

**Secure client intake protocol**: New client intake should occur through channels that do not create commercial platform records. The practical minimum: Signal for initial contact (a subpoena to Signal returns only account creation date and last connection time — it stores no message content). For document exchange: OnionShare (temporary .onion addresses, no central server to subpoena) or a self-hosted secure file transfer. For clients who cannot use Signal: ProtonMail, which cannot be compelled to produce email content. Never: client intake via Gmail, WhatsApp, or unencrypted SMS.

**Responding to office searches and device seizures**: Organizations should have a written legal protocol for responding to unexpected government visits, including: the right to ask to see a warrant before admitting government personnel; the right to call legal counsel immediately (do not wait); the right not to consent to searches beyond the scope of any warrant; the obligation to document what is being searched and seized (photograph visible warrant scope, inventory seized items); and the prohibition on obstructing lawful process. The National Immigration Law Center and ILRC maintain current guidance on responding to immigration enforcement at nonprofit offices.

**Sanctuary location data security**: For organizations that operate any form of emergency assistance for individuals seeking safety from enforcement: the physical location of a safe house or shelter must never appear in any administrative record. Review the ELITE data architecture (documented in `immigration-surveillance-evasion-playbook.md`): ELITE aggregates utility enrollment, Medicaid records, DMV address updates, and credit applications. Any administrative record created at a sensitive address begins contributing to ELITE's confidence scoring within days to weeks. A sanctuary location that appears in any administrative system is not, functionally, a sanctuary.

---

## Part 4: Governance and Operational Safeguards

### 4.1 Board-Level Security Governance

Cybersecurity for civil society organizations was assessed in the 2025 Okta "Nonprofits at Work" report as having made nonprofits the second-most targeted sector for cyberattacks, behind only the energy sector. Despite this, most nonprofit boards do not have a standing cybersecurity governance agenda item.

**Board minimum responsibilities**:
- Designate a board member with cybersecurity oversight responsibility (does not need to be a technical expert — the role is accountability, not implementation)
- Review the organization's security posture annually, with a report from the Executive Director on what threats the organization faces, what measures are in place, and what gaps remain
- Approve the incident response policy and legal counsel retainer
- Review any government legal process the organization has received (with legal counsel present)
- Understand the organization's cyber liability insurance coverage and its conditions

**Who on the board should know what**: Board members are not all equally positioned to hold sensitive information. Board members with access to donor identities, confidential strategy, or active legal matters should be limited to those with a genuine need-to-know for their board function. A board member who serves primarily on the finance committee does not need access to program case files. Compartmentalization at the board level is as important as at the staff level — a single board member's personal device compromise should not expose the entire organization's sensitive operations.

### 4.2 Document Classification Policy

A document classification policy does not require a government security clearance framework. For most civil society organizations, three categories are sufficient:

| Category | Description | Access | Storage |
|----------|-------------|--------|---------|
| **Public** | Content intended for public audience (website, publications, press releases, public Form 990) | Anyone | Standard organizational systems |
| **Internal** | Operational documents not intended for public view (board minutes, staff communications, organizational plans) | Staff and board per role | Encrypted organizational systems (cloud with MFA) |
| **Restricted** | Sensitive information where exposure causes direct harm (client case files, member Social Security numbers, confidential source identities, sanctuary location information, active legal strategy, donor information where disclosure creates risk) | Need-to-know basis only | Encrypted systems with access controls; key personnel only; logged access |

Assign document categories at creation. Establish a review cycle (annually) to assess whether restricted documents can be moved to lower categories or destroyed per the retention policy.

### 4.3 Membership Vetting and Infiltration Awareness

The FBI used infiltrators in 85% of domestic intelligence investigations during the COINTELPRO era. Modern informant use against activist and labor organizations is documented in the same 2020–2026 period. Infiltration is a real threat, not a paranoid one. The practical countermeasures are not about accusing members of being informants — they are structural controls that limit what any single member can expose.

**Structural infiltration resistance**:
- **Tiered access**: New members have access to public organizing activities. Access to sensitive planning discussions, internal strategy, membership contact lists, and financial information is earned over time and confirmed by existing trusted members.
- **Operational compartmentalization**: No single person should have knowledge of all active operations. Divide activities into working groups with limited cross-information-sharing. A meeting-planning team does not need to know who is managing the legal strategy.
- **Face-to-face for the most sensitive discussions**: Written communications, even encrypted ones, create records. The most sensitive strategic decisions should be made in person, without devices present. Devices should be in another room or in Faraday bags.
- **Be aware of provocateur patterns**: Agent provocateurs — infiltrators who push for illegal, violent, or legally risky activity — are documented in labor, climate, and civil rights organizing contexts. Organizations should have a clear policy that any member who consistently pushes for illegal activity, who seems interested in escalating tactics beyond the organization's stated mission, or who requests access to information beyond their legitimate role should be assessed as a potential infiltration risk.

### 4.4 Staff Onboarding and Security Culture

Security culture is the most effective long-term organizational security measure and the hardest to build. Technical controls fail when staff bypass them under time pressure; security culture makes the safe choice the default choice.

**Security onboarding components**:
1. **Threat model briefing**: Why does this organization face surveillance pressure? What specifically are the adversaries trying to obtain? What is the consequence of exposure for our clients/members? (Answer: real harm to real people, not abstract compliance failure.)
2. **Tool setup and verification**: Supervised installation of Signal (or Wire), password manager, MFA on all accounts, and full-disk encryption on their device — on their first day, not as a self-serve task.
3. **Incident reporting procedure**: Who do you call if your device is lost or stolen? If you receive a suspicious email? If law enforcement contacts you? Pre-save the incident commander's Signal username and personal phone number in their phone before they leave orientation.
4. **Device and account expectations**: Written policy on personal vs. organizational device use for sensitive work, approved cloud services, and the prohibition on client/member data in personal accounts.
5. **Legal rights briefing**: Staff who may encounter law enforcement — either at their home or in connection with organizational work — should know their rights. A one-page card with local legal support contacts (National Lawyers Guild, ACLU affiliate, legal defense fund retainer) should be part of orientation.

**Ongoing security culture maintenance**:
- Monthly 15-minute "security moment" at staff meetings: one current threat, one mitigation action
- Annual tabletop incident response exercise (what would we do if our email was compromised? If we received a subpoena?)
- Recognition that security failures are usually systemic, not individual — debrief failures without blame to identify and fix the systemic cause

---

## Part 5: Incident Response Playbook for Organizations

The `organizational-defense-playbook.md` provides a detailed technical incident response framework. This section supplements it with organization-specific considerations for government access events — the incident type most distinctive to the sectors covered by this playbook.

### 5.1 Government Legal Process Response

**Receiving a subpoena or government information demand**:

Do not comply before consulting legal counsel. Legal process — even a validly issued subpoena — is typically not self-executing. You have time to seek legal counsel and assess your options. The response timeline varies:
- Grand jury subpoena: compliance date stated in the subpoena, typically 14–30 days
- Administrative subpoena (DHS/ICE): compliance timeline may be shorter; some carry 10-day windows
- National Security Letter: carry gag orders that prohibit notification to the subject; legal counsel should assess challenge options under 18 U.S.C. § 3511

**Immediate steps on receiving legal process**:
1. Do not confirm or deny receipt to any party outside your legal team
2. Call legal counsel immediately — use your pre-established retainer if available, or the ACLU's legal intake line for civil liberties matters
3. Preserve all documents relevant to the legal process scope — do not destroy documents after receiving process, as destruction may constitute obstruction
4. Assess legal privilege: is the information sought covered by attorney-client privilege? Work product privilege? Is there a First Amendment privilege claim for journalist or advocacy organizations?
5. Assess challenge options: is the process valid? Can it be challenged as overbroad? Does it implicate protected First Amendment activity?

**Government personnel visiting your office**:

Training every staff member on this is as important as any technical control:
1. Do not consent to entry without a warrant. Ask to see the warrant and document its stated scope.
2. Call legal counsel immediately. Do not answer questions without counsel present.
3. Document everything: names and agency affiliations of agents, warrant number, scope of search, items seized. Photograph the warrant face and any seizure inventory.
4. Do not lie to federal agents. If you cannot safely answer a question without legal counsel, say: "I'm going to exercise my right to have an attorney present before answering any questions." This is your right and cannot be used against you.
5. Notify your incident commander and board chair immediately after the agents leave.

### 5.2 Data Breach Response

See `organizational-defense-playbook.md` for technical detail. The organization-specific supplements:

**Member and client notification requirements**: A data breach involving Social Security numbers, financial account information, or health information triggers mandatory notification obligations under state data breach laws (most states have them) and potentially HIPAA (for legal aid organizations that handle health information). Review your breach notification obligations within the first 48 hours of detecting a breach — most notification statutes have short windows (30–72 hours for some).

**Funder notification**: Major funders (foundations, government grants) typically have breach notification requirements in grant agreements. Review grant agreements within 48 hours and identify notification obligations. A direct phone call to major funders before they learn through press coverage is standard practice; it preserves the relationship and demonstrates good faith.

**Community trust recovery**: For organizations serving vulnerable communities, a data breach is not merely a technical event — it is a betrayal of trust that the community extended in a context of significant power imbalance. Members who were enrolled in a union drive, clients who shared immigration case information, or donors who gave to a cause under political attack all trusted the organization with sensitive information. Recovery of community trust requires: (a) transparent, honest disclosure of what happened; (b) specific, verifiable remediation steps; (c) accountability from leadership (not just from IT staff); and (d) demonstrated structural changes, not just communications about changes.

---

## Part 6: Implementation Roadmap

### Months 1–2: Essential Baseline

Regardless of organizational size, the first 60 days should focus on completing all Tier 1 measures. The highest-priority actions in sequence:

**Week 1**:
- Apply for Cloudflare Project Galileo (free, no reason to delay)
- Enforce MFA on all organizational accounts
- Deploy a shared password manager
- Move all sensitive staff communications to Signal or Wire

**Week 2–3**:
- Conduct access review for all sensitive systems
- Configure disappearing messages on sensitive channels
- Enable full-disk encryption on all staff devices
- Enable registrar lock and hardware key MFA on domain registrar account

**Week 4–6**:
- Complete staff security onboarding (all current staff, not just new hires)
- Document the data classification policy
- Establish the out-of-band communication channel
- Designate incident commander and provide them with legal counsel contact information

**Week 7–8**:
- Conduct vendor security assessment for top 3 vendors handling sensitive data
- Implement data minimization — delete what you don't need
- Draft the government legal process response protocol (designating legal counsel, establishing board notification chain)
- First tabletop exercise: "what would we do if we received a subpoena tomorrow?"

### Months 3–6: Advanced Hardening

- Deploy Wire or Element for organizational communications (if Signal is insufficient for your organizational control needs)
- Complete Swiss-jurisdiction or EU-hosted migration for most sensitive data categories
- Complete sector-specific implementation (Section 3 above, as relevant to your sector)
- Establish or expand legal defense fund retainer relationship
- Complete Tier 2 infrastructure hardening (DNSSEC, vendor assessments, backup strategy)

### Months 7–12: Sustaining and Testing

- First annual security review at board level
- Annual access review cycle
- Penetration test by external security firm (optional but recommended for Tier 2+ organizations)
- Update incident response protocol based on tabletop exercise findings
- Expand security culture training to all staff, volunteers, and contractors

---

## Part 7: Resource Directory

### Free and Low-Cost Tools

| Category | Tool | Cost | Link |
|----------|------|------|------|
| Web protection | Cloudflare Project Galileo | Free for qualifying orgs | [cloudflare.com/galileo](https://cloudflare.com/galileo) |
| Encrypted messaging | Signal | Free | [signal.org](https://signal.org) |
| Organizational messaging | Wire (Teams) | $4/user/month | [wire.com](https://wire.com) |
| Password manager | Bitwarden Teams | $3/user/month | [bitwarden.com](https://bitwarden.com) |
| Encrypted email | ProtonMail | Free–$10/month | [proton.me](https://proton.me) |
| Encrypted file storage | Tresorit | $10/user/month | [tresorit.com](https://tresorit.com) |
| Secure document sharing | OnionShare | Free | [onionshare.org](https://onionshare.org) |
| TOTP authenticator | Ente Auth | Free | [ente.io/auth](https://ente.io/auth) |
| Hardware security key | YubiKey | $25–$50 per key | [yubico.com](https://yubico.com) |
| VPN (no-log, no-identity) | Mullvad | $5/month | [mullvad.net](https://mullvad.net) |
| Board governance portal | BoardEffect or OnBoard | Varies | (multiple vendors) |

### Emergency Support

| Organization | Services | Contact |
|----------|---------|---------|
| Access Now Digital Security Helpline | Free emergency digital security assistance for civil society | [accessnow.org/help](https://accessnow.org/help) |
| Freedom of the Press Foundation | Digital security for press-adjacent organizations | [freedom.press](https://freedom.press) |
| CyberPeace Institute | Cybersecurity support for NGOs and humanitarian organizations | [cyberpeaceinstitute.org](https://cyberpeaceinstitute.org) |
| Electronic Frontier Foundation | Legal support and security guidance | [eff.org](https://eff.org) |
| National Lawyers Guild | Legal support for activists and labor organizers | [nlg.org](https://nlg.org) |
| ILRC (Immigration) | Immigration legal aid security guidance | [ilrc.org](https://ilrc.org) |
| Government Accountability Project | Whistleblower legal support | [whistleblower.org](https://whistleblower.org) |

### Training and Consulting

- **Front Line Defenders**: Security training for human rights defenders at risk; free for qualifying organizations
- **Access Now Digital Security Helpline**: Incident response, training, and consultation
- **Security Education Companion (EFF)**: Free security training curriculum for organizations training their own staff
- **NTEN Cybersecurity Resource Hub**: Practical nonprofit cybersecurity guidance

---

## Part 8: Confidence Assessment and Evidence Gaps

**High confidence** (multiple primary sources, documented cases):
- Government legal process threats (administrative subpoenas, FOIA, NSLs) — confirmed with multiple documented cases
- IRS political targeting trajectory — confirmed via WSJ reporting, Presidential Memorandum, IRS LCA documentation
- DDoS and web attack volume against civil society — confirmed with Cloudflare Project Galileo primary data
- NLRB deterioration and labor organizing suppression — confirmed via NLRB data and CAP analysis
- ICE Graphite spyware capability and deployment — confirmed via ICE acting director's written response to Congress
- Employer surveillance during organizing drives — documented in multiple specific cases (Amazon, Google)
- Supply chain vulnerability (MOVEit case) — fully documented

**Medium confidence** (reported via journalism, not independently confirmed in primary sources):
- Scope of active FBI informant programs in current organizing contexts — extensive historical documentation, but current scope not independently verifiable
- ICE Graphite deployment against US-based civil society organizations specifically — WhatsApp's 2025 disclosure covers international civil society; US-specific deployment acknowledged but not confirmed at scale
- Specific organizational targeting under the September 2025 Presidential Memorandum — the Memorandum itself is confirmed; specific operational targeting under it is not yet documented

**Evidence gap requiring further research**:
- Effective technical countermeasures against zero-click spyware at the organizational scale (Graphite/Paragon) — individual countermeasures documented (Lockdown Mode, GrapheneOS, aggressive patching), but organizational deployment patterns for these countermeasures are not yet well-documented
- Practical federated Element/Matrix deployment at multi-chapter union scale — limited documented case studies for US labor unions specifically

---

## Cross-References

- For individual staff security measures applicable at all tiers: `opsec-playbook.md`
- For supply chain and technical infrastructure attacks in depth: `organizational-defense-playbook.md`
- For immigration attorney-specific implementation steps: `immigration-attorney-implementation-guide.md`
- For activist organizing and protest-specific guidance: `activist-organizing-playbook.md`
- For the complete government surveillance threat model: `threat-model.md` and `palantir-threat-model.md`
- For sector-specific distribution contacts: `tier-2-sector-contact-lists.md`

---

## Sources

- [Cloudflare — Celebrating 11 Years of Project Galileo's Global Impact](https://blog.cloudflare.com/celebrating-11-years-of-project-galileo-global-impact/)
- [SiliconANGLE — Cloudflare sees massive rise in attacks targeting media, nonprofits and human rights groups](https://siliconangle.com/2025/06/12/cloudflare-sees-massive-rise-attacks-targeting-media-nonprofits-human-rights-groups/)
- [Dianova / SecureWorld — Cybersecurity for NGOs in 2026: from Digital Fragility to Cyber Resilience](https://www.secureworld.io/industry-news/cybersecurity-for-ngos-in-2026)
- [Al Jazeera — FBI cuts ties with civil rights watchdog SPLC after conservative pressure](https://www.aljazeera.com/news/2025/10/3/fbi-cuts-ties-with-civil-rights-watchdog-splc-after-conservative-pressure)
- [NPR — DOJ indicts Southern Poverty Law Center on federal fraud charges](https://www.npr.org/2026/04/22/nx-s1-5794620/doj-indicts-southern-poverty-law-center-on-federal-fraud-charges)
- [The Intercept — FBI counterterrorism agents visited Extinction Rebellion member](https://theintercept.com/2026/02/12/fbi-counterterror-extinction-rebellion/)
- [TechCrunch — DHS subpoenas to unmask anti-ICE accounts](https://techcrunch.com/2026/02/14/homeland-security-reportedly-sent-hundreds-of-subpoenas-seeking-to-unmask-anti-ice-accounts/)
- [NPR — ICE acknowledges it is using Graphite spyware](https://www.npr.org/2026/04/07/nx-s1-5776799/ice-spyware-privacy)
- [Business and Human Rights Centre — Lawmakers warn about ICE's access to Graphite spyware](https://www.business-humanrights.org/en/latest-news/lawmakers-ring-the-alarm-about-ices-potential-to-abuse-graphite-spyware/)
- [Charity Lawyer Blog — The Rising Politicization of the Nonprofit Sector in 2025](https://charitylawyerblog.com/2025/12/01/the-rising-politicization-of-the-nonprofit-sector/)
- [TNPA — 2025 Nonprofit Policy Moments and a 2026 Look Ahead](https://tnpa.org/2025-nonprofit-policy-moments-and-a-2026-look-ahead/)
- [Center for American Progress — NLRB-Overseen Union Elections Fell in 2025](https://www.americanprogress.org/article/nlrb-overseen-union-elections-fell-in-2025-amid-trump-administration-attacks/)
- [The Regulatory Review — Regulating Digital Surveillance of Workers](https://www.theregreview.org/2026/04/28/basila-regulating-digital-surveillance-of-workers/)
- [UC Berkeley Labor Center — Union Rights and Employer Obligations for Monitoring and Surveillance](https://laborcenter.berkeley.edu/negotiating-tech/governance-of-workplace-technology-applications/electronic-monitoring-and-surveillance-regulations/)
- [EFF — How Cops Are Using Flock Safety to Surveil Protesters and Activists](https://www.eff.org/deeplinks/2025/11/how-cops-are-using-flock-safetys-alpr-network-surveil-protesters-and-activists/)
- [Union Impact — Data Security for Unions: What You Need to Know in 2025](https://unionimpact.com/blog/data-security-for-unions-what-you-need-to-know-in-2025/)
- [Reason — Civil Liberties Groups Sue for Information on ICE's Speech-Chilling Subpoenas](https://reason.com/2026/04/24/civil-liberties-groups-sue-for-information-on-ices-speech-chilling-subpoenas/)
- [ILRC — Attacks on FOIA Continue](https://www.ilrc.org/resources/attacks-foia-continue)
- [National Immigration Forum — IRS and ICE Immigration Data-Sharing Agreement Explainer](https://forumtogether.org/article/irs-ice-immigration-data-sharing-agreement-explainer/)
- [Wire — Signal Attacks Explained: Securing Messages vs Members](https://wire.com/en/blog/signal-attacks-securing-messages-vs-members)
- [Wire — Best Secure Communication Platforms for Enterprises (2026 Guide)](https://wire.com/en/blog/best-secure-communication-platforms-enterprises)
- [ACLU — History Shows Activists Should Fear the Surveillance State](https://www.aclu.org/news/national-security/history-shows-activists-should-fear-surveillance)
- [CyberPeace Institute — Actionable Cybersecurity for NGOs](https://nonprofitcyber.org/actionable-cybersecurity-for-ngos-the-stories-of-the-heroes-safeguarding-those-who-safeguard-us/)
- [Access Now — Digital Security Helpline](https://www.accessnow.org/help/)
- [FEMA — Nonprofit Security Grant Program FY2025](https://www.fema.gov/grants/preparedness/nonprofit-security)
- [Okta — Nonprofits at Work 2025 (cited in nonprofit cybersecurity coverage)]
- [Georgetown Law Poverty Journal — Labor Organizing and AI Surveillance in the Workplace](https://www.law.georgetown.edu/poverty-journal/blog/labor-organizing-and-ai-surveillance-in-the-workplace/)

---

*Research conducted May 2026. Confidence level: high on documented cases and confirmed capabilities; medium on current operational scope of active government informant programs. Next update checkpoint: July 2026, concurrent with Phase 2 quarterly review.*
