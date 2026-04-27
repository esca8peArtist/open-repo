# Seedwarden Customer Cohort Analysis Framework

**Created**: Session 551 (2026-04-27)
**Purpose**: Pre-Phase-1-launch analytics framework for customer segmentation, conversion tracking, and per-cohort messaging
**Status**: Ready to operationalize upon Phase 1 launch

---

## Overview

This framework provides the analytical structure and practical templates to understand customer behavior post-Phase-1 launch. It bridges raw Etsy/Google Analytics data to actionable customer segments (high-intent forager, survival prepper, homesteader, gift buyer) and their corresponding messaging strategies.

The framework is designed to be implemented incrementally:
- **Week 1–2 post-launch**: Basic Etsy metrics collection + Google Analytics overlay
- **Week 3–4**: Cohort classification (assign customers to segments based on behavior)
- **Week 5–6**: Per-cohort messaging and retention experiments

---

## Core Customer Segments

### 1. **High-Intent Forager** (Target: 20–25% of customer base)

**Profile**:
- Purchases: Wild edibles guides, multiple plant guides per order
- Geographic concentration: Pacific Northwest, Northeast (high bioregional plant diversity)
- Repeat purchase frequency: 4–6 purchases/year (seasonal foraging peaks)
- Typical order value: $25–$60 (bundles or premium editions)
- Messaging tone: Educational, precision-focused, seasonal

**Identifying signals**:
- Multiple guide purchases in single transaction
- Repeat purchase within 2–3 months (seasonal windows)
- High page time on "edible uses" sections
- Cart contains 3+ items per order
- Abandon rate: <5% (high intent)

**Pre-Phase-1 hypotheses**:
- Target: College-educated, 25–45 years old, outdoor recreation participation
- Acquisition: Foraging forums (r/foraging, regional Facebook groups), iNaturalist cross-promotion
- Retention: Quarterly seasonal guides (spring mushrooms, summer edibles, fall nuts)

---

### 2. **Survival Prepper** (Target: 15–20% of customer base)

**Profile**:
- Purchases: All guides + emergency prep bundles (if offered)
- Geographic spread: More uniform nationally; slight concentration in rural areas
- Repeat purchase frequency: 2–3 purchases/year (less seasonal, more event-driven)
- Typical order value: $45–$100+ (bulk purchases, bundle discounts)
- Messaging tone: Practical, risk-focused, self-sufficiency

**Identifying signals**:
- Single large order (6+ guides at once)
- Cart contains diverse plant types (edibles, medicinals, ID guides)
- High engagement with "survival scenarios" content (if available)
- Repeat purchase triggered by news events (economic/natural disaster)
- Abandon rate: 10–15% (higher than foragers; price sensitivity)

**Pre-Phase-1 hypotheses**:
- Target: 35–60 years old, homestead interest, emergency preparedness community
- Acquisition: Prepper forums (r/preppers), homesteading blogs, YouTube channels
- Retention: Event-driven messaging ("Wild Food Security for Uncertain Times"), annual bundle refresh

---

### 3. **Homesteader** (Target: 30–35% of customer base)

**Profile**:
- Purchases: Medicinal guides, agricultural guides, permaculture-adjacent content
- Geographic concentration: Homesteading-dense regions (Vermont, Tennessee, coastal California, PNW)
- Repeat purchase frequency: 2–4 purchases/year (project-driven)
- Typical order value: $15–$45 (targeted purchases per season)
- Messaging tone: Community-oriented, practical application, system thinking

**Identifying signals**:
- Medicinal guide + edible guide purchases (healthcare + food security)
- Moderate repeat purchase (quarterly projects)
- High engagement with "permaculture" or "integrated farming" content
- Tend to add guides incrementally (project-by-project vs. bulk)
- Abandon rate: 8–12% (standard)

**Pre-Phase-1 hypotheses**:
- Target: Mixed age (25–65), active homesteading involvement, sustainability-minded
- Acquisition: Homesteading blogs (Backwoods Home, Mother Earth News), community groups, Etsy "homesteading" category browsing
- Retention: Seasonal content (spring garden prep, fall preservation guides), community stories from other homesteaders

---

### 4. **Gift Buyer** (Target: 15–20% of customer base)

**Profile**:
- Purchases: Premium editions, gift sets (if available), single impulsive purchases
- Geographic spread: Concentrated in urban areas, higher income
- Repeat purchase frequency: 1–2 purchases/year (holidays, occasions)
- Typical order value: $25–$50 (gift price point)
- Messaging tone: Aspirational, novelty, lifestyle-positioning

**Identifying signals**:
- Single-purchase customers with no return within 90 days
- High cart abandonment (50%+) on premium items during non-peak seasons
- Peak purchase windows: Mother's Day (May), holiday season (Nov–Dec), Father's Day (June)
- Messaging resonance: "Unique gift for the naturalist" positioning
- Mobile traffic: Higher than other segments

**Pre-Phase-1 hypotheses**:
- Target: Urban professionals, 28–50 years old, gift-giving occasions
- Acquisition: Pinterest (gift guides), Etsy holiday browsing, Instagram lifestyle content
- Retention: Seasonal gift guides, email campaigns around gifting holidays (Mother's Day, holiday season)

---

## Analytics Infrastructure

### 1. **Etsy Analytics Data Collection**

**Monthly metrics to track** (collected manually or via Etsy API):

| Metric | Definition | Tracking Method | Goal by Month 3 |
|--------|-----------|-----------------|-----------------|
| **Conversion Rate** | Orders / Visits | Etsy Dashboard → Monthly report | 2–3% (Etsy average ~1%) |
| **Average Order Value** | Total Revenue / Orders | Etsy Dashboard | $25–$35 |
| **Customer Acquisition Cost** (CAC) | Ad spend / New customers | Link ads to customer source | <$15 per customer |
| **Repeat Customer Rate** | Repeat customers / Total | Query Etsy Dashboard | 20%+ by Month 3 |
| **Product Mix** | % of revenue per guide | Manual tracking or Etsy reports | Top 3 guides = 40–50% of revenue |
| **Geographic Distribution** | Orders by region | Etsy Dashboard geographic filter | Top 5 regions = 60%+ of orders |
| **Cart Abandonment** | Abandoned carts / Sessions | Etsy Dashboard (if available) | <50% |
| **Return/Refund Rate** | Returns / Orders | Etsy Dashboard | <2% |

**Monthly collection schedule**:
- 1st of month: Pull previous month's data from Etsy Dashboard
- Log into [Seedwarden customer analytics spreadsheet](./customer-analytics.csv)
- Calculate month-over-month growth % for each metric
- Flag anomalies (e.g., sudden conversion drop, geographic shift)

---

### 2. **Google Analytics Integration**

**Setup (Week 1 post-launch)**:
1. Install Google Analytics 4 on Seedwarden product page (if hosted externally) or link Etsy listings to GA via UTM parameters
2. Create GA segments for each cohort (based on initial customer survey or purchase behavior proxy):
   - Segment 1: Repeat purchasers (sessions from returning customers)
   - Segment 2: High time-on-site (forager behavior signal)
   - Segment 3: Multi-product viewers (research depth signal)

**Key GA metrics to track**:
- Session duration by page (longer on "edible uses" → forager signal)
- Scroll depth (premium content engagement)
- Exit pages (where customers leave without purchasing)
- Traffic source (organic, Pinterest, Reddit, homesteading blogs)
- Device (mobile vs. desktop, important for gift buyers vs. research-driven cohorts)

**Etsy-GA linkage** (if Etsy listings are external):
- Use UTM parameters: `?utm_source=etsy&utm_medium=listing&utm_campaign=[product]`
- Track conversions back to Etsy listing via `utm_source=etsy` traffic

---

### 3. **Customer Survey (Post-Purchase)**

**Brief 3-question survey** (send 5 days post-delivery):

```
Thank you for purchasing! One quick question:

1. What brought you to Seedwarden? (Multiple choice)
   [ ] Foraging / wild plant identification
   [ ] Emergency preparedness / food security
   [ ] Homesteading / gardening
   [ ] Gift for a friend/family member
   [ ] Other: _______

2. How will you use this guide? (Free text)
   [1–2 sentences]

3. Can we follow up with seasonal guides on topics like [edible mushrooms / medicinal herbs / survival prep]?
   [ ] Yes, email me updates
   [ ] No thanks
```

**Goal**: Assign customers to cohorts based on responses; store in customer analytics spreadsheet (cohort_assignment column).

---

## Cohort Tracking Spreadsheet

**File**: `projects/seedwarden/customer-analytics.csv`

**Structure**:

| Column | Description | Example |
|--------|-------------|---------|
| `customer_id` | Etsy order ID or unique hash | `ORD-2026-001` |
| `order_date` | YYYY-MM-DD | `2026-05-15` |
| `product_ids` | Comma-separated products ordered | `wild-edibles, medicinal-plants` |
| `order_value` | Total $ | `$42.50` |
| `geo_state` | State/region of order | `OR` (Oregon) |
| `geo_region` | Macro region | `Pacific Northwest` |
| `customer_type` | Repeat or first-time | `repeat` |
| `survey_response` | Cohort from survey | `high-intent-forager` |
| `purchase_pattern` | Behavior-inferred cohort | `homesteader` |
| `final_cohort` | Survey + behavior consensus | `homesteader` |
| `repeat_purchase_1` | Date of next purchase (if any) | `2026-07-20` |
| `days_to_repeat` | Days between orders | `66` |
| `ltv_estimate` | Lifetime value projection | `$180` (based on repeat pattern) |
| `engagement_score` | 1–5 rating based on behavior | `4` |
| `notes` | Qualitative observations | `High engagement with medicinal content; likely health-focused` |

**Monthly update protocol**:
- Week 1: Pull new orders from Etsy, add rows to spreadsheet
- Week 2: Survey responses arrive, populate `survey_response` column
- Week 3: Infer behavior patterns from purchase data, populate `purchase_pattern`
- Week 4: Assign final cohort, calculate repeat purchase rate and LTV estimates

---

## Per-Cohort Messaging Strategy

### **High-Intent Forager Messaging**

**Seasonal campaign cadence**:
- **Spring (March–May)**: "Wild Spring Edibles: Mushroom, Ramp, and Fiddlehead Season"
  - Email subject: "Identify 5 edible mushrooms in your region — Free guide inside"
  - Landing page: Highlight mushroom guide, cross-sell with identification app (if available)
  - CTA: "Get the spring foraging guide"
  
- **Summer (June–August)**: "Berry Season Field Guide"
  - Email subject: "Which berries are edible in your state? Season starts now"
  - CTA: "Claim your free berry identification guide"

- **Fall (September–November)**: "Nut and Root Identification"
  - Email subject: "Acorns, walnuts, and roots: The forager's fall harvest"
  - CTA: "Download the fall guide"

**Messaging themes**:
- Educational depth: "Master 8 species of wild mushrooms this season"
- Regional specificity: "Pacific Northwest foraging hotspots you haven't discovered"
- Urgency (time-limited): "Peak ramp season ends in 3 weeks — don't miss it"
- Community: "What foragers in your region are finding right now"

**Channel priority**: Email (primary), Reddit (r/foraging, regional subreddits), iNaturalist integration

---

### **Survival Prepper Messaging**

**Campaign cadence**:
- **Event-triggered** (news of economic/natural disaster): "Food Security in Uncertain Times"
  - Timing: 2–3 days after headline event (while attention is high)
  - Email subject: "In times of crisis, know what grows in your backyard"
  - CTA: "Get 15% off the complete wild edibles bundle"

- **Annual refresh** (September): "Survival Season — Prepare Now"
  - Email subject: "One year to prepare: Your food security checklist"
  - Content: Bundle discount, testimonial from prepper customer, "30-day challenge"

- **Quarterly check-in**: "What we've learned from our prepper customers"
  - Positioning: Community-building, not directly sales

**Messaging themes**:
- Self-sufficiency: "Be independent from supply chains"
- Practical security: "Growing your own food reduces exposure during shortages"
- Empowerment: "Knowledge you can depend on when it matters most"
- Credibility: "Trusted by 5,000+ preppers and homesteaders"

**Channel priority**: Email (primary), Prepper forums (r/preppers, survivalism blogs), YouTube survival channels (influencer partnerships)

**Bundle strategy**: Offer 20–30% discount on 6+ guide bundle; market as "Complete Prepper's Plant Guide"

---

### **Homesteader Messaging**

**Campaign cadence**:
- **Quarterly project guides** (aligned with homesteading cycle):
  - Spring (March): "Medicinal herb garden planning" (medicinal guide cross-sell)
  - Summer (June): "Companion planting with wild edibles"
  - Fall (September): "Preservation and drying wild foods"
  - Winter (December): "Planning next year's polyculture system"

- **Monthly community stories**: "Homesteader spotlight: How Sarah built her food forest"
  - Customer testimonials, photos, success stories
  - Build community feeling

**Messaging themes**:
- System thinking: "Every plant serves multiple purposes in your ecosystem"
- Long-term planning: "Year-round food security through polyculture design"
- Community: "Join 2,000+ homesteaders building resilient food systems"
- Practical: "Recipes, preservation methods, seasonal planning templates"

**Channel priority**: Email (primary), Homesteading blogs (Backwoods Home, Mother Earth News), Facebook homesteading groups, Pinterest (system design boards)

---

### **Gift Buyer Messaging**

**Campaign cadence**:
- **Mother's Day (Early May)**: "Gifts for the nature-loving mom"
  - Email subject: "The gift she didn't know she needed: A wild edibles guide"
  - Landing page: Premium gift edition (if available), gift packaging, personalization option
  - CTA: "Order the Mother's Day premium edition"
  - Timeline: Campaign runs April 15 – May 10

- **Holiday season (October–December)**:
  - Email subject: "Perfect gift for the naturalist on your list"
  - Campaign: Gift guides (lantern emails) featuring different guides
  - Offer: Free gift wrapping, personalization, gift message

- **Father's Day (June)**: "Gifts for the outdoor explorer"
  - Email subject: "The guide that gets better every season"
  - Positioning: Adventure, exploration, knowledge

**Messaging themes**:
- Aspirational lifestyle: "The perfect gift for anyone who loves wild places"
- Uniqueness: "Not another generic gift — something truly special"
- Practical luxury: "Beautiful, hardcover editions designed for years of use"
- Occasion-focused: "The gift that keeps giving every season"

**Channel priority**: Pinterest (gift guides), Instagram (lifestyle), Email (seasonal campaigns), Etsy ads (holiday season)

**Visual strategy**: High-quality photography of guides in outdoor settings, gift packaging, lifestyle photography (person using guide in nature)

---

## Conversion Funnel Metrics by Cohort

**Expected funnel for each cohort** (Month 1–3 post-launch):

| Stage | High-Intent Forager | Survival Prepper | Homesteader | Gift Buyer |
|-------|-------------------|-----------------|-------------|-----------|
| **Awareness** | 100% (baseline) | 100% | 100% | 100% |
| **Interest** (page visit) | 70–80% | 60–70% | 65–75% | 40–50% |
| **Consideration** (cart add) | 40–50% | 25–35% | 30–40% | 15–25% |
| **Conversion** (purchase) | 15–20% | 8–12% | 12–16% | 6–10% |
| **Repeat** (90 days) | 25–35% | 15–25% | 18–25% | 3–8% |

**Metrics to improve**:
- **Low consideration → conversion**: Reduce friction (faster checkout, more payment options)
- **Low interest**: Improve landing page relevance (cohort-specific messaging)
- **Low repeat**: Implement retention campaigns (seasonal messaging, loyalty discounts)

---

## Post-Launch Implementation Timeline

### **Week 1–2: Setup Phase**
- [ ] Install Etsy and Google Analytics tracking
- [ ] Create customer analytics spreadsheet (customer-analytics.csv)
- [ ] Design post-purchase survey
- [ ] Configure email service (Klaviyo, ConvertKit, or Mailchimp) for segmentation

### **Week 3–4: Initial Data Collection**
- [ ] Collect first 50 customer orders
- [ ] Deploy post-purchase survey to first 20 customers
- [ ] Begin daily monitoring of Etsy metrics (conversion, AOV, geographic distribution)

### **Week 5–6: Cohort Classification**
- [ ] Classify first 50 customers into segments (survey + behavior)
- [ ] Identify top-performing products by cohort
- [ ] Analyze repeat purchase patterns by cohort

### **Week 7–8: First Campaign**
- [ ] Launch first seasonal campaign for high-intent forager segment
- [ ] A/B test email subject lines (track open rates)
- [ ] Measure conversion uplift from campaign

### **Month 3+: Optimization & Scaling**
- [ ] Refine cohort definitions based on actual data (vs. hypothesis)
- [ ] Expand campaigns to additional cohorts based on performance
- [ ] Implement dynamic pricing or bundles for high-LTV segments
- [ ] Plan Phase 3 expansion (influencer partnerships, paid ads, community engagement)

---

## Key Success Metrics

**Month 1 targets** (establish baseline):
- 20–50 orders
- 1.5–2% conversion rate (Etsy average ~1%)
- $25–$35 AOV
- 5–10 customer survey responses (cohort assignments)

**Month 3 targets** (demonstrate viability for Phase 2):
- 150–250 total orders YTD
- 15–25% repeat customer rate
- 2–3% conversion rate (sustained improvement)
- Cohorts clearly differentiated by purchase behavior
- 1–2 successful seasonal campaigns

**Month 6 targets** (inform Phase 3 expansion):
- 400–600 orders YTD
- 20–30% repeat customer rate
- $35–$50 AOV (through bundling, premium editions, or price increase)
- Actionable insights on highest-LTV segments
- Paid ads and influencer partnerships ROI calculated

---

## Data Privacy & Compliance

**Etsy data**: Owned by Etsy; we access via official Dashboard API only. No customer PII stored locally except order-level aggregates.

**Google Analytics**: GA4 ensures customer privacy (no PII in GA). Use GA4's data retention settings (delete raw event-level data after 14 months).

**Customer survey**: Collect via Typeform, Google Forms, or email. Store responses securely; delete after 12 months if not needed for analysis.

**Compliance**:
- GDPR: If EU customers exist, ensure survey respects data collection consent
- CCPA: California customers have right to data deletion (implement "right to be forgotten" process)

---

## References & Tools

**Analytics tools**:
- Etsy Dashboard (built-in): Free, limited
- Google Analytics 4: Free tier adequate for Phase 1
- Klaviyo or Mailchimp: Free tier for <5,000 subscribers
- Spreadsheet (CSV): This framework is designed to work with manual tracking first; automate later via Zapier or custom API if needed

**Customer research**:
- Typeform or Google Forms for post-purchase survey
- iNaturalist forums for forager community insights
- r/preppers, r/homesteading for segment research

**Attribution**:
- UTM parameters on external links
- Etsy "Traffic" source breakdown (built-in)
- Google Analytics campaign tracking

---

## Appendix: Customer Segment Validation Questions

Use these questions in Month 3–4 customer interviews or surveys to validate/refine the four segments:

1. **Forager validation**: "Do you forage regularly? How often? What plants?"
2. **Prepper validation**: "Does food security or self-sufficiency interest you? Why?"
3. **Homesteader validation**: "Do you have land? What practices (gardening, food storage, etc.)?"
4. **Gift buyer validation**: "Who did you buy this for? What made you choose this gift?"

Refinements based on actual data will be the primary input for Phase 2 product/marketing decisions.

---

**Status**: Ready to deploy upon Phase 1 launch. Framework can be implemented incrementally (Week 1 = basic analytics, Week 3 = cohort classification, Week 5 = first campaign).

