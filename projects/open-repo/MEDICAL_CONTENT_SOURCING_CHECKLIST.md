---
title: "Medical Content Sourcing Checklist — Offline Medical Reference Module"
project: open-repo
phase: "5.2 Wave 1"
status: "Wave 0 pre-work — initiate before June 1"
created: 2026-05-21
author: General Research Agent
depends_on: "PHASE_5.2_IMPLEMENTATION_ROADMAP.md"
priority: "CRITICAL PATH — longest lead time of any Phase 5.2 deliverable"
---

# Medical Content Sourcing Checklist

## Purpose and Scope

This checklist governs the sourcing, validation, and publication of medical content in the `MedicalReferenceArchiver` ZIM module. Medical content in an offline archive is different from all other Phase 5.2 content domains: errors in botanical taxonomy are embarrassing; errors in drug dosing or procedure protocols can directly cause patient harm in austere conditions where no correction is available.

The design philosophy of this module is established in `off-grid-living/08-medical-health.md`: this is knowledge for prepared individuals in austere environments, not a replacement for trained medical professionals. Every article in the module must reinforce this framing at every level — from the disclaimer template to the article structure to the sourcing policy.

This checklist is organized into five sections: authoritative source evaluation, data format and compatibility requirements, contraindication and interaction logic, librarian review process, and offline-first design requirements.

---

## Section 1: Authoritative Source Evaluation

### Required Sources (must be included before Wave 1 ships)

**Source 1: WHO Model Formulary for Adults (2008 edition, updated supplements)**

- URL: https://apps.who.int/iris/bitstream/handle/10665/44053/9789241547659_eng.pdf
- License: CC BY-NC-SA 3.0 — free for offline use in non-commercial humanitarian contexts; open-repo's mission qualifies
- Content: ~480 pages covering ~340 essential medicines with clinical pharmacology, indications, contraindications, dosing, adverse effects, and drug interactions
- Format: PDF — requires structured extraction to per-drug JSON; target fields are dosing tables and contraindication lists
- Why this source: WHO Model Formulary is the global standard reference for essential medicines, used by Doctors Without Borders, ICRC, and national health ministries worldwide. It is specifically designed for resource-limited settings.
- Verification step: Compare 5 randomly selected drugs against a current clinical reference (UpToDate or equivalent) to confirm no dosing guidance has changed significantly since 2008. Flag any discrepancies for medical reviewer.

**Source 2: WHO Essential Medicines List, 23rd edition (2023)**

- URL: https://www.who.int/groups/expert-committee-on-selection-and-use-of-essential-medicines/essential-medicines-lists
- License: CC BY-NC-SA — same as above
- Content: 502 essential medicines with international non-proprietary names (INNs), dosage forms, and strengths
- Format: PDF and structured web listing; a community-maintained CSV version exists on GitHub (search "WHO EML CSV 2023")
- Why this source: The EML defines the minimum medicine set for basic healthcare needs. It is the drug selection criterion for the Phase 5.2 formulary — only EML drugs are included in the initial release. This prevents scope creep into specialized oncology, transplant immunosuppression, or other domains requiring specialist monitoring.
- Verification step: Confirm the CSV version matches the current WHO EML PDF. Check version date on the CSV source.

**Source 3: ICRC First Aid in Armed Conflicts and Other Situations of Violence (2006 / updated 2025)**

- URL: https://shop.icrc.org/first-aid-in-armed-conflicts-and-other-situations-of-violence.html
- License: Free for humanitarian use; ICRC grants offline distribution rights for non-commercial educational use. Contact permission: icrc.org/en/contact
- Content: Trauma protocols, wound care, burn management, blast injury, drowning, hemorrhage control — the field medicine scenarios absent from clinical references designed for hospital settings
- Format: PDF; extraction required for structured procedure articles
- Why this source: The only authoritative source specifically written for austere-environment trauma care by a neutral humanitarian organization. Its protocols are validated by decades of field use in conflict zones — the highest-stress austere medical scenario.
- Action required: Email ICRC permissions team before June 1 to confirm offline redistribution rights are granted for open-source educational archives. Expected turnaround: 5–10 business days.

**Source 4: Wilderness Medical Society Practice Guidelines**

- URL: https://wms.org/magazine/1569/practice-guidelines
- License: Open access with attribution; WMS publishes guidelines for free distribution
- Content: Altitude sickness (AMS, HACE, HAPE), hypothermia, heat illness, envenomation, dental emergencies, wound closure, wilderness analgesia
- Format: Individual PDF papers, each covering one clinical guideline; structured extraction to JSON
- Why this source: WMS guidelines are the standard of care for wilderness and backcountry medicine, written by emergency physicians and wilderness medicine specialists. They cover the specific scenarios (remote environment, delayed evacuation, limited supplies) that characterize the open-repo use case.
- Verification step: Confirm the practice guideline edition year. WMS updates most guidelines on a 5-year cycle; check that no guideline used is older than 2020.

**Source 5: CDC Emergency Preparedness — Medical Countermeasures and First Aid**

- URL: https://emergency.cdc.gov/preparedness/
- License: Public domain (US government work)
- Content: Household emergency preparedness, water purification, wound care, improvised first aid, psychological first aid
- Format: HTML pages (downloadable via `wget --mirror` or similar); convert to Markdown for import pipeline
- Why this source: CDC materials are public domain, freely reproducible, and verified for factual accuracy by federal health authorities. They complement the WMS and ICRC sources by covering the public health and community-scale dimensions of austere medicine.

**Source 6: RxNorm Essential Medicines Subset (NLM)**

- URL: https://www.nlm.nih.gov/research/umls/rxnorm/
- License: Public domain (NLM work)
- Content: Standardized drug names (brand, generic, INNs), dosage forms, strengths, NDC codes, and drug interaction data from the NLM drug interaction database
- Format: SQL dump (~3 GB full); essential medicines subset is extractable as CSV (~10 MB) using the filter criteria: drugs present on the WHO Essential Medicines List
- Why this source: RxNorm provides the authoritative naming standard for drug records, ensuring that drug articles use consistent INNs and do not use brand names that may not be available in resource-limited settings. The interaction data supplements (but does not replace) the WHO Model Formulary interaction tables.
- Extraction note: Use the `RXNCONSO.RRF` and `RXNREL.RRF` tables; filter by `TTY = IN` (ingredient) and `SAB = MTHSPL` or `VANDF` for VA national formulary items aligned with WHO EML.

**Source 7: Médecins Sans Frontières (MSF) Clinical Guidelines**

- URL: https://medicalguidelines.msf.org/
- License: CC BY-NC-SA — MSF explicitly supports offline humanitarian use
- Content: Diagnostic and treatment protocols for 300+ conditions, written specifically for resource-limited settings; includes pediatric dosing, which is absent or abbreviated in several WHO sources
- Format: Web (structured HTML with machine-readable content); MSF publishes the full guidelines site as a downloadable offline package
- Why this source: MSF guidelines are the single most authoritative reference for resource-limited clinical practice. They are written by physicians working in exactly the austere conditions the open-repo ZIM is designed for. The pediatric dosing section is particularly valuable.

**Source 8: American Heart Association / European Resuscitation Council CPR Guidelines (2020/2021)**

- URL: https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines (AHA) / https://www.resus.org.uk/library/2021-resuscitation-guidelines (ERC)
- License: AHA guidelines are freely reproducible with attribution for educational purposes; ERC guidelines are open access
- Content: Adult and pediatric CPR compression ratios, AED use, choking protocol (Heimlich), drowning resuscitation
- Why this source: CPR guidelines are updated every 5 years based on systematic evidence reviews. The 2020/2021 guidelines are current. Including outdated CPR protocols (e.g., 15:2 ratio that was superseded) could cause harm; this source ensures the ZIM contains current evidence-based protocols.

---

## Section 2: Data Format Compatibility

### Content Type Schema (finalized in Wave 0)

Every medical article in the ZIM pipeline must conform to the `medical_article` content type with the following mandatory fields:

| Field | Type | Null permitted | Validation rule |
|---|---|---|---|
| `title` | string | No | Must include INN drug name or clinical condition name |
| `indication` | string | No | Plain language; must not require medical degree to parse |
| `contraindications` | list[string] | No | Minimum 1 entry; "none known" is permitted only with citation |
| `dosing_adult` | structured dict | No for drug monographs | Includes route, dose, frequency, maximum daily dose |
| `dosing_pediatric` | structured dict | No for drug monographs | Weight-based dosing (mg/kg); must include minimum age |
| `supply_quantity_1yr` | string | Yes | "X tablets/year for household of 4" format |
| `evacuation_criteria` | list[string] | No for procedure articles | "Evacuate immediately if..." format |
| `disclaimer` | string | No | Must reference the standard disclaimer template (cannot be customized per article) |
| `source_citation` | list[string] | No | Minimum 1 citation; must be from the approved source list above |
| `last_reviewed_date` | date | No | Date of most recent medical accuracy review |

Any record missing a required field must fail validation and must not be written to the ZIM. The importer raises `ValueError` with a description of the missing field, not a silent default.

### Supported Input Formats

| Format | Parser | Notes |
|---|---|---|
| Markdown (off-grid-living source files) | Python `markdown` library (existing) | Primary source format |
| PDF (WHO, ICRC, WMS guidelines) | `pdfplumber` (one-time extraction scripts) | Extraction runs once, output saved as JSON |
| CSV (WHO EML, RxNorm subset) | Python `csv` standard library | Clean imports; no parsing edge cases |
| HTML (CDC, MSF web pages) | Python `html.parser` standard library | Requires whitelist-based element extraction |
| SQL dump (RxNorm full) | SQLite or PostgreSQL; one-time extraction | Run extraction script; save output as CSV |

---

## Section 3: Contraindication and Interaction Logic

### Design Constraint: No Dynamic Lookup

ZIM is a static format. There is no JavaScript in Kiwix articles. Drug interaction lookup at read time is not possible. All interaction data must be pre-rendered.

### Practical Approach for Drug Interaction Tables

The WHO Model Formulary already solves this problem for the Phase 5.2 scope: it lists clinically significant interactions per drug in a structured "Drug Interactions" subsection. This is the source of truth for the Phase 5.2 ZIM.

Do not attempt to generate a full interaction matrix from RxNorm. For a 200-drug formulary, a full pairwise matrix is 40,000 entries — too large to pre-render per article without making each article enormous. Instead:

Each `drug_monograph` article includes:
1. A "Major Drug Interactions" section: lists the 3–10 most clinically significant interactions (those that can cause death or serious harm if missed) with brief mechanism and management note
2. A "Known Interaction Categories" section: lists drug classes to avoid (e.g., "Avoid concurrent use with MAO inhibitors" rather than listing every MAOI drug name)
3. A link to a single "Drug Interaction Reference" article that contains a pre-rendered cross-reference table of the 50 most commonly encountered interaction pairs in austere medicine

This approach serves the use case (a user consulting the archive offline to check a specific drug before administering it) without requiring computational infrastructure.

### Contraindication Severity Classification

All contraindications in the ZIM must be classified with a severity indicator:

| Class | Meaning | Display |
|---|---|---|
| ABSOLUTE | Must never be used in this condition regardless of alternatives | Red alert box |
| RELATIVE | Avoid if possible; use only when benefit outweighs risk | Orange alert box |
| CAUTION | Monitor closely if used; increased risk but not contraindicated | Yellow note |

The WHO Model Formulary uses equivalent classification language. Map their terminology to these classes during extraction.

---

## Section 4: Librarian / Medical Review Checklist

The following checklist is for the designated medical reviewer. It must be completed for Wave 1 Medical module to pass Deployment Gate 3.

### Reviewer Qualifications

The reviewer must have at least one of:
- Medical degree (MD, DO, MBBS) with clinical experience
- Pharmacist licensure (PharmD or equivalent) with clinical pharmacy background
- Wilderness medicine certification (FAWM, WMS Fellow) plus 5+ years field medicine experience
- Emergency medical technician (EMT-P or equivalent paramedic) with 10+ years experience

A nurse practitioner or physician assistant with emergency or wilderness medicine background is also acceptable.

### Pre-Review Materials (provided by developer)

Before the reviewer begins, provide:
1. The full list of drug categories and conditions included (derived from WHO EML + off-grid-living source)
2. 5 sample drug monograph articles in rendered HTML (as they will appear in Kiwix)
3. The disclaimer template text
4. The evacuation criteria article for 5 common emergency conditions
5. The "intended user" description: "prepared adult without formal medical training, operating in an environment with delayed or no access to professional medical care"

### Reviewer Checklist — Drug Monographs

For each drug monograph article, the reviewer confirms:

- [ ] Drug name is the WHO INN (not a brand name)
- [ ] Indication matches the WHO EML indication; no off-label uses without explicit labeling
- [ ] Adult dosing (route, dose, frequency, duration) matches WHO Model Formulary or MSF Clinical Guidelines
- [ ] Pediatric dosing includes minimum age and weight-based calculation
- [ ] Contraindications include pregnancy where relevant
- [ ] Major drug interactions are correct and clinically significant
- [ ] Severity classification (ABSOLUTE / RELATIVE / CAUTION) is appropriate
- [ ] Disclaimer text is present, prominent, and accurate
- [ ] Evacuation criteria are clinically appropriate (i.e., the listed signs are actual indications for evacuation)
- [ ] No dosing values have been modified from the cited source

### Reviewer Checklist — Procedure Articles

For each clinical procedure article, the reviewer confirms:

- [ ] Procedure steps are in the correct order
- [ ] Required equipment list is complete and realistic for austere conditions
- [ ] Contraindications for performing the procedure are listed
- [ ] Known complications and their management are described
- [ ] When to stop and evacuate is clearly stated

### Reviewer Checklist — Module-Level Review

- [ ] The disclaimer template accurately represents the scope and limitations of the archive
- [ ] No drug class is missing from the Essential Medicines formulary that would constitute a significant gap in austere medicine capability
- [ ] No article contains advice that would be harmful to a non-medical reader who follows it literally
- [ ] Pediatric dosing coverage is adequate (not just "consult a physician" for all pediatric cases)

---

## Section 5: Offline-First Design Requirements

### Article Structure for Austere-Environment Use

The ZIM will be consulted under stress, potentially in poor lighting, by someone who is not a medical professional and who needs a specific answer fast. Article design must reflect this reality.

**Required article structure for drug monographs**:
1. Drug name (INN, large heading)
2. One-sentence plain-language description of what it treats
3. Dosing quick-reference box (high contrast, large font CSS class `.dosing-qr`) — adult dose first, pediatric dose second
4. STOP BOX: absolute contraindications and red-flag interactions (colored alert box, always before full body text)
5. Full clinical information (indication detail, mechanism, adverse effects, full interaction list)
6. Supply planning note
7. Disclaimer (styled `<aside>` element, always last, but cannot be removed from the article)

**Required article structure for procedure articles**:
1. Procedure name (large heading)
2. One-sentence scope ("Use this procedure when...")
3. STOP BOX: contraindications — when NOT to perform this procedure
4. Equipment list (bullet list, specific quantities where relevant)
5. Steps (numbered, plain language, each step one action only)
6. Expected outcomes and failure signs
7. Evacuation criteria
8. Disclaimer

This structure ensures that a user who opens the article and reads only the top 25% (the most likely behavior under stress) sees the most critical information: the dose and what to avoid.

### Nopic Variant Considerations

Medical articles in the nopic ZIM variant must not lose clinical information when images are omitted. Any information conveyed by a diagram or image must also be present in adjacent text. This includes:
- Injection sites (describe in text: "Inject into the outer upper quadrant of the buttock, approximately 3 cm from the nearest bone prominence")
- Anatomical landmarks for wound closure
- Rash identification (describe morphology in text: "flat, non-raised, non-blanching petechiae")

Images are decorative aids, not primary information carriers in the medical module.

### Article Length and Searchability

Target article length: 500–1,500 words per article. Longer articles should be split into sub-articles linked by ZIM internal references (e.g., "Amoxicillin" links to "Penicillin Allergy Cross-Reactivity" rather than including that content inline).

All drug articles must include the following in the article metadata for Xapian search indexing:
- All major brand names known for the drug (so a user searching "Tylenol" finds the Paracetamol/Acetaminophen article)
- Common condition names the drug treats (so "tooth pain" finds the Ibuprofen and Paracetamol articles)
- Alternative spellings (particularly US vs. UK spelling: "acetaminophen" vs. "paracetamol")

This is implemented via the `tags` and `aliases` fields in the ZIM article metadata, not as visible body text.

---

## Pre-Publication Sign-Off

Before the `MedicalReferenceArchiver` module is included in any ZIM distributed beyond the development team, all of the following must be confirmed:

- [ ] Medical reviewer has signed off on all drug monographs and procedure articles (Deployment Gate 3)
- [ ] Disclaimer text has been reviewed by the project maintainer
- [ ] All source citations are present and traceable (no orphaned articles)
- [ ] `zimcheck` reports 0 errors on the medical domain ZIM
- [ ] At least one non-developer user has opened the ZIM in Kiwix and confirmed the dosing quick-reference boxes render correctly on a mobile screen
- [ ] The ICRC permission confirmation email has been received and archived in `docs/licensing/`

---

## Sources

- [WHO Model Formulary for Adults — WHO](https://apps.who.int/iris/bitstream/handle/10665/44053/9789241547659_eng.pdf)
- [WHO Essential Medicines List 23rd edition — WHO](https://www.who.int/groups/expert-committee-on-selection-and-use-of-essential-medicines/essential-medicines-lists)
- [ICRC First Aid in Armed Conflicts — ICRC](https://shop.icrc.org/first-aid-in-armed-conflicts-and-other-situations-of-violence.html)
- [Wilderness Medical Society Practice Guidelines — WMS](https://wms.org/magazine/1569/practice-guidelines)
- [CDC Emergency Preparedness — CDC](https://emergency.cdc.gov/preparedness/)
- [RxNorm — National Library of Medicine](https://www.nlm.nih.gov/research/umls/rxnorm/)
- [MSF Clinical Guidelines — Médecins Sans Frontières](https://medicalguidelines.msf.org/)
- [AHA CPR & ECC Guidelines 2020 — American Heart Association](https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines)
- [ERC Resuscitation Guidelines 2021 — European Resuscitation Council](https://www.resus.org.uk/library/2021-resuscitation-guidelines)
