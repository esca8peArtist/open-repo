---
title: "Phase 5 Option B Execution Toolkit — Unified Release"
project: systems-resilience
phase: 5
option: B
status: ACTIVATION-READY
decision_trigger: User selects Option B by May 31 23:59 UTC
publication_target: 2026-06-15
editorial_window: 2026-06-01 through 2026-06-14
total_words: 66442
confidence: 90%
created: 2026-05-27
---

# Option B Execution Toolkit: Unified Release
## Full 66,442-Word Corpus on June 15

> **Activation trigger**: User selects Option B (checkbox in PHASE_5_PUBLICATION_DECISION_FRAMEWORK.md)
> **Critical resource gate**: Confirm 10-15 hours editorial capacity June 1-14 BEFORE proceeding
> **First action**: Within 15 minutes of decision — see Phase B-0 below
> **Execution window**: June 1-15, 2026

---

## Why Option B (and Why Its Risks Are Real)

Option B scored 24/40 in the decision matrix — the lowest of the three options — but it wins on two specific criteria: discoverability (a single "66,000-word comprehensive guide" is a stronger artifact than a staged release) and distribution leverage (one high-density announcement moment).

The tradeoff is clear: two weeks of reader impact are sacrificed to editorial integration work. Communities that could have started acting on Wave 1+2 in June 1-5 instead wait until June 15. And the 10-15 hour editorial window is tight: citation consolidation (renumbering 423 references across 12 documents) alone takes 3+ hours, and any slip in the June 1-14 window creates a June 15 slip.

**Choose Option B if**:
- The corpus needs to function as a single authoritative reference (academic libraries, institutional adoption)
- You have confirmed 10-15 editorial hours available June 1-14
- A single canonical URL and announcement moment is strategically important for your distribution goals

**Do not choose Option B if**:
- Editorial hours are not confirmed
- Community practitioners need the content as soon as possible
- Any delay risk is unacceptable (Option A has lower execution risk)

**Confidence level**: 90% (contingent on editorial hours being available and no major integration issues discovered during citation consolidation)

---

## Phase B-0: Decision Activation — Capacity Gate (15 Minutes)

**CRITICAL**: This gate must pass before any other work begins.

**Minutes 0-5**: Confirm user selected Option B. Read any user notes on specific integration priorities or deadline flexibility.

**Minutes 5-10**: **Capacity confirmation** — answer both questions:
1. Is there a person available 1-2 hours/day, June 1-14? (14 days × 1 hour minimum = 14 hours)
2. Do they have read/write access to all 12 source documents?

**If NO to either question**: Stop. Recommend Option A. The editorial window cannot be compressed below 10 hours — attempting Option B without capacity creates a June 15 slip and no backup plan.

**Minutes 10-15**: Create `PHASE_5_EXECUTION_LOG.md`:
```
Option Selected: B (Unified)
Decision Date: [date/time]
Publication Target: June 15, 2026, 10:00 AM UTC
Editorial Window: June 1-14 (10-15 hours)
Editorial Capacity Confirmed: YES / NO
Status: [ACTIVE or STOPPED — CAPACITY NOT CONFIRMED]
```

---

## Phase B-1: Pre-Integration Inventory (May 31 Evening)

### Confirm All 12 Documents Are Present

Verify each file exists and is readable:

**Wave 1+2 (5 documents)**:
- `phase-5-wave-2-community-implementation-playbook.md` (8,619 words)
- `phase-5-wave-2-microgrids-research.md` (6,545 words)
- `phase-5-wave-2-psychological-support-guide.md` (9,163 words)
- `phase-5-wave-2-conflict-resolution-framework.md` (8,596 words)
- `phase-5-wave-2-veterinary-care-guide.md` (10,698 words)

**Wave 3 (7 documents)**:
- `phase-5-wave-3-food-preservation-and-storage.md` (4,865 words)
- `phase-5-wave-3-water-systems-and-purification.md` (4,943 words)
- `phase-5-wave-3-livestock-care.md` (2,943 words)
- `phase-5-wave-3-seed-saving-and-storage.md` (2,426 words)
- `phase-5-wave-3-healthcare-offline.md` (2,930 words)
- `phase-5-wave-3-fuel-production-and-storage.md` (2,567 words)
- `phase-5-wave-3-educational-governance.md` (2,147 words)

Run total word count:
```bash
wc -w phase-5-wave-2-*.md phase-5-wave-3-*.md
```
Expected: 66,442 words combined

### Create Integration Roadmap File

Create `PHASE_5_B_EDITORIAL_INTEGRATION_ROADMAP.md` (working document for June 1-14):

```markdown
# Option B Editorial Integration Roadmap

Publication target: June 15, 2026
Total editorial hours: 10-15
Checkpoint format: End-of-day log entry for each June 1-14 day

Integration tasks:
1. Frontmatter standardization (2 hours) — June 1-2
2. Citation consolidation (3 hours) — June 3-6
3. Cross-reference integration (3 hours) — June 7-10
4. Master Table of Contents (2 hours) — June 11-12
5. Quality spot-check (1 hour) — June 13
6. Final formatting and PDF prep (1 hour) — June 14

Quality gates (must pass before June 15):
[ ] All 12 documents have consistent YAML frontmatter
[ ] No broken [N] citation references in any document
[ ] Every Wave 3 document references 2-4 Wave 1+2 documents
[ ] Master TOC matches actual document structure (100%)
[ ] Writing voice at least 80% consistent across all 12 documents

End-of-day log format:
Date | Tasks completed | Hours | Blockers | Tomorrow's priority
```

---

## Phase B-2: Frontmatter Standardization (June 1-2, 2 Hours)

### Standard Frontmatter Template

All 12 documents must use this YAML block at the top:

```yaml
---
title: "[Document Title]"
phase: 5
wave: "[1-2 or 3]"
release_date: 2026-06-15
status: production-ready
word_count: [number]
citations: [number]
zone_focus: Midwest Zone 5 (IL, MI, IA, IN, WI)
audience: [primary audience description]
volume: unified
corpus_total_words: 66442
corpus_total_documents: 12
---
```

**June 1 (30 minutes)**: Update all 5 Wave 1+2 documents

**June 2 (30 minutes)**: Update all 7 Wave 3 documents

**Quality gate after June 2**: Open each of the 12 documents and verify the YAML block is present, parseable, and contains all required fields. A malformed YAML block breaks Obsidian and any static site generator.

---

## Phase B-3: Citation Consolidation (June 3-6, 3 Hours)

This is the most technically intensive and time-sensitive task. Do not skip or abbreviate it.

### The Problem

Wave 1+2 documents contain citations numbered [1] through approximately [210] (internal to the wave). Wave 3 documents contain citations [1] through approximately [213] (independent numbering). If both sets are published together without renumbering, readers will find "[1]" referenced in two different documents pointing to different sources.

### The Process

**Step 1 (June 3, 60 min)**: Extract citation lists from Wave 1+2

For each Wave 1+2 document, locate the references/bibliography section. Create a master list of all Wave 1+2 sources with their current [N] numbers. Record: `[N] — author/title/URL — which document`.

**Step 2 (June 4, 60 min)**: Extract citation lists from Wave 3

Same process for all 7 Wave 3 documents. Identify the current [1]-[213] numbering in Wave 3 documents. Record which [N] numbers exist and what sources they point to.

**Step 3 (June 5, 60 min)**: Renumber Wave 3 citations

Wave 1+2 citations keep their numbers [1]-[~210]. Wave 3 citations are renumbered to continue the sequence: Wave 3's [1] becomes [211], Wave 3's [2] becomes [212], etc. For each Wave 3 document:
- Create a mapping table: old [N] → new [N]
- Run a global find/replace using the mapping (work document by document, not corpus-wide)
- Verify: no original Wave 3 citation number remains unreplaced

**Step 4 (June 6, 30 min)**: Build master bibliography

Create a single `PHASE_5_MASTER_BIBLIOGRAPHY.md` with all 423 sources in order [1]-[423]. Each entry includes: number, author/organization, title, URL or publication, year.

**Step 5 (June 6, 30 min)**: Spot-check verification

Open 5 random documents and spot-check 4-5 citations each (total: ~25 citation checks). Verify the citation number in the text matches the correct source in the master bibliography. Zero errors acceptable here — citation integrity is the most visible quality dimension for academic/institutional readers.

### Risk Mitigation

The highest risk is creating a broken reference (a [N] in the text that doesn't exist in the bibliography, or points to the wrong source). To prevent this:
- Keep original citation lists open side-by-side while renumbering
- Work one Wave 3 document at a time (do not renumber multiple documents in a single session)
- After renumbering each document, immediately verify 3 random citations in that document before moving on

---

## Phase B-4: Cross-Reference Integration (June 7-10, 3 Hours)

Wave 3 documents were written independently from Wave 1+2. They do not internally reference the Wave 1+2 foundation. A reader picking up the Water Systems document should be able to find "for grid-tied power considerations, see Microgrids Section 4.2" rather than encountering the topic in isolation.

### Cross-Reference Map

Add callout boxes (1-2 sentences each) to each Wave 3 document at relevant section entry points:

| Wave 3 Document | Required Cross-References | Where to Add |
|-----------------|--------------------------|--------------|
| Food Preservation & Storage | Implementation Playbook (supply chain logistics), Conflict Resolution (food allocation under scarcity) | Near sections on community-scale storage and distribution |
| Water Systems & Purification | Microgrids (power for pumps, treatment systems), Implementation Playbook (maintenance coordination) | Near infrastructure planning and governance sections |
| Livestock Care | Veterinary Care Guide (integrated health protocols), Conflict Resolution (herd ownership/access disputes), Psychological Support (animal loss) | Near health protocols and community herd management |
| Seed Saving & Storage | Food Preservation (storage integration), Conflict Resolution (seed library governance) | Near community seed library and storage sections |
| Healthcare Offline | Psychological Support (mental/physical health integration), Conflict Resolution (group medical decision-making) | Near sections on community health governance |
| Fuel Production & Storage | Microgrids (power system integration), Implementation Playbook (labor coordination for fuel production) | Near production planning and infrastructure sections |
| Educational Governance | Conflict Resolution (institutional governance framework), Implementation Playbook (organizational structure) | Near governance design and organizational sections |

**Format for each callout**:
```
> **Cross-reference**: For [broader context], see [Document Title], Section [X] (Volume 1 of this corpus).
> [1-sentence explanation of the connection.]
```

**Allocation**: 30 minutes per Wave 3 document × 7 documents = 3.5 hours. Over June 7-10, this is approximately 50 minutes/day.

**Quality gate**: After completing all 7 Wave 3 documents, count total cross-references. Target: 21 or more (3 per document × 7 documents = 21 minimum). Each cross-reference must point to a section that actually exists in the target document — do not cross-reference a section that was removed or renamed.

---

## Phase B-5: Master Table of Contents (June 11-12, 2 Hours)

The Master TOC is the navigational spine of the unified corpus. It must be complete, accurate, and useful — not just a list of documents but a genuine reading guide.

### Structure

```markdown
# Phase 5: Systems Resilience at the Community Scale
## Complete Corpus — June 15, 2026
## 66,442 Words | 12 Documents | 423 Citations

---

### How to Use This Guide

This corpus covers community-scale resilience in two integrated layers:

**Layer 1 (Documents 1-5)**: Community foundations — how to organize, power,
psychologically support, govern, and provide animal care for a 15-100 person community.

**Layer 2 (Documents 6-12)**: Practical operations — food, water, livestock, seeds,
healthcare, fuel, and education at community and household scale.

**Reading paths by audience:**

For community leaders starting from scratch:
→ Community Implementation Playbook → Microgrids → Psychological Support →
  Conflict Resolution → Food Preservation → Water Systems

For communities already organized, adding operational depth:
→ Jump to specific operational documents (Documents 6-12) as needed

For technical/infrastructure specialists:
→ Microgrids → Water Systems → Fuel Production → cross-reference Playbook for
  organizational integration

For facilitators and governance leaders:
→ Conflict Resolution → Psychological Support → Community Implementation Playbook →
  Educational Governance

---

### Part I: Community Foundations

#### Document 1: Community Implementation Playbook (8,619 words)
Organizational structure, decision-making systems, labor coordination,
resource management, and phased implementation roadmap for 15-100 person communities.
[Key sections: organizational design, governance integration, 4-phase launch sequence]

#### Document 2: Microgrids — Community Energy Infrastructure (6,545 words)
Distributed energy planning: AC/DC architecture, battery storage sizing, generation mix
(solar/wind/backup), Zone 5 seasonal analysis, regulatory landscape, implementation timeline.
[Key sections: architecture options, Zone 5 sizing guide, interconnection, maintenance]

#### Document 3: Psychological Support Guide (9,163 words)
Community mental health under stress: trauma response, group cohesion, facilitator tools,
grief protocols, long-term psychological resilience architecture.
[Key sections: trauma-informed frameworks, facilitator skill set, group resilience practices]

#### Document 4: Conflict Resolution Framework (8,596 words)
Governance under pressure: decision-making architecture, voting and consent models,
conflict de-escalation protocols, resource allocation disputes, leadership accountability.
[Key sections: decision models, conflict escalation ladder, resource allocation frameworks]

#### Document 5: Veterinary Care Guide (10,698 words)
Animal healthcare in crisis contexts: triage, wound care, disease management, crisis-context
treatment decisions, Zone 5 regional considerations across species.
[Key sections: triage protocols, species-specific guides, Zone 5 disease patterns]

---

### Part II: Practical Operations

#### Document 6: Food Preservation & Storage (4,865 words)
Long-term food security techniques: canning, fermentation, dehydration, root cellaring,
community-scale storage design, and seasonal planning for Zone 5.
[Key sections: technique comparison matrix, storage infrastructure, seasonal calendar]

#### Document 7: Water Systems & Purification (4,943 words)
Sourcing (wells, springs, rainwater, surface), treatment, storage, greywater systems,
and water governance for communities sharing water resources.
[Key sections: Zone 5 groundwater, treatment options, governance frameworks]

#### Document 8: Livestock Care (2,943 words)
Hands-on protocols for small-to-medium herds: feeding, health monitoring, seasonal care,
crisis-context triage, and Zone 5 winter management.
[Key sections: species-specific care schedules, Zone 5 winter protocols]

#### Document 9: Seed Saving & Storage (2,426 words)
Heirloom variety selection, isolation distances, harvest timing, storage conditions,
viability testing, and community seed library governance.
[Key sections: Zone 5 variety selection, storage conditions, library governance]

#### Document 10: Healthcare Offline (2,930 words)
Medical care without professional infrastructure: wound management, medication
management, triage, childbirth, chronic disease management, and community health organization.
[Key sections: triage framework, medication sourcing/storage, community health coordinator role]

#### Document 11: Fuel Production & Storage (2,567 words)
Biodiesel, wood gas, propane — crisis-context energy beyond the electric grid.
Production processes, safety, storage, and integration with microgrid infrastructure.
[Key sections: production comparison, Zone 5 feedstocks, storage safety]

#### Document 12: Educational Governance (2,147 words)
Community-run schooling: curriculum frameworks, teacher sourcing, knowledge
transmission across generations, institutional design for long-term learning.
[Key sections: curriculum architecture, intergenerational knowledge transfer, governance]

---

### Appendix A: Master Bibliography
All 423 sources in citation order [1]-[423]

### Appendix B: Cross-Reference Index
Find all passages on specific topics (microgrids, psychology, governance, water, etc.)
across all 12 documents — organized by subject area, with document and section reference.
```

**June 11 (1 hour)**: Write the navigational sections (reading paths, overview descriptions)

**June 12 (1 hour)**: Write the document-level entries and appendix headers; verify against actual document structure to confirm no section references are inaccurate

---

## Phase B-6: Quality Spot-Check (June 13, 1 Hour)

Run each quality gate systematically:

**Gate 1 — Frontmatter completeness** (15 min)
Open each of the 12 documents and verify the YAML header is present and has all required fields. If any are missing: fix immediately.

**Gate 2 — Citation integrity** (20 min)
Randomly select 20 [N] references across the corpus (at least 2 per document, weighted toward Wave 3 where renumbering happened). Verify each reference resolves correctly in the master bibliography. Zero broken citations acceptable.

**Gate 3 — Cross-reference accuracy** (10 min)
Select 5 of the 21+ cross-reference callouts added in Phase B-4. Verify that each points to a section that actually exists in the referenced document. Fix any that point to non-existent or renamed sections.

**Gate 4 — Master TOC accuracy** (10 min)
Select 4-5 entries from the Master TOC. Open the corresponding document and verify the section descriptions are accurate. Fix any mismatches.

**Gate 5 — Voice consistency** (5 min)
Read the first 2-3 paragraphs of Document 1, Document 6, and Document 12. Assess: does the writing voice feel compatible (not identical, but coherent within a single corpus)? If one document sounds dramatically different, note it but do not attempt a full rewrite — the June 14 deadline is fixed.

---

## Phase B-7: Final Formatting (June 14, 1 Hour)

**Morning (30 min)**:
- Confirm all 12 documents in consistent markdown format
- Add explicit page break markers between documents if generating a single PDF (`---` or `\pagebreak` depending on rendering system)
- Verify that the Master TOC document is properly integrated (either as Document 0 or as the opening page of the combined PDF)
- Test PDF rendering if generating a single-file corpus

**Afternoon (30 min)**:
- Final pass: read opening paragraph of each document one more time
- Confirm all frontmatter fields are correct and consistent
- Create `PHASE_5_B_QUALITY_GATES_LOG.md` recording which gates passed and any known residual issues

**Hard stop at 5:00 PM UTC, June 14**: No additional editorial changes after this point. June 15 morning is distribution-only. If an issue is discovered after 5:00 PM June 14, assess whether it is critical (broken citations, factual error) or cosmetic (phrasing, formatting) and act accordingly:
- Critical: fix and distribute on June 15 with a 2-line erratum note
- Cosmetic: log for future revision, distribute as-is

---

## Phase B-8: Publication and Distribution (June 15)

### June 15, 9:00 AM UTC — Final Quality Check (30 minutes)

Open the combined corpus PDF or the master document index. Spot-check:
- 3 random sections (one from Wave 1+2, one from Wave 3, one cross-reference callout)
- Confirm no layout errors, broken citations, or formatting issues visible
- Approve for distribution

### June 15, 10:00 AM UTC — Email Distribution (60 minutes)

Send to all distribution contacts simultaneously (unified release; no staggering by network type):

Subject: Systems Resilience: Complete 66,400-Word Guide — All 12 Research Documents

```
Dear [Name/Network],

We've published the complete Phase 5 systems resilience research corpus — 66,442 words,
12 documents, 423 citations, covering community-scale resilience from organization to
practical operations.

Contents:
Part I (Community Foundations): Implementation playbook, microgrids, psychological
support, conflict resolution, veterinary care (43,621 words)

Part II (Practical Operations): Food preservation, water systems, livestock care, seed
saving, healthcare offline, fuel production, educational governance (22,821 words)

Zone 5/Midwest focus throughout. All materials free to download, adapt, and redistribute.
No registration. No paywall.

Download full corpus: [link]
Read specific documents: [index link]
Master table of contents: [direct link to TOC]

We welcome feedback for future editions. If you find gaps, Zone 5-specific improvements,
or factual corrections, please reply.
```

### June 15, 2:00 PM UTC — Social Media and Forum Posts (60 minutes)

Reddit primary post:
Title: "Complete Systems Resilience Guide — 66,400 Words, All 12 Research Documents, Free (Zone 5/Midwest Focus)"

Content: 500-word summary of corpus scope, reading paths, and key findings, plus download link.

Post to 5+ relevant subreddits: r/Permaculture, r/resiliency, r/mutual_aid, r/homesteading, r/farming (stagger over June 15-17 to avoid spam filters).

### June 15-30 — Feedback Monitoring

- Daily (15 min): check email and forum for responses
- Log substantive feedback in `PHASE_5_B_FEEDBACK_LOG.md`
- Respond to questions within 48 hours
- Identify top themes for any future second-edition planning

---

## Option B Success Metrics

### June 15 Publication On-Time
- [ ] Full 66,442-word corpus published by June 15 (no slippage)
- [ ] Master TOC complete and accurate
- [ ] All 12 documents accessible at single URL or index

### Editorial Integration Quality
- [ ] 0 broken citations in consolidated bibliography (spot-check 20 citations)
- [ ] All 12 documents have consistent YAML frontmatter
- [ ] 21+ cross-references from Wave 3 documents to Wave 1+2 foundation

### Distribution Coverage
- [ ] All planned distribution contacts received June 15 announcement
- [ ] Social media posts live by June 15, 4:00 PM UTC
- [ ] "Complete guide" messaging used consistently (not "Volume 1 and Volume 2")

### Post-Publication Quality
- [ ] No critical errors (broken citations, factual errors) reported by June 22
- [ ] Master TOC confirmed accurate by 3+ readers who used it for navigation
- [ ] Feedback log populated with 5+ substantive items by June 30

---

## Contingency: If June 15 Is At Risk

**If editorial integration is running 4+ hours over schedule at any point in June 1-14**:

Assess whether to slip to June 20 or switch to Option A fallback:

| Assessment Criterion | Slip to June 20 | Switch to Option A |
|----------------------|-----------------|-------------------|
| Issue is citation consolidation only | Yes — fixable in 3-5 extra hours | No |
| Issue is structural (Wave 3 contradicts Wave 1+2) | Depends on severity | If critical: yes |
| Editor hours confirmed through June 20 | Yes | No |
| Strategic reason for unified release still holds | Yes | No |

**Option A fallback (always available)**: If June 15 is no longer achievable, switch to Option A — publish Wave 1+2 immediately (it needs only 3-4 hours of work) and treat it as the original Wave 1+2 June 5 release. Wave 3 continues on its own timeline.

---

*Option B Execution Toolkit — Activation-ready upon user Option B decision*
*Created: 2026-05-27 | Status: AWAITING USER DECISION (deadline May 31 23:59 UTC)*
*Critical requirement: Confirm editorial capacity (10-15 hours, June 1-14) before activating*
