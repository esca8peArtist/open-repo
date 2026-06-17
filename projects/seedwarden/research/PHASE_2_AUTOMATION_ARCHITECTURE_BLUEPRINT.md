---
title: "Phase 2 Automation Architecture Blueprint: Botanical Data Pipeline"
date: 2026-06-17
status: research-complete
phase: Phase 2 planning
confidence: 85%
sources-consulted: 16
tags: [seedwarden, phase-2, automation, data-pipeline, taxonomy, phenology, iNaturalist, USDA-PLANTS]
---

# Phase 2 Automation Architecture Blueprint: Botanical Data Pipeline

**Lead finding**: A production-viable botanical data pipeline for Seedwarden can be assembled from five free or low-cost authoritative sources — iNaturalist, USDA PLANTS (via Flora API), USA National Phenology Network, Wikidata, and Wikimedia Commons — using Python (pyinaturalist, GBIF/SPARQL libraries) as the ingestion layer and Airtable or PostgreSQL as the local database. The full pipeline can be built to near-zero API cost. The highest engineering complexity is taxonomy synchronization across sources, not data access.

---

## 1. Data Source Inventory

### 1.1 iNaturalist API v2

**What it provides**:
- Taxon records: scientific name, common name(s), taxonomy hierarchy (kingdom → species), IUCN status, Wikipedia summary, representative photos (with license metadata)
- Observation records: geo-tagged sightings with date, phenological stage (if annotated), photo attachments, Research Grade status
- Open Data download: monthly CSV dumps of all Research Grade observations available at inaturalist.org/observations/export — no API rate limits apply to bulk exports

**API access**:
- Base URL: `https://api.inaturalist.org/v2/`
- Authentication: OAuth2 → JWT (expires 24h); required only for write operations
- Rate limit: 100 req/min (target 60 req/min to avoid blocks)
- Python library: `pyinaturalist` (full type annotations, built-in rate limiting, caching)
- Export formats via `pyinaturalist-convert`: CSV, JSON, DataFrame, Darwin Core Archive, GeoJSON, SQLite

**Key endpoints for Seedwarden**:
- `GET /taxa/{id}` — full taxon record including common names, taxonomy hierarchy, representative photos
- `GET /taxa/autocomplete?q={name}` — fuzzy search for species names (useful for synonym resolution)
- `GET /observations?taxon_id={id}&place_id={place}` — observations filtered by taxon and geography
- `GET /observations/species_counts` — aggregate species richness by place

**Bulk data approach** (preferred for initial load): Download the GBIF-iNaturalist data export (available via GBIF.org under CC-BY 4.0) rather than paginating the API for hundreds of species. Process locally, then use the API only for incremental updates.

---

### 1.2 USDA PLANTS Database (via Flora API)

**What it provides** (100+ fields per species):
- Taxonomy: scientific name, family, genus, USDA symbol, synonyms
- Distribution: state-level and county-level presence/absence, native/introduced/invasive status
- Growing conditions: hardiness zones, drought/heat tolerance, soil requirements, light
- Physical characteristics: habit, flower color, bloom months, leaf/fruit characteristics
- Ethnobotany: edible parts, medicinal uses, wildlife attractants, restoration value
- Conservation: global conservation rank, rarity

**API access**:
- Flora API (floraapi.com) wraps the USDA PLANTS public domain dataset
- Free tier: 1,000 requests/month, state-level data
- Developer tier: $19/month — county-level distribution, plant ID, conservation status
- Professional tier: $79/month — bulk export tools, climate resilience planning
- Authentication: API key in request header
- The underlying USDA PLANTS data is public domain; the R package `plantr` offers direct access without the Flora API middleman

**Direct USDA PLANTS access (no API key required)**:
The USDA PLANTS website (plants.usda.gov) supports bulk CSV download of the full plant characteristics database. For a one-time initial load of all US native species metadata, this CSV download is the most efficient route. Use Flora API for incremental updates and county-level queries thereafter.

**Gap**: The original REST API for USDA PLANTS data (`sckott/usdaplantsapi` on GitHub) is now defunct. Flora API is the primary maintained wrapper. The `plantr` R package remains active as of 2025.

---

### 1.3 USA National Phenology Network (USA-NPN)

**What it provides**:
- Observational phenology data from 2009 to present: bloom dates, leaf-out, fruiting, senescence — for thousands of plant species across the US
- Geospatial (raster) products: "Status of Spring" maps, accumulated degree-day layers, historical anomaly maps
- Four data formats: Status & Intensity, Individual Phenometrics, Site Phenometrics, Magnitude Phenometrics

**API access**:
- REST API: documented at usanpn.org/data/code
- R library: `rnpn` (CRAN) — primary maintained client
- Python: no official library, but REST endpoints are straightforward to call with `requests`
- Data available: free, no authentication required for observational data
- GitHub: github.com/usa-npn

**Seedwarden use case**: Automate monthly phenology alerts ("species currently in bloom in your region") by querying USA-NPN for current-season bloom status by species and geographic place. This powers a "What's in flower now?" feature or newsletter content without manual research.

**Implementation note**: Query `Individual Phenometrics` endpoint filtered by `taxon_id` (mapped to USDA PLANTS symbol) and `state` or bounding box. Join to Airtable species records by USDA symbol.

---

### 1.4 Wikidata (Taxonomy Synchronization)

**What it provides**:
- Structured taxonomic data: accepted scientific name, synonyms, higher taxonomy, common names in 300+ languages
- External ID crosswalks: USDA PLANTS symbol (P1772), iNaturalist taxon ID (P3151), GBIF species ID (P846), NCBI taxonomy ID (P685), IPNI plant ID (P961)
- Free SPARQL query endpoint: query.wikidata.org

**Why this matters for taxonomy sync**: Wikidata is the only public source that links USDA PLANTS symbols, iNaturalist taxon IDs, and GBIF IDs on the same entity. A single SPARQL query returns all external IDs for a species in one call — enabling cross-source joins without manual lookup.

**Example SPARQL query** (returns USDA symbol, iNaturalist ID, GBIF ID, common names for Trillium grandiflorum):
```sparql
SELECT ?item ?usdaSymbol ?inatID ?gbifID ?commonName WHERE {
  ?item wdt:P31 wd:Q16521 .       # instance of taxon
  ?item wdt:P225 "Trillium grandiflorum" .
  OPTIONAL { ?item wdt:P1772 ?usdaSymbol }
  OPTIONAL { ?item wdt:P3151 ?inatID }
  OPTIONAL { ?item wdt:P846 ?gbifID }
  OPTIONAL { ?item wikibase:label ?commonName . 
             FILTER(LANG(?commonName) = "en") }
}
```

**Rate limits**: No authentication required; SPARQL endpoint has a 60-second timeout per query. Batch queries by genus to stay within limits.

---

### 1.5 Wikimedia Commons (Image Automation)

**What it provides**: Public domain and Creative Commons botanical photographs and illustrations, accessible via the MediaWiki API.

**API access**:
- `action=query&prop=images` — list images on a Wikipedia plant article
- `action=query&titles=File:{filename}&prop=imageinfo&iiprop=url|extmetadata` — retrieve image URL and full license metadata (license type, attribution, description)
- Python: `mwclient` library handles authentication and pagination

**Automation workflow**: For each species record in Airtable, query Wikimedia for images tagged with the species' scientific name. Pull top 3 images with CC0 or CC BY licenses. Store URL and attribution metadata in the Airtable image fields. Run as a scheduled job (weekly or on new species record creation).

---

## 2. Data Pipeline Architecture

### 2.1 Pipeline Diagram (Conceptual)

```
AUTHORITATIVE SOURCES                INGESTION LAYER              LOCAL DATABASE          PUBLICATION
─────────────────────                ───────────────              ──────────────          ───────────
iNaturalist API v2 ──────────────►                                                        
USDA PLANTS (CSV/Flora API) ──────► Python Pipeline  ─────────► Airtable / PostgreSQL ──► Web Frontend
USA-NPN REST API ─────────────────► (pyinaturalist,               (species records,        (Astro/Next.js
Wikidata SPARQL ──────────────────►  requests, sparql             phenology data,           or GitBook)
Wikimedia Commons API ────────────►  mwclient)                    image assets,
                                     n8n / Make                   changelog)
                                     (automation                  
                                      middleware)                 
                                                                              
CONTRIBUTOR SUBMISSIONS                                                       
Airtable Form ──────────────────────────────────────────────────►             
iNaturalist Observation Export ──────────────────────────────────►             
```

### 2.2 Initial Load (One-Time)

**Step 1 — Species seed list**: Define target species list by bioregion (e.g., Northeast US native plants). Sources: USDA PLANTS state checklist CSVs (download directly from plants.usda.gov), bplant.org ecoregion lists, or existing Seedwarden product catalog.

**Step 2 — Taxonomy scaffolding via Wikidata**: For each species name, run a SPARQL query to fetch USDA symbol, iNaturalist taxon ID, GBIF ID, and all accepted synonyms. Load into Airtable as the canonical crosswalk table. This is the spine that allows any source to be joined to any other source by a consistent identifier.

**Step 3 — Metadata enrichment from USDA PLANTS**: Using USDA symbols from Step 2, query Flora API (or process the bulk CSV) for distribution, growing conditions, phenology fields, and uses. Load into Airtable species records.

**Step 4 — Observation data from iNaturalist**: Using iNaturalist taxon IDs from Step 2, query pyinaturalist for Research Grade observations in the target bioregion. Use `pyinaturalist-convert` to export as Darwin Core archive for archival, and as SQLite for local queries. Extract representative CC-licensed photos.

**Step 5 — Image enrichment**: For each species record, run the Wikimedia Commons API query to pull high-resolution images with license metadata. Cross-check against iNaturalist observation photos.

**Estimated time for initial load (500 species)**: 4–6 hours of pipeline runtime; 20–40 hours of development time to build and test.

---

### 2.3 Incremental Sync (Ongoing Automation)

Automation runs on three schedules:

**Daily (lightweight)**:
- iNaturalist new Research Grade observations for target species in target regions (detects range expansions, confirms seasonal presence)
- USA-NPN current phenological status for the target species list (powers "What's in bloom now")

**Weekly**:
- Wikimedia Commons image refresh: check for new high-quality images added to target species pages
- Wikidata synonym check: query for any recent synonym or taxonomic status changes (taxonomic updates propagate through Wikidata faster than USDA PLANTS)

**Monthly**:
- Full USDA PLANTS characteristics refresh (distribution updates, conservation status changes)
- Phenological summary: generate "monthly what's happening in each bioregion" report for newsletter content

**Implementation**: n8n (self-hosted, free) or Make ($9–29/month) as automation middleware. n8n is preferred for botanical pipelines due to native HTTP request node, code execution node (Python or JavaScript), and Airtable integration without per-operation fees.

---

## 3. Taxonomy Synchronization

### 3.1 The Core Problem

Plant taxonomy changes constantly. Species get split, lumped, reclassified, or renamed. A species known as *Aster novae-angliae* is now accepted as *Symphyotrichum novae-angliae*. Common names vary by region. The USDA PLANTS database, iNaturalist, GBIF, and Wikidata do not always agree on the accepted name at any given time.

**Without taxonomy sync, Seedwarden species records will drift out of alignment with authoritative sources**, resulting in broken cross-references, outdated names displayed to users, and failure to match incoming iNaturalist observation data.

### 3.2 Synchronization Strategy

**Layer 1 — Wikidata as the canonical resolver**: Wikidata's WikiProject Taxonomy maintains accepted names and their external IDs. Run a weekly SPARQL query against Wikidata for all species in the Seedwarden database, comparing the Wikidata-accepted name against the stored accepted name. Flag discrepancies for expert review rather than auto-applying changes (taxonomy changes are not always correct immediately after they propagate to Wikidata).

**Layer 2 — TNRS (Taxonomic Name Resolution Service)** — accessible at tnrs.biendata.org — resolves plant names against six authoritative sources (USDA, Tropicos, NCBI, Wikidata, etc.) and returns an accepted name with a match confidence score. Python access via `requests`. Use TNRS for any user-submitted species name that does not exactly match a Seedwarden record.

**Layer 3 — Synonym table in Airtable**: Every accepted species record links to a synonyms table containing all known alternate names (historical, regional, vernacular). Incoming data from any source is first checked against the synonym table before attempting a new species record creation.

**Layer 4 — Common name regional variants**: Common names are stored as a multi-value field with region tags. "New England Aster" (Northeast), "Michaelmas Daisy" (general), "Purple Daisy" (informal) are all linked to *Symphyotrichum novae-angliae* with region context.

---

## 4. Seasonal / Phenological Content Updates

### 4.1 USA-NPN Integration for "What's Happening Now"

The USA-NPN `Individual Phenometrics` endpoint returns phenological event records (first bloom, peak bloom, fruit set, etc.) by species, location, and year. For each target bioregion (e.g., "Northeast US" = states ME, VT, NH, MA, RI, CT, NY, NJ, PA), query for the current calendar week's status across the Seedwarden species list.

**Output**: A ranked list of species currently in bloom, fruiting, or setting seed in each bioregion, generated weekly and usable for:
- "This week in the Northeast" newsletter section
- Website homepage phenology widget
- Triggered content prompts (e.g., auto-drafting a plant spotlight for the top 3 in-bloom species)

### 4.2 iNaturalist Observation Spike Detection

Observation volume on iNaturalist spikes when a species is visibly in bloom (more people photograph it). Query the `observations/species_counts` endpoint weekly for each bioregion, sorted by recent observation count. A sudden increase in observations for a species is a reliable proxy for peak phenological activity — even without explicit phenological annotations.

This approach is used by Flora Incognita's expert botanist review loop: high observation volume triggers content review cycles for that species.

### 4.3 Phenology Field Schema in Airtable

Each species record carries:
- `bloom_months_usda`: USDA PLANTS-sourced bloom months (historical baseline)
- `bloom_months_npn`: USA-NPN derived from current-year observations (current-season truth)
- `last_observed_inat`: date of most recent Research Grade iNaturalist observation in target bioregion
- `npn_current_status`: formula field — "In bloom", "Past peak", "Not yet", "No data" — updated by weekly automation

---

## 5. Image Watermarking and Storage

### 5.1 Image Storage Architecture

**Recommended**: Cloudflare R2 (S3-compatible, zero egress fees) for primary image storage. Per-species folders named by USDA symbol (e.g., `/SYNE7/` for *Symphyotrichum novae-angliae*). Each image stored with a companion JSON sidecar file containing full license metadata.

**Cost**: R2 free tier covers 10 GB storage and 1M Class A operations/month — sufficient for Phase 2 (500 species × ~5 images each ≈ 2,500 images, approximately 2.5 GB at 1MB average).

### 5.2 Watermarking Policy

**For Seedwarden original photography** (field photos taken by staff or paid contractors): Apply a discreet watermark (small wordmark bottom-right corner) using Pillow (Python) or ImageMagick as part of the upload pipeline. Store both watermarked (public) and un-watermarked (archival) versions.

**For open-license images from Wikimedia/iNaturalist**: Do not watermark — this would violate CC license terms by obscuring original attribution. Instead, display attribution text visibly on the page adjacent to the image.

**Thumbnail generation**: Generate 3 sizes (thumbnail 200px, medium 600px, large 1200px) at upload time using Pillow. Store all three in R2. Serve appropriate size based on display context.

---

## 6. Architecture Summary and Implementation Sequence

| Phase | Action | Tools | Est. Dev Hours |
|---|---|---|---|
| 2a (weeks 1–2) | Build Airtable schema with all field types; set up Wikidata SPARQL crosswalk table | Airtable, Python | 8–12 hrs |
| 2b (weeks 2–3) | Initial species load: USDA PLANTS bulk CSV + Flora API enrichment (50 target species) | Python, Flora API | 10–15 hrs |
| 2c (weeks 3–4) | iNaturalist taxon + observation ingestion; image pipeline (Wikimedia + iNat) | pyinaturalist, mwclient, Cloudflare R2 | 15–20 hrs |
| 2d (week 4–5) | USA-NPN weekly phenology sync; Wikidata weekly taxonomy sync | n8n or Make, rnpn or requests | 8–10 hrs |
| 2e (week 5–6) | Contributor submission form + expert review queue in Airtable | Airtable automations | 4–6 hrs |
| 2f (weeks 6–8) | Frontend publication layer (static site pulling from Airtable API) | Astro or Next.js | 20–40 hrs |

**Total estimated development**: 65–103 hours for a complete Phase 2 pipeline covering 50–500 species. This is a 1–2 developer effort over 6–8 weeks.

---

## 7. Confidence Assessment and Gaps

**High confidence (>90%)**:
- iNaturalist API structure, rate limits, pyinaturalist library capabilities
- USDA PLANTS data availability (bulk CSV + Flora API)
- USA-NPN REST API and rnpn R library access
- Wikidata SPARQL endpoint capabilities for taxonomy crosswalk

**Medium confidence (75–85%)**:
- Flora API pricing stability (third-party service; pricing may change)
- n8n reliability for production automation at this scale (well-reviewed but self-hosted adds maintenance overhead)
- Phenology alert accuracy — USA-NPN data density varies significantly by region; Northeast and Midwest have strongest coverage, Southwest and Pacific Northwest are thinner

**Gaps identified**:
- No direct Flora of North America (FNA) API exists. Morphological descriptions must come from FNA text via web scraping (requiring HTML parsing of floranorthamerica.org Semantic MediaWiki) or manual entry — this is the most labor-intensive content production gap.
- iNaturalist phenological annotation (explicit "in bloom" vs. just "observed") covers only a subset of Research Grade observations. Not all observations include phenological stage annotations.
- County-level distribution data for Canadian provinces is weaker than US coverage across all sources examined.

---

## Sources

- [iNaturalist API Reference](https://www.inaturalist.org/pages/api+reference)
- [iNaturalist API Recommended Practices](https://www.inaturalist.org/pages/api+recommended+practices)
- [pyinaturalist Python Client](https://github.com/pyinat/pyinaturalist)
- [pyinaturalist-convert (Darwin Core + SQLite export)](https://github.com/pyinat/pyinaturalist-convert)
- [iNaturalist Developer Portal](https://www.inaturalist.org/pages/developers)
- [Flora API — Plant Data Endpoints and Pricing](https://floraapi.com/plant-data)
- [USDA PLANTS Database — plantr R package](https://mikemahoney218.github.io/plantr/)
- [USDA PLANTS Database API in R — Ag Data Commons](https://data.nal.usda.gov/dataset/usda-plants-database-api-r)
- [USA National Phenology Network — Data Access](https://www.usanpn.org/data/code)
- [rnpn R Library — CRAN vignette](https://cran.r-project.org/web/packages/rnpn/vignettes/I_introduction.html)
- [Darwin Core Standard — TDWG](https://dwc.tdwg.org/)
- [Darwin Core Data Package (DwC-DP) 2025](https://biss.pensoft.net/article/181043/)
- [Wikidata for Botanists — Annals of Botany](https://academic.oup.com/aob/article/136/3/491/8158086)
- [Wikidata WikiProject Taxonomy Tutorial](https://www.wikidata.org/wiki/Wikidata:WikiProject_Taxonomy/Tutorial)
- [ParseGBIF Workflow for GBIF Occurrence Data](https://www.nature.com/articles/s41598-024-56158-3)
- [GBIF — Darwin Core](https://www.gbif.org/darwin-core)
- [Flora of North America Online](https://floranorthamerica.org/Main_Page)
- [bplant.org — Interlinking Databases for Plant Research](https://bplant.org/blog/14)
- [Expanding Phenological Insights — PMC 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12479636/)
