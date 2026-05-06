---
title: "Phase 2 Week 1 Success Metrics"
subtitle: "KPIs to track May 30 – June 6, decision thresholds, and Week 2 feature decisions"
date: 2026-05-06
status: production-ready
measurement-window: 2026-05-30 to 2026-06-06
references:
  - phase-2-post-launch-analytics-framework.md
  - customer-analytics.csv
  - TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md Step 8
  - TRACK_B_FINAL_EXECUTION_GUIDE.md Section 5
---

# Phase 2 Week 1 Success Metrics

**Purpose**: A specific, quantified measurement framework for Days 1-7 post-launch. Every metric has a source, a target, a minimum acceptable threshold, and an explicit action if the metric is below threshold. Pull data daily but act weekly — Day 7 is the decision gate for Week 2 content.

**Measurement window**: May 30 (launch) through June 6 (Day 7 full review)
**Decision output from Day 7 review**: Which 2-3 products to spotlight in Week 2; which content angle to lead with; whether to hold or accelerate the next Phase 2 push.

---

## Part 1: Daily Monitoring (Days 1-7)

Check the following every evening, 5-10 minutes. Log in customer-analytics.csv. Do not make strategic decisions from single-day data — you are building a trend line.

### Etsy Daily Metrics

| Metric | Where to Find | What It Means |
|---|---|---|
| Shop views today | Etsy Shop Manager > Stats > Today | How many buyers landed on any listing |
| Orders today | Etsy Shop Manager > Orders | Direct revenue signal |
| Listing views by product | Etsy Shop Manager > Stats > Listings | Which products Etsy's algorithm is surfacing |
| Favorites today | Etsy Shop Manager > Stats | Buying-intent signal (favorited = considering) |
| Revenue today | Etsy Shop Manager > Stats | Absolute revenue, Phase 2 period |

**Log format in customer-analytics.csv**:
```
Date, Etsy-Views, Etsy-Orders, Etsy-Revenue, Top-Listing-By-Views, Etsy-Favorites
```

---

### Kit Daily Metrics (Days 1-5)

| Metric | Where to Find | When to Check |
|---|---|---|
| New subscribers today | Kit > Subscribers > sorted by date | Evening |
| Email 1 open rate (running) | Kit > Automations > Seedwarden Welcome > Email 1 | Days 1-3 |
| Email 1 click rate (download) | Kit > Automations > Email 1 > Stats | Days 1-3 |
| Broadcast open rate (running total) | Kit > Broadcasts > [launch broadcast] > Stats | Days 1-2 |
| Broadcast click rate | Kit > Broadcasts > Stats | Days 1-2 |
| Subscribers with any cohort tag | Kit > Subscribers > filter by tag | Day 5+ (Email 3 delivers Day 5) |

**Note on broadcast open rate inflation**: Apple Mail Privacy Protection (MPP) auto-loads email images on Apple devices, recording an "open" even when the subscriber did not actually open the email. This artificially inflates open rates by 10-25%. A 50% open rate on Kit may represent a true open rate of 35-40%. The click rate is a more reliable engagement signal — it cannot be faked by MPP.

---

### Social Daily Metrics

| Metric | Where | Check Frequency |
|---|---|---|
| Instagram impressions | Instagram > Profile > Insights > Content | Daily |
| Instagram profile visits | Instagram Insights > Audience | Daily |
| TikTok views | TikTok > Analytics > Overview | Daily |
| New Kit sign-ups attributed to social | Kit > Subscribers > check by sign-up date vs. social post times | Daily |
| Pinterest impressions | Pinterest Analytics > Overview | Every 2 days (Pinterest data lags 24-48h) |

---

## Part 2: Day 7 Full Review — June 6

This is the weekly checkpoint. Block 30 minutes in the morning. Pull all metrics, compare to targets, make Week 2 decisions.

### Email Funnel — Week 1 Targets

| Metric | Target | Minimum Acceptable | If Below Minimum |
|---|---|---|---|
| Total subscribers (7-day) | 50+ | 20+ | Review: (1) Is Kit landing page URL in all 3 social bios? (2) Is the "Free Zone Card" offer visible in the bio copy itself (not just the link)? (3) Instagram bio character limit — does it have room for the CTA? |
| Email 1 open rate | 60%+ | 40%+ | Below 40%: email is landing in spam. Steps: (1) Check Kit > Settings > Email Settings — are SPF and DKIM both green? (2) Send a test from Kit to wanka95@gmail.com — does it land in inbox? (3) If DNS records are not yet propagated (check at mxtoolbox.com): wait 24-48h. |
| Email 1 download click rate | 40%+ | 25%+ | Below 25%: the download button is not visible enough. In Kit Email 1: increase button size to full-width, change button color to #143b28 (Deep Forest Green) with white text if not already set. |
| Email 3 open rate (Day 5 subscribers) | 40%+ | 25%+ | Email 3 is the inflection point — opens here predict Email 5 coupon redemption. Below 25%: review the Email 3 subject line. A story-based subject ("The seed saving mistake that cost me a whole harvest") typically outperforms generic subject lines. |
| Subscribers with cohort tags (seed-saver, city-grower, preservationist) | 20%+ of list | 10%+ of list | Low click-through on Emails 3 and 4. Make the tracked links larger and more prominent in those emails — the link should feel like a navigation element, not a footnote. |
| Email 5 coupon redemptions (Day 10+ subscribers only) | 8-15% of Email 5 recipients | Any redemption | Zero redemptions: (1) Confirm SEEDWARDEN15 coupon is active in Etsy > Marketing > Coupons. (2) Confirm the coupon code is spelled exactly "SEEDWARDEN15" in the email body. (3) Check if the Etsy listing URLs in Email 5 are correct (live listings, not draft). |

---

### Etsy — Week 1 Targets

| Metric | Target | Minimum Acceptable | If Below Minimum |
|---|---|---|---|
| Total shop views (7-day) | 200+ | 75+ | Below 75: SEO check on top 3 listings. (1) Does the listing title start with the primary keyword? (2) Are all 13 tags filled? (3) Is the listing description's first sentence benefit-focused? |
| Total orders (7-day) | 2+ | 1+ | Even 1 order = market validation. Zero orders after 7 days with 200+ views = conversion issue (see Listing Conversion Rate row). Zero orders with <75 views = traffic issue. |
| Listing conversion rate (orders/views) | 1.5-3% | 0.5%+ | Below 0.5%: review the listing's primary image (Slot 1 — still a mockup, not a lifestyle image) and the first 150 characters of the description. These are the two elements that drive click-through from search results. |
| New favorites (7-day) | 20+ | 5+ | Favorites are buying-intent signals. 20+ favorites with 0 orders often means price sensitivity — consider a limited-time 10% sale on the top-favorited products to convert "considering" into "purchased." |
| Top listing by views | Identify | Identify | The top-traffic listing reveals which audience segment Etsy's algorithm is most effectively routing to your store. This determines Week 2 content focus. |

---

### Social — Week 1 Targets

| Platform | Metric | Target | Minimum Acceptable | If Below Minimum |
|---|---|---|---|---|
| Instagram | Followers (7-day) | 150+ | 50+ | Below 50 after 7 days: review Day 1 Reel completion rate in Insights. Below 30% completion = the hook (first 3 seconds) is not working. Re-record with a stronger opening statement. |
| Instagram | Reach (7-day total) | 500+ | 150+ | Low reach = content is not being distributed by the algorithm. Increasing post frequency to 2 Reels per week for Week 2 typically increases algorithmic reach within 5-7 days. |
| TikTok | Followers (7-day) | 100+ | 30+ | Below 30: confirm the video was uploaded natively (not cross-posted from Instagram — TikTok suppresses cross-posted content). Re-upload natively if needed. |
| TikTok | Video views (first video) | 200+ | 50+ | Below 50 views on a natively uploaded video: TikTok's algorithm flagged the video for review (common with new accounts). Re-post the same video with a slightly different caption. |
| Pinterest | Monthly viewers (7-day reading) | 1,000+ | 200+ | Pinterest lags 2-3 weeks before significant view growth. If weekly views are below 200 after 14 days (not 7): increase pin frequency to 4-5 pins per day and verify Rich Pins are enabled. |
| All | Kit sign-ups from social (7-day) | 15+ | 5+ | Below 5 sign-ups from social: the bio link CTA is not visible enough. Add "Get your free zone card at the link below" as the first line of the Instagram bio (above the link). |

---

## Part 3: Week 2 Decisions — Made on June 6

Based on the Day 7 data, make these three decisions before closing the review session.

### Decision 1: Which Products to Feature in Week 2 Social

**Data source**: Etsy Shop Manager > Stats > Listings > sort by views (7-day)

**Framework**:
- **Top 2 products by views**: these are getting Etsy algorithmic traffic. Feature them in Instagram Reels (product spotlight format), TikTok videos, and Pinterest pins Week 2. The algorithm is already routing buyers to them — social reinforcement accelerates that.
- **If the top 2 products by views have 0 orders**: the traffic is real but the conversion is failing. Feature these products in social with a different angle — user benefit story, rather than product feature. Social for a non-converting product is a storytelling exercise, not a product promotion.
- **Top product by favorites (no order yet)**: add this product to Week 2 email newsletter as a "readers' choice" spotlight.

---

### Decision 2: Which Email Content Angle to Lead Week 2 Newsletter

**Data source**: Kit > Subscribers > filter by tag

| If Most Common Cohort Tag Is | Lead Week 2 Newsletter With |
|---|---|
| seed-saver | Seed saving content. Open with a tip about saving tomato seeds. Feature Seed Saving Field Manual and Heirloom Variety Guide. |
| city-grower | Apartment growing content. Open with a quick win for balcony or windowsill gardeners. Feature Container Growing Blueprint and Apartment Growing Guide. |
| preservationist | Harvest preservation content. Open with a fermentation tip. Feature Fermented Harvest Handbook and Harvest Preservation Field Manual. |
| No dominant tag (evenly distributed) | Mixed content with one tip from each category. End with a question: "What's your biggest challenge right now — growing, foraging, or preserving?" Use replies to refine future segmentation. |

---

### Decision 3: Hold or Accelerate the Phase 2 Push

**Framework**:

| Week 1 Outcome | Week 2 Strategy |
|---|---|
| 2+ orders, 50+ subscribers, Email 3 open rate 40%+ | Accelerate. Increase social posting to 5x/week Instagram, 4x/week TikTok. Double Pinterest pin production. Stage the next email broadcast (product spotlight) for Week 3. |
| 1 order, 20-50 subscribers, Email 3 open rate 25-40% | Hold steady. Continue current cadence. Test one new Instagram Reel format in Week 2 (behind-the-scenes or "unboxing" the physical print of the guide). Monitor Email 3 performance before changing email copy. |
| 0 orders, <20 subscribers, Email 3 open rate <25% | Diagnose before acting. Check spam placement for all emails. Check Etsy listing SEO on top 3 products. Check that the Kit landing page URL is live and correctly linked from all bios. Fix the technical blockers before increasing content volume. |

---

## Part 4: Data Logging Reference

### customer-analytics.csv — Column Reference

The file is at `projects/seedwarden/customer-analytics.csv`. Add a row for each day in the Phase 2 launch window.

**Required columns for Phase 2 launch week**:
```
Date
Etsy-Views-Today
Etsy-Orders-Today
Etsy-Revenue-Today (USD)
Kit-Subscribers-Total
Kit-New-Subscribers-Today
Kit-Email1-Open-Rate (%)
Kit-Email1-Click-Rate (%)
Kit-Broadcast-Open-Rate (%) [fill Days 1-3 only]
Kit-Broadcast-Click-Rate (%) [fill Days 1-3 only]
Instagram-Followers
TikTok-Followers
Pinterest-Monthly-Views
New-Signups-From-Social (estimated from timing of sign-ups vs. social posts)
Notes (anomalies, manual interventions, errors)
```

---

### WORKLOG.md — Phase 2 Launch Week Entries

Add a WORKLOG entry every evening for Days 1-7. Format:

```
## [Date] — Phase 2 Day [N]

**Etsy**: [views] views, [orders] orders, [revenue] revenue
**Kit**: [subscriber count] total, [N] new today, Email 1 open [%]
**Social**: Instagram [followers], TikTok [followers], Pinterest [monthly views]
**Anomalies**: [anything unexpected — orders, errors, social spikes, subscriber drop-offs]
**Manual actions taken**: [any fixes, manual email sends, platform reconnections]
**Tomorrow's priority**: [what you will do first the next morning]
```

---

## Part 5: Interpreting Metric Relationships

Understanding how metrics relate to each other prevents misreading the data.

**High Etsy views + zero orders**: The listing is getting traffic but failing to convert. Primary suspects: (1) the listing's first image (still a mockup instead of lifestyle, or the lifestyle image is unclear at thumbnail size), (2) the price, (3) the listing description's opening paragraph (buyer benefit not stated in the first 2 sentences).

**High email open rate + low click rate**: The subject line is working but the email body or CTA is not compelling. For Email 1: the download button must be large, clearly labeled, and above the fold on mobile. For Email 3: the seed saving story must feel personal and specific — generic educational content underperforms personal story content.

**High social impressions + zero email sign-ups**: The bio link is not being clicked. Instagram CTA may not be visible enough. Add "Free zone card — link below" as the very first line of the Instagram bio. If it is already there: the issue may be that followers are consuming content but not taking action (common in early audience-building). This resolves over time as the relationship deepens.

**Zero TikTok views on the first video**: TikTok occasionally holds new-account videos in a review queue before distributing them. Wait 24 hours and check again. If still 0 views after 24h: delete the video and re-upload natively with a slightly different caption — this resets the distribution queue.

**Kit subscriber count grows, Etsy orders don't follow**: Normal in Week 1. The welcome sequence runs for 10 days — most subscribers won't see the product offer (Email 5) until Day 10. Week 1 subscriber growth + zero orders is the expected pattern. Week 2 (when Day 10 subscribers start receiving Email 5) is the first real conversion signal.

---

## Part 6: When Week 1 is Below All Targets

If, at the Day 7 review, all metrics are below the minimum acceptable threshold, this is the diagnostic sequence:

**Step 1 — Spam check (30 min)**
Send a test email from Kit to wanka95@gmail.com and to a Gmail + a non-Gmail account (Yahoo, Outlook, Apple Mail). Check all three inboxes AND spam folders. If the email lands in spam on any provider: DNS authentication issue (SPF/DKIM). Verify both records are green in Kit Settings.

**Step 2 — Landing page accessibility check (10 min)**
Open the Kit landing page URL in an incognito window and on a phone. If the form does not load or the page shows an error: the landing page is down or the URL was updated by Kit. Re-copy the URL from Kit > Landing Pages, update all social bios.

**Step 3 — Etsy listing visibility check (15 min)**
Go to Etsy.com (logged out). Search for "seed saving guide" and "companion planting chart." Do any Seedwarden listings appear in the first 2 pages of results? If no: Phase 1 has not yet established enough listing history for Etsy to surface the products organically. This is normal for a new store — SEO builds over 30-60 days. Phase 2 social and email marketing are the primary channels while Etsy SEO matures.

**Step 4 — Social content audit (20 min)**
Open the most recent Instagram post and the most recent TikTok video. Do they have at least: a hook in the first 2-3 seconds or first sentence, a clear single topic, and a call to action in the caption? Generic "just launched" content underperforms specific tutorial or story content for this audience type.

**Step 5 — No further action needed this week**
After steps 1-4, stop. Do not change all systems simultaneously — that makes it impossible to attribute what worked. Pick the one most-likely broken element, fix it, and measure for 5 more days before changing anything else.

---

*Generated: 2026-05-06. References: phase-2-post-launch-analytics-framework.md (measurement architecture), TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md Step 8 (email metrics), TRACK_B_FINAL_EXECUTION_GUIDE.md Section 5 (checkpoints). This document covers May 30-June 6 only — Phase 3 metrics framework begins in PHASE3_ROADMAP_INDEX.md.*
