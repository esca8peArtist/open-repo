# Integration with Phase 1 Measurement Dashboard

## Overview

The adoption tracking script collects data that populates the Phase 1 Measurement Dashboard (Google Sheets). This guide shows how to integrate the script's output with your dashboard.

---

## Weekly Workflow (10 minutes)

### 1. Script Runs Automatically (Monday 08:00 AM)

The script runs via cron every Monday and generates:
- `monitoring/adoption-summary-YYYY-MM-DD.md` — Human-readable summary
- `scripts/data/gist-views.csv` — Gist analytics history
- Updated email log if using Gmail API

### 2. Review Summary

```bash
cat monitoring/adoption-summary-$(date +%Y-%m-%d).md
```

### 3. Manual Import to Dashboard (5 minutes)

#### Update Gist View Log Sheet

From the summary, copy Gist view counts into the **Gist View Log** sheet:

**Column mapping:**

| Script Output | Dashboard Column |
|---------------|------------------|
| full_proposal | C (DRP_Proposal_Clicks) or relevant domain |
| executive_summary | D (DRP_Summary_Clicks) |
| litigation_tracker | E (DRP_Litigation_Clicks) |
| first_amendment | F (DRP_FA_Clicks) |

**Example workflow:**

```
1. Check: monitoring/adoption-summary-2026-06-03.md
2. Find: "- **full_proposal**: 42 views"
3. Go to: Gist View Log sheet, Week 2 row
4. Enter: 42 in column C (DRP_Proposal_Clicks)
5. Repeat for each gist
6. Formula auto-calculates totals
```

#### Update Master Contact Log Sheet

From email replies section, update contact status:

**Column mapping:**

| Email Reply | Dashboard Column |
|-------------|------------------|
| from_email | Match to contact row |
| subject | Add to H (First_Reply_Date) |
| reply_type | Update I (Reply_Score) |
| snippet | Update P (Notes) |

**Reply type to score mapping:**

- "substantive" → Reply_Score: 3 or higher
- "question" → Reply_Score: 3 (substantive)
- "thanks-no-action" → Reply_Score: 2
- "forward" → Reply_Score: 3+ (forwarding = collaboration request)
- "out-of-office" → Reply_Score: 1

---

## Automated Integration (Optional)

For full automation, configure Google Sheets API credentials.

### Setup (one-time, 5 minutes)

1. **Get Spreadsheet ID:**
   ```
   From your Google Sheet URL:
   https://docs.google.com/spreadsheets/d/ABC123XYZ/edit
   Use: ABC123XYZ
   ```

2. **Create service account and JSON key:**
   - Go to [console.cloud.google.com](https://console.cloud.google.com)
   - Create new project or select existing
   - Enable "Google Sheets API"
   - Create service account key (JSON format)
   - Save to: `scripts/sheets-credentials.json`

3. **Share Google Sheet with service account:**
   - Open your adoption tracking Google Sheet
   - Click Share
   - Add service account email (from JSON file)
   - Give "Editor" access

4. **Update config:**
   ```json
   {
     "github_username": "your-username",
     "sheets_credentials": "/path/to/scripts/sheets-credentials.json",
     "spreadsheet_id": "your-spreadsheet-id"
   }
   ```

### Automatic Updates

Once configured, the script automatically:
1. Fetches Gist view counts
2. Parses email replies
3. Updates `Gist View Log` sheet with view counts
4. Updates `Master Contact Log` sheet with reply info

No manual work needed beyond reviewing summaries.

---

## Data Structures

### Gist View Log Integration

**Script CSV:**
```csv
timestamp,gist_label,gist_id,cumulative_views,week_number,notes
2026-06-03T08:15:22,full_proposal,2dec7fd0...,42,23,
2026-06-03T08:15:33,executive_summary,2869da6e...,38,23,
```

**Maps to Dashboard Sheet "Gist View Log":**

| Column | Header | Data |
|--------|--------|------|
| A | Week_Number | 23 |
| B | Week_End_Date | 2026-06-08 |
| C | DRP_Proposal_Clicks | 42 |
| D | DRP_Summary_Clicks | 38 |
| E | DRP_Litigation_Clicks | (from script) |
| I | Total_Clicks_Week | =SUM(C23:H23) |
| J | Cumulative_Clicks | =I22+I23 |

### Master Contact Log Integration

**Email replies CSV (if using manual log):**
```csv
date,from_email,from_name,subject,snippet,reply_type
2026-06-01,jane@harvard.edu,Jane Doe,RE: Framework distribution,Thanks for sending...,substantive
```

**Maps to Dashboard Sheet "Master Contact Log":**

| Column | Header | Data |
|--------|--------|------|
| E | Email | jane@harvard.edu |
| H | First_Reply_Date | 2026-06-01 |
| I | Reply_Score | 3 (from reply_type: substantive) |
| P | Notes | From: Jane Doe, Harvard... |

---

## Tracking Lifecycle

### Week 1 (Distribution Launch)

**Script does:**
- Fetches Gist views (expect: 0–5 views)
- Fetches email replies (expect: 0–2 replies)
- Triggers alerts if zero activity on both fronts

**Dashboard update:**
- Populate Gist View Log Week 1 row
- Log any replies in Master Contact Log
- Begin Engagement Timeline (daily summary)

### Week 2–4 (Active Engagement)

**Script does:**
- Collects cumulative view counts (trends upward)
- Captures reply messages and first-response timing
- Detects forwarding events (secondary distribution)

**Dashboard update:**
- Update Gist View Log each week
- Add new replies to Master Contact Log
- Compute Score 3+ percentages in Engagement Timeline

### Week 8+ (Checkpoint Window)

**Script does:**
- Provides historical view counts and reply timeline
- Feeds data for adoption signal detection

**Dashboard update:**
- Prepare Month 1 and Month 3 snapshots (Section 3 of PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE.md)
- Use script data for Adoption Signal Registry
- Document citation events (separate monitoring tool)

---

## Checkpoint Integration

The script data directly feeds the three key checkpoint decisions:

### Day 7 Checkpoint

**Data from script:**
- Total Gist views across all links
- Count of any substantive replies

**Decision gate (from PHASE_1_MEASUREMENT_DASHBOARD_TEMPLATE.md Section 3):**
```
Week 1 target: 15+ total clicks
If: Total_Clicks_Week < 15 → Investigate delivery (email bounces, link broken)
```

### Day 30 (Month 1) Checkpoint

**Data from script:**
- Cumulative view counts from Gist View Log
- Reply rate calculation: Replies / Delivered emails
- First substantive reply timing

**Decision gate:**
```
Minimum meaningful adoption: 5+ unique citation events across 2+ sectors
Script provides: view counts + reply evidence
Dashboard calculates: adoption level scores (0–4 scale)
```

### Day 60–90 (Month 3) Checkpoint

**Data from script:**
- Full 8-week view trend (time series)
- All reply events with categorization
- Secondary distribution signals (forwarding mentions)

**Decision gate:**
```
Domain heat map: which domains generating engagement vs. silence
Score 3+ rate: substantive replies / delivered
Phase 2 threshold: if 40%+ of Tier 1 contacts at Level 2+
```

---

## Troubleshooting Integration

| Problem | Diagnosis | Fix |
|---------|-----------|-----|
| Data not appearing in sheet | Service account not shared | Verify share permissions on Google Sheet |
| Gist views always zero | Gist IDs incorrect or not accessible | Verify CANONICAL_GISTS in script match actual Gists |
| Replies not syncing | Email monitoring disabled | Check config: gmail_credentials or gmail_manual_log |
| Manual import takes too long | Too much data to copy | Enable automated sync (configure sheets_credentials) |
| Week numbers don't match | ISO week vs. calendar week mismatch | Dashboard uses calendar weeks 1-8, script uses ISO |

---

## CSV File Formats (For Reference)

### Gist Views CSV

```csv
timestamp,gist_label,gist_id,cumulative_views,week_number,notes
2026-06-03T08:15:22.123456,full_proposal,2dec7fd03b08ab5b41c55d402f44c261,42,23,
2026-06-03T08:15:33.234567,executive_summary,2869da6eaeb15a47246ade3bbbc4a3f4,38,23,
2026-06-03T08:15:44.345678,litigation_tracker,418d51bda087f15a04d685ab171a5ee0,35,23,
2026-06-03T08:15:55.456789,first_amendment,10d0a86e386e6c3c11c3830295a6503c,22,23,
```

### Email Replies CSV (Manual Log)

```csv
date,from_email,from_name,subject,snippet,reply_type
2026-06-01,nicholas.stephanopoulos@law.harvard.edu,Nicholas Stephanopoulos,RE: 35-Domain Framework Distribution,This is excellent work on the efficiency gap analysis in Domain 1...,substantive
2026-06-02,wendy.weiser@brennancenter.org,Wendy Weiser,Quick clarification on Domain 33,Could you elaborate on the state legislative autocratization mechanisms...,question
2026-06-03,ian@protectdemocracy.org,Ian Bassin,Forwarding to our litigation team,I'm sharing this with our Domain 29 specialists - expect follow-up...,forward
```

---

## Next Steps

1. **After first script run (May 31):** Review monitoring summary and verify Gist/email collection working
2. **For June 1 execution:** Ensure script scheduled and logs being generated
3. **Ongoing (Weeks 1–8):** Import data weekly to dashboard; monitor dashboard metrics against checkpoint gates
4. **At Day 30 and Day 60:** Use script data + citation monitoring to populate Adoption Signal Registry and trigger decision gates

---

*For issues or customization requests, see ADOPTION_TRACKING_DEPLOYMENT_GUIDE.md troubleshooting section.*
