---
title: "Phase 1 Adoption Tracking — Setup Checklist"
created: 2026-06-01
version: 1.0
status: production-ready
trigger: Complete morning of June 3, before 12:00 UTC
scope: >
  One-page checklist for completing the adoption tracking setup. All steps
  reference PHASE_1_ADOPTION_TRACKING_DEPLOYMENT_GUIDE.md for detail.
  If you can check every box here, the system is production-ready.
---

# Phase 1 Adoption Tracking — Setup Checklist

**Complete by**: June 3, 2026 (before Domain 39 follow-up window opens)
**Time required**: 15–20 minutes
**If you complete all boxes, you are ready for the June 4 Day 7 checkpoint.**

---

## Environment Prerequisites

- [ ] Python 3.10+ confirmed: `python3 --version`
- [ ] Working directory: `projects/resistance-research/`
- [ ] `phase-1-adoption-tracking-script.py` is present (confirm: `ls phase-1-adoption-tracking-script.py`)
- [ ] `phase-1-adoption-tracking-config.json.template` is present

---

## Step 1: Install Dependencies

- [ ] Ran: `pip install -r phase-1-adoption-tracking-requirements.txt`
- [ ] Confirmed: `python3 -c "import requests, gspread, google.auth; print('OK')"`
- [ ] Output was `OK` (not an ImportError)

---

## Step 2: Gmail OAuth2 Setup

- [ ] Google Cloud project created (or existing project identified)
- [ ] Gmail API enabled in that project
- [ ] OAuth credentials JSON downloaded and saved as `gmail-oauth-credentials.json`
- [ ] File saved outside the git repo (not committed to version control)
- [ ] `phase-1-responses` label created in Gmail
- [ ] Any existing replies from May 28 – June 3 manually labeled `phase-1-responses`
- [ ] First-run browser authentication completed (ran `--run-now`, browser authorized, `token.json` saved)

---

## Step 3: Config JSON

- [ ] `phase-1-adoption-tracking.json` created from template: `cp phase-1-adoption-tracking-config.json.template phase-1-adoption-tracking.json`
- [ ] `github_token` filled in (or left blank — script degrades gracefully)
- [ ] `github_username` set to `esca8peArtist`
- [ ] `gmail_credentials` set to absolute path of `gmail-oauth-credentials.json`
- [ ] `sheets_credentials` set to absolute path of Google Sheets service account JSON
- [ ] `spreadsheet_id` filled in (copied from Sheets URL)
- [ ] `phase-1-adoption-tracking.json` added to `.gitignore` (or confirmed not staged for commit)

**Domain 56 and Domain 39 Gist URLs noted separately** (script does not auto-track these — verify manually):
- [ ] Domain 56 Gist: https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f — accessible (HTTP 200)
- [ ] Domain 39 Gist: https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b — accessible (HTTP 200)

---

## Step 4: Google Sheets Workbook

- [ ] New Google Sheets document created and named "Phase 1 Adoption Tracking"
- [ ] Service account email from credentials JSON added as Editor in Sheets share dialog
- [ ] The following tabs created (exact names matter for script sync):
  - [ ] Master Contact Log
  - [ ] Gist Views
  - [ ] Replies
  - [ ] Adoptions
  - [ ] Constituencies
  - [ ] Checkpoints
  - [ ] Network Map

**Gist Views tab — seed with Day 1 data**:
- [ ] Row added for May 28 with Domain 56 Gist view count (pull manually from GitHub Analytics)
- [ ] Row added for June 1 with Domain 39 Gist view count (pull manually from GitHub Analytics)

**Replies tab — seed with any replies already received**:
- [ ] All replies received May 28 – June 3 entered with date, organization, constituency, engagement score

---

## Step 5: Cron Job

- [ ] Ran `crontab -e` and added the Monday 09:00 UTC line
- [ ] Confirmed with `crontab -l` — entry is visible
- [ ] Absolute path to script and config confirmed in the cron entry (no relative paths)
- [ ] Python binary path confirmed with `which python3` — matches cron entry

**Cron entry format** (fill in your absolute paths):
```
0 9 * * 1 /usr/bin/python3 /ABSOLUTE/PATH/phase-1-adoption-tracking-script.py --run-now --config /ABSOLUTE/PATH/phase-1-adoption-tracking.json >> /ABSOLUTE/PATH/logs/cron.log 2>&1
```

---

## Step 6: First Manual Run and Verification

- [ ] Ran: `python3 phase-1-adoption-tracking-script.py --run-now --config phase-1-adoption-tracking.json`
- [ ] Console output showed all three collection steps (Gist / Email / Alerts) without fatal errors
- [ ] `logs/week-2026-06-03-summary.md` file created and contains data (not empty)
- [ ] Email reply count in summary matches count of replies actually received since May 28
- [ ] No unexpected ESCALATE alerts in summary (expected: possibly `ZERO_REPLIES_DETECTED` if no replies yet — this is informational, not a failure)

---

## Day 7 Checkpoint Readiness (June 4)

Confirm you know how to pull these four numbers manually in case the cron run encounters an error before June 9:

- [ ] Can check total Bitly clicks: log into bit.ly account used for distribution
- [ ] Can count email replies: open Gmail, filter by `phase-1-responses` label
- [ ] Can identify bounces: check outgoing sent folder for bounce notifications
- [ ] Can open PHASE_1_DECISION_TREES.md and run the Day 7 tree with those four numbers

**Day 7 HOLD thresholds to have memorized**:
- Bitly total >= 15 clicks
- Reply count >= 2 (any level)
- Bounce count < 3

---

## File Locations Reference

| File | Location |
|------|----------|
| Tracking script | `projects/resistance-research/phase-1-adoption-tracking-script.py` |
| Config template | `projects/resistance-research/phase-1-adoption-tracking-config.json.template` |
| Active config (not in git) | wherever you saved it — use absolute path in cron |
| Requirements | `projects/resistance-research/phase-1-adoption-tracking-requirements.txt` |
| Deployment guide | `projects/resistance-research/PHASE_1_ADOPTION_TRACKING_DEPLOYMENT_GUIDE.md` |
| Weekly synthesis template | `projects/resistance-research/PHASE_1_WEEKLY_SYNTHESIS_TEMPLATE.md` |
| Decision trees | `projects/resistance-research/PHASE_1_DECISION_TREES.md` |
| Measurement system | `projects/resistance-research/PHASE_1_MEASUREMENT_SYSTEM.md` |
| Weekly synthesis output dir | `projects/resistance-research/monitoring/` |
| Script log output | `projects/resistance-research/logs/` |

---

## Quick Reference: The Week's Timeline

| Date | Event | Action |
|------|-------|--------|
| June 3 | Setup complete | Complete this checklist; run manual test |
| June 4 | Day 7 checkpoint | Pull 4 numbers; run Day 7 decision tree; complete Week 1 synthesis |
| June 9 | First automated cron run | Review `logs/week-2026-06-09-summary.md` (5–10 min) |
| June 11 | Day 14 checkpoint | Pull 4 numbers; run Day 14 decision tree; Week 2 synthesis |
| June 27 | Day 30 checkpoint | Full decision tree; Phase 2 sequencing decision |
| July 27 | Day 60 checkpoint | Full decision tree; Phase 2 full-scale activation decision |

---

*Checklist version 1.0 — June 1, 2026. Deploy with PHASE_1_ADOPTION_TRACKING_DEPLOYMENT_GUIDE.md.*
