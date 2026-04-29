---
title: "Phase 6: Multi-Organization Federation Roadmap"
project: open-repo
phase: 6
status: design-proposal
date: 2026-04-29
author: research-agent
confidence: high
tags: [federation, activitypub, matrix, multi-tenant, gdpr, governance, economics]
---

# Phase 6: Multi-Organization Federation Roadmap

**Status**: Design Proposal (pre-Phase 5 merge)
**Audience**: Core team, prospective federation partners, governance contributors
**Scope**: Scaling open-repo from a single organization instance to a federated network of independent operators
**Word count**: ~4,800 words

---

## Executive Summary

Phase 5 proved that open-repo can run as a single-organization platform with CQRS-backed federation service architecture. Phase 6 is the step that makes the network effect real: it allows any independent research organization, transparency initiative, or citizen group to operate their own open-repo instance and participate in a shared discovery and endorsement graph — without surrendering data sovereignty or operational autonomy.

The reference model is not a centralized SaaS multi-tenant system. It is closer to email or Matrix: a protocol-first, operator-independent network in which each participant controls their own node. A researcher at Organization A can discover, cite, and endorse a dataset published by Organization B's node, and that endorsement propagates across the network. Both organizations keep their private data private, comply with their own jurisdictional requirements, and can leave the network without loss of their own records.

The single hardest problem in Phase 6 is not the protocol — ActivityPub provides a working template, and Phase 4 already implements the core of it. The hard problems are compliance heterogeneity (GDPR-resident nodes cannot simply push data to US-resident nodes), economic sustainability at the coordination layer, and the governance of a specification that no single party controls.

The recommended sequencing puts conflict resolution and data-boundary enforcement first, economic primitives second, and governance formalization third. This order ensures that the network is trustworthy before it is monetizable.

---

## 1. Multi-Tenant Federation Architecture

### 1.1 Topology: Peer Nodes, Not a Hub

The foundational architectural decision is whether the federation is hub-and-spoke or peer-to-peer mesh. Hub-and-spoke (one canonical coordination server, many leaf nodes) is operationally simpler but introduces a single point of failure, a single target for legal attack, and a permanent dependency on whoever runs the hub. The email and Matrix models both prove that peer-to-peer mesh federations are operationally viable at scale: as of early 2025, the Matrix federation comprised over 10,000 discoverable homeservers.

Open-repo Phase 6 should adopt the **peer mesh** model. Each organization runs an independent instance with its own PostgreSQL, Meilisearch, and federation service. There is no required central node. Discovery is bootstrapped through a voluntary public registry (analogous to `instances.social` for Mastodon), but the registry is not in the trust path — two organizations can federate directly without it.

```
           [Org A Node]
          /      |      \
  [Org B Node]  [Org C Node]  [Org D Node]
       |              |
  [Org E Node]   [Org F Node]

  Each edge = bilateral ActivityPub federation pair.
  No central coordinator required after bootstrapping.
```

### 1.2 Researcher Identity Across Nodes

When a researcher has accounts on two federated nodes (Org A and Org B), the current Phase 4 architecture treats them as separate actors because ActivityPub actors are scoped to a domain. Phase 6 needs an identity bridge.

The recommended approach is **DID:WEB** — W3C Decentralized Identifiers anchored to an HTTPS domain. A researcher can claim `did:web:researcher.example.com` as their portable identifier and present Verifiable Credentials proving affiliation with Org A or Org B. Both nodes store the DID as a canonical identifier alongside the local account. Cross-node endorsement queries can then aggregate by DID rather than by account.

This is analogous to how Matrix handles cross-server identity: a user `@alice:orgA.example.com` is a local actor, but their MXC avatar and display name are resolvable globally, and a room shared between orgA and orgB maintains a single consistent view of Alice's contributions.

Implementation note: DID:WEB requires no blockchain. A researcher with a personal domain publishes their DID document at `https://researcher.example.com/.well-known/did.json`. Each federated node caches and periodically reverifies this document.

### 1.3 Content Propagation and Sync Strategy

Phase 4 established the basic ActivityPub Create/Update/Delete/Announce pattern. Phase 6 must extend this to handle three scenarios that become common in multi-organization contexts:

**Scenario A: Mirror vs. Reference.** When Org B receives a `Create` activity for a dataset published by Org A, it has a choice: store a full local copy (mirror), or store a stub that points back to Org A's canonical URL (reference). Mirroring improves resilience and search performance but increases storage costs and complicates ownership semantics. Referencing keeps provenance clean but creates availability dependencies.

Recommended policy: store references by default; mirror on explicit opt-in by the receiving organization's admin. The federation protocol should carry a `x-open-repo-allow-mirror: true/false` flag in the actor's profile so senders can declare their preference.

**Scenario B: Same dataset, two publishing nodes.** Research datasets often exist in multiple places — a university may publish the same underlying data as a government transparency node. These are not the same ActivityPub object (different authors, different URIs), but they describe the same real-world artifact. Phase 6 should implement a lightweight **content deduplication hint** using the dataset's hash (already computed as a CID in Phase 1-3). When a node receives a `Create` and detects a CID collision with an existing object from another node, it creates a `sameAs` relationship rather than a conflict. Neither record is deleted; both are surfaced in search, linked by the equivalence relation.

**Scenario C: Concurrent edits (genuine conflict).** If Org A and Org B both independently edit a mutually-owned dataset within the same clock window, Phase 4's version-based last-write-wins strategy produces a deterministic winner but silently discards the other edit. Phase 6 should log these conflicts explicitly, notify both organizations' admins, and present a three-way merge interface in the admin UI (local version, remote version, common ancestor). This is the approach used by Matrix's State Resolution Algorithm — servers independently execute the same consensus algorithm, converging to identical state without coordination.

### 1.4 What Stays Private vs. What Federates

Not everything should propagate across the network. The following taxonomy should be enforced at the federation service boundary:

| Data Category | Default Behavior | Rationale |
|---|---|---|
| Published research datasets | Federate (Create/Update/Delete) | Core value proposition |
| Endorsements and citations | Federate (Announce/Undo) | Enables cross-network reputation |
| User profiles (public) | Federate via WebFinger | Enables cross-node attribution |
| User profiles (private fields) | Never federate | PII minimization |
| Internal moderation notes | Never federate | Organizational confidentiality |
| Draft/unpublished content | Never federate | Author control |
| Access-controlled datasets | Federate metadata only | Lets others discover, not read |
| Audit logs | Never federate raw; aggregate stats only | Compliance and privacy |

This taxonomy should be encoded as a per-object `federationPolicy` field in the JSON-LD schema, not enforced only at the transport layer, so that receiving nodes can verify the sending node's intent and flag unexpected policy deviations.

---

## 2. Compliance and Auditability

### 2.1 Data Residency: The Central Compliance Challenge

The most structurally difficult aspect of Phase 6 is that federated nodes will operate under different legal regimes. As of 2026, 62 jurisdictions have some form of data localization requirement, up from 35 in 2017. The EU-US Data Privacy Framework survived its first legal challenge in September 2025 but remains contested. TikTok was fined €530 million in 2025 for allowing EEA user data to be accessed from China. For a research transparency network, the stakes are lower — but the structure of the problem is identical: EU-resident user data that federates to a US-resident node may constitute a cross-border transfer requiring a legal basis.

The Phase 6 response to this is **data residency tagging at the object level**. Every federated activity should carry the originating node's ISO 3166-1 country code and a declared residency policy. Receiving nodes should enforce an `inboundResidencyPolicy` configuration that specifies which origin jurisdictions they accept. An EU node can be configured to reject activities from nodes that lack an adequacy decision or SCCs, before processing the payload.

This is not a complete compliance solution — it does not replace the need for each organization to perform its own Transfer Impact Assessment — but it ensures the protocol does not make compliance impossible. The alternative (federation that is blind to jurisdiction) would make EU participation legally untenable.

### 2.2 Encryption Key Architecture

The recommended architecture is **per-organization key management with optional federation-layer escrow**.

Each node generates its own RSA-4096 or Ed25519 keypair at bootstrap (Phase 4 already does this for HTTP Signatures). For data-at-rest encryption, each organization manages its own AES-256 key, optionally via a cloud KMS (AWS KMS, Azure Key Vault, GCP Cloud KMS). Data encrypted with Org A's key is never decipherable by Org B's node, even if both are federation partners.

Federation-layer escrow is an optional enterprise add-on: an organization can nominate a trusted third-party escrow agent (or a threshold of three trusted peers) to hold key recovery material. This matters for continuity — if an organization's IT team is unreachable, the network should not permanently lose access to the data they published. The escrow mechanism should use Shamir's Secret Sharing: split the key into N shares, require K to reconstruct, distribute to K trusted organizations in the federation. No single escrow holder can unilaterally recover the key.

Central key management (one key authority for all nodes) is explicitly rejected. It recreates the hub-and-spoke failure mode in the security layer, and it means a subpoena served on the coordinator could expose all organizations' data simultaneously.

### 2.3 Audit Trail Architecture

Audit trails in a federated system face a tension: comprehensive logging is valuable for accountability, but raw audit logs contain PII and operational metadata that organizations may be prohibited from sharing.

Phase 6 should implement a **two-layer audit architecture**:

**Layer 1 — Local audit log**: Each node maintains a comprehensive, tamper-evident append-only log of all local actions (creates, edits, deletes, access events, moderation decisions) and all received federation activities. This log is stored locally, never federated, and is subject to the organization's own retention and access policies. Tamper-evidence is achieved via hash chaining (each entry includes the hash of the previous entry), similar to certificate transparency logs.

**Layer 2 — Federation activity log**: Each node publishes an ActivityPub `OrderedCollection` at `/audit/public` containing only the activities it has sent to the network (not received), stripped of PII. This is the publicly accountable layer: any federation partner can verify that Node A's claimed activity history matches what they actually received.

### 2.4 Access Control: Org-to-Org Permission Policies

Phase 4 established bilateral trust (Node A follows Node B, Node B accepts). Phase 6 needs a richer permission model for cases where one organization wants limited visibility into another's data without full federation.

Proposed model: **Federation Permission Tiers**

- **Tier 0 (Public)**: Follows without requiring approval. Receives all public activities.
- **Tier 1 (Verified Partner)**: Requires mutual admin approval. Enables access to access-controlled metadata.
- **Tier 2 (Data Sharing Agreement)**: Requires signed agreement stored as a hash-committed document on both nodes. Enables federated access to restricted datasets.
- **Tier 3 (Research Consortium)**: Multi-party arrangement. Requires N-of-M signatures from consortium admins. Used for joint research projects with shared private workspaces.

The permission tier is stored in the `federation_partners` table introduced in Phase 4, extended with a `tier` column and a `agreement_hash` field for Tier 2 and above.

### 2.5 Governance: Who Can Join?

Three models exist in the wild: open entry (anyone can run a Mastodon instance and federate), approval-required (Matrix rooms can be invite-only), and paid/credentialed membership.

For open-repo, the recommended model is **open entry with soft defederation**. Any organization can run an instance and attempt to federate with others. But because research transparency is the use case, nodes are expected to have a visible organizational identity — they publish a human-readable `about` page with contact information and a stated mission. A federated node that behaves maliciously (spam, fake data, harassment of researchers) can be defederated by any individual node, and federation communities can maintain shared blocklists (analogous to Mastodon's instance blocklist ecosystem).

No central authority grants or revokes membership. This is the correct design for a network that exists partly to resist institutional capture.

---

## 3. Economic Model for Federation

### 3.1 The Sustainability Precedent

The Matrix.org Foundation's 2024-2025 experience is instructive. With over 250,000 daily active users on the matrix.org homeserver alone, the Foundation ran at a $1.2M annual operating cost against $561K in revenue — a 53% deficit. The lesson is not that federation is uneconomical; it is that a foundation running a reference node at scale needs diversified revenue and cannot rely solely on donations. By contrast, the many independent Matrix homeservers operated by organizations for their own users are economically sustainable because the cost is proportional to the user base and paid by the beneficiaries.

Open-repo should learn from this: **the coordination layer must be cost-minimal and funded independently; the operational layer is self-funded by each organization**.

### 3.2 Tier Structure

**Tier 0 — Self-Hosted (Free)**
Any organization can run open-repo on their own infrastructure at zero licensing cost. All federation protocol features are available. Limits: no SLA guarantee from the project, no centralized support, no participation in optional analytics aggregation. This tier is the default for technical organizations and is essential to the network's credibility — if self-hosting is impossible or crippled, the federation is a vendor-lock-in mechanism in disguise.

**Tier 1 — Managed Hosting (Paid)**
The open-repo project (or a designated hosting cooperative) provides managed infrastructure for organizations that cannot self-host. Pricing is based on storage, monthly active users, and support level. Suggested baseline: $200–600/month for small organizations (<100 users, <50 GB data). This tier funds the maintenance of the hosted platform but not the protocol development.

**Tier 2 — Federation Analytics (Paid Add-On)**
Opt-in aggregate analytics: cross-network endorsement trends, citation graphs, dataset discovery metrics. Organizations pay for dashboard access. Individual user data is never included. Revenue from this tier funds protocol development and the public registry.

**Tier 3 — Enterprise (Contract)**
SLA guarantees, dedicated support, custom compliance documentation (for organizations with specific regulatory requirements), and participation in the governance advisory body. Modeled after Mastodon gGmbH's service contracts with the European Commission and the state of Schleswig-Holstein (signed 2024).

### 3.3 Cross-Organization Data Access: Who Pays?

When Org A's researcher accesses data published by Org B (read-only, public), no payment is required — this is the free layer of the network that creates the value proposition. If Org A's researchers generate significant traffic on Org B's node through automated scripts or large dataset downloads, bandwidth costs are an externality.

The Phase 6 solution is **egress rate limiting with voluntary cost-sharing**. Each node can configure:
- A free egress quota per federation partner per month (default: 10 GB)
- A cost-recovery rate for excess egress (suggested: $0.01/GB, below AWS transfer pricing)
- An exemption list for partners with whom they have reciprocal or charitable relationships

This is not automated billing — it is a signal system. If Org B is consistently absorbing significant egress costs from Org A's usage, the federation permission system should surface that data, enabling a direct conversation about cost-sharing or upgrading to a Tier 2 or Tier 3 relationship.

### 3.4 Incentive Structure: Why Join?

The network effect value proposition has three components:

**Discovery**: A dataset on an isolated node is found only by people who already know that node exists. The same dataset, federated across a network of 50 nodes with combined search indices, is discoverable by everyone in those organizations' research communities. This is the same argument that drove early adoption of email federation and XMPP.

**Credibility**: Endorsements from multiple independent organizations carry more weight than self-endorsements. A research dataset that three independent organizations have cited and endorsed is more credible than one endorsed only by its publisher. This is structurally similar to how citation counts work in academic publishing, but decentralized.

**Resilience**: A dataset mirrored (with the author's permission) across three nodes survives the takedown of any one node. For organizations doing adversarial transparency work — documenting government misconduct, corporate malfeasance, or civil rights violations — this is not a theoretical benefit.

### 3.5 Coordination Infrastructure Funding

The public registry, protocol documentation, and reference implementation require ongoing funding independent of any single organization. Recommended structure: a small non-profit entity (modeled on the Kiwix Association or the XMPP Standards Foundation) funded by Tier 3 enterprise contracts, grants from journalism and transparency foundations, and voluntary contributions from Tier 1 operators. The foundation should publish annual accounts. The target is a minimal footprint — 1-2 FTE for protocol maintenance, documentation, and community coordination — requiring approximately $200–300K/year.

---

## 4. Enterprise Operational Requirements

### 4.1 SLA Guarantees Across Independent Operators

The fundamental tension in a federated network is that an organization's researchers may depend on data hosted by a node they do not control. If Org B's node goes down, Org A's researchers experience degraded access to Org B's datasets.

Phase 6 cannot offer uptime guarantees for other operators' nodes. What it can offer is **graceful degradation with clear observability**. When a federation partner becomes unreachable:

1. The requesting node should return cached data (up to 24 hours stale) with a clearly labeled `[cached — source node unavailable as of HH:MM UTC]` notice.
2. The federation health dashboard (see 4.4) should surface the outage immediately.
3. If the partner has been down for more than 48 hours, the requesting node's admin receives an alert and can choose to either extend the cache window or remove the partner from the active federation list temporarily.

Organizations with enterprise requirements can establish bilateral SLAs with their specific federation partners — this is a contractual relationship between those two organizations, not something the protocol enforces. The Tier 3 commercial model can facilitate these agreements.

### 4.2 Data Durability: Backup and Replication

Each organization is responsible for its own backup strategy. The protocol does not require cross-organization replication. However, Phase 6 should provide tools to make replication easy:

**Option A — Self-managed backups**: The open-repo admin toolkit (Phase 5 extension) should include a `backup-export` command that produces a portable archive (JSON-LD + attachments + event log) in a format that any open-repo node can import. This is the exit strategy and the disaster recovery mechanism simultaneously.

**Option B — Federated mirror agreements**: Using the Tier 2/3 permission system, two organizations can establish a mirror agreement in which each stores a full encrypted copy of the other's dataset archive. Decryption requires the originating organization's key — the mirror node cannot read the data, but it can restore the archive if the primary node is destroyed.

Option B is the most resilient design but requires explicit trust relationships. It should be optional and well-documented, not assumed.

### 4.3 Security Incident Response Across the Federation

A security incident at one federation node — a data breach, a compromised signing key, a malicious admin — affects the entire network's trust graph.

Phase 6 should define a **Federation Security Response Protocol (FSRP)**:

**Detection**: Any node that detects anomalous federation behavior (unexpected activity floods, signature verification failures, unusual data patterns) can broadcast a signed `Flag` activity to its known federation partners. This is analogous to a Certificate Transparency audit alert.

**Containment**: Upon receiving a credible `Flag` for a specific node, recipient nodes should enter a `quarantine` state for that partner: continue accepting activities but queue them for manual review rather than applying them immediately. This provides a window for investigation without full defederation.

**Revocation**: If the incident is confirmed, the compromised node's operator (or any operator who has verified the compromise) publishes a signed `KeyRevocation` activity. All receiving nodes should drop cached public keys for that node and refuse further unsigned or newly-signed activities until a new key is published through a verified out-of-band channel (email to the registered admin, signed announcement from a trusted third party).

**Coordination channel**: The network needs an out-of-band communication channel for security incidents — a mailing list or Matrix room for federation administrators, maintained separately from the federation protocol itself. This mirrors how certificate authority security incidents are handled via the CA/Browser Forum.

### 4.4 Monitoring and Observability

Phase 6 should expose a **Federation Health API** at `/.well-known/open-repo/health` returning:

```json
{
  "version": "1.0",
  "node_id": "https://node.example.org",
  "status": "operational",
  "federation_partners": {
    "total": 12,
    "active": 11,
    "degraded": 1,
    "offline": 0
  },
  "sync_lag_p95_seconds": 45,
  "last_activity_received": "2026-04-29T14:23:00Z",
  "last_activity_sent": "2026-04-29T14:25:00Z"
}
```

A public network-level dashboard (analogous to `matrixrooms.info` for Matrix) should aggregate health reports from nodes that opt in to public monitoring. This enables prospective federation partners to evaluate a node's reliability before establishing a relationship.

Key metrics to track at the network level:
- Median and p95 activity propagation latency (time from Create on source node to indexing on remote nodes)
- Percentage of federation pairs with <60-second sync lag (target: >95%)
- Number of unresolved content conflicts per month
- Node uptime distribution

### 4.5 Rollout and Migration Strategy

Organizations migrating from an isolated open-repo instance to the federated network should follow a three-phase migration:

**Phase A — Shadow mode (2 weeks)**: The node's federation service is enabled but all received activities are logged, not applied. This lets the admin verify that incoming data volume, jurisdictional tags, and content types match expectations before any data enters the local database.

**Phase B — Read-only federation (2 weeks)**: The node processes incoming activities (can search federated content) but does not publish its own activities to peers. This allows researchers to see the value of federation before the organization commits to publishing.

**Phase C — Full federation**: The node publishes activities and receives them. At this point the organization appears in the public registry (if opted in).

This graduated rollout mirrors best practices from Matrix's partial state joins (faster joins), which allow a server to participate in a room's current activity before fully syncing historical state.

---

## 5. Governance and Evolution

### 5.1 Protocol Governance Structure

ActivityPub's post-W3C working-group experience provides a cautionary model. After the WG closed, protocol evolution moved to the Fediverse Enhancement Proposal (FEP) process — a community-led, merge-request-based system that is explicitly informal. The result is that FEPs accumulate faster than implementations can absorb them, and interoperability regressions between major implementations (Mastodon, Lemmy, Misskey) are common.

Open-repo should adopt a more structured model from the outset, modeled on the IETF's process: a small steering group (3-5 people from distinct organizations) reviews and approves protocol changes, with a mandatory public comment period and documented rationale for all decisions. Changes are classified as:

- **Additive extensions**: New fields, new activity types. Backward compatible. Can be merged with steering group approval + 30-day comment period.
- **Behavioral changes**: Modifications to how existing activities are processed. Require a protocol version bump. 90-day comment period, two independent implementation proofs required before merging.
- **Breaking changes**: Removal of existing capabilities. Require a deprecation period of no less than one year, announced to all registered nodes.

Protocol version is carried in the ActivityPub actor object as `x-open-repo-protocol-version`. Nodes reject activities from peers claiming an incompatible protocol version and log the mismatch for admin attention.

### 5.2 Version Compatibility

The recommended versioning strategy uses semantic versioning with explicit compatibility windows:

- **Minor versions** (1.0 → 1.1): Always backward compatible. All nodes in the 1.x series can federate with each other.
- **Major versions** (1.x → 2.0): May introduce breaking changes. Nodes running 1.x and 2.0 can federate via a compatibility mode that strips or translates unsupported fields. Compatibility mode is maintained for a minimum of 24 months.

This is analogous to how email servers handle protocol evolution: an SMTP server from 2010 can still exchange mail with a 2026 server, because extensions are negotiated via `EHLO` capability advertisement rather than mandated globally.

### 5.3 Exit Strategy and Data Portability

An organization must be able to leave the federation at any time with its data intact. This is not just an ethical requirement — it is the design constraint that prevents the network from becoming extractive.

The exit protocol:

1. The departing organization's admin publishes a signed `Unfollow` to all federation partners, with a `data-export-available` flag indicating that a portable export is available at a signed URL for 90 days.
2. Partners who have mirrored data from the departing node receive a notification that the source node is leaving and should decide whether to retain or delete their copies.
3. The departing organization runs `open-repo export --format=portable`, producing a structured archive containing all items in JSON-LD format, all events (CQRS event log), all endorsements, and all federation activity history.
4. This archive can be imported into any open-repo instance or processed independently — it is not a proprietary format.

The 90-day grace period for data export is modeled on GDPR's right to data portability (Article 20) and should be available to all departing nodes regardless of reason.

### 5.4 Community Building and Governance Evolution

Protocol governance must grow alongside the network. The recommended trajectory:

**Phase 6.0 (0–12 months)**: Core team makes all protocol decisions; community feedback via GitHub issues. Simple, fast, appropriate for a pre-critical-mass network.

**Phase 6.1 (12–24 months, contingent on 10+ active nodes)**: Elect a 3-person technical steering committee from representatives of active federation organizations. First FEP-style enhancement proposals accepted.

**Phase 6.2 (24+ months, contingent on 50+ active nodes)**: Formalize as an independent standards body or join an existing one (e.g., W3C Community Group, SocialHub). Establish a code of conduct enforced by the steering committee. Model on the ActivityPub community's hard-won lessons: explicit governance prevents the informal power concentrations that plagued early Fediverse development.

---

## Recommended Phase 6 Sequencing

Phase 6 spans an estimated 12–18 months and three sequential sub-phases. Each sub-phase produces independently deployable value.

### Sub-Phase 6A: Foundation (Months 1–5)
*Goal: The protocol can handle real-world multi-organization scenarios safely.*

1. Data boundary enforcement — residency tagging, `federationPolicy` on objects, inbound residency filters
2. Content deduplication by CID — `sameAs` relationship for equivalent datasets across nodes
3. Three-way conflict resolution interface for concurrent edits
4. Federation Health API and per-node health dashboard
5. Security incident protocol (Flag/Quarantine/Revocation activities)
6. Graduated migration rollout tooling (shadow → read-only → full)

**Why first**: Without data boundary enforcement, EU organizations cannot safely participate. Without the health API, operators cannot make informed federation decisions.

### Sub-Phase 6B: Identity and Permissions (Months 4–9)
*Goal: Researchers have portable identities; organizations have expressive permission controls.*

1. DID:WEB integration for researcher identity
2. Federation Permission Tier system (Tier 0–3 with agreement hash storage)
3. Per-organization key management with optional Shamir escrow
4. Two-layer audit architecture (local tamper-evident + public federation activity log)
5. Egress rate limiting and cost-signal system

**Why second**: Identity portability is high-value but not required for basic multi-org federation. The permission tier system requires the data boundary work from 6A to be meaningful.

### Sub-Phase 6C: Economics and Governance (Months 8–18)
*Goal: The network is self-sustaining and has a defined path for protocol evolution.*

1. Managed hosting tier infrastructure
2. Opt-in federation analytics (Tier 2)
3. Public registry with health integration
4. Technical steering committee formation (if node count warrants)
5. Protocol versioning machinery (compatibility mode, version negotiation)
6. Exit protocol and portable export tooling
7. Governance documentation and FEP-equivalent process

**Why last**: You cannot govern what does not yet exist. Governance overhead imposed on a sub-10-node network creates process debt without benefit.

---

## Success Metrics

### Network Health
| Metric | Phase 6A Target | Phase 6B Target | Phase 6C Target |
|---|---|---|---|
| Active federated nodes | 3–5 (pilot partners) | 10–20 | 50+ |
| Activity sync lag p95 | <120 seconds | <60 seconds | <30 seconds |
| Unresolved content conflicts per month | <10 | <5 | <2 |
| Nodes with public health endpoint | 100% | 100% | 100% |

### Adoption and Trust
| Metric | Target |
|---|---|
| Organizations completing full 3-phase migration | >80% complete all 3 phases |
| Defederation incidents (nodes removed by community) | <1 per quarter by 6C end |
| Cross-org endorsements as % of total endorsements | >30% by end of 6C |
| Researcher DID adoption rate | >50% of active researchers on multi-org nodes |

### Compliance Readiness
| Metric | Target |
|---|---|
| Nodes with declared residency policy | 100% before public launch |
| Nodes passing automated compliance health check | >95% |
| Documented Transfer Impact Assessments for EU nodes | Available as template, adopted by 100% of EU operators |

---

## Risk Assessment

### Risk 1: EU-US Data Residency Creates Network Fragmentation
**Likelihood**: High. **Impact**: Medium.
**Description**: If residency enforcement is strict, EU nodes and US nodes may be unable to federate without explicit SCCs, creating de facto regional sub-networks. This fragments the discovery value proposition.
**Mitigation**: Design the residency tagging system to be expressive enough to satisfy compliance without defaulting to outright rejection. SCCs can be implemented as a Tier 2 digital agreement. Engage an EU data protection lawyer during 6A to verify the technical design.

### Risk 2: ActivityPub Extension Proliferation Breaks Interoperability
**Likelihood**: Medium. **Impact**: High.
**Description**: Each open-repo enhancement (DID:WEB, residency tags, permission tiers) is an ActivityPub extension. If other Fediverse platforms implement incompatible versions of similar extensions, open-repo nodes may diverge from the broader ecosystem.
**Mitigation**: Submit all extensions as FEPs to the ActivityPub community early. Follow the `x-open-repo-` namespace convention to avoid collisions. Participate in SocialHub discussions about standardizing data residency and permission primitives.

### Risk 3: Coordination Layer Under-Funding Stalls Protocol Development
**Likelihood**: Medium. **Impact**: High.
**Description**: The Matrix.org Foundation's financial crisis (2024-2025) shows that reference implementations and coordination infrastructure are chronically underfunded in federation networks. Without paid maintainers, the protocol stagnates and security issues go unpatched.
**Mitigation**: Secure Tier 3 contracts before launching the public network. Pursue foundation grants (NLnet funded Lemmy's federation work; similar grants are available for open-source infrastructure). Design the coordination layer to require minimal ongoing maintenance — static documentation, automated test infrastructure, no required runtime services.

### Risk 4: Malicious Nodes Degrade Network Trust
**Likelihood**: Low initially, higher as network grows. **Impact**: Medium.
**Description**: A bad-faith organization could join the network, publish plausible-looking fabricated research data, and leave before detection. Federated nodes that mirrored the data would need to purge it after the fact.
**Mitigation**: Soft defederation (any node can reject a partner) limits propagation. The `sameAs` deduplication system makes it harder to inject fake versions of real datasets — a hash collision would be required. Cross-organization endorsements create a reputation signal — new nodes with no endorsement history from trusted organizations should be flagged as provisional in the UI.

### Risk 5: Protocol Ossification Under Governance
**Likelihood**: Low in 6A-6B, increases in 6C. **Impact**: Medium.
**Description**: Formal governance processes can slow protocol evolution to the point where necessary changes cannot be made quickly. XMPP's governance maturity contributed to its loss of momentum against non-federated alternatives.
**Mitigation**: Keep breaking-change governance heavy; keep additive extension governance light. Reserve the 90-day comment period for behavioral changes, not new fields. Ensure the steering committee includes at least one person whose role is to advocate for simplicity and removal of complexity.

---

## Sources

1. [ActivityPub W3C Specification](https://www.w3.org/TR/activitypub/) — W3C Recommendation, primary protocol reference
2. [Matrix Specification — Federation API](https://spec.matrix.org/latest/) — State resolution algorithm, federation transport, partial state joins
3. [Matrix.org — 2024 Roadmap and Fundraiser](https://matrix.org/blog/2024/01/2024-roadmap-and-fundraiser/) — Foundation economics and sustainability data
4. [Matrix.org — We're at a crossroads (February 2025)](https://matrix.org/blog/2025/02/crossroads/) — Revenue/cost gap, sustainability challenges
5. [Mastodon Annual Report 2024](https://blog.joinmastodon.org/2025/12/annual-report-2024/) — Federation economics, service contract model
6. [Mastodon — Service Offerings (2025)](https://blog.joinmastodon.org/2025/09/service-offerings-from-mastodon/) — Enterprise service tier pricing model
7. [Fediverse Enhancement Proposals — Codeberg Repository](https://codeberg.org/fediverse/fep) — FEP governance process
8. [The Efforts to Extend ActivityPub — We Distribute (March 2024)](https://wedistribute.org/2024/03/extending-activitypub/) — Extension landscape, governance gaps
9. [GDPR Cross-Border Data Transfers 2025 — SecurityAlign](https://securityalign.com/insights/gdpr-cross-border-data-transfers-2025) — SCC requirements, updated geofencing mandates
10. [Data Sovereignty in 2025 — Sovy](https://www.sovy.com/blog/data-sovereignty/) — 62-jurisdiction localization data, growth trend
11. [Lemmy Federation Documentation — SocialHub](https://socialhub.activitypub.rocks/t/we-have-created-documentation-on-how-exactly-lemmy-federation-works/1085) — Community federation implementation reference
12. [NLnet — Lemmy Federation Funding](https://nlnet.nl/project/LemmyFed-AP/) — Grant model for open federation infrastructure
13. [ActivityPub Federation Library (Rust) — LemmyNet/activitypub-federation-rust](https://github.com/LemmyNet/activitypub-federation-rust) — High-level federation implementation patterns
14. [DID Link: Authentication in TLS with Decentralized Identifiers](https://arxiv.org/html/2405.07533v2) — DID:WEB integration with existing TLS infrastructure
15. [CQRS Pattern — Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs) — CQRS/event sourcing reference for federation sync design
16. [Multi-Tenant Database Design Patterns 2024 — Daily.dev](https://daily.dev/blog/multi-tenant-database-design-patterns-2024) — Per-tenant encryption key isolation patterns
17. [Event Sourcing Pattern — Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing) — Append-only event log for audit trail design
18. [A Glimpse of the Matrix (Extended Version) — arXiv](https://arxiv.org/pdf/1910.06295) — Academic analysis of Matrix federation and CAP theorem tradeoffs
