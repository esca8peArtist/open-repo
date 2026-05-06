---
title: "Tracker Source Audit — Detailed Four-Tracker Assessment"
subtitle: "Current source freshness, bias, coverage gaps, and 5+ new source recommendations per tracker with feasibility ratings"
date: 2026-05-06
status: complete
phase: phase-2-preparation
project: resistance-research
purpose: Phase 2 enrichment strategy — immediate post-Phase-1-launch execution
cross_references:
  - tracker-automation-feasibility.md
  - tracker-visualization-prototype-specs.md
  - tracker-measurement-framework.md
  - first-amendment-suppression.md
  - environmental-rollbacks-tracker.md
  - police-brutality-consent-decree-tracker.md
  - domains/domain-29-prosecutorial-weaponization-and-doj-capture.md
---

# Tracker Source Audit — Detailed Assessment

*Created: May 6, 2026. This document delivers Phase 2 enrichment preparation for four active civil liberties trackers. It assumes Phase 1 distribution is live and users are actively consulting these trackers. Every recommendation is grounded in what a solo operator can realistically implement without paid subscriptions or institutional database access.*

**Lead finding**: The most significant gap across all four trackers is not in major national news coverage — that is adequately captured — but in three specific areas: (1) state-level developments that never reach national outlets, (2) court filings that are searchable in PACER/CourtListener but not surfaced by news monitoring, and (3) agency-level enforcement data (what is NOT being enforced) that requires dedicated database access, not media tracking. The first two gaps are closable with free APIs in weeks. The third requires ongoing quarterly manual effort that cannot be fully automated.

---

## Section 1: First Amendment Suppression Tracker

### 1.1 Current Sources

The `first-amendment-suppression.md` tracker is maintained through six primary input channels as of May 2026.

**National news monitoring (NYT, WaPo, Guardian, CNN, Reuters, AP)**: The backbone of current coverage. Catches major incidents — the Pentagon press rules case, the Associated Press exclusion, the FBI raid on Hannah Natanson — reliably. Lag from event to tracker entry: 24–72 hours for nationally prominent incidents. Incidents that do not reach national prominence are systematically missed.

**ACLU case tracker (aclu.org/cases)**: Checked manually every 1–2 weeks. Reliable for active federal litigation but has a publication lag of 1–7 days from filing to page update. ACLU also under-covers state-level First Amendment cases that ACLU state affiliates handle without national visibility.

**Freedom of the Press Foundation (FPF) and Reporters Committee for Freedom of the Press (RCFP)**: Monitored via email subscriptions and periodic website visits. Both organizations publish high-quality analysis but are not comprehensive incident-tracking databases. FPF press releases arrive when FPF chooses to publish them, not on a systematic schedule.

**U.S. Press Freedom Tracker (pressfreedomtracker.us)**: The single most valuable existing source. Jointly maintained by FPF and Committee to Protect Journalists (CPJ), it systematically documents all verified press freedom incidents in the U.S. Currently consulted ad hoc rather than through its API. This is the most actionable immediate upgrade available at zero cost.

**RSF (Reporters Without Borders) World Press Freedom Index**: Annual publication. Used for contextual framing ("US now ranks 64th globally") but not for tracking individual incidents. Publication frequency makes it unsuitable for current tracking.

**PEN America, CPJ, EFF websites**: Checked ad hoc. PEN America is the authoritative source for book bans and campus speech restrictions. CPJ covers journalist arrests globally and in the U.S. EFF covers digital free speech and government surveillance intersections with First Amendment rights. All three are currently used episodically rather than systematically.

### 1.2 Freshness Assessment

**Update lag**: Average 3–7 days from event to tracker entry during active news periods. During lower-attention periods (summer, holidays, competing major news), lag extends to 10–14 days. There is no systematic review process — coverage depends on the researcher actively reading news.

**Lag patterns by event type**:
- Presidential/cabinet-level press freedom actions: 1–2 day lag (high national salience, surfaces everywhere)
- Federal court rulings: 2–5 day lag (requires reading legal news outlets, which are not always primary news sources)
- State-level anti-protest laws: 7–21 day lag or never (requires state legislative monitoring not currently in place)
- SLAPP suit filings in state courts: Often never captured (no state court filing monitoring)
- Journalist arrests at protests: 1–3 day lag if nationally covered; 3–21 days if only local coverage

**The April 2026 LAPD journalist assault entry (Section 1.9)** is an instructive case: the incident happened April 11 at an LA immigration protest; tracker entry was added April 27 — a 16-day lag. The event was documented by the LA Press Club and covered in local Los Angeles outlets before reaching the tracker.

### 1.3 Bias Audit

**Overrepresented**: Federal executive branch actions; cases involving national news outlets or well-known journalists; cases where major civil liberties organizations have already filed litigation.

**Underrepresented**: Independent journalists and freelancers (the Press Freedom Tracker shows they face higher arrest rates than staff journalists, but they generate less national news coverage); state and local law enforcement as actors; cases resolved without litigation (informal suppression through bureaucratic obstruction); First Amendment rights of ordinary citizens rather than journalists.

**Ideological skew analysis**: The current source set is predominantly progressive or press-freedom-focused (ACLU, FPF, RCFP, PEN America, CPJ). This produces a coverage gap on the right: First Amendment suppression of conservative speech by institutions (social media platforms, universities acting on federal DEI pressure) receives less systematic coverage even though it constitutes real First Amendment activity. The tracker should be factually complete, not ideologically filtered. Adding the Foundation for Individual Rights and Expression (FIRE) as a source would fill this gap without compromising the tracker's accuracy.

**Geographic skew**: Current coverage is 70%+ Washington DC and major coastal metros. Small-city and rural First Amendment incidents (local government suppression of small-town newspapers, library board challenges, zoning restrictions on religious assembly) are structurally undercovered.

### 1.4 Coverage Gap Analysis

**Gap 1 — State anti-protest legislation**: The tracker captured the Kansas student protest law (enacted April 10–11, 2026, via veto override) but only after it became nationally prominent. Dozens of similar state-level bills are filed each legislative session in states including Florida, Texas, Georgia, Tennessee, Idaho, and Montana. State legislature session calendars and bill-tracking tools (LegiScan API, OpenStates API) could surface these at introduction stage, not enactment stage — which is when advocacy intervention is still possible.

**Gap 2 — SLAPP suits in state courts**: Section 4 of the tracker covers SLAPP suits. The Kash Patel $250M defamation suit against The Atlantic (Section 4.6) was captured because it's a federal official making national news. The dozens of smaller SLAPP suits filed at state courts against local journalists, activists, and small nonprofits are not systematically tracked. The Lumen Database (a database of takedown requests and legal threats, maintained by Harvard's Berkman Klein Center) captures the digital-rights SLAPP intersection; state court filings require PACER/CourtListener monitoring filtered for media defendant + defamation or tortious interference claim type.

**Gap 3 — Digital speech restrictions**: The tracker's Section 3 covers government-coerced deplatforming but does not systematically cover First Amendment implications of algorithmic content moderation under government pressure, Section 230 legislative activity, or state social media laws (the NetChoice v. Paxton litigation track, state age-verification laws with speech implications). EFF's Deeplinks blog is the authoritative source for this area and is not currently monitored.

**Gap 4 — Religious freedom and assembly**: First Amendment protection of religious practice and assembly is substantively distinct from press freedom but constitutionally related. The current tracker has zero coverage of this category. During periods of immigration enforcement, religious institutions providing sanctuary face genuine First Amendment assembly/religion questions. RFRA (Religious Freedom Restoration Act) litigation is tracked by the Becket Fund for Religious Liberty and the ACLU simultaneously (from opposing directions) — both are currently absent from the source set.

**Gap 5 — International dimensions**: The tracker's World Press Freedom Day 2026 entry (US ranks 64th, Section A.8) captures the aggregate international ranking but not the specific incidents that caused it. RSF's full incident database, CPJ's Prison Census (journalists imprisoned globally with U.S. connections), and the International Federation of Journalists alerts cover transnational First Amendment dimensions.

### 1.5 Recommended New Sources

**Source 1: U.S. Press Freedom Tracker API (pressfreedomtracker.us/api/edge/)**
- **What it adds**: All verified press freedom incidents documented by FPF/CPJ, updated within 24–72 hours of occurrence. Currently consulted ad hoc; switching to API ingestion would produce a daily automated feed.
- **API**: `GET /api/edge/incidents/?date_lower=2026-05-01` returns all incidents after a specified date. Returns JSON with incident type, date, location, media outlet, and source URLs.
- **Freshness after upgrade**: Same-day to next-day for major incidents; 1–3 day lag for verified incidents.
- **Cost**: Free. No API key required.
- **Feasibility**: Immediate. This is a drop-in upgrade requiring 20 lines of Python and a cron job.
- **Bias effect**: FPF/CPJ are press-freedom-focused (not ideologically partisan on left/right content politics) — this addition does not worsen the bias profile.

**Source 2: Foundation for Individual Rights and Expression (FIRE) Newsdesk**
- **What it adds**: First Amendment cases involving campus speech restrictions, government viewpoint discrimination, and cases where conservatives are the speech targets. FIRE tracks cases across the ideological spectrum but documents many right-leaning speech suppression cases that do not appear in current sources.
- **Access**: FIRE's newsdesk (thefire.org/news) publishes new cases; RSS feed available at `thefire.org/feed`. No API.
- **Freshness**: Updated daily; cases published within 24 hours of major developments.
- **Cost**: Free.
- **Feasibility**: RSS ingestion, lowest implementation effort. Requires editorial filter to identify cases relevant to tracker scope (state action, not private employer action).
- **Bias effect**: Partially corrects geographic and ideological skew in current source set. FIRE applies the same First Amendment principles regardless of the speaker's political views; adding FIRE does not introduce partisan bias.

**Source 3: LegiScan API (legiscan.com/legiscan-api) — State Anti-Protest Bill Monitoring**
- **What it adds**: Real-time legislative tracking across all 50 state legislatures. Can monitor for bills matching keyword queries ("protest," "demonstration," "public assembly," "criminal trespass," "disorderly conduct" with penalty enhancement language) in states with active anti-protest legislation histories.
- **API**: LegiScan REST API v1. Free tier: 30,000 operations/month (adequate for weekly bill monitoring). Requires API key (free registration).
- **Endpoint**: `GET /api/?key={API_KEY}&op=getSearch&state=ALL&query=anti-protest`
- **Freshness**: Updated daily for bill status changes; introduces to tracker at bill introduction stage rather than enactment.
- **Cost**: Free tier adequate for this use case.
- **Feasibility**: Medium. Requires keyword calibration to reduce false positives (many bills about "public demonstration" are permit procedures, not restrictions). Realistic implementation time: 4–6 hours.
- **Important constraint**: Anti-protest bills are introduced in large numbers but most die in committee; the tracker should note bill status (introduced vs. passed committee vs. enacted) to avoid overcounting.

**Source 4: Lumen Database (lumendatabase.org) — Legal Threats Against Speech**
- **What it adds**: The Lumen Database, maintained by Harvard's Berkman Klein Center, aggregates DMCA takedown requests and cease-and-desist letters sent to online platforms. For the First Amendment tracker, the relevant subset is letters threatening legal action against speech (potential SLAPP suits) before a formal lawsuit is filed. This provides earlier warning than PACER monitoring.
- **API**: `GET https://lumendatabase.org/notices.json?term=first+amendment&sort_by=date_received&sort_order=desc`
- **Freshness**: Updated within 24 hours of new submissions; major platforms (Google, Twitter/X, GitHub) submit in near-real-time.
- **Cost**: Free. API access requires registration (free).
- **Feasibility**: Low effort. Primary challenge: volume is high (thousands of notices daily). Filter to notices involving government actors or public figures as senders; exclude pure copyright/trademark notices.
- **Bias effect**: Neutral. Lumen covers legal threats from actors across the political spectrum.

**Source 5: EFF Deeplinks Blog RSS (eff.org/deeplinks/rss)**
- **What it adds**: EFF's Deeplinks is the authoritative source for digital civil liberties: surveillance law, government censorship of online speech, Section 230, state social media laws, algorithmic speech suppression. These are First Amendment issues that are structurally absent from the current tracker.
- **Access**: RSS feed at `https://www.eff.org/deeplinks/rss`. Updates daily.
- **Freshness**: Published within hours of EFF's analysis being ready; typically same-day as court decisions for cases EFF is tracking.
- **Cost**: Free.
- **Feasibility**: Lowest possible — RSS subscription in any news aggregator. Requires editorial filter to distinguish tracker-relevant items (government action affecting speech) from pure technology law items.

**Source 6 (bonus): OpenStates API (openstates.org/api) — Alternative to LegiScan**
- **What it adds**: Open States is an open-source alternative to LegiScan covering state legislative data. Slightly less comprehensive than LegiScan for bill text but fully free with no rate limits for reasonable use.
- **API**: `https://v3.openstates.org/bills?q=anti-protest&include=abstracts`
- **Cost**: Free. API key required (free registration).
- **Feasibility**: Same as LegiScan; both can be implemented; LegiScan has better coverage, OpenStates has better terms.

### 1.6 Source Feasibility Summary Table

| Source | Automated Ingestion | Update Frequency | Cost | Implementation Effort | Priority |
|--------|---------------------|------------------|------|-----------------------|----------|
| Press Freedom Tracker API | Yes — explicit API | 24–72 hours | Free | 2 hours | **1** |
| FIRE Newsdesk RSS | Yes — RSS | Daily | Free | 30 minutes | **2** |
| EFF Deeplinks RSS | Yes — RSS | Daily | Free | 30 minutes | **3** |
| LegiScan API | Yes — REST API | Daily | Free (30K ops/mo) | 4–6 hours | **4** |
| Lumen Database API | Yes — REST API | Near real-time | Free | 3–4 hours | **5** |
| OpenStates API | Yes — REST API | Daily | Free | 3–4 hours | **6** |

---

## Section 2: Environmental Rollbacks Tracker

### 2.1 Current Sources

The `environmental-rollbacks-tracker.md` is the most source-complete of the four trackers. Its existing source set includes Harvard EELP, Federal Register, EPA press releases, Earthjustice, NRDC, EDF, and Regulations.gov.

**Harvard Environmental and Energy Law Program (EELP) Regulatory Tracker**: The gold standard for expert-verified rule summaries. The tracker's methodology mirrors EELP's framework. Current lag from Federal Register publication to EELP update: 3–7 days for major rules, longer for lower-profile actions. EELP is comprehensive for formal rules but does not systematically cover enforcement data (what violations are NOT being prosecuted).

**Federal Register (federalregister.gov)**: The primary official source. Checked manually — no automated ingestion. The Federal Register publishes at 8:45 AM ET daily; each issue contains EPA and other environmental agency documents. Currently browsed reactively rather than polled.

**Earthjustice, NRDC, EDF press releases**: Advocacy organizations that reliably signal litigation responses to rollbacks. All monitored via email subscriptions; lag varies by organization's publication cadence.

**EPA official press releases**: Monitored via EPA newsroom. The current administration's EPA frames rollbacks as "regulatory reform" and "burden reduction" — editorial filtering is required. Value: announces the administration's own characterization of actions, which is itself analytically important.

**Regulations.gov docket monitoring**: Occasionally checked for comment period deadlines. Not systematically ingested.

### 2.2 Freshness Assessment

**Strongest area**: Federal Register formal rules. The tracker is current within 1–7 days for finalized rules. The April 27 and May 5 updates demonstrate that formal rule publication triggers timely tracker entries.

**Weakest area**: Agency guidance and enforcement. The Endangerment Finding entry documents that formal rescission became effective April 20, 2026, but the enforcement implications — what EPA is actually doing or not doing under the rescinded authority — lag significantly behind. EPA enforcement action data requires direct database access, not press release monitoring.

**Lag patterns by action type**:
- Final rules in Federal Register: 1–7 days (best performance)
- Proposed rules (NPRM stage): 3–14 days (important to catch early: comment periods create advocacy windows)
- Agency enforcement data: 2–8 weeks, if captured at all
- Interior/BLM/FWS non-rulemaking actions (drilling approvals, EIS decisions): 7–21 days or not captured
- State environmental rollbacks: Not captured

### 2.3 Bias Audit

**Overrepresented**: EPA formal rulemaking; clean air and climate issues; litigation by large national environmental groups. The entries for greenhouse gas, MATS, PM2.5, WOTUS, and vehicle emissions standards are thorough. This reflects both the political prominence of these issues and the fact that the listed source organizations prioritize them.

**Underrepresented**:
- Chemical safety and Toxic Substances Control Act (TSCA) actions — entirely absent despite significant rollbacks in industrial chemicals
- Interior Department non-rulemaking actions (BLM lease approvals, monument revocations administered under existing authority without new rulemaking)
- EPA enforcement data (violations not prosecuted, fines not levied) — this is arguably as important as formal deregulation but requires enforcement database access
- State environmental rollbacks in Texas, Wyoming, Louisiana, and Florida, where state-level preemption of local environmental rules is ongoing
- Small regulatory changes (guidance memos, compliance deadline extensions) that collectively matter but individually fall below the national news threshold

**Source independence**: All current sources (Earthjustice, NRDC, EDF, CATF) are advocacy organizations with strong positions on the issues tracked. This does not make them inaccurate — their factual assertions are generally verifiable — but creates a perspective gap. The tracker would benefit from including industry-side monitoring (American Petroleum Institute comment letters, American Chemistry Council docket filings) not to endorse their positions but to understand what regulatory relief they are obtaining.

### 2.4 Coverage Gap Analysis

**Gap 1 — Enforcement data**: The single largest coverage gap. The tracker documents what rules have been formally repealed or weakened. It does not document what violations are not being pursued under still-existing rules. EPA's civil and criminal enforcement data is published in the ECHO (Enforcement and Compliance History Online) database. Q1 2026 data cited in tracker entry 12 (Section I, entry 12) was sourced from EHSLeaders, a trade publication — not from ECHO directly. Direct ECHO API access would provide near-real-time enforcement collapse data.

**Gap 2 — TSCA and chemical safety**: The Toxic Substances Control Act regulates industrial chemicals with demonstrated health hazards. Under the current administration, TSCA risk evaluations have been paused or weakened for multiple substances (asbestos, TCE, PCE). None of the current entries cover TSCA. Relevant sources: TSCA docket on Regulations.gov, EPA Chemical Safety Office newsroom.

**Gap 3 — Interior Department non-rulemaking**: BLM lease approvals, ESA critical habitat changes, and monument boundary adjustments are executed under existing administrative authority without new rulemaking. They do not appear in the Federal Register as proposed or final rules. Interior Department press releases and BLM decision records are the primary signals.

**Gap 4 — State environmental preemption**: Several states have enacted laws preempting local environmental ordinances (plastic bag bans, local fracking moratoria, green building codes). These are not federal rollbacks but collectively reduce the regulatory floor. State environmental agency dockets are the primary signal.

**Gap 5 — Comment period advocacy windows**: The tracker documents rules after they finalize. For advocacy purposes, the critical intervention point is during the notice-and-comment period, when public comments can (in theory) affect the final rule and when the rule is most vulnerable to procedural challenge. Regulations.gov monitoring would add this earlier-warning layer.

### 2.5 Recommended New Sources

**Source 1: Federal Register API — Automated Environmental Agency Monitoring**
- **What it adds**: Daily automated polling of all EPA, Interior (BLM, FWS, NPS), NOAA, DOE, USDA rulemaking. Replaces manual Federal Register browsing with a structured feed.
- **API endpoint**: `https://www.federalregister.gov/api/v1/documents.json?conditions[agencies][]=environmental-protection-agency&conditions[type]=RULE,PRORULE,NOTICE&per_page=20`
- **Coverage**: 295 EPA documents published in 2026 as of May 1 — this is the documented volume to handle.
- **Freshness**: Same-day. Federal Register publishes at 8:45 AM ET; API reflects same-day publication.
- **Cost**: Free. No key required.
- **Feasibility**: Immediate. 15 lines of Python + daily cron job. This should be the first implementation step for this tracker.
- **Additional agencies**: Add `interior-department`, `fish-and-wildlife-service`, `bureau-land-management`, `energy-department` as separate agency filters.

**Source 2: EPA ECHO (Enforcement and Compliance History Online) API**
- **What it adds**: Enforcement and compliance data for regulated facilities. Tracks civil penalties assessed, inspection rates, violations documented but not prosecuted. This is the gap between formal rules (what the law says) and enforcement reality (what agencies actually do).
- **API**: EPA ECHO RESTful API at `https://echo.epa.gov/tools/web-services`. Key endpoints: `https://echodata.epa.gov/echo/cwa_rest_services.get_facility_info` (Clean Water Act); `https://echodata.epa.gov/echo/air_rest_services.get_facility_info` (Clean Air Act).
- **Freshness**: Quarterly data releases; not real-time. Enforcement inspection data typically lags reality by 60–90 days due to reporting cycles.
- **Cost**: Free. Government public data.
- **Feasibility**: Medium. The ECHO API requires facility-level queries rather than national aggregate queries; building a national enforcement summary requires aggregation logic. Realistic implementation time: 8–12 hours for initial setup; quarterly maintenance thereafter.
- **Realistic expectation**: This source enables quarterly enforcement audit entries (e.g., "EPA issued 34% fewer penalties in Q1 2026 than Q1 2025 for Clean Air Act violations") rather than real-time alerts.

**Source 3: Regulations.gov API v4 — Comment Period Calendar**
- **What it adds**: Tracks all open and upcoming comment periods for environmental rules. Comment periods are the advocacy intervention window — when organized public comment can affect final rules or create an administrative record for later litigation.
- **API**: `https://api.regulations.gov/v4/documents?filter[agencyId]=EPA&filter[documentType]=Proposed%20Rule&api_key=DEMO_KEY`
- **Note**: As documented in `tracker-data-source-audit.md`, the POST API (for submitting comments) was restricted to federal agencies in August 2025. The GET/read API for monitoring dockets remains fully publicly available.
- **Freshness**: Daily updates as agencies post new documents.
- **Cost**: Free with API key (free registration at api.data.gov).
- **Feasibility**: Low effort for the monitoring use case; more effort if the tracker also wants to export comment deadlines to a calendar for user advocacy.

**Source 4: Environmental Data and Governance Initiative (EDGI) — Agency Monitoring**
- **What it adds**: EDGI systematically monitors EPA and Interior Department websites for content removal, scientific data deletion, and policy page changes. Their reports document the "invisible" rollback — when the administration simply removes scientific information from public-facing websites rather than formally revoking a rule.
- **Access**: EDGI publishes reports at envirodatagov.org and maintains a public GitHub repository of website change detection data.
- **Freshness**: Reports released approximately monthly; GitHub repository updates as detected.
- **Cost**: Free.
- **Feasibility**: Low effort to monitor EDGI reports via RSS. Higher effort to integrate their raw website-change data.
- **Unique value**: This source covers a category of rollback (data erasure, scientific content removal) that is not captured by any other source on this list. It is specifically designed to monitor the current administration's practice of removing scientific data without formal rulemaking.

**Source 5: State Environmental Agency Docket Feeds — Texas, Wyoming, Louisiana**
- **What it adds**: State-level environmental rollbacks from the three states most active in opposing federal environmental regulation and implementing their own deregulatory agendas.
- **Access**: Texas Commission on Environmental Quality (TCEQ) rulemaking page; Wyoming Department of Environmental Quality (WDEQ) rulemaking notices; Louisiana Department of Environmental Quality (LDEQ) notices. All publish RSS feeds or structured HTML pages.
- **Freshness**: Published on state administrative record timelines (varies: same-day to 1 week after agency action).
- **Cost**: Free.
- **Feasibility**: Low for RSS monitoring; medium for structured data extraction.
- **Coverage gap filled**: The three states account for a disproportionate share of oil/gas production and industrial emissions. State rollbacks in these states often precede or supplement federal deregulation.

**Source 6 (bonus): Earthjustice Active Cases RSS (earthjustice.org/rss.xml)**
- **What it adds**: All active Earthjustice litigation, updated within 24 hours of filings or decisions. Already partially used (through press releases), but the RSS feed provides structured, automated coverage of all cases including smaller ones that do not generate press releases.
- **Cost**: Free.
- **Feasibility**: 10 minutes — RSS subscription.

### 2.6 Source Feasibility Summary Table

| Source | Automated Ingestion | Update Frequency | Cost | Implementation Effort | Priority |
|--------|---------------------|------------------|------|-----------------------|----------|
| Federal Register API | Yes — REST API | Daily (8:45 AM) | Free | 2 hours | **1** |
| Earthjustice RSS | Yes — RSS | Daily | Free | 10 minutes | **2** |
| Regulations.gov API v4 | Yes — REST API | Daily | Free (API key) | 3–4 hours | **3** |
| EDGI monitoring | Semi-automated | Monthly reports | Free | 2 hours setup | **4** |
| EPA ECHO API | Yes — REST API | Quarterly | Free | 8–12 hours | **5** |
| State agency RSS (TX, WY, LA) | Yes — RSS/scrape | Weekly | Free | 4–6 hours | **6** |

---

## Section 3: Police Brutality / Consent Decree Tracker

### 3.1 Current Sources

The `police-brutality-consent-decree-tracker.md` draws from a combination of DOJ press releases, ACLU case pages, ProPublica investigations, local news monitoring, and major national outlets (NPR, CNN, NYT).

**DOJ press releases (justice.gov/news)**: Primary signal for federal prosecution announcements and official DOJ civil rights actions. Critical limitation: the current DOJ only publicizes cases it wants publicized. Civil rights prosecutions of officers are now rare (down 36% in 2025 to 54 cases, documented in the tracker). Monitoring what DOJ announces tells you what the administration is doing; it does not tell you what it is not doing.

**ACLU national case pages**: Reliable for active federal civil rights litigation. Lag: 1–7 days from filing to page update. Structural gap: ACLU state affiliates operate semi-independently; a case handled by ACLU of Louisiana may not appear on the national ACLU website for weeks.

**ProPublica investigative pieces**: High quality but irregular publication. ProPublica's "Injustice on Your Block" database (police use-of-force settlements) is directly relevant but not currently systematically monitored.

**Local news monitoring**: The tracker explicitly identifies this as its most significant gap. The May 21, 2025 DOJ withdrawal actions affected cities including Phoenix, Trenton, Memphis, Mount Vernon, Oklahoma City, and Louisiana State Police. Coverage of those cities' responses to losing federal oversight requires local news monitoring — Phoenix New Times, Commercial Appeal (Memphis), NJ.com — that is not systematically in place.

**NPR, CNN, New York Times**: Reliable for high-profile incidents and national consent decree news. Not reliable for anything below the threshold of national significance.

### 3.2 Freshness Assessment

**Best performance**: High-profile police killings with national coverage (added within 24–48 hours); major court rulings in tracked cases (added within 48 hours if case is already on the tracker). The Pattern 6 entry (10th Circuit Denver ruling, circuit split on protest policing) demonstrates that case-following produces timely updates.

**Worst performance**: City-level consent decree monitoring reports from independent monitors (these are public documents filed with federal courts but are not newsworthy in themselves — they only surface if an advocacy organization highlights them). The Chicago monitoring team's April 14, 2026 report (compliance at 25%) was captured, but this was because the tracker was actively tracking Chicago. A city like Phoenix — where DOJ closed its investigation — has no systematic monitoring.

**Key lag pattern**: Consent decree compliance reports are filed with courts quarterly or semi-annually. These are primary source documents that update the tracker's accuracy significantly but require actively monitoring federal court dockets for the relevant cases. Currently this requires manual PACER access; it should be automated.

### 3.3 Bias Audit

**Geographic bias**: Extraordinary coverage of Chicago (most detailed entries), Seattle, Baltimore, Los Angeles, and Minneapolis — cities where major national news events occurred. Systematic undercoverage of medium-sized cities with active consent decree dynamics: Albuquerque, Louisville (whose proposed decree was dismissed May 21, 2025), Cleveland (whose exit motion was pending as of late April 2026), and Newark (one of the first consent decrees entered and potentially first completed).

**Institutional bias**: Heavy reliance on DOJ as a source produces a fundamental problem in 2026: the institution responsible for oversight has withdrawn from that function. The tracker's lead finding documents this explicitly. But the source set has not fully adapted to the post-DOJ-enforcement world — it still monitors justice.gov/news as a primary source even though DOJ now generates mostly absence-of-action signals.

**Missing actor: state AGs**: As federal DOJ withdrew, state attorneys general in California, New York, Massachusetts, Minnesota, Illinois, and Washington have partially assumed the pattern-or-practice enforcement function. The tracker captures state-level cases when they generate national news (California AG actions sometimes do) but does not systematically monitor state AG press releases or litigation dockets.

**Missing actor: independent monitors**: The actual compliance data comes from independent monitors appointed by courts (not DOJ) to assess compliance in cities with active consent decrees. These monitors file reports with courts on regular schedules. The reports are public documents filed in PACER but are rarely covered by news outlets unless compliance deteriorates dramatically. Monitoring these reports directly — rather than waiting for news coverage — would provide earlier and more accurate compliance data.

### 3.4 Coverage Gap Analysis

**Gap 1 — Independent monitor reports**: The most significant data quality gap. Monitor reports are filed quarterly or semi-annually in PACER as part of the consent decree docket. For Chicago, the monitor files at `ILND 1:17-cv-06260` (the AG decree case). For Seattle, at `WD WA 2:12-cv-01282`. Monitoring these dockets via CourtListener would produce automated alerts when new monitor reports are filed, without requiring news coverage.

**Gap 2 — ICE use-of-force incidents**: The tracker acknowledges this gap explicitly ("ICE use-of-force incidents (increasingly relevant post-2025) are not systematically included"). ICE is not subject to local consent decrees, but patterns of force during immigration enforcement are documented by immigrant rights organizations. American Immigration Lawyers Association (AILA), Immigrant Legal Resource Center (ILRC), and state-level detention monitoring groups (e.g., NYU Immigrant Rights Clinic, UCLA Immigrant Family Legal Clinic) document these incidents. This is a crossover issue between this tracker and the `consent-decree-defiance-tracker.md`.

**Gap 3 — Settlement database**: ProPublica's "Injustice on Your Block" database documents police misconduct settlements paid by cities. This quantifies the financial cost of non-compliance with consent decrees in a way that is politically persuasive but is not currently integrated. The database covers settlements nationwide and updates as new settlements are reported.

**Gap 4 — Exit motion litigation**: The tracker notes that Cleveland's exit motion is pending as of late April 2026. When a police department seeks to exit a consent decree, the litigation itself is a tracker-relevant event. Monitoring CourtListener for consent-decree-related motions in tracked cities would catch these.

**Gap 5 — State AG pattern-or-practice investigations**: As documented in the lead finding, the May 21, 2025 DOJ withdrawal created a vacuum. State AGs have partially filled it with their own investigations. These state-level actions have different legal authority and timeline but represent the primary remaining federal accountability mechanism. None of the current source monitoring captures state AG investigation announcements systematically.

### 3.5 Recommended New Sources

**Source 1: CourtListener RECAP API — Consent Decree Docket Monitoring**
- **What it adds**: Automated monitoring of federal court dockets for active consent decree cases. When a monitor files a new compliance report, when a city files an exit motion, or when a court issues a ruling, RECAP captures it within hours.
- **Implementation**: Maintain a list of active consent decree docket numbers (Chicago: ILND 1:17-cv-06260; Seattle: WD WA 2:12-cv-01282; Louisville: KY Western District etc.) and poll each for new filings using the CourtListener docket endpoint.
- **API**: `GET /api/rest/v4/dockets/{docket_id}/docket_entries/?order_by=-date_filed`
- **Freshness**: 1–24 hours from filing.
- **Cost**: Free. Rate limit note: CourtListener is transitioning to a membership model as of April 2026; current free access may become tiered. Monitor this.
- **Feasibility**: Low-medium. Requires maintaining the docket-number list manually as new decrees are entered or terminated.

**Source 2: Mapping Police Violence Database (mappingpoliceviolence.org)**
- **What it adds**: The most comprehensive national database of police killings, updated within 24–48 hours of incidents. Available as a public Airtable base with read API access. Provides geographic, demographic, and circumstances data that the current tracker lacks for individual incidents.
- **Access**: Public Airtable base at `https://airtable.com/appzVzSeINK1S3EVR`. Airtable read API for public bases requires an API token but is free.
- **Freshness**: 24–48 hours.
- **Cost**: Free.
- **Feasibility**: Low effort for API access; medium effort to integrate into tracker narrative (raw incident data needs contextual filtering).

**Source 3: State Attorney General RSS Feeds — Pattern-or-Practice Coverage**
- **What it adds**: Direct monitoring of state AG press releases for pattern-or-practice investigations, consent decree negotiations, and civil rights enforcement actions. Fills the post-DOJ-withdrawal enforcement gap.
- **States to monitor**: California OAG (oag.ca.gov/rss), New York AG (ag.ny.gov/press-releases RSS), Massachusetts AG (mass.gov/ag), Minnesota AG (ag.state.mn.us), Illinois AG (illinoisattorneygeneral.gov), Washington AG (atg.wa.gov).
- **Freshness**: Same-day for press releases.
- **Cost**: Free.
- **Feasibility**: Lowest effort. RSS subscriptions in any aggregator.

**Source 4: ProPublica Injustice on Your Block Database**
- **What it adds**: Police misconduct settlement database covering settlements paid by U.S. cities and counties. Allows the tracker to quantify the financial cost of non-compliance (e.g., "Chicago paid $X million in settlements in 2025 while only at 25% consent decree compliance").
- **Access**: ProPublica's database is accessible at projects.propublica.org/injustice. CSV download available.
- **Freshness**: Updated as ProPublica adds new records; not real-time (reporting takes time). Quarterly updates are a reasonable expectation.
- **Cost**: Free.
- **Feasibility**: Medium. Requires matching ProPublica's city/department identifiers to tracker entries.

**Source 5: Law Enforcement Knowledge Lab Federal Interventions Dashboard**
- **What it adds**: The LEKL Federal Interventions Dashboard tracks all active and terminated DOJ Civil Consent Decrees and Settlement Agreements. Provides a structured list of all currently active decrees with status, monitoring status, and case document links — filling the "which cities currently have active decrees" gap.
- **Access**: `https://leknowledgelab.org/resources/federal-interventions-dashboard/`. No formal API; change-detection monitoring appropriate.
- **Freshness**: Updated as cases change status; lag varies.
- **Cost**: Free.
- **Feasibility**: Change-detection monitoring (Changedetection.io or similar): $5–15/month.

**Source 6 (bonus): DOJ Civil Rights Division Press Release RSS**
- **What it adds**: Direct feed of Civil Rights Division announcements — new investigations opened, findings letters issued, settlements reached. Currently the DOJ CRT is not opening new pattern-or-practice investigations, but this feed would immediately detect if that changes.
- **Access**: `https://www.justice.gov/crt/civil-rights-news-releases` — DOJ maintains an RSS feed for Civil Rights Division news.
- **Freshness**: Same-day.
- **Cost**: Free.
- **Feasibility**: Immediate.

### 3.6 Source Feasibility Summary Table

| Source | Automated Ingestion | Update Frequency | Cost | Implementation Effort | Priority |
|--------|---------------------|------------------|------|-----------------------|----------|
| State AG RSS feeds | Yes — RSS | Daily | Free | 1 hour | **1** |
| DOJ Civil Rights RSS | Yes — RSS | Daily | Free | 30 minutes | **2** |
| CourtListener RECAP (docket monitoring) | Yes — REST API | 1–24 hours | Free* | 4–6 hours | **3** |
| Mapping Police Violence (Airtable) | Yes — Airtable API | 24–48 hours | Free | 3–4 hours | **4** |
| LEKL Dashboard | Change-detection | Variable | $5–15/mo | 1 hour | **5** |
| ProPublica Settlements DB | Manual quarterly | Quarterly | Free | 2 hours/quarter | **6** |

*Rate limit transition in progress; monitor CourtListener's membership policy.

---

## Section 4: Prosecutorial Weaponization Tracker

### 4.1 Current Sources

The prosecutorial weaponization tracker presents a different challenge than the other three: as of May 2026, there is no dedicated `prosecutorial-weaponization-tracker.md` file. Coverage is distributed across `first-amendment-suppression.md` (Section 7, the SPLC indictment) and `domains/domain-29-prosecutorial-weaponization-and-doj-capture.md`, with fragmentary references in `litigation-tracker-2026.md`.

This is the most significant structural gap in the tracker ecosystem: the content exists in the form of deep analysis documents, but there is no centralized tracking file formatted for distributable reference use (like the other three trackers) with consistent entry structure, current status fields, and regular update cadence.

**Current ad-hoc sources for the distributed content**:

**Major national news (NYT, WaPo, Reuters, NPR)**: Catches high-profile indictments (SPLC, Nashville prosecutor's ruling) but misses lower-profile USAO press releases about politically connected defendants. Out of 94 U.S. Attorneys' offices, only a handful of prosecutions receive national coverage.

**Just Security (justsecurity.org)**: Provides expert legal analysis of Trump DOJ pattern. Has published the most analytically rigorous coverage of the SPLC indictment (Weissmann's analysis, Zelinsky on bank fraud counts). Not a systematic data source — publishes analysis when major cases occur.

**Protect Democracy Retaliatory Action Tracker (protectdemocracy.org)**: A structured tracker of Trump administration investigations and prosecutions that appear retaliatory or politically motivated. Currently checked manually and inconsistently. This is the single most important source to bring into systematic monitoring for this tracker.

**SPLC monitoring (post-April 21, 2026)**: Following the SPLC's own indictment, their communications and litigation updates are now monitored. Previously not a source at all.

**Freshness assessment**: No systematic monitoring. Estimated 50–70% of politically relevant prosecutions are currently missed entirely. Events surface when they receive national media coverage. The domain-29 analysis documents 22 tracked cases, but the sourcing methodology for those cases was ad hoc retrospective research, not prospective monitoring.

### 4.2 Bias Audit

**Directional bias**: The current coverage skews heavily toward cases where the prosecution appears politically motivated against progressive or Democratic-aligned targets. There is no equivalent monitoring of cases where federal prosecutors have been pressured to NOT prosecute politically connected individuals (nolle prosequi decisions, cases dropped, investigations closed). Both the decision to prosecute and the decision not to prosecute are evidence of weaponization; the current source set captures only one direction.

**Geographic bias**: Cases in the DC circuit and high-profile federal districts (SDNY, NDCA) dominate. Red-state federal districts (SD Alabama, ED Texas, WD Louisiana) are where the administration has the most compliant U.S. Attorneys and where politically targeted prosecutions of progressive organizations are most likely. These districts receive the least national news coverage.

**Legal theory bias**: The SPLC case generated extensive coverage because its legal theory was facially implausible and drew immediate expert condemnation. Prosecutions with more facially valid legal theories — even if the targeting is politically motivated — are harder to identify as weaponization and receive less coverage.

**Systemic vs. individual bias**: The domain-29 analysis correctly identifies systemic patterns (22 cases with common structural elements). But that systemic view was built through retrospective research, not prospective monitoring. Prospective monitoring will initially produce individual cases that must be assessed for whether they fit the pattern.

### 4.3 Coverage Gap Analysis

**Gap 1 — USAO press releases across 94 districts**: The DOJ's primary public announcement mechanism for new prosecutions is U.S. Attorney press releases. There is no current systematic monitoring of these. The DOJ publishes an RSS feed for all USAO press releases (`https://www.justice.gov/usao/pressreleases`) but it produces hundreds of releases weekly; without keyword filtering for politically relevant cases, the volume is unmanageable. Filtered monitoring is the key implementation challenge.

**Gap 2 — Vindictive prosecution judicial findings**: Federal courts occasionally issue rulings finding that a prosecution was vindictively motivated (the Nashville ruling documented in domain-29 is the paradigmatic example). These rulings are filed in PACER and occasionally generate national coverage, but systematic monitoring of federal criminal dockets for motions to dismiss on vindictive prosecution grounds is not in place.

**Gap 3 — Non-prosecution data**: As noted in the bias audit, the decision not to prosecute is evidence of weaponization in the other direction — protecting allies. DOGE-related financial misconduct, January 6 defendant pardons, dismissal of civil rights cases against police officers. These are not captured by prosecution monitoring.

**Gap 4 — Civil society targeting beyond prosecution**: Prosecutorial weaponization is broader than criminal indictments. It includes: IRS audit targeting of political opponents (requires IRS data access, legally constrained), SEC enforcement actions against progressive donors, FTC and DOJ antitrust cases with political dimensions, and civil enforcement actions by federal agencies. Domain-29 analysis documents some of these but the tracker scope needs to be defined before building a source architecture.

**Gap 5 — State-level prosecutorial weaponization**: Federal focus misses state-level political prosecution patterns. Texas AG Ken Paxton's prosecutorial conduct (documented in multiple cases) and similar state AG behavior is relevant to the broader pattern. State court filings require PACER alternatives — state-specific court records systems.

### 4.4 Recommended New Sources

**Source 1: DOJ All USAO Press Releases RSS (justice.gov/usao/rss)**
- **What it adds**: The primary official signal for all new federal prosecutions across 94 districts. When DOJ announces a high-profile prosecution — or even a lower-profile one with political dimensions — the USAO press release comes first.
- **Implementation challenge**: Volume (hundreds per week). Requires keyword filtering for politically relevant cases: names of known targets, civil society organization names, categories like "nonprofit fraud," "election interference," "protest organizer," "civil rights attorney." This filtering must evolve as new targets emerge.
- **Freshness**: Same-day as charging announcement.
- **Cost**: Free.
- **Feasibility**: Medium. RSS ingestion is easy; keyword filtering is the ongoing maintenance burden.

**Source 2: Protect Democracy Retaliatory Action Tracker (protectdemocracy.org/work/retaliatory-action-tracker/)**
- **What it adds**: Expert-curated, structured tracker applying a consistent three-question test to identify politically retaliatory federal actions. This is the closest thing to a pre-built source for exactly this tracker's purpose.
- **Access**: No API. Change-detection monitoring (Changedetection.io or Distill.io) alerts when the page updates. The page structure is consistent enough for parsing.
- **Freshness**: 2–5 day lag from public announcement to Protect Democracy documentation.
- **Cost**: Free to monitor; $5–15/month for change-detection service.
- **Feasibility**: Low for change-detection monitoring; medium for structured data extraction.
- **Priority**: Highest single source for this tracker. Implement this first.

**Source 3: CourtListener RECAP — Vindictive/Selective Prosecution Motions**
- **What it adds**: Federal criminal dockets mentioning motions to dismiss on vindictive or selective prosecution grounds. These motions are filed by defense attorneys when they have evidence that the prosecution was politically motivated. They are filed in PACER and occasionally generate press coverage; systematic monitoring catches them earlier.
- **Query**: `GET /api/rest/v4/dockets/?q="vindictive+prosecution"&type=r` (RECAP documents mentioning "vindictive prosecution")
- **Freshness**: 1–24 hours from filing.
- **Cost**: Free.
- **Feasibility**: Low effort for the query; medium effort to assess relevance of hits (not all vindictive prosecution motions are politically relevant).

**Source 4: Wikipedia Revision Feed — Political Targeting Article**
- **What it adds**: The Wikipedia page "Targeting of political opponents and civil society under the second Trump administration" is actively maintained by community editors and provides a crowd-sourced index of targeted individuals and organizations. Its revision history timestamps when new targets are documented. This acts as a secondary completeness check: if a case appears on Wikipedia before appearing in the tracker, the tracker missed it.
- **API**: `GET https://en.wikipedia.org/api/rest_v1/page/summary/Targeting_of_political_opponents_and_civil_society_under_the_second_Trump_administration`
- **Revision history**: `https://en.wikipedia.org/w/api.php?action=query&titles=Targeting_of_political_opponents_and_civil_society_under_the_second_Trump_administration&prop=revisions&rvprop=timestamp|comment`
- **Cost**: Free.
- **Feasibility**: Low. Wikipedia API is the easiest integration on this list.
- **Note**: Wikipedia is a secondary source and a completeness check, not a primary source. Every entry it surfaces needs primary-source verification before tracker inclusion.

**Source 5: Just Security RSS (justsecurity.org/feed)**
- **What it adds**: Expert legal analysis of prosecutorial weaponization cases as they develop. Just Security has been the fastest and most analytically rigorous outlet for major cases (SPLC, Nashville, Lori Lightfoot investigation). Their analysis often surfaces legal theory issues (bank fraud *Thompson* contradiction in the SPLC case) that are not in news coverage.
- **Access**: RSS feed at `https://www.justsecurity.org/feed/`.
- **Freshness**: Published within hours of major case developments.
- **Cost**: Free.
- **Feasibility**: Immediate — RSS subscription.

**Source 6 (bonus): PACER Case Locator API — Named-Target Monitoring**
- **What it adds**: Proactive monitoring for when specific named individuals or organizations become defendants in federal cases. For a maintained watchlist of people at risk of retaliatory prosecution (Democratic officials, civil rights organization leadership, prominent critics of the administration), PCL can detect federal case filings.
- **API**: PCL REST API at `https://pcl.uscourts.gov/pcl/pages/search/find.jsf`. Authentication required (PACER account, free to register). Case queries are free; document access is $0.10/page.
- **Feasibility**: Medium. Requires maintaining the watchlist of names. The PACER case locator has batch job limitations that affect real-time monitoring.

### 4.5 Source Feasibility Summary Table

| Source | Automated Ingestion | Update Frequency | Cost | Implementation Effort | Priority |
|--------|---------------------|------------------|------|-----------------------|----------|
| DOJ USAO RSS | Yes — RSS + filtering | Daily | Free | 3–4 hours (filtering) | **1** |
| Protect Democracy Tracker | Change-detection | 2–5 days lag | $5–15/mo | 2 hours | **2** |
| Just Security RSS | Yes — RSS | Daily | Free | 10 minutes | **3** |
| Wikipedia revision feed | Yes — API | Daily | Free | 1 hour | **4** |
| CourtListener (vindictive prosecution) | Yes — REST API | 1–24 hours | Free | 3 hours | **5** |
| PACER Case Locator | Semi-automated | Variable | Free (search) | 4–6 hours | **6** |

---

## Cross-Tracker Summary: Implementation Priority Order

Ranked by combined impact (coverage gap filled × implementation cost):

| Priority | Source | Trackers | Effort | Cost |
|----------|--------|----------|--------|------|
| 1 | Press Freedom Tracker API | FA | 2 hours | Free |
| 2 | Federal Register API | ENV | 2 hours | Free |
| 3 | EFF Deeplinks RSS | FA | 30 minutes | Free |
| 4 | FIRE Newsdesk RSS | FA | 30 minutes | Free |
| 5 | Just Security RSS | PW | 10 minutes | Free |
| 6 | DOJ USAO RSS | PW | 3–4 hours | Free |
| 7 | Earthjustice RSS | ENV | 10 minutes | Free |
| 8 | State AG RSS (6 states) | PB | 1 hour | Free |
| 9 | DOJ Civil Rights RSS | PB | 30 minutes | Free |
| 10 | Regulations.gov API v4 | ENV | 3–4 hours | Free |
| 11 | Protect Democracy change-detection | PW | 2 hours | $5–15/mo |
| 12 | CourtListener RECAP (docket) | PB, PW | 4–6 hours | Free* |
| 13 | Mapping Police Violence (Airtable) | PB | 3–4 hours | Free |
| 14 | LegiScan API | FA | 4–6 hours | Free |
| 15 | EPA ECHO API | ENV | 8–12 hours | Free |

Total Wave 1 (items 1–10): approximately 15 hours of implementation work, $0 ongoing cost. Wave 2 (items 11–15): approximately 20 additional hours, $5–15/month ongoing.

FA = First Amendment, ENV = Environmental, PB = Police Brutality, PW = Prosecutorial Weaponization.

---

*Sources consulted: [CourtListener API documentation](https://www.courtlistener.com/help/api/) | [Press Freedom Tracker API](https://pressfreedomtracker.us/data/) | [Federal Register API](https://www.federalregister.gov/developers/documentation/api/v1) | [Regulations.gov API](https://open.gsa.gov/api/regulationsgov/) | [EPA ECHO](https://echo.epa.gov/tools/web-services) | [LegiScan API](https://legiscan.com/legiscan-api) | [Protect Democracy Tracker](https://protectdemocracy.org/work/retaliatory-action-tracker/) | [EDGI](https://envirodatagov.org) | [Lumen Database](https://lumendatabase.org) | [FIRE](https://thefire.org) | [PACER PCL API](https://pacer.uscourts.gov/help/pacer/pacer-case-locator-pcl-api-user-guide) | [Mapping Police Violence](https://mappingpoliceviolence.org) | [Harvard EELP](https://eelp.law.harvard.edu/tracker-type/regulatory-tracker/)*
