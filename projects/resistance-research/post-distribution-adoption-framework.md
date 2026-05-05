---
title: "Post-Distribution Institutional Adoption Tracking Framework"
date: 2026-05-04
status: production-ready
phase: Pre-distribution research
project: resistance-research
companion_files:
  - post-distribution-impact-framework.md        # Sector-by-sector operational tracking
  - post-distribution-tracking.md                # Real-time decision trees, Week 1-4 roadmap
  - adoption-tracking-dashboard-spec.md          # Tool specs and alert templates
scope: "Conceptual and analytical framework — historical precedent, diffusion theory, attribution methodology, version tracking, partial adoption patterns"
---

# Post-Distribution Institutional Adoption Tracking Framework

**Research basis**: Policy diffusion literature, Model Penal Code history, ABA Model Rules adoption record, ALEC model legislation empirics, Brennan Center impact model, Rogers Diffusion of Innovations (1962/1995), Overton index methodology.

**What this document is not**: This is not the operational tracking dashboard (see `adoption-tracking-dashboard-spec.md`) or the sector-specific decision trees (see `post-distribution-tracking.md`). This document provides the conceptual architecture underneath those tools: what institutions adopt, why they adopt when they do, how to interpret partial and contested adoption, and how to distinguish framework impact from independent parallel development.

---

## 1. Institutional Adoption Typology

### 1.1 What "Adoption" Means By Institution Type

The failure mode in post-distribution measurement is applying a single adoption standard across sectors with fundamentally different operating logics. A law review "adopting" a framework means something categorically different from a state AG "adopting" it. Without sector-specific definitions, signal interpretation breaks down in both directions — false positives (counting as adoption what is merely awareness) and false negatives (missing adoption that doesn't look like citation).

**State Attorneys General**

Adoption for AG offices is never formal citation and rarely public acknowledgment. AGs adopt frameworks operationally: a domain's analytical structure becomes the implicit organizing logic for a litigation brief, a press release, or a coalition memo, without the framework being named. The correct adoption signal is thematic convergence — when an AG's filings start describing executive overreach using the same pattern-and-practice theory that Domain 16 develops, or when a multi-AG coalition letter structures its argument using the four-mechanism framework from Domain 34 (fiscal authority), those are adoption events even absent attribution.

Measurable adoption thresholds:
- Level 1 (awareness): Documented substantive reply to outreach, or confirmed reading by policy counsel
- Level 2 (reference): Domain language appears in a public AG document (press release, brief, coalition letter) without formal citation
- Level 3 (integration): Framework analysis anchors a litigation theory or formal legal position
- Level 4 (propagation): AG office shares framework internally or to peer AG offices, triggering network diffusion

Timeline to Level 2: 4-8 weeks. Level 3: 2-4 months. Level 4: 3-6 months.

**Law Schools and Law Reviews**

Law schools have three distinct adoption tracks operating on different timelines:

*Clinic adoption* (fastest, most operationally significant): Clinic directors integrate domain analysis into active casework. A voting rights clinic using Domain 1's procedural disenfranchisement framework as its theory of harm, or an immigration clinic using Domain 16's warrantless arrest pattern-and-practice theory, constitutes adoption even if the document is never formally cited. Timeline: 6-12 weeks from contact to first substantive use.

*Faculty adoption* (medium speed, high legitimacy multiplier): A law professor assigns a domain document as course reading, uses its analytical structure in a seminar, or incorporates its framework into their own research. Faculty adoption is a critical bridge because it drives the next stage — student scholarship. Law review notes and comments frequently originate in seminar assignments. Timeline: 4-16 weeks (semester cycle dependent).

*Law review adoption* (slowest, highest legitimacy signal): A law review article cites the framework, applies its analytical structure, or produces a rebuttal or refinement. A formal law review citation is the highest-credibility external validation signal available — it means legal scholars have engaged with the framework as scholarship, not merely as advocacy. Timeline: 12-24 months from submission to publication.

The counterintuitive implication: law review citation is the *last* adoption event to measure, not the first. It is a lagging indicator of adoption that already happened at the clinic and faculty level.

**Think Tanks and Policy Institutes**

Think tanks adopt frameworks by incorporating their analytical vocabulary into published research. The adoption gradient runs from surface to structural:

- Surface adoption: A Brennan Center or CAP brief uses a term or concept first developed in the framework (e.g., "state legislative autocratization," "appellate capture") — this is adoption of a coinage
- Framework adoption: A think tank report applies the framework's analytical structure to a new problem domain — this is adoption of method
- Strategic adoption: A think tank builds a multi-report research agenda around the framework's gaps or extensions — this is adoption as research direction

Think tanks are the fastest institutional sector to produce public output (2-6 week report turnaround is standard), making them the first place measurable public adoption signal appears. They are also the highest-velocity legitimacy multipliers: a Brennan Center report citing the framework reaches journalists, legislative staff, and AG offices through established distribution channels, driving secondary adoption.

**Labor Unions**

Union adoption is primarily instrumental and domain-specific. Research departments at large national unions (AFL-CIO, SEIU, AFSCME) read policy frameworks for domains with direct worker impact — labor policy (Domain 15), healthcare (Domain 31), fiscal authority (Domain 34), and electoral interference (Domain 37). Adoption manifests as: incorporation into collective bargaining research materials, testimony before Congress or state legislatures, public education materials for members, or campaign integration.

The strategic leverage point with unions is that they are both end-users and distribution infrastructure. A union that adopts Domain 37 (federal electoral interference) as part of its get-out-the-vote research becomes a distribution node reaching millions of members.

**Journalists and Media**

Journalistic adoption operates on a different logic than institutional adoption. Journalists adopt analytical frameworks as interpretive lenses — they do not cite them, they use them to frame stories. Adoption is best measured not by citation but by vocabulary migration: when a reporter at ProPublica or The Atlantic starts describing executive enforcement patterns using the framework's analytical categories, the framework has been adopted as a journalistic lens.

This is why media coverage metrics (article count, unique outlets) are less useful than vocabulary analysis. The meaningful signal is whether the framework's concepts are appearing in reporting as unmarked analytical background — the transition from "the administration is using ICE aggressively" to "the administration has created an enforcement pattern that courts have found exceeds statutory authority in 14 of 16 reviewed cases" is a vocabulary migration event.

Journalists also serve as framework modification accelerators: they interview critics and practitioners whose responses to framework concepts reveal where the analysis is contested or incomplete, which drives the version tracking cycle described in Section 4.

---

### 1.2 Historical Precedent: How Similar Frameworks Diffused

Three historical case studies offer the clearest empirical baselines for the Democratic Renewal Framework's expected diffusion pattern.

**The Model Penal Code (1962 — 10-year development, 36-state adoption)**

The MPC is the most successful law reform framework in American legal history. Developed by the American Law Institute over a decade (1952-1962) with Herbert Wechsler as chief reporter, it had no enforcement mechanism and no official status in any jurisdiction. It was purely a model.

The diffusion pattern: law schools adopted first (the MPC became standard criminal law pedagogy within 3-5 years of publication), then state legislative drafters used it as a template, then courts cited it as persuasive authority in statutory interpretation. Thirty-six states adopted new criminal codes influenced by the MPC. Several (New Jersey, New York, Oregon) adopted it nearly wholesale. The full adoption wave lasted approximately 15 years from publication.

Key diffusion mechanisms that are directly applicable:
- *The prestige anchor*: The ALI's institutional credibility meant law schools adopted without individual faculty resistance. The parallel for the Democratic Renewal Framework is early adoption by a recognized institution (a T14 law school clinic, a leading think tank, or a state AG coalition) that creates an implicit credibility signal for secondary adopters.
- *The lagging legislative signal*: In the MPC case, legislative adoption followed law school and practitioner adoption by 3-7 years. The framework was shaping legal culture and building a constituency for statutory reform years before it appeared in legislation. Early absence of legislative citation does not mean failure; it means the institutional groundwork phase is still running.
- *Partial adoption as the norm*: No state adopted the MPC unchanged. Every adopting state modified provisions to reflect local political constraints. The partial adoption rate was higher than the full adoption rate. This is not framework failure — it is successful framework functioning. The MPC is considered a success precisely because it shaped the terrain of the debate in every adopting state, including states that rejected core provisions. The Democratic Renewal Framework should expect and plan for partial adoption as the dominant adoption mode, not the exception.

**The ABA Model Rules of Professional Conduct (1983 — All 50 states adopted within 20 years)**

The Model Rules replaced the 1969 Model Code and addressed attorney professional responsibility. Starting from zero adoption in 1983, all 50 states and DC had adopted rules based on the Model Rules within approximately 20 years. The key mechanism: the bar exam (specifically the Multistate Professional Responsibility Examination, MPRE) created an enrollment mechanism that guaranteed law students learned the framework regardless of whether faculty preferred it.

The Democratic Renewal Framework has no equivalent enrollment mechanism. This is significant. The ABA Model Rules' near-total adoption is partly attributable to the fact that every prospective attorney has to pass a test based on them. Without a forced-enrollment mechanism, diffusion depends entirely on pull — institutions choosing to engage because the framework meets a real need.

The implication for the 6-month roadmap: do not expect anything approaching the ABA's eventual adoption breadth in the first year. The ABA's near-universal adoption took two decades, and it had structural advantages (testing requirement, mandatory bar membership, practitioner-facing content) that a policy framework lacks. The correct comparison is the first three years of the ABA Model Rules' adoption cycle, not the 20-year completed picture.

**The Brennan Center Institutional Model**

The Brennan Center's impact model — part think tank, part public interest law firm, part advocacy organization — is the closest structural analog to the Democratic Renewal Framework's intended positioning. The Brennan Center's automatic voter registration (AVR) research provides the clearest diffusion case: the Center produced rigorous research identifying the policy problem (eligible citizens failing to register), designed a specific legislative solution (automatic registration), built a coalition of advocacy organizations to advance it, and tracked legislative adoption state by state.

Result: 19 states and DC adopted AVR. This took approximately 10 years from the Brennan Center's focused campaign (roughly 2010-2020).

The distributable lesson: the Brennan Center's success was not primarily about the quality of its research. It was about having a specific, actionable legislative solution that was cheap to adopt, had minimal opposition in sympathetic state legislatures, and whose advocacy was coordinated across organizations. The Democratic Renewal Framework's domains that have the highest adoption probability in the first 6 months share these characteristics — they have clear, bounded legislative proposals (not systemic reform requiring constitutional amendment), and they address problems that sympathetic institutions (Democratic AGs, progressive state legislatures, voting rights organizations) already want to solve.

Domains with Brennan Center-like adoption profiles (high specificity, low adoption friction):
- Domain 1 (voting rights — specific procedural protections), Domain 34 (fiscal authority — specific congressional oversight mechanisms), Domain 37 (election interference — specific CISA budget and election security requirements)

Domains with MPC-like adoption profiles (high ambition, slower legislative adoption, faster academic adoption):
- Domain 6 (judicial independence — structural court reform requiring legislation), Domain 35 (SCOTUS reform — constitutional-level changes), Domain 26 (government accountability — institutional redesign)

---

## 2. Six-Month Adoption Roadmap

### Weeks 1-4: Early Adopter Phase

The first four weeks are the highest-volatility phase. Early adopter behavior in the first month is not predictable from the framework's content quality alone — it depends on timing, recipient circumstances, and whether a triggering event creates immediate relevance.

**Expected early adopters** (institutions most likely to engage in weeks 1-4):

*Digital rights organizations* (EFF, ACLU's Project on Speech, Privacy and Technology): These organizations have the fastest internal processing speed and the most permeable institutional boundaries. Staff can engage with new analytical frameworks without waiting for executive director approval. Domain 25 (surveillance) and Domain 36 (AI governance) will likely generate the first meaningful responses here, because these organizations are already tracking the specific policy failures those domains analyze.

*Law review editors at T14 schools*: Law review submissions committees meet regularly and can flag externally produced analytical frameworks as basis for invited symposia or note topics within 3-6 weeks of receiving materials. The fastest path to early adoption signal in the law school sector is not faculty engagement (which requires semester timing) but law review engagement.

*State AG policy counsel already in coalition*: The 24 state AGs with active litigation coordination networks (the States United Democracy Center and Democracy Docket networks) have policy staff who read new analytical material as part of routine litigation preparation. Domain 1, Domain 16, and Domain 29 are most likely to generate early response because they map to active litigation dockets.

**Leading indicators that predict eventual wide adoption** (week 1-4 signals):

1. *Vocabulary migration in the first 30 days*: Does any public output from a Tier 1 contact (press release, blog post, tweet thread) use a term or analytical frame that first appeared in the framework? Vocabulary migration in week 1-4 is a stronger predictor of eventual adoption than a formal reply, because it means the framework has been internalized, not merely acknowledged.

2. *Unprompted secondary distribution*: Does any contact share the materials to a peer network without being asked? This is the single strongest 30-day indicator of eventual wide adoption. In Rogers' diffusion framework, the transition from innovator to early adopter happens through trusted peer referral — if a Tier 1 contact is actively passing the framework to their network, the S-curve has begun.

3. *Domain-specific requests*: Does any contact ask for more material on a specific domain, or request to speak with someone who worked on it? A request for elaboration means the contact has moved from awareness (read it) to engagement (thinking with it).

### Months 2-3: Secondary Diffusion Phase

By month 2, the first-mover coalition's adoption behavior is visible. The measurement question shifts from "who is engaging?" to "what are they doing with it?"

**Expected secondary diffusion pattern**:

Academic programs (law school clinics, political science departments, public policy programs) adopt frameworks on a semester cycle. A framework distributed in May 2026 will appear in Fall 2026 syllabi if it reaches course-design decision-makers by mid-June. This creates a hard deadline: the most important 6-week window for curriculum adoption is May-June 2026.

Labor research departments (AFL-CIO, SEIU, AFSCME research divisions) typically have 60-90 day internal review cycles. A framework reaching their research staff in May will likely produce internal research memos by July and public output (testimony, member education materials) by August-September.

Policy journalists covering government accountability typically take 4-8 weeks to integrate a new analytical framework into their interpretive lens. The signal here is not an article about the framework — it is an article about something else that uses the framework's analytical structure without citing it.

**Month 2-3 success threshold**: At least 2 think tank publications citing framework + at least 1 law school clinic confirming active use + at least 5 AG-aligned organizations using domain language in public communications.

### Months 4-6: Institutional Integration Phase

By month 4, the distinction between adoption and integration becomes measurable. Adoption means an institution has used the framework. Integration means an institution has made the framework part of its standard toolkit.

**Integration signals** (harder to achieve but more durable):

*Curriculum integration* (law schools, policy programs): A domain document appearing on a course syllabus as assigned reading, or a domain's analytical framework appearing in a course's problem sets or mock briefs. This requires instructor buy-in and course modification — it is a two-semester lag from awareness to curriculum appearance, meaning May 2026 distribution produces curriculum integration in Fall 2027 at the earliest, not Fall 2026.

*Formal policy proposals*: A state legislative bill or federal bill uses the framework's language in its findings section or committee report. This is the formal legislative acknowledgment that the framework has achieved policy relevance. Timeline: 6-18 months from distribution. The first instance is a significant milestone; it triggers additional legislative staff engagement.

*Litigation references*: An amicus brief or court filing uses the framework's analysis as expert background, or a complaint's factual narrative uses the framework's structural categories. This is the AG sector's integration signal. Timeline: 4-8 months (dependent on docket timing).

**Month 4-6 success threshold**: At least 1 confirmed litigation reference + at least 2 formal policy proposals using framework language + at least 15 organizations integrating specific domain materials into standing research or advocacy infrastructure.

---

## 3. Impact Metrics That Matter

### 3.1 The Measurement Hierarchy

Not all metrics are equally meaningful. The failure mode is optimizing for the most visible metric (media mentions, social shares) rather than the most consequential one (litigation citation, curriculum integration).

**Tier 1 metrics** (highest consequence, hardest to achieve):
- *Litigation references*: A brief or complaint using domain analysis. Measurable via CourtListener and PACER full-text search. Search string: domain title phrases + conceptual coinages ("prosecutorial weaponization," "appellate capture," "state legislative autocratization"). Each litigation reference represents the framework being used as a legal tool — the highest-impact adoption mode.
- *Formal policy proposal citations*: A legislative bill or committee report citing the framework. Measurable via Congress.gov full-text search and state legislative databases (LegiScan, Legiscan API for multi-state). Requires monitoring 50+ state legislatures plus Congress — resource-intensive but unambiguous.
- *Curriculum adoption*: A domain document assigned in a law school or policy program course. Not publicly visible; requires direct contact survey or faculty relationship intelligence. Measurable via annual survey to law school clinic directors and core faculty contacts.

**Tier 2 metrics** (meaningful institutional legitimacy signals):
- *Academic citations in law review articles or working papers*: Measurable via Google Scholar, SSRN, HeinOnline. This is a lagging indicator (12-24 months to publication) but represents peer validation that the framework meets scholarly standards. Overton.io is the most comprehensive policy citation database and can track citations across think tank publications, policy documents, and grey literature — it indexes 21 million documents from 1,000+ sources.
- *Think tank publication citations*: Measurable via Overton.io and direct monitoring of major institutes' publication pages. Faster signal than academic citations (2-6 week publication cycle for think tank reports).
- *Training/curriculum adoption at advocacy organizations*: A national organization incorporating domain materials into member education, staff training, or organizer guides. Measurable via email list monitoring, annual check-in calls.

**Tier 3 metrics** (reach and awareness signals, useful but not sufficient):
- *Media coverage*: Article count, outlet tier, framing quality. Measurable via Google News alerts, Nexis Uni, Muck Rack. Media coverage is high-visibility but low-durability — a ProPublica article mentioning the framework generates awareness but not necessarily adoption. Track media reach (unique visitors to citing articles) vs. media engagement (reader comments indicating substantive engagement with framework concepts).
- *Social media reach*: Shares, quote-tweets, thread engagement. Measurable via platform analytics, Tweetdeck monitoring. Useful for measuring reach among engaged civic audiences; not useful for measuring institutional adoption.

### 3.2 Metric Measurability Windows

| Metric | 90-day window | 6-month window | 1-year window |
|--------|--------------|----------------|---------------|
| Litigation references | Possible (fastest courts) | Expected (1-3 cases) | Reliable (5-15 cases) |
| Policy proposal citations | Unlikely | Possible (state level) | Expected (2-5 bills) |
| Academic law review citations | No | No (submission only) | No (under review) |
| Think tank publication citations | Yes (2-6 week lag) | Yes (3-8 publications) | Yes (ongoing) |
| Curriculum adoption | No | Survey only | Confirmed |
| Media mentions | Yes (immediate) | Yes (cumulative) | Yes (trend analysis) |
| Social shares | Yes (immediate) | Yes | Yes |
| Vocabulary migration | Yes (watch for it) | Yes | Yes |
| AG coalition language use | Yes (if active dockets) | Yes | Yes |

The 90-day window is primarily useful for monitoring awareness signals (Tier 3) and early-mover Tier 2 signals (think tank output, Overton citation). Tier 1 metrics require 6-12 months to materialize in measurable form.

---

## 4. Framework Adaptation Patterns

### 4.1 Which Domains Are Most Likely to Be Modified or Contested

Domain vulnerability to modification is predictable from three factors: empirical contestability (are the underlying facts disputed?), political alignment risk (does the domain require adopters to take a position that alienates part of their coalition?), and reform ambition (does the domain's recommended solution require constitutional change or merely statutory change?).

**High modification likelihood** (adopters will use the analysis but adjust the prescription):

*Domain 6 (Judicial Independence and Reform)*: The diagnosis (coordinated judicial capture through Federalist Society pipeline, dark money, and appointment gaming) is broadly accepted by center-left institutions. The prescription (court expansion, mandatory recusal rules, jurisdiction reform) is politically costly for institutions that want to maintain bipartisan credibility. Expect selective adoption: analysis accepted, structural reform proposals either softened or omitted.

*Domain 35 (SCOTUS October 2026 Term and Post-Loper Landscape)*: Highly time-sensitive — the domain's October 2026 docket predictions become outdated immediately. Adopters will use the Loper Bright doctrinal analysis and the Humphrey's Executor trajectory, but the specific docket sections will require continuous update. This domain needs version cadence rather than static adoption.

*Domain 19f (War Powers Reform)*: The Iran crisis analysis will age rapidly (May 1 deadline section is already historical by distribution time). Adopters — particularly national security law scholars and AG offices — will need the constitutional framework (which is durable) separated from the crisis-specific analysis (which is dated). Expect adoption of the constitutional structure, contestation or replacement of crisis-specific material.

**Low modification likelihood** (high analytical specificity, durable empirical grounding):

*Domain 33 (State Legislative Autocratization)*: The four-mechanism analysis (REDMAP 2.0, state supreme court capture, ballot initiative suppression, voter suppression escalation) is empirically dense and hard to contest. Adopters will use it largely as written because the data is specific, cited, and not politically controversial within the institutions most likely to adopt it.

*Domain 34 (Congressional Power of the Purse Fiscal Authority Reassertion)*: The four-mechanism fiscal assault ($425B+ in withheld appropriations, Category C expansion, Treasury interference, pocket rescissions) is documented with primary source data. Institutional adopters (congressional oversight staff, government accountability organizations) will use this as written because it provides the specific documentation they need.

*Domain 16 (Immigration Enforcement and ICE Accountability)*: The most-used domain in active litigation. AGs have already filed 71 lawsuits in this space; the domain provides supplementary framework for legal arguments already in use. Low modification risk because the framework aligns with existing litigation strategy rather than proposing it.

### 4.2 Tracking Partial Adoption

The Model Penal Code precedent establishes that partial adoption is the norm, not failure. Every state that adopted the MPC modified it. Every institution that adopts the Democratic Renewal Framework will select the domains relevant to their mandate.

**Partial adoption categories**:

*Domain-selective adoption*: An institution adopts 5-10 of the 35 domains and ignores the rest. This is the expected adoption mode for specialized organizations — a voting rights organization will focus on Domains 1, 33, and 37; an environmental organization will focus on Domains 21, 31; a labor union will focus on Domains 15, 31, 34.

Tracking approach: Maintain a domain heat map (introduced in the operational tracking documents) that records which specific domains appear in each adoption event. Over time, the heat map reveals which domains are generating pull and which are not — a domain with zero adoption signal at 6 months is either genuinely irrelevant to adopting institutions or requires re-framing.

*Analytical-selective adoption*: An institution uses the framework's diagnostic analysis but rejects its prescriptions. The government accountability community may adopt Domain 26's analysis of coordinated accountability failure while rejecting or softening its specific statutory reform recommendations. This is analytical adoption without programmatic adoption — valuable but insufficient for policy change.

*Prescription-selective adoption*: An institution adopts the framework's prescriptions (specific statutory reform language, litigation arguments) while citing independent analytical justification. This is the hardest adoption mode to detect because there is no citation or vocabulary signal, only convergence on specific policy proposals.

**Version tracking protocol**:

Domain documents need version updates when three conditions are met:
1. A major institutional adopter identifies a factual error or outdated data point in direct feedback
2. A significant court ruling, legislative development, or executive action changes the empirical baseline (e.g., a new SCOTUS decision changes the doctrinal analysis in Domain 35)
3. The domain's crisis-specific analysis (Iran war powers in Domain 19f, October 2025 SCOTUS term in Domain 35) becomes so outdated that it undercuts the durable constitutional analysis

Version control recommendation: Tag each domain document with a content currency date (current through April 2026). When an update is warranted, produce a "Domain Update" supplement rather than rewriting the base document — this preserves the stable analytical framework while noting new developments. Institutional adopters who have already cited the base document can reference the supplement without their citations becoming obsolete.

---

## 5. Attribution Analysis

### 5.1 The Core Attribution Problem

The Democratic Renewal Framework will be distributed into a space where hundreds of organizations are already working on the same policy problems. Attribution — determining that a given policy outcome or institutional adoption happened *because of* the framework, rather than independently — is one of the hardest problems in policy impact evaluation.

The correct frame is not binary attribution (did we cause this, or didn't we?) but contribution analysis: did the framework meaningfully accelerate, deepen, or coordinate outcomes that might have occurred anyway, and by how much?

### 5.2 Distinguishing Framework-Driven from Independent Parallel Development

**The parallel development problem**: If an AG files a brief using pattern-and-practice theory for ICE enforcement in September 2026, did that happen because Domain 16 provided the analytical framework, or because the AG's policy counsel independently developed the same argument from the same underlying case law?

Several markers distinguish framework-driven adoption from independent parallel development:

*Vocabulary test*: Does the output use terms or coinages that first appeared in the framework? If an AG's brief uses "pattern-and-practice enforcement" — a well-established legal term — that is ambiguous. If it uses "warrantless arrest escalation pattern" — a specific framework coinage — that is a vocabulary marker indicating framework exposure. The operational implication: the framework documents need to include distinctive analytical coinages that serve as traceable vocabulary markers.

*Structural convergence test*: Does the output use the framework's specific organizational structure for analyzing the problem, not just the conclusion? A brief that distinguishes between the four mechanisms of fiscal authority bypass (OMB apportionment abuse, agency fund holds, Treasury interference, pocket rescissions) in the same sequence and with the same taxonomic logic as Domain 34 is using the framework's structure, not just arriving at the same conclusion.

*Timing and contact test*: Did the output appear after documented contact with the framework, and within a plausible processing window? A think tank report using Domain 33's four-mechanism analysis that is published 6 weeks after the framework was distributed to that think tank is prima facie framework-driven. The same report published before distribution is independent development. Reports published 3-6 months after distribution require timing and contact record analysis.

*Network trace*: Can the specific pathway from framework distribution to output be reconstructed? A Tier 1 contact (directly received framework) shares it with a Tier 2 contact (think tank researcher), whose output then cites it — that is a traceable network adoption event. Documented contact records and bridge node tracking (from `adoption-tracking-dashboard-spec.md`) enable this analysis.

### 5.3 Counterfactual Baseline

What policy activity would have occurred without the framework?

The counterfactual baseline for the Democratic Renewal Framework's policy space is high. AGs were filing 71 lawsuits before distribution. The Brennan Center, ACLU, Protect Democracy, and EFF were already working on all 35 domain areas. Law schools and think tanks were already producing analysis on federal overreach.

This means: the framework's marginal contribution is coordination and synthesis, not origination. The correct counterfactual is not "would any of these policy outcomes have happened?" (answer: yes) but "would they have happened faster, at greater scale, or with more cross-domain integration?" The framework's value is in providing the connective tissue between siloed institutional efforts — the synthesis that makes Domain 1 (voting rights) + Domain 33 (state autocratization) + Domain 37 (electoral interference) legible as a unified pattern of democratic deterioration, rather than three separate policy problems.

Attribution claims should therefore focus on:
- *Coordination effects*: Did the framework enable two organizations that were working independently on related problems to recognize the connection and coordinate? (This is measurable via bridge node tracking.)
- *Acceleration effects*: Did institutions that used the framework move from research to action faster than comparable institutions that did not? (This requires a comparison group — organizations in the same sector that did not receive the framework — but is approximable from timing data.)
- *Coverage effects*: Did the framework cause institutions to address domains they were not previously working on? (This is the clearest attribution claim: if a labor union that had no prior work on Domain 6 judicial independence now incorporates it into its legislative agenda, that is a coverage effect attributable to the framework.)

### 5.4 Practical Attribution Protocol

At 6 months, run the following attribution assessment:

1. For each documented adoption event, classify it as: (a) vocabulary-marker adoption, (b) structural-convergence adoption, (c) timing-and-contact adoption, (d) ambiguous
2. For ambiguous cases, apply the counterfactual test: was this organization working on this specific analytical problem before framework distribution? If yes, the framework likely accelerated or refined existing work, not originated it. If no, the framework is the more probable origin.
3. Produce an attribution confidence score for each adoption cluster (sector + domain combination): High (vocabulary marker + timing evidence), Medium (structural convergence only), Low (thematic alignment only).
4. In external communications, use contribution language ("the framework supported and accelerated...") rather than causation language ("the framework caused...") unless the High confidence threshold is met.

---

## Sources

- [Model Penal Code — Wikipedia](https://en.wikipedia.org/wiki/Model_Penal_Code)
- [The American Model Penal Code — Paul Robinson, University of Pennsylvania (2007)](https://scholarship.law.upenn.edu/cgi/viewcontent.cgi?article=1130&context=faculty_scholarship)
- [ABA Model Rules of Professional Conduct — Wikipedia](https://en.wikipedia.org/wiki/American_Bar_Association_Model_Rules_of_Professional_Conduct)
- [Alphabetical List of Jurisdictions Adopting Model Rules — ABA](https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/alpha_list_state_adopting_model_rules/)
- [Brennan Center for Justice — About Us](https://www.brennancenter.org/about-us)
- [ALEC's Influence over Lawmaking in State Legislatures — Brookings](https://www.brookings.edu/articles/alecs-influence-over-lawmaking-in-state-legislatures/)
- [Legislative Influence Detector: Finding Text Reuse in State Legislation — KDD 2016](https://www.kdd.org/kdd2016/papers/files/adf0831-burgessA.pdf)
- [Linking Policy Design and Policy Diffusion — Policy Studies Journal, Wiley (2025)](https://onlinelibrary.wiley.com/doi/10.1111/psj.12591)
- [Policy Diffusion Theory, Evidence-Informed Public Health — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10030077/)
- [Diffusion of Innovations — Everett Rogers (Stanford summary)](https://web.stanford.edu/class/symbsys205/Diffusion%20of%20Innovations)
- [Overton: A Bibliometric Database of Policy Document Citations — MIT Press Quantitative Science Studies](https://direct.mit.edu/qss/article/3/3/624/112760/Overton-A-bibliometric-database-of-policy-document)
- [Impact Tracking — Overton.io](https://www.overton.io/policy-impact)
- [Policy Citation Databases Offer New Ways to Understand Impact — LSE Impact Blog](https://blogs.lse.ac.uk/impactofsocialsciences/2022/03/23/policy-citation-databases-offer-new-ways-to-understand-the-impact-of-social-sciences-research/)
- [The Influence of Amicus Curiae Briefs on the Supreme Court — Columbia Law Review](https://scholarship.law.columbia.edu/cgi/viewcontent.cgi?article=4504&context=faculty_scholarship)
- [Attribution vs. Contribution in Impact Measurement — SOPACT](https://www.sopact.com/use-case/attribution-vs-contribution)
- [CourtListener Citation Lookup Tool](https://www.courtlistener.com/c/)
