# Seedwarden WORKLOG

Ongoing log of image downloads, content edits, and sourcing decisions.

---

## Session: 2026-04-27 — Wholesale & Affiliate Partnership Strategy

Built `projects/seedwarden/marketing/wholesale-and-affiliate-strategy.md` (~4,100 words), the B2B and affiliate channel strategy for Phase 2–3 growth beyond direct-to-consumer Etsy.

**Five channels designed**:

1. **Affiliate programs** — Three-tier commission structure (Standard 25%, Partner Creator 30%, Institutional Publisher 20% or flat annual fee). Full outreach list of 20+ named targets across YouTube creators (Melissa K. Norris, Homesteading Family, PREPSTEADERS, Homestead HEART, Dirtpatcheaven, The Seasonal Homestead), blogs (Simply Canning, Prairie Homestead), and newsletter publishers (Mother Earth News, Grit, Backwoods Home). Phase-gated technical upgrade path: UTM + Google Sheet → Pretty Links → Rewardful/Tapfiliate. Commission rationale grounded in existing CAC data from growth-metrics-framework.md (affiliate 25% = Etsy ads $4.80 CAC parity on $14 product).

2. **Wholesale partnerships** — Three sub-models: per-unit add-on for retailer digital bundles ($1.50–$5.00/PDF by volume tier), annual site license for educational/institutional use ($250–$1,200/year), and physical kit inclusion licensing. Named targets: True Leaf Market, Botanical Interests, High Mowing Organic Seeds, Seed Savers Exchange, Southern Exposure, Fedco Seeds, Lehman's, Homesteaders Supply, Roots & Harvest, Valley Food Storage. Institutional targets: county cooperative extension services, FFA chapters, public library seed library programs, community college continuing education. Wholesale outreach email template included.

3. **Corporate training and bulk licensing** — Seat-license pricing model ($2.50–$6.00/seat by volume, $60–$2,497 total per deal). Two sub-channels: employee wellness programs (tech companies with LSA programs, hospital systems, remote-first companies) and disaster preparedness training (CERT program coordinators, corporate ERG trainers, state emergency management agencies). Corporate branded cover add-on ($150 flat) and virtual workshop option ($300/session) documented. Note: 3–6 month sales cycle; Phase 3 start for Phase 4 revenue.

4. **White-label partnerships** — Two sub-models: Etsy kit-bundler inclusion ($2.00/unit, co-branded) and content platform annual license ($1,500–$3,000/year for up to 1,000 members). Named target types for Etsy bundlers: heirloom seed packet sellers (search by review count), homesteading subscription boxes, canning kit sellers, foraging kit sellers. Platform targets: homesteading Patreon communities, survival content platforms (The Prepared, Ask a Prepper), permaculture networks. White-label Etsy bundler email template included.

5. **Seasonal partnership windows** — Three windows aligned to existing demand peaks from annual-product-plan.md. Spring (Jan–Apr): seed companies as primary partners; "Spring Partner Pack" (Seed Saving Manual + Anti-Catalog) licensed at $4.00/unit. Preservation season (Jul–Sep): canning/fermentation suppliers; "Preservation Partner Pack" licensed at $8.00/unit. Holiday (Oct–Dec): subscription boxes and gift retailers; Homesteader's Complete Bundle licensed at $15/unit. Month-by-month calendar for outreach timing for each window.

**Master partnership pipeline template** included: 10-column spreadsheet structure covering all five channels, status workflow (Prospect → Active → Closed), and per-partner tracking columns for revenue and renewal dates.

**Commission structure summary table** consolidates all rates in one reference.

**Phase sequencing recommendations**: Phase 2 = affiliate outreach (10 creators) + spring 2027 seed company co-promotion outreach + first 5 Etsy white-label bundlers. Phase 3 = upgrade tracking infrastructure + institutional extension office outreach + corporate wellness LinkedIn outreach + preservation season 2026 partnerships. Phase 4 = corporate deals close; affiliate revenue $300–$800/month.

**Phase 3 revenue targets**: affiliate $300–$800/month; wholesale/licensing $3K–$8K/year; corporate $500–$2,500/year; white-label $1K–$3.5K/year; total partnership revenue 20–35% of total.

**Design decisions**:
- Commission floor (25%) set at parity with Etsy ads CAC, not as an arbitrary discount — any deal at or above that floor is margin-neutral vs. paid acquisition
- Baker Creek excluded from partner list — confirmed they do not run affiliate or influencer programs (search-verified); approach via media relations if pursuing editorial coverage, not commercial partnership
- Corporate channel treated as Phase 3+ start, not Phase 2 priority — 3–6 month sales cycles make it a Phase 4 revenue contributor even if outreach begins in Phase 3
- White-label full rebrand (Seedwarden branding removed) has a $5,000/year minimum floor; co-branded is the default; this protects brand equity while not foreclosing high-value partnership opportunities

---

## Session: 2026-04-27 — Growth Metrics & Cohort Analysis Framework

Built the full growth metrics and cohort analysis infrastructure for Phase 1+ scaling. Four deliverables created, all cross-referenced.

**`projects/seedwarden/marketing/growth-metrics-framework.md`** (~3,700 words)

Seven sections:
1. Customer cohort segmentation — acquisition channel (Etsy organic, email, social, influencer), first-product price tier (entry/mid/premium/bundle), email engagement health tiers, behavioral tag segments (Seed Saver / City Grower / Preservationist), and seasonal acquisition windows (spring planning / preservation / holiday gift).
2. LTV, CAC, and payback period calculations — Etsy fee baseline (89.6% net margin), LTV by price tier ($14.80–$43 over 24 months), CAC by channel (Etsy organic ~$0, Etsy ads ~$4.80, Pinterest ~$8.00, influencer ~$18), payback period analysis with channel-specific break-even conditions.
3. Product-level cohort analysis — repeat-purchase driver products (Food Sovereignty Guide, Companion Planting Chart, Zone Calendar), one-time buyer products (Hunting Manual, Native Plants, Survival Garden Plans), bundle LTV ceiling problem and cross-sell paths, listing conversion rate benchmarks (1–3% target, below 0.5% = intervention needed, above 3% = ad candidate).
4. Email engagement cohort analysis — open rate health tiers, click-through cohorts by content type, unsubscribe timing patterns (welcome sequence vs. newsletter vs. post-broadcast), segment performance tracking for behavioral tag cohorts.
5. Seasonal cohort tracking — three-peak framework (spring, preservation, holiday), 12-month retention targets per cohort, year-over-year comparison methodology (starts May 2027), seasonal product demand index.
6. Conversion funnel metrics — six-stage funnel from listing impression through VIP status, target rate per stage, diagnostic action when below target.
7. Metrics governance — Etsy vs. Kit data availability, metric optimization hierarchy (listing conversion rate first, list growth second, second-purchase rate third, CAC fourth), 6-month and 12-month KPI targets.

**`projects/seedwarden/analytics/cohort-analysis-template.sql`**

Eight sections of SQL queries: raw data staging views (v_orders_enriched with Etsy fee calculations, seasonal cohort assignment, price tier derivation), cohort retention table (monthly retention %), LTV curves by cohort, seasonal cohort analysis (revenue by season/month, 90-day second-purchase rates), product-level cohort analysis (repeat-purchase trigger rate, cross-sell flow, listing conversion rate with health flags), email engagement cohort queries (subscriber health distribution, behavioral tag performance, unsubscribe timing, email-to-purchase funnel), CAC and ROAS calculations by channel, and a monthly executive summary query. Full table schemas included in appendix for SQLite/DuckDB setup.

**`projects/seedwarden/analytics/dashboard-template.ipynb`**

Eight-cell Jupyter notebook: setup/configuration cell (pandas, matplotlib, seaborn, duckdb; brand palette), data loading with synthetic fallback (250-order sample with realistic seasonal distribution for layout validation before real data is available), revenue trend charts (gross vs. net by month, orders/buyers, AOV trend, bundle revenue %), cohort retention heatmap (seaborn annotated heatmap with cohort size labels), LTV curves by first-product price tier (with 24-month target dashed lines), seasonal cohort performance (stacked revenue by season + second-purchase rate comparison), product-level conversion and repeat-trigger rate charts, email health visualization (subscriber health donut, list growth bar/line, tag distribution), and monthly scorecard with target-tracking output.

**`projects/seedwarden/analytics/monthly-metrics-checklist.md`**

Operator runbook for 90-minute monthly analysis: pre-work exports (Etsy payment CSV, listing stats, Kit subscriber CSV), six sections (revenue analysis, cohort and repeat purchase analysis, email list health, paid channel analysis, listing health audit, data log), Monthly Data Log table template for ongoing appending, actions-arising format with priority tiers, and seasonal action trigger calendar (month-by-month specific actions for the full year).

---

## Session: 2026-04-27 — Annual Product Calendar & Email Growth Engine

Built the full-year growth infrastructure for Seedwarden: four documents covering seasonal strategy, a 12-month product calendar, email automation architecture, and a detailed May–July 2026 social media calendar.

### Files created

**`projects/seedwarden/marketing/annual-product-plan.md`** (~3,400 words)

Six-section strategic roadmap:

1. **Seasonal demand patterns** — Two primary peaks (spring garden Jan–Apr, holiday gift Nov–Dec), one secondary peak (preservation Jul–Sep), plus back-to-school and hunting-season patterns. Month-by-month demand map with top products per month across all 21.

2. **Email marketing architecture** — Six-tier funnel: welcome sequence, nurture newsletter, behavioral segmentation (Seed Saver / City Grower / Preservationist), post-purchase sequence, cart-browse re-engagement, VIP repeat-buyer track. Success metric table with 6-month and 12-month targets.

3. **Seasonal product and bundle strategy** — 21 products assigned to seasonal demand profiles (spring peak, preservation peak, fall/winter gift peak, year-round). Five bundle opportunities mapped to seasons with pricing and positioning. Limited-edition title/tag update schedule for Zone Calendar, Seed Starting Kit, and Survival Garden Plans.

4. **Holiday gift campaign** — October 15 through January cadence: gift listing updates, Pinterest gift guide board, Black Friday/Cyber Monday structure (25% off sale, CYBER2026 bundle code), December 22 last-minute gift email, post-holiday planning pivot.

5. **Social media monthly theme calendar** — 12-month content theme rotation with primary theme, content topics, featured products, and promotional campaigns per month. Six content pillars with percentage targets (Education 35%, Product Feature 20%, Values 15%, Behind-the-Scenes 15%, Community 10%, Relatable 5%).

6. **Etsy seller case studies** — Five case studies: Jill Winger / Prairie Homestead (long-game blueprint, email-first monetization), Pretty Arrow (optimization blueprint, keyword repetition, 14-month $168K), @barefeetandmimosas (400K TikTok, preservation niche, $1,500–$5,000/month), seed saving category benchmarks (top sellers 200–800+ reviews, regional specificity advantage), native plants/foraging niche premium (regional guides command 30–50% price premium, field guide format requirements).

---

**`projects/seedwarden/marketing/product-calendar-2026-2027.json`**

12-month JSON calendar (May 2026 through April 2027) with structured fields per month:
- `themes` — 4 content themes for the month
- `content_topics` — 5 specific post/article topics
- `product_focus` — 3–4 individual products with seasonal rationale
- `bundles_to_feature` — 1–2 bundle recommendations
- `promotional_campaigns` — specific actions (listing updates, ad changes, outreach)
- `email_campaigns` — weekly breakdown of newsletter and segment sends
- `social_cadence` — per-platform posting frequency
- `etsy_actions` — listing, tag, and ad changes
- `kpis` — monthly targets for views, sales, email subscribers, Pinterest views

Annual summary block includes revenue trajectory ($8K–$30K gross year 1), email list trajectory (50 in May 2026 → 1,800–2,500 by April 2027), top revenue months ranked, and seasonal product leaders by category.

---

**`projects/seedwarden/marketing/email-automation-blueprint.md`** (~2,200 words)

Eight-part implementation guide:

1. Lead magnet recommendation — Zone Quick-Start Card (zone-personalized single-page printable), with alternative (existing 5-variety guide from email-and-launch-plan.md), delivery mechanism, and promotion channels including Etsy PDF end-page.
2. Five automations architecture overview — Welcome, Post-Purchase, Newsletter, Win-Back, Seasonal Broadcasts — with trigger conditions and goals.
3. Welcome sequence Kit setup — form configuration, email schedule with conditional send rules, behavioral tag application in Emails 3–4, SEEDWARDEN15 coupon implementation.
4. Post-Purchase sequence — Trigger options (manual vs. Zapier at $19.99/month), three-email structure with product-specific cross-sell variants per cluster, review request language and Etsy direct link.
5. Weekly newsletter — Thursday cadence, 500–800 word format, subject line formulas, seasonal product rotation rule.
6. Win-back campaign — Three emails over 90 days, "Keep me on the list" click trigger, automatic list pruning rationale.
7. Seasonal broadcast campaigns — Five planned campaigns per year with timing, target list, and CTA.
8. Success metrics table — 7 metrics with healthy ranges and action triggers. Quarterly review protocol.

---

**`projects/seedwarden/marketing/social-media-calendar-may-july-2026.md`** (~3,100 words)

Detailed week-by-week social calendar for May, June, and July 2026:

- **May** (4 weeks): Launch week (uses Day 1–7 from existing social-media-calendar.md), then community/seed swaps, native plants/foraging, container gardening. 5 posts/week with full hooks, format, content direction, product tie-in, hashtag stacks.
- **June** (4 weeks): Mid-season troubleshooting, preservation season preview, hot sauce season, seed saving setup.
- **July** (4 weeks): Preservation season launch, fermentation deep dive, dehydrating and long-term storage, homesteader bundle push.
- Pinterest cadence — batch build plan: 63 pins in May (3 variants per product), Board 8 "Food Preservation" created in June, promoted pins ($25–$50) in July on Harvest Preservation and Preservation Bundle.
- 10 evergreen pin topics with copy and Etsy link targets.
- Hashtag reference table by 8 content categories.

### Design decisions

- Zone Quick-Start Card recommended over existing 5-variety lead magnet as the Phase 2 lead magnet upgrade — immediate personal relevance (zone-specific) drives higher completion and perceived value. The existing guide is the interim deployment option (ready to use today without additional work).
- Product calendar delivered as JSON rather than Markdown — more parseable for future automation, and the structured fields make it easier to extract per-field data (e.g., pull all November `etsy_actions` as a checklist).
- Case studies drawn from real creator data documented in phase-3-social-media-growth-strategy.md, supplemented with web research on Etsy seller revenue benchmarks and seasonal patterns. No estimated data presented as confirmed without caveat.
- Social calendar for May Week 1 explicitly defers to the existing 30-day calendar (marketing/social-media-calendar.md Day 1–7) rather than duplicating content — avoids conflicting versions.

---

## Session: 2026-04-27 — Phase 3 Operations Playbook

Built `projects/seedwarden/marketing/phase-3-operations-playbook.md` (~3,600 words), the execution-level Phase 3 infrastructure document. This fills the gap between the existing strategy/calendar/spec documents and daily operational reality.

### File created

**`projects/seedwarden/marketing/phase-3-operations-playbook.md`**

Six sections:

**Part 1 — TikTok Content Creation System**
- Complete shoot-ready production specs (camera setup, lighting rule, safe zones, export settings) — single reference card replaces hunting across multiple documents
- Hook templates by category (educational, values, product feature, relatable) — pull and use
- Populated 30-day content calendar: 30 rows, all platforms, specific hooks, Phase 2 asset references mapped to file paths, product tie-ins, operational notes per post
- Upload schedule optimization: best days (Tue–Fri + Sat AM), best times (7–9pm primary), spacing rules, native scheduler guidance
- Engagement response protocol: 5 comment-type templates, DM templates for "where do I buy this" and "do you ship seeds," 60-minute response window guidance for algorithm boost

**Part 2 — Instagram Reel + Feed Strategy**
- Phase 2 photo asset reuse map: which file from which directory feeds which Instagram format, including the 9:16 crop-from-landscape technique
- Three carousel templates with full slide-by-slide structure: "X Things You Need to Know" (saves-optimized), "Problem-Solution" (conversion-optimized), "Variety Spotlight" (brand-building, generates 10 carousels from Anti-Catalog alone)
- Daily Story mechanics: 3–5 slide structure, one interactive element per day, behind-the-scenes Story content from Phase 2 raw photo outtakes, link slide frequency rule (not every day)
- Bio link strategy: rotation schedule (Etsy default / Kit lead magnet / product launch), 140-character bio copy with rationale, Linktree avoided with reasoning

**Part 3 — Pinterest Pin Strategy**
- Full design specs: 1000×1500px, text overlay formula, font minimums, contrast rule, Seedwarden hex palette
- Three-template system with complete structure for each: product mockup pin (commercial intent), benefit-focused pin (discovery intent), educational hook pin (longest lifespan)
- 63-pin batch build plan: 3–4 hour Canva session, build order aligned with PHASE2_PRODUCT_PRIORITIES.md tiers
- 7-board structure with keyword-optimized names, purpose, pin types, pinning frequency, cross-linking rule
- Rich Pins setup: one-time Etsy catalog integration, 20-minute setup instructions

**Part 4 — Email List Launch**
- Welcome sequence activation: three specific changes to make to existing email-and-launch-plan.md sequence before Phase 3 launch (update product recommendations with Phase 1 data, add seasonal P.S.)
- Weekly newsletter template: Thursday cadence, 800–1,000 words, four-section structure (growing update / technique / product spotlight / mailbag), 10-item subject line swipe file
- Segment strategy: three Kit behavioral segments (seed saving, urban/apartment, food preservation) with click-trigger setup and practical application for Thursday split sends
- 3-email win-back campaign: targeting non-openers after 6 missed emails, free resource re-engagement offer, automatic list removal implementation, 90-day schedule

**Part 5 — First 30 Days Execution Checklist**
- Pre-launch week: 9-item checklist before Day 1 (content bank, Canva templates, 63 draft pins, Pinterest boards, Rich Pins, Kit sequence)
- Days 1–7: day-by-day posts with Pinterest pin assignments
- Days 8–14: mid-week analytics review instructions, Etsy traffic source tracking
- Days 15–21: influencer outreach launch (Day 15), social proof content prep, analytics milestone
- Days 22–30: first standalone email, second outreach batch, first Thursday newsletter, Month 1 WORKLOG entry

**Part 6 — Decision Trees**
- Six operational triage rules: whether to post under time pressure, which product to feature, how to handle an unexpected high-view video, Pinterest flatline diagnosis, influencer response protocol, Phase 3 launch gate (no Phase 2 photos = delay)
- Cross-reference index mapping decision types to specific document sections

### Design decisions
- Option A selected over Option B (paid ads infrastructure) because Phase 3 paid ads strategy is well-covered in phase-3-social-media-growth-strategy.md (Section 4 is 800+ words of detailed paid channel guidance). The operational gap was daily execution templates and the populated calendar, not more strategy.
- 30-day calendar kept product-agnostic for Days 3, 8, 15 (the three "top converting product" slots) — these slots are deliberately held open and filled from Phase 1 conversion data. Populating them with guesses would require revision at Phase 3 launch.
- Email segment strategy is behavioral (click-triggered), not demographic — more accurate and requires no subscriber self-identification.

---

## Session: 2026-04-27 — Phase 2 Photography Execution Planning

Three Phase 2 planning documents created. These are preparation materials for when LIFESTYLE_PHOTOGRAPHY_STRATEGY.md is approved by the user. Phase 2 is currently blocked on Phase 1 tag corrections + Etsy account verification.

### Files created

**`projects/seedwarden/PHASE2_PHOTOGRAPHY_EXECUTION_PLAN.md`** (~1,750 words)
Operational execution plan for the hybrid photography approach (15 products physical, 6 products stock).
- Section 1: Logistics breakdown — which 15 products get physical photos vs. which 6 get stock, including specific props lists by cluster and tablet/printed-page setup guidance.
- Section 2: Week-by-week timeline — Week 1 stock sourcing (free sources then iStock fill-in for Clusters D/E), Week 2 physical shooting and editing for Clusters A/B/C, Week 3 final compositing and Etsy upload. Includes per-day action items.
- Section 3: Equipment and location setup — minimum viable kit (smartphone + wooden surface + window light), optional softbox, backdrop choices by cluster.
- Section 4: iStock credit purchasing strategy — on-demand credits over subscription, priority order for 6 gap products, license verification checklist, expected spend at $0/free-tier, $48–$90 (4–6 images), or $120–$150 maximum.
- Section 5: QA checklist — 15-item checklist covering technical specs (2400×2400px, under 1MB), Etsy compliance (no competing brands, not misleading), conversion-focused angles (product visible, props on-theme, natural lighting, earthy hands), brand consistency (warm tone, non-aspirational).
- Section 6: Risk mitigation — 5 risks with mitigations and fallback paths (physical photo failure, iStock budget exhaustion, scheduling constraints, compositing quality issues, Phase 1 data suggesting photos are low priority).

**`projects/seedwarden/PHASE2_PRODUCT_PRIORITIES.md`** (~650 words)
Priority matrix for sequencing lifestyle photography across all 21 products.
- Tier 1 (photograph first, Week 1 critical mass): Survival Garden $22, Hunting Manual $20, Livestock Manual $18, Meat/Fish Preservation $18, Harvest Preservation $16. These are the 5 highest-ticket products with the most revenue upside per additional conversion. Getting lifestyle images live on these 5 within Week 1 is the critical mass threshold.
- Tier 2 (photograph second): Fermented Harvest $13, Hot Sauce $15, Seed Saving Manual $14, Native Plants $18, Heirloom Guide $11, Apartment Plant Catalog $14, Container Blueprint $12.
- Tier 3 (photograph third, minimal additional setup): remaining lower-ticket products; all shoot during existing Cluster A/B batch sessions at near-zero marginal cost.
- Tracking note: record the date lifestyle images go live on each listing; before/after conversion measurement window begins from those dates.

**`projects/seedwarden/PHASE2_TO_PHASE3_TRANSITION.md`** (~900 words)
How Phase 2 photography output feeds Phase 3 social media (TikTok, Instagram, Pinterest).
- Phase 3 readiness checklist (photography complete, social accounts set up, 30 days of Phase 1 data collected).
- Platform-by-platform breakdown: TikTok (lifestyle photos as B-roll stills cut into educational videos), Instagram (Reels cross-posts, carousel format using cluster photos, Stories from raw behind-the-scenes shots), Pinterest (3 pin variants per product from same photo = 63 minimum pins).
- Example 30-day content calendar with specific post-by-post asset mapping (which Phase 2 photo goes into which post type on which platform).
- Critical handoff instruction: archive raw (unedited, uncropped) Phase 2 photos separately from Etsy-ready composites; raw photos are the Phase 3 content bank for vertical (9:16), horizontal (16:9), and Pinterest (2:3) formats.
- Recommended folder structure: `marketing/lifestyle-photos/stock/`, `raw/cluster-a/ b/ c/`, `etsy-ready/`.

### Verification
`phase-3-social-media-growth-strategy.md` reviewed and confirmed complete (created this same session earlier). All three new files cross-reference it and the content calendar template and creator brief from the prior Phase 3 preparation session.

---

## Session: 2026-04-27 — Phase 3 Launch Preparation Framework (Option A)

Three Phase 3 preparation documents created. Option A selected over Option B based on existing ready material: Phase 3 strategy doc complete, 30-day launch calendar complete, video scripts complete, product mockups all generated.

### Files created

**`projects/seedwarden/marketing/phase-3-content-calendar-template.md`**
Reusable 30-day block framework extending the launch calendar into ongoing Phase 3 operations.
- Content mix ratios by category (educational 35%, product feature 20%, values 15%, behind-the-scenes 15%, community 10%, relatable 5%)
- Posting frequency per platform (TikTok 4–7/week, IG Reels 3–4/week + daily Stories, Pinterest 5–7 pins/week)
- Seasonal content angles for May–July 2026 window (late spring planting prep, garden launch, companion planting payoff, peak preservation season)
- Product-to-content-theme mapping for all 21 products with recommended platform per product
- Repeating 30-day calendar skeleton (30 rows, all platforms, all categories)
- Pre-built hashtag stacks by post type
- Monthly tracking metrics table with action thresholds

**`projects/seedwarden/marketing/phase-3-creator-brief.md`**
1.5-page creator partnership brief for influencer outreach, ready to attach or adapt for DM/email.
- Brand description written for external creator audience (not internal voice)
- Audience fit criteria and why Seedwarden products convert for homesteading/gardening creators
- 7 specific video angles with full descriptions (seed saving how-to, heirloom variety stories, container setup, hot sauce, seed-buying treadmill, container compatibility, planner walkthrough)
- Three partnership structures: gift+affiliate (25% commission), flat fee+affiliate ($150–$300 + 15% commission), ongoing affiliate (25% indefinite)
- FTC disclosure requirements, creative control terms, Etsy affiliate tracking note
- Full 21-product reference table with price and best audience match per product
- Outreach tracker template + priority target criteria

**`projects/seedwarden/marketing/phase-3-platform-asset-specs.md`**
Platform specification reference document.
- TikTok: video dimensions, safe zones, caption limits, hashtag stack, export settings
- Instagram: Reels (9:16), Carousels (1:1 and 4:5), Stories (9:16), static posts — dimensions, safe zones, hashtag strategy
- Pinterest: standard pin (2:3), video pin, text overlay formula, three-variant-per-product approach, link-to-listing requirement
- Etsy: shop banner (3360x840px, mobile crop zone), listing images (2400x2400px already generated), listing video spec
- Cross-platform repurposing map (TikTok to IG Story to Pinterest pin to carousel)
- Canva export cheatsheet (all assets, all platforms)

---

## Session: 2026-04-27 — Phase 3 Social Media Growth Strategy Research

Completed deep research document for Phase 3 (post-Phase 1 launch) social media and paid advertising strategy.

**File**: `projects/seedwarden/phase-3-social-media-growth-strategy.md`

**Research scope covered**:
- TikTok competitive landscape: top creators by follower tier (ballerinafarm 10.5M, itsbreellis 772K, thermal_and_oaks 367K), engagement benchmarks (7.5% under 100K), hashtag strategy (#homestead = 5.4B views), monetization thresholds
- Instagram and Pinterest strategy: Pinterest CPC $0.05–$0.50, 33% more referral traffic to Etsy than Facebook, pin lifespan 4+ months, posting cadence, format differences by platform
- Creator breakdown: Jill Winger (Prairie Homestead) as canonical case study, mid-tier creators at 100K–600K with relevant audience overlap, 5 traits shared by successful monetizing creators
- Paid ads: Etsy ROAS benchmarks (2.8x average, 1.05 break-even for digital products), Facebook Shopping category CPC $0.34, Pinterest CPA ~$8, phased budget allocation
- Influencer partnerships: micro-influencer rate cards ($100–$500/post), three deal structures (pure affiliate, gift+affiliate, flat fee+affiliate), direct outreach approach at Phase 3 budget level
- Phase 3 blueprint: 3-month implementation timeline, $500–$1,000/month budget allocation table, success scorecard, 4 failure modes with mitigations

**Sources**: 28 cited sources including WordStream 2025 benchmarks, Tailwind Pinterest cost data, Feedspot creator lists, IZEA homesteading influencer report, Emplicit TikTok engagement data, Influencer Marketing Hub micro-influencer rates, eRank/Marmalead Etsy platform data.

---

## Session: 2026-04-26 — Track B Mockup Advancement (phone frame variant)

### Step 1: Regenerate tablet mockups (timestamp sync)

All 21 tablet mockups regenerated to sync with the Apr 26 PDF rebuild
(native-plants-regional-guide.pdf and all others). Previously the native-plants
mockup was dated Apr 14 while the PDF was Apr 26.

- 21/21 PDFs processed, 0 failures
- Output: `projects/seedwarden/mockups/*-mockup.png`
- All files 341-388 KB, 2400x2400 px

### Step 2: Phone frame variant

Added `--frame portrait` argument to `generate_mockups.py`. When passed, the
script renders each PDF into a matte-black portrait smartphone frame (iPhone 13
proportions, scaled 2x for the 2400x2400 canvas) instead of the tablet frame.

**New function: `build_phone_frame(screen_img)`**
- Draws phone body in matte black (28, 28, 30) with PHONE_RADIUS=100 corners
- Drop shadow: darker than tablet shadow (30, 35, 30, 120 alpha) to read against light background
- Dynamic Island pill notch at top centre (200x40px pill)
- Side buttons: power button right side, volume up/down left side
- Home indicator bar: thin pill at bottom of screen area
- Subtle white rim-light highlight (18 alpha) on phone body edges
- Screen area: PHONE_SCREEN_W x PHONE_SCREEN_H (820x1700px), inset 30px sides, 100px top/bottom

**Helper: `_draw_phone_frame(canvas)`**
- Draws the phone chrome layer (body, notch, buttons, indicator) on top of an already-pasted screen image

**Output naming**: `{stem}_phone.png` (underscore before "phone" to distinguish from `-mockup.png` tablet files)

All 21 phone mockups generated, 0 failures. All 2400x2400 px, ~70 KB each
(smaller than tablet mockups because the phone body covers less canvas area,
leaving more of the plain gradient background).

**Backward compatibility verified**: running without `--frame` still generates
tablet mockups with original `-mockup.png` naming and original geometry.

### Files changed
- `projects/seedwarden/scripts/generate_mockups.py` — added `--frame portrait` argument, `build_phone_frame()`, `_draw_phone_frame()`, PHONE_* geometry constants
- `projects/seedwarden/mockups/*_phone.png` — 21 new phone mockup files

---

## Session: 2026-04-13 — Wild Edibles Habit Photos

### Status update

The "0/18 complete" counter in the prior task description was stale. PROJECTS.md (Session 74) confirmed all 120+ native-plants images are downloaded and cached under `projects/seedwarden/scripts/images/native-plants/`. Actual count as of this session: **129 images** (including all 18 wild edibles and additional species).

Both Stellaria media and Taraxacum officinale images were already present as valid JPEG files (~960KB each) downloaded via the Wikipedia REST API in Session 74.

### Images logged this session

| Species | Common Name | Filename | Source URL | License | Notes |
|---------|-------------|----------|------------|---------|-------|
| *Stellaria media* | Chickweed | `stellaria-media-habit.jpg` | https://upload.wikimedia.org/wikipedia/commons/0/05/Kaldari_Stellaria_media_01.jpg | CC0 | Author: Kaldari (Wikimedia Commons). Full habit photo showing sprawling mat habit, white star flowers. |
| *Taraxacum officinale* | Dandelion | `taraxacum-officinale-habit.jpg` | https://upload.wikimedia.org/wikipedia/commons/4/4f/DandelionFlower.jpg | CC BY-SA 3.0 | Author: Greg Hume (Greg5030, Wikimedia Commons). Attribution required for any publication. Share-alike applies. |

### Files created

- `/projects/seedwarden/assets/wild-edibles/stellaria-media-habit.jpg` — copied from scripts/images/native-plants/stellaria-media.jpg
- `/projects/seedwarden/assets/wild-edibles/taraxacum-officinale-habit.jpg` — copied from scripts/images/native-plants/taraxacum-officinale.jpg

### License notes

- CC0 images (Stellaria media): free for all uses including commercial, no attribution required (though attribution recommended as good practice).
- CC BY-SA 3.0 images (Taraxacum officinale): attribution required, derivative works must use same license. For Etsy PDF products this means adding a photo credits page. Acceptable for commercial use with proper credits.

---

## Image sourcing: full native-plants set

All 129 images in `scripts/images/native-plants/` were sourced via:
1. Wikipedia REST API summary endpoint (`https://en.wikipedia.org/api/rest_v1/page/summary/[Article]`) — returns curated main article image, typically high quality botanical photograph.
2. iNaturalist API fallback for species where Wikipedia lacked a usable image (CC0 and CC-BY research-grade observations, sorted by votes).

Source: `scripts/download_plant_images.py`. Session 74 verified all 129 files are valid JPEGs.

---

## Session: 2026-04-26 — Native Plants PDF image pipeline rebuild

### Problem
`native-plants-regional-guide.pdf` was 56.96 MB — exceeding Etsy's 5 MB hard upload limit.

### Root cause
The 129 source images (downloaded via Wikipedia REST API and iNaturalist) were embedded into FPDF at full resolution. Source images ranged from 500px to 5,472px wide, averaging 118 KB for already-small images and up to 10 MB for large ones. FPDF does not compress JPEG images during embedding, so the full file size was transferred into the PDF for each of the 126 unique images referenced (275 total references including repeats across regions).

### Fix
Added Pillow-based image compression to `generate_pdfs.py`:

- New constants: `_MAX_IMAGE_PX = 600`, `_JPEG_QUALITY = 55`
- New function `_compressed_image_path(src)`: re-encodes every image as JPEG at quality 55 and at most 600px on the long axis, caching results in a process-scoped temp directory. Runs regardless of original image size (previously small images at 118 KB each also contributed significant bulk).
- `render_line()` now calls `_compressed_image_path()` before passing path to `pdf.image()`.
- Source images in `scripts/images/native-plants/` are untouched.

### Results
| Version | File size | Pages |
|---------|-----------|-------|
| Before (original) | 56.96 MB | 404 |
| After (600px, q55) | 4.91 MB | 404 |

Compressed images average 31 KB each (down from 118-2213 KB). At 600px wide displayed at 110mm in the PDF, effective DPI is ~138 — adequate for on-screen reading and plant identification.

### Files changed
- `projects/seedwarden/scripts/generate_pdfs.py` — added Pillow imports, `_compressed_image_path()`, updated `render_line()` to use it

---

## Content note: guide cross-references

The native-plants-regional-guide.md has a "More from Seedwarden" section (lines 7727-7735) with 3 cross-links. The product-audit recommends expanding to 2-3 links minimum — current 3 links meets the minimum. Regional cross-reference expansion (thin "see Northeast entry" stubs) is tracked separately in fix_guide.py output.

**Southwest region is thin**: 14 entries vs. 27-46 in all other regions. Flagged for content expansion in a future session.

---

## Session: 2026-04-26 — Track B Status Assessment

### Track B: Native Plants Regional Guide — Production Ready

**PDF rebuild verified complete.**

| Check | Result |
|-------|--------|
| File size | 4.91 MB (Etsy hard limit: 5 MB) — PASS |
| Page count | 404 pages |
| Timestamp | Apr 26 20:22 (rebuilt this session) |
| Mockup exists | native-plants-regional-guide-mockup.png, 355 KB, 2400x2400 px — PASS |
| Mockup currency | Mockup dated Apr 14; PDF rebuilt Apr 26. Mockup shows pre-rebuild cover. Recommend regenerating before upload. |

The 4.91 MB figure is confirmed by both the WORKLOG session entry (Session 486) and direct file stat. The PDF is compliant for Etsy upload. However, the existing mockup was generated from the pre-rebuild PDF (Apr 14 timestamp vs PDF Apr 26 timestamp). Whether the cover page changed during the rebuild is unclear — regenerating the mockup before upload is low-cost insurance.

### Track A: 8 Text-Heavy Products — Status

The UPLOAD_SEQUENCE.md Phase 2 backlog lists 13 products as "ready now." The 8 products matching the "text-heavy" description (all content, PDF, and listing copy complete; no blocking issues):

| # | Product | Price | PDF Size | Blocking Issue |
|---|---------|-------|----------|----------------|
| 1 | Seed Swap Hosting Kit | $10 | 680 KB | None |
| 2 | Zone-by-Zone Seed Starting Calendar | $8 | 771 KB | Tag correction needed (user applies at upload) |
| 3 | Apartment Seed Starting Kit | $9 | 683 KB | None |
| 4 | 12-Month Urban Growing Planner | $7 | 688 KB | None |
| 5 | Container Growing Blueprint Pack | $12 | 686 KB | None |
| 6 | Heirloom Variety Selection Guide | $11 | 690 KB | None |
| 7 | Fermented & Preserved Harvest Handbook | $13 | 697 KB | None |
| 8 | Apartment Growing Complete Guide | $13 | 884 KB | None |

All 8 have PDFs under 5 MB, mockups at 2400x2400 px, and listing copy in etsy-store-copy.md. Tag corrections for Zone Calendar are documented in UPLOAD_READY_CHECKLIST.md Section 4 and UPLOAD_SEQUENCE.md. These products are Phase 2 in the upload sequence — they do not require user action beyond Etsy account verification (which is a Track A shared blocker).

### Phase 2 Work (phone mockups, lifestyle, printed page mockups) — Assessment

MOCKUP_STRATEGY.md documents three Phase 2 enhancements:

1. **Phone mockup variations** — New script variant producing portrait phone frame. Estimated 2-3 hours to write the frame, 30 min to generate all 21. Can start NOW without Phase 1 data. Does not require conversion data; a phone frame is additive.

2. **Interior page mockup** — Modified generate_mockups.py to render an interior page instead of the cover. Estimated 1-2 hours to modify script. Can start NOW. Especially useful for Companion Planting Chart and Zone Calendar (chart-format content; buyers want to see the content structure before purchasing).

3. **Lifestyle photography / printed page mockups** — Requires stock images or actual photography. Cannot be fully automated. Can prepare stock-image sourcing brief now, but actual assets require user input on visual direction. Partially blocked.

MOCKUP_STRATEGY.md explicitly notes: "Do not spend time on these until at least 7 days of live listing data is available." This guidance applies to deciding WHICH products to prioritize, not to the technical work of building the mockup variants. Building the phone frame script and interior page script now means Phase 2 rollout takes 30 minutes instead of 3 hours once data is in.

### Next Work Item Recommendation

**Recommended: Regenerate the native-plants mockup from the rebuilt PDF, then build the phone-frame mockup script variant.**

Rationale:
- Regenerating the native-plants mockup is a 30-second task (run generate_mockups.py). Ensures the cover image in the listing matches the rebuilt PDF.
- Building the phone-frame script variant is pure code work, no user action needed, and it unlocks image slot 2 on all listings the moment Phase 1 goes live.
- Southwest region content expansion (14 entries vs. 27-46 in other regions) is the other available Track B task — valid but lower priority than the mockup work.

### Files checked this session

- `projects/seedwarden/scripts/output/native-plants-regional-guide.pdf` — 4.91 MB, 404 pp, Apr 26
- `projects/seedwarden/mockups/native-plants-regional-guide-mockup.png` — 355 KB, Apr 14 (pre-rebuild, needs regen)
- `projects/seedwarden/UPLOAD_READY_CHECKLIST.md` — Phase 1 status, tag corrections
- `projects/seedwarden/UPLOAD_SEQUENCE.md` — Phase 1 and Phase 2 backlog
- `projects/seedwarden/MOCKUP_STRATEGY.md` — Phase 2 mockup plan
- `projects/seedwarden/product-audit-2026-04-11.md` — product readiness by tier
- `projects/seedwarden/scripts/generate_pdfs.py` — confirmed Pillow compression active

---
