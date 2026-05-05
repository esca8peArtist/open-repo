---
title: "Phase 1 Measurement Dashboard — Specification and Operational Manual"
date: 2026-05-05
status: production-ready
purpose: >
  Defines the real-time KPI tracking architecture for Phase 1 distribution.
  Specifies what gets measured at each cadence (daily, weekly, monthly),
  where data comes from, how the dashboard is structured, what is automated
  vs. manually curated, and how measurement reliability is scored.
  Companion to attribution-measurement-plan.md and phase-1-baseline-metrics.md.
cross_references:
  - attribution-measurement-plan.md
  - phase-1-baseline-metrics.md
  - BATCH_1_CONTACT_LOG.md
  - DISTRIBUTION_EXECUTION_LOG.md
---

# Phase 1 Measurement Dashboard — Specification and Operational Manual

**Established: May 5, 2026 — before Phase 1 distribution**

This document specifies the operational measurement system that activates the moment Phase 1 distribution begins. It translates the attribution methodology in `attribution-measurement-plan.md` and the baselines in `phase-1-baseline-metrics.md` into a concrete tracking architecture: what to check daily, what to check weekly, what to review monthly, and how to summarize the state of Phase 1 health in a single weekly status entry that takes under 30 minutes to produce.

The dashboard is designed for a one-person operation. It does not assume institutional infrastructure, staff, or paid subscriptions beyond the free tools already in the stack. Every measurement cadence maps to a specific action and a specific file in the repository.

---

## Part I: Dashboard Architecture — Four Views

The dashboard has four logical views, each serving a different decision need. All views draw from the same underlying data log (`DISTRIBUTION_EXECUTION_LOG.md`), which is the single source of truth for all Phase 1 activities and outcomes.

### View 1: Summary Dashboard (Weekly — 15 minutes)

**Purpose**: Answer the question "Is Phase 1 on track?" at a glance.

**Format**: A single table, updated weekly, capturing the six core KPIs against their baseline (Day 0) and their current rolling target. This view goes at the top of the weekly CHECKIN.md entry.

| KPI | Day 0 Baseline | Current Count | 30-Day Target | 90-Day Target | Status |
|-----|---------------|---------------|---------------|---------------|--------|
| Institutional contacts engaged (replied or routed) | 0 | — | 10+ | 30+ | — |
| Tier A/B framework citations (vocabulary marker confirmed) | 0 | — | 0–2 | 3–8 | — |
| AG offices with confirmed awareness | 0 | — | 2–4 | 6–10 | — |
| Law school faculty with confirmed engagement | 0 | — | 2–4 | 6–10 | — |
| Think tank organizations engaged | 0 | — | 2–4 | 8–12 | — |
| Open/reply rate on most recent outreach batch | 0% | — | 12–18% open | — | — |

**Status coding**:
- **On Track**: Current count is at or above the linear interpolation between Day 0 and target.
- **Watch**: Current count is 50–80% of interpolated target; no corrective action yet, but next batch should adjust.
- **Action Required**: Current count is below 50% of interpolated target; consult Metric 5 contingency triggers in `phase-1-baseline-metrics.md`.

**Time to populate**: Fill each "Current Count" cell from DISTRIBUTION_EXECUTION_LOG.md. No external lookups required for this view.

---

### View 2: Institutional Tier Breakdown (Weekly — 10 minutes)

**Purpose**: Track engagement by institutional sector to identify which sectors are converting and which are lagging.

**Format**: One row per institutional tier. Updated weekly from the contact log.

| Tier | Total Targets | Contacted | Engaged (replied/routed) | Citation Event | Attribution Event |
|------|--------------|-----------|-------------------------|----------------|------------------|
| Tier 1A — State AGs (6 primary) | 6 | — | — | — | — |
| Tier 1B — Top think tanks (5 primary) | 5 | — | — | — | — |
| Tier 1C — T14 law school faculty (Batch 1-2) | 10 | — | — | — | — |
| Tier 2A — AG offices (16 secondary) | 16 | — | — | — | — |
| Tier 2B — Think tanks (6 secondary) | 6 | — | — | — | — |
| Tier 2C — Law school faculty (broad) | 37 | — | — | — | — |
| Tier 3 — Social/Substack/Reddit reach | N/A | — | Subscribers | Shares | — |

**Definitions**:
- **Contacted**: Email sent or Substack post live.
- **Engaged**: Reply received, or contact confirms routing to a colleague or team.
- **Citation Event**: Contact uses framework vocabulary or analytical structure in published work.
- **Attribution Event**: Four-test attribution assessment completed in `attribution-measurement-plan.md`; category A, B, or C assigned.

**Why this view matters**: The Phase 2 domain sequencing decision (documented in `phase-2-domain-research-priority-matrix.md`) depends on which institutional sectors are engaging first. If AG offices engage early but law schools lag, Phase 2 domain selection should prioritize litigation-support domains over academic-curriculum domains.

---

### View 3: Domain Performance Heatmap (Monthly — 30 minutes)

**Purpose**: Track which of the 35+ domains are generating the most institutional interest, citation, and engagement. Identifies where Phase 2 research should focus.

**Format**: One row per domain cluster. Updated monthly by reviewing all citation events, email replies, and routing confirmations for domain references.

| Domain Cluster | Domains Included | Engagement Mentions | Citation Events | Attribution Events | Demand Signal Strength |
|----------------|-----------------|--------------------|-----------------|--------------------|------------------------|
| Electoral Architecture | 1, 2, 3, 33, 37 | — | — | — | — |
| Judicial Independence | 6, 35 | — | — | — | — |
| Prosecutorial Weaponization | 29 | — | — | — | — |
| War Powers / Executive Unilateralism | 19f, 28 | — | — | — | — |
| Economic / Trade | 4, 23 | — | — | — | — |
| Civil Service / Congressional Authority | 26, 34 | — | — | — | — |
| Healthcare / Social Provision | 31 | — | — | — | — |
| Higher Education / Academic Freedom | 27 | — | — | — | — |
| AI / Surveillance / Information | 25, 36 | — | — | — | — |
| Phase 2 Candidates (38–41+) | 38+ | — | — | — | — |

**Demand Signal Strength** categories (for the Phase 2 sequencing decision):
- **Strong**: 3+ unsolicited domain mentions or citation events within the measurement window.
- **Moderate**: 1–2 mentions; contacts have engaged but not cited.
- **Weak**: No domain-specific mentions; only framework-general engagement.
- **None**: No engagement with this cluster.

**Reading this view**: Strong demand for Domain 37 but Weak demand for Domain 36 in Month 1–2 tells the orchestrator: (a) election-protection contacts are engaging first; (b) AI governance needs a different contact strategy or is a Month 4+ adoption. This directly informs Phase 2 domain sequencing.

---

### View 4: Measurement Reliability Scoring (Monthly — 20 minutes)

**Purpose**: Track how confident we are that the measurement data is accurate, complete, and actionable — not just whether the numbers look good.

The problem this view solves: it is possible to have a "full" dashboard that is systematically misleading. If citation monitoring is running but the PACER alerts are not set up, the zero in the "AG brief citations" column reflects monitoring failure, not actual absence of citations. This view distinguishes actual zero from unmonitored zero.

**Reliability Score by Measurement Source**:

| Data Source | Setup Status | Last Checked | Coverage | Reliability |
|-------------|-------------|--------------|----------|-------------|
| Email open/click tracking | Not set up / Set up | — | Batch 1 only / All batches | Low / Medium / High |
| Google Alerts ("35-domain") | Not set up / Active | — | Web only | Low / Medium |
| Google Scholar Alert | Not set up / Active | — | Academic | Low / Medium |
| PACER / CourtListener keyword alerts | Not set up / Active | — | Federal courts | Low / High |
| Democracy Docket case tracker | Manual / Subscribed | — | Election law cases | Medium |
| Overton.io alert | Not subscribed / Active | — | Policy documents | Low (if unsubscribed) |
| Weekly manual search: Just Security, Lawfare, Brennan Center | Not done / Done | — | Tier A/B sources | Medium / High |
| Contact reply log (BATCH_1_CONTACT_LOG.md) | Active | — | Batch 1 only | High |
| DISTRIBUTION_EXECUTION_LOG.md | Active | — | All contacts | High |

**Reliability verdict**:
- If 5+ sources are "High" or "Medium/High": dashboard is reliable enough to make tactical decisions.
- If 3–4 sources are "High" or "Medium/High": dashboard is indicative but not complete; note gaps when reporting targets.
- If fewer than 3 sources are "High": dashboard is unreliable; prioritize setup before interpreting numbers.

**The reliability score prevents a common failure mode**: reporting confident numbers from an incomplete monitoring system, then using those numbers to make Phase 2 go/no-go decisions.

---

## Part II: Measurement Cadences — What to Do and When

### Daily Cadence (5–10 minutes, first 30 days only)

During the first 30 days post-launch, daily monitoring catches early adopter signals that would be missed by weekly review.

**Daily checks (Days 1–30)**:
1. Email client: any replies to Batch 1 or Batch 2 outreach? Log in `BATCH_1_CONTACT_LOG.md` or equivalent.
2. Google Alerts inbox: any web mentions of "35-domain" or "democratic renewal proposal"? Log in `DISTRIBUTION_EXECUTION_LOG.md`.
3. Social media: any shares of framework-linked content on Substack, X, Bluesky, Reddit? Log subscriber count and notable shares.

**What does not need daily checking**: PACER, Overton, SSRN. These have minimum lag times that make daily checks irrelevant — the earliest possible PACER signal is 4–6 weeks post-distribution; the earliest SSRN working paper would appear in Month 2 at minimum.

**Daily check threshold**: If a day produces zero engagement after Day 7, that is not a signal — it is normal. The signal threshold for investigation is zero engagement across the first 14 days combined (fewer than 2 total interactions from the full Batch 1 send).

---

### Weekly Cadence (30 minutes, ongoing through Month 12)

**Every Monday (or equivalent weekly anchor)**:

1. Update Summary Dashboard (View 1) — 10 minutes.
2. Update Institutional Tier Breakdown (View 2) — 10 minutes.
3. Manually search Just Security, Lawfare, Brennan Center, Democracy Docket for new publications. Scan for vocabulary markers. Log any citations in `DISTRIBUTION_EXECUTION_LOG.md` — 10 minutes.
4. Write a 3–5 sentence "Week X Status" entry in `CHECKIN.md` using the format: (a) what happened this week; (b) what the numbers say vs. targets; (c) one tactical decision for next week.

**Weekly ritual output**: A single CHECKIN.md entry that serves as the operational record for the entire Phase 1 period. If Phase 1 runs for 12 months, there will be ~52 entries. These entries are the data source for the Phase 1 Impact Assessment at Month 12 and for the Phase 2 go/no-go decision.

---

### Monthly Cadence (90 minutes, Months 1–12)

**First week of each month**:

1. Update Domain Performance Heatmap (View 3) — 30 minutes.
2. Update Measurement Reliability Scoring (View 4) — 20 minutes.
3. Run full manual search across all eight citation databases listed in `phase-1-baseline-metrics.md` Metric 1.1 — 30 minutes.
4. Run PACER / CourtListener search for framework vocabulary in recent filings — 10 minutes.
5. Write the "Month X Attribution Review" — a 300–500 word assessment of what happened this month, which attribution tests were satisfied for any new citations, and what the numbers now imply for Phase 2 timing — 10 minutes.

**Monthly ritual output**: An updated Domain Performance Heatmap and a dated attribution review entry in `DISTRIBUTION_EXECUTION_LOG.md`. These monthly outputs feed directly into the Phase 2 domain sequencing decision.

---

## Part III: Data Sources — Operational Detail

### Email Engagement Metrics

**What to measure**: Open rate (percentage of recipients who opened the email), reply rate (percentage who sent any reply), substantive engagement rate (percentage whose reply indicates domain-level interest, routing, or request for materials).

**Tool options**:
- Free: Mailtrack (Gmail extension) — provides open rate per email; does not provide click tracking.
- Free: HEY email — open rate built-in.
- Paid ($15/month): Superhuman — full open, click, and reply tracking.
- No-tool fallback: Log replies manually in `BATCH_1_CONTACT_LOG.md`; open rate is untracked but reply rate is fully accurate.

**Reliability note**: Email open rates are systematically undercounted after Apple Mail Privacy Protection (iOS 15+) made open-pixel tracking unreliable for roughly 40% of recipients who use Apple Mail. A zero "open rate" from a tool may reflect tracking failure, not non-opening. Reply rate is the only fully reliable email engagement metric.

**Threshold for concern**: Zero replies from all 5 Batch 1 contacts after 14 days. This triggers the Metric 5 contingency protocol in `phase-1-baseline-metrics.md`.

---

### Institutional Adoption Tracking

**What to measure**: Whether a contacted institution uses the framework in a verifiable work product.

**Data sources**:
- **State AGs**: PACER (free public search), CourtListener (free, with full-text search for recent filings), Democracy Docket (election law cases), state AG press release pages (manually reviewed monthly).
- **Think tanks**: Publication mailing lists (subscribe to Brennan Center, Just Security, Lawfare, Protect Democracy newsletters), Google Alerts for institution name + domain keywords.
- **Law schools**: Google Scholar "Cite" alerts for the framework, SSRN new uploads in constitutional law and election law fields, faculty personal pages for syllabi updates.

**Lag time awareness**: AG adoption signals appear fastest (4–8 weeks), think tank signals appear in 2–6 weeks for blog posts and 3–12 months for reports, law school signals appear in 2–8 weeks for syllabi and 6–18 months for publications.

**Logging protocol**: Every adoption event, regardless of source, is logged in `DISTRIBUTION_EXECUTION_LOG.md` with: date discovered, institution, contact (if known), domain(s) referenced, attribution test results, and attribution category (A/B/C per `attribution-measurement-plan.md`).

---

### Citation Pipeline Velocity

**What to measure**: The rate at which citations accumulate across Tier A (fast), Tier B (medium), and Tier C (slow) publication sources.

**Citation velocity benchmark** (from `attribution-measurement-plan.md` historical comparisons):
- Month 1–3: 0–5 citations expected (innovator phase).
- Month 4–6: 5–15 citations expected (early adopter phase).
- Month 7–12: 15–30 citations expected (early adopter / early majority transition).

**Below-velocity signal**: If cumulative citations are below the lower bound at Month 3 (fewer than 2 citations), diagnose whether the monitoring system is the problem (Reliability Score view) before diagnosing content failure.

**Above-velocity signal**: If cumulative citations exceed the upper bound at any measurement window — for example, 10+ citations by Month 3 — this is an early adopter acceleration signal. Escalate to Phase 2 domain prioritization immediately; do not wait for Month 6 check-in.

**Tool setup** (one-time, 30 minutes):
- Google Alerts: exact phrase "35-domain democratic renewal" — activates web-crawl alerts within hours of publication.
- Google Scholar alert: author search + keyword combo — activates email notifications for academic citations.
- SSRN email digest for "constitutional law" and "election law" keyword folders.
- CourtListener keyword alert: "35-domain" or "democratic renewal proposal" — activates for federal court filing notifications.

---

### Media Mentions Tracking

**What to measure**: Framework vocabulary appearing in news coverage, opinion pieces, or broadcast media.

**Data sources**:
- Google Alerts (free): broad keyword alerts for "democratic renewal proposal" and "35-domain" — catches most English-language web publications within hours.
- Muck Rack (free tier): media monitoring for political journalists; useful for tracking whether any of the framework's specific figures appear in news stories without explicit attribution.
- Manual scan of the Tier A sources list: Letters from an American (daily newsletter), The Atlantic democracy desk (weekly), MSNBC online articles (relevant shows: Rachel Maddow, Ali Velshi).

**Attribution calibration**: Media mentions are low-weight for academic or policy purposes but high-weight for public discourse reach. A single feature in a Tier A media outlet reaches 10–100x more readers than the cumulative reach of all think tank publications. Log all media mentions but weight them appropriately in attribution assessments.

---

### Framework Mention Detection

**What to measure**: Vocabulary markers appearing in sources that may not have explicit citation — the "used but not attributed" category documented in `attribution-measurement-plan.md`.

**Detection method**: The vocabulary marker test (Test 1 in the attribution framework). Specific phrases to track as Google Alerts:
- "35-domain" (highest specificity)
- "prosecutorial weaponization" as a standalone analytical category (unique to Domain 29)
- "five-vector interference strategy" (if this framing is adopted from Domain 37)
- "hybrid theory" in the OLC/Venezuela war powers context (unique to Domain 28)
- "CISA seven-baseline" in election security context (unique to Domain 37 analysis)

**Why unattributed mentions matter**: Institutional actors — especially AG offices — routinely use research without attribution to protect their independence from appearing to endorse external advocacy work. An AG brief that uses "prosecutorial weaponization" as a standalone analytical category, with the same evidence structure as Domain 29, is a framework adoption event even with no citation. Tracking vocabulary markers catches this category of adoption that citation tracking alone misses.

---

## Part IV: Automation Strategy

### What Can Be Automated

The following monitoring functions are fully automatable with free tools and require zero ongoing manual effort after initial setup (30–60 minutes total):

| Function | Tool | Setup Time | Ongoing Effort |
|----------|------|-----------|----------------|
| Web mention detection | Google Alerts (5 keyword phrases) | 10 minutes | Zero — email notifications |
| Academic citation alerts | Google Scholar alerts | 10 minutes | Zero — email notifications |
| Federal court filing detection | CourtListener keyword alerts | 15 minutes | Zero — email notifications |
| Democracy Docket new case notifications | DD newsletter subscription | 5 minutes | Zero — email notifications |
| Think tank publication notifications | Newsletter subscriptions (5 orgs) | 20 minutes | Zero — email notifications |

**Total automation setup**: 60 minutes on Day 1. After setup, all automated monitoring runs in the background and surfaces in an email inbox. The weekly 30-minute cadence is spent processing those notifications and logging relevant findings.

### What Requires Manual Curation

The following functions cannot be automated and require human judgment:

| Function | Why Manual | Cadence | Time Required |
|----------|-----------|---------|---------------|
| Attribution assessment (4 tests) | Tests 1–4 require judgment about vocabulary novelty, structural convergence, timing plausibility, and counterfactual comparison | Per citation event | 15–30 minutes per event |
| Domain performance heatmap update | Requires reading replies and routing confirmations for domain-level signals | Monthly | 30 minutes |
| PACER amicus brief text review | Alerts catch filings; reviewing brief text for vocabulary markers requires reading | Per alert | 10–20 minutes per brief |
| SSRN working paper relevance assessment | Alerts catch uploads; determining whether a paper uses framework analysis requires reading | Per alert | 10–15 minutes per paper |
| Contact log reply coding | Categorizing replies as substantive vs. acknowledgment vs. routing requires judgment | Per reply | 5 minutes per reply |

**The curation labor budget**: Across a 12-month Phase 1 window, the realistic manual curation time is approximately 2–4 hours per month in the first three months (low citation volume, high setup/calibration work), rising to 4–8 hours per month in Months 4–9 (higher citation velocity, more attribution assessments), then declining to 2–3 hours per month in Months 10–12 (monitoring known channels, preparing Phase 1 Impact Assessment). Total manual curation investment over 12 months: approximately 40–70 hours.

---

## Part V: Success Confidence Scoring

The measurement system itself needs to be assessed for reliability before its outputs can drive Phase 2 decisions. The following confidence scoring protocol prevents the most common error: concluding that Phase 1 is performing weakly when the problem is actually monitoring gaps.

### Confidence Score Components

**Component 1 — Citation Monitoring Coverage (0–3 points)**
- 0 points: No automated alerts set up; monitoring is ad-hoc.
- 1 point: Google Alerts active; no academic or court monitoring.
- 2 points: Google Alerts + Google Scholar alerts active; PACER/CourtListener not set up.
- 3 points: All five automated monitoring tools active (Google Alerts, Scholar, CourtListener, newsletter subscriptions, Overton if available).

**Component 2 — Contact Engagement Tracking (0–3 points)**
- 0 points: No contact log; replies tracked only in email inbox.
- 1 point: Basic contact log with send/reply dates; no systematic coding.
- 2 points: Full contact log with reply coding (substantive/acknowledgment/routing) and domain references.
- 3 points: Full contact log + routing confirmation follow-up (confirmed who contacts passed the framework to).

**Component 3 — Attribution Assessment Completeness (0–2 points)**
- 0 points: Citation events noted but not formally assessed against four-test attribution framework.
- 1 point: Some citations assessed; others noted without attribution category.
- 2 points: Every citation event formally assessed against Tests 1–4; attribution category (A/B/C) assigned; recorded in DISTRIBUTION_EXECUTION_LOG.md.

**Component 4 — Baseline Integrity (0–2 points)**
- 0 points: Day 0 baselines not established before distribution.
- 1 point: Day 0 baselines established but monitoring has drifted from baseline categories.
- 2 points: Day 0 baselines intact; all post-distribution measurements use baseline as denominator.

**Maximum score: 10 points.**

### Confidence Score Interpretation

| Score | Interpretation | Decision Rule |
|-------|---------------|---------------|
| 8–10 | High confidence | Dashboard numbers are reliable. Use them to make Phase 2 go/no-go decisions. |
| 5–7 | Medium confidence | Dashboard is indicative but has gaps. Note specific gaps in Phase 2 decision memo. Fill monitoring gaps before Month 6 review. |
| 3–4 | Low confidence | Dashboard cannot support Phase 2 decisions. Prioritize monitoring setup before next measurement window. |
| 0–2 | Unreliable | Monitoring system is not operational. Phase 2 decision must be delayed until setup is complete. |

**Target**: Reach a confidence score of at least 7 by Day 30. The setup cost is approximately 90 minutes (one-time). An 8-month Phase 1 period with low-confidence measurement is worse than delaying launch by 90 minutes to achieve reliable monitoring.

---

## Part VI: Dashboard Maintenance — Minimal Viable Version

If full dashboard maintenance is not feasible due to time constraints, the following Minimal Viable Version preserves the critical data without the full cadence:

**MVV Maintenance (10 minutes/week)**:
1. Log any replies or routing confirmations received this week in `BATCH_1_CONTACT_LOG.md`.
2. Check Google Alerts inbox; log any framework mentions in `DISTRIBUTION_EXECUTION_LOG.md`.
3. Add one line to `CHECKIN.md`: "Week X: [N] contacts engaged, [N] citations found."

**MVV Monthly (30 minutes)**:
1. Run the eight-source citation search from `phase-1-baseline-metrics.md` Metric 1.1.
2. Update the Summary Dashboard (View 1).
3. Assign attribution categories to any new citation events.

**What the MVV sacrifices**: Domain performance granularity (no heatmap), institutional tier breakdown detail, and real-time citation velocity tracking. The MVV preserves the minimum data needed to make the Phase 2 go/no-go decision at Month 6 and the Phase 1 Impact Assessment at Month 12. If full dashboard maintenance is not feasible through Month 3, switch to MVV rather than abandoning tracking entirely.

---

*Cross-references: phase-1-baseline-metrics.md (Day 0 baselines), attribution-measurement-plan.md (four-test attribution framework and causal windows), DISTRIBUTION_EXECUTION_LOG.md (single data source for all logging), BATCH_1_CONTACT_LOG.md (contact engagement log), CHECKIN.md (weekly status entries).*
