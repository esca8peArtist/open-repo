---
title: "Unified Inventory Model — ModRun Multi-Channel Operations"
created: 2026-05-21
status: production-ready
scope: "Inventory tracking schema, channel-specific stock types, sync procedures, oversell prevention, backorder handling, and seasonal forecasting integration across Etsy + Amazon FBA + Shopify D2C"
confidence: high
related: inventory-forecast-model.md, MULTI_CHANNEL_SALES_ARCHITECTURE.md, SHOPIFY_PRINTFUL_INTEGRATION_GUIDE.md, fulfillment-workflow.md
---

# Unified Inventory Model — ModRun

**Lead finding**: ModRun's made-to-order architecture fundamentally changes the multi-channel oversell calculus. Unlike a product business with a fixed warehouse count, ModRun has effectively unlimited virtual inventory for Etsy (print on demand), a fixed forward stock count for Amazon FBA (physically locked in Amazon's warehouse), and a small finished goods buffer for Shopify D2C. Oversell risk is not symmetric across channels — it is near-zero on Etsy, low on Shopify if buffer is managed, and an Amazon ODR risk if FBA stock hits zero and orders queue. The unified inventory model must account for these three distinct inventory types separately while maintaining a single source of truth for raw material planning.

---

## Part 1: Inventory Type Architecture

### 1.1 Three Inventory Types for ModRun

| Inventory Type | Channel | Physical Location | Replenishment Method | Oversell Risk |
|---|---|---|---|---|
| Type 1: Virtual (filament-backed) | Etsy | n/a (made-to-order) | Filament reorder | Near-zero (print more) |
| Type 2: FBA Forward Stock | Amazon FBA | Amazon Fulfillment Center | Batch print → ship to FC (10–16 day lead time) | Medium (if stock hits 0, lose Prime badge + ODR risk on queued orders) |
| Type 3: Finished Goods Buffer | Shopify D2C | Home workshop | Print-on-demand from filament | Low (if buffer depletes, listing shows "Out of stock") |

### 1.2 Single Source of Truth: Craftybase

Craftybase serves as the inventory system of record. It tracks:
- Raw material inventory (filament spools by color and material type)
- Finished goods inventory (units available for Shopify D2C)
- COGS per order (deducted as orders close)
- Production runs (prints completed → units added to finished goods)

**Craftybase does NOT track**:
- Amazon FBA inventory (tracked in Amazon Seller Central)
- Etsy virtual inventory (maintained at 999 perpetual; made-to-order never depletes)

```
INVENTORY HIERARCHY

Craftybase (Source of Truth)
├── Raw Materials
│   ├── PLA+ Black [X kg on hand]
│   ├── PLA+ White [X kg on hand]
│   ├── PLA+ Grey [X kg on hand]
│   └── PETG Black [X kg on hand]
├── Finished Goods (Shopify D2C buffer)
│   ├── Starter Bundle [X units]
│   ├── Standard 3-Pack [X units]
│   ├── Pro Expansion Pack [X units]
│   ├── Headphone Hook [X units]
│   └── Magnetic Labels 10-pack [X units]
└── Orders (imported from Etsy + Shopify)

Amazon Seller Central (Separate System)
├── FBA Inventory (forward stock in warehouse)
│   ├── Starter Bundle [X units at Amazon FC]
│   ├── Pro Expansion Pack [X units at Amazon FC]
│   └── Standard 3-Pack [X units at Amazon FC]
└── FBA Orders (Amazon fulfills independently)

Etsy (Virtual)
└── All listings set to quantity 999 (perpetual; never depletes)
```

---

## Part 2: Inventory Tracking Schema

### 2.1 Finished Goods Tracker (Google Sheets — Shopify D2C Buffer)

Maintain as a live sheet. Update each time a production run completes or a Shopify order ships.

**Sheet: "Finished Goods"**

| Column | Content | Example |
|---|---|---|
| SKU | Internal product code | modrun_starter_bundle_black |
| Product Name | Human-readable | Starter Bundle — Black Rail + 3 Black Clips |
| Units On Hand | Current finished goods count | 12 |
| Units In Queue | Currently printing for this SKU | 0 |
| Total Available | On Hand + In Queue | 12 |
| Weekly Velocity (Shopify) | Avg Shopify orders/week for this SKU | 3 |
| Days of Supply | Total Available ÷ Daily Velocity | 28 |
| Reorder Point (units) | Buffer below which new print run triggers | 7 |
| Buffer Status | Formula: IF(On Hand < Reorder Point, "PRINT NOW", "OK") | OK |
| Last Production Date | Date of last print run for this SKU | 2026-05-20 |
| Notes | Color, material variant, batch notes | Black PLA+ batch #4 |

**Reorder point calculation for Shopify D2C buffer**:
- At 50 combined units/month (early Phase 3): Shopify takes ~25% of volume = 12–13 units/month = 3 units/week
- Print run lead time: 4–8 hours (same-day production possible)
- Safety stock: 1 day of demand = ~0.5 units → round to 2 units
- Reorder point: (3 units/week × 0.5 day lead time / 7 days) + 2 = 2.2 → **round to 3 units**
- **Practical rule at early Phase 3**: Pre-build 7-unit buffer per active Shopify SKU (2–3 day supply); trigger a print plate when on-hand drops below 3 units

### 2.2 FBA Inventory Tracker (Amazon Seller Central + Supplemental Sheet)

Amazon Seller Central provides its own inventory dashboard. Supplement with a local tracking sheet for restock planning.

**Sheet: "Amazon FBA Stock"**

| Column | Content | Example |
|---|---|---|
| ASIN | Amazon product identifier | B0XXXXXXXX |
| SKU | ModRun internal | modrun_starter_bundle |
| FNSKU | Amazon warehouse label code | X0XXXXXXXX |
| Units at FC | From Seller Central "Manage Inventory" | 48 |
| Units in Transit | Shipped to FC, not yet received | 0 |
| Total Amazon Stock | FC + Transit | 48 |
| 30-day Sales Velocity | From Seller Central Business Reports | 30 units |
| Days of Supply | Total Stock ÷ (30-day velocity ÷ 30) | 48 days |
| FBA Restock Trigger | 28-day supply threshold | 28 days |
| Restock Status | IF(Days of Supply < 28, "RESTOCK NOW", "OK") | OK |
| Last Restock Date | Date batch shipped to Amazon | 2026-05-10 |
| Batch Size | Units in most recent batch | 50 |

**FBA restock rules**:
- Restock trigger: Days of Supply drops below 28 days (triggers LILL fee after 180-day new-ASIN exemption expires)
- Minimum restock batch: 35 units (to restore 28+ day supply and avoid LILL)
- Target restock batch: 50–75 units (45–60 day sell-through at 30–50 units/month; stays comfortably above 28-day threshold)
- Lead time from print decision to FBA live: 10–16 days — start restock when Days of Supply hits 28, not 14

### 2.3 Filament Raw Materials Tracker (Craftybase + Google Sheets)

Per `inventory-forecast-model.md` Section 2.3, filament is the primary constraint on all production. Update Craftybase when any spool is opened.

**Sheet: "Filament Tracker"**

| Column | Content | Example |
|---|---|---|
| Material | Color + type | PLA+ Black |
| Supplier | Primary supplier | eSUN (Amazon) |
| Spools On Hand | Physical count | 3 |
| kg/Spool | Spool weight | 1.0 kg |
| Total kg | Spools × kg/spool | 3.0 kg |
| Daily Consumption | kg/day at current production rate | 0.21 kg (at 20 units/week) |
| Days of Supply | Total kg ÷ Daily Consumption | 14.3 days |
| Reorder Point (kg) | 14-day supply + formula buffer | 3.74 kg |
| Reorder Status | IF(Total kg < Reorder Point, "ORDER NOW", "OK") | OK |
| Last Order Date | Date of last purchase | 2026-05-15 |
| Order Quantity (kg) | Standard order size | 10 kg (1 case) |

**Color-specific tracking**: Maintain a separate row for each color in active production. At Phase 1/2 launch, track Black, White, and Grey PLA+ separately. Add PETG Black when the outdoor/ASA variant is activated.

---

## Part 3: Oversell Prevention

### 3.1 Oversell Risk by Channel

| Channel | Oversell Scenario | Platform Penalty | Prevention Mechanism |
|---|---|---|---|
| Etsy | Made-to-order listing hits 0 quantity (never happens if perpetual quantity set correctly) | Order cancellation required → harms Star Seller status | Set all Etsy listings to quantity: 999; never reduce manually |
| Amazon FBA | FBA stock hits 0; new orders queue and cannot fulfill | ODR risk if order is cancelled; Prime badge removed; ranking drops | Track days of supply; trigger restock at 28 days; never let stock hit 0 |
| Shopify D2C | Finished goods buffer depletes; Shopify sells last unit same instant as Etsy purchase | No platform penalty; customer disappointed; refund/delay required | Enable "Continue selling when out of stock: NO" in Shopify product settings; buffer depletes → product shows Out of Stock automatically |

### 3.2 Etsy Oversell Prevention (No Shared Inventory)

Etsy listings must NEVER share inventory with Shopify.

The naive integration mistake is connecting Shopify and Etsy via QuickSync with shared inventory (e.g., both channels see 12 units). When Shopify sells 3 and Etsy sells 3 simultaneously, QuickSync may report 6 total sold but if sync delay is 60 seconds, both channels could oversell the same units.

**ModRun-specific protection**: Since Etsy is made-to-order, there is no shared pool. Etsy listings stay at 999 permanently. A sale on Etsy does not decrement Shopify inventory. A sale on Shopify does not change the Etsy quantity. The channels are inventory-independent.

In QuickSync (if installed):
- Set Etsy listings to "Unmanaged" quantity (do not sync quantity to/from Etsy)
- Set Shopify listings to "Managed" quantity (sync from Craftybase)
- Amazon FBA: excluded from QuickSync quantity management

### 3.3 Shopify D2C Oversell Prevention

Shopify's default allows sales of out-of-stock products ("Continue selling when out of stock" is enabled by default). Disable this.

- [ ] In Shopify Admin: Each product → Inventory section → uncheck "Continue selling when out of stock"
- [ ] In Shopify Admin: Settings → Notifications → enable "Out of stock" email alert (triggers when product reaches 0 units)
- [ ] In Craftybase: Set low inventory alert at 3 units for each active Shopify SKU (alert fires before Shopify reaches 0)

**Backorder handling when Shopify shows Out of Stock**:
- Option A (recommended at current scale): Show "Out of Stock — Back in 2 days" with a pre-order button
  - Add an "Add to Waitlist" form (Klaviyo can collect email + send automated restock notification)
  - Time to restock: 4–8 hours from print trigger; ship next business day
  - Customer experience: "We'll notify you the moment this is available" is better than cancellation
- Option B: Accept backorder with extended processing time
  - Shopify allows processing time: "Ships in 3–5 business days" set on out-of-stock product
  - Risk: customer doesn't read the processing time; opens dispute after 2 days

**Recommended setting**: Option A (waitlist). The Klaviyo restock notification email generates a 15–25% conversion rate from waitlist subscribers — a free, high-converting email trigger.

### 3.4 Amazon FBA Stockout Prevention

FBA stockout is the highest-consequence oversell scenario. When FBA stock hits 0:
1. Prime badge is removed immediately
2. Listing drops in search ranking
3. Regaining ranking after a stockout takes 2–4 weeks (Amazon's algorithm penalizes sales velocity gaps)
4. During restocking, the 10–16 day lead time means 2+ weeks of lost Prime-eligible sales

**Prevention**:
- Hard rule: Never let Amazon FBA units drop below 15 (two-week safety buffer at 30 units/month velocity)
- Alert trigger: When Seller Central shows < 28 days of supply on any FBA ASIN, print and ship a restock batch immediately
- Never cut FBA inventory to fund Shopify demand: Shopify D2C can absorb a 2-day out-of-stock; Amazon FBA cannot

---

## Part 4: Backorder Handling Strategy

### 4.1 Etsy Backorders

Etsy does not support backorders natively. If production capacity is temporarily exceeded:

**Short-term demand spike (1–3 days)**:
- Update Etsy processing time from "1–2 business days" to "3–5 business days"
- Do not cancel existing orders; just extend the processing window
- Print overnight batch to clear backlog

**Extended demand spike (4–14 days)**:
- Update processing time to "5–7 business days"
- If orders are outpacing 14-day capacity: "temporarily pause" the listing (deactivate, not delete) to prevent new orders until backlog clears
- Alert in Etsy shop announcement: "High demand — processing time temporarily extended to 7 days"
- Per `inventory-forecast-model.md` Section 4.2: if sustained 5× spike, activate JLC3DP contract manufacturer backup

### 4.2 Amazon FBA Backorders

Amazon FBA does not support backorders — if FBA stock hits 0, the listing becomes "Temporarily out of stock" and loses Prime. Amazon cannot hold orders for future inventory.

**Prevention is the only strategy**: FBA does not have a backorder recovery path. If stock runs out, orders are lost (buyers buy from a competitor), not deferred. The 28-day days-of-supply restock trigger in Section 2.2 is non-negotiable.

### 4.3 Shopify D2C Backorders

Shopify natively supports backorder selling with custom messaging.

**Setup**:
- [ ] In Shopify Admin: Product → Inventory → check "Continue selling when out of stock" (enable this for pre-order/backorder only)
- [ ] Add custom messaging via product description or theme customization: "Currently out of stock. Pre-order now — ships within 3 business days."
- [ ] In checkout: display the shipping message clearly so customer understands before completing purchase

**Backorder acceptance criteria**:
- Maximum backorder acceptance window: 5 business days (to be printed and shipped)
- If production delay > 5 business days: disable backorders and show out-of-stock
- Communicate proactively: Klaviyo automated email on order confirmation if flagged as backorder — "Thank you for your pre-order. We'll ship your order within [X] business days."

---

## Part 5: Seasonal Forecasting Integration

### 5.1 Seasonal Demand Calendar (Multi-Channel View)

From `ETSY_SEO_STRATEGY_Q2_Q3_2026.md` Section 4 and `inventory-forecast-model.md` Section 1.2, cross-referenced with multi-channel behavior:

| Period | Etsy Demand Multiplier | Amazon Demand Multiplier | Shopify Demand Multiplier | Inventory Action |
|---|---|---|---|---|
| May–June 2026 | 85–100% (baseline) | n/a (Phase 2 not yet launched) | n/a (Phase 3 not yet launched) | Build filament safety stock before Q3 |
| July–August 2026 | 105–135% (BTS surge) | 100–120% (Prime Day) | 100–110% | Pre-build FBA batch in late June; prime Shopify buffer to 14 units |
| September 2026 | 90–105% | 90–100% | 90–100% | Normal cadence; update Q4 pre-build plan |
| October–November 2026 | 105–155% (Q4 ramp) | 100–130% (holiday) | 110–140% (gift buyers) | Pre-build 3× normal FBA batch in early October; Shopify buffer to 21 units |
| December 2026 | 130–160% (peak) | 125–145% (peak) | 130–150% (gift peak) | All channels at maximum pre-build; filament safety stock at 30 kg |
| January 2027 | +30–40% (New Year org) | +20–30% | +25–35% | January is highest single-month demand; pre-build in December |

### 5.2 Seasonal Pre-Build Protocol

**Q4 (October–December) Pre-Build Schedule**:

| Action Date | Action | Quantity | Channel |
|---|---|---|---|
| September 1 | Print 100-unit FBA batch (double normal) | 100 units | Amazon FBA |
| September 15 | Ship FBA batch to Amazon FC | 100 units | Amazon FBA |
| September 25 | Verify FBA batch received and live | — | Amazon FBA |
| October 1 | Build Shopify D2C buffer to 21 units per top 3 SKUs | 63 units total | Shopify |
| October 1 | Add Q4 gift tags to all Etsy and Amazon listings | — | Etsy + Amazon |
| October 15 | Review FBA days of supply; trigger 75-unit restock if below 45 days | 75 units (if needed) | Amazon FBA |
| November 1 | Build FBA to 150+ units (covers November + December peak) | As needed | Amazon FBA |
| November 15 | Cap Amazon FBA stock at 90 days of supply (avoid peak storage fee tier) | — | Amazon FBA |
| November 30 | Etsy processing time: Update to "3–5 business days" (December rush) | — | Etsy |
| December 26 | Remove gift tags; update all listings to "New Year organization" framing | — | All channels |

**Q4 Amazon Storage Fee Warning**:
Amazon's storage fees increase to $2.40/cubic foot/month (vs. $0.78 off-peak) from October through December. At ModRun's 0.5–0.75 cubic feet per 50-unit batch, the peak-season storage cost is $1.20–$1.80/month total — negligible and not a reason to reduce FBA stock ahead of peak demand. The revenue loss from a stockout during Q4 far exceeds any storage fee savings.

### 5.3 January 2027 Pre-Build (Critical)

January is the highest-demand month for desk organization across all channels (120–150% above baseline on Etsy; similar pattern on Amazon and Shopify). Listings must be live, stocked, and optimized **before** January 1 — listings launched in December are too new to rank organically by the peak January 7–21 window.

**December 1–15 pre-build actions**:
- Etsy: No inventory action (made-to-order); update descriptions to "New Year desk organization" framing by December 26
- Amazon FBA: Ensure 100+ units in warehouse by December 15; Amazon receiving slows during December holidays
- Shopify: Buffer to 28 units per top 3 SKUs by December 20

---

## Part 6: Multi-Channel Sync Procedures — Master Reference

### 6.1 Daily Operations (5 minutes)

| Action | Tool | What It Does |
|---|---|---|
| Check Craftybase Finished Goods dashboard | Craftybase | Identify any Shopify SKU below reorder point |
| Check Amazon Seller Central "Manage Inventory" | Amazon Seller Central | Verify FBA days of supply; trigger restock if below 28 days |
| Check Filament Tracker sheet | Google Sheets | Confirm no filament color below reorder point |

### 6.2 Weekly Operations (15 minutes, Sunday)

| Action | Tool | What It Does |
|---|---|---|
| Calculate 7-day velocity per channel | Etsy Stats + Amazon Business Reports + Shopify Analytics | Update demand forecast in inventory sheets |
| Physical filament count | Manual | Verify Filament Tracker matches actual stock |
| Update Finished Goods sheet | Manual | Count all pre-built units on shelf |
| Verify QuickSync last sync time | QuickSync dashboard | Confirm no sync failures in past 7 days |
| Review Amazon FBA sell-through rate | Amazon Business Reports | Catch declining velocity early (signals listing issue) |

### 6.3 Monthly Operations (30 minutes, end of month)

| Action | Tool | What It Does |
|---|---|---|
| Reconcile all channel inventory with Craftybase | Craftybase + manual | Catch any discrepancies between tracked and actual stock |
| Download Amazon FBA inventory report | Amazon Seller Central | Archive for tax/COGS records |
| Calculate channel-level margins | Craftybase P&L + channel fee reports | Verify each channel is still operating at target margin |
| Seasonal forecast review | Seasonal demand calendar (Section 5.1) | Determine if upcoming period requires pre-build actions |
| Update filament safety stock targets | Inventory Forecast Model formulas | Scale safety stock with increasing demand |

### 6.4 Emergency Procedures

**Scenario: Shopify shows Out of Stock on a high-demand SKU**
1. Check Craftybase: Are units actually at 0 or did sync fail?
2. If sync failure: Manually update Shopify product inventory count in Shopify Admin → Products → Inventory
3. If genuinely 0: Start print run immediately; print 12-unit plate (4–8 hour completion)
4. Update Shopify product to show "Back in 2 days" message; Klaviyo waitlist captures demand
5. Root cause: Add that SKU to the daily buffer monitoring routine

**Scenario: Amazon FBA stock hits 0 unexpectedly**
1. Immediately list the affected ASIN for Amazon FBM (self-fulfilled) as a temporary bridge
   - In Seller Central: Add FBM offer to the same ASIN; set processing time to 3 business days
   - This preserves listing visibility (even without Prime) while FBA restock is in transit
2. Print emergency restock batch (50 units); ship within 48 hours via FedEx overnight to Amazon FC (~$40 premium)
3. At FC receiving (estimated 5–7 business days), FBA listing restores Prime badge
4. Estimated ranking recovery from stockout: 2–4 weeks

**Scenario: Etsy demand spike exceeds print capacity**
1. Extend processing time to 5–7 business days immediately (prevents late shipment penalty)
2. Activate JLC3DP backup order if spike duration > 5 days (see `inventory-forecast-model.md` Section 4.2)
3. Do NOT attempt to draw from Shopify D2C buffer to fulfill Etsy orders (different fulfillment contexts; creates tracking confusion)

---

## Part 7: Sync Tool Configuration Summary

| Tool | Plan | Monthly Cost | Channels Synced | What It Manages |
|---|---|---|---|---|
| Craftybase | Studio | $49 | Etsy, Shopify, Square | Source of truth: raw materials, COGS, finished goods, Etsy/Shopify order import |
| QuickSync | Pro | $29 | Etsy, Shopify, Amazon | Real-time inventory quantity sync; order sync; price propagation |
| Amazon Seller Central | Included (Professional plan) | $0 (Handmade waiver) | Amazon only | FBA inventory, FBA orders, shipping |
| Pirate Ship | Free | $0 | Etsy, Shopify | Shipping labels, carrier rate comparison |
| Klaviyo | Free (≤500 contacts) | $0 | Shopify | Email marketing, post-purchase flows, restock alerts |
| Google Sheets | Free | $0 | All (manual tracking) | Filament tracker, FBA tracker, production queue |

**Total sync infrastructure cost**: $78/month (Craftybase + QuickSync)

**When to upgrade QuickSync to Ultra ($69/month)**: At 3+ channels with 2,500+ active SKUs or when international pricing (forex rules) is needed. Not required through Phase 3 with ModRun's current SKU count.

**When to replace Craftybase + QuickSync with Linnworks or Extensiv**: At 300+ monthly orders across 3+ channels or when 3PL integration is needed (ShipMonk, Simpl Fulfillment). Linnworks starts at ~$499/month and is overkill below that threshold.

---

## Part 8: Inventory Schema — Data Format Reference

For developers or if transitioning to an IMS (inventory management system) in Phase 4:

```
SKU Schema:
  sku_id: string (modrun_{product}_{color}_{size})
  Example: modrun_starter_bundle_black_std

Inventory Record:
  sku_id: string
  channel: enum [etsy, amazon_fba, shopify]
  quantity_on_hand: integer
  quantity_committed: integer (orders placed, not yet shipped)
  quantity_available: integer (on_hand - committed)
  reorder_point: integer
  reorder_quantity: integer
  last_updated: datetime
  sync_source: enum [craftybase, amazon_seller_central, manual]

Channel Allocation:
  etsy: virtual (quantity = 999, never depletes)
  amazon_fba: quantity at FC (tracked in Amazon Seller Central)
  shopify: finished_goods_buffer (tracked in Craftybase, synced to Shopify)

Filament Material Record:
  material_id: string (pla_black, pla_white, petg_black)
  quantity_on_hand_kg: float
  reorder_point_kg: float
  daily_consumption_kg: float
  supplier: string
  lead_time_days: integer
  status: enum [OK, REORDER_NOW, CRITICAL]
```

---

## Sources

- [Multi-Channel Inventory Sync 2026 — US Tech Automations](https://ustechautomations.com/resources/blog/automate-multi-channel-inventory-sync-ecommerce-2026)
- [How to Sync Etsy and Shopify Inventory 2026 — Craftybase](https://craftybase.com/blog/sync-etsy-and-shopify-inventory)
- [Multi-Channel Inventory Sync Oversell Prevention — Bazaroo](https://bazaroo.app/blog/multi-channel-inventory-sync-avoid-overselling)
- [QuickSync All-in-One App — Shopify App Store](https://apps.shopify.com/sqsync)
- [Track Inventory Across Amazon, Shopify & Etsy — Accountipro](https://accountipro.com/how-to-track-inventory-across-multiple-sales-channels-amazon-shopify-etsy/)
- [Amazon FBA Storage Fee Schedule 2026 — Brandwoven](https://gobrandwoven.com/resources/articles/amazon-2026-fees-breakdown-fba-referral-inbound-placement/)
- [Amazon Low Inventory Level Fee — AMZ Prep](https://amzprep.com/amazon-low-inventory-level-fee/)
- [Craftybase Inventory Sync App — Shopify App Store](https://apps.shopify.com/craftybase)
- Internal: `inventory-forecast-model.md`, `fulfillment-workflow.md`, `ETSY_SEO_STRATEGY_Q2_Q3_2026.md`
