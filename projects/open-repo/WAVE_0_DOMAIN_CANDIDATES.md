---
title: "Wave 0 Domain Candidates — Scored Evaluation"
project: open-repo
phase: "5.2 Wave 0"
document_type: domain-assessment
status: draft-for-review
date: 2026-06-28
---

# Wave 0 Domain Candidates — Scored Evaluation

**Scope**: Five candidate domains (all have existing Phase 5.2 schemas). Scored against four criteria; recommendation is based on aggregate score weighted toward Gap and Recruitment.

**Scoring key**: 1 = weak, 2 = moderate, 3 = strong

---

## Scoring Matrix

| Domain | Gap Score (1-3) | Community Signal (1-3) | Schema Complexity (1=hard, 3=easy) | Recruitment Feasibility (1-3) | **Total** | **Priority** |
|---|---|---|---|---|---|---|
| Water Systems | 3 | 3 | 2 | 3 | **11** | Priority 1 |
| Food Preservation | 2 | 3 | 3 | 3 | **11** | Priority 2 (tie-broken by schema simplicity) |
| Seed Preservation | 2 | 2 | 2 | 2 | **8** | Priority 3 (community building) |
| Medical Reference | 3 | 1 | 1 | 1 | **6** | Standby — reviewer-gated |
| Botanical Knowledge | 1 | 2 | 2 | 2 | **7** | Wave 1 |

---

## Domain 1 — Water Systems

### Gap Analysis

**Score: 3/3 — Strong gap**

Wikipedia covers water treatment at the encyclopedic level: articles on chlorination, reverse osmosis, and the physics of slow sand filtration exist and are reasonably complete. What does not exist in a structured, offline, practical form:

- Step-by-step construction procedures for appropriate-technology water systems (slow sand filter from local materials, ceramic pot filter construction, rainwater harvesting cistern sizing)
- WHO WASH field manuals in machine-readable format. The WHO Emergency Water Supply manual (2011, updated 2013) is licensed for reproduction but not available as a ZIM file or structured JSON-LD
- Context-specific treatment protocols (flood event vs. drilled well vs. spring box vs. surface water from known source)
- Quantitative parameters at the procedure level (minimum boiling time at altitude, chlorine dose per litre for different turbidity levels, testing intervals)

Kiwix's library includes Wikivoyage, Wikipedia, and a few specific humanitarian archives, but no WASH-specific operational reference. The Humanitarian OpenStreetMap Team (HOT) covers infrastructure location, not procedure. Practical Action has ~8 water system technical briefs (CC BY), none in machine-readable form.

**Confidence**: High. The gap is verifiable by searching Kiwix's content library and Wikipedia's water treatment articles.

### Community Interest Signal

**Score: 3/3 — Strong signal**

Documented interest points:
- WASH practitioners (NGO field staff, government health workers, MSF field logistics): ~50,000 active globally; concentrated on ReliefWeb forums, OXFAM's humanitarian knowledge platform, and UNICEF WASH cluster mailing lists
- Wilderness first response and survival communities: /r/preppers (1.5M members), /r/Bushcraft (300K), /r/Survival (400K) — all have active discussions about water purification and regularly cite need for offline references
- Rural water system designers: smaller but highly motivated community via Rural Water supply Network (RWSN), the International Water and Sanitation Centre (IRC)
- Permaculture design community: rainwater harvesting is a core design element; multiple active Discord servers and YouTube channels

The 2021–2025 period of increasing interest in emergency preparedness (COVID supply chain disruptions, climate-linked flooding) has produced documented growth in survival preparedness communities. This is not speculative demand.

### Schema Complexity

**Score: 2/3 — Moderate complexity**

The `water_systems.schema.json` is already complete. The complexity concern is content validation:

- Most water treatment procedures can be verified against authoritative public sources (WHO, CDC, EPA) without requiring a licensed professional sign-off
- Exception: water quality testing protocols that lead to treatment decisions in medical contexts (e.g., "is this water safe for immunocompromised patients?") touch medical territory and need careful framing
- Construction procedures (filter building, cistern construction) are analogous to general engineering instructions — high accuracy is important but no professional licensing gate applies
- Mitigation: All procedures explicitly cite source (WHO guideline, CDC recommendation, etc.); no procedure presents open-repo as the authority

Review overhead: 1–2 maintainer hours per procedure for source verification. No external reviewer required for operational content.

### Recruitment Feasibility

**Score: 3/3 — High feasibility**

Concrete outreach targets with known online presence:
- r/preppers: active, post-friendly for resource sharing (1.5M members, mods allow resource posts in weekly megathread)
- r/Bushcraft: active water purification discussion; "offline reference" is a recurring interest
- ReliefWeb job/community board: reachable for WASH practitioners
- Practical Action community forums: small but highly relevant audience

Expected conversion rate from outreach post to contributor: 0.5–1% (industry benchmark for volunteer knowledge platforms). With 500 readers of an outreach post: 2–5 contributor inquiries, 1–3 actual submissions. This is the realistic Week 2–4 target.

---

## Domain 2 — Food Preservation

### Gap Analysis

**Score: 2/3 — Moderate gap**

The gap here is narrower than Water Systems but highly practical. The NCHFP (National Center for Home Food Preservation) is the authoritative US source; its content is produced by the USDA and is in the public domain (US government works, not subject to copyright). However:

- NCHFP content is web-only; no ZIM file exists
- Ball Blue Book is widely used but commercially licensed (not open-source compatible)
- Fermentation knowledge (lacto-fermentation, kimchi, sourdough, vinegar) is distributed across hundreds of blogs and YouTube channels; no structured, authoritative, offline reference exists
- Root cellaring, dehydration, and freeze-drying procedures exist in books but not in structured machine-readable form

Wikivoyage has basic food safety notes for travelers. Wikipedia's food preservation article is encyclopedic but not procedural. The Kiwix library has no food preservation archive.

**Confidence**: High for NCHFP content; moderate for fermentation (sources are distributed, quality varies).

### Community Interest Signal

**Score: 3/3 — Strong signal**

Documented community interest:
- /r/Canning: 250K members; recurring requests for offline reference materials
- /r/fermentation: 600K members; sophisticated community with high interest in accuracy and sourcing
- /r/homestead: 650K members; cross-domain overlap with water/seed content
- /r/preppers: already noted; food preservation is a core preparedness topic

The 2020–2024 homesteading boom is well-documented in market research; canning equipment sales increased 40–60% in 2020 and have remained elevated. This community actively seeks authoritative, offline-compatible reference material.

### Schema Complexity

**Score: 3/3 — Easy**

The `food_preservation.schema.json` maps cleanly to existing NCHFP procedure structure:
- Canning procedures have explicit processing times, temperatures, and altitude adjustments — these are tabular data that fit the schema fields directly
- Fermentation procedures are simpler (ratios, temperatures, times) — less standardized but no safety-critical processing parameters
- Dehydration: temperature and time are the key parameters; sourcing from NCHFP or Cooperative Extension publications provides authoritative values

Safety note: canning botulism risk is real and the NCHFP explicitly warns against modifying tested recipes. All Wave 0 canning content must be sourced directly from NCHFP or equivalent government extension publications, not adapted or modified. This is a content policy rule, not a schema constraint.

Review overhead: 30–60 minutes per procedure for source transcription and schema mapping. Lower than Water Systems because NCHFP provides the authoritative source directly.

### Recruitment Feasibility

**Score: 3/3 — High feasibility**

Outreach targets:
- /r/Canning: moderators are known to approve resource posts; community is experienced at sharing resources
- Cooperative Extension educators: county-level Cooperative Extension programs teach food preservation; some are reachable via university email directories
- Master Preservers certification network: NCHFP trains Master Preserver volunteers; this network is a natural contributor pool for content review
- YouTube homesteading community: channels with preservation focus (Homesteady, Deep South Homestead, etc.) have audiences who would share an offline resource post

---

## Domain 3 — Seed Preservation

### Gap Analysis

**Score: 2/3 — Moderate gap**

Seed Savers Exchange (SSE) has deep content but is a membership organization; much of its procedural content is not openly licensed. The Open Source Seed Initiative (OSSI) focuses on licensing (not procedures). iNaturalist covers identification. Wikipedia's seed-related articles are encyclopedic.

What is genuinely missing in structured offline form:
- Seed viability parameters (temperature, humidity, years to expected viability loss) by species — this exists in academic literature but not in accessible structured form
- Isolation distances for preventing cross-pollination (critical for seed purity) — scattered across extension publications
- Seed cleaning and processing techniques (wet vs. dry processing by species) — partially on YouTube, not in structured offline form
- Regional adaptation notes (variety selection for different climates) — almost entirely absent from structured sources

**Confidence**: Moderate. The gap is real but requires more curation effort per procedure than Water or Food Preservation, because no single authoritative source covers it comprehensively.

### Community Interest Signal

**Score: 2/3 — Moderate signal**

- Seed Savers Exchange community: active but smaller than food preservation (~300K seed library members estimated across network)
- Permaculture communities: seed saving is a core competency; overlap with water domain audience
- Community seed library network (Seed Libraries): ~400 community seed libraries in North America with varying online presence
- /r/vegetablegardening: 700K members but seed saving is a subset interest

The philosophical alignment between seed preservation culture (reciprocity, open sharing, anti-corporate agriculture) and open-repo's values is the strongest community signal. Practitioners in this space already believe in commons-based knowledge sharing.

### Schema Complexity

**Score: 2/3 — Moderate**

The `seed_preservation.schema.json` is complete but the content requires more domain expertise to validate than food preservation:
- Viability data varies by variety, storage method, and starting germination rate — simple tables, but sourcing requires cross-checking multiple extension publications
- Genetic isolation distances depend on species pollination mechanism (wind vs. insect) — requires botanical knowledge to verify
- Climate adaptation data is local — a procedure written for the Pacific Northwest may be wrong for the Southeast

Review overhead: 2–4 maintainer hours per procedure, or 30–60 minutes with an experienced seed saver reviewing. This is the domain most likely to benefit from an expert reviewer partnership (university extension programs, community seed library staff).

### Recruitment Feasibility

**Score: 2/3 — Moderate**

Outreach path:
- Community seed library network: libraries are identifiable via Seed Libraries directory; many have newsletters or social media presence
- Permaculture Research Institute and similar organizations: potentially willing to provide content or link
- /r/vegetablegardening and /r/Seeds: smaller but relevant

The challenge: seed saving practitioners who would contribute tend to be deeply embedded in local, in-person communities (seed swaps, farmers markets). Digital-first outreach reaches a subset. A partnership with a community seed library is the highest-leverage path.

---

## Domain 4 — Medical Reference

### Gap Analysis

**Score: 3/3 — Strong gap**

The gap in structured, offline, openly licensed practical medical reference is profound. MSF (Medecins Sans Frontieres) publishes the Clinical Guidelines (free to download); WHO publishes treatment protocols; ICRC publishes first aid manuals. None of these are in structured JSON-LD form; none are in a Kiwix ZIM archive as interlinked, searchable content.

However: the gap alone does not make this Wave 0 material.

### Why Medical Is Not Wave 0

**Schema complexity: 1/3 — Hard**

Medical content requires a medical accuracy reviewer before publication. This is not a discretionary quality gate — it is an ethical and legal minimum. Incorrect medication dosing or contraindication information can cause serious harm. The medical reviewer outreach (to Wilderness Medical Society, MSF, ICRC) is drafted but not yet sent.

**Community signal: 1/3 — Weak in Wave 0 context**

Medical practitioners who would contribute are not present on /r/preppers in contributor mode. The contributor pool requires targeted outreach to medical schools, wilderness medicine programs, and humanitarian medical organizations — a 4–8 week recruitment cycle before content can start.

**Recruitment feasibility: 1/3 — Low in Wave 0 timeframe**

Medical content contributors must have domain credentials. The pool is small and the onboarding is heavier (contributor must understand medical disclaimer requirements, citation standards, and the difference between clinical and austere-environment protocols).

**Recommendation**: Medical Reference remains Priority 0 pending reviewer recruitment. Send the outreach emails in Week 2 (see `medical-reviewer-outreach-draft.md`). Begin content development in Wave 1 (post-Week 12) once a reviewer relationship is established. This is not a gap that should be filled without proper review infrastructure.

---

## Domain 5 — Botanical Knowledge

### Gap Analysis

**Score: 1/3 — Weak gap**

iNaturalist covers species identification with community-verified photos. Wikipedia's botanical articles are substantive. Plants for a Future (PFAF) database covers medicinal and edible properties for ~7,000 species. Kiwix already has Wikipedia offline.

The genuine gap is at the intersection: operational procedures that combine plant identification with specific use instructions (foraging, medicinal preparation, cultivation). This is narrower than the domain implies — it is not "plant knowledge" in general but specifically "what do I do with this plant, step by step, in a resource-constrained context."

This sub-gap is real but better served as a Phase 6 domain, once the federation layer enables open-repo to link its procedural content to iNaturalist observations and Wikipedia taxon pages via Wikidata QIDs. In Wave 0, the value added by open-repo over existing sources is smaller.

**Recommendation**: Standby for Wave 1. The Botanical Knowledge schema is published and ready; begin content development when the federation layer can surface the cross-linking value.

---

## Summary

| Domain | Wave 0 Priority | Recommended Start | First content gate |
|---|---|---|---|
| Water Systems | Priority 1 | Week 1 | 3 procedures by Day 5 |
| Food Preservation | Priority 2 | Week 3 | 3 procedures by Week 3 end |
| Seed Preservation | Priority 3 (community) | Week 6 | Domain index + 1 procedure |
| Medical Reference | Standby | Week 12+ | After reviewer sign-off |
| Botanical Knowledge | Wave 1 | Post-Week 12 | After federation layer |

---

## Sources

- [NCHFP: National Center for Home Food Preservation](https://nchfp.uga.edu/)
- [WHO Emergency Water Supply Guidelines](https://www.who.int/publications/i/item/WHO-SDE-WSH-02.09)
- [Practical Action Technical Briefs (CC BY)](https://practicalaction.org/knowledge-centre/technical-briefs/)
- [Seed Libraries directory](https://libraryseednetwork.org/)
- [Kiwix content library](https://library.kiwix.org/)
- [Seed preservation conservation challenges (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8623176/)
- [Crop wild relatives knowledge gaps (Frontiers)](https://www.frontiersin.org/journals/sustainability/articles/10.3389/frsus.2025.1453170/full)

*Prepared 2026-06-28.*
