---
title: "Phase 5: Export Strategy and Scoping"
project: open-repo
phase: 5
status: implementation-ready
date: 2026-04-28
author: research-agent
confidence: high
tags: [offline-export, zim, versioning, incremental, accessibility, storage, cdn]
---

# Phase 5: Export Strategy and Scoping

This document defines the three export variants, scoping rules, incremental update strategy,
content freeze policy, accessibility requirements, and storage/retention policy for open-repo's
ZIM-based offline export system. It is the authoritative reference for what gets included in each
export, how exports are named and versioned, and how old versions are cleaned up.

---

## 1. Three Export Variants

The Phase 4 federation data model stores `ContentItem` records with `item_type`, `domain`, and
`is_local` fields. Phase 5 defines three export variants built on top of this data model.

### Variant A: Full Export

**Purpose**: Complete offline snapshot of the entire open-repo knowledge library, including all
35+ knowledge domains, implementation architecture documentation, and activation guides.

**Content scope**:
- All `ContentItem` records where `is_local = True` (locally-authored content)
- All `domain` values included
- All `item_type` values: `procedure`, `recipe`, `schematic`, `plan`, `service-listing`
- Implementation architecture documentation (static Markdown converted to HTML)
- Domain overview pages (auto-generated from domain metadata)
- Top-level navigation (index page with domain browser)
- License and attribution pages
- Search index over all content (Xapian full-text)

**What is excluded from Full Export**:
- Federated content from partner nodes (included only in Federated Export)
- Dynamic content: live vote counts, real-time node status, user registration
- Administrative interfaces
- Node configuration or private metadata

**Estimated ZIM size**: 50-80 MB (text-only, `nopic` flavour); 200-500 MB (with images, `all`
flavour). These estimates are based on the Phase 4 data model with approximately 500-1,000 content
items across 35 domains. As content grows, expect linear scaling.

**ZIM naming**:
- `nopic` flavour: `open-repo_en_nopic_YYYY-MM.zim`
- `all` flavour: `open-repo_en_all_YYYY-MM.zim`

**Generation frequency**: Weekly (`nopic`), monthly (`all`).

### Variant B: Domain-Specific Export

**Purpose**: Single knowledge domain plus implementation architecture. Enables users who only care
about one topic (e.g., agriculture, water systems, electronics) to download a small, focused
offline library.

**Content scope**:
- All `ContentItem` records matching one `domain` value
- Implementation architecture documentation scoped to that domain
- Domain-specific navigation (no cross-domain links)
- Approximately 20-100 content items depending on domain maturity
- Search index over domain content only

**What is excluded**:
- Content from other domains
- Cross-domain references (replaced with "available in full export" stub pages)
- Administrative content

**Estimated ZIM size**: 5-10 MB (text-only). At this size, ZIM files are practical for users with
very limited storage (8 GB phone with other apps installed).

**ZIM naming**: `open-repo_en_{domain}_YYYY-MM.zim`
- Example: `open-repo_en_agriculture_2026-04.zim`

**Domain flavour registry** (values used in ZIM `Flavour` metadata and filename):

| Domain | Flavour | Description |
|---|---|---|
| Agriculture | `agriculture` | Farming, soil, crop management |
| Water systems | `water` | Filtration, sanitation, irrigation |
| Food preparation | `recipes` | Preservation, preparation, nutrition |
| Electronics | `electronics` | Repair, circuits, power systems |
| Building | `building` | Construction, materials, structures |
| Energy | `energy` | Solar, wind, storage systems |

**Generation frequency**: Weekly for active domains (>10 items), monthly for sparse domains.

### Variant C: Read-Only Reference Export

**Purpose**: Static archive snapshot intended for long-term preservation and citation. Unlike
Variants A and B, which are updated regularly, Reference Exports are created on demand (major
project milestones, governance decisions) and never updated post-export.

**Content scope**: Identical to Full Export at the time of creation.

**Key difference from Full Export**: A Reference Export carries a `status: archived` flag in the
OPDS catalog entry. It has no "latest" redirect; its versioned URL is permanent and its CDN cache
headers are set to `immutable`. It is never deleted by the retention policy.

**Use case**: Researchers and institutional partners who need a stable, citable snapshot of
open-repo's content at a specific point in time. Academic references can cite a specific Reference
Export by its SHA-256 checksum and versioned URL.

**ZIM naming**: `open-repo_en_archive_YYYY-MM-DD.zim`
(Note: uses full date instead of YYYY-MM to allow multiple snapshots per month)

**Estimated ZIM size**: 40-60 MB (text-only). Same as Full Export.

**Generation trigger**: Manual only (not on a schedule). Created by node operator via:
```
POST /api/exports/reference
Body: { "reason": "Phase 4 completion milestone", "scope": "full" }
```

---

## 2. Scoping Rules

### 2.1 Content Inclusion Logic

For each export job, content is selected by SQL query against the `content_items` table:

```python
# Full Export
query = db.query(ContentItem).filter(
    ContentItem.is_local == True
)

# Domain-Specific Export
query = db.query(ContentItem).filter(
    ContentItem.is_local == True,
    ContentItem.domain == config.domain_name
)

# Reference Export (same as Full Export at snapshot time)
query = db.query(ContentItem).filter(
    ContentItem.is_local == True
)
# Snapshot captured at a specific `created_at` cutoff date if needed
```

### 2.2 Search Indexing Strategy

| Export Type | Indexing | Xapian Language |
|---|---|---|
| Full Export | Full-text, all items | `eng` (primary) |
| Domain Export | Full-text, domain items only | `eng` |
| Reference Export | Full-text, all items at snapshot | `eng` |

Xapian stemming performs best with a single language. For multilingual content, the primary
language of the majority of content determines the stemmer. Future multilingual exports
(`open-repo_mul_all`) will use a separate export job with the appropriate Xapian configuration.

### 2.3 Internal Link Resolution

ZIM articles use relative links to navigate between items. The export renderer must:

1. Resolve all internal `cid://` links to ZIM-relative paths: `../{cid}`
2. For cross-domain links in domain-specific exports, replace with a stub page:
   `"This article is available in the full Open-Repo export."`
3. For links to external URLs, leave them as-is (`http://`). Kiwix readers display external links
   but warn users they require internet access.
4. Never include `http://` links to the open-repo node itself — these would break in fully offline
   context. All internal references must be ZIM-relative.

---

## 3. Incremental Update Strategy

### 3.1 Why Full Exports, Not Diffs

True ZIM binary diffs (`zimdiff`/`zimpatch`) are not production-ready as of 2026. No major ZIM
publisher uses them. Open-repo's incremental strategy is **versioned full exports with smart
scheduling** — the same approach used by Wikipedia, Stack Exchange, and Project Gutenberg.

The practical "incremental" benefit for users comes from scope: a user who only needs agriculture
content downloads a 5-10 MB domain export, not a 50-80 MB full export. This is more useful than
binary diffs at open-repo's current scale.

### 3.2 Versioning Scheme

Export version identifiers follow the format: `YYYY-MM` with optional alphabetic suffix.

Examples:
- `2026-04` — first export of April 2026
- `2026-04a` — second export of April 2026 (manual re-export after error correction)
- `2026-05` — next scheduled export

Filename construction:
```
{name}_{period}.zim
open-repo_en_nopic_2026-04.zim
open-repo_en_nopic_2026-04a.zim
open-repo_en_agriculture_2026-05.zim
```

### 3.3 Export Schedule

| Export Variant | Flavour | Schedule | Trigger |
|---|---|---|---|
| Full (`nopic`) | `nopic` | Every Sunday at 02:00 UTC | Cron / APScheduler |
| Full (`all`) | `all` | 1st of each month at 03:00 UTC | Cron |
| Domain exports | per-domain | Every Sunday at 04:00 UTC | Cron |
| Reference export | `archive` | Manual only | Admin API |

All scheduled exports run as background jobs (Celery task or FastAPI BackgroundTask). Failed
exports are retried once after 1 hour. After two failures, the job is marked as errored and an
alert is raised.

### 3.4 Content Freeze Policy

**Scheduled exports** do not "freeze" content — they export a snapshot of whatever content exists
at job start time. If content is being actively edited during an export job, the export captures
the state at query time (PostgreSQL `READ COMMITTED` isolation). This is acceptable.

**Reference exports** enforce an explicit freeze: the job captures `export_started_at` and
excludes any `ContentItem` with `updated_at > export_started_at`. This ensures the Reference
Export is stable even during concurrent editing.

**Emergency re-export trigger**: If a critical error is discovered in a published export (corrupted
HTML, missing metadata, `zimcheck` failure discovered post-publication), the operator triggers a
manual re-export via:
```
POST /api/exports/emergency
Body: { "flavour": "nopic", "reason": "zimcheck failure: missing Illustration_48x48" }
```
Emergency exports use the `a`/`b` suffix on the current period and immediately supersede the
previous export.

---

## 4. Accessibility Considerations

### 4.1 Screen Reader Compatibility

ZIM articles served by Kiwix use standard HTML rendered in a browser WebView (mobile) or standard
browser (desktop/kiwix-serve). Standard HTML accessibility practices apply.

Requirements for all exported HTML:
- Every `<img>` element must have a non-empty `alt` attribute describing the image content
- Procedure steps must use ordered lists (`<ol>/<li>`) for screen reader step enumeration
- Section headings must be hierarchical (`<h1>`, `<h2>`, `<h3>`) and not skip levels
- Interactive elements (if any) must have ARIA labels where the visual label is not sufficient
- Language must be declared: `<html lang="en">` (or appropriate ISO code)

### 4.2 Alt Text for Diagrams

Technical diagrams (schematics, procedure illustrations) require descriptive alt text. The
`content_jsonld` schema supports a `description` field on media items. The export renderer must
use this as the `alt` attribute:

```python
# Template rendering logic
for media_item in item.content_jsonld.get("media", []):
    alt = media_item.get("description", {}).get("en", "Diagram")
    html += f'<img src="{media_item["path"]}" alt="{alt}">'
```

Where no description exists, use `"{item_type} diagram for {item_title}"` as a fallback. Do not
leave `alt=""` on informational images.

### 4.3 Text Fallbacks for Interactive Elements

Open-repo's web UI may include interactive elements (step-by-step progress tracking, vote buttons).
These must be stripped from the export HTML. Replace with static equivalents:

- Vote counts: render as static text (`"Endorsed by 42 community members"`)
- Progress trackers: remove entirely (not meaningful in offline context)
- Comment sections: remove entirely
- "Contribute edit" buttons: replace with text: `"Download the full Open-Repo to contribute edits"`

### 4.4 Font and Contrast

ZIM articles should use system fonts (`font-family: system-ui, sans-serif`) to avoid embedding
large font files in the ZIM. Minimum contrast ratio: 4.5:1 for body text (WCAG AA). Test the
exported HTML template against WCAG AA before the first production export.

---

## 5. Storage and Retention Policy

### 5.1 Retention Rules

Following the openZIM v2 retention model (June 2024), adapted for open-repo:

| Rule | Details |
|---|---|
| Current version | Always keep (is_current = True) |
| Previous month | Keep the most recent export from the previous calendar month |
| 30-day safety window | Keep any export less than 30 days old (protects active downloads) |
| Reference exports | Keep permanently (never delete) |
| All others | Delete from object storage; mark DB row `status = 'deleted'` |

At steady state (weekly exports), this means: current week's export + previous month's export + any
export < 30 days old. Typically 4-6 versions in storage at any time per flavour.

**Maximum versions per flavour at steady state**: 5-6. **Minimum**: 2 (current + previous month).

### 5.2 Storage Cost Estimates

Using Cloudflare R2 at $0.015/GB/month:

| Scenario | ZIM Size | Flavours | Versions | Monthly Cost |
|---|---|---|---|---|
| Phase 5 MVP | 80 MB | 3 | 5 each | ~$0.18/month |
| Phase 5 at scale | 500 MB | 6 | 5 each | ~$2.25/month |
| Image-inclusive exports | 2 GB | 3 | 5 each | ~$0.45/month |

Total storage cost at Phase 5 MVP: well under $1/month. Budget alert threshold: $10/month.

### 5.3 Deletion Process

The retention policy runs as part of the export job after a new export is marked `is_current`:

```python
def apply_retention_policy(db, name: str, flavour: str):
    """Delete superseded exports per retention rules."""
    now = datetime.utcnow()
    cutoff_30d = now - timedelta(days=30)

    # Find all non-current, non-reference exports for this name+flavour
    candidates = db.query(ZimExport).filter(
        ZimExport.name == name,
        ZimExport.flavour == flavour,
        ZimExport.is_current == False,
        ZimExport.is_reference == False,
        ZimExport.status == "superseded",
        ZimExport.generated_at < cutoff_30d,
    ).order_by(ZimExport.generated_at.desc()).all()

    # Keep the most recent from the previous calendar month
    previous_month = (now.replace(day=1) - timedelta(days=1)).strftime("%Y-%m")
    kept_previous_month = False

    for export in candidates:
        export_month = export.period[:7]  # YYYY-MM
        if export_month == previous_month and not kept_previous_month:
            kept_previous_month = True
            continue  # Keep this one
        # Delete from object storage
        delete_from_storage(export.storage_path)
        export.status = "deleted"

    db.commit()
```

### 5.4 Cross-Region Backup Strategy

ZIM files are immutable once published. Backups are straightforward:

1. **Primary**: Cloudflare R2 bucket (production)
2. **Secondary**: Automated sync to a second R2 bucket in a different Cloudflare region, or a
   GitHub Release asset for exports < 2 GB
3. **Git-based metadata backup**: The `zim_exports` table metadata (not the binary files) is
   included in a weekly database dump stored in the git repository under
   `infrastructure/exports-metadata/` (JSON format, machine-readable)

Reference Exports (permanently retained) should also be mirrored to the Internet Archive via their
S3-compatible upload API, which provides free long-term storage for open-source content.

---

## Sources

- [openZIM ZIM Updates v2 — retention logic](https://wiki.openzim.org/wiki/ZIM_Updates)
- [openZIM ZIM Naming Convention](https://wiki.openzim.org/wiki/ZIM_Naming_Convention)
- [Cloudflare R2 Pricing](https://developers.cloudflare.com/r2/pricing/)
- [WCAG 2.1 AA Contrast Requirements](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum)
- [Internet Archive S3-like API](https://archive.org/developers/internetarchive/quickstart.html)
- [Phase 4 Design](../PHASE_4_DESIGN.md)
- [Phase 5 Offline Export Architecture](../phase-5-offline-export-architecture.md)
