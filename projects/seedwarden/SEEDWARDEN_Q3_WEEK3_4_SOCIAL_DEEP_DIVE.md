---
title: "Seedwarden Q3 Week 3-4 Social Engagement Deep-Dive Framework"
date: 2026-07-13
version: 1.0
status: production-ready
sprint-window: July 13 – July 27, 2026
scope: "Per-platform social engagement monitoring (LinkedIn, Instagram, YouTube) with algorithm risk detection, escalation rules, and content-type pivot triggers"
cross-references:
  - SEEDWARDEN_Q3_SOCIAL_ENGAGEMENT_TRACKING.md (Week 1-2 aggregate baseline)
  - SEEDWARDEN_Q3_WEEK3_4_DAILY_OPS_CHECKLIST.md (daily launch execution)
  - SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md (all-platform RED trigger)
---

# Seedwarden Q3 Week 3-4 Social Engagement Deep-Dive Framework

**Purpose**: Per-platform monitoring of LinkedIn, Instagram, and YouTube during Week 3-4 peak execution (Jul 13-27). Replaces aggregate-only tracking from Week 1-2 with platform-specific thresholds, algorithm risk signals, and automated escalation rules.

**Week 3-4 baseline**: Week 3-4 baseline is derived from Week 1-2 average performance. If Week 1-2 data is not yet available at document activation, use the initial baseline assumptions from SEEDWARDEN_Q3_SOCIAL_ENGAGEMENT_TRACKING.md (Section 3) as the proxy.

**Baseline proxy values (if Week 1-2 data unavailable)**:
- LinkedIn engagement: 6-12% educational, 3-5% promotional, 10-15% testimonial
- Instagram engagement: 3-6% educational, 1.5-3% promotional
- YouTube comment rate: 10-30 comments per question post

---

## Section 1: Per-Platform Daily Tracking Templates

### 1.1 LinkedIn Daily Log

Run at T+24hr after each post (not same-day — engagement develops for 24-48 hours).

| Field | Value | Source |
|-------|-------|--------|
| Post date | YYYY-MM-DD | Calendar |
| Post title (first 50 chars) | [copy from post] | LinkedIn |
| Content type | Educational / Testimonial / Promotional | Manual |
| Likes | [#] | LinkedIn Analytics |
| Comments | [#] | LinkedIn Analytics |
| Shares | [#] | LinkedIn Analytics |
| Saves | [#] | LinkedIn post menu |
| Profile visits (post-linked) | [#] | LinkedIn Analytics > Visitors |
| Current follower count | [#] | LinkedIn Analytics |
| Engagement rate | (Likes + Comments + Shares) / Followers × 100 = [%] | Calculated |
| DM count received (this day) | [#] | LinkedIn Messages |
| Status | GREEN >8% / YELLOW 5-8% / RED <5% | Applied |

**Weekly DM baseline tracking**:
```
Week 1-2 avg DMs/day: [#] (establish from Week 1-2 actuals)
Week 3 DM daily counts:
  Jul 13: [#] | Jul 14: [#] | Jul 15: [#] | Jul 16: [#] | Jul 17: [#] | Jul 18: [#] | Jul 19: [#]
Week 3 avg DMs/day: [calculated]

Week 4 DM daily counts:
  Jul 20: [#] | Jul 21: [#] | Jul 22: [#] | Jul 23: [#] | Jul 24: [#] | Jul 25: [#] | Jul 26: [#] | Jul 27: [#]
Week 4 avg DMs/day: [calculated]
```

---

### 1.2 Instagram Daily Log

Run at T+48hr after each post (Instagram's algorithm distributes engagement over a longer window than LinkedIn).

| Field | Value | Source |
|-------|-------|--------|
| Post date | YYYY-MM-DD | Calendar |
| Caption snippet (first 50 chars) | [copy] | Instagram |
| Content type | Educational / Testimonial / Promotional | Manual |
| Likes | [#] | Instagram Insights |
| Comments | [#] | Instagram Insights |
| Saves | [#] | Instagram Insights (star icon count) |
| Shares/Sends | [#] | Instagram Insights |
| Reach | [#] | Instagram Insights |
| Impressions | [#] | Instagram Insights |
| Profile visits (from this post) | [#] | Instagram Insights |
| Follower change (day) | +/- [#] | Instagram Analytics |
| Engagement rate | (Likes + Comments + Saves) / Reach × 100 = [%] | Calculated |
| Spam/bot comment signals | [None / Suspect: ___] | Manual review |
| Status | GREEN >5% / YELLOW 3-5% / RED <3% | Applied |

**Instagram engagement rate thresholds** (different from LinkedIn):
- GREEN: >5% engagement rate (Instagram audience is more visual; benchmarks are lower)
- YELLOW: 3-5% engagement rate
- RED: <3% engagement rate

**Note on calculation**: Use REACH (not followers) as denominator for Instagram. Instagram's algorithm controls distribution, so reach is a more accurate measure of post performance than total follower count.

---

### 1.3 YouTube Community Tab Daily Log

Run within 72 hours of post (YouTube Community posts have longer engagement windows — comments come in over 2-5 days).

| Field | Value | Source |
|-------|-------|--------|
| Post date | YYYY-MM-DD | Calendar |
| Question text (full) | [copy from post] | YouTube Studio |
| Post type | Question / Poll / Information | Manual |
| Comments (total) | [#] | YouTube Studio |
| Comment quality | Short (1-2 words) / Medium (1 sentence) / Long (2+ sentences) | Manual review |
| Likes on post | [#] | YouTube Studio |
| Subscriber gain (from post) | [#] | YouTube Studio > Subscribers > source |
| Recommended traffic triggered? | Yes / No (check by Day 3 after post) | YouTube Analytics |
| Status | GREEN >10 long-form comments / YELLOW 5-10 / RED <5 | Applied |

**YouTube engagement definitions**:
- GREEN: 10+ substantive comments (2+ sentences each) within 72 hours
- YELLOW: 5-9 comments within 72 hours, or 10+ but mostly 1-2 word replies
- RED: fewer than 5 comments within 72 hours
- Recommended traffic signal: YouTube Analytics > Traffic Source > "Browse features" or "Suggested" appearing within 72 hours = algorithm pick-up signal

---

## Section 2: Algorithm Risk Detection — LinkedIn

### 2.1 LinkedIn Engagement Rate Thresholds

LinkedIn's organic distribution suppresses posts with <5% engagement within the first 24 hours. Algorithm signals for Week 3-4:

| Metric | GREEN | YELLOW | RED | Action |
|--------|-------|--------|-----|--------|
| Engagement rate (24hr) | >8% | 5-8% | <5% | See escalation rules Section 3 |
| Comments (24hr) | >10 comments | 5-10 comments | <5 comments | Comments outweigh likes; prioritize comment generation |
| Profile visit spike | >200 visits/post | 100-200 | <100 | Low spike = post not driving profile discovery |
| Shares (24hr) | >5 shares | 2-5 shares | <2 shares | Shares indicate network amplification value |
| Viral coefficient | >0.30 | 0.15-0.30 | <0.15 | (Shares + Saves) / Likes |

### 2.2 LinkedIn DM Surge Detection (Profile Flag Risk)

Unusually high DM volume following posts can indicate LinkedIn is flagging the account as "spam-adjacent" or that a post went viral. Both cases require different responses.

**Baseline**: Week 1-2 average DMs/day (establish from actuals; proxy if unavailable: 2-5 DMs/day).

**Surge threshold**: >10 DMs/day vs. baseline = potential profile flag signal.

**Detection protocol**:
```
Daily at 22:00 UTC:
  1. Count LinkedIn DMs received in last 24 hours
  2. Compare to Week 1-2 daily average
  3. Apply threshold:

IF DMs <10/day (and <2× baseline):
  → Normal range. Log count and close.

IF DMs 10-20/day (OR 2-4× baseline):
  → YELLOW — DM surge signal
  Step 1: Review DM content — are they spam/bot? Legitimate inquiries? Partnership requests?
    - If >50% are clearly spam/bot: LinkedIn may have amplified your profile to bot accounts
      → Do not engage with bot DMs; mark as spam
      → Monitor next 2 days; if continues, slow down posting frequency (reduce to 1 post/week)
    - If >50% are legitimate: your content went "semi-viral" and practitioners/buyers are reaching out
      → Respond to legitimate DMs; this is a GOOD signal
      → Continue normal posting schedule

IF DMs >20/day (OR >4× baseline):
  → RED — possible profile flag or viral content moment
  Step 1: Check if a specific post is driving DM surge (check which post has unusually high reach)
  Step 2: If viral content (post reach 5× normal): this is a positive signal; engage, repost, pin to profile
  Step 3: If no specific post and DMs are mostly unsolicited: potential LinkedIn flag
    → Pause posting for 48 hours
    → Review LinkedIn account status (no notifications of restriction?)
    → Restart posting at 1 post/week for 2 weeks, then return to normal cadence
  Step 4: Log all actions in PHASE_3_EXECUTION_LOG.md with dates
```

### 2.3 LinkedIn Hashtag Performance Tracking

Week 3-4 hashtag monitoring (check weekly via LinkedIn Analytics > Posts):

**Hashtags in active rotation (Jul 13-27)**:
- Tier 1 (always): `#seedwarden`
- Tier 2 (rotate 2-3 per post): `#herbalism`, `#medicinalherbs`, `#herbgarden`, `#plantscience`
- Tier 3 (bundle-specific): `#sleep`, `#immunity`, `#nervines`, `#immunesupport`

**Hashtag performance tracking table** (update weekly):

| Hashtag | Posts Used In (W3-4) | Total Impressions via Hashtag | Avg Engagement on Posts Using This Tag | Status |
|---------|---------------------|-------------------------------|----------------------------------------|--------|
| #seedwarden | [#] | [#] | [%] | — |
| #herbalism | [#] | [#] | [%] | — |
| #medicinalherbs | [#] | [#] | [%] | — |
| #herbgarden | [#] | [#] | [%] | — |
| #plantscience | [#] | [#] | [%] | — |
| #sleep | [#] | [#] | [%] | — |
| #immunity | [#] | [#] | [%] | — |

**Hashtag underperformance rule**: If any Tier 2 hashtag has <500 impressions across 3+ posts using it, swap it out. Rotate in: `#botanicals`, `#herbeducation`, `#foraging`, or `#harvest`.

### 2.4 LinkedIn Engagement Cliff Detection

An engagement cliff is a sudden 30%+ drop in engagement rate between consecutive similar posts (same content type, same time slot).

**Calculation**:
```
Post N engagement rate: [%]
Post N+1 engagement rate: [%]
Change: ([N+1] - [N]) / [N] × 100 = [%] change

IF change is -30% or worse (e.g., 10% → 6.5%):
  → ENGAGEMENT CLIFF DETECTED
  Action: See Section 3.3 escalation rules
```

**Cliff detection log** (check weekly):
```
Week 3 consecutive post comparison (same content type):
  Post A (Educational, Jul [date]): [%] engagement
  Post B (Educational, Jul [date]): [%] engagement
  Change: [%]
  Cliff: Yes / No

Week 4 consecutive post comparison:
  Post A: [%] engagement
  Post B: [%] engagement
  Change: [%]
  Cliff: Yes / No
```

---

## Section 3: Algorithm Risk Detection — Instagram

### 3.1 Instagram Engagement Rate Trending

**Week 3-4 baseline** = Week 1-2 average engagement rate (by content type).

| Metric | GREEN | YELLOW | RED | Threshold definition |
|--------|-------|--------|-----|---------------------|
| Engagement rate (vs. W1-2 baseline) | ≥95% of baseline | <95% of baseline | <85% of baseline | "Baseline" = Week 1-2 avg for same content type |
| Saves (by content type) | Educational: >20 saves | 10-20 saves | <10 saves | Saves = highest Instagram value signal |
| Follower gain per post | >5 per post | 2-5 per post | <2 per post | Gaining fewer followers per post = declining reach |
| Comment quality | Mostly genuine | Mixed (some short) | Mostly short/generic | Spam/bot comments = account at risk of suppression |

**Engagement rate trending protocol**:
```
At end of each week (Friday 22:00 UTC):
  1. Calculate Week 3-4 avg Instagram engagement rate per content type
  2. Compare to Week 1-2 avg for same content type
  3. Apply threshold:

IF Week 3-4 rate ≥95% of Week 1-2 rate:
  → GREEN. No action. Continue current content strategy.

IF Week 3-4 rate <95% but ≥85% of Week 1-2 rate:
  → YELLOW.
  Step 1: Identify which content type is declining (educational? testimonial? promotional?)
  Step 2: Check hashtag performance (are hashtags from W1-2 still relevant in Week 3-4?)
  Step 3: Review posting time (same time as Week 1-2, or shifted?)
  Step 4: No immediate pivot — monitor for 3 more posts before adjusting

IF Week 3-4 rate <85% of Week 1-2 rate:
  → RED.
  Step 1: Immediately run content audit (compare 3 most recent posts to 3 highest-performing W1-2 posts)
  Step 2: Identify 1 difference (hook? photo quality? caption length? hashtags?)
  Step 3: Adjust next post to address the identified difference
  Step 4: Document change in PHASE_3_EXECUTION_LOG.md
  Step 5: If RED persists for 2+ consecutive posts after adjustment: escalate to Section 4.3 (content type pivot)
```

### 3.2 Instagram Spam/Bot Comment Detection

**Indicators of spam/bot comments**:
- Comments are 1-3 generic words: "Nice!" "Love this!" "Great content!" repeated by different accounts
- Commenter accounts have 0 posts, 0 followers, or were created within the last 7 days
- Comments appear within seconds of posting (bots scrape new posts faster than human engagement)
- Comments include emojis only or unrelated hashtags

**Action tree**:
```
IF <20% of comments are bot-like:
  → Normal level of bot activity. Do not engage; do not delete (deletion can trigger Instagram review).
  → Log count in daily tracking. No escalation.

IF 20-40% of comments are bot-like:
  → YELLOW. Moderate bot exposure.
  Step 1: Delete the bot comments (Instagram: swipe left on comment > trash icon)
  Step 2: Do NOT reply to bot comments
  Step 3: Review hashtags used on this post — bots target popular/generic hashtags
    → If post used very broad hashtags (#herbs, #natural): switch to niche hashtags next post
  Step 4: Monitor next post; if bot rate drops: hashtag adjustment was the fix

IF >40% of comments are bot-like:
  → RED. High bot exposure — account may be at suppression risk.
  Step 1: Delete all identifiable bot comments within 4 hours of detection
  Step 2: Report most flagrant bot accounts to Instagram (Account > three dots > Report)
  Step 3: For next 2 posts: reduce hashtags from 8-10 to 3-5 (fewer hashtags = fewer bot magnets)
  Step 4: Enable Instagram comment filters: Settings > Privacy > Comments > enable "Hide offensive comments" and "Manual filter" (add common bot phrases)
  Step 5: Log in PHASE_3_EXECUTION_LOG.md with date, post, bot count, actions taken
  Step 6: If bot activity persists across 3+ posts: pause Instagram for 48 hours; contact Instagram support
```

---

## Section 4: Algorithm Risk Detection — YouTube

### 4.1 YouTube View Duration and Subscriber Gain

YouTube's algorithm weighs video watch completion and subscriber gain signals. For Community Tab posts (non-video), the equivalent signals are comment count and comment depth.

**Community Tab signals** (Week 3-4):
- Comments within 72 hours: target 10+ long-form (2+ sentence) responses
- Subscriber gain attributable to Community Tab: check YouTube Analytics > Subscribers > Traffic Source
  - If Community Tab is driving 5+ new subscribers per question post: algorithm is amplifying content (positive signal)
  - If Community Tab drives 0-1 subscribers per post consistently: community is not converting to subscribers; reassess question framing

**If YouTube video content is active in Week 3-4** (check if added since Week 1-2 planning):

| Metric | GREEN | YELLOW | RED | Threshold |
|--------|-------|--------|-----|-----------|
| View duration (avg %) | >70% of video watched | 50-70% | <50% | Completion rate |
| Subscriber gain per video | >5/video | 2-5/video | <2/video | Weekly average |
| Recommended traffic (by Day 3) | "Browse" or "Suggested" appears | Minimal | None | YouTube Analytics |
| CTR (link clicks / views) | >5% | 3-5% | <3% | Traffic to Etsy |

### 4.2 YouTube Algorithm Signal: No Recommended Traffic by Day 3

**Definition**: If a YouTube video or Community Tab post shows no "Browse features" or "Suggested" traffic source by 72 hours after posting, the algorithm is not amplifying the content.

**Trigger**: No recommended traffic by Day 3 on 2+ consecutive posts.

**Action tree**:
```
IF recommended traffic appears by Day 3:
  → Algorithm is picking up content. Log signal and continue.

IF no recommended traffic by Day 3 on first post:
  → Watch only. Test content adjustment on next post (see below).

IF no recommended traffic by Day 3 on 2 consecutive posts:
  → CONTENT ADJUSTMENT TRIGGER
  Step 1: Review hook (first 2-3 seconds of video, or first line of Community Tab question)
    - Weak hook: "Here's a question about herbs..."
    - Strong hook: "What one medicinal herb surprised you most this season — and why?"
  Step 2: Review content quality signals
    - Are comments averaging 2+ sentences? If not, reframe question to require more detail in response
    - Is the question topic niche enough? Broad questions ("tell me about herbs") underperform vs. specific ones
  Step 3: For next post, change question framing to a specific-outcome question:
    - Before: "What herbs do you grow?" (too broad, yes/no possible)
    - After: "What's one herb you harvested this season that surprised you by how different fresh vs. dried smells?"
  Step 4: Log change in PHASE_3_EXECUTION_LOG.md
  Step 5: Monitor Day 3 recommended traffic on adjusted post
```

---

## Section 5: Escalation Rules — Cross-Platform

### 5.1 Per-Platform RED Trigger (Single Platform)

If any single platform is RED for 2 consecutive days:

```
TRIGGER: One platform RED for 2 consecutive days

Mandatory response (no judgment call):
  Step 1: Shift content type for that platform
    IF the last 2 RED posts were Educational → post Testimonial next
    IF the last 2 RED posts were Testimonial → post Educational next
    IF the last 2 RED posts were Promotional → post Educational next (do not repeat Promotional)
  Step 2: Increase posting frequency for that platform for 3 days
    IF current frequency is 1 post/day → post 2x per day for 3 days (morning + evening)
    IF current frequency is 1 post/2 days → post 1x/day for 3 days
  Step 3: Log content shift and frequency change in PHASE_3_EXECUTION_LOG.md
  Step 4: Measure engagement on first 2 posts under new approach
  Step 5:
    IF engagement recovers to YELLOW or GREEN → continue new approach for remainder of Week 3-4
    IF engagement stays RED after 2 posts under new approach → escalate to Section 5.2
```

### 5.2 Two-Platform RED Trigger (Systemic Underperformance)

If 2+ platforms are RED on the same day or within 24 hours:

```
TRIGGER: 2 or more platforms RED within 24-hour window

This indicates a systemic content problem (not platform-specific timing issue).

Mandatory response:
  Step 1: Audit last 3 posts across ALL platforms
    - Were they all Promotional? (Common cause of systemic RED)
    - Were they all posted at the same time? (Audience timezone mismatch)
    - Did they all reference the same bundle? (Audience may be saturated on this bundle)
  Step 2: Implement a 48-hour content pause on the underperforming content type
    - If all 3 posts were Promotional: pause Promotional for 48 hours; post Educational only
    - If all 3 posts were same bundle: pivot to different topic for next 2 posts
  Step 3: Publish a high-value Educational post on each platform (do not wait — post within 24 hours of trigger detection)
    - LinkedIn: Plant science deep-dive (300 words, specific herb mechanism)
    - Instagram: Behind-the-scenes herb preparation photo with educational caption
    - YouTube Community: Specific outcome question (see Section 4.2 for strong question format)
  Step 4: Log in PHASE_3_EXECUTION_LOG.md with date, platforms affected, root cause hypothesis, actions taken
  Step 5: If systemic RED persists after 2-day content shift: escalate to SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md Section 4 (paid promotion activation)
```

### 5.3 All-Platform RED Trigger (Full Escalation)

If all 3 platforms are RED for 2+ consecutive days:

```
TRIGGER: LinkedIn + Instagram + YouTube all RED for 2+ consecutive days

This is a full escalation condition. Activate SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md Section 4 immediately.

Pre-escalation actions (take these before contacting contingency doc):
  1. Log precise dates and engagement rates for each platform
  2. Document which content types were underperforming
  3. Note any external factors (holiday? news event? platform algorithm update?)
  4. Confirm unsubscribe rate — is email also underperforming simultaneously?
     IF email also RED (open rate <15%) on same 2-day window:
       → This is a systemic Q3 launch underperformance event
       → Activate SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md AND SEEDWARDEN_Q3_WEEK3_4_CHURN_MONITORING.md simultaneously
```

---

## Section 6: Weekly Social Engagement Summary (Every Monday)

Complete this summary every Monday morning (08:00 UTC) for the prior week.

### Week 3 Summary (complete by Jul 20 08:00 UTC)

**LinkedIn Week 3 Performance**

```
Posts published: [#]
Total engagements: [likes + comments + shares]
Avg engagement rate: [%] | Status: GREEN/YELLOW/RED

Per-post breakdown:
  Jul 13 [post type]: [%] engagement | Status
  Jul 15 [post type]: [%] engagement | Status
  Jul 17 [post type]: [%] engagement | Status (if applicable)

DM volume: avg [#]/day | Surge events: [None / Date: ___]
Hashtag performance: top performer [#hashtag] — impressions [#]
Engagement cliff: [None / Detected on [date]: [%] drop]
Algorithm signal: [Normal / Suppression risk / Viral moment]

Content type performance this week:
  Educational: avg [%] | Status
  Testimonial: avg [%] | Status
  Promotional: avg [%] | Status
```

**Instagram Week 3 Performance**

```
Posts published: [#]
Avg engagement rate: [%] | vs. W1-2 baseline [%]: [+/-]%
  Status: GREEN (≥95% baseline) / YELLOW (<95%) / RED (<85%)

Saves (total): [#] — indicator of high-value content
Follower gain: [#] new followers
Bot comment activity: [Low (<20%) / Moderate (20-40%) / High (>40%)]
  Actions taken: [None / Hashtag adjustment / Comment filter enabled]
```

**YouTube Week 3 Performance**

```
Community posts published: [#]
Total comments received: [#]
Comment quality: [Short / Medium / Long]
Recommended traffic signal (by Day 3): [Yes / No]
Subscriber gain from Community Tab: [#]

Content adjustment trigger: [Not triggered / Triggered on [date] — action: ___]
```

**Week 3 Content Mix Analysis**

```
Actual content mix (all platforms combined):
  Educational: [%] of posts
  Testimonial: [%] of posts
  Promotional: [%] of posts

vs. Target mix:
  Educational: 50-60%
  Testimonial: 20-30%
  Promotional: 15-20%

Adjustment needed for Week 4?
  [ ] No — mix within target range
  [ ] Yes — shift [content type] from [%] to [%]
  Reason: [engagement data showing which type over/under-performed]
```

**Week 3 Escalations Summary**

```
Single-platform RED events: [None / Platform: ___ on [date]]
Two-platform RED events: [None / Platforms: ___ on [date]]
All-platform RED: [None / Dates: ___]
DM surge events: [None / [date] — action: ___]
Hashtag underperformance: [None / [hashtag] swapped out on [date]]
Instagram bot alert: [None / [date] — level: LOW/MODERATE/HIGH]
YouTube algorithm signal: [Recommended traffic present / No signal on [date] — action: ___]
```

### Week 4 Summary (complete by Jul 28 08:00 UTC)

Use the identical template structure as Week 3 above, with dates Jul 20-27.

Add the following Week 4-specific field:

```
Week 3 vs. Week 4 engagement comparison:
  LinkedIn W3 avg: [%] | LinkedIn W4 avg: [%] | Change: [+/-]%
  Instagram W3 avg: [%] | Instagram W4 avg: [%] | Change: [+/-]%
  YouTube W3 comments: [#] | YouTube W4 comments: [#] | Change: [+/-]%

Trend interpretation:
  [ ] Stable or improving — continue approach into Week 5-6
  [ ] Declining — implement content type pivot for Week 5-6 (document adjustment)
  [ ] Severe decline (>30% drop) — activate SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md Section 4
```

---

## Section 7: Content Type Pivot Decision Table

When escalation rules in Section 5 trigger a content type pivot, use this table to select the replacement content:

| Current failing type | Pivot to | Rationale | Implementation |
|---------------------|----------|-----------|----------------|
| Promotional (all platforms RED) | Educational | Educational content is the highest-engagement type for Seedwarden audience; restores credibility before next promotional push | Write a plant-science deep-dive (herb mechanism, harvest timing, preparation method) |
| Educational (LinkedIn RED only) | Testimonial | Testimonials drive comments; LinkedIn algorithm weights comments heavily | Post a practitioner quote or grower story with specific herb, result, and full name |
| Testimonial (low saves, low comments) | Educational with story hook | Testimonials may feel generic; educational with personal opening ("Here's why I started growing valerian...") mimics testimonial engagement | Open with a first-person observation, transition to plant science detail |
| Promotional (Instagram RED only) | Save-bait Educational | Instagram saves are the highest-value signal; create a "swipe to save" format (top 5 herbs, comparison chart, dose guide) | Use carousel format if available; include clear "save this for later" CTA |
| YouTube Community Tab (no comments) | Specific-outcome question | Generic questions get generic responses; outcome questions force longer replies | "What's one herb that surprised you by how different it works in tea vs. tincture form — and which do you prefer?" |

---

## Section 8: Platform-Specific Posting Checklist (Pre-Post Verification)

### LinkedIn Pre-Post (run before each LinkedIn post)

- [ ] Post text finalized and proofread (200-300 words for educational; 150-200 words for promotional)
- [ ] First 50 characters are compelling (not "Here's a post about sleep herbs..." but "Passionflower's MAOI interaction risk is the most misunderstood contraindication in nervine herbalism")
- [ ] NO external URL in post body (LinkedIn algorithm suppresses link posts by 30-40%)
- [ ] Comment with Etsy link ready to post within 5 minutes of publishing
- [ ] Engagement question at end of post (open-ended, invites 2+ sentence response)
- [ ] Hashtags: 3-5 max, at end of post in separate paragraph, Tier 1 + 2-3 Tier 2/3 tags
- [ ] Post scheduled for 09:00 ET / 14:00 UTC (optimal LinkedIn window)

### Instagram Pre-Post (run before each Instagram post)

- [ ] Caption is 80-150 words (longer gets cut off on mobile)
- [ ] Image is 1080×1350px (portrait format for feed; highest real estate on mobile)
- [ ] Image is on-brand: same filter/tone as previous posts, no inconsistent visual style
- [ ] Hashtags planned for FIRST COMMENT (not in caption) — 8-10 hashtags in first comment
- [ ] "Link in bio" updated to point to current bundle Etsy listing (or Linktree page)
- [ ] Bot comment filter active (Settings > Privacy > Comments > Manual filter enabled)
- [ ] CTA in caption: "save this" or "link in bio" as appropriate

### YouTube Community Tab Pre-Post

- [ ] Question is specific and outcome-oriented (not "tell me about herbs")
- [ ] Image or graphic attached to post (Community posts with images get more engagement)
- [ ] Post planned for Tuesday-Thursday (mid-week Community posts get best 72-hour comment windows)
- [ ] Reply plan: check and reply to comments within 24 hours of posting

---

## Appendix: Escalation Contact Matrix

| Escalation Type | When to Trigger | First Action | Document |
|----------------|-----------------|--------------|----------|
| Single platform RED, 2 consecutive days | Any platform <5% engagement for 2 days | Content type pivot (Section 5.1) | This document |
| LinkedIn DM surge >20/day | LinkedIn DMs exceed 20 in one day | Pause 48 hours; review account status (Section 2.2) | This document |
| Instagram bot activity HIGH (>40%) | >40% of comments are bot-like | Delete bots; reduce hashtags; enable filters (Section 3.2) | This document |
| YouTube no recommended traffic 2+ posts | Algorithm not amplifying content | Reframe question hook (Section 4.2) | This document |
| 2+ platforms RED simultaneously | 2+ platforms RED same day | Systemic content audit + 48hr content pause (Section 5.2) | This document |
| All platforms RED 2+ consecutive days | All 3 platforms RED for 2+ days | SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md Section 4 | Contingency triggers doc |
| Social engagement drop all platforms <10% | All platforms below 10% engagement by Week 5 | Paid promotion + influencer (Section 5.3 and contingency doc) | SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md |

---

*Document status: Production-ready. Version 1.0 created July 13, 2026. Covers Week 3-4 (Jul 13-27) per-platform social monitoring. All thresholds are explicit. All escalation rules are mechanical. No judgment calls required at execution time. Update daily log fields after each post. Run weekly summaries every Monday 08:00 UTC.*
