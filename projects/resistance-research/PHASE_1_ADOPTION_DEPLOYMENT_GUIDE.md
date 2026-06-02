---
title: "Phase 1 Adoption Tracking — Master Deployment Guide"
created: 2026-06-02
version: 3.0
status: production-ready
activation: June 2-3, 2026
replaces: PHASE_1_ADOPTION_TRACKING_DEPLOYMENT_GUIDE.md (v1.0, June 1)
companion_system: phase-1-adoption/ directory (v2.0, Session 2507)
scope: >
  Unified user-executable deployment guide integrating the v2.0 tracking system
  for the June 2-3 activation window. Copy-paste checklists throughout.
  15-20 minute total setup. Daily ops: 5-10 min. Weekly: 15-20 min.
---

# Phase 1 Adoption Tracking — Master Deployment Guide

**Version 3.0 — June 2, 2026**

**Deploy window**: June 2-3, 2026 (Domain 39 sent June 1; Day 7 checkpoint is June 7-8)

**Total setup time**: 15-20 minutes (one-time)

**Ongoing overhead**: 5-10 min/day, 15-20 min/week normal weeks, ~40 min checkpoint weeks

---

## Lead Finding

The v2.0 tracking system in `phase-1-adoption/` is fully built and ready to activate. The canonical script is at `projects/resistance-research/phase-1-adoption/phase-1-adoption-tracking-script.py`. Everything below is a copy-paste execution path — no decision-making required. Follow the steps in order.

**Current state as of June 2**:
- Domain 56 (Civil Service) — sent May 28, Day 7 checkpoint was June 4 (Day 7 complete)
- Domain 39 (Healthcare Access) — sent June 1 to 5 Tier 1 contacts for HHS June 1 deadline
- Day 7 checkpoint for Domain 39: June 7-8
- Day 30 checkpoint: June 27-28
- Phase 2 Domain 58/59 activation gate: Day 30 (June 27-28), with early triggers possible

---

## Part 1: Pre-Deployment Verification (2 minutes)

Run these commands exactly as written. Do not skip.

```bash
# Confirm working directory
ls /home/awank/dev/SuperClaude_Framework/projects/resistance-research/phase-1-adoption/

# Confirm canonical script exists
ls /home/awank/dev/SuperClaude_Framework/projects/resistance-research/phase-1-adoption/phase-1-adoption-tracking-script.py

# Confirm both Domain Gists are accessible
curl -I https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b 2>/dev/null | head -1
curl -I https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f 2>/dev/null | head -1
```

Expected: `HTTP/2 200` for both Gist URLs. If you see 404, the Gist has been deleted or made private — see Troubleshooting at end of this document.

---

## Part 2: Install Dependencies (2 minutes)

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/resistance-research/phase-1-adoption/

# Required
pip3 install requests

# Verify
python3 -c "import requests; print('OK')"
```

For Gmail reply monitoring (recommended — this is your primary reply signal):

```bash
pip3 install google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

---

## Part 3: Configure and Verify (3 minutes)

The config file is pre-populated with all Gist IDs and the GitHub username. You only need to check it.

```bash
# Check current config
cat adoption-tracking-config.json | python3 -m json.tool | head -20
```

The `github_username` should be `esca8peArtist`. If not, edit line 3 of the config file.

Run the built-in config check:

```bash
python3 phase-1-adoption-tracking-script.py --check-config
```

Expected output (acceptable):
```
[OK     ] Config file found
[OK     ] GitHub username: esca8peArtist
[MISSING ] GitHub token: optional; adds rate-limit headroom
[INFO   ] Canonical Gists: 8 Gists tracked
```

"MISSING" for GitHub token is acceptable for normal weekly operation. The script runs at 60 requests/hour without a token, which is sufficient for 8 weekly Gist polls.

**Optional — add GitHub token for 5000 req/hr**:
1. GitHub > Settings > Developer settings > Personal access tokens > Tokens (classic)
2. Generate token with `gist` scope (read-only)
3. Edit `adoption-tracking-config.json`: set `"github_token": "ghp_YOUR_TOKEN"`

---

## Part 4: First Run — Baseline Collection (2 minutes)

```bash
python3 phase-1-adoption-tracking-script.py --run-now
```

This creates four files:
- `data/state.json` — persistent tracking state
- `data/week-01-2026-06-02-summary.md` — Week 1 baseline summary
- `data/gist-view-tracking.json` — Gist engagement baseline
- `logs/adoption-tracking.log` — execution log

Verify the run succeeded:

```bash
ls data/
cat logs/adoption-tracking.log | tail -5
```

If output ends with `Weekly collection complete`, the baseline is established.

---

## Part 5: Schedule Weekly Automation (1 minute)

```bash
python3 phase-1-adoption-tracking-script.py --schedule-weekly
```

Copy the printed crontab line, then:

```bash
crontab -e
```

Paste the line. It will look like:
```
0 9 * * 1 /usr/bin/python3 /home/awank/dev/SuperClaude_Framework/projects/resistance-research/phase-1-adoption/phase-1-adoption-tracking-script.py --run-now
```

Verify:
```bash
crontab -l | grep adoption-tracking
```

After this step, the script runs every Monday at 09:00 UTC without user action. Output is written to `data/` automatically.

---

## Part 6: Gmail Reply Monitoring Setup (5 minutes, if not done before June 1)

Skip if Gmail label `phase-1-responses` was already created and the OAuth2 flow was completed before the June 1 send.

**Step 6a — Create Gmail label**:
1. Open Gmail (wanka95@gmail.com)
2. Settings (gear) > See all settings > Labels > Create new label
3. Name: `phase-1-responses` (exact spelling, case-sensitive)

**Step 6b — Create reply filter**:
1. Gmail > Settings > Filters and Blocked Addresses > Create new filter
2. "From" field: enter all Phase 1 contact email domains (or use "Subject contains: Re:")
3. Action: Apply label `phase-1-responses`

**Step 6c — Run OAuth2 setup**:
```bash
python3 oauth2_login.py
```
Follow the browser prompt. This creates `token.json`. Run once; token auto-refreshes thereafter.

**Step 6d — Enable in config**:
Edit `adoption-tracking-config.json`:
```json
"gmail_enabled": true,
"gmail_credentials": "./credentials.json"
```

**Step 6e — Test**:
```bash
python3 phase-1-adoption-tracking-script.py --run-now
```
Look for `[INFO] X replies retrieved` in the output.

---

## Part 7: Bitly Click Tracking Setup (5 minutes, if not done before June 1)

Bitly provides the primary engagement signal — click counts per Gist link. GitHub API does not expose view counts.

**If Bitly links were embedded in the June 1 send**: Skip to Step 7c to retrieve click counts.

**If Bitly was NOT set up before June 1**: Week 1 click data is unavailable. Do not re-send emails to add Bitly links. Begin tracking from Week 2. Note "No Bitly data — tracking starts Week 2" in the Google Sheets Gist_Views tab, Week 1 row.

**Step 7a — Create Bitly account** (if not done):
1. Go to app.bitly.com
2. Sign in with wanka95@gmail.com or create account
3. Settings > API > Generate Generic Access Token

**Step 7b — Create short links**:
- Domain 56: `https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f` → back-half: `drp-d56`
- Domain 39: `https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b` → back-half: `drp-d39`

**Step 7c — Enable in config**:
```json
"bitly_enabled": true,
"bitly_token": "YOUR_TOKEN_HERE",
"bitly_links": {
  "domain_56_civil_service": "bit.ly/drp-d56",
  "domain_39_healthcare": "bit.ly/drp-d39"
}
```

Replace `bit.ly/drp-d56` and `bit.ly/drp-d39` with your actual custom back-halves.

**Step 7d — Weekly click pull** (manual, 3 min/week):
1. app.bitly.com > Dashboard
2. Select each link > Analytics > Last 7 days
3. Enter per-link click counts in Google Sheets `Gist_Views` tab

---

## Part 8: Google Sheets Dashboard Setup (15-20 minutes, if not done before June 1)

**Create the dashboard**:
1. Open sheets.google.com (wanka95@gmail.com)
2. Create new sheet titled: `Phase 1 Impact Dashboard — June 2026`
3. Create 7 tabs (double-click tab name at bottom to rename):
   - `Contacts`
   - `Gist_Views`
   - `Replies`
   - `Adoptions`
   - `Constituencies`
   - `Checkpoints`
   - `Synthesis_Log`
4. Share > "Anyone with the link" > Viewer
5. Copy share URL > paste in `CHECKIN.md` under "Dashboard URL"

**Full setup formulas and schema**: `phase-1-adoption/GOOGLE_SHEETS_TEMPLATE_COMPLETE.md`

**Most critical formulas to enter immediately** (Contacts tab, summary block):

Place these in Row 1 of the Contacts tab:

| Column A label | Column B formula |
|----------------|-----------------|
| Delivered | `=COUNTIF(G3:G200,"Delivered")` |
| Bounced | `=COUNTIF(G3:G200,"Bounced")` |
| Any reply | `=COUNTA(H3:H200)-COUNTBLANK(H3:H200)` |
| Reply rate | `=IFERROR((COUNTA(H3:H200)-COUNTBLANK(H3:H200))/COUNTIF(G3:G200,"Delivered"),0)` |
| Score 3+ replies | `=COUNTIF(I3:I200,">=3")` |
| Score 3+ rate | `=IFERROR(COUNTIF(I3:I200,">=3")/COUNTIF(G3:G200,"Delivered"),0)` |

**Enter all 45 contacts** (one per row starting at A3) from:
- `execution/domain-39-contact-list.md` (Domain 39 contacts)
- `execution/domain-56-email-template.md` (Domain 56 contacts)

Set `Wave_Sent` = 05/28/2026 for Domain 56 contacts, 06/01/2026 for Domain 39 contacts.

Set `Delivery_Status` = "Unknown" initially. Change to "Delivered" after confirmed. "Bounced" only if you received a bounce notification from your email provider.

---

## Part 9: Deployment Verification Checklist

Before running the Day 7 checkpoint, confirm all of these:

- [ ] Script runs without errors: `python3 phase-1-adoption-tracking-script.py --run-now`
- [ ] Cron installed: `crontab -l | grep adoption-tracking`
- [ ] `data/state.json` exists
- [ ] `logs/adoption-tracking.log` has today's entry
- [ ] Google Sheets dashboard created and URL pasted in `CHECKIN.md`
- [ ] Contacts tab populated with all 45 contacts
- [ ] Gmail monitoring enabled (or explicitly skipped with note in CHECKIN.md)
- [ ] Bitly tracking configured or Week 1 absence noted in Gist_Views tab

**Total time to this point**: 15-20 minutes setup.

---

## Part 10: Daily Operations Schedule (5-10 min/day)

**Every day** (2 minutes):
- Check Gmail `phase-1-responses` label for new replies
- If reply received: score immediately using the 5-second rule (see Part 11 below)
- If Score 4 or 5: update `CHECKIN.md` same day

**Every Monday** (15-20 minutes):
1. Read `data/week-NN-YYYY-MM-DD-summary.md` (generated by cron)
2. Pull Bitly click counts from app.bitly.com > Analytics > Last 7 days (3 min)
3. Enter per-link counts in Google Sheets Gist_Views tab
4. Score any unscored Gmail replies; enter in Replies tab
5. Update Contacts tab (Reply_Date, Reply_Score, Delivery_Status)
6. Complete PHASE_1_WEEKLY_SYNTHESIS_TEMPLATE.md Sections 1-6 (12 min)

**Checkpoint Mondays** (Days 7, 14, 30 — +20 min):
```bash
# Day 7 (June 7-8)
python3 phase-1-adoption-tracking-script.py --day7-report

# Day 30 (June 27-28)
python3 phase-1-adoption-tracking-script.py --day30-report
```

Follow the printed decision tree. Enter results in Checkpoints tab. Update CHECKIN.md.

---

## Part 11: Reply Scoring Reference (5-second rule)

Before scoring, ask: "Does this reply tell me anything about what the person plans to do with the material?"

- NO: Score 1 (OOO) or 2 (polite ack)
- YES: Score 3, 4, or 5 depending on specificity of stated intent

| Score | Signal | Action |
|-------|--------|--------|
| 1 | OOO auto-reply | Log; set reminder for return date |
| 2 | "Thanks for sharing" — no substance | Log; no follow-up needed |
| 3 | Question about methodology, or forward stated to named person/team | Log; respond within 48h |
| 4 | Intent to use — specific named use case (amicus, training module, policy brief, syllabus) | Log; respond same day; CHECKIN.md flag |
| 5 | Adoption confirmed — published output, court filing, curriculum in use | Log; CHECKIN.md same day; pre-activate Phase 2 |

**Score 4 requires**: a specific named use case OR a specific named recipient of a forward. "I'll share this with my team" is Score 2. "I'm forwarding this to our litigation director for the Ninth Circuit amicus we're filing June 18" is Score 4.

**Full reply triage calibration**: `phase-1-adoption/WEEK_1_DATA_COLLECTION_FRAMEWORK.md`, Section "Reply Triage Rules"

---

## Part 12: Key Thresholds Reference Card

| Checkpoint | HOLD (proceed) | MONITOR (recheck) | ESCALATE (action needed) |
|-----------|---------------|-------------------|--------------------------|
| Day 7 | 15+ clicks AND 2+ replies | 5-14 clicks OR 0-1 replies | 0-4 clicks with confirmed delivery |
| Day 14 | 25+ cumulative clicks | 10-24 cumulative clicks | < 10 cumulative clicks |
| Day 30 | STRONG: A>=50%, B>=4 constituencies, C>=3 cross-org refs, D>=2 confirmed adoptions | MODERATE: partial signals | FAILURE: all zeros |

**Phase 2 early activation** (pre-Day 30):
- Any Score 5 received Days 1-14: pre-activate both Domain 58 and 59 immediately
- Two or more Score 4 replies in Days 1-7: stage Domain 58 and 59 for Day 14 window
- Single Score 4 reply from Domain 58/59 primary constituency: stage that domain for Day 14

**Phase 2 activation files**:
- `phase-1-adoption/DAY_7_CHECKPOINT_DECISION_TREE.md` — full Day 7 + Phase 2 sequencing logic
- `PHASE_1_DAY_7_CHECKPOINT_DECISION_TREE.md` (this directory) — consolidated version

---

## Part 13: Alert Levels

Alerts above MONITOR are auto-appended to `CHECKIN.md` when the script runs:

| Level | Meaning | Required response time |
|-------|---------|----------------------|
| INFO | Informational; no action needed | — |
| MONITOR | Below target; recheck at next checkpoint | Before next checkpoint |
| ESCALATE | Possible delivery failure; diagnostic needed | Within 24 hours |
| FAILURE_IMMINENT | Critical threshold breached | Within 48 hours |
| ESCALATE_NOW | Score 5 adoption or Score 4 cluster | Same day |
| URGENT | Bounce count exceeds threshold | Within 24 hours |

---

## Part 14: Operational Overhead Summary

| Activity | Frequency | Time estimate |
|----------|-----------|---------------|
| Morning Gmail label check | Daily | 2 min |
| Reply scoring (per reply) | Per reply (~3/week average) | 3 min/reply |
| Bitly pull and Sheets entry | Once/week (Monday) | 3 min |
| Script review (data/ summary) | Once/week (Monday) | 5 min |
| Weekly synthesis Sections 1-6 | Once/week (Monday) | 12 min |
| Checkpoint decision tree | Weeks 1, 2, 4, 8 | 20 min |
| Score 4/5 reply response | As needed (~2-4 total) | 15-20 min/event |

**Normal week**: ~17 min
**Checkpoint week**: ~37-40 min
**8-week total estimate**: 5-6 hours

---

## Part 15: Troubleshooting

**ImportError on script run**:
```bash
pip3 install requests
pip3 install google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

**GitHub rate limit (60 req/hr exceeded)**:
- Add GitHub personal access token to config (no scopes required — public read is sufficient)
- Field name: `"github_token": "ghp_YOUR_TOKEN"`

**Gmail token expired (401 error)**:
```bash
rm /home/awank/dev/SuperClaude_Framework/projects/resistance-research/phase-1-adoption/token.json
python3 oauth2_login.py
```

**Cron not running**:
```bash
systemctl status cron
crontab -l
python3 phase-1-adoption-tracking-script.py --run-now  # test manually
```

**Gist returns HTTP 404**:
- Verify Gist is set to Public (not Secret) in GitHub
- Check Gist ID matches `phase-1-adoption/README.md` Live Gist URLs table

**Bitly link returns 0 clicks permanently**:
- Verify the short link was embedded in sent emails (check sent folder for Bitly URL vs. raw Gist URL)
- If raw Gist URLs were sent instead: accept 0 Bitly data for those weeks; track via reply rate only

---

## Reference Files

| File | Purpose |
|------|---------|
| `phase-1-adoption/README.md` | v2.0 system overview and quick-start |
| `phase-1-adoption/DEPLOYMENT_CHECKLIST.md` | Detailed step-by-step checklist |
| `phase-1-adoption/WEEK_1_DATA_COLLECTION_FRAMEWORK.md` | Day 1-7 checklist, reply triage, scoring calibration |
| `phase-1-adoption/DAY_7_CHECKPOINT_DECISION_TREE.md` | Day 7 + Phase 2 Domain 58/59 activation logic |
| `phase-1-adoption/GOOGLE_SHEETS_TEMPLATE_COMPLETE.md` | 7-tab Sheets setup with all formulas |
| `PHASE_1_WEEKLY_MEASUREMENT_TEMPLATES.md` | Weeks 2-4 synthesis templates and automated formulas |
| `PHASE_1_DAY_7_CHECKPOINT_DECISION_TREE.md` | Day 7 decision tree (consolidated, this directory) |
| `PHASE_1_MEASUREMENT_SPREADSHEET_SPEC.md` | Full schema spec (canonical reference) |
| `PHASE_1_WEEKLY_SYNTHESIS_TEMPLATE.md` | Monday morning synthesis template |
| `CHECKIN.md` | Escalation target for all urgent alerts |
