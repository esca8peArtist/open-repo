---
title: "Off-Grid Living Guide — Engagement Metrics Framework"
created: 2026-05-05
status: active
github_url: https://github.com/esca8peArtist/off-grid-living-guide
related: distribution-campaign-plan.md, phase-2-social-media-execution-toolkit.md
---

# Engagement Metrics Framework

## Purpose

This document defines the measurable signals that indicate whether distribution is working, at what thresholds traction becomes Phase 2-sufficient, and what a healthy weekly tracking practice looks like. It is a companion to `distribution-campaign-plan.md` (which covers *what* to post and when) and fills in the *how to know if it's working* layer.

The existing Phase 2 toolkit captures a monitoring dashboard format. This document goes deeper on per-platform baselines, breakout probability thresholds, and decision-ready success criteria.

---

## Section 1: Per-Platform Metrics and Baselines

### 1.1 GitHub (Primary Signal)

GitHub stars are the only metric that compounds. Stars feed the trending algorithm, appear in Google searches for the topic, and create social proof for every subsequent distribution post. All other platform metrics are secondary to this one.

**Metric definitions**:

| Metric | What it measures | Tracking location |
|--------|-----------------|-------------------|
| Stars | Discovery and endorsement by unique visitors | Repository page → Stargazers count |
| Forks | Active adoption — users copying for personal modification | Repository page → Forks count |
| Unique visitors (14-day) | Traffic volume | Insights tab → Traffic → Visitors |
| Views (14-day) | Repeat visit frequency (views / unique visitors > 1.2 = return traffic) | Insights tab → Traffic → Views |
| Top referrers | Which distribution channels are actually sending people | Insights tab → Traffic → Referring Sites |
| Issues opened | Depth of engagement — someone read carefully enough to notice a gap | Issues tab → count by week |
| PRs submitted | Contribution signal — community taking ownership | Pull requests tab |
| Clones (14-day) | Active usage, not just browsing | Insights tab → Traffic → Git Clones |

**Growth trajectory benchmarks for niche knowledge-base projects** (derived from comparable documentation repos with no existing audience):

| Trajectory | Week 1 | Month 1 | Month 3 | Month 6 |
|------------|--------|---------|---------|---------|
| Conservative (Reddit only, no HN traction) | 15–60 stars | 60–180 stars | 120–350 stars | 180–550 stars |
| Moderate (Reddit + HN partial traction, 50–150 HN points) | 40–200 stars | 180–480 stars | 350–850 stars | 550–1,400 stars |
| Breakout (HN front page or viral Reddit post) | 150–600 stars | 400–1,200 stars | 800–2,200 stars | 1,200–4,000 stars |

**GitHub Trending baseline**: A repository typically needs 25–50 new stars in a single day to appear on the daily trending list for its topic category. 100+ new stars in a day reaches the general trending list. These are not targets — they are signals to watch for if a post goes viral.

**Decision-ready success thresholds**:
- 50 stars in Week 1 = healthy launch, continue distribution plan
- 150 stars by end of Month 1 = sufficient traction to expand to secondary channels
- 250 stars total = minimum signal to begin Phase 2 scoping
- 500 stars total = clear community adoption, Phase 2 is justified
- 10 GitHub issues opened (any mix of bug reports, feature requests, questions) = community is reading deeply enough to engage substantively

**What forks signal specifically**: Forks without PRs mean personal-use adoption (people copying for offline use or customization). Forks with subsequent PRs mean active contributors. A fork-to-PR ratio above 0.15 (15%) is unusually healthy for a knowledge-base project; 0.03–0.08 is typical.

---

### 1.2 Reddit

Reddit is the highest-volume immediate channel. The algorithm rewards early velocity above almost everything else: a post that accumulates 10+ upvotes in its first 60 minutes gets pushed into the hot feed and enters a compounding cycle. A post that gets 3 upvotes in the first hour typically stays buried.

**Core Reddit algorithm mechanics** (as of 2025–2026):
- The ranking formula weights velocity (rate of upvotes) over total upvotes
- Engagement velocity — comments-per-hour in the first 2 hours — triggers hot feed placement
- Discussion quality signals matter: posts generating substantive back-and-forth rank above posts with identical upvote counts but thin comment threads
- Crosspost detection suppresses reach if the same URL appears in multiple subreddits within 24 hours

**Per-subreddit baselines** (niche knowledge-base posts, non-viral baseline):

| Subreddit | Baseline upvotes (24h) | Baseline comments (24h) | Breakout threshold | Notes |
|-----------|----------------------|------------------------|-------------------|-------|
| r/offgrid | 40–150 | 8–25 | 300+ upvotes | Skeptical audience; slower but higher quality comments |
| r/preppers | 80–350 | 15–50 | 500+ upvotes | Faster velocity, higher volume, more engagement per upvote |
| r/homesteading | 25–120 | 5–15 | 200+ upvotes | Lower comment density but more personal/experiential replies |
| r/solarpunk | 20–80 | 5–12 | 150+ upvotes | Philosophically engaged; lower volume, higher quality |
| r/SHTF | 30–150 | 10–30 | 250+ upvotes | Nuclear/disaster content performs 2–3x vs general prep content |
| r/self_reliance | 10–50 | 3–10 | 100+ upvotes | Small community; lower bar for meaningful engagement |

**Comment quality indicators** (more valuable than upvote count alone):
- Comments that ask specific domain questions = deep reading signal
- Comments that dispute a specific fact = expert engagement (valuable even when critical)
- Comments that say "saving this" or "this is going in my bookmarks" = durable value signal
- Comments that share personal experience building on the guide = community ownership signal

**Upvote-to-comment ratio benchmarks**: Typical Reddit posts have a comment-per-100-upvotes ratio of 5–15. Technical knowledge-base posts often skew higher (10–25 comments per 100 upvotes) because the content invites questions. A ratio below 5 suggests passive appreciation rather than active engagement — useful for reach but less valuable as a feedback signal.

**Shadow-ban and spam filter indicators to watch**:
- Post shows in your own session but has 0 upvotes after 30 minutes from a fresh browser/incognito session → likely caught in spam filter
- Post gets 5+ upvotes but disappears from the subreddit feed → shadow-removed by moderator
- In either case: do not repost. Contact the subreddit moderators via modmail.

---

### 1.3 Hacker News

HN is bimodal: a post either gains traction within the first 2 hours or it does not. There is limited middle ground. The ranking formula is: **Score = (P − 1) / (T + 2)^1.8**, where P = points (upvotes) and T = age in hours. The gravity exponent of 1.8 means a 2-hour-old post with 10 points ranks identically to a 1-hour-old post with ~6 points. Early velocity is everything.

**Breakout probability benchmarks** (Show HN category, based on aggregate analysis of documentation/knowledge-base Show HN submissions):

| HN points at 2h | Breakout probability | Expected 24h outcome |
|-----------------|---------------------|---------------------|
| < 5 | < 5% | Post stays in /new, never reaches front page |
| 5–15 | 10–20% | May reach page 2–3 for a few hours |
| 15–30 | 30–50% | Reaches front page briefly, 500–2,000 GitHub views |
| 30–75 | 55–75% | Front page for 4–12 hours, 2,000–8,000 GitHub views |
| 75–150 | 80–90% | Front page 12–24h, 8,000–20,000 GitHub views, 100–300 GitHub stars likely |
| 150–300 | Front page confirmed | 20,000–60,000 GitHub views, 250–600 GitHub stars likely |
| 300+ | Top of front page | "Exceptional" event; 600+ GitHub stars in 48h realistic |

**Note on the controversy penalty**: HN's algorithm applies a soft penalty to posts that accumulate more than ~40 comments where upvotes and downvotes are heavily contested. Posts on politically charged or contentious topics (nuclear preparedness may qualify depending on comment tone) can see their scores artificially suppressed even with high raw vote counts. This guide's technical framing helps avoid triggering this penalty.

**Comment quality signals for HN**:
- Critical but substantive comments = high signal (HN readers are experts; absorb their corrections)
- Requests for source citations = opportunity (cite FEMA, NCRP, CDC in your responses — it elevates perceived quality)
- "This reminds me of [related project]" = network effect potential
- Off-topic ideological arguments = noise; ignore, do not engage

**Decision thresholds**:
- 30+ HN points at 2h mark = check back every 30 minutes and respond to all comments
- 75+ HN points = front-page event; expect GitHub referral traffic for 48h
- Below 10 points at 2h = post is not gaining traction; do not resubmit (HN prohibits it), move on

---

### 1.4 Twitter/X

Twitter/X engagement signals shifted substantially in 2025–2026. The algorithm now weights these metrics in this order (per xAI's open-sourced ranking code, confirmed in January 2026 release):

**Algorithm weight hierarchy**:
1. Replies that generate further replies: 75x multiplier vs. likes
2. Author replies to comments: 150x multiplier vs. likes
3. Retweets/reposts: 20x multiplier vs. likes
4. Bookmarks: 10x multiplier vs. likes
5. Profile clicks: 12x multiplier vs. likes
6. Link clicks: 11x multiplier vs. likes
7. Likes: baseline (1x)

This hierarchy has direct implications: a thread that generates a back-and-forth reply chain between you and engaged commenters will reach far more people than a thread that gets passive likes. Respond to replies immediately after posting.

**Engagement benchmarks for informational threads** (accounts with < 2,000 followers posting niche content):

| Metric | Minimal (no amplification) | Healthy (1–2 RT from relevant accounts) | Strong (influencer RT or organic spread) |
|--------|--------------------------|----------------------------------------|----------------------------------------|
| Impressions (tweet 1) | 200–800 | 1,500–5,000 | 10,000–50,000 |
| Thread completion rate | 5–15% | 15–35% | 35–60% |
| Bookmarks | 3–15 | 20–80 | 150–500 |
| Profile clicks | 10–40 | 50–200 | 400–1,500 |
| Retweets | 2–10 | 15–60 | 100–400 |
| Link clicks to GitHub | 5–25 | 30–120 | 200–800 |

**Bookmark-to-like ratio**: For informational/resource content (tutorials, guides, data), a healthy ratio is 0.3–0.5 bookmarks per like (30–50 bookmarks per 100 likes). This is significantly higher than entertainment content (0.05–0.15). If your ratio falls below 0.15 on a resource thread, the thread is being appreciated but not saved — the content may be too abstract or the value proposition unclear.

**Thread decay**: Twitter thread reach drops ~70% after 48 hours for accounts without algorithmic boost. Pin tweet 1 immediately after posting. After 2 weeks, unpin and let the thread age naturally (pinning stale content depresses perceived activity).

**Amplification signals to watch for**: A single retweet from an account with 10,000+ followers in the homesteading, prepper, or off-grid space can multiply impressions by 10–50x. The accounts most likely to amplify are educators, homesteading YouTubers, and emergency management professionals. Tag none of them in the initial thread — let discovery happen organically or through direct outreach after the post is established.

---

### 1.5 Email (if applicable)

If an email capture is added (Substack, ConvertKit, or a simple form), the following metrics apply:

| Metric | Healthy benchmark | Action threshold |
|--------|------------------|-----------------|
| Open rate | 35–55% (niche topic, opted-in audience) | Below 25% = subject line problem or list fatigue |
| Click-through rate | 8–18% on links to specific domains | Below 5% = content-link mismatch; links not relevant |
| Link CTR by section | Track which domain links get clicked most | Top 3 domains by CTR = Phase 2 content priorities |
| Unsubscribe rate | < 0.5% per send | Above 1% = sending too frequently or content mismatch |
| Forward rate | 2–5% for niche content | Above 5% = exceptional; below 1% = low perceived value |

---

## Section 2: Weekly Tracking Template

Use this table each week. Populate from GitHub Insights, platform analytics, and manual review of comment threads.

```
WEEK: _______________  PERIOD: _______________ to _______________

GITHUB
  Stars (cumulative):          ___  (Δ from last week: ___)
  Forks (cumulative):          ___  (Δ: ___)
  Unique visitors (14-day):    ___
  Views (14-day):              ___
  Clones (14-day):             ___
  New issues opened:           ___
  New PRs submitted:           ___
  Top referrer this week:      _______________  (___% of traffic)
  Second referrer:             _______________  (___% of traffic)

REDDIT
  Active posts this week (if any): ___
  Post 1 — subreddit: r/___________  upvotes: ___  comments: ___
  Post 2 — subreddit: r/___________  upvotes: ___  comments: ___
  Notable comments (copy 1–2 that signal content gaps or errors):
    -
    -

HACKER NEWS
  Points at 2h (if submitted): ___
  Final points:                ___
  Comment count:               ___
  GitHub referral traffic from HN (Insights): ___

TWITTER/X
  Thread impressions (tweet 1): ___
  Bookmarks:                    ___
  Retweets:                     ___
  Link clicks to GitHub:        ___
  New followers from thread:    ___

EMAIL (if applicable)
  Subscribers (cumulative):    ___  (Δ: ___)
  Open rate (last send):       ___%
  Top-clicked section link:    _______________

QUALITATIVE OBSERVATIONS
  Organic spread detected (someone posted in a community you didn't post in): Y / N
  Note: _______________
  Educator or organization engagement: Y / N
  Note: _______________
  Factual error or gap reported: Y / N
  GitHub issue filed: Y / N  Issue #: ___

PHASE 2 SIGNAL
  Stars vs. threshold (250 = phase 2 min): ___  → on track / below pace / ahead
  Issues total opened to date: ___  → target: 10 before Phase 2 scoping
  Dominant feedback theme this week: _______________
```

---

## Section 3: Success Criteria for Phase 1 Distribution

These are go/no-go signals for Phase 2 investment. All thresholds are cumulative from launch date.

**Minimum viable traction (Phase 2 justified as modest expansion)**:
- 250 GitHub stars
- 10+ GitHub issues opened (signals deep readership)
- At least one subreddit post exceeding 200 upvotes
- At least one referrer domain other than the ones you posted to (organic spread)

**Strong traction (Phase 2 justified as substantial expansion)**:
- 500 GitHub stars
- 25+ GitHub issues
- HN post reached 50+ points or at least one Reddit post exceeded 500 upvotes
- 3+ organic mentions (posts in communities you didn't seed)

**Exceptional traction (Phase 2 justified as fully resourced effort)**:
- 1,000+ GitHub stars within 90 days
- 50+ GitHub issues, 5+ PRs
- HN front-page event confirmed
- Unsolicited media coverage, educator adoption, or organizational licensing inquiry

**Failure signals (reassess distribution strategy before Phase 2)**:
- Fewer than 80 stars after Month 1 and all 7 distribution posts published
- Zero GitHub issues opened after Month 1 (no deep reading signal)
- All referral traffic concentrated in one channel with no organic spread

If the failure signals apply: before pivoting to Phase 2, try one secondary distribution push (r/solarpunk, r/SHTF, or a Medium article indexed by Google). If stars remain below 100 after that push, the guide may need a README rewrite and a different framing strategy before further distribution investment.

---

## Sources

- [How Hacker News Ranking Algorithm Works](https://medium.com/hacking-and-gonzo/how-hacker-news-ranking-algorithm-works-1d9b0cf2c08d) — Salihefendic (algorithm formula and gravity parameter)
- [How Hacker News Ranking Really Works](http://www.righto.com/2013/11/how-hacker-news-ranking-really-works.html) — righto.com (penalty factors, controversy detection)
- [Reddit Algorithm Explained 2026](https://upvotemax.com/reddit-algorithm-explained) — UpvoteMax (velocity mechanics, engagement quality signals)
- [Reddit Analytics Explained 2025](https://liftburst.com/en/blog/reddit-analytics-explained-master-performance-tracking-2025) — LiftBurst (engagement velocity as primary driver)
- [Twitter/X Engagement Metrics 2026](https://xcrop.io/blog/twitter-engagement-metrics-explained) — xCrop (algorithm weighting hierarchy, bookmark signals)
- [Twitter Engagement Benchmarks 2026](https://www.tweetarchivist.com/twitter-engagement-benchmarks-2025) — Tweet Archivist (per-metric baselines)
- [X Algorithm Ranking Factors](https://www.socialmediatoday.com/news/x-formerly-twitter-open-source-algorithm-ranking-factors/759702/) — Social Media Today (confirmed xAI algorithm weights)
- [GitHub Star History](https://www.star-history.com/) — star-history.com (comparative growth trajectory tool)
- [How to Grow GitHub Repository Stars](https://markaicode.com/grow-github-repository-stars/) — Markaicode (growth strategy benchmarks)
