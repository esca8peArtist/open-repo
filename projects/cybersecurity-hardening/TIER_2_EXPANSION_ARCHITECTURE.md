---
title: "Tier 2 Expansion Architecture — Post-Phase-1 Decision Gates and Pilot Sequencing"
project: cybersecurity-hardening
created: 2026-05-13
status: production-ready
item: 27 — Tier 2 Expansion Architecture
depends-on:
  - TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md
  - TIER_2_PILOT_LAUNCH_READINESS.md
  - TIER1_OUTREACH_EXECUTION_PLAN.md
  - tier-2-sector-contact-lists.md
  - TIER_2_DISTRIBUTION_STRATEGY.md
decision-gates: 5
pilot-groups: A (3-5 orgs, May 28–June 15), B (5-10 orgs, August 1–September 1)
tier-3-decision: September 15, 2026
executor: Anya
---

# Tier 2 Expansion Architecture
## Post-Phase-1 Decision Gates and Phased Pilot Sequencing

**Lead finding**: The decision to expand to ~50 organizations is not made on June 1 — it is made on June 15 (Gate 2) based on Week 2 Phase 1 metrics, and confirmed or revised at three further gates through August. This document is the binding framework for those decisions. All thresholds, diagnostic procedures, and contingency pivots are pre-committed. Do not improvise during execution.

**Document purpose**: Enable confident, unambiguous go/no-go decisions at five checkpoints between May 28 and August 28, 2026. Every gate has a named decision owner, explicit threshold values, and a next action that does not require consulting the orchestrator. Print this before June 1. Read sections relevant to the current week during execution.

**Coordinates with**:
- `TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md` — Phase 1 KPI targets, measurement infrastructure, Day 7/14/21/28/42 thresholds
- `TIER_2_PILOT_LAUNCH_READINESS.md` — Group A organization selection (FPF, NLG, CLS), 8-week pilot plan
- `TIER1_OUTREACH_EXECUTION_PLAN.md` — Phase 1 wave cadence (5 contacts/wave, 5 waves, June 1–15)
- `tier-2-sector-contact-lists.md` — Verified contacts for Tier 2 organizations (digital rights, academic, researcher, journalist sectors)

---

## Section 1: Tier 2 Cohort Selection Framework

### 1A. Selection Criteria (Five Dimensions)

Every Tier 2 candidate is evaluated on five dimensions. Scores are 1–5 per dimension; maximum score is 25. Thresholds are: Fast Followers (20–25), Steady Majority (13–19), Late Adopters (8–12). Organizations scoring below 8 are not included in Tier 2.

**Dimension 1 — Adoption Likelihood (1–5)**
Predicts whether the organization will move from receipt to active use within 8 weeks.
- 5: Staff with explicit security mandate, prior technical security engagement, or known threat model alignment (e.g., active Palantir/ELITE campaigns)
- 4: Staff who engage substantively with technical documentation; organization working directly with at-risk populations
- 3: Policy-level engagement; likely to recommend but not implement directly
- 2: General digital rights interest; no documented operational security focus
- 1: Communications-facing, no technical implementation capacity

**Dimension 2 — Sector Diversity Value (1–5)**
Rewards geographic and sector gaps not already covered by Phase 1 (senators, think tanks, law schools) or Group A pilot (FPF = journalism, NLG = legal/activist, CLS = immigration legal aid).
- 5: Fills a sector with zero Phase 1 or Group A presence (labor unions, disabled advocacy, reproductive rights, faith communities)
- 4: Fills a geographic gap (non-coastal, non-urban) or sub-sector gap within a covered sector
- 3: Adds depth to a covered sector but in a materially different operational context
- 2: Adds another organization in an already-represented sector
- 1: Near-duplicate of an existing contact's sector, geography, and operational focus

**Dimension 3 — Media Amplification Potential (1–5)**
Assesses whether adoption will generate press coverage, academic citation, coalition referrals, or policy document citations.
- 5: National media relationships; prior press coverage of surveillance or civil liberties issues; op-ed capacity
- 4: State or regional media relationships; policy publication capacity (reports, briefs)
- 3: Sector publication presence (labor press, immigrant rights newsletters, disability advocacy outlets)
- 2: Social media reach; no institutional publication capacity
- 1: Internal-facing only; minimal external communication

**Dimension 4 — Geographic Gap Fill (1–5)**
Phase 1 contacts are concentrated in coastal metros (DC, New York, San Francisco, Boston). Tier 2 prioritizes underrepresented regions.
- 5: Deep South, Mountain West, or upper Midwest — states with large undocumented populations and minimal digital rights infrastructure (Texas, Arizona, Georgia, Michigan)
- 4: Mid-Atlantic or Great Plains non-metro; Pacific Northwest outside Seattle/Portland
- 3: Mid-size coastal city (Philadelphia, Baltimore, Denver, Atlanta)
- 2: Major coastal metro adjacent to Phase 1 contacts
- 1: Same metro as an existing Phase 1 or Group A contact

**Dimension 5 — Sector Leadership Status (1–5)**
High-status organizations confer credibility on the corpus when they adopt it; their adoption is a recruitment signal for downstream contacts.
- 5: Nationally recognized sector leader (e.g., AFL-CIO for labor, ACLU nationally for civil liberties, NARAL for reproductive rights)
- 4: Recognized regional leader or national mid-tier organization with name recognition in sector
- 3: Credible practitioner organization with sector respect but limited name recognition outside the field
- 2: Local chapter or affiliate of a national body
- 1: Emerging organization or startup without established reputation

---

### 1B. Pre-Screened Candidate Organizations (18 Total)

These organizations are pre-screened against the five dimensions. Scores are estimates based on publicly available information as of May 2026; verify against current organizational status before outreach. Contact details sourced from `tier-2-sector-contact-lists.md` and organizational websites.

**Scoring format**: [Adoption / Diversity / Amplification / Geography / Leadership] = Total

---

#### FAST FOLLOWERS (Score 20–25) — Top 5

**FF-01: Electronic Frontier Foundation (EFF)**
- Sector: Digital rights / civil liberties
- Location: San Francisco, CA (national reach)
- Primary contact: Saira Hussain, Senior Staff Attorney — saira@eff.org (confirmed, eff.org/about/staff, April 2026)
- Playbook match: Journalist Security Playbook + Immigration Surveillance Evasion Playbook
- Scores: Adoption 5 / Diversity 2 / Amplification 5 / Geography 2 / Leadership 5 = **19**
- Note: EFF's January 2026 ELITE/Medicaid report creates an active news peg. Hussain works specifically on ICE surveillance and license plate data sharing. Eva Galperin (Director of Cybersecurity) is secondary contact. EFF adoption = automatic credibility signal for all subsequent Tier 2 contacts. Upgraded to Fast Follower despite geographic score because leadership and amplification scores are maximum.
- Category: Fast Follower (score 19, upgraded for strategic value)

**FF-02: Surveillance Technology Oversight Project (S.T.O.P.)**
- Sector: Surveillance-specific civil liberties litigation
- Location: New York, NY
- Primary contact: Michelle Dahl, Executive Director — info@stopspying.org (confirmed, stopspying.org/our-team, April 2026)
- Secondary: Albert Fox Cahn, Founder-in-Residence
- Playbook match: Immigration Surveillance Evasion Playbook; Activist Organizing Playbook
- Scores: Adoption 5 / Diversity 3 / Amplification 4 / Geography 2 / Leadership 5 = **19**
- Note: STOP is running the active #PowerDownSurveillance campaign (2026) and won class certification against Thomson Reuters for selling personal data to ICE. Albert Fox Cahn's 2026 book *Move Slow and Upgrade* (Cambridge University Press) positions STOP at the credibility intersection of practitioner and academic. Cahn's Thomson Reuters case directly parallels ELITE's commercial data pipeline.
- Category: Fast Follower

**FF-03: Just Futures Law**
- Sector: Immigration + surveillance litigation
- Location: National (staff distributed)
- Primary contact: Paromita Shah, Founding Executive Director — justfutureslaw.org/contact (form-based; no direct email publicly listed)
- Playbook match: Immigration Surveillance Evasion Playbook; Immigration Attorney Implementation Guide
- Scores: Adoption 5 / Diversity 4 / Amplification 4 / Geography 3 / Leadership 4 = **20**
- Note: Just Futures Law won EFF's 2025 Award for Leading Immigration and Surveillance Litigation. They filed a FOIA case against DHS and USCIS in March 2026 seeking documents on immigration surveillance — they are actively litigating in the exact space the corpus documents. The corpus's FOIA-sourced documentation is directly relevant to their active case development. No geographic concentration bias; national distributed staff.
- Category: Fast Follower

**FF-04: National Immigration Law Center (NILC)**
- Sector: Immigration legal policy
- Location: Los Angeles, CA + Washington, DC
- Primary contact: Marielena Hincapié, Executive Director (verify current — leadership transition history noted); general: nilc.org/contact
- Secondary: Policy Department (policy@nilc.org)
- Playbook match: Immigration Surveillance Evasion Playbook; Undocumented Immigrant Implementation Guide
- Scores: Adoption 4 / Diversity 3 / Amplification 5 / Geography 3 / Leadership 5 = **20**
- Note: NILC is a national policy and litigation organization serving low-income immigrants. They publish widely-read policy briefs, issue public comments, and have strong media relationships. A NILC policy brief citing the corpus would be read by state immigration coalitions, congressional staff, and legal aid networks simultaneously. Their geographic bicoastal presence is a limitation but their downstream amplification to state networks compensates.
- Category: Fast Follower

**FF-05: ACLU Speech, Privacy, and Technology Project**
- Sector: Civil liberties / surveillance law
- Location: Washington, DC (national reach)
- Primary contact: Ashley Gorski, Senior Staff Attorney — aclu.org/bio/ashley-gorski (verify email through ACLU press office or website)
- Playbook match: Journalist Security Playbook; Activist Organizing Playbook; Immigration Surveillance Evasion Playbook
- Scores: Adoption 4 / Diversity 2 / Amplification 5 / Geography 2 / Leadership 5 = **18**
- Note: The ACLU's Speech, Privacy, and Technology Project actively litigates surveillance cases and publishes extensively. Gorski works specifically on government surveillance. ACLU adoption creates a downstream signal for ACLU state affiliates (52 affiliates across 50 states + Puerto Rico + DC) — single adoption decision has a 52-org amplification potential. Score upgraded to Fast Follower for this multiplier effect.
- Category: Fast Follower (score 18, upgraded for multiplier)

---

#### STEADY MAJORITY (Score 13–19) — Top 10

**SM-01: Service Employees International Union (SEIU) — Strategic Campaigns**
- Sector: Labor / union organizing
- Location: Washington, DC (national reach, chapters in all 50 states)
- Primary contact: SEIU Strategic Campaigns Department — seiu.org/contact (route to strategic campaigns); verify named contact before outreach
- Playbook match: Activist Organizing Playbook; Device Hardening Guide
- Scores: Adoption 3 / Diversity 5 / Amplification 4 / Geography 4 / Leadership 5 = **21**
- Note: SEIU represents 2 million workers in healthcare, public service, and property services. Their organizing campaigns involve extensive employer surveillance (workplace monitoring, location tracking, social media scraping). The Activist Organizing Playbook's device hygiene and ALPR documentation are directly relevant to ongoing organizing drives. Steady Majority classification is due to adoption uncertainty — union staff leadership varies significantly in technical engagement; approach through strategic campaigns, not communications. If approach reaches the right function (organizer training coordinator), adoption probability rises substantially.
- Category: Steady Majority (technical engagement variable)

**SM-02: United Auto Workers (UAW) — Organizing Department**
- Sector: Labor / union organizing
- Location: Detroit, MI (geographic gap fill: Midwest)
- Primary contact: UAW Organizing Department — uaw.org/contact (verify named contact before outreach; approach organizing director, not communications)
- Playbook match: Activist Organizing Playbook; Device Hardening Guide
- Scores: Adoption 3 / Diversity 5 / Amplification 3 / Geography 5 / Leadership 4 = **20**
- Note: UAW's ongoing expansion campaigns (2024–2026 wins at Volkswagen, Daimler, other southern plants) involve active employer surveillance countermeasure needs. The Midwest geographic gap — Detroit is the largest Tier 2 gap city — is a strong diversity score driver. UAW media reach is labor-sector-specific but strong within that sector. Same contact routing caveat as SEIU: must reach organizer training function, not external affairs.
- Category: Steady Majority (contact routing critical)

**SM-03: Disability Rights Advocates (DRA)**
- Sector: Disability rights litigation
- Location: Berkeley, CA + New York, NY
- Primary contact: General inquiry — info@dralegal.org (dralegal.org); verify litigation staff contact before outreach
- Playbook match: High-Risk Populations guide; Device Hardening Guide
- Scores: Adoption 3 / Diversity 5 / Amplification 3 / Geography 3 / Leadership 4 = **18**
- Note: DRA is the leading disability rights litigation firm. Disabled people — particularly those who are also immigrants, undocumented, or involved in advocacy — face compounded surveillance risks. The corpus does not currently include a dedicated disabled-population variant; this is a gap the DRA engagement could help fill. DRA's adoption would validate a new sector expansion and generate feedback for a disabled advocacy playbook variant.
- Category: Steady Majority (sector gap — corpus needs customization before outreach)

**SM-04: National Network to End Domestic Violence (NNEDV) — Safety Net Project**
- Sector: Domestic violence / technology safety
- Location: Washington, DC
- Primary contact: Cindy Southworth, Executive Vice President (Safety Net Project founder) or current Safety Net staff — nnedv.org/content/safety-net (verify current contact)
- Playbook match: DV Survivor Safety Playbook (Phase 2 version ready)
- Scores: Adoption 4 / Diversity 4 / Amplification 4 / Geography 2 / Leadership 5 = **19**
- Note: NNEDV's Safety Net Project is the primary technical resource for DV advocates across the US — they train advocates on technology safety for survivors. The DV Survivor Safety Playbook maps directly to their existing training curriculum. NNEDV adoption means the playbook enters the national DV advocate training infrastructure, reaching thousands of frontline advocates. This is the highest-multiplier DV sector contact available.
- Category: Steady Majority

**SM-05: Mijente**
- Sector: Latinx political organization / immigration advocacy
- Location: National (headquarters in Phoenix, AZ — geographic gap fill: Southwest)
- Primary contact: Marisa Franco, Executive Director — info@mijente.net (mijente.net); verify current contact
- Playbook match: Immigration Surveillance Evasion Playbook; Undocumented Immigrant Implementation Guide
- Scores: Adoption 4 / Diversity 5 / Amplification 3 / Geography 5 / Leadership 3 = **20**
- Note: Mijente's #NoTechForICE campaign directly opposes Palantir's immigration enforcement contracts — the corpus's ELITE documentation extends that campaign with primary-source technical detail. Mijente has a mobile-first, community-organizing model; playbook customization for phone-centric security is needed before outreach. Phoenix geography fills the Southwest gap (Arizona has one of the highest undocumented immigrant populations by proportion). Spanish-language playbook availability is a strong asset here.
- Category: Steady Majority (playbook customization needed)

**SM-06: Color of Change**
- Sector: Digital racial justice
- Location: Oakland, CA + Washington, DC
- Primary contact: Rashad Robinson, President — colorofchange.org/contact (verify named staff contact for technology/surveillance policy)
- Playbook match: Activist Organizing Playbook; Immigration Surveillance Evasion Playbook
- Scores: Adoption 3 / Diversity 4 / Amplification 5 / Geography 3 / Leadership 4 = **19**
- Note: Color of Change runs active campaigns against facial recognition and predictive policing, with named campaigns against Amazon Rekognition and Clearview AI (2020–2026). Their 7-million-member base gives them the largest individual reach of any Tier 2 candidate. Adoption likelihood is moderate because their campaigns are policy-facing, not practitioner-facing; implementation at the individual level depends on their campaign framing.
- Category: Steady Majority

**SM-07: Planned Parenthood Federation of America — Digital Security**
- Sector: Reproductive rights / healthcare
- Location: National (New York, NY headquarters)
- Primary contact: Planned Parenthood security or technology policy team — plannedparenthood.org/about-us/contact-us (routing needed; verify specific department contact)
- Playbook match: Financial Resistance Playbook; Device Hardening Guide; Identity Recovery and Breach Response Guide
- Scores: Adoption 3 / Diversity 5 / Amplification 4 / Geography 2 / Leadership 5 = **19**
- Note: Post-Dobbs enforcement has created active surveillance threats against reproductive healthcare providers and patients — location data from healthcare app visits is a documented enforcement vector. The financial resistance playbook (protecting payment privacy for healthcare) and device hardening are directly relevant. Planned Parenthood's existing digital security protocols make them a sophisticated audience. Sector diversity score is maximum — reproductive rights is unrepresented in Phase 1 and Group A.
- Category: Steady Majority (routing to digital security function is critical; avoid communications/press)

**SM-08: Brennan Center for Justice — Democracy Program / Liberty & National Security**
- Sector: Policy think tank / civil liberties law
- Location: New York, NY
- Primary contact: Michael Price, Senior Counsel, Liberty & National Security Program — brennancenter.org/experts/michael-price (verify email through Brennan Center staff directory)
- Secondary: Democracy Program staff on surveillance policy
- Playbook match: Policy briefing materials; Journalist Security Playbook
- Scores: Adoption 3 / Diversity 2 / Amplification 5 / Geography 2 / Leadership 5 = **17**
- Note: Brennan Center published *America's Surveillance State* and has active Liberty & National Security work on surveillance. A Brennan Center policy brief citing the corpus is the single highest-impact academic amplification event available. The corpus's FOIA-sourced technical detail fills a documentation gap in their policy work. Adoption likelihood is moderate — they generate analysis, not implementation; the corpus is most useful to them as a citation foundation.
- Category: Steady Majority

**SM-09: National Council of La Raza / UnidosUS**
- Sector: Latinx civil rights / immigration advocacy
- Location: Washington, DC + Phoenix, AZ
- Primary contact: Janet Murguía, President and CEO — unidosus.org/about-us/contact (verify department routing for policy/technology)
- Playbook match: Immigration Surveillance Evasion Playbook; Undocumented Immigrant Implementation Guide
- Scores: Adoption 3 / Diversity 4 / Amplification 4 / Geography 4 / Leadership 5 = **20**
- Note: UnidosUS has a 300+ affiliate network of community-based organizations serving Latino communities across the country. Single adoption decision at the national level routes the corpus through their affiliate network. Geographic reach fills Southwest and South gaps. Adoption at the national level is policy-facing; implementation at the affiliate level requires the Spanish-language playbook variant.
- Category: Steady Majority (Spanish-language variant required)

**SM-10: Georgetown Center on Privacy and Technology**
- Sector: Academic / privacy policy research
- Location: Washington, DC
- Primary contact: Laura Moy, Executive Director — contact@law.georgetown.edu (Georgetown Law routing; verify named contact)
- Playbook match: Policy briefing; Immigration Surveillance Evasion Playbook
- Scores: Adoption 3 / Diversity 3 / Amplification 4 / Geography 2 / Leadership 5 = **17**
- Note: Georgetown CPT published *American Dragnet* (2022), the closest existing institutional analog to the corpus's surveillance documentation work. The corpus extends their documentation with countermeasures and 2025–2026 ELITE system updates. An academic partnership with Georgetown CPT validates the corpus methodologically. Adoption as a citation source or research partner (not just a recipient) is the target outcome.
- Category: Steady Majority

---

#### LATE ADOPTERS (Score 8–12) — Reserve 5

Late Adopters require the strongest available case study evidence before engagement begins. Do not contact this tier until Group A adoption is confirmed (>60%) and at least one external case study (security incident + resolution, or policy citation) is available.

**LA-01: National Domestic Workers Alliance (NDWA)**
- Sector: Labor / domestic worker rights
- Location: National (Atlanta, GA headquarters — geographic gap fill: South)
- Scores: Adoption 2 / Diversity 5 / Amplification 3 / Geography 5 / Leadership 3 = **18**
- Hold reason: Domestic workers face surveillance in private residences — threat model customization needed before outreach. Current playbooks do not address home-workplace surveillance dynamics. Score is borderline Steady Majority but hold until a domestic worker surveillance section is added to the corpus.

**LA-02: UndocuBlack Network**
- Sector: Black undocumented immigrant community advocacy
- Location: National (Miami, FL — geographic gap fill: South)
- Scores: Adoption 2 / Diversity 5 / Amplification 2 / Geography 5 / Leadership 2 = **16**
- Hold reason: Emerging organization (founded 2016); strong mission alignment but limited organizational capacity for implementation without support. Needs case study evidence of corpus utility for Black undocumented communities specifically.

**LA-03: Faith in Action (formerly PICO National Network)**
- Sector: Faith-based community organizing
- Location: National (Oakland, CA)
- Scores: Adoption 2 / Diversity 5 / Amplification 3 / Geography 2 / Leadership 3 = **15**
- Hold reason: Faith communities are an important sector gap but implementation requires significant playbook framing adaptation. Technical language needs simplification for non-technical faith community audiences. Hold until a faith-community playbook variant exists.

**LA-04: National Association of Criminal Defense Lawyers (NACDL) — Digital Evidence Committee**
- Sector: Criminal defense / legal profession
- Location: Washington, DC
- Scores: Adoption 3 / Diversity 3 / Amplification 3 / Geography 2 / Leadership 4 = **15**
- Hold reason: NACDL's Digital Evidence Committee is the right function but engagement requires a lawyer-specific playbook framing (attorney-client privilege in digital contexts, law office device hygiene, criminal client surveillance risks). Hold until corpus includes a legal profession variant.

**LA-05: Transgender Law Center**
- Sector: Trans rights / civil rights litigation
- Location: Oakland, CA
- Scores: Adoption 2 / Diversity 5 / Amplification 3 / Geography 2 / Leadership 4 = **16**
- Hold reason: Trans individuals face compounded surveillance risks (gender-affirming care tracking, legal name change exposure, family court surveillance). Corpus needs a trans-population threat model section before outreach. This is a documented gap. Hold until corpus extends to include trans-specific threat model and countermeasures. When ready, Transgender Law Center is a high-value fast follower.

---

### 1C. Pre-Screen Summary Table

| ID | Organization | Sector | Score | Category | Hold Reason |
|----|-------------|--------|-------|----------|-------------|
| FF-01 | EFF | Digital rights | 19* | Fast Follower | None |
| FF-02 | S.T.O.P. | Surveillance litigation | 19 | Fast Follower | None |
| FF-03 | Just Futures Law | Immigration litigation | 20 | Fast Follower | None |
| FF-04 | NILC | Immigration policy | 20 | Fast Follower | None |
| FF-05 | ACLU SPT Project | Civil liberties | 18* | Fast Follower | None |
| SM-01 | SEIU Strategic | Labor | 21 | Steady Majority | Routing critical |
| SM-02 | UAW Organizing | Labor | 20 | Steady Majority | Routing critical |
| SM-03 | Disability Rights Advocates | Disability | 18 | Steady Majority | Corpus gap |
| SM-04 | NNEDV Safety Net | DV advocacy | 19 | Steady Majority | None |
| SM-05 | Mijente | Latinx immigration | 20 | Steady Majority | Customization needed |
| SM-06 | Color of Change | Racial justice | 19 | Steady Majority | None |
| SM-07 | Planned Parenthood | Reproductive rights | 19 | Steady Majority | Routing critical |
| SM-08 | Brennan Center | Policy think tank | 17 | Steady Majority | None |
| SM-09 | UnidosUS | Latinx civil rights | 20 | Steady Majority | Spanish variant required |
| SM-10 | Georgetown CPT | Academic | 17 | Steady Majority | None |
| LA-01 | NDWA | Domestic labor | 18 | Late Adopter | Corpus gap |
| LA-02 | UndocuBlack | Black undocumented | 16 | Late Adopter | Corpus gap |
| LA-03 | Faith in Action | Faith organizing | 15 | Late Adopter | Framing gap |
| LA-04 | NACDL Digital Evidence | Criminal defense | 15 | Late Adopter | Legal variant needed |
| LA-05 | Transgender Law Center | Trans rights | 16 | Late Adopter | Corpus gap |

*Scores marked with asterisk are upgraded from raw score for strategic value (see individual notes).

---

## Section 2: Phased Pilot Architecture

### 2A. Three-Tier Structure Overview

```
Phase 1 (Tier 1): June 1–15
│  25 high-leverage policy contacts (senators, think tanks, law schools)
│  5 contacts/wave × 5 waves
│  Success gate: June 15 (Week 2 metrics)
│
├── Pilot Group A: May 28–June 15 (concurrent with Phase 1)
│   3–5 organizations (FPF, NLG, CLS — from TIER_2_PILOT_LAUNCH_READINESS.md)
│   Purpose: Rapid feedback, messaging refinements, playbook customization
│   Success gate: July 1 (Gate 3)
│
├── Pilot Group B: August 1–September 1 (post-Phase-1 evaluation)
│   5–10 organizations from Steady Majority cohort
│   Dependent on Phase 1 KPI achievement and Group A success
│   Success gate: August 28 (Gate 5)
│
└── Tier 3 Decision: September 15
    Full 50-org expansion based on combined pilot evidence
    Three outcomes: GO / CONDITIONAL / INSUFFICIENT
```

---

### 2B. Pilot Group A (May 28 – June 15)

**Organizations**: FPF, NLG Mass Defense, Community Legal Services Philadelphia — as specified in `TIER_2_PILOT_LAUNCH_READINESS.md`. These three are pre-vetted, contacts verified, and playbooks matched.

**Purpose**: Run concurrent with Phase 1 to generate rapid feedback on:
1. Messaging refinements (what framing converts for practitioner audiences)
2. Material gaps (what sections are missing, unclear, or require customization)
3. Playbook customization needs by sector (journalism, legal, immigration legal aid)

**Launch condition**: Phase 1 Week 1 metrics available by June 7 (Gate 1). If Gate 1 shows >30% click-through, Group A launches as scheduled. If Gate 1 shows <30%, Group A launch deferred pending Phase 1 diagnosis. (Do not run Group A in parallel with a failing Phase 1 — diagnostic bandwidth is limited.)

**Outreach sequence** (from TIER_2_PILOT_LAUNCH_READINESS.md):
- May 28: FPF outreach (security@freedom.press)
- May 29: NLG Mass Defense outreach (massdef@nlg.org)
- May 30: Community Legal Services Philadelphia outreach (verify current contact)

**Success gate (July 1 — Gate 3)**:
- Go: >60% adoption (2+ of 3 orgs show active engagement — scheduled session or substantive feedback)
- Caution: 40–59% adoption (1–2 orgs engaged) — proceed to Group B but flag for messaging refinement
- No-go: <40% adoption (fewer than 1 engaged org) — diagnostic pause; hold Group B

**4th candidate (if one Group A org declines)**: Access Now Digital Security Helpline (help@accessnow.org — Mohammed Al-Maskati, Director). Access Now operates with the same practitioner orientation as FPF and CLS and maps to both the journalist and immigration population playbooks.

---

### 2C. Pilot Group B (August 1 – September 1)

**Organizations**: 5–10 from the Steady Majority cohort, selected based on Group A feedback about what messaging framing and playbook content worked. Prioritize organizations where Group A feedback revealed a transferable lesson.

**Recommended Group B sequence** (subject to Group A feedback):
1. NNEDV Safety Net Project (DV sector — corpus gap confirmed or addressed during July)
2. Mijente (immigration + Latinx sector — Spanish variant status check)
3. EFF (if not already engaged through Phase 1 as Tier 1 contact)
4. S.T.O.P. (surveillance litigation — highest adoption likelihood among pre-screened orgs)
5. Just Futures Law (immigration litigation — FOIA case active)
6. SEIU Strategic Campaigns (labor sector — if Activist Organizing Playbook was refined in Group A)
7. Color of Change (racial justice amplification)
8. Brennan Center Liberty & National Security (policy citation multiplier)
9. Georgetown Center on Privacy and Technology (academic citation)
10. NILC (immigration policy, national amplification)

**Launch condition**: Phase 1 adoption >40% (Gate 2, June 15) AND Group A adoption >40% (Gate 3, July 1). If either condition is unmet, Group B is delayed pending diagnostic.

**Key distinction from Group A**: Group B is informed by Group A feedback. Before sending Group B invitations, complete the Group A feedback synthesis (Weeks 5–6, July 1–28) and incorporate at minimum 2 messaging refinements identified by Group A organizations.

**Success gate (August 28 — Gate 5)**:
- Go: >50% adoption among Group B orgs (5 of 10) — proceed to Tier 3 decision
- Caution: 35–49% adoption — proceed with Tier 3 CONDITIONAL track (25-org subset)
- No-go: <35% adoption — halt; pivot to intensify Group A/B before Tier 3

---

### 2D. Tier 3 Readiness Gate (September 15)

**Decision**: Full 50-org expansion, 25-org conditional expansion, or focused intensification.

**Decision criteria**:
- Group A adoption >60% AND Group B adoption >50% AND any sector shows policy uptake → GO (full 50-org expansion)
- Mixed results meeting only some criteria → CONDITIONAL (25-org Tier 3 subset, pause remainder)
- Both pilots below thresholds → INSUFFICIENT DATA (pause; run additional diagnostic quarter)

Full scoring matrix in Section 7.

---

## Section 3: 12-Week Tier 2 Pilot Timeline

All dates anchored to Phase 1 Day 1 = June 1, 2026. Week 1 = June 1–7. Week 2 = June 8–14, etc.

### Weeks 1–4 (June 1 – June 28): Parallel Phase 1 + Group A Delivery

**June 1–7 (Week 1)**
- Phase 1: Wave 1 sends (5 contacts). Monitor Bitly daily.
- Group A: Deliver FPF, NLG, CLS invitations (May 28–30 — pre-Week-1, already launched)
- Group A: Monitor initial responses; schedule any sessions requested within 5 business days
- Resource: 3 hours/day Phase 1 + 1 hour/day Group A = 4 hours/day

**[GATE 1 — June 7 — Decision Owner: Anya]**
- Metric: Phase 1 Bitly click rate by end of Week 1
- Check: Tab 5 of tracking spreadsheet, "Week 1" row, "Bitly Clicks" column
- GO (>30% click): Proceed with Phase 1 Wave 2 and Group A as scheduled
- CAUTION (20–30% click): Proceed but run subject line diagnostic before Wave 2 (see Section 5, Scenario A Step 1)
- STOP (<20% click): Diagnose Phase 1 email deliverability. Hold Group A follow-ups (do not expand scope while Phase 1 is failing). See Contingency Trigger 1 (Section 6).
- Action if STOP: Do not send Wave 2 until Gate 1 diagnosis is complete. Maximum 48-hour diagnostic window.

**June 8–14 (Week 2)**
- Phase 1: Wave 2 sends (5 contacts). Follow up with Wave 1 non-responders.
- Group A: First responses expected from FPF, NLG, CLS (Days 7–10 post-send). Log in pilot tracking tab.
- Group A: Schedule sessions for any positive responders.
- Resource: 4 hours/day (3 Phase 1 + 1 Group A)

**[GATE 2 — June 15 — Decision Owner: Anya]**
- Metric: Phase 1 Week 2 overall metrics (click rate cumulative, meetings scheduled, early adoption signals)
- Check: Tab 5 "Week 2" row + Tab 3 meeting count
- GO (>40% click, ≥3 meetings scheduled, any adoption signal): Approve Group B timeline. Start Group B prep immediately (Weeks 5–8).
- CAUTION (30–40% click, 1–2 meetings): Proceed with Phase 1. Group B timeline approved but contingent on Week 4 review.
- STOP (<30% click, 0 meetings): Pause Tier 2 preparation. Redirect resource to Phase 1 diagnostic. See Contingency Trigger 2 (Section 6).
- Action if STOP: Defer Group B indefinitely. Focus all capacity on Phase 1 recovery. Group A can continue (it is smaller scope) but no new Tier 2 prep.

**June 15–28 (Weeks 3–4)**
- Phase 1: Waves 3–5 (final 15 contacts). Complete all sends by June 28.
- Group A: Deliver sessions for positive responders (Week 3). Collect initial feedback (Week 4).
- Group A: Send feedback survey within 24 hours of each session.
- Milestone: By June 28, all 25 Phase 1 contacts sent. All Group A sessions scheduled or attempted.
- Resource: 4 hours/day

---

### Weeks 5–8 (July 1 – July 28): Group A Feedback Synthesis + Group B Preparation

**[GATE 3 — July 1 — Decision Owner: Anya]**
- Metric: Group A adoption rate
- Check: Pilot tracking tab — count orgs with substantive engagement (session held OR feedback survey completed OR specific feedback received)
- GO (>60% adoption, i.e., 2+ of 3 orgs): Proceed to Group B preparation. Begin customizing materials.
- CAUTION (40–59%, i.e., exactly 1 of 3 orgs): Proceed to Group B preparation but flag messaging for revision. Run 1-on-1 diagnostic with the non-responding orgs before Group B sends.
- STOP (<40%, i.e., 0 orgs): Escalate to diagnostic. Hold Group B until resolved. See Contingency Trigger 3 (Section 6).
- Action if STOP: Interview available Group A contacts (even non-adopters if they responded) about barriers. Synthesize before deciding whether Group B proceeds.

**July 1–14 (Weeks 5–6): Group A Feedback Synthesis**
- Analyze Group A adoption patterns: Which sections generated the most substantive feedback?
- Document messaging refinements: Subject lines that worked, framing that converted, sections that generated confusion or pushback.
- Document playbook corrections: Any factual gap or implementation error identified by practitioner review.
- Identify at least 2 specific messaging refinements to incorporate before Group B sends.
- Milestone: Group A feedback synthesis document (internal, 1-2 pages, bullet format) by July 14.

**July 15–28 (Weeks 7–8): Group B Material Customization**
- Select Group B organizations (8–10 from Steady Majority list) based on Group A sector feedback.
- Customize outreach messages for each Group B org — lead with the sector-specific hook, not the generic corpus frame.
- Incorporate Group A messaging refinements into Group B templates.
- Verify Group B contact details before outreach (organization websites, LinkedIn, verify names are current).
- Draft Group B pilot invitations (under 200 words each; specific ask per org).
- Milestone: Group B invitations drafted and contacts verified by July 28.
- Resource: 2 hours/day

---

### Weeks 9–12 (August 1 – August 28): Group B Delivery + Tier 3 Decision Preparation

**August 1–7 (Week 9)**
- Group B: Send outreach to first 4–5 organizations (Monday–Friday, 1 per day)
- Phase 1: Week 6 adoption signal follow-ups still in process (check Tab 4 adoption signals)
- Resource: 3 hours/day

**August 8–14 (Week 10)**
- Group B: Send remaining 4–5 organizations (Monday–Friday, 1 per day)
- Group B: Monitor initial responses from Week 9 sends. Schedule sessions promptly.
- Resource: 3 hours/day

**[GATE 4 — August 15 — Decision Owner: Anya]**
- Metric: Group B mid-point adoption rate (engagement from first 5–7 sends)
- Check: Pilot tracking tab, Group B section. Count orgs with any substantive engagement (reply with question, session scheduled, or feedback received).
- TRACKING (>35% of first-wave Group B sends): On track. Continue Group B outreach.
- WARNING (20–35%): Flag for escalation. Intensify follow-up for non-responders. Consider whether contact routing is correct (are messages reaching the right function?).
- ESCALATE (<20%): See Contingency Trigger 4 (Section 6). May halt Tier 3 expansion planning if pattern persists.
- Action if WARNING: Send personalized follow-ups to non-responding Group B orgs. Use sector-specific hook different from initial send.

**August 15–28 (Weeks 11–12)**
- Group B: Complete all engagement sessions. Collect feedback surveys within 24 hours of each session.
- Prepare Tier 3 readiness assessment: compile all Phase 1, Group A, and Group B metrics into Tier 3 scoring matrix (Section 7).
- Draft Tier 3 organizational shortlist (25-org or 50-org list based on scoring outcome).
- Resource: 3 hours/day

**[GATE 5 — August 28 — Decision Owner: Anya]**
- Metric: Combined Phase 1 + Group A + Group B scoring matrix total (Section 7)
- Check: Tier 3 scoring matrix, calculate weighted total.
- GO (>55% weighted): Proceed to full 50-org Tier 3 expansion. Begin outreach September 15.
- CONDITIONAL (40–55%): Proceed with 25-org Tier 3 subset. Focus on sectors showing highest adoption (identified by Group A + B data).
- INSUFFICIENT (<40%): Pause Tier 3. Convene diagnostic session with 3 Group A/B adopters to identify blockers.
- Decision communicated to user: August 28, with the scoring matrix as supporting evidence.

---

### 12-Week Gantt Summary

```
WEEK | DATE RANGE    | PHASE 1      | GROUP A         | GROUP B      | GATES
-----|---------------|--------------|-----------------|--------------|------
 1   | June  1- 7   | Wave 1 (5)   | Sessions + fbk  | —            | Gate 1 (June 7)
 2   | June  8-14   | Wave 2 (5)   | Non-resp f/u    | —            | Gate 2 (June 15)
 3   | June 15-21   | Wave 3 (5)   | Synthesis prep  | —            | —
 4   | June 22-28   | Waves 4-5(10)| Feedback survey | —            | —
 5   | July  1- 7   | Follow-ups   | Synthesis       | —            | Gate 3 (July 1)
 6   | July  8-14   | Week 6 f/u   | Synthesis done  | —            | —
 7   | July 15-21   | Monitoring   | —               | Customization| —
 8   | July 22-28   | Monitoring   | —               | Verify+draft | —
 9   | Aug   1- 7   | —            | —               | Wave 1 (4-5) | —
10   | Aug   8-14   | —            | —               | Wave 2 (4-5) | Gate 4 (Aug 15)
11   | Aug  15-21   | —            | —               | Sessions     | —
12   | Aug  22-28   | —            | —               | Fbk+scoring  | Gate 5 (Aug 28)
```

---

## Section 4: Success Metrics Per Phase

### 4A. Phase 1 (Tier 1) — June 1–15

Source metrics: `TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md`, Section 1 and Section 6.

| Metric | Target | Go Threshold | No-Go Threshold | Data Source |
|--------|--------|--------------|-----------------|-------------|
| Bitly click rate (Day 14) | 45% | >40% | <30% | Bitly dashboard |
| Meeting acceptance rate (Day 42) | 60% | >50% | <40% | Calendar bookings |
| Adoption signals (Week 6) | 10% (2–3 orgs) | >8% | <5% | Tab 4 tracking sheet |
| Bounce rate | <5% | <5% | >8% | Gmail bounces |
| Reply quality (Stage 1+) | 60% of replies | >50% | <40% | Tab 2 tracking sheet |

**Critical distinction**: The Day 14 meeting acceptance number is the primary gate for Tier 2 authorization. Per the measurement framework: "Design every metric, every follow-up, and every escalation around [the scheduled 30-minute call]." A 40%+ click rate with zero meetings is a failure signal, not a success signal.

---

### 4B. Pilot Group A — May 28–June 28 (assessed July 1)

| Metric | Target | Go Threshold | No-Go Threshold | Data Source |
|--------|--------|--------------|-----------------|-------------|
| Adoption rate | 60% (2 of 3 orgs) | >55% | <45% | Pilot tracking tab |
| Engagement rate | 40% (session or feedback) | >35% | <25% | Pilot tracking tab |
| Substantive feedback items | 3+ total | 2+ | 0–1 | Feedback survey responses |
| Messaging refinements documented | 2+ | 2 | 0–1 | Internal synthesis doc |
| Downstream policy ask identified | 1+ | 1 | 0 | Meeting notes |

**What "adoption" means for Group A**: An organization has adopted if they: (a) completed a session AND submitted feedback survey, OR (b) confirmed they are implementing a playbook section with named staff member responsible, OR (c) requested additional customization for their context. Generic "thank you, we'll review" does not count.

---

### 4C. Pilot Group B — August 1–September 1 (assessed August 28)

| Metric | Target | Go Threshold | No-Go Threshold | Data Source |
|--------|--------|--------------|-----------------|-------------|
| Adoption rate | 50% of Group B orgs | >45% | <35% | Pilot tracking tab |
| Policy uptake signal | 1+ | 1 | 0 | Meeting notes + email threads |
| Engagement rate | 40% | >35% | <25% | Pilot tracking tab |
| Messaging refinements applied | 2+ from Group A | Confirmed | Not applied | Outreach templates |

**Lower Group B threshold rationale**: Group B benefits from Group A refinements. If Group B underperforms Group A significantly (e.g., Group A = 70%, Group B = 30%), the issue is contact selection or routing, not the materials. That diagnostic distinction is important for the Tier 3 decision.

---

### 4D. Tier 3 (Full Expansion) Gate — September 15

| Criterion | Required for GO | Weight |
|-----------|----------------|--------|
| Phase 1 adoption ≥ 40% | Required | 40% |
| Group A adoption ≥ 60% | Required | 30% |
| Group B adoption ≥ 45% | Required | 20% |
| Policy uptake in any sector | Required | 10% |

**Decision**:
- All criteria met: GO — expand to full 50 orgs
- 3 of 4 criteria met: CONDITIONAL — expand to 25-org subset, prioritize sectors showing uptake
- 2 or fewer criteria met: INSUFFICIENT — pause, run additional diagnostic quarter before expanding

---

## Section 5: Risk Escalation Playbook

### Scenario A: Phase 1 Underperforms (>30% but <40% Adoption)

**When this applies**: Gate 2 (June 15) shows click rate 30–40%, meetings 1–2, no adoption signals yet.

**Do not skip the diagnostic sequence. Take no corrective action before completing Steps 1–3.**

**Step 1 — Click-through analysis by sector** (30 minutes)
- Open Bitly dashboard. Note click times. Do any clicks cluster by time of day (e.g., all during business hours = office-based readers)?
- Open Tab 2 tracking sheet. Sort by sector (Senate / Think-Tank / Law-School). Which sector has the lowest click rate?
- If sector-specific low: the subject line may not be resonating with that sector. Test a sector-specific variant on the next wave sends for that sector before sending a uniform follow-up.

**Step 2 — Meeting no-show rate** (15 minutes)
- Check Tab 3. Of scheduled meetings, how many were completed vs. cancelled/no-showed?
- If no-show rate >25%: the scheduling process is not qualifying intent. Before the next scheduled call, send a pre-call question (from TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md Section 1B): "To make the call most useful — are you focused primarily on legislative oversight implications, civil liberties litigation angles, or operational security for your team?" A contact who answers this question is genuinely engaged.

**Step 3 — Feedback quality assessment** (20 minutes)
- Review all Stage 0 vs. Stage 1+ replies in Tab 2. Is feedback generic ("looks interesting") or specific ("the Part 0 data broker sequence would be useful for our intake forms")?
- Generic-only feedback hypothesis: playbook framing is too abstract for this cohort. Test a more concrete opening: instead of describing the corpus, describe a specific use case for that organization's work.

**Lever 1 — Sector-specific intensification** (if issue is sector-specific)
- Identify the underperforming sector. Write custom follow-up emails for each non-responding organization in that sector with a different hook (see TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md Section 5, Scenario 4 for hook variants).
- Do not send the same email twice. Each follow-up must have a different opening line and subject line.

**Lever 2 — Meeting conversion strengthening** (if issue is low meeting acceptance)
- Replace all remaining "happy to discuss" CTAs with specific offers: "I can walk through the ELITE system documentation in 20 minutes — are you free [date] at [time]?"
- Add Calendly link to all follow-ups to reduce scheduling friction.

**Lever 3 — Introductory framing simplification** (if feedback quality is generic)
- The playbook may be too advanced for this cohort as framed. Add a one-paragraph "why this matters specifically for your work" introduction to each follow-up, personalized per organization.

**Escalation threshold**: If all three levers are applied and adoption is still <35% by Day 28, pause Tier 2 and run a diagnostic session with 3 Phase 1 early adopters (the ones who did engage). Ask: "What made this corpus valuable to you? What would have made it less useful?" Use their answers to reframe for the remaining non-responding contacts.

---

### Scenario B: Group A Adoption High (>70%) but Engagement Low (<25%)

**When this applies**: Group A orgs downloaded or reviewed the playbook but did not complete sessions, submit feedback, or implement any section.

**Hypothesis**: Organizations want the material but face implementation barriers (time, technical capacity, unclear first step).

**Step 1 — Diagnostic interviews** (1 hour)
- Contact 2–3 Group A orgs that adopted but did not engage further.
- Ask: "You received and reviewed the playbook — what happened after that? What would have made it easier to take the next step?"
- Record verbatim responses. Look for patterns: Is the barrier time? A specific unclear section? Lack of staff with implementation capacity? Waiting for organizational approval?

**Lever 1 — Simplify implementation pathway** (applies if barrier is "too comprehensive")
- Create a 5-page quick-start version of the relevant playbook section — the 3 most important actions, in plain language, with verification steps.
- Do not replace the full playbook. Offer it as: "Here's where to start — the full playbook is available when you're ready for more depth."
- This can be produced in 2–3 hours; prioritize for Group A orgs showing this pattern.

**Lever 2 — Add implementation support offer** (applies if barrier is capacity)
- Offer a 30-minute "office hours" call for implementation questions. Keep it concrete: "I can answer questions about Part 0 data broker opt-outs specifically — no technical background needed."
- Note in Group B invitations: "Office hours support available — you won't be on your own." This converts hesitant adopters who want reassurance of backup.

**Lever 3 — Peer adoption social proof** (applies if barrier is organizational approval)
- Request permission to reference adopting Group A organizations in Group B outreach: "FPF has implemented the journalist security playbook — here's what they found most useful."
- Social proof from a recognized peer organization removes the "is this legitimate?" barrier.

**Group B implication**: If this scenario applies, Group B invitations should lead with the quick-start version (not the full playbook) and mention office hours support from the first email.

---

### Scenario C: Security Incident Affects a Group A Organization

**When this applies**: An FPF, NLG, or CLS organization experiences a security incident (data breach, device compromise, targeted surveillance) during the pilot period.

**Assessment first**: The playbook is incident-response focused. An incident validates the playbook's threat model — if the countermeasures were not yet implemented, the incident demonstrates urgency. If countermeasures were implemented and the incident occurred anyway, it identifies gaps.

**Immediate response sequence** (within 24 hours of learning about the incident):
1. Contact the affected organization: "I heard about [incident]. I want to offer any support we can — we can go through the incident response section of the playbook together at no cost." Do not ask for information about what happened. Offer support.
2. Do not discuss the incident publicly or reference it in outreach to other organizations without explicit permission from the affected org.
3. If they agree to share outcome: document the incident in anonymized form (sector, type of incident, whether countermeasures were in place, outcome). This becomes a case study for Group B recruitment.

**Pilot timeline implication**: An incident at a Group A organization is an acceleration signal, not a setback.
- Organizations in Group B's outreach pipeline are now more aware of concrete threats. Incident news often travels within advocacy networks.
- If the affected organization consents, reference the outcome in Group B outreach: "An organization in the same sector recently faced [incident type]. Here is what the playbook's incident response section covers for this scenario."
- Maintain Group B timeline — accelerate it if the incident generates inbound interest from prospective Group B contacts.

**Do not**: Leak details of the incident, name the organization without consent, or use the incident as a sales argument in outreach without consent.

---

### Scenario D: Organizational Turnover or Leadership Change (Group A Contact Departs)

**When this applies**: Primary contact at FPF, NLG, or CLS departs or announces departure during the pilot period.

**Backup contacts** (from TIER_2_PILOT_LAUNCH_READINESS.md):
- FPF: If security@freedom.press bounces, use info@freedom.press to route to current security team.
- NLG Mass Defense: If massdef@nlg.org is unresponsive, NLG national office routes to current Mass Defense coordinator.
- CLS Philadelphia: If initial contact left, CLS intake line identifies correct immigration program staff.

**Response timeline**:
- On learning of departure: identify backup contact within 24 hours. Do not wait for a bounce — proactive re-routing is faster.
- Contact backup within 48 hours of identifying them. Brief introduction: name the departing contact, explain the prior engagement, offer to restart from wherever the organization is comfortable.

**If no backup exists and bounce occurs**:
- 48-hour re-engagement window: call the organization's main line, ask for the relevant department (security team at FPF, Mass Defense at NLG, immigration program at CLS), request an introduction to the new contact. This is a single call attempt.
- If call is not productive within 48 hours: deprioritize that organization for the pilot period. Do not send further emails. Move the 4th candidate (Access Now) into the active pilot slot.
- Do not count the departed-contact organization as a "no-go" for Gate 3 — note it as a contact-disruption event and assess the remaining 2–3 orgs for the adoption gate.

**Escalation threshold**: If 2+ Group A organizations are disrupted by contact turnover simultaneously, pause Group B start (do not begin Group B with fewer than 2 functioning Group A orgs). A Group A that loses contact integrity before providing feedback has not generated the refinements that Group B needs. Fix Group A first.

---

## Section 6: Contingency Activation Triggers

All triggers are binary: activated or not. Do not apply partial responses to triggers. Decision owner for all triggers is Anya unless otherwise noted.

---

**Trigger 1 — June 7 (Gate 1): Phase 1 click-through <20%**
- Condition: Bitly click rate below 20% after Wave 1 sends are complete
- Action: (1) Run deliverability test at mail-tester.com from the outreach address. (2) Check Gmail Sent folder — did all Wave 1 sends actually send? (3) Send a test email from the outreach address to a personal Gmail and non-Gmail account. Confirm it does not land in spam. (4) If deliverability score is below 7/10: switch to alternate email address for Wave 2. If score is above 7/10: test a different subject line variant.
- Group A implication: Do not send Group A follow-up emails until this is resolved. Hold Group A sessions if already scheduled (do not cancel, but do not schedule new ones).
- Resolution window: 48 hours maximum.
- Escalation: If not resolved in 48 hours, notify user with: (1) current click rate, (2) deliverability test result, (3) recommended action.
- Do not start: Group A follow-up outreach, Wave 2 sends

---

**Trigger 2 — June 15 (Gate 2): Phase 1 adoption <30% click, 0 meetings scheduled**
- Condition: Click rate below 30% cumulative AND no meetings scheduled after 2 full waves
- Action: (1) Pause Phase 1 Waves 3–5. (2) Convene self-diagnostic (1 hour): Is this a list quality problem? A message fit problem? A timing problem? (3) Redirect all daily resource hours to Phase 1 recovery — stop Group B preparation entirely.
- Group A implication: Group A may continue (it is independently valuable) but allocate no additional prep time to Tier 2 expansion until Phase 1 recovery is confirmed.
- Escalation: Notify user immediately with: (1) current metrics vs. targets, (2) probable cause assessment from diagnostic, (3) recommended pivot (list re-scope, message reframe, or timeline delay).
- Do not start: Group B preparation, Weeks 5–8 material customization

---

**Trigger 3 — July 1 (Gate 3): Group A adoption <40%**
- Condition: Fewer than 1 of 3 Group A organizations shows substantive engagement by July 1
- Action: (1) Do not send Group B invitations. (2) Run 1-on-1 calls with Group A non-responders — a single direct call request converts at higher rates than follow-up email for this audience. (3) Identify whether the barrier is subject line (reached wrong function), framing (too abstract), or timing (organization is in a high-workload period). (4) Document finding before deciding whether to proceed with Group B.
- Resolution criteria: At least 2 of 3 Group A orgs engaged before Group B launches. No fixed timeline — Group B timing is secondary to Group A integrity.
- Escalation: Notify user if Group B is delayed more than 2 weeks (past August 15) due to this trigger.
- Do not start: Group B outreach until at least 2 Group A orgs show engagement

---

**Trigger 4 — August 15 (Gate 4): Group B trending <35% adoption at mid-point**
- Condition: Of the first 5–7 Group B sends, fewer than 1–2 show any substantive engagement (reply with question, session scheduled, or feedback received)
- Action: (1) Run contact routing check — are messages reaching the correct function (organizing director, not external affairs; digital security team, not press)? (2) Review subject lines — test an alternate sector-specific line for remaining sends. (3) Increase personalization level for remaining unsent Group B invitations.
- Escalation: If mid-point engagement is still below 20% after routing check and subject line revision, notify user: "Group B is underperforming. Recommend pausing Tier 3 expansion planning pending diagnosis."
- Tier 3 implication: If this trigger is active, do not finalize the Tier 3 organizational shortlist until Group B diagnosis is complete.

---

**Trigger 5 (Positive) — August 28 (Gate 5): Both pilots show policy uptake in DIFFERENT sectors**
- Condition: Group A produces a policy ask in one sector (e.g., journalism or immigration legal aid) AND Group B produces a policy ask in a different sector (e.g., labor or civil liberties)
- Action: This is a positive trigger — accelerate Tier 3 planning for the sectors showing uptake. (1) Identify which sectors generated policy uptake. (2) Build Tier 3 organizational shortlist starting with those sectors. (3) Notify user: "Cross-sector policy uptake confirmed. Recommend GO for Tier 3 with [sectors] as priority targets."
- Tier 3 implication: Tier 3 outreach begins September 15 as planned, but sector prioritization is informed by which sectors generated uptake. Lead with high-uptake sectors first.
- No hold required: This trigger does not pause anything. It refines the Tier 3 execution sequence.

---

## Section 7: Tier 3 Readiness Criteria Scoring Matrix

Complete this matrix at Gate 5 (August 28). Calculate the weighted score and apply the decision threshold.

### Scoring Components

**Component 1: Phase 1 (Tier 1) Adoption — Weight 40%**

Source: `TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md` Day 42 gate data.

| Phase 1 Outcome | Raw Score | Weighted Score (×0.40) |
|----------------|-----------|----------------------|
| ≥60% meeting acceptance + ≥2 adoption signals | 100 | 40 |
| 40–59% meeting acceptance + ≥1 adoption signal | 75 | 30 |
| 20–39% meeting acceptance, 0 adoption signals | 50 | 20 |
| <20% meeting acceptance | 25 | 10 |
| Campaign not completed | 0 | 0 |

---

**Component 2: Group A Adoption + Engagement — Weight 30%**

Source: Pilot tracking tab, Group A section.

| Group A Outcome | Raw Score | Weighted Score (×0.30) |
|----------------|-----------|----------------------|
| ≥2 of 3 orgs adopted + ≥2 messaging refinements documented | 100 | 30 |
| ≥2 of 3 orgs adopted, <2 refinements documented | 75 | 22.5 |
| 1 of 3 orgs adopted, ≥1 refinement | 50 | 15 |
| 0 orgs adopted / contact disruption prevented assessment | 25 | 7.5 |

---

**Component 3: Group B Adoption — Weight 20%**

Source: Pilot tracking tab, Group B section.

| Group B Outcome | Raw Score | Weighted Score (×0.20) |
|----------------|-----------|----------------------|
| ≥50% of Group B orgs adopted | 100 | 20 |
| 35–49% of Group B orgs adopted | 75 | 15 |
| 20–34% of Group B orgs adopted | 50 | 10 |
| <20% of Group B orgs adopted | 25 | 5 |
| Group B not launched (Phase 1 or Group A failure) | 0 | 0 |

---

**Component 4: Policy Uptake Signals — Weight 10%**

Source: Meeting notes, email threads, Tab 4 adoption signals (Phase 1), pilot tracking tab.

| Policy Uptake Outcome | Raw Score | Weighted Score (×0.10) |
|----------------------|-----------|----------------------|
| Policy uptake in 2+ sectors (different sectors) | 100 | 10 |
| Policy uptake in 1 sector (any) | 75 | 7.5 |
| Policy interest expressed but no confirmed uptake | 50 | 5 |
| No policy signals detected | 25 | 2.5 |

---

### Tier 3 Decision Thresholds

**Calculate**: Sum the four weighted scores. Total possible = 100.

| Total Weighted Score | Decision | Action |
|---------------------|----------|--------|
| >55 | **GO** | Proceed to full 50-org Tier 3 expansion beginning September 15. Prioritize sectors showing highest policy uptake. |
| 40–55 | **CONDITIONAL** | Proceed with 25-org Tier 3 subset. Lead with Fast Follower cohort (FF-01 through FF-05) + highest-scoring Steady Majority orgs. Pause remainder until CONDITIONAL orgs reach 50% adoption. |
| <40 | **INSUFFICIENT DATA** | Pause Tier 3. Convene diagnostic session with 3 Group A/B adopters. Identify root cause. Reassess at 90-day mark (late November 2026). Do not expand to 50 orgs until scoring reaches 40+. |

**Worked example (illustrative)**:
- Phase 1: 50% meeting acceptance, 1 adoption signal → raw 75 × 0.40 = 30
- Group A: 2 of 3 adopted, 2 refinements → raw 100 × 0.30 = 30
- Group B: 40% of Group B adopted → raw 75 × 0.20 = 15
- Policy: 1 sector uptake → raw 75 × 0.10 = 7.5
- Total: 82.5 → **GO**

---

## Section 8: Resource Allocation Table

### Weekly Resource Estimates (Hours Per Day)

| Period | Phase | Activities | Hours/Day | Hours/Month |
|--------|-------|-----------|-----------|-------------|
| Weeks 1–4 (June 1–28) | Phase 1 active | Outreach coordination, Bitly monitoring, reply logging, follow-up management | 3.0 | — |
| Weeks 1–4 (June 1–28) | Group A pilot | Invitation follow-up, session scheduling, feedback collection | 1.0 | — |
| **Weeks 1–4 Total** | | | **4.0** | **~80 hours** |
| Weeks 5–6 (July 1–14) | Phase 1 follow-up + Group A synthesis | Week 6 adoption follow-ups; Group A feedback synthesis | 2.5 | — |
| Weeks 7–8 (July 15–28) | Group B prep | Contact verification, message customization, outreach sequencing | 1.5 | — |
| **Weeks 5–8 Total** | | | **~2.0** | **~40 hours** |
| Weeks 9–10 (Aug 1–14) | Group B delivery | Outreach, response monitoring, session scheduling | 3.0 | — |
| Weeks 11–12 (Aug 15–28) | Group B engagement + Tier 3 prep | Feedback collection, metric tracking, scoring matrix, Tier 3 shortlist | 3.0 | — |
| **Weeks 9–12 Total** | | | **3.0** | **~48 hours** |
| **12-Week Total** | | | | **~168 hours** |

**FTE check**: 168 hours over 12 weeks = 14 hours/week = 2.8 hours/day on a 5-day week. This is sustainable at 1 FTE with moderate workload. Weeks 1–4 are the heaviest (4 hours/day); allow for this concentration.

---

### Contingency Reallocation (If Group A <40% Adoption — Trigger 3)

When Trigger 3 activates (Group A below threshold, Group B on hold):

| Reallocated Activity | Hours/Day Freed | Redirected To |
|--------------------|----------------|---------------|
| Group B material customization | 1.5 | Group A diagnostic + re-engagement |
| Tier 3 list preparation | 0.5 | Phase 1 adoption signal follow-up |
| **Total reallocated** | **2.0** | Concentrated on Group A recovery |

**Net resource in contingency**: 2.0 hours/day for Group A recovery + 1.0 hour/day for ongoing Phase 1 monitoring = 3.0 hours/day total. Group B prep resumes only after Group A gate is met.

---

## Section 9: Contingency Timeline

### Scenario 1: Phase 1 Delivery Slips 2 Weeks (June 1 → June 15 Start)

If Phase 1 begins June 15 instead of June 1 (2-week slip):

| Milestone | Original Date | Slipped Date | Impact |
|-----------|---------------|--------------|--------|
| Gate 1 (Phase 1 W1) | June 7 | June 21 | 2-week delay |
| Gate 2 (Phase 1 W2) | June 15 | June 28 | 2-week delay |
| Group A launch | May 28 | June 15 (revised) | Lost 3-week parallel benefit |
| Gate 3 (Group A) | July 1 | July 15 | 2-week delay |
| Group B launch | August 1 | August 15 | 2-week delay |
| Gate 5 (Group B) | August 28 | September 12 | 2-week delay |
| Tier 3 decision | September 15 | October 1 | 2-week delay |

**Impact assessment**: Moderate. Group A no longer runs fully concurrent with Phase 1 (lose approximately 2 weeks of parallel validation), but Group B timeline remains intact with only a 2-week slip. Tier 3 moves from September 15 to October 1 — acceptable trade-off given additional validation data from the longer Phase 1 window.

**Group A adjustment**: If Phase 1 slips to June 15 start, send Group A invitations June 10–12 (3–5 days before Phase 1 launch). Group A still launches before Phase 1 completes; partial parallel benefit preserved.

---

### Scenario 2: Phase 1 Adoption <40%, Diagnostic Extends to July 15

If Gate 2 (June 15) triggers a no-go and the Phase 1 diagnostic takes 4 weeks:

| Milestone | Original Date | Slipped Date | Impact |
|-----------|---------------|--------------|--------|
| Phase 1 diagnostic complete | — | July 15 | 4-week diagnostic period |
| Group A launch (with refined playbook) | May 28 | August 1 | 10-week delay |
| Gate 3 (Group A) | July 1 | September 1 | 9-week delay |
| Group B launch | August 1 | September 15 | 6-week delay |
| Gate 5 (Group B) | August 28 | October 15 | 7-week delay |
| Tier 3 decision | September 15 | November 1 | 7-week delay |

**Impact assessment**: Significant but not disqualifying. The 7-week slip moves Tier 3 decision to November 1. Full Tier 3 expansion would then target December 2026–January 2027 (winter academic/policy calendar). The trade-off: more refinement data = higher Group A and B success probability when launched.

**Key insight**: A failed Phase 1 diagnostic that results in a genuinely improved playbook produces better Tier 2/3 outcomes than a hasty Group A launch with unresolved Phase 1 framing problems. Accept the delay.

**Resource during diagnostic period**: Redirect all 4 hours/day to Phase 1 analysis. Do not begin Group A outreach until the diagnostic is complete and at least 2 specific messaging revisions are documented.

---

## Appendix: Gate Reference Card

Print and keep with the tracking spreadsheet during Phase 1 and pilot execution.

```
GATE REFERENCE CARD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GATE 1 — June 7  |  Decision Owner: Anya
Check: Bitly click rate after Wave 1 (5 sends)
• >30%: Proceed. Run Wave 2 as scheduled.
• 20–30%: Caution. Revise subject line before Wave 2.
• <20%: STOP. Deliverability diagnostic. 48h window. Hold Group A follow-ups.

GATE 2 — June 15  |  Decision Owner: Anya
Check: Click rate cumulative + meetings scheduled (all waves to date)
• >40% clicks + ≥3 meetings: GO. Approve Group B timeline. Begin Group B prep.
• 30–40% clicks + 1–2 meetings: Caution. Proceed Phase 1. Group B contingent.
• <30% clicks + 0 meetings: STOP. Pause Tier 2 prep. Phase 1 diagnostic only.

GATE 3 — July 1  |  Decision Owner: Anya
Check: Group A adoption count (orgs with substantive engagement)
• 2–3 of 3 orgs: GO. Begin Group B customization this week.
• 1 of 3 orgs: Caution. Direct call to non-responders first. Group B delayed.
• 0 of 3 orgs: STOP. Diagnostic. Group B on hold. Escalate if 2+ weeks delay.

GATE 4 — August 15  |  Decision Owner: Anya
Check: Group B mid-point engagement (first 5–7 sends)
• >35% engagement: On track. Continue Group B outreach.
• 20–35%: Warning. Route check + subject line revision.
• <20%: Escalate. Halt Tier 3 planning. Notify user.

GATE 5 — August 28  |  Decision Owner: Anya
Check: Tier 3 scoring matrix (Section 7) — calculate weighted score
• >55: GO — full 50-org Tier 3 expansion, September 15.
• 40–55: CONDITIONAL — 25-org subset, prioritize high-uptake sectors.
• <40: INSUFFICIENT — pause, diagnostic quarter, reassess November 2026.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

*Created: 2026-05-13. Production-ready for Phase 1 execution beginning June 1, 2026. All gate thresholds pre-committed — do not adjust during execution without documenting the reason and the data that warranted adjustment.*

*Coordinates with: `TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md` (KPI targets and measurement infrastructure), `TIER_2_PILOT_LAUNCH_READINESS.md` (Group A organization selection and 8-week pilot plan), `TIER1_OUTREACH_EXECUTION_PLAN.md` (Phase 1 wave cadence), `tier-2-sector-contact-lists.md` (Tier 2 verified contacts), `TIER_2_DISTRIBUTION_STRATEGY.md` (full Tier 2 sector messaging and sequencing).*
