---
title: "Phase 2 Supply Chain Risk & Contingency Planning"
prepared: 2026-05-18
session: 1218
launch-target: 2026-05-30
days-remaining: 12
status: planning document — do not execute contingencies yet; May 25 decision gates apply
references:
  - PHASE_2_SUPPLY_CHAIN_CONTINGENCIES.md (root-level, detailed scenario recovery)
  - phase-2-plant-sourcing-vendor-list.md
  - MAY_30_RISK_AND_CONTINGENCY_PLAN.md
  - phase-2-location-scout-report.md
  - PHASE_2_PHOTOGRAPHY_LOGISTICS.md
  - CANVA_SETUP_STATUS.md
  - PHASE2_PRODUCT_PRIORITIES.md
  - contingency-paths.md
  - june-6-contingency-path.md
---

# Phase 2 Supply Chain Risk & Contingency Planning

**Prepared**: May 18, 2026 — Session 1218
**Launch target**: May 30, 2026 (12 days out)
**Planning horizon**: Now through May 25 decision gates
**Purpose**: Consolidated contingency reference for the May 30 Phase 2 (Track B) launch. This document synthesizes backup supplier options, minimum viable launch thresholds, location alternatives, critical-path analysis, and a risk scoring matrix into a single decision-ready format. It is a planning document only. Do not activate any contingency path before the May 25 gate unless a delay is already confirmed and requires same-day response.

---

## Executive Summary

The May 30 launch is achievable under current conditions, but it is not guaranteed without active monitoring of four risk areas over the next 12 days. The supply chain — plant specimens from Strictly Medicinal Seeds and Prairie Moon Nursery, and dried roots from Mountain Rose Herbs — is the most visible risk but is not the most dangerous one. Every physical specimen delay has a documented same-day fallback (iNaturalist CC-BY sourcing or local retail), and the critical path to May 30 depends on guide PDF exports, not on physical specimen receipt. The single scenario that can kill May 30 is Canva production not starting by May 27. Canva work is currently at zero percent complete (Brand Kit NOT STARTED as of May 18). That gap requires immediate user attention between now and May 24.

Location scouting status: the Asheville Botanical Garden permit deadline passed May 12 without confirmed application, and the private forest farm outreach window (May 10 target) is past. The indoor studio alternative is fully documented and is now the operational baseline for the botanical photo session. No field permit is available within the May 20-22 window.

Contingency readiness: High for all physical supply chain risks. Low for Canva production start risk. The five sections below document the specific fallback paths, trigger thresholds, and decision rules.

---

## Section 1: Backup Supplier Availability

### 1.1 If Mountain Rose Herbs Misses the May 15 Target

Mountain Rose Herbs supplies American Ginseng whole dried root ($14-22/oz) and Goldenseal dried root ($14-20/oz) with 2-3 day USPS Priority lead time and same- or next-day processing. A delay from this vendor is a logistics failure, not a supply failure — dried roots are available year-round and multiple equivalents exist.

**Trigger**: No shipping confirmation email within 48 hours of order placement.

**Backup vendor table — same-day or next-day delivery options:**

| Vendor | URL | Products Available | Lead Time | Cost vs. MRH | Confidence |
|--------|-----|-------------------|-----------|--------------|------------|
| Starwest Botanicals | starwest-botanicals.com | Ginseng dried root, Goldenseal dried root, most medicinal herbs | 3-5 days USPS Priority (Sacramento CA warehouse) | Comparable ($12-22/oz ginseng, $14-22/oz goldenseal) | High — established competitor, same organic certification standards |
| Local Whole Foods / co-op / natural food store | In-person | Goldenseal dried root commonly stocked in bulk herb section; ginseng less reliable | Same day — zero shipping wait | 15-30% premium over mail-order retail markup | High for goldenseal; Medium for ginseng |
| Korean grocery store | In-person | Whole Korean red ginseng or fresh ginseng in produce/supplement aisle; root structure intact and photogenic | Same day | $10-25 for a root of adequate size | High for photography purposes |
| Amazon Prime (Frontier Co-op or Starwest listings) | amazon.com | Ginseng dried root, Goldenseal dried root | 1-2 day Prime delivery | 15-30% higher than direct-from-vendor | Medium — use only if local retail fails |
| Bulk Herb Store | bulkherbstore.com | Wide medicinal herb inventory including goldenseal | 3-5 days standard; expedited available | Comparable to Starwest | Medium — less established for shipping speed |

**Action sequence if Mountain Rose Herbs misses:**
1. Day of miss detection: call local health food store and Korean grocery to confirm goldenseal and ginseng root in stock.
2. If local stock confirmed: purchase same day. Zero timeline impact.
3. If local stock not confirmed: place Starwest Botanicals order immediately with expedited shipping. Add Amazon Prime as parallel order if shoot date is within 3 days.
4. Log vendor switch in WORKLOG.md with format: `[DATE] — MRH DELAY — fallback to [vendor] — [order confirmation number] — expected arrival [date]`.

**Cost premium for expedited shipping**: Starwest expedited (2-day FedEx) adds $12-18 to order. Amazon Prime adds zero cost over base order. Local retail adds 15-30% markup but eliminates shipping entirely. Budget impact: $15-30 maximum above the original Mountain Rose Herbs estimate.

---

### 1.2 If Strictly Medicinal Seeds and Prairie Moon Nursery Both Miss May 20-27

Strictly Medicinal Seeds supplies Black Cohosh live potted plant ($8-12) with 8-12 day lead time from order. Prairie Moon Nursery supplies Ramps bulblets ($8-15) with 7-14 day lead time. Orders placed May 13 should arrive May 20-27. If both miss simultaneously, these fallback suppliers apply:

**Fallback vendor table — live plant specimens:**

| Vendor | URL | Products | Lead Time | Cost | Confidence |
|--------|-----|----------|-----------|------|------------|
| Etsy native plant sellers | etsy.com (search: "black cohosh live plant", "ramps bulbs cultivated", "native plant Appalachian") | Black Cohosh, Ramps, Trillium — small Appalachian growers | 3-7 days if seller ships within 2 business days | $10-25/species, comparable to commercial nurseries | Medium — verify "cultivated not wild-harvested" and shipping timeline before ordering |
| NC Native Plant Society chapter plant sales | ncnps.org | Black Cohosh, Ramps, native understory species | Same day if a sale is scheduled | $4-12/plant | Medium — dependent on sale calendar; call ahead |
| Local native plant nursery (Asheville region) | Call ahead | Black Cohosh in stock at specialty native plant nurseries in Appalachian region through June | Same day | $8-18/plant | Medium — availability varies |
| Farmers market (fresh ramp leaves) | Local market | Fresh ramp leaves for leaf identification photos; bulblets sometimes available | Same day | $3-8 | High for leaf photography; not for bulb photos |
| iNaturalist CC-BY archive | inaturalist.org | Research Grade habit, leaf, and habitat photos for all species; no shipping required | Immediate — 1-2 hour sourcing sprint | $0 | Very High — this is the documented primary fallback, not a last resort |

**The iNaturalist path is not a compromise.** Per the existing sourcing plan, CC-BY photos are the baseline standard for every guide. A guide built on 5 high-quality CC-BY photos is fully publishable and competitive on Etsy. Physical specimens are an upgrade layer.

**Action sequence if both vendors miss (trigger: no tracking number from either vendor by May 19):**
1. May 19 (same day): Execute iNaturalist CC-BY sourcing sprint for Black Cohosh, Trillium, and Ramps. Complete in one 2-3 hour session. Log every photo in WORKLOG.md with observer name, iNaturalist URL, license type CC-BY, and access date.
2. May 19 (same day): Search Etsy for "black cohosh live plant" and message 2-3 sellers to confirm cultivated origin and 2-business-day ship capability. Place order with fastest-confirmed seller.
3. May 20-21: Purchase fresh ramp leaves at farmers market or co-op. Refrigerate wrapped in damp paper towel. Photograph within 48 hours of purchase.
4. Log all actions in WORKLOG.md immediately.

**Total recovery time**: 2-3 hours for iNaturalist sourcing sprint plus same-day or next-day Etsy order. No launch date impact. The live plant props are an enhancement; iNaturalist provides the complete baseline.

---

### 1.3 Cost Comparison Summary

| Scenario | Original Budget | Fallback Cost | Premium |
|----------|----------------|---------------|---------|
| Mountain Rose Herbs on time | $28-42 (ginseng + goldenseal) | — | — |
| MRH → Starwest expedited | $28-42 base + $12-18 shipping | $40-60 | $12-18 (shipping surcharge) |
| MRH → Local retail same day | $28-42 equivalent | $34-55 | $6-13 (retail markup) |
| Strictly Medicinal → Etsy | $8-12 per species | $10-25 per species | $2-13 per species |
| Prairie Moon → Farmers market | $8-15 | $3-8 (leaves only) | -$5-7 (less expensive) |
| All vendors miss → iNaturalist | $65-115 total prop budget | $0 | -$65-115 (full savings) |

If all vendors miss and the iNaturalist path is activated, the entire plant sourcing budget is saved. The cost premium for any single-vendor backup is small ($6-18). No scenario requires a budget increase greater than $20 above the original estimate.

---

## Section 2: Minimum Viable Launch

### 2.1 Canva Palette Delay: Can Launch With Existing Palette?

**Current status**: Canva Brand Kit is NOT STARTED as of May 18. The May 26 user gate for palette setup is now 8 days away.

**Answer: Yes, launch can proceed without the new Endangered Species palette.** Three options exist:

**Option A — Manual hex entry (recommended if Brand Kit not set up by May 26)**: Canva's color picker accepts direct hex code input. The Endangered Species palette (7 colors documented in `CANVA_ENDANGERED_SPECIES_STYLE_GUIDE.md`) can be entered manually per-use. This adds 2-3 minutes per color application across the guide production session but produces an identical visual result. No quality loss on final guides.

**Option B — Launch with existing Seedwarden palette**: The existing Brand Kit palette (Deep Forest Green #143b28, Warm Cream #F5EDD6, Sage #8FA882, Burnt Sienna #A0522D) is a fully functional botanical design palette documented in `CANVA_SETUP_STATUS.md`. Launching with this palette is viable. The Endangered Species Series palette adds conservation-specific signaling (Conservation Red #8B2000, Species Gold #C49A2A) that enhances positioning — but buyers will not recognize its absence.

**Option C — Build Brand Kit before May 26 (preferred)**: 30-minute one-time setup. The Brand Kit deadline should be treated as May 24 (not May 26) to leave buffer. If the Brand Kit is not set up by May 25, activate Option A for the production session.

**Phase 3 implication**: If launching with the existing palette, the Endangered Species Brand Kit setup must be completed before any Phase 3 production begins.

---

### 2.2 Which Guides Are Critical for Launch?

Based on `PHASE2_PRODUCT_PRIORITIES.md` and the Appalachian Medicinals guide blueprint, the five Phase 2 guides (American Ginseng, Goldenseal, Black Cohosh, Bloodroot, Ramps) are not equal in production complexity or photo-sourcing independence.

**Must-have guides for May 30 (2-guide minimum viable launch):**

| Guide | Why Critical | Photo Sourcing Independence | Canva Production Time |
|-------|-------------|-----------------------------|-----------------------|
| American Ginseng | Highest visual distinctiveness; dried root prop available from Mountain Rose Herbs or local retail regardless of any other delay; iNaturalist + BHL illustration complete the set | Fully independent — no live plant required | 5-6 hours (master template build) |
| Black Cohosh | No physical specimen required at all; iNaturalist CC-BY provides complete habit, leaf, and habitat coverage; this guide can be produced at any point with zero sourcing risk | Fully independent | 3-4 hours (duplicate from Ginseng master) |

**Strong-want guides (launch by June 4 if delayed):**

| Guide | Dependency | Fallback If Delayed |
|-------|------------|---------------------|
| Goldenseal | Dried root from Mountain Rose Herbs (same order as Ginseng); if MRH delays, Starwest or local retail; iNaturalist covers leaf and habitat | Starwest or local retail; 3-4 hours Canva from Ginseng master |
| Bloodroot | Rhizome prop for the orange-red sap photo (30-minute oxidation window on shoot day); this constraint is scheduling, not sourcing | iNaturalist CC-BY + BHL illustration are complete fallback; no sap photo if rhizome not obtained |
| Ramps | Fresh leaves from farmers market (within 48h of shoot); bulblets from Prairie Moon or Etsy; iNaturalist CC-BY excellent for woodland emergence and leaf identification | Farmers market same-day purchase; iNaturalist for habitat shots |

**Can-wait (Phase 3 expansion):** Any guides beyond the core five Appalachian Medicinals series. The five-guide series is the Phase 2 commitment; no guides beyond these five are on the critical path.

---

### 2.3 Revenue Impact: 3-Guide vs. 5-Guide Launch

**Assumptions**: Average guide price $15; Phase 1 buyer list converted at 8%; new traffic converting at 2%; launch-week estimate of 30-50 visitors from email + social.

| Launch Scope | Guides Live May 30 | Estimated Week-1 Revenue | Notes |
|-------------|-------------------|--------------------------|-------|
| Full launch (5 guides) | 5 | $60-90 | Maximum launch-week revenue; all 5 available to email broadcast |
| Reduced launch (3 guides) | 3 (Ginseng, Goldenseal, Black Cohosh) | $40-65 | Remaining 2 guides add $15-25 at June 4 publication |
| Minimum viable (2 guides) | 2 (Ginseng, Black Cohosh) | $25-45 | Lowest risk scenario; add Goldenseal by June 2, Bloodroot + Ramps by June 10 |

**Revenue impact of 3 vs. 5 at launch**: $20-25 difference in Week 1, recovered within 7 days when remaining guides publish. The May 30 marketing event (Kit broadcast, social posts, Etsy debut) generates the same momentum regardless of whether 3 or 5 guides are live — buyers return when they see the "full collection now available" follow-up email. A 3-guide launch is not a failure; it is a structured rollout with a documented follow-up date.

**Recommendation**: Target 5 guides. Accept 3 guides if live plant specimens for Bloodroot and Ramps have not been photographed by May 26 when Canva production begins. Never slip below 2 guides — 2 guides is the hard floor for maintaining the May 30 launch date.

---

## Section 3: Location Contingencies

### 3.1 Asheville Permit: Status and Impact

The Asheville Botanical Garden application deadline was May 12. As of May 18 (current date), the application window has closed without confirmed submission. This means the primary outdoor field location is not available for the May 20-22 shoot window.

The private forest farm access path (United Plant Savers / Western Carolina Botanical Club referral) required outreach by May 10 and written permission by May 14. That window is also past.

**Current operational baseline**: Indoor studio photography + iNaturalist CC-BY for habitat context. This is fully sufficient for a May 30 launch. The field permit situation eliminates the outdoor upgrade option; it does not create a production gap.

**What was lost by missing the Asheville permit:**
- Naturalistic woodland backdrop for full-plant-in-habitat context shots
- Seasonal water feature context for Ramps photography
- In-situ habitat colony shots for Black Cohosh and Goldenseal

**What iNaturalist CC-BY provides instead:**
- Research Grade habit and habitat observations for all four target species from multiple geographic contexts and seasonal stages
- Black Cohosh: abundant observations in Appalachian region
- Trillium grandiflorum: the most-photographed woodland wildflower in eastern North America
- Ramps: strong late-April through May archive; seasonal colony emergence well documented
- Goldenseal: adequate coverage; supplement with North Carolina Botanical Garden institutional photos if needed

**Assessment**: The outdoor field shoot would have produced stronger habitat context photos. The iNaturalist CC-BY path produces guide-quality photos that meet the commercial publication standard. Buyers purchasing botanical identification guides on Etsy do not distinguish between a CC-BY habit photo and a proprietary habit photo when both are well-selected, properly attributed, and high resolution.

---

### 3.2 Indoor Studio Alternative Timeline

**Setup**: White foam-core reflector board (24x36 inch, $8-12 at any craft store), kitchen table within 3-5 feet of the largest east- or south-facing window, smartphone or camera. Setup time: 15 minutes.

**What indoor studio produces for the guides:**
- All root and rhizome close-up shots (controlled lighting is actually superior to field for close-up ID work — eliminates harsh shadows)
- Seed and seed packet identification shots
- Dried specimen arrangements and comparative layouts
- Potted live plant habit shots (Black Cohosh, Wild Bergamot)
- Leaf detail against a controlled dark or neutral background

**Compressed indoor shoot: can 3 days compress to 2 days?**

Yes. The original 3-day field shoot plan (May 20-22) was structured around travel logistics and outdoor lighting windows (9am-11am soft light, 2pm overcast for flat illumination). Indoor studio photography eliminates both constraints. An indoor session can run from 8am to 6pm with consistent light throughout.

| Original 3-day field plan | Compressed 2-day indoor plan |
|--------------------------|------------------------------|
| Day 1: Travel to Asheville + Cluster 1 (Ginseng, Goldenseal, dried root props) | Day 1: All dried root props + potted plant props + seed ID shots — 3-4 hours |
| Day 2: Cluster 2 (live plants — Black Cohosh, Wild Bergamot) | Day 2: iNaturalist CC-BY sourcing sprint (all habitat context, habit, and flower archive) — 2-3 hours; Bloodroot rhizome shoot if specimen arrived — 1 hour |
| Day 3: Float day and reshoot | Day 3: Eliminated — absorbed by efficiency gain |

The compressed 2-day indoor plan can execute May 20-21, freeing May 22 as a float day for processing. This actually creates more calendar slack than the original 3-day field plan would have.

**Guide timeline impact from using indoor studio photos instead of outdoor location photos**: None. The guides do not have a field photography requirement. The indoor + iNaturalist path has been documented as the baseline approach since the Phase 2 photography plan was written.

---

## Section 4: Critical-Path Options

### 4.1 Guide Production Compression: 15 Days to 10 Days

The original 15-day production window (May 15-30) was designed for the full sequence including specimen arrival, acclimatization, photography, processing, and Canva production. A compressed 10-day window (May 21-30) is achievable for certain guides.

**Guides that compress from 15 days to 10 days without quality loss:**

| Guide | Why It Compresses Cleanly | Compressed Timeline |
|-------|--------------------------|---------------------|
| American Ginseng | Mountain Rose Herbs root available; iNaturalist + BHL photos sourceable in one 1-hour session; Canva master template build is a single focused work day | Photos: May 21. Canva: May 26. Export: May 26 end of day |
| Goldenseal | Same photo sourcing path as Ginseng; Canva is a template duplication from Ginseng master (3-4 hours, not 5-6) | Photos: May 21. Canva: May 27 morning. Export: May 27 midday |
| Black Cohosh | Zero physical specimen required; iNaturalist CC-BY is the complete photo set; can source and confirm photos in a 1-hour sprint at any point through May 29 | Photos: any day May 21-27. Canva: May 27 afternoon. Export: May 28 |

**Guides that do not compress easily:**

| Guide | Compression Barrier | Realistic Earliest Completion |
|-------|--------------------|-----------------------------|
| Bloodroot | Requires rhizome prop for orange-red sap photo; 30-minute oxidation window on shoot day requires dedicated scheduling around specimen receipt | May 28 if rhizome arrives by May 25 |
| Ramps | Fresh leaves must be purchased within 48 hours of shoot; constrains scheduling around farmers market availability | May 28-29 if leaves purchased May 26-27 |

**Compression conclusion**: The 3-guide core (Ginseng, Goldenseal, Black Cohosh) compresses to 10 days with no quality loss. The 2-guide tail (Bloodroot, Ramps) requires arrival/purchase events that cannot be accelerated beyond their natural constraints.

---

### 4.2 Bottleneck Identification: Where Is the Critical Path?

There are three production workstreams: (1) photo sourcing, (2) Canva guide production, (3) Etsy listing setup. The bottleneck is not photography — it is Canva production.

**Photography**: The entire photo set for all five guides can be sourced in a single day if using iNaturalist CC-BY exclusively (approximately 2-3 hours per species = 10-15 hours total for 5 species, or 2 days if divided into focused 3-hour sessions). Physical specimen photography adds 1-2 days but is not required.

**Canva guide production**: Each guide takes 3-6 hours. Five guides total: 17-22 hours across the production window. At a realistic 6-hour uninterrupted work day, this is 3-4 full days of Canva production. Canva production cannot be compressed below 3 days without accepting incomplete guides. The production window must begin by May 26.

**Etsy listing setup**: 30-45 minutes per guide (copy from blueprint, attach PDF, set price). Five listings: 2.5-4 hours total. This is not a bottleneck.

**The single critical-path item**: Canva production starting on or before May 26. Everything else — physical specimens, location access, Brand Kit setup — is a quality multiplier. Canva production start date is the launch gate. Missing May 26 by one day is recoverable (3-guide launch on May 30). Missing May 26 by two or more days triggers the June 10 deferred launch.

---

### 4.3 Worst-Case Analysis: Absolute Latest Date for May 30

**Condition**: What is the absolute latest Canva production can start and still hit May 30 with at least 2 guides?

Working backward from May 30 8:00am (Etsy listings must be publishable):
- May 29 11:00pm: Etsy drafts complete with PDFs attached
- May 29 5:00pm-11:00pm: Etsy listing setup (2.5 hours for 2 guides)
- May 29 8:00am-5:00pm: Second guide Canva production (3-4 hours minimum)
- May 28 all day: First guide Canva production (5-6 hours for Ginseng master)

**Answer: Canva production must start by 8:00am May 28 for a 2-guide minimum viable launch.** Starting at May 28 produces 2 guides by May 29 evening. Starting later than May 28 makes a May 30 launch impossible.

**However**: The May 26 start date is strongly preferred because:
- It allows 5-guide production (4 days at 5-6 hours/day)
- It builds in a buffer day (May 29) for QA and Etsy upload
- It does not require uninterrupted 8-hour days under deadline pressure
- Starting May 28 requires two full-day Canva sessions in a row with no buffer

**Non-negotiable decision rule**: If Canva has not started by end of day May 27, the realistic outcome is a 2-guide minimum viable launch, not a 5-guide launch. Decide the launch scope on May 27 and communicate it in the May 29 go/no-go check.

---

## Section 5: Risk Scoring Matrix

### 5.1 Supplier x Delay Days x Activation Threshold

| Supplier | Delay 0-2 Days | Delay 3-5 Days | Delay 6-10 Days | Delay 10+ Days | Activation Trigger |
|----------|---------------|---------------|-----------------|----------------|-------------------|
| Mountain Rose Herbs (dried roots) | No action needed | Activate local retail same day — zero launch impact | Activate Starwest Botanicals parallel order — 3-5 day recovery | iNaturalist CC-BY is complete fallback — no launch impact | No shipping confirmation within 48 hours of order |
| Strictly Medicinal Seeds (Black Cohosh live plant) | Monitor — no action | Activate Etsy native plant search | iNaturalist CC-BY sprint (2-3 hours, immediate) | iNaturalist CC-BY sprint + no live plant for launch | No tracking number by May 16 |
| Prairie Moon Nursery (Ramps bulblets) | Monitor — no action | Activate farmers market ramp leaves purchase | iNaturalist CC-BY for Ramps guide; farmers market leaves if available | iNaturalist CC-BY complete fallback | No tracking number by May 18 |
| All mail-order vendors combined miss | — | — | Execute iNaturalist sprint for all species (May 19); local retail for dried roots | June 10 deferred launch only if Canva production also blocked | All orders untracked by May 19 |
| Canva Brand Kit not set up | No action (time available) | Activate manual hex entry | Activate existing Seedwarden palette | Launch with existing palette; Endangered Species palette in Phase 3 | Brand Kit not set up by May 25 |
| Canva production not started | No action if before May 26 | 3-guide launch plan activated | 2-guide minimum viable launch | June 10 deferred launch | Canva production not started by May 27 end of day |

### 5.2 Impact Severity Rating

| Risk Item | Probability | Impact on May 30 | Recoverable Without Date Slip? |
|-----------|------------|------------------|-------------------------------|
| Mountain Rose Herbs delay | Low (very reliable vendor) | None — local fallback immediate | Yes |
| Strictly Medicinal Seeds delay | Medium (8-12 day lead time, ordered late) | None — iNaturalist CC-BY covers | Yes |
| Prairie Moon Nursery delay | Medium (7-14 day lead time) | None — farmers market or iNaturalist covers | Yes |
| Canva Brand Kit not set up | High (currently NOT STARTED) | Minor — manual hex entry is equivalent | Yes — 2-3 min/color extra |
| Canva production delayed past May 27 | Medium (depends on user schedule) | High — forces 2-guide launch or date slip | Only if started by May 28 |
| Canva production delayed past May 28 | Low-Medium | Kills May 30 launch — June 10 required | No |
| Location permit missed | Confirmed (permit deadline passed May 12) | None — indoor studio + iNaturalist is the baseline | Already resolved |
| Lifestyle photo shoot delayed | Medium (already past original May 10-11 target) | None — mockup images fill gap | Yes |

---

## Section 6: Decision Checklist

Five-to-ten specific trigger-response pairs for the May 18 to May 30 window. Check each by the indicated date.

**Trigger 1 — If no Mountain Rose Herbs shipping confirmation by May 17 (or by the day after order placement):**
Response: Call local Whole Foods, co-op, or Korean grocery to confirm goldenseal and ginseng root in stock. Purchase same day. Log purchase in WORKLOG.md. Do not wait for mail-order resolution.

**Trigger 2 — If Strictly Medicinal Seeds shows no tracking number by May 19:**
Response: Same day, open iNaturalist and begin CC-BY sourcing sprint for Black Cohosh habit, leaf close-up, and habitat shots. Filter: taxon_id=47430 (Actaea racemosa), license=CC-BY, quality_grade=research, photos=true. Log each photo in WORKLOG.md. Simultaneously search Etsy for "black cohosh live plant" and message 2 sellers about shipping timeline.

**Trigger 3 — If Prairie Moon Nursery shows no tracking number by May 19:**
Response: Same day, purchase fresh ramp leaves at local farmers market or specialty grocery. Refrigerate wrapped in damp paper towel. Photograph within 48 hours. Begin iNaturalist CC-BY sourcing for ramps woodland emergence shots (taxon_id=55701). Log in WORKLOG.md.

**Trigger 4 — If Canva Brand Kit is not set up by May 24:**
Response: On May 25, open CANVA_ENDANGERED_SPECIES_STYLE_GUIDE.md, note the 7 hex codes, and confirm the manual entry workflow. Do not delay Canva production waiting for Brand Kit. Begin guide production on May 26 using manual hex entry. Accept the 2-3 minute per-color overhead. Note in WORKLOG.md: "Brand Kit skipped — manual hex entry used throughout production."

**Trigger 5 — If Canva guide production has not started by end of day May 26:**
Response: May 27 morning, activate the 3-guide reduced scope plan. Confirm production order: (1) Ginseng master template, (2) Goldenseal from Ginseng duplicate, (3) Black Cohosh from Ginseng duplicate. Defer Bloodroot and Ramps to June 4. Update Kit launch broadcast copy to read "3 guides available now, full collection June 4." Log scope change in WORKLOG.md.

**Trigger 6 — If Canva guide production has not started by end of day May 27:**
Response: Immediately activate 2-guide minimum viable launch plan (Ginseng and Black Cohosh). Set June 10 as the target for all 5 guides published. Update Kit broadcast copy. If neither guide is in production by May 28 8:00am, activate June 10 deferred launch. Log decision in WORKLOG.md.

**Trigger 7 — If all 5 guides are not exported as PDFs by May 29 5:00pm:**
Response: Publish whichever guides are complete. Do not delay the May 30 launch for incomplete guides. Set June 4 as the completion date for remaining guides and send a follow-up Kit email on June 4: "Complete collection now available." Any guide live on May 30 is a successful launch.

**Trigger 8 — If the May 29 evening go/no-go check finds fewer than 2 guide PDFs exported:**
Response: Slip to June 10. Log in WORKLOG.md. Update Kit broadcast scheduled send date from May 30 to June 10. Update social posts scheduled dates. This is the only scenario that requires moving the launch date. Do not attempt a launch with fewer than 2 complete guide PDFs — an Etsy listing without an attached PDF fails on purchase.

**Trigger 9 — If lifestyle photo shoot has not occurred by May 24:**
Response: Launch proceeds with existing mockup images in Etsy listing slots 4 and 5. Do not delay guides for lifestyle photos. Lifestyle photos are Etsy listing enhancement images, not guide content. Schedule lifestyle shoot for June 1-7 and upload as a post-launch listing update.

**Trigger 10 — If any supplier issue is detected and no contingency path from this document clearly applies:**
Response: Open `PHASE_2_SUPPLY_CHAIN_CONTINGENCIES.md` (root-level, 39KB detailed scenario reference) and locate the vendor row in Section 4.1. Apply the documented fallback. If still unclear, apply the default rule: if the miss does not affect guide PDF production directly, it is recoverable. Execute iNaturalist sourcing and proceed.

---

## Vendor Alternates Quick-Reference Table

| Vendor Slot | Primary | Backup A | Backup B | Backup C |
|-------------|---------|----------|----------|----------|
| Dried ginseng root | Mountain Rose Herbs (mrh.com) | Starwest Botanicals (starwest-botanicals.com) | Korean grocery store (same day) | Amazon Prime — Frontier Co-op listing |
| Dried goldenseal root | Mountain Rose Herbs (mrh.com) | Starwest Botanicals (starwest-botanicals.com) | Local co-op or Whole Foods bulk herbs (same day) | Amazon Prime — Frontier Co-op listing |
| Black Cohosh live plant | Strictly Medicinal Seeds (strictlymedicinalseeds.com) | Etsy — Appalachian native plant sellers | NC Native Plant Society spring sale | iNaturalist CC-BY (no shipping required) |
| Ramps bulblets | Prairie Moon Nursery (prairiemoon.com) | Etsy — "ramps bulbs cultivated" | Farmers market fresh leaves ($3-8, same day) | iNaturalist CC-BY archive |
| Botanical habitat photos | Proprietary field shoot (permit required) | iNaturalist CC-BY Research Grade photos | NC Botanical Garden institutional archive | BHL (Biodiversity Heritage Library) historical illustrations |

---

## Timeline Recovery Options

### Best Case — All Suppliers On Time, Canva Starts May 26

**Conditions**: Mountain Rose Herbs roots confirmed photographed by May 15. Strictly Medicinal and Prairie Moon tracking confirmed by May 16-18. Photos complete (field or iNaturalist) by May 22. Brand Kit set up by May 24. Canva starts May 26.

| Date | Milestone |
|------|-----------|
| May 15 | MRH roots photographed and filed |
| May 20-21 | Indoor studio shoot for live plants; iNaturalist CC-BY for habitat |
| May 24 | Brand Kit set up |
| May 26 | Canva production begins: Ginseng master template |
| May 27 | Goldenseal guide complete |
| May 28 | Black Cohosh guide complete |
| May 29 | Bloodroot + Ramps guides complete; all 5 PDFs exported; Etsy drafts final |
| May 30, 8:00am | Final QA; publish all Etsy listings |
| May 30, 10:00am | Listings live |
| May 30, 12:00pm | Kit broadcast sends |

---

### Medium Case — 1-2 Vendors Delay 3-5 Days, Canva Starts May 27

**Trigger**: Live plant specimens arrive May 24-26 instead of May 20-22. Canva start slips one day to May 27.

| Date | Milestone | Adjustment |
|------|-----------|------------|
| May 21-22 | iNaturalist CC-BY sourcing sprint; iNaturalist replaces late-arriving vendor photos | iNaturalist sprint replaces delayed live plant photos |
| May 27 | Canva production begins: Ginseng master | 1 day later than best case |
| May 28 | Goldenseal + Black Cohosh guides complete (combined session) | Compressed double guide day |
| May 29 | Bloodroot guide complete; Ramps guide complete if fresh leaves purchased May 27 | Tight but achievable |
| May 29, 8:00pm | Go/no-go check: how many PDFs exported? | Launch with whatever is complete |
| May 30 | 3-5 guides live; remaining guides (if any) published June 4 | June 4 follow-up broadcast |

---

### Worst Case — Multiple Delays, Canva Starts May 28 or Later

**Trigger**: Canva production cannot start before May 28 due to stacked delays (vendor misses + photo processing + Brand Kit setup all consuming pre-production time).

| Date | Milestone |
|------|-----------|
| May 28, 8:00am | Canva production begins: Ginseng master only |
| May 29, all day | Black Cohosh guide (iNaturalist CC-BY, no specimen required) |
| May 29, 5:00pm | 2 guides exported as PDFs; Etsy drafts attached |
| May 30, 10:00am | 2 guides live on Etsy; Kit broadcast sends ("2 guides now, full collection June 10") |
| June 3-9 | Remaining 3 guides produced |
| June 10 | Full 5-guide collection live; follow-up Kit broadcast |

**June 10 target**: If the worst case materializes, June 10 is a comfortable full-collection launch date — 11 days of Canva production from May 30, more than enough for 3 additional guides.

---

## Final Verdict

**May 30 launch is achievable under the following contingency plan:**

Primary path: Canva production begins May 26, completes 5 guides by May 29. All physical specimen delays are handled via iNaturalist CC-BY or local retail fallbacks, none of which affect the Canva production start date.

Fallback path (Contingency Plan B): If Canva starts May 27, launch with 3 guides on May 30 and publish Bloodroot + Ramps on June 4. Revenue impact: $15-25 in Week 1, recovered by June 4.

Minimum viable path (Contingency Plan C): If Canva starts May 28, launch with 2 guides (Ginseng and Black Cohosh) on May 30 and defer remaining 3 guides to June 10.

**Remaining user decision gates before May 25:**

1. **Canva Brand Kit setup** — complete by May 24 (30-minute one-time task; currently NOT STARTED). This is the highest-urgency pre-production item. It has been not started since May 5.
2. **Confirm Mountain Rose Herbs order shipped** — verify shipping confirmation email. If no confirmation within 48 hours of order, activate local retail fallback same day.
3. **Confirm Strictly Medicinal Seeds and Prairie Moon Nursery tracking** — check by May 19. If no tracking from either vendor, execute iNaturalist sourcing sprint May 19.
4. **Clear May 26-29 calendar for Canva production** — four uninterrupted 5-6 hour work days. This is the only remaining action that determines whether May 30 launches at full scope, reduced scope, or minimum viable scope.

The supply chain is well-covered. The calendar is the constraint.

---

*Prepared: 2026-05-18. Session 1218. Seedwarden Agent. References: PHASE_2_SUPPLY_CHAIN_CONTINGENCIES.md (root-level detailed recovery scenarios), phase-2-plant-sourcing-vendor-list.md (vendor specs and costs), MAY_30_RISK_AND_CONTINGENCY_PLAN.md (platform risk analysis and partial launch viability), phase-2-location-scout-report.md (Asheville permit details and indoor studio spec), PHASE_2_PHOTOGRAPHY_LOGISTICS.md (field protocol and iNaturalist sourcing), CANVA_SETUP_STATUS.md (Brand Kit not started status), PHASE2_PRODUCT_PRIORITIES.md (guide prioritization framework), contingency-paths.md (scenario sequences), june-6-contingency-path.md (June 6 and June 10 slip path documentation).*
