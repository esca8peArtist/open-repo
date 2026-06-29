---
title: "Week 1-2 Email Open/Click Monitoring Dashboard — Google Sheets Template"
date: 2026-06-29
version: 1.0
status: production-ready
scope: "June 29 – July 4, 2026 (Women's Health launch week). Paste-ready Google Sheets grid."
cross-references:
  - WEEK_1_2_EMAIL_OPEN_CLICK_MONITORING_AND_ALERT_THRESHOLDS.md (threshold definitions)
  - WEEK_1_2_EMAIL_SEND_VERIFICATION_TEMPLATE.md (pre-send verification)
  - SEEDWARDEN_Q3_DAILY_EMAIL_MONITORING_CHECKLIST.md (full procedure reference)
  - PHASE_3_EXECUTION_LOG.md (metric recording)
---

# Week 1-2 Email Open/Click Monitoring Dashboard
## Google Sheets Template — Jun 29 to Jul 4, 2026

**Purpose**: Daily paste-in grid for Kit.com analytics during Women's Health bundle launch week (Email 1, sent Jun 29). Six rows map each day Jun 29–Jul 4. Pull numbers from Kit.com > Campaigns > Women's Health Launch > Analytics. Flag exceptions by changing cell color (RED for RED status, YELLOW for YELLOW status).

**Baselines used**:
- Open rate baseline: 22% (Q2 2026 construction-audience benchmark)
- Click rate baseline: 2% (conservative floor; Q2 benchmark was 3–5%)
- Threshold logic below accounts for launch-day boost and post-launch decline pattern

---

## DASHBOARD GRID

### Tab: "Week 1 — Women's Health Email 1"

Copy these 8 columns into Google Sheets row 1 as headers, then fill rows 2–7 daily.

| **Date** | **Sends** | **Opens** | **Open Rate %** | **Threshold Status** | **Clicks** | **Click Rate %** | **Alert** |
|----------|-----------|-----------|-----------------|----------------------|------------|------------------|-----------|
| Jun 29 (Launch) | [Kit sends count] | [Kit opens count] | =Opens/Sends×100 | GREEN/YELLOW/RED | [Kit clicks count] | =Clicks/Sends×100 | [See logic below] |
| Jun 30 | [Running opens from Jun 29 email] | [Cumulative if open window still active] | [48-hr running rate] | GREEN/YELLOW/RED | [Running clicks] | [Running %] | |
| Jul 1 | [Opens: 72-hr cumulative from Jun 29 send] | — | [72-hr final rate] | GREEN/YELLOW/RED | [Clicks: 72-hr] | [72-hr %] | FINAL BASELINE |
| Jul 2 | [Non-send day — churn only] | N/A | N/A | [Unsub rate check] | N/A | N/A | [if unsubs >0.5%: RED] |
| Jul 3 | [Non-send day — churn only] | N/A | N/A | [Unsub rate check] | N/A | N/A | |
| Jul 4 | [Non-send day — churn only] | N/A | N/A | [Unsub rate check] | N/A | N/A | |

**Column definitions**:

- **Date**: Calendar date (ET timezone). Jun 29 is send day. Jun 30–Jul 1 are active tracking (opens arrive up to 72 hours post-send). Jul 2–4 are non-send monitoring days (unsubscribe watch only).
- **Sends**: Kit.com total sent count for Women's Health Email 1. Pull from Campaigns > Women's Health Launch > Sent. This number does not change after send.
- **Opens**: Cumulative unique opens from Kit.com > Campaigns > Women's Health Launch > Analytics > Opens. Refresh daily. This number grows through the 72-hour open window.
- **Open Rate %**: Formula: `=Opens/Sends×100`. Round to 1 decimal. Do not use Kit's displayed percentage — calculate from raw counts to avoid rounding drift.
- **Threshold Status**: GREEN / YELLOW / RED. Apply logic from column below.
- **Clicks**: Cumulative unique clicks (CTA button only) from Kit.com > Campaigns > Analytics > Clicks.
- **Click Rate %**: Formula: `=Clicks/Sends×100`. Round to 1 decimal.
- **Alert**: Free-text field. Enter action taken or "None." Examples: "None — GREEN", "YELLOW — sent test email to check rendering", "RED — reviewed messaging at 14:00 UTC".

---

## THRESHOLD LOGIC

### Open Rate Thresholds (Column E)

Apply these rules to populate "Threshold Status" each day:

```
IF Open Rate % > 22%:
  → Status = GREEN
  → Alert = "None"
  → No action required

IF Open Rate % is 20–22%:
  → Status = YELLOW
  → Alert = "Monitor — check T+48hr final before acting"
  → No immediate action; log and watch

IF Open Rate % < 20%:
  → Status = YELLOW (soft trigger)
  → Alert = "YELLOW — send check: confirm subject line rendering + spam filter test"
  → Run spam placement test (Gmail + Outlook + Apple Mail)

IF Open Rate % < 15% (at T+24hr):
  → Status = RED
  → Alert = "RED — review messaging and subject line. Consider subject line A/B for Email 2 (Jul 6)"
  → Within 2 hours: log in PHASE_3_EXECUTION_LOG.md, activate WEEK_1_2_EMAIL_OPEN_CLICK_MONITORING_AND_ALERT_THRESHOLDS.md Tier 2 response
```

**Notes on timing**:
- Jun 29 (T+0): First pull at 14:00 UTC (T+1hr). Early data only — do not set status until T+24hr read.
- Jun 30 (T+24hr): First meaningful status read. Set GREEN/YELLOW/RED based on this row.
- Jul 1 (T+48–72hr): Final baseline. This number becomes the Email 1 benchmark used to calibrate Email 2 (Jul 6) expectations.

### Click Rate Thresholds (Column G)

```
IF Click Rate % > 2%:
  → Status = GREEN

IF Click Rate % is 1–2%:
  → Status = YELLOW
  → Alert = "YELLOW clicks — check CTA placement in email preview"

IF Click Rate % < 1% AND Open Rate > 20%:
  → Status = RED (click-specific issue — opens fine, CTA not converting)
  → Alert = "RED clicks — review CTA button text and placement for Email 2"
  → Action: Revise Email 2 (Jul 6) CTA from current text to stronger verb form

IF Click Rate % < 1% AND Open Rate < 15%:
  → Status = RED (both metrics — content or audience issue)
  → Alert = "RED — both open and click RED. Review Email 2 subject line, sender, and content."
```

### Non-Send Day Alert (Jul 2–4, Column H)

On non-send days, only unsubscribe rate matters:

```
Pull: Kit.com > Subscribers > Unsubscribes > filter "last 24 hours"
Calculate: Daily Unsub % = (Daily unsubscribes / Current subscriber count) × 100

IF Daily Unsub % < 0.3%:
  → Alert = "GREEN — churn normal"

IF Daily Unsub % is 0.3–0.5%:
  → Alert = "YELLOW — churn elevated; review last email for friction"

IF Daily Unsub % > 0.5%:
  → Alert = "RED — churn spike. Investigate: check Kit unsubscribe reasons, spam complaints, and last email content"
  → Log immediately in PHASE_3_EXECUTION_LOG.md
  → Cross-reference SEEDWARDEN_Q3_DAILY_SUBSCRIBER_CHURN_MONITORING.md for response procedure
```

---

## DAILY DATA PULL INSTRUCTIONS

### How to Pull Numbers from Kit.com

**Step 1**: Log into Kit.com.

**Step 2**: Navigate to Broadcasts > Women's Health Launch (or the exact campaign name used for Jun 29 send).

**Step 3**: Click "Analytics" tab on the campaign.

**Step 4**: Record:
- Sent: Total emails sent (fixed number, confirm it matches expected subscriber count ± 2%)
- Opens: Unique opens (not total opens — unique removes duplicate opens from same person)
- Clicks: Unique clicks on primary CTA

**Step 5**: Paste into dashboard grid. Calculate rates using formulas in column notes.

**Step 6**: Set status and write alert note.

**Step 7**: Log summary line in PHASE_3_EXECUTION_LOG.md using this template:

```
[DATE] [UTC TIME] — Email 1 Women's Health [T+Xhr check]
Sent: ___ | Opens: ___ (___%) | Clicks: ___ (___%) | Unsubs today: ___ (___%)
Status: [GREEN/YELLOW/RED] | Action: [None / Action taken]
```

---

## SUMMARY GATE — JUL 1 (T+72HR FINAL BASELINE)

After the Jul 1 row is filled (Email 1 final baseline), complete this summary to inform Email 2 (Jul 6) setup:

| Metric | Email 1 Final | Target | Gap | Email 2 Adjustment |
|--------|--------------|--------|-----|-------------------|
| Open Rate % | [FILL] | >22% | [FILL] | [None / A/B subject / Revised subject] |
| Click Rate % | [FILL] | >2% | [FILL] | [None / Revised CTA text / CTA repositioned] |
| Unsubscribes Jul 29-Jul 1 | [FILL] | <0.5%/day avg | [FILL] | [None / Gap before Email 2] |
| Final status | [GREEN/YELLOW/RED] | GREEN | — | [See adjustment column] |

**Decision rule for Email 2 (Jul 6)**:
- Email 1 GREEN (>22% opens, >2% clicks): Send Email 2 with same subject format, no changes.
- Email 1 YELLOW (20–22% opens OR 1–2% clicks): Run A/B subject test on Email 2; maintain CTA position.
- Email 1 RED (<20% opens OR <1% clicks): Revise subject line completely for Email 2; revise CTA button text; increase email gap by 1 day if unsub rate was >0.5%.

---

## EMAIL 2 PRE-STAGE (JUL 6 SEND)

Set up Email 2 in Kit.com before Jun 30 EOD. Do not wait until Jul 6.

Pre-staging checklist:
- [ ] Kit.com draft created: "Respiratory Health Launch — Jul 6"
- [ ] Subject line loaded (default or revised based on Email 1 status)
- [ ] Preview text loaded (distinct from subject line, 40–50 characters)
- [ ] Etsy Respiratory bundle URL confirmed (not Women's Health URL — copy-paste error risk)
- [ ] CTA button text matches strategy (revised or same based on Email 1 click status)
- [ ] Send time: 9:00 AM ET (13:00 UTC) July 6
- [ ] Test email sent to personal inbox: subject renders, image loads, CTA links to Respiratory bundle

---

## GOOGLE SHEETS SETUP INSTRUCTIONS

To activate this as a live dashboard:

1. Open Google Sheets. Create new spreadsheet: "Seedwarden Q3 Week 1-2 Email Dashboard".
2. Create Tab 1: rename to "Email 1 — Women's Health Jun 29".
3. Row 1: paste 8 column headers exactly as listed in the Dashboard Grid section above.
4. Rows 2–7: paste 6 date rows (Jun 29 through Jul 4). Pre-fill the Date column. Leave metric columns blank until data is pulled from Kit.com.
5. Column E (Threshold Status): set conditional formatting — GREEN background for "GREEN", YELLOW background for "YELLOW", RED background for "RED".
6. Column H (Alert): set text color red if the cell contains "RED".
7. Tab 2: rename to "Email 2 — Respiratory Jul 6". Repeat same structure for Jul 6–Jul 11 (6 rows).
8. Tab 3: rename to "Jul 1 Summary Gate". Paste the Summary Gate table from this document.
9. Share spreadsheet link with yourself via email for mobile access on launch day.

---

*Document prepared: June 29, 2026. Activate at Women's Health email send, 9:00 AM ET (13:00 UTC). Fill daily by 22:00 UTC. Final Email 1 baseline due Jul 1. Email 2 adjustment decisions due Jul 2 based on Jul 1 final baseline. Cross-reference WEEK_1_2_EMAIL_OPEN_CLICK_MONITORING_AND_ALERT_THRESHOLDS.md for full alert response procedures.*
