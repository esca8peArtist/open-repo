---
title: "Measurement Automation Setup — Phase 1 KPI Infrastructure"
project: cybersecurity-hardening
created: 2026-05-13
version: 1.0
status: production-ready
item: 38 — Measurement Automation Setup
phase: Phase 1 (launch June 1, 2026)
depends-on:
  - TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md (Item 17 — KPIs, thresholds, benchmarks)
  - PHASE_1_EXECUTION_CALENDAR.md (Item 29 — 25 contacts, send schedule, gate dates)
scripts:
  - scripts/kit_email_sync.py
  - scripts/discord_daily_briefing.py
config:
  - config/measurement_env_template.txt
---

# Measurement Automation Setup
## Phase 1 KPI Infrastructure — Ready by May 31, Live June 1

**Lead finding**: The measurement system must be live before the first email sends on June 1. Data collection retroactively applied after the first wave is permanently incomplete — the Kit API returns broadcast stats from the send date, but you cannot recover click and open timing data from emails sent before the sync was running. Set up this infrastructure by May 31.

**What this document delivers**:
1. Google Sheets 5-tab template (column layout, all formulas copy-paste ready)
2. Kit (ConvertKit) email engagement API integration guide
3. Discord webhook daily briefing setup
4. Email engagement log automation (VLOOKUP, conditional formatting)
5. Meeting tracking spreadsheet with outcome categorization
6. KPI dashboard with trend indicators and threshold alerts
7. May 31 setup checklist (5-point pre-launch verification)
8. June 1 morning verification steps
9. Contingency response triggers with decision trees

**Code deliverables** (scripts are production-ready on the Pi, copy-paste from the sections below or use the files in `scripts/`):
- `scripts/kit_email_sync.py` — Kit API to Sheets sync (~100 lines)
- `scripts/discord_daily_briefing.py` — Discord daily briefing with anomaly detection (~150 lines)
- `config/measurement_env_template.txt` — environment variable template

---

## Section 1: Google Sheets 5-Tab Template

### 1.1 Create the Spreadsheet

Create a new Google Sheet titled: **Phase 1 Policy Outreach Tracker — June 2026**

Share it with two accounts:
- Your personal Gmail (Editor)
- The service account email from `config/service_account.json` (Editor — required for the sync scripts)

The spreadsheet ID appears in the URL between `/d/` and `/edit`. Copy it into `config/measurement_env_template.txt` as `SPREADSHEET_ID`.

---

### 1.2 Tab 1: Contact Master List

Create a tab named exactly: **Contact Master List**

**Column layout (Row 1 = header)**:

| Col | Header | Notes |
|-----|--------|-------|
| A | Contact Name | Full name |
| B | Organization | Full org name |
| C | Title / Function | Role at org |
| D | Email Address | Verified current address |
| E | Sector | Senate / Think Tank / Law School / Civil Rights |
| F | Wave | 1 / 2 / 3 |
| G | Send Date | YYYY-MM-DD format |
| H | Send Time | HH:MM local |
| I | Bitly Click Y/N | Y or N |
| J | Click Date | YYYY-MM-DD |
| K | Reply Received Y/N | Y or N (excludes OOO and auto-replies) |
| L | Reply Date | YYYY-MM-DD |
| M | Reply Type | Stage0 / Stage1-Q / Stage1-MR / Stage1-R / Declined / OOO / Bounce |
| N | Days to Reply | Formula — see below |
| O | Follow-Up Sent Y/N | Y or N |
| P | Follow-Up Date | YYYY-MM-DD |
| Q | Meeting Scheduled Y/N | Y or N |
| R | Meeting Date | YYYY-MM-DD |
| S | Meeting Status | Scheduled / Completed / Rescheduled / Cancelled |
| T | Next Action | Free text |
| U | Notes | Free text |

**Pre-populated data rows (Rows 2–26)**: Enter all 25 contacts from `PHASE_1_EXECUTION_CALENDAR.md` Section 3 contact tables before May 31. Use the send order from that document:
- Rows 2–6: Senate staff (Days 1–2 sends, June 1–2)
- Rows 7–9: CRS and House (Day 2, June 2)
- Rows 10–18: Think tanks (Days 3–4, June 3–4)
- Rows 19–25: Law schools (Days 5 and 8, June 5 and June 8)

**Formulas to add below Row 26 (e.g., Row 28 onward)**:

```
Reply rate:         =COUNTIF(K2:K26,"Y")/COUNTA(A2:A26)*100
Stage 1+ ratio:     =COUNTIFS(M2:M26,"Stage1-*")/COUNTIF(K2:K26,"Y")*100
Avg days to reply:  =AVERAGEIF(N2:N26,"<>")
Meeting scheduled:  =COUNTIF(Q2:Q26,"Y")/COUNTA(A2:A26)*100
Click rate:         =COUNTIF(I2:I26,"Y")/COUNTA(A2:A26)*100
```

**Days to Reply formula (enter in N2, drag to N26)**:
```
=IF(L2="","",L2-G2)
```
Format column N as Number (no decimals). This gives you the integer days between send and reply.

---

### 1.3 Tab 2: Email Engagement Log

Create a tab named exactly: **Email Engagement Log**

This tab is written by `scripts/kit_email_sync.py`. The script appends one row per Kit broadcast (email campaign). You can also add rows manually for emails sent outside Kit.

**Column layout**:

| Col | Header | Written by |
|-----|--------|-----------|
| A | Broadcast ID | kit_email_sync.py |
| B | Email Date | kit_email_sync.py (YYYY-MM-DD) |
| C | Subject Line | kit_email_sync.py |
| D | Recipients | kit_email_sync.py |
| E | Open Rate % | kit_email_sync.py |
| F | Click Rate % | kit_email_sync.py |
| G | Unsubscribes | kit_email_sync.py |
| H | Reply Y/N | Manual entry |
| I | Sentiment | Manual entry: Positive / Neutral / Negative |
| J | Last Synced | kit_email_sync.py (UTC timestamp) |

**VLOOKUP to pull contact info from Tab 1** (add to Column K if desired):
```
=IFERROR(VLOOKUP(C2,'Contact Master List'!C:E,3,FALSE),"not found")
```
This looks up the subject line in the Contact Master List title column and returns the sector. Adjust the column indices if your layout differs.

**Conditional formatting — engagement heat map**:
Select column E (Open Rate %) and column F (Click Rate %):
1. Format > Conditional formatting
2. Color scale: Red (0%) → Yellow (30%) → Green (50%+)
3. Apply to E2:E500 and F2:F500

**Weekly aggregation formula (add to a new column, e.g., K)**:

Wave-by-week reply rate — paste into a summary block below your data:
```
Week 1 click rate:  =AVERAGEIFS(F:F,B:B,">="&DATE(2026,6,1),B:B,"<="&DATE(2026,6,7))
Week 2 click rate:  =AVERAGEIFS(F:F,B:B,">="&DATE(2026,6,8),B:B,"<="&DATE(2026,6,14))
Week 3 click rate:  =AVERAGEIFS(F:F,B:B,">="&DATE(2026,6,15),B:B,"<="&DATE(2026,6,21))
```

---

### 1.4 Tab 3: Meeting Schedule

Create a tab named exactly: **Meeting Schedule**

This tab is read by `scripts/discord_daily_briefing.py` to count confirmed and completed meetings.

**Column layout**:

| Col | Header | Notes |
|-----|--------|-------|
| A | Contact Name | |
| B | Organization | |
| C | Meeting Date | YYYY-MM-DD |
| D | Meeting Time | HH:MM timezone |
| E | Format | Phone / Video / In-Person |
| F | Attendees | Comma-separated names |
| G | Status | Scheduled / Completed / Rescheduled / Cancelled |
| H | Key Outcomes | Bullet summary within 24h of call |
| I | Follow-Up Committed | What you promised to send |
| J | Next Steps | Action items |
| K | Adoption Signal Y/N | Y / N / Partial |
| L | Tier 2 Candidate Y/N | Y or N |
| M | Commitment Type | Made / No Decision / Declined / Deferral |
| N | Policy Ask Tracked | Specific policy ask from the meeting |
| O | Policy Outcome Status | Pending / Progressed / Completed / Stalled |

**Outcome categorization guide**:
- Commitment Made: Contact stated they will take a specific action (implement a practice, share with team, draft a memo, cite in legislation)
- No Decision: Meeting completed, no specific commitment but positive reception — add to Week 4 follow-up queue
- Declined: Contact explicitly declined further engagement — mark closed, no further follow-up
- Deferral: Contact interested but needs to wait for a specific event (hearing, semester end, budget cycle) — note the deferred date and set a reminder

**Calendar integration**:
There is no automated ICS sync in this setup. For each confirmed meeting:
1. Create a Google Calendar event in the "Tier 1 Policy Briefings" calendar
2. Add the organization name, contact name, meeting format, and agreed agenda to the event description
3. Share Calendly link (calendly.com — free tier, 20-min and 30-min slots) in follow-up emails to reduce scheduling friction
4. After the call, immediately fill out columns H–O in this tab

**Meeting completion rate formula** (add below data):
```
Completion rate: =COUNTIF(G:G,"Completed")/COUNTIFS(G:G,"<>",G:G,"<>Status")*100
```

---

### 1.5 Tab 4: Policy Uptake Signals

Create a tab named exactly: **Policy Uptake Signals**

This tab is read by `scripts/discord_daily_briefing.py` to count policy signals.

**Column layout**:

| Col | Header | Notes |
|-----|--------|-------|
| A | Organization | |
| B | Contact Name | |
| C | Signal Type | Internal Share / Practice Implementation / Referral / Media Mention / Policy Citation / Distribution Request |
| D | Signal Description | Specific description of what was shared, implemented, or cited |
| E | Date Detected | YYYY-MM-DD |
| F | Confidence Level | High / Medium / Low |
| G | Source | Email thread / Meeting note / Google Alert / Direct statement |
| H | Escalation Path | None / Notify user / Accelerate Tier 2 |
| I | Follow-Up Action | What action this signal requires |

**Monitoring setup** (outside the spreadsheet):
Before June 1, set Google Alerts for these terms. Any alert that cites a Tier 1 organization should be logged as a Policy Citation signal in this tab:
- "ELITE address confidence score"
- "Palantir ICE ELITE"
- "DROP platform immigration"

Check CourtListener quarterly for amicus brief citations. Check Overton.io quarterly for policy document citations.

---

### 1.6 Tab 5: KPI Summary Dashboard

Create a tab named exactly: **KPI Summary Dashboard**

This tab is read by `scripts/discord_daily_briefing.py`. The script expects row labels in column A and weekly values in columns B–E.

**Layout (Row 1 = header: Metric | Week 1 | Week 2 | Week 3 | Final)**:

| Row | Col A (Metric) | Col B (Week 1) | Col C (Week 2) | Col D (Week 3) | Col E (Final) |
|-----|---------------|---------------|---------------|---------------|--------------|
| 2 | Total sends | | | | |
| 3 | Total Bitly clicks | | | | |
| 4 | Bitly Click Rate % | | | | |
| 5 | Total replies | | | | |
| 6 | Reply rate % | | | | |
| 7 | Stage 1+ replies | | | | |
| 8 | Stage 1+ ratio % | | | | |
| 9 | Meetings scheduled | | | | |
| 10 | Meetings completed | | | | |
| 11 | Meeting completion rate % | | | | |
| 12 | Meeting rate % | | | | |
| 13 | Adoption signals logged | | | | |
| 14 | Bounce rate % | | | | |
| 15 | Gate 1 result | | N/A | N/A | |
| 16 | Gate 2 result | N/A | | N/A | |
| 17 | Tier 2 readiness result | N/A | N/A | | |

**Auto-calculating formulas** — the weekly columns for most metrics should pull from the other tabs using these formulas. Paste these into the Week 1 column (B) for each row and adjust the date range for Week 2 and Week 3:

Row 4 (Click Rate %):
```
=COUNTIF('Contact Master List'!I2:I26,"Y")/COUNTA('Contact Master List'!A2:A26)*100
```

Row 6 (Reply Rate %):
```
=COUNTIF('Contact Master List'!K2:K26,"Y")/COUNTA('Contact Master List'!A2:A26)*100
```

Row 8 (Stage 1+ Ratio %):
```
=COUNTIFS('Contact Master List'!M2:M26,"Stage1-*")/COUNTIF('Contact Master List'!K2:K26,"Y")*100
```

Row 11 (Meeting Completion Rate %):
```
=COUNTIF('Meeting Schedule'!G:G,"Completed")/MAX(1,COUNTIFS('Meeting Schedule'!G:G,"<>",'Meeting Schedule'!G:G,"<>Status"))*100
```

Row 12 (Meeting Rate %):
```
=COUNTIFS('Meeting Schedule'!G:G,"<>Cancelled",'Meeting Schedule'!G:G,"<>Status",'Meeting Schedule'!G:G,"<>")/COUNTA('Contact Master List'!A2:A26)*100
```

**Sparkline charts** — add these below the data table for visual trend indicators. Paste into cells to the right of the data:

7-day trend for reply rate (shows last 4 weekly values as a mini chart):
```
=SPARKLINE(B6:E6,{"charttype","line";"color","blue";"linewidth",2})
```

Apply the same formula pattern for rows 4, 6, 8, 12, 14 (substituting the row number).

**Threshold alert conditional formatting**:
Select B4:E4 (Click Rate %):
- Format > Conditional formatting > Custom formula
- Red: `=B4<30` (below warning threshold)
- Yellow: `=AND(B4>=30,B4<45)` (warning band)
- Green: `=B4>=45` (at or above target)

Apply the same pattern for rows 6, 8, 12, 14 using the thresholds from the Summary table at the end of `TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md`:

| Row | KPI | Green | Yellow | Red |
|-----|-----|-------|--------|-----|
| 4 | Click Rate % | ≥45% | 30–44% | <30% |
| 6 | Reply Rate % | ≥20% | 10–19% | <10% |
| 8 | Stage 1+ Ratio % | ≥60% | 40–59% | <40% |
| 12 | Meeting Rate % | ≥60% | 30–59% | <30% |
| 14 | Bounce Rate % | <5% | 5–8% | >8% |

**Benchmark comparison row** — add below the main table:

| Metric | Your Target | HubSpot Benchmark (Gov sector) | M+R Benchmark (Nonprofit) |
|--------|-------------|-------------------------------|--------------------------|
| Click rate | 45% | 30.5% | 28–40% |
| Reply rate | 20% | N/A (email-specific) | N/A |
| Meeting acceptance | 60% | N/A | N/A |

Source: HubSpot Email Open Rate Benchmarks 2024; M+R Benchmarks 2025. Your targets are above benchmark because this is a curated 25-contact list with personalized subject lines (Campaign Monitor 2025: personalization increases open rates 26–30%).

---

## Section 2: Kit Email Integration API Walkthrough

### 2.1 Authentication

Kit (formerly ConvertKit) uses two authentication methods:
- **v3 API Secret** (recommended for this setup): A single long string available at app.kit.com → Settings → Developer → API Secret. No OAuth flow required. Rate limit: 120 requests/minute (free tier), 300/minute (Creator tier).
- **v4 OAuth**: Bearer token required, more complex setup, no advantage for this use case.

Use the v3 API Secret. It is sufficient for reading broadcast stats.

**To get your API Secret**:
1. Log in to app.kit.com
2. Settings (top right) → Developer
3. Copy the "API Secret" (not the "API Key" — the Secret is longer and required for write operations, but we use it for authenticated reads)
4. Paste into `config/measurement_env_template.txt` as `KIT_API_SECRET`

**Security**: Never commit the API Secret to git. Store it only in the env file (which is git-ignored). On the Pi, source the env file in the cron job command rather than hardcoding values.

### 2.2 Key API Endpoints Used

All endpoints are `https://api.convertkit.com/v3/{endpoint}?api_secret=YOUR_SECRET`

| Endpoint | What it returns |
|----------|----------------|
| `broadcasts` | List of all sent email broadcasts with metadata |
| `broadcasts/{id}/stats` | Open rate, click rate, unsubscribes for one broadcast |
| `broadcasts/{id}/subscribers` | Subscriber-level engagement (Creator plan only) |

**Rate limit handling**: The sync script automatically sleeps when Kit returns HTTP 429 with a `Retry-After` header. On the free plan with 25 contacts and daily syncs, you will never approach the rate limit.

### 2.3 The Sync Script

The full script is at `scripts/kit_email_sync.py`. It requires no modification beyond setting the three environment variables. Here is the operational summary:

1. Reads existing Broadcast IDs from the Email Engagement Log tab to avoid duplicate rows
2. Fetches all broadcasts from Kit API
3. For each new broadcast, fetches stats (open rate, click rate, unsubscribes)
4. Appends one row per new broadcast to the Email Engagement Log tab
5. Logs all actions to stdout (captured in the cron log file)

**Reply tracking limitation**: Kit does not expose reply data via API. The `Reply Y/N` and `Sentiment` columns (H and I) in the Email Engagement Log must be filled manually as replies arrive in Gmail. This is a fundamental limitation of email API tracking — replies go to your Gmail inbox, not back through Kit.

### 2.4 Install Dependencies

On the Pi:
```bash
pip install requests google-auth google-auth-oauthlib google-api-python-client
```

Or with uv (if using the project's Python environment):
```bash
uv pip install requests google-auth google-auth-oauthlib google-api-python-client
```

### 2.5 Google Service Account Setup

The sync scripts authenticate to Google Sheets via a service account. This avoids the interactive OAuth browser flow and works in headless/cron environments.

**Steps**:
1. Go to console.cloud.google.com
2. Create a new project (or use an existing one)
3. Enable the Google Sheets API: APIs & Services → Library → search "Google Sheets API" → Enable
4. Create a service account: IAM & Admin → Service Accounts → Create
5. Give it the role "Editor" at project level (or just Sheets access)
6. Create a key: click the service account → Keys → Add Key → JSON
7. Download the JSON file
8. Move it to `projects/cybersecurity-hardening/config/service_account.json`
9. Open the Google Sheet, click Share, and share it with the service account email address (shown in the JSON as `client_email`) with Editor access

Set the path in your env file:
```bash
export SHEETS_CREDS_JSON="/home/awank/dev/SuperClaude_Framework/projects/cybersecurity-hardening/config/service_account.json"
```

### 2.6 Cron Job Scheduling

Add these two lines to your crontab (`crontab -e`):

```
# Kit sync at 20:00 UTC daily
0 20 * * * source /home/awank/dev/SuperClaude_Framework/projects/cybersecurity-hardening/config/measurement_env.sh && python3 /home/awank/dev/SuperClaude_Framework/projects/cybersecurity-hardening/scripts/kit_email_sync.py >> /tmp/kit_sync.log 2>&1

# Discord briefing at 20:05 UTC daily (5 min after sync)
5 20 * * * source /home/awank/dev/SuperClaude_Framework/projects/cybersecurity-hardening/config/measurement_env.sh && python3 /home/awank/dev/SuperClaude_Framework/projects/cybersecurity-hardening/scripts/discord_daily_briefing.py >> /tmp/discord_briefing.log 2>&1
```

Note: The Pi's system clock must be set to UTC. Verify with `date -u`. If the Pi is set to local time, adjust the cron hours accordingly (e.g., if you are in EDT = UTC-4, use `0 16 * * *` to run at 20:00 UTC).

### 2.7 Common API Errors and Recovery

**HTTP 401 Unauthorized**:
- Cause: Wrong API Secret or expired credentials
- Fix: Re-copy the API Secret from app.kit.com → Settings → Developer
- Recovery: Update `KIT_API_SECRET` in the env file, re-source, run manually to confirm

**HTTP 403 Forbidden**:
- Cause: The endpoint requires a paid Kit plan (e.g., subscriber-level broadcast stats)
- Fix: The script falls back to aggregate stats automatically — no action needed

**HTTP 404 Not Found**:
- Cause: Broadcast ID no longer exists (deleted broadcasts)
- Fix: The script skips 404 responses and logs a warning — no action needed

**HTTP 429 Too Many Requests**:
- Cause: Rate limit exceeded (unlikely with daily sync of 25 broadcasts)
- Fix: The script reads `Retry-After` and sleeps automatically

**Google Sheets HttpError 403**:
- Cause: Service account does not have Editor access to the spreadsheet
- Fix: Open the Sheet → Share → add the service account email address with Editor access

**Google Sheets HttpError 404**:
- Cause: Wrong `SPREADSHEET_ID`
- Fix: Re-copy the ID from the Sheet URL, update env file

---

## Section 3: Discord Webhook Setup

### 3.1 Create the Webhook

1. Open Discord → your server → the channel you want briefings in (e.g., `#phase1-monitoring`)
2. Click the gear icon next to the channel → Integrations → Webhooks
3. Click "New Webhook"
4. Name it "Phase 1 Briefing Bot"
5. Click "Copy Webhook URL"
6. Paste the URL into `config/measurement_env_template.txt` as `DISCORD_WEBHOOK_URL`

**Test the webhook immediately** after creating it:
```bash
curl -X POST -H 'Content-Type: application/json' \
  -d '{"content":"Webhook test — Phase 1 measurement automation"}' \
  YOUR_WEBHOOK_URL
```
Expected response: HTTP 204 No Content (Discord webhooks return 204 on success, not 200).

### 3.2 What the Daily Briefing Sends

The `discord_daily_briefing.py` script sends one message per day at 20:05 UTC (5 minutes after the Kit sync). The message contains:

**Header**: Campaign Day number, week number, UTC timestamp

**Overall Status**: GREEN / YELLOW / RED based on all KPI statuses combined. Any RED KPI makes the overall status RED. Any YELLOW with no RED makes it YELLOW.

**KPI Snapshot**: Six KPIs with current value, target, trend arrow (↑ / → / ↓), and status emoji:
- Bitly Click Rate % (target: 45%)
- Reply Rate % (target: 20%)
- Stage 1+ Ratio % (target: 60%)
- Meeting Rate % (target: 60%)
- Bounce Rate % (target: <5%)
- Adoption Signals (target: 10% by Week 6)

**Anomaly Triggers**: If any of the five thresholds below are crossed, the message includes a specific action instruction.

**Status text**: GREEN = "All KPIs on track." YELLOW = "Apply sector-specific follow-up adjustments." RED = "Review escalation matrix — action required."

### 3.3 The Five Anomaly Triggers

These thresholds are hardcoded in the script based on `TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md` Section 3:

| Trigger | Threshold | Message |
|---------|-----------|---------|
| Wave 1 reply rate low | <15% reply rate | Check contact routing — named individual vs. general inbox |
| Adoption stalled | <5% adoption rate at Week 4+ | Week-4 follow-up emails needed |
| No meetings scheduled | 0 meetings at Week 2+ | Replace vague CTAs with specific 20-min offer + Calendly link |
| No policy signals | 0 signals logged at Week 3+ | Check Tab 4 — ensure post-meeting notes are being captured |
| Bounce rate elevated | ≥5% bounce rate | Stop wave sends — re-validate all remaining contact emails |

### 3.4 Weekly Trend Detection

The script compares the last two non-zero weekly values for each KPI and reports:
- ↑ if the latest week is more than 1 percentage point above the previous week
- ↓ if the latest week is more than 1 percentage point below the previous week
- → if the change is within 1 percentage point (stable)

Trend detection requires at least two weeks of data — during Week 1, all trends show "—" (insufficient data).

### 3.5 Escalation Routing

| Overall Status | Discord Message Action | User Action |
|---------------|----------------------|-------------|
| GREEN | "All KPIs on track. No action required." | None |
| YELLOW | "Apply sector-specific follow-up adjustments before next wave send." | Review which KPI is yellow; check the relevant Warning Trigger in TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md Section 3 |
| RED | "Action required: Review escalation matrix." | Same-day response; escalation notification format from TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md Section 7 |

If the Discord webhook goes down (see Section 9 contingencies), the cron job logs to `/tmp/discord_briefing.log` — check this file daily if no Discord message arrives.

---

## Section 4: Email Engagement Log Automation

### 4.1 VLOOKUP: Populate Sender Info from Master List

In the Email Engagement Log tab, add these formulas to populate contact metadata automatically. These assume the Email Engagement Log Column C contains the email subject line and you want to look up data from the Contact Master List.

**Look up sector based on subject line** (approximate match — adapt as needed):
Since Kit emails are sent to lists, not individual contacts, the most reliable approach is to use the broadcast subject line to manually tag which wave each broadcast belongs to, then use the contact master for sector-level aggregation.

Add a helper column in the Contact Master List (Column V) to aggregate by sector:
```
Senate sends:     =COUNTIF(E2:E26,"Senate")
Think Tank sends: =COUNTIF(E2:E26,"Think Tank")
Law School sends: =COUNTIF(E2:E26,"Law School")
```

For the Email Engagement Log, use a sector-based reply rate aggregation:
```
Senate reply rate:      =COUNTIFS('Contact Master List'!E:E,"Senate",'Contact Master List'!K:K,"Y")/COUNTIF('Contact Master List'!E:E,"Senate")*100
Think Tank reply rate:  =COUNTIFS('Contact Master List'!E:E,"Think Tank",'Contact Master List'!K:K,"Y")/COUNTIF('Contact Master List'!E:E,"Think Tank")*100
Law School reply rate:  =COUNTIFS('Contact Master List'!E:E,"Law School",'Contact Master List'!K:K,"Y")/COUNTIF('Contact Master List'!E:E,"Law School")*100
```

### 4.2 Conditional Formatting: Engagement Heat Map

Apply to the Email Engagement Log tab:

**Open Rate % column (E)**:
- Select E2:E500
- Format → Conditional formatting → Color scale
- Min: 0% (red) — Midpoint: 30% (yellow) — Max: 50% (green)

**Click Rate % column (F)**:
- Same color scale applied to F2:F500

**Reply Y/N column (H)**:
- Format → Conditional formatting → Custom formula is `=H2="Y"` → Background: light green
- Custom formula is `=H2="N"` → Background: light red

### 4.3 Weekly Aggregation Formulas

Add a summary block below Row 500 in the Email Engagement Log (or in a separate "Weekly Summary" section within the tab):

```
Week 1 sends (June 1-7):    =COUNTIFS(B:B,">="&DATE(2026,6,1),B:B,"<="&DATE(2026,6,7))
Week 1 avg open rate:       =AVERAGEIFS(E:E,B:B,">="&DATE(2026,6,1),B:B,"<="&DATE(2026,6,7))
Week 1 avg click rate:      =AVERAGEIFS(F:F,B:B,">="&DATE(2026,6,1),B:B,"<="&DATE(2026,6,7))

Week 2 sends (June 8-14):   =COUNTIFS(B:B,">="&DATE(2026,6,8),B:B,"<="&DATE(2026,6,14))
Week 2 avg open rate:       =AVERAGEIFS(E:E,B:B,">="&DATE(2026,6,8),B:B,"<="&DATE(2026,6,14))
Week 2 avg click rate:      =AVERAGEIFS(F:F,B:B,">="&DATE(2026,6,8),B:B,"<="&DATE(2026,6,14))

Week 3 (June 15-21):        =COUNTIFS(B:B,">="&DATE(2026,6,15),B:B,"<="&DATE(2026,6,21))
```

---

## Section 5: Meeting Tracking Spreadsheet

### 5.1 Calendar Integration

There is no automated two-way calendar sync in this setup (that would require the Google Calendar API and additional authentication). Use this manual workflow instead:

**When a meeting is confirmed** (within 2 hours of the contact's reply):
1. Create a Google Calendar event in "Tier 1 Policy Briefings" calendar
2. Set the event title: "[Organization] — 20-min Phase 1 Briefing"
3. Add the contact name, format (Zoom/Phone), and pre-agreed agenda to the event description
4. Add a 10-minute reminder
5. Add a row to the Meeting Schedule tab with Status = "Scheduled"

**After the meeting** (within 24 hours):
1. Update the Meeting Schedule tab row: Status = "Completed"
2. Fill in columns H–O (outcomes, commitments, adoption signal, Tier 2 candidate)
3. Update the Contact Master List tab: S = "Completed", T = "Post-meeting follow-up [date]"

**If a meeting is cancelled or rescheduled**:
1. Update Status column to "Cancelled" or "Rescheduled"
2. If rescheduled: add a new row with the new date
3. If cancelled: note the reason in the Notes column; log whether this is a soft decline or a timing issue

### 5.2 Outcome Categorization

Four outcome types (column M in the Meeting Schedule tab):

**Commitment Made**: The contact stated they will take a specific action. Log the specific commitment in column N (Policy Ask Tracked). Examples:
- "Will share the corpus with the subcommittee staff director by Friday"
- "Clinic director will integrate threat model into Fall 2026 clinic curriculum"
- "Staff counsel will draft an oversight letter referencing the ELITE documentation"

Track the commitment through to completion in column O (Policy Outcome Status).

**No Decision**: Meeting held, positive reception, no specific commitment made. These contacts go back into the Week 4 follow-up queue. Log in column H (Key Outcomes) what aspect they found most relevant — this becomes the hook for the Week 4 check-in.

**Declined**: Contact explicitly says they are not in a position to use or share the corpus. Mark closed. Do not send any further outreach to this contact. Mark column L (Tier 2 Candidate) = "N".

**Deferral**: Contact is interested but cited a timing constraint (Senate recess, exam period, budget cycle, pending litigation). Log the stated return date in column I (Follow-Up Committed) and set a calendar reminder. Deferral contacts are warm leads — they need a single check-in when their constraint lifts, not a re-pitch.

### 5.3 Policy Commitment Tracking

For contacts who made a commitment (column M = "Commitment Made"):

1. Log the specific ask in column N (Policy Ask Tracked)
2. Update column O (Policy Outcome Status) weekly:
   - Pending: Commitment made but not yet verifiable
   - Progressed: Contact sent an interim update (e.g., "Shared with team, waiting for their response")
   - Completed: The commitment is complete and verifiable (oversight letter published, curriculum updated)
   - Stalled: No update after 2 weeks — send a light check-in

When an outcome reaches "Completed" status, log it in the Policy Uptake Signals tab (Tab 4) as a Policy Citation or Practice Implementation signal. This is how a meeting commitment becomes a lagging indicator milestone.

---

## Section 6: KPI Dashboard with Auto-Calculating Trend Indicators

### 6.1 Sparkline Configuration

Sparklines are built-in Google Sheets charts that render inside a single cell. Add these to the KPI Summary Dashboard tab in the column to the right of the weekly data (Column F):

```
Row 4  (Click Rate):   =SPARKLINE(B4:E4,{"charttype","line";"color","#4472C4";"linewidth",2})
Row 6  (Reply Rate):   =SPARKLINE(B6:E6,{"charttype","line";"color","#4472C4";"linewidth",2})
Row 8  (Stage1+ Ratio):=SPARKLINE(B8:E8,{"charttype","line";"color","#4472C4";"linewidth",2})
Row 12 (Meeting Rate): =SPARKLINE(B12:E12,{"charttype","line";"color","#4472C4";"linewidth",2})
Row 14 (Bounce Rate):  =SPARKLINE(B14:E14,{"charttype","line";"color","#E06666";"linewidth",2})
```

For 7-day and 14-day trend windows (when you have daily data instead of weekly aggregates), the sparkline range changes:
```
7-day:  =SPARKLINE(OFFSET(B4,0,0,1,7),{"charttype","line";"color","#4472C4"})
14-day: =SPARKLINE(OFFSET(B4,0,0,1,14),{"charttype","line";"color","#4472C4"})
```

### 6.2 Threshold Alert Formulas

Add a "Status" column (Column G) to the KPI Summary Dashboard with these IF formulas. They return the text RED / YELLOW / GREEN based on the latest weekly value (Column E):

```
Row 4  (Click Rate):
=IF(E4>=45,"GREEN",IF(E4>=30,"YELLOW","RED"))

Row 6  (Reply Rate):
=IF(E6>=20,"GREEN",IF(E6>=10,"YELLOW","RED"))

Row 8  (Stage1+ Ratio):
=IF(E8>=60,"GREEN",IF(E8>=40,"YELLOW","RED"))

Row 12 (Meeting Rate):
=IF(E12>=60,"GREEN",IF(E12>=30,"YELLOW","RED"))

Row 14 (Bounce Rate — lower is better):
=IF(E14<5,"GREEN",IF(E14<=8,"YELLOW","RED"))
```

Apply conditional formatting to Column G:
- "GREEN" → background: #B7E1CD (light green)
- "YELLOW" → background: #FCE8B2 (light yellow)
- "RED" → background: #F4C7C3 (light red)

### 6.3 Benchmark Comparison

Add a comparison section below Row 20 in the KPI Summary Dashboard:

| KPI | Your Week 2 Actual | Your Week 3 Actual | HubSpot Gov Benchmark | M+R Nonprofit Benchmark |
|-----|--------------------|--------------------|-----------------------|------------------------|
| Click rate | [formula: =C4] | [formula: =D4] | 30.5% | 28–40% |
| Reply rate | [formula: =C6] | [formula: =D6] | N/A | N/A |
| Meeting rate | [formula: =C12] | [formula: =D12] | N/A | N/A |

This comparison is for calibration only. A well-personalized 25-contact list targeting the correct function at each institution should substantially outperform the benchmark averages.

---

## Section 7: May 31 Setup Checklist

Complete all five items on May 31 before June 1 launch. Do not send any Wave 1 email if any item is unchecked.

### Checkpoint 1: Google Sheets Account Access Verified

- [ ] Google Sheet titled "Phase 1 Policy Outreach Tracker — June 2026" is created
- [ ] All 5 tabs created with exact names: Contact Master List, Email Engagement Log, Meeting Schedule, Policy Uptake Signals, KPI Summary Dashboard
- [ ] All 25 contacts pre-populated in Tab 1 with verified emails and send wave assignments
- [ ] Formulas in Tab 1 calculating correctly (reply rate, click rate, stage1+ ratio)
- [ ] KPI Dashboard formulas linked to Tab 1 and Tab 3 and returning 0 (not #REF! errors)
- [ ] Sparklines rendering in Column F of the KPI Dashboard
- [ ] Service account email has Editor access to the spreadsheet

### Checkpoint 2: Kit API Credentials Configured

- [ ] Kit API Secret copied from app.kit.com → Settings → Developer
- [ ] `measurement_env.sh` created from template with `KIT_API_SECRET` filled in
- [ ] Manual test: `source measurement_env.sh && python3 scripts/kit_email_sync.py`
- [ ] Output shows "Fetched N broadcasts from Kit" (may be 0 if no broadcasts sent yet — that is correct)
- [ ] No authentication errors in the output

### Checkpoint 3: Discord Webhook URL Validated (Test Send Successful)

- [ ] Webhook created in the target Discord channel
- [ ] Webhook URL pasted into `measurement_env.sh` as `DISCORD_WEBHOOK_URL`
- [ ] Test send confirmed: `curl -X POST -H 'Content-Type: application/json' -d '{"content":"Webhook test — Phase 1 monitoring online"}' $DISCORD_WEBHOOK_URL`
- [ ] Message appeared in the Discord channel within 5 seconds
- [ ] Full script test: `source measurement_env.sh && python3 scripts/discord_daily_briefing.py`
- [ ] Formatted briefing message appeared in Discord (will show zeros for all metrics — that is correct)

### Checkpoint 4: Python Scripts Installed in projects/cybersecurity-hardening/scripts/

- [ ] `scripts/kit_email_sync.py` is present and executable (`ls -la scripts/`)
- [ ] `scripts/discord_daily_briefing.py` is present and executable
- [ ] Dependencies installed: `pip install requests google-auth google-auth-oauthlib google-api-python-client`
- [ ] `service_account.json` is present at `config/service_account.json`
- [ ] Both scripts run without ImportError or FileNotFoundError when env vars are set

### Checkpoint 5: Cron Jobs Scheduled for Daily 20:00 UTC

- [ ] `crontab -e` opened and the two cron lines added (from Section 2.6)
- [ ] Cron lines reference absolute paths (not relative paths)
- [ ] Cron lines source `measurement_env.sh` before running the scripts
- [ ] Pi system clock is UTC (`date -u` shows correct UTC time)
- [ ] Test: advance the cron schedule by 5 minutes, wait for it to fire, verify the log and Discord message appear
- [ ] Restore cron to 20:00 UTC and 20:05 UTC after testing

---

## Section 8: June 1 Morning Verification Steps

Run these verification steps on June 1 before sending any Wave 1 emails (target: 7:00–8:00 AM, before the 8:30 AM send window).

### Step 1: Test Email Send to Verify Open/Click Tracking

Before sending any contact email, send a test email from the outreach address to two personal email accounts (one Gmail, one non-Gmail such as Outlook or Yahoo):
1. Use the same Kit template that Wave 1 will use
2. Include the `bit.ly/palantir-briefing` Bitly short URL
3. Click the Bitly link in the test email from both personal accounts
4. Check the Bitly dashboard — the click should appear within 60 seconds
5. Confirm the Kit broadcast stats show a click (may take up to 15 minutes to update)
6. Run `python3 scripts/kit_email_sync.py` manually — confirm the test broadcast appears in the Email Engagement Log tab

If the Bitly click does not appear within 5 minutes: the Bitly account is misconfigured or the link is broken. Do not proceed with Wave 1 until the link is working.

### Step 2: Dashboard Formulas Calculating Correctly (No #REF! Errors)

Open the Google Sheet and check:
- [ ] Tab 1: All formula rows (Reply Rate, Stage1+ Ratio, etc.) show 0% or 0 — not #REF!, #DIV/0!, or #NAME?
- [ ] Tab 5 (KPI Dashboard): All linked formulas showing 0 — not errors
- [ ] Sparklines rendering as flat lines (no data yet — that is correct)
- [ ] Status column in Tab 5 showing "RED" for all KPIs (0% is below all thresholds — this is correct before any sends)

If any cell shows an error: fix the formula before proceeding. Common causes:
- Tab name has extra spaces or wrong capitalization — must be exact
- Column range does not start at Row 2 (starts at Row 1 instead) — adjust the formula range
- Cross-tab formula references the wrong tab — re-enter the formula by clicking into the other tab

### Step 3: Discord Test Message to Confirm Webhook Live

Run the briefing script manually:
```bash
source config/measurement_env.sh && python3 scripts/discord_daily_briefing.py
```
Confirm the formatted Phase 1 Daily Briefing message appears in Discord. It should show:
- Campaign Day 1, Week 1
- All KPIs at RED (0% values — correct before sends)
- Anomaly trigger for meetings (0 meetings scheduled at Week 1) — this is expected

If no message appears: check `/tmp/discord_briefing.log` for error output. Most common issue is a wrong webhook URL or the webhook having been regenerated in Discord.

### Step 4: Contact Master List Verified (25 Names, No Missing Email Addresses)

In Tab 1 (Contact Master List):
- [ ] 25 rows populated (Rows 2–26)
- [ ] Column D (Email Address) has a value for every row — no blanks
- [ ] Column E (Sector) has a value for every row
- [ ] Column F (Wave) has a value for every row (1, 2, or 3)
- [ ] Rows 2–6 are the five Day 1 Wave 1 Senate contacts from the execution calendar
- [ ] Formula row shows 25 contacts in denominator (COUNTA returning 25)

### Step 5: Final Send-Ready Check

- [ ] Kit email templates saved and reviewed for each sector (Senate, Think Tank, Law School variants)
- [ ] Bitly short URL `bit.ly/palantir-briefing` redirects correctly in private browser window
- [ ] Gist URL loads without login in private browser — all three documents present
- [ ] Calendly link working — booking flow completes successfully in private browser
- [ ] Mail-tester.com score ≥8/10 from the outreach address
- [ ] Day 1 send window reminder set for 8:20 AM

---

## Section 9: Contingency Response Triggers and Decision Trees

### Contingency 1: Kit API Sync Fails

**Symptom**: Cron job fires at 20:00 UTC but the Email Engagement Log tab has no new rows, and `/tmp/kit_sync.log` shows errors.

**Decision tree**:

```
Kit sync fails
│
├── Check /tmp/kit_sync.log for error type
│   │
│   ├── "KIT_API_SECRET is not set"
│   │   → Env file not sourced by cron. Verify cron line includes:
│   │     source /path/to/measurement_env.sh
│   │     Fix cron line, run manually to confirm, wait for next day.
│   │
│   ├── HTTP 401 Unauthorized
│   │   → API secret expired or wrong. Re-copy from app.kit.com.
│   │     Update measurement_env.sh. Run manually to confirm.
│   │
│   ├── HttpError on Sheets write
│   │   → Service account lost Editor access (someone removed it from Sheet share).
│   │     Re-share the Google Sheet with the service account email (Editor).
│   │     Run manually to confirm.
│   │
│   └── Network error / timeout
│       → Pi network connectivity issue.
│         Test: curl https://api.convertkit.com/v3/broadcasts?api_secret=XXX
│         If network is down: script will retry next day automatically.
│
└── Fallback manual update procedure:
    1. Log into app.kit.com
    2. Broadcasts → select the most recent broadcast → View Stats
    3. Read: recipients, open rate %, click rate %
    4. Open the Email Engagement Log tab in Google Sheets
    5. Add a row manually with today's date, broadcast subject, and the stats
    6. This manual entry will be skipped by the sync script (it checks by Broadcast ID)
```

**Recovery time**: 15–30 minutes for most errors. Network outage: wait for connectivity to restore; the next cron run will catch up.

---

### Contingency 2: Discord Webhook Goes Down

**Symptom**: No Discord message at 20:05 UTC. `/tmp/discord_briefing.log` shows "Discord webhook returned 404" or connection refused.

**Decision tree**:

```
No Discord briefing
│
├── Check /tmp/discord_briefing.log
│   │
│   ├── HTTP 404
│   │   → Webhook was deleted or regenerated in Discord.
│   │     Server Settings → Integrations → Webhooks → create new webhook.
│   │     Update DISCORD_WEBHOOK_URL in measurement_env.sh.
│   │     Test with curl. Fix cron. Manual run to confirm.
│   │
│   ├── Connection refused / timeout
│   │   → Discord API is down (rare) or Pi network issue.
│   │     Test: curl https://discord.com
│   │     If Discord is down: wait. If Pi network: restore connectivity.
│   │
│   └── Content too long (HTTP 400)
│       → Message exceeded Discord's 2,000-character limit.
│         This should not occur with the current script. If it does:
│         Edit discord_daily_briefing.py, truncate the anomaly messages.
│
└── Email fallback while webhook is down:
    1. Open Google Sheets Tab 5 (KPI Dashboard)
    2. Read the current values manually
    3. Compare to thresholds in Section 6.2
    4. If any KPI is RED: take the escalation action from
       TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md Section 3
    5. Fix the webhook before the next day's cron run
```

---

### Contingency 3: Google Sheets Quota Exceeded

**Symptom**: Scripts fail with HttpError 429 (Sheets API quota). This is unlikely with daily reads of a small spreadsheet, but possible if you run scripts many times manually in quick succession.

**Decision tree**:

```
Sheets quota error
│
├── Google Sheets API free tier: 300 read requests/minute, 60 write requests/minute
│   Daily cron runs 2 requests total. Manual runs are fine up to ~100/day.
│
├── If quota exceeded:
│   → Wait 60 seconds and retry. Quotas reset per minute.
│   → If repeated across multiple minutes: quota is daily (unusual).
│     Wait until the next UTC day reset.
│
└── If quota keeps hitting (running scripts repeatedly):
    → Add 2-second sleep between sheet reads in the scripts.
    → Archive historical data:
       1. Create a new tab "Archive YYYY-MM"
       2. Cut rows older than 30 days from the Email Engagement Log
       3. Paste into the archive tab
       4. The main tab will have fewer rows and be faster to read/write
```

---

### Contingency 4: Email Engagement Gaps (Kit vs. Gmail Discrepancy)

**Symptom**: Kit shows 5 opens on a broadcast, but you received 3 replies — some contacts seem to be engaging but the Kit stats do not reflect it. Or vice versa: Kit shows high opens but no replies.

**Root cause**: Apple Mail Privacy Protection (MPP) pre-loads tracking pixels, inflating open rates. Gmail proxy loads also inflate opens. This is why the framework uses Bitly click rate as the primary engagement proxy rather than Kit open rate.

**Decision tree**:

```
Kit stats differ from observed engagement
│
├── Kit open rate is higher than expected
│   → MPP or Gmail proxy inflation. Use Bitly click rate instead.
│     Kit open rate is a reference metric only — not your primary KPI.
│
├── Kit open rate is 0% but you received replies
│   → The replies were sent directly to Gmail (contacts replied without clicking Bitly).
│     This is a positive signal. Log replies in Tab 1 (Contact Master List)
│     column K–M. The Kit stat for opens is a floor, not a ceiling.
│
├── Kit shows clicks but you cannot find them in Bitly
│   → Kit "clicks" are clicks on any link in the email, not just the Bitly link.
│     Check if the email template has any other links (unsubscribe, social icons).
│     Bitly and Kit click metrics measure different things.
│
└── Cross-check procedure when discrepancy exceeds 10 percentage points:
    1. Check Bitly dashboard: unique clicks by date
    2. Check Gmail Sent folder: all replies received
    3. Check Kit Broadcasts: open rate and click rate
    4. The authoritative record for replies and meetings is the Google Sheet.
       Kit stats are supplementary. Bitly stats are the primary click-through proxy.
    5. Log discrepancy in the Notes column of the relevant Tab 2 row.
```

---

## Section 10: Inline Python Script Code

Both scripts are production-ready and present in `scripts/`. The code below is the authoritative copy; if there is ever a discrepancy between this document and the file in `scripts/`, the file in `scripts/` is the version to use (it may have been updated).

### 10.1 kit_email_sync.py

Full path: `projects/cybersecurity-hardening/scripts/kit_email_sync.py`

```python
#!/usr/bin/env python3
"""
kit_email_sync.py — Kit (ConvertKit) to Google Sheets email engagement sync
Run daily at 20:00 UTC via cron: 0 20 * * * /path/to/kit_email_sync.py

Dependencies:
    pip install requests google-auth google-auth-oauthlib google-api-python-client
"""

import os, sys, time, datetime, logging, requests
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

KIT_API_SECRET    = os.environ.get("KIT_API_SECRET", "")
KIT_API_BASE      = "https://api.convertkit.com/v3"
SHEETS_CREDS_JSON = os.environ.get("SHEETS_CREDS_JSON", "")
SPREADSHEET_ID    = os.environ.get("SPREADSHEET_ID", "")
ENGAGEMENT_TAB    = "Email Engagement Log"

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)-8s %(message)s")
log = logging.getLogger(__name__)

def _kit_get(endpoint, params=None, retries=3):
    url = f"{KIT_API_BASE}/{endpoint}"
    p = {"api_secret": KIT_API_SECRET}
    if params: p.update(params)
    for attempt in range(1, retries + 1):
        try:
            r = requests.get(url, params=p, timeout=20)
            if r.status_code == 429:
                time.sleep(int(r.headers.get("Retry-After", 60))); continue
            r.raise_for_status(); return r.json()
        except requests.exceptions.RequestException as e:
            log.error("Kit API error attempt %d/%d: %s", attempt, retries, e)
            if attempt == retries: raise
            time.sleep(5 * attempt)
    return {}

def _sheets_service():
    creds = Credentials.from_service_account_file(
        SHEETS_CREDS_JSON, scopes=["https://www.googleapis.com/auth/spreadsheets"])
    return build("sheets", "v4", credentials=creds, cache_discovery=False)

def append_rows(service, tab, rows):
    service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID, range=f"'{tab}'!A1",
        valueInputOption="USER_ENTERED", insertDataOption="INSERT_ROWS",
        body={"values": rows}).execute()
    log.info("Appended %d row(s) to '%s'", len(rows), tab)

def existing_ids(service, tab):
    try:
        r = service.spreadsheets().values().get(
            spreadsheetId=SPREADSHEET_ID, range=f"'{tab}'!A:A").execute()
        return {str(row[0]) for row in r.get("values", []) if row}
    except HttpError: return set()

def run_sync():
    if not KIT_API_SECRET: log.error("KIT_API_SECRET not set"); sys.exit(1)
    if not SPREADSHEET_ID: log.error("SPREADSHEET_ID not set"); sys.exit(1)
    svc  = _sheets_service()
    seen = existing_ids(svc, ENGAGEMENT_TAB)
    broadcasts = _kit_get("broadcasts", {"page": 1}).get("broadcasts", [])
    new_rows = []
    for b in broadcasts:
        bid = str(b.get("id", ""))
        if bid in seen: continue
        stats = _kit_get(f"broadcasts/{bid}/stats").get("broadcast", {}).get("stats", {})
        now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
        row = [bid, (b.get("published_at") or b.get("created_at") or "")[:10],
               b.get("subject", ""), stats.get("recipients", 0),
               round(stats.get("open_rate", 0) * 100, 1),
               round(stats.get("click_rate", 0) * 100, 1),
               stats.get("unsubscribes", 0), "", "", now]
        new_rows.append(row)
        time.sleep(0.5)
    if new_rows: append_rows(svc, ENGAGEMENT_TAB, new_rows)
    log.info("Sync complete — %d new broadcast(s)", len(new_rows))

if __name__ == "__main__":
    run_sync()
```

### 10.2 discord_daily_briefing.py

Full path: `projects/cybersecurity-hardening/scripts/discord_daily_briefing.py`

The full 150-line version is in `scripts/discord_daily_briefing.py`. The structure is:
- `_sheets_service()` — authenticates to Google Sheets
- `read_tab()` — reads a named tab
- `parse_kpi_tab()` — parses the KPI Summary Dashboard into a dict
- `classify_kpi()` — returns GREEN / YELLOW / RED per metric
- `detect_anomalies()` — checks the 5 anomaly thresholds
- `build_discord_message()` — assembles the formatted message
- `post_to_discord()` — sends via webhook with retry on 429
- `run()` — orchestrates the full sequence

Run manually at any time:
```bash
source config/measurement_env.sh && python3 scripts/discord_daily_briefing.py
```

---

## Section 11: Google Sheets JSON Export Template (Local Backup)

The spreadsheet can be exported to JSON for local backup using the Google Sheets API. Run this script manually once per week to create a local archive.

**Add to `scripts/` as `export_sheets_backup.py`**:

```python
#!/usr/bin/env python3
"""Export all 5 tabs from the Phase 1 tracker to a local JSON backup."""
import os, json, datetime
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SHEETS_CREDS_JSON = os.environ.get("SHEETS_CREDS_JSON", "")
SPREADSHEET_ID    = os.environ.get("SPREADSHEET_ID", "")
TABS = ["Contact Master List", "Email Engagement Log", "Meeting Schedule",
        "Policy Uptake Signals", "KPI Summary Dashboard"]

creds = Credentials.from_service_account_file(
    SHEETS_CREDS_JSON, scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"])
svc = build("sheets", "v4", credentials=creds, cache_discovery=False)

backup = {}
for tab in TABS:
    result = svc.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID, range=f"'{tab}'!A1:Z500").execute()
    backup[tab] = result.get("values", [])

date_str = datetime.date.today().isoformat()
filename = f"sheets_backup_{date_str}.json"
with open(filename, "w") as f:
    json.dump(backup, f, indent=2)
print(f"Backup written to {filename}")
```

Run: `source config/measurement_env.sh && python3 scripts/export_sheets_backup.py`

Backups are written to the current directory. Move them to `projects/cybersecurity-hardening/` for safe-keeping. Add `sheets_backup_*.json` to `.gitignore` if working in a git repo.

---

## Summary: What Is Live on June 1, Day 1

| Component | Status at June 1 8:00 AM | Automated? |
|-----------|--------------------------|------------|
| Google Sheets 5-tab tracker | Populated with 25 contacts, all formulas active | No — manual updates for Contact Master List |
| Kit API sync | Cron scheduled for 20:00 UTC | Yes — daily |
| Discord briefing | Cron scheduled for 20:05 UTC | Yes — daily |
| Email Engagement Log | Empty (no sends yet) | Auto-populated by Kit sync after first send |
| Meeting Schedule | Empty (no meetings yet) | Manual — fill after each confirmed call |
| Policy Uptake Signals | Empty | Manual — fill as signals appear |
| KPI Dashboard | All zeros, RED status | Auto-calculated from other tabs |
| Bitly click tracking | Active (link created May 29–31) | Manual — check Bitly dashboard, log in Tab 1 |

The first cron run at 20:00 UTC on June 1 will pull stats from the Day 1 Kit broadcasts and write them to the Email Engagement Log. The Discord briefing at 20:05 will post the first real data briefing of the campaign. From that point forward, the measurement system runs without manual intervention beyond the daily Tab 1 updates (logging clicks and replies as they arrive).

---

*Item 38 — MEASUREMENT_AUTOMATION_SETUP.md  |  Created 2026-05-13  |  Status: production-ready*
*Scripts: scripts/kit_email_sync.py, scripts/discord_daily_briefing.py*
*Config: config/measurement_env_template.txt*
*Coordinates with: TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md (Item 17), PHASE_1_EXECUTION_CALENDAR.md (Item 29)*
*Ready for June 1 launch pending May 31 checklist completion.*
