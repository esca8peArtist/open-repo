---
title: "Phase 5: Offline Export — Production Architecture"
project: open-repo
phase: 5
status: pre-implementation design
date: 2026-04-27
author: research-agent
confidence: high
prerequisites:
  - phase-5-kiwix-architecture.md (read first — this document builds on it without repeating it)
tags: [offline-export, zim, kiwix, cdn, opds, federation, metadata, incremental, versioning]
---

# Phase 5: Offline Export — Production Architecture

**This document assumes familiarity with `phase-5-kiwix-architecture.md`.** That document covers: what Kiwix is, ZIM format internals, tool selection (python-libzim is the right choice), comparable project pipelines, integration strategy options (Option A: direct python-libzim), and a high-level 15–23 day implementation blueprint. None of that is repeated here.

This document deepens four areas that the prior research left as stubs: (1) the exact ZIM metadata and naming scheme needed for catalog discoverability, (2) a concrete incremental/versioning export strategy tied to open-repo's federation data model, (3) CDN and download infrastructure at production scale, and (4) the OPDS catalog integration that makes open-repo's exports visible inside Kiwix applications.

---

## 1. ZIM Metadata and Naming — Production Specification

### 1.1 Why Metadata Precision Matters

A ZIM file with correct metadata is discoverable in Kiwix's in-app library browser and the official `library.kiwix.org` catalog. One with malformed or missing mandatory fields may fail `zimcheck` validation, be silently rejected by Kiwix readers on some platforms, or appear with a blank title and no illustration in catalog UIs. Getting metadata right before first release avoids downstream pain.

### 1.2 Mandatory vs. Optional Metadata Fields

The openZIM specification defines metadata entries stored in the `M/` namespace. The following table reflects the current mandatory/optional distinction as tracked in the zim-tools `zimcheck` validation tool:

| Field | Required | Format | Open-Repo Value |
|---|---|---|---|
| `Title` | Mandatory | UTF-8 string, max 30 chars recommended | `"Open-Repo: [Scope] ([Language])"` |
| `Description` | Mandatory | UTF-8 string, max 80 chars | `"Offline knowledge library — practical how-to, recipes, and schematics"` |
| `Language` | Mandatory | ISO 639-3 code(s), comma-separated | `"eng"` or `"eng,spa"` for multilingual exports |
| `Creator` | Mandatory | UTF-8 string | `"Open-Repo Community"` |
| `Publisher` | Mandatory | UTF-8 string | `"Open-Repo"` (the node operator) |
| `Date` | Mandatory | `YYYY-MM-DD` | Generated at export time |
| `Name` | Mandatory for catalog | Naming convention (see 1.3) | `"open-repo_en_all"` (version-free) |
| `Flavour` | Optional but recommended | Freeform scope identifier | `"all"`, `"agriculture"`, `"recipes"` |
| `Tags` | Optional | Semicolon-separated | `"offline;practical-knowledge;procedures"` |
| `LongDescription` | Optional | UTF-8, max 4000 chars | Extended description |
| `Scraper` | Optional | Tool name + version | `"open-repo-exporter/1.0"` |
| `Source` | Optional | URL | The node's base URL |
| `Illustration_48x48` | Mandatory for catalog | PNG, exactly 48×48 px | Open-repo logo |

**Critical**: `LongDescription` is currently marked mandatory in some zimcheck versions but is contested (see [issue #408](https://github.com/openzim/zim-tools/issues/408)). Include it to be safe. The `Illustration_48x48` field is what appears as the icon in Kiwix's library browser — without it, the export looks broken in the UI even if technically valid.

### 1.3 The Naming Convention

The `Name` metadata field and the ZIM filename follow the openZIM naming convention exactly. The structure is:

```
{publisher}_{language}_{flavour}_{period}.zim
```

Rules:
- All lowercase, alphanumerics, hyphens, and periods only (`[a-z0-9\-\.]+`)
- Underscore is the part separator — do not use underscores within a part
- `{publisher}` maps to the content source domain (e.g., `open-repo.example.org` becomes `open-repo`)
- `{language}` is ISO 639-3 code; use `all` only for deliberately multilingual exports
- `{flavour}` describes the content scope: `all`, `agriculture`, `nopic`, `mini`
- `{period}` is `YYYY-MM` (as of openZIM ZIM Updates v2, 2024), with optional letter suffix `YYYY-MMa` if regenerating within the same month

**The `Name` metadata must be the filename without the period and `.zim` suffix:**

```python
# Example:
name_metadata = "open-repo_en_all"          # stored in ZIM metadata
period        = "2026-04"                    # appended at export time
filename      = f"{name_metadata}_{period}.zim"  # → open-repo_en_all_2026-04.zim
```

**Flavour strategy for open-repo:**

| Export Scope | Name | Flavour | Filename example |
|---|---|---|---|
| Full library, English, no images | `open-repo_en_nopic` | `nopic` | `open-repo_en_nopic_2026-04.zim` |
| Full library, English, with images | `open-repo_en_all` | `all` | `open-repo_en_all_2026-04.zim` |
| Agriculture domain only | `open-repo_en_agriculture` | `agriculture` | `open-repo_en_agriculture_2026-04.zim` |
| Recipes only | `open-repo_en_recipes` | `recipes` | `open-repo_en_recipes_2026-04.zim` |
| Multilingual full | `open-repo_mul_all` | `all` | `open-repo_mul_all_2026-04.zim` |

`nopic` is strongly recommended as the first export target: it will be significantly smaller, faster to generate, and more practical for the low-bandwidth use cases open-repo targets.

### 1.4 The Illustration Field

```python
with open("open-repo-icon-48x48.png", "rb") as f:
    icon_bytes = f.read()

# In the Creator context:
creator.add_illustration(48, icon_bytes)
```

The icon must be exactly 48×48 pixels and PNG-encoded. Kiwix readers use this for the library thumbnail. A correctly sized open-repo logo should be prepared as a project asset before the first export run.

### 1.5 Full-Text Search Index Language Configuration

The Xapian full-text index embedded by `creator.config_indexing(True, language_code)` uses Xapian's stemming library. Language must be the ISO 639-3 code (`"eng"`, `"spa"`, etc.). For multilingual exports, index only the primary language of the majority of content, or generate separate ZIM files per language to maximise search quality. Xapian does not support multi-language stemming in a single index cleanly.

**Search performance context**: Benchmark data from the openZIM community shows that a cold ZIM file read takes approximately 7–8 seconds while a warm (cached) read takes around 0.1 seconds. For institutional kiwix-serve deployments, this means the first search after server restart is slow but subsequent searches are fast. Open-repo's documentation should note this warmup behaviour.

---

## 2. Incremental Export Strategy — Tied to the Federation Data Model

### 2.1 Why Binary Diffs Are Not the Answer

The `zimdiff`/`zimpatch` tools from zim-tools were developed as a GSoC 2013 project and have never been declared production-ready. The core issue — checksum mismatches between the original and the patched file for large ZIM files — remains open as of 2025. No major ZIM publisher uses binary diffing in production. The Kiwix Android app requires a full re-download when a new version is available, and this is the documented status quo across all current ZIM content producers.

This is not a limitation to work around — it is the appropriate design constraint to accept. Versioned full exports with a smart retention policy is the correct implementation.

### 2.2 Export Versioning Model

Open-repo's export service should maintain a **versioned export catalog** in its database:

```sql
CREATE TABLE zim_exports (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,           -- "open-repo_en_all" (Name metadata value)
    flavour VARCHAR(100) NOT NULL,        -- "all", "nopic", "agriculture"
    language VARCHAR(20) NOT NULL,        -- "eng", "spa", "mul"
    period VARCHAR(10) NOT NULL,          -- "2026-04", "2026-04a"
    filename VARCHAR(512) NOT NULL,       -- "open-repo_en_all_2026-04.zim"
    file_size_bytes BIGINT,
    sha256_checksum VARCHAR(64),
    article_count INT,
    storage_path TEXT,                    -- S3/R2/B2 key path
    download_url TEXT,                    -- Public CDN URL
    torrent_url TEXT,                     -- Optional torrent URL
    is_current BOOLEAN DEFAULT FALSE,     -- Latest version for this name+flavour
    generated_at DATETIME,
    generation_duration_seconds INT,
    status ENUM('generating', 'validating', 'available', 'superseded', 'error'),
    error_message TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    INDEX idx_name_flavour (name, flavour),
    INDEX idx_is_current (is_current),
    INDEX idx_period (period)
);
```

When a new export run completes successfully:
1. Insert a new row with `status = 'available'` and `is_current = TRUE`.
2. Update all previous rows with the same `name` + `flavour` combination: set `is_current = FALSE` and `status = 'superseded'`.
3. Apply the retention policy (see 2.3).

### 2.3 Retention Policy

Following the openZIM ZIM Updates v2 retention logic (as of June 2024):

- Keep the **current** version (is_current = TRUE) always.
- Keep the **most recent version from each of the two most recent distinct months**.
- Keep any version that is **30 days old or less** (safety window for users mid-download).
- Delete everything else from object storage and mark the database row as `status = 'deleted'`.

This means at steady state (monthly exports), users always have access to this month's version and last month's version. Users who began downloading the previous-previous month's file but haven't finished have a 30-day safety window.

**Example**: If exports exist for 2026-01, 2026-02, 2026-03, 2026-04:
- 2026-04: keep (current)
- 2026-03: keep (most recent previous month)
- 2026-02: eligible for deletion if more than 30 days old
- 2026-01: delete

### 2.4 Scope-Based Sub-Exports as a Delta Proxy

Because true delta downloads don't exist, scope-scoped exports serve as the practical incremental strategy. A user who only needs agriculture content downloads the `agriculture` flavour (potentially 200 MB) instead of the `all` flavour (potentially 2 GB). This is the model that Kiwix itself uses: Wikipedia is available as a full archive (110 GB), a no-pictures archive (57 GB), and an introduction-only mini (7.4 GB).

**Export schedule recommendation:**

| Flavour | Generation trigger | Storage estimate |
|---|---|---|
| `nopic` (all domains, no images) | Weekly (Sunday night) | < 500 MB |
| `agriculture` | Weekly | < 200 MB |
| `recipes` | Weekly | < 100 MB |
| `all` (with images) | Monthly | 1–5 GB |
| `mul` (multilingual) | Monthly when translations available | 1–3 GB |

The `nopic` and domain-scoped flavours should be prioritised for Phase 5 MVP. The `all`-with-images export requires careful image processing (WebP conversion, thumbnail generation) and is a Phase 5.1 scope item.

### 2.5 Content Change Tracking for Export Scoping

The federation data model (Phase 4) provides version numbers on each content item. The export service can log the latest version seen at the time of each export:

```sql
CREATE TABLE export_content_snapshots (
    export_id BIGINT NOT NULL REFERENCES zim_exports(id),
    content_cid VARCHAR(255) NOT NULL,
    content_version INT NOT NULL,
    PRIMARY KEY (export_id, content_cid)
);
```

This table enables future work: computing which items changed between two export periods, which is the prerequisite for any future delta scheme. It does not enable incremental downloads in Phase 5, but it makes the data available for Phase 6+ analysis.

---

## 3. CDN Hosting and Download Infrastructure

### 3.1 Object Storage Selection

For open-repo's use case — public, large-file distribution of ZIM archives to a globally distributed audience, likely including many users in low-bandwidth regions — the storage and egress cost model is the dominant factor.

**Recommended: Backblaze B2 + Cloudflare CDN (zero egress cost combination)**

Backblaze B2 and Cloudflare are members of the [Bandwidth Alliance](https://www.cloudflare.com/bandwidth-alliance/), meaning data transferred from B2 to Cloudflare's CDN incurs zero egress fees from Backblaze. Combined with Cloudflare's global edge network, this gives:

- B2 storage: ~$6/TB/month
- Cloudflare egress: $0 (covered by Bandwidth Alliance)
- Cloudflare CDN delivery: zero additional cost for cached ZIM files

**Alternative: Cloudflare R2**

R2 eliminates egress fees entirely (no alliance required) and uses the S3-compatible API. The tradeoff is that R2 has no free tier for storage beyond 10 GB, while B2 includes 10 GB free. At open-repo's scale (a few GB of ZIM files), either is viable. R2 is slightly simpler operationally (no CDN configuration needed — R2 behind a Cloudflare zone delivers via the global edge automatically).

**For a community open-source project with minimal budget, the practical recommendation is:**
1. Phase 5 MVP: Cloudflare R2 (simplest setup, zero egress, free 10 GB tier covers early-stage exports)
2. Scale: migrate to B2 + Cloudflare if total storage exceeds 50 GB (lower storage cost per GB)

**Do not use AWS S3** for public ZIM distribution. Egress fees for a 2 GB file downloaded 10,000 times would cost approximately $180 in data transfer. This is not acceptable for a public open-source project.

### 3.2 Download URL Architecture

Three URL patterns should be supported:

**1. Permanent latest URL (for documentation and bookmarks):**
```
https://exports.open-repo.example.org/zim/open-repo_en_nopic_latest.zim
```
This resolves to a redirect (`HTTP 302`) pointing to the actual versioned file. The redirect target changes when a new export is released. The file itself is never overwritten — old versions remain accessible at their versioned URLs during the retention window.

**2. Versioned direct URL (stable, CDN-cacheable):**
```
https://exports.open-repo.example.org/zim/open-repo_en_nopic_2026-04.zim
```
This URL never changes for a given file. It can be cached aggressively by CDN (`Cache-Control: public, max-age=2592000`). Appropriate for torrent web seeds and mirror links.

**3. Pre-signed URL (for access control or analytics):**
If the ZIM bucket is private, the export API generates time-limited pre-signed URLs (24-hour expiry recommended). S3-compatible pre-signed URLs support `Range` headers, enabling resumable downloads even when signed. The URL includes an expiry timestamp in the query string, so the download continues even if the expiry passes during an active download.

### 3.3 Resumable Download Support

Large ZIM files (1–10 GB) must support resumable downloads. HTTP `Range` requests are how download managers, wget, aria2, and mobile browsers resume interrupted downloads. The implementation requirements:

**Server-side (object storage):** Both B2 and R2 support `Range` requests natively. If the export service proxies downloads through its own API (rather than redirecting to the CDN URL), the Python response must set:

```python
# FastAPI example for range-aware streaming
from fastapi.responses import StreamingResponse
import boto3

async def stream_zim(filename: str, range_header: str | None):
    s3_kwargs = {"Bucket": bucket, "Key": f"zim/{filename}"}
    if range_header:
        s3_kwargs["Range"] = range_header
    
    response = s3_client.get_object(**s3_kwargs)
    
    status_code = 206 if range_header else 200
    headers = {
        "Content-Type": "application/octet-stream",
        "Content-Disposition": f'attachment; filename="{filename}"',
        "Accept-Ranges": "bytes",
        "Content-Length": str(response["ContentLength"]),
    }
    if range_header:
        headers["Content-Range"] = response["ResponseMetadata"]["HTTPHeaders"]["content-range"]
    
    return StreamingResponse(
        response["Body"].iter_chunks(),
        status_code=status_code,
        headers=headers,
    )
```

**For most deployments, the recommended architecture is to redirect to the CDN URL directly** (the export API returns a redirect, the user's client talks directly to the CDN). This avoids the export service becoming a bottleneck for large-file transfers. CDN-served ZIM files already support `Range` headers.

### 3.4 Checksums and Download Integrity

Every export entry in the catalog must include a SHA-256 checksum. This allows users to verify the downloaded file has not been corrupted in transit:

```python
import hashlib

def compute_sha256(filepath: str) -> str:
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()
```

The checksum should be:
- Stored in the `zim_exports` table at generation time.
- Included in the export catalog API response (JSON).
- Available as a sidecar file at `{filename}.sha256` alongside the ZIM file in object storage (standard practice for open-source distributions, as used by Apache, Linux kernel, etc.).

### 3.5 BitTorrent Distribution (Phase 5.1)

BitTorrent is how Kiwix officially distributes Wikipedia-sized ZIM files. The `download.kiwix.org` server uses MirrorBrain for CDN distribution and publishes `.torrent` files alongside each ZIM. The `kiwix-seeder` tool then allows community members to automatically seed any subset of the Kiwix catalog.

For open-repo, BitTorrent distribution is a Phase 5.1 item (after the direct-download path is stable). The implementation path is:

1. Generate a `.torrent` file for each ZIM export using any torrent creation library (`torrentool` for Python).
2. Include the CDN URL as a web seed in the torrent (users without peers can fall back to HTTP).
3. Publish the `.torrent` file alongside the ZIM in object storage.
4. Document how community operators can run `kiwix-seeder` or a standard BitTorrent client to help seed open-repo exports.

This is low-effort, high-value for distribution resilience — the torrent infrastructure means the exports remain downloadable even if the open-repo CDN goes down.

---

## 4. OPDS Catalog Integration

### 4.1 What OPDS Is

OPDS (Open Publication Distribution System) is an Atom-based XML catalog format for discovering and downloading ebooks and media. Kiwix adopted OPDS v1.2 as the protocol for its in-app library browser. When a user opens the Kiwix app and browses the "Online Library," they are fetching the OPDS feed from `library.kiwix.org`.

A third-party content provider that publishes a valid OPDS feed can be added to Kiwix's official catalog, making its ZIM files discoverable from within every Kiwix app — Android, iOS, desktop — without users needing to know the download URL.

### 4.2 The kiwix-serve OPDS API (Self-Hosted)

When open-repo operators run `kiwix-serve` locally (the institutional use case), it auto-generates an OPDS feed at `/catalog/v2/root.xml` based on the loaded ZIM files. The endpoints:

| Endpoint | Purpose |
|---|---|
| `/catalog/v2/root.xml` | Root catalog with navigation links |
| `/catalog/v2/entries` | Paginated list of all ZIM files (acquisition feed) |
| `/catalog/v2/entry/{uuid}` | Single entry by UUID |
| `/catalog/v2/categories` | Navigation by category |
| `/catalog/v2/languages` | Navigation by language |
| `/catalog/v2/searchdescription.xml` | OpenSearch description for catalog search |

The `uuid` in these URLs is the ZIM file's internal UUID, which is embedded in the ZIM header at creation time by python-libzim. This UUID must be stable across versions of the same ZIM (i.e., the `open-repo_en_nopic` UUID should be consistent across monthly exports so that Kiwix apps can recognise an update to the same content).

**Implementation note**: python-libzim generates a random UUID for each `Creator` instance by default. To maintain a stable UUID per flavour, store the UUID in the export database and pass it back to the next export run:

```python
import uuid

# At export job start:
existing = db.query(ZimExport).filter_by(name=name, flavour=flavour, is_current=True).first()
zim_uuid = existing.zim_uuid if existing else str(uuid.uuid4())

# Pass to Creator (python-libzim supports uuid parameter):
with Creator(output_path).config_indexing(True, "eng") as creator:
    creator.set_uuid(zim_uuid)
    # ... add items
```

Verify whether the current python-libzim version exposes `set_uuid()` — if not, the UUID will be auto-generated and should be read back from the ZIM header after creation and stored for the next run.

### 4.3 Open-Repo's Public OPDS Endpoint

Open-repo nodes should publish their own OPDS catalog at:

```
https://{node-url}/opds/v2/root.xml
```

This is a FastAPI endpoint that generates OPDS-compliant XML describing all available ZIM exports. A minimal valid OPDS root document:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opds="http://opds-spec.org/2010/catalog"
      xmlns:dc="http://purl.org/dc/terms/"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">
  <id>urn:uuid:{node-uuid}</id>
  <title>Open-Repo Offline Library Catalog</title>
  <updated>2026-04-27T00:00:00Z</updated>
  <author>
    <name>Open-Repo</name>
    <uri>https://{node-url}</uri>
  </author>
  <link rel="self" type="application/atom+xml;profile=opds-catalog;kind=navigation"
        href="/opds/v2/root.xml"/>
  <link rel="start" type="application/atom+xml;profile=opds-catalog;kind=navigation"
        href="/opds/v2/root.xml"/>
  <link rel="search" type="application/opensearchdescription+xml"
        href="/opds/v2/searchdescription.xml"/>
  
  <entry>
    <title>All Offline Exports</title>
    <id>urn:uuid:{node-uuid}:all</id>
    <updated>2026-04-27T00:00:00Z</updated>
    <link rel="subsection"
          type="application/atom+xml;profile=opds-catalog;kind=acquisition"
          href="/opds/v2/entries"/>
  </entry>
</feed>
```

The `/opds/v2/entries` endpoint returns the acquisition feed — one `<entry>` per available ZIM export. Each entry includes the download link, file size, language, and illustration URL.

### 4.4 Submitting to the Official Kiwix Catalog

To have open-repo's exports appear in the Kiwix in-app library browser (the most valuable discoverability surface):

1. Submit a ZIM request on the [openzim/zim-requests](https://github.com/openzim/zim-requests) GitHub repository. This is the official process for requesting a new ZIM to be added to the Zimfarm/catalog pipeline. The request describes the content, proposes a scraper recipe, and the openZIM team reviews it.

2. Alternatively, after the self-hosted export pipeline is stable and producing validated ZIM files, contact the Kiwix/openZIM team directly to arrange catalog inclusion without requiring Zimfarm hosting. This is the appropriate path for open-repo since the project generates its own ZIM files rather than relying on Zimfarm workers.

**Practical first step**: Once the first production-quality ZIM file passes `zimcheck` and has been downloaded and tested in Kiwix apps, open a GitHub issue at `openzim/zim-requests` referencing the OPDS endpoint. The timeline from request to catalog inclusion is typically 24–48 hours for active scrapers.

### 4.5 OPDS in the Kiwix Android App — Version Compatibility Note

Kiwix Android versions since approximately 2023 require that externally-downloaded ZIM files be placed in a Kiwix-controlled directory when installed via the Play Store (due to Android 11+ restrictions). The **full (F-Droid) version** of the Kiwix Android app can open ZIM files from any location via the file picker.

Practical implication for open-repo's user documentation: Users on Android should be directed to either the full Kiwix APK (available from kiwix.org or F-Droid) or told that they can access open-repo's exports by tapping "Open file" and navigating to their Downloads folder after downloading via browser. The in-app catalog path (where Kiwix displays open-repo's library and handles download internally) works with both variants and is the preferred UX.

---

## 5. Offline Search — Xapian Index Quality Strategy

### 5.1 What the Embedded Index Contains

When `creator.config_indexing(True, "eng")` is set, python-libzim builds a Xapian full-text search database during ZIM creation and embeds it as internal ZIM entries. The index is built from the `title` and content text of every item added to the Creator. It is not built from raw HTML — libzim extracts text from the HTML content provider before indexing, stripping tags.

This means: the quality of offline search results directly depends on the quality of the HTML rendered for each entry. If an article's HTML contains navigation elements, breadcrumbs, and boilerplate mixed with the main content, the search index will be polluted with irrelevant terms.

### 5.2 HTML Rendering Recommendations for Search Quality

Each knowledge entry's HTML should be rendered with search index quality in mind:

1. **Separate the `<main>` content from navigation and chrome.** The rendered HTML for ZIM entries should contain only the article body, not the site header, footer, related links, or breadcrumbs. These add noise to the Xapian index and degrade search precision.

2. **Put the most important terms in the `<title>` and first paragraph.** Xapian ranks title matches higher than body matches. Ensure the `<title>` element matches the `get_title()` return from the `Item` subclass. The first paragraph should include the primary subject terms.

3. **Include alt text for images.** Image alt attributes are indexed as text. Meaningful alt text (describing the procedure step, the component name) improves recall for searches like "biosand filter sand layer."

4. **Render multilingual content with language-tagged spans.** If an article has content in both English and Spanish, wrap each section in `<span lang="en">` and `<span lang="es">`. This does not affect single-language Xapian indexing but improves future multi-language support.

5. **Include structured metadata as hidden text.** Tags, categories, and domain labels that don't appear in the visible article body can be added in a `<meta name="keywords">` tag or in a visually hidden `<div>`. Xapian will index them, improving tag-based recall.

### 5.3 Title Indexing — The `get_title()` Contract

In python-libzim, the `get_title()` method of an `Item` subclass controls both the article's display title and its primary search term. Items without a title are not included in the title search index. Every open-repo content entry must return a non-empty, meaningful title string from `get_title()`. This is the most important single factor for search quality in the resulting ZIM.

### 5.4 Index Warming for kiwix-serve Deployments

For institutional deployments running kiwix-serve, the first Xapian search against a cold ZIM takes approximately 7–8 seconds as the index is read from disk. Subsequent searches in the warm cache take 0.1–1.5 seconds.

Recommended: add a startup warmup call to kiwix-serve's setup script that issues a dummy search query immediately after startup. This pre-warms the Xapian index into the OS page cache before real users hit the service:

```bash
# In startup script, after kiwix-serve is healthy:
curl -s "http://localhost:8080/search?pattern=water" > /dev/null
echo "Search index warmed"
```

---

## 6. Federation Integration — ZIM Exports Across Nodes

### 6.1 The Gap Between Phase 4 Federation and Phase 5 Export

Phase 4 establishes ActivityPub-based content sync between nodes. Every item created on Node A propagates to Node B. Node B's local database therefore contains a federated superset of content — its own items plus those received from federation partners.

Phase 5 must decide: when Node B generates a ZIM file, does it export only its own content, or does it also export federated content from Node A?

**Recommended answer: each node exports its own authoritative content by default, with an opt-in federated export.**

Rationale:
- License and attribution: federated content from Node A carries Node A's attribution and may have different licensing. Including it in Node B's ZIM without explicit tracking creates attribution problems.
- Quality control: Node B has not necessarily validated Node A's content to its own standards.
- Size: a full federated export grows with the network. A node federating with 10 partners could produce a ZIM 10x larger than its own content.

**Implementation: two export scopes, controlled by `ExportConfig`:**

```python
class ExportScope(str, Enum):
    LOCAL_ONLY = "local"         # Items authored or approved by this node
    FEDERATED = "federated"      # All content in the local DB including received items
    DOMAIN = "domain"            # Filtered to a single knowledge domain
    TAG = "tag"                  # Filtered by tag

class ExportConfig(BaseModel):
    scope: ExportScope
    scope_value: str | None      # Domain name or tag for filtered scopes
    include_federated: bool = False  # Override: include federated items in any scope
    language: str = "eng"
    include_images: bool = False
    flavour: str = "all"
```

A `LOCAL_ONLY` export is the safe default. A `FEDERATED` export includes attribution metadata for each item indicating which node it originated from — this must be rendered in the HTML template.

### 6.2 Attribution in ZIM Exports for Federated Content

When a federated item appears in a ZIM export, the article HTML must include:

```html
<footer class="attribution">
  <p>Originally published on <a href="{source_node_url}">{source_node_name}</a>
  under <a href="{license_url}">{license_name}</a>.</p>
</footer>
```

This footer is included in the Xapian index (as low-relevance terms). It ensures that users who encounter federated content in the offline archive can trace it back to its origin.

### 6.3 Cross-Node Export Discovery via OPDS

Each federated node publishes its own OPDS catalog at `/opds/v2/root.xml`. A user with kiwix-serve can add multiple OPDS sources by configuring separate library XML files. The export catalog API (`GET /api/exports`) should return links to peer nodes' OPDS endpoints for users who want a broader content library:

```json
{
  "exports": [ ... ],
  "federation_sources": [
    {
      "node_name": "Node B",
      "node_url": "https://node-b.example.com",
      "opds_url": "https://node-b.example.com/opds/v2/root.xml"
    }
  ]
}
```

This is purely informational — it helps users discover that the network has more content than a single node's export, without requiring central coordination.

---

## 7. Update and Synchronisation Mechanisms for Offline Copies

### 7.1 Notification for Available Updates

Users who have downloaded a ZIM file should be notified when a newer version is available. Three mechanisms, in order of implementation priority:

**A. Export Catalog API (polling).** The export catalog API returns the `generated_at` timestamp and `period` for the current version. A user or script can periodically poll `GET /api/exports?name=open-repo_en_nopic` and compare the `period` field against what they downloaded. This is the lowest-effort mechanism and suitable for advanced users and institutional deployments.

**B. RSS/Atom feed for new exports.** The OPDS catalog is already an Atom feed. Adding an `<updated>` element that changes whenever a new export is published means any RSS reader can monitor for updates. This is a no-code addition to the existing OPDS endpoint.

**C. Email or webhook notification.** Advanced users (institutional deployments) can register a webhook URL at `POST /api/exports/subscribe` to receive a POST notification when a new export matching their criteria (flavour, language) is released. This is a Phase 5.1 feature.

### 7.2 Update Guidance for Kiwix Desktop

Kiwix desktop (all platforms) does not have an automatic update mechanism for ZIM files. The user must:
1. Download the new ZIM file.
2. Remove the old ZIM from Kiwix's library (or replace the file in the ZIM directory).
3. Kiwix will detect the new file on next launch or library refresh.

Open-repo's documentation should provide explicit steps for each platform (Windows, macOS, Linux) because this flow is not obvious to non-technical users. The documentation should also explain that the old ZIM file remains valid and can be kept as an archive.

### 7.3 Update Guidance for kiwix-serve Institutional Deployments

For institutions running kiwix-serve with the `--monitorLibrary` flag enabled, the update flow is:

1. Download the new ZIM file to the ZIM directory.
2. Update the library XML file to reference the new filename.
3. kiwix-serve detects the library file change (via inotify on Linux) and reloads without restart.
4. Remove the old ZIM file after confirming the new one is serving correctly.

The `--monitorLibrary` flag is specifically designed for this zero-downtime update pattern. Open-repo should document the exact steps and provide an optional update script (`update-open-repo-zim.sh`) that automates the download, verification (sha256sum check), library XML update, and old file removal.

### 7.4 kiwix-seeder for Community Seeding

Open-repo can publish a `kiwix-seeder` filter configuration that allows community members to automatically seed open-repo's ZIM exports via BitTorrent. The seeder connects to open-repo's OPDS catalog, identifies matching ZIM files, and seeds them. As more community members run the seeder, the BitTorrent distribution becomes more resilient.

Configuration for open-repo's seeder filter:
```yaml
# kiwix-seeder filter for open-repo content
catalog_url: https://open-repo.example.org/opds/v2/entries
filters:
  name_prefix: "open-repo"
  max_file_size: 5GB     # Exclude very large exports
max_storage: 20GB
keep: 60d               # Keep old versions for 60 days to support slow downloaders
```

This is a Phase 5.1 item requiring BitTorrent infrastructure (see section 3.5).

---

## 8. End-to-End Export Flow Diagram

```
[Scheduled trigger: weekly cron / manual API call]
         │
         ▼
ExportJob.run(config: ExportConfig)
         │
         ├── 1. Query DB for content matching scope
         │       (local-only OR federated, by domain/tag/language)
         │
         ├── 2. Resolve Name + Period + UUID
         │       Name:   "open-repo_en_nopic"
         │       Period: "2026-04" (or "2026-04a" if same month)
         │       UUID:   stable per-flavour UUID from previous export (or new)
         │
         ├── 3. Create temp file path: /tmp/{uuid}.zim.partial
         │
         ├── 4. Open python-libzim Creator
         │       - config_indexing(True, "eng")
         │       - set_uuid(uuid)
         │       - set_mainpath("index")
         │       - add_metadata(Name, Title, Description, Language, ...)
         │       - add_illustration(48, icon_bytes)
         │
         ├── 5. Stream items through ZimWriter
         │       for item in content_stream(config):
         │           creator.add_item(ArticleItem(
         │               path=item.slug,
         │               title=item.title,
         │               html=render_html(item)
         │           ))
         │
         ├── 6. Creator.close() → ZIM file written
         │
         ├── 7. Run zimcheck(output_path)
         │       → FAIL: mark export as 'error', log, notify
         │       → PASS: continue
         │
         ├── 8. Compute SHA-256 checksum
         │
         ├── 9. Upload to object storage (B2/R2)
         │       Key: "zim/{filename}"
         │       Sidecar: "zim/{filename}.sha256"
         │
         ├── 10. Insert zim_exports row (status='available', is_current=TRUE)
         │         Update previous row for same name+flavour: is_current=FALSE, status='superseded'
         │
         ├── 11. Apply retention policy (delete eligible superseded exports)
         │
         ├── 12. Update OPDS catalog (auto-derived from zim_exports table)
         │
         └── 13. Emit export.completed event (for webhooks / RSS / notification)
```

---

## 9. Testing Strategy — Phase 5

### Unit Tests

| Test | What it verifies |
|---|---|
| `test_zim_metadata_completeness` | All mandatory metadata fields present and non-empty |
| `test_naming_convention` | `Name` field matches the regex `[a-z0-9\-\.]+_[a-z]{3}_[a-z0-9\-]+` |
| `test_period_generation` | Period is `YYYY-MM` format with correct same-month suffix logic |
| `test_html_rendering_no_external_deps` | Rendered HTML has no `<link rel="stylesheet" href="http...">` or external JS |
| `test_export_config_scope` | LOCAL_ONLY scope excludes items with `is_local=False` |
| `test_uuid_stability` | Second export run for same flavour reuses UUID from first |

### Integration Tests

| Test | What it verifies |
|---|---|
| `test_zim_roundtrip_small` | Write 50 items → `zimcheck` passes → read back with `libzim.reader.Archive` → article count matches |
| `test_search_index_populated` | After write, `Archive.search("water")` returns at least one result |
| `test_illustration_present` | `Archive.get_illustration_blob(48)` returns non-empty bytes |
| `test_sha256_matches` | Checksum stored in DB matches `sha256sum` of the file on disk |
| `test_retention_policy` | After 4 monthly exports, only 2 superseded + current are retained |
| `test_opds_feed_valid_xml` | `GET /opds/v2/root.xml` returns well-formed XML with correct namespaces |
| `test_opds_entry_has_download_link` | Each OPDS entry has an `application/x-zim` acquisition link |
| `test_range_request` | HTTP Range request to download endpoint returns 206 with correct bytes |

### End-to-End Tests

| Test | What it verifies |
|---|---|
| `test_kiwix_serve_can_serve` | Generate ZIM → launch kiwix-serve → GET to kiwix-serve returns article HTML |
| `test_opds_discoverable_in_kiwix` | kiwix-serve configured with open-repo OPDS URL → catalog entries appear |
| `test_federated_attribution` | Federated export includes attribution footer in HTML for remote-origin items |

---

## 10. Dependency Additions for Phase 5

The following are additions to open-repo's dependency surface, beyond what the Phase 5 prior research documented:

| Dependency | Purpose | Phase |
|---|---|---|
| `boto3` or `cloudflare` Python SDK | Object storage upload to R2/B2 | 5 MVP |
| `jinja2` (confirm already present) | HTML template rendering for ZIM articles | 5 MVP |
| `torrentool` (PyPI) | Generate `.torrent` files for BitTorrent distribution | 5.1 |
| `feedgen` (PyPI) | Generate OPDS/Atom XML feed | 5 MVP |
| `httpx` (likely already present from Phase 4) | Webhook notification delivery | 5.1 |
| `celery-beat` or APScheduler | Scheduled weekly/monthly export triggers | 5 MVP |

---

## 11. Effort Estimate — Additive to Prior Blueprint

The prior document estimated 15–23 days for the core export pipeline. This document adds four additional work areas:

| Area | Estimated Days |
|---|---|
| OPDS endpoint (FastAPI + feedgen, both directions) | 2–3 days |
| CDN/object storage setup (R2 or B2 + Cloudflare) | 1–2 days |
| Export versioning DB schema + retention policy | 1 day |
| Federated attribution in ZIM HTML | 1–2 days |
| Update notification (RSS + API polling) | 1 day |
| User documentation (3 platforms × 2 use cases) | 1–2 days |
| Extended test coverage (OPDS, range requests, retention) | 2–3 days |
| **Additive total** | **9–14 days** |

**Revised total estimate (including prior blueprint): 24–37 days for complete Phase 5.**

The wide range reflects the unknown complexity of the HTML rendering layer and whether the existing Jinja2 templates can be adapted with minimal changes for the offline context.

---

## 12. Key Risks — Additions to Prior Risk Register

| Risk | Impact | Mitigation |
|---|---|---|
| UUID instability across export runs | Kiwix app treats each export as a different book, no update path | Store UUID in `zim_exports` table; pass to Creator explicitly |
| OPDS XML namespace errors | Kiwix rejects the feed as invalid | Validate OPDS XML with the `feedgen` library's built-in validation; test against kiwix-serve in CI |
| Object storage cost spike (large exports, high download volume) | Budget overrun | Start with R2 (zero egress); monitor egress; add BitTorrent seeding before heavy traffic |
| Android Kiwix Play Store restrictions | Users can't open downloaded ZIM files | Document the full/F-Droid Kiwix variant; provide in-app OPDS path as primary UX |
| Federated attribution omitted | License violation for CC-BY content from partner nodes | Fail the export job if any federated item lacks attribution metadata; unit test this path |

---

## Sources

- [openZIM ZIM Naming Convention](https://wiki.openzim.org/wiki/ZIM_Naming_Convention)
- [openZIM Metadata Specification](https://openzim.org/wiki/Metadata)
- [openZIM ZIM Updates v2 (2024 period format)](https://wiki.openzim.org/wiki/ZIM_Updates)
- [kiwix-tools OPDS documentation](https://kiwix-tools.readthedocs.io/en/latest/kiwix-serve.html)
- [OPDS Catalog Spec v1.2 — Kiwix wiki](https://wiki.kiwix.org/wiki/OPDS)
- [kiwix/seeder — BitTorrent seeding tool](https://github.com/kiwix/seeder)
- [openzim/zim-requests — ZIM catalog submission process](https://github.com/openzim/zim-requests)
- [openzim/zimfarm](https://github.com/openzim/zimfarm)
- [Kiwix/ZIM incremental updates — MediaWiki](https://www.mediawiki.org/wiki/Kiwix/ZIM_incremental_updates)
- [zimdiff/zimpatch issue tracker — Phabricator T49406](https://phabricator.wikimedia.org/T49406)
- [LongDescription mandatory status — issue #408](https://github.com/openzim/zim-tools/issues/408)
- [libzim Xapian speed-up issue — issue #617](https://github.com/openzim/libzim/issues/617)
- [Backblaze B2 + Cloudflare free egress — Bandwidth Alliance](https://www.backblaze.com/docs/cloud-storage-deliver-public-backblaze-b2-content-through-cloudflare-cdn)
- [Cloudflare R2 overview](https://www.cloudflare.com/developer-platform/products/r2/)
- [Backblaze B2 vs Cloudflare R2 comparison](https://www.taloflow.ai/guides/comparisons/backblazeb2-vs-cloudflarer2-object-storage)
- [S3 Range download with pre-signed URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html)
- [Zimi — modern ZIM server with JSON API](https://github.com/epheterson/zimi)
- [Kiwix Android app — Play Store variant restrictions](https://github.com/kiwix/kiwix-android)
- [python-libzim — ReadTheDocs](https://python-libzim.readthedocs.io/)
- [openZIM GitHub organization](https://github.com/openzim)
