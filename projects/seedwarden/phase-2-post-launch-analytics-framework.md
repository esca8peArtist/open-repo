# Phase 2 Post-Launch Analytics Framework

**Status**: Production-ready measurement system for Phase 1 → Phase 2 transition  
**Created**: 2026-05-05 (Session 758)  
**Purpose**: Capture Phase 1 sales data, identify which customer cohorts to prioritize, inform Phase 2 product expansion decisions with empirical evidence

---

## Part 1: Core Analytics Objectives

### Primary Goals
1. **Identify high-value customer segments** — Which of 4 cohorts (forager, prepper, homesteader, gift buyer) convert and repeat?
2. **Measure Phase 1 product performance** — Which of 21 Phase 1 products drive sales, repeat purchases, bundle behavior?
3. **Quantify Phase 2 triggers** — At what conversion rate, repeat frequency, and AOV does Phase 2 expansion become viable?
4. **Detect Phase 2 readiness signals** — Early indicators (velocity, cohort concentration, seasonal timing) that predict Phase 3 success

### Secondary Goals
1. **Price optimization** — Which price points achieve max revenue (consider demand elasticity, not just margin)?
2. **Bundle strategy validation** — Do customers prefer/buy bundles, or is single-guide better?
3. **Seasonal patterns** — When do different cohorts buy (back-to-school, spring planting, holiday gifting)?
4. **Retention curves** — 30/60/90-day repeat purchase rates by cohort and product

---

## Part 2: Measurement System Architecture

### Data Collection Points

#### A. Etsy Platform Native Data (automatic)
**Collection method**: Etsy Stats API (daily sync) + manual monthly export as backup

| Metric | Granularity | Business Meaning |
|--------|-------------|-----------------|
| Orders | Per product | Which products sell |
| Revenue | Per product | Total $ by product; hidden: repeat customers |
| Views | Per product | Traffic quality; low views = visibility issue |
| Conversion Rate | Per product | Traffic → sales; low conversion = messaging issue |
| Favorited | Per product | Buying-signal quality |
| Traffic source | Overall | Organic vs. Etsy search vs. social referral |

**Setup**: Etsy Stats → daily CSV export (via automation.etsy.com or API → Google Sheets)  
**Owners**: Backup-read on Sheets each Sunday; alerts if revenue drops >20% vs. 4-week rolling average

#### B. Google Analytics 4 (Gist + Etsy referral tracking)
**Collection method**: GA4 custom events + UTM parameters

Custom events to implement:
- `view_product_category` (payload: product_id, category: wild-edibles|native-plants|zone-quickstart)
- `guide_deep_read` (>60% of page scrolled)
- `add_to_cart` (Etsy-side event, can be pulled via Shopify connector if needed)
- `checkout_start`
- `purchase_complete` (with product list)
- `repeat_purchase` (timestamp of 2nd purchase same customer, >30 days after 1st)

**Segments to create** (for repeatable reporting):
- Cohort: Forager (wild-edibles focused)
- Cohort: Prepper (survival-focused)
- Cohort: Homesteader (general homesteading)
- Cohort: Gift Buyer (high AOV bundles, gift messaging)
- Time windows: First-time buyers vs. repeat (30-day, 60-day, 90-day repeat)

**Setup**: GA4 property → custom events via Google Tag Manager (if Gist supports GTM, otherwise manual event script)  
**Dashboard**: Automated GA4 dashboard with 4-week rolling metrics (see Part 3 dashboards)

#### C. Customer Cohort Tracking (tagging system)
**Collection method**: Post-purchase email survey + manual tagging

At Day 1 (order confirmation email), ask:
> "What brought you to Seedwarden? (Check one)"
> - [ ] Foraging / wild plants
> - [ ] Prepper / survival
> - [ ] Homesteading / gardening
> - [ ] Gift for someone else
> - [ ] Just browsing

**Implementation**: Email via Kit → responses trigger Kit tag ("Cohort_Forager", "Cohort_Prepper", etc.)  
**Fallback**: If survey response rate <30%, infer cohort from product purchased (wild-edibles → Forager, etc.) with 70% accuracy  
**Owner**: Kit automation script; monthly hand-clean for misclassifications

#### D. Repeat Purchase & Lifetime Value Tracking
**Collection method**: Manual Etsy API extract (monthly) or spreadsheet formula on Sheets

Columns needed:
- Customer ID (Etsy) or email
- Order date
- Product(s) purchased
- Revenue
- Days since first purchase
- Cohort tag (from survey or inference)

**Calculation**:
- `Repeat_30d` = count(purchases) > 1 AND days_since_first ≤ 30
- `Repeat_90d` = count(purchases) > 1 AND days_since_first ≤ 90
- `LTV_30d` = total_revenue (first 30 days)
- `LTV_90d` = total_revenue (first 90 days)
- `AOV` = total_revenue / order_count

**Owner**: Monthly export task (1 hour), uploaded to `seedwarden-analytics.csv` in projects/seedwarden/  
**Trigger**: Day 30, 60, 90 analysis windows

---

## Part 3: Dashboards & Reporting Cadence

### Daily Dashboard (Automated, 10 min review)
**Owner**: Anya (optional, for engagement tracking only)  
**Refreshes**: 8am each day (Etsy API lag is ~6-12 hours)

| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| New orders today | Track (no target) | >200% of 4-week avg = capacity alert |
| Revenue today | Track | Revenue down >50% vs. 4-week avg = investigate |
| Avg price | $12-18 | Drift >$5 = product mix change |
| Conversion rate | ≥1.5% | <1.0% for 3 days = traffic quality issue |

**Action**: If revenue anomaly + conversion normal = traffic drop (check Etsy search algorithm changes). If revenue anomaly + conversion drops = messaging or product issue.

### Weekly Dashboard (Manual, 30 min review)
**Owner**: Anya  
**Timing**: Every Sunday evening

**Section 1: Sales Velocity (4-week rolling)**
| Metric | Week 1 | Week 2 | Week 3 | Week 4 | Trend |
|--------|--------|--------|--------|--------|-------|
| Orders | — | — | — | — | ↑ or ↓ or → |
| Revenue | — | — | — | — | — |
| Avg order value | — | — | — | — | — |
| Units sold | — | — | — | — | — |

**Section 2: Product Performance (Top 5)**
| Product | Orders This Week | Total Revenue | % of Total | ∆ vs Last Week |
|---------|------------------|---------------|-----------|-----------------|
| [Product 1] | — | — | — | — |
| [Product 2] | — | — | — | — |
| [Product 3] | — | — | — | — |
| [Product 4] | — | — | — | — |
| [Product 5] | — | — | — | — |
| *Other* | — | — | — | — |

**Section 3: Cohort Mix (This Week)**
| Cohort | % of Orders | Avg AOV | Repeat Rate (90d) |
|--------|-------------|---------|-------------------|
| Forager | — | — | — |
| Prepper | — | — | — |
| Homesteader | — | — | — |
| Gift Buyer | — | — | — |

**Action questions**: 
- Which product drove growth? Can it be promoted/bundled with others?
- Which cohort is underrepresented? Why? (seasonal? messaging?)
- AOV trending up (bundling working) or down (single-guide preference)?

### Monthly Deep Dive (2 hours, Day 1 of next month)
**Owner**: Anya + (optional) external analyst if budget allows  
**Deliverable**: 1-page summary for CHECKIN.md

**Analysis blocks**:

**Block 1: Cohort LTV Analysis**
- 30-day and 90-day repeat rate by cohort
- Avg LTV by cohort (which cohort brings most $ per customer?)
- Cohort acquisition cost (proxy: product-specific ad spend if applicable, else estimate from traffic source data)
- **Decision gate**: Repeat rate ≥10% (any cohort) = good product-market fit; <5% = messaging/product gap

**Block 2: Product Categorization**
Classify all 21 Phase 1 products as:
- **Anchor** (drives traffic, mediocre margin): Wild-edibles guide (if trending)
- **Workhorse** (steady sales, good margin): Zone quick-start card (if it exists in Phase 1)
- **Star** (high sales + high margin): Native Plants guide (projected)
- **Dog** (low sales, low margin): Usually text-heavy guides without visual mockups
- **Hidden gem** (low sales, high customer satisfaction): Flag for Phase 2 variant expansion

**Block 3: Seasonal Pattern Detection**
- Week-over-week trend (velocity curve fitting: linear growth, S-curve plateau, decay?)
- Cohort seasonal concentration (if prepper cohort is >40% of sales in Mar-May, that's spring planting signal)
- Holiday/event alignment (Mother's Day gift spike, back-to-school prep season, fall garden planning)

**Block 4: Phase 2 Readiness Assessment**
Score against Go/No-Go criteria (see Part 5 below):
- [ ] Phase 1 launched without major issues?
- [ ] ≥50 total orders in first 30 days?
- [ ] ≥$600 gross revenue in first 30 days?
- [ ] ≥1 identified "Star" product (high sales + margin)?
- [ ] ≥2 identified cohorts (each ≥20% of sales)?
- [ ] Repeat rate ≥5% at Day 30?

**Output**: Update PROJECTS.md with Go/No-Go recommendation (see Part 5)

---

## Part 4: Technical Implementation (Setup Checklist)

### Before Phase 1 Launch (User action required)

- [ ] **Etsy Stats API access**: Verify account permissions; enable API access in Etsy seller account settings
- [ ] **Google Analytics 4 property**: Create new GA4 property for Etsy store (not same as Gist property); link Etsy account
- [ ] **UTM parameters**: Add to all outbound links from Gist to Etsy:
  - Gist → Etsy: `utm_source=gist&utm_medium=referral&utm_campaign=phase_1_launch`
  - Email → Etsy: `utm_source=kit&utm_medium=email&utm_campaign=phase_1_launch`
  - Social → Etsy: `utm_source=instagram&utm_medium=social&utm_campaign=phase_1_launch`
- [ ] **Kit automation**: Create post-purchase email survey (see Part 2C); define cohort tags
- [ ] **Google Sheets setup**: Create `seedwarden-analytics.csv` with columns:
  - Customer email, Order date, Product(s), Revenue, Days since first purchase, Cohort tag
- [ ] **Weekly reporting calendar**: Block 30 min every Sunday evening for dashboard review

### Day 0 (Phase 1 Launch)
- [ ] Verify Etsy Stats API is flowing data (check 2 hours after first order)
- [ ] Verify GA4 events are firing (check Real-Time > Events in GA4)
- [ ] Verify Kit automation trigger is active (send test order confirmation)
- [ ] Set up Slack/Discord alert for revenue anomalies (optional but recommended)

### Week 1-2 (Ongoing)
- [ ] Monitor daily dashboard for anomalies
- [ ] Respond to cohort survey responses (triage into tags)
- [ ] Check weekly dashboard template is populating correctly

### Day 30 (First Monthly Checkpoint)
- [ ] Run monthly deep dive analysis
- [ ] Update PROJECTS.md Phase 2 readiness assessment
- [ ] Make Phase 2 go/no-go decision (see Part 5)

---

## Part 5: Phase 2 Decision Framework

### Phase 2 Readiness Scoring (Threshold: ≥5 of 6 criteria pass)

| Criterion | Pass | Fail | Business Meaning |
|-----------|------|------|-----------------|
| **Sales Velocity** | ≥50 orders in 30d | <30 orders | Product-market fit validation |
| **Revenue Floor** | ≥$600 gross (30d) | <$400 | Sufficient scale for Phase 2 investment |
| **Product Quality** | ≥1 "Star" identified | All "Dogs" | What to expand on |
| **Cohort Diversity** | ≥2 cohorts >20% each | <2 segments | Product appeal breadth |
| **Repeat Engagement** | ≥5% repeat (Day 30) | <3% repeat | Customer satisfaction signal |
| **Operational Health** | <2% error rate (wrong product, shipping issues) | ≥5% error | Execution readiness |

**Scoring logic**:
- **6/6 pass** (Optimal) → Launch Phase 2 immediately. Expand "Stars" first.
- **5/6 pass** (Go) → Launch Phase 2 with mild caution. Investigate failed criterion.
- **4/6 pass** (Conditional) → Delay Phase 2 by 2 weeks, address failures, reassess.
- **<4/6 pass** (No-Go) → Halt Phase 2. Debug product/messaging issues (see Part 6).

### Phase 2 Scope Decisions (If Go)

**Option A: Expand Stars (Recommended if 1-2 "Stars" identified)**
- Take highest-performing products (e.g., "Native Plants Regional Guide")
- Create regional variants (Zone 3-4 Perennials, Zone 7-9 Edibles, etc.)
- Timeline: 2-week variant production, 4-week social/email campaign
- Expected revenue boost: 50-80% of Phase 1 baseline

**Option B: Defensify Workhorse (If "Stars" lack variant potential)**
- Take steady sellers (e.g., zone quick-start card)
- Bundle with related Phase 1 products (zone card + plant guide for that zone)
- Add new content layers (photo variant, video guide, interactive PDF)
- Timeline: 3-week production, 2-week launch
- Expected revenue boost: 30-50% of Phase 1 baseline

**Option C: Phase Out Dogs (Parallel to A or B)**
- Remove products with <5 total sales AND <1% of revenue in first 45 days
- Redeploy listing slots to Phase 2 variants
- Timeline: Immediate (reallocate Etsy slots)
- Expected benefit: Improved portfolio clarity

---

## Part 6: Failure Mode Recovery

### Red Flag #1: Low Revenue (<$300 in 30 days)
**Root causes**: (a) Listing visibility (Etsy SEO issue), (b) Pricing too high, (c) Mockups not compelling, (d) Niche too small

**Diagnostic questions**:
- Is traffic dropping off (conversion issue) or no traffic (visibility issue)?
- Other sellers in same niche — what's their pricing?
- Do mockups compare to competitors?

**Recovery actions**:
- Visibility issue → Etsy tag refinement + social media push (2 weeks)
- Pricing issue → A/B test lower price on 1-2 products (2 weeks)
- Mockup issue → Refresh mockups + relist (2 weeks)
- Niche issue → Pivot Phase 2 to adjacent category (e.g., endangered plants instead of native plants)

### Red Flag #2: High Churn (0% repeat rate at Day 30)
**Root causes**: (a) Quality issue (customer expected something different), (b) Messaging mismatch (ad promised one thing, product delivers another), (c) Price objection (not worth the cost to customer)

**Diagnostic questions**:
- Do customer reviews exist? Are they positive or negative?
- Do cohort surveys mention "not what I expected"?
- Are customers from organic search or paid ads? (Paid often has higher expectation mismatch)

**Recovery actions**:
- Quality issue → Audit product specs; produce revised version
- Messaging issue → Refine product description/mockups to match reality
- Price issue → Offer bundle discount on 2nd purchase (Kit automation)

### Red Flag #3: Imbalanced Cohorts (<30% diversity)
**Meaning**: One cohort is ≥70% of sales (e.g., 80% gift buyers, 20% others)

**Risk**: If that cohort has seasonality (e.g., gift buyers peak Dec), Year-round revenue becomes volatile

**Recovery actions**:
- Under-served cohort analysis: forager cohort at 5%? → Create foraging-specific product (wild mushroom guide)
- Seasonal hedge: If gift buyers are 80%, design 3 non-gift products specifically for other cohorts
- Phase 2 explicitly targets under-served cohort (e.g., prepper-focused expansion if preppers are <20%)

---

## Part 7: Privacy & Data Governance

- **Customer data**: Email + purchase history only; no browsing data beyond GA4 segments
- **Data retention**: Keep Etsy order data permanently (needed for LTV calc). GA4 events retained per GA4 policy (24 months)
- **Cohort tags**: Stored in Kit (email platform), encrypted at rest, access limited to Anya only
- **Reporting**: Monthly summary shared with anyone who needs it (no PII, only aggregated metrics)
- **Transparency**: If asked by customer, can confirm "your purchase data is used to improve product recommendations" (true and fair)

---

## Part 8: Success Benchmarks (Industry Comparison)

Based on Etsy digital products + indie course creators:

| Metric | Typical | Target | Stretch |
|--------|---------|--------|---------|
| Conversion rate (Etsy listings) | 0.5–1.5% | ≥1.5% | ≥2.5% |
| 30-day repeat rate | 2–5% | ≥5% | ≥10% |
| Cohort concentration (top cohort) | 50–70% | 35–50% | <35% (balanced) |
| Price elasticity (perceived value) | 1.2–1.5 | 1.3–1.8 | >2.0 (premium positioning) |
| Avg order value | $12–18 | $15–22 | >$25 (bundles dominating) |
| CAC (customer acquisition cost via social) | 3–5x product price | <3x | <2x |

---

## Appendix: Metrics Spreadsheet Template

**File**: `seedwarden-analytics.csv`

| Date | Product | Orders | Revenue | Views | CVR | Favorites | Repeat_30d | Repeat_90d | Cohort_Primary | Cohort_Secondary |
|------|---------|--------|---------|-------|-----|-----------|------------|------------|-----------------|------------------|
| 2026-05-30 | Native Plants | 12 | $180 | 2,400 | 0.50% | 47 | 2 | — | Homesteader | Forager |
| 2026-05-30 | Wild Edibles | 8 | $120 | 1,600 | 0.50% | 34 | 0 | — | Forager | Prepper |
| … | … | … | … | … | … | … | … | … | … | … |

**Weekly summary row (rolling 7-day aggregate)**:
| 2026-W22 | ALL | 156 | $2,340 | 34,200 | 0.46% | 612 | 14 | 8 | — | — |

**Update frequency**: Manual copy-paste from Etsy Stats API → Google Sheets; or automated via Zapier if budget allows ($30-50/month)

---

**Next**: Coordinate Phase 1 launch timing with analytics setup. Anya should have all dashboards operational before Day 1 of Phase 1 for full data capture.
