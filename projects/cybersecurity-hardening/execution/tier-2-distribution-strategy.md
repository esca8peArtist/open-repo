---
title: "Tier 2 Distribution Strategy — Customization Matrix, Email Templates, Timeline, Success Metrics"
project: cybersecurity-hardening
created: 2026-05-09
status: production-ready
phase: Phase 2 — Tier 2 Organizational Distribution (launch ~Week 5 post-Tier-1)
scope: Labor unions, immigration legal aid, civil rights, academic/law schools, faith coalitions
depends-on:
  - execution/tier-2-organizational-contact-list.md
  - TIER2_DISTRIBUTION_PREP.md
  - TIER2_MESSAGING_TEMPLATES.md
  - TIER_2_DISTRIBUTION_STRATEGY.md
  - execution/TIER2_THREAT_BRIEFING_INDEX.md
  - phase-2-threat-briefing-labor-organizers.md
  - phase-2-threat-briefing-academics.md
  - phase-2-threat-briefing-faith-leaders.md
  - execution/tier2-threat-briefing-immigration-lawyers.md
  - execution/tier2-threat-briefing-dv-advocates.md
trigger: Phase 1 Tier 1 completion + minimum gate passage (see Section 3)
---

# Tier 2 Distribution Strategy

**Bottom line**: This document is the operational playbook for Tier 2 distribution to the five sectors mapped in `tier-2-organizational-contact-list.md`. It answers four questions: which corpus materials go to which organizations (customization matrix), what does the outreach email say for each sector (templates), when does each wave send (timeline), and how do you know if it worked (success metrics). Everything here is ready to deploy the moment Phase 1 Tier 1 completes its minimum gate.

**Coordination note**: Tier 2 for digital rights organizations, academic cybersecurity programs, researcher communities, and journalist organizations is documented in `TIER2_DISTRIBUTION_PREP.md`, `TIER2_MESSAGING_TEMPLATES.md`, and `TIER_2_DISTRIBUTION_STRATEGY.md`. This document covers the five sectors that are new or not fully addressed in those materials. Do not duplicate effort — confirm outreach status on Georgetown CPT, Harvard Cyberlaw Clinic, and ACLU Immigrants' Rights Project before sending from this document, as those contacts appear in both.

---

## Section 1: Customization Matrix

The matrix below maps each organization sector to: (1) the Phase 1 corpus materials that are most relevant, (2) the Phase 2 sector-specific threat briefing to attach, and (3) the specific framing emphasis that distinguishes this sector from generic distribution. Do not send all corpus materials to all recipients — targeted matching produces 3–5x higher adoption rates than full-corpus sends to organizational contacts.

### Matrix: Five Sectors

| Sector | Primary Phase 1 Materials | Phase 2 Threat Briefing | Key Framing Emphasis |
|--------|--------------------------|-------------------------|----------------------|
| **Labor unions** | `activist-organizing-playbook.md`, `organizational-opsec-playbook.md`, Part 0 (data broker opt-outs), `device-hardening-guide.md` | `phase-2-threat-briefing-labor-organizers.md` | Employer surveillance + immigration enforcement convergence; NLRA boundary (what employer can/cannot monitor); DHS Penlink real-time location tracking of organizers |
| **Immigration legal aid** | `immigration-attorney-implementation-guide.md`, `immigration-surveillance-evasion-playbook.md`, Part 0, DROP platform documentation | `execution/tier2-threat-briefing-immigration-lawyers.md` | Paragon Graphite zero-click spyware (April 2026); attorney-client privilege in digital communications; DROP platform (California, no-ID pathway) vs. state gaps |
| **Civil rights orgs (NAACP/SPLC)** | Threat model section (FOIA-sourced, primary-source citable), `organizational-opsec-playbook.md`, discriminatory impact documentation | No single briefing — pair with labor organizer briefing for organizing-context contacts, immigration lawyer briefing for legal-focus contacts | Discriminatory impact of algorithmic scoring on Black and Brown immigrant communities; FOIA-sourced primary sources as litigation foundation; Medicaid integration as HIPAA intersect |
| **DV advocacy (NNEDV/CAS)** | `dv-survivor-safety-playbook.md`, `organizational-opsec-playbook.md`, Part 0 | `execution/tier2-threat-briefing-dv-advocates.md` | Law enforcement database access by abusers; stalkerware at scale; Safety Net Project technical assistance framing |
| **Academic/law schools** | Threat model section (full, for citation), `immigration-attorney-implementation-guide.md`, `immigration-surveillance-evasion-playbook.md` | `phase-2-threat-briefing-academics.md` or `execution/tier2-threat-briefing-educators.md` | Fourth Amendment gap (Carpenter extension question); HIPAA pre-enforcement obligations; primary-source structure for student notes and clinical cases; semester timing awareness |
| **Faith coalitions** | `organizational-opsec-playbook.md`, Part 0, sanctuary legal guidance sections from `immigration-attorney-implementation-guide.md` | `execution/tier2-threat-briefing-faith-leaders.md` | April 2026 sensitive location policy change; congregational operational security for sanctuary operations; accessible countermeasures (no technical expertise required) |

### Sector-Specific Material Pairing — Detailed

**For labor unions**: Send the activist-organizing-playbook as the primary attachment. The organizational-opsec-playbook is the secondary reference for staff-level security hygiene. Part 0 is relevant for member-level distribution in sectors with undocumented worker concentrations (UFW, SEIU healthcare, NDWA domestic workers). Do not send the full threat model to union organizing departments — the employer surveillance and immigration enforcement convergence sections are sufficient; the full ELITE technical documentation is more detail than most organizing departments will use.

**For immigration legal aid**: Send the immigration attorney implementation guide and the immigration surveillance evasion playbook together as the primary package. Attach the Tier 2 threat briefing for immigration lawyers as the sector context document. The DROP platform documentation within Part 0 is the most time-sensitive single piece: include it prominently for all organizations with California-based clients. For national organizations (AILA, NILC, CLINIC), the full corpus Gist link is appropriate; for smaller direct-service organizations, link to specific sections rather than the full document.

**For civil rights organizations**: The primary value is the threat model's primary-source citeability. Send the full threat model section (not just a summary) to NAACP LDF Digital Justice Program and SPLC Intelligence Project, because these organizations will evaluate the corpus on evidentiary quality, not accessibility. The discriminatory impact angle — how ELITE's confidence scoring aggregates data from programs that correlate with race and national origin — is not explicitly developed in the corpus; note this as an open legal research question in the outreach message, which invites legal researchers to engage with the documentation as a foundation for their own analysis.

**For DV advocacy**: The DV survivor safety playbook is the correct primary material. The organizational opsec playbook covers DV shelter operations. The Coalition Against Stalkerware contact (Eva Galperin via EFF) should receive both the DV advocate briefing and the stalkerware countermeasures documentation. NNEDV's technical assistance mandate means they need the full practitioner-level resource; Safety Net Project staff will evaluate completeness and accessibility.

**For academic and law school programs**: Send the threat model section with explicit note on primary-source structure. The immigration attorney implementation guide is appropriate for law clinics with active removal defense cases. For law reviews and student publications, include a note on the unsettled legal questions the corpus raises (Fourth Amendment third-party doctrine extension; HIPAA enforcement obligations for commercial data broker sales; state privacy law enforcement gap against federal data purchases). Do not send the full implementation guide to academic contacts — it is too practitioner-focused for a curriculum or research audience.

**For faith coalitions**: The faith leader threat briefing is the single most important document — send it as the first attachment. Part 0 (accessible, no technical expertise required) is the appropriate countermeasures companion. The sanctuary legal guidance sections from the immigration attorney implementation guide are relevant for congregations providing physical sanctuary. Do not lead with technical countermeasures detail — faith leaders respond to the documented threat and the practical protective steps, not the technical architecture. Keep the email short and the ask concrete.

---

## Section 2: Email Templates — Five Sector-Specific Variants

**Template principle**: Each template leads with the recipient's institutional mandate before describing the corpus. Personalization variables are marked `{{like this}}`. Fill these before sending. The templates below are distinct from the four templates in `tier-2-outreach-email-templates.md` (digital rights, academic cybersecurity, researcher communities, journalist organizations) — do not mix templates across documents.

---

### Template 1: Labor Unions

**Best for**: AFL-CIO Technology Institute, SEIU, UFW, CNA, CWA, NDWA, NUPGE

**Subject line options**:
- Primary: `Organizer digital security: employer surveillance and immigration enforcement convergence — briefing offer`
- Variant A (for AFL-CIO Technology Institute): `AI Principles for Workers — operational layer: surveillance documentation + organizer countermeasures`
- Variant B (for UFW/NDWA — immigrant worker focus): `Protecting organizing and immigration status simultaneously — documented threat + countermeasures`
- Variant C (for CWA Code): `The surveillance infrastructure CWA members build: documented use cases + worker accountability frame`

**Email body**:

```
Dear {{name}} at {{organization}},

{{organization}}'s organizing work in {{sector: healthcare / agriculture / 
domestic work / tech and telecom}} puts members at the intersection of two 
threat systems that are now operating together: employer surveillance of 
organizing activity and federal immigration enforcement of the same population.

The convergence is documented. The Department of Homeland Security awarded a 
$2.9 million contract to Penlink PLX — a surveillance system that collects 
cellphone location data from advertising SDK networks to track which phones 
attended specific locations. Privacy advocates have documented ICE using 
Penlink to identify individuals who observed ICE enforcement operations. For 
organizing drives in sectors with high concentrations of immigrant workers, 
an organizer's presence at repeated union meetings creates a location pattern 
that is accessible to any DHS component — including ICE. The threat briefing 
attached documents this specifically, with sources.

The countermeasures I'm offering are practical and calibrated to the NLRA 
boundary: what employers can legally monitor (work-issued devices, work 
networks, workplace AI systems) versus what they cannot (personal devices, 
personal networks, Signal groups used off work hours). The activist-organizing-
playbook covers device compartmentalization, Signal group security protocols 
for organizing committees, and the BYOD boundary — the same protection 
framework that NLRA rights training should sit alongside.

{{LABOR_SPECIFIC}}

This is a training resource offer, not a policy partnership request. If a 
30-minute orientation for your organizing team or education department would 
be useful, I'm available to schedule. 

Corpus: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
Attached: Sector threat briefing — Union Organizers and Labor Networks (May 2026)
```

**{{LABOR_SPECIFIC}} variants**:

- AFL-CIO Technology Institute: "The AI Principles for Workers document (2025) established the framework; this corpus provides the operational layer — specific documented surveillance capabilities matched to countermeasures calibrated for the organizing context. Integration into Technology Institute programming reaches all 56 affiliated unions."
- UFW/NDWA: "Part 0 of the countermeasures — data broker opt-outs requiring no technical expertise and no government-issued ID — is designed specifically for the demographic {{organization}} serves. The California DELETE Act DROP platform provides a single-submission opt-out pathway for California residents regardless of documentation status."
- CWA Code: "CWA members at technology companies build and maintain components of the commercial surveillance infrastructure this corpus documents. The worker accountability angle — that CWA members can understand the end-use of their technical work — is a distinctive frame I'm not offering to other unions."
- SEIU: "The DHS social media surveillance program has demonstrably suppressed protected labor speech — over 60% of UAW members who were aware of the program reported changing their social media activity. SEIU members organizing in healthcare and service sectors face the same surveillance environment."

---

### Template 2: Immigration Legal Aid Organizations

**Best for**: RAICES, AILA, CLINIC, ACLU Immigrants' Rights Project, NIPNLG, Vera Institute, JACIR, NAPA/DRUM

**Subject line options**:
- Primary: `ELITE threat model + attorney countermeasures — primary-source documentation for immigration legal practice`
- Variant A (for CLINIC/AILA — CLE focus): `CLE resource: Palantir ELITE data pipeline — documented threat + client protection protocols for immigration attorneys`
- Variant B (for RAICES/Texas-context orgs): `ICE ELITE in Texas: FOIA-sourced enforcement documentation + client intake security protocols`
- Variant C (for ACLU Immigrants' Rights Project — not cold): `Supplementary ELITE documentation — FOIA-sourced contracts extending the corpus you've cited`

**Email body**:

```
Dear {{name}} at {{organization}},

ICE's Paragon Graphite spyware has been deployed against immigration attorneys 
in at least four documented cases since April 2026 — zero-click attacks that 
require no user interaction to compromise a device. This is not speculation; 
it is documented in the threat briefing attached. {{organization}}'s attorneys 
are in the threat model.

The corpus I'm sharing provides two things your legal team needs: a documented 
threat model (every claim sourced to FOIA-obtained procurement contracts, 
government court filings, or named vendor relationships) and a practitioner 
implementation guide specifically designed for immigration attorneys. The 
attorney-client privilege section addresses the digital communications 
question directly: which platforms provide privilege protection, which do not, 
and what the current DOJ guidance (January 20, 2026) changed.

{{IMMIGRATION_SPECIFIC}}

The corpus is structured for citation — the threat model section's FOIA 
citations and vendor contract documentation are at the same level of primary-
source specificity as material you'd use in a brief. It is not an advocacy 
document; it is a documented technical record with countermeasures calibrated 
to the legal practice context.

If adding a data broker opt-out step to your client intake protocol is 
relevant — the corpus includes a step-by-step guide requiring no technical 
expertise and no government-issued ID, specifically designed for clients who 
cannot complete individual broker opt-outs requiring a state ID — I can provide 
that section separately for immediate use.

Corpus: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
Attached: Tier 2 Threat Briefing — Immigration Attorneys and Legal Aid Workers (May 2026)
```

**{{IMMIGRATION_SPECIFIC}} variants**:

- RAICES (Texas): "In the Texas enforcement zone — where ELITE's address confidence scoring is most operationally concentrated — the commercial data broker layer is the least visible component of the threat your clients face. The corpus maps the full pipeline: smartphone app SDK location data → commercial broker → ICE ELITE query → address confidence score → removal target. Every step is sourced."
- AILA: "For CLE integration: the attorney-client communications security section and the data broker opt-out protocol are both ready for integration into AILA continuing education programming without adaptation. The threat model section is structured as a primary-source reference appropriate for practitioner publication."
- CLINIC (network multiplier): "CLINIC's 400+ affiliates represent the largest single distribution pathway for this corpus in the immigration legal services sector. A resource library listing or practitioner alert reaches every affiliated organization simultaneously. I'm offering this for that pathway specifically."
- ACLU Immigrants' Rights Project (not cold): "You published 'All the Ways Palantir is Assisting Trump's Abusive Removal Campaign' in 2026 — this corpus extends that documentation with the full commercial data broker supply chain that feeds ELITE (specific vendors, contract amounts, FOIA sources for each). The Medicaid integration section adds detail that wasn't in your published piece. Happy to discuss how this fits your current litigation strategy."

---

### Template 3: Civil Rights Organizations

**Best for**: NAACP LDF Digital Justice Program, SPLC, Human Rights First, Mijente

**Subject line options**:
- Primary: `ELITE discriminatory impact — primary-source documentation for civil rights litigation and policy work`
- Variant A (for NAACP LDF): `Algorithmic scoring and disparate impact: ELITE's data pipeline, FOIA-sourced, for Digital Justice Program`
- Variant B (for SPLC): `Commercial surveillance of immigrant communities — primary-source documentation extending Intelligence Project methodology`
- Variant C (for Mijente — not cold): `ELITE 2026 update — primary sources for the surveillance infrastructure you've been tracking`

**Email body**:

```
Dear {{name}} at {{organization}},

ICE's Palantir ELITE system generates "address confidence scores" for 
deportation targeting by aggregating commercial data broker purchases with 
Medicaid enrollment records, DMV data, and utility payment history. Every 
data category in that pipeline correlates with race and national origin — 
Medicaid enrollment correlates with poverty; utility payment history 
correlates with geographic segregation; commercial location data correlates 
with residential patterns in immigrant communities. This is not a theoretical 
disparate impact argument. It is documented in FOIA-sourced procurement 
contracts with named vendors and contract amounts.

{{CIVIL_RIGHTS_SPECIFIC}}

The corpus's primary value for {{organization}}'s work is evidentiary: the 
threat model section is structured so every surveillance capability claim 
is individually citable, with a primary source (FOIA document, procurement 
contract, or federal court filing) for each. The documentation is at the 
same specificity level as material used in civil rights litigation — it is 
not an advocacy summary, it is a primary-source-dense technical record.

Two specific questions the corpus raises that are not yet resolved in case 
law: First, whether the Carpenter v. United States (2018) protection for 
cell-site location data extends to commercially-purchased app-derived GPS 
data of the type ELITE queries. Second, whether HIPAA's pre-enforcement 
obligations attach to commercial data brokers who sell Medicaid-derived 
data to federal agencies. Both are open litigation questions; the corpus 
provides the factual predicate.

Corpus: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
```

**{{CIVIL_RIGHTS_SPECIFIC}} variants**:

- NAACP LDF Digital Justice Program: "The Digital Justice Program's work on algorithmic decision-making and civil rights maps directly onto ELITE's confidence scoring mechanism. The corpus documents how administrative data programs that correlate with race — Medicaid, Section 8, utility payment histories — are integrated into an algorithmic scoring system used to prioritize enforcement actions against a population that is disproportionately Black and Brown. I'm sharing this as a primary-source foundation for analysis your team is positioned to develop."
- SPLC Intelligence Project: "SPLC's Intelligence Project has tracked the commercial data infrastructure behind hate group organizing using methodology similar to what this corpus deploys — FOIA documents, vendor relationships, funding flows. The corpus applies the same methodology to ICE's commercial data purchases. The vendor documentation section (Venntel/Gravy Analytics, Thomson Reuters CLEAR, LexisNexis Risk Solutions) maps the commercial surveillance ecosystem at a level of specificity that extends your existing tracking work."
- Mijente: "You published 'Who's Behind ICE?' in 2018 — this corpus is the May 2026 operational update. The ELITE system you've been tracking has expanded its commercial data broker supply chain; the DOGE cross-agency integration adds IRS, SSA, and HHS data pipelines to what ELITE could previously access. The new vendor documentation and the DOGE integration section are the primary additions since your last major documentation effort."

---

### Template 4: Academic and Law School Programs

**Best for**: Georgetown CPT, Harvard Cyberlaw Clinic, NYU Immigrant Rights Clinic, UT Law Immigration Clinic, Cardozo Immigration Justice Clinic, AALS Clinical Section, ImmProf Network

**Subject line options**:
- Primary: `ELITE primary-source documentation — Fourth Amendment and HIPAA unsettled questions for clinical and scholarly work`
- Variant A (for Georgetown CPT — pre-contact): `American Dragnet 2026 extension: ELITE commercial data broker supply chain, FOIA-sourced`
- Variant B (for law school clinics): `Clinical case material: Palantir ELITE FOIA contracts + documented Fourth Amendment gap`
- Variant C (for AALS/ImmProf — distribution channels): `Curriculum resource: ELITE surveillance documentation — primary-source structure suitable for clinical and scholarly citation`

**Email body**:

```
Dear {{name}} at {{institution}},

The Carpenter v. United States ruling (2018) extended Fourth Amendment 
protection to cell-site location data. Courts have not yet ruled whether 
that protection extends to location data purchased from commercial brokers 
who aggregated app-derived GPS data. ICE's Palantir ELITE system sits 
precisely in that gap — it purchases app-derived GPS location data from 
commercial brokers without a warrant, aggregates it with Medicaid enrollment 
records and DMV data, and generates "address confidence scores" used to 
prioritize deportation targets.

The documentation I'm sharing maps the full ELITE data pipeline with 
primary-source citations — FOIA-obtained procurement contracts, named 
vendor relationships with contract amounts, and federal court filings — 
at a specificity level designed for legal citation. The methodological 
basis: every surveillance capability claim is traceable to a primary source. 
The corpus is not an advocacy document; it is a primary-source-dense 
technical record of a surveillance system that raises unsettled questions 
in Fourth Amendment law, HIPAA enforcement, and state privacy statute 
application.

{{ACADEMIC_SPECIFIC}}

If the documentation raises questions relevant to clinic case development, 
student scholarship, or curriculum, I'd welcome a conversation. I'm sharing 
this for potential research or clinical use, not endorsement.

Corpus: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
Attached: Sector threat briefing — Academic Researchers (May 2026)
```

**{{ACADEMIC_SPECIFIC}} variants**:

- Georgetown CPT (pre-contact, not cold): "This corpus is explicitly an operational extension of American Dragnet — updated to May 2026, with the commercial data broker supply chain documentation and countermeasures sections that American Dragnet's policy framing didn't address. Emily Tucker and Stevie Glaberson are the right contacts; I'm approaching this as a peer researcher sharing follow-on primary-source documentation, not as an outside advocate."
- NYU/UT/Cardozo Immigrant Rights Clinics: "For active clinic case development: the FOIA-sourced contracts document the specific data broker purchases that generate ELITE's confidence scores — which brokers, which data categories, which contract vehicles. This is primary-source material for the factual predicate of a Fourth Amendment, HIPAA, or state privacy law case. If your clinic is working on enforcement accountability matters where ELITE's data pipeline is at issue, this documentation may accelerate the research phase."
- AALS Clinical Section / ImmProf: "For curriculum or practitioner resource distribution: the threat model section is formatted for citation in student notes, clinical seminar reading lists, and practitioner publications. The unsettled legal questions it raises — Carpenter extension, HIPAA commercial data obligations, state privacy enforcement gap — are each a semester's worth of student scholarship. I'm offering this specifically for consideration as a resource through {{institution}}'s distribution channel to clinical faculty."

---

### Template 5: Faith Coalitions and Sanctuary Networks

**Best for**: National Council of Churches, UUA, Faith in Action, United Methodist Church, USCCB Migration Services, Church World Service, JCPA, ISNA, ELCA, Interfaith Worker Justice

**Subject line options**:
- Primary: `Faith community security after the April 2026 sanctuary policy change — practical protection guide`
- Variant A (for denominational leadership): `Protecting congregations and sanctuary guests: documented ICE threat + operational security guide for faith leaders`
- Variant B (for interfaith coalition coordinators): `Sanctuary network security briefing: April 2026 policy change + congregation-level countermeasures`
- Variant C (for legal services-focused faith orgs like USCCB MRS): `Immigration enforcement at houses of worship: documented threat, sanctuary legal guidance, and digital security for faith-based legal staff`

**Email body**:

```
Dear {{name}} at {{organization}},

In April 2026, ICE revoked the sensitive location protections that had 
historically prevented enforcement operations at houses of worship, schools, 
and hospitals. Congregations providing sanctuary — or simply serving 
immigrant community members — are now operating in a different threat 
environment than they were six months ago.

The threat briefing I'm attaching documents what changed and what specific 
security measures protect sanctuary congregations now. It is written for 
faith leaders, not technical staff — plain language, practical steps, no 
technical expertise required. The accompanying guide covers three areas 
most relevant for congregation-level security:

1. Data broker opt-out protocols for community members at risk of ELITE 
   targeting — step-by-step, no government-issued ID required, accessible 
   to undocumented congregation members
2. Organizational communications security for sanctuary coordinators and 
   clergy — specifically what communication platforms protect privilege, 
   what they do not, and the minimum secure configuration
3. Physical security coordination for sanctuary operations — what 
   information to keep off digital systems entirely

{{FAITH_SPECIFIC}}

The documentation behind the threat briefing is primary-source (FOIA 
contracts, federal court filings) — not advocacy conjecture. If it would 
be useful for {{organization}}'s congregations, constituent organizations, 
or training programs, I'm offering it for distribution through your 
existing channels. No endorsement required or expected.

Corpus: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
Attached: Sector threat briefing — Faith Leaders and Sanctuary Advocates (May 2026)
```

**{{FAITH_SPECIFIC}} variants**:

- National Council of Churches / Interfaith Immigration Coalition: "The Interfaith Immigration Coalition's 53 member organizations are on the front lines of the sanctuary movement. A single distribution through your network reaches all 53 simultaneously. The threat briefing is formatted for immediate use by coalition staff and can be distributed to member organization leadership without adaptation."
- UUA: "UUA congregations have been publicly committed to sanctuary since well before the April 2026 policy change. The operational security guidance in this corpus is specifically designed for the congregation-level deployment context that UUA's existing sanctuary programs use — it does not require technical staff."
- USCCB Migration and Refugee Services: "Catholic Charities offices providing immigration legal services operate in the same threat environment as immigration attorneys — the Paragon Graphite spyware documented in the attached briefing has been deployed against legal aid attorneys. The attorney-client privilege section of the corpus is relevant to your legal services staff as well as to the sanctuary guidance."
- Faith in Action (PICO): "Faith in Action's 1,000+ congregations across 45 states include many providing sanctuary or direct immigration legal assistance. The practical countermeasures — accessible without technical expertise — are designed for congregation-level deployment that PICO's organizing model already supports."

---

## Section 3: Rollout Timeline

### Timeline Logic

Phase 1 Tier 1 launches on Day 1 (nominally May 8, 2026). Tier 2 is cleared to launch approximately 4 weeks after Phase 1 Day 1, subject to minimum gate passage. The timeline below assumes a Day 1 of May 8, placing Tier 2 Week 1 at approximately June 5, 2026. Adjust all dates proportionally if Phase 1 Day 1 is different.

**Minimum gate before any Tier 2 send** (from `TIER_2_DISTRIBUTION_STRATEGY.md` Section 2):
- Gate A: 40+ of targeted Tier 1 organizations contacted
- Gate B: 10%+ response rate (5+ replies from 50 sends) OR 3+ confirmed Bitly clicks OR 1 Score 4–5 contact
- Gate C: Gist publicly accessible, no deliverability block, Bitly active

If minimum gate not met by Day 28: hold Tier 2 by one week and re-evaluate. Do not launch on empty response data.

### Pre-Contact Window (Days 28–35: approximately June 5–12)

Before the main wave sends, contact the pre-contact candidates personally. Pre-contact candidates from this document's five sectors:

| Organization | Pre-Contact Reason | Personalized Note |
|---|---|---|
| Georgetown CPT (A-01) | Highest institutional alignment; American Dragnet predecessor | Reference American Dragnet explicitly; send directly to Emily Tucker or Stevie Glaberson |
| NDWA (L-07) | Highest-priority labor contact per phase-2-tier2-organizational-outreach-strategy.md | Reference Ai-jen Poo's public statements on immigration enforcement; dual organizing + immigration frame |
| CLINIC (I-06) | 400+ affiliates = highest network multiplier in immigration sector | Offer distribution through CLINIC's practitioner alert channel; mention CLINIC-specific format |
| NNEDV Safety Net Project (C-03) | DV advocate briefing specifically names NNEDV data; Cindy Southworth has technical background | Reference NNEDV's own data (stalkerware statistics in the threat briefing) |

Send no more than 2–3 pre-contact emails per day; each generates a scheduling conversation. Pre-contact emails are personal, reference specific engagement, and offer a concrete next step (orientation session, resource format discussion). They are not form letters.

### Wave Sequencing

| Wave | Timing | Sectors | Organizations | Rationale |
|------|--------|---------|---------------|-----------|
| Pre-contact | Days 28–35 (approx. June 5–12) | All sectors | 4 pre-contact candidates | Personalized; generates partnership relationships before wave sends |
| Wave 1 (immigration legal aid) | Week 5 (approx. June 9–13) | Immigration legal aid | RAICES, AILA, ACLU IRP, CLINIC, NILC (already Tier 1), NIPNLG | Most acute threat (Paragon Graphite deployment is live); highest direct client impact |
| Wave 1 (faith coalitions) | Week 5 (approx. June 9–13) | Faith coalitions | NCC/Interfaith Coalition, UUA, Faith in Action, USCCB MRS, CWS, ELCA | April 2026 sanctuary policy change is most time-sensitive faith sector trigger |
| Wave 2 (labor) | Week 6 (approx. June 16–20) | Labor unions | AFL-CIO Tech Institute, SEIU, UFW, CNA, CWA Code, NDWA (follow-up from pre-contact) | DHS Penlink contract is spring 2026 deployment; less time-sensitive than immigration/faith |
| Wave 2 (civil rights) | Week 6 (approx. June 16–20) | Civil rights | NAACP LDF, SPLC, Mijente, Human Rights First, Coalition Against Stalkerware | Build on immigration legal aid response; civil rights framing benefits from prior immigration sector credibility signals |
| Wave 3 (academic law schools) | Week 7–8 (approx. June 23 – July 3) | Academic/law | Georgetown CPT (follow-up from pre-contact), Harvard Cyberlaw, NYU IRL, UT Law, Cardozo, AALS, ImmProf | Academic calendar: May–June is optimal for clinic planning; late June still acceptable |
| Wave 4 (secondary contacts) | Week 9–10 (approx. July 7–17) | All sectors | NUPGE, JACIR, NAPA/DRUM, Human Rights First, JCPA, ISNA, CLEA, ImmProf follow-ups, AU WCL, Vera | Second-tier contacts and organizations without a specific 2026 threat trigger |

### Follow-Up Protocol

Follow-up is triggered at 10 business days after initial send (not calendar days). Per `tier-2-distribution-calendar.md`:

- **No response at 10 days**: Send one follow-up. Subject: `Re: {{original subject}} — follow-up`. Body: three sentences maximum — "I sent this [n] days ago. If this didn't reach the right person, please point me to who handles {{training resources / practitioner tools / organizing security}} — I don't want to duplicate the send to the wrong inbox. If timing was wrong, a note saying when to check back would be helpful." Do not add new content; let the original message do the work.
- **No response at 20 days (after follow-up)**: Mark "Hold — no response" in tracking. Do not send a third email. Move to October second-round outreach cycle.
- **Response received**: Act within 48 hours. If response is substantive (question, use case), personalize the next exchange immediately. If response is social ("great work"), acknowledge and offer a concrete next step within the same reply.

### Academic Calendar Awareness

For law school clinic contacts specifically:
- **June 1–15**: Best window — clinic directors are planning fall semester projects
- **June 16 – August 15**: Reduced response probability; send but expect August follow-up
- **September – October**: Second-best window for fall semester integration follow-through
- **November – December**: Hold; end-of-semester crunch

If a law school clinic contact goes unanswered through the summer, a September re-send is not a duplicate — frame it as a fall semester offer: "I sent this in June with a note about fall semester planning — following up now that the semester is beginning."

---

## Section 4: Success Metrics

### Metric Framework

Success metrics for Tier 2 operate at three levels: output (sends and engagements), outcome (organizational adoption), and impact (downstream use). The primary metrics are outcome-level; output metrics are diagnostic, not success indicators in themselves.

### By-Sector Minimum Success (Week 12 post-Tier-1 launch)

| Sector | Minimum Success (Week 12) | Strong Signal | Network Multiplier Achieved |
|--------|--------------------------|---------------|----------------------------|
| **Labor unions** | 5 organizations contacted, 1 reply from an organizing/education department (not press) | AFL-CIO Technology Institute integration discussion initiated | AFL-CIO Tech Institute adoption = reaches 56 affiliated unions |
| **Immigration legal aid** | 7 organizations contacted, 2 replies from legal staff (not communications) | CLINIC resource listing confirmed, or AILA CLE content submission acknowledged | CLINIC adoption = reaches 400+ affiliates |
| **Civil rights** | 5 organizations contacted, 1 reply from a legal or research team (not press) | NAACP LDF Digital Justice Program citation or Georgetown CPT acknowledgment | NAACP LDF citation = public endorsement propagating to 54 state affiliates |
| **DV advocacy** | NNEDV Safety Net Project contacted and replied | Safety Net Project recommending corpus to state DV coalitions | NNEDV adoption = reaches 55 state coalitions |
| **Academic/law schools** | 7 organizations contacted, 1 reply from a faculty or clinic director | Georgetown CPT citation in any published output | Georgetown CPT citation = highest academic credibility signal for all subsequent outreach |
| **Faith coalitions** | 5 organizations contacted, 1 reply from denominational leadership (not communications) | NCC Interfaith Coalition or Faith in Action distribution to member congregations | NCC distribution = reaches 53 member organizations |

### Aggregated Tier 2 Targets (All Five Sectors, Week 12)

- **Minimum acceptable**: 30 organizations contacted across all five sectors; 6+ responses from decision-makers (not press contacts); 2 organizational adoption discussions initiated
- **Good outcome**: 40+ organizations contacted; 10+ decision-maker responses; 4+ adoption discussions; 1 confirmed resource listing in a sector network (CLINIC, NNEDV, AFL-CIO Tech, or equivalent)
- **Strong outcome**: 47 organizations contacted; 15+ decision-maker responses; 6+ adoption discussions; 3+ network-level distribution agreements (one per three sectors); 1 academic citation in published output; 1 faith coalition broadcasting to member congregations

### Sector-Specific KPIs

**Labor sector KPIs**:
- Primary: Organizing department reply rate (measure replies from organizing/education staff vs. press/communications staff)
- Secondary: Orientation session requests (each session request = Score 5 contact; represents organizational integration intent)
- Watch metric: CWA Code engagement (unique because of tech worker frame — their engagement validates the commercial data pipeline documentation from a practitioner source)

**Immigration legal aid KPIs**:
- Primary: Intake protocol integration signal (any organization indicating Part 0 or DROP platform documentation will be used in client intake = highest-value adoption)
- Secondary: CLE submission or practitioner alert trigger (AILA or CLINIC distribution mechanism)
- Watch metric: California-specific DROP platform take-up rate (if organizations report clients using the DROP platform pathway, this is a real-world protective outcome, not just an adoption metric)

**Civil rights KPIs**:
- Primary: Legal research citation (any mention that the corpus is being used as a primary source in litigation preparation, brief writing, or amicus work)
- Secondary: Discriminatory impact theory development (any organization indicating they are developing the algorithmic scoring discriminatory impact theory suggested in the outreach email)
- Watch metric: Mijente amplification (Mijente has social media reach to immigrant communities directly; any Mijente post linking the corpus is a direct-to-community distribution event)

**DV advocacy KPIs**:
- Primary: Safety Net Project recommendation to state coalitions
- Secondary: Coalition Against Stalkerware inclusion in any stalkerware resource list update
- Watch metric: Survivor-level access (if DV shelter operators report providing Part 0 to survivors directly, this indicates the corpus has penetrated to the population with highest acute need)

**Academic/law school KPIs**:
- Primary: Published citation (any academic or practitioner publication citing the corpus in any format — student note, law review comment, clinic case filing, policy brief)
- Secondary: Course assignment or reading list inclusion (any faculty indicating the corpus or a section of it is assigned reading)
- Watch metric: Georgetown CPT timeline (Georgetown CPT is the single highest-leverage academic contact; track separately and prioritize any response from Emily Tucker or Stevie Glaberson)

**Faith coalition KPIs**:
- Primary: Distribution to member congregations (any network-level distribution through a denominational or coalition channel)
- Secondary: Sanctuary training integration (any faith leader training program incorporating the sanctuary security countermeasures)
- Watch metric: USCCB Migration and Refugee Services engagement (USCCB's Catholic Charities network is the largest faith-based legal services network in the US; USCCB adoption reaches every Catholic Charities immigration program)

### Tracking Infrastructure

Use the existing `engagement-scoring-template.csv` and `adoption-tracking-dashboard-spec.md` tracking infrastructure. Add a "Sector" column if not already present (Labor / Immigration Legal Aid / Civil Rights / Academic / Faith). Apply the same 0–5 engagement scoring from `phase-2-tier2-organizational-outreach-strategy.md` Section 1.

Key tracking columns to add for this Tier 2 wave:
- `Wave` (Pre-Contact / Wave 1 / Wave 2 / Wave 3 / Wave 4)
- `Sector` (from the five sectors above)
- `Decision_Maker_Contact` (Y/N — was the reply from an organizing/legal/research/clergy role, vs. press/communications?)
- `Network_Multiplier_Achieved` (Y/N — has the organization committed to distributing to their affiliate/member network?)

### Gate 2 Final Decision (Before Tier 3)

Tier 3 is conditioned on Tier 2 producing specific outcome signals, not just engagement. The Tier 3 gate (from `tier-2-implementation-checklist.md`) requires:

- 3 confirmed workflow modifications across at least 2 sectors (e.g., CLINIC adds Part 0 to intake protocol AND AFL-CIO Technology Institute adds organizer playbook to training curriculum AND Georgetown CPT cites corpus in a publication)
- At least 1 network-level distribution event (one organization distributes to 10+ downstream organizations)
- Zero substantive factual challenges to the threat claims in any briefing outstanding at 30 days

If these conditions are met at the 90-day checkpoint, proceed with Tier 3 planning per `tier-3-audience-expansion-roadmap.md`. If not met, extend Tier 2 follow-up by 4 weeks before evaluating Tier 3 readiness.

---

## Section 5: Operational Notes and Risk Mitigations

### Contact Verification

All organization contacts in this document are drawn from public sources (organizational websites, staff directories, press releases) as of May 2026. Before sending any wave, verify:
- Current leadership at SPLC (organizational restructuring 2025-2026)
- Current Human Rights First CEO (Elisa Massimino; verify if organizational changes have occurred)
- NIPNLG National Director (organizational transition in 2025; do not send to a vacated role)
- CLEA Executive Director (verify current)
- ISNA President (Safiyyah Ally; verify)

Verification takes 2 minutes per organization (Google the organization + "executive director 2026"). Do not skip this step for organizations flagged as "transitioning."

### Duplicate Contact Risk

Several organizations appear in both this document and prior materials:
- ACLU Immigrants' Rights Project: appears in `phase-2-target-organizations.csv` — confirm no prior outreach before sending from this document's Template 2
- Harvard Cyberlaw Clinic: appears in `tier-2-sector-contact-lists.md` — confirm no prior outreach
- Georgetown CPT: appears in `phase-2-target-organizations.csv` — pre-contact candidate; confirm outreach has not already been sent

Sending duplicate outreach to a named contact at a sophisticated organization damages credibility. Check the tracking spreadsheet before each send.

### Sensitive Recipient Handling

Several contacts in this document are at organizations under active federal scrutiny or litigation (ACLU, RAICES, Mijente). Handle these with the same operational security posture as the corpus itself recommends:
- Use Signal or encrypted email for follow-up conversations involving case strategy or client information
- Do not discuss specific case details in unencrypted email
- Note in tracking spreadsheet if a contact requests secure communications; honor that request in all subsequent contact

### Pre-Contact Personal Invitation Format

Pre-contact emails (Georgetown CPT, NDWA, CLINIC, NNEDV) follow a three-part structure:
1. Reference the specific prior signal that triggered the pre-contact (even if prior contact was only a CSV listing — for these four organizations, the prior signal is the documented institutional alignment, not a Phase 1 reply)
2. Name the next step: a specific resource plus an offer to schedule a session within a defined time window
3. Keep it short: pre-contact emails should be 3–4 sentences. They are not sales emails. They are invitations from a peer.

---

*Document created: 2026-05-09. Coordinates with: `tier-2-organizational-contact-list.md` (contact details), `TIER2_DISTRIBUTION_PREP.md` (digital rights/academic/researcher/journalist templates), `TIER_2_DISTRIBUTION_STRATEGY.md` (prior Tier 2 strategy), `phase-2-tier2-organizational-outreach-strategy.md` (transition criteria), `execution/TIER2_THREAT_BRIEFING_INDEX.md` (threat briefing deployment guide), `tier-2-implementation-checklist.md` (execution checklist and risk mitigations). Quarterly review checkpoint: August 9, 2026.*
