---
title: Printer Farm Equipment Specifications — ModRun Fleet Matrix
project: mfg-farm (ModRun / Etsy Print Farm)
created: 2026-05-21
status: production-ready
version: 1.0
scope: Equipment evaluation matrix for 1–5 printer farm (Q2–Q4 2026); includes printers, software, infrastructure, and consumables
related:
  - MULTI_PRINTER_SCALING_ROADMAP.md
  - MULTI_PRINTER_FARM_ARCHITECTURE.md
  - PRE_PRODUCTION_SUPPLY_CHAIN_RISK_MITIGATION.md
---

# Printer Farm Equipment Specifications

**Purpose**: Production-ready equipment reference matrix for ModRun's 1-to-5 printer scaling plan. Covers printer hardware, fleet management software, infrastructure components, filament supply, and consumables. All pricing reflects verified May 2026 figures.

**Decision framework**: ModRun's baseline is the Bambu P1S ecosystem. This document evaluates alternative options at each equipment category to document why the baseline was chosen and under what conditions an alternative would be selected.

---

## Section 1: Printer Hardware Matrix

| Name | Cost (May 2026) | Spec Highlights | Integration Notes | Fleet-Scale Considerations |
|---|---|---|---|---|
| **Bambu Lab P1S** | $399 MSRP (current street price; was $699 at launch) | 256×256×256 mm build volume; 500 mm/s rated / 200–250 mm/s sustained production; fully enclosed (HEPA + carbon filter); auto bed leveling (Lidar); AMS 2 Pro compatible (multi-color); ±0.05 mm dimensional accuracy | Native integration with Bambu Farm Manager (free, LAN mode), SimplyPrint, Printago, and Obico; gcode profiles portable across all P1S units — zero reconfiguration when adding 2nd, 3rd, nth printer | **Primary recommendation for all phases.** Lowest hardware cost per throughput unit in the Bambu lineup. Enclosure supports future PETG/ABS expansion without platform change. Uniform fleet means one spare parts kit covers all printers. Reliability score 9.5/10 per farm operator community data (May 2026). |
| **Bambu Lab A1** | $399 MSRP ($329–369 on sale) | 256×256×256 mm build volume; 500 mm/s rated / 200–250 mm/s production; no enclosure; AMS Lite (4-color); ±0.05 mm accuracy | Full SimplyPrint and Printago compatibility; same Bambu ecosystem software stack as P1S; shares gcode profiles for common SKUs | Same throughput as P1S for PLA on ModRun's current product mix. Absence of enclosure limits future PETG runs (PLA does not require enclosure). Valid Phase 1 filler purchase if P1S is backordered or cash is tight; upgrade to P1S for subsequent additions. |
| **Bambu Lab A1 Mini** | $299 MSRP ($219–249 on sale) | 180×180×180 mm build volume (smaller than P1S); 500 mm/s rated; no enclosure; AMS Lite (4-color) | Same Bambu ecosystem compatibility as P1S and A1 | Smaller build plate limits multi-unit batching for any part larger than 80mm. Cable clips fit comfortably; desk rails do not. Valid for dedicated clip-only production slots. Lower unit cost makes it attractive for Phase 1 budget scaling. Do not mix with P1S fleet for rail SKUs. |
| **Bambu Lab P2S** | $549 MSRP ($499–549) | 256×256×256 mm; 600 mm/s rated / 250–300 mm/s production (15–20% faster than P1S); fully enclosed; AMS 2 Pro compatible; ±0.05 mm | Same Bambu ecosystem integration as P1S; same slicer profiles with minor speed parameter adjustment | **Phase 3+ evaluation candidate.** Community reliability data still accumulating (new in 2026). Speed advantage generates ~15–20% throughput gain per printer. At 5-printer scale, this represents 600–750 additional units/month — significant at full traction. Introduce only after 6+ months of P2S community reliability confirmation. Do not mix P2S hotend spares with P1S spares. |
| **Prusa i3 MK4S** | $799 assembled ($549 kit) | 250×210×220 mm; 400 mm/s rated / 150–200 mm/s sustained production; no enclosure; MMU3 multi-material optional ($299 add-on); ±0.1 mm accuracy; fully open-source and user-serviceable | OctoPrint native; SimplyPrint compatible; Prusa Connect cloud; not compatible with Bambu Farm Manager — would require separate monitoring stack if mixed with Bambu fleet | **Not recommended for ModRun fleet.** 15–25% slower than P1S at equivalent print quality. $400 more per unit. All parts are user-serviceable and many are 3D printable — this is its primary advantage, but Bambu's consumables cost is low enough to make repairability a secondary concern. Only warranted if Bambu hardware supply becomes a risk (ban, tariff, supply disruption), in which case MK4S is the highest-quality fallback. |
| **Creality K2 Plus** | $699–799 ($649 common sale) | 350×350×350 mm build volume; 600 mm/s rated / 180–220 mm/s production; partial enclosure; CFS 16-color system (add-on); ±0.1–0.15 mm accuracy | Klipper/Moonraker based; compatible with Obico and OctoPrint; not compatible with Bambu Farm Manager; requires separate monitoring setup | **Not recommended for ModRun fleet.** Large build volume wasted on cable clips. CFS multi-color system has documented reliability issues at high duty cycle. Lower nozzle durability interval (300–500 hours vs. P1S's 600–800 hours). Mixed fleet with Bambu adds software fragmentation cost. Creality's strongest use case is large-format parts — not relevant to ModRun's product mix. |

---

## Section 2: Fleet Management Software Matrix

| Name | Cost | Spec Highlights | Integration Notes | Fleet-Scale Considerations |
|---|---|---|---|---|
| **Bambu App (cloud)** | Free | Remote monitoring and control for all Bambu printers; push notifications; print progress camera view; basic job queue | Native Bambu cloud integration; requires internet for all commands; no job queue prioritization; no cross-printer scheduling | **Phase 0 only.** Sufficient for monitoring a single P1S. At 2+ printers, lack of queue management and cross-printer coordination becomes a real operational burden. No Etsy integration. No filament tracking. |
| **Bambu Farm Manager** | Free (Windows 10+) | LAN-mode cloud-free operation; monitors unlimited Bambu printers simultaneously; batch command dispatch; smart queue (assigns jobs based on printer availability); staggered start scheduling to prevent power overload; file management with tags and folders | Supports P1S, A1, X1C, P1 series; Windows-only (Linux/Mac planned); requires internet for initial activation only; operates fully offline after setup | **Phase 1–2 primary tool.** Launched May 2025. Free with no printer count limit covers Phase 1 (2 printers) through Phase 2 (3–4 printers) without subscription cost. Key gap: no Etsy order integration, no filament inventory tracking, no AI failure detection. Pair with a wall-mounted camera for Phase 2 failure detection until SimplyPrint is added. |
| **SimplyPrint** | $10/month (up to 10 printers, Starter) | Cloud-based fleet monitoring; AI failure detection via camera (detects spaghetti prints within 60–90 seconds); print queue management; filament tracking; mobile dashboard; broad printer compatibility (Bambu, Prusa, generic FDM) | Native Bambu API integration; camera-based failure detection requires USB webcam or compatible IP camera per printer; supports SimplyPrint's own slicer profile system; API for inventory integration | **Phase 2 add-on, Phase 3 primary.** The AI failure detection is the key value differentiator — catching one overnight failed print per month pays for the $10/month subscription 3–4× over. Filament weight tracking supports safety stock reorder discipline. Use alongside Bambu Farm Manager at Phase 2; consider transitioning fully to SimplyPrint at Phase 3. |
| **Printago** | Free tier: unlimited printers, 1 concurrent slot; $29/month: 5 concurrent slots; $99/month: unlimited concurrent | Production automation platform; Etsy/Shopify/WooCommerce order-to-print-queue integration; cloud slicing (Bambu Studio profiles in cloud); material-aware job routing; RFID filament tracking; production analytics; multi-brand support (Bambu, Klipper, Prusa) | Supports Bambu (cloud and LAN mode), Klipper, Prusa; 3MF files from Bambu Studio import directly; order integration via webhooks; ecommerce platform API connections | **Phase 3 evaluation, Phase 3+ primary.** The Etsy-to-queue automation is the feature that justifies the cost at high order volume — eliminating manual job transcription at 50+ orders/day saves 30–45 minutes of operator time daily. Free tier allows validation before committing to paid. At 5 printers and $7,000+/month revenue, $29/month for 5 concurrent slots is a rounding error. |
| **Obico (formerly OctoEverywhere)** | $10/month Pro | AI failure detection; remote monitoring and control; Bambu and OctoPrint compatible; push notifications; print history | Bambu native plugin available; pairs with Bambu App for failure alerts | Alternative to SimplyPrint for AI failure detection only. Less comprehensive queue management. Use if already familiar with OctoEverywhere from prior printers. SimplyPrint is preferred for new ModRun deployment due to stronger Bambu-native integration. |

---

## Section 3: Infrastructure and Facility Equipment Matrix

| Name | Cost | Spec Highlights | Integration Notes | Fleet-Scale Considerations |
|---|---|---|---|---|
| **Workbench (6 ft, heavy-duty)** | $80–150 | 72"×30" steel or wood-top; 500 lb capacity; adjustable height | Supports 2 P1S printers side-by-side with AMS clearance; add pegboard mount above for tools and spare parts | Phase 1 (2 printers): one bench sufficient. Phase 2 (4 printers): add second bench or extend to 10 ft total. Phase 3 (5 printers): L-shaped bench configuration allows QC station perpendicular to printer row. |
| **Surge-Protected Power Strip (6-outlet, 2,100 J)** | $25–40 each | 6-outlet; 2,100+ joule surge rating; 15–20A; preferably with individual outlet switches | One per 2-printer pair; plug P1S into switched outlets for staggered start implementation; route cabling under bench to avoid tangle | Do not daisy-chain power strips. Phase 2 (4 printers): two power strips on one 20A circuit with staggered starts. Phase 3 (5 printers): split across two dedicated 20A circuits. |
| **UPS (APC 1500VA)** | $150–200 | 1,500W capacity; 8–12 min runtime at 1,000W load; automatic voltage regulation; USB monitoring port | Connects between wall circuit and power strip; protects 2 P1S printers from power interruption during print jobs | Phase 1–2: one UPS per 2-printer pair. Phase 3: one UPS per 2-printer pair (3 total for 5-printer farm). Prevents mid-layer power loss events — a 3-hour print abandoned 2 hours in wastes 100g of filament and 2 hours of machine time. |
| **Window Exhaust Fan (110 CFM)** | $40–60 | 110 CFM airflow; 4" duct compatible; 110V plug-in | Vent through window or exterior wall; maintains 8+ air changes per hour in print room up to 36 m³ | Phase 0–1: P1S internal HEPA/carbon filter is sufficient for PLA. Phase 2 (3+ printers): add exhaust fan for room-level air exchange. Not a health requirement for PLA, but reduces ambient particle accumulation and keeps room cooler. |
| **Dehumidifier (30-pint)** | $150–200 | 30-pint/day capacity; integrated humidistat; continuous drain option | Set to 40% RH; place centrally between printer rows; empty reservoir daily or route continuous drain to sink | Phase 2 and beyond. Above 55% RH, unsealed PLA spools absorb moisture within hours, causing print artifacts (bubbling, stringing, poor layer adhesion). One dehumidifier covers a 65–100 sq ft print room. |
| **Sunlu S4 Filament Dry Box** | $80–120 | Active heating to 55°C; holds 4–6 standard 1 kg spools; integrated humidity display; 5–15% RH capability | Printers load directly from dry box via PTFE tube; prevents moisture uptake during active use (vs. airtight bins that require manual spool transfer) | Phase 2 add-on. Four spools of active working colors stay dry continuously. Less critical for black/white PLA than for specialty colors, PETG, or any hygroscopic material. Cost: ~$80–120 one-time. |
| **Industrial Dry Cabinet** | $400–700 | 60–100 kg capacity; constant <5% RH; powered by desiccant regeneration | Passive dry storage for bulk filament inventory; no active heating | Phase 3+ (5-printer farm with 30+ kg/month consumption). Replaces airtight bins and silica gel at scale. One-time investment. |
| **QC Bench Tools (calipers + IPA + wipes)** | $30–60 total | Digital calipers ±0.01 mm; 99% IPA in spray bottle; lint-free shop wipes | Calipers for snap-arm dimensional check (±0.05 mm spec); IPA for bed wipe and part cleaning | One set per farm, shared. Upgrade to second set at Phase 3 if QC tech and operator work simultaneously. |
| **Postal Scale (0.1 oz precision)** | $25–40 | 11 lb capacity; 0.1 oz / 1g resolution; tare function | Used for Pirate Ship weight entry; prevents overpay on shipping labels; catches assembly errors (missing clip in bundle) | One per farm. Does not scale with printer count. |

---

## Section 4: Filament Supply Matrix

| Name | Cost/kg (May 2026) | Spec Highlights | Integration Notes | Fleet-Scale Considerations |
|---|---|---|---|---|
| **eSUN PLA+ Pro (Amazon)** | $12–14/kg (10-kg bundle); $15–18/kg single spool | 1.75mm ±0.03 mm diameter tolerance; tensile strength 52 MPa; AMS-confirmed compatible; consistent batch-to-batch color | Amazon Prime 1–2 day delivery; ASIN stable stock for black/white/grey; specialty colors subject to availability gaps | **Phase 0–2 primary.** Proven AMS compatibility. 10-kg bundles at $120–140 provide 2 weeks supply at Phase 2 volumes. Limit: Chinese-origin (tariff exposure); specialty color availability is unreliable. Restrict to 5 core production colors. |
| **Overture PLA+ (Amazon)** | $11–14/kg single; sub-$11/kg in 4-pack | 1.75mm ±0.05 mm; AMS confirmed; broad color range; broad US fulfillment center coverage | Same Amazon Prime delivery as eSUN; 4-pack availability often covers color gaps when eSUN runs short | **Phase 0–2 backup / emergency fill.** Order when eSUN's specific color is OOS. Quality consistent with eSUN for cable management applications. Slight diameter tolerance disadvantage (±0.05 vs. ±0.03) — negligible for non-precision PLA parts. |
| **Polymaker PolyLite PLA (wholesale)** | $14.99/kg (wholesale; $1,000 minimum order); $16–20/kg retail | 1.75mm ±0.02 mm diameter (tighter than retail brands); tensile strength 58 MPa; "Print Farm Tested" Bambu AMS certification; manufactured in USA from NatureWorks Ingeo pellets; 3 kg large spools available | Ships next-day from Texas; free shipping on orders over $3,000; RFID spool tags compatible with Printago RFID tracking; batch-to-batch color consistency guaranteed | **Phase 2 activation (40+ kg/month consumption), Phase 3 primary (60% of volume).** At $14.99/kg wholesale vs. $12–13/kg eSUN retail, the premium is ~$0.15/unit at 75g average weight — offset by tariff immunity and quality consistency. The $1,000 MOQ at Phase 2 scale (40–50 kg/month) represents 2–2.5 weeks of supply. Domestic manufacturing eliminates tariff exposure entirely. |
| **MatterHackers Build Series PLA** | $19–23/kg (retail); wholesale pricing available via business account | 1.75mm; NatureWorks 4043D Ingeo PLA (domestic); AMS confirmed; broad color selection with good restocking reliability | 2–4 day standard shipping; free shipping on orders over $35; PRO Series (same base material) at ~$24/kg | **Phase 2–3 secondary domestic source (30% of volume alongside Polymaker).** Slightly higher cost than Polymaker wholesale but no MOQ requirement — order in 5-spool increments as needed. Use for color variants not available at Polymaker, or as surge fill when Polymaker order is in transit. |
| **Polar Filament PLA (Michigan)** | ~$18.99/kg; free shipping on 3+ spools | Michigan-manufactured; NatureWorks sourced; AMS compatibility not yet confirmed for Bambu | 3–5 day standard shipping from Michigan | **Phase 3 tariff-emergency backup.** More expensive than Polymaker at equivalent domestic sourcing. Use only if Polymaker wholesale is supply-constrained. Confirm AMS compatibility via 1-spool test before committing to bulk order. |
| **Hatchbox PLA (Amazon)** | $25–28/kg | 4.7-star Amazon rating (40,954+ reviews); consistent quality; AMS confirmed | Amazon Prime 1–2 day delivery | **Premium quality option for headphone hook SKUs** where surface finish is more visible to buyers. 2× the cost of eSUN — justified only for high-visibility products, not cable clips. |

---

## Section 5: Printer Consumables and Spare Parts Matrix

| Name | Cost | Spec Highlights | Integration Notes | Fleet-Scale Considerations |
|---|---|---|---|---|
| **Bambu P1S Nozzle 0.4mm (hardened steel)** | $3–5 each (Bambu official); $8–15 for 2–5 pack (Amazon compatible) | 0.4mm diameter; hardened steel (suitable for PLA, PETG; use copper for abrasive filaments); 600–800 hour wear interval | Direct swap — 5-minute replacement; no calibration required after swap (P1S re-runs first-layer calibration automatically on next print start) | Safety stock: 6 per printer (18–24 months at 40 hr/week). Replace proactively at 600 hours to prevent clog-caused failures. Track hours via SimplyPrint. At 5 printers, hold 30 nozzles total (~$90–150 for full fleet stock). |
| **Bambu P1S Textured PEI Plate (256×256 mm)** | $25–40 (Bambu official); $12–25 (Amazon compatible) | Textured PEI on spring steel magnetic base; dual-side textured; compatible with PLA, PETG, TPU, ABS; 9–12 month durability at production duty cycle | Magnetic snap-on; no tools required; clean with IPA wipe before every batch; acetone wash every 200 prints to restore full adhesion | Safety stock: 1 spare per printer. Replace when adhesion degrades (bubbles, worn spots, first-layer failures with clean bed). At 5 printers, hold 5 spare plates. Annual replacement cost: ~$125–200 for full fleet. |
| **PTFE Tubing (1.75mm ID, 2–4mm OD)** | $5–15 for 2-meter length | PTFE hotend tubing; replace at 800–1,000 hours; discoloration and yellowing indicate replacement time | Cut to length; push-fit into hotend; no tools required beyond tube cutter | Hold 2 meters per printer (4 replacements). Annual cost: ~$10–15 per printer. Failure mode: jamming and inconsistent extrusion. |
| **Heating Cartridge (24V, 50W)** | $8–12 each | Replaces hotend heating element; rare failure but production-stopping; installs in 20 minutes | Requires hotend cooldown before replacement; follow Bambu disassembly guide | Hold 1 per printer. Replace if heat-up time exceeds 5 minutes or temperature readings are erratic. Annual failure rate: <0.5 per printer at normal duty cycle. |
| **Thermistor (NTC 100K)** | $5–8 each | Replaces hotend temperature sensor; rare failure; production-stopping | Install procedure identical to heating cartridge | Hold 1 per printer. Same failure trigger as heating cartridge. |
| **Drive Belt (XY axis pair)** | $15–25/set | Replaces X and Y motion system belts; 1,500–2,000 hour interval; tension loss causes dimensional drift before snapping | Requires 30-minute replacement; tension calibration after install | Hold 1 set per 2 printers. Annual cost: ~$15–25 per printer. Replace when dimensional accuracy degrades or belt vibration noise increases. |
| **P1S HEPA + Carbon Filter Set** | $15–25 | Internal air filtration (VOC and particle capture); replace every 200–400 hours of PLA printing (3–6 months at production duty cycle) | Tool-free replacement; slide-in filter cassette | Annual cost: ~$30–50 per printer at production duty cycle. Required for enclosure filtration efficacy. |

---

## Section 6: Summary — Recommended Equipment by Phase

### Phase 0 (May–June 2026): Single Printer Launch
**Hardware**: 1× Bambu P1S (existing)
**Software**: Bambu App (free)
**Infrastructure**: Standard 20A outlet; existing benchtop; 6× nozzles + 1 spare PEI plate pre-staged
**Filament**: eSUN PLA+ (black ×3, white ×2, grey ×1 — see PRE_PRODUCTION_SUPPLY_CHAIN_RISK_MITIGATION.md Section 7.1)
**Total new capital**: ~$90 (filament) + ~$75–110 (consumables kit) = **~$165–200**

### Phase 1 (June–July 2026): 2-Printer Cluster
**Hardware**: +1× Bambu P1S ($399)
**Software**: Bambu Farm Manager (free); add wall-mounted webcam ($30–50) for visual monitoring
**Infrastructure**: Evaluate dedicated 20A circuit; add UPS if budget allows ($150–200)
**Filament**: Increase safety stock; begin Overture as secondary source
**Total new capital**: **~$580–650** (printer + monitoring + optional UPS)

### Phase 2 (July–August 2026): 3–4 Printer Cluster
**Hardware**: +1–2× Bambu P1S ($399–798)
**Software**: SimplyPrint Starter ($10/month)
**Infrastructure**: Dedicated 20A circuit ($150–250); dehumidifier ($150–200); Sunlu S4 dry box ($80–120); UPS per 2 printers ($150–200 × 2)
**Filament**: Activate Polymaker wholesale account; first $1,000 bulk order at 40+ kg/month
**Total new capital**: **~$1,600–2,400** (across 3- and 4-printer acquisitions + infrastructure)

### Phase 3 (September–November 2026): 5-Printer Cluster
**Hardware**: +1× Bambu P1S ($399); designate as color specialist
**Software**: Evaluate Printago Starter ($29/month) alongside SimplyPrint; choose one by end of Phase 3
**Infrastructure**: Second dedicated 20A circuit ($150–250); 110 CFM exhaust fan ($50–60); second UPS ($150–200)
**Filament**: Polymaker wholesale as primary (60%); MatterHackers as secondary (30%); eSUN as emergency fill (10%)
**Staffing**: Begin FT production tech recruiting (6-week lead time)
**Total new capital**: **~$1,000–1,200** (printer + electrical + ventilation) + **$2,400–2,880/month** (FT tech when hired)

---

## Equipment Cost Summary Table

| Category | Phase 0 | Phase 1 Add | Phase 2 Add | Phase 3 Add | Cumulative 5-Printer |
|---|---|---|---|---|---|
| Printer hardware | $0 (sunk) | $399 | $399–798 | $399 | $1,197–1,596 |
| Software subscriptions | $0 | $0 | $120/yr (SimplyPrint) | $348–588/yr (Printago or SimplyPrint Pro) | $468–708/yr |
| Electrical infrastructure | $0 | $0–200 | $150–250 | $150–250 | $300–700 |
| UPS | $0 | $150–200 | $300–400 | $150–200 | $600–800 |
| Ventilation (fan + dehumidifier) | $0 | $0 | $200–260 | $50–60 | $250–320 |
| Filament dry storage | $40–60 (bins) | $0 | $80–120 (Sunlu S4) | $0 | $120–180 |
| Consumables kit (per printer) | $75–110 | $75–110 | $150–220 (2 printers) | $75–110 | $375–550 |
| **Phase total (hardware + infra)** | **$115–170** | **$624–709** | **$1,279–2,048** | **$824–1,019** | **$3,313–4,654** |

Note: Filament costs are operational expenses (consumed in production), not capital. Labor costs are excluded from this table (see MULTI_PRINTER_SCALING_ROADMAP.md Section 2.5 for staffing model).

---

## Sources

- [Bambu Lab P1S — Official US Store](https://us.store.bambulab.com/products/p1s)
- [Bambu Lab A1 — Official US Store](https://us.store.bambulab.com/products/a1)
- [Bambu Farm Manager Wiki](https://wiki.bambulab.com/en/software/bambu-farm-manager)
- [Bambu Farm Manager FAQ](https://wiki.bambulab.com/en/software/bambu-farm-faq-troubleshoot)
- [Bambu Lab Print Farm Manager Launch — Tom's Hardware](https://www.tomshardware.com/3d-printing/bambu-lab-introduces-free-software-to-manage-an-unlimited-number-of-3d-printers-simultaneously-cloud-free-lan-mode-print-farm-manager-program-simplifies-mass-3d-printing)
- [SimplyPrint Pricing and Features](https://simplyprint.io/pricing)
- [Printago Bambu Lab Farms](https://printago.io/solutions/bambu-lab-farms)
- [Printago vs SimplyPrint](https://printago.io/alternatives/simplyprint)
- [Polymaker Wholesale Print Farm Page](https://us-wholesale.polymaker.com/pages/wholesale-filament-for-print-farms)
- [Prusa MK4S Specifications — Prusa3D](https://www.prusa3d.com/product/original-prusa-mk4s-3d-printer/)
- [Bambu vs Prusa vs Creality 2026 — LayerMath](https://layermath.com/blog/bambu-vs-prusa-vs-creality-2026)
- [Best PLA Filaments Amazon US 2026 — 3D Printed Decor](https://3dprinteddecor.com/best-pla-filaments-on-amazon-us/)
- mfg-farm/MULTI_PRINTER_FARM_ARCHITECTURE.md — TCO analysis, hardware decision matrix
- mfg-farm/PRE_PRODUCTION_SUPPLY_CHAIN_RISK_MITIGATION.md — filament vendor directory, safety stock
- mfg-farm/8-printer-farm-cost-model.md — operational cost model by volume tier
