---
title: "Track B Monitoring Automation Framework — Day 3/7/14 Checkpoints"
created: 2026-06-04
status: production-ready
launch-date: 2026-06-04
day-3: 2026-06-07
day-7: 2026-06-11
day-14: 2026-06-18
purpose: >
  Metric collection procedures, automation scripts, and data-gathering runbooks
  for the June 4–18 post-launch tracking window. Designed to be executed in
  15–20 minutes per checkpoint without requiring a Claude session.
references:
  - CONTINGENCY_TRIGGER_DECISION_TREE.md (numeric thresholds, GO/CAUTION/NO-GO)
  - POST_LAUNCH_ANALYSIS_TEMPLATE.md (metric collection sheet)
  - DAY_3_AND_7_DECISION_GATES.md (predecessor framework, May 30 launch)
  - CONTINGENCY_DECISION_THRESHOLDS.md (original threshold reference)
  - TRACK_B_HERBALIST_OUTREACH_MATRIX.md (influencer response log)
---

# Track B Monitoring Automation Framework
## Day 3 / Day 7 / Day 14 Post-Launch Checkpoints

**Launch date**: June 4, 2026 (13:00 UTC activation)
**Day 3 checkpoint**: June 7, 2026 at 08:00 UTC
**Day 7 checkpoint**: June 11, 2026 at 08:00 UTC
**Day 14 checkpoint**: June 18, 2026 at 08:00 UTC
**Tracking window**: June 4–18, 2026

**Time to complete each checkpoint**: 15–20 minutes

---

## Overview

Three checkpoints gate three decisions:

| Checkpoint | Date | Primary decision |
|-----------|------|-----------------|
| Day 3 | June 7 | Is early traction sufficient to activate contingency amplification? |
| Day 7 | June 11 | Which channels to accelerate? Sales velocity check. Phase 2 scope? |
| Day 14 | June 18 | Full performance review. Phase 2 expansion go/no-go. Archive. |

Each section below provides: (1) where to find each metric, (2) how to query it, (3) the collection template, and (4) threshold reference.

---

## Day 3 Checkpoint — June 7, 2026 at 08:00 UTC

**Purpose**: Quick pulse on initial adoption. Catch critical failures before they compound. Identify any amplification opportunities while the launch window is still active.

---

### Metric 1: Email Open Rate — Campaign Monitor

**Where**: Campaign Monitor dashboard > Campaigns > [launch broadcast name]

**Manual procedure (2 minutes)**:
1. Log in at campaignmonitor.com
2. Navigate to Campaigns tab
3. Locate the launch email broadcast (sent June 4)
4. Click "View Report"
5. Record:
   - Total sent
   - Opens (unique)
   - Open rate %
   - Click rate %
   - Unsubscribes
   - Bounce rate

**Automation option — Campaign Monitor API**:

If the Campaign Monitor API key is configured, run this query. Replace `CAMPAIGN_ID` with the actual campaign ID visible in the campaign URL.

```bash
# Replace API_KEY and CAMPAIGN_ID before running
curl -s -u "API_KEY:x" \
  "https://api.createsend.com/api/v3.2/campaigns/CAMPAIGN_ID/summary.json" \
  | python3 -c "
import sys, json
d = json.load(sys.stdin)
print('Opens (unique):', d.get('UniqueOpened'))
print('Open rate:     ', round(d.get('UniqueOpened',0) / d.get('TotalRecipients',1) * 100, 1), '%')
print('Clicks:        ', d.get('Clicks'))
print('Click rate:    ', round(d.get('Clicks',0) / d.get('TotalRecipients',1) * 100, 1), '%')
print('Unsubscribes:  ', d.get('Unsubscribed'))
print('Bounces:       ', d.get('Bounced'))
print('Total sent:    ', d.get('TotalRecipients'))
"
```

**Threshold reference** (from CONTINGENCY_TRIGGER_DECISION_TREE.md):
- GO: open rate >= 20%
- CAUTION: 10–19%
- NO-GO trigger: < 10% (or < 5% within first 6 hours)

---

### Metric 2: Gist View Count

**Where**: The Gist URL used as the distribution endpoint for Zone Cards.

**Manual procedure (1 minute)**:
1. Log in to github.com
2. Navigate to gist.github.com/[username]
3. Open the Zone Card Gist
4. The view count is displayed at the top right of the Gist page (next to the star count)
5. Record: cumulative views since June 4

**Automation option — GitHub API**:

```bash
# Replace GITHUB_TOKEN and GIST_ID
curl -s -H "Authorization: token GITHUB_TOKEN" \
  "https://api.github.com/gists/GIST_ID" \
  | python3 -c "
import sys, json
d = json.load(sys.stdin)
print('Gist ID:      ', d.get('id'))
print('Description:  ', d.get('description'))
print('Forks:        ', len(d.get('forks', [])))
print('Comments:     ', d.get('comments'))
print('Updated:      ', d.get('updated_at'))
# Note: GitHub API does not expose raw view counts for Gists.
# View count must be read directly from the Gist web page.
print('VIEW COUNT: check gist.github.com/[username] directly — not in API')
"
```

Note: GitHub's Gist API does not return view counts. The count visible on the Gist page is the authoritative number. Check the page directly and record manually.

**Threshold reference**:
- GO: > 70 views by 72h
- CAUTION: 30–70
- NO-GO trigger: < 30

---

### Metric 3: Influencer Activity — Twitter/Instagram Mentions

**Where**: Twitter (X) search, Instagram mentions/tags, and the email inbox.

**Manual procedure — Twitter search (2 minutes)**:

Run each search query in twitter.com/search and record hit count and any accounts that posted:

```
Search 1: seedwarden
Search 2: "zone quick-start" OR "zone card" herbalism
Search 3: "wild edibles" "zone" since:2026-06-04
```

For each result found: note the username, post URL, approximate reach (follower count visible on profile), and whether the account is one of the 15 influencer contacts.

**Manual procedure — Instagram (2 minutes)**:

1. Open Instagram > Profile > Tags tab (content where you are tagged)
2. Also search hashtag: #seedwarden, #zonecard, #wildedibles
3. Note any tags or mentions by the 15 influencer contacts

**Tracking template — Day 3 influencer activity**:

```
Influencer contacts reached (total outreach sent): ___ / 15
Contacts who replied (any response): ___
Contacts who confirmed they will share: ___
Contacts who shared publicly by Day 3:
  - [Name]: [platform] [post URL if available]
  - [Name]: [platform] [post URL if available]
Organic third-party mentions (not the 15 contacts): ___
  - [Handle]: [platform] [post URL if available]
```

**Threshold reference**:
- GO: 1+ influencer contacts confirmed sharing publicly
- CAUTION: responses received but no public shares yet
- NO-GO trigger: 0 responses from all 15 contacts after 72h

---

### Metric 4: Sales and Referral Attribution

**Where**: Etsy Shop Manager, Gumroad dashboard (if applicable), PayPal activity.

**Etsy — Manual procedure (2 minutes)**:
1. Log in to etsy.com/your/shops/[shopname]/tools/stats
2. Select date range: June 4 to today
3. Record:
   - Listing views (per product)
   - Visits
   - Orders
   - Revenue

**PayPal — Manual procedure (1 minute)**:
1. Log in to paypal.com > Activity
2. Filter by date: June 4 onwards
3. Record any transactions linked to seedwarden/Zone Card sales

**Referral tracking** (if Bitly or UTM links were set up):
- Bitly: bitly.com/a/bitlinks — click the short link to see click count by source
- Google Analytics (if landing page has GA4): check Acquisition > Traffic Acquisition for source/medium breakdown

**Day 3 revenue template**:

```
Etsy listing status: Active / Draft / Not live
Etsy listing views (since June 4): ___
Etsy orders: ___
Etsy revenue: $___
PayPal transactions (seedwarden): ___  total $___
Referral channel breakdown (if UTM/Bitly active):
  - Direct: ___  clicks
  - Email: ___  clicks
  - Social: ___  clicks
  - Influencer referral: ___  clicks
```

**Threshold reference**:
- GO: any sales (even 1)
- CAUTION: views but zero conversions
- NO-GO trigger: 0 sales AND Etsy listing status is Draft or inactive

---

### Metric 5: User Onboarding Funnel

**Where**: Kit (formerly ConvertKit) dashboard.

**Kit — Manual procedure (3 minutes)**:
1. Log in to kit.com
2. Navigate to Subscribers tab
3. Filter: created after June 4, 2026
4. Record:
   - New subscribers (total since launch)
   - Subscribers who opened Email 1 (zone card delivery email)
   - Subscribers who clicked the PDF download link in Email 1

For Kit automation email stats:
1. Go to Automations > [Zone Card welcome sequence]
2. Click on Email 1 step
3. View open rate and click rate for that step

**PDF download proxy** (Kit click rate on Email 1 is the best available signal for PDF downloads from the email funnel):

```
Kit new subscribers (since June 4): ___
Email 1 open rate: ___%
Email 1 PDF link click rate: ___%
  (click rate = PDF download rate proxy)
Estimated PDF downloads via email: ___ (subscribers x click rate)
```

**Threshold reference**:
- GO: email subscription rate > 5% of Gist visitors (healthy funnel)
- CAUTION: 2–5% conversion
- NO-GO trigger: Kit automation paused or 0 new subscribers despite Gist traffic

---

### Day 3 Complete Collection Template

Copy and fill in at 08:00 UTC June 7:

```
DAY 3 METRIC SNAPSHOT — June 7, 2026 08:00 UTC
Launch: June 4, 2026 | Elapsed: 72 hours

EMAIL (Campaign Monitor)
  Open rate: ___%    (threshold: GO >20%, CAUTION 10-19%, NO-GO <10%)
  Click rate: ___%
  Unsubscribe rate: ___%
  Total sent: ___

GIST DISTRIBUTION
  Cumulative views: ___    (threshold: GO >70, CAUTION 30-70, NO-GO <30)
  Day 1 views: ___
  Day 2 views: ___
  Day 3 views: ___

INFLUENCER ACTIVITY
  Contacts reached: ___ / 15
  Responses received: ___
  Public shares confirmed: ___    (threshold: GO >=1, CAUTION 0 shares/responses received, NO-GO 0 responses)
  Third-party organic mentions: ___

SOCIAL MEDIA
  Instagram reach (cumulative): ___
  Instagram new followers: ___
  Twitter/X mentions: ___
  Reddit upvotes (all posts): ___
  Reddit comments: ___

SALES / REVENUE
  Etsy listing status: Active / Draft / Not live
  Etsy views: ___
  Etsy orders: ___    (threshold: GO >=1, NO-GO 0 AND listing not live)
  Total revenue: $___

ONBOARDING FUNNEL (Kit)
  New subscribers: ___
  Email 1 open rate: ___%
  Email 1 PDF click rate: ___%

DAY 3 OVERALL STATUS: GO / CAUTION / NO-GO
```

---

## Day 7 Checkpoint — June 11, 2026 at 08:00 UTC

**Purpose**: Aggregate the first full week. Identify channel velocity trends. Make the Phase 2 scope decision. Run cohort split between early adopters (days 1–3) and late followers (days 4–7).

---

### Day 7 Metric Collection

**Full week cumulative totals** (June 4 – June 11):

Run all the same queries from Day 3 but collect 7-day totals. Add the following new metrics:

**Engagement trend analysis — Day 3 vs Day 7**:

Calculate the daily average for each half of the week:
- Days 1–3 average Gist views per day = (Day 3 cumulative) / 3
- Days 4–7 average Gist views per day = (Day 7 cumulative - Day 3 cumulative) / 4

If days 4–7 average > days 1–3 average: content is gaining momentum (uncommon, very positive).
If days 4–7 average roughly equals days 1–3: stable organic reach.
If days 4–7 average < 50% of days 1–3: initial spike has faded, dependent on continued promotion.

**Email engagement trend — Campaign Monitor**:

If a second email was sent during days 4–7 (e.g., a follow-up broadcast or a second Kit automation email):
1. Pull stats on Email 2 open rate
2. Compare to Email 1 open rate
3. If Email 2 open rate < 60% of Email 1: normal decay, no action needed
4. If Email 2 open rate < 30% of Email 1: deliverability issue or audience mismatch. Check spam folder and Kit automation health.

**Cohort analysis — early adopters vs late followers**:

- Early adopters: subscribers who joined June 4–6 (first 72h)
- Late followers: subscribers who joined June 7–10 (days 4–7)

In Kit, segment by join date (Subscribers > filter by date range). Compare:
- Email 1 open rate for early cohort vs late cohort
- PDF download click rate for each cohort

If late cohort open rate is higher: influencer shares or organic discovery is bringing a more engaged audience (positive signal — influencer channel is working).
If early cohort open rate is higher: the launch-day audience was most engaged (typical for opt-in email audiences; not a problem).

**Sales velocity per channel**:

By Day 7 you should have enough data to see whether any sales came from:
- Direct (typed URL or bookmark)
- Email campaign (UTM: utm_source=email)
- Social (UTM: utm_source=instagram, utm_source=reddit)
- Influencer referral (UTM: utm_source=influencer_[name])

If Bitly or UTM links were not set up before launch: attribute by timing. Sales within 6h of the launch email going out are likely email-attributed. Sales arriving in clusters after a Reddit post spike are likely Reddit-attributed.

**Twitter/X mention search scripts** (run in browser search bar):

```
from:@[influencer_handle] seedwarden   (check each of the 15 contacts)
#seedwarden since:2026-06-04
"zone card" OR "zone quick-start" since:2026-06-04
```

Record any found mentions in the influencer log at TRACK_B_HERBALIST_OUTREACH_MATRIX.md.

---

### Day 7 Complete Collection Template

```
DAY 7 METRIC SNAPSHOT — June 11, 2026 08:00 UTC
Launch: June 4, 2026 | Elapsed: 7 days (168 hours)

EMAIL (Campaign Monitor)
  Launch broadcast open rate: ___%
  Launch broadcast click rate: ___%
  Unsubscribe rate: ___%
  Follow-up broadcast open rate (if sent): ___%

GIST DISTRIBUTION
  Cumulative 7-day views: ___    (threshold: GO >200, CAUTION 100-200, NO-GO <100)
  Days 1-3 average views/day: ___
  Days 4-7 average views/day: ___
  Trend: ACCELERATING / STABLE / FADING

INFLUENCER ACTIVITY (cumulative 7 days)
  Public shares by influencer contacts: ___    (threshold: GO >=3, CAUTION 1-2, NO-GO 0)
  Third-party organic mentions: ___
  Affiliate interest expressed: ___
  Contacts still awaiting follow-up: ___

SOCIAL MEDIA (cumulative 7 days)
  Instagram total reach: ___    (threshold: GO >500, CAUTION 200-500, NO-GO <200)
  Instagram followers gained: ___
  Twitter/X mentions (total): ___
  Reddit upvotes (all posts, all communities): ___
  Reddit comments: ___
  Pinterest saves: ___

SALES / REVENUE (cumulative 7 days)
  Etsy views: ___
  Etsy orders: ___
  Total revenue: $___
  Revenue channel attribution:
    Email: $___
    Social: $___
    Direct: $___
    Influencer referral: $___

ONBOARDING FUNNEL (Kit — cumulative 7 days)
  Total new subscribers: ___
  Early cohort (days 1-3) open rate: ___%
  Late cohort (days 4-7) open rate: ___%
  Overall funnel conversion (subscribers / Gist views): ___%

COHORT COMPARISON
  Early adopter quality signal: HIGHER / EQUAL / LOWER than late followers
  Primary traffic driver this week: EMAIL / REDDIT / INSTAGRAM / INFLUENCER / ORGANIC

DAY 7 OVERALL STATUS: GO / CAUTION / NO-GO
PHASE 2 SCOPE DECISION: EXPAND / MAINTAIN / ADJUST (see CONTINGENCY_TRIGGER_DECISION_TREE.md)
```

---

## Day 14 Checkpoint — June 18, 2026 at 08:00 UTC

**Purpose**: Full campaign performance review. Identify best-performing assets. Make Phase 2 expansion decision. Archive all metrics for post-launch synthesis.

---

### Day 14 Metric Collection

Collect the same metrics as Day 7 but for the full 14-day window. Add the following:

**Email sequence completion rates** (Kit):

For the Kit welcome automation, track completion rates per email step:
- Email 1 open rate (delivery step) — already tracked at Day 3/7
- Email 2 open rate (follow-up/engagement step)
- Email 3 open rate (product introduction, if scheduled)
- Unsubscribe rate across full sequence

A healthy sequence decay: Email 1 ~35–45%, Email 2 ~25–35%, Email 3 ~20–30%.
An unhealthy decay: Email 2 open rate below 15% suggests subject line or content mismatch.

**Best-performing asset identification**:

1. Best zone (most requested/mentioned): search Instagram DMs, email inbox, and Reddit comments for zone number mentions. Tally per zone. The top zone is the Phase 2 anchor.
2. Best email subject line: compare open rates across all broadcasts and automation steps. Note the subject line text that performed best.
3. Best influencer contact: from TRACK_B_HERBALIST_OUTREACH_MATRIX.md, identify which single contact drove the most downstream traffic.
4. Best platform per-post reach: calculate (total platform reach) / (number of posts on that platform) for each channel.

**Phase 2 expansion inputs**:

By Day 14 you need to answer:
- Expand contact list? (Yes if influencer channel drove >30% of traffic)
- Add new distribution channels? (Yes if one untested channel e.g. Substack Notes, Pinterest, LinkedIn had high organic discovery)
- Scale paid promotion budget? (Yes only if at least 1 organic sale per $0 spent is proven; paid amplifies working channels)
- Second product readiness: is medicinal herbs bundle content production justified? (Gate: Day 14 GO status + any revenue signal)

---

### Day 14 Complete Collection Template

```
DAY 14 METRIC SNAPSHOT — June 18, 2026 08:00 UTC
Launch: June 4, 2026 | Elapsed: 14 days

EMAIL (Campaign Monitor — cumulative)
  Total broadcast sends: ___
  Best open rate (broadcast name): ___  at ___%
  Worst open rate: ___  at ___%
  Cumulative unsubscribes: ___    (threshold: NO-GO if >5% of list)
  Unsubscribe rate (% of total sent): ___%

GIST DISTRIBUTION (cumulative 14 days)
  Total views: ___    (threshold: GO >400, CAUTION 150-400, NO-GO <150)
  Week 1 views: ___
  Week 2 views: ___
  Week-over-week trend: ___

INFLUENCER ACTIVITY (cumulative 14 days)
  Total public shares: ___    (threshold: GO >=3, CAUTION 1-2, NO-GO 0)
  Total organic third-party mentions: ___
  Affiliate partnerships established: ___
  Influencer contacts to follow up in Phase 2: ___

SOCIAL MEDIA (cumulative 14 days)
  Instagram total reach: ___    (threshold: GO >1000, CAUTION 500-1000, NO-GO <500)
  Instagram followers gained: ___
  Twitter/X total mentions: ___
  Reddit total upvotes: ___
  Pinterest total saves: ___
  Best-performing platform (per-post avg reach): ___  at ___ reach/post

SALES / REVENUE (cumulative 14 days)
  Total Etsy orders: ___
  Total revenue: $___
  Sales velocity Week 1: $___
  Sales velocity Week 2: $___
  Primary revenue channel: EMAIL / SOCIAL / DIRECT / INFLUENCER

ONBOARDING FUNNEL (Kit — cumulative 14 days)
  Total new subscribers: ___
  Email 1 open rate: ___%
  Email 2 open rate: ___%
  Email 3 open rate (if sent): ___%
  Sequence unsubscribe rate: ___%
  Funnel conversion (subscribers / Gist views): ___%

BEST-ASSET IDENTIFICATION
  Best zone (most requested): Zone ___
  Best email subject line: "___"  open rate: ___%
  Best influencer contact: ___  (traffic contribution: ___)
  Best platform (per-post reach): ___  at ___ avg reach/post

DAY 14 OVERALL STATUS: GO / CAUTION / NO-GO
PHASE 2 DECISION: see CONTINGENCY_TRIGGER_DECISION_TREE.md Section 5
```

---

## Contingency Trigger Quick Reference

Full decision trees are in CONTINGENCY_TRIGGER_DECISION_TREE.md. Quick reference:

| Trigger | Threshold | Immediate action |
|---------|-----------|-----------------|
| Low email open rate | < 20% | Check Kit/Campaign Monitor delivery logs; check spam; verify SPF/DKIM |
| Very low open rate | < 10% | Treat as delivery failure; re-send via Gmail to Tier 1 contacts |
| Low Gist views | < 50 at Day 7 | Audit URL placement in all social bios; check Reddit post removal |
| Zero sales | 0 at Day 7 | Verify Etsy listing is Active; check listing title SEO; add paid bundle if not live |
| Influencer silence | 0 responses from all 15 at Day 7 | Send one follow-up to top 5 with social proof numbers; try DM if email bounced |
| High unsubscribe rate | > 5% | Pause any additional broadcasts; audit email content for mismatch with audience expectations |

---

*Document version: 1.0 — June 4, 2026*
*References: CONTINGENCY_TRIGGER_DECISION_TREE.md, POST_LAUNCH_ANALYSIS_TEMPLATE.md, DAY_3_AND_7_DECISION_GATES.md*
