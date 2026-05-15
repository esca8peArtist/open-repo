---
title: "Sector-Specific Threat Briefings: Master Document — May 2026"
project: cybersecurity-hardening
created: 2026-05-15
status: production-ready
phase: Phase 2 — Tier 2 Distribution
author: Cybersecurity Hardening Project (public-source research corpus)
gist-url: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
next-review: 2026-08-15
sectors:
  - Journalists
  - Immigration Legal Aid
  - Educators and Academic Researchers
  - Labor and Civil Rights Organizers
  - Faith Leaders and Spiritual Communities
depends-on:
  - phase-2-threat-briefing-journalists.md
  - phase-2-threat-briefing-immigration-legal-aid.md
  - phase-2-threat-briefing-academics.md
  - phase-2-threat-briefing-labor-organizers.md
  - phase-2-threat-briefing-faith-leaders.md
  - PHASE_2_SEQUENCING.md
  - SCENARIO_PLAYBOOK_INDEX.md
  - may-2026-tier2-threat-briefing.md
---

# Sector-Specific Threat Briefings: Master Document
## May 2026 — Phase 2 Tier 2 Distribution

**Prepared by**: Cybersecurity Hardening Project (public-source research corpus)
**Date**: May 15, 2026
**Corpus**: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
**Quarterly review**: August 15, 2026

---

## How to Use This Document

This master document serves three purposes:

1. **Navigation hub**: Links to all five sector-specific briefings with a one-paragraph summary of each
2. **Escalation scenarios**: 2–3 "we have been compromised" scenarios per sector, with incident response triggers and contact lists — this content does not exist in the individual briefings and is new
3. **Tier 2 playbook integration**: Which cybersecurity-hardening playbooks apply to which sector, in what priority order, and where to customize for organizational context

The individual sector briefings (phase-2-threat-briefing-*.md) contain the full 500–800 word threat analysis. This master document extends them with the operational response layer.

---

## Cross-Sector Threat Threads — May 2026

Before the sector breakdown, five threat developments are present across all five sectors and should be understood as cross-cutting context:

**1. Penlink PLX location tracking (DHS, $2.9M contract, confirmed operational)**: Every phone at every gathering — organizing meeting, worship service, legal clinic, rally, class — generates location data accessible to DHS without a warrant. This affects all five sectors identically. The countermeasure is identical: leave phones out of sensitive spaces or understand that presence is being recorded.

**2. Palantir cross-agency data fusion (ICE ELITE + IRS CI + ICM September 2026 deadline)**: A query against any one agency database can surface connections to individuals in other agency databases through the Palantir relationship-mapping architecture. This affects sectors differently (legal aid and faith leaders face the most immediate client exposure; journalists face indirect exposure through sources) but the architecture is shared.

**3. Babel Street persistent monitoring (DHS, ICE, CBP, State contracts confirmed)**: Once a keyword match flags a name, social media handle, or organization, all future content is continuously monitored without new queries. Public-facing individuals in all five sectors who have participated in anti-enforcement advocacy since 2025 are likely already flagged.

**4. DOJ enforcement posture shift (Bondi memo framework, Enforcement and Affirmative Litigation Branch, FACE Services expansion)**: The DOJ's decision to use non-press legal theories to reach journalist sources, conspiracy frameworks to reach organizer communications, and civil rights enforcement to reach educational programs reflects a shared pattern: using existing statutory authority in novel prosecutorial configurations that bypass traditional constitutional protections. Each sector encounters this pattern through a different front door but the structural shift is the same.

**5. FISA Section 702 — June 12, 2026 deadline**: The Government Surveillance Reform Act's data broker loophole provision is the single most achievable legislative constraint on the commercial data pipeline feeding ICE. All five sectors have policy advocacy capacity that can be directed at this deadline. Organizations with contact lists or membership email access should send constituent communications to uncommitted senators before June 5.

---

## Sector 1: Journalists and Media Organizations

**Full briefing**: `phase-2-threat-briefing-journalists.md`
**Distribution tier**: Phase 2 Priority Constituency 2
**Primary contacts**: FPF, CPJ, RCFP, IRE, SPJ, NAHJ, AAJA, freelance reporters on civil liberties beats

### Briefing Summary (May 15, 2026)

Zero-click spyware (ICE Paragon Graphite) has made transport-layer security irrelevant for high-risk journalists — a device running Signal with full encryption can be fully compromised before the user touches it. The DOJ Bondi memo has reopened subpoena pathways for source identities through third-party records and conspiracy theories that bypass shield law analysis. CPJ has documented device seizures at protests and CBP border searches of journalist devices. AI-enhanced social media surveillance is operating against journalists who cover immigration enforcement. The November 2026 midterm election cycle is the highest-threat window for journalists covering voting rights, and the federal election security infrastructure has been dismantled.

---

### Tier 2 Playbook Integration — Journalists

| Playbook | File | Priority for Journalists | Customization Points |
|----------|------|--------------------------|---------------------|
| Journalist Security | `journalist-security-playbook.md` | **Priority 1 — Core** | CBP border protocol for reporters; SecureDrop deployment scale (solo vs. newsroom); Signal safety number verification cadence with sources |
| Journalist Security Extended | `journalist-security-playbook-extended.md` | **Priority 2 — Extended** | Source device hardening for confidential sources; deepfake response preparation specific to the reporter's public visibility level |
| Core OpSec | `opsec-playbook.md` | Priority 3 — Foundation | Device hardening base layer; applies before the journalist-specific layer |
| Activist Organizing | `activist-organizing-playbook.md` | Priority 4 — Protest contexts | For reporters covering protests and direct actions: ALPR vehicle tracking at event sites, biometric perimeter identification, drone surveillance coverage |

**Deployment sequence**:
1. Begin with `journalist-security-playbook.md` — covers the ICE Paragon Graphite countermeasure (Lockdown Mode) and the Bondi memo response (third-party record minimization)
2. Extend to `journalist-security-playbook-extended.md` for reporters on high-risk beats (immigration, political organizing, national security)
3. Add `activist-organizing-playbook.md` for any reporter who covers events in person where physical surveillance (ALPR, drone, biometric ID) is documented

**Org-specific customization**:
- **Solo freelancers**: Prioritize Lockdown Mode, Signal safety number verification, and SecureDrop for anonymous source intake. Border-crossing protocol is essential if traveling internationally.
- **Small newsrooms (under 20 staff)**: Add SecureDrop deployment guidance. Prioritize organizational credential hygiene (one compromised staff account reaches all source communications).
- **Large newsrooms**: Organizational-level security audits, newsroom IT configuration, and staff security training cadence. The Bitwarden CLI supply chain compromise window (April 21–late May 2026) requires credential rotation for any technical staff who updated password managers via package managers.

---

### Escalation Scenarios — Journalists

#### Scenario J-1: Source Identification Through Third-Party Records

**What it looks like**: You learn (through legal process notifications, a contact at the platform, or a source telling you) that DOJ has subpoenaed Google, Apple, or your mobile carrier for metadata associated with your accounts or phone number. Alternatively, a source tells you they have been contacted by federal agents who appear to know specific details that only you and they discussed — including details that were only communicated via a platform you believed was secure.

**Incident triggers**:
- Platform notifies you of a legal process demand (not all platforms do this — Signal does not receive content subpoenas because it holds none, but Apple will in some circumstances notify before complying with account requests)
- A source reports unexpected federal contact that correlates with information from your communications
- You receive a target letter, grand jury subpoena, or civil investigative demand
- A DOJ press inquiry to your newsroom references non-public information that originated in your reporting

**Immediate response**:
1. Do not delete anything. Preservation of evidence (the original source materials, the communications, the metadata) is required for your legal defense and may be legally required under a preservation order.
2. Contact press freedom legal counsel before speaking to any federal agent. The Reporters Committee for Freedom of the Press operates a 24/7 legal defense hotline: 1-800-336-4243.
3. Activate your newsroom's security protocol if one exists. If not: immediately stop communicating with the source via the potentially compromised channel and notify the source via a different channel that you are consulting counsel.
4. Document what you know: when you first became aware of the subpoena or contact, what information the agents appeared to have, which platforms or accounts are implicated.

**Who to contact**:
- Reporters Committee for Freedom of the Press: 1-800-336-4243 (legal defense hotline)
- Freedom of the Press Foundation: https://freedom.press / security@freedom.press (digital security emergency support)
- EFF Digital Security Helpline: https://www.eff.org/pages/digital-security-helpline
- Committee to Protect Journalists Emergency Line: +1 212 465 1004

**Forward-looking**: If the source identification occurred through third-party records rather than your own device, it means the countermeasure is technical (Signal for all future source communications; SecureDrop for anonymous document intake) rather than behavioral. The subpoena reached records you did not control.

---

#### Scenario J-2: Device Seizure at a Protest or Border

**What it looks like**: Law enforcement at a protest arrests you or temporarily detains you and seizes your device. Alternatively, CBP at a border crossing demands your device for inspection. In both cases the device contains source contact information and unpublished reporting materials.

**Incident triggers**:
- Device taken by law enforcement or CBP
- Law enforcement demands your password or biometric unlock
- You are told the device will be "forensically examined"

**Immediate response**:
1. Do not unlock your device voluntarily. Law enforcement can compel biometric unlock in some jurisdictions but generally cannot compel a memorized PIN under the Fifth Amendment's protection against self-incrimination. (Note: the law here is jurisdiction-specific and unsettled — consult counsel immediately if possible.)
2. Invoke your right to counsel before answering any questions about your device or its contents.
3. If the device is taken and returned: treat it as potentially compromised at the firmware level (LogoFAIL/BootKitty can be deployed during a device seizure with no visible indicator). Do not use the returned device for sensitive communications. Restore from a clean backup or replace the device.
4. Notify your newsroom's security contact or editor immediately.
5. Document what was on the device when seized: which apps, which accounts were logged in, which contacts were accessible.

**Who to contact**:
- Reporters Committee legal defense: 1-800-336-4243
- Your newsroom's general counsel (if applicable)
- National Press Photographers Association (NPPA) for photojournalists: https://nppa.org
- For CBP device searches: the border search exception means you have fewer immediate legal options but you can contest the search after the fact — document everything and contact RCFP immediately

---

#### Scenario J-3: Deepfake Content Deployed Against You or Your Reporting

**What it looks like**: Fabricated video or audio attributed to you circulates online, depicting you saying or doing something you did not say or do. Alternatively, deepfake content attributed to a source in your reporting is used to discredit the reporting itself.

**Incident triggers**:
- Someone contacts you about video or audio attributed to you that you did not create
- Your social media mentions spike with references to fabricated content
- A source reports that content attributed to them is being used to deny or undermine your reporting
- You receive a direct communication from an entity claiming to have compromising content and making demands

**Immediate response**:
1. Preserve evidence: screenshot URLs, download copies of the content with metadata if possible, document when and where it appeared.
2. Do not respond publicly before consulting legal counsel. The legal theories available to you (defamation, identity theft, computer fraud) depend on jurisdiction, the nature of the content, and who produced it.
3. Contact your newsroom editor and legal team immediately.
4. Report to EFF Digital Security Helpline for technical analysis support (forensic examination of synthetic content to document that it is fabricated).
5. Report to CPJ and FPF: documented cases of synthetic content targeting journalists are part of the public record that builds the legal and regulatory case against deepfake abuse.

**Who to contact**:
- EFF Digital Security Helpline: https://www.eff.org/pages/digital-security-helpline
- Freedom of the Press Foundation: https://freedom.press
- Committee to Protect Journalists: https://cpj.org (for documentation of the incident)
- Your newsroom's legal counsel

---

## Sector 2: Immigration Legal Aid and Civil Rights Organizations

**Full briefing**: `phase-2-threat-briefing-immigration-legal-aid.md`
**Distribution tier**: Phase 2 Priority Constituency 1 (highest priority)
**Primary contacts**: NILC, CLINIC, RAICES, AILA regional chapters, legal services organizations, law clinic staff

### Briefing Summary (May 15, 2026)

The Palantir ELITE system's address confidence score mechanism converts client data generated outside your organization (phone location data, utility billing, social media OSINT) into ICE targeting intelligence — regardless of encrypted communications protocols you use with clients. The September 2026 Palantir ICM deployment will integrate biometrics across all federal law enforcement databases, creating a multi-agency investigative environment for every HSI case. The IRS Palantir platform maps organizational financial relationships, meaning legal aid nonprofit donors and partner organizations may appear in ICE-adjacent queries. Device seizures at border crossings represent a complete client file exposure event. DOJ has used conspiracy and obstruction frameworks to reach journalist source communications — the same framework is available against attorneys in contexts where client advice touches on civil disobedience.

---

### Tier 2 Playbook Integration — Immigration Legal Aid

| Playbook | File | Priority | Customization Points |
|----------|------|----------|---------------------|
| Immigration Surveillance Evasion | `phase-2-immigration-surveillance-evasion-playbook.md` | **Priority 1 — Core** | Client-facing vs. staff-facing protocol distinction; California DROP vs. national opt-out pathways |
| Immigration Attorney Implementation | `immigration-attorney-implementation-guide.md` | **Priority 2 — Staff** | Week 1 / Month 1 / Month 3 implementation timeline for attorney and paralegal roles |
| Core OpSec | `opsec-playbook.md` | Priority 3 — Foundation | Device hardening baseline for all staff; border-crossing protocol for attorneys who travel |
| Financial Resistance | `financial-resistance-playbook.md` | Priority 4 — Org-level | For organizations facing donor exposure through IRS Palantir cross-agency mapping; financial compartmentalization |

**Deployment sequence**:
1. Begin with `phase-2-immigration-surveillance-evasion-playbook.md` — the client-protection protocol that is most immediately urgent given the September 2026 ICM deadline
2. Add `immigration-attorney-implementation-guide.md` for staff-side hardening (attorney-client communications, border device protocol, cloud storage migration)
3. Review `financial-resistance-playbook.md` if your organization has donor exposure through civil rights or advocacy-adjacent funding relationships

**Org-specific customization**:
- **Standalone legal aid firms (2–10 attorneys)**: Prioritize Signal migration for client communications, need-to-know case file access controls, and one clean device policy for international travel.
- **Large nonprofit legal aid organizations (50+ staff)**: Role-based access controls are the highest-leverage intervention — a single account compromise or legal process action against one staff member should not expose the full client database. Document your incident response authority chain before it is needed.
- **Law clinics in law schools**: Students working on clinic cases should be briefed specifically on the IRS cross-agency mapping risk — student records (FERPA-protected) and client records (privileged) exist in different legal frameworks but can both surface in Palantir relationship-mapping queries.

---

### Escalation Scenarios — Immigration Legal Aid

#### Scenario IL-1: Subpoena or Legal Process Targeting Client Files

**What it looks like**: Your organization receives a subpoena, civil investigative demand, or warrant demanding client files, communication records, or billing records. Alternatively, you are served with a court order requiring you to identify clients who attended a specific event or received services in connection with a specific case.

**Incident triggers**:
- Receipt of any legal process document (subpoena, CID, warrant) directed at client records
- A client reports that federal agents have contacted them and appear to have knowledge of your communication with them
- ICE or CBP appears at your office requesting information about clients (this is a warrantless administrative request that you can decline — but document it)
- A third-party provider (your email host, cloud storage provider) notifies you that they have received or are considering complying with a legal process request for your data

**Immediate response**:
1. Do not comply with any legal process without consulting your organization's general counsel or a pro bono attorney who handles government investigations. Time-limited compliance windows are real, but producing records before counsel reviews them is irreversible.
2. Invoke attorney-client privilege and work product doctrine at the earliest opportunity. Your supervising attorney should be involved within the hour of receiving any legal process document.
3. If clients are at risk: notify your organization's communication tree. Do not use the potentially compromised communication channel (if the subpoena targets your email, do not send notifications via that email system).
4. Document the date, time, and content of receipt, and preserve the original document.
5. Contact your state bar's ethics hotline — they provide free guidance on responding to subpoenas targeting privileged client communications.

**Who to contact**:
- National Immigration Law Center (NILC): https://www.nilc.org
- National Lawyers Guild (NLG) legal support: https://www.nlg.org
- ACLU Know Your Rights program: https://www.aclu.org
- Your state bar ethics hotline (for attorney-client privilege guidance)
- Electronic Frontier Foundation: https://www.eff.org (if the subpoena targets digital communications or stored records)

---

#### Scenario IL-2: Staff Device Seized or Compromised

**What it looks like**: An attorney or paralegal's device is seized at a border crossing, at a court appearance, or during a law enforcement action at a client event. Alternatively, you have reason to believe a device holding client records has been compromised (unusual behavior, security alerts, or a returned device after an extended seizure period).

**Incident triggers**:
- Device physically seized or requested by law enforcement or CBP
- Staff member reports their device was taken and returned after inspection
- Security software alerts to unusual outbound connections or unauthorized access
- Staff member's accounts show login activity from unfamiliar locations or devices
- A client reports that information from their file appears to have leaked to ICE

**Immediate response**:
1. Do not reconnect the returned device to your organization's network or any account until it has been evaluated. Firmware-level compromise (BootKitty) can survive a full OS reinstall and disk re-encryption.
2. Revoke the staff member's access credentials immediately from all organizational systems — not to punish them but to prevent the potentially compromised device from being used to authenticate to client database systems.
3. Identify which clients had files accessible on the device. Implement your notification protocol. Note: the ethics rules on notifying clients of a potential data breach vary by state bar — consult ethics counsel on the notification question before sending notifications that could themselves expose client information.
4. Replace the device. Do not attempt to restore and reuse a device that was in law enforcement custody.

**Who to contact**:
- Your organization's technical support contact for emergency credential revocation
- Your state bar ethics hotline for client notification guidance
- NILC for coordination support if the incident appears to be part of a broader enforcement pattern targeting your organization
- EFF Digital Security Helpline for forensic evaluation guidance: https://www.eff.org/pages/digital-security-helpline

---

#### Scenario IL-3: Organizational Financial Records Exposed Through IRS-Adjacent Palantir Query

**What it looks like**: You receive informal indication (through a source, a coalition partner, or a legal contact) that your organization's financial records — donor lists, payment records, grant receipts — have surfaced in a federal investigation that appears unrelated to your organization's work. Alternatively, donors begin reporting that they are receiving federal inquiries, or you learn through a FOIA request that your organization's name appears in enforcement-related records you did not expect to appear in.

**Incident triggers**:
- Unusual IRS inquiry or audit request that focuses on organizational relationships rather than tax compliance
- Donors contacting you to report government inquiries about their giving
- Coalition partners reporting that your organization's name surfaced in a legal process they received
- A news report references financial connections involving your organization in the context of a federal investigation

**Immediate response**:
1. Do not respond to any IRS or DOJ inquiry without legal counsel. Contact your organization's tax counsel and general counsel simultaneously.
2. Audit what financial relationship data your organization holds in publicly accessible or cloud-hosted form. The IRS Palantir platform reaches financial records in federal systems — but OSINT tools reach what you have published (annual reports, Form 990 public disclosures, grant acknowledgment posts).
3. Assess your donor notification obligations under your state's charitable solicitation statutes. In some states, organizations have duties to notify donors if donor information has been the subject of government inquiry.
4. Review your financial record retention and destruction policies. Records you are not legally required to hold are a discovery surface you can reduce prospectively.

**Who to contact**:
- Bolder Advocacy (Alliance for Justice): https://www.boldadvocacy.org — nonprofit advocacy law specialists
- Lawyers Committee for Civil Rights Under Law: https://lawyerscommittee.org
- Center for Constitutional Rights: https://ccrjustice.org
- Your state's nonprofit association legal referral service

---

## Sector 3: Educators and Academic Researchers

**Full briefing**: `phase-2-threat-briefing-academics.md`
**Distribution tier**: Phase 2 Priority Constituency 3
**Primary contacts**: University faculty, graduate researchers, diversity office administrators, researchers on federal grants, education equity advocates

### Briefing Summary (May 15, 2026)

DOJ civil rights investigations targeting DEI programs have moved beyond EEOC filings into active enforcement actions. 1,752 NSF grants were terminated under DOGE audit — the pattern of terminations (keyword-based review of grant text for political consistency) means that grant documentation in federal systems is a political exposure surface, not just a financial one. State AG coordination has produced civil investigative demands targeting gender studies curricula. Palantir's presence in NIH, DOJ, and NASA databases means cross-agency relationship-mapping is architecturally available against researcher records. The State Department's Catch and Revoke program is systematically monitoring international student and researcher social media, with visa revocations following.

---

### Tier 2 Playbook Integration — Educators

| Playbook | File | Priority | Customization Points |
|----------|------|----------|---------------------|
| Core OpSec | `opsec-playbook.md` | **Priority 1 — Foundation** | Device hardening for international travel; institutional vs. personal communications distinction |
| Device Hardening Guide | `device-hardening-guide.md` | **Priority 2 — Devices** | Border-crossing protocol for researchers traveling internationally; Before First Unlock (BFU) state for devices at checkpoints |
| Activist Organizing | `activist-organizing-playbook.md` | Priority 3 — Advocacy contexts | For faculty and student activists: Babel Street monitoring implications for academic protest participation |
| Immigration Surveillance Evasion | `phase-2-immigration-surveillance-evasion-playbook.md` | Priority 4 — International community | For advisors to international students and researchers: data broker opt-out and Catch and Revoke briefing materials |

**Deployment sequence**:
1. Begin with `opsec-playbook.md` and the institutional communications hygiene guidance — the boundary between institutional email (discoverable) and end-to-end encrypted personal communications is the most immediately actionable distinction
2. Add `device-hardening-guide.md` for researchers who travel internationally; the border-crossing protocol is the most time-sensitive piece (a device in BFU state at a border crossing is materially more protected than a device that is powered on)
3. Add `phase-2-immigration-surveillance-evasion-playbook.md` resources for advising international students and researchers on Catch and Revoke

**Org-specific customization**:
- **Individual faculty**: Communications hygiene (Signal for sensitive institutional discussions), data broker opt-out, social media review before any international travel
- **Graduate programs and research labs**: Brief incoming students and postdocs on Catch and Revoke during orientation. Brief international researchers on data broker exposure.
- **University administrators**: IRB consent language review for research involving at-risk populations; need-to-know access controls for grant databases; review institutional cloud storage provider compliance posture for U.S. legal process

---

### Escalation Scenarios — Educators

#### Scenario E-1: DOJ Civil Rights Investigation Targeting a Program or Department

**What it looks like**: Your institution's general counsel notifies faculty that DOJ has initiated a civil rights investigation under Executive Order 14151 targeting a program, department, or research area. Alternatively, a conservative watchdog group files a formal investigation request, and DOJ notifies the institution that the request is being considered. You receive a document preservation order covering institutional communications related to DEI programs, gender studies, immigration research, or related areas.

**Incident triggers**:
- Receipt of a DOJ inquiry letter, civil investigative demand, or document preservation order
- Institutional general counsel notification of a pending investigation
- Subpoena to the institution's email provider or cloud storage provider for records related to your program
- A former student or employee contacts you to report they have been interviewed by federal investigators about your program

**Immediate response**:
1. Do not delete or alter any records after receiving a preservation order — destruction of evidence after a preservation obligation attaches is a federal crime (obstruction of justice), regardless of the underlying merit of the investigation.
2. Contact your institution's general counsel immediately. Do not discuss the investigation with colleagues via institutional email (which is held by a cloud provider that will comply with legal process).
3. Consult AAUP (American Association of University Professors) if the investigation appears to target academic speech, curriculum, or research. AAUP has specific resources for faculty under government investigation.
4. Identify what communications and records exist in institutional systems versus personal systems. This is a legal question requiring counsel — the distinction matters for privilege and for the scope of any preservation obligation.
5. Do not speak with federal investigators without counsel present.

**Who to contact**:
- AAUP: https://www.aaup.org (academic freedom defense resources)
- FIRE (Foundation for Individual Rights and Expression): https://www.thefire.org (First Amendment resources for academic speech)
- National Center for Science Education: https://ncse.ngo (for researchers in contested scientific areas)
- Your institution's general counsel and faculty senate
- ACLU campus rights program: https://www.aclu.org/campus-rights

---

#### Scenario E-2: International Researcher or Student Targeted Through Catch and Revoke

**What it looks like**: An international student or researcher in your department receives a visa revocation notice, unexpectedly does not receive a visa renewal, or is detained at a port of entry. Review of their public social media suggests the action was triggered by political content — protest attendance, immigration advocacy, critical commentary on government policy.

**Incident triggers**:
- A department member receives a visa revocation notice or USCIS denial without a stated substantive reason
- DHS or ICE contacts your institution's international students and scholars office regarding a specific student or researcher
- A student or researcher reports being questioned at a border crossing about their social media content or political views
- Multiple international members of your department community experience visa difficulties in a short window — this may indicate targeted monitoring of your program

**Immediate response**:
1. Contact your institution's international students and scholars office and general counsel simultaneously. Many universities have emergency protocols for student or researcher visa emergencies.
2. For the individual affected: refer them immediately to an immigration attorney — not a general attorney, but one who handles federal immigration enforcement matters. Time is critical in visa revocation proceedings.
3. Do not advise the individual to delete or alter social media. This could be characterized as destruction of evidence and may harm their legal case.
4. Document the timeline: when the content was posted, when the visa action occurred, any government communications received.
5. Coordinate with your institution's communications office if the situation becomes public — media attention can sometimes affect the pace of administrative proceedings.

**Who to contact**:
- NILC (National Immigration Law Center): https://www.nilc.org — for immigration attorney referrals
- American Immigration Lawyers Association (AILA): https://www.aila.org — member referral directory
- ACLU Immigrants' Rights Project: https://www.aclu.org/immigrants-rights
- Your institution's international students and scholars office
- NAFSA: Association of International Educators: https://www.nafsa.org — institutional resources

---

#### Scenario E-3: Research Data on At-Risk Populations Potentially Accessed Through Cross-Agency Query

**What it looks like**: You learn that a federal agency has accessed, subpoenaed, or attempted to access research data you collected on a vulnerable population (undocumented immigrants, political activists, LGBTQ+ individuals, religious minorities). Alternatively, you receive a FOIA request or civil discovery request seeking research data, IRB protocols, or participant contact information.

**Incident triggers**:
- A subpoena or court order targeting your research data, IRB files, or participant records
- A federal agency (NIH, NSF, DOJ, DHS) requests access to data collected under a federal grant
- A participant in your research contacts you to report that federal agents have questioned them and appear to have information from your research
- Your IRB notifies you of an external access request to your research files

**Immediate response**:
1. Invoke the research privilege where applicable. Federal common law recognizes a qualified researcher privilege for academic research data — it is not absolute but it provides a procedural basis to contest the request. The privilege is stronger when data is collected under IRB protocols with explicit confidentiality assurances.
2. Contact your IRB immediately. IRBs have legal counsel resources and procedures for exactly this scenario.
3. Do not voluntarily provide participant-identifying data to any government agency without a court order and review by institutional legal counsel.
4. Notify your institution's general counsel and research compliance office.
5. Consider emergency de-identification if you are not already under a preservation order. If participant-identifying data can be destroyed lawfully (not yet under preservation obligation), do so. The best protection is data you do not have.

**Who to contact**:
- Your institution's IRB and general counsel
- American Association for the Advancement of Science (AAAS) science policy resources: https://www.aaas.org
- Human Rights Watch (if the research is human rights-related): https://www.hrw.org
- ACLU: https://www.aclu.org
- Reporters Committee for Freedom of the Press (if the research data was collected in a journalistic capacity): 1-800-336-4243

---

## Sector 4: Labor and Civil Rights Organizers

**Full briefing**: `phase-2-threat-briefing-labor-organizers.md`
**Distribution tier**: Phase 2 Priority Constituency 4
**Primary contacts**: AFL-CIO affiliates, independent unions, worker centers, UAW, CWA, AFT regional contacts, domestic worker networks

### Briefing Summary (May 15, 2026)

Penlink PLX converts union meeting attendance and rally participation into persistent location history accessible to DHS without a warrant. Babel Street's persistent monitoring means that publicly visible organizers — shop stewards, union social media managers, public advocates — are likely already permanently flagged for continuous monitoring. Flock Safety ALPR captures vehicle identities at organizing events and stores them indefinitely. The UAW/CWA/AFT lawsuit documents a 40–80% chilling effect on protected labor speech among members aware of the surveillance. DHS administrative subpoenas have compelled Google, Meta, and Discord to identify anonymous organizer accounts. The NLRB's rollback of Abruzzo-era electronic monitoring guidance has removed procedural protections for workers in surveilled organizing environments.

---

### Tier 2 Playbook Integration — Organizers

| Playbook | File | Priority | Customization Points |
|----------|------|----------|---------------------|
| Activist Organizing | `activist-organizing-playbook.md` | **Priority 1 — Core** | Role-specific guidance (communications coordinator, legal observer, frontline organizer); vehicle/ALPR protocol; drone surveillance awareness |
| Phase 2 Activist Organizing | `phase-2-activist-organizing-security-playbook.md` | **Priority 2 — Condensed** | Condensed May 2026 protocol for rapid deployment; use as the handout version |
| Core OpSec | `opsec-playbook.md` | Priority 3 — Foundation | Device hardening baseline; border-crossing protocol for organizers who travel for campaigns |
| Immigration Surveillance Evasion | `phase-2-immigration-surveillance-evasion-playbook.md` | Priority 4 — Member protection | For campaigns involving immigrant workers: client-facing data broker opt-out and device protocols |

**Deployment sequence**:
1. Begin with `phase-2-activist-organizing-security-playbook.md` — the condensed version is the fastest path to the most critical protocol (social media compartmentalization, Signal for internal communications, vehicle ALPR awareness)
2. Extend to `activist-organizing-playbook.md` for communications coordinators and leadership roles who need the full counter-surveillance framework
3. Add `phase-2-immigration-surveillance-evasion-playbook.md` for organizing campaigns in sectors with immigrant worker participation — this is the client-side complement to the organizer-side playbook

**Org-specific customization**:
- **Union headquarters and AFL-CIO affiliates**: Organizational social media account protocols (separation of internal communications from public accounts); DHS administrative subpoena response procedures for platform accounts used in organizing.
- **Worker centers**: Member communications with immigration vulnerability are the specific high-priority item — share data broker opt-out materials as standard intake. Brief staff on Penlink implications for in-person event attendance.
- **Civil rights organizations in the labor space**: The Babel Street monitoring means public-facing legal and policy advocates (not just frontline organizers) are surveillance subjects. Review all staff social media profiles for content that could trigger Catch and Revoke for non-citizen staff or associate members.

---

### Escalation Scenarios — Organizers

#### Scenario O-1: DHS Administrative Subpoena Targeting Organizational Accounts

**What it looks like**: You receive notification (from the platform, from a legal contact, or through press coverage) that DHS has issued an administrative subpoena to a platform (Google, Meta, Discord, Reddit) seeking the identity of accounts associated with your organization or campaign. Alternatively, you learn that an anonymous account operated by your organization has been identified by federal authorities.

**Incident triggers**:
- Platform notifies you that it has received or is considering complying with a subpoena for account information
- A press report mentions a subpoena targeting anonymous accounts in a campaign you are associated with
- Federal agents contact you directly about accounts or communications they appear to already know are associated with you
- A coalition partner reports that accounts associated with your network have been identified in a federal legal proceeding

**Immediate response**:
1. Do not delete any account or content. This is the most critical error to avoid — deletion after a legal process exists can be characterized as obstruction.
2. Contact the ACLU, NLG, or EFF immediately for legal support. All three organizations have experience defending labor organizations against government subpoenas targeting organizing activity.
3. If the subpoena has not yet been served on you directly, you may have time to contest it before the platform complies. The Electronic Frontier Foundation has contested overbroad administrative subpoenas. Engage legal counsel immediately.
4. Audit all organizational accounts for connections to personal identifiers (personal email used for account registration, phone numbers, payment methods). Document what is discoverable — your legal team needs this information.
5. Notify your organization's leadership and legal committee of the situation.

**Who to contact**:
- EFF: https://www.eff.org — digital rights legal support; has contested DHS administrative subpoenas
- ACLU: https://www.aclu.org — civil liberties legal representation
- National Lawyers Guild: https://www.nlg.org — labor and political organizing legal support
- Labor law counsel familiar with NLRA Section 7 (protected concerted activity) — administrative subpoenas targeting labor organizing activity may be challengeable on labor law grounds in addition to First Amendment grounds

---

#### Scenario O-2: Infiltration Detection — Agent or Informant in the Organization

**What it looks like**: You have reason to believe that an individual inside your organization — a member, a volunteer, a coalition partner — is sharing internal communications and planning information with law enforcement or employer representatives. Indicators may include: enforcement actions that appeared timed to internal organizational decisions, employer behavior that reflects knowledge of non-public campaign strategy, or a direct tip from a reliable source.

**Incident triggers**:
- A picket action, a workplace action, or an organizing meeting produces an employer or law enforcement response that could only have been anticipated with advance knowledge of your plans
- You receive information (from a trusted source, or through a legal proceeding) that an individual in your organization has been in contact with management, law enforcement, or a security firm
- Internal communications or materials appear in external contexts (employer communications, court filings, media reports) without a plausible explanation other than insider access
- An individual in your organization asks questions that seem designed to elicit information about internal structures, member identities, or planned actions — particularly someone who joined recently or with limited verifiable background

**Immediate response**:
1. Do not confront the suspected informant directly. This can compromise any future legal claims and can endanger members if the suspicion is wrong.
2. Compartmentalize information immediately. Move sensitive planning to a smaller group operating on a separate communication channel. Do not explain the change organizationally — implement it quietly.
3. Consult with your organization's legal counsel or the NLG before taking any action. The NLG has specific guidance on informant detection and response within labor and organizing contexts.
4. Preserve evidence of the infiltration indicators — the timeline of decisions followed by employer or law enforcement responses, the nature of questions asked, any documentation.
5. Consider whether a trusted security or counter-intelligence professional should evaluate your organizational communications environment. The EFF and NLG can refer appropriate resources.

**Who to contact**:
- National Lawyers Guild: https://www.nlg.org — has specific experience advising organizations on government infiltration of labor and political groups
- ACLU: https://www.aclu.org
- EFF Digital Security Helpline: https://www.eff.org/pages/digital-security-helpline
- Your labor law counsel for NLRA-related advice on employer surveillance of organizing activity

---

#### Scenario O-3: ICE Enforcement at an Organizing Event

**What it looks like**: ICE or CBP agents appear at a union meeting, a rally, a worker center event, or a picket line and begin detaining workers. This is documented as an employer retaliation tactic in the current enforcement environment — employers with knowledge of organizing campaigns have in some documented cases cooperated with ICE to initiate enforcement actions during organizing activity.

**Incident triggers**:
- Federal agents appear at any organizing event where immigrant workers are present
- Workers at an organizing event are approached, questioned, or detained by individuals who identify themselves as federal agents or who do not identify themselves
- An employer or security firm representative appears at an organizing event alongside people who appear to be law enforcement

**Immediate response**:
1. Know Your Rights cards in all languages spoken by your members. Workers do not have to answer questions about their immigration status. Workers have the right to remain silent. Workers have the right to speak to an attorney.
2. Contact a Know Your Rights legal observer or hotline immediately. Many local NLG chapters maintain rapid-response legal observer networks.
3. Document everything: photographs and video of what is happening (which all workers have the right to take in public), names of agents if visible on badges, badge numbers if visible, descriptions of vehicles.
4. Activate your organization's rapid response tree. Pre-established networks of attorneys, community organizations, and media contacts can respond faster when the contact list exists before the incident.
5. File an NLRA unfair labor practice charge if there is evidence that the ICE enforcement action was initiated by or coordinated with the employer.

**Who to contact**:
- NLG rapid-response legal observers: find your local chapter at https://www.nlg.org
- NILC: https://www.nilc.org — for worker immigration rights
- ACLU: https://www.aclu.org
- Your union's legal department and the appropriate NLRB regional office for an unfair labor practice charge: https://www.nlrb.gov/about-nlrb/regional-offices

---

## Sector 5: Faith Leaders and Spiritual Communities

**Full briefing**: `phase-2-threat-briefing-faith-leaders.md`
**Distribution tier**: Phase 2 Priority Constituency 5
**Primary contacts**: Sanctuary congregations, interfaith coalitions, denominational social justice offices, chaplains serving immigrant communities

### Briefing Summary (May 15, 2026)

The January 20, 2025 rescission of the sensitive location policy ended 14 years of de facto protection for houses of worship as enforcement-free zones. ICE has conducted operations at church properties in Georgia, North Carolina, California, and Louisiana. A February 2026 preliminary injunction protects named congregations but not the general sanctuary movement. Church management software stores congregant data (names, addresses, household composition) in cloud databases that comply with U.S. legal process. Penlink PLX converts congregant phone presence at sanctuary services into persistent location records accessible to DHS. Publicly active faith leaders are likely already under Babel Street persistent monitoring. DOJ's Task Force on Eradicating Anti-Christian Bias has created an enforcement posture that applies selectively — specifically against progressive religious communities engaged in immigration advocacy.

---

### Tier 2 Playbook Integration — Faith Leaders

| Playbook | File | Priority | Customization Points |
|----------|------|----------|---------------------|
| Core OpSec | `opsec-playbook.md` | **Priority 1 — Foundation** | Device hardening; PIN vs. biometric unlock; communications hygiene for pastoral care |
| Device Hardening Guide | `device-hardening-guide.md` | **Priority 2 — Devices** | Full-disk encryption for pastoral devices; BFU state guidance for devices holding congregant information |
| Activist Organizing | `activist-organizing-playbook.md` | **Priority 3 — Publicly active leaders** | For faith leaders engaged in public immigration advocacy: Babel Street, drone surveillance, ALPR at public events |
| Phase 2 Activist Organizing | `phase-2-activist-organizing-security-playbook.md` | Priority 4 — Condensed | Condensed protocol; the handout version for faith leaders who need a quick-start reference |

**Deployment sequence**:
1. Begin with `opsec-playbook.md` — the device hardening and communications hygiene guidance is the foundation; specifically the PIN vs. biometric guidance, which is immediately actionable and requires no technology purchase
2. Add `device-hardening-guide.md` for faith leaders who hold congregant records on personal or organizational devices
3. For publicly active faith leaders (those who participate in protests, sanctuary operations, or public advocacy events): add the activist organizing playbook

**Org-specific customization**:
- **Sanctuary congregations**: Congregant data audit is the immediate priority — understanding what your church management software holds and whether it needs to hold it. Phone-free protocol for sanctuary spaces is the operational complement.
- **Denominational offices**: Centralized databases of member congregations and affiliated staff create a large discovery surface. Review what is held centrally and whether field-level data should be decentralized.
- **Interfaith coalitions**: Coalition membership lists and coordination communications are a surveillance surface. Signal should be the default for inter-organizational coordination about sanctuary or immigration advocacy activity.

---

### Escalation Scenarios — Faith Leaders

#### Scenario F-1: Federal Agents Appear at Your Property Requesting Congregant Information

**What it looks like**: Federal agents (ICE, FBI, DHS) appear at your church, synagogue, mosque, or temple — either requesting a meeting with you, appearing at the property during worship or service hours, or appearing during an event at which immigrant community members are present. They request the names and addresses of congregants, or present a document requesting access to membership records.

**Incident triggers**:
- Federal agents appear at your property and request congregant information (names, addresses, immigration status)
- Agents present what they describe as a "request" for records — this may or may not be a legal process document; the distinction matters legally
- Agents are present at the property during an active service or event and begin interacting with congregants
- You receive a formal subpoena, civil investigative demand, or court order demanding access to membership records

**Immediate response**:
1. Do not provide any names, addresses, or information about congregants without consulting legal counsel. A "request" without a court order is not legally compellable. Even a court order may be contestable.
2. Calmly ask agents to identify themselves, their agency, and the legal authority for their presence or request. You are entitled to this information.
3. Tell the agents that your attorney will contact them. Then call your legal counsel.
4. If agents are on private property and you have not given consent for their presence: you may ask them to leave. If they have a warrant, ask to see it and have your attorney review it before complying.
5. Do not lie to federal agents. You can decline to speak without lying — "I am not going to answer questions without my attorney present" is a complete response.
6. Notify your denominational leadership, interfaith coalition partners, and any congregation members in leadership roles — not by mass email (which creates a record) but through your established pastoral leadership structure.

**Who to contact**:
- Becket Fund for Religious Liberty: https://www.becketlaw.org — religious freedom legal defense
- ACLU: https://www.aclu.org — First Amendment and religious freedom
- NLG: https://www.nlg.org — rapid-response legal support for communities under federal pressure
- Your denominational office's legal counsel or social justice team
- Faith in Action: https://faithinaction.org — national interfaith advocacy network
- Church World Service (for sanctuary congregations): https://cwsglobal.org

---

#### Scenario F-2: ICE Conducts an Enforcement Operation at Your Property or an Adjacent Location

**What it looks like**: ICE agents conduct an enforcement operation at or immediately adjacent to your property — at a parking lot event, during a food pantry operation, or in the immediate vicinity of your building during a worship service. Congregants are approached, questioned, or detained.

**Incident triggers**:
- Congregants or staff report ICE agent presence at the property during an event
- An enforcement action occurs in your parking lot, in an adjacent street, or at an event your congregation is hosting
- You witness federal agents following congregants who have left your property
- An enforcement action targets an individual who was on church property within the preceding hours

**Immediate response**:
1. Activate your sanctuary congregation's established response protocol if one exists. If not, the first priority is to ensure that vulnerable individuals know their rights: they have the right to remain silent, the right to not answer questions about immigration status, and the right to speak to an attorney.
2. Document what is happening: photographs, video, badge numbers if visible, vehicle plates, time and location. This documentation is essential for legal challenges.
3. Call the NLG or your local legal observer network immediately. In many cities, faith communities and legal observer networks have pre-established rapid-response protocols — activate yours if it exists.
4. Do not physically obstruct agents who have a lawful warrant. This protects you from obstruction charges and preserves your ability to challenge the action in court.
5. After the incident: submit a formal report to CPJ (if it involves a journalist), the ACLU, and your denominational advocacy office. Documentation of enforcement at religious sites is the primary evidentiary basis for future legal challenges to the policy.

**Who to contact**:
- NLG local chapter rapid response: https://www.nlg.org
- ACLU: https://www.aclu.org
- Church World Service: https://cwsglobal.org
- Your denominational headquarters
- RAICES (for referral to immigration legal support for detained individuals): https://www.raicestexas.org
- NILC: https://www.nilc.org

---

#### Scenario F-3: A Congregation Member Is Detained Through Location Data or Social Media Monitoring

**What it looks like**: A congregation member is detained or faces immigration enforcement, and there is reason to believe the enforcement action was initiated through location data (Penlink PLX) generated by their phone's presence at church events, or through social media monitoring (Babel Street) that documented their association with your congregation's public advocacy activity.

**Incident triggers**:
- A congregation member is detained and reports that ICE agents referenced specific events, locations, or associations that could only have been known through surveillance
- Multiple congregation members face enforcement actions within a short timeframe following a high-visibility public event hosted by your congregation
- You learn that ICE has generated a profile of your congregation that documents which individuals attend sanctuary services
- A detained member's attorney indicates that the government's evidence appears to include location history or social media content from your congregation's activities

**Immediate response**:
1. Immediately refer the detained individual to an immigration attorney. Do not rely on general legal resources for this — immigration detention is time-sensitive and requires specialized counsel.
2. Contact RAICES, NILC, and your local immigration legal aid network with the individual's name, detention location, and contact information.
3. Implement the phone-free protocol for sanctuary spaces prospectively if you have not already. This is the primary countermeasure against Penlink-based location surveillance.
4. If there is evidence that Babel Street social media monitoring was a factor: review and archive (do not delete) the social media content that may have triggered the monitoring. This documentation is relevant to First Amendment legal challenges.
5. Assess whether the pattern of detentions reflects targeting of your congregation specifically — if so, this is a legal case worth bringing, not just an individual to defend.

**Who to contact**:
- RAICES: https://www.raicestexas.org
- NILC: https://www.nilc.org
- ACLU Immigrants' Rights Project: https://www.aclu.org/immigrants-rights
- EFF (for the social media monitoring dimension): https://www.eff.org
- Your denominational office's legal resources and social justice networks

---

## Deployment Integration: Sector-to-Playbook Cross-Reference

The following table provides a complete cross-reference of which cybersecurity-hardening playbooks apply to which sectors, in priority order. Use this table for Tier 2 outreach preparation — each sector's email can reference the specific playbooks most relevant to that recipient.

| Playbook | Journalists | Immigration Legal Aid | Educators | Organizers | Faith Leaders |
|----------|-------------|----------------------|-----------|------------|---------------|
| `journalist-security-playbook.md` | **P1 — Core** | — | — | — | — |
| `journalist-security-playbook-extended.md` | **P2 — Extended** | — | — | — | — |
| `phase-2-immigration-surveillance-evasion-playbook.md` | Reference for source protection | **P1 — Core** | P4 (intl. students) | P4 (immigrant members) | — |
| `immigration-attorney-implementation-guide.md` | — | **P2 — Staff** | — | — | — |
| `activist-organizing-playbook.md` | P4 (protest beats) | — | P3 (activist faculty) | **P1 — Core** | P3 (public leaders) |
| `phase-2-activist-organizing-security-playbook.md` | — | — | — | **P2 — Condensed** | P4 — Condensed |
| `opsec-playbook.md` | P3 | P3 | **P1** | P3 | **P1** |
| `device-hardening-guide.md` | Included in journalist guides | Included in attorney guide | **P2** | P3 | **P2** |
| `financial-resistance-playbook.md` | — | P4 (nonprofit exposure) | — | P4 (union finances) | P4 (organizational donors) |
| `whistleblower-playbook.md` | P2 (source protection) | — | — | P3 (workers with evidence) | — |

---

## June 12 Policy Window: All-Sector Action

Regardless of sector, the FISA Section 702 June 12 legislative deadline represents the highest-leverage near-term policy action available:

**The ask**: Contact your senators before June 5 to support the data broker loophole provision of the Government Surveillance Reform Act (S.4082, sponsors: Wyden, Lee, Davidson, Lofgren). This provision would prohibit federal agencies from purchasing cell phone location data and browsing history from commercial data brokers without a warrant — the specific mechanism by which ICE and DHS currently acquire location data (Penlink PLX, advertising SDK networks) without any court process.

**Who can act**: Any organization with a membership email list, a newsletter audience, or a social media following can direct constituent advocacy to this deadline. The five sectors described in this document — journalists, legal aid organizations, educational institutions, labor organizations, and faith communities — all have internal communications channels that can reach their members with this ask.

**Minimum viable action**: A single email to members with a link to Contact Congress (https://www.contactcongress.org) and the specific ask: "Contact your senators before June 5, ask them to support the data broker loophole provision of S.4082."

---

## Sources

All findings are grounded in the primary-source research documented in the individual sector briefings and the May 2026 threat landscape analysis. Key cross-sector sources:

1. Prism Reports: DHS Buying Access to Real-Time Location Data via Penlink PLX — https://prismreports.org/2026/04/29/dhs-surveillance-location-data-penlink-plx/
2. The Intercept: Palantir IRS Cross-Agency Relationship Mapping — https://theintercept.com/2026/04/24/palantir-irs-contract-data/
3. Biometric Update: ICE Advances Sole-Source Deal with Palantir for New Surveillance Backbone — https://www.biometricupdate.com/202506/ice-advances-sole-source-deal-with-palantir-for-new-surveillance-backbone
4. EFF: Labor Unions, EFF Sue Trump Administration over Ideological Surveillance — https://www.eff.org/press/releases/labor-unions-eff-sue-trump-administration-stop-surveillance-free-speech-online
5. Citizen Lab: Paragon Solutions Graphite Spyware Targeting Journalists — https://citizenlab.ca/2025/02/paragon-solutions-graphite-spyware-targeting-journalists/
6. Security Boulevard: Congress Punts FISA 702 to June — https://securityboulevard.com/2026/05/congress-punts-fisa-section-702-renewal-to-june/
7. Religion News Service: How the Sanctuary Movement Became the Faithful's Answer to ICE Raids — https://religionnews.com/2026/03/23/how-the-sanctuary-movement-became-the-faithfuls-answer-to-ice-raids/
8. Inside Higher Ed: DOJ Declares DEI Practices Unlawful — https://www.insidehighered.com/news/government/2025/07/30/doj-declares-slew-dei-practices-unlawful-memo
9. APS News: NSF Lags in Grant Awards — https://www.aps.org/apsnews/2026/04/nsf-lags-trump-proposes-cuts
10. EFF: How Cops Are Using Flock Safety to Surveil Protesters and Activists — https://www.eff.org/deeplinks/2025/11/how-cops-are-using-flock-safetys-alpr-network-surveil-protesters-and-activists/
11. Word & Way: Judge Freezes ICE Raids at Some Baptist, Lutheran, and MCC Churches — https://wordandway.org/2026/02/14/judge-freezes-ice-raids-at-some-baptist-lutheran-mcc-churches/
12. Freedom of the Press Foundation: Post-Bondi Memo Resources — https://freedom.press
13. Wyden Senate: Government Surveillance Reform Act — https://www.wyden.senate.gov/news/press-releases/wyden-lee-davidson-and-lofgren-introduce-bill-to-reform-fisa-section-702-protect-americans-constitutional-rights-and-plug-data-broker-surveillance-loophole

---

*Master document date: May 15, 2026. Individual sector briefings dated May 7, 2026. Corpus reflects surveillance and enforcement landscape as documented through May 15, 2026. Quarterly review: August 15, 2026.*

*Individual sector briefings for PDF export: phase-2-threat-briefing-journalists.md, phase-2-threat-briefing-immigration-legal-aid.md, phase-2-threat-briefing-academics.md, phase-2-threat-briefing-labor-organizers.md, phase-2-threat-briefing-faith-leaders.md*
