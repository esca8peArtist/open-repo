---
title: "Phase 2 Handoff Document — Week 1 Monitoring and Phase 2 Decision Gates"
project: career-training
phase: "1-to-2 transition"
created: 2026-06-29
status: ready-for-use-post-deployment
trigger: "Complete POST_DEPLOYMENT_VERIFICATION_CHECKLIST.md first, then use this document Week 1"
---

# Phase 2 Handoff Document

**Purpose**: Track what happened in Phase 1 launch, establish Week 1 baselines, and define the exact triggers that determine Phase 2 direction. This is a living document — fill in the blanks as you go.

**When to use this**: Start filling in Section 1 immediately after the first successful deploy. Fill in Section 2 during Days 1-7. Make the Phase 2 decision at the end of Day 7 using Section 3.

---

## Section 1 — Phase 1 Launch Record

### 1.1 Deployment facts

Fill in immediately after first successful deploy:

| Field | Value |
|-------|-------|
| First successful deploy date/time | |
| Platform (GitHub Pages / Netlify / Vercel) | |
| Custom domain live? | [ ] Yes [ ] Not yet |
| GA4 tracking confirmed live? | [ ] Yes [ ] No |
| Kit signup forms live? | [ ] Yes [ ] Placeholder |
| Modules 37-38 included in site? | [ ] Yes [ ] Excluded from Phase 1 |
| Lighthouse performance score (mobile, homepage) | |

### 1.2 What worked better than expected

Write a sentence or two on anything that was easier, faster, or better than planned. This helps scope Phase 2 estimates accurately.

```
[Fill in after deploy — e.g., "Jekyll build was faster than expected (12 seconds). 
Netlify rollback to alternative took 22 minutes not 30. 
Just the Docs sidebar loaded with zero extra configuration."]
```

### 1.3 What was harder than expected or produced surprises

Write a sentence or two on unexpected friction. These are the items most likely to need attention in Phase 2.

```
[Fill in after deploy — e.g., "GA4 production guard meant I could not verify tracking 
locally at all — had to wait for a live deploy to confirm. 
Kit confirmation email landed in spam 2/3 test attempts."]
```

### 1.4 What would be done differently

If you were doing a Phase 2 site from scratch tomorrow, what would you change?

```
[Fill in after deploy — e.g., "Would set up GA4 property and get Measurement ID 
before touching Jekyll config at all. Would use Netlify from the start instead 
of GitHub Pages."]
```

### 1.5 Open issues entering Phase 2

List any known issues, deferred fixes, or technical debt from Phase 1 that need Phase 2 attention. Examples:

- [ ] Kit signup forms are placeholder — need live forms wired up
- [ ] Modules 37-38 were excluded from Phase 1 — decision needed on including in Phase 2
- [ ] Lighthouse performance score below 70 on mobile — optimize before paid traffic
- [ ] Custom domain not yet configured — using GitHub Pages default URL
- [ ] GA4 custom dimensions not yet configured (user_segment, learning_path, module_number)
- [ ] `signup-thank-you` page not created — Kit redirects to Kit default after sign-up

---

## Section 2 — Week 1 Monitoring (Days 1-7)

### 2.1 How to check your metrics

**GA4 daily check** (takes 5 minutes):
1. Go to [analytics.google.com](https://analytics.google.com) and select your Construction Career Training property
2. Click Reports > Overview for top-level numbers
3. Key metrics to note daily:
   - Users (unique visitors for the day)
   - Sessions (total visits including repeat)
   - Engagement rate (% of sessions where someone actually did something — scrolled, clicked)
   - Pages per session (are people reading more than one page?)

**Kit subscriber check** (takes 2 minutes):
1. Go to [app.kit.com](https://app.kit.com)
2. Main dashboard shows subscriber count and recent signups
3. Note total subscribers and any new signups for the day

**Save these numbers** in the daily log below, every day for Days 1-7.

---

### 2.2 Daily log — Days 1-7

Copy this row for each day:

```
Day N | Date: YYYY-MM-DD | Users: ___ | Sessions: ___ | Engagement rate: ___% 
      | New Kit subscribers: ___ | Cumulative subscribers: ___
      | Notable events: [any traffic spike, link shared somewhere, etc.]
```

---

Day 1 | Date: ___________ | Users: ___ | Sessions: ___ | Engagement rate: ___%  
      | New Kit subscribers: ___ | Cumulative subscribers: ___  
      | Notable events: ___

Day 2 | Date: ___________ | Users: ___ | Sessions: ___ | Engagement rate: ___%  
      | New Kit subscribers: ___ | Cumulative subscribers: ___  
      | Notable events: ___

Day 3 | Date: ___________ | Users: ___ | Sessions: ___ | Engagement rate: ___%  
      | New Kit subscribers: ___ | Cumulative subscribers: ___  
      | Notable events: ___

Day 4 | Date: ___________ | Users: ___ | Sessions: ___ | Engagement rate: ___%  
      | New Kit subscribers: ___ | Cumulative subscribers: ___  
      | Notable events: ___

Day 5 | Date: ___________ | Users: ___ | Sessions: ___ | Engagement rate: ___%  
      | New Kit subscribers: ___ | Cumulative subscribers: ___  
      | Notable events: ___

Day 6 | Date: ___________ | Users: ___ | Sessions: ___ | Engagement rate: ___%  
      | New Kit subscribers: ___ | Cumulative subscribers: ___  
      | Notable events: ___

Day 7 | Date: ___________ | Users: ___ | Sessions: ___ | Engagement rate: ___%  
      | New Kit subscribers: ___ | Cumulative subscribers: ___  
      | Notable events: ___

---

### 2.3 Establishing baselines

After Day 3, calculate a 3-day baseline. This is your reference point for the YELLOW/RED triggers.

**Day 1-3 average daily users**: _______

**Day 1-3 average daily Kit signups**: _______

**Day 1-3 email signup conversion rate**:
- Formula: (Total Kit subscribers after 3 days) / (Total sessions Days 1-3) × 100
- Expected range: 3-8%
- Your result: _______%

**Day 1-3 average engagement rate**: _______%

Fill in once baseline is calculated:

| Metric | Day 1-3 Baseline | YELLOW threshold | RED threshold |
|--------|-----------------|-----------------|---------------|
| Daily users | `[fill in]` | < 80% of baseline | < 50% of baseline |
| Kit signup conversion | `[fill in]` | < 2% | 10+ days with 0 signups |
| Mobile bounce rate | `[fill in]` | > 60% | > 75% |
| Any module > avg engagement | `[fill in]` | any module < 10% of avg | — |

---

## Section 3 — Monitoring Triggers (YELLOW and RED alerts)

### 3.1 Daily Active Users

**Context**: In Week 1 you will not have much organic traffic unless you actively shared the site. "Daily users" in Week 1 mainly reflects word-of-mouth and any direct links you share. This is normal. The baseline is what YOU generate in Days 1-3, not an absolute number.

**YELLOW signal** — Investigate if Week 2 average is less than 80% of the Day 1-3 baseline:
- If Days 1-3 averaged 25 users/day and Week 2 drops to under 20, investigate
- Most likely cause: you stopped sharing the link. Resolution: resume sharing.
- Not a technical failure if traffic drops when sharing stops.

**RED signal** — Traffic drops to near-zero (under 5 users/day) for 3+ consecutive days with no change in your sharing behavior:
- Check GA4 is still tracking: revisit Check 6 of `POST_DEPLOYMENT_VERIFICATION_CHECKLIST.md`
- Check the site is still live: visit `[SITE_URL]` from a different device
- Check GitHub Pages status page: [githubstatus.com](https://githubstatus.com) — Pages section
- If site is down: activate `GITHUB_PAGES_ROLLBACK_PROCEDURES.md`

---

### 3.2 Module Content Engagement

**Context**: "Module completion" is hard to measure without custom JavaScript. Use GA4's "average engagement time" per page as a proxy — if someone is on a module page for less than 60 seconds, they probably did not read it.

**How to check in GA4**:
1. Reports > Engagement > Pages and screens
2. Sort by "Average engagement time" ascending
3. Look for module pages with very low average time (under 30 seconds)

**YELLOW signal** — Any module page has average engagement time under 30 seconds AND more than 10 visitors:
- Content may be confusing, off-target for audience, or technically broken
- Click the module name in GA4 to see the full path report — are users leaving immediately or navigating elsewhere?
- Read the module yourself with fresh eyes — does the opening paragraph clearly state what the reader will get?

**RED signal** — The signup page (`/signup/`) has very high traffic (top 5 pages) but 0 subscribers:
- Form is broken, not rendering, or confirmation email is going to spam
- Re-run Check 5 of `POST_DEPLOYMENT_VERIFICATION_CHECKLIST.md`
- Submit a test subscription yourself from Incognito mode to diagnose

---

### 3.3 Email Signup Conversion Rate

**Formula**: (Kit subscribers confirmed) / (Total site sessions) × 100 = conversion rate

**Context**: For organic traffic with no paid ads and no email marketing, expect 1-4% of visitors to sign up. A higher rate indicates the content and audience targeting are well-aligned. A lower rate can mean many things (wrong audience, form not working, "coming soon" placeholder still in place).

**Expected range for Week 1**: 1-8% depending on how warm the initial traffic is. If you shared the link in a construction professional community where members know you, expect the high end (5-10%). If traffic is cold (strangers), expect the low end (1-3%).

**YELLOW signal** — Conversion rate below 2% after 50+ sessions with live Kit forms:
- Investigate whether the signup page is being visited (GA4 > Pages > `/signup/`)
- If signup page visits are under 5% of total sessions, the CTA links in module pages are not driving traffic to the form
- Check that module pages contain visible "Sign up" CTA links (not buried at the bottom)
- If signup page IS getting traffic but not converting: re-read the signup page copy — is the value proposition clear?

**RED signal** — 10 or more consecutive days pass after launch with zero new Kit subscribers:
- First: confirm the site has live Kit forms (not a placeholder)
- If placeholder: this is expected — resolve Kit setup and add live forms
- If live forms: re-run Check 5 (form submission end-to-end test)
- Contact Kit support if submission works but no subscribers appear

---

### 3.4 Mobile Usability

**Context**: Construction professionals increasingly use phones to access training content during commutes, lunch breaks, or on job sites. If the mobile experience is poor, you will see high mobile bounce rates.

**How to check in GA4**:
1. Reports > Demographics and Tech > Tech details
2. Filter by "Device category = mobile"
3. Note the engagement rate and bounce rate for mobile users specifically

**YELLOW signal** — Mobile bounce rate above 60% (users arrive on mobile and immediately leave):
- Test the site on your own phone (real device, not DevTools)
- Is there a horizontal scroll? Are text and buttons too small?
- Consider: is the content accessible on mobile or does it assume a desktop with a wide screen?

**RED signal** — Mobile bounce rate above 75% sustained over 3+ days:
- This indicates a consistent UX problem, not an outlier
- Run Lighthouse on mobile (Check 10 from `POST_DEPLOYMENT_VERIFICATION_CHECKLIST.md`) and look at the specific issues reported
- If Just the Docs theme is loading correctly, mobile layout should be handled — a very high bounce rate may indicate content load time problems (Performance score below 50) rather than layout

---

## Section 4 — Phase 2 Decision Gates

At the end of Day 7, use this section to decide Phase 2 direction.

### 4.1 Phase 2 trigger criteria

**Full Phase 2 activation** — proceed to `PHASE_2_3_EXECUTION_ROADMAP.md` when ALL of these are true:

- [ ] Week 1 data collected (at least 7 days of GA4 data)
- [ ] At least 3 confirmed Kit subscribers (real people, not your test submissions)
- [ ] Site has been up continuously for 7 days without deployment issues
- [ ] Verification checklist: all critical checks PASS (no unresolved Check 1, 2, 5, or 6 failures)
- [ ] You have personally read through 3 different modules on the live site and confirmed the experience

**Partial Phase 2** — Begin Phase 2 planning but hold distribution spend until resolved:

- [ ] Week 1 data shows engagement rate above 30% (people reading, not just bouncing)
- [ ] Kit setup is complete (live forms, not placeholder)
- [ ] No RED signals triggered in Section 3

**Phase 2 deferred** — Resolve Phase 1 issues before Phase 2 investment:

- Any RED signal is active
- Site was down for more than 24 hours in Week 1
- Zero Kit subscribers after 14 days with live forms
- Lighthouse accessibility score below 70

---

### 4.2 Phase 2 options and what Week 1 data tells you

**Option A: Email platform deepening**
Pursue if: Kit conversion rate is 3%+ and subscribers are engaging with welcome sequence (check Kit's email open rate — target >30%).
Next step: Set up Kit automation sequences per `PHASE_2_3_EXECUTION_ROADMAP.md`, create lead magnets (PDF versions of top modules).

**Option B: Social media distribution**
Pursue if: Traffic is low but engagement rate on site is high (>50%) — people who find the site like it, but not enough people are finding it.
Next step: Choose 1-2 platforms where construction professionals concentrate (LinkedIn, Reddit r/Construction, YouTube), create 3-5 posts sharing module excerpts as "tips," measure traffic lift.

**Option C: Paid traffic test**
Pursue if: Organic traffic is too slow to get statistically significant data, and you have budget ($50-150 test).
Prerequisite: Kit forms must be live (not placeholder). GA4 conversion tracking must be working. Without tracking, you cannot measure ROAS.
Channels to test in order: Google Search Ads (intent-based, highest quality), LinkedIn (professional audience, expensive), Meta (cheap traffic, lower intent).

**Option D: Content deepening**
Pursue if: High engagement rate on specific modules, clear appetite for more depth.
Modules with the highest average engagement time (GA4 Pages report) are candidates for expansion, spin-off modules, or companion resources (printable checklists, video walkthroughs).

---

### 4.3 Day 7 Phase 2 decision log

Fill in at end of Week 1:

- Week 1 total users: ___
- Week 1 total Kit subscribers: ___
- Week 1 email signup conversion rate: ___%
- Highest-engagement module: ___
- Lowest-engagement module: ___
- Any RED signals triggered: [ ] Yes (which: ___) [ ] No
- Any YELLOW signals triggered: [ ] Yes (which: ___) [ ] No
- Platform stability: [ ] No downtime [ ] Brief downtime (resolved) [ ] Extended downtime
- Phase 2 decision: [ ] Option A [ ] Option B [ ] Option C [ ] Option D [ ] Multiple [ ] Deferred
- Phase 2 start date: ___________
- Next review checkpoint: Day 30 (___________) — full Month 1 analysis

---

## Section 5 — Netlify Migration Reference (if GitHub Pages proves unreliable)

If GitHub Pages produces two or more deployment failures within the first 30 days, migrate to Netlify. The migration is documented fully in `GITHUB_PAGES_ROLLBACK_PROCEDURES.md` Option A.

**Migration is not a failure**. Netlify is a superior platform for teams who prioritize reliability over simplicity. The trade-off is a slightly more complex setup — which is already documented and requires 30 minutes.

**Triggers for migration decision** (choose any):
- [ ] Two or more GitHub Pages deployment failures requiring manual intervention in 30 days
- [ ] GitHub Pages build takes more than 5 minutes consistently (Netlify is typically 60-90 seconds for this site)
- [ ] GitHub Pages custom domain configuration produces repeated SSL certificate errors
- [ ] You want deploy previews (Netlify's "Deploy Preview" feature — GitHub Pages does not have this)

**Migration steps**: See `GITHUB_PAGES_ROLLBACK_PROCEDURES.md` > Option A. Archive this decision in Section 1.3 of this document.

---

## Document Maintenance

This document is intended to be filled in progressively during Week 1. It is not a set-and-forget file. If you find it useful, copy it for Phase 2 with updated baseline metrics and adjusted triggers. Phase 2 targets will be higher — adjust thresholds once Week 1 establishes what "normal" looks like for this specific audience and content.
