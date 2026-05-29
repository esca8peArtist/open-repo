---
title: "Phase 5.2 Medical Dosing Databases — Content Sourcing & Platform Validation Checklist"
project: open-repo
phase: "5.2"
module: "Medical Reference (Priority 1)"
composite_score: 8.20
implementation_start: "June 1, 2026"
status: "pre-implementation validation — complete before June 1"
created: 2026-05-27
depends_on: "PHASE_5.2_MEDICAL_WATER_SEED_ROADMAP.md, MEDICAL_CONTENT_SOURCING_CHECKLIST.md"
---

# Phase 5.2 Medical Dosing Databases — Content Sourcing & Platform Validation Checklist

**Purpose**: This document is the June 1 morning startup guide for the Medical Reference module. Open this, work through it top-to-bottom, and you will have all content sourced before you write a single line of importer code.

**Prerequisites verified**: Phase 5.1 ZIM export production-stable. `libzim>=3.10.0` confirmed in `pyproject.toml`. XSS fix applied. `ZimExport` ORM class created.

---

## Tier Classification

**Tier 1 — Required (minimal cost, ship blocker)**: Sources that must be included before the module ships. All are open-access or public domain. No subscription fees, no institutional access required.

**Tier 2 — Recommended (institutional subscription or significant extraction effort)**: Sources that materially improve content depth and accuracy. Include if accessible; document gap if not.

**Tier 3 — Nice-to-have (cost-prohibitive or blocked by licensing)**: Sources that would improve the module but are not critical path. Note and defer to Phase 5.3.

---

## Tier 1: Required Sources

### T1-A: WHO Model Formulary for Adults (2008 + supplements)

- **URL**: https://apps.who.int/iris/bitstream/handle/10665/44053/9789241547659_eng.pdf
- **License**: CC BY-NC-SA 3.0 IGO — free for offline non-commercial humanitarian use; open-repo qualifies
- **Format**: PDF (~480 pages); requires one-time structured extraction to per-drug JSON
- **What to extract**: ~340 essential medicines — dosing tables, contraindication lists, drug interaction subsections, pediatric weight-based dosing where present
- **Rate limits**: No API; single PDF download; no throttle concerns
- **June 1 action**: Download PDF. Run `pdfplumber` extraction script. Save JSON output to `data/sources/who_model_formulary_2008.json`. Commit extraction script to `scripts/extractors/who_formulary_extractor.py`.
- **Validation**: Cross-check 5 randomly sampled drugs against current MSF Clinical Guidelines. Flag discrepancies for medical reviewer. Known gap: 2008 edition; some protocols may be updated. WHO supplement PDFs (2013, 2016, 2019 editions on the same page) address most gaps.

### T1-B: WHO Essential Medicines List, 23rd Edition (2023)

- **URL**: https://www.who.int/groups/expert-committee-on-selection-and-use-of-essential-medicines/essential-medicines-lists
- **License**: CC BY-NC-SA 3.0 IGO
- **Format**: PDF + community-maintained CSV (search GitHub for "WHO EML CSV 2023"; verify CSV date matches PDF)
- **What to extract**: 502 medicines — international non-proprietary names (INNs), dosage forms, strengths; use as the drug selection gate (only EML drugs included in initial release)
- **Rate limits**: No API; one-time CSV/PDF download
- **June 1 action**: Download CSV. Load into `data/sources/who_eml_2023.csv`. This CSV drives the drug inclusion/exclusion filter in `MedicalReferenceArchiver`.

### T1-C: MSF Clinical Guidelines (medicalguidelines.msf.org)

- **URL**: https://medicalguidelines.msf.org/
- **License**: CC BY-NC-SA — MSF explicitly supports offline humanitarian redistribution; download the full offline package from the site
- **Format**: Structured HTML (full offline package available as ZIP download from the site)
- **What to extract**: Diagnostic and treatment protocols for 300+ conditions; pediatric dosing (this is the primary pediatric dosing source); drug interaction tables; critical decision trees
- **Rate limits**: No API; ZIP archive download; no throttle
- **June 1 action**: Download offline package ZIP. Unzip to `data/sources/msf_guidelines/`. Parse HTML using `html.parser` into structured JSON. The MSF site's HTML is well-structured with `<div class="drug-box">` and `<div class="dosage-table">` elements that are straightforward to extract.
- **Why required**: MSF guidelines are written by physicians operating in exactly the austere conditions the ZIM targets. Pediatric dosing coverage here is significantly better than WHO Model Formulary.

### T1-D: Internal Source — off-grid-living/08-medical-health.md

- **URL**: `projects/off-grid-living/08-medical-health.md` (internal)
- **License**: Internal; no restrictions
- **Format**: Markdown (~1,500+ lines)
- **What to extract**: Condition sections, drug monographs, dosing tables, evacuation criteria, wilderness-specific scenarios (cold injury, altitude sickness, trauma triage)
- **June 1 action**: Copy to `data/sources/off_grid_medical.md`. This file is the primary source for field-specific content not well-covered by clinical references.

### T1-E: CDC Emergency Preparedness & First Aid

- **URL**: https://emergency.cdc.gov/preparedness/ and https://www.cdc.gov/niosh/topics/emres/
- **License**: Public domain (US government)
- **Format**: HTML pages
- **What to extract**: Wound care, improvised first aid, water purification for medical use, psychological first aid, mass casualty basic triage
- **Rate limits**: No API needed; `wget --mirror` or `requests` download; no throttle for reasonable crawl
- **June 1 action**: Mirror relevant CDC emergency pages to `data/sources/cdc_emergency/`. Respect robots.txt.

### T1-F: RxNorm Essential Medicines Subset (NLM)

- **URL**: https://www.nlm.nih.gov/research/umls/rxnorm/ (free registration at https://uts.nlm.nih.gov/uts/signup-login)
- **License**: Public domain (NLM/US government)
- **Format**: SQL dump (~3 GB full); essential medicines subset extractable as CSV (~10 MB) using WHO EML filter
- **What to extract**: Standardized INNs, drug class hierarchy, dosage form normalization, brand-name cross-reference; ensures ZIM uses INN names not brand names
- **Rate limits**: Bulk download; one-time extraction. NLM requires free registration but no OAuth/API key for bulk download.
- **June 1 action**: Register at NLM UTS (https://uts.nlm.nih.gov/uts/signup-login). Download `RxNorm_full_YYYYMMDD.zip`. Run extraction using `RXNCONSO.RRF` filtered by `TTY=IN` and `SAB=RXNORM`. Save as `data/sources/rxnorm_eml_subset.csv`.

---

## Tier 2: Recommended Sources

### T2-A: ICRC First Aid in Armed Conflicts (2006/2025 update)

- **URL**: https://shop.icrc.org/first-aid-in-armed-conflicts-and-other-situations-of-violence.html
- **License**: Free for humanitarian use; ICRC grants offline distribution rights for non-commercial educational use
- **Format**: PDF
- **What to extract**: Trauma protocols, wound care, burn management, blast injury, drowning, hemorrhage control
- **Action required before June 1**: Email icrc.org/en/contact to confirm offline redistribution rights. Expected turnaround: 5-10 business days. **Send this email by May 29 at the latest.** If no response by June 1, proceed with Tier 1 sources; add ICRC as a Phase 5.2.1 update.

### T2-B: Wilderness Medical Society Practice Guidelines

- **URL**: https://wms.org/magazine/1569/practice-guidelines
- **License**: Open access with attribution
- **Format**: Individual PDF papers per guideline
- **What to extract**: Altitude sickness (AMS/HACE/HAPE), hypothermia, heat illness, envenomation, dental emergencies, wound closure, wilderness analgesia
- **Action**: Download all available PDFs. WMS updates guidelines on 5-year cycles; verify none are older than 2020. If older than 2020, flag for medical reviewer.
- **Note**: WMS content is valuable specifically for high-altitude and backcountry scenarios underrepresented in WHO/MSF.

### T2-C: AHA/ERC CPR Guidelines (2020/2021)

- **URL**: https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines (AHA) and https://www.resus.org.uk/library/2021-resuscitation-guidelines (ERC)
- **License**: Freely reproducible with attribution for educational purposes (AHA); open access (ERC)
- **What to extract**: Adult/pediatric CPR compression ratios, AED protocol, choking/Heimlich, drowning resuscitation
- **Why recommended**: CPR guidelines are updated every 5 years. Outdated CPR protocol in the ZIM (e.g., 15:2 ratio) could cause harm. These are the 2020/2021 current-standard documents.

---

## Tier 3: Nice-to-Have (Cost-Prohibitive / Blocked)

### T3-A: AHFS Drug Information

- **Status**: BLOCKED — subscription-only; institutional hospital access required; no public API; not available for open redistribution
- **Alternative**: WHO Model Formulary + MSF Clinical Guidelines cover the clinical scope; AHFS depth is not needed for the EML-scoped formulary

### T3-B: Micromedex / UpToDate

- **Status**: BLOCKED — commercial subscription ($1,500-5,000+/year); strict terms prohibit redistribution in any format
- **Alternative**: WHO/MSF sources are specifically designed for the open-repo use case (resource-limited settings); Micromedex/UpToDate are designed for in-hospital specialist use

### T3-C: FDA MedWatch / EudraVigilance Adverse Events

- **Status**: Deferred — FDA MedWatch data (https://www.fda.gov/safety/medwatch) is public domain and downloadable; however, interpreting adverse event signals requires pharmacovigilance expertise to avoid alarming users with rare events. Defer to Phase 5.3 when medical reviewer relationship is established.

### T3-D: ClinicalTrials.gov API

- **URL**: https://clinicaltrials.gov/data-api/api
- **Rate limits**: ~50 requests/minute per IP; no authentication required
- **Status**: Not needed for Phase 5.2 — clinical trial data is appropriate for a systematic review tool, not a field medical reference. Include as a Tier 3 note; defer to Phase 5.3 if a "current treatment evidence" feature is requested.

### T3-E: PubMed Central (NCBI Entrez)

- **Rate limits**: 3 req/second without API key; 10 req/second with free API key (register at https://www.ncbi.nlm.nih.gov/account/); enhanced rates available by email to info@ncbi.nlm.nih.gov
- **Status**: Useful for verifying dosing evidence quality; not needed for Phase 5.2 content sourcing directly. Note for medical reviewer workflow if they want to cite primary literature.

---

## Scope Definition

**Selected scope for Phase 5.2 initial release**: Single-drug monographs for WHO EML drugs only. No drug interaction matrix (pre-render top 50 pairs only, per existing design). No adverse event summaries (Phase 5.3).

**Target article counts**:
- Drug monographs: 30-50 (WHO EML priority medicines for austere care: analgesics, antibiotics, antimalarials, antidiarrheals, rehydration, wound care, respiratory)
- Condition articles: 20-30 (trauma, infection, dehydration, respiratory, musculoskeletal, environmental emergencies)
- Procedure articles: 10-15 (wound care, CPR, splinting, airway management, improvised triage)
- Total: 60-95 articles in v1

**Out of scope for Phase 5.2**: Oncology, transplant immunosuppression, psychiatric medications, specialist diagnostics, genetic/lab testing interpretation.

---

## API Rate Limits Summary

| Source | Rate Limit | Auth Required | Bulk Download Available |
|---|---|---|---|
| WHO (PDF downloads) | None | No | Yes (direct PDF) |
| MSF Guidelines | None | No | Yes (ZIP package) |
| CDC | None (crawl respectfully) | No | Yes (wget mirror) |
| NLM RxNorm | None (bulk) | Free registration | Yes (full dump) |
| ClinicalTrials.gov API | ~50 req/min | No | Deferred (T3) |
| PubMed/NCBI Entrez | 3 req/sec (free); 10 req/sec (API key) | Optional free API key | FTP bulk available |
| ICRC | No API; PDF download | Permission email | Yes (once permission granted) |

---

## Licensing Summary

| Source | License | Commercial Use | Offline Redistribution | Attribution Required |
|---|---|---|---|---|
| WHO Model Formulary | CC BY-NC-SA 3.0 IGO | No | Yes (non-commercial) | Yes |
| WHO EML | CC BY-NC-SA 3.0 IGO | No | Yes (non-commercial) | Yes |
| MSF Clinical Guidelines | CC BY-NC-SA | No | Yes (humanitarian) | Yes |
| CDC materials | Public domain (US) | Yes | Yes | No (good practice) |
| RxNorm / NLM | Public domain (US) | Yes | Yes | No (good practice) |
| ICRC First Aid | ICRC humanitarian use | No | Yes (with permission) | Yes |
| WMS Guidelines | Open access with attribution | Educational use | Yes | Yes |
| off-grid-living internal | Internal | N/A | N/A | N/A |

**Key constraint**: CC BY-NC-SA sources (WHO, MSF) can be redistributed in the ZIM only for non-commercial purposes. The open-repo project must confirm its mission statement is unambiguously non-commercial before publication. Community contributions for profit (e.g., paid support subscriptions) must not be bundled with the ZIM that includes WHO/MSF content.

---

## Medical Content Risk Assessment

### Accuracy Liability

**Risk level: HIGH**. Incorrect dosing values in an offline archive consulted in an austere environment (no internet, no pharmacist) can cause direct patient harm. This is the highest-risk content domain in the entire Phase 5.2 roadmap.

**Mitigation**:
1. All dosing values must be transcribed verbatim from cited sources — no rounding, no interpolation, no paraphrasing of dose quantities
2. Two-pass validation: developer cross-check during authoring; designated medical reviewer cross-check before publication gate
3. Disclaimer present on every condition and drug monograph article: "This reference is for prepared individuals in austere environments as a last resort. Consult a trained medical professional whenever one is available."
4. Evacuation criteria included in every article: when the condition exceeds self-care capability
5. Source citation field is non-nullable: no article ships without a traceable source for every dosing value

### Attribution Requirements

Medical content requires peer-review-grade attribution. Every drug monograph must cite:
- Source document name, edition year, and section number
- Medical reviewer name and qualification (MD, PharmD, FAWM, or equivalent)
- Date of last medical accuracy review

Articles that have not completed medical accuracy review must carry a visible "DRAFT — UNREVIEWED" banner and must not be included in a production ZIM release.

### Update Cadence

| Source | Update frequency | Review cadence for ZIM |
|---|---|---|
| WHO Essential Medicines List | Every 2 years (odd years) | Update ZIM on each WHO EML edition |
| WHO Model Formulary | Supplemented periodically | Check for new supplements annually |
| MSF Clinical Guidelines | Continuous (web); major versions periodically | Annual review of changed protocols |
| WMS Practice Guidelines | 5-year cycle | Review at each WMS update cycle |
| CPR Guidelines (AHA/ERC) | 5-year cycle (next due 2025/2026) | Check for 2025 AHA update before publication |
| CDC materials | Ad hoc | Annual review |

**AHA 2025 CPR update**: AHA publishes updated CPR guidelines approximately every 5 years. The 2020 guidelines are current; a 2025 update may be imminent. Check https://cpr.heart.org before finalizing CPR procedure articles.

---

## June 1 Morning Startup Sequence

1. Confirm Phase 5.1 is production-stable (48-hour zero-error window complete)
2. Create branch: `git checkout -b feature/phase-5.2-medical`
3. Create directories: `mkdir -p data/sources/medical/` and `app/services/importers/`
4. Download WHO Model Formulary PDF (T1-A) — save to `data/sources/medical/who_model_formulary_2008.pdf`
5. Download WHO EML CSV (T1-B) — save to `data/sources/medical/who_eml_2023.csv`
6. Download MSF Guidelines ZIP (T1-C) — unzip to `data/sources/medical/msf_guidelines/`
7. Copy `projects/off-grid-living/08-medical-health.md` to `data/sources/medical/off_grid_medical.md`
8. Register at NLM UTS for RxNorm access (T1-F) — takes ~24 hours for email confirmation
9. Verify ICRC permission email has been sent (should be sent May 29)
10. Begin content schema design — finalize 3 article type field definitions (condition, drug monograph, procedure)
