---
title: "Phase 1 to Phase 2 Transition Roadmap — Seedwarden Native Plant Guides"
date: 2026-06-04
version: 5.0
prepared_by: research-agent (claude-sonnet-4-6)
status: production-ready — decision-support document
supersedes: v4.0 (June 4, 2026)
confidence: 90%
scope: >
  Track-agnostic Phase 1 → Phase 2 scaling decision framework. Covers gate metrics,
  content production planning, platform capacity, Phase 1/2 operational overlap,
  risk scenarios, data collection checklist, decision logic, supply chain implications
  (including 3D-printing / mfg-farm intersection), and Phase 2 content gap analysis.
  Applies to Path A (Etsy-first), Path B (social-first), or both executing concurrently.
sources:
  - Kit pricing: emailtooltester.com, passivekit.com (2026)
  - Etsy benchmarks: insightagent.app, craftybase.com, printify.com (2026)
  - Email benchmarks: mailerlite.com, inboxally.com, klaviyo.com (2026)
  - Social benchmarks: socialinsider.io, rivaliq.com, posteverywhere.ai (2026)
  - Content production: yourcontentempire.com, brianhonigman.com, automateed.com
  - Etsy suspension/policy: cindylouwho2.com, etsy.com/legal (2025-2026)
  - TikTok algorithm: socialync.io, presencenews.org, opus.pro (2026)
  - Print-on-demand: lulu.com, reedsy.com (2025)
  - 3D printing packaging: 3dinsider.com, all3dp.com (2025-2026)
  - Phase 2 content scope: PHASE_2_GUIDE_CONTENT_BLUEPRINT.md (May 9, 2026)
---

# Phase 1 to Phase 2 Transition Roadmap
## Seedwarden — Native Plant Guides Scaling Framework

---

## Executive Summary

Phase 2 is defined as: producing 20–30 new plant guides, expanding distribution to additional channels (premium ebooks, potential print-on-demand), and investing in infrastructure (Kit Creator upgrade, content scheduling tools, possible print partnerships). The threshold question is whether Phase 1 performance justifies that investment.

**The core finding**: Phase 2 approval should not wait for perfect Phase 1 data. The binding constraint is the summer 2026 botanical photography window (June 15 – August 15 for Zones 4–6), which cannot be recovered if missed. If Phase 1 launches in early June, the Day 14 gate checkpoint falls approximately June 17–20 — enough runway to greenlight a June 22 Phase 2 writing sprint before the photography window peaks. Waiting for Month 1 data before starting content production squanders the highest-quality field conditions of the year.

**The decision gate is binary**: At Day 14 post-launch, if email subscribers reach 25+ with a 15%+ open rate on Email 1, Phase 2 content production should begin. Everything else — Phase 2 scope (3 bundles vs. 5), Kit upgrade timing, collaborator recruitment — is calibrated against the data that arrives by Day 30. Phase 2 beginning is not the same as Phase 2 fully committing.

**Phase 1 and Phase 2 can and should run in parallel**: Content production does not require Phase 1 to stabilize first. The two operations draw on different time blocks — Phase 1 monitoring takes 5–10 minutes per day; Phase 2 writing takes 4–6 hours in sprint blocks. The conflict point is social media management, which can be addressed by pre-scheduling 2 weeks of Phase 1 posts before the Phase 2 sprint begins.

**Supply chain is not a Phase 2 risk** for a digital product business. Etsy digital delivery is unlimited. The only genuine constraint as scale increases is Kit email tier limits, which are well-defined and low-cost to address. Physical products — if introduced in Phase 3 — introduce the first real supply chain complexity.

---

## Section 1: Phase 1 Success Metrics

Phase 1 monitoring covers three time windows: Day 7 (early signal), Day 14 (primary gate), and Day 30 (confirmation). Track the following 10 metrics. The gate decision uses G1, G2, and G4 as the three primary indicators; the others provide diagnostic context.

### Gate Metric Table

Evaluate at Day 7, Day 14, and Day 30 post-launch.

| # | Metric | Red — Defer Phase 2 | Yellow — Reduced Scope | Green — Full GO | Weight |
|---|--------|---------------------|----------------------|-----------------|--------|
| G1 | Kit email subscribers (Day 14) | Under 25 | 25–74 | 75+ | **Primary** |
| G2 | Email 1 open rate (48-hr settled) | Under 15% | 15–24% | 25%+ | **Primary** |
| G3 | Email click-through rate (Email 1) | Under 2% | 2–4% | 5%+ | Secondary |
| G4 | Etsy listing conversion rate — views to sales (Track A) | Under 1% | 1–3% | 3%+ | **Primary (Track A)** |
| G5 | Etsy 30-day unit sales | Under 10 | 10–29 | 30+ | Secondary |
| G6 | Social reach — cumulative Day 14, all platforms | Under 500 | 500–2,000 | 2,000+ | Secondary |
| G7 | Influencer or community shares | 0 | 1–2 | 3+ | Secondary |
| G8 | Average order value trend (Days 1–30) | Declining | Flat | Stable or rising | Low |
| G9 | Email list 7-day retention (no unsubscribes after Email 1) | Under 50% | 50–65% | 65%+ | Secondary |
| G10 | Revenue trajectory — 30-day annualised | Under $2,400/yr | $2,400–$6,000/yr | $6,000+/yr | Low |

**Decision logic — all three gates evaluated together:**

- All G1, G2, G4 GREEN: Full Phase 2 GO. Begin content production sprint within 14 days of gate read.
- Two of three GREEN, none RED: Proceed with reduced scope (produce 10 guides rather than 20–30; hold physical product investment).
- Any G1, G2, or G4 RED: Hold Phase 2 sprint. Run 2-week rapid-distribution push first. Re-evaluate at Day 30.
- G10 RED with all others YELLOW or better: Proceed. Revenue lags conversion for digital products; early list quality predicts late revenue.

**Override conditions** — Phase 2 unlocked even in RED scenarios:
1. Email 1 open rate exceeds 35% on any list size: exceptional audience-product fit; write Phase 2 content immediately.
2. Three or more influencer/community shares with confirmed clicks: audience exists; conversion infrastructure needs work, not content.
3. Any Etsy listing achieves 5%+ conversion rate: pricing and positioning are correct; scale is the solution.

### Benchmark Context

**G1 — Subscriber count.** Kit free tier supports 10,000 subscribers — no platform constraint on list size in Phase 1 or early Phase 2. The 75-subscriber Green threshold is deliberately low: a 75-subscriber niche list with 30% opens outperforms a 5,000-subscriber broad list with 10% opens in purchase intent for a content-led product.

**G2 — Open rate.** Industry averages for niche content creators in 2025–2026 run 25–43%. A 25%+ rate on a brand-new list signals subscribers opted in with genuine interest. Below 15% suggests spam placement or low-quality acquisition. Niche interest lists built on a free lead magnet typically open higher than broad commercial lists.

**G4 — Etsy conversion.** Etsy-wide average for digital products: 1–3% of views converting to sales. Top performers in niche digital products reach 12–20%. A new shop should expect 1–2% in first 30 days, rising to 3–5% as reviews accumulate. Above 3% in the first 30 days with fewer than 5 reviews is a strong signal.

**G6 — Social reach.** Instagram accounts under 10K followers see 1.5–6% engagement in 2026. Pinterest is search-driven — a pin retains discovery value for 12+ months and does not register meaningfully in 14-day launch data. Measure reach volume at Day 14; measure engagement rate at Day 30.

**G8 — Average order value.** For a single-price digital product, order value is effectively constant unless a bundle upgrade is offered. If 20%+ of buyers choose a premium option when offered, Phase 2 premium pricing is validated.

### Healthy Conversion Rate Context

Etsy digital products: 1–3% average, 3–5% strong, 5%+ top tier. For native plant guides in the homesteading/foraging niche specifically, the closest public analogs (seed catalog digital shops, homesteading plan bundles) cluster around 2–4% once the shop has 10+ reviews. Day 1 conversion at 0.8–1.5% is expected and not a concern. The threshold to investigate is under 0.5% after 200+ views on any single listing — that signals a trust, price, or clarity problem rather than a traffic problem.

---

## Section 2: Phase 2 Timeline and Dependencies

### If Phase 1 Launches June 3

| Checkpoint | Date | Decision |
|------------|------|----------|
| Day 3 | June 6 | First metrics read. 4+ targets met = Phase 2 preparation on schedule. |
| Day 7 | June 10 | Tier 2 partnership identification. Check G1: if 50+ subscribers, begin pre-sprint infrastructure. |
| Day 14 | June 17 | Primary gate. Apply G1–G10 table. Full GO / reduced scope / HOLD decision. |
| Phase 2 sprint start | June 22 | Women's Health bundle writing begins (22-day sprint). |
| Phase 2 first Etsy upload | ~June 29 | First Phase 2 guide live. |
| Phase 2 sprint close | July 13 | Final Phase 2 bundle uploaded. |
| Day 30 | July 3 | Confirm Day 14 decision was correct. Assess revenue trajectory against G10. |
| Phase 2 autumn sprint | September–October | Second production batch (15–18 more guides). |
| Phase 2 catalogue target | October 31 | 20+ guides live (baseline scenario), 30+ guides (aggressive with collaborators). |

### Does Phase 2 Require New Content?

Yes — Phase 2 is primarily a content production sprint. Phase 1 launched with the Zone Quick-Start Card (free lead magnet) and the first guide bundle (Bundle E, 5 species). Phase 2 requires:

- 18–25 additional species guides (see Appendix)
- Revised email sequences for medicinal herb subscribers (separate automation, requires Kit Creator upgrade)
- 3 new Etsy bundle listings with full tag/SEO optimization
- 15–20 social post templates for the medicinal herbs content pillar
- New Pinterest infographics for Phase 2 species (evergreen SEO value)

None of this requires creating new infrastructure — it requires filling content into the infrastructure Phase 1 built.

### Does Phase 2 Change the Product?

Phase 2 adds product lines; it does not change the format. The guide format validated in Phase 1 (zone-specific field guide, PDF, Etsy digital download, $18–$28 price point) applies unchanged to Phase 2. New additions:

- Premium guide bundle tier at $35–$45 (3 guides bundled at a discount — viable if Phase 1 establishes 2%+ conversion)
- Potential ebook compilation of 10+ guides at a flat rate ($49–$69) — viable as Phase 2 closes and Phase 3 opens
- Consultation add-on (email Q&A, 30 min call) — evaluate only if email engagement data shows sustained practitioner audience

### Four-Week Phase 2 Prep Sprint (Once Gate Cleared)

If the Day 14 gate clears, this four-week window (June 17 – July 13) is the production sprint:

**Week 1 (June 17–21): Infrastructure prep**
- Kit Creator upgrade confirmed
- Phase 2 herbalist automation loaded (8-email sequence, pre-built)
- Canva Phase 3 palette loaded (hard deadline June 22)
- All Phase 2 species audited for Wikimedia Commons availability
- 20 social posts pre-scheduled (covers full sprint period)

**Week 2 (June 22–28): First bundle**
- Women's Health / Respiratory bundle — 3 species guides written and QA'd
- Etsy listing drafted (title, description, tags ready for upload)
- Day 1 of sprint: upload to Etsy and Kit sequence activates for new subscribers

**Week 3 (June 29 – July 5): Second bundle**
- Sleep + Nervines bundle — 3 species guides written and QA'd
- Upload to Etsy
- Email broadcast to Phase 1 list announcing Phase 2 availability

**Week 4 (July 6–13): Third bundle + review**
- Third bundle (Digestive Health or Immune Support) — written and uploaded
- Day 30 data review: is Phase 2 revenue trajectory justifying a September/October sprint?
- Community builder candidate list assessed for Phase 3 recruitment

---

## Section 3: Operational Overlap Analysis — Can Phase 1 and Phase 2 Run in Parallel?

The short answer is yes, with one bandwidth constraint that requires deliberate management.

### Content Production Bandwidth

Phase 1 monitoring requires approximately 10 minutes per day during the first 14 days. After Day 14, it drops to 5 minutes per day. Phase 2 writing requires 4–6 hours per sprint day. These do not conflict — they occupy different time blocks (morning monitoring vs. afternoon writing).

The one genuine conflict: social media management. Phase 1 requires active social presence (1–2 posts per day during launch week, then 4–5 posts per week). Phase 2 writing during the 22-day sprint requires 6–8 hours per day of focused work that is incompatible with managing live social accounts.

**Resolution**: Pre-schedule 2 weeks of Phase 1 social posts (using Buffer or Later) before the Phase 2 sprint starts. This has already been templated — the TRACK_B_SOCIAL_CALENDAR_MAY28_30.md and Phase 2 social content bank provide ready-to-schedule posts. Pre-scheduling eliminates the daily social management overhead during the sprint.

### Email Marketing: Kit Automation Bandwidth

Phase 1 is running a 5-email welcome sequence (Zone Quick-Start Card onboarding, Days 0–14). Phase 2 requires a separate automation for the medicinal herb subscriber cohort.

**Kit free tier** allows one automation slot. Running Phase 1 and Phase 2 automations simultaneously requires Kit Creator ($33/month billed annually). This is the binding platform constraint — not subscriber count, not storage, not sends. The Creator tier must be in place before Phase 2 automation can run.

The two sequences do not conflict in content (they serve different subscriber cohorts), but they cannot both run on the free tier. The Kit upgrade is a prerequisite for simultaneous Phase 1/2 email operations, not just a Phase 2 nice-to-have.

Phase 1 subscribers who indicate interest in medicinal herbs (via the Day 10 survey or by clicking an herb-related link) are tagged `medicinal-herbs` and routed into the Phase 2 herbalist sequence automatically when it activates. Subscribers who do not click herb-related content remain in the Phase 1 zone-card onboarding track. The two sequences share the same subscriber list but operate on different cohort tags — no conflict, but requires Creator automation capabilities.

### Etsy Shop Focus: Does Phase 2 Dilute Phase 1 Organic Reach?

Adding Phase 2 listings to the Etsy shop does not hurt Phase 1 listing performance. Etsy's search algorithm ranks each listing independently. A shop with 8 listings does not dilute the traffic of a listing with 2 listings. If anything, more listings create more entry points — a customer finding the medicinal herbs guide may navigate to the wild edibles guide through the shop page.

The only risk is shop coherence: if Phase 2 listings are poorly tagged or misaligned with the shop's established category, they could drag down the shop's overall conversion rate metric (which Etsy uses in search ranking). Mitigation: Phase 2 listings use the same tag structure and SEO optimization standards as Phase 1, not a rushed upload.

### Social Media: Does Phase 2 Require More Social?

Path B (social-first launch) adds Instagram, TikTok, and Pinterest to Phase 1. Phase 2 does not add channels — it adds content volume on the same channels. The Phase 2 social content (medicinal herb identification videos, seasonal content, UGC campaigns) flows through the same accounts and scheduling tools established in Phase 1.

The Phase 2 content calendar (documented in SEEDWARDEN_PHASE_2_CONTENT_ROADMAP.md) runs 4–5 posts per week across all three platforms — identical cadence to Phase 1. No additional social management bandwidth is required. The difference is content topic: Phase 1 social focuses on zone cards and wild edibles; Phase 2 shifts emphasis to medicinal herbs and preservation while maintaining the evergreen content rotation.

---

## Section 4: Risk Scenarios

### Slow Growth — Fewer Than 10 Orders in 30 Days

**Definition**: Day 30 data shows fewer than 10 Etsy orders AND email subscriber count under 25 AND no community shares.

**Probability**: Moderate for Path A solo without external promotion. Lower for Path B or dual-track.

**Phase 2 response**: Defer the Phase 2 writing sprint to August. Do not stop Phase 2 work entirely — use the gap period to complete the Wikimedia Commons audit, pre-write guide outlines, and audit photography needs for the August field window. An August sprint still produces 3 bundles by September, ahead of the fall gardening content peak (second-highest Etsy traffic window after April–May).

**Alternative path if Etsy channel remains cold**: Phase 2 medicinal herbs bundles have strong SEO potential independent of a warm email list. A cold Etsy launch (3 bundles with strong tags, no social promotion) converts more slowly but requires no subscriber threshold. If Phase 1 email list is small, the Etsy cold-discovery path for Phase 2 is viable — it just takes 6–8 weeks longer to accumulate reviews.

### Moderate Growth — 20–50 Orders in First 30 Days

**Definition**: 20–50 Etsy orders in Month 1 AND email subscribers in the 25–74 range AND at least 1 community share.

**Probability**: Most likely outcome for Path B or dual-track with consistent social execution.

**Phase 2 response**: Phase 2 greenlit for August content production (not June 22). Use July for:
- Completing the Wikimedia Commons audit
- Photographing any species in the summer window that require original photos
- Outlining all 18+ Phase 2 species guides
- Building Phase 2 email sequences in Kit

Launch Phase 2 writing sprint August 1–21. Three bundles uploaded by August 31. Etsy reviews from Phase 1 buyers provide social proof for Phase 2 listings at launch.

### Fast Growth — 50+ Orders in First 30 Days

**Definition**: 50+ Etsy orders in Month 1 OR Kit subscribers exceeding 75 before Day 14 OR email open rate above 35%.

**Probability**: Low-moderate for Path B with influencer amplification.

**Phase 2 response**: Accelerate Phase 2 to June 22 writing sprint as planned. If Etsy sales exceed 30 units in the first 14 days, consider listing 1–2 Phase 2 bundles as pre-sales with stated delivery dates 3–4 weeks out. Pre-sale listings capture buyer intent before Phase 2 writing is complete — but only if the stated delivery date is achievable.

**What cannot be accelerated**: Writing quality. The 36–44 hour estimate for the Phase 2 writing sprint is a minimum, not a maximum. Fast Phase 1 growth does not justify inferior Phase 2 content. Negative Etsy reviews from rushed Phase 2 bundles compound directly into Phase 3 pricing power and the practitioner tier.

**Supply chain note for fast growth**: Digital delivery is unlimited. Etsy handles 500 downloads as easily as 5. The only genuine constraint at fast-growth scale is Kit email throughput — if the subscriber list exceeds 10,000, Kit Creator is required ($39/month). At 10,001 subscribers, automated delivery continues uninterrupted; only the billing tier changes.

### Overwhelm Scenario — Phase 1 Succeeds Faster Than Content Production Can Follow

**Definition**: Demand exceeds content supply — Phase 1 buyers exhaust the existing guide catalog before Phase 2 is ready, leading to flat revenue and stalled list growth.

**Probability**: Low in the first 60 days given the Phase 1 catalog size. Risk increases if a viral post drives a traffic spike.

**Response**: List Phase 2 bundles as pre-orders with honest delivery dates. The herbalism community has demonstrated tolerance for advance purchases from credible creators when the content quality is established. A 2–3 week delivery window on a pre-order is acceptable if it is clearly stated and delivered on time. Do not list a pre-order and miss the delivery date.

---

## Section 5: Data Collection Checklist — What to Measure in Phase 1

The following data must be collected during Phase 1 to inform the Phase 2 GO/NO-GO decision. Most is available directly from Etsy Stats and Kit dashboards with no additional tooling.

### Email Data (Kit Dashboard — Daily)

- [ ] Subscriber count (absolute and daily delta)
- [ ] Email 1 open rate (48-hour settled figure)
- [ ] Email 1 click-through rate (link clicks / delivered)
- [ ] Email 3 and Email 4 click-through rates (Etsy product page visits from email)
- [ ] Unsubscribe rate per email (healthy: under 0.5% per send)
- [ ] Reply count per email (direct qualitative signal — every reply is recorded manually)

### Etsy Data (Shop Manager — Daily in Week 1, Then Weekly)

- [ ] Views per listing (daily delta)
- [ ] Conversion rate per listing (orders / views — calculate manually)
- [ ] Total orders (cumulative)
- [ ] Revenue (gross, before Etsy fees)
- [ ] Traffic source breakdown (Etsy search vs. social vs. direct — available in Etsy Stats)
- [ ] Review count and star rating (monitor after Day 7 when first reviews may arrive)

### Social Data (Platform Insights — Daily in Week 1, Then 3x/Week)

- [ ] Instagram: reach per post, saves per post, profile visits, follower count
- [ ] TikTok: views per video, completion rate (available in TikTok Analytics), follows from video
- [ ] Pinterest: impressions, outbound clicks (to Kit landing page or Etsy)

### Qualitative Data (Manual Collection — Record in WORKLOG.md)

- [ ] Influencer responses: name, platform, response content, level of interest
- [ ] Community shares: platform, account name, estimated reach, content of share
- [ ] Email replies: subscriber name, content, category (question / praise / feature request)
- [ ] Comments indicating purchase intent ("where can I buy this?", "is there a guide for Zone 4?")
- [ ] Comments requesting specific content not yet produced (Phase 2 content gap signals)

### Phase 2 Scope Decision Data (Collect by Day 14)

- [ ] Which species or topics received the most direct requests (in comments, replies, or DMs)?
- [ ] Which Etsy listing received the most views as a percentage of total shop views?
- [ ] Which email subject line had the highest open rate?
- [ ] Did any influencer or community member specifically endorse the medicinal herbs direction vs. the wild edibles direction?

The answers to the scope decision questions determine whether Phase 2 prioritizes medicinal herbs first (high community signal) or expands wild edibles first (high Etsy signal). This data cannot be guessed in advance — it must be collected from the live Phase 1 run.

---

## Decision Framework

**Single-gate decision logic for Phase 2 activation:**

Phase 2 writing sprint is approved when, at Day 14 post-launch:

```
IF (G1 ≥ 25 subscribers) AND (G2 ≥ 15% open rate)
    → Phase 2 writing sprint GREENLIT
    → Kit Creator upgrade: REQUIRED before sprint starts
    → Sprint start: no later than Day 21 (7 days after gate)

IF (G1 ≥ 75 subscribers) AND (G2 ≥ 25% open rate)
    → Full Phase 2 scope (5 bundles, collaborator recruitment open)
    → Sprint start: Day 14 + 7 days

IF (G1 < 25 subscribers) OR (G2 < 15% open rate)
    → Hold sprint
    → Run rapid-distribution push for 14 days
    → Re-evaluate at Day 30 using same thresholds
    → If Day 30 still below threshold: defer to August sprint

OVERRIDE: Phase 2 greenlit regardless of G1/G2 IF:
    (a) Email 1 open rate > 35% on any list size, OR
    (b) 3+ influencer shares with confirmed clicks, OR
    (c) Any single Etsy listing conversion rate > 5%
```

**Phase 2 scope calibration (once sprint is approved):**

| Phase 1 Outcome | Phase 2 Scope | Collaborators | Sprint Duration |
|-----------------|---------------|---------------|-----------------|
| 25–49 subscribers, 15–24% open | 3 bundles (10 guides) | None | 22 days |
| 50–99 subscribers, 25%+ open | 5 bundles (18 guides) | None or 1 | 22–28 days |
| 100+ subscribers, 25%+ open | 5+ bundles (20+ guides) | 1–2 | 28 days |
| Any override condition | 5 bundles minimum | Evaluate based on revenue | ASAP |

**Phase 2 deferral conditions:**

| Trigger | Meaning | Action |
|---------|---------|--------|
| G1 < 25 at Day 30 AND G2 < 15% | List too small and quality too low | Defer to August; run list-building push |
| Etsy verification hold on new listings | Platform risk active | Activate Gumroad backup; 7-day resolution deadline |
| Kit delivery rate below 90% | Spam placement risk | Pause list growth; fix sending domain config |
| TikTok reach drops to near-zero | Platform risk | Shift social to Instagram/Pinterest; do not rebuild TikTok as primary |

---

## Section 6: Supply Chain Impact

### Phase 2 Is Entirely Digital

Phase 2 as currently defined involves no physical product component. Every guide is a PDF digital download delivered automatically by Etsy. Fulfillment overhead per additional order is zero. Phase 2 adding 20–30 new listings does not add fulfillment complexity.

Etsy fee structure at Phase 2 scale:

| Fee | Rate | At 30 guides uploaded |
|-----|------|----------------------|
| Listing fee | $0.20/listing | $6.00 total — negligible |
| Transaction fee | 6.5% of sale price | $1.43 per $22 sale |
| Payment processing | ~3% + $0.25 | ~$0.91 per $22 sale |
| Net margin per $22 sale | ~$19.66 | 89% net margin |

**Offsite Ads threshold**: Once cumulative Etsy sales exceed $10,000 in any 365-day window, Offsite Ads participation is mandatory for the lifetime of the shop. At $22/guide, this threshold is crossed at approximately 455 sales. At 15+ sales per day during Phase 2 peak, the $10K threshold can be reached in 30 days. This is a Phase 2 planning milestone, not a risk.

### Phase 3 Physical Products — When Supply Chain Matters

If Phase 3 or Phase 4 introduces physical products (printed guides, seed packets, merchandise), the supply chain model changes entirely. Before any physical product launches:

- Select and test a print-on-demand partner (Lulu, Blurb, or IngramSpark) with a single test order. Lulu's 6×9 full-color paperback: approximately $8–$12 per copy at 200 pages. Retail at $24–$28 yields 50–60% margin after printing.
- Production lead time to customer: 7–14 days (3–7 manufacturing, 2–5 shipping). Not compatible with the instant-download expectation. State delivery windows explicitly in every physical listing.
- Inventory risk: print-on-demand eliminates inventory risk entirely at the cost of per-unit margin. Only consider bulk physical printing when monthly order volume exceeds 100 units consistently.

**Recommendation**: Stay digital-only through Phase 2 (Q4 2026). Evaluate physical products as a Phase 3 initiative after the digital catalogue is complete and Etsy reviews provide social proof.

### 3D Printing / mfg-Farm Intersection

The mfg-farm 3D printing operation represents a potential manufacturing resource for Phase 3 physical product development. There are three viable intersection points:

**Intersection 1 — Seed packet display stands and retail fixtures**. If seedwarden expands to wholesale or retail (craft fair, herbalist supply stores), 3D-printed display fixtures — seed packet holders, label stands, guide display racks — have low material cost and high customizability. These are not viable as Phase 2 products because the channel does not yet exist, but they are Phase 3 production-ready if wholesale distribution is pursued.

**Intersection 2 — Plant identification tools and educational props**. 3D-printed plant morphology teaching aids (cross-section models, seed anatomy models) are an underdeveloped product category in the native plant education space. There is no direct Etsy competitor at present. These are slow to produce (2–4 hours per unit print time), not easily scalable, and require significant upfront design work — viable as a premium add-on to a practitioner tier at Phase 4 pricing ($45–$65 per model), not as a Phase 2 product.

**Intersection 3 — Branded packaging for physical seed or herb kit bundles**. If seedwarden eventually sells physical seed kits (curated seed packets for specific growing zones), 3D-printed branded packaging inserts, herb label clips, or seed organizers could differentiate the product from generic seed packet competitors. This is a Phase 4 idea: the economics only work when order volume justifies the print time investment and the brand has established the premium positioning.

**Current assessment**: No mfg-farm production capacity should be committed to seedwarden during Phase 1 or Phase 2. The digital product model has far superior economics (zero variable cost per sale) and the 3D-printed physical product layer adds complexity without improving margins at Phase 2 scale. Document the intersection points now for Phase 3 and Phase 4 planning, and revisit when Phase 2 catalogue is complete and monthly revenue exceeds $2,000.

**Economies of scale potential**: When seedwarden reaches Phase 3 wholesale or Phase 4 physical product stage, the mfg-farm printing infrastructure avoids the minimum order requirements of third-party injection-molded packaging (typically 500–5,000 units per SKU). This is a meaningful capital advantage for a product launch at 50–200 units. The break-even analysis at that point: mfg-farm print cost vs. offshore minimum-order cost vs. print-on-demand supplier margin. Run this analysis before Phase 3 physical product commitment.

---

## Appendix: Phase 2 Content Gap Analysis

### Current Phase 1 Catalogue (Post-Bundle E)

Phase 1 launched with:
- Zone Quick-Start Card (8 zones, Zones 3–10) — free lead magnet
- Bundle E: 5 wild edibles species guides (launched June 2026)
- Companion planting chart
- Food sovereignty starter guide

**Total paid SKUs at Phase 1 close**: 7 Etsy listings across the catalogue.

### Phase 2 Content Gap — Species Requiring Guides

The following species have been prioritized in PHASE_2_GUIDE_CONTENT_BLUEPRINT.md but not yet produced. Organized by production urgency:

**Tier 1 — Write First (22-day sprint, June 22 – July 13)**

These 8 species have the highest Etsy search demand, the clearest safety content angles, and align with the medicinal herbs bundle structure:

| Species | Common Name | Bundle Target | Key Gap |
|---------|-------------|--------------|---------|
| *Urtica dioica* | Stinging Nettle | Respiratory / Allergy | Harvest safety (gloves, timing) not illustrated |
| *Sambucus canadensis* | American Elderberry | Immune / Respiratory | Berry toxicity vs. flower safety distinction thin |
| *Hypericum perforatum* | St. John's Wort | Sleep + Mood | Drug interactions are the primary safety content gap |
| *Matricaria chamomilla* | Chamomile | Sleep + Nervines | Ragweed allergy cross-reactivity not documented in existing guides |
| *Valeriana officinalis* | Valerian | Sleep + Nervines | No entry in Phase 1; cultivation from root division undocumented |
| *Echinacea purpurea* | Purple Coneflower | Immune | 3-year grow-from-seed timeline requires illustration |
| *Achillea millefolium* | Common Yarrow | Wound / Inflammation | Harvest stage (first flower head) requires photo documentation |
| *Mentha* spp. | Wild Mint complex | Digestive | Species differentiation (spearmint vs. peppermint vs. water mint) requires ID chart |

**Tier 2 — Write July–September (Second Production Sprint)**

These 12 species are summer-peak or fall-peak, with field photography windows that align with the summer 2026 botanical window:

| Species | Common Name | Season | Notes |
|---------|-------------|--------|-------|
| *Solidago* spp. | Goldenrod | August | Allergy myth-busting angle is the highest-reach content opportunity |
| *Monarda fistulosa* | Wild Bergamot | July | Edible + medicinal dual-use; native bee content overlap |
| *Rubus occidentalis* | Black Raspberry | July | Short harvest window; urgency content |
| *Crataegus* spp. | Hawthorn | August–September | Berry ID guide; thorns and harvest method |
| *Asarum canadense* | Wild Ginger | August | Seed collection window; seed saving content |
| *Actaea racemosa* | Black Cohosh | September | Phase 3 medicinal bridge species |
| *Verbascum thapsus* | Mullein | July–August | Highly photogenic; respiratory herb with strong search demand |
| *Symphytum officinale* | Comfrey | July | External use vs. internal use safety distinction critical |
| *Glycyrrhiza glabra* | Licorice Root | (Cultivation guide) | No wild harvest possible; cultivation guide format |
| *Hydrastis canadensis* | Goldenseal | September | Threatened status; ethical sourcing guide is the content angle |
| *Lobelia inflata* | Indian Tobacco | August | Safety-critical; narrow therapeutic window requires detailed dosing note |
| *Asclepias syriaca* | Common Milkweed | July | Edible stages (shoots, flowers, pods) not documented; monarch context |

**Tier 3 — Phase 3 Integration Species (not new, cross-reference only)**

These medicinal species are covered by the Phase 3 photography and guide pipeline. They require cross-reference links from Phase 2 guides but not new standalone Phase 2 content:

American Ginseng, Bloodroot, False Unicorn, Red Clover, Ramps (medicinal context), Wild Bergamot (medicinal context — shared with Tier 2 above, so write once and cross-reference)

### Topic Gaps Beyond Species Guides

Phase 2 also addresses the following content gaps that are not species-specific:

| Gap | Format | Priority | Notes |
|-----|--------|----------|-------|
| Drug interaction reference card | PDF infographic | HIGH | St. John's Wort, Echinacea, Valerian are the three most requested; this is also the most shareable safety content in the herbalism niche |
| Zone-specific growing calendar (medicinal herbs) | PDF, 8-zone format | HIGH | Parallel to Zone Quick-Start Card; same format, medicinal focus |
| Seed saving guide (medicinal herbs specific) | Full guide | MEDIUM | Complements existing Seed Saving Field Manual; references Phase 2 species |
| Harvest and preservation by season | Reference card | MEDIUM | Connects Phase 2 guides to the homesteader preservation audience |
| "Start here" guide for medicinal herb gardeners | Landing guide | MEDIUM | The lead magnet for the Phase 2 herbalist subscriber track |

### Summary Count

| Tier | Species | Additional topics | Total content items |
|------|---------|-------------------|---------------------|
| Phase 2 Tier 1 (sprint) | 8 | 1 (drug interaction card) | 9 |
| Phase 2 Tier 2 (autumn sprint) | 12 | 3 | 15 |
| Phase 2 Tier 3 (cross-reference only) | 6 | — | 6 (no new production) |
| **Phase 2 total new production** | **20** | **4** | **24 content items** |

At 5–8 hours per guide (including Canva design with Wikimedia CC images), the 24-item Phase 2 content backlog represents approximately 120–192 hours of production work. Distributed across the June 22 sprint (22 days) and an October sprint (15 days), this is manageable at 3–5 hours per day in sprint mode. Without sprint windows, at steady-state 2 hours per day, Phase 2 completes by December 31, 2026.

---

## Infrastructure Pre-Phase 2 Checklist

Complete before Phase 2 sprint begins (target: June 21, 2026):

**Email infrastructure**
- [ ] Kit Creator upgrade confirmed ($33/month billed annually)
- [ ] Phase 2 herbalist welcome sequence loaded (8 emails, pre-built)
- [ ] Herbalist tag routing confirmed (`medicinal-herbs` tag triggers Phase 2 sequence)
- [ ] Kit sending domain verified with SPF/DKIM

**Etsy**
- [ ] Account verification status confirmed with Etsy support (no pending holds on new digital downloads)
- [ ] Payment account active (no outstanding payment holds)
- [ ] Phase 2 listing templates drafted (title, description, tags) for all 3 Phase 2 bundles
- [ ] Backup distribution channel (Gumroad or Payhip) operational with at least one test product

**Social media**
- [ ] All social accounts (Instagram, TikTok, Pinterest) active and posting history established
- [ ] 20 social post templates loaded and pre-scheduled through July 13 sprint close
- [ ] Pinterest boards created for Phase 2 content categories

**Content production**
- [ ] All 20 Phase 2 species audited against Wikimedia Commons
- [ ] Species requiring original photography: field session scheduled before July 15
- [ ] Canva Phase 3 palette loaded (June 22 hard deadline)
- [ ] QA checklist adapted for medicinal herbs safety profile (drug interactions section required)

**Financial**
- [ ] Kit Creator cost ($33/month) included in Phase 2 operating cost projection
- [ ] Break-even: 1.5 bundle sales per month at $22/bundle covers Kit Creator cost

---

*Prepared: June 4, 2026 by research-agent (claude-sonnet-4-6)*
*Version 5.0 — supersedes v4.0 (June 4, 2026), v3.0, v2.0, v1.0*
*Track-agnostic: applies to Path A (Etsy-first), Path B (social-first), or both executing concurrently*
*Cross-references: SEEDWARDEN_PHASE_2_CONTENT_ROADMAP.md, PHASE_2_GUIDE_CONTENT_BLUEPRINT.md, GATE_1_SUCCESS_METRICS_AND_MONITORING.md, COMMUNITY_BUILDER_RECRUITMENT_FRAMEWORK.md*
