---
title: "Off-Grid Living Guide — Feedback Loop Protocol"
created: 2026-05-05
status: active
github_url: https://github.com/esca8peArtist/off-grid-living-guide
related: engagement-metrics-framework.md, phase-2-social-media-execution-toolkit.md
---

# Feedback Loop Protocol

## Purpose

This document defines how to systematically harvest, categorize, and act on feedback from all distribution channels. The goal is to turn community engagement — Reddit comments, HN threads, GitHub issues, Twitter replies — into structured intelligence that informs Phase 2 content decisions. Without a formal categorization system, valuable signals get lost in notification noise.

This protocol is designed to be executable with no tooling beyond a spreadsheet and periodic manual review.

---

## Section 1: Comment Parsing Framework

### 1.1 The Four-Category Taxonomy

Every piece of community feedback falls into one of four categories. Train yourself to file it immediately when you see it:

**Category A — Error Reports**
Definition: A specific factual claim in the guide is incorrect, outdated, or misleading.

Signals: "That solar sizing formula is wrong for AGM batteries," "NCRP guidance was updated in 2024," "The cost estimate in Domain 6 assumes 2022 prices."

Weight: Highest urgency. Error reports damage trust and can result in readers making costly mistakes. Address within 48 hours.

Response protocol:
1. Acknowledge in the comment thread within 24h ("Thank you — I'll look into this and file a GitHub issue.")
2. Open a GitHub issue immediately with the label `bug` or `factual-error`
3. Verify with the original source cited in the document (FEMA, CDC, NCRP, cost databases)
4. Correct the document within 7 days if verified; close the issue with a note to the reporter
5. If you cannot verify either way: leave the issue open, add a "needs verification" label, and note it in the monthly review

**Category B — Feature Requests / Gap Identification**
Definition: Content that doesn't exist in the guide but the community wants.

Signals: "You don't cover composting toilets," "What about rainwater legality by state?", "Missing guidance on keeping livestock as a food source," "You should add a tropical climate regional guide."

Weight: Phase 2 input queue. File immediately; do not commit to building any specific item yet.

Response protocol:
1. Acknowledge warmly: "Great call — I've flagged this for Phase 2 consideration."
2. Open a GitHub issue with the label `enhancement` or `phase-2-candidate`
3. Note the source (which platform, which post) so you can assess frequency later
4. Do not promise timelines. You are gathering, not committing.

**Category C — Enthusiasm Signals**
Definition: Positive reactions that don't contain specific feedback.

Signals: "This is incredible," "Bookmarked," "Sharing this with my group," "Finally a comprehensive guide that doesn't require buying a course."

Weight: Morale and social proof. Use sparingly as evidence of product-market fit when making Phase 2 pitch decisions. Do not over-index on enthusiasm alone — it's the least actionable signal.

Response protocol:
1. Brief acknowledgment in the comment thread (optional — not required for every positive comment)
2. Screenshot or note the most substantive enthusiastic comments for the monthly review ("what resonated" section)
3. Identify whether enthusiasm is concentrated in a specific domain (people saying "Domain 6 is gold") — this is a content strength signal

**Category D — Neutral / Off-Topic**
Definition: Comments that are tangentially related, entirely off-topic, or purely conversational.

Weight: Low. File nothing unless the commenter asks a question that reveals a genuine gap (which would make it Category B).

Response protocol:
1. Brief reply if directly asked a question
2. No filing required
3. Do not let this category consume disproportionate response time

---

### 1.2 Manual Sentiment Triage Process

Rather than deploying automated sentiment analysis tools (which require setup overhead), use this structured manual process. It takes 15–20 minutes per platform per week and is more accurate for niche technical content than lexicon-based tools like VADER (which are calibrated for general social media language, not domain-specific technical discourse).

**Weekly triage ritual (Fridays, 20 minutes)**:

1. Open each active platform (Reddit threads, HN post, Twitter thread, GitHub issues) in sequence
2. Read every new comment from the past 7 days
3. For each comment, ask: "Does this contain (A) a specific error report, (B) a gap or feature request, (C) pure enthusiasm, or (D) nothing actionable?"
4. File A and B items immediately into the Issue Tracker (see Section 2)
5. Note the 1–2 most interesting C items in the monthly review doc

**Volume thresholds for escalation**: If you receive more than 20 new comments per platform per week, start using categories as a filter: read all comments that are longer than 50 words first (these are almost always A or B); skim shorter ones for explicit error language ("wrong," "incorrect," "missing," "should include").

---

### 1.3 Automated Tooling (Optional, Low-Overhead)

If comment volume grows to 50+ per week across platforms, consider these lightweight approaches:

**VADER (free, no API key)**: Python's `vaderSentiment` library can classify Reddit/HN comments as positive/negative/neutral in bulk. Useful for detecting spike events (a sudden surge of negative sentiment may indicate an error report got amplified). Run weekly against any thread with 10+ comments. Install: `pip install vaderSentiment`. Limitation: calibrated for casual social media language; technical corrections often read as neutral even when they contain substantive criticism.

**TextBlob (free, simple)**: Provides polarity and subjectivity scores. Run a simple loop over comment text to identify polarity < -0.2 (likely criticism) for manual review. Better as a filter than a classifier.

**Manual wins over automation at this scale**: For a guide generating 20–100 comments per week, manual triage is more accurate and takes comparable time to running automated scripts. Reserve automation for when weekly comment volume exceeds 200.

---

## Section 2: GitHub Issue Routing

### 2.1 Issue Classification and Labels

Set up these GitHub labels before the first distribution post goes live:

| Label | Color | Meaning |
|-------|-------|---------|
| `bug` | Red | Factual error in the guide |
| `factual-error` | Orange | Specific data point that is wrong or outdated |
| `enhancement` | Blue | Valid request for new content |
| `phase-2-candidate` | Purple | Confirmed gap that belongs in Phase 2 planning |
| `good-first-issue` | Green | Accessible task for a new contributor |
| `needs-verification` | Yellow | Error report that cannot be confirmed without primary source check |
| `domain-[N]` | Gray | Domain-specific tag (domain-6 = Energy, domain-4 = Food, etc.) |
| `regional` | Teal | Regional guide gap or request |

**Tagging 20–25% of open issues as `good-first-issue`** is the single highest-leverage contributor acquisition action. Research on open-source projects shows this label is associated with a 13% increase in new contributor submissions. Good candidates for this label: fixing a broken link, correcting a unit (gallons to liters), adding a missing cost reference, or filling in a specific factual gap in a domain you've already researched.

### 2.2 Response SLA

| Issue type | First response SLA | Resolution SLA |
|------------|-------------------|---------------|
| Factual error (verified) | 24 hours | 7 days |
| Factual error (unverified) | 24 hours | 30 days or "needs-verification" label |
| Enhancement request | 48 hours | Deferred to Phase 2 (acknowledge with timeline) |
| Good-first-issue PR | 48 hours | Review and merge within 7 days if correct |
| Substantive PR (new content) | 48 hours | Review within 14 days; provide detailed feedback |

**What to say when you can't act immediately**: "Thanks for filing this — I've labeled it `phase-2-candidate` and it will be reviewed in the monthly planning cycle. If you have primary source citations to back this up, adding them to this issue will accelerate its inclusion."

### 2.3 When to Incorporate vs. Defer

**Incorporate immediately** (make a fix without waiting for Phase 2):
- Factual errors verified against primary sources
- Broken links
- Typographical errors that change meaning
- Unit conversions that are clearly wrong

**Defer to Phase 2 scoping** (do not commit to individual requests):
- New sections or domains
- Expanded regional coverage
- New appendices or reference tables
- Any content addition that requires primary research you haven't done

**Decline gracefully**:
- Content that falls outside the scope of the guide (commercial product recommendations, adjacent skills like blacksmithing)
- Contributions that duplicate existing content
- Issues that are really just personal preferences ("I would have organized this differently")

---

## Section 3: Email Feedback Integration

If an email list is added, integrate feedback through this lightweight mechanism:

**Segment subscribers at signup** (3-question form, optional):
1. "Where are you in your off-grid journey?" → Planning / Early stages / Actively homesteading / Researching only
2. "Which topic brought you here?" → Energy / Water / Food / Shelter / Emergency prep / Community / Other
3. "Geographic region?" → Northeast / Southeast / Midwest / Pacific Northwest / Southwest / Non-US

These segments directly map to Phase 2 prioritization. If 40% of email subscribers selected "Water" as their primary interest, that's a strong signal to expand Domain 3 (Water Systems) in Phase 2.

**Email-to-GitHub bridge**: Every email that contains substantive feedback (error report, gap identification) should be converted to a GitHub issue. Reply to the email with the issue URL. This creates a durable record and keeps feedback visible to the broader community.

**Unsubscribe pattern analysis**: Track which email subject lines (domains, topics) correlate with unsubscribes above your 0.5% baseline. High unsubscribe rate on a specific topic = that topic isn't why people subscribed. Low unsubscribe + high forward rate = your core value proposition.

---

## Section 4: Sentiment Thresholds for Phase 2 Decision

These thresholds define when feedback volume is sufficient to make confident Phase 2 decisions.

### 4.1 Trigger Conditions

**Phase 2 content inventory is justified** when any ONE of these is true:
- 15+ GitHub issues filed with `enhancement` or `phase-2-candidate` labels
- A single content gap mentioned independently in 3+ separate threads across different platforms
- A GitHub issue with 5+ "thumbs up" reactions (community endorsement of a gap)
- Email subscriber segment >35% interested in a topic not well-covered in Phase 1

**Phase 2 full planning is justified** when ALL THREE of these are true:
- 250+ GitHub stars (community adoption is real, not just traffic)
- 15+ enhancement issues (concrete gap identification)
- At least one Phase 1 distribution post exceeded 200 upvotes on Reddit (audience validated)

**Phase 2 prioritization confidence is high** when you can answer YES to all of these:
- Is this gap mentioned in multiple independent sources (Reddit + GitHub + Twitter)?
- Does the gap appear in referral traffic search terms from GitHub Insights?
- Would filling this gap serve existing guide users (deepening), not only new audiences (expansion)?

---

## Section 5: Monthly Review Template

Execute this review on the first Monday of each month. Takes 60–90 minutes. Write the output into a plain text file or running doc.

```
MONTHLY REVIEW — [MONTH YEAR]

1. WHAT HAPPENED THIS MONTH?

GitHub status:
  Stars: ___ (Δ from last month: ___)
  Forks: ___
  New issues: ___
  Issues resolved: ___
  PRs merged: ___

Distribution activity this month:
  Posts published: [list with subreddit/platform and upvote count]
  Biggest performing post: _______________  (___upvotes / ___comments)
  Worst performing post:   _______________  (___upvotes / ___comments)
  Traffic sources (top 3 from GitHub Insights): _______________

2. WHAT DID WE LEARN THIS MONTH?

Error reports filed: ___  Verified and fixed: ___  Pending: ___

Top content gaps identified (list up to 5, with source):
  1. Gap: _______________  Source: _______________  Frequency: ___x mentioned
  2. Gap: _______________  Source: _______________  Frequency: ___x mentioned
  3. Gap: _______________  Source: _______________  Frequency: ___x mentioned
  4.
  5.

Top enthusiasm signals (what resonated):
  - _______________
  - _______________

Community dynamics (unexpected observations):
  - _______________

3. WHAT SHOULD PHASE 2 ADDRESS?

Carry forward from last month (unresolved high-priority gaps):
  - _______________

New high-priority candidates this month:
  - _______________

Confirmed Phase 2 candidates with multiple independent signals:
  - _______________

4. DECISION: ARE WE AT THE PHASE 2 THRESHOLD?

Stars vs. threshold (250 min): ___  → YES / NO / APPROACHING
Enhancement issues filed: ___  → YES (15+) / NO
Any post 200+ upvotes: ___  → YES / NO

Overall: PROCEED with Phase 2 scoping / NOT YET — continue Phase 1 distribution / REASSESS distribution strategy

5. NEXT MONTH'S PRIORITIES

Distribution (1–2 actions max):
  - _______________

Maintenance (error fixes, link updates):
  - _______________

Community (contributor onboarding, PR reviews):
  - _______________
```

---

## Sources

- [Open Source Community Mailing List Sentiment Analysis](https://dl.acm.org/doi/10.1145/3306446.3340824) — ACM OpenSym (sentiment patterns in release cycles)
- [Top 7 Open Source Sentiment Analysis Tools](https://aimultiple.com/open-source-sentiment-analysis/) — AIM Multiple (VADER, TextBlob, spaCy tooling)
- [Open Source Contributor Onboarding: 10 Tips](https://daily.dev/blog/open-source-contributor-onboarding-10-tips) — daily.dev (good-first-issue effectiveness, 13% increase in contributors)
- [Leadership and Governance — Open Source Guides](https://opensource.guide/leadership-and-governance/) — GitHub Open Source Guides (role definition, governance structures)
- [Project and Community Governance — The Open Source Way](https://guidebook.theopensourceway.org/growing-contributors/project-and-community-governance) — Red Hat (contributor pipeline, peripheral to central participation)
- [Best Python Sentiment Analysis Libraries](https://www.bairesdev.com/blog/best-python-sentiment-analysis-libraries/) — BairesDev (VADER, TextBlob, Flair comparison)
