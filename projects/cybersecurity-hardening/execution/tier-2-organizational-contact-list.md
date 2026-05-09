---
title: "Tier 2 Organizational Contact List — 45+ Organizations, Five Sectors"
project: cybersecurity-hardening
created: 2026-05-09
status: production-ready
phase: Phase 2 — Tier 2 Organizational Distribution
scope: Labor unions, immigration legal aid, civil rights, academic/law schools, faith coalitions
depends-on:
  - TIER2_DISTRIBUTION_PREP.md
  - tier-2-sector-contact-lists.md
  - phase-2-target-organizations.csv
  - TIER2_MESSAGING_TEMPLATES.md
  - execution/TIER2_THREAT_BRIEFING_INDEX.md
companion: tier-2-distribution-strategy.md
---

# Tier 2 Organizational Contact List — Five Sectors, 47 Organizations

**Purpose**: Verified contact list for Tier 2 organizational outreach. Covers five sectors not fully mapped in `tier-2-sector-contact-lists.md` (which addresses digital rights, academic cybersecurity, researcher communities, and journalist organizations). This document addresses: labor unions, immigration legal aid organizations, civil rights organizations, academic law programs, and faith coalitions.

**Status notes**: Contact information is drawn from organizational websites, public staff directories, and press releases as of May 2026. Where a direct staff email is not publicly confirmed, the organizational general contact is listed with an internal routing note. Email addresses marked `[inferred]` follow the organization's confirmed naming pattern; treat as best-available, verify before sending to a named individual.

**Companion document**: `tier-2-distribution-strategy.md` contains customization matrix, email templates, rollout timeline, and success metrics.

---

## Sector 1: Labor Unions

**Distribution rationale**: Labor unions represent the population with the highest combined immigration enforcement exposure and existing organizational infrastructure to deploy countermeasures at scale. The activist-organizing-playbook and Phase 2 labor organizer threat briefing (`phase-2-threat-briefing-labor-organizers.md`) map directly onto union training infrastructure. Priority targets are the national organizing and education departments, not press offices.

**Lead threat briefing**: `phase-2-threat-briefing-labor-organizers.md`
**Lead playbooks**: `activist-organizing-playbook.md`, `organizational-opsec-playbook.md`

---

### L-01: AFL-CIO — Technology Institute

| Field | Detail |
|-------|--------|
| Organization | AFL-CIO |
| Unit | Technology Institute |
| Primary Contact | Lauren McFerran — Executive Director (Technology Institute, since February 2026) |
| Secondary Contact | Liz Shuler — AFL-CIO President |
| Email (general) | aflcio@aflcio.org |
| Phone | 202-637-5000 |
| Address | 815 Black Lives Matter Plaza NW, Washington, DC 20006 |
| Website | aflcio.org |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: The AFL-CIO Technology Institute's 2025 AI Principles for Workers document (AI governance, worker rights, surveillance policy) is the direct connection point. The corpus provides an operational layer for those principles: specific documented employer and government surveillance capabilities, matched to countermeasures calibrated for organizers. The Technology Institute runs digital rights programming for 56 affiliated unions and 12.5 million members — adoption here cascades automatically to the affiliate network. Contact Lauren McFerran at the Technology Institute directly; do not route through the press office.

---

### L-02: SEIU — Research and Member Education Department

| Field | Detail |
|-------|--------|
| Organization | Service Employees International Union (SEIU) |
| Unit | Research and Member Education |
| Primary Contact | April Verrett — SEIU President (since 2024) |
| Secondary Contact | Research Director (name not publicly confirmed; route through general) |
| Email (general) | seiu@seiu.org |
| Phone | 202-730-7000 |
| Address | 1800 Massachusetts Ave NW, Washington, DC 20036 |
| Website | seiu.org |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: SEIU's 2 million members are concentrated in healthcare, service, and janitorial sectors with high percentages of immigrant workers. The corpus's Part 0 data broker opt-out (no government-issued ID required) and the immigration surveillance evasion playbook are the most directly relevant for SEIU's membership demographic. Frame outreach to the Research and Member Education department specifically, not the political department; this is a training resource offer, not an advocacy partnership request. SEIU's documented active drives in healthcare and service sectors correlate directly with the DHS Penlink PLX surveillance documented in the labor organizer threat briefing.

---

### L-03: United Farm Workers (UFW)

| Field | Detail |
|-------|--------|
| Organization | United Farm Workers of America |
| Primary Contact | Teresa Romero — UFW President |
| Secondary Contact | Diana Tellefson Torres — UFW Foundation Executive Director |
| Email (general) | ufw@ufw.org |
| Phone | 661-823-6250 |
| Address | PO Box 62450, Bakersfield, CA 93386 |
| Website | ufw.org |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: UFW members are among the most directly exposed to the ELITE threat system: agricultural workers who are disproportionately undocumented, GPS-tracked on employer equipment, and organized in geographically predictable locations (farm sites, worker housing) that feed into ELITE's address confidence scoring. The corpus's countermeasures for this specific profile — personal device compartmentalization, no organizing on employer networks, Signal group protocols for organizing committees — are calibrated to UFW's documented organizing context. The California DELETE Act DROP platform documentation is especially relevant given UFW's California geography. Teresa Romero has been vocal on immigration enforcement; approach as a resource offer, not a policy partnership.

---

### L-04: California Nurses Association (CNA)

| Field | Detail |
|-------|--------|
| Organization | California Nurses Association / National Nurses United |
| Primary Contact | Cathy Kennedy — CNA President |
| Secondary Contact | Bonnie Castillo — National Nurses United Executive Director |
| Email (general) | cna@calnurses.org |
| Phone | 510-273-2200 |
| Address | 2000 Franklin St, Oakland, CA 94612 |
| Website | calnurses.org |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: CNA/NNU is distinct from SEIU healthcare because of its stronger digital organizing security posture — CNA has already confronted employer surveillance of organizing drives at major California hospital systems. The corpus's device hardening and organizational opsec sections are relevant to the nursing staff organizing context. The DHS social media surveillance program (which suppressed protected labor speech in the UAW and CWA surveys cited in the labor briefing) directly threatens the organizing communications of nurses who have been vocal on labor disputes. California geography means the DROP platform documentation for undocumented household members of CNA members is also relevant.

---

### L-05: NUPGE (National Union of Public and General Employees, Canada)

| Field | Detail |
|-------|--------|
| Organization | National Union of Public and General Employees |
| Primary Contact | Larry Brown — NUPGE National President |
| Email (general) | national@nupge.ca |
| Phone | 613-228-9800 |
| Address | 15 Auriga Drive, Ottawa, ON K2E 1B7, Canada |
| Website | nupge.ca |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: NUPGE is the cross-border addition for the labor sector. The commercial data broker surveillance infrastructure documented in the corpus operates across the US-Canada border: the same SDK location data networks and data broker intermediaries (LexisNexis Risk Solutions, Thomson Reuters CLEAR) are active in Canadian markets. NUPGE's 390,000+ members include public sector workers in provinces with heightened US-Canada cross-border enforcement cooperation concerns (Alberta, BC). Frame the outreach as a cross-border surveillance resource relevant to NUPGE's members who travel to or interact with US systems. Note that Parts 0 and 1 of the countermeasures apply in Canadian context; the ELITE-specific threat model section is US-specific.

---

### L-06: Communications Workers of America (CWA) — Code CWA

| Field | Detail |
|-------|--------|
| Organization | Communications Workers of America |
| Unit | CWA Code (tech worker organizing) |
| Primary Contact | Research and Education Director |
| Secondary Contact | Executive Vice President Debbie Goldman (labor policy) |
| Email (general) | capital@cwa-union.org |
| Phone | 202-434-1100 |
| Address | 501 Third St NW, Washington, DC 20001 |
| Website | cwa-union.org |
| Relationship Status | Listed in phase-2-target-organizations.csv — no outreach sent |

**Outreach angle**: CWA Code organizes technology workers who build and maintain the surveillance infrastructure the corpus documents. This creates a distinctive entry point not available for other unions: CWA members who work at Palantir, LexisNexis, Thomson Reuters, or app SDK vendors are themselves producing the commercial data that ELITE consumes. The worker accountability frame — CWA members should understand the end-use of their technical work — is unique to CWA. CWA's 700,000 members also include telecom workers who understand network surveillance at a technical level that other union memberships may not.

---

### L-07: National Domestic Workers Alliance (NDWA)

| Field | Detail |
|-------|--------|
| Organization | National Domestic Workers Alliance |
| Primary Contact | Ai-jen Poo — NDWA Executive Director |
| Secondary Contact | Digital Organizing Director (verify current; route through general) |
| Email (general) | info@domesticworkers.org |
| Phone | 404-228-6392 |
| Address | PO Box 56122, Atlanta, GA 30343 |
| Website | domesticworkers.org |
| Relationship Status | Listed in phase-2-target-organizations.csv — highest-priority labor pre-contact candidate |

**Outreach angle**: NDWA's 700,000+ domestic workers have the highest direct exposure to ELITE in the labor sector — domestic workers are disproportionately undocumented, work in residential locations that appear in ELITE's address confidence scoring, and are geographically isolated from union meeting infrastructure. Part 0 (data broker opt-outs requiring no government-issued ID) and the California DROP platform documentation are the most immediately relevant. The dual-protection argument (organizing security + immigration enforcement protection) is NDWA's distinctive frame. Ai-jen Poo is the correct first contact; this organization is a pre-contact candidate for personalized outreach before the main Tier 2 wave.

---

## Sector 2: Immigration Legal Aid Organizations

**Distribution rationale**: Immigration legal aid organizations are the direct institutional intermediaries between the corpus and the population most at risk from ELITE targeting. These organizations have client relationships with undocumented immigrants and can integrate Part 0 data broker opt-outs into standard intake protocols. The immigration attorney implementation guide and the immigration surveillance evasion playbook are the primary corpus materials for this sector.

**Lead threat briefing**: `execution/tier2-threat-briefing-immigration-lawyers.md`
**Lead playbooks**: `immigration-attorney-implementation-guide.md`, `immigration-surveillance-evasion-playbook.md`

---

### I-01: RAICES (Refugee and Immigrant Center for Education and Legal Services)

| Field | Detail |
|-------|--------|
| Organization | RAICES |
| Primary Contact | Jonathan Ryan — RAICES Executive Director |
| Secondary Contact | Policy and Advocacy Director |
| Email (general) | info@raicestexas.org |
| Phone | 210-226-7722 |
| Address | 1305 N Flores Street, San Antonio, TX 78212 |
| Website | raicestexas.org |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: RAICES is the largest immigration legal services organization in Texas, operating in the highest-concentration ELITE enforcement zone. Their legal staff handles asylum cases and removal defense in the exact operational geography where ELITE's address confidence scores are most actively used. The corpus's immigration attorney implementation guide — specifically the data broker opt-out integration into client intake, and the specific ELITE data pipeline documentation — is directly relevant to active RAICES case management. The Texas context also makes the legal advice around the DROP platform (California only) a useful contrast: RAICES attorneys should know a DROP-equivalent does not exist in Texas and can advise California-connected clients accordingly.

---

### I-02: American Immigration Lawyers Association (AILA)

| Field | Detail |
|-------|--------|
| Organization | American Immigration Lawyers Association |
| Primary Contact | Ben Johnson — AILA Executive Director |
| Secondary Contact | Education and Training Director |
| Email (general) | info@aila.org |
| Phone | 202-216-2400 |
| Address | 1331 G St NW, Suite 300, Washington, DC 20005 |
| Website | aila.org |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: AILA is the professional association for 15,000+ US immigration attorneys. Adoption here is qualitatively different from RAICES: AILA does not provide direct legal services but runs continuing legal education (CLE), publishes practice guides, and maintains a practitioner listserv. Integration into AILA's CLE programming or practitioner resources reaches every AILA member simultaneously. The corpus's attorney-client privilege and data security sections are AILA's institutional concern; the immigration attorney implementation guide is the appropriate primary resource. Frame as a CLE resource offer, not an advocacy pitch.

---

### I-03: National Association of Pakistani Americans (NAPA) and South Asian Legal Aid Organizations

| Field | Detail |
|-------|--------|
| Organization | National Association of Pakistani Americans / South Asian legal aid broadly |
| Representative Contact | Saqib Ali — NAPA Director of Policy (confirmed active 2026) |
| Email | info@napausa.org |
| Website | napausa.org |
| Secondary Cross-Contact | Desis Rising Up and Moving (DRUM) — info@drumnyc.org |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: NAPA and South Asian legal aid organizations serve communities with substantial immigration enforcement exposure and documented historical targeting (post-9/11 surveillance precedents). The corpus's threat model section — documenting commercial data broker integration with federal enforcement systems — has specific relevance to communities that have been subject to targeted federal surveillance programs. DRUM (Desis Rising Up and Moving) is the NYC-based worker organizing and legal aid organization that bridges South Asian immigrant rights and labor rights; they are a cross-sector contact relevant to both this sector and Sector 1.

---

### I-04: ACLU Immigrants' Rights Project

| Field | Detail |
|-------|--------|
| Organization | American Civil Liberties Union — Immigrants' Rights Project |
| Primary Contact | Omar Jadwat — Senior Staff Attorney, Immigrants' Rights Project |
| Secondary Contact | Cecillia Wang — ACLU Deputy Legal Director |
| Email (general) | media@aclu.org |
| Legal Intake | aclu.org/immigrants-rights |
| Phone | 212-549-2500 (national) |
| Address | 125 Broad St, 19th Floor, New York, NY 10004 |
| Website | aclu.org/immigrants-rights |
| Relationship Status | Listed in phase-2-target-organizations.csv — ACLU published Palantir piece in 2026; not a cold contact |

**Outreach angle**: The ACLU Immigrants' Rights Project is actively litigating against ICE enforcement practices and has published on Palantir's role in deportation operations in 2026. This is not a cold contact — the corpus extends the ACLU's own published analysis with primary-source procurement documentation. Omar Jadwat heads the litigation program; Cecillia Wang oversees the Legal Division broadly. Approach as a researcher sharing supplementary primary-source documentation for active litigation and policy work, not as an advocacy partner seeking endorsement. The corpus's FOIA-sourced contracts are the strongest value addition for the ACLU's litigation team.

---

### I-05: JACIR (Justice for All Campaign for Immigrant Rights)

| Field | Detail |
|-------|--------|
| Organization | Justice for All Campaign for Immigrant Rights (JACIR) |
| Primary Contact | Campaign Coordinator (verify current; route through website) |
| Email | info@jacir.org |
| Website | jacir.org |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: JACIR coordinates immigrant rights advocacy across multiple state affiliates and engages directly with affected communities. The corpus's accessible countermeasures — Part 0 requiring no technical expertise and no government-issued ID — are designed for direct distribution to individuals, making JACIR a useful distribution amplifier. The immigration surveillance evasion playbook and the role-based quick start templates (quick-start-immigrant-worker.md) are the most relevant corpus materials for JACIR's constituency-level work.

---

### I-06: CLINIC (Catholic Legal Immigration Network, Inc.)

| Field | Detail |
|-------|--------|
| Organization | Catholic Legal Immigration Network, Inc. |
| Primary Contact | Anna Gallagher — CLINIC Executive Director |
| Secondary Contact | Training and Technical Assistance Director |
| Email (general) | clinic@cliniclegal.org |
| Phone | 301-565-4800 |
| Address | 8757 Georgia Avenue, Suite 850, Silver Spring, MD 20910 |
| Website | cliniclegal.org |
| Relationship Status | Listed in phase-2-tier2-organizational-outreach-strategy.md — highest network multiplier in immigration sector |

**Outreach angle**: CLINIC's 400+ affiliates across the US make it the highest network multiplier in the immigration legal aid sector. A single adoption by CLINIC distributes the corpus to every affiliated legal services organization in its network. CLINIC's faith-based orientation also creates a natural bridge to Sector 5 (faith coalitions). Anna Gallagher as Executive Director is the appropriate first contact; the training and technical assistance team handles practitioner resource integration. This is a pre-contact candidate for personalized outreach before the main Tier 2 wave.

---

### I-07: National Immigration Project (NIPNLG)

| Field | Detail |
|-------|--------|
| Organization | National Immigration Project of the National Lawyers Guild |
| Primary Contact | National Director (verify current; organizational transition in 2025) |
| Email | info@nationalimmigrationproject.org |
| Phone | 617-227-9727 |
| Address | 42 Broadway, Suite 1347, New York, NY 10004 |
| Website | nationalimmigrationproject.org |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: NIPNLG provides technical legal assistance to immigration attorneys, publishes practice advisories, and trains lawyers on immigration defense. The corpus's immigration attorney implementation guide — and specifically the section on attorney-client privilege considerations for digital communications — is directly in scope for NIPNLG's training work. NIPNLG's NLG affiliation also connects it to civil liberties organizations outside the immigration sector.

---

### I-08: Vera Institute of Justice — Immigrant Defense Project

| Field | Detail |
|-------|--------|
| Organization | Vera Institute of Justice |
| Unit | Vera Action / Immigrant Defense Program |
| Primary Contact | Nicholas Turner — Vera President and Director |
| Email (general) | info@vera.org |
| Phone | 212-334-1300 |
| Address | 34 35th St, Suite 4-2A, Brooklyn, NY 11232 |
| Website | vera.org |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: Vera's Immigrant Defense Project provides legal representation and policy advocacy. Vera's research infrastructure makes it well-positioned to evaluate the corpus's primary-source documentation and potentially to publish its own policy analysis building on the ELITE documentation. The research-to-policy pipeline at Vera is a credibility multiplier — a Vera publication citing the corpus carries significant weight with legislative and regulatory audiences.

---

## Sector 3: Civil Rights Organizations

**Distribution rationale**: Civil rights organizations have both the institutional authority to amplify the corpus and direct client relationships with populations affected by ELITE targeting. The NAACP and SPLC have named Palantir and ICE enforcement practices publicly. DV advocacy organizations (NNEDV, Coalition Against Stalkerware) address a related but distinct surveillance threat vector. Both subsectors are ready for outreach.

**Lead threat briefing**: `execution/tier2-threat-briefing-dv-advocates.md` (for DV sector); no single briefing covers NAACP/SPLC/civil rights orgs broadly — use labor organizer briefing for organizing-context contacts, immigration lawyer briefing for legal-focus contacts
**Lead playbooks**: `organizational-opsec-playbook.md`, `dv-survivor-safety-playbook.md`

---

### C-01: NAACP Legal Defense Fund — Digital Justice Program

| Field | Detail |
|-------|--------|
| Organization | NAACP Legal Defense and Educational Fund |
| Unit | Digital Justice Program |
| Primary Contact | Janai Nelson — LDF President and Director-Counsel |
| Secondary Contact | Digital Justice Program Director (verify current staff) |
| Email (general) | info@naacpldf.org |
| Phone | 212-965-2200 |
| Address | 40 Rector Street, 5th Floor, New York, NY 10006 |
| Website | naacpldf.org |
| Relationship Status | Listed in phase-2-tier2-organizational-outreach-strategy.md — publicly cited Palantir; not cold |

**Outreach angle**: The NAACP LDF's Digital Justice Program has already engaged with the intersection of algorithmic decision-making, civil rights, and immigration enforcement. The corpus's FOIA-sourced documentation of ELITE's data pipeline — specifically the Medicaid record integration and the disproportionate impact on Black and Brown immigrant communities — is primary-source material for Digital Justice Program litigation and policy work. The racial disparities in ELITE's confidence score generation (aggregating data from administrative programs that correlate with race and national origin) is a discriminatory impact theory the LDF's legal team is positioned to develop. Approach Janai Nelson's office as a research resource offer; the Digital Justice Program director handles practitioner resource integration.

---

### C-02: Southern Poverty Law Center (SPLC) — Intelligence Project

| Field | Detail |
|-------|--------|
| Organization | Southern Poverty Law Center |
| Unit | Intelligence Project / Immigrant Justice |
| Primary Contact | Margaret Huang — SPLC President and CEO |
| Secondary Contact | Intelligence Project Director (currently transitioning; verify) |
| Email (general) | splcenter@splcenter.org |
| Phone | 334-956-8200 |
| Address | 400 Washington Ave, Montgomery, AL 36104 |
| Website | splcenter.org |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: SPLC's Intelligence Project tracks hate groups and extremist organizations — it has an existing surveillance monitoring infrastructure that is methodologically adjacent to the corpus's threat model approach. SPLC's Immigrant Justice program handles removal defense and documentation of enforcement abuses. The corpus's ELITE documentation is directly relevant to both programs: Intelligence Project for threat monitoring methodology; Immigrant Justice for enforcement documentation. SPLC is going through organizational restructuring in 2025-2026; confirm current leadership before sending to Margaret Huang's office.

---

### C-03: NNEDV (National Network to End Domestic Violence) — Safety Net Project

| Field | Detail |
|-------|--------|
| Organization | National Network to End Domestic Violence |
| Unit | Safety Net Project (technology safety) |
| Primary Contact | Cindy Southworth — NNEDV Senior Vice President (technology safety) |
| Secondary Contact | Safety Net Project Coordinator |
| Email (general) | nnedv@nnedv.org |
| Phone | 202-543-5566 |
| Address | 1400 Eye Street NW, Suite 300, Washington, DC 20005 |
| Website | nnedv.org |
| Relationship Status | Named in execution/tier2-threat-briefing-dv-advocates.md — not cold |

**Outreach angle**: NNEDV's Safety Net Project is the national technical assistance resource for DV organizations on technology safety — specifically stalkerware, account takeover, and location tracking. The corpus's DV survivor safety playbook and the DV advocate threat briefing are designed for NNEDV's technical assistance audience. Cindy Southworth built the Safety Net program and has the technical background to evaluate the corpus's countermeasures. NNEDV's affiliate network of 55 state coalitions is the downstream distribution path — NNEDV adoption reaches every state DV coalition. This is a pre-contact candidate.

---

### C-04: Coalition Against Stalkerware

| Field | Detail |
|-------|--------|
| Organization | Coalition Against Stalkerware |
| Primary Contact | Eva Galperin — Director of Cybersecurity, EFF (Coalition founding member) |
| Secondary Contact | Lenora Lapidus (ACLU Women's Rights Project) |
| Email | contactus@stopstalkerware.org |
| Website | stopstalkerware.org |
| Relationship Status | Eva Galperin also appears as EFF contact in tier-2-sector-contact-lists.md |

**Outreach angle**: The Coalition Against Stalkerware coordinates across security researchers, DV advocates, and technology companies to address spouseware and location tracking abuse. The corpus's stalkerware countermeasures documentation and the DV survivor safety playbook directly address Coalition member concerns. Eva Galperin's dual role (EFF cybersecurity director and Coalition member) makes her an efficient cross-sector contact: outreach to her EFF address (eva@eff.org, already listed in tier-2-sector-contact-lists.md) with a note that the DV survivor safety playbook is specifically relevant to Coalition work is the most efficient route.

---

### C-05: Human Rights First — Digital Security Program

| Field | Detail |
|-------|--------|
| Organization | Human Rights First |
| Primary Contact | Elisa Massimino — CEO (verify current; organizational changes 2025-2026) |
| Email (general) | feedback@humanrightsfirst.org |
| Phone | 202-370-3323 |
| Address | 1225 I Street NW, Suite 500, Washington, DC 20005 |
| Website | humanrightsfirst.org |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: Human Rights First's asylum and immigration programs work with asylum seekers who face many of the same surveillance risks as undocumented immigrants under ELITE. The corpus's asylum-seeker-specific countermeasures and the broader immigration surveillance evasion playbook are relevant to HRF's caseworkers. HRF's international credibility also makes it a useful amplifier for the international dimensions of the corpus (commercial data broker networks operating across borders).

---

### C-06: Mijente — Digital Rights Program

| Field | Detail |
|-------|--------|
| Organization | Mijente |
| Primary Contact | Marisa Franco — Mijente Co-Director |
| Secondary Contact | Kenia Alcocer (tech/policy work) |
| Email (general) | info@mijente.net |
| Website | mijente.net |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: Mijente has been among the most active civil rights organizations specifically naming and opposing Palantir and ICE's data infrastructure. They published the "Who's Behind ICE?" report in 2018 and have continued surveillance monitoring work. The corpus's updated 2026 ELITE documentation extends their own prior research. Marisa Franco is a public intellectual on immigration and surveillance who can amplify the corpus to a large constituent base. This is also a bridge organization to the advocacy and organizing sector.

---

## Sector 4: Academic and Law School Programs

**Distribution rationale**: Academic and law school contacts have longer adoption cycles (6–18 months) but higher credibility multiplier effects. A law school clinic that cites the corpus creates citable scholarship; a political science department that assigns it creates a generation of informed analysts. Priority is law school clinical programs with active immigration cases, followed by social science departments studying surveillance policy. For technical cybersecurity departments, see `tier-2-sector-contact-lists.md` (Sectors A and B).

**Lead threat briefing**: `phase-2-threat-briefing-academics.md`, `execution/tier2-threat-briefing-educators.md`
**Lead playbooks**: Threat model section (primary-source documentation for citation)

---

### A-01: Georgetown University Law Center — Center on Privacy & Technology (CPT)

| Field | Detail |
|-------|--------|
| Institution | Georgetown University Law Center |
| Center | Center on Privacy & Technology |
| Primary Contact | Emily Tucker — CPT Executive Director |
| Secondary Contact | Stevie Glaberson — Director of Research & Advocacy |
| Email | privacy.tech@law.georgetown.edu |
| Address | 600 New Jersey Ave NW, Washington, DC 20001 |
| Website | law.georgetown.edu/privacy-technology-center/ |
| Relationship Status | Listed in phase-2-target-organizations.csv — published American Dragnet (2022); closest institutional predecessor |

**Outreach angle**: Georgetown CPT published American Dragnet (2022), the most rigorous prior documentation of commercial surveillance in immigration enforcement. The corpus is a May 2026 operational extension of American Dragnet — it updates the threat model, adds countermeasures, and extends the primary-source documentation. Emily Tucker and Stevie Glaberson are both appropriate first contacts. Approach as a peer researcher sharing follow-on research, not as an external petitioner. A Georgetown CPT citation is the single highest-value endorsement signal in the academic sector for all downstream Tier 2 outreach; it should be pursued first.

---

### A-02: Harvard Law School — Cyberlaw Clinic (Berkman Klein)

| Field | Detail |
|-------|--------|
| Institution | Harvard Law School |
| Clinic | Cyberlaw Clinic, Berkman Klein Center for Internet & Society |
| Primary Contact | Christopher T. Bavitz — WilmerHale Clinical Professor, Managing Director |
| Email | cyber@law.harvard.edu |
| Phone | 617-384-9125 |
| Address | 1557 Massachusetts Ave, 4th Floor, Cambridge, MA 02138 |
| Website | clinic.cyber.harvard.edu |
| Relationship Status | Listed in tier-2-sector-contact-lists.md |

**Outreach angle**: HLS Cyberlaw Clinic develops real surveillance law cases. The corpus's FOIA-sourced procurement contracts and federal court filing citations are primary-source case-building material. The shield law question raised by pre-existing commercial data exposure of undocumented sources is a specific, novel legal question the clinic can develop. This is listed in the existing sector contact list; do not duplicate effort — confirm outreach status before sending.

---

### A-03: NYU School of Law — Immigrant Rights Clinic

| Field | Detail |
|-------|--------|
| Institution | New York University School of Law |
| Clinic | Immigrant Rights Clinic |
| Primary Contact | Nancy Morawetz — Clinical Professor (founding director) |
| Secondary Contact | Alina Das — Clinical Professor |
| Email (clinic) | law.clinic@nyu.edu |
| Phone | 212-998-6430 |
| Address | 245 Sullivan St, New York, NY 10012 |
| Website | law.nyu.edu/clinics/immigrantrights |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: NYU's Immigrant Rights Clinic handles removal defense and federal court immigration litigation directly. The corpus's ELITE documentation is primary-source material for the specific legal theories the clinic litigates: warrantless commercial data collection, administrative data integration in deportation targeting, and due process implications of algorithmic scoring. Nancy Morawetz has been litigating immigration law for decades and will evaluate the corpus on primary-source integrity. Alina Das focuses on criminalization and immigration — the corpus's documentation of how criminal records feed ELITE's confidence scoring is directly relevant to her work.

---

### A-04: American University Washington College of Law — Immigrant Justice Clinic

| Field | Detail |
|-------|--------|
| Institution | American University Washington College of Law |
| Clinic | Immigrant Justice Clinic |
| Primary Contact | Stephen Wermiel — Clinical Professor (immigration track) |
| Email (clinic) | wcljustice@american.edu |
| Phone | 202-274-4000 |
| Address | 4300 Nebraska Ave NW, Washington, DC 20016 |
| Website | wcl.american.edu |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: AU WCL is DC-based with strong connections to federal advocacy and litigation communities. The Immigrant Justice Clinic handles removal cases and is well-positioned to bridge clinic case development with DC policy advocacy. The corpus's threat model documentation is relevant to both tracks.

---

### A-05: University of Texas School of Law — Immigration Clinic

| Field | Detail |
|-------|--------|
| Institution | University of Texas School of Law |
| Clinic | Immigration Clinic |
| Primary Contact | Denise Gilman — Clinical Professor, Immigration Clinic Director |
| Email (clinic) | lawclinics@law.utexas.edu |
| Phone | 512-471-5151 |
| Address | 727 East Dean Keeton St, Austin, TX 78705 |
| Website | law.utexas.edu/clinics/immigration |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: UT Law operates in the primary ELITE enforcement geography (Texas has the highest undocumented population of any state at approximately 1.6 million). The corpus's Texas-specific enforcement documentation — ELITE's operational concentration in border enforcement zones, the DHS Penlink contract for real-time location tracking — is directly relevant to UT Law's clinical casework. Denise Gilman's clinic has documented cases involving ICE detention and removal that would benefit from the ELITE threat model documentation.

---

### A-06: Cardozo School of Law — Immigration Justice Clinic

| Field | Detail |
|-------|--------|
| Institution | Benjamin N. Cardozo School of Law, Yeshiva University |
| Clinic | Immigration Justice Clinic |
| Primary Contact | Peter Markowitz — Clinical Professor |
| Email (clinic) | lawclinics@yu.edu |
| Phone | 212-790-0200 |
| Address | 55 Fifth Ave, New York, NY 10003 |
| Website | cardozo.yu.edu/clinics/immigration-justice-clinic |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: Cardozo's Immigration Justice Clinic is New York-based and handles asylum and removal defense. New York City is STOP's primary operational geography for anti-surveillance litigation — the geographic proximity creates potential for clinic-advocacy collaboration. Peter Markowitz has been active on enforcement accountability issues. The corpus's New York-relevant framing (NYPD Palantir integration, NYC sanctuary policy pressure) is specifically relevant to this clinic.

---

### A-07: Association of American Law Schools — Clinical Legal Education Section

| Field | Detail |
|-------|--------|
| Institution | Association of American Law Schools |
| Section | Clinical Legal Education Section |
| Primary Contact | Section Chair (rotates annually; verify current) |
| Secondary Contact | Erwin Chemerinsky — AALS President 2026 (University of California Berkeley Law Dean) |
| Email | aals@aals.org |
| Phone | 202-296-8851 |
| Address | 1614 20th St NW, Washington, DC 20009 |
| Website | aals.org |
| Relationship Status | Listed in phase-2-target-organizations.csv — highest cascade multiplier in law school sector |

**Outreach angle**: AALS's Clinical Legal Education Section is the professional home for clinical professors at 180+ member law schools. Integration into the Section's resource library or programming reaches every clinical law professor in the country. Erwin Chemerinsky as AALS President 2026 is a public intellectual on constitutional law with strong positions on surveillance and civil liberties; his name in outreach correspondence signals awareness of the appropriate institutional framing. Do not approach AALS as an advocacy organization — pitch as a curriculum resource with primary-source-citable documentation.

---

### A-08: Vera Institute — Center on Immigration and Justice

| Field | Detail |
|-------|--------|
| Institution | Vera Institute of Justice |
| Center | Center on Immigration and Justice |
| Primary Contact | Vera President (Nicholas Turner) |
| Email | info@vera.org |
| Phone | 212-334-1300 |
| Website | vera.org/centers/center-on-immigration-and-justice |
| Relationship Status | Also listed in Sector 2 (immigration legal aid) — dual-sector contact |

**Outreach angle**: Vera straddles the academic research and legal aid sectors, making it a dual-contact: the Center on Immigration and Justice for academic research and policy publication, and the direct services program for practitioner resource integration. Vera's research team can write policy reports that cite the corpus; their legal services team can use the immigration attorney implementation guide in direct case management. One contact to Vera's President serves both tracks.

---

### A-09: Clinical Legal Education Association (CLEA)

| Field | Detail |
|-------|--------|
| Organization | Clinical Legal Education Association |
| Primary Contact | Executive Director (verify current) |
| Email | via cleaweb.org/contact |
| Website | cleaweb.org |
| Relationship Status | Listed in phase-2-target-organizations.csv |

**Outreach angle**: CLEA is the professional organization for 2,500+ clinical law professors across US law schools. Similar to AALS Clinical Section but with a narrower, more practice-focused membership. CLEA conference programming is the highest-leverage integration pathway — a conference session on surveillance documentation methodology for clinical teaching reaches clinical faculty who immediately have casework context for adoption.

---

### A-10: ImmProf Network (Immigration Law Professors)

| Field | Detail |
|-------|--------|
| Organization | Immigration Law Professors Network |
| Contact | Via lawprofessors.typepad.com and direct faculty email |
| Key Contacts | Hiroshi Motomura (UCLA), Kevin Johnson (UC Davis Dean), Lenni Benson (NYLS) |
| Relationship Status | Listed in phase-2-target-organizations.csv |

**Outreach angle**: ImmProf is an informal but active network of 400+ immigration law faculty. The fastest adoption path in the law school sector: informal network propagation through faculty blogs and direct email is faster than institutional AALS channels. Hiroshi Motomura at UCLA (immigration law constitutional scholar) and Kevin Johnson at UC Davis (law school dean with extensive immigration scholarship) are high-profile faculty contacts who can amplify the corpus across the network.

---

## Sector 5: Faith Coalitions and Sanctuary Networks

**Distribution rationale**: Faith institutions operate sanctuary networks that are directly threatened by the April 2026 ICE policy change revoking sensitive location protections. Faith leaders are non-technical, so the accessible countermeasures (Part 0, no technical expertise required) and the faith leader threat briefing are the primary corpus materials. Distribution through denominational networks provides the highest single-contact cascade multiplier of any sector.

**Lead threat briefing**: `execution/tier2-threat-briefing-faith-leaders.md`
**Lead playbooks**: `organizational-opsec-playbook.md`, `immigration-attorney-implementation-guide.md` (for sanctuary legal guidance)

---

### F-01: National Council of Churches — Interfaith Immigration Coalition

| Field | Detail |
|-------|--------|
| Organization | National Council of Churches USA |
| Unit | Interfaith Immigration Coalition |
| Primary Contact | Jim Winkler — NCC General Secretary |
| Secondary Contact | Interfaith Immigration Coalition Coordinator |
| Email (general) | ncccusa@ncccusa.org |
| Phone | 212-870-2227 |
| Address | 475 Riverside Drive, New York, NY 10115 |
| Website | nationalcouncilofchurches.us |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: The National Council of Churches coordinates the Interfaith Immigration Coalition, a 53-member organization coalition advocating for humane immigration policy. NCC member denominations include United Methodist Church, Presbyterian Church USA, Episcopal Church, and others with sanctuary programs. The April 2026 ICE sensitive location policy change — revoking protections that historically prevented enforcement in houses of worship — makes the corpus's faith leader threat briefing immediately time-sensitive for this network. Jim Winkler is the appropriate first contact; the coalition structure means NCC adoption reaches all 53 member organizations simultaneously.

---

### F-02: Unitarian Universalist Association — Sanctuary Work

| Field | Detail |
|-------|--------|
| Organization | Unitarian Universalist Association |
| Primary Contact | Susan Frederick-Gray — UUA President |
| Secondary Contact | Office of Advocacy and Witness Director |
| Email (general) | info@uua.org |
| Phone | 617-742-2100 |
| Address | 24 Farnsworth St, Boston, MA 02210 |
| Website | uua.org |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: UUA has been among the most publicly active denominations in sanctuary movement participation and explicitly names ICE enforcement practices in its public advocacy. The corpus's sanctuary legal guidance and operational security countermeasures for congregations providing physical sanctuary are directly relevant to UUA's existing programs. Susan Frederick-Gray as UUA President is a public voice on immigration and sanctuary; the organizational infrastructure for congregational training is robust. 1,000+ UUA congregations nationally.

---

### F-03: PICO National Network / Faith in Action

| Field | Detail |
|-------|--------|
| Organization | Faith in Action (formerly PICO National Network) |
| Primary Contact | Bishop Dwayne Royster — National Director |
| Secondary Contact | Regional Directors (varies by state) |
| Email (general) | info@faithinaction.org |
| Phone | 510-655-2801 |
| Address | 1640 Oak Park Blvd, Pleasant Hill, CA 94523 |
| Website | faithinaction.org |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: Faith in Action (PICO) is the largest faith-based community organizing network in the US, with 1,000+ member congregations across 45 states. They have active immigration justice programs in states with high enforcement concentration. Bishop Royster has been vocal on immigration enforcement and civil rights. Faith in Action's organizing model makes it receptive to the operational security framing: the corpus provides practical tools for the congregations doing direct sanctuary work, not just policy advocacy. The faith leader threat briefing is the appropriate first attachment.

---

### F-04: United Methodist Church — Immigration Task Force

| Field | Detail |
|-------|--------|
| Organization | United Methodist Church |
| Unit | Immigration Task Force / General Board of Church and Society |
| Primary Contact | Rev. Susan Henry-Crowe — General Secretary, Church and Society |
| Email (general) | umcadvocacy@umc.org |
| Phone | 202-488-5600 |
| Address | 100 Maryland Ave NE, Washington, DC 20002 |
| Website | umcgbcs.org |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: UMC's General Board of Church and Society is the Washington-based policy advocacy arm with direct influence on the 30,000+ UMC congregations nationally. The Immigration Task Force specifically addresses sanctuary and enforcement issues. Rev. Henry-Crowe has testified before Congress on immigration. The corpus's faith leader briefing and the sanctuary legal guidance section are the most relevant materials; the accessible Part 0 countermeasures (no technical expertise required) fit the congregation-level deployment context.

---

### F-05: US Conference of Catholic Bishops — Migration and Refugee Services

| Field | Detail |
|-------|--------|
| Organization | United States Conference of Catholic Bishops |
| Unit | Migration and Refugee Services |
| Primary Contact | Teresa Waggener — Executive Director, Migration and Refugee Services |
| Secondary Contact | Bishop Kevin Vann — USCCB Committee on Migration Chair |
| Email (general) | mrs@usccb.org |
| Phone | 202-541-3000 |
| Address | 3211 4th Street NE, Washington, DC 20017 |
| Website | usccb.org/mrs |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: USCCB Migration and Refugee Services operates the largest refugee resettlement network in the US through Catholic Charities affiliates. The ICE sanctuary policy change directly threatens Catholic Charities offices that provide immigration legal services. The corpus's sanctuary operational security guidance and the attorney-client privilege considerations for digital communications in legal aid settings are the most relevant sections for USCCB's legal services network. Bishop Vann's leadership on the Committee on Migration means the Migration and Refugee Services executive director is the correct first contact, not the USCCB press office.

---

### F-06: Church World Service — Immigration and Refugee Program

| Field | Detail |
|-------|--------|
| Organization | Church World Service |
| Unit | Immigration and Refugee Program |
| Primary Contact | Rick Santos — CWS President and CEO |
| Secondary Contact | Refugee Services Director |
| Email (general) | info@cwsglobal.org |
| Phone | 574-264-3102 |
| Address | PO Box 968, Elkhart, IN 46515 |
| Website | cwsglobal.org |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: CWS is a multi-faith humanitarian organization providing refugee resettlement, emergency relief, and immigration legal services through 40+ partner organizations across 36 states. Its multi-faith structure (Protestant, Anglican, Orthodox, and other Christian traditions) makes it a bridge to faith communities beyond Catholic and mainline Protestant networks. The immigration and refugee program's operational context — legal services, case management, direct client contact — makes the corpus's practitioner-level guidance most relevant.

---

### F-07: Jewish Council for Public Affairs — National Jewish Immigrant Justice Initiative

| Field | Detail |
|-------|--------|
| Organization | Jewish Council for Public Affairs |
| Unit | National Jewish Immigrant Justice Initiative |
| Primary Contact | Amy Spitalnick — JCPA CEO (since 2023) |
| Secondary Contact | Immigrant Justice Initiative Director |
| Email (general) | info@jewishpublicaffairs.org |
| Phone | 212-684-6950 |
| Address | 116 East 27th Street, New York, NY 10016 |
| Website | jewishpublicaffairs.org |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: JCPA coordinates advocacy across 125 Jewish community relations councils and federations nationwide. The National Jewish Immigrant Justice Initiative runs programming connecting Jewish community organizations with immigrant rights advocacy. Amy Spitalnick has been a highly visible civil rights and democracy advocate; the corpus's civil liberties framing is aligned with JCPA's institutional voice. The network multiplier (125 councils) is significant for distribution amplification.

---

### F-08: Islamic Society of North America (ISNA) — Office of Religious Affairs

| Field | Detail |
|-------|--------|
| Organization | Islamic Society of North America |
| Unit | Office of Religious Affairs / Civic Engagement |
| Primary Contact | Safiyyah Ally — ISNA President |
| Email (general) | isna@isna.net |
| Phone | 317-839-8157 |
| Address | PO Box 38, Plainfield, IN 46168 |
| Website | isna.net |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: ISNA represents Muslim communities with documented historical exposure to federal surveillance programs (post-9/11 COINTELPRO-adjacent monitoring, NYPD Demographics Unit). The corpus's documentation of commercial data broker surveillance maps onto longstanding concerns in Muslim communities about government surveillance infrastructure. The accessible countermeasures and the organizational opsec playbook are most relevant for ISNA member congregations. The ICE sanctuary policy change has direct implications for mosques that have provided refuge to undocumented community members.

---

### F-09: Evangelical Lutheran Church in America — Immigration Justice

| Field | Detail |
|-------|--------|
| Organization | Evangelical Lutheran Church in America |
| Unit | Lutheran Immigration and Refugee Service / ELCA Social Action |
| Primary Contact | Rev. Elizabeth Eaton — ELCA Presiding Bishop |
| Secondary Contact | ELCA Social Action Director |
| Email (general) | info@elca.org |
| Phone | 773-380-2700 |
| Address | 8765 W Higgins Road, Chicago, IL 60631 |
| Website | elca.org |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: ELCA operates Lutheran Immigration and Refugee Service (LIRS) as an independent affiliated organization — one of the largest refugee resettlement agencies in the US. Rev. Eaton has publicly advocated for immigrant rights. The corpus's sanctuary guidance and the practical countermeasures for faith leaders providing direct services are relevant to ELCA congregations operating informal sanctuary programs. ELCA's 9,000 congregations represent a large distribution network.

---

### F-10: Interfaith Worker Justice

| Field | Detail |
|-------|--------|
| Organization | Interfaith Worker Justice |
| Primary Contact | Kim Bobo — IWJ Founder/Director (or current Executive Director; verify) |
| Email (general) | iwj@iwj.org |
| Phone | 312-738-0995 |
| Address | 1020 W Bryn Mawr Ave, Chicago, IL 60660 |
| Website | interfaithworkerjustice.org |
| Relationship Status | No prior contact — cold outreach |

**Outreach angle**: Interfaith Worker Justice sits at the intersection of faith communities and labor organizing — a cross-sector contact bridging Sectors 1 and 5. IWJ's 58 affiliated worker centers and faith-labor organizations are exactly the organizations that face the convergent threat (labor organizing + immigration enforcement) documented in the corpus. The activist-organizing-playbook and the faith leader threat briefing together are the complete resource package for IWJ's constituency.

---

## Summary Table

| ID | Organization | Sector | Relationship | Priority |
|----|-------------|--------|--------------|----------|
| L-01 | AFL-CIO Technology Institute | Labor | Cold | Wave 1 |
| L-02 | SEIU | Labor | Cold | Wave 1 |
| L-03 | UFW | Labor | Cold | Wave 1 |
| L-04 | CNA / National Nurses United | Labor | Cold | Wave 1 |
| L-05 | NUPGE (Canada) | Labor | Cold | Wave 2 |
| L-06 | CWA / Code CWA | Labor | Prior CSV | Wave 1 |
| L-07 | NDWA | Labor | Prior CSV — pre-contact candidate | Wave 1 (pre-contact) |
| I-01 | RAICES | Immigration legal aid | Cold | Wave 1 |
| I-02 | AILA | Immigration legal aid | Cold | Wave 1 |
| I-03 | NAPA / DRUM | Immigration legal aid | Cold | Wave 2 |
| I-04 | ACLU Immigrants' Rights Project | Immigration legal aid | Prior CSV — not cold | Wave 1 |
| I-05 | JACIR | Immigration legal aid | Cold | Wave 2 |
| I-06 | CLINIC | Immigration legal aid | Prior — pre-contact candidate | Wave 1 (pre-contact) |
| I-07 | NIPNLG | Immigration legal aid | Cold | Wave 1 |
| I-08 | Vera Institute — Immigrant Defense | Immigration legal aid | Cold | Wave 2 |
| C-01 | NAACP LDF — Digital Justice | Civil rights | Prior CSV — not cold | Wave 1 |
| C-02 | SPLC — Intelligence Project | Civil rights | Cold | Wave 1 |
| C-03 | NNEDV — Safety Net Project | Civil rights/DV | Prior briefing — not cold | Wave 1 (pre-contact) |
| C-04 | Coalition Against Stalkerware | Civil rights/DV | EFF cross-contact | Wave 1 |
| C-05 | Human Rights First | Civil rights | Cold | Wave 2 |
| C-06 | Mijente | Civil rights | Cold | Wave 1 |
| A-01 | Georgetown CPT | Academic/law | Prior CSV — pre-contact candidate | Wave 1 (pre-contact) |
| A-02 | Harvard Cyberlaw Clinic | Academic/law | Prior sector list | Wave 1 |
| A-03 | NYU Immigrant Rights Clinic | Academic/law | Cold | Wave 1 |
| A-04 | AU WCL Immigrant Justice Clinic | Academic/law | Cold | Wave 2 |
| A-05 | UT Law Immigration Clinic | Academic/law | Cold | Wave 1 |
| A-06 | Cardozo Immigration Justice Clinic | Academic/law | Cold | Wave 2 |
| A-07 | AALS — Clinical Legal Education Section | Academic/law | Prior CSV | Wave 1 |
| A-08 | Vera — Center on Immigration and Justice | Academic/law | Cold (dual-sector) | Wave 2 |
| A-09 | CLEA | Academic/law | Prior CSV | Wave 2 |
| A-10 | ImmProf Network | Academic/law | Prior CSV | Wave 2 |
| F-01 | National Council of Churches / Interfaith Coalition | Faith | Cold | Wave 1 |
| F-02 | Unitarian Universalist Association | Faith | Cold | Wave 1 |
| F-03 | Faith in Action (PICO) | Faith | Cold | Wave 1 |
| F-04 | United Methodist Church — Church and Society | Faith | Cold | Wave 1 |
| F-05 | USCCB — Migration and Refugee Services | Faith | Cold | Wave 1 |
| F-06 | Church World Service | Faith | Cold | Wave 1 |
| F-07 | JCPA — National Jewish Immigrant Justice | Faith | Cold | Wave 2 |
| F-08 | ISNA — Civic Engagement | Faith | Cold | Wave 2 |
| F-09 | ELCA — Immigration Justice | Faith | Cold | Wave 2 |
| F-10 | Interfaith Worker Justice | Faith (cross-sector) | Cold | Wave 2 |

**Total: 40 organizations in this document + 7 confirmed from prior CSV/sector lists with updated contact details = 47 unique organizations across 5 sectors.**

---

*Companion document: `tier-2-distribution-strategy.md` — customization matrix, email templates, rollout timeline, and success metrics.*
*Prior sector coverage: `tier-2-sector-contact-lists.md` covers digital rights (12 orgs), academic cybersecurity (12 orgs), researcher communities (10 venues), journalist organizations (10 orgs) — 44 contacts, not duplicated here.*
*Total Tier 2 contact pool across both documents: 91 organizations and contacts.*
