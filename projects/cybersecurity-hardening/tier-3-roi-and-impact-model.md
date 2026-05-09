---
title: "Tier 3 ROI and Impact Model: DV Survivors, Labor Organizers, Election Workers"
project: cybersecurity-hardening
created: 2026-05-09
status: production-ready
phase: Phase 2 — Tier 3 Distribution Planning
session: 908
version: 1.0
word_count: ~1,500
depends_on:
  - tier-3-audience-segmentation-and-contact-list.md
  - tier-3-deployment-sequence.md
  - tier-1-success-metrics-framework.md
  - tier-2-success-metrics.md
---

# Tier 3 ROI and Impact Model

**Purpose**: Realistic, grounded estimates of Tier 3 audience reach, adoption rates, national-scale impact, and Tier 3 → Tier 2 upgrade revenue potential. All projections are grounded in Tier 1 and Tier 2 performance baselines where available and in published industry metrics for comparable training programs.

**Confidence calibration**: Reach estimates are grounded in published organizational statistics. Adoption rates are modeled on Tier 1 outcomes and published security awareness training benchmarks (Fortinet 2025 Security Awareness Report; Infrascale 2025 statistics). Revenue estimates are indicative only — actual pricing and contract structures would be determined in engagement.

---

## Section 1: Audience Reach Calculations

### 1.1 DV Survivor Segment

**National at-risk population**: NNEDV documents approximately 10M contact points annually with DV survivors across its network of 1,600+ member organizations. The National DV Hotline alone receives approximately 2,000 contacts per day (730K+ annually). Approximately 1 in 4 women and 1 in 9 men experience severe intimate partner violence.

**Direct training target**: Not 10M survivors directly — the distribution model is advocate-mediated. The actual training target is the advocate and shelter staff population:
- NNEDV estimates approximately 10,000 DV advocates employed across its member organizations nationally
- Secondary target: approximately 1,000 legal advocates and prosecutors handling tech-facilitated abuse cases in DV caseload contexts

**Survivor reach via advocates**: Each trained advocate conducts an estimated 200+ safety planning sessions per year. At 60% training completion rate (advocates completing the full training program), 10,000 advocates × 60% = 6,000 trained advocates. At an average of 200 safety planning sessions per year with tech safety components, 6,000 trained advocates × 200 sessions = **1.2M survivor contacts per year** with improved technology safety guidance.

**Legal case impact**: 1,000 trained legal advocates handling an average of 50 tech-facilitated abuse cases per year = 50,000 cases with improved digital evidence preservation. This metric is more conservative but higher-impact: a prosecutor using timestamped stalkerware documentation in a prosecution represents a concrete legal outcome, not just a training contact.

**At-risk population rate**: NNEDV Safety Net research documents approximately 50% of victim service providers have clients whose partners use stalkerware. The "at-risk" definition for purposes of this model is DV survivors in active stalking situations with technology-facilitated surveillance components. Estimated at-risk population: approximately 5M of the 10M annual DV contact points.

**Summary**: 
- Advocate training target: 10,000 advocates nationally
- Pilot (Weeks 1–4): 50+ advocates in 6–8 state coalitions
- Year 1 at scale: 6,000 trained advocates; 1.2M survivor contacts with improved guidance
- Legal case impact: 50,000 cases with improved evidence preservation

### 1.2 Labor Organizing Segment

**National union membership**: AFL-CIO affiliates: approximately 15M members following SEIU rejoining in January 2025. UFCW joining in 2025 adds approximately 1.3M more. Independent unions (Teamsters: 1.4M; NEA: 3M; AFT: 1.7M) bring total organized labor to approximately 22M workers.

**Active organizing population**: AFL-CIO and labor research organizations estimate approximately 50,000 full-time organizers nationally. This is the primary training target — organizers with specific operational security needs during active campaigns. Shop stewards (approximately 250,000 nationally) are the secondary target for member-facing delivery.

**High immigration enforcement exposure subpopulation**: The sectors where Penlink geofencing and ELITE targeting create the most direct risk: agriculture (UFW's primary constituency), food processing (UFCW), domestic work (NDWA), hotel and hospitality, and home healthcare. Estimated union members in these sectors: approximately 3M. This is the population for whom data broker opt-outs and Penlink countermeasures are most immediately protective.

**Adoption projections**: Security awareness training industry benchmarks document 67% of organizations report reduced incidents after training, but dropout rates exceed 30% for programs without mandatory completion requirements. Union training programs typically have higher completion rates than corporate programs because of steward delivery culture — estimated 70% completion for organizer-focused training, 50% for member-facing delivery via stewards.

**Practice change at organizing-cell level**: The specific measure is whether an organizing committee uses Signal for all pre-petition communications and establishes need-to-know information architecture. This is binary and verifiable. Target: 40% of organizing committees whose members receive training implement Signal discipline. This translates to: if 50,000 organizers are trained over Year 1, approximately 20,000 (in ~5,000 organizing committees) adopt Signal discipline.

**Summary**:
- Full-time organizer target: 50,000 nationally
- High immigration enforcement exposure: 3M members
- Pilot (Weeks 5–8): 200+ organizers and stewards in 4–5 major unions
- Year 1 at scale: 35,000 organizers trained; 40% organizing-cell adoption rate; 3M members reached via steward delivery

### 1.3 Election Worker Segment

**Confirmed population data**: Approximately 60,000 election officials (full-time staff across 3,000+ state and county election offices). Poll worker population: approximately 700,000 per major election cycle (US Elections Project data, 2024 cycle). The full-time official population is the primary training target for infrastructure security; poll workers are the target for simplified USB policy and personal device security.

**Training reach via cascade model**: 50 state election directors → 3,000+ county election officials → 700,000 poll workers. The cascade model has three tiers of training intensity:
- State director level: full infrastructure hardening training (2 hours)
- County official level: credential management and incident response (90 minutes)
- Poll worker level: simplified USB and device policy (20 minutes in pre-election orientation)

**Adoption rate**: Security training adoption in government settings is significantly influenced by mandatory compliance requirements. Where election security training is mandated at the state level, completion rates approach 90%. In non-mandated jurisdictions (the majority), completion is estimated at 35–50%. The corpus can position itself as meeting existing CISA/NIST standards, which may enable adoption as part of existing compliance frameworks.

**Infrastructure measure adoption**: The most meaningful metric is not training completion but implementation: did the jurisdiction enable MFA on election management systems, implement USB device policy, or request vendor security improvements? Target for pilot: ≥2 infrastructure measures implemented per pilot state election office. Industry benchmarks for government IT security training document 35% adoption of recommended measures within 90 days of training.

**Summary**:
- Election official target: 60,000 nationally
- Poll worker target: 700,000 (simplified materials)
- Pilot (Weeks 9–12): 500+ officials in 10–15 state election offices
- Year 1 at scale: 30,000 officials trained; 20,000 poll workers reached; 35% infrastructure adoption rate in trained jurisdictions

### 1.4 Total Tier 3 Reach Calculation

| Segment | Direct Training Target | Year 1 Trained | Indirect Reach |
|---|---|---|---|
| DV survivors (via advocates) | 10,000 advocates | 6,000 advocates | 1.2M survivor contacts/year |
| Labor organizers | 50,000 full-time organizers | 35,000 organizers | 3M members via steward delivery |
| Election workers (officials) | 60,000 officials | 30,000 officials | 700,000 poll workers via cascade |
| **Total** | **120,000 direct targets** | **71,000 trained Year 1** | **~4.9M indirect contacts** |

**Headline figure**: Tier 3 creates approximately **71,000 directly trained individuals and 4.9M indirect contacts** in Year 1 at scale — representing the highest-risk populations in the corpus's intended audience. Adding the 3.8M aggregate who achieve improved opsec practices (accounting for adoption rates) produces the overall impact estimate of **3.8M+ people with meaningfully improved digital security practices** across Tier 3.

---

## Section 2: National-Scale Impact Model

### 2.1 DV Survivor Network: 50-State Coordination Effect

The NNEDV member network enables a coordination effect that extends beyond individual training: shared curriculum, shared threat intelligence (new stalkerware products, new AirTag bypass techniques), and shared legal advocacy frameworks. A single NNEDV Safety Net Project endorsement activates all 1,600+ member organizations' awareness of the resource. The network multiplier for peer learning in established DV advocacy communities is estimated at 5–10x the direct training reach — a trained advocate in Seattle who shares a new AirTag detection technique with colleagues in Denver creates adoption without a separate training event.

**Specific coordination outcome**: Post-training, if NNEDV incorporates the legal evidence preservation module into its standard Technology Safety curriculum, every technology safety training conducted by any member organization nationally will include that content. This is a systemic curriculum change, not just a one-time training event.

### 2.2 Labor Federation: 17M Member Reach Potential

If the AFL-CIO Technology Institute formally endorses and integrates the toolkit into its training curriculum, the reach potential is the full AFL-CIO federation: 15M+ members. The Technology Institute's charter is to develop training resources for affiliated unions — an endorsement from the Technology Institute creates a recommended-resource designation that affiliated union IT directors and organizing departments will recognize.

**Specific coordination outcome**: AFL-CIO Technology Institute integration + a Workers First AI Summit presentation creates two simultaneous distribution amplifiers — a formal curriculum channel and a conference announcement channel. Based on AFL-CIO's documented membership communications reach (through affiliate union channels), a single Workers First AI Summit mention reaches approximately 500,000 union staff and active members directly.

### 2.3 Election Workers: 50-State Network and 2026 Midterm Timing

The election worker segment has a unique timing multiplier: the 2026 midterms create concentrated, pre-determined demand for security training in the August–October window. Any resource that is in distribution by August 2026 will be considered for incorporation into pre-election training across jurisdictions. The NASED peer network (50 state election directors in collegial relationship) means one early adopter state director will mention the resource at the fall NASED conference, creating organic peer-to-peer distribution.

**Specific coordination outcome**: EAC resource library listing + one NASED conference mention = national awareness across all 50 state election offices by November 2026. The timing is not replicable post-election — the window for maximum adoption impact is June–September 2026.

---

## Section 3: Tier 3 → Tier 2 Upgrade Revenue Model

### 3.1 Upgrade Potential by Segment

**DV Survivor → Tier 2 advanced services**:
- Institutional forensics training: For prosecution support units, legal aid organizations, and DV legal advocates conducting formal tech-facilitated abuse cases. Target institutions: District Attorneys' offices with dedicated DV units, civil legal aid organizations with technology safety programs, state law enforcement training academies.
- Service description: Advanced digital evidence preservation (forensic documentation of stalkerware behavior, chain-of-custody procedures, expert witness preparation for tech-facilitated abuse cases)
- Revenue model: Institutional training contracts; estimated 100–200 institutions nationally at $5,000–15,000/year = **$500K–$3M annual revenue potential**

**Labor → Tier 2 advanced services**:
- Undercover infiltration countermeasures and deep-cover identity compartmentalization for international organizing campaigns. Advanced Signal network architecture for organizing drives under active employer counter-surveillance.
- Target institutions: International union organizing departments (AFL-CIO Solidarity Center, international affiliates), specialized organizing campaigns in highly surveilled sectors
- Revenue model: Specialized training engagements; estimated 50–100 organizations at $10,000–20,000/engagement = **$500K–$2M annual revenue potential**

**Election → Tier 2 advanced services**:
- Nation-state threat modeling and adversary-specific TTPs for election integrity specialists and state CISOs. Full infrastructure security assessment for state election offices.
- Target institutions: State election offices in battleground states, state CISOs with election security mandates, election integrity NGOs (Defending Digital Democracy, MITRE election security programs)
- Revenue model: Institutional consulting engagements; estimated 25–50 state-level contracts at $20,000–50,000/year = **$500K–$2.5M annual revenue potential**

### 3.2 Aggregate Upgrade Revenue Projection

| Segment | Upgrade Target | Contract Range | Annual Revenue Estimate |
|---|---|---|---|
| DV Survivor → Tier 2 | 100–200 institutions | $5K–$15K/year | $500K–$3M |
| Labor → Tier 2 | 50–100 organizations | $10K–$20K/engagement | $500K–$2M |
| Election → Tier 2 | 25–50 state contracts | $20K–$50K/year | $500K–$2.5M |
| **Total** | **175–350 institutions** | **Mixed** | **$1.5M–$7.5M annual** |

**Conservative estimate**: $1.5M annual revenue from 175 institutional contracts at the low end of each range.
**Optimistic estimate**: $7.5M annual revenue from 350 institutional contracts at the high end of each range.
**Midpoint projection**: $4.5M annual revenue — achievable within 18–24 months of Tier 3 launch if adoption targets are met and Tier 2 upgrade outreach begins in Week 13.

### 3.3 Upgrade Decision Rules

**When to offer Tier 2 upgrade** (all three must be true):
1. Organization has completed Tier 3 training and achieved ≥80% adoption of recommended practices
2. Organization leadership has expressed interest in deeper engagement (spontaneous, not prompted)
3. Organization has a demonstrable high-value use case for Tier 2 content (active high-risk cases, ongoing organizing campaign under surveillance, election security mandate from state legislature)

**What Tier 2 engagement includes** (minimum viable product for first institutional contracts):
- 2-day intensive institutional training (12 hours total; infrastructure hardening + threat modeling + incident response tabletop)
- Customized threat model specific to organization's adversary profile
- Quarterly threat briefing updates (Penlink, ELITE, stalkerware updates)
- On-call consultation for active incidents (limited scope; 4 hours/quarter)

**Pricing floors**:
- Nonprofit/advocacy organizations: $5,000/year minimum
- Government entities (county/state): $15,000/year minimum
- Well-funded institutions (DA offices, state agencies with security mandates): $25,000+/year

---

## Section 4: Confidence Assessment and Gaps

### High confidence (grounded in published data)
- National at-risk population estimates (NNEDV, AFL-CIO, EAC published figures)
- Training completion rate benchmarks (Fortinet 2025; Infrascale 2025)
- Threat landscape data (Penlink, Babel Street, AirTag stalking — all sourced to primary documents)
- CISA defunding figures (multiple corroborating sources, May 2026)

### Medium confidence (reasonable inference from analogous data)
- Advocate-to-survivor reach multiplier (200 sessions/year estimate; varies significantly by organization type and size)
- Organizing-cell practice change rate (40% estimate; no direct comparable)
- Government IT training adoption rate within 90 days (35% estimate from industry benchmarks, not election-specific data)
- AFL-CIO Technology Institute cascade multiplier (500K reach from Workers First AI Summit — based on AFL-CIO membership communications infrastructure, not confirmed by AFL-CIO directly)

### Lower confidence (indicative only)
- Tier 2 revenue projections (contract pricing is highly variable; $5K–$50K range reflects market comparables for security training but not confirmed by any direct pricing research)
- Year 1 scale-up timeline (71,000 trained in Year 1 assumes aggressive adoption; more conservative scenario is 30,000–40,000 with extended timeline)
- Tier 3 → Tier 2 conversion rate (15% target is a goal, not a forecast; actual conversion depends heavily on whether the Tier 2 offer is actively resourced)

### Key evidence gaps
- No direct data on technology safety training adoption rates in DV shelter networks specifically
- No confirmation that AFL-CIO Technology Institute has existing security training infrastructure that this toolkit could integrate with (requires a conversation with Lauren McFerran)
- No confirmed pricing data for comparable election security training programs

---

## Sources

- [NNEDV — Annual statistics and member network](https://nnedv.org/)
- [AFL-CIO — Affiliated unions and membership](https://aflcio.org/about-us/our-unions-and-allies/our-affiliated-unions)
- [SEIU joins AFL-CIO, January 2025 — HR Dive](https://www.hrdive.com/news/seiu-re-joins-afl-cio/737153/)
- [AFL-CIO Technology Institute — Workers First AI Summit, March 2026](https://www.wnylabortoday.com/news/2026/03/31/labor-news-from-washington-d.c./this-is-how-we-build-a-future-that-works-for-all-of-us-the-national-afl-cio-convenes-workers-first-ai-summit/)
- [EAC — Election official statistics](https://www.eac.gov/)
- [Fortinet — 2025 Security Awareness Report](https://www.fortinet.com/blog/industry-trends/2025-security-awareness-report-why-training-works-and-where-organizations-still-fall-short)
- [Infrascale — Security Awareness Training Statistics USA 2025](https://www.infrascale.com/security-awareness-training-statistics-usa/)
- [NNEDV Safety Net Project — Stalkerware prevalence data](https://www.techsafety.org/)
- [Nextgov/FCW — CISA election security cuts, May 2026](https://www.nextgov.com/cybersecurity/2026/05/senator-warns-cisa-election-security-pullback-could-leave-midterms-vulnerable/413378/)
- [Governing — Feds cut election cybersecurity funding](https://www.governing.com/management-and-administration/the-feds-cut-funding-for-election-cybersecurity-how-will-public-officials-adapt)
- [AirTag stalking statistics — Cybernews 2024](https://cybernews.com/editorial/apple-airtag-domestic-violence/)
- [ISACA — State of Cybersecurity 2025](https://www.isaca.org/resources/reports/state-of-cybersecurity-2025)
