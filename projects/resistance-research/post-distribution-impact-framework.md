---
title: "Post-Distribution Impact Measurement Framework"
created: "2026-05-06"
supersedes: "Session 688 version (April 30, 2026)"
status: active
phase: Phase 1 distribution preparation
project: resistance-research
companion_docs:
  - adoption-tracking-dashboard-spec.md
  - measurement-and-iteration-framework.md
  - execution-plans/EXECUTION_PATHS_DECISION_FRAMEWORK.md
  - domains/domain-37-baseline-metrics.md
cross_references:
  - DISTRIBUTION_GUIDE.md
  - distribution-institutional-outreach-templates.md
  - policy-influencer-mapping.md
scope: "Institutional adoption pathways by sector; concrete measurement tools with specific searches; domain-level success pattern analysis; failure mode detection with early warning signals"
---

# Post-Distribution Impact Measurement Framework

**May 6, 2026 — Phase 1 Execution Prep. Activate on distribution launch.**

This document governs post-Phase-1-distribution impact assessment across all three execution paths (A, A+37, B). It is a complete rebuild of the Session 688 draft, extending it in four areas that earlier version left underspecified: (1) sector-by-sector institutional adoption mechanics — not just what sectors exist, but how each one actually processes and absorbs policy research, including the specific gatekeeping functions and transformation stages in each sector; (2) measurement tools configured to the specific content of this framework, with concrete search queries rather than tool categories; (3) domain-level adoption likelihood tied to specific domain characteristics and current institutional demand; (4) failure mode detection with three distinct misuse archetypes and early warning signals.

The companion document `adoption-tracking-dashboard-spec.md` (Session 717, production-ready) provides the tracking templates, spreadsheet schema, and reporting cadence. This document provides the analytical foundation that makes those templates meaningful.

**Path-agnostic**: All three distribution paths generate measurable outcomes through the same institutional channels. Path A+37 creates a separate measurement track for the 12 election-protection-targeted Domain 37 contacts; Path B delays the start date; neither changes the institutional mechanics described here.

---

## Part I: Institutional Adoption Pathways by Sector

### The Transformation Model: How Policy Research Moves Through Institutions

The naive mental model — researcher distributes framework, institution reads it and implements it — does not describe how policy research actually moves. Research diffuses through a series of gatekeeping communities, each of which transforms the material before passing it along. The transformation is not degradation; it is the mechanism by which abstract analysis becomes operational practice. Understanding the specific transformation stages in each sector is prerequisite to building measurement systems that detect real adoption rather than surface engagement.

**Five-stage model**:

1. **Discovery**: A member of a professional community encounters the research through direct outreach, peer referral, or passive browsing
2. **Credentialing**: A gatekeeper with standing in the community vouches for it (citation, assignment, endorsement, organizational adoption)
3. **Translation**: The research is reformatted for the next audience (one-pager, brief, testimony, training module, court argument)
4. **Integration**: The translated version is incorporated into the professional community's active work
5. **Institutionalization**: The framework becomes a reference point the community uses without necessarily citing the origin

Measurement is hardest at stages 4 and 5 — the highest-value adoptions are also the least visible. A Senate staffer incorporating domain language verbatim into draft legislation will not appear in any citation database. This is the fundamental measurement challenge this framework is designed to work around.

---

### Sector 1: State Attorneys General

**How AGs actually process policy research**

AG adoption operates through a structured internal consumption pathway that most researchers are unaware of. When a Tier 1 brief arrives in an AG's office, it goes to the policy counsel or senior litigation staff, not to the AG directly. These staff members scan new research against three questions: (1) Does this support a live case we have filed or are considering? (2) Does this provide a doctrinal argument we have not yet used? (3) Does this give us evidence for a coalition letter the office has not already signed?

The National Association of Attorneys General (NAAG) operates a formal information-sharing function across AG offices: joint briefings, shared research databases, and multi-state litigation coordination infrastructure. Research that reaches NAAG's policy pipeline reaches all 22+ coalition AGs simultaneously. This is the highest-leverage single channel in the sector.

The 35-domain framework's primary entry points for AG adoption:
- **Domain 6 (Judicial Independence)**: Universal injunction doctrine analysis, state parens patriae standing as structural workaround post-CASA. State AGs have filed 75+ lawsuits against the Trump administration in 2025; Domain 6 provides the doctrinal architecture for how state courts can provide relief where federal courts are constrained.
- **Domain 29 (Prosecutorial Weaponization)**: AG self-interest in documenting federal overreach into local and state prosecutorial independence. The Abrego Garcia vindictive prosecution finding is the bridge document — it demonstrates that federal political pressure on local prosecution is documentable and challengeable.
- **Domain 37 (Election Interference)**: The 22-state AG coalition is already coordinating on election protection litigation. The domain-37-baseline-metrics.md provides the quantified reference frame AGs need for emergency TRO filings against SAVE-based voter roll removals in the NVRA quiet period.
- **Domain 16 (Immigration)**: State AG authority over enforcement limitations, community supervision alternatives. Washington AG Bob Ferguson has already filed against the March 31 election executive order — this is a live docket.

**Adoption timeline**: 60-180 days from receipt to detectable use. Exception: emergency litigation. If an AG office is litigating an active SAVE purge TRO, the Domain 37 baseline metrics are relevant within days, not months.

**What AG adoption looks like**:
- Amicus brief that incorporates domain analysis or cites specific domain data
- Coalition letter signed by multiple AGs citing framework as evidentiary support
- AG press statement or public report incorporating domain framing
- NAAG newsletter or conference presentation citing the framework as research the coalition is tracking

**Detection methods**:
- PACER (pacer.gov) and CourtListener (courtlistener.com): search `"democratic renewal" OR "35-domain" OR "domain 37" AND "election" AND "amicus"` monthly
- 22 state AG press release archives: manual monthly review for the coalition states (CA, NY, IL, MA, PA, WA, CO, MI, MN, NJ, CT, MD, OR, NV, NM, VA, HI, ME, VT, RI, WI, DE + DC)
- NAAG newsletter and annual conference materials: monitor naag.org for research citations
- Direct contact intelligence from contacts with AG network access

**Success signal**: An AG amicus brief or coalition letter citing domain analysis constitutes Level 3 institutional adoption. This is the highest-value AG outcome. A NAAG conference presentation citing the framework constitutes Level 2.

---

### Sector 2: Law Schools and Legal Clinics

**How law schools actually process policy research**

Law schools operate on three separate adoption tracks with distinct timelines and measurement approaches. Conflating them produces measurement confusion.

**Track A — Faculty**: Law professors discover research through SSRN, Google Scholar, legal blog aggregators (PrawfsBlawg, Balkinization, Faculty Lounge, Just Security), and subject-matter journal tables of contents. Faculty adoption manifests as citation in law review articles (6-18 month lag from submission to publication), syllabus assignment (visible only through annual surveys or direct contact), or op-ed and academic commentary (fast). The value of faculty citation is permanence — a citation in a Yale Law Journal article is a permanent entry in legal research databases accessible to every law student and lawyer for decades.

**Track B — Clinical programs**: Law school clinics (immigration, civil rights, environmental justice, housing, prisoners' rights) have active dockets and consume research much faster than faculty — weeks rather than months. Clinics need specific, actionable analysis that can be incorporated into filings. The framework's constitutional analysis in Domain 6 and Domain 29, and the comparative constitutional law sections across all domains, are the primary value-add for clinics. The Harvard Immigration and Refugee Clinical Program and Columbia's Immigrants' Rights Clinic are the highest-leverage targets — their dockets are directly relevant to Domains 16 and 29.

**Track C — Student note and comment authors**: Law review note editors and student comment authors actively search SSRN and Google Scholar for recent frameworks to build on. A domain that identifies an open doctrinal question — the Section 3 enforcement gap after Trump v. Anderson; the "arrest operation" legal theory in Domain 28; the vindictive prosecution doctrine's application to federal-state political coordination in Domain 29 — is a potential note topic. Student adoption is fast (law review notes take 4-8 months from selection to publication) and creates a citation chain that persists in HeinOnline, Westlaw, and Lexis databases for the life of the publication.

**Primary entry points by domain**:
- Domain 28 (War Powers): The OLC memo's internal contradictions are a doctrinal article waiting to be written. Just Security has covered the congressional vote record; the domain synthesis provides the analytical frame that turns reporting into scholarship.
- Domain 29 (Prosecutorial Weaponization): The Abrego Garcia vindictive prosecution finding at full evidentiary hearing stage with documentary support is unprecedented in this political context. For law review note authors, this is the case study that makes abstract doctrine concrete.
- Domain 37a scope document (Section 3 post-Trump v. Anderson): The enforcement gap is a known doctrinal problem with no published solution. A note identifying the state-level enforcement pathway and the federal appropriate-legislation path fills a gap that every constitutional law professor teaching Trump v. Anderson needs.
- Domain 6 (Judicial Independence): Universal injunction doctrine and the three-track response to CASA is directly relevant to pending SCOTUS cert petitions. A faculty article on this is publishable in a top-10 journal.

**Detection methods**:
- SSRN download and citation tracking: upload all domain documents to SSRN (free; search `ssrn.com/search` by title); monitor weekly download counts and citations via SSRN author dashboard
- Google Scholar alerts (scholar.google.com/scholar_alerts): set for each document title and for doctrinal phrases unique to the framework (e.g., `"arrest operation theory" "war powers"`; `"Section 3 enforcement gap" "appropriate legislation"`)
- HeinOnline (heinonline.org) and Westlaw citation searches: quarterly manual search (not automated); search for framework title and key domain phrases
- Law school clinical program director check-ins at 60 and 120 days (direct contact; not passive monitoring)
- PrawfsBlawg and Faculty Lounge: set RSS alerts for any post citing the framework

**Success signal**: A citation in a student note in a top-15 law review, or use in a filed brief by a law school clinic, constitutes Level 2 adoption. A law faculty article citation in a peer-reviewed journal constitutes Level 2 with higher cascade value (it enters Westlaw, HeinOnline, and JSTOR permanently). A clinic case that builds an argument on the domain analysis — even without explicit citation — constitutes Level 3 operational adoption.

---

### Sector 3: Think Tanks

**How think tanks actually process policy research**

Think tanks operate in two modes relevant to the framework: as research producers who may cite it, and as framework consumers who may absorb its analytical architecture without citation. The second mode is more valuable but harder to detect.

**Mode 1 — Citation**: A think tank researcher writes a report and cites the framework as a source. This is measurable through Overton and Google Scholar alerts. The value is legitimate but limited — a footnote citation does not mean the framework has shaped the organization's analytical approach.

**Mode 2 — Framework absorption**: A think tank researcher structures their own report using the framework's analytical architecture — the diagnostic vector approach, the international evidence comparative method, the domain decomposition — without necessarily citing the origin. This is the highest-value outcome in the think tank sector. When the Brennan Center publishes a report on election interference that uses the same seven interference vectors as Domain 37, organized with the same before/after baseline methodology as domain-37-baseline-metrics.md, the framework has shaped how one of the field's most influential organizations thinks about the problem. This does not appear in citation databases.

**The competitive dynamic**: Unlike advocacy organizations that welcome an external research base to cite, think tanks that produce their own research on the same topics are partially competitive with the framework. Brennan Center, EPI, Protect Democracy, and Just Security all produce original research on domains where the framework is strongest. The adoption pathway for these organizations is not "cite the framework" but "be shaped by the framework's analytical approach while producing their own original content."

**Primary entry points by think tank**:
- Brennan Center (Domains 1-3, 6, 37): The Brennan Center's democracy and justice programs overlap with the framework's strongest domains. The election baseline metrics provide the specific numerical reference frame that Brennan Center's research uses but doesn't always establish systematically.
- Economic Policy Institute (Domain 17): EPI publishes issue briefs that are distributed through the AFL-CIO network to 56 affiliated unions. One EPI issue brief citing the Domain 17 international comparative evidence on sectoral bargaining reaches labor legislative directors across all major U.S. unions.
- Protect Democracy (Domains 29, 37, executive power architecture): Protect Democracy's retaliatory action tracker is already cited in Domain 29. Reciprocal citation is likely if the framework provides synthesis and framing that goes beyond Protect Democracy's own case-by-case documentation.
- Just Security (Domains 28, 29): Just Security publishes daily. A Just Security article citing the framework's OLC memo analysis (Domain 28) or synthesizing the vindictive prosecution doctrine (Domain 29) cascades to Senate Intelligence/Judiciary staff and federal judicial clerks within 48-96 hours of publication.
- Third Way and Data for Progress (Domains 1-3): These organizations conduct polling and produce electoral strategy analysis. The framework's electoral reform domain provides the structural context for their political analysis.

**Detection methods**:
- Overton Policy Citation Index (overton.io): Set alerts for framework title, key domain phrases. Overton crawls 30,000+ policy sources including think tank publications. Lag time 2-6 weeks for recently published material. This is the primary automated detection tool for think tank adoption.
- RSS monitoring: Create RSS feeds for target think tank publication pages (Brennan Center /our-work/research-reports; EPI /research; Protect Democracy /work; Just Security all articles). Check weekly.
- Direct contact check-ins at 60 days: The research directors who received the framework are the most direct information source. A structured check-in question ("have you seen any of your colleagues use the framework's framing in their own work?") surfaces Mode 2 adoption that passive monitoring misses.

**Success signal**: An EPI issue brief citing Domain 17 analysis, or a Brennan Center report using the Domain 37 vector framework, constitutes Level 2-3 adoption. A think tank report that uses the framework's comparative international evidence structure is Level 2 framework adoption. A Just Security article that synthesizes domain analysis and attributes it to the framework constitutes Level 2 adoption with cascade potential.

---

### Sector 4: Advocacy Groups and Civil Society Organizations

**How advocacy organizations actually process policy research**

Advocacy organizations have two distinct research needs with different timelines: (1) factual documentation for member education and media engagement (the tracker model — fast turnaround, punchy format, shareable), and (2) policy arguments for legislative testimony, regulatory comments, and public campaigns (slower, requiring more vetting).

The most operationally important adoption signal in this sector is not a citation — it is **operational integration**: the research appears in materials the organization produces as part of its ongoing work, not in a one-time footnote. When Indivisible incorporates a domain analysis into a chapter training module, that analysis reaches every chapter that runs the training. The value is not a single citation but repeated activation across the network.

**Primary entry points**:
- Domain 37 and domain-37-baseline-metrics.md: Election protection organizations (Democracy Docket, Campaign Legal Center, ACLU VRA section, States United) are on the tightest operational timeline. The seven baseline metrics provide the before/after measurement infrastructure these organizations need for impact reporting and litigation support.
- Domains 1-3: Voting rights coalitions (States United, FairVote, Common Cause). These organizations produce member and public communications that benefit from the international comparative evidence the framework provides.
- Domain 29: Civil rights organizations (NAACP LDF, Lawyers' Committee, Southern Coalition for Social Justice). The SPLC indictment doctrinal analysis in Domain 29 is directly relevant to organizations considering whether and how to challenge federal prosecutorial actions.
- Environmental rollbacks tracker: Environmental justice coalitions (Sierra Club, Earthjustice, NRDC). The tracker provides the Federal Register citations and litigation status documentation these organizations need for regulatory comment and litigation.
- Domain 17: Labor coalitions (AFL-CIO, SEIU). The EPI bridge remains the most efficient path for labor sector adoption — EPI as a formal intermediary rather than direct outreach to 56 affiliated unions.

**Detection methods**:
- Direct organizational contact follow-ups at 30 and 60 days: the only reliable detection mechanism for member communications that do not enter public databases
- Organizational newsletter monitoring: subscribe to email lists for the 15 highest-priority organizations; scan weekly for domain language
- Organizational testimony databases: Congress.gov testimony archive; state legislative testimony records; search for domain-specific phrases in testimony filed by Tier 3 organizations
- Regulatory comment tracking: regulations.gov docket search for comments filed by Tier 3 organizations in domains with open comment periods (Domain 27 accreditation rulemaking; any EPA rollback comment period)
- Tracker contribution monitoring: organizations that add entries to the First Amendment Suppression Tracker, Environmental Rollbacks Tracker, or Police Consent Decree Tracker have confirmed engagement

**Success signal**: An organization's legislative testimony, regulatory comment, or public statement citing a domain or tracker constitutes Level 3 operational adoption. A training module or educational material incorporating the framework constitutes Level 2-3 adoption. A tracker contribution (organization adds entries) constitutes Level 2 adoption with ongoing engagement signal.

---

### Sector 5: Government Agencies (State-Level)

**Realistic scope for Phase 1**: Federal agency adoption under the current administration is near-zero for the framework's content. The relevant government agencies are state-level: state election directors, state legislative research offices, state supreme court law clerks, and state administrative law judges.

**Primary entry points**:
- State election offices (coordinated through NASS and NASED): Domain 37 analysis and the seven baseline metrics. State election directors are fighting the same voter roll lawsuits documented in Metric 1 of the baseline metrics file. The framework provides the analytical context for what the DOJ litigation strategy is designed to accomplish.
- State legislative research bureaus: Domain 1-3 analysis as background for voting rights and redistricting legislation in blue state legislatures still in session.
- State supreme court clerks: Domain 6 analysis as background for state judicial independence doctrine; state courts are being asked to serve as substitutes for federal courts post-CASA, and clerks drafting opinions need the comparative constitutional law evidence the domain provides.

**Detection methods**: LegiScan API (legiscan.com) for state legislative monitoring; direct contact with NASS (nass.org) and NASED representatives; state supreme court opinion searches through CourtListener for domain-specific language.

**Measurement priority**: Medium for election offices (August 7 NVRA timeline creates urgency); low for other state agencies in Phase 1.

---

### Sector 6: Corporate Boards (Phase 2+ Target)

Direct corporate adoption of the democratic renewal framework is not a Phase 1 measurement priority. Shareholder activist organizations with corporate-sector reach (As You Sow, Ceres, Interfaith Center on Corporate Responsibility) are the relevant actors and are better understood as civil society organizations. Flag corporate adoption if detected through Overton or media monitoring; do not invest in active monitoring resources for Phase 1.

---

## Part II: Impact Metrics Framework — Concrete Tools and Searches

### Design Principle: The Measurability-Value Inversion

The most measurable indicators (social media shares, download counts, search engine traffic) are inversely correlated with impact value. The least measurable indicators (a Senate staffer incorporating domain language into a committee memo, a clinic building an argument around the domain analysis without citing it) represent the highest-value outcomes. A measurement framework that optimizes for measurable outcomes will systematically undercount what the distribution is accomplishing.

This framework tracks three indicator categories explicitly organized around this inversion:

**Type 1 — High measurability, moderate value**: Citations in published work, document downloads, media mentions. Captured by automated passive monitoring.

**Type 2 — Moderate measurability, high value**: Organizational adoption signals, testimony incorporation, regulatory comment citations. Captured by a combination of passive monitoring and active contact check-ins.

**Type 3 — Low measurability, very high value**: Legislative language incorporating domain analysis, court brief arguments built on the framework, coalition strategy frameworks that mirror the domain architecture. Captured almost entirely through active contact intelligence — no passive tool reaches this.

---

### Tool 1: Overton Policy Citation Index

**What it captures**: Citations to the framework in policy documents, think tank reports, government publications, parliamentary records, and NGO reports — from 30,000+ sources across 188 countries. Most comprehensive automated tool for grey literature citation.

**Setup**:
1. Register at overton.io. Institutional access (via SAGE partnership) available if affiliated with a subscribing library; free public tier provides limited search.
2. Create document profiles for the main proposal Gist URL, the executive summary Gist URL, and the Domain 37 Gist URL.
3. Set keyword alerts for: `"democratic renewal proposal"`, `"35-domain framework"`, `"38-domain framework"`, `"domain 37 election interference"`, and five framework-specific coined phrases (see Tool 3 below for the coinage list).
4. Review weekly; log all citations in the adoption scorecard.

**Lag time**: Overton typically indexes documents 2-6 weeks after publication. Government documents can take 4-12 weeks. Use as a confirming indicator, not a real-time detector.

**Limitation**: Does not capture internal government documents, unpublished memos, or subscription-only research. The most operationally important adoptions — Hill staff briefing memos, AG internal research notes — will never appear in Overton.

---

### Tool 2: Google Scholar Alerts

**What it captures**: Academic citations faster than most other tools; typically indexes within days of publication.

**Setup**:
1. Upload all domain documents to Google Scholar through a Google Scholar profile (free; requires Google account).
2. Go to `scholar.google.com/scholar_alerts` and create alerts for each document title.
3. Set additional alerts for doctrinal phrases unique to the framework — phrases that are not standard legal vocabulary but appear in the framework's analysis.

**Specific alerts to set**:
- `"arrest operation theory" "war powers"` — unique to Domain 28 analysis
- `"Section 3 enforcement gap" "appropriate legislation"` — unique to Domain 37a scope
- `"Vance doctrine" "Youngstown"` — unique to Domain 19f/28 synthesis
- `"81 percent" SAVE voter rolls` — Metric 6 from baseline metrics file
- `"election denier" CISA cybersecurity` — Domain 37 frame
- `"ESG activation" midterm election security` — Domain 37 baseline Metric 2

**Quarterly manual searches** (these are not automatable but high value):
- `"democratic renewal" "35 domains"` — full framework citations
- `"prosecutorial weaponization" "DOJ capture"` — Domain 29 specific framing
- `"SAVE database" "false positive" voter` — Metric 6 frame
- `"state legislative autocratization"` — Domain 33 coined frame

---

### Tool 3: PACER and CourtListener for Federal Court Filings

**What it captures**: Citations to the framework in federal court filings, including party briefs, amicus briefs, and judicial opinions.

**Setup**:
1. PACER account at pacer.gov (per-page fees, typically $0.10/page; most searches are free)
2. RECAP browser extension (free, from Free Law Project): automatically uploads every PACER document you view to the free RECAP archive, making it searchable by others and reducing your future costs
3. CourtListener (courtlistener.com): full-text search of uploaded PACER documents; free; no account required for basic searches

**Specific searches**:
- CourtListener full-text search: `"democratic renewal proposal"` — checks all uploaded federal filings
- CourtListener docket monitoring for active cases in litigation-tracker-2026.md:
  - Abrego Garcia / Xinis docket: new filings weekly
  - SPLC indictment proceedings: new filings weekly
  - Oregon voter roll appeal (Ninth Circuit): oral argument monitoring
  - Any AG-filed SAVE Act litigation: search for new filings monthly

**Active cases most likely to generate citations**:
- DOJ voter roll cases (24 active + DC, Brennan Center tracker): state AGs filing motions to intervene or amicus briefs may cite Domain 37 baseline metrics
- Universal injunction post-CASA cases: Domain 6 analysis may appear in amicus filings by state AGs
- SPLC indictment proceedings: Domain 29 doctrinal analysis may be cited by defense amicus filers

**Detection value**: A citation in a federal court filing is a high-value Type 2 indicator. A citation in a federal judge's opinion is a Type 3 indicator and among the most significant impact events possible.

---

### Tool 4: SSRN for Law School Adoption

**What it captures**: Academic paper downloads, preprint citations, and law review note pipeline signals.

**Setup**:
1. Create SSRN author account at ssrn.com (free)
2. Upload all domain documents as working papers under the appropriate subject category
3. SSRN auto-tracks weekly download counts and emailed reports
4. Quarterly: manually search SSRN for papers that cite uploaded documents (SSRN search tool; or use Google Scholar's "cited by" link for documents that have been indexed)

**SSRN's law school pipeline function**: Law review note editors and student comment authors routinely search SSRN for recent working papers in their subject area. High SSRN download counts provide social proof. A Domain 37a note posted to SSRN with a title like "The Section 3 Enforcement Gap After Trump v. Anderson: State-Level Pathways and Federal Legislative Options" will appear in searches run by student note authors at every major law school.

**Note**: SSRN is the single highest-leverage upload action for the law school sector. It is a one-time setup that creates persistent discoverability in the exact channel law school Track A and Track C adopters use.

---

### Tool 5: Congress.gov and State Legislative Monitoring

**What it captures**: Framework language in congressional hearing transcripts, committee reports, legislation text; state legislative hearing testimony and bill language.

**Specific searches to run quarterly**:
- Congress.gov full-text search (free): `"democratic renewal" proposal` in hearing transcripts and committee reports
- Congress.gov: `"voter roll" SAVE NVRA "quiet period"` in any bill text or hearing (Domain 37 baseline language)
- Congress.gov: `"prosecutorial weaponization"` in any Judiciary Committee hearing transcript
- LegiScan (legiscan.com, free tier): Domain 1/37 election language in 12 priority states; Domain 33 state autocratization language; Domain 6/34 institutional authority language (full search queries specified in adoption-tracking-dashboard-spec.md Component 1.5)

**State hearing transcripts**: Not all states make hearing transcripts searchable online. For priority states (Michigan, Wisconsin, Pennsylvania, Georgia, Arizona, Nevada), check state legislature websites quarterly for committee hearings on election administration and voting rights — these are the hearings most likely to incorporate Domain 37 analysis.

---

### Tool 6: State AG Press Release Archives and NAAG

**What it captures**: State AG actions citing research frameworks; coalition letter citations; NAAG research utilization signals.

**Specific archives to monitor** (monthly, manually):
- California AG (oag.ca.gov/news): most active in democratic accountability litigation
- New York AG (ag.ny.gov/press-releases): second-most-active
- Washington AG (atg.wa.gov/news): active on election litigation (Ferguson filed against March 31 EO)
- Michigan, Pennsylvania, Wisconsin AGs: key battleground state election protection focus
- NAAG (naag.org/news-publications): coalition research citations and conference materials

---

## Part III: Success Pattern Analysis

### Domain Adoption Likelihood Tiers

Domains fall into three adoption-likelihood tiers based on four variables: (1) legal imminence — whether there is an active case, pending vote, or approaching regulatory deadline; (2) organizational fit — whether the domain solves a problem an active institution is currently facing; (3) citation chain availability — whether the domain cites organizations whose researchers will notice and reciprocate; (4) format accessibility — whether derived briefs exist or can be prepared quickly.

**Tier A — High adoption likelihood (30-90 day window)**

| Domain | Driving Variable | Primary Sector | Likely Form | Deadline |
|--------|-----------------|----------------|-------------|----------|
| Domain 37 (Election Interference) | Legal imminence (NVRA Aug 7) | State AGs, election orgs | Litigation filing, amicus, testimony | August 7, 2026 |
| Domain 29 (Prosecutorial Weaponization) | Organizational fit (SPLC docket) | Legal clinics, civil rights orgs | Brief, Just Security article, law review note | No hard deadline |
| Domain 28 (War Powers) | Citation chain (Just Security) | Just Security, law school faculty | Published analysis, faculty article | No hard deadline |
| Domain 37a scope (Section 3 gap) | Law review gap identification | Law school Track C (student notes) | Law review note | No hard deadline |

**Tier B — Moderate adoption likelihood (60-180 day window)**

| Domain | Driving Variable | Primary Sector | Likely Form | Deadline |
|--------|-----------------|----------------|-------------|----------|
| Domain 6 (Judicial Independence) | Organizational fit (post-CASA) | Law schools, Brennan Center | Law review, amicus brief | No hard deadline |
| Domain 17 (Labor) | Citation chain (EPI) | EPI, AFL-CIO | EPI issue brief, union testimony | No hard deadline |
| Domains 1-3 (Electoral) | Organizational fit (FairVote, States United) | Voting rights orgs | Policy brief, coalition letter | Varies by state session |
| Domain 27 (Academic Freedom) | Legal imminence (accreditation rulemaking) | AAUP, law faculty | Regulatory comment, published commentary | Rulemaking comment deadline |

**Tier C — Slower adoption cycles (90-180+ day window)**

| Domain | Driving Variable | Primary Sector | Likely Form | Notes |
|--------|-----------------|----------------|-------------|-------|
| Domain 15 (Environment) | Organizational fit (active rollbacks) | Earthjustice, NRDC, state AGs | Regulatory comment, litigation | EPA rollback tracker provides most immediate entry |
| Domain 22 (Racial Justice) | Citation chain (NAACP LDF) | Civil rights orgs | Testimony, brief, campaign material | Reparations framing narrows immediate audience |
| Domains 4, 5 (Digital gov, Fiscal) | No immediate deadline | Think tanks, academics | Issue brief, academic article | Long-cycle analysis domains |
| Domain 25 (FISA) | Legal imminence (FISA outcome pending) | EFF, Just Security, ACLU | Regulatory advocacy | Outcome determination needed first |

---

### What Drives Adoption Variance: The Four Variables

**Variable 1 — Legal imminence is the strongest predictor**

Domains with an active case, pending vote, or approaching regulatory deadline generate 3-5x faster adoption than domains without a temporal hook. Domain 37 has four simultaneous hooks as of the distribution window: the NVRA quiet period (August 7), Griswold primary (June 30), ESG non-activation (ongoing), and 24+ active DOJ voter roll lawsuits. Domain 27 has the accreditation rulemaking comment window. Domain 28 has ongoing Senate war powers procedural context. Domain 5 (fiscal reform) has no immediate hook — it is important but not urgent, and adoption will wait.

**Variable 2 — Organizational fit with current work, not topic importance**

Research is adopted when it solves a problem an organization is facing right now, not when it correctly identifies an important future problem. EPI adopts Domain 17 not because labor is important (EPI already knows that) but because the international comparative evidence on sectoral bargaining fills a gap in their current arguments about why sectoral bargaining would work in the U.S. context. Brennan Center adopts Domain 37 not because elections matter (Brennan Center tracks everything about elections) but because the seven-vector interference baseline provides a systematic reference frame that their own issue-by-issue research doesn't consolidate.

**Variable 3 — Citation chain reciprocity creates pull**

The framework cites the organizations it is distributing to. Domain 28 cites Just Security's OLC memo coverage. Domain 29 cites Protect Democracy's retaliatory action tracker. Domain 37 baseline metrics cites the Brennan Center tracker, Wisconsin SDRI tracker, and Democracy Docket. Organizations read research that takes their own work seriously. This is not citation farming — it is accurate attribution that happens to create reciprocal engagement incentives. Domains that cite target organizations should be distributed to those organizations first; domains that do not cite any target organization's prior work will require more direct persuasion.

**Variable 4 — Format accessibility determines time-to-adoption, not likelihood**

A 10,000-word domain document requires a derived two-page brief before most practitioners can use it. This is not a content problem — it is a format problem. Tier A domains should have derived one-pagers or "current threat" briefs prepared before initial outreach. The institutional outreach templates in `distribution-institutional-outreach-templates.md` provide the distribution format; what is missing for Tier A domains is a practitioner-facing brief that can be forwarded within an organization. See `measurement-and-iteration-framework.md` Part V for the five-step adoption facilitation sequence — the derived brief (Step 2) is the highest-leverage single action the distributing researcher can take.

---

## Part IV: Failure Mode Detection

### The Three Misuse Archetypes

Policy frameworks distributed into contested political environments face three distinct failure modes. Each requires a separate detection approach. The common mistake is treating all bad-faith or misguided citations as the same problem — they are not. A bad-faith extraction (Mode 1) requires a rapid response; a structural misapplication (Mode 2) requires a sustained correction strategy; a credibility-association problem (Mode 3) requires immediate internal correction regardless of whether any external response is warranted.

---

**Failure Mode 1: Selective Extraction for Distortion**

Definition: A bad-faith or ideologically misaligned actor extracts a data point or argument from the framework and uses it in a context that inverts the framework's purpose.

Concrete examples for this framework:
- The DOJ citing the framework's documentation of voter registration irregularities as support for voter roll purge litigation, presenting the SAVE database error documentation as evidence of the program's necessity rather than its unreliability
- A conservative legal organization citing the war powers analysis in Domain 28 to argue that the president has always had unilateral military authority — extracting the factual documentation of the Venezuela operation while discarding the normative critique
- An election administration organization (aligned with voter restriction policy) citing the Domain 37 baseline metrics on voting law changes as evidence that state legislatures are engaged in "voter protection" rather than voter suppression

**Early warning signals**:
- An Overton or Google Scholar alert shows the framework cited in a source with an adversarial orientation (Heritage Foundation, Pacific Legal Foundation, America First Legal, or administration-aligned organizations)
- The citation references a specific statistic without the surrounding analytical context — a data point appears without the domain's interpretive frame
- The citation appears in a legal filing or public statement that opposes the framework's stated goals
- A Tier 1 contact flags that they have seen the framework cited by an organization that mischaracterizes its conclusions

**Detection method**: Overton and Google Scholar alerts are context-blind. Every citation detected through passive monitoring must be read within 48 hours of detection. Do not assume a citation is positive before verifying context. The detection protocol is simply: read it immediately.

**Response protocol**:
1. Do not respond directly to the bad-faith use in the same public channel — this amplifies the misuse
2. Add a "Common misinterpretation" subsection to the relevant domain file within 48 hours, providing precise language for what the data point does and does not demonstrate
3. Contact the organizations closest to the cited domain within 24 hours (e.g., if Domain 37 is cited by a voter-restriction organization, contact Democracy Docket and States United within 24 hours with context and the corrected language)
4. If the misuse appears in a legal filing, prepare a factual rebuttal brief that can be shared with litigation organizations who may need to respond in the same proceeding

---

**Failure Mode 2: Framework Capture by Misaligned Organizations**

Definition: The framework is adopted in good faith by an organization whose actual application of it violates its core principles, typically because the adopting organization shares some goals but not the framework's analytical integrity requirements.

Concrete examples:
- A nominally "nonpartisan" voter integrity organization uses the framework's election interference analysis to argue for more aggressive voter roll purging, accepting the "election security" framing while rejecting the framework's documentation that the SAVE false-positive rate makes purge-based security illusory
- A corporate governance organization uses the framework's anti-corruption analysis to argue for prosecution of progressive movement leaders, accepting the structural corruption critique while redirecting it away from the executive branch
- A right-leaning think tank uses the war powers analysis to argue for congressional approval of military actions by Democratic presidents while implicitly exempting Republican executive unilateralism

**This failure mode is harder to detect** because the adopting organization will not self-identify as misapplying the framework. They will sincerely believe they are using it correctly. The detection mechanism is therefore the expert reader network — Tier 1 contacts who read the framework carefully will notice distortions in how it is cited by others in their professional communities, and will typically communicate this unprompted if the relationships are maintained.

**Early warning signals**:
- An adopting organization's stated interpretation of the framework diverges from the framework's explicit analytical criteria in the domain they cite
- Secondary citations of the framework come primarily from one ideologically homogeneous community that was not the intended audience
- A Tier 1 contact mentions that the framework is being discussed in their professional community in ways that seem to mischaracterize its purpose
- Media coverage of the framework frames it as a partisan document rather than an institutional analysis

**Detection method**: Cannot be detected through passive monitoring alone. Requires active Tier 1 contact maintenance — the check-in schedule in measurement-and-iteration-framework.md Part II Mechanism 3 is the primary detection protocol. A structured check-in question ("Have you seen the framework cited in ways that seem to mischaracterize it?") will surface Mode 2 signals that no automated tool can detect.

**Response protocol**:
1. Consult Tier 1 contacts immediately on characterization: Is this misapplication, or a legitimate alternative reading?
2. If confirmed misapplication: prepare a public clarification document (not a retort, but a precise statement of what the framework does and does not argue)
3. If the misapplication is public and attributable and has reached a significant audience: publish the clarification through the highest-credibility channel available (Tier 2 academic or journalist who will write it neutrally)
4. If the misapplication is minor: correct the text in the relevant domain file and do not respond publicly

**Threshold for public response**: (a) the misuse is public and attributable, (b) the misuse has reached a significant audience (not a single obscure citation), and (c) a correction would not amplify the bad-faith use. Below this threshold, internal correction and private communication with contacts close to the source are appropriate.

---

**Failure Mode 3: Credibility Association with Erroneous Claims**

Definition: The framework is associated with a claim that is subsequently challenged or disproven, degrading its usefulness as an evidence base. This is the most dangerous failure mode for long-term impact because it is self-inflicted — it arises from the framework's own evidence standards, not from external bad faith.

Concrete examples:
- The framework cites the 81% SAVE false-positive rate (Missouri data); new research from more states finds a significantly different error rate; citations to the framework inherit the potentially outdated figure
- A court ruling directly contradicts a factual claim in a domain (e.g., a federal court finds that the DOJ voter roll litigation is legally authorized, contradicting Domain 37's characterization of the legal theory as without precedent)
- A domain's comparative evidence from another country is subsequently found to be inapplicable in the U.S. context in ways the domain did not acknowledge

**This is self-inflicted and requires no external bad actor.** It arises purely from evidence standards — if the framework does not update when evidence changes, it becomes an unreliable source, and every organization that cited it inherits the credibility problem.

**Early warning signals**:
- A Tier 1 or Tier 2 contact identifies a specific evidence claim as incorrect, outdated, or overstated
- New empirical research contradicts a specific baseline metric or domain factual claim
- A court ruling, regulatory finding, or official government data release directly contradicts factual statements in the framework
- A domain cites a preliminary finding that has since been superseded by more complete data

**Detection method**: Two mechanisms work in combination. First, the two-Tier-1-contact threshold from measurement-and-iteration-framework.md Part II is the primary detection trigger for contested claims. Second, the domain-37-baseline-metrics.md update protocol (monthly re-measure on six specific metrics) is the model to apply to all Tier A domains. Any court ruling, regulatory finding, or empirical publication in a relevant domain should trigger an immediate domain review, regardless of whether a contact flags it.

**Response protocol**: Factual errors are corrected unconditionally. There is no threshold for correction — a single verified factual error triggers an update within 24-72 hours. The update is documented in the domain file with: `Updated: [date] — [nature of update, 1-2 sentences]`. Contacts who have received the prior version should be notified of significant factual corrections; minor clarifications can wait for the next check-in cycle.

---

### Early Warning Dashboard

| Signal | Failure Mode | Detection Source | Response Window |
|--------|-------------|------------------|-----------------|
| Citation by adversarial organization | Mode 1 (Distortion) | Overton / Scholar alert | 48 hours — read citation context |
| Data point cited without analytical context | Mode 1 (Distortion) | Manual citation review | 48 hours — assess context |
| Tier 1 contact reports unexpected citation | Mode 1 or Mode 2 | Direct contact | 24 hours — investigate |
| Adopter's interpretation diverges from domain conclusions | Mode 2 (Capture) | Contact check-in | 72 hours — consult Tier 1 contacts |
| Secondary citations from homogeneous adversarial community | Mode 2 (Capture) | Overton source analysis | 1 week — assess pattern |
| Tier 1 contact identifies specific evidence claim as wrong | Mode 3 (Credibility) | Direct inbound | 24 hours — begin domain review |
| Court ruling contradicts domain factual claim | Mode 3 (Credibility) | Litigation tracker / news alert | 24 hours — begin domain review |
| New empirical study contradicts baseline metric | Mode 3 (Credibility) | Google Scholar / news alert | 72 hours — update domain |
| No Tier 1 or Tier 2 engagement at Day 60 | Adoption failure | Contact log review | Day 60 — structured check-in |
| Single sector accounts for >70% of citations | Diffusion imbalance | Domain heat map | Day 30 — targeted outreach to lagging sectors |

---

## Part V: Path-Specific Measurement Considerations

### Path A — All 35 Domains, Single Wave

Domain 37 reaches all institutional sectors simultaneously with the rest of the framework. The measurement framework applies uniformly.

**Path A specific actions**:
- Within 72 hours of distribution: Verify all Gist links functional; confirm Google Alerts, Scholar Alerts, and CourtListener alerts are active
- Day 7: First contact log review; identify any initial responses; check Domain 37 specifically (election protection organizations are on the tightest timeline)
- Day 14: Targeted follow-up with non-responding Domain 37 election protection contacts — the NVRA window makes these contacts more time-sensitive than any other Tier 1 outreach
- Day 30: First adoption scorecard; flag any zero-response election protection contacts for emergency check-in

### Path A+37 Hybrid (Recommended)

Path A+37 creates two distinct measurement tracks. Phase 1a (34 domains) generates a general adoption signal; Phase 1b (Domain 37, targeted to 12 election protection contacts) generates a separate election-focused adoption signal that can be analyzed independently.

**Measurement advantage of A+37**: Phase 1b contacts have targeted Domain 37 framing — subject lines keyed to their specific litigation dockets, body copy referencing their current cases. Response rates from Phase 1b contacts can be directly compared to Phase 1a response rates to test whether targeted framing improves adoption velocity for election protection organizations specifically.

**Path A+37 specific actions**:
- After Phase 1a send: Monitor for any election-protection-adjacent responses among the general Phase 1a contacts — these contacts have already seen the framework and will receive Domain 37 as a sequenced follow-on
- After Phase 1b send: Maintain a separate scorecard for the 12 election protection contacts (from DOMAIN_37_SEQUENCING_PLAN.md); track adoption levels independently
- Day 30 post Phase 1b: Compare Phase 1b adoption scorecard to Phase 1a Tier 1 adoption scorecard; if Phase 1b response rates are higher, this is evidence that targeted framing is worth the two-wave complexity

### Path B — Phase 2 Research First

Path B creates the longest delay before impact measurement can begin, but it also creates the cleanest measurement baseline: all contacts receive the same updated document at the same time.

**Critical pre-distribution action for Path B**: Before any contacts receive the framework, update domain-37-baseline-metrics.md to reflect developments between the May 4 baseline and the actual distribution date. The pre-distribution baseline is the reference point against which all post-distribution movement is measured. An outdated baseline produces unreliable impact assessments.

---

## Part VI: 90-Day Measurement Calendar

Counting from distribution Day 0 (whichever path is selected).

### Days 1-7: Infrastructure setup

- Verify all distribution Gist links active and tracking page views
- Activate all monitoring tools (Overton alerts, Google Scholar alerts, Google News alerts, CourtListener alerts)
- Upload all domain documents to SSRN with appropriate metadata and subject categories
- Populate adoption scorecard with all outreach contacts
- Establish contact log baseline
- Day 7 checklist (see adoption-tracking-dashboard-spec.md Component tracking template)

### Days 8-30: First signal window

- Day 14: Follow-up with non-responding Tier 1 contacts; targeted and specific (not mass follow-up)
- Day 21: First domain heat map review — which domains have generated any engagement signal?
- Day 30: First adoption scorecard review
  - Target: 3-5 Level 1 or Level 2 adoption events
  - Flag: Domain 37 contacts who have not responded — NVRA window is narrowing (August 7 is ~99 days from distribution Day 0)
  - Flag: Any citation in adversarial source (Mode 1 early warning check)
  - Action trigger: If zero Tier 1 responses after 30 days, check delivery before redesigning strategy (emails to spam, Gist links broken)

### Days 31-60: Institutional absorption window

- Week 5: Structured check-in call or email with all Tier 1 contacts who have responded; specific questions about use (see measurement-and-iteration-framework.md Part II Mechanism 3 for check-in protocol)
- Day 45: First SSRN citation check (manual search)
- Day 60: Second adoption scorecard
  - Target: 8-12 adoption events; at least 2 Level 3
  - Flag: Any Tier 3 operational adoption signals (organizations using the framework in active work)
  - Flag: Any Mode 2 or Mode 3 failure signals identified through check-ins
  - Action trigger: If Domain 37 has fewer than 2 Level 2+ events at Day 60, execute emergency check-in with Democracy Docket and Campaign Legal Center contacts — the NVRA window is within 47 days of this checkpoint

### Days 61-90: Pre-NVRA assessment

- Day 75: State AG coalition monitoring pass — check the 22 coalition AG press release archives for any election protection filings, coalition letters, or amicus briefs
- Day 80: Pre-NVRA quiet period checkpoint (August 7 is approximately 28 days away at this point if distribution occurred on May 6)
  - Assess whether election protection organizations have incorporated Domain 37 analysis into active litigation or public statements
  - Check domain-37-baseline-metrics.md Metrics 1, 2, and 6 against current data — have any of the seven baselines moved?
  - CourtListener search for any new AG filings in DOJ voter roll cases citing baseline data
- Day 90: Comprehensive review
  - Full citation scan: Overton, Google Scholar, PACER/CourtListener, Congress.gov, SSRN
  - Contact intelligence synthesis across all tiers
  - Domain heat map: which domains have zero events at Day 90?
  - Phase 2 domain prioritization update based on revealed demand signals
  - Failure mode assessment: have any Mode 1, 2, or 3 signals materialized?
  - 90-day report to personal record (see adoption-tracking-dashboard-spec.md Month 3 Snapshot template)

---

## Appendix A: Measurement Infrastructure Summary

**Infrastructure already established** (no setup required at distribution):
- Brennan Center DOJ voter roll tracker — brennancenter.org/our-work/research-reports/tracker-justice-department-requests-voter-information
- Wisconsin SDRI DOJ lawsuit tracker — statedemocracy.law.wisc.edu/tracker-doj-lawsuits-states-voter-data/
- Democracy Docket cases database — democracydocket.com/cases
- Domain 37 pre-distribution baselines — domains/domain-37-baseline-metrics.md (7 quantified metrics with re-measure protocol)
- Adoption scorecard schema — adoption-tracking-dashboard-spec.md Component 2
- Bridge node tracking templates — measurement-and-iteration-framework.md Part III

**Infrastructure to activate at distribution**:
- Overton alerts (overton.io) — 30-minute setup; activate on Day 0
- Google Scholar profile + alerts (scholar.google.com) — 10-minute setup; activate before distribution
- SSRN document uploads (ssrn.com) — 30-60 minute setup per document; complete before distribution
- Google News alerts (news.google.com/alerts) — 15-minute setup; activate on Day 0
- CourtListener docket monitors (courtlistener.com) — 20-minute setup; activate on Day 0
- LegiScan API search alerts (legiscan.com) — 30-minute setup; activate on Day 0

---

## Appendix B: Domain Coinage Glossary for Search Alerts

The following phrases appear in the framework but not in standard policy or legal vocabulary. They function as fingerprints — any document using them has been influenced by the framework, whether or not it cites directly.

| Phrase | Domain | Alert type |
|--------|--------|------------|
| "arrest operation theory" + "war powers" | Domain 28 | Google Scholar + Overton |
| "Section 3 enforcement gap" + "appropriate legislation" | Domain 37a | Google Scholar |
| "Vance doctrine" + "Youngstown" | Domain 19f/28 | Google Scholar + News |
| "81 percent" + SAVE + voter rolls | Domain 37 (Metric 6) | Google News + Scholar |
| "ESG activation" + midterm + election | Domain 37 (Metric 2) | Google News |
| "state legislative autocratization" | Domain 33 | All tools |
| "appellate capture" + judicial independence | Domain 6 | All tools |
| "fiscal authority bypass" + OMB | Domain 34 | Google News + Scholar |
| "election denier" + CISA + cybersecurity | Domain 37 | Google News |
| "ICE-at-polls" | Domain 37 | All tools |

Set Google News, Google Scholar, and Overton alerts for each phrase. Any document using these phrases without citing the framework is a Mode 2 (capture) or positive influence signal — context determines which.

---

*Version 2.0 — May 6, 2026. Supersedes Session 688 version. Review at 30, 60, and 90 days post-distribution. Companion documents: adoption-tracking-dashboard-spec.md (Session 717, production-ready); measurement-and-iteration-framework.md (Session 546, operational). Sources: [Overton.io policy impact methodology](https://www.overton.io/policy-impact) | [CourtListener / RECAP](https://free.law/recap/) | [Democracy Docket cases](https://www.democracydocket.com/cases/) | [NAAG](https://www.naag.org/) | [LegiScan](https://legiscan.com/) | [SSRN](https://www.ssrn.com/) | [LSE Impact Blog, policy citation databases](https://blogs.lse.ac.uk/impactofsocialsciences/2022/03/23/policy-citation-databases-offer-new-ways-to-understand-the-impact-of-social-sciences-research/) | [Brennan Center DOJ voter roll tracker](https://www.brennancenter.org/our-work/research-reports/tracker-justice-department-requests-voter-information) | [Wisconsin SDRI tracker](https://statedemocracy.law.wisc.edu/tracker-doj-lawsuits-states-voter-data/)*
