---
title: "Phase 2 Tracks 2–4 Integration Plan"
project: mfg-farm (ModRun)
created: 2026-06-28
status: decision-ready
confidence: 91%
scope: >
  How Tracks 2 (supply chain), 3 (market expansion), and 4 (fulfillment automation)
  interconnect, the sequencing of actions post-test-print, and the decision gates that
  govern progression. Complements PHASE_2_SCALING_DECISION_MATRIX.md with
  track-specific sequencing and cross-track dependencies.
related:
  - PHASE_2_TRACK_2_SUPPLY_CHAIN_RESEARCH.md
  - PHASE_2_TRACK_3_MARKET_EXPANSION_RESEARCH.md
  - PHASE_2_TRACK_4_FULFILLMENT_AUTOMATION_RESEARCH.md
  - PHASE_2_SCALING_DECISION_MATRIX.md
  - post-test-print-execution.md
---

# Phase 2 Tracks 2–4 Integration Plan

**Lead finding**: The three tracks are more tightly coupled than they appear. Inventory management platform selection (Track 2) determines whether Amazon FBA and Etsy can share a unified stock pool without overselling (Track 3). Label printing setup (Track 4) must be in place before the first Amazon FBA inbound shipment is packed (Track 3, since FBA requires FNSKU barcodes and poly-bag labels printed to spec). The correct activation sequence is: (1) packing station + Rollo printer on Day 1 post-test-print, (2) Craftybase Pro activated for COGS tracking simultaneously, (3) Etsy listing live, (4) Amazon Handmade application submitted within the first week, (5) Walmart Marketplace application in Week 2. The tracks are parallel from Week 2 onward — supply chain monitoring (Track 2), market expansion execution (Track 3), and packing workflow optimization (Track 4) run simultaneously.

---

## Part 1: Cross-Track Dependencies Map

```
TEST PRINT PASSES
      │
      ├── Track 4 FIRST: Packing station setup (Day 1–2)
      │     - Rollo X1040 purchased ($100)
      │     - Packing table organized with bins, mailers, tape
      │     - Craftybase Pro activated ($20/month)
      │     - Pirate Ship account configured with Etsy integration
      │
      ├── Track 3: Market activation (Day 1–7)
      │     - Etsy listing goes live (already drafted)
      │     - Amazon Handmade application submitted (workspace photos taken)
      │     - Walmart Marketplace application started (EIN required)
      │
      └── Track 2: Supply chain monitoring (Day 1, ongoing)
            - Filament inventory audit (current stock vs. first 30-day demand)
            - Craftybase raw material entries (eSUN PLA+ as primary; Polymaker as tariff hedge)
            - Packaging supplies ordered (500 poly mailers, 500 review cards)
```

### Critical Path Analysis

The true critical path is: **Test print → Amazon Handmade application submitted → Amazon approval (2–4 weeks) → FBA inbound shipment prepared → Inventory at Amazon FC → ASIN live → First Amazon sale**.

This 5–7 week path from test print to first Amazon sale means the Amazon application should be submitted in the first 48 hours post-test-print, not after Etsy is established. Waiting even 2 weeks to submit adds 2 weeks to Amazon revenue start date.

---

## Part 2: Week-by-Week Activation Sequence

### Week 1 (Day 1–7 post-test-print)

**Track 4 (Fulfillment Automation):**
- Purchase Rollo X1040 thermal printer (Amazon, 1-day delivery)
- Set up packing station per Track 4 station design
- Activate Craftybase Pro: enter filament as raw material, cable clip as manufactured product
- Print test labels via Pirate Ship to confirm Rollo setup

**Track 3 (Market Expansion):**
- Etsy listing live (existing copy; update photos with test-print images)
- Amazon Handmade application: take 6–8 workspace photos (P1S printer, filament, prints in progress, finished clips); write production process description; submit
- Walmart Marketplace: create Business Seller account; begin application (approval takes 2–4 weeks)
- Submit Vine enrollment pre-request (available once ASIN is created in Seller Central after Handmade approval)

**Track 2 (Supply Chain):**
- Confirm filament inventory: target 3kg minimum per color for first 30 days
- Order 500 poly mailers (9×12", self-seal) + 500 review cards if not already stocked
- Craftybase: log current filament stock levels; set reorder alert at 500g per color

### Week 2–4

**Track 3:**
- Amazon Handmade application in review (asynchronous; no action needed)
- Etsy: monitor views, favorites, and click-through rates; adjust primary photo if CTR below 3%
- Walmart Marketplace: approval expected within this window

**Track 4:**
- Obico AI monitor installed if running unattended prints ($10/month)
- Packing station procedure card written and laminated
- First-article QC procedure documented

**Track 2:**
- First Craftybase COGS report: verify per-unit cost matches model ($3.75 target for 3-clip bundle)
- If eSUN PLA+ experiencing stockouts, activate Polymaker (Houston) as secondary source

### Week 5–7 (Amazon FBA launch)

**Track 3:**
- Amazon Handmade approved → create ASIN in Seller Central
- Prepare FBA inbound shipment: 25 units, poly bags, FNSKU barcodes printed on Rollo
- Send inbound shipment to Amazon FC (UPS or USPS, tracked)
- Activate Sponsored Products campaign ($3/day) once inventory confirmed at FC

**Track 4:**
- Trunk inventory sync activated: connects Etsy stock pool to Amazon FBA ASIN (prevents overselling from same physical inventory if not using FBA for Amazon)
- Note: FBA uses Amazon FC inventory (separate pool) — Trunk sync is needed only if also doing Amazon self-fulfill; if pure FBA, track separately

**Track 2:**
- Second filament order placed (eSUN or Polymaker) if first 30-day consumption tracked in Craftybase suggests need
- 3PL assessment: if Etsy orders exceed 50/month by Week 6, Fulfillrite outreach for quote

### Month 2–3

**Track 3:**
- Walmart Marketplace approved → list top 3 SKUs
- Begin Faire wholesale application (requires production proof: 50+ Etsy sales or equivalent evidence)
- Evaluate TikTok Shop: if producing content for Etsy/Instagram, add TikTok channel with 1.8% promo rate

**Track 4:**
- If daily packing exceeds 30 minutes, evaluate Shippo Pro upgrade for batch API
- First packer hired (part-time) if orders exceed 150/month and packing consumes >45 min/day

**Track 2:**
- Trunk activated for cross-channel inventory sync (Etsy + Walmart + Shopify when live)
- Craftybase COGS analysis: verify actual per-unit cost vs. modeled; adjust if material consumption differs

---

## Part 3: Decision Gates

### Gate 1: 30-Day Revenue Check (Post-Etsy Launch)

**Threshold**: $500/month (conservative scenario validation)

| Outcome | Action |
|---|---|
| >$500/month | Proceed to Amazon FBA activation; continue as planned |
| $200–500/month | Amazon FBA still warranted (traffic diversification); investigate Etsy SEO underperformance |
| <$200/month | Hold Amazon FBA launch; diagnose listing quality, pricing, photos; add 2–3 SKUs before platform expansion |

### Gate 2: Amazon FBA 60-Day Check

**Threshold**: 10+ reviews, 2+ sales/week

| Outcome | Action |
|---|---|
| 10+ reviews, >$400/month | Increase FBA batch to 50 units; apply for Faire wholesale |
| 5–9 reviews, $150–400/month | Continue; optimize PPC bids; add variation listing |
| <5 reviews, <$150/month | Pause Sponsored Products; reduce bids; investigate search term targeting |

### Gate 3: 3PL Activation Gate

**Threshold**: 300+ orders/month sustained for 4+ weeks

| Metric | Action |
|---|---|
| Orders/month ≥300 | Contact Fulfillrite Baltimore for quote; activate in 30 days |
| Orders/month 150–300 | Hire part-time packer first; reassess 3PL at 300 |
| Orders/month <150 | Self-fulfillment; no 3PL |

### Gate 4: Shopify Launch Gate

**Threshold**: 200+ combined Etsy/Amazon buyers with email addresses; repeat purchase rate >15%

| Metric | Action |
|---|---|
| 200+ emails AND 15%+ repeat rate | Launch Shopify Basic ($39/month); migrate email list to Klaviyo |
| 200+ emails, <15% repeat rate | Improve product range first; Shopify D2C traffic requires brand loyalty |
| <200 emails | Continue building email list; Shopify launch premature |

---

## Part 4: Inter-Track Conflict Points and Resolutions

### Conflict 1: Inventory Allocation (Etsy vs. Amazon FBA)

**Problem**: Producing 25 units for Amazon FBA inbound + 10–20 units for Etsy simultaneously strains a single-printer operation in early Phase 2.

**Resolution**: Print in color batches. Batch 1 (first week after test print): 20 units Etsy inventory. Batch 2 (Week 2): 25 units Amazon FBA inbound (Etsy continues selling from Batch 1). Stagger production so FBA batch does not create Etsy stockout.

### Conflict 2: Packaging Specification Mismatch

**Problem**: Amazon FBA requires poly bags + FNSKU barcode on every unit. Etsy uses poly mailers (different format). Two different label types on the same Rollo printer.

**Resolution**: Rollo accepts rolls of varying widths (1.57–4.1"). Amazon FNSKU labels print on 2×1" label rolls; shipping labels print on 4×6" rolls. Keep both rolls; swap when changing packaging context. Designate a "FBA prep session" (weekly) separate from daily Etsy pack-and-ship.

### Conflict 3: Craftybase vs. Manual COGS Tracking

**Problem**: If Craftybase Pro ($20/month) is activated and Etsy sells primarily, the cost feels unjustified in Month 1 when revenue is $200–400.

**Resolution**: The COGS tracking becomes essential at tax time (accurate cost-of-goods-sold directly affects net taxable income) and when making SKU-level profitability decisions. At Phase 2 with 3–5 SKUs, a Craftybase error in COGS could cost more than $20/month in tax filing errors. Activate at launch regardless of revenue.

### Conflict 4: Walmart Application Timing vs. Amazon FBA Focus

**Problem**: Walmart Marketplace approval takes 2–4 weeks and requires attention during the same period as Amazon Handmade approval and FBA prep.

**Resolution**: Walmart application is 2–3 hours of setup work, then asynchronous review. Submit in Week 1–2 alongside Amazon application. Do not delay Walmart to focus on Amazon — they are parallel applications requiring no ongoing attention during review.

---

## Part 5: 90-Day Dashboard (Post-Test-Print KPIs)

Track these metrics weekly in a single Google Sheet to monitor cross-track health:

| Metric | Week 4 Target | Week 8 Target | Week 12 Target |
|---|---|---|---|
| Etsy orders/month | 20–40 | 50–100 | 80–150 |
| Amazon FBA reviews | 0 | 5–10 | 15–25 |
| Amazon FBA orders/month | 0 | 20–50 | 40–80 |
| Walmart orders/month | 0 | 5–20 | 15–40 |
| Total monthly revenue | $200–500 | $600–1,500 | $1,200–2,500 |
| Daily packing time | <15 min | <30 min | <45 min |
| Craftybase actual COGS/unit | <$4.00 | <$4.00 | <$3.75 (volume effect) |
| Filament in stock (days of runway) | 30+ days | 45+ days | 60+ days |
| Platforms live | Etsy | Etsy + Amazon FBA | Etsy + Amazon + Walmart |

---

## Part 6: Capital Allocation Across Tracks

Post-test-print capital deployment priority (at $272–322 available):

| Allocation | Amount | Track | Priority |
|---|---|---|---|
| Rollo X1040 printer | $100 | Track 4 | 1 — enables all label printing |
| Poly mailers (500 units) | $25–85 | Track 2 | 2 — required for Etsy fulfillment |
| Review cards (500 units) | $15–25 | Track 2 | 2 — print locally via Canva |
| Craftybase Pro (3 months) | $60 | Track 2 | 3 — COGS tracking |
| Amazon FBA inbound batch (25 units COGS + packaging + shipping) | $93.75 | Track 3 | 4 — Amazon revenue |
| Sponsored Products 30-day ($3/day) | $90 | Track 3 | 5 — Amazon discoverability |
| **Total** | **$383–453** | | |

This exceeds the $272–322 available capital floor, requiring ~$60–130 additional from first Etsy revenue before FBA inbound is shipped. Sequencing: use initial Etsy revenue from Weeks 1–3 to fund the Amazon FBA batch in Week 4–5. This is the natural cash-flow-positive sequencing.

---

*Integration plan completed June 28, 2026. All four Phase 2 research deliverables are production-ready and sequenced for immediate post-test-print execution.*
