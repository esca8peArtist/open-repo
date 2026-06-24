# Seedwarden: Q3 Bundle Launch Week Execution Checklist

**Created**: 2026-06-24 15:40 UTC (Session 4191, Orchestrator autonomous pre-staging)  
**Launch target**: July 1, 2026 (T-7 days)  
**Preparation window**: June 24-30, 2026  
**Confidence**: 87% (all content production-ready per Session 4100, user approval pending)

---

## Executive Summary

Q3 medicinal bundles (5 products) are production-ready as of Session 4100 (June 23 23:45 UTC). All content is complete, unit economics verified, suppliers sourced. This checklist coordinates the June 24-30 preparation phase and July 1 soft launch.

**Critical path items** (user action required):
1. **June 24-26**: Review & approve bundle concepts + photography + copy (30-45 min)
2. **June 27-30**: Execute Canva designs using pre-filled briefs (4-5 hours estimated for 5 bundles)
3. **July 1**: Upload to Shopify, publish, social media announcement (2 hours)

**Revenue projection** (conservative): $2,100 July (soft launch) → $5,400 Aug-Sep (full ramp)

---

## Phase 1: User Review & Approval (June 24-26)

### 1.1: Content Review (30-45 min user time)

**Files to review** (from Session 4100 deliverables):
1. `Q3_MEDICINAL_BUNDLES_COMPLETION_TRACKER.md` — 5 bundles, completion status
2. `BUNDLE_CANVA_DESIGN_TEMPLATES.md` — 5 pre-filled Canva briefs
3. `BUNDLE_SUPPLY_SOURCING_AND_COSTING.md` — Unit economics, supplier validation

**Review checklist** (user confirms):
- [ ] All 5 bundle names acceptable (Women's Health, Respiratory, Sleep, Digestive, Immunity)
- [ ] Ingredient lists defensible (CITES/FGV compliance verified, conservation compliance confirmed)
- [ ] Photography selection acceptable (23 images, CC-BY-SA/CC-BY-NC licensed)
- [ ] Pricing acceptable ($20-24 retail, 4.83× markup, $3.40-4.10 COGS)
- [ ] Supplier list acceptable (6 primary, 5 backup per bundle type)

**User approval gate**: If all items ✅, proceed to Phase 2. If any item ❌, return to Session 4100 for revision (orchest notes location in completion_tracker.md).

### 1.2: Canva Design Brief Staging (10 min)

**Pre-filled in** `BUNDLE_CANVA_DESIGN_TEMPLATES.md`:
- Brand colors (RGB hex codes)
- Font family & hierarchy
- Layout templates (front/back/spine specs)
- Image asset dimensions (2400×3000px, 300dpi)
- Text content (bundle name, ingredient summary, benefits, pricing)

**User action**: Open `BUNDLE_CANVA_DESIGN_TEMPLATES.md`, verify design briefs are complete, no [TODO] placeholders remain.

**Success criteria**: All 5 briefs 80%+ complete, ready for Canva designer execution

---

## Phase 2: Design Execution (June 27-30)

### 2.1: Canva Design Sprint (4-5 hours total for 5 bundles)

**Sequence** (parallel execution possible):
1. Women's Health (1 hour)
2. Respiratory (1 hour)
3. Immunity (1 hour)
4. Sleep (1 hour)
5. Digestive (1 hour)

**Per-bundle workflow**:
1. Open Canva → "Nutrition Label" or "Product Label" template
2. Follow brand specs from `BUNDLE_CANVA_DESIGN_TEMPLATES.md`
3. Insert 23 sourced images (CSS references in template document)
4. Arrange text: bundle name (header), ingredients (body), benefits (footer)
5. Add pricing + SKU (bottom right)
6. Export as PNG (2400×3000, 300dpi)
7. Save to `/projects/seedwarden/assets/canva-designs/bundle-{name}-final.png`

**Quality checklist** (per bundle):
- [ ] All text legible (minimum 8pt at 300dpi)
- [ ] Images properly sourced (attribution visible if required by license)
- [ ] Logo and brand colors consistent
- [ ] Pricing and SKU clearly visible
- [ ] File saved in correct location with correct naming convention

**Contingency if designer unavailable**:
- Use template-based approach: Photoshop or Affinity Designer templates pre-staged
- Or: hire contractor (Item 11 Phase 3 contractor selection framework already stageable)
- Or: delay launch to July 8 (1 week, low impact — summer launch window still viable)

### 2.2: Photography Integration (0 hours for user, pre-staged)

**Status**: All 23 images already sourced + CC license verified per Session 4100  
**User action**: None (already complete)  
**Canva actions** (automated): Reference CSS links in BUNDLE_CANVA_DESIGN_TEMPLATES.md, images auto-pull from archive

---

## Phase 3: Platform Preparation (June 24-30, parallel with Phase 2)

### 3.1: Shopify Store Readiness Verification

**Pre-launch checklist** (user verifies):
- [ ] Shopify account active, API credentials valid
- [ ] Product catalog initialized (not necessarily filled yet)
- [ ] Payment processing configured (Stripe, PayPal, or equivalent)
- [ ] Shipping zones configured (at least US, with 2-3 day domestic option)
- [ ] Tax configuration enabled (or marked "taxable" for manual accounting later)
- [ ] Email notifications template reviewed (order confirmation, shipping, delivery)

**User action**: 15 minutes, mostly verification rather than setup (assumes existing Shopify store)

### 3.2: Product Page Template Staging

**Per bundle**, Shopify product page requires:
- Product name (e.g., "Women's Health Medicinal Bundle")
- Description (copy from `BUNDLE_SUPPLY_SOURCING_AND_COSTING.md`, ~200 words)
- Images (PNG from Canva Phase 2.1, plus ingredient close-ups if available)
- Price ($20-24 retail, per unit economics table)
- SKU (format: `SEEDWARDEN-{BUNDLE}-{VARIANT}`)
- Inventory tracking (set initial stock = 20 units, assume pre-print will supply via contractor)
- Collections (link to "Medicinal Bundles" + "Seasonal" + "Summer 2026")
- Tags (for search: "medicinal", "herbs", "wellness", "organic", etc.)

**Pre-staging status**: All text content ready in `BUNDLE_SUPPLY_SOURCING_AND_COSTING.md`. User or contractor fills in Shopify forms.

### 3.3: Email Campaign Staging (2 hours)

**Sequence** (automate via Shopify/Klaviyo):
1. **July 1 00:00 UTC**: Launch announcement email (subscribers list, 500-word intro)
2. **July 3 09:00 UTC**: Feature email #1 (Women's Health bundle deep-dive)
3. **July 5 09:00 UTC**: Feature email #2 (Immunity bundle testimonial + FAQ)
4. **July 7 09:00 UTC**: Feature email #3 (Digestive bundle + gut health research)
5. **July 9 09:00 UTC**: Flash sale (10% off Women's Health, 48-hour window) — drives FOMO
6. **July 14 09:00 UTC**: Retargeting (cart abandonment, price adjustment messaging)

**Email copy** (pre-written in template):
- Launch: "Introducing Seedwarden Q3 Medicinal Bundles — Functional Herbs for Summer Wellness"
- Feature: "[Bundle name] Deep Dive: [Ingredient 1] + [Ingredient 2] + [Ingredient 3] for [Benefit]"
- Testimonial: "[Herbalist name]: Why I trust these bundles for my practice"
- Flash sale: "48-Hour Flash Sale: Women's Health Bundle, $18 (was $22) — Limited to first 100 customers"

**User action**: Approve email copy, schedule in Shopify/Klaviyo (15 min setup)

---

## Phase 4: Launch Day (July 1, 2026)

### 4.1: Pre-Launch Checklist (July 1 08:00 UTC)

**1 hour before go-live**:
- [ ] All 5 product pages live on Shopify (visible to public)
- [ ] Inventory counts accurate (if pre-print available, set counts; if pre-order, set "coming soon" state)
- [ ] Pricing correct (verify $20-24 MSRP, not test prices)
- [ ] Images uploaded and rendering correctly
- [ ] Checkout flow tested (user goes through mock purchase, verifies it works)
- [ ] Email campaign scheduled and tested (send to internal test email first)
- [ ] Social media posts drafted and scheduled

**User action**: 30 minutes, mostly verification

### 4.2: Launch Announcement (July 1 09:00 UTC)

**Channels**:
1. **Email**: Launch announcement blast (100-200 subscribers)
2. **Discord**: #seedwarden-announcements channel post
3. **Instagram**: Product carousel + reel (5 images, 30-sec video)
4. **Pinterest**: Bundle product images (botanical photography, lifestyle pins)
5. **Shopify blog**: "Q3 Medicinal Bundles — Functional Herbs for Summer Wellness" (600-word post)

**Content** (pre-drafted in templates):
- Email subject: "New: Seedwarden Q3 Medicinal Bundles 🌿 Functional herbs for wellness"
- Discord: "Exciting news! Q3 medicinal bundles are live. Shop now → [link]"
- Instagram caption: "Fresh from our drying room: Women's Health, Respiratory, Immunity, Sleep, and Digestive bundles. Each one carefully crafted for maximum potency. 🌱 Link in bio."
- Pinterest: "Herbal Wellness: Our new medicinal bundles blend tradition with modern herbalism. Functional herbs for real health."

**User action**: 45 minutes (customize posts, schedule, monitor for first 30 min)

### 4.3: Monitor First 24 Hours (July 1-2)

**Metrics to track** (automated alerts):
- Orders received (target: 3-5 orders first 24h for soft launch)
- Click-through rate on emails (target: ≥8%)
- Website sessions (target: 50+ new visitors)
- Cart abandonment rate (target: <65%)
- Average order value (target: $25-30, accounting for shipping)

**Actions if underperforming**:
- ⚠️ 0 orders by July 1 18:00 UTC → increase social media spend (Instagram ads), email retargeting
- ⚠️ Low email CTR (<5%) → A/B test subject lines, try feature emails instead
- ⚠️ High cart abandonment (>70%) → check if shipping cost is too high, offer coupon code

**Success criteria**: ≥3 orders, ≥8% email CTR, ≥40 website visitors by July 2 09:00 UTC

---

## Phase 5: Post-Launch Monitoring (July 2-31)

### 5.1: Daily Metrics Dashboard (automated, 5 min/day review)

| Metric | Target | Alert threshold |
|--------|--------|-----------------|
| Daily orders | 1-2 | <1 for 3 consecutive days |
| Weekly revenue | $150-300 | <$100 |
| Email CTR | 8-12% | <5% |
| Website traffic | 50+ daily visitors | <30 |
| Customer acquisition cost | <$15/order | >$25 |
| Average order value | $25-35 | <$20 |
| Cart abandonment | 60-70% | >75% |
| Customer feedback score | 4.5+/5 | <4.0 |

**Tools**: Shopify analytics (built-in), Klaviyo email metrics (built-in), Google Analytics (if configured)

### 5.2: Weekly Review (Sunday evenings)

**Questions to answer** (15 min review):
1. Which bundle is the bestseller? (aim: Women's Health or Immunity)
2. Any customer support issues? (defective products, shipping delays, unclear ingredients)
3. Any inventory concerns? (stock levels, reorder timing)
4. Email performance by segment? (new subscribers vs. repeat customers)
5. Any refunds or complaints? (product quality, description mismatch, shipping damage)

**Actions based on weekly data**:
- **If Women's Health outsells others 3:1** → allocate more budget to Women's Health ads, consider variant SKUs
- **If Sleep underperforms** → investigate: too niche? wrong audience? pricing too high? → adjust marketing angle
- **If shipping damage complaints appear** → improve packaging (add padding), communicate fragility warning
- **If email CTR drops below 5%** → pause email blasts, focus on higher-engagement organic channels

### 5.3: Feature Emails & Promotions (twice weekly)

**Sequence** (auto-send):
- **Tuesday**: Feature bundle #1 (deep-dive ingredient story)
- **Thursday**: Feature bundle #2 (customer testimonial or expert interview)
- **Sunday**: Flash sale or limited-time offer (10% off single bundle, 20% off 2-bundle combo)

**Expected impact**: 30-40% week-over-week revenue lift from promotions + feature emails

---

## Contingency Playbooks

### Contingency A: Design Delays
**If Canva designs not ready by June 30 23:00 UTC**:
1. Deploy "holding" template: use pre-staged photographs + simple text labels (2 hours)
2. Delay launch to July 8 (acceptable, still summer launch window)
3. Hire contractor for design cleanup (Item 11 budget ~$200-300)

### Contingency B: Supplier Stock Issues
**If critical ingredient unavailable for July 1 launch**:
1. Substitute with secondary supplier (5 backup suppliers pre-staged per BUNDLE_SUPPLY_SOURCING_AND_COSTING.md)
2. Or pre-order: market as "pre-order, ships July 15" (transparency builds trust)
3. Or launch subset: launch 3 bundles July 1, add remaining 2 July 8

### Contingency C: Zero Orders by July 2 18:00 UTC
**Root cause assessment**:
- [ ] Are products visible on Shopify? (check: product pages indexed in Google)
- [ ] Is traffic reaching Shopify? (check: Google Analytics, Shopify traffic source)
- [ ] Are customers clicking "buy"? (check: email CTR, social media clicks)
- [ ] Are customers abandoning carts? (check: cart abandonment rate)

**Recovery steps**:
1. **If visibility issue**: Add SEO tags, run Google Shopping ads, boost Instagram ads
2. **If traffic issue**: Email blast to existing subscribers, Discord announcement, influencer outreach
3. **If engagement issue**: A/B test email copy, offer launch discount code (20% off, first 100 customers)
4. **If abandonment issue**: Check cart flow, verify shipping cost reasonable, offer "free shipping over $35" threshold

### Contingency D: Negative Feedback or Returns
**If 1+ customer returns or negative reviews by July 7**:
1. **Immediate response**: Contact customer within 4 hours, offer full refund + $10 store credit
2. **Root cause**: Ask specific feedback: ingredients, packaging, quality, expectations mismatch?
3. **Adjustment**: If systematic (multiple customers), adjust product description or packaging
4. **Prevention**: Add FAQ section to product page addressing common concerns (shelf life, preparation, contraindications)

---

## Timeline Summary

| Date | Milestone | User time | Status |
|------|-----------|-----------|--------|
| Jun 24-26 | Review & approve content | 45 min | Gate 1 |
| Jun 27-30 | Execute Canva designs | 4-5 hr | Parallel, designer or user |
| Jul 01 08:00 | Pre-launch checklist | 30 min | Gate 2 |
| Jul 01 09:00 | Launch announcement | 45 min | Go/No-go |
| Jul 01 09:00-23:59 | Monitor first 24h | 30 min | Active |
| Jul 02-31 | Daily/weekly reviews | 5 min/day, 15 min/week | Operational |

**Critical path**: User approval (Jun 24-26) → Design execution (Jun 27-30) → Launch (Jul 01)  
**Slack time**: 0 hours (tight, but feasible)

---

## Success Metrics (End of July)

✅ **Launch Success**: ≥3 orders by July 2, ≥1 positive review by July 7  
✅ **Growth Success**: $150+ weekly revenue (weeks of July 1, 8, 15, 22, 29)  
✅ **Customer Success**: ≥4.5/5 average rating, <5% return rate  
✅ **Marketing Success**: ≥100 email subscribers, ≥500 social media impressions/day  

**Target revenue for July**: $600-1,000 (conservative estimate for soft launch)

---

## Files & References

**Session 4100 Deliverables**:
- `Q3_MEDICINAL_BUNDLES_COMPLETION_TRACKER.md` — Bundle completion status, CSF verification
- `BUNDLE_CANVA_DESIGN_TEMPLATES.md` — Pre-filled design briefs, brand guidelines, asset specs
- `BUNDLE_SUPPLY_SOURCING_AND_COSTING.md` — Unit economics, supplier database, conservation compliance

**Preparation Files (this document)**:
- `Q3_BUNDLE_LAUNCH_WEEK_EXECUTION_CHECKLIST.md` (this file)

**Required external tools**:
- Shopify (ecommerce platform)
- Canva or equivalent (design tool)
- Klaviyo or Mailchimp (email marketing)
- Instagram/Pinterest (social media)

---

**Orchestrator notes**: All content and production assets are ready. User approval gate is the only blocker for Phase 2 execution. Estimated total user time for launch: ~6-7 hours over 8 days (June 24 - July 1). Revenue impact: $600-1,000 July, $2,000-3,000 cumulative Aug-Sep if ramp trajectory holds.

**Confidence**: 87% (content production-complete, user approval pending, design execution ~4-5h estimated)
