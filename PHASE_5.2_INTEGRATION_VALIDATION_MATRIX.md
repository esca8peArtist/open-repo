---
title: "Phase 5.2 Integration Validation Matrix — Medical, Water, Seed"
project: open-repo
phase: "5.2"
document_type: integration-validation-matrix
status: pre-implementation (use before each module's Wave 1 code begins)
created: 2026-05-27
target_start: "June 1, 2026"
depends_on: "PHASE_5.1_POST_MERGE_DEPLOYMENT_CHECKLIST.md, PHASE_5.2_MEDICAL_WATER_SEED_ROADMAP.md"
candidates:
  - "Medical Reference (Score 8.20)"
  - "Water Systems (Score 7.90)"
  - "Seed Preservation (Score 7.80)"
---

# Phase 5.2 Integration Validation Matrix

**Purpose**: Runnable per-candidate integration checklist covering four validation gates — data format compatibility, media embedding, interactive components, and performance — for the three Phase 5.2 modules (Medical, Water, Seed). Use this document before beginning Wave 1 code for each module and again at ZIM integration test time.

**How to use**: Work through each candidate section top to bottom. Each item is a discrete test with a binary PASS / FAIL outcome. Any FAIL triggers a fallback path described at the bottom of each section. Do not proceed to the next gate until all items in the current gate pass.

**Constraints inherited from Phase 5.1 that every item below must satisfy**:
- ZIM articles are static HTML only — no JavaScript, no live API calls at read time
- All CSS must be inline `<style>` tags; no external stylesheets
- Images: base64-encoded in "all" variant, omitted in "nopic" variant
- Platform: Raspberry Pi 5, aarch64, Python 3.11.2, 4–8 GB RAM
- ZIM writer: `ZimWriter.add_article(path, content, article_type)` → `create_zim()` → `ZimWriteResult`
- Full-text search: Xapian embedded, indexes all visible and invisible body text
- Offline constraint: zero `http://` or `https://` in `src` or `href` attributes of any article

---

## Gate Definitions

**Gate 1 — Data Format Compatibility**: Source data (CSV, JSON, Markdown) can be parsed and mapped to the module's article schema without data loss or field truncation. All required metadata fields are non-null for every generated article.

**Gate 2 — Media Embedding**: All images and diagrams required for the module are available in a ZIM-compatible format (base64-PNG, inline SVG, or ASCII art), render correctly in Kiwix Android (WebView) and kiwix-serve, and stay within the 200KB-per-article size limit.

**Gate 3 — Interactive Component Support**: Any interactive element (search index, data table, category navigation, calculator output) is represented as static HTML that fully preserves the information value. No JavaScript is required for any feature to work.

**Gate 4 — Performance Baselines**: ZIM export completes within time and size bounds on the Raspberry Pi 5 deployment target. Search returns relevant results. Articles render in under 2 seconds in Kiwix.

---

## Candidate 1: Medical Reference (Score 8.20)

### Gate 1 — Data Format Compatibility

**Source formats**: Markdown (off-grid-living 08-medical-health.md), PDF (WHO EML, ICRC First Aid, WMS guidelines), CSV/JSON (RxNorm, WHO EML structured export), plain text (Wilderness Medical Society).

- [ ] **Markdown parser** renders `off-grid-living/08-medical-health.md` section headers correctly. Each `##` section maps to exactly one article (`condition`, `drug_monograph`, or `medical_procedure`). Verify with: `python3 -c "import re; data=open('projects/off-grid-living/08-medical-health.md').read(); sections=[m.group() for m in re.finditer(r'^## .+', data, re.M)]; print(len(sections), 'sections')"` — expect 40+ sections.

- [ ] **WHO EML structured data** (CSV or structured PDF extraction) maps to `drug_monograph` article fields. Required fields that must be non-null: `drug_name`, `indication_class`, `adult_dose`. Verify by importing one drug (e.g., Amoxicillin) and asserting all three fields are populated.

- [ ] **RxNorm CSV download** parses without encoding errors. Test: `python3 -c "import csv; rows=list(csv.DictReader(open('data/rxnorm.csv', encoding='utf-8-sig'))); print(rows[0].keys())"` — all expected column names present.

- [ ] **Dosing format validation**: Every `adult_dose` value in drug monographs is a non-empty string. Run the importer with a small sample (10 drugs) and assert no null or empty `adult_dose` fields. A null dosing field is a data integrity failure, not a missing-data warning.

- [ ] **Source citation field is non-null on every article**. Every article type (condition, drug_monograph, procedure) must have `source_citation` populated. Articles without source citations must be rejected by the importer and logged, not silently included with a null citation.

- [ ] **Article count gate**: Importer produces at least 60 articles from the source corpus: ≥20 condition articles, ≥30 drug monograph articles, ≥10 procedure articles. If count falls below 60, identify the parser gap before proceeding to Gate 2.

**Gate 1 result**: PASS if all six items above are checked. Any unchecked item is a Gate 1 FAIL — see Fallback Path 1.

### Gate 2 — Media Embedding

Medical content in the nopic variant requires no images. The all variant targets embedding small anatomical and procedural diagrams where they exist in public-domain sources.

- [ ] **Nopic variant completeness check**: Every article carries all essential clinical information in text alone. Verify by generating a test nopic ZIM and opening it in Kiwix with images disabled. Confirm that drug dosing, contraindications, evacuation criteria, and procedure steps are fully readable without images.

- [ ] **Disclaimer rendering**: All condition and drug monograph articles include the liability disclaimer at the top, before any treatment content. Verify by selecting 5 random articles from the test ZIM and confirming the disclaimer is the first element in the article body.

- [ ] **Danger box CSS renders in Kiwix Android WebView**: The `.danger-box` alert style (red border, light red background, used for contraindications and evacuation criteria) renders correctly in the Kiwix Android app. Test by generating a single medical article with a danger box, loading it in Kiwix Android, and confirming the visual distinction is present. This must be tested on the actual Kiwix Android app, not just kiwix-serve.

- [ ] **Article size gate (all variant)**: The largest anticipated article (complex drug monograph with interaction table + 2 procedure diagrams) stays below 200KB uncompressed. Test with: `python3 -c "content = open('test_article.html').read(); print(len(content.encode('utf-8')), 'bytes')"` — must be under 200,000.

- [ ] **No external URLs in HTML content**: Run `grep -r 'src="http\|href="http' test_medical_articles/` — expected zero matches. This test must pass for every generated article before the ZIM is built.

**Gate 2 result**: PASS if all five items above are checked. Any unchecked item is a Gate 2 FAIL — see Fallback Path 2.

### Gate 3 — Interactive Component Support

Medical requires drug category navigation, alias search, and procedure cross-referencing. All must be static HTML.

- [ ] **Drug class category index articles**: At least 5 index articles exist (Antibiotics, Analgesics, Antiparasitics, Oral Rehydration, First Aid Drugs), each listing and linking to all drug monographs in that class. Verify by opening the "Antibiotics" index article in the test ZIM and confirming all antibiotic drug monograph links resolve.

- [ ] **Condition-to-drug cross-links**: Every condition article links to at least one drug monograph article. And every drug monograph article links back to at least one condition article. These are standard ZIM internal links (`<a href="A/medicine/drug/amoxicillin">`) — verify no links produce 404 in Kiwix.

- [ ] **Search alias system**: Brand name aliases (e.g., "Tylenol" → Paracetamol, "Advil" → Ibuprofen) are embedded in article body text or in a `<meta name="keywords">` tag. Test: in Kiwix full-text search, enter "Tylenol" — the Paracetamol article must appear on the first page of results.

- [ ] **Procedure step ordering**: Procedure articles render numbered steps in order. Verify by opening 3 procedure articles and confirming steps are rendered as `<ol>` elements with steps in sequence. No unordered steps in procedure articles.

- [ ] **Evacuation criteria prominence**: Evacuation criteria text is visually distinct from treatment steps (uses `.danger-box` or bold header). Open 5 condition articles and confirm evacuation criteria are not buried in body text.

**Gate 3 result**: PASS if all five items above are checked. Any unchecked item is a Gate 3 FAIL — see Fallback Path 3.

### Gate 4 — Performance Baselines

Target: Raspberry Pi 5 (aarch64, Python 3.11.2, 4 GB RAM usable).

- [ ] **ZIM export time**: Generate a full medical ZIM (200+ articles) on the Pi 5. Expected: under 3 minutes. Command: `time uv run python3 -m app.services.export.export_cli --domain medicine --flavour nopic`. If export takes over 5 minutes, investigate libzim Creator thread usage — the Pi 5 at thermal ceiling throttles; exports should be scheduled at 02:00 UTC.

- [ ] **ZIM file size**: The generated `open-repo_en_medicine_YYYY-MM.zim` (nopic variant, 200+ articles) is under 50 MB. Medical text content for 200 articles is expected to be 5–15 MB before compression. If file exceeds 50 MB, check for accidental inclusion of large binary content.

- [ ] **Kiwix article render time**: Open the most complex drug monograph article (e.g., a multi-drug interaction table with 3 treatment alternatives) in Kiwix running against kiwix-serve on the Pi 5. Confirm article renders in under 2 seconds. Measure with `curl -o /dev/null -s -w '%{time_total}' http://127.0.0.1:8080/article/...` — expect under 2.0 seconds.

- [ ] **Search response time**: In Kiwix, search "amoxicillin" — result appears in under 1 second. Xapian search on the Pi 5 is fast; if search takes over 3 seconds, the Xapian index may not have been built correctly during ZIM generation.

- [ ] **zimcheck passes**: `zimcheck open-repo_en_medicine_YYYY-MM.zim` exits 0. Any warning is a publication blocker. Common zimcheck failure modes: illustration dimensions wrong (must be 48x48 PNG), description field over 80 characters, `name` field contains uppercase letters or spaces.

**Gate 4 result**: PASS if all five items above are checked.

### Medical Fallback Paths

**Fallback Path 1 (Gate 1 FAIL — data format incompatibility)**:
- If Markdown parser produces fewer than 60 articles: expand the parser regex to capture subsections (`###` level headers). If the off-grid-living source document lacks sufficient structured content, supplement with ICRC First Aid PDF extraction (manual structured JSON input from PDF) before retrying.
- If WHO EML structured data cannot be downloaded (API unavailable): use the PDF table extraction fallback — convert the WHO EML PDF table to CSV manually for the top 50 most critical drugs. This is a 3-4 hour manual task.
- If RxNorm CSV has encoding errors: try `encoding='latin-1'` fallback. If that fails, use the WHO EML drug list as the sole drug source (narrower coverage, still adequate for austere environment use).

**Fallback Path 2 (Gate 2 FAIL — media embedding)**:
- If danger box CSS does not render in Kiwix Android: replace CSS border/background with pure HTML `<blockquote>` elements with `⚠ WARNING:` prefix text. This is less visually distinctive but universally supported.
- If article size exceeds 200KB: move interaction tables to separate linked articles ("see Drug Interactions for Amoxicillin"). This reduces main article size at the cost of one extra navigation step.

**Fallback Path 3 (Gate 3 FAIL — interactive components)**:
- If brand name aliases do not appear in Kiwix search results: add aliases to the article `<title>` tag as a comma-separated suffix: "Paracetamol (Tylenol, Acetaminophen)". This is guaranteed to be indexed by Xapian.
- If internal links produce 404 in Kiwix: verify that all article path slugs are lowercase, hyphen-separated, and use the `A/` namespace prefix. Missing `A/` prefix is the most common cause of broken ZIM internal links.

**Fallback Path 4 (Gate 4 FAIL — performance)**:
- If ZIM export exceeds 5 minutes on Pi 5: schedule export at 02:00 UTC and increase Pi 5 cooling. The Pi 5 at 87°C throttles to ~50% CPU speed. With active cooling, thermal throttle does not engage.
- If ZIM file size exceeds 50 MB: check for large base64-encoded images accidentally included in nopic variant. The nopic path in `ZimWriter.add_article()` must strip `<img>` tags before writing to the ZIM.

---

## Candidate 2: Water Systems (Score 7.90)

### Gate 1 — Data Format Compatibility

**Source formats**: PDF (WHO Drinking Water Quality Guidelines, USDA rural water guides), HTML (CDC Water Treatment), Markdown (off-grid-living 03-water.md, systems-resilience 01-water.md), CSV (USGS water quality data, optional).

- [ ] **WHO DWQG PDF extraction** yields the key chemical quantity tables (chlorination rates, turbidity thresholds, nitrate limits) as structured data. Test: extract Table 1 (chemical quality guideline values) and verify at least 10 chemical parameters are captured with their guideline values and units.

- [ ] **CDC Water Treatment HTML parse** extracts chlorination rate tables. Verify: boiling time at sea level (1 minute) and at altitude over 2,000 meters (3 minutes) are correctly captured as distinct records. These specific values appear in the CDC guidance and are the most commonly referenced.

- [ ] **off-grid-living 03-water.md sections** map to `water_procedure`, `sizing_guide`, or `system_selection` article types. Run the importer and confirm at least 40 articles are generated: ≥15 procedures, ≥10 sizing guides, ≥5 system selection guides, ≥10 general water knowledge articles.

- [ ] **Chemical quantity units are consistent**: All chlorination dose values use the same unit system within the ZIM (prefer mg/L throughout). If WHO data uses mg/L and CDC data uses ppm, normalize to mg/L at import time (1 ppm ≈ 1 mg/L for dilute aqueous solutions). Log every unit conversion explicitly.

- [ ] **Source citation non-null on every article**: Same requirement as Medical. Every water procedure and sizing guide article must have `source_citation` populated. Reject articles with null citations.

- [ ] **`WaterSizingCalculator` output validation**: Run the sizing calculator for all four household sizes (individual 1-person, family 4-person, community 25-person, community 100-person) and all four source types (well, surface, rainwater, piped). Assert that all 16 output combinations produce non-zero `daily_requirement_liters` and `storage_recommendation_liters` values. Any zero output is a calculator bug.

**Gate 1 result**: PASS if all six items are checked.

### Gate 2 — Media Embedding

Water systems has the most complex multimedia requirement of the three Phase 5.2 modules — specifically, pump construction schematics and well cross-sections.

- [ ] **SVG schematic source validation**: Locate at least 3 public-domain SVG files for core water system schematics:
  - Hand pump cross-section (Simple Pump or equivalent design)
  - Pitcher pump assembly (PVC design, basic construction)
  - Sand filter cross-section (slow sand filter or biosand filter)
  
  Acceptable sources: WHO technical documentation, Practica Foundation engineering drawings (open-access), FAO AQUASTAT technical annexes, Wikimedia Commons. Verify license before inclusion. Confirm at least one acceptable source per schematic.

- [ ] **SVG renders in Kiwix Android**: Embed one SVG (the simplest of the three — pitcher pump) inline in a test article HTML. Open the test ZIM in Kiwix Android and confirm the SVG is visible and correctly proportioned. Test specifically for: `currentColor` CSS fill (may not render — replace with explicit hex colors), external `href` references (strip or embed), and `<use>` elements with external symbol definitions (convert to inline path elements).

- [ ] **SVG renders in kiwix-serve**: Repeat the above test against kiwix-serve on the Pi 5 via a browser. Kiwix-serve renders through a standard browser WebView; SVG support is broader here than in Kiwix Android.

- [ ] **PNG fallback readiness**: If the SVG rendering test above fails in Kiwix Android, export the three schematics as PNG at 800px width and base64-encode them. Confirm the base64-encoded PNG for the largest schematic is under 150KB. The PNG fallback is the reliable path; SVG is the preferred path.

- [ ] **Sizing table HTML rendering**: The `WaterSizingCalculator` output renders as a correctly formatted `<table>` element in Kiwix. Confirm column headers, row labels, and cell values are all visible. Test with the community-100 sizing scenario (the most data-dense output).

- [ ] **No external URLs in any article**: Same as Medical. `grep -r 'src="http\|href="http' test_water_articles/` — expected zero matches.

**Gate 2 result**: PASS if all six items are checked.

### Gate 3 — Interactive Component Support

Water requires sizing calculation navigation, water source type filtering, and chemical quantity quick-reference.

- [ ] **System type index articles**: At least 4 index articles exist (Well Systems, Surface Water Treatment, Rainwater Harvesting, Piped Water Emergency Treatment), each linking to all relevant procedure articles. Verify links resolve in Kiwix.

- [ ] **Household size navigation**: The sizing guide index article groups sizing guides by household size (Individual, Family-4, Community-25, Community-100). A user can navigate to their household size and find all relevant sizing guides without searching. Verify this path in the test ZIM.

- [ ] **Chemical quantity quick-reference**: A dedicated "Water Treatment Quick Reference" article lists chlorine doses, boiling times, and iodine doses in a single scannable table. This article must be findable by searching "chlorine dose" or "boiling time" in Kiwix. Confirm search returns it.

- [ ] **Cross-links to Medical module (if Medical is deployed first)**: If the Medical ZIM is deployed before Water, water quality condition articles (diarrheal disease, cholera risk, dysentery) should link to relevant medical condition articles. If Water deploys before Medical, these links are placeholders. Verify the link handling does not produce 404 errors in the current deployment state — use conditional linking logic in the importer.

- [ ] **Schematic article accessibility**: Each schematic is a full article (not just an embedded image in another article). The hand pump schematic article has a title, description, materials list, and step-by-step assembly notes alongside the SVG. A user searching "hand pump construction" finds this article. Confirm in Kiwix search.

**Gate 3 result**: PASS if all five items are checked.

### Gate 4 — Performance Baselines

- [ ] **ZIM export time**: Generate a full water ZIM (150+ articles, 3 embedded schematics) on the Pi 5. Expected: under 3 minutes. If SVG schematics are base64-encoded PNG (fallback path), add 30 seconds for encoding overhead — still acceptable.

- [ ] **ZIM file size**: `open-repo_en_water_YYYY-MM.zim` (nopic variant, no embedded schematics) under 10 MB. All variant with 3 embedded PNG schematics: under 20 MB. If file exceeds 20 MB, the base64-encoded images are too large — reduce PNG width to 640px or use ASCII art fallback.

- [ ] **Kiwix article render time**: Open the community-100 sizing guide (most complex HTML table) in Kiwix via kiwix-serve. Confirm render under 2 seconds.

- [ ] **Sizing calculator article count**: Every sizing scenario has a corresponding article. Verify `result.article_count` accounts for: 15+ procedures + 10+ sizing guides + 5+ system selection + 10+ general water + 4 index articles = minimum 44 articles total. Missing article types indicate importer gaps.

- [ ] **zimcheck passes**: `zimcheck open-repo_en_water_YYYY-MM.zim` exits 0.

**Gate 4 result**: PASS if all five items are checked.

### Water Fallback Paths

**Fallback Path 1 (Gate 1 FAIL — WHO PDF extraction fails)**:
- Manual structured JSON input: create a `data/who_dwqg_chemical_table.json` file with key chemical guideline values. This is a 1-2 hour manual task covering the 20 most critical parameters (coliform, turbidity, nitrate, chlorine, fluoride, arsenic, lead, E.coli).
- If CDC HTML structure changes (bot-blocking or HTML layout change): use the CDC's published PDF guide as fallback. CDC Water Treatment PDF is available at no cost.

**Fallback Path 2 (Gate 2 FAIL — SVG does not render in Kiwix Android)**:
- Immediately switch to PNG fallback. Export all three schematics as 800px-wide PNG, base64-encode, and embed in articles. Add 2–3 hours to implementation timeline.
- If PNG also causes render issues: fall back to ASCII art schematics with text descriptions. ASCII art for a pitcher pump cross-section can be done in approximately 30 lines of text and is guaranteed to render in any Kiwix environment.

**Fallback Path 3 (Gate 3 FAIL — cross-links to Medical produce 404)**:
- Use conditional linking: check if the Medical ZIM is deployed before generating water links. If Medical is not deployed, omit the cross-links and add a note: "(See medical reference for treatment of waterborne illness)". This avoids dead links without losing the information value.

---

## Candidate 3: Seed Preservation (Score 7.80)

### Gate 1 — Data Format Compatibility

**Source formats**: CSV (GRIN species data, USDA PLANTS database — large files), Markdown (seedwarden project documents, off-grid-living 04-food-production.md, systems-resilience midwest/calendar.md), XML (GRIN accession data, alternative to CSV).

- [ ] **GRIN CSV download and parse**: The GRIN bulk data download is large (multiple CSV files, 500+ MB total before filtering). Verify the download completes and that the species viability table (`viability.txt` or equivalent file) can be parsed. Filter to food-producing and medicinal species for US zones 3–8 — target: 500+ species after filtering.

- [ ] **USDA PLANTS CSV parse**: The USDA PLANTS complete species list CSV is approximately 44,000 species. Filter to species present in GRIN viability data. Verify the `Symbol`, `Scientific_Name`, `Common_Name`, and `National_Wetland_Indicator_Status` columns are accessible. The USDA symbol (`ALVI2` for Allium vineale, etc.) is the join key between USDA PLANTS and GRIN data.

- [ ] **seedwarden Markdown extraction**: Parse `projects/seedwarden/seed-saving-field-manual.md` and extract: seed saving procedures (each `##` or `###` section), viability testing protocols, and storage specifications. Confirm at least 10 discrete procedure articles can be extracted.

- [ ] **GRIN viability data join**: Join GRIN viability records to USDA PLANTS records by USDA symbol or Latin binomial. Verify that at least 200 species have matched viability data from GRIN. If fewer than 200 match, inspect the join key — common causes are spelling differences in Latin binomials (var./subsp. notations differ between databases).

- [ ] **`SeedViabilityCalculator` validation**: For 10 known species (e.g., tomato viability ~4 years, carrot ~3 years, onion ~1–2 years), verify the calculator produces output consistent with GRIN reference values. Assert: `calculate_viability(species="Solanum lycopersicum") == 4` (years, approximate). Tolerance: ±1 year.

- [ ] **Article count gate**: Importer produces at least 215 articles: ≥200 species cards + ≥5 viability test procedures + ≥5 regional growing calendars (USDA zones 3–8) + ≥5 category index articles. Missing categories must be investigated before proceeding to Gate 2.

**Gate 1 result**: PASS if all six items are checked.

### Gate 2 — Media Embedding

Seed module is the cleanest multimedia scenario of the three candidates — species cards do not require images for core utility. The primary media element is the HTML germination calendar grid.

- [ ] **Germination calendar HTML table renders**: The `planting_calendar` article renders as an HTML `<table>` with months as column headers and species as row labels. In Kiwix, confirm: (1) table scrolls horizontally if there are 12+ month columns, (2) cell colors (if used for season indication) render without external CSS, (3) table is readable at standard Kiwix zoom level.

- [ ] **Viability projection table renders**: The `SeedViabilityCalculator` output table (years of storage vs. expected germination rate %) renders correctly in Kiwix for a 10-year projection. Confirm percentages in cells are legible.

- [ ] **Species dual-name title format consistency**: Every species article title uses the format "Common Name — Genus species" (em dash, not hyphen). Verify with: `python3 -c "articles = ...; bad = [a for a in articles if ' — ' not in a['title']]; print(len(bad), 'articles with wrong title format')"` — expect 0 bad titles.

- [ ] **Nopic variant completeness**: Every species card in the nopic variant includes all essential information (common name, growing zones, seed saving method, isolation distance, storage specifications, viability years) without relying on images. Verify by opening 10 random species cards in a nopic test ZIM.

- [ ] **Index article navigation**: The "Seed Viability — Long-Term Storage (5+ years)" index article lists all species with viability ≥5 years and links to their species card articles. Verify all links resolve.

**Gate 2 result**: PASS if all five items are checked.

### Gate 3 — Interactive Component Support

Seed module's primary interactive requirement is the category index system, since ZIM full-text search cannot filter by structured field values.

- [ ] **Growing zone index articles**: One index article per USDA hardiness zone covered (target: zones 3–8, 6 articles). Each lists all species recommended for that zone. A user navigates to "Zone 5 — Recommended Species" and finds a browsable list with links. Verify all 6 zone index articles exist and their links resolve.

- [ ] **Crop category index articles**: At least 5 category index articles (Root Vegetables, Leafy Greens, Legumes, Alliums, Fruiting Crops). Each links to all species in that category. Verify a user can find "all legumes suitable for Zone 5" by navigating to "Legumes" index → then the Zone 5 list.

- [ ] **Seed saving method navigation**: Two index articles — "Self-Pollinating Species" and "Cross-Pollinating Species" — with isolation distance notes. This is the most practically important navigation path for seed savers. Verify both index articles exist and correctly categorize at least 10 species each.

- [ ] **Viability testing procedure navigation**: A "Seed Viability Tests" index article links to all viability testing procedure articles. Searchable by "seed viability test" in Kiwix. Confirm search returns this index article.

- [ ] **Planting calendar cross-references**: Each species card links to its relevant regional planting calendar. A user on the Cherokee Purple Tomato species card can navigate to "Zone 6 — Planting Calendar" via a direct link. Verify cross-links resolve.

**Gate 3 result**: PASS if all five items are checked.

### Gate 4 — Performance Baselines

The Seed module is the largest of the three by article count (200+ species cards). Performance testing is more important here than for Medical or Water.

- [ ] **ZIM export time with 200+ species cards**: Generate the full seeds ZIM on the Pi 5. Expected: under 5 minutes (200+ articles is ~3x the Medical module). If export exceeds 8 minutes: reduce batch size, process species in chunks of 50, and combine into the final ZIM in a second pass using libzim merge functionality.

- [ ] **ZIM file size**: `open-repo_en_seeds_YYYY-MM.zim` (nopic variant, 200+ species cards + viability tables + 5 zone calendars + 5 crop category + 5 index = ~215+ articles) expected 3–10 MB. If file exceeds 15 MB, check for accidentally large viability projection tables — cap projections at 10 years to limit table size.

- [ ] **Kiwix search latency — species name search**: In Kiwix, search "Cherokee Purple" — correct species card appears on first result page. Expected search latency: under 1 second. If search takes over 3 seconds, the Xapian index size may be too large — review the number of articles being indexed (should be ~215 articles maximum, well within Xapian limits).

- [ ] **Kiwix search latency — Latin binomial search**: Search "Solanum lycopersicum" — correct species card appears. Latin binomial search is the secondary search path (used by more technically sophisticated users). Confirm both common name and Latin name search paths work.

- [ ] **zimcheck passes**: `zimcheck open-repo_en_seeds_YYYY-MM.zim` exits 0. Pay particular attention to the ZIM `name` field — it must be `open-repo_en_seeds_2026-06` (all lowercase, underscore separators, no spaces).

**Gate 4 result**: PASS if all five items are checked.

### Seed Fallback Paths

**Fallback Path 1 (Gate 1 FAIL — GRIN join produces fewer than 200 matched species)**:
- Expand the join to include species matched by family + growth habit, not just exact Latin binomial. Tolerate minor spelling variations (var./subsp. normalization).
- If match count is still below 200 after normalization: use GRIN data for species where available and fall back to USDA PLANTS duration data ("annual", "perennial") for viability inference. This is a weaker signal but maintains coverage.
- Minimum viable article count: 100 species cards. Below 100 is insufficient for a useful seed reference and Phase 5.2 Seed module should be deferred to Phase 5.3 with more sourcing time.

**Fallback Path 2 (Gate 2 FAIL — germination calendar table is unreadable)**:
- Simplify the calendar table format: replace month-column format with a text-based list per species ("Start indoors: April 1–15. Transplant: May 15. Direct sow: N/A"). This is less visually appealing but universally readable.
- If table horizontal scrolling does not work in Kiwix: split the 12-month calendar into two 6-month tables (Jan–Jun and Jul–Dec) displayed vertically. This avoids scrolling requirements.

**Fallback Path 3 (Gate 3 FAIL — index articles fail to populate)**:
- If GRIN data does not include growing zone information: use USDA PLANTS "Growth_Habit" + hardiness data to infer zone suitability. This requires a lookup table for growth habit to zone mapping.
- If species cross-links to planting calendars produce 404: verify that the calendar article paths use the same zone numbering format as the species card links. Standardize on `seeds/calendar/zone-5` (not `seeds/calendar/zone_5` or `seeds/calendar/hardiness-5`).

---

## Consolidated 3x4 Success Criteria Matrix

This matrix is the minimum bar for each module to be considered integration-ready. All 12 cells must be PASS before any module's ZIM is published to the OPDS catalog or CDN.

| | Gate 1: Data Compatibility | Gate 2: Media Embedding | Gate 3: Interactive Components | Gate 4: Performance |
|---|---|---|---|---|
| **Medical (8.20)** | ≥60 articles; all dosing fields non-null; source citations on every article | Disclaimer visible on all articles; danger-box CSS renders in Kiwix Android; no external URLs | Brand name aliases searchable; internal cross-links resolve; procedure steps in ordered lists | Export <3 min; ZIM <50 MB; zimcheck passes |
| **Water (7.90)** | ≥40 articles; chemical unit consistency (mg/L); sizing calculator produces 16 valid outputs | SVG or PNG schematics render in Kiwix Android; sizing tables display in Kiwix; no external URLs | System-type index articles link correctly; sizing navigation by household size works; no 404 links | Export <3 min; nopic ZIM <10 MB; zimcheck passes |
| **Seed (7.80)** | ≥215 articles; GRIN join ≥200 species; viability calculator validates against GRIN reference | Calendar table readable in Kiwix; species card nopic variant complete; dual-name title format consistent | Zone index articles (6 zones) all resolve; species-to-calendar cross-links work; viability testing navigable | Export <5 min; ZIM <15 MB; Latin binomial search works; zimcheck passes |

---

## Shared Validation Requirements (All Three Modules)

These requirements apply to every Phase 5.2 module regardless of candidate-specific results.

**Schema backward compatibility**: Adding new `item_type` values (`medical_condition`, `drug_monograph`, `medical_procedure`, `water_procedure`, `sizing_guide`, `system_selection`, `seed_species`, `viability_test`, `planting_calendar`) must not break any of the 240 Phase 5.1 tests. Verify: `uv run pytest tests/ -q --tb=short` still shows 240 passed before AND after each new module is merged.

**Database migration (if required)**: New `item_type` enum values may require a schema migration if the `item_type` column uses a database-level enum type. In SQLite (current deployment), enum constraints are application-level — new item types can be inserted without a migration. Verify: `sqlite3 sqlite.db "SELECT DISTINCT item_type FROM content_items;"` shows only valid types after import run.

**Rollback test**: Before publishing any module, verify the rollback procedure works. Specifically: delete the generated ZIM file and re-run the full export pipeline. The re-generated ZIM must be byte-for-byte identical (or functionally equivalent) to the original. Non-reproducible ZIM generation is a pipeline bug that must be fixed before production use.

**Content accuracy review gate**: No module's ZIM is published until the author has completed a manual spot-check of every numerical value (drug dose, chemical quantity, seed viability years) against the cited source document. The spot-check must cover at least 20% of all numerical fields. Sampling protocol: select 10 random articles from each type (conditions, drugs, procedures, etc.) and verify all numerical values against source.

---

## Sources

- Phase 5.1 ZIM Architecture — `/projects/open-repo/PHASE_5_ARCHITECTURE.md`
- Phase 5.2 Capability Audit — `/projects/open-repo/PHASE_5.2_CAPABILITY_AUDIT.md`
- Phase 5.2 ZIM Validation Matrix (pre-implementation capability) — `/projects/open-repo/PHASE_5.2_ZIM_VALIDATION_MATRIX.md`
- Phase 5.2 Medical Water Seed Roadmap — `/projects/open-repo/PHASE_5.2_MEDICAL_WATER_SEED_ROADMAP.md`
- [openZIM ZIM format specification](https://wiki.openzim.org/wiki/ZIM_file_format)
- [zimcheck documentation — openzim/zim-tools](https://github.com/openzim/zim-tools)
- [Kiwix Android WebView SVG rendering notes](https://github.com/kiwix/kiwix-android)
- [GRIN Global bulk data download](https://www.grin-global.org/)
- [USDA PLANTS database bulk CSV](https://plants.usda.gov/home/downloads)
- [WHO DWQG 4th edition](https://www.who.int/publications/i/item/9789241549950)
- [CDC water treatment guidelines](https://www.cdc.gov/healthywater/drinking/index.html)
