---
title: "Phase 2 Enrollment Funnel Architecture"
project: career-training
phase: "2"
created: 2026-06-29
status: planning
confidence: 75%
depends_on:
  - PHASE_1_AB_TESTING_FRAMEWORK.md
  - PHASE_1_KIT_COM_INTEGRATION_SETUP.md
  - PHASE_1_GOOGLE_ANALYTICS_SETUP.md
---

# Phase 2 Enrollment Funnel Architecture

**Scope**: Five-stage enrollment funnel from first site visit to paid conversion and advocacy. Each stage has defined entry criteria, target conversion rates, measurement methods, success definitions, and failure triggers. Includes A/B testing framework integration and Week-1 measurement checklist.

**Operating context**: Static GitHub Pages site. No native LMS. Measurement via GA4 events + Kit email analytics + UTM parameter tracking. No server-side code. All funnel stages are measurable without a backend.

---

## Funnel Overview

```
Stage 1: AWARENESS
Landing page visit, CTA engagement
         ↓  (target: 3-5% CTA click)
Stage 2: ACTIVATION
Email signup, first module completion
         ↓  (target: 5-10% of visitors → email signup; 40-60% of signups → first module)
Stage 3: RETENTION
Module sequence completion, email open cadence, community participation
         ↓  (target: 15-25% complete 5+ modules; 30-40% open rate)
Stage 4: REVENUE
Certification purchase, instructor session booking, institutional license
         ↓  (target: 2-5% of active email list converts to paid)
Stage 5: ADVOCACY
NPS 50+, referral signups, instructor recruitment, alumni case studies
```

Revenue does not precede Retention. No paid product should be offered until the learner has completed at least one module and opened at least two emails. Premature monetization is the single most common failure mode in freemium education platforms.

---

## Stage 1: Awareness

**Definition**: The visitor lands on any page of the site. They do not need to click a CTA to be "in" Stage 1.

**Primary entry points (by projected traffic volume)**:
1. LinkedIn post referral (high volume in Months 1-4; drops off without posting cadence)
2. Partnership newsletter mention (spike traffic, highest signup conversion)
3. Reddit post referral (unpredictable; can be 50 visits or 1,000 visits from a single post)
4. Organic search (negligible in Months 1-4; grows after Month 5 for long-tail terms)
5. Direct/dark social (existing contacts; highest conversion; can't measure accurately)

### CTAs Under Test

Three CTAs are being A/B tested per PHASE_1_AB_TESTING_FRAMEWORK.md:

| Variant | CTA Text | Value Proposition |
|---------|----------|-------------------|
| A (control) | "Start with your path" | Structured learning entry |
| B | "Free module library — browse 33 modules" | Zero-commitment exploration |
| C | "Get certified — complete your path" | Credential / career signal |

**Expected performance by persona**:
- Learner persona: Variant B likely outperforms (exploration framing reduces friction)
- Contractor persona: Variant C likely outperforms (certification = business legitimacy)
- Instructor persona: Neither B nor C speaks to their use case; they need a fourth CTA variant ("Use this curriculum in your classroom") added in Phase 2 when instructor-specific landing page is live

**Established benchmark**: Kit/ConvertKit's own published data on email CTA testing shows 10-20% lift from subject-line and CTA personalization in educational email sequences. Independent A/B research (ConversionXL, Unbounce) shows CTA button copy that leads with the user's desired outcome ("Get certified") outperforms generic action verbs ("Learn more") by 14-30% in education contexts.

### Stage 1 Metrics

| Metric | Target | Measurement Method | Success | Failure Trigger |
|--------|--------|--------------------|---------|-----------------|
| Bounce rate (homepage) | Below 50% | GA4 engagement rate (sessions with 10s+ or 2+ pages) | 50%+ engaged sessions | Over 60% bounce at 1,000+ sessions |
| CTA click-through rate | 3-5% of sessions | GA4 `path_selection` event count / sessions | Any variant reaching 4%+ CTR | All variants below 2% after 200 sessions each |
| Average time on page (homepage) | 90+ seconds | GA4 engagement time | 90-120s average | Below 45s across all traffic |
| Top traffic source | Partnership + LinkedIn combined: 50%+ of visits | GA4 Acquisition report (Source/Medium) | Clear dominant channel | No single channel exceeds 20% (signals all channels weak) |

**Failure trigger — Stage 1**: If bounce rate exceeds 60% at 1,000+ total sessions and CTA click-through is below 2% across all variants, the problem is audience-message mismatch, not a specific CTA. Audit the traffic source first: if Reddit is driving the bounce, the Reddit post is attracting the wrong audience. If LinkedIn is driving the bounce, the LinkedIn post's promise does not match the landing page.

---

## Stage 2: Activation

**Definition**: A visitor becomes an activated user by (a) submitting an email signup form AND (b) completing their first module (clicked any module link from any email or site page within 14 days of signup).

Two sub-stages:
- **Activation 2A**: Email signup (passive activation — they have provided contact info but have not engaged with content)
- **Activation 2B**: First module completion (active activation — they have consumed at least one content unit)

Both thresholds matter. A subscriber who signs up and never reads a module is Stage 2A-only and has a high churn probability. Stage 2B activation is the reliable predictor of 60-day retention.

### Email Signup Rate (Stage 2A)

**Target**: 5-10% of all site visitors submit an email signup form.

**Benchmark context**: Average website-to-free-signup conversion is 2-5% across all industries. Education platforms with high-intent audiences and free lead magnets perform at the upper end: 5-8% is typical for a free curriculum with a relevant lead magnet. The California GC Pre-Licensing Checklist (Tier 1 lead magnet) should push conversion into the 6-10% range for visitors who arrive from construction-specific sources, since the checklist directly solves a painful known question (CSLB licensing requirements).

**Placement A/B test** (per PHASE_1_AB_TESTING_FRAMEWORK.md Test 2): Three form placements are being tested: bottom of homepage (control), mid-page after path descriptions, and scroll-triggered modal at 60% depth. Mid-page placement typically outperforms bottom-of-page for engaged audiences (this audience is task-oriented, not impulsive; they want to know what they are signing up for before they sign up). Expect mid-page to outperform bottom-of-page by 15-30%.

**Kit tag applied at Stage 2A**: One of `path-industrial`, `path-residential`, `path-specialty-sub`, `path-instructor`, or `path-untagged`. Tag accuracy determines the relevance of every subsequent email.

### First Module Completion (Stage 2B)

**Target**: 40-60% of email signups click and read their first module within 14 days of signup.

**How it is measured**: Kit link tracking on the module link in the Day 4 case study email. When a subscriber clicks the module link, the Kit automation applies the tag `module-1-visited`. This does not confirm the full module was read, but it confirms engagement beyond the inbox. Note: this is a proxy metric, not a true completion signal. Accept this limitation — a static site without a login system cannot track read completion.

**The Day 4 email is the critical activation lever**: The welcome sequence is designed with the Day 4 case study email as the mechanism that drives first module engagement. It presents a scenario ("How would you handle this?") and links to the module that contains the answer. This is more effective than a direct "Read Module 1" call-to-action because it creates genuine curiosity pull rather than instructional compliance.

**Expected activation funnel shape**:

```
1,000 site visitors
    → 60-80 email signups (6-8% signup rate)
        → 24-48 first module visits (40-60% of signups within 14 days)
            → 9-20 subscribers still active at Day 30 (15-25% of signups reach 5+ modules)
```

### Stage 2 Metrics

| Metric | Target | Measurement | Success | Failure Trigger |
|--------|--------|-------------|---------|-----------------|
| Email signup rate (2A) | 5-10% of visitors | Kit subscriber count / GA4 sessions | 7%+ sustained | Below 3% at 500+ sessions |
| First module visit rate (2B) | 40-60% of signups | Kit `module-1-visited` tag count / total signups | 50%+ | Below 25% after 50 signups |
| Form completion by path | Roughly even split across 3 paths | Kit subscriber counts by tag | No single path > 70% of list | Not a failure trigger; just signals audience composition |
| Lead magnet download rate | 2-5% of site visitors | GA4 `/signup-thank-you/` page views with `form=*` parameter | 3%+ | Below 1% after 300 visitors |

**Failure trigger — Stage 2A (email signup)**: If signup rate is below 3% after 500 sessions, the lead magnet is not visible or not compelling enough. First fix: move the lead magnet above the fold on the homepage. Second fix: change the lead magnet offer (try the "5 Case Study Sampler" if the "Pre-Licensing Checklist" is not converting).

**Failure trigger — Stage 2B (module visit)**: If first module visit rate falls below 25% after 50 signups, audit the Day 4 email. Most likely problem: the case study in the email is not interesting enough to create curiosity pull, or the "see the answer" link is not prominent. Test a plain-text Day 4 email vs. the formatted version; plain text typically outperforms in early list stages when the audience does not yet trust the sender.

---

## Stage 3: Retention

**Definition**: A subscriber who has completed 5+ modules and maintains an active email engagement status (opened at least one email in the prior 30 days).

**Why 5 modules is the threshold**: At 5 modules, a learner has made a measurable commitment of time (each module is approximately 45-90 minutes of reading; 5 modules = 4-8 hours). They have passed the "exploration" phase and entered the "using it" phase. Data from comparable self-paced platforms (Ruzuku completion gap research) shows that learners who reach the 5-module mark complete their chosen path at 3-4x the rate of learners who stop at 1-2 modules.

**Weekly active user definition**: A subscriber who has opened at least one email in the prior 7 days OR visited the site from an email link in the prior 7 days. Tracked in Kit by the `engagement-active` tag.

### Retention Mechanics

**Streak tracking**: The curriculum does not have a native streak mechanism (no login system). The email sequence substitutes: bi-weekly path-specific digests arriving on a predictable schedule serve as the streak signal. A subscriber who opens every digest is functionally on a "streak" in terms of re-engagement cadence. Kit's "opened at least X emails in last 30 days" segment identifies active streakers.

**Completion badges**: Digital badges issued via email (a graphic sent in the email when a subscriber self-reports reaching a phase milestone). The mechanism: Day 30 "check-in" email asks "Which phase are you on?" A click on "Phase 1 complete" triggers a Kit automation that sends a badge email and tags the subscriber `phase-1-complete`. This requires no backend — it uses Kit's click-to-tag automation.

**Weekly digest**: The bi-weekly digest (2x/month per path) is the primary retention mechanism. Format: one module spotlight, one case study question, one regulatory update relevant to their path. Optimized subject lines tested per path:
- Residential GC digest: "This week: California ADU permits + a change order scenario"
- Industrial GC digest: "This week: ASME B31.3 update + a SIMOPS scheduling case"
- Specialty Sub digest: "This week: Reading specs before you bid + a lien waiver scenario"

**Community highlights**: As the subscriber base grows, "what others are learning" content builds social proof. An email section titled "From our learners this week" (aggregating LinkedIn comments or email replies with permission) creates community signal without requiring a dedicated community platform. Target: add this section to monthly digest by Month 4 when there are enough learners to quote.

### Stage 3 Metrics

| Metric | Target | Measurement | Success | Failure Trigger |
|--------|--------|-------------|---------|-----------------|
| 5+ module completion rate | 15-25% of signups | Kit `phase-1-started` tag count (proxy) / total signups | 20%+ | Below 10% at 100+ signups |
| Email open rate (bi-weekly digest) | 30-40% | Kit broadcast analytics | 35%+ | Below 25% for 3 consecutive sends |
| Weekly active user rate | 25-35% of list | Kit `engagement-active` segment count / total subscribers | 30%+ | Below 20% at Month 3 |
| 30-day retention rate | 60-70% of signups still opening emails at Day 30 | Kit: signups from Month N vs. active at Day 30 of Month N | 65%+ | Below 50% |
| Path completion (all modules in path) | 3-6% of signups | Self-reported via check-in + `path-complete` tag | Any path completions occurring | Zero completions after Month 4 |

**Failure trigger — open rate below 25%**: Run a subject line A/B test immediately (Kit supports subject line A/B on broadcast emails). Test plain text vs. curiosity-hook subject lines. Example: "This week: California lien rights update" vs. "The contractor just served you a preliminary notice. What now?" — curiosity format should outperform informational format by 15-25%.

**Failure trigger — 30-day retention below 50%**: The Day 14 case study email bundle offer is the last-chance retention mechanism. If 50% of subscribers are inactive by Day 30, the Day 0-14 sequence content needs revision. Most common problem: emails are too long or too academic; the audience wants practical tools, not curriculum overview.

---

## Stage 4: Revenue

**Definition**: A subscriber makes a financial transaction with the platform. Revenue Stage 4 is not expected before Month 4 (October 2026 if launched July).

**Prerequisites for revenue activation**:
- Email list at 300+ subscribers
- At least 30 subscribers have reached 5+ modules (providing a warm audience for the certification offer)
- At least 1 instructor actively engaged (for live sessions)
- Certification track fully built and tested internally

### Revenue Products in Priority Order

**Product 1 — Certification track** ($97-127):
- Entry: Email broadcast to `phase-1-complete` and `engagement-high` segments only (not the full list — this avoids coming across as sales-first to inactive subscribers)
- Launch sequence: 3-email drip (introduction, deadline, last-chance) over 10 days
- Expected conversion rate: 3-8% of the warm audience (subscribers who have completed Phase 1 and are engagement-active)
- At 30 warm subscribers and 5% conversion: 1-2 initial certification enrollments. Not impressive, but it validates the product and price point. Scale after first 5 completions with testimonials.

**Product 2 — Live instructor session** ($35-75):
- Entry: Email to `engagement-high` and `phase-2-started` segments
- Booking: Simple scheduling link (Calendly free plan; 1 event type sufficient for the first session)
- Group minimum: 10 registrants required for session to run; 30 maximum per session
- Expected conversion: 5-12% of targeted segment; group structure requires critical mass

**Product 3 — Institutional license** ($150-500/year):
- Entry: Outbound sales conversation with partner organizations identified through partnership outreach
- Not a self-serve product at Phase 2 stage; requires direct negotiation

### Stage 4 Metrics

| Metric | Target (by Dec 2026) | Measurement | Success | Failure Trigger |
|--------|---------------------|-------------|---------|-----------------|
| Active instructors | 5-10 | Kit `path-instructor` subscribers with email activity | 5+ | 0 by Month 6 |
| Certification enrollments | 50-100 | Direct count from payment processor | 50+ | Below 10 by Month 5 |
| ARPU (active subscribers) | $5-15/month blended across list | Gross revenue / active subscriber count | $7+ | Below $3 after first product launch |
| Gross revenue | $2,500-8,000 by December 2026 | Payment processor totals | $3,000+ | Below $500 by December 2026 |
| Conversion rate (email list → paid) | 2-5% of email list | Paid customers / total subscribers | 3%+ | Below 1% after first product launch broadcast |

**ARPU context**: The $5-15/month target is a blended number across the full list including inactive subscribers. The active-subscriber ARPU will be higher — a 500-subscriber list with 50 paying certification students at $97 averages $9.70 ARPU on the active list, which is within target. This is comparable to SaaS education freemium benchmarks (5-8% of freemium users convert to paid; EdTech platforms specifically see 24-29% trial-to-paid conversion where a "trial" is defined as completing at least one module).

**Failure trigger — Revenue Stage 4**: If zero paid conversions occur after broadcasting to 50+ warm subscribers, the problem is one of: wrong price point, unclear value proposition, or the certification product itself is not compelling. Diagnosis: survey the non-converters with a one-question reply-to email ("What would make you pay $97 for a construction GC certification?"). Price objection vs. value objection have different fixes.

---

## Stage 5: Advocacy

**Definition**: A subscriber actively refers others to the platform, recruits instructors, or provides a usable testimonial or case study.

**Target NPS**: 50+ (world-class for education platforms; Duolingo achieves ~65, typical MOOCs achieve 30-40). For a free curriculum, NPS tends to be higher than for paid products because expectations are calibrated differently.

**NPS measurement**: Send a one-question NPS survey ("How likely are you to recommend this curriculum to a colleague? 0-10") at Day 45 via Kit broadcast to all subscribers who have opened at least 3 emails. Follow-up open text: "What is the main reason for your score?" Kit cannot natively measure NPS, but you can build it with a redirect-to-typeform-or-google-form link and capture responses in a spreadsheet.

### Advocacy Mechanics

**Instructor recruitment**: The most powerful advocacy mechanic is an active instructor who assigns the curriculum to their students. An instructor at a community college can add 15-30 new email subscribers per semester by directing students to the signup page. The instructor persona is the primary advocacy vector — investing in instructor satisfaction and retention has outsized return.

**Alumni referral program**: Simple referral mechanism introduced at Stage 4 (after first certification completions). Format: email to all `phase-1-complete` and `phase-2-started` subscribers saying "Know someone who would benefit from this? Share this link." Referral tracking: unique UTM parameter per subscriber (e.g., `?ref=subscriber-id`) is complex without a backend. Simpler: generic referral link (e.g., `?source=learner-referral`) that identifies the channel even if not the individual referrer.

**Case studies**: At Month 4+, begin soliciting case study submissions from subscribers who have completed paths or earned certifications. Format: "Submit your story" link in the monthly digest footer. Three case studies by December 2026 provide strong social proof for the next cohort's enrollment decision.

**Target referral rate**: 20-30% of growth by Month 9 (Q1 2027 if launch is July 2026) attributable to referral sources (learner-referral UTM, instructor word-of-mouth, association newsletter). At Month 3-4, referral traffic is typically under 10% of growth. It grows as the subscriber base grows — the math requires a base of 500+ subscribers before referrals produce statistically meaningful new subscriber volume.

### Stage 5 Metrics

| Metric | Target | Measurement | Success | Failure Trigger |
|--------|--------|-------------|---------|-----------------|
| NPS | 50+ | One-question survey at Day 45 | 50+ | Below 30 |
| Referral signups as % of growth | 20-30% by Q1 2027 | GA4 UTM `source=learner-referral` | 20%+ | Below 10% at Month 6 |
| Testimonials collected | 5+ by December 2026 | Direct count from form submissions | 5+ | Zero by Month 5 |
| Active instructors recruited from subscriber base | 2-5 by Month 6 | Kit `path-instructor` tag + email activity | 2+ | Zero by Month 5 |
| Case studies published on site | 3+ by December 2026 | Page count on /case-studies/ (new page) | 3+ | Zero by Month 5 |

**Failure trigger — NPS below 30**: This signals a curriculum quality or delivery experience problem, not a marketing problem. Survey the detractors (score 0-6): what specifically disappointed them? Common failure modes are email frequency mismatch (too many emails), content depth not matching the description ("I expected more practical stuff"), or a specific module that feels incomplete.

---

## A/B Testing Framework Integration

The A/B testing framework from PHASE_1_AB_TESTING_FRAMEWORK.md covers three active tests at site launch:

1. **Homepage CTA framing** (Test 1): Variants A/B/C. Winner expected by Week 6-8 at 200 sessions per variant.
2. **Email signup placement** (Test 2): Bottom vs. mid-page vs. scroll modal. Overlap possible with Test 1 after Week 3.
3. **Module page CTA text** (Test 3): Generic subscribe vs. path-specific vs. case study hook. Begins Week 5-8.

**Phase 2 A/B tests (new, not in Phase 1 framework)**:

| Test | Hypothesis | Variants | Start Condition | Measurement |
|------|------------|----------|-----------------|-------------|
| Day 4 email format | Plain text outperforms formatted for early list | Plain text vs. formatted | 50+ signups | Open rate + module visit rate by variant |
| Certification landing page CTA | "Get certified" vs. "Start your intensive" | Two-button variants | First 30 warm subscribers identified | Enrollment conversion rate |
| Instructor outreach email | Specific value proposition vs. general | "Free CSLB checklist for your students" vs. "Curriculum access offer" | 20 outreach emails baseline sent | Response rate by variant |

**Platform limitation**: Kit does not support A/B testing of automation emails (only broadcast emails). The Day 4 email A/B test requires manually sending one variant to the first 25 signups and the other to the next 25, then measuring. Acceptable for Phase 2 volumes; upgrade to a more sophisticated automation when list exceeds 500 subscribers and Kit Creator plan is active.

---

## Week-1 Measurement Checklist

Collect this data before scaling any channel or spending on paid acquisition. Data collected in Week 1 establishes the baseline against which all later growth is measured.

**GA4 data to review by end of Week 1**:
- [ ] Total sessions (establish baseline daily/weekly count)
- [ ] Bounce rate (engagement rate) on homepage — note the number, do not optimize yet
- [ ] Top traffic sources (Source/Medium report) — what is sending early visitors?
- [ ] Top landing pages — is the homepage the primary entry, or are modules getting direct traffic?
- [ ] `path_selection` event count — are visitors clicking any CTA?
- [ ] `email_signup_conversion` event count — is the Kit form firing correctly on the thank-you page?

**Kit data to review by end of Week 1**:
- [ ] Subscriber count and growth curve (daily additions)
- [ ] Tag distribution: what % of signups carry each path tag? (Expected: residential-gc largest, given California curriculum weighting)
- [ ] Day 0 open rate for each path variant welcome email
- [ ] Automation status: is the welcome automation triggering correctly for all tag branches?

**Module engagement to check Week 1**:
- [ ] GA4 page views by module — which modules are getting organic discovery traffic?
- [ ] Which modules appear in the Day 4 email case study? — confirm those module pages are receiving referral traffic from Kit link clicks
- [ ] Are there any modules with zero page views? — those are invisible to the audience; add them to the LinkedIn content calendar as spotlight posts

**Demographic data (where available)**:
- [ ] GA4 user demographics: age range and location breakdown if enabled (requires user consent signal; GitHub Pages with basic GA4 setup collects this by default if user is in the GA4 audience expansion pool)
- [ ] GA4 device category: mobile vs. desktop — construction professionals often browse on mobile during breaks; if mobile > 60% of sessions, audit the signup form mobile experience
- [ ] Kit subscriber location: not available on free plan; note this as a reason to eventually upgrade (knowing which % of list is California helps calibrate regulatory-content weighting)

**Checklist sign-off criteria**: Week 1 data is sufficient to proceed with channel scaling if:
- Email signup conversion is firing correctly (GA4 event confirmed)
- At least 5 subscribers with correct path tags in Kit
- Welcome automation smoke test completed with at least 1 test subscriber per path
- Baseline GA4 session count established (even if it is only 20 sessions — you need a baseline)

Do not wait for "enough data" before checking Week 1 metrics. The purpose of Week 1 measurement is not to make optimization decisions — it is to confirm the instrumentation is working correctly and catch problems before they affect 100 subscribers.

---

## Funnel Health Dashboard (Ongoing)

Track these metrics in a simple spreadsheet updated monthly. No analytics platform required beyond GA4 + Kit.

| Stage | Metric | Month 1 Target | Month 3 Target | Month 6 Target |
|-------|--------|----------------|----------------|----------------|
| Awareness | Monthly sessions | 500 | 2,000 | 5,000 |
| Awareness | Homepage bounce rate | Below 55% | Below 50% | Below 45% |
| Activation | Email signup rate | 5% of sessions | 7% of sessions | 8% of sessions |
| Activation | First module visit | 40% of signups | 50% of signups | 55% of signups |
| Retention | 5+ module rate | 12% of signups | 18% of signups | 22% of signups |
| Retention | Email open rate | 35% | 38% | 35% (steady-state) |
| Retention | Total active subscribers | 50 | 250 | 750 |
| Revenue | Paid conversions | 0 | 0-5 | 15-30 |
| Revenue | Gross MRR | $0 | $0-500 | $500-2,000 |
| Advocacy | NPS | Not measured | Baseline survey sent | 50+ target |
| Advocacy | Referral % of growth | N/A | 5-10% | 15-20% |

---

## Sources

- [SaaS Freemium Conversion Rates 2026 — First Page Sage](https://firstpagesage.com/seo-blog/saas-freemium-conversion-rates/)
- [SaaS Average Free Trial Conversion Rate Benchmarks — Userpilot](https://userpilot.com/blog/saas-average-conversion-rate/)
- [The Completion Gap: 32,000 Courses — Ruzuku](https://www.ruzuku.com/learn/articles/completion-gap)
- [13 Proven Ways to Increase Online Course Completion Rates — Learning Revolution](https://www.learningrevolution.net/online-course-completion-rates/)
- [Dropout Rates in Online Training Programs — Matsh.co](https://www.matsh.co/en/dropout-rates-in-online-training-programs-stats-and-insights/)
- [How to A/B Test Email Content — Kit Help Center](https://help.kit.com/en/articles/11563912-how-to-a-b-test-email-content)
- [How to A/B Test Subject Lines — Kit Help Center](https://help.kit.com/en/articles/2502634-how-to-a-b-test-subject-lines)
- [Kit Review 2026 — EmailToolTester](https://www.emailtooltester.com/en/reviews/convertkit/)
- [Online Learning Statistics 2026 — EntrepreneurHQ](https://entrepreneurshq.com/online-learning-statistics/)
- [elearning Statistics 2025 — Teachfloor Blog](https://www.teachfloor.com/blog/elearning-statistics)
- [PHASE_1_AB_TESTING_FRAMEWORK.md](./PHASE_1_AB_TESTING_FRAMEWORK.md)
- [PHASE_1_KIT_COM_INTEGRATION_SETUP.md](./PHASE_1_KIT_COM_INTEGRATION_SETUP.md)
- [CAREER_TRAINING_USER_SEGMENTATION_FRAMEWORK.md](./CAREER_TRAINING_USER_SEGMENTATION_FRAMEWORK.md)
