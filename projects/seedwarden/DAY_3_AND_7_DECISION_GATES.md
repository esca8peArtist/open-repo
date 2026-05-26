---
title: "Day 3 and Day 7 Decision Gates — Track B Post-Launch"
date: 2026-05-27
version: 1.0
session: 1691
status: production-ready
purpose: >
  Extends CONTINGENCY_DECISION_THRESHOLDS.md with operationalized Day 3 and
  Day 7 gates including aggregate metric collection, immediate-action triggers,
  and Phase 3 go/no-go framework. Adds Day 14 early-win identification. Designed
  to be completed in 15 minutes per checkpoint without requiring a Claude session.
references:
  - CONTINGENCY_DECISION_THRESHOLDS.md (Day 3/7/14 numerical thresholds — primary doc)
  - TRACK_B_LAUNCH_MONITORING_CHECKPOINTS.md (checkpoint decision trees)
  - TRACK_B_LAUNCH_DAY_RUNBOOK.md (Day 0 metrics snapshot format)
  - CONTINGENCY_DECISION_PLAYBOOK.md (failure scenario responses)
  - TRACK_B_SOCIAL_CALENDAR_MAY28_30.md (June 1–7 content calendar)
  - INFLUENCER_STAGING_VERIFICATION.md (influencer response tracking)
---

# Day 3 and Day 7 Decision Gates
## Track B Zone Cards — Post-Launch Checkpoint Framework

**Extension of**: `CONTINGENCY_DECISION_THRESHOLDS.md` (Day 3/7/14 thresholds). This document adds the operational layer: how to collect the metrics, what to do in each scenario, and how to execute the resulting decisions.

**Launch date**: May 30, 2026
**Day 3 gate**: June 2, 2026 at 08:00 UTC
**Day 7 gate**: June 6, 2026 at 08:00 UTC
**Day 14 gate**: June 13, 2026 at 08:00 UTC

**Time to complete each gate**: 15–20 minutes

---

## Day 3 Gate — June 2, 2026 at 08:00 UTC

### Step 1: Collect Aggregate Metrics (5 minutes)

Open each platform and record the numbers below. These are cumulative totals since launch (May 30 08:00 UTC through June 2 08:00 UTC — 72 hours).

```
Day 3 Metric Snapshot — June 2, 2026 08:00 UTC

DISTRIBUTION (cumulative 72 hours)
Gist views (cumulative): ___
  -- Day 0 (May 30): ___
  -- Day 1 (May 31): ___
  -- Day 2 (June 1): ___
Reddit r/herbalism upvotes: ___
Reddit r/herbalism comments: ___
Reddit additional communities upvotes (if posted elsewhere): ___
Instagram reach (cumulative, all posts): ___
Instagram new followers: ___
TikTok views (cumulative): ___
Pinterest saves: ___
Bitly clicks (if tracking): ___
Kit new subscribers (via landing page): ___

INFLUENCER ENGAGEMENT
Contacts reached (total DMs + emails sent): ___ of 15
Contacts who responded (any response): ___
Contacts who confirmed sharing: ___
Contacts who shared publicly (newsletter, social post, community post): ___
Organic shares by third parties (not the 15 contacts): ___

CUSTOMER ENGAGEMENT
Total DM / email inquiries received: ___
Total comments responded to: ___
Any notable qualitative feedback:
[notes here]

REVENUE
Etsy listing status: Active / Draft / Not started
Etsy listing impressions: ___
Etsy listing views: ___
Etsy sales: ___
```

---

### Step 2: Run the Day 3 Decision Matrix (5 minutes)

Compare your Gist views and Reddit upvotes against the thresholds from `CONTINGENCY_DECISION_THRESHOLDS.md`:

| Metric | Your number | RED (<) | YELLOW | GREEN (>) |
|--------|-------------|---------|--------|-----------|
| Gist views (72h) | ___ | < 30 | 30–70 | > 70 |
| Reddit upvotes (total) | ___ | < 10 | 10–25 | > 25 |

**Mark your Day 3 status**: GREEN / YELLOW / RED

---

### Step 3: Day 3 Decision — Track A Holdout Influencer Activation

The primary Day 3 decision is whether to activate the Track A holdout influencer cohort. From `CONTINGENCY_DECISION_THRESHOLDS.md`:

**GREEN (Gist > 70, Reddit > 25)**:
Activate Track A holdout influencers now.

The Track A holdout cohort is a subset of influencer contacts who were not approached during May 28–30 pre-launch outreach because their audience fit better with a paid product framing than a free resource. With strong Day 3 signals, the free product has proven its distribution strength — introducing a paid or affiliate angle to these contacts is now viable.

Activation script (send to holdout contacts by June 2 end of day):

Subject: Zone cards are getting traction — would you be open to an affiliate arrangement?

```
Hi [NAME],

The Seedwarden Zone Quick-Start Cards launched last Friday and have been
getting strong early response — [X] downloads in the first 3 days.

I wanted to reach out because I think your audience would respond well,
and I'd like to offer an affiliate arrangement rather than just sharing
the free link. Terms:

- 15–25% commission on any sales from your link
- If we move to a paid Etsy bundle (planned for June), your link
  carries into that as well
- No timeline pressure — if this isn't the right fit right now,
  no problem

Free PDF preview available if you'd like to review before deciding.

Best,
[YOUR_NAME]
Seedwarden
```

---

**YELLOW (Gist 30–70, Reddit 10–25)**:
Track B is functioning but not at breakthrough pace. Optional activation of 1–2 Track A holdout contacts who are easiest to reach (email address already drafted, clear audience match). Do not activate the full holdout cohort yet — wait for Day 7 data.

Action: Identify the 1–2 easiest holdout contacts and send the affiliate activation email above. For all others, hold until June 6.

---

**RED (Gist < 30, Reddit < 10)**:
Do not activate Track A holdouts. Diagnose the Track B distribution gap first.

Immediate-action triggers (execute before Day 7):

**A: Were outreach emails sent?** (30-second check)
Look in your email sent folder. Were the May 28 influencer emails sent? If not, send all Tier 1 and Tier 2 contacts today. This is the most common cause of low Day 3 traction.

**B: Audit the distribution URL** (2 minutes)
Open the Gist URL in an incognito window. Is it accessible? Is the correct URL in all social bios? Check each platform's bio link. A broken or missing URL is the second most common cause of low Gist views.

**C: Reddit post check** (2 minutes)
Check whether the Reddit posts were removed by moderators. Navigate to your Reddit profile > Posts submitted. If any are missing, they were removed. Post in r/foraging (750K+ members) using the image post format: upload Zone 5 card image as a PNG instead of a link. Image posts bypass most subreddit promotional filters.

**D: If all channels were correctly executed and traffic is still below 30 views**: This is not a failure — it is a data point. New accounts with zero prior audience often see 10–30 Gist views in the first 72 hours from organic search and direct outreach alone. Do not panic. The Day 7 checkpoint has more meaningful data.

---

### Step 4: Secondary Day 3 Decision — Reddit Strategy Adjustment

From `CONTINGENCY_DECISION_THRESHOLDS.md`:

| Reddit result | Decision |
|--------------|---------|
| Total upvotes > 20 | Continue current Reddit strategy. Post June 3 "Native Plants / AHG crossover" content as planned in social calendar. |
| Total upvotes < 20, posts still live | Convert next Reddit post to image format: upload Zone 5 or Zone 7 card as a PNG image post. Image posts bypass promotional filters and accumulate upvotes faster than link posts. |
| Post removed by mods | Do not repost same content. Post in r/foraging or r/homesteading with personal framing: "I built this for my zone — wanted to share." |
| Zero activity (0 upvotes, 0 comments) | Post was likely shadow-filtered. Message mod team with pre-approved educational framing from `HERBALIST_PARTNERSHIP_EMAIL_TEMPLATE.md` Template E. Ask for explicit mod approval before next post. |

---

### Step 5: Log Day 3 Status (2 minutes)

Record in the tracking log:
- Day 3 status: GREEN / YELLOW / RED
- Gist views (72h): ___
- Reddit upvotes: ___
- Influencer contacts confirmed sharing: ___
- Track A holdout decision: Activated / Optional 1–2 / Hold
- Reddit strategy adjustment: No change / Image post format / New community
- Any qualitative observations (1–3 sentences):

---

## Day 7 Gate — June 6, 2026 at 08:00 UTC

### Step 1: Collect Aggregate Metrics (7 minutes)

Cumulative totals for the full first week (May 30 – June 6, 168 hours):

```
Day 7 Metric Snapshot — June 6, 2026 08:00 UTC

DISTRIBUTION (cumulative 7 days)
Gist views (cumulative): ___
Reddit upvotes total (all posts, all communities): ___
Reddit comments total: ___
Instagram reach (total, all posts since launch): ___
Instagram followers gained (launch day to today): ___
TikTok views (total, all videos): ___
Pinterest saves (total): ___
Kit subscribers (total, since launch): ___

INFLUENCER ENGAGEMENT
Confirmed shares by influencer contacts: ___
Organic shares by third parties: ___
Affiliate interest expressed: ___
Follow-up response needed for: ___ contacts

CUSTOMER ENGAGEMENT
Total inquiries received (7 days): ___
Average response time: ___
Common question themes:
  1. ___
  2. ___
  3. ___

REVENUE
Etsy listing status: Active / Draft / Not started
Etsy impressions (7-day): ___
Etsy views (7-day): ___
Etsy impression-to-view ratio: ___%  (views ÷ impressions × 100)
Etsy sales: ___
Total revenue to date: $___
```

---

### Step 2: Run the Day 7 Decision Matrix (5 minutes)

From `CONTINGENCY_DECISION_THRESHOLDS.md`:

| Metric | Your number | RED | YELLOW | GREEN |
|--------|-------------|-----|--------|-------|
| Gist views (7-day) | ___ | < 100 | 100–200 | > 200 |
| Reddit upvotes | ___ | < 25 | 25–50 | > 50 |
| Instagram reach (total) | ___ | < 200 | 200–500 | > 500 |
| Organic shares by others | ___ | 0 | 1–2 | 3+ |

**Mark your Day 7 status**: GREEN / YELLOW / RED

---

### Step 3: Day 7 Primary Decision — Phase Scope

**GREEN (Full success: Gist > 200, Reddit > 50, Instagram > 500, shares 3+)**:

Phase 2 scope expansion. Execute in this order:

1. **Build the Etsy paid bundle listing** (target: complete by June 9):
   - Product: all 8 zone cards + cover page + zone-selection guide ("which zone am I in?" one-pager)
   - Suggested price: $5–9
   - Bonus content for paid version: seasonal planting calendar (this differentiates paid from free Gist)
   - List title: "Seedwarden Zone Quick-Start Card Bundle — All 8 USDA Zones"

2. **Add email capture to the landing page** (2-hour action):
   - Kit landing page already exists. Ensure the subscribe form is prominently placed and the CTA says "Get Your Zone Card + Updates."
   - The organic sharing momentum means email capture is now worth the setup friction.

3. **Begin Phase 2 content wave** (start June 9–13):
   - Zone-specific deep-dive posts: one post per zone, covering the top 3 medicinal herbs for that zone. 8 posts total over 2 weeks.
   - This is distinct from the June 1–7 calendar already planned in `TRACK_B_SOCIAL_CALENDAR_MAY28_30.md`.

4. **Activate affiliate partnerships** for the 2–3 highest-engagement influencer contacts:
   - Prioritize contacts with newsletters (Sabrena Gwin / AHG route, John Gallagher / LearningHerbs) because newsletter mentions produce sustained click traffic rather than single-day spikes.
   - Use the affiliate activation script from Day 3 Gate Step 3 if not yet sent.

---

**YELLOW (Moderate: Gist 100–200, Reddit 25–50, Instagram 200–500, shares 1–2)**:

Maintain current cadence with minor adjustments.

1. Continue June 1–7 social calendar as planned (no changes to content or posting frequency).
2. Build Etsy listing on relaxed timeline: target June 13 (not June 9). Moderate response still validates the paid bundle.
3. Send one follow-up to the 2–3 highest-engagement influencer contacts. Subject: "Quick follow-up — zone cards got [X] downloads in week 1, thought you might like to know."
4. Do not activate paid promotion yet. The Day 14 checkpoint will have a more meaningful baseline.
5. Influencer channel secondary assessment: which contacts responded? Log in `TRACK_B_HERBALIST_OUTREACH_MATRIX.md`.

---

**RED (Low response: Gist < 100, Reddit < 25, Instagram < 200, shares 0)**:

Rapid-response adjustment before investing further. Do not start Phase 2 scope expansion.

Diagnose distribution gap first (15 minutes):

| Hypothesis | Check | If true — action |
|------------|-------|-----------------|
| Reddit posts were removed or filtered | Check Reddit profile > submitted posts for removal notices | Repost as image posts with personal framing. Try r/foraging. |
| Gist URL was not in social posts | Check actual published post captions for the URL | Edit captions. Add new Story with corrected link. |
| Instagram reach is low because account is new | Check Instagram account age and follower count | Expected for new accounts. Not a failure. Continue. |
| Outreach emails were not sent | Check email sent folder | Send immediately — highest priority action. |
| Gist is not the right distribution format | Views proportionally low across all platforms | Consider Gumroad or Etsy free listing as alternate distribution. |

Rapid-response actions in priority order:
1. If outreach emails not sent: send all Tier 1 and Tier 2 contacts immediately.
2. If Reddit distribution failed: post in r/foraging (750K+ members, not yet reached if r/vegetablegardening was primary) with image post format.
3. If social posts had placeholder URL: correct immediately. Add Instagram Story with corrected link.
4. If all above were correctly executed: do not panic. Proceed with June 1–7 calendar. Day 14 will have a more meaningful baseline.

---

### Step 4: Day 7 Secondary Decision — Influencer Channel Assessment

Classify each of the 15 contacts by response type. Record in `TRACK_B_HERBALIST_OUTREACH_MATRIX.md`.

| Response type | Count target | What it means for Phase 3 |
|--------------|-------------|--------------------------|
| No response | < 10 of 15 | Expected; most outreach at this scale has 30–50% no-response |
| Positive reply (not yet shared) | 2–5 | Pipeline for June partnerships; follow up once |
| Shared publicly (social, newsletter, community) | 1–3 | Highest-value response; thank publicly; prioritize for Phase 3 |
| Expressed affiliate interest | 1–2 | Schedule brief follow-up to confirm terms |
| Asked for more info | 1–3 | Respond with specific assets (PDF preview, affiliate terms, zone brief) |

**Phase 3 influencer strategy decision**:
- If 3+ shared publicly by Day 7: influencer channel is the primary distribution lever for Phase 3. Expand the contact list for medicinal herbs launch.
- If fewer than 3 shared publicly: organic Reddit and Pinterest search are likely stronger distribution channels for this product type. De-prioritize influencer outreach budget for Phase 3.

---

### Step 5: Log Day 7 Status (3 minutes)

Record in the tracking log:
- Day 7 status: GREEN / YELLOW / RED
- Gist views (7-day cumulative): ___
- Reddit upvotes total: ___
- Instagram total reach: ___
- Organic shares: ___
- Phase 2 scope decision: Expand / Maintain / Adjust
- Etsy listing target date: ___
- Influencer channel verdict: Primary / Secondary / De-prioritize for Phase 3
- Primary driver of this week's traffic (1–2 sentences):

---

## Day 14 Gate — June 13, 2026 at 08:00 UTC

### Purpose

The Day 14 gate answers four questions:
1. Does the two-week baseline support Phase 3 investment?
2. Which zone, email, influencer, and platform performed best?
3. Is there any early-win that should be amplified before Phase 3?
4. What does Phase 3 (medicinal herbs) scope and timing look like?

This gate is covered in detail in `CONTINGENCY_DECISION_THRESHOLDS.md` and `TRACK_B_LAUNCH_MONITORING_CHECKPOINTS.md`. The section below adds the early-win identification layer.

---

### Early-Win Identification (Day 14)

After 14 days of data, identify the single best performer in each category. This is the template for Phase 3.

**Highest-performing zone (visitor-to-engagement conversion)**:

At Day 14, check which zone card generated the most:
- Direct requests via DM or email ("Can I get the Zone X card?")
- Social mentions referencing a specific zone
- Influencer content citing a specific zone

This is your anchor zone for Phase 3 content. The top-performing zone should be featured first in the medicinal herbs launch content.

How to check: Search Instagram DMs, email inbox, and Reddit comments for zone number mentions. Tally counts per zone. The top zone is the lead product for Phase 3.

**Best email subject line**:

If Kit automation data is available (opens by email number): compare open rates across the 5-email welcome sequence. If you sent any broadcast emails during the week: compare open rates.

At Day 14, the email with the highest open rate is the format template for Phase 3 herbalist outreach. Note the subject line and the characteristic that made it work (curiosity gap, zone-specificity, personal tone).

**Best influencer contact**:

From the influencer response log in `TRACK_B_HERBALIST_OUTREACH_MATRIX.md`, identify which single contact:
- Generated the most downstream traffic (Bitly clicks or Gist views spiking after their share)
- Had the highest response quality (newsletter mention, social post, community post — not just a DM reply)
- Showed most enthusiasm for the product

This is your Phase 3 anchor contact. Reach out to them first when preparing the medicinal herbs launch outreach.

**Best platform (algorithmic feedback)**:

Compare cumulative reach per platform per post:
- Instagram: total reach ÷ number of posts
- TikTok: total views ÷ number of videos
- Pinterest: total saves ÷ number of pins
- Reddit: total upvotes ÷ number of posts

The platform with the highest per-post metric is where Phase 3 content investment should concentrate.

---

### Phase 3 Go/No-Go Scorecard (Day 14)

From `CONTINGENCY_DECISION_THRESHOLDS.md`:

| Date | Checkpoint | Gist views | Green | Yellow | Red |
|------|-----------|------------|-------|--------|-----|
| June 13 | Day 14 | Cumulative | > 400 | 150–400 | < 150 |
| June 13 | Day 14 | Reddit upvotes | > 100 | 50–100 | < 50 |
| June 13 | Day 14 | Instagram reach | > 1,000 | 500–1,000 | < 500 |
| June 13 | Day 14 | Phase 3 decision | Green-lit | Proceed with adjustment | Diagnose before investing |

**GREEN (Gist > 400)**: Phase 3 medicinal herbs launch is green-lit. Begin June 22 sprint with confidence that the Zone Card format has a proven audience. Consider a social media growth sprint: $20–50 paid test on Instagram or Pinterest, targeting gardening and homesteading interests.

**YELLOW (Gist 150–400)**: Phase 3 proceeds at baseline scope. Build the paid Etsy bundle listing first. Set price at $5–9 for all 8 cards with a cover page and zone-selection guide. Etsy listing is the proof of revenue viability before Phase 3 investment.

**RED (Gist < 150)**: Diagnose distribution gap before Phase 3 investment. Do not start medicinal herbs content production until you understand why Zone Cards underperformed. Hypotheses: (a) Gist is not the right distribution channel — test Etsy free listing or Gumroad; (b) "Zone Quick-Start Cards" is not the most searchable phrase — test alternate SEO framing; (c) outreach targeting was off — review which communities had the highest engagement rate and replicate for Phase 3.

---

### Day 14 Log Template

```
Day 14 (June 13) Gate — logged [TIME] UTC

CUMULATIVE 14-DAY TOTALS
Gist views: ___
Reddit upvotes total: ___
Instagram total reach: ___
TikTok total views: ___
Pinterest total saves: ___
Kit total subscribers: ___

EARLY-WIN IDENTIFICATION
Best zone (most requested / mentioned): Zone ___
Best email subject line: ___
  Open rate: ___%
Best influencer contact: ___
  Traffic generated (downstream clicks / views): ___
Best platform (per-post average reach): ___
  Per-post metric: ___

PHASE 3 DECISION
Day 14 status: GREEN / YELLOW / RED
Phase 3 go/no-go: Green-lit / Proceed with adjustment / Diagnose first
Phase 3 anchor zone (top-performing zone): Zone ___
Phase 3 anchor contact: ___
Etsy paid bundle status: Live / Build by [date] / Hold
Paid promotion decision: Yes ($20–50 test) / No / Revisit at Day 21

QUALITATIVE OBSERVATIONS
What worked better than expected (1–2 sentences): ___
What worked worse than expected (1–2 sentences): ___
What single action would most improve results if done again: ___
```

---

## Threshold Quick Reference (All Three Gates)

Sourced from `CONTINGENCY_DECISION_THRESHOLDS.md`. Consolidated here for single-document review.

| Date | Gate | Metric | RED | YELLOW | GREEN |
|------|------|--------|-----|--------|-------|
| June 2 | Day 3 | Gist views (72h) | < 30 | 30–70 | > 70 |
| June 2 | Day 3 | Reddit upvotes | < 10 | 10–25 | > 25 |
| June 2 | Day 3 | Track A holdout decision | Hold | Optional 1–2 | Activate |
| June 6 | Day 7 | Gist views (7-day) | < 100 | 100–200 | > 200 |
| June 6 | Day 7 | Reddit upvotes | < 25 | 25–50 | > 50 |
| June 6 | Day 7 | Instagram reach | < 200 | 200–500 | > 500 |
| June 6 | Day 7 | Organic shares | 0 | 1–2 | 3+ |
| June 6 | Day 7 | Phase 2 scope | Adjust | Maintain | Expand |
| June 13 | Day 14 | Gist views (14-day) | < 150 | 150–400 | > 400 |
| June 13 | Day 14 | Reddit upvotes | < 50 | 50–100 | > 100 |
| June 13 | Day 14 | Instagram reach (total) | < 500 | 500–1,000 | > 1,000 |
| June 13 | Day 14 | Phase 3 decision | Diagnose | Proceed adjusted | Green-lit |

---

*Document version: 1.0 — May 27, 2026, Session 1691*
*Extends: CONTINGENCY_DECISION_THRESHOLDS.md (adds Day 3/7/14 operational layer — metric collection, decision steps, early-win identification)*
*Companion documents: TRACK_B_LAUNCH_DAY_RUNBOOK.md, CONTINGENCY_DECISION_PLAYBOOK.md, TRACK_B_LAUNCH_MONITORING_CHECKPOINTS.md, TRACK_B_HERBALIST_OUTREACH_MATRIX.md, TRACK_B_SOCIAL_CALENDAR_MAY28_30.md*
