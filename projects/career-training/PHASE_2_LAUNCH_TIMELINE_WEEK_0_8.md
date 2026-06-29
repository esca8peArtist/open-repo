---
title: "Phase 2 Launch Timeline — Week 0 Through Week 8"
project: career-training
phase: "2"
created: 2026-06-29
status: execution-ready
confidence: 88%
depends_on:
  - PHASE_2_3_EXECUTION_ROADMAP.md
  - EMAIL_SOCIAL_FUNNEL_STRATEGY.md
  - PHASE_2_GROWTH_STRATEGY_AND_COHORT_ANALYSIS.md
---

# Phase 2 Launch Timeline — Week 0 Through Week 8

**Purpose**: Fixed-date 8-week execution calendar covering Kit.com infrastructure, welcome sequence deployment, LinkedIn content launch, and YouTube pre-staging. All dates are expressed as Day-offsets from Phase 1 launch day (D+0). Substitute real calendar dates once the GitHub Pages push is confirmed.

**Starting assumption**: Phase 1 GitHub Pages site is live. Kit account has NOT yet been created. No subscribers exist.

**Confidence**: 88%. Strategy validated in Session 4469 (EMAIL_SOCIAL_FUNNEL_STRATEGY.md, PHASE_2_3_EXECUTION_ROADMAP.md) and platform validated in Session 4467 (PHASE_2_EMAIL_SERVICE_COMPARISON_MATRIX.md, KIT_ACCOUNT_SETUP_CHECKLIST.md). Uncertainty in subscriber projection is ±40% depending on LinkedIn post reach and whether a partnership mention occurs in the window.

---

## Calendar Anchor Table

Fill in this table the day Phase 1 goes live:

| Week | Offset | Calendar Date | Status |
|------|--------|--------------|--------|
| Week 0 (Phase 1 launch) | D+0 | __________ | Awaiting push |
| Week 1 start | D+8 | __________ | |
| Week 2 end | D+21 | __________ | |
| Week 3 start | D+22 | __________ | |
| Week 4 end | D+35 | __________ | |
| Week 5 start | D+36 | __________ | |
| Week 8 end | D+56 | __________ | |

---

## Week 0 — Phase 1 Launch + Days 0-7

**Goal**: Email list capture fully operational. Every visitor who arrives during launch week can subscribe and receive a correct path-specific welcome email within 5 minutes.

**Critical path time budget**: 10-17 hours across Days 0-7 (see PHASE_2_3_EXECUTION_ROADMAP.md time table). Can be done in one focused day if Kit setup is done immediately after the push.

### Milestones

| Milestone | Target Day | PASS Condition | FAIL Condition |
|-----------|-----------|----------------|----------------|
| Kit account created and verified | D+0 | Account active, no credit card entered, email verified | Any paywall prompt during free-tier signup |
| 4 subscriber tags created in Kit | D+0 | All 7 tags exist: `residential-gc`, `industrial-gc`, `specialty-sub`, `generic`, `instructor`, `high-engagement`, `inactive-30d` | Missing any path tag |
| 4 signup forms created in Kit | D+1 | Each form applies correct path tag at subscribe | Any form applying wrong tag |
| Kit forms embedded on GitHub Pages | D+1 | Form renders on `/signup/` page; `/signup-thank-you/` page exists | Blank space where form should appear |
| GA4 conversion event firing | D+1 | `email_signup_conversion` event visible in GA4 Realtime when thank-you page loads | Event absent from GA4 |
| Welcome email copy loaded into Kit | D+2 | Day 0, Day 3, Day 7 emails exist in Kit sequences or automation | Any email slot empty |
| Welcome automation or sequences built | D+2 | Path-routing tested with 1 test subscriber per path | Automation not triggered |
| Full smoke test passed | D+3 | 4 test subscribers (one per form) received correct path-specific welcome email | Any test subscriber received wrong email or no email |
| Day 7 email list capture rate | D+7 | 2%+ of total site sessions have signed up (Kit subscribers / GA4 sessions) | Below 1% after 30+ sessions |

### Day-by-Day Actions — Week 0

**D+0 (Phase 1 push day)**:
- [ ] Verify site is live at GitHub Pages URL
- [ ] Confirm all 38 modules load and render
- [ ] Begin Kit account creation immediately: https://app.kit.com/users/signup
- [ ] Create all 7 subscriber tags (see KIT_ACCOUNT_SETUP_CHECKLIST.md Step 4)
- [ ] Do NOT share the site publicly until Kit forms are live (D+1)

**D+1**:
- [ ] Create 4 Kit signup forms with correct tag assignments (KIT_ACCOUNT_SETUP_CHECKLIST.md Step 5)
- [ ] Copy embed codes for all 4 forms
- [ ] Add embed codes to `docs/signup.md` (see PHASE_1_KIT_COM_INTEGRATION_SETUP.md Part 1)
- [ ] Create `docs/signup-thank-you.md` with GA4 event script
- [ ] Configure post-subscribe redirects in Kit to point to thank-you page
- [ ] Add signup CTAs to: homepage, quick-start page, all three path overview pages
- [ ] Push changes to GitHub Pages
- [ ] Test: submit your own email via each form from the live site; confirm you land on thank-you page

**D+2**:
- [ ] Load WELCOME_SEQUENCE_DRAFT.md email copy into Kit
- [ ] Build path-routing automation OR 4 path-specific sequences (depending on free plan limits — see EMAIL_DELIVERABILITY_TEST_RESULTS.md Section D)
- [ ] Set form success action: enroll subscriber in correct sequence at subscribe time
- [ ] Create test subscriber aliases for smoke test: youraddress+residential@gmail.com, +industrial, +specialty, +generic
- [ ] Run smoke test with each alias (KIT_ACCOUNT_SETUP_CHECKLIST.md Step 8)

**D+3**:
- [ ] Confirm smoke test passed: 4 test subscribers each received path-correct Day 0 email
- [ ] Record automation latency (time from subscribe to email receipt; target: under 5 minutes)
- [ ] Check GA4 Realtime: confirm `email_signup_conversion` event fires when thank-you page loads
- [ ] Begin GA4 analytics setup if not already complete (PHASE_1_GOOGLE_ANALYTICS_SETUP.md)
- [ ] Begin lead magnet PDF creation (California GC Pre-Licensing Checklist) — runs in parallel

**D+4-5**:
- [ ] Complete lead magnet PDF (Canva free plan or Google Docs export to PDF)
- [ ] Upload PDF to `docs/assets/downloads/gclicensing-checklist.pdf`
- [ ] Update Kit form incentive settings: set PDF as post-subscribe incentive for Residential GC and Industrial GC forms
- [ ] Create Google Search Console property; submit sitemap.xml

**D+6-7**:
- [ ] Review 7-day metrics: Kit subscriber count, GA4 sessions, email signup conversion rate
- [ ] Fill in Section 2 of PHASE_2_HANDOFF_DOCUMENT.md (Day 1-7 log)
- [ ] Make Phase 2 direction decision per PHASE_2_HANDOFF_DOCUMENT.md Section 4
- [ ] Share site publicly for first time: personal network (LinkedIn message to 10-20 direct connections in construction)

### Week 0 KPI Targets

| KPI | Target | PASS | FAIL |
|-----|--------|------|------|
| Kit email capture rate (subscribers / sessions) | ≥2% | ≥2% | <1% after 30 sessions with live forms |
| Welcome email delivery latency | <5 min | ≤5 min | >15 min average |
| Spam folder placement rate | 0% | Primary or Promotions tab | Any test email in spam |
| All 4 path tags functioning | 100% | All 4 tags apply at subscribe | Any form tag mismatch |
| GA4 conversion event firing | 100% | Event visible in Realtime | Event missing |

---

## Week 1-2 — Days 8-21: Welcome Sequence Deployment + Baseline Metrics

**Goal**: Welcome sequence delivering correctly to all new subscribers. Baseline metrics established across email, site traffic, and path distribution.

### Milestones

| Milestone | Target Day | PASS Condition | FAIL Condition |
|-----------|-----------|----------------|----------------|
| Welcome email Day 0 open rate | D+14 | ≥35% (industry average for education: 28%) | <25% across all path variants |
| Welcome email Day 3 delivery | D+11 | Delivered within 15 min of D+3 trigger for each subscriber | Not delivered OR delivered to spam |
| Day 3 module click rate | D+14 | ≥20% of Day 0 openers click a module link | <10% module click rate |
| Total subscribers | D+21 | 15-30 subscribers | <10 subscribers after 21 days with live forms |
| Path tag distribution | D+21 | No single path > 75% of list | N/A (informational) |
| Lead magnet downloads | D+21 | ≥1 PDF download per 25 site visitors | 0 downloads after 50 visitors on form pages |

### Week 1 Day-by-Day Actions

**D+8 (Week 1 start)**:
- [ ] Pull Kit dashboard: how many subscribers so far? Check tag distribution.
- [ ] Pull GA4: what are top traffic sources? Which modules got most views?
- [ ] Check PHASE_2_HANDOFF_DOCUMENT.md Section 2.1 metrics for any YELLOW signals
- [ ] Review Day 0 open rate for any real subscribers (Kit > Automations or Sequences > analytics)

**D+9-10**:
- [ ] Check Day 3 email delivery: any real subscribers who joined D+6-7 should receive Day 3 email today. Confirm delivery.
- [ ] Respond to any direct email replies to the welcome sequence (these are gold — a subscriber who replies has extremely high engagement)
- [ ] Complete Google Search Console verification if not done Week 0

**D+11-12**:
- [ ] Compile Week 1 metrics snapshot (PHASE_2_HANDOFF_DOCUMENT.md Section 2.2, Days 8-12)
- [ ] Identify highest-engagement module from GA4 (Pages > by engagement time) — this module gets a LinkedIn post in Week 3-4
- [ ] Second lead magnet: begin Construction Drawing Quick-Reference Card PDF

**D+13-14**:
- [ ] Pull Week 2 metrics: subscriber count, Day 0 open rate, Day 3 click rate
- [ ] Compare against Week 0 KPI targets from PHASE_2_GROWTH_STRATEGY_AND_COHORT_ANALYSIS.md failure triggers
- [ ] Make Day 3 email format decision: if Day 3 open rate < 25%, draft a plain-text variant for A/B testing with next 25 subscribers
- [ ] Share site in first external community: LinkedIn personal post referencing curriculum (NOT a hard sell — share a module insight and mention the curriculum exists)

### Week 2 Day-by-Day Actions

**D+15-17**:
- [ ] Monitor Day 7 welcome email delivery for subscribers who joined Week 1
- [ ] Check Kit: Day 7 email includes LinkedIn link. Note if any clicks occur on that link (early signal of LinkedIn follow conversion).
- [ ] Begin LinkedIn profile optimization (if not done): update headline, about section, featured section (see PHASE_2_3_EXECUTION_ROADMAP.md Track 2)
- [ ] Finish Construction Drawing Quick-Reference Card PDF; add to Kit form incentives for Specialty Sub form

**D+18-21**:
- [ ] Complete Week 1-2 retrospective: fill in metrics template (below)
- [ ] Set up re-engagement automation IF second Kit automation slot is available (EMAIL_DELIVERABILITY_TEST_RESULTS.md Section D established whether free plan supports this)
- [ ] Begin drafting first 5 LinkedIn posts (use case study format: question only, no answer in post)
- [ ] Deploy any subject line A/B test: if 30+ subscribers, test Email 1 subject line variant

### Week 1-2 Metrics Template

Record these values at D+21 (end of Week 2):

```
WEEK 1-2 METRICS SNAPSHOT — D+21
----------------------------------
Total subscribers: ___
  residential-gc tag: ___  (___%)
  industrial-gc tag:  ___  (___%)
  specialty-sub tag:  ___  (___%)
  generic tag:        ___  (___%)

Email performance:
  Day 0 welcome open rate:         ___% (target: ≥35%)
  Day 3 module deep-dive open rate: ___% (target: ≥28%)
  Day 3 module link click rate:    ___% (target: ≥20%)
  Day 7 case study open rate:      ___% (target: ≥28%)
  Any spam folder placements:      [ ] None [ ] Some (investigate)
  Any bounced emails:              [ ] None [ ] Some (___ count)

Site traffic:
  Total sessions D+1 to D+21:      ___
  Email signup conversion rate:    ___% (subscribers / sessions)
  Top 3 modules by page views:     1.___ 2.___ 3.___
  Top traffic source:              ___

PASS/FAIL assessment:
  Email capture rate ≥2%:          [ ] PASS [ ] FAIL
  Day 0 open rate ≥35%:            [ ] PASS [ ] FAIL
  Module click rate ≥20%:          [ ] PASS [ ] FAIL
  15+ subscribers by D+21:         [ ] PASS [ ] FAIL
```

### Week 1-2 Decision Gates

**If email capture rate < 1% at D+21**: Form is not visible enough. Move signup form embed above the fold on the homepage. Add a "subscribe" link to the top navigation bar. Do not proceed to LinkedIn content launch until signup rate improves.

**If Day 0 open rate < 25%**: Subject line or sender name is not resonating. A/B test immediately: keep current subject line for next 15 subscribers, run "Your construction training started" as alternate for next 15. Compare open rates after 30 samples.

**If 0 email replies in first 21 days**: Normal. Do not assume disengagement. First replies typically appear after Day 7 case study email as that email asks an explicit question.

---

## Week 3-4 — Days 22-35: LinkedIn Content Library Launch

**Goal**: LinkedIn posting cadence established at 3x/week. First 20 posts published or scheduled. Referral traffic from LinkedIn visible in GA4 by D+35.

### Milestones

| Milestone | Target Day | PASS Condition | FAIL Condition |
|-----------|-----------|----------------|----------------|
| LinkedIn profile optimized | D+22 | Headline updated, about section edited, site linked | Profile still shows pre-Phase-2 description |
| First 5 LinkedIn posts scheduled | D+24 | Posts queued in Buffer or scheduled in LinkedIn native scheduler | Zero posts queued |
| LinkedIn posting cadence active | D+28 | 3 posts published Week 3 | Fewer than 2 posts in Week 3 |
| LinkedIn referral traffic visible | D+35 | GA4 source "linkedin.com / referral" showing at least 10 sessions | Zero LinkedIn referral sessions after 14 posts |
| New subscribers from LinkedIn | D+35 | At least 3 subscribers whose session source was LinkedIn (GA4 attribution) | Zero LinkedIn-attributed signups |
| Week 3-4 total subscribers | D+35 | 30-60 cumulative | <20 cumulative after 35 days |

### LinkedIn Post Schedule — Week 3-4

Post at **9:00 AM ET** on **Tuesday** and **Thursday**, and at **11:00 AM ET** on **Saturday**. These times are optimized for construction professionals (before site startup / during weekend work planning). All times are Eastern.

**Week 3 Schedule**:

| Day | Date (fill in) | Post Type | Topic | CTA |
|-----|---------------|-----------|-------|-----|
| Tue D+23 | __________ | Case study question | Lien waiver dispute scenario (from workbook) | "Full answer in the curriculum — link in profile" |
| Thu D+25 | __________ | Module excerpt | Cal/OSHA IIPP requirement (Module 14) | "Module 14 is free at [site URL]" |
| Sat D+27 | __________ | Career story | "What it actually takes to get a California GC license" | "CSLB checklist — download at [signup URL]" |

**Week 4 Schedule**:

| Day | Date (fill in) | Post Type | Topic | CTA |
|-----|---------------|-----------|-------|-----|
| Tue D+30 | __________ | Case study question | Change order dispute — who pays? | "Worked answer in the curriculum" |
| Thu D+32 | __________ | Module excerpt | Reading construction drawings — sheet numbering (Module 6) | "Module 6 free at [site URL]" |
| Sat D+34 | __________ | Regulatory update | 2025 California fall protection height change (6 ft trigger) | "Module 14 covers this in detail" |

**Post format for case study posts** (use this template for all 6 of the Week 3-4 case study posts):

```
[SCENARIO TITLE]

[2-3 sentence setup describing the situation]

[The specific decision point — usually 1 clear question]

What would you do?

—

This is from the 150-scenario case study workbook at [site URL].
Module [X] has the full answer. Free access, no account required.

#ConstructionManagement #GCLicense #CaliforniaContractor
```

**Post format for module excerpt posts**:

```
[MODULE NAME / NUMBER]

[1-2 key facts from the module that are surprising or counterintuitive]

[1 actionable takeaway]

Full module at [site URL] — free.

#Construction #CalOSHA #ContractorTraining
```

### LinkedIn CTA Testing Framework — Week 3-4

Track each CTA variant's performance to identify what drives signups vs. engagement:

| CTA Type | Posts Using It | LinkedIn Clicks (LinkedIn native analytics) | Site Sessions from LinkedIn (GA4) | Signups Attributed (GA4 → Kit) |
|----------|---------------|-------------------------------------------|---------------------------------|-------------------------------|
| "Free at [site URL]" | 3 posts | ___ | ___ | ___ |
| "Download checklist at [signup URL]" | 2 posts | ___ | ___ | ___ |
| "Full answer in the curriculum — link in profile" | 1 post | ___ | ___ | ___ |

**Decision rule at D+35**: The CTA type that generates the most signups per post (not most LinkedIn clicks — signups are the target) becomes the default CTA for all subsequent posts.

**LinkedIn engagement floor**: Each post should reach ≥200 impressions (LinkedIn native analytics). If any post reaches fewer than 200 impressions after 48 hours:
- Check: Was it posted at 9:00 AM ET on a weekday?
- Check: Does it contain an external link? LinkedIn suppresses posts with external links early in the post — move site URL to the first comment instead.
- If consistent under 200 impressions across 4+ posts: activate Contingency C from PHASE_2_3_EXECUTION_ROADMAP.md (profile completeness and engagement timing audit).

### Week 3-4 Partnership Outreach — Running Parallel to LinkedIn

Begin partnership outreach emails Week 3. This is the highest-ROI channel per PHASE_2_GROWTH_STRATEGY_AND_COHORT_ANALYSIS.md (50-200 subscribers from a single association mention vs. 3-12 from $300 paid ads).

**Week 3 outreach target**: 10 outreach emails sent by D+35.

Priority targets (in order):
1. CSLB — California Contractors State License Board (cslb.ca.gov) — training resources coordinator
2. AGC California — Associated General Contractors (agcca.org) — member education director
3. CFCA — California Framing Contractors Association — executive director
4. NARI California — National Assoc. of the Remodeling Industry — chapter president
5. 6-7 California community college construction departments (start with Los Angeles Trade Technical College, San Diego City College, Sacramento City College)

**Outreach email format** (use this template exactly — do not deviate):

```
Subject: Free construction training curriculum for [ORGANIZATION] members

Hi [Name],

I've built a free, open-access construction career curriculum — 38 modules 
covering California GC licensing, CSLB compliance, Cal/OSHA requirements, 
lien rights, and career path planning. It's published on GitHub Pages and 
requires no account to access.

I'd like to offer [ORGANIZATION] members a free download of the CSLB 
Pre-Licensing Checklist (1-page PDF covering bond minimums, DIR registration, 
and license classifications) as a member resource, with attribution to you.

No strings attached. If it's useful, I'd appreciate a mention in a future 
member communication or newsletter.

The curriculum is at [SITE URL]. Happy to send a sample module by email 
if that's easier to review.

Best,
[Your name]
[Phone number — construction industry follows up by phone, not email]
```

Track outreach in a simple spreadsheet:

```
Name | Organization | Email | Date Sent | Response | Status | Notes
```

---

## Week 5-8 — Days 36-56: Email Nurture + YouTube Pre-Staging

**Goal**: 300+ subscribers by D+56. Email automation providing path-specific module recommendations. YouTube channel pre-staged for Month 3 launch decision.

### Week 5-6 — Days 36-42

**Email nurture expansion** (primary focus):

- [ ] Launch bi-weekly path-specific digest emails (2x/month per path, not ad-hoc broadcasts)
- [ ] Digest format: 1 module spotlight + 1 case study scenario + 1 regulatory update relevant to path
- [ ] Schedule digests for Tuesday at 9:00 AM ET (matches LinkedIn posting cadence; reinforces consistency signal)
- [ ] Kit subject line A/B test: for each path digest, test informational vs. curiosity-hook subject line

Informational example: "Residential GC digest: Module 9 permit timelines + a change order scenario"
Curiosity-hook example: "The permit took 14 weeks. Here's what the GC did wrong."

Target: curiosity-hook outperforms informational by ≥10 percentage points in open rate within 3 sends.

**LinkedIn: Content performance review**:
- [ ] Pull LinkedIn native analytics: which Week 3-4 posts got the most impressions? Most comments?
- [ ] Cross-reference with GA4 referral report: which posts drove the most site sessions?
- [ ] The intersection (high LinkedIn impressions AND high site sessions) is your best content format
- [ ] Discontinue any content type that drives LinkedIn engagement but zero site sessions (vanity metric)

**Module behavior-based recommendations** (automation if free plan allows, manual if not):

Once 30+ subscribers are tagged with module visit activity, segment subscribers by behavior:

- Subscribers who clicked Module 14 link (safety) → next recommendation: Module 36 (Safety Program Design)
- Subscribers who clicked Module 13 link (lien rights) → next recommendation: Module 12 (GC Business Setup)
- Subscribers who clicked Module 7 link (residential GC scope) → next recommendation: Module 8 (Residential Estimating)

If Kit free plan supports link-click triggers in automations, build this as an automation action: "when subscriber clicks [link X] → add tag `module-X-visited` → send recommendation email after 3 days." If branching is unavailable, send these as manual broadcasts segmented by tag.

**Week 5-6 milestones**:

| Milestone | Target Day | PASS | FAIL |
|-----------|-----------|------|------|
| First bi-weekly digest sent | D+36 | Sent to correct path segments | Not sent |
| Digest open rate | D+40 | ≥28% (education ESP average) | <20% for 2 consecutive sends |
| Partnership responses received | D+42 | ≥1 active conversation from 10 outreach emails | 0 responses after 20 emails |
| Total subscribers | D+42 | 75-150 | <50 |
| LinkedIn followers | D+42 | 50+ | <20 after 18 posts |

### Week 7-8 — Days 43-56

**Email nurture: re-engagement sequence**:

- [ ] Deploy re-engagement automation for subscribers who have not opened any email in 30 days
- [ ] Re-engagement email subject: "Still interested in construction training?" (plain text, 3 sentences maximum)
- [ ] Wait 7 days after re-engagement email; if no open, tag `inactive-30d` and pause all sends for that subscriber
- [ ] Track re-engagement rate: target ≥15% of inactive subscribers re-engaging after the single re-engagement email

**YouTube channel pre-staging (go/no-go decision at D+56)**:

The YouTube decision gate is at D+56. Pre-stage the channel during Week 7-8 so you can launch immediately if criteria are met.

Pre-staging tasks (do these regardless of go/no-go decision):
- [ ] Create YouTube channel: use the same brand name as the LinkedIn page
- [ ] Write channel description (under 250 words): "38-module construction career curriculum — free access, California-focused, covering GC licensing, CSLB compliance, Cal/OSHA, lien rights, and career paths for residential GCs, industrial GCs, and specialty subs. Weekly videos covering module topics."
- [ ] Set channel art to match LinkedIn profile visuals (consistent brand signal)
- [ ] Draft titles and outlines for first 3 videos (do NOT record yet):
  - Video 1: "How to Read Construction Drawings — Module 6 Overview" (target: 10-12 min)
  - Video 2: "California GC License Explained — What CSLB Actually Requires" (target: 12-15 min)
  - Video 3: "Which Career Path? Residential GC vs. Industrial GC vs. Specialty Sub" (target: 8-10 min)
- [ ] Identify recording equipment minimum: USB microphone ($50-80), ring light or window light, clean background

**D+56 YouTube go/no-go decision** (all criteria must be met to proceed):

| Criterion | Target | Actual | Go? |
|-----------|--------|--------|-----|
| LinkedIn producing 25+ site clicks/week | ≥25 clicks/week consistent | ___ | [ ] Go [ ] No-go |
| Email list size | ≥100 subscribers | ___ | [ ] Go [ ] No-go |
| Bi-weekly digest open rate | ≥28% sustained | ___% | [ ] Go [ ] No-go |
| Video production commitment | 2 videos/month minimum | [ ] Yes [ ] No | [ ] Go [ ] No-go |

**If any criterion is NO-GO**: Defer YouTube to D+84 (Month 3 review). Stay LinkedIn-only. Adding a platform you cannot sustain is worse than not having it. Revisit at D+84 with updated metrics.

**If ALL criteria are GO**: Begin recording Video 1 in Week 9. Publish in Week 11-12 (allow time for editing and thumbnail creation).

### Week 5-8 Subscriber Target — 300+

The 300+ subscriber target at D+56 requires contribution from multiple channels:

| Channel | Projected D+56 Subscribers | Assumptions |
|---------|---------------------------|-------------|
| LinkedIn referral | 50-100 | 18 posts; 1-3% of post impressions click through; 5-8% signup rate |
| Direct/word-of-mouth | 20-40 | 10-20 direct shares from personal network |
| Partnership mention (1) | 50-150 | If 1 association mention occurs; 3-5% signup rate from newsletter |
| Reddit seeding | 20-60 | 2-3 posts in r/Construction, r/generalcontractor; 1 resonant post drives 100-500 visits |
| Welcome email referral loop | 10-30 | Subscribers sharing Day 7 case study email to their LinkedIn networks |

**If 300 is not reached by D+56**: Per PHASE_2_3_EXECUTION_ROADMAP.md Decision Point 2, this is not a failure trigger unless total subscribers are below 75. At 75-300 subscribers, the issue is traffic volume, not conversion. Double LinkedIn posting cadence to 5x/week and invest 5 additional hours in Reddit seeding before considering any paid acquisition.

---

## Decision Gate Map — Full 8-Week View

| Gate | Trigger Day | Decision | Criteria | Output |
|------|------------|----------|----------|--------|
| Gate 0 | D+3 | Kit smoke test | 4 test emails delivered correctly | Proceed / Fix automation |
| Gate 1 | D+7 | Week 0 capture rate | ≥2% email capture | Proceed / Fix form visibility |
| Gate 2 | D+14 | Welcome sequence health | Day 0 open rate ≥35% | Proceed / Revise subject lines |
| Gate 3 | D+21 | LinkedIn launch | ≥15 subscribers, forms working | Proceed / Fix email first |
| Gate 4 | D+35 | LinkedIn CTA test result | Best-performing CTA identified | Lock in CTA format for remaining posts |
| Gate 5 | D+42 | Partnership outreach | ≥1 response from 10 emails | Continue / Personalize deeper |
| Gate 6 | D+56 | YouTube go/no-go | All 4 criteria met | Launch Month 3 / Defer YouTube |

---

## KPI Summary Table — Full 8 Weeks

| KPI | D+7 Target | D+21 Target | D+35 Target | D+56 Target | Source |
|-----|-----------|-------------|-------------|-------------|--------|
| Total subscribers | 5-15 | 15-30 | 30-60 | 300+ | PHASE_2_3_EXECUTION_ROADMAP.md 30/60/90 targets |
| Email capture rate | ≥2% | ≥2% | ≥3% | ≥4% | PHASE_2_ENROLLMENT_FUNNEL_ARCHITECTURE.md Stage 2 |
| Day 0 open rate | N/A | ≥35% | ≥35% | ≥35% | EMAIL_SOCIAL_FUNNEL_STRATEGY.md cohort benchmarks |
| Module click rate (Day 3 email) | N/A | ≥20% | ≥20% | ≥20% | PHASE_2_ENROLLMENT_FUNNEL_ARCHITECTURE.md Stage 2B |
| Bi-weekly digest open rate | N/A | N/A | N/A | ≥28% | Education ESP average (EmailToolTester 2026) |
| LinkedIn posts published | 0 | 0 | 6 | 18 | EMAIL_SOCIAL_FUNNEL_STRATEGY.md 90-day plan |
| LinkedIn referral sessions (GA4) | 0 | 0 | ≥10 | ≥50 | PHASE_2_3_EXECUTION_ROADMAP.md Track 1 |
| Partnership emails sent | 0 | 0 | 10 | 20 | PHASE_2_GROWTH_STRATEGY_AND_COHORT_ANALYSIS.md Week 3 |
| Partnership responses | 0 | 0 | 0-1 | 1-3 | PHASE_2_3_EXECUTION_ROADMAP.md Track 3 |
| YouTube channel staged | No | No | No | Yes (pre-stage) | This document Week 7-8 |

---

## Sources

- PHASE_2_3_EXECUTION_ROADMAP.md — phase timeline, parallel tracks, decision points
- EMAIL_SOCIAL_FUNNEL_STRATEGY.md — welcome sequence design, LinkedIn strategy, cohort benchmarks
- PHASE_2_GROWTH_STRATEGY_AND_COHORT_ANALYSIS.md — channel ROI projections, persona definitions
- PHASE_2_ENROLLMENT_FUNNEL_ARCHITECTURE.md — funnel metrics, Stage 2A/2B targets
- KIT_ACCOUNT_SETUP_CHECKLIST.md — Kit setup procedures and feature audit
- PHASE_1_KIT_COM_INTEGRATION_SETUP.md — form embedding, automation specification
- EMAIL_DELIVERABILITY_TEST_RESULTS.md — automation constraint findings
- WELCOME_SEQUENCE_DRAFT.md — email copy ready for Kit loading
- PHASE_2_HANDOFF_DOCUMENT.md — Phase 1 launch record and Week 1 monitoring framework
- [LinkedIn Construction Industry Engagement — LinkedIn Marketing Blog](https://www.linkedin.com/business/marketing/blog/linkedin-ads/best-linkedin-ad-targeting-options)
- [Email Marketing Benchmarks for Education 2026 — EmailToolTester](https://www.emailtooltester.com/en/blog/email-marketing-benchmarks/)
- [YouTube Growth: First 100 Subscribers — Buffer](https://buffer.com/resources/creator-growth-playbook/)
