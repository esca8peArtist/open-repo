---
title: "Seedwarden Launch-Week Monitoring Spec — Day 1 Metrics and Week 1 Success Targets"
prepared: 2026-05-19
status: production-ready — pre-staged for post-launch execution May 30+
scope: Day 1 metrics that matter, platform-specific Week 1 targets, daily check-in cadence,
       escalation triggers, decision gates
launch-date: 2026-05-30
references:
  - phase-2-week-1-success-metrics.md (canonical metric targets and minimum thresholds)
  - LOOKER_STUDIO_DASHBOARD_SPEC.md (optional Looker dashboard if >200 orders/month)
  - PHASE_2_ANALYTICS_GOOGLE_SHEETS_TEMPLATE_SPEC.md (Google Sheets daily log)
  - customer-analytics.csv (daily data entry file)
  - CONTENT_CALENDAR_TEMPLATE.md (post timing for social metric attribution)
positioning: Midwest Zone 5 native plants + wild edibles
---

# Seedwarden Launch-Week Monitoring Spec

**Purpose**: Define the exact metrics to pull on Day 1, the daily check-in cadence for Days 1–7,
platform-specific success targets for Week 1, and the decision rules at the Day 7 gate.

**Relationship to existing docs**: `phase-2-week-1-success-metrics.md` contains the full target
table, minimum thresholds, and "if below minimum" remediation steps. This document consolidates
those targets into a monitoring dashboard format and adds the Day 1 priority stack and platform-
specific rationale that is absent from the existing framework.

**Tool**: Google Sheets daily log (per `PHASE_2_ANALYTICS_GOOGLE_SHEETS_TEMPLATE_SPEC.md`).
Looker Studio is optional and only warranted if monthly orders exceed 200 (see `LOOKER_STUDIO_DASHBOARD_SPEC.md`).
For launch week, Sheets is the correct tool — simpler, faster to set up, no API integration needed.

---

## Part 1: Day 1 Metrics — What Matters in the First 24 Hours

### Day 1 Priority Stack

The signal-to-noise problem on launch day is real: there are 20+ metrics available across Etsy,
Kit, Instagram, TikTok, and Pinterest. Pulling all of them creates analysis paralysis. The following
hierarchy isolates the 6 metrics that actually predict Week 1 outcomes.

**Check these 6 metrics at 9:00pm on May 30:**

| Priority | Metric | Source | What It Tells You |
|---|---|---|---|
| 1 | Kit subscriber count (total) | Kit > Subscribers | Is the email funnel working? This is the Day 1 conversion signal. |
| 2 | Instagram Reel reach | Instagram Insights > Reach | Is the algorithm distributing content? Low reach = algorithm friction. |
| 3 | TikTok video views (first video) | TikTok Analytics > Overview | Is the first video circulating? Below 50 views = distribution hold. |
| 4 | Etsy shop views | Etsy Shop Manager > Stats > Today | Is the shop getting any traffic? |
| 5 | Pinterest impressions (first 3 pins) | Pinterest Analytics > Overview | Baseline for pin performance; data lags 24–48h so this is preliminary. |
| 6 | Kit Email 1 open rate | Kit > Automations > Welcome > Email 1 | Are new subscribers opening the welcome email? Below 40% = spam placement risk. |

**Do not check on Day 1**: Etsy orders, Etsy favorites, follower counts, email click rates.
These signals require 48–72 hours of data to be meaningful. Acting on Day 1 order counts is
the most common launch-week mistake — it produces premature pivots.

### Day 1 Acceptable vs. Alarming Readings

| Metric | Acceptable (Day 1) | Alarming (Day 1) | If Alarming |
|---|---|---|---|
| Kit subscribers | 1–10 | 0 after 12 hours | Verify bio link is live and clickable on all platforms; test Kit landing page in incognito |
| Instagram Reel reach | 50–500 | <20 | Check that Reel was posted as a Reel (not a static post or Story); confirm account is public |
| TikTok video views | 50–300 | 0 after 6 hours | TikTok review queue — wait 24h; if still 0 then delete and re-upload natively |
| Etsy shop views | 5–50 | 0 | Confirm listings are published (not draft); check Etsy shop URL is correct in bio |
| Pinterest impressions | 0–200 | N/A — normal | Pinterest data lags 24–48h; do not act on Day 1 Pinterest data |
| Kit Email 1 open rate | 40–70% | <25% | DNS authentication check: Kit Settings > Email Settings; verify SPF and DKIM are green |

---

## Part 2: Daily Check-In Cadence — Days 1–7

**Time budget per day**: 10 minutes maximum. Log data in `customer-analytics.csv`. Do not make
strategic decisions from single-day data — you are building a trend line for the Day 7 review.

### Check-In Sequence (9:00pm each evening)

1. Open Etsy Shop Manager > Stats > Today. Record: Views, Orders, Revenue, Top listing by views.
2. Open Kit > Subscribers. Record: total count, new subscribers today.
3. Open Kit > Automations > Welcome > Email 1 > Stats. Record: open rate (running total).
4. Open Instagram > Profile > Insights > Content. Record: today's impressions and any new followers.
5. Open TikTok > Analytics > Overview. Record: video views today, new followers.
6. Pinterest: check every 2 days only — data lags 24–48h; daily checks add no new information.

**Log format** (add one row per day to `customer-analytics.csv`):
```
Date, Etsy-Views, Etsy-Orders, Etsy-Revenue, Top-Listing, Kit-Subscribers-Total,
Kit-New-Today, Email1-Open-Rate, Instagram-Followers, TikTok-Followers,
Pinterest-Monthly-Views, Notes
```

### When to Check More Frequently

The 9:00pm daily check is standard. Add a morning check (8:00–9:00am) only on:
- Day 1 (May 30) — morning check to confirm the launch post distributed correctly
- Day 3 (June 1) — morning check to verify the second TikTok/Instagram post is live
- Day 7 (June 6) — full 30-minute review, not a quick check

Do not check metrics hourly on launch day. Hourly checks do not produce actionable information
and create anxiety that degrades decision quality.

---

## Part 3: Week 1 Success Targets by Platform

### Email Funnel (Kit)

| Metric | Week 1 Target | Minimum Acceptable | Rationale |
|---|---|---|---|
| Total subscribers (Day 7) | 50+ | 20+ | 50 subscribers at 8–15% Email 5 coupon redemption rate = 4–8 first orders from email alone. 20 is the "business is alive" threshold. |
| Email 1 open rate | 60%+ | 40%+ | Zone 5 Midwest homesteader audience has high intent; 60% is achievable with a specific, useful subject line. Below 40% indicates spam placement. |
| Email 1 download click rate | 40%+ | 25%+ | The zone card download is the primary value exchange; click rate measures whether the offer is landing. |
| Email 3 open rate (Day 5+ subscribers) | 40%+ | 25%+ | Email 3 is the inflection point — opens here predict Email 5 coupon redemption. |
| Subscribers with cohort tag | 20%+ of list | 10%+ | Measures engagement quality, not just list size. Cohort-tagged subscribers have a significantly higher lifetime value. |

**Note on Apple MPP inflation**: Apple Mail Privacy Protection auto-opens emails, inflating open
rates by 10–25%. A 50% reported open rate may represent a true open rate of 35–40%. Click rate
is the more reliable engagement signal — it cannot be inflated by MPP.

### Etsy

| Metric | Week 1 Target | Minimum Acceptable | Rationale |
|---|---|---|---|
| Total shop views (7-day) | 200+ | 75+ | 200 views at 2.24% historical conversion rate = ~4.5 orders. 75 is the "SEO is not the only blocker" threshold — below this, investigate listing-level issues. |
| Total orders (7-day) | 4+ | 1+ | 4 orders validates conversion rate is holding. Even 1 order is market validation — do not pivot on 1 order, but do not panic either. |
| Listing conversion rate | 1.5–3% | 0.5%+ | Phase 1 baseline was 2.24%. Expect slight degradation as social-sourced traffic is lower intent than Etsy-search traffic. |
| New favorites (7-day) | 20+ | 5+ | Favorites are buying-intent signals 2–3 weeks out. 20+ favorites with 0 orders is normal in Week 1 — the Email 5 coupon converts favorites 10 days post-signup. |

### Instagram

| Metric | Week 1 Target | Minimum Acceptable | Rationale |
|---|---|---|---|
| Followers (Day 7) | 150+ | 50+ | 150 followers is the threshold where Reels start receiving algorithmic amplification in this niche (per `PHASE_2_SOCIAL_GROWTH_STRATEGY.md` cohort analysis). |
| Reach (7-day total) | 500+ | 150+ | Reach is the distribution signal. Low reach on a new account is normal for the first 2–3 days; it should climb by Day 5. |
| Reel completion rate | 30%+ | 20%+ | Instagram's primary quality signal for Reels. Below 20% = the hook is not working. Check: is the first 3 seconds specific and immediately useful, not a generic brand intro? |
| Profile link clicks | 10+ | 3+ | Profile link clicks to Kit landing page are the conversion pathway. Below 3 = the bio CTA is not visible enough. Add "Free zone card — link below" as the first bio line. |
| Save rate (carousels) | 5%+ of reach | 2%+ | Saves are the highest-value engagement signal on Instagram for educational content. A 5% save rate on carousels indicates the content is reference-quality (the goal). |

### TikTok

| Metric | Week 1 Target | Minimum Acceptable | Rationale |
|---|---|---|---|
| Followers (Day 7) | 100+ | 30+ | TikTok follower growth is nonlinear — one video can drive 500 follows, the next zero. 100 is a reasonable week-one baseline for educational niche content with consistent posting. |
| Video views (first video) | 200+ | 50+ | TikTok distributes new videos to 50–200 accounts first; strong completion rate on this seed group triggers wider distribution. Below 50 = distribution hold (see Day 1 alarm table). |
| Average view duration | 30%+ of video length | 15%+ | TikTok's primary quality signal. At 30–45 second video length, 30% duration = 9–13 seconds of watch time. Below 15% = the hook or pacing is losing viewers in the first 5 seconds. |
| Profile visits to bio clicks | 15%+ conversion | 5%+ | Of users who visit the profile, 15% clicking the bio link is achievable when the CTA is explicit in the video ("link in bio for the guide"). |

### Pinterest

| Metric | Week 1 Target | Minimum Acceptable | Rationale |
|---|---|---|---|
| Monthly viewers (Day 7 reading) | 1,000+ | 200+ | Pinterest lags 2–3 weeks before significant reach growth. The Week 1 target is a baseline indicator, not a mature signal. If below 200 after 14 days (not 7): increase pin frequency. |
| Outbound clicks (7-day) | 5+ | 1+ | Direct traffic to Etsy or Kit landing page. Pinterest drives the slowest but most durable traffic — outbound clicks in Week 1 often represent compounded pin performance 2–4 weeks post-launch. |
| Impressions per pin | 50+ | 10+ | Impression rate in the first 48h indicates whether the pin is being indexed correctly. Below 10 per pin: verify Rich Pins are enabled in Pinterest settings. |

---

## Part 4: Day 7 Decision Gate — June 6

**Time required**: 30 minutes. Do not abbreviate this — it determines Week 2 strategy.

Pull all metrics collected during Days 1–7. Apply this decision framework:

### Gate Logic

| Scenario | Definition | Week 2 Strategy |
|---|---|---|
| Green — Accelerate | 2+ orders AND 50+ Kit subscribers AND Instagram reach 500+ | Increase cadence: 5x/week Instagram, 4x/week TikTok. Stage next email broadcast (product spotlight) for Week 3. Add 5 pins/day on Pinterest. |
| Yellow — Hold | 1 order OR 20–50 Kit subscribers OR reach 150–500 | Continue current cadence. Test one new format in Week 2 (BTS or talking-head). Monitor Email 3 performance before changing email copy. |
| Red — Diagnose | 0 orders AND <20 subscribers AND reach <150 | Run the 5-step diagnostic in `phase-2-week-1-success-metrics.md` Part 6. Fix the one most-likely broken element. Do not change all systems simultaneously. |

### Three Specific Decisions to Make on June 6

**Decision 1: Which product to feature in Week 2 social.**
Pull Etsy Shop Manager > Stats > Listings > sort by views (7-day). The top-traffic listing gets
featured in the Week 2 Instagram Reel and Pinterest pins. If the top-traffic listing has zero
orders, feature it with a user-benefit story angle rather than a product-feature angle.

**Decision 2: Which email angle to lead Week 2.**
Pull Kit > Subscribers > filter by cohort tag. The most common tag determines Week 2 newsletter
content (see `phase-2-week-1-success-metrics.md` Part 3, Decision 2 table).

**Decision 3: Hold or accelerate.**
Apply the Gate Logic table above. Do not escalate from Yellow to Green based on emotion — apply
the numeric criteria.

---

## Part 5: Metric Relationship Map

Understanding how metrics relate to each other prevents misreading the data.

**High Etsy views + zero orders**:
- Primary suspect: listing primary image (mockup vs. lifestyle) and the first 150 characters of the description.
- These are the two elements visible at thumbnail size in Etsy search results.
- Remediation: add a lifestyle photo as Slot 1 image if not already done.

**High email open rate + low click rate**:
- Subject line is working; email body CTA is not.
- For Email 1: download button must be large, full-width, above the fold on mobile (iPhone 12 size).
- For Email 3: story-based subject line outperforms generic educational subject lines.

**High social impressions + zero Kit sign-ups**:
- Bio link is not being clicked, or the bio CTA is not visible.
- Fix: add "Free zone card — link below" as the very first line of the Instagram bio.
- If already there: the audience is consuming content but not yet taking action (common in Days 1–5,
  resolves as trust builds by Day 7–10).

**Zero TikTok views on first video**:
- TikTok review queue — wait 24 hours before acting.
- If still zero after 24h: delete and re-upload natively with a slightly different caption.
- Never cross-post from Instagram to TikTok; TikTok suppresses cross-posted content.

**Kit subscriber growth with zero Etsy orders (Days 1–7)**:
- This is expected behavior. Email 5 (the product offer with coupon SEEDWARDEN15) delivers at Day 10.
- Week 1 subscriber growth with zero orders is the correct pattern. The first Email 5 conversion
  signal arrives in Week 2 (Day 10+ subscribers entering the coupon offer phase).

---

## Part 6: Platform-Specific Engagement Rate Benchmarks

Use these to evaluate whether the Week 1 numbers indicate performance or underperformance
relative to the niche. Benchmarks are sourced from `PHASE_2_SOCIAL_GROWTH_STRATEGY.md`
and the competitive landscape analysis (10 benchmark accounts).

| Platform | Metric | Seedwarden Target | Niche Benchmark (comparable accounts) | Notes |
|---|---|---|---|---|
| Instagram | Engagement rate | 8–12% | 2.5–3.8% (mid-tier niche) | New accounts (<500 followers) typically show higher engagement rates because followers are highly self-selected |
| Instagram | Save rate on carousels | 5–8% | 2–4% | Educational carousels save at higher rates than Reels; this is the primary value signal for carousel content |
| TikTok | Engagement rate | 10–15% | 6–8% (niche macro creators) | New accounts with small, self-selected audiences show higher engagement; expect this to normalize downward as follower count grows |
| TikTok | Average view duration | 30–40% | 25–35% | Educational content with a strong hook outperforms broad content on duration; Zone 5 specificity is the hook here |
| Pinterest | Save rate on pins | 1–3% | 0.5–2% | Educational pins in the foraging/homesteading niche save at higher rates than lifestyle pins; expect Template 2 (Educational Hook) to outperform Template 1 (Product Mockup) on saves |

**Interpreting early engagement rates**: In Days 1–7, engagement rates will appear inflated
relative to the niche benchmarks above. This is normal — early followers are the highest-intent
segment of any audience. Engagement rates will normalize downward as the account reaches 500–1,000
followers. Do not use Week 1 engagement rates to extrapolate long-term growth projections.

---

## Part 7: Monitoring Tool Stack

| Tool | What It Monitors | Access |
|---|---|---|
| Google Sheets (`customer-analytics.csv`) | Daily data log: all platforms in one row | `projects/seedwarden/customer-analytics.csv` |
| Etsy Shop Manager | Etsy views, orders, revenue, listing stats | Etsy > Shop Manager > Stats |
| Kit dashboard | Email opens, clicks, subscriber count, cohort tags | Kit > Subscribers and Automations |
| Instagram Insights | Reach, impressions, profile visits, Reel completion | Instagram app > Profile > Insights |
| TikTok Analytics | Video views, average duration, profile visits, followers | TikTok app > Analytics |
| Pinterest Analytics | Monthly viewers, impressions, outbound clicks | Pinterest app or desktop > Analytics |
| Looker Studio | Optional: live dashboard connecting all sources | Only if >200 orders/month; see `LOOKER_STUDIO_DASHBOARD_SPEC.md` |

**Daily time budget**: 10 minutes for the standard check-in, 30 minutes for the Day 7 full review.

---

*Prepared: 2026-05-19. Exploration Queue Item 93. Status: production-ready. Targets verified against
`phase-2-week-1-success-metrics.md` (canonical source). Platform engagement benchmarks from
`PHASE_2_SOCIAL_GROWTH_STRATEGY.md` competitive landscape section.*
