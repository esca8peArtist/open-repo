---
title: Post-Test-Print Launch Readiness Research — May 2026 Market Validation
project: mfg-farm
created: 2026-05-18
status: FINAL — go/no-go assessment with specific update actions
scope: Etsy UI validation, supplier pricing verification, cost model assumptions, launch readiness
---

# Post-Test-Print Launch Readiness Research — May 2026

**Assessment Date**: 2026-05-18
**Deliverables Under Review**:
1. `etsy-listing-launch-checklist.md` (648 lines)
2. `supplier-negotiation-playbook.md` (551 lines)
3. `8-printer-farm-cost-model.md` (639 lines)

**Bottom Line Up Front**: All three deliverables are fundamentally sound and are go-for-execution with targeted numerical updates. No structural rewrites are needed. Six specific data points have drifted from assumptions and require in-place corrections before the documents are handed to someone executing on day one.

---

## SCOPE CLARIFICATION — Botanical Vendor Brief Error

The research brief mentioned Mountain Rose Herbs, Prairie Moon Nursery, Strictly Medicinal Seeds, and Baker Creek as suppliers in the scorecard. These are botanical seed vendors with no connection to this project. The actual `supplier-scorecard.csv` contains only filament and fulfillment vendors: eSUN, Anycubic, Polymaker, Overture, SUNLU, Pirate Ship, Shop4Mailers, Packlane, EcoEnclose, Simpl Fulfillment, ShipMonk, and Amazon FBA. The botanical vendor list was likely cross-contamination from a separate project in the research brief. No action needed on those vendors — they are not part of this project.

---

## SECTION 1: ETSY SHOP SETUP VALIDATION

### Current Etsy UI State (May 2026)

Prior validation (`Etsy_Setup_May2026_Validation.md`, dated 2026-05-17) already identified three material changes. This research deepens those findings and adds two new items.

**Onboarding — New $15 Setup Fee (CRITICAL)**

As of September 2024 (still in force May 2026), Etsy charges new sellers a one-time nonrefundable setup fee of $15–29 before a shop can open. The checklist contains no mention of this. A first-time seller who reaches the payment step without expecting it will experience a friction point on launch day.

- **Checklist gap**: Section 1.2 (Shop Standards and Billing Checklist), line 72 — "Confirm Etsy Shop Membership: Active (paid)" — does not mention the setup fee.
- **Confidence level**: High. Confirmed by Etsy's own seller handbook, eRank, and multiple 2026 seller guides.

**Identity Verification — Persona Partnership (NEW)**

Etsy now requires photo ID upload plus a selfie for all new shops via a Persona integration. This step occurs during onboarding, before the shop is live. It is not mentioned anywhere in the checklist.

- **Checklist gap**: Section 1.2 has no identity verification step.
- **Impact**: A seller who doesn't have their ID on hand on launch day loses 20–40 minutes to this step. Low severity but notable.
- **Confidence level**: High. Confirmed by Etsy Seller Handbook article on new-shop onboarding.

**Fee Rate — Effective Rate Is 11–11.5%, Not 9.5% (MATERIAL)**

The checklist states 9.5% throughout pricing formulas (Section 5.1, lines 336–346). The correct breakdown is:
- Transaction fee: 6.5% of total (including shipping)
- Payment processing: 3% + $0.25 per transaction
- At a $14.99 single clip sale with $4.50 shipping: effective rate is approximately 10.8–11.2%

The prior validation recommended 10.5% as a planning baseline. Rounding to 11% is the most conservative and accurate for small-ticket items where the $0.25 fixed component has outsized impact.

- **Checklist gap**: Section 5.1 pricing formula; Section 5.2 margin calculation table.
- **Dollar impact**: On a $14.99 clip, the difference is $0.22/unit ($1.58 vs. $1.36 in fees). At 200 units/month, $44/month understatement.
- **Confidence level**: High. Confirmed by Etsy's official Fees and Payments Policy (Feb 13, 2026 update) and Voolist 2026 breakdown.

**Return Policy UI — Listing-Level, Not Shop-Level (LOW PRIORITY)**

Return policies are now set per-listing (or bulk-applied) rather than through a single shop-wide settings page. The checklist (Section 1.1, lines 42–45) describes the old shop-level flow. The strategic guidance (30-day returns, buyer pays return shipping) remains valid. Only the navigation path changes.

- **Confidence level**: High.

**AI Disclosure Requirement — January 2026 (NEW)**

Etsy's January 14, 2026 Seller Policy update requires disclosure if generative AI tools are used in product design. For an original ModRun design created in CAD (CadQuery), this is not applicable. No listing change needed. However, if any AI-generated photography backgrounds or marketing copy was used, disclosure may be required.

- **Confidence level**: High. Policy confirmed via CedCommerce 2026 policy roundup.

**Materials Tag Field — Removed (CONFIRMED)**

The legacy text-based "Materials" tag field has been removed from Etsy listing forms. Only the structured Attributes panel remains. The checklist Section 3.3 references "Material" as an attribute (not a tag), so this is already correct. No change needed beyond confirming sellers don't look for a free-text materials field.

- **Confidence level**: High.

**Share and Save Program — New Upside**

A new "Share and Save" program offers a 4% fee reduction on sales driven via unique seller-generated links. This program has no downside — it is worth activating at launch. The checklist does not mention it.

- **Checklist addition**: Section 8 (Shop Marketing) is the appropriate location for a 1-line note.
- **Confidence level**: Medium. Program details confirmed by Etsy policy coverage; exact mechanics not fully documented in public sources.

### Confidence Summary — Etsy Checklist

| Section | Issue | Confidence | Priority |
|---|---|---|---|
| Section 1.2 — Billing | Missing $15 setup fee | High | High — add before launch day |
| Section 1.2 — Identity | Missing Persona verification step | High | Medium — minor friction risk |
| Section 5.1 — Pricing | Fee rate 9.5% → 11% | High | High — affects all margin math |
| Section 5.2 — Tiers | Margin recalculation needed | High | High — tied to fee rate fix |
| Section 1.1 — Returns | Navigation path updated (shop → per-listing) | High | Low — same outcome, different path |
| Section 8 — Marketing | Share and Save program missing | Medium | Low — optional upside |

**Overall Etsy Checklist Verdict**: LAUNCH-READY with three targeted line edits (setup fee, identity verification step, fee rate correction). Structural integrity of all SEO strategy, photography specs, launch timing, and monitoring protocol is confirmed valid for 2026.

---

## SECTION 2: SUPPLIER SCORECARD VERIFICATION

### Filament Suppliers — Current Pricing (May 2026)

Prior validation (`Supplier_Scorecard_May2026_Update.md`, dated 2026-05-17) identified the most critical issue: the scorecard confuses PLA Basic pricing with PLA+ pricing. This research confirms and extends those findings.

**eSUN PLA+ (ASIN B0G2KWC5XL) — PRICING DRIFT, HIGH IMPACT**

The playbook scorecard (line 53) states "$11–13/kg" for eSUN 10kg bundles. The current market reality:
- eSUN 10kg PLA+ bundle (B0G2KWC5XL): approximately $13.50–14/kg at standard Amazon pricing
- eSUN 10kg PLA Basic bundle (B0G2KSS613): approximately $9.50/kg — this is the source of the $11/kg assumption

The scorecard's Step 1 action (lines 87–90) correctly directs the reader to check ASIN B0G2KSS613 for "PLA Basic" and B0G2KWC5XL for "PLA+", but the decision gate on line 111 uses $13/kg as the threshold for viability — which is now at the floor of current PLA+ pricing, not comfortably above it.

- **Impact on playbook**: The decision gate at line 111 ("If eSUN Amazon is currently ≤$13/kg AND Anycubic 50kg is ≤$11/kg, proceed as written") is now on the margin of triggering. Real-world execution may land at $13.50/kg, which is above the gate threshold.
- **Recommended fix**: Update the decision gate to ≤$14.50/kg for PLA+ (reflecting the PLA+ premium over Basic). If PLA Basic quality is acceptable for the product, the $9.50/kg Basic pricing dramatically changes the math.
- **Confidence level**: High. Multiple 2026 filament price trackers (LayerMath, SpoolPrices, eSUN ASINs cross-referenced) confirm the $13–15/kg range for PLA+ in retail quantities.

**Anycubic 50kg Pallet — Price Verification Needed**

The playbook targets $10.49/kg (line 95). The prior validation flagged this as a sale price that may not be permanent. Current search results did not return a confirmed live Anycubic pallet price as of May 2026. The playbook's Step 1 action correctly directs the reader to check store.anycubic.com directly — this instruction remains valid and is the correct execution step.

- **Risk**: If the $10.49/kg sale has ended, the secondary supplier economics shift. The playbook's walk-away threshold of $11/kg (line 327) is the correct backstop.
- **Confidence level**: Medium. Price requires real-time verification on execution day.

**Polymaker Wholesale — Phase 3 Pricing Requires Update**

The scorecard lists $10.49/kg for Polymaker (line 54), which was likely a data error (Anycubic's pallet price was mistakenly attributed to Polymaker). Current Polymaker wholesale pricing is $17.99/kg (28% off MSRP of $24.99). This is a Phase 3 concern only, but the scorecard table has an incorrect number.

- **Impact**: Phase 3 filament cost projections in the cost model are approximately 70% underestimated for Polymaker. At Phase 3 volumes (100+ kg/month), this is a material planning error.
- **Confidence level**: High. Prior validation confirmed $17.99/kg.

**MatterHackers — Within Range**

MatterHackers is referenced in the cost model (Section 2.1, lines 107–112) but not in the supplier-negotiation-playbook.md's core scorecard. Current pricing ($22.99/kg retail, ~$19.31/kg bulk) aligns with cost model assumptions of $19–21/kg. No change needed for Phase 1–2 planning.

**Other Vendors — Confirmed Operational**

- Pirate Ship: Operating normally; commercial rates active; 8% USPS surcharge confirmed in effect through January 17, 2027.
- Shop4Mailers: Standard poly mailers at $0.05/unit confirmed available.
- Simpl Fulfillment, ShipMonk: Both operational. No service level changes reported.

### Supplier Scorecard Confidence Summary

| Vendor | Scorecard Assumption | Current Reality | Action | Priority |
|---|---|---|---|---|
| eSUN PLA+ | $11–13/kg | $13–14/kg | Update decision gate to ≤$14.50/kg | High |
| eSUN PLA Basic | (referenced as comparison) | ~$9.50/kg | Clarify Basic vs. Plus distinction in Step 1 | High |
| Anycubic 50kg | $10.49/kg | Unverified — may be higher | Verify on execution day per existing Step 1 action | Medium |
| Polymaker | $10.49/kg | $17.99/kg | Update Phase 3 cost projections | Medium |
| MatterHackers | $19–21/kg | $19.31–22.99/kg | No change | Low |
| Pirate Ship | $3.50–6.00/label | Current; 8% surcharge confirmed | No change | None |

**Overall Playbook Verdict**: LAUNCH-READY for Phase 1. The playbook's most important instruction — verify current prices before committing to any path — is correct and already present in Step 1. The decision gate threshold for PLA+ needs updating ($13/kg → $14.50/kg), but the framework is sound.

---

## SECTION 3: COST MODEL ASSUMPTIONS VERIFICATION

Prior validation (`Cost_Model_May2026_Validation.md`, dated 2026-05-17) identified three revision areas. This research confirms all three and adds new context on equipment costs and the print farm landscape.

### Filament Cost — Phase 1 Baseline Requires Correction

The cost model uses $12/kg as the Phase 1 filament baseline (Section 2.1, line 89). This is now confirmed to be too low for PLA+ at retail quantities.

- **Corrected Phase 1 baseline**: $13.50/kg (PLA+, eSUN 10kg bundle via Amazon Prime)
- **Per-unit impact**: +$0.12/unit at 75g/clip (from $0.90 to $1.02)
- **Table impact**: Section 2.1 material cost tables understate all tiers. Recalculate with $13.50/kg for Phases 1–2, $12/kg for Phase 3 wholesale, $10–11/kg for Phase 4.
- **Gross margin impact**: Section 3.2 gross margins drop approximately 0.5–1.0 percentage points across all volume tiers. Still healthy — no thesis change.
- **Confidence level**: High.

### USPS Shipping Costs — Confirmed Elevated

The cost model assumes $4.50/order average across all shipments (Section 2.5 and revenue tables). USPS raised Ground Advantage commercial rates twice in 2026:
- January 18, 2026: 9.6% average commercial rate increase (small packages under 1 lb saw 12.2% increase)
- April 26, 2026: 8% temporary surcharge, in effect through January 17, 2027

Combined impact for sub-1-lb shipments (cable clip + packaging): approximately 21% year-over-year increase from December 2025 baseline. Pirate Ship commercial rates remain below retail USPS but are subject to the same increases.

Revised rate estimates for ModRun products via Pirate Ship:
- Single clip (~2 oz + packaging, ~3.5 oz total): $4.10–4.55 (after surcharge)
- 3-pack bundle (~8–10 oz): $5.00–5.50 (after surcharge)

The $4.50 flat rate assumption is within the revised single-clip range but is too low for 3-pack bundles. The revenue tables in Section 3.1 assume a blended $4.50 regardless of SKU mix, which understates shipping costs for bundle-heavy orders.

- **Recommended fix**: Use $4.75 for single-clip average, $5.25 for 3-pack average in revenue table calculations.
- **Gross margin impact**: Approximately $0.25–0.75/order increase depending on SKU mix. Still within healthy range.
- **Confidence level**: High. USPS rate hike percentages confirmed by GoWarpSpeed and atoship.

### Etsy Fee Rate — 9.5% → 11% (MATERIAL)

Same correction as identified in the Etsy checklist section. The cost model Section 3.1 revenue table applies 9.5% Etsy fees. The correct effective rate for ModRun pricing (items under $35 with $4–5 shipping) is 10.5–11%.

- **Dollar impact at 2,000 units/month ($55K revenue)**: Approximately $550/month fee understatement.
- **Gross margin impact**: 80.5% → 79.3% at 2,000 units/month. Still strong.
- **Confidence level**: High.

### Equipment Costs — FAVORABLE UPDATE

The cost model uses $699 as the Bambu P1S unit cost (Section 1.1, line 35). Current market pricing:
- P1S has dropped to $399–449 during frequent 2026 promotions (confirmed record low of $399 in early 2026)
- Street pricing regularly sits at $399–499; $699 is now the exception rather than the norm
- P1S Combo (with AMS) is approximately $749, down from original launch pricing

The ADP Industries 2026 farm review adds a strategic insight: three Bambu A1 Mini units ($299 each = $897 total) can outproduce a single P1S on throughput for many single-material use cases, at similar total cost. This is relevant if the farm strategy needs to optimize for throughput-per-dollar rather than enclosed printing capability.

- **Cost model update**: Keep $699 as the planning-conservative figure per prior validation recommendation, but note in assumptions that effective acquisition cost is $399–499 on promotion. This reduces total 8-printer farm capital cost by approximately $2,400–2,800 when purchasing during sales.
- **ROI impact**: Favorable — payback period shortens from 4–5 months to 3–4 months at promotional pricing.
- **Confidence level**: High for price range. Medium for promotion availability on specific purchase dates.

### Electricity Cost — CONFIRMED CONSERVATIVE BUT DEFENSIBLE

The cost model uses $0.12/kWh (Section 2.3). The US average commercial rate for small businesses is $0.12–0.14/kWh. For a home-based operation, residential rates of $0.10–0.16/kWh are typical depending on state. The $0.12/kWh figure is defensible as a national planning baseline.

- **Per-unit impact**: Electricity is approximately $0.04/unit at 2,000 units/month — genuinely negligible. Even at $0.20/kWh (high-cost states), the per-unit impact is $0.07. This assumption does not materially affect the model.
- **Confidence level**: High that the assumption is acceptable for planning purposes.

### Print Farm Landscape — No Major Competitive Threat Found

The broader 3D print farm landscape in 2026 shows significant growth but no disruptive entrants specifically targeting the cable management / desk accessory Etsy niche. Notable context:

- Bambu Lab released a free LAN Mode Print Farm Manager for fleet management (confirmed Q1 2026). This is relevant to the orchestration tooling section — SimplyPrint ($40/month) may be partially replaceable with Bambu's native free tool for basic fleet management at lower printer counts.
- Prusa's Automated Farm System (AFS) at $thousands is enterprise-grade and not relevant to Phase 1–3.
- The "2026 Year of the Low-Cost Print Farm" report confirms the economics are favorable for small operators targeting Etsy niches — no competitive threat from industrial entrants at this price point.
- **Implication for cost model**: SimplyPrint subscription in Section 2.4 ($40/month) should note Bambu's free LAN tool as an alternative that reduces software cost to $0–6/month (G Workspace email only) for Phases 1–3.

### Cost Model Confidence Summary

| Assumption | Model Value | Corrected Value | Impact | Priority |
|---|---|---|---|---|
| Filament (Phase 1) | $12/kg | $13.50/kg | +$0.12/unit; −0.5–1% gross margin | High |
| USPS single clip | $4.50 | $4.75 | +$0.25/order | Medium |
| USPS 3-pack | $4.50 | $5.25 | +$0.75/order | Medium |
| Etsy fees | 9.5% | 11% | −1.2% gross margin at scale | High |
| P1S unit cost | $699 | $399–499 (promo) | −$2,400–2,800 capex (favorable) | Medium |
| Electricity | $0.12/kWh | Confirmed | No change | None |
| SimplyPrint | $40/month required | Bambu LAN tool is free alternative | Optional savings $40/month Ph. 1–3 | Low |

**Overall Cost Model Verdict**: STRUCTURALLY SOUND. The investment thesis (3–5 month payback, 29–50x ROI over 24 months) survives all corrections. Adjusted gross margins are 78–80% (down from 80–82%) — still exceptional for a physical products business. Proceed with launch.

---

## SECTION 4: RECOMMENDED CHECKLIST UPDATES (Line-Number Referenced)

### etsy-listing-launch-checklist.md

**Update 1 — Line 72 (High Priority)**
Current: `- [ ] **Confirm Etsy Shop Membership**: Active (paid)`
Add before this line: `- [ ] **Etsy Setup Fee**: Pay one-time $15–29 nonrefundable fee (required before shop opens; charged during new-shop onboarding flow)`
Add below that: `- [ ] **Identity Verification**: Complete Persona photo ID + selfie verification (required during onboarding; have government-issued ID ready)`

**Update 2 — Lines 336–346, Section 5.1 (High Priority)**
Change all instances of `9.5%` in pricing formulas to `11%` for planning purposes.
Recalculate the margin formula example:
- Old: `Retail Price = $1.26 / (1 - 0.095 - 0.70) = $6.15`
- New: `Retail Price = $1.26 / (1 - 0.11 - 0.70) = $6.63`
- At $14.99 market price: gross margin = 1 - ($1.26/14.99) - 0.11 = **80.6%** (was stated as 82%)

**Update 3 — Lines 350–357, Section 5.2 (High Priority)**
Recalculate net margin for the 3-Pack Bundle example using 11% fees:
- Old net: "$17.34"
- Revised: `($24.99 - 1.26×3) - (24.99 × 0.11) - $5.25 shipping = $15.97 net`
- Still a strong margin; no pricing strategy change required.

**Update 4 — Lines 53–55 (Low Priority)**
Section 2.2 Photography note: `Do NOT use AI-generated backgrounds (Etsy's June 2025 policy flags these)` — this is confirmed valid for 2026. No change needed; policy still in force.

**Update 5 — Section 8 addition (Low Priority)**
Add to Section 8.1 or 8.2: `- [ ] **Activate Share and Save program** (Etsy Marketing tab): Earn 4% fee reduction on sales driven via your personal referral link. No downside. Activate at or before launch.`

### supplier-negotiation-playbook.md

**Update 1 — Line 111 (High Priority)**
Current decision gate: `If eSUN Amazon is currently ≤$13/kg AND Anycubic 50kg is ≤$11/kg, proceed with the playbook as written.`
Revise to: `If eSUN Amazon PLA+ is currently ≤$14.50/kg AND Anycubic 50kg is ≤$11.50/kg, proceed with the playbook as written. Note: eSUN PLA Basic (B0G2KSS613) typically prices ~$9.50/kg — verify you are comparing PLA+ (B0G2KWC5XL) to the target, not Basic.`

**Update 2 — Lines 52–54, Supplier Rankings Table (Medium Priority)**
- Row for eSUN: Change `$11-13/kg` to `$13–14/kg (PLA+); $9–10/kg (PLA Basic)`
- Row for Polymaker: Change `$14.99/kg` to `$17.99/kg (28% off MSRP)` — Phase 3 cost projections need separate update in cost model.

**Update 3 — Lines 403–410, Filament Cost by Volume Table (High Priority)**
Change the `0-10 kg (retail)` row from `$14-15/kg` to `$13.50–14.50/kg (PLA+)` to reflect current pricing. The table structure remains valid.

### 8-printer-farm-cost-model.md

**Update 1 — Lines 89, 107–112 (High Priority)**
Section 2.1: Change `$12/kg` Phase 1 baseline to `$13.50/kg`. Recalculate the material cost table rows accordingly. The $12/kg figure becomes the Phase 2 target (negotiated wholesale), not the retail starting point.

**Update 2 — Section 3.1 Revenue Tables (High Priority)**
Change `9.5%` Etsy fee assumption to `11%` in all revenue and gross profit calculations. Recompute net revenue and gross profit columns. Gross margins drop 1–2 percentage points but remain at 65–80% across volume tiers.

**Update 3 — Lines 156–160, Electricity/Power Table (None needed)**
$0.12/kWh confirmed. No change.

**Update 4 — Section 1.1 Equipment Cost Table (Medium Priority)**
Add footnote to P1S row: `Current street pricing $399–499 on frequent promotion; $699 retained as conservative planning assumption. Effective capex savings of $2,400–2,800 achievable with promotional timing.`

**Update 5 — Section 2.4 Software Subscriptions (Low Priority)**
Add note: `SimplyPrint alternative: Bambu Lab released free LAN Mode Print Farm Manager (2026) for fleet management without cloud dependency. Reduces Phase 1–3 software cost to $0 for Bambu-only farms.`

---

## SECTION 5: GO/NO-GO ASSESSMENT

### Are the Three Deliverables Ready to Deploy?

**Etsy Listing Launch Checklist** — GO with edits
The checklist is operational as written. Two high-priority additions (setup fee warning, identity verification step) should be made before execution to prevent day-1 friction. The fee rate correction (9.5% → 11%) affects pricing math but does not change the pricing strategy — suggested retail prices remain $11.99 and $24.99 with strong margins at corrected rates. Five targeted line edits required; no structural rewrite.

**Supplier Negotiation Playbook** — GO with edits
The playbook's self-verification structure (Step 1 directs seller to check live prices before committing) means it is partially self-correcting for price drift. The PLA+ vs. PLA Basic confusion in the decision gate threshold is the only material risk: if a seller reads $13/kg and sees $13.50/kg, they may incorrectly abort to a more expensive fallback. Two table corrections and one decision gate threshold update required. No structural rewrite.

**8-Printer Farm Cost Model** — GO with edits
The investment thesis survives all corrections. The 24-month ROI of 29–50x on $10K capital investment holds at corrected inputs. The payback period of 4–5 months extends to 5–6 months at corrected filament and fee inputs — still well within acceptable range. Three numerical updates required (filament baseline, Etsy fee rate, shipping costs); no structural rewrite.

### Day-1 Blockers — Confirmed None

No launch-blocking issues were found in research. The following items must be resolved before execution:
1. Etsy setup fee warning added to checklist (prevent unexpected $15 charge)
2. Fee rate corrected from 9.5% to 11% in checklist and cost model (pricing math consistency)
3. PLA+ baseline cost corrected to $13.50/kg in playbook and cost model (accurate COGS planning)

Items 2 and 3 do not change the launch strategy, pricing tier recommendations, or supplier selection logic. They are numerical corrections to planning math, not strategic reversals.

---

## SOURCES

- [Etsy Policy Changes 2026 — CedCommerce](https://cedcommerce.com/blog/etsy-policy-changes-2026-what-shopify-etsy-sellers-must-fix-to-stay-compliant-visible-and-profitable/)
- [Etsy Shop Setup Step-by-Step Guide 2026 — Printify](https://printify.com/blog/how-to-start-an-etsy-shop/)
- [Etsy New-Shop Onboarding Announcement — Etsy Seller Handbook](https://www.etsy.com/seller-handbook/article/1241780194948)
- [Etsy Setup Fee Explained — eRank Help](https://help.erank.com/blog/understanding-etsys-new-15-setup-fee/)
- [Etsy Fees 2026 Complete Breakdown — Voolist](https://www.voolist.com/blog/etsy-fees-explained-2026)
- [Etsy Fees 2026 — CraftyBase](https://craftybase.com/blog/the-complete-guide-to-etsy-fees)
- [Etsy Policy Updates 2026 — Marmalead](https://blog.marmalead.com/etsy-policy-updates/)
- [Etsy Shipping Profiles Guide 2026 — LitCommerce](https://litcommerce.com/blog/how-to-set-up-etsy-shipping-profile/)
- [Filament Prices 2026 — LayerMath](https://layermath.com/filament-prices)
- [SpoolPrices Filament Price Comparison 2026](https://spoolprices.com/)
- [3D Print Filament Cost Guide 2026 — LatestCost](https://latestcost.com/3d-print-filament-cost/)
- [eSUN 10KG PLA+ Bundle ASIN B0G2KWC5XL — Amazon](https://www.amazon.com/eSUN-Pro-Grade-Toughness-Clog-Free-Dimensional/dp/B0G2KWC5XL)
- [USPS 2026 Rate Hikes — GoWarpSpeed](https://gowarpspeed.com/blog/usps-2026-rate-hikes)
- [USPS Ground Advantage Rates 2026 — I'd Ship That](https://idshipthat.app/shipping-rates/usps-ground-advantage/)
- [2026 Shipping Rate Guide — ThriftFlipping](https://thriftflipping.com/blog/article-129-shipping-rate-guide-resellers-2026.html)
- [Bambu Lab Printer Prices 2026 — OriginalPricing](https://originalpricing.com/bambu-lab-printer-prices/)
- [Bambu P1S Record Low $399 — Tom's Hardware](https://www.tomshardware.com/3d-printing/grab-this-usd399-bambu-lab-p1s-3d-printer-back-down-to-a-record-low-price-for-the-new-year-save-usd300-on-high-speed-enclosed-printer-for-beginners-and-enthusiasts-alike)
- [Best 3D Printer 2026 — ADP Industries Farm Operator Review](https://www.adpindustries.com/blog/best-3d-printer-2026/)
- [Best Budget FDM Printers 2026 — 3DWithUs](https://3dwithus.com/best-cheap-budget-fdm-3d-printers)
- [2026 Year of the Low Cost Print Farm — 3DPrint.com](https://3dprint.com/322953/2026-the-year-of-the-low-cost-print-farm/)
- [Bambu Lab Free LAN Mode Print Farm Manager — Tom's Hardware](https://www.tomshardware.com/3d-printing/bambu-lab-introduces-free-software-to-manage-an-unlimited-number-of-3d-printers-simultaneously-cloud-free-lan-mode-print-farm-manager-program-simplifies-mass-3d-printing)
- [Strictly Medicinal Seeds Wholesale](https://wholesale.strictlymedicinalseeds.com/) — Not applicable to this project
