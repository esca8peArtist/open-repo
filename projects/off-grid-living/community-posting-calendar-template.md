---
title: "Off-Grid Living Guide — Community Posting Calendar Template"
version: "2.0"
created: 2026-04-30
updated: 2026-05-05
status: ready-to-execute
---

# Community Posting Calendar Template

Use this as your week-by-week execution checklist. Replace `[LAUNCH_TUESDAY]` with your chosen start date. All times are UTC.

---

## Pre-Launch: Account Readiness Check

Before scheduling any posts, run this check:

```
Is the posting account established (> 6 months old, > 500 karma)?
  YES → Proceed directly to Week 1 launch.
  NO  → Is it moderate (1–6 months, 100–500 karma)?
         YES → Run 1-week comment warm-up, then launch.
         NO  → Account is new/cold (< 100 karma or < 30 days old).
                → Run the full 3-week warm-up in the toolkit (Part 2).
                → Set LAUNCH_TUESDAY to 3 weeks from today.
```

**Minimum viable account state before posting with links**: 50+ comment karma, at least 2 weeks of Reddit activity visible in the account history.

---

## Week 1 — Core Launch

| Day | Platform | UTC Window | Angle | Primary Action |
|-----|----------|-----------|-------|---------------|
| Day 1 — Tuesday | r/offgrid | 10:00–12:00 | Interconnected systems, real specs | Post text thread; respond to all comments within 1 hour |
| Day 2 — Wednesday | HackerNews | 12:00–15:00 (or Sunday 12:00–14:00 for higher breakout) | "Show HN: 17-domain open-source off-grid guide" | Submit; monitor every 30 min for 2 hours; respond to all comments |
| Day 2 evening | Twitter/X | 18:00–20:00 | 7-tweet thread; pin Tweet 1 | Post thread; do not add to it for 48 hours |
| Day 4 — Friday | r/preppers | 10:00–12:00 | Disaster/nuclear angle, FEMA/CDC sourcing | Post text thread; respond within 8 hours |
| Day 5 — Weekend | Dev.to | Any time | "Open-source knowledge infrastructure" developer angle | Publish; tags: #opensource #homesteading #tools |
| Day 6 — Monday | r/homesteading | 10:00–12:00 | Food production, regional guides, personal narrative hook | Post text thread; lead with personal voice |
| Day 7 — Tuesday | Medium | Any time | Domain 6 (Energy) standalone article | Publish; end with GitHub link |

**Week 1 daily monitoring checklist**:
- [ ] GitHub Insights > Traffic > Views (check daily; log in metrics spreadsheet)
- [ ] GitHub Insights > Traffic > Referrers (check daily; note top 3 sources)
- [ ] GitHub Stars (check daily; log number and delta)
- [ ] Reddit upvote totals per post (check once per day)
- [ ] Issues opened (check daily; triage within 24 hours)
- [ ] Check for spam filter: if a post has zero activity after 30 min at peak hours, test visibility in a logged-out browser

---

## Post-Type Decision Tree

Use this before drafting any post to determine the right platform, angle, and format.

```
WHAT TYPE OF CONTENT AM I SHARING?
│
├─► FULL GUIDE OVERVIEW (announcing the whole project)
│     │
│     ├─► Is this the first post in this community?
│     │     YES → Use the "Complete guide" format below (long text, all domains listed,
│     │            GitHub link at the end, CC BY-SA stated early)
│     │     NO  → Do not repost the same overview. Use a domain-specific angle instead.
│     │
│     └─► Which community?
│           r/offgrid  → Lead with energy/water/shelter specs; avoid nuclear headline
│           r/preppers → Lead with disaster scenarios + nuclear; cite FEMA/CDC/NCRP
│           r/homesteading → Lead with food/regional guides; personal narrative hook required
│           r/sustainability → Lead with Domain 13 (community governance); CC BY-SA framing
│
├─► DOMAIN-SPECIFIC DEEP DIVE (sharing one section, not the whole guide)
│     │
│     └─► Match domain to community:
│           Domain 1 (Site Selection)     → r/homesteading, r/offgrid, Medium
│           Domain 2 (Shelter)            → r/homesteading, r/offgrid, Dev.to
│           Domain 3 (Water)              → r/offgrid, r/homesteading
│           Domain 4 (Food Production)    → r/homesteading, r/sustainability
│           Domain 5 (Food Preservation)  → r/homesteading, r/canning
│           Domain 6 (Energy)             → r/offgrid, r/solar, Medium (SEO value)
│           Domain 11 (Communications)    → r/preppers, r/amateurradio
│           Domain 13 (Community)         → r/sustainability, r/solarpunk
│           Domain 15 (Disaster Scenarios)→ r/preppers, r/SHTF
│           Domain 17 (Nuclear)           → r/preppers, r/SHTF
│           Regional Guides               → Match region to community demographics
│
├─► HOW-TO GUIDE (teaching a skill, not announcing the project)
│     │
│     └─► Post as standalone text; link to guide section at END not beginning.
│          This performs better with Reddit algorithms than link-first posts.
│          Best for: r/homesteading, r/homestead, r/self_reliance
│
├─► QUESTION / COMMUNITY ENGAGEMENT
│     │
│     └─► Ask a genuine question in a community where you have karma.
│          Example: "What do you wish you'd known before sizing your solar system?"
│          Post the guide in a comment reply to relevant answers, not in the OP.
│          This is the lowest-risk posting pattern for newer accounts.
│
└─► NEWS / UPDATE (guide has been updated, new domain added, etc.)
      │
      └─► Post as a brief text update in 1–2 communities max.
           Include specific change ("added a nuclear prep domain" is better than
           "updated the guide"). Link to the specific commit or section, not just README.
```

---

## Community Posting Checklists

### r/offgrid Pre-Post Checklist

Before submitting, verify:
- [ ] Account karma is above 50 (ideally 100+)
- [ ] Post is a text post, not a bare link post
- [ ] Opening sentence contains a concrete specification (watt-hours, gallons, dollars per day) — not just a description
- [ ] GitHub link appears after at least 2–3 paragraphs of substantive content, not in the first paragraph
- [ ] CC BY-SA 4.0 and "no paywall" are stated explicitly in the post body
- [ ] No affiliate links, donation requests, or newsletter signup prompts
- [ ] Nuclear/defense content is mentioned as available but is NOT the headline
- [ ] Post is scheduled for Tuesday–Thursday, 10:00–14:00 UTC
- [ ] You are available to respond to comments for the next 2 hours after posting

### r/preppers Pre-Post Checklist

Before submitting, verify:
- [ ] Account karma is above 50
- [ ] Post title references source credibility: FEMA, CDC, NCRP, or similar
- [ ] Opening paragraph includes at least one specific claim you can defend ("Domain 17 uses NCRP Report 161 dosing thresholds")
- [ ] Disaster scenarios and/or nuclear content is the headline angle (this is expected and welcomed)
- [ ] GitHub link appears after substantive preview content
- [ ] No commercial links or monetization signals anywhere in the post
- [ ] Post angle is meaningfully different from the r/offgrid post (different title, different opening, different domain emphasis)
- [ ] Minimum 48 hours have passed since the r/offgrid post (crossover audience overlap)
- [ ] Post scheduled for Tuesday–Friday, 10:00–14:00 UTC

### r/homesteading Pre-Post Checklist

Before submitting, verify:
- [ ] Post opens with a personal narrative element ("we," "I," "our homestead") — not a product announcement
- [ ] Food production or regional guides are featured prominently
- [ ] Security/defense content (Domain 12) is not mentioned in the post — omit it here
- [ ] Tone is warm and conversational, not technical or clinical
- [ ] Minimum 48 hours have passed since the most recent post in r/preppers or r/offgrid
- [ ] Post is scheduled for Monday or Wednesday, 12:00–15:00 UTC
- [ ] You have read the current sidebar rules for this specific subreddit variant (r/homesteading vs r/homestead rules differ)
- [ ] Regional guides (PNW, Southwest, South, Midwest, Northeast) are mentioned specifically — this is a differentiating asset for this community

---

## Pre-Drafted Template Replies for Common Comment Types

Use these as starting points. Personalize where the brackets indicate — do not copy-paste verbatim, as Reddit users can recognize template responses.

### "What's the power system / solar setup?"

> The energy domain (Domain 6) goes into it in detail — the guide has sizing tables based on daily watt-hour consumption and battery bank calculations. Short answer: [provide a 1–2 sentence summary of the most relevant finding from Domain 6]. The full methodology and cost tables are in the guide. If you have a specific setup question I didn't cover well, happy to open a GitHub issue and expand that section.

### "Is this AI-generated?"

> Fair question given how much AI content is around right now. The sourcing is based on FEMA guidelines, CDC public health documentation, NCRP technical reports, and similar primary sources — all cited in each domain. The commit history on GitHub shows the development process. It's CC BY-SA 4.0, so the full text is readable and auditable. If you spot anything that looks wrong or under-sourced, I'd genuinely welcome a GitHub issue — that's exactly the kind of feedback that makes this better.

### "This is missing [topic X]"

> That's a real gap, you're right. [If you know the answer: quick honest response.] [If you don't: "I don't have deep coverage of that yet."] If you have expertise there, I'd welcome a PR — the contribution guide is in the repo. Or I can file it as a 'help wanted' issue. Which domain does it fit closest to? [Keeps the conversation going without overpromising.]

### "What's your background / why should I trust this?"

> The guide leans on primary source material rather than personal authority — FEMA, CDC, NCRP, and similar. That's deliberate: I wanted something verifiable and auditable, not just my own experience. Every factual claim has a source citation. If something looks wrong, the GitHub issue tracker is the place to dispute it with evidence. The open-source model means errors get caught and fixed publicly.

### "Can I share this / use this for [purpose]?"

> Absolutely — CC BY-SA 4.0 means you can use it, adapt it, translate it, or republish it with attribution. If you're doing something interesting with it I'd love to hear about it.

### "Have you considered adding [regional guide / climate type]?"

> Yes, that's on the list. The current regional guides cover [PNW / Southwest / South / Upper Midwest / Northeast], but [mentioned region] isn't there yet. If you know that region well and want to contribute, I've filed a 'help wanted' issue for it — or let me know and I'll create one. Even a rough draft of the key regional differences would be a solid starting point.

### "This is way too long / overwhelming"

> Fair point — it's not designed to be read front to back. Each domain is meant to be a standalone reference. If you're just starting, Domain 1 (site selection) and Domain 6 (energy) are the most common first questions. Domain 16 (skills) is also a good orientation if you're not sure where to start.

---

## Week 2 — Secondary Expansion

Review Week 1 data before deciding which communities to post in next.

| Week 1 Signal | Interpretation | Week 2 Action |
|--------------|---------------|---------------|
| r/preppers outperformed r/offgrid 2:1 or more | Disaster/nuclear angle is the primary draw | Post in r/SHTF with a nuclear-specific angle; consider domain-specific follow-up |
| r/offgrid drove most GitHub traffic | Core off-grid audience is the primary adopter | Post in r/self_reliance; engage follow-up questions in existing threads |
| HN drove significant traffic (> 500 views) | Technical audience is engaged | Post second Dev.to article; submit to relevant awesome lists |
| Twitter drove meaningful engagement | Social amplification is viable | Post a second thread on a different domain (Domain 15 or Domain 13) |
| All channels modest | Distributed, sustained traction | Continue planned supplemental posts; no pivot needed |
| All channels poor (< 200 total upvotes, < 50 stars) | Distribution underperformed | Diagnose: spam filter? Wrong timing? Investigate before reposting |

**Supplemental communities for Week 2+**:

| Subreddit | Size | Angle | Timing |
|-----------|------|-------|--------|
| r/solarpunk | ~200,000 | Community governance + CC BY-SA framing | Week 2 |
| r/self_reliance | ~60,000 | Self-sufficiency philosophy | Week 2 |
| r/SHTF | ~400,000 | Disaster scenarios, nuclear content | Week 2 only if r/preppers underperformed |
| r/sustainability | ~600,000–750,000 | Collective resilience; Domain 13 | Week 2–3 |
| r/solar | ~150,000 | Domain 6 specifically | Week 3 (domain-specific post, not full guide) |
| r/amateurradio | ~180,000 | Domain 11 (Communications) | Week 3 |

**Week 2 non-Reddit actions**:
- [ ] Submit repo to awesome-selfhosted or awesome-sustainable-technology
- [ ] Open 3–5 "help wanted" GitHub issues targeting clear expansion areas
- [ ] Draft one newsletter pitch (use Homestead Honey or Prepared Not Scared as first targets)
- [ ] Draft second Medium article based on highest-traffic domain signals from Week 1

---

## Escalation Matrix: When a Post Underperforms

**Tier 1 response (post is live, low engagement after 1 hour during peak time)**:
1. Check if the post is visible to logged-out users (spam filter test)
2. If filtered: send modmail to the subreddit moderators
3. If not filtered: accept that early velocity did not materialize; do not add calls to upvote in comments

**Tier 2 response (post has been live for 6 hours, fewer than 10 upvotes)**:
1. Analyze: was the timing correct? Was the angle right for this community?
2. Do not repost in the same community for at least 2 weeks
3. If this was the primary community (r/offgrid or r/preppers), advance the next-scheduled community post to compensate
4. Take notes on what the title and framing were — the pattern matters for future posts

**Tier 3 response (post actively downvoted to 0 or negative)**:
1. Read the top critical comment carefully — there may be a substantive objection that deserves a response
2. Respond once, calmly, to the most substantive criticism
3. Do not argue
4. File a GitHub issue for any legitimate content concern raised in the thread
5. Do not delete the post — a deleted post looks worse than a low-scoring one
6. Wait 48 hours before posting in any other community; reconsider the angle

**What NOT to do in any tier**:
- Do not ask friends to upvote (violates Reddit's rules and can trigger account-level action)
- Do not post the same content in multiple subreddits within 24 hours
- Do not edit the post title after it has been submitted
- Do not delete and repost

---

## Weeks 3–4 — Community Building

| Action | Timing | Notes |
|--------|--------|-------|
| Respond to all open GitHub issues | Every 2 days | Even a brief "acknowledged" keeps contributors engaged |
| Twitter thread #2 | Week 3, Tuesday 13:00–15:00 UTC | Topic: "What we learned researching nuclear preparedness" or highest-performing domain |
| Newsletter pitch #1 | Week 3 | Identify 3–5 newsletters; send Homestead Honey or Prepared Not Scared first |
| Contributor spotlight (if PRs received) | Week 4 | Tweet + Reddit mention thanking contributor; update CONTRIBUTORS.md |
| Medium article #2 | Week 4 | Domain 13 (Community) or Domain 1 (Site Selection) |
| CONTRIBUTING.md review | Week 4 if no PRs yet | Add specific "help wanted" examples to lower contribution friction |
| YouTube influencer outreach | Weeks 3–4 | Start with Tier 3 micro-influencers (see toolkit Part 5); send 3–5 outreach messages |

---

## Months 2–3 — Maintenance Mode

**Monthly cadence**:

| Week of Month | Activity |
|--------------|---------|
| Week 1 | Scan open GitHub issues; prioritize 2–3 factual corrections |
| Week 2 | Implement fixes; update CHANGELOG |
| Week 3 | Identify one domain for "deepening" based on issue volume and Reddit questions |
| Week 4 | Publish deepened section; mention on Twitter; note in newsletter if active |

**Monthly metrics review (30-minute session)**:
- GitHub stars trajectory: on track, ahead, or behind model? (See toolkit Part 4)
- Fork:star ratio: above 10%? Above 15%?
- Top referrers: new organic sources appearing?
- Issues: quality increasing over time (field experience, not just requests)?
- Unprompted cross-links: any new communities linking the guide?

---

## Metrics Tracking Spreadsheet Template

Copy this header row into a spreadsheet. Update daily for Week 1, then weekly.

```
Date | GH Stars | GH Star Delta | GH Views | GH Forks | GH Issues Open | GH PRs | Reddit r/offgrid | Reddit r/preppers | Reddit r/homesteading | HN Points | Top Referrer | Notes
```

**Thresholds that trigger action**:

| Signal | Threshold | Action |
|--------|-----------|--------|
| Stars stagnant | < 10 new stars/week after Week 2 | Secondary channel expansion; awesome-list submission |
| Fork:star ratio low | < 8% by Month 1 | Update README with fork-friendly use cases; add CONTRIBUTING.md examples |
| Issue quality high | 3+ issues citing field experience | Prioritize those domains for Month 2 deepening |
| Traffic source unexpected | New domain in referrers | Research that community; engage organically |
| PR submitted | Any PR | Respond within 24 hours; spotlight the contributor publicly |
| Stars exceeding model | > 2x expected rate | Accelerate Phase 3 planning; begin regional expansion |

---

## 30/60/90 Day GitHub Stars Trajectory Model

Use this model to calibrate expectations and trigger decisions. These ranges are based on comparable open-source documentation and knowledge-base projects with niche-community Reddit distribution (no software tool, no viral pre-seeding, no large existing follower base).

### Conservative Trajectory (Reddit distribution only, no HN traction)

| Checkpoint | Stars | Drivers | Warning Signs |
|-----------|-------|---------|--------------|
| Day 7 | 20–80 | r/offgrid post | < 20 = spam filter or poor timing |
| Day 14 | 50–150 | r/preppers, r/homesteading | Stagnation here = secondary channel expansion needed immediately |
| Day 30 | 80–200 | Secondary communities, organic shares | |
| Day 60 | 120–350 | SEO (Medium articles indexing), newsletter mentions | No organic new sources = no compound growth |
| Day 90 | 150–500 | Ongoing organic; community contributors re-sharing | |

### Moderate Trajectory (Reddit + one solid HN post, 20–60 HN points)

| Checkpoint | Stars | Drivers |
|-----------|-------|---------|
| Day 7 | 80–250 | r/offgrid + HN traffic spike |
| Day 14 | 150–400 | All three subreddits complete |
| Day 30 | 200–500 | Secondary communities, first newsletter mention |
| Day 60 | 350–800 | GitHub Trending micro-appearance (requires ~30 new stars/day to trigger) |
| Day 90 | 500–1,200 | Contributor PRs, organic community citations |

### High Trajectory (Front-page HN or viral Reddit post)

| Checkpoint | Stars | Drivers |
|-----------|-------|---------|
| Day 7 | 250–1,000 | Single viral event dominates |
| Day 30 | 500–2,000 | Secondary community spread, influencer mentions |
| Day 60 | 800–3,500 | GitHub Trending appearances begin compounding |
| Day 90 | 1,500–5,000 | Phase 3 actively underway |

### Key Threshold Events

**200 stars**: GitHub "related repositories" algorithms begin surfacing the project to adjacent users. Below this, all discovery is manual distribution.

**500 stars**: Social proof threshold for Tier 2 influencer outreach (YouTube channels 200K–1M). Before this threshold, cold outreach to mid-tier channels is unlikely to convert.

**1,000 stars**: GitHub Trending algorithm begins generating organic daily star accumulation of 10–20 stars/day independent of active distribution. This is the compound-growth inflection point.

### Fork-to-Star Ratio Benchmarks

| Ratio | Interpretation | Action |
|-------|---------------|--------|
| < 5% | Passive bookmarking; low actual use | Improve README with fork-friendly use cases and CONTRIBUTING examples |
| 5–10% | Normal for knowledge-base projects | On track; monitor |
| 10–20% | Active adaptation (regional forks, custom versions) | Feature contributors publicly; add "help wanted" labels |
| > 20% | Exceptional adoption | Consider structured contributor program; Phase 3 |

---

## Phase 3 Gate (Day 30 Decision)

On Day 30, evaluate against these thresholds before committing to Phase 3 (visual content, video guides, domain deepening):

**Proceed to Phase 3 if**:
- GitHub stars >= 300
- At least 1 community-submitted PR received
- Traffic still showing week-over-week growth (not just launch spike)
- Issues opened >= 5 (signal of active engagement)

**Hold at Phase 2 if**:
- GitHub stars < 150
- No PRs received
- Traffic declining to near-zero after launch spike
- Action: stabilize, update content based on GitHub issue feedback, wait 60 days and re-evaluate

**Exceptional case**:
- If stars >= 800 by Day 30, begin Phase 3 planning immediately
- Prioritize: regional guide expansion (Appalachia, Gulf Coast, Pacific Coast) and video companion content for highest-traffic domains; reach out to Tier 1 YouTube influencers with the star count as social proof
