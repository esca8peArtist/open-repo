---
title: "Wave 0 Timeline and Gates"
project: open-repo
phase: "5.2 Wave 0"
document_type: timeline
status: draft-for-review
date: 2026-06-28
wave_start: 2026-06-28
wave_end_target: 2026-09-06
---

# Wave 0 Timeline and Gates

**Wave 0 scope**: 8–12 weeks of live operation on GitHub Pages. Start: 2026-06-28. Decision point: 2026-09-06.

All dates are fixed. "When ready" is not a valid schedule. Each gate has a numeric threshold; if the threshold is not met, the pre-authorized action in the corresponding risk scenario activates.

---

## At-a-Glance Roadmap

| Week | Dates | Milestone | Go/No-Go Gate |
|---|---|---|---|
| 1 | Jun 28 – Jul 4 | GitHub Pages live, 3 seed articles, analytics active | Site resolves + GoatCounter records data by Jul 4 |
| 2 | Jul 5 – Jul 11 | Outreach Wave 1, Netlify shadow deploy, issue template live | 50 unique page views by Jul 11 |
| 3 | Jul 12 – Jul 18 | Food Preservation domain live, first external submission reviewed | Issue template viewed >10 times by Jul 18 |
| 4 | Jul 19 – Jul 25 | 5+ published procedures, CTA Variant B live | 5 published items by Jul 25 |
| 5 | Jul 26 – Aug 1 | Outreach Wave 2, GitHub Actions schema validator added | 100 unique page views/week by Aug 1 |
| 6 | Aug 2 – Aug 8 | 10-contributor gate | 10 submission issues opened by Aug 8 — if not, Scenario A activates |
| 7 | Aug 9 – Aug 15 | First ZIM file generated and published | ZIM file accessible via OPDS endpoint by Aug 15 |
| 8 | Aug 16 – Aug 22 | CTA Variant C live, Seed Preservation community seeding begins | 20 published procedures by Aug 22 |
| 10 | Aug 30 – Sep 5 | Review CTA A/B/C data, select winning variant | Decision logged by Sep 5 |
| 12 | Sep 6 | Wave 0 Decision Point | See Gate 12 below |

---

## Detailed Week-by-Week

### Week 1 — June 28 to July 4

**Objective**: GitHub Pages hard launch. No outreach until the site is functional and seeded with real content.

**Actions** (in execution order, each with a deadline):

| Action | Owner | Deadline | Done signal |
|---|---|---|---|
| Enable GitHub Pages via `gh api` command in GITHUB_PAGES_SETUP.md | User | Jun 28 | Site resolves at https://esca8peArtist.github.io/open-repo/ |
| Add GoatCounter tracking to `docs/_config.yml` | User | Jun 28 | GoatCounter dashboard shows first page view |
| Publish Variant A landing page (CTA: "Submit a procedure") | User | Jun 29 | Landing page renders correctly, CTA links to issue template |
| Create `.github/ISSUE_TEMPLATE/submit-procedure.md` from WAVE_0_CONTRIBUTOR_ONBOARDING_TEMPLATE.md | User | Jun 29 | Template appears in "New Issue" dropdown |
| Publish `docs/contributing/index.md` from WAVE_0_CONTRIBUTOR_ONBOARDING_TEMPLATE.md | User | Jun 30 | Page renders at /contributing/ |
| Publish `docs/content/water/index.md` (domain overview) | User | Jun 30 | Page renders |
| Author and publish 3 Water Systems seed procedures | User | Jul 3 | 3 procedure pages live at /content/water/ |
| Verify schemas are accessible at docs/schemas/ URLs | User | Jul 4 | schema.json files return 200 |

**Go/No-Go Gate — Week 1**:
- PASS: Site is live, GoatCounter is recording, 3 content items are published, issue template is accessible. Proceed to Week 2.
- FAIL: Any of the above is not done by Jul 4. Investigate blockers. If GitHub Pages itself is the problem, activate Scenario C (Netlify fallback) — do not wait more than 48 hours.

**Note**: The 3 seed procedures are maintainer-authored from publicly available sources. Recommended sources: WHO WASH manual (water by boiling, solar disinfection, chlorination). These are unambiguously authoritative, public domain, and directly schematizable.

---

### Week 2 — July 5 to July 11

**Objective**: First public outreach. Netlify shadow deploy. No new content domains yet.

**Actions**:

| Action | Owner | Deadline | Done signal |
|---|---|---|---|
| Post to r/preppers weekly resource megathread | User | Jul 6 | Post live, not removed |
| Post to r/Bushcraft (check subreddit rules first) | User | Jul 7 | Post live |
| Deploy Netlify shadow copy (verify Netlify builds successfully from same repo) | User | Jul 8 | Netlify URL returns same content as GitHub Pages |
| Submit to Kiwix third-party library list | User | Jul 9 | Submission confirmed (email or web form) |
| Invite 3 known contacts to make first submissions | User | Jul 10 | Invitations sent |
| Send medical reviewer outreach emails (from medical-reviewer-outreach-draft.md) | User | Jul 11 | Emails sent to 3 contacts |

**Go/No-Go Gate — Week 2**:
- PASS: 50+ unique page views by Jul 11 (GoatCounter). Proceed to Week 3.
- FAIL: <50 unique page views by Jul 11. Do not stop. Increase outreach in Week 3 (add 2 more subreddits: r/Survival, r/homestead). The 50-view threshold is an early-signal check, not a kill switch. If not met after Week 3 additional outreach, investigate whether the site is indexed by search engines (check Google Search Console).

---

### Week 3 — July 12 to July 18

**Objective**: Food Preservation domain goes live. First external submission reviewed and responded to.

**Actions**:

| Action | Owner | Deadline | Done signal |
|---|---|---|---|
| Publish `docs/content/food-preservation/index.md` | User | Jul 12 | Page renders |
| Author and publish 3 Food Preservation seed procedures (NCHFP source) | User | Jul 14 | 3 procedure pages live |
| Switch landing page CTA to Variant B ("Browse procedures") | User | Jul 14 | Variant B live, GoatCounter tracking click-through |
| Respond to any contributor-submitted issues (target: within 72 hours of submission) | User | Ongoing | All issues have a response |
| Publish `docs/contributors.md` | User | Jul 18 | Page renders (even if only maintainer is listed) |

**Milestone check — Week 3**:
- Issue template viewed >10 times (GoatCounter referral clicks to issue template URL)? If YES: onboarding funnel is working. If NO: consider adding a direct link to the issue template on the content procedure pages, not just the landing page.
- Has 1+ external submission been received? If YES: green signal. If NO and issue template viewed <10 times: discovery problem (fix: more prominent CTA). If NO and issue template viewed >10 times: motivation/complexity problem (fix: simplify the template or add an example filled-in submission).

---

### Week 4 — July 19 to July 25

**Objective**: 5 published procedures milestone. CTA data collection continues.

**Actions**:

| Action | Owner | Deadline | Done signal |
|---|---|---|---|
| Ensure 5 total published procedures (maintainer + contributor) | User | Jul 25 | 5+ items in /content/ |
| Review GoatCounter data: which procedure pages have highest views? | User | Jul 22 | Data review logged |
| If any contributor submissions received: publish them and notify contributor | User | Ongoing | Contributor notified with live URL |

---

### Week 5 — July 26 to August 1

**Objective**: Outreach Wave 2. GitHub Actions schema validation automated.

**Actions**:

| Action | Owner | Deadline | Done signal |
|---|---|---|---|
| Post to 2 additional communities (r/homestead, r/fermentation) | User | Jul 28 | Posts live |
| Add GitHub Actions workflow for JSON-LD schema validation on PRs | User | Jul 30 | .github/workflows/validate-schema.yml live |
| Target: 100 unique page views/week (GoatCounter weekly total) | Metric | Aug 1 | GoatCounter weekly report |

**Go/No-Go Gate — Week 5 (soft gate)**:
- If weekly page views <50 after Outreach Wave 2: add r/Survival and r/Permaculture to outreach list. Consider a blog post on a permaculture or preparedness newsletter.
- If weekly page views >=100: proceed to Week 6 as planned.

---

### Week 6 — August 2 to August 8

**THE CRITICAL GATE — 10 Contributor Submissions**

**Target**: 10 unique contributor submissions received (GitHub issues opened using the template), of which at least 3 are reviewed and published.

**Hard decision tree** (no exceptions, no "wait and see"):

**Result A (>=10 submissions):**
- Wave 0 contributor funnel is working
- Begin Seed Preservation community seeding this week
- Publish `docs/content/seed-preservation/index.md`
- Plan Outreach Wave 3 targeting seed saving communities

**Result B (5–9 submissions):**
- Funnel is partially working
- Investigate: Open GoatCounter referrer data. Are contributors arriving from Reddit posts? From direct GitHub search? This determines whether the problem is discovery (need more outreach) or conversion (need simpler template)
- If discovery problem: double outreach efforts in Weeks 7–8
- If conversion problem: test a simplified 3-question template ("What is it? What is the source? What are the steps?")
- Do not expand to Seed Preservation until 10-submission target is met

**Result C (<5 submissions):**
- Activate Scenario A from PHASE_5_2_WAVE_0_CONTENT_STRATEGY.md
- Switch to content-led growth strategy immediately
- Author 20 additional maintainer procedures over Weeks 7–10
- Do not invest more energy in contributor recruitment until Week 12 review

---

### Week 7 — August 9 to August 15

**Objective**: First ZIM file generated and published via OPDS.

**Actions**:

| Action | Owner | Deadline | Done signal |
|---|---|---|---|
| Run ZIM export pipeline on all published content | User | Aug 12 | ZIM file generated with no errors |
| Verify ZIM file is accessible via OPDS endpoint | User | Aug 12 | OPDS entry returns valid Atom XML with ZIM download link |
| Publish ZIM download link on `docs/index.md` | User | Aug 13 | Download link live and functional |
| Add "Download for offline use" section to each domain index page | User | Aug 15 | Sections live |

**Note**: The ZIM export pipeline is complete from Phase 5. This is an operational step, not a development task.

---

### Week 8 — August 16 to August 22

**Objective**: CTA Variant C live. Seed Preservation community building begins (conditional on Week 6 gate).

**Actions**:

| Action | Owner | Deadline | Done signal |
|---|---|---|---|
| Switch landing page CTA to Variant C ("Join the community") | User | Aug 16 | Variant C live |
| 20 published procedures milestone | Metric | Aug 22 | 20+ items published |
| If Week 6 gate was met: post to seed saving communities (r/vegetablegardening, seed library networks) | User | Aug 20 | Posts live |
| If Week 6 gate was NOT met: continue solo content authoring | User | Ongoing | — |

---

### Week 10 — August 30 to September 5

**Objective**: A/B/C CTA analysis. Select winning CTA for Wave 1.

**Decision**:

Pull GoatCounter data for three time periods:
- Weeks 1–3: Variant A (CTA: "Submit a procedure")
- Weeks 3–8: Variant B (CTA: "Browse procedures")
- Weeks 8–10: Variant C (CTA: "Join the community")

Metric: Click-through rate from landing page to issue template submission form (GoatCounter: clicks on the issue template link / total landing page views).

Decision rule: Highest click-through rate wins. Ties broken in favor of the action-oriented CTA (A > B > C).

Minimum sample size caveat: if total landing page views across any period is <200, the data is directional only. In this case, select Variant A by default (action-first framing is the standing hypothesis for a contribution-oriented project).

Log the decision in WORKLOG.md.

---

### Week 12 — September 6: Wave 0 Decision Point

**Metrics review**:

| Metric | Target | Green | Yellow | Red |
|---|---|---|---|---|
| Unique contributors | 10+ | >=10 | 5–9 | <5 |
| Published procedures | 20+ | >=25 | 15–24 | <15 |
| Page views/month (GoatCounter) | 500+ | >=500 | 200–499 | <200 |
| Domain coverage | Water + Food active | Both active | One active | Neither active |

**Decision tree**:

**All green**: Begin Phase 6 planning (SaaS hosting, federation node). Expand to Seed Preservation as third Wave 0 domain. Announce Wave 1 timeline.

**Two or three green, one yellow**: Maintain current scope for 4 more weeks (to Oct 4). Do not expand domains. Identify which metric is lagging and allocate targeted effort (more outreach for contributors; more content for page views; more domains for coverage).

**Two or more red**: Re-scope. Content-led library (solo maintainer authoring) is the operating model. Contributor recruitment is deferred to Phase 6 when the platform has more content to demonstrate value. This is not failure — 20+ high-quality offline procedures is a better Wave 0 outcome than 5 low-quality ones.

---

## Dependency Map

```
Week 1 (Pages live)
    |
    +-- Week 2 (Outreach Wave 1) -- requires: Week 1 content seeded
    |
    +-- Week 3 (Food domain live) -- requires: Week 1 complete
    |
    +-- Week 5 (GitHub Actions) -- requires: Week 1 complete; independent of Weeks 2-3
    |
    +-- Week 6 (10-contributor gate) -- requires: Weeks 2-3 outreach + template
    |
    +-- Week 7 (ZIM export) -- requires: Week 1 complete; independent of Week 6
    |
    +-- Week 8 (Seed community) -- CONDITIONAL on Week 6 gate pass
    |
    +-- Week 12 (Decision point) -- requires: all prior weeks
```

ZIM export (Week 7) is independent of the contributor gate. Even if Wave 0 is contributor-light, the ZIM file gets published on schedule.

---

## Non-Negotiable Rules

1. All dates are fixed. If a milestone slips, the next milestone does not move — it shrinks.
2. Every go/no-go gate has a numeric threshold. "Things seem to be going well" is not a gate pass.
3. Risk scenarios activate within 48 hours of threshold breach — not after further analysis.
4. The Netlify shadow deploy (Week 2) is mandatory even if GitHub Pages is working. Test the fallback before it is needed.
5. The medical reviewer emails (Week 2) send on schedule regardless of other workload. Medical content is a Wave 1 deliverable; the reviewer relationship must start now.

---

*Prepared 2026-06-28. All dates assume Wave 0 launch in week of 2026-06-28.*
