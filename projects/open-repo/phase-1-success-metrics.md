# Phase 1 Success Metrics — open-repo

**Document Type**: Strategic measurement framework
**Status**: Production-ready for post-PR#1 merge implementation
**Last updated**: 2026-05-05
**Scope**: Define quantitative and qualitative success indicators for Phase 1 (PR #1 launch through 6-month post-merge checkpoint)

---

## Executive Summary

open-repo Phase 1 success depends on three pillars: **(1) Code adoption** (how many projects fork/star/integrate the federation standard), **(2) Community engagement** (contributor participation, discussion quality, issue responsiveness), **(3) Sustainability** (contributor retention, codebase health, momentum). This framework provides weekly/monthly measurement across all three pillars, enabling early detection of health issues and data-driven Phase 2 advancement decisions.

---

## GitHub Repository Metrics

### Primary Engagement Signals (Track Weekly)

**Star Growth**:
- **Target baseline** (Month 1): 20–50 stars (limited to federation/P2P developer network, not general)
- **Target trajectory** (Month 3): 100–150 stars (increased awareness in academic/civil tech circles)
- **Target trajectory** (Month 6): 250–500 stars (mainstream federation/open-source awareness)
- **Measurement**: GitHub API `stargazers` endpoint, track date-added per star for cohort analysis
- **Interpretation**: Stars indicate awareness + relevance. Slower growth (vs. viral projects) is expected for infrastructure projects. Growth trajectory matters more than absolute number.

**Fork Count**:
- **Target baseline** (Month 1): 3–8 forks (active developers integrating or modifying)
- **Target trajectory** (Month 3): 10–20 forks (Phase 2 candidates: institutions building on top)
- **Target trajectory** (Month 6): 25–50 forks (multiple derivative projects in active development)
- **Measurement**: GitHub API `forks_count`, track organization/user type per fork (academic, civil tech, commercial, hobbyist)
- **Interpretation**: Forks indicate active use + modification. Track WHO is forking (institution type). Commercial/academic forks > hobbyist forks = quality signal.

**Issue Count & Response Time**:
- **Target baseline** (Month 1): 2–5 issues/month (exploratory questions from early users)
- **Target trajectory** (Month 3): 5–10 issues/month (mix of questions + feature requests + bugs)
- **Target trajectory** (Month 6): 10–20 issues/month (sustained engagement, community identifying improvements)
- **Measurement**: Average time-to-first-response (TTFR) on issues
  - **Target TTFR**: <24 hours for bug reports, <48 hours for questions
  - **Interpretation**: Fast TTFR signals active maintenance. Slow TTFR = burnout risk or unclear issue priority.

**Pull Request Velocity**:
- **Target baseline** (Month 1): 1–3 external PRs (early contributors from research phase)
- **Target trajectory** (Month 3): 3–8 external PRs/month (sustained contribution from 2–5 core contributors)
- **Target trajectory** (Month 6): 8–15 external PRs/month (diverse contributor base, healthy review cadence)
- **Measurement**: 
  - Number of external PRs per month
  - Average PR merge time (target: <1 week for non-controversial, <2 weeks for design decisions)
  - Number of unique contributors per month (target: 2–5 Month 1, 5–10 Month 3, 10–15 Month 6)
- **Interpretation**: PR velocity > Issue velocity = healthy balance. Many PRs with slow merge = review bottleneck. Few PRs = contributor barrier.

### Secondary Metrics (Track Monthly)

**Repository Traffic**:
- **Target baseline** (Month 1): 100–200 unique views/month, 50–100 clones/month
- **Target trajectory** (Month 3): 400–800 unique views/month, 150–300 clones/month
- **Target trajectory** (Month 6): 800–1,500 unique views/month, 300–600 clones/month
- **Measurement**: GitHub Insights → Traffic tab (top referrers, most-viewed pages)
- **Interpretation**: Sustained traffic growth (20–25% MoM) indicates word-of-mouth + academic/professional circulation. Plateau after Month 2 = normal maturation (early adopters saturated).

**Dependencies & Reverse Dependencies**:
- **Target baseline** (Month 1): 0–2 projects depend on open-repo
- **Target trajectory** (Month 3): 2–5 projects depend on open-repo (libraries, frameworks building on federation standard)
- **Target trajectory** (Month 6): 5–10 projects depend (Phase 2 ecosystem emerging)
- **Measurement**: GitHub API `dependents` endpoint, track organization/project type
- **Interpretation**: Dependents = impact validation. Slow growth acceptable (infrastructure projects have long adoption timelines).

---

## Community Health Indicators

### Engagement Quality (Track Weekly)

**Issue Discussion Depth**:
- **Metric**: Average comments per issue (target: 2–5 for Q&A, 4–8 for design discussions)
- **Red flag**: Single-response issues (user opens, gets one-line answer, no follow-up) = opportunity for better documentation
- **Green signal**: Multi-turn discussions showing problem-solving in action = strong community

**PR Review Quality**:
- **Metric**: Average reviews per PR (target: 2–3 technical reviews, 1 UX/design review)
- **Red flag**: PRs merged without review = CI/testing over-reliance, potential quality issues
- **Green signal**: Substantive code reviews with design discussion = healthy stewardship

**Discussion Tone & Inclusivity**:
- **Qualitative assessment** (monthly): Read through issues/PRs, assess for:
  - Respectful disagreement (good) vs. dismissive tone (bad)
  - Newcomer integration (questions welcomed, onboarding clear)
  - Diversity of contributor perspectives
- **Measurement**: Tag issues by sentiment category (welcoming, neutral, discouraging)
- **Target**: 80%+ of issues tagged as welcoming/neutral; zero discouraging patterns

### Contributor Cohorts (Track Monthly)

**New Contributor Onboarding**:
- **Target baseline** (Month 1): 1–2 new contributors (from research phase or immediate network)
- **Target trajectory** (Month 3): 2–4 new contributors/month (sustained organic recruitment)
- **Target trajectory** (Month 6): 4–8 new contributors/month (established as known project)
- **Measurement**: Track contributor emergence by:
  - First contribution date (GitHub API)
  - Number of subsequent contributions (1-time = experimental, 3+ = committed)
  - Time-to-second-contribution (target: <2 weeks = high retention)
- **Success signal**: >50% of new Month 1 contributors remain active in Month 3

**Core Contributor Retention**:
- **Definition**: Contributor with 5+ commits or 3+ reviews in the prior month
- **Target baseline** (Month 1): 2–3 core contributors (maintainers + research collaborators)
- **Target trajectory** (Month 3): 3–5 core contributors
- **Target trajectory** (Month 6): 5–8 core contributors
- **Red flag**: Core contributor churn (drop from 5 to 2 in a month) = burnout or project direction friction
- **Measurement**: Track contributor commit frequency curves (should remain flat or grow, not cliff)

**Contributor Diversity** (Track Quarterly):
- **Dimensions**: 
  - Organizational affiliation (academic, civil tech, commercial, hobbyist independent)
  - Geographic distribution (measure by commit timezone patterns, contributor profile)
  - Experience level (new developers vs. established maintainers)
- **Target**: >50% contributors not directly affiliated with lead maintainers = healthy ecosystem
- **Interpretation**: Diverse contributors = resilience against single-point-of-failure

---

## Sustainability & Velocity Metrics

### Codebase Health (Track Monthly)

**Test Coverage**:
- **Target baseline**: >70% code coverage for Phase 1 (federation core)
- **Target trajectory (Month 3)**: >80% code coverage
- **Measurement**: CI/CD coverage reports (use `codecov.io` or equivalent)
- **Red flag**: Declining coverage = untested code entering. Leads to brittleness post-merge.

**Dependency Currency**:
- **Metric**: Percentage of dependencies within 1 major version of latest
- **Target**: >80% current (critical security + compatibility)
- **Red flag**: >20% of dependencies 2+ versions behind = technical debt + security risk
- **Measurement**: Dependabot or equivalent tool tracking

**Build Health** (CI/CD):
- **Metric**: Percentage of main branch commits passing CI
- **Target**: >98% (occasional failures acceptable, sustained failures = alarm)
- **Measurement**: CI/CD dashboard (GitHub Actions, Travis, etc.)
- **Red flag**: <90% pass rate = integration testing gaps or infrastructure instability

### Velocity & Momentum (Track Monthly)

**Commit Frequency**:
- **Metric**: Commits to main branch per week
- **Target baseline** (Month 1): 3–5 commits/week (active development + bug fixes)
- **Target trajectory** (Month 3): 5–10 commits/week (feature development + refactoring)
- **Target trajectory** (Month 6): 8–15 commits/week (product-market fit + steady improvement)
- **Red flag**: Declining commit frequency (e.g., 8/week → 2/week) = project stalling or maintainer overload
- **Green signal**: Consistent or growing frequency = active stewardship

**Issue Closure Rate**:
- **Metric**: (Issues closed in month) / (Issues opened in month)
- **Target**: 0.7–1.0 (closing 70–100% of new issues monthly; growth backlog acceptable)
- **Red flag**: <0.5 = issues piling up faster than resolution = prioritization crisis
- **Interpretation**: Ratio > 1.0 acceptable if backlog shrinking

**Release Cadence**:
- **Metric**: Releases to main branch
- **Target baseline** (Month 1): 1–2 minor releases (0.1.x, 0.2.x)
- **Target trajectory** (Month 3): 1 minor release/month + 2–3 patch releases
- **Target trajectory** (Month 6): 1–2 minor releases/month + ongoing patches
- **Red flag**: No releases for >2 months = project stalled (even if commits active)
- **Interpretation**: Consistent versioning = user confidence in stability

---

## Real-Time Monitoring Dashboard (Proposed)

### Weekly Check-in Metrics

```
OPEN-REPO HEALTH SNAPSHOT (Week N)

GitHub Activity:
  Stars: XXX (Δ +YY from last week)
  External PRs: X open, Y merged this week
  Issues: Z open, W closed this week
  Avg issue TTFR: D days
  New external contributors: N

Velocity:
  Commits (main): M this week
  Tests passing: X% (was Y% last week)
  Code coverage: Z% (was W% last week)

Contributor Health:
  Core team commits: X
  External contributor commits: Y
  First-time contributors: N

Alerts:
  ⚠️ YELLOW: [threshold-triggered alerts]
  🔴 RED: [critical alerts]
```

### Monthly Reporting Template

1. **Executive Summary** (1 paragraph): Overall health status (strong/stable/declining), key wins, key concerns
2. **Metrics Summary Table**: All primary metrics vs. targets for the month
3. **Cohort Analysis**: Star growth by week, contributor acquisition by source, fork types (academic/commercial/hobbyist breakdown)
4. **Narrative**: What happened? What drove the metrics? Any incidents or turning points?
5. **Forward Look**: What to watch for next month? Any Phase 2 advancement gates approaching?

---

## Phase 2 Advancement Gates

Movement from Phase 1 → Phase 2 (post-PR #1 merge + 3-month stabilization) requires:

**Gate 1: Community Establishment**
- ✅ 100+ stars (awareness threshold)
- ✅ 5+ unique external contributors (established community, not dependent on single developer)
- ✅ 10+ external PRs (contributions flowing in, not just issues)
- ✅ <24h average issue TTFR (responsive maintenance)

**Gate 2: Codebase Stability**
- ✅ >80% test coverage (code quality baseline)
- ✅ Zero critical security vulnerabilities (verified by audit or Dependabot)
- ✅ 98%+ CI pass rate (integration testing solid)
- ✅ Dependency currency >80% (security + compatibility)

**Gate 3: Product-Market Fit Indicators**
- ✅ 5+ organizations/projects forked for their own federation implementations
- ✅ 3+ peer-reviewed papers or technical blog posts citing the framework
- ✅ Steady issue quality (architectural questions > typo reports, ratio >3:1)
- ✅ Sustainable commit velocity (8+ commits/week sustained for 2+ months)

**Failure Gates** (Pause Phase 2 if):
- ❌ Star growth plateau <50 stars after 3 months (insufficient awareness)
- ❌ Core contributor burnout (commit velocity cliff)
- ❌ Test coverage decline below 70% (code quality degradation)
- ❌ >20% of dependencies outdated (security risk)

---

## Success Benchmarks from Comparative Projects

For calibration, comparable open-source infrastructure projects show these Phase 1 patterns:

| Project | Timeframe | Stars | Contributors | Release Cadence | Outcome |
|---------|-----------|-------|---------------|-----------------|---------|
| Prometheus | Y1 | 500–1,500 | 10–30 | Bi-weekly | Massive adoption (Phase 2+) |
| Kubernetes | Y1 | 1,000–5,000+ | 50+ | Weekly | Extreme adoption (Phase 3+) |
| ActivityPub | Y1 | 100–300 | 5–15 | Monthly | Moderate adoption (Phase 2) |
| Federation specs (avg) | Y1 | 50–200 | 3–10 | 2-3/month | Stabilizing (Phase 2-ready) |

open-repo targets the "Federation specs" band (academic + civil tech niche, not consumer-mass). Success = 100–200 stars in Year 1, 5–10 sustained contributors, 1–2 releases/month.

---

## Feedback Loop: Connecting Metrics to Actions

### If Stars Growth Slow (<20 in Month 1)
- **Action**: Increase awareness (mention in papers, civil tech mailing lists, academic networks)
- **Timeline**: Course-correct by end of Month 2 or accept niche positioning

### If Issue TTFR >48h
- **Action**: Triage backlog, recruit issue reviewers, or reduce scope (move issues to future releases)
- **Timeline**: Address within 2 weeks

### If External PR Velocity Slow (<1/month)
- **Action**: Check contributor barriers (bad CONTRIBUTING.md? no issue labels for newcomers? complex code?)
- **Timeline**: Reduce friction and reassess in 4 weeks

### If Core Contributor Churn (>30% drop)
- **Action**: Immediate 1:1 conversations. Risk of project stall.
- **Timeline**: Resolve within 1 week

---

## Measurement Tools & Integration

- **GitHub API**: Direct metrics (stars, forks, issues, PRs, traffic)
- **Dependabot or similar**: Dependency currency tracking
- **Codecov or similar**: Test coverage trends
- **GitHub Actions**: CI/CD health via workflow status
- **Manual monthly review**: Community sentiment, discussion quality, contributor diversity

**Recommendation**: Automate weekly pull of GitHub API metrics into a CSV or JSON, visualize in dashboard tool (Notion, Airtable, or custom HTML). Monthly human review for qualitative assessment.

---

## Conclusion

Phase 1 success is **measurable, achievable, and realistic** for an infrastructure/federation project in the civil tech and academic networks. The framework above enables data-driven Phase 2 decisions and early detection of sustainability issues.
