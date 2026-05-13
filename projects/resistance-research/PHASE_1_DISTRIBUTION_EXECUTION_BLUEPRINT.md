---
title: "Phase 1 Distribution Execution Blueprint — All Three Paths (A / A+37 / B)"
created: 2026-05-13
updated: 2026-05-13
status: production-ready — awaiting final user path confirmation
version: 2.0
scope: "Comprehensive operational blueprint for all three distribution paths. Covers decision matrix, day-by-day calendars, sector message templates, Gist creation guide, email pre-fill templates for Domains 42/48/49/50, social media scheduling, success metrics dashboard, contingency playbook, pre-launch checklist, and outcome definitions."
reference_sources:
  - DISTRIBUTION_PATH_EXECUTION_GUIDE.md (Session 933 operational manual)
  - PHASE_1_EXECUTION_READINESS.md (Session 662 readiness audit)
  - PHASE_1_EXECUTION_BLUEPRINT.md (Session 967 confirmed A+37 execution)
  - execution/domain-42-email-template-may28-urgency.md
  - DOMAIN_EXPANSION_ROADMAP_PHASE_2_DOMAINS_44_50.md
  - DISTRIBUTION_PATH_ANALYSIS.md
note: >
  Path A+37 was confirmed May 13, 2026, 00:45 UTC. This document supersedes the prior
  PHASE_1_DISTRIBUTION_EXECUTION_BLUEPRINT.md (Item 28, produced earlier May 13) with the
  full multi-path reference requested. The PHASE1_DEPLOYMENT_MASTER.md remains the
  authoritative Day-1 runbook for the confirmed A+37 path.
---

# Phase 1 Distribution Execution Blueprint

**Date**: May 13, 2026  
**Path confirmed**: A+37 Hybrid (confirmed 00:45 UTC)  
**Hard external deadline**: May 28, 2026 — DEA-1362 hearing participation notice (Domain 42). This deadline is independent of path selection. Domain 42 Category A outreach must go out today (May 13) regardless of which path is chosen.

---

## Section 1: Quick-Reference Decision Matrix

| Parameter | Path A | Path A+37 Hybrid | Path B |
|-----------|--------|------------------|--------|
| **Philosophy** | Immediate full distribution | Full distribution + targeted election-org track | Research extension first, then distribute |
| **Time to first email** | 3–4 hours | 3–4 hours (Phase 1a) + 1–2 hrs Days 1–3 (Phase 1b) | 14–21 days research, then Path A calendar |
| **Total user time, Days 1–30** | 14–18 hours | 15–20 hours | 26–60 hours |
| **Number of waves** | 3 (Days 0–21) | 3 + Phase 1b election track (Days 1–3) | 3 compressed (Days 14–35 post-research) |
| **Sectors per wave** | W1: Think tanks/senators (6); W2: Law/policy (9); W3: Labor/civil society (10) | Same as Path A + 12 election orgs standalone | Same as Path A launched 14–21 days later |
| **Domain 42 DEA track** | Runs parallel, independent of path | Runs parallel, independent of path | Runs parallel — send Category A today |
| **May 30 DOJ consent decree window** | 17 days lead time (adequate) | 17 days + targeted election-org framing (strong) | 0–9 days (marginal to insufficient) |
| **August 7 NVRA margin** | 86 days (strong) | 83–85 days (strong) | 38–72 days (borderline to marginal) |
| **Domain 37 routing to election orgs** | Embedded in general send (moderate probability) | Standalone Phase 1b with docket-specific framing (high probability) | Delayed past May 30 window (low probability) |
| **Capital requirement** | Zero — all materials exist | Zero — one additional Gist creation required | Zero — research sessions add 26–42 hours |
| **Reversibility** | A → A+37 fully reversible Days 1–5 | A+37 → full-audience expand fully reversible | Non-reversible once committed |
| **Key deadlines** | Batch 1 by May 14; Wave 2 by May 21; May 28 DEA | Same + Phase 1b by May 16; May 28 DEA | Research checkpoint Day 14; distribute from Day 15 |
| **Success threshold (minimum viable)** | 25% Wave 1 reply; 3+ org engagement; 5+ media | Same + 3+ election org Domain 37 signals by May 30 | Same as Path A delayed |
| **Orchestrator verdict** | Viable if election-org connections exist already | RECOMMENDED — election-org precision at low cost | Only if strategic June anchor exists AND no May 30 urgency |

**Bottom line**: If in doubt, select Path A+37. The additional Phase 1b work (1–2 hours) is the cheapest available upgrade to the election-protection track before the May 30 and August 7 windows close.

---

## Section 2: Three Complete Calendar Variants

### 2.1 Path A: Day-by-Day Calendar, Days 0–21

**T+0 = Day of path decision. Reference assumption: decision confirmed May 13; execution begins May 14.**

**Day 0 (May 14) — Launch Day: 3.5–4 hours**

Pre-launch (30 min before clock starts):
- Verify all 6 canonical Gist URLs in incognito browser
- Confirm email client open, draft folder accessible
- Have YOUR_NAME, YOUR_CONTACT_INFO, Substack handle ready

08:00–08:30: Block 1 — Template configuration  
- Open scripts/fill_templates.py; set DISTRIBUTION_PATH = "A"  
- Set {{YOUR_NAME}}, {{YOUR_CONTACT_INFO}}, {{SUBSTACK_HANDLE}} in FIELD_VALUES  
- Set DRY_RUN = True; run; confirm zero warnings  

08:30–09:00: Block 2 — Template URL replacement  
- Set DRY_RUN = False; run fill_templates.py  
- Open scripts/filled_output/PHASE_1_EMAIL_TEMPLATES.md; verify zero remaining {{...}} strings  
- Verify published/README.md shows correct domain count (37+, not 22 or 28)  

09:00–09:30: Block 3 — Batch 1 contact re-verification (5 contacts, 6 min each)  
- Ryan Goodman: justsecurity.org/about-us — confirm ryan.goodman@nyu.edu or ryan@justsecurity.org  
- Wendy Weiser: brennancenter.org/about/leadership — confirm wweiser@brennancenter.org  
- Erica Chenoweth: hks.harvard.edu/faculty/erica-chenoweth — confirm echenoweth@hks.harvard.edu  
- Ian Bassin: protectdemocracy.org/team/ian-bassin — confirm ian@protectdemocracy.org  
- Marc Elias: democracydocket.com/about — confirm marc@democracydocket.com  

09:30–10:00: Block 4 — Per-email manual personalization  
- Goodman: note most recent Just Security article (visit site today)  
- Weiser: note most recent Brennan Center voting rights publication  
- Chenoweth: note most recent Nonviolent Action Lab working paper  
- Bassin: note most recent Protect Democracy filing or public statement  
- Elias: note most recent Democracy Docket active case  

10:00–10:30: Block 5 — Email draft preparation  
- Copy each email body from filled_output/PHASE_1_EMAIL_TEMPLATES.md  
- Fill manual placeholder from Block 4; select one subject line (A, B, or C)  
- Final read: no {{...}} strings, no broken Gist URLs, correct sign-off  

10:30–11:00: Block 6 — Tracking setup  
- Create Google Sheet: Tab 1 = Contacts (Name, Org, Email, Date Sent, Subject Variant, Response Date, Response Type, Notes); Tab 2 = Gist Views; Tab 3 = Media  
- Set email filter: all five Batch 1 addresses → label "Phase 1 Responses" + star  
- Record current Gist view counts (baseline)  

14:00–16:30: Block 7 — Substack and social media staging  
- Schedule Substack Post 1 for Day 3 (May 17), 10:00 AM ET  
- Stage Twitter Thread 1 for Day 1 (May 15), 08:00 AM ET  
- Stage r/law Reddit post for Day 2 (May 16)  
- Stage r/PoliticalScience post for Day 4 (May 18)  

16:00–18:30: Block 8 — Batch 1 send  
- 16:00 — Email 1: Ryan Goodman; log timestamp  
- 16:30 — Email 2: Wendy Weiser; log timestamp  
- 17:00 — Email 3: Erica Chenoweth; log timestamp  
- 17:30 — Email 4: Ian Bassin; log timestamp  
- 18:00 — Email 5: Marc Elias; log timestamp  
- 18:30 — Record Gist view counts (post-send snapshot)  

End of Day 0 check:  
[ ] 5 emails sent, timestamps logged  
[ ] 0 bounce notifications at 60 min post-send  
[ ] Substack Post 1 scheduled  
[ ] Tracking filter active  

**Days 1–5 (May 15–19) — Monitor, Stage, and Public Channel Launch**

Day 1 (May 15): Post Twitter Thread 1; check Batch 1 bounces; begin Wave 2 personalization (Stephanopoulos, Shams, McNicholas, Lydgate, Reynolds — 10–12 min each); send Domain 42 Category B emails (NAACP LDF, ACLU Criminal Law Reform, Sentencing Project)

Day 2 (May 16): Submit r/law Reddit post; continue Wave 2 personalization (Johnson, Gerken, Knight Foundation); send Domain 42 Category C academic outreach (Mason Marks — Yale Law, Ohio State Moritz, ACUS)

Day 3 (May 17): Substack Post 1 publishes at 10:00 AM ET; share on Twitter and LinkedIn; send Domain 42 Category D state AG outreach (Colorado, California, Michigan, Washington AGs)

Day 4 (May 18): Submit r/PoliticalScience Reddit post; confirm all Wave 2 emails have correct Gist URLs

Day 5 (May 19): Assess Wave 1 response rate — if below 20% reply, execute Contingency A (Section 8); post Twitter Thread 2

**Days 6–14 (May 20–28) — Wave 2 Send and Domain 42 DEA Deadline**

Day 6 (May 20): Domain 42 postal mail deadline (organizations submitting by post must postmark today); send Wave 2 Batch 1 (5 contacts: Stephanopoulos, Shams, McNicholas, Lydgate, Reynolds — 20-min spacing)

Day 7 (May 21): Publish Substack Post 2 (Domains 1–6 synthesis); send Wave 2 Batch 2 (4 contacts: Johnson, Gerken, Knight Foundation + one additional); submit r/electionreform Reddit post

Days 8–9 (May 22–23): Monitor Wave 2 bounces; begin Wave 3 personalization (AFL-CIO, SEIU, ACLU VRA, Lawyers' Committee VRP, NAACP LDF — 8–10 min each); Day 9 is Domain 42 email hard cutoff (do not send Domain 42 outreach after May 23)

Day 10 (May 24): Post Twitter Thread 3; publish Substack Post 3 (Domains 7–22 synthesis)

Day 14 (May 28 — Domain 42 DEA DEADLINE): Log which Domain 42 contacts filed participation notices; calculate Wave 1–2 response rate for Wave 3 personalization quality input

**Days 15–21 (May 29 – June 4) — Wave 3 Send**

Day 15 (May 29): Send Wave 3 Batch 1 (5 contacts: AFL-CIO, SEIU, ACLU VRA, Lawyers' Committee VRP, NAACP LDF — 20-min spacing)

Day 16 (May 30): DOJ consent decree advocacy window closes — note Domain 37 engagement signals; submit r/democracy Reddit post

Day 17 (May 31): Publish Substack Post 4 (Domains 23–37 synthesis)

Day 18 (June 1): HHS comment deadline (Domain 31 NVRA enforcement framing); send Wave 3 Batch 2 (5 contacts: Poor People's Campaign, OSF Fellowship, Democracy Fund, NEA/AFT, Substack public note — 20-min spacing)

Day 21 (June 4): OSF Fellowship application deadline (if pursuing); Phase 1 distribution complete; calculate aggregate response rates against Section 7 targets

**Send timing rules (all paths)**: Send institutional emails Tuesday–Thursday before noon recipient's local time. Schedule Reddit posts Monday or Tuesday morning. Schedule Substack posts Tuesday or Wednesday 10:00 AM ET. Twitter threads Tuesday–Friday 08:00–10:00 AM ET. Do not send institutional email Friday afternoon or Monday morning.

---

### 2.2 Path A+37 Hybrid: Day-by-Day Calendar, Days 0–21

Path A+37 executes the identical Wave 1–3 calendar as Path A, with two modifications: (1) each Phase 1a email includes the [PATH A+37] paragraph block; (2) Phase 1b runs Days 1–3 for 12 election protection organizations with a standalone Domain 37 send.

**Day 0 (May 14) — Launch Day: 4–5 hours**

Hours 0:00–3:00: Execute all Path A blocks above, with [PATH A+37] paragraph in each email

Hours 3:00–4:00 (Phase 1b prep):
- Block 9: Create Domain 37 standalone Gist (see Section 4 — 10 minutes)
- Block 10: Review each Phase 1b organization's current litigation/advocacy page — one active case per org connecting to a specific Domain 37 section (5 min per org, 7 Tier 1 orgs = 35 minutes)

Hours 4:00–6:30: Batch 1 send (identical to Path A)

**Day 1 (May 15) — Phase 1b Tier 1 Send**

09:00–11:00: Personalize 7 Tier 1 Phase 1b emails (approximately 5 min each beyond template). Pre-written subject lines are fixed — do not modify them.

14:00–16:45: Send 7 Phase 1b Tier 1 emails at 15-minute spacing:
- 14:00 — Wendy Weiser (Brennan Center Democracy Program)
- 14:15 — Marc Elias / editorial team (Democracy Docket)
- 14:30 — Ian Bassin (Protect Democracy)
- 14:45 — VRP Team (vrp@lawyerscommittee.org — Lawyers' Committee)
- 15:00 — ACLU Voting Rights Project (voting@aclu.org)
- 15:15 — Joanna Lydgate (States United Democracy Center)
- 15:30 — Common Cause (national)
Log all 7 sends in Phase 1b tracking tab (Tab 2 of Google Sheet)

Note on Weiser/Elias/Bassin: These contacts also appear in Wave 1 Phase 1a. Phase 1b is a different email, different subject, different framing. Opening: "Following up on the 35-domain framework I sent earlier today..."

**Day 2 (May 16) — Phase 1b Tier 2 Send**

Morning: Personalize 5 Tier 2 state-level Phase 1b emails (per DOMAIN_37_SEQUENCING_PLAN.md Tier 2)  
Afternoon: Send 5 Tier 2 emails at 15-minute spacing; log in Phase 1b tracking tab

**Day 3 (May 17): Phase 1b Complete + Substack Launch**

Verify all 12 Phase 1b sends logged; Substack Post 1 publishes; Domain 42 Category B outreach

**Days 4–21**: Identical to Path A calendar above

**Domain 37 vs. Standard Messaging by Sector and Week**

| Week | Sector | Gets Domain 37? | How |
|------|--------|----------------|-----|
| Week 1 Days 0–7 | Think tanks, Senators, Academia | YES — embedded via [PATH A+37] paragraph | General email references Domain 37 as separately routed to election orgs |
| Week 1 Days 1–3 | Election protection orgs (12) | YES — standalone Phase 1b | Direct Domain 37 targeted email with active-docket framing |
| Week 2 Days 7–14 | Law professors, Policy schools, Foundations | YES — embedded | Same [PATH A+37] paragraph block |
| Week 3 Days 14–21 | Labor unions | NO — not their primary use-case | Labor emails use Domain 17/23/31 emphasis only |
| Week 3 Days 14–21 | Civil rights orgs (ACLU VRA, NAACP LDF) | YES — explicit call-out | Civil rights emails include Domain 37 section reference |

**Phase 1b monitoring checkpoints (additional to Path A calendar)**:
- Day 7: Any Tier 1 contacts requesting Domain 37 follow-up or case-specific extracts?
- Day 14: Any contacts signaling Domain 37 integration into active litigation?
- Day 21: Pre-May 30 advocacy window traction — any organizations connecting Domain 37 to May 30 consent decree strategy?
- May 30: Which organizations acted before the window? Record as Phase 2 success indicators.

---

### 2.3 Path B: 14-Day Research Window + Accelerated Path A Distribution

**Path B is only viable if**: (a) a specific strategic June anchor exists (hearing, coalition meeting, grant deadline) AND (b) the May 30 advocacy window is not a priority. If both conditions are not met, choose Path A or A+37.

**Days 0–14: Research Phase (Priority Order — execute in sequence, not parallel)**

Day 0–2: Domain 25 update (FISA/Section 702 outcome)  
Confirm Senate vote on S.4344 or 45-day extension; document presidential signature date, warrant requirement as enacted; write 400–700 words. Cross-reference to Domain 37 surveillance infrastructure section.

Day 2–5: Domain 1 update (Voting Rights post-SAVE Act defeat)  
State SAVE Act analog wave current through May (which states, which stage); Arizona ballot initiative qualification outcome; write 700–1,000 words.

Day 5–8: Domain 19f update (War Powers/Iran — cannot begin until post-May 1 outcome confirmed in 3+ primary sources)  
Three scenarios: WPR compliance (blockade withdrawn), continued non-compliance (blockade maintained), or lapse (ceasefire collapsed). Document whichever materialized. Write 500–800 words.

Day 8–11: Domain 6 update (Judicial Independence)  
May–June circuit vacancy count (estimated 8 — verify); state AG enforcement coalition update; write 600–900 words.

Day 11–14: Domain 33 update (State Legislative Autocratization)  
May–June session adjournments; 2026 Secretary of State race landscape (primary outcomes through May); write 400–600 words.

**Day 14: Mandatory Launch Checkpoint**

Answer three questions in order:

1. Is May 30 advocacy window still open?  
   - If Day 14 = May 28: window has 2 days — launch immediately  
   - If Day 14 = May 23: window has 7 days — launch immediately if Domain 37 election-org framing matters  
   - If Day 14 = May 19: 11 days remaining — adequate; may continue to new domain research if strategically justified  

2. What is the NVRA August 7 margin (days remaining until August 7)?  
   - Below 75 days: launch immediately; no new domain research  
   - 75–85 days: one additional new domain is viable  
   - Above 85 days: one additional research sprint defensible  

3. Has a specific strategic June anchor been identified?  
   - If yes (coalition meeting, grant deadline, hearing): delay to anchor is justified if NVRA margin permits  
   - If no: launch immediately from Day 14  

**Days 15–35: Accelerated Path A Distribution**

Treat Day 15 (or Day 14 if checkpoint triggers immediate launch) as new T+0. Execute Path A calendar with compressed wave timing:
- Wave 1: Days 0–3 (not 0–5) — credibility-building time consumed by research phase
- Wave 2: Days 4–10 (not 6–14)
- Wave 3: Days 11–17 (not 15–21)

Path B framing note: add to all Path B emails — "Domain 25 (FISA) integrates the [outcome] confirmed [date]. Domains 19f and 33 reflect confirmed outcomes through [date]."

If new domain research is added (Days 14–55): Add at most one domain from candidates Domain 38 (Intelligence Oversight, 12–16 hours), Domain 39 (Reproductive Rights, 10–14 hours), or Domain 40 (Voting Systems Architecture, 8–12 hours). Adding all three pushes launch past Day 45 (June 27 at earliest), compressing NVRA margin below 6 weeks — inside the 6–8 week institutional adoption cycle.

---

## Section 3: Message Personalization Templates (Sector-Specific)

### 3.1 Law Schools and Policy Schools

**Domain emphasis**:
- Election law (Stephanopoulos, Goodman, Elias, Karlan): Domains 1, 33, 37
- Constitutional law (Chemerinsky, Yoshino, Baude): Domains 6, 29, 34, 35
- Policy schools (Skocpol, Fung, Hacker, Mettler): Domains 3, 9, 17, 18, 26

**Subject lines (5 variants)**:
- Option A: `[Specific domain concept tied to their recent publication] — research for [Clinic/Program name]`
- Option B: `Independent research: [domain name] analysis cites your work on [their specific contribution]`
- Option C: `[Domain name] analysis — potential citation resource for [recent publication title]`
- Option D: `[Framework concept] research: seeking [their institution] clinic review before wider distribution`
- Option E: `[Domain name] documentation for [active litigation] — framework for [organization name]`

**Body structure**: Open with a specific connection to their most recent published work (name the work, the specific claim, how your domain extends it). Follow with 3-4 sentences on the framework. One domain-specific paragraph naming the exact section and data point. Close with: feedback on the analysis from their expertise perspective; referral to colleagues at peer institutions; citation if the comparative evidence is useful in their work.

**Customization points**: [RECENT_PUBLICATION_OR_COURSE], [CLINIC_OR_PROGRAM], [THEIR_RESEARCH_AREA], [DOMAIN_1_PARAGRAPH], [DOMAIN_2_PARAGRAPH], [PATH-SPECIFIC BLOCK]

---

### 3.2 Think Tanks

**Domain emphasis**:
- Democracy-focused (Brennan Center, Protect Democracy, States United): Domains 1, 2, 26, 29, 33, 37
- Labor and economy (EPI, Roosevelt Institute): Domains 17, 18, 20, 5, 23
- Governance and accountability (Brookings Governance): Domains 2, 26, 34, 35, 6

**Subject lines (5 variants)**:
- Option A: `[Organization name]'s [recent publication] — [domain name] extends the analysis`
- Option B: `Testimony support for [upcoming hearing]: [domain name] comparative evidence`
- Option C: `[Domain name] framework — congressional testimony resource for [policy staff contact]`
- Option D: `Democratic institutions analysis: [domain count]-domain framework for [program name] review`
- Option E: `[Organization name] policy brief support: [domain name] international comparative record`

**Lead with the Litigation Tracker**: "The Litigation Tracker ({{LITIGATION_TRACKER_URL}}) is the element most immediately usable in testimony and policy briefs — active federal cases with court, status, and deadline, saving staff research time."

**Ask**: Circulation to relevant policy staff; citation in upcoming briefs or testimony; introduction to program officers at aligned foundations.

---

### 3.3 Labor Unions

**Domain selection by union** (do NOT pitch Domain 37 to labor contacts):
- All unions: Domain 17 (sectoral bargaining, PRO Act) as primary
- SEIU: Domain 31 (OBBBA Medicaid crisis for healthcare workers)
- CWA: Domain 8 (media workers, platform accountability)
- UAW: Domain 23 (tariff unilateralism, auto supply chain)
- AFSCME: Domain 2 (Schedule F, civil service dismantling)

**Subject lines (5 variants)**:
- Option A: `PRO Act and NLRB defense research — [domain 17 angle] for [union name] advocacy`
- Option B: `[Union name] member education resource: [domain name] — free for internal distribution`
- Option C: `NLRB capture timeline + sectoral bargaining evidence — legislative resource for [union name]`
- Option D: `[Specific issue they are working on] research: [domain name] for [union name] policy staff`
- Option E: `[Domain name] framework — testimony support for [upcoming labor hearing]`

**Body lead**: "The labor domain analysis (Domain 17) synthesizes the NLRB capture timeline, the PRO Act's current legislative pathway, and the international sectoral bargaining record. Available free for internal education, member communications, and legislative testimony with no restrictions."

**Union-specific paragraph** (select one and delete others): AFL-CIO: sectoral bargaining synthesis (Denmark, Austria, Germany) + Domain 2 civil service protection. SEIU: Domain 31 Medicaid cuts = 2.5M healthcare workers represented by SEIU + facility closure projections. UAW: Domain 23 tariff unilateralism = $9–14B annual cost increase to domestic auto production.

---

### 3.4 Civil Rights Organizations

**Domain emphasis**:
- NAACP LDF: Domains 22, 1, 14, 29
- Lawyers' Committee VRP: Domains 1, 33, 37
- ACLU: Domains 7, 1, 37, 29
- UnidosUS / Mijente: Domains 16, 22, 18

**Subject lines (5 variants)**:
- Option A: `[Organization name]'s [active docket type] docket + [specific domain] documentation`
- Option B: `[Domain name]: litigation support documentation for [case name or issue area]`
- Option C: `[Specific finding] — [domain name] analysis for [organization name] brief work`
- Option D: `[Constitutional challenge type] documentation: [domain name] for [litigation team]`
- Option E: `[Organization name] voting rights docket: [specific domain finding] for active cases`

**Body instruction**: Be specific enough that they can tell this is not a form letter — name the specific case, the constitutional provision, the data point. Show you have read their litigation record, not just their organization name.

**Ask**: Distribution to litigation team for the specific active case; feedback on which challenge pathways are most relevant to active dockets; introduction to allied coalition organizations for the comparative international evidence.

---

### 3.5 State Attorneys General

**Domain emphasis**: Domain 6 (state AG enforcement theory), Domain 33 (AG authority threats), Domain 37 (election interference mechanisms AGs can challenge), Domain 9 (federalism), Domain 35 (impoundment).

**Subject lines (5 variants)**:
- Option A: `[State] AG enforcement theory: [domain name] + state authority framework`
- Option B: `Multistate litigation research: [domain name] for [AG coalition name]`
- Option C: `[Domain name] federalism analysis — [state] AG office review`
- Option D: `State authority against federal [specific action]: [domain name] documentation for [state] AG`
- Option E: `[AG coalition active case]: [domain name] comparative evidence for [state] brief`

**Optimal send time**: Tuesday–Wednesday, 09:00–10:00 AM recipient's local time.

---

### 3.6 Media and Journalists

**Domain emphasis by beat**: National security/executive power reporters: Domains 28, 19f, 35, 6. Voting rights/election reporters: Domains 1, 33, 37, 42. Civil rights reporters: Domains 22, 29, 16, 14. Labor reporters: Domains 17, 23, 2. Courts reporters: Domains 6, 29, 34, 35 and Litigation Tracker.

**Subject lines (5 variants)**:
- Option A: `[Specific underreported angle] — sourced documentation for [reporter beat]`
- Option B: `[Domain name]: primary-source documentation on [specific story hook]`
- Option C: `Research for [recent article they published]: [new finding or data]`
- Option D: `[Specific data point] — [domain name] documentation for [publication name]`
- Option E: `Independent research: [story hook] with 54 primary source citations — for [beat reporter name]`

**Key instruction**: Name the specific underreported angle. "You can cite it, excerpt it, and use it as background freely. I don't need attribution for the compilation; I ask that primary sources are cited directly."

---

### 3.7 Election Protection Organizations (Path A+37 Phase 1b — Critical)

**Pre-written subject lines (fixed — do not modify):**
- Wendy Weiser / Brennan Center: `Domain 37: CISA destruction + HSGP conditionality — 2026 midterm interference briefing`
- Marc Elias / Democracy Docket: `Domain 37: 24 active DOJ voter roll cases + NVRA quiet period (Aug 7) — research for Democracy Docket`
- Ian Bassin / Protect Democracy: `Domain 37: HSGP leverage + election denier personnel network — connecting to your current work`
- Lawyers' Committee VRP: `Domain 37: DOJ consent decree clock (May 30) + Advocacy Window framework`
- ACLU Voting Rights Project: `Domain 37: Section 3 litigation prep + voter roll systematic challenge framework`
- Joanna Lydgate / States United: `Domain 37: state AG vulnerability + federal interference mechanisms — 2026 briefing`
- Common Cause: `Domain 37: SAVE Act error rates + August 7 voter roll removal window`

**Lead sentence by org type** (vary; delete inapplicable options):
- Litigation orgs (Democracy Docket, ACLU VRA, Lawyers' Committee VRP): "The 24-case DOJ voter roll litigation map documents active cases with court, status, and next deadline; the NVRA quiet period analysis (52 U.S.C. § 20507(c)(2) — August 7) provides the 90-day advance documentation needed for pre-period injunction preparation."
- Research/policy orgs (Brennan Center, Protect Democracy): "The CISA destruction timeline ($39.6M election security budget cut), EAC conditionality documentation, and 8 named election-denier officials currently in senior positions provide the institutional-capture narrative that contextualizes voter roll cases operationally."
- State AG networks (States United, Common Cause): "The HSGP grant conditionality mechanism and SAVE Act 81% false positive rate (24,000+ voters flagged nationally) are the two Domain 37 sections most directly applicable to state-level defensive litigation strategy."

**Direct ask — choose one per email**:
- Litigation ask: "Does the 24-case voter roll litigation map add anything to cases you are currently tracking?"
- Documentation ask: "Would the SAVE Act error rate documentation be useful as a standalone extracted document for brief filing?"
- Coordination ask: "Can you connect me to the staff member handling voter roll cases for a 20-minute call?"

---

## Section 4: Gist Creation Step-by-Step Guide

### 4.1 Zone A/D Structure Overview

Every public Gist follows this structure:
- **Zone A (Header)**: YAML-style metadata block — framework context, document identity, CC license, cross-links
- **Zone B (Body)**: Full document content, verbatim from source file, no edits
- **Zone D (Footer)**: "About This Document" block — related Gist links, research standard statement, currency note

### 4.2 Step-by-Step Gist Creation (10 minutes)

**Pre-creation checklist (2 minutes)**:
- [ ] Source file is current (check last-modified date in file header)
- [ ] Logged in to GitHub as esca8peArtist (check avatar top-right)
- [ ] Advocacy deadline is still in the future (do not create Domain 42 Gist after May 28)

**Step 1**: Navigate to https://gist.github.com/new

**Step 2**: Set filename field: `domain-{{NUMBER}}-{{kebab-case-title}}-2026.md`  
Examples: `domain-37-federal-executive-interference-2026-midterms.md` | `domain-42-drug-policy-democratic-legitimacy-regulatory-capture-2026.md`

**Step 3**: Set description field: `Domain {{NUMBER}} — {{Full Title}} | Democratic Renewal Research Framework | {{Advocacy deadline if applicable}}`

**Step 4**: Paste Zone A header block:
```
---
Research project: Democratic Renewal Framework ({{DOMAIN_COUNT}}-domain analysis, CC 4.0)
Document: Domain {{NUMBER}} — {{TITLE}}
Framework version: May 2026
License: Creative Commons Attribution 4.0 International (CC BY 4.0)
Full framework: https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261
Executive summary: https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4
Contact: {{YOUR_CONTACT_INFO — or leave blank}}
---
```

**Step 5**: Paste Zone B domain-context block immediately after Zone A:
```
---
**Domain**: {{NUMBER}} — {{TITLE}}
**Parent framework section**: {{PHASE_AND_CATEGORY}}
**Framework domains total**: {{DOMAIN_COUNT}} (as of May 2026)
**Advocacy windows**:
  - {{DATE_1}}: {{ADVOCACY_WINDOW_DESCRIPTION}}
  - {{DATE_2}}: {{ADVOCACY_WINDOW_DESCRIPTION — delete if no second window}}
**Cross-reference domains**: {{LIST_CROSS_REFERENCES}}
---
```

**Step 6**: Paste full document body verbatim from source file. Do not abbreviate any section.

**Step 7**: Paste Zone D footer after the Sources section:
```
---

## About This Document

**Part of**: The Democratic Renewal Research Framework ({{DOMAIN_COUNT}} domains, May 2026)
**Full framework**: https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261
**Executive summary**: https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4
**Litigation tracker**: https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0
**License**: Creative Commons Attribution 4.0 International.

**Other documents in this series**:
- First Amendment Suppression Tracker: https://gist.github.com/esca8peArtist/10d0a86e386e6c3c11c3830295a6503c
- Environmental Rollbacks Tracker: https://gist.github.com/esca8peArtist/87e2bdb931b77480e56a08044c567bc4
- Police Consent Decree Tracker: https://gist.github.com/esca8peArtist/1f5cb28527c98d12526c14302c725731

**Research standard**: All claims sourced to primary materials — court filings, congressional records, peer-reviewed research, official government documents. No anonymous sources used as primary evidence.

**Currency**: Current through {{LAST_UPDATED_DATE}}. Pending updates: {{PENDING_ITEMS — or "None"}}.
```

**Step 8**: Set visibility to Public. Click "Create public gist."

**Step 9 — Rendering verification (2 minutes)**:
- [ ] Zone A header renders as gray metadata block
- [ ] Zone B labels render as bold text
- [ ] Document H1 heading renders correctly
- [ ] Tables render with column borders
- [ ] Sources section renders as numbered list with working links
- [ ] Zone D footer renders after Sources section
- If tables render as raw Markdown: verify filename ends in .md not .txt

**Step 10**: Record Gist URL in DISTRIBUTION_GIST_URLS.md. Update email templates with live URL.

### 4.3 Cross-Linking Strategy

Every Gist links to: main proposal Gist, executive summary Gist (both in Zone A and Zone D), and litigation tracker, First Amendment, Environmental, and Police Consent Decree trackers (in Zone D only). Domain-specific Gists additionally cross-link to each other via the Zone B cross-reference field.

### 4.4 Public vs. Private Settings

All canonical and domain-specific Gists: Public (distribution is the purpose). Draft Gists during construction: Secret (convert to public only when Zone D footer is complete and rendering is verified).

### 4.5 Troubleshooting

**Gist URL returns 404**: Wait 60 seconds (propagation delay). If still inaccessible, check account status at github.com.

**Account suspended**: Appeal within 24 hours via GitHub support. If appeal will take more than 48 hours: create backup account, upload all canonical Gists, send Batch 1 contacts a follow-up email with new URLs.

**Tables render as raw Markdown**: Check filename extension is .md. Check for any unescaped `|` character inside a table row.

**Zone A block renders as plain text**: Expected behavior — GitHub Gists do not render YAML frontmatter as a styled box (unlike GitHub repository READMEs). The triple-dash-bordered block is correct.

**Fallback if GitHub unavailable entirely**: Use Google Docs (Share > Anyone with link > Commenter). For Substack-published domains, link to the Substack post URL.

---

## Section 5: Email Pre-Fill Templates (Domain-Specific)

### 5.1 Domain 42 Email Templates (DEA Hearing, May 28 Deadline)

**Domain 42 Gist**: https://gist.github.com/esca8peArtist/98dc61a3294a612482b37bd90f5c94ab  
**Filing address**: nprm@dea.gov — Docket No. DEA-1362  
**Hard cutoff for new outreach**: May 21 (7-day buffer before deadline)  
**Send days**: Tuesday–Thursday only, before noon recipient's local time  

**Subject lines by sector (5 variants each):**

Drug Policy Organizations:
- A: `DEA hearing participation deadline May 28 — Docket DEA-1362 — democratic design analysis of the regulatory capture problem`
- B: `[Organization name] — [X] days to DEA-1362 May 28 deadline — can we get you on the record?`
- C: `DEA-1362 briefing for [Organization name]: democratic exclusion architecture + Weill Cornell May 2026 disparity data`
- D: `[Organization name]'s [recent campaign] — Domain 42 democratic design analysis for DEA hearing participation`
- E: `NORML/DPA/MPP: Domain 42 hearing prep — regulatory capture + disenfranchisement feedback loop`

Civil Rights Organizations:
- A: `Democratic exclusion architecture of the drug war — briefing for [Organization name] on DEA-1362 hearing + felony disenfranchisement feedback loop`
- B: `Weill Cornell May 2026 data + DEA-1362 hearing — democratic design framing for [Organization name]`
- C: `[Organization name] — DEA hearing participation: racial disparity + political exclusion nexus`
- D: `DEA-1362 civil rights angle: felony disenfranchisement + drug enforcement feedback loop — [Organization name] briefing`
- E: `Drug war democratic exclusion: 4M disenfranchised voters + DEA scheduling capture — civil rights hearing brief`

Academic / Administrative Law:
- A: `Domain 42 draft — DEA regulatory capture analysis cites your work; would welcome methodological feedback before May 28 hearing`
- B: `Mason Marks / Ohio State Moritz: DEA-1362 hearing structure — APA procedural challenge analysis for review`
- C: `[Recent publication] + Domain 42: regulatory capture framework for DEA-1362 — academic review requested`
- D: `Administrative law analysis of DEA scheduling capture — methodological feedback before June 29 hearing`
- E: `Domain 42 APA procedural reform argument (Section 6.1) — review before June 29 DEA hearing`

State Attorneys General:
- A: `Domain 42 briefing — DEA-1362 hearing and federalism analysis for [State] AG office`
- B: `[State] AG and DEA-1362: 24-state democratic majority vs. federal scheduling — federalism analysis`
- C: `SAFER Banking letter + DEA-1362 hearing: Domain 42 federalism framing for [State] AG review`
- D: `[State] AG coalition: democratic legitimacy analysis for DEA-1362 participation — May 28 deadline`
- E: `DEA regulatory capture + 24-state democratic majorities: [State] AG hearing participation briefing`

**Reply handling**: If contact responds with interest in filing a participation notice, send the pre-drafted three-sentence participation notice template immediately (available in execution/domain-42-email-template-may28-urgency.md Section 6). Do not wait.

---

### 5.2 Domain 48 Email Template (Criminal Justice Civic Exclusion, June 5 Target)

**Note on naming**: In the production roadmap (DOMAIN_EXPANSION_ROADMAP_PHASE_2_DOMAINS_44_50.md), Domain 48 is Criminal Justice, Abolitionism, and the Civic Exclusion Architecture — not Surveillance Capitalism. Use Domain 37 (surveillance infrastructure section) for electoral manipulation framing, and Domain 51 (Campaign Finance, forthcoming) for surveillance capitalism. Templates below use the production-roadmap framing.

**Target organizations**: Brennan Center Justice Program, Movement for Black Lives Policy Table, Sentencing Project, Worth Rises, Color of Change, NAACP LDF

**Subject lines (5 variants)**:
- A: `Domain 48: criminal justice as civic exclusion architecture — research for [Organization name]`
- B: `4.4 million disenfranchised — felony restriction framework as democratic exclusion: [Organization name] briefing`
- C: `[Organization name]'s [active campaign]: Domain 48 civic exclusion analysis — SCOTUS OT2025 implications`
- D: `Criminal justice democratic exclusion: disenfranchisement + jury exclusion + employment barriers — [Organization name]`
- E: `Domain 48 framework for [Organization name]: civic exclusion architecture with 2026 midterm advocacy window`

**Body hook by organization type**:
- M4BL Policy Table: "The 4.4 million Americans disenfranchised by felony convictions are a structural democracy mechanism, not just a civil rights statistic: the communities most subjected to enforcement are underrepresented in the processes that set enforcement policy, in a self-reinforcing feedback loop. Domain 48 synthesizes this as democratic exclusion architecture."
- Brennan Center Justice Program: "Domain 48 bridges Brennan Center's 'Democracy and Justice' framing with the full civic exclusion analysis — jury exclusion (19 states permanently bar felony records), public employment restrictions (40,000+ federal job categories), and Worth Rises's $182 billion debt burden data. Available now if useful for the Democracy and Justice series."

**Ask options**: Research orgs: "Would Domain 48's civic exclusion synthesis be useful for [upcoming publication or testimony]?" Advocacy orgs: "Does this framing add anything to [organization name]'s [active campaign]?" Legal orgs: "Which of the challenge pathways in Section 6 are most relevant to your active dockets?"

---

### 5.3 Domain 49/31 Email Template (Healthcare-Democracy Nexus, June 1 HHS Deadline)

**Note on naming**: Domain 49 in the production roadmap is Environmental Justice. Healthcare-democracy content lives in Domain 31 (OBBBA Medicaid Restructuring, already complete). Templates below use Domain 31 with the NVRA enforcement theory angle for the June 1 HHS comment deadline.

**Target**: State AG offices in states with Medicaid expansion and Democratic AG

**Subject lines (5 variants)**:
- A: `OBBBA Medicaid + NVRA enforcement: healthcare access as voter registration infrastructure — [State] AG office`
- B: `Domain 31: OBBBA Medicaid restructuring — $700B cut + NVRA § 7 implications for [State] AG`
- C: `[State] AG NVRA enforcement theory: healthcare site voter registration at risk from OBBBA — June 1 HHS deadline`
- D: `OBBBA Medicaid work requirements: 3.3 million at risk + NVRA § 7 infrastructure — [State] coalition briefing`
- E: `Healthcare-democracy nexus: Medicaid cuts + NVRA voter registration enforcement — [State] AG research briefing`

**Body core argument**: NVRA Section 7 requires state public assistance agencies — including Medicaid offices — to offer voter registration at every transaction. The OBBBA work requirement provisions (Section 70215: 80-hour-per-month requirement) and biannual redetermination requirements (Section 70213) add administrative burden to Medicaid offices that are simultaneously NVRA Section 7 registration sites. When administrative capacity is strained by redetermination processing, NVRA compliance historically degrades first. A state AG coalition filing that Medicaid administrative overload constitutes a constructive NVRA Section 7 violation has standing under the NVRA's private right of action (§20510(b)).

**Ask**: Does [State] AG's office plan to file comments on the OBBBA Medicaid provisions before June 1? If the NVRA enforcement theory is useful, offer to extract Section 4 (enforcement pathways) as a standalone document for comment filing.

---

### 5.4 Domain 50 Email Template (Callais VRA Redistricting Emergency)

**Note on naming**: Domain 50 in the production roadmap is LGBTQ+ Rights. The Callais VRA redistricting emergency is covered in the litigation tracker (Category 10, entries 10.1 and 10.2) and Domain 1 (Voting Rights). Templates below address VRA redistricting using those primary documents.

**Target**: NAACP LDF, Lawyers' Committee VRP, ACLU VRA, Democracy Docket (already in Waves 1–2 for these orgs)

**Subject lines (5 variants)**:
- A: `Louisiana v. Callais redistricting cascade: Domain 1 + litigation tracker for [Organization name]`
- B: `Callais post-SCOTUS cascade: Alabama, Tennessee, Florida redistricting — prelim injunction research`
- C: `VRA redistricting emergency: Callais 2026 + Alabama stay + [active state] — [Organization name] briefing`
- D: `Domain 1 VRA analysis: post-Callais redistricting deadlines + preliminary injunction framework`
- E: `Redistricting litigation cascade post-Callais: Domain 1 + litigation tracker Category 10 for [Organization name]`

**Body core argument**: The Louisiana v. Callais redistricting cascade (SCOTUS denied delay of immediate effect; Category 10 in the litigation tracker) has created time-sensitive preliminary injunction opportunities in Alabama, Tennessee, and Florida. Domain 1's Section 4 documents the four states with active redistricting exposure and timeline constraints. The litigation tracker (Category 10, entries 10.1–10.2) documents Callais 2026 formal entries with court citations.

**Ask**: "Does the Callais cascade documentation add anything to your active redistricting tracking? I want to know if the tracker is missing cases — the goal is for it to be comprehensive."

---

### 5.5 Standard Wave Email (Mixed Domains 1–37)

**Subject lines (5 variants for A/B testing)**:
- A: `[Specific domain concept] — [domain count]-domain democratic reform framework for [Organization name]`
- B: `Independent research: democratic institutional erosion in comparative perspective — [domain count] domains, CC 4.0`
- C: `[Specific finding relevant to their work] — research framework for [Organization name] review`
- D: `[Their recent publication] + [Domain name] analysis: seeking feedback from [their institution]`
- E: `[Domain count]-domain democracy documentation framework — [litigation or policy angle] for [Organization name]`

**Body structure**: (1) Opening 2–3 sentences: specific connection to their most recent published work — name it, name the specific claim, name how your domain extends it. (2) Framework 3–4 sentences: what the framework is, why structured as it is, CC license. (3) Domain-specific 3–5 sentences: the 1–2 domains most relevant to their work, specific enough that it is clearly not a form letter. (4) Path paragraph: one of [PATH A], [PATH A+37], or [PATH B] — delete the other two. (5) Closing ask: one primary ask, one secondary ask, never more than two.

---

## Section 6: Social Media Scheduling Guide

### 6.1 LinkedIn Posting Strategy

**Timing by organizational size**:
- Large think tanks (Brennan Center, Brookings, EPI, Roosevelt): Monday and Wednesday 08:00–09:00 ET
- Medium NGOs and advocacy organizations: Tuesday and Thursday 09:00–10:30 ET
- Small civil society organizations: Thursday 14:00–16:00 ET
- Labor unions: Thursday 15:00–17:00 ET
- Academic contacts: Tuesday or Wednesday 10:00 AM

**Format**: Lead with the most specific finding, not the framework overview. 3–5 sentences maximum before "Read more:" link. 3–5 highly targeted hashtags — not hashtag spam.

**Hashtag strategy**:
- Domain 42: #DrugPolicy #DEAHearing #DemocraticReform #RegulatoryCapture #CivilRights
- Domain 1 / VRA: #VotingRights #VRA #DistrictingReform #ElectionProtection
- Domain 37: #ElectionIntegrity #VoterRolls #NVRADeadline #2026Midterms
- General: #DemocraticRenewal #ConstitutionalLaw #PolicyResearch #LegalResearch

**Tone variations**: Think tank posts: analytical, cite specific data. Civil rights org posts: connect to community impact, lead with human consequence. Labor posts: connect to worker power, not just procedural democracy. Legal posts: lead with constitutional question, not policy conclusion.

### 6.2 Twitter/Mastodon Threading Guide

**Thread structure (7–12 tweets)**:
1. Hook tweet: most counterintuitive or underreported finding
2. Context tweet: what the domain is and why it matters
3. Mechanism tweet: how it operates, cite primary source
4–7. Evidence tweets: 4 specific data points or cases, each sourced
8. International comparison tweet: what functioning democracies do differently
9. Reform architecture tweet: the three-tier proposal
10. Advocacy window tweet: what can be acted on now, specific deadline if applicable
11. Link tweet: Gist URL + full framework URL
12. Retweet request: "If useful, share with one person who works in [sector]."

**Hashtag discipline**: Lead hashtag at tweet 1 (one topical hashtag). Domain hashtag on link tweet (#DemocraticRenewal #OpenResearch). Maximum 3 hashtags per tweet.

**Mastodon federation strategy**: Primary servers: mastodon.social or scholar.social. Server targeting by domain: scholar.social for academic contacts; legal.social for legal contacts; kolektiva.social for labor and civil society. Posts federate automatically — you do not need accounts on every server. Use CW (content warning) for threads exceeding 5 tweets.

### 6.3 Short-Form Video Hook Scripts (10–15 seconds)

**Domain 42**: "The DEA is holding a hearing about whether marijuana should be Schedule I. The hearing will be run by DEA's own employees. DEA is judging whether DEA's authority should change. The deadline to get other voices in that room is May 28. Here's what that means for democracy." [Cut to: DEA-1362 deadline May 28]

**Domain 37**: "There are 24 active lawsuits challenging voter rolls in federal court right now. Most of them were filed by the Justice Department. Against voters. Here's what August 7th means." [Cut to: August 7 NVRA quiet period]

**Domain 1**: "Black Americans are arrested for marijuana possession at 3.6 times the rate of white Americans. They're also disenfranchised by those arrests at higher rates. So the people most affected by drug policy have less political power to change drug policy. That's not a coincidence." [Cut to: Weill Cornell May 2026 citation]

**Domain 29**: "The SPLC — the organization that tracks hate groups — was indicted by the federal government in April 2026. Here's what that has to do with democracy." [Cut to: SPLC indictment, April 21, 2026]

**Call-to-action variants (rotate)**: "The full research is free, linked in bio." / "The May 28 deadline is real. Link in bio for the DEA participation notice format." / "Share this if you think this is underreported."

### 6.4 Reddit Strategy and Cross-Posting

**Primary subreddits**: r/law (voting rights and election law focus; heavy moderation — frame as sharing a research resource, not self-promotion); r/PoliticalScience (democratic institutions; academic framing); r/electionreform (election administration and NVRA; high expertise, smaller community); r/democracy (democratic theory; structural analysis); r/progressive (civil rights and economic focus; lead with Domain 17 or 22)

**Cross-posting rules**: Post to r/law first (Monday morning); observe response before cross-posting. Do not cross-post the same thread to more than 3 subreddits on the same day. Adapt post title for each subreddit. Stage posts 2–3 days apart.

**Reddit post structure**: Title: specific finding, not framework overview ("Litigation Tracker 2026: 24 active DOJ voter roll cases with court, status, and next deadline" — not "Democratic reform research"). Body: 3–5 paragraph summary + link; do not paste the full document. Comments: respond to every substantive comment in the first 24 hours.

### 6.5 Timing Summary Table

| Channel | Sector | Best Day | Best Time (ET) | Frequency |
|---------|--------|----------|----------------|-----------|
| Email | Think tanks | Tue–Thu | 09:00–11:00 AM | Once per wave |
| Email | Civil rights orgs | Wednesday | 10:00–11:30 AM | Once per wave |
| Email | Labor unions | Tue or Thu | 09:00–10:00 AM | Once per wave |
| Email | State AGs | Tue–Wed | 09:00–10:00 AM | Once per wave |
| LinkedIn | Large think tanks | Mon and Wed | 08:00–09:00 AM | 2x/week during active waves |
| LinkedIn | NGOs | Tue–Thu | 09:00–10:30 AM | 1–2x/week |
| Twitter threads | All | Tue–Fri | 08:00–10:00 AM | 1 thread per wave |
| Substack posts | Public | Tue or Wed | 10:00 AM | Once per domain cluster |
| Reddit | Law/politics | Monday | 08:00–09:00 AM | 1 post per subreddit, 2 days apart |
| Mastodon | Academic | Tuesday | 10:00 AM | After Twitter thread |

---

## Section 7: Success Metrics and Monitoring Dashboard

### 7.1 Wave-Level KPI Targets

| Wave | Contacts | Reply rate target | Timeline | Contingency trigger |
|------|----------|-------------------|----------|---------------------|
| Wave 1 (Credibility anchors) | 5–6: Goodman, Weiser, Chenoweth, Bassin, Elias, Senate staff | 40–60% within 7 days | Days 0–7 | Below 20% by Day 7: Contingency A |
| Wave 2 (Institutional depth) | 9: Stephanopoulos, Shams, McNicholas, Lydgate, Reynolds, Johnson, Gerken, Knight | 25–40% within 10 days | Days 6–20 | Below 10% by Day 14: review subject line personalization before Wave 3 |
| Wave 3 (Civil society, labor) | 10: AFL-CIO, SEIU, ACLU VRA, Lawyers' Committee, NAACP LDF, Poor People's Campaign, OSF, Democracy Fund, NEA/AFT | 15–25% within 14 days | Days 15–35 | 15–25% is expected — do not treat as failure |
| Phase 1b (Path A+37 only) | 12 election orgs via Domain 37 standalone | 25–40% within 14 days | Days 1–16 | Below 15%: accelerate Domain 37 follow-up; do not add more orgs |
| Domain 42 DEA track | 10 DEA orgs across Categories A–D | 3+ participation notices filed by May 28 | May 13–28 | Below 1 filing by May 21: proactively send participation notice draft text |

### 7.2 Institutional Engagement Tracking Categories

For each contact, assign one of the following and update when it changes:
1. No response (after 14 days from send date)
2. Acknowledgment only ("thanks for sharing")
3. Interest signal (follow-up question, additional domain requested)
4. Referral signal (mentioned routing to colleague or team)
5. Implementation signal (referenced using it in specific work — testimony, brief, member education)
6. Public adoption (cited in published work, testimony, or public statement)

### 7.3 Policy Uptake Signals Tracker

Track each signal with: which contact/organization; date observed; specific publication or policy; which domain content used; how discovered (reply email / public statement / news coverage / secondhand referral).

| Signal type | Observable indicator | Detection method |
|-------------|---------------------|-----------------|
| Amicus brief | Court filing cites domain analysis | Google Scholar alerts; Democracy Docket brief tracker |
| Testimony | Senate/House committee record cites domain | Congress.gov witness testimony search |
| Comment filing | Regulatory docket includes domain citations | Regulations.gov search on DEA-1362 and other open rulemakings |
| Public statement | Organization press release or social post references domain | Google Alerts for key domain phrases |
| Newsletter inclusion | Domain linked or excerpted in organizational newsletter | Direct contact reply; subscribe to relevant org newsletters |
| Staff referral | Contact routes to colleague who then contacts researcher | Emails from new org addresses citing original contact |

**Google Alerts to configure**: "Democratic Renewal Research Framework" | "domain-42 DEA regulatory capture" | "NVRA quiet period August 7" | "SAVE Act false positive 81%" | "felony disenfranchisement feedback loop"

### 7.4 Google Sheets Dashboard Structure

**Tab 1: Contacts Master List**  
Columns: Name | Organization | Tier | Wave | Email | Date Sent | Subject Variant | Response Date | Response Type (1–6 scale) | Signal Category | Notes | Next Step

Auto-calc formulas:
- Wave 1 reply rate: `=COUNTIFS(D:D,"Wave 1",H:H,"<>")/COUNTIF(D:D,"Wave 1")`
- Days to reply: `=IF(H2<>"",H2-F2,"pending")`
- Signal conversion rate (categories 3+): `=COUNTIFS(I:I,">="&3,D:D,"Wave 1")/COUNTIF(D:D,"Wave 1")`

**Tab 2: Policy Uptake Signals**  
Columns: Date | Contact | Organization | Signal Type | Domain Referenced | Publication/URL | Discovery Method | Notes  
Auto-calc: Total adoption signals by domain; cumulative count by week; breakdown by signal type

**Tab 3: Media Mentions**  
Columns: Date | Outlet | Article Title | URL | Domain Angle | Citation Type (named/borrowed) | Estimated Reach | Notes  
Auto-calc: Total mentions by domain; weekly mention rate; outlet tier breakdown (Tier 1 national / Tier 2 policy / Tier 3 local)

### 7.5 Weekly Reporting Template (15–20 min/week)

**Week of**: ___________

Wave progress: Wave [X] sends this week: [number]. Cumulative Wave 1 reply rate: [X]% (target 40–60%). Cumulative Wave 2 reply rate: [X]% (target 25–40%).

Top 3 wins this week:  
1. [Specific engagement, adoption signal, or media mention]  
2. [Second win]  
3. [Third win or "none detected"]  

Early warning signals: [Any signal approaching contingency trigger, e.g., "Wave 1 reply rate 18% after Day 10 — approaching Contingency A threshold"]

Contingency triggers activated: [None / list triggers fired and response initiated]

Next week priorities:  
1. [Specific action item]  
2. [Specific action item]  
3. [Monitoring item]  

---

## Section 8: Contingency Activation Triggers and Responses

### 8.1 Contingency A: Low Wave 1 Reply Rate

**Trigger**: Fewer than 1 of 5 Wave 1 contacts has replied by Day 7 (below 20%).

**Diagnosis sequence (complete before responding)**:  
Step 1 — Delivery: Send one contact a test from a different address asking if they received it.  
Step 2 — Personalization: Re-read the opening paragraph. Could it apply to any researcher in that field? If yes, it was not personalized.  
Step 3 — Contact currency: Verify each of the 5 contacts is still at the listed institution (20% annual leadership turnover at advocacy organizations).  
Step 4 — Ask clarity: Was the closing ask specific and low-friction? "20-minute call" is lower friction than "detailed feedback."  

**Response by diagnosis**:
- Delivery/spam: Resend with modified subject (remove "advocacy," "action," "deadline" — common spam triggers). Test by emailing yourself first.
- Personalization failed: Rewrite opening paragraph per EMAIL_PERSONALIZATION_GUIDE.md. Do not move to Wave 2 until at least one Wave 1 response is received.
- Contact has moved: Identify new contact through institutional website; do not mark as failed until new contact is reached.
- Ask unclear: Add one specific ask to follow-up email (different subject, 7+ days after original): "Would 20 minutes by phone be feasible this week to discuss Domain 37's election litigation framework?"

Do not: Resend the same email without modification. Do not increase volume as a substitute for personalization quality. Do not send Wave 2 if Wave 1 reply rate is zero.

### 8.2 Contingency B: Key Organizations Do Not Reply by Day 7

**Trigger**: Any of 5 designated key organizations (Brennan Center, Protect Democracy, NAACP LDF, two Senate offices) have not replied within 7 days.

**Phone follow-up script**: "Hi, this is {{YOUR_NAME}}. I sent {{CONTACT_FIRST_NAME}} an email on {{SEND_DATE}} about a democratic reform research framework — subject line was [specific subject]. I'm following up because spam filters sometimes catch research emails from independent senders. If it didn't arrive, I can resend. My number is {{YOUR_PHONE}}."

If voicemail: send a follow-up email referencing the voicemail ("I just left a message...") with a link to the executive summary (not the full proposal).

**Escalation**: If primary contact has not replied and phone follow-up produces no response by Day 12, identify one additional contact at the same organization (different program director, press contact, or board member) and send cold outreach referencing the primary contact: "I sent [Primary Contact] research on [domain] earlier this month..."

### 8.3 Contingency C: Low Media Coverage

**Trigger**: Zero Google Alert detections by Day 10.

**Response sequence**:
1. Send a 500-word press release to 50 targeted journalists, leading with the most newsworthy specific finding. Subject line: `Research alert: [Specific finding] — primary-source documentation [current date]`
2. Pitch op-eds to Just Security (Goodman is a Wave 1 contact — follow up specifically on op-ed submission) and Lawfare Blog (150-word summary of the most legally significant finding)
3. Create a 3-part Twitter thread highlighting top three findings with media potential: (a) counterintuitive claim, (b) primary source evidence, (c) so-what for democracy. Post at 08:00 ET Tuesday.
4. Identify one relevant podcast and pitch a guest slot.

### 8.4 Contingency D: Organizations Request Modifications or Extensions

**Decision tree by request type**:

Minor modification (factual error, outdated statistic): Accommodate within 24 hours. Update source file and Gist. Note correction in domain's "Accuracy Note" section.

Major modification (changing analytical framing, adding policy position researcher does not hold): Flag for user consultation. Acknowledge receipt: "Thank you — could you identify the specific passage?" Then present to user with three response options (modify / decline with explanation / engage in dialogue).

Data request (underlying dataset, methodology documentation): Propose Q&A call rather than document modification. "The methodology and source citations are in the Sources section. Happy to do a 20-minute call to walk through it."

Extension request (more time to review): "Take all the time you need — no obligation attached to receiving this research. If you'd like to reconnect in [specific month], I can follow up then." Log with follow-up date.

### 8.5 Contingency E: Technical Failures

**High email bounce rate (above 10%)**:
- Do not send additional emails until diagnosis is complete
- Distinguish hard bounces (address does not exist — permanent) from soft bounces (mailbox full — retry in 24 hours)
- Hard bounces: visit org website today, find current email format, resend to verified address within 24 hours
- High bounce rate across multiple contacts: check whether your sending domain has been flagged as spam; test by sending yourself an email from a different provider

**fill_templates.py script fails**:
- Check error message. Most common failure: missing dependency (run `uv pip install`) or malformed FIELD_VALUES dictionary (mismatched quotes or brackets)
- If not fixed in 30 minutes: proceed with manual placeholder substitution in your text editor. Manual substitution takes 20–30 minutes and is fully equivalent to script output.

**Gist account suspended**: See Section 4.5 backup procedure above.

---

## Section 9: Pre-Launch Day 0 Checklist

**Contact and content verification**:
- [ ] All 5 Batch 1 contacts re-verified at institutional websites today (positions and email addresses current)
- [ ] {{RECENT_JUST_SECURITY_ARTICLE}} for Goodman: filled with specific title and date from today's check
- [ ] {{RECENT_WEISER_PUBLICATION}} for Weiser: filled
- [ ] {{RECENT_CHENOWETH_WORK}} for Chenoweth: filled
- [ ] {{BASSIN_RECENT_FILING}} for Bassin: filled
- [ ] {{ELIAS_RECENT_CASE}} for Elias: filled

**Gist verification (check all in incognito browser)**:
- [ ] Main proposal: https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261
- [ ] Executive summary: https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4
- [ ] Litigation tracker: https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0
- [ ] First Amendment tracker: https://gist.github.com/esca8peArtist/10d0a86e386e6c3c11c3830295a6503c
- [ ] Environmental rollbacks: https://gist.github.com/esca8peArtist/87e2bdb931b77480e56a08044c567bc4
- [ ] Police consent decree: https://gist.github.com/esca8peArtist/1f5cb28527c98d12526c14302c725731
- [ ] Domain 42: https://gist.github.com/esca8peArtist/98dc61a3294a612482b37bd90f5c94ab
- [ ] [PATH A+37 ONLY] Domain 37 standalone Gist created and URL recorded in DISTRIBUTION_GIST_URLS.md

**Script and template verification**:
- [ ] scripts/fill_templates.py: {{YOUR_NAME}} and {{YOUR_CONTACT_INFO}} filled (not placeholder text)
- [ ] DISTRIBUTION_PATH set correctly (A, A+37, or B)
- [ ] Dry run completed: zero {{...}} warnings in output
- [ ] 5 email drafts in email client with correct subject line selected per draft
- [ ] Each draft: no remaining {{...}} strings; both Gist URLs in body click-test to correct pages
- [ ] Each draft: path-specific paragraph shows only correct path block (other two deleted)
- [ ] published/README.md: domain count correct (37+, not 22 or 28)

**Email and tracking setup**:
- [ ] Email client filter: Batch 1 sender addresses → "Phase 1 Responses" label + star
- [ ] Google Sheets dashboard created (3 tabs: Contacts, Policy Uptake, Media)
- [ ] Gist view counts recorded (baseline)
- [ ] Google Alerts configured for 5 target phrases (see Section 7.3)

**Social media staging**:
- [ ] Substack Post 1 body in drafts, scheduled for Day 3
- [ ] Twitter Thread 1 ready for Day 1 manual post or scheduled send
- [ ] r/law Reddit post body ready

**Domain 42 specific (run today, May 13 — independent of path selection)**:
- [ ] Domain 42 Gist URL confirmed live (above)
- [ ] Category A emails (5 organizations) sent or queued for today
- [ ] Calendar reminder: May 21 = hard stop on new Domain 42 outreach
- [ ] Calendar reminder: May 28 = DEA participation notice deadline

**[PATH A+37 ONLY] Phase 1b specific**:
- [ ] Domain 37 standalone Gist created (Section 4.2 procedure)
- [ ] Domain 37 Gist URL recorded in DISTRIBUTION_GIST_URLS.md
- [ ] 7 Phase 1b Tier 1 email bodies ready for Day 1 afternoon send
- [ ] Pre-written Phase 1b subject lines confirmed (do not modify)
- [ ] Domain 37 Gist URL inserted into all 7 Phase 1b email templates

**[PATH B ONLY] Research phase specific**:
- [ ] Research sessions scheduled for Days 0–14 (calendar blocked)
- [ ] Day 14 checkpoint criteria confirmed (Section 2.3)
- [ ] NVRA August 7 margin calculated from planned launch date

---

## Section 10: Outcome Targets and Success Definition

### 10.1 Minimum Viable Success (any path)

- 25% of Wave 1 contacts (2 of 5–6) reply with substantive engagement within 14 days
- At least 3 organizations show any adoption signal (referral, use in internal work, citation) within 45 days
- At least 5 media mentions (Google Alert or manual discovery) within 45 days

If minimum viable threshold is not met by Day 30: do not proceed to Tier 2 outreach with unchanged messaging. Diagnose per Section 8 and revise.

### 10.2 Strong Success (any path)

- 50%+ Wave 1 reply rate within 14 days
- 10+ organizations show adoption signals within 60 days
- 15+ media mentions within 60 days
- 2+ policy uptakes (legislation introduced, regulation proposed, executive action corresponding to domain recommendation) within 180 days

### 10.3 Sector-Specific Targets

| Sector | Success threshold | Observable signal |
|--------|-------------------|-------------------|
| Law schools | 2 amicus briefs citing domain analysis | Court filings via Google Scholar or Democracy Docket |
| State AGs | 4 AG offices send comment letters or filing notices | Regulations.gov filings; direct contact reply |
| Labor unions | 3 unions integrate domain into member communications | Newsletter referencing domain; direct reply confirming |
| Civil rights organizations | 4 organizations coordinate testimony referencing domain | Senate/House committee records; direct contact reply |
| Election protection orgs (Path A+37) | 1 org uses Domain 37 SAVE Act error rate in emergency filing before August 7 | Democracy Docket brief tracker; ACLU press releases |
| Think tanks | 3 think tanks cite domain in published policy briefs or testimony | Google Scholar; congressional testimony search |
| Media | 2 national outlets (Lawfare, Just Security, or major newspaper) cite specific domain finding | Google Alerts; direct discovery |

### 10.4 Domain 42 Specific Success (Path-Independent)

**Minimum**: At least 1 organization files a DEA-1362 participation notice citing democratic design or regulatory capture framing consistent with Domain 42 arguments.

**Strong**: 3+ organizations file participation notices; at least 1 specifically on the felony disenfranchisement-electoral feedback loop dimension.

**Maximum**: Mason Marks or another administrative law expert agrees to testify at the June 29 hearing using Domain 42's APA procedural reform framework (Section 6.1).

**Monitoring**: Check regulations.gov Docket DEA-1362 after May 28. Public participation notices will be posted there. Read filed notices to see which organizations engaged and what framing they used.

---

## Appendix: Calendar Structures (CSV for Google Calendar / Outlook Import)

To import: save each CSV block as a .csv file. Google Calendar: Settings > Import > select file. Outlook: File > Open & Export > Import/Export > Import from another program > Comma Separated Values.

### Path A Calendar CSV

```csv
Subject,Start Date,Start Time,End Date,End Time,Description
"Domain 42 Cat A Send — TODAY",5/13/2026,10:00 AM,5/13/2026,11:00 AM,"Send to Drug Policy Alliance; MPP; NORML; LEAP; SSDP — independent of path"
"Day 0: Path A Launch Blocks 1-8",5/14/2026,8:00 AM,5/14/2026,6:30 PM,"Template config; Gist verify; contact re-verify; email draft; send Batch 1 at 30-min intervals 4pm-6pm"
"Day 1: Twitter Thread 1 + D42 Cat B",5/15/2026,8:00 AM,5/15/2026,10:00 AM,"Post Twitter Thread 1; send Domain 42 Category B (NAACP LDF; ACLU CL Reform; Sentencing Project)"
"Day 2: r/law + D42 Cat C",5/16/2026,9:00 AM,5/16/2026,11:00 AM,"Submit r/law Reddit post; Domain 42 Category C (Marks; Ohio State Moritz; ACUS)"
"Day 3: Substack Post 1 + D42 Cat D",5/17/2026,10:00 AM,5/17/2026,12:00 PM,"Substack Post 1 publishes; share on Twitter/LinkedIn; Domain 42 Category D state AGs"
"Day 5: Wave 1 Response Assessment",5/19/2026,9:00 AM,5/19/2026,10:00 AM,"Check Wave 1 reply rate; apply Contingency A if below 20%"
"Day 6: Wave 2 Batch 1 + D42 Postal Deadline",5/20/2026,9:00 AM,5/20/2026,12:00 PM,"D42 postal mail postmark deadline; send Wave 2 Batch 1 (Stephanopoulos; Shams; McNicholas; Lydgate; Reynolds)"
"Day 7: Substack Post 2 + Wave 2 Batch 2",5/21/2026,10:00 AM,5/21/2026,2:00 PM,"Publish Substack Post 2 (Domains 1-6 synthesis); send Wave 2 Batch 2 (Johnson; Gerken; Knight)"
"Day 9: Domain 42 Email Hard Cutoff",5/23/2026,9:00 AM,5/23/2026,9:30 AM,"No new Domain 42 outreach after today — 5-day buffer before May 28"
"Day 10: Substack Post 3 + Twitter Thread 3",5/24/2026,10:00 AM,5/24/2026,12:00 PM,"Publish Substack Post 3 (Domains 7-22); post Twitter Thread 3"
"Day 14: DEA DEADLINE (Domain 42)",5/28/2026,11:59 PM,5/28/2026,11:59 PM,"Final participation notices due to nprm@dea.gov — Docket DEA-1362"
"Day 15: Wave 3 Batch 1",5/29/2026,10:00 AM,5/29/2026,12:00 PM,"Send Wave 3 Batch 1: AFL-CIO; SEIU; ACLU VRA; Lawyers' Committee VRP; NAACP LDF"
"Day 16: DOJ Consent Decree Window Closes",5/30/2026,9:00 AM,5/30/2026,9:30 AM,"Note Domain 37 election org engagement signals; submit r/democracy Reddit post"
"Day 17: Substack Post 4",5/31/2026,10:00 AM,5/31/2026,11:00 AM,"Publish Substack Post 4 (Domains 23-37 synthesis)"
"Day 18: Wave 3 Batch 2 + HHS Deadline",6/1/2026,10:00 AM,6/1/2026,12:00 PM,"HHS comment deadline (Domain 31 NVRA framing); send Wave 3 Batch 2: Poor People's Campaign; OSF; Democracy Fund; NEA/AFT"
"Day 21: Phase 1 Complete + OSF Deadline",6/4/2026,5:00 PM,6/4/2026,6:00 PM,"OSF Fellowship application deadline if pursuing; calculate aggregate response rates"
"Day 22: Domain 48 Outreach Start",6/5/2026,10:00 AM,6/5/2026,11:00 AM,"Send Domain 48 (Criminal Justice/Civic Exclusion) to M4BL; Brennan Center Justice; Sentencing Project"
"August 7: NVRA Quiet Period",8/7/2026,12:00 AM,8/7/2026,12:00 AM,"NVRA 90-day quiet period begins — 52 USC 20507(c)(2) — monitor for systematic removal activity"
```

### Path A+37 Calendar CSV

```csv
Subject,Start Date,Start Time,End Date,End Time,Description
"Domain 42 Cat A Send — TODAY",5/13/2026,10:00 AM,5/13/2026,11:00 AM,"Independent of path — send today"
"Day 0: Path A+37 Launch (Blocks 1-8 + Phase 1b prep)",5/14/2026,8:00 AM,5/14/2026,6:30 PM,"All Path A blocks with [PATH A+37] paragraph; create Domain 37 standalone Gist; review 7 Tier 1 election org active litigation pages"
"Day 1 AM: Phase 1b Tier 1 Personalization",5/15/2026,9:00 AM,5/15/2026,11:00 AM,"Personalize 7 Tier 1 Phase 1b emails: Weiser; Elias; Bassin; LC-VRP; ACLU VRA; States United; Common Cause"
"Day 1 PM: Phase 1b Tier 1 Send",5/15/2026,2:00 PM,5/15/2026,4:45 PM,"Send 7 Phase 1b emails at 15-min spacing (2:00-4:30pm); log in Tab 2 tracking sheet"
"Day 2: Phase 1b Tier 2 + Reddit",5/16/2026,9:00 AM,5/16/2026,12:00 PM,"Personalize + send 5 Tier 2 state Phase 1b emails; submit r/law Reddit post; D42 Cat C"
"Day 3: Phase 1b Complete + Substack Post 1",5/17/2026,10:00 AM,5/17/2026,12:00 PM,"Verify all 12 Phase 1b sends logged; Substack Post 1 publishes"
"Day 7: Phase 1b Response Checkpoint",5/21/2026,9:00 AM,5/21/2026,9:30 AM,"Check Phase 1b reply rate (target 25-40%); any Domain 37 follow-up requests?"
"Day 14: Phase 1b Adoption Checkpoint + DEA Deadline",5/28/2026,9:00 AM,5/28/2026,10:00 AM,"Phase 1b: any contacts integrating D37 into active litigation? Also: DEA-1362 deadline today"
"Day 16: May 30 Consent Decree Check",5/30/2026,9:00 AM,5/30/2026,9:30 AM,"Which organizations acted before May 30? Record as Phase 2 success indicators"
"Day 21: Phase 1b Final Assessment",6/4/2026,5:00 PM,6/4/2026,6:00 PM,"Pre-August 7 advocacy window traction assessment for Phase 1b contacts"
"August 7: NVRA Quiet Period + D37 Emergency Watch",8/7/2026,12:00 AM,8/7/2026,12:00 AM,"Monitor for emergency injunction filings citing SAVE Act 81% false positive rate"
```

### Path B Calendar CSV

```csv
Subject,Start Date,Start Time,End Date,End Time,Description
"Domain 42 Cat A Send — TODAY regardless of path",5/13/2026,10:00 AM,5/13/2026,11:00 AM,"Path-independent — send today"
"Days 0-2: Domain 25 Research",5/14/2026,9:00 AM,5/16/2026,5:00 PM,"FISA/Section 702 outcome confirmation; write 400-700 words"
"Days 2-5: Domain 1 Research",5/16/2026,9:00 AM,5/19/2026,5:00 PM,"State SAVE Act analog wave current; AZ ballot initiative; write 700-1000 words"
"Days 5-8: Domain 19f Research (awaiting confirmation)",5/19/2026,9:00 AM,5/22/2026,5:00 PM,"Cannot begin until post-May 1 Iran WPR outcome confirmed in 3+ primary sources"
"Days 8-11: Domain 6 Research",5/22/2026,9:00 AM,5/25/2026,5:00 PM,"Circuit vacancy count; state AG coalition update; write 600-900 words"
"Days 11-14: Domain 33 Research",5/25/2026,9:00 AM,5/28/2026,5:00 PM,"May-June session adjournments; 2026 SoS race landscape; write 400-600 words"
"Day 14: MANDATORY LAUNCH CHECKPOINT",5/28/2026,9:00 AM,5/28/2026,10:00 AM,"Answer 3 questions: May 30 window open? NVRA margin? Strategic June anchor? Decision: launch immediately or continue research"
"Day 21: FORCE LAUNCH regardless of research",6/4/2026,9:00 AM,6/4/2026,5:00 PM,"Absolute deadline — launch Path A calendar from T+0 today. NVRA margin cannot be further compressed."
"August 7: NVRA Quiet Period",8/7/2026,12:00 AM,8/7/2026,12:00 AM,"Fixed legal deadline. If Path B launch was delayed past June 11: margin is now below 57 days."
```

---

*Blueprint prepared: May 13, 2026. Version 2.0, supersedes PHASE_1_DISTRIBUTION_EXECUTION_BLUEPRINT.md (Item 28, Session 933 era). Path A+37 confirmed May 13, 00:45 UTC. For the confirmed path, the primary execution runbook is PHASE1_DEPLOYMENT_MASTER.md. This blueprint provides the decision matrix, comprehensive message templates, and contingency playbook for ongoing operational reference.*

*Sources: DISTRIBUTION_PATH_EXECUTION_GUIDE.md (Session 933); PHASE_1_EXECUTION_READINESS.md (Session 662); PHASE_1_EXECUTION_BLUEPRINT.md (Session 967); execution/domain-42-email-template-may28-urgency.md (May 9, 2026); DOMAIN_EXPANSION_ROADMAP_PHASE_2_DOMAINS_44_50.md (May 9, 2026); DISTRIBUTION_PATH_ANALYSIS.md (May 5, 2026); DOMAIN_37_SEQUENCING_PLAN.md; execution/domain-42-gist-creation-steps.md; 52 U.S.C. § 20507(c)(2) (NVRA quiet period); 21 U.S.C. § 811 (Controlled Substances Act scheduling); Meinhofer et al., American Economic Journal: Economic Policy, May 1, 2026.*
