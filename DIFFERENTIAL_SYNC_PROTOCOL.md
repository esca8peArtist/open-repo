---
title: "Phase 5.3 Differential Sync Protocol — Bandwidth-Efficient ZIM Updates"
project: open-repo
phase: "5.3 design"
status: design-proposal
created: 2026-05-22
author: General Research Agent
depends_on:
  - PHASE_5_ARCHITECTURE.md
  - FEDERATION_ARCHITECTURE.md
  - VERSIONING_STRATEGY.md
deadline: 2026-05-30
tags: [differential-sync, delta-compression, bandwidth, offline, rsync, zimdiff, low-connectivity]
---

# Phase 5.3 Differential Sync Protocol
## Bandwidth-Efficient ZIM Updates for Poor-Connection Environments

---

## Executive Summary

A full-library ZIM file is 50–300 MB. A weekly content update might change 5–15 articles out of 3,000. Without differential sync, a community library on a 2G connection downloads 300 MB to receive 200 KB of actual new content — a 1,500:1 waste ratio. At 50 KB/s throughput (typical 2G), that is a 100-minute download for a 4-minute content change.

This document designs a differential sync protocol that ships only the changed content between ZIM versions, enabling updates that are proportional in size to the actual changes rather than to the full library.

The core mechanism is a **two-layer delta approach**:

1. **Article-level deltas**: The source database tracks which articles changed between versions. A delta manifest lists only changed articles by their content hash.
2. **Binary patch files**: For ZIM file consumers who cannot rebuild from source, a binary patch (zimdiff format) transforms the old ZIM into the new ZIM with minimal data transfer.

For a weekly update that modifies 12 articles averaging 15 KB each, the delta transfer is approximately 180 KB versus a 300 MB full download — a 1,666:1 improvement in bandwidth efficiency.

---

## 1. The Bandwidth Problem in Context

### 1.1 Real-World Connection Profiles

The open-repo target deployment environments span a wide range of connectivity:

| Environment | Typical connection | Throughput | Full ZIM download time (300 MB) |
|---|---|---|---|
| Urban community center | Broadband / Wi-Fi | 10 Mbps | 4 minutes |
| Rural school | 3G mobile | 1 Mbps | 40 minutes |
| Remote clinic | 2G mobile | 100–300 Kbps | 3–8 hours |
| Satellite (once weekly) | VSAT | 50 Kbps | 16 hours |
| Sneakernet (USB courier) | Physical transfer | N/A (latency, not throughput) | Days to weeks |

For the satellite and sneakernet cases, differential sync is not just an optimization — it is what makes any regular updating feasible at all. A clinic receiving a USB drive once a week can receive a 500 KB delta on that drive and apply it in seconds. Receiving a 300 MB full file changes the entire calculus of update frequency.

### 1.2 What Changes Between ZIM Versions

Understanding what changes between versions is essential to designing an efficient delta strategy.

**PATCH version changes** (most frequent, smallest):
- 1–20 articles corrected
- Typical delta size: 50 KB – 2 MB
- Article content changes (not structure changes)
- No new articles, no deleted articles

**MINOR version changes** (weekly to monthly):
- 10–200 new articles added
- 5–30 existing articles revised
- Typical delta size: 2 MB – 30 MB
- May include new internal cross-links between articles

**MAJOR version changes** (rare, several per year):
- Structural changes: article URL scheme, metadata schema, new domains
- May require full re-download because the patch cannot safely transform the old structure to the new
- Typical delta size: varies widely, may approach full file size

The differential sync protocol is primarily designed for PATCH and MINOR version transitions, which represent the overwhelming majority of updates in a steady-state content library.

---

## 2. Delta Compression: Technical Approaches

### 2.1 Three Candidate Approaches

**Approach A: zimdiff / zimpatch (ZIM-native)**

The openZIM project developed `zimdiff` and `zimpatch` tools as part of a 2013 Google Summer of Code project. Zimdiff takes two ZIM files as input, computes their difference, and produces a ZIM diff file where `old_zim + diff_file = new_zim`. Zimpatch applies the diff to produce the updated ZIM.

The openZIM project revisited this with a ZIM Update v2 initiative in 2024, updating the period suffix format to `YYYY-MM[ll]` to support within-month update releases.

Strengths:
- ZIM-native: understands the ZIM cluster structure and article index, enabling smarter diffing than a generic binary diff
- The receiver does not need the new ZIM — only the old ZIM and the diff file
- Two patching modes: fast merge (index rewriting, higher storage) or full recompute (lower storage)
- Diff file is itself in ZIM format, enabling the diff to be inspected or applied by any ZIM-aware tool

Weaknesses:
- The tooling is not fully productionized as of 2025; implementation status requires verification
- Diff file size depends on article content changes, but also on ZIM cluster reorganization — if the cluster layout changes significantly (e.g., when many new articles are added and clusters are rebalanced), the diff file may be large even if content changes are small
- The receiver must have the exact same version of the old ZIM that the diff was computed against (no partial patch chains without intermediate versions)

**Approach B: rsync / librsync (generic binary delta)**

Rsync's algorithm does not require both files to be present at the server. Instead:
1. The receiver sends a set of checksums describing its file (the "signature")
2. The server uses these checksums to identify which blocks in the new file match blocks the receiver already has
3. The server sends only the instructions to reconstruct the new file ("delta"), referencing matching blocks by offset and copying non-matching content verbatim

The rsync algorithm is available as a library (`librsync`) that can be embedded in any application without the rsync command-line tool.

Strengths:
- Well-proven at scale; powers millions of daily synchronizations
- Does not require ZIM-specific knowledge; works on any binary file
- The receiver only sends a small signature (checksums), not the entire file
- Rolling checksums detect matching blocks even when their positions shift between versions

Weaknesses:
- Generic binary delta: does not understand ZIM cluster boundaries, so may produce larger deltas than zimdiff for ZIM-specific structural changes
- Requires a protocol round-trip: receiver sends signature, server computes and sends delta. Not suitable for push-only distribution (USB, pre-computed patch files)
- Signature computation on the receiver adds CPU load on low-power devices (Raspberry Pi)

**Approach C: Manifest-based article patching (application-layer delta)**

Instead of treating the ZIM file as an opaque binary, this approach works at the application layer:
1. The publisher generates a **delta manifest** listing exactly which articles changed between v1.2.0 and v1.3.0, with their new content hashes
2. The receiver downloads only the changed article bodies (as pre-rendered HTML fragments)
3. The receiver's open-repo node rebuilds the ZIM locally from its existing cached article content plus the new articles

Strengths:
- Delta size is precisely proportional to changed content — no cluster-reorganization overhead
- Works in a push model (publisher pre-computes what changed; receiver only downloads the delta manifest and changed articles)
- Does not require the receiver to have the previous ZIM file — it rebuilds from article-level caches
- Most natural fit for the article-level versioning model in `VERSIONING_STRATEGY.md`

Weaknesses:
- Requires the receiver to have the ZIM build pipeline (libzim) installed and sufficient CPU/RAM to run ZIM assembly — not suitable for bare Kiwix readers
- The rebuilt ZIM may have different cluster layout than the original, making it technically a new ZIM file (different CID) even with the same content
- More complex implementation than binary delta approaches

### 2.2 Recommended Approach: Hybrid Strategy

The appropriate delta mechanism depends on the receiver's capabilities. The protocol should support both:

**For open-repo nodes** (libraries running the full open-repo stack with libzim):
Use the manifest-based article patching approach. The publisher generates a delta manifest listing changed articles, and the receiver downloads changed articles and rebuilds the ZIM locally. This produces the smallest possible delta size.

**For bare Kiwix readers** (users who have downloaded a ZIM and want to update it without running open-repo):
Use zimdiff/zimpatch for binary patches. The publisher pre-computes binary patch files for each version transition and makes them available alongside the full ZIM download. A user with the old ZIM and the patch file can update locally without re-downloading the full archive.

**For the sneakernet case** (USB delivery):
The USB bundle includes both the full new ZIM (for users who do not have the previous version) and the binary patch file from the previous version (for users who do). The receiver chooses which to use based on what they have.

---

## 3. Delta Manifest Format

The delta manifest is the core data structure that enables manifest-based article patching. It is a signed JSON document.

```json
{
  "schema_version": "1.0",
  "source_library_id": "LIBID-5mfFqPJmzGGHGjHx...",
  "zim_name": "open-repo_en_seed-preservation",
  "from_version": "1.2.0",
  "to_version": "1.3.0",
  "generated_at": "2026-05-22T02:00:00Z",
  "summary": "Added 80 East African heritage grain varieties; corrected storage temperatures for 12 species",
  "changes": {
    "added": [
      {
        "article_path": "/items/seed-sorghum-sorgo",
        "title": "Sorghum bicolor — Sorgo",
        "content_hash": "sha256:7f3a9b...",
        "size_bytes": 18234,
        "download_url": "https://library.example.org/articles/seed-sorghum-sorgo_v1.html",
        "domain": "seed-preservation"
      }
    ],
    "modified": [
      {
        "article_path": "/items/seed-corn-maize",
        "title": "Zea mays — Corn / Maize",
        "old_content_hash": "sha256:2b8e1a...",
        "new_content_hash": "sha256:9f4c3d...",
        "size_bytes": 22891,
        "download_url": "https://library.example.org/articles/seed-corn-maize_v3.html",
        "change_summary": "Corrected optimal storage humidity from 35% to 40% RH (GRIN 2024 data)"
      }
    ],
    "deleted": [
      {
        "article_path": "/items/seed-amaranth-ornamental",
        "reason": "Moved to botanical domain"
      }
    ]
  },
  "stats": {
    "articles_added": 80,
    "articles_modified": 12,
    "articles_deleted": 1,
    "estimated_delta_size_bytes": 1843200
  },
  "binary_patch": {
    "format": "zimdiff",
    "patch_url": "https://library.example.org/zim/seed-preservation_v1.2.0-to-v1.3.0.zimdiff",
    "patch_sha256": "sha256:c4e7f2...",
    "patch_size_bytes": 2100000
  },
  "signature": "<base64-encoded Ed25519 signature>"
}
```

The delta manifest is published at:
```
GET /zim/{name}_v{from}-to-v{to}.delta.json
```

And referenced in the OPDS catalog entry and signed ZIM manifest (see `FEDERATION_ARCHITECTURE.md` section 3.2).

---

## 4. Sync Workflow: Step by Step

### 4.1 Open-Repo Node Sync (Full Pipeline)

For a community library running the open-repo node with libzim:

**Step 1: Discover available updates**
The node polls trusted peer manifests on schedule (see `FEDERATION_ARCHITECTURE.md` section 4.2). The manifest includes the latest ZIM version for each domain. If the peer's version is higher than the local version, an update is available.

**Step 2: Fetch delta manifest**
Before downloading anything, the node fetches the delta manifest for the version transition. The delta manifest tells the node:
- How many articles changed
- What the estimated delta download size is
- Whether a binary patch file is also available

**Step 3: Bandwidth estimation**
The node estimates transfer time based on a rolling average of recent transfer speeds to this peer. If the estimated time exceeds a configurable threshold (default: 30 minutes), the sync is scheduled for a low-traffic time window (configurable, default: 02:00–06:00 local time).

```
Estimated time = delta_size_bytes / avg_transfer_speed_bytes_per_sec
```

**Step 4: Download changed articles**
The node downloads only the articles listed in `changes.added` and `changes.modified`. Downloads are:
- Resumable (HTTP Range requests)
- Verified by content hash on completion of each article
- Cached locally in an article cache, not written to the ZIM yet

**Step 5: Rebuild the ZIM**
Once all changed articles are downloaded and verified, the node rebuilds the ZIM using libzim:
1. Load all unchanged articles from the previous ZIM (read by the libzim reader)
2. Apply the added and modified articles from the article cache
3. Remove deleted articles
4. Rebuild with full Xapian indexing
5. Run zimcheck validation
6. Compute new CID and SHA-256

**Step 6: Verify and commit**
The new ZIM's CID is verified against the peer's manifest entry. If they match, the old ZIM is archived (or deleted, per retention policy) and the new ZIM is moved to the active collection.

Total data transferred: sum of changed article sizes + delta manifest size. For a typical PATCH release, this is 100 KB to 2 MB.

### 4.2 Binary Patch Application (Bare Kiwix Reader)

For a library that has the old ZIM file and the binary patch file but cannot run libzim:

```
zimpatch old_zim.zim patch.zimdiff new_zim.zim
```

The zimpatch tool applies the binary delta and produces the new ZIM. This requires:
- The exact previous ZIM file (same CID as the one the patch was computed against)
- The zimpatch binary (available for Linux, macOS, Windows via the openzim package)
- Sufficient disk space for both the old and new ZIM simultaneously

After patching, the new ZIM is verified by computing its SHA-256 and comparing to the published checksum.

### 4.3 Partial Download and Resume

Long downloads over unreliable connections must be resumable. The implementation:

**HTTP Range requests**: Every ZIM file and delta patch file served by open-repo nodes supports HTTP `Range` requests. A download interrupted at 30 MB resumes from byte 31,457,280 in the next connection attempt.

**Chunk-level verification**: For files downloaded via BitTorrent, piece-level SHA-256 hashes (from the `.torrent` file) enable verification of each 1 MB chunk independently. A corrupted chunk is re-requested; a verified chunk is never re-downloaded.

**Progress persistence**: The open-repo node stores download progress in its database. A node restart does not lose progress on in-flight downloads.

**Timeout and backoff**: If a connection to a peer is lost, the node applies exponential backoff before retrying (30s, 1m, 2m, 5m, 10m). After 24 hours without successful connection, the download is paused and the operator is notified.

### 4.4 Sneakernet Delta Distribution

For communities served by USB couriers:

**At the source library** (preparing the USB bundle):
```
library-bundle-2026-05-22/
├── manifest.json           # Signed manifest listing current ZIM versions
├── deltas/
│   ├── seed_v1.2.0-to-v1.3.0.delta.json       # Delta manifest
│   ├── seed_v1.2.0-to-v1.3.0.zimdiff          # Binary patch (for bare Kiwix)
│   └── articles/                               # Changed article HTML files
│       ├── seed-sorghum-sorgo_v1.html
│       └── seed-corn-maize_v3.html
└── full/                   # Optional: full ZIM files for recipients without previous version
    └── open-repo_en_seed-preservation_v1.3.0.zim
```

The courier carries this USB drive to receiving libraries. Libraries with the previous ZIM version can apply only the delta (faster). Libraries without the previous version download the full ZIM (also provided in the bundle for this reason).

**At the receiving library** (importing):
The open-repo import UI detects the library bundle structure, verifies the manifest signature, and presents options:
- "Apply delta from version 1.2.0 to 1.3.0" (if the library has v1.2.0)
- "Install full version 1.3.0" (if the library does not have a previous version)

---

## 5. Bandwidth Estimation and Scheduling

### 5.1 Bandwidth Model

The open-repo node tracks rolling statistics on transfer performance to each known peer:

```json
{
  "peer_id": "LIBID-...",
  "transfer_stats": {
    "avg_speed_bytes_per_sec": 12500,
    "p95_speed_bytes_per_sec": 8000,
    "last_successful_transfer": "2026-05-20T14:23:00Z",
    "successful_transfers_30d": 4,
    "failed_transfers_30d": 2,
    "avg_failure_duration_seconds": 180
  }
}
```

Transfer time for a delta is estimated at the p95 speed (more conservative than average, reflecting poor-connection conditions) plus a 20% buffer for connection overhead:

```
estimated_time_seconds = (delta_size_bytes / p95_speed) * 1.2
```

### 5.2 Scheduling Strategies

**Immediate sync** (for PATCH releases with delta < 2 MB and estimated time < 5 minutes): Sync immediately when the update is discovered, regardless of time of day.

**Scheduled sync** (for MINOR releases or larger deltas): Queue for the next low-traffic window. The default window is 02:00–06:00 local time. The operator can configure the window to match their connection schedule (e.g., a library on satellite uplink only active Wednesday 20:00–22:00 UTC can configure that window).

**Manual sync** (for MAJOR releases or after-hours): Require operator confirmation. A MAJOR version change may require the operator to communicate changes to their community before updating. The node does not apply MAJOR updates automatically.

**Bandwidth cap enforcement**: The operator can set a maximum daily or weekly bandwidth budget for sync operations. The node tracks usage against this cap and defers non-urgent syncs when the cap is approached.

### 5.3 Prioritization

When multiple domain ZIMs have updates pending and bandwidth is constrained, updates are prioritized by:

1. **Safety-critical content** (medical, food safety): highest priority
2. **Time-sensitive content** (seasonal agricultural guides): elevated priority during relevant seasons
3. **User-configured priority**: the operator can pin priority order for their deployment
4. **File size**: smaller deltas first (more updates completed per bandwidth unit)

The node exposes a simple queue UI showing pending updates, their estimated download sizes, and their scheduled time.

---

## 6. Storage Trade-offs

### 6.1 Delta File Retention Policy

The delta files themselves consume storage. The retention policy balances storage cost against the ability to serve updates to libraries on different version timelines:

| Delta age | Retention policy |
|---|---|
| 0–90 days | Keep all delta files |
| 90–365 days | Keep delta files for MINOR and MAJOR transitions; discard PATCH deltas |
| > 365 days | Keep only full ZIM files for archive; discard all deltas |

The rationale: a library that is more than 3 months behind on PATCH updates should do a MINOR or full update rather than applying a long chain of PATCH deltas. Chaining many sequential deltas is both computationally expensive and more error-prone (a corrupt intermediate state propagates forward).

**Maximum delta chain depth**: The protocol caps delta chains at 3 sequential patches before requiring a full ZIM download or MINOR-level update. This prevents a library from needing to apply a chain of 20 PATCH deltas to get current.

### 6.2 Article Cache

The open-repo node maintains a local article cache (individual article HTML files keyed by content hash) separate from the ZIM files. The article cache serves two purposes:
- Enables incremental ZIM rebuilds without downloading unchanged articles
- Provides a fallback read path if a ZIM file is corrupt

The article cache has its own retention policy: articles not referenced by any current ZIM version for more than 90 days are pruned. The cache size is bounded at a configurable maximum (default: 2x the largest ZIM file currently in the collection).

### 6.3 Disk Space Estimate for a Typical Deployment

For a community library running 5 domain ZIMs (medical, water, seed, food, botanical) at Phase 5.2 scope:

| Item | Estimated size |
|---|---|
| Full ZIM files (5 domains, current version) | 100–400 MB |
| Previous version ZIM files (1 version retained) | 100–400 MB |
| Delta files (90-day retention, PATCH + MINOR) | 50–200 MB |
| Article cache | 50–150 MB |
| Database and metadata | 10–50 MB |
| **Total** | **310 MB – 1.2 GB** |

This is within the range of a 16 GB SD card (Raspberry Pi) with significant headroom for the operating system and other applications.

---

## 7. Design Trade-offs

| Trade-off | Choice Made | Alternative Rejected | Reason |
|---|---|---|---|
| **Generic binary delta (rsync) vs. ZIM-native diff (zimdiff)** | Both, depending on receiver capability | One approach only | Different receiver capabilities warrant different mechanisms; both should be supported |
| **Pre-computed patches vs. on-demand delta computation** | Pre-computed patches published by source | On-demand (receiver requests diff) | Pre-computed patches avoid the round-trip and work for USB/sneakernet; on-demand requires both parties to be online simultaneously |
| **Deep delta chains vs. periodic full rebase** | Maximum 3-deep chains, then full rebase | Unlimited chain depth | Deep chains accumulate error risk and are computationally expensive on constrained hardware |
| **Aggressive caching vs. minimal storage footprint** | Configurable (default: 2x largest ZIM) | Fixed minimal cache | Deployments vary widely; aggressive caching enables faster rebuilds on good storage; tight budgets can reduce cache size |
| **Automatic MAJOR updates vs. always-manual** | Always manual for MAJOR | Automatic for all | MAJOR changes may require community communication; automation risk is high for breaking changes |
| **Bandwidth estimation based on history vs. user-configured** | History-based with user override | User-configured only | History-based is more accurate for variable connections; override needed for known schedules (satellite uplinks) |

---

## 8. Security Considerations

### 8.1 Delta File Integrity

A malicious delta file could corrupt a library's ZIM collection. Defenses:

- Every delta manifest is signed by the source library's Ed25519 key and verified before any content is applied
- Every downloaded article is verified by content hash before being written to the article cache
- The rebuilt ZIM is verified by zimcheck before replacing the previous version
- If any verification step fails, the update is rolled back completely and the previous version is retained

The rollback guarantee is essential: a failed update must never leave the library with a corrupt or partial ZIM. The implementation must maintain the previous ZIM until the new ZIM is fully verified.

### 8.2 Version Rollback

If a library discovers after applying an update that the new version contains errors (incorrect medical data, bad food safety tables), they can roll back to the previous version:

1. The previous ZIM version is retained for 30 days after supersession (configurable)
2. The rollback is a single operation: mark the previous version as current, demote the new version to superseded
3. A rollback event is logged in the audit trail with a reason field
4. The library can report the error to the source library through the Change Proposal system (see `VERSIONING_STRATEGY.md` section 3.1)

### 8.3 Replay Attack Prevention

The delta manifest includes a `generated_at` timestamp. Nodes reject delta manifests older than a configurable maximum age (default: 30 days). This prevents an attacker who has captured a legitimate old delta manifest from replaying it to a library that has since advanced to a newer version.

The `from_version` and `to_version` fields are also validated against the library's current state: a delta from v1.2.0 to v1.3.0 is only applied if the library's current version is exactly v1.2.0 (not v1.1.0 or v1.3.0).

---

## 9. Implementation Priority

Phase 5.3 differential sync should be implemented in stages, aligned with the federation development phases in `FEDERATION_ARCHITECTURE.md` section 8.3:

**Stage 1 (alongside 5.3a — foundational)**: Delta manifest generation in the export pipeline. When the export pipeline generates a new ZIM version, it also:
- Computes the article-level diff against the previous version
- Generates and signs the delta manifest JSON
- Publishes the delta manifest alongside the ZIM in R2/CDN

No sync logic yet — just the manifest generation. Cost: 4–6 hours.

**Stage 2 (alongside 5.3b — verification)**: Apply delta manifests on import. When the USB import receives a delta manifest, the node applies changed articles to rebuild the ZIM. Cost: 8–12 hours.

**Stage 3 (alongside 5.3c — peer networking)**: Automatic delta sync with trusted peers. The node polls peers, detects available deltas, and applies them on schedule. Cost: 12–16 hours.

**Stage 4 (optional, alongside 5.3d)**: zimdiff/zimpatch binary patch generation. Publish binary patch files for bare Kiwix reader compatibility. Cost: 6–10 hours (contingent on zimdiff tooling availability and stability).

---

## Cross-References

- ZIM export pipeline and scheduling: `PHASE_5_ARCHITECTURE.md` section 2.5
- Signed manifest format: `FEDERATION_ARCHITECTURE.md` section 3.2
- Version numbering (MAJOR/MINOR/PATCH): `VERSIONING_STRATEGY.md` section 2.2
- Article-level versioning and audit trail: `VERSIONING_STRATEGY.md` sections 2.3 and 5.2
- Phase 5.2 domain ZIM sizes and content scope: `PHASE_5.2_IMPLEMENTATION_ROADMAP.md`
- OPDS catalog delta references: `PHASE_5_ARCHITECTURE.md` section 3 (OPDS entry format)

---

## Sources

- [Kiwix/ZIM Incremental Updates — MediaWiki](https://www.mediawiki.org/wiki/Kiwix/ZIM_incremental_updates)
- [T49406 Incremental update: zimdiff & zimpatch — Wikimedia Phabricator](https://phabricator.wikimedia.org/T49406)
- [openZIM ZIM Updates — wiki.openzim.org](https://wiki.openzim.org/wiki/ZIM_Updates)
- [librsync — GitHub](https://github.com/librsync/librsync)
- [Rsync — Wikipedia](https://en.wikipedia.org/wiki/Rsync)
- [Delta encoding — Wikipedia](https://en.wikipedia.org/wiki/Bsdiff)
- [Git Delta Compression — gitperf.com](https://gitperf.com/chapter-06.html)
- [How Git Efficiently Transmits Changes — teknikaldomain.me](https://teknikaldomain.me/post/how-git-efficiently-transmits-your-changes/)
- [Syncthing Block Exchange Protocol v1](https://docs.syncthing.net/specs/bep-v1.html)
- [Anatomy of the Block Exchange Protocol — Reliability Whisperer](https://reliabilitywhisperer.substack.com/p/the-anatomy-of-the-block-exchange)
- [Efficient game updates (delta encoding case study) — fasterthanli.me](https://fasterthanli.me/articles/efficient-game-updates)
- [Offline-First Done Right — Developers Voice](https://developersvoice.com/blog/mobile/offline-first-sync-patterns/)
- [Offline sync and conflict resolution — Sachith Dassanayake (2026)](https://www.sachith.co.uk/offline-sync-conflict-resolution-patterns-architecture-trade%E2%80%91offs-practical-guide-feb-19-2026/)
- [Phase 5 Architecture — open-repo project](./PHASE_5_ARCHITECTURE.md)
- [Federation Architecture — open-repo project](./FEDERATION_ARCHITECTURE.md)
- [Versioning Strategy — open-repo project](./VERSIONING_STRATEGY.md)
