# Phase 5: Offline Export & Kiwix Integration — Comprehensive Architecture Plan

**Status**: Ready for Implementation (pending Phase 4 PR #1 merge)  
**Version**: 1.0  
**Date**: 2026-05-13  
**Target Duration**: 6 weeks (post-PR-merge) · ~18 hours total effort  
**Target Completion**: Late June 2026

---

## Executive Summary

**What is Phase 5?**

Phase 5 enables offline access to the open-repo knowledge base by exporting content as Kiwix-compatible ZIM archives. Users will download a ~100 MB offline library and read it in Kiwix readers (mobile, desktop, Raspberry Pi) without requiring internet connectivity.

**Why it matters:**

Open-repo's target audience includes users in low-bandwidth regions, offline field workers, and institutions without reliable internet. Phase 5 unlocks distribution to these communities via USB, downloaded files, and offline readers—expanding reach beyond web access.

**What will be delivered:**

1. **Export pipeline**: Automated weekly generation of ZIM archives (text-only and domain-specific variants)
2. **ZIM format output**: Valid, compressed offline archives that pass Kiwix validation tools
3. **Offline reader integration**: Exports compatible with Kiwix Android (F-Droid), Kiwix Desktop (all platforms), and kiwix-serve (institutional)
4. **Distribution channels**: HTTPS CDN downloads, OPDS catalog discovery in Kiwix apps, IPFS content addressing
5. **Pull-sync foundation**: Database and API infrastructure for peer-to-peer node sync (Wave 5.2)

**Success means:**
- Users download a `~100 MB` ZIM file
- Open it in Kiwix reader
- Browse all documents offline with full-text search
- Works on phones, laptops, Raspberry Pi, and offline servers
- No internet required

**Technical dependencies on Phase 4:**

- Phase 4 must deliver: ContentItem database schema with `is_local`, `domain`, `version` fields
- Phase 4 must deliver: ActivityPub federation endpoints (used for sync in Phase 5 Wave 2)
- Phase 4 must deliver: HTTP Signature key infrastructure (reused for distributed sync)

---

## 1. Phase 5 Overview & Goals

### 1.1 Scope Definition

**In Scope:**
- Export local content items (where `is_local = True`) to ZIM format
- Generate three export variants: full library (text), domain-specific, reference snapshot
- Validate exports with `zimcheck`; store checksums and CIDs
- Publish OPDS catalog for Kiwix in-app discovery
- Host archives on CDN (Cloudflare R2, zero egress cost)
- Implement retention policy (keep 2 recent versions + references)
- Design distributed sync infrastructure (implement in Phase 5 Wave 2)

**Out of Scope (Phase 5.1+):**
- Incremental delta exports (use full re-exports instead)
- Federated content inclusion (each node exports only its own items)
- Mobile client (PWA that wraps kiwix-serve — Phase 5 stretch goal)
- BitTorrent seeding (Phase 5.1 supplement)
- Multi-language support beyond English (Phase 5.1)

### 1.2 Success Criteria (End of Phase 5)

| Criterion | Target | Rationale |
|-----------|--------|-----------|
| **Export generation time** | < 60 seconds for nopic variant | Large files should generate within a typical cron window |
| **ZIM file size** | Full: < 500 MB; Domain: < 50 MB | Fits in GitHub Releases, practical for low-bandwidth download |
| **Compression ratio** | 3:1 (Zstandard cluster compression) | Zstd default; validates file integrity |
| **zimcheck validation** | 100% pass rate | No invalid exports shipped to users |
| **Kiwix compatibility** | Works on 3+ platforms (Android F-Droid, Desktop, kiwix-serve) | Proof of interoperability |
| **Full-text search** | All articles indexed and searchable | Xapian index embedded in ZIM |
| **Storage cost** | < $5/month steady-state | R2 Free Tier covers MVP (10 GB/month) |
| **Uptime** | 99%+ availability (CDN + R2) | End-users can always download latest |
| **Update frequency** | Weekly automated exports | Keeps content fresh without manual intervention |
| **Documentation completeness** | 3 platforms (Android, Desktop, Server) + one example walkthrough | Users can operate independently |

---

## 2. Offline Export Pipeline Architecture

### 2.1 Data Source & Input

**Source**: Phase 4 database (`content_items` table)

**Query logic**:
```sql
SELECT * FROM content_items 
WHERE is_local = True
  AND status IN ('published', 'featured')
  [AND domain = {domain}]  -- optional filter for domain exports
ORDER BY domain, created_at DESC
```

**Streaming approach**: Load items in batches of 200 to avoid memory overhead. A production deployment with 1,000+ items should stream through 5+ batches.

**Fields used**:
- `content_id` (unique key)
- `title` (export as ZIM article title)
- `slug` (ZIM URL path: `/items/{slug}`)
- `content_html` (rendered body; must be self-contained)
- `item_type` ('procedure', 'recipe', 'schematic', 'plan', 'service-listing')
- `domain` ('agriculture', 'water', 'food', 'electronics', 'building', 'energy')
- `created_at`, `updated_at` (for versioning)
- `endorsement_count` (static snapshot: "Endorsed by N community members")

### 2.2 Transformation Layer: Content → ZIM HTML

**Step 1: HTML Rendering**

Each item is rendered to self-contained HTML with NO external dependencies:
- All CSS embedded in `<style>` tags (no external stylesheets)
- No `<script>` tags (JavaScript not available offline)
- No external image URLs; images must be embedded as base64 or skipped in nopic variant
- Interactive elements (voting UI, edit buttons) stripped entirely
- Navigation elements removed (no sidebars, headers, footers in the article body)
- Content-only HTML suitable for full-text indexing

**Template structure** (Jinja2):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ item.title }}</title>
    <style>
        /* Embedded CSS: typography, layout, responsive design */
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto; }
        .main-content { max-width: 42em; margin: 0 auto; padding: 1em; }
        .procedure-step { margin: 1em 0; padding: 1em; border-left: 3px solid #0066cc; }
        .endorsement-badge { color: #666; font-size: 0.9em; }
    </style>
</head>
<body>
    <main class="main-content">
        <h1>{{ item.title }}</h1>
        <p class="item-metadata">
            <strong>Category:</strong> {{ item.domain }} | 
            <strong>Type:</strong> {{ item.item_type }}
        </p>
        
        <!-- Rendered content (procedures, recipes, schematics) -->
        {% if item.item_type == 'procedure' %}
            <ol class="procedure-steps">
                {% for step in item.steps %}
                    <li class="procedure-step">{{ step.instruction | safe }}</li>
                {% endfor %}
            </ol>
        {% endif %}
        
        <!-- Static endorsement snapshot -->
        <p class="endorsement-badge">
            ✓ Endorsed by {{ item.endorsement_count }} community members
        </p>
        
        <!-- Attribution (if federated) -->
        {% if item.is_local == False %}
            <footer class="attribution">
                <p>Originally published on {{ item.source_node_name }}. 
                   Distributed under {{ item.license_name }}.</p>
            </footer>
        {% endif %}
    </main>
</body>
</html>
```

**Key rendering decisions**:
- No JavaScript: Xapian FTS (offline search) doesn't execute JS; interactive elements are pointless.
- Embedded CSS only: Keeps the ZIM self-contained.
- Static counts: Vote counts rendered as plain text (e.g., "42 endorsements"), not live numbers.
- Main content only: Article body and metadata; no site chrome.

### 2.3 Storage Layer: ZIM Assembly

**ZIM file structure** (what gets written):

| Component | Generated by | Purpose |
|-----------|----------|---------|
| ZIM Header | libzim | File format magic, compression settings, cluster offsets |
| Articles | ZimWriter loop | One entry per content item (path: `/items/{slug}`, content: HTML) |
| Metadata (M/) | creator.add_metadata() | Title, Description, Language, Creator, Date, Illustration |
| Xapian Index | creator.config_indexing() | Full-text search index (auto-generated from article text) |
| Namespaces | libzim | Directory structure (`A/` for articles, `M/` for metadata) |
| Compression | Zstandard (zstd) | Cluster-level compression; 3:1 typical ratio |

**File size estimate** (at Phase 5 launch, 500-1,000 items):
- Text-only (nopic): 50-80 MB → compressed to 15-25 MB
- With low-res images (nopic variant skips): 200-400 MB → compressed to 60-120 MB
- Domain-specific (agriculture, 50-100 items): 5-10 MB

**Staging location**: Local filesystem temporary directory or FastAPI temp file (`/tmp/{uuid}.zim.partial`). Move to permanent storage after validation.

### 2.4 Distribution: CDN & Download Paths

**Primary CDN**: Cloudflare R2 (zero egress cost, S3-compatible API)

**URL structure**:
```
https://exports.open-repo.example.org/zim/open-repo_en_nopic_2026-05.zim
https://exports.open-repo.example.org/zim/open-repo_en_nopic_2026-05.zim.sha256
https://exports.open-repo.example.org/zim/open-repo_en_nopic_latest.zim  [redirect]
```

**Download channels**:
1. **Direct HTTPS**: CDN URL (fastest, cached globally)
2. **OPDS catalog**: In-app Kiwix library browser (preferred UX for mobile)
3. **GitHub Releases** (future): For domain exports < 50 MB
4. **IPFS** (Wave 5.2): Content-addressed, censorship-resistant
5. **BitTorrent** (Phase 5.1): Community seeding

**Retention policy** (after each successful export):
- Keep current version (`is_current = True`) forever
- Keep previous month's version (most recent previous)
- Keep any version < 30 days old (safety window for ongoing downloads)
- Delete older versions from CDN; mark DB row `status = 'deleted'`
- Result: 4-6 live versions per flavour at steady state

### 2.5 Update Frequency

| Variant | Schedule | Notes |
|---------|----------|-------|
| **Full (nopic)** | Weekly (Sunday 02:00 UTC) | Fast, low-bandwidth friendly |
| **Domain-specific** | Weekly for active domains (>10 items) | Targets specific communities |
| **Full (with images)** | Monthly (1st at 02:00 UTC) | Slower generation, larger file |
| **Reference snapshot** | Manual (`POST /api/exports/reference`) | Immutable, never deleted; citeable |

**Scheduled job infrastructure**: FastAPI BackgroundTask or APScheduler cron. Must handle concurrent exports (lock mechanism to prevent duplicate runs).

---

## 3. Kiwix Integration Approach

### 3.1 ZIM Format Specification

**ZIM file format** is the open-source offline archiving standard used by Kiwix, Wikipedia's offline distribution, and Project Gutenberg.

**Key properties**:
- **Random-access**: Cluster offsets allow article retrieval without decompressing the entire file
- **Embedded search**: Xapian full-text index bundled in the ZIM; no separate search server needed
- **Compression**: Zstandard cluster-level compression; 2.5-3x typical ratio on text
- **Streaming read**: Suitable for low-RAM devices (Raspberry Pi, old phones)

**Mandatory metadata** (zimcheck enforces):

| Field | Format | Example |
|-------|--------|---------|
| `Title` | UTF-8, ≤ 30 chars | `"Open-Repo: All Domains"` |
| `Description` | UTF-8, ≤ 80 chars | `"Offline practical knowledge library"` |
| `Language` | ISO 639-3 code | `"eng"` |
| `Creator` | String | `"Open-Repo Community"` |
| `Publisher` | String | `"Open-Repo"` |
| `Date` | YYYY-MM-DD | `"2026-05-13"` |
| `Name` | `{publisher}_{lang}_{flavour}` (no period) | `"open-repo_en_nopic"` |
| `Illustration_48x48` | PNG, exactly 48×48 px | Binary blob (stored in ZIM) |

**Naming convention** (openZIM standard):
```
{name}_{period}.zim

open-repo_en_nopic_2026-05.zim
open-repo_en_agriculture_2026-05.zim
open-repo_en_all_2026-05.zim
```

### 3.2 Kiwix Library Integration

**Tool choice: `python-libzim`** (PyPI package: `libzim`)

**Why python-libzim**:
- ✓ Official C++ libzim with Python bindings
- ✓ Wheels pre-built for Linux x86/ARM64, macOS, Windows
- ✓ No Rust or C++ compiler required
- ✓ Stable Creator API (Context Manager syntax)
- ✓ Xapian indexing built-in
- ✗ Alternative: `zimit` (headless browser crawl) — rejected; too heavyweight for API-based export

**Dependency**: Pin `libzim>=3.2,<4.0` in `pyproject.toml`

**Minimal usage example**:
```python
from libzim.writer import Creator

with Creator("output.zim") as creator:
    creator.config_indexing(True, "eng")  # Enable Xapian FTS
    creator.add_metadata("Title", "Open-Repo: All Domains")
    creator.add_metadata("Description", "Offline practical knowledge library")
    creator.add_metadata("Language", "eng")
    creator.add_metadata("Creator", "Open-Repo Community")
    creator.add_metadata("Publisher", "Open-Repo")
    creator.add_metadata("Date", "2026-05-13")
    creator.add_metadata("Name", "open-repo_en_nopic")
    creator.add_illustration(48, icon_bytes)  # 48x48 PNG
    
    # Add articles (streamed from DB)
    for item in content_items:
        creator.add_item(ArticleItem(
            path=f"/items/{item.slug}",
            title=item.title,
            content=render_html(item),
            mimetype="text/html"
        ))
```

### 3.3 Content Indexing Strategy

**Full-text search** is powered by Xapian, embedded in the ZIM:

**What gets indexed**:
1. Article title (high relevance weight)
2. Article body (rendered HTML; tags stripped before indexing)
3. Domain/category metadata (if rendered as hidden text)
4. Item type and tags (if rendered in `<meta>` or hidden div)

**Search quality depends on**:
- Non-empty `get_title()` for each article (required)
- Semantic HTML structure (procedures as `<ol>`, categories as metadata)
- Clean article body (no navigation/header/footer chrome mixed in)

**Xapian language**: Set to `"eng"` (English stemming). For multilingual content, generate separate ZIM files per language or index only the primary language.

**Search performance**: Cold first search (~7-8s), warm subsequent searches (~0.1-1.5s). kiwix-serve documentation should note this warmup behavior.

### 3.4 Mobile Reader Compatibility

**Kiwix Android** (Official, F-Droid):
- ✓ Opens ZIM files from Downloads folder
- ✓ Built-in full-text search (Xapian)
- ✓ Responsive UI for phones
- ✓ Offline reading without internet
- ✗ Play Store variant has path restrictions (uses in-app OPDS catalog as workaround)

**Kiwix Desktop** (macOS, Windows, Linux):
- ✓ Opens ZIM files from any folder
- ✓ Tabbed browsing
- ✓ Full-text search
- ✓ Downloadable offline catalogs

**kiwix-serve** (Docker/standalone):
- ✓ HTTP server for ZIM files (LAN or internet-facing)
- ✓ OPDS catalog endpoint
- ✓ Multi-user access
- ✓ Institutional deployments (schools, clinics)

### 3.5 Recommended Reader Apps (with License Notes)

| App | Platform | License | Use Case | Notes |
|-----|----------|---------|----------|-------|
| **Kiwix Android (F-Droid)** | Mobile | GPL 3 | Individual offline access | Full version, no Play Store restrictions |
| **Kiwix Desktop** | Windows, macOS, Linux | GPL 3 | Desktop offline access | Cross-platform, professional UX |
| **kiwix-serve + Docker** | Server/LAN | GPL 3 | Institutional (schools, clinics) | Zero-conf deployment |
| **Kiwix iOS** | iPhone/iPad | MPL 2 | iPhone users | Limited (Kiwix Foundation maintains) |
| **Iram** | Android | GPL 3 | Custom reader | Lightweight alternative |

---

## 4. Deployment Options & Selection

### 4.1 Option A: GitHub Actions Build (Nightly)

**Mechanism**: GitHub Actions workflow runs ZIM export every night; uploads to GitHub Releases.

**Pros**:
- ✓ Free CI/CD (GitHub Actions free tier: 2,000 minutes/month)
- ✓ No server infrastructure to maintain
- ✓ Built-in release asset management
- ✓ Versioning via GitHub's release system

**Cons**:
- ✗ GitHub Releases 2 GB per-file limit (domain exports OK, full exports may be constrained)
- ✗ No automated retention policy (manual release cleanup)
- ✗ Harder to distribute IPFS/CAR variants
- ✗ Analytics (download counts) not available

**Cost**: Free

**When to use**: Small projects, < 100 MB archives, community-driven

### 4.2 Option B: Self-Hosted Pipeline (VPS Cron)

**Mechanism**: Dedicated VPS runs export job weekly via cron; uploads to external CDN or serves directly.

**Pros**:
- ✓ Full control over scheduling and retention
- ✓ Can generate IPFS hashes and CAR files
- ✓ Custom analytics and monitoring
- ✓ No GitHub dependency

**Cons**:
- ✗ Infrastructure cost ($10-20/month)
- ✗ Manual maintenance (monitoring, backups, updates)
- ✗ Single point of failure (if VPS is down, exports don't run)
- ✗ Bandwidth costs if not paired with CDN

**Cost**: $10-20/month VPS + optional CDN

**When to use**: Mature projects with dedicated ops resources

### 4.3 Option C: S3 + CloudFront CDN (AWS)

**Mechanism**: Export jobs push ZIM to S3; CloudFront distributes globally.

**Pros**:
- ✓ Global distribution (low latency for users worldwide)
- ✓ Automatic expiry/versioning via S3 lifecycle policies
- ✓ HTTPS and resumable downloads
- ✗ Per-gigabyte egress fees ($0.085/GB for non-CloudFront, but CF can reduce)

**Cons**:
- ✗ Setup complexity (IAM, lifecycle policies, cache headers)
- ✗ Egress costs (10,000 downloads of 2 GB = $1,700 per month)

**Cost**: $50-200+/month for active distribution

**Not recommended for open-source projects.**

### 4.4 Option D: Cloudflare R2 + R2 Serve (RECOMMENDED)

**Mechanism**: Export jobs push ZIM to R2 bucket; R2's global edge automatically caches and serves via Cloudflare.

**Pros**:
- ✓ Zero egress fees (R2's value proposition vs. S3)
- ✓ Automatic global distribution (Cloudflare edge network)
- ✓ S3-compatible API (standard boto3 client)
- ✓ Retention policies via bucket lifecycle rules
- ✓ Free 10 GB tier (covers Phase 5 MVP entirely)
- ✓ Resumable downloads (HTTP Range requests)
- ✓ CDN caching headers and CORS-ready

**Cons**:
- ✗ Requires Cloudflare account (domain must be Cloudflare nameserver)

**Cost**: Free (10 GB/month), then $0.015/GB storage

**Phase 5 MVP estimate**: 2-5 GB storage at any time = < $0.10/month

### 4.5 DECISION FRAMEWORK

| Dimension | A: GitHub | B: Self-Hosted | C: AWS S3 | D: R2 (CHOSEN) |
|-----------|-----------|---|---|---|
| Setup time | < 1 hour | 4 hours | 2 hours | 2 hours |
| Monthly cost | $0 | $10-20 | $50-200+ | $0-1 |
| Egress cost | $0 | Depends on CDN | High | $0 |
| Retention policy | Manual | Automated cron | Automated lifecycle | Automated lifecycle |
| IPFS integration | Hard (no daemon) | Easy (daemon available) | Hard | Easy |
| Scaling to 10+ GB | Limited (2 GB/file) | Fine | Fine | Fine |
| Ops burden | Minimal | Moderate | Moderate | Minimal |

**Recommendation**: **Cloudflare R2 for Phase 5 MVP and beyond**

- Zero egress cost makes it suitable for high-traffic distribution
- Cloudflare's global edge automatically serves cached content fast
- Free 10 GB tier covers MVP; scales cost-effectively
- S3-compatible API; no vendor lock-in
- Integrates cleanly with IPFS and CAR workflows

**Fallback**: If R2 adoption is delayed, GitHub Actions + GitHub Releases works for Phase 5 MVP.

---

## 5. Testing Strategy

### 5.1 Unit Tests (ZIM Output Validation)

| Test | What it verifies |
|------|------------------|
| `test_zim_metadata_complete` | All mandatory fields present; Title ≤ 30 chars |
| `test_naming_convention` | Filename matches `{name}_{YYYY-MM}.zim` pattern |
| `test_html_no_external_deps` | BeautifulSoup scan: no `<link href="http">` or `<img src="http">` |
| `test_article_title_not_empty` | Every article has non-empty `get_title()` |
| `test_article_count` | Article count in ZIM matches expected count from query |
| `test_sha256_checksum` | SHA-256 matches computed hash of file |

### 5.2 Integration Tests (Reader Compatibility)

| Test | What it verifies | Platform |
|------|------------------|----------|
| `test_zimcheck_validation` | `zimcheck output.zim` returns no errors | CI (subprocess) |
| `test_libzim_reader` | libzim.reader.Archive can read back all articles | CI |
| `test_search_index_populated` | Archive.search("agriculture") returns ≥ 1 result | CI |
| `test_illustration_present` | Archive.get_illustration_blob(48) returns non-empty | CI |
| `test_kiwix_serve_localhost` | kiwix-serve can serve ZIM; GET returns article | Docker (CI) |
| `test_opds_feed_valid` | OPDS XML is well-formed and parseable by feedgen | CI |

### 5.3 Manual Testing (Reader Apps)

| Platform | Test | Success Criteria |
|----------|------|------------------|
| **Android** | Download ZIM via browser; open in Kiwix F-Droid | Articles display correctly; search works |
| **Desktop (Linux)** | Download ZIM; open in Kiwix desktop | Articles display; full-text search functional |
| **kiwix-serve** | Generate ZIM → docker run kiwix/kiwix-serve → browse localhost:8080 | All articles accessible via browser |

### 5.4 Content Fidelity Tests

| Test | What it verifies |
|------|------------------|
| `test_all_fields_preserved` | Item title, type, domain rendered in output; no truncation |
| `test_no_character_loss` | Unicode (Spanish, Arabic) survives render → HTML → ZIM → read |
| `test_procedure_steps_ordered` | Procedure items with 5+ steps render in correct order |
| `test_image_fallback` | nopic variant skips images; no broken `<img>` tags |

### 5.5 Search Verification

| Test | What it verifies |
|------|------------------|
| `test_title_search` | Searching for item title returns that item (top result) |
| `test_domain_search` | Searching for domain name returns items from that domain |
| `test_keyword_search` | Searching for a specific technique/ingredient returns relevant items |
| `test_search_relevance` | Title matches ranked higher than body text matches |

---

## 6. Success Criteria & Metrics

### 6.1 Minimum Viable Success

- [ ] **ZIM export succeeds**: `POST /api/exports` returns job ID; job completes without errors
- [ ] **Format valid**: `zimcheck output.zim` returns zero errors
- [ ] **All content present**: Article count in ZIM matches database query
- [ ] **Readable**: ZIM opens in Kiwix Android (F-Droid) and desktop; articles display
- [ ] **Searchable**: Full-text search returns results for common keywords
- [ ] **Checksummed**: SHA-256 sidecar published alongside ZIM file
- [ ] **Accessible**: Public HTTPS download link works (via R2 or GitHub Releases)

### 6.2 Strong Success (Phase 5 Complete)

| Metric | Target | Evidence |
|--------|--------|----------|
| **Generation time** | < 60 seconds (nopic variant) | Time logged in export job |
| **File size** | Full < 500 MB, Domain < 50 MB | Actual ZIM sizes |
| **Compression ratio** | 3:1 or better | File size / uncompressed estimate |
| **Storage cost** | < $5/month | R2 billing |
| **Reader compatibility** | 3+ platforms (Android, Desktop, kiwix-serve) | Manual testing across 3 apps |
| **Search quality** | All 10 test keywords return results | Search integration tests pass |
| **Uptime** | 99%+ CDN availability | CloudflareR2 status dashboard |
| **Update frequency** | Weekly automated | Cron job executes; exports published |
| **Documentation** | 3 platforms covered + 1 walkthrough | README + user guide sections |

### 6.3 Stretch Goals (Phase 5.1+)

- [ ] Incremental/differential exports (only changed items)
- [ ] Multi-language ZIM files
- [ ] BitTorrent .torrent files for each export
- [ ] IPFS CAR files for offline transfer
- [ ] Signed manifest (GPG) for artifact verification
- [ ] Pull-sync endpoint for peer-to-peer node synchronization

---

## 7. Week-by-Week Implementation Timeline

*Starts immediately after Phase 4 PR #1 merges. Total: 6 weeks (~18 hours effort)*

### Week 1: Kiwix Format Learning & ZIM Experimentation (3 hours)

**Goals**: Understand ZIM specification; run trial export

**Tasks**:
- [ ] Read openZIM ZIM format specification (30 min)
- [ ] Read python-libzim API documentation (30 min)
- [ ] Create a minimal test ZIM (10 articles) using python-libzim (1 hour)
- [ ] Validate with zimcheck; verify opens in kiwix-serve (30 min)
- [ ] Document findings in `phase-5-implementation-notes.md` (30 min)

**Checkpoint**: "Hello ZIM" works; zimcheck passes; kiwix-serve serves it.

---

### Week 2: Export Pipeline v0.1 (5 hours)

**Goals**: Build core export logic; generate first real archive

**Tasks**:
- [ ] Implement `ContentQueryStream` (iterate DB in batches of 200) (1 hour)
- [ ] Implement HTML rendering template (Jinja2) (1.5 hours)
- [ ] Implement `ZimWriter` class (python-libzim wrapper) (1 hour)
- [ ] Implement `zimcheck` validation integration (30 min)
- [ ] Compute SHA-256 checksum (15 min)
- [ ] Generate test archive from real data; pass zimcheck (30 min)

**Deliverable**: `test_export_50_items.zim` (< 10 MB), passes zimcheck, validated

**Checkpoint**: First real ZIM with actual open-repo content; ready for reader testing

---

### Week 3: Phase 4 Integration (3 hours)

**Goals**: Wire export pipeline to Phase 4 database; support multiple variants

**Tasks**:
- [ ] Implement `ExportConfig` dataclass (scope, flavour, language, images) (30 min)
- [ ] Implement `ExportJob` background task (FastAPI or APScheduler) (1 hour)
- [ ] Add domain-scoped exports (filter by domain in query) (30 min)
- [ ] Add nopic variant (skip images in HTML) (30 min)
- [ ] Create `zim_exports` database table + migration (30 min)

**Deliverables**:
- Full export ZIM (all domains, text-only)
- Agriculture domain ZIM (5-10 MB)
- Recipes domain ZIM (similar)

**Checkpoint**: Multiple variants generated; each passes zimcheck

---

### Week 4: Testing on Multiple Readers (3 hours)

**Goals**: Prove ZIM works on 3+ Kiwix reader platforms

**Tasks**:
- [ ] Manual test on Kiwix Android (F-Droid) (1 hour)
  - Download ZIM from share link
  - Open in Kiwix app
  - Browse articles; test search
- [ ] Manual test on Kiwix Desktop (Linux) (1 hour)
  - Download ZIM
  - Open in Kiwix
  - Verify display and search
- [ ] Manual test on kiwix-serve (Docker) (30 min)
  - Build Docker image with ZIM
  - Start server; browse via browser
- [ ] Document any UI quirks or compatibility issues (30 min)

**Deliverable**: Testing report; any bugs fixed

**Checkpoint**: "Users can download our ZIM and read it in Kiwix" — DONE

---

### Week 5: Deployment Setup (2 hours)

**Goals**: Automate export generation and publishing

**Tasks**:
- [ ] Set up Cloudflare R2 bucket (30 min)
  - Create bucket
  - Configure public read access
  - Test upload via boto3
- [ ] Implement R2 upload in export job (30 min)
- [ ] Add APScheduler cron for weekly export (Sunday 02:00 UTC) (30 min)
- [ ] Implement retention policy (keep 2 versions + references) (30 min)

**Deliverable**: First automated export runs; files uploaded to R2; accessible via HTTPS

**Checkpoint**: "Exports happen automatically and are publicly downloadable"

---

### Week 6: Documentation & User Guide (2 hours)

**Goals**: Document for end-users on 3 platforms

**Tasks**:
- [ ] Write Android setup guide (30 min)
  - Screenshot walkthrough
  - URL shortlink to R2 download
  - Notes on F-Droid variant vs. Play Store
- [ ] Write Desktop setup guide (30 min)
  - Windows, macOS, Linux steps
  - Where to place ZIM files
- [ ] Write kiwix-serve (Institutional) guide (30 min)
  - Docker command
  - LAN sharing setup
  - Library XML format
- [ ] Create one end-to-end walkthrough example (30 min)
  - Download → open → search workflow

**Deliverable**: `/projects/open-repo/docs/PHASE_5_USER_GUIDE.md`

**Checkpoint**: "Users can self-serve without asking for help"

---

### Summary

| Phase | Duration | Effort | Gate |
|-------|----------|--------|------|
| 1: Learning | 1 week | 3 hours | Hello ZIM passes zimcheck |
| 2: Pipeline | 1 week | 5 hours | Real ZIM validated |
| 3: Integration | 1 week | 3 hours | Multiple variants generated |
| 4: Testing | 1 week | 3 hours | Works on 3+ reader platforms |
| 5: Deployment | 1 week | 2 hours | Automated exports to CDN |
| 6: Documentation | 1 week | 2 hours | User guide complete |
| **TOTAL** | **6 weeks** | **18 hours** | **MVP ready** |

---

## 8. Dependencies & Risk Mitigation

### 8.1 Hard Dependencies (Blocking)

| Dependency | Status | Mitigation |
|-----------|--------|-----------|
| **Phase 4 PR #1 merge** | BLOCKING (as of 2026-05-13) | No Phase 5 implementation until merged; preliminary work on design/tests only |
| **Phase 4 ContentItem schema** | Must include: `is_local`, `domain`, `version` | Coordinate with Phase 4 implementation; validate schema before Week 2 |
| **python-libzim >= 3.2** | New dependency | Add to `pyproject.toml`; test wheels on Linux/macOS/Windows before commit |
| **Cloudflare account** | R2 requires Cloudflare | Open account before Week 5; verify boto3 upload works |

### 8.2 Risk Register

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| **ZIM format complexity** | Medium | High (export fails) | Use python-libzim abstraction; study IPFS/Wikipedia ZIM exports for examples |
| **HTML rendering bugs** (truncation, character loss) | Medium | Medium (data loss in offline copy) | Unit tests for Unicode/special chars; manual content fidelity spot-checks |
| **zimcheck validation fails** (non-obvious error) | Low | High (exports unusable) | Verbose zimcheck output in CI; test minimal ZIM first; reference openzim docs |
| **Generation time > 60s** (large exports slow) | Medium | Low (async task OK) | Profile generation; optimize streaming if needed; incremental approach in Phase 5.1 |
| **R2 costs unexpected** (egress charge) | Low | Low (R2 has zero egress by design) | Monitor monthly bill; R2 is cost-effective |
| **Kiwix reader incompatibilities** | Medium | Medium (some users can't read) | Test on F-Droid Kiwix + desktop; document incompatibilities |
| **Android Play Store path restrictions** | Medium | Low (F-Droid workaround exists) | Document F-Droid as primary distribution; in-app OPDS as alternative |
| **Search index bloat** | Low | Low (affects performance, not correctness) | Xapian stemming is standard; monitor index size relative to article count |
| **Missing attribution** (federated content) | Medium | High (license violation) | Phase 5 MVP: exclude federated content; add attribution template if included later |

### 8.3 Contingency Scenarios

**Scenario A: libzim wheel not available for target platform**
- **Mitigation**: Test wheel availability before Week 2; if missing, use pure-Python zim-tools CLI wrapper (slower but works)

**Scenario B: zimcheck rejects valid ZIM for obscure reason**
- **Mitigation**: Compare output against known-good Wikipedia ZIM; report issue to openzim team; may need to adjust metadata

**Scenario C: Generation time > 5 minutes for large exports**
- **Mitigation**: Implement streaming/chunked generation; or reduce initial export scope to domains only (skip "full")

**Scenario D: R2 or Cloudflare account provisioning delayed**
- **Mitigation**: Use GitHub Releases as fallback (2 GB per-file limit OK for nopic variant); migrate to R2 later

**Scenario E: Kiwix compatibility issues on specific platform**
- **Mitigation**: Document workarounds; prioritize platforms with active users (Android F-Droid first)

---

## Appendix A: Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     PHASE 5 DATA FLOW                            │
└─────────────────────────────────────────────────────────────────┘

        ┌───────────────────┐
        │  Phase 4 Database │
        │  (content_items)  │
        └────────┬──────────┘
                 │
                 ▼
    ┌─────────────────────────────────┐
    │  ContentQueryStream (batch 200)  │
    │  WHERE is_local=True             │
    │  ORDER BY domain                 │
    └────────┬────────────────────────┘
             │
             ▼
    ┌─────────────────────────────────┐
    │  HTML Rendering (Jinja2)        │
    │  - Self-contained CSS           │
    │  - No external deps             │
    │  - Static content only          │
    └────────┬────────────────────────┘
             │
             ▼
    ┌─────────────────────────────────┐
    │  ZimWriter (libzim.Creator)     │
    │  - Add articles                 │
    │  - Config Xapian indexing       │
    │  - Add metadata & illustration  │
    └────────┬────────────────────────┘
             │
             ▼
    ┌─────────────────────────────────┐
    │  zimcheck Validation            │
    │  [FAIL → mark job 'error']      │
    │  [PASS → continue]              │
    └────────┬────────────────────────┘
             │
             ▼
    ┌─────────────────────────────────┐
    │  Compute SHA-256 Checksum       │
    │  Store in .sha256 sidecar       │
    └────────┬────────────────────────┘
             │
             ▼
    ┌─────────────────────────────────┐
    │  Upload to Cloudflare R2        │
    │  - ZIM file                     │
    │  - .sha256 sidecar              │
    │  - Public read access           │
    └────────┬────────────────────────┘
             │
             ▼
    ┌─────────────────────────────────┐
    │  Database (zim_exports)         │
    │  - Insert new row (available)   │
    │  - Update old row (superseded)  │
    │  - Apply retention policy       │
    └────────┬────────────────────────┘
             │
             ├─────┬──────────────┬────────────┐
             ▼     ▼              ▼            ▼
          OPDS  CDN URL   GitHub Release  IPFS/CAR
          Feed  (R2)      (Phase 5.1)     (Wave 5.2)
             │     │              │            │
             ├─────┴──────────────┴────────────┤
             │                                 │
             ▼                                 ▼
    ┌──────────────────┐          ┌────────────────────┐
    │  Kiwix Readers   │          │  End-User Download │
    │  - Android       │          │  + Offline Reading │
    │  - Desktop       │          │                    │
    │  - kiwix-serve   │          │  ✓ DONE            │
    └──────────────────┘          └────────────────────┘
```

---

## Appendix B: Code Entry Points (Post-Phase 4 Merge)

**Where Phase 5 code will live:**

```
projects/open-repo/backend/
├── app/
│   ├── api/
│   │   └── export.py              # POST /api/exports, GET /api/exports/{job_id}
│   ├── services/
│   │   ├── export_service.py      # ExportJob, ExportConfig, ExportScope
│   │   ├── zim_writer.py          # ZimWriter (libzim wrapper)
│   │   └── content_stream.py      # ContentQueryStream
│   ├── models/
│   │   └── export.py              # ZimExport SQLAlchemy model
│   └── templates/
│       └── zim_article.html       # Jinja2 template for rendered HTML
├── migrations/
│   └── versions/
│       └── 2026_05_13_zim_exports_table.py  # Alembic migration
├── tests/
│   ├── unit/
│   │   ├── test_content_stream.py
│   │   ├── test_zim_writer.py
│   │   ├── test_export_config.py
│   │   └── test_html_rendering.py
│   └── integration/
│       ├── test_zimcheck_validation.py
│       ├── test_kiwix_serve.py
│       └── test_end_to_end_export.py
└── docs/
    ├── PHASE_5_USER_GUIDE.md      # User-facing documentation
    └── PHASE_5_IMPLEMENTATION_NOTES.md  # Dev notes/decisions
```

---

## Appendix C: OPDS Catalog Example

**Endpoint**: `/opds/v2/root.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opds="http://opds-spec.org/2010/catalog">
  <id>urn:uuid:open-repo-exports</id>
  <title>Open-Repo Offline Library</title>
  <updated>2026-05-13T00:00:00Z</updated>
  
  <link rel="self" href="/opds/v2/root.xml"/>
  <link rel="start" href="/opds/v2/root.xml"/>
  <link rel="search" href="/opds/v2/searchdescription.xml"/>
  
  <entry>
    <title>Full Library (Text-Only)</title>
    <id>urn:open-repo:export:nopic:2026-05</id>
    <updated>2026-05-13T00:00:00Z</updated>
    <author><name>Open-Repo Community</name></author>
    <summary>All domains, no images. 50-80 MB.</summary>
    <link rel="acquisition"
          type="application/x-zim"
          href="https://exports.open-repo.example.org/zim/open-repo_en_nopic_2026-05.zim"
          length="52428800"/>
  </entry>
  
  <entry>
    <title>Agriculture (Domain)</title>
    <id>urn:open-repo:export:agriculture:2026-05</id>
    <updated>2026-05-13T00:00:00Z</updated>
    <summary>Agriculture and farming guides. 5-10 MB.</summary>
    <link rel="acquisition"
          type="application/x-zim"
          href="https://exports.open-repo.example.org/zim/open-repo_en_agriculture_2026-05.zim"
          length="8388608"/>
  </entry>
</feed>
```

---

## References & Further Reading

- [openZIM ZIM Format Specification](https://wiki.openzim.org/wiki/ZIM_file_format)
- [python-libzim ReadTheDocs](https://python-libzim.readthedocs.io/)
- [Kiwix Official Site](https://kiwix.org/)
- [Kiwix/OPDS Catalog Documentation](https://wiki.kiwix.org/wiki/OPDS)
- [zimcheck Tool](https://github.com/openzim/zim-tools)
- [Cloudflare R2 Documentation](https://developers.cloudflare.com/r2/)
- [Phase 4 Design: Federation & ActivityPub](./PHASE_4_DESIGN.md)

---

**Document Status**: Ready for implementation (waiting Phase 4 PR #1 merge)

**Last Updated**: 2026-05-13

**Next Steps**: Upon PR #1 merge, hand off to implementation team with this architecture as the specification.
