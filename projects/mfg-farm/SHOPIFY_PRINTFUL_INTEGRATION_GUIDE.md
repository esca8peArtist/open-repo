---
title: "Shopify D2C Integration Guide — ModRun Phase 3"
created: 2026-05-21
status: production-ready (activate at Phase 3 trigger)
scope: "Shopify store setup, fulfillment routing, inventory sync automation, email marketing integration for ModRun D2C channel"
confidence: high
note: "Printful is NOT applicable to ModRun products. This guide covers Shopify + self-fulfillment + 3PL routing. The 'Printful' in the deliverable title is a misnomer — Printful discontinued warehousing for own-inventory products in March 2026 and only serves its own POD catalog."
related: MULTI_CHANNEL_SALES_ARCHITECTURE.md, UNIFIED_INVENTORY_MODEL.md, fulfillment-workflow.md
trigger: "50+ combined units/month (Etsy + Amazon) + 50+ Etsy reviews + 100+ past customer email list"
---

# Shopify D2C Integration Guide — ModRun

**Critical note on Printful**: Printful's Warehousing & Fulfillment service for seller-owned products was discontinued effective March 1, 2026 (all inbound shipments halted). Printful is exclusively a print-on-demand service for its own product catalog (apparel, accessories, etc.) — it cannot and will not fulfill custom 3D-printed cable clips, headphone hooks, or magnetic labels. The Shopify D2C channel for ModRun uses Shopify + self-fulfillment (or 3PL at scale).

---

## Part 1: Why Shopify for Phase 3 (Not Earlier)

Shopify is structurally the cheapest transaction channel (6.6% effective fees vs. Etsy 11% vs. Amazon FBA 30.4%) and the only channel that gives ModRun full customer data ownership. But the fee advantage is misleading without accounting for customer acquisition cost.

**The math that determines Shopify viability**:

At a $60 blended D2C CAC (2026 benchmark for home goods — see `MULTI_CHANNEL_SALES_ARCHITECTURE.md`):

- A customer who buys once ($28.99 Starter Bundle) generates:
  - Revenue: $28.99
  - Platform fees: $1.92 (6.6%)
  - CAC: $60.00
  - Net contribution: $28.99 − $1.92 − $60.00 = **−$32.93 (net loss)**

- A customer who buys twice generates:
  - Revenue: $57.98
  - Platform fees: $3.84
  - CAC (one-time): $60.00
  - Net contribution: $57.98 − $3.84 − $60.00 = **−$5.86 (near breakeven)**

- A customer who buys three times (LTV $87) generates:
  - Revenue: $86.97
  - Platform fees: $5.75
  - CAC (one-time): $60.00
  - Net contribution: $86.97 − $5.75 − $60.00 = **+$21.22 (profitable)**

**Shopify D2C is profitable only when LTV/CAC ratio reaches 3:1+.** At LTV of $87 (3 purchases average), the payback period on a $60 CAC is achievable. At 1-purchase LTV, it is a guaranteed loss channel.

LTV of $87 requires an email list-driven repeat purchase strategy. This requires:
1. Capturing email addresses (package inserts with QR codes, Etsy Offsite traffic)
2. Email sequences that bring customers back (3-email post-purchase flow, seasonal promotions)
3. Product expansion that gives customers something to come back for (headphone hooks, labels, bundles are cross-sells to cable clip buyers)

**Phase 3 trigger** (repeat: don't launch Shopify before):
- 50+ combined monthly units (Etsy + Amazon) — proves demand volume exists to support a third channel
- 50+ Etsy reviews — establishes brand credibility that can be referenced on the Shopify store
- 100+ past customer emails collected — provides the seed list for email-driven repeat purchase economics

---

## Part 2: Shopify Store Setup

### 2.1 Plan and Account Creation

- [ ] Navigate to shopify.com → "Start free trial"
- [ ] Select **Basic plan** ($39/month, billed monthly; $29/month annual billing)
  - Basic is sufficient for ModRun through $100K/year revenue; no transaction fee if using Shopify Payments
  - Do not choose Grow ($79/month) at launch; the lower card processing rates ($2.7% + $0.30 vs. 2.9% + $0.30) save $0.006/dollar — not meaningful at early volumes
- [ ] Choose a store name matching the brand: "modrun" or "modrundesign" (check availability)
- [ ] Select store currency: USD
- [ ] Time zone: Your local zone

**Domain setup**:
- [ ] Purchase `modrun.com` (or `modrundesign.com`) via Shopify Domains ($14/year) or externally (Namecheap ~$12/year)
- [ ] Connect domain: Shopify Admin → Online Store → Domains → Add existing domain or buy new

### 2.2 Payment Processing — Shopify Payments

- [ ] In Shopify Admin: Settings → Payments → Complete Shopify Payments setup
  - Required: Bank account, SSN or EIN, business type
  - Shopify Payments waives the additional 2.0% third-party payment processor fee
  - Do not use PayPal as primary payment method (adds 2.0% Shopify fee + PayPal's own 3.49% + $0.49 per transaction)
- [ ] Enable accelerated checkout: Shop Pay (1-click checkout; increases conversion rate ~18% for returning customers)
- [ ] Enable Apple Pay and Google Pay in Shopify Payments settings (zero additional cost; adds checkout option for mobile buyers)

**Effective per-transaction cost with Shopify Payments Basic**:
- 2.9% + $0.30 per transaction
- On a $28.99 sale: $0.84 + $0.30 = $1.14 (3.9%)
- Monthly plan amortized at 50 orders: $0.78/order
- **Total platform cost per $28.99 sale: $1.92 (6.6%)** — confirmed lowest fee channel

### 2.3 Store Theme and Product Configuration

**Recommended free theme**: Dawn (Shopify default 2026 — fast, mobile-optimized, conversion-tested)

Product setup:
- [ ] Create product for each active SKU (cable clips, headphone hooks, labels)
- [ ] Use identical product copy from Etsy listings as the base; adapt for D2C tone (remove Etsy-specific language)
- [ ] Upload the same 5–7 photos used on Etsy (or higher-resolution versions)
- [ ] Set product type tags: "cable-management," "desk-accessories," "3d-printed"
- [ ] Enable inventory tracking per product (critical for multi-channel sync — see UNIFIED_INVENTORY_MODEL.md)

### 2.4 Shipping Configuration

- [ ] Install **Pirate Ship** or **Shippo** Shopify app (free base tier for both)
  - Pirate Ship: Already used for Etsy fulfillment; same rates apply; install Shopify app to import Shopify orders
  - Shippo: $0/month for up to 30 shipments/month; $19/month Professional for higher volumes
- [ ] In Shopify Admin: Settings → Shipping and delivery → Create shipping profile
  - Domestic USPS Ground Advantage: $0 free shipping (bake cost into product price) or calculated carrier rate (recommended for Shopify — buyer sees exact cost vs. Etsy where shipping is hidden in price)
  - International: Enable 5 key markets (CA, UK, AU, DE, FR) via USPS First Class International; configure Shippo for customs document auto-generation (CN22/CN23 forms)
- [ ] Set processing time in product descriptions: "Ships in 1–2 business days"

---

## Part 3: Inventory Sync — Shopify + Etsy + Amazon

### 3.1 The Sync Architecture Problem

ModRun runs three separate inventory contexts simultaneously:
1. **Etsy made-to-order**: No finished goods inventory; only filament tracking matters
2. **Amazon FBA**: Forward stock physically in Amazon's warehouse; Amazon tracks it
3. **Shopify D2C**: Self-fulfilled from home/workshop; tracks finished goods inventory

The critical failure point is overselling: if Shopify and Etsy share inventory and both sell the same unit simultaneously, one customer gets their order cancelled. At ModRun's made-to-order model, this risk is lower than it appears (you can just print more) but the platform penalty for a cancelled order is high (Etsy seller score, Amazon ODR).

**Recommended architecture at Phase 3 scale** (50–200 units/month total):

```
INVENTORY SOURCE OF TRUTH: Craftybase
    ↓
CHANNELS:
├── Etsy: Made-to-order (infinite virtual inventory; Craftybase tracks filament only)
├── Amazon FBA: Amazon's own inventory system (separate; not synced to Craftybase)
└── Shopify D2C: Finished goods inventory → synced from Craftybase to Shopify via API
```

**Why Etsy and Shopify can share a Craftybase source of truth without oversell risk**:
- Etsy made-to-order: each order triggers a print job; listing quantity stays at 999 (never depletes)
- Shopify D2C: tracks a small finished goods buffer (7–14 units); if stock hits 0, listing shows "Out of stock" until next print run
- Amazon FBA: completely separate; Amazon tracks its own warehouse inventory; no sync needed with Craftybase

### 3.2 Craftybase Shopify Integration Setup

- [ ] In Craftybase: Settings → Integrations → Shopify → Connect store
- [ ] Authorize with Shopify store URL and API credentials
- [ ] Map each Shopify product to its Craftybase product (same SKU structure as Etsy mapping)
- [ ] Set sync direction: Craftybase → Shopify (Craftybase is source of truth; push stock levels to Shopify)
- [ ] Enable automatic sync trigger: When Craftybase inventory updates (production run logged or order closed), push new quantity to Shopify
- [ ] Configure minimum threshold: when Shopify product quantity hits 2 units, trigger an alert to print a new pre-build plate

**Craftybase plan upgrade for multi-channel**:
- Studio plan ($49/month): Supports Etsy + Shopify; 250 order lines/month — sufficient through 200 combined orders/month
- Business plan ($129/month): Adds hourly sync, 5,000 order lines/month, Square — upgrade when monthly orders exceed 250

**Limitation**: Craftybase does not currently sync with Amazon. Amazon FBA inventory must be managed separately in Seller Central. This is acceptable because FBA inventory is physically at Amazon's warehouse and cannot be allocated to Shopify orders anyway.

### 3.3 QuickSync as Alternative/Supplemental Sync Tool

For direct Etsy ↔ Shopify listing synchronization (beyond inventory — also syncing product descriptions, prices, photos):

**QuickSync** ($19/month Lite, $29/month Pro) syncs:
- Product inventory quantities between Etsy and Shopify in real-time
- Order data from both channels
- Supports Etsy, Shopify, Amazon, eBay, TikTok, Square

**When to use QuickSync instead of (or alongside) Craftybase**:
- If maintaining identical product listings on both Etsy and Shopify and want one update to propagate to both
- If managing more than 10 active SKUs where manual price/description updates across channels become error-prone
- If adding Amazon Seller Central to the sync chain (Craftybase does not sync Amazon; QuickSync Pro does)

**QuickSync for three-channel (Etsy + Amazon + Shopify) sync**:
- Pro plan ($29/month): Syncs all three channels; real-time inventory update on sale
- Set a channel-specific buffer stock allocation: 
  - Amazon: managed in Amazon Seller Central (forward stock)
  - Etsy: virtual quantity 999 (made-to-order; never depletes)
  - Shopify: real finished goods inventory (depletes on sale; triggers pre-build alert)
- Result: A Shopify sale decrements Shopify inventory in QuickSync and pushes to Craftybase; a print run in Craftybase pushes replenished quantity back to Shopify

**Cost summary**:
- Craftybase Studio ($49/month) + QuickSync Pro ($29/month) = $78/month total sync infrastructure
- Justified at 50+ combined monthly orders; ROI payback is ~2 prevented oversell incidents per month

### 3.4 Sync Frequency Requirements

| Sync Event | Required Frequency | Tool | What Updates |
|---|---|---|---|
| Sale on any channel | Immediate (< 60 sec) | QuickSync / Craftybase auto-trigger | Shopify inventory decrements |
| Production run completion | Same-day (within 4 hours) | Craftybase manual log → auto-push | Shopify inventory increments |
| Amazon FBA restock | Manual (not synced) | Amazon Seller Central | Amazon inventory only |
| Price change | Within 24 hours | QuickSync or manual | All channels updated from Craftybase |
| New SKU addition | Within 48 hours | QuickSync product sync | New product pushed to Etsy/Shopify |

---

## Part 4: Automated Order-to-Fulfillment Workflow (Shopify)

### 4.1 Automation Trigger Chain

```
SHOPIFY ORDER PLACED
    ↓
EMAIL NOTIFICATION → inbox + Pirate Ship/Shippo app
    ↓
PIRATE SHIP: Import Shopify order → auto-populated with buyer address
    ↓
PRINT LABEL (USPS Ground Advantage)
    ↓
PICK FROM FINISHED GOODS BUFFER (if available)
    OR
TRIGGER PRINT JOB (if buffer depleted)
    ↓
PACKAGE + APPLY LABEL
    ↓
SHIP
    ↓
PIRATE SHIP AUTO-UPDATES SHOPIFY: Marks order fulfilled + tracking number inserted
    ↓
SHOPIFY SENDS AUTOMATED TRACKING EMAIL TO CUSTOMER
    ↓
CRAFTYBASE CLOSES ORDER: COGS recorded, inventory decremented
```

**Processing time commitment for Shopify**: 1–2 business days (same as Etsy). Shopify allows you to set this in the product description and checkout page. Do not promise same-day shipping until the finished goods buffer is established (7–14 units pre-built).

### 4.2 Pirate Ship Shopify Integration

- [ ] In Pirate Ship: Settings → Store Connections → Shopify → Connect
- [ ] Authorize with Shopify store credentials
- [ ] Enable: Import Shopify orders (automatic, all open orders appear in "Ship" queue)
- [ ] Enable: Auto-mark as fulfilled when label purchased (sends fulfillment notification to Shopify, which sends tracking email to customer)
- [ ] Set default package dimensions per SKU (saves manual entry per order):
  - Cable clips: 6 × 4 × 1 in, 3.5 oz
  - Starter Bundle: 8 × 6 × 2 in, 6 oz
  - Headphone Hook: 8 × 4 × 2 in, 4 oz
  - Magnetic Labels 10-pack: 6 × 4 × 1 in, 5 oz

### 4.3 Post-Purchase Email Sequence (Klaviyo)

Email marketing is the primary customer retention mechanism for Shopify D2C. Klaviyo's free plan supports 500 contacts and 1,000 emails/month — sufficient through Phase 3 launch.

- [ ] Install Klaviyo app from Shopify App Store (free for up to 500 contacts)
- [ ] Connect Klaviyo to Shopify: Settings → Integrations → Shopify → Connect
- [ ] Build three automated email flows:

**Flow 1 — Post-Purchase (trigger: order placed)**:
- Email 1 (immediate): Order confirmation + estimated ship date + "Your order is entering the print queue" message (sets expectation for made-to-order model)
- Email 2 (Day 3 after ship): "Your ModRun order is on its way" + setup tips (installation guide link or PDF attachment)
- Email 3 (Day 10 after delivery): "How's your ModRun setup?" + product review request + "Here's 10% off your next order" (coupon code drives repeat purchase conversion)

**Flow 2 — Repeat Customer Win-Back (trigger: no purchase in 90 days)**:
- Email 1 (Day 90): "New products added" + feature announcement (headphone hook if cable clip buyer, labels if workshop buyer)
- Email 2 (Day 105): "10% off for returning customers" + expiration date urgency

**Flow 3 — Abandoned Cart (trigger: add to cart + no purchase after 2 hours)**:
- Email 1 (2 hours): "You left something in your cart" + product photo + direct checkout link
- Email 2 (24 hours): "Still thinking it over?" + review quote from Etsy (social proof)

**Expected email channel economics**:
- Email CAC: $2–$4 per converted customer (2026 benchmark) vs. $35–$85 for paid social
- Email drives 15–25% of D2C revenue for established small Shopify stores
- The post-purchase + repeat purchase email flows are the mechanism that brings LTV/CAC above 3:1

---

## Part 5: Traffic Sources — Shopify D2C

### 5.1 Organic Traffic Sources (Zero CAC)

These drive Shopify traffic without paid acquisition cost:

**Package insert QR codes (highest ROI)**:
- Include in every Etsy and Amazon shipment: "Visit modrun.com for 10% off your next order + exclusive bundles"
- QR code links to Shopify product page or email opt-in
- Conversion rate: 3–8% of QR code scans
- At 50 Etsy shipments/month: 1–4 additional Shopify visitors/month; at 200 shipments/month: 6–16 visitors
- Cost: $0.02/card (printed on thank-you card stock)

**Organic social media (Instagram, Pinterest)**:
- Pinterest: Workspace organization is a top Pinterest category; lifestyle shots of desk setups generate long-tail organic traffic
- Instagram: 3D printing process videos (Bambu P1S time-lapse) are organic engagement drivers in the maker community
- No paid spend initially; organic only
- Expected outcome: 50–200 monthly visitors by Month 9 (organic social takes 3–6 months to build)

**Google organic (SEO)**:
- Blog posts on Shopify store targeting desk organization keywords: "how to organize desk cables," "3D printed desk accessories"
- Long-tail, low-competition terms at launch; builds over 6–12 months
- One 1,000-word blog post per month minimum

### 5.2 When to Start Paid Acquisition

Do not start paid Meta or Google ads until:
- Shopify store has been live for 30+ days (baseline organic conversion data)
- Shopify store conversion rate is ≥ 2% on organic/email traffic (proves the funnel works before paying to fill it)
- Email list has 200+ contacts (retargeting audiences need minimum size for effective Facebook/Instagram audience matching)

**First paid channel recommendation**: Google Shopping ads (not Meta). Google Shopping targets buyers actively searching for your product terms — lower CAC and higher purchase intent than Meta social. Expected Google Shopping CAC for desk accessories: $35–$55 vs. $45–$85 for Meta.

**Initial paid budget**: $5/day ($150/month) as a test budget. Evaluate 30-day ROAS before scaling. Target ROAS of 3× ($450 revenue on $150 ad spend).

---

## Part 6: Shopify D2C Launch Checklist

### Pre-Launch (7–10 days before going live)

- [ ] Shopify store fully configured (theme, products, pricing, policies)
- [ ] Shopify Payments activated and verified
- [ ] Pirate Ship or Shippo integrated (test with a $0 dummy order)
- [ ] Craftybase connected to Shopify (test inventory sync with a manual stock adjustment)
- [ ] QuickSync connected to Etsy + Shopify (test real-time inventory deduct)
- [ ] Klaviyo email flows built and tested (send test emails to yourself)
- [ ] Domain pointing correctly to Shopify store (DNS propagation complete)
- [ ] All product pages have 5+ photos, complete descriptions, and correct pricing
- [ ] Cart and checkout tested on mobile (70%+ of ecommerce traffic is mobile)
- [ ] Google Analytics 4 installed on Shopify store (track traffic sources from day one)
- [ ] Meta Pixel installed (even if not running ads — start building audience data now)

### Launch Day

- [ ] Announce Shopify store to Etsy customer email list (offer 10% first-order discount)
- [ ] Add "Also available at modrun.com" to all Etsy shop announcement text
- [ ] Update Amazon Handmade storefront with website link (permitted by Amazon TOS if no incentive is offered)
- [ ] Share on social media (if accounts exist)

### First 30 Days Post-Launch

- [ ] Monitor Shopify Analytics: traffic sources, conversion rate, average order value daily
- [ ] Monitor Klaviyo: email open rates (target 35%+), click rates (target 5%+), post-purchase email conversion (target 8–12%)
- [ ] Track email list growth rate
- [ ] Calculate 30-day Shopify CAC: (total ad spend + email tool cost) / new customers
- [ ] If CAC > $80: Do not scale ad spend; focus on organic and email channel improvement first

---

## Sources

- [Shopify Pricing 2026 — Taxomate](https://taxomate.com/blog/shopify-fees)
- [Shopify Fees 2026 — Qualimero](https://qualimero.com/en/blog/shopify-fees)
- [Printful Warehousing Discontinuation — Printful Help Center](https://help.printful.com/hc/en-us/articles/21048694941340-What-should-I-know-about-the-Dallas-warehousing-service-closure)
- [QuickSync Pricing and Features — QuickSync.pro](https://quicksync.pro/)
- [Craftybase Etsy + Shopify Sync 2026 — Craftybase Blog](https://craftybase.com/blog/sync-etsy-and-shopify-inventory)
- [D2C CAC Benchmarks 2026 — Tenten.co](https://tenten.co/shopify/d2c-cac-benchmarks-2026/)
- [Shopify International Shipping Guide 2026 — FreightAmigo](https://www.freightamigo.com/en/blog/ecommerce-logistics/shopify-international-shipping-guide-2026-cross-border-strategies-for-global-sellers/)
- [Shopify CAC Guide 2026 — EasyAppsEcom](https://easyappsecom.com/guides/shopify-customer-acquisition-guide)
- [LitCommerce Shopify-Amazon Integration — LitCommerce](https://litcommerce.com/shopify-amazon-integration/)
- [Multi-Channel Inventory Sync 2026 — US Tech Automations](https://ustechautomations.com/resources/blog/automate-multi-channel-inventory-sync-ecommerce-2026)
- Internal: `fulfillment-workflow.md`, `UNIFIED_INVENTORY_MODEL.md`
