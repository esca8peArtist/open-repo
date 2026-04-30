---
title: "Adoption Tracking Dashboard Specification"
date: April 30, 2026
status: production-ready
phase: Phase 1 measurement tooling
companion: post-distribution-impact-measurement-framework.md
cross_references:
  - measurement-and-iteration-framework.md
  - post-distribution-tracking.md
  - tracking-template.json
  - DISTRIBUTION_OUTREACH_CONTACTS.md
---

# Adoption Tracking Dashboard — Tool Specifications and Templates

**April 30, 2026**

This document specifies the tooling architecture and operational templates for measuring institutional adoption of the 35-domain Democratic Renewal Framework across all three distribution paths. It translates the measurement framework into concrete instruments: what to build, what to track, where to log, and what the outputs look like at 30, 90, and 180 days.

The dashboard is designed to be operated with free or low-cost tools by a solo researcher with 2-3 hours of monitoring time per week.

---

## Dashboard Architecture Overview

The adoption tracking system has five components, each addressing a distinct measurement problem:

| Component | What it measures | Primary tool | Update cadence |
|-----------|-----------------|--------------|---------------|
| 1. Citation Monitor | When the framework appears in published work | Google Alerts + CourtListener + Overton | Daily/weekly |
| 2. Adoption Scorecard | Who is using it and at what depth | Manual contact log | Per event |
| 3. Domain Heat Map | Which domains are generating engagement | Aggregated from citation log | Weekly |
| 4. Failure Mode Detector | Signs of misapplication or stalled diffusion | Structured review of citation log | Monthly |
| 5. Network Cascade Tracker | Second- and third-order amplification | Bridge node log | Per event |

These five components can run entirely in a spreadsheet or Obsidian database without any additional software. Optional enhancements for network visualization and citation aggregation are noted where applicable.

---

## Component 1: Citation Monitor — Setup and Alert Templates

### Google Alerts (setup time: 15 minutes)

Create the following alerts at news.google.com/alerts with daily delivery to a dedicated email folder:

**Alert set A — Framework title and primary coinages**
- `"democratic renewal proposal"`
- `"35-domain democratic"`
- `"democratic renewal framework" democracy`
- `"domain 37" election interference 2026`

**Alert set B — Key analytical coinages in the corpus**
- `"ICE-at-polls" election`
- `"NVRA quiet period" 2026`
- `"prosecutorial weaponization" SPLC`
- `"state legislative autocratization"`
- `"appellate capture" judicial independence 2026`

**Alert set C — Named bridge node contacts (for detecting second-order citation)**
- `Chenoweth "nonviolent action" democracy 2026` (triggers if Chenoweth cites in new publication)
- `"Just Security" "judicial independence" 2026`
- `"Brennan Center" "voting rights" "democratic renewal"`

Set all alerts to "All results" (not "Best results") and configure to email folder `monitoring/google-alerts/`.

### Google Scholar Alerts (setup time: 10 minutes)

At scholar.google.com/scholar_alerts, create alerts for:
- `"democratic renewal proposal"`
- `"35-domain" democracy institutional`
- `"domain 6 judicial independence" democratic`

Scholar alerts deliver when new academic papers matching the query are indexed. These will be sparse for the first 3-4 months; the absence of Scholar alerts before Month 3 is not a signal of failure.

### CourtListener RECAP Search Alerts (setup time: 20 minutes)

At courtlistener.com, create saved searches for the following and enable email alerts:

**Search 1 — Framework title**
Query: `"democratic renewal proposal"` 
Scope: All federal courts

**Search 2 — Key domain phrases in litigation context**
Query: `"ICE at polls" OR "NVRA quiet period" OR "35-domain" election 2026`
Scope: All federal courts

**Search 3 — Named case dockets from litigation tracker**
For each case in `litigation-tracker-2026.md` at Tier A priority, bookmark the CourtListener docket page and check monthly for new filings. Key dockets to monitor: Wilcox/Slaughter (independent agency removal), any AG-filed election security cases, SAVE Act litigation.

CourtListener's RECAP alerts are the equivalent of Google Alerts for federal court filings. New alerts mean a filing matching the search terms has been docketed — download the document and review for framework language.

### Overton.io (setup time: 30 minutes, requires account)

Register at overton.io. If affiliated with a university library with Overton access, use institutional login (SAGE partnered with Overton to provide free researcher access at partner institutions). If no institutional access, use the free public search tier.

Create an impact tracking alert for the framework. Overton searches its 21 million+ policy document database (government reports, think tank publications, IGO documents) for citations. Due to the 6-18 month indexing lag, do not check Overton before Month 4. Set a calendar reminder for Month 4, Month 8, and Month 12 to run Overton searches.

**Monthly Overton search template** (run at Month 4+):
- Search: `"democratic renewal" proposal institutional`
- Filter by: document type (government, think tank, IGO separately)
- Export results to `monitoring/overton-results-[date].csv`

### LegiScan API (setup time: 30 minutes for account + search setup)

Register at legiscan.com/legiscan-register (free tier: 30,000 queries/month).

Create full-text saved searches for the following terms in priority states (CA, NY, MN, WI, PA, MI, CO, AZ, OH):

**Search set A — Domain 1 / Domain 37 election language**
- `"voter roll" purge SAVE 2026`
- `"ICE" polling place election interference`
- `"NVRA" voter removal quiet period`

**Search set B — Domain 33 state autocratization language**
- `preemption "local government" ballot initiative restriction`
- `"election administration" override legislature`

**Search set C — Domain 27 academic freedom language**
- `"viewpoint diversity" university funding`
- `academic freedom "federal funding" compliance`

Set email alerts for daily notification when new or amended bills match searches. Log any alerts to Component 2 (Adoption Scorecard) under "Legislative sector."

---

## Component 2: Adoption Scorecard — Template

The Adoption Scorecard is the central tracking document. Maintain as a spreadsheet or Obsidian table. One row per organization in the outreach universe.

### Scorecard Schema

| Column | Description | Values |
|--------|-------------|--------|
| Organization | Full name | Text |
| Tier | Influencer tier | 1 / 2 / 3 |
| Primary domain(s) | Which domains are most relevant | Domain numbers |
| Outreach date | Date of first contact | YYYY-MM-DD |
| First response | Date of first substantive reply | YYYY-MM-DD or "None" |
| Response type | Nature of first response | Reply / Material request / Methodology question / No response |
| Adoption level | Current depth of engagement | 0 / 1 / 2 / 3 / 4 (see below) |
| Adoption evidence | What documents the adoption | URL or file reference |
| Last update | Date of last status change | YYYY-MM-DD |
| Next action | What to do next | Text |
| Notes | Free text | Text |

**Adoption level scale**:
- 0: No engagement
- 1: Reference — cited the framework in published work
- 2: Framework — using the analytical structure in their own work
- 3: Operational — domain analysis in active casework, testimony, or legislation
- 4: Coalition — actively introducing the framework to other organizations

### Pre-populated Scorecard Rows (Tier 1 Core)

Copy this table as the starting point; expand with full DISTRIBUTION_OUTREACH_CONTACTS.md list:

| Organization | Tier | Primary domain(s) | Outreach date | Adoption level |
|-------------|------|------------------|--------------|---------------|
| Brennan Center | 1 | 1, 6, 29 | — | 0 |
| Just Security | 1 | 28, 29 | — | 0 |
| Democracy Docket | 1 | 1, 37 | — | 0 |
| EPI | 1 | 17 | — | 0 |
| Protect Democracy | 1 | All / 37 | — | 0 |
| Campaign Legal Center | 1 | 1, 37 | — | 0 |
| ACLU Voting Rights | 1 | 1, 37 | — | 0 |
| Whitehouse office | 1 | 6, 29 | — | 0 |
| Klobuchar office | 1 | 1, 27 | — | 0 |
| Chenoweth / Nonviolent Action Lab | 2 | Resistance meta | — | 0 |
| Heather Cox Richardson | 2 | All | — | 0 |
| NAACP LDF | 3 | 1, 14, 22 | — | 0 |
| Indivisible | 3 | Resistance meta | — | 0 |
| AFL-CIO (via EPI) | 3 | 17 | — | 0 |
| Democracy Docket Phase 2 (Domain 37 targeted) | 1 | 37 | — | 0 |

### Aggregate Adoption Scorecard Targets

Update this summary table monthly:

| Metric | Day 30 target | Day 90 target | Day 180 target | Current count |
|--------|--------------|--------------|---------------|--------------|
| Total outreach sent | 125 | 125+ | 125+ | — |
| Substantive responses received | 4-8 | 15-25 | — | — |
| Level 1 adoption events | 1-2 | 5-10 | 15+ | — |
| Level 2 adoption events | 0-1 | 3-5 | 8-12 | — |
| Level 3 adoption events | 0 | 1-2 | 4-6 | — |
| Level 4 adoption events | 0 | 0-1 | 1-2 | — |
| Legal citations (court filings) | 0 | 0-1 | 1-3 | — |
| Policy proposals citing framework | 0 | 0-1 | 1-3 | — |
| Bridge node cascades confirmed | 0 | 1-2 | 2-4 | — |

---

## Component 3: Domain Heat Map — Template

The Domain Heat Map is a weekly-updated table showing which domains are generating engagement signals. Update every week; the shape of the heat map at Day 60 is the most important diagnostic for understanding diffusion patterns.

### Heat Map Schema

One row per domain. Columns represent weeks since launch (W1 through W26 for 6-month tracking).

| Domain | Title | Tier | W1 | W2 | W3 | W4 | W8 | W12 | W16 | W20 | W26 |
|--------|-------|------|----|----|----|----|-----|-----|-----|-----|-----|
| D1 | Voting Rights | A | — | — | — | — | — | — | — | — | — |
| D2 | Redistricting | C | — | — | — | — | — | — | — | — | — |
| D3 | Campaign Finance | C | — | — | — | — | — | — | — | — | — |
| D5 | Fiscal Reform | C | — | — | — | — | — | — | — | — | — |
| D6 | Judicial Independence | A | — | — | — | — | — | — | — | — | — |
| D9 | Federalism | C | — | — | — | — | — | — | — | — | — |
| D11/31 | Healthcare | C | — | — | — | — | — | — | — | — | — |
| D14 | Criminal Justice | C | — | — | — | — | — | — | — | — | — |
| D15 | Environment | C | — | — | — | — | — | — | — | — | — |
| D16 | Immigration | A | — | — | — | — | — | — | — | — | — |
| D17 | Labor | B | — | — | — | — | — | — | — | — | — |
| D19f | War Powers Reform | B | — | — | — | — | — | — | — | — | — |
| D21/25 | Surveillance / FISA | B | — | — | — | — | — | — | — | — | — |
| D23 | Trade Policy | B | — | — | — | — | — | — | — | — | — |
| D27 | Higher Education | B | — | — | — | — | — | — | — | — | — |
| D28 | War Powers / Venezuela | A | — | — | — | — | — | — | — | — | — |
| D29 | Prosecutorial Weaponization | A | — | — | — | — | — | — | — | — | — |
| D33 | State Autocratization | B | — | — | — | — | — | — | — | — | — |
| D34 | Congressional Purse | C | — | — | — | — | — | — | — | — | — |
| D35 | SCOTUS OT2026 | C | — | — | — | — | — | — | — | — | — |
| D36 | AI Governance | B | — | — | — | — | — | — | — | — | — |
| D37 | Election Interference | A | — | — | — | — | — | — | — | — | — |

**Cell codes**:
- (blank): No signal detected
- `R`: Reply or inquiry received about this domain
- `C1`: Level 1 citation confirmed
- `C2`: Level 2 (framework) adoption confirmed
- `C3`: Level 3 (operational) adoption confirmed
- `L`: Legal citation in court filing
- `P`: Policy proposal/bill citing domain

**Tier column**: Tier A = fastest expected adoption; Tier B = moderate; Tier C = slower. Used to distinguish expected silence from unexpected silence.

### Heat Map Interpretation Rules

At Day 60, apply these interpretation rules:

- **3+ domains generating signals, Tier A domains all generating signals**: Normal pattern — concentrate adoption facilitation on hot domains; cold domains at this stage are not failures.
- **Only Tier A domains generating signals, no Tier B or C**: Expected at Day 60; do not act. Tier B/C domains adopt on a 90-180 day timeline.
- **Tier A domain silent at Day 60 despite outreach to primary contact**: Investigate delivery. The most likely cause is delivery or filtering failure, not content failure.
- **Domain 37 generating citation signals from general-audience channels but not from election-protection institutional contacts (Path A+37)**: Phase 2 Domain 37 targeted distribution is working; track election-protection institutional signals separately in a Domain 37 sub-tracker.

---

## Component 4: Failure Mode Detector — Monthly Review Checklist

Run this checklist in the first week of each month, starting at Month 2.

### Monthly Failure Mode Review

**Date of review**: ________

**1. Partisan capture check**

Total social media engagement events (Reddit upvotes, Substack shares, Twitter/Bluesky forwards) in the past month: ____

Total institutional engagement events (Tier 1-2 replies, material requests, methodology questions, citations) in the past month: ____

Ratio (social : institutional): ____

Threshold: If ratio exceeds 50:1, flag for "partisan capture early warning" and activate Protocol A (see below).

**2. Domain concentration check**

Total citation events identified in past month: ____

Number of distinct domains cited: ____

Top 4 domains by citation count: _____, _____, _____, _____

Top 4 domains as % of all citations: _____%

Threshold: If top 4 domains account for more than 70% of all citations, flag for "domain concentration" and prepare domain-specific briefs for under-cited structural domains.

**3. Citation quality check**

Total citations identified in past month: ____

Classified as substantive (cites specific evidence, analytical claim, or cross-domain connection): ____

Classified as label-only (names framework without specific content): ____

Classified as mischaracterization (attributes claim framework does not make): ____

Threshold: If label-only citations exceed 50% of total, flag for "framework flattening." If any mischaracterizations identified, flag for direct contact with citing organization.

**4. Adoption depth check**

Total confirmed adoption events (all levels): ____

At Level 1 (citation): ____

At Level 2 (framework): ____

At Level 3 (operational): ____

Threshold: If more than 80% of adoption events remain at Level 1 at Month 4, flag for "adoption depth stall" and prepare domain-specific implementation playbooks for highest-adoption organizations.

**5. Bridge node status check** (see Component 5 for full bridge node log)

Bridge nodes with confirmed second-order activation: ____

Bridge nodes contacted but no second-order signal at 90 days: ____

Threshold: If more than 3 bridge nodes have been contacted for 90+ days with no second-order signal, investigate whether outreach was received and review bridge node activation approach.

**6. Domain 37 mischaracterization check**

Any Domain 37 citations in past month: ____

Citations using future-tense language for documented present-tense facts: ____

Threshold: Any mischaracterization of Domain 37 content triggers immediate direct contact with the citing organization. Do not wait for the monthly review.

---

### Recovery Protocols (activate when failure mode thresholds are crossed)

**Protocol A — Partisan Capture**
Timeline: Execute within 2 weeks of detection.
Actions: (1) Identify 3-5 Tier 1 think tank contacts not yet engaged; activate warm referral approach through existing relationships to reach them. (2) Contact the most credible existing Tier 1 adopter; ask if they would co-publish or co-endorse a brief that establishes the institutional context for the framework. (3) Temporarily reduce social media amplification until institutional credibility anchor is established.

**Protocol B — Domain Concentration**
Timeline: Execute within 4 weeks of detection.
Actions: (1) Prepare domain-specific briefs for the 3 structural domains with the lowest citation counts (typically Domains 5, 9, 34). (2) Route briefs to think tank contacts whose institutional focus matches those domains (EPI for D17, Brookings for D9 and D34, CAP for D5 and D11). (3) In follow-up outreach, lead with the hot domain that has already established credibility, then bridge to the structural domain: "The Domain 6 analysis has been getting attention at the Brennan Center; the Domain 34 analysis uses the same evidentiary standard and addresses why the litigation wins need the fiscal architecture to consolidate them."

**Protocol C — Framework Flattening**
Timeline: Execute within 6 weeks of detection.
Actions: (1) Create a "What the Framework Actually Argues" one-pager that foregrounds the cross-domain synthesis and the wave-sequencing logic — not additional evidence, but the analytical architecture that distinguishes this framework from a domain list. (2) Send to organizations currently at Level 1 adoption with an invitation to engage with the analytical architecture, not just the domain evidence. (3) Consider a Substack post that explicitly addresses the framework's cross-domain logic.

**Protocol D — Adoption Depth Stall**
Timeline: Execute at Month 4 if Level 2+ adoption events are below target.
Actions: (1) For each Level 1 adopter who has cited the framework, prepare a tailored domain brief for their next publication or campaign. Frame it as supporting their ongoing work, not asking them to do more. (2) Identify whether any Level 1 adopter is working on a project where Level 3 adoption (operational integration) is structurally possible — this requires knowing their current workplan, which requires active relationship maintenance. (3) Consider a training webinar or briefing for the 3-5 organizations with highest Level 1 engagement, positioned as "deeper engagement for organizations already using the framework."

---

## Component 5: Network Cascade Tracker — Bridge Node Log

One entry per priority bridge node. Copy the template for each node.

### Bridge Node Entry Template

```
BRIDGE NODE: [Name / Organization]
Influencer tier: [1 / 2 / 3]
Network reach: [Estimate — how many people does their output reach?]
Most relevant domains: [Domain numbers]

CONTACT STATUS
First contact date: [YYYY-MM-DD or "Not yet contacted"]
Contact method: [Email / Warm referral / Conference / Other]
First response: [Date and nature, or "None yet"]

FIRST-ORDER SIGNAL
Has the node engaged substantively with the framework? [Yes / No / In progress]
Evidence: [Description of engagement or "None"]

SECOND-ORDER SIGNAL
Has the node used the framework in their own published or public work? [Yes / No / Not yet]
If yes:
  Date: 
  Form: [Publication / Speech / Training material / Brief / Social media / Other]
  Venue/URL:
  Estimated reach of second-order use:
  
THIRD-ORDER SIGNALS
[Log downstream citations to the node's second-order work — date, who, where]
  
CASCADE DEPTH: [Count of citation generations: 1 = only bridge node cited, 2 = one downstream, etc.]

CASCADE FAILURE NOTE
If no second-order signal by Day 90: [Yes / No / Pending]
  Probable cause (if known):
  Alternative activation path:
```

### Pre-populated Bridge Node Log — Priority Seven

**Node 1: Erica Chenoweth / Harvard Nonviolent Action Lab**
- Network reach: 50,000+ organizer network direct; hundreds of thousands via academic citation trail and media appearances
- Most relevant domains: Resistance meta-analysis (3.5% threshold), Domains 7, 33
- Why priority: A Chenoweth citation triggers simultaneous cascade to political science faculty (via journal citation), organizer networks (via Indivisible and M4BL), and graduate students (via syllabi). This is the highest single-node cascade potential in the bridge node map.
- Contact approach: Do not cold-contact until one published academic or high-quality journalistic citation exists. Approach with that citation as credibility anchor.

**Node 2: Brennan Center (Waldman / Weiser) — Congressional Staff Pipeline**
- Network reach: All Hill staff who read Brennan Center reports; direct relationships with Senate Judiciary committee staff
- Most relevant domains: 1, 6, 29
- Why priority: A Brennan Center brief citing the framework reaches 435 congressional offices that receive Brennan Center material. The cascade from Brennan Center to Hill staff to committee hearing materials is the most institutionally consequential path in the map.
- Contact approach: Brennan Center is already in Tier 1 outreach. Primary signal to monitor: brennancenter.org/our-work/research-reports (weekly).

**Node 3: Ryan Goodman / Just Security**
- Network reach: National security attorneys, Senate Intelligence and Judiciary staff, federal judicial clerks, international law scholars
- Most relevant domains: 28, 29 (editorial focus of Just Security)
- Why priority: Just Security publishes within 48-96 hours. A Just Security piece citing the framework is the fastest institutional credibility signal available — it precedes any other publication by weeks.
- Contact approach: Domain 28 or Domain 29 pitch. Frame the domain analysis as filling a specific analytical gap in existing Just Security coverage of those topics.

**Node 4: Heather Cox Richardson / Letters from an American**
- Network reach: 2.9 million newsletter subscribers (direct); substantial social media amplification
- Most relevant domains: All (historical framing)
- Why priority: Single-trigger mass reach. Richardson's subscriber base is the largest organic policy communications channel in the progressive ecosystem.
- Contact approach: Do not approach until academic citations exist. Organic discovery preferred — Richardson cites research she encounters through her own reading, not through cold outreach. Monitor heathercoxrichardson.substack.com.

**Node 5: EPI / AFL-CIO Labor Bridge**
- Network reach: AFL-CIO to 56 affiliated unions (12.5 million workers via union communications infrastructure)
- Most relevant domain: 17
- Why priority: An EPI issue brief citing Domain 17 triggers AFL-CIO newsletter distribution, which triggers union legislative testimony citing the EPI brief. This is the most predictable cascade chain in the map because the EPI-AFL-CIO distribution relationship is institutional and reliable.
- Contact approach: Domain 17 brief specifically targeting EPI's labor research agenda. Monitor epi.org/research for new Domain 17-relevant publications.

**Node 6: ACS Scholars Network — Law School to Hill Staff Pipeline**
- Network reach: Law school clinic directors, law review editors, and Hill staff simultaneously via ACS programming
- Most relevant domains: 6, 29, 28
- Why priority: ACS programming spans legal academia and Hill staff in a single venue — activation through ACS reaches both populations simultaneously.
- Contact approach: Via an ACS constitutional law symposium or CLE where the framework's comparative constitutional law methodology is the hook.

**Node 7: Levitsky / Ziblatt**
- Network reach: Political science community (via academic citation), general educated public (via New York Times op-eds and book tour), foreign policy community (via Foreign Affairs)
- Most relevant domains: Resistance meta-analysis, comparative democratic backsliding framework (Domains 6, 33, international case studies)
- Why priority: A Levitsky or Ziblatt mention in any public commentary cascades to every political scientist who reads them.
- Contact approach: Do not approach until Tier 2 academic credibility is established — a Balkin blog mention or Just Security citation creates the basis for this approach. They will assess the framework against the "How Democracies Die" and "Tyranny of the Minority" analytical standards; ensure the comparative methodology in the framework meets that standard before approaching.

---

## Component 6: Sector-Specific Monitoring Calendars

These calendar templates organize the monitoring work by sector, preventing the dual failure modes of over-monitoring (checking for signals daily when the sector's adoption timeline is 90+ days) and under-monitoring (missing an early signal in a fast-moving sector).

### State AGs — Monitoring Calendar

| Check | Cadence | Method | What to look for |
|-------|---------|--------|-----------------|
| AG press rooms (priority 5 states) | Weekly | RSS or manual | Domain-aligned language in press releases without attribution |
| AG coalition statements (NAAG, DAGA) | Weekly | NAAG.org + DAGA press pages | Coalition letters using domain framework |
| CourtListener RECAP search | Biweekly | Saved search | New AG-filed complaints with domain-aligned language |
| Direct contact check-in | Day 45, Day 90 | Email | Substantive follow-up with AG policy counsel contacts |

### Think Tanks — Monitoring Calendar

| Institution | Check cadence | Method | Priority domains |
|------------|--------------|--------|-----------------|
| Brennan Center | Weekly | brennancenter.org/our-work/research-reports RSS | 1, 6, 29 |
| Just Security | Daily | justsecurity.org RSS | 28, 29 |
| Lawfare | Daily | lawfaremedia.org RSS | 28, 29 |
| Balkinization | Daily | balkin.blogspot.com RSS | 6, 28, 29 |
| EPI | Weekly | epi.org/research RSS | 17 |
| CAP | Monthly | americanprogress.org | 11, 5, 23 |
| Protect Democracy | Weekly | protectdemocracy.org/work | 37, 6, 1 |
| Brookings | Monthly | brookings.edu/topic/democracy | 9, 28, 34 |

### Law Schools — Monitoring Calendar

| Check | Cadence | Method | What to look for |
|-------|---------|--------|-----------------|
| SSRN alerts | Weekly | SSRN email alerts (set for domain title phrases) | Working papers citing framework |
| Google Scholar alerts | Weekly | Alert email review | Academic citations |
| Direct check-in with faculty contacts | Day 60, Day 120 | Email | Research gap interest, clinic case connection |
| Top law review online companions | Monthly | HLR Forum, Yale LJ online, Colum LJ Sidebar | Rapid-response articles on SCOTUS/Domain 35 rulings |

### Civil Rights Coalitions — Monitoring Calendar

| Organization | Check cadence | Method | What to look for |
|-------------|--------------|--------|-----------------|
| Indivisible resource library | Monthly | indivisible.org/resources | Framework citations in training materials |
| NAACP LDF publications | Monthly | naacpldf.org/news-resources | Reports citing domain analysis |
| Lawyers' Committee | Monthly | lawyerscommittee.org | Publications using domain framework |
| States United | Monthly | statesuniteddemocracy.org | Domain 37 or Domain 1 citations |
| Democracy Docket newsletter | Weekly | Email subscription | Domain 37 or Domain 1 analytical framing alignment |

---

## Synthesis: Monthly Reporting Template

At the start of each month, complete this 1-page reporting template. It is the output that informs iteration decisions.

**Month**: ________ **Distribution day count**: Day ___

**Citation summary**
- New Level 1+ adoption events confirmed this month: ____
- New legal citations (court filings): ____
- New policy proposals / legislation: ____
- New academic citations: ____
- Most-cited domains this month: ___________________________

**Domain heat map assessment**
- Hot domains (generating regular signals): ___________________
- Warm domains (at least one signal): _______________________
- Cold domains (no signal yet): ______________________________
- Unexpected silence from Tier A domain: [ ] Yes [ ] No
  If yes, domain: ___ Probable cause: _______________________

**Failure mode check**
- Partisan capture flag: [ ] Yes [ ] No
- Domain concentration flag (>70% in top 4): [ ] Yes [ ] No
- Framework flattening flag (>50% label-only): [ ] Yes [ ] No
- Domain 37 mischaracterization detected: [ ] Yes [ ] No

**Bridge node status**
- Nodes with second-order activation this month: ________________
- New cascade events logged: _______
- Nodes at 90+ days with no activation: _______

**Iteration decisions this month**
- Domains flagged for revision (two Tier 1 objections threshold): ______
- Phase 2 demand signals received (explicit Tier 1 requests): ________
- Recommended research priority for next session: ________________

**Key quote or qualitative finding this month**
(Capture the single most important thing learned about how the framework is being used — this is the data that doesn't fit in any cell above.)

---

*Dashboard Spec version 1.0 — April 30, 2026. Activates on distribution launch. The five components can be built in a single 3-hour session using free tools (Google Alerts, Google Scholar Alerts, CourtListener, LegiScan, a spreadsheet). Cross-reference: post-distribution-impact-measurement-framework.md (the analytical framework this dashboard operationalizes), measurement-and-iteration-framework.md (the iteration logic), post-distribution-tracking.md (the first 30-day roadmap).*

---

Sources:
- [CourtListener RECAP Search Alerts for PACER](https://free.law/2025/06/18/recap-search-alerts-for-pacer-are-now-live/)
- [CourtListener.com](https://www.courtlistener.com/)
- [Overton Impact Tracking](https://www.overton.io/policy-impact)
- [Overton Index](https://www.overton.io/overton-index)
- [LegiScan API](https://legiscan.com/legiscan)
- [LegiScan Full Text Search](https://legiscan.com/fulltext-search)
- [Google Scholar Alerts](https://scholar.google.com/scholar_alerts?view_op=list_alerts)
