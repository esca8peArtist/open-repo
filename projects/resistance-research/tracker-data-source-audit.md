---
title: "Tracker Data Source Audit — Four-Tracker Automation Infrastructure"
subtitle: "Existing source assessment, new automatable sources, legal feasibility, and priority rankings"
date: 2026-05-05
status: design-phase
project: resistance-research
purpose: Post-Phase-1 automation infrastructure planning
cross_references:
  - first-amendment-suppression.md
  - environmental-rollbacks-tracker.md
  - police-brutality-consent-decree-tracker.md
  - tracker-automation-architecture.md
---

# Tracker Data Source Audit

*Created: May 5, 2026. Purpose: Audit current sources across four trackers and identify 5+ new automatable sources per tracker with legal feasibility assessment and priority rankings. This document supports the automation infrastructure design described in `tracker-automation-architecture.md`.*

---

## How to Read This Document

Each tracker section covers: (1) current sources and their honest freshness/completeness assessment, (2) five or more new automatable sources organized by type, (3) a legal feasibility table for each new source, and (4) a priority ranking scoring each source on five dimensions (scale 1–10). The combined score at the end of each source table is the ordering criterion for implementation sequencing.

---

## Section 1: First Amendment Suppression Tracker

### 1.1 Current Sources (as of May 2026)

The `first-amendment-suppression.md` tracker is maintained through a combination of:

- **Manual news monitoring**: Researcher monitors major national outlets (NYT, WaPo, Guardian, CNN, Reuters, AP) for press freedom, protest, and SLAPP-related stories. Coverage is reactive — stories surface when researcher is actively reading.
- **ACLU case tracker** (aclu.org/cases): Checked manually every 1–2 weeks. Provides reliable litigation data but has a 1–7 day lag between filing and page update.
- **Freedom of the Press Foundation (FPF) alerts**: FPF publishes press releases when major press freedom incidents occur. These are monitored via email subscription but are not systematically ingested.
- **Reporters Committee for Freedom of the Press (RCFP)**: Monitored via website visits. Publishes analysis but rarely publishes raw case data.
- **RSF (Reporters Without Borders) World Press Freedom Index**: Annual publication used for context only, not for tracking individual incidents.
- **Earthjustice, PEN America, CPJ websites**: Checked ad hoc, no systematic cadence.

**Freshness assessment**: Publication lag averages 3–7 days from event to tracker entry, rising to 10–14 days during low-attention periods. The tracker has zero automation; every entry is manually authored.

**Completeness gaps**:
- State-level anti-protest laws and their legislative status are systematically undercovered. A bill passing the Kansas legislature is unlikely to surface through national news monitoring.
- SLAPP suits filed at state courts rarely appear in national coverage; local legal news is the only reliable source.
- Overseas press freedom incidents affecting U.S. journalists are inconsistently captured.
- Congressional subpoenas targeting journalists are not systematically tracked through public PACER filings.

**False positive rate**: Low. Researcher applies high scrutiny before adding entries, but the flip side is systematic undercoverage of lower-profile incidents.

**Estimated new entries per week**: 3–6 during active news periods, 1–2 during quiet periods.

### 1.2 New Automatable Sources

**Type A — Government/Judicial APIs**

**Source A1: PACER / CourtListener RECAP API**
- **What it covers**: All federal court filings, including First Amendment cases in district and appellate courts. Can be queried for dockets mentioning "First Amendment," "press freedom," "prior restraint," "qualified immunity," "journalist," "shield law," etc.
- **API**: CourtListener REST API v4 at `https://www.courtlistener.com/api/rest/v4/`. Free tier; authentication via token. RECAP archive covers nearly every federal case since 2008 and grows by thousands of documents daily.
- **Freshness**: Near-real-time for new filings (RECAP users upload documents within hours of retrieval from PACER). Docket updates typically lag 1–24 hours.
- **Endpoint**: `GET /api/rest/v4/dockets/?q=first+amendment+journalist&type=d` with date filters. Can also query by party name (e.g., "Associated Press," "ACLU").
- **Cost**: Free. CourtListener is a nonprofit project.
- **URL**: https://www.courtlistener.com/help/api/

**Source A2: U.S. Press Freedom Tracker API**
- **What it covers**: All documented incidents of press freedom violations in the U.S. — arrests of journalists, equipment seizures, physical assaults, denial of access, subpoenas. Maintained by Freedom of the Press Foundation and CPJ. Verified before publication.
- **API**: REST API at `https://pressfreedomtracker.us/api/edge/incidents/`. Returns JSON. Filterable by date, category (arrest, equipment seizure, etc.), state, and keyword search. CSV and JSON bulk download also available.
- **Example query**: `https://pressfreedomtracker.us/api/edge/incidents/?date_lower=2026-01-01&categories=4` (arrests)
- **Freshness**: Incidents verified and published within 24–72 hours of occurrence for major events; smaller incidents may lag 1–2 weeks.
- **Cost**: Free. Open source.
- **URL**: https://pressfreedomtracker.us/data/

**Source A3: Federal Register API — Executive Orders and Notices Affecting Press**
- **What it covers**: Executive orders, agency notices, and proposed rules that affect First Amendment rights (press access rules, media regulation, public affairs guidance from executive agencies).
- **API**: Federal Register API v1 at `https://www.federalregister.gov/api/v1/documents.json`. Filter by agency (e.g., DOD, DHS), document type (executive order, rule, notice), and keyword.
- **Example query**: `https://www.federalregister.gov/api/v1/documents.json?conditions[term]=press+access&conditions[agencies][]=defense-department`
- **Freshness**: Federal Register publishes daily; API reflects same-day publication.
- **Cost**: Free. Government API, no rate limits published (reasonable use expected).
- **URL**: https://www.federalregister.gov/developers/documentation/api/v1

**Type B — News APIs**

**Source B1: GDELT Project DOC 2.0 API**
- **What it covers**: Monitors global news in 100+ languages, updated every 15 minutes. Can filter to U.S. news sources with keywords like "First Amendment," "press freedom," "book ban," "journalist arrested," etc.
- **API**: GDELT DOC 2.0 API. Free to access. Returns article lists with metadata, sentiment scores, and geographic tagging.
- **Example query**: `https://api.gdeltproject.org/api/v2/doc/doc?query=journalist+arrested+first+amendment+sourcelang:english&mode=ArtList&maxrecords=25&format=json`
- **Freshness**: Updated every 15 minutes. Fastest news signal available free.
- **Cost**: Free. GDELT is an academic project (Kalev Leetaru, Georgetown University).
- **Caveats**: Volume is very high; filtering rules need to be precise to avoid false positives. Attribution is to GDELT, not original outlets.
- **URL**: https://blog.gdeltproject.org/gdelt-doc-2-0-api-debuts/

**Source B2: Media Cloud API**
- **What it covers**: News search API covering 1 billion+ stories from U.S. and global outlets. Particularly strong for tracking how topics spread across regional and local news, which GDELT can miss.
- **API**: `https://search.mediacloud.org/`. Python client available at `github.com/mediacloud/api-client`. Requires registration (free academic/nonprofit use).
- **Freshness**: Updates within hours of publication for indexed sources.
- **Cost**: Free for nonprofit/research use.
- **URL**: https://www.mediacloud.org/

**Type C — Specialized Databases**

**Source C1: PEN America Index of School Book Bans**
- **What it covers**: Twice-yearly report on book bans in K–12 schools, including specific titles, districts, and legislative/administrative action taken. PEN America provides CSV download.
- **Access**: Direct data download from pen.org/pen-america-index-of-school-book-bans/. CSV/JSON. No API; requires scheduling a periodic download (semi-annual publication).
- **Freshness**: Published twice per year; individual events between publications are documented in press releases.
- **Cost**: Free.
- **URL**: https://pen.org/research-and-reports/

**Type D — FOIA Request Feeds**

**Source D1: MuckRock FOIA Requests — Press Access Records**
- **What it covers**: FOIA requests filed through MuckRock targeting press access rules, journalist monitoring programs, and related records at federal agencies. MuckRock's API allows searching all public requests by agency and keyword.
- **API**: `https://www.muckrock.com/api_v1/foia/?q=press+access`. Returns JSON list of FOIA requests with their status, filing agency, date, and any released documents.
- **Freshness**: Real-time (requests appear in API as soon as filed or updated).
- **Cost**: Free to query. Filing new requests costs $20–40/request.
- **Rate limits**: 1 request/second sustained, burst to 20/second.
- **URL**: https://www.muckrock.com/api/

### 1.3 Legal Feasibility Table

| Source | Automated Ingestion Permitted | Attribution Required | Commercial Restrictions | Cost |
|--------|------------------------------|---------------------|------------------------|------|
| CourtListener RECAP | Yes — explicit API ToS allows it | Cite Free Law Project | None | Free |
| Press Freedom Tracker | Yes — open source data | Cite pressfreedomtracker.us | None | Free |
| Federal Register API | Yes — public domain | None required | None | Free |
| GDELT DOC 2.0 | Yes — free to use | Cite GDELT | Redistribution requires scrutiny | Free |
| Media Cloud | Yes — for nonprofit/research | Cite Media Cloud | Non-commercial use terms | Free |
| PEN America data | Yes — CC licensed | Cite PEN America | Non-commercial | Free |
| MuckRock API | Yes — ToS allows it | Cite MuckRock | None for querying | Free |

### 1.4 Priority Ranking

| Source | Completeness | Freshness | Uniqueness | Implementation Cost | Reliability | **Total** |
|--------|-------------|-----------|------------|--------------------|-----------|----|
| CourtListener RECAP | 8 | 8 | 9 | 10 | 9 | **44** |
| Press Freedom Tracker API | 9 | 7 | 10 | 10 | 8 | **44** |
| Federal Register API | 6 | 10 | 7 | 10 | 10 | **43** |
| GDELT DOC 2.0 | 7 | 10 | 6 | 10 | 7 | **40** |
| Media Cloud | 7 | 8 | 7 | 9 | 8 | **39** |
| MuckRock API | 5 | 9 | 8 | 9 | 7 | **38** |
| PEN America data | 6 | 3 | 9 | 10 | 9 | **37** |

**Implementation sequence**: (1) Press Freedom Tracker API and CourtListener RECAP — highest combined value, both free and well-documented. (2) Federal Register API — fast signal on executive actions. (3) GDELT — bulk signal processing, requires false-positive filtering investment. (4) Media Cloud — fills regional/local coverage gaps. (5) MuckRock — episodic use for specific monitoring campaigns.

---

## Section 2: Environmental Rollbacks Tracker

### 2.1 Current Sources (as of May 2026)

The `environmental-rollbacks-tracker.md` tracker currently draws from:

- **Harvard EELP Regulatory Tracker** (eelp.law.harvard.edu): The gold standard for rule-by-rule documentation. Monitored manually 2–3 times per week. High accuracy; moderate lag (typically 3–7 days from Federal Register publication to EELP update).
- **Federal Register** (federalregister.gov): Checked for EPA, Interior, NOAA, DOE, DOT publications. Manually browsed; no automated ingestion.
- **Earthjustice, NRDC, EDF press releases**: Checked via email subscriptions and website visits. Good for litigation signals.
- **EPA official press releases**: Monitored via the EPA newsroom. Good for agency-level announcements; agency propaganda frame requires editorial filtering.
- **Regulations.gov docket comments**: Occasionally checked for public comment deadlines and significant industry/advocacy comments. Not systematically ingested.

**Freshness assessment**: The tracker is current within 1–7 days for rules published in the Federal Register. Agency guidance changes, internal memo leaks, and enforcement data (rather than formal rules) have a longer lag — sometimes 2–4 weeks.

**Completeness gaps**:
- State-level environmental rollbacks are not tracked at all, despite being significant in oil/gas states (Wyoming, Texas, Louisiana).
- EPA enforcement actions (what violations go unprosecuted) require specific enforcement databases not currently consulted.
- Interior Department actions outside formal rulemaking (drilling approvals, monument revocations, BLM lease decisions) are covered sporadically.
- Chemical safety and TSCA actions are undercovered compared to air/climate.

**Estimated new entries per week**: 2–5 during active rulemaking periods, 1–2 in quieter windows.

### 2.2 New Automatable Sources

**Type A — Government/Judicial APIs**

**Source A1: Federal Register API — Filtered to EPA + Environmental Agencies**
- **What it covers**: All EPA, Interior (BLM, FWS, NPS), NOAA, DOE, and USDA rulemaking notices published in the Federal Register — proposed rules, final rules, and notices of intent.
- **API**: `https://www.federalregister.gov/api/v1/documents.json?conditions[agencies][]=environmental-protection-agency&conditions[type]=RULE,PRORULE,NOTICE`
- **Additional agency filters**: `interior-department`, `fish-and-wildlife-service`, `bureau-land-management`, `energy-department`
- **Freshness**: Same-day; Federal Register publishes at 8:45 a.m. ET daily.
- **Cost**: Free. No key required.

**Source A2: Regulations.gov API v4 — Environmental Docket Monitoring**
- **What it covers**: Every EPA and Interior rulemaking docket — supporting documents, public comments, and docket metadata. Especially useful for tracking comment periods (which signal the timeline to a final rule) and industry comment patterns.
- **API**: `https://api.regulations.gov/v4/documents?filter[agencyId]=EPA&api_key=DEMO_KEY`
- **Registration**: Free API key at api.data.gov/signup for higher rate limits (1,000 requests/hour vs. 40/hour for DEMO_KEY).
- **Freshness**: Updated as agencies post new documents; typically same-day for newly published notices.
- **Cost**: Free with API key.
- **URL**: https://open.gsa.gov/api/regulationsgov/

**Source A3: GovInfo API — EPA Enforcement and EIS Publications**
- **What it covers**: Environmental Impact Statements (EIS) published by agencies, final rules in the Code of Federal Regulations, and congressional documents about environmental legislation.
- **API**: `https://api.govinfo.gov/collections/CFR/2025-01-01/`. Requires API key (free at api.data.gov/signup).
- **Freshness**: Daily updates for new publications.
- **Cost**: Free.
- **URL**: https://www.govinfo.gov/developers

**Type B — News APIs**

**Source B1: GDELT Project — Environmental Filtering**
- **What it covers**: All news about environmental rollbacks, agency regulatory actions, oil and gas permitting, and environmental litigation.
- **Filter terms**: "EPA rollback," "methane rule," "Endangered Species Act," "clean air," "clean water," "wetlands permit," "climate regulation," "Federal Register final rule."
- **API**: Same GDELT DOC 2.0 endpoint; different query terms.
- **Cost**: Free.
- **Note**: Produces high volume; will need keyword blacklisting to suppress routine weather and non-regulatory environmental news.

**Source B2: Justia Regulations Tracker — EPA Feed**
- **What it covers**: Justia aggregates Federal Register documents by agency and provides topic feeds. EPA-specific page updates daily.
- **URL**: `https://regulations.justia.com/regulations/fedreg/agencies/environmental-protection-agency`
- **Access**: Web scraping or RSS. Justia does not publish a formal API but the structure is consistent enough for parsing.
- **Freshness**: Daily (follows Federal Register publication schedule).
- **Cost**: Free.

**Type C — Specialized Databases**

**Source C1: Harvard EELP Regulatory Tracker RSS/Web Monitoring**
- **What it covers**: Curated, expert-verified summary of every significant environmental regulatory change. The most reliable single source for this tracker.
- **Access**: No formal API. The EELP tracker pages follow a consistent URL pattern (`eelp.law.harvard.edu/tracker/[rule-name]/`). A change-detection webhook (via services like Changedetection.io or Distill.io) monitoring the EELP tracker index page will alert when new entries are posted.
- **Freshness**: EELP updates within 3–7 days of major regulatory actions.
- **Cost**: Free to monitor; change-detection services run $5–15/month.
- **URL**: https://eelp.law.harvard.edu/tracker-type/regulatory-tracker/

**Source C2: Earthjustice Active Cases RSS**
- **What it covers**: All Earthjustice litigation — the primary environmental public interest law firm. New case filings and updates on ongoing environmental litigation.
- **Access**: RSS feed at `https://earthjustice.org/rss.xml`. Also filterable by topic on their website.
- **Freshness**: Published within 24 hours of filing or decision.
- **Cost**: Free.

**Type D — FOIA Request Feeds**

**Source D1: MuckRock — EPA and Interior FOIA Requests**
- **What it covers**: Pending and completed FOIA requests targeting EPA enforcement records, Interior drilling approval documents, and agency communications about rollback decisions.
- **API**: `https://www.muckrock.com/api_v1/foia/?q=EPA+enforcement&agency=epa`
- **Value**: Released FOIA documents often surface regulatory decisions that agencies did not formally announce.
- **Cost**: Free to query.

### 2.3 Legal Feasibility Table

| Source | Automated Ingestion Permitted | Attribution Required | Commercial Restrictions | Cost |
|--------|------------------------------|---------------------|------------------------|------|
| Federal Register API | Yes — public domain | None | None | Free |
| Regulations.gov API | Yes — ToS permits | Cite data.gov | None | Free (API key) |
| GovInfo API | Yes — public domain | None | None | Free (API key) |
| GDELT | Yes | Cite GDELT | Redistribution scrutiny | Free |
| Justia feed | Scraping: check ToS | Cite Justia | Non-commercial preferred | Free |
| Harvard EELP monitoring | Change-detection: permitted | Cite EELP | Non-commercial | Free + $5–15/mo |
| Earthjustice RSS | Yes — RSS is public | Cite Earthjustice | None | Free |
| MuckRock API | Yes | Cite MuckRock | None for querying | Free |

### 2.4 Priority Ranking

| Source | Completeness | Freshness | Uniqueness | Implementation Cost | Reliability | **Total** |
|--------|-------------|-----------|------------|--------------------|-----------|----|
| Federal Register API | 9 | 10 | 7 | 10 | 10 | **46** |
| Regulations.gov API v4 | 8 | 9 | 8 | 9 | 9 | **43** |
| Harvard EELP monitoring | 9 | 6 | 9 | 8 | 8 | **40** |
| Earthjustice RSS | 7 | 9 | 8 | 10 | 8 | **42** |
| GDELT | 6 | 10 | 5 | 9 | 7 | **37** |
| GovInfo API | 6 | 8 | 7 | 9 | 9 | **39** |
| Justia feed | 5 | 9 | 4 | 7 | 7 | **32** |
| MuckRock API | 5 | 8 | 8 | 9 | 7 | **37** |

**Implementation sequence**: (1) Federal Register API — single most reliable signal, near-zero effort to implement. (2) Regulations.gov API — covers rulemaking lifecycle including comment periods that flag upcoming final rules. (3) Earthjustice RSS — catches litigation responses to rollbacks. (4) GovInfo — supplemental for EIS and CFR tracking. (5) EELP change-detection — adds expert curation layer. (6) GDELT for bulk signal on news coverage of rollbacks.

---

## Section 3: Police Brutality / Consent Decree Tracker

### 3.1 Current Sources (as of May 2026)

The `police-brutality-consent-decree-tracker.md` and `consent-decree-defiance-tracker.md` trackers draw from:

- **DOJ press releases**: Monitored via the DOJ newsroom (justice.gov/news). Good for federal prosecution announcements; biased toward cases the administration chooses to publicize.
- **ACLU national and state chapter case pages**: Checked manually 1–2 times per week. Reliable for civil litigation; under-covers state criminal prosecution of officers.
- **National Immigrant Justice Center and NIJC court cases**: Monitored for cross-over cases.
- **ProPublica investigative pieces**: Read as published. Irregular; not a systematic source.
- **Local news monitoring**: The most significant gap — DOJ pattern-or-practice investigations in cities like Phoenix, Memphis, and Oklahoma City are best covered by local newsrooms, not national outlets.
- **NPR, CNN, New York Times**: Monitored for high-profile incidents.

**Freshness assessment**: High-profile incidents (nationally covered police killings, major court rulings) are added within 24–48 hours. Lower-profile incidents, particularly in smaller cities, are systematically undercovered. Consent decree monitoring updates lag 1–4 weeks behind actual court filings.

**Completeness gaps**:
- Civil rights complaints filed at state courts (not federal) are largely untracked.
- Individual officer discipline outcomes are rarely captured unless part of a consent decree case.
- State attorney general investigations of police departments (as an alternative to DOJ, now that DOJ has stepped back) are not systematically monitored.
- ICE use-of-force incidents (increasingly relevant post-2025) are not systematically included.

**Estimated new entries per week**: 3–8 during active news periods, 1–3 during quieter periods.

### 3.2 New Automatable Sources

**Type A — Government/Judicial APIs**

**Source A1: CourtListener RECAP — Section 1983 Cases**
- **What it covers**: All federal civil rights cases filed under 42 U.S.C. § 1983 (the primary vehicle for police misconduct civil litigation). Can query by statute citation, case type ("civil rights"), and keywords ("police," "excessive force," "Fourth Amendment").
- **API**: `https://www.courtlistener.com/api/rest/v4/dockets/?q=excessive+force+police+section+1983&type=d&filed_after=2026-01-01`
- **Volume**: High — hundreds of § 1983 cases filed monthly. Need filtering for cases that represent new systemic patterns, not routine individual incidents.
- **Freshness**: 1–24 hour lag.
- **Cost**: Free.

**Source A2: DOJ Press Releases API — Civil Rights Division**
- **What it covers**: Press releases from the DOJ's Civil Rights Division (which includes Special Litigation Section, the unit that handles pattern-or-practice investigations and consent decrees), and from U.S. Attorneys' offices on civil rights prosecutions.
- **API**: The DOJ maintains an undocumented but consistent JSON endpoint. The `usdoj` R package (available on CRAN and GitHub at `rOpenGov/usdoj`) wraps a DOJ API that returns press releases filtered by keyword.
- **Direct RSS**: `https://www.justice.gov/usao/rss` (all USAO press releases), filterable by topic.
- **Civil Rights Division feed**: `https://www.justice.gov/crt/civil-rights-news-releases`
- **Freshness**: Same-day for new press releases.
- **Cost**: Free.
- **URL**: https://www.justice.gov/developer

**Source A3: Law Enforcement Knowledge Lab — Federal Interventions Dashboard**
- **What it covers**: The Federal Interventions Dashboard tracks all active and terminated federal Civil Consent Decrees and Settlement Agreements between DOJ and local law enforcement. Includes case status, monitoring status, and case document links.
- **Access**: `https://leknowledgelab.org/resources/federal-interventions-dashboard/`. No formal API but structured page; change-detection monitoring appropriate.
- **Freshness**: Updated as cases change status.
- **Cost**: Free.

**Type B — News APIs**

**Source B1: GDELT — Police Violence and Civil Rights Filtering**
- **What it covers**: News articles about police use of force, police killings, civil rights settlements, consent decrees, and DOJ investigations. GDELT's 15-minute update cycle makes it the fastest signal for breaking incidents.
- **Query terms**: "police brutality," "police shooting," "consent decree," "excessive force," "civil rights violation," "DOJ investigation police," "qualified immunity."
- **Cost**: Free.

**Source B2: Mapping Police Violence Data (Airtable)**
- **What it covers**: The most comprehensive national database of people killed by police in the U.S., maintained by Samuel Sinyangwe and team. Data is updated within 24–48 hours of incidents, sourced from news, social media, and official records. Available as a public Airtable base.
- **Access**: Public Airtable base at `https://airtable.com/appzVzSeINK1S3EVR/shroOenW19l1m3w0H/tblxearKzw8W7ViN8`. Airtable provides a read API for public bases.
- **Freshness**: 24–48 hours for new incidents.
- **Cost**: Free. Airtable API access for public bases requires an API token but is free.

**Type C — Specialized Databases**

**Source C1: Police Funding Database — LDF/TMI Consent Decrees**
- **What it covers**: Comprehensive database of consent decrees maintained by the NAACP Legal Defense Fund and TMI Strategy. Lists all active decrees with source documentation.
- **Access**: `https://policefundingdatabase.org/explore-the-database/consent-decrees/`. Structured HTML; parseable. No formal API.
- **Freshness**: Updated as new information is verified.
- **Cost**: Free.

**Source C2: State Attorney General Press Releases — Police Reform**
- **What it covers**: As federal DOJ has retreated from pattern-or-practice enforcement, state AGs (California, New York, Massachusetts, Minnesota, Washington) have partially filled the gap. Their press releases announce new state-level investigations and enforcement actions.
- **Access**: RSS feeds for CA DOJ (`https://oag.ca.gov/rss`), NYAG (`https://ag.ny.gov/press-releases`), and other state AG offices.
- **Freshness**: Published same-day as announcements.
- **Cost**: Free.

**Type D — FOIA Request Feeds**

**Source D1: MuckRock — Police Accountability FOIA Requests**
- **What it covers**: FOIA requests targeting police use-of-force data, misconduct records, and DOJ investigation files. Released documents often surface patterns not otherwise disclosed.
- **API**: `https://www.muckrock.com/api_v1/foia/?q=police+use+of+force&status=done`
- **Cost**: Free to query.

### 3.3 Legal Feasibility Table

| Source | Automated Ingestion Permitted | Attribution Required | Commercial Restrictions | Cost |
|--------|------------------------------|---------------------|------------------------|------|
| CourtListener RECAP | Yes | Cite Free Law Project | None | Free |
| DOJ Press Releases RSS | Yes — public domain | None required | None | Free |
| Law Enforcement Knowledge Lab | Change-detection: check ToS | Cite LEKL | None specified | Free |
| GDELT | Yes | Cite GDELT | Redistribution scrutiny | Free |
| Mapping Police Violence | Public Airtable: check ToS | Cite MPV | Non-commercial preferred | Free |
| Police Funding Database | Scraping: check ToS | Cite LDF/TMI | Non-commercial | Free |
| State AG RSS feeds | Yes — public domain | None | None | Free |
| MuckRock API | Yes | Cite MuckRock | None for querying | Free |

### 3.4 Priority Ranking

| Source | Completeness | Freshness | Uniqueness | Implementation Cost | Reliability | **Total** |
|--------|-------------|-----------|------------|--------------------|-----------|----|
| CourtListener RECAP | 8 | 9 | 8 | 10 | 9 | **44** |
| Mapping Police Violence | 9 | 8 | 10 | 8 | 8 | **43** |
| DOJ Civil Rights RSS | 7 | 10 | 6 | 10 | 9 | **42** |
| State AG RSS feeds | 7 | 9 | 8 | 10 | 8 | **42** |
| GDELT | 6 | 10 | 5 | 9 | 7 | **37** |
| Law Enforcement Knowledge Lab | 8 | 6 | 9 | 7 | 7 | **37** |
| MuckRock API | 5 | 8 | 8 | 9 | 7 | **37** |
| Police Funding Database | 7 | 5 | 8 | 7 | 7 | **34** |

**Implementation sequence**: (1) CourtListener RECAP for federal civil rights filings. (2) DOJ Civil Rights RSS for federal prosecution signals. (3) State AG RSS feeds for filling the post-DOJ enforcement gap. (4) Mapping Police Violence Airtable for comprehensive incident data. (5) GDELT for rapid signal. (6) Law Enforcement Knowledge Lab for consent decree status.

---

## Section 4: Prosecutorial Weaponization Tracker

### 4.1 Current Sources (as of May 2026)

There is no dedicated `prosecutorial-weaponization` tracker file in the current directory. Coverage of this topic is distributed across `first-amendment-suppression.md` (Section 7, covering the SPLC indictment) and `litigation-tracker-2026.md`. This represents the largest data gap in the current tracker ecosystem.

**Current ad-hoc sources**:
- **Major national news** (NYT, WaPo, Reuters): catches high-profile political prosecution announcements but misses USAO press releases about politically connected defendants in non-marquee cases.
- **Just Security** (justsecurity.org): Provides analysis of Trump DOJ pattern, but not a systematic data source.
- **Protect Democracy Retaliatory Action Tracker**: A structured tracker of Trump administration investigations and prosecutions of political opponents, available at protectdemocracy.org/work/retaliatory-action-tracker/. Currently manually checked.
- **SPLC updates**: Following SPLC's April 2026 indictment, SPLC communications are now monitored. Previously not a source.

**Freshness assessment**: No systematic monitoring. Incidents surface when they receive national media coverage. Estimate: 50–70% of politically relevant prosecutions are currently missed entirely.

**Key gap**: This tracker has the largest ratio of data gap to political significance of any of the four trackers. It needs the most new source infrastructure.

### 4.2 New Automatable Sources

**Type A — Government/Judicial APIs**

**Source A1: PACER / CourtListener — USAO Criminal Filings**
- **What it covers**: All criminal indictments and information filed by U.S. Attorneys' offices. Filterable by district, defendant party affiliation, and case keywords. Can monitor for defendants who are public figures, civil society organizations, journalists, or former officials.
- **API**: `https://www.courtlistener.com/api/rest/v4/dockets/?q=indictment+political&type=d&court=dcd,cacd,sdny&filed_after=2026-01-01`
- **Freshness**: 1–24 hours from filing.
- **Cost**: Free.

**Source A2: DOJ All USAO Press Releases RSS**
- **What it covers**: Every press release from all 94 U.S. Attorneys' offices. This is the primary official signal for new prosecutions — the DOJ always issues a press release when charging high-profile defendants. RSS feed covers all 94 districts.
- **Feed**: `https://www.justice.gov/usao/pressreleases` with district filtering via URL parameters. The USAO RSS index is at `https://www.justice.gov/usao/rss`.
- **Freshness**: Published same day as charging announcement.
- **Cost**: Free.
- **Note**: Very high volume (hundreds of press releases weekly). Requires keyword filtering for politically relevant cases: names of known targets, civil society organizations, former officials, media organizations.

**Source A3: Congressional Record API — Congressional Statements on Prosecutions**
- **What it covers**: Congressional floor statements, committee hearing transcripts, and press releases from congressional members documenting political use of DOJ. Congressional Record is public domain.
- **API**: GovInfo API, collection `CREC` (Congressional Record). `https://api.govinfo.gov/collections/CREC/2026-01-01/`
- **Also**: ProPublica's Congress API tracked congressional press releases mentioning bills (now deprecated), but C-SPAN's Congressional Record remains accessible through GovInfo.
- **Freshness**: Congressional Record publishes daily when Congress is in session.
- **Cost**: Free (GovInfo API key required, free at api.data.gov).

**Source A4: PACER Case Locator — Defendant Search**
- **What it covers**: The PACER Case Locator (PCL) API allows querying the national case index by party name. For a list of known persons targeted by the Trump administration, PCL can detect when they become defendants.
- **API**: PCL REST API documented at `https://pacer.uscourts.gov/help/pacer/pacer-case-locator-pcl-api-user-guide`
- **Authentication**: PACER account required (free to register; $0.10/page for documents accessed, but search queries are free).
- **Freshness**: Updated as courts submit index entries (typically same-day to next business day).

**Type B — News APIs**

**Source B1: GDELT — Political Prosecution Filtering**
- **What it covers**: News coverage of politically motivated prosecutions, DOJ investigations of political opponents, selective enforcement claims.
- **Query terms**: "selective prosecution," "vindictive prosecution," "political prosecution," "DOJ political," specific names of known targets.
- **Cost**: Free.

**Source B2: Media Cloud — Regional Coverage of Political Prosecutions**
- **What it covers**: Local news coverage of prosecutions that do not reach national outlets. A federal prosecution in a red-state district targeting a progressive civil society organization may receive significant local coverage but miss national radar.
- **Cost**: Free for research use.

**Type C — Specialized Databases**

**Source C1: Protect Democracy Retaliatory Action Tracker**
- **What it covers**: Expert-curated tracker of Trump administration arrests, investigations, and prosecutions that appear retaliatory or politically motivated. Applies a three-question test (was the target identified as political opposition before the action? Does the legal theory have precedent? Is there a pattern of similar actions?).
- **Access**: `https://protectdemocracy.org/work/retaliatory-action-tracker/`. No API; change-detection monitoring appropriate. The page is structured enough for consistent parsing.
- **Freshness**: Updated as new cases are identified; typically 2–5 day lag from public announcement.
- **Cost**: Free.

**Source C2: Wikipedia — "Targeting of Political Opponents Under Trump" Page**
- **What it covers**: The Wikipedia page `Targeting of political opponents and civil society under the second Trump administration` is actively maintained by a community of editors and provides a crowd-sourced index of targeted individuals and organizations with source citations.
- **Access**: Wikipedia's REST API at `https://en.wikipedia.org/api/rest_v1/page/summary/Targeting_of_political_opponents_and_civil_society_under_the_second_Trump_administration`. Revision history available.
- **Value**: Acts as a secondary cross-reference to verify completeness; the edit history timestamps when new targets are documented.
- **Cost**: Free.

**Type D — FOIA Request Feeds**

**Source D1: MuckRock — DOJ Political Prosecution Records**
- **What it covers**: FOIA requests targeting DOJ communications about politically sensitive cases, prosecutorial decision memos, and AG office communications about political defendants.
- **API**: `https://www.muckrock.com/api_v1/foia/?q=DOJ+political+prosecution+retaliatory`
- **Cost**: Free to query.

**Source D2: PACER Bulk Data — Section 3 Disqualification Filings**
- **What it covers**: The Free Law Project's RECAP archive specifically documents Section 3 (Fourteenth Amendment disqualification) litigation, which is a specialized subset of politically motivated prosecution resistance.
- **Access**: CourtListener search for cases mentioning "Section 3" or "Fourteenth Amendment disqualification."
- **Cost**: Free.

### 4.3 Legal Feasibility Table

| Source | Automated Ingestion Permitted | Attribution Required | Commercial Restrictions | Cost |
|--------|------------------------------|---------------------|------------------------|------|
| CourtListener RECAP | Yes | Cite Free Law Project | None | Free |
| DOJ USAO RSS | Yes — public domain | None | None | Free |
| Congressional Record (GovInfo) | Yes — public domain | None | None | Free (API key) |
| PACER Case Locator API | Yes — ToS permits | None | PACER account required | Free (search); $0.10/page (docs) |
| GDELT | Yes | Cite GDELT | Redistribution scrutiny | Free |
| Media Cloud | Yes — research use | Cite Media Cloud | Non-commercial | Free |
| Protect Democracy Tracker | Change-detection: check ToS | Cite Protect Democracy | Non-commercial | Free |
| Wikipedia API | Yes — CC-BY-SA | Cite Wikipedia | None | Free |
| MuckRock API | Yes | Cite MuckRock | None for querying | Free |

### 4.4 Priority Ranking

| Source | Completeness | Freshness | Uniqueness | Implementation Cost | Reliability | **Total** |
|--------|-------------|-----------|------------|--------------------|-----------|----|
| DOJ USAO RSS | 8 | 10 | 7 | 10 | 10 | **45** |
| CourtListener RECAP | 8 | 9 | 8 | 10 | 9 | **44** |
| Protect Democracy Tracker | 8 | 7 | 9 | 8 | 8 | **40** |
| PACER Case Locator | 7 | 8 | 9 | 7 | 8 | **39** |
| GDELT | 6 | 10 | 5 | 9 | 7 | **37** |
| Media Cloud | 6 | 8 | 7 | 9 | 8 | **38** |
| Congressional Record | 5 | 8 | 8 | 8 | 9 | **38** |
| Wikipedia API | 5 | 6 | 7 | 10 | 6 | **34** |
| MuckRock API | 4 | 8 | 8 | 9 | 7 | **36** |

**Implementation sequence**: (1) DOJ USAO RSS — the primary official signal for any new prosecution. (2) CourtListener RECAP — catches what DOJ does not announce. (3) Protect Democracy tracker monitoring — expert curation layer. (4) PACER Case Locator — proactive monitoring for specific named targets. (5) GDELT — news coverage signal. (6) Media Cloud — regional coverage gap-fill.

---

## Cross-Tracker Summary: Top Implementation Priorities

Looking across all four trackers, five sources appear in multiple tracker priority rankings:

| Source | Trackers Covered | Combined Priority | Implementation Effort |
|--------|-----------------|------------------|----------------------|
| CourtListener RECAP API | FA, PB, PW | Very High | Low (free, documented) |
| Federal Register API | ENV, (FA) | Very High | Very Low (free, documented) |
| GDELT DOC 2.0 | FA, ENV, PB, PW | High | Medium (filtering investment) |
| MuckRock API | FA, ENV, PB, PW | Medium | Low (free, documented) |
| Media Cloud | FA, PB, PW | Medium | Low (free, registration) |

**Recommendation**: Phase the implementation in two waves. Wave 1 (Weeks 1–2): CourtListener RECAP, Federal Register API, DOJ USAO RSS, Press Freedom Tracker API, Regulations.gov API. These are all free, well-documented, and immediately useful. Wave 2 (Weeks 3–6): GDELT filtering, Media Cloud integration, PACER Case Locator, Protect Democracy monitoring, state AG RSS feeds.

Total Wave 1 implementation cost: $0. Wave 2 adds nominal hosting cost for automated pipeline (estimated $10–30/month on a small VPS or AWS Lambda).

---

*Sources for this audit: [PACER API docs](https://pacer.uscourts.gov/help/pacer/pacer-case-locator-pcl-api-user-guide) | [CourtListener API](https://www.courtlistener.com/help/api/) | [Press Freedom Tracker API](https://pressfreedomtracker.us/data/) | [Federal Register API](https://www.federalregister.gov/developers/documentation/api/v1) | [Regulations.gov API](https://open.gsa.gov/api/regulationsgov/) | [GDELT DOC 2.0](https://blog.gdeltproject.org/gdelt-doc-2-0-api-debuts/) | [Media Cloud](https://www.mediacloud.org/) | [MuckRock API](https://www.muckrock.com/api/) | [Mapping Police Violence](https://mappingpoliceviolence.org/methodology) | [Protect Democracy Tracker](https://protectdemocracy.org/work/retaliatory-action-tracker/) | [Earthjustice RSS](https://earthjustice.org/rss.xml) | [Harvard EELP](https://eelp.law.harvard.edu/tracker-type/regulatory-tracker/) | [GovInfo API](https://www.govinfo.gov/developers) | [Law Enforcement Knowledge Lab](https://leknowledgelab.org/resources/federal-interventions-dashboard/)*
