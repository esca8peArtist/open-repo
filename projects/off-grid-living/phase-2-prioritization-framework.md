---
title: "Off-Grid Living Guide — Phase 2 Prioritization Framework"
created: 2026-05-05
status: active
github_url: https://github.com/esca8peArtist/off-grid-living-guide
related: feedback-loop-protocol.md, engagement-metrics-framework.md
---

# Phase 2 Prioritization Framework

## Purpose

Phase 1 covers 17 domains end-to-end. Phase 2 is not about adding another 17 domains — it is about going deeper on the right things, expanding into the right adjacent areas, and building the case studies or practical examples the community has explicitly asked for. This document defines the decision process for choosing what Phase 2 includes, when to green-light it, and which of three expansion paths to take.

---

## Section 1: Data Sources for Prioritization

Phase 2 decisions should be driven by signal, not intuition. Use these four sources in combination.

### 1.1 GitHub Issue Frequency Analysis

Every enhancement issue filed represents one community member who read deeply enough to notice a gap and cared enough to file it. Frequency across multiple issues — or a single issue with many thumbs-up reactions — indicates genuine demand.

**Method**:
- Monthly, export all open issues labeled `enhancement` or `phase-2-candidate`
- Sort by: (a) number of independent mentions of the same topic across issues and comments, and (b) thumbs-up reactions on individual issues
- Build a frequency table of gap topics

**Example frequency table** (hypothetical, to illustrate):

| Topic / Gap | Issues filed | Cross-platform mentions | Total signals |
|-------------|-------------|------------------------|---------------|
| Composting / humanure systems | 4 | r/homesteading ×2, HN ×1 | 7 |
| Rainwater harvesting legal status by state | 3 | r/offgrid ×3 | 6 |
| Livestock integration (chickens, goats) | 2 | r/homesteading ×4 | 6 |
| Greywater system design | 3 | r/sustainability ×1 | 4 |
| Passive solar building design | 2 | Twitter ×1 | 3 |
| Tropical/subtropical regional guide | 1 | r/offgrid ×2 | 3 |

**Cutoff for Phase 2 candidacy**: Any topic with 4+ total signals across at least 2 independent sources.

### 1.2 GitHub Insights Traffic Analysis

GitHub's Insights tab shows referrer sources and — crucially — the search terms driving people to the repository from Google. This is the most direct signal of search-intent demand.

**What to check**:
- Navigate to: Repository → Insights → Traffic → Referring Sites
- Note the top organic search referrers (these are often Google search queries surfaced through the URL)
- Check GitHub's "Popular content" view (shows which files/pages within the repo get the most direct views)

**Interpretation**:
- A domain document that receives disproportionate direct traffic (e.g., Domain 3 Water gets 3x more views than average) suggests it is being reached via search and bookmarked/shared separately
- Referrer domains outside your distribution channels (e.g., traffic from a forum you never posted to, or from an education site) indicate organic adoption and search discovery

**Limitation**: GitHub Insights does not show the specific Google search terms that led to the repo — only that Google was the referrer. To get actual search terms, you need to add the repo to Google Search Console (free, 5-minute setup) via DNS verification.

**Google Search Console setup** (if growth justifies it):
- Add property at search.google.com/search-console
- Verify ownership via a DNS TXT record on your domain (if you have a custom domain) or via an HTML file in the repo
- After 2–4 weeks of data collection, check Performance → Queries to see which search terms bring traffic
- These queries are the highest-confidence signal for Phase 2 content because they represent unsatisfied search intent

### 1.3 Comment Text Mining for Term Gaps

Comments across platforms often contain terminology that appears nowhere in Phase 1. These terms signal concepts the community considers related and expects to find.

**Manual method** (monthly, 30 minutes):
- Open the top 20 most-commented threads from the past month
- Read comments for technical terms, domain-specific vocabulary, or named techniques not covered in the guide
- List them: "aquaponics," "swales," "food forest," "IMO / bokashi fermentation," "passive annual heat storage (PAHS)"
- Cross-reference against Phase 1 documents: is this term mentioned or handled?
- Terms that appear 3+ times in comments but have no Phase 1 coverage = content gap signals

**What this produces**: A vocabulary list of community mental models. The community's language is the community's search behavior — if they use a term repeatedly in comments, they are searching for it independently.

### 1.4 Comparative Content Benchmarking

Check what the top 3–5 most-cited competing resources cover that Phase 1 does not. This is not about copying — it is about identifying what readers expect in a comprehensive off-grid guide.

**Method**:
- Search for "off-grid living guide," "homesteading guide," "preparedness guide" on Google
- Identify the top 3 non-commercial, non-paywalled results
- Skim their table of contents / topic lists
- Note topics they cover that Phase 1 does not

**Filter**: Only flag topics that also appear in the community feedback (GitHub issues or comment terms). Topics that exist in competitor content but never appear in community requests may simply not be relevant to your audience.

---

## Section 2: Decision Rubric — Urgency vs. Strategic Fit

Not every gap should be filled. Use this 2x2 rubric to classify candidates before committing resources.

### The Rubric

**Urgency axis** (how frequently and specifically is this requested?):
- High urgency: mentioned 5+ times independently, with specificity (people describe exact scenarios)
- Low urgency: mentioned 1–2 times, or mentioned vaguely ("you should cover more about water")

**Strategic fit axis** (does this advance the guide's core purpose?):
- High fit: serves the existing audience (people planning or actively building off-grid systems), fills a gap in the core 17-domain framework, or creates a regional guide for an underserved geography
- Low fit: adjacent topic that serves a different audience (e.g., hunting skills — relevant to preppers but not core to the guide's framework), requires substantial new primary research with uncertain accuracy, or primarily serves Phase 2 marketing goals rather than reader utility

**Classification matrix**:

| | High urgency | Low urgency |
|---|---|---|
| **High strategic fit** | Build first — Phase 2 core | Evaluate — include if scope allows |
| **Low strategic fit** | Decline gracefully or scope narrowly | Skip — redirect to other resources |

**Note on scope creep**: The guide's 17-domain structure is a strength, not a limitation. "Domain 18" should be added only when the existing domains cannot accommodate the topic. Most gap requests are actually deepenings of existing domains (more detail in Domain 3 Water, more regional variation in Domain 1 Site Selection) rather than genuinely new domains.

---

## Section 3: Three Phase 2 Expansion Paths

Choose at most two of these paths per Phase 2 cycle. Attempting all three simultaneously fragments effort and degrades quality.

### Path A — Fill Comment-Identified Gaps (Depth Expansion)

**What it is**: Deepen existing domains with specific sections, sub-topics, or case studies that the community has repeatedly identified as missing.

**Best for**: Error reports that revealed oversimplification, feature requests with 5+ community endorsements, topics that appear in comment threads but have zero Phase 1 coverage.

**Examples** (drawn from typical off-grid community feedback patterns):
- Domain 3 (Water): Add a "Rainwater Harvesting Legal Status by State" appendix
- Domain 4 (Food Production): Expand to include small livestock (chickens, rabbits, goats) with real cost and labor data
- Domain 6 (Energy): Add a dedicated "battery bank maintenance and replacement cycle" section
- Domain 9 (Waste/Sanitation): Add composting toilet design options with cost comparison

**Effort profile**: Medium. These require primary source research but fit within the established document structure. Each deepening adds 200–600 lines to an existing domain document rather than creating a new one.

**Success signal that Path A is working**: New issues filed on Path A content drop to <1/month per topic (saturation); issues shift to other domains (the gap queue moves).

### Path B — Expand Into Adjacent Domains

**What it is**: Add genuinely new domains that are adjacent to the existing 17 but not covered. These are not depths — they are genuinely new topic areas.

**Best for**: Topics with high community demand AND high strategic fit that cannot be handled within existing domain structures.

**Viable candidates** (based on typical off-grid community interests not currently in the guide):
- Domain 18: Permaculture Design Principles — integrates Domains 1, 4, and 7; provides the design methodology that connects site selection, food systems, and climate management. High demand in r/homesteading and r/solarpunk.
- Domain 19: Water Systems Engineering — a deep-dive beyond Domain 3's operational coverage, covering gravity-fed systems, spring development, well drilling and maintenance, water testing protocols. Consistently requested by practitioners.
- Domain 20: Animal Husbandry — livestock as food security systems, including chickens, goats, pigs, and rabbits. High demand signal in r/homesteading.

**Effort profile**: High. New domains require 1,000–2,000 lines of primary research, the same structure as existing domains (costs, regional variation, decision matrices). Only justify with strong evidence from Phase 1 feedback.

**Go/no-go filter for Path B**: A candidate domain should have 8+ independent community signals before proceeding. Fewer than that, and you are building speculatively.

### Path C — Case Studies and Detailed Guides

**What it is**: Create standalone case studies, worked examples, or step-by-step implementation guides tied to high-interest topics. These are not encyclopedic domain documents — they are practical, narrative-driven, first-person or composite examples.

**Best for**: Topics where the community understands the theory (Phase 1 covers it) but wants implementation detail ("how did you actually do this?"). Also effective for converting passive readers to active contributors — case studies invite personal stories.

**Examples**:
- "Budget off-grid cabin in the Pacific Northwest: a $45,000 full-system build case study"
- "Year-one food production: what we grew, what failed, what it actually cost in the Upper Midwest"
- "Solar sizing walkthrough: sizing a 3kW system for a 1,000 sq ft cabin in the Southwest"
- "Community governance in practice: how three households manage a shared 40-acre property"

**Effort profile**: Low-to-medium if sourced from community contributors. High if self-researched. The ideal model: issue a GitHub Discussion or Reddit thread asking the community for their real-world case study data, compile into a structured document, credit contributors.

**Why Path C often outperforms A and B on engagement**: Case studies are shareable stories, not reference documents. A case study post on Reddit ("Here's how we built a 3kW off-grid solar system for $12,000 — full cost breakdown") outperforms a documentation post by 3–5x on engagement metrics in homesteading and off-grid communities. Path C content is distribution fuel, not just reference material.

---

## Section 4: Go/No-Go Decision Timeline

### 4.1 Decision Gates

**Gate 1 (Month 1): Traction confirmed?**

Inputs: GitHub stars, Reddit upvotes, issues filed.

Decision:
- YES (250+ stars, 10+ issues): Move to feedback aggregation — run the monthly review template from `feedback-loop-protocol.md`, build the frequency table from Section 1.1 above
- NOT YET: Continue Phase 1 distribution, add secondary channels (r/solarpunk, r/SHTF, Medium article 2)
- NO (below 80 stars, zero issues after all posts published): Reassess — this is a distribution problem, not a content problem. Audit the README framing and title before investing in Phase 2.

**Gate 2 (Month 2–3): Phase 2 scope defined?**

Inputs: Frequency table from monthly reviews, GitHub Insights referrer analysis, Google Search Console (if set up).

Decision:
- Select ONE primary path (A, B, or C) based on signal distribution
- Identify top 3 specific items within that path (e.g., Path A: composting toilets, rainwater legal appendix, livestock expansion)
- Write a Phase 2 scope document with those 3 items, estimated effort per item, and contribution opportunities

**Gate 3 (Month 3–4): Community building?**

Inputs: PRs submitted, quality contributor identification (see Section 4.2), CONTRIBUTING.md quality.

Decision:
- If 2+ quality contributors have emerged: invest in the contributor pipeline (GOVERNANCE.md, regular contributor calls or async updates)
- If zero contributors: Phase 2 proceeds as solo effort; lower the contribution barrier (more `good-first-issue` labels, simpler CONTRIBUTING.md)

### 4.2 Identifying Quality Contributors

Not all contributors are equal. Quality contributors are rare and worth specific investment. They are characterized by:

- Submitting comments with primary source citations rather than assertions ("according to NRPA 2023 standards, the value should be...")
- Filing issues that include proposed solutions, not just complaints
- Asking for clarification before submitting a PR (indicates they read the CONTRIBUTING.md and are trying to match the guide's standards)
- Subject matter expertise signals: their Reddit or GitHub profile shows sustained engagement with the topic, not first-time comments

**Routing quality contributors toward Phase 2**:
1. Respond to their issue or comment with explicit encouragement: "This is exactly the kind of depth we need in Phase 2 — would you be interested in contributing to an expansion of Domain X?"
2. Tag their issue `good-first-issue` if the scope is manageable, or create a new issue specifically scoped for them
3. For substantive contributors: invite them to a CONTRIBUTORS.md acknowledgment and note that sustained contribution can earn co-author credit on Phase 2 expansions

**Community governance model** (appropriate at this project's scale):

The guide does not need a formal governance committee at Phase 2 scale. A lightweight BDFL (Benevolent Dictator For Life) model is appropriate: one maintainer (you) holds final editorial authority, with documented norms for contributions (CONTRIBUTING.md) and a clear signal that PRs are welcome. Formalize governance (voting on direction, co-maintainers, steering committee) only when the contributor base exceeds 10 active people — before that, process overhead exceeds its benefit.

---

## Section 5: SEO Long-Tail Strategy for Phase 2

### 5.1 Search Term Gap Analysis

Google Search Console (once set up) will show which search queries are already driving traffic to the guide. The gap analysis asks: what terms appear in comments but do NOT appear in Search Console as active traffic sources? These are content gaps with proven demand but zero current coverage.

**Example gap pattern**:
- Comments contain: "aquaponics," "food forest," "biochar," "swales"
- Search Console shows: zero traffic for these terms
- Conclusion: these topics are in the community's mental model but the guide doesn't cover them — Google can't rank content that doesn't exist

**Phase 2 SEO priority formula**: (comment frequency of term) × (estimated monthly search volume) × (absence from existing guide) = prioritization score. The highest-priority targets are terms that are frequently mentioned in comments, have meaningful search volume, and have no Phase 1 coverage.

**Practical estimation of search volume without paid tools**: Use Google Autocomplete and "People also ask" to assess relative demand. A query that generates 10 autocomplete suggestions has more search volume than one that generates 2. For more precision, Google Keyword Planner (free with a Google Ads account, no spend required) provides search volume ranges.

### 5.2 Domain Depth vs. New Domain SEO Tradeoff

Adding a new domain (Path B) creates a new URL and can rank independently. Deepening an existing domain (Path A) improves dwell time and topical authority on existing pages. For SEO purposes:

- Path A (depth) builds topical authority and tends to improve rankings for the entire domain document, not just the added section — Google rewards comprehensive documents on specific topics
- Path B (new domains) creates new ranking opportunities but requires building authority from zero
- Path C (case studies) performs best for long-tail, narrative search queries ("how much does it cost to build an off-grid solar system") and is most likely to generate backlinks — the primary driver of domain authority

**Recommendation**: For Phase 2 SEO, lead with Path A (depth) and one Path C case study. Path B (new domains) should follow only if community signal is strong, not primarily for SEO.

---

## Sources

- [Content Gap Analysis 2026: 10 Tips For AI Search](https://www.yotpo.com/blog/modern-content-gap-analysis/) — Yotpo (gap prioritization methodology)
- [SEO Gap Analysis: How to Find Content and Keyword Gaps](https://searchengineland.com/guide/gap-analysis) — Search Engine Land (search intent vs. content coverage)
- [Leadership and Governance — Open Source Guides](https://opensource.guide/leadership-and-governance/) — GitHub Open Source Guides (governance models, BDFL vs. committee)
- [Governance in Practice: How Open Source Projects Define Roles](https://arxiv.org/html/2603.24879) — arXiv (empirical study of governance artifacts in OSS projects)
- [Open Source Contributor Onboarding: 10 Tips](https://daily.dev/blog/open-source-contributor-onboarding-10-tips) — daily.dev (good-first-issue impact, contributor pipeline)
- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/) — GitHub Open Source Guides (contributor motivation and onboarding mechanics)
- [Understanding Open Source Governance Models](https://www.redhat.com/en/blog/understanding-open-source-governance-models) — Red Hat (BDFL, committee, foundation models)
- [GitHub SEO: Rank Your Repo and Get Adoption in 2026](https://nakora.ai/blog/github-seo) — Nakora (repository optimization, search visibility)
- [The Ultimate Guide to GitHub SEO for 2025](https://dev.to/infrasity-learning/the-ultimate-guide-to-github-seo-for-2025-38kl) — DEV Community (GitHub search and Google indexing mechanics)
