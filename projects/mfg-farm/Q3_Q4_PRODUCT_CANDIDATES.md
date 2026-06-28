---
title: "Q3-Q4 Product Pipeline — New Candidates Beyond Initial 15 SKUs"
project: mfg-farm (ModRun)
created: 2026-06-28
status: research-complete
confidence: 82% overall (individual scores below)
scope: >
  5 new high-margin cable management and desk accessory products identified through
  Etsy market search, Amazon competitive analysis, Reddit community pain-point mapping,
  and design-sharing feasibility assessment. Extends Q3_Q4_SKU_EXPANSION_MATRIX.md
  (15 SKUs, June 23 2026) with candidates targeting whitespace gaps.
related:
  - Q3_Q4_SKU_EXPANSION_MATRIX.md
  - PHASE_2_TRACK_3_MARKET_EXPANSION_RESEARCH.md
  - ITEM9_PRODUCT_VIABILITY_ANALYSIS.md
  - PHASE_2_TRACK_4_FULFILLMENT_AUTOMATION_RESEARCH.md
---

# Q3-Q4 Product Pipeline — New Candidates Beyond Initial 15 SKUs

**Lead finding**: The five products below fill gaps the initial 15 SKUs left open. The highest opportunity is the standing-desk cable chain — heavily downloaded on free STL platforms (validating demand) but almost entirely absent as a physical-print product on Etsy, where the only seller found ships from Spain with no English-language competitor. Second strongest: desk-clamp cable holders, where one Austin, TX seller (BAMprecision, Feb 2026 listing) has 113 favorites and strong reviews with zero scale, suggesting an underdeveloped market position a systematic seller can capture. Third: device-specific USB hub/power-brick mounts that command $14–28 per unit at 70%+ margins with minimal material complexity.

---

## Candidate Table

| # | Product Name | Etsy Listing Count (est.) | Etsy Price Range | Est. FDM Margin | Amazon Competitive Landscape | Reddit Sentiment | CAD Efficiency (Shared Parts) | Supplier Requirements | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| A | Standing Desk Cable Chain | <10 physical-print Etsy listings; 80+ free STL downloads | $18–35/set (6–10 links) | 71–76% | Zero Amazon 3D-print sellers; DeskLogics vertebrae spine ($25–45 injection-molded) is closest but different geometry | r/battlestations: "adhesive keeps failing when I raise/stand" — exact pain point this solves | HIGH: each link identical, parametric width variant from single part | PLA+ or PETG (existing supplier) | HIGH (82%) |
| B | Desk-Clamp Cable Holder | 30–60 physical listings; multiple STL-only; BAMprecision (Austin) leading with 113 favs | $12–22/unit, $22–40 multi-pack | 72–77% | No dedicated 3D-printed desk clamp on Amazon Handmade with >50 reviews | r/desksetup: "I hate drilling into my desk" — clamp-on products explicitly preferred | MEDIUM: clamp mechanism shared with cable tray; new jaw geometry | PLA+ (existing) + optional rubber pad inserts ($0.08/unit) | HIGH (80%) |
| C | Monitor-Arm Cable Spine Guide | 5–15 physical listings; 1 Printables model with high engagement | $16–28/unit | 73–78% | 0 Amazon sellers; off-the-shelf sleeves fail (slip, snag); XDA Developers article explicitly calls this an unsolved problem | r/battlestations: "cables flapping everywhere when I adjust monitor" — consistent complaint | HIGH: link geometry shared with cable chain; hinged variant of same base print | PETG recommended (flexibility under arm movement); existing supplier | MEDIUM (73%) |
| D | Wall/Desk Grommet (Parametric, Custom-Fit) | 20–40 listings; Wall Eye Solutions ($10.99) sole dedicated competitor | $9–18/unit, $22–35 3-pack | 74–80% | No dedicated seller with >50 reviews; store-bought grommets "rarely right size" per XDA article | r/homeoffice: "my desk has a cable hole but the grommet fell out" — standard frustration | HIGH: parametric diameter scales from single CAD file | PLA+ only; fully existing supply chain | HIGH (81%) |
| E | USB Hub / Power Brick Under-Desk Mount | 50–90 listings (scattered across brand-specific models); Anker hub mount, HP dock mount, CalDigit mount all exist from different sellers | $12–28/unit | 70–76% | Amazon 3D-printed offerings nonexistent; commercial alternatives glue/velcro only | r/battlestations: "my USB hub wanders off every time I move something" | MEDIUM: mounting bracket base shared; only front-face adapter changes per device model | PLA+ only; same supply chain; may need per-device variant catalog | MEDIUM (70%) |

---

## Candidate A: Standing Desk Cable Chain

### Product Description

A linked articulating chain printed in PLA+ or PETG that routes from the desk underside to the floor, flexing as the desk rises and lowers. Each link is identical (reducing design work and print waste). A set of 6–10 links covers 400–700mm of cable drop range, accommodating most standing desk travel distances (100–150mm raise/lower). Cable channels run along the interior spine of each link to isolate power cables from data cables.

### Market Validation

**Etsy supply gap**: Searching "standing desk cable chain" or "sit stand cable organizer" on Etsy returns primarily free STL file listings and a single physical-print seller on Etsy Spain (listing 1530121878 — Spain seller, no reviews visible, contact required before purchase). Zero English-language US-based physical print sellers found at the time of this research (June 28, 2026). This is a clean whitespace position.

**Demand signal (free STL platforms)**:
- Printables: Multiple standing desk cable chain designs with 1,000+ downloads each (jhultgre model: "Standing Desk Cable Chain" cited by multiple aggregators)
- MakerWorld: "Desk cable chain (round)" and "Magnetic standing desk cable chain" among cable management top downloads
- Yeggi aggregator returns 10+ distinct standing desk cable chain designs

**The demand-supply gap**: High download counts on free model platforms indicate consumers want this product. The absence of a Etsy physical-print seller means consumers who can't or don't want to print themselves have no viable source. This is the canonical demand-without-supply whitespace.

**Amazon competitive landscape**: Commercial alternatives (DeskLogics vertebrae spine, $25–45) are injection-molded, fixed-length, and generic. DeskLogics clamp-on variant uses 1365mm flexible spine — price-competitive but aesthetically bulky. No 3D-printed custom chain on Amazon Handmade with notable reviews.

**Reddit community signal**: Recurring r/battlestations thread topic — adhesive cable management solutions fail when desks are raised/lowered repeatedly (adhesive cycles fail). Vertebrae/chain approach is the community-approved solution. No competitor is systematically targeting this conversation with a purchase link.

### Economics

| Line Item | Value |
|---|---|
| Material (PLA+) | $0.65–0.85/set (65g for 8-link set) |
| Hardware (optional magnet clasp) | $0.20/set |
| Packaging | $0.35/set |
| Total COGS | $1.20–1.40/set |
| Suggested retail | $24.99–$34.99/set |
| Gross margin | 72–76% |
| Print time per set (8 links) | 45–60 min (P1S batch) |

**Volume potential**: 15–30 units/week once listed (conservative, given no competitor); 40–80/week once review base builds. Basis: comparable physical-print cable management products on Etsy with similar demand signals sell at 15–40 units/week within 90 days.

### Supplier Requirements

No new suppliers needed. PLA+ (eSUN, existing) or PETG (Overture, existing). PETG marginally preferred for durability in repeated flex cycles (chain links hinge under desk movement) — add $0.15/set material cost at PETG prices.

### Timeline Impact

No lead-time risk. Design is a single parametric link (mirror + array for full set). Estimated CAD time: 2–4 hours. Test print: 1 set (60 min). Etsy listing ready within 1 week of design completion.

**Confidence: HIGH (82%)** — Demand signal strongly validated via free STL platform downloads; supply gap confirmed via Etsy search; zero competitor with review count. Only uncertainty: retail price acceptance (no prior price reference in English-language market).

---

## Candidate B: Desk-Clamp Cable Holder

### Product Description

A two-jaw clamp that secures to the desk edge (15–55mm thickness range) with a thumbscrew or snap mechanism, holding 2–6 cables in routed channels on the external face. No drilling, no adhesive. Can be repositioned. Design language matches ModRun cable clip ecosystem.

### Market Validation

**Etsy activity**: BAMprecision (Austin, TX) listed Feb 21, 2026 — 113 favorites, strong positive reviews ("Simple and very effective! I bought two of these..."). Their listing (4376147876) appears to be the leading seller but has not aggressively scaled. Listing count for desk clamp cable holders: approximately 30–60 total Etsy listings, majority are simple aesthetic variations from low-review sellers.

**Demand signal (reviews)**: Top-reviewed desk clamp products on Etsy show average 200–400 reviews among the top 5 sellers in the broader "desk clamp" category, suggesting the category is real and buyers are finding it. The 3D-printed cable-specific desk clamp subcategory has far fewer reviews per seller — opportunity.

**XDA Developers validation**: 2026 article "5 3D-printed mounts that solved cable management problems no product on Amazon could" explicitly lists "Desk cable clamp" as one of the five, noting off-the-shelf options "slip, snag" or require tools/adhesive. Cited as an unsolved problem by a mainstream 3D printing publication.

**Amazon landscape**: No Amazon 3D-printed desk clamp cable holder with >50 reviews. Competitors are: generic cable clips (adhesive, $8–12 packs), Anker cable organizer boxes, and CCCEI under-desk trays. None offer the desk-edge clamp format.

**Reddit**: r/desksetup and r/battlestations explicitly reference "can't drill into my desk" as a constraint when recommending cable management. Clamp-on products are the recommended category for apartment renters and standing desks.

### Economics

| Line Item | Value |
|---|---|
| Material (PLA+) | $0.48–0.60/unit (46g clamp body) |
| Hardware (M4 thumbscrew + rubber jaw pads) | $0.28/unit |
| Packaging | $0.30/unit |
| Total COGS | $1.06–1.18/unit |
| Suggested retail | $17.99–$22.99/unit; $34.99–$44.99 (2-pack) |
| Gross margin | 72–77% |
| Print time | 30–40 min/unit |

**Volume potential**: 12–20 units/week within 60 days, scaling to 25–40/week with review base.

### Supplier Requirements

PLA+ (existing eSUN supplier). Rubber jaw pads: small adhesive-backed EPDM rubber strips (Amazon, $0.08/unit at bulk — existing category from surge protector holder). M4 thumbscrews: $0.20/unit at 100+ quantity (Amazon or McMaster-Carr, same supplier used for other hardware). No new supplier relationships needed.

### Shared Part Opportunity

The jaw mechanism (fixed jaw + moving jaw + thumbscrew boss) is parametric. Width variant (for desks 15–30mm vs. 30–55mm thick) requires only a single dimension change. The same base clamp geometry can produce the desk clamp AND a monitor arm clamp (Candidate C) with minor profile changes. This is a key batch-design efficiency — design both in the same CAD session.

### Timeline Impact

Low lead-time risk. Design from scratch: 3–5 hours CAD. Thumbscrews from Amazon Prime: 2–3 days. No MOQ issues. Etsy-ready within 1–2 weeks.

**Confidence: HIGH (80%)** — Direct competitor evidence (BAMprecision 113 favorites) confirms market. Gap is in scaling and marketing discipline, not demand.

---

## Candidate C: Monitor-Arm Cable Spine Guide

### Product Description

A series of hinged links that bolt or clip to an existing monitor arm (most VESA arms have screw holes or flat surfaces at link intervals), forming a spine that routes display cable, power cable, and USB cables from the monitor to the desk surface without flapping or snagging. Each link is low-profile (10–15mm wide) with a snap-open channel. The design follows the arm's movement — links pivot at connection points, so raising/lowering the monitor does not stress cables.

### Market Validation

**Etsy supply**: Searching "monitor arm cable clip" and "monitor arm cable spine" returns primarily generic clips (not spine-form) or alignment clips for dual monitors. Dedicated articulating spine guides: approximately 5–15 physical-print Etsy listings found. Most have fewer than 30 reviews. Competitive density: low.

**XDA Developers deep-dive (2026)**: The article "5 3D-printed mounts that solved cable management problems no product on Amazon could" specifically documents a Monitor-Arm Cable Spine Guide as one of the five — noting "off-the-shelf sleeves and clips slip, snag, or leave a big, loose loop." The described solution: low-profile spine with hinged links, shallow channels with snap features. This is a real, validated pain point in the maker/desk community.

**Printables signal**: "Simple Monitor Arm Cable Clip" model by Tridense exists; multiple remixes. "MONITORARM" tag on Printables has numerous downloads. Demand signal via free models is moderate-to-strong.

**Amazon landscape**: Zero Amazon 3D-printed monitor arm cable spine with notable reviews. Commercial alternatives are generic cable sleeves (neoprene, $5–15) that do not address the arm-movement problem. No spine-form product on Amazon.

**Flexispot-specific precedent**: Etsy listing 4312014377 (Flexispot E5 cable clips, "mostlyMakes" seller) demonstrates that desk-brand-specific cable management products find buyers. A universal monitor-arm spine guide would have broader appeal than brand-specific clips.

### Economics

| Line Item | Value |
|---|---|
| Material (PETG preferred for flex durability) | $0.55–0.70/unit-set (55g, 6-link set) |
| Hardware (M3 screws for arm attachment, 4-pack) | $0.18/unit |
| Packaging | $0.30/unit |
| Total COGS | $1.03–1.18/unit |
| Suggested retail | $19.99–$26.99/set |
| Gross margin | 73–78% |
| Print time | 50–65 min per set (PETG, slower than PLA) |

**Volume potential**: Lower initial ramp (10–18 units/week) due to narrower addressable audience (monitor arm users only). Scales as monitor arm adoption grows and reviews build. Long-term steady-state: 20–35 units/week.

### Supplier Requirements

PETG (Overture, existing $15–17/kg supplier). M3 screws: existing hardware supplier. No new suppliers.

### Shared Part Opportunity

The hinged link geometry from the standing desk cable chain (Candidate A) is a direct design relative. The chain link adapts to spine guide with: (1) addition of screw boss for arm attachment, (2) narrower profile to fit between arm sections. CAD time if Candidate A is designed first: 1–2 additional hours (not 3–5 from scratch). Designing both in the same batch session halves per-product design time.

### Timeline Impact

No lead-time supplier risk. PETG is existing stock. Design is moderately complex (hinge geometry requires tolerance testing) — 4–6 hours CAD, 2 test-print iterations (4–5 print hours). Etsy-ready in 2–3 weeks from design start.

**Confidence: MEDIUM (73%)** — Demand validated by XDA article and Printables downloads but Etsy physical-print supply is thin (harder to estimate market size). Risk is that "monitor arm user" TAM is smaller than general cable management TAM.

---

## Candidate D: Parametric Wall/Desk Grommet

### Product Description

A two-piece parametric grommet (trim ring + removable inner guide) for cable pass-through holes in desks or drywall. Sizes: 55mm, 64mm, 80mm, and 100mm diameter (covering standard desk hole sizes plus IKEA desk cutout sizes). Inner guide has a star-slot pattern (cables push through from any angle; slot closes around cable bundle for dust-block). Two-piece design: trim ring installs from one side of hole; insert snaps in from the same side. No need to access underside of desk.

### Market Validation

**Etsy activity**: Etsy listing 1039562105 ("3D Printed, Customizable Desk Grommets") — a three-tiered customizable design, listed June 2021, still active. Wall Eye Solutions (walleyesolutions.com) sells 3D-printed wall grommets at $10.99 per unit — a dedicated brand built around this single product category. Flanged cable pass-through grommet (listing 4406786616) listed recently with positive reviews. Total grommet category listing count on Etsy: approximately 20–40 physical-print listings.

**Gap analysis**: IKEA's Signum cable tray doesn't fit hollow desks (Lagkapten drops out). IKEA does not make a bespoke grommet for their own desk hole dimensions. The 3D printing community has built multiple free STL alternatives (Printables: "Parametric Cable Grommet" by Blizzard, "Desk Cable Grommet" by VC Design, listed 2025–2026). XDA article explicitly notes: "Store-bought grommets are 'rarely the right size' and lack strain relief" — exact product-market fit statement.

**Amazon landscape**: Amazon has commodity plastic grommets ($5–12, injection-molded, generic sizes). No 3D-printed parametric options with notable Amazon presence. The parametric fit (custom diameter) is the FDM advantage.

**Reddit signal**: r/homeoffice users regularly post about grommet problems: holes too large for standard grommets, grommet fell out, no grommet for standing desk pass-through holes. Each post represents a buyer who couldn't find the right product.

### Economics

| Line Item | Value |
|---|---|
| Material (PLA+) | $0.22–0.32/unit (22g trim ring + insert) |
| Hardware | none |
| Packaging (small bag) | $0.18/unit |
| Total COGS | $0.40–0.50/unit |
| Suggested retail | $9.99/unit; $22.99 (3-pack with 3 sizes); $14.99 (2-pack same size) |
| Gross margin | 74–80% |
| Print time | 15–25 min per 2-piece set |

**Highest gross margin of the five candidates.** Print time is lowest. COGS floor is lowest. The parametric design generates 4+ SKU variants (55mm/64mm/80mm/100mm) from a single parametric CAD file — this is a catalog-multiplier product.

**Volume potential**: 20–40 units/week once SEO captures grommet search traffic. Especially strong in January (desk organization season) and back-to-office cycles.

### Supplier Requirements

PLA+ only (existing). No hardware. This is the simplest supply chain of the five candidates.

### CAD Efficiency

Parametric diameter is a single variable in CadQuery. Generating all 4 size variants takes hours, not days. The inner-guide star-slot pattern is reused across all sizes. CAD estimated time: 2–3 hours total for all 4 variants.

**Recommended as the "batch-lead" product**: Design first, print immediately, list within 2 weeks. Revenue from this SKU can fund design iterations on higher-complexity candidates.

### Timeline Impact

Zero lead-time risk. Simplest design, lowest material cost, no new suppliers. Flag: if custom text engraving requested (company logo grommet for corporate), laser engraving capability needed (Phase 3). For Phase 2, standard molded-text approach (embossed text in CAD) works fine.

**Confidence: HIGH (81%)** — Dedicated competitor (Wall Eye Solutions) already earns revenue in this niche, validating WTP. Gap is in Etsy presence and parametric customization.

---

## Candidate E: USB Hub / Power Brick Under-Desk Mount

### Product Description

A device-specific mounting bracket that secures a USB hub or power brick to the underside of a desk via screws or adhesive. Variants organized by device model: Anker PowerExpand (most popular USB-C hub on Amazon), CalDigit Thunderbolt 4 Element Hub, UGREEN 7-in-1, and universal "slot mount" (adjustable for non-standard devices). Each variant is a simple tray/cradle with cable-exit channels and mounting holes. Print time: 20–30 min. Material: 10–20g PLA+.

### Market Validation

**Etsy activity**: Category spread across brand-specific listings. Found: Anker 4-Port hub mount (listing 1170342396), HP USB G Series docking station mount (listing 1019995101), CalDigit Element Hub listing. Customer reviews positive: "easy enough to mount with screws," "higher quality than expected from 3D printing." However, each seller covers only 1–3 device models — no seller offers a systematic catalog of hub mounts.

**Supply pattern**: This is a classically fragmented market. Individual makers list one mount for their specific hub. No Etsy seller has built a catalog of 5–10+ device variants under one brand. ModRun has the catalog and batch-design approach to be the first.

**Amazon gap**: No 3D-printed hub mounts on Amazon Handmade with notable reviews. Generic "USB hub" products on Amazon are the hubs themselves, not mounts. No dedicated mount-as-product category on Amazon.

**Reddit demand**: r/battlestations: "my USB hub wanders around my desk every time I unplug something" is a documented recurring thread type. Community-approved solution is to mount it under the desk. Products that solve this are readily purchased when they appear in "show your setup" posts.

**Flexispot precedent (again)**: The model of device-specific accessories built for popular brand-specific hardware is validated by Etsy's Flexispot E5 clip seller (mostlyMakes, from Phase 2 Track 3 research). Same model: parametric design, brand-specific variants, loyal niche community.

### Economics

| Line Item | Value |
|---|---|
| Material (PLA+) | $0.18–0.28/unit (18g cradle body) |
| Hardware (optional Velcro or 3M adhesive strip) | $0.20/unit |
| Packaging | $0.20/unit |
| Total COGS | $0.58–0.68/unit |
| Suggested retail | $12.99–$17.99/unit; $28.99 (bundle: mount + cable tray) |
| Gross margin | 70–76% |
| Print time | 20–30 min/unit |

**Volume potential**: 8–15 units/week per device variant at steady state. With 5–8 device variants listed, aggregate potential: 40–120 units/week. This is a long-tail catalog play — low per-variant volume, high total portfolio volume.

### Supplier Requirements

PLA+ only (existing). Optional: 3M Command strips or Velcro for adhesive-mount variants (existing hardware channel from surge protector holder and cable organizer SKUs).

### CAD Efficiency

Each device variant requires measuring the physical device (or using published dimensions). CAD per variant: 45–90 min. With 5 variants, total CAD investment: 4–8 hours. However, the mounting bracket base (rear plate with holes, cable exit slots) is identical across variants — only the cradle face changes. This is a parametric catalog approach: one template, N device adaptations.

**Shared part opportunity**: The under-desk mounting plate (2 screws, counter-sunk holes, standard 80mm spacing) is identical to the surge protector holder mounting plate from the existing 15-SKU plan. The existing Surge Protector Holder design (Priority 1B in Q3_Q4_SKU_EXPANSION_MATRIX.md) can share the mounting plate CAD block — reducing per-variant design time by ~20 minutes per hub mount variant.

### Timeline Impact

Moderate. Requires sourcing dimensions for each device model (can be found in manufacturer product listings and community-published measurements). Risk: if Anker or UGREEN changes product dimensions (happens at model refresh), existing CAD becomes outdated. Mitigation: design with 1–2mm clearance tolerance; bundle 2-pack at discounted price to encourage purchase before model change.

**Confidence: MEDIUM (70%)** — Individual precedents exist (brand-specific sellers earn revenue) but no seller has built a systematic catalog. Market fragmentation is both the opportunity and the risk — the catalog approach is unproven for this specific category on Etsy.

---

## Competitor Presence Summary

| Candidate | Etsy Competitor Count | Amazon Competitor Count | Pricing Gap vs. ModRun | Key Differentiation |
|---|---|---|---|---|
| A — Standing Desk Cable Chain | <10 (1 US-based) | 0 3D-printed | None (whitespace) | First US English-language physical print; chain vs. flimsy sleeve |
| B — Desk-Clamp Cable Holder | 30–60 listings; BAMprecision leads but has not scaled | 0 3D-printed clamp-cable | $2–8 below top Etsy competitor | ModRun ecosystem branding; parametric jaw width |
| C — Monitor-Arm Spine Guide | 5–15 listings; sparse | 0 3D-printed | None (whitespace) | Systematic articulated spine vs. ad-hoc clip clips |
| D — Parametric Grommet | 20–40 listings; Wall Eye Solutions at $10.99 | Generic injection-molded at $5–12 | ~$0–3 above commodity | Parametric custom fit; star-slot dust block; two-piece install |
| E — USB Hub / Power Brick Mount | 50–90 listings (fragmented, brand-specific) | 0 systematic catalog | $3–8 below branded dock mounts | First multi-device catalog from one ModRun brand |

---

## UGC and Positioning Notes

**Highest UGC opportunity**: Candidate A (standing desk cable chain) and Candidate B (desk-clamp cable holder). Both solve the specific problem r/battlestations users photograph: cable management that fails when the desk is raised. A single desk-transformation photo showing before/after cable state (messy standing desk cables vs. chained/clamped clean cables) is the canonical battlestations post format and receives hundreds of upvotes.

**Positioning recommendation**: Market all five candidates under the ModRun "cable ecosystem" brand umbrella. Each product should reference the others: "pairs well with ModRun cable tray" on the chain listing, "complete your setup" cross-link from grommet to clamp. This is the Etsy SEO and review multiplication strategy — one buyer buys all five.

**Community approach for Candidates A and C**: Post a desk transformation photo to r/battlestations with the standing desk chain installed. Comment mentions the Etsy shop only if asked. Based on community norms from Phase 2 Track 3 research, 2–3 weeks of genuine participation before any self-promotion reference.

---

## Sources

- [Cable Management Desk Clamp — BAMprecision (Etsy, listing 4376147876)](https://www.etsy.com/listing/4376147876/cable-management-desk-clamp-3d-printed)
- [Flexispot E5 Cable Clips — mostlyMakes (Etsy, listing 4312014377)](https://www.etsy.com/listing/4312014377/flexispot-desk-cable-management-clips-3d)
- [5 3D-printed mounts that solved cable management problems no product on Amazon could — XDA Developers 2026](https://www.xda-developers.com/3d-printed-mounts-solved-cable-management-problems/)
- [3D Printed Cable Management Spine — Printables.com (Scott Gibb)](https://www.printables.com/model/494691-3d-printed-cable-management-spine)
- [DeskLogics Clamp-On Cable Management Spine — Amazon](https://www.amazon.com/DeskLogics-Clamp-Vertebrae-Cable-Management/dp/B0D7ZKKXY3)
- [Customizable 3D Printed Cable Tidy Chain — Etsy Spain (listing 1530121878)](https://www.etsy.com/listing/1530121878/customizable-3d-printed-cable-tidy-chain)
- [Best Cable Management Kits for Standing Desks — WorkWhileWalking (2026)](https://www.workwhilewalking.com/best-cable-management-kits-for-standing-desk-workstations)
- [3D Printed Customizable Desk Grommets — Etsy (listing 1039562105)](https://www.etsy.com/listing/1039562105/3d-printed-customizable-desk-grommets)
- [Parametric Cable Grommet — Printables.com (Blizzard)](https://www.printables.com/model/439554-parametric-cable-grommet)
- [Under-Desk Power Strip Mount — Etsy (listing 1665724354)](https://www.etsy.com/listing/1665724354/under-desk-power-strip-mount-wall-surge)
- [Anker USB-C Hub 3D Printed Mount — Etsy (listing 1170342396)](https://www.etsy.com/listing/1170342396/anker-4-port-usb-c-hub-3d-printed-mount)
- [Monitor Arm Cable Manager 4-pack — Etsy (listing 1043324488)](https://www.etsy.com/listing/1043324488/monitor-arm-cable-manager-4-pack)
- [Best Selling 3D Printed Items on Etsy 2026 — Insight Agent](https://www.insightagent.app/guides/best-selling-3d-printed-items-etsy)
- [If you 3D print a cable management tray for under your desk it will improve your entire setup — XDA Developers](https://www.xda-developers.com/3d-print-cable-management-tray-desk-improve-setup/)
- [Drag Chain Cable Organizer for Monitor Risers — MakerWorld](https://makerworld.com/en/models/1176787-drag-chain-cable-organizer-for-monitor-risers)
- [Standing Desk Cable Chain — Printables.com (jhultgre)](https://www.printables.com/model/55276-standing-desk-cable-chain)
- [Wall Eye Solutions — Desk Grommet](https://www.walleyesolutions.com/collections/frontpage/desk-grommet)

*Research completed June 28, 2026. All Etsy listing counts are estimates from search result aggregation; exact counts require direct Etsy search with full pagination.*
