---
title: "Organizational OpSec Playbooks: Infrastructure Security for NGOs, Unions, Legal Services, and Academic Institutions"
project: cybersecurity-hardening
created: 2026-05-06
status: phase-2-guidance
phase: Phase 2 — Organizational Expansion
session: 847
depends_on:
  - threat-model.md
  - PHASE_2_SEQUENCING_STRATEGY.md
  - opsec-playbook.md
  - implementation-guide.md
  - palantir-threat-model.md
confidence: high — threat model grounded in documented government surveillance (ELITE, Palantir Foundry contracts, IRS LCA financial social graph mapping, DOGE cross-agency data fusion, Mobile Fortify field deployment), FBI biometric expansion, DHS HART platform, plus organizational-specific threats (employer surveillance for labor, intimate partner monitoring for DV organizations, ICE data-sharing requests for legal services)
audience: NGO/nonprofit directors and IT staff, labor union organizing departments and leadership, legal aid organizations and immigration attorneys, academic institution security officers and faculty leadership
---

# Organizational OpSec Playbooks: Security Infrastructure for At-Risk Organizations

**Executive Summary**: This document extends the Phase 2 cybersecurity-hardening corpus from individual-focused playbooks to organizational contexts. Organizations serving at-risk populations (undocumented immigrants, activists, survivors of violence, workers in organizing drives) face compound threat surfaces: they must protect (1) their own infrastructure and data, (2) their staff from targeting by federal agencies and other adversaries, and (3) their clients/members from surveillance that flows through organizational systems. This document provides four scenario-specific playbooks addressing governance, staff safety, data compartmentalization, and legal compliance for organizations operating under intensive government surveillance.

Each playbook is designed for organizational leadership and IT teams to implement over 4–12 weeks, with immediate wins in Weeks 1–2 and structural hardening in subsequent phases.

---

## PLAYBOOK 1: Nonprofits and NGO Infrastructure Security

### 1.1 Target Audience and Threat Profile

**Target audience**: Directors, board chairs, IT staff, and finance teams at NGOs and nonprofits serving politically sensitive populations (immigration rights, civil rights, environmental justice, labor advocacy). This includes legal aid organizations, community healthcare providers, housing nonprofits, and mutual aid networks.

**Organizational threat profile specific to this context**:

NGOs face surveillance that targets them at three distinct levels:

1. **Institutional targeting**: IRS LCA platform social-graph mapping treats financial relationships between organizations as investigation leads. If your organization's bank accounts show regular transfers with an entity under investigation (another NGO, a movement network, a foreign-based human rights organization), your organization enters the social graph of that investigation. This is documented in `palantir-threat-model.md` and confirmed in SPLC litigation.

2. **Board and leadership targeting**: Board members and executive directors of civil rights organizations are subjects of FBI intelligence investigations under the guise of "First Amendment monitoring." COINTELPRO is officially over, but FBI field offices continue to maintain subject files on civil rights leaders. This is documented in "Safeguarding Civil Rights Groups" (EFF/CACI) and confirmed in FOIA releases through 2025.

3. **Staff and client intersection**: Staff members become potential investigation subjects based on their organizational affiliation alone. This is compounded by the fact that staff who work with vulnerable populations (undocumented immigrants, welfare recipients, unhoused individuals) often live in high-enforcement contexts themselves. A staff member's personal data (address, phone number, financial accounts) can become a surveillance anchor for the organization as a whole.

Additional threat: some NGOs receive ICE data-sharing requests and subpoenas seeking information about clients. A subpoena to an immigration legal aid organization seeking client records is a federal pressure point that requires legal preparation and infrastructure that most nonprofits do not have.

---

### 1.2 Governance-Level Protections

**Establish a "Sensitive Operations" governance framework**:

Organizations serving politically sensitive populations should establish a formal governance structure around sensitive client and operational data. This is not only good security — it is good nonprofit governance.

*Board-level cybersecurity committee*: Establish a standing subcommittee of the board (or full board if small) responsible for oversight of client data security, cybersecurity incidents, and legal data-handling obligations. Quarterly meeting minimum. The committee should include at least one board member with cybersecurity or legal background, but this should not be the only criterion — the committee should include persons representing the client/member base, to ensure that security decisions account for their vulnerability.

*Data classification policy*: Establish a classification system for your organization's data:
- **Level 1 (Public)**: Donor lists not linked to organization operations, aggregate program statistics, organizational website content
- **Level 2 (Internal)**: Staff directories, financial statements, strategic plans
- **Level 3 (Sensitive)**: Client personally identifiable information (PII), health records, legal case details, internal vulnerability assessments, government correspondence
- **Level 4 (Legal Hold)**: Records subject to litigation, FOIA requests, or subpoena holds

Each level should have explicit data retention, encryption, and access control requirements. Level 3 and 4 data requires:
- Encryption at rest (full-disk encryption on all devices; encrypted database with access key stored separately)
- Encryption in transit (HTTPS/TLS for all data movements; encrypted email for inter-organizational communication)
- Access logging (who accessed what data, when, for what purpose)
- Retention minimization (legal hold policies; destroy data when retention period expires)

*Subpoena response protocol*: Establish a written protocol for responding to government information requests. This is not optional — it is a legal exposure point. The protocol should:
1. Immediately notify your organization's general counsel (or outside counsel if you do not have in-house legal)
2. Freeze all data destruction processes for the category of data requested (even if your retention policy would normally delete it)
3. Do not respond directly to subpoenas — let counsel review and negotiate scope before responding
4. Document all communications with law enforcement in a dedicated file
5. Notify your board and any oversight body (depending on your legal context) of subpoena receipt

Organizations serving immigration populations should expect ICE subpoenas for client information. Litigation around these subpoenas (particularly around First Amendment attorney-client privilege) is active but uncertain. Counsel can advise on assertion of privilege and scope negotiation, but your organization must have a protocol in place before a subpoena arrives.

*Board confidentiality structure*: Board conversations are often not privileged unless the organization has an established attorney-client relationship through board counsel. This creates a vulnerability: if board members' emails are subpoenaed, all board discussions may be discoverable. Mitigate this by:
1. Ensuring an attorney is present for board meetings (or available for consultation) so that communications can be attorney-client privileged
2. Separating operational board discussions from strategic/legal discussions; mark attorney-related discussions as "prepared under attorney direction for litigation strategy" to create privilege claims
3. Using Signal or encrypted email (not Gmail/Outlook which are cloud-based and potentially accessible to subpoena) for sensitive board communication

---

### 1.3 Staff and Volunteer Safety

**Personal security screening for staff in high-risk roles**:

Staff and volunteers who work directly with vulnerable populations or handle sensitive data should undergo basic personal security assessment:

1. *Device security baseline*: All staff handling Level 3 and 4 data should use:
   - Full-disk encrypted laptops (FileVault on Mac, BitLocker on Windows, LUKS on Linux)
   - Work phones running GrapheneOS (Android) or hardened iOS
   - No work data stored on personal devices unless encrypted and segregated

2. *Work-personal separation*: Staff should not use personal email accounts for work communications, even if remote. This prevents data breaches in your organization from exposing their personal identity, and prevents their personal adversaries (abusive partners, creditors, etc.) from gaining access to organizational data.

3. *Address privacy and home security*: Staff working with enforcement-vulnerable populations should understand that their home address, if exposed, becomes an enforcement target anchor. Some organizations offer staff the option to use the organization's address for:
   - Voter registration (if not already registered)
   - Business licensing (if staff run any personal businesses)
   - Court filings and legal documents
   
   This is a sensitive balance — staff privacy should be preserved — but staff should have the option to compartmentalize their home identity from their work identity.

4. *Threat briefing for staff with field exposure*: Staff who meet directly with clients or work in field environments should receive training on:
   - Recognition of Mobile Fortify and other biometric scanning
   - De-escalation if approached by federal agents
   - Emergency contact protocol for legal support
   - What to do if they believe they are under investigation

---

### 1.4 Financial Account Compartmentalization

**Operational and sensitive-work financial separation**:

IRS LCA financial social-graph mapping creates a permanent record of financial relationships between organizations. This is not stoppable, but it can be minimized.

*Donor privacy*: For organizations that wish to protect donor privacy:
1. Encourage donors to give through fiscal sponsors (a 501(c)(3) organization that receives funds on behalf of your organization). This legal technique breaks direct donor-to-organization financial records visible in the IRS pipeline.
2. For in-kind donations, maintain separate records systems for donors who wish to remain anonymous. Store these records separately from your financial system (encrypted, on-site, not in cloud accounting software where they may be more discoverable).

*Operational accounts*: Organizations should maintain clear separation between:
- **Grant management accounts**: For government grants and formal funding relationships (visible and intended to be visible)
- **Donor accounts**: For individual and foundation donations (appropriate for privacy but auditable)
- **Operations accounts**: For day-to-day expenses, staffing, client services (necessary for audit but not sensitive)

Do not commingle these. If your grant is from federal sources (HHS, DoJ, etc.), that account is not private — it is accessible to other federal agencies. Keep grant-funded operations separate from sensitive client services where operationally possible.

---

### 1.5 Technology and Data Infrastructure

**Email and communications security**:

1. *Organization email*: Move away from Gmail/Outlook if possible. These cloud-based systems are accessible to subpoenas and are not organizationally owned. Options:
   - Self-hosted email using ProtonMail for Business (encrypted, but cloud-based) or Tutanota
   - Self-hosted using an email server on your organization's own infrastructure (requires IT support but is under your control)
   
   At minimum, ensure that email backup is encrypted and stored separately from live email.

2. *Encrypted messaging for sensitive coordination*: Signal for groups with <500 members. Matrix/Element for larger internal communications. Do not use Slack, Teams, or Discord for sensitive organizational communication — these are US-based commercial platforms with known government access agreements.

3. *Client intake and document handling*: For organizations that collect sensitive client information:
   - Use encrypted forms (encrypted Google Forms, Typeform with HTTPS only, or self-hosted encrypted form software)
   - Store collected data in an encrypted database with access controls
   - Have a data deletion protocol — when a case closes or a client leaves your organization, explicitly delete their data rather than archiving indefinitely

---

### 1.6 Cyber Insurance and Incident Response

**Cyber incident response plan**:

Organizations should have a written incident response plan that includes:
1. Incident detection: how will you know if you have been compromised? (IDS monitoring, unusual account activity alerts, etc.)
2. Containment: how will you isolate the breach and prevent further damage?
3. Investigation and notification: how will you determine what was accessed and who to notify?
4. Recovery: how will you restore systems?
5. Legal notification: does your state law require notification to affected individuals? Does your federal funding require notification to government agencies?

Organizations handling federal data or federal grants often have government reporting requirements — these should be in your plan in advance, not discovered during the incident.

**Cyber insurance**: Organizations should carry cyber insurance that covers data breach response costs, regulatory fines, and legal fees. This is increasingly available to nonprofits, often at subsidized rates through nonprofit consortia.

---

## PLAYBOOK 2: Labor Union Organizing and Encrypted Coordination

### 2.1 Target Audience and Threat Profile

**Target audience**: Union organizing departments, rank-and-file organizers, union IT staff, and labor legal teams. This includes both traditional labor unions (AFL-CIO affiliates, SEIU, UFW) and worker-led organizing networks (independent shops, Amazon warehouse organizing, gig worker networks).

**Organizing-specific threat profile**:

Labor unions face surveillance from three primary threat sources:

1. **Employer surveillance**: Workplace monitoring software is ubiquitous. Employees suspected of organizing are subject to keystroke logging (software like ActivTrak, Teramind), email monitoring, productivity analytics (Hubstaff, Time Doctor), and device management software that can remotely wipe devices. The threat is escalation: if organizing is detected, retaliation (firing, blacklisting) follows swiftly. Federal protections exist (NLRA 29 U.S.C. § 157) but enforcement is slow. The organizing window may close before legal remedies attach.

2. **Government financial investigation**: IRS LCA platform has explicitly documented shift toward investigating "left-leaning groups." Union financial accounts, especially those handling strike funds or solidarity networks, are in the social-graph scope of the IRS targeting infrastructure. FOIA requests from the Government Accountability Project confirm that IRS investigations of union organizations accelerated substantially between 2024 and 2026.

3. **Employer+government coordination**: In some cases, employers have shared surveillance data with federal agencies (Palantir customer instances at DHS, ICE, CBP include private employer-sourced data streams). A union organizing drive at an employer with ICE contracts or DHS vendor status puts organizers at elevated risk of biometric identification and immigration-specific targeting.

*New 2026 threat addition*: USDA's Palantir contract includes a $75M "workforce surveillance" component for return-to-office compliance monitoring with real-time analytics. This establishes precedent that federal agencies will contract for private-sector workforce surveillance feeds. Federal contractors with union organizing are particularly exposed.

---

### 2.2 Organizing Structure and Compartmentalization

**Three-layer organizing communication architecture**:

Effective organizing requires three distinct communication layers, each with different security properties:

*Layer 1 — Public messaging*: Organizing announcements, strike updates, public call-outs. Use:
- Signal groups (public channels, or groups with 50+ members where anonymity is less feasible)
- Organizational social media accounts (Facebook, X, TikTok) with maximum privacy controls
- Printed materials (flyers, newsletters) for in-person distribution

This layer is intentionally visible. The threat here is not secrecy — it is preventing Babel Street OSINT from building behavioral patterns about individual organizers. Guidance from the activist playbook (Part 2) applies: set accounts to private, review posts 72 hours before actions, avoid identifying individual organizer locations.

*Layer 2 — Closed organizing coordination*: Meetings, tactic decisions, support structure. Use:
- Signal groups with maximum 20–30 core organizers (verified members, in-person vetting required for new additions)
- In-person meetings for sensitive decisions (no digital record)
- Encrypted mailing lists (using SecureDrop server software or similar) for announcements to 50–500 people

This layer should have disappearing messages enabled and no member directories accessible to outsiders.

*Layer 3 — Leadership security and escalation*: Decisions about legal exposure, threat assessment, resource allocation. Use:
- Face-to-face meetings only
- Encrypted phones (GrapheneOS, hardened iOS) for any remote discussion
- Physical security protocols for locations where organizing leadership meets (secure meeting spaces, counter-surveillance awareness)

The critical vulnerability in most unions is conflation of layers: organizers post about their organizing role on personal social media (Layer 1 information on a personal channel), then discuss strategy in Signal groups with overlapping membership. This links the personal identity to the organizing coordination. Prevent this through explicit policy: organizing discussions use dedicated organizing accounts/channels; personal social media is personal.

---

### 2.3 Rank-and-File Safety and Device Security

**Organizing-specific device hardening**:

For rank-and-file workers participating in organizing drives, especially workers in dangerous industries or with immigration vulnerability:

1. *Work device security*: Devices issued by the employer are surveilled. Period. Do not assume any privacy:
   - Organize using personal devices only
   - Do not access organizing communications on work devices
   - Assume all work computer activity is logged and may be shared with law enforcement

2. *Personal device hardening for organizers*: Workers in active organizing campaigns should:
   - Use GrapheneOS (Android) for organizing communication
   - Use Signal (with disappearing messages, not SMS fallback) for coordination
   - Use VPN for any organizing-related internet access from work or locations near work
   - Disable location services on phones used for organizing

3. *Burner device for elevated-risk organizing*: For workers in organizing roles who face high retaliation risk (documented prior terminations, visible leadership role, employer has history of aggressive response), maintain a dedicated organizing phone:
   - Purchased with cash, from a store not near home or work
   - Activated on a prepaid plan not linked to identity
   - Used exclusively for organizing communication
   - Powered off and stored in Faraday bag when not in use

---

### 2.4 Financial Security and Solidarity Networks

**Strike fund and solidarity network financial compartmentalization**:

Strike funds and solidarity networks that move money to support workers face IRS scrutiny and employer legal attacks. Financial infrastructure should be hardened:

1. *Strike fund architecture*:
   - Use a dedicated bank account for strike funds (do not commingle with union general operating accounts)
   - Establish explicit documentation that fund is for strike support (workers' legal right under NLRA) and record the legal authority
   - Maintain clear records of distributions to striking workers (legal defense of strike fund)
   - Consider using a fiscal sponsor organization (501(c)(3) fund) that receives and disburses strike funds on behalf of the union, breaking direct union-to-workers financial chains

2. *Solidarity network cryptocurrency (if used)*:
   - Monero is more private than Bitcoin but remains vulnerable at entry/exit points (exchanges). If your union accepts crypto donations, use Monero with the explicit understanding that any funds that have touched a regulated exchange with KYC data create a link to that exchange customer.
   - Do not accept crypto donations unless you have a plan for converting them to cash (or using them directly for purchases) without exchange KYC linking.

3. *Physical cash protocols*:
   - Cash strike support leaves no financial record. For informal worker networks and rank-and-file support, physical cash networks funded by individual worker donations are the most financially private approach.
   - Establish protocols for cash handling: dedicated persons who hold strike funds, documented distribution lists, destroyed records after strike ends (unless you need to retain for legal defense).

---

### 2.5 Legal Preparation and Government Pressure Response

**Pre-strike legal infrastructure**:

Before any strike or major organizing action:

1. *Retain external counsel*: Do not rely on internal union legal staff for adversarial government interaction. Hire external labor counsel (ILG, PLF, local labor lawyers) to represent the union in government proceedings. This maintains attorney-client privilege for all interactions with that counsel.

2. *FOIA readiness*: Before any action, assume that the IRS, FBI, DOJ, and potentially ICE will FOIA your communications. What would be damaging if made public? Have counsel advise on what communications should be privileged, and which should not be memorialized at all.

3. *Retaliation documentation protocol*: If workers face retaliation (firing, blacklisting), document everything. Coordinated retaliation across multiple employers in an industry can constitute ULP (unfair labor practice) under NLRA, but documentation must be contemporaneous. Implement a retaliation reporting system:
   - Secure form (encrypted, no identifying IP) for workers to report retaliation
   - Lawyer review of reports (creates attorney-client privilege)
   - Aggregated analysis for NLRB charges and litigation

4. *Security clearance for immigrant workers*: Workers in organizing who are undocumented or have immigration vulnerabilities should be counseled by immigration legal staff:
   - What information should never be shared with law enforcement (certain visa categories, past entries, family structure)
   - What rights they have (right to remain silent, right to refuse search, right to have an attorney present) regardless of immigration status
   - What protections exist (TPS holders have specific workplace rights; U visa victims have specific protections)

---

### 2.6 Post-Strike Financial and Reputational Recovery

**Operational security after strike/campaign ends**:

After a major campaign:

1. *Financial account cleanup*: Close dedicated strike fund accounts, consolidate temporary coordination accounts, archive and encrypt sensitive communications. Do not delete anything until litigation is clearly over and limitations periods have passed.

2. *Member communication about surveillance*: Acknowledge to members that organizing activity has likely generated government attention (IRS investigation, FBI file, possible ICE targeting of immigrant members). Provide resources:
   - Immigration legal clinic contacts
   - Information about FOIA requests members can file to see what government has on them
   - Guidance on ongoing security practices as organizing intensity winds down but the organization's political exposure remains

3. *Ongoing external threat monitoring*: Subscribe to notifications from organizations that track government contractor activity (CACI Insider Threat, DigitalGlobe contractor activity, etc.). If your industry's major employers take on government contracts that involve worker surveillance, your membership should know it.

---

## PLAYBOOK 3: Legal Service Providers and Immigration Attorneys

### 3.1 Target Audience and Threat Profile

**Target audience**: Immigration attorneys, legal aid organizations, public defender offices, civil rights law clinics, pro bono networks, and paralegal staff. This includes solo practitioners, law firm immigration departments, and law school clinical programs.

**Legal services-specific threat profile**:

Legal service providers face a distinct and acute threat: their client files are the target.

1. **Subpoena and government access to client files**: ICE, CBP, and DHS routinely issue subpoenas to immigration attorneys and legal aid organizations seeking client information. The stated purpose is law enforcement — identifying allegedly deportable aliens — but the structural effect is to turn the legal system itself into a reporting infrastructure. Attorneys have attorney-client privilege and work product doctrine, but these are not impenetrable:
   - Subpoenas that meet "reasonable particularity" can compel production of file documents
   - In some cases, federal courts have found that metadata (client names, appointment dates, document names) itself is discoverable even when document contents are privileged
   - Prosecutors have obtained warrants to search attorney offices (Giuliani's office in April 2021 was a high-profile case, but similar searches occur regularly against civil rights attorneys)

2. **Physical surveillance of attorneys and clients**: LAPD drone surveillance includes the ACLU Los Angeles office building (documented in the aerial surveillance investigative reporting). Attorneys working with immigration and civil rights clients should assume their office buildings are in the surveillance perimeter and that arriving clients are being documented.

3. **The parallel construction risk**: Even if an attorney successfully asserts privilege and refuses to produce client files, ICE can initiate enforcement action against the client using information obtained through other means (ALPR, biometric identification, community tips), and then "parallel construct" a case that conceals the actual intelligence source (attorney communications). An attorney's refusal to cooperate does not prevent enforcement; it only limits the evidence available to the government's case.

---

### 3.2 File Security and Data Architecture

**Privilege-aware file systems**:

Legal files contain attorney-client privileged information and should be treated with the highest security standard:

1. *Physical file security*:
   - Maintain separate file systems for different client matters. Do not comingle clients' files.
   - Store client files in a secure location (locked cabinet, locked room, or locked building section) with access limited to attorneys and essential staff.
   - For files under litigation hold or subpoena risk, maintain a separate secure storage with audit logging.
   - Maintain file access logs: who accessed which files, when, for what purpose.

2. *Digital file security*:
   - All client files (intake forms, correspondence, pleadings, legal memoranda) must be encrypted at rest.
   - Use full-disk encryption on all attorney and paralegal computers.
   - Use encrypted email (ProtonMail, Tutanota, or Tresorit) for any client communication that goes outside the office (do not send client information via Gmail or Outlook).
   - If cloud-based file storage is used (Dropbox, Google Drive, Box), ensure files are encrypted at the client level before uploading, and ensure the encryption key is not stored with the files.
   - If self-hosted file storage is used, maintain regular encrypted backups in a geographically separate location.

3. *Client intake privacy*:
   - Use encrypted intake forms with HTTPS-only access.
   - Store intake information separately from correspondence files.
   - Have explicit client consent forms that explain what data you collect, how it is stored, and what government requests you may receive.

---

### 3.3 Subpoena Response and Government Requests

**Formalized subpoena response protocol**:

Attorneys should have a written, practiced protocol for responding to government information requests:

1. *Immediate protocol upon subpoena receipt*:
   - Do not respond directly
   - Notify all implicated clients immediately (they may have independent privilege claims)
   - Freeze all file destruction for affected matters
   - Consult with outside counsel specializing in government requests (if you do not have this expertise in-house)
   - Document the subpoena, the scope, and all internal communications in an attorney file (separate from client files, marked as attorney work product)

2. *Privilege assertion and negotiation*:
   - In federal cases, file a motion to quash or limit the subpoena within the specified timeframe. Do not assume that privilege will be clear from default — force the government to justify the narrowness of its request.
   - For immigration subpoenas specifically, the courts have developed some (limited) precedent requiring government to demonstrate that:
     - The information sought is relevant to a specific investigation
     - The information cannot be obtained through other means
     - The scope is narrowly tailored to what is actually needed
   These are not full protections, but they are negotiation points. Counsel should use them.

3. *Production strategy*:
   - If privilege cannot be fully asserted, produce only non-privileged documents (factual information that is not work product).
   - For metadata (client names, appointment dates), argue that this information is itself work product if it reveals the attorney's investigation strategy.
   - Consider seeking a protective order that limits government use of produced information and requires destruction at the end of the case.

4. *Client notification*:
   - Notify affected clients that information about them has been produced (or withheld on privilege grounds).
   - If information was produced, explain what was produced and any protective orders that limit government use.
   - Advise clients of their rights (what to do if they are subsequently contacted by agents, etc.).

---

### 3.4 Staff and Paralegal Safety

**Personal security for legal staff**:

Paralegals and legal support staff often handle sensitive client information without attorney protections. They face distinct risks:

1. *Device security for paralegal staff*:
   - Work devices should be fully encrypted and password-protected
   - Personal devices should never be used for work communications
   - Paralegals should have clear guidance on what client information can be discussed with whom (confidentiality training)
   - Email access should use multi-factor authentication

2. *Personal security concerns*:
   - Paralegals working with immigration clients may themselves be vulnerable to immigration enforcement. Organizations should be prepared to:
     - Adjust work schedules to avoid peak enforcement times
     - Provide immigration legal consultation to staff members who are concerned about their own status
     - Offer emergency support (legal funds, community defense networks) if staff face enforcement action

3. *Background vulnerability assessment*:
   - Staff with documented prior legal issues, immigration vulnerability, or other factors that could be used as leverage should understand the risks of working with sensitive client data
   - Organizations should provide support (legal representation, financial assistance for resolution of prior issues, security guidance) for staff facing these vulnerabilities

---

### 3.5 Client Communication and Safety Briefing

**Client security counseling**:

Attorneys should brief clients on surveillance and government access risks as part of standard client intake:

1. *Subpoena risk briefing*:
   - Explain that legal files are at risk of subpoena
   - Explain attorney-client privilege and work product doctrine, but be explicit about limitations (privilege can be overcome; metadata can be discoverable)
   - Recommend that clients communicate sensitive information during in-person meetings rather than by email
   - Advise clients of what to do if contacted by agents about the attorney relationship

2. *Government contact protocol*:
   - If an agent arrives with a warrant to search the office, advise staff to:
     - Not resist; compliance is required under warrant
     - Document the scope of the search and what was accessed
     - Immediately notify attorneys
     - Do not volunteer information beyond the warrant scope
   - If an agent appears with a subpoena (not a warrant), advise staff to:
     - Inform the agent that you have received a subpoena and are consulting counsel
     - Do not produce documents without attorney direction
     - Document the agent's identity and agency

3. *Client self-security briefing*:
   - Advise clients on basic device and communication security (use Signal, not SMS; full-disk encryption; not sharing identifying information)
   - Provide resources on government surveillance (EFF, ACLU) and security guides
   - Ensure clients understand the risks specific to their situation (immigration status, political activity, etc.)

---

### 3.6 Organizational Resilience and Community Defense

**Post-subpoena operational resilience**:

If an organization has received significant government pressure:

1. *Public documentation and transparency*:
   - Document all subpoena requests received (redacted for client privacy)
   - Publish annual reports on government information requests received (transparency report model)
   - Share information with the broader legal community (NAPSA, AILA, NLG) about targeting patterns and tactics

2. *Security infrastructure redundancy*:
   - Maintain off-site encrypted backups of client files
   - Ensure that loss of the office (raid, sabotage) does not result in loss of client representation capability
   - Consider distributed work arrangements (multiple office locations, remote work capability)

3. *Community accountability and legal support*:
   - Establish relationships with civil rights organizations that can mobilize support if the organization itself is targeted
   - Maintain relationships with media and watchdog organizations that can amplify information about government overreach
   - Participate in coalitions with other organizations serving vulnerable populations (DV services, medical providers, etc.) to share threat intelligence

---

## PLAYBOOK 4: Academic Institutions and Faculty Protection

### 4.1 Target Audience and Threat Profile

**Target audience**: Academic security officers, faculty in civil rights and critical scholarship areas, law school IT directors, faculty who advise student activists, graduate programs in immigration law and policy. This includes public universities, private institutions, and law schools with immigration clinics.

**Academic institution-specific threat profile**:

Universities face surveillance pressures from multiple directions:

1. **Targeted faculty and student researcher surveillance**: Scholars researching immigration policy, civil rights, federal enforcement, or labor topics have become investigation subjects. FBI field offices maintain files on academic researchers who work on government accountability topics. This is documented in FOIA releases and confirmed in interviews with scholars who received threat briefings from FBI.

2. **Foreign student and researcher targeting**: International students and scholars from China, Iran, Russia, and other designated countries are subject to intensive surveillance. The Significant Countrywide Overreach Program (SCOOP — formally the China Initiative, now expanded) has moved beyond tech industry espionage to monitor academic research broadly. Foreign-national students and scholars face biometric collection, visa revocation, and investigation solely based on research topics.

3. **Political retaliation against research**: Research findings that contradict government policy (on immigration enforcement effectiveness, on police practices, on surveillance impacts) have triggered government pressure: defunding of research, investigation of researchers, and institutional pressure to silence or retract findings. Documented cases: the Stanford study on ICE effectiveness funded by NIH (government pressure to suppress findings); the study on facial recognition accuracy funded by DARPA (government pressure to limit distribution); law school research on government contractors (subpoena of faculty files).

4. **Student activist targeting**: Student organizers on campus face surveillance through campus police (which are integrated into federal law enforcement database systems), student informants, and federal agency monitoring. Universities that cooperate with ICE (on-campus immigration enforcement) create direct targeting risk for undocumented and DACA students.

---

### 4.2 Institutional-Level Protections

**University policy framework for faculty protection**:

Universities should establish explicit policies protecting faculty research and faculty engagement with activism:

1. *Academic freedom and research protection policy*:
   - Establish a written commitment that the institution will not suppress, alter, or retract research findings based on government pressure
   - Commit that the institution will defend faculty from government requests for research data, methodologies, or preliminary findings (this can be done through attorney-client privilege if legal counsel is involved in research governance)
   - Establish a faculty research security committee that provides security guidance for sensitive research

2. *Government request response protocol*:
   - Establish that the institution (through general counsel) will be the sole point of contact for government information requests involving faculty or students
   - Do not allow individual faculty to respond directly to subpoenas or records requests
   - Negotiate scope and privilege with legal counsel before producing any records

3. *Sanctuary campus commitment*:
   - For institutions with significant populations of undocumented or DACA students, establish explicit "sanctuary campus" policies:
     - ICE access to campus is limited to specific locations (not general campus access)
     - Campus police do not cooperate with ICE absent specific warrant
     - University will not provide student directory or registration information to ICE absent subpoena (and will negotiate subpoena scope)
     - Campus provides emergency legal support and financial assistance for students facing enforcement

---

### 4.3 Faculty and Student Safety Infrastructure

**Department-level security for vulnerable faculty and students**:

Departments with faculty doing sensitive research (immigration, surveillance, federal enforcement) should establish:

1. *Research security protocols*:
   - Preliminary research findings should not be circulated except to co-authors and advisors (not on email; communicate verbally or in person)
   - Research involving vulnerable populations (undocumented immigrants, detained persons) requires human subjects review and explicit security protocols for data storage
   - Raw data should be encrypted and separate from analysis
   - Metadata (client names, interview dates, locations) should be separately encrypted and stored in a different location
   - Consider pseudonymizing sensitive data even before government requests arrive (refer to subjects by ID number, not name; store the name-ID mapping in a separate encrypted file)

2. *Faculty personal security*:
   - Faculty doing government accountability research should be briefed on:
     - How to recognize surveillance (being followed, devices being accessed, unusual contacts)
     - How to document threats (if receiving hostile messages, subpoenas, or government contacts)
     - How to request FBI threat briefings (this is available to any academic through the FBI field office; requesting one preemptively can provide intelligence)
   - Department chairs should establish confidential check-in protocols for faculty under visible government pressure

3. *Student activist protection*:
   - For students organizing politically, institutions should provide:
     - Legal support coordination (relationships with student legal defense organizations, bail funds, legal clinics)
     - Communication security training (organized by IT staff with security expertise; includes Signal setup, device hardening, etc.)
     - Documentation of retaliation if it occurs (academic sanctions, disciplinary actions, or institutional restrictions appear to retaliate for political activity)

---

### 4.4 Data Security and Records Management

**Research and student data protection**:

1. *Research database security*:
   - All research involving human subjects should use encrypted databases
   - Access should be limited to research team members and should require multi-factor authentication
   - Backup should be encrypted and stored off-site
   - Data retention policies should be explicit (delete data when study ends; if legal hold, maintain encrypted)

2. *Student records and FERPA compliance*:
   - FERPA (Family Educational Rights and Privacy Act) limits government access to student records, but does not provide complete protection
   - Institutions should use FERPA protections to the maximum extent (require specific subpoena for release of student information; assert privacy protections where available)
   - Student-sensitive data (undocumented status, visa type, disability, legal proceedings) should be stored separately from general enrollment records and should require specific authorization to access

3. *Communication security for academic teams*:
   - Do not use Gmail, Outlook, or other consumer cloud email for research communication involving sensitive data
   - Use institutional email with encryption (ProtonMail for Business integrated with institutional domain, or self-hosted encrypted email)
   - For sensitive research coordination, use Signal or Matrix for team communication
   - Do not store preliminary research, methodologies, or raw data on cloud services accessible to the institution's IT staff (this creates a single point of government access)

---

### 4.5 Public Communication and Research Distribution

**Threat-aware research publication strategy**:

Before publishing sensitive research:

1. *Legal review*:
   - Have institutional counsel review research for potential legal exposure (is the research likely to draw government scrutiny? Will publishing create security risks for research subjects?)
   - If research involves human subjects, have IRB confirm that publication plan does not violate subject privacy

2. *Publication timing*:
   - Consider timing of publication to avoid publication during government transition periods (when administrations change, enforcement priorities shift)
   - Consider whether preliminary findings should be shared with policy makers before public release (this can allow policy-informed commentary and can create advocates for the research)

3. *Author safety*:
   - For lead authors of controversial research, consider using a pen name or institutional affiliation only (not personal email/contact)
   - Establish institutional contact procedures so individuals do not contact lead authors directly
   - Document all hostile communications or threats related to the research

---

## Implementation Roadmap — Organizational Playbook Adoption

### Immediate (Weeks 1–2)
- Establish governance structures (board cybersecurity committee for nonprofits; organizing finance separation for unions)
- Distribute security briefings to leadership and IT staff
- Conduct a threat assessment: what is your organization's specific threat profile?

### Short-term (Weeks 3–8)
- Implement encryption for at-rest data (full-disk encryption on computers; encrypted database for sensitive files)
- Establish data classification and retention policies
- Conduct staff security training and device hardening

### Medium-term (Weeks 9–16)
- Implement encrypted communications infrastructure (Signal, Matrix, encrypted email)
- Establish government request protocols and train staff
- Conduct vulnerability assessment with external security consultant (optional but recommended)

### Long-term (Months 4–12)
- Establish organizational cyber insurance
- Conduct tabletop exercises (simulate government subpoena or breach scenario)
- Build redundancy and resilience infrastructure (off-site backups, distributed work capability, etc.)

---

## Sources and References

- Amnesty International. 2025. "Babel Street and DHS Surveillance of Protest." Amnesty International Report.
- EFF. 2025. "How Cops Are Using Flock Safety to Surveil Protesters." EFF report and FOIA analysis.
- The Intercept. 2026. "LAPD Drone Surveillance of Protests." Investigative reporting.
- NBC News. 2026. "ICE Facial Recognition at Protests." Video investigation.
- Government Accountability Project. 2025. "Immigration Whistleblowers." whistleblower.org.
- Freedom of the Press Foundation. 2026. "SecureDrop." securedrop.org.
- EFF. 2025. "Surveillance Capitalism and Civil Rights." Briefing paper.
- NAPSA (National Association of Protection and Advocacy Services). 2026. "Government Surveillance and Disability Rights." Legal analysis.

