---
title: "Phase 1 Adoption Tracking — Deployment Checklist"
created: 2026-06-03
status: production-ready
activation: June 3, 2026 morning
total_time: "10-15 minutes"
---

# Phase 1 Adoption Tracking — Deployment Checklist

**Activation date**: June 3, 2026 morning
**Total deployment time**: 10-15 minutes
**Prerequisite**: Domain 39 was sent June 1. Domain 56 was sent May 28. Both Gists are live.

Run steps in order. Each step has a time estimate. Steps marked [SKIP IF DONE] were completed before June 1.

---

## Pre-Deployment Checks (2 minutes)

- [ ] Python 3.10+ installed: `python3 --version`
- [ ] Working directory: `projects/resistance-research/phase-1-adoption/`
- [ ] `adoption-tracking-config.json` exists (it does — pre-created)
- [ ] Verify both Gists accessible:
  - `curl -I https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f` (Domain 56)
  - `curl -I https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b` (Domain 39)
  - Expected response: HTTP 200

---

## Step 1: Install Dependencies (2 minutes)

Run from the `phase-1-adoption/` directory:

```bash
pip3 install requests
```

For Gmail monitoring (optional — add later if not done before June 1):
```bash
pip3 install google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

Verify:
```bash
python3 -c "import requests; print('requests OK')"
```

---

## Step 2: Configure github_username (1 minute)

The config already has all Gist IDs. Set your GitHub username:

Edit `adoption-tracking-config.json` — line 3:
```json
"github_username": "esca8peArtist",
```

This is already set correctly if you have not changed it. Verify the username matches the account that owns the Gists.

Optional: Add a GitHub personal access token to increase rate limit from 60 to 5000 requests/hour:
1. GitHub > Settings > Developer settings > Personal access tokens > Tokens (classic)
2. Generate token with scope: `gist` (read-only)
3. Add to config: `"github_token": "ghp_YOUR_TOKEN_HERE"`

---

## Step 3: Verify Configuration (1 minute)

```bash
python3 phase-1-adoption-tracking-script.py --check-config
```

Expected output:
```
  [OK     ] Config file: /path/to/adoption-tracking-config.json
  [OK     ] GitHub username: esca8peArtist
  [MISSING ] GitHub token: Required for 5000 req/hr; optional for 60 req/hr
  [INFO   ] Canonical Gists: 8 Gists tracked
  ...
```

"MISSING" for GitHub token is acceptable — the script runs without it at 60 req/hr (sufficient for weekly polling of 8 Gists).

---

## Step 4: First Run — Baseline Collection (2 minutes)

```bash
python3 phase-1-adoption-tracking-script.py --run-now
```

Expected output ends with:
```
Done — Week X | 0 clicks | 0 replies | N alerts
```

This creates:
- `data/state.json` — tracking state initialized
- `data/week-01-2026-06-03-summary.md` — Week 1 baseline summary
- `data/gist-view-tracking.json` — Gist engagement log (first entry)
- `logs/adoption-tracking.log` — execution log

Verify:
```bash
ls data/
cat logs/adoption-tracking.log | tail -10
```

---

## Step 5: Schedule Weekly Cron (1 minute)

```bash
python3 phase-1-adoption-tracking-script.py --schedule-weekly
```

This prints the crontab entry. Install it:

```bash
crontab -e
```

Add the printed line (it will look like):
```
0 9 * * 1 /usr/bin/python3 /home/awank/dev/SuperClaude_Framework/projects/resistance-research/phase-1-adoption/phase-1-adoption-tracking-script.py --run-now
```

Verify installation:
```bash
crontab -l | grep adoption-tracking
```

---

## Step 6: Gmail Configuration (Optional — 5 minutes if not done)

Skip if Gmail label was created before June 1 send.

If not yet configured:

1. Create Gmail label named exactly `phase-1-responses` (case-sensitive):
   - Gmail > Settings (gear) > See all settings > Labels > Create new label
   - Name: `phase-1-responses`

2. Create filter to auto-label Phase 1 replies:
   - Gmail > Settings > Filters and Blocked Addresses > Create a new filter
   - "From" field: paste Phase 1 contact emails (or filter by "subject: Re:")
   - Action: Apply label "phase-1-responses"

3. Run OAuth2 setup:
   ```bash
   python3 oauth2_login.py
   ```
   Follow browser prompt. Creates `token.json`.

4. Enable in config (`adoption-tracking-config.json`):
   ```json
   "gmail_enabled": true,
   "gmail_credentials": "./credentials.json"
   ```

5. Test:
   ```bash
   python3 phase-1-adoption-tracking-script.py --run-now
   ```
   Look for `[INFO] X replies retrieved` in output.

---

## Step 7: Bitly Configuration (Optional — 5 minutes if not done)

Skip if Bitly links were created and embedded in sent emails before June 1.

If Bitly was not set up:
- Note that Week 1 click data will be unavailable
- Start Bitly tracking from Week 2
- Do NOT re-send emails to add Bitly links

If Bitly is configured:
1. Get Bitly Generic Access Token: app.bitly.com > Account Settings > API
2. Add to config:
   ```json
   "bitly_enabled": true,
   "bitly_token": "YOUR_TOKEN",
   "bitly_links": {
     "domain_56_civil_service": "bit.ly/drp-d56",
     "domain_39_healthcare": "bit.ly/drp-d39"
   }
   ```
3. Replace `bit.ly/drp-d56` and `bit.ly/drp-d39` with your actual custom back-halves

---

## Step 8: Google Sheets Dashboard (15-20 minutes — if not done before June 1)

If the 7-tab Google Sheets dashboard was not created before the June 1 send, create it now.

Quick setup (20 minutes):
1. Create Google Sheet: `Phase 1 Impact Dashboard — June 2026`
2. Rename 7 tabs: Contacts, Gist_Views, Replies, Adoptions, Constituencies, Checkpoints, Synthesis_Log
3. Contacts tab: enter 45 contacts from `execution/domain-39-contact-list.md` and `execution/domain-56-email-template.md`
4. Add column headers from `PHASE_1_MEASUREMENT_SPREADSHEET_SPEC.md`
5. Add summary row formulas (copy from Spreadsheet Spec document)
6. Share: "Anyone with the link can view"
7. Paste URL in `CHECKIN.md` under "Dashboard URL"

Full schema: `PHASE_1_MEASUREMENT_SPREADSHEET_SPEC.md`

---

## Deployment Complete

When all checked steps above are done:

- [ ] Script runs without errors
- [ ] Cron is installed (verify: `crontab -l`)
- [ ] data/state.json exists
- [ ] logs/adoption-tracking.log has today's run entry
- [ ] Google Sheets dashboard URL pasted in CHECKIN.md
- [ ] Gmail monitoring enabled (or skipped for now)

**Next actions**:
- Monday morning each week: review `data/week-NN-YYYY-MM-DD-summary.md`
- Day 7 (June 7-8): run `python3 phase-1-adoption-tracking-script.py --day7-report`
- Day 30 (June 27-28): run `python3 phase-1-adoption-tracking-script.py --day30-report`

---

## Day 3 Pre-Send Preparations (June 3 send window)

If Day 3 outreach emails are planned:

- [ ] Review data/week-01-raw.json — confirm no delivery failures detected
- [ ] Check Gmail phase-1-responses label — any replies received Days 1-2?
- [ ] If any Score 4 reply: add to CHECKIN.md before sending Day 3 emails (social proof context)
- [ ] Verify send schedule against DOMAIN_39_14UTC_ACTIVATION_RUNBOOK.md (Section 3)
- [ ] If Day 3 sends are a separate wave: ensure Bitly links are embedded in those templates

Day 3 email template verification:
- [ ] [YOUR_NAME] placeholder filled in all templates
- [ ] [YOUR_CONTACT_INFO] filled
- [ ] Gist URL is Bitly short link (not raw GitHub URL)
- [ ] Subject line matches original send subject (for reply threading)

---

## Email Template for Phase 1 Participants — Day 3 Follow-up Option

If you want to send a brief Day 3 follow-up to contacts who have not replied:

```
Subject: Following up — [Framework Name]

[First name],

Quick follow-up to my email from [date]. I wanted to confirm delivery and flag
one development since I sent it:

[One sentence: Domain 39 healthcare/HHS update, or Domain 56 civil service update
that is time-sensitive as of June 1, 2026]

The framework is accessible at [Bitly short link]. Happy to discuss any portion
of it by phone or email.

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

When to use: Only if 0 clicks AND 0 replies by Day 3 from a specific contact. Do not send to contacts who have already replied.

Timing: Send between 10:00-15:00 recipient's local time for best open rates.

---

## Operational Overhead Assessment

**Daily operations** (automated, no user input):
- Script runs weekly via cron (Monday 09:00 UTC) — 0 user minutes

**Daily monitoring** (manual, optional):
- Morning check of Gmail phase-1-responses label: 2 min
- Reply scoring if reply received: 3 min/reply

**Weekly synthesis** (Monday morning, required):
- Section 1-6 of PHASE_1_WEEKLY_SYNTHESIS_TEMPLATE.md: 12 min
- Bitly click pull and Sheets entry: 3 min
- Script output review (data/week-NN summary): 2 min
- Total normal week: 17 min

**Checkpoint weeks** (Weeks 1, 2, 4, 8):
- Decision tree run: 10 min
- CHECKIN.md update: 5 min
- Full synthesis (Sections 1-13): 35 min
- Total checkpoint week: ~40 min

**Ad hoc adoption events**:
- Score 4 or 5 reply: 15-20 min (log, respond, CHECKIN.md)
- Expected: 2-4 events across 8-week window

**8-week total estimate**: ~5-6 hours (37-45 min/week averaged)

**Conclusion**: < 20 min/day user input is achieved in all non-checkpoint weeks. Formula calculations are fully autonomous. The stated daily cap is met; checkpoint weeks run slightly over the daily average but remain under 90 min for the week.
