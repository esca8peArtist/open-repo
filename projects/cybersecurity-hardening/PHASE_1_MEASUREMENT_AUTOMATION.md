---
title: "Phase 1 Measurement Automation — No-Code Setup Guide"
project: cybersecurity-hardening
created: 2026-05-13
version: 1.0
status: production-ready
item: 38 — Phase 1 Measurement Automation
phase: Phase 1 (launch June 1, 2026; arm May 31)
audience: "User with basic Google Sheets experience; no email marketing automation background"
depends-on:
  - TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md (Item 17 — KPIs, thresholds, sector benchmarks)
  - PHASE_1_EXECUTION_CALENDAR.md (Item 29 — 25 contacts, send schedule, gate dates)
  - MEASUREMENT_AUTOMATION_SETUP.md (Item 38 — technical Python/API version for Pi cron jobs)
tool-stack: "Gmail, Google Sheets, Bitly, Zapier free tier, Discord webhook, Calendly free tier"
---

# Phase 1 Measurement Automation
## No-Code Setup Guide — Arm by May 31, Live June 1

**Lead finding**: The biggest risk to Phase 1 is not a poor response rate — it is a poor response rate that goes unnoticed for five days while follow-up windows close. This system eliminates that risk. It does not require any coding. Every tool used here has a free tier. Total setup time is 3–4 hours. Arm it the evening of May 31. Do not send the first Wave 1 email until all five checkpoints below are verified.

**Relationship to the technical setup document**: This document is the no-code version of `MEASUREMENT_AUTOMATION_SETUP.md`. If you are running the Pi cron jobs and Python scripts described in that document, you do not need to set up the Zapier automations described here — the Pi scripts cover the same functions with more precision. Use this document if you want to arm the measurement system without touching the command line, or as a fallback if the Pi is unavailable.

---

## MEASUREMENT GO/NO-GO CHECKLIST

Complete all five items before the June 1 morning send. These are binary — each is either armed or it is not. "Mostly set up" does not count.

**Item 1: Google Sheets tracker is populated with all 25 contacts and all formulas return numbers, not errors.**
Open the sheet. Confirm 25 rows in the Contact Master List. Confirm the KPI Summary tab shows 0% for all metrics (not #REF! or #DIV/0!). If any cell shows an error formula, do not send until it is fixed.

**Item 2: Bitly link is live and returning click data.**
Open `bit.ly/palantir-briefing` in a private browser window. The corpus Gist must load. Then open the Bitly dashboard and confirm the click registered within 60 seconds. If the link is broken, Wave 1 has zero click tracking.

**Item 3: Discord webhook is delivering messages.**
Run the test command (Section 3, step 5). The formatted test message must appear in your Discord channel. If it does not appear, the daily briefing will not fire — you will be monitoring blind.

**Item 4: Gmail labels are created and the outreach-sent label is applied to every test send.**
See Section 1.3. The label structure takes 8 minutes to create. It is required for the Zapier automations to route correctly.

**Item 5: Zapier automations are live and have been tested with at least one real email send to a personal address.**
The Zapier zaps (Section 1.4) need at least one successful test run. "Turned on" is not sufficient — run the test with a real email to yourself and confirm the Sheet row updates.

If any of these five items is not verified, delay the send. Phase 1 has no retroactive data recovery. Click and reply events that happen before tracking is armed are permanently lost.

---

## Section 1: Email Tracking Setup

Phase 1 outreach is sent from Gmail. Gmail does not natively support click tracking or reply notifications to a spreadsheet. This section adds that capability using two tools: Bitly (click tracking) and Zapier (reply and label automation). Neither requires a paid account for a 25-contact campaign.

### 1.1 Bitly Click Tracking Setup

Bitly creates a short URL that redirects to the corpus Gist. Every time a contact clicks the link in your email, Bitly records it. This is your primary engagement signal — more reliable than email open tracking, which is inflated by Apple Mail Privacy Protection and Gmail proxy loading.

**Time required**: 10 minutes.

**Steps**:

1. Go to bitly.com. Click "Get started for free." Create an account using any email address. The free tier supports unlimited links and provides click analytics.

2. After logging in, click "Create new" in the top right, then "Link."

3. In the "Destination" field, paste the full Gist URL: `https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108`

4. In the "Custom back-half" field (the part after `bit.ly/`), type `palantir-briefing`. This creates `bit.ly/palantir-briefing`. If that back-half is taken, use `palantir-opsec-2026` or similar.

5. Click "Create." Bitly shows you the short link.

6. Test it: open a private/incognito browser window, paste `bit.ly/palantir-briefing` into the address bar, and press Enter. The Gist must load.

7. Return to the Bitly dashboard. Within 60 seconds, the click count should increment to 1. If it does not update within 2 minutes, refresh the dashboard. If clicks are not recording, the link has a configuration error — do not proceed until clicks register.

**Using the link**: Replace the full Gist URL in all 25 email templates with `bit.ly/palantir-briefing`. Every contact receives the same short URL. Do not create separate Bitly links per contact — that fragments your analytics and makes the 45% click-rate target harder to measure cleanly.

**Checking Bitly daily**: Log into bitly.com each morning during Weeks 1–3. The dashboard shows total clicks, unique clicks by day, and geographic/referrer data. Note the cumulative click count in Column I of the Contact Master List (mark Y for the contact you believe clicked, based on timing and geography). Referrer data showing a `.gov` or `.edu` domain is a positive internal-forwarding signal.

**Bitly free tier limitations**: The free tier does not show which individual contact clicked the link — only aggregate data. If you need contact-level click attribution, upgrade to Bitly Starter ($8/month) for link tags, or use UTM parameters to create per-contact links (advanced — not required for this campaign).

---

### 1.2 Gmail Label Structure

Gmail labels function as tracking tags. Creating the label structure below takes 8 minutes and enables the Zapier automations in Section 1.4 to work correctly. It also gives you an instant visual triage of where each contact is in the funnel.

**Time required**: 8 minutes.

**Steps** (Gmail desktop, not mobile):

1. In Gmail, click the gear icon (Settings) in the top right. Select "See all settings."

2. Click the "Labels" tab. Scroll down to "Create new label."

3. Create the following labels exactly as written. For nested labels (with a `/`), create the parent label first:

```
Tier1-Policy
Tier1-Policy/Sent
Tier1-Policy/Reply-Stage0-Acknowledgment
Tier1-Policy/Reply-Stage1-Question
Tier1-Policy/Reply-Stage1-MeetingRequest
Tier1-Policy/Reply-Stage1-Routing
Tier1-Policy/Reply-Declined
Tier1-Policy/OOO-Active
Tier1-Policy/Bounce-Unresolved
Tier1-Policy/Follow-Up-Pending
Tier1-Policy/Meeting-Scheduled
Tier1-Policy/Meeting-Completed
```

To create a nested label: when creating a new label, check "Nest label under" and select `Tier1-Policy`.

4. After creating all labels, return to the main Gmail view. When you send Wave 1 emails (Section from `PHASE_1_EXECUTION_CALENDAR.md`), apply the `Tier1-Policy/Sent` label to each sent email immediately after sending. This is manual — it takes 5 seconds per email.

5. As replies arrive, apply the appropriate reply-type label. The Zapier automation (Section 1.4) will also do this automatically for new replies, but applying labels manually for the first few responses helps you verify the automation is working.

---

### 1.3 Gmail Filter for Automatic Label Application

Set up a Gmail filter so that replies from the 25 contacts are automatically routed to the `Tier1-Policy` parent label. This is optional but reduces the daily maintenance burden.

**Steps**:

1. In Gmail, click the search bar at the top. Click the filter icon (a small triangle on the right side of the search bar).

2. In the "From" field, you can enter multiple email domains separated by `OR`. For example: `from:(@senate.gov OR @aclu.org OR @brookings.edu)` to auto-label all replies from senate and known think tank domains.

3. Click "Create filter." On the next screen, check "Apply the label" and select `Tier1-Policy`. Also check "Never send it to Spam" — policy contacts sending from official domain addresses are sometimes incorrectly spam-filtered.

4. Click "Create filter."

Note: This filter labels replies from entire domains, not specific contacts. If your outreach domain overlaps with other correspondence (e.g., you receive other email from senate.gov), this filter will label those too. Review applied labels daily and remove false positives.

---

### 1.4 Zapier Automation: Gmail Reply to Google Sheets Row Update

Zapier connects Gmail and Google Sheets without code. The free tier allows 5 active Zaps and 100 tasks per month — sufficient for a 25-contact campaign.

**What this automation does**: When a reply arrives in Gmail from one of the 25 tracked contacts, Zapier automatically adds a row to the Email Engagement Log tab in Google Sheets with the sender name, email address, date, and subject line. This eliminates manual logging of reply events.

**Time required**: 25 minutes for initial setup; 5 minutes per additional Zap.

**Pre-requisite**: Google Sheets tracker must already be created with the 5-tab structure from `MEASUREMENT_AUTOMATION_SETUP.md` Section 1. If you have not created the sheet yet, do that first (see Section 2 of this document).

**Steps to create the Gmail-to-Sheets Zap**:

1. Go to zapier.com. Create a free account.

2. Click "Create Zap" (or "+ New Zap" depending on your Zapier version).

3. **Trigger step — set up Gmail**:
   - Search for and select "Gmail" as the trigger app.
   - Select "New Email" as the trigger event. Click "Continue."
   - Connect your Gmail account. Zapier will ask for permission to read emails — grant it.
   - In the trigger configuration: set "Label/Mailbox" to `Tier1-Policy` (the parent label you created in Section 1.2). This means the Zap only fires when a new email lands in that label — not for every email.
   - Click "Test trigger." Zapier will look for a recent email in the Tier1-Policy label. If you have not sent any test emails yet, temporarily apply the Tier1-Policy label to any email and run the test. The test just needs to find an email to confirm the connection works.

4. **Action step — set up Google Sheets**:
   - Click the "+" to add an action. Search for "Google Sheets."
   - Select "Create Spreadsheet Row" as the action event.
   - Connect your Google account and select the spreadsheet "Phase 1 Policy Outreach Tracker — June 2026."
   - Select the worksheet "Email Engagement Log."
   - Map the fields from the Gmail trigger to the Sheet columns:
     - Column A (Broadcast ID): map to Gmail "Message ID"
     - Column B (Email Date): map to Gmail "Date" (format as YYYY-MM-DD)
     - Column C (Subject Line): map to Gmail "Subject"
     - Column D (Recipients): type `1` (each row is one email)
     - Column H (Reply Y/N): type `Y` (this Zap only fires for replies — they are always Y)
   - Leave columns E, F, G, I, J blank — those are filled by the Kit/Gmail sync script or manually.

5. Click "Test action." Zapier will create a test row in the Email Engagement Log tab. Open the sheet and confirm the row appeared with correct data.

6. Click "Publish Zap." The Zap is now live and will fire automatically for every new reply that lands in the Tier1-Policy label.

**Free tier limits**: Zapier free allows 100 tasks per month. Each time the Zap fires is one task. With 25 contacts and a maximum of 2–3 replies per contact over three weeks, you will use approximately 50–75 tasks — within the free limit.

**What this does not automate**: The Zapier free tier cannot filter by sender, so the Zap fires for any new email in the Tier1-Policy label — including out-of-office replies. After each run, scan the new rows in the Email Engagement Log and delete rows for OOO and automated responses. Marking them as logged keeps the tab clean.

---

### 1.5 Optional: Zapier Automation for Bounce Detection

Create a second Zap to log Gmail bounce notifications (which arrive as system emails from `mailer-daemon@googlemail.com`) to a dedicated range in the Email Engagement Log.

**Steps**:

1. Create a new Zap with Gmail as the trigger, "New Email" as the trigger event.
2. Set the search filter to: From = `mailer-daemon@googlemail.com`.
3. Action: Google Sheets "Create Spreadsheet Row" — log the subject and date to the Email Engagement Log.
4. Manually review these rows daily and update the Contact Master List (Column M = `Bounce`) for any contact whose email bounced.

Bounce detection matters: if two contacts bounce in Wave 1, the `TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md` threshold says to pause all sends and re-validate remaining contact emails before proceeding.

---

## Section 2: Google Sheets Dashboard — 5-Tab Template

The Google Sheet is the authoritative record for all campaign data. Everything else (Discord briefings, Zapier automations, Bitly data) flows into this sheet. Set it up before May 31.

**Time required**: 45 minutes for full setup with all formulas.

### 2.1 Create the Spreadsheet

1. Go to sheets.google.com. Click "Blank spreadsheet."
2. Name it exactly: **Phase 1 Policy Outreach Tracker — June 2026**
3. Share it with Editor access to any additional accounts that need to view or update it (e.g., a co-organizer's Gmail).

You will have 5 tabs. The default "Sheet1" becomes Tab 1. Add four more by clicking the "+" at the bottom left.

Name the tabs exactly as follows (capitalization and spacing matter for the Python sync scripts in `MEASUREMENT_AUTOMATION_SETUP.md`):

- Tab 1: `Contact Master List`
- Tab 2: `Email Engagement Log`
- Tab 3: `Meeting Schedule`
- Tab 4: `Policy Uptake Signals`
- Tab 5: `KPI Summary Dashboard`

---

### 2.2 Tab 1: Contact Master List

This is the primary tracking tab. You update it manually as events happen (sent, clicked, replied, meeting booked). The formulas at the bottom calculate campaign-wide metrics automatically.

**Column headers (Row 1)**:

| Col | Header |
|-----|--------|
| A | Contact Name |
| B | Organization |
| C | Title / Function |
| D | Email Address |
| E | Sector |
| F | Wave |
| G | Send Date |
| H | Send Time |
| I | Bitly Click Y/N |
| J | Click Date |
| K | Reply Received Y/N |
| L | Reply Date |
| M | Reply Type |
| N | Days to Reply |
| O | Follow-Up Sent Y/N |
| P | Follow-Up Date |
| Q | Meeting Scheduled Y/N |
| R | Meeting Date |
| S | Meeting Status |
| T | Next Action |
| U | Notes |

**Valid values for Column E (Sector)**: `Senate` / `Think Tank` / `Law School` / `Civil Rights`

**Valid values for Column F (Wave)**: `1` / `2` / `3`

**Valid values for Column M (Reply Type)**: `Stage0` / `Stage1-Q` / `Stage1-MR` / `Stage1-R` / `Declined` / `OOO` / `Bounce`

(Stage1-MR = Stage 1 Meeting Request; Stage1-Q = Stage 1 Question; Stage1-R = Stage 1 Routing)

**Pre-populate**: Enter all 25 contacts in Rows 2–26 before May 31. Use the send order from `PHASE_1_EXECUTION_CALENDAR.md` Section 3.

**Formula block** — paste these below Row 26 (e.g., starting at Row 29). These auto-calculate as you update the contact rows:

In a label cell (e.g., A29), type "CAMPAIGN METRICS" to separate formulas from contact data.

```
Row 30, A30: "Click Rate %"
Row 30, B30: =COUNTIF(I2:I26,"Y")/COUNTA(A2:A26)*100

Row 31, A31: "Reply Rate %"
Row 31, B31: =COUNTIF(K2:K26,"Y")/COUNTA(A2:A26)*100

Row 32, A32: "Stage 1+ Ratio %"
Row 32, B32: =IFERROR(COUNTIFS(M2:M26,"Stage1-*")/COUNTIF(K2:K26,"Y")*100, 0)

Row 33, A33: "Meeting Rate %"
Row 33, B33: =COUNTIF(Q2:Q26,"Y")/COUNTA(A2:A26)*100

Row 34, A34: "Bounce Rate %"
Row 34, B34: =COUNTIF(M2:M26,"Bounce")/COUNTA(A2:A26)*100

Row 35, A35: "Avg Days to Reply"
Row 35, B35: =IFERROR(AVERAGEIF(N2:N26,"<>"), 0)
```

**Days to Reply formula** — enter this in N2, then drag it down to N26:
```
=IF(L2="","",L2-G2)
```
Format Column N as "Number" with 0 decimal places. If a reply date and send date are entered correctly, this auto-calculates the integer days between send and reply.

**Sector-specific reply rates** — paste in a separate block below Row 36:

```
Row 38, A38: "Senate Reply Rate %"
Row 38, B38: =IFERROR(COUNTIFS(E2:E26,"Senate",K2:K26,"Y")/COUNTIF(E2:E26,"Senate")*100, 0)

Row 39, A39: "Think Tank Reply Rate %"
Row 39, B39: =IFERROR(COUNTIFS(E2:E26,"Think Tank",K2:K26,"Y")/COUNTIF(E2:E26,"Think Tank")*100, 0)

Row 40, A40: "Law School Reply Rate %"
Row 40, B40: =IFERROR(COUNTIFS(E2:E26,"Law School",K2:K26,"Y")/COUNTIF(E2:E26,"Law School")*100, 0)
```

These three formulas tell you whether a specific sector is underperforming. According to `TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md`, the escalation trigger fires if law school reply rate falls below 30% by Day 7 — these formulas surface that before it becomes a crisis.

---

### 2.3 Tab 2: Email Engagement Log

This tab is populated automatically by the Zapier Gmail-to-Sheets Zap (Section 1.4). You do not need to manually add rows here unless Zapier is not set up.

**Column headers (Row 1)**:

| Col | Header | Filled by |
|-----|--------|-----------|
| A | Message ID | Zapier (Gmail ID) |
| B | Email Date | Zapier |
| C | Subject Line | Zapier |
| D | Recipients | Zapier (always 1 for individual sends) |
| E | Open Rate % | Manual or Kit API sync |
| F | Click Rate % | Manual from Bitly |
| G | Unsubscribes | Manual |
| H | Reply Y/N | Zapier (Y when a reply triggers the Zap) |
| I | Sentiment | Manual: Positive / Neutral / Negative |
| J | Last Synced | Auto-timestamp if using Kit sync script |

**Conditional formatting — engagement heat map**:

Select Column F (Click Rate %):
1. Format > Conditional formatting
2. Choose "Color scale"
3. Min value: 0, color: red. Midpoint: 30, color: yellow. Max: 50, color: green.
4. Apply to F2:F500.

Repeat for Column E (Open Rate %).

**Weekly aggregation formulas** — paste in a summary block below Row 500 (or in a separate "Weekly Summary" section within the tab):

```
Week 1 sends (June 1–7):       =COUNTIFS(B:B,">="&DATE(2026,6,1),B:B,"<="&DATE(2026,6,7))
Week 1 avg click rate:          =AVERAGEIFS(F:F,B:B,">="&DATE(2026,6,1),B:B,"<="&DATE(2026,6,7))

Week 2 sends (June 8–14):      =COUNTIFS(B:B,">="&DATE(2026,6,8),B:B,"<="&DATE(2026,6,14))
Week 2 avg click rate:          =AVERAGEIFS(F:F,B:B,">="&DATE(2026,6,8),B:B,"<="&DATE(2026,6,14))

Week 3 (June 15–21):           =COUNTIFS(B:B,">="&DATE(2026,6,15),B:B,"<="&DATE(2026,6,21))
```

---

### 2.4 Tab 3: Meeting Schedule

Every confirmed briefing call gets a row here. Fill it within 2 hours of a contact confirming a meeting.

**Column headers (Row 1)**:

| Col | Header |
|-----|--------|
| A | Contact Name |
| B | Organization |
| C | Meeting Date |
| D | Meeting Time |
| E | Format (Phone / Video / In-Person) |
| F | Attendees |
| G | Status (Scheduled / Completed / Rescheduled / Cancelled) |
| H | Key Outcomes |
| I | Follow-Up Committed |
| J | Next Steps |
| K | Adoption Signal Y/N |
| L | Tier 2 Candidate Y/N |
| M | Commitment Type (Made / No Decision / Declined / Deferral) |
| N | Policy Ask Tracked |
| O | Policy Outcome Status (Pending / Progressed / Completed / Stalled) |

**Meeting completion rate formula** — add below data:
```
=IFERROR(COUNTIF(G:G,"Completed")/COUNTIFS(G:G,"<>",G:G,"<>Status")*100, 0)
```

**Sector-specific meeting rate** — cross-reference with the Contact Master List:
```
Senate meetings: =COUNTIFS('Contact Master List'!E:E,"Senate",'Contact Master List'!Q:Q,"Y")/COUNTIF('Contact Master List'!E:E,"Senate")*100
Think Tank meetings: =COUNTIFS('Contact Master List'!E:E,"Think Tank",'Contact Master List'!Q:Q,"Y")/COUNTIF('Contact Master List'!E:E,"Think Tank")*100
Law School meetings: =COUNTIFS('Contact Master List'!E:E,"Law School",'Contact Master List'!Q:Q,"Y")/COUNTIF('Contact Master List'!E:E,"Law School")*100
```

---

### 2.5 Tab 4: Policy Uptake Signals

This tab tracks downstream evidence that Phase 1 is affecting policy. Entries here are logged manually after meetings, after weekly web scans, or when a contact mentions sharing or citing the corpus. The `TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md` adoption target is 10% of contacted organizations (2–3 of 25) reporting a positive signal by Week 6.

**Column headers (Row 1)**:

| Col | Header |
|-----|--------|
| A | Organization |
| B | Contact Name |
| C | Signal Type |
| D | Signal Description |
| E | Date Detected |
| F | Confidence Level (High / Medium / Low) |
| G | Source |
| H | Escalation Path (None / Notify user / Accelerate Tier 2) |
| I | Follow-Up Action |

**Valid Signal Types**: `Internal Share` / `Practice Implementation` / `Referral` / `Media Mention` / `Policy Citation` / `Distribution Request`

**Weekly web scan SOP** (log results in this tab):

Every Friday during Phase 1 and for 8 weeks after, spend 15 minutes scanning for policy uptake signals. Use this checklist:

1. Google search: `"ELITE address confidence score"` — look for new hits not in your Gist.
2. Google search: `"Palantir ICE ELITE"` — look for news articles, academic papers, legal filings.
3. Google search: `"DROP platform immigration" site:.gov OR site:.edu` — new government or academic references.
4. Check each Tier 1 organization's recent publications page (think tanks and law schools post working papers and policy briefs regularly). Look for surveillance-related publications dated after June 1.
5. CourtListener (courtlistener.com): search "Palantir ICE" filtering by date (after June 1) — amicus briefs, Fourth Amendment motions.
6. If any result references the corpus or cites language from it, log it in this tab as a `Policy Citation` signal with Confidence = High and Source = URL.

**Google Alerts setup** (one-time, takes 5 minutes):

1. Go to google.com/alerts.
2. Create alerts for each of these queries:
   - `"ELITE address confidence score"`
   - `"Palantir ICE ELITE"`
   - `"DROP platform immigration"`
3. Set delivery to: "As-it-happens," to your Gmail, all results.
4. Any alert that mentions a Tier 1 organization should be logged in this tab as a Policy Citation signal.

---

### 2.6 Tab 5: KPI Summary Dashboard

This is the single-pane view. It auto-calculates from the other tabs. The Discord bot reads this tab daily to generate the 20:05 UTC briefing.

**Layout** (Row 1 = header row: Metric | Week 1 | Week 2 | Week 3 | Final):

| Row | Col A (Metric) | Col B | Col C | Col D | Col E |
|-----|---------------|-------|-------|-------|-------|
| 1 | Metric | Week 1 | Week 2 | Week 3 | Final |
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

**Auto-calculating formulas for Column B (Week 1)** — paste these, then adjust date ranges for Columns C and D:

Row 4 (Click Rate %):
```
='Contact Master List'!B30
```
(This pulls directly from the formula block at the bottom of Tab 1.)

Row 6 (Reply Rate %):
```
='Contact Master List'!B31
```

Row 8 (Stage 1+ Ratio %):
```
='Contact Master List'!B32
```

Row 12 (Meeting Rate %):
```
='Contact Master List'!B33
```

Row 14 (Bounce Rate %):
```
='Contact Master List'!B34
```

Row 13 (Adoption signals logged):
```
=COUNTA('Policy Uptake Signals'!A2:A500)-1
```

Row 9 (Meetings scheduled):
```
=COUNTIF('Meeting Schedule'!G:G,"Scheduled")+COUNTIF('Meeting Schedule'!G:G,"Completed")
```

Row 10 (Meetings completed):
```
=COUNTIF('Meeting Schedule'!G:G,"Completed")
```

**Status column (Column G)** — enter these IF formulas in the status column to the right of the Final column. They return RED / YELLOW / GREEN based on the value in Column E (Final):

```
Row 4:  =IF(E4>=45,"GREEN",IF(E4>=30,"YELLOW","RED"))
Row 6:  =IF(E6>=20,"GREEN",IF(E6>=10,"YELLOW","RED"))
Row 8:  =IF(E8>=60,"GREEN",IF(E8>=40,"YELLOW","RED"))
Row 12: =IF(E12>=60,"GREEN",IF(E12>=30,"YELLOW","RED"))
Row 14: =IF(E14<5,"GREEN",IF(E14<=8,"YELLOW","RED"))
```

**Conditional formatting for Column G**:
1. Select G4:G14.
2. Format > Conditional formatting > Custom formula.
3. Rule 1: `=G4="GREEN"` → background color `#B7E1CD` (light green).
4. Rule 2: `=G4="YELLOW"` → background color `#FCE8B2` (light yellow).
5. Rule 3: `=G4="RED"` → background color `#F4C7C3` (light red).

**Sparklines** — add these to Column F to show the trend across weeks:
```
Row 4:  =SPARKLINE(B4:E4,{"charttype","line";"color","#4472C4";"linewidth",2})
Row 6:  =SPARKLINE(B6:E6,{"charttype","line";"color","#4472C4";"linewidth",2})
Row 12: =SPARKLINE(B12:E12,{"charttype","line";"color","#4472C4";"linewidth",2})
Row 14: =SPARKLINE(B14:E14,{"charttype","line";"color","#E06666";"linewidth",2})
```

**Auto-alert formula for sector lagging** — add this below the main table (e.g., Row 20):
```
=IF('Contact Master List'!B38<30,"ALERT: Senate reply rate below 30% — review contact routing","Senate OK")
=IF('Contact Master List'!B39<30,"ALERT: Think Tank reply rate below 30% — check follow-up timing","Think Tank OK")
=IF('Contact Master List'!B40<30,"ALERT: Law School reply rate below 30% — try phone follow-up","Law School OK")
```

Apply red background conditional formatting to any cell in this block that contains "ALERT:".

---

## Section 3: Discord Webhook Daily Briefing

The Discord webhook sends one automated message per day at 20:05 UTC (12:05 PM Pacific / 3:05 PM Eastern). It reads the KPI Summary Dashboard tab and reports current status, trend direction, and any anomaly triggers. You do not need to check the spreadsheet every day — the Discord briefing will flag problems.

### 3.1 Create the Discord Webhook

**Time required**: 5 minutes.

**Steps**:

1. Open Discord on desktop (the web app or installed app — not mobile).

2. Go to the server where you want briefings delivered. Right-click the channel you want to use (e.g., `#phase1-monitoring` — create this channel if it does not exist).

3. Click "Edit Channel" (gear icon).

4. In the left sidebar, click "Integrations."

5. Click "Webhooks," then "New Webhook."

6. Name it "Phase 1 Briefing Bot." Leave the channel selection as-is.

7. Click "Copy Webhook URL." This URL is a long string starting with `https://discord.com/api/webhooks/`. Save it somewhere secure — you will need it in Step 3.2.

8. Click "Save Changes."

**Test the webhook immediately**:

Open a terminal (on any computer — this is just a one-time test):
```bash
curl -X POST -H 'Content-Type: application/json' \
  -d '{"content":"Webhook test — Phase 1 monitoring online"}' \
  YOUR_WEBHOOK_URL
```

Replace `YOUR_WEBHOOK_URL` with the URL you copied. The expected response is HTTP 204 No Content (blank response). Within 5 seconds, the message "Webhook test — Phase 1 monitoring online" should appear in the Discord channel.

If you do not have terminal access, use an online curl tool such as reqbin.com — paste the webhook URL and the JSON body and send a POST request.

---

### 3.2 Discord Automation Options

There are two ways to send daily Discord briefings. Choose based on whether the Pi cron job system is set up.

**Option A: Pi cron job (recommended if Pi is available)**

The `scripts/discord_daily_briefing.py` script in `projects/cybersecurity-hardening/scripts/` handles this automatically. Set up as described in `MEASUREMENT_AUTOMATION_SETUP.md` Section 2.6. The script reads the KPI Summary Dashboard tab from Google Sheets and posts a formatted briefing at 20:05 UTC.

**Option B: Zapier webhook Zap (no Pi required)**

Create a Zapier "Schedule" Zap that fires daily and sends a simplified status message to Discord.

1. In Zapier, create a new Zap.
2. Trigger: "Schedule by Zapier" → "Every Day" → set time to 20:00 UTC.
3. Action: "Webhooks by Zapier" → "POST."
4. URL: your Discord webhook URL.
5. Payload type: JSON.
6. Data: `{"content": "Phase 1 daily check-in — open Google Sheets KPI tab and review."}`

This Option B version does not pull live data — it is just a reminder. The full automated version requires the Pi script or a more complex Zapier setup (Multi-Step Zaps require the paid tier). For live data in Discord without the Pi, use Option B as a reminder trigger and manually check the sheet. If the Pi is available, use Option A.

---

### 3.3 What the Daily Briefing Reports

The daily Discord message (from the Pi script) includes:

- Campaign Day number and week number
- Overall status: GREEN (all KPIs on track) / YELLOW (warning band) / RED (escalation required)
- Six KPI snapshots with current value, target, trend arrow (up/down/stable)
- Active anomaly alerts (only shown if a threshold is crossed)
- Actionable next step for YELLOW or RED status

**Anomaly triggers that fire an alert**:

| Trigger condition | Alert text |
|-------------------|-----------|
| Reply rate below 15% | Check contact routing — named individual vs. general inbox |
| Adoption rate below 5% at Week 4+ | Week-4 follow-up emails needed |
| Zero meetings scheduled at Week 2+ | Replace vague CTAs with specific 20-min offer + Calendly link |
| Zero policy signals logged at Week 3+ | Ensure post-meeting notes are being captured in Tab 4 |
| Bounce rate at or above 5% | Stop wave sends — re-validate remaining contact emails |

**If no Discord message arrives by 20:15 UTC**: Check the log file at `/tmp/discord_briefing.log` on the Pi. Common causes: webhook URL changed (regenerate and update the env file), Pi network down, or Google Sheets API credentials expired. See `MEASUREMENT_AUTOMATION_SETUP.md` Section 9 for the full contingency decision tree.

---

## Section 4: Meeting Scheduler Integration

When a contact sends a Stage 1 Meeting Request reply, you need to confirm a time within 24 hours. Friction in the scheduling process costs confirmed calls. This section sets up a friction-free scheduling flow.

### 4.1 Calendly Free Tier Setup

Calendly's free tier allows one event type and handles the full scheduling flow: the contact picks a time from your availability, the meeting is added to both calendars, and both parties receive a confirmation email. You share a single link in every follow-up email.

**Time required**: 15 minutes.

**Steps**:

1. Go to calendly.com. Click "Get started for free." Create an account and connect your Google Calendar.

2. Calendly will ask you to create your first "event type." Create two (the free tier allows one — if you need two, use one and mention the duration flexibility in your email text):

   - **20-minute Briefing Call**: Title = "Palantir/ICE Threat Model Briefing — 20 min." Description = "A focused 20-minute briefing on primary-source documentation of ICE's Palantir ELITE targeting system and recommended OpSec countermeasures." Duration = 20 minutes.
   - **30-minute Briefing Call**: Duplicate the above with 30 minutes. For the free tier, use one event type and note in the email that you can do 20 or 30 minutes.

3. Set your availability: select the hours when you can take calls. Avoid Friday afternoons and Monday mornings for senate offices (legislative staff are typically in briefings or constituent meetings at those times).

4. Set a buffer: in the event settings, add a 10-minute "buffer" after each event so calls do not stack. This also gives you time to add notes to the Meeting Schedule tab immediately after each call.

5. Go to your Calendly dashboard and copy your scheduling link. It looks like `calendly.com/your-username/briefing-call`. Save this link — you will include it in all Stage 1 follow-up emails.

**Using the link**: After a contact sends a Stage 1+ reply, your follow-up email should include:

> "I have 20-minute slots available this week and next — you can pick a time directly here: calendly.com/your-username/briefing-call. If none of those times work, reply with two or three options and I will confirm one."

Offering the Calendly link reduces back-and-forth by eliminating the "when are you free" negotiation. According to `TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md`, scheduling friction is a known cause of low meeting-completion rates — contacts who agree to a meeting in principle but never lock a time are a conversion problem, not a reply problem.

### 4.2 When Calendly Confirms a Meeting

After a contact books through Calendly, two things happen automatically: both calendars receive the event, and both parties receive a confirmation email. Your manual step is:

1. Within 2 hours of the Calendly confirmation email arriving, add a row to the Meeting Schedule tab (Tab 3) with Status = `Scheduled`.
2. Update the Contact Master List (Tab 1) for that contact: Column Q = `Y`, Column R = meeting date.
3. Prepare a 2-3 sentence recap of the most relevant section of the corpus for this contact's sector — have it ready before the call.

### 4.3 Alternative: Google Form + Manual Calendar

If Calendly is not preferred, use this lower-friction alternative:

1. Create a Google Form with two questions: "What time zone are you in?" and "Select three available time slots [dropdown: Morning / Afternoon, Monday through Friday]."
2. Share the Google Form link in follow-up emails in place of the Calendly link.
3. When a form response arrives, Zapier can notify you via Discord using a simple "Google Forms → Discord Webhook" Zap (search for this template in Zapier's template library — it is pre-built and takes 10 minutes to set up).
4. After receiving the form response, manually create the Google Calendar event and send a confirmation email.

The Google Form approach requires more manual steps but has no account requirements.

---

## Section 5: Policy Uptake Tracking SOP

Policy uptake is a lagging indicator — it takes 4–12 weeks for a briefing to surface as a policy citation, legislative reference, or operational change. This section documents the manual weekly scan procedure that tracks early signals.

### 5.1 Scan Schedule

| Scan type | Frequency | Time required |
|-----------|-----------|---------------|
| Google Alerts review | Daily (automated to Gmail) | 2 minutes |
| Org website publication scans | Weekly, every Friday | 15 minutes |
| CourtListener search | Monthly | 10 minutes |
| Overton.io policy doc search | Quarterly | 20 minutes |
| Contact follow-up email check | Weekly, after Week 4 | 5 minutes |

### 5.2 Weekly Friday Scan Procedure (15 minutes)

Do this every Friday from June 1 through August 1.

**Step 1 — Google Alerts inbox** (2 min): Check Gmail for any Google Alerts that arrived since last Friday. Open any alerts containing the monitored keywords. If any alert links to a new document that references the corpus or cites Palantir ELITE, log it in Tab 4 (Policy Uptake Signals) as a `Policy Citation` signal.

**Step 2 — Tier 1 org publication pages** (8 min): Visit the "Publications," "Reports," or "Working Papers" page of five Tier 1 organizations per week (rotate through the 25-contact list over 5 weeks). Scan any publications dated after June 1. If a publication discusses surveillance, ICE data practices, digital rights, or Fourth Amendment technology — and the organization is in your contact list — log it as a potential `Policy Citation` with Confidence = Medium. Contact the author to confirm if the connection to the corpus is plausible.

Organizations to prioritize (check every week): Brennan Center for Justice, Cato Institute, EFF, ACLU, and whichever think tanks have had the most substantive replies.

**Step 3 — CourtListener** (monthly, 5 min): Go to courtlistener.com. Search "Palantir ICE" with a date filter set to after June 1. Any new legal filing that cites ELITE or DROP is a `Policy Citation` signal with Confidence = High.

**Step 4 — Weekly summary log**: After each Friday scan, add a row to Tab 4 with Signal Type = `Internal Share` or leave blank if nothing new. Even a "nothing new this week" log entry is useful — it confirms the scan happened and the silence is documented, not forgotten.

### 5.3 Keyword List for Scans

Use these exact strings in Google searches and document searches to identify corpus-adjacent signals:

```
"ELITE address confidence score"
"Palantir ICE ELITE"
"Palantir ICE DROP"
"DROP platform immigration"
"address confidence score ICE"
"Palantir CODIS immigration"
"ICE data broker targeting"
"immigration surveillance targeting algorithm"
```

Broaden these searches quarterly. As media coverage of Palantir's ICE programs increases, new terminology will emerge — add it to the list.

### 5.4 Logging Signals in Tab 4

For every signal logged in Tab 4, complete all columns:

- **Confidence Level**: High = direct citation or explicit statement from the contact; Medium = publication on an adjacent topic from a contacted organization; Low = keyword match without organizational connection.
- **Escalation Path**: If Confidence is High and Signal Type is `Policy Citation`, set Escalation Path = `Accelerate Tier 2`. This signal means a Tier 1 contact has produced verifiable uptake — that organization is a strong Tier 2 candidate.
- **Follow-Up Action**: For High-confidence signals, send a congratulatory note to the contact within 48 hours acknowledging the publication or filing. This reinforces the relationship and creates an opportunity to offer additional materials or introduce the Tier 2 playbooks.

---

## Section 6: Contingency Automation — Pre-Staged Escalation Triggers

These triggers are defined in advance so that when a failure signal appears, the correct response is already decided and staged. Do not improvise under pressure during the campaign.

The thresholds below are drawn from `TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md` Sections 3 and 4, with specific automation steps added here.

---

### Contingency 1: Reply Rate Below 20% by Day 10

**Trigger condition**: KPI Summary Dashboard Row 6 (Reply rate %) shows a value below 20 at any point during Days 6–10.

**What the Discord bot does**: Posts an anomaly alert with text "Reply rate below 15% — check contact routing."

**What you do**:

1. Open the Contact Master List and filter Column M (Reply Type) for blanks — these are non-responding contacts.
2. For each non-responding contact, verify Column D (Email Address) against the organization's current website staff directory. Legislative staff turn over rapidly; if the contact has left, find their replacement.
3. Review the Gmail Sent folder for the non-responding contacts. Confirm the email was delivered (no bounce in Column M).
4. On Day 11, send a subject-line variation to the five non-responding contacts with the highest sector priority (senate offices first). Change the subject line — do not repeat the same framing.

**Pre-staged follow-up subject lines** (test one per sector):
- Senate: `Re: Palantir's ELITE — primary-source documentation for oversight staff`
- Think Tank: `Thought you'd want to see this: primary-source ICE targeting data`
- Law School: `Fourth Amendment implications — ICE data access documentation`

**If reply rate is still below 10% by Day 14**: The email channel is failing. Escalate top 5 priority contacts to LinkedIn outreach (for think tanks and law school faculty) or phone outreach (for senate offices — call the main line, ask for the legislative assistant handling civil liberties or surveillance policy).

---

### Contingency 2: Click Rate Below 30% by Day 7

**Trigger condition**: The Bitly dashboard shows fewer than 7–8 unique clicks from the 25 sends after the first full wave completes (Day 5–7).

**What the Discord bot does**: Flags Click Rate % as RED (below the 30% warning threshold).

**What you do**:

1. Send a test email from your outreach address to a personal Gmail account and a personal non-Gmail account (e.g., Outlook, Yahoo). Does it arrive? Does it land in spam?

2. Check mail-tester.com: send a test email to the address shown on that page. The score should be ≥8/10. If it is below 8, the domain has a deliverability problem. Common causes: missing SPF record, no DKIM setup, or sending from a new Gmail account with no send history.

3. If deliverability checks out: the subject line is the problem. For Week 2 sends (Days 8–10), use a different subject line variant. Test two variants — send half the Week 2 contacts one subject line and half another. Compare click rates after 3 days.

4. If clicks remain below 20% on both variants: the corpus link itself may be triggering spam filters (gist.github.com URLs are sometimes blocked by organizational email gateways). Create an alternative landing page — a simple Google Doc or a Notion page with the same content — and use that URL in Week 3 sends.

---

### Contingency 3: Meeting Acceptance Below 30% by Day 21

**Trigger condition**: KPI Summary Dashboard Row 12 (Meeting rate %) shows a value below 30 after all three waves of sends are complete.

**What the Discord bot does**: Posts anomaly alert "Zero briefing calls scheduled at Week 2+" (or equivalent after meeting count is available).

**What you do**:

1. Audit the call-to-action in all sent emails. Did every follow-up offer a specific time, a specific duration, and the Calendly link? If any follow-up said "happy to discuss further" without a specific ask, those contacts have not received a proper CTA.

2. Send a re-engagement email to all contacts who replied Stage 1+ but have not scheduled a call. The email should contain:
   - One sentence stating the specific value to their work ("Given your office's oversight work on surveillance technology, I think 20 minutes on the ELITE documentation would be directly relevant")
   - The Calendly link
   - An alternative: "If you prefer, reply with a preferred date and I will send a calendar invite directly"

3. For contacts who replied Stage 0 (generic acknowledgment), send a follow-up that upgrades the ask — attach a 1-page executive summary as a PDF (the `publication-prep.md` document from the corpus) and ask if the summary is useful for their work.

**Pre-staged 1-on-1 video offer**: If meeting acceptance remains below 30% after re-engagement, offer video calls as a named alternative. Some contacts prefer video to phone (especially law school faculty and think tank fellows who are accustomed to Zoom academic seminars). Add to the follow-up: "Happy to do a Zoom call if that's easier — I can share a screen with the primary-source documentation during the call."

---

### Contingency 4: Law School Sector Reply Rate Below 30% by Day 7

**Trigger condition**: The auto-alert formula in Tab 5 shows "ALERT: Law School reply rate below 30%."

**What this means**: Law school clinical faculty and supervising attorneys have the slowest reply velocity of the three sectors (typical response window is 48–96 hours versus 72 hours for senate staff). Day 7 is early to escalate, but if law schools are silent by end of Week 1, a structural problem is more likely than timing.

**What you do**:

1. Review which law school contacts were sent Wave 1 vs. Wave 2 emails. According to `PHASE_1_EXECUTION_CALENDAR.md`, law schools receive sends on Days 5 and 8 — by Day 7, only the first law school batch has been contacted.

2. Verify that sends went to clinic directors or supervising attorneys, not to the dean's office, general info@ addresses, or communications departments.

3. If sends went to the correct function and there are still no replies by Day 10: try a phone call to the law school's clinic office main line. Introduce yourself and ask whether the contact received an email about surveillance law documentation. This confirms deliverability and adds a personal touchpoint.

4. If phone follow-up produces no response: LinkedIn outreach to the named contact is acceptable for law school faculty (most are on LinkedIn and check it regularly).

---

### Contingency 5: Zero Adoption Signals by Week 6

**Trigger condition**: Tab 4 (Policy Uptake Signals) has zero rows with Confidence = High or Medium at the end of Week 6.

**What this means**: Briefing calls occurred but did not produce observable downstream action. This is the most serious failure scenario because it calls into question whether the Phase 1 cohort is the right target population, not just whether the message is right.

**What you do**:

Per `TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md` Scenario 4: send the Week 6 follow-up email (the three-question email in the framework's Section 2C) to all contacts who completed a briefing call. Wait 7 days for responses.

If responses come in but report no adoption, assess whether the barrier is:
- **Institutional**: The contact wants to act but their organization's bureaucracy is blocking it (common for senate offices — a legislative assistant may need supervisor approval to circulate external materials). Offer to brief the supervisor directly.
- **Timing**: The contact needs to wait for a specific trigger (a legislative hearing, a court date, a funding cycle). Ask when the relevant timing opens and set a reminder.
- **Relevance gap**: The threat model did not connect to their active work. Ask what specific aspect of surveillance policy or digital rights they are focused on in the next 90 days and identify whether a different section of the corpus is more directly relevant.

If zero responses come to the Week 6 follow-up: Phase 1 has not produced adoption signals. Proceed to Tier 2 on schedule but treat Phase 1 as a relationship-building exercise rather than an adoption exercise. The contacts are warm; a Tier 2 sector-specific playbook may convert better than the general corpus.

---

## Section 7: Day-1 Checklist — May 31 Evening (4 Hours Pre-Launch)

Complete these steps the evening of May 31, before the June 1 morning send window.

### 7.1 System Verification Sequence (estimated 90 minutes total)

**Step 1 — Google Sheets** (20 min):
- [ ] Open the spreadsheet. Confirm all 5 tabs exist with exact names.
- [ ] Confirm 25 contacts in Rows 2–26 of the Contact Master List.
- [ ] Confirm Column D has no blank email addresses.
- [ ] Confirm formula row (Row 30) shows 0% for click rate and reply rate — not #REF! or #DIV/0!.
- [ ] Confirm KPI Summary tab formulas show 0 — not errors.
- [ ] Confirm sparklines render as flat lines (no data yet — correct).
- [ ] Confirm status column in KPI Summary shows "RED" for all metrics (0% is below all thresholds — correct before any sends).

**Step 2 — Bitly** (5 min):
- [ ] Open `bit.ly/palantir-briefing` in a private browser window. Corpus Gist must load.
- [ ] Log into the Bitly dashboard. Click count must increment for the private-window visit.
- [ ] Reset your awareness of the current click count so you can track net new clicks from Day 1.

**Step 3 — Gmail labels** (5 min):
- [ ] Open Gmail Settings → Labels. Confirm all 12 Tier1-Policy labels exist.
- [ ] Send a test email to yourself. Apply the `Tier1-Policy/Sent` label. Confirm the label appears on the message.

**Step 4 — Zapier Zap test** (15 min):
- [ ] Log into zapier.com. Confirm the Gmail-to-Sheets Zap is "On" (green toggle).
- [ ] Send a test email to your outreach address from a personal address, with the Tier1-Policy label applied. Within 2 minutes, a row should appear in the Email Engagement Log tab.
- [ ] If no row appears: check the Zap's task history in Zapier. If the Zap fired but the row did not appear in Sheets, the spreadsheet ID or tab name is wrong. Fix before proceeding.

**Step 5 — Discord webhook** (10 min):
- [ ] Run the webhook test command from Section 3.1. Message must appear in Discord within 5 seconds.
- [ ] If the Pi cron job is set up: run `source config/measurement_env.sh && python3 scripts/discord_daily_briefing.py` and confirm a briefing message appears in Discord with zeros for all metrics.
- [ ] Confirm the Pi system clock is UTC (`date -u` on the Pi). Cron schedule expects UTC.

**Step 6 — Calendly** (5 min):
- [ ] Open your Calendly scheduling link in a private browser window. Confirm the booking flow works end-to-end (pick a time, fill in name and email, confirm).
- [ ] Confirm the booked meeting appears in your Google Calendar.
- [ ] Cancel the test booking.

**Step 7 — Kit/email platform test** (20 min):
- [ ] If using Kit (ConvertKit): send a test broadcast to two personal addresses (one Gmail, one non-Gmail). Confirm delivery in the inbox (not spam). Confirm the Bitly link in the email works. Confirm the Kit broadcast appears in `scripts/kit_email_sync.py` output after running the script manually.
- [ ] If sending directly from Gmail: confirm the first five Wave 1 drafts are staged and ready, each with the personalized opener, the corpus link (`bit.ly/palantir-briefing`), and the Calendly link in the follow-up CTA.

**Step 8 — Final contact list review** (10 min):
- [ ] Open the Contact Master List. Confirm the five Wave 1 contacts (Rows 2–6) are senate staff with verified email addresses. These are the Day 1 sends.
- [ ] Cross-check each Wave 1 contact email against the organization's current website staff directory or LinkedIn. Confirm each contact is still in the same role.
- [ ] If any contact has left the organization: do not send to the old address. Identify the replacement and update the row before tomorrow morning.

---

### 7.2 June 1 Morning Sequence (30 minutes, 7:00–7:30 AM)

1. Open Google Sheets. Confirm Tab 1 is still showing 25 rows and no errors.
2. Open Bitly dashboard. Note current click count as "Day 0 baseline."
3. Open Discord. Confirm the channel is accessible and the previous evening's test message is visible.
4. Open Gmail. Confirm Wave 1 drafts are ready.
5. Run the Pi sync script one final time: `source config/measurement_env.sh && python3 scripts/kit_email_sync.py`. Confirm no errors.
6. At 8:30 AM (or your preferred send window), send Wave 1 emails. Apply the `Tier1-Policy/Sent` Gmail label to each sent email within 5 minutes of sending.
7. After sending, update Column G (Send Date) and Column H (Send Time) in the Contact Master List for each contacted row.
8. Phase 1 is live. The measurement system will report its first real data at 20:05 UTC tonight.

---

## Cross-References and Authority

This document establishes the no-code automation layer. For deeper technical detail on any component:

- **KPI definitions, targets, and escalation thresholds**: `TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md` (Item 17) — canonical source for all metric definitions.
- **Contact list and send schedule**: `PHASE_1_EXECUTION_CALENDAR.md` (Item 29) — canonical source for the 25 contacts and 3-week timeline.
- **Python scripts and cron job setup**: `MEASUREMENT_AUTOMATION_SETUP.md` (Item 38) — technical version with Kit API integration, Google Sheets service account, and Pi cron scheduling.
- **Gmail and domain deliverability**: `TIER1_EXECUTION_RUNBOOK.md` — spam filter avoidance, subject line testing, and send-rate pacing.

When this document and the technical setup document differ on a procedure, the technical setup document takes precedence for Pi-based operations. This document takes precedence for no-code Zapier/Calendly operations.

---

*Phase 1 Measurement Automation (No-Code Guide) | Created 2026-05-13 | Item 38*
*Arm by May 31 evening | Live June 1 at 20:05 UTC first Discord briefing*
*Depends on: Item 17 (KPIs), Item 29 (calendar), MEASUREMENT_AUTOMATION_SETUP.md (technical scripts)*
