---
title: "Tracker Measurement Framework"
subtitle: "How to measure tracker impact on Phase 1 distribution — attribution signaling, institutional feedback, success metrics, and measurement infrastructure"
date: 2026-05-06
status: complete
phase: phase-2-preparation
project: resistance-research
purpose: Phase 2 enrichment strategy — operational by month 2 post-Phase-1-launch
cross_references:
  - tracker-source-audit-detailed.md
  - tracker-automation-feasibility.md
  - tracker-visualization-prototype-specs.md
  - measurement-and-iteration-framework.md
  - phase-1-measurement-dashboard-spec.md
---

# Tracker Measurement Framework

*Created: May 6, 2026. This document establishes how to determine whether the four trackers are doing what they are supposed to do. The target audience is the solo operator who needs to know, 60 days after Phase 1 distribution, whether the trackers are generating institutional utility or are being filed and ignored. All metrics here are operational within month 2 — no "someday" research infrastructure.*

**Lead finding**: The hardest measurement problem for these trackers is not counting views or downloads — it is determining whether the tracker changed a decision or prevented a harm that would otherwise have occurred. This document takes a deliberately modest position: measure what is measurable (citation signals, access patterns, direct feedback) and establish conservative success thresholds rather than aspirational ones. A tracker that is cited twice in institutional advocacy materials within 60 days of distribution is working; it does not need to produce a viral moment.

---

## 1. Attribution Signaling — How to Know the Tracker Is Being Used

Attribution for civil liberties reference documents is structurally different from attribution for research reports. Institutional users cite tracker data in their own filings, testimony, and advocacy materials — not necessarily with a link or formal citation. The measurement problem is that the most valuable uses are the least visible ones.

### 1.1 Direct Citation Signals (Measurable Automatically)

**Web traffic analytics**: If trackers are hosted on a public URL (GitHub Pages, Substack, Datasette), basic Google Analytics or Plausible (privacy-respecting alternative, $9/month, no data sales) shows visits, visitor locations (country/state level), time on page, and referrer source. This is the baseline.

**PDF download tracking**: If PDFs are distributed via a link (e.g., a bit.ly or GitHub release URL), click tracking provides a download count. If emailed as attachments, download tracking is not available. For the Phase 1 distribution context (email to ~50–100 institutional contacts), a simple tracking spreadsheet (who received which PDF, did they respond or forward) substitutes for analytics.

**Search result inclusion**: Once trackers are publicly hosted, monitor for their appearance in search results for key query terms ("police consent decree tracker 2026," "EPA rollback list 2026," "first amendment violations journalist"). Tools: Google Search Console (free), manual periodic searches. Target: appearing on page 1 for 2–3 high-intent queries within 90 days of publication.

**Backlinks**: If any external websites link to the trackers, this is a strong attribution signal. Tools: Ahrefs (expensive) or Moz (has a free tier for limited backlink monitoring). More practically: Google Alerts for the tracker URLs detects most web mentions.

### 1.2 Secondary Attribution Signals (Require Active Monitoring)

**Media mentions**: Set up Google Alerts for the specific tracker names and for distinctive phrases from the tracker text (e.g., "three-quarters of consent decree provisions remain unmet" is a distinctive finding unlikely to appear identically in other sources). An exact-phrase match in a news article or advocacy publication is a citation signal.

**Academic and legal citation**: Google Scholar citation tracking (free) and CourtListener case citation search (free) can detect if tracker language appears in briefs, law review articles, or court opinions. This is a lagging indicator — legal citation takes 6–18 months to appear in searchable form. Set a reminder to run this check at 6 months and 12 months post-launch.

**Congressional and legislative use**: Set up a search in the Congressional Record API (GovInfo `CREC` collection) for the tracker names and distinctive findings. Congressional staff write floor statements and testimony that sometimes incorporate external tracking data without formal citation.

**Direct feedback from institutional contacts**: The most reliable attribution signal for Phase 1 distribution is direct response from the contacts who received the material. If a law school clinic says "we used the consent decree compliance data in our amicus brief," that is a high-quality attribution signal regardless of whether the brief formally cites the tracker.

### 1.3 Attribution Red Flags

**Zero response after 30 days**: If no institutional contact in the Phase 1 distribution list has responded (replied, forwarded, acknowledged receipt, or cited the tracker in any way) within 30 days, the distribution method may be the problem rather than the content. Escalate: send a targeted follow-up to 3–5 high-priority contacts with a specific question ("Would this tracking format be useful for your current docket?").

**High traffic, zero engagement**: If the tracker URL shows high visit counts but very short average session duration (under 30 seconds), users are landing and leaving immediately. This indicates a presentation problem — the tracker is not surfacing its key findings quickly enough. Response: redesign the document header to lead with the most important current finding.

**Download without engagement**: If the PDF is being downloaded but no responses or citations are appearing, the content may be reaching the wrong contacts or the right contacts at the wrong time. Measure: compare distribution date to known advocacy calendar moments (comment periods, scheduled hearings, consent decree monitoring deadlines).

---

## 2. Institutional Feedback Integration

### 2.1 Feedback Collection Template

Every institutional contact who receives Phase 1 distribution should receive one brief follow-up survey at 30 days post-distribution. The survey must be short enough that a busy lawyer or advocate will actually complete it.

**Three-question user survey**:

> Thank you for receiving the resistance-research tracker materials. Three quick questions (2 minutes):
>
> **Question 1**: Have you consulted any of the four trackers (First Amendment, Environmental, Police Brutality, Prosecutorial Weaponization) in your work in the past 30 days?
> ○ Yes — in active work  ○ Yes — for background  ○ No, not yet  ○ Received but haven't had time
>
> **Question 2**: For any tracker you have used: which one, and what were you trying to find? (Free text, optional)
>
> **Question 3**: What would make the trackers more useful to you?
> ○ More frequent updates  ○ Different categories  ○ Different format  ○ Different geographic coverage  ○ Better cross-referencing with litigation  ○ Other: _______

**Distribution method**: Plain-text email, not a survey tool that requires login. Some institutional contacts have strict data policies that prevent them from completing third-party surveys. Plain email means the response lands in your inbox and can be logged manually.

**Response target**: 20–30% response rate from initial Phase 1 distribution contacts. If response rate is below 10%, the distribution list may not be reaching active users.

### 2.2 Feedback Integration Protocol

Feedback is useless without a clear protocol for acting on it. The following rules apply:

**Immediate action (within 1 week of feedback)**:
- If a specific entry is reported as inaccurate: verify the cited sources, correct if necessary, note the correction in the entry
- If a contact requests a category that does not exist: assess whether it fits within the tracker's scope; if yes, create a placeholder entry and note it as "queued for research"

**Monthly synthesis (first Monday of each month)**:
- Aggregate all feedback received in the prior month
- Identify the top 2–3 patterns: what are users looking for that the trackers don't currently provide?
- Select one actionable change for the next monthly cycle: a new category, a different format element, a new source added

**Quarterly category review**:
- Are the current category taxonomies still accurate? (Prosecutorial weaponization cases that initially looked like "civil society targeting" may actually be better characterized as "press suppression" as cases develop)
- Are there emerging patterns that need a new category? (The SPLC indictment created a new "civil rights organization prosecution" category that did not exist in April 2025)
- Review the tracker lead findings: do they still accurately describe the current state, or have they been superseded by developments?

### 2.3 Red Flags Indicating Tracker Failure

The following signals indicate that a tracker is not performing its function and requires intervention:

**Structural failure signals**:
- Six weeks without an entry update (tracker has gone stale)
- An entry remains "status: pending" for more than 90 days without any update notation (case has developed but entry was not updated)
- A major incident in the tracker's domain is covered by national news but does not appear in the tracker within 7 days

**Quality failure signals**:
- Any source URL in an active entry returns 404 (source has moved or been deleted)
- A court ruling "pending" notation remains in place after the court has issued its decision
- Compliance percentages for tracked cities are more than 6 months old (monitoring reports have been filed but not incorporated)

**Impact failure signals**:
- 90 days post-distribution with no attribution signals of any type (no citations, no traffic, no feedback)
- Institutional contacts report using a competitor resource (DOJ tracker, Earthjustice tracker, etc.) for needs the tracker should be meeting

When any failure signal is detected, the response is not to rebuild the tracker from scratch — it is to identify the specific gap and address it. Most failure signals point to a maintenance cadence problem (stale entries) or a distribution audience mismatch (reaching the wrong contacts).

---

## 3. Success Metrics Per Tracker

These thresholds are conservative and achievable within 60–90 days of Phase 1 launch.

### 3.1 First Amendment Suppression Tracker

**Primary success metric**: Reduction in undetected suppression events. The current estimated miss rate is 30–40% of nationally significant events. Success = reducing this miss rate below 15% through improved monitoring.

**How to measure**: Perform a monthly retrospective comparison — look back 30 days and verify that every significant First Amendment event covered by RCFP, CPJ, and national news was in the tracker within 7 days of occurrence. If the retrospective audit finds events that were not in the tracker within 7 days, that is a miss.

**Target by month 2**: Fewer than 2 missed events per month (events that required retroactive adding after more than 7-day lag).

**Secondary success metric**: If tracker reduces undetected suppression events from the estimated "5–7 nationally significant events per week" to "fewer than 2 per week that require retroactive entry," monitoring is working.

**Institutional success signal**: Any civil liberties organization (ACLU, CPJ, FPF, RCFP, PEN America, EFF) acknowledges or cites tracker data in their own publications. This is the single strongest validation signal — these organizations are the reference standards for this topic. If they point to the tracker as a useful resource, it has achieved institutional credibility.

**Measurement infrastructure**: Google Alerts for tracker-distinctive phrases; monthly retrospective audit (30 minutes); quarterly outreach to ACLU/FPF/RCFP contacts for feedback.

### 3.2 Environmental Rollbacks Tracker

**Primary success metric**: If tracker prevents duplicate litigation effort — same rollback being challenged twice by different organizations without coordination.

**How to measure**: This is inherently difficult to measure directly (averted events are invisible). Proxy measure: if advocacy organizations and law school clinics that receive the tracker distribution report using the litigation status column to avoid duplicating cases already in court, the tracker is performing this function. The 30-day feedback survey should specifically ask: "Have you checked the environmental rollbacks tracker before filing a challenge to determine whether a challenge is already pending?"

**Target by month 2**: At least 3 institutional contacts report using the litigation status field to inform filing decisions.

**Secondary success metric**: Federal Register API automation (once implemented per the automation feasibility plan) should produce tracker entries within 48 hours of EPA Federal Register publication. Current baseline: 1–7 day lag. Target: under 48 hours for any final rule.

**How to measure freshness**: Timestamp comparison — record the Federal Register publication date and the tracker entry date for every entry added after automation is live. Calculate the rolling average lag. Target: under 2 days.

**Institutional success signal**: Harvard EELP tracker or Earthjustice litigation page cites or links to the environmental rollbacks tracker. These are the reference standards for this domain.

**Measurement infrastructure**: Google Alerts; freshness log (simple spreadsheet tracking entry dates vs. event dates); quarterly comparison of tracker coverage against EELP tracker to identify gaps.

### 3.3 Police Brutality / Consent Decree Tracker

**Primary success metric**: If tracker enables faster state AG response to post-DOJ-withdrawal enforcement gaps.

**Operational definition**: After the May 21, 2025 DOJ withdrawal, the state AGs of California, New York, Illinois, Massachusetts, Minnesota, and Washington are the primary remaining federal accountability actors for police consent decrees. If any of these AGs opens a new pattern-or-practice investigation in a city that appears on the tracker as having lost federal oversight, the tracker has contributed to the policy ecosystem that made that response possible.

**Measurement caveat**: Proving causation (the tracker caused the AG action) is impossible. The relevant proxy measure is: did the AG cite the tracker? Did an advocacy organization that received the tracker brief the AG? If yes, the causal chain is plausible.

**Target by month 2**: At least one state AG office acknowledges receiving or reviewing the tracker data, OR one advocacy organization briefs a state AG using tracker data.

**Secondary success metric**: Chicago compliance percentage documentation is current within 30 days of each independent monitor report filing. Current performance: monitor reports are sometimes captured weeks after filing. Target: new monitor report incorporated within 7 days of PACER filing.

**How to measure compliance data freshness**: CourtListener docket monitoring (once implemented) will produce automated alerts within 24 hours of new monitor report filings. Freshness = time from PACER filing to tracker entry. Target: under 7 days.

**Institutional success signal**: Any civil rights law school clinic (NYU, Georgetown, UCLA, University of Chicago) uses tracker compliance data in a brief or advocacy filing. These clinics are the most active users of consent decree compliance documentation.

**Measurement infrastructure**: Google Alerts for tracker-distinctive phrases; monthly Chicago compliance update check; quarterly outreach to civil rights clinic contacts.

### 3.4 Prosecutorial Weaponization Tracker

**Primary success metric**: If tracker provides early-warning function for activists — flagging prosecution patterns before they become a crisis for targeted organizations.

**Operational definition**: An activist or civil society organization reads the tracker before receiving a subpoena or indictment and takes preparatory action (establishing legal relationships, reviewing their own records retention, documenting their practices) that reduces their exposure. This is an inherently difficult signal to capture — organizations that benefited from early warning will not publicize that they were worried about prosecution.

**Proxy measure**: How often does the tracker flag a new entry before the targeted organization's own communications department issues a statement? If the tracker has the prosecution listed before the organization tweets about it, the monitoring is working faster than the organization's own crisis communications.

**Target by month 2**: For any prosecution that is subsequently covered nationally, tracker entry should appear within 72 hours of DOJ press release issuance. Current baseline: events surface through national news, typically 48–96 hours after announcement. Target: within 24 hours for any USAO press release after DOJ RSS monitoring is implemented.

**Secondary success metric**: The tracker contributes to the pattern analysis documented in domain-29. If new cases after tracker activation continue to confirm the 22-case pattern (same structural elements, same legal theory families, same target categories), the tracker is providing evidentiary foundation for the systemic argument.

**How to measure pattern confirmation**: Quarterly review of new tracker entries against the three-question pattern test: (1) target pre-identified as opposition? (2) legal theory without precedent? (3) pattern of similar actions? If 70%+ of new entries score positive on 2 of 3 questions, the pattern is confirmed.

**Institutional success signal**: A defense attorney in a politically targeted case cites the tracker's pattern analysis in a vindictive prosecution motion. This is the highest-value institutional use of this tracker — it converts pattern documentation into a legal argument.

**Measurement infrastructure**: Google Alerts; CourtListener search for filings citing "prosecutorial weaponization" or similar phrases; DOJ RSS monitoring freshness log (entry date vs. DOJ press release date); quarterly pattern test review.

---

## 4. Measurement Infrastructure — What to Track in Real-Time vs. Quarterly

### 4.1 Real-Time (Daily or Automated)

These metrics require no human action — they are byproducts of automated monitoring once the pipeline is live:

- **Tracker entry freshness** (automated): Timestamp every entry's `date_of_event` vs. `date_entered`. Alert if lag exceeds 7 days for any new entry.
- **Source URL validity** (automated): Weekly automated check of all source URLs in tracker entries for 404 errors. Log broken links for human correction.
- **Traffic analytics** (automated): If hosted on a public URL, daily visitor counts accumulate automatically. No human action required; review monthly.
- **DOJ RSS monitoring** (automated once implemented): Tracks how many USAO press releases are ingested and how many pass keyword filters. This is a pipeline health metric, not a tracker quality metric.

### 4.2 Weekly (Human Review Required)

- **Entry review queue**: Review the automated signal queue for each tracker (estimated: 15–30 items per week across all four trackers once automation is live). Approve, reject, or queue for further research.
- **Broken link scan results**: Address any 404 errors from the automated scan. Target resolution: within 48 hours of detection.
- **Pattern alert assessment**: Any new entry in the prosecutorial weaponization tracker triggers a pattern-test assessment (30 minutes/entry).

### 4.3 Monthly (Human Synthesis)

- **Retrospective miss audit**: For each tracker, review the prior 30 days for events that should have been in the tracker but weren't. Count misses. Track miss rate over time.
- **Freshness calculation**: Calculate average lag for entries added in the prior 30 days. Compare to baseline. Is automation reducing lag as expected?
- **Feedback synthesis**: Aggregate any feedback received from institutional contacts. Identify the top pattern. Make one targeted improvement.
- **Lead finding review**: Is the tracker's lead finding still accurate? If the political/legal landscape has shifted significantly, the lead finding should be updated.

### 4.4 Quarterly (Comprehensive Review)

- **Category taxonomy review**: Are existing categories still adequate? Any new patterns requiring new categories?
- **Source audit**: Are all current sources still active? Any sources that have become less reliable? Any new sources (from the source audit document) ready to add?
- **Competitive landscape check**: Have other organizations launched trackers that cover the same ground? If yes: does the tracker offer something distinct? Should it link to and cross-reference the other tracker rather than duplicating it?
- **Attribution search**: Google Scholar search for tracker citations; CourtListener search for brief citations; Congressional Record search for legislative mentions. Log all findings.
- **Phase 2 routing decision**: If the tracker is demonstrably useful (attribution signals, positive feedback, freshness improving), prioritize automation investment. If usage signals are weak after 90 days, diagnose before investing further.

---

## 5. Phase 2 Routing Implications

The measurement framework connects directly to Phase 2 decisions. Use these thresholds:

**Proceed to Phase 2 automation (full investment)**:
- At least 3 attribution signals (citations, feedback, institutional acknowledgment) within 90 days
- At least 10% response rate on 30-day feedback survey
- At least one institutional contact reports using the tracker data in active work

**Pause and diagnose (hold Phase 2 investment)**:
- Zero attribution signals at 60 days
- Response rate below 5% on 30-day feedback survey
- Multiple feedback responses indicating wrong framing or wrong audience

**Pivot to different format**:
- Feedback consistently indicates tracker format is the problem (too long, not filterable, wrong entry structure)
- Traffic data shows short session duration (under 45 seconds)

**Retire the tracker**:
- Phase 1 contacts report that an equivalent resource already exists from a more authoritative source (ACLU, EFF, Harvard EELP for the relevant domain)
- In this case, the right move is to link to the authoritative source and redirect resources to trackers where a gap actually exists

---

*This measurement framework integrates with and extends `measurement-and-iteration-framework.md` (created Session 546) which covers the broader post-distribution measurement infrastructure for the full democratic-renewal-proposal distribution. The tracker-specific metrics here are a subset of that larger framework, with tracker-specific thresholds, feedback questions, and success definitions calibrated to the institutional audience for legal and advocacy reference materials.*
