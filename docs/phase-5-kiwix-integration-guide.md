---
title: "Phase 5: Kiwix Integration Guide"
project: open-repo
phase: 5
status: implementation-ready
date: 2026-04-28
author: research-agent
confidence: high
prerequisites:
  - phase-5-kiwix-architecture.md
  - phase-5-offline-export-architecture.md
tags: [kiwix, zim, openzim, python-libzim, opds, cdn, offline-export, integration]
---

# Phase 5: Kiwix Integration Guide

This document is the hands-on implementation reference for Kiwix integration in Phase 5. The prior
research documents (`phase-5-kiwix-architecture.md` and `phase-5-offline-export-architecture.md`)
cover the why; this guide covers the how — installation, version constraints, metadata requirements,
naming conventions, OPDS catalog generation, CDN deployment, and integration points with the Phase 4
federation service. Engineers implementing Phase 5 should read this document before writing any code.

---

## 1. Kiwix Ecosystem Overview

### 1.1 Components Relevant to Open-Repo

The Kiwix ecosystem has five layers that open-repo will interact with directly or indirectly:

**ZIM File Format** — The binary container format that holds all content. A single ZIM file is a
complete, self-contained offline library: it contains articles, images, stylesheets, a full-text
search index (Xapian), and metadata. ZIM files are random-access: a reader can serve any individual
article without decompressing the entire file. Format spec: https://wiki.openzim.org/wiki/ZIM_file_format

**python-libzim** — The Python binding for the C++ libzim library. This is the primary tool for
generating ZIM files from open-repo's backend. PyPI package: `libzim`. Pre-built wheels for Linux
(x86_64, armhf, aarch64), macOS (x86_64, arm64), Windows (x64). No Rust or C++ build required in
CI.

**Kiwix Reader** — The application users install to open ZIM files. Available on Android, iOS,
macOS, Windows, Linux, and as a browser extension. The reader handles ZIM file indexing, search,
and navigation.

**kiwix-serve** — A lightweight HTTP server that reads ZIM files and serves them as a local web
application. Institutional users (schools, libraries, field offices) run kiwix-serve so any device
on the local network can browse the content via a standard web browser. Docker deployment is one
command: `docker run -v /path/to/zims:/data -p 8080:8080 ghcr.io/kiwix/kiwix-serve '*.zim'`

**OPDS Catalog** — The Atom-based XML feed format Kiwix uses for its in-app library browser. When
a user taps "Online Library" in the Kiwix Android app, they are fetching an OPDS catalog from
`library.kiwix.org`. Open-repo will publish its own OPDS endpoint and eventually request inclusion
in the official catalog.

### 1.2 What Open-Repo Builds vs. What It Consumes

Open-repo **builds**: python-libzim-based export pipeline, ZIM files, OPDS endpoint, CDN-hosted
distribution.

Open-repo **consumes**: Kiwix readers (downstream users install these), kiwix-serve (institutional
deployments), `zimcheck` (post-export validation, system binary), `zim-tools` (debugging).

---

## 2. python-libzim Installation and Version Constraints

### 2.1 Current Version and Installation

As of 2026, the current stable series is **3.x** (tracking libzim 9.x internally). The Python
package name on PyPI is `libzim` (not `python-libzim`).

```bash
# Add to project dependencies
uv add libzim

# Or install directly
uv pip install libzim
```

The package requires Python >= 3.10. Open-repo's backend already specifies `requires-python =
">=3.10"` in `pyproject.toml`, so there is no conflict.

### 2.2 Pre-Built Wheel Availability

Wheels are published for:
- `manylinux2014_x86_64` (standard Linux amd64 — the production deployment target)
- `manylinux2014_aarch64` (ARM64 Linux — Raspberry Pi 4+, AWS Graviton)
- `manylinux2014_armhf` (32-bit ARM)
- `macosx_12_0_x86_64` and `macosx_12_0_arm64` (macOS Intel and Apple Silicon)
- `win_amd64` (Windows)

If no wheel matches the CI environment, pip will attempt to build from source, which requires the
`libzim` C++ library and development headers. In Docker-based CI, use the official openzim base
image to guarantee wheel availability:

```dockerfile
FROM openzim/zim-tools:latest AS builder
# libzim and zimcheck are already present
RUN pip install libzim
```

### 2.3 Version Pinning Strategy

Pin to a minor version but not a patch version. The 3.x API is stable; only patch versions fix
bugs. Breaking API changes between major versions (2.x to 3.x) were significant (the `Creator`
context manager API changed).

In `pyproject.toml`:
```toml
dependencies = [
    # ... existing dependencies
    "libzim>=3.2,<4.0",
]
```

### 2.4 Known API Surface for Open-Repo's Use Case

The complete python-libzim writer API open-repo will use:

```python
from libzim.writer import Creator, Item, StringProvider, FileProvider, Hint

# Creator: context manager, one per ZIM file
with Creator("output.zim") as creator:
    creator.config_indexing(True, "eng")  # Enable full-text search
    creator.set_mainpath("index")          # Path of the home/index article
    creator.add_metadata("Title", "...")   # Metadata fields (see section 3)
    creator.add_illustration(48, bytes)    # 48x48 PNG icon
    creator.add_item(item)                 # Add an article or asset

# Item: abstract base class, subclass for each content type
class ArticleItem(Item):
    def get_path(self) -> str: ...       # URL path within ZIM
    def get_title(self) -> str: ...      # Display title (also indexed)
    def get_mimetype(self) -> str: ...   # e.g. "text/html"
    def get_hints(self) -> dict: ...     # {Hint.FRONT_ARTICLE: True}
    def get_contentprovider(self): ...   # StringProvider or FileProvider

# StringProvider: in-memory content
StringProvider(content="<html>...</html>")

# FileProvider: file-backed content (for large assets)
FileProvider(filepath="/path/to/asset.png")
```

**Threading constraint**: The `Creator` API is not thread-safe. Do not call `add_item()` from
multiple threads concurrently. Use a single thread or protect with a lock.

---

## 3. ZIM Metadata Structure

### 3.1 Mandatory Fields

These fields must be present or `zimcheck` will fail:

| Field | Open-Repo Value | Notes |
|---|---|---|
| `Title` | `"Open-Repo: {Scope} (English)"` | Max 30 chars recommended |
| `Description` | `"Offline practical knowledge library"` | Max 80 chars |
| `Language` | `"eng"` | ISO 639-3 code |
| `Creator` | `"Open-Repo Community"` | Content author |
| `Publisher` | `"Open-Repo"` | Who generated this ZIM |
| `Date` | `"2026-04-28"` | ISO 8601, generated at export time |
| `Name` | `"open-repo_en_nopic"` | See naming convention below |
| `Illustration_48x48` | `<PNG bytes>` | Must be exactly 48x48 pixels |

### 3.2 Recommended Optional Fields

Include these for catalog quality and discoverability:

| Field | Value |
|---|---|
| `Flavour` | `"nopic"`, `"all"`, `"agriculture"`, etc. |
| `Tags` | `"offline;practical-knowledge;procedures"` |
| `LongDescription` | Extended paragraph (max 4000 chars) |
| `Scraper` | `"open-repo-exporter/1.0"` |
| `Source` | Node's base URL (e.g., `"https://node.example.org"`) |

### 3.3 Setting Metadata in Python

```python
with Creator("output.zim") as creator:
    creator.add_metadata("Title", "Open-Repo: Full Library (English)")
    creator.add_metadata("Description", "Offline practical knowledge library")
    creator.add_metadata("Language", "eng")
    creator.add_metadata("Creator", "Open-Repo Community")
    creator.add_metadata("Publisher", "Open-Repo")
    creator.add_metadata("Date", datetime.utcnow().strftime("%Y-%m-%d"))
    creator.add_metadata("Name", "open-repo_en_nopic")
    creator.add_metadata("Flavour", "nopic")
    creator.add_metadata("Tags", "offline;practical-knowledge;procedures")
    creator.add_metadata("Source", "https://node.example.org")
    creator.add_metadata("Scraper", "open-repo-exporter/1.0")

    # Illustration: must be exactly 48x48 PNG
    with open("assets/open-repo-icon-48x48.png", "rb") as f:
        creator.add_illustration(48, f.read())
```

---

## 4. ZIM Naming Convention

### 4.1 The OpenZIM Standard

The `Name` metadata field and ZIM filename follow the openZIM naming convention. Structure:

```
{publisher}_{language}_{flavour}_{period}.zim
```

Rules:
- All lowercase, alphanumerics, hyphens, and periods only: `[a-z0-9\-\.]+`
- Underscore is the **part separator** — never use underscores within a part
- `{publisher}`: derived from the content domain (e.g., `open-repo`)
- `{language}`: ISO 639-3 code or `all` for mixed-language
- `{flavour}`: scope identifier (`all`, `nopic`, `agriculture`, `recipes`, `mini`)
- `{period}`: `YYYY-MM`, with `a`/`b` suffix for same-month re-exports

The `Name` metadata field is the filename **without the period and `.zim` suffix**:

```python
name_metadata = "open-repo_en_nopic"    # stored in ZIM M/Name
period        = "2026-04"               # computed at export time
filename      = f"{name_metadata}_{period}.zim"  # open-repo_en_nopic_2026-04.zim
```

### 4.2 Flavour Definitions for Open-Repo

| Export Scope | Name Metadata | Flavour | Example Filename |
|---|---|---|---|
| Full library, no images | `open-repo_en_nopic` | `nopic` | `open-repo_en_nopic_2026-04.zim` |
| Full library, with images | `open-repo_en_all` | `all` | `open-repo_en_all_2026-04.zim` |
| Agriculture domain only | `open-repo_en_agriculture` | `agriculture` | `open-repo_en_agriculture_2026-04.zim` |
| Recipes domain only | `open-repo_en_recipes` | `recipes` | `open-repo_en_recipes_2026-04.zim` |
| Multilingual full | `open-repo_mul_all` | `all` | `open-repo_mul_all_2026-04.zim` |

**MVP recommendation**: implement `open-repo_en_nopic` first. Smallest file, fastest to generate,
most practical for low-bandwidth users. Add image-inclusive exports in Phase 5.1.

### 4.3 Period Suffix Logic

```python
def compute_period(existing_periods: list[str], now: datetime) -> str:
    """Compute the YYYY-MM period string with same-month suffix if needed."""
    base = now.strftime("%Y-%m")
    # Find all periods for this month already published
    same_month = [p for p in existing_periods if p.startswith(base)]
    if not same_month:
        return base
    # Add alphabetic suffix: 2026-04 -> 2026-04a -> 2026-04b
    last = sorted(same_month)[-1]
    if last == base:
        return f"{base}a"
    suffix = last[-1]
    return f"{base}{chr(ord(suffix) + 1)}"
```

---

## 5. Integration Points with the Phase 4 Federation Service

### 5.1 Data Model Assumptions

Phase 5 export code assumes the following from Phase 4's data model (based on `models.py` and
`PHASE_4_DESIGN.md`):

**ContentItem** (existing `content_items` table):
- `cid: str` — content hash, unique identifier
- `title: Dict[str, str]` — multilingual: `{"en": "Biosand Water Filter", "es": "..."}`
- `item_type: str` — one of: `procedure`, `recipe`, `schematic`, `plan`, `service-listing`
- `domain: str` — knowledge domain (e.g., `agriculture`, `recipes`, `electronics`)
- `license: str` — SPDX identifier (e.g., `CC-BY-4.0`)
- `content_jsonld: Dict` — full JSON-LD content object
- `source_url: Optional[str]` — attribution URL
- `created_at: datetime`

**FederationPartner** (from Phase 4 `PHASE_4_DESIGN.md`):
- `partner_url: str` — remote node URL
- `actor_url: str` — ActivityPub actor URL
- `federation_state: str` — `active` | `pending` | `suspended`

**Export scope flags** (to be added in Phase 5 migration):
- `is_local: bool` — whether the item was authored on this node (vs. received via federation)
- `federation_source_url: Optional[str]` — source node for federated items

### 5.2 Export API Contract

The export service will expose these endpoints (to be implemented in Phase 5):

```
POST /api/exports
    Body: ExportConfig (scope, flavour, language, include_images)
    Response: { job_id: str, status: "queued" }

GET /api/exports/{job_id}
    Response: { status: "generating"|"available"|"error", download_url: str|null, ... }

GET /api/exports
    Response: { exports: [ZimExportSummary, ...], federation_sources: [...] }
```

### 5.3 Content Query Interface for ZimWriter

The `ZimWriter` class (see `src/export/zim_writer.py`) accepts a content stream. The export
service must translate `ContentItem` database objects into this stream format:

```python
# ContentItem -> ZimWriter.add_article() mapping
writer.add_article(
    path=item.cid,                           # URL path in ZIM
    content=render_html_template(item),      # Rendered HTML
    article_type=item.item_type,
    language=item.content_jsonld.get("language", ["en"])[0]
)
```

The `render_html_template()` function must produce fully self-contained HTML with no external
dependencies — all CSS must be inline or embedded in `<style>` tags, no external JS references.

---

## 6. CDN Deployment Options

### 6.1 Cost Analysis: Cloudflare R2 vs Backblaze B2 vs AWS S3

For public, large-file distribution of ZIM archives (targeting low-bandwidth regions), the egress
cost model is the dominant factor. Open-source projects cannot absorb S3-level egress fees.

**Cloudflare R2 (Recommended for MVP)**

| Metric | Cost |
|---|---|
| Storage | $0.015/GB/month |
| Egress | $0 (zero egress fees — R2's primary value proposition) |
| Class A operations (write) | $4.50/million |
| Class B operations (read) | $0.36/million |
| Free tier | 10 GB storage, 1M Class A ops, 10M Class B ops/month |

At Phase 5 MVP scale (3-5 ZIM files, ~2-5 GB total), R2 storage costs less than $0.15/month with
zero egress. The free tier covers the initial months entirely. R2 uses the S3-compatible API, so
boto3 works with a custom endpoint URL.

**Backblaze B2 + Cloudflare CDN (Recommended at scale)**

B2 and Cloudflare are in the [Bandwidth Alliance](https://www.cloudflare.com/bandwidth-alliance/),
meaning traffic from B2 to Cloudflare CDN is zero egress cost from Backblaze's side.

| Metric | Cost |
|---|---|
| Storage | $6/TB/month ($0.006/GB) — 2.5x cheaper than R2 |
| Egress to Cloudflare | $0 (Bandwidth Alliance) |
| Egress to other destinations | $0.01/GB after 1 GB free/day |
| Free tier | 10 GB storage, 1 GB/day download free |

At scale (>50 GB of ZIM files), B2 + Cloudflare is significantly cheaper on storage costs.
Operational complexity is slightly higher (need to configure Cloudflare as CDN fronting B2).

**AWS S3 — Do Not Use for Public Distribution**

Egress: $0.09/GB after 100 GB/month free. A 2 GB ZIM downloaded 10,000 times = $1,800 in egress
alone. Not viable for an open-source community project.

### 6.2 Configuration Summary

For Phase 5 MVP, use **Cloudflare R2** with public bucket access. Configure:

```python
# boto3-compatible R2 client
import boto3
r2_client = boto3.client(
    "s3",
    endpoint_url="https://{account_id}.r2.cloudflarestorage.com",
    aws_access_key_id=settings.R2_ACCESS_KEY_ID,
    aws_secret_access_key=settings.R2_SECRET_ACCESS_KEY,
    region_name="auto",
)
```

ZIM files should be uploaded with:
```python
r2_client.upload_file(
    local_path,
    bucket_name,
    f"zim/{filename}",
    ExtraArgs={
        "ContentType": "application/x-zim",
        "CacheControl": "public, max-age=2592000, immutable",  # 30 days, immutable
    }
)
```

### 6.3 Public URL Patterns

Three URL tiers for ZIM distribution:

```
# Permanent latest (redirects, changes on each export):
https://exports.{node-domain}/zim/open-repo_en_nopic_latest.zim

# Versioned stable (never changes, cache forever):
https://exports.{node-domain}/zim/open-repo_en_nopic_2026-04.zim

# Checksum sidecar (download integrity):
https://exports.{node-domain}/zim/open-repo_en_nopic_2026-04.zim.sha256
```

---

## 7. OPDS Catalog Generation Strategy

### 7.1 feedgen Library

OPDS 1.2 is Atom-compatible XML. Python's `feedgen` library (PyPI: `feedgen`) generates valid Atom
feeds and is the correct tool for OPDS catalog generation in open-repo's backend.

```bash
uv add feedgen
```

The `opds_generator.py` module (see `src/export/opds_generator.py`) uses feedgen to build the OPDS
catalog from the `zim_exports` database table, regenerated after each successful export job.

### 7.2 Submission to the Official Kiwix Catalog

The path to appearing in Kiwix's in-app library browser (the highest-value discoverability
surface):

1. Generate the first production-quality ZIM export and validate it with `zimcheck`.
2. Open an issue at https://github.com/openzim/zim-requests with:
   - The `Name` metadata value (`open-repo_en_nopic`)
   - A download URL for the initial ZIM file
   - The OPDS endpoint URL (`https://{node}/opds/v2/root.xml`)
   - A description of the content and update schedule
3. The openZIM team reviews and adds the OPDS endpoint to the catalog index.
4. After catalog inclusion, open-repo's exports appear in Kiwix Android, iOS, and desktop without
   users needing to know the download URL.

Expected timeline from request to catalog inclusion: 1-5 business days for active scrapers with
validated ZIM output.

### 7.3 Self-Hosted OPDS Endpoint Structure

Open-repo nodes publish OPDS at `/opds/v2/root.xml`. The endpoint structure:

```
GET /opds/v2/root.xml        Navigation root
GET /opds/v2/entries         Acquisition feed (all available ZIM files)
GET /opds/v2/entry/{uuid}    Single ZIM entry by UUID
GET /opds/v2/searchdescription.xml  OpenSearch description
```

The acquisition feed entry for each ZIM includes:
- Download link with `application/x-zim` MIME type
- File size, SHA-256 checksum
- Language, illustration URL
- Version history (last 5 releases visible)

---

## 8. Offline Reader Distribution Paths

Three paths for users to get open-repo's ZIM files:

**Path 1: Direct download from open-repo node**
User visits the open-repo web UI, clicks "Download Offline Copy," selects a flavour, and downloads
the ZIM file. User then opens it in Kiwix desktop/mobile. Best for individual users.

**Path 2: Kiwix in-app catalog (after catalog submission)**
User opens the Kiwix app, browses the online library, finds "Open-Repo," and downloads from within
the app. Kiwix handles download resumption, integrity checking, and library management. Best UX for
non-technical users.

**Path 3: GitHub Releases (supplementary)**
Attach ZIM files to GitHub Releases as release assets. GitHub's CDN handles distribution; no
additional infrastructure needed. Useful for small exports (< 2 GB GitHub limit) and as a fallback
if CDN is down. ZIM files are immutable once published, making them a natural fit for release
assets.

For institutional kiwix-serve deployments, the operator downloads via any of the above paths and
runs: `docker run -v /path/to/zims:/data -p 8080:8080 ghcr.io/kiwix/kiwix-serve '*.zim'`

---

## Sources

- [openZIM ZIM Naming Convention](https://wiki.openzim.org/wiki/ZIM_Naming_Convention)
- [openZIM Metadata Specification](https://wiki.openzim.org/wiki/Metadata)
- [python-libzim ReadTheDocs](https://python-libzim.readthedocs.io/)
- [python-libzim GitHub](https://github.com/openzim/python-libzim)
- [feedgen PyPI](https://pypi.org/project/feedgen/)
- [Cloudflare R2 Pricing](https://developers.cloudflare.com/r2/pricing/)
- [Backblaze B2 Pricing](https://www.backblaze.com/b2/cloud-storage-pricing.html)
- [Bandwidth Alliance members](https://www.cloudflare.com/bandwidth-alliance/)
- [openzim/zim-requests](https://github.com/openzim/zim-requests)
- [OPDS Catalog Spec v1.2 on Kiwix wiki](https://wiki.kiwix.org/wiki/OPDS)
- [kiwix-serve Docker image](https://github.com/kiwix/kiwix-tools/blob/main/docker/server/README.md)
