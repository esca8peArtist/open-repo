---
title: "Wave 2 Peer Review Pairing Protocol"
project: systems-resilience
phase: 6
wave: 2
status: PRODUCTION-READY — use June 14 author matching session
created: 2026-06-05
purpose: "Assignment algorithm for pairing reviewers with authors, 20-item peer review checklist, 48-hour SLA and escalation mechanism, multiple-review protocol for Tier C authors, and conflict resolution when author and reviewer disagree on publication readiness."
deadline: June 14, 2026 (must exist before author matching session)
cross_references:
  - AUTHOR_DOMAIN_MAPPING_RUBRIC.md
  - WAVE_2_PUBLICATION_READY_CRITERIA.md
  - WAVE_2_QUALITY_GATE_INTEGRATION.md
  - PHASE_5_EDITORIAL_REVIEW.md
  - PHASE_6_DOMAIN_60_65_RESEARCH_LANDSCAPE.md
---

# Wave 2 Peer Review Pairing Protocol
## Assignment Algorithm, Review Checklist, Turnaround SLA, and Conflict Resolution

> **Lead finding**: The pairing algorithm prioritizes adjacent-domain reviewers over same-domain reviewers because the primary failure mode in practitioner-facing research is disciplinary insularity, not technical inaccuracy — an author and a same-domain reviewer will both miss scope creep that an adjacent-domain reviewer catches immediately. Tier A authors review Tier B/C work by default; Tier C authors are never assigned review duties until their own document is publication-ready.

---

## Part 1: Assignment Algorithm

### Step 1 — Build the Reviewer Pool

Before June 14 matching session, compile a reviewer pool from three sources:

**Source A — Wave 2 author pool (cross-review)**: Authors reviewing each other's work. This is the primary reviewer pool. Every author who is Tier A or Tier B is eligible to review one domain that is not their own.

**Source B — Phase 5 Wave 1+2 authors**: Authors who produced the five published Phase 5 documents. They know the project's quality standards from experience. Eligible for review if they have confirmed 2–3 hours available during the review windows (June 30–July 2 and August 20–25).

**Source C — External domain experts**: Expert contacts from the PHASE_6_DOMAIN_60_65_RESEARCH_LANDSCAPE.md starter lists (e.g., Practical Farmers of Iowa for Domain 63, Ostrom Workshop contacts for Domain 65). External reviewers must be briefed on the practitioner-audience standard and the 48-hour SLA before being assigned. External reviewers are preferred for domains where no Wave 2 author has adjacent expertise.

### Step 2 — Apply the Domain Adjacency Matrix

**Primary rule**: Reviewer must not be assigned to review their own domain. A Domain 63 author does not peer-review a Domain 63 document.

**Second rule**: Assign adjacent-domain reviewers preferentially over distant-domain reviewers. Adjacent pairings produce more actionable feedback because the reviewer shares enough conceptual language to assess content depth without being so close that they share the author's blind spots.

**Approved adjacent pairings** (from AUTHOR_DOMAIN_MAPPING_RUBRIC.md, Section 5):

| Primary Domain | Adjacent Reviewer Domains (in preference order) |
|---------------|------------------------------------------------|
| 60 — International Coordination | 65, 64 (governance and economics share international precedent literature) |
| 61 — Intergenerational Knowledge | 65, 63 (institutional learning and ecosystem both deal with tacit transmission) |
| 62 — Infrastructure Interdependencies | 63, 64 (ecosystem restoration and economics both deal with material systems under constraint) |
| 63 — Ecosystem Restoration | 62, 64 (infrastructure and economics are the natural adjacent domains for land-based practice) |
| 64 — Community Economic Resilience | 65, 60 (governance and international coordination are adjacent to economic systems design) |
| 65 — Institutional Learning | 61, 60 (intergenerational knowledge transmission and international coordination both deal with governance legitimacy) |

**If no adjacent reviewer is available** (e.g., only one author in the adjacent domain and they are already assigned to a different review): assign a distant-domain reviewer and flag to the project lead. A distant-domain review is better than no review; the project lead compensates by doing a closer content spot-check before publication approval.

### Step 3 — Apply the Tier Hierarchy Rule

**Rule**: Tier A reviewers review Tier B and Tier C documents. Tier B reviewers review other Tier B documents or Tier A documents if no Tier A reviewer is available. Tier C authors do not serve as primary peer reviewers during Wave 2. Tier C authors may serve as second reviewers on Tier C documents after completing their own first full draft (see Part 4 on multiple-review protocol).

**Rationale**: Peer review requires the reviewer to be able to identify what is missing, not only to evaluate what is present. A Tier C reviewer — who is themselves navigating the research synthesis task for the first time — may not have the pattern recognition to identify structural gaps or source quality issues. The Tier A/B reviewer pool has this capacity.

**If Tier A reviewers are unavailable**: Assign two Tier B reviewers instead of one. Two independent moderate-experience reviews produce equivalent coverage to one high-experience review, and disagreements between the two Tier B reviewers surface the ambiguous cases where the project lead's judgment is needed.

### Step 4 — Apply Conflict of Interest Screen

Disqualify a reviewer for a specific document if:

- The reviewer co-authored or contributed sources to the document (even informally — if a reviewer suggested three key citations to the author during drafting, they have a conflict).
- The reviewer and author have a professional relationship where negative feedback would create career risk (e.g., reviewer is a supervisor or major funder contact of the author). This is rare in this project but must be screened.
- The reviewer has a stated public position that is directly contrary to one of the document's core claims (e.g., a reviewer who actively argues against local currency systems should not review a Domain 64 document). Note: this is a conflict of interest, not a content check — the point is that ideologically opposed reviewers are not positioned to give neutral structural feedback.

If a conflict is identified, assign to the next eligible reviewer in the adjacency matrix ranking.

### Step 5 — Confirm Reviewer Availability and SLA Acceptance

Before finalizing any pairing, confirm the reviewer has:

- Confirmed availability during the review window (June 30–July 2 for Wave 2 first-draft reviews; August 20–25 for Wave 2 final reviews)
- Accepted the 48-hour turnaround SLA in writing (Matrix message or email is sufficient)
- Received and read Part 2 of this document (the 20-item review checklist)

A reviewer who has not accepted the SLA is not assigned. This prevents the most common peer review failure mode: reviewer assigned but not available, author waits, publication schedule slips.

### Pairing Record Template

Complete this record for each author-reviewer pair before June 20:

```
Author Name: _______________
Author Domain: Domain ___
Author Tier: A / B / C

Primary Reviewer: _______________
Primary Reviewer Domain: Domain ___
Primary Reviewer Tier: A / B
Adjacency: Same / Adjacent / Distant (flag if distant)
Conflict of Interest Screened: YES (no conflicts) / FLAG: _______________
SLA Accepted: YES / NO (do not assign until YES)

Second Reviewer (if Tier C author OR two Tier B reviewers assigned):
Second Reviewer: _______________
Second Reviewer Domain: Domain ___
Conflict of Interest Screened: YES / FLAG: _______________
SLA Accepted: YES / NO

Review Window 1 (first draft): June 30 – July 2
Review Window 2 (final): August 20 – 25
```

---

## Part 2: Peer Review Checklist (20 Items)

The peer reviewer works through this checklist after reading the full document. The checklist is structured in three blocks: structural and scope (Items 1–7), source quality (Items 8–12), and content quality (Items 13–20). The reviewer completes all 20 items and returns the completed checklist to the author within 48 hours of receiving the document.

**Rating scale**: PASS / NEEDS-REVISION / FAIL

PASS: The criterion is satisfied without revision needed.
NEEDS-REVISION: The criterion is substantially met but requires a specific revision (reviewer must identify the specific location and describe the needed change). Author must address all NEEDS-REVISION items before publication.
FAIL: The criterion is not met in a way that requires structural revision (not just editing). A single FAIL blocks publication until resolved with a full review cycle.

**Note on rating discipline**: Reviewers should use FAIL only when the document cannot be corrected by editing — when the problem is architectural (missing section, wrong scope, no implementation pathway present at all). Most issues are NEEDS-REVISION. A document with no FAILs and fewer than 5 NEEDS-REVISION items is effectively publication-ready after author addresses the revisions.

---

### Block 1 — Structural and Scope Review (Items 1–7)

**Item 1 — Scope Compliance**

PASS: The document remains within the domain's defined scope (see WAVE_2_PUBLICATION_READY_CRITERIA.md Part 2 for each domain's scope hard boundary). Every major section addresses Zone 5 community-scale content.

NEEDS-REVISION: One or two passages operate outside scope (e.g., a paragraph about national policy in a community-scale document). Identify the passages and describe the correction.

FAIL: One or more sections are substantially out of scope and cannot be corrected without major structural revision or replacement.

---

**Item 2 — Section Structure Completeness**

PASS: All required sections are present and distinguishable (Foundation, Mechanisms, Landscape, Pathways, Implementation, International Precedent, Summary — or the tier-appropriate subset). Each section is functionally distinct from adjacent sections.

NEEDS-REVISION: A required section is present but has been merged into an adjacent section in a way that loses its distinct function. Identify which sections need separation or development.

FAIL: A required section is absent (heading present with no substantive content counts as absent for Tier A/B documents; for Tier C, a merged section is acceptable if the function is preserved).

---

**Item 3 — Section Word Count Compliance**

PASS: Each required section meets its minimum word count (see WAVE_2_PUBLICATION_READY_CRITERIA.md Part 1, Section 1.3).

NEEDS-REVISION: One section is below minimum word count but the shortfall is less than 30% — the section exists and covers the topic, it is just thin. Identify and describe what content is missing.

FAIL: A section is below 60% of minimum word count, or is essentially a header with a paragraph.

---

**Item 4 — Total Word Count**

PASS: Document total word count falls within the per-domain range for the author's tier.

NEEDS-REVISION: Document is within 10% of the floor (slightly thin — identify which sections need development) or within 10% of the ceiling (slightly long — identify which sections can be condensed).

FAIL: Document is more than 10% below the floor (substantially thin — needs structural development). Document is more than 25% above the ceiling (scope creep — red flag per WAVE_2_PUBLICATION_READY_CRITERIA.md Part 5).

---

**Item 5 — Audience Calibration**

PASS: The document is consistently written for the practitioner/policymaker/community organizer audience specified in the onboarding kit. Technical content is explained at the level a Zone 5 community coordinator could act on. Acronyms are defined on first use. No passages assume doctoral-level background knowledge.

NEEDS-REVISION: One or two passages are written at academic density without adequate translation for practitioners. Identify the specific passages.

FAIL: Large portions of the document are inaccessible to the practitioner audience — written in academic register throughout, or assuming specialist knowledge not shared by community coordinators.

---

**Item 6 — Tonal Consistency with Phase 5 Corpus**

PASS: The document's tone is consistent with the Phase 5 Wave 1+2 published documents — direct, evidence-based, non-advocacy (describing what works, not arguing for ideological positions), and practitioner-respectful (not condescending or simplistic).

NEEDS-REVISION: Specific passages slide into advocacy register, dismissive register, or excessive hedging. Identify and describe.

FAIL: The document's overall tone is inappropriate for the corpus (pure advocacy, academic theoretical argument, or popularization pitched below community organizer level).

---

**Item 7 — Cross-Domain Bridges**

PASS: At least three explicit cross-domain bridges are present, each naming a specific other domain and explaining the connection with enough specificity to be actionable. At least one bridge connects to Phase 5. All three bridges are consolidated or referenced in the Summary section.

NEEDS-REVISION: Fewer than three bridges, or bridges present but too vague. Identify missing bridges and suggest appropriate connections based on the domain adjacency matrix.

FAIL: No cross-domain bridges present. (Rare — most authors include some bridges; this FAIL is for documents that operate in complete isolation.)

---

### Block 2 — Source Quality Review (Items 8–12)

**Item 8 — Citation Count**

PASS: Document has ≥40 citations (Tier A/B) or ≥25 citations (Tier C). Counted manually or via grep on citation pattern.

NEEDS-REVISION: Count is within 5 of the minimum (e.g., 36–39 for a Tier A/B document). Identify which sections are undercited and suggest source types that would fill the gap.

FAIL: Count is more than 5 below the minimum. (For a Tier A/B document at 34 or below, 6+ citations are missing — this is a research gap, not an editing gap.)

---

**Item 9 — Citation Quality Distribution**

PASS: At least 30% peer-reviewed or formally published; at least 50% have accessible URLs; no more than 20% from a single organization.

NEEDS-REVISION: One quality condition is marginally not met (e.g., 28% peer-reviewed vs. 30% required). Identify the specific gap and suggest what source types would correct it.

FAIL: Two or more quality conditions not met, or the peer-reviewed percentage is below 20%, indicating the document is primarily a secondary synthesis without adequate primary literature grounding.

---

**Item 10 — Citation Accuracy (20% Sample)**

PASS: The reviewer tests every 5th citation (20% sample). At least 87% of tested citations are: accessible (URL returns non-error response OR bibliographic reference is verifiable), accurately described in the text (the cited source actually says what the author claims it says), and appropriate for the claim being supported (a practitioner guide cited for a mechanism claim is appropriate; a news article cited for a mechanistic claim requires scrutiny).

NEEDS-REVISION: One or two tested citations are inaccurately described or cite sources that do not support the claim. Identify each error.

FAIL: More than two tested citations are inaccurate, or more than 13% of tested URLs return errors.

---

**Item 11 — Source Diversity**

PASS: Citations draw from at least three distinct source types (academic journals, government/NGO reports, practitioner publications, grey literature, primary-source interviews or field data). No single perspective or school of thought dominates the citations.

NEEDS-REVISION: Source diversity is narrow — document draws overwhelmingly from one institution's publications or one disciplinary tradition. Suggest source types or specific sources from PHASE_6_DOMAIN_60_65_RESEARCH_LANDSCAPE.md that would diversify.

FAIL: All or nearly all citations come from a single institution or disciplinary tradition, creating a document that is effectively a summary of one organization's position rather than a synthesis.

---

**Item 12 — Recency of Sources**

PASS: For empirically active domains (63 Ecosystem Restoration, 64 Economic Resilience), at least 30% of citations are from 2020 or later. For domains with stable theoretical foundations (60, 61, 65), at least 20% are from 2020 or later. Older foundational works (Ostrom 1990, Polanyi 1966, Lave and Wenger 1991) are legitimate citations regardless of age.

NEEDS-REVISION: The document relies heavily on older sources where newer research exists. Identify 2–3 recent publications from PHASE_6_DOMAIN_60_65_RESEARCH_LANDSCAPE.md that the author should incorporate.

FAIL: No sources from the past five years in a domain with active recent publication (Domain 63 and Domain 64 in particular have extensive 2024–2026 literature; a document with no recent citations in these domains has missed the current state of knowledge).

---

### Block 3 — Content Quality Review (Items 13–20)

**Item 13 — Implementation Pathway Specificity**

PASS: At least one implementation pathway includes: named starting condition, sequenced steps (numbered or explicitly ordered), resource requirements at each step (time, materials, or cost), and at least three measurable success metrics.

NEEDS-REVISION: A pathway is present but missing one or two of the required elements (e.g., steps are present but no resource estimates; or metrics are present but not measurable at community scale without specialist equipment). Identify the specific gaps.

FAIL: No implementation pathway meets the specificity standard — all implementation content is descriptive ("communities can do X") without sequenced steps or resource estimates.

---

**Item 14 — Actionability of Pathways**

PASS: A Zone 5 community coordinator reading Section 4 and Section 5 can begin implementation from the document alone — they have enough information to identify their starting condition, take the first two steps, and know how to assess progress. They may need additional resources for advanced steps, but they can start.

NEEDS-REVISION: A coordinator reading the document would know what to do in principle but not know how to start specifically. Identify where the gap between principle and specific first action occurs.

FAIL: The document describes what exists or what should be done but provides no pathway for starting. This is the "reads like a research outline" failure mode the entire quality system is designed to prevent.

---

**Item 15 — Technical Accuracy**

PASS: The reviewer, using their domain expertise or the expert contact starter lists in PHASE_6_DOMAIN_60_65_RESEARCH_LANDSCAPE.md, can verify that the document's central technical claims are accurate. No significant factual errors in core mechanisms or implementation protocols.

NEEDS-REVISION: One or two factual errors in peripheral claims (not in core mechanisms). Identify each error and the correct information.

FAIL: One or more factual errors in core mechanisms or implementation protocols — errors that, if followed, would lead a community to take harmful or ineffective action. (Example: incorrect soil amendment application rates, incorrect governance transition triggers, incorrect complementary currency design parameters.)

---

**Item 16 — Claim/Source Binding (Full Review)**

PASS: Reading the document, the reviewer cannot identify more than two unsourced factual claims (beyond the spot-check done in the publication-ready checklist). Claims that appear to be the author's analysis, synthesis, or framing (rather than empirical assertions) do not require individual citations.

NEEDS-REVISION: Three to six unsourced factual claims identified. Provide the specific sentences and suggest appropriate source types.

FAIL: Seven or more unsourced factual claims. The document makes empirical assertions throughout without citation support — it reads as opinion rather than evidence-based research.

---

**Item 17 — International Precedent Quality**

PASS: Section 6 (International Precedent) presents at least two non-US examples with: named geographic location, named community or organization, specific outcome data or process description, and Zone 5 translation (how does this precedent apply in Zone 5?).

NEEDS-REVISION: International precedents are named but described at insufficient depth for transfer (e.g., "Zapatista communities have done this" without describing what specifically they did, what the outcome was, and how it translates). Identify which examples need deeper treatment.

FAIL: No international precedents present, or precedents are so thinly described (two sentences each) that they provide no transferable value.

---

**Item 18 — Zone 5 Specificity**

PASS: The document is specifically applicable to Zone 5 (Midwest US hardiness zone, primarily agricultural, predominantly rural, four-season climate). Generic community resilience recommendations that would apply in any context are present only as background; Zone 5-specific adaptations are the document's core contribution.

NEEDS-REVISION: The document is applicable in Zone 5 but is not specific to it — the same document could have been written for Zone 8 coastal California without significant changes. Identify where Zone 5-specific content is missing.

FAIL: The document operates entirely at the generic level. No Zone 5-specific content (no Zone 5 climate, soil, crop, institution, regulatory environment, or cultural context) appears. This is a complete scope failure.

---

**Item 19 — Summary Section Quality**

PASS: The Summary section (a) synthesizes the document's key findings in 3–5 bullet points, (b) includes a practitioner decision matrix (as a table — at minimum: "if your community is in condition X, take action Y"), and (c) explicitly names all three cross-domain bridges.

NEEDS-REVISION: Summary is present but is a narrative recap rather than a synthesis; or the practitioner decision matrix is missing or too vague to act on; or cross-domain bridges are named in the body but not consolidated in the Summary. Identify which elements need development.

FAIL: Summary section is absent or is a single paragraph with no decision matrix and no cross-domain bridge consolidation.

---

**Item 20 — Language and Readability**

PASS: The document reads cleanly — no run-on paragraphs (maximum 8 sentences per paragraph), no undefined acronyms, no jargon without definition, no passive voice overuse. Not seeking perfection; assessing whether language is a barrier to comprehension.

NEEDS-REVISION: Specific sections have readability issues (long paragraphs, undefined acronyms, dense jargon passages). Identify the specific locations.

FAIL: Language issues are pervasive throughout the document — the reviewer would need to recommend a full line-editing pass before the content can be evaluated on its merits. (Rare for established researchers; more common for first-time English-language authors or highly technical Tier B authors writing for a new audience.)

---

### Reviewer Feedback Template

Complete and return to author within 48 hours of receiving the document.

```
WAVE 2 PEER REVIEW FEEDBACK
Document Title: _______________
Author: _______________
Author Domain: _______________
Reviewer: _______________
Review Date: _______________
Review Window: First Draft (July) / Final Review (August)

BLOCK 1 — STRUCTURAL AND SCOPE
Item 1 — Scope Compliance:          PASS / NEEDS-REVISION / FAIL
Item 2 — Section Structure:         PASS / NEEDS-REVISION / FAIL
Item 3 — Section Word Count:        PASS / NEEDS-REVISION / FAIL
Item 4 — Total Word Count:          PASS / NEEDS-REVISION / FAIL
Item 5 — Audience Calibration:      PASS / NEEDS-REVISION / FAIL
Item 6 — Tonal Consistency:         PASS / NEEDS-REVISION / FAIL
Item 7 — Cross-Domain Bridges:      PASS / NEEDS-REVISION / FAIL

BLOCK 2 — SOURCE QUALITY
Item 8 — Citation Count:            PASS / NEEDS-REVISION / FAIL
Item 9 — Citation Quality:          PASS / NEEDS-REVISION / FAIL
Item 10 — Citation Accuracy:        PASS / NEEDS-REVISION / FAIL
Item 11 — Source Diversity:         PASS / NEEDS-REVISION / FAIL
Item 12 — Source Recency:           PASS / NEEDS-REVISION / FAIL

BLOCK 3 — CONTENT QUALITY
Item 13 — Pathway Specificity:      PASS / NEEDS-REVISION / FAIL
Item 14 — Pathway Actionability:    PASS / NEEDS-REVISION / FAIL
Item 15 — Technical Accuracy:       PASS / NEEDS-REVISION / FAIL
Item 16 — Claim/Source Binding:     PASS / NEEDS-REVISION / FAIL
Item 17 — Intl. Precedent Quality:  PASS / NEEDS-REVISION / FAIL
Item 18 — Zone 5 Specificity:       PASS / NEEDS-REVISION / FAIL
Item 19 — Summary Quality:          PASS / NEEDS-REVISION / FAIL
Item 20 — Language/Readability:     PASS / NEEDS-REVISION / FAIL

SUMMARY ASSESSMENT
Total FAIL items: ___
Total NEEDS-REVISION items: ___
Total PASS items: ___

Overall Assessment:
[ ] PUBLICATION-READY (0 FAILs, ≤4 NEEDS-REVISION): Ready for final checklist
[ ] REVISE AND RESUBMIT (0 FAILs, 5–9 NEEDS-REVISION): Author addresses all items; no second full review required, project lead spot-checks
[ ] MAJOR REVISION REQUIRED (1+ FAILs OR 10+ NEEDS-REVISION): Full second review cycle needed after author revisions
[ ] HOLD FOR PROJECT LEAD (structural or scope issue exceeds reviewer's mandate): Flag to project lead before returning to author

REQUIRED DETAIL FOR EACH NON-PASS ITEM:
[List each NEEDS-REVISION and FAIL item here with: item number, location in document (section/paragraph), specific description of the problem, and specific description of what is needed to reach PASS status]

OPTIONAL — POSITIVE FEEDBACK (Not Required but Valued):
[Note 1–3 specific strengths of the document that the author should preserve through revision]
```

---

## Part 3: Turnaround SLA and Escalation

### Standard SLA

**Reviewer turnaround: 48 hours maximum from document receipt to completed feedback delivery.**

The 48-hour window is the maximum, not the target. Reviewers who complete feedback within 24 hours enable authors to begin revisions earlier and protect the publication schedule margin.

**How the 48-hour window is measured:**
- Start time: The moment the author posts the document to the reviewer's Nextcloud folder OR sends a Matrix notification that the document is ready for review. Start time is recorded in the author's Matrix domain room.
- End time: The moment the reviewer posts completed feedback to the author's Nextcloud folder AND sends a Matrix notification to the author. End time is self-reported by the reviewer.

**Author revision turnaround: 24 hours maximum after receiving feedback.**

Authors have 24 hours to address all NEEDS-REVISION items and resubmit. For MAJOR REVISION REQUIRED assessments (1+ FAILs), the author has 48 hours for the first revision pass, after which the reviewer does a targeted re-review of the failed items only (not a full 20-item pass — just the FAIL items and any NEEDS-REVISION items that may have been affected by the FAIL correction).

### Escalation Mechanism

**If the reviewer does not return feedback within 48 hours:**

1. At 36 hours: Author sends a Matrix reminder to the reviewer: "Checking in — feedback due in 12 hours. Let me know if you need an extension."
2. At 48 hours with no feedback: Author notifies project lead via Matrix and email: "Reviewer [name] has not returned feedback for [document title] as of [timestamp]. 48-hour SLA missed."
3. Project lead response within 6 hours of notification: Contact reviewer directly. If reviewer is unavailable: activate backup reviewer from the reviewer pool. Backup reviewer gets an expedited 24-hour SLA (not 48-hour) given the schedule impact.
4. If no backup reviewer is available: Project lead performs the review personally using this checklist. Project lead review may be compressed (12-item spot-check rather than full 20 items) if timeline pressure is severe, with notation that a partial review was completed.

**If the author does not submit revisions within 24 hours:**

1. Reviewer notifies project lead: "Author [name] has not resubmitted after feedback for [document]. 24-hour revision window missed."
2. Project lead contacts author directly within 4 hours.
3. If author is experiencing a blocking issue (illness, access problem, research gap requiring additional source work): grant a one-time 48-hour extension. Log in WAVE_2_QUALITY_GATE_INTEGRATION.md for July 5 checkpoint assessment.
4. If author has abandoned the revision or cannot identify a path to resolving the FAIL items: escalate to domain split or Tier-3 editor support (see WAVE_2_QUALITY_GATE_INTEGRATION.md Part 3).

### Schedule Implications of SLA Misses

| SLA Miss | Schedule Impact | Recovery Path |
|----------|----------------|---------------|
| Reviewer 48h miss, backup assigned same day | 0–12 hours slip | None required if backup completes within expedited window |
| Reviewer 48h miss, no backup available, project lead reviews | 12–24 hours slip | Monitor at July 5 checkpoint; no action if single occurrence |
| Author 24h miss, 48h extension granted | 24 hours slip | Absorbed within standard schedule margin |
| Author 24h miss, revision not completed within extension | 72+ hours slip | Escalate to July 5 checkpoint with CAUTION flag |
| Two or more SLA misses on same document | 5–7 day slip | Author moves to Tier-3 editor support protocol |

---

## Part 4: Multiple-Review Protocol for Tier C Authors

Tier C authors (score 6–13 on five-dimension rubric) receive two peer reviewers by default. The rationale is that Tier C authors are more likely to have structural gaps that a single reviewer might miss, and that the additional review round adds quality insurance that is proportionate to the risk.

### Two-Reviewer Assignment for Tier C

The project lead assigns two reviewers to every Tier C author at the June 14 matching session. Both reviewers receive the document simultaneously. Both return independent feedback within 48 hours. The author receives both feedback documents at the same time.

**Reviewer 1** (Primary): Adjacent-domain reviewer from the Wave 2 author pool or Phase 5 author pool. Completes all 20 checklist items. Focuses on structural and scope items (Block 1) and content quality (Block 3).

**Reviewer 2** (Secondary): May be a more distant-domain reviewer or an external domain expert from the starter lists. Completes Block 2 (source quality) in full and Items 13–16 from Block 3. Does not complete Block 1 — primary reviewer owns structural assessment.

This division of labor ensures that: (a) a full structural review happens without overwhelming either reviewer, (b) the citation audit is double-checked, and (c) an external expert validates the technical claims even if the primary reviewer is not a domain specialist.

### Handling Disagreement Between Two Reviewers

**When Reviewer 1 and Reviewer 2 agree**: Straightforward. Author addresses all flagged items. No escalation.

**When Reviewer 1 gives PASS and Reviewer 2 gives NEEDS-REVISION on the same item**: Author treats it as NEEDS-REVISION. The more conservative assessment stands. Author addresses the flagged item.

**When Reviewer 1 gives NEEDS-REVISION and Reviewer 2 gives FAIL on the same item**: Project lead is notified. Project lead reads the item in the document and makes a call within 24 hours: FAIL (major revision required) or NEEDS-REVISION (author can correct with targeted editing). Project lead's call is final.

**When Reviewer 1 gives PASS and Reviewer 2 gives FAIL on the same item**: Project lead is notified immediately (same day). Project lead reads the document section in question, reviews both reviewers' reasoning, and makes a call. This pattern — where two qualified reviewers disagree by two full rating levels — indicates either (a) the two reviewers are applying different standards, (b) the document section is genuinely ambiguous, or (c) one reviewer has misread the document. Project lead diagnoses which and issues a binding judgment.

**When both reviewers give FAIL on the same item**: The author has a confirmed structural problem. Author and project lead hold a 30-minute scope alignment call within 24 hours of receiving the feedback. The call produces a revision plan. Author implements the revision plan and resubmits for a second full review cycle (both reviewers receive the revised document; 48-hour SLA applies again).

---

## Part 5: Conflict Resolution — Author and Reviewer Disagree on Publication Readiness

The primary escalation path when an author believes their document is publication-ready and the reviewer disagrees.

### When Conflict Arises

An author may dispute a reviewer's FAIL assessment when:
- The author believes the flagged item is present in the document and the reviewer has misread it
- The author believes the flagged item is not within scope for their domain or tier
- The author has addressed a NEEDS-REVISION item in revision and the reviewer still rates it NEEDS-REVISION after revision

An author may NOT dispute a reviewer's judgment on the basis of the following:
- "The reviewer is from a different domain and doesn't understand mine" (adjacent-domain reviewers are intentionally used for scope detection; their not-understanding is diagnostic)
- "The reviewer's standard is too high" (standards are defined in this protocol and WAVE_2_PUBLICATION_READY_CRITERIA.md; disputes about standards go to the project lead, not the reviewer)

### Escalation Path

**Step 1 — Author-Reviewer Direct Dialogue (24 hours)**

Author and reviewer exchange written messages (Matrix or email) to clarify the disputed item. Reviewer specifies the exact text in the document that fails the criterion. Author describes their interpretation of why the text passes. This exchange is documented in the Nextcloud folder as `DISPUTE_[DOMAIN]_[DATE].md`.

**Step 2 — Project Lead Third-Party Review (48 hours from Step 1 conclusion)**

If Step 1 does not resolve the dispute: author notifies project lead with the `DISPUTE` document. Project lead reads the specific document section and the two parties' arguments. Project lead issues a binding decision:

- PASS: The criterion is met. Reviewer's assessment was incorrect. Document proceeds.
- NEEDS-REVISION: The criterion is not fully met but can be addressed with targeted editing. Author makes specific edit; no second full review required.
- FAIL: The criterion is not met and cannot be addressed with editing alone. Major revision required. Author and project lead agree on a revision plan with a specific deadline.

**Project lead's decision is final and not subject to further appeal within Wave 2.**

**Step 3 — Domain Split or Tier-3 Editor Escalation (if FAIL cannot be resolved)**

If the author cannot resolve a FAIL within the escalation timeline (see WAVE_2_QUALITY_GATE_INTEGRATION.md for the August 30 deadline), the project lead activates one of two options:

- **Domain split**: The publication-ready portions of the document (typically 4,000–6,000 words) are published as Part A. The sections with unresolved FAIL items are deferred to Wave 3 as Part B. Part A is not labelled "incomplete" — it is labelled "Phase 6 Wave 2 [Domain] — Community Foundations" with a brief note that a companion document on advanced implementation is in development.

- **Tier-3 editor support**: The project lead brings in an external editor with domain expertise to complete the FAIL sections. The external editor is credited as a contributor (not co-author) in the publication. The author retains primary authorship credit. This option is used when the author has strong foundational content but cannot complete the advanced sections within timeline.

---

*Version 1.0 — Phase 6 Wave 2 — Created June 5, 2026*
*Use alongside WAVE_2_PUBLICATION_READY_CRITERIA.md and WAVE_2_QUALITY_GATE_INTEGRATION.md*
*Reviewer assignments must be finalized by June 14 matching session. SLAs accepted before June 20 kickoff.*
