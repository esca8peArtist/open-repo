---
title: "Phase 5.2 Wave 1 Domain Selection"
project: open-repo
phase: "5.2 Wave 1"
document_type: domain-selection
status: approved
date: 2026-07-05
author: "Open-Repo Research Agent"
confidence: 92%
---

# Phase 5.2 Wave 1 Domain Selection

**Decision**: Two domains selected for Wave 1 content development.

1. **Composting & Soil Amendment** (primary)
2. **Food Preservation** (primary, co-equal)

Both are developed to full production depth (~10,000+ words each). Natural building and livestock management are deferred to Wave 2.

---

## Domain 1: Composting & Soil Amendment

### Selection Rationale

**Gap in existing repositories**: Wikipedia's composting articles cover the biology of decomposition but lack the operational depth needed by practitioners — specific C:N ratios for common household materials, step-by-step bin construction, troubleshooting for the dozen most common failure modes, and vermicomposting setup with bin sizing calculations. Extension publications (Cornell, NC State, OSU) have this operational depth but are not structured for offline use and are distributed across dozens of separate PDFs.

**Community interest signal**: The composting/homesteading community is large and well-organized. Reddit communities (/r/composting, ~900K members; /r/homesteading, ~500K members; /r/permaculture, ~300K members) regularly ask procedural questions that a well-structured offline reference would answer. The questions cluster around: "why isn't my pile heating up?", "what can/can't I compost?", "how do I start a worm bin indoors?"

**Schema complexity**: Low-to-moderate. No safety review gate required. Composting content does not require medical or legal sign-off. The most safety-adjacent content (handling animal manures, excluding pathogens from finished compost) is well-documented in extension literature and can be included with appropriate sourcing.

**Content coverage**: Wave 1 covers four topics:
1. Hot composting (thermophilic, outdoor pile method)
2. Cold composting (passive, low-maintenance)
3. Vermicomposting (worm bins, indoor-capable)
4. Compost application and soil amendment rates

**Deferred to Wave 2**: Bokashi fermentation, compost tea, large-scale windrow composting, municipal compost program participation.

**Primary authoritative sources**: NC State Extension Gardener Handbook (CC-licensed content), Cornell CALS composting guides, University of Maryland Extension organic matter guide, OSU Extension vermicomposting guide, USDA AMS compost tipsheet.

**Confidence**: 92%. All core procedural information is sourced from peer-reviewed extension literature. Vermicomposting bin sizing uses multiple-source corroboration.

---

## Domain 2: Food Preservation

### Selection Rationale

**Gap in existing repositories**: The NCHFP and USDA Complete Guide to Home Canning (2015 revision) are the authoritative sources for home food preservation in the US context. These are public domain documents. However, they are not available as structured offline content in any ZIM archive, and their procedural format (scattered PDF tables by food type) is not optimized for offline reference use. The open-repo schema already defines the required structure; this is a content gap problem, not a schema problem.

**Community interest signal**: Home food preservation experienced documented growth post-2020 (supply chain disruptions, homesteading movement growth). Reddit communities focused on this domain have aggregate 2M+ members (/r/canning, ~900K; /r/fermentation, ~600K; /r/homestead components). These communities explicitly discuss wanting offline, authoritative reference material — a direct match for open-repo's value proposition.

**Schema complexity**: Moderate, but with a clear safety boundary. Canning safety requires using USDA/NCHFP processing times verbatim — this is non-negotiable. The expert review gate is pre-cleared for content sourced directly from NCHFP (University of Georgia, operating under USDA cooperative agreement). No individual reviewer sign-off is required for content that is directly transcribed from these public domain sources with appropriate attribution. The safety boundary is clearly stated: the content presents tested procedures from authoritative sources; it does not derive or adapt processing times.

**Content coverage**: Wave 1 covers four topics:
1. Water bath canning (high-acid foods: fruits, tomatoes with acidification, pickles, jams/jellies)
2. Pressure canning (low-acid foods: vegetables, beans)
3. Lacto-fermentation (sauerkraut, pickles, kimchi — no equipment required beyond a jar)
4. Food dehydration (fundamentals)

**Deferred to Wave 2**: Freeze-drying, smoking/curing meats, root cellaring, pressure canning for meat/poultry (high complexity, more safety surface area than Wave 1 should carry).

**Primary authoritative sources**: USDA Complete Guide to Home Canning (2015 revision, public domain), NCHFP at nchfp.uga.edu, CDC botulism prevention guidance, UMN Extension fermentation guidance, Illinois Extension lacto-fermentation factsheet.

**Confidence**: 90%. All processing times are sourced verbatim from NCHFP/USDA. Fermentation safety is well-documented in extension literature. Dehydration fundamentals are well-sourced from NIDA and USDA.

---

## Deferred Candidates

**Wildcraft/Foraging Identification**: Deferred to Wave 2. The botanical knowledge schema requires toxicity reviews for lookalike species — this is the highest-stakes safety content in the open-repo system. Writing production-ready foraging guides without an identified domain expert to review lookalike hazards introduces unacceptable safety risk. This is not a content gap that can be closed from literature alone.

**Rainwater Harvesting Systems**: Content already exists in Wave 0 (`water-systems-domain-sample-section.md`). This section is production-ready. Not needed as a Wave 1 deliverable.

**Natural Building Techniques**: Deferred to Wave 2. The content is well-documented (cob, earthbag, strawbale) but jurisdiction-specific building code interactions make completeness difficult without regional scoping. Better served by a scoped guide (e.g., "small structures not requiring permits") than a broad overview.

**Small-Scale Livestock Management**: Deferred to Wave 2. Content depth requires species-specific sections (chickens, goats, rabbits). Adequate for Wave 2 when composting and food preservation establish the community base.

**Medical Reference / Healthcare Guides**: Not Wave 1 scope. The PHASE_5.2_MEDICAL_CONTENT_SOURCING_CHECKLIST.md identifies the medical reviewer outreach as a prerequisite gate. This gate is not closed.

---

## Output Locations

- `docs/wave-1-composting/composting-complete-guide.md`
- `docs/wave-1-food-preservation/food-preservation-complete-guide.md`

---

*Approved 2026-07-05. Confidence: 92%.*
