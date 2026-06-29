---
title: "Phase 3 Metrics Collection Dashboard — Google Sheets Setup"
date: 2026-06-29
version: 1.0
status: production-ready
scope: Pre-configured Google Sheets templates for real-time Week 1-2 metrics tracking
---

# Phase 3 Metrics Collection Dashboard

This document describes the Google Sheets dashboards for tracking Week 1-2 (June 29 – July 13) execution metrics. All sheets are **pre-configured with formulas** and ready to populate with daily data.

---

## Setup Instructions

### Create Google Sheet (One-Time Setup)

1. **Open Google Sheets**
   - Visit https://sheets.google.com/
   - Click "+ New" → "Blank spreadsheet"

2. **Name your sheet**
   - Click "Untitled spreadsheet" at top
   - Rename: "Phase 3 Week 1-2 Metrics — June 29 – July 13"

3. **Create four sheets** (tabs at bottom)
   - Right-click tab → "Insert sheet below"
   - Sheet 1: "Daily Email Metrics"
   - Sheet 2: "Daily Social Media Metrics"
   - Sheet 3: "Contractor Tracking"
   - Sheet 4: "Bundle Launch Readiness"

4. **Share access** (optional but recommended)
   - Click "Share" (top right)
   - Add collaborators or set to "Viewer" link-only for reference
   - Copy link for reference in PHASE_3_EXECUTION_CHECKLIST.md

### Sheet URLs for Reference

After setup, add these URLs to PHASE_3_WEEK_1_2_EXECUTION_CHECKLIST.md:

```
Google Sheets Dashboard:
https://docs.google.com/spreadsheets/d/[YOUR_SHEET_ID]/edit

Sheet 1 — Daily Email Metrics:
https://docs.google.com/spreadsheets/d/[YOUR_SHEET_ID]/edit#gid=0

Sheet 2 — Daily Social Media Metrics:
https://docs.google.com/spreadsheets/d/[YOUR_SHEET_ID]/edit#gid=[GID]

Sheet 3 — Contractor Tracking:
https://docs.google.com/spreadsheets/d/[YOUR_SHEET_ID]/edit#gid=[GID]

Sheet 4 — Bundle Launch Readiness:
https://docs.google.com/spreadsheets/d/[YOUR_SHEET_ID]/edit#gid=[GID]
```

---

## SHEET 1: Daily Email Metrics

**Purpose**: Track email opens, clicks, unsubscribes, and alerts for all emails sent Jun 29 – Jul 13.

### Column Headers (Row 1)

Copy-paste these headers into Row 1:

```
Date | Bundle | Email # | Send Time (ET) | Send Time (UTC) | Recipients | Delivered | Delivered % | Opens | Open % | Clicks | Click % | Bounces | Unsubscribes | Alert Status | Notes
```

### Column Widths

| Column | Width | Format | Notes |
|--------|-------|--------|-------|
| A (Date) | 100px | mm/dd/yyyy | Jun 29, Jun 30, Jul 6, etc. |
| B (Bundle) | 150px | Text | Women's Health / Respiratory / Sleep |
| C (Email #) | 80px | Number | 1, 2, or 3 |
| D (Send Time ET) | 120px | Time | 09:00 AM or 03:00 PM (for reference) |
| E (Send Time UTC) | 120px | Time | 13:00 or 19:00 (primary time) |
| F (Recipients) | 100px | Number | Count from Kit dashboard |
| G (Delivered) | 100px | Number | Count from Kit dashboard |
| H (Delivered %) | 100px | Percent (formula) | =G/F*100 |
| I (Opens) | 80px | Number | Count from Kit dashboard |
| J (Open %) | 100px | Percent (formula) | =I/G*100 |
| K (Clicks) | 80px | Number | Count from Kit dashboard |
| L (Click %) | 100px | Percent (formula) | =K/G*100 |
| M (Bounces) | 80px | Number | Count from Kit (if available) |
| N (Unsubscribes) | 100px | Number | Count from Kit (if available) |
| O (Alert Status) | 120px | Text (formula) | IF(J<15%,"🔴 LOW",IF(J<20%,"🟡 MEDIUM","🟢 NORMAL")) |
| P (Notes) | 200px | Text | Any special notes |

### Formulas

**Column H (Delivered %)**:
```
=IF(F=0,0,G/F*100)
```
Format as **Percent** with 1 decimal place.

**Column J (Open %)**:
```
=IF(G=0,0,I/G*100)
```
Format as **Percent** with 1 decimal place.

**Column L (Click %)**:
```
=IF(G=0,0,K/G*100)
```
Format as **Percent** with 1 decimal place.

**Column O (Alert Status)** — Conditional coloring:
```
=IF(J<0.15,"🔴 LOW",IF(J<0.20,"🟡 MEDIUM","🟢 NORMAL"))
```
Also set cell background colors:
- RED for "🔴 LOW" (open rate <15%)
- YELLOW for "🟡 MEDIUM" (open rate 15-20%)
- GREEN for "🟢 NORMAL" (open rate >20%)

### Data Entry (Sample Rows)

**Row 2 — Jun 29 Email 1 (Women's Health Launch)**:
```
06/29/2026 | Women's Health | 1 | 9:00 AM ET | 13:00 UTC | 312 | 308 | 98.7% | 68 | 22.1% | 19 | 6.2% | 2 | 0 | 🟢 NORMAL | Strong launch
```

**Row 3 — Jun 30 Email 2 (Women's Health Deep-Dive)**:
```
06/30/2026 | Women's Health | 2 | 9:00 AM ET | 13:00 UTC | 320 | 314 | 98.1% | 71 | 22.6% | 22 | 7.0% | 1 | 0 | 🟢 NORMAL | Day 1 follow-up
```

### Weekly Summary Rows

At the end of each week, add a **SUMMARY ROW** with formulas:

**Row 7 — Week 1 Total (Women's Health)**:
```
Sum of Recipients (Week 1): =SUM(F2:F6)
Average Open %: =AVERAGE(J2:J6)
Average Click %: =AVERAGE(L2:L6)
Total Unsubscribes (Week 1): =SUM(N2:N6)
```

**Example summary**:
```
Week 1 Total | Women's Health | [TOTAL: 3 emails] | — | — | 932 | 922 | 98.9% | 213 | 23.1% | 63 | 6.8% | 4 | 1 | 🟢 NORMAL | Week 1 average: 23% open
```

### Refresh Schedule

- **Daily**: Update at 18:00 UTC (4 hours after 09:00 ET send, captures early engagement)
- **End of week**: Add summary row with weekly totals and averages
- **Red flag alert**: If any email open rate <15%, flag immediately and investigate (see Failure Mode 4)

---

## SHEET 2: Daily Social Media Metrics

**Purpose**: Track Instagram and LinkedIn engagement for all posts sent Jun 29 – Jul 13.

### Column Headers (Row 1)

```
Date | Platform | Post # | Content Type | Post Time (ET) | Post Time (UTC) | Post URL | Impressions | Likes | Comments | Shares | Engagement Rate % | Alert Status | Notes
```

### Column Widths & Formats

| Column | Width | Format | Notes |
|--------|-------|--------|-------|
| A (Date) | 100px | mm/dd/yyyy | Jun 29, Jun 30, etc. |
| B (Platform) | 100px | Text | Instagram or LinkedIn |
| C (Post #) | 80px | Number | 1, 2, 3, etc. |
| D (Content Type) | 120px | Text | Educational / Testimonial / Promotional |
| E (Post Time ET) | 120px | Time | 10:00 AM or 03:00 PM (reference) |
| F (Post Time UTC) | 120px | Time | 14:00 or 19:00 (primary) |
| G (Post URL) | 250px | Text (URL) | https://www.instagram.com/p/[ID] |
| H (Impressions) | 100px | Number | From platform analytics (if available) |
| I (Likes) | 80px | Number | From platform or manual count |
| J (Comments) | 100px | Number | From platform or manual count |
| K (Shares) | 80px | Number | From platform or manual count |
| L (Engagement Rate %) | 120px | Percent (formula) | =(I+J+K)/H*100 OR manual estimation |
| M (Alert Status) | 120px | Text (formula) | IF(L<2%,"🔴 LOW",IF(L<4%,"🟡 MEDIUM","🟢 NORMAL")) |
| N (Notes) | 200px | Text | Top comment, unusual engagement, etc. |

### Formulas

**Column L (Engagement Rate %)**:
```
=IF(H=0,(I+J+K)*100/[BASELINE_FOLLOWER_COUNT],ROUND((I+J+K)/H*100,1))
```
For Week 1-2, use **manual input** if platform analytics unavailable. Estimate based on:
- Instagram baseline: 4-8% engagement (likes + comments + shares / impressions)
- LinkedIn baseline: 6-10% engagement

**Column M (Alert Status)** — Conditional:
```
=IF(L<0.02,"🔴 LOW",IF(L<0.04,"🟡 MEDIUM","🟢 NORMAL"))
```
Set cell colors:
- RED for <2% engagement (unusual low)
- YELLOW for 2-4% engagement (below target)
- GREEN for >4% engagement (normal to strong)

### Data Entry (Sample Rows)

**Row 2 — Jun 29 Instagram Post 1**:
```
06/29/2026 | Instagram | 1 | Educational/Promotional | 10:00 AM ET | 14:00 UTC | https://www.instagram.com/p/Cu1234abcd/ | 127 | 9 | 1 | 0 | 7.9% | 🟢 NORMAL | Launch post, good initial engagement
```

**Row 3 — Jun 30 LinkedIn Post 1**:
```
06/30/2026 | LinkedIn | 2 | Educational | 3:00 PM ET | 19:00 UTC | https://www.linkedin.com/feed/update/urn:li:activity:123456/ | 245 | 18 | 5 | 1 | 9.8% | 🟢 NORMAL | Professional audience, strong response
```

### Weekly Summary Rows

**Row 8 — Week 1 Social Total**:
```
Week 1 Total | Both | [5-6 posts] | Mixed | — | — | [Link to most-engaged post] | 1,200+ | 67 | 12 | 3 | 6.7% avg | 🟢 NORMAL | Instagram strong, LinkedIn excellent
```

### Refresh Schedule

- **Same-day**: Manually check platforms 2-4 hours after post (before "peak" engagement window closes)
- **Daily**: Update engagement metrics at 19:00 UTC
- **Weekly**: Add summary row with average engagement rate across platform

---

## SHEET 3: Contractor Tracking

**Purpose**: Monitor 6 contractors' deliverables, payment status, and responsiveness.

### Column Headers (Row 1)

```
Contractor Name | Assigned Bundles | Deliverable Type | Due Date | Status | Payment Sent | Payment Amount | Last Check-in | Response Status | Alert | Notes
```

### Column Widths & Formats

| Column | Width | Format |
|--------|-------|--------|
| A (Contractor Name) | 150px | Text |
| B (Assigned Bundles) | 150px | Text |
| C (Deliverable Type) | 150px | Text (photos/written/video) |
| D (Due Date) | 100px | mm/dd/yyyy |
| E (Status) | 120px | Dropdown: Not started / In progress / Complete / Delayed |
| F (Payment Sent) | 100px | YES / NO |
| G (Payment Amount) | 100px | Number ($) |
| H (Last Check-in) | 120px | Date |
| I (Response Status) | 150px | Text (Responded / Awaiting / Unresponsive) |
| J (Alert) | 100px | Text (formula) |
| K (Notes) | 200px | Text |

### Sample Data (6 Contractors)

```
Contractor 1 | Women's Health | Photos (8-10) | Jul 4 | In progress | YES | $50 | Jul 1 | Responded — on track | ✓ | Day 1-2 shoot scheduled
Contractor 2 | Women's Health | Testimonials (3) | Jul 4 | Complete | YES | $50 | Jul 1 | Responded — complete | ✓ | Submitted Jun 30
Contractor 3 | Respiratory | Photos (8-10) | Jul 11 | In progress | YES | $50 | Jul 7 | Responded — on track | ✓ | Started Jul 5
Contractor 4 | Respiratory | Written (500-word) | Jul 11 | In progress | YES | $50 | Jul 7 | Awaiting response | ⚠ | Follow-up needed Jul 8
Contractor 5 | Sleep | Photos (6-8) | Jul 18 | Not started | NO | $50 | Jul 7 | Responded — on track | ✓ | Starting next week
Contractor 6 | Sleep | Video (2-3 min) | Jul 18 | Not started | NO | $50 | — | Awaiting initial check-in | ⚠ | Contact Jul 8
```

### Alert Formula (Column J)

```
=IF(E="Delayed","🔴 OVERDUE",IF(AND(E="In progress",D<=TODAY()+3),"🟡 DUE SOON","✓ ONTRACK"))
```

### Refresh Schedule

- **Weekly**: Monday 09:00 UTC + Friday 17:00 UTC (contractor check-in days)
- **As-needed**: Update status when contractor responds or delivers
- **Payment verification**: End of each week (Friday)

---

## SHEET 4: Bundle Launch Readiness

**Purpose**: High-level GO/NO-GO status for each bundle launch (Women's Health, Respiratory, Sleep, etc.).

### Column Headers (Row 1)

```
Bundle Name | Launch Date | Email Templates Ready | Social Posts Scheduled | Contractor Deliverables | Email Engagement | Launch Status | Go/No-Go | Notes
```

### Column Widths & Formats

| Column | Width | Format | Values |
|--------|-------|--------|--------|
| A (Bundle Name) | 150px | Text | Women's Health / Respiratory / Sleep / etc. |
| B (Launch Date) | 100px | mm/dd/yyyy | Jun 29 / Jul 6 / Jul 13 |
| C (Email Ready) | 100px | YES / NO | Checked against PHASE_3_BUNDLE_LAUNCH_EMAIL_SEQUENCES.md |
| D (Social Ready) | 100px | YES / NO | Posts scheduled in Buffer/Later/Meta Business Suite |
| E (Contractor Deliverables) | 150px | ON TRACK / DELAYED / COMPLETE | Based on Sheet 3 status |
| F (Email Engagement) | 120px | Percent OR "Pending" | After Day 1 send: [%] open rate |
| G (Launch Status) | 120px | Dropdown: READY / AT RISK / BLOCKED | |
| H (Go/No-Go) | 100px | 🟢 GO / 🟡 CAUTION / 🔴 NO-GO | Executive summary |
| I (Notes) | 200px | Text | Key issues, contingencies, etc. |

### Sample Data (3 Bundles in Week 1-2 Scope)

```
Women's Health | 06/29/2026 | YES | YES | COMPLETE | 23.1% (Day 1) | READY | 🟢 GO | All systems ready, strong email open rate
Respiratory | 07/06/2026 | YES | YES | ON TRACK | Pending | READY | 🟡 CAUTION | Contractor 4 slightly delayed, catchup plan in place
Sleep | 07/13/2026 | YES | YES | ON TRACK | Pending | READY | 🟢 GO | Launch staging complete, ready for handoff
```

### Refresh Schedule

- **Before each bundle launch**: Day 0 morning (update to READY status if all items YES)
- **Launch day**: After first email send, update engagement percentage
- **Post-launch**: Day 3 to assess success and plan next bundle

---

## QUICK ACCESS LINKS

**Copy these links to PHASE_3_WEEK_1_2_EXECUTION_CHECKLIST.md after creating sheet**:

### Main Dashboard
- **URL**: https://docs.google.com/spreadsheets/d/[YOUR_SHEET_ID]/edit
- **View**: All sheets visible from this link

### Direct Sheet Links
- **Sheet 1 (Email Metrics)**: https://docs.google.com/spreadsheets/d/[YOUR_SHEET_ID]/edit#gid=0
- **Sheet 2 (Social Metrics)**: https://docs.google.com/spreadsheets/d/[YOUR_SHEET_ID]/edit#gid=[GID_2]
- **Sheet 3 (Contractor Tracking)**: https://docs.google.com/spreadsheets/d/[YOUR_SHEET_ID]/edit#gid=[GID_3]
- **Sheet 4 (Bundle Readiness)**: https://docs.google.com/spreadsheets/d/[YOUR_SHEET_ID]/edit#gid=[GID_4]

---

## MAINTENANCE NOTES

- **Auto-refresh**: Google Sheets does NOT auto-pull from Kit or Instagram. **Manual data entry required** at scheduled times (see Refresh Schedule above).
- **Backup**: Google Sheets auto-saves. No manual backup needed.
- **After Week 1-2**: Archive this sheet. Create new sheet for Week 3-4 (Jul 14-27) following same template.
- **Permission**: Share read-only link with user or collaborators for visibility during execution.

---

## DOCUMENT VERSION

**Version**: 1.0  
**Date**: June 29, 2026  
**Sheets**: 4 (Email, Social, Contractor, Bundle Readiness)  
**Total rows per sheet**: 20-30 (7 data rows + summaries + headers)  
**Setup time**: 20-30 minutes (one-time)  
**Daily refresh time**: 10-15 minutes per day
