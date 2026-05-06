---
title: "Phase 2 Litigation Tracking System: Impact Measurement and Institutional Adoption Infrastructure"
created: "2026-05-06"
revised: "2026-05-06"
status: design-complete
phase: Phase 2 (post-launch operationalization)
distribution_status: "Independent of Path A / A+37 / B decision — ready for Day 1 activation"
cross_references:
  - measurement-and-iteration-framework.md
  - litigation-tracker-2026.md
  - domains/domain-37-baseline-metrics.md
  - phase-1-execution-checklist.md
  - PROJECTS.md
---

# Phase 2 Litigation Tracking System

**Design completed**: May 6, 2026. **Operational trigger**: Path decision (any path) + Batch 1 emails sent.

**Purpose**: This document specifies the complete infrastructure for measuring what happens after the 35-domain framework reaches Tier 1–3 recipients. The core measurement problem in policy dissemination is that the most consequential adoptions — a Senate Judiciary Committee staffer incorporating analysis into hearing prep; a district court brief citing comparative constitutional evidence; a law school clinic folding domain research into a student-litigated case — leave no public footprint for weeks or months. A tracking system that only captures public signals will systematically undercount impact at exactly the institutional level where it matters most. This design balances passive monitoring (free, continuous, objective) with active contact intelligence (expensive, intermittent, irreplaceable) and provides the infrastructure to make attribution claims that can withstand scrutiny.

**Path independence**: This system activates on the day Batch 1 emails are sent. The Airtable configuration differs only in the initial contact list import. The measurement architecture is identical across Path A, A+37, and B.

**What this system does not attempt**: Real-time case outcome attribution. Courts rule on evidence in the record, not on external policy frameworks. When a district court cites a comparative constitutional argument, that citation will appear in the opinion. When a congressional staffer incorporates domain language into a bill draft, it usually will not. The attribution decision tree in Part 3 handles that asymmetry honestly.

---

## Part 1: Data Sources

### 1.1 PACER and Federal Court Document Monitoring

PACER (Public Access to Court Electronic Records) is the authoritative source for federal docket data but is not designed for monitoring at scale. The practical implementation uses a two-tier approach: CourtListener for alert coverage, PACER for document retrieval on specific events.

**CourtListener as the primary alert layer** (courtlistener.com): The Free Law Project's CourtListener mirrors PACER metadata for appellate courts and most district courts, provides a REST API documented at courtlistener.com/help/api/, and supports case-level email alerts without per-page charges. Set up CourtListener alerts for all 38+ active cases in `litigation-tracker-2026.md`. Each alert fires when a new docket entry appears for that case — orders, opinions, motions, amicus filings.

**What to track via CourtListener/PACER**:

- Orders and rulings in all tracked cases (immigration enforcement, consent decree enforcement, First Amendment, electoral challenges, executive power)
- Amicus curiae filings — these are the most direct signal that organizational recipients of the framework are mobilizing legal argument; a Brennan Center amicus in a Domain 6 judicial independence case, filed 45 days after receiving the framework, is a high-confidence adoption signal
- New complaints filed in the same case categories, to detect emerging litigation patterns the tracker does not yet cover
- TRO and preliminary injunction motions in new cases matching tracked domain areas

**PACER API specifics**: api.pacer.gov provides REST endpoints for case and docket data. Authentication requires a PACER account with API access enabled. Billing is $0.10 per page for document retrieval, but PACER waives fees for users whose quarterly charges do not exceed $30. At $0.10/page, that is 300 pages before billing begins. Targeted retrieval of orders and amicus filings for 50–80 active cases stays well within this threshold. Do not retrieve full complaint text for every new filing — retrieve only orders, injunction rulings, and amicus briefs.

**Domain-to-search-term mapping for new case discovery**:

| Domain range | Primary search terms | Secondary terms |
|---|---|---|
| Domains 1–3 (electoral, redistricting, campaign finance) | election, voting rights, voter registration, redistricting | HAVA, VRA, Section 2, NVRA |
| Domain 6 (judicial independence) | judicial removal, court structure, jurisdiction stripping | Article III, good behavior |
| Domain 14 (criminal justice) | Section 1983, consent decree, police accountability | Monell, pattern and practice |
| Domains 18–19 (immigration enforcement) | warrantless arrest, ICE, habeas corpus, immigration detention | 8 U.S.C., Fourth Amendment, flight risk |
| Domains 27–28 (academic freedom, war powers) | First Amendment, academic freedom, War Powers Resolution | WPR, 50 U.S.C. 1541 |
| Domain 29 (prosecutorial weaponization) | vindictive prosecution, DOJ, selective prosecution | 18 U.S.C. 242, retaliatory indictment |
| Domain 37 (election interference) | voter roll, SAVE, election security, CISA | EAC, Help America Vote, state election administration |

**PACER search limitations**: PACER full-text search is not available for all courts or all document types. The search function searches case names and docket titles, not document content. For content-level search (e.g., finding briefs that use specific analytical vocabulary from the framework), Google Scholar is more effective than PACER.

---

### 1.2 Google Scholar Citation Alerts

Google Scholar tracks citations of published academic and legal work, including documents hosted on public URLs. Once the framework is live on GitHub Gist, it becomes indexable. Scholar is the right tool for finding framework citations in academic papers, legal blogs, law review articles, and working papers that PACER and Westlaw miss.

**Alert configuration** (scholar.google.com/scholar_alerts):

Set alerts for the following search strings, each as a separate alert:
- The full framework title (exact phrase, in quotation marks)
- "Democratic Renewal Proposal" (if this remains the working title)
- Domain titles that are analytically distinctive — for example, "prosecutorial weaponization" or "election interference 2026 midterm" — where a hit is likely to be substantively related rather than coincidental
- Author/researcher names whose work is cited throughout the framework (Levitsky, Ziblatt, Chenoweth, Balkin, Goodman) — when new publications cite their work alongside the framework's topic areas, it indicates convergent intellectual activity even without a direct citation to the framework

**Overton Index as a supplement**: Overton.io indexes policy documents — government reports, think tank publications, IGO papers — and tracks citations within them. It captures institutional citations that Scholar misses: citations in committee reports, regulatory dockets, and executive agency guidance. An Overton alert for the framework title activates the policy-document tracking layer. Cost is $99–$300/month. If budget does not allow, this layer is deferred until a citation event creates a specific reason to check manually.

**Scholar lag time**: Google Scholar indexing can lag 2–6 weeks for new documents. Initial citation events after Phase 1 launch will not appear in Scholar for several weeks. Do not interpret absence of Scholar results in the first 30 days as absence of engagement.

**Justia and CourtListener full-text search as citation supplements**: Both Justia (justia.com) and CourtListener provide full-text search of judicial opinions. If a court opinion cites the framework or uses distinctive analytical vocabulary from it, a Justia full-text search will surface it. Run a monthly manual search against Justia using domain-specific phrases as the query.

---

### 1.3 Institutional Contact Reply Tracking

This is the highest-signal data source and the most operationally intensive. Every Batch 1–N email sent during Phase 1 distribution generates a potential data point. The tracking system must capture who replied, when, with what content, and what follow-up was required.

**Minimum viable CRM fields** (implementable in Airtable without custom code):

| Field | Values | Notes |
|---|---|---|
| Contact ID | Unique identifier | Carry over from Phase 1 outreach log |
| Tier | 1 / 2 / 3 | Per Policy Influencer Map taxonomy |
| Sector | Legislative / Policy-think tank / Academic / Journalism / Legal-litigation / Civil society / Labor | See Part 2.2 taxonomy |
| Domain focus | Domain number(s) | Domains the contact received or subsequently requested |
| Batch number | 1–N | Which distribution batch |
| Send date | ISO date | |
| First reply date | ISO date | Days since batch send |
| Reply type | None / Acknowledgment / Substantive / Request / Referral / Adoption signal | See definitions below |
| Referral target | Name and org if named | Only if reply type = Referral |
| Follow-up sent | Yes / No / Pending | |
| Adoption status | Not yet / Monitoring / Confirmed | |
| Adoption evidence | Text | Specific citation, document, or contact confirmation |
| Attribution tier | Causal / Correlated / Coincidental | Applied after adoption event; see Part 3 |
| Last updated | ISO date | |

**Reply type definitions**:

- **Acknowledgment**: Receipt confirmed, no substantive content (e.g., "Thanks for sending this")
- **Substantive**: Contact engaged with content — question, critique, or discussion of a specific domain
- **Request**: Contact asked for additional materials, a specific domain document, or a follow-up conversation
- **Referral**: Contact forwarded to a named third party — the highest early signal, because it means the contact judged the framework worth passing on and has extended the network without prompting
- **Adoption signal**: Contact indicated they are using, will use, or have used framework content in their own work (explicit testimony)

**Logging discipline**: Log every reply within 48 hours. Do not wait until you have a batch to log — reply tracking that lags more than 48 hours loses the context needed to classify reply type accurately. An adoption signal logged three weeks after the conversation is a weaker evidence base than one logged within the day.

**Contact volume expectation**: At a 15–20% substantive response rate across 80–100 Tier 1–2 contacts, expect 12–20 substantive replies in the first 30 days. This is a manageable volume. The danger is not volume; it is logging discipline in the face of other demands during the busy early post-launch period.

---

## Part 2: Aggregation and Normalization

### 2.1 Case Aggregation by Domain

Every case in `litigation-tracker-2026.md` and every new case added during Phase 2 monitoring receives domain tags. The domain tag connects litigation events to the analytical framework and allows monthly roll-ups by domain.

**Domain tagging protocol**: Apply domain tags at the time a new case is added to the tracker, not retrospectively. Cases spanning multiple domains (e.g., a case challenging both warrantless arrests and racial profiling spans Domains 14 and 18) receive multiple tags. Do not force single-domain classification.

**Monthly domain roll-up metrics**:

| Metric | What it measures | Source |
|---|---|---|
| Active cases per domain | Current litigation intensity in that domain area | Cases table |
| New cases this month per domain | Acceleration or deceleration in litigation activity | Cases table (date filed filter) |
| Plaintiff win rate per domain | Legal trajectory — whether the legal resistance is succeeding or losing ground | Rulings table |
| Amicus filings per domain | Organizational mobilization by domain | Rulings table (entry type filter) |
| Adoption events per domain | Which framework domains are generating most institutional pull | Adoption events table |

**Cross-domain pattern detection**: When a single month shows a spike in both new litigation and adoption events for the same domain, this is a convergence signal — the legal community and the policy community are responding to the same pressure point simultaneously. Document convergence events explicitly; they are the strongest evidence that a domain's analysis is reaching practitioners at the moment of highest relevance.

---

### 2.2 Adoption Tracking by Sector

The Phase 1 influencer map organized contacts by tier. Phase 2 adds sector as a second axis because sector predicts the type of adoption signal that will appear and the lag time before it becomes visible. Without sector classification, the monthly review cannot distinguish between "think tank adoption is strong" and "labor sector is lagging" — it only sees aggregate adoption rate.

**Sector taxonomy and signal characteristics**:

| Sector | Representative contacts | Expected adoption signal type | Typical visibility lag | How to surface invisible adoption |
|---|---|---|---|---|
| Legislative | Congressional staff, DLCC, SiX | Bill language, hearing memo, floor statement | 60–180 days | Structured check-in; ask directly about bill drafting |
| Policy / think tank | Brennan Center, CAP, EPI, Protect Democracy | Published brief, issue paper, citation in report | 30–90 days | Scholar alert + Overton; usually surfaces publicly |
| Academic | Law faculties, Levitsky, Chenoweth, Ziblatt | Citation in paper, syllabus adoption, symposium | 60–365 days | Scholar alert; annual conference tracking |
| Journalism | Vox, Atlantic, Just Security, NPR | Article citation, interview request | 14–60 days | Google News alert; surfaces quickly |
| Legal / litigation | ACLU, NAACP LDF, Lawyers' Committee, law clinics | Brief citation, amicus argument, case strategy | 90–365 days | CourtListener amicus tracking + direct contact |
| Civil society | Indivisible, States United, Common Cause | Training materials, organizational memo | 60–120 days | Organizational website monitoring; direct follow-up |
| Labor | AFL-CIO, SEIU, NEA, EPI | Issue brief, member communication | 60–180 days | EPI publication monitoring; AFL-CIO distribution tracking |

**Monthly sector roll-up**: For each sector, compute contacts reached, contacts with any reply, contacts with confirmed adoption. Adoption rate = adopted / reached. Sectors with high reply rates but low confirmed adoption are generating internal use that has not yet surfaced publicly — these warrant active structured check-in outreach to surface invisible adoption before the 90-day window closes.

---

### 2.3 Timeline Modeling

Three curves must be tracked simultaneously. Plotting all three at the monthly review allows early detection of whether the adoption trajectory is on track, accelerating, or stalling.

**Curve 1 — Contact activation curve**: Cumulative contacts with any substantive reply over time (days since Batch 1 send). Expected shape: front-loaded, with 60% of all replies received within the first 30 days and a long tail through Day 90. If the curve flattens below the 60% threshold at Day 30, investigate delivery before concluding the content is the problem.

**Curve 2 — Adoption maturation curve**: Cumulative confirmed adoption events over time. Expected shape: lagged 30–90 days relative to the activation curve. The gap between the two curves is the "maturation gap" — it measures how long it takes an engaged contact to move from interest to confirmed use. If the maturation gap widens past 120 days without adoption confirmations, initiate structured check-ins with all contacts who showed engagement signals. Absence of adoption data does not mean absence of adoption.

**Curve 3 — Citation propagation curve**: Cumulative new secondary contacts (reached by referral or organic citation, not direct Phase 1 outreach) over time. Expected shape: near-zero for first 30 days, gradual increase as primary contacts refer the framework. The inflection point — when referral contacts begin to outnumber direct outreach contacts in a given month — is the signal that the framework has reached self-sustaining circulation within a professional network. Document the inflection date and the sector in which it occurred; it is the most important single milestone in Phase 2.

**Quarterly checkpoint**: At Day 90 (approximately August 2026 if Phase 1 launches in May), plot all three curves and determine: whether adoption rate is tracking toward 12-month targets; which sectors are ahead of or behind the sector-specific visibility lag estimates; whether the citation propagation curve has inflected.

---

## Part 3: Attribution Decision Tree

The fundamental attribution problem in policy dissemination: when a court issues a ruling that reflects arguments the framework analyzed, or a legislator introduces a bill whose language tracks the framework's recommendations, what fraction of that outcome is attributable to the framework's influence? This decision tree does not resolve the problem — it provides a consistent, documentable basis for classifying attribution so that both over-claiming and under-counting are avoided. Every adoption event in the log receives a classification, and every classification has a documented evidence basis.

---

### The Three Attribution Categories

**Causal**: The framework demonstrably changed what a contact did. Requires at least one of: (a) direct testimony from the contact confirming they used the framework in their work; (b) a published document (article, brief, report, bill language) that cites the framework by title or URL; or (c) a contact request for specific domain materials followed by documented use of those materials, confirmed by the contact. Causal attribution is the highest standard and should not be applied without specific, documentable evidence.

**Correlated**: The framework reached the contact before the adoption event, the contact showed an engagement signal, and the adoption event is analytically consistent with the framework's arguments — but direct causal connection cannot be confirmed. This is the most common category in policy dissemination work. It is honest: the connection is real, but it cannot be proven. Requires: (i) contact is confirmed in Phase 1 distribution; (ii) contact showed at least one engagement signal (any reply type other than None); (iii) adoption event occurred within the sector-specific visibility lag window; (iv) adoption event involves analytical vocabulary or arguments distinctive to the framework, not merely the same policy area.

**Coincidental**: The adoption event is consistent with the framework's arguments but there is no evidence the contact engaged with it, or the event predates framework receipt, or the analytical overlap is generic rather than distinctive. No attribution claim is warranted. This category exists to explicitly exclude events that are tempting to claim but are not supportable. Under-claiming is preferable to over-claiming when the evidence is ambiguous.

---

### The Decision Tree (apply in order)

**Step 1**: Was the contact in the Phase 1 distribution?
- No: Category = Coincidental. Log as "ambient evidence" (shows the analysis was correct, not that the framework caused anything). Stop.
- Yes: Proceed to Step 2.

**Step 2**: Did the contact show an engagement signal (any reply type other than None)?
- No: Category = Coincidental. The contact received the framework but left no evidence of engagement. Stop.
- Yes: Proceed to Step 3.

**Step 3**: Is there a direct citation to the framework (by title or URL) in a published document, or explicit testimony from the contact attributing their work to the framework?
- Yes: Category = Causal. Document the citation URL or the date, medium, and paraphrase of the testimonial statement. Stop.
- No: Proceed to Step 4.

**Step 4**: Did the adoption event occur within the sector-specific visibility lag window (see Part 2.2 sector taxonomy)?
- No (event predates the lag window, or lag window has passed with no event): Category = Coincidental. The timeline does not support a plausible influence pathway. Stop.
- Yes: Proceed to Step 5.

**Step 5**: Does the adoption event involve analytical arguments, organizational frameworks, or specific vocabulary that is distinctive to the 35-domain framework — not merely the same policy area?
- No (generic policy overlap — anyone following the news would have produced similar analysis): Category = Coincidental.
- Yes (distinctive analytical vocabulary, comparative constitutional framing, specific domain structure, or research citations that trace back to the framework's source material): Category = Correlated.

---

### Attribution Log Entry Format

Every adoption event — Causal, Correlated, or Coincidental — receives a log entry. The log is the audit trail. If adoption claims are ever challenged, this log is the response.

```
Contact: [Name / Organization / Tier / Sector]
Framework receipt date: [Date of Batch N send]
Engagement signal: [Type per taxonomy / date / brief paraphrase]
Adoption event: [Description / URL or document reference if public / date]
Attribution category: [Causal / Correlated / Coincidental]
Evidence basis: [Specific: citation URL, testimonial date and paraphrase, or description of distinctive analytical overlap]
Confidence: [High / Medium / Low]
  High = two or more independent evidence points
  Medium = one clear evidence point
  Low = single indirect or ambiguous signal
```

---

## Part 4: Monitoring Dashboard Specification

### 4.1 Weekly View (Active Monitoring Layer)

Cadence: Every Tuesday morning. This allows Monday court filings to appear and captures weekend social/media engagement.

**Weekly review panels**:

| Panel | Data source | What to look for |
|---|---|---|
| New court filings and rulings | CourtListener alert digest | Any ruling in tracked cases; new cases in tracked categories; amicus filings |
| Reply log status | Airtable CRM | New replies since last Tuesday; any reply requiring follow-up within 48h |
| Citation alerts | Google Scholar / News alert digest | Any citation event or press mention |
| Referral contacts | CRM (referral target field) | Any new contacts who appeared via referral from Phase 1 recipients |
| Anomaly flags | Manual scan | Any data point falling outside the ranges defined in 4.3 |

**Time required**: 30–45 minutes. The weekly view is diagnostic, not analytical. Its function is to ensure no signal sits unaddressed through the week.

---

### 4.2 Monthly View (Analytical Layer)

Cadence: First Monday of each month. First monthly review: approximately 30 days after Batch 1 send.

**Monthly review panels**:

| Panel | Data source | What to calculate |
|---|---|---|
| Contact activation rate | CRM | Substantive replies / total contacts reached. Target: 15–20% by Day 30 |
| Adoption confirmed by sector | CRM + attribution log | Count per sector; compare against sector-specific lag window estimate |
| Case activity by domain | Litigation tracker | Active cases, new cases, new rulings, plaintiff win rate — per domain |
| Citation events | Scholar + Overton + Justia manual search | New citations in academic, policy, journalism, legal sources |
| Curve plots | Python or Airtable chart | Activation curve, adoption maturation curve, citation propagation curve |
| Attribution log review | Attribution log | New Causal or Correlated entries; any reclassifications from prior months |
| Revision queue update | Research notes | Domains receiving substantive pushback from contacts; schedule for next update cycle |

**Monthly output**: A brief (2–3 paragraph) internal assessment written to WORKLOG.md. Not a formal report — a concise statement of whether the adoption trajectory is on track, above, or below target, and what the next month's priority action is. The assessment should name specific contacts or events, not use only aggregate numbers.

---

### 4.3 Anomaly Detection

An anomaly is any data point that diverges meaningfully from the expected trajectory. Because early-phase sample sizes are small, formal statistical thresholds are not appropriate. The following triggers define operationally significant anomalies.

**Positive anomalies — accelerate response**:

- A Tier 1 contact refers the framework to three or more named individuals within 14 days of receipt. This is a bridge node event. Stop standard follow-up cadence and prioritize the relationship with the referring contact; they are a hub, and hubs compound.
- A court ruling in a tracked case cites comparative constitutional arguments that trace directly to the framework's analytical domains. Identify the filing attorney and organization; add to the direct outreach list for Phase 2.
- A Tier 2 journalist requests a briefing call. This is rare. Respond same day; do not let it sit.
- Google Scholar records a citation of the framework within 60 days of distribution — earlier than the 2–6 week indexing lag plus 30-day minimum adoption time. This signals faster academic uptake than the lag model predicts; immediately classify as Causal and document.
- A second or third referral contact from the same organization appears independently. This means the framework is circulating inside the organization without further direct outreach — it has reached the internal distribution stage, which typically precedes formal institutional adoption.

**Negative anomalies — investigate and adjust**:

- Reply rate falls below 8% at Day 30. This is below even the conservative lower bound of the 15–20% target. Before concluding the content is the problem, investigate delivery: check for bounced emails, verify Gist URLs are loading correctly, confirm subject line is not triggering spam filters. Do not adjust content before diagnosing the delivery problem.
- Two or more Tier 1 contacts raise the same objection to a specific domain within 14 days. This is an immediate triage trigger regardless of the monthly review cycle. That domain enters the revision queue for a rapid assessment — is the objection about evidence quality, framing, or factual accuracy?
- No adoption confirmation events by Day 90. This is the maturation gap warning. Initiate structured check-in outreach with every Tier 1 contact who showed an engagement signal. Ask a specific, substantive question about a recent development in their area — do not ask whether they have read the document.
- A court ruling in a tracked case goes against the expected legal trajectory (e.g., a circuit court reverses an injunction that had been holding). The litigation tracker requires immediate update. Assess whether the ruling weakens the evidentiary basis of the relevant domain and whether recipients who are using that domain in their work need to be notified.
- A referral contact reports that the framework they received has already been superseded by more recent analysis. This is a staleness signal; it indicates the distribution reached a contact who was already well-informed and found the framework insufficiently current. Schedule a domain update for the area the contact referenced.

---

## Part 5: Tooling Options

### 5.1 Airtable (Recommended Starting Configuration)

Airtable is the right tool for contact and adoption tracking. It handles relational data, supports formula fields, and has a visual interface that makes the monthly review practical without requiring SQL fluency. The free tier supports up to 1,000 records per base and 2 weeks of revision history — sufficient for the first 6 months at expected volumes.

**Recommended base structure**:

- **Contacts table**: One row per contact. Core fields listed in Part 1.3. Linked to Adoption Events.
- **Adoption Events table**: One row per adoption event. Linked to Contacts. Fields: event type, date, description, URL or document reference, attribution category, confidence, evidence basis.
- **Cases table**: One row per tracked case. Fields: case name, court, domain tags, current status, plaintiff, defendant, last updated, next deadline, ruling date if applicable.
- **Rulings table**: One row per order or opinion. Linked to Cases. Fields: date, entry type (order / opinion / amicus / motion), outcome (for plaintiff / for defendant / procedural), key holding, domain relevance, amicus filer if applicable.

**Airtable automations** (free and paid tiers): Configure an automation that sends an email or Slack message when a record in the Adoption Events table is created with attribution category = "Causal". This ensures no Causal event sits unreviewed for more than 24 hours.

**Upgrade threshold**: If record count approaches 1,000 after 6 months, export historical data to an archived base and continue in a fresh base. The Pro tier ($20/month) removes the record limit and extends revision history to 6 months.

---

### 5.2 Zapier (Integration and Alert Routing)

Zapier connects services that do not natively integrate. The three most useful workflows for this system:

**Workflow 1 — CourtListener alert to Airtable**: When a CourtListener email alert arrives (trigger: email received from courtlistener.com with a subject matching a tracked case name), parse the case name and docket entry type, then create a new record in the Rulings table with case name, date, and entry type pre-filled. This eliminates manual log creation for court events.

**Workflow 2 — Google Scholar alert to Airtable**: When a Scholar alert email arrives, create a record in the Adoption Events table with event type = "Citation," paste the alert content into the description field, and set attribution category = "Pending — needs classification." Flag it for review in the next weekly session.

**Workflow 3 — Gmail reply prompt**: When an email reply arrives from a sender matching a contact record's email address, trigger an Airtable update prompt (opens a prefilled form for the reply log entry). This functions as a reminder to log rather than an automated log; it does not write to Airtable automatically without review.

**Zapier cost**: The free tier supports 5 Zaps and 100 tasks/month. Workflows 1–3 stay within this limit in most months. If adoption events scale significantly after Month 3, the Starter tier ($20/month) handles 750 tasks/month. n8n (open source, self-hostable) is a zero-cost alternative for operators willing to manage a server.

---

### 5.3 Python Batch Scripts

Python handles two tasks that Airtable and Zapier cannot do efficiently: bulk docket metadata retrieval and curve plotting for the monthly review. All three scripts below run in the existing UV-managed Python environment with no additional environment configuration beyond installing `requests`, `pandas`, `matplotlib`, and `pyairtable` via `uv pip install`.

**Script 1 — CourtListener docket monitor** (`cl_monitor.py`):

Uses the CourtListener REST API to query docket entries for all cases in the tracker. Designed to run daily via cron at 09:00 UTC. Queries the `/api/rest/v3/docket-entries/` endpoint with parameters `docket_id` (one query per tracked case) and `date_filed__gte` (entries since the previous run date). Outputs a JSON file of new docket entries filtered to entry types that warrant review: opinions, orders, preliminary injunction motions, and amicus filings. Does not retrieve document content — only metadata. The human review determines which entries warrant document retrieval via PACER.

Authentication: CourtListener API token, free with account registration. Token is passed as a Bearer token in the Authorization header.

**Script 2 — Adoption curve plotter** (`adoption_curves.py`):

Reads from an Airtable CSV export (generated manually at the start of each monthly review) and plots the three curves defined in Part 2.3 using matplotlib. Outputs a single PNG with three subplots side by side. Run manually as part of the monthly review, not on a cron schedule. Input: two CSV files (contacts export, adoption events export). Output: `adoption_curves_YYYY-MM.png` saved to the working directory.

**Script 3 — Attribution log exporter** (`attribution_export.py`):

Reads the Airtable adoption events table via the Airtable API (`pyairtable` library), filters to records where attribution category is "Causal" or "Correlated," and exports them as a formatted Markdown file. Used to generate the monthly attribution summary without manual transcription. The output file is a straightforward list: contact name, org, event date, adoption event description, attribution category, evidence basis. Run at the end of each monthly review session.

---

### 5.4 Tooling Decision Matrix

| Function | Tool | Setup time | Ongoing effort | Monthly cost |
|---|---|---|---|---|
| Contact and adoption CRM | Airtable | 3–4 hours (initial base build) | 30 min/week | Free (first 6 months) |
| Court alert monitoring | CourtListener built-in alerts | 1 hour | Minimal | Free |
| Citation monitoring | Google Scholar alerts | 30 min | Minimal | Free |
| Alert-to-Airtable routing | Zapier | 2 hours | None once configured | Free tier sufficient |
| Bulk docket metadata retrieval | Python cl_monitor.py | 2 hours (write + test) | Minimal (cron) | Free |
| Monthly curve visualization | Python adoption_curves.py | 1 hour (write + test) | 30 min/month | Free |
| Policy document citation tracking | Overton.io | 30 min | Minimal | $99+/month, optional |

**Minimum viable stack**: Airtable + CourtListener alerts + Google Scholar alerts. Operational within 4 hours. Covers approximately 80% of the monitoring surface. Python scripts and Zapier reduce manual effort but are not required for the system to function. Start with the minimum viable stack on Day 1 and add automation components during Month 1 as time allows.

---

## Part 6: 12-Month Tracking Roadmap

### Pre-Launch Setup Window (Days -7 to 0)

The system should be built before Batch 1 goes out, not after. The seven days before launch are the window to configure tools so monitoring begins on Day 1 rather than catching up during the first week.

**Day -7 to -5**: Build Airtable base. Create Contacts, Adoption Events, Cases, and Rulings tables. Import Phase 1 contact list from the distribution log. Import the case list from `litigation-tracker-2026.md` into the Cases table with initial domain tags.

**Day -4 to -3**: Configure CourtListener alerts for all 38+ tracked cases. Test that alerts deliver to the monitored email address. Configure Google Scholar alerts for framework title and domain titles. Set up Google News alerts for framework title and key domain vocabulary.

**Day -2 to -1**: Set up Zapier workflows (CourtListener alert → Airtable Rulings entry; Scholar alert → Airtable Adoption Events entry). Test each workflow end-to-end with a simulated trigger. Configure Airtable automations for Causal attribution events.

**Day 0**: Batch 1 sends. Monitoring begins.

---

### Month 1 (Days 1–30): Activation and First Signal

**Week 1 (Days 1–7)**: Log all replies within 48 hours of receipt. Apply reply type classification immediately. Run the first weekly review on Day 7: confirm that CourtListener and Scholar alerts are delivering, that Zapier workflows are routing correctly, and that the reply log has no gaps. This week's review is primarily a system health check, not an analytical review.

**Weeks 2–4 (Days 8–30)**: Continue logging replies. Note any domains generating disproportionate engagement (multiple contacts asking about the same domain within a short window). At Day 30, run the first monthly review: compute contact activation rate, plot the activation curve (Day 1–30 only), note any anomalies, write a brief WORKLOG entry.

**Month 1 targets**: 12–20 substantive replies; 2–5 referral contacts identified; 0–2 adoption events at any attribution level; 3–5 new court rulings logged in tracked cases. If reply rate is below 8%, treat as a negative anomaly and diagnose delivery before Day 35.

---

### Months 2–3 (Days 31–90): Signal Consolidation

**Primary focus**: Distinguishing genuine adoption pipeline from noise; building the baseline dataset for curve analysis.

**Key actions**:

Conduct structured check-in outreach to contacts who showed engagement signals in Month 1 but have not confirmed adoption. Use the structured check-in format from `measurement-and-iteration-framework.md` (Mechanism 3): ask a specific, substantive question about a recent development relevant to the contact's area, not a follow-up asking whether they read the document.

Begin Domain 37 re-measurement: compare the active DOJ voter roll lawsuit count against the May 2026 baseline established in `domains/domain-37-baseline-metrics.md` (24 active + DC as of May 4, 2026). Note whether appellate courts have ruled on any of the three pending appeals (Michigan Sixth Circuit, Oregon, California Ninth Circuit). Record the current count and any new developments in the re-measurement field.

If the revision queue has any entries (two or more Tier 1 contacts objecting to the same domain), run the domain revision assessment and complete updates before Month 3 ends.

**Day 90 curve review**: Plot all three curves. Identify sectors ahead of or behind the visibility lag estimate. Note whether any sectors have shown the maturation gap warning (high engagement, low confirmed adoption).

**Month 3 targets**: 1–3 Causal attribution events; 5–15 Correlated attribution events; at least 1 academic or journalism citation visible in Scholar or news monitoring; adoption confirmed in at least 2 sectors.

---

### Months 4–6 (Days 91–180): Adoption Maturation

**Primary focus**: Tracking institutional adoption as contacts who engaged in Months 1–3 move from interest to documented use.

**Key actions**:

Legislative sector check-in: any confirmed Hill staff recipients should receive a structured check-in around Month 4–5. Ask a specific question about committee work or bill drafting in the relevant policy area. Legislative adoption is almost entirely invisible to passive monitoring; active contact intelligence is the only way to detect it before it surfaces in public legislative records.

Litigation sector monitoring: review new amicus briefs filed in tracked cases for analytical overlap with framework domains. If an amicus filer is a Phase 1 recipient and the brief's arguments overlap distinctively with the framework's analysis, classify as Correlated and log the brief citation.

Academic sector: Month 4–6 is when initial academic interest from Month 1–3 contact converts to invited symposium contributions or working paper citations. Law review symposium planning cycles run 6–12 months from initial contact to publication; a Month 5 citation to the framework in a symposium invitation is the leading indicator of a published citation 6 months later.

Second Domain 37 re-measurement: August–September 2026 is the window when the midterm election cycle enters the period of highest interference risk. Re-measure all six baseline metrics from `domain-37-baseline-metrics.md` and note changes from the May 2026 baseline.

**Month 6 targets**: Adoption rate of 8–15% across all Tier 1–2 contacts; at least 1 legislative sector adoption event at any attribution level; at least 1 published document with Causal attribution; citation propagation curve showing measurable referral network growth; Domain 37 re-measurement complete for at least 3 of 6 baseline metrics.

---

### Months 7–9 (Days 181–270): Amplification

**Primary focus**: Identifying which domains and sectors are generating the strongest adoption signal and concentrating the next research cycle accordingly.

**Key actions**:

Run a domain-level adoption review: which domains have the highest confirmed attribution count (Causal + Correlated combined)? Domains with the highest adoption rate are the candidates for Phase 2 research depth — additional case studies, updated statistics, new comparative analysis. Allocate the next research iteration cycle to those domains, not to domains selected arbitrarily.

Directly engage referral contacts who showed engagement signals — they arrived through organic network spread rather than direct Phase 1 outreach. These contacts represent the self-sustaining circulation threshold. Their engagement is qualitatively more significant than an engagement from a direct outreach recipient because it required no prompt.

Litigation tracker deep update: cases filed in early 2026 will reach summary judgment or preliminary injunction ruling stages in district courts during Months 7–9. Update case status for all tracked cases; flag any cases where the legal trajectory has shifted from the early 2026 assessment that informed the framework's domain analysis.

**Month 9 targets**: At least 5 Causal attribution events across at least 3 sectors; citation propagation curve inflected in at least 1 sector; at least 1 Domain 37 metric showing measurable change from the May 2026 baseline.

---

### Months 10–12 (Days 271–365): Annual Assessment and Phase 3 Scoping

**Primary focus**: Consolidating the 12-month record and identifying Phase 3 priorities from the data.

**Key actions**:

Run `attribution_export.py` to generate the complete attribution log export. Review all Correlated entries and determine whether any now have sufficient additional evidence to upgrade to Causal. Verify the evidence basis for every Causal entry — confirm that cited documents are still accessible at their recorded URLs.

Conduct a domain adoption audit: for each of the 35+ domains, document whether adoption was confirmed in any sector. Identify the 5 domains with the strongest adoption record and the 5 with the weakest. Weakest-adoption domains are candidates for either revision (if the evidence is the problem) or retargeting (if the wrong audience is receiving them).

Final Domain 37 re-measurement against all 6 May 2026 baselines. Document the full change in each metric over the 12-month period.

Write the Phase 3 scoping brief: a 1–2 page internal document identifying the three highest-priority Phase 3 actions based on the 12-month adoption data. Potential Phase 3 actions include domain expansion into areas showing high demand but no current coverage; new sector outreach based on which sectors are under-reached; a litigation support strategy for cases where the framework's analysis is being actively used; or a legislative campaign tied to a specific domain where both think tank and civil society adoption are confirmed.

**Year-end targets**: Adoption confirmed in at least 4 of 7 sectors; at least 10 Causal attribution events total; at least 1 domain cited in a court filing or congressional hearing record; citation propagation curve inflected in at least 2 sectors; Domain 37 re-measured against all 6 baseline metrics with year-over-year change documented.

---

## Operational Notes

**The contact log is the foundation**. Everything else — curve plotting, attribution classification, sector rollup, anomaly detection — depends on having a complete and accurate record of who replied, when, and what they said. Log every reply within 48 hours. A tracking system with incomplete input data produces misleading output that is worse than no tracking at all.

**Absence of data is not absence of adoption**. The most operationally important adoptions — Hill staff incorporating domain language into legislation, a coalition attorney building a brief argument around comparative constitutional evidence, a union researcher using domain analysis in contract campaign materials — leave no public footprint for months. Passive monitoring systematically undercounts the highest-value adoptions. Active contact intelligence is not a supplement to passive monitoring; it is the primary layer for institutional sectors.

**Attribution discipline is a credibility asset**. The temptation in policy dissemination work is to claim adoption whenever a downstream event is consistent with the framework's arguments. This is a mistake. Correlated attribution claimed accurately is more valuable than Causal attribution claimed inaccurately. The attribution log is only as useful as it is honest.

**Related files**:
- `/home/awank/dev/SuperClaude_Framework/projects/resistance-research/measurement-and-iteration-framework.md` — Phase 1 success metrics and feedback mechanisms; the precursor framework this system extends
- `/home/awank/dev/SuperClaude_Framework/projects/resistance-research/litigation-tracker-2026.md` — Active case log that feeds the Cases and Rulings tables
- `/home/awank/dev/SuperClaude_Framework/projects/resistance-research/domains/domain-37-baseline-metrics.md` — Quantified baselines that Month 3, 6, and 9 re-measurements are compared against
- `/home/awank/dev/SuperClaude_Framework/projects/resistance-research/phase-1-execution-checklist.md` — The execution sequence whose completion triggers Day 0 of this roadmap
