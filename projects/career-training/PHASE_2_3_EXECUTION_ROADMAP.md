---
title: "Phase 2-3 Execution Roadmap"
project: career-training
phase: "2-3"
created: 2026-06-28
status: decision-ready
---

# Phase 2-3 Execution Roadmap

**Scope**: Sequenced execution plan for Phase 2 (Email List Infrastructure) and Phase 3 (Social Media Distribution) after Phase 1 (GitHub Pages deployment) is complete. Identifies parallel tracks, critical path items, decision points, contingency paths, and time estimates.

**Starting assumption**: GitHub Pages site is live or user has pushed to deploy. Curriculum content is published and accessible.

---

## Phase Status Baseline

| Phase | Status | Gate Condition |
|-------|--------|---------------|
| Phase 1 — GitHub Pages Deployment | Ready for user push | User must push to GitHub and verify live URL |
| Phase 2 — Email Infrastructure | Not started | Phase 1 site live; Kit account created |
| Phase 3 — Social Distribution | Not started | Phase 2 email capture active; LinkedIn page exists |

---

## Phase 2: Email Infrastructure (Weeks 1-4 Post-Deployment)

### Critical Path (Sequential — Cannot Parallelize)

These must happen in order:

1. **Kit account created** (15 minutes) — Create account at kit.com/signup; select free Newsletter plan
2. **Signup forms built** (1-2 hours) — Create 4 forms: Industrial GC Path, Residential GC Path, Specialty Sub Path, Generic (homepage)
3. **Form embed codes placed on site** (1-2 hours) — Add embed code to homepage, Quick Start page, bottom of each learning path overview, bottom of individual module pages (at minimum: first module of each path)
4. **Welcome email sequence written** (3-4 hours) — 6 emails: Days 0, 2, 4, 7, 10, 14. See EMAIL_SOCIAL_FUNNEL_STRATEGY.md for outlines.
5. **Welcome automation built in Kit** (1-2 hours) — Single automation with path-tag branching (free plan compatible)
6. **Smoke test** (30 minutes) — Submit your own email address via each of the 4 forms; verify correct tag applied, correct welcome email received, automation routing correct

Total critical path time: ~8-11 hours. This can be done in a single focused day.

### Parallel Tracks (Can Run Simultaneously with Critical Path)

These do not block email capture but should be completed in Week 1-2:

**Track A: Lead Magnet Creation**
- Duration: 2-4 hours
- Deliverables: 2 PDF lead magnets (California GC Pre-Licensing Checklist + Construction Drawing Quick-Reference Card)
- Tool: Canva free plan, Google Docs export to PDF, or any PDF creation tool
- Output: PDFs hosted at `/assets/downloads/` in GitHub Pages repo
- Dependency: None — can start before Kit account

**Track B: Analytics Setup**
- Duration: 1-2 hours
- Deliverables: Google Analytics 4 property created; GA4 snippet added to Jekyll `_layouts/default.html`; Google Search Console property created; sitemap.xml submitted
- Dependency: GitHub Pages site live (Phase 1)
- Note: Do not delay this. Every week without analytics is traffic data you cannot recover.

**Track C: Path Selector Quiz (Optional, adds 2-4 hours)**
- Duration: 2-4 hours
- Deliverables: 5-question quiz built in Typeform (free), Kit landing page, OR embedded HTML quiz
- Integration: Quiz result routes to Kit form with appropriate path tag pre-applied
- Dependency: Kit account and forms created (Track C depends on critical path Step 2)
- Decision point: If time-constrained, skip quiz and use 3 separate forms on a "Choose your path" page. Same outcome, less sophistication.

**Track D: Kit Re-engagement Automation**
- Duration: 1-2 hours
- Deliverables: Automation that tags subscribers `engagement-inactive` after 30 days no open; queues re-engagement email
- Dependency: Welcome automation complete (critical path Step 5)
- Note: This can be built Week 2 without blocking email capture. Priority is lower than critical path.

### Phase 2 Gantt (Week View)

```
Week 1:
  Day 1-2: CRITICAL PATH — Kit account + forms + embed + smoke test
  Day 1-2: PARALLEL — Analytics setup (GA4 + Search Console)
  Day 2-4: PARALLEL — Lead magnet PDFs created and hosted
  Day 3-5: CRITICAL PATH — Welcome sequence emails written
  Day 4-5: CRITICAL PATH — Kit welcome automation built

Week 2:
  Day 6-8: Path Selector Quiz (if doing it; optional)
  Day 6-8: Re-engagement automation built in Kit
  Day 8-10: A/B test subject line variants on Day 4 case study email (set up in Kit)
  Day 10:  PHASE 2 OPERATIONAL — All capture, automation, analytics live
```

**Phase 2 Definition of Done:**
- [ ] 4 Kit signup forms live and embedded on site
- [ ] Welcome sequence (6 emails) loaded and active
- [ ] Welcome automation routing by path tag confirmed via smoke test
- [ ] GA4 and Search Console active
- [ ] At least 1 lead magnet PDF created and linked from signup form
- [ ] First test subscriber has received correct path-specific welcome email

---

## Phase 3: Social Media Distribution (Weeks 3-12 Post-Deployment)

### Decision Point 1: LinkedIn Personal vs. Company Page

**Make this decision before building any content:**

| Option | Pro | Con | Best For |
|--------|-----|-----|---------|
| Personal LinkedIn profile | Higher organic reach (personal > company in LinkedIn algorithm); immediate following from existing connections | Content tied to one person; not transferable if project expands | Solo operator; if you have an existing professional LinkedIn presence in construction |
| LinkedIn company page | Brand separation; transferable; multiple contributors | Lower organic reach on new pages without paid promotion; must build following from zero | If planning to scale to team; if personal LinkedIn is in an unrelated field |

**Recommendation**: Start with personal profile if your LinkedIn connections include any construction professionals. Switch to or add company page at 1,000 followers.

### Phase 3 Parallel Tracks

Phase 3 has significantly more parallel capacity than Phase 2 because content production and platform setup are independent.

**Track 1: LinkedIn Content Library Build (Weeks 3-6)**
- Duration: 3-5 hours upfront; 2-3 hours/week ongoing
- Deliverables: 20-post content library (enough for 7 weeks at 3 posts/week)
- Content types: 8x module excerpts, 6x case study questions, 4x career stories, 2x regulatory updates
- Tool: Buffer or Later for scheduling ($15-18/month); or post manually
- Dependency: Phase 2 email capture live (each LinkedIn post links to email signup)

**Track 2: LinkedIn Profile/Page Optimization (Week 3, parallel with Track 1)**
- Duration: 2-3 hours
- Deliverables: 
  - Profile headline updated: "Construction Career Training | 33 Modules, 150 Case Studies, 3 Career Paths"
  - About section: Lead with the curriculum value prop; end with "DM for free access" or link to site
  - Featured section: Pin link to site homepage and most popular module
  - Contact info: Link to email signup page (not raw site URL — link to lead magnet landing page for better conversion)

**Track 3: Partnership Outreach (Weeks 3-8, parallel)**
- Duration: 1-2 hours/week
- Deliverables: 10 outreach emails/week to construction associations, community colleges, union training programs
- Template: Already drafted in deployment-plan.md Section 2.5
- Tracking: Simple spreadsheet (Name | Organization | Email | Sent Date | Response | Status)
- Dependency: Site live (Phase 1); email capture live (Phase 2)
- Note: Partnership outreach is the highest-ROI subscriber acquisition channel for this curriculum. Each association newsletter mention can produce 50-200 subscribers. Prioritize this over paid ads.

**Track 4: Reddit and Online Community Seeding (Week 4-6)**
- Duration: 1-2 hours/week
- Platforms: r/Construction, r/generalcontractor, r/HomeImprovement, r/civilengineering
- Approach: Post value-first (share a module insight or case study scenario); mention the curriculum as the source; no hard sell
- One Reddit post linking to a genuinely useful module excerpt can drive 100-500 site visits in 48 hours if it resonates
- Caution: Reddit communities detect promotional content quickly. Lead with the case study or module content; let the curriculum URL be visible but not the headline.

**Track 5: YouTube Channel Setup (Week 8-12, optional)**
- Duration: 4-8 hours setup; 2-4 hours per video ongoing
- Dependency: LinkedIn content calendar running consistently (Track 1); email list at 100+ subscribers
- Do not start until: LinkedIn posts are producing consistent site traffic (check GA4 referral source)
- First 3 videos: "How to Read Construction Drawings" (Module 6 overview), "California GC Licensing Explained" (Module 12 overview), "Residential vs Industrial vs Specialty Sub Path — Which Is Right for You?" (curriculum overview)

### Phase 3 Gantt (Week View)

```
Week 3:
  Track 1: LinkedIn content library build (20 posts drafted)
  Track 2: LinkedIn profile/page optimization
  Track 3: Partnership outreach begins (10 emails/week cadence)
  Track 4: First Reddit post seeding

Week 4:
  Track 1: LinkedIn posting begins (3x/week)
  Track 3: Partnership outreach continues
  Track 4: Reddit community monitoring; respond to construction questions with curriculum references

Week 5-6:
  Track 1: LinkedIn analytics review — which post type drives site clicks?
  Track 3: First partnership responses expected; follow up non-responders
  Monitor: Email list subscriber count, weekly new subscribers, lead magnet conversion rate

Week 7-8:
  Decision Point 2: Email list growth review (see below)
  Track 3: 2-3 partnership confirmations expected if outreach is effective
  Track 5: YouTube setup begins IF LinkedIn + email are producing consistent results

Week 9-12:
  Track 1: LinkedIn cadence continues; optimize by post type performance
  Track 3: Active partnerships begin driving referral traffic; track UTM parameters
  Track 5: First YouTube videos published (if proceeding)
  Month 3 review: Email list size vs. targets; LinkedIn follower count vs. targets; top module page views
```

---

## Decision Points

### Decision Point 1: Email Platform Upgrade (Triggered at 200-500 Subscribers)

**Current state**: Kit free plan (10,000 subscriber ceiling; 1 automation)

**Upgrade trigger**: When you need a second standalone automation (e.g., separate instructor sequence running in parallel with path-specific sequences)

**Options at upgrade decision:**
- Kit Creator ($39/mo at 1,000 subscribers): Unlimited automations, sequences, A/B testing
- Mailchimp Standard ($20/mo at 500 contacts): Alternative if Kit Creator feels expensive at small list size
- Stay on free plan: If 1 automation (with branching) is sufficient; defer upgrade until 5,000 subscribers

**Recommendation**: Upgrade to Kit Creator when you have 300+ subscribers and are spending more than 2 hours/month managing workarounds to the 1-automation limit.

### Decision Point 2: Email List Growth Review (Week 8, ~2 Months Post-Launch)

**Check against targets:**

| Metric | Week 8 Target | If Below Target |
|--------|--------------|-----------------|
| Total subscribers | 75-150 | Review lead magnet placement; consider paid LinkedIn post boost ($50-100) |
| Weekly new subscribers | 15-25 | Check which traffic source drives signups (GA4 acquisition report) |
| Day 7 open rate | 40%+ | Revise subject lines; test plain text vs. designed email |
| Lead magnet conversion | 2-4% of site visitors | Move lead magnet above the fold; try different magnet |

**If Week 8 subscribers < 50**: Primary issue is site traffic, not email conversion. Double down on LinkedIn posting cadence and Reddit seeding before spending on paid ads.

**If Week 8 subscribers 50-150 but open rate < 30%**: Primary issue is email quality or subscriber expectation mismatch. Review Day 0 and Day 2 emails; ensure they match what was promised on the signup form.

### Decision Point 3: YouTube vs. LinkedIn Doubling Down (Month 3)

**Check LinkedIn performance at Month 3:**

| LinkedIn Metric | If Meeting Target | If Below Target |
|----------------|-------------------|-----------------|
| 150+ followers | Proceed to YouTube planning | Stay LinkedIn-only; identify why follower growth is slow |
| Top post: 2,000+ impressions | Good content-market fit; YouTube will compound | Experiment with different post formats before adding platform |
| 25+ site clicks per week from LinkedIn | LinkedIn is driving traffic; YouTube adds to this | Fix LinkedIn before adding YouTube |

**YouTube go/no-go criteria at Month 3:**
- LinkedIn producing 25+ site clicks/week consistently
- Email list at 100+ subscribers
- You or someone on the project can commit to 2 videos/month minimum
- Budget exists for basic recording setup ($200-500 for mic + lighting)

**If all four criteria met**: Start YouTube in Month 4.
**If any criterion unmet**: Defer YouTube until criteria are met. Adding a platform you can't sustain is worse than not having it.

### Decision Point 4: Paid Advertising (Month 4+)

**Only consider paid ads when:**
- Email list at 200+ organic subscribers (proves the content converts)
- LinkedIn content is producing organic engagement (proves the message resonates)
- You have defined a specific audience segment for targeting (not "construction professionals" — specific: "California GCs who manage residential projects over $500K")

**Starting budget**: $100-200/month on LinkedIn sponsored posts targeting GCs by job title and California location. Run for 30 days; measure cost per email signup. Acceptable: under $5 per signup. Pause if over $15 per signup.

**Do not start paid ads in Phase 2**. The organic channels have not yet been validated, and paying to amplify an unvalidated message is wasteful.

---

## Contingency Paths

### Contingency A: GitHub Pages Deployment Blocked

If user cannot deploy to GitHub Pages or chooses a different static site host (Netlify, Cloudflare Pages, etc.):

- Email strategy is identical. Kit forms work on any HTML page.
- GA4 setup is identical (same snippet).
- LinkedIn strategy is identical.
- The only GitHub Pages-specific elements are the Jekyll configuration and the `/docs/` directory structure. All other Phase 2-3 elements are platform-agnostic.

### Contingency B: Kit Free Plan Insufficient (1-Automation Limit)

If the single branching automation is not sufficient to cover all path variants:

1. **First workaround**: Use Kit's "Sequences" feature (unlimited on free plan) for path-specific content. A Sequence is a scheduled email series — not as flexible as an Automation, but sufficient for linear welcome drips per path.
2. **Second workaround**: Instead of one automation with branching, route all subscribers through a single generic welcome sequence, then use the Day 2 "which path are you on?" email to get self-reported path selection. Apply path tag manually or via a one-click link that triggers an automation. This defers path segmentation by 2 days but stays within free plan limits.
3. **Upgrade**: Creator plan at $39/month removes the automation limit entirely.

### Contingency C: Low LinkedIn Organic Reach

If LinkedIn posts are getting under 200 impressions per post after 4 weeks of consistent posting:

1. **Check profile completeness**: Incomplete profiles get lower distribution. 500+ connections, full About section, profile photo, and active posting history all affect reach.
2. **Check posting time**: Peak LinkedIn engagement is Tuesday-Thursday 8-10 AM and 12-2 PM local time.
3. **Check content format**: LinkedIn's algorithm in 2026 favors content that drives comments over content that drives external clicks. Ask a question at the end of each post. The case study format ("What would you do?") is algorithmically superior to module excerpt format ("Here's what Module 6 says about...").
4. **Engage with other construction LinkedIn posts before and after publishing**: 30 minutes of genuine comments on other construction professionals' posts increases your own post reach by activating the algorithm's reciprocal distribution.
5. **If still under 200 impressions after 8 weeks**: $50 LinkedIn post boost (1 post) to test whether the content resonates with the paid target audience. If boosted post reaches 2,000+ impressions and drives 50+ profile views, the content is fine — the issue is distribution. If boosted post gets low engagement, the content needs revision.

### Contingency D: Partnership Outreach Unresponsive

If 20 outreach emails produce 0-1 responses:

1. **Personalize**: Generic "we built a curriculum" emails do not work. Lead with the specific organization: "Hi [Name], I see [AGC California] serves contractors in the [region] market. I've built a 33-module GC curriculum that covers the exact licensing, lien rights, and safety compliance topics your members deal with daily."
2. **Phone follow-up**: Email is low-signal in the construction industry. A brief phone call to a training director ("Did you see my email? I wanted to make sure it didn't get buried") converts significantly better than email-only outreach.
3. **Start smaller**: Community college construction departments and union training coordinators are more responsive than large associations. Build credibility with 2-3 smaller partnerships before approaching AGC California.
4. **Offer something specific**: Instead of "free access to the curriculum," offer "I'd like to send your 2026 CSLB compliance module to your members as a free download — no strings attached." Gives the organization something concrete to share with members.

---

## Time and Resource Summary

### Phase 2 (Email Infrastructure)

| Task | Time Estimate | Skill Required | Parallel? |
|------|--------------|----------------|-----------|
| Kit account + 4 forms | 2-3 hours | Basic | No (sequential) |
| Form embeds on site | 1-2 hours | Basic HTML/Markdown | No (after forms) |
| Welcome email sequence (6 emails) | 3-4 hours | Writing | Yes (parallel with forms) |
| Welcome automation | 1-2 hours | Kit platform | No (after emails and forms) |
| Lead magnet PDFs (2) | 2-4 hours | Design/writing | Yes (parallel with everything) |
| GA4 + Search Console | 1-2 hours | Basic | Yes (parallel, starts Day 1) |
| Smoke test + QA | 30-60 min | None | No (last step) |
| **Phase 2 Total** | **10-17 hours** | | |

### Phase 3 (Social Distribution, First 30 Days)

| Task | Time Estimate | Skill Required | Parallel? |
|------|--------------|----------------|-----------|
| LinkedIn profile optimization | 2-3 hours | Writing | Yes |
| 20-post content library build | 3-5 hours | Writing | Yes |
| Social scheduler setup (Buffer) | 1 hour | Basic | Yes |
| Partnership outreach setup (10 emails) | 2-3 hours | Writing/research | Yes |
| Reddit community seeding | 1-2 hours/week | Writing | Yes (ongoing) |
| LinkedIn posting (3x/week) | 30-60 min/week | Writing | Ongoing |
| **Phase 3 First 30 Days Total** | **12-18 hours** | | |

**Cumulative Phase 2 + Phase 3 launch (60 days post-deployment)**: 22-35 hours.

At 5 hours/week: 5-7 weeks to have both email infrastructure and social distribution fully operational.
At 10 hours/week: 3-4 weeks.

---

## 30/60/90 Day Milestones

### 30 Days Post-Deployment (End of Phase 2)

- [ ] Email capture live on site (4 forms)
- [ ] Welcome sequence sending to all new subscribers
- [ ] GA4 collecting data
- [ ] Lead magnets available
- [ ] LinkedIn posting at 3x/week cadence
- [ ] First 10 partnership outreach emails sent
- **Target**: 50+ email subscribers; LinkedIn page active

### 60 Days Post-Deployment (End of Phase 2 / Start of Phase 3 Expansion)

- [ ] Re-engagement automation running
- [ ] Email list segmented by path (all subscribers tagged)
- [ ] 15+ LinkedIn posts published; performance data available
- [ ] 3-5 partnership responses received; 1-2 partnerships initiated
- [ ] Week 8 decision point review completed
- **Target**: 150+ email subscribers; LinkedIn 100+ followers; top module: 50+ page views

### 90 Days Post-Deployment (Phase 3 Operational)

- [ ] Monthly path-specific digest emails running (2x/month per segment)
- [ ] First partnership live (association newsletter mention OR community college link)
- [ ] LinkedIn performance stabilized (consistent 500+ impressions per post)
- [ ] YouTube decision made (go/no-go based on Decision Point 3 criteria)
- [ ] Month 3 analytics review complete: which modules get most views, which email type gets best CTR
- **Target**: 300+ email subscribers; LinkedIn 200+ followers; 5,000+ total site page views

---

## Sources

- [The Complete Email Marketing Implementation Roadmap — Your Digital Breakthrough](https://yourdigitalbreakthrough.com/email-marketing-implementation-roadmap/)
- [Marketing Roadmap Template 2026 — Monday.com](https://monday.com/blog/marketing/marketing-roadmap-template/)
- [Email Marketing for Online Courses 2026 — EmailToolTester](https://www.emailtooltester.com/en/blog/email-marketing-for-online-courses/)
- [Social Media Strategy for Creators 2026 — Newzenler](https://www.newzenler.com/blog/social-media-strategy-creators-2026)
- [How to Grow on Social Media 2026 — Buffer](https://buffer.com/resources/creator-growth-playbook/)
- [Kit Creator Plan Features — Kit Pricing Page](https://kit.com/pricing)
