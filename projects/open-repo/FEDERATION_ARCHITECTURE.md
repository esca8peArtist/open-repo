---
title: "Phase 5.3 Federation Architecture — Peer-to-Peer ZIM Library Sharing"
project: open-repo
phase: "5.3 design"
status: design-proposal
created: 2026-05-22
author: General Research Agent
depends_on:
  - PHASE_5_ARCHITECTURE.md
  - PHASE_5.2_IMPLEMENTATION_ROADMAP.md
  - ITEM15_PHASE6_FEDERATION_ROADMAP.md
deadline: 2026-05-30
tags: [federation, p2p, zim, ipfs, bittorrent, identity, trust, offline-first]
---

# Phase 5.3 Federation Architecture
## Peer-to-Peer ZIM Library Sharing Without Central Servers

---

## Executive Summary

Phase 5.1 proved that open-repo can export valid ZIM archives and distribute them via CDN. Phase 5.2 adds domain-specific content coverage. Phase 5.3 addresses the long-term distribution problem: how do community libraries — a clinic in rural Kenya, a seed bank in Appalachia, a school network in coastal Bangladesh — share ZIM files and updates with each other when there is no reliable centralized server, no always-on internet, and no dedicated IT staff?

The core design choice in Phase 5.3 is to treat ZIM files as content-addressed artifacts that can be discovered, verified, and transferred through multiple parallel channels simultaneously. No single channel is required to work at any given moment. A community library that can reach another library via Bluetooth, local Wi-Fi, a USB drive carried by a courier, a satellite uplink once a week, or a BitTorrent swarm on intermittent 3G should be able to use whichever channel is available right now, with the same verification guarantees regardless of transfer method.

The three mechanisms that make this work together are:

1. **Content addressing via SHA-256 / IPFS CIDs**: Every ZIM file is identified by a hash of its content, not by a URL. Any transfer method that delivers a file with the correct hash is trustworthy.
2. **Signed manifests**: Each publishing library signs a manifest listing its current ZIM files by CID. Peers can verify the manifest against the publisher's public key without a certificate authority.
3. **Multi-channel transfer**: IPFS pinning, BitTorrent seeding, kiwix-serve HTTP, and USB/sneakernet are all valid transfer paths. The protocol layer is agnostic to which channel succeeded.

This document designs the federation layer for Phase 5.3. Versioning strategy and differential sync are addressed in companion documents `VERSIONING_STRATEGY.md` and `DIFFERENTIAL_SYNC_PROTOCOL.md`.

---

## 1. Problem Statement

### 1.1 What "Federated Library" Means in This Context

In Phase 5.1–5.2, the distribution model is hub-and-spoke: a central export pipeline generates ZIM files, uploads them to Cloudflare R2, and users download from the CDN. This model has real limitations for the target deployment environments:

- A clinic network in a region with 2G connectivity cannot reliably download a 300 MB ZIM from a CDN on demand. The download fails mid-stream, resumes from scratch, and consumes prepaid data budgets.
- A community library that has collected local adaptations (translated procedures, region-specific seed varieties, locally validated medical protocols) cannot contribute them back to the network without administrator access to the central pipeline.
- Two community libraries in the same region cannot share their ZIM collections with each other without routing through a central server, even when they have a 100 Mbps local Wi-Fi link between them.
- A region under network disruption (natural disaster, infrastructure failure, political restriction) loses access to the entire library if the CDN is the only distribution point.

Phase 5.3 federation solves this by making every community library node both a consumer and a potential publisher and relay. The CDN remains as an optional bootstrap and high-bandwidth seed, but it is not required for library sharing to function.

### 1.2 Constraints

The design must satisfy all of the following:

| Constraint | Rationale |
|---|---|
| **Offline-first** | Must work when both peers have no internet access; local transfer channels must be sufficient |
| **No central authority required** | No server that, if it goes down, breaks the network |
| **Open source only** | No proprietary sync services; all components must be auditable and self-hostable |
| **Low-bandwidth differential sync** | A 1 MB patch should ship a 1 MB payload, not re-download the full ZIM |
| **Tamper-evident** | A corrupted or maliciously modified ZIM must be detectable without trusting the transfer channel |
| **Non-technical operators** | Community library staff are not developers; the UX must not require CLI competence |
| **Graceful degradation** | Every feature must degrade safely if a component is unavailable |

---

## 2. Reference Systems and What Open-Repo Can Learn

Before designing the open-repo federation layer, it is worth examining how three existing systems solve related problems, and where their designs fall short for the offline library use case.

### 2.1 IPFS

IPFS is a peer-to-peer hypermedia protocol that uses content addressing (CIDs — cryptographic hashes of content) to identify and retrieve data. Any node that has a file can serve it; requestors find providers through a Kademlia DHT. IPFS is the most relevant reference for content addressing and deduplication.

**What open-repo takes from IPFS**:
- Content identifiers (CIDs) as the canonical identity for each ZIM file and each delta patch. A CID is computed once, is location-independent, and enables tamper verification without trust in any specific peer.
- The concept of "pinning" — a node declares that it is responsible for keeping a specific CID available. Open-repo community libraries can "pin" ZIM files they want to maintain locally and serve to peers.
- IPFS CAR (Content Addressable aRchive) files as a transport-agnostic container for ZIM content chunks, usable over USB or Bluetooth even without an IPFS daemon.

**What open-repo does not take from IPFS**:
- DHT dependency. The IPFS DHT requires internet connectivity for peer discovery. Open-repo cannot depend on DHT for local network sharing.
- The IPFS daemon itself is heavyweight (Go binary, memory-intensive) and inappropriate for Raspberry Pi deployments with 1 GB RAM. Open-repo uses IPFS addressing as a naming convention, not as a required runtime service.
- Garbage collection complexity. IPFS's block-level storage model is powerful but operationally opaque for non-technical librarians. Open-repo treats ZIM files as atomic units, not decomposed IPFS blocks.

### 2.2 BitTorrent / DHT

BitTorrent v2 (BEP 52) uses per-file SHA-256 Merkle trees, enabling chunk-level verification and deduplication. BitTorrent DHT enables tracker-independent peer discovery. BitTorrent is the most mature technology for distributing large binary files across an open peer network.

**What open-repo takes from BitTorrent**:
- `.torrent` metadata files as a self-contained description of a ZIM file: the file's SHA-256 hash, file size, and a list of piece hashes for chunk-level verification. A `.torrent` file can be transferred via USB and used offline with a local swarm (LAN peers), even without internet trackers.
- Piece-level verification: downloading peers can verify each 512 KB or 1 MB chunk independently, enabling safe resumption after interrupted transfers without re-downloading completed chunks.
- Tracker + DHT + PEX (Peer Exchange) as three independent discovery mechanisms. If trackers are down, DHT works. If DHT is down, peers already connected can exchange peer lists via PEX.

**What open-repo does not take from BitTorrent**:
- Swarm participation as a default expectation. Many community library deployments cannot maintain open ports or seed continuously. Seeding should be opt-in.
- The tracker ecosystem. Open-repo needs its own lightweight tracker or must use DHT bootstrap nodes it controls, rather than depending on public BitTorrent infrastructure.

### 2.3 Secure Scuttlebutt (SSB)

Secure Scuttlebutt is a peer-to-peer gossip protocol built around append-only, cryptographically signed identity feeds. Each identity has an Ed25519 keypair; every message is signed by the identity's long-term key, chained to the previous message's SHA-256 hash. This creates an immutable, tamper-evident log — exactly the property needed for library audit trails.

**What open-repo takes from SSB**:
- The append-only feed model for audit logs: every version event (proposal, acceptance, rejection, key rotation) is appended as a signed, chained entry. Tampering with any entry breaks the chain from that point forward.
- The gossip sync approach: when two SSB peers connect, they exchange vector clocks listing which feed entries each has. Only the missing entries are transferred. This is bandwidth-efficient and works over any transport — TCP, Bluetooth, USB file copy.
- Content-addressed blobs referenced by SHA-256 hashes: the same CID model used in the open-repo ZIM manifest.

**What open-repo does not take from SSB**:
- SSB's full social graph (following, unfollowing, blocking) is too heavyweight for the library use case. Open-repo's trust model is simpler: a fixed peer list with explicit trust levels, not a dynamic follow graph.
- SSB requires knowing which feeds to replicate, determined by the social graph. Open-repo uses domain-scoped peer lists and manifest polling instead.
- SSB's `EBT` (Epidemic Broadcast Trees) replication protocol is powerful but assumes always-on connectivity. Open-repo's sync is scheduled and batch-oriented, not real-time streaming.

### 2.4 Briar / Bramble Protocol

Briar is a messaging application built for activists and journalists in adversarial environments. Its Bramble protocol suite handles synchronization across Bluetooth, Wi-Fi Direct, Tor, and USB — exactly the transport stack that open-repo's sneakernet and LAN-sharing scenarios require.

**What open-repo takes from Briar**:
- The transport-agnostic sync design: Briar's Bramble Transport Protocol (BTP) defines a common interface for payload delivery that is independent of whether the underlying channel is Bluetooth, Wi-Fi Direct, or USB. Open-repo's multi-channel approach (HTTP, BitTorrent, IPFS, USB bundle) should similarly define a common verification layer that operates identically regardless of how bytes arrived.
- Contact verification via QR code: Briar exchanges public keys via QR code scans for initial trust establishment. Open-repo's out-of-band Library ID exchange should support QR code display/scan in the UI for the common case of two librarians in the same room exchanging peer credentials.
- Store-and-forward relay: Briar allows a mutual contact to carry encrypted messages between disconnected parties. The analogous mechanism in open-repo is the USB courier carrying a signed manifest and ZIM delta bundle — the courier is a relay who does not need to understand or decrypt the content.

**What open-repo does not take from Briar**:
- Briar's Bramble Onion Protocol (BOP) — Tor integration for metadata resistance — is valuable in adversarial political contexts but adds significant complexity. Phase 5.3 does not require anonymization; Phase 6+ can add a Tor transport option for high-risk deployments.
- Briar's real-time replication over Bluetooth assumes devices are in proximity. Open-repo's offline sync is asynchronous (USB bundles, scheduled network sync) rather than real-time.

### 2.5 ActivityPub / Fediverse

Phase 4 already implements ActivityPub federation for the open-repo web platform. ActivityPub handles content metadata federation (announcements, endorsements, discovery of new items) efficiently. The `ITEM15_PHASE6_FEDERATION_ROADMAP.md` covers ActivityPub in depth.

**What Phase 5.3 takes from ActivityPub**:
- Signed activities as the discovery mechanism. When a library publishes a new ZIM file, it creates a signed ActivityPub `Announce` activity containing the ZIM's CID, version, size, and domain. Peers subscribed to that library receive the announcement and decide whether to fetch the file.
- HTTP Signature key infrastructure already built in Phase 4. The same Ed25519 keypairs used for ActivityPub federation can sign ZIM manifests.
- The concept of a public actor with a discoverable endpoint. Each community library has a URL-addressable identity (the ActivityPub actor) that publishes its library manifest.

**What Phase 5.3 does not take from ActivityPub**:
- ActivityPub is not a file transfer protocol. Announcing a ZIM via ActivityPub does not transfer the ZIM. The announcement contains the CID and the transfer channel URLs; the actual transfer uses IPFS, BitTorrent, HTTP, or sneakernet.
- ActivityPub requires internet connectivity for federation. Fully offline peer discovery must use a separate channel (mDNS, Bluetooth advertisement, or a pre-shared peer list).

### 2.6 IPFS 2025 State: What Has Changed

The IPFS ecosystem changed significantly in 2025 in ways that affect the open-repo federation design. Bitswap (the IPFS block exchange protocol) improvements demonstrated **50–95% bandwidth reductions and 80–98% message volume reduction** in testing, making IPFS more viable for constrained-connectivity environments than it was when Phase 5 was originally designed. The DHT was rebuilt from scratch to handle hundreds of thousands of CIDs without excessive memory usage.

Critically for browser-based open-repo clients: Chrome 137 (May 2025) added native Ed25519 support, joining all other major browsers. This means Ed25519 signatures in the ZIM manifest can be verified in browser JavaScript without a polyfill. This solidifies the Ed25519 Library ID approach as the right cryptographic primitive: it is now universally supported from Raspberry Pi firmware to mobile browsers.

IPFS Helia's `verified-fetch` (a drop-in replacement for the standard Fetch API that verifies content against CIDs) and the Service Worker Gateway (enabling browser-based IPFS retrieval without a daemon) both shipped in 2025. These open a Phase 6 path where a Kiwix-served open-repo library can retrieve IPFS-addressed ZIM chunks directly in the browser, without requiring a local IPFS daemon. Open-repo's current Phase 5.3 design (treating the IPFS daemon as optional) is validated by this direction.

---

## 3. Distributed Identity: Library IDs and Peer Trust

### 3.1 Library Identity

Each community library node has a **Library ID**: an Ed25519 public key presented as a base58-encoded string. The Library ID is the canonical, location-independent identifier for that node. It is stable across IP address changes, domain changes, and operator transitions.

```
Library ID format: LIBID-<base58-encoded Ed25519 public key>
Example: LIBID-5mfFqPJmzGGHGjHxGFdJAHLBZaWgVNnKpBJNzHQnERQ4
```

The private key corresponding to this ID is held exclusively by the library's operator. Loss of the private key means loss of the ability to publish new signed manifests. Key rotation is possible (see section 3.3).

This design is directly analogous to how Syncthing identifies devices (per-device TLS certificates generating stable device IDs) and how IPFS node identity works (Ed25519 keypair generating a PeerID). Neither requires a certificate authority.

### 3.2 Manifest Format

Every library publishes a **signed manifest**: a JSON document listing all ZIM files the library currently offers, signed with its Ed25519 private key.

```json
{
  "schema_version": "1.0",
  "library_id": "LIBID-5mfFqPJmzGGHGjHxGFdJAHLBZaWgVNnKpBJNzHQnERQ4",
  "library_name": "Appalachian Seed and Skills Library",
  "library_url": "https://library.appalachianseeds.org",
  "published_at": "2026-05-22T14:00:00Z",
  "files": [
    {
      "name": "open-repo_en_seed-preservation_2026-05.zim",
      "cid": "bafybeif7ztnhq65lumvvtr4ekcwd2ifwgm3awq4zfr3srh62ukfhasenly",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "size_bytes": 48234567,
      "domain": "seed-preservation",
      "version": "1.2.0",
      "language": "eng",
      "transfer_urls": [
        "https://library.appalachianseeds.org/zim/open-repo_en_seed-preservation_2026-05.zim",
        "ipfs://bafybeif7ztnhq65lumvvtr4ekcwd2ifwgm3awq4zfr3srh62ukfhasenly",
        "magnet:?xt=urn:btih:e3b0c44298fc1c149afbf4c8&dn=open-repo_en_seed-preservation_2026-05.zim"
      ]
    }
  ],
  "signature": "<base64-encoded Ed25519 signature over canonical JSON>"
}
```

The manifest is available at a well-known URL: `https://{library_domain}/.well-known/open-repo-library/manifest.json`

For offline-only libraries (no domain, LAN-only), the manifest is broadcast via mDNS and available at the device's local IP. See section 4.2.

### 3.3 Trust Model: How Libraries Trust Each Other

Trust in the open-repo federation is **explicit and bilateral**, not transitive. Library A trusting Library B does not imply Library A trusts Library B's peers. This is the same trust model used by Syncthing and is appropriate for the threat model: a compromised library in the network should not be able to inject content into libraries that have not explicitly trusted it.

**Trust establishment** happens out-of-band: a librarian at Library A receives Library B's Library ID (via email, QR code, shared document, or in-person exchange) and adds it to Library A's trusted peer list. The peer list is stored locally and includes:

```json
{
  "peers": [
    {
      "library_id": "LIBID-...",
      "library_name": "Rural Health Cooperative",
      "trust_established": "2026-03-15T00:00:00Z",
      "trust_level": "verified",
      "contact": "admin@ruralhealthcoop.org",
      "domains_accepted": ["medical", "water"],
      "auto_sync": true
    }
  ]
}
```

`trust_level` has three values:

| Level | Meaning | Behavior |
|---|---|---|
| `provisional` | Known but unverified | Manifests are downloaded and verified but files not auto-fetched |
| `verified` | Library ID confirmed via out-of-band channel | Files in accepted domains are auto-fetched if `auto_sync: true` |
| `blocked` | Deliberately excluded | Manifests and files from this ID are rejected |

### 3.3.1 Alternative: Vouchsafe Capability Graph (Future Phase)

The bilateral trust model described above is appropriate for Phase 5.3 but may become limiting in Phase 6 when many libraries need to establish trusted relationships efficiently. The Vouchsafe model (Kuri, 2026) offers a zero-infrastructure alternative: a directed capability graph where each node is an identity claim and each edge is a delegated capability encoded as a signed JSON Web Token.

In a Vouchsafe-augmented federation, Library A could issue a signed capability token to Library B saying "I vouch for Library B's medical content authority in domain: malaria-treatment." Library C, which trusts Library A, could accept Library B's medical content based on this vouched capability — without having a direct prior relationship with Library B.

The key property is offline verification: Vouchsafe tokens embed the full cryptographic proof chain, enabling verification without network access to the issuing library. This is relevant for the USB sneakernet case where Library C receives a signed bundle from Library B via USB courier and has no way to phone home to Library A to verify the vouching relationship.

Vouchsafe uses Ed25519 signatures and standard JWT/JWS formats, making it compatible with the Library ID infrastructure already specified in section 3.1. Phase 5.3 does not implement Vouchsafe, but the library identity and signing infrastructure is forward-compatible with it.

**Recommendation**: Phase 5.3 implements bilateral trust (explicit peer lists) as specified. Phase 6+ can layer Vouchsafe capability tokens on top of the existing Ed25519 Library ID infrastructure to enable more scalable trust delegation without abandoning the bilateral trust security model.

### 3.4 Key Rotation

If a library's private key is compromised or lost, it can publish a signed **Key Rotation Notice** from its old key (if available) or initiate an out-of-band rotation:

- **Graceful rotation** (old key available): Library publishes a signed `key_rotation` document from the old key, containing the new public key and a timestamp. Peers that trust the old key update their trust store to the new key automatically.
- **Emergency rotation** (old key lost): Library operator contacts trusted peers directly (email, phone) with the new Library ID. Peers must re-verify the new ID out-of-band and manually update their trust stores.

There is no centralized revocation mechanism. This is acceptable for a community library network where trusted peer lists are small and operators have human-level relationships. The tradeoff is that revocation propagation is slower than in PKI systems.

---

## 4. Library Discovery Protocol

The discovery problem has two distinct sub-problems: how do libraries initially find each other (bootstrap discovery) and how do libraries that already know each other stay updated about new files (ongoing discovery).

### 4.1 Bootstrap Discovery Channels

**Channel 1: Manual peer entry.** A librarian enters a peer's URL and Library ID directly. This is the most reliable mechanism for the initial trust establishment and is always available regardless of network state.

**Channel 2: Public registry (optional).** Libraries that choose to be publicly discoverable can register on a voluntary public index (hosted by the open-repo project or a community operator). The registry is a static JSON file listing Library IDs, library names, domains covered, and contact endpoints. It is not in the trust path — a library appearing in the registry is not automatically trusted; it just enables discovery. Libraries in the registry can be found by browsing a web page or by querying a registry API.

**Channel 3: Local network discovery.** Libraries on the same local network broadcast their presence. Two protocol options are supported:

*Option A: mDNS (Bonjour/Avahi compatible).* A kiwix-serve or open-repo node announces itself as `_open-repo-library._tcp.local` with service fields containing its Library ID and manifest URL. Other nodes discover it via standard mDNS resolution. This works on any platform that supports Bonjour (macOS, Linux with Avahi, Android 9+, iOS, some Windows setups) without requiring configuration.

*Option B: UDP broadcast announcement (Syncthing local discovery model).* For environments where mDNS is filtered or unavailable (some enterprise Wi-Fi configurations, some Android hotspot modes), the node broadcasts a UDP Announcement packet to `255.255.255.255` on port 21028 (IPv4) and multicast group `ff12::8384` on port 21028 (IPv6), containing the Library ID and manifest URL. The broadcast interval is 30–60 seconds. This is the exact model used by Syncthing's Local Discovery Protocol v4, which has proven reliable across a wide variety of network configurations including Raspberry Pi hotspots.

Both options carry the same payload: Library ID, manifest URL, and a timestamp. Receiving nodes verify the Library ID against their trust store before acting on the announcement.

This enables the key offline use case: two Raspberry Pi libraries in the same room (or connected by a Wi-Fi hotspot) automatically discover each other and can begin sharing ZIM files without any internet connectivity.

**Channel 4: ActivityPub follows.** A library with an ActivityPub actor can be followed by peers in the open-repo ActivityPub network. When the library publishes a new manifest via ActivityPub, all followers receive the update. This is the internet-connected discovery channel, building on Phase 4 infrastructure.

### 4.2 Ongoing Discovery: Manifest Polling

Once a peer is known and trusted, the local node polls the peer's manifest URL on a configurable schedule (default: every 24 hours). The polling is conditional (uses `If-None-Match` / `ETag` HTTP headers or a version timestamp comparison) to avoid downloading the manifest when nothing has changed.

For offline peers (LAN-only), the manifest is fetched from the peer's local IP when the local node is on the same network. If the peer is not currently reachable, the last-known manifest is retained and marked as potentially stale.

The polling schedule is intentionally slow (24 hours default) to be respectful of bandwidth. Libraries on satellite connections should set polling intervals of 7 days or longer.

### 4.3 Anti-Sybil and Spam Considerations

The trust model's explicit bilateral design limits Sybil attacks: a malicious actor cannot inject content into any library that has not manually added them as a trusted peer. The public registry is a directory, not a trust list. However, two secondary defenses are appropriate:

**Content hash verification**: Every downloaded ZIM file is verified against the CID in the manifest. A file that does not match its declared CID is rejected, logged, and the peer is automatically flagged for review. This prevents man-in-the-middle content injection even from trusted peers whose transfer infrastructure has been compromised.

**Domain scoping**: Peers can restrict which content domains they accept from a given trusted library. A medical library might accept only `medical` and `water` domain ZIMs from a peer, ignoring other domains even if the peer offers them. This limits the blast radius of a trusted peer publishing content outside their area of expertise.

---

## 5. Sharing Mechanisms

### 5.1 Direct Peer HTTP Transfer

The simplest and most reliable transfer mechanism: Library B fetches a ZIM from Library A's HTTPS or HTTP endpoint. For LAN transfers this requires no internet access. For internet transfers it requires both libraries to be online simultaneously.

Library A's open-repo node exposes:
```
GET /zim/{filename}                          # Full file download
GET /zim/{filename}?range={start}-{end}     # Range request for resume support
GET /manifest.json                           # Signed manifest
```

Range requests enable download resumption: a partially downloaded ZIM can be resumed from the last byte received without re-downloading already-transferred data.

**Bandwidth estimate**: A 50 MB domain ZIM at 1 Mbps (typical 3G) takes approximately 7 minutes. With range-request resumption, a connection that drops every 2 minutes still completes the download in 4 sessions of 2 minutes each with no retransmission waste.

### 5.2 BitTorrent Seeding

For distributing large ZIM files to many peers simultaneously, BitTorrent seeding is dramatically more bandwidth-efficient than direct HTTP: the more peers seed, the higher the effective bandwidth for each new peer downloading.

The open-repo export pipeline generates a `.torrent` file alongside every ZIM export. The `.torrent` file contains:
- The ZIM file's info-hash (SHA-256 in BitTorrent v2)
- A list of piece hashes for chunk-level verification
- The file size and name
- Tracker URLs and DHT bootstrap nodes (optional; the `.torrent` works without them)

Community libraries that choose to seed participate in the swarm. A library does not need to seed to benefit from seeding by others.

**Offline BitTorrent swarms**: BitTorrent works within a LAN without internet access. If Library A and Library B are on the same Wi-Fi network, and both have the same `.torrent` file, they can transfer the ZIM to Library C using local peer discovery (LSD — Local Service Discovery, the BitTorrent equivalent of mDNS) without any tracker or DHT involvement.

The `.torrent` file itself can be transferred via USB or email, acting as a self-describing package that enables community sharing even in fully offline environments.

### 5.3 IPFS Pinning

Libraries with internet access can pin their ZIM files to the IPFS network (via a pinning service like Pinata or Web3.Storage, or a self-hosted IPFS node). An IPFS-pinned ZIM is retrievable by its CID from any IPFS gateway without knowledge of the originating library's domain.

IPFS pinning provides:
- **Censorship resistance**: If the originating library's domain is blocked or seized, the content is still available via any IPFS gateway
- **Content deduplication**: If Library A and Library B both export the same ZIM content, they produce the same CID and IPFS automatically deduplicates storage
- **CAR file portability**: IPFS CAR (Content Addressable aRchive) files can be transferred via USB and imported into a local IPFS node, enabling fully offline IPFS-addressed distribution

IPFS pinning is an optional enhancement for libraries with internet access. It is not required for the core federation protocol.

### 5.4 Sneakernet / USB Transfer

For the lowest-connectivity environments — communities reachable only by courier, or libraries that share content via USB drives physically carried between locations — the protocol must support USB transfer as a first-class mechanism.

A **USB library bundle** is a directory containing:
```
library-bundle-2026-05/
├── manifest.json          # Signed manifest (same format as HTTP manifest)
├── manifest.json.sig      # Detached signature file
├── zim/
│   ├── open-repo_en_medical_2026-05.zim
│   ├── open-repo_en_water_2026-05.zim
│   └── open-repo_en_seed-preservation_2026-05.zim
└── README.txt             # Human-readable instructions for importing
```

The receiving library's open-repo node can import a USB bundle via a file picker UI or by placing the directory in a watched import folder. The import process:
1. Reads and verifies the manifest signature against the sender's Library ID (which must already be in the trust store)
2. Verifies the SHA-256 hash of each ZIM file against the manifest
3. Imports verified files into the local ZIM collection
4. Rejects any file whose hash does not match the manifest

This mechanism requires zero network connectivity and zero real-time coordination between the sender and receiver.

### 5.5 Kiwix Hotspot Sharing

The Kiwix Hotspot ecosystem already supports LAN sharing of ZIM files via kiwix-serve. A Raspberry Pi running kiwix-serve creates a Wi-Fi access point; devices on the network browse and download ZIM files via a standard HTTP server.

Phase 5.3 extends this with the manifest protocol: a kiwix-serve node that has adopted the open-repo federation extension publishes a signed manifest at the well-known URL. Other nodes on the hotspot can discover it via mDNS and fetch its manifest to learn which ZIM files are available and their CIDs.

This turns the existing Kiwix Hotspot deployment model (passive read-only serving) into an active peer in the federation (actively announcing and sharing its library catalog).

---

## 6. Trust, Verification, and Security

### 6.1 Content Verification Pipeline

Every ZIM file, regardless of which transfer mechanism delivered it, passes through the same verification pipeline before being added to the local collection:

```
Received file
     │
     ├─ Compute SHA-256 hash of received bytes
     │     └─ Compare against manifest CID/sha256
     │           ├─ Match → proceed
     │           └─ Mismatch → reject, log, flag peer
     │
     ├─ Verify manifest signature
     │     └─ Check signature against sender's Library ID (Ed25519 verify)
     │           ├─ Valid → proceed
     │           └─ Invalid → reject, alert operator
     │
     ├─ Run zimcheck validation
     │     └─ zimcheck exits 0
     │           ├─ Pass → add to collection
     │           └─ Fail → quarantine, alert operator
     │
     └─ Add to local ZIM collection
```

The three-stage pipeline (hash, signature, zimcheck) catches three different attack classes:
- **Hash mismatch**: file corrupted in transit, or man-in-the-middle substitution
- **Signature failure**: manifest forged by an attacker impersonating a trusted peer
- **zimcheck failure**: malformed ZIM that could crash readers or exploit parsing vulnerabilities

### 6.2 Privacy: Library Access Patterns

Community libraries may be in contexts where the information their patrons access is sensitive (medical information, reproductive health, political content). The federation protocol should not expose patron access patterns.

Design choices that protect access pattern privacy:
- **No analytics beaconing**: The manifest and ZIM files contain no embedded tracking pixels, analytics scripts, or call-home mechanisms. This is enforced by the Phase 5 ZIM rendering pipeline (no external JS or CSS).
- **Local-only access logs**: kiwix-serve and the open-repo node log article access locally. Logs are not federated. Aggregate statistics (total downloads, not per-article) can optionally be shared with peers if the library operator explicitly enables this.
- **No CDN leakage**: When Library A fetches a ZIM from Library B via HTTP, Library B's server logs know that Library A's IP fetched the file. Library B does not know which patron at Library A later read which article. This is the same privacy model as any library lending a book to another library.
- **mDNS is LAN-scoped**: Local network discovery does not expose library presence to the internet. A library's mDNS advertisement is only visible to devices on the same network segment.

### 6.3 Malware and Content Pollution Prevention

The primary attack vector is a compromised or malicious library publishing ZIM files with harmful content (malware embedded in HTML, disinformation replacing verified medical protocols, propaganda replacing seed guides).

Defenses in priority order:

1. **Trust gates**: Only explicitly trusted peers can contribute content to a library's collection. The trust model's bilateral, non-transitive design means compromising one trusted peer does not automatically compromise the whole network.
2. **Domain authority**: Domain experts maintain canonical versions. A medical library network establishes which libraries are authoritative for medical content. Content from non-authoritative sources for a given domain is marked as unreviewed even if it passes hash verification.
3. **zimcheck validation**: Malformed ZIM files (including files with embedded JavaScript or external resource links, which Phase 5 strips during export) fail zimcheck and are rejected.
4. **Version pinning**: Libraries can pin specific versions of a ZIM (by CID) rather than always accepting the latest. This provides a stability window: the library reviews new versions before adopting them.
5. **Community blocklists**: The public registry can maintain a blocklist of Library IDs that have been confirmed as malicious by the community. Individual libraries choose whether to subscribe to the blocklist.

---

## 7. Design Trade-offs

| Trade-off | Choice Made | Alternative Rejected | Reason |
|---|---|---|---|
| **Central directory vs. fully decentralized** | Voluntary public registry (not in trust path) | Fully decentralized DHT | DHT requires internet; registry provides UX without becoming a dependency |
| **Transitive trust vs. bilateral trust** | Bilateral (explicit peer lists) | Web of Trust (transitive) | Transitive trust amplifies compromise of one node across the network |
| **Certificate authority vs. self-signed keys** | Self-signed Ed25519 (Library IDs) | CA-signed TLS certificates | CA dependency introduces centralized control; self-signed keys work offline |
| **Atomic ZIM files vs. IPFS block decomposition** | Atomic ZIM files | IPFS block-level decomposition | IPFS daemon is too heavyweight for Raspberry Pi; atomic files are simpler for non-technical operators |
| **Automatic content adoption vs. manual review** | Configurable (`auto_sync: true/false` per peer) | Always manual | Communities with reliable trusted peers benefit from automation; sensitive content domains prefer manual review |
| **Public manifest vs. private library** | Both supported | Mandatory public | Some libraries operate in sensitive political contexts and cannot be publicly listed |
| **Open sockets for seeding vs. opt-in seeding** | Opt-in seeding | Default seeding | Many deployments are on NAT'd networks or have no open ports |

---

## 8. Implementation Strategy

### 8.1 What Already Exists

- **HTTP Signature keypairs** (Phase 4): The Ed25519 keypairs generated for ActivityPub federation can double as Library ID keypairs. No new key generation infrastructure is needed.
- **ZIM export pipeline** (Phase 5.1): Already generates ZIM files with SHA-256 checksums. Adding CID computation (SHA-256 with the multihash prefix) and `.torrent` file generation is a small addition.
- **kiwix-serve** (Phase 5.1): Already serves ZIM files over HTTP. Adding the manifest endpoint is a configuration addition.
- **ActivityPub federation** (Phase 4): Already propagates announcements to federated peers. ZIM manifest announcements can use the same ActivityPub `Announce` activity type.

### 8.2 What Is New in Phase 5.3

| Component | New Work | Estimated Effort |
|---|---|---|
| Manifest format spec and schema | New | 2–4 hours |
| Manifest generation in export pipeline | New | 4–6 hours |
| Manifest signing (Ed25519) | New (uses existing keypairs) | 2–3 hours |
| Manifest verification on import | New | 4–6 hours |
| mDNS local discovery (avahi-browse or zeroconf) | New | 6–10 hours |
| USB bundle import/export UI | New | 8–12 hours |
| `.torrent` file generation in export pipeline | New | 4–6 hours |
| IPFS CID computation in export pipeline | New (additive) | 2–3 hours |
| Content verification pipeline (hash + sig + zimcheck) | New | 4–6 hours |
| Peer trust store (database table + UI) | New | 6–8 hours |
| Public registry crawler/sync | New (optional) | 4–8 hours |

**Total estimated effort**: 46–72 hours (not counting UI polish)

### 8.3 Phasing Recommendation

Phase 5.3 can be developed incrementally without blocking Phase 5.2:

**5.3a (foundational)**: Manifest generation + signing in the export pipeline. No peer interaction yet — just adds a manifest file alongside every ZIM export. Feeds into Phase 5.2's OPDS catalog as a parallel discovery channel.

**5.3b (verification)**: Content verification pipeline on import. Any ZIM file imported into the collection is verified against a manifest if one is provided. Enables safe USB bundle import.

**5.3c (peer networking)**: mDNS discovery + HTTP peer fetch + trust store. Enables LAN-to-LAN sharing without internet.

**5.3d (internet federation)**: ActivityPub manifest announcements + BitTorrent seeding + IPFS pinning. Enables global sharing via existing open-repo ActivityPub network.

---

## 9. Phase Transition Map: 5.2 → 5.3 → Phase 6

This section makes explicit which capabilities unlock at each phase boundary and what Phase 5.2 completion triggers in Phase 5.3.

### 9.1 What Phase 5.2 Must Deliver for 5.3 to Proceed

Phase 5.2 (Medical/Water/Seed domain ZIM content) must deliver the following artifacts before 5.3 implementation begins:

| Phase 5.2 Output | Why 5.3 Needs It |
|---|---|
| 5 domain ZIM files with stable naming (`open-repo_en_{domain}_{YYYY-MM}.zim`) | Manifest schema depends on stable ZIM naming conventions |
| SHA-256 checksums for each ZIM export | The manifest's `sha256` field is populated directly from these |
| Domain scope definitions (which articles belong to which domain) | Delta manifest `domain` field and domain-scoped peer acceptance lists |
| OPDS catalog entries for each domain ZIM | Phase 5.3a extends the OPDS entry format with `delta-available` and version fields |
| Phase 4 Ed25519 keypairs in production | Manifest signing (5.3a) uses these keypairs |

Phase 5.3a can begin immediately upon Phase 5.2 delivering its first full ZIM export — it does not need all 5 domains, just at least one complete domain.

### 9.2 What Phase 5.3 Delivers as Inputs to Phase 6

Phase 6 (`ITEM15_PHASE6_FEDERATION_ROADMAP.md`) is the multi-organization ActivityPub federation. Phase 5.3 provides its prerequisites:

| Phase 5.3 Output | Phase 6 Dependency |
|---|---|
| Signed manifest format (5.3a) | Phase 6 can extend the manifest with organizational metadata and GDPR residency tags |
| Library ID infrastructure (Ed25519 peer identity) | Phase 6's DID:WEB identity resolution builds on top of this |
| mDNS / UDP peer discovery (5.3c) | Phase 6's instance discovery (analogous to `instances.social`) reuses the same transport primitives |
| Trust store (peer list database, 5.3c) | Phase 6 extends this with organizational identity, not just library identity |
| ActivityPub manifest announcements (5.3d) | Phase 6 federation directly extends these to multi-organization content propagation |

The implementation can be understood as: **Phase 5.3 is the file-layer federation; Phase 6 is the social-layer federation.** Both share the same identity and trust substrate.

### 9.3 What Remains Out of Scope Until Phase 6

The following capabilities are deliberately deferred and must not be designed into Phase 5.3:

- **Transitive trust / web of trust**: Phase 5.3 is bilateral only. Vouchsafe delegation is Phase 6+.
- **Cross-library content ownership and attribution arbitration**: Phase 5.3 treats ZIM files as atomic. Content-level ownership disputes are Phase 6 governance problems.
- **Real-time collaborative editing**: Phase 5.3 has asynchronous change proposals. Real-time CRDT sync is Phase 6+.
- **Anonymization / Tor transport**: The high-risk deployment case (libraries in politically adversarial contexts needing transport-layer anonymity) is Phase 6+.
- **Content licensing cross-checks across the federation**: Phase 5.3 validates license fields locally. Cross-federation license policy enforcement is Phase 6.

## 10. Cross-References to Existing Docs

- ZIM export pipeline: `PHASE_5_ARCHITECTURE.md` section 2
- Phase 4 HTTP Signature keypairs: `PHASE_4_DESIGN.md`
- Phase 6 ActivityPub federation (multi-organization): `ITEM15_PHASE6_FEDERATION_ROADMAP.md`
- Versioning strategy for collaborative ZIM updates: `VERSIONING_STRATEGY.md` (this release)
- Differential sync protocol for low-bandwidth updates: `DIFFERENTIAL_SYNC_PROTOCOL.md` (this release)
- Phase 5.2 domain-specific ZIM content: `PHASE_5.2_IMPLEMENTATION_ROADMAP.md`

---

## Sources

- [IPFS — Content Addressed, Versioned, P2P File System (Benet, 2014)](https://arxiv.org/abs/1407.3561)
- [Design and Evaluation of IPFS (Trautwein et al., 2022)](https://arxiv.org/pdf/2208.05877)
- [Content Identifiers (CIDs) — IPFS Docs](https://docs.ipfs.tech/concepts/content-addressing/)
- [Content Addressing: 2025 In Review — IPFS Foundation](https://ipfsfoundation.org/content-addressing-2025-in-review/)
- [Ed25519 Support in Chrome 137 — IPFS Blog](https://blog.ipfs.tech/2025-08-ed25519/)
- [Syncthing Block Exchange Protocol v1](https://docs.syncthing.net/specs/bep-v1.html)
- [Syncthing Local Discovery Protocol v4](https://docs.syncthing.net/specs/localdisco-v4.html)
- [BitTorrent v2 — libtorrent blog](https://blog.libtorrent.org/2020/09/bittorrent-v2/)
- [libp2p pubsub Peer Discovery with Kademlia DHT](https://medium.com/rahasak/libp2p-pubsub-peer-discovery-with-kademlia-dht-c8b131550ac7)
- [Kiwix Hotspot — Offline Knowledge Distribution](https://kiwix.org/en/kiwix-hotspot/)
- [Kiwix/ZIM Incremental Updates — MediaWiki](https://www.mediawiki.org/wiki/Kiwix/ZIM_incremental_updates)
- [Data Integrity EdDSA Cryptosuites v1.0 — W3C](https://www.w3.org/TR/vc-di-eddsa/)
- [ActivityPub W3C Specification](https://www.w3.org/TR/activitypub/)
- [Content Censorship in IPFS (2023)](https://arxiv.org/pdf/2307.12212)
- [Peer2PIR: Private Queries for IPFS](https://arxiv.org/pdf/2405.17307)
- [Scuttlebutt Protocol Guide — SSBC](https://ssbc.github.io/scuttlebutt-protocol-guide/)
- [Secure Scuttlebutt: An Identity-Centric Protocol — ACM](https://dl.acm.org/doi/10.1145/3357150.3357396)
- [Briar — How It Works (Bramble Protocol)](https://briarproject.org/how-it-works/)
- [Vouchsafe: A Zero-Infrastructure Capability Graph Model for Offline Identity and Trust (Kuri, 2026)](https://arxiv.org/pdf/2601.02254)
- [Phase 5 Architecture — open-repo project](./PHASE_5_ARCHITECTURE.md)
- [Phase 6 Federation Roadmap — open-repo project](./ITEM15_PHASE6_FEDERATION_ROADMAP.md)
