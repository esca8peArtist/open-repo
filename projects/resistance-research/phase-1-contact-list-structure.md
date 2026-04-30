---
title: "Phase 1 Contact List Structure — Tier 1 Institutions"
created: 2026-04-30
status: ready-to-populate
path-agnostic: true
purpose: "Database schema and contact list organization for 25 Tier 1 institutions across law schools, think tanks, and policy organizations. Fields, sourcing methodology, and domain relevance scoring."
companion_files:
  - phase-1-outreach-email-templates.md
  - phase-1-email-sequence-framework.md
  - BATCH_1_CONTACT_VERIFICATION.md
  - DISTRIBUTION_OUTREACH_CONTACTS.md
---

# Phase 1 Contact List Structure — Tier 1 Institutions

**Scope**: Database schema, field definitions, sourcing methodology, and pre-populated institution framework for 25 Tier 1 organizations. Contact-level fields (name, email, title) require user research before sending — the schema and institution list are complete; contact-level fill-in takes approximately 10–15 minutes per institution.

**Relationship to existing contacts**: The existing `DISTRIBUTION_OUTREACH_CONTACTS.md` and `BATCH_1_CONTACT_VERIFICATION.md` contain verified contacts for Batch 1 (5 contacts). This document provides the broader 25-institution framework for Batches 1–5 and the schema for tracking outreach progress.

---

## 1. Database Schema

Use a spreadsheet (Google Sheets, Airtable, or CSV) with the following fields. One row per contact, not per institution (a single institution may have 2–3 contacts at different levels).

### Required Fields (Must Fill Before Sending)

| Field Name | Type | Description |
|-----------|------|-------------|
| `institution_name` | Text | Full official name of the institution |
| `institution_short` | Text | Short name used in email drafts (e.g., "Yale Law," "Brennan Center") |
| `sector` | Dropdown | Law School / Think Tank / Policy Org |
| `sub_sector` | Text | More specific: "Constitutional Law," "National Security," "Democracy Research," "Civil Rights," "Immigration," "Environmental," "Labor," "Election Protection" |
| `contact_name` | Text | Full name of primary contact |
| `contact_title` | Text | Current title — verify before sending (people move) |
| `contact_email` | Text | Professional email, not personal |
| `contact_role_type` | Dropdown | Director / Senior Researcher / Counsel / Faculty / Program Lead |
| `institutional_mandate_fit` | Text (1–2 sentences) | What is this institution's core mandate, and which 1–2 domains map directly to it? |
| `domain_relevance_score` | Integer 1–5 | How directly does the proposal's content map to this institution's active work? 5 = high relevance (active litigation or research in this exact area); 3 = medium (general mandate overlap); 1 = tangential |
| `primary_domain` | Text | The single domain most relevant to this contact (e.g., "Domain 28 — War Powers") |
| `secondary_domains` | Text | Comma-separated list of 1–2 additional relevant domains |
| `notes` | Text | Any specific context — recent publication to reference, pending case, known network connection |

### Outreach Tracking Fields (Fill As You Send)

| Field Name | Type | Description |
|-----------|------|-------------|
| `batch_number` | Integer | Which send batch (1–5) |
| `email_sent_date` | Date | Date primary email sent |
| `subject_line_variant` | Text | "A," "B," "C," or "D" — tracks which subject line variant |
| `email_template` | Text | "Primary," "Follow-Up," "Relationship-Building" |
| `response_received` | Boolean | Y/N |
| `response_date` | Date | Date of first response |
| `response_type` | Dropdown | Acknowledgment / Feedback / Referral Offer / Forwarding Offer / Call Request / No Response |
| `follow_up_sent_date` | Date | Date of follow-up email (if sent) |
| `relationship_status` | Dropdown | Cold / First Contact / Engaged / Ongoing / Declined |
| `referrals_generated` | Integer | Number of new contacts generated from this relationship |

---

## 2. Institution Framework — 25 Tier 1 Organizations

Organized by sector. Contact-level fields (name, email, title) require user research using the sourcing methodology in Section 3. Domain relevance scores and institutional mandate fit are pre-populated.

### Sector 1: Law Schools (8 institutions)

**Institution 1**: Yale Law School — Constitutional Law / Administrative Law Program
- Sector: Law School
- Sub-sector: Constitutional Law, Administrative Law
- Institutional mandate fit: Public interest law scholarship, constitutional accountability, separation of powers. Domains 2, 6, 28, 29 are directly relevant to current faculty research areas.
- Domain relevance score: 5
- Primary domain: Domain 6 (Judicial Independence)
- Secondary domains: Domain 2 (Executive Power), Domain 29 (Prosecutorial Weaponization)
- Contact target: Director, Constitutional Clinics; or Kurland Professor of Law covering executive power
- Notes: Yale's Rule of Law Clinic has active dockets in executive accountability. Justice Department FOIA project is particularly relevant to Domain 29.

**Institution 2**: Harvard Law School — Cyberlaw Clinic / Constitutional Law Program
- Sector: Law School
- Sub-sector: Constitutional Law, Digital Rights
- Institutional mandate fit: Cyberlaw Clinic active on First Amendment and platform accountability; Constitutional Law faculty working on executive immunity. Domains 6, 7, 21 directly relevant.
- Domain relevance score: 5
- Primary domain: Domain 21 (Data Privacy and Digital Surveillance)
- Secondary domains: Domain 6 (Judicial Independence), Domain 7 (Rights Protection)
- Contact target: Director, Cyberlaw Clinic; or Constitutional Law faculty working on executive power post-June 2024 immunity decision
- Notes: Harvard Kennedy School's Democratic Governance and Innovation program is a secondary contact if law school outreach stalls.

**Institution 3**: Georgetown Law — Institute for Constitutional Advocacy and Protection (ICAP)
- Sector: Law School
- Sub-sector: Constitutional Law, Civil Rights Litigation
- Institutional mandate fit: ICAP does direct legal representation and impact litigation on constitutional rights. Domains 7, 29, 16 directly relevant to current dockets.
- Domain relevance score: 5
- Primary domain: Domain 7 (Rights Protection)
- Secondary domains: Domain 16 (Immigration), Domain 29 (Prosecutorial Weaponization)
- Contact target: ICAP Executive Director; or faculty directing immigration rights clinic
- Notes: ICAP filed amicus briefs in multiple cases currently in the Litigation Tracker. Reference specific case in personalization paragraph.

**Institution 4**: Columbia Law School — Knight First Amendment Institute
- Sector: Law School
- Sub-sector: First Amendment, Academic Freedom
- Institutional mandate fit: Knight Institute specifically focused on First Amendment rights in the digital era — directly relevant to Domains 7, 8, 27. Active litigation on press freedom and academic freedom.
- Domain relevance score: 5
- Primary domain: Domain 27 (Higher Education and Academic Freedom)
- Secondary domains: Domain 7 (Rights Protection), Domain 8 (Media and Information)
- Contact target: Knight Institute Executive Director; or Research Director
- Notes: Knight Institute has published on the student visa revocations (relevant to Domain 27). Reference their specific publications.

**Institution 5**: University of Texas Law — Texas Law Review / Administrative Law Program
- Sector: Law School
- Sub-sector: Administrative Law, Energy/Environmental Law
- Institutional mandate fit: Administrative law scholarship directly relevant to post-Loper Bright regulatory landscape (Domain 5, Domain 6). Energy and environmental law relevant to Domains 15, 23.
- Domain relevance score: 4
- Primary domain: Domain 5 (Congressional Structure and Administrative Reform)
- Secondary domains: Domain 15 (Environment and Climate), Domain 23 (Trade Policy)
- Contact target: Administrative Law faculty; Texas Environmental Law Journal editor
- Notes: Texas Law is in a state with active redistricting litigation — Domain 1 (Electoral Reform) is a viable secondary angle.

**Institution 6**: University of Michigan Law — Civil Rights Litigation Initiative
- Sector: Law School
- Sub-sector: Civil Rights, Voting Rights
- Institutional mandate fit: Civil rights litigation focus; voting rights work directly relevant to Domains 1, 7, 22. Michigan faculty have published on gerrymandering and redistricting.
- Domain relevance score: 4
- Primary domain: Domain 1 (Electoral Reform)
- Secondary domains: Domain 22 (Reparations and Racial Justice), Domain 37 (2026 Midterms)
- Contact target: Civil Rights Litigation Initiative Director; or Voting Rights faculty
- Notes: Michigan has produced litigation in the Brennan Center's redistricting tracker — reference specific case.

**Institution 7**: NYU Law School — Brennan Center for Justice (housed at NYU)
- Sector: Law School (adjacent — Brennan Center is formally at NYU)
- Sub-sector: Democracy Research, Voting Rights, Justice
- Institutional mandate fit: Brennan Center is the primary institutional democracy reform research organization in the U.S. Direct mandate overlap with nearly every domain. Already cited extensively in the proposal — frame the outreach as sharing research that builds on their work.
- Domain relevance score: 5
- Primary domain: Domain 1 (Electoral Reform) — Brennan Center's primary focus
- Secondary domains: Domain 6 (Judicial Independence), Domain 37 (2026 Midterms)
- Contact target: Democracy Program Director; or Justice Program Director
- Notes: Brennan Center is cited throughout the proposal — the personalization paragraph should reference a specific recent Brennan Center publication. This is a Batch 1 candidate.

**Institution 8**: Stanford Law School — Mills Legal Clinic / Immigrants' Rights Project
- Sector: Law School
- Sub-sector: Immigration Law, Criminal Justice
- Institutional mandate fit: Immigrants' Rights Project active on detention, removal, and due process — directly relevant to Domains 16, 7. Criminal justice reform work relevant to Domain 14.
- Domain relevance score: 4
- Primary domain: Domain 16 (Immigration)
- Secondary domains: Domain 14 (Criminal Justice and Policing), Domain 7 (Rights Protection)
- Contact target: Immigrants' Rights Project Director; or Clinical Faculty supervising detention dockets

---

### Sector 2: Think Tanks (9 institutions)

**Institution 9**: Brennan Center for Justice (standalone contact — separate from NYU Law contact)
- Sector: Think Tank
- Sub-sector: Democracy Research, Voting Rights, Judicial Independence
- Institutional mandate fit: Primary U.S. democracy reform research institution. Proposal builds on and extends Brennan Center research extensively.
- Domain relevance score: 5
- Primary domain: Domain 37 (2026 Midterms / Election Protection)
- Secondary domains: Domain 1 (Electoral Reform), Domain 6 (Judicial Independence)
- Contact target: Senior Research Fellow, Elections; or Director, Voting Rights and Elections Program
- Notes: Distinguish this contact from the NYU Law contact above. Different staff, different programs.

**Institution 10**: Just Security (NYU-affiliated national security law journal)
- Sector: Think Tank (adjacent — it is an online journal with think-tank-style commentary)
- Sub-sector: National Security Law, War Powers, Executive Power
- Institutional mandate fit: Just Security published the most rigorous OLC memo analysis after the Venezuela operation — the proposal builds directly on their documentation. Domain 28 is the direct entry point.
- Domain relevance score: 5
- Primary domain: Domain 28 (War Powers, Venezuela)
- Secondary domains: Domain 2 (Executive Power), Domain 6 (Judicial Independence)
- Contact target: Founding Editor or Managing Editor
- Notes: Reference their specific Venezuela/OLC memo coverage in the personalization paragraph. This is a Batch 1 candidate.

**Institution 11**: Center for American Progress (CAP)
- Sector: Think Tank
- Sub-sector: Progressive Policy Research (multi-issue)
- Institutional mandate fit: CAP covers healthcare, labor, immigration, climate, democracy — broad mandate overlap. Best approach: lead with the domain where CAP has current active publication rather than generic outreach.
- Domain relevance score: 4
- Primary domain: Select from CAP's current priority portfolio — check capmedia.org before sending
- Secondary domains: Domain 22 (Racial Justice), Domain 17 (Labor)
- Contact target: Director, Democracy or Elections program; or Senior Fellow covering current publication area
- Notes: CAP's institutional relationships make referrals the highest-value outcome here.

**Institution 12**: Cato Institute
- Sector: Think Tank
- Sub-sector: Libertarian Policy Research (civil liberties, executive power)
- Institutional mandate fit: Cato's civil liberties and executive power work overlaps with Domains 2, 6, 7, 21 — particularly on surveillance, presidential immunity, and executive overreach. The proposal's structural reform framing is bipartisan; civil liberties domains are genuine shared interest.
- Domain relevance score: 3
- Primary domain: Domain 21 (Data Privacy / Surveillance)
- Secondary domains: Domain 2 (Executive Power), Domain 7 (Rights Protection)
- Contact target: Senior Fellow, Constitutional Studies or Civil Liberties
- Notes: Frame the outreach around shared concern for executive power restraint and civil liberties — not partisan framing. Cato contacts forwarding the research cross-ideological lines, which significantly expands reach.

**Institution 13**: Quincy Institute for Responsible Statecraft
- Sector: Think Tank
- Sub-sector: Foreign Policy, War Powers, Military Restraint
- Institutional mandate fit: Quincy's mandate is directly aligned with Domain 28 (War Powers, Venezuela) and Domain 19f (War Powers Reform). Quincy publishes the most sustained critical analysis of executive military unilateralism.
- Domain relevance score: 5
- Primary domain: Domain 28 (War Powers, Venezuela)
- Secondary domains: Domain 19f (War Powers Reform)
- Contact target: Executive Director or Senior Fellow covering Latin America / military operations
- Notes: Quincy is cited in Domain 28. Reference specific Quincy analysis in personalization. This is a Batch 1 candidate.

**Institution 14**: Economic Policy Institute (EPI)
- Sector: Think Tank
- Sub-sector: Labor Economics, Wage Policy
- Institutional mandate fit: EPI's labor market research directly informs Domain 17 (Labor and Employment). Sectoral bargaining analysis, minimum wage evidence, non-compete bans are all EPI research areas.
- Domain relevance score: 4
- Primary domain: Domain 17 (Labor and Employment)
- Secondary domains: Domain 18 (Social Safety Net), Domain 22 (Racial Justice economic dimensions)
- Contact target: President or Senior Economist covering wage policy
- Notes: EPI's research is cited in Domain 17. Frame the outreach as sharing research that synthesizes their work with constitutional design reform.

**Institution 15**: Urban Institute
- Sector: Think Tank
- Sub-sector: Housing, Health Policy, Criminal Justice
- Institutional mandate fit: Urban's housing research (Domain 13), healthcare policy (Domain 31 / OBBBA Medicaid), and criminal justice (Domain 14) are all direct mandate overlaps. Multi-domain approach is appropriate here.
- Domain relevance score: 4
- Primary domain: Domain 31 (Healthcare Access — OBBBA Medicaid)
- Secondary domains: Domain 13 (Housing), Domain 14 (Criminal Justice)
- Contact target: Senior Fellow, Health Policy; or Director, Justice Policy Center
- Notes: Urban's Medicaid impact modeling is likely more current than what's in the proposal — frame the outreach as wanting their feedback on the healthcare analysis.

**Institution 16**: Demos (Democracy and Policy Research)
- Sector: Think Tank
- Sub-sector: Democracy, Economic Equality
- Institutional mandate fit: Demos works on structural democracy reform, economic equality, and racial justice — Domains 1, 22, 5, and 3 are direct mandate overlaps.
- Domain relevance score: 4
- Primary domain: Domain 3 (Democratic Participation)
- Secondary domains: Domain 1 (Electoral Reform), Domain 22 (Racial Justice)
- Contact target: President or Senior Policy Analyst, Democracy Program
- Notes: Demos has worked with Brennan Center on democracy reform campaigns — a Demos referral to Brennan Center contacts (or vice versa) would be valuable.

**Institution 17**: R Street Institute
- Sector: Think Tank
- Sub-sector: Center-right policy research (criminal justice, financial regulation, governance)
- Institutional mandate fit: R Street's criminal justice reform work (Domain 14) and governance research (Domain 2, Domain 5) are genuine overlaps. Like Cato, a center-right think tank engaging with the proposal creates cross-ideological reach.
- Domain relevance score: 3
- Primary domain: Domain 14 (Criminal Justice and Policing)
- Secondary domains: Domain 5 (Congressional Structure), Domain 2 (Executive Power)
- Contact target: Senior Fellow, Criminal Justice; or Governance Program Director
- Notes: Frame as structural reform research, not partisan. R Street's criminal justice work is genuinely evidence-based.

---

### Sector 3: Policy Organizations (8 institutions)

**Institution 18**: Protect Democracy
- Sector: Policy Org
- Sub-sector: Democracy, Anti-Autocracy, Litigation
- Institutional mandate fit: Protect Democracy's retaliatory action tracker is cited in Domain 29. Direct mandate overlap with the full proposal. They are the primary institutional tracker of executive retaliation against political opposition.
- Domain relevance score: 5
- Primary domain: Domain 29 (Prosecutorial Weaponization)
- Secondary domains: Domain 2 (Executive Power), Domain 37 (2026 Midterms)
- Contact target: Litigation Director or Senior Counsel
- Notes: The proposal builds on Protect Democracy's tracker — frame the outreach as sharing a structural synthesis that complements their case-by-case documentation. This is a Batch 1 candidate.

**Institution 19**: Democracy Docket (Marc Elias organization)
- Sector: Policy Org
- Sub-sector: Election Law, Voting Rights Litigation
- Institutional mandate fit: Democracy Docket's election litigation directly informs Domain 1 and Domain 37. They are the primary tracker of redistricting and voting rights cases.
- Domain relevance score: 5
- Primary domain: Domain 37 (Federal Executive Interference in 2026 Midterms)
- Secondary domains: Domain 1 (Electoral Reform)
- Contact target: Research Director or Senior Counsel
- Notes: Reference a specific recent Democracy Docket case in the personalization paragraph. Domain 37 is the direct entry point.

**Institution 20**: Campaign Legal Center
- Sector: Policy Org
- Sub-sector: Campaign Finance, Voting Rights
- Institutional mandate fit: CLC's work on campaign finance reform and voting rights directly informs Domains 1 and 5. They have active litigation in redistricting and campaign finance.
- Domain relevance score: 4
- Primary domain: Domain 1 (Electoral Reform — campaign finance subsection)
- Secondary domains: Domain 5 (Congressional Structure — filibuster and campaign finance reform)
- Contact target: President or Senior Counsel, Voting Rights
- Notes: CLC's recent FEC enforcement work is directly relevant to Domain 5's campaign finance analysis.

**Institution 21**: American Civil Liberties Union (ACLU) — National Political Accountability or Voting Rights Project
- Sector: Policy Org
- Sub-sector: Civil Liberties, Voting Rights, Immigration, National Security
- Institutional mandate fit: ACLU's multi-program structure means multiple contacts are warranted — National Security Project for Domain 21/28, Voting Rights Project for Domain 1/37, Immigrants' Rights Project for Domain 16.
- Domain relevance score: 5
- Primary domain: Domain 7 (Rights Protection)
- Secondary domains: Domain 16 (Immigration), Domain 1 (Electoral Reform)
- Contact target: Director, National Political Accountability Project; or Staff Attorney, Voting Rights Project
- Notes: The ACLU is cited throughout the proposal. This is likely a follow-on contact after initial batches — their response rate to cold outreach is lower than smaller organizations; a warm introduction from a law school clinic or think tank contact significantly improves the probability of engagement.

**Institution 22**: Lawyers' Committee for Civil Rights Under Law
- Sector: Policy Org
- Sub-sector: Civil Rights Litigation, Voting Rights
- Institutional mandate fit: Voting rights litigation and civil rights enforcement — Domains 1, 22, 7 are direct mandate overlaps.
- Domain relevance score: 4
- Primary domain: Domain 22 (Reparations and Racial Justice)
- Secondary domains: Domain 1 (Electoral Reform), Domain 7 (Rights Protection)
- Contact target: President and Executive Director; or Voting Rights Project Director
- Notes: Frame around the VRA restoration analysis in Domain 1 and the structural reform proposals in Domain 22.

**Institution 23**: Demand Progress
- Sector: Policy Org
- Sub-sector: Progressive Advocacy, Congressional Reform, War Powers
- Institutional mandate fit: Demand Progress runs active campaigns on war powers, surveillance, and congressional reform — Domains 19f, 28, 25 (FISA), and 5 are direct overlaps.
- Domain relevance score: 4
- Primary domain: Domain 28 (War Powers, Venezuela) or Domain 25 (Surveillance / FISA)
- Secondary domains: Domain 5 (Congressional Structure), Domain 19f (War Powers Reform)
- Contact target: National Director or Senior Policy Advocate
- Notes: Demand Progress has a congressional base — referrals to Hill staff are a valuable outcome of this relationship.

**Institution 24**: States United Democracy Center
- Sector: Policy Org
- Sub-sector: State-Level Democracy, Election Administration
- Institutional mandate fit: States United tracks state-level democratic erosion (Domain 9b candidate) and election administration threats (Domain 37). Their work on election official threats and state legislature action is directly relevant.
- Domain relevance score: 4
- Primary domain: Domain 37 (2026 Midterms / Election Protection)
- Secondary domains: Domain 1 (Electoral Reform — state-level redistricting angle)
- Contact target: Executive Director or Senior Counsel
- Notes: States United is positioned at the intersection of law school, think tank, and advocacy — the tone should be collegial rather than activist-facing.

**Institution 25**: Indivisible Project (national organization, not local chapters)
- Sector: Policy Org
- Sub-sector: Grassroots Organizing, Congressional Advocacy
- Institutional mandate fit: Indivisible's congressional advocacy work directly informs understanding of which reform proposals have grassroots political traction. Domain 5 (Congressional Structure), Domain 1 (Electoral Reform), and Domain 3 (Democratic Participation) are direct overlaps.
- Domain relevance score: 3
- Primary domain: Domain 3 (Democratic Participation)
- Secondary domains: Domain 1 (Electoral Reform), Domain 5 (Congressional Structure)
- Contact target: Policy Director or Research Director
- Notes: Indivisible's value is primarily in distribution reach — if they share the research with their chapter network, it reaches a large organized base. Frame the referral/sharing CTA explicitly.

---

## 3. Sourcing Methodology

### Finding Decision-Maker Contacts

For each institution, use this sourcing sequence in order:

1. **Institution's public staff/leadership page** (fastest; usually accurate within 3–6 months). Find the staff directory and identify: Program Director, Senior Fellow in the relevant area, or Counsel leading active litigation in your target domain.

2. **LinkedIn** (for current role verification). Confirm the person is still in the stated role — staff move frequently in policy organizations. Cross-check title against the institution's website.

3. **Recent publications** (critical for personalization). Search the institution's website for publications from the past 6 months. Identify one publication you will reference in the personalization paragraph. Download or bookmark it — you need to have actually read the abstract or introduction before sending.

4. **Email format inference** (if direct email is not public). Most policy organizations use consistent email formats: `firstname@organization.org`, `firstname.lastname@organization.org`, or `flastname@organization.org`. The format can usually be inferred from one confirmed public email address at the organization (often listed on press releases or in CC fields in public documents).

5. **Professional network** (for warm introductions). Before sending cold outreach to a high-value institution (Batch 1 candidates), spend 10 minutes checking whether anyone in your professional network has a connection there. LinkedIn's "2nd degree" feature is useful. A warm introduction from a mutual connection converts at 3–5x the rate of cold outreach.

### Domain Relevance Scoring Calibration

Score each institution 1–5 on domain relevance:

- **5**: The institution has active litigation, ongoing research, or public publications directly in the domain being offered. The connection is specific, not general. (Examples: Just Security + Domain 28; Democracy Docket + Domain 37; Knight Institute + Domain 27.)
- **4**: The institution's mandate directly overlaps with the domain, and they have published on related topics in the past 12 months.
- **3**: The institution's mandate has clear overlap with the domain, but their recent publications do not specifically address the domain's content.
- **2**: The connection is plausible but requires creative framing that might not land.
- **1**: Tangential at best; do not include in initial outreach.

**Only send to institutions scored 3 or above**. Scores of 1–2 indicate the outreach will be perceived as generic — it will not convert.

---

## 4. Batch Assignment

Based on domain relevance scores and the existing `BATCH_1_CONTACT_VERIFICATION.md`, the recommended batch sequence is:

- **Batch 1** (Day 0, 5 contacts): Highest-relevance contacts — Just Security (#10), Quincy Institute (#13), Protect Democracy (#18), Brennan Center (#9 or #7), one law school clinic contact (Georgetown ICAP #3 or Columbia Knight #4).
- **Batch 2** (Day 7, 5–7 contacts): Democracy Docket (#19), Campaign Legal Center (#20), Yale Law (#1), Harvard Law (#2), Demand Progress (#23).
- **Batch 3** (Day 14, 5–7 contacts): ACLU (#21), Lawyers' Committee (#22), States United (#24), EPI (#14), Urban Institute (#15).
- **Batch 4** (Day 21, remaining): Remaining law school contacts and think tanks.
- **Batch 5** (Day 28): Cato, R Street, Indivisible — cross-ideological and large-network contacts whose value is primarily in reach rather than direct engagement.

---

*Companion documents: `phase-1-outreach-email-templates.md`, `phase-1-email-sequence-framework.md`, `BATCH_1_CONTACT_VERIFICATION.md`, `DISTRIBUTION_OUTREACH_CONTACTS.md`.*
