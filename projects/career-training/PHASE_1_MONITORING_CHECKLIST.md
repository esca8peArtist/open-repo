---
title: "Phase 1 Week 1-4 Monitoring Checklist"
project: career-training
phase: "1"
created: 2026-06-28
status: operational
---

# Phase 1 Week 1-4 Monitoring Checklist

**Scope**: Operationally executable week-by-week monitoring for the first 4 weeks of the Phase 1 GitHub Pages deployment. Each item specifies where to find the metric, what number to record, and what action to take based on what you see. This is not a metrics catalog — it is a checklist you run once per day (Monday-Friday, 10 minutes per session).

**Tools required**: GA4 (analytics.google.com), Kit dashboard (app.kit.com), optional: Google Search Console (search.google.com/search-console)

**Data availability note**: GA4 reports have a 24-48 hour lag. Realtime data is live but cannot be exported. The daily check-in uses the "last 7 days" report view, not realtime, except where noted.

---

## Pre-Launch Baseline Check (Do This Before Pushing)

Complete before the first GitHub Pages push so you have a clean pre-launch baseline:

- [ ] GA4 property created; Measurement ID confirmed
- [ ] GA4 snippet in `head_custom.html` and committed to repo
- [ ] Kit account created; 4 forms created; welcome automation built
- [ ] Smoke test passed (test subscriber received correct welcome email per path)
- [ ] Thank-you page created (`/signup-thank-you/`) with GA4 conversion event
- [ ] Google Search Console property created; sitemap submitted
- [ ] Baseline record: zero subscribers in Kit, zero sessions in GA4

**First hour after push**: Verify GA4 Realtime shows your own session when you visit the live site. If Realtime shows 0 active users after 2 minutes, the snippet is not firing — check `head_custom.html` deployment.

---

## Week 1 Checklist (Days 1-7 Post-Launch)

**Monitoring goal**: Confirm traffic is arriving, events are firing correctly, and the email signup funnel is functioning end-to-end.

### Day 1 (Launch Day)

**Time required**: 20 minutes (expanded for launch)

**GA4 Realtime** (analytics.google.com > Reports > Realtime):

- [ ] Visit your live site; confirm your session appears in Realtime > Active users
- [ ] Click a module page link; confirm page view appears in Realtime > Pages
- [ ] Click a path CTA link; confirm `path_selection` event appears in Realtime > Events
- [ ] Submit a test email via the signup form; confirm redirect to thank-you page fires `email_signup_conversion` in Realtime > Events

**Kit Dashboard** (app.kit.com):

- [ ] Confirm test subscriber from smoke test has correct tag
- [ ] Confirm welcome email was sent (Broadcasts or Automations > Activity)

**Record to tracking sheet** (create a simple Google Sheet or text file):

```
Date: [DATE]
Sessions today: [from GA4 Realtime, approximate]
Subscribers: [from Kit Dashboard]
Events firing: YES / NO / PARTIAL
Issues found: [describe or "none"]
```

**If events are NOT firing**: Check the browser console (F12 > Console) for JavaScript errors. Common causes: `head_custom.html` file not committed, `jekyll.environment` check blocking the script on GitHub Pages (remove the production guard temporarily to test), or Measurement ID typo.

### Days 2-7 (First Week)

**Time required**: 10 minutes each morning

Check GA4 > Reports > Acquisition > Traffic acquisition (date range: last 7 days):

- [ ] Record total sessions for the week
- [ ] Record top traffic source (Direct / Organic Search / Social / Referral)
- [ ] Record which pages have the most views (Reports > Engagement > Pages and screens)

Check Kit Dashboard > Subscribers:

- [ ] Record subscriber count (total, not new)
- [ ] Record which form has the most subscribers (check by tag count)

**Week 1 targets** (these are realistic for a new GitHub Pages site with no promotion):

| Metric | Week 1 Target | Concern Threshold |
|---|---|---|
| Total sessions | 20-100 | Under 10 = possible indexing failure |
| Email signups | 1-5 | 0 after 50+ sessions = funnel issue |
| Bounce rate | Under 70% | Over 85% = content/CTA mismatch |
| Module pages viewed | At least 5 unique | 0 = navigation problem |

**If sessions are under 10 after 7 days**: The site may not be indexed yet (expected), or there is a technical deployment issue. Check Search Console for crawl errors. See `github-pages-deployment-guide.md` for troubleshooting.

**If 0 email signups after 50+ sessions**: The Kit forms are either not rendering or not visible. Check that the embed code is on the page and that Kit forms load correctly. Test from an incognito window.

---

## Week 1 End-of-Week Summary (10 minutes, Friday)

Run this after Day 7. It sets your baseline for Week 2-4 trend analysis.

**GA4 > Reports > Engagement > Overview (last 7 days)**:

- [ ] Total sessions: ___
- [ ] Total users: ___
- [ ] Average engagement time per session: ___
- [ ] Engaged sessions rate: ___% (target: above 30%; under 20% = visitors are not reading)
- [ ] Top 5 pages by views: ___

**GA4 > Reports > Engagement > Events (last 7 days)**:

- [ ] `page_view` count: ___
- [ ] `path_selection` count: ___
- [ ] `email_signup_conversion` count: ___
- [ ] `scroll` events (90% scroll depth — from Enhanced Measurement): ___

**GA4 > Reports > Tech > Tech overview (last 7 days)**:

- [ ] % mobile sessions: ___ (target: benchmark this week; act if mobile vs desktop conversion rates diverge significantly)
- [ ] Top browsers: ___

**Kit Dashboard**:

- [ ] Total subscribers: ___
- [ ] Subscribers by path tag: residential-gc: ___ industrial-gc: ___ specialty-sub: ___ generic: ___
- [ ] Welcome emails sent (from automation activity): ___
- [ ] Welcome email open rate (if available on free plan): ___%

**Week 1 baseline record**: Save this data. All future weeks compare against it.

---

## Week 2 Checklist (Days 8-14)

**Monitoring goal**: Identify the highest-performing traffic sources and modules; begin shaping Week 3 promotion accordingly.

### Daily Check (10 minutes each morning)

- [ ] GA4 > Reports > Realtime: Any sessions right now? (Monday mornings and Thursday afternoons tend to be peak for professional audiences)
- [ ] Kit > Subscribers: Daily new subscriber count (Kit shows this in the dashboard header)
- [ ] Any emails in your inbox from Kit (welcome emails to yourself from earlier test, bounced emails, unsubscribes)

### Week 2 Mid-Week Deep Dive (Wednesday, 20 minutes)

**Module performance** — GA4 > Explorations > Free Form:

1. Open GA4 > Explore > blank exploration
2. Dimensions: `Page path and screen class`
3. Metrics: `Views`, `Average engagement time`
4. Filter: Page path contains `/modules/`
5. Sort by Views descending

Answer these questions:
- [ ] Which module is the most viewed? Record: ___
- [ ] Is the most-viewed module the first module of a path (expected) or a middle module (interesting — people are navigating directly)?
- [ ] What is the average engagement time on module pages? (Under 1 minute = likely a bounce, not a read; over 3 minutes = active reading)

**Traffic source performance** — GA4 > Reports > Acquisition > Traffic acquisition:

- [ ] Which channel is sending the most sessions? ___
- [ ] Which channel is sending the most email signups (conversions)? ___
  - Note: If organic search is already sending traffic in Week 2, that is unusually fast — verify it is not mostly bots via the Realtime filter

**Mobile vs. desktop conversion split** — GA4 > Explore > create custom exploration:
- Dimension: `Device category`
- Metric: `Conversions` (email_signup_conversion)
- This shows whether mobile or desktop visitors are converting to email subscribers
- If mobile conversion rate is significantly lower (e.g., 0.5% mobile vs. 3% desktop): Kit forms may not be rendering well on mobile. Test on a real mobile device.

### Week 2 End-of-Week Summary

- [ ] Total sessions Week 2 vs. Week 1: ___% change
- [ ] Total email signups Week 2 vs. Week 1: ___% change
- [ ] Most-viewed module (still): ___
- [ ] Any unsubscribes from Kit welcome sequence? ___
  - More than 10% unsubscribe rate in first 7 days = welcome email content or cadence issue

**Week 2 decision**: If traffic is under 50 sessions total in Week 2, begin LinkedIn promotion (if you have a LinkedIn presence). Share one module link with a 2-sentence context note. Do not wait for organic search to build.

---

## Week 3 Checklist (Days 15-21)

**Monitoring goal**: Identify content gaps and CTA optimization opportunities; begin A/B test data collection.

### Daily Check (5-10 minutes)

- [ ] Kit subscriber count: ___
- [ ] GA4: Did yesterday's sessions exceed the daily average from Weeks 1-2?

### Week 3 Deep Dive — Bounce Analysis (30 minutes, Tuesday)

Bounce/exit analysis is the most actionable data at this traffic scale.

**GA4 > Reports > Engagement > Pages and screens > add "Exits" metric**:

Not all pages show "Exits" by default. Use Explore:

1. GA4 > Explore > Free Form
2. Dimensions: `Page path and screen class`, `Exit page path`
3. Metrics: `Views`, `Exits`, `Bounce rate`
4. Filter: Page path NOT containing `signup-thank-you` (exclude the confirmation page)

Answer:
- [ ] Which page has the highest exit rate? ___
- [ ] Is the homepage a top exit page? (Expected — many visitors leave without clicking through. High exit rate on the homepage is acceptable if engagement rate is above 30%)
- [ ] Are module pages exit pages? (Concern: if a module page has a high exit rate, visitors are not reading to the next module. Check if there is a "Next module" link at the bottom)
- [ ] Is the signup page an exit page? (Concern: if visitors visit `/signup/` and leave without subscribing, the page may be confusing or the forms may not be loading)

**Action if signup page exit rate is above 70%**: The signup page is losing people. Test: visit `/signup/` yourself in an incognito window on mobile. Do the Kit forms load? Do they render correctly? Is there a clear value proposition before the forms?

### Week 3 Module Completion Proxy

There is no native progress tracking on a static site. Use this proxy:

**GA4 > Explore > User Explorer** (requires sufficient traffic):
- Find users with 5+ sessions; look at their page path sequences
- If a user visited Module 01 → Module 02 → Module 03 in sequence, that is a path completion proxy
- Low-traffic reality: you may not have enough users with 5+ sessions in Week 3. If so, skip this and return in Week 6+.

**Alternative proxy**: Email engagement rate from Kit. If welcome sequence Day 7 email has above 40% open rate, subscribers are actively reading. Below 25% = either deliverability issue or wrong content.

### Email Capture Rate Calculation (Week 3)

Calculate: `(total email signups) / (total sessions) × 100 = email capture rate %`

Benchmark for a content-heavy educational site with no paid traffic:
- Under 0.5%: Low — the form placement or offer is not compelling
- 0.5%-2%: Normal for organic traffic to educational content
- 2%-5%: Good — content-to-offer alignment is working
- Above 5%: Excellent — lead magnet or offer is very strong

**If email capture rate is under 0.5% by Week 3**: Run through this diagnosis:
1. Are the Kit forms actually rendering on the page? (Test in incognito/mobile)
2. Is the form above the fold on the signup page? (Placement issue)
3. Is the offer clear? ("Get weekly modules" is abstract; "Get Module 2 in your inbox tomorrow" is concrete)
4. Are most visitors arriving, seeing the homepage, and immediately leaving? (If yes, the content/CTA mismatch is on the homepage, not the signup page)

---

## Week 4 Checklist (Days 22-28)

**Monitoring goal**: Make data-based decisions for Phase 2 launch timing and priorities.

### Week 4 Full Diagnostic (60 minutes, Wednesday)

This is the comprehensive Week 4 review. All prior weekly checks feed into this one.

#### 4.1 Traffic Summary

GA4 > Reports > Engagement > Overview (date range: last 28 days):

- [ ] Total sessions (28 days): ___
- [ ] Total users (28 days): ___
- [ ] Returning users % (28 days): ___% (above 15% = people are coming back; strong signal for content quality)
- [ ] Average engagement time: ___

**28-day email capture rate**: `total Kit subscribers / total GA4 sessions × 100 = ___%`

#### 4.2 Module Popularity Ranking

GA4 > Explore: rank all module pages by views (last 28 days):

Top 5 modules by views:
1. ___
2. ___
3. ___
4. ___
5. ___

**Decision input**: The most-viewed modules outside the "first module of each path" category are where interest exceeds expectation. In Phase 2 email sequences, prioritize case studies and deep-dives on these modules.

#### 4.3 Path Selection Funnel

GA4 > Explore > Funnel Exploration:
- Step 1: `page_view` on homepage
- Step 2: `path_selection` event
- Step 3: `page_view` on any module
- Step 4: `email_signup_conversion`

This shows exactly where visitors drop off in the funnel from arrival to email signup.

Record:
- [ ] Homepage to path selection conversion rate: ___%
- [ ] Path selection to module read conversion rate: ___%
- [ ] Module read to email signup conversion rate: ___%

**If path selection rate is under 20%**: Homepage CTA is not working. Test Variant B or C from the A/B testing framework.
**If module-to-signup rate is under 1%**: The module pages need better inline CTAs. Add a Kit form embed at the bottom of the top-5 most-viewed modules.

#### 4.4 Mobile vs. Desktop Split

GA4 > Reports > Tech > Tech Overview > Device category:

- [ ] Mobile sessions: ___% of total
- [ ] Desktop sessions: ___% of total
- [ ] Tablet sessions: ___% of total

**Email conversion by device**: In GA4 Explore, break down `email_signup_conversion` by device category.

- [ ] Mobile conversion rate: ___%
- [ ] Desktop conversion rate: ___%

**If mobile conversion rate is more than 40% lower than desktop**: Construction professionals read on mobile (field workers check content between tasks). A poor mobile signup experience is costing you subscribers. Diagnose: test Kit form on mobile, test the signup page load time on a slow connection (use Chrome DevTools Lighthouse > Mobile).

#### 4.5 Email Health Check (Kit Dashboard)

- [ ] Total subscribers at Day 28: ___
- [ ] Welcome sequence open rate (Day 0 email): ___% (target: 40-60%)
- [ ] Welcome sequence open rate (Day 7 email): ___% (target: 30-45%)
- [ ] Unsubscribe rate over 28 days: ___% (concern threshold: above 2% cumulative)
- [ ] Spam complaints (if visible in Kit free dashboard): ___ (target: 0)

**If Day 7 email open rate is below 25%**: The welcome sequence is losing subscribers after Day 0. Possible causes: Day 2 and Day 4 emails were not compelling, or email subject lines are landing in spam. Test: send the Day 4 email to yourself and check if it appears in Gmail Primary (not Promotions/Spam).

#### 4.6 Search Console Check (if 28+ days post-launch)

- [ ] Total impressions from Google Search (last 28 days): ___
- [ ] Total clicks from Google Search: ___
- [ ] Average position for top queries: ___
- [ ] Which queries are driving impressions? Record top 3: ___, ___, ___

**If 0 impressions after 28 days**: Site may not be indexed. In Search Console, request indexing for the homepage via URL Inspection. Verify sitemap.xml is submitted and shows "Success" status.

---

## Week 4 Go/No-Go Decision for Phase 2

After completing the Week 4 diagnostic, make a Phase 2 readiness call:

**Phase 2 GO conditions** (all should be true):
- [ ] GA4 is receiving data without errors
- [ ] At least 1 email subscriber acquired (non-test)
- [ ] Welcome automation is delivering emails correctly (confirmed via test subscriber)
- [ ] Kit forms are rendering on mobile and desktop
- [ ] No critical technical issues (broken pages, 404s on module links, navigation errors)

**Phase 2 WAIT conditions** (fix before starting Phase 2 email infrastructure build):
- [ ] GA4 events not firing (fix snippet first)
- [ ] Kit forms not rendering (diagnose embed code issue)
- [ ] Welcome email going to spam (configure sending domain — see `KIT_ACCOUNT_SETUP_CHECKLIST.md` Step 7)
- [ ] Signup thank-you redirect not working (GA4 conversion data will be missing)

Phase 2 can begin when GO conditions are all checked. Phase 2 is not blocked on traffic levels — it is blocked on infrastructure correctness. Even 5 real subscribers is enough to validate the funnel works.

---

## Ongoing Daily Check Template (Week 5+)

After Phase 1 monitoring is established, reduce to a 5-minute daily check:

```
Date: ___
Kit subscribers today: ___
GA4 sessions (yesterday): ___
Email capture rate (running 7-day): ___%
Any errors or issues: [Yes / No — describe if yes]
Note: ___
```

Track in a simple Google Sheet with one row per day. After 90 days, you will have a trend line that informs Phase 3 decisions (social media channels to prioritize, module content to expand, lead magnet ideas).

---

## Metric Reference Card

Quick lookup for where to find each metric:

| Metric | Where to Find It | Report Path |
|---|---|---|
| Daily active users | GA4 | Reports > Realtime (current), Reports > Engagement > Overview (historical) |
| Module completion proxy | GA4 | Explore > User Explorer (multi-session paths) |
| Email capture rate | Calculate | (Kit subscribers / GA4 sessions) × 100 |
| Bounce analysis | GA4 | Explore > Free Form > Page path + Exits metric |
| Mobile vs. desktop | GA4 | Reports > Tech > Tech overview |
| Module views ranking | GA4 | Reports > Engagement > Pages and screens (filter /modules/) |
| Path selection events | GA4 | Reports > Engagement > Events > path_selection |
| Email signup events | GA4 | Reports > Conversions > email_signup_conversion |
| Welcome email open rate | Kit | Automations > [automation name] > Activity |
| Subscriber count by tag | Kit | Subscribers > Tags view |
| Organic search impressions | Search Console | Performance > Search results |
| Indexing status | Search Console | URL Inspection |

---

## Sources

- [GA4 Reports Overview — Google Analytics Help](https://support.google.com/analytics/answer/11825091)
- [GA4 Explore — Custom Reports and Explorations](https://support.google.com/analytics/answer/7579450)
- [GA4 Funnel Exploration — Google Analytics Help](https://support.google.com/analytics/answer/9327974)
- [Email Marketing Benchmarks for Education — Campaign Monitor 2026](https://www.campaignmonitor.com/resources/guides/email-marketing-benchmarks/)
- [Google Search Console — Indexing and Performance](https://support.google.com/webmasters/answer/9128668)
- [Kit Automation Activity Reporting — Kit Help Center](https://help.kit.com/en/articles/2502557-automation-reporting)
