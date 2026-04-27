---
title: "Real-Time Crisis Monitoring and Democratic Resistance Tracking Infrastructure"
subtitle: "Phase 3 Candidate 1 — Framework for Keeping the 35-Domain Proposal Distribution-Current"
date: 2026-04-27
status: production-ready
phase: 3
project: resistance-research
word_count: ~3,500
cross_references:
  - first-amendment-suppression.md
  - environmental-rollbacks-tracker.md
  - police-brutality-consent-decree-tracker.md
  - litigation-tracker-2026.md
  - implementation-roadmap.md
  - policy-influencer-mapping.md
  - domains/APRIL_2026_UPDATES.md
related_templates:
  - monitoring/templates/monthly-crisis-snapshot.md
  - monitoring/templates/contingency-trigger-log.md
  - monitoring/templates/coalition-feedback-tracker.md
---

# Real-Time Crisis Monitoring and Democratic Resistance Tracking Infrastructure

*Phase 3 — Implementation Support Infrastructure | April 27, 2026*

---

## The Central Problem This Document Solves

The 35-domain Democratic Renewal Proposal documents crisis conditions as of April 2026. Institutional audiences — law school clinics, AG coalitions, labor unions, congressional staffers — evaluate proposals partly on currency. A proposal that was accurate in April but is three months stale by the time it reaches a Senate staffer in July loses credibility precisely where it matters most: in the actionability window before the November 2026 midterms.

Sessions 529-530 demonstrated what happens when this problem is solved: SAVE Act Senate failure (April 2026) became evidence of a durable GOP institutionalist bloc; Trump v. Wilcox became documentation of judicial capture; the State Department's "Operation Epic Fury" memo became the definitive analysis of War Powers Reform exhaustion. Those updates, totaling 5,720 words across five domains, took one working session each and materially strengthened the proposal's credibility with election-protection organizations and law review editors specifically.

This document formalizes that ad hoc process into a systematic monitoring infrastructure. It answers four questions:

1. **Which of the 35 domains require automated monitoring, and which require human curation?**
2. **How should the implementation roadmap adapt as specific crisis outcomes occur?**
3. **What monthly cadence keeps the framework within two weeks of crisis development?**
4. **Which monitoring data should be published to reinforce the proposal's authority versus kept internal for coalition strategy?**

---

## Part I: The 35-Domain Monitoring Matrix

### Tier 1 — Automated Monitoring (High-Frequency, Low-Context)

These domains generate high-volume, structured data that can be tracked through automated alerts and API monitoring. The events that matter are public, dateable, and appear in structured databases within hours.

**Domain 1 — Voting Rights and Elections**

Primary data sources: Democracy Docket (cases filed, decided, pending — sortable by state and issue); CourtListener docket alerts for Watson v. RNC and Louisiana v. Callais; FEC filings (independent expenditure reports — quarterly, with October pre-election deadlines); Congress.gov API (bill status for SAVE Act follow-on legislation and VRA reauthorization activity). 

Monitoring cadence: Weekly during election cycles (all of 2026); monthly otherwise. Flag triggers: new case filings in voter roll purge litigation; FEC filings showing dark money spending on voter ID campaigns; any Senate vote on electoral legislation.

**Domain 6 — Judicial Independence**

Primary sources: CourtListener docket alerts for Trump v. Slaughter (pending June 2026); SCOTUS orders list (every Monday); Senate Judiciary Committee hearing notices; PACER for Cruz-led impeachment proceedings. SCOTUSblog's [Interim Docket tracker](https://www.scotusblog.com/cases/interim-docket/2025/) and [Orders of the Court](https://www.supremecourt.gov/orders/ordersofthecourt/26) provide near-real-time shadow docket activity.

Flag triggers: any shadow docket emergency application granted or denied in a domain-relevant case; Senate Judiciary hearings on judicial conduct; any Article III judge removal or impeachment vote.

**Domain 29 — Prosecutorial Weaponization and DOJ Capture**

Primary sources: PACER docket alerts (SPLC v. United States); DOJ press releases (kash-patel-era announcements pattern-trackable by subject); Reporters Committee for Freedom of the Press; Just Security's [Anti-Corruption Tracker](https://www.justsecurity.org/117267/anti-corruption-tracker/).

Flag triggers: new indictments of civil society organizations; congressional subpoenas to journalists; DOJ press conferences announcing investigations of Democratic officials.

**Domain 33 — State Legislative Autocratization**

Primary sources: Democracy Docket state cases; Brennan Center state legislative tracker; LegiScan API (50-state bill monitoring — supports keyword search for "ballot initiative," "redistricting," "preemption"); Ballotpedia state legislation database.

Flag triggers: any state passing supermajority requirements for ballot initiatives; any mid-decade congressional redistricting attempt; dark money state supreme court race filings.

**Domain 34 — Congressional Power-of-the-Purse**

Primary sources: OMB apportionment reports (published quarterly); CBO's Budget and Economic Outlook; GAO appropriations law reports; USASpending.gov (obligation data, can flag holds vs. obligations).

Flag triggers: any OMB Category C apportionment exceeding 8% of a discretionary account; any agency refusing to spend specifically appropriated funds; new GAO budget cut proposals.

**Domain 37 — Federal Executive Interference in 2026 Midterms**

Primary sources: CISA election security press releases; EAC (Election Assistance Commission) security advisories; DHS Secretary statements on election administration; Democracy Docket for executive order challenges; DOJ voter roll litigation tracker (23 active cases as of April 2026).

Flag triggers: any new DOJ suit against state voter roll procedures; any CISA budget cut passing committee; any ICE enforcement announcement tied to election calendar.

---

### Tier 2 — Human-Curated Monitoring (Medium-Frequency, High-Context)

These domains require interpretive judgment to assess whether new developments materially change the proposal's analysis. Automated alerts capture the raw events; a coordinator must decide whether each event crosses the threshold for a domain update.

**Domain 2 — Civil Service and Executive Constraint**

Raw data source: OPM workforce statistics (available quarterly); MSPB appeal statistics; Federal circuit decisions on Schedule F/Policy; union grievance filings. Human curation needed: distinguishing personnel actions that represent Schedule F escalation from normal attrition requires knowledge of which agencies and which positions are affected.

**Domain 9 — Federalism and State-Federal Conflict**

Raw data source: National Governors Association statements; AG coalition press releases (track via NAAG and individual AG websites); interstate compact activity (uniform law commission). Human curation needed: the significance of a state-federal conflict depends on which state, which coalition composition, and whether the conflict involves a legal challenge or purely political resistance.

**Domain 11 — Healthcare Access**

Raw data source: CMS guidance pages; HHS Secretary testimony; KFF Medicaid tracker; National Rural Health Association hospital closure data; Protect Our Care litigation tracker. Human curation needed: Medicaid guidance documents require substantive analysis — "technical corrections" can contain material policy changes. Coordinate with the June 2026 work requirement HHS guidance deadline.

**Domain 19f — War Powers Reform**

Raw data source: Senate.gov roll call votes; White House communications to Congress (WPR section 4 notifications); State Department legal office publications; Congressional Research Service reports. Human curation needed: the Iran situation is legally dynamic — each new State Department memo or Senate vote attempt requires assessing whether it materially changes the constitutional exhaustion analysis.

**Domain 27 — Higher Education and Academic Freedom**

Raw data source: AAUP statements; university press releases on federal funding holds; State Department visa revocation announcements; FIRE (Foundation for Individual Rights and Expression) campus incident tracker. Human curation needed: distinguish between funding holds that are leverage (negotiable) and funding cuts that are irreversible institutional damage; distinguish between individual student visa cases (individual domain) and pattern-establishing visa campaigns (domain 27 territory).

**Domain 28 — War Powers Venezuela**

Raw data source: Congressional Research Service legal memos; DOJ Office of Legal Counsel publications; Senate Armed Services Committee hearings. Human curation needed: the arrest-operation framing as WPR avoidance has been set as precedent; future monitoring is about whether subsequent operations use the same legal theory.

**Domain 35 — Supreme Court 2026 Term Preview**

Raw data source: SCOTUSblog cert-stage monitoring (petitions, responses, distributed for conference); SCOTUS orders lists; oral argument transcripts. Human curation needed: cert grant significance depends on which legal question is presented, which circuits are in conflict, and whether the case falls within the proposal's reform pathway domains.

---

### Tier 3 — Coalition-Fed Monitoring (Low-Frequency, High-Leverage)

These domains require input from actual reform constituencies whose operational knowledge exceeds what public data captures. The proposal's distribution strategy (policy-influencer-mapping.md) creates natural feedback channels.

**Domain 23 — Trade Policy and Tariff Unilateralism**

Coalition source: Business Roundtable litigation updates; Chamber of Commerce Section 301 investigation tracking; Court of International Trade filings (24 state AG challenge). These actors have first-hand knowledge of litigation timeline and business impact data that is not publicly reported.

**Domain 26 — Government Accountability and Institutional Resilience**

Coalition source: POGO (Project on Government Oversight), CREW (Citizens for Responsibility and Ethics in Washington), MERIT Systems Protection Board case pipeline, Inspector General community (if any IGs remain). These organizations track accountability failures in real time.

**Domain 31 — Healthcare Access / OBBBA Medicaid Crisis**

Coalition source: Georgetown Center for Children and Families state-by-state tracking; KFF monthly enrollment data; Families USA impact reports; state Medicaid director communications (tracked through NAMD — National Association of Medicaid Directors). The June 2026 HHS guidance window is the primary advocacy alert — this coalition will know before public reporting whether the guidance has substance.

---

## Part II: Implementation Roadmap Adaptation Triggers

The three-wave implementation roadmap (implementation-roadmap.md) was written in April 2026 against a specific set of assumptions. The following trigger table documents which assumptions are load-bearing and what changes to the roadmap when each assumption is violated.

### Wave 1 Trigger Table (0-18 Months from Recovery Initiation)

| Trigger Event | Load-Bearing Assumption | Roadmap Adaptation Required |
|---------------|------------------------|----------------------------|
| 2026 midterms: House flips to Democratic control | Wave 1 success criteria met; courts + Congress provide floor | Accelerate Wave 2 (parallel institution building) — compress 6-36 month window to 6-24 months |
| 2026 midterms: House stays Republican, but <10-seat margin | Wave 1 partial success — courts constrain but Congress doesn't | Extend Wave 1 defense phase; focus on AG coalition + state-level action; Wave 2 preparation begins without legislative partner |
| Trump v. Slaughter decided against independent agencies (June 2026) | Domain 6 assumption that some judicial backstop remains | Update Domain 6 reform pathways; statutory options require explicit Constitutional amendment framing; add to Wave 1 urgency list |
| Iran WPR 60-day window expires without compliance (post-May 1) | Domain 19f assumption that process exhaustion is gradual | Document complete enforcement mechanism exhaustion; update Domain 19f Section 9 with post-deadline outcome; changes Phase IV risk assessment (Domain 34 funding cutoff mechanism compromised) |
| SAVE Act or equivalent passes Senate (60-vote threshold broken) | Domain 1 assumption that filibuster protects electoral legislation | Update Domain 1 coalition analysis; identify which GOP senators flipped and why; assess vulnerability of other protective thresholds |
| CISA election security program defunded in FY27 appropriations | Domain 37 assumption that some federal election infrastructure remains | Trigger Domain 37 contingency scenario B (state-only election security); update Wave 1 success criteria for elections domain |

### Wave 2 Trigger Table (Months 6-36)

| Trigger Event | Load-Bearing Assumption | Roadmap Adaptation Required |
|---------------|------------------------|----------------------------|
| 2026 State elections: AG coalition expands from 22 to 28+ states | Domain 9 and coalition strategy assume existing coalition size | Expand coalition-specific playbook; 28 states crosses threshold for interstate compact formation without federal authorization |
| Medicaid work requirements effective January 2027 with no injunction | Domain 11 assumes litigation blocks or delays implementation | Update Domain 11 with live implementation data; shifts reform window from "prevent" to "reverse" — different litigation strategy and advocacy targets |
| North Carolina 2026 state supreme court captures additional seat | Domain 33 assumption that some state courts remain independent | Update state-level legal strategy; identifies states where redistricting legal challenge is no longer viable; shifts recommendations toward ballot initiative defense |
| Section 702 lapses without reauthorization | Surveillance tracking assumption that some oversight framework persists | Document the shift to EO 12333 authorities; update Domain 21 analysis; adds urgency to state-level data privacy legislation (Domain 21 + Domain 33 intersection) |

### Wave 3 Trigger Table (Months 18-60)

Wave 3 triggers are structurally different — they represent long-horizon conditions that cannot be actively monitored but should be checked at the six-month domain refresh cycle.

| Trigger Condition | Assessment Point | Roadmap Adaptation |
|------------------|-----------------|-------------------|
| 2030 Census redistricting cycle — state legislature composition | January 2031 (whoever controls state legislatures draws maps) | Domain 33 long-horizon tracker; identifies which 2026 state legislative races are most consequential for 2031 map-drawing |
| Second SCOTUS vacancy (expected 2027-2029) | Monitor SCOTUS justice health/retirement signals | Domain 6 and Domain 35 reform viability assessment; any vacancy changes the reform pathway analysis for constitutional amendments |
| Federal AI governance statute enacted or blocked | Ongoing — no fixed window | Domain 36 regulatory gap analysis; determines whether state AI authority floor (Domain 36 Section 6) is the primary implementation pathway |

---

## Part III: Monthly Refresh Cadence

### The "Two-Week Currency" Standard

The proposal remains credible with institutional audiences if domain content is within two weeks of the most significant crisis development in that domain. The April 2026 updates cycle (Sessions 529-530) demonstrates this standard is achievable: six domains updated across two sessions using WebSearch + WebFetch against primary sources, producing 5,720 words of new content with 45 citations.

The two-week standard means: if a major ruling (Trump v. Slaughter), significant legislation (SAVE Act final vote), or documented executive action (State Department WPR memo) occurs, the relevant domain document should be updated within two weeks. For distribution to institutional audiences — law school clinics, AG offices, think tanks — that standard is what distinguishes a live proposal from an archived document.

### Monthly Refresh Protocol

**First week of each month — Automated Monitoring Review (2-3 hours)**

Run the Tier 1 monitoring checks across all six automated domains. For each domain: has a flag trigger been crossed? If yes, queue for domain update session. If no, note the domain as current and move on. Deliverable: updated status line in PROJECTS.md (Domains 1, 6, 29, 33, 34, 37 — status and last-checked date).

**Second week — Monthly Crisis Snapshot (3-4 hours)**

Complete the Monthly Crisis Snapshot template (see templates/monthly-crisis-snapshot.md). Identify which 5-7 domains are most urgent based on: (a) pending court decisions with known deadlines, (b) legislative action windows, (c) coalition feedback from Tier 3 sources. The snapshot is the planning document for the month's domain update work.

**Third week — Domain Update Sessions (variable, typically 4-6 hours)**

Execute domain updates for any flagged domains. Priority order: (1) domains with pending advocacy windows closing within 30 days, (2) domains cited by coalition contacts as most urgent, (3) domains with pending court decisions that will materially change the analysis.

**Fourth week — Distribution Integration**

Update the executive summary and proposal's Part I introduction to reflect new domain findings. If a significant new development warrants a standalone update brief (as distinct from a domain document update), draft it here. These standalone update briefs are the primary vehicle for reaching audiences who have already received the proposal — they reinforce currency without requiring re-reading the full document.

### Annual Structural Refresh (January and June)

Twice per year, the full 35-domain matrix should be reviewed against the trigger tables above. This is not routine maintenance — it is a structural assessment of whether the implementation roadmap's assumptions remain valid. The assessment should produce: (a) updated trigger table with new assumptions identified, (b) any domains that need full rewrites rather than incremental updates, (c) any new domains that warrant addition to the framework.

---

## Part IV: Publication Versus Coalition-Internal Data

### What Should Be Published

**Domain update documents** — when a domain is updated with new citations and analysis, that update should be distributed to the proposal's recipient list with a one-paragraph summary of what changed and why. This serves two functions: it demonstrates the proposal's ongoing currency to audiences who are evaluating whether to act on it; and it gives coalition contacts who have not yet engaged a second-touch reason to read the proposal.

**Monthly Crisis Snapshots (selective)** — the snapshot's identification of which 5-7 domains are most urgent can be published as a "Current Alerts" section on a public-facing Substack post or brief. The urgency ranking serves as a news hook — it tells journalists, advocates, and policy staff what the framework's current assessment is without requiring them to read 35 domains.

**The litigation tracker** — the litigation-tracker-2026.md document is already designed for public distribution. Any significant new case additions (especially cases filed against voting rights, judicial independence, or executive overreach) should be distributed immediately via the channels already mapped in policy-influencer-mapping.md.

**The three public trackers** — first-amendment-suppression.md, environmental-rollbacks-tracker.md, and police-brutality-consent-decree-tracker.md are already framed as public reference documents. Monthly update notes (section headers with dates) make these documents function as live resources rather than static reports.

### What Should Be Kept Internal for Coalition Strategy

**Contingency trigger logs** — the specific analysis of which implementation roadmap pathways close under which adverse outcomes is strategic planning information. Publishing it alerts opposing actors to which outcomes matter most to the reform coalition, enabling targeted efforts to produce those outcomes. The trigger analysis should be shared with high-trust coalition contacts (Tier 1 contacts from policy-influencer-mapping.md) under distribution norms that prevent further dissemination.

**Coalition feedback tracking** — which organizations have engaged with which domains, and what their specific concerns or additions are, constitutes strategic intelligence about coalition formation. This information should inform domain sequencing and advocacy messaging but not be published.

**The adversary response section of the Contingency Trigger Log** — assessments of which opposition responses are most likely for each domain should be shared only with coalition partners who have agreed to work on implementation, not distributed broadly.

**Engagement metrics and contact pipeline** — tracking which Tier 1 contacts have received the proposal, whether they responded, and what their specific feedback was is operational information that, if published, would compromise the relationship-building dynamic that makes the distribution strategy work.

---

## Part V: Integration with Existing Trackers

### First Amendment Suppression Tracker

The first-amendment-suppression.md document currently covers press crackdowns, protest restrictions, platform coercion, and SLAPP litigation. Its monitoring protocol should be connected to:

- **Domain 7 (Democratic Participation and Political Rights)** — Tier 2 human-curated domain. Each new Section 1 (Press Crackdowns) entry in the First Amendment tracker should be assessed for whether it crosses the threshold for a Domain 7 update. The threshold is: does this case establish a new mechanism or materially worsen the existing mechanism? Pentagon corridor closure was a threshold event; individual press pool decisions are not.

- **Domain 29 (Prosecutorial Weaponization)** — The SPLC indictment was a threshold event in both documents simultaneously. Future civil society prosecutions should trigger simultaneous entries in the First Amendment tracker (Section 7: civil society prosecution) and Domain 29 (new case study for the prosecutorial pattern).

- **Monthly update cadence**: First Amendment tracker entries should be reviewed at the start of each month to identify whether any new entry warrants promotion into the monthly crisis snapshot as a high-urgency item. The tracker is the raw data source; the monthly snapshot is the prioritized output.

### Environmental Rollbacks Tracker

The environmental-rollbacks-tracker.md is the most comprehensive of the three public trackers — 28+ entries with agency-by-agency structure, litigation status, and confidence levels. Its monitoring integration points are:

- **Domain 12 (Environmental Justice and Climate)** — the rollbacks tracker is the evidentiary base for Domain 12. Any rollback entry that has a finalized effective date, surviving litigation, should be flagged as a Domain 12 update candidate. The Endangerment Finding effective date (April 20, 2026) is the canonical example of an event that crossed the threshold.

- **Domain 9 (Federalism)** — state AG coalitions challenging environmental rollbacks (22 state AGs on the Endangerment Finding) are documented in the tracker but also relevant to Domain 9's AG coalition analysis. Track whether the environmental coalition membership overlaps with and reinforces the broader 22-state AG coalition.

- **Monthly protocol**: the environmental tracker's litigation status entries should be checked against Earthjustice, NRDC, and Environmental Defense Fund dockets monthly. Entries marked [PROPOSED] that become [FINAL] cross a monitoring threshold and should update the tracker within one week.

### Police Brutality Consent Decree Tracker

The police-brutality-consent-decree-tracker.md documents the May 21, 2025 DOJ rollback and city-by-city compliance tracking. Its integration points are:

- **Domain 7 (Democratic Participation)** — consent decree defiance is directly related to protest policing and the democratic right of assembly. The 10th Circuit Denver protest policing ruling (Pattern 6 in the tracker) is simultaneously a Domain 7 event (protest policing circuit split) and a consent decree event.

- **Domain 6 (Judicial Independence)** — the pattern of administration defiance of court orders in the consent decree context is the same pattern documented in Domain 6 for immigration and political cases. Cases like Boasberg, Xinis, and the Minneapolis consent decree dismissal share a common mechanism: the administration discovers procedural arguments rather than complying. Track these together under a shared "court order defiance" flag in the monthly snapshot.

- **Monthly protocol**: the Cleveland and Oakland open research threads (per the tracker's April 2026 update) should be checked monthly against CourtListener docket alerts. The Cleveland ruling has been pending since late April 2026 and will cross a monitoring threshold when issued.

---

## Part VI: Coalition Feedback Architecture

### How Institutional Engagement Feeds Back into Domain Selection

The policy-influencer-mapping.md document identifies 150+ contacts across three tiers. As those contacts receive the proposal and respond, their engagement produces domain-specific intelligence that should feed directly into monitoring priorities.

**From legislative Tier 1 contacts (senators and House members)**

Congressional staff responses will often flag which specific domains are most immediately actionable given current committee activity. Senator Whitehouse's staff engaging with Domain 6 signals that judicial independence legislation is a viable vehicle; Senator Klobuchar's staff engaging with Domain 1 signals that electoral reform is in active consideration. These signals should update the Tier 2 monitoring priority order — the most actively legislated domains become the highest-priority human-curated monitoring.

**From think tank and law school Tier 1-2 contacts**

Academic and policy institution responses will often identify domains where the proposal's analysis is incomplete or where there is significant recent scholarship the proposal has not incorporated. These responses represent expert peer review and should be treated as domain update candidates. The Ryan Goodman (Just Security) / Erica Chenoweth sequencing from policy-influencer-mapping.md is specifically valuable here: Goodman's engagement would validate the litigation tracker and Domain 6 analysis; Chenoweth's engagement would validate the mobilization theory in the implementation roadmap.

**From labor, civil rights, and state-level Tier 3 contacts**

These organizations have operational knowledge that is not publicly reported. An AFL-CIO contact engaging with Domain 15 (labor rights) will know which NLRB cases are most consequential before they reach public reporting. A state-level Medicaid director contact engaging with Domain 31 will know whether the June 2026 HHS guidance has substantive content three weeks before it is published. This operational intelligence is the highest-value input for domain monitoring and should be treated as confidential coalition intelligence (per Part IV above).

### The Feedback-to-Priority Loop

Coalition engagement → identify most-engaged domains → elevate to Tier 2 human-curated monitoring → execute targeted domain updates → distribute updates specifically to engaged contacts → deepen engagement with evidence that the framework responds to their input → generates further engagement.

This loop is the mechanism by which the proposal becomes a living document rather than a one-time publication. The monitoring infrastructure is not just about keeping the proposal current — it is about creating ongoing relationships with institutional constituencies that are the foundation of any implementation strategy.

---

## Part VII: Source and Tool Inventory

### Automated Monitoring Sources (Free or Low-Cost)

| Source | Coverage | Access Method | Cost |
|--------|----------|---------------|------|
| [CourtListener](https://www.courtlistener.com/) | Federal district + appellate + SCOTUS dockets | Docket alerts via email; REST API | Free |
| [Democracy Docket](https://www.democracydocket.com/cases/) | Voting rights litigation, all 50 states | RSS feed; manual weekly check | Free |
| [Just Security Litigation Tracker](https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/) | Administration challenges, all categories | Manual weekly check | Free |
| [Congress.gov API](https://api.congress.gov/) | Federal bill status and text, all committees | REST API, free with key | Free |
| [LegiScan API](https://legiscan.com/legiscan) | 50-state legislative bill tracking | REST API; $0 for basic monitoring | Free tier |
| [FEC.gov Data](https://www.fec.gov/data/) | Campaign finance, PAC filings, dark money routing | REST API; bulk download | Free |
| [OpenSecrets](https://www.opensecrets.org/) | Dark money tracking, 527 organizations | Manual; limited API | Free |
| [SCOTUSblog](https://www.scotusblog.com/) | SCOTUS cert petitions, orders, argument calendar | Manual weekly; RSS | Free |
| [Federal Register](https://www.federalregister.gov/) | Agency rulemaking, proposed and final rules | API; email alerts by agency | Free |
| [PACER](https://pacer.uscourts.gov/) | Federal court dockets, district + circuit | Per-page fee after $30 quarterly waiver | ~Free for limited use |
| [USASpending.gov](https://usaspending.gov/) | Federal obligations and expenditures vs. appropriations | REST API | Free |
| [Brennan Center Issue Tracker](https://www.brennancenter.org/) | Voting legislation, judicial independence, money in politics | Manual; email newsletter | Free |

### Human-Curated Sources (Require Substantive Reading)

| Source | Coverage | Access | Recommended Cadence |
|--------|----------|--------|---------------------|
| [Harvard EELP Regulatory Tracker](https://eelp.law.harvard.edu/regulatory-tracker/) | Environmental rollbacks, agency-by-agency | Manual | Monthly |
| [AAUP Academic Freedom Reports](https://www.aaup.org/reports-publications) | Higher education, academic freedom, Domain 27 | Manual | Quarterly |
| [KFF Medicaid Tracker](https://www.kff.org/medicaid/) | Medicaid enrollment, waiver status, Domain 31 | Manual | Monthly (quarterly HHS deadlines) |
| [Public Rights Project](https://www.publicrightsproject.org/) | State AG litigation coordination, civil rights | Manual | Monthly |
| [Georgetown Center for Children and Families](https://ccf.georgetown.edu/) | Medicaid state-by-state impact data | Manual | Monthly |
| [Earthjustice Docket](https://earthjustice.org/cases) | Environmental litigation status | Manual | Monthly |
| [Democracy Forward Research](https://democracyforward.org/work/research/) | Regulatory and constitutional litigation | Manual | Monthly |
| [National Immigration Litigation Alliance](https://immigrationlitigation.org/) | Immigration enforcement litigation | Manual | Weekly (high-urgency) |

---

## Confidence Assessment

**High confidence (well-established, documented mechanisms)**

- Tier 1 monitoring sources: all are operational, free, and actively maintained as of April 2026
- Monthly refresh protocol: demonstrated as achievable in Sessions 529-530
- Trigger table for Wave 1: based on documented outcomes and specific pending decisions with known deadlines

**Medium confidence (contingent on circumstances)**

- Coalition feedback architecture: depends on successful Tier 1 distribution engagement, which has not yet begun
- Wave 2 and Wave 3 trigger tables: longer-horizon assumptions are necessarily more speculative; these should be reviewed and revised at the January 2027 structural refresh

**Evidence gaps**

- The Tier 3 coalition-fed monitoring sources depend on relationships that do not yet exist — this gap closes as distribution proceeds but cannot be backfilled retroactively
- LegiScan's 50-state monitoring has known coverage gaps in some states with non-standard legislative calendars (Texas odd-year sessions, for example)
- FEC dark money tracking has a structural limitation: 501(c)(4) spending is not disclosed at the FEC, only routed contributions to super PACs. OpenSecrets' dark money tracking is the best available but has a 6-8 week reporting lag

---

## Next Actions

**Immediate (before distribution begins)**

- Create the three templates in `monitoring/templates/` (monthly-crisis-snapshot.md, contingency-trigger-log.md, coalition-feedback-tracker.md)
- Set CourtListener docket alerts for Trump v. Slaughter, Watson v. RNC, Louisiana v. Callais
- Set Federal Register email alerts for CMS and HHS agencies (June 2026 Medicaid guidance)
- Set Democracy Docket RSS for voting rights cases in Arizona, Georgia, Michigan, Pennsylvania, Wisconsin (swing-state priority)

**Within 30 days of distribution launch**

- Complete first Monthly Crisis Snapshot (identify the 5-7 most urgent domains given distribution launch timing)
- Send update brief on any domain that crosses a flag trigger before the first crisis snapshot
- Begin tracking Tier 1 contact responses in the coalition feedback tracker

**60-90 days post-launch**

- Evaluate which Tier 3 coalition sources have become active; promote active sources to Tier 2 curated monitoring
- Complete the first quarterly automated monitoring review
- Assess whether the trigger table assumptions for Wave 1 are holding; update the roadmap accordingly

---

*Production-ready monitoring infrastructure document. Companion templates at `monitoring/templates/`. Part of Phase 3 structural deepening sequence. Next Phase 3 candidate: Implementation Playbooks — Sector-Specific Tactics (Phase 3 Candidate 2).*

---

## Sources

- [Democracy Docket — Case Tracker](https://www.democracydocket.com/cases/)
- [CourtListener](https://www.courtlistener.com/)
- [Just Security Litigation Tracker](https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/)
- [Just Security Anti-Corruption Tracker](https://www.justsecurity.org/117267/anti-corruption-tracker/)
- [SCOTUSblog Interim Docket](https://www.scotusblog.com/cases/interim-docket/2025/)
- [SCOTUS Orders of the Court 2026](https://www.supremecourt.gov/orders/ordersofthecourt/26)
- [Congress.gov API](https://api.congress.gov/)
- [LegiScan API](https://legiscan.com/legiscan)
- [FEC Campaign Finance Data](https://www.fec.gov/data/)
- [OpenSecrets Dark Money Tracking](https://www.opensecrets.org/dark-money/basics)
- [Brennan Center — Dark Money Hit Record High $1.9B in 2024](https://www.brennancenter.org/our-work/research-reports/dark-money-hit-record-high-19-billion-2024-federal-races)
- [Federal Register](https://www.federalregister.gov/)
- [USASpending.gov](https://usaspending.gov/)
- [Harvard EELP Regulatory Tracker](https://eelp.law.harvard.edu/regulatory-tracker/)
- [KFF Medicaid Tracker](https://www.kff.org/medicaid/)
- [Georgetown Center for Children and Families](https://ccf.georgetown.edu/)
- [Democracy Forward SCOTUS Guide 2025-26](https://democracyforward.org/work/research/peoples-guide-scotus-25-26/)
- [FEC Statistical Summary 2025-2026 Election Cycle](https://www.fec.gov/updates/statistical-summary-of-12-month-campaign-activity-of-the-2025-2026-election-cycle/)
