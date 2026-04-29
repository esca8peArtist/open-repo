---
title: "Phase 5: Federation Conflict Resolution & Scaling Architecture"
project: open-repo
phase: 5
status: design-proposal
date: 2026-04-29
author: research-agent
confidence: high
tags: [federation, crdt, conflict-resolution, distributed-systems, consensus, merkle, vector-clocks, activitypub]
---

# Phase 5: Federation Conflict Resolution & Scaling Architecture

**Status**: Design Proposal — ready for Phase 5 implementation planning after PR #1 merges
**Audience**: Open-repo core developers (assumes familiarity with Phase 4 ActivityPub federation basics)
**Prerequisite**: Phase 4 Wave 4 complete — `federation_partners` table, HTTP signature verification, partner trust state machine all implemented
**Word count**: ~3,800 words

---

## Executive Summary

Phase 4 gives us a working two-node federation: partners register, activities are signed and verified, and endorsements propagate. What Phase 4 does not give us is any answer to five failure modes that become unavoidable as the network grows beyond two manually-managed nodes. This document names those five scenarios, analyzes the resolution strategies available for each, and proposes a unified architecture that Phase 5 can implement incrementally.

The core recommendation is a **layered conflict model**: content-addressed immutable blobs as the base layer (eliminating most storage conflicts by definition), vector-clock-tagged versions for mutable metadata (enabling causal divergence detection), gossip-based Merkle-tree comparison for anti-entropy synchronization (efficient at scale without O(N²) messaging), and an explicit quarantine-and-review workflow for trust failures (because Byzantine faults cannot be resolved algorithmically without human judgment in an open federation). Consensus protocols (Raft, PBFT) are deliberately excluded from the core path — they are expensive, require fixed quorums, and are architecturally incompatible with the voluntary, asynchronous nature of the open-repo federation model.

---

## Part 1: The Five Conflict Scenarios

### 1.1 Content Conflict: Same Resource, Different Content

**Scenario**: Node A hosts `/wiki/climate-science` at version 5. While Node A and Node B are both online and federated, a contributor on Node A edits the article (now version 6A), and simultaneously a different contributor on Node B edits the same article (now version 6B). Both nodes propagate `Update` activities to each other. Each receives an incoming version 6 that conflicts with its own locally-held version 6.

**Root causes in the current Phase 4 implementation**:
- The `version` field is an integer that increments independently on each node. Two nodes can reach version 6 by different paths without any coordination.
- The current conflict detection in `content_conflicts` logs conflicts but applies last-write-wins by wall-clock timestamp, meaning one edit is silently discarded without the editing contributor ever knowing.
- There is no concept of a common ancestor — the system cannot tell an admin *what changed* on each side, only that the two version-6 payloads differ.

**Why this matters at scale**: At two nodes with manual admin oversight, a few flagged conflicts per month is manageable. At fifty nodes with frequent edits, silent last-write-wins produces permanent data loss. Admins cannot meaningfully review hundreds of conflict notifications without tooling that shows them a diff.

**The Byzantine fault tolerance question**: Full BFT requires 3f+1 nodes to tolerate f malicious actors, with voting overhead proportional to N². For content conflicts between honest nodes (simple concurrent edits), BFT is massively over-engineered. The right tool is causal versioning plus a merge UI, not consensus.

**Real-world precedent**: Wikipedia handles concurrent edits at massive scale through edit conflict detection (shows you the diff between your edit and what's now the current version), not through consensus. The "conflict" is surfaced to the human editor who made the second save, not resolved automatically.

---

### 1.2 Version Divergence: Lagging and Catching-Up Nodes

**Scenario**: Node A publishes an update to Domain-X on April 15. Node B goes offline April 10–20. Node C joins the federation on April 18. When Node B comes back online on April 20, it has a 10-day gap. Node C has never seen any activity before its join date.

**The catching-up problem**: The current ActivityPub inbox/outbox model delivers activities in real-time. If a node is offline during delivery, the activity is attempted, fails, and (with the retry queue added in Phase 4) may be retried up to three times over 24 hours. After that, the activity is dropped. Node B returns to a permanently incomplete state unless it can request a full re-sync.

**The join-at-point-in-time problem**: Node C joined on April 18. It has never seen activities from before that date. If it wants to have a complete view of Domain-X's history, it needs a mechanism to fetch historical activities, not just receive new ones. The ActivityPub `outbox` endpoint returns an ordered collection that *can* be paginated back in time — but no current Phase 4 code implements catching up from the outbox of a federation partner.

**Git analogy**: This is precisely the problem that `git pull` with `--rebase` versus `--merge` solves differently. Rebase replays your local commits on top of the remote state — equivalent to a catching-up node applying remote activities in order, then replaying its own local changes. Merge creates a new commit that combines both histories — equivalent to a three-way merge of the diverged states. Both are valid; the choice depends on whether preserving the temporal order of local edits matters.

**Key question for Phase 5**: Should a catching-up node request activities via outbox pagination (replay semantics, preserves history) or request a current-state snapshot (snapshot semantics, efficient but loses intermediate history)? The answer is architecture-defining. Snapshot is simpler to implement and sufficient for most use cases; replay is necessary for audit-trail integrity.

---

### 1.3 Trust Cascades: Compromised Node Propagation

**Scenario**: Node A is a trusted federation partner of both Node B and Node C. An attacker compromises Node A — either gaining admin access or replacing its signing key. The attacker begins publishing `Update` activities containing fabricated or malicious content. Because Node A is in `trust_status = 'trusted'` on both B and C, those activities are automatically applied.

**Propagation risk**: In the current Phase 4 model, once an activity passes signature verification and trust-status check, it is applied immediately. There is no rate-limit on how many updates a trusted partner can push, no anomaly detection on content, and no "staging" layer before application. A compromised trusted partner can update every item it previously authored, and those updates propagate to all of that partner's trusted peers within the normal activity-delivery window.

**Historical precedent — Wikipedia vandalism**: Wikipedia's Counter-Vandalism Unit documents that automated bots can introduce vandalism at rates that briefly outpace human reverters. The defense is a combination of human watchlists, automated scoring (ORES, which flags probable vandalism before it is applied to the visible article), and the ability to bulk-rollback all edits by a compromised account. Open-repo needs analogous tooling: not just the ability to revoke a partner, but the ability to *retroactively* identify and roll back activities ingested from that partner.

**The compounding risk in a mesh**: If Node B trusted Node A and Node B is trusted by Node D, can Node A's compromised content reach Node D via Node B? In the current architecture, yes — because Node B re-propagates updates it applies locally. Defederation of Node A by Node B does not automatically reach Node D unless Node D independently defederates Node A as well. This is the trust cascade problem: one compromised node can poison multiple hops.

---

### 1.4 Split-Brain Scenarios: Network Partition

**Scenario**: A network partition splits the open-repo federation into two sub-networks: {Node A, Node B} and {Node C, Node D}. Both groups continue operating independently for three days. During those three days, items are created, edited, and endorsed on both sides. On day four, the network heals and the nodes attempt to re-federate.

**The CAP theorem framing**: Every distributed system that experiences network partitions must choose, during the partition, between Consistency (refuse writes to stay consistent) and Availability (accept writes and risk divergence). Open-repo nodes are available-during-partition by design — they do not pause operations while waiting for unreachable partners. This means they choose AP over CP, which is the right choice for a knowledge repository (a node that refuses to accept new articles because its federation partners are unreachable would be unusable). The cost of this choice is that divergence must be reconciled when the partition heals.

**Cassandra/DynamoDB precedent**: Cassandra uses a gossip-based anti-entropy mechanism — each node periodically compares Merkle tree roots with its peers to identify diverged data, then repairs the differences. DynamoDB originally used vector clocks to detect conflicting versions and returned all conflicting versions to the client for reconciliation. The key insight from both systems: efficient divergence detection (Merkle root comparison is O(log N) in tree depth, not O(N) in item count) is separate from conflict resolution policy (which can be LWW, CRDT, or human review).

**Convergence semantics for open-repo**: When the partition heals and {A,B} reconnects with {C,D}, each side needs to:
1. Detect what diverged (Merkle tree comparison)
2. Exchange the diverged items (activity replay or snapshot transfer)
3. Apply a resolution policy for genuine conflicts (same item edited on both sides during partition)

Steps 1 and 2 are engineering problems with known solutions. Step 3 is a policy decision that Phase 5 must make explicit.

---

### 1.5 Rollback Semantics: Reverting Propagated Bad Versions

**Scenario**: A content error or malicious edit propagates across three nodes before being detected. An admin on the originating node wants to revert the item to its pre-error state. How does that revert propagate?

**The current state**: Phase 4 has a `Delete` activity type (tombstone) and an `Undo` activity type (retract endorsement). There is no `Rollback` activity type — no mechanism to say "revert item X to version N-3" across the federation.

**Transaction journal requirement**: Rollback requires that each node maintains enough history to reconstruct prior states. If nodes store only the current version of each item (not the full edit history), rollback requires the originating node to re-publish the prior state as a new `Update` activity at a higher version number. This works but is semantically messy — it creates a "forward rollback" rather than a true reversion.

**Git reflog / MySQL binlog analogy**: Git's reflog maintains a local history of all ref changes, enabling `git reset --hard HEAD~3` even after the commits are no longer reachable from the current branch. MySQL's binary log enables point-in-time recovery by replaying all changes from a known-good snapshot. For open-repo, the CQRS event log (designed in Phase 5's service architecture) is the equivalent: an append-only log of all state-changing events that enables replaying the full history of any item.

**The cross-node rollback problem**: Even if Node A can reconstruct item X at version N-3, Nodes B and C have already applied versions N-2, N-1, and N. Reverting Node B and Node C requires propagating a new `Update` activity (with the rolled-back content) to all affected partners. Nodes B and C will accept this as a new version — version N+1 containing the rolled-back content. The history record on each node will show the rollback as an explicit event, not a clean erasure.

---

## Part 2: Resolution Strategies and Technology Choices

### 2.1 Technology Primer

Before evaluating options, a brief description of each technology for readers who haven't worked with all of them:

**CRDTs (Conflict-free Replicated Data Types)**: A class of data structures designed so that concurrent updates from multiple sources can always be merged into a single consistent state without human intervention. CRDTs achieve this by choosing only operations that are commutative, associative, and idempotent — meaning the order and repetition of operations does not change the final result. Formally defined by Shapiro et al. (INRIA, 2011), CRDTs come in two families: state-based (CvRDT, merge the full states) and operation-based (CmRDT, merge the operation logs). Leading implementations include Automerge (JSON CRDT, written in Rust with JS/WASM bindings) and Yjs (text-optimized CRDT using the YATA algorithm). CRDTs are best for shared editing of fine-grained data where automatic convergence is more important than semantic correctness.

**Consensus protocols (Raft, Paxos, PBFT)**: Algorithms that enable a cluster of nodes to agree on a single value or sequence of values, even if some nodes fail. Raft is the most practically understandable: it elects a leader who serializes all writes; followers replicate from the leader; if the leader fails, a new leader is elected with majority vote. A 5-node Raft cluster tolerates 2 simultaneous failures. PBFT (Practical Byzantine Fault Tolerance) extends this to tolerate nodes that actively lie — it requires 3f+1 nodes to tolerate f malicious nodes. Consensus is strong but expensive: it adds latency proportional to network round-trip time and requires a quorum of nodes to be online for any write to succeed (choosing CP over AP).

**Git semantics (3-way merge)**: Git resolves divergent histories by finding the common ancestor of two branches and applying both sets of changes relative to that ancestor. If the changes are to different parts of the content, they merge automatically. If both sides changed the same part, a conflict marker is inserted and a human resolves it. This model requires storing the common ancestor (or computing it from the event log) and is inherently interactive for genuine conflicts.

**Content addressable storage (Merkle trees, IPFS CIDs)**: Content is identified by the cryptographic hash of its bytes, not by a mutable name. Two nodes that hold the same content will have identical CIDs regardless of when or how they received it. This eliminates a whole class of "same content, different identity" conflicts. Merkle trees build on this: a tree where each parent node's hash is derived from its children's hashes, so the root hash is a summary of all content in the tree. Comparing root hashes tells you instantly whether two nodes are identical; descending the tree identifies exactly where they diverge. Used by IPFS, Git, and Cassandra's anti-entropy repair.

**Eventual consistency with gossip**: Nodes propagate updates peer-to-peer in rounds, each round contacting a random subset of peers. Information spreads exponentially: in O(log N) rounds, all N nodes have received the update. Cassandra uses gossip for cluster state; the cost is temporary divergence and O(N log N) total message complexity per update (significantly better than direct broadcast's O(N²)).

---

### 2.2 Per-Scenario Strategy Analysis

#### Scenario 1 — Content Conflict

**Strategy A: CRDT-based automatic merge**
Apply Automerge or Yjs to the item content, treating each field as a CRDT. Concurrent edits to different fields merge automatically; concurrent edits to the same field are resolved by the CRDT's tie-breaking rule (usually actor ID ordering). Cost: requires migrating the item content model to a CRDT-compatible format; adds complexity to the content schema; breaks the clean JSON-LD model that ActivityPub expects.

**Strategy B: Git-style 3-way merge with conflict markers**
Store a common ancestor pointer alongside each item version (the CID of the last mutually-acknowledged version). When a conflict is detected, compute a 3-way diff. If the edits are to different sections, auto-merge. If they overlap, flag the conflict with markers and surface it to an admin with a split-screen diff view. Cost: requires storing ancestor CIDs, implementing a diff algorithm, and building a merge UI. Preserves human judgment for genuine semantic conflicts.

**Strategy C: Last-write-wins with explicit audit trail**
Keep the current LWW policy but make the discarded version permanently accessible in the conflict log, with a diff view so admins can see what was lost. Add a "recover discarded version" button. Cost: some edits are silently discarded in the common case; admins must actively monitor the conflict log.

**Verdict**: Strategy B is the correct long-term choice. For Phase 5 MVP, Strategy C with enhanced tooling (diff view, recovery button) is sufficient and far simpler to implement. Strategy A adds CRDT complexity to a content schema that is not naturally CRDT-shaped.

---

#### Scenario 2 — Version Divergence

**Strategy A: Outbox pagination (replay)**
The catching-up node requests activities from the partner's `/outbox` endpoint, paginating backward until it reaches its last-known activity. Activities are replayed in chronological order. Cost: requires the outbox to retain full history (storage grows unboundedly); slow for large gaps; risks reapplying already-known activities.

**Strategy B: Snapshot transfer**
The lagging node requests a current-state snapshot of a specific resource or domain from the partner. The partner generates a point-in-time export and delivers it. The lagging node replaces its local copy with the snapshot. Cost: loses intermediate history; simpler to implement; works well for joining nodes (Node C joining April 18 can bootstrap from a snapshot).

**Strategy C: Merkle-tree-based delta sync**
Each node maintains a Merkle tree over its content corpus. Two nodes compare their tree roots. If they differ, they recursively exchange sub-tree hashes until they identify exactly which items diverge. Then only the diverged items are transferred. Cost: requires implementing Merkle tree maintenance; most efficient for large corpora with small deltas.

**Verdict**: Phase 5 should implement Strategy B (snapshot) for new node onboarding and Strategy A (outbox replay, limited to 30-day window) for short-gap recovery. Strategy C is the right long-term solution for large-scale anti-entropy and should be planned for Phase 6.

---

#### Scenario 3 — Trust Cascade

**Strategy A: Quarantine mode**
When anomalous behavior is detected from a trusted partner (high volume of updates, signature anomalies, content pattern changes), place that partner's incoming activities into a quarantine queue rather than applying them immediately. An admin reviews and approves or rejects the queued activities. Cost: adds latency to legitimate partner updates; requires anomaly detection heuristics.

**Strategy B: Propagation-scoped trust**
A node marks activities as originating from partner X (provenance tracking). When propagating activities to its own partners, it includes the provenance chain. Downstream nodes can independently decide whether to trust activities that originated from X, even if they were relayed by a trusted intermediary. Cost: requires propagating provenance metadata in all activities; changes the ActivityPub activity schema.

**Strategy C: Retroactive rollback tooling**
After a partner is revoked, add an admin tool that lists all activities ingested from that partner and provides a bulk-rollback option (re-publishes all affected items at their pre-partner-ingestion state). Cost: requires storing snapshots of each item before each modification, or a full event log; complex to implement correctly.

**Verdict**: All three strategies are needed. Phase 5 should implement Strategy A (quarantine mode with a configurable anomaly threshold) and the first half of Strategy C (retroactive listing of partner activities). Strategy B and full retroactive rollback require the CQRS event log and are Phase 6 scope.

---

#### Scenario 4 — Split-Brain

**Strategy A: Explicit partition detection + convergence protocol**
When a node detects that a partner has been unreachable for longer than a configurable threshold (e.g., 48 hours), it logs the partition start time. When the partner reconnects, both nodes exchange their partition-period activity logs and apply a merge. Cost: requires partition detection, activity log timestamping, and a merge protocol.

**Strategy B: Merkle-tree anti-entropy on reconnect**
On reconnect, both nodes immediately compare Merkle tree roots. Diverged subtrees are exchanged. Conflicts within the exchanged items are flagged. This is the Cassandra repair model. Cost: requires Merkle tree implementation; efficient for large divergences.

**Strategy C: Accept divergence, surface to admins**
After reconnect, run a diff of both nodes' item states. Items that exist on only one side are added to the other. Items with diverging content are flagged as conflicts for admin review. No automatic merge. Cost: simplest to implement; may generate large numbers of conflicts after a long partition.

**Verdict**: Strategy C is the correct Phase 5 starting point. Strategy A and B are Phase 6 improvements. A long-term production deployment needs Merkle anti-entropy, but implementing it before the federation has more than a handful of nodes is premature optimization.

---

#### Scenario 5 — Rollback

**Strategy A: Forward rollback via new Update activity**
The originating node re-publishes the item with the correct (pre-error) content as a new `Update` activity at version N+1. All nodes apply it normally. The erroneous versions (N-2 to N) remain in the activity log as historical record. Cost: semantically clean; easy to implement; requires no new activity types.

**Strategy B: Dedicated Rollback activity type**
Define a new `Rollback` activity type that references the target version to restore. Receiving nodes apply the rollback by reverting their local item state. Cost: requires all nodes to implement the new activity type; requires each node to retain enough history to reconstruct target versions.

**Strategy C: Version-tagged snapshot rebroadcast**
When a node needs to roll back, it generates a signed snapshot of the item at the target version (retrieved from the event log) and broadcasts it as a `Create` activity with a special `rollback: true` flag and a reference to the rolled-back version. Receiving nodes update their item state and log the rollback event. Cost: requires event log access; creates a clear audit trail.

**Verdict**: Strategy A is sufficient for Phase 5 — it requires no new protocol additions and produces a clean audit trail. Strategy C is preferable long-term because it explicitly labels rollbacks in the activity stream, making them easily queryable. Strategy B adds protocol complexity without significant benefit over Strategy C.

---

### 2.3 Decision Matrix

The following matrix scores each technology option against each scenario. Scores reflect the cost-to-implement and operational complexity within the specific open-repo architecture (ActivityPub base, asynchronous federation, voluntary participation).

| Scenario | CRDT Cost | Consensus Cost | Git-like 3-Way Merge Cost | Content Hash (Merkle) Cost | Eventual Consistency (LWW + Gossip) Cost | **Recommended** |
|---|---|---|---|---|---|---|
| Content Conflict | Medium — CRDT schema migration required | Very High — quorum breaks async federation | Low-Medium — ancestor pointer + diff UI needed | Low — CID equality eliminates hash collisions | Low — simple but loses data silently | **Git-like (Phase 6) + LWW+audit (Phase 5)** |
| Version Divergence | N/A — not a CRDT problem | High — consensus on ordering | Low — outbox replay is git-like | Low — Merkle delta sync is ideal long-term | Low — snapshot transfer + bounded replay | **Snapshot + bounded replay (Phase 5), Merkle delta (Phase 6)** |
| Trust Cascade | N/A | N/A | N/A | Medium — provenance hashes enable tracking | N/A | **Quarantine + retroactive audit (Phase 5)** |
| Split-Brain | High — CRDT convergence across arbitrary partition | Very High — Raft requires quorum, breaks partition availability | Medium — 3-way merge after partition heals | Medium — Merkle anti-entropy on reconnect | Low — accept divergence, surface conflicts | **Divergence acceptance + admin review (Phase 5), Merkle anti-entropy (Phase 6)** |
| Rollback | N/A | N/A | Low — git reset semantics | Low — CID of prior version | Low — forward-rollback Update activity | **Forward-rollback Update (Phase 5), versioned snapshots (Phase 6)** |

**Cost scale**: Low = <2 weeks to implement, no architectural changes; Medium = 2–6 weeks, moderate schema/protocol changes; High = 6+ weeks, significant architectural changes; Very High = would require replacing core architectural assumptions.

---

## Part 3: Architecture Recommendations

### 3.1 Core Data Model

**Recommendation**: Content-addressed immutable blobs + vector-clock-versioned mutable metadata + append-only event log.

**Content layer (already partially implemented via CID in Phase 1–3)**: All binary content (files, images, PDFs, 3D models) is stored with IPFS CIDs. Identical content produces identical CIDs — there is no "conflict" between two nodes that both hold the same file under the same CID. This layer is conflict-free by definition. Phase 5 does not need to change this.

**Metadata layer (requires Phase 5 change)**: Item metadata (title, description, tags, relationships, version) is currently versioned with a simple integer. Replace this with a **version vector** (also called a vector version): instead of `version: 6`, store `version: {"node-a": 4, "node-b": 2}` representing that the item has been edited 4 times on Node A and 2 times on Node B. Two version vectors can be compared to determine if they are causally related (one happened-before the other) or concurrent (neither is a prefix of the other). Concurrent version vectors indicate a genuine conflict requiring resolution. Non-concurrent vectors are automatically resolved by accepting the higher version.

**Why version vectors over Lamport clocks**: Lamport clocks establish a total order but cannot distinguish causally unrelated events from genuinely concurrent ones. Version vectors (the structure used by Amazon DynamoDB and Riak) preserve the happens-before partial order and correctly identify concurrency.

**Event log (requires Phase 5 implementation)**: Introduce an append-only event log table that records every state-changing operation on every item. Each entry contains: item ID, event type (Create/Update/Delete/Rollback), actor, timestamp, previous version vector, new version vector, and content delta or CID. This log serves triple duty: (a) enables rollback to any prior state, (b) enables catching-up nodes to replay history, (c) provides the audit trail required for trust cascade investigation.

**Explicit tradeoff**: Version vectors grow with the number of nodes that have ever edited an item. In a large mesh federation with hundreds of nodes, this is bounded but non-trivial. Pruning strategies (merging vector entries for nodes that have left the federation) are a Phase 6 concern.

---

### 3.2 Conflict Detection

**Mechanism**: Two-level detection using version vector comparison (fast, per-item) and periodic Merkle root exchange (background, per-corpus).

**Per-item conflict detection (implement in Phase 5)**: When an `Update` activity arrives at the `/inbox`, the federation service compares the incoming version vector against the local version vector. Three outcomes:
1. **Incoming dominates local** (incoming vector >= local on all node entries): Apply the update. No conflict.
2. **Local dominates incoming** (local vector >= incoming on all entries): Discard the incoming update as stale. Log for debugging.
3. **Concurrent** (neither dominates the other): Flag as conflict. Store both versions in the `content_conflicts` table. Do not apply either version automatically. Notify admin.

This detection runs on every incoming `Update` and adds approximately one database read per activity (the local version vector lookup). Cost is negligible.

**Corpus-level Merkle comparison (plan for Phase 5, implement in Phase 6)**: Periodically (every 4–24 hours depending on federation size), each node broadcasts a Merkle root hash of its entire content corpus to its federation partners. If a partner's Merkle root differs from the locally-computed root (based on the last activity that partner sent), the two nodes schedule a tree-descent reconciliation to find the diverged items. This catches divergences that were not propagated through the normal inbox/outbox path (e.g., due to transient delivery failures).

Cassandra implements exactly this pattern with its "anti-entropy repair" mechanism using Merkle trees over partition key ranges. The cost is O(log N) round trips for each pair of nodes, O(N²) pairs total — acceptable at federation sizes below ~100 nodes.

---

### 3.3 Resolution Mechanisms

**Content conflicts (concurrent edits)**: The conflict is stored in `content_conflicts` with both full version payloads and the version vectors. The admin dashboard shows a side-by-side diff (field by field for structured metadata, line-by-line for text fields). The admin can:
- Accept the local version (update the version vector to dominate the remote, re-broadcast)
- Accept the remote version (apply the remote update, update local version vector)
- Manually merge (edit the item to a new state that incorporates both changes, which becomes version N+1 on this node)

**Version divergence — catching-up nodes**: A node returning from offline requests the last N days of activities from each partner's `/outbox` endpoint, paginated backward from the current position to the node's last-known activity. Items that were deleted are tombstoned; items that were updated are applied in order. If any of these replayed activities conflict with local state (the node made edits during its offline period), those are flagged as conflicts using the standard version-vector mechanism.

**Trust cascade — quarantine workflow**: When a partner's `failed_signature_count` exceeds a configurable threshold OR when an admin manually flags a partner, the partner transitions to a new `quarantined` state (extending the current `trust_status` enum). Activities from quarantined partners are stored in the `activities` table with a `quarantine: true` flag but are not applied to item state. An admin reviews the quarantine queue and either applies activities individually, bulk-applies all, or bulk-discards all and revokes the partner. The retroactive audit tool queries `activities WHERE partner_id = X AND applied = TRUE` to enumerate all past contributions from a partner under review.

**Split-brain recovery**: When federation partners reconnect after a partition, the reconnecting node's outbox activity log is paginated and all partition-period activities are re-delivered. The receiving node processes each with the standard version-vector conflict detection. The expected outcome: most items have no conflict (edited on only one side); some items have genuine conflicts that go to admin review.

**Rollback**: Admin selects an item and a target version from the event log. The system reconstructs the item state at that version from the event log entries. A new `Update` activity is generated with the reconstructed content and version vector {local_node: current+1}. This is broadcast to all trusted partners. Partners apply it normally (it dominates any non-quarantined earlier version). A `rollback_reason` field in the activity metadata labels it in the activity log.

---

### 3.4 Operational Procedures

**New node joining the federation**:
1. Admin on new node registers existing nodes as partners (POST `/admin/federation/partners/register` per Phase 4 design).
2. New node enters `pending` trust state on existing nodes.
3. Admin on an existing node reviews the new node and upgrades to `trusted`.
4. New node optionally requests a bootstrap snapshot from a trusted partner: POST `/admin/federation/bootstrap-from/{partner_id}`. Partner generates a point-in-time JSON-LD export of its public content corpus. New node imports it, setting version vectors to reflect the partner's last-known state.
5. New node begins receiving and sending activities normally. Gaps between bootstrap snapshot and current state are filled via outbox pagination.

**Node leaving the federation**:
1. Admin posts a signed `Unfollow` activity to all partners with `data-export-available: true` flag.
2. Node's trust state is transitioned to `revoked` on all partners (preventing further activity delivery).
3. Partner nodes retain items received from the departing node (they are part of the corpus now). A `source-node-offline` flag is added to those items' metadata.
4. Departing node runs an export and makes it available for 90 days.

**Network partition — during partition**:
- Each node operates independently. No special handling required. Items are created, edited, and endorsed normally.
- Delivery failures to unreachable partners are logged in the activity delivery retry queue.

**Network partition — on healing**:
1. Partner reconnects; signature handshake succeeds.
2. Both nodes re-deliver all failed activities from the retry queue.
3. Each node runs version-vector conflict detection on all received updates.
4. Conflicts are queued for admin review.
5. If the number of conflicts exceeds a configurable threshold (e.g., > 50 items), the admin receives a "partition reconciliation" notification with a summary before review begins.

---

### 3.5 Success Metrics

| Metric | Phase 5 Target | Phase 6 Target |
|---|---|---|
| Convergence time after reconnect | All non-conflicting items synced within 5 minutes of reconnect | All items synced within 60 seconds (Merkle anti-entropy) |
| Conflict detection accuracy | 100% of concurrent edits flagged (no silent discards) | Same |
| Data durability — Byzantine fault | Cannot guarantee (no BFT quorum); quarantine + audit reduces blast radius | Provenance chains limit 1-hop propagation |
| Scalability — convergence latency | <60 seconds for sync lag at N=10 nodes | <30 seconds at N=50 nodes |
| Admin review queue | Conflicts surfaced with full diff view | Conflicts auto-prioritized by severity (content vs. metadata) |
| Rollback capability | Any item reverted to any version in event log within 5 minutes | Same, with cross-node propagation confirmation |
| New node bootstrap time | <30 minutes for corpus import + catch-up at 10,000 items | <5 minutes (Merkle delta sync) |

---

## Part 4: References and Precedents

### Academic Foundations

**CRDTs — Shapiro et al. (2011)**: The foundational papers are "Conflict-free Replicated Data Types" and "A comprehensive study of Convergent and Commutative Replicated Data Types" by Marc Shapiro, Nuno Preguiça, Carlos Baquero, and Marek Zawirski (INRIA, 2011). The papers formalize both state-based (CvRDT) and operation-based (CmRDT) approaches and describe concrete CRDT implementations for sets, counters, maps, and graphs. Available at the [INRIA HAL repository](https://inria.hal.science/inria-00609399v2/document) and [Springer](https://link.springer.com/chapter/10.1007/978-3-642-24550-3_29). The key insight for open-repo: CRDTs are ideal for counters (endorsement counts, which are naturally commutative and associative) and less ideal for rich text or structured metadata (where semantic conflicts require human judgment).

**Raft consensus — Ongaro & Ousterhout (2014)**: "In Search of an Understandable Consensus Algorithm" (USENIX ATC 2014) at [raft.github.io](https://raft.github.io/). Raft's leader-election model produces strong consistency at the cost of availability during leader unavailability. For open-repo's voluntary, asynchronous federation, Raft's quorum requirement is architecturally incompatible — a 5-node Raft cluster that loses 3 nodes stops accepting writes, which is unacceptable for independent federation nodes. Raft is the right choice for internal cluster coordination within a single organization's multi-node deployment, not for cross-organization federation.

**Vector clocks — Lamport (1978), Fidge (1988), Mattern (1989)**: Vector clocks were first described by Lamport ("Time, Clocks, and the Ordering of Events in a Distributed System," 1978) and extended to version vectors by Fidge and Mattern independently. The [Wikipedia article on Vector clocks](https://en.wikipedia.org/wiki/Vector_clock) provides a solid introduction. For practical distributed database use, see Amazon's Dynamo paper (DeCandia et al., 2007, available via [ACM Digital Library](https://dl.acm.org/doi/10.1145/1294261.1294281)), which uses version vectors to detect conflicts and returns all conflicting versions to the application layer.

**Merkle trees for anti-entropy — Cassandra documentation**: Cassandra's use of Merkle trees for anti-entropy repair is documented in the [official Cassandra architecture docs](https://cassandra.apache.org/doc/3.11/cassandra/architecture/dynamo.html). The repair process computes Merkle tree roots over token ranges and recursively descends to find diverged leaves, then exchanges only the differing data. Directly applicable to open-repo's corpus comparison problem.

**Merkle Search Trees for CRDT replication — Auvolat & Taïani (2020)**: "Merkle Search Trees: Efficient State-Based CRDTs in Open Networks" shows how Merkle trees can be used as the backing structure for state-based CRDT synchronization, providing O(log N) state comparison and efficient delta extraction. Available at [ResearchGate](https://www.researchgate.net/publication/340304230_Merkle_Search_Trees_Efficient_State-Based_CRDTs_in_Open_Networks).

### Real-World System Precedents

**Wikipedia's concurrent edit handling**: Wikipedia detects conflicts by comparing the `baseRevId` (the revision the editor started from) against the current revision ID at save time. If they differ, the editor is shown a diff and must manually merge. Wikipedia does not automatically merge concurrent edits. The ORES system (now Lift Wing) scores incoming edits for probable vandalism before they are applied to the visible article, providing a lightweight staging layer analogous to the quarantine mode proposed for open-repo. See [Wikimedia Research — Knowledge Integrity](https://research.wikimedia.org/knowledge-integrity.html).

**Git's 3-way merge algorithm**: Git's merge strategy uses the common ancestor of two branches and applies both sets of changes relative to that ancestor. Non-overlapping changes merge automatically; overlapping changes generate conflict markers. The [git merge strategies documentation](https://git-scm.com/docs/merge-strategies) describes the `ort` (default since Git 2.33) and `recursive` strategies. The critical insight for open-repo: storing a common ancestor pointer (the CID of the last mutually-acknowledged version) is what makes 3-way merge possible. Without it, you can only do 2-way merge (compare current versions directly), which produces more conflicts because you cannot tell whether a difference represents a change on one side or both.

**IPFS content addressing and Merkle DAGs**: IPFS uses content-addressed Merkle DAGs where each node's CID is the cryptographic hash of its content. Two nodes holding identical content will have identical CIDs regardless of how they acquired it. The [IPFS Merkle DAG documentation](https://docs.ipfs.tech/concepts/merkle-dag/) explains how this property enables efficient deduplication and integrity verification. For open-repo: items with the same content but different provenance paths can be detected as duplicates via CID comparison, enabling the `sameAs` relationship without conflict.

**Matrix State Resolution Algorithm**: The Matrix homeserver protocol independently implements a consensus algorithm that all participating servers execute on partially ordered state events to converge on identical room state. State Resolution v2 (implemented since 2019) protects against state resets where delayed federation traffic could cause key-value state to revert to an earlier state. The [Matrix State Resolution documentation](https://matrix.org/docs/older/stateres-v2/) and the [academic analysis (arXiv 1910.06295)](https://arxiv.org/pdf/1910.06295) are the best references for how a federated protocol handles the split-brain problem without requiring a central coordinator. Project Hydra (2025) is further improving state resolution efficiency. This is the closest architectural precedent to what open-repo needs for split-brain reconciliation.

**Cassandra gossip and anti-entropy repair**: Cassandra's gossip protocol exchanges cluster state information in O(log N) rounds, and its anti-entropy repair compares Merkle tree roots between replica pairs to detect and fix divergences. The [Cassandra architecture documentation](https://cassandra.apache.org/doc/3.11/cassandra/architecture/dynamo.html) and the [Scott Logic analysis](https://blog.scottlogic.com/2017/10/06/cassandra-eventual-consistency.html) explain both mechanisms. Key lesson: Cassandra uses gossip for metadata propagation and Merkle trees for data integrity — these are complementary, not competing mechanisms.

**ActivityPub and URL canonicity**: The ActivityPub specification (W3C Recommendation, 2018) at [https://www.w3.org/TR/activitypub/](https://www.w3.org/TR/activitypub/) handles identity conflicts through URL canonicity: an ActivityPub object is identified by its URL, and that URL belongs to the domain that published it. This is a simple but effective conflict avoidance strategy: Node A cannot "conflict" with Node B's content because each node's content is canonical under its own domain. Conflicts arise only for mutually-owned or jointly-edited content — which open-repo supports through the content endorsement and contribution model.

**DNS hierarchical delegation**: DNS's authority model is instructive as a federation precedent: a parent zone delegates authority for a subdomain to a child zone's nameservers, and that delegation is propagated via cached NS records with TTL-based expiry. The zone transfer mechanism (AXFR/IXFR) enables a secondary nameserver to synchronize with a primary — IXFR in particular transfers only the incremental changes since a known serial number, which is a simple form of the delta-sync problem. See [DNS delegation concepts](https://www.catchpoint.com/dns-monitoring/dns-delegation). The analogy to open-repo: each node is authoritative for the content it originated; other nodes can mirror (with permission) but the originating node's version is canonical, exactly as a secondary DNS server's zone copy is authoritative only in absence of the primary.

### Implementation Libraries

- **Automerge**: [github.com/automerge/automerge](https://github.com/automerge/automerge) — JSON CRDT in Rust with Python/JS bindings. Most applicable to open-repo's endorsement counters and tag lists.
- **Yjs**: [github.com/yjs/yjs](https://github.com/yjs/yjs) — Text-optimized CRDT. Relevant if open-repo adds collaborative text editing to wiki articles.
- **activitypub-federation-rust (Lemmy)**: [github.com/LemmyNet/activitypub-federation-rust](https://github.com/LemmyNet/activitypub-federation-rust) — High-level ActivityPub federation library that handles inbox/outbox mechanics, idempotency, and retry. Worth evaluating as a replacement for the hand-rolled Phase 4 implementation as the federation grows.
- **merkle-search-tree (Rust)**: [github.com/domodwyer/merkle-search-tree](https://github.com/domodwyer/merkle-search-tree) — An implementation of Merkle Search Trees for efficient CRDT state synchronization. Directly applicable to the Phase 6 anti-entropy implementation.

---

## Phase 5 Implementation Sequence

Based on this analysis, Phase 5 conflict resolution work should proceed in three increments:

**Increment 5A (prerequisite — implement first)**:
- Replace integer `version` field with version vectors on the `items` table
- Add event log table (append-only, records all item state changes)
- Update version-vector conflict detection in the `/inbox` handler
- Enhance `content_conflicts` table with diff storage (both full versions + version vectors)
- Admin diff view for conflict review

**Increment 5B (core conflict management)**:
- Add `quarantined` state to `federation_partners` trust state machine
- Quarantine queue UI (review, apply, discard, bulk-revoke)
- Rollback tool: event-log-based version reconstruction + Update activity broadcast
- Bootstrap snapshot endpoint: `GET /federation/corpus-snapshot` (paginated JSON-LD export)
- Catching-up node outbox replay (bounded 30-day window)

**Increment 5C (partition recovery)**:
- Partition detection: track last-successful-contact per partner; alert after configurable gap
- Reconnect reconciliation workflow: re-deliver retry queue + version-vector conflict sweep
- Admin partition-recovery summary notification
- Integration tests: Docker-based partition simulation (iptables split + heal)

Increment 5C's Merkle anti-entropy (background corpus comparison) is scoped to Phase 6, as it requires the corpus to be large enough that per-item comparison becomes infeasible.

---

## Sources

1. [Conflict-free Replicated Data Types — Shapiro et al., INRIA 2011](https://inria.hal.science/inria-00609399v2/document)
2. [About CRDTs — crdt.tech](https://crdt.tech/)
3. [Automerge — GitHub](https://github.com/automerge/automerge)
4. [Yjs — GitHub](https://github.com/yjs/yjs)
5. [Raft Consensus Algorithm — raft.github.io](https://raft.github.io/)
6. [CAP Theorem Explained — PingCAP](https://www.pingcap.com/article/understanding-cap-theorem-basics-in-distributed-systems/)
7. [Vector Clock — Wikipedia](https://en.wikipedia.org/wiki/Vector_clock)
8. [Version Vectors in Distributed Systems — Educative](https://www.educative.io/courses/distributed-systems-practitioners/version-vectors)
9. [Amazon Dynamo Paper — DeCandia et al., 2007 (via ACM)](https://dl.acm.org/doi/10.1145/1294261.1294281)
10. [Cassandra Architecture: Dynamo](https://cassandra.apache.org/doc/3.11/cassandra/architecture/dynamo.html)
11. [Anti-Entropy in Distributed Systems — GeeksforGeeks](https://www.geeksforgeeks.org/system-design/anti-entropy-in-distributed-systems/)
12. [Merkle Trees and Anti-Entropy — Deep Engineering Substack](https://deepengineering.substack.com/p/merkle-trees-and-anti-entropy-concepts)
13. [Merkle Search Trees: Efficient State-Based CRDTs — ResearchGate](https://www.researchgate.net/publication/340304230_Merkle_Search_Trees_Efficient_State-Based_CRDTs_in_Open_Networks)
14. [merkle-search-tree Rust implementation — GitHub](https://github.com/domodwyer/merkle-search-tree)
15. [IPFS Merkle DAG documentation](https://docs.ipfs.tech/concepts/merkle-dag/)
16. [Matrix State Resolution v2 — matrix.org](https://matrix.org/docs/older/stateres-v2/)
17. [A Glimpse of the Matrix (Extended Version) — arXiv 1910.06295](https://arxiv.org/pdf/1910.06295)
18. [Project Hydra: Improving state resolution in Matrix — matrix.org](https://matrix.org/blog/2025/08/project-hydra-improving-state-res/)
19. [Git merge strategies documentation](https://git-scm.com/docs/merge-strategies)
20. [The Magic of 3-Way Merge — blog.git-init.com](https://blog.git-init.com/the-magic-of-3-way-merge/)
21. [Byzantine Fault Tolerance — GeeksforGeeks](https://www.geeksforgeeks.org/system-design/byzantine-fault-tolerance-in-distributed-system/)
22. [Byzantine fault — Wikipedia](https://en.wikipedia.org/wiki/Byzantine_fault)
23. [ActivityPub W3C Specification](https://www.w3.org/TR/activitypub/)
24. [Gossip Protocol — Wikipedia](https://en.wikipedia.org/wiki/Gossip_protocol)
25. [Gossip Protocols in Distributed Systems: Membership, Failure Detection, and Anti-Entropy — letsbuildsolutions.com](https://letsbuildsolutions.com/blog/system-design/gossip-protocols-in-distributed-systems-membership-failure-detection-and-anti-entropy-at-scale/)
26. [DNS Delegation: Concepts and Best Practices — Catchpoint](https://www.catchpoint.com/dns-monitoring/dns-delegation)
27. [Wikimedia Research — Knowledge Integrity (ORES/Lift Wing)](https://research.wikimedia.org/knowledge-integrity.html)
28. [activitypub-federation-rust — LemmyNet/GitHub](https://github.com/LemmyNet/activitypub-federation-rust)
29. [Cassandra Eventual Consistency — Scott Logic](https://blog.scottlogic.com/2017/10/06/cassandra-eventual-consistency.html)
