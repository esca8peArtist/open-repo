---
title: "Tier 3 Audience Segmentation and Contact List: DV Survivors, Labor Organizers, Election Workers"
project: cybersecurity-hardening
created: 2026-05-09
status: production-ready
phase: Phase 2 — Tier 3 Distribution Planning
session: 908
version: 1.0
word_count: ~2,500
depends_on:
  - tier-3-audience-expansion-roadmap.md
  - TIER3_DISTRIBUTION_PREP.md
  - phase-2-dv-survivor-safety-playbook.md
  - phase-2-threat-briefing-labor-organizers.md
  - election-worker-opSec-supplement.md
  - tier-3-threat-model.md
---

# Tier 3 Audience Segmentation and Contact List

**Purpose**: Production-ready segmentation of the three Tier 3 priority populations — domestic violence survivors, labor organizers, and election workers — with threat models calibrated to each segment, decision-maker maps, and verified contact targets for pilot outreach beginning June 1, 2026.

**Context**: Tiers 1 and 2 seeded the corpus into digital rights organizations, academic security programs, journalist organizations, and policy think tanks. Tier 3 moves from institutional amplifiers to direct-audience organizations that serve high-risk populations who have no prior security background. The distribution model shifts accordingly: simpler materials, higher trust mediation requirements, and organization-specific threat framing.

**Total Tier 3 reach potential**: 10.8M people across three highest-risk categories:
- DV survivors: 10M+ annual contact points via NNEDV and state coalition networks
- Labor organizers: 17M union members; 50K full-time organizers at highest risk
- Election workers: 60K election officials + 700K+ poll workers

---

## Section 1: Tier 3 Audience Overview

### Why These Three Segments

The three Tier 3 populations share a common structural condition: they are individually high-risk, institutionally under-resourced on security, and reachable through specific national networks with established trust. None of them are served adequately by the corpus as currently packaged for Tier 1/2 audiences.

**DV survivors** face abuser surveillance that is intimate-access-based, not government-or-corporate-based. Their threat model is categorically different from the Palantir/ICE frame that dominates Tiers 1 and 2. Approximately half of victim service providers report that perpetrators use stalkerware on their partners' devices (NNEDV Safety Net Project data). These survivors are reachable through the established NNEDV coalition infrastructure — 56 state and territorial coalitions, 1,600+ member organizations serving 1.6M survivors annually.

**Labor organizers** face a compounded threat: employer surveillance of organizing activity combined with immigration enforcement targeting of immigrant workers through the exact same Penlink/ELITE infrastructure documented in the corpus. The September 2025 DHS Penlink PLX contract allows geofencing of protest and organizing locations. The UAW/CWA/AFT lawsuit (filed October 2025) documented that AI-powered social media surveillance of union members has already created a chilling effect: 60%+ of UAW members aware of the program changed their social media behavior. This population is reachable through the AFL-CIO federation structure and its 56 affiliated unions.

**Election workers** face a distinct threat: infrastructure-level ransomware targeting election offices, USB/bootloader attacks on election management systems, and insider threat vectors through poll worker access. The CISA election security program has been substantially defunded — more than a third of CISA's workforce was cut since February 2026, and the FY2027 budget proposes eliminating the election security program entirely (Nextgov/FCW, May 2026). 75% of local election officials report insufficient replacement resources. The election worker population is accessible through the EAC and NASED, organizations with direct relationships to all 50 state election offices and 3,000+ county jurisdictions.

### Shared Structural Conditions

Each segment has a national gateway organization that can activate the broader network — NNEDV (DV), AFL-CIO (labor), EAC (election). Each also has a specific trust mediation requirement: materials cannot be distributed cold; they must arrive through a trusted organizational channel. And each segment faces a materially worsening threat environment in 2026 driven by federal policy changes, technology capability expansion by adversaries, and defunding of the support infrastructure they previously relied on.

---

## Section 2: DV Survivor Segment

### 2.1 Threat Model

The DV survivor threat model is intimate-access-first. The primary adversary has pre-existing inside access to the survivor's devices, accounts, credentials, and physical location. Standard "external attacker" hardening frameworks do not apply. The threat is:

**Stalkerware**: Commercial products (mSpy, FlexiSPY, Hoverwatch, Cocospy) installed on victim devices by abusers with physical access. As of 2025, approximately half of victim service providers report clients whose abusive partners use stalkerware. These products monitor real-time GPS location (typically updating every 1–15 minutes), calls, SMS, keystrokes, camera, and microphone. They are designed to be invisible and often masquerade as system apps.

**AirTag and Bluetooth tracker stalking**: AirTag stalking cases increased 317% by 2024. Abusers plant $29 trackers in bags, vehicles, and clothing. A 2024 Chicago case ended in murder after a victim removed a tracking device, triggering retaliation. Samsung SmartTags and Tile are used identically. Detection requires active scanning with apps such as Apple's Tracker Detect or Android's Safety app — neither of which survivors typically know to use.

**Account credential access**: Abusers with knowledge of Apple ID, Google account, or iCloud credentials can monitor without device contact — accessing iCloud photo libraries, location via Find My, iCloud-backed iMessage, and email. Family plan primary account holders have carrier-level access to call records, data usage, and real-time location for all lines.

**Biometric coercion**: Courts are split on whether compelled biometric device unlock violates the Fifth Amendment. In the DV context, this legal question is irrelevant — abusers physically force biometric unlock by holding a victim's face or finger to the device. Safety Net Project guidance specifically warns that changing security settings without a safety plan can trigger this escalation vector.

**Digital coercion as evidence suppression**: Abusers use account control and credential access to monitor legal communications, delete evidence, and interfere with protective order proceedings. Legal evidence preservation — screenshots, timestamped exports of threatening messages — is both a safety and legal tool.

**Technical readiness**: Low-to-moderate. Shelter staff and DV advocates are the primary intermediary — survivors require advocate-mediated introduction to any technical material. Training must be designed for advocates to deliver, not for survivors to self-administer.

### 2.2 Network Structure

- National gateway: NNEDV (National Network to End Domestic Violence), Washington DC
  - Safety Net Project: Dedicated technology safety program at techsafety.org; contact SafetyNet@NNEDV.org
  - Member network: 56 state and territorial coalitions, 1,600+ local member organizations
- Secondary channels: National DV Hotline (1-800-799-7233), state DV coalitions, local shelters, legal aid organizations

### 2.3 Decision-Makers

- NNEDV: President and CEO; Safety Net Project Director; Technology Safety Director
- State coalitions: Executive Director, Technology Safety Coordinator, Training Director
- Local organizations: Executive Director, Safety Planning Coordinator

### 2.4 Customization Angle

Two distinct value propositions:

**Safety-first opsec (low technical burden, high effectiveness)**: The content that matters most for survivors is a short, advocate-delivered protocol covering: using a safe device (library, trusted friend's phone); detecting AirTag and stalkerware; account separation checklist; carrier plan separation. This must be deliverable in a 15-minute advocate conversation, not an 8-section guide.

**Legal protection (evidence preservation for restraining orders, prosecution)**: This is often more immediately actionable for shelter legal advocates and prosecution support staff than device hardening. Timestamped exports of threatening messages, documentation of stalkerware behavior for courts, location tracking evidence chains. The corpus can be positioned as a tool for legal advocates handling tech-facilitated abuse cases.

### 2.5 Contact Targets (12 Organizations)

| Organization | Role | Contact | Notes |
|---|---|---|---|
| NNEDV National | National gateway | SafetyNet@NNEDV.org | Safety Net Project is the direct program; coordinates all 56 state coalitions |
| California Partnership to End DV (CPEDV) | Largest state coalition by population | info@cpedv.org | 916-444-7163; 107 9th St. Ste 910, Sacramento CA |
| Texas Council on Family Violence | 2nd largest state | tcfv.org contact form | Austin TX; serves 200+ Texas programs |
| New York State Coalition Against DV | 3rd largest state | nyscadv@nyscadv.org | 800-942-6906; Albany NY |
| Florida Coalition Against DV | 4th largest state | fcadv.org contact form | Tallahassee FL |
| Illinois Coalition Against DV | 5th largest | icadv@ilcadv.org | Springfield IL |
| Pennsylvania Coalition Against DV | 6th largest | webmaster@pcadv.org | Harrisburg PA |
| Ohio Domestic Violence Network | 7th largest | odvn@odvn.org | Columbus OH |
| Georgia Coalition Against DV | 8th largest | gcadv@gcadv.org | Atlanta GA |
| North Carolina Coalition Against DV | 9th largest | nccadv@nccadv.org | Durham NC |
| Michigan Coalition to End DV | 10th largest | mcedv@mcedv.org | Lansing MI |
| Washington State Coalition Against DV | Pacific Northwest hub | wscadv.org contact form | Seattle WA; strong tech sector connections |

**Verification approach**: All state coalition contacts are findable at nnedv.org/content/state-u-s-territory-coalitions/ and ncadv.org/state-coalitions. Email patterns follow [acronym]@[acronym].org in most cases; verify at coalition websites before sending.

---

## Section 3: Labor Organizing Segment

### 3.1 Threat Model

The labor organizing threat model in May 2026 has two compounding layers: employer surveillance of organizing activity and government immigration surveillance infrastructure that can be weaponized against immigrant workers in organizing campaigns.

**Penlink PLX geofencing (confirmed operational, September 2025)**: DHS awarded a $2.9M contract to Penlink PLX in September 2025. The system geofences specific locations — including protest sites, union halls, and worker gathering points — and identifies every phone present during a specified timeframe by purchasing commercial advertising SDK location data. ICE has used this technology against individuals who observed or protested enforcement operations (Prism Reports, April 2026). For labor organizing in sectors with high concentrations of immigrant workers (agriculture, food processing, domestic work, hotel/hospitality), an organizer's repeated presence at organizing events creates a location pattern accessible via Penlink to any DHS component without a warrant.

**AI-powered social media surveillance (UAW/CWA/AFT lawsuit, October 2025)**: DHS, ICE, USCIS, and State Department hold contracts with Babel Street, ShadowDragon, and similar platforms that continuously monitor social media accounts of visa holders and lawful permanent residents. The persistent search function flags individuals automatically for all future content matching parameters — meaning once an organizer is flagged, all future content is monitored without a new query. Documented chilling effect: 60%+ of UAW members aware of the program changed their social media activity; 80%+ of non-citizen UAW members changed their activity.

**Congressional oversight response (March 2026)**: 72 senators and representatives signed a letter demanding DHS inspector general investigation of ICE's warrantless location data purchases. ICE is stonewalling congressional oversight. The legal landscape for organizer surveillance remains permissive — no court has yet enjoined the Penlink contract.

**Employer surveillance (non-government layer)**: Union-avoidance consultants use OSINT against organizing committees. GPS tracking of union vehicles, monitoring of company email/Slack for organizing activity, and NLRB case exposure if organizing communications are disclosed before petition filing. These employer tools operate entirely within current NLRA grey zones.

**ICE-employer coordination**: Documented cases of employers contacting ICE during organizing drives, using the enforcement threat to suppress organizing among undocumented workers. The NLRB's enforcement posture on this practice has weakened under the current administration.

**Technical readiness**: Moderate. Union IT departments are functional but often understaffed. Organizers are often non-technical but highly motivated. Training must be role-differentiated: organizers (communications security), stewards (member coaching), IT (infrastructure hardening), legal (documentation and privilege).

### 3.2 Network Structure

- National gateway: AFL-CIO (56 affiliated unions, 15M members as of January 2025 when SEIU rejoined)
  - AFL-CIO Technology Institute: dedicated program; Executive Director Lauren McFerran (as of February 2026); aflciotechinstitute.org
- Major affiliated unions with direct organizing security relevance:
  - SEIU (2M members, healthcare, property services) — rejoined AFL-CIO January 2025
  - UFW (100K+ members, agriculture — highest immigration enforcement exposure)
  - CWA / CODE-CWA (tech and media workers; active organizing in tech sector)
  - UFCW (joined AFL-CIO 2025; food processing — high immigrant worker concentration)
  - United Steelworkers (850K members, industrial)
  - Teamsters (independent; 1.4M members, logistics)

### 3.3 Decision-Makers

- AFL-CIO: Lauren McFerran (Technology Institute ED), National Organizing Department, IT Security Officers
- Individual unions: IT Director, National Security Officer, Organizing Department Director, General Counsel (for privilege questions)
- Regional: District Directors, Regional Organizing Coordinators

### 3.4 Customization Angle

**Operational security for organizing (SIGINT evasion)**: Signal for all organizing communications; need-to-know information architecture before petition filing; geofencing awareness (don't bring phones you use regularly to organizing meetings in sensitive locations; use dedicated organizing devices); Babel Street social media exposure reduction.

**Border and ICE hardening for immigrant worker organizing**: Penlink geofencing countermeasures (Faraday bags, burner phones for organizing events); ELITE address confidence score reduction (data broker opt-outs as union-wide practice); Palantir ELITE threat model as organizing education material for members.

**Whistleblower protection**: NLRB unfair labor practice charge documentation; encrypted communication channels for reporting labor violations; Signal for attorney communication.

**Union democracy transparency**: Frame all training in union democratic values — member participation in security decisions, transparency about threats, member-controlled security practices. Avoid the framing of top-down security mandates.

### 3.5 Contact Targets (8 Organizations)

| Organization | Role | Contact | Notes |
|---|---|---|---|
| AFL-CIO Technology Institute | National federation gateway | aflciotechinstitute.org | Lauren McFerran, ED; Workers First AI Summit (March 2026) — entry point for conversation |
| AFL-CIO National | Policy and organizing leadership | aflcio@aflcio.org | President Liz Shuler; frame around Penlink threat to member safety |
| SEIU National | 2M members, healthcare/property services | info@seiu.org | DC headquarters; Organizing Division is primary contact |
| UFW (United Farm Workers) | Agriculture; highest ICE enforcement overlap | media@ufw.org | Keene CA headquarters; corpus Part 0 immediately actionable for members |
| CWA / CODE-CWA | Tech sector organizing | info@code-cwa.org | Frame around employer surveillance and NLRB exposure; some members build surveillance tools |
| UFCW | Food processing; immigrant worker concentration | https://www.ufcw.org/contact/ | Washington DC; UFCW joined AFL-CIO in 2025 |
| United Steelworkers | Industrial; 850K members | info@usw.org | Pittsburgh PA; strong IT security baseline already in place |
| Teamsters | Independent; 1.4M, logistics | info@teamster.org | Washington DC; logistics sector = high location data exposure |

**Priority**: AFL-CIO Technology Institute first — a successful relationship there activates the full 56-union network without individual outreach to each affiliated union.

---

## Section 4: Election Worker Segment

### 4.1 Threat Model

The election worker threat model is infrastructure-security-first. Unlike DV survivors (intimate adversary) or labor organizers (government surveillance), election workers face adversaries targeting the administration of elections — not individual workers per se, though individual targeting (doxing, harassment) is a documented secondary threat.

**Ransomware targeting election infrastructure (primary threat, 2026 cycle)**: Election offices are local government entities, which represent the category most targeted by ransomware in Q1 2026 (Trend Micro, April 2026). The disruption model is not vote manipulation — it is paralyzing election administration: voter registration databases taken offline, election results websites downed, administrative email systems encrypted. The 2026 midterm cycle creates specific timing pressure. An October ransomware attack on a county election office could disrupt provisional ballot processing during the critical pre-election window.

**CISA defunding and federal support withdrawal**: As of May 2026, CISA has cut more than a third of its workforce and halted most programs working on elections — including red teams, incident response units, and regional election security advisors. The FY2027 budget proposes eliminating the election security program and EI-ISAC entirely. Trust between state election offices and CISA is "broken" (Votebeat, January 2026). When Iranian-linked hackers targeted Arizona systems in summer 2025, state officials did not report the incident to CISA, citing distrust. The corpus can position itself as a gap-filler for the coordination and training CISA previously provided.

**USB/bootloader attacks on election management systems**: Election management systems (EMS) are specialized software running on dedicated hardware. USB-delivered malware is a documented vector — introducing malicious USB drives into air-gapped EMS environments is a standard red team finding. Bootloader-level persistence (UEFI implants) can survive OS reinstallation. Poll worker access to these systems during high-volume election periods creates human-vector exposure.

**Insider threat (poll worker compromise)**: Poll workers are temporary staff, often recruited ad hoc, with limited background check capacity in many jurisdictions. CISA and EAC have published joint insider threat guidance; the 2026 environment makes it more relevant as jurisdictions operate with fewer trained staff. Insider threat vectors include: unauthorized USB device connection, credential sharing, unauthorized photography of sensitive materials, and social engineering of permanent staff.

**Phishing and credential theft**: Spearphishing targeting election administrators is a documented vector from 2016 (DNC/Podesta) through 2024. Election administrators receive legitimate-looking emails from fictitious county IT staff, vendors, and federal agencies requesting credential resets. Multi-factor authentication gaps remain common in underfunded county election offices.

**Doxing and personal harassment (secondary threat)**: 38% of election officials report personal harassment or threats (election-worker-opSec-supplement.md source data). Workers whose home addresses, family information, or political affiliations are exposed face physical safety risk. This is a different threat from infrastructure attack but affects the same population.

**Technical readiness**: Variable but generally moderate-to-low. State election offices typically have IT staff with formal security training. County offices are highly variable — some have dedicated IT, many do not. Poll workers are non-technical by definition. Training must be tiered: state-level IT-oriented for officials, simplified checklist-based for poll workers.

### 4.2 Network Structure

- Federal gateway: EAC (Election Assistance Commission) — sole federal agency with direct relationships to every election jurisdiction; provides cybersecurity resource library; contact via eac.gov
- Professional association gateway: NASED (National Association of State Election Directors) — 2026 President Mark Goins (Tennessee); direct peer network of 50 state election directors; nased.org
- Secondary: NASS (National Association of Secretaries of State) — 40+ chief election officials; communications contact Maria Benson, mbenson@nass.org
- State election offices: 50 state election directors, accessible via NASED membership directory
- County election officials: 3,000+ offices, reached through state election director cascade

### 4.3 Decision-Makers

- EAC: Executive Director, Commissioner for Cybersecurity (contact via eac.gov)
- NASED: President Mark Goins; Executive Director
- NASS: Director of Communications Maria Benson (mbenson@nass.org); Senior Director Brittany Hamilton (bhamilton@nass.org)
- State election directors: accessible via nased.org/members
- County officials: reached through state-level cascade after state director engagement

### 4.4 Customization Angle

**Hardware security — USB/bootloader hardening**: EMS-specific USB policy (disable autorun, inventory authorized drives, chain-of-custody for all devices in contact with election systems). BIOS/UEFI password protection, secure boot enabled. Physical tamper-evident seals on election system ports.

**Infrastructure-level opsec — credential compartmentalization**: Separate administrative accounts for election management systems (no shared credentials across staff). MFA on all EMS access (hardware key or TOTP, not SMS). Incident escalation procedures that do not depend on CISA (given trust breakdown): direct FBI liaison contacts, state CISO office, and EAC cybersecurity resources.

**Insider threat detection and prevention**: Physical access logs for EMS; two-person integrity rule for sensitive election procedures; USB device inventory audit before and after each election worker shift; anomaly reporting protocol for poll workers.

**Regulatory compliance angle**: The corpus meets or exceeds post-2020 election security baselines recommended by CISA (before defunding). Frame as both a security resource and a compliance documentation tool for jurisdictions maintaining their own security records in the absence of federal support.

### 4.5 Contact Targets (10 Organizations)

| Organization | Role | Contact | Notes |
|---|---|---|---|
| EAC (Election Assistance Commission) | Federal gateway | eac.gov / election-security page | Publishes cybersecurity resource library; corpus can be proposed as supplementary resource |
| NASED | 50 state election directors | nased.org | 2026 President Mark Goins (Tennessee); Brinson Bell (NC) in line for 2026 president per NCSBE |
| NASS | 40+ secretaries of state | mbenson@nass.org / bhamilton@nass.org | #TrustedInfo2026 initiative is an active outreach vehicle |
| California Secretary of State | Largest state | sos.ca.gov contact form | Approx. 6M registered voters to administer |
| Texas Secretary of State | 2nd largest | sos.texas.gov/contact/ | High ransomware risk due to legacy county systems |
| New York State Board of Elections | 3rd largest | info@elections.ny.gov | Albany NY; Board of Elections structure (dual party) |
| Florida Department of State / Division of Elections | 4th largest | dos.myflorida.com | Tallahassee FL; post-2020 heightened security investment |
| Defending Digital Democracy (D3P) — Harvard Kennedy School | Non-government training resource | Belfer Center, HKS | Runs election security tabletop exercises; does not depend on CISA; receptive to curriculum additions |
| Center for Democracy and Technology (CDT) | Midterm election security mapping | contact@cdt.org | Published "Countdown to the Midterms" (2026); framing ally |
| Votebeat | Investigative journalism / trust bridge | editors@votebeat.org | Covers election official security concerns; can amplify via coverage |

**Priority**: EAC first (resource library submission is the lowest-friction entry point). NASED second (peer-to-peer cascade from one state director to others). State secretaries of state are direct outreach targets for June–July 2026, before the fall election administration cycle begins.

---

## Section 5: Cross-Segment Strategic Notes

### The Network Effect Priority

The three segments have different network multiplier dynamics:

- **DV survivors**: NNEDV Safety Net Project is a single gateway to all 1,600+ member organizations. One relationship creates 1,600 distribution touchpoints. This is the highest multiplier ratio of any Tier 3 contact target.

- **Labor organizing**: AFL-CIO Technology Institute is a gateway to 56 affiliated unions. However, individual union organizing departments operate with significant autonomy — the Technology Institute endorsement signals credibility but does not guarantee adoption by each affiliate. Expect 10–15 affiliated unions to engage actively if the Technology Institute endorses.

- **Election workers**: The NASED peer network is highly effective but slow. State election directors are collegial; one state director who adopts the toolkit will mention it to peers at NASED conferences. Expect a 6-month adoption cycle from initial contact to meaningful multi-state uptake.

### The Timing Constraint

All three segments face a common timing pressure: the 2026 midterm election cycle begins its highest-activity phase in August–October 2026. For election workers, June–July 2026 is the optimal training window. For labor organizers, pre-election period organizing surges create urgency for communications security training in September–October. For DV survivors, no seasonal constraint applies — the Safety Net Project operates year-round.

**Recommendation**: Sequence outreach with election workers first (June 1) given the tightest timing window, DV survivors simultaneously (NNEDV has no seasonal constraint, and the need is constant), and labor organizers beginning June 22 to coincide with typical summer organizing campaign planning cycles.

### Tier 3 → Tier 2 Upgrade Path

Each Tier 3 segment has a natural upgrade pathway to Tier 2 advanced services:

- **DV survivors → Tier 2**: Institutional forensics and legal evidence preservation training for prosecutors, legal advocates, and victim service organizations doing formal legal case support. High value for courts and prosecution support units.

- **Labor → Tier 2**: Undercover infiltration countermeasures, deep-cover identity compartmentalization, advanced Signal network architecture for international organizing campaigns. Relevant for international union organizing departments and AFL-CIO solidarity programs.

- **Election workers → Tier 2**: Nation-state threat modeling, adversary-specific TTPs for election integrity specialists, state CISO-level briefings. Relevant for state election directors in high-target states (battleground states, states with active foreign adversary interest in election outcomes).

---

## Sources

- [NNEDV Safety Net Project](https://nnedv.org/content/technology-safety/) — Technology safety resources and state coalition directory
- [NNEDV State Coalitions Directory](https://nnedv.org/content/state-u-s-territory-coalitions/) — 56 state and territorial coalitions
- [Prism Reports — DHS Penlink PLX contract, April 2026](https://prismreports.org/2026/04/29/dhs-surveillance-location-data-penlink-plx/)
- [Citizen Lab — Penlink Webloc analysis](https://citizenlab.ca/research/analysis-of-penlinks-ad-based-geolocation-surveillance-tech/)
- [EFF — Labor unions/EFF lawsuit against ideological surveillance](https://www.eff.org/press/releases/labor-unions-eff-sue-trump-administration-stop-surveillance-free-speech-online)
- [Nextgov/FCW — CISA election security pullback, May 2026](https://www.nextgov.com/cybersecurity/2026/05/senator-warns-cisa-election-security-pullback-could-leave-midterms-vulnerable/413378/)
- [Votebeat — CISA election security trust broken, January 2026](https://www.votebeat.org/2026/01/15/cisa-election-security-trust-broken-trump-chris-krebs-denise-merrill/)
- [Trend Micro — US Public Sector threat intelligence Q1 2026](https://www.trendmicro.com/en_us/research/26/d/us-public-sector-under-siege.html)
- [Brennan Center — How federal government is undermining election security](https://www.brennancenter.org/our-work/research-reports/how-federal-government-undermining-election-security)
- [EAC Election Security Preparedness](https://www.eac.gov/election-officials/election-security-preparedness)
- [NASED — About and Members](https://www.nased.org/about-nased)
- [NASS — Election Administration and Security](https://www.nass.org/initiatives/election-administration-security)
- [AFL-CIO Technology Institute — Lauren McFerran announcement](https://aflciotechinstitute.org/news-media/lauren-mcferran-named-new-executive-director-afl-cio-tech-institute)
- [AirTag stalking statistics — Cybernews analysis](https://cybernews.com/editorial/apple-airtag-domestic-violence/)
- [Safety Net Project — Cell Phone Safety Plan](https://www.techsafety.org/resources-survivors/cell-phone-safety-plan)
- [The Register — 72 lawmakers demand probe into ICE data purchases, March 2026](https://www.theregister.com/2026/03/03/us_lawmakers_ice_data_purchases)
- [CDT — Countdown to the Midterms, 2026](https://cdt.org/insights/countdown-to-the-midterms-mapping-the-rapid-evolution-of-election-security/)
