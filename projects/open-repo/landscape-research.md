---
title: "Open-Repo: Landscape Research — Existing Resources Survey"
date: 2026-04-13
status: initial-draft
tags: [open-knowledge, landscape-research, distributed-library]
---

# Open-Repo: Landscape Research

## Executive Finding

No single system does what this project envisions. What exists are silos — excellent in their domains, disconnected from each other, and collectively covering perhaps 30-40% of the content surface that matters. The gap is not in any one category; it is in the connective tissue: a unified discovery layer, a shared identity/contribution model, cross-domain structured metadata, and support for practical know-how (how to build, make, do, and exchange things) rather than just text and encyclopedic fact.

The project's opportunity is not to rebuild Wikipedia or reclone the Internet Archive. It is to build the **index, the bridge, and the missing quadrants** — particularly practical knowledge (plans, schematics, local services, recipes as executable instructions, skill exchange) combined with a federated graph that ties existing sources together.

---

## Platform-by-Platform Assessment

### 1. Wikipedia / Wikidata

**What it does well:**
- ~6.7 million articles in English; 62+ million across all languages
- Wikidata: 116 million items, ~16 billion triples, the world's largest open knowledge graph as of mid-2025
- CC0 license on Wikidata — truly free
- SPARQL query interface; structured facts with persistent QIDs
- Daily updates at ~500,000 edits/day; highly current for notable topics
- October 2025: added vector embeddings and MCP-compatible API

**What is missing or broken:**
- Notability bias: anything not "notable enough" gets deleted. Practical local knowledge, community resources, small-scale techniques — all excluded
- No procedural content: Wikipedia tells you what a thing is, not how to build, make, or do it
- No structured recipes, building plans, 3D models, or service listings
- Wikidata's underlying database (Blazegraph) was effectively abandoned when Amazon acquired the dev team in 2018; the Wikimedia Foundation has been in a multi-year migration that is still incomplete as of late 2025
- Quality is wildly uneven outside English; many topics have thin or no coverage in under-resourced languages
- Governance is opaque to newcomers; editing culture is hostile to non-expert contributors

**Verdict:** Foundational reference layer. Link to it, query Wikidata's graph. Do not attempt to replicate or compete.

---

### 2. Internet Archive / Open Library / Wayback Machine

**What it does well:**
- Wayback Machine: 1 trillion archived webpages (100,000+ TB) as of October 2025
- Open Library: 3M+ books, "one web page for every book ever published" ambition
- Designated Federal Depository Library by U.S. Senate in July 2025
- Preservation copies stored in multiple geographic locations
- Strong track record as the world's institutional memory for the web

**What is missing or broken:**
- Open Library lost its fair use appeal in 2024; controlled digital lending is legally constrained, limiting access to in-copyright material
- Book metadata is extensive but content access for non-public-domain works is legally uncertain and shrinking
- No structured data layer: you can read books but you cannot query "all recipes that mention turmeric" or "all schematics for water pumps"
- No practical/procedural content beyond text
- Centralised: a single organisation controls it; funding crises are existential (the Archive suffered a major hack and service disruption in 2024)
- No service/skills exchange or 3D model hosting

**Verdict:** Essential archival foundation. Link to it for text and web history. The centralised single-point-of-failure model is a risk the open-repo project should consciously avoid replicating.

---

### 3. OpenStreetMap (OSM)

**What it does well:**
- The canonical open geospatial dataset: streets, buildings, amenities, land use, elevation
- Massive contributor base; corporate sponsors include TomTom, Microsoft, Esri, Meta
- Open license (ODbL); free to use, modify, redistribute
- Overture Maps Foundation emerging as an alternative/complement with additional data layers

**What is missing or broken:**
- Coverage quality is highly variable by geography — excellent in Western Europe, poor in rural Global South
- No semantic linking to knowledge about places (a building in OSM has coordinates, not a link to what it is, its history, its open hours in a structured way)
- No procedural content, skills, or local service exchange
- Tag ontology is folksonomy — useful but inconsistent

**Verdict:** Use OSM as the geospatial layer for any location-indexed content (local services, community resources, places of interest). Do not rebuild it.

---

### 4. Project Gutenberg / Wikisource

**What it does well:**
- Project Gutenberg: ~78,000 public domain texts (March 2026), oldest digital library (founded 1971)
- Wikisource: proofread, structured texts at the individual-work level; multilingual
- Fully public domain; no legal ambiguity
- Open Library is progressively integrating both as "Trusted Book Providers"

**What is missing or broken:**
- Strictly public domain — nothing in copyright
- Text only; no multimedia, no procedural content
- No structured metadata that would allow cross-querying (e.g., "all medical texts from the 1800s mentioning smallpox")
- Gutenberg's volunteer-driven model means coverage is idiosyncratic — prolific Victorian novelists, yes; non-English traditional knowledge, no

**Verdict:** Link in as a text source. The gap they leave is everything in copyright and everything non-textual.

---

### 5. LibreTexts / Khan Academy / OpenStax

**What it does well:**
- LibreTexts: 2,000+ open educational resources, STEM focus, higher education
- Khan Academy: K-college mathematics and sciences; free, accessible globally; available in many languages
- OpenStax: peer-reviewed open textbooks for higher education STEM
- Together cover a large fraction of formal educational content

**What is missing or broken:**
- All three are heavily STEM-biased; humanities, trades, crafts, vocational skills, traditional knowledge are thin or absent
- Khan Academy: Reading/Language Arts is the weakest area; no depth in real analysis, advanced topics, non-Western subjects
- None host procedural/practical content: how to repair an engine, grow food in a specific climate, build a solar panel array
- None support community contribution at the level of Wikipedia
- Khan Academy's content model is video + exercises — does not support structured data or remixable content units

**Verdict:** Excellent supplementary links for formal educational content. The gap they leave is vocational/practical knowledge and non-formal learning.

---

### 6. Thingiverse / Printables / MyMiniFactory (3D Models)

**What it does well:**
- Thingiverse: established the genre; massive legacy library
- Printables (Prusa): cleaner UI, better search filters (printer type, material, print time), active community
- MyMiniFactory: quality-controlled; printability guaranteed
- MakerWorld: fully free, building fast
- Yeggi/STLFinder: cross-platform search indexes

**What is missing or broken:**
- Thingiverse: outdated interface, unreliable, creator abandonment accelerating
- All platforms are siloed; no cross-platform search that is reliable and comprehensive
- 3D models are the format; engineering schematics (PCB layouts, mechanical drawings) live elsewhere (GrabCAD, CERN OHR, Open Circuits)
- No unified metadata standard linking a 3D model to its schematics, bill of materials, assembly instructions, and sourcing guides
- No connection to the social context: who made it, where to get help, local makers who can print it

**Verdict:** The 3D model space is fragmented and needs a unified metadata/discovery layer. The gap is cross-format: the same object should link its STL, its schematic, its BOM, its assembly guide, and its Instructables-style how-to.

---

### 7. Instructables / Hackaday / WikiHow

**What it does well:**
- Instructables: the dominant how-to platform; strong maker/craft/electronics content
- Hackaday: electronics and engineering focus; deep expertise
- WikiHow: broad procedural coverage; illustrated step-by-step format
- Together cover a large surface of practical how-to knowledge

**What is missing or broken:**
- Instructables is corporate-owned (Autodesk); no commitment to open data or long-term preservation
- WikiHow is proprietary and centrally controlled
- No structured data: steps are prose, not machine-readable
- No formal linking to materials, tools, sourcing (beyond Amazon affiliate links)
- Poor coverage of traditional crafts, indigenous techniques, agricultural practices, repair culture
- No cross-linking to the 3D models, schematics, or scientific literature behind a project
- Content quality is extremely uneven; no peer review mechanism

**Verdict:** Key content gap to fill with structured, machine-readable, openly licensed procedural knowledge. This is one of the most important missing layers.

---

### 8. GitHub

**What it does well:**
- The world's largest software repository; also hosts hardware designs, datasets, documentation
- Strong versioning, collaboration, issue-tracking model
- GitHub Pages for documentation; free for public repos
- Massive network effects; most open source projects live here

**What is missing or broken:**
- Discovery is poor for non-software content: a PCB design lives next to a JavaScript library with no way to distinguish them by category
- Requires Git literacy — enormous barrier for non-technical contributors
- Microsoft-owned; not decentralised
- No content metadata standards for non-code assets
- No notion of "this repo is a recipe / schematic / building plan / dataset"

**Verdict:** Use as a hosting layer and contribution mechanism for technical contributors. Git/GitHub should be one of several contribution pathways, not the only one.

---

### 9. IPFS / Filecoin / Distributed Storage

**What it does well:**
- Content-addressed storage: files are identified by cryptographic hash of their content, making them censorship-resistant and verifiable
- Demonstrated use case: Turkey blocked Wikipedia in 2017; IPFS mirror remained accessible
- No single point of failure or control
- Growing ecosystem: Filecoin adds economic incentives for long-term storage
- 2025 developments: convergence with zero-knowledge proofs for privacy-preserving verification; MCP-compatible datasets for AI training

**What is missing or broken:**
- Retrieval performance is unreliable: content must be pinned by someone or it disappears; pure IPFS without pinning services is not "permanent"
- User experience is poor for non-technical contributors
- Centralisation creep: most IPFS traffic routes through a small number of gateways (Cloudflare, Protocol Labs) — the decentralisation is theoretical for most users
- No governance layer, no search, no metadata standards
- ACM WWW 2025 paper: "Centralization in the Decentralized Web: Challenges and Opportunities in IPFS Data Management" documents this problem formally

**Verdict:** Correct storage substrate for a censorship-resistant knowledge commons. Must be combined with a pinning network, search index, and metadata layer to be usable.

---

### 10. Kiwix

**What it does well:**
- ZIM file format: highly compressed, fully indexed offline snapshots of websites
- Wikipedia, Wikisource, Wikivoyage, Wikibooks all available; regular updates
- Deployed in schools across Nigeria, Tanzania, Ecuador, and elsewhere with no internet access
- Raspberry Pi integration; works on old hardware
- Available as browser extension, desktop app, mobile

**What is missing or broken:**
- Kiwix is a reading/distribution tool, not a contribution platform
- Content is still centralised at creation time; Kiwix just distributes it offline
- June 2025: English Wikipedia ZIM update was significantly delayed (estimated end June 2025) — production pipeline fragility
- No structured data querying; ZIM is read-only

**Verdict:** Critical distribution layer for offline/low-bandwidth contexts. Open-repo should produce Kiwix-compatible ZIM exports as a matter of course.

---

### 11. Anna's Archive

**What it does well:**
- Self-described "largest truly open library in human history"
- 51 million books, 99 million papers as of 2025; 1.1 petabytes
- March 2025: 650,000+ daily downloads — roughly 10x the New York Public Library's estimated daily distribution
- Backs up from Internet Archive, HathiTrust, DuXiu, and other sources
- Non-profit; preservation-first mission

**What is missing or broken:**
- Legally precarious: operates in direct violation of copyright law in most jurisdictions
- No structured metadata layer; search is basic
- No procedural content; text/PDF only
- No community contribution model for original content

**Verdict:** Illustrates enormous demand for free access to knowledge regardless of copyright. The legal grey zone means open-repo cannot directly replicate its model for in-copyright content — but the demand it serves is real and unmet by legal means.

---

### 12. Common Crawl

**What it does well:**
- Open repository of web crawl data; December 2025 archive: 2.16 billion pages
- Freely available for research and AI training
- Used by virtually every major LLM training pipeline

**What is missing or broken:**
- Raw crawl data, not curated knowledge; extremely noisy
- No structure beyond HTML; requires extensive processing to extract useful information
- No attribution, provenance, or licensing information for individual pages
- Not accessible to non-technical users

**Verdict:** Research infrastructure layer. Not a user-facing knowledge resource; useful as a data source for populating structured knowledge.

---

### 13. Semantic Scholar

**What it does well:**
- AI-powered search over 200+ million scientific papers
- Open API; free access; backed by Allen Institute for AI
- Semantic search, citation graphs, influential-paper detection
- Strong coverage of CS, medicine, biology

**What is missing or broken:**
- Science-only: no practical knowledge, no how-to, no non-academic content
- Paywalled papers surface in search but not in content
- No contribution model for practitioners or non-academics
- Coverage in humanities, social sciences, and non-English research is thinner

**Verdict:** Strong link target for scientific claims. Open-repo should integrate Semantic Scholar citations where relevant but not attempt to replicate its corpus.

---

### 14. Open Food Facts

**What it does well:**
- 4 million food products from 150 countries; 25,000+ contributors
- Structured data: ingredients, allergens, nutrition facts, product labels
- Open database (ODbL); API available
- Genuinely crowdsourced; mobile app for scanning and contributing

**What is missing or broken:**
- Products only, not recipes; no procedural knowledge
- No cultural context, cooking methods, or regional variation
- Coverage is skewed toward packaged goods in wealthy countries

**Verdict:** Excellent model for structured community-contributed data. The contribution UX (scan product, add data) is a template worth studying.

---

### 15. WikiHouse / Open Building Institute

**What it does well:**
- WikiHouse: CNC-cut wood panel construction system; plans downloadable, buildable by amateurs
- Open Building Institute (OBI): modular design library for structures; open source forever commitment
- Paperhouses: aggregates architect-designed open source home plans globally
- Alejandro Aravena's Elemental: CC-licensed public housing designs (AutoCAD DWG files)

**What is missing or broken:**
- Fragmented across multiple sites with no common search or metadata standard
- No connection to 3D models, material sourcing, or local builder networks
- Most designs assume access to CNC machinery or professional tools
- No adaptation layer for different climates, building codes, or available materials

**Verdict:** A critical content category almost entirely absent from existing aggregators. Open-repo should be the index that ties these together and adds the structured metadata layer.

---

### 16. Time Banking / Skills Exchange Platforms

**What it does well:**
- hOurworld (Time and Talents): free nonprofit platform for time bank communities
- Shareish: open-source, map-based mutual aid; gift economy model; openly replicable
- Ruby for Good Mutual Aid: used by multiple city-level mutual aid organisations
- Blockchain-based time banking experiments for elder care coordination

**What is missing or broken:**
- Fragmented by locality: each community runs its own instance with no interoperability
- No federated standard for service/skill descriptions
- No connection to the knowledge base (if you offer to teach someone to repair bikes, where is the linked repair guide?)
- Discovery is hyper-local; no global index of what skills/services communities offer

**Verdict:** Completely absent from every major knowledge platform. This is a high-value missing layer: connecting practical knowledge with the people who have it and the communities that need it.

---

## Synthesis: The Gap Map

| Content Category | Best Existing Source | Gap Level |
|---|---|---|
| Encyclopedic facts | Wikipedia / Wikidata | Low — well served |
| Scientific literature | Semantic Scholar + arXiv | Medium — access limited |
| Public domain books | Gutenberg / Wikisource | Low — well served |
| In-copyright books | Anna's Archive (illegal) | High — legal void |
| Web archive | Internet Archive | Low — well served |
| Educational video/exercises | Khan Academy | Medium — STEM-heavy |
| Open textbooks | LibreTexts / OpenStax | Medium — STEM-heavy |
| Maps / geospatial | OpenStreetMap | Low — well served |
| 3D models | Printables / Thingiverse | High — fragmented, no metadata |
| Electronics schematics | GitHub / GrabCAD / CERN | High — fragmented, no unified index |
| Building plans / architecture | WikiHouse / OBI / Paperhouses | Very High — scattered, no index |
| How-to / procedural | Instructables / WikiHow | High — unstructured, proprietary |
| Recipes (structured) | None at scale | Very High — massive gap |
| Traditional/indigenous knowledge | None systematically | Critical gap |
| Vocational/trades knowledge | None systematically | Very High |
| Agricultural techniques | None systematically | Very High |
| Local services / skills exchange | hOurworld / Shareish | Very High — no global index |
| Offline distribution | Kiwix | Low — well served for text |

**The highest-value gap:** Structured, machine-readable, openly licensed **practical knowledge** — how to build, grow, cook, repair, make, and exchange — that links across formats (text, 3D model, schematic, video, BOM) and connects to local human networks who can help.

---

## Sources

- [Wikidata — Wikipedia](https://en.wikipedia.org/wiki/Wikidata)
- [Scaling the Knowledge Graph Behind Wikipedia — BigDATAwire](https://www.hpcwire.com/bigdatawire/2025/07/10/scaling-the-knowledge-graph-behind-wikipedia/)
- [Wikidata adds AI vectors — Diginomica](https://diginomica.com/wikidata-adds-ai-vectors-graph-and-knowledge-bases-heres-why)
- [Internet Archive — Wikipedia](https://en.wikipedia.org/wiki/Internet_Archive)
- [Internet Archive loses appeal — Communia](https://communia-association.org/2024/09/25/internet-archive-loses-appeal-what-does-it-mean/)
- [Anna's Archive — Wikipedia](https://en.wikipedia.org/wiki/Anna's_Archive)
- [Anna's Archive re-emerges — CyberNews](https://cybernews.com/security/shadow-library-annas-archive-resurfaces-after-disruption/)
- [IPFS — Wikipedia](https://en.wikipedia.org/wiki/InterPlanetary_File_System)
- [Centralization in IPFS — ACM WWW 2025](https://dl.acm.org/doi/10.1145/3696410.3714627)
- [Kiwix — Wikipedia](https://en.wikipedia.org/wiki/Kiwix)
- [Kiwix offline Wikipedia update — Kiwix Hub](https://hub.kiwix.org/weblog/2025/6/an-update-on-the-offline-wikipedia-update/)
- [Kiwix for Schools — Wikimedia Diff](https://diff.wikimedia.org/2025/06/05/highlights-from-the-webinar-how-to-use-wikipedia-offline-bringing-knowledge-where-the-internet-cant-reach%F0%9F%93%9A/)
- [Printables alternatives — 3D-Printed.org](https://www.3d-printed.org/thingiverse-alternative/)
- [WikiHouse](https://www.wikihouse.cc/)
- [Open Building Institute — Opensource.com](https://opensource.com/life/16/7/getting-serious-about-open-source-homes)
- [Open source architecture — Opensource.com](https://opensource.com/life/16/5/6-open-source-architecture-projects)
- [Shareish mutual aid — ACM](https://dl.acm.org/doi/10.1145/3593743.3593790)
- [hOurworld time banking](https://hourworld.org/_TimeAndTalents.htm)
- [Open Food Facts — GitHub](https://github.com/openfoodfacts)
- [RecipeDB — Oxford Academic](https://academic.oup.com/database/article/doi/10.1093/database/baaa077/6006228)
- [Federated knowledge graphs — Wikimedia Meta](https://meta.wikimedia.org/wiki/Federated_knowledge_graphs)
- [ActivityPub — W3C](https://www.w3.org/TR/activitypub/)
- [Fediverse — Wikipedia](https://en.wikipedia.org/wiki/Fediverse)
- [Decentralised content moderation — Policy Review](https://policyreview.info/glossary/decentralised-content-moderation)
- [Bluesky stackable moderation](https://bsky.social/about/blog/03-12-2024-stackable-moderation)
- [Common Crawl](https://commoncrawl.org)
- [OpenStreetMap — Wikipedia](https://en.wikipedia.org/wiki/OpenStreetMap)
- [Semantic Scholar](https://www.semanticscholar.org)
- [List of open-source hardware projects — Wikipedia](https://en.wikipedia.org/wiki/List_of_open-source_hardware_projects)
- [Distributed Manufacturing of Open Hardware — NYU Law](https://www.law.nyu.edu/sites/default/files/DistributedManufacturingofOpenHardware.pdf)
