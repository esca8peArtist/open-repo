---
title: "Phase 1 Impact Evaluation — Integration with Adoption-Tracking-Script.py"
created: 2026-06-06
version: 1.0
status: production-ready
scope: >
  How the real-time dashboard (PHASE_1_IMPACT_EVALUATION_DASHBOARD.md) integrates
  with the existing phase-1-adoption-tracking-script.py. Roles, division of labor,
  weekly reconciliation checklist, and automation ideas for post-Phase-1 cycles.
companion_files:
  - PHASE_1_IMPACT_EVALUATION_DASHBOARD.md
  - PHASE_1_IMPACT_EVALUATION_ROUTING.md
  - phase-1-adoption/phase-1-adoption-tracking-script.py
word_count: ~1100
---

# Phase 1 Impact Evaluation — Integration with adoption-tracking-script.py

**Version 1.0 — June 6, 2026**

**Lead finding**: The adoption-tracking-script.py is a weekly batch system. It fetches Gist view counts via GitHub API, monitors Gmail replies via Gmail API, and writes a structured weekly Markdown summary to `monitoring/`. It is authoritative for post-hoc verification — it does not require manual data entry and catches things a manual dashboard might miss (e.g., a reply in a Gmail label not checked that day). The real-time dashboard is an intra-week operational layer. The two systems are complementary; they should not contradict each other by Day 7.

---

## 1. Division of Labor

| Function | Real-Time Dashboard | adoption-tracking-script.py |
|----------|--------------------|-----------------------------|
| Data entry model | Manual daily (8–10 min/day) | Automated weekly batch |
| Primary use | Intra-window decisions (June 10–17) | Post-hoc verification and weekly synthesis |
| Engagement velocity | Yes (hourly, daily deltas) | No (weekly snapshot only) |
| Phase 2 routing triggers | Yes (auto-alert cells) | No (data collection only) |
| Gist view count | Bitly as proxy (daily) | GitHub API + HTML scrape (weekly) |
| Email reply count | Manual Gmail audit | Gmail API (automated) |
| Adoption signal registry | Adoptions tab (manual) | Weekly summary Markdown |
| Day 7 checkpoint integration | Primary input for decision tree | Parallel verification run |
| Archive / audit trail | Google Sheets (persistent) | monitoring/week-*.md files |

**The reconciliation rule**: At Day 7 (June 17), both systems should be run. If they disagree on a metric by more than 20% (e.g., dashboard shows 12 Bitly clicks, script shows 9 via GitHub API), investigate the discrepancy before recording the Day 7 determination. Usually this reflects a difference between Bitly click tracking (who clicked the short link) and GitHub view tracking (who accessed the Gist directly) — both are valid but measure slightly different things.

---

## 2. How to Run the Script

The canonical script is at:
```
/home/awank/dev/SuperClaude_Framework/projects/resistance-research/phase-1-adoption/phase-1-adoption-tracking-script.py
```

The stub at `projects/resistance-research/phase-1-adoption-tracking-script.py` redirects to the canonical version.

**Day 7 run** (June 17, after completing the morning dashboard update):
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/resistance-research
uv run python phase-1-adoption-tracking-script.py --run-now --config phase-1-adoption-tracking.json --output-dir monitoring
```

**What the script generates**:
- `monitoring/week-2026-06-17-summary.md` — Gist view counts, email reply list, alerts triggered
- Console output: JSON summary with gist_views, email_replies, leading_alerts

**Script configuration** (`phase-1-adoption-tracking.json` template is at `phase-1-adoption-tracking-config.json.template`):

Required fields:
```json
{
  "github_token": "[YOUR_GITHUB_TOKEN]",
  "github_username": "esca8peArtist",
  "gmail_credentials": "[PATH_TO_GMAIL_OAUTH_JSON]",
  "spreadsheet_id": "[GOOGLE_SHEETS_ID_FOR_MAIN_DASHBOARD]"
}
```

If Gmail OAuth credentials are not set up, the script still runs Gist view collection — set `gmail_credentials` to null to skip Gmail monitoring.

---

## 3. Tab 7: INTEGRATION — Google Sheets Reconciliation Zone

The INTEGRATION tab in the real-time dashboard (Tab 7) serves as the reconciliation zone. After running the script on Day 7, paste key outputs here and compare against dashboard values.

### Column Schema

| Col | Header | Notes |
|-----|--------|-------|
| A | Metric | Pre-populated list of reconciliation metrics |
| B | Dashboard_Value | Value from real-time dashboard (manual entry) |
| C | Script_Value | Value from script output (manual entry from monitoring/week-* file) |
| D | Delta | Formula: `=ABS(B2-C2)` |
| E | Delta_Pct | Formula: `=IF(C2=0,"N/A",IFERROR(D2/C2,"N/A"))` |
| F | Discrepancy_Flag | Formula: `=IF(E2="N/A","REVIEW",IF(E2>0.2,"DISCREPANCY","OK"))` |
| G | Reconciliation_Note | Text — explanation if discrepancy detected |

### Pre-Populated Metric Rows (A2:A8)

```
Row 2:  Cumulative Gist clicks / views (7-day total)
Row 3:  Total email replies received
Row 4:  Score 3+ replies
Row 5:  Bounce count
Row 6:  Total adoption signals detected
Row 7:  Constituencies with any signal
Row 8:  Network/referral events
```

### Acceptable Discrepancy Ranges

| Metric | Acceptable Delta | Explanation |
|--------|-----------------|-------------|
| Gist clicks/views | ≤20% | Bitly click count vs. GitHub view count measure different things; some drift is expected |
| Email replies | ≤5% | Both sources access Gmail; small delta indicates labeling difference |
| Score 3+ replies | 0 | Scoring is manual; both sources should agree exactly (same human scores both) |
| Bounce count | 0 | Exact match expected; bounces are definitive |
| Adoption signals | 0 | Same manual entry; both sources should agree |

---

## 4. Weekly Reconciliation Checklist (June 10–July 10)

Run this checklist once per week, on the same day as the script run.

### Week 1 (June 17 — Day 7 Checkpoint)

- [ ] Dashboard morning update complete (DAILY_SIGNALS row 8 filled)
- [ ] CONSTITUENCY_TRACKER all 7 rows updated with final Day 7 signals
- [ ] REPLY_LOG all received replies logged with scores
- [ ] Script run: `uv run python phase-1-adoption-tracking-script.py --run-now`
- [ ] `monitoring/week-2026-06-17-summary.md` opened; key metrics extracted
- [ ] INTEGRATION tab filled: Dashboard values vs. Script values for all 8 metrics
- [ ] Discrepancy review: Any metric with DISCREPANCY flag → investigate and note explanation
- [ ] Day 7 checkpoint decision tree run (PHASE_1_DAY_7_CHECKPOINT_DECISION_TREE.md)
- [ ] Determination recorded in DAILY_SIGNALS Column L Row 8 and Checkpoints tab
- [ ] CHECKIN.md updated with Day 7 summary
- [ ] Routing decisions executed per PHASE_1_IMPACT_EVALUATION_ROUTING.md

**Total time**: 45–60 minutes (Day 7 checkpoint is the most time-intensive weekly event)

### Week 2 (June 24 — Day 14 Check, if Day 7 = MONITOR)

- [ ] Dashboard daily updates complete through June 24
- [ ] Script run: `uv run python phase-1-adoption-tracking-script.py --run-now`
- [ ] `monitoring/week-2026-06-24-summary.md` extracted
- [ ] INTEGRATION tab updated with Week 2 values
- [ ] Day 14 check per PHASE_1_DAY_7_CHECKPOINT_DECISION_TREE.md Part 3
- [ ] Any Tier C contacts who haven't replied by Day 14: root-cause survey sent (Routing doc Section 3.3)
- [ ] CHECKIN.md updated

**Total time**: 20–25 minutes

### Week 3 (July 1 — Interim Progress Check)

- [ ] Dashboard updated through July 1
- [ ] Script run
- [ ] INTEGRATION tab updated
- [ ] Adoption signals reviewed in Adoptions tab: any new confirmed adoptions since Day 7?
- [ ] Network Map reviewed: any new referral events?
- [ ] CHECKIN.md updated with brief interim note

**Total time**: 15–20 minutes

### Week 4 (July 10 — Day 30 Checkpoint)

- [ ] All dashboard tabs fully current
- [ ] Script run with full output
- [ ] INTEGRATION tab final reconciliation
- [ ] Day 30 checkpoint per PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Section 5
- [ ] Overall reply rate calculated from Contacts tab
- [ ] Constituencies_Strong count from Constituencies tab
- [ ] Cross-org references counted from Adoptions tab (Signal_Type = Referral)
- [ ] Confirmed adoption signals counted from Adoptions tab (Verification_Status = Confirmed)
- [ ] STRONG / MODERATE / WEAK / FAILURE determination made
- [ ] Phase 2 acceleration or hold decision executed per PHASE_1_IMPACT_EVALUATION_ROUTING.md Section 4
- [ ] CHECKIN.md updated with Day 30 summary and Phase 2 decision

**Total time**: 45–60 minutes

---

## 5. Automation Ideas for Post-Phase-1 Cycles

The current setup is intentionally manual-first: manual daily data entry with formulas for calculation. This approach is appropriate for Phase 1 because the volume is manageable (45 Tier 1 contacts, 7 domains) and because manual entry catches edge cases that automated scraping misses (e.g., a reply buried under an OOO thread, a forwarded email not in the expected Gmail label).

For Phase 2 and Phase 3, as contact lists expand to hundreds of contacts and dozens of domains, the following automation improvements would materially reduce overhead:

**Automation improvement 1: Bitly API integration into the script**

The adoption-tracking-script.py already has a `GistAnalyticsCollector` class. Extend it to poll the Bitly API (v4 REST API, free tier supports daily click pulls) and write directly to a Google Sheets cell via the `SheetsSync` class. This eliminates the 3-minute manual Bitly check from the morning routine.

Implementation: Add a `BitlyAnalyticsCollector` class to the script with `get_daily_clicks(link_id)` method. Bitly v4 API requires `Authorization: Bearer [token]` header. The endpoint is `GET https://api-ssl.bitly.com/v4/bitlinks/{bitlink_id}/clicks?unit=day&units=7`.

**Automation improvement 2: REPLY_LOG auto-population from Gmail API**

The script's `EmailReplyMonitor.get_recent_replies()` method already fetches recent replies. The gap is that it writes to a Markdown summary file rather than directly appending to the REPLY_LOG tab. Adding a `SheetsSync.append_reply_log(reply_dict)` method would eliminate the 4-minute manual Gmail audit.

Implementation: Extend `EmailReplyMonitor` to call `SheetsSync.append_reply_log()` for each new reply. Requires a scoring heuristic (keyword-based: "will cite," "will use," "forwarded" → Score 4–5; "thank you," "appreciate" → Score 2; explicit question words → Score 3). Manual override is still recommended for boundary cases, but auto-population handles routine cases.

**Automation improvement 3: ALERTS tab webhook notifications**

The ALERTS tab fires visual alerts in Google Sheets — but only if you have the sheet open. For real-time awareness during the June 10–17 window, consider setting up a Google Sheets Apps Script trigger that sends an email notification when any ALERTS!C column cell changes from CLEAR to ACTIVE.

Implementation (Google Apps Script, paste in Sheets → Extensions → Apps Script):
```javascript
function checkAlerts() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('ALERTS');
  var statuses = sheet.getRange('C2:C9').getValues();
  var alerts = sheet.getRange('A2:A9').getValues();
  var active = [];
  
  for (var i = 0; i < statuses.length; i++) {
    if (statuses[i][0] === 'ACTIVE') {
      active.push(alerts[i][0]);
    }
  }
  
  if (active.length > 0) {
    MailApp.sendEmail(
      'wanka95@gmail.com',
      'Phase 1 Alert: ' + active.join(', '),
      'Active alerts as of ' + new Date().toISOString() + ':\n\n' + active.join('\n')
    );
  }
}
```

Set a time-based trigger to run `checkAlerts()` every hour during the June 10–17 window. This provides near-real-time alert delivery without requiring the sheet to be open.

To set the trigger: Google Apps Script → Triggers (clock icon) → Add trigger → checkAlerts → Time-driven → Hour timer → Every hour. Active June 9–17 only; delete or disable afterward to avoid unnecessary API quota use.

---

## 6. System Architecture Summary

```
DATA SOURCES
├── Gmail (replies)
│   ├── Real-time: Manual REPLY_LOG daily entry (8 AM morning check)
│   └── Automated: adoption-tracking-script.py Gmail API pull (weekly)
├── Bitly (click tracking)
│   ├── Real-time: Manual GIST_VELOCITY daily entry (Bitly dashboard)
│   └── Future: Bitly API integration into script (Automation improvement 1)
└── GitHub (Gist view counts)
    └── Automated: adoption-tracking-script.py API + HTML scrape (weekly)

PROCESSING
├── Real-Time Dashboard (Google Sheets)
│   ├── DAILY_SIGNALS: threshold status, Phase 2 signal, daily velocity
│   ├── CONSTITUENCY_TRACKER: per-constituency 7-day matrix
│   ├── REPLY_LOG: per-reply scoring with routing flags
│   ├── GIST_VELOCITY: Bitly click velocity and spike detection
│   └── ALERTS: auto-firing alert board
└── adoption-tracking-script.py
    ├── Weekly batch collection (Gist views + Gmail replies)
    ├── Alert detection (zero views, zero replies)
    └── monitoring/week-*.md output files

DECISION LAYER
├── Real-time: ALERTS tab → intra-window routing (PHASE_1_IMPACT_EVALUATION_ROUTING.md)
├── Day 7: PHASE_1_DAY_7_CHECKPOINT_DECISION_TREE.md (primary decision tree)
└── INTEGRATION tab: reconciliation between dashboard and script outputs

OUTPUT
├── CHECKIN.md: escalation and decision records
├── Routing actions: follow-up emails per PHASE_1_IMPACT_EVALUATION_ROUTING.md
└── Phase 2 activation: per DOMAIN_51_JUNE_16_DECISION_LOGIC.md and Day 7 decision tree
```
