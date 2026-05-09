---
title: "Tier 2 Sector-Specific Tactical Guide: Nonprofits and Civil Society Organizations"
project: cybersecurity-hardening
created: 2026-05-09
status: production-ready
phase: Phase 2 — Sector Expansion
audience: Executive directors, CISOs, IT managers, and operations leads at advocacy organizations, legal aid organizations, immigrant rights groups, labor unions, faith communities, investigative media, environmental organizations, and related civil society entities
word_count: ~5,300
depends_on:
  - 2026-threat-landscape-q2-update.md
  - threat-model.md
  - opsec-playbook.md
  - organizational-opsec-playbook.md
  - activist-organizing-playbook.md
  - palantir-threat-model.md
confidence: high — all threat claims sourced to primary or near-primary sources as of May 2026
---

# Tier 2 Sector-Specific Tactical Guide: Nonprofits and Civil Society Organizations

**Most important finding**: Civil society organizations face a threat environment in 2026 that is structurally different from the private sector threats that dominate commercial cybersecurity guidance. The primary threat is not ransomware — though ransomware is a real risk — it is targeted surveillance and infiltration by a combination of state actors, corporate private intelligence firms, and hostile domestic political actors. Cloudflare Project Galileo's 2025 data documented a 241% increase in attacks against civil society and human rights organizations between 2024 and 2025. The attacks were not financially motivated. They were mission-disruptive.

The second defining characteristic: civil society organizations are "cyber-poor, target-rich" — the CyberPeace Institute's description. They hold sensitive information about the populations they serve (immigration status, financial vulnerability, health information, political activity), they serve as trusted intermediaries for people in legal jeopardy, and they operate with security budgets that are a fraction of those in the private sector. The combination creates a humanitarian security problem that commercial cybersecurity guidance does not adequately address.

This guide draws on the full cybersecurity-hardening corpus — particularly the organizational-opsec-playbook.md, activist-organizing-playbook.md, and palantir-threat-model.md — and maps their guidance to the organizational contexts, threat models, and resource constraints specific to civil society organizations.

**Role-specific navigation**: Executive directors should read Sections 1 and 5 (governance and donor/partner-facing risks). IT managers and operations leads should read Sections 2 and 3. Advocacy and program staff should read Section 4 (staff operational security). Legal counsel or privacy officers at legal aid organizations should supplement this guide with the tier-2-immigration-attorney-implementation-guide.md.

---

## Section 1: 2026 Threat Model — Who Is Targeting Civil Society and How

### 1.1 State-Sponsored Targeting — The Geopolitical Context

Civil society organizations working on immigration, labor rights, environmental advocacy, election security, and government accountability are operating in an environment where federal executive agencies have both the legal authority and demonstrated willingness to deploy surveillance capabilities against domestic civil society.

**The confirmed threat capabilities directed at civil society in 2025-2026**:

**DHS administrative subpoenas to unmask digital activists**: Between late 2025 and early 2026, DHS and ICE issued hundreds of administrative subpoenas to Google, Meta, Reddit, Discord, and other platforms seeking to identify the people behind accounts that posted ICE raid alerts, bilingual immigration information, or criticism of enforcement operations. Administrative subpoenas require no judicial authorization. Reddit, Meta, and Google voluntarily complied with some requests. The ACLU challenged several in California and Pennsylvania; DHS withdrew some subpoenas rather than litigate. A lawsuit challenging the subpoena authority was filed in April 2026. As of May 2026, the authority remains in use.

**Babel Street social media persistent monitoring**: The DHS, ICE, CBP, and State Department hold confirmed contracts with Babel Street for persistent keyword-based social media monitoring. Once a person or organization is flagged, Babel Street continuously monitors all new public content matching that flag without requiring a new query. The "Catch and Revoke" program uses Babel Street to identify visa holders posting protest-related content and revokes their visas. Organizations that post about protest activity, immigration enforcement, or advocacy on public social media accounts are being monitored through this infrastructure.

**Mobile Fortify field biometric identification**: ICE agents have photographed protesters and observers at public demonstrations using Mobile Fortify, a real-time facial recognition system with confirmed deployments in Minneapolis, Portland, and Los Angeles. Field agents in Portland told a US citizen observing an enforcement action that she would be "on a domestic terrorist watchlist" for continuing to attend such events. The chilling effect of this statement is the mechanism — the actual inclusion in any specific list is secondary to the behavioral change it produces.

**Paragon Graphite zero-click spyware**: ICE confirmed in April 2026 the deployment of Paragon Solutions' Graphite spyware, which can compromise device cameras, microphones, and messages without the target clicking any link. WhatsApp disclosed that approximately 90 journalists and civil society members were targeted. For organizations with staff who communicate with undocumented clients, Graphite represents the elimination of Signal's endpoint protection — the encryption is intact, but the device is compromised before the message is sent.

**Sources**: [EFF: Palantir and ICE Work (April 2026)](https://www.eff.org/deeplinks/2026/04/palantir-has-human-rights-policy-its-ice-work-tells-different-story); [NBC News: ICE agents using Mobile Fortify at protests](https://www.nbcnews.com/tech/security/ice-agent-facial-recognition-video-protest-movile-fortify-photo-rcna257331); [CyberPeace Institute: Cyber-Poor, Target-Rich](https://cyberpeaceinstitute.org/news/cyber-poor-target-rich-the-crucial-role-of-cybersecurity-in-nonprofit-organizations/)

### 1.2 Corporate Private Intelligence — The OSINT Threat

Organizations involved in labor organizing, environmental advocacy, or corporate accountability campaigns face a parallel threat from corporate private intelligence firms. These firms — Kroll, Guidepost Solutions, Pinkerton, and smaller specialized operations — are hired by corporations facing advocacy campaigns to conduct surveillance, gather intelligence on organizational operations, and identify "vulnerabilities" that can be used to disrupt campaigns.

The tools available to private intelligence firms in 2026 include commercial data broker products (the same pipeline documented in the palantir-threat-model.md), social media monitoring platforms, OSINT aggregation services, and in some documented cases, infiltration of advocacy organizations by paid informants.

The defense is the same as the government surveillance defense: organizational compartmentalization, strong account security, data minimization, and staff security awareness. The specific threat profile differs — private intelligence firms are not focused on deportation but on campaign intelligence — but the countermeasures largely overlap.

### 1.3 Ransomware — The Financially Motivated Threat

Criminal ransomware groups target nonprofit organizations because nonprofit networks often contain sensitive donor and client data that can be threatened in double-extortion scenarios, because nonprofits frequently have weaker technical defenses than private organizations, and because the charitable status of the organization creates reputational pressure to pay quickly before donor relationships are damaged by a public disclosure.

In 2025-2026, the nonprofit sector has experienced documented ransomware incidents at multiple immigration legal aid organizations, DV shelters, and labor unions. The Rhysida and Medusa groups have specifically targeted organizations whose client data includes protected immigration status information, calculating that these organizations face the highest pressure to avoid public data disclosure.

**The specific nonprofit ransomware risk factor**: Staff personal email accounts used for organizational business. This is common in under-resourced nonprofits where staff use Gmail or other personal email for convenience. Personal email accounts connected to organizational cloud storage (shared Google Drives, shared Dropbox) are not protected by any organizational security controls. A phishing attack against a staff member's personal email can reach organizational data through shared storage connections.

**Sources**: [SecureWorld: Cybersecurity for NGOs in 2026](https://www.secureworld.io/industry-news/cybersecurity-for-ngos-in-2026); [Cloudflare Project Galileo: Civil Society Attack Statistics](https://www.cloudflare.com/galileo/); [CyberPeace Institute: Nonprofit Cybersecurity](https://cyberpeaceinstitute.org/news/cyber-poor-target-rich-the-crucial-role-of-cybersecurity-in-nonprofit-organizations/)

---

## Section 2: Priority Technical Controls — The Nonprofit Resource-Constrained Stack

### 2.1 Free and Low-Cost Security Resources for Civil Society Organizations

The commercial cybersecurity market is not designed for nonprofit budgets. Several initiatives exist specifically to address this gap:

**Cloudflare Project Galileo**: Free enterprise-grade DDoS protection and security services for qualifying civil society organizations — nonprofits, media organizations, human rights groups, and election administration bodies. At the price point of $0, this is the highest-ROI security resource available to qualifying organizations. Apply at cloudflare.com/galileo. The application process takes approximately 30 minutes; approval takes 1-2 weeks. Project Galileo has protected over 2,400 civil society websites from DDoS attacks that would have been disabling without the service.

**Google Workspace for Nonprofits**: The full Google Workspace Business Starter package (Gmail, Drive, Docs, Meet, security admin console) at zero cost for qualifying 501(c)(3) organizations. The organizational Google Workspace account provides security features that personal Gmail accounts do not — centralized MFA enforcement, data loss prevention, account recovery controls, and audit logging. Organizations still using staff personal Gmail accounts for organizational business should migrate to Google Workspace for Nonprofits immediately.

**Microsoft 365 for Nonprofits**: Similar to Google Workspace for Nonprofits — Microsoft 365 Business Basic at no cost for qualifying nonprofits. Includes Exchange email, SharePoint, Teams, and Microsoft Defender for Office 365 (Plan 1 for free tier, Plan 2 for paid tiers with significant nonprofit discounts).

**Defending Democracy Foundation's Cybersecurity Initiative**: Provides FIDO2 hardware security keys at subsidized or zero cost to qualifying high-risk civil society organizations. The application process requires demonstrating that the organization faces elevated threat levels. Immigration legal aid organizations, election security organizations, and investigative journalism organizations have historically qualified.

**Access Now's Digital Security Helpline**: Direct security support for civil society organizations facing active threats. Free. Available at accessnow.org/help. Response time is typically 24-48 hours for urgent cases.

### 2.2 The Organizational Account Architecture — The Single Most Important Control

The most impactful security change for most nonprofits is not a technical tool — it is moving organizational activity from staff personal accounts to organizational accounts that can be centrally managed.

**The current state at most under-resourced nonprofits**:
- Staff use personal Gmail or Yahoo email for organizational work
- Organizational files are in personal Google Drive folders shared to other staff personal accounts
- Organizational social media accounts have multiple personal users with the password shared informally
- No central admin can revoke access when staff departs

**The target state**:
- All staff use email under the organizational domain (yourorg.org), managed via Google Workspace or Microsoft 365
- Files are in organizational Google Drive or SharePoint, with access controlled by role (staff, volunteer, board)
- Social media accounts use business manager features with individual login credentials for each authorized user
- When staff departs, the IT admin or executive director revokes access to all organizational accounts in a single administrative action

**The transition path**: If all staff currently use personal Gmail and share a personal Google Drive, transitioning to Google Workspace takes approximately one week for a small organization. The steps are: set up the Google Workspace account under the organizational domain, create accounts for each staff member, migrate shared files from personal Google Drive to organizational Shared Drive, and update organizational email addresses with external contacts. This is not technically complex — it is a logistics project.

**The specific security gain**: When an attacker compromises a staff member's personal Gmail account, they gain access to everything that staff member can access with their personal credentials. When an attacker compromises a staff member's organizational Workspace account, they gain access to what that staff member is authorized to access — which, in a properly configured organizational account, does not include the entire organization's data. The blast radius is defined by role-based access control rather than by what that individual has personally shared.

### 2.3 Signal as Organizational Infrastructure — Configuration and Governance

Signal is the recommended communications tool for sensitive organizational communications in the cybersecurity-hardening corpus. For civil society organizations, the specific configuration steps that matter are:

**Usernames, not phone numbers**: Signal now supports usernames as the primary identifier, meaning users do not need to share their phone number to connect. For staff who communicate with clients or external contacts, username-based connection prevents those contacts from learning the staff member's personal phone number. Set up Signal usernames for all staff who use Signal for organizational purposes.

**Disappearing messages — organizational policy, not individual choice**: Set organization-wide guidance on disappearing message timers for different communication contexts. For client communications: 1 week (balances documentation needs with exposure reduction). For internal strategy discussions: 1 week or 1 month depending on organizational retention policy. For public campaign communications: can be longer. The goal is that sensitive internal discussions are not retained indefinitely on every participant's device.

**Group admin controls**: Signal group admins can control who can add members, who can change group settings, and who can send messages. For organizing committees and sensitive working groups, use admin-only member additions to prevent an unauthorized contact from being added to a sensitive group.

**The Graphite threat and Lockdown Mode**: Given the confirmed deployment of Paragon Graphite zero-click spyware against civil society by ICE, organizations whose staff communicate with at-risk clients should implement iOS Lockdown Mode on staff devices used for client communications. Lockdown Mode blocks the message attachment vector exploited by Graphite-class spyware. It restricts some convenience features (certain web browsing behaviors, some media types) but does not prevent Signal use. For staff at elevated risk, the restriction is worth the protection.

---

## Section 3: Organizational Data Governance — What to Collect, What to Keep, What to Delete

### 3.1 The Data Minimization Principle for High-Risk Populations

The single most effective protection for clients and constituents in high-risk populations is not encrypting their data — it is not having their data in the first place. Data that does not exist cannot be subpoenaed, stolen, or compelled.

**The legal compulsion threat**: Administrative subpoenas require no judicial authorization. If your organization receives an ICE administrative subpoena for client records, the subpoena is legally self-authorized and you must respond in writing (asserting applicable privileges and limitations) even if you ultimately contest compliance. But if your intake records do not include client addresses, your response to a subpoena for "client home addresses" is honest and complete: "We do not maintain client home address information."

**What the data minimization policy looks like in practice**:

At intake: Collect the information the organization needs to provide its service — not everything a comprehensive intake form might ask for. If your organization provides legal consultation, you need to know what legal issue the client faces and how to contact them. You may not need their home address, their employer's name, or the names of their household members unless those are specifically needed for the legal service.

In client files: Regularly review and delete information that is no longer needed. A closed case file that is 18 months old and for which the client is no longer served has limited ongoing value to the organization and significant ongoing risk if subpoenaed or stolen. Implement a retention schedule that deletes case files after a defined period (consult with legal counsel for your jurisdiction's requirements) and actually execute it.

For community programs: Event attendance lists, volunteer sign-in sheets, and participation records contain information about who attended a specific event at a specific time and place. If this information is not needed for organizational purposes, don't collect it. If it is needed (for grant reporting on "number served"), collect aggregate numbers, not names.

### 3.2 Secure Client Communication Channels

For organizations that communicate with clients who face legal jeopardy, the choice of communication channel is a security decision, not just a convenience decision.

**The communication channel risk matrix**:

| Channel | Content Protection | Metadata Protection | Subpoena Resistance | Recommended Use |
|---|---|---|---|---|
| Regular phone call | None | None | Carrier metadata produced with subpoena | Not for sensitive client communications |
| SMS/text message | None | None | Carrier produces with subpoena | Appointment reminders only |
| Email (Gmail, Outlook) | TLS in transit only | None | Google/Microsoft produces with subpoena | Non-sensitive communications |
| ProtonMail (end-to-end) | E2E encrypted | Limited metadata | Proton resists U.S. subpoenas for content; metadata may be producible | Sensitive client email |
| Signal | E2E encrypted | Minimal metadata | Signal has no content to produce; metadata is limited | All sensitive client communications |
| In-person | Maximum | None | Notes may be subpoenaed | Highest-risk client discussions |

**The operational implication**: Any organization that communicates with clients about immigration status, legal strategy, or sensitive personal matters using regular phone or email is creating a record that is accessible to law enforcement via administrative subpoena with no judicial authorization required. The shift from phone/email to Signal for client communications is an operational change, not just a technical one — it requires training staff and educating clients about how to use the new channel.

---

## Section 4: Staff Operational Security — The Human Layer

### 4.1 Security Awareness for Civil Society Staff

Civil society organizations face a specific challenge in security awareness: the threats their staff face are politically motivated, not merely financially motivated. A generic security awareness training that focuses on "don't click phishing links" addresses only a fraction of the threat.

**The civil society-specific awareness curriculum should cover**:

**Personal device hygiene for staff who work with sensitive populations**: Staff who use personal devices for organizational communications (even if the organization is implementing organizational accounts) need to understand: full-disk encryption is enabled on their personal device; their personal device has a strong PIN or passphrase (not fingerprint or face unlock, which can be compelled by law enforcement); Signal is configured with disappearing messages; their personal social media accounts are not linked to their organizational role in ways that could be used to identify clients.

**Social media operational security**: Staff at organizations working on immigration, labor organizing, or government accountability should review their personal social media accounts with the lens of: does anything in my public posts identify my clients or constituents by name, location, or immigration status? Does anything in my posts connect my personal social media to my organizational role in ways that could be targeted? The goal is not secrecy about employment — it is careful separation of personal social media presence from client-identifiable information.

**Physical security at sensitive events**: Staff who attend community events, legal clinics, or organizing meetings where undocumented individuals may be present should understand that mobile devices create location records. An organizational event log can be reconstructed from the location data of staff phones even without any explicit digital record. The standard protocol: for events where participant confidentiality is critical, ask staff to leave phones in the car or place them in a Faraday bag during the event.

**The OSINT awareness test**: Have staff Google themselves and their organization. What information appears? What could an adversary learn from the first page of search results about organizational structure, client programs, staff home addresses, and staff personal social media? This exercise builds the intuition for what information is publicly accessible without any hacking required.

### 4.2 Board and Leadership Security

Executive directors and board members of advocacy organizations are specific targets because they make organizational decisions, communicate with funders, and often have the highest level of access to sensitive organizational information.

**The spear phishing threat to leadership**: A spear phishing email targeting an executive director will be personalized — it will reference a specific funder, a current campaign, or a realistic internal request. Generic phishing training ("look for bad spelling and urgent requests") does not prepare leaders for personalized targeted phishing. The defense is process, not awareness: all requests to move money, share credentials, or provide sensitive information to new contacts must be verified through an established secondary channel (phone call to a known number, not a call to a number in the email) regardless of how legitimate the request appears.

**Board member personal security briefing**: Board members of high-risk civil society organizations should receive a brief (30-minute) individual security orientation covering: their personal email account security (MFA enabled, unique password), their personal phone security (strong PIN, encrypted), and the organizational communications channels they should use for board business. Board members are often less security-aware than staff because they receive less organizational training.

### 4.3 The Departure Protocol — Staff and Volunteer Offboarding

The most common internal security failure in nonprofits is the absent departure protocol. When a staff member or volunteer leaves, their access to organizational accounts, files, shared passwords, and client data must be revoked immediately.

**The 24-hour offboarding checklist**:
- [ ] Revoke access to organizational Google Workspace or Microsoft 365 account
- [ ] Remove from all organizational Signal groups
- [ ] Change any shared passwords the departing individual knew (administrative accounts, social media accounts, CRM system)
- [ ] Revoke access to shared cloud storage (Google Drive, Dropbox, SharePoint)
- [ ] Remove from organizational mailing lists that include sensitive information
- [ ] Disable any VPN credentials or remote access
- [ ] Archive and transfer any client data from the departing individual's organizational account to their supervisor

**The volunteer offboarding gap**: Organizations meticulously offboard paid staff but frequently neglect volunteers who had the same system access. Build volunteer offboarding into the standard volunteer departure process.

---

## Section 5: Organizational Governance — The Security-Mission Integration

### 5.1 Security as Mission, Not Overhead

The most common executive director objection to security investment is that it diverts resources from mission. The reframe: for organizations serving populations facing surveillance and enforcement, security is mission. A legal aid organization that cannot protect client confidentiality is not serving clients effectively. An immigrant rights organization whose client database is subpoenaed is not protecting the community it serves. An advocacy organization whose internal strategy communications are infiltrated by a private intelligence firm is not winning its campaign.

The effective argument for security investment: "Our organization's mission requires that we be trustworthy stewards of the information our clients, donors, and partners share with us. Being trustworthy stewards requires technical controls. These are mission expenses, not overhead."

**The donor conversation**: Major donors to civil society organizations in 2026 increasingly understand the security threat landscape. ACLU, Ford Foundation, Open Society Foundations, and other major institutional funders have explicitly stated that organizations serving high-risk populations should treat security as a fundable program expense. When budgeting for security improvements, include them in program budgets (as "program infrastructure") alongside the legal aid or organizing program they protect, not in overhead/administration.

### 5.2 The Incident Escalation Policy — Who Decides What

Civil society organizations need a documented incident escalation policy that answers: if our systems are compromised, who makes decisions and in what order?

**The four decisions that need pre-authorized decision makers**:

1. **Isolate a compromised system from the network**: This is an IT-technical decision that in most small organizations cannot wait for board approval. Pre-authorize the IT manager or senior staff member to make this decision immediately without convening leadership.

2. **Notify funders and partners**: This is an executive director decision, made in consultation with legal counsel. A security incident that may have compromised donor data or partner communications requires prompt notification — but the specific language and timing must be reviewed before sending.

3. **Notify clients who may be affected**: This is the highest-stakes notification decision for organizations serving high-risk populations. If client data may have been compromised in a way that creates immigration enforcement risk, the notification is urgent. If the nature of the compromise is unclear, premature notification that causes clients to take defensive actions (moving, changing contact information) before the risk is assessed may be unnecessary and disruptive. Pre-authorize who makes this decision and what process governs it.

4. **Cooperate with or resist law enforcement demands related to the incident**: If a security incident leads to law enforcement contact (FBI cyber division, state police cybercrime unit), the organization needs legal counsel before any cooperation. Pre-authorize that no staff member will provide any information to law enforcement in connection with a security incident without first consulting legal counsel.

### 5.3 The OSINT Reduction Program — Organizational Data Hygiene

The cybersecurity-hardening corpus's Part 0 (data broker opt-outs) covers individual data broker removal. Organizations also have a presence in commercial data broker databases — organizational addresses, staff names, organizational phone numbers, and in some cases internal organizational charts scraped from LinkedIn.

**Organizational data broker opt-out program**:

1. Search your organization's name in Spokeo, BeenVerified, Whitepages, and Intelius. Document what information appears about the organization, its programs, and its key staff.

2. Submit opt-out requests for organizational information at each data broker. Most accept organizational opt-outs through the same process as individual opt-outs — use the organization's name as the search term.

3. Remove unnecessary organizational information from public-facing websites. Many nonprofit websites list staff names, titles, phone extensions, and email addresses in ways that help clients contact the organization but also provide OSINT resources to adversaries. Consider a general-contact model (contact@yourorg.org, a general phone number) that does not expose individual staff contact information on public pages.

4. Review LinkedIn profiles of staff for information that could identify organizational clients, current campaigns, or internal structure. Staff personal LinkedIn pages are their own — this is not a requirement to limit personal expression — but it is appropriate to provide guidance that staff should not post information that identifies clients, reveals confidential organizational strategy, or provides an adversary with an organizational chart.

---

## Sources

- [Cloudflare Project Galileo: Civil Society Attack Data](https://www.cloudflare.com/galileo/)
- [CyberPeace Institute: Cyber-Poor, Target-Rich](https://cyberpeaceinstitute.org/news/cyber-poor-target-rich-the-crucial-role-of-cybersecurity-in-nonprofit-organizations/)
- [SecureWorld: Cybersecurity for NGOs in 2026](https://www.secureworld.io/industry-news/cybersecurity-for-ngos-in-2026)
- [Dianova: Cybersecurity for NGOs 2026](https://www.dianova.org/news/cybersecurity-for-ngos-in-2026-from-digital-fragility-to-cyber-resilience-in-a-hostile-world/)
- [fundsforNGOs: Growing Threats Facing Civil Society 2026](https://news.fundsforngos.org/2026/01/12/understanding-the-growing-threats-facing-civil-society-today/)
- [CISA: Cybersecurity Resources for High-Risk Communities](https://www.cisa.gov/audiences/high-risk-communities/cybersecurity-resources-high-risk-communities)
- [Access Now: Digital Security Helpline](https://www.accessnow.org/help/)
- [EFF: Palantir and ICE Work (April 2026)](https://www.eff.org/deeplinks/2026/04/palantir-has-human-rights-policy-its-ice-work-tells-different-story)
- [ACLU: ICE Administrative Subpoenas](https://assets.aclu.org/live/uploads/2025/04/ACLU-KYR-on-ICE-administrative-subpoenas-4.17.25.pdf)
- [NBC News: ICE agents using Mobile Fortify at protests](https://www.nbcnews.com/tech/security/ice-agent-facial-recognition-video-protest-movile-fortify-photo-rcna257331)
- [Organizational Opsec Playbook (corpus internal)](../organizational-opsec-playbook.md)
- [Palantir Threat Model (corpus internal)](../palantir-threat-model.md)
- [Activist Organizing Playbook (corpus internal)](../activist-organizing-playbook.md)

---

*Created: 2026-05-09. Threat currency current as of May 9, 2026. All organizational security decisions involving legal risk should be reviewed by legal counsel. Attorney-client privilege for nonprofit legal counsel communications protects strategic communications — ensure that legal counsel is engaged before any decisions about law enforcement cooperation. Quarterly review checkpoint: July 26, 2026.*
