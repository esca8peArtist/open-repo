---
title: "Off-Grid Living Guide — Community Posting Calendar Template"
created: 2026-04-30
status: ready-to-execute
---

# Community Posting Calendar Template

Use this as a week-by-week execution checklist. Replace `[DATE]` with actual dates based on your chosen launch Tuesday.

---

## Week 1 — Core Launch (Days 1–7)

| Day | Platform | UTC Window | Angle | Action |
|-----|----------|-----------|-------|--------|
| Day 1 — Tuesday | r/offgrid | 10:00–12:00 | Full guide: real specs, interconnected systems | Post text thread; respond to first 5 comments within 1 hour |
| Day 2 — Wednesday | HackerNews | 12:00–15:00 UTC (or Sunday 12:00–14:00 UTC for higher breakout rate) | "Show HN: 17-domain open-source off-grid guide" | Submit; monitor every 30 min for 2 hours; respond to all comments |
| Day 2 evening | Twitter/X | 18:00–20:00 | 7-tweet thread; pin tweet 1 | Post thread; do not add to it for 48 hours |
| Day 4 — Friday | r/preppers | 10:00–12:00 | Disaster/nuclear angle, FEMA/CDC sources | Post text thread; respond to comments; flag factual questions to GitHub |
| Day 5 — Weekend | Dev.to | Any time | "Open-source knowledge infrastructure — project structure" | Publish; add tags: #opensource #homesteading #tools |
| Day 6 — Monday | r/homesteading | 10:00–12:00 | Food, site selection, regional guides angle | Post text thread; lead with personal voice |
| Day 7 — Tuesday | Medium | Any time | Domain 6 (Energy) standalone article | Publish; end with GitHub link |

**Week 1 Monitoring Checklist**:
- [ ] GitHub Insights > Traffic > Views (check daily)
- [ ] GitHub Insights > Traffic > Referrers (check daily — note top 3 sources)
- [ ] GitHub Stars (check daily; log in metrics spreadsheet)
- [ ] Reddit upvote totals (check once per day per post)
- [ ] Issues opened (check daily; triage within 24 hours)

---

## Week 2 — Secondary Expansion (Days 8–14)

Review Week 1 data before deciding which communities to post in next.

| Decision | If True | Action |
|----------|---------|--------|
| r/preppers outperformed 2:1 or more | Disaster angle resonates strongly | Post in r/SHTF or r/preppers follow-up (different domain, nuclear or grid-down) |
| r/offgrid drove most GitHub traffic | Core community is the primary audience | Post in r/self_reliance; engage in comments with follow-up questions |
| HN drove significant traffic (>500 views) | Technical audience is engaged | Post second Dev.to article; submit to relevant awesome lists |
| Twitter drove meaningful engagement | Social amplification is viable | Post a second thread on a different domain (Domain 15 or Domain 13) |
| All channels performed modestly | Distributed, sustained traction | Continue with planned supplemental posts; no pivot needed |

**Supplemental communities to consider (Week 2 or later)**:

| Subreddit | Estimated Size | Angle | Notes |
|-----------|---------------|-------|-------|
| r/solarpunk | ~200,000 | Community governance + open-source ethos | CC BY-SA framing; lead with Domain 13 |
| r/self_reliance | ~60,000 | Self-sufficiency philosophy | Lower volume, high engagement quality |
| r/SHTF | ~400,000 | Disaster scenarios, nuclear content | High overlap with r/preppers; use only if r/preppers post did not perform |
| r/sustainability | ~600,000–750,000 | Collective resilience framing | Post Domain 13 angle; avoid security/defense content |

**Week 2 Actions**:
- [ ] Choose 1–2 supplemental communities based on Week 1 performance data
- [ ] Open 3–5 "help wanted" GitHub issues targeting clear expansion areas
- [ ] Submit repo to 2–3 relevant awesome lists (awesome-selfhosted, awesome-sustainable-technology)
- [ ] Draft second Medium article based on highest-traffic domain signals

---

## Weeks 3–4 — Community Building

| Action | Timing | Notes |
|--------|--------|-------|
| Respond to all open GitHub issues | Every 2 days | Even a brief "acknowledged" keeps contributors engaged |
| Twitter thread #2 | Week 3, Tuesday 13:00–15:00 UTC | Topic: "What we learned researching nuclear preparedness" or highest-performing domain |
| Newsletter pitch | Week 3–4 | Identify 3–5 relevant newsletters; pitch with star count as social proof |
| Contributor spotlight (if PRs received) | Week 4 | Tweet + Reddit mention thanking contributor; update CONTRIBUTORS.md |
| Medium article #2 | Week 4 | Domain 13 (Community) or Domain 1 (Site Selection) |
| CONTRIBUTING.md update | Week 4 if no PRs yet | Add specific "help wanted" examples to reduce contribution friction |

---

## Weeks 5–12 — Maintenance Mode

**Monthly cadence**:

| Week of Month | Activity |
|--------------|---------|
| Week 1 | Scan open GitHub issues; prioritize 2–3 factual corrections |
| Week 2 | Implement fixes; update CHANGELOG |
| Week 3 | Identify one domain for "deepening" based on issue volume and Reddit questions |
| Week 4 | Publish deepened section; mention on Twitter; note in newsletter if active |

**Monthly metrics review** (30-minute session):
- GitHub stars trajectory: on track, ahead, or behind model? (See toolkit Part 3)
- Fork:star ratio: above 10%? Above 15%?
- Top referrers: new organic sources appearing?
- Issues: quality increasing over time (field experience, not just requests)?
- Unprompted cross-links: any new communities linking the guide?

---

## Metrics Tracking Spreadsheet Template

Copy this header row into a new spreadsheet. Update daily for Week 1, then weekly.

```
Date | GH Stars | GH Views | GH Forks | GH Issues | GH PRs | Reddit Upvotes (r/offgrid) | Reddit Upvotes (r/preppers) | Reddit Upvotes (r/homesteading) | HN Points | Top Referrer | Notes
```

**Thresholds that trigger action**:

| Signal | Threshold | Action |
|--------|-----------|--------|
| Stars stagnant | < 10 new stars/week after Week 2 | Secondary channel expansion; awesome-list submission |
| Fork:star ratio low | < 8% by Month 1 | Update README with fork-friendly use cases; add CONTRIBUTING.md examples |
| Issue quality high | 3+ issues citing field experience | Prioritize those domains for Month 2 deepening |
| Traffic source unexpected | New domain in referrers | Research that community; engage organically |
| PR submitted | Any PR | Respond within 24 hours; spotlight the contributor publicly |

---

## Phase 3 Gate (Day 30 Decision)

On Day 30, evaluate against these thresholds before committing to Phase 3 expansion (visual content, video guides, domain deepening):

**Proceed to Phase 3 if**:
- GitHub stars ≥ 300
- At least 1 community-submitted PR received
- Traffic still showing week-over-week growth (not just launch spike)
- Issues opened ≥ 5 (signal of active engagement)

**Hold at Phase 2 if**:
- GitHub stars < 150
- No PRs received
- Traffic declining to near-zero after launch spike
- Action: stabilize, update content based on GitHub issue feedback, wait 60 days and re-evaluate

**Exceptional case — exceed targets significantly**:
- If stars ≥ 800 by Day 30, begin Phase 3 planning immediately
- Prioritize: regional guide expansion (Appalachia, Gulf Coast, Pacific Coast) and video companion content for highest-traffic domains
