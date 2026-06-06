---
title: "Wave 2 Author Matching Algorithm"
project: systems-resilience
phase: 5/6
wave: 2
status: PRODUCTION-READY
purpose: "Systematic matching of Phase 6 Wave 2 authors to domains 60–65 using 5-dimension capability scoring"
created: 2026-06-06
execution_deadline: 2026-06-14
business_value: "Pre-computed matching scores reduce June 14–15 matching session from 3–4 hours to 90 minutes"
---

# Wave 2 Author Matching Algorithm
## Phase 5/6 Domain Assignment Logic

> **Purpose**: This document systematizes the author-to-domain matching decision on June 14–15 by pre-computing capability scores and identifying optimal pairings before the matching session.

---

## Overview: Five-Dimension Scoring

The matching algorithm scores each author on five dimensions derived from AUTHOR_DOMAIN_MAPPING_RUBRIC.md:

| Dimension | Scale | What It Measures |
|-----------|-------|------------------|
| D1: Domain Knowledge | 1–5 | Direct working experience + expertise in the domain |
| D2: Long-Form Practitioner Writing | 1–5 | Ability to write accessible research-grounded content for non-specialists |
| D3: Markdown & Digital Collaboration | 1–5 | Technical readiness (Markdown, GitHub, async collaboration) |
| D4: Research & Citation | 1–5 | Ability to synthesize sources and verify evidence quality |
| D5: Domain-Specific Practitioner Grounding | 1–5 | Lived/field experience distinguishing real expertise from reading |

**Maximum score per author**: 25 points (5 × 5)

**Domain-specific minimum thresholds**:
- **Domain 60 (International Coordination)**: Requires D1 ≥ 3, D5 ≥ 3 (18-point minimum)
- **Domain 61 (Intergenerational Knowledge)**: Requires D1 ≥ 3, D5 ≥ 3 (18-point minimum)
- **Domain 62 (Infrastructure Interdependencies)**: Requires D1 ≥ 3, D5 ≥ 3 (18-point minimum)
- **Domain 63 (Ecosystem Restoration)**: Requires D1 ≥ 4, D5 ≥ 4 (20-point minimum, highest threshold)
- **Domain 64 (Community Economic Resilience)**: Requires D1 ≥ 3, D5 ≥ 3 (18-point minimum)
- **Domain 65 (Institutional Learning & Governance)**: Requires D1 ≥ 3, D5 ≥ 3 (18-point minimum)

---

## Scoring Instructions

### Step 1: Collect Author Data
For each Wave 2 author candidate, obtain:
- Completed AUTHOR_READINESS_INTAKE_FORM.md (primary source for D1–D4 scoring)
- Domain interest ranking (Domains 60–65, preference order 1–6)
- Availability confirmation (8 hrs/week, July 16 – September 15 minimum)
- Email + backup contact

### Step 2: Score Each Author on Five Dimensions

#### D1: Domain Knowledge (1–5)
**Source**: AUTHOR_READINESS_INTAKE_FORM.md Section 2 (Background & Experience)

| Score | Criteria |
|-------|----------|
| 1 | Academic familiarity only; no hands-on experience |
| 2 | Some hands-on experience; basic concept proficiency |
| 3 | Direct working experience; can solve real problems in this domain |
| 4 | Multiple years applied practice; has trained/mentored others |
| 5 | Recognized expertise; published, taught, or led in this domain |

**Examples**:
- Author with permaculture design experience + soil testing: **D1 = 4** (Domain 63)
- Author with economics degree but no cooperative experience: **D1 = 1** (Domain 64)
- Author with 10 years cooperative board service: **D1 = 5** (Domain 65)

#### D2: Long-Form Practitioner Writing (1–5)
**Source**: AUTHOR_READINESS_INTAKE_FORM.md Section 3 (Writing Experience) + portfolio review

| Score | Criteria |
|-------|----------|
| 1 | No long-form writing; primarily short-form or academic only |
| 2 | Has written 4,000+ words, but for academic/internal audiences only |
| 3 | Has written practitioner guides, training materials, or blog posts (5,000–15,000 words) |
| 4 | Regular practitioner writing; multiple guides; comfortable with editing |
| 5 | Extensive history; published in practitioner/extension publications; used as training |

**Examples**:
- Author with 15-year Extension Service publication record: **D2 = 5**
- Author with blog posts on herbalism (8,000 words): **D2 = 4**
- Author with academic papers only (10,000 words): **D2 = 2**

#### D3: Markdown & Digital Collaboration (1–5)
**Source**: AUTHOR_READINESS_INTAKE_FORM.md Section 4 (Technical Skills)

| Score | Criteria |
|-------|----------|
| 1 | No Markdown or GitHub experience |
| 2 | Some exposure; can handle basic formatting with reference |
| 3 | Comfortable with headings, lists, links; semi-regular use |
| 4 | Proficient; writes Markdown without reference; comfortable with YAML |
| 5 | Expert; daily Markdown use; familiar with Obsidian, Git, or similar |

**Examples**:
- Author with no coding experience but willing to learn: **D3 = 2**
- Author with technical writing background (rst/Markdown): **D3 = 4**
- Author with daily use of Obsidian for note-taking: **D3 = 5**

#### D4: Research & Citation (1–5)
**Source**: AUTHOR_READINESS_INTAKE_FORM.md Section 5 (Research Capability) + writing samples

| Score | Criteria |
|-------|----------|
| 1 | Limited synthesis experience; new to citation verification |
| 2 | Can synthesize sources with time; citation checking is developing skill |
| 3 | Comfortable with synthesis; can write cited section with 10–15 sources |
| 4 | Strong synthesis; comfortable with contested evidence; prioritizes source quality |
| 5 | Expert; has produced bibliographies, literature reviews, or evidence hierarchies |

**Examples**:
- Author with Master's thesis (40+ sources, full bibliography): **D4 = 5**
- Author with policy brief writing (20–30 sources, cited sections): **D4 = 4**
- Author new to research writing but willing: **D4 = 2**

#### D5: Domain-Specific Practitioner Grounding (1–5)
**Source**: AUTHOR_READINESS_INTAKE_FORM.md Section 1 (Domain Relevance + Personal Connection)

| Score | Criteria |
|-------|----------|
| 1 | Only read about the domain; no lived/field experience |
| 2 | Limited hands-on experience (< 1 year) or secondary interest |
| 3 | 2–5 years hands-on experience or active community participation |
| 4 | 5+ years experience or recognized community leader in domain |
| 5 | Deep expertise through decades of practice or leadership; identity tied to domain |

**Critical distinction**: D5 ≠ D1. D1 is what you *know*; D5 is whether you've *lived it*.

**Examples**:
- Author who grew up on a farm + 15 years agroforestry work: **D5 = 5** (Domain 63)
- Author who read cooperatives literature but never joined one: **D5 = 1** (Domain 64)
- Author with 3 years participation in local currency system: **D5 = 3** (Domain 64)

---

## Step 3: Calculate Domain-Specific Fitness Scores

For each author-domain pairing, compute:

```
Raw Fitness Score = D1 + D2 + D3 + D4 + D5
```

Then **check domain-specific minimum thresholds**:
- If D1 < domain minimum OR D5 < domain minimum → **Mark as INELIGIBLE**
- Otherwise → **Mark as ELIGIBLE**

**Example calculation**:
- Author A for Domain 63: D1=4, D2=3, D3=3, D4=3, D5=4
  - Minimum thresholds: D1≥4 ✓, D5≥4 ✓ → ELIGIBLE
  - Raw Score = 17 (meets 20-point minimum? NO) → **INELIGIBLE**

- Author B for Domain 64: D1=3, D2=4, D3=3, D4=4, D5=3
  - Minimum thresholds: D1≥3 ✓, D5≥3 ✓ → ELIGIBLE
  - Raw Score = 17 (meets 18-point minimum? NO) → **BORDERLINE** (accept if no alternatives)

---

## Step 4: Generate Optimal Matching

**Goal**: Assign each of 6 domains (60–65) to 1–2 authors such that:
1. All authors meet domain-specific minimum thresholds
2. Each domain's highest-fitness author is assigned first
3. Author preference rankings (from intake form) are secondary consideration
4. No author is overallocated (max 1 domain per author unless split-domain approved)

**Algorithm**:

1. **Sort all author-domain pairs by Fitness Score (descending)**
   ```
   Domain 63, Author C: 21 points
   Domain 64, Author A: 20 points
   Domain 61, Author B: 19 points
   Domain 65, Author D: 19 points
   ...
   ```

2. **Greedy assignment**: Process top scores first
   - Assign top pair (Domain, Author) if author is not yet allocated
   - If author is already allocated, check if split-domain is approved; if not, skip to next pair
   - Continue until all 6 domains have primary assignments

3. **Fallback assignment**: If any domain has no eligible author
   - Use PHASE_6_AUTHOR_RECRUITMENT_TARGET_LIST.md Tier B fallback candidates
   - Schedule accelerated intake for fallback candidate (June 12–13)
   - Apply same 5-dimension scoring algorithm

4. **Document all assignments** in WAVE_2_AUTHOR_PROFILE_CARDS.md

---

## Step 5: Conflict Resolution

**If multiple authors compete for the same domain**:

1. **Fitness score as tiebreaker**: Assign domain to author with highest raw score
2. **If tied on fitness score**: Author preference ranking (intake form) is secondary tiebreaker
3. **If still tied**: Allocate to author with highest D5 (practitioner grounding) — this ensures domain expertise is prioritized

**If an author is torn between two eligible domains**:

- Ask author: "If we could only assign you one, which domain would you choose?" (phone call, 2 minutes)
- Assign to author's stated preference
- Fallback to second-choice domain if author accepts split-domain approval

---

## Edge Cases & Special Handling

### Edge Case 1: No Eligible Author for a Domain
**Scenario**: Domain 63 (Ecosystem Restoration) requires D1≥4, D5≥4. No author meets both thresholds.

**Resolution**:
1. Check PHASE_6_AUTHOR_RECRUITMENT_TARGET_LIST.md Tier B candidates
2. If Tier B has candidate with D1≥3, D5≥4, offer conditional assignment with **supervision**: primary writer (from Wave 1) provides 2-hour weekly mentoring for 4 weeks
3. If no Tier B candidate exists, escalate to project lead: Domain 63 may need to be deferred to Wave 3 or combined with Domain 62 (Infrastructure)

### Edge Case 2: Author Scores Below All Domain Minimums
**Scenario**: Author C scores D1=2, D2=3, D3=4, D4=3, D5=2 (total 14 points). No domain accepts this.

**Resolution**:
- Author is not suitable for solo assignment in Phase 6 Wave 2
- Offer alternative: Tier 3 synthesizer role (combining Wave 1 & Wave 2 outputs) if author is strong writer
- Otherwise: Respectfully decline and thank for interest; add to Wave 3 candidate pool

### Edge Case 3: Author Prefers Multiple Domains (All ≥18 Points)
**Scenario**: Author D scores 20+ on both Domain 63 and Domain 65, both in top preference ranking.

**Resolution**:
1. Contact author: "You're qualified for both. Domain 64 and 65 both need strong authors. If we assigned you to Domain 65 (your #2 choice), could we find a secondary author for Domain 63?"
2. If author agrees → Assign Author D to Domain 65, use Tier B for Domain 63
3. If author prefers Domain 63 → Assign Author D to Domain 63, use Tier B for Domain 65

---

## Tier Assignments

**Tier A** (Fitness Score 20–25, all minimums met):
- Primary author assignment
- Full documentation package
- Weekly 30-minute check-in calls
- Access to Phase 5 drafts for reference

**Tier B** (Fitness Score 18–19, all minimums met):
- Primary author assignment with lighter oversight
- 2-week check-in calls instead of weekly
- Potential for mentoring from Wave 1 primary author (2 hrs/week)

**Tier C** (Fitness Score <18 OR minimum thresholds not met):
- Not eligible for primary assignment
- Possible secondary role: Tier 3 synthesis, reference library curation, community editing
- Alternative: Add to Wave 3 candidate pool

---

## Worked Example: Matching Session Preparation

**Scenario**: 12 Wave 2 authors confirm availability by June 12. Domains 60–65 need assignment.

| Author | Domain Pref #1 | D1 | D2 | D3 | D4 | D5 | Total | Domain 60 | Domain 61 | Domain 62 | Domain 63 | Domain 64 | Domain 65 |
|--------|---|----|----|----|----|-------|--------|----------|----------|----------|----------|----------|----------|
| A (International NGO) | 60 | 4 | 4 | 3 | 3 | 5 | 19 | ✓ 19 | 16 | 14 | 12 | 13 | 15 |
| B (Pedagogy) | 61 | 3 | 5 | 4 | 4 | 4 | 20 | 15 | ✓ 20 | 14 | 13 | 14 | 15 |
| C (Farmer/Agroecologist) | 63 | 5 | 3 | 2 | 3 | 5 | 18 | 14 | 15 | 17 | ✓ 18 | 15 | 14 |
| D (Economist/Cooperative) | 64 | 4 | 4 | 3 | 4 | 4 | 19 | 16 | 16 | 15 | 14 | ✓ 19 | 17 |
| E (Systems Engineer) | 62 | 4 | 4 | 5 | 3 | 2 | 18 | 15 | 14 | ✓ 18 | 16 | 15 | 16 |
| F (Cooperative Leader) | 65 | 3 | 4 | 3 | 3 | 5 | 18 | 16 | 16 | 16 | 14 | 18 | ✓ 18 |

**Sorted by highest fitness per domain**:
1. **Domain 63**: Author C (18 points) ✓ meets D1≥4, D5≥4 minimum → ASSIGN C to Domain 63
2. **Domain 61**: Author B (20 points) ✓ meets minimum → ASSIGN B to Domain 61
3. **Domain 64**: Author D (19 points) ✓ meets minimum → ASSIGN D to Domain 64
4. **Domain 65**: Author F (18 points) ✓ meets minimum → ASSIGN F to Domain 65
5. **Domain 62**: Author E (18 points) ✓ meets minimum → ASSIGN E to Domain 62
6. **Domain 60**: Author A (19 points) ✓ meets minimum → ASSIGN A to Domain 60

**Final assignments**:
- Domain 60 (International Coordination) → Author A (Tier A, 19 pts)
- Domain 61 (Intergenerational Knowledge) → Author B (Tier A, 20 pts)
- Domain 62 (Infrastructure) → Author E (Tier B, 18 pts) — pair with Wave 1 mentor
- Domain 63 (Ecosystem Restoration) → Author C (Tier B, 18 pts) — meets minimum barely
- Domain 64 (Economic Resilience) → Author D (Tier A, 19 pts)
- Domain 65 (Governance Scaling) → Author F (Tier B, 18 pts)

---

## Implementation

**June 6**: Pre-compute all author scores using AUTHOR_READINESS_INTAKE_FORM responses (completed by June 5)
**June 10–12**: Final outreach confirming availability; collect any missing intake data
**June 13**: Final score verification; generate matching algorithm output (this document + scores matrix)
**June 14 08:00**: Open matching session with pre-computed matches as starting point (90 minutes vs. 3–4 hours)

---

## Related Documents

- `AUTHOR_DOMAIN_MAPPING_RUBRIC.md` — Detailed expertise requirements per domain
- `AUTHOR_READINESS_INTAKE_FORM.md` — Data source for D1–D4 scoring
- `PHASE_6_AUTHOR_RECRUITMENT_TARGET_LIST.md` — Tier A/B candidate contact list
- `JUNE_14_15_AUTHOR_MATCHING_SESSION_RUNBOOK.md` — Execution procedures for matching session
