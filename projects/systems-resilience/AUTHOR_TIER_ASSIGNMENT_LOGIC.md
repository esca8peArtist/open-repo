---
title: "Wave 2 Author Tier Assignment Logic — Decision Tree and Conflict Resolution Rules"
project: systems-resilience
phase: 6
wave: 2
item: 88
status: PRODUCTION-READY — use June 12-14 matching session
created: 2026-06-05
purpose: "Decision tree and conflict resolution rules for author tier assignment. Companion to AUTHOR_MATCHING_AUTOMATION_SCRIPT.py. All logic here is implemented in the script; this document exists for human auditors and facilitators at the June 14 matching session."
cross_references:
  - AUTHOR_DOMAIN_MAPPING_RUBRIC.md
  - AUTHOR_READINESS_INTAKE_FORM.md
  - AUTHOR_MATCHING_AUTOMATION_SCRIPT.py
  - WAVE_2_PRIORITIZED_ONBOARDING_SEQUENCE.md
word_count: ~1200
---

# Wave 2 Author Tier Assignment Logic
## Decision Tree, Override Rules, and Conflict Resolution for June 14 Matching Session

---

## Overview

Tier assignment is the first gate that shapes every subsequent onboarding decision: what scaffolding the author receives, how often the project lead checks in, whether a solo or split-domain assignment is appropriate, and what word count target is set. Getting the tier wrong in either direction — assigning too high and leaving an author unsupported, or too low and over-managing an experienced practitioner — creates problems that compound over the 30-day sprint.

This document describes the decision tree the automation script implements. If you are running the matching session manually without the script, use this document as your step-by-step guide. If you are using the script's output to guide the session, use this document to understand and audit each recommendation.

---

## Phase 6 Scoring Basis

Phase 6 uses a five-dimension rubric (maximum 25 points). This is distinct from the Phase 5 Wave 2 intake form, which used four dimensions and a 20-point maximum. The fifth dimension, Domain-Specific Practitioner Grounding (D5), was added because Phase 6 domains require lived field experience — not just academic familiarity — for credible authorship at community-practitioner scale.

The five dimensions and their scales:

| Dimension | What it measures | Scale | Max |
|-----------|-----------------|-------|-----|
| D1 — Domain Knowledge | Depth of knowledge in the assigned domain | 1–5 | 5 |
| D2 — Long-Form Practitioner Writing | Ability to write for non-specialist audiences at length | 1–5 | 5 |
| D3 — Markdown and Digital Collaboration | Platform fluency | 1–5 | 5 |
| D4 — Research and Citation | Source synthesis and verification competency | 1–5 | 5 |
| D5 — Domain Practitioner Grounding | Lived or field experience in the specific domain | 1–5 | 5 |

The total score (max 25) determines the provisional tier:

| Score | Tier | Implications |
|-------|------|-------------|
| 20–25 | Tier A | Minimal scaffolding. Eligible for split-domain assignment. |
| 14–19 | Tier B | Standard onboarding. T+3 check-in added. Solo domain only. |
| 6–13 | Tier C | Scope reduction to 2,500-3,500 words. Weekly check-ins. Solo only. |
| Below 6 | HOLD | Do not assign. Resolve gaps first. |

---

## Decision Tree

### Step 1: Compute the total score

Sum all five dimensions. If the author's intake form does not include D5 (because they completed the Phase 5 form rather than the Phase 6 form), set D5 to the default value based on the narrative evidence in the form. A D5 score of 3 requires demonstrated field implementation — not just reading or academic study.

### Step 2: Assign provisional tier from the score matrix

Use the table above. This is the starting point only. Steps 3–5 may override it.

### Step 3: Apply override rules

Override rules take precedence over the matrix score. Check each rule in order. The most restrictive override that applies wins.

**Override Rule 1: D2 = 1 → HOLD regardless of total score**

Writing production is the core deliverable. An author with no long-form writing experience cannot produce a 8,000-word practitioner document regardless of how strong their domain expertise is. Do not assign. Flag for resolution: the author needs to demonstrate at least a 4,000-word practitioner-oriented writing sample before they can be reconsidered.

**Override Rule 2: D1 = 1 for the target domain → HOLD for that domain**

A writer with no domain knowledge in the assigned domain cannot produce accurate content. This rule applies per domain — an author who scores D1=1 for Domain 60 but D1=4 for Domain 63 is still eligible for Domain 63. The rule blocks assignment to the specific domain where D1=1, not all domains.

**Override Rule 3: D5 = 1 and D1 = 2 for the target domain → cap at Tier C**

When both the practitioner grounding and the domain knowledge are very low, the author can only handle a scoped, project-lead-supported assignment. The project lead must provide a source sprint before the author begins production. Scope is restricted to 2,500–3,500 words with section-by-section guidance.

**Override Rule 4: D4 < 3 → cap at Tier B**

If research and citation skills are below the competent threshold, the author cannot self-manage source quality for an 8,000-word document with 15+ citations. Cap at Tier B. Project lead performs a citation audit at the T+7 checkpoint to verify citation quality before the author continues.

### Step 4: Check domain eligibility

Even if the author's overall tier is A or B, they may not be eligible for all domains. The eligibility screen for each domain requires both D1 ≥ 3 and D5 ≥ 3 for full Tier A/B eligibility in that domain.

- Both D1 ≥ 3 and D5 ≥ 3: fully eligible (Tier A or B as determined by overall score)
- Only one of D1 or D5 ≥ 3: eligible for Tier C assignment only in this domain
- Neither D1 nor D5 ≥ 3: ineligible for this domain — do not assign

### Step 5: Apply domain difficulty adjustment and rank eligible domains

For each domain the author is eligible for, compute the adjusted assignment score:

```
Assignment Score = (D1 × 2) + (D5 × 2) + D2 + D4
Adjusted Score = Assignment Score + Domain Difficulty Modifier
```

Domain difficulty modifiers:
- Domain 60 (International Coordination): -2 (lowest source readiness)
- Domain 61 (Intergenerational Knowledge): -1 (crisis-context literature gap)
- Domain 62 (Infrastructure Interdependencies): -2 (community-scale gap)
- Domain 63 (Ecosystem Restoration): 0 (richest source base)
- Domain 64 (Economic Resilience): 0 (strong source base)
- Domain 65 (Institutional Learning): -1 (failure documentation challenge)

The domain with the highest adjusted score is the primary domain recommendation. This double-weighting of D1 and D5 reflects the rubric's principle that domain knowledge and practitioner grounding are the hardest to supplement at runtime — writing and research skills can be supported by the project lead, but domain expertise cannot be injected mid-sprint.

---

## Conflict Resolution Rules

These rules govern what happens when two or more authors are optimal candidates for the same domain.

### Rule 1: Higher tier wins

If a Tier A and a Tier B author are both eligible for the same domain, the Tier A author takes that domain. The Tier B author is reassigned to their second-ranked eligible domain.

### Rule 2: Within the same tier, higher D5 wins

D5 (Domain-Specific Practitioner Grounding) is the tiebreaker. The author with deeper lived experience in the domain is the better fit, because practitioner grounding is what differentiates a document that rings true to Zone 5 practitioners from one that is technically accurate but feels written from outside.

### Rule 3: The displaced author goes to their second-ranked eligible domain

Do not leave an author without an assignment simply because they lost a conflict. Run the ranking algorithm for their second-best eligible domain and assign them there. If their second-best domain is already claimed, continue down the ranked list.

### Rule 4: If no Tier A or Tier B author is eligible for a domain

Assign the highest-scoring eligible Tier C author with explicit project lead co-research support. Flag the domain for an additional source sprint before the author begins production. Domains 60 and 62, with source readiness below 65%, are the most likely to require this fallback.

### Rule 5: If no eligible author exists for a domain

Flag the domain as unassigned. Activate secondary recruitment or project lead self-execute fallback for that domain. Do not delay the rest of the wave to fill the gap.

---

## Split-Domain Eligibility Logic

Split-domain assignment (one author covers two domains simultaneously) is appropriate only when all three of the following conditions are met:

1. **Tier A only**: The author's total score is 20+/25. Split-domain is never appropriate for Tier B or Tier C authors.

2. **Approved adjacent pairing**: The two domains share substantial literature overlap. The three approved pairings for Phase 6 are:
   - Domain 63 + Domain 64 (Ecosystem Restoration and Economic Resilience — Ostrom commons framework bridges both)
   - Domain 61 + Domain 62 (Intergenerational Knowledge and Infrastructure Interdependencies — systems complexity and tacit knowledge)
   - Domain 64 + Domain 65 (Economic Resilience and Governance Scaling — cooperative enterprise and governance theory)
   Non-adjacent pairings require project lead approval and an explicit scope reduction plan.

3. **Bandwidth confirmation**: The author has confirmed at least 8 hours per week for the duration of the sprint. Standard solo commitment is 4–6 hours per week. Split-domain doubles the research and writing load.

Additional red flags that should trigger project lead review before split-domain is confirmed:
- The author proposed split-domain during intake (rather than the project lead identifying it)
- Either of the two proposed domains has a source readiness modifier of -2 (Domains 60 or 62)
- The author's confirmed availability drops below 6 hours per week for any week in the sprint

---

## Operational Conflict Flags

These flags do not change the tier assignment but affect onboarding sequencing and communication planning.

| Flag | Severity | Trigger | Resolution |
|------|----------|---------|------------|
| Hours below minimum | Blocker | < 4 hrs/week confirmed | Do not assign. Resolve before June 12. |
| D2 = 1 | Blocker | Long-form writing score = 1 | Do not assign. See Override Rule 1. |
| D1 = 1 for domain | Blocker | Domain Knowledge = 1 | Do not assign to that domain. |
| Conflict in T+7 window | Warning | Author unavailable June 14-19 | Adjust T+7 checkpoint date by 1-2 days. |
| Conflict in peer review window | Warning | Author unavailable June 24-27 | Adjust peer review window. Notify peer reviewer. |
| Batch weekly communicator | Warning | Response time = weekly | Author must agree to daily check during sprint. Confirm before onboarding. |
| Limited Zone 5 familiarity | Note | zone5_familiarity = "limited" | Note in scope document. Add Zone 5 calibration question to T+7. |

Blockers must be resolved before an author can be onboarded. Warnings must be addressed explicitly in the onboarding communication. Notes inform the scope document and checkpoint review questions.

---

## Onboarding Depth by Tier

| Tier | Scaffolding | Check-ins | Word Count Target | Additional steps |
|------|------------|-----------|-------------------|-----------------|
| A | Scope doc + bibliography, no extra notes | Formal checkpoints only (T+7, T+14, T+21) | 8,000–10,000 (solo) or 14,000–18,000 (split) | None |
| B | Scope doc + scope constraint intro note | T+3 + formal checkpoints | 8,000–10,000 | Project lead citation spot-check at T+7 |
| C | Scope consultation June 14 + reduced scope | Weekly + T+3 mandatory | 2,500–3,500 | Editorial pass at T+14; pair with Tier A/B peer reviewer |
| HOLD | None until flag resolved | N/A | N/A | Resolve blocker, reassess |

---

*Logic Version 1.0 — Item 88 — Created June 5, 2026*
*Implements AUTHOR_DOMAIN_MAPPING_RUBRIC.md Section 2-5 as executable decision logic.*
*All rules implemented in AUTHOR_MATCHING_AUTOMATION_SCRIPT.py.*
