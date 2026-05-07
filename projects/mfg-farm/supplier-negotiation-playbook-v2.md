---
title: ModRun Supplier Negotiation Playbook v2 — Contract Manufacturer Negotiation
project: mfg-farm
created: 2026-05-07
status: ready-for-execution (post-test-print)
session: multi-supplier-research
confidence: high — based on published supplier negotiation frameworks (2025–2026), verified contract manufacturer pricing benchmarks, and ModRun supply chain context
related: supply-chain-diversification-strategy.md, supplier-comparison-matrix.csv, supplier-negotiation-playbook.md
note: This is v2 of the negotiation playbook. v1 (supplier-negotiation-playbook.md) covers filament supplier negotiation. This document covers contract manufacturer negotiation for the ModRun clip and rail as finished products.
---

# ModRun Supplier Negotiation Playbook v2 — Contract Manufacturers

**This playbook is distinct from v1.** Version 1 (`supplier-negotiation-playbook.md`) covers filament supplier negotiation (eSUN, Anycubic, Polymaker). This document covers negotiating with contract manufacturers who would produce the ModRun clip and rail as finished goods — used for overflow production, demand spikes, or scaling beyond single-printer capacity.

**Execute this playbook:** Post-test-print, in parallel with Etsy store setup. The 10-unit sample order from JLC3DP should be placed within 2 weeks of the test print confirming design viability.

---

## Context and Position

At ModRun's current scale (20 units/week target, $2,500/month gross), you are a small buyer with no volume leverage. This is an honest assessment. The correct negotiation posture is not to demand discounts — it is to:

1. Establish a professional, production-credible presence with Tier 2 suppliers
2. Validate quality and lead time with a low-risk sample order
3. Build a paper trail (quotes, confirmations) that creates leverage at Month 3+ volume

The negotiation payoff comes at Month 3–6 when volume creates real leverage. The work done now (accounts, sample orders, relationship emails) is what makes that leverage usable.

---

## Step 1: Account Setup and STL Preparation (Day 1–2, ~45 minutes total)

**Objective:** Have accounts and quote files ready at all three Tier 2 platforms before placing any orders.

### JLC3DP
1. Create account at jlc3dp.com (email + password; no business registration required)
2. Navigate to "3D Printing Quote" → FDM → PLA material
3. Upload `modrun_clip.stl` → set quantity to 100 → note quoted price → screenshot
4. Upload `modrun_rail.stl` → set quantity to 100 → note quoted price → screenshot
5. Repeat both at qty 50 and qty 200 for price elasticity mapping
6. Save all screenshots to `projects/mfg-farm/research/tier2-quotes/`

**Expected output:** 6 screenshots (2 files × 3 quantities). This is the price baseline for all future negotiations.

### Xometry
1. Create account at xometry.com
2. Navigate to "Get a Quote" → "3D Printing" → "FDM"
3. Upload `modrun_clip.stl` → PLA material → standard finish → quantity 25 (their entry-level for meaningful pricing)
4. Note quoted price and lead time → screenshot
5. Repeat for expedited delivery option (note price premium)
6. Upload `modrun_rail.stl` → same process

**Expected output:** Expedited lead time and premium cost confirmed. Useful for understanding the cost of an emergency overflow order.

### Craftcloud
1. Go to craftcloud3d.com
2. Upload `modrun_clip.stl` → select FDM → PLA → quantity 50
3. Review the multi-supplier quote list → note lowest 3 prices and corresponding manufacturers
4. Screenshot for comparison

**Decision point:** After completing all three platform quotes, you will have a reliable price range. JLC3DP is expected to be lowest; Xometry highest. The gap quantifies the premium for domestic turnaround.

---

## Step 2: The 10-Unit Sample Order (Week 2 post-test-print, ~$50–80)

**Objective:** Validate JLC3DP's FDM quality for the ModRun clip geometry before any overflow dependency.

**Why this is non-negotiable:**
The ModRun clip has a 1.4mm snap arm — the highest-risk feature for contract manufacturing. Layer orientation, infill density, and wall count directly determine whether the snap arm clicks or fails. A $50–80 sample order is the cheapest possible insurance before placing a $200–800 overflow order during a demand spike.

### JLC3DP Sample Order Instructions

1. Log into JLC3DP account
2. Upload `modrun_clip.stl`
3. **Critical specification notes to add in the "Remarks" or "Special Instructions" field:**
   ```
   Print orientation: Snap arm must be oriented vertically (Z-axis growth direction).
   Do NOT print with the arm flat/horizontal — this causes layer delamination failure.
   Infill: 25% minimum (gyroid or grid pattern)
   Walls: 3 perimeters minimum
   Layer height: 0.20mm
   Material: PLA (standard white or natural preferred for inspection)
   Post-processing: Remove all support material. Smooth support contact marks if visible.
   ```
4. Quantity: 10 units
5. Select standard shipping (5–10 days); no need for expedited on a validation order
6. Place order; save order confirmation

**Validation checklist when parts arrive:**
- [ ] Snap arm clicks audibly when pressed and rebounds cleanly
- [ ] Cable channel holds a 5mm (USB-C width) cable securely without lateral play
- [ ] Rail mating surface is flush with < 0.5mm gap when clip is seated
- [ ] No visible delamination or layer separation on snap arm
- [ ] Dimensional check: measure clip width at 3 points; all should be within ±0.4mm of STL dimension
- [ ] Surface finish: acceptable for product listing photos (minor layer lines are fine; heavy banding or stringing is not)

**If validation passes:** JLC3DP is a confirmed Tier 2 supplier. Document in `supplier-comparison-matrix.csv`.

**If validation fails:** Note specific failures. Contact JLC3DP support with photos and describe the issue. Their support team can advise on print settings adjustments. A second sample order with corrected parameters is the next step, not walking away.

---

## Step 3: Negotiation Talking Points by Supplier Type

### For Online Platforms (JLC3DP, Xometry, Craftcloud)

These platforms have algorithmic pricing — there is limited room to negotiate below the quoted price. The leverage is in:

**Volume commitment framing:**
When initiating any production conversation (especially with Xometry or Makelab, which have sales teams), use this framing:

> "I'm currently testing your platform with a small sample order. I'm building a Bambu printer farm for a cable management product line on Etsy, targeting 50–150 units/week by Q3 2026. I'm evaluating you as an overflow partner for when my farm is at capacity. What does your pricing look like for monthly recurring orders of 50–150 units?"

This opens a conversation at the account manager level for platforms with sales teams (Xometry, Makelab). Even if they cannot discount the algorithmic price today, they may offer net-30 terms or a dedicated account rep at higher volume.

**Specific asks by platform:**

| Platform | Best Ask | Expected Response |
|---|---|---|
| JLC3DP | "Do you have a volume discount tier for orders above 100 units?" | Check their site; some platforms auto-discount at 50/100/200 quantity thresholds |
| Xometry | "What does pricing look like for a net-30 account? I'm targeting $2,000–5,000/month in orders by Month 6." | Net-30 typically unlocked at $5,000 cumulative orders; they will note your account |
| Craftcloud | No direct negotiation; leverage is selecting the lowest-price manufacturer in their network | — |

### For China Direct Suppliers (Alibaba, PCBWay)

These platforms have more negotiable pricing — especially on recurring orders.

**Opening position email template (Alibaba vendor):**

```
Subject: Recurring PLA FDM Production Inquiry — Cable Management Components

Hello [Supplier Name],

I am building a cable management product line (ModRun) for the Etsy marketplace
and looking for a reliable Chinese FDM manufacturing partner for overflow production.

PRODUCT DETAILS:
- Part 1: Cable clip (PLA, ~75g, 1.4mm snap arm — functional part)
- Part 2: Cable rail (PLA, ~250g, 300mm length, channel clip)
- Files: STL files attached for quotation

VOLUME:
- Starting: 100 units/month (50 clips + 50 rails) — Q3 2026
- Scaling: 300–500 units/month by Q4 2026 as second printer farm
- Long-term: Monthly recurring order relationship

REQUIREMENTS:
1. Price per unit at 100 units/month and 300 units/month quantities
2. Lead time (production + shipping to US, standard and expedited)
3. Quality: PLA, 3 wall minimum, 25% infill, snap arm printed vertically (Z-orientation)
4. Sample: I will place a 10-unit paid sample order before committing to production volumes
5. Trade Assurance: Required for all orders — non-negotiable

Please send your quotation and confirm Trade Assurance availability.

Best regards,
[Name] | ModRun | [Email]
```

**Key negotiation points for Alibaba suppliers:**

1. **Trade Assurance is non-negotiable.** Any supplier who will not provide Trade Assurance is automatically disqualified. This protects your payment if parts do not match specifications.

2. **Sample before bulk.** Never place a production order without a validated sample. Frame this as normal: "I always start with a 10-unit paid sample to validate quality before committing to volume. Is that acceptable?"

3. **Price elasticity at 300 vs. 500 units.** Always ask: "What is your price at 100 units vs. 300 units vs. 500 units?" Get the full tier table. The step from 100 to 300 units often has the largest discount (20–35%). Knowing the 500-unit price tells you what the long-term relationship cost structure looks like.

4. **Payment terms progression.** Start with standard (30/70 deposit/final). After 2 successful orders, ask: "Can we move to a 50/50 payment structure?" After 5 orders: "Can we discuss net-15 for established buyers?"

5. **Recurring order discount.** Ask explicitly: "If I commit to a monthly recurring order for 6 months, what discount can you offer?" Recurring orders reduce their customer acquisition cost and are worth 5–15% off list price.

---

## Step 4: Counter-Offer Framework

Use this table when evaluating supplier responses:

| Supplier Quote | Your Counter | Walk-Away Condition |
|---|---|---|
| JLC3DP > $5/unit for 100-unit clip order | Upload to Craftcloud for comparison; if Craftcloud shows $3–4, use as leverage | Walk away from JLC3DP if > $5 when Craftcloud equivalent is available at < $3.50 |
| Xometry > $12/unit for 25-unit clip (urgent order) | Accept if lead time is < 3 business days and JLC3DP is not viable | Walk away at > $15/unit unless it's a literal emergency where Etsy standing is at stake |
| Alibaba quote > $3/unit for 200-unit clip order | Counter with: "Competitor is at $1.80–2.50 for same spec. Can you match $2.50?" | Walk away at > $3.50/unit for the clip; the economics of outsourcing vs. self-printing break down |
| Any supplier refuses Trade Assurance | Disqualify immediately. Do not negotiate. | Non-negotiable |
| Any supplier cannot produce snap arm in Z-orientation | Request DFM consultation; if they cannot accommodate: disqualify | Cannot outsource snap-fit parts to a shop that prints flat |

---

## Step 5: Contract and Confirmation Checklist

For every Tier 2/3 supplier order, obtain written confirmation of the following before payment:

- [ ] Part specification: file name, version, material (PLA), color
- [ ] Print orientation: snap arm vertical (Z-axis) confirmed in writing
- [ ] Infill and walls: 25% infill, 3 wall perimeters
- [ ] Quantity: exact unit count
- [ ] Lead time: production days + shipping days, in writing
- [ ] Price: per-unit and total, in writing
- [ ] Post-processing: supports removed, rough edges addressed
- [ ] Defect/rejection policy: what happens if >5% of units fail functional test upon receipt?
- [ ] Payment terms: deposit amount, final payment trigger
- [ ] For Alibaba: Trade Assurance order number confirmed

**Defect response protocol (for any contract manufacturer):**
If received parts have a defect rate above 5%: photograph all defective units with measurements, email supplier with photos, request replacement for defective units at no charge or partial refund. For Alibaba orders: file Trade Assurance dispute with photographic evidence if supplier is unresponsive within 48 hours.

---

## Step 6: Performance Monitoring (Ongoing from First Order)

After each contract manufacturer order, record in the supplier tracking sheet:

| Metric | Target | Action if Below Target |
|---|---|---|
| On-time delivery (within stated window) | 90%+ | Warn supplier; switch to alternate if two consecutive misses |
| Functional defect rate (snap arm failure) | <5% | Request replacement; document; escalate to Trade Assurance if no response |
| Dimensional accuracy (within ±0.4mm) | >95% of units | Review print spec with supplier; increase inspection rate |
| Surface finish (acceptable for product listing) | >90% of units | Request surface smoothing as post-process step |
| Quote-to-invoice accuracy | 100% | Question any unexplained charges before payment |

---

## Key Terms to Lock In (Priority Order)

1. **Print orientation spec** — The highest-risk issue with contract FDM. Get explicit written confirmation that the snap arm is printed vertically before any order.

2. **Defect replacement policy** — Know what happens if 10% of your order arrives non-functional before you need to invoke it.

3. **Lead time guarantee** — Not "typically 5–7 days" — get a written lead time commitment. Overflow orders exist because you need predictable delivery, not approximations.

4. **Price stability for recurring orders** — For any supplier you plan to use monthly, ask: "If I commit to X units/month for 6 months, will you hold this price?" Lock in price stability before you become dependent on the supplier.

5. **30-day price change notice** — For ongoing relationships, request 30-day advance notice of any price increase so you can budget or switch.

---

## Week 1 Action Checklist (Post-Test-Print)

- [ ] Create JLC3DP account; upload STL files; get quotes at 50/100/200 units; screenshot all
- [ ] Create Xometry account; upload STL files; get quotes at 25 units standard and expedited; screenshot
- [ ] Upload to Craftcloud; note top 3 cheapest manufacturer quotes
- [ ] Document all quotes in `supplier-comparison-matrix.csv` (update existing rows for JLC3DP and Xometry)
- [ ] Place 10-unit clip sample order at JLC3DP with full spec notes in remarks field
- [ ] Set calendar reminder: sample order arrival + 2 days → run validation checklist
- [ ] If sample passes: document JLC3DP as "Validated Tier 2 Supplier" in supplier tracking sheet
- [ ] Send Alibaba inquiry email to 3 suppliers (rail only; use email template from Step 3) — only if Month 6 scaling is being planned now

---

## Sources

- [How to Negotiate Supplier Payment Terms — Phoenix Strategy Group](https://www.phoenixstrategy.group/blog/how-to-negotiate-supplier-payment-terms)
- [How to Negotiate Payment Terms with Suppliers — Onramp Funds](https://www.onrampfunds.com/resources/how-to-negotiate-payment-terms-with-suppliers)
- [Net 30/60/90 Terms Guide — Resolve](https://resolvepay.com/blog/post/net-terms/)
- [Tips to Broker Favorable Payment Terms — Sourcing Allies](https://www.sourcingallies.com/blog/tips-to-broker-payment-terms)
- [JLC3DP FDM Service](https://jlc3dp.com/3d-printing/fused-deposition-modeling)
- [Xometry 3D Printing Service](https://www.xometry.com/capabilities/3d-printing-service/)
- [Craftcloud 3D Printing Marketplace](https://craftcloud3d.com/)
- [PCBWay 3D Printing](https://www.pcbway.com/rapid-prototyping/3d-printing/)
- Internal: `supply-chain-diversification-strategy.md`, `supplier-comparison-matrix.csv`, `supplier-negotiation-playbook.md` (v1 filament)
