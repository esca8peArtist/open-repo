---
title: "Phase 2 Implementation Roadmap: 6–12 Month Execution Plan"
date: 2026-06-17
status: research-complete
phase: Phase 2 planning
confidence: 80%
sources-consulted: 8 (synthesis of prior three documents)
tags: [seedwarden, phase-2, roadmap, milestones, implementation, botanical-platform]
---

# Phase 2 Implementation Roadmap: 6–12 Month Execution Plan

**Lead finding**: Phase 2 splits into two parallel tracks that should not be sequenced — Track A (content production and automation pipeline) and Track B (market validation and commercial partnerships). The most common failure mode for botanical knowledge platforms is investing 6–12 months building infrastructure before validating that any audience will pay for it. The roadmap below front-loads market validation (B2B conversations, affiliate pilot) within the first 6 weeks, in parallel with infrastructure build.

---

## Assumptions and Constraints

- Team: 1 primary content/product owner + optional 1 developer (part-time)
- Budget: Phase 2 infrastructure costs are low ($50–200/month at scale) but development time is the primary constraint
- Existing assets: Seedwarden already has Etsy product presence, supplier relationships, audience (Phase 1–3 buyers), and content production experience
- The "botanical knowledge platform" described in this roadmap is an expansion layer on top of the existing Etsy/product business — not a replacement

---

## Phase 2 Milestone Overview

| Month | Track A (Technical) | Track B (Commercial) |
|---|---|---|
| 1 | Airtable schema + first 50 species loaded | B2B outreach to 5 native plant nurseries (content licensing pilot) |
| 2 | iNaturalist + USDA PLANTS ingestion pipeline | Affiliate link integration in Etsy listings and any existing web presence |
| 3 | Wikidata taxonomy sync; image pipeline | First B2B licensing contract target; evaluate freemium landing page |
| 4 | USA-NPN phenology sync; contributor form | Partnership outreach: Native Plant Trust, bplant.org, Prairie Moon |
| 5 | Public-facing web frontend (Astro/GitBook) live | Phenology newsletter pilot (email to existing buyers) |
| 6 | 200+ species records live; Darwin Core export | Review conversion data; decide on subscription model launch |
| 7–9 | Scale to 500 species (second bioregion) | Launch premium subscription ($8–12/month) |
| 10–12 | API endpoint for B2B/garden software licensing | Grant applications (SARE, NFWF, state SWAP programs) |

---

## Month 1: Foundation

### Track A — Technical Foundation

**Week 1–2: Airtable schema**

Set up Airtable base with the field schema defined in the Platform Comparison document:
- Core identification fields (scientific name, USDA symbol, Wikidata QID, synonyms)
- Distribution fields (ecoregion codes, state presence, native/introduced status)
- Ecological and phenological fields
- Use and propagation fields
- Media fields (image + license metadata)
- Workflow fields (review status, reviewer, last updated)

**Week 2–3: Wikidata crosswalk**

Select 50 target species for the pilot bioregion (recommendation: Northeast US — strongest existing Seedwarden audience based on Phase 2 product analysis showing Survival Garden Regional Plans as top seller). Run Wikidata SPARQL queries to build the crosswalk table (USDA symbol, iNaturalist taxon ID, GBIF ID, common names) for all 50 species.

**Week 3–4: Initial load**

Download USDA PLANTS bulk CSV for Northeast states. Process with Python script to extract metadata for the 50 target species. Load into Airtable. Result: 50 structurally complete species records with all field values sourced from authoritative data.

**Milestone**: 50 species records in Airtable with complete taxonomy, distribution, and growing condition fields. Crosswalk table complete. No frontend yet.

### Track B — Commercial Validation

**Week 1: B2B outreach**

Identify 5 regional native plant nurseries in the Northeast that have thin species content on their websites. Candidates: New England Wild Flower Society shop (Native Plant Trust), Nasami Farm, Pinelands Nursery, Shooting Star Nursery, Clearwater Farm. Draft a one-page content licensing pitch: "Embed Seedwarden's species profiles in your plant catalog pages. $300/year for up to 100 profiles. Includes phenology data, propagation notes, and ecosystem service ratings."

**Target**: 2 responses, 1 interest conversation.

**Week 2–4: Affiliate link integration**

Add affiliate links to existing Etsy product listings and any social media content: Prairie Moon Nursery affiliate program, Native Plant Trust shop affiliate program, Ernst Conservation Seeds. Affiliate commission typically 5–15%. This is zero-cost to implement and generates immediate signal about which species drive purchase intent.

---

## Month 2: Data Pipeline

### Track A

**iNaturalist ingestion pipeline**: Write Python script using `pyinaturalist` to fetch Research Grade observations for all 50 target species in the Northeast bioregion. Extract: representative CC-licensed photos, recent observation counts (phenology proxy), range confirmation data. Store photos in Cloudflare R2. Update Airtable image fields with photo URL + license metadata.

**USDA PLANTS enrichment**: Use Flora API (Developer tier, $19/month) to fetch county-level distribution data and ethnobotany fields for the 50 species. Update Airtable records.

**Automation trigger**: Set up n8n workflow — when a new species record is created in Airtable with status "Data Loaded", trigger the iNaturalist photo fetch automatically. This removes the manual image-sourcing step from the content production workflow.

**Milestone**: 50 species records fully enriched with images, county-level distribution, and uses data. Automated image pipeline operational.

### Track B

**Affiliate pilot analysis**: After 30 days, review affiliate click-through data. Which species/guides drive the most outbound clicks to nurseries? This reveals audience purchase intent and informs which species to prioritize for detailed propagation content.

**B2B follow-up**: Follow up with nurseries contacted in Month 1. If no interest from cold outreach, pivot to a warmer approach: propose a free content pilot (provide 10 species profiles at no cost for 60 days, then present a paid offer based on their usage data).

---

## Month 3: Taxonomy Sync and Image Automation

### Track A

**Wikidata weekly sync**: Build n8n scheduled workflow — every Sunday, query Wikidata for the Seedwarden species list. Compare accepted names against Airtable records. Flag any discrepancies (taxonomy change detected) in an Airtable "Needs Review" view for the botanical reviewer.

**Image quality workflow**: For each species, rank available images by quality (resolution, composition, license type). Automate selection of top image as primary photo. Flag species with no CC-licensed images for manual sourcing.

**TNRS integration**: Add a lookup step in the contributor submission form: when a user submits a species name, auto-query TNRS to validate the name and return the accepted synonym. Reduces expert review load.

**Milestone**: Taxonomy sync running weekly. Image pipeline automated. Contributor submission form live (even if not yet publicly promoted).

### Track B

**First B2B contract target**: Close first nursery content licensing deal (even at reduced or trial pricing). This is the most important commercial signal of Month 3. If no nursery interest after 3 months of outreach, pivot to direct-consumer subscription as the primary revenue hypothesis.

**Landing page for botanical knowledge platform**: Even before the full frontend is built, create a waitlist landing page: "Seedwarden is building the most detailed bioregional native plant guide in the Northeast. Join the waitlist for early access." Measure email signups from existing audience and any new traffic.

---

## Month 4: Phenology Integration and Contributor System

### Track A

**USA-NPN phenology sync**: Build weekly API call to USA-NPN Individual Phenometrics endpoint for the 50 target species and Northeast region. Parse results and update Airtable `npn_current_status` field. Test that the formula field correctly displays "In bloom", "Past peak", or "Not yet" based on current week.

**Contributor submission workflow**: Promote the Airtable-based contributor form to the existing Seedwarden audience (email list, Etsy buyers). Define the incentive: contributors who submit verified observations with photos receive a free species profile PDF download. Design the expert review queue view in Airtable (Kanban: Submitted → Under Review → Verified / Rejected with notes).

**Milestone**: Phenology sync operational. First contributor submissions received and reviewed.

### Track B

**Partnership outreach — native plant organizations**:
- Native Plant Trust: propose a content cross-linking partnership (Seedwarden propagation data cross-links to Go Botany identification data)
- bplant.org: propose ecoregion data sharing (Seedwarden uses bplant.org range map methodology; bplant.org links to Seedwarden propagation guides)
- Homegrown National Park: propose placement in their native plant databases directory

These are zero-cost partnerships that increase platform authority and traffic, not commercial deals.

---

## Month 5: Public Frontend Launch

### Track A

**Web frontend live**: Launch public-facing plant guide website using Astro (recommended) or GitBook pulling from Airtable via API. Initial feature set:
- Species profile pages: all fields visible, photos with attribution
- Regional filter: browse by Northeast US state or EPA Level III ecoregion
- "What's in bloom now" widget: powered by USA-NPN sync
- Search by common name, scientific name, or USDA symbol

**SEO infrastructure**: Each species page has a unique URL (slug = USDA symbol), proper meta title/description, structured data (schema.org/Plant markup where applicable), and alt text on all images with proper attribution.

**Milestone**: Public site live with 50+ indexed plant profiles. Site indexed by Google.

### Track B

**Phenology newsletter pilot**: Send first "What's happening in Northeast forests this week" email to existing Seedwarden buyers. Include 3–5 species currently in bloom, links to their profile pages, and a "growing tip of the week." Measure open rate, click-through, and replies.

**Hypothesis to test**: Does the existing Seedwarden audience (primarily product-purchase focused) engage with pure knowledge content? If open rates are above 30% and click-throughs are above 5%, the content-first audience exists within the existing list.

---

## Month 6: Evaluation and Scale Decision

### Track A

**100 species milestone**: Expand from 50 to 100 species, adding the highest-traffic species from iNaturalist observation data in the Northeast. Use the automated pipeline — new species should take under 30 minutes to add to Airtable (schema + crosswalk + data load + image).

**Darwin Core export**: Add export functionality so the Seedwarden database can be submitted to GBIF as a registered data publisher. This builds institutional credibility and increases backlinks to the platform.

### Track B

**Conversion assessment checkpoint**:
- Affiliate revenue from nursery referrals: Is it generating $50+/month? (If yes, scale with more species and more nursery partners)
- B2B licensing: Has at least 1 nursery paid for content licensing? (If yes, pursue 5 more)
- Waitlist/newsletter signups: Are there 500+ engaged subscribers? (If yes, proceed to freemium subscription launch)
- Phenology newsletter engagement: Open rate above 30%? (Required for subscription launch)

**Decision point**: Based on Month 6 data, choose primary revenue path:
- Path A: B2B licensing first (if nursery deals are closing)
- Path B: Consumer subscription first (if newsletter engagement is strong)
- Path C: Continue affiliate-only + free platform (if demand validation is inconclusive — de-risk by building more species before monetizing)

---

## Months 7–9: Scale to Second Bioregion

**Target second bioregion**: Pacific Northwest (WA/OR) — second-largest gap identified in market analysis, strong conservation culture, proximity to existing ecological restoration market.

**Repeat pipeline**: Wikidata crosswalk → USDA PLANTS load → iNaturalist enrichment → image pipeline → USA-NPN sync → public profiles. With the pipeline built in Months 1–4, the second bioregion should take 4–6 weeks to reach 50 species vs. the 8 weeks the first bioregion took.

**If premium subscription is launched (Month 7)**:
- Initial offering: $8/month or $72/year
- Premium features: full propagation guides, phenology email alerts, offline PDF generation, ad-free browsing
- Target: 100 paying subscribers by Month 9 = $800–900/month incremental revenue

---

## Months 10–12: API and Grant Track

**B2B API endpoint**: If garden design software partnership conversations have progressed (initiated in Month 3–6 outreach), build a documented REST API for native plant metadata. Pricing model: $200–800/year for small platforms, $2,000–8,000/year for mid-size platforms.

**Grant applications**:
- SARE (Sustainable Agriculture Research & Education): Letter of intent for Northeast native plant database project. SARE has funded directly comparable projects.
- NFWF Monarch Butterfly and Pollinator Conservation Fund: Pollinator plant profiles are a fundable deliverable.
- State-level: Several northeastern states (NY, MA, PA) have state wildlife agency grant programs for plant conservation education resources.

**12-month target state**:
- 500+ species profiles across 2 bioregions (Northeast + PNW)
- Automated pipeline running with <30 min/week maintenance
- 1–3 B2B content licensing contracts ($300–900/month)
- 100–300 premium subscribers ($800–2,700/month)
- Affiliate revenue ($100–400/month)
- Grant application(s) submitted
- Total monthly revenue from knowledge platform: **$1,200–4,000/month** (in addition to existing Etsy product revenue)

---

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Flora API pricing changes or shuts down | Low-Medium | Medium — switch to direct USDA PLANTS CSV + R package (plantr) | Use bulk CSV as primary, Flora API for incremental only |
| iNaturalist changes API rate limits | Low | Medium — use monthly bulk export as primary data source | Already recommended above |
| No nursery B2B interest in content licensing | Medium | High — pivot to consumer subscription only | Validate in Month 1–3 before committing |
| Taxonomy changes break cross-references | Medium | Low-Medium — automated via Wikidata sync flags these | Weekly sync + expert review queue |
| Audience doesn't convert from free to paid | Medium | High — re-evaluate product value proposition | Run 90-day free trial of premium features before paywalling |
| Developer time bottleneck | High (solo dev) | Medium — use no-code/low-code tools (Airtable, n8n, Astro) | Deliberately chose low-code stack to minimize dev dependency |

---

## Key Decisions Not Made in This Document

The following decisions require Seedwarden stakeholder input before this roadmap can be fully executed:

1. **Target bioregion for Phase 2 launch**: This document recommends Northeast US based on existing Seedwarden audience signals (per PHASE2_PRODUCT_PRIORITIES.md). Confirm or override.
2. **Build vs. buy for frontend**: Astro (requires developer) vs. GitBook (no-code). Choose based on available development resources.
3. **Subscription pricing**: $8/month vs. $10/month vs. annual-only. Requires A/B test or comparable platform analysis before launch.
4. **Content licensing price point**: $300/year vs. $500/year vs. usage-based. Validate with first B2B conversations.
5. **Solo content production vs. hiring botanical writers**: The 500-species target requires roughly 400+ plant profile writeups (the 100 initial records use automated data; rich propagation/identification content requires writing). Budget for freelance botanical writers or accept slower scale.

---

## Sources (Synthesis Documents)

All source citations are contained in the three preceding research documents:
- [PHASE_2_CONTENT_SCALING_PLATFORM_COMPARISON.md](./PHASE_2_CONTENT_SCALING_PLATFORM_COMPARISON.md)
- [PHASE_2_AUTOMATION_ARCHITECTURE_BLUEPRINT.md](./PHASE_2_AUTOMATION_ARCHITECTURE_BLUEPRINT.md)
- [PHASE_2_MARKET_OPPORTUNITY_ASSESSMENT.md](./PHASE_2_MARKET_OPPORTUNITY_ASSESSMENT.md)

Additional synthesis references:
- [Airtable Automations — multi-step workflows](https://automationswitch.com/tool-comparisons/airtable-vs-notion-automation-platform)
- [n8n workflow automation — Airtable + HTTP integrations](https://n8n.io/integrations/airtable/and/notion/)
- [Automate WordPress Publishing with Airtable and n8n](https://kjetilfuras.com/automate-wordpress-blog-publishing/)
- [Calflora — 1.4M users/year, 8,500+ species, free nonprofit model](https://www.calflora.org/case-statement.html)
