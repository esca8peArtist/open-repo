---
title: "Domain 37: Pre-Distribution Baseline Metrics"
created: "2026-04-30"
session: "703"
domain: "Domain 37 — Federal Executive Interference in 2026 Midterms"
measurement_window: "May 2026 – November 4, 2026"
distribution_path: "Path-agnostic — applies to A, A+37, and B"
status: "production-ready"
companion: "projects/resistance-research/domains/domain-37-federal-executive-interference-2026-midterms.md"
---

# Domain 37: Pre-Distribution Baseline Metrics

**Established**: April 30, 2026 (Session 703)
**Measurement window**: May 2026 – November 4, 2026 (Election Day)
**Purpose**: Quantified pre-distribution baselines enabling post-distribution impact attribution across all three distribution paths (A, A+37, B)

---

## Why This Document Exists

Distribution impact cannot be measured without a fixed pre-distribution snapshot. Domain 37's five interference mechanisms are active and evolving; the legal and political landscape will change materially between now and November 4, 2026. This document locks four quantified baselines as of April 30, 2026, establishes the measurement protocol for each, and provides the success criteria and failure modes that distinguish framework influence from ambient change.

The four metrics were selected because they are: (a) directly tied to the five interference mechanisms documented in Domain 37; (b) measurable via public data sources at weekly frequency; (c) attributable — each metric has a plausible causal pathway through which framework distribution could influence outcomes; and (d) actionable — they map to specific advocacy windows in Domain 37's activation timeline.

---

## Metric 1: DOJ Voter Roll Litigation — Active Case Count and Judicial Posture

### Baseline (April 30, 2026)

The DOJ has filed lawsuits against approximately 30 states and the District of Columbia demanding unredacted voter registration files. As of this writing, the DOJ stands 0-for-6 at the district court level:

- **Dismissed with prejudice**: California, Oregon, Massachusetts, Rhode Island, Michigan (Sixth Circuit affirmed), Arizona (April 28, 2026 — Trump-appointed Judge Susan Brnovich ruled voter rolls are "not a document subject to request by the Attorney General")
- **Active / briefing complete, decision pending**: Approximately 9 states including Washington (allowed to proceed April 7, 2026)
- **Active / briefing ongoing**: Approximately 8 additional states
- **DOJ theory in surviving cases**: Civil Rights Act of 1960, Section 303 — split among courts on whether voter rolls qualify as "voting records"
- **Appellate posture**: DOJ has appealed all dismissals; expedited review sought in Sixth Circuit (Michigan)
- **Parallel challenge**: Common Cause v. DOJ (D.D.C., filed April 21, 2026) — seeks to block the national voter database construction entirely

**Baseline count: 23 active cases** (approximately 17 district court cases active/pending decision + the 6 dismissed cases in the appellate pipeline)

### Measurement Protocol

| Parameter | Detail |
|-----------|--------|
| Collection frequency | Weekly (every Monday) |
| Primary source | University of Wisconsin State Democracy Research Initiative tracker: https://statedemocracy.law.wisc.edu/tracker-doj-lawsuits-states-voter-data/ |
| Secondary source | Democracy Docket active cases: https://www.democracydocket.com/cases/ |
| Tertiary source | DOJ press releases: https://www.justice.gov/opa/pr |
| Data points to collect | Case name, court, filing date, current status, most recent ruling, next deadline, appellate status |

**Attribution rules**: Direct attribution is possible when (a) a dismissal ruling cites an analytical argument present in Domain 37's legal framework; (b) an AG's amicus brief or motion incorporates Domain 37's treatment of CASA's post-*Trump v. CASA* injunction architecture; or (c) a court opinion references the SAVE error-rate data (81% false positives from Missouri, documented in Domain 37 Section II.A). Indirect attribution when overall litigation posture hardens after documented framework adoption by an AG's office.

**Confidence scoring**:
- High confidence: AG policy counsel contact confirmed receipt + subsequent filing mirrors Domain 37 legal framework
- Medium confidence: Coalition AG statement mirrors Domain 37 analysis within 4–8 weeks of confirmed distribution
- Low confidence: Favorable ruling in a circuit where distribution occurred, no direct confirmation

### Success Criteria

**Conservative success**: At least 2 of the pending district court cases are dismissed citing legal arguments present in Domain 37 (CASA architecture, SAVE error rate as standing basis, Elections Clause allocation of authority), and at least one dismissal opinion cites or mirrors Domain 37's analysis within 90 days of distribution.

**Ambitious success**: All appellate cases are resolved against DOJ by November 4, 2026; no SAVE-based voter removals occur after the August 7 NVRA quiet period; at least one state AG's emergency filing incorporates the Domain 37 quiet-period enforcement protocol by name.

**Failure mode**: DOJ wins at the appellate level in any circuit before August 7; SAVE-based removals proceed in compliant states without successful injunctive challenge; no attribution linkage between framework distribution and legal arguments deployed.

---

## Metric 2: CISA Election Security Budget — FY27 Appropriations Trajectory

### Baseline (April 30, 2026)

The Trump administration's April 7, 2026 FY27 budget proposal contains:

- **Gross proposed cut**: $707 million from CISA
- **Net funding reduction**: approximately $360 million after transfers
- **Position eliminations**: 867 positions (860+ figures across sources)
- **Election security program**: Complete elimination proposed — information-sharing support, dedicated election security advisors, EI-ISAC, MS-ISAC funding all zeroed out
- **Total CISA operating budget if passed**: approximately $2 billion (down from approximately $2.7 billion)
- **Congressional precedent**: The prior year proposal sought approximately $490 million in CISA reductions; Congress significantly narrowed the cuts
- **Key congressional voice**: Rep. Andrew Garbarino (R-NY) stated Congress has "a responsibility to ensure the agency has the resources it needs to succeed"
- **Appropriations process**: Budget requires congressional approval; subcommittee markup expected June–September 2026

**Baseline: $707 million proposed cut / $0 election security budget proposed**

### Measurement Protocol

| Parameter | Detail |
|-----------|--------|
| Collection frequency | Weekly for congressional calendar events; monthly for budget line status |
| Primary source | Congress.gov appropriations subcommittee activity: https://www.congress.gov/committees/listing/house-committees |
| Secondary source | Nextgov/FCW and CyberScoop for agency coverage: https://www.nextgov.com/ and https://cyberscoop.com/ |
| Tertiary source | House Appropriations Subcommittee on Homeland Security markup releases |
| Data points to collect | Subcommittee markup date, proposed CISA allocation, election security line item, vote count (committee and floor), amendment activity, conference report outcome |

**Key tracking dates**:
- June–July 2026: House Appropriations Subcommittee on Homeland Security markup expected
- September 2026: Full committee and floor votes
- October 2026: Senate action and conference report
- November 2026: Continuing resolution or enacted appropriation

**Attribution rules**: Direct attribution when a member's floor statement or committee markup amendment explicitly references the election security infrastructure argument made in Domain 37; or when the Garbarino-type "Congress has a responsibility" framing is amplified in ways that can be traced to framework adoption by election security advocacy networks. Indirect attribution when the election security line item is restored or reduced less than proposed, concurrent with documented framework circulation among congressional staff or advocacy networks.

**Confidence scoring**:
- High confidence: Staff counsel for Subcommittee confirms use of Domain 37 analysis in markup preparation
- Medium confidence: Amendment language mirrors Domain 37's CISA infrastructure analysis; amendment sponsor cited the framework in a prior public statement
- Low confidence: CISA election security line is restored/maintained; distribution to election security advocacy communities preceded the markup

### Success Criteria

**Conservative success**: The FY27 election security program line item is not completely eliminated — Congress restores at least partial EI-ISAC or MS-ISAC funding, consistent with the prior-year precedent of narrowing cuts. Domain 37's documentation of the information-sharing void becomes part of the public record referenced in markup debates.

**Ambitious success**: A bipartisan amendment restores election security funding to near-FY26 levels; at least one Republican co-sponsor cites the election security void (a Domain 37 core argument) in their floor statement; CISA restores an Election Day situation room for November 4, 2026.

**Failure mode**: The FY27 election security line is completely eliminated as proposed with no floor or committee amendment activity; the Garbarino position does not attract co-sponsors; appropriations are resolved through a continuing resolution that preserves the cut.

---

## Metric 3: Federal Election Denier Appointments — Headcount, Tenure, and Function

### Baseline (April 30, 2026)

Domain 37 documents 11+ confirmed federal appointees connected to the Election Integrity Network (led by Cleta Mitchell) across DHS and DOJ, plus additional key officials:

**Named individuals in position as of April 30, 2026**:

1. **Harmeet Dhillon** — Assistant AG, Civil Rights Division (confirmed April 3, 2025, 52-45; 75% of career staff departed)
2. **Eric Neff** — Acting Chief, DOJ Voting Section (coordinates national voter database operation)
3. **Thomas Albus** — U.S. Attorney (Eastern District of Missouri), designated nationwide election jurisdiction under 28 U.S.C. § 515
4. **David Harvilicz** — DHS, oversees voting machine security (co-founded AI company with Antrim County fraud conspiracy architect)
5. **Heather Honey** — DHS elections position (falsely claimed Pennsylvania ballot irregularities; ties to Election Integrity Network)
6. **Kurt Olsen** — White House election security director (worked to overturn 2020 results; pressured FBI Atlanta on Fulton County seizure)
7. **At least 6 additional Election Integrity Network-connected appointees** across DHS and DOJ (not individually named in public sources as of this baseline)

**Baseline: 11+ appointees; 7 individually named and confirmed; all remain in position**

### Measurement Protocol

| Parameter | Detail |
|-----------|--------|
| Collection frequency | Monthly headcount review; weekly news monitoring for departures, confirmations, or reassignments |
| Primary source | Democracy Docket analysis and Just Security government structure coverage |
| Secondary source | ProPublica reporting on specific officials (Thomas Albus, Heather Honey profiles documented) |
| Tertiary source | Votebeat election official coverage: https://www.votebeat.org/ |
| Spreadsheet tracking fields | Official name, position title, agency, date of appointment, Election Integrity Network connection (yes/no, documented basis), current status (active/departed/reassigned), notable actions taken since last update |

**Attribution rules**: Direct attribution when a confirmed departure or Senate confirmation rejection follows domain-documented opposition research being introduced into public or legislative record. Indirect attribution when public accountability pressure (op-eds, coalition letters, state AG filings naming specific officials) increases after distribution and precedes a departure or reassignment.

**Confidence scoring**:
- High confidence: Senate Judiciary hearing testimony cites Domain 37 appointee documentation; specific official departure follows documented congressional inquiry referencing framework
- Medium confidence: Opposition research organizations (CREW, States United) incorporate Domain 37 official documentation in their public filings after distribution
- Low confidence: Official departure within 90 days of distribution; no direct attribution possible

### Success Criteria

**Conservative success**: At least 2 of the 7 named officials are either (a) subjected to formal Senate oversight inquiry citing their election-related background, or (b) depart from their positions by November 4, 2026; the departure creates a documented gap in the interference coordination architecture.

**Ambitious success**: Thomas Albus's nationwide election jurisdiction is challenged in federal court before October 2026; Harmeet Dhillon faces Senate inquiry or confirmation re-hearing on her fitness to oversee the Voting Section; the Election Integrity Network-to-federal-appointment pipeline is publicly documented as a pattern (not merely individual cases) in mainstream media coverage traceable to framework distribution.

**Failure mode**: All 11+ appointees remain in position through November 4, 2026 with no formal oversight action; the Albus cross-district jurisdiction goes unchallenged; the Fulton County seizure infrastructure is replicated in one or more swing states before election night.

---

## Metric 4: Section 3 Litigation Infrastructure Readiness

### Baseline (April 30, 2026)

The post-*Trump v. Anderson* (March 4, 2024) landscape eliminates state-initiated administrative disqualifications of federal officeholders. What remains:

**Current state AG positioning**:
- 24-state AG coalition has filed against the March 31 mail voting EO (Arizona, California, Colorado, Connecticut, DC, Illinois, Maine, Maryland, Massachusetts, Michigan, Minnesota, Nevada, New Jersey, New Mexico, New York, North Carolina, Oregon, Rhode Island, Vermont, Virginia, Washington, Wisconsin + Delaware AG + Pennsylvania Governor Shapiro)
- Jena Griswold (Colorado Secretary of State, running for CO AG in 2026) was the lead official in the original *Anderson* Section 3 case; her AG candidacy creates a pathway to Section 3 enforcement capability in Colorado
- CREW has the most developed factual record for Section 3 proceedings, including documentation of specific officials' January 6 coordination acts
- Just Security maintains a Section 3 litigation clearinghouse: https://www.justsecurity.org/90972/clearinghouse-14th-amendment-section-3-litigation/

**What Section 3 infrastructure requires before November 2026**:
1. A congressional Section 5 enforcement statute (not yet introduced)
2. A federal court declaratory action establishing factual record for specific officials
3. State-level enforcement mechanisms for state officeholders (available in favorable states)

**Baseline: No active Section 3 proceedings targeting 2026 election administration officials; coalition litigation active on EO challenge but not Section 3 specifically; pre-litigation factual record exists at CREW**

### Measurement Protocol

| Parameter | Detail |
|-----------|--------|
| Collection frequency | Weekly for new filings; monthly for coalition status |
| Primary source | Just Security Section 3 clearinghouse: https://www.justsecurity.org/90972/clearinghouse-14th-amendment-section-3-litigation/ |
| Secondary source | CREW litigation tracker: https://www.citizensforethics.org/legal-action/ |
| Tertiary source | Democracy Docket election protection filing tracker |
| Data points to collect | New Section 3-related filings (name, court, filing date, named defendants, procedural status); state AG coalition statements referencing specific officials; congressional bill introductions for Section 5 enforcement mechanism; pre-election coordination meetings (publicly reported) among state AGs on election night response |

**Key signals to watch**:
- Any federal declaratory action naming Olsen, Albus, or Harvilicz and alleging Section 3 grounds
- Colorado AG race outcome (Griswold candidacy) and its effect on CO Section 3 standing
- Congressional introduction of a Section 5 enforcement bill (even without floor vote, signals coalition formation)
- State AG coalition coordination on election night rapid-response positioning (reported through September–October 2026)

**Attribution rules**: Direct attribution when a Section 3 filing incorporates the *Anderson* framework analysis or the specific official documentation methodology from Domain 37. Indirect attribution when Domain 37's Section 3 reform pathway analysis (Section IV.B) is cited in advocacy materials produced by organizations that received the framework.

**Confidence scoring**:
- High confidence: A filing directly incorporates Domain 37's Section 3 analysis; domain received by CREW or a state AG office is confirmed
- Medium confidence: New Section 3 filing emerges within 60 days of distribution that addresses the specific officials named in Domain 37
- Low confidence: Increased Section 3 litigation activity post-distribution; no direct confirmation of attribution

### Success Criteria

**Conservative success**: At least one state introduces (not necessarily passes) a Section 5 enforcement bill or state-level Section 3 mechanism for state election officials by September 2026; the Fulton County warrant infrastructure (Albus cross-district jurisdiction) is challenged in a federal declaratory action before election night.

**Ambitious success**: A coalition of state AGs publicly coordinates election night rapid-response protocols specifically designed to counter a Fulton County-type seizure; at least one federal court issues a declaratory ruling that deployment of federal law enforcement at ballot-counting facilities before certification constitutes a per se violation of the Elections Clause, creating a pre-certification protective order.

**Failure mode**: No Section 3-related filings target 2026 election administration officials before November 4; the Albus cross-district jurisdiction remains legally unchallenged; state AGs have no pre-positioned emergency authority to counter ballot seizure attempts.

---

## Spreadsheet Schema — Universal Tracking Template

For use across all four metrics. One row per data collection event.

```csv
date,metric_id,metric_name,value,value_unit,source_name,source_url,data_collector,confidence_level,attribution_type,notes
2026-04-30,M1,DOJ_voter_roll_cases_active,23,case_count,UW_SDRI_tracker,https://statedemocracy.law.wisc.edu/tracker-doj-lawsuits-states-voter-data/,agent_703,baseline,none,Baseline snapshot: 6 dismissed at district court level (all in appellate pipeline) + ~17 active
2026-04-30,M2,CISA_election_security_proposed_cut,707,USD_millions,Nextgov_FCW,https://www.nextgov.com/cybersecurity/2026/04/trump-proposes-cutting-cisa-election-security-program-fy27-budget/412672/,agent_703,baseline,none,FY27 request proposes complete elimination of election security program
2026-04-30,M3,election_denier_appointees_in_position,11,headcount,Domain37_Section_II.C,internal,agent_703,baseline,none,7 individually named + 4 unnamed EIN-connected appointees
2026-04-30,M4,section3_infrastructure_active_filings,0,filing_count,Just_Security_clearinghouse,https://www.justsecurity.org/90972/clearinghouse-14th-amendment-section-3-litigation/,agent_703,baseline,none,No active S3 proceedings targeting 2026 election admin officials
```

**Confidence levels**: `baseline` / `high` / `medium` / `low`
**Attribution types**: `none` / `direct_confirmed` / `direct_probable` / `indirect_correlative`

---

## Path-Agnostic Application

These metrics work identically across all three distribution paths:

**Path A (34-domain distribution)**: Domain 37 is not in the initial distribution set. These metrics establish baseline for post-Path-A environmental monitoring — tracking whether election protection activity increases in response to the 34-domain framework even without Domain 37 being distributed. If activity increases substantially without Domain 37, the baseline informs a faster Domain 37 distribution decision.

**Path A+37 Hybrid (Domain 37 distributed early)**: These metrics become the primary impact attribution tool. The measurement window opens the week of May 5, 2026 and extends to November 4. The 60-day mark (approximately July 5) is the first meaningful attribution checkpoint — sufficient time for institutional adoption by AGs and litigation organizations, but before the critical August 7 NVRA quiet period deadline.

**Path B (continued research)**: These metrics become the foundation for Phase 2 research deepening. Weekly collection continues regardless of distribution, building the empirical record that Phase 2 work will analyze. If distribution remains on hold through September 2026, the metrics transform into a pre-election damage assessment rather than an impact attribution tool — which is itself a research output.

---

## Attribution Framework and Decision Tree

**Week 4 post-distribution (attribution checkpoint 1)**
- If M1 shows new dismissals citing CASA architecture or SAVE error-rate standing: flag for medium confidence attribution
- If M4 shows new Section 3 filings or coalition coordination letters: flag for medium confidence attribution
- If no signals: confirm infrastructure is working (organizations received materials); note that AGs have 4-8 week adoption lag per the post-distribution impact framework

**Week 8 post-distribution (attribution checkpoint 2)**
- M2: Has any subcommittee markup date been announced? Is election security appearing in pre-markup advocacy? If yes and distribution preceded advocacy escalation: medium confidence
- M3: Any named officials departed or faced formal oversight inquiry? If yes with traceable pressure campaign: medium-to-high confidence
- Decision: If all four metrics show zero movement by week 8, increase direct outreach intensity to bridge nodes (Brennan Center, Democracy Docket, state AG staff) per `post-distribution-impact-measurement-framework.md`

**Pre-August 7 (quiet period checkpoint)**
- M1 critical: Is injunctive relief in place in all compliant states? If no and framework was distributed without quiet-period enforcement protocol being adopted: flag as attribution gap — accelerate direct outreach to Democracy Docket and state AGs
- This is the highest-urgency attribution window: the NVRA quiet period deadline is non-negotiable and framework non-adoption by this date constitutes a measurable failure mode

**Election Night**
- M4 critical: Were any Fulton County-type seizure attempts made? Was there pre-positioned rapid-response capacity? These outcomes — positive or negative — are the primary November 4 attribution data points

---

## Data Sources — Master Reference

| Source | URL | Metrics | Update Frequency |
|--------|-----|---------|-----------------|
| UW State Democracy Research Initiative | https://statedemocracy.law.wisc.edu/tracker-doj-lawsuits-states-voter-data/ | M1 | Ongoing |
| Brennan Center DOJ tracker | https://www.brennancenter.org/our-work/research-reports/tracker-justice-department-requests-voter-information | M1 | Ongoing |
| Democracy Docket active cases | https://www.democracydocket.com/case-status/filed/ | M1, M4 | Daily |
| CourtListener PACER filings | https://www.courtlistener.com/ | M1, M4 | Daily |
| Congress.gov Appropriations | https://www.congress.gov/committees | M2 | Weekly |
| Nextgov / CyberScoop | https://www.nextgov.com/ / https://cyberscoop.com/ | M2 | Daily |
| Cybersecurity Dive | https://www.cybersecuritydive.com/ | M2 | Weekly |
| Just Security Section 3 clearinghouse | https://www.justsecurity.org/90972/clearinghouse-14th-amendment-section-3-litigation/ | M4 | Ongoing |
| CREW litigation tracker | https://www.citizensforethics.org/legal-action/ | M3, M4 | Weekly |
| Votebeat | https://www.votebeat.org/ | M1, M3 | Daily |
| ProPublica Trump election coverage | https://www.propublica.org/ | M3 | As published |

---

*Domain 37 baseline metrics established: April 30, 2026 (Session 703)*
*Next measurement collection: Week of May 5, 2026 (or at time of distribution, whichever comes first)*
*Companion document: `projects/resistance-research/domains/domain-37-federal-executive-interference-2026-midterms.md`*
