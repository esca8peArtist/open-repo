---
title: "Phase 1 Adoption Tracking — Deployment Guide"
created: 2026-06-01
version: 1.0
status: production-ready
trigger: Deploy morning of June 3, immediately after Domain 39 distribution window closes
scope: >
  Complete operational guide for deploying phase-1-adoption-tracking-script.py,
  configuring Gmail OAuth2 and GitHub API access, setting up the Google Sheets
  tracking workbook, establishing Monday 09:00 UTC cron cadence, and running
  the Day 7/14/30/60 checkpoint decision trees through Week 4.
companion_files:
  - phase-1-adoption-tracking-script.py
  - phase-1-adoption-tracking-config.json.template
  - phase-1-adoption-tracking-requirements.txt
  - PHASE_1_MEASUREMENT_SYSTEM.md
  - PHASE_1_WEEKLY_SYNTHESIS_TEMPLATE.md
  - PHASE_1_DECISION_TREES.md
  - PHASE_1_ADOPTION_TRACKING_SETUP_CHECKLIST.md
---

# Phase 1 Adoption Tracking — Deployment Guide

**Version 1.0 — June 1, 2026**

**Deploy**: Morning of June 3, immediately after the Domain 39 distribution window closes.

**Time required for initial setup**: 15–20 minutes.

**Ongoing overhead**: Script runs autonomously every Monday 09:00 UTC. User reviews the log (5–10 minutes). Weekly synthesis on checkpoint weeks (20–30 additional minutes).

---

## Lead Finding

The tracking system has two distinct jobs: (1) mechanical data collection — Gist view counts, Gmail reply triage, Sheets sync — which the script handles autonomously after setup; and (2) signal interpretation — distinguishing a polite acknowledgment (Level 1) from an adoption intent statement (Level 4) — which requires your judgment. This guide covers setup for both. The script handles job one. The templates and decision trees in this guide handle job two.

Domain 56 sent May 28. Domain 39 sent June 1. Day 7 checkpoint is June 4. You have approximately 36 hours from June 3 deployment to June 4 checkpoint. Setup must complete June 3.

---

## Part 1: Quick-Start Deployment Guide (15–20 minutes)

### Prerequisites

Before beginning, confirm you have:

- Python 3.10 or higher installed (`python3 --version`)
- A GitHub account with a personal access token that has `gist` read scope
- A Gmail account used for outreach (the account that sent the May 28 and June 1 emails)
- A Google account for Google Sheets (can be the same Gmail account)
- The `projects/resistance-research/` directory accessible on your machine (it is — this is the repo)

**GitHub token**: Not strictly required for initial monitoring. The Gist analytics endpoint on GitHub's REST API does not expose view counts publicly; the script attempts the analytics page scrape as a fallback. If you do not have a GitHub token, Gist view collection will degrade gracefully — the script logs a warning and continues. Email reply collection and Sheets sync work independently.

**Gmail OAuth2 is required** for email monitoring. Without it, the script runs but skips the reply collection step — which means you lose the primary signal. Complete the Gmail setup before deploying.

---

### Step 1: Install dependencies (3 minutes)

```bash
cd /path/to/projects/resistance-research/

pip install -r phase-1-adoption-tracking-requirements.txt
```

Dependencies are: `requests`, `google-auth`, `gspread`, `google-auth-httplib2`, `google-auth-oauthlib`, `python-dateutil`, `pytz`.

Confirm installation:

```bash
python3 -c "import requests, gspread, google.auth; print('OK')"
```

Expected output: `OK`. If you see an ImportError, rerun the pip install command.

---

### Step 2: Configure Gmail OAuth2 (5–8 minutes)

This step grants the script read-only access to your Gmail inbox under the `phase-1-responses` label.

**2a. Create a Google Cloud project** (skip if you already have one):

1. Go to https://console.cloud.google.com/
2. Create a new project — name it anything (e.g., "phase1-tracking")
3. Enable the Gmail API: APIs & Services > Enable APIs > search "Gmail API" > Enable

**2b. Create OAuth credentials**:

1. APIs & Services > Credentials > Create Credentials > OAuth client ID
2. Application type: Desktop app
3. Name: phase1-tracking-script
4. Download the JSON credentials file
5. Save it as `gmail-oauth-credentials.json` in a secure location (not inside the git repo)

**2c. Create the `phase-1-responses` label in Gmail**:

Gmail does not automatically create labels. Before the script can filter by label, you must create it:

1. Open Gmail > Settings (gear icon) > See all settings > Labels
2. Create a new label: `phase-1-responses`
3. Apply this label manually to any replies that arrive before the script runs — this gives the script a clean corpus to search

The Gmail query the script uses by default is `after:[date]`, pulling all messages from the past 168 hours. You can restrict this to the label by editing the `query` parameter in `run_weekly_collection()` — pass `query='label:phase-1-responses'` to narrow the search.

**2d. First-run authentication** (browser popup required, one time only):

```bash
python3 phase-1-adoption-tracking-script.py --run-now --config phase-1-adoption-tracking.json
```

On first run, a browser window opens asking you to authorize the app. Authorize with the Gmail account used for outreach. After authorizing, a `token.json` file is saved in the same directory as `gmail-oauth-credentials.json`. Subsequent runs use this token automatically and do not require browser interaction.

---

### Step 3: Configure the tracking JSON (2 minutes)

Copy the template and fill in your values:

```bash
cp phase-1-adoption-tracking-config.json.template phase-1-adoption-tracking.json
```

Edit `phase-1-adoption-tracking.json`:

```json
{
  "github_token": "ghp_YOUR_TOKEN_HERE",
  "github_username": "esca8peArtist",
  "gmail_credentials": "/absolute/path/to/gmail-oauth-credentials.json",
  "sheets_credentials": "/absolute/path/to/google-sheets-service-account.json",
  "spreadsheet_id": "YOUR_GOOGLE_SHEETS_DOC_ID",
  "canonical_gists": {
    "full_proposal": "2dec7fd03b08ab5b41c55d402f44c261",
    "executive_summary": "2869da6eaeb15a47246ade3bbbc4a3f4",
    "litigation_tracker": "418d51bda087f15a04d685ab171a5ee0",
    "first_amendment": "10d0a86e386e6c3c11c3830295a6503c",
    "environmental_rollbacks": "87e2bdb931b77480e56a08044c567bc4",
    "police_consent_decrees": "1f5cb28527c98d12526c14302c725731"
  },
  "monitoring": {
    "email_lookback_hours": 168,
    "citation_log_enabled": true,
    "google_alerts_enabled": false
  }
}
```

**Important**: The Domain 56 and Domain 39 Gist IDs used in distribution are not in the canonical_gists list above (those are the full-proposal and domain-specific Gists). Add the distribution Gist IDs explicitly:

```json
"domain_56_gist": "8f11e868397921a4e6556b41196d1b1f",
"domain_39_gist": "131e8a94c955b973b87f7fb87d0f594b"
```

The script's `CANONICAL_GISTS` dict tracks the proposal-level Gists. You should manually check Domain 56 and Domain 39 Gist view counts directly at:
- https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f
- https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b

GitHub's analytics page requires you to be logged in as the Gist owner to see view counts. The script's HTML scrape may fail if GitHub changes the page structure — manual weekly verification takes 2 minutes and is more reliable.

**Do not commit `phase-1-adoption-tracking.json`** to git. It contains credentials. Add it to `.gitignore` if not already excluded.

---

### Step 4: Set up Google Sheets tracking workbook (3 minutes)

Create a new Google Sheets document. Name it "Phase 1 Adoption Tracking." Share it with the service account email from your Sheets credentials JSON (the `client_email` field).

Tabs to create (see Part 2 for column specifications):

1. **Master Contact Log** — one row per contact, tracks delivery and reply status
2. **Gist Views** — weekly view count log by Gist
3. **Replies** — one row per reply received, with engagement score
4. **Adoptions** — Level 4+ adoption signals only
5. **Constituencies** — aggregated metrics by constituency (formula-driven)
6. **Checkpoints** — one row per checkpoint run (Day 7, 14, 30, 60)
7. **Network Map** — cross-organizational referral events

Copy the Sheets document ID from the URL:
`https://docs.google.com/spreadsheets/d/[THIS_IS_THE_ID]/edit`

Paste this ID as `spreadsheet_id` in your config JSON.

---

### Step 5: Set up cron job for Monday 09:00 UTC (2 minutes)

The script's built-in cron entry targets 08:00 UTC (per the script's `--schedule-weekly` output). The measurement system's synthesis cadence targets Monday 09:00 UTC. Adjust to 09:00 to align the cron with the synthesis window:

```bash
crontab -e
```

Add this line:

```
0 9 * * 1 /usr/bin/python3 /absolute/path/to/projects/resistance-research/phase-1-adoption-tracking-script.py --run-now --config /absolute/path/to/phase-1-adoption-tracking.json >> /absolute/path/to/projects/resistance-research/logs/cron.log 2>&1
```

Replace all `/absolute/path/to/` with the actual paths. Use `which python3` to confirm the Python binary location.

Verify the cron is registered:

```bash
crontab -l
```

You should see your entry. The first automated run will execute Monday June 9 at 09:00 UTC. For the June 4 Day 7 checkpoint, run manually:

```bash
python3 phase-1-adoption-tracking-script.py --run-now --config phase-1-adoption-tracking.json
```

---

### Step 6: First manual run and output verification (2 minutes)

Run the script now:

```bash
python3 phase-1-adoption-tracking-script.py --run-now --config phase-1-adoption-tracking.json
```

Expected output (console):

```
============================================================
PHASE 1 ADOPTION TRACKING — Weekly Collection
Timestamp: 2026-06-03T09:XX:XX
============================================================

[1/3] Fetching Gist view counts...
[2/3] Fetching recent email replies...
[3/3] Checking leading-indicator alerts...

============================================================
Weekly collection complete
  Gists tracked: 6
  Email replies: [N]
  Alerts triggered: [0 or 1]
============================================================
```

A Markdown summary file is saved to `logs/week-2026-06-03-summary.md`. Open it and confirm:
- Gist view counts are populated (not all zeros unless truly zero views)
- Email reply count matches what you expect based on what you've already received
- No unexpected errors in the Errors section

If the summary shows `Email replies: 0` but you have received replies, the Gmail query or label filter is not matching. Check Step 2d and re-run.

---

### Troubleshooting: Common Errors

**`ImportError: No module named 'google'`**
Run `pip install -r phase-1-adoption-tracking-requirements.txt` again. Confirm you are using the same Python version as cron will use.

**`Gmail authentication failed: invalid_grant`**
The `token.json` has expired or the OAuth app was revoked. Delete `token.json` and re-run — a new browser authorization prompt will appear.

**`Failed to fetch analytics for Gist [ID]: 403`**
GitHub is returning a 403 for the analytics page. This happens if you are not authenticated as the Gist owner, or if GitHub has changed the analytics URL structure. Switch to manual view count recording: log into GitHub as `esca8peArtist`, navigate to each Gist's Analytics tab, record the weekly view count in the Gist Views sheet manually.

**`Failed to authenticate with Google Sheets: invalid_client`**
The service account credentials JSON path is wrong, or the service account does not have access to the spreadsheet. Confirm the `client_email` from the credentials JSON appears in the spreadsheet's Share dialog with Editor access.

**`Sheets not connected; skipping update`**
Sheets credentials not loaded. Check `sheets_credentials` path in config JSON is an absolute path and the file exists.

**`Zero substantive replies detected` alert but you have replies**
The Gmail query is not matching replies in your inbox. Try running the script with an explicit query: edit `run_weekly_collection()` to pass `query='in:inbox'` to `get_recent_replies()`. If replies appear, the label filter is the issue — apply the `phase-1-responses` label to all inbound replies manually.

**Script runs but logs directory is not found**
The script creates `logs/` relative to the script's location. Confirm you are running from `projects/resistance-research/` or use an absolute `--output-dir` path.

---

## Part 2: First-Week Data Collection Template (Days 1–7)

### Google Sheets Column Specification

**Tab: Gist Views** — one row per week per Gist

| Column | Header | Notes |
|--------|--------|-------|
| A | date_recorded | YYYY-MM-DD (Monday of the week) |
| B | gist_id | Short label: domain_56, domain_39, full_proposal, etc. |
| C | views_this_week | Delta from prior week (manual if script analytics fail) |
| D | views_cumulative | Running total |
| E | source | "script" or "manual" |
| F | notes | Any spike explanation |

**Tab: Replies** — one row per reply

| Column | Header | Notes |
|--------|--------|-------|
| A | reply_date | YYYY-MM-DD |
| B | reply_id | R001, R002, etc. |
| C | organization | Name of sender's org |
| D | constituency | Law School / Imm Legal Aid / Civil Rights / Academic / Faith / Labor / Mutual Aid |
| E | domain_engaged | Domain 56, Domain 39, or "general" |
| F | reply_category | Implementation Signal / Critique / Data Request / General Question / Partnership / Opt-Out |
| G | engagement_score | 0–5 per PHASE_1_MEASUREMENT_SYSTEM.md scale |
| H | key_content | 1–3 sentence summary or direct quote |
| I | action_required | YES / NO |
| J | escalation | ESCALATE / none |
| K | tier2_candidate | YES / NO |
| L | notes | |

**Tab: Adoptions** — Level 4+ only

| Column | Header | Notes |
|--------|--------|-------|
| A | date_detected | YYYY-MM-DD |
| B | organization | |
| C | adoption_level | 4 (Intent) or 5 (Confirmed) |
| D | evidence | Direct quote or external artifact URL |
| E | verification_status | Probable / Confirmed |
| F | artifact_type | Brief / Curriculum / Policy / Training / Publication / Other |
| G | domain_cited | Domain 56 / Domain 39 / Other |
| H | notes | |

---

### Day-by-Day Expectations: Days 1–7

**Days 0–1 (May 28 – May 29): Domain 56 immediate window**

Gist view trajectory: 5–15 views per day is normal immediately after send. Recipients who open emails on the same day often click through within 24 hours. A spike of 10–25 views on May 28 (send date) is a positive signal. Zero views through May 29 with confirmed delivery is the first flag — check Gist URL accessibility.

Email replies: Do not expect substantive replies in the first 48 hours. Out-of-office auto-replies (Level 1) may arrive within hours. Score them as Level 1 and note the return date.

**Days 1–3 (June 1 – June 3): Domain 39 layered send**

Domain 39 emails sent June 1 to: Georgetown CCF, NHeLP, Black Mamas Matter Alliance, Brennan Center, Institute for Responsive Government. Expect a second Gist view spike around June 1–2 as Domain 39 recipients click through. This is the cross-send click-through effect documented in the Week 1 Example in PHASE_1_WEEKLY_SYNTHESIS_TEMPLATE.md.

If Domain 56 views spike on June 1 (not just Domain 39), this is a positive cross-domain signal — Domain 39 recipients are exploring the broader proposal. Note it in the Gist Views tab.

**Days 3–4 (June 1 – June 2 from Domain 39 perspective): Reply window opens**

Recipients who read immediately typically reply within 24–72 hours. The fastest responders in institutional outreach are usually those with active pending use cases (e.g., an organization with imminent litigation that finds the model brief immediately useful). Immigration legal aid contacts (NHeLP, Georgetown CCF) are highest-probability early responders given the June 1 HHS rule publication.

First substantive replies (Level 3+) arriving by June 3–4 are ahead of baseline. Level 1–2 replies by this date are normal.

**Days 5–7 (June 2 – June 4): Pre-checkpoint consolidation**

By June 4 (Day 7), you need the following data points for the Day 7 decision tree:

1. Total Bitly clicks across all tracked links (cumulative since May 28)
2. Total reply count at any level
3. Bounce count (confirmed undeliverable, not just unknown delivery status)
4. Score 3+ reply count

The Day 7 threshold for system-level HOLD (proceed normally) is: total Bitly clicks >= 15, at least 2 replies at any score, fewer than 3 bounces.

If the automated script has not yet run (first automated run is June 9), pull these numbers manually:
- Bitly: log into bit.ly and check click counts for each tracked link
- Gmail: count replies in the `phase-1-responses` label
- Bounces: check for bounce notifications in the outreach Gmail account's sent folder

---

### Pre-Populated Sample Data from Domain 56 (for calibration)

This is the Week 1 Example scenario from PHASE_1_WEEKLY_SYNTHESIS_TEMPLATE.md, reproduced here as a calibration baseline. Actual figures will differ; use this to calibrate what "normal" looks like.

| Metric | Domain 56 Week 1 Example | Your Domain 56+39 Target |
|--------|--------------------------|--------------------------|
| Contacts sent | 11 (Domain 56 only) | ~16 (11 D56 + 5 D39) |
| Bitly clicks total | 23 | >= 15 |
| Replies received | 4 | >= 2 |
| Score 3+ replies | 2 | >= 1 |
| Score 4+ replies | 1 (NILC amicus request) | >= 0 (any is ahead) |
| Constituencies with signal | 4 of 7 | >= 4 of 7 |
| Confirmed adoptions | 0 | 0 expected |
| Day 7 determination | HOLD | HOLD expected |

The Domain 56 example is a moderate-positive Week 1 scenario, not a guarantee. Fewer than 15 clicks with confirmed delivery is MONITOR status; zero clicks is ESCALATE. More than 23 clicks in Week 1 is above-baseline.

---

## Part 3: Day 7 Checkpoint Decision Tree

**Run on**: June 4, 2026 (7 days after May 28 Domain 56 send).

**How long it takes**: 10–15 minutes to pull data and run the tree.

**Data to pull before starting**:
- Total Bitly clicks since May 28 (all tracked links combined)
- Total reply count (all levels)
- Bounce count (confirmed undeliverable)
- Score 3+ reply count

---

### Step 1: Check delivery (gate question)

**How many confirmed bounces have you received?**

- 3 or more bounces (>6% of 45-contact list): run PHASE_1_DECISION_TREES.md CONTACT_VERIFY branch. Pull BATCH_1_CONTACT_VERIFICATION.md, correct addresses, re-send to corrected addresses. Restart the Day 7 clock from the re-send date. Do not proceed to Phase 2 until re-delivery is confirmed.
- Fewer than 3 bounces: continue to Step 2.

---

### Step 2: Check total Bitly clicks

**How many total clicks across all tracked links since May 28?**

- 15 or more: HOLD — delivery and interest confirmed. Continue to Step 3.
- 5–14: MONITOR — engagement below target but not zero. Check again at Day 10–12. Do not change framing yet.
- 0–4 with confirmed delivery: ESCALATE — run delivery diagnostic immediately. Check that Gist URLs are live and accessible. Check that Bitly links resolve correctly. If technical issue is found, fix it. If no technical issue, check whether recipients open emails without clicking links (reply evidence may still arrive).

---

### Step 3: Check reply count (any level)

**How many replies of any kind have you received?**

- 2 or more: system-level HOLD confirmed. Continue to constituency check.
- 1: MONITOR — single reply does not confirm system health. Continue to Day 10–12.
- 0 with confirmed delivery and >= 15 clicks: unusual — clicks confirm link access but no replies. Wait for Day 10. Some recipients read thoroughly before replying. This is not a failure signal at Day 7.
- 0 with 0 clicks: ESCALATE per Step 2.

---

### Step 4: Check reply quality

**How many replies are at Score 3 or above?**

- 1 or more Score 3+ reply by Day 7: ahead of baseline. A Score 3+ reply within Day 7 indicates the recipient read and processed content. This is the leading indicator for Day 30 STRONG trajectory.
- 0 Score 3+ replies: normal at Day 7. Day 7 is a delivery check, not a quality-of-engagement check. Score 3+ replies typically peak Days 10–21.

---

### Step 5: Constituency minimum check

For each constituency, note whether at least one signal (click or reply) has been recorded:

| Constituency | Day 7 Minimum | Status |
|---|---|---|
| Law Schools | >= 2 Bitly clicks | [ ] MET / [ ] BELOW |
| Immigration Legal Aid | >= 1 click or reply | [ ] MET / [ ] BELOW |
| Civil Rights | >= 1 click or reply | [ ] MET / [ ] BELOW |
| Academic | >= 1 reply at any score | [ ] MET / [ ] BELOW |
| Faith | >= 1 click | [ ] MET / [ ] BELOW |
| Labor | >= 1 click | [ ] MET / [ ] BELOW |
| Mutual Aid | >= 1 click | [ ] MET / [ ] BELOW |

- 5 or more constituencies meeting minimum: normal HOLD.
- 3–4 constituencies meeting minimum: MONITOR — not a system failure. Watch whether below-minimum constituencies surface in Days 8–14.
- Fewer than 3 constituencies meeting minimum: flag in CHECKIN.md as a concern. Not yet ESCALATE unless paired with low Bitly totals.

---

### Step 6: Day 7 GO/NO-GO determination

**GO (HOLD — normal trajectory)**:
All three of the following are true: Bitly total >= 15, reply count >= 2, bounce count < 3.

Next action: Proceed to Week 2. Run the script automatically on June 9 (first Monday cron run). Conduct Week 1 synthesis using PHASE_1_WEEKLY_SYNTHESIS_TEMPLATE.md on June 4.

**MONITOR**:
One of the three thresholds is missed (e.g., Bitly 8, replies 3, bounces 0). Do not change strategy. Check again manually on June 7–8 before the June 9 cron run.

**ESCALATE**:
Any of: Bitly < 5 with confirmed delivery, bounce count >= 3, zero replies AND zero clicks at Day 7.

Action: Flag in CHECKIN.md under "Needs Your Input." Run delivery diagnostic before June 5.

---

### Per-Constituency Thresholds at Day 7

Different constituencies move at different speeds. These per-constituency notes supplement the system-level decision tree above.

**Law Schools** (primary: Georgetown CCF is Domain 39; law school contacts in Domain 56 include Brookings, Berkeley Law): Expect 21–60 day adoption latency. Day 7 signal is purely delivery confirmation — a click or reply confirms delivery. No Score 3+ expected by Day 7. If Georgetown CCF (healthcare/democracy intersection) replies by Day 7, it would be ahead of baseline; log as Level 3+ and flag in CHECKIN.md.

**Immigration Legal Aid** (primary: NHeLP, NILC-adjacent contacts): 5–14 day reply latency for organizations with active litigation. NHeLP is the highest-probability early responder for Domain 39 given the June 1 HHS rule timing. If NHeLP replies with any substantive content about the work requirement rule by June 4, log as Score 3+ and flag for immediate Tier 2 follow-up.

**Mutual Aid**: 2–7 day reply latency from local coordinators when materials are immediately applicable. Black Mamas Matter Alliance (Domain 39 recipient) may respond faster than other constituencies because the Medicaid work requirements directly threaten their network's base population. Any reply from Black Mamas Matter Alliance by June 4 is ahead of baseline.

**Civil Rights** (Brennan Center is a Domain 39 recipient): Brennan Center typically responds within 5–10 days on policy-relevant materials. A click-through without reply by Day 7 is normal for Brennan Center's volume; expect a reply by June 6–10 if material is relevant to active projects.

**Academic, Faith, Labor**: 14–30 day normal reply latency. Zero signal at Day 7 is not a flag for these three. MONITOR status at Day 7 is the default and expected outcome.

---

## Part 4: Weekly Synthesis Templates (Weeks 2–4)

The PHASE_1_WEEKLY_SYNTHESIS_TEMPLATE.md file contains the full 13-section synthesis template. Use it every Monday starting June 4. This section provides the operational skeleton for Weeks 2–4 specifically, with formula references and the 20-minute overhead breakdown.

---

### Weekly Cadence

**Every Monday morning, in order**:

1. Run script if cron has not already run (09:00 UTC is the cron target; run manually if you are earlier)
2. Open `logs/week-[date]-summary.md` — review script output (5 minutes)
3. Open Google Sheets — pull the four key numbers from Constituencies tab (3 minutes)
4. Copy PHASE_1_WEEKLY_SYNTHESIS_TEMPLATE.md to `monitoring/phase-1-week-[N]-synthesis-[YYYY-MM-DD].md`
5. Fill Sections 1–6 (required every week — ~12 minutes)
6. Fill Sections 7–13 only on checkpoint weeks or if specific events occurred (adds 6–8 minutes)
7. Commit the completed synthesis file

Total non-checkpoint weeks: 15–20 minutes. Checkpoint weeks: 25–35 minutes.

---

### Formula-Driven Analysis: Four Key Numbers

Pull these four numbers from the Constituencies tab every week. They drive all decision trees.

**(A) Score 3+ reply rate** = (count of replies with engagement_score >= 3) / (count of contacts with confirmed delivery)

Google Sheets formula (in Constituencies tab):
```
=COUNTIF(Replies!G:G,">=3") / COUNTIF(Contacts!I:I,"Delivered")
```

**(B) Constituencies meeting strong threshold** = count of constituency rows where the strong threshold column is TRUE

Manual check: For each of 7 constituencies, does the count of Score 3+ replies from that constituency meet the Day 30 strong threshold? (Law Schools: >= 3; Imm Legal Aid: >= 2 or 1 litigation use; Civil Rights: >= 3 Score 2+ or 1 confirmed adoption; Academic: >= 2 Score 3+ or 1 confirmed citation; Faith: >= 2 engaged or 1 pastoral use; Labor: >= 2 engaged or 1 training integration; Mutual Aid: >= 2 engaged or 1 governance use)

**(C) Cross-organizational references** = total rows in Network Map tab

Every time a contact mentions forwarding, a colleague mentions receiving the material, or a second-hop organization appears in a reply, add a row to the Network Map tab.

**(D) Confirmed adoption signals** = count of rows in Adoptions tab where verification_status = "Confirmed"

Only external evidence (PACER filings, published documents, web detections) upgrades Level 4 to Level 5 Confirmed.

---

### Adoption Scoring Reference (0–5 Scale)

Use this scale to score every reply. From PHASE_1_MEASUREMENT_SYSTEM.md:

| Level | Label | Definition | What it looks like in a reply |
|-------|-------|-----------|-------------------------------|
| 0 | No Engagement | No reply, no click, within 14 days | [no reply] |
| 1 | Acknowledged Receipt | Polite ack or OOO without substance | "Thanks, I'll look at this" / OOO auto-reply |
| 2 | Active Read | Evidence of link access, minimal substantive content | "This is important work" + Bitly click |
| 3 | Substantive Engagement | Reply demonstrates familiarity with specific content | Cites a specific domain, asks methodology question, reports forwarding |
| 4 | Organizational Intent | Explicit intent to use in organizational work | "We're incorporating this in our amicus brief" / "I'm presenting this at faculty meeting" |
| 5 | Confirmed Adoption | External artifact confirms organizational use | Published paper citing framework / PACER filing / curriculum listing |

**False-positive exclusions (critical)**:
- Flattery without substance ("impressive work!") = Level 2, not Level 3
- Intent statement without external confirmation = Level 4, not Level 5
- A single Bitly click without substantive reply = Level 2 at most
- Out-of-office where no human follow-up occurs = Level 1 only

---

### Rolling 7-Day Gist View Average

Calculate this in the Gist Views tab to detect whether interest is sustaining or fading.

```
=AVERAGE([last 7 days of views_this_week column])
```

Targets:
- Week 1 (May 28 – June 4): 3–5 views/day average (cumulative target: >= 15 views)
- Week 2 (June 4–11): 2–4 views/day (cumulative target: >= 25 views)
- Weeks 3–4 (June 11–27): 1–3 views/day (cumulative target >= 40 views at Day 30)

A declining view rate week over week is expected and normal — initial curiosity decays. What matters is whether the total stays above thresholds and whether late-arriving views correlate with late replies (indicating slow readers who engage substantively once they read).

---

### Reply Velocity Calculation

Tracks whether new replies are still arriving or whether the reply window has closed.

```
reply_velocity = new_replies_this_week / days_in_week
```

- Week 1: any velocity > 0 is positive
- Week 2: velocity >= 0.3 replies/day (2+ per week) is on-track
- Week 3–4: velocity can drop; what matters is cumulative Score 3+ count reaching thresholds

A velocity crash (zero replies in two consecutive weeks after initial replies) before Day 21 is the flag to watch. After Day 21, natural decay to zero is expected.

---

### Weekly Synthesis Output Format

Each completed synthesis file should produce:

**Numeric dashboard block** (paste into Checkpoints tab on checkpoint weeks):

```
Week [N] | [YYYY-MM-DD] | Bitly total: [N] | Replies: [N] | Score 3+: [N] | Score 3+ rate: [X%] | Adoptions confirmed: [N] | Determination: [HOLD/MONITOR/ESCALATE/STRONG/MODERATE/WEAK]
```

**Narrative summary** (2–3 paragraphs, fills "One-sentence summary" field in Section 13):

Paragraph 1: What happened this week numerically. Clicks, replies, score distribution.

Paragraph 2: What the numbers mean for Phase 2 timing. Which constituencies are performing, which are lagging. Whether any adoption signals have appeared.

Paragraph 3 (if checkpoint week): Decision reached. Next checkpoint date. Any user escalation required.

---

## Part 5: Operational Overhead Documentation

### Time Budget Summary

| Activity | Frequency | Time per instance | Notes |
|----------|-----------|-------------------|-------|
| Initial setup | One-time | 15–20 min | This guide, Steps 1–6 |
| Script run | Automated Monday 09:00 UTC | 0 min user time | Reviews log 5–10 min |
| Log review | Weekly | 5–10 min | Open Markdown summary, check for alerts |
| Non-checkpoint synthesis | Weeks 2, 3 | 15–20 min | Sections 1–6 of template only |
| Checkpoint synthesis | Weeks 1, 4 (Day 7, Day 30) | 25–35 min | All 13 sections + decision tree |
| Adoption signal logging | Per-event | 15–20 min | Level 4+ only; expect 2–4 events total |
| Major checkpoint (Day 30, Day 60) | Weeks 4, 8 | 45–60 min | Full decision tree + CHECKIN.md update |

### Realistic Total by Week

| Week | Dates | Overhead | Reason |
|------|-------|----------|--------|
| Week 1 | May 28 – June 4 | 35–45 min | High initial reply volume; Day 7 checkpoint |
| Week 2 | June 4–11 | 20–30 min | Reply volume decaying; Day 14 checkpoint |
| Week 3 | June 11–27 | 15–20 min | Steady state |
| Week 4 | June 11–27 | 45–60 min | Day 30 checkpoint — full decision tree |
| Weeks 5–8 | June 27 – July 27 | 15–20 min/week except Day 60 | Day 60 adds 45–60 min |

**Total across first 4 weeks**: approximately 2–3 hours. Well within the 4-hour/month budget.

The 15-minute/week figure from the measurement system's overhead estimate is accurate for steady-state (non-checkpoint) weeks. It understates Week 1 and checkpoint weeks. The honest weekly average across all 8 weeks of the Phase 1 window is 30–45 minutes.

---

### What the User Does vs. What Runs Automatically

**Automatic (script handles)**:
- Gist view count collection (best-effort — may degrade to manual if GitHub analytics page changes)
- Gmail reply fetching (all replies in the past 168 hours matching the query)
- Sheets sync for logging (when Sheets credentials are configured)
- Alert detection (zero-views alert, zero-replies alert)
- Summary Markdown file generation to `logs/`

**Manual (user judgment required)**:
- Engagement score assignment for each reply (0–5 scale; script cannot read intent)
- Escalation decisions based on reply content (legal concerns, opt-out requests)
- Constituency mapping of each reply (which of the 7 constituencies does this contact belong to?)
- Level 4 → Level 5 upgrade verification (requires external artifact confirmation)
- Day 7/14/30/60 checkpoint determination (pull four numbers, run decision tree)
- Weekly synthesis narrative (Sections 4, 5, 13 of synthesis template)
- CHECKIN.md update for escalations

The division of labor is: the script surfaces the data; the user interprets it. Setup time pays off over 8 weeks because the data collection is fully hands-off once configured.

---

## Appendix A: Constituency Adoption Latency Reference

Calibration data from PHASE_1_MEASUREMENT_SYSTEM.md Section 3. Use this when assessing whether a constituency is underperforming or simply following its natural cycle.

| Constituency | Level 3 typical latency | Level 5 typical latency | Primary adoption artifact |
|---|---|---|---|
| Law Schools | 14–30 days | 60–90 days | Syllabus / SSRN working paper |
| Immigration Legal Aid | 5–14 days | 14–30 days (if active litigation) | PACER filing / published advisory |
| Civil Rights Orgs | 14–30 days | 30–60 days | Published brief / press statement |
| Academic Research | 21–45 days | 90–180 days | SSRN / conference paper |
| Faith Coalitions | 7–21 days | 30–60 days | Sermon guide / pastoral letter |
| Labor Unions | 14–30 days | 30–90 days | Training curriculum / member bulletin |
| Mutual Aid Networks | 2–7 days (local coordinators) | 30–60 days | Governance document / network newsletter |

**Interpretation rule**: Do not apply Day 30 Level 5 absence as a failure signal for Law Schools or Academic Research — their adoption cycles extend to 60–180 days. The leading indicator for these constituencies is Level 3 replies, not Level 5 artifacts.

---

## Appendix B: Escalation Quick Reference

**Escalate same day (add to CHECKIN.md "Needs Your Input" immediately)**:
- Zero Bitly clicks AND zero replies with confirmed delivery at Day 7
- Any reply expressing legal concern, privacy concern, or opt-out request
- A confirmed Level 5 adoption event (overperformance — same-day Phase 2 pre-activation available)
- Three or more confirmed bounces (>= 6% of contact list)

**Escalate within 24 hours**:
- Day 14: zero Level 3+ replies AND zero Bitly activity in Days 8–14
- Day 30: FAILURE determination (rate < 10%, zero adoptions, zero cross-org references, dead Gist clicks in Weeks 3–4)
- Score 4 events from two or more contacts within first 14 days (Phase 2 pre-activation available)

**Do not escalate — wait for signal**:
- Level 1 and Level 2 replies only in Week 1 (normal — wait for Day 14)
- One constituency at zero signal at Day 7 (not system-level failure)
- Reply rate below 25% at Day 14 (reply timing peaks Days 10–21)
- Gist click counts below 15 at Day 7 when replies are present (reading happens through alternative paths)

---

## Appendix C: Day 30 and Day 60 Threshold Reference

For the Day 30 checkpoint (June 27) and Day 60 checkpoint (July 27), the four-number pull determines STRONG / MODERATE / WEAK / FAILURE:

**STRONG** (3.0+ average adoption score): Score 3+ reply rate >= 50% AND >= 4 constituencies passing individual strong threshold AND >= 3 cross-org references AND >= 2 confirmed adoptions.

**MODERATE** (2.0–2.9 average): Score 3+ rate 30–49% OR >= 3 constituencies at strong threshold OR >= 1 cross-org reference OR >= 1 confirmed adoption.

**WEAK** (< 2.0 average): Rate < 20% AND < 2 constituencies at strong threshold AND 0 cross-org references.

**FAILURE**: Rate < 10% AND 0 adoptions AND 0 cross-org references AND 0 Gist clicks in Weeks 3–4.

Phase 2 activation:
- STRONG: Full Phase 2 activation (Tier 2 outreach with social proof from Phase 1 endorsements)
- MODERATE: Partial Phase 2 (launch in constituencies with Level 3+ signals; hold others)
- WEAK: Extend Phase 1 with framing revision before Phase 2 commitment
- FAILURE: Full contingency review; see PHASE_2_CONTINGENCY_PLAYBOOK.md

---

*Guide version 1.0 — June 1, 2026. Deploy June 3 morning after Domain 39 distribution window closes. First checkpoint: Day 7, June 4, 2026.*
