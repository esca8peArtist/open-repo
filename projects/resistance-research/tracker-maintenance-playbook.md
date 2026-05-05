---
title: "Tracker Maintenance Playbook — Keeping Four Trackers Current and Accurate"
subtitle: "Update cadence, role definitions, validation checklists, false positive detection, source maintenance, archival, and escalation matrix"
date: 2026-05-05
status: design-phase
project: resistance-research
purpose: Post-Phase-1 automation infrastructure
cross_references:
  - tracker-automation-architecture.md
  - tracker-data-source-audit.md
  - tracker-dashboard-mockups.md
---

# Tracker Maintenance Playbook

*Created: May 5, 2026. Purpose: Specify the exact operational procedures for maintaining four civil liberties trackers — not generic guidance, but the specific steps, cadences, checklists, and decision rules that keep the data current, accurate, and useful for institutional partners.*

*This document assumes the automation pipeline described in `tracker-automation-architecture.md` is live. Until then, the human-review cadences below apply to manual monitoring.*

---

## 1. Update Cadence Per Tracker

Each tracker has a different cadence because news cycle, source availability, and institutional stakes differ.

### 1.1 First Amendment Suppression Tracker — Daily

**Why daily**: First Amendment incidents move fast. A journalist arrested at a protest on a Monday morning may generate advocacy action, congressional statements, and litigation by Wednesday. A two-day delay means the tracker is behind the news cycle when advocacy partners most need it.

**Daily workflow**:
- **7:00 AM**: Automated pipeline runs overnight poll. Diagnostic report appears in `CHECKIN.md`.
- **7:30 AM**: Researcher reviews auto-approved entries (expected: 1–3 per day). Spot-check one randomly selected entry: verify source URL is live, headline matches actual event.
- **8:00 AM**: Researcher works through review queue (expected: 2–5 items requiring human judgment). Average review time: 4 minutes per entry. Total: 10–20 minutes.
- **End of day**: If a high-confidence, time-sensitive entry has been in review queue for more than 6 hours (e.g., a Supreme Court ruling with First Amendment implications), approve or escalate before end of business.

**Weekly synthesis (Monday morning, 45 minutes)**:
- Review prior week's entries for category patterns (are new case types emerging?)
- Update the tracker's "Lead Finding" section if trend has shifted
- Prepare the weekly text-only partner update (see dashboard mockups Section 6.4)
- Check for flagged entries that need follow-up (cases where a "pending review" or "pending ruling" notation was added)

**Sources monitored daily by the automated pipeline**:
- Press Freedom Tracker API (4x daily)
- CourtListener RECAP — First Amendment query (hourly)
- DOJ USAO RSS — keyword filtered (hourly)
- GDELT — First Amendment filter (every 15 minutes)
- EFF RSS feed (every 6 hours)

---

### 1.2 Environmental Rollbacks Tracker — 2–3x Weekly

**Why 2–3x weekly**: Formal rulemaking (proposed rules, final rules, Federal Register publications) moves at a regulatory pace, not a news pace. The Federal Register publishes Monday through Friday, but a new EPA rulemaking that matters typically generates a week or more of commentary before it needs to be documented. The exception is enforcement data, which can shift quickly.

**Monday/Wednesday/Friday workflow**:
- **9:00 AM**: Automated pipeline has run the Federal Register morning poll (9:00 AM ET, matching the FR's 8:45 AM ET publication). Diagnostic report available.
- **9:15 AM**: Researcher reviews new Federal Register entries filtered to environmental agencies. Expected: 3–15 new items from the Federal Register, of which 1–4 are tracker-relevant.
- **9:30 AM**: Review queue check for Regulations.gov and Earthjustice RSS items that require scope judgment.
- **End of session (45–60 minutes total)**: All pending entries either approved, rejected, or escalated.

**Monthly synthesis (first Monday of each month, 90 minutes)**:
- Pull entry volume statistics for the month
- Identify the 2–3 most consequential rollbacks added that month
- Update the tracker's "Most Consequential Actions" section
- Review Harvard EELP tracker for entries not yet captured in our tracker
- Check all entries marked "[PROPOSED]" — have any moved to [FINAL]? Update status.
- Prepare the monthly institutional briefing (see dashboard mockups Section 3)

**Sources monitored**:
- Federal Register API — EPA + Interior agencies (daily at 9 AM)
- Regulations.gov API — EPA, Interior, NOAA, DOE (twice daily)
- Earthjustice RSS (every 6 hours)
- Harvard EELP change-detection (daily)
- GDELT — environmental regulation filter (every 15 minutes; reviewed 2–3x/week)

---

### 1.3 Police Brutality / Consent Decree Tracker — Daily

**Why daily**: Two distinct types of events have different cadences but both require daily attention. Police use-of-force incidents that result in death or serious injury generate immediate news coverage and may require same-day documentation (particularly when they occur in cities with active consent decrees). Consent decree compliance hearings, court filings, and DOJ Civil Rights actions have a legal cadence but are frequently missed if not monitored systematically.

**Daily workflow**:
- **7:00 AM**: Pipeline diagnostic report in `CHECKIN.md`. Focus attention on any city with an active consent decree: is there a new filing, hearing, or news report?
- **8:00 AM**: Review queue (expected: 2–6 items). Priority order: (1) incidents in cities with active consent decrees, (2) new federal court filings, (3) general use-of-force incidents.
- **Weekly**: Check Law Enforcement Knowledge Lab dashboard for any status changes to consent decrees (termination motions, compliance hearing dates).

**Monthly synthesis (first Monday, 60 minutes)**:
- Update entry counts for each active consent decree city
- Review Pattern documentation (Patterns 1–6 in the current tracker) — is a new pattern emerging that warrants its own section?
- Check FBI crime data updates (quarterly; note when new data expected)
- Prepare monthly briefing for law school clinic partners

**Sources monitored**:
- CourtListener RECAP — § 1983 and consent decree query (hourly)
- DOJ Civil Rights Division press releases RSS (hourly)
- Mapping Police Violence Airtable (daily sync — detect new rows added since last check)
- State AG RSS feeds — CA, NY, MA, MN, WA (every 6 hours)
- GDELT — police violence filter (every 15 minutes; reviewed daily)

---

### 1.4 Prosecutorial Weaponization Tracker — Daily

**Why daily**: This tracker currently has zero automation and the largest data gap. Until the pipeline is live, manual daily monitoring is required. Once the pipeline runs, daily cadence matches the pace at which the DOJ announces new prosecutions — which has been several per week in 2025–2026.

**Note**: The prosecutorial weaponization tracker does not currently exist as a standalone file. Until it is created, its entries should accumulate in a new file `prosecutorial-weaponization-tracker.md`. The initial seeding of this tracker from existing entries in `first-amendment-suppression.md` Section 7 and `litigation-tracker-2026.md` should be completed as a bootstrap task before automation goes live.

**Daily workflow**:
- **7:00 AM**: Pipeline diagnostic. DOJ USAO RSS is the primary signal source — review keyword-filtered press releases for the prior 24 hours.
- **7:30 AM**: Apply the three-question Protect Democracy test to any new prosecution that appears politically relevant:
  - Q1: Was the target identified as political opposition before the DOJ action?
  - Q2: Is the legal theory novel, or has it been applied to non-political actors?
  - Q3: Is there a pattern of similar actions against political opponents?
- **8:00 AM**: Approve, reject, or escalate. Estimated 3–8 entries reviewed daily once pipeline is live.

**Weekly synthesis (Monday, 30 minutes)**:
- Review Protect Democracy Retaliatory Action Tracker for new entries added since last week
- Cross-check Wikipedia "Targeting of political opponents" article edit history for missed entries
- Update running count of total investigations vs. indictments vs. convictions

**Monthly synthesis (first Monday, 75 minutes)**:
- Assess whether the pattern of prosecutorial targeting has shifted (new target categories? new legal theories?)
- Prepare briefing for legal academic partners focused on selective prosecution doctrine
- Review and update the "open questions" section (cases where outcome is unknown)

---

## 2. Role Definitions

Three roles, each with a specific mandate. One person can hold multiple roles, but the responsibilities should be understood as distinct.

### 2.1 Automated Ingestion Engine

**What it does**: Polls sources on schedule, normalizes data, runs scope filter and confidence scoring, submits to deduplication, and either auto-approves (High confidence, established category) or places in review queue (Medium/Low confidence). The engine never makes editorial judgments.

**What it does not do**: Decide whether a novel event is within scope, write descriptions, update trend analyses, or communicate with partners.

**Accountability**: The engine logs every action to the `edits` table. If an entry was auto-approved incorrectly, the log shows when it was ingested, which source it came from, and what confidence logic applied. This is the audit trail.

### 2.2 Human Reviewer (Senior Researcher)

**What they do**: Work through the review queue. For each queued entry: (1) verify source URL is live and matches the described event; (2) apply scope check using the scope definitions in `tracker-automation-architecture.md` Section 3.1; (3) assess whether confidence rating is appropriate; (4) look for duplicates; (5) improve the description if the automated draft is inadequate; (6) approve, reject, or escalate.

**Target throughput**: 8–12 entries per hour. A daily queue of 15 entries should take 90–120 minutes.

**What they do not do**: Change the category taxonomy, modify scope definitions, or make governance decisions — those require the orchestrator.

**Accountability**: Every review action is logged to the `reviews` table with reviewer identity, action taken, and timestamp.

### 2.3 QA Auditor

**What they do**: Once per week, pull a random sample of 10 published entries and verify: (1) source URL still lives; (2) headline accurately describes the event documented at the source; (3) entry is within tracker scope; (4) no closely related entry exists (duplicate missed by deduplication); (5) description provides sufficient context for a non-specialist reader.

**Time required**: 30–45 minutes per weekly audit.

**Output**: A brief log entry in `CHECKIN.md` under the weekly QA header, flagging any issues found and whether they were corrected immediately or require follow-up.

**Threshold**: If the QA sample reveals more than 2 errors in 10 entries (20% error rate), treat as a quality alarm: pause auto-approvals until the source of errors is identified and corrected.

---

## 3. Validation Checklist (Human Review)

Use this checklist for every entry in the review queue. Each item is binary (pass/fail). If any item fails, do not approve — either fix the issue and re-check, or reject with a reason noted.

```
ENTRY VALIDATION CHECKLIST

Entry ID: ____________  Tracker: ____________  Date reviewed: ____________

[ ] 1. Source URL resolves (not 404, not paywalled without a cached version)
[ ] 2. Headline matches the actual event described at the source URL
[ ] 3. Date field reflects the date of the underlying event, not the date the source published
       (Some news sources publish days after an incident — verify against earliest source)
[ ] 4. Event falls within tracker scope (use scope definition in tracker-automation-architecture.md
       Section 3.1; if uncertain, consult the scope definition document or escalate)
[ ] 5. Confidence rating is appropriate:
       - Source is government/judicial document → can be High
       - Source is established watchdog → Medium or High with corroboration
       - Source is news media only → Medium maximum
       - Source is single outlet, unconfirmed → Low
[ ] 6. No duplicate exists (search existing entries for same event by:
       a. Same defendant/subject name
       b. Same date + same city
       c. Similar headline keywords)
[ ] 7. Description provides sufficient context: a reader unfamiliar with the tracker's focus
       should be able to understand what happened, who did it, and why it matters
[ ] 8. Category is correctly assigned from the taxonomy
       (If event does not fit any existing category, flag for taxonomy expansion — do not create
       ad hoc categories without orchestrator approval)
[ ] 9. State field is correct (2-letter code, or 'federal' for federal actions)
[ ] 10. All source URLs are included (if event appeared in 3 sources, all 3 should be in
        the entry_sources table, not just the first one found)

DECISION:
[ ] Approve and publish
[ ] Approve with edits (describe changes made below)
[ ] Reject (reason: _____________________________)
[ ] Escalate — needs legal expertise (describe issue: _________________)
[ ] Mark as duplicate of entry ID: ____________

Notes: ___________________________________________________________________
```

---

## 4. False Positive Detection

False positives — entries that pass the automated scope filter but are actually outside scope — are the most damaging data quality issue. They erode partner trust. The following procedures catch them before they accumulate.

### 4.1 Per-Entry False Positive Indicators

An automated entry is more likely to be a false positive if:
- The source is GDELT and the keyword match is a single common term (e.g., "press" in a sports article)
- The headline contains one tracker keyword but also contains common false-positive phrases: "opinion," "commentary," "editorial," "review," "analysis," "prediction"
- The `state` field is populated as a foreign country (GDELT ingests international news; most tracker events are U.S. only)
- The date is more than 30 days in the past (may indicate GDELT re-circulating old articles)

The validation engine should flag these indicators and apply an automatic confidence downgrade of one level before queuing for review.

### 4.2 Per-Source False Positive Rate Monitoring

Track false positive rate by source, calculated as: (entries rejected from source / total entries from source) over a rolling 30-day window.

```sql
SELECT 
    s.source_name,
    COUNT(*) as total_entries,
    SUM(CASE WHEN r.action = 'rejected' THEN 1 ELSE 0 END) as rejections,
    ROUND(SUM(CASE WHEN r.action = 'rejected' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) 
        as false_positive_rate
FROM entry_sources s
JOIN reviews r ON r.entry_id = s.entry_id
WHERE s.added_at >= date('now', '-30 days')
GROUP BY s.source_name
ORDER BY false_positive_rate DESC;
```

**Action thresholds**:
- FP rate < 10%: Normal. No action.
- FP rate 10–25%: Review the source's keyword filter rules. Tighten if possible.
- FP rate 25–50%: Require double human review for all entries from this source (two reviewers must independently approve).
- FP rate > 50%: Suspend the source from automated ingestion. Move to manual-only monitoring. Investigate root cause before re-enabling.

### 4.3 Monthly Audit (Full-Sample Check)

On the first Monday of each month, the QA auditor pulls a random sample of 20 published entries (not the usual 10) to assess the false positive rate at the published layer — meaning entries that passed both automation and human review.

If the audit finds > 2 out of 20 entries (10%) are false positives or have significant accuracy issues, this triggers a quality review meeting and a re-examination of the validation checklist and scope definitions.

---

## 5. Source Maintenance

### 5.1 Monthly Checks

On the last business day of each month:

1. **Verify API credentials are valid**: For each source that requires authentication (CourtListener token, data.gov API key, PACER login, MuckRock API key), make a test API call and confirm a 200 response.
2. **Check source coverage**: Pull entry counts by source for the month. If a source that previously contributed 5+ entries per month contributes 0, investigate:
   - Did the source change their API schema?
   - Did the keyword filter become too restrictive?
   - Is the source simply slow (FOIA results, academic publications)?
3. **Log results**: Update the `source_health_log` table with the monthly check results.

### 5.2 Quarterly Reviews

On the first Monday of January, April, July, and October:

1. **Rate limit review**: Check whether any source's rate limits are being hit (look for 429 response codes in the ingestion log). If hitting limits, either reduce polling frequency or upgrade the API tier.
2. **Source quality review**: For each source, compute the 90-day FP rate, coverage rate (% of known events captured vs. missed), and freshness lag (average time between event and ingestion). Update the priority ranking table in `tracker-data-source-audit.md`.
3. **New source evaluation**: Review the Exploration Queue for any new sources identified in the past quarter. Apply the priority ranking criteria from the audit document and schedule implementation if score > 38.
4. **Deprecation decision**: If a source has FP rate > 40% for two consecutive quarters, deprecate it. Create a transition plan to a replacement source before shutting down the failing source.

### 5.3 Source Reliability Floor

If a source's reliability (measured as: successful polls / total attempted polls over 30 days) drops below 90%, implement a backup procedure:

- Identify the nearest-equivalent alternative source from `tracker-data-source-audit.md`
- Enable the backup source at reduced priority (Medium confidence for all entries regardless of source tier)
- Document the transition in `source_health_log`
- Set a 30-day review to either restore the primary or formally transition to the backup

---

## 6. Data Archival

### 6.1 Retention Policy

All tracker entries are kept indefinitely. Historical data is valuable for:
- Trend analysis (how has the rate of press freedom violations changed over time?)
- Legal documentation (longitudinal record is admissible in pattern-or-practice litigation)
- Academic research (researchers need multi-year datasets)
- Accountability (can the administration demonstrate any improvement?)

No entry is ever deleted from the database. Entries that are found to be errors are marked `is_published = FALSE` and given a rejection reason — but the entry record and its full history remain in the database.

### 6.2 Version Control for Edited Entries

Every edit to a published entry is tracked in the `edits` table. This means: if a researcher corrects a date, adds a new source URL, or updates the description after a court ruling, the original version is preserved as a row in `edits`. This prevents the loss of the historical record.

```sql
-- Example: update an entry date (captured in edits table)
INSERT INTO edits (entry_id, field, old_value, new_value, edited_by, reason)
VALUES ('a3f2b1c4', 'date', '2026-04-20', '2026-04-21', 'researcher', 
        'DOJ press release confirms April 21 as indictment date, not April 20 as initially reported');

UPDATE entries SET date = '2026-04-21' WHERE id = 'a3f2b1c4';
```

### 6.3 Backup Schedule

- **Daily**: The SQLite database file is backed up to a designated Google Drive folder using `rclone`. Backup includes: `tracker.db`, the raw ingestion log (JSON files from each source), and the `CHECKIN.md` file. Total daily backup size estimate: 5–20 MB.
- **Weekly**: A full CSV export of all four trackers is generated and stored in Google Drive under `backups/YYYY-WW/`.
- **Monthly**: A snapshot is pushed to a private GitHub repository as a tagged release, enabling version-pinned citations by research partners.

**rclone backup command** (add to cron or systemd timer, daily at 2 AM):
```bash
rclone sync /path/to/tracker.db gdrive:resistance-research/backups/daily/
rclone sync /path/to/raw_logs/ gdrive:resistance-research/backups/raw/
```

---

## 7. Community Contributions (Optional Future Feature)

If the trackers are opened for community submissions (submitted by journalists, lawyers, activists, and community members), the following procedures apply. **This feature is NOT enabled by default.** It should only be activated after the automated pipeline is stable and a reviewer has consistent capacity to handle the additional volume.

### 7.1 Submission Requirements

Community submissions must include:
- **Required**: Headline, date of event, state/jurisdiction, at least one source URL, category selection from the taxonomy
- **Required**: Submitter contact information (not published; used for verification only)
- **Optional**: Additional context, additional URLs, tag suggestions

Submission form built on Datasette's `datasette-insert-api` plugin or a simple Netlify form.

### 7.2 Submission Review Process

Community submissions are treated identically to Low-confidence automated entries:
- Never auto-approved
- Require full human validation checklist
- Source URL must be independently verified
- Submitter may be contacted for additional information
- If approved, credited as: "Submitted by community contributor" (not by name unless submitter requests attribution)

### 7.3 Moderation Policy

Reject community submissions that:
- Duplicate an existing entry without adding new information
- Are out of scope (wrong tracker, or event is not a civil liberties issue)
- Are based on rumor, social media, or unverified claims without a credible source URL
- Are about events outside the United States without a clear U.S. nexus
- Appear to be submitted in bad faith (promoting a political narrative without factual basis)

Submitters whose submissions are consistently rejected receive a notice and are removed from the submission whitelist.

### 7.4 Incentives for Quality Contributors

After the feature is live for 3 months, review contributor patterns:
- Top contributors (by volume of approved, accurate submissions) are acknowledged in the monthly partner briefing ("Community Contributors This Month")
- High-quality contributors are invited to join the reviewer pool
- Exceptional contributions (unique discoveries that would have been missed by automated monitoring) are noted in the lead finding section of the relevant monthly briefing

---

## 8. Escalation Matrix

When something goes wrong, this matrix determines who is responsible and what action to take.

| Situation | First Responder | Action | Escalation If Unresolved |
|-----------|---------------|--------|--------------------------|
| Entry scope is ambiguous — cannot determine if it qualifies | Human reviewer | Forward to researcher with legal expertise for a 24-hour turnaround | If no response in 48h, default-reject with "pending" notation; revisit next week |
| Source quality has degraded (FP rate > 25%) | QA auditor | Review and tighten keyword filters; document in source_health_log | If FP rate not improved in 7 days, suspend source; notify orchestrator |
| Source is unreachable for > 2 polling cycles | Automated alert → researcher | Investigate: is the source's website down? Has API endpoint changed? | If source unreachable > 48 hours, activate backup source; notify orchestrator |
| Review queue backlog > 50 items | Researcher | Triage: auto-approve High-confidence items that meet all auto-approve criteria; escalate if needed | If backlog > 100 items, temporarily reduce freshness targets: pause Medium and Low confidence items, process High only |
| Institutional partner feedback (requests more/different coverage) | Researcher | Document request in `CHECKIN.md` under "Partner Feedback"; assess against tracker scope | If request requires scope expansion, bring to orchestrator for decision |
| Auto-approved entry found to be factually wrong post-publication | QA auditor | Immediately mark `is_published = FALSE`; add note to entry; investigate source of error | If same source caused multiple errors: suspend source; notify orchestrator |
| Possible legal sensitivity (entry names a private individual in a potentially defamatory context) | Reviewer | Flag immediately; do not approve; escalate to researcher with legal background | If no response in 24h, default-reject. Never publish legally risky entries without explicit approval. |
| Overwhelming volume of entries — more than 3x normal daily volume | Researcher | Spot-check first 10 entries from each source for false positives before approving; alert orchestrator | If spike is from a real civil liberties escalation (not data error), document it as a "surge event" in `CHECKIN.md` |
| Partner asks for data to be used in litigation | Orchestrator | Consult on data provenance, edit history, and source attribution before authorizing. Confirm all cited entries have verifiable sources. | If litigation use requires expert testimony about data methodology, escalate to academic partnership |

---

## Quick Reference Card

For the researcher doing daily maintenance, this is the abbreviated version:

**Every day**:
1. Check `CHECKIN.md` for the pipeline diagnostic
2. Review queue: approve, reject, or escalate all queued items
3. Spot-check one auto-approved entry (random)
4. If review queue > 30 items, triage using the escalation matrix

**Every week**:
1. Synthesize the week's entries for the weekly partner update
2. Run the 10-entry QA spot-check
3. Update "lead finding" if trend has shifted
4. Note any entries with pending outcomes (awaiting court ruling, etc.) and whether updates are available

**Every month**:
1. Generate monthly briefings (automated)
2. Run the 20-entry full QA audit
3. Verify all API credentials
4. Check source FP rates; adjust filters if needed
5. Review open research threads in `PROJECTS.md` for tracker-adjacent developments

**Every quarter**:
1. Full source quality review
2. Rate limit audit
3. Evaluate new source candidates
4. Assess scope definitions — do they need updating given new patterns of suppression?

---

*References: [Datasette documentation](https://datasette.io/) | [Protect Democracy three-question test](https://protectdemocracy.org/work/retaliatory-action-tracker/) | [WCAG 2.1 validation](https://www.w3.org/WAI/WCAG21/quickref/) | [rclone documentation](https://rclone.org/docs/) | [tracker-automation-architecture.md] | [tracker-data-source-audit.md]*
