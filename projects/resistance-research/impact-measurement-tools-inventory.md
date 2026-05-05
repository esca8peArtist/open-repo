---
title: "Impact Measurement Tools Inventory"
date: 2026-05-05
status: production-ready
phase: Phase 1 Day 0 setup
distribution_paths: A / A+37 / B (path-independent)
companion_files:
  - adoption-tracking-dashboard-spec.md            # Dashboard components and alert templates
  - post-distribution-impact-measurement.md        # Metrics framework, baselines, failure modes
scope: "Tool-by-tool inventory: citation tracking, policy databases, litigation tracking, media monitoring, vocabulary tracking. Cost analysis. Setup timeline."
---

# Impact Measurement Tools Inventory

**Day 0 setup reference. Activate tools in the order below — not all at once.**

This inventory covers every tool needed to run the adoption tracking dashboard in `adoption-tracking-dashboard-spec.md`. Each entry includes: what it tracks, access tier (free / freemium / paid), setup time, and setup window (Day 0 / Month 1 / Month 3). Tools are sequenced — activate Day 0 tools on distribution day; Month 1 tools during the first week of monitoring; Month 3 tools at the 90-day review.

---

## Category 1: Citation Tracking

### Google News Alerts
**What it tracks:** News articles, blog posts, press releases, and some government documents mentioning alert keywords. Strongest for media and advocacy adoption signals.
**Access:** Free, no account required (Google account recommended for management)
**URL:** news.google.com/alerts
**Setup time:** 15 minutes
**Coverage gaps:** Does not reliably index PDF documents, paywalled content, or legal filings. Supplement with CourtListener for litigation, Overton for policy documents.
**Activation window:** Day 0 — create all alert sets before distributing the framework
**Alert sets:** See `adoption-tracking-dashboard-spec.md` Component 1.1 for exact query strings

---

### Google Scholar Alerts
**What it tracks:** Academic papers, law review articles, working papers indexed in Google Scholar. Best for 12–24 month academic adoption window.
**Access:** Free, Google account required
**URL:** scholar.google.com/scholar_alerts
**Setup time:** 10 minutes
**Coverage gap:** Only indexes items already in Scholar's database; new working papers take 1–4 weeks to index. SSRN preprints typically index within 2 weeks of upload.
**Activation window:** Day 0 — set up immediately; do not expect results before Month 3

---

### SSRN (Social Science Research Network)
**What it tracks:** Law and social science working papers and preprints. Most law faculty post working papers on SSRN before journal publication; this is the earliest signal of academic adoption.
**Access:** Free for search and download; free account for download tracking and author alerts
**URL:** ssrn.com
**Setup time:** 15 minutes to create an account and set keyword alerts
**Key capability:** SSRN email alerts for papers matching keyword searches; download counts for any framework paper posted here
**Activation window:** Day 0 if the framework document is posted to SSRN as a working paper; Month 1 for keyword monitoring of other authors' papers
**Search strategy:** Run monthly searches for `"democratic renewal" institutional framework` and `"domain" election interference 2026 United States` in the law and political science categories

---

### HeinOnline
**What it tracks:** Law review articles, legal periodicals, government documents. The most comprehensive searchable database of legal scholarship in the United States.
**Access:** Paid institutional subscription (typically $3,000–$8,000/year for standalone; included in most law school library subscriptions). No free public access for full text.
**URL:** heinonline.org
**Cost:** Institutional only unless you have law school affiliation. If no affiliation: use Google Scholar as free substitute for most searches; HeinOnline's ScholarCheck citation ranking data is not available elsewhere.
**Alternative for non-institutional users:** Harvard Law School Library and many state bar association libraries offer free HeinOnline access to the public. Contact your state bar.
**Activation window:** Month 3 — first meaningful law review coverage expected 6–12 months post-distribution; HeinOnline search most useful at Month 6 and Month 12

---

### Overton.io
**What it tracks:** Policy documents — government reports, think tank publications, intergovernmental organization documents, NGO reports. Largest publicly accessible policy document database (21 million+ documents). Tracks citations between policy documents and to academic literature.
**Access:** Free public search tier (limited queries); institutional access free via SAGE partnership at partner universities. Register at overton.io.
**URL:** overton.io
**Setup time:** 30 minutes (account creation + initial search templates)
**Critical limitation:** 6–18 month indexing lag. Documents published today will not appear in Overton search results until 6–18 months after publication. Do not expect Overton results before Month 4.
**Best use:** Confirming at Month 6 and Month 12 what the citation monitor detected in real time at Month 1–3. Also useful for establishing pre-distribution baseline (documents from 2024–2025 are already indexed).
**Activation window:** Month 3 (first query to establish expected output pattern); meaningful results from Month 6
**Source:** [Overton — bibliometric database of policy document citations (MIT Press, QSS 2022)](https://direct.mit.edu/qss/article/3/3/624/112760/Overton-A-bibliometric-database-of-policy-document)

---

## Category 2: Policy Database Access

### Congress.gov
**What it tracks:** All introduced federal legislation, committee reports, floor amendments, congressional record entries. Full text searchable.
**Access:** Free, no account required
**URL:** congress.gov/search
**Setup time:** 5 minutes to bookmark and run initial search
**Search strategy:** Full-text search for `"NVRA" "voter roll" purge 2026`, `"ICE" polling place election`, `"judicial independence" federal funding`, `"fiscal authority" executive impoundment`. Filter by "Bills and Resolutions" and current Congress.
**Activation window:** Day 0 — run baseline search before distribution; re-run monthly

---

### LegiScan API
**What it tracks:** State legislative bills and amendments in all 50 states. Full-text search. Email alerts for new bill filings matching saved searches.
**Access:** Free tier: 30,000 API queries/month; paid tiers for bulk data and webhook alerts
**URL:** legiscan.com/legiscan-register
**Setup time:** 30 minutes (account + saved search configuration)
**Key advantage:** Only free tool that monitors all 50 state legislatures simultaneously for new bill filings. Voting Rights Lab and Brennan Center roundups are more curated but updated less frequently.
**Activation window:** Day 0 — set up saved searches before distributing the framework; configure email alerts for priority states

---

### Voting Rights Lab Election Policy Tracker
**What it tracks:** Voting legislation in all 50 states — introduced, passed, signed. Categorized by policy type (voter ID, early voting, registration, election administration). Updated continuously.
**Access:** Free, no account required
**URL:** tracker.votingrightslab.org
**Setup time:** 5 minutes to bookmark; check weekly
**Activation window:** Day 0

---

### Brennan Center State Voting Laws Roundups
**What it tracks:** Monthly roundup of enacted and pending voting legislation. Expert commentary on significance. Most authoritative secondary source for state voting law changes.
**Access:** Free
**URL:** brennancenter.org/series/state-voting-laws-roundups
**Activation window:** Month 1 — first monthly roundup after distribution launch

---

## Category 3: Litigation Tracking

### CourtListener / RECAP Archive
**What it tracks:** Federal court dockets and filings (PACER documents), plus searchable RECAP archive of over 100 million docketed documents. Search alert feature ("Google Alerts for federal courts") sends email when new filings match saved searches.
**Access:** Free. Five daily alerts on the free forever tier. RECAP browser extension (Firefox, Chrome, Safari) automatically shares purchased PACER documents to the public archive.
**URL:** courtlistener.com and free.law/recap/
**Setup time:** 20 minutes (account + saved searches + RECAP extension install)
**Key capability:** RECAP Search Alerts launched in 2025 allow keyword monitoring of all PACER filings as they are docketed — equivalent of a real-time litigation monitoring service, free.
**Activation window:** Day 0 — create saved searches before distribution; install RECAP extension immediately
**Source:** [Free Law Project RECAP Suite](https://free.law/recap/) | [CourtListener RECAP Search Alerts launch (LawSites, 2025)](https://www.lawnext.com/2025/06/courtlistener-launches-recap-search-alerts-for-pacer-filings-google-alerts-for-federal-courts.html)

---

### Democracy Docket
**What it tracks:** Election law litigation — voting rights cases, election administration cases, gerrymandering. Expert commentary. Case database.
**Access:** Free
**URL:** democracydocket.com/cases/
**Activation window:** Day 0 — bookmark and check weekly for new case filings in Domain 1, 33, 37 areas

---

### Just Security Litigation Tracker
**What it tracks:** All federal civil challenges to the Trump administration (as of 2026: 362+ cases). Updated regularly. Expert legal analysis.
**Access:** Free
**URL:** justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/
**Activation window:** Day 0 — bookmark; check weekly for new cases in framework domain areas

---

### PACER (Public Access to Court Electronic Records)
**What it tracks:** All federal court dockets and filings — the authoritative source. CourtListener/RECAP provides free access to a large subset of PACER documents already retrieved by other users.
**Access:** Pay-per-page ($0.10/page after $30/quarter threshold; fee waived if usage under threshold). Not free but near-free for targeted searches.
**URL:** pacer.uscourts.gov
**Activation window:** Month 3 — use CourtListener RECAP first; use PACER directly only when a specific document is needed that is not in the RECAP archive

---

## Category 4: Media Monitoring

### Google News Alerts (see Category 1)
Best free option for media monitoring. Configure alert sets as specified in `adoption-tracking-dashboard-spec.md` Component 1.1.

---

### Meltwater / Cision / LexisNexis Newsdesk
**What it tracks:** Comprehensive media monitoring including licensed content, broadcast, and paywalled sources not accessible to Google Alerts. Industry-standard PR monitoring tools.
**Access:** Paid. Pricing starts at approximately $10,000–$20,000/year for Meltwater; similar for Cision. LexisNexis Newsdesk pricing on request.
**URL:** meltwater.com | cision.com | lexisnexis.com/newsdesk
**Recommendation:** Not necessary for solo researcher monitoring. Google Alerts + manual monitoring of target publication RSS feeds covers 80%+ of relevant media at zero cost. Consider only if the framework achieves Tier 1 adoption and you need systematic coverage tracking for a funder report or institutional report.
**Activation window:** Optional, Month 6+ if resources allow
**Source:** [Media Monitoring Tools comparison — Meltwater vs Cision (NewsbyWire, 2025)](https://newsbywire.com/meltwater-vs-cision-comparing-media-monitoring-and-pr-software/)

---

### RSS Feed Monitoring (Target Publication Feeds)
**What it tracks:** New articles from specific publications. Real-time.
**Access:** Free (RSS reader: Feedly free tier, Inoreader free tier)
**Publications to subscribe:** Brennan Center, Just Security, ProPublica, The Atlantic, Democracy Docket, Lawfare, Balls and Strikes, SCOTUSblog
**Setup time:** 20 minutes (RSS reader account + feed subscriptions)
**Activation window:** Day 0

---

## Category 5: Vocabulary Tracking

### Regex Pattern Library for Framework-Specific Vocabulary

Build this list at distribution launch. These are terms coined or specifically operationalized in the framework that are unlikely to appear in pre-distribution discourse. A Google Alert hit on any of these terms from a major institutional source is a high-confidence vocabulary adoption signal.

**High-confidence markers (unlikely pre-existing usage in this context):**
- `"ICE-at-polls"` or `"ICE at polls"` — enforcement pattern at polling locations
- `"NVRA quiet period"` — the 90-day pre-election prohibition on voter roll removals
- `"state legislative autocratization"` — Domain 33's specific analytical frame
- `"appellate capture"` — Domain 6's framing of circuit court ideological engineering
- `"constraint failure"` — Domain analysis terminology for institutional breakdown
- `"fiscal authority bypass"` — Domain 34's framing of OMB/Treasury executive actions
- `"voter surveillance database"` — Domain 37's characterization of SAVE deployment

**Medium-confidence markers (may appear in independent usage, but unusual in combination):**
- `"SAVE" "false positive" voter roll` — the 81% error rate evidence from Domain 37
- `"pattern-and-practice" immigration enforcement Fourth Amendment` — Domain 16 theory
- `"independent agency removal" democratic accountability` — Domain 6 and Domain 28 framing
- `"election denier" federal appointment` — Domain 37 framing of EIN appointees

**Tracking method:** Create Google Alerts for each high-confidence marker (see Category 1). Run manual Google News searches for medium-confidence markers quarterly. Log any hit in the Adoption Scorecard under the relevant organization.

---

## Cost Summary

| Tool | Cost | Priority | Setup window |
|------|------|----------|-------------|
| Google News Alerts | Free | Required | Day 0 |
| Google Scholar Alerts | Free | Required | Day 0 |
| SSRN search | Free | Required | Day 0 |
| CourtListener / RECAP | Free | Required | Day 0 |
| Democracy Docket | Free | Required | Day 0 |
| LegiScan API | Free (30K queries/mo) | Required | Day 0 |
| Voting Rights Lab tracker | Free | Required | Day 0 |
| Congress.gov | Free | Required | Day 0 |
| Brennan Center roundups | Free | Required | Month 1 |
| Just Security tracker | Free | Required | Day 0 |
| RSS feeds (Feedly free) | Free | Recommended | Day 0 |
| Overton.io (free tier) | Free | Required | Month 3 |
| PACER | ~$0 (under threshold) | As needed | Month 3 |
| HeinOnline | Institutional / free via bar library | Recommended | Month 6 |
| Meltwater / Cision | $10K–$20K/yr | Optional, Month 6+ | Only if needed |

**Total cost for solo researcher with no institutional affiliation: $0 to establish full monitoring infrastructure.** The paid tools add coverage depth but are not required for meaningful adoption tracking.

---

## Setup Timeline: What to Activate When

### Day 0 (Distribution launch day — 90 minutes total setup)
1. Google News Alerts — all sets (15 min)
2. Google Scholar Alerts (10 min)
3. CourtListener account + RECAP extension + saved searches (20 min)
4. LegiScan account + saved searches + email alerts (30 min)
5. Democracy Docket, Just Security, Voting Rights Lab bookmarks (5 min)
6. RSS reader with target publication feeds (10 min)
7. Run baseline vocabulary sweep: Google News search for each high-confidence vocabulary marker; document results as pre-distribution baseline (10 min)

### Month 1 (First week of monitoring)
1. Create Google Sheets dashboard using schema from `adoption-tracking-dashboard-spec.md` (60 min)
2. Populate Adoption Scorecard with all Tier 1 contacts from `DISTRIBUTION_OUTREACH_CONTACTS.md` (30 min)
3. Subscribe to Brennan Center roundup and other monthly publication digests (15 min)
4. Run first Month 1 Snapshot (see dashboard spec) (30 min)

### Month 3 (90-day review)
1. Create Overton account; run baseline query; document results (30 min)
2. Run full vocabulary sweep for medium-confidence markers (30 min)
3. Run full failure mode audit (45 min)
4. First Overton search against distribution-era documents (note: most results will still be in indexing lag; document the null result as expected baseline)

### Month 6 (180-day evaluation)
1. Run pre-post baseline comparison using Section 5 baselines from `post-distribution-impact-measurement.md` (60 min)
2. Second Overton search; compare against Month 3 baseline (20 min)
3. HeinOnline search for law review citations (if institutional access available) (30 min)
4. Full failure mode audit + decay detection sweep (45 min)
5. Decide whether to activate paid media monitoring tools based on adoption scale

---

*Sources: [RECAP Suite and CourtListener — Free Law Project](https://free.law/recap/) | [Overton bibliometric database — MIT Press QSS 2022](https://direct.mit.edu/qss/article/3/3/624/112760/Overton-A-bibliometric-database-of-policy-document) | [SAGE-Overton partnership for researchers](https://www.sagepub.com/explore-our-content/press-office/press-releases/2023/12/07/sage-partners-with-overton-on-free-to-use-tool-that-empowers-researchers-to-uncover-their-policy-impact) | [SSRN for legal scholarship — BYU Hunter's Query](https://huntersquery.byu.edu/how-to-use-ssrn-a-source-for-the-hottest-new-legal-scholarship/) | [HeinOnline citation tools — Drake Law Library](https://libguides.law.drake.edu/c.php?g=1312171&p=9644962) | [Meltwater media monitoring overview](https://www.meltwater.com/en/products/media-monitoring) | [CourtListener RECAP Search Alerts launch 2025](https://www.lawnext.com/2025/06/courtlistener-launches-recap-search-alerts-for-pacer-filings-google-alerts-for-federal-courts.html)*
