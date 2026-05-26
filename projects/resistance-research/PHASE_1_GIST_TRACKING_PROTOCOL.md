---
title: "Phase 1 Gist View Tracking Protocol"
created: 2026-05-26
version: 1.0
status: production-ready
scope: >
  Step-by-step protocol for weekly Bitly click snapshot extraction, spike detection,
  interpretation, and recording into the Gist Views tab of the monitoring dashboard.
  Two methods: Option A (manual, 3 min/week) and Option B (GitHub API, one-time
  15-min setup + 3 min/week). Includes troubleshooting and integration with
  the weekly synthesis.
companion_files:
  - PHASE_1_MONITORING_DASHBOARD_SHEETS_SPEC.md
  - PHASE_1_MONITORING_DASHBOARD.md
  - day-7-14-30-decision-trees.md
  - weekly-synthesis-template.md
  - DISTRIBUTION_GIST_URLS.md
setup_time_option_a: "5 minutes (one-time)"
weekly_time: "3 minutes per week"
first_snapshot_date: "Monday, June 2, 2026"
---

# Phase 1 Gist View Tracking Protocol

**Version 1.0 — May 26, 2026**

## What You Are Measuring

GitHub Gist does not expose view counts via any public API. The measurement proxy is Bitly click data: each outreach email contains a Bitly short link pointing to the Gist, and Bitly records every click on that short link. This is not identical to raw Gist views — it measures clicks from your outreach emails only, not all views — but it is the most reliable signal available without embedding tracking pixels or requiring contacts to authenticate.

This document covers two methods:
- **Option A: Manual Bitly Snapshot** — recommended. Zero coding, 3 minutes per week.
- **Option B: GitHub API Query** — for users comfortable with basic Python. Higher precision for fork/comment data; still relies on Bitly for click counts.

Choose Option A unless you have a specific reason to need Option B.

---

## One-Time Setup: Create Bitly Short Links

**Time required**: 5 minutes. Do this before May 28.

1. Go to bitly.com. Log in or create a free account.

2. For each Gist URL below, create a short link with the specified back-half. Back-half = the custom text after "bit.ly/":

| Gist Document | Full Gist URL | Bitly Short Link to Create |
|---------------|---------------|---------------------------|
| Domain 56 (Civil Service) | https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f | bit.ly/drp-d56 |
| Domain 39 (Healthcare) | https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b | bit.ly/drp-d39 |
| DRP Proposal | https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261 | bit.ly/drp-2026 |
| Executive Summary | https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4 | bit.ly/drp-summary |
| Litigation Tracker | https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0 | bit.ly/drp-litigation |

To create a custom back-half in Bitly free tier:
- Click "Create" > "Link"
- Paste the Gist URL in the destination field
- Expand "Customize back-half" and type the back-half (e.g., `drp-d56`)
- Click "Create"

3. Test each link immediately after creation:
   - Open an incognito browser window (important: incognito so it counts as a real click)
   - Paste the Bitly short link and press Enter
   - Confirm the Gist loads
   - Return to Bitly dashboard: verify the click count for that link incremented by 1

4. Replace all raw Gist URLs in your Domain 56 and Domain 39 email templates with the Bitly short links before sending.

**Critical**: If you send emails with raw Gist URLs (not Bitly short links), no click data will be captured and the Gist Views tab will show zero for the week even if contacts read the document. Verify this substitution before the May 28 send.

---

## Option A: Manual Weekly Snapshot

### When to Run

Every Monday morning, starting June 2 (one week after first send on May 28). Budget: 3 minutes.

If June 2 is your first snapshot, you are capturing Week 1 data (May 28–June 1).

### Step-by-Step Procedure

**Step 1** (1 minute): Log in to bitly.com. Click "Links" in the left sidebar to see all your short links.

**Step 2** (1 minute): For each tracked link, click the link name. On the link detail page, you will see a graph of clicks by day for the past 30 days and a "Total clicks" summary. Record the weekly total (Monday through Sunday of the prior week). Bitly free tier shows a daily breakdown — sum the days if the weekly view is not available.

Write down the numbers:
- Domain 56 clicks (bit.ly/drp-d56): ____
- Domain 39 clicks (bit.ly/drp-d39): ____
- DRP Proposal clicks (bit.ly/drp-2026): ____
- Executive Summary clicks (bit.ly/drp-summary): ____
- Litigation Tracker clicks (bit.ly/drp-litigation): ____

**Step 3** (1 minute): Open the Google Sheets dashboard. Navigate to the "Gist Views" tab. Add a new row at the bottom with:
- Column A: Week number (1, 2, 3, …)
- Column B: Sunday date of the week just ended (YYYY-MM-DD)
- Columns C–H: The click counts you just recorded
- Columns I–L: Auto-calculate from formulas already in the sheet
- Column M: Note any spike observations (see Spike Detection below)

**Step 4**: Add a one-line note to WORKLOG.md:
```
[Date] — Gist Views Week [N]: [X] total clicks ([+Y] vs prior week). Cumulative: [Z]. [Any spike note.]
```

### Example Week 1 Entry

```
Week_Number: 1
Week_End_Date: 2026-06-01
Domain56_Clicks: 8
Domain39_Clicks: 0    (Domain 39 not yet sent — sends June 1)
DRP_Proposal_Clicks: 3
DRP_Summary_Clicks: 2
LitigationTracker_Clicks: 2
Other_Links_Clicks: 0
Total_Clicks_This_Week: 15 [auto-calculated]
Cumulative_Clicks: 15 [auto-calculated]
Delta_vs_Prior_Week: — [first week]
Spike_Flag: [auto: SPIKE if any link >= 5, else blank]
Spike_Notes: "8 clicks on drp-d56 Day 1–2; correlates with May 28 Domain 56 send. Strong delivery confirmation."
```

---

## Spike Detection and Interpretation

**Spike definition**: Any single tracked link shows 5 or more clicks in the weekly period, OR any single day shows an unusual cluster relative to average.

### How to Check for Spikes in Bitly

1. On the link detail page, look at the daily click graph. A spike day is a bar substantially taller than surrounding days.
2. Note the date of the spike in Column M (Spike_Notes).
3. Cross-reference against your send schedule (see table below).

### Spike Interpretation Table

| Spike Timing Relative to Send | Interpretation | Action |
|-------------------------------|---------------|--------|
| 1–3 days after a Wave send | Delivery confirmed. Direct click-through from your outreach. | Note as "Send-correlated spike." No action required. |
| 4–7 days after send | Delayed read. Contact opened the email later. | Normal. Note date. |
| 7–14 days after send with no new Wave | Forwarding / amplification. A Tier 1 contact forwarded the email to colleagues who are now clicking. | Log as "Network multiplier signal" in Gist Views!M. Watch for replies from organizations not on your contact list. |
| Spike with no recent Wave at all | Organic amplification. Someone discovered the framework outside your direct outreach (search, social media, etc.). | Excellent signal. Log as "Organic amplification event." Escalate to user if a reply from an unknown organization follows. |
| Zero clicks for 2+ consecutive weeks after a previous spike | Traffic has dropped to zero. | Investigate: check if Gist became private, Bitly link broke, or interest has lapsed. |

### Spike Example Note Format

```
Spike: 6 clicks on bit.ly/drp-d56 on June 5 (Day 8).
Timing: 8 days after May 28 send — consistent with forwarding hypothesis.
Action: Watch for replies from non-contacted law school orgs through June 12.
```

---

## Option B: GitHub API Query (Advanced)

Use this only if you want real-time metadata (forks, comments) beyond what Bitly provides. Note: GitHub Gist API does not expose view counts — the Bitly approach remains the primary click-tracking method regardless of which option you choose. Option B supplements with star/fork/comment counts.

### One-Time Setup (15 minutes)

1. Go to github.com/settings/tokens. Click "Generate new token (classic)".
   - Name: `phase1-gist-tracking`
   - Scopes: `gist` (read-only is sufficient)
   - Expiration: 90 days
   - Save the token in your password manager.

2. Identify Gist IDs from the Gist URLs in `DISTRIBUTION_GIST_URLS.md`:
   - Domain 56 Gist ID: `8f11e868397921a4e6556b41196d1b1f`
   - Domain 39 Gist ID: `131e8a94c955b973b87f7fb87d0f594b`
   - DRP Proposal Gist ID: `2dec7fd03b08ab5b41c55d402f44c261`
   - Executive Summary Gist ID: `2869da6eaeb15a47246ade3bbbc4a3f4`
   - Litigation Tracker Gist ID: `418d51bda087f15a04d685ab171a5ee0`

3. Save the following script as `projects/resistance-research/gist_tracking.py`:

```python
import requests
import json
from datetime import datetime

GITHUB_TOKEN = "your_token_here"  # Replace with actual token

GIST_REGISTRY = {
    "domain56": "8f11e868397921a4e6556b41196d1b1f",
    "domain39": "131e8a94c955b973b87f7fb87d0f594b",
    "drp_proposal": "2dec7fd03b08ab5b41c55d402f44c261",
    "drp_summary": "2869da6eaeb15a47246ade3bbbc4a3f4",
    "litigation_tracker": "418d51bda087f15a04d685ab171a5ee0",
}

def query_gist(gist_id: str) -> dict:
    url = f"https://api.github.com/gists/{gist_id}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        data = response.json()
        return {
            "description": data.get("description", ""),
            "forks_count": data.get("forks_count", 0),
            "comments": data.get("comments", 0),
            "updated_at": data.get("updated_at", ""),
        }
    return {"error": f"HTTP {response.status_code}"}

print(f"Gist Tracking Snapshot — {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
print("=" * 60)
for name, gist_id in GIST_REGISTRY.items():
    stats = query_gist(gist_id)
    print(f"{name}: forks={stats.get('forks_count', 'ERR')}, comments={stats.get('comments', 'ERR')}, updated={stats.get('updated_at', 'ERR')[:10]}")
print("=" * 60)
print("Note: GitHub API does not expose raw view counts.")
print("Use Bitly dashboard for click counts (primary engagement metric).")
```

4. Run weekly with: `uv run python projects/resistance-research/gist_tracking.py`

5. Redirect output to a log file: `uv run python projects/resistance-research/gist_tracking.py >> projects/resistance-research/monitoring/gist-api-log.txt`

### What Option B Adds

- **Forks**: If a contact forks the Gist (makes a copy to their own GitHub account), this shows in the API response. Forks are a strong adoption signal.
- **Comments**: Gist comments from GitHub users. Rare but meaningful.
- **Updated_at timestamp**: Confirms when the Gist was last edited.

Option B does NOT replace Bitly. Always run Option A alongside Option B.

---

## Trigger Thresholds — When to Act

These thresholds trigger immediate action, not deferred review:

| Condition | When | Required Action |
|-----------|------|----------------|
| Week 1 total clicks < 5 with confirmed email delivery | June 4 (Day 7 checkpoint) | Bitly link integrity check: click each link in incognito, verify it increments. If broken: create new links, resend. |
| Week 1 total clicks 5–14 | June 4 | MONITOR status. Recheck at Day 14. No immediate action. |
| Week 1 total clicks 15+ | June 4 | HOLD status. Delivery confirmed. Proceed to Day 30 checkpoint. |
| Zero clicks in any week after Week 2 | Any Monday | ESCALATE. Check: Gist still public? Bitly link still valid? |
| Organic spike (spike day with no corresponding send) | Any Monday | Flag in Gist Views!M as "Organic amplification." Watch for replies from non-contacted organizations within 72 hours. |
| Week 4 cumulative clicks < 30 | July 6 | Add note to CHECKIN.md. Consider resend to non-responders or framing revision (see Modification 2 in day-7-14-30-decision-trees.md). |
| Week 4 cumulative clicks >= 60 | July 6 | On track for Day 60 100-click target. No action needed. |

**Messaging adjustment trigger**: If Day 14 cumulative clicks < 20 AND total reply count < 2, the outreach message may need revision. This is the trigger to review subject line and first paragraph. See Modification 2 in `day-7-14-30-decision-trees.md`.

---

## Integration with Weekly Synthesis

Every Monday, include a Gist Views section in your weekly synthesis file:

```
## Gist Views (Week of [date])

Domain 56 (bit.ly/drp-d56): [X] clicks this week
Domain 39 (bit.ly/drp-d39): [Y] clicks this week
All links total this week: [Z]
Cumulative to date: [N]

Spike detected: YES / NO
  If YES: [link name], [date], [interpretation]

Click velocity: [Z] clicks / [days since first send] = [X.X] clicks/day

Status vs. checkpoint targets:
  Week [N] target: [X]+ cumulative
  Actual: [N cumulative]
  Assessment: On track / Below target / Above target
```

This section feeds directly into Section 3 of `weekly-synthesis-template.md` and the Day 7/14/30 decision trees.

---

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---------|-------------|-----------|
| 0 clicks in Week 1, emails confirmed delivered | Bitly link broken in email, or email in spam | Test link in incognito. Check Gmail Sent folder — was the Bitly link included? Check contacts' spam folders if possible. |
| Clicks stopped abruptly after Day 3 | Normal: initial wave engagement exhausted | Expected. Second uptick should occur after Domain 39 send on June 1. |
| Spike on Day 15 with no recent send | Forwarding or organic amplification | Log as network multiplier. Watch for new email replies from non-contacted orgs. |
| Bitly shows 0 clicks but you receive email replies | Contacts already had the Gist URL from a prior communication, or Bitly link was not included in the email | Verify the email sent actually contained the Bitly link (not the raw Gist URL). If raw URL was used: future sends should use Bitly. |
| Cumulative and weekly totals disagree | Bitly refreshes daily totals at different times | Use the cumulative number as authoritative. Weekly is for delta only. |

---

**Status**: Production-ready. Complete one-time setup before May 28. Run first snapshot on Monday June 2.
