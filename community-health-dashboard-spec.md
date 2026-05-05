# Community Health Dashboard Specification — open-repo

**Document Type**: Dashboard design + tracking protocol
**Status**: Production-ready for implementation post-PR#1 merge
**Last updated**: 2026-05-05
**Scope**: Real-time + monthly visualization of open-repo community health, contributor patterns, and sustainability indicators

---

## Executive Summary

This specification defines the **Community Health Dashboard** — a lightweight, data-driven system for visualizing open-repo's Phase 1 growth and detecting sustainability risks. The dashboard surfaces key metrics weekly and produces monthly reports, enabling rapid course-correction if health signals degrade.

The design prioritizes **actionable insights** over vanity metrics. Rather than simply showing star count, it asks: "Are new contributors staying?" "Is code quality improving?" "Is the review process responsive?" These questions guide Phase 2 readiness decisions.

---

## Dashboard Architecture

### Three-Tier Visualization

**Tier 1: Executive Summary (1 page, updated weekly)**
- Current status snapshot (5 key metrics)
- Trend arrows (growing, stable, declining)
- Alert zone (green / yellow / red)
- 30-word interpretation for non-technical stakeholders

**Tier 2: Detailed Metrics (2-3 pages, updated weekly)**
- All primary metrics with 4-week trend graphs
- Cohort breakdowns (contributors by type, forks by organization)
- Anomaly highlighting (unexpected drops or spikes)

**Tier 3: Deep Dives (Monthly deep-read)**
- Issue discussion analysis
- PR quality assessment (code review depth, design discussion richness)
- Contributor trajectory stories (who's joining, who's staying, burnout signals)

---

## Weekly Snapshot Template

**Format**: Single-page HTML or Markdown report, auto-generated from GitHub API pulls

```
═══════════════════════════════════════════════════════════════════
              OPEN-REPO COMMUNITY HEALTH — WEEK OF MAY 5–11
═══════════════════════════════════════════════════════════════════

STATUS: 🟢 HEALTHY [vs. 🟢 HEALTHY last week]

KEY METRICS:
  ⭐ Stars:             45  (↑3 from last week, target: 20–50)  ✅
  👥 Contributors:      6  (↑1 new, 100% retention this week)   ✅
  🔀 PRs:              2 open, 1 merged this week (vs. target 1–2) ✅
  📋 Issues:           4 open, 2 closed (ratio: 0.5, healthy)    ✅
  ⏱️  Avg issue TTFR:  18h (target: <24h, GOOD)                ✅

ALERTS: None 🟢

LAST WEEK'S QUESTIONS:
  Q: New contributor retention — 1 contributor from Week N active? 
  A: ✅ YES — @contributor_name merged 2 PRs this week

FORWARD LOOK:
  Watch: PR review depth next week. This week's average was 1.2 reviews/PR.
  Target: 2+ reviews/PR for design-heavy PRs.

═══════════════════════════════════════════════════════════════════
```

---

## Detailed Metrics Page Template (Weekly)

### 1. GitHub Activity

**Visualization**: Line graph with dual Y-axes
- Primary axis: Stars/Forks (cumulative)
- Secondary axis: Weekly PRs/Issues closed (flow)
- Time window: 4 weeks rolling

**Table**:
| Metric | This Week | Last Week | 4-Week Avg | Target | Status |
|--------|-----------|-----------|-----------|--------|--------|
| New stars | 3 | 5 | 3.5 | 4–6 | ⚠️ YELLOW (slightly below) |
| New forks | 1 | 0 | 0.75 | 1–2 | 🟢 OK |
| PRs merged | 1 | 2 | 1.5 | 1–3 | 🟢 OK |
| Issues closed | 2 | 3 | 2.25 | 2–4 | 🟢 OK |
| Avg issue TTFR | 18h | 12h | 15h | <24h | 🟢 GOOD |
| Test coverage | 82% | 80% | 81% | >80% | 🟢 OK |

**Interpretation**: 
- Star growth slightly below baseline (watch for Week N+1 to see if it's just weekly variance)
- PR merge velocity stable
- Issue response time consistent and healthy
- Test coverage improving (80% → 82%)

---

### 2. Contributor Cohorts

**Visualization**: Stacked area chart showing contributor count by status
- Tier: Core (5+ commits/mo), Active (1–4 commits/mo), New (<1 month in project)
- Color: Blue (retained from prior month), Orange (new)

**Table**: Contributor Activity This Week

| Name | Commits | PRs | Reviews | Org | Status |
|------|---------|-----|---------|-----|--------|
| @esca8peArtist | 4 | 2 | 8 | esca8pe / volunteer | Core, active |
| @contributor_B | 2 | 1 | 2 | Academic org | Active |
| @contributor_C | 1 | 1 | 0 | Hobbyist | New, experimental |
| @contributor_D | 0 | 0 | 1 | Hobbyist | Core, quiet week |

**Metrics**:
- **Core contributors active**: 4 of 6 (67%, target: >50%)
- **New contributors this week**: 1 (@contributor_C)
- **New contributor 2-week retention**: 2 of 3 from 2 weeks ago (67%, target: >50%)
- **Contributor diversity** (by org): 50% hobbyist independent, 25% academic, 25% other

---

### 3. Engagement Quality

**Qualitative Assessment** (conducted during monthly deep-dive, summarized weekly):

**Issue Discussion Depth**:
- Sample issues from week: [Link to top 3 issues by comment count]
- Average comments/issue: 3.2 (target: 2–5 for Q&A)
- Quality distribution: 80% substantive discussion, 20% duplicates/off-topic

**PR Review Quality**:
- Sample PRs from week: [Link to top 2 PRs by review count]
- Average reviews/PR: 1.8 (target: 2–3)
- Review tone: 100% constructive (0 dismissive/hostile comments)
- Design discussion: 50% of PRs had architectural discussion (healthy)

**Accessibility for Newcomers**:
- Onboarding friction (feedback from @contributor_C): "Contributing guide clear, but needed 1 clarification on PR template"
- Action: Improve CONTRIBUTING.md section on PR format (do this Week N+1)

---

## Monthly Deep-Dive Report Template

**Format**: 3–4 page narrative with tables and charts

### 1. Executive Summary

```
APRIL COMMUNITY HEALTH ASSESSMENT

Status: 🟢 STABLE + GROWING
- Star growth: 28 → 45 (61% growth, tracking well vs. target)
- Contributor establishment: 3 → 6 core/active contributors (healthy growth)
- Code quality: Test coverage improved 76% → 82% (positive trend)
- Contributor retention: 80% (strong — only 1 person who started in March is now inactive)

Key wins this month:
1. New contributor @contributor_C integrated smoothly; merged 2 PRs
2. Academic org @Academic_Org_X contributed substantial refactoring PR
3. Test coverage improved despite active feature development
4. Issue TTFR consistently <24h (responsive to user questions)

Areas to watch:
1. PR review depth inconsistent (some PRs merged with 1 review, others stuck at 2 weeks)
2. Design discussion could be richer (1.2 avg comments on architectural PRs)
3. No releases this month (accumulated 8 commits; plan minor release Week N+1)

Phase 2 readiness: On track. Current trajectory suggests hitting Phase 2 gates by Month 3.
```

### 2. Contribution Patterns & Cohort Analysis

**Chart 1: Contributor Emergence Timeline**

```
@esca8peArtist  ████████████████████  (5 months, core)
@contributor_B  ████████               (2 months, active)
@contributor_C  ██                     (0.5 months, new)
@contributor_D  ████                   (1.5 months, core-quiet)
@contributor_E  ██                     (0.5 months, new)
@contributor_F  ██                     (1 week, experimental)
```

**Table: First-to-Second-Contribution Timeline**

| Contributor | First PR | Second PR | Days to 2nd | Status |
|-------------|----------|-----------|------------|--------|
| @contributor_B | Mar 15 | Mar 28 | 13d | ✅ Retained |
| @contributor_C | Apr 20 | Apr 25 | 5d | ✅ Engaged |
| @contributor_D | Apr 1 | Apr 3 | 2d | ✅ Very engaged |
| @contributor_E | Apr 18 | [pending] | >12d | ⚠️ Watch |

**Interpretation**: 
- 75% of contributors from prior month remain active (strong retention)
- New contributors integrating quickly (5–13 days to 2nd contribution)
- Time from first to second contribution is **predictive of retention**: <2 weeks = 90% stay; >2 weeks = 40% churn

---

### 3. Dependency & Security Trends

**Table: Dependency Currency**

| Category | Current | Target | Status |
|----------|---------|--------|--------|
| Direct dependencies up-to-date | 12/14 | >80% (11+) | 🟢 86% |
| Dev dependencies up-to-date | 8/10 | >80% (8+) | 🟢 80% |
| Critical vulns | 0 | 0 | 🟢 CLEAN |
| High-severity vulns | 0 | 0 | 🟢 CLEAN |

**Action**: 2 minor version updates pending for transitive dependencies; schedule for Week N+1

---

### 4. Code Quality & Sustainability

**Chart: Test Coverage Trend**

```
Week 1:  ████████████████░░░░░░░░░░  74%
Week 2:  █████████████████░░░░░░░░░  76%
Week 3:  ██████████████████░░░░░░░░  78%
Week 4:  ██████████████████░░░░░░░░  82%

Target: >80% ✅ GOAL ACHIEVED
```

**Table: Build Health**

| Metric | This Month | Last Month | Trend |
|--------|-----------|------------|-------|
| CI pass rate | 97% | 95% | ⬆️ +2% |
| Avg merge time | 4d | 6d | ⬆️ -2d (faster) |
| Critical issues open | 0 | 0 | 🟢 GOOD |
| Tech debt issues | 2 | 3 | ⬆️ -1 (improving) |

---

### 5. Release & Versioning

**Releases This Month**: 0 (accumulated commits: 8)
- Recommendation: Cut v0.2.0 in Week N+1
- Changelog: [3 major features, 2 bugfixes, 1 refactoring]
- Communication plan: Announce in Twitter, mention in weekly newsletter, post on Hacker News

---

### 6. Community Feedback & Sentiment

**Issue/PR Tone Analysis** (sample 10 issues/PRs):
- Welcoming/collaborative: 8/10 (80%, target: >80%) ✅
- Neutral: 2/10 (20%)
- Discouraging/dismissive: 0/10 (0%, target: 0%) ✅
- Avg response time to newcomer questions: 8h (target: <24h) ✅

**Feedback Themes**:
1. "Contributing guide could be more detailed" (2 mentions) → Action: Expand CONTRIBUTING.md
2. "Love the clear federation model" (3 mentions) → Positive signal, use in Phase 2 marketing
3. "Would be great to see X integration" (1 mention) → Track for Phase 2 scope

---

### 7. Forward Look & Gate Assessment

**Phase 2 Readiness Assessment** (as of end of month):

| Gate | Metric | Current | Target | Status |
|------|--------|---------|--------|--------|
| Community | Stars | 45 | 100+ | 🟡 45% of target (on track for Month 3) |
| Community | External contributors | 6 | 5+ | ✅ PASS |
| Community | External PRs | 12 YTD | 10+ | ✅ PASS |
| Community | Issue TTFR | 18h | <24h | ✅ PASS |
| Codebase | Test coverage | 82% | >80% | ✅ PASS |
| Codebase | Vulns | 0 critical | 0 | ✅ PASS |
| Codebase | CI pass rate | 97% | >98% | 🟡 1% short (acceptable) |
| Codebase | Dependency currency | 86% | >80% | ✅ PASS |
| Product | Forks for federation use | 1 | 5+ | 🟡 20% of target |
| Product | Issue quality | 80% architectural | 3:1 ratio | ✅ PASS |

**Verdict**: On track for Phase 2 advancement by Month 3. No red flags. Two yellow flags (star growth slower than ideal, but within variance; only 1 fork vs. target 5, but early for this metric).

**Recommendation**: Continue current trajectory. Increase awareness efforts (academic conferences, civil tech channels) to accelerate star growth. Actively recruit Phase 2 federation partners to increase fork rate.

---

## Anomaly Detection Rules

### Yellow Alerts (Trigger investigation)
- Star growth <50% of target for 2 consecutive weeks
- Issue TTFR >36h (1.5× target)
- Core contributor commits drop >50% in a week
- PR merge time >8d (2× target)
- New contributor 2-week retention <33%

### Red Alerts (Require immediate action)
- Core contributor complete dropout (commit velocity cliff)
- Test coverage drop >5% in a month
- 3+ critical security vulnerabilities
- CI pass rate <90%
- >30% of dependencies critical-version-behind

---

## Integration with Measurement Tools

**Weekly Automated Data Pull** (Thursday EOD UTC):
1. GitHub API call: `GET /repos/esca8peArtist/open-repo/stargazers` → store count
2. GitHub API call: `GET /repos/.../stats/contributors` → extract activity
3. GitHub API call: `GET /repos/.../pulls` (state=all, sort=updated) → extract merge times, reviewer counts
4. GitHub API call: `GET /repos/.../issues` (state=all, sort=created) → extract creation/response/closure times
5. Codecov API call: Extract test coverage %
6. GitHub Actions API call: Extract CI pass rate
7. Dependabot data: Extract dependency status

**Output**: JSON file `community_health_metrics_week_N.json` stored in repo `/docs/metrics/`

**Monthly Report Generation** (First Friday of month):
1. Aggregate weekly JSON files into monthly CSV
2. Generate charts (using matplotlib or R script)
3. Conduct qualitative review (human, 30 min)
4. Produce final report (Markdown) and publish to `/docs/monthly-reports/`

---

## Conclusion

The Community Health Dashboard provides **objective, actionable visibility** into open-repo's Phase 1 growth. By tracking contributions, code quality, and community sentiment weekly and assessing comprehensively monthly, the project can maintain momentum, detect sustainability risks early, and make data-driven Phase 2 advancement decisions.

The framework is lightweight (mostly automated, <30 min monthly human input) and designed to grow with the project's complexity.
