---
title: "Seedwarden Growth Metrics & Cohort Analysis Framework"
date: 2026-04-27
status: ready-to-implement
phase: Phase-1-launch-and-post-Phase-1-analysis
tags: [seedwarden, analytics, cohort-analysis, ltv, cac, email-metrics, growth]
---

# Seedwarden Growth Metrics & Cohort Analysis Framework

**Purpose**: This document defines how Seedwarden measures growth, segments customers into analytically useful cohorts, and interprets the resulting data to improve product mix, email sequencing, and advertising decisions. It is written for Phase 1 launch conditions (low data volume, manual tracking) and designed to scale into Phase 2 and beyond without requiring a rebuild. Frameworks are adapted from SaaS cohort analysis practice (Amplitude, Mixpanel patterns) and calibrated for a digital-product Etsy seller with email-driven repeat purchases and a strongly seasonal demand structure.

---

## 1. Customer Cohort Segmentation

Cohort analysis groups customers by a shared characteristic at a shared point in time, then tracks how each group behaves over subsequent periods. For Seedwarden, the most actionable cohort dimensions are: acquisition channel, first product purchased, behavioral engagement tier, and seasonal acquisition window. These four dimensions cut across each other and reveal patterns that aggregate metrics hide.

### Acquisition Channel Cohorts

Every customer enters through one of four channels. Tracking which channel each cohort came from is the foundation of every other analysis.

**Channel A: Etsy organic search.** Buyer discovered the listing through Etsy search (no prior social or email relationship). This is the largest cohort at launch and the one most dependent on listing SEO. Etsy organic buyers have the lowest acquisition cost (zero) but also no prior brand relationship, making them the highest-risk cohort for churn after the first purchase. Their conversion depends entirely on the listing quality at the moment of discovery.

**Channel B: Email list (lead magnet subscribers).** Buyers who signed up for the Zone Quick-Start Card or 5-variety guide before purchasing. This cohort has a pre-existing trust relationship and is exposed to the welcome sequence before they buy. Expected to have higher average order values and higher second-purchase rates than Etsy organic cohort because the email sequence warms them toward bundles rather than individual low-price products.

**Channel C: Social media referral.** TikTok, Instagram, or Pinterest traffic that clicked through to an Etsy listing. Tracked via UTM parameters appended to all bio links and pins. This cohort's conversion rate on the first visit is typically lower than email cohorts but higher than cold Etsy search for some platforms (particularly Pinterest, which carries purchase intent).

**Channel D: Influencer or affiliate referral.** Buyers who arrived via a creator's affiliate link or discount code. This cohort is trackable by the unique code used at checkout. Useful for calculating influencer-specific LTV and deciding whether to renew partnerships.

### First-Product Cohorts

The first product a customer purchases predicts their subsequent buying behavior better than any other single variable. In digital product businesses, the first product establishes a reference point for what the seller offers and a trust floor for subsequent purchases.

**Entry-price cohort ($5–$9).** First purchase was Companion Planting Chart ($5), Apartment Seed Starting Kit ($9), 12-Month Urban Growing Planner ($7), Food Sovereignty Starter Guide ($8), or Zone-by-Zone Seed Starting Calendar ($8). These buyers responded to low-risk pricing. The key question for this cohort: what percentage upgrade to a mid-price individual product or bundle within 90 days? If the answer is under 15%, the welcome sequence email cross-sell is underperforming and needs revision.

**Mid-price cohort ($10–$15).** First purchase was Anti-Catalog, Seed Swap Kit, Container Growing Blueprint, Fermented Harvest, Apartment Plant Catalog, or similar. These buyers demonstrated higher initial willingness to pay and likely arrived with clearer intent. This cohort has a stronger correlation with bundle purchase behavior in the subsequent 60 days.

**Premium cohort ($16–$22).** First purchase was Survival Garden Regional Plans ($22), Hunting/Fishing Manual ($20), Livestock Manual ($18), or Native Plants Guide ($18). This is the highest-LTV seed cohort — buyers willing to spend $18–$22 on their first purchase from an unknown seller have high trust or strong intent, and they respond well to VIP treatment (early access, exclusive pricing).

**Bundle-first cohort.** Buyer's first purchase was a bundle ($28–$50). This cohort has the highest first-transaction AOV and typically represents either a gift buyer (purchasing for someone else, uncorrelated with subsequent purchases) or a committed self-purchaser (high intent, likely to become a repeat buyer). These two sub-cohorts behave very differently and should be separated by seasonal acquisition window: November–December bundle buyers are predominantly gift buyers; January–April bundle buyers are predominantly self-purchasers.

### Email Engagement Cohorts

Every subscriber is simultaneously in an acquisition channel cohort and an engagement cohort. The engagement cohort tracks how the subscriber interacts with emails over time.

**Engaged subscribers (open rate above 30% over trailing 8 sends).** This is the core monetizable segment. Kit's subscriber activity data allows filtering for this group. Engaged subscribers should receive all newsletters, seasonal broadcasts, and VIP early-access offers. They are the primary target for new product launch emails.

**Warming subscribers (open rate 15–30%).** Subscribers who occasionally engage but are not consistent. These subscribers respond well to content-first emails (educational, no product pitch in subject line). They should be excluded from high-frequency promotional sends that might push them toward unsubscribe. One promotional email per month maximum.

**Cold subscribers (open rate under 15% over trailing 6 sends).** These subscribers trigger Automation 4 (win-back campaign). Kit's automation can identify and tag this group automatically. Cold subscribers who do not re-engage within 90 days should be removed from the active list. A list of 800 engaged subscribers is operationally more valuable than 2,000 mixed-engagement subscribers because inbox placement degrades when open rates are consistently low.

**Behavioral tag cohorts.** Subscribers who clicked category-specific links in Emails 3 and 4 of the welcome sequence are tagged: Seed Saver, City Grower, or Preservationist. These tags create product-affinity cohorts that receive segment-specific newsletter content and are the primary targeting layer for seasonal broadcast campaigns. A Seed Saver-tagged subscriber receives a different product spotlight in the August newsletter than a Preservationist-tagged subscriber. Track conversion rates to purchase separately for each tag to identify which segment has the strongest email-to-purchase conversion.

### Seasonal Acquisition Window Cohorts

The seasonal acquisition window when a customer first purchased predicts the products they will want in subsequent seasons and calibrates re-engagement timing.

**Spring planning cohort (January–April acquisitions).** These buyers arrived during peak gardening planning season. Their reference product was likely a zone calendar, seed starting guide, or planting planner. They will be in-market again the following January–March. The correct re-engagement campaign for this cohort is a November email about planning ahead for the next growing season, not a preservation-focused campaign in August.

**Preservation season cohort (July–September acquisitions).** Buyers motivated by harvest and preservation content. They arrived via Fermented Harvest, Harvest Preservation, or similar entry points. They are in-market again the following July. Email them a "canning season is here" broadcast in early July. Do not feature spring planting guides to this cohort in January — they have lower intent for that content.

**Holiday gift cohort (November–December acquisitions).** The gift buyer cohort is the most behaviorally distinct. Approximately half purchased for themselves, half as gifts. The gift-buyer sub-cohort has near-zero repeat purchase probability (the recipient, not the purchaser, would need to return). The self-purchaser sub-cohort has normal repeat purchase potential. Differentiating them is difficult without survey data, but a proxy exists: if a December buyer's shipping name differs from their billing name, they are likely a gift buyer. Track this cohort's second-purchase rate separately — it will be the lowest of all seasonal cohorts and should not be used to assess general customer health.

**Long-tail cohort (May–June, October acquisitions).** Buyers who arrived outside the three main peaks. These cohorts tend to be more intent-driven (searching for something specific, found Seedwarden, purchased) rather than seasonally motivated. They have moderate repeat purchase rates and respond well to the post-purchase cross-sell sequence.

---

## 2. LTV, CAC, and Payback Period Calculations

For a digital product seller with near-100% gross margin and email-driven repeat purchases, LTV and CAC calculations must be adapted from physical-product e-commerce conventions. The key adjustments: no COGS to subtract beyond payment processing fees (Etsy takes approximately 6.5% transaction fee), email is the primary repeat-purchase driver rather than paid retargeting, and seasonal demand creates lumpy LTV rather than smooth monthly recurring revenue.

### Gross Margin Baseline

Before calculating LTV, establish the true net margin per product. Etsy fee structure: $0.20 listing fee per renewal (every 4 months per unit sold), 6.5% transaction fee, 3% + $0.25 payment processing fee. Total Etsy cost on a $13.50 average sale: approximately $1.40, or 10.4% of revenue. Net margin on digital products after Etsy fees: approximately 89.6%. This is the margin baseline for all LTV calculations. Bundles have identical percentage cost structure but higher absolute revenue per transaction — a $38 Preservation Bundle nets approximately $34.05 after fees. The "52% margin vs. 29% margin" framing from manufacturing research applies to physical product bundles; for digital products, all items approach the same near-100% gross margin floor, making bundle strategy about revenue-per-transaction uplift rather than margin improvement.

### LTV Calculation by Cohort

LTV (Lifetime Value) = average order value x purchase frequency x customer lifespan.

For Seedwarden, average order value (AOV) varies significantly by first-product cohort:

- Entry-price first purchasers: AOV on first transaction ~$8. If they purchase again (targeting 25% second-purchase rate), second transaction AOV is ~$16 (weighted toward mid-price products). LTV at 24-month horizon: $8 + (0.25 x $16) + (0.08 x $35) = ~$14.80.
- Mid-price first purchasers: AOV on first transaction ~$12. Second-purchase rate target 30%. LTV at 24-month horizon: $12 + (0.30 x $20) + (0.10 x $38) = ~$21.80.
- Premium first purchasers: AOV ~$19. Second-purchase rate target 35%. LTV at 24-month horizon: $19 + (0.35 x $22) + (0.12 x $40) = ~$31.50.
- Bundle-first purchasers (self-purchaser sub-cohort): AOV ~$38. Second-purchase rate target 20% (catalog coverage means less room for repeat). LTV: $38 + (0.20 x $25) = ~$43.
- Bundle-first purchasers (gift buyer sub-cohort): LTV equals first transaction only ~$38. No meaningful second-purchase signal.

These LTV estimates should be updated quarterly once 90-day and 180-day purchase data is available. The email post-purchase sequence (Day 7 cross-sell email) is the primary lever for moving subscribers from the low-LTV to mid-LTV bucket — it is the most important single automation to test and optimize.

### CAC Calculation

CAC (Customer Acquisition Cost) = total marketing spend / number of new customers acquired in the same period.

For Seedwarden's Phase 3 channel mix, CAC breaks down by channel:

**Etsy organic: CAC = $0.20 per listing renewal / units sold from that listing.** A listing selling 8 units per month (one renewal every 4 months amortized) contributes $0.025 per sale in listing cost. Effectively zero CAC. This is the best-margin acquisition channel.

**Etsy internal ads: CAC = ad spend / purchases attributable to ads.** At the benchmark ROAS of 2.5x on a $12 average product, the implied CAC is $4.80. Break-even CAC for Etsy ads = net product revenue / 1 = ~$11 (since margin is ~89%). A $4.80 CAC on an $11 net product sale is comfortable and sustainable.

**Pinterest ads: CAC = ~$8.00 (category benchmark).** At $12 average product price, this produces approximately 1.5x ROAS on the first transaction. Marginally profitable on first purchase, profitable when second-purchase LTV is included. Target audience: buyers whose first-purchase LTV is above $20 (mid-price or premium cohorts) to ensure positive 24-month returns.

**Email list (lead magnet): CAC = cost to acquire email subscriber / email-to-purchase conversion rate.** If lead magnet promotes via TikTok bio (zero marginal cost) and 15% of subscribers purchase within 90 days (target from email sequence performance), the implied CAC per customer from email = $0 acquisition cost / 0.15 = $0. But in practice, time cost of content creation that drives bio-link clicks should be attributed. Estimate conservatively: if 2 hours/week of content creation yields 20 new subscribers/week and 3 purchases/week (15% conversion), the implicit CAC is (2 hours x $25 shadow wage) / 3 purchases = $16.67 per customer. This is the email channel's true cost and should be compared against product LTV of $14.80–$31.50 depending on cohort.

**Influencer partnerships: CAC = (flat fee + gifting cost + commission per sale) / total sales attributed.** At $200 flat fee + $30 gifting cost + 20% commission per sale, if a partnership generates 15 sales at $13.50 average: CAC = ($200 + $30 + $40.50) / 15 = $18.03. This is above the entry-price cohort LTV ($14.80) but below mid-price cohort LTV ($21.80). Only run flat-fee influencer partnerships when the expected average sale price is above $18.

### Payback Period

Payback period = CAC / (net revenue per customer per month).

Because Seedwarden customers do not pay monthly subscriptions, payback is calculated differently: CAC is recovered when cumulative revenue from the customer exceeds acquisition cost.

- Etsy organic acquisition: Payback period = near-instant. First transaction recovers the $0.02–$0.20 listing cost.
- Etsy ad acquisition at $4.80 CAC: Recovered on first purchase (net $11 on a $12 product). Payback period = one transaction.
- Pinterest ad acquisition at $8.00 CAC: Recovered on first purchase for products above $9. For $5–$8 products, requires a second purchase. Do not run Pinterest ads for the $5 Companion Planting Chart — CAC would exceed single-transaction LTV for that product.
- Influencer acquisition at $18.03 CAC: Recovered when the customer reaches $20+ in cumulative spending. For an entry-price first buyer, this requires one additional purchase. For a mid-price or bundle first buyer, recovered on second purchase. Track influencer cohort second-purchase rate separately to verify recovery.

---

## 3. Product-Level Cohort Analysis

Not all products serve the same role in the customer journey. Product-level cohort analysis answers two questions: which products lead to repeat purchases, and which products attract one-time buyers?

### Repeat-Purchase Driver Products

These are products that frequently appear as the first purchase in a sequence that includes a second purchase within 90 days. They have "gateway" characteristics: entry pricing, broad appeal, or content that reveals adjacent needs clearly enough to drive exploration of related products.

**Expected repeat-purchase drivers:**
- Food Sovereignty Starter Guide ($8): Short, accessible, and explicitly political. Buyers who finish it are primed for the Seed Saving Field Manual and Anti-Catalog because those are named in the guide's own cross-links.
- Companion Planting Chart ($5): The lowest-friction entry point. Buyers who purchase this product have demonstrated they will pay money for growing information; they have not yet explored the catalog. Natural follow-on: Container Growing Blueprint Pack, Apartment Seed Starting Kit.
- Zone-by-Zone Seed Starting Calendar ($8): Highly practical, used repeatedly. Buyers who use this calendar encounter monthly references to specific growing techniques and products. Natural follow-on: the product covering whatever month's challenge they are facing.

**Identification method**: For each product, calculate the ratio of customers who made a second purchase within 90 days to total customers who purchased that product first. Do this monthly starting Month 3 when 90-day windows are available. Any product with a repeat-purchase-trigger rate above 25% is a repeat-purchase driver and should be featured prominently in paid acquisition campaigns because the LTV of buyers entering through that product is meaningfully higher than the first-transaction price suggests.

### One-Time Buyer Products

These products typically sell to buyers with a specific, narrow need that is satisfied by the one purchase. They have high single-transaction value but low repeat-purchase signal.

**Expected one-time buyer products:**
- Hunting, Fishing & Trapping Field Manual ($20): Buyers typically have a specific use case (hunting season prep). Once purchased, the guide covers the topic comprehensively and there is no natural adjacent product with equal urgency.
- Native Plants Regional Guide ($18): Deep, comprehensive field guide. Buyers who need it get everything they need from one purchase. Repeat-purchase driver rate likely below 15%.
- Survival Garden Regional Plans ($22): Region-specific and comprehensive. A buyer in the Pacific Northwest does not need the Mid-Atlantic plan. Repeat purchases would require a completely different interest (e.g., preservation after growing season).

**Strategic implication**: One-time buyer products should not be the primary paid-ad targets because their CAC payback depends entirely on the first transaction. They can still be profitable ad targets (high individual price covers most ad CACs) but should not be treated as funnel entry points for LTV optimization. They are better positioned as upsells to existing customers who arrived through repeat-purchase driver products.

### Bundle Gateway vs. Bundle Ceiling

Bundles create a LTV ceiling problem: a customer who purchases the Homesteader's Complete Bundle ($50) has already acquired the 4 products that would otherwise be sold separately at up to $72 combined. There is no natural upsell path within the existing catalog for this customer. Track the bundle-first cohort's repeat purchase rate — if it falls below 15% at 180 days, bundle listings should include explicit cross-references to products not in the bundle as a strategy to create post-bundle purchase paths. The Food Sovereignty Bundle ($30) buyer, for example, has not purchased any preservation products — the Day 7 cross-sell email specifically targets this gap.

### Product-Level Conversion Funnel

For each product listing, track the micro-conversion funnel: listing views to favorites to add-to-cart to purchase. Etsy's Stats dashboard provides views and orders. The conversion rate (orders / views) is the key product-level health metric.

Industry benchmark for Etsy digital products: 1–3% conversion rate from listing view to purchase. Products below 0.5% after 100+ views need listing intervention (mockup image quality, title relevance, or pricing). Products above 3% are performing well and are the priority targets for Etsy internal ad spend because every additional view at a proven 3% conversion rate produces predictable revenue.

---

## 4. Email Engagement Cohort Analysis

Email engagement is a leading indicator of future purchase activity. A subscriber who opens 6 of the last 8 emails is more likely to purchase within the next 30 days than one who has opened 1 of the last 8. Track email engagement not just as a deliverability metric but as a purchase-prediction signal.

### Open Rate Cohort Thresholds and Actions

Maintain three subscriber health buckets in Kit at all times:

**Healthy (30%+ open rate over trailing 8 sends):** These subscribers should receive full cadence — weekly newsletter, seasonal broadcasts, VIP offers. Do not reduce frequency for this group. They are reading and not unsubscribing.

**Marginal (15–30% open rate):** These subscribers are periodically engaged. Reduce promotional sends (no more than 1 broadcast per month) and emphasize value-first content in newsletter subject lines. If a subscriber in this bucket makes a purchase, tag them "purchased" — purchase events often correlate with a bump in subsequent email engagement.

**At-risk (below 15% over 6 consecutive sends):** This triggers Automation 4 (win-back). The 90-day win-back sequence attempts re-engagement through a free resource, a direct question, and a final removal notice. Subscribers who re-engage move back to the Marginal bucket. The goal is not to keep everyone — it is to maintain a clean, high-signal list.

### Click-Through Rate Cohorts by Content Type

Click-through rate (CTR) on specific email links reveals product affinity at a list-wide level. Track CTR separately for:

- Educational links (blog, video, free resource): Baseline CTR target 4–7%. High CTR on educational content predicts long-term list retention even without purchases.
- Product links (Etsy listing URLs): Target CTR 2–4%. Subscribers who click product links are in-market. If CTR is above 4% and conversion on the Etsy listing is above 1%, the email-to-purchase funnel is healthy.
- Bundle links: CTR will be lower than individual product links (larger decision, higher price) but purchase rates from bundle clicks should be higher. Track bundle CTR separately.

Subject lines should be A/B tested quarterly using Kit's A/B testing feature (available on Creator tier and above). Test one variable at a time: question format vs. statement format, or curiosity-gap vs. explicit benefit. Document results in the monthly metrics checklist.

### Unsubscribe Pattern Analysis

Unsubscribe events are data, not failures. Track when in the subscriber lifecycle unsubscribes occur:

**Email 1–5 of welcome sequence (within first 10 days):** Unsubscribes here indicate lead magnet-to-content mismatch. If someone downloaded the Zone Quick-Start Card expecting planting zone data and received brand philosophy content instead, they leave. Target: below 2% unsubscribe rate on the welcome sequence. If above 3%, audit Email 2 (the most opinionated email in the sequence — heirloom vs. hybrid framing) for tone or relevance issues.

**Weeks 2–6 (after welcome sequence, early newsletter period):** Unsubscribes here indicate the transition from sequence to newsletter is jarring. The welcome sequence ends on Day 10; the subscriber then shifts to weekly content. If weekly content is lower quality or more promotional than the sequence, unsubscribes spike. Target: below 0.5% per send.

**After promotional broadcasts:** Any broadcast send will produce above-average unsubscribes. A Black Friday sale email to a 1,000-person list will lose 5–20 subscribers regardless of quality. This is expected and acceptable. Concern threshold: if a single promotional send generates above 1.5% unsubscribes (15+ people), the content or frequency is wrong.

**Seasonal spikes:** If unsubscribes spike in May after spring planting content was sent to the full list, it may indicate that some subscribers are not gardeners (came via a social share or recipe content) and are self-selecting out. This is healthy list hygiene, not a problem to fix.

### Segment Performance by Tag

For the three behavioral tag segments (Seed Saver, City Grower, Preservationist), track monthly:

- Open rate for segment-targeted content vs. full-list sends
- CTR on segment-appropriate product links
- Purchase rate in the 30 days following a segment-targeted email

The expectation is that segment-targeted emails outperform full-list sends on CTR by at least 50% (e.g., 6% CTR for a Seed Saver email about Seed Saving Field Manual vs. 4% CTR for the same email to the full list). If the performance gap is smaller than expected, the tagging behavior (click signals in Emails 3–4) is not a strong enough signal of product affinity and additional tagging triggers should be added — for example, tagging based on which type of free resource a subscriber downloads in a subsequent email.

---

## 5. Seasonal Cohort Tracking

The seasonal demand structure documented in annual-product-plan.md creates predictable acquisition waves. Treating each wave as a distinct cohort enables forward planning rather than reactive response.

### Three-Peak Framework

**Spring planning cohort (January–April acquisitions).** This is Seedwarden's largest annual cohort by volume. Buyers arrive in search of specific, immediately applicable information: when to start seeds, what varieties to grow, how to set up containers. Their seasonal re-engagement window is the following January. The key tracking metric for this cohort is 12-month retention rate: what percentage of January–April buyers are still email-engaged and make a second purchase in the following spring window?

Benchmarking target: 20% of Spring Planning cohort makes a second purchase within 12 months, with the second purchase concentrated in August–October (preservation season) or the following January–March (re-engagement with spring content). If second-purchase concentration falls in the following spring window rather than the intermediate preservation season, it confirms these buyers are garden-planning-motivated and the post-purchase cross-sell should de-emphasize preservation products in favor of complementary growing guides.

**Preservation season cohort (July–September acquisitions).** Secondary in volume but strategically important because the preservation niche has lower competitive density on Etsy. Buyers arrive with harvest-specific problems. Their re-engagement window is the following July. Track: percentage who purchase a growing guide in the subsequent spring (indicating the buyer is moving up the food chain from preservation to full-cycle growing), versus percentage who repeat a preservation purchase (unlikely — they already have comprehensive coverage after one guide or bundle).

**Holiday gift cohort (November–December acquisitions).** As discussed above, this cohort bifurcates between gift buyers (near-zero LTV beyond first transaction) and self-purchasers (normal LTV). In Year 1, treat the entire cohort conservatively and do not invest in re-engagement campaigns beyond the standard win-back sequence. In Year 2, once a second holiday season has passed, compare the Year 1 holiday cohort's 12-month purchase history against other cohorts. If any sub-segment shows repeat purchase behavior, that sub-segment can be targeted with a personalized holiday re-engagement campaign.

### Year-over-Year Cohort Comparison (Starting Year 2)

After completing the first full seasonal cycle (by May 2027), create a cohort comparison:

- January 2026 subscribers: What is their 12-month engagement rate? Second-purchase rate? Which products did they buy on second purchase?
- Contrast with July 2026 preservation subscribers: same metrics.
- If January cohort has 25% second-purchase rate and July cohort has 12%, the spring planning cohort has higher inherent LTV and marketing investment should weight toward January–March acquisition spending.

This comparison is not possible in Year 1 but should be the explicit goal of data collection in the monthly checklist: gather the inputs to build this table by May 2027.

### Seasonal Product Demand Index

Maintain a simple index across seasons by tracking which products account for what percentage of total monthly revenue:

- January: what percentage of total monthly revenue came from planning products (Zone Calendar, Survival Garden Plans, 12-Month Planner) vs. preservation vs. bundles?
- August: what percentage from preservation products?

This index has two uses: it validates the seasonal demand forecasts in annual-product-plan.md and it provides early warning when a month's product mix diverges from expectations. If August 2026 shows planning products outperforming preservation products in total revenue, investigate whether a non-seasonal marketing push (a social video about seed starting that went unexpectedly viral) is distorting the natural pattern.

---

## 6. Conversion Funnel Metrics

The full Seedwarden conversion funnel spans from product listing discovery through second purchase. Each stage has a measurable rate, a target, and a diagnostic action when below target.

### Stage 1: Listing Discovery to View

**Metric:** Impressions to listing views (available in Etsy Stats > Traffic).
**Target:** Greater than 2% impression-to-view rate.
**Low-rate diagnosis:** If impressions are high (product is appearing in search) but click-through is low, the listing thumbnail image is not compelling or the title is not matching buyer intent. Action: test a new cover mockup image or revise the title's leading phrase. Do not change both simultaneously — change one variable at a time.

### Stage 2: Listing View to Add-to-Cart

**Metric:** Estimated from listing view count and add-to-cart events (Etsy does not provide this directly; proxy is the view-to-sale rate as add-to-cart data is not exposed to sellers).
**Proxy target:** View-to-sale rate above 1.5% for individual products, above 0.8% for bundles (bundles have a higher consideration threshold).
**Low-rate diagnosis:** Below 1% view-to-sale rate after 150+ views indicates a listing content problem: description does not answer the key buyer objection (is this worth $12?), the product images do not show enough of the content, or the price is misaligned with perceived value. Priority fix: add a content-preview mockup image showing a spread of actual pages from the guide, not just the cover.

### Stage 3: Add-to-Cart to Purchase

Etsy cart abandonment is not directly measurable without an external integration. The proxy: if a subscriber clicks an Etsy listing link from an email (tracked via UTM parameters) but does not use a coupon code within 7 days, treat this as a cart-abandon signal and trigger a single re-engagement email (not a discounted offer — a "here's what might help you decide" format that answers common purchase objections).

### Stage 4: Purchase to Email Signup

**Metric:** Percentage of Etsy purchasers who subsequently sign up for the email list.
**Target:** 20–35% of buyers sign up for email list within 30 days of purchase.
**Driver:** Every product PDF includes an end-page with the lead magnet CTA ("Get our free Zone Quick-Start Card: [landing page URL]"). This is the primary email-from-buyer acquisition mechanism since Etsy does not share buyer email addresses. Track by comparing monthly new email subscribers to monthly Etsy buyers — if the ratio falls below 15%, the end-page CTA needs redesign (stronger headline, clearer benefit, simpler URL).

### Stage 5: Email Subscriber to Second Purchase

**Metric:** Percentage of email subscribers (who are also past purchasers) who make a second purchase within 90 days.
**Target:** 20–30% second-purchase rate within 90 days of subscribing post-purchase.
**Primary driver:** Post-purchase email sequence (Day 7 cross-sell email). This is the single highest-leverage email in the automation stack. A/B test the product featured in the Day 7 email: test pairing a Seed Saving purchaser with the Food Sovereignty Bundle versus the Anti-Catalog. The winning variant should be adopted list-wide.

### Stage 6: Second Purchase to VIP Status

**Metric:** Percentage of second-purchase customers who make a third purchase within 180 days.
**Target:** 10–15% of second-purchase customers become three-purchase (VIP) customers.
**VIP treatment:** Tag manually in Kit as "vip" after the second purchase is confirmed. VIP subscribers receive early access to new product launches, exclusive bundle pricing, and "what should we build next?" surveys. The VIP segment is the product development feedback loop — their expressed preferences directly influence the Phase 4 product roadmap.

### Full Funnel Benchmark Summary

| Funnel Stage | Target Rate | Primary Lever |
|---|---|---|
| Impression to listing view | 2%+ | Cover image quality, title SEO match |
| Listing view to purchase | 1.5%+ | Content mockups, description clarity, pricing |
| Purchase to email signup | 20%+ | PDF end-page CTA quality |
| Email signup to second purchase (90 days) | 20%+ | Day 7 cross-sell email optimization |
| Second to third purchase (VIP) (180 days) | 10%+ | VIP early access and exclusive pricing |
| Welcome sequence Email 5 coupon redemption | 8%+ | Product-intent alignment of the offer |
| Post-purchase review email conversion | 8%+ | Timing (Day 14 vs. Day 21 test) |

---

## 7. Metrics Governance and Data Collection

### What Etsy Provides vs. What Must Be Tracked Manually

Etsy Stats provides: listing views, favorites, orders, revenue, traffic sources (organic search, direct, social referral — but not email-referral specifically), and geographic distribution of buyers. Etsy does not provide: add-to-cart events, demographic data, returning buyer identification across orders, or email addresses for post-purchase follow-up.

The practical consequence: much of the most valuable data must be assembled manually or through Kit's subscriber activity reports. The monthly checklist (see monthly-metrics-checklist.md) formalizes this collection into a repeatable 90-minute monthly process.

### Metric Hierarchy: What to Optimize First

Given the operational constraints of a one-person business, do not attempt to optimize all metrics simultaneously. The hierarchy:

1. Etsy listing conversion rate (views to purchases) — this is the floor. If this is below 1%, no amount of email optimization or paid advertising will produce acceptable unit economics.
2. Email list growth rate (new subscribers per month) — this is the compounding asset. A growing, engaged list is the primary defense against Etsy algorithm changes and the primary driver of eventual paid-channel profitability.
3. Second-purchase rate (30–90 days post first purchase) — this is the LTV multiplier. Moving from a 10% to a 25% second-purchase rate roughly doubles 24-month LTV without any change in acquisition cost.
4. CAC by paid channel (Etsy ads, Pinterest ads) — this matters only after the above three are healthy. Running ads to a listing with a 0.5% conversion rate is expensive data collection, not growth.

### KPI Targets at 6-Month and 12-Month Marks

**6-Month Targets (November 2026):**
- Etsy monthly revenue: $600–$1,200
- Email list size: 400–600 subscribers
- Email list open rate: 32%+
- Top-3 product conversion rate: 2%+
- Second-purchase rate (90-day): 15%+
- Etsy review count: 20–40

**12-Month Targets (May 2027):**
- Etsy monthly revenue: $1,500–$3,000 (holiday peak month: $3,000–$5,000)
- Email list size: 1,200–2,000 subscribers
- Email list open rate: 35%+
- Second-purchase rate (90-day): 22%+
- LTV for mid-price first-purchaser cohort: validated at $20+
- Etsy review count: 80–150
- Proportion of revenue from bundles: 35%+

---

*Prepared: 2026-04-27. Sources: annual-product-plan.md, email-automation-blueprint.md, phase-3-social-media-growth-strategy.md, bundle-listings.md, product-audit-2026-04-11.md. Cohort framework adapted from Amplitude and Mixpanel e-commerce cohort analysis patterns.*
