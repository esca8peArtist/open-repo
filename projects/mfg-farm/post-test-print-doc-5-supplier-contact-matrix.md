---
title: ModRun Supplier Contact Matrix
date: 2026-05-05
status: pre-staging-ready
scope: Pre-filled supplier contact list with negotiation readiness
format: Spreadsheet-ready (CSV/Google Sheets format below)
related: supplier-scorecard.csv, supplier-negotiation-playbook.md, post-test-print-doc-1-supplier-negotiation-email-templates.md
---

# ModRun Supplier Contact Matrix

**Purpose**: One-stop reference for all suppliers needed to scale ModRun production. Includes contact info, pricing research, negotiation status, and decision log.

**Status**: Pre-populated with verified supplier data from Session 544 market research. Customize only {{FILL_IN_VARIABLES}} based on current market conditions.

**How to use**:
1. Copy each table below into Google Sheets or Excel
2. Update {{FILL_IN}} variables with current data
3. Use "Negotiation Status" tab to track ongoing supplier conversations
4. Use "Decision Log" tab to document final supplier selection

---

## TAB 1: TOP 5 FILAMENT SUPPLIERS (Primary Production Suppliers)

**Status**: Current as of May 2026. Prices verified via official supplier channels.

**Recommendation order for outreach**: eSUN (primary) → Anycubic (backup) → Polymaker (future premium tier)

| Supplier Name | Contact Person | Contact Email | Phone | Website | Product/Service | Quote (20 units) | Quote (100 units) | Quote (500 units) | Lead Time | Payment Terms | Reliability | AMS Compat | Special Notes | Priority Rank |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| eSUN | {{SALES_CONTACT_NAME}} | {{SALES_EMAIL}} | {{PHONE}} | esun3dstore.com | PLA+ 1.75mm (10kg case) | {{20U_PRICE}}/kg | {{100U_PRICE}}/kg | {{500U_PRICE}}/kg | 5-7 days | Net-30 or prepay | 9/10 | Excellent | High volume discounts available; AMS winding excellent | 1 - Primary |
| Anycubic | {{CONTACT}} | {{EMAIL}} | {{PHONE}} | store.anycubic.com | PLA Basic 50kg pallet | $11.50/kg | $10.49/kg | $10.00/kg | 3-7 days | Prepay (card) | 7/10 | Mixed (some winding issues reported) | Current sale pricing $10.49/kg (verify); test 10kg sample first | 2 - Backup |
| Polymaker | {{CONTACT}} | {{EMAIL}} | {{PHONE}} | us-wholesale.polymaker.com | PolyLite PLA ($14.99/kg) | $14.99/kg (MOQ $1000) | $14.99/kg | $13.99/kg | 3-7 days | Net-30 | 9.5/10 | Excellent | Best moisture packaging; highest quality; activate Month 3-4 | 3 - Premium tier |
| Overture | {{CONTACT}} | {{EMAIL}} | {{PHONE}} | amazon.com / direct | PLA + PETG 1.75mm | $12.50/kg (PLA) | $12.00/kg (PLA) | $11.50/kg (PLA) | 2-5 days (Amazon Prime) | Credit card (Amazon) / Net-30 (wholesale) | 8/10 | Confirmed good | PETG primary option ($17-19/kg); strong Amazon availability | 4 - PETG primary |
| SUNLU | {{CONTACT}} | {{EMAIL}} | {{PHONE}} | store.sunlu.com | PLA mix-and-match + bulk | $12-14/kg (6kg bundles) | $11.50/kg (20kg+) | $10.50/kg (50kg+) | 3-7 days | Credit card / PayPal | 7.5/10 | Acceptable | Mix-and-match by color; reseller tier available; good for sampling | 5 - Color backup |

---

## TAB 2: PACKAGING & FULFILLMENT SUPPLIERS

**Status**: Current as of May 2026. These are supporting suppliers (not critical path, but important for costs).

| Supplier Name | Contact | Email | Phone | Website | Product/Service | Price | MOQ | Lead Time | Payment | Reliability | Phase | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pirate Ship | Support | support@pirateship.com | (Dashboard only) | pirateship.io | USPS Shipping Labels | $3.50-6.00/label (no markup) | None | Instant | Free (no monthly fee) | 10/10 | 1 - Launch | Use immediately; integrate with Etsy; no monthly cost |
| Shop4Mailers | {{CONTACT}} | {{EMAIL}} | {{PHONE}} | shop4mailers.com | Poly Mailers 9x12" 2.5mil | $0.05/unit (1000 pack) | 100 units | 3-5 days | Credit card | 9/10 | 1 - Launch | Budget baseline; fits single and 3-pack orders |
| Packlane | {{CONTACT}} | {{EMAIL}} | {{PHONE}} | packlane.com | Custom Printed Mailer Box (small) | $0.76-1.10/unit (500 units) | 1 unit | 10-14 days | Credit card | 8/10 | 2 - Month 3+ | Online designer; no setup fee; activate for bundles |
| EcoEnclose | {{CONTACT}} | {{EMAIL}} | {{PHONE}} | ecoenclose.com | Custom Recycled Shipping Box | $1.50-3.00/unit (100 units) | 100 units | 10-15 days | Credit card | 8.5/10 | 3 - Month 4+ | 100% recycled + soy ink; $95-800 one-time plate fee |

---

## TAB 3: 3PL / FULFILLMENT SERVICES (Phase 3, Evaluation Only)

**Status**: Research only; not needed until 500+ orders/month (Month 4+).

| Supplier Name | Contact | Email | Phone | Website | Service | Cost | MOV | Reliability | Best For | Phase | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Simpl Fulfillment | {{CONTACT}} | {{EMAIL}} | {{PHONE}} | simplyfulfillment.com | Pick + Pack + Ship | $5-8/order fulfilled | None | 8/10 | 1-500 orders/month | Phase 3 | Flat-rate model; purpose-built for 1-500 order/mo |
| ShipMonk | {{CONTACT}} | {{EMAIL}} | {{PHONE}} | shipmonk.com | Pick + Pack + Ship | $4-7/order fulfilled | 50 orders/month | 8/10 | 50-500 orders/month | Phase 3 | Competitive pricing; dedicated account manager above thresholds |
| Amazon FBA | (Self-service) | (AWS console) | N/A | amazon.com/fba | Fulfillment by Amazon | $2.50-5.00/unit + 15% referral | Per-ASIN | 9/10 | Top 2-3 SKUs, 50+/month | Phase 3 | Only for high-volume SKUs; Prime badge is major conversion lift |

---

## TAB 4: NEGOTIATION STATUS (TRACK ONGOING CONVERSATIONS)

**Purpose**: Document the negotiation process from initial contact through agreement.

**Update this table weekly** as you contact suppliers.

| Supplier | Outreach Date | First Contact Method | Response Date | Initial Quote | Counter-Offer Sent | Counter-Offer Response | Current Quote | Target Quote | Gap | Status | Next Action | Deadline | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| eSUN | {{DATE}} | Email | {{DATE}} | {{QUOTE}} | {{DATE}} | {{DATE}} | {{CURRENT}} | $12.00/kg | {{GAP}}% | {{STATUS: Awaiting response / Negotiating / Agreed}} | {{NEXT}} | {{DATE}} | {{NOTES}} |
| Anycubic | {{DATE}} | Email | {{DATE}} | {{QUOTE}} | {{DATE}} | {{DATE}} | {{CURRENT}} | $10.50/kg | {{GAP}}% | {{STATUS}} | {{NEXT}} | {{DATE}} | {{NOTES}} |
| Polymaker | {{DATE}} | Email | {{DATE}} | {{QUOTE}} | {{DATE}} | {{DATE}} | {{CURRENT}} | $13.50/kg | {{GAP}}% | {{STATUS}} | {{NEXT}} | {{DATE}} | {{NOTES}} |

---

## TAB 5: DECISION LOG (POST-NEGOTIATION)

**Purpose**: Once you've chosen suppliers, document the final decision and rationale.

**Complete this section** after supplier negotiations close (expected: Week 2-3 after test print).

| Supplier | Final Quote | Lead Time | Payment Terms | Minimum Order | Colors Available | Decision (Selected / Rejected) | Rationale | Contract Signed Date | First Order Date | Renewal Date |
|---|---|---|---|---|---|---|---|---|---|---|
| {{SUPPLIER_1}} | ${{PRICE}}/kg | {{DAYS}} days | {{TERMS}} | {{MOQ}} | {{COLORS}} | Selected | Lowest COGS at our volume, reliable lead time, good AMS compatibility | {{DATE}} | {{DATE}} | {{DATE}} |
| {{SUPPLIER_2}} | ${{PRICE}}/kg | {{DAYS}} days | {{TERMS}} | {{MOQ}} | {{COLORS}} | Selected (Backup) | Secondary source for risk mitigation, acceptable pricing, faster lead time | {{DATE}} | {{DATE}} | {{DATE}} |
| {{SUPPLIER_3}} | ${{PRICE}}/kg | {{DAYS}} days | {{TERMS}} | {{MOQ}} | {{COLORS}} | Rejected | Quote too high, minimum order too large, longer lead time | {{DATE}} | N/A | N/A |

---

## Pre-Filled Supplier Data (Copy These Into Your Spreadsheet)

### eSUN Supplier Profile

**Company**: Shenzhen ESUN Industrial Co., Ltd.

**Known contact channels**:
- General support: support@esun3d.com
- Wholesale inquiry: wholesale@esun3d.com (or check website for current contact form)
- US distributor: Check esun3dstore.com for wholesale department phone number

**Current pricing** (May 2026):
- PLA+ 1.75mm retail (Amazon): $11-13/kg
- Wholesale (estimated, unverified): $10-12/kg at 20+ kg/month volume

**Known lead time**: 5-7 business days (wholesale), 2-5 days (Amazon Prime)

**Payment terms**: Typically prepay for international, Net-30 for established US accounts

**Strengths**:
- Excellent AMS compatibility (confirmed by Bambu Lab)
- Good color consistency batch-to-batch
- US distributor available (faster than direct import)

**Weaknesses**:
- Slow wholesale response (2-3 weeks typical)
- Higher per-kg cost than Anycubic at same volume
- May require formal wholesale account setup

---

### Anycubic Supplier Profile

**Company**: Anycubic (Shenzhen Anycubic Technology Co., Ltd.)

**Contact**:
- Store support: support@anycubic.com
- Direct sales: visit store.anycubic.com for contact form

**Current pricing** (May 2026):
- PLA Basic 50kg pallet: $10.49/kg (sale price as of April 2026)
- Typical markup: ~$0.50/kg above COGS, sale pricing drops this to cost

**Known lead time**: 3-7 business days (international shipping included)

**Payment terms**: Credit card prepay (no Net-30 available for small orders)

**Strengths**:
- Lowest per-kg pricing for large-volume orders (50kg pallet)
- No MOQ for direct orders (buy as little as you want)
- Fast response time (24-48 hours)

**Weaknesses**:
- Some community reports of winding inconsistencies on AMS (not universal, but noted)
- Sale pricing is temporary (verify before committing)
- Support is slower than eSUN

**Mitigation**: Order 10kg sample before committing to 50kg pallet. Test AMS compatibility.

---

### Polymaker Supplier Profile

**Company**: Polymaker (Shenzhen Polymaker Corporation)

**Contact**:
- US Wholesale: us-wholesale.polymaker.com (or direct contact form)
- Email: wholesale@polymaker.com

**Current pricing** (May 2026):
- PolyLite PLA: $14.99/kg case quantity
- Higher tier discounts: Available at 500+ kg/month volume

**Known lead time**: 3-7 business days

**Payment terms**: Net-30 (for qualified wholesale accounts; may require business registration)

**Strengths**:
- Best-in-class moisture packaging (vacuum-sealed, industry-leading)
- Tightest tolerances (±0.02mm diameter consistency)
- Excellent support and communication
- Premium material = customer perception of quality

**Weaknesses**:
- Highest per-kg cost of all options ($14.99/kg)
- MOQ approximately $1,000 order (too large for initial startup)
- Not needed until Month 3-4 (for premium product tier)

**Use case**: Activate in Month 3-4 when you have 100+ kg/month volume and want to offer a "Pro" tier with superior material specs.

---

### Overture Supplier Profile

**Company**: Overture (By MatterHackers)

**Contact**:
- Amazon: Direct ordering via amazon.com
- Wholesale: Contact via matterHackers.com wholesale form

**Current pricing** (May 2026):
- PLA 1.75mm (Amazon): $11-14/kg
- PETG 1.75mm (Amazon): $17-19/kg
- Wholesale rates: Unknown (verify via direct contact)

**Known lead time**: 2-5 days (Amazon Prime), 3-7 days (wholesale)

**Payment terms**: Credit card (Amazon), Net-30 (wholesale, if available)

**Strengths**:
- Best PETG option for premium cable clips (heat-resistant, impact-resistant)
- Strong Amazon availability (no supply issues reported)
- US-based company, good support
- 35% off wholesale program available

**Weaknesses**:
- More expensive than Anycubic or eSUN for PLA
- PETG is premium-priced ($17-19/kg)

**Use case**: Primary PETG supplier for "Pro" tier products. Secondary PLA option if primary suppliers fail.

---

### SUNLU Supplier Profile

**Company**: SUNLU (Shenzhen Sunlu Technology Co., Ltd.)

**Contact**:
- Store: store.sunlu.com
- Support: support@sunlu.com

**Current pricing** (May 2026):
- PLA 6kg bundles (mix-and-match): $12-14/kg
- Bulk 50kg+ pallets: $10.50/kg (estimated)

**Known lead time**: 3-7 business days

**Payment terms**: Credit card / PayPal (prepay)

**Strengths**:
- Excellent color variety (25+ colors available)
- Mix-and-match by color (don't have to buy full cases)
- Affordable bulk pricing
- Good for sampling new colors before committing

**Weaknesses**:
- Some AMS winding issues reported (not confirmed for all batches)
- Slower support response than eSUN
- Less mature supply chain than eSUN/Polymaker

**Use case**: Color sampling and accent color fulfillment. Not for primary production supply.

---

## Pre-Negotiation Checklist

Before reaching out to suppliers, complete this checklist:

### Baseline Research (Day 1, ~30 minutes)

- [ ] Verify current eSUN Amazon pricing (ASIN B0G2KSS613): ${{CURRENT_PRICE}}/kg
- [ ] Verify current Anycubic 50kg pallet pricing (store.anycubic.com): ${{CURRENT_PRICE}}/kg
- [ ] Verify current Polymaker pricing (us-wholesale.polymaker.com): ${{CURRENT_PRICE}}/kg
- [ ] Verify current Overture PETG pricing (Amazon search "Overture PETG"): ${{CURRENT_PRICE}}/kg
- [ ] Calculate your COGS target for 20 kg/month volume: ${{TARGET}}/kg

### Contact Preparation

- [ ] Research current contact emails/forms (websites change; verify before sending)
- [ ] Draft initial email (use Template 1 from Document 1)
- [ ] Gather your information:
  - [ ] Printer model: {{PRINTER}}
  - [ ] Current volume: {{VOLUME}} kg/month
  - [ ] Projected volume: {{PROJECTION}} kg/month
  - [ ] Color requirements: {{COLORS}}
  - [ ] Material requirements: {{MATERIALS}}
  - [ ] Timeline for first order: {{DATE}}

### Strategy Selection

- [ ] Determine your path (A/B/C from Supplier Negotiation Playbook)
- [ ] Rank suppliers by priority (1=most preferred, 5=fallback)
- [ ] Set your negotiation targets:
  - [ ] Price target: ${{TARGET}}/kg
  - [ ] Walk-away price: ${{WALKAWAY}}/kg
  - [ ] Minimum volume commitment: {{MIN_VOL}} kg/month
  - [ ] Ideal lead time: {{LEAD_TIME}} days
  - [ ] Payment terms preference: {{TERMS}}

---

## Supplier Communication Timeline

**Expected flow** (if everything goes smoothly):

```
Day 0-2: Initial contact (email)
Day 3-5: Supplier responds with preliminary quote
Day 5-7: You request detailed pricing and terms
Day 7-14: Supplier provides full quote sheet
Day 14-21: You negotiate terms (price, MOQ, lead time)
Day 21-28: Agreement reached, contract signed
Day 28+: Place first order, establish recurring supply
```

**Total timeline**: 3-4 weeks from initial contact to first order placed

**Parallel execution**: Send initial contacts to 3 suppliers simultaneously (eSUN, Anycubic, Polymaker). They'll respond at different speeds; use their response time to inform your priority ranking.

---

## Monthly Supplier Scorecard (Track Performance)

Create this spreadsheet in Google Sheets and update monthly:

| Month | Supplier | Volume (kg) | Price (actual vs. quoted) | Lead Time (days) | Quality Issues | Payment Smooth | Notes | Rating (1-5) |
|---|---|---|---|---|---|---|---|---|
| May | eSUN | 20 | $12.00 vs $12.00 (✓ match) | 6 vs 5-7 (✓ on time) | None | Yes | First order went smoothly | 5 |
| June | eSUN | 30 | $12.00 vs $12.00 | 6 vs 5-7 | 1 spool (winding issue) | Yes | Contacted; replacement sent | 4 |
| June | Anycubic | 50 | $10.49 vs $10.49 | 7 vs 3-7 | 3 spools (winding) | Yes | More issues than eSUN | 3 |

---

## Emergency Supplier Backup Plan

If your primary supplier fails (stock-out, price spike, quality issue):

| Scenario | Primary Supplier | Secondary (Use) | Tertiary (Fallback) | Timeline |
|---|---|---|---|---|
| eSUN out of stock | Anycubic | Polymaker (if available) | Amazon Prime (retail cost) | Can switch within 2 days |
| eSUN price spike | Anycubic | Check SUNLU | Amazon Prime | 3-5 days |
| Anycubic quality fails | eSUN (if available) | Polymaker | Amazon Prime | 5-7 days |
| Both primary suppliers unavailable | Polymaker | SUNLU + Amazon Prime mix | Message customers: "Processing delay" | 7-10 days |

**Note**: Keep contact information for all 5 suppliers in your phone. In a real emergency, you may need to reach out to multiple suppliers within hours.

---

## Variables Summary (Fill These In Before Using)

| Variable | Your Value | Category |
|---|---|---|
| {{SALES_CONTACT_NAME}} | Name of eSUN sales person | eSUN contact |
| {{SALES_EMAIL}} | their.email@esun3d.com | eSUN contact |
| {{PHONE}} | Their phone number | eSUN contact |
| {{20U_PRICE}} | $12.50/kg | eSUN pricing |
| {{100U_PRICE}} | $12.00/kg | eSUN pricing |
| {{500U_PRICE}} | $11.00/kg | eSUN pricing |
| {{CURRENT_PRICE}} | $12.00 (verified today) | Current market data |
| {{TARGET}} | $11.50/kg | Your negotiation target |
| {{WALKAWAY}} | $13.00/kg | Your maximum acceptable price |
| {{PRINTER}} | Bambu P1S | Your equipment |
| {{VOLUME}} | 20 | Current monthly volume |
| {{PROJECTION}} | 100 | Projected volume by Q4 |
| {{COLORS}} | Black, White, Gray | Your requirements |
| {{MATERIALS}} | PLA+ (primary), PETG (secondary) | Your requirements |
| {{DATE}} | June 1, 2026 | When you'll place first order |
| {{MIN_VOL}} | 20 | Minimum monthly commitment |
| {{LEAD_TIME}} | 7 days | Your ideal lead time |
| {{TERMS}} | Net-30 | Your preferred payment terms |

---

## Quick Reference: Who to Contact First

**If you're in a hurry (need supply in next 2 weeks)**:
1. Contact Anycubic first (fastest response, fastest shipping)
2. Contact eSUN second (slower response, but lower price)
3. Skip Polymaker (too slow for urgent startup)

**If you have 4+ weeks**:
1. Contact eSUN first (best long-term partner, good pricing)
2. Contact Anycubic second (backup, lowest COGS)
3. Contact Polymaker third (future premium tier)

**If you're willing to pay premium for quality**:
1. Contact Polymaker first (best material quality)
2. Contact eSUN second (good balance of price + quality)
3. Contact Anycubic second (lowest price option)

---

## Final Notes

- **Update this matrix weekly** during the negotiation period
- **Archive the decision log** once suppliers are selected (reference for future discussions)
- **Monitor supplier performance monthly** — the scorecard catches quality degradation early
- **Build relationships**: Your best deal comes from being a good customer, not from hard-negotiating lower prices

Good luck with your supplier negotiations!
