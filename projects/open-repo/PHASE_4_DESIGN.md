# Open-Repo Phase 4: Federation Architecture

**Status**: Design Document (Pre-implementation)  
**Version**: 1.0  
**Date**: 2026-04-26  
**Target**: ~400–500 story points (3–4 months, 2–3 FTE)  
**Dependencies**: Phase 1–3 complete (commit 7351680, 81/81 tests passing)

---

## Executive Summary

Phase 4 **proves the distributed architecture** by deploying a second independent node that federates with the first. This phase implements:

1. **ActivityPub protocol** support (inbox/outbox, activity streams)
2. **Multi-node federation** (content sync, endorsement propagation)
3. **Node discovery & identity** (WebFinger, DID:WEB)
4. **Distributed conflict resolution** (versioning, merge logic)
5. **Cross-node search** (federated index updates)

By the end of Phase 4, two independent nodes will synchronize content and endorsements in real-time, proving that the open-repo architecture can scale beyond a single instance.

---

## What Success Looks Like

| Milestone | Success Criteria |
|-----------|------------------|
| **ActivityPub Endpoints** | Seed Node implements `/inbox`, `/outbox`, `/followers`, `/following` per W3C spec. All activities are cryptographically signed. |
| **Multi-Node Deploy** | Second test node (Node B) operational in separate region/environment with independent PostgreSQL + Meilisearch. |
| **Content Sync** | New item created on Node A appears in Node B's search index within 60 seconds (via ActivityPub `Create` activity). |
| **Endorsement Propagation** | Upvotes on Node A increment the endorsement count on Node B (and vice versa). Vote totals converge across nodes. |
| **Federation Discovery** | Both nodes advertise each other via `.well-known/webfinger` + node registry. Manual federation handshake succeeds. |
| **Contribution Workflow** | A user submits a contribution on Node B; it appears in Node A's review queue. Cross-node moderation works end-to-end. |
| **Conflict Resolution** | Same item edited on both nodes simultaneously; system applies conflict resolution (versioning + last-write-wins or consensus). |
| **Test Coverage** | 60+ new tests covering ActivityPub, federation mechanics, conflict resolution, cross-node workflows. Overall test suite ≥95% passing. |

---

## Architecture: ActivityPub + Multi-Node Sync

### 1. ActivityPub Protocol Implementation

**Goal**: Implement W3C ActivityPub specification for content distribution.

#### 1.1 Core Endpoints

Each node exposes the following ActivityPub endpoints:

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/.well-known/webfinger` | GET | Node identity (RFC 7033). Returns actor URL for the domain. |
| `/actor` | GET | Actor object (node identity). Returns name, publicKey, inbox, outbox, followers, following. |
| `/inbox` | POST | Receive activities from other nodes (Create, Update, Delete, Announce, Undo). |
| `/outbox` | GET | Ordered collection of activities this node has generated. Supports pagination. |
| `/followers` | GET | List of nodes following this instance. |
| `/following` | GET | List of nodes this instance is following (federation partners). |
| `/api/contributions/{id}/activity` | GET | JSON-LD representation of a contribution as an Activity. |

#### 1.2 Activity Types

Implement the following activity types:

1. **Create** — New item or contribution submitted. Payload includes the full JSON-LD content object.
2. **Update** — Item or contribution edited. Payload includes delta + new version number.
3. **Delete** — Item withdrawn or contribution rejected. Payload includes tombstone.
4. **Announce** — Endorsement (upvote/downvote). Payload includes vote count + endorsement URI.
5. **Undo** — Retract an endorsement or activity. Used for vote removal or activity corrections.

#### 1.3 Cryptographic Signing

All outgoing activities are signed using **HTTP Signatures (RFC 8017 + W3C extension)**:

- **Algorithm**: RSA-SHA256 (PKCS#1 v1.5) or Ed25519 (for newer implementations)
- **Key generation**: Each node generates a 2048-bit RSA keypair at bootstrap. Public key embedded in actor object.
- **Signature headers**: `Signature: keyId="...",algorithm="rsa-sha256",headers="(request-target) host date",signature="..."`.
- **Verification**: All incoming activities are verified against the sender's public key before processing.

---

### 2. Multi-Node Federation Mechanics

#### 2.1 Federation Bootstrap

**Goal**: Establish trust relationship between two nodes.

**Sequence**:

1. **Node A Admin → Node B Admin**: Exchange node identifiers (URLs).
2. **Node A**: Fetches Node B's actor object (`GET /actor`).
3. **Node A**: Stores Node B's public key and inbox URL in a `federation_partners` table.
4. **Node A**: Sends a `Follow` activity to Node B's inbox.
5. **Node B**: Receives `Follow` activity; verifies signature.
6. **Node B**: Stores Node A's public key and fetches Node A's actor object.
7. **Node B**: Sends an `Accept` activity back to Node A.
8. **Both nodes**: Add each other to their `following` list. Federation is now bidirectional.

**Data Schema**:

```sql
CREATE TABLE federation_partners (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    partner_url VARCHAR(512) NOT NULL UNIQUE,  -- https://node-b.example.com
    actor_url VARCHAR(512) NOT NULL,  -- https://node-b.example.com/actor
    public_key_pem TEXT NOT NULL,  -- PEM-encoded public key
    inbox_url VARCHAR(512) NOT NULL,  -- https://node-b.example.com/inbox
    outbox_url VARCHAR(512) NOT NULL,
    followers_url VARCHAR(512),
    following_url VARCHAR(512),
    federation_state VARCHAR(20),  -- 'pending' | 'active' | 'suspended'
    first_contact DATETIME,
    last_verified DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

#### 2.2 Content Propagation: Create + Update

When a new item is created on Node A:

1. Node A stores the item locally (existing Phase 1–3 flow).
2. Node A generates a `Create` activity with the full JSON-LD object.
3. Node A sends the `Create` activity to all federation partners' inboxes.
4. **Node B receives** the activity:
   - Verifies the signature.
   - Checks if an item with this CID already exists locally (idempotent).
   - If new: creates a local stub (or full copy, depending on sync strategy).
   - Updates Meilisearch index for federation search.
   - Returns HTTP 202 Accepted.

**For edits** (Update activity):

1. Node A edits an item locally and increments the version number.
2. Node A generates an `Update` activity with the edit diff + new version.
3. Node B receives and applies the update if the version is newer than its local copy.
4. **Conflict resolution** (if both nodes edited independently): see section 2.4.

#### 2.3 Endorsement Propagation: Announce + Undo

When a user upvotes an item on Node A:

1. Node A increments the local endorsement count.
2. Node A generates an `Announce` activity with the vote URI and updated count.
3. Node A sends `Announce` to federation partners.
4. **Node B receives** the `Announce`:
   - Extracts the endorsement count.
   - Updates its local copy of the item with the aggregated vote total.
   - Returns 202 Accepted.

**Endorsement aggregation logic**:

- Each node tracks endorsements separately (e.g., Node A has 10 upvotes, Node B has 7 upvotes).
- A query for total endorsements aggregates across known federation partners.
- Endorsement counts are **eventually consistent** (may lag by a few seconds to minutes).

#### 2.4 Conflict Resolution: Versioning + Last-Write-Wins

When the same item is edited on two nodes independently, a conflict arises. Use this strategy:

**Version-based resolution**:

1. Each content item has a `version` field (integer, starts at 1).
2. On each edit, the version increments.
3. When receiving an `Update` activity:
   - If incoming version > local version: apply the update.
   - If incoming version ≤ local version: **ignore** (local version is newer or equal).
   - If incoming version = local version AND edit differs from local: **flag as conflict** (store both versions, notify admins).

**Conflict logging**:

```sql
CREATE TABLE content_conflicts (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    content_cid VARCHAR(255) NOT NULL,
    version INT,
    local_content JSONLD,
    remote_content JSONLD,
    remote_node_url VARCHAR(512),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    resolved BOOLEAN DEFAULT FALSE,
    resolution_note TEXT
);
```

Admins are notified of conflicts; they manually choose which version to keep (or manually merge).

---

### 3. Node Discovery & Identity

#### 3.1 WebFinger (.well-known/webfinger)

Implements RFC 7033 for node identity discovery:

```bash
curl https://node-a.example.com/.well-known/webfinger?resource=acct:node@node-a.example.com

{
  "subject": "acct:node@node-a.example.com",
  "links": [
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://node-a.example.com/actor"
    }
  ]
}
```

#### 3.2 DID:WEB Integration (Optional for Phase 4, Full for Phase 5)

**DID:WEB** allows portable identity across nodes:

```
did:web:node-a.example.com
```

Resolves to:

```
https://node-a.example.com/.well-known/did.json

{
  "@context": "https://w3id.org/did/v1",
  "id": "did:web:node-a.example.com",
  "publicKey": [{
    "id": "did:web:node-a.example.com#key-1",
    "type": "RsaVerificationKey2018",
    "publicKeyPem": "-----BEGIN PUBLIC KEY-----\n..."
  }]
}
```

For Phase 4, this is **optional but recommended**. Allows third-party nodes to verify Node A's identity without a centralized registry.

#### 3.3 Federation Registry (Optional)

A simple optional registry helps nodes discover each other:

```
https://open-repo-registry.example.com/nodes

{
  "nodes": [
    {
      "url": "https://node-a.example.com",
      "did": "did:web:node-a.example.com",
      "description": "Agricultural knowledge base (English + Spanish)",
      "joined": "2026-05-15",
      "item_count": 245,
      "languages": ["en", "es"]
    },
    {
      "url": "https://node-b.example.com",
      "did": "did:web:node-b.example.com",
      "description": "Electronics and repair guides",
      "joined": "2026-06-01",
      "item_count": 187,
      "languages": ["en"]
    }
  ]
}
```

Nodes can **opt-in** to register themselves. The registry is purely informational; it does not control federation.

---

## Implementation Roadmap (Waves)

### Wave 1: ActivityPub Protocol (Weeks 1–2)

**Scope**: Core ActivityPub endpoints + HTTP signature verification.

**Deliverables**:
- [ ] `/.well-known/webfinger` endpoint (node identity)
- [ ] `/actor` endpoint (actor object with publicKey)
- [ ] `/inbox` endpoint (receives activities; basic validation)
- [ ] `/outbox` endpoint (lists activities; ordered collection)
- [ ] HTTP signature generation (RSA-SHA256)
- [ ] HTTP signature verification (validate incoming activities)
- [ ] Activity models (Create, Update, Delete, Announce, Undo)
- [ ] 20+ unit tests (endpoint responses, signature validation, idempotency)

**Tech stack**:
- `cryptography` library for RSA key generation + signing
- `httpx` for outbound activity delivery with signed requests
- FastAPI routes for ActivityPub endpoints
- SQLAlchemy for activity logging

---

### Wave 2: Federation Bootstrap & Content Sync (Weeks 2–3)

**Scope**: Multi-node federation, content propagation.

**Deliverables**:
- [ ] `federation_partners` table (store partner nodes + public keys)
- [ ] Federation bootstrap workflow (Follow/Accept handshake)
- [ ] `Create` activity generation when new items are added
- [ ] `Create` activity ingestion (Node B receives Node A's items)
- [ ] `Update` activity generation + ingestion (edits sync)
- [ ] Federated search index updates (Meilisearch sync)
- [ ] Idempotency checks (same activity received twice doesn't duplicate)
- [ ] 15+ integration tests (cross-node content flow, endpoint interactions)

**Data flow**:
```
Node A: User submits item
  → Item stored locally + version=1
  → Create activity generated
  → Sent to Node B's inbox
  ↓
Node B: Receives Create activity
  → Verifies signature
  → Stores item (or fetches via CID from IPFS)
  → Indexes in Meilisearch
  → Returns 202 Accepted
```

---

### Wave 3: Endorsement Propagation (Week 3)

**Scope**: Vote sync across nodes.

**Deliverables**:
- [ ] `Announce` activity generation (when item is upvoted)
- [ ] `Announce` activity ingestion (receive votes from federation partners)
- [ ] Endorsement aggregation logic (sum votes across nodes for query results)
- [ ] `Undo` activity (retract votes)
- [ ] Eventually-consistent vote counts (may lag by seconds)
- [ ] 10+ tests (vote propagation, aggregation, undo)

**Example**:
```
Node A: User upvotes item (vote count: 10)
  → Announce activity sent to Node B
  ↓
Node B: Receives Announce
  → Updates item with new vote total from Node A
  → Local votes (7) + remote votes (10) = reported total in queries
```

---

### Wave 4: Conflict Resolution & Versioning (Week 4)

**Scope**: Handle concurrent edits across nodes.

**Deliverables**:
- [ ] Version field on all content items (starts at 1, increments on edit)
- [ ] Version-based conflict detection (same version, different content)
- [ ] `content_conflicts` table (log unresolved conflicts for admin review)
- [ ] Admin dashboard to view and resolve conflicts (choose which version wins)
- [ ] Last-write-wins policy (incoming version > local = apply)
- [ ] 10+ tests (conflict scenarios, versioning, admin resolution)

---

### Wave 5: Deployment & Testing (Weeks 4–5)

**Scope**: Deploy a second node; validate end-to-end federation.

**Deliverables**:
- [ ] Node B infrastructure (PostgreSQL, Meilisearch, FastAPI instance, separate domain)
- [ ] DNS/SSL setup for Node B
- [ ] Federation bootstrap between Node A (prod) and Node B (test)
- [ ] End-to-end test scenarios:
  - [ ] Create item on Node A → verify appears on Node B's search
  - [ ] Create item on Node B → verify appears on Node A
  - [ ] Upvote on Node A → verify propagates to Node B
  - [ ] Edit on Node A, different edit on Node B simultaneously → conflict resolved
  - [ ] Contribution submitted on Node B → appears in Node A's review queue
- [ ] Performance benchmarks (latency of activity delivery, search index sync time)
- [ ] Documentation for third-party node operators (federation setup guide)
- [ ] 15+ end-to-end tests

---

## Technical Stack Recommendations

| Component | Choice | Rationale |
|-----------|--------|-----------|
| ActivityPub Library | Custom (FastAPI routes) | Existing Python libraries are immature; simpler to implement 5 required endpoints directly. |
| HTTP Signatures | `cryptography` + custom middleware | Use proven `cryptography` library; implement RFC 8017 verification in FastAPI middleware. |
| Async Delivery | `httpx` + task queue (Celery or RQ) | Outbound activity delivery must be async; task queue ensures retry on transient failures. |
| Activity Logging | PostgreSQL `activities` table | Log all sent/received activities for debugging + audit trail. |
| Conflict Resolution | In-app logic (no external tool) | Simple versioning + flag for admin review is sufficient for MVP. |
| DID:WEB | Optional; implement in Phase 5 if needed | For Phase 4, DNS-based node discovery + registry is sufficient. |

---

## Testing Strategy

### Unit Tests (30 tests)
- ActivityPub endpoint responses
- HTTP signature generation + verification
- Activity model validation
- Version comparison logic
- Conflict detection

### Integration Tests (20 tests)
- Federation bootstrap workflow
- Cross-node content propagation
- Endorsement sync
- Edit sync + conflict resolution

### End-to-End Tests (15+ tests)
- Two nodes federating in Docker containers
- Create item on Node A → search on Node B
- Vote propagation across nodes
- Contribution workflow across nodes

### Performance Tests (5 tests)
- Activity delivery latency (target: <5s)
- Search index sync time (target: <60s)
- Endorsement aggregation query time (target: <200ms)

---

## Success Criteria (End of Phase 4)

- [ ] ActivityPub endpoints fully implemented + signed
- [ ] Two independent nodes deployed and federating
- [ ] Content created on Node A appears on Node B's search (and vice versa)
- [ ] Endorsements propagate and aggregate correctly
- [ ] Conflicts detected and logged (admin can resolve)
- [ ] Contribution workflow works cross-node
- [ ] ≥95% test coverage (80+ new tests)
- [ ] Documentation for federation setup and API
- [ ] Performance metrics meet targets (delivery <5s, search <60s)

---

## Known Risks & Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| ActivityPub spec complexity | Implementation delays | Start with 5 core activities; skip extensions in Phase 4. Reference implementations (Mastodon, PeerTube) for guidance. |
| HTTP signature verification bugs | Security vulnerability | Use battle-tested `cryptography` library; extensive tests for edge cases. |
| Activity delivery failures (network) | Lost content updates | Implement task queue with exponential backoff (3 retries over 24 hours). |
| Conflict explosion (many simultaneous edits) | Unresolvable state | Versioning + admin review is sufficient for MVP. Implement consensus algorithms in Phase 4.5 if needed. |
| Spam/malicious nodes | Data pollution | Federation is manual (admin-approved handshake). No open federation in Phase 4. |

---

## Out of Scope (Phase 4)

- **Kiwix/offline export** (Phase 5)
- **Governance & protocol steering** (Phase 5+)
- **Open federation** (any node can join) — manual handshake only
- **Blockchain-based consensus** — simple versioning + admin review
- **Advanced DID integration** (use DID:WEB only if simple)
- **GraphQL federation** (REST-only for Phase 4)
- **Full Fediverse compatibility** (Mastodon timeline integration) — can be added in Phase 4.5

---

## Timeline & Capacity

- **Duration**: 3–4 months (12–16 weeks)
- **Team size**: 2–3 FTE (1 backend lead + 1 DevOps + 1 QA)
- **Estimated effort**: 400–500 story points (40–50 points/week = 8–13 weeks)
- **Target start**: Week of 2026-05-27 (after Phase 3 validation period)
- **Target completion**: Week of 2026-08-26 (federation MVP complete)

---

## Appendix: References

- [W3C ActivityPub Spec](https://www.w3.org/TR/activitypub/)
- [HTTP Signatures (RFC 8017 + W3C ext)](https://tools.ietf.org/html/draft-cavage-http-signatures)
- [WebFinger (RFC 7033)](https://tools.ietf.org/html/rfc7033)
- [DID:WEB Method](https://w3c-ccg.github.io/did-method-web/)
- [Mastodon ActivityPub Implementation](https://github.com/mastodon/mastodon)
- [Open-Repo Architecture Notes](./architecture-notes.md)
- [Open-Repo MVP Protocol Design](./mvp-protocol-design.md)
