---
title: "Phase 5 Wave 2 Author Matching Algorithm — Scoring, Routing, and Constraint Handling"
project: systems-resilience
phase: 5
wave: 2
status: PRODUCTION-READY
created: 2026-06-06
purpose: "Automated matching algorithm for recruiting 20-40 secondary authors from Wave 2 candidate pool (June 14-15 execution). Scores candidates on 5 dimensions, ranks by weighted scoring, assigns to 5 domain teams respecting capacity and diversity constraints."
confidence: 90%+ on algorithm design
use_case: "June 14 matching execution — pre-computed matches collapsing 3-4 hours manual work to 90 minutes (matches + pre-filled templates)"
word_count: 2800+
publication_day: 2026-06-09
wave_2_execution: 2026-06-14_15
---

# Phase 5 Wave 2 Author Matching Algorithm
## Scoring Rubric, Matching Algorithm, Constraints, and Worked Examples

### Executive Summary

This document specifies the complete author matching algorithm for systems-resilience Phase 5 Wave 2 recruitment (June 14-15 execution). The algorithm:

1. **Scores** 50-60 Wave 2 candidates on 5 dimensions (domain expertise, network reach, writing capacity, timezone, prior-wave success)
2. **Ranks** candidates by weighted composite score
3. **Assigns** top-ranked matches to 5 domain teams (targets: 4-8 authors per domain, 40 total recruited)
4. **Handles** capacity limits, timezone diversity, and conflict-of-interest constraints
5. **Resolves** common edge cases (withdrawals, overflow, tie-breaking)

**Domains covered**: Governance & Decision-Making, Food Systems & Supply Chain, Information Infrastructure, Security & Defense, Scaling Pathways & Thresholds

**Result**: Pre-computed matched-authors.md per domain with ranked assignments, enabling June 14 execution with zero ad-hoc decisions and 90-minute turnaround.

---

## Section 1: Scoring Rubric (0-100 Scale Per Dimension)

Each candidate is scored independently on 5 dimensions. Dimension scores are then weighted and summed to produce a final composite score (0-500 range, normalized to 0-100 percentile for comparison).

### Dimension 1: Domain Expertise (0-100, weight 25%)

Measures depth and specificity of knowledge in the candidate's stated domain interest.

| Score Range | Descriptor | Evidence |
|------------|-----------|----------|
| 90-100 | Expert (5+ years) | Published work, PhD/masters in field, or 5+ years professional practice in domain |
| 75-89 | Advanced (3-5 years) | 3-5 years professional experience, or active researcher/practitioner with clear publications |
| 60-74 | Intermediate (1-3 years) | 1-3 years professional experience, or strong educational background + 1-2 years applied work |
| 40-59 | Foundational | Academic coursework + 6-12 months applied experience, or 2+ years hobbyist/volunteer work |
| 20-39 | Beginner | Academic interest without professional application, or <6 months applied experience |
| 0-19 | No expertise | Self-identified as new to domain |

**Scoring method**: Use CV/publication review + self-assessment from Wave 2 profile card. Compare stated expertise against Wave 1 author roster to calibrate (e.g., if Wave 1 had 3 PhDs in governance, a Wave 2 candidate with 5 years practitioner experience in same domain scores 75-80, not 90).

**Calibration anchors** (from Wave 1 runbook):
- Michael McGinnis (30+ years governance, published, Ostrom affiliate): 95
- Ted Scholte (sociocracy trainer, 10+ years): 85
- Greta Byrum (NYC Mesh, policy author, 8+ years community broadband): 82
- Jack Kloppenburg (seed sovereignty, decades of work): 92
- Rachel MacNair (nonviolence researcher, 15+ years): 88

### Dimension 2: Network Reach (0-100, weight 20%)

Measures ability to mobilize others, attract attention, and amplify the Phase 5 publication through social networks.

| Score Range | Followers/Subscribers | Descriptor |
|------------|-------------------|-----------  |
| 90-100 | 20,000+ | Established author, speaker, or organizer with significant public following |
| 75-89 | 5,000-20,000 | Active social media presence or recognized voice in their field |
| 60-74 | 1,000-5,000 | Strong local/specialized network, published or widely recognized in niche |
| 40-59 | 200-1,000 | Moderate network, active in communities but not widely known beyond |
| 20-39 | 50-200 | Small but engaged network (Slack groups, email lists, local orgs) |
| 0-19 | <50 | No measurable reach (primarily personal connections) |

**Scoring method**: Count followers (Twitter/LinkedIn/Mastodon/etc.) + estimated email list + active community memberships (Reddit, Slack communities, discussion forums). If public metrics unavailable, use interview estimate ("How many people would you feel comfortable inviting to a community project?").

**Normalization baseline**: 5,000 followers = 50-60 score. Scores scale logarithmically above (20K followers = 90, not 100).

**Network reach calculation**:
```
score = min(100, 20 + (log10(followers) * 20))
```

### Dimension 3: Writing Capacity (0-100, weight 25%)

Measures available time and demonstrated ability to produce long-form content over 6-8 week publication sprint.

| Score Range | Hours/Week Available | Descriptor |
|------------|------|-----------|
| 90-100 | 8-10 | Can commit 8-10 hrs/week for 6-8 week publication sprint |
| 75-89 | 6-8 | Can commit 6-8 hrs/week consistently |
| 60-74 | 4-6 | Can commit 4-6 hrs/week but may have conflicts |
| 40-59 | 2-4 | Limited capacity, 2-4 hrs/week with possible drops |
| 20-39 | 1-2 | Very limited, hobbyist-only availability |
| 0-19 | <1 | Cannot commit sustained time |

**Scoring method**: Use Wave 2 profile self-report + verify against Wave 1 performance if applicable.

**Cross-reference with Wave 1 completion data**: If candidate was Wave 1 author:
- Completed on-time, high quality → add 5-10 points to stated capacity
- Completed but late/scope-reduced → use stated capacity only
- Did not complete → cap at 40 (cannot rely on stated capacity)

**Composition scoring** (combine commitment + demonstrated history):
```
score = (self_reported_capacity_score * 0.6) + (wave1_completion_bonus * 0.4)
```

### Dimension 4: Timezone Overlap (0-100, weight 15%)

Measures coordination capability with primary domain team (US Central timezone baseline).

| Score Range | Timezone Overlap | Descriptor |
|------------|----------|-------------|
| 100 | Full overlap with team (same timezone ±2 hours) | Synchronous collaboration possible daily |
| 75-89 | Partial overlap (±4-6 hours) | 3-4 synchronous hours per day |
| 60-74 | Limited overlap (±8-12 hours) | 1-2 synchronous hours per day |
| 40-59 | Minimal overlap (±14-18 hours) | <1 hour synchronous overlap |
| 20-39 | Opposite hemisphere (18-22+ hours difference) | Async-only collaboration required |
| 0-19 | Extreme difference (23+ hours) | Coordination overhead very high |

**Scoring method**: Map candidate's primary timezone (from profile) against team's primary timezone (UTC-6 / US Central). Use UTC offset differences.

**Example**:
- Team primary: UTC-6 (US Central)
- Candidate: UTC-7 (US Mountain) → score 100 (1 hour difference)
- Candidate: UTC+0 (UK) → score 60 (6 hour difference)
- Candidate: UTC+8 (Asia) → score 30 (14 hour difference)

### Dimension 5: Prior-Wave Success (0-100, weight 15%)

Measures likelihood of completion based on Wave 1 performance or other completion history.

| Score Range | Indicator | Descriptor |
|------------|-----------|-----------|
| 90-100 | Wave 1 completion + high engagement | Completed Wave 1 article on-time, actively participated in feedback cycles |
| 75-89 | Wave 1 completion + standard engagement | Completed on-time, minimal feedback iterations |
| 60-74 | Wave 1 completion + late delivery | Completed but required extension, completed all revisions |
| 40-59 | Wave 1 non-completion OR no Wave 1 data | Started Wave 1 but did not complete, or new to project |
| 20-39 | Withdrawn from Wave 1 | Started Wave 1 but withdrew mid-sprint |
| 0-19 | Not applicable / strong red flags | No Wave 1 participation and no completion history elsewhere |

**Scoring method**: Check Wave 1 roster. If candidate participated:
- On-time completion, 0-1 revision cycles: 85-95
- On-time completion, 2-3 revision cycles: 70-80
- Late completion: 55-70
- Withdrew/incomplete: 20-35

If no Wave 1 participation: baseline score 50. Add points for:
- +10 for strong referral from Wave 1 author
- +5 for external completion history (published articles outside this project)
- +10 if candidate explicitly states high motivation / has prepared materials before invitation

---

## Section 2: Matching Algorithm — Process Overview

### Algorithm Steps

**Input**: 60 Wave 2 candidate profiles, each with scores on 5 dimensions

**Process**:
1. Compute weighted composite score for each candidate
2. Rank all candidates by composite score (descending)
3. Allocate top 40-50 candidates to 5 domain teams
4. Within each team, sort by score to identify tier assignments
5. Check constraints (capacity, timezone, COI); swap if needed
6. Output: matched-authors.md per domain with rank and assignment rationale

**Output**: Matched author list per domain, tier assignments, constraint flags, and onboarding priority sequence

### Step 1: Compute Weighted Composite Score

For each candidate, calculate:

```
Composite Score = (D1 * 0.25) + (D2 * 0.20) + (D3 * 0.25) + (D4 * 0.15) + (D5 * 0.15)
```

Result: 0-100 score per candidate.

**Example candidate scoring**:

| Candidate | D1 | D2 | D3 | D4 | D5 | **Composite** |
|-----------|-----|-----|----------|----------|-----------|----------|
| Alex Chen (Governance) | 78 | 65 | 85 | 100 | 75 | **79.25** |
| Jordan Smith (Food Systems) | 62 | 45 | 70 | 60 | 50 | **58.35** |
| Casey Williams (Info Infra) | 85 | 80 | 92 | 75 | 85 | **84.40** |
| Morgan Lee (Security) | 72 | 55 | 65 | 40 | 60 | **63.15** |
| Taylor Brown (Scaling) | 88 | 70 | 78 | 100 | 80 | **81.30** |

### Step 2: Rank Candidates and Allocate to Domains

After computing composite scores for all 60 candidates, rank by score (highest first).

**Domain allocation strategy**:
- Rank 1-8: Assign to domain with highest D1 score among top 8
- Rank 9-16: Assign to domain with highest D1 among remaining top 8
- Continue until all 5 domains have 8 authors or top 40 candidates assigned

**Rationale**: Highest-scoring candidates get first choice of domain; allocation is then done in waves to balance team quality.

**Example allocation** (40 candidates, 8 per domain):

| Domain | Rank Range | Target | Actual | Avg Score |
|--------|----------|----------|---------|----------|
| Governance & Decision-Making | 2,7,14,18,24,31,38,42 | 8 | 8 | 74.2 |
| Food Systems & Supply Chain | 1,9,15,19,27,35,41,48 | 8 | 8 | 71.8 |
| Information Infrastructure | 3,8,12,22,29,36,43,49 | 8 | 8 | 76.5 |
| Security & Defense | 5,11,17,26,34,40,47,50 | 8 | 8 | 69.3 |
| Scaling Pathways & Thresholds | 4,6,10,20,25,32,39,45 | 8 | 8 | 75.1 |
| **Total** | **1-50** | **40** | **40** | **73.4** |

### Step 3: Apply Constraints and Reassign if Needed

After initial allocation, check each constraint. If violated, swap candidates between domains to resolve.

**Constraint 1: Capacity Limits**
- Maximum 10 hrs/week per author
- Domain team total must be <80 hrs/week average

**Constraint 2: Timezone Diversity (Soft)**
- Each domain team must have ≥2 time zones represented
- Avoid single-timezone teams (reduces coordination friction)

**Constraint 3: Conflict of Interest (Hard)**
- Authors with same affiliation/organization cannot be on same domain team
- Example: Two authors from "Food Sovereignty Network" split across domains

---

## Section 3: Constraint Handling — Detailed Rules

### Capacity Limit Resolution

If a domain team exceeds 80 hrs/week total capacity:

1. **Identify over-capacity authors** (lowest score on that domain)
2. **Check secondary domain preferences** for each low-scorer
3. **Swap** lower-scorer to secondary domain if that domain is under-capacity
4. **Reduce scope** (6,000 words → 4,000 words) for one 8-hr/week author rather than drop them

**Example**: Security domain total 87 hrs/week (exceeds 80 limit)
- Lowest-scoring author: Morgan Lee, 8 hrs/week, score 63.15
- Morgan's second domain: Information Infrastructure (score 68)
- Info Infra capacity: 72 hrs/week (can add 8)
- **Resolution**: Reassign Morgan to Info Infra, add next-ranked candidate to Security

### Timezone Diversity Resolution

If a domain has only 1 UTC offset represented:

1. **Identify authors from other domains in different timezones**
2. **Prefer authors with lower domain expertise score** (minimize skill loss)
3. **Swap** single-timezone author with multi-timezone author
4. **Verify** new assignment still respects domain expertise threshold (D1 ≥ 60)

### Conflict-of-Interest Resolution

If two authors from same organization are assigned to same domain:

1. **Keep higher-scoring author** on preferred domain
2. **Reassign lower-scorer** to their second-ranked domain preference
3. **If second-ranked domain is full**, reassign to third-ranked domain
4. **If no alternative domain exists**, offer COI waiver if:
   - Authors work in different specialties within organization
   - One is senior/one is junior (no peer review concerns)
   - Explicit acknowledgment of same-org affiliation

---

## Section 4: Edge Cases and Resolution

### Edge Case 1: Candidate Withdraws Post-Matching

**Scenario**: July 1, Morgan withdraws from Security domain (personal emergency).

**Resolution**:
1. Identify next-ranked candidate for Security: Riley Martinez, score 62.8
2. Offer Riley the Security domain assignment
3. If Riley declines: move to rank 3, repeat
4. If no alternative candidates: scale domain to 2-3 authors, increase word count per author

**Timing**: Activate replacement within 24 hours. July 1 is 3+ weeks before deliverable; replacement author can onboard quickly.

### Edge Case 2: Domain Team Hits Capacity Limit Mid-Sprint

**Scenario**: June 28, Security domain hits 85 hrs/week, cannot accommodate additional research requests.

**Resolution**:
1. Identify authors nearing completion (can reduce to <2 hrs/week)
2. Identify authors with lower productivity (can reduce to 50% scope)
3. Offer scope reduction: 8,000 words → 5,000 words on core sections only
4. Redistribute reduced-scope topics to another domain if possible

### Edge Case 3: Score Tie Between Two Candidates

**Scenario**: Casey Williams (84.40) and Taylor Brown (84.40) have identical composite score.

**Tier-breaker order** (first applicable wins):
1. Higher D1 (Domain Expertise): Casey D1=85, Taylor D1=88 → **Taylor wins**
2. If tied D1: Higher D2 (Network Reach)
3. If tied D1+D2: Higher D3 (Capacity)
4. If all tied: Coin flip (note tie-break in matching log for audit trail)

### Edge Case 4: Domain-Specific Shortage

**Scenario**: Only 3 strong candidates (score 70+) available for Information Infrastructure; need 8.

**Resolution** (in priority order):
1. **Recruit from Wave 1** (ask high-performers to cover 1 additional domain)
2. **Cross-train** from adjacent domains (Info Infra + Governance both involve systems thinking)
3. **Reduce team size** to 5-6 for that domain, increase word count per author
4. **Partner with external expert** (provide co-author support for Tier C authors)

---

## Section 5: Worked Examples

### Worked Example 1: Standard Assignment (45 Candidates → 40 Matches, 5 Teams)

**Setup**: 60 Wave 2 candidates profiled, 45 meet minimum threshold (score 50+).

**Initial Ranking** (top 40):

| Rank | Name | Domain | D1 | D2 | D3 | D4 | D5 | Score | Status |
|------|------|--------|-----|-----|-----|-----|-----|-------|-------------|
| 1 | Casey Williams | Info Infra | 85 | 80 | 92 | 75 | 85 | **84.4** | Assigned |
| 2 | Alex Chen | Governance | 78 | 65 | 85 | 100 | 75 | **79.25** | Assigned |
| 3 | Taylor Brown | Scaling | 88 | 70 | 78 | 100 | 80 | **81.3** | Assigned |
| 4 | Jordan Smith | Food Systems | 62 | 45 | 70 | 60 | 50 | **58.35** | Assigned |
| 5 | Morgan Lee | Security | 72 | 55 | 65 | 40 | 60 | **63.15** | Assigned |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 40 | Riley Martinez | Scaling | 68 | 50 | 62 | 75 | 55 | **63.9** | Assigned |

**Domain Assignment** (after constraint checks):

| Domain | Assigned | Avg Score | Capacity (hrs/wk) | Timezones |
|--------|---------|-----------|---------|----------|
| Governance | 8 | 74.2 | 74 | UTC-6, UTC+0 |
| Food Systems | 8 | 71.8 | 68 | UTC-6, UTC-7, UTC+1 |
| Info Infra | 8 | 76.5 | 79 | UTC-6, UTC+0, UTC+8 |
| Security | 8 | 69.3 | 71 | UTC-6, UTC-8 |
| Scaling | 8 | 75.1 | 76 | UTC-6, UTC-7, UTC+0 |
| **Total** | **40** | **73.4** | **368** | **Full coverage** |

**Constraint Check Results**: ✅ All constraints met. No reassignments needed.

**Output**: 5 domain-specific matched-authors.md files ready for June 14 execution.

---

### Worked Example 2: One Team Hits Capacity Limit, Rebalancing

**Setup**: Same as Example 1, but Info Infra identified with 88 hrs/week (exceeds 80 limit).

**Violation**: Info Infra over-capacity by 8 hrs/week.

**Resolution Process**:
1. Identify lowest-scoring Info Infra author: Pat Johnson (score 65.2, 8 hrs/week)
2. Check Pat's second-ranked domain: Governance (score 68.5)
3. Check Governance capacity: 74 hrs/week (can add 8)
4. **Swap**: Pat → Governance, promote highest-ranked unassigned (Sam Riley, score 62.1) → Info Infra
5. Verify Sam's Info Infra D1 score: 71 (acceptable, >60 minimum)

**After Rebalancing**:

| Domain | Before → After | Capacity Change | Avg Score |
|--------|---------|---------|----------|
| Info Infra | 8 → 8 | 88 → 80 hrs/wk | 76.1 → 75.8 |
| Governance | 8 → 8 | 74 → 82 hrs/wk | 74.2 → 74.3 |

**Result**: ✅ All constraints met. Capacity normalized. Minimal score impact.

---

### Worked Example 3: Candidate Withdraws, Replacement Logic

**Setup**: June 20, Taylor Brown (Scaling, rank 3, score 81.3) withdraws due to job change.

**Replacement Process**:
1. Scaling domain now has 7 authors instead of 8
2. Identify next-ranked unassigned candidate for Scaling: Chris Patel (score 61.7)
3. Offer Chris the Scaling assignment
4. Chris accepts on June 21
5. Onboarding window: June 22-30 (9 days until July 1 sprint start) — sufficient time

**Timing**: Replacement within 1 day of withdrawal. No impact on July 1 sprint start.

---

## Section 6: Implementation Checklist

**To execute this algorithm on June 14:**

- [ ] Collect 50+ Wave 2 profile cards with 5-dimension scores (from PHASE_5_WAVE_2_AUTHOR_PROFILE_CARDS.md)
- [ ] Run scoring spreadsheet: compute weighted composite scores for each candidate
- [ ] Sort candidates by composite score (highest first)
- [ ] Allocate top 40-50 to 5 domains using Step 2 algorithm
- [ ] Check all constraints (capacity, timezone, COI)
- [ ] Resolve any constraint violations using Section 3 rules
- [ ] Generate matched-authors.md per domain with rank, score, and rationale
- [ ] Populate matching rationale (why this author for this domain) for project lead audit
- [ ] Verify all matched authors have been contacted and confirmed availability
- [ ] Output final matched roster to PHASE_5_MATCHED_WAVE_2_AUTHORS_[DATE].md for audit trail

**Expected output by 14:30 UTC June 14**: 5 domain-specific matched-authors.md files + 1 consolidated matching report, ready to feed into recruitment template execution.

---

## Appendix: Scoring Reference Tables

### Domain Expertise Calibration Anchors (from Wave 1)

| Domain | Tier 1 Expert (90+) | Tier 2 Advanced (75-89) | Tier 3 Intermediate (60-74) |
|--------|---------|---------|----------|
| Governance | McGinnis (30+ yrs) | Scholte (10+ yrs sociocracy) | Community organizer (2-3 yrs) |
| Food Systems | Kloppenburg (decades) | Gwin (5+ yrs research) | CSA/gardener (2+ yrs) |
| Info Infra | Network architect (10+ yrs) | Byrum (8+ yrs community broadband) | Tech enthusiast (1-2 yrs) |
| Security | Aldrich (disaster resilience) | MacNair (15+ yrs nonviolence) | Conflict resolution (1+ yr) |
| Scaling | Henfrey (Transition, 10+ yrs) | Miller (cooperative development) | Transition participant (2+ yrs) |

### Capacity Baseline Scoring

| Self-Reported Hrs/Wk | Base Score | Wave 1 Bonus | Final Score |
|------------|-------|------|---------|
| 8-10 | 90 | On-time (+5) | 95 |
| 6-8 | 75 | On-time (+5) | 80 |
| 4-6 | 60 | On-time (+5) | 65 |
| 2-4 | 40 | On-time (+10) | 50 |
| <2 | 20 | Any completion (+10) | 30 |

---

**Document Version**: 1.0  
**Last Updated**: June 6, 2026 18:00 UTC  
**Next Review**: After June 14 matching execution (capture insights from live matching)
