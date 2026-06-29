---
title: "Phase 3 Social Platform Alert Rules — LinkedIn / Instagram / YouTube"
date: 2026-06-29
version: 1.0
status: active
sprint-window: June 29 – August 3, 2026
cross-references:
  - PHASE_3_EXECUTION_LOG.md (where metrics are logged daily)
  - PHASE_3_SOCIAL_MEDIA_CONTENT_CALENDAR.md (source post copy and post schedule)
  - PHASE_3_WEEK_1_2_ALERT_THRESHOLDS.md (supplementary numeric gates)
  - PHASE_3_EXTENDED_SOCIAL_CALENDAR_JUL_SEP.md (posts through Week 6)
---

# Phase 3 Social Platform Alert Rules

**How to use**: Check each platform's metrics at the times specified. All thresholds are numeric. When a metric crosses a threshold, follow the listed steps in order. Log all YELLOW and RED triggers in `PHASE_3_EXECUTION_LOG.md`.

**Post send time**: 14:00 UTC (= 10:00 ET) is the primary send window for LinkedIn and Instagram. Instagram secondary window: 22:00 UTC (= 18:00 ET). YouTube Shorts: 14:00 UTC premiere.

---

## PLATFORM 1 — LINKEDIN

### Schedule

| Day | Post # | Content Type | Send Time (UTC) |
|-----|--------|--------------|-----------------|
| Mon Jun 29 | Post 1 | Promotional — Women's Health launch | 14:00 UTC |
| Tue Jun 30 | Post 2 | Educational — Red Clover spotlight | 14:00 UTC |
| Thu Jul 2 | Post 4 | Community — Grower Feature 1 | 14:00 UTC |
| Fri Jul 3 | Post 5 | Educational — Expectorant vs. Demulcent | 14:00 UTC |
| Sun Jul 6 | Post 7 | Promotional — Respiratory launch | 14:00 UTC |
| Tue Jul 8 | Post 8 | Educational — Elderberry Deep Dive | 14:00 UTC |

LinkedIn posts not listed above are Instagram-only or YouTube-only days.

### Engagement Thresholds

**Metric**: Engagement rate = (likes + comments + shares + clicks) / impressions × 100.

```
IF engagement rate >8% at T+8hr:
  → Status: GREEN. No action needed.
  Log in PHASE_3_EXECUTION_LOG.md.

IF engagement rate 4–8% at T+8hr:
  → Status: YELLOW.
  Step 1: Check comments for the type of engagement. Are these surface likes (no comments) 
    or substantive interactions (questions, shares)?
    - Surface likes only: try adding a question at the end of the next LinkedIn post 
      ("What's your experience with [herb]?") to increase comment rate.
    - No engagement at all but impressions are high: consider whether the hook 
      (first 2 lines, before "see more") is compelling.
  Step 2: Check: was the post published at exactly 14:00 UTC on a Tue or Thu?
    - Off-day posts (Mon, Fri) typically underperform by 20-30% vs. Tue/Thu baseline.
    - If this post ran on a non-optimal day, do not use this data point to change the posting strategy.
  Step 3: No changes to current post. Apply findings to next LinkedIn post.
  Log in PHASE_3_EXECUTION_LOG.md.

IF engagement rate <4% at T+8hr:
  → Status: RED.
  Step 1: Check: did the post publish? Open LinkedIn and confirm the post is visible on the page.
    - If post is missing: repost immediately. Check scheduler for failure.
  Step 2: Audit the hook. Open the post. Look at the first 2 lines before "see more."
    - Hook criterion A: does it make a specific claim or start a surprising statement?
    - Hook criterion B: does it avoid starting with "I" (LinkedIn algorithm penalizes first-person openers)?
    - Hook criterion C: is the text followed by a line break (LinkedIn collapses long first paragraphs)?
    If hooks fail: revise the next post's opening 2 lines before scheduling.
  Step 3: Audit post timing. Compare post timestamp vs. optimal window.
    - Optimal: Tuesday 14:00 UTC or Thursday 14:00 UTC.
    - If posted outside this window: move next post to next available Tue or Thu 14:00 UTC.
  Step 4: Audit content-type mix. Count the last 5 LinkedIn posts:
    - Promotional posts: _____/5. Target: max 2/5.
    - If >2 of last 5 posts are promotional (bundle launch announcements), pivot next 2 posts 
      to educational content before next promotional post.
  Log RED in PHASE_3_EXECUTION_LOG.md with specific finding and action taken.
```

### Zero-Check (Check at T+8hr for every post)

```
IF impressions = 0 at T+8hr:
  → Status: RED (post not distributing).
  Step 1: Confirm the post is live (not in draft or failed state in scheduler).
  Step 2: Check LinkedIn company page directly — confirm the post appears in the feed.
  Step 3: If post appears but has 0 impressions: tag 1 personal connection in a comment 
    to seed initial distribution ("Tagging [NAME] who might find this useful").
  Step 4: If post is in draft or failed: republish immediately. Screenshot error message if present.
  Log RED in PHASE_3_EXECUTION_LOG.md.
```

### LinkedIn Strategy Adjustment Triggers

| Condition | Trigger | Adjustment |
|-----------|---------|------------|
| 3 consecutive posts below 4% engagement | Any 3 consecutive posts RED | Shift 2 promotional posts to educational for next 2 weeks |
| 0 comments in first 7 posts | No comments by Jul 13 | Add explicit question ("What's your go-to respiratory herb?") in every LinkedIn post for 2 weeks |
| >20% drop in impressions post-to-post | Impressions decline >20% 2 posts in a row | Test posting at 12:00 UTC instead of 14:00 UTC for 2 posts |

---

## PLATFORM 2 — INSTAGRAM

### Schedule

| Day | Post # | Content Type | Send Time (UTC) |
|-----|--------|--------------|-----------------|
| Mon Jun 29 | Post 1 | Promotional — Women's Health launch | 14:00 UTC |
| Wed Jul 1 | Post 3 | Educational — Harvest Timing | 14:00 UTC |
| Thu Jul 2 | Post 4 | Community — Grower Feature 1 | 14:00 UTC |
| Sat Jul 5 | Post 6 | Educational — Thyme Respiratory | 22:00 UTC |
| Sun Jul 6 | Post 7 | Promotional — Respiratory launch | 14:00 UTC |
| Wed Jul 8 | Post 9 | Educational — Respiratory lifestyle | 14:00 UTC |

Instagram secondary window (22:00 UTC): use for Saturday posts and any educational posts that underperformed at 14:00 UTC.

### Engagement Thresholds

**Metric**: Engagement rate = (likes + comments + saves + shares) / reach × 100.

```
IF engagement rate >5% at T+8hr:
  → Status: GREEN. No action.
  Log in PHASE_3_EXECUTION_LOG.md.

IF engagement rate 2–5% at T+8hr:
  → Status: YELLOW.
  Step 1: Check saves specifically (saves are the highest-signal Instagram action — they indicate 
    the content is useful enough to return to).
    - If saves >0.5% of reach: the content is resonating but reach is limiting engagement rate. 
      Consider boosting with a Story crosspost ("New post on herb cultivation — link in stories").
    - If saves = 0: add a "save this for harvest season" CTA to the next educational post.
  Step 2: Check hashtag performance. Open Instagram Insights > Post > Discovery.
    - If >60% of reach is from hashtags (not followers): post is reaching new audiences but 
      not converting them to engagement. Consider: are hashtags too broad (e.g., #herbs, #plants) 
      vs. specific (e.g., #herbalmedicine, #medicinalplants)?
  Step 3: Log YELLOW in PHASE_3_EXECUTION_LOG.md.

IF engagement rate <2% at T+8hr:
  → Status: RED.
  Step 1: Check reach. If reach is very low (<100 for a post):
    - Option A: Check whether the account is under a shadowban (Instagram restriction). 
      Test: post a simple photo with no hashtags and check if it appears in followers' feeds.
    - Option B: Increase hashtag specificity. Replace 3–4 broad hashtags with niche ones.
  Step 2: Check image quality. Open the post.
    - Is the first image visually striking when viewed at thumbnail size (80px square)?
    - Is there text overlay that is legible on mobile?
    - If image quality is weak: carousel posts typically outperform single-image posts by 20–30%. 
      Try a 3-slide carousel for the next educational post.
  Step 3: Check post timing. Was this post published at 14:00 UTC or 22:00 UTC?
    - Monday posts: 14:00 UTC (consistent followers)
    - Saturday posts: 22:00 UTC (higher weekend evening engagement)
    - If a post ran at a non-optimal time: use 22:00 UTC window for next post as a test.
  Step 4: Log RED in PHASE_3_EXECUTION_LOG.md with specific finding.
```

### Instagram-Specific Rules

**Bio link**: Update bio link each time a new bundle launches. Bio link priority order:
1. Most recently launched bundle (drives conversion)
2. Etsy store homepage (if multiple bundles live and you want general traffic)
Never leave bio link pointing to a sold-out or unlaunched bundle.

**Story crosspost rule**: Within 30 minutes of publishing every promotional feed post, publish a Story that links to the same post (Instagram "Share to Story" feature). Stories decay in 24 hours; they supplement, not replace, feed posts.

**Reels vs. static post rule**: If a post achieves <2% engagement (RED) for 3 consecutive posts, test switching to a Reel (15–30 second video). Video content typically gets 2–3× the organic reach of static posts on Instagram in 2026.

### Algorithm Decay Alert

```
IF Instagram impressions-per-post decline >30% over 3 consecutive posts:
  → Algorithm decay likely (account is being shown less in non-follower feeds).
  Step 1: Increase posting frequency temporarily: 2× per week instead of 1× for 2 weeks.
  Step 2: Add CTA to each post asking followers to share ("If this was useful, send it to 
    someone who grows herbs.").
  Step 3: Re-test with a Reel format (video) on the next post.
  Log in PHASE_3_EXECUTION_LOG.md.
```

---

## PLATFORM 3 — YOUTUBE (Shorts + Long-Form)

### Schedule

| Date | Content Type | Format | Premiere Time (UTC) |
|------|--------------|--------|---------------------|
| Fri Jul 3 | Educational — Herb harvest timing | Shorts (15–60 sec) | 14:00 UTC |
| Fri Jul 10 | Guest pre-recorded — Respiratory health | Long-form (8–15 min) | 14:00 UTC premiere |

YouTube Friday 14:00 UTC premiere is optimal for herbal/natural health audience. Pre-recording ensures no live-session failure risk.

### Click-Through Rate (CTR) Thresholds

**Metric source**: YouTube Studio > Analytics > Reach > Impressions click-through rate.
**Check time**: T+48hr (not T+8hr — YouTube metrics take longer to stabilize than social posts).

```
IF CTR >3% at T+48hr:
  → Status: GREEN. No action.
  Log in PHASE_3_EXECUTION_LOG.md.

IF CTR 1–3% at T+48hr:
  → Status: YELLOW.
  Step 1: Audit the thumbnail.
    - Is there a human face in the thumbnail? (Faces increase CTR by ~25% on YouTube.)
    - Is the text overlay legible at 120×90px (thumbnail size on mobile)?
    - Is the title specific ("How to harvest thyme at peak volatile oil content" vs. 
      "Herb harvest tips")?
  Step 2: Audit the title and first 100 characters of description (preview text in search).
    - Does the title include a specific outcome or curiosity hook?
    - Is the main keyword in the first 60 characters of the title?
  Step 3: For Shorts specifically: are the first 2 seconds visually engaging (no slow intros)?
  Log YELLOW. Apply findings to next YouTube upload.

IF CTR <1% at T+48hr:
  → Status: RED.
  Step 1: Check: is the video showing in YouTube search for target keywords 
    ("herbal medicine," "medicinal herbs," "herb harvest")?
    - Test: open an incognito browser. Search for "how to harvest thyme." Does the video appear?
    - If not in search results: update description with 5+ keyword-rich sentences about the video topic.
  Step 2: If CTR is low and views are also low (not from search): 
    - Post the Shorts on Instagram Reels and TikTok (if active) for cross-platform distribution.
    - Embed the long-form video in the next Kit email (link to YouTube, not embed — Kit does not support embeds).
  Step 3: Evaluate guest interview resonance (for long-form videos with guests):
    - Check: does watch time reach 30% of video length? (YouTube Analytics > Audience retention.)
    - If watch time <30%: first 60 seconds are not capturing interest. Trim the intro in the next video.
    - If watch time <30% consistently for 2 videos: reconsider interview format — consider solo 
      educational format instead.
  Log RED in PHASE_3_EXECUTION_LOG.md.
```

### Watch Time Thresholds (Long-Form)

| Metric | GREEN | YELLOW | RED | Action if RED |
|--------|-------|--------|-----|---------------|
| Audience retention at 30 sec | >70% | 50–70% | <50% | Trim intro to <15 seconds |
| Audience retention at 2 min | >50% | 30–50% | <30% | Content density issue — add visual cuts every 45 seconds |
| Average watch time vs. video length | >40% | 25–40% | <25% | Video too long for topic — cap future videos at 8 minutes |

---

## CROSS-PLATFORM WEEKLY HEALTH CHECK

Run every Sunday at 22:00 UTC. Fill in the grid below and log in `PHASE_3_EXECUTION_LOG.md`.

| Week | Platform | Posts Published | Avg Engagement Rate | GREEN / YELLOW / RED Posts | Net New Followers | Action Required |
|------|----------|-----------------|--------------------|-----------------------------|-------------------|-----------------|
| Wk 1 (Jun 29–Jul 5) | LinkedIn | /5 | % | G: Y: R: | | |
| Wk 1 (Jun 29–Jul 5) | Instagram | /4 | % | G: Y: R: | | |
| Wk 1 (Jun 29–Jul 5) | YouTube | /0 | CTR: % | G: Y: R: | | |
| Wk 2 (Jul 6–13) | LinkedIn | /5 | % | G: Y: R: | | |
| Wk 2 (Jul 6–13) | Instagram | /4 | % | G: Y: R: | | |
| Wk 2 (Jul 6–13) | YouTube | /1 | CTR: % | G: Y: R: | | |

---

## POSTING TIME REFERENCE

| Platform | Primary Window (UTC) | Secondary Window (UTC) | Best Days | Avoid |
|----------|---------------------|------------------------|-----------|-------|
| LinkedIn | 14:00 UTC (10:00 ET) | — | Tue, Thu | Sat, Sun |
| Instagram (feed) | 14:00 UTC (10:00 ET) | 22:00 UTC (18:00 ET) | Mon, Wed, Sat | — |
| YouTube | 14:00 UTC (10:00 ET) | — | Fri | Mon–Wed (lower view velocity) |

All times optimized for construction industry morning routine (primary audience). 14:00 UTC = 10:00 ET = 7:00 PT (before job-site hours begin, peak mobile check-in window).

---

*Prepared: June 29, 2026. Engagement benchmarks based on Q2 2026 campaign data (construction/home-improvement Etsy audience). LinkedIn 8%+ = top-quartile small brand benchmark. Instagram 5%+ = industry average for botanical/herbal content. YouTube 3%+ CTR = standard benchmark for educational Shorts. Update benchmarks after Week 2 if actual data diverges significantly.*
