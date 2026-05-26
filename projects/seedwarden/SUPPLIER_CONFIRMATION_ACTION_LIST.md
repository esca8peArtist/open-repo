---
title: "Supplier Confirmation Action List — Phase 3 Medicinal Herbs"
date: 2026-05-26
version: "2.0 — Session 1655 update"
status: user-action-required
phase: Phase 3 pre-production
purpose: >
  Five concrete email/order/confirmation actions required from the user before June 22 sprint start.
  Each action is self-contained — no research required, just execution. Ordered by deadline.
  v2.0 reflects May 26 critical update: Strictly Medicinal Seeds pauses live plant shipping in summer,
  changing the Tier 3 live plant sourcing strategy.
decision-window: May 27 – June 22, 2026
cross-references:
  - PHASE_3_SUPPLIER_CONFIRMATION_TRACKER.csv (v2.0 — full supplier detail, May 26 update)
  - PHASE_3_PRODUCTION_TIMELINE_SKELETON.csv (Gantt — deadline context)
  - PHASE_3_PRODUCTION_TIMELINE_DETAILED.csv (full sprint schedule)
tags: [seedwarden, phase-3, suppliers, user-action, email-templates]
---

# Supplier Confirmation Action List
## Phase 3 — Five Actions Before June 22

**Version**: 2.0 (Session 1655, May 26, 2026)
**Key change from v1.0**: Action 3 revised — Strictly Medicinal Seeds confirmed to pause live plant shipping in summer (mid-June through August). Tier 3 live plant strategy updated accordingly.

**Purpose**: These are the only supplier actions the user needs to take before the sprint starts. No research needed — the contacts, pricing, and decision logic are all pre-resolved. Send the emails, place the orders, log the confirmations.

**Total user time**: approximately 55 minutes across 27 days. All research and decision logic is pre-resolved.

---

## Action 1 — Email Strictly Medicinal Seeds by May 27
**Deadline**: May 27 (tomorrow if reading on May 26)
**Float**: 0 days — this directly gates Action 3 (live plant sourcing strategy for Echinacea, Passionflower, Valerian)
**Contact**: info@strictlymedicinalseeds.com
**Subject**: June shipping inquiry — Echinacea, Passionflower, Valerian transplants + potted Goldenseal

**Email body** (copy-paste ready):

> Hello,
>
> I'm planning a late-June order for medicinal herb photography specimens and had two questions about your summer shipping schedule:
>
> 1. I understand you typically pause live plant and root shipping during summer heat. Will you be shipping live transplants in late June 2026 (approximately June 22-28)? Specifically, I'm looking for: Echinacea purpurea transplant, Passiflora incarnata (passionflower) transplant, and Valeriana officinalis transplant — 1-2 plants of each.
>
> 2. Do you currently have potted Goldenseal (*Hydrastis canadensis*) in stock for shipping? Your website indicates potted plants ship mid-March through July, but I want to confirm before ordering.
>
> I would place the order immediately upon your confirmation that you're shipping in late June.
>
> Thank you,
> [Your name]
> Seedwarden

**What to do with the response**:
- If SM confirms late-June shipping is available for these three species: log in WORKLOG.md and plan June 22 Tier 3 orders as originally scheduled.
- If SM confirms summer shutdown applies through late June: activate Prairie Moon Nursery as backup (Action 3 Option A). Log the shutdown dates in WORKLOG.md.
- If SM confirms potted Goldenseal in stock: order immediately and log tracking in WORKLOG.md. If out of stock: Wikimedia CC Path 2 is the confirmed path (see Action 5).

---

## Action 2 — Order Black Cohosh by May 30
**Deadline**: May 30 (hard — aligns with Phase 2 launch day and Phase 3 decision gate)
**Float**: The June 8 absolute deadline still applies; May 30 gives 3-4 extra weeks of plant establishment before sprint photography
**Supplier**: NativeWildflowers.net — nativewildflowers.net — confirmed in stock as of May 22
**Item**: Black Cohosh (*Actaea racemosa*) bareroot — $5.99/plant
**Order**: 1-2 plants via website checkout
**Expected delivery**: 3-5 business days from order (June 2-6 if ordered May 30)
**On arrival**: Pot immediately in a shade-soil mix (loamy, moist, slightly acidic); place in dappled shade; water regularly. New growth emerges within 2-3 weeks.
**Log in WORKLOG.md**: "Black Cohosh ordered NativeWildflowers.net $[amount], tracking [#], expected delivery [date]."

**Note**: If the SM email (Action 1) confirms SM potted Black Cohosh in stock before May 30, order from SM instead and skip NativeWildflowers.net for this species. Either path delivers the same result.

---

## Action 3 — Confirm Live Plant Sourcing Strategy by June 1
**Deadline**: June 1
**Float**: 3 weeks to June 22 sprint start — but confirming early locks the photo strategy for Echinacea, Passionflower, and Valerian

**Context (v2.0 update)**: Strictly Medicinal Seeds has been identified as a supplier that pauses live plant shipping during summer (typically mid-June through August). This removes SM as an assumed Tier 3 plant source for June 22 orders UNLESS Action 1 email confirms otherwise.

**Herbs needing a confirmed live-plant path for Tier 3 (live specimens)**:
- Echinacea purpurea / angustifolia
- Passiflora incarnata (passionflower)
- Valeriana officinalis (valerian)
- Sambucus canadensis / nigra (elderberry)

**Four-step decision tree (execute June 1)**:

**Step 1 — Check SM response (from Action 1)**:
Did SM confirm late-June plant shipping? If YES — proceed with SM as Tier 3 supplier for Echinacea, Passionflower, and Valerian. Place orders on June 22 as originally planned. If NO or no response — continue to Step 2.

**Step 2 — Check Prairie Moon Nursery website (June 1)**:
Go to prairiemoon.com and search each species: Sambucus canadensis, Echinacea purpurea, Passiflora incarnata, Valeriana officinalis.
- If "In Stock" shows for summer shipping: add to cart and order Elderberry and any available Tier 3 plants immediately. Call 866-417-8156 if website status is ambiguous.
- If Elderberry is in stock: order 1-2 plants; expected June 15-22 delivery for a June 1 order.
- Log the result for each species in WORKLOG.md.

**Step 3 — Local nursery for Elderberry, Lavender, Lemon Balm (regardless of Steps 1-2)**:
Call your nearest garden center or farm store. Ask for: "2-gallon potted elderberry shrub — Sambucus nigra or canadensis." Price range $15-35/plant. Buy 1-2 plants between June 1-15. Also buy: 1 potted Lavender start and 1 potted Lemon Balm start (universally available at any garden center through July; $5-15/plant each).

**Step 4 — Wikimedia CC-BY-SA confirmation for remaining Tier 3 herbs**:
If SM and Prairie Moon cannot supply live Echinacea, Passionflower, or Valerian transplants by June 22:
- Confirm in WORKLOG.md that Wikimedia CC-BY-SA path is active for these species. All three have confirmed launch-quality images:
  - Echinacea purpurea: abundant purple coneflower photos on Wikimedia — among the most-photographed garden herbs in North America.
  - Passiflora incarnata: several confirmed CC-BY-SA full-flower images; radial structure is visually superior to most live-plant photos.
  - Valeriana officinalis: good Wikimedia coverage of flowering stalk.
- Log: "Tier 3 live specimens not sourced for [species list] — Wikimedia CC-BY-SA path confirmed. Photo attribution logged in PHOTO_ATTRIBUTION_LOG.md."
- This is not a degraded outcome. The Wikimedia path was the planned launch path for these species even before the SM summer-shutdown finding.

**Log in WORKLOG.md**: "Action 3 complete June 1. Elderberry: [source, in-person / Prairie Moon / other]. Lavender: [local nursery, purchase date TBD June 1-15]. Lemon Balm: [local nursery]. Echinacea live specimen: [SM confirmed / PM ordered / Wikimedia path]. Passionflower live specimen: [SM confirmed / PM ordered / Wikimedia path]. Valerian live specimen: [SM confirmed / PM ordered / Wikimedia path]."

---

## Action 4 — Place Mountain Rose Herbs Dried Herb Order by June 13 (hard)
**Deadline**: June 13 (recommended), June 15 (absolute hard deadline)
**Float**: June 15 is the absolute hard deadline; June 13 adds a 2-day buffer for shipping confirmation and delivery tracking
**Contact**: mountainroseherbs.com — retail order via website
**Order**: 1 oz each of the following 11 species (Goldenseal root and Black Cohosh root are both OUT OF STOCK at MRH — do not include):

1. Elderberry (dried whole berry)
2. Echinacea purpurea root
3. Echinacea angustifolia root
4. Valerian root
5. Passionflower herb (aerial parts)
6. Lemon Balm leaf
7. Lavender flower
8. Calendula flower
9. Dandelion root
10. Ashwagandha root
11. Mullein leaf

**Estimated total**: $73-107 retail (1 oz per species)
**Use**: Studio photography props for the dried herb flat-lay images; also reference material for writing preparation sections. These are the dried-herb specimens for the June 17-21 studio shoot — the launch-quality photos for all five bundles.

**Before ordering**: Verify each sku is in stock on the MRH website. The May 22 stockout affected only Goldenseal root and Black Cohosh root. All 11 sprint skus are assumed in stock but individual sku availability has not been phone-confirmed — a brief check of the product pages before checkout catches any additional stockouts.

**For Goldenseal root and Black Cohosh root dried specimens** (optional photography props — not blocking sprint launch):
- Check local Whole Foods, Fresh Market, or independent co-op/herb store. These retailers often stock Mountain Rose Herbs products locally even when MRH online shows out of stock.
- Alternative: skip dried root props for these two species and use Wikimedia Commons root cross-section images (confirmed sufficient quality for sprint launch; dried root props upgrade to v1.1 in September).

**If MRH has not shipped by June 15**: Place Frontier Co-op (frontiercoop.com) order same day for the 11 species. Frontier ships in 3-5 days. Do not wait past June 15 for MRH.

**Log in WORKLOG.md**: "MRH order placed [DATE]; order confirmation [#]; tracking [#]; estimated delivery [DATE]. All 11 skus confirmed in stock at time of order: [YES/NO — note any stockouts]."

---

## Action 5 — Confirm Goldenseal Path in WORKLOG.md by June 8
**Deadline**: June 8 (ZERO FLOAT — hard deadline)
**This is not an order — it is a 5-minute documentation action, but it cannot be skipped**

Mark one path in WORKLOG.md before June 8:

**Path 2 (recommended — pre-selected, no order needed)**:
> Goldenseal Path 2 confirmed [DATE]. Wikimedia CC-BY-SA images downloaded: [filenames]. Logged in PHOTO_ATTRIBUTION_LOG.md: YES. NC Botanical Garden email sent [date] (optional for high-res upgrade). Missouri Botanical Garden email sent [date] (optional). Cost: $0. Schedule risk: zero.

**Path 1 (only if you want a live specimen for photography)**:
Order at nativewildflowers.net — $4.99, ships now. Log tracking number and expected delivery in WORKLOG.md.
> Goldenseal Path 1 confirmed [DATE]. NativeWildflowers.net order placed $[amount], tracking [#], expected delivery [date]. Cultivated source confirmed: YES (NativeWildflowers.net product page states nursery-propagated).

**Why this matters**: Goldenseal has a 5-6 week lead time through primary suppliers (Prairie Moon and Mountain Rose Herbs both confirmed out of stock for summer 2026). If no confirmation exists by June 8, the Immunity bundle has no resolved photo strategy at sprint start. The confirmation takes 5 minutes; the consequence of skipping it is a full Immunity bundle photo redesign during the sprint.

---

## Summary Table

| # | Action | Deadline | Float | Effort | Supplier/Contact |
|---|---|---|---|---|---|
| 1 | Email SM Seeds — confirm June shipping for live plants + Goldenseal stock | May 27 | 0 days | 5 min (copy-paste email above) | info@strictlymedicinalseeds.com |
| 2 | Order Black Cohosh bareroot | May 30 | 10 days to June 8 | 10 min (website order) | nativewildflowers.net |
| 3 | Confirm live plant sourcing strategy — SM response, Prairie Moon check, local nursery, Wikimedia fallback | June 1 | 3 weeks | 20 min (website check + calls) | prairiemoon.com / local nursery / WORKLOG.md |
| 4 | Place MRH dried herb order (11 species) | June 13 (rec.) / June 15 (hard) | 2 days | 20 min (website order) | mountainroseherbs.com |
| 5 | Log Goldenseal path in WORKLOG.md | June 8 | 0 days | 5 min (documentation only) | WORKLOG.md |

**Total user time**: approximately 60 minutes across 27 days.

---

## v2.0 Change Log (May 26, Session 1655)

- **Action 3 fully revised**: Original v1.0 Action 3 assumed Strictly Medicinal Seeds was a viable live-plant source for June 22 Tier 3 orders. Confirmed May 26: SM pauses live plant and root shipping during summer heat (typically mid-June through August). SM is now a conditional source — viable only if Action 1 email confirms they are shipping in late June 2026.
- **Action 3 Prairie Moon added**: Prairie Moon spring potted plant season runs April-June; mid-summer window is narrow. Added as explicit June 1 check step with call option (866-417-8156).
- **Action 3 Wikimedia CC fallback formalized**: Echinacea, Passionflower, and Valerian all have confirmed launch-quality Wikimedia CC-BY-SA images. The Wikimedia path is not a degraded outcome — it was the planned launch path. Formalizing it as the Action 3 Step 4 fallback removes ambiguity.
- **Action 4 order deadline tightened**: Recommendation moved from June 15 to June 13 to add 2-day delivery buffer for the June 17-21 studio session.
- **Action 1 email revised**: Subject line and body updated to ask about summer shipping schedule in addition to Goldenseal stock.
