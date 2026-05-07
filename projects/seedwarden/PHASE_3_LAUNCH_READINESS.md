---
title: "Phase 3 Product-Launch Readiness Checklist — Medicinal Herbs"
date: 2026-05-07
status: production-ready
phase: Phase 3 implementation
purpose: All user actions required before Phase 3 medicinal herbs launch (July 2026). Kit automation, zone card content, photography specs, Canva Brand Kit, Etsy category setup, analytics dashboard.
cross-references:
  - phase-3-medicinal-herbs-strategy.md
  - PHASE_3_AUDIENCE_STRATEGY.md
  - phase-3-medicinal-herbs-etsy-listings.md
  - phase-3-medicinal-herbs-content-outline.md
  - phase-2-buyer-retention-lifecycle-strategy.md
  - PHASE_2_EMAIL_STRATEGY.md
  - CANVA_SETUP_AND_EXECUTION_GUIDE.md
tags: [seedwarden, phase-3, medicinal-herbs, launch-checklist, kit-automation, zone-cards, photography, canva, etsy, analytics]
word_count: ~2300
---

# Phase 3 Product-Launch Readiness Checklist — Medicinal Herbs

**Prepared**: May 7, 2026
**Target launch date**: Late June–July 2026 (Women's Health bundle is the anchor; all other bundles follow per the production sequencing in phase-3-medicinal-herbs-strategy.md Part 3)
**Gate condition**: Confirm before executing any Phase 3 production work: Phase 2 forager cohort above 20% of buyers AND Native Plants Regional Guide converting above 1.5%. Check this at Phase 2 Week 6 (approximately July 11, 2026). If gate conditions are not met, defer Phase 3 guide production but keep automation prep and Etsy category setup work active — these are zero-wasted-effort if Phase 3 launches later.

**How to use**: Items are organized by work stream. Each item is tagged [USER ACTION] for tasks only the operator can complete, [BUILD] for creation tasks that can begin immediately, or [VERIFY] for confirmation of existing assets. Complete the [VERIFY] items first (30 minutes total) to establish baseline. Then sequence [USER ACTION] and [BUILD] items by the critical path defined at the end of each section.

---

## Section 1: Kit Automation Setup — Herbalist Email Funnels

The herbalist email funnel defined in PHASE_3_AUDIENCE_STRATEGY.md Part 4 runs in Kit as a parallel automation to the existing Phase 2 welcome and post-purchase sequences. All Kit setup below assumes the Phase 2 Kit account is live and the Phase 2 welcome sequence (5 emails) is active.

### 1.1 Tag Architecture Setup

- [ ] [USER ACTION] Create Kit custom tag: `herbalist` — if not already created in Phase 2 cohort setup. Verify in Kit → Subscribers → Tags.
- [ ] [USER ACTION] Create Kit custom tag: `practitioner-segment` — for ND/NP subscribers from Lead Magnet C.
- [ ] [USER ACTION] Create Kit custom tag: `student-segment` — for herbalism student subscribers from Lead Magnet B.
- [ ] [USER ACTION] Create Kit custom tag: `lead-magnet-black-cohosh` — applied on Lead Magnet A sign-up.
- [ ] [USER ACTION] Create Kit custom tag: `lead-magnet-curriculum` — applied on Lead Magnet B sign-up.
- [ ] [USER ACTION] Create Kit custom tag: `lead-magnet-sample-pack` — applied on Lead Magnet C sign-up.
- [ ] [USER ACTION] Create Kit custom tag: `herbalist-vip` — for herbalist buyers who have made 2+ purchases. Applied manually or via purchase count automation.

**Critical path note**: Tags must exist before any automation referencing them is built. Create all 7 tags in a single Kit session before proceeding to automations.

---

### 1.2 Landing Pages (Three Lead Magnet Pages)

- [ ] [USER ACTION] Create Kit landing page for Lead Magnet A (Black Cohosh Conservation Guide). Fields: first name, email. Headline: "Grow Your Own Black Cohosh: A Conservation Guide for Herbalists and Gardeners." Style: match Phase 2 Zone Quick-Start Card landing page styling. Tag applied on sign-up: `herbalist`, `lead-magnet-black-cohosh`.
- [ ] [USER ACTION] Create Kit landing page for Lead Magnet B (Curriculum Alignment Guide). Fields: first name, email. Headline: "Studying Herbalism? Map Your Curriculum to Real-World Cultivation Guides." Tag applied: `herbalist`, `student-segment`, `lead-magnet-curriculum`.
- [ ] [USER ACTION] Create Kit landing page for Lead Magnet C (Practitioner Sample Pack). Fields: first name, email. Headline: "Sample Patient Education Resource: Medicinal Herb Guides for Integrative Practitioners." Tag applied: `herbalist`, `practitioner-segment`, `lead-magnet-sample-pack`.
- [ ] [VERIFY] All three Kit landing page URLs are live and confirmed functional before any social post or partner email references them.

---

### 1.3 Zapier Sequences for Herbalist Email Funnels

The herbalist funnel is 8 emails over 60 days. Build it in Kit as a Sequence (not a Broadcast). Kit Sequences send emails on a schedule relative to the subscriber's enrollment date — this is the correct tool for a drip funnel.

**Zapier connections required**:

- [ ] [USER ACTION] Set up Zapier trigger: Etsy new order → filter by product tag containing "medicinal" OR "herbalist" → apply Kit tag `herbalist` to buyer email. This is the purchase-entry path for the herbalist funnel. Note: Kit-Etsy connection requires either the Kit-Etsy Zapier Zap template (if available) or a webhook trigger using the Etsy webhook documented in the Phase 2 email automation blueprint.
- [ ] [USER ACTION] Set up Zapier trigger: Kit form submission with tag `herbalist` → send internal Slack/email notification to Anya summarizing new herbalist lead (first name, lead magnet variant). This is optional but provides real-time visibility during early launch.

**Kit Sequence build (8 emails, all copy in PHASE_3_AUDIENCE_STRATEGY.md Part 4)**:

- [ ] [BUILD] Create Kit Sequence: "Herbalist Funnel — Lead Magnet Non-Buyer Track." Add all 8 emails. Set delays: Email 1 (Day 0 = immediate), Email 2 (Day 3), Email 3 (Day 7), Email 4 (Day 10), Email 5 (Day 14), Email 6 (Day 21), Email 7 (Day 30), Email 8 (Day 60).
- [ ] [BUILD] Set Email 6 condition: "Send only if subscriber opened Email 5 but has no Kit purchase tag." In Kit, this requires an automation rule that checks tag presence. Tag to check: any of the Phase 3 product purchase tags (see Section 4 below for Etsy purchase tag naming).
- [ ] [BUILD] Set Email 8 condition: "Send only if subscriber has at least one Phase 3 product purchase tag AND does not have `practitioner-license-purchased` tag." Prevents sending the practitioner license upsell to someone who has already bought it.
- [ ] [BUILD] Create Kit Sequence entry rule: subscribers with tag `herbalist` who do NOT have a Phase 3 purchase tag enter at Email 1. Subscribers who have a Phase 3 purchase tag enter at Email 5 (Content Deepening), skipping the pre-purchase nurture track.
- [ ] [VERIFY] Send test emails for all 8 sequence emails to a personal address before going live. Confirm formatting, links, and personalization fields (`first_name`, `product_name`, `lead_magnet_variant`) resolve correctly.

---

### 1.4 Phase 2 Herbalist Cohort Activation Email

Before the Phase 3 launch, send one pre-launch announcement email to all Phase 2 subscribers tagged `herbalist` or `forager`. This is a Broadcast (one-time send), not a Sequence.

- [ ] [BUILD] Draft pre-launch broadcast email. Subject: "Something new for the medicinal herb practitioners in our community." Body: 3 paragraphs — (1) Announcement: Seedwarden is expanding into medicinal herb cultivation guides; (2) Conservation story: why sourcing ethics are central to every guide; (3) First-notice offer: sign up to receive the Women's Health bundle launch notification and a 10% early-bird discount. CTA: Link to Lead Magnet A landing page (or direct Etsy listing if it is live before the broadcast goes out).
- [ ] [USER ACTION] Schedule the broadcast for 2 weeks before the first Phase 3 Etsy listing goes live.

---

## Section 2: Zone Card Content — 32 Medicinal Herb Guide Cards

Phase 3 introduces a medicinal herbs track to the Zone Quick-Start Card system. The existing Phase 2 zone cards cover foraging, seed saving, and cultivation by zone. Phase 3 adds medicinal herb cultivation zone cards — 8 cards across 4 medicinal zones, 2 species per card, covering the species from the 5 themed bundles.

### 2.1 Zone Selection for Medicinal Herb Cards

The 4 medicinal zones are defined by practical growing overlap for the Phase 3 bundle species:

| Medicinal Zone | USDA Zones Covered | Primary Species in Zone | Card Count |
|---|---|---|---|
| Zone A (Cool Temperate) | Zones 3–5 | Black Cohosh, Valerian, Elderberry, Red Clover | 8 cards |
| Zone B (Warm Temperate) | Zones 6–7 | Vitex, Calendula, Mullein, Echinacea, Lavender | 8 cards |
| Zone C (Subtropical Margin) | Zones 8–9 | Tulsi, Passionflower, California Poppy, Fennel | 8 cards |
| Zone D (Arid/Western) | Zones 5–8 West | Echinacea angustifolia, Astragalus, Lemon Balm, Ginger | 8 cards |

Total: 32 cards. Each card is 2 species. Card format: matches the Phase 2 Zone Quick-Start Card spec (ZONE_QUICKSTART_CARD_SPEC.md) — one card per species pair, printable at 4x6 or 5x7.

### 2.2 Card Content Specification

Each of the 32 cards contains:

- **Card front**: Species pair name + illustrated botanical sketch (from Wikimedia Commons CC images per the phase-3-medicinal-herbs-sourcing-guide.md photo sourcing protocol). Medicinal zone designation and USDA zone range.
- **Card back, Species 1 block**:
  - Common name + Latin binomial (italicized)
  - Planting window for the zone (month range)
  - Sun/shade requirement
  - Soil preference
  - Harvest timing note (1 sentence)
  - Conservation note if UpS At-Risk (1 sentence: "Prefer cultivated stock — see sourcing note in full guide")
  - Contraindication flag if applicable (1 sentence: e.g., "Avoid during pregnancy — see guide for details")
- **Card back, Species 2 block**: Same structure as Species 1.
- **Footer**: Seedwarden logo + "Full guide available at [Etsy shop URL]" + FTC educational disclaimer (2 lines max).

### 2.3 Build Checklist for 32 Cards

- [ ] [VERIFY] Zone Quick-Start Card Canva template from Phase 2 (CANVA_ZONE_CARD_BATCH_WORKFLOW.md) is accessible and can be adapted for medicinal herb species content.
- [ ] [BUILD] Create Canva template variant "Medicinal Herb Zone Card" — use Phase 2 Zone Quick-Start Card template as base. Update color accent to the herbalist-track color (see Section 3.2 for Canva Brand Kit update).
- [ ] [BUILD] Write content blocks for all 32 cards (64 species slots). Source content from the Phase 3 content outlines (phase-3-medicinal-herbs-content-outline.md). Each content block = ~80 words. Total writing volume: ~5,100 words. Allocate 4–5 hours.
- [ ] [USER ACTION] Export 32 cards from Canva as print-ready PDFs (300 DPI). File naming convention: `medicinal-zone-[A/B/C/D]-card-[01-08].pdf`. Save to: `projects/seedwarden/products/zone-cards/medicinal/`.
- [ ] [VERIFY] All 32 exported cards are legible at 4x6 print size. Spot-check 4 cards (one per zone) before completing the full export batch.

---

## Section 3: Product Photography Specs — Phase 3 Medicinal Herb Kits

Phase 3 requires a new photography tier: lifestyle and product images for medicinal herb guide listings. These images feed Etsy listing slots 4–5, Pinterest pins, and Instagram content (per PHASE_3_AUDIENCE_STRATEGY.md Part 5).

### 3.1 Image Category Requirements

**Category 1 — Medicinal Herb Kit Flat-Lay (Required for all 5 bundles)**
Format: Top-down flat-lay. Props: printed guide cover page + relevant dried herbs in small jars or linen sachets + mortar and pestle or small scale + wooden surface or marble tile. One shot per bundle theme with species-specific props. Required dimensions: 2400x2400px (Etsy square) plus a 2:3 vertical crop saved separately for Pinterest (1600x2400px).
Shot list (5 images):
1. Women's Health flat-lay: black cohosh root (raw/dried), dried lavender, calendula petals, mortar
2. Respiratory flat-lay: dried elderberries, mullein leaf, fresh thyme sprig, honey dipper
3. Immunity flat-lay: echinacea root or flower, dried astragalus slices, tulsi leaves, amber glass jar
4. Sleep/Nervines flat-lay: dried valerian root, passionflower vine, dried lavender, small ceramic bowl
5. Digestive flat-lay: fresh ginger root, fennel seeds, dried dandelion root, tea strainer

**Category 2 — Herbalist Lifestyle (Required for social + partnership materials)**
Format: Environmental lifestyle. Props: person's hands (not face visible) leafing through a printed guide or writing in a margin; field journal alongside the guide; herbs on a cutting board. Warm, professional setting — kitchen counter, wooden desk, or garden bench. NOT a clinical/cold setting.
Shot list (3 images):
1. Hands with guide open to a species page, dried herb sample next to the page
2. Guide closed on a wooden desk alongside a cup of tea and botanicals
3. Guide open on an outdoor surface (stone wall, garden bench) with living plants visible in background

**Category 3 — Certification Badge and Practitioner-Focused Image (For practitioner license listings)**
Format: Clean product mockup. A printed guide on a desk alongside a practitioner's tools (stethoscope out of focus, pen, clean clinical desk surface). Conveys "this belongs in a professional setting." Stock photography is acceptable for this category if the stock image meets the 2400x2400px minimum and is available for commercial use. Source from Unsplash (CC0) or Pexels (CC0 commercial license). Keywords: "herbalist desk," "botanical education," "natural medicine practitioner."
Required: 1 image for each practitioner license listing (5 bundles × 1 = 5 images minimum).

### 3.2 Photography Production Options

**Option A (Preferred)**: Anya shoots Category 1 and 2 images herself. Required props: dried herb samples for each bundle theme. Most herbs are available at Mountain Rose Herbs in sample quantities ($2–$8 per herb). Total props cost estimate: $30–$50. Equipment: same setup used for Phase 2 photography (natural light, white or wooden surface). Time estimate: 90 minutes per bundle theme = 7.5 hours total for all 5 bundle flat-lay shots + 3 lifestyle shots.

**Option B**: Source Category 1 images from Wikimedia Commons or iNaturalist for guide content; supplement with Unsplash/Pexels stock for Etsy listing slots. This approach reduces production time but produces less differentiated Etsy images. Use only if Option A is not feasible before launch.

- [ ] [USER ACTION] Order dried herb samples for Category 1 flat-lay props (Mountain Rose Herbs: dried elderberries, mullein leaf, black cohosh root, valerian root, calendula petals, passionflower, echinacea root, astragalus slices, tulsi leaves, fennel seeds, ginger root). Lead time: 3–5 business days.
- [ ] [USER ACTION] Schedule 1 photography session (2 hours) per bundle theme. Can batch all 5 in a 2-day session.
- [ ] [BUILD] Download 5 Unsplash/Pexels stock images for Category 3 (practitioner desk/clinical). Save to `projects/seedwarden/assets/lifestyle-photos/stock/practitioner/`.
- [ ] [VERIFY] All Category 1 and 2 images are exported at 2400x2400px minimum. Verify one image before completing the batch export.

---

## Section 4: Canva Brand Kit Updates — Herbalist-Focused Design Track

The Phase 2 Canva Brand Kit (documented in CANVA_SETUP_AND_EXECUTION_GUIDE.md) uses the core Seedwarden palette. Phase 3 medicinal herbs content uses a secondary palette that distinguishes it from Phase 2 foraging content while remaining within the Seedwarden brand family.

### 4.1 Phase 3 Color Scheme (Herbalist Track)

The herbalist track uses a muted botanical palette derived from dried plant material and apothecary aesthetics — intentionally distinct from the Phase 2 bright foraging palette.

| Color Role | Hex Code | Use |
|---|---|---|
| Primary accent | #6B4F35 | Section headers, card borders, primary CTA buttons |
| Secondary accent | #8A9E6E | Botanical illustration accent, species name text |
| Background | #F5EFE0 | Card backgrounds, email header backgrounds |
| Dark text | #2E2A24 | Body text on all herbalist-track materials |
| Alert/conservation | #B85C38 | UpS At-Risk species callouts, conservation sidebar borders |

These five colors should be added to the Canva Brand Kit as a "Medicinal Herbs" color palette — a secondary palette alongside the existing Seedwarden core palette. Do not replace the core palette.

### 4.2 Fonts

Phase 3 medicinal herb materials use the same Canva font stack as Phase 2, with one addition:

- **Headers**: Playfair Display (already in Phase 2 Brand Kit) — the serif quality reads as "practitioner-grade" for this audience
- **Body text**: Lato Regular (already in Phase 2 Brand Kit)
- **Species names (Latin binomials)**: Lato Italic — this is standard botanical citation style and does not require a new font

No new fonts are required in Canva. The species name italic style is achievable with the existing Lato Italic weight.

### 4.3 Template Library Updates

- [ ] [USER ACTION] Add "Medicinal Herbs" color palette (5 hex codes above) to Canva Brand Kit secondary palette.
- [ ] [BUILD] Create 3 Canva template variants for Phase 3:
  - `template-phase3-zone-card-medicinal.canva` — based on Phase 2 zone card template, updated to herbalist palette
  - `template-phase3-pin-product.canva` — Pinterest pin template with herbalist palette for bundle product pins
  - `template-phase3-pin-educational.canva` — Pinterest educational pin template (longer text overlay, botanical illustration space)
- [ ] [BUILD] Create Instagram carousel template for Phase 3 educational posts (5-slide format: species name → identification → cultivation → traditional use → sourcing note). Base on Phase 2 carousel template. Use herbalist palette.
- [ ] [VERIFY] All Phase 3 Canva templates use the correct herbalist-track color palette (not the Phase 2 bright foraging palette). Cross-reference with the hex codes in Section 4.1 before using any template for live content.

---

## Section 5: Etsy Category Setup — Medicinal Herb Listings

Phase 3 adds a new section to the Etsy shop for medicinal herb guides. This section is distinct from the existing Etsy sections (foraging guides, zone calendars, preservation guides).

### 5.1 Etsy Shop Section Structure (Post-Phase 3 Launch)

Current Phase 1/2 sections (from existing setup):
- Wild Edibles & Foraging Guides
- Seed Saving & Garden Planning
- Homesteading & Preservation
- Zone Calendars & Regional Guides

Phase 3 adds:
- **Medicinal Herbs & Herbalist Guides** (new section)

Within this section, listing subcategory hierarchy:
1. Medicinal Herb Bundles (5 themed bundles)
2. Medicinal Herb Single Guides (12 single-species guides — derived from bundle content)
3. Practitioner Licenses (5 practitioner bulk 10-packs)
4. Medicinal Herb Zone Cards (32 printable zone cards)

### 5.2 Etsy Category and Tag Setup

- [ ] [USER ACTION] Create new Etsy shop section: "Medicinal Herbs & Herbalist Guides." Log in to Etsy Seller Dashboard → Shop Manager → Sections → Add Section.
- [ ] [USER ACTION] Upload the Women's Health Herbs bundle listing first (it is the Phase 3 launch anchor). Use the full listing template from phase-3-medicinal-herbs-etsy-listings.md. Price: $22.00. Etsy category: Digital Downloads → Patterns & How To → Guides.
- [ ] [USER ACTION] Upload the practitioner license listing for the Women's Health bundle within 48 hours of the bundle listing going live. Price: $130.00 (10-pack). SKU: MH-PRAC-10-WH. Listing title: "Women's Health Herbs Guide — Practitioner License (Print & Distribute 10 Copies) | PDF."
- [ ] [BUILD] Prepare all 5 bundle listing templates (copy-paste from phase-3-medicinal-herbs-etsy-listings.md) as draft Etsy listings. Save as drafts — do not publish until Phase 2 gate conditions are confirmed.
- [ ] [BUILD] Prepare 5 practitioner license listing templates (one per bundle). License listings require a modification to the standard bundle description: add a "Practitioner License" section explaining print-and-distribute rights. See Phase 3 strategy document Part 5 for license language guidance.
- [ ] [VERIFY] All Phase 3 Etsy listings have 5 images in the listing slots: slot 1 (cover/product mockup), slot 2 (sample interior page), slot 3 (species close-up botanical photo), slot 4 (lifestyle flat-lay from Section 3), slot 5 (infographic or certification badge graphic). Do not publish a listing until all 5 slots are filled.

### 5.3 Etsy SEO Checklist for Phase 3 Listings

For each of the 5 bundle listings, verify:
- [ ] Title is under 140 characters and leads with the highest-priority keyword (e.g., "Women's Health Herbs Guide")
- [ ] 13 tags are filled. Cross-reference the tag list in phase-3-medicinal-herbs-etsy-listings.md Part 1 for each bundle.
- [ ] Description opens with a paragraph that includes the primary keyword and at least 2 secondary keywords in the first 160 characters (shown in search results preview)
- [ ] Price is consistent with the Phase 3 pricing strategy: bundles $18–$22, practitioner licenses $120–$180, single-herb guides $14–$18

---

## Section 6: Analytics Dashboard — Herbalist Cohort Tracking

The Phase 2 analytics infrastructure (phase-2-analytics-strategy.md, phase-2-analytics-dashboard-template.csv) must be extended to track Phase 3 herbalist cohort performance. Three data streams require dashboard additions.

### 6.1 Herbalist Cohort LTV Tracker

The existing `phase-2-ltv-tracker-phase1-baseline.csv` has columns for each Phase 2 cohort. Add columns for Phase 3 herbalist cohort tracking.

- [ ] [BUILD] Add to `phase-2-ltv-tracker-phase1-baseline.csv` (or create a Phase 3 variant):
  - Column: `cohort` — add value `Herbalist` to the cohort dropdown/column values
  - Column: `first_product_purchased` — track whether entry product was bundle, single guide, or practitioner license
  - Column: `practitioner_license_purchased` — boolean, date if yes
  - Column: `white_label_inquiry` — boolean, date if yes
  - Column: `ltv_30d`, `ltv_60d`, `ltv_90d`, `ltv_12mo` — running totals per buyer
  - Column: `email_funnel_stage` — current herbalist funnel email stage (Email 1 through Email 8, or "post-funnel")

- [ ] [BUILD] Create Phase 3 summary tab in the analytics spreadsheet with the following KPI row structure:
  - Row 1: Total herbalist cohort buyers (count)
  - Row 2: Average LTV herbalist cohort (formula: sum LTV / count)
  - Row 3: Practitioner license attach rate (formula: count with license / total herbalist count)
  - Row 4: Bundle-to-library conversion rate (formula: full library purchasers / total herbalist buyers)
  - Row 5: Email funnel open rate by stage (manual input from Kit Sequence reports)
  - Row 6: Month-over-month revenue from medicinal herb listings (Etsy Seller Dashboard export)

### 6.2 Repeat Purchase Patterns

- [ ] [BUILD] Create a repeat purchase tracking view: filter `phase-2-ltv-tracker` for `cohort = Herbalist`, then view the distribution of purchase counts (1 purchase, 2 purchases, 3+ purchases). This is the metric that reveals whether the herbalist funnel is driving repeat behavior.
- [ ] [BUILD] Add a conditional trigger note to the spreadsheet: "If herbalist cohort repeat purchase rate (2+ purchases) falls below 15% at Month 3, activate the Phase 3 contingency plan (PHASE_3_90_DAY_TIMELINE.md contingency triggers)."

### 6.3 Email Engagement Dashboard

Kit provides Sequence performance reports natively. Supplement with manual tracking in the analytics spreadsheet.

- [ ] [USER ACTION] In Kit, navigate to Sequences → Herbalist Funnel → Performance. Note open rate and click rate for each email. Export the data weekly during the first 60 days post-launch.
- [ ] [BUILD] Create a Kit engagement tab in the analytics spreadsheet with columns: `email_number`, `send_date`, `subscribers_sent`, `open_rate`, `click_rate`, `unsubscribes`. Update weekly.
- [ ] [BUILD] Add alert thresholds: if any email's open rate drops below 20%, flag for subject line A/B test. If Email 5 click rate (first offer email) drops below 8%, flag for offer adjustment (price test or bundle combination test).

### 6.4 Etsy Listing Analytics Integration

- [ ] [USER ACTION] Verify Google Analytics integration is tracking Phase 3 medicinal herb listings separately from Phase 2 listings. In GA4, confirm that events are tagged with the listing ID for each Phase 3 product. Reference google-analytics-integration-guide.md for the event tagging setup.
- [ ] [BUILD] Add Phase 3 Etsy listing IDs to the GA4 event tracking filter once listings are live. Pull weekly from GA4: views, click-through rate (to listing), add-to-cart rate, conversion rate by listing.
- [ ] [VERIFY] Phase 2 analytics baseline (from phase-2-analytics-dashboard-template.csv) is updated with 30 days of Phase 2 live data before Phase 3 metrics are added. Do not blend Phase 2 and Phase 3 metrics — maintain separate sheets.

---

## Section 7: Critical Path Summary

Complete items in this order to avoid production bottlenecks:

**Week of June 22–28 (4 weeks before target launch)**:
1. [USER ACTION] Create all 7 Kit tags (Section 1.1) — 15 minutes
2. [USER ACTION] Create 3 Kit landing pages for lead magnets (Section 1.2) — 60 minutes
3. [USER ACTION] Order dried herb props for photography (Section 3) — 10 minutes; allows 5-day shipping lead time
4. [USER ACTION] Add Phase 3 color palette to Canva Brand Kit (Section 4.1) — 15 minutes
5. [BUILD] Build all 3 Canva Phase 3 templates (Section 4.3) — 90 minutes

**Week of June 29–July 5 (3 weeks before target launch)**:
6. [BUILD] Build Kit Sequence 8-email herbalist funnel (Section 1.3) — 90 minutes
7. [USER ACTION] Photograph all 5 bundle flat-lay shots + 3 lifestyle shots (Section 3) — 2-day session
8. [BUILD] Write zone card content for 32 cards (Section 2.3) — 4–5 hours

**Week of July 6–12 (2 weeks before target launch)**:
9. [BUILD] Export 32 Canva zone cards as PDFs (Section 2.3) — 2–3 hours
10. [BUILD] Prepare all 5 bundle Etsy draft listings (Section 5.2) — 2 hours
11. [VERIFY] Phase 2 gate conditions confirmed (forager >20%, conversion >1.5%)

**Week of July 13–19 (Launch week)**:
12. [USER ACTION] Publish Women's Health Herbs bundle listing on Etsy (Section 5.2)
13. [USER ACTION] Publish Women's Health practitioner license listing on Etsy (Section 5.2)
14. [USER ACTION] Send pre-launch broadcast email to Phase 2 herbalist/forager subscribers (Section 1.4)
15. [USER ACTION] Activate Kit herbalist funnel Sequence (Section 1.3)
16. [BUILD] Extend analytics dashboard for herbalist cohort (Section 6)

**Estimated total operator hours for all Phase 3 launch readiness work**: 20–28 hours across the 4-week critical path. This is achievable at 5–7 hours per week alongside Phase 2 maintenance tasks.
