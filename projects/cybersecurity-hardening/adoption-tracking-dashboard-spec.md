---
title: "Adoption Tracking Dashboard Spec"
project: cybersecurity-hardening
created: 2026-05-01
status: ready-for-use
session: 717
depends-on: post-distribution-impact-tracker.md, feedback-collection-template.csv
---

# Adoption Tracking Dashboard Spec

**Purpose**: Define the monitoring infrastructure to run alongside the CSV tracker. The CSV captures what you know from direct contact. The dashboard catches what you would otherwise miss: organic citations, social sharing, and policy references that happen without a reply email.

**Cost**: All monitoring tools described here have free tiers sufficient for this use case. No paid subscriptions required.

---

## Component 1: GitHub Gist Traffic Tracker

### What to Track and When

Log the following data from the Gist dashboard monthly. The Gist dashboard shows view counts and referrer breakdown when you are logged in as the account owner.

| Metric | Log Frequency | Where to Log |
|--------|--------------|--------------|
| Total view count | Monthly (first of each month) | Gist traffic log (see template below) |
| Top 5 referrers | Monthly | Gist traffic log |
| Unique visitors | Monthly if available | Gist traffic log |

### Gist Traffic Log Template (add rows monthly)

```
Date       | Total Views | Delta | Top Referrer 1           | Top Referrer 2      | Notes
-----------+-------------+-------+--------------------------+---------------------+------
2026-05-15 | [baseline]  | —     | direct                   | —                   | Launch day baseline
2026-06-01 | [log]       | [+N]  |                          |                     | End of week 2
2026-07-01 | [log]       | [+N]  |                          |                     | 45-day mark
2026-08-01 | [log]       | [+N]  |                          |                     | 90-day mark
2026-11-01 | [log]       | [+N]  |                          |                     | 180-day mark
2027-05-01 | [log]       | [+N]  |                          |                     | 12-month mark
```

### Interpretation Benchmarks

- **Flat growth (0-10 incremental views/month)**: Organic traffic is not occurring. The corpus is not being shared beyond initial sends.
- **Slow growth (10-50 incremental views/month)**: Some referral sharing is occurring. Expected for a narrowly targeted initial distribution.
- **Moderate growth (50-200 incremental views/month)**: Organic amplification is happening — likely from social sharing or a link appearing in a newsletter or resource page.
- **Spike (200+ views in a single month)**: A major referral source (media article, org newsletter, conference mention) drove traffic. Cross-reference with Google Alert results and social media monitoring to identify the source.

For context, comparable civil society security documentation hosted on GitHub (e.g., Access Now's security guides, EFF's Surveillance Self-Defense) achieves thousands of views over the course of months once picked up by digital rights networks. This corpus, distributed to a more specific audience, should aim for 500-1,500 total views in the first 180 days if distribution is working. Below 300 total views at 90 days is a signal that something is not functioning in the distribution chain.

### If Migrating to a Full GitHub Repository

If the corpus is ever moved from a Gist to a full GitHub repository (`github.com/[account]/opsec-corpus` or similar), additional metrics become available:

- **Stars**: Track weekly for first 3 months, monthly thereafter. Comparable security guidance repos in the civil society space (SAFETAG: ~400 stars over 8 years; Access Now Digital Security Helpline guides: variable by sub-guide, typically 50-200 stars) suggest realistic targets of 20-50 stars in the first 6 months for a targeted distribution of this type.
- **Forks**: Each fork indicates someone intends to adapt or reference the content. Track fork count monthly; a fork from a known Tier 1 or Tier 2 organization domain is a Stage 4 adoption signal.
- **Open Issues**: Monitor for content correction requests (valuable), scope expansion requests (signals what gaps users identify), and engagement from unexpected user types (signals distribution has reached beyond targeted audience).
- **Pull Requests**: Any PR from an external contributor is a Stage 5 community engagement signal.

---

## Component 2: Social Media Monitoring Dashboard

### Platform Priority and Method

| Platform | Priority | Method | Frequency |
|----------|----------|--------|-----------|
| Mastodon | High | Manual search + infosec.exchange search | Weekly (Month 1), Monthly (thereafter) |
| Twitter/X | Medium | Search for Gist URL + key phrases | Weekly (Month 1), Monthly (thereafter) |
| LinkedIn | Medium | Company page monitoring for Tier 1-2 orgs | Monthly |
| Reddit | Low | Subreddit monitoring (r/privacy, r/netsec, r/immigration) | Monthly |

### Mastodon Monitoring

Search infosec.exchange and mastodon.social using these queries monthly:

- `palantir ELITE immigration`
- `data broker opt-out undocumented`
- `opsec immigration 2026`
- `[full Gist URL]`

Record any post that references the corpus or its core concepts in the social media log below.

### Twitter/X Monitoring

Use Twitter's advanced search (`site:x.com` in Google, or native advanced search) with:

- `"esca8peArtist" OR "palantir ELITE" immigration opsec`
- `"data broker" "undocumented" "opt-out" security`
- The Gist URL in quotes

### Social Media Mention Log Template

```
Date       | Platform   | Account               | Content Summary                  | Stage Signal | Action Taken
-----------+-----------+-----------------------+----------------------------------+-------------+-------------
[date]     | [platform] | [handle or page]      | [1-sentence description]         | [1-5]       | [reply, note, nothing]
```

### Organic Social Post (Optional — 90-Day Trigger)

If the 90-day gate shows the Gist view count is flat and no social mentions have been logged, consider publishing one public post on Mastodon (infosec.exchange) with the following structure:

> Thread: Primary-source documentation of Palantir ELITE's commercial data vendor architecture and what immigration-adjacent organizations can do about it. We built an OpSec playbook from FOIA contracts + public procurement records. Seeking technical critique and distribution to immigration legal networks.
>
> [Gist URL]
>
> #infosec #surveillance #privacy #immigration #palantir

Tag structure: lead with the technical audience (#infosec, #surveillance), follow with the policy audience (#immigration). Do not self-identify as the source organization or link to personal accounts unless you are comfortable with attribution.

---

## Component 3: Policy Database Search Strategy

### Overton.io Search Protocol

Overton indexes published policy documents, government reports, NGO publications, and think tank outputs in English. Run searches quarterly (May, August, November, February) using these queries:

**Primary queries**:
- `Palantir ELITE immigration enforcement`
- `commercial data broker immigration government`
- `operational security undocumented immigrants`

**Secondary queries** (after Tier 2 academic distribution):
- `data broker opt-out civil society guidance`
- `immigration surveillance countermeasures`

**What to log**: Any result from a known Tier 1-3 organization, any result with a date after the corpus launch date, any result that appears to reference concepts specific to this corpus (not just the general topic).

**Expected timeline for Overton results**: Policy citation lag is typically 6-18 months from distribution. Do not expect Overton results in the first 90 days. The first meaningful Overton results should appear in the August or November search if Tier 2 academic and digital rights distribution is working.

### Google Scholar Alert

Set a Google Scholar alert (scholar.google.com → Create alert) for:
- `"Palantir ELITE" immigration`
- `"data broker opt-out" undocumented`

Scholar alerts fire by email when new academic papers or preprints match the query. Response lag is 12-24 months for traditional academic publication. Preprints (arXiv, SSRN) may appear faster. Log all Scholar alert results in the policy impact column of the CSV tracker.

### Legal Filing Tracking

If the corpus is cited in a legal filing, amicus brief, or regulatory comment, this will typically surface through one of the following channels:

- A Tier 1 legal aid organization mentions the citation in a follow-up email
- A journalist covers the filing and mentions the corpus as a source
- Westlaw/PACER search for "Palantir ELITE" produces a result with the filing date after the corpus launch

This is a manual, low-frequency check. Add a quarterly calendar reminder to search PACER or CourtListener for "Palantir ELITE" immigration filings.

---

## Component 4: Quarterly Reporting Template

Produce a quarterly impact summary at 90 days, 180 days, and 12 months. The template below takes approximately 30 minutes to complete from the CSV tracker data.

### Quarterly Impact Summary Template

```
CYBERSECURITY-HARDENING CORPUS — IMPACT SUMMARY
Report Date: [DATE]
Period Covered: Launch through [DATE]
Prepared by: [NAME]

--- DISTRIBUTION SUMMARY ---
Tier 1 sends: [N]
Tier 2 sends: [N]
Tier 3 sends: [N]
Total: [N]

--- RESPONSE SUMMARY ---
Acknowledgment rate (Tier 1): [N]%  (target: 35%)
Stage 2+ adoption rate (Tier 1): [N]%  (target: 20% at 90 days)
Reply rate (Tier 2 digital rights): [N]%  (target: 20%)
Reply rate (Tier 2 academic): [N]%  (target: 10%)

--- CONVERSION SUMMARY ---
Organizations with Stage 3+ adoption: [N]
Organizations with Stage 4 (sustained): [N]
External citations logged: [N]
Case study interviews completed: [N]

--- CONTENT FEEDBACK ---
Most common gap identified: [text]
Most common friction point: [text]
Referrals generated (net new contacts): [N]

--- COMMUNITY SIGNALS ---
Gist total view count: [N]  (delta from last period: +[N])
Social media mentions: [N]
Overton citations: [N]
Google Scholar alerts: [N]

--- ASSESSMENT ---
Gate status: [PASS / BELOW TARGET / FAIL]
Primary risk: [text]
Recommended adjustments before next tier: [text]

--- ACTIONS BEFORE NEXT REPORT ---
1. [action]
2. [action]
3. [action]
```

### Reporting Schedule

| Report | Trigger Date | Audience | Purpose |
|--------|-------------|----------|---------|
| 90-day | ~August 2026 | Self / decision record | Tier 2 launch go/no-go |
| 180-day | ~November 2026 | Self / decision record | Tier 3 launch go/no-go; case study capture |
| 12-month | ~May 2027 | Self / potential external sharing | Full impact summary; September re-engagement planning |

---

*Dashboard spec complete. All components are designed for manual operation without paid tools. If distribution scales significantly (Tier 3 academic launch reaches 50+ organizations), consider upgrading to a paid Overton subscription and a dedicated mention monitoring tool (Mention.com or Brand24).*
