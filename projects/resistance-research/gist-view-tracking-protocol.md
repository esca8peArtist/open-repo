---
title: "Gist View Tracking Protocol — Phase 1 Wave 1"
created: 2026-05-26
version: 1.0
status: production-ready
scope: >
  Weekly procedure for capturing Gist view counts via Bitly click tracking.
  Two methods: (A) Manual snapshot for simplicity; (B) Automated GitHub API query
  for higher precision. Includes spike detection and interpretation guidance.
word_count: ~1600
companion_files:
  - PHASE_1_WAVE_1_MONITORING_DASHBOARD.md
  - PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md
  - DISTRIBUTION_GIST_URLS.md
setup_time: "5 minutes per week"
---

# Gist View Tracking Protocol — Phase 1 Wave 1

**Version 1.0 — May 26, 2026**

## Overview

Gist views are your primary **passive engagement signal**. Unlike email replies (which require recipient action + decision to respond), Gist views indicate that someone has:
1. Received and opened the email
2. Clicked the link
3. Read (or started to read) the document

This protocol explains how to capture weekly Gist view counts and what the numbers mean.

**Quick choice**: If you want simplicity, use **Option A (Manual Snapshot)** below. It takes 3 minutes per week and requires no coding. If you want precision and don't mind a one-time 15-minute setup, use **Option B (Automated)**.

---

## Option A: Manual Weekly Snapshot (Recommended for Simplicity)

Use this method if you prefer point-in-time snapshots without automated infrastructure.

### Setup (One-Time, 5 Minutes)

1. Create a free Bitly account at `bitly.com` (or use existing account)
2. Create one Bitly short link per Gist, mapping to the canonical URLs in `DISTRIBUTION_GIST_URLS.md`:
   - Example: `bit.ly/drp-domain56` → (Domain 56 Gist URL)
   - Example: `bit.ly/drp-domain39` → (Domain 39 Gist URL)
3. Replace all raw Gist URLs in your Phase 1 email templates with the Bitly short links
4. Before sending: Test each link by opening it in an incognito browser and confirming the Gist loads

**Important**: One link per Gist (not per contact), so you can aggregate view counts across all recipients who received the same Gist.

### Weekly Snapshot Procedure (Every Monday, 3 Minutes)

1. Open `bitly.com/a/dashboard` and log in
2. For each Bitly link you created:
   - Click the link to view its details
   - Note the **total clicks** for the week (Bitly shows daily breakdown; sum Monday–Sunday)
   - Record this number in your **Gist Views** sheet, **Column C (Domain56_Clicks)** or **Column D (Domain39_Clicks)**
3. Fill in **Column E (Total_Week_Clicks)** with the sum: `=SUM(C2:D2)`
4. Fill in **Column F (Cumulative_Clicks)** with a running sum: `=SUM($C$2:C2)` (auto-updates each week)

### Example Snapshot (Week 1 of Phase 1)

```
Week_Number: 1
Week_End_Date: June 1, 2026
Domain56_Clicks: 8
Domain39_Clicks: 7
Total_Week_Clicks: 15 (=SUM(8+7))
Cumulative_Clicks: 15 (first week)
Spike_Flag: NO
Spike_Notes: [blank]
```

### Success Targets by Week

| Week | Timing | Cumulative Click Target | Meaning |
|------|--------|------------------------|---------|
| Week 1 | Day 1–7 | 15+ clicks | Delivery confirmed; minimum viable engagement across constituencies |
| Week 2 | Day 8–14 | 30+ cumulative clicks | Sustained engagement; not a one-time click pattern |
| Week 3 | Day 15–21 | 45+ cumulative clicks | Ongoing discussion/forwarding; strong signal |
| Week 4 | Day 22–28 | 60+ cumulative clicks | By Day 30 checkpoint: indicates strong trajectory |
| Week 8 | Day 50–56 | 100+ cumulative clicks | By Day 60 checkpoint: indicates sustained movement-scale interest |

### Spike Detection (Manual)

**Spike definition**: Any single day with 5+ clicks on any one link.

**How to detect**:
1. In Bitly dashboard, click each link to see the daily breakdown
2. Look for any day with a spike (5+ clicks above the daily average)
3. If found: note the date in your **Gist Views sheet**, **Column G (Spike_Notes)**

**Interpretation**:
- **Spike 24–72 hours after a Wave send**: Confirms the wave was received and people are clicking through. Good signal.
- **Spike 7–14 days after send**: Indicates forwarding/amplification. Example: Law school faculty forwards the Gist to all clinic directors; they all click on the same day. This is a **network multiplier signal**. Very good.
- **Spike with no recent Wave send**: Indicates **organic amplification** — someone found the framework outside of your direct outreach (web search, social media share, etc.). Excellent signal.

**Example spike note**:
```
Spike_Notes: 6 clicks on bit.ly/drp-domain56 on June 5 (Day 8).
Likely cause: Law school group email forwarded to multiple clinic directors.
Network multiplier signal: flag for Day 30 checkpoint review.
```

**What to do when you detect a spike**:
1. Note it in the Gist Views sheet
2. Cross-reference the date against your email wave send schedule
3. If it's 24–72 hours post-send: Add a note saying "Delivery confirmed, strong engagement"
4. If it's post-Day 7 organic: Add a note saying "Network multiplier detected" and watch for follow-up replies from non-contacted orgs
5. If a spike leads to new non-contacted-list replies, escalate to user: "Organic amplification detected — [Org Name] found us through referral"

---

## Option B: Automated GitHub API Query (Advanced, Higher Precision)

Use this method if you prefer real-time data, don't mind a 15-minute setup, and are comfortable with basic API calls.

### Setup (One-Time, 15 Minutes)

1. **Get a GitHub personal access token**:
   - Go to `github.com/settings/tokens`
   - Click "Generate new token (classic)"
   - Name: `phase1-gist-tracking`
   - Scopes: Select `gist` (read-only)
   - Expiration: 90 days
   - Copy the token; save it in a secure location (password manager, not plain text)

2. **Identify Gist IDs**:
   - For each Gist in Phase 1 distribution, extract the Gist ID from the URL
   - Example: `https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f`
   - Gist ID = `8f11e868397921a4e6556b41196d1b1f`
   - Create a reference list with Gist ID ↔ Domain mapping (keep in a text file)

3. **Create tracking script** (Python):
   ```python
   import requests
   import json
   from datetime import datetime

   GITHUB_TOKEN = "your_token_here"
   GIST_IDS = {
       "domain56": "8f11e868397921a4e6556b41196d1b1f",
       "domain39": "...",
   }

   def get_gist_forks_stars(gist_id):
       url = f"https://api.github.com/gists/{gist_id}"
       headers = {"Authorization": f"token {GITHUB_TOKEN}"}
       response = requests.get(url, headers=headers)
       if response.status_code == 200:
           data = response.json()
           return {
               "forks": data.get("forks_count", 0),
               "stars": data.get("comments", 0),  # comments as proxy for engagement
           }
       return {"forks": 0, "stars": 0}

   for domain, gist_id in GIST_IDS.items():
       stats = get_gist_forks_stars(gist_id)
       print(f"{domain}: Forks={stats['forks']}, Engagement={stats['stars']}")
       print(f"Timestamp: {datetime.now()}")
   ```

4. **Save script** as `gist_tracking.py` in the resistance-research project directory
5. **Run weekly**: `uv run python gist_tracking.py` every Monday at 9 AM, redirect output to a log file, then manually enter the results in your Gist Views sheet

### Automated vs. Manual Trade-off

| Aspect | Manual (Option A) | Automated (Option B) |
|--------|------------------|-------------------|
| Setup time | 5 minutes | 15 minutes |
| Weekly time | 3 minutes | 3 minutes (just run script) |
| Precision | Daily aggregates | Real-time query |
| Accuracy | Bitly-based (proxy) | GitHub-based (authoritative) |
| Complexity | Zero coding | Minimal Python |
| Recommended for | Most users | Users comfortable with API calls |

**Recommendation**: Start with **Option A (Manual)**. If by Week 2 you find the weekly snapshots are not capturing important spike patterns, switch to **Option B**.

---

## Interpreting Click Velocity

Click velocity is **clicks per day** since the wave send. It predicts engagement trajectory:

```
High velocity (>2 clicks/day for first 7 days)
  → Indicates strong immediate uptake
  → Expect 3+ replies by Day 14
  → Phase 2 STRONG signal likely at Day 30

Medium velocity (0.5–2 clicks/day for first 7 days)
  → Normal baseline engagement
  → Expect 1–2 replies by Day 14
  → Phase 2 MODERATE signal at Day 30

Low velocity (<0.5 clicks/day, even with confirmed delivery)
  → Below baseline; investigate delivery or content issues
  → Check: Are links in emails broken? Is domain name unfamiliar to recipients?
  → Possible action: Resend to corrected list or adjust framing for Day 14 re-send

Zero velocity (0 clicks despite confirmed email delivery)
  → Critical issue; requires immediate investigation
  → Check: Did emails get marked as spam? Is Bitly link broken?
  → Action: Run delivery diagnostic immediately
```

---

## Handling Ambiguities

### Multiple Bitly Links in One Email

If you include multiple Gist links in the same email (e.g., "See the full framework [link] or the executive summary [link]"), use separate Bitly links for each Gist. This lets you see which documents are generating the most interest.

**Example**:
```
bit.ly/drp-domain56-full → Domain 56 (full)
bit.ly/drp-domain56-summary → Domain 56 (summary)
```

Record both in the Gist Views sheet and analyze click patterns:
- If full version gets 8 clicks and summary gets 2: people want depth
- If summary gets more: people prefer quick reference

### Forwarded Emails (Secondary Recipients)

When a Tier 1 contact forwards the email to a peer organization, the peer may click the Gist link. **You won't know who they are** from the Bitly data alone, but you might:
1. See a spike in clicks on a day when no Wave was sent
2. Later receive a reply from the peer organization mentioning the Tier 1 contact as the source

When this happens:
- **Bitly data**: Shows up as a spike day
- **Email reply**: Contact says "I got this from [Tier 1 contact]"
- **Action**: Log in **Adoptions sheet** as "Referral" and in **Network Map** sheet as a network event

### Cross-Domain Gist Links

If Domain 56 and Domain 39 are distributed in different waves (May 28 vs. June 1), create separate Bitly links and track separately:

| Link | Domain | Send Date | Contacts | Target Clicks by Day 7 |
|------|--------|-----------|----------|----------------------|
| `bit.ly/drp-domain56` | Domain 56 | May 28 | 11 law schools + civil rights | 7–10 clicks by June 4 |
| `bit.ly/drp-domain39` | Domain 39 | June 1 | 5 immigration legal aid | 4–6 clicks by June 8 |

This lets you track each wave's performance independently.

---

## Weekly Gist Views Sheet Template

Copy this into your Google Sheets **Gist Views** sheet (Row 1 = headers):

```
Week_Number | Week_End_Date | Domain56_Clicks | Domain39_Clicks | Total_Week_Clicks | Cumulative_Clicks | Spike_Flag | Spike_Notes
1           | June 1, 2026  | [Bitly total]   | [Bitly total]   | =SUM(C2:D2)       | =SUM($C$2:C2)    | YES/NO    | [date, reason]
2           | June 8, 2026  | [Bitly total]   | [Bitly total]   | =SUM(C3:D3)       | =SUM($C$2:C3)    | YES/NO    | [if any]
...
```

---

## Troubleshooting Click Count Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| 0 clicks in Week 1, but emails delivered | Emails possibly marked as spam | Check spam folder; re-send to corrected list |
| Clicks stopped after Day 3 | Content fatigue or audience exhaustion | Normal after initial wave. Expect uptick when Domain 39 sends on June 1 |
| Spike on Day 15, no recent send | Organic amplification or forwarding | Good sign. Log as network multiplier. Watch for new replies from non-contacted orgs |
| Bitly showing 0 clicks but receiving replies | Bitly link may be broken OR recipients already have Gist open | Check Bitly link works; add fallback note in weekly synthesis |
| Different click counts in Bitly daily vs. cumulative | Bitly refreshes daily totals; cumulative is always authoritative | Use the cumulative number in your Gist Views sheet |

---

## Integration with Weekly Synthesis

Every Monday, include a brief Gist Views section in your `weekly-synthesis-template.md`:

```
## Gist Views (Week of June 3)

Domain 56 clicks this week: 8
Domain 39 clicks this week: 7
Cumulative clicks to date: 15

Spike detected this week: NO
Velocity: 2.1 clicks/day (15 clicks / 7 days)
Status: On track for Day 7 minimum (target: 15+ by June 4)
```

This feeds directly into your Day 7 checkpoint decision (see `day-7-14-30-decision-trees.md`).

---

**Status**: Production-ready. Choose Option A or B before May 28, and execute the first weekly snapshot on Monday, June 3, 2026.

