---
title: "Phase 5: Offline Export & Distributed Node Sync — Architecture"
project: open-repo
phase: 5
status: design-ready
date: 2026-04-30
author: research-agent
confidence: high
supersedes:
  - phase-5-kiwix-architecture.md (absorbed into §1)
  - phase-5-offline-export-architecture.md (absorbed into §1–§2)
  - phase-5-export-strategy.md (absorbed into §2)
  - phase-5-kiwix-integration-guide.md (absorbed into §1–§2)
  - phase-5-implementation-plan.md (absorbed into §4)
tags: [offline-export, zim, kiwix, ipfs, distributed-sync, node-sync, architecture, roadmap]
---

# Phase 5: Offline Export & Distributed Node Sync

**Phase context**: Phases 1–4 complete. Wave 4 PR #1 awaiting maintainer merge. Phase 5 adds two
orthogonal capabilities: (A) exporting federation data as Kiwix/ZIM offline archives for
distribution, and (B) peer-to-peer sync between open-repo nodes without requiring a persistent
server connection. These capabilities share a data model but are independently deployable.

**This document is the canonical Phase 5 architecture reference.** The five preliminary documents
(`phase-5-kiwix-architecture.md`, `phase-5-offline-export-architecture.md`,
`phase-5-export-strategy.md`, `phase-5-kiwix-integration-guide.md`,
`phase-5-implementation-plan.md`) remain valid technical references and are not deleted — they
contain deeper implementation detail on individual subsystems. This document synthesizes them into
a unified design and extends the scope to cover distributed node sync, which those documents
treated as a future concern.

---

## 1. Offline Export Strategy

### 1.1 What Gets Exported and Why

The open-repo data model (post-Phase 4) stores `ContentItem` records with `item_type`, `domain`,
and `is_local` flags. Phase 5 exports define precisely which records enter the offline archive.

**Scope decision**: only `is_local = True` items enter any scheduled export. Federated content from
partner nodes carries attribution obligations and potentially different licenses that cannot be
assumed to permit bulk redistribution. A "Federated Export" variant that includes partner content
with explicit per-item attribution is a Phase 5.1 consideration, not an MVP requirement.

**Five content types exported**: `procedure`, `recipe`, `schematic`, `plan`, `service-listing`.

**What is excluded from all exports**:
- Live vote counts and real-time node status (point-in-time snapshots replace them)
- Administrative endpoints and node configuration
- Private metadata, user account information
- External CDN dependencies (all CSS/JS must be self-contained)
- Partner node infrastructure data (URLs, trust states, keys)

### 1.2 Export Variants

Three export variants serve different user needs and distribution constraints:

**Variant A: Full Export (`open-repo_en_nopic_YYYY-MM.zim`)**
All locally-authored `ContentItem` records across all domains. Text-only (`nopic` flavour) to
minimize file size for low-bandwidth regions. Estimated size: 50–80 MB at Phase 5 MVP scale
(500–1,000 items, 35 domains). Expected to reach 200–500 MB with images (`all` flavour) at the
same scale.

Generated weekly (Sunday 02:00 UTC, automated). A monthly `all`-flavour variant runs on the 1st
of each month.

**Variant B: Domain Export (`open-repo_en_{domain}_YYYY-MM.zim`)**
A single knowledge domain — agriculture, water, food, electronics, building, energy. Approximately
20–100 items. Target size: 5–10 MB. At this size the file is practical for users with constrained
storage (8 GB phone) and transfers over SMS-based data plans common in sub-Saharan Africa.

Generated weekly for active domains (>10 items); monthly for sparse domains.

**Variant C: Reference Export (`open-repo_en_archive_YYYY-MM-DD.zim`)**
A permanent, immutable snapshot for institutional citation. Identical scope to Variant A at
creation time. Never updated. Cache headers set to `immutable`. Never deleted by the retention
policy. Triggered manually by node operator via:
```
POST /api/exports/reference
Body: { "reason": "Phase 4 completion milestone", "scope": "full" }
```

Academic references can cite a Reference Export by its SHA-256 checksum and versioned URL.

### 1.3 ZIM Format and Tooling

The ZIM file format is an open binary container with three relevant properties for open-repo: (1)
random-access article retrieval without full decompression (critical for large archives on low-RAM
devices), (2) embedded Xapian full-text search index (eliminates need for a search server), (3)
Zstandard cluster compression achieving 2.5–3x compression on HTML text.

**Tooling choice: `python-libzim` (PyPI package: `libzim`)**. The C++ libzim reference
implementation with Python bindings. Pre-built wheels for Linux (x86/ARM64), macOS, and Windows.
No Rust or C++ toolchain required in CI. Pin `libzim>=3.2,<4.0` in `pyproject.toml`. The 3.x
Creator API (context manager interface) is stable; the 2.x to 3.x transition was the last major
breaking change.

Alternative considered: **Zimit** (headless browser crawl → WARC → ZIM). Rejected: heavyweight
Docker dependency, designed for scraping sites without export APIs. Open-repo controls its own
data model and can emit HTML directly.

Alternative considered: **zimfarm recipe submission**. Valid for large-scale community publishing,
but requires open-repo to be a publicly crawlable website. Not suitable for private or
institutional node deployments. Future enhancement, not MVP.

**Mandatory ZIM metadata** (zimcheck will fail without these):

| Field | Value |
|---|---|
| `Title` | `"Open-Repo: {Scope} (English)"` (≤30 chars) |
| `Description` | `"Offline practical knowledge library"` (≤80 chars) |
| `Language` | `"eng"` (ISO 639-3) |
| `Creator` | `"Open-Repo Community"` |
| `Publisher` | `"Open-Repo"` |
| `Date` | `"YYYY-MM-DD"` (generated at export time) |
| `Name` | `"open-repo_en_nopic"` (flavour-specific, no period) |
| `Illustration_48x48` | 48×48 PNG, exact pixel dimensions |

Filename convention: `{Name}_{period}.zim` where period is `YYYY-MM`, with alphabetic suffix
(`2026-04a`) for same-month re-exports after errors.

### 1.4 Data Preparation Pipeline

The export pipeline runs as a background job (FastAPI `BackgroundTask` or Celery Beat if available
from Phase 4). The pipeline has five stages:

**Stage 1: Content query.** Query `content_items` WHERE `is_local = True` (and optionally
`domain = {domain}` for domain exports). Stream in batches of 200 to avoid loading all records
into memory. Reference exports add a `created_at ≤ export_started_at` cutoff.

**Stage 2: HTML rendering.** Convert each `ContentItem` to self-contained HTML. No external
links: all CSS embedded in `<style>` tags, no `src` or `href` attributes pointing to `http://`.
Procedure steps render as `<ol>/<li>` for screen-reader compatibility. Vote counts render as
static text (`"Endorsed by 42 community members"`). Interactive UI elements stripped.

**Stage 3: ZIM assembly.** Feed rendered HTML and static assets to `libzim.Creator`. Configure
Xapian indexing (`creator.config_indexing(True, "eng")`). Add all mandatory metadata. Add the
48×48 illustration. The Creator is not thread-safe: run in a single thread.

**Stage 4: Validation.** Run `zimcheck output.zim` subprocess. Parse output for errors and
warnings. Fail the export job on any error. Common failure modes: missing `Illustration_48x48`,
non-UTF-8 characters in metadata, broken internal links, articles with empty `get_title()`.

**Stage 5: Upload and publication.** Compute SHA-256 checksum. Upload ZIM and `.sha256` sidecar
to Cloudflare R2 with `Content-Type: application/x-zim` and `Cache-Control: public, max-age=
2592000, immutable`. Update `zim_exports` database row to `status=available, is_current=True`.
Supersede previous current export. Run retention policy.

### 1.5 File Size Targets by Distribution Channel

Different distribution channels impose hard file size constraints. Exports must be designed with
these limits in mind:

| Channel | Practical Size Limit | Notes |
|---|---|---|
| USB (FAT32) | 4 GB per file | FAT32 limitation; most USB drives use FAT32 |
| USB (exFAT/NTFS) | No practical limit | Requires reformatting; not universal |
| Internet Archive (archive.org) | No limit | Free hosting for open content via S3-compatible API |
| IPFS / Filecoin | No hard limit | Content-addressed; large files pinnable via services |
| GitHub Releases | 2 GB per asset | Hard limit; use for domain exports and small variants |
| Git LFS | 5 GB (GitHub) | Per-file limit on GitHub; not recommended for ZIMs |
| Android Kiwix (Play Store) | No file limit | Play Store sandboxing restricts user-specified paths on some versions; F-Droid variant has no restrictions |
| kiwix-serve (institutional) | No limit | Operator-managed; RAM is the practical constraint |

**Design consequence**: the `nopic` Full Export should stay under 500 MB to fit in GitHub
Releases. Domain exports should target under 50 MB each. The `all`-flavour (with images)
is deployed only to R2, archive.org, and IPFS — not GitHub Releases.

### 1.6 Validation and Signed Releases

Every published export must include a cryptographic integrity mechanism. Two levels:

**Checksum sidecar**: SHA-256 hash of the ZIM binary, published as a `.sha256` file at the same
URL. Generated in Stage 5 of the pipeline. Example:
```
https://exports.example.org/zim/open-repo_en_nopic_2026-04.zim
https://exports.example.org/zim/open-repo_en_nopic_2026-04.zim.sha256
```

**Signed release manifest** (Phase 5.1 enhancement): A GPG-signed JSON manifest listing all
current exports with their checksums, generated after each export job and stored at
`/api/exports/manifest.json`. Downstream tools (node sync, IPFS pinning bots) can verify the
manifest signature against the node's public key (already available via the Phase 4
`/.well-known/webfinger` endpoint). This creates a chain of trust from the federation PKI
(Phase 4) through to the offline archive.

**CI enforcement**: The integration test harness (`tests/integration/test_export_pipeline.py`)
must include a test that parses exported HTML with BeautifulSoup and fails if any `src` or `href`
attribute starts with `http://` (catches accidental external dependencies). Add `zimcheck` to the
CI pipeline with `--verbose` output.

### 1.7 Retention Policy and Storage Costs

The retention policy runs after each successful export as part of the pipeline:
- Keep the current export (`is_current=True`) permanently
- Keep the most recent export from the previous calendar month
- Keep any export less than 30 days old (protects active downloads)
- Keep Reference Exports permanently (never delete)
- Delete all others from object storage; mark DB row `status=deleted`

This yields 4–6 live versions per flavour at steady state.

**Storage cost estimate (Cloudflare R2 at $0.015/GB/month)**:
- Phase 5 MVP (3–5 ZIMs, ~2–5 GB total): < $0.15/month
- Phase 5 at scale (6 flavours × 5 versions × 500 MB): ~$2.25/month
- Zero egress cost (R2's primary value proposition for open-source projects)

The Free Tier (10 GB storage, 10M Class B reads/month) covers Phase 5 MVP entirely. Budget
alert: $10/month.

For long-term archival, mirror Reference Exports to the Internet Archive via their S3-compatible
upload API (free for open-source content) as a secondary backup alongside R2.

---

## 2. Distributed Node Sync Model

### 2.1 The Sync Problem

Phase 4 federation enables real-time ActivityPub propagation of endorsement activities between
online nodes. Distributed sync addresses a different scenario: nodes that are offline most of the
time (Raspberry Pi in a field office, a laptop operated by an NGO worker) that need to
periodically synchronize their local open-repo database with one or more upstream nodes without
maintaining a persistent connection.

The sync problem for open-repo has three distinct sub-problems:

1. **Content sync**: Propagating new and updated `ContentItem` records between nodes.
2. **Endorsement sync**: Propagating `Activity` records (Announce/Undo) that did not reach a
   node during its offline period.
3. **Archive sync**: Distributing ZIM files to nodes and end-users without a central server.

These sub-problems have different optimal solutions. The distributed sync architecture below
addresses each separately.

### 2.2 Peer Discovery

Before sync can happen, nodes must find each other. Three mechanisms, in order of priority:

**Manual registration** (current Phase 4 model): An administrator registers a partner node URL
in `/admin/federation/partners/register`. This is the baseline. No auto-discovery is required for
MVP.

**Well-known bootstrap list**: Each open-repo node can publish a list of known active peers at
`/.well-known/open-repo-peers.json`. This allows a new node to bootstrap by fetching the peer
list from any existing node. Format:
```json
{
  "peers": [
    {"url": "https://nodeA.example.org", "last_seen": "2026-04-30T12:00:00Z"},
    {"url": "https://nodeB.example.org", "last_seen": "2026-04-28T08:00:00Z"}
  ],
  "updated_at": "2026-04-30T12:30:00Z"
}
```

**Kademlia DHT** (future enhancement): For fully decentralized discovery without a seed list,
nodes can participate in a Kademlia DHT (as used by IPFS/Kubo and libp2p). Each node announces
its presence with a key derived from its node identifier. This is the approach taken by IPFS in
2025 (Kubo's rebuilt DHT with efficient "sweep" provider in v0.39). Practical for Phase 5.2;
not needed for MVP where node counts are small.

### 2.3 Transport Options: Evaluation and Decision

Four transport models were evaluated:

#### Option A: Git-Based Sync

**Mechanism**: Content items are serialized to JSON files in a Git repository. Nodes sync by
cloning or pulling the repository. Large binary files (ZIM archives) use Git LFS.

**Advantages**: Familiar tooling, built-in version history, conflict detection via git merge,
no new infrastructure. CRDT-like properties for text files: git merge handles concurrent edits.

**Disadvantages**: Git is not designed for binary-heavy sync. Git LFS has a 5 GB per-file limit
on GitHub. Git repositories grow monotonically (all history retained); for a continuously updated
knowledge base this creates unbounded repository size. The git network protocol is optimized for
developer machines, not intermittent-connection edge devices. No native support for
content-addressed verification.

**Verdict**: Suitable for metadata export and changelog tracking, not for primary content or
binary archive sync. Use for publishing `zim_exports` table metadata to a Git repository as a
backup (already proposed in the retention policy for export metadata).

#### Option B: BitTorrent

**Mechanism**: ZIM files and content archives are published as torrents. Nodes seed and download
via the BitTorrent protocol (or WebTorrent via WebRTC for browser contexts). The Internet Archive
currently distributes over 1.4 million items via BitTorrent, totaling nearly a petabyte.

**Advantages**: Proven at massive scale. Swarm-based distribution reduces load on the origin
server: once several nodes have a file, the origin need not serve it again. Bandwidth is pooled
across all seeders. Torrent files are small metadata descriptors. Zero infrastructure cost for the
publisher (beyond initial seeding). The Internet Archive's BitTorrent integration is a direct
model for open-repo's Reference Export distribution.

**Disadvantages**: BitTorrent does not address structured data sync (ContentItem records). It
distributes immutable files, not live databases. DHT peer discovery leaks node participation to
passive observers. Requires a persistent seeder to maintain swarm health; if all seeders go
offline, content becomes unavailable. No native content-addressed verification beyond info-hash.
BitTorrent is the right tool for ZIM file distribution, not for ContentItem synchronization.

**Verdict**: Use for ZIM archive distribution as a supplementary channel alongside CDN. Generate
`.torrent` files for each ZIM export and seed from the open-repo node. Integration with the
Internet Archive's BitTorrent seeding infrastructure for Reference Exports is a high-value, low-
effort enhancement.

#### Option C: IPFS (Content-Addressed Distributed Storage)

**Mechanism**: Content is addressed by its hash (CID). Nodes pin content they want to retain.
Any node with a CID can serve that content to any other node requesting it. The DHT maps CIDs to
providing peers.

**Advantages**: Content-addressed verification is native and cryptographically strong — a CID
computed from a file's hash uniquely identifies that file. Content retrieval is location-
independent: if Node A has a file, any other node can retrieve it from A without knowing A's
address in advance (DHT lookup). Supports offline transfer via CAR (Content Addressable aRchive)
files — similar to TAR but content-addressed — which can be transferred over USB/sneakernet and
imported into IPFS without network connectivity. The ORCESTRA atmospheric research campaign (2025)
demonstrated IPFS sync on a Raspberry Pi and notebooks with intermittent connectivity, showing
practical viability for exactly the edge-device scenario open-repo targets.

**2025 improvements**: Kubo v0.39 rebuilt the DHT with efficient CID sweep (handles hundreds of
thousands of CIDs without memory issues). Bitswap protocol improvements yielded 50–95% bandwidth
reduction and 80–98% message volume reduction. Helia (JavaScript IPFS implementation) provides
verified fetch via Service Workers, enabling browser-based IPFS without a full node.

**Disadvantages**: Running a full Kubo node requires 512 MB RAM minimum (recommended 6 GB); this
is marginal on a Raspberry Pi 3 (1 GB RAM) but viable on a Pi 4 (2–8 GB). Default storage
quota: 10 GB (configurable). The public IPFS network participates in content routing with any
peer, which may be undesirable for private institutional deployments. Iroh (an alternative IPFS
implementation by n0) is lighter-weight and designed for embedded/edge scenarios, but trades
public network compatibility for performance — it does not participate in the main Amino DHT.

**Verdict for ZIM distribution**: IPFS is the preferred transport for ZIM archive distribution.
CIDs provide the content-addressed verification that signed releases need. CAR file export enables
offline ("sneakernet") distribution. Public pinning services (Filebase, Pinata, web3.storage) can
act as always-on seeders, eliminating the need for open-repo nodes to remain online.

**Verdict for ContentItem sync**: IPFS is not a database sync protocol. Use IPFS for immutable
export distribution; use a structured sync protocol (see §2.4) for live database replication.

#### Option D: libp2p / Custom Sync Protocol

**Mechanism**: Build a direct peer-to-peer sync layer using libp2p primitives (multiplexed
streams, Kademlia DHT peer routing, Gossipsub pub/sub for change notifications). This is the
approach taken by Matrix homeservers and ActivityPub implementations.

**Advantages**: Maximum flexibility. Can be tuned for open-repo's exact data model. No dependency
on IPFS DHT. Gossipsub v1.1 supports peer exchange bootstrapping from a small set of initial
nodes, enabling network formation without a central directory.

**Disadvantages**: Highest implementation cost. libp2p has no production Python implementation
as of 2026 (go-libp2p and rust-libp2p are primary; py-libp2p exists but is immature). Building
a custom sync protocol requires implementing conflict resolution, version vectors, and security
hardening from scratch. The existing ActivityPub/HTTP signature infrastructure (Phase 4) already
provides a partial sync mechanism; extending it is lower risk.

**Verdict**: Not recommended for Phase 5. The existing ActivityPub federation is already a
libp2p-style protocol. Phase 5 should extend it for pull-based sync rather than introducing a
second P2P layer.

### 2.4 Recommended Architecture: Hybrid Model

The recommended Phase 5 distributed sync architecture is a three-layer hybrid:

```
Layer 1: Content sync        →  ActivityPub pull-sync (extends Phase 4)
Layer 2: Archive distribution →  IPFS (primary) + BitTorrent (secondary)
Layer 3: Metadata/discovery  →  Git-backed export metadata + .well-known peer list
```

**Layer 1: ActivityPub Pull-Sync for ContentItem Records**

Phase 4 already implements push-based federation: Node A pushes an `Announce` activity to Node
B's `/inbox` when a new endorsement occurs. Phase 5 extends this with a pull-based sync endpoint
that allows Node B to catch up after a period of disconnection.

New endpoint:
```
GET /api/federation/sync?since={ISO8601}&partner_id={id}&limit=200
Authorization: HTTP Signature (Phase 4 key)
```

Response:
```json
{
  "activities": [...],  // Activity objects since `since` timestamp
  "content_items": [...],  // ContentItem records created/updated since `since`
  "next_cursor": "2026-04-29T14:32:00Z",
  "has_more": true
}
```

Node B calls this endpoint on reconnection, using the timestamp of its last successful sync as
the cursor. HTTP Signature verification (Phase 4) gates access: only trusted partners receive
the sync feed. This is the same security model as Phase 4's inbox, applied to a pull interface.

**Conflict resolution**: Open-repo's ContentItem records are append-only by design (new items are
created, existing items are not edited in place — edits create new versions). This eliminates
most conflict scenarios. If the same CID exists on two nodes with different metadata, the node
with the higher `updated_at` wins. For endorsements (Activity records), the authoritative state
is the union of all `Announce` activities minus all `Undo` activities — set semantics with no
ordering conflicts.

**Layer 2: IPFS for ZIM Archive Distribution**

Each ZIM export is:
1. Added to the local IPFS node: `ipfs add --pin open-repo_en_nopic_2026-04.zim`
2. The resulting CID stored in the `zim_exports` database row alongside the R2 URL
3. Published to the OPDS catalog as an alternate download link:
   `ipfs://bafy...{CID}/open-repo_en_nopic_2026-04.zim`
4. Announced to trusted federation partners via the sync endpoint (partners can pin the CID)

For nodes without an IPFS daemon (most lightweight deployments): the CID and CAR file are
sufficient for verification. A user can download the ZIM from CDN and verify it against the CID
without running IPFS. For nodes with IPFS: they can retrieve the ZIM directly from the network
if the CDN is unavailable.

**Offline transfer (sneakernet)**: CAR files serialize the IPFS DAG into a single portable file:
```
ipfs dag export {CID} > open-repo_en_nopic_2026-04.car
```
This CAR file can be copied to a USB drive, carried to an offline node, and imported:
```
ipfs dag import open-repo_en_nopic_2026-04.car
```
The CID is self-verifying — import will fail if any block is corrupted. This is the primary
mechanism for air-gapped or very-low-bandwidth deployments (e.g., satellite uplinks at <10 KB/s).

**Layer 3: Git-Backed Export Metadata**

The `zim_exports` table metadata (not the binary files) is serialized to JSON and committed to
the open-repo repository under `infrastructure/exports-metadata/`. Each export job appends one
JSON file:
```
infrastructure/exports-metadata/
  2026-04-01_open-repo_en_nopic.json
  2026-04-01_open-repo_en_agriculture.json
  2026-04-07_open-repo_en_nopic.json
```

Each file contains: filename, period, flavour, SHA-256 checksum, IPFS CID, R2 URL, item count,
generated_at timestamp. This Git record serves as the authoritative history of published exports
and enables downstream tooling (pinning bots, mirrors, institutional archivists) to discover and
verify all historical exports without querying the live API.

### 2.5 Security Model

**Content trust chain**: Every distributed artifact traces back to the node's Phase 4 identity:

```
Node Identity (RSA keypair, Phase 4)
    │
    ├── HTTP Signatures on ActivityPub activities (Phase 4 existing)
    │
    ├── Signed export manifest (Phase 5):
    │   GPG sign manifest.json with node's private key
    │   Manifest contains SHA-256 checksums + IPFS CIDs for all exports
    │
    └── ZIM file integrity (Phase 5):
        SHA-256 checksum sidecar + IPFS CID (content-addressed)
```

**Pull-sync authorization**: The `/api/federation/sync` endpoint requires HTTP Signature
authentication (same mechanism as Phase 4's `/inbox`). Only partners with `trust_status=trusted`
in `federation_partners` table receive sync responses. This prevents unauthorized nodes from
harvesting all content.

**IPFS privacy**: The public IPFS DHT announces pinned CIDs to the global network, which reveals
which content a node has stored. For private institutional deployments, run a private IPFS
swarm (using `--swarm-key` to create an isolated network) or distribute CAR files via the R2 CDN
without using the public DHT. The architecture accommodates both modes.

**Conflict-free trust**: Because open-repo uses append-only content (no in-place edits, only new
versions) and set-based endorsements (union of Announce minus Undo), there are no Byzantine
fault scenarios in the content model. A malicious node can send fake activities, but Phase 4's
HTTP Signature verification gates ingestion. A node that sends invalid activities gets its
`trust_status` downgraded to `untrusted` after repeated failures.

### 2.6 Edge Device Constraints

**Raspberry Pi 4 (reference edge device)**:
- RAM: 2–8 GB available. Kubo recommends 6 GB for comfortable operation; 2 GB is marginal but
  usable with `Swarm.ResourceMgr.MaxMemory` set to 1 GB and `Datastore.StorageMax` set to 8 GB.
  For Pi 3 (1 GB RAM), skip Kubo and use only CAR file import/export.
- Storage: A 32 GB microSD is sufficient for 3–5 ZIM domain exports plus the IPFS datastore.
  A 64 GB card (approximately $12) provides comfortable headroom.
- Bandwidth: The pull-sync endpoint uses cursor-based pagination (200 items per page) to avoid
  large payloads over slow connections. ZIM files (5–80 MB) are practical over connections as
  slow as 1 Mbps (5–80 seconds). For satellite/VSAT links (64 Kbps), use CAR file sneakernet.
- Power: Raspberry Pi 4 draws ~3–6W. An edge node in a field office with 8 hours of grid power
  per day can sync once per day during the power window.

**Bandwidth-constrained sync protocol**: The pull-sync endpoint supports a `fields` parameter
to fetch only metadata (title, CID, domain, updated_at) without full content for the initial
delta discovery:
```
GET /api/federation/sync?since=2026-04-28T00:00:00Z&fields=cid,title,updated_at
```
The client then requests full content only for items it doesn't already have (by CID). This
pattern reduces sync traffic by 60–80% when most items have not changed.

---

## 3. Technology Evaluation Matrix

### 3.1 Export Format Comparison

| Criterion | ZIM | SQLite | JSON | IPFS CAR |
|---|---|---|---|---|
| **Compressed size** | Excellent (zstd cluster compression, 3x ratio) | Good (WAL mode; compress externally) | Poor (text overhead; compress externally) | Moderate (content-addressed blocks; no additional compression) |
| **Random access** | Excellent (cluster offsets, O(1) article lookup) | Excellent (B-tree index) | Poor (full scan required) | Poor (must traverse DAG) |
| **Embedded search** | Excellent (Xapian FTS built in) | Good (FTS5 extension) | None | None |
| **Reader ecosystem** | Excellent (Kiwix: Android, iOS, macOS, Windows, Linux, browser extension, kiwix-serve) | Moderate (requires custom reader; DB Browser for SQLite) | Minimal (requires custom reader) | None (raw format; requires IPFS tooling) |
| **Mobile deployment** | Excellent (official Kiwix Android app, no extra tooling) | Moderate (SQLite native on Android; no reader app exists) | Poor (requires custom app) | Poor (IPFS not mobile-ready without Iroh) |
| **Institutional deployment (server)** | Excellent (kiwix-serve Docker, one command) | Moderate (requires custom server) | Moderate (any static file server) | Moderate (requires IPFS node) |
| **Interoperability** | Excellent (open standard, 10M+ downloads/year) | Good (universal SQLite support) | Excellent (universally parseable) | Moderate (IPFS ecosystem only) |
| **Ease of generation** | Good (python-libzim, wheel available; API learning curve) | Excellent (Python sqlite3 stdlib) | Excellent (json.dumps) | Moderate (requires libipfs or CAR tooling) |
| **Integrity verification** | Good (zimcheck validator; no native signing) | Poor (no standard integrity check) | Poor (no standard integrity check) | Excellent (CID is content hash; self-verifying) |
| **Archival suitability** | Excellent (widely accepted by libraries and archives) | Good (SQLite is an archival format, ISO/IEC 14598) | Moderate (human-readable but fragile) | Good (content-addressed, permanent if pinned) |

**Recommendation**: ZIM is the primary export format. IPFS CAR is used as a transport/verification
layer alongside ZIM, not as an alternative format. SQLite export is a Phase 5.1 option for
developers who want programmatic access to the dataset without a ZIM reader. JSON dumps are
reserved for backup and debugging.

### 3.2 Sync Transport Comparison

| Criterion | Git-based | BitTorrent | IPFS (Kubo) | ActivityPub pull-sync |
|---|---|---|---|---|
| **Ease of implementation** | High (git CLI, existing infrastructure) | Moderate (torrent library; tracker setup) | Moderate (Kubo daemon; IPFS API) | High (extends Phase 4 HTTP API) |
| **Data model fit** | Poor (file-oriented; JSON serialization needed) | Poor (immutable-file-only; no DB sync) | Poor for DB sync; Excellent for files | Excellent (native ContentItem and Activity records) |
| **Resilience** | Moderate (requires git server or hosting) | Excellent (swarm-based; no central point) | Excellent (DHT; any node can serve) | Moderate (requires at least one online peer) |
| **Bandwidth efficiency** | Moderate (git pack compression; LFS for large files) | Excellent (swarm; origin serves once) | Excellent (Bitswap: 50–95% reduction in 2025) | High (cursor pagination; field selection; delta sync) |
| **Security** | Good (HTTPS; SSH keys) | Poor (DHT leaks participation; no auth) | Moderate (TLS; content-addressed but no access control on public DHT) | Excellent (inherits Phase 4 HTTP Signatures and trust model) |
| **Edge device suitability** | Moderate (git on Pi is fine; LFS is heavyweight) | Moderate (requires torrent client) | Poor on Pi 3 (RAM); Good on Pi 4 | Excellent (HTTP only; minimal deps) |
| **Conflict resolution** | Good (git merge for text; poor for binary) | None (immutable files only) | None (CIDs are immutable; versioning manual) | Excellent (append-only model eliminates most conflicts; timestamp wins for metadata) |
| **Discovery** | Poor (requires known remote URL) | Moderate (DHT for peer discovery; trackers) | Good (Kademlia DHT; content routing) | Good (.well-known peer list; manual registration) |
| **Offline/sneakernet** | Moderate (git bundle files) | Poor (no offline mode) | Excellent (CAR files; USB transfer; self-verifying) | Poor (requires live HTTP connection) |
| **Maturity** | Excellent | Excellent | Good (production since 2015; major 2025 improvements) | Good (ActivityPub spec stable; open-repo implementation new) |

**Recommendation by use case**:
- ContentItem and Activity record sync: ActivityPub pull-sync (Layer 1)
- ZIM archive distribution (online): IPFS + CDN (Layer 2)
- ZIM archive distribution (offline): IPFS CAR files via USB/sneakernet (Layer 2)
- ZIM archive distribution (community seeding): BitTorrent (Layer 2 supplementary)
- Export metadata tracking: Git (Layer 3)

---

## 4. Phase 5 Implementation Roadmap

### 4.1 Prerequisites (Blocking — must complete before Wave 5 starts)

- [ ] Phase 4 PR #1 merged to master
- [ ] `python-libzim` (`libzim>=3.2,<4.0`) added to `pyproject.toml` and verified in CI
- [ ] `feedgen` added to `pyproject.toml` (OPDS catalog generation)
- [ ] Cloudflare R2 bucket provisioned with public read access and correct CORS headers
- [ ] 48×48 PNG logo/icon asset created and committed to `assets/`
- [ ] `zimcheck` binary available in CI (via openzim/zim-tools Docker image or system package)
- [ ] `zim_exports` database migration committed and ready

### 4.2 Wave 5 Phase 1: Kiwix Export Pipeline (Weeks 1–4)

**Goal**: A running export pipeline that generates valid ZIM files, passes zimcheck, and uploads
to R2. No distributed sync yet.

**Deliverables and sequence** (items at the same level run in parallel):

```
Level 1 (Week 1):
  [ContentItem query layer + stream interface]
  [HTML template (self-contained, no external deps)]
  [ZimWriter full implementation (python-libzim)]

Level 2 (Week 2, requires Level 1):
  [ExportJob background task (FastAPI BackgroundTask)]
  [zimcheck subprocess validation integration]
  [SHA-256 checksum computation and sidecar]
  [R2 upload integration (boto3 with R2 endpoint)]

Level 3 (Week 3, requires Level 2):
  [Export API endpoints: POST /api/exports, GET /api/exports/{job_id}, GET /api/exports]
  [OPDS catalog endpoint: /opds/v2/root.xml (feedgen-based)]
  [Retention policy implementation]
  [zim_exports DB schema + Alembic migration]

Level 4 (Week 4, requires Level 3):
  [Scheduled exports (APScheduler or Celery Beat cron)]
  [End-to-end test: generate ZIM → zimcheck → R2 upload → OPDS entry]
  [Domain export variants (3 initial domains)]
  [User documentation: Android, desktop, kiwix-serve]
```

**Key integration test (Checkpoint 3 from implementation plan)**: Generate a ZIM file from 10–50
real content items. Run `zimcheck output.zim`. All subsequent work assumes this passes.

**Effort estimate**: 16–22 days (1 FTE). Wide range reflects HTML template complexity and
whether APScheduler is already present from Phase 4.

### 4.3 Wave 5 Phase 2: Distributed Node Sync (Weeks 5–8)

**Goal**: Nodes can sync ContentItem records and ZIM archives without persistent connections.

**Deliverables**:

```
Level 1 (Week 5, parallel):
  [Pull-sync endpoint: GET /api/federation/sync with cursor pagination]
  [IPFS daemon integration: ipfs add + pin on export completion]
  [.well-known/open-repo-peers.json endpoint]

Level 2 (Week 6, requires Level 1):
  [CID storage in zim_exports table]
  [CAR file export on demand: GET /api/exports/{job_id}/car]
  [IPFS CID in OPDS catalog entries as alternate link]
  [Pull-sync client: triggered on node startup if last_sync > 6 hours ago]

Level 3 (Week 7, requires Level 2):
  [Sync conflict resolution: timestamp-wins for metadata; set-union for activities]
  [Signed export manifest: GPG sign manifest.json with node's Phase 4 key]
  [BitTorrent .torrent file generation for each ZIM export]
  [Git-backed metadata export to infrastructure/exports-metadata/]

Level 4 (Week 8, requires Level 3):
  [Bandwidth-constrained sync: ?fields= parameter for delta discovery]
  [Edge device documentation (Raspberry Pi setup guide)]
  [Integration tests: offline CAR import, sync catch-up after 48h offline]
```

**IPFS implementation note**: Use Kubo's HTTP API (`http://localhost:5001/api/v0/`) from the
Python backend rather than embedding a Go library. This keeps the dependency boundary clean:
the Python service talks to Kubo over HTTP, and Kubo manages the IPFS datastore. If Kubo is not
running (lightweight deployments), the IPFS integration degrades gracefully: CIDs are still
computed and stored (using the `multihash` Python library) but files are not added to the public
DHT. The CDN URL remains the primary download path.

**Effort estimate**: 14–20 days (1 FTE). The pull-sync endpoint reuses most Phase 4 plumbing;
IPFS integration and CAR file tooling are the new surface area.

### 4.4 Wave 5 Phase 3: Offline-First Mobile Client (Stretch Goal, Weeks 9–12)

**Status**: Stretch goal. Do not block Phase 1 or Phase 2 on this.

**Goal**: A lightweight web application that works offline using Service Workers, backed by a
local ZIM file (served by kiwix-serve) or by the Helia/IPFS verified fetch API. The mobile
client is primarily for NGO field workers who need to browse the knowledge base on a phone
without installing Kiwix.

**Approach**: Progressive Web App (PWA) with Service Worker caching the static app shell and
routing content requests to a local kiwix-serve instance (`http://localhost:8080`) or to the
IPFS gateway (Helia in-browser, using Helia's verified fetch via Service Workers as demonstrated
in 2025). This is analogous to how Wikipedia's offline PWA works.

**Dependencies**: Phase 1 ZIM pipeline complete. kiwix-serve running locally or accessible on
LAN. Helia browser library for IPFS-backed mode.

**Effort estimate**: 10–15 days (1 FTE, requires frontend skills).

### 4.5 Dependencies and Risk Register

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Phase 4 PR #1 blocks all Phase 5 | Certain (it is the dependency) | High | Preliminary work (stubs, tests, docs) done now; full implementation starts on merge |
| python-libzim version conflict | Low | Medium | Pin `libzim>=3.2,<4.0`; test in clean venv before adding |
| zimcheck rejects ZIM for non-obvious reason | Low | Medium | Run zimcheck in CI with `--verbose`; test known-good minimal ZIM first |
| Kubo RAM usage exceeds Pi constraints | Medium | Medium | Set `Swarm.ResourceMgr.MaxMemory=1g`; use CAR-only mode on Pi 3 |
| IPFS public DHT reveals private node content | Medium (for private deployments) | Medium | Use private swarm key for institutional deployments; document clearly |
| BitTorrent swarm dies if all seeders offline | Medium | Low | Primary distribution via R2; BitTorrent is supplementary; seed from Internet Archive |
| Pull-sync endpoint overwhelmed by large catch-up | Low | Medium | Cursor pagination (200 items/page); `Retry-After` header if too many requests |
| Android Kiwix Play Store path restrictions | Medium | Low | Document F-Droid Kiwix as primary path; in-app OPDS catalog as UX |
| HTML template includes external dependencies | Medium | High | CI test: BeautifulSoup scan of exported HTML; fail on any external `src`/`href` |
| OPDS XML malformed, rejected by Kiwix | Medium | Medium | Use feedgen's built-in validation; test against kiwix-serve in CI |
| ContentItem schema inconsistency with ZimWriter assumptions | Medium | Medium | API contract validation (Checkpoint 2): verify schema before HTML template work |

### 4.6 Timeline Estimate

| Wave | Phase | Weeks | Effort (1 FTE) | Gate |
|---|---|---|---|---|
| Pre-work | Preliminary stubs and docs | Done | 7.5 days | Phase 4 PR #1 merge |
| Wave 5.1 | Kiwix export pipeline | Weeks 1–4 | 16–22 days | First ZIM passes zimcheck |
| Wave 5.2 | Distributed node sync | Weeks 5–8 | 14–20 days | CAR file import works offline |
| Wave 5.3 | Mobile client (stretch) | Weeks 9–12 | 10–15 days | PWA serves offline content |
| **Total** | | **9–12 weeks** | **40–57 days** | |

**Go/no-go decision point**: After Wave 5.1 Checkpoint 4 (first production ZIM deployed to R2
and accessible in Kiwix Android), reassess Wave 5.2 priority against competing roadmap items.
If node sync is lower priority than Phase 6 federation features at that point, Wave 5.2 can slip
to Phase 5.1 without blocking any other work.

---

## 5. Success Criteria

### Wave 5.1 Complete When:

- [ ] `POST /api/exports` triggers a background export job and returns a job ID
- [ ] Full export ZIM (`open-repo_en_nopic_YYYY-MM.zim`) passes `zimcheck` with zero errors
- [ ] Domain exports work for at least 3 domains (agriculture, water, electronics)
- [ ] ZIM opens in Kiwix Android (F-Droid) and all articles are readable
- [ ] ZIM opens in Kiwix desktop (Linux) and full-text search returns relevant results
- [ ] kiwix-serve serves the ZIM from Docker; articles accessible via browser
- [ ] OPDS endpoint at `/opds/v2/root.xml` returns valid Atom XML
- [ ] SHA-256 checksum sidecar published alongside each ZIM
- [ ] No external HTTP references in exported HTML (CI enforced via BeautifulSoup scan)
- [ ] Scheduled export job runs weekly without manual intervention
- [ ] Monthly storage cost under $5

### Wave 5.2 Complete When:

- [ ] `GET /api/federation/sync?since={timestamp}` returns delta ContentItems and Activities
- [ ] Only trusted federation partners (Phase 4 trust model) can access sync endpoint
- [ ] IPFS CID stored in `zim_exports` table for every published ZIM
- [ ] CAR file available for every ZIM via `GET /api/exports/{job_id}/car`
- [ ] CAR file imported into an offline IPFS node produces the correct CID (self-verifying)
- [ ] `.well-known/open-repo-peers.json` published and parseable by new nodes
- [ ] Signed export manifest (`manifest.json`) generated and GPG-verifiable
- [ ] BitTorrent `.torrent` file available for each ZIM export
- [ ] Edge device documentation covers Raspberry Pi 4 setup (Kubo + sync client)
- [ ] Integration test: simulate 48-hour offline period, reconnect, verify catch-up completes

---

## 6. Cross-References

The following prior documents remain authoritative on their specific subsystems:

- `phase-5-kiwix-architecture.md` — ZIM format internals, Kiwix ecosystem, tool selection
  rationale, Wikipedia/Project Gutenberg pipeline comparisons
- `phase-5-offline-export-architecture.md` — ZIM metadata specification, naming convention,
  CDN infrastructure (R2 vs B2 vs S3 cost analysis)
- `phase-5-export-strategy.md` — Export variants in detail, scoping SQL queries, incremental
  update strategy, accessibility requirements, retention policy with code
- `phase-5-kiwix-integration-guide.md` — python-libzim API surface, OPDS catalog structure,
  CDN deployment configuration, offline reader distribution paths
- `phase-5-implementation-plan.md` — Effort estimates, dependency tree (Level 0–5), known risks,
  post-launch maintenance plan, checkpoint criteria

---

## Sources

- [IPFS Foundation: Content Addressing 2025 In Review](https://ipfsfoundation.org/content-addressing-2025-in-review/)
- [IPFS Documentation: How IPFS Works](https://docs.ipfs.tech/concepts/how-ipfs-works/)
- [Kubo GitHub: IPFS Implementation in Go](https://github.com/ipfs/kubo)
- [Iroh: Lightweight IPFS Implementation](https://www.iroh.computer/docs/ipfs)
- [IPLD CARv1 Specification](https://ipld.io/specs/transport/car/carv1/)
- [Syncthing Block Exchange Protocol v1](https://docs.syncthing.net/specs/bep-v1.html)
- [Syncthing: Understanding Synchronization](https://docs.syncthing.net/users/syncing.html)
- [Syncthing 2.0 Release (August 2025)](https://www.webpronews.com/syncthings-quiet-revolution-mastering-peer-to-peer-file-sync-in-a-cloud-dominated-world/)
- [libp2p Gossipsub v1.1 Specification](https://github.com/libp2p/specs/blob/master/pubsub/gossipsub/gossipsub-v1.1.md)
- [libp2p Kademlia DHT Peer Discovery](https://medium.com/rahasak/libp2p-pubsub-peer-discovery-with-kademlia-dht-c8b131550ac7)
- [Internet Archive BitTorrent Distribution](https://help.archive.org/help/archive-bittorrents/)
- [Pinata: Kubo vs Helia vs Elastic-IPFS Comparison](https://pinata.cloud/blog/kubo-vs-helia-vs-elastic-ipfs-comparing-the-major-ipfs-implementations-ease-of-working-with/)
- [openZIM ZIM Naming Convention](https://wiki.openzim.org/wiki/ZIM_Naming_Convention)
- [openZIM ZIM Updates v2 Retention Model](https://wiki.openzim.org/wiki/ZIM_Updates)
- [python-libzim ReadTheDocs](https://python-libzim.readthedocs.io/)
- [Cloudflare R2 Pricing](https://developers.cloudflare.com/r2/pricing/)
- [openzim/zim-requests (Catalog Submission)](https://github.com/openzim/zim-requests)
- [OPDS Catalog Spec on Kiwix Wiki](https://wiki.kiwix.org/wiki/OPDS)
- [How to Run IPFS on a Raspberry Pi (Pinata)](https://pinata.cloud/blog/how-to-run-ipfs-on-a-raspberry-pi/)
- [Phase 4 Design: Federation Partner Management](../WAVE_4_DESIGN.md)
- [Phase 6 Federation Roadmap](../ITEM15_PHASE6_FEDERATION_ROADMAP.md)
