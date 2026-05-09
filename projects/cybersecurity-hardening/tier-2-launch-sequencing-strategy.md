---
title: "Tier 2 Launch Sequencing Strategy: Organizational Playbook Adoption"
project: cybersecurity-hardening
created: 2026-05-09
status: production-ready
phase: Phase 2 — Organizational Playbook Adoption
session: Exploration Queue Item (cybersecurity-hardening Phase 2 launch)
depends_on:
  - ORGANIZATIONAL_OPSEC_PLAYBOOKS.md
  - engagement-scoring-template.csv
  - phase-2-tier2-candidate-scorecard.csv
  - TIER2_MESSAGING_TEMPLATES.md
  - TIER2_DISTRIBUTION_PREP.md
  - phase-2-tier2-distribution-sequencing-strategy.md
  - phase-2-tier2-organizational-outreach-strategy.md
audience: Internal — Phase 2 launch sequencing and organizational outreach design
---

# Tier 2 Launch Sequencing Strategy: Organizational Playbook Adoption

**Bottom line**: Phase 1 Tier 1 individual distribution targets approximately 45 institutional contacts across law schools, immigration legal aid organizations, and civil society groups. Phase 2 Tier 2 shifts the unit of adoption from the individual recipient to the organization. A single organizational adoption at CLINIC (400+ affiliated programs), AFL-CIO Technology Institute (12.5 million members across 56 unions), or the ACLU (54 state affiliates) generates more reach than the entire Phase 1 individual distribution combined. This document answers five questions in sequence: which Tier 1 contacts graduate to Tier 2 invitees, which new organizations enter in Tier 2, what the organizational adoption pitch is, how the sequence runs week by week, and what success looks like.

---

## Section 1: Phase 1 Tier 1 Organizations That Graduate to Tier 2 Invitees

### The Three-Factor Readiness Score

At the Day 28 checkpoint after Phase 1 launch, each Tier 1 contact is scored on three factors using data from the `engagement-scoring-template.csv`. The scoring is binary on each factor — a point is earned or it is not. This is not a preference ranking. A 3/3 score triggers personalized pre-contact invitation; a 2/3 score triggers standard wave inclusion; a 1/3 score triggers conditional monitoring through Day 42; a 0/3 score means exclusion from Tier 2 until a second-round outreach window in Q4 2026.

**Factor A — Engagement Depth (0 or 1 point)**

Scoring threshold: a Day 7 or Day 14 engagement score of 3 or higher on the 0–5 engagement scale tracked in `engagement-scoring-template.csv`. Score 3 requires: confirmed read or open signal, click-through to the Gist corpus, and no bounce or decline. Score 4–5 requires a substantive reply — a question about specific sections, a forwarding confirmation with a named internal routing destination, or a request for additional materials. Factor A = 1 only at Score 3 or higher.

When tracking data is unavailable (web-form contacts, non-trackable delivery): a reply that references specific sections of the corpus by name counts as Factor A = 1 regardless of open/click data. A reply that says only "thank you" without specificity does not earn Factor A.

**Factor B — Integration Signal (0 or 1 point)**

Scoring threshold: the organization has explicitly or behaviorally indicated intent to integrate the corpus into operations, not just read it. Factor B = 1 requires one of: (a) an explicit statement of intent to share with staff, clients, or members; (b) a request for materials formatted for a specific operational context (intake, training, staff briefing); (c) a question about Part 0 implementation that implies active client or member use rather than abstract interest. "This is useful, will share" earns Factor B = 1. "Interesting, thank you" does not.

Organizations in the legal services sector can earn Factor B = 1 through litigation-relevant engagement: an attorney who asks whether the FOIA-sourced contracts are formatted for federal court citation has signaled adoption intent at the highest operational level.

**Factor C — Network Multiplier (0 or 1 point)**

Scoring threshold: the organization has documented national reach or a formal affiliate or member network that would receive the corpus through the adopting organization's internal channels without additional direct outreach from the sender. Factor C = 1 if the organization has either: (a) 10+ formally affiliated member or partner organizations in the same sector, or (b) a documented internal communications channel — newsletter, training infrastructure, conference, listserv — that reaches 50+ persons in the target population.

Factor C = 1 is automatic for the following Tier 1 organizations regardless of engagement data, based on structural network characteristics: CLINIC (400+ affiliated programs), NLG (national chapter structure), AFL-CIO Technology Institute (56 unions, 12.5M members), ACLU (54 state affiliates), NDWA (75 affiliates, 700,000+ members), EFF (Surveillance Self-Defense reach across the technical civil society sector), FPF (journalist training network), and IRE (NICAR conference pipeline).

### Provisional Tier 2 Readiness Scoring for Phase 1 Tier 1 Organizations

The following table assigns provisional Factor B and C scores based on pre-campaign structural knowledge from `phase-2-tier2-candidate-scorecard.csv`. Factor A is blank pending Day 28 engagement data. "Pre-contact" status means a 3/3 score is achievable if Factor A = 1 at Day 28; these organizations receive personalized individual invitations before the main wave send.

| Organization | Sector | Factor A (Day 28) | Factor B (provisional) | Factor C | Provisional Total | Tier 2 Status |
|---|---|---|---|---|---|---|
| CLINIC | Immigration legal aid | TBD | 1 (affiliate cascade) | 1 (400+ affiliates) | 2+ | Pre-contact if A=1 |
| AFL-CIO Technology Institute | Labor | TBD | 1 (AI Principles implementation) | 1 (56 unions, 12.5M members) | 2+ | Pre-contact if A=1 |
| ACLU Immigrants' Rights Project | Civil rights/legal | TBD | 1 (active litigation) | 1 (54 state affiliates) | 2+ | Pre-contact if A=1 |
| NDWA | Labor/immigration | TBD | 1 (member-facing urgency) | 1 (75 affiliates) | 2+ | Pre-contact if A=1 |
| Georgetown CPT | Academic/legal | TBD | 1 (research + clinic) | 1 (publication and litigation reach) | 2+ | Pre-contact if A=1 |
| Harvard Berkman Cyberlaw Clinic | Academic/legal | TBD | 1 (clinic case development) | 1 (academic publication reach) | 2+ | Pre-contact if A=1 (academic latency — confirm Day 28, not Day 14) |
| Access Now | Digital rights | TBD | 1 (Helpline direct client use) | 1 (Digital Security Helpline network) | 2+ | Pre-contact if A=1 |
| FPF | Journalist/press | TBD | 1 (training program integration) | 1 (journalist training network) | 2+ | Pre-contact if A=1 |
| IRE | Journalist/press | TBD | 1 (NICAR curriculum) | 1 (conference training pipeline) | 2+ | Pre-contact if A=1 |
| EFF | Digital rights | TBD | 0 (policy-only, no direct client use) | 1 (SSD reach) | 1+ | Standard wave if A=1 |
| NLG | Legal/civil rights | TBD | 1 (Mass Defense toolkit) | 0 (chapter structure, not federated cascade) | 1+ | Standard wave if A=1 |
| RAICES | Immigration | TBD | 1 (client-facing, Texas urgency) | 0 (regional) | 1+ | Standard wave if A=1 |
| EPIC | Digital rights | TBD | 1 (FOIA publication pipeline) | 0 (DC-focused) | 1+ | Standard wave if A=1 |
| STOP (Albert Fox Cahn) | Digital rights | TBD | 1 (NYC/ICE surveillance alignment) | 0 (city-level) | 1+ | Standard wave if A=1 |
| CMU CyLab | Academic | TBD | 0 (research, not client-facing) | 1 (academic publication) | 1+ | Standard wave if A=1 (academic latency) |
| UC Berkeley CLTC | Academic | TBD | 0 (policy research focus) | 1 (policy publication reach) | 1+ | Standard wave if A=1 (academic latency) |

**Interpretation**: Any organization with a provisional total of 2+ that confirms Factor A = 1 at Day 28 becomes a pre-contact candidate. Pre-contact candidates receive personalized individual invitations referencing their specific Phase 1 engagement, with a named organizational playbook and a proposed orientation session date. Standard wave candidates receive sector-appropriate personalization in the main Tier 2 send. Conditional (1+) organizations are monitored through Day 42 before a decision.

---

## Section 2: New Organizations to Introduce in Tier 2

Phase 2 Tier 2 introduces 30 new organizations not contacted in Phase 1. These are sector-specific targets: foundations that fund civil society security infrastructure, coordinating bodies that serve as force multipliers, and federation structures that cascade adoption through member networks. They are organized by sector priority, with the highest network-multiplier organizations listed first within each sector.

### Sector A: Foundations and Funders (8 organizations)

These organizations do not directly adopt the corpus — they fund the organizations that do. Outreach to funders at the right moment (after 3+ organizational adoptions are confirmed) can accelerate Phase 2 by providing resources for translation, training development, and staff time for adoption. Do not contact funders before organizational pilot adoptions are confirmed.

1. **Ford Foundation (Civil Society & Government Program)**: Funds immigration legal aid, civil rights litigation, and digital rights organizations across the full Tier 2 target list. Contact: civilsociety@fordfoundation.org. Timing: after Georgetown CPT or ACLU adoption is confirmed.
2. **MacArthur Foundation (Justice & Opportunity Program)**: Active funder of both immigration enforcement accountability and digital security infrastructure for at-risk populations. Contact: answers@macfound.org (inquiry form). Timing: after two organizational adoptions in legal services or immigration sectors.
3. **Open Society Foundations (US Programs / Democracy and Equality)**: OSF funds ACLU, NDWA, NLG, and most of the Tier 2 target list. A program officer referral from OSF transforms cold outreach to new organizations into warm introductions. Contact: info@opensocietyfoundations.org. Timing: after ACLU or NDWA adoption.
4. **Surdna Foundation (Strong Local Economies / Thriving Cultures)**: Funds labor organizing and immigrant worker organizations with a strong New York focus. Direct contact is difficult; best path is introduction through a funded organization (NDWA, RAICES affiliates). Timing: through NDWA relationship if established.
5. **Tides Foundation (Project Support)**: Fiscal sponsor and capacity builder for dozens of immigration, civil rights, and worker advocacy organizations. Contact through program staff. Timing: Month 2 of Phase 2, through an existing Tides project relationship.
6. **NoVo Foundation (Advancing Social Justice)**: Focuses on immigrant women and girls with worker justice organizing components. Relevant to NDWA and domestic worker organizing security. Contact: info@novofoundation.org.
7. **Unitarian Universalist Veatch Program (Social Justice Funding)**: Funds grassroots organizing including immigration rights. Faith-based funding infrastructure. Contact: veatch@uua.org. Relevant for faith-based network expansion in Month 3.
8. **Schmidt Futures / Eric and Wendy Schmidt Fund**: Funds technology and democracy initiatives including digital security infrastructure. Relevance increases if the corpus integrates into a formal tool or platform. Contact: info@schmidtfutures.com. Long-horizon target.

### Sector B: National Coordinating Bodies (10 organizations)

These organizations coordinate member networks without the automatic affiliate cascade of Sector A. They are high-value because a single adoption decision reaches tens of organizations and hundreds of practitioners.

9. **National Immigration Project (NIP) of the National Lawyers Guild**: Specifically focused on immigration law practitioners. Smaller than NLG national but more directly targeted to immigration attorney practice. Contact: info@nipnlg.org. Playbook 3 (Legal Services) is the direct match.
10. **American Immigration Lawyers Association (AILA)**: 15,000+ immigration attorney members. AILA integrates practical resources into its practice management guidance; Part 0 and Playbook 3 fit directly into their practitioner toolkit. Contact: aila@aila.org; target AILA's Practice & Professionalism Center.
11. **Association of Legal Aid Attorneys (ALAA) / Legal Services NYC**: Coordinates legal aid attorneys. Route through ALAA organizing committee. Contact: info@alaa-uaw.org. Playbook 3 is the match; subpoena response protocol is the entry hook.
12. **National Employment Law Project (NELP)**: Researches and advocates on worker rights; coordinates with worker center networks. Relevant for labor union sector and gig worker organizing security. Contact: nelp@nelp.org. Playbook 2 is the match.
13. **Interfaith Worker Justice (IWJ)**: Coordinates faith-rooted worker justice organizing across 25+ state affiliates. Bridges faith-based networks and labor organizing — a connector to both the faith-based expansion track and the labor organizing track. Contact: iwj@iwj.org.
14. **National Council of Nonprofits**: 25,000+ member nonprofits through state associations. Focuses on nonprofit governance and operations — Playbook 1's board-level governance framework (cybersecurity committee, data classification, subpoena protocol) fits directly into their member guidance. Contact: ncn@councilofnonprofits.org.
15. **National Center for Law and Economic Justice (NCLEJ)**: Focuses on economic justice and racial equity litigation; coordinates with legal services organizations. Contact: info@nclej.org. Playbook 3 and subpoena response protocol are the entry points.
16. **Center for Popular Democracy (CPD)**: Coordinates progressive grassroots organizing networks across 55+ partner organizations. Activist organizing and community safety focus. Contact: info@populardemocracy.org. Playbook 1 and activist organizing playbook are both relevant.
17. **Lawyers' Committee for Civil Rights Under Law**: Coordinates civil rights litigation across the legal sector. Direct relevance to ACLU-adjacent litigation on ELITE documentation. Contact: info@lawyerscommittee.org. Georgetown CPT introduction is the right path in.
18. **National Domestic Violence Hotline / DV organizational networks**: Coordinates DV service providers nationally. The DV survivor safety playbook (`phase-2-dv-survivor-safety-playbook.md`) makes this a Phase 2 expansion candidate. Contact via NDVH's organizational partnership program. Different playbook match than the four ORGANIZATIONAL_OPSEC_PLAYBOOKS but relevant to the broader Phase 2 corpus.

### Sector C: Federation Structures (12 organizations)

These organizations have explicit federated structures with member-to-member information sharing — the architecture that creates automatic cascade adoption when national-level adoption occurs.

19. **SEIU (Service Employees International Union)**: 2 million members, heavy healthcare and building services worker concentration. SEIU organizing in immigrant-heavy industries creates direct overlap with ELITE threat model. Contact: media@seiu.org; target SEIU Research Department for labor threat model documentation. Playbook 2.
20. **UFW (United Farm Workers)**: Agricultural workers, predominantly immigrant. ELITE targeting of agricultural communities documented. Contact: ufw@ufw.org. Playbook 2 with immigration-specific threat model is the match.
21. **CWA (Communications Workers of America)**: 700,000 members; strong technology worker organizing component. CWA's CODE-CWA chapter organizes tech workers directly relevant to surveillance infrastructure deployment. Contact: info@cwa-union.org. Playbook 2 with technical threat briefing.
22. **UFCW (United Food and Commercial Workers)**: 1.3 million members; grocery and food processing workers with high immigrant worker concentration. Direct relevance to ELITE enforcement in food processing communities. Contact: ufcw@ufcw.org. Playbook 2.
23. **LIUNA (Laborers' International Union of North America)**: Construction and public sector workers. Relevant in states with high construction enforcement. Contact: liuna@liuna.org. Playbook 2.
24. **National Council of La Raza / UnidosUS**: Largest Latino civil rights and advocacy organization. 300+ affiliated community-based organizations. Direct population overlap with ELITE targeting. Contact: info@unidosus.org. Playbook 1 (NGO/Nonprofit) + immigration surveillance playbook.
25. **National Alliance of Latin American and Caribbean Communities (NALACC)**: Coordinates 35+ Latino community organizations across 15 cities. Contact: nalacc@nalacc.org. Playbook 1; Spanish translation is prerequisite for integration into NALACC member network.
26. **Asian Americans Advancing Justice (AAJC) — National**: Coordinates four regional Asian American legal services affiliates. Contact: information@advancingjustice-aajc.org. Playbook 3 and Playbook 1.
27. **National Urban League**: 100 affiliate organizations in 36 states. Urban League affiliates provide workforce development and civil rights services in majority-Black urban communities. Contact: info@nul.org. Playbook 1 (NGO/Nonprofit) with financial account protection section relevant to community development finance.
28. **Coalition of Black Trade Unionists (CBTU)**: Coordinates Black union members across AFL-CIO affiliates. Bridges labor union and civil rights sectors. Contact: cbtu@cbtu.net. Playbook 2 with IRS financial targeting documentation.
29. **National Immigration Forum (NIF)**: Advocacy and communications infrastructure for immigration reform coalition. Media and framing capacity. Contact: info@immigrationforum.org. Playbook 1; relevant to organizational communications security section.
30. **Jewish Labor Committee (JLC)**: Labor organizing and civil rights coordination with faith-based and immigrant worker networks. Contact: jlc@jewishlabor.org. Bridges faith-based and labor sectors; relevant for Month 3 faith-network expansion.

---

## Section 3: Why "Organizational OpSec Capability" Is Compelling to Organizational Leaders

### The Argument That Works for Individuals Does Not Work for Organizations

Individual recipients of Phase 1 materials ask: "Is this useful for my situation?" Organizational decision-makers ask a different set of questions: "Does adopting this make my organization more effective at its existing mission? Does the commitment this requires fit our current capacity? Will my board and funders understand why we're doing this?" The Phase 2 pitch must answer all three without creating new cognitive load for already-stretched organizational leadership.

The Phase 1 pitch — "you face a documented surveillance threat and here are the countermeasures" — lands as mission-adjacent for individual practitioners. For executive directors and program directors, it can land as a new obligation in a context where obligations are already exceeding capacity. The Phase 2 shift is: "this threat is already affecting your mission outcomes, whether or not you address it — the question is whether you get to decide how."

### The Three Pillars of the Organizational Adoption Argument

**Pillar 1: The threat is already in the room.** Organizations serving undocumented immigrants, activists in organizing drives, domestic violence survivors, and workers in high-enforcement industries do not get to opt out of the surveillance landscape documented in the corpus. ICE's ELITE system is operational. The IRS LCA financial social-graph mapping treats financial relationships between organizations as investigation leads. The Palantir workforce surveillance contracts create risk for federal contractor organizing drives. None of this is conditional on the organization's decision about whether to address it. The decision that is available: whether the organization's clients and members have the tools to reduce their exposure before they arrive at the office.

**Pillar 2: Organizational adoption multiplies individual impact non-linearly.** A legal aid attorney who remembers to discuss data broker opt-outs with a client occasionally is a Tier 1 outcome. An organization that integrates Part 0 into its standard intake checklist walks every qualifying client through the process, without depending on attorney recall. One intake coordinator trained on the 20-minute Part 0 walkthrough reaches every client who comes through intake for as long as that coordinator is in the role. The multiplier is structural, not dependent on individual motivation. This is the argument that converts "we'll look at it" into "we'll integrate it."

**Pillar 3: Sector-specific playbooks are already built; adoption requires integration, not development.** The four organizational playbooks in `ORGANIZATIONAL_OPSEC_PLAYBOOKS.md` were built for the specific threat profiles of each constituency. A nonprofit executive director receives Playbook 1, which addresses board governance, IRS social-graph mapping, subpoena response, and financial compartmentalization. A union organizing director receives Playbook 2, which addresses employer surveillance detection, three-layer communication architecture, and strike fund protection. The specificity eliminates the "we'd have to adapt this" barrier. The question becomes "when can we schedule the orientation session," not "who will do the adaptation work."

### Sector-Specific Entry Points for Organizational Leaders

What makes the organizational adoption argument "click" is different in each sector. The entry point should match the threat that already costs the organization money, time, or mission outcomes.

**Nonprofit and NGO executive directors**: The entry point is governance liability. Board members have fiduciary responsibility for client data. A subpoena to an immigration NGO that arrives without a written response protocol costs the organization legal fees, board attention, and potential compliance failures. The corpus's subpoena response protocol and board-level cybersecurity committee structure are the answer to a question the board is likely already asking: "What happens when we get a government information request?"

**Labor union organizing directors**: The entry point is operational security for the campaign window. Organizing campaigns that are detected by employers before NLRA protections attach face termination, blacklisting, and NLRB complaint delays that can kill momentum. The three-layer communication architecture in Playbook 2 is not hygiene — it is operational discipline that determines whether the campaign survives the critical window before card check completion. "We've had campaigns compromised by communication failures" is the experience that makes this immediately relevant.

**Legal service providers and immigration attorneys**: The entry point is the DocketWise breach. In October 2025, DocketWise's immigration case management software exposed 116,000 clients' complete case files — names, addresses, case details, firm relationships. Playbook 3's file security architecture and client intake data minimization protocol are the answer to the question every immigration attorney asked in October 2025: "If this happened to us, how would we know, and what could we do differently?" That question has not been answered by most organizations. The corpus answers it.

**Academic institution administrators and faculty leadership**: The entry point is research integrity under federal defunding pressure. NSPM-33 compliance is mandatory for institutions receiving $50M+ in federal research funding. IRB data security obligations create legal liability for research groups handling sensitive human subjects data. The documented threat of federal agencies requesting data as a condition of defunding — the threat vector in the Stanford NIH case — is the institutional risk that makes Playbook 4 relevant to provosts and general counsels, not just IT staff.

---

## Section 4: Timeline and Sequencing

### Week 1 Post-Phase-1-Approval: Tier 2 Invitation Wave

**Day 1 (May 28 or equivalent date after Phase 1 launch)**: Run three-factor readiness scoring for all 45 Tier 1 contacts using Day 28 engagement data from `engagement-scoring-template.csv`. Generate four sub-lists: pre-contact (3/3), standard wave (2/3), conditional (1/3), exclude (0/3). Target completion: 2 hours.

**Days 2–5**: Draft and send personalized pre-contact invitations to the 3/3 list. No more than 2–3 invitations per day to preserve response management capacity. Each invitation references: (a) the specific Phase 1 engagement — name the question they asked or the section they requested; (b) the specific organizational playbook matched to their sector; (c) a proposed orientation session (60–90 minutes, bounded time commitment, specific dates in the 2-week window following); (d) one concrete organizational outcome the session will produce. Do not send a generic "I'd love to discuss" close. Name the deliverable.

**Day 7 (Decision gate)**: Is at least one orientation session confirmed? If yes, proceed with standard Tier 2 wave send. If no confirmed sessions after 7 days: delay wave by 1 week and re-contact pre-list contacts with an alternative subject line anchored to a time-sensitive policy hook (June 12 GSRA deadline or DocketWise breach anniversary framing for legal contacts).

**Concurrent with outreach (Days 1–7)**: Send Tier 2 invitations to the highest-priority new Sector B organizations (AILA, National Immigration Project, National Council of Nonprofits) — those with the tightest mission alignment and no prerequisite on Phase 1 engagement data. These new organizations are not on the 3-factor scoring model; their invitations are based on structural mission alignment and network multiplier.

### Weeks 2–3: First Responses, Orientation Sessions, and Feedback

**Week 2 start**: Send standard Tier 2 wave to all 2/3 candidates. Include a social proof element: reference at least one pre-contact organization that has confirmed adoption (identify the sector, not the organization by name until explicit permission is received).

**Weeks 2–3 (Orientation Window)**: Conduct organizational orientation sessions at a rate of no more than 3 per week. Session structure: 15 minutes threat model overview calibrated to sector, 30 minutes countermeasures walkthrough with the sector-specific playbook, 20 minutes on how the organization delivers the corpus to its own population (the mechanism they will use, not the aspiration), 15 minutes Q&A. Send a written summary within 48 hours. Confirm the 30-day check-in call at the close of the session.

**Week 2 checkpoint (mid-wave)**: Count response rates from the standard wave. Below 15% acknowledgment: diagnose subject line, personalization depth, and sector routing. If 4–5 score contacts appear in responses: flag immediately for expedited pre-contact follow-up; do not wait for the next wave cycle.

**Concurrent (Weeks 2–3)**: Send Tier 2 invitations to the Sector C federation structures (SEIU, UFW, UFCW, UnidosUS) that have the highest network multiplier value. These organizations have longer institutional response cycles; initiating contact in Week 2 sets up Month 2 response alignment.

### Month 2 (July 2026): Full Tier 2 Launch with Organizational Partnerships

**Week 1 (July 1–7)**: Process 30-day feedback from June orientation cohort. Triage within 72 hours. Incorporate confirmed factual errors or procedural gaps into v1.1 of relevant organizational playbooks. Begin quarterly threat model update research (Mobile Fortify, HART biometrics, post-SCOTUS DOGE/SSA status).

**Week 2 (July 8–14)**: Follow up with conditional (1/3) Tier 1 contacts. Some will have moved to Score 3+ with additional time; others can be sent materials without requiring orientation session commitment. The document-first approach — send the playbook directly and make the 30-day check-in the follow-up — is appropriate for organizations that did not initially schedule a session.

**Week 3 (July 15–21)**: Initiate outreach to Sector A funders (Ford Foundation, MacArthur, Open Society) with specific organizational adoption data — names of sectors with confirmed adoptions, number of organizations, and specific workflow integrations confirmed. Do not contact funders without concrete adoption data to present. A vague "several organizations have expressed interest" pitch will not move funders who are used to seeing those claims.

**Week 4 (July 22–28)**: Publish v1.1 organizational playbooks incorporating July feedback. Distribute quarterly threat model update to all active Tier 2 partners. Confirm Tier 3 outreach preparation is complete. Conduct 90-day check-in calls for the June onboarding cohort.

---

## Section 5: Success Metrics

The following metrics apply at four time horizons: Day 28 (transition gate), Month 1 (pulse check), Month 3 (directional assessment), and Month 6 (full evaluation).

### Primary Metric: Organizational Playbook Adoption Rate

The unit is an organization that has modified an operational workflow to include corpus content — not an organization that has read the corpus, attended an orientation, or expressed intent to adopt. Workflow modification means: intake checklist updated, staff training curriculum updated, communication protocol updated, or subpoena response protocol written using Playbook content.

- **Minimum threshold to proceed to Tier 3 planning**: 3 organizations with confirmed workflow modification, across at least 2 different sectors. Single-sector success does not validate the cross-sector strategy.
- **Target**: 6 organizations with confirmed workflow modification, across 3 sectors.
- **Strong outcome**: 9 organizations with confirmed adoption, including at least 1 national network (CLINIC, AFL-CIO, ACLU) and at least 1 academic institution. A national network adoption with automatic cascade is weighted equivalent to 5 individual organizational adoptions.
- **Hard ceiling on active partnerships**: 10 simultaneously. Above that, support quality degrades and adoption velocity slows as the sender becomes the bottleneck.

### Secondary Metric: Derivative Products from Organizations

Count of organizational materials (intake checklists, staff training curricula, member briefings, policy briefs) that cite or incorporate corpus content. These are the artifacts that make adoption durable beyond the initial orientation session.

- **Minimum**: 2 derivative products documented at Month 6.
- **Target**: 5 derivative products, from at least 3 organizations.
- **Strong**: 10 derivative products, including at least 1 published policy brief from an academic or civil rights organization citing the ELITE documentation.

### Tertiary Metric: Cross-References in Organizational Materials

Count of corpus citations in external organizational materials — policy briefs, litigation filings, training curricula, published resources. These are passive metrics (they do not require active tracking, only search monitoring).

- **Minimum**: 1 citation in an externally published document (any format) at Month 6.
- **Target**: 3 citations across different organizations and publication types.
- **Strong**: 5+ citations, including at least 1 in a federal court filing or formal policy submission.

### Quaternary Metric: Media References to the Framework

References to the corpus — or to the ELITE threat model it documents — in press coverage, trade publications, or academic publications. This metric is not actively pursued; it is a byproduct of organizational adoption by credentialed institutions.

- **Minimum**: 1 reference in any press or trade outlet by Month 6.
- **Target**: 3 references across legal press, security press, or immigration trade press.
- **Strong**: Coverage in mainstream press (New York Times, Washington Post, Reuters) or citation in a federal agency response document.

### Milestone: Self-Sustaining Distribution

The November 2026 checkpoint question: are Tier 2 organizations generating inbound referrals from organizations the sender did not contact, without prompting? Minimum signal: 1 inbound contact citing a Tier 2 organization as the source. If zero at November: diagnose adoption-without-propagation (organizations using materials internally but not amplifying) vs. adoption failure. These have different remedies — the former requires co-promotion infrastructure; the latter requires content revision.

---

*Created: 2026-05-09. The Day 28 engagement scoring in Section 1 cannot be executed until Phase 1 has been live for 28 days and engagement data has been populated in `engagement-scoring-template.csv`. Sections 2–5 are executable immediately and do not depend on Phase 1 engagement data.*
