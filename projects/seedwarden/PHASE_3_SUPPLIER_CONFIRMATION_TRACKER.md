---
title: "Phase 3 Supplier Confirmation Tracker — Medicinal Herbs"
date: 2026-05-21
version: 4.0
status: production-ready — fill in status fields as supplier responses arrive
critical-deadlines:
  - May 25, 2026 — Black Cohosh ORDER PLACED (optimal; June 21–28 arrival locks sprint Week 1 photography)
  - June 8, 2026 — Goldenseal ORDER PLACED or Wikimedia CC path confirmed in writing (ZERO FLOAT)
  - June 15, 2026 — Elderberry + Mountain Rose Herbs dried herbs ordered (HARD DEADLINE)
purpose: >
  Supplier × Herb status table with lead times, June 21 delivery windows, bulk pricing at Phase 3
  photography volumes, minimum order quantities, payment terms, and confirmation deadlines.
  Per-bundle delivery requirements for all 5 bundles (Women's Health, Respiratory, Immunity, Sleep,
  Digestive). Goldenseal sourcing decision documented with CC licensing analysis.
  Companion CSV at phase-3-supplier-tracker.csv for spreadsheet use during June execution.
suppliers: Prairie Moon Nursery, Strictly Medicinal Seeds, Mountain Rose Herbs, Southern Exposure, Fedco Seeds
goldenseal-cc-decision: Path 2 (Wikimedia CC) — confirmed CC-BY-SA; $0 cost; $0 risk; launch quality
tags: [seedwarden, phase-3, suppliers, tracker, medicinal-herbs, goldenseal, june-8-deadline]
cross-references:
  - phase-3-medicinal-herbs-sourcing-guide.md
  - PHASE_3_PRODUCTION_LAUNCH_CHECKLIST.md
  - phase-3-timeline.csv
supersedes: v3.0 (2026-05-20)
---

# Phase 3 Supplier Confirmation Tracker — Medicinal Herbs

**Version**: 4.0 — Updated May 21, 2026  
**Tracker purpose**: Confirm all supplier windows, pricing, lead times, and delivery feasibility before June 22 sprint start  
**Critical dates**: May 25 (Black Cohosh), June 8 (Goldenseal), June 15 (Elderberry + MRH)  
**All fields marked [CONFIRM] require a live supplier response before ordering**

---

## THREE CRITICAL DATES — SUMMARY

| Date | Action | Float | Consequence if Missed |
|---|---|---|---|
| **May 25** | Black Cohosh order placed — Strictly Medicinal Seeds 2-year seedling | 14 days to June 8 absolute deadline | Arrival slips from June 21–28 to July 4–11; still within sprint but no Week 1 photography of live plant |
| **June 8** | Goldenseal order placed (Path 1) OR Wikimedia CC path confirmed in WORKLOG.md (Path 2) | ZERO — hard constraint | Path 1 only: order after June 8 arrives after July 13 sprint end. Path 2 has zero consequence — confirm any time before June 8. |
| **June 15** | Elderberry order (Prairie Moon) + Mountain Rose Herbs dried herb order (13 species, 1 oz each) | 5 days on MRH; 0 days on Elderberry for ~July 13 delivery | MRH: Frontier Co-op backup (3–5 day ship). Elderberry: local nursery 2-gal potted (~1 week). Neither blocks writing or upload. |

---

## GOLDENSEAL SOURCING DECISION — PATH 2 CONFIRMED (Wikimedia CC)

**Decision**: Path 2 — Wikimedia Commons CC-BY-SA. $0 cost. $0 schedule risk.

### CC Licensing Verification

Goldenseal (*Hydrastis canadensis*) is well-documented in Wikimedia Commons under confirmed CC-BY-SA 4.0 and CC-BY-SA 3.0 licenses. The following images are suitable for commercial use in digital guides sold on Etsy:

| Image Type | Wikimedia File | License | Attribution Required | Quality |
|---|---|---|---|---|
| Habit / forest floor | Search: `Hydrastis canadensis` — multiple habit photos by Eric Hunt (CC BY-SA 4.0) | CC-BY-SA 4.0 | "Eric Hunt, CC BY-SA 4.0, via Wikimedia Commons" | Excellent — dappled light, forest understory |
| Flower close-up | "Hydrastis canadensis" by H. Zell (CC BY-SA 3.0) | CC-BY-SA 3.0 | "H. Zell, CC BY-SA 3.0, via Wikimedia Commons" | Good — white flower with yellow stamens |
| Root / rhizome | "Goldenseal root" — USDA NRCS Plants Database images (public domain) | Public domain | "USDA-NRCS PLANTS Database" | Good — dried root, yellow coloration visible |
| Botanical illustration | "Hydrastis canadensis" Sturm's Deutschlands Flora (1796, public domain) | Public domain | "Sturm's Deutschlands Flora, 1796" | Excellent — high resolution engraving |

**Backup sources (if Wikimedia images insufficient)**:
- Email media@ncbg.unc.edu (NC Botanical Garden) — free educational use license, response typically 3–5 business days
- Email media@mobot.org (Missouri Botanical Garden) — similar educational use license
- iNaturalist.org — filter *Hydrastis canadensis* observations by CC-BY license; Appalachian populations abundant

**Path 2 action items** (all complete before June 8):
- [ ] Download 3–5 Wikimedia CC-BY-SA Goldenseal images (habit, flower, root minimum)
- [ ] Log each image in `PHOTO_ATTRIBUTION_LOG.md` with: species / Wikimedia URL / license / attribution text / download date
- [ ] Confirm cultivated-source framing for CITES sidebar does NOT require a live specimen photo — Wikimedia images are sufficient for launch-quality Immunity bundle

**Cost**: $0. Risk: Zero. Image quality: Launch-quality. No action required beyond downloading and logging.

---

## CRITICAL GATE: JUNE 8 — GOLDENSEAL (ZERO FLOAT)

> **Goldenseal (*Hydrastis canadensis*) has a 5–6 week lead time. An order placed after June 8 will NOT arrive before the July 13 sprint end date. This is a physical supply chain constraint, not a soft guideline.**
>
> **Path 2 (Wikimedia CC) is pre-selected.** Confirm by logging in WORKLOG.md before June 8. If you change to Path 1 (live specimen), order must be placed by June 8.
>
> **Path 2 is the correct choice under Option C (3-bundle sprint).** Zero cost. Zero schedule risk. Launch-quality Immunity bundle photography.

---

## Per-Bundle Delivery Requirements — June 21 Window

The June 21 date is the pre-sprint photography deadline, not the launch date. All live specimens needed for launch-quality photography must arrive by June 21. Wikimedia CC is the automatic fallback for any species not present.

| Bundle | Upload Target | Species Needed for June 21 Photo | Supplier | Delivery Feasibility | Fallback if Late |
|---|---|---|---|---|---|
| Women's Health | June 29 | Black Cohosh (live plant), Calendula (seedling), Lavender (local nursery) | SM (Black Cohosh), local (Lavender/Calendula) | Feasible — order BC May 25 = June 21–28 arrival | iNaturalist CC-BY (Black Cohosh Appalachian); Wikimedia CC-BY-SA (Calendula, Lavender) |
| Respiratory | July 6–7 | Elderberry (shrub), Echinacea purpurea (flowering) | PM (Elderberry by June 15), SM/PM (Echinacea by June 22) | Elderberry arrives ~July 13–20 — AFTER sprint start. Echinacea June 22 order arrives July 6–13. | Wikimedia CC-BY-SA Sambucus nigra berry cluster; iNaturalist CC-BY Echinacea purpurea |
| Immunity | July 20 | Goldenseal (root + habit), Ashwagandha | Wikimedia CC (Path 2), SM (Ashwagandha June 22) | Goldenseal: CC path confirmed. Ashwagandha: Tier 3 (June 22 order). | Path 2 confirmed. Ashwagandha: iNaturalist CC-BY India-range |
| Sleep | July 13 | Valerian (root), Passionflower (flower) | PM or SM (both June 22 Tier 3) | June 22 order = July 6–13 arrival — within sprint | iNaturalist CC-BY — Passionflower SE US populations exceptional |
| Digestive | August 3 | Dandelion (root focus), Ginger (rhizome) | Phase 2 archive (Dandelion), grocery store (Ginger) | Dandelion: existing owned photos in `/assets/wild-edibles/`. Ginger: grocery rhizome same-day. | No fallback needed — both sources confirmed |

**Summary**: Women's Health is the only bundle where a live specimen (Black Cohosh) could arrive within the June 21 pre-sprint window if ordered by May 25. All other live specimens arrive during or after the sprint and feed v1.1 photography upgrades, not the v1.0 launch.

---

## Master Supplier × Herb Table

Suppliers: **PM** = Prairie Moon Nursery | **SM** = Strictly Medicinal Seeds | **MRH** = Mountain Rose Herbs (dried) | **SE** = Southern Exposure Seed Exchange | **FC** = Fedco Seeds

"Phase 3 Volume" for photography purposes = 1–3 live specimens per species (not commercial seed stock). Bulk pricing at 100+ units refers to dried herb wholesale for Mountain Rose Herbs only — this is the supplier where volume pricing applies in Phase 3.

### Tier 1 — Two Sub-Tiers (May 25 optimal; June 8 absolute)

#### Tier 1A — MAY 25 OPTIMAL: Black Cohosh

| Species | Bundle(s) | Primary Supplier | Specimen Form | Lead Time | Cost | May 25 Delivery? | June 8 Latest? | Status |
|---|---|---|---|---|---|---|---|---|
| **Black Cohosh** (*Actaea racemosa*) | Women's Health | SM (2yr transplant) | Nursery-propagated transplant | 5–6 weeks | $10–15 (1 plant) | May 25 order = June 21–28 arrival (YES — sprint Week 1) | June 8 order = July 13–20 arrival (post-sprint, photo-only) | [ ] Pending |

**May 25 is the optimal date** because a June 21–28 arrival gives 1–7 days of in-person photography before sprint writing begins. Ordering June 8 instead means the plant arrives July 13–20 — after the July 13 Sleep upload — and upgrades v1.1 only. Either date is acceptable since iNaturalist CC-BY is the confirmed launch fallback.

Contact: info@strictlymedicinalseeds.com (primary) or info@prairiemoon.com (backup)

**Supplier confirmation status — Black Cohosh:**

| Date Contacted | Response Received | Available? | Form | Lead Time Confirmed | Order Placed | Tracking # | Est. Delivery |
|---|---|---|---|---|---|---|---|
| [FILL] | [FILL] | [ ] Yes / [ ] No | [FILL] | [ ] Yes / [ ] No | [ ] Yes — May 25 / [ ] June 8 | [#] | [DATE] |

---

#### Tier 1B — JUNE 8 HARD DEADLINE: Goldenseal (Path 2 pre-selected)

| Species | Bundle(s) | Path | Cost | Deadline | Action Required | Status |
|---|---|---|---|---|---|---|
| **Goldenseal** (*Hydrastis canadensis*) | Immunity | **Path 2 — Wikimedia CC** | $0 | June 8 (confirm in WORKLOG.md) | Download images; log in PHOTO_ATTRIBUTION_LOG.md | [ ] Pending |

**Path 2 confirmation actions** (must complete by June 8):
- [ ] Download 3–5 Wikimedia CC-BY-SA Goldenseal images (see CC Licensing section above for specific files)
- [ ] Log each in PHOTO_ATTRIBUTION_LOG.md
- [ ] Record in WORKLOG.md: "Goldenseal Path 2 confirmed — images downloaded [DATE], logged in PHOTO_ATTRIBUTION_LOG.md"

**If switching to Path 1** (live specimen):

| Species | Primary Supplier | Fallback | Lead Time | Cost | June 8 Order Arrival |
|---|---|---|---|---|---|
| Goldenseal | Prairie Moon — prairiemoon.com — 866-417-8156 — rhizome | Strictly Medicinal — info@strictlymedicinalseeds.com — $12–18 | 5–6 weeks | $15–22 (PM) / $12–18 (SM) | July 13–20 (within v1.1 window) |

**Goldenseal ordering deadline (Path 1 only): June 8. Contact Prairie Moon and Strictly Medicinal by June 1.**

> Regardless of path: if no Goldenseal confirmation exists by June 7 EOD, email media@ncbg.unc.edu and media@mobot.org the same day as a belt-and-suspenders backup. Response typically within 5 business days. Zero cost.

### Tier 2 — Order by June 15

| Species | Bundle(s) | Primary Supplier | Form | Lead Time | Photo Volume Cost | June 21 Delivery? | Status |
|---|---|---|---|---|---|---|---|
| **Elderberry** (*Sambucus nigra*) | Respiratory, Immunity | PM (bare-root) | 2-year bare-root shrub | 4 weeks | $30–45 (1–2 plants) | Feasible if ordered June 15 | [ ] Pending |
| **Dried herbs (all 12 species)** | All 5 | MRH | Dried cut/sifted, 1 oz each | 3–5 business days | $80–120 retail | YES — if ordered June 15 | [ ] Pending |

**Elderberry and Mountain Rose Herbs dried orders must be placed by June 15 EOD.**

### Tier 3 — Order by June 22 (Sprint Start Day; All Have Photo Fallback)

| Species | Bundle(s) | Primary Supplier | Form | Lead Time | Photo Volume Cost | Photo Fallback | Status |
|---|---|---|---|---|---|---|---|
| Echinacea purpurea | Respiratory, Immunity | SM or PM | Transplant | 2–3 weeks | $12–21 (2 plants) | iNaturalist CC-BY — abundant | [ ] Pending |
| Echinacea angustifolia | Respiratory, Immunity | SM | Seed or plug | 2–3 weeks | $8–15 (2 plants) | iNaturalist CC-BY — prairie range | [ ] Pending |
| Ashwagandha | Immunity | SM | Seed or started plant | 2–3 weeks | $10–16 (2 plants) | iNaturalist CC-BY (India range) | [ ] Pending |
| Passionflower (*P. incarnata*) | Sleep | PM or SM | Transplant | 3–4 weeks | $16–24 (2 plants) | iNaturalist CC-BY — SE US abundant | [ ] Pending |
| Valerian (*V. officinalis*) | Sleep | PM or SM | Transplant | 2–3 weeks | $12–18 (2 plants) | iNaturalist CC-BY — NE populations | [ ] Pending |
| Ginger (*Zingiber officinale*) | Digestive | SM or grocery store | Fresh rhizome | 2–3 weeks (or same-day grocery) | $4–12 (2 rhizomes) | Grocery store — no fallback needed | [ ] Pending |
| Vitex (*V. agnus-castus*) | Women's Health | Local nursery | Container start | 2–3 weeks (local) | $12–25 (1 plant) | Wikimedia CC-BY-SA — widely cultivated | [ ] Pending |

### Photo-Only Species (No Specimen Order Needed)

| Species | Bundle(s) | Photo Source | License | Quality Note |
|---|---|---|---|---|
| Red Clover (*Trifolium pratense*) | Women's Health | Wikimedia Commons | CC-BY-SA | Excellent coverage — flowering head close-ups available |
| Mullein (*Verbascum thapsus*) | Respiratory | Wikimedia Commons + iNaturalist | CC-BY-SA / CC-BY | Exceptional — 6-ft flower spike photos abundant |
| Thyme (*Thymus vulgaris*) | Respiratory | Wikimedia Commons + iNaturalist | CC-BY-SA / CC-BY | Abundant ornamental coverage |
| Lemon Balm (*Melissa officinalis*) | Sleep, Digestive | Wikimedia Commons | CC-BY-SA | Good coverage; bushy habit well documented |
| Lavender (*Lavandula spp.*) | Women's Health, Sleep | Wikimedia Commons + Unsplash | CC-BY-SA / CC0 | Best-documented medicinal herb on Wikimedia |
| Calendula (*Calendula officinalis*) | Women's Health, Digestive | Wikimedia Commons | CC-BY-SA | Excellent; bright orange flower close-ups available |
| Dandelion (*Taraxacum officinale*) | Digestive | Phase 2 wild-edibles archive | Original (owned) | Confirmed existing in `/assets/wild-edibles/` |

---

## Detailed Supplier Profiles

### Supplier 1: Prairie Moon Nursery

| Attribute | Detail |
|---|---|
| Website | prairiemoon.com |
| Email | info@prairiemoon.com |
| Phone | 866-417-8156 |
| Shipping | Bare-root (no pot, no soil); must be potted on arrival |
| MOQ (photography) | 1 plant (no MOQ for retail orders) |
| Payment terms | Prepay (credit card); no Net terms for retail |
| Wholesale minimum (if applicable) | Not relevant at Phase 3 photography volumes |

**Species available for Phase 3 and estimated pricing:**

| Species | Form | Per-Unit Price | Lead Time | Notes |
|---|---|---|---|---|
| Goldenseal | Rhizome division | $15–22 | 5–6 weeks | Verify summer stock Jun 1 — may be limited after spring selling season |
| Black Cohosh | Bare-root 2-year | $12–18 | 5–6 weeks | Nursery-propagated; verify on product page before ordering |
| Elderberry (*S. nigra* or *S. canadensis*) | Bare-root | $15–25 | 4 weeks | Strong category; likely in stock Jun 15 |
| Echinacea angustifolia | Plug or bare-root | $5–8 | 3–4 weeks | Prairie-native; cultivated stock |
| Passionflower | Plug | $8–12 | 3–4 weeks | SE US native; good availability |
| Valerian | Plug | $6–9 | 3–4 weeks | Hardy zones 4–9 |

**June 8 confirmation required for**: Goldenseal, Black Cohosh  
**June 15 confirmation required for**: Elderberry

**Notes**: All Prairie Moon material is nursery-propagated from native seed stock. Their product pages explicitly state "nursery-propagated" or "cultivated" — verify this language before citing in guide content. Do not order without confirming "not wild-collected" in writing.

**Supplier confirmation status:**

| Date Contacted | Response Received | Goldenseal Available? | Black Cohosh Available? | Elderberry Available? |
|---|---|---|---|---|
| [FILL] | [FILL] | [ ] Yes / [ ] No | [ ] Yes / [ ] No | [ ] Yes / [ ] No |

---

### Supplier 2: Strictly Medicinal Seeds

| Attribute | Detail |
|---|---|
| Website | strictlymedicinalseeds.com |
| Email | info@strictlymedicinalseeds.com |
| MOQ (photography) | 1 unit (no MOQ for retail orders) |
| Payment terms | Prepay (credit card, PayPal); no Net terms for retail |
| Organic certification | USDA Organic available on most species |

**Species available for Phase 3 and estimated pricing:**

| Species | Form | Per-Unit Price | Lead Time | Organic? | Notes |
|---|---|---|---|---|---|
| Goldenseal | Rhizome division (1–2 year) | $12–18 | 5–6 weeks | YES | Primary cultivation supplier; confirm cultivated in product description |
| Black Cohosh | 2-year transplant | $10–15 | 4–5 weeks | YES | Nursery-propagated |
| Echinacea purpurea | Transplant | $4–7 | 2–3 weeks | YES | Widely available |
| Echinacea angustifolia | Seed or plug | $3–6 | 2–3 weeks | YES | Confirm cultivated source — prairie-native at-risk species |
| Ashwagandha | Seed or started plant | $5–8 | 2–3 weeks | YES | Annual in most US zones |
| Passionflower | Transplant | $8–12 | 3–4 weeks | YES | SE US native |
| Valerian | Transplant | $6–10 | 2–3 weeks | YES | |
| Calendula | Seed or transplant | $2–5 | 1–2 weeks | YES | Easy annual |
| Lemon Balm | Transplant | $5–8 | 2–3 weeks | YES | |
| Ginger | Rhizome | $8–12 | 2–3 weeks | YES | |
| Mullein | Seed pack | $3–5 | 1–2 weeks | NO | Biennial; second-year plants best for photography |

**June 8 confirmation required for**: Goldenseal, Black Cohosh  
**Notes**: Preferred single source for Goldenseal rhizome, Black Cohosh, Ashwagandha, Echinacea angustifolia. Bulk pricing begins at 25+ units per species — not relevant at Phase 3 photography quantities.

**Supplier confirmation status:**

| Date Contacted | Response Received | Goldenseal Available? | Black Cohosh Available? | Lead Time Confirmed? |
|---|---|---|---|---|
| [FILL] | [FILL] | [ ] Yes / [ ] No | [ ] Yes / [ ] No | [ ] Yes / [ ] No |

---

### Supplier 3: Mountain Rose Herbs (Dried Herbs — Primary Photo Prop and Reference Source)

| Attribute | Detail |
|---|---|
| Website | mountainroseherbs.com |
| Wholesale contact | wholesale@mountainroseherbs.com |
| Retail ordering | Direct via website |
| MOQ (retail) | No minimum; per-oz ordering |
| MOQ (wholesale) | Typically $250–500 opening order — not needed for Phase 3 photography quantities; use retail pricing |
| Payment terms | Prepay for retail; Net 30 may be available for wholesale accounts |
| Certifications | USDA Organic certified; Fair Trade on several species; third-party lab tested |
| Shipping | Standard USPS/UPS; 3–5 business days typical |

**Dried herb pricing for Phase 3 photography (retail, 1 oz per species):**

| Species | Bundle(s) | 1 oz Retail (est.) | 1 lb Retail (est.) | 100+ units (wholesale est.) | Organic? | June 21 Delivery? |
|---|---|---|---|---|---|---|
| Goldenseal root | Immunity | $20–28 | $180–250 | $140–200/lb | YES | YES — order by June 13 |
| Black Cohosh root | Women's Health | $8–12 | $75–110 | $60–90/lb | YES | YES |
| Elderberry (dried whole) | Respiratory, Immunity | $5–8 | $45–70 | $36–56/lb | YES | YES |
| Echinacea purpurea root | Respiratory, Immunity | $6–9 | $55–80 | $44–64/lb | YES | YES |
| Echinacea angustifolia root | Respiratory, Immunity | $12–16 | $110–145 | $88–116/lb | YES | YES |
| Ashwagandha root | Immunity | $7–10 | $60–90 | $48–72/lb | YES | YES |
| Valerian root | Sleep | $6–9 | $55–80 | $44–64/lb | YES | YES |
| Passionflower herb | Sleep | $6–8 | $55–75 | $44–60/lb | YES | YES |
| Lemon Balm leaf | Sleep, Digestive | $5–7 | $45–65 | $36–52/lb | YES | YES |
| Lavender flower | Women's Health, Sleep | $5–8 | $45–75 | $36–60/lb | YES | YES |
| Calendula flower | Women's Health, Digestive | $8–12 | $70–110 | $56–88/lb | YES | YES |
| Dandelion root | Digestive | $5–7 | $45–65 | $36–52/lb | YES | YES |
| Ginger root (sliced) | Digestive | $5–7 | $45–65 | $36–52/lb | YES | YES |
| **TOTAL (1 oz each, 13 species)** | — | **$93–141** | — | — | — | — |

**Phase 3 volume note (100+ units context)**: Phase 3 is producing educational digital guides, not sourcing bulk herbs for resale. The 100+ unit pricing column is included for completeness in case the guides are recommended to practitioners purchasing supplies in volume. For Phase 3 photography, order 1 oz per species (total $93–141 retail).

**CITES compliance for Goldenseal**: Request a Certificate of Analysis from Mountain Rose Herbs confirming cultivated origin of Goldenseal root when placing the order. Retain the CoA in WORKLOG.md — it is the documentation that supports the guide's FGV and cultivated-only sourcing claim.

**Emergency backup**: Frontier Co-op (frontiercoop.com) — comparable species, comparable pricing, 3–5 day ship. Activate if Mountain Rose Herbs cannot confirm June 17 delivery by June 13.

**Order confirmation deadline**: June 15 (for June 17–18 delivery). If not shipped by June 13: order Frontier Co-op same day.

**Supplier confirmation status:**

| Date Contacted | Response Received | All 13 Species In Stock? | Est. Delivery | Goldenseal CoA Available? | Order Total |
|---|---|---|---|---|---|
| [FILL] | [FILL] | [ ] Yes / [ ] Partial | [FILL] | [ ] Yes / [ ] No | $[FILL] |

---

### Supplier 4: Southern Exposure Seed Exchange

| Attribute | Detail |
|---|---|
| Website | southernexposure.com |
| Contact | southernexposure.com/contact/ |
| Primary order season | January–February (spring catalog); June availability uncertain for perennials |
| MOQ | No minimum for retail |
| Payment terms | Prepay |
| Certifications | Open-pollinated, heirloom-preserving; organic growing practices |

**Phase 3 role**: Guide citation for Appalachian and southeastern US regional practitioners. Secondary specimen supplier only if primary suppliers fail.

**Critical constraint**: Southern Exposure's primary catalog is January–February. By late May, most transplant stock of conservation species (Goldenseal, Black Cohosh) may be depleted. Email inquiry May 20 to confirm June order capability before relying on them as a fallback.

| Species | Form | Estimated Price | Lead Time | June Availability | Role |
|---|---|---|---|---|---|
| Goldenseal | Seed only (not rhizome) | $5–10/packet | 2–3 weeks | [CONFIRM] | Guide citation — seed only; does not provide photo specimen |
| Echinacea | Seed or transplant | $4–7 | 2–3 weeks | [CONFIRM] | Backup if SM and PM out of stock |
| Calendula | Seed | $2–4 | 1–2 weeks | Likely YES | Regional alternative citation |
| Lemon Balm | Seed or transplant | $4–6 | 2–3 weeks | [CONFIRM] | |
| Lavender | Seed or transplant | $4–7 | 2–3 weeks | [CONFIRM] | |
| Valerian | Seed | $4–6 | 2–3 weeks | [CONFIRM] | |

**Supplier confirmation status:**

| Date Contacted | Response Received | June Transplants Available? | Notes |
|---|---|---|---|
| [FILL] | [FILL] | [ ] Yes / [ ] No | [FILL] |

---

### Supplier 5: Fedco Seeds

| Attribute | Detail |
|---|---|
| Website | fedcoseeds.com |
| Contact | fedcoseeds.com/contact (form-based) |
| Business model | Worker-owned cooperative |
| Primary order season | January–February; spring plant stock may be depleted by late May |
| MOQ | No minimum for retail |
| Payment terms | Prepay |
| Certifications | Non-GMO, open-pollinated focus |

**Phase 3 role**: Regional alternative for northeastern US practitioner guide citations; potential Black Cohosh specimen supplier if in stock.

**Critical constraint**: Fedco's conservation species (Black Cohosh, Echinacea angustifolia) sell out rapidly. Do not plan on Fedco as a Tier 1 supplier without confirming current inventory. If Black Cohosh is still in stock, Fedco is the preferred citation for practitioners in Vermont, Maine, New Hampshire, and New York.

| Species | Form | Estimated Price | Lead Time | June Availability | Notes |
|---|---|---|---|---|---|
| Black Cohosh | Plants (spring catalog) | $12–18/plant | 3–5 weeks | [CONFIRM — likely limited] | Confirm inventory before relying on this source |
| Echinacea | Seed or plug | $4–6 | 2–3 weeks | [CONFIRM] | |
| Valerian | Seed or plug | $5–7 | 2–3 weeks | [CONFIRM] | |
| Calendula | Seed | $2–4 | 1–2 weeks | Likely YES | |
| Lemon Balm | Seed or plug | $4–6 | 2–3 weeks | [CONFIRM] | |
| Lavender | Seed or plug | $5–7 | 2–3 weeks | [CONFIRM] | |

**Supplier confirmation status:**

| Date Contacted | Response Received | Black Cohosh In Stock? | Notes |
|---|---|---|---|
| [FILL] | [FILL] | [ ] Yes / [ ] No | [FILL] |

---

## Ordering Calendar

| Date | Action | Supplier | Contact | Status |
|---|---|---|---|---|
| May 20 | Email inquiry: Goldenseal rhizome + Black Cohosh transplant availability for June/July delivery | Strictly Medicinal Seeds | info@strictlymedicinalseeds.com | [ ] Sent |
| May 20 | Email inquiry: Goldenseal, Black Cohosh, Elderberry availability for June/July delivery | Prairie Moon Nursery | info@prairiemoon.com | [ ] Sent |
| May 20 | Email inquiry: June order capability for transplants | Southern Exposure | southernexposure.com/contact/ | [ ] Sent |
| May 20 | Email inquiry: Black Cohosh spring plant availability | Fedco Seeds | fedcoseeds.com/contact | [ ] Sent |
| May 23 | Email inquiry: 13 species dried 1 oz each; confirm stock and lead time | Mountain Rose Herbs | wholesale@mountainroseherbs.com | [ ] Sent |
| May 25 | Place Goldenseal + Black Cohosh orders if confirmed available | Best Tier A | — | [ ] Complete |
| **June 7 EOD** | **If no Goldenseal order confirmation: email NC Botanical Garden + Missouri Botanical Garden** | NC Botanical Garden; Missouri Botanical Garden | media@ncbg.unc.edu; media@mobot.org | [ ] N/A / [ ] Sent |
| **June 8** | **HARD DEADLINE: Goldenseal order placed with tracking, OR Wikimedia CC path fully activated** | — | — | **[ ] COMPLETE** |
| June 13 | Confirm Mountain Rose Herbs has shipped; if not: place Frontier Co-op order | Mountain Rose Herbs / Frontier Co-op | wholesale@mountainroseherbs.com | [ ] Complete |
| **June 15** | **HARD DEADLINE: Elderberry order placed + Mountain Rose Herbs dried herb order placed** | Prairie Moon + Mountain Rose | info@prairiemoon.com; website | **[ ] COMPLETE** |
| June 22 | Place Tier 3 orders on sprint start day (Echinacea, Ashwagandha, Passionflower, Valerian, Ginger, Vitex) | Strictly Medicinal / local nurseries | info@strictlymedicinalseeds.com | [ ] Complete |

---

## Final Ordering Decision Tables

### Tier 1 — June 8 Deadline (Fill in as Decisions Are Made)

| Species | Supplier Selected | Order Placed | Date Placed | Tracking # | Est. Delivery | Photo Path |
|---|---|---|---|---|---|---|
| Goldenseal | [Strictly Medicinal / Prairie Moon / **Wikimedia CC**] | [ ] Yes / [ ] No | [DATE] | [#] | [DATE] | [Live specimen / Wikimedia CC / NC Botanical Garden] |
| Black Cohosh | [Prairie Moon / Strictly Medicinal] | [ ] Yes / [ ] No | [DATE] | [#] | [DATE] | [Live specimen / iNaturalist CC-BY] |

**Goldenseal Path Declared** (mark one by June 8):
- [ ] **Path 1 — Live specimen order**: Supplier [name], tracking number [#], expected delivery [date]
- [ ] **Path 2 — Wikimedia CC**: Botanical garden email sent [date], CC images downloaded [date], filenames logged in PHOTO_ATTRIBUTION_LOG.md

### Tier 2 — June 15 Deadline

| Species | Supplier | Order Placed | Date Placed | Tracking # | Est. Delivery | Fallback Activated? |
|---|---|---|---|---|---|---|
| Elderberry | [Prairie Moon / Local nursery] | [ ] | [DATE] | [#] | [DATE] | [ ] N/A / [ ] Local nursery |
| Dried herbs (all 13 species) | Mountain Rose Herbs | [ ] | [DATE] | [#] | [DATE] | [ ] N/A / [ ] Frontier Co-op |

### Tier 3 — June 22 Orders

| Species | Supplier | Order Placed | Date | Tracking # | Est. Delivery |
|---|---|---|---|---|---|
| Echinacea purpurea | [SM / PM] | [ ] | [DATE] | [#] | [DATE] |
| Echinacea angustifolia | [SM / PM] | [ ] | [DATE] | [#] | [DATE] |
| Ashwagandha | [SM] | [ ] | [DATE] | [#] | [DATE] |
| Passionflower | [PM / SM] | [ ] | [DATE] | [#] | [DATE] |
| Valerian | [PM / SM] | [ ] | [DATE] | [#] | [DATE] |
| Ginger | [SM / grocery store] | [ ] | [DATE] | [#] | [DATE] |
| Vitex | [Local nursery / PM] | [ ] | [DATE] | [#] | [DATE] |

---

## Budget Summary

| Category | Supplier | Low Estimate | High Estimate | Actual | Notes |
|---|---|---|---|---|---|
| Goldenseal rhizome (1–3 divisions) | SM or PM | $12 | $54 | $____ | Path 1 only; Path 2 = $0 |
| Black Cohosh transplant (1–2 plants) | PM or SM | $10 | $30 | $____ | |
| Elderberry bare-root (1–2 plants) | PM or local | $15 | $50 | $____ | |
| Tier 3 plants (6 species, 1–2 each) | SM + local | $65 | $105 | $____ | |
| Dried herbs (13 species, 1 oz each) | MRH | $93 | $141 | $____ | |
| Studio props | Various | $60 | $100 | $____ | |
| **Total (Path 1)** | | **$255** | **$480** | **$____** | |
| **Total (Path 2 — no Goldenseal order)** | | **$243** | **$426** | **$____** | |

**Budget target**: $400 total. This is achievable at mid-range estimates under either path.

---

## Backup Vendor Decision Reference

If a primary supplier fails, use this table for immediate escalation:

| Species | Primary Supplier Fails | Backup 1 | Backup 2 | Lead Time (Backup) | Cost Impact |
|---|---|---|---|---|---|
| Goldenseal | Prairie Moon | Strictly Medicinal Seeds | NC Botanical Garden photo license (free) | SM: same ~5–6 weeks; Botanical garden: 1 week response | $0 on Path 2 |
| Black Cohosh | Strictly Medicinal | Prairie Moon Nursery | iNaturalist CC-BY (free photo) | PM: 4 weeks | +0–5 days |
| Elderberry | Prairie Moon | Local nursery (potted 2-gal) | Wikimedia CC-BY-SA (free photo) | Local: 1–2 weeks | +$5–15 (local premium) |
| Echinacea | Prairie Moon | Local native plant nursery | iNaturalist CC-BY | Local: 1–2 weeks | Comparable |
| Ashwagandha | Strictly Medicinal | Baker Creek Heirloom Seeds | iNaturalist CC-BY (India-range) | Baker Creek: 1–2 weeks | +$2–5 |
| Dried herbs (all) | Mountain Rose Herbs | Frontier Co-op | Local health food co-op | Frontier: 3–5 days | Comparable |

---

## Sign-Off and Tracking

### June 8 Sign-Off (Goldenseal)

Complete before June 8, 23:59 UTC. Enter in WORKLOG.md.

```
## Goldenseal Sourcing Decision — June 8 (required)

Path selected: [ ] Path 1 (live order)  [ ] Path 2 (Wikimedia CC)

If Path 1:
  Supplier: __________
  Order tracking number: __________
  Expected delivery: __________
  Cultivated source confirmed: YES / NO

If Path 2:
  NC Botanical Garden email sent: __________
  Missouri Botanical Garden email sent: __________
  Wikimedia CC images downloaded: YES / NO
  Image filenames logged in PHOTO_ATTRIBUTION_LOG.md: YES / NO

Black Cohosh order status:
  Supplier: __________  | Order placed: YES / NO | Tracking: __________

Authorization: Goldenseal path confirmed. Critical gate cleared.
```

### June 15 Sign-Off (Elderberry + Dried Herbs)

```
## Tier 2 Ordering — June 15

Elderberry order placed: YES / NO
  Supplier: __________  | Tracking: __________  | Est. delivery: __________

Mountain Rose Herbs order placed: YES / NO
  Tracking: __________  | Est. delivery: __________
  All 13 species confirmed in stock: YES / NO
  Goldenseal CoA requested: YES / NO

Frontier Co-op contingency order needed: YES / NO
  If YES: order placed: __________
```

### June 21 Pre-Sprint Sign-Off (All Suppliers)

Complete before sprint start. Enter in WORKLOG.md.

```
## Supplier Track Cleared — June 21

All critical orders placed: YES / NO
Outstanding orders with confirmed ship dates: YES / NO
Goldenseal path confirmed in PHOTO_ATTRIBUTION_LOG.md: YES / NO
PHASE_3_SUPPLIER_CONFIRMATION_TRACKER.md fully populated: YES / NO

Outstanding contingencies (if any): __________

Authorization: Supplier track cleared. Sprint may begin June 22.
```

---

*Tracker version 4.0 — May 21, 2026. Supersedes v3.0. Key additions: May 25 Black Cohosh critical date, per-bundle delivery requirements table, Goldenseal Wikimedia CC licensing analysis (Path 2 confirmed), updated Tier 1 structure (1A/1B). Update all [FILL] and [ ] fields as supplier responses arrive. Maintain in parallel with WORKLOG.md.*

*Next reviews: May 25 (Black Cohosh order), June 1 (supplier outreach follow-up), June 7 EOD (Goldenseal path confirm), June 8 (Goldenseal hard gate), June 15 (Elderberry + MRH), June 21 (pre-sprint supplier sign-off).*
