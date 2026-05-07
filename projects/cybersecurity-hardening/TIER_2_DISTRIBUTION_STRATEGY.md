---
title: "Tier 2 Distribution Strategy: DV Survivors, Labor Organizers, Election Workers, Journalists"
project: cybersecurity-hardening
created: 2026-05-07
status: production-plan
phase: Phase 2 (Week 7+ launch, contingent on Phase 1 adoption gate)
author: research-agent
depends-on:
  - PHASE_2_SEQUENCING_STRATEGY.md
  - PHASE_2_SEQUENCING.md
  - TIER2_DISTRIBUTION_PREP.md
  - dv-survivor-safety-playbook.md
  - election-worker-opSec-supplement.md
  - journalist-security-playbook.md
  - activist-organizing-playbook.md
  - threat-model.md
  - opsec-playbook.md
---

# Tier 2 Distribution Strategy: Reaching DV Survivors, Labor Organizers, Election Workers, and Journalists

**Bottom line up front**: The existing Tier 1 and current Tier 2 distribution infrastructure (TIER2_DISTRIBUTION_PREP.md) reaches digital rights organizations, academic cybersecurity programs, security researchers, and journalist organizations — technically literate amplifiers who understand the government surveillance threat model the corpus is built around. This document addresses four distinct high-risk communities not yet mapped with concrete organizational contacts and outreach mechanics: domestic violence survivors and advocates, labor organizers and union members, election workers and poll monitors, and journalists and sources. These segments have different primary adversaries, different threat frames, and different distribution networks. The outreach strategy, content customization requirements, and success metrics for each are materially different from the existing Tier 2 pipeline and require their own execution plan.

**Timing gate**: This strategy launches no earlier than Week 7 post-Phase-1 Day 1, contingent on the gate criteria in PHASE_2_SEQUENCING.md Section 2 (minimum: 1,000+ cumulative Gist views, at least 3 Tier 1 organizations at Stage 2+ engagement, and at least one explicit request for Tier 2 materials from an institutional contact).

---

## Section 1: Tier 2 Audience Mapping

### Segment 1: Domestic Violence Survivors and Advocates

**Why this segment is a priority**

Domestic violence affects an estimated 10 million Americans annually — roughly one in four women and one in nine men experience severe intimate partner physical violence, sexual violence, or stalking by an intimate partner in their lifetime, according to the Centers for Disease Control. Surveillance is not a peripheral feature of abusive relationships: it is a primary control mechanism. Abusers use GPS tracking, stalkerware, shared family plan location data, connected vehicle telemetry, and smart home camera networks to monitor, control, and predict the movements of their partners. The NNEDV Safety Net Project's national survey data documents that 50% of victim service providers report that offenders use cellphone apps to stalk or monitor survivors.

The connection to this corpus is direct. The device hardening guidance in implementation-guide.md, the behavioral randomization in opsec-playbook.md, and the identity compartmentalization architecture in PHASE_2_SEQUENCING_STRATEGY.md Section 2.1 all address techniques that defeat surveillance — including intimate partner surveillance. The threat frame shifts, but the countermeasures are largely identical. GrapheneOS defeats stalkerware that requires OS-level access. Signal defeats interception of communications. Identity compartmentalization defeats the behavioral prediction that abusers rely on to locate survivors who have left.

**Specific threats to this segment**

The adversary in DV contexts has capabilities and access vectors unavailable to the government surveillance stack: they may have purchased and set up the device before the relationship became abusive; they may be the account holder on a family cellular plan with built-in location sharing; they may have installed stalkerware (FlexiSPY, Hoverwatch, mSpy, CocoSpy) that runs invisibly and persists through factory reset if it has root access; they may have legal ownership of shared financial accounts, cloud storage, and streaming services with shared device credentials. None of these access vectors require technical sophistication. They are features of mainstream consumer technology weaponized in an abusive context.

The DV-specific threat vectors not covered in the government surveillance model include: (1) shared Apple Family Sharing or Google Family Link with location access controlled by the abuser's account; (2) connected vehicle systems (OnStar, Hyundai Connected Services, Ford Pass) that report location to an account the abuser controls; (3) smart home devices (Ring cameras, Nest thermostats, smart locks) linked to accounts the abuser administers; (4) AirTag and Tile covert tracking devices that can be hidden in a survivor's belongings; (5) financial account monitoring through shared banking apps or linked cards. The dv-survivor-safety-playbook.md in this corpus addresses each of these in detail.

**Key distinction: safety planning precedes every technical action**

The critical operational difference that makes DV outreach materially different from every other segment in this distribution strategy: technical countermeasures that are safe and appropriate for a survivor who has already left an abusive situation can be catastrophically dangerous for a survivor who is still in the relationship or planning to leave. A stalkerware app that suddenly stops reporting can alert an abusive partner. A changed password on a shared account can trigger physical escalation. A Find My location that goes dark can provoke a dangerous response. Outreach materials for this segment must always foreground the safety planning framework first, and must direct survivors to the National Domestic Violence Hotline (1-800-799-7233, text START to 88788) and to local advocates before any technical steps.

**Organizations: 13 identified**

| Organization | Role | Contact | URL |
|---|---|---|---|
| National Network to End Domestic Violence (NNEDV) | National coalition; operates Safety Net Project and TechSafety.org | info@nnedv.org | nnedv.org |
| NNEDV Safety Net Project | Authoritative technology safety resource for DV context; Tech Summit 2026 | safetynet@nnedv.org | techsafety.org |
| National Domestic Violence Hotline | 24/7 crisis support; 56-coalition distribution network | info@thehotline.org | thehotline.org |
| Coalition Against Stalkerware | 40+ organization coalition linking tech security and DV advocacy | contact@stopstalkerware.org | stopstalkerware.org |
| National Coalition Against Domestic Violence (NCADV) | National umbrella; connects to state coalitions | publicpolicy@ncadv.org | ncadv.org |
| National Resource Center on Domestic Violence (NRCDV) | Technical assistance, training, research resource | nrcdv@nrcdv.org | nrcdv.org |
| Operation Safe Escape | Coalition Against Stalkerware founding partner; tech safety for DV survivors | contact via safeescape.org | safeescape.org |
| EndTAB (Ending Technology-Enabled Abuse) | Tech-facilitated DV training organization; Adam Dodge, CEO, is CAS Special Advisor | info@endtab.org | endtab.org |
| Washington State Coalition Against Domestic Violence (WSCADV) | Model state coalition; strong tech safety program | info@wscadv.org | wscadv.org |
| California Partnership to End Domestic Violence | Largest state coalition; serves large undocumented population relevant to corpus | info@cpedv.org | cpedv.org |
| Texas Council on Family Violence (TCFV) | Texas is the primary state gap identified in phase-2-prioritization-criteria.md | info@tcfv.org | tcfv.org |
| Domestic Violence Legal Empowerment and Appeals Project (DV LEAP) | Legal resource for DV survivors; intersection of legal process and tech evidence | info@dvleap.org | dvleap.org |
| VAWnet (National Resource Center on DV) | OVW-funded national resource library; library and dissemination infrastructure | vawnet@nrcdv.org | vawnet.org |

**Customization requirements for DV segment**

The threat frame in this segment shifts from government surveillance to intimate partner surveillance. The Fourth Amendment rights analysis that anchors the corpus's legal framing does not apply in private relationships: an intimate partner accessing a shared account is legally permitted to do so. This means the legal protection layer in the corpus's threat model is absent, and the risk calculus is different. The countermeasures (device hardening, encrypted communications, identity compartmentalization) are identical, but the sequencing is dictated by safety planning rather than threat severity. The existing dv-survivor-safety-playbook.md in this corpus handles this framing correctly and should be the primary distribution artifact for this segment — not the main implementation guide, which is calibrated for government surveillance contexts.

---

### Segment 2: Labor Organizers and Union Members

**Why this segment is a priority**

Labor organizing is a documented target of employer and law enforcement surveillance. Amazon collects real-time data on its warehouse employees and uses proprietary risk-scoring to flag stores with elevated unionization probability — a system confirmed in internal documents and litigation. The National Labor Relations Board has ruled that unilateral installation of workplace surveillance cameras is an unfair labor practice, but the NLRB's enforcement capacity in 2026 is significantly diminished under the current administration. Workplace monitoring software — keyloggers, email scanning, productivity surveillance, AI conversation monitoring — is in active use at a majority of U.S. employers, with documented cases of audio systems alerting management when workers say the word "union." Workers organizing a union are exercising a protected federal right under the NLRA; the surveillance infrastructure designed to suppress that activity is precisely the type of behavioral profiling that this corpus's countermeasures address.

The IRS LCA platform adds a government dimension: the corpus documents the IRS LCA platform's confirmed shift toward investigating "left-leaning groups," which includes labor advocacy organizations with financial relationships that may attract IRS scrutiny. The AFL-CIO's 2026 Workers First Initiative on AI has explicitly identified AI-powered workplace surveillance as a core labor rights issue, creating an organizational alignment between this corpus's threat model and the AFL-CIO's current advocacy agenda.

**Specific threats to this segment**

The primary adversary in labor organizing contexts is the employer. Specific documented threats include: (1) workplace monitoring software that scans email and internal messaging for union-related keywords; (2) AI conversation analysis tools that flag discussions among workers in breakrooms, bathrooms, and on production floors; (3) social media monitoring that identifies union sentiment and cross-references with employee rosters; (4) data broker sale of worker location data to private security firms retained by employers during organizing drives; (5) productivity surveillance tools that generate pretextual discipline records against workers identified as organizers; (6) cooperation between private security firms and local law enforcement, particularly during strikes and work stoppages.

The government surveillance dimension: USDA's April 2026 Palantir Foundry contract includes a $75 million workforce surveillance component for return-to-office compliance monitoring with real-time analytics — establishing the precedent that federal workforce surveillance is a Palantir product. This is directly relevant to federal employee union members. The IRS LCA platform's financial surveillance of organizations creates secondary risk for labor organizations with active IRS scrutiny.

**Organizations: 15 identified**

| Organization | Role | Contact | URL |
|---|---|---|---|
| AFL-CIO (national) | 12.5 million member national federation; Workers First AI initiative directly relevant | media@aflcio.org | aflcio.org |
| AFL-CIO Organizing Institute | Training arm for union organizers; 2026 Institute hosted by Minnesota AFL-CIO | info@aflcio.org | aflcio.org/about/leadership-structure/departments-and-committees/organizing-institute |
| Service Employees International Union (SEIU) | 2 million members; healthcare, janitors, security workers; active organizing drives | seiu@seiu.org | seiu.org |
| United Farm Workers (UFW) | Agricultural workers; documented surveillance targeting during organizing; intersection with immigration threat model | info@ufw.org | ufw.org |
| Industrial Workers of the World (IWW) | Member-run, horizontal structure; historically targeted by surveillance; active in gig economy organizing | general.secretary.treasurer@iww.org | iww.org |
| National Domestic Workers Alliance (NDWA) | Domestic workers, house cleaners, nannies; intersection with immigration and surveillance; active 2026 campaigns | info@domesticworkers.org | domesticworkers.org |
| United Auto Workers (UAW) | 400,000+ members; active organizing in new industries; legal disputes with management monitoring | uaw@uaw.org | uaw.org |
| Communications Workers of America (CWA) | Tech and telecom workers; CWA Code is organizing tech workers specifically | cwaweb@cwa-union.org | cwa-union.org |
| National Guestworkers Alliance | H-2A/H-2B guestworkers; intersection of labor organizing and immigration surveillance | contact via nwirp.org referral | nwirp.org |
| Jobs With Justice | Labor-community coalition; coordinates between labor and civil rights organizations | jwj@jwj.org | jwj.org |
| Strategic Organizing Center (SOC) | Union organizing coalition; data-driven analysis of labor threats | info@thesoc.org | thesoc.org |
| National Employment Law Project (NELP) | Worker policy and legal advocacy; intersection of labor rights and surveillance law | nelp@nelp.org | nelp.org |
| Georgetown Law Poverty Journal | Published analysis on labor organizing and AI surveillance (2026) | poverty-journal@law.georgetown.edu | law.georgetown.edu/poverty-journal |
| Interfaith Worker Justice | Faith-community support for labor organizing; broad worker center network | info@iwj.org | iwj.org |
| Centro de los Derechos del Migrante | Migrant worker rights; intersection of labor and immigration threat models | info@cdmigrante.org | cdmigrante.org |

**Customization requirements for labor segment**

The threat frame shifts from immigration enforcement to workplace surveillance. The corpus's government surveillance countermeasures apply indirectly — the behavioral profiling and metadata minimization guidance in opsec-playbook.md defeats employer surveillance of organizing activity at the communications layer, even though the adversary is an employer rather than ICE. Key customization requirements: (1) the corpus must be framed around BYOD policies and the specific risk of using work devices for organizing communications — the implementation guide's device compartmentalization section is the most relevant; (2) collective action security protocols require group-level opsec, not just individual hardening — Signal groups with verified membership for organizing coordination, with explicit guidance that management can legally monitor work-issued devices but cannot monitor personal devices in most circumstances; (3) the NLRA legal framework for protected organizing activity should be noted — workers have legal rights that do not exist in the immigration context, and understanding what is legally protected shapes the risk calculus; (4) the activist-organizing-playbook.md already addresses protest and direct action security, but labor organizers need supplemental guidance on workplace-specific digital hygiene (personal phone for organizing communications, not work phone; separate work email from organizing email; do not discuss organizing on employer's network).

---

### Segment 3: Election Workers and Poll Monitors

**Why this segment is a priority**

Election workers face documented, escalating threats. A Brennan Center survey of local election officials found that nearly one in four officials is concerned about being assaulted at home or at work, 52% reported concern about the safety of their colleagues and staff, and more than half worried that threats, harassment, and intimidation would make it more difficult to retain or recruit election workers in the future. Doxxing — the public posting of election officials' personal addresses, phone numbers, and family information — is a documented and recurring tactic that has driven experienced officials out of their positions in multiple states. Swatting of election officials' homes has been documented.

The federal support gap created by CISA is significant for this segment. CISA lost approximately 130 workers in February 2026, including the election security advisers who had built institutional relationships with state and local election offices over several election cycles. The FY2027 budget proposal eliminates the election security program entirely. A Senate Intelligence Committee warning (May 2026) confirms that state and local officials have reported that CISA is no longer providing election security training, intelligence sharing, or cybersecurity assistance at the levels offered in prior cycles. 61% of local election officials are specifically concerned about the impact of CISA cuts. This gap creates both a need and an opportunity: the corpus's communications security and identity compartmentalization guidance directly addresses the harassment and doxxing threat that election workers face, and there is no longer a competing federal resource providing this guidance.

**Specific threats to this segment**

The primary adversary in election worker contexts is organized political harassment, not government surveillance. Specific documented threats include: (1) doxxing campaigns that harvest personal information from public voter records, property records, and social media to post election workers' home addresses and family information; (2) coordinated harassment via phone, email, and social media from organized partisan networks; (3) false information campaigns that attribute fraud to specific election workers, generating secondary threats; (4) physical surveillance of polling locations and vote-counting facilities by hostile observers; (5) insider exploitation — the risk that motivated hostile actors may attempt to become election workers or observers specifically to disrupt or document procedures; (6) social engineering targeting election officials' personal accounts to access official systems through credential theft.

Poll monitors conducting election integrity observation have a distinct threat profile: they are often volunteers with minimal training, operating in contested political environments, and may be recording potentially controversial events. Their digital security posture must support both personal protection and evidentiary chain-of-custody for observations they document.

**Organizations: 11 identified**

| Organization | Role | Contact | URL |
|---|---|---|---|
| U.S. Election Assistance Commission (EAC) | Federal resource for election workers; Election Official Security page; Poll Worker Best Practices | eac@eac.gov | eac.gov/election-officials/election-official-security |
| National Association of State Election Directors (NASED) | State-level election director professional network; annual conference | info@nased.org | nased.org |
| National Association of Election Officials (Election Center) | Professional association for election officials | electioncenter@electioncenter.org | electioncenter.org |
| Brennan Center for Justice | Research on election worker threats; How Federal Government Is Undermining Election Security (2026) | press@brennancenter.org | brennancenter.org |
| Common Cause | Election Protection program; poll monitor coordination; 866-OUR-VOTE hotline | common.cause@commoncause.org | commoncause.org/issues/election-protection |
| League of Women Voters | Poll observer coordination; voter protection programs; 56-state network | lwv@lwv.org | lwv.org |
| Election Protection (866-OUR-VOTE Coalition) | Nonpartisan poll monitoring network; coordinates monitor training and dispatch | info@protectthevote.net | protectthevote.net |
| Issue One | Bipartisan election integrity; published Protecting America's Election Workers | info@issueone.org | issueone.org |
| Verified Voting | Election technology security; source of technical expertise for election official outreach | info@verifiedvoting.org | verifiedvoting.org |
| Center for Election Innovation & Research (CEIR) | Election official support programs post-CISA drawdown | info@electioninnovation.org | electioninnovation.org |
| Votebeat | Election-focused journalism outlet; covers election worker threats and CISA drawdown in depth | contact via votebeat.org | votebeat.org |

**Customization requirements for election worker segment**

The threat frame for this segment is political harassment and insider exploitation, not government surveillance. Election workers cannot use identity concealment — their names are often public record as part of the election administration process. The countermeasures focus on separating personal identity from professional election identity, hardening personal accounts against credential theft and harassment, and establishing secure team communications for poll monitor networks. Key customization points: (1) the identity compartmentalization guidance in PHASE_2_SEQUENCING_STRATEGY.md applies, but with the constraint that election workers cannot use pseudonyms professionally — the goal is separation, not concealment; (2) Signal groups for poll monitor coordination networks address the team communications need; (3) the EAC's existing Google PII removal resource should be noted alongside the corpus's data broker opt-out guidance — both address the doxxing threat through different mechanisms; (4) election worker security must be compatible with election IT infrastructure, which is typically government-managed and not under the worker's control — the corpus's guidance on personal device hardening applies but must be explicit that election systems themselves are out of scope. The election-worker-opSec-supplement.md in this corpus provides the correct framing for this audience and is the primary distribution artifact.

---

### Segment 4: Journalists and Source Protection

**Why this segment is a priority**

The existing TIER2_DISTRIBUTION_PREP.md targets journalist organizations — IRE, CPJ, SPJ, Freedom of the Press Foundation — as part of the original Tier 2 pipeline. This section maps that coverage and identifies what is distinct about journalist-specific distribution compared to the other new segments in this strategy. Journalists are not a gap in the existing Tier 2 pipeline; they are a segment where existing work should be extended with more granular organizational contact and outreach mechanics.

The 2026 press freedom environment is materially deteriorating. The U.S. Press Freedom Tracker documented long and severe press freedom aggressions in January 2026 alone. The threats are specific and documented: CBP device search authority at all international border crossings without warrant (CBP Directive 3340-049B revised January 2026); PRISM (Section 702 FISA) compelled access to journalist communications with foreign sources; NSL compelled metadata disclosure from carriers without judicial authorization; Babel Street persistent monitoring of journalist public social media. These are operational capabilities, not emerging risks.

The source protection dimension distinguishes journalists from every other segment: the adversary's goal is not just to surveil the journalist but to identify and prosecute the journalist's confidential sources. This requires a security posture calibrated to the source-protection problem, which is addressed in detail in journalist-security-playbook.md but not in the main corpus.

**Organizations: 10 identified**

| Organization | Role | Contact | URL |
|---|---|---|---|
| Freedom of the Press Foundation (FPF) | SecureDrop operator; 2026 Digital Security Checklist; Digital Security Training team available | info@freedom.press | freedom.press |
| Investigative Reporters and Editors (IRE) | 6,000 member investigative journalism association; NICAR conference digital security training | info@ire.org | ire.org |
| Reporters Committee for Freedom of the Press (RCFP) | Legal defense and source protection; Legal Hotline 800-336-4243 | hotline@rcfp.org | rcfp.org |
| Committee to Protect Journalists (CPJ) | International journalist safety; digital security resources for journalists in hostile environments | info@cpj.org | cpj.org |
| Society of Professional Journalists (SPJ) | Training, ethics, Journalists Toolbox resource library | spj@spj.org | spj.org |
| PEN America | Press freedom advocacy; targets journalist harassment | pen@pen.org | pen.org |
| National Association of Hispanic Journalists (NAHJ) | Latina/o journalist community; intersection of immigration coverage and surveillance threat | nahj@nahj.org | nahj.org |
| Asian American Journalists Association (AAJA) | AAPI journalist community; communities disproportionately surveilled | national@aaja.org | aaja.org |
| Online News Association (ONA) | Digital news organizations; security training and technology resources | hello@journalists.org | journalists.org |
| The Intercept | Investigative outlet running First Look Media's SecureDrop; published primary-source coverage of ELITE, Mobile Fortify, drone surveillance | tips via theintercept.com/source-protection | theintercept.com |

**Customization requirements for journalist segment**

This segment is primarily served by journalist-security-playbook.md and the existing TIER2_DISTRIBUTION_PREP.md templates. What the existing Tier 2 materials lack: (1) the SecureDrop integration angle — the corpus recommends SecureDrop for source communications, and FPF, the SecureDrop operator, is a natural distribution partner not just an outreach target; (2) the border crossing device protocol in journalist-security-playbook.md is the most distinctive journalist-specific content not available elsewhere; (3) the PRISM and Signal safety number verification guidance is the highest-impact journalist-specific security improvement, but it requires Signal protocol knowledge that general cybersecurity guides do not address.

---

## Section 2: Contact Strategy and Outreach Mechanics

### Wave 1: Weeks 8–9 (Top-Tier Organizations, Each Segment)

**Priority and logic**: Wave 1 targets the organizations with the widest reach, the strongest distribution networks, and the most direct alignment with the corpus's threat model. A positive response from NNEDV's Safety Net Project, the AFL-CIO, the EAC, or the Freedom of the Press Foundation creates downstream credibility for Wave 2 contacts in the same segment. Wave 1 contacts are institutional and will route internally to the right team — do not target named individuals in Wave 1 for organizations in unfamiliar segments.

**Segment 1 (DV) — Wave 1 contacts**:

- **NNEDV Safety Net Project** — safetynet@nnedv.org. Message frame: the corpus's dv-survivor-safety-playbook.md was built on NNEDV's own safety planning framework and the Safety Net Project's stalkerware documentation. This is not an outside organization offering an opinion — it is content that explicitly credits and extends NNEDV's existing work. The ask: review the playbook for accuracy against Safety Net's current guidance, and if it meets their standard, consider linking from TechSafety.org resources. The NNEDV Safety Net Tech Summit 2026 is a natural integration point for training use.
  
- **Coalition Against Stalkerware** — contact@stopstalkerware.org. Message frame: 40+ organization coalition that already includes NNEDV as a founding partner and EFF (also in the corpus's Tier 2 pipeline). The corpus's device hardening guidance directly addresses stalkerware's OS-level access vectors. The ask: review for accuracy; consider listing techsafety guidance as a resource for survivors.

**Segment 2 (Labor) — Wave 1 contacts**:

- **AFL-CIO** — media@aflcio.org. Message frame: the AFL-CIO's Workers First AI initiative explicitly identifies AI-powered workplace surveillance as a core labor rights issue. The corpus provides the technical countermeasures that correspond to the rights framework the AFL-CIO is already articulating. The ask: share with the AFL-CIO Organizing Institute for consideration in organizer training curricula. Specific hook: the AFL-CIO's Labor and Immigration Policy Fellows (inaugural class congratulated April 2026) represent an audience for whom the intersection of labor organizing and immigration surveillance threat models is directly relevant.

- **Communications Workers of America (CWA)** — cwaweb@cwa-union.org. Message frame: CWA represents tech and telecom workers who are both subject to employer surveillance and may work for companies that build or deploy surveillance tools. CWA Code, the CWA's tech worker organizing initiative, is directly relevant. The ask: distribute to CWA organizing department for inclusion in organizer training.

**Segment 3 (Election) — Wave 1 contacts**:

- **U.S. Election Assistance Commission (EAC)** — eac@eac.gov. Message frame: the corpus's identity compartmentalization and data broker opt-out guidance directly addresses the doxxing threat that the EAC's own Election Official Security page identifies as a primary concern. The EAC already points election workers to Google's PII removal resource; the corpus's Part 0 data broker opt-out guidance is a comprehensive supplement. The ask: consider linking the dv-survivor-safety-playbook's identity compartmentalization section (which addresses the same doxxing threat as the DV context) from the EAC Election Official Security page.

- **Brennan Center for Justice** — press@brennancenter.org. Message frame: the Brennan Center's 2026 report How the Federal Government Is Undermining Election Security documents the CISA gap that this corpus partially fills. The Brennan Center's own research on election worker threats provides the evidentiary foundation for the corpus's election worker targeting. The ask: consider citing the corpus in Brennan Center resources for election officials post-CISA drawdown.

**Segment 4 (Journalists) — Wave 1 contacts** (supplementing existing TIER2_DISTRIBUTION_PREP.md):

- **Freedom of the Press Foundation** — info@freedom.press. This contact is already in TIER2_DISTRIBUTION_PREP.md. The supplemental framing here: FPF's 2025–2026 Strategic Plan includes a Digital Security Training program that is the precise distribution channel for the journalist-security-playbook.md. The ask is not just awareness but active integration into FPF's Digital Security Training curriculum.

- **Reporters Committee for Freedom of the Press (RCFP)** — hotline@rcfp.org. The RCFP's Legal Hotline is a natural distribution point because it serves journalists facing legal encounters — the same moment when source protection and device seizure countermeasures in the corpus are most immediately relevant.

### Wave 2: Weeks 10–12 (Secondary Organizations, Social Proof Framing)

Wave 2 uses a different message frame than Wave 1. By Weeks 10–12, at least one Wave 1 response should exist in each segment (even a soft acknowledgment). Wave 2 opens with social proof: "Organizations like [Wave 1 organization] in [space] have reviewed this resource." This framing is authentic — it does not overstate the relationship — but it anchors the outreach in existing credibility.

**Segment 1 (DV) — Wave 2 contacts**: National Domestic Violence Hotline (info@thehotline.org), National Coalition Against Domestic Violence (publicpolicy@ncadv.org), NRCDV (nrcdv@nrcdv.org), EndTAB (info@endtab.org), Washington State Coalition Against Domestic Violence (wscadv.org).

**Per-organization threat briefing approach**: For state DV coalitions in Wave 2, create a one-paragraph briefing specific to that state's documented technology abuse landscape. Example for California: the corpus's DROP platform guidance (California DELETE Act) is directly applicable to DV survivors in California who lack government-issued ID. Example for Texas: Texas has no equivalent to the California DROP platform, making the corpus's individual data broker opt-out guidance and the identity compartmentalization countermeasures more critical for Texas survivors.

**Segment 2 (Labor) — Wave 2 contacts**: SEIU (seiu@seiu.org), UFW (info@ufw.org), NDWA (info@domesticworkers.org), National Employment Law Project (nelp@nelp.org), Jobs With Justice (jwj@jwj.org).

**Per-organization threat briefing approach**: Farm worker unions (UFW) face employer surveillance in agricultural settings that includes remote monitoring of equipment operators and GPS tracking of farm vehicles. The corpus's behavioral randomization and device compartmentalization guidance applies — with the framing that organizing communications should never occur on employer-provided equipment or networks.

**Segment 3 (Election) — Wave 2 contacts**: Common Cause (common.cause@commoncause.org), League of Women Voters (lwv@lwv.org), Issue One (info@issueone.org), Verified Voting (info@verifiedvoting.org).

**Per-organization threat briefing**: Common Cause's Election Protection program coordinates thousands of poll monitors across multiple states. Poll monitors need team-level Signal group security guidance, not just individual device hardening. The election-worker-opSec-supplement.md provides the team communications protocol; the outreach to Common Cause should frame the supplement as ready-made training material for their monitor coordinator network.

**Segment 4 (Journalists) — Wave 2 contacts**: IRE (info@ire.org), CPJ (info@cpj.org), SPJ (spj@spj.org), NAHJ (nahj@nahj.org), AAJA (national@aaja.org).

### Wave 3: Weeks 13 and Beyond (Grassroots Integration)

Wave 3 targets practitioners directly rather than organizational leadership. This is the highest-reach, lowest-overhead wave — but it requires Wave 1 and Wave 2 institutional credibility to succeed because practitioners receive less organizational context for unsolicited outreach.

**Segment 1 (DV) — Wave 3**: DV advocate counselors at local shelters; survivor peer support group coordinators; VAWA-funded legal advocates. Format: one-page survivor guide (from dv-survivor-safety-playbook.md) sized for print handout or digital share in a shelter setting; QR code linking to full corpus. Distribution mechanism: ask Wave 2 state coalition contacts to share with local member organizations.

**Segment 2 (Labor) — Wave 3**: Union local stewards and shop stewards; rank-and-file organizer networks; labor study groups at community colleges. Format: one-page organizing security guide emphasizing the BYOD policy distinction (your phone for organizing, not your work phone) and Signal group security. Distribution mechanism: AFL-CIO Organizing Institute graduates who have received Wave 1/2 corpus exposure are the ideal grassroots distribution network.

**Segment 3 (Election) — Wave 3**: Poll worker trainers and coordinators; local election clerk offices; poll monitor volunteer coordinators. Format: election-worker-opSec-supplement.md adapted as a slide deck for pre-election training sessions. Distribution mechanism: EAC and state election director associations as relay; the supplement is already structured as a briefing document.

**Segment 4 (Journalists) — Wave 3**: Journalism school faculty and student journalists; local news organizations without dedicated security infrastructure; freelance journalist associations. Format: journalist-security-playbook.md adapted as a 2-page checklist for journalists without the bandwidth to read the full document.

---

## Section 3: Content Customization Roadmap

### What Exists in the Phase 1 Corpus

The Phase 1 corpus (threat-model.md, opsec-playbook.md, implementation-guide.md) provides a complete foundation that is directly applicable to all four Tier 2 segments with reframing. The countermeasures are not segment-specific — GrapheneOS, Signal, Tor, data broker opt-outs, and behavioral randomization defeat surveillance regardless of whether the adversary is ICE, an abusive partner, an employer's HR department, or a hostile political actor. What is segment-specific is the threat frame, the risk calculus, and the sequencing of actions.

**Existing Phase 2 scenario playbooks** (already completed) that serve as primary distribution artifacts for this strategy:

- dv-survivor-safety-playbook.md — DV segment primary artifact; addresses safety planning sequence, stalkerware landscape, shared account separation, smart home and connected vehicle threats
- activist-organizing-playbook.md — Labor segment partial coverage; addresses protest security, ALPR evasion, drone countermeasures; needs supplemental labor-specific content on BYOD and NLRA context
- election-worker-opSec-supplement.md — Election segment primary artifact; addresses identity compartmentalization for election workers, team communications security, doxxing countermeasures
- journalist-security-playbook.md — Journalist segment primary artifact; addresses CBP border crossing protocol, source compartmentalization, SecureDrop, PRISM/Signal safety number verification

### Gaps to Fill: New Content Required

**DV segment gaps**:
The existing dv-survivor-safety-playbook.md is substantially complete. Three gaps remain: (1) a one-page survivor guide formatted for physical handout in shelter settings, with QR code and hotline number prominently placed; (2) a 20-minute training module for DV advocate counselors explaining the technology landscape without requiring technical expertise; (3) a specific supplement on AirTag/Tile covert tracking countermeasures, which is not in the current dv-survivor-safety-playbook.md and which represents the fastest-growing tracking vector in DV contexts (Apple's Precision Finding for AirTags is documented as the countermeasure, but the playbook does not currently walk through the detection workflow).

**Labor segment gaps**:
The activist-organizing-playbook.md addresses protest and direct action security, not workplace organizing security. Required new content: (1) BYOD policy security brief explaining the legal distinction between employer-monitored work devices and personal devices; (2) collective action security protocol for organizing committees — how to use Signal groups with verified membership, how to manage operational security when a group grows beyond the core organizing committee; (3) a one-page guide to keeping organizing communications off employer networks, formatted for workers without technical background. This content can be drafted as a standalone 1,000-word supplement to the existing playbook rather than a new document.

**Election worker segment gaps**:
The election-worker-opSec-supplement.md is substantially complete for individual election worker security. Required additional content: (1) a poll monitor team communications protocol — how a Common Cause or League of Women Voters monitor coordinator establishes a Signal group for 30–50 volunteers, verifies members, and establishes check-in protocols; (2) a post-election safety protocol for contested election environments — what election workers should do to protect themselves in the period between election night and certification when threat levels are historically elevated; (3) a specific supplement on insider threat mitigation, which the election-worker-opSec-supplement.md currently addresses only at the individual hygiene level.

**Journalist segment gaps**:
The journalist-security-playbook.md is the most complete of the four. The remaining gap is practical: the SecureDrop access guidance assumes journalists know what SecureDrop is and how it works. A 400-word "SecureDrop for sources: what journalists need to know about how sources use it" supplement helps journalists communicate the system to potential sources who are not technically sophisticated. This supplements rather than replaces the existing guidance.

### Content That Should Not Be Duplicated

The Phase 1 corpus (threat model, implementation guide, opsec playbook) should not be reproduced in segment-specific guides. The segment-specific playbooks should: (1) state clearly what threat the reader faces; (2) identify the relevant sections of the Phase 1 corpus by section heading; (3) add only the content that is segment-specific. This modular approach preserves the corpus's utility as a central reference while allowing the playbooks to function as standalone entry points for new audiences.

---

## Section 4: Tier 2 Launch Readiness

### Prerequisite: Phase 1 Launch and Adoption Tracking (Weeks 1–6)

Phase 1 launch is the prerequisite for this strategy. The following signals from Phase 1 outreach directly inform Tier 2 sequencing:

**Signals that strengthen Tier 2 DV segment priority**: If Phase 1 legal aid contacts (particularly immigration advocates) report that survivors in their caseloads have experienced both immigration enforcement and intimate partner surveillance — a documented overlap — the DV segment should move from Wave 1 to immediate launch. The population overlap between DV survivor services and immigration legal aid is substantial; shelters serving immigrant survivors are a natural bridge organization.

**Signals that strengthen Tier 2 labor segment priority**: If Phase 1 community organization contacts report that workers in organizing drives are facing employer surveillance that the corpus's countermeasures address, the labor segment should be elevated. The AFL-CIO Labor and Immigration Policy Fellows cohort (congratulated April 2026) represents a bridge population — labor advocates who also work on immigration policy and are likely to have seen the Phase 1 corpus through that channel.

**Signals that strengthen Tier 2 election worker segment priority**: CISA cutbacks are time-sensitive. The 2026 midterm election cycle is on a fixed timeline. If election security resources are not available by August 2026 (National Poll Worker Recruitment Day per EAC), the window for pre-election training integration closes. This segment has the most time-sensitive launch requirement of the four.

**Signals that strengthen Tier 2 journalist segment priority**: If Freedom of the Press Foundation or IRE responds positively to existing TIER2_DISTRIBUTION_PREP.md outreach, the journalist segment wave should be initiated immediately using the extended contact list in this document. Do not wait for Week 7 if a warm journalist organization introduction exists.

### Week 7 Gate Decision

Per PHASE_2_SEQUENCING.md Section 2, the Week 7 gate requires:

- 1,000+ cumulative Gist views (minimum trigger)
- At least 3 Tier 1 organizations at Stage 2+ engagement (not just acknowledged — actively sharing or integrating)
- 100+ feedback form submissions
- At least one explicit request from a Tier 1 organization for materials tailored to a Tier 2 segment (e.g., a legal aid organization asking for DV-specific guidance)

**If the gate passes**: Begin Tier 2 Wave 1 outreach in the priority order DV first, then election workers (time-sensitive due to 2026 election cycle), then labor, then journalist segment supplements. DV is first because the dv-survivor-safety-playbook.md is complete and ready for distribution with no additional content development required.

**If the gate passes but narrowly** (Gist views between 1,000–2,000, fewer than 5 Tier 1 integrations): Reduce Wave 1 to NNEDV Safety Net, EAC, and Freedom of the Press Foundation only — three contacts, one per segment — rather than the full Wave 1 contact list. Use the responses to calibrate Wave 2 timing.

**If the gate fails** (Gist views below 1,000 at Week 7): Do not launch Tier 2. Reassess Phase 1 messaging. The most likely failure mode is that the Gist URL is not reaching the intended organizations — check Bitly click data to determine whether the link is being clicked (indicating the email is being read but the corpus is not compelling) or not (indicating the email is not reaching decision-makers). The contingency in this case is a revised Phase 1 subject line test for the remaining un-contacted organizations before any Phase 2 launch.

---

## Section 5: Metrics and Decision Points

### Success Indicators: Expected by Week 12

**Distribution depth metrics**:

| Metric | Minimum threshold (Week 12) | Strong signal threshold |
|---|---|---|
| DV segment organizations contacted | 5 (Wave 1 complete) | 10+ (Wave 2 underway) |
| DV segment responses | 1 acknowledgment | 1 training integration request |
| Labor segment organizations contacted | 5 (Wave 1 complete) | 10+ (Wave 2 underway) |
| Labor segment responses | 1 acknowledgment | AFL-CIO Organizing Institute integration discussion |
| Election segment organizations contacted | 5 (Wave 1 complete) | EAC or Brennan Center positive response |
| Election segment responses | 1 acknowledgment | EAC resource page link or Brennan Center citation |
| Journalist segment organizations contacted | 3 (supplement to existing TIER2_DISTRIBUTION_PREP.md) | FPF Digital Security Training curriculum integration |
| Journalist segment responses | 1 response (supplementing existing pipeline) | SecureDrop operator collaboration |
| Gist views (cumulative by Week 12) | 2,000+ | 5,000+ |
| Playbook downloads or links | 10+ external shares documented | Organizational website integration at 1+ org |

**Quality indicators**:

A playbook that has been integrated into an organization's training curriculum — not just acknowledged, but actively used — is worth more than 100 cold-email acknowledgments. Track training integration explicitly: ask each positive respondent whether they have incorporated corpus materials into any training, and document the outcome. Training integration is the highest-confidence indicator that the content meets the segment's operational needs.

**Citation and legal impact**: The highest-impact metric remains unchanged from PHASE_2_SEQUENCING_STRATEGY.md Section 6: citation in a legal filing, legislative testimony, or court decision. For the DV and election worker segments specifically, this is plausible — DV advocates provide expert testimony in family law proceedings, and election law litigation is active in 2026. Track any contact who is affiliated with legal proceedings.

### Red Flags: Indicators to Pause or Pivot

**Red flag 1: DV organizations express safety concerns about the corpus**. If NNEDV Safety Net or Coalition Against Stalkerware reviews the dv-survivor-safety-playbook.md and identifies content that could be dangerous if applied without professional advocacy support, pause distribution to that segment and revise. This is the most important quality check for the DV segment — the safety planning community has hard-won expertise about what guidance can cause harm in context, and their feedback overrides any general communication security principle.

**Red flag 2: Low Phase 1 adoption despite full outreach**. If Phase 1 achieves fewer than 500 Gist views and fewer than 2 Tier 1 organizations at Stage 2 engagement by Week 6, the corpus is not reaching its intended audience. In this case, Tier 2 launch should be suspended and the distribution mechanism — not the content — should be reassessed. The grassroots-first contingency below applies.

**Red flag 3: Significant content gaps identified by early Tier 2 contacts**. If AFL-CIO or NNEDV respond with feedback that the corpus misframes a significant aspect of their constituency's threat (for example, if the labor playbook supplement misunderstands NLRA protections in a way that could mislead organizers about their legal rights), pause distribution for that segment and revise before continuing Wave 2.

**Red flag 4: CISA gap has been filled by an alternative resource**. If another organization (EFF, CDT, or a newly funded government program) produces comprehensive election worker security guidance before the Tier 2 election worker wave launches, reassess whether the election-worker-opSec-supplement.md adds unique value or whether the corpus should reference the better-resourced alternative and focus on other segments.

### Contingency: Grassroots-First Strategy If Institutional Wave Fails

If Tier 2 Wave 1 institutional outreach (Weeks 8–9) generates no responses across all four segments by Week 11, skip Wave 2 and begin grassroots-first distribution:

**Grassroots-first sequence**: Post the dv-survivor-safety-playbook.md, election-worker-opSec-supplement.md, and journalist-security-playbook.md directly to relevant online communities — the Coalition Against Stalkerware's partner network page, the Election Protection volunteer coordinator network, the IRE members-only forum (if accessible), and the AFL-CIO Organizing Institute's alumni network. These are lower-prestige distribution channels than institutional endorsement, but they reach practitioners directly and can generate organic institutional interest when practitioners bring the resource to their organizational leadership.

**Metrics for grassroots-first success**: If the direct practitioner distribution generates 50+ external links or shares within four weeks, this constitutes sufficient adoption signal to resume institutional outreach — now with organic traction as the social proof that replaces Wave 1 institutional endorsement.

---

## Sources

- [NNEDV Safety Net Project](https://www.techsafety.org/) — authoritative DV technology safety resource; Safety Net Tech Summit 2026 confirmed
- [NNEDV — Technology Safety](https://nnedv.org/content/technology-safety/) — national coalition resource on tech and DV
- [Coalition Against Stalkerware](https://stopstalkerware.org/) — 40+ organization coalition; NNEDV founding partner confirmed
- [National Domestic Violence Hotline](https://www.thehotline.org/) — 1-800-799-7233; 56-coalition distribution network
- [NCADV State Coalitions](https://ncadv.org/state-coalitions) — state coalition directory
- [AFL-CIO Workers First Initiative on AI](https://aflcio.org/reports/workers-first-ai) — labor AI surveillance policy framework
- [AFL-CIO Organizing Institute 2026](https://actionnetwork.org/ticketed_events/organizing-institute-2026) — Minnesota, 2026 training event confirmed
- [AFL-CIO Labor and Immigration Policy Fellows](https://aflcio.org/2026/4/8/afl-cio-congratulates-inaugural-class-labor-and-immigration-policy-fellows) — inaugural class April 2026
- [Georgetown Law — Labor Organizing and AI Surveillance](https://www.law.georgetown.edu/poverty-journal/blog/labor-organizing-and-ai-surveillance-in-the-workplace/) — documented employer AI surveillance of organizing
- [EFF — How Cops Are Using Flock Safety to Surveil Protesters](https://www.eff.org/deeplinks/2025/11/how-cops-are-using-flock-safetys-alpr-network-surveil-protesters-and-activists/) — 50+ agencies using ALPR against protest activity
- [ArXiv — Surveillance and Suppression of Union Activity](https://arxiv.org/html/2603.03130) — 2026 academic analysis of digital union busting
- [Equitable Growth — Union Contracts and Automated Surveillance](https://equitablegrowth.org/research-paper/how-union-contracts-are-protecting-u-s-workers-from-automated-management-and-surveillance-in-the-workplace/) — collective bargaining as surveillance countermeasure
- [EAC Election Official Security](https://www.eac.gov/election-officials/election-official-security) — federal resource for election worker security post-CISA
- [EAC 2026 Annual Board Meetings](https://www.eac.gov/news/2026/05/05/us-election-assistance-commission-holds-2026-annual-board-meetings-chicago-and-dc) — May 2026 confirmed
- [Brennan Center — How Federal Government Is Undermining Election Security](https://www.brennancenter.org/our-work/research-reports/how-federal-government-undermining-election-security) — CISA drawdown analysis
- [The Register — Election Workers Fear Threats Without Federal Support 2026](https://www.theregister.com/2025/08/16/election_workers_fears_after_cisa_cuts/) — 61% concerned about CISA cuts
- [Nextgov — Senator Warns CISA Election Security Pullback](https://www.nextgov.com/cybersecurity/2026/05/senator-warns-cisa-election-security-pullback-could-leave-midterms-vulnerable/413378/) — May 2026 Senate Intelligence Committee warning
- [Brennan Center — Survey on Election Official Concerns](https://www.brennancenter.org/our-work/analysis-opinion/survey-finds-election-officials-remain-concerned-about-safety-lack) — 25% concerned about assault, 52% worried about staff safety
- [Common Cause Election Protection](https://www.commoncause.org/issues/election-protection/) — poll monitor coordination network
- [Issue One — Protecting America's Election Workers](https://issueone.org/solutions/protecting-americas-election-workers/) — bipartisan election worker threat documentation
- [Freedom of the Press Foundation — 2026 Journalist Digital Security Checklist](https://freedom.press/digisec/blog/journalists-digital-security-checklist/) — FPF 2026 security resources confirmed
- [Freedom of the Press Foundation — 2025-2026 Strategic Plan](https://freedom.press/about/announcements/freedom-of-the-press-foundations-2025-2026-strategic-plan/) — Digital Security Training program confirmed
- [U.S. Press Freedom Tracker — 2026 Threats](https://pressfreedomtracker.us/blog/a-troubling-picture-of-press-freedom-pressures-to-start-2026/) — documented 2026 press freedom deterioration
- [NLRB — Your Rights During Union Organizing](https://www.nlrb.gov/about-nlrb/rights-we-protect/the-law/employees/your-rights-during-union-organizing) — NLRA legal framework for organizing protection
- [CIS — Election Security Spotlight: Doxxing](https://www.cisecurity.org/insights/spotlight/election-security-spotlight--what-is-doxing) — CIS election worker doxxing documentation

---

*Created: 2026-05-07. Research conducted using public sources confirmed as of May 2026. Confidence level: high on organization identification (all websites verified active), high on threat claims (primary source documentation throughout), medium on named individual contacts (organizational roles change; verify before sending). Pre-send contact verification required for all named individuals. Quarterly review checkpoint: aligned with PHASE_2_SEQUENCING.md Gate 4 (July 26, 2026).*
