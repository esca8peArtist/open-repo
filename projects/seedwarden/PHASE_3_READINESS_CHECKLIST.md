---
title: "Phase 3 Readiness Checklist — Pre-Production by Option"
date: 2026-04-30
status: production-ready
context: Phase 3 prep, awaiting Phase 1 week-6 data trigger
references: phase-3-decision-framework.md, phase-3-product-specifications.json, PHASE3_ROADMAP_INDEX.md, phase-3-product-expansion-roadmap.md
---

# Phase 3 Readiness Checklist
## Pre-Production Verification for Options A, B, C, and D

**Purpose**: When Phase 1 data arrives at Week 6 (approximately June 15, 2026) and the Phase 3 decision is made using phase-3-decision-framework.md, the production team needs to move immediately. This checklist ensures nothing is missing at the moment of execution. Each option section below is a standalone checklist — consult only the section that matches the selected option.

**How to use**: On June 15–July 1, complete the 30-minute decision process in phase-3-decision-framework.md first. Once Option A, B, C, or D is selected, turn to that option's section here and verify every line. Items marked [USER ACTION] require human action before production can begin. Items marked [VERIFY] require reviewing an existing document or asset. Items marked [BUILD] are creation tasks that can begin immediately after the option is selected.

---

## Universal Pre-Launch Checks (All Options)

Complete these regardless of which option is selected. They are prerequisites for all Phase 3 execution.

### Etsy Account Status
- [ ] [USER ACTION] Phase 1 Etsy account fully verified and active (no pending verification blocks)
- [ ] [USER ACTION] Etsy Star Seller eligibility check: if Phase 1 has 10+ sales and 5-star reviews at Week 6, initiate the Star Seller status process — it affects listing visibility in Phase 3
- [ ] [VERIFY] Phase 1 listings are all live with 5-image slots filled (including slot 4 lifestyle photo) before Phase 3 listings go live
- [ ] [VERIFY] Etsy shop policies are current and include a digital download delivery statement

### Analytics and Data Availability
- [ ] [USER ACTION] Google Analytics integration active for the Etsy shop (google-analytics-integration-guide.md has the setup instructions)
- [ ] [USER ACTION] Pull Phase 1 data from Etsy Stats: total views, conversion rate, top-performing listings, geographic distribution
- [ ] [VERIFY] customer-analytics.csv is populated with Phase 1 transaction data
- [ ] [USER ACTION] Identify which of the four cohorts (forager, homesteader, prepper, gift buyer) accounts for the largest share of Phase 1 transactions — this is the input to the Phase 3 option selection

### Email Platform Status
- [ ] [VERIFY] Kit (ConvertKit) account is active and the Zone Quick-Start Card welcome sequences are live
- [ ] [VERIFY] Email list has at least 50 subscribers before Phase 3 product launch emails go out
- [ ] [BUILD] Pre-write Phase 3 announcement email (one paragraph: "Here's what we're adding to the catalog") — can be drafted now and sent on July 1 regardless of option

### Content Assets Confirmed Available
- [ ] [VERIFY] All 18 wild edibles habit photos are in `/projects/seedwarden/assets/wild-edibles/` (18 files confirmed as of Phase 2)
- [ ] [VERIFY] All 21 Phase 1 PDFs are in `/projects/seedwarden/scripts/output/` and remain under 5 MB
- [ ] [VERIFY] Phase 3 product specifications for all 12 products are in `phase-3-product-specifications.json`
- [ ] [VERIFY] Cohort messaging for each of the 4 cohorts is in `phase-3-cohort-messaging.md`

---

## Option A — Conservative: Regional Listings Only

**Trigger condition**: Phase 1 achieves fewer than 20 total sales by June 15 OR conversion rate is below 0.75% across all listings.

**Scope**: No new content. Create 14 regional variant listings only (7 Survival Garden + 7 Native Plants), plus update the existing Zone Quick-Start Card lead magnet for regional promotion.

**Development commitment**: 19 hours total (listed in phase-3-product-expansion-roadmap.md Section 4). Out-of-pocket cost: $0.

### Option A Content Checks

- [ ] [VERIFY] Survival Garden Regional Plans product file (`scripts/output/survival-garden-regional-plans.pdf`) contains distinct regional content (not generic) — open and confirm at least 5 unique regional sections
- [ ] [VERIFY] Native Plants Regional Guide (`scripts/output/native-plants-regional-guide.pdf`) is segmented by US region — open the table of contents and confirm regional organization
- [ ] [BUILD] Draft 7 Survival Garden regional listing titles (format: "[Region] Survival Garden Plan — Heirloom Varieties, Planting Calendar, Food Storage | PDF Download")
  - Northeast Survival Garden Plan
  - Southeast Survival Garden Plan
  - Midwest Survival Garden Plan
  - Southwest Survival Garden Plan
  - Pacific Northwest Survival Garden Plan
  - Mountain/Rocky Mountain Survival Garden Plan
  - Gulf Coast and Lower South Survival Garden Plan
- [ ] [BUILD] Draft 7 Native Plants regional listing titles (format: "Native Plants of the [Region] — Identification, Habitat, and Edibility Guide | PDF Download")
- [ ] [BUILD] Confirm regional slugs for file naming: `survival-garden-northeast.pdf`, `native-plants-pacific-northwest.pdf`, etc.

### Option A Etsy Listing Template

Each regional listing requires:
- [ ] [BUILD] Title (use format above, confirm under 140 characters)
- [ ] [BUILD] Description (adapt from the parent product description in etsy-store-copy.md — 200 words minimum, region-specific in paragraph 1)
- [ ] [BUILD] Tags (13 tags: regional keyword + "survival garden" + "native plants" + 3 zone-specific tags)
- [ ] [BUILD] Price: Survival Garden regional listing = $5.99; Native Plants regional listing = $12
- [ ] [BUILD] Mockup: Use the parent product mockup image for all regional listings initially — do not delay launch for unique regional mockups

### Option A Launch Timeline

| Task | Owner | Hours | Launch Date |
|---|---|---|---|
| 7 Survival Garden regional listing creation | User | 8 hours | July 1 |
| 7 Native Plants regional listing creation | User | 11 hours | July 14 |
| Total | | 19 hours | July 14 complete |

### Option A Success Check (Week 8 Review)
- If regional listings generate at least 5 combined sales by August 1, proceed to Option B wave 1 products
- If regional listings generate 0–4 sales by August 1, hold Phase 3 and focus on Phase 1 listing optimization (update titles, tags, and photos before adding new listings)

---

## Option B — Standard: Full Phase 3 Roadmap

**Trigger condition**: Phase 1 achieves 20–60 total sales by June 15 AND conversion rate is between 0.75% and 2.5%.

**Scope**: Complete 3-wave expansion across all 12 Phase 3 products plus 14 regional variants plus 3 bundles. Development commitment: approximately 50 hours for Wave 1 (July), 70 hours for Wave 2 (September–October). Out-of-pocket cost: approximately $370–440 as documented in phase-3-product-development-strategy.md.

### Option B Wave 1 Checks (July Launches)

**Wild Edibles Quick Reference ($10)**
- [ ] [VERIFY] 18 habit photos in `/projects/seedwarden/assets/wild-edibles/` — list filenames to confirm all 18 present
- [ ] [VERIFY] CC BY-SA license attributions for all 18 photos documented in WORKLOG.md
- [ ] [BUILD] Design brief: 22–25 pages, one species per page, portrait format. Page template: top third = habit photo, middle = identification features (3–5 bullet points), bottom = harvest season / edible parts / preparation. No scientific diagrams needed — photos carry identification load.
- [ ] [BUILD] Confirm all 18 species are from the wild edibles habit photo archive (if any gap, note here and substitute with descriptive text for that species)
- [ ] [BUILD] Canva document started: US Letter, 300 DPI, Seedwarden brand colors from Brand Kit

**Beginner Canning Quick-Start Guide ($9)**
- [ ] [VERIFY] Source content: Fermented and Preserved Harvest Handbook PDF contains canning content — open and identify the 10–15 pages of water-bath canning content that form the core of this derivative guide
- [ ] [BUILD] Outline: Introduction (1 page), Equipment list (1 page), Safety and pH primer (1 page), 5 beginner-friendly recipes with step-by-step instructions (5 pages), Troubleshooting (1 page), Resource page (cross-links to full Handbook)
- [ ] [BUILD] Total target: 12–15 pages

**Fermentation Starter Kit Guide ($8)**
- [ ] [VERIFY] Source content: Fermented and Preserved Harvest Handbook contains fermentation content — identify the lacto-fermentation section as the primary source material
- [ ] [BUILD] Outline: What is lacto-fermentation (1 page), Equipment list (1 page), Brine ratio reference table (1 page), 4 beginner recipes: sauerkraut, dill pickles, kimchi-style, hot sauce (4 pages), Troubleshooting (1 page)
- [ ] [BUILD] Total target: 10–12 pages

**Dehydrating and Drying Field Guide ($11)**
- [ ] [VERIFY] Harvest Preservation Field Manual contains dehydrating content — identify and mark those pages
- [ ] [BUILD] Outline: Equipment overview (1 page), Temperature and time reference chart (1 page), Vegetables section (2 pages), Herbs section (1 page), Fruits section (1 page), Meat jerky basics (1 page), Storage and shelf life (1 page)

**14 Regional Variant Listings**
- [ ] [BUILD] Same as Option A regional listing work — all 14 regional variants
- [ ] 19 hours for listing creation

### Option B Wave 2 Checks (September–October Launches)

**Native Plants Identification Flashcard Set ($12)**
- [ ] [VERIFY] Native Plants Regional Guide PDF contains species entries with botanical details — confirm total species count (should be 40+)
- [ ] [BUILD] Design brief: 3x5 inch card format, 300 DPI, PDF download. Front of card: species common name, one botanical illustration or habit photo. Back: identification features, habitat, edibility note, one lookalike warning.
- [ ] [BUILD] Image sourcing plan: Wikimedia Commons CC-licensed botanical illustrations for 40+ species — search protocol is already established from wild edibles habit photo work
- [ ] [VERIFY] Canva can export multiple-page PDFs at 3x5 inch dimensions — test this in the Zone Card template before committing to Canva for flashcard production

**Seed Library Setup and Organization System ($14)**
- [ ] [VERIFY] Seed Saving Field Manual PDF contains reference to seed library organization concepts — confirm the content exists to derive from
- [ ] [BUILD] 10 printable templates needed: seed envelope label, germination tracking log, viability chart, trade and swap record, storage conditions reference, library catalog card (front), library catalog card (back), annual inventory sheet, seed source log, variety notes page
- [ ] [BUILD] Each template is one page — total deliverable is a 10-page printable PDF at 8.5x11 inches

**Homestead Skills Assessment and Roadmap ($10)**
- [ ] [BUILD] Self-assessment section: 100 skills across 8 categories (food growing, preservation, seed saving, foraging, animal husbandry, construction/tools, first aid/medicine, community/trade)
- [ ] [BUILD] Each skill entry: skill name, difficulty level (beginner/intermediate/advanced), Seedwarden product cross-reference where applicable
- [ ] [BUILD] 12-month learning pathway: a suggested sequence for building skills in a logical order

### Option B Designer Brief Status

- [ ] [VERIFY] CANVA_EXECUTION_PLAYBOOK.md has template guidance for all Phase 3 design formats
- [ ] [BUILD] Zone Quick-Start Card Canva template exists and can be adapted for Phase 3 product formats (confirmed from ZONE_QUICKSTART_CARD_SPEC.md)

---

## Option C — Aggressive: Compressed 12-Week Execution

**Trigger condition**: Phase 1 achieves 60+ total sales by June 15 OR monthly revenue is above $800 in Month 2.

**Scope**: Full Option B scope, compressed into 12 weeks (July 1 – September 30) rather than the standard 16-week window. This requires 10+ development hours per week rather than the standard 7. Every item from Option B applies, plus the acceleration checks below.

### Option C Acceleration Checks

- [ ] [USER ACTION] Confirm 10 hours per week of Phase 3 development time is available for the July–September window. If not available at that rate, revert to Option B and do not execute Option C.
- [ ] [BUILD] Priority ranking: build in launch order from phase-3-product-specifications.json — specifically, which 3 products launch in Week 1 of July, which 3 in Week 2. Do not batch them all to the same day.
- [ ] [BUILD] Canva production queue: list all 12 products in production order and assign estimated hours each. Wild Edibles Quick Reference and Flashcard Set are the most design-intensive — do not leave them for last.
- [ ] [USER ACTION] If design-intensive products (Flashcard Set, Zone Card variants) will take more than 14 hours each, determine whether a designer will be hired for those specific products. Budget: $150–250 for 2–3 products via Fiverr or local designer.
- [ ] [BUILD] Pinterest pin campaign: for Option C, add Pinterest promoted pins for the top 3 launch products. Budget: $25 per product per month (total $75/month). Pre-write pin descriptions and budget allocation plan.

### Option C Launch Calendar Template

| Week | Products Launching | Hours Required |
|---|---|---|
| Week 1 (July 1–7) | 7 Survival Garden regional listings | 8 |
| Week 2 (July 8–14) | 7 Native Plants regional listings + Wild Edibles Quick Reference | 15 |
| Week 3 (July 15–21) | Beginner Canning + Fermentation Starter Kit | 10 |
| Week 4 (July 22–31) | Dehydrating Guide + Preservation Season Starter Bundle | 12 |
| Week 5 (Aug 1–7) | Pressure Canning Meat Guide + Master Preserver Bundle | 10 |
| Week 6–8 (Aug) | Seed Library System + Flashcard Set | 18 |
| Week 9–10 (Sept) | Homestead Skills Roadmap + First-Year Preservation Planner | 14 |
| Week 11–12 (Sept) | Medicinal Herb Guide + Homesteader's Complete Reference Set | 16 |
| **Total** | **All 12 products + 14 regional + 3 bundles** | **~103 hours** |

If this pace is unsustainable at any point, Option C converts to Option B mid-execution without losing work. All products built remain on Etsy.

---

## Option D — Focused: One-Cohort Concentration

**Trigger condition**: One cohort accounts for 50%+ of Phase 1 transactions, regardless of total sales volume.

**Scope**: Develop only the 4–6 products most relevant to the dominant cohort. Defer all other Phase 3 products until the dominant cohort's product set is complete and converting. This is the highest ROI-per-hour option when one cohort is clearly dominant.

### Identifying the Dominant Cohort

Use Phase 1 purchase patterns to classify buyers using customer-cohort-analysis-framework.md signals:

| Signal | Cohort |
|---|---|
| Bought: Wild Edibles, Native Plants, Foraging-adjacent guides | High-Intent Forager |
| Bought: Seed Saving, Zone Calendar, Companion Planting, Heirloom Guide | Homesteader |
| Bought: Survival Garden, Hunting Manual, Livestock, Meat/Fish Preservation | Survival Prepper |
| Purchased around holidays, Mother's Day, graduation, or as a one-time single-item buy | Gift Buyer |

If one cohort is above 50%, select the product track below.

### Option D: Forager Cohort Dominant

Products to build immediately (in order):

1. **Wild Edibles Quick Reference** ($10) — Weeks 1–2 of July
   - Same spec as Option B above
   - Launch date: July 1 (first product in the store directly serving forager visual needs)

2. **7 Native Plants Regional Listings** ($12 each) — Week 2–3 of July
   - Region-specific keyword capture for the cohort already buying the national guide
   - Templates needed: [VERIFY] that the Native Plants PDF has content for each of the 7 regions

3. **Native Plants Identification Flashcard Set** ($12) — August
   - Visual, portable, exactly what the forager cohort wants as a companion to the text-heavy guide
   - [BUILD] Design brief as specified in Option B above

4. **Wild Edibles Photo Pack** ($14) — August
   - Zero new development time: ZIP the 18 habit photos with attribution files
   - [VERIFY] All 18 CC-licensed photos have written attribution files in the assets directory
   - [BUILD] Create a single-page PDF cover for the download and a 2-paragraph Etsy description

5. **Regional Forager Bundle** ($28) — September
   - Bundle: Wild Edibles Quick Reference + Native Plants Regional Guide (one region of buyer's choice) + Flashcard Set
   - [BUILD] Bundle listing copy using forager cohort messaging from phase-3-cohort-messaging.md

6. **Medicinal Herb Growing and Harvest Guide** ($14) — October (if Forager cohort still dominant at Month 5)

### Option D: Homesteader Cohort Dominant

Products to build immediately (in order):

1. **7 Survival Garden Regional Listings** ($5.99 each) — Week 1 of July
2. **Beginner Canning Quick-Start Guide** ($9) — Week 2 of July
3. **Fermentation Starter Kit Guide** ($8) — Week 3 of July
4. **Dehydrating and Drying Field Guide** ($11) — Week 4 of July
5. **Preservation Season Starter Bundle** ($22) — August 1
6. **Seed Library Setup and Organization System** ($14) — September
7. **Homestead Skills Assessment and Roadmap** ($10) — October

### Option D: Survival Prepper Cohort Dominant

Products to build immediately (in order):

1. **7 Survival Garden Regional Listings** ($5.99 each) — July 1
2. **Pressure Canning Meat and Poultry Guide** ($13) — July 15
3. **Dehydrating and Drying Field Guide** ($11) — July 22
4. **Master Preserver Bundle** ($52) — August 1 (the prepper high-value bundle — confirm spec in phase-3-product-specifications.json)
5. **Homestead Skills Assessment and Roadmap** ($10) — September

For the prepper cohort, bundle framing is the primary conversion lever. The Master Preserver Bundle at $52 (individual total ~$75) should be the anchor promotion through August–September.

### Option D: Gift Buyer Cohort Dominant

Gift buyer dominance is rare (expected 15–20% share maximum) but if it occurs, Phase 3 focuses on gift-ready bundles and presentation:

1. **Holiday Gift Bundle** listing — repackage existing Apartment Grower Bundle or Food Sovereignty Bundle with gift-specific title and description (no new content)
2. **Gift card option**: Add a Seedwarden gift card listing on Etsy (Etsy native feature, takes 30 minutes to set up)
3. **Homesteader's Complete Reference Set** ($62) — the premium bundle as the anchor gift item
4. Content focus: Instagram and Pinterest content with gift framing, starting in October for the holiday window

---

## Final Pre-Launch Checklist (All Options, Day Before Each Launch)

Before any new Phase 3 listing goes live:

- [ ] PDF file is in `/projects/seedwarden/scripts/output/` and confirmed under 5 MB
- [ ] Etsy listing has a title under 140 characters with primary keyword in first 40 characters
- [ ] Etsy listing has exactly 13 tags
- [ ] Etsy listing has at least one mockup image (slot 1 minimum; slot 2 and 3 are better)
- [ ] Etsy listing price matches phase-3-product-specifications.json
- [ ] The new product is cross-referenced in at least one existing listing's description (the most relevant Phase 1 product links to the new Phase 3 product)
- [ ] WORKLOG.md is updated with: product name, Etsy listing URL, launch date, option (A/B/C/D)
- [ ] Phase 3 announcement email or social post is scheduled for the same day

---

## Production Time Summary

| Option | Total Dev Hours | Out-of-Pocket Cost | Target Completion |
|---|---|---|---|
| A | 19 hours | $0 | July 14 |
| B | ~120 hours | $370–440 | October 31 |
| C | ~103 hours | $370–440 + $75/mo Pinterest | September 30 |
| D (Forager) | ~60 hours | $0–50 | September 30 |
| D (Homesteader) | ~55 hours | $0 | October 15 |
| D (Prepper) | ~35 hours | $0 | August 31 |
| D (Gift) | ~8 hours | $0 | October 1 |
